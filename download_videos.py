import csv
import sys
import yt_dlp

def download_videos(csv_path):
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            urls = [row[0] for row in reader if row]  # Avoid empty rows

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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 download_videos.py download_videos path/to/file.csv")
        sys.exit(1)

    func_name, csv_path = sys.argv[1], sys.argv[2]

    if func_name != 'download_videos':
        print(f"Function '{func_name}' not found.")
        sys.exit(1)

    download_videos(csv_path)
