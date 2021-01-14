# -*- coding: utf-8 -*-
import os
import time
import sys
import tty
import termios
import platform
import random
from engine import inventory
from engine import attribute_player
from engine import balance
from engine import quests
from ui import map2
from ui import print_map2

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




def player_pos():
    for i in range(1, len(map2) + 1):
        if stuff['player'] in map2[i]:
            x_axis = i
            y_axis = map2[i].index(stuff['player'])
            global pos
            del pos[:]
            pos.append(x_axis)
            pos.append(y_axis)


def updater():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

        print_map2()
        player_pos()


updater()
# i made a question bank here to make randomize!
questions = []
questions.append(("When was the 1848 revolution?", "1848"))
questions.append(('When was the "Aranybulla" created? ', "1222"))
questions.append(("What Was the Largest Contiguous Empire in History?", "Khan"))
questions.append(("Who Discovered America?", "Colombus"))
questions.append(("What Does the D in D-Day Stand For?", "Doom"))
questions.append(("Who Invented the Automobile?", "Henry Ford"))
questions.append(("When Was the Declaration of Independence Signed?", "1776"))
questions.append(("What is the oldest city of the United States?", "Jamestown"))
questions.append(("Which African Country's Capital was Named After a U.S. President?", "Monrovia"))

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
        if map2[pos[0] - 1][pos[1]] is not stuff['wall']:
            up(map2, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall : up")
    if pressedkey == 'w' or pressedkey == 'W':
        if map2[pos[0] - 1][pos[1]] is stuff['chest']:
            up(map2, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall : up")
    elif pressedkey == 's' or pressedkey == 'S':
        if map2[pos[0] + 1][pos[1]] is not stuff['wall']:
            down(map2, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall : down")
    elif pressedkey == 'a' or pressedkey == 'A':
        if map2[pos[0]][pos[1] - 1] is not stuff['wall']:
            left(map2, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall : left")
    elif pressedkey == 'd' or pressedkey == 'D':
        if map2[pos[0]][pos[1] + 1] is not stuff['wall']:
            right(map2, stuff['empty'], stuff['player'])
            updater()
            print(pos)
        else:
            print("You can't go trough Wall: right")
    if map2[pos[0]][pos[1] + 1] is stuff['chest']:
        right(map2, stuff['empty'], stuff['player'])
        print('Congrats! You got a chest')
        print('You got the Blade of the Ruined King')
        inventory.append("Blade of the Ruined King:1")
        print(pos)
        time.sleep(1)
    if map2[pos[0]][pos[1] + 1] is stuff['money']:
        right(map2, stuff['empty'], stuff['player'])
        print('Congrats! You got $15 ')
        print('Go see the nearest shop and buy something')
        balance.append('$15')
        print(pos)
        time.sleep(1)
    if pressedkey == "r" or pressedkey == "R":
        print("Here's your character attributes!")
        print("For starters you can add only +4 (if you choose ninja class you have extra +1 attribute)")
        for k, v in dict.items(attribute_player):
            print(k, v)
    if map2[pos[0]][pos[1] + 1] is stuff['boss']:
        right(map2, stuff['empty'], stuff['player'])
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
    if map2[pos[0]][pos[1] + 1] is stuff['monster']:
        right(map2, stuff['empty'], stuff['player'])
        print("You are about to face this monster!")
        print("To defeat this monster you need to answer 1 question!")
        random_question = random.choice(questions)
        question, answer = random_question
        user_answer = input(question)
        if user_answer != answer:
            print("You lost! Better luck next time")
        else:
            print("Congratulations! You beat this monster")
            print("You got 15$")
            print("You got a key!")
            balance.append("45$")
            inventory.append("Key:1")