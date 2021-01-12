# -*- coding: utf-8 -*-
import os
import time
import sys
import tty
import termios
import platform
from engine import inventory
from engine import attribute_player
from engine import balance
from engine import quests

try:
    from msvcrt import getch  # For windows
except ImportError:  # For linux and maybe mac...
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def pressedkey():
    return getch()


room = {1:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'], # ^
	    2:['#','.','₿','←','←','←','←','←','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
	    3:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], # |
	    4:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], # |
	    5:['#','.','N','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], # |
	    6:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], # x
	    7:['#','@','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], # |
	    8:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','.','.','.','.','#','.','M','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], # |
	    9:['#','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], # |
	   10:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','.','.','.',"Ω",'.','.','.','.','.','#','.','.','$','.','.','♥','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',"#"], # |
	   11:['#','.','C','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','#','.','.','.','M','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], #
	   12:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','#','M','.','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], #
	   13:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','#'], #
	   14:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','.','.','.','.','.','.','#'],
	   15:['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'], #
	   16:['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']}   #


stuff = {'wall': "#",
         'player': "@",
         'empty': ".",
         'money': "$",
         'chest': "C",
         'shop': "Ω",
         'boss': "₿",
         'monster': "M",
         'npc': "N",
         'exit': "X",
         'health': "♥"}

pos = []


def gamemap():
    print("You are on the second map!")
    print("")
    for i in range(1, len(room) + 1):
        print("".join(room[i]))


def player_pos():
    for i in range(1, len(room) + 1):
        if stuff['player'] in room[i]:
            x_axis = i
            y_axis = room[i].index(stuff['player'])
            global pos
            del pos[:]
            pos.append(x_axis)
            pos.append(y_axis)


def updater():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

        gamemap()
        player_pos()


updater()


def up(ditcioary, inst_replace, inst_player):
    (ditcioary[pos[0]]).pop(pos[1])
    (ditcioary[pos[0]]).insert(pos[1], inst_replace)
    (ditcioary[pos[0] - 1]).pop(pos[1])
    (ditcioary[pos[0] - 1]).insert(pos[1], inst_player)


def down(ditcioary, inst_replace, inst_player):
    (ditcioary[pos[0]]).pop(pos[1])
    (ditcioary[pos[0]]).insert(pos[1], inst_replace)
    (ditcioary[pos[0] + 1]).pop(pos[1])
    (ditcioary[pos[0] + 1]).insert(pos[1], inst_player)


def left(ditcioary, inst_replace, inst_player):
    (ditcioary[pos[0]]).pop(pos[1])
    (ditcioary[pos[0]]).insert(pos[1], inst_replace)
    (ditcioary[pos[0]]).pop(pos[1] - 1)
    (ditcioary[pos[0]]).insert(pos[1] - 1, inst_player)


def right(ditcioary, inst_replace, inst_player):
    (ditcioary[pos[0]]).pop(pos[1])
    (ditcioary[pos[0]]).insert(pos[1], inst_replace)
    (ditcioary[pos[0]]).pop(pos[1] + 1)
    (ditcioary[pos[0]]).insert(pos[1] + 1, inst_player)


while True:
    pressedkey = getch()
    if pressedkey == "q" or pressedkey == "Q":
        print("Quests list:")
        print("")
        print(*quests, sep="\n")

    if pressedkey == "i" or pressedkey == "I":
        print("You have these items at the moment!")
        print(*inventory, sep="\n")
    if pressedkey == "l" or pressedkey == "L":
        print(*balance, sep="\n")
    if pressedkey == 'w' or pressedkey == 'W':
        if room[pos[0] - 1][pos[1]] is not stuff['wall']:
            up(room, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall : up")
    if pressedkey == 'w' or pressedkey == 'W':
        if room[pos[0] - 1][pos[1]] is stuff['chest']:
            up(room, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall : up")
    elif pressedkey == 's' or pressedkey == 'S':
        if room[pos[0] + 1][pos[1]] is not stuff['wall']:
            down(room, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall : down")
    elif pressedkey == 'a' or pressedkey == 'A':
        if room[pos[0]][pos[1] - 1] is not stuff['wall']:
            left(room, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall : left")
    elif pressedkey == 'd' or pressedkey == 'D':
        if room[pos[0]][pos[1] + 1] is not stuff['wall']:
            right(room, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall: right")
    if room[pos[0]][pos[1] + 1] is stuff['chest']:
        right(room, stuff['empty'], stuff['player'])
        print('Congrats! You got a chest')
        print('You got the Blade of the Ruined King')
        inventory.append("Blade of the Ruined King:1")
        print(pos)
        time.sleep(1)
    if room[pos[0]][pos[1] + 1] is stuff['money']:
        right(room, stuff['empty'], stuff['player'])
        print('Congrats! You got $15 ')
        print('Go see the nearest shop and buy something')
        balance.append('$15')
        print(pos)
        time.sleep(1)
    if room[pos[0]][pos[1] + 1] is stuff['shop']:
        right(room, stuff['empty'], stuff['player'])
        print('Hello Adventurer! Welcome our shop! Come back every day to see our new items" ')
        print("Today's item: 1 xCoke : 10$")
        items = ["1.Coke:1 $10", "2.Torch:1 $5", "3.Old sword:1 $15,"]
        print(*items, sep='\n')
        append_item = input("Please type which items would you buy!")
        if balance == ["Your balance:"]:
            print("You don't have enough money to buy this!")
        else:
            balance.remove('$15')
            inventory.append(append_item)
        print(pos)
        time.sleep(1)
    if pressedkey == "r" or pressedkey == "R":
        print("Here's your character attributes!")
        print("For starters you can add only +4 (if you choose ninja class you have extra +1 attribute)")
        for k, v in dict.items(attribute_player):
            print(k, v)
    if room[pos[0]][pos[1] + 1] is stuff['boss']:
        right(room, stuff['empty'], stuff['player'])
        print("You are about to face the boss! In order to beat him you need to answer 3 questions!")
        print("Every bad answers results -1 point from your health")
        answer = input("Are you ready? ")
        if answer == "yes":
            print("Who was the king?",
                  "1.Tibó Sláger",
                  "2.Tibi Csokis",
                  "3.Elvis Presley",
                  "4.Jimmy Zámbó")
            answer_2 = input("Type your answer: ")
            if answer_2 == "4":
                print("Good job!")
                print("You got $15 and a brand-new Armor:1")
                armor = "Armor:1"
                inventory.append(armor)
                balance.append("$15")
                print(
                    "Next Question!:I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I? ")
                answer_3 = input("Type your answer!")
                if answer_3 == "Your Shadow":
                    print("Congrats! You killed the boss, and won the game!")
                    print("Here is your reward:")
                    print("You got: God Butcher:1")
                    inventory.append("God Butcher:1")
                    print("GAME OVER!")
            else:
                print("Seriously???? The Boss defeated you, good luck next time!")
        else:
            print("It is a wise decision")
    if room[pos[0]][pos[1] + 1] is stuff['npc']:
        right(room, stuff['empty'], stuff['player'])
        print('Johhny: Hello, Adventurer, i need your help ')
        print("If you help me i will reward you! What do you say?")
        answer = input("Will you help Johhny? type yes or no: ")
        if answer == "yes":
            print("Thank you so much!")
            print("I lost my wallet, i'm bet one of the monsters stole from me ")
            print("Please kill those monsters and bring back my wallet!")
            print("Tips: this quest has been added to your quest list to see press Q!")
            del quests[1]
            quests.append("2: Find Johhny's wallet,")
        else:
            print("It's shame , really!")
