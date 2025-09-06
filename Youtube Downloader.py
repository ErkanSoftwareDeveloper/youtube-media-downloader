import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox

# os Dosya ve klaösor islemleri icin, mesela Downloads klasorunu olusturmka icin
# yt_dlp Youtube videolarini indirmek icin
# tkinter GUI icin (grafik arayüz)
# messagebox kullaniciya uyari ve hatali mesaj göstermek icin


def download_as_mp3():
    url = entry.get()  # Tkinter giris kutusundan linki aliyoruz
    if not url:
        messagebox.showwarning("Error", "Give me the Youtube Link")
        return
    # Eger link bossa kullaniya uyariyoruz

    output_folder = "downloads"
    os.makedirs(output_folder, exist_ok=True)
# indirilen MP3lerin kaydedilecegi klasör
#  exist_ok=True Klasör zaten varsa hata vermesin
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True, # konsolda fazla yazi cikmasin diye
    }

    # outtmpl: dosyanin kaydedilecegi klasör + video basligi
    # postprocessors : FFmpeg kullarak MP3 3 cevirme
    # messagebox. : Islem basarili,basarisiz mesaji

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"Download failed:\{str(e)}")


# --- Tkinter GUI olusturma ---
root = tk.Tk()
root.title("Youtube to MP3 Downloader")

tk.Label(root, text="Youtube Link:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

download_button = tk.Button(root, text="Download MP3", command=download_as_mp3)
download_button.pack(pady=10)

root.mainloop()