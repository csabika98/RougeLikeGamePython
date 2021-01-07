import time




def main():
    print("Hello player! Welcome to our World, your aim is to beat the boss aka Pali and collect all the hidden treasure")
    print("Choose attribute to your character:")
    print("Note: YOU ONLY HAVE 4 ATTRIBUTE TO SPEND!, FOR STARTERS ONLY 2 POINT/ATTRIBUTE OR 1 POINT EACH ATTRIBUTE ")
    for k, v in dict.items(attribute_player):
        print(k,v)
    choose_attrib = input("Type the attribute name: ")
    attribute_player[choose_attrib] = 3 
    attribute_player[choose_attrib] -= 2
    choose_attrib = input("Type another attribute name: ")
    if choose_attrib == "Power":
        attribute_player[choose_attrib] = 4 
        attribute_player[choose_attrib] -= 2
        print("Congrats! That attribute recieved +1 point")
    else: 
        choose2 = input("Type another attribute name: ")
        attribute_player[choose2] = 1 
        print("Congrats! That attribute recieved +1 point")
    choose3 = input("Type another attribute name: ")
    attribute_player[choose3] = 1 
    choose4 = input("Type another attribute name: ")
    attribute_player[choose4] = 1 
    print("Congrats! That attribute recieved +1 point")
    for k, v in dict.items(attribute_player):
        print(k,v)
        saved_information = attribute_player
    print("You are starting with 3 health point, be careful fighting against monsters may harm your health.")
    print(health_bar)
    print("Tips: Enter I on your keyboard if you want to see your inventory!")
    print("Have fun!")
    time.sleep(5)
    import game

	
health_bar = 'Your health: 3/3'

attribute_player = {"Power":0,
					"Defense":0,
					"Intelligence":0,
					"Charisma":0,
					"Luck":0}  
inventory =         ['Torch:1',
					'Letter from mom:1',
	                'Rusty sword:1'] 

if __name__ == "__main__":
    main()
    