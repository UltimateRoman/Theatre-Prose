import csv
from tkinter import *
from threading import Thread
from playsound import playsound
from utils import get_plays, get_players, get_lines


modes = ["Single-Player", "Multi-Player"]
plays = get_plays()
players = []
lines = []

selectedPlay = None
selectedMode = modes[0]
selectedPlayer = None

window = Tk()
bg = PhotoImage(file = "assets/bg.png")
bg = bg.subsample(2, 2)
bphoto1 = PhotoImage(file = "assets/start.png")
nxt = PhotoImage(file = "assets/next.png")
nxtimg = nxt.subsample(40, 40)
bimage1 = bphoto1.subsample(6, 8)

window.title("Theatre Pros(e)")
window.resizable(False, False)
window.geometry('876x540')
frame1 = Frame(window)
Label(frame1, image=bg).place(bordermode=INSIDE)
Label(frame1, bg="red4", fg="white", text="Theatre Pros(e)", font=("times", 40, "bold")).place(x=250, y=70)
frame1.pack(fill="both", expand=True)
frame2 = None
count = 0

def startPlay():
    global lines, frame2, count
    frame1.destroy()
    frame2 = Frame(window)
    Label(frame2, image=bg).place(bordermode=INSIDE)    
    frame2.pack(fill="both", expand=True)
    Button(frame2, image=nxtimg, command=nextLine).place(x=820, y=460)
    lines = get_lines(selectedPlay, selectedPlayer) 
    Label(frame2, bg="red4", fg="white", text=lines[count]['Play'], font=("Times", 30)).place(x=250, y=75)
    Label(frame2, fg="black", text=lines[count]['Player'], font=("roboto", 20)).place(x=300, y=300)
    Label(frame2, fg="black", text='"'+lines[count]['PlayerLine']+'"', font=("roboto", 18)).place(x=300, y=400)
    count = count + 1

def nextLine():
    global frame2, count, lines
    frame2.destroy()
    frame2 = Frame(window)
    Label(frame2, image=bg).place(bordermode=INSIDE)
    frame2.pack(fill="both", expand=True)
    Button(frame2, image=nxtimg, command=nextLine).place(x=820, y=460)
    if count < len(lines):
        Label(frame2, bg="red2", fg="white", text=lines[count]['Play'], font=("Times", 30, "bold")).place(x=250, y=75)
        Label(frame2, fg="black", text=lines[count]['Player'], font=("roboto", 20)).place(x=300, y=300)
        Label(frame2, fg="black", text='"'+lines[count]['PlayerLine']+'"', font=("roboto", 15)).place(x=300, y=400)
        count = count + 1
    else:
        if count == len(lines):
            Label(frame2, fg="black", text="SCORE", font=("Times", 30)).place(x=250, y=75)
            Label(frame2, fg="black", text=str(count)+" / "+str(count), font=("roboto", 40)).place(x=250, y=150)
            Label(frame2, fg="black", text="Standing Ovation!", font=("helvetica", 40)).place(x=250, y=230)
        else:
            playsound("assets/applause.mp3")
            window.destroy()        
        count = count + 1    

def selectMode(choice):
    global selectedMode
    selectedMode = choice

def selectPlay(choice):
    global selectedPlay
    selectedPlay = choice
    if selectedMode == modes[0]:
        displayPlayers()
    Button(frame1, text="Start Play", image=bimage1, command=startPlay).place(x=365, y=450)

def selectPlayer(choice):
    global selectedPlayer
    selectedPlayer = choice

def displayPlayers():
    global players
    players = get_players(selectedPlay)
    players_value = StringVar(frame1)
    players_value.set("Select a Player")
    players_menu = OptionMenu(frame1, players_value, *players, command=selectPlayer)
    players_menu.config(width=18, height=1, bg='royalblue1', fg="white", font=('Helvetica', 18, "bold"))
    players_menu.place(x=300, y=340)

def displayModes():
    modes_value = StringVar(frame1)
    modes_value.set("Select Mode")
    modes_menu = OptionMenu(frame1, modes_value, *modes, command=selectMode)
    modes_menu.config(width=15, height=1, bg='royalblue1', fg="white", font=('Helvetica', 18, "bold"))
    modes_menu.place(x=320, y=220)

def displayPlays():
    plays_value = StringVar(frame1)
    plays_value.set("Select a Play")
    plays_menu = OptionMenu(frame1, plays_value, *plays, command=selectPlay)
    plays_menu.config(width=20, height=1, bg='royalblue1', fg="white", font=('Helvetica', 18, "bold"))
    plays_menu.place(x=290, y=280)

def main():
    displayModes()
    displayPlays()
    window.mainloop()   


if __name__ == '__main__':
    main()

