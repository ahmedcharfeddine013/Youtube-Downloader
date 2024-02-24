import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        finish.configure(text="Download error!")
    finish.configure(text="Downloaded!")

def on_progress(stream, chunk , bytes_remaining) : 
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()

    progressBar.set(float(percentage_of_completion) / 100)

# system settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

# Adding ui elements

title = customtkinter.CTkLabel(app, text="Inser a youtube link")
title.pack(padx=10, pady=10)

# Link input

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finish = customtkinter.CTkLabel(app, text="")
finish.pack()

# progress %

progress = customtkinter.CTkLabel(app, text='0%')
progress.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx = 10, pady =10)

# Download button

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app

app.mainloop()
