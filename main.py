import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3




def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player_datas ={PLAYER_ICON:'@'}  
    choose_difficulty = input("There are 3 difficulties , choose wisely ,type a number 1.easy(20x50), 2.medium(20x60), 3.hard(40x40): ")
    if choose_difficulty == '1':
        easy_diff = engine.create_board(20,50)
    elif choose_difficulty == '2':    
        medium_diff = engine.create_board(20,60)
    elif choose_difficulty == '3':
        hard_diff = engine.create_board(30,80)
    else:
        ValueError
        print("Not valid input")

def main():
    player = create_player()
    board = engine.create_board()

    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
