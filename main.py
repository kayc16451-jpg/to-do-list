import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_label.config(text=folder)

def download_video():
    url = url_entry.get().strip()
    download_path = path_label.cget("text")

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    if download_path == "No folder selected":
        messagebox.showerror("Error", "Please select a download folder")
        return

    try:
        status_label.config(text="Fetching video...", fg="blue")
        root.update()

        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        status_label.config(text="Downloading...", fg="blue")
        root.update()

        stream.download(download_path)

        status_label.config(text="Download completed!", fg="green")
        messagebox.showinfo("Success", f"Downloaded:\n{yt.title}")

    except Exception as e:
        status_label.config(text="Download failed", fg="red")
        messagebox.showerror("Error", str(e))

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("520x320")
root.configure(background='teal')
root.resizable(False, False)

tk.Label(
    root,
    text="YouTube Video Downloader",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="YouTube URL:").pack()

url_entry = tk.Entry(root, width=65)
url_entry.pack(pady=5)

tk.Button(
    root,
    text="Select Download Folder",
    command=browse_folder
).pack(pady=5)

path_label = tk.Label(root, text="No folder selected", fg="gray")
path_label.pack()

tk.Button(
    root,
    text="Download Video",
    bg="#E50914",
    fg="white",
    font=("Arial", 12),
    command=download_video
).pack(pady=15)

status_label = tk.Label(root, text="")
status_label.pack()


root.mainloop()
