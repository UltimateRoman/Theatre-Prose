import csv
from tkinter import *
from time import sleep
from threading import Thread
from playsound import playsound

window = Tk()
bg = PhotoImage(file = "assets/bg.jpeg")

window.title("Theatre Pros(e)")
window.resizable(False, False)
window.geometry('500x500')
canvas1 = Canvas(window, width = 500, height = 500)  
canvas1.pack(fill = "both", expand = True)   
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
Label(window, bg="blue", fg="white", text="Theatre Pros(e)", font=("roboto", 40)).place(x=140, y=100)

plays = []
players = {}

with open('./plays.csv', 'r') as data:
    for line in csv.DictReader(data):
        play = line['Play']
        if play not in plays:
            plays.append(play)
            players[play] = []
        else:
            player = line['Player']
            if player not in players[play]:
                players[play].append(player)

playIndex = int(input("play:"))
playerIndex = int(input("player:"))

play = plays[playIndex]
player = players[plays[playIndex]][playerIndex]

print(play, ":", player)

with open('./plays.csv', 'r') as data:
    for line in csv.DictReader(data):
        if line['Play'] == play and line['Player'] == player:
            print("Line " + line['PlayerLinenumber'] + " " + line['PlayerLine'])
            sleep(len(line['PlayerLine'])*0.14)