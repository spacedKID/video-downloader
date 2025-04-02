# 🎞️ Video Downloader CLI

A Python-based command-line tool for downloading high-quality `.mp4` videos from a list of URLs in a CSV file. Built for macOS with sensible defaults and Finder preview compatibility.

---

## 📚 Table of Contents
- [Features](#-features)
- [Installation & Use](#-installation--use-macos)
- [Usage](#-usage)
- [Logs](#-logs)
- [Login-Protected Videos](#-login-protected-videos)
- [Optional Dependencies](#-optional-dependencies)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✅ Features

- Downloads highest-quality AVC-encoded `.mp4` videos for macOS compatibility.
- Handles login-restricted videos via `~/cookies.txt`.
- Graceful error handling and retry logic.
- Timestamped log files stored in `~/Library/Logs/video-downloader/`.
- Simple CLI interface.

---

## 💻 Installation & Use (macOS)

This project uses [`uv`](https://github.com/astral-sh/uv), a modern, Rust-based Python package and environment manager.

### 1. Clone the repo
Obtain a copy of the repository and enter its root directory.

```bash
git clone https://github.com/spacedKID/video-downloader.git
cd video-downloader
```

### 2. 📦 Set up the environment with uv
Create and activate a virtual environment for the project. Then install the package as a shell command.

```bash
uv venv
source .venv/bin/activate
uv pip install pip
uv pip install --uv-lock uv.lock
pip install -e .
```

### 3. 🚀 Usage
Call the function, provide the path to URLs, and (optionally) pass a directory path for the downloaded videos.

```bash
video-downloader path/to/urls.csv (path/to/saved/videos)
```

**Format note**: The input CSV format is simple: no header, simply one column of URLs.

---

## 📁 Logs
Each run creates a timestamped log file in the user Library/Logs directory as:

```
~/Library/Logs/video-downloader/video_downloader_YYYY-MM-DD_HHMMSS.log
```

---

## 🔐 Login-Protected Videos
Some video files require authentication to a remote server for download. The [yt-dlp FAQ](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp) provides context for this need.

If a video requires authentication, place your cookies export at: `~/cookies.txt`. The tool will automatically retry failed downloads using this file when login is required.

---

## 📦 Optional Dependencies
(This step is only required should you install additional software and need to update the repository.)

Dependencies are listed in `pyproject.toml` and fully locked in `uv.lock`.

To update the lockfile after changing dependencies:

```bash
uv pip compile pyproject.toml > uv.lock
```

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
