import csv
import sys
import os
import logging
from datetime import datetime
import yt_dlp
from yt_dlp.utils import DownloadError

# --------- Setup Logging ---------
def setup_logger():
    log_dir = os.path.expanduser("~/Library/Logs/video-downloader")
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    log_path = os.path.join(log_dir, f"video_downloader_{timestamp}.log")

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return log_path

# --------- Video Download Function ---------
def download_video(url, ydl_opts, fallback_opts, failed_urls):
    logging.info(f"Starting download for URL: {url}")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            logging.info(f"✅ Download successful: {info.get('title', 'unknown title')}")
    except DownloadError as e:
        logging.warning(f"Download failed: {url} | Error: {e}")
        if 'login' in str(e).lower() or 'account' in str(e).lower():
            logging.info(f"Retrying with cookies: {url}")
            cookies_path = os.path.expanduser("~/cookies.txt")
            if os.path.exists(cookies_path):
                fallback_opts['cookiefile'] = cookies_path
                try:
                    with yt_dlp.YoutubeDL(fallback_opts) as ydl:
                        info = ydl.extract_info(url, download=True)
                        logging.info(f"✅ Retry with cookies succeeded: {info.get('title', 'unknown title')}")
                        return
                except DownloadError as e2:
                    logging.error(f"Retry failed: {url} | Error: {e2}")
            else:
                logging.warning(f"No cookies file found at {cookies_path}")
        failed_urls.append(url)

# --------- Batch Download Entry Point ---------
def download_videos(csv_path, base_download_path=None):
    failed_urls = []
    log_path = setup_logger()
    logging.info("🎬 Starting batch download session")

    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            urls = [row[0] for row in reader if row]

        if not urls:
            logging.warning("No URLs found in CSV")
            print("No URLs found in the CSV file.")
            return

        # Set default download base path if none provided
        base_download_path = os.path.expanduser(base_download_path or "~/Desktop")

        # Generate timestamped subfolder name
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        download_dir = os.path.join(base_download_path, f"{timestamp} video-downloads")
        os.makedirs(download_dir, exist_ok=True)

        logging.info(f"Download destination: {download_dir}")

        ydl_opts = {
            'format': 'bv*[vcodec^=avc1]+ba/best[ext=mp4]',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        }

        fallback_opts = ydl_opts.copy()

        for url in urls:
            download_video(url, ydl_opts, fallback_opts, failed_urls)

        # Summary
        if failed_urls:
            logging.warning("Some downloads failed:")
            logging.warning("\n".join(failed_urls))
            print("\n⚠️ The following downloads failed:")
            for url in failed_urls:
                print(f" - {url}")
        else:
            logging.info("🎉 All downloads completed successfully.")
            print("\n✅ All downloads completed successfully.")

        print(f"\nDownloaded videos are saved to: {os.path.abspath(download_dir)}")
        print(f"Log saved to: {os.path.abspath(log_path)}")

    except FileNotFoundError:
        logging.critical(f"CSV file not found: {csv_path}")
        print(f"File not found: {csv_path}")
    except Exception as e:
        logging.critical(f"Critical error: {e}")
        print(f"A critical error occurred: {e}")

# --------- CLI Entry Point ---------
def main():
    args = sys.argv[1:]

    if not (1 <= len(args) <= 2):
        print("Usage: video-downloader path/to/urls.csv [optional-download-dir]")
        sys.exit(1)

    csv_path = args[0]
    download_path = args[1] if len(args) == 2 else None

    download_videos(csv_path, download_path)

if __name__ == "__main__":
    main()
