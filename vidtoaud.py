from tkinter import Tk, Button
import moviepy.editor as mp
import os
import re
from tkinter.filedialog import askdirectory
from tkinter import messagebox

root = Tk()
root.title('Convert video to audio')
root.configure(background="dark green")
root.minsize(width=200,height=300)
root.resizable(width=False,height=False)

def open_video_folder():
    global video_directory
    video_directory=askdirectory()
    print(video_directory)

def open_audio_folder():
    global audio_directory
    audio_directory=askdirectory()
    print(audio_directory)


def convert():
    for file in [n for n in os.listdir(video_directory) if re.search('.mp4',n)]:
        full_path = os.path.join(video_directory,file)
        output_path = os.path.join(audio_directory, os.path.splitext(file)[0]+ '.mp3')
        audioclip = mp.AudioFileClip(full_path)
        audioclip.write_audiofile(output_path)
        messagebox.showinfo("Complete", "Successfully converted from video to audio")


video_button = Button(root,text="Click on Video", width=25, command=open_video_folder, bg="blue",fg="white")
video_button.grid(row=1,column=0,pady=35,padx=35)

audio_button = Button(root,text="Click on Audio", width=25, command=open_audio_folder, bg="blue",fg="white")
audio_button.grid(row=2,column=0,pady=35,padx=35)

convert_button = Button(root,text="Convert", width=25, command=convert, bg="blue",fg="white")
convert_button.grid(row=3,column=0,pady=35,padx=35)

exit_button = Button(root,text="Exit", width=25, command=root.destroy,bg="blue",fg="white")
exit_button.grid(row=4,column=0,pady=35,padx=35)


root.mainloop()
