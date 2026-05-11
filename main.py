from tkinter import *
from pytube import YouTube
root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("youtube Download by lean")
Label(root, text="youtube download", font="arial 20 bold").pack()
link=StringVar()
Label(root,text="past link Here: ",font="arial 15 bold").place(x =160,y =60)
link_enter=Entry(root,width=70,textvariable = link).place(x=32,y=90)
def hight():
    url= YouTube(str(link.get()))
    video= url.streams.get_highest_resolution()
    video.download()
    Label(root,text="Download!",font="arial 15 bold").place(x = 180 , y = 210)
Button(root, text="high Resulotion", font="arial 15 bold",bg="red", padx=2, command=hight).place(x =100 , y= 150)



def low():
    url= YouTube(str(link.get()))
    video= url.streams.get_lowest_resolution()
    video.download()
    Label(root,text="Download!",font="arial 15 bold").place(x = 180 , y = 210)
Button(root, text="low Resulotion", font="arial 15 bold",bg="blue", padx=2, command=hight).place(x =110 , y= 200)



def audio_only():
    url= YouTube(str(link.get()))
    video= url.streams.get_audio_only()
    video.download()
    Label(root,text="Download!",font="arial 15 bold").place(x = 180 , y = 210)
Button(root, text="Audio_only Resulotion", font="arial 15 bold",bg="green", padx=2, command=audio_only).place(x =280 , y= 200)

root.mainloop()
