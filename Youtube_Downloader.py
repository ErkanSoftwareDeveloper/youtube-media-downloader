import os
import yt_dlp                # Powerful library for downloading YouTube videos
import tkinter as tk         # Simple GUI library
from tkinter import messagebox  # For showing info/error dialogs

# --- Main download function ---


def download_as_mp3():
    url = entry.get()  # Get the YouTube URL entered by the user
    if not url:
        messagebox.showwarning("Warning", "Please enter a YouTube URL!")
        return  # If URL is empty, show warning and stop

    # Folder where downloaded MP3s will be saved
    output_folder = "downloads"
    # Create folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # yt-dlp options
    ydl_opts = {
        # Get best audio (prefer m4a)
        'format': 'bestaudio/best[ext=m4a]/best',
        # File name
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',   # Extract audio using FFmpeg
            'preferredcodec': 'mp3',       # Convert to MP3
            'preferredquality': '192',     # 192 kbps
        }],
        'extractor_args': {                # Bypass new YouTube protection
            'youtube': {'player_client': ['android']}
        },
        'quiet': True,  # Avoid unnecessary console output
    }

    # --- Download process ---
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "MP3 downloaded successfully! 🎶")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed: {str(e)}")


# --- Tkinter GUI ---
root = tk.Tk()
root.title("🎧 YouTube to MP3 Downloader")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

download_button = tk.Button(root, text="Download MP3", command=download_as_mp3)
download_button.pack(pady=10)

root.mainloop()
# --- End of code ---

