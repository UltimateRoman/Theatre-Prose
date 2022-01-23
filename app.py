import csv
from tkinter import *
from time import sleep
from threading import Thread
from playsound import playsound

plays = []
players = []
lines = []
modes = ["Single-Player", "Multi-Player"]

selectedPlay = None
selectedMode = modes[0]
selectedPlayer = None

window = Tk()
bg = PhotoImage(file = "assets/bg.png")
bg = bg.subsample(2, 2)
bphoto1 = PhotoImage(file = "assets/start.png")
bimage1 = bphoto1.subsample(5, 6)

window.title("Theatre Pros(e)")
window.resizable(False, False)
window.geometry('876x540')
frame1 = Frame(window)
Label(frame1, image=bg).place(bordermode=INSIDE)
Label(frame1, fg="black", text="Theatre Pros(e)", font=("roboto", 40)).place(x=250, y=70)
frame1.pack(fill="both", expand=True)
frame2 = None
count = 0

with open('./plays.csv', 'r') as data:
    for line in csv.DictReader(data):
        play = line['Play']
        if play not in plays:
            plays.append(play)

def startPlay():
    global lines, frame2, count
    frame1.destroy()
    frame2 = Frame(window)
    Label(frame2, image=bg).place(bordermode=INSIDE)
    Label(frame2, fg="black", text="Theatre Pros(e)", font=("roboto", 40)).place(x=250, y=70)
    frame2.pack(fill="both", expand=True)
    Button(frame2, text="Start Play", image=bimage1, command=nextLine).place(x=350, y=430)
    if selectedMode == modes[0]:
        with open('./plays.csv', 'r') as data:
            for line in csv.DictReader(data):
                if line['Play'] == selectedPlay and line['Player'] == selectedPlayer:
                    lines.append(line)
                    # print("Line " + line['PlayerLinenumber'] + " " + line['PlayerLine'])
                    # sleep(len(line['PlayerLine'])*0.14)
    else:
        with open('./plays.csv', 'r') as data:
            for line in csv.DictReader(data):
                if line['Play'] == selectedPlay:
                    lines.append(line)
                    # print("Line " + line['PlayerLinenumber'] + " Player: " + line['Player'] + " - " + line['PlayerLine'])
                    # sleep(len(line['PlayerLine'])*0.14)  
    # playsound("assets/applause.mp3")

def nextLine():
    global frame2, count, lines
    frame2.destroy()
    frame2 = Frame(window)
    Label(frame2, image=bg).place(bordermode=INSIDE)
    Label(frame2, fg="black", text="Theatre Pros(e)", font=("roboto", 40)).place(x=250, y=70)
    frame2.pack(fill="both", expand=True)
    Button(frame2, text="Start Play", image=bimage1, command=nextLine).place(x=350, y=430)
    if count < len(lines):
        Label(frame2, fg="black", text=lines[count]['PlayerLine'], font=("roboto", 20)).place(x=100, y=300)
        count = count + 1
    else:
        Label(frame2, fg="black", text="Standing Ovation", font=("roboto", 20)).place(x=100, y=300)
        playsound("assets/applause.mp3")

def selectMode(choice):
    global selectedMode
    selectedMode = choice

def selectPlay(choice):
    global selectedPlay
    selectedPlay = choice
    if selectedMode == modes[0]:
        displayPlayers()

def selectPlayer(choice):
    global selectedPlayer
    selectedPlayer = choice

def displayPlayers():
    global players
    players = []
    with open('./plays.csv', 'r') as data:
        for line in csv.DictReader(data):
            play = line['Play']
            if play == selectedPlay:
                player = line['Player']
                if player not in players:
                    players.append(player)
    players_value = StringVar(frame1)
    players_value.set("Select a Player")
    players_menu = OptionMenu(frame1, players_value, *players, command=selectPlayer)
    players_menu.config(width=18, height=1, bg='light blue', font=('Helvetica', 15))
    players_menu.place(x=310, y=340)

def displayModes():
    modes_value = StringVar(frame1)
    modes_value.set("Select Mode")
    modes_menu = OptionMenu(frame1, modes_value, *modes, command=selectMode)
    modes_menu.config(width=15, height=1, bg='light blue', font=('Helvetica', 15))
    modes_menu.place(x=330, y=220)

def displayPlays():
    plays_value = StringVar(frame1)
    plays_value.set("Select a Play")
    plays_menu = OptionMenu(frame1, plays_value, *plays, command=selectPlay)
    plays_menu.config(width=20, height=1, bg='light blue', font=('Helvetica', 15))
    plays_menu.place(x=300, y=280)

def main():
    displayModes()
    displayPlays()
    Button(frame1, text="Start Play", image=bimage1, command=startPlay).place(x=350, y=430)
    window.mainloop()   

main()

