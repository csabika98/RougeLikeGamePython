import time
import io


def print_ascii_art():
    file = io.open("ascii.txt", "r", encoding="utf-8")
    entire_file = file.read()
    file.close()
    ascii_text = f"\033[91m{entire_file}\033[00m"
    print(ascii_text)




def story():
    print("You are Shinek the half-ghoul")
    print("Half-ghoul means half-human, half-undead")
    print("You have to kill Baltaazar , the giga-boss who did this to you")
    print("Your journey begins here!")
    print("")




selected_name = input("Type your character name: ")
char_selected = input("Type your character class: 1.Warrior, 2.Ninja, 3.Shaman: ")
print("Warrior has less health than Ninja or Shaman but he has more DMG")
print("Ninja can add extra +1 attribute ")

def attributes():
    print("Hello player! Welcome to our World")
    print("Tips: YOU ONLY HAVE 4 ATTRIBUTE TO SPEND!, FOR STARTERS ONLY 2 POINT/ATTRIBUTE OR 1 POINT EACH ATTRIBUTE ")
    import game
    time.sleep(2)

	
health_bar = 'Your health: 3/3'

attribute_player = {"Power":0,
					"Defense":0,
					"Intelligence":0,
					"Charisma":0,
					"Luck":0}  
inventory =         ['Torch:1',
					'Letter from mom:1',
	                'Rusty sword:1']
balance = ["Your balance:"]
quests =["1: Defeat 2 monsters", "2: Speak with Johhny[NPC],"]  

