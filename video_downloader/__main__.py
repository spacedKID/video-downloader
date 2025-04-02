import csv
import sys
import yt_dlp

def download_videos(csv_path):
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            urls = [row[0] for row in reader if row]

        if not urls:
            print("No URLs found in the CSV file.")
            return

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for url in urls:
                print(f"\nDownloading: {url}")
                ydl.download([url])

    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m video_downloader path/to/file.csv")
        sys.exit(1)

    csv_path = sys.argv[1]
    download_videos(csv_path)

if __name__ == "__main__":
    main()
