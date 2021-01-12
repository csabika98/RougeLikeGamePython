import time
import io


def print_ascii_art():
    file = io.open("ascii.txt", "r", encoding="utf-8")
    entire_file = file.read()
    file.close()
    ascii_text = f"\033[91m{entire_file}\033[00m"
    print(ascii_text)


def story():
    print("")





def attributes():
    print("Hello player! Welcome to our World")
    print("Choose attribute to your character:")
    print("Note: YOU ONLY HAVE 4 ATTRIBUTE TO SPEND!, FOR STARTERS ONLY 2 POINT/ATTRIBUTE OR 1 POINT EACH ATTRIBUTE ")
    import main
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

if __name__ == "__main__":
    print_ascii_art()
    story()
    attributes()
    