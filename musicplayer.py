from lib2to3.pgen2.token import LEFTSHIFT
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os
from numpy import pad
from pygame import *
import pygame
win=Tk()
win.title("ESS Music Player")
win.geometry("1000x570+100+70")
win.resizable(False,False)
icon=PhotoImage(file="icons/music.png")
win.iconphoto(False,icon)


# colors========================
col1="#3E4095"
col2="#333333"
col3="#80d4ff"
# ==============================
icond=20
# fonts=========================
font1=("times",11,"bold")
font2=("times",11)
# ==============================
# images and icons==============
mainimg=Image.open("icons/ui.png")
mainimg=mainimg.resize((200,200))
mainimg=ImageTk.PhotoImage(mainimg)
iconprev=Image.open("icons/prevplay.png")
iconprev=iconprev.resize((icond,icond))
iconprev=ImageTk.PhotoImage(iconprev)
iconplay=Image.open("icons/play.png")
iconplay=iconplay.resize((icond,icond))
iconplay=ImageTk.PhotoImage(iconplay)
iconnext=Image.open("icons/nextplay.png")
iconnext=iconnext.resize((icond,icond))
iconnext=ImageTk.PhotoImage(iconnext)
iconpause=Image.open("icons/pause.png")
iconpause=iconpause.resize((icond,icond))
iconpause=ImageTk.PhotoImage(iconpause)
iconunpause=Image.open("icons/continue.png")
iconunpause=iconunpause.resize((icond,icond))
iconunpause=ImageTk.PhotoImage(iconunpause)
iconstop=Image.open("icons/stop.png")
iconstop=iconstop.resize((icond,icond))
iconstop=ImageTk.PhotoImage(iconstop)
iconminus=Image.open("icons/minusvolume.png")
iconminus=iconminus.resize((15,15))
iconminus=ImageTk.PhotoImage(iconminus)
iconadd=Image.open("icons/addvolume.png")
iconadd=iconadd.resize((15,15))
iconadd=ImageTk.PhotoImage(iconadd)
iconmute=Image.open("icons/speakeroff.png")
iconmute=iconmute.resize((15,15))
iconmute=ImageTk.PhotoImage(iconmute)
iconunmute=Image.open("icons/speakeron.png")
iconunmute=iconunmute.resize((15,15))
iconunmute=ImageTk.PhotoImage(iconunmute)
# ==============================

win.config(bg=col1)

# functions=====================================
def play_music():
    running=mylist.get(ACTIVE)
    lblcurrentplaying.config(text=running)
    
    try:

        mixer.music.load(running)
        mixer.music.play()
        playing=lblcurrentplaying['text']
        index=songs.index(playing)
        
    except IOError:
        pass
    
    
def pause_music():
    mixer.music.pause()
def unpause_music():
    mixer.music.unpause()
def stop_music():
    mixer.music.stop()
def next_music():
    playing=lblcurrentplaying['text']
    index=songs.index(playing)
    new_index=index+1
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    mylist.delete(0,END)
    show()
    mylist.select_set(new_index)
    lblcurrentplaying['text']=playing
def prev_music():
    playing=lblcurrentplaying['text']
    index=songs.index(playing)
    new_index=index-1
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    mylist.delete(0,END)
    show()
    mylist.select_set(new_index)
    lblcurrentplaying['text']=playing
curvolume=1
def addvolume():
    global curvolume
    if curvolume>=1:
        pass
    else:
        curvolume=curvolume+0.05
        mixer.music.set_volume(curvolume)
def minusvolume():
    global curvolume
    if curvolume<=0:
        pass
    else:
        curvolume=curvolume-0.05
        mixer.music.set_volume(curvolume)
mute=0
def speakerstatus():
    global mute,curvolume
    if mute==0:
        mixer.music.set_volume(0)
        mute=1
        btntogglemute.config(image=iconmute)
    elif mute==1:
        mixer.music.set_volume(curvolume)
        mute=0
        btntogglemute.config(image=iconunmute)
    else:
        mixer.music.set_volume(curvolume)
        btntogglemute.config(image=iconunmute)
def loadmusic():
    myfolder=filedialog.askdirectory(initialdir="",title="Select folder to load music")
    os.chdir(myfolder)
    songs=os.listdir()
    def show1():
        for i in songs:
            if i.endswith(".mp3"):
                mylist.insert(END,i)
    show1()
def clearmylist():
    mylist.delete(0,END)
    stop_music()
def loadnext():
    playing=lblcurrentplaying['text']
    index=songs.index(playing)
    new_index=index+1
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()
    print(index)
    mylist.delete(0,END)
    show()
    mylist.select_set(new_index)
    lblcurrentplaying['text']=playing
# ==============================================

mainframe=Frame(win,bg=col3)
mainframe.place(x=0,y=0,relwidth=1,relheight=1)
framephoto=Frame(mainframe,bg=col3)
framephoto.grid(column=0,row=0)
lblimg=Label(framephoto,image=mainimg,width=400,height=400,bg=col3,bd=0)
lblimg.pack(expand=True,fill=BOTH,padx=10,pady=13)
frameformylist=Frame(mainframe,width=600,height=400,bg=col2,bd=0)
frameformylist.grid(column=1,row=0)
framefiltermusic=Frame(frameformylist,bg=col2)
framefiltermusic.pack(side=TOP,fill=X,pady=(4,0))
Label(framefiltermusic,text="Search",font=font1,bg=col2,fg=col3).pack(side=LEFT,pady=5)
textfilter=Entry(framefiltermusic,font=font2,bd=2,borderwidth=3)
textfilter.pack(side=LEFT,fill=X,padx=(50,2),pady=5)
Button(framefiltermusic,text="X",bg=col1,fg=col3,font=font1,width=6,bd=0,cursor="hand2").pack(side=LEFT,pady=5)
mylistframe=Frame(frameformylist,bd=0)
mylistframe.pack(side=TOP,fill=X)
mylist=Listbox(mylistframe,height=21,font=font2,fg="aliceblue",width=80,bg=col2,bd=0,activestyle=None)
mylist.pack(side=LEFT,fill=BOTH,expand=True)
myscrollbar=Scrollbar(mylistframe,orient="vertical",command=mylist.yview,bg=col2)
myscrollbar.pack(side=LEFT,fill=Y)
mylist.config(yscrollcommand=myscrollbar.set)
framebtn1=Frame(frameformylist,bg=col2)
framebtn1.pack(side=TOP,fill=X,expand=True)
framebtn11=Frame(framebtn1,bg=col2)
framebtn11.pack(pady=2)
btnload=Button(framebtn11,text="Load Music",width=10,height=1,fg=col2,font=font1,cursor="hand2",bd=0,bg=col3,command=loadmusic)
btnload.pack(padx=4,side=LEFT)
btnclear=Button(framebtn11,text="Clear",width=10,height=1,fg=col2,font=font1,cursor="hand2",bd=0,bg=col3,command=clearmylist)
btnclear.pack(padx=4,side=LEFT)


framecontrols=Frame(mainframe,bg=col3)
framecontrols.grid(column=0,row=1,columnspan=2)
lblcurrentplaying=Label(framecontrols,width=110,text="Choose Music",font=font1,justify=LEFT)
lblcurrentplaying.pack(side=TOP,fill=X)

framebtn2=Frame(framecontrols,bg=col3)
framebtn2.pack(side=TOP,fill=X)
btnframecontrol1=Frame(framebtn2,bg=col3)
btnframecontrol1.pack(side=LEFT,pady=(15,5))
btnprev=Button(btnframecontrol1,image=iconprev,bd=1,cursor="hand2",command=prev_music)
btnprev.grid(column=0,row=0,padx=6,pady=4)
btnplay=Button(btnframecontrol1,image=iconplay,bd=1,cursor="hand2",command=play_music)
btnplay.grid(column=1,row=0,padx=6,pady=4)
btnnext=Button(btnframecontrol1,image=iconnext,bd=1,cursor="hand2",command=next_music)
btnnext.grid(column=2,row=0,padx=6,pady=4)
btnpause=Button(btnframecontrol1,image=iconpause,bd=1,cursor="hand2",command=pause_music)
btnpause.grid(column=3,row=0,padx=6,pady=4)
btnunpause=Button(btnframecontrol1,image=iconunpause,bd=1,cursor="hand2",command=unpause_music)
btnunpause.grid(column=4,row=0,padx=6,pady=4)
btnstop=Button(btnframecontrol1,image=iconstop,bd=1,cursor="hand2",command=stop_music)
btnstop.grid(column=5,row=0,padx=6,pady=4)
myscale=Scale(framebtn2,orient=HORIZONTAL)
myscale.pack(pady=(15,5))
btnframevolume1=Frame(framebtn2,bg=col3)
btnframevolume1.pack(side=RIGHT)
btntogglemute=Button(btnframevolume1,image=iconunmute,bd=0,cursor="hand2",command=speakerstatus)
btntogglemute.grid(column=0,row=0,padx=10)
btnminus=Button(btnframevolume1,image=iconminus,bd=0,cursor="hand2",command=minusvolume)
btnminus.grid(column=1,row=0)
lbvolume=Label(btnframevolume1,text="volume",bg=col3)
lbvolume.grid(column=2,row=0)
btnadd=Button(btnframevolume1,image=iconadd,bd=0,cursor="hand2",command=addvolume)
btnadd.grid(column=3,row=0)

os.chdir(r'C:\Users\Eric\Music')
songs=os.listdir()
def show():
    for i in songs:
        if i.endswith(".mp3"):
            mylist.insert(END,i)
show()

mixer.init()
music_state=StringVar()
music_state.set("choose1")
win.mainloop()