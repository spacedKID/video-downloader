import csv
import sys
import os
import yt_dlp
from yt_dlp.utils import DownloadError

def download_video(url, ydl_opts, fallback_opts):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except DownloadError as e:
        print(f"\nDownload failed for {url}: {e}")
        # Check for login requirement message
        if 'login' in str(e).lower() or 'account' in str(e).lower():
            print(f"Retrying {url} using cookies from ~/cookies.txt...")
            cookies_path = os.path.expanduser("~/cookies.txt")
            if os.path.exists(cookies_path):
                fallback_opts['cookiefile'] = cookies_path
                try:
                    with yt_dlp.YoutubeDL(fallback_opts) as ydl:
                        ydl.download([url])
                except DownloadError as e2:
                    print(f"Retry with cookies also failed: {e2}")
            else:
                print("No cookies file found at ~/cookies.txt.")
        else:
            print("Error not related to login — skipping.")

def download_videos(csv_path):
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            urls = [row[0] for row in reader if row]

        if not urls:
            print("No URLs found in the CSV file.")
            return

        ydl_opts = {
            'format': 'bv*[vcodec^=avc1]+ba/best[ext=mp4]',
            'merge_output_format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

        fallback_opts = ydl_opts.copy()

        for url in urls:
            print(f"\nDownloading: {url}")
            download_video(url, ydl_opts, fallback_opts)

    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: video-downloader path/to/file.csv")
        sys.exit(1)

    csv_path = sys.argv[1]
    download_videos(csv_path)

if __name__ == "__main__":
    main()
