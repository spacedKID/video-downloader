# 🎞️ Video Downloader CLI

A Python-based command-line tool for downloading high-quality `.mp4` videos from a list of URLs in a CSV file. Built for macOS with sensible defaults and Finder preview compatibility.

---

## ✅ Features

- Downloads highest-quality AVC-encoded `.mp4` videos for macOS compatibility
- Handles login-restricted videos via `~/cookies.txt`
- Graceful error handling and retry logic
- Timestamped log files stored in `~/Library/Logs/video-downloader/`
- Simple CLI interface

---

## 💻 Installation & Use (macOS)

This project uses [`uv`](https://github.com/astral-sh/uv), a modern, Rust-based Python package and environment manager.

### 1. Clone the repo

```bash
git clone https://github.com/YOUR-USERNAME/video-downloader.git
cd video-downloader
```

### 2. 📦 Set up the environment with uv

```uv venv
source .venv/bin/activate
uv pip install pip  # ensures pip is available
pip install -e .
```


### 3. 📦 Dependencies

Dependencies are listed in `pyproject.tom` and fully locked in `uv.lock`.

To update the lockfile after changing dependencies:

```
uv pip compile pyproject.toml > uv.lock
```

### 4. 🚀 Usage
```
video-downloader path/to/urls.csv
```

### 🔐 Optional: Login-Protected Videos

If a video requires authentication, place your cookies export at:

`~/cookies.txt`

The tool will automatically retry failed downloads using this file when login is required.

### 📁 Logs

Each run creates a timestamped log file at:

`~/Library/Logs/video-downloader/video_downloader_YYYY-MM-DD_HHMMSS.log`