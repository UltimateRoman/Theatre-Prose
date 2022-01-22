import csv
from tkinter import *
from time import sleep
from threading import Thread
from playsound import playsound

plays = []
players = []
modes = ["Single-Player", "Multi-Player"]

selectedPlay = None
selectedMode = modes[0]
selectedPlayer = None

window1 = Tk()
bg = PhotoImage(file = "assets/bg.png")
bg = bg.subsample(2, 2)
bphoto1 = PhotoImage(file = "assets/start.png")
bimage1 = bphoto1.subsample(4, 4)

window1.title("Theatre Pros(e)")
window1.resizable(False, False)
window1.geometry('876x580')
canvas1 = Canvas(window1, width = 500, height = 500)  
canvas1.pack(fill = "both", expand = True)   
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
Label(window1, fg="black", text="Theatre Pros(e)", font=("roboto", 40)).place(x=260, y=80)

with open('./plays.csv', 'r') as data:
    for line in csv.DictReader(data):
        play = line['Play']
        if play not in plays:
            plays.append(play)

def startPlay():
    window1.destroy()
    if selectedMode == modes[0]:
        with open('./plays.csv', 'r') as data:
            for line in csv.DictReader(data):
                if line['Play'] == selectedPlay and line['Player'] == selectedPlayer:
                    print("Line " + line['PlayerLinenumber'] + " " + line['PlayerLine'])
                    sleep(len(line['PlayerLine'])*0.14)
    else:
        with open('./plays.csv', 'r') as data:
            for line in csv.DictReader(data):
                if line['Play'] == selectedPlay:
                    print("Line " + line['PlayerLinenumber'] + " Player: " + line['Player'] + " - " + line['PlayerLine'])
                    sleep(len(line['PlayerLine'])*0.14)  
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
    with open('./plays.csv', 'r') as data:
        for line in csv.DictReader(data):
            play = line['Play']
            if play == selectedPlay:
                player = line['Player']
                if player not in players:
                    players.append(player)
    players_value = StringVar(window1)
    players_value.set("Select a Player")
    players_menu = OptionMenu(window1, players_value, *players, command=selectPlayer)
    players_menu.config(width=18, height=2, bg='light blue', font=('Helvetica', 15))
    players_menu.place(x=325, y=380)

def displayModes():
    modes_value = StringVar(window1)
    modes_value.set("Select Mode")
    modes_menu = OptionMenu(window1, modes_value, *modes, command=selectMode)
    modes_menu.config(width=15, height=2, bg='light blue', font=('Helvetica', 15))
    modes_menu.place(x=335, y=220)

def displayPlays():
    plays_value = StringVar(window1)
    plays_value.set("Select a Play")
    plays_menu = OptionMenu(window1, plays_value, *plays, command=selectPlay)
    plays_menu.config(width=18, height=2, bg='light blue', font=('Helvetica', 15))
    plays_menu.place(x=325, y=300)

def main():
    displayModes()
    displayPlays()
    Button(window1, text="Start Play", image=bimage1, command=startPlay).place(x=300, y=460)
    window1.mainloop()   

main()

