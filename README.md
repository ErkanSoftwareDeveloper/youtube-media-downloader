#  YouTube Media Downloader

A simple and lightweight **YouTube to MP3 downloader desktop application** built with **Python** and **Tkinter**.
Easily download YouTube videos as MP3 files directly to your computer.

---

##  Features

* Download YouTube videos as MP3
* Automatically convert to 192 kbps MP3
* Choose output folder (`downloads/`)
* Simple and clean user interface
* Fast and reliable downloading

---

##  Technologies Used

* **Python 3**
* **Tkinter** – GUI framework
* **yt-dlp** – YouTube video downloader
* **FFmpeg** – for audio conversion

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/ErkanSoftwareDeveloper/youtube-media-downloader.git
cd youtube-media-downloader
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure **FFmpeg** is installed and added to your system PATH.

---

##  Usage

Run the application:

```bash
python Youtube_Downloader.py
```

1. Enter the YouTube video URL
2. Click **Download MP3**
3. The MP3 file will be saved in the `downloads/` folder
4. Check success or error messages via popup dialogs

---

##  Project Structure

```text
youtube-media-downloader/
├─ Youtube_Downloader.py   # Main application file
├─ downloads/              # Folder for downloaded MP3s
├─ .gitignore              # Git ignored files
├─ README.md               # Project documentation
└─ requirements.txt        # Project dependencies
```

---

##  Video

![2026-01-1115-56-59-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/2ce94531-b61e-4dba-aad3-d2e00d1cd33d)


---

##  Possible Improvements

* Support for playlists
* Option to choose audio quality
* MP4 video download option
* Progress bar during download
* Dark / light theme
* Packaging as executable (.exe)

---

##  License

This project is intended for **educational and personal use**.
