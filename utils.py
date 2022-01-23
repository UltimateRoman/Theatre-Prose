import csv

def get_plays():
    plays = []
    with open('./plays.csv', 'r') as data:
        for line in csv.DictReader(data):
            play = line['Play']
            if play not in plays:
                plays.append(play)
    return plays

def get_players(selectedPlay):
    players = []
    with open('./plays.csv', 'r') as data:
        for line in csv.DictReader(data):
            play = line['Play']
            if play == selectedPlay:
                player = line['Player']
                if player not in players:
                    players.append(player)
    return players

def get_lines(selectedPlay, selectedPlayer):
    lines = []
    if selectedPlayer:
        with open('./plays.csv', 'r') as data:
            for line in csv.DictReader(data):
                if line['Play'] == selectedPlay and line['Player'] == selectedPlayer:
                    lines.append(line)                    
    else:
        with open('./plays.csv', 'r') as data:
            for line in csv.DictReader(data):
                if line['Play'] == selectedPlay:
                    lines.append(line)    
    return lines          