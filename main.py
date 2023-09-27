import tkinter
import customtkinter
from pytube import YouTube
import pathlib

path = pathlib.Path.home() / "Downloads"

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        finishLabel.configure(text="")
        if ytObject is not None:
            video.download(path)
        finishLabel.configure(text="Download is finished", text_color="white")
        title.configure(text=ytObject.title, text_color="white")
    except:
        finishLabel.configure(text="Download Error", text_color="red")
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    precentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(precentage_of_completion))
    pPrecen.configure(text=per + '%')
    pPrecen.update()
    progressBar.set(float(precentage_of_completion) / 100)
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube download")

title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

pPrecen = customtkinter.CTkLabel(app, text="0%")
pPrecen.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=20,pady=20)

app.mainloop()