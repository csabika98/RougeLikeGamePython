def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    #width = int(input("Please enter the width: "))
    #height = int(input("Please enther the height: "))

    for i in range(width):
        for j in range(height):
            if(i == 0 or i == width-1 or j ==0 or j == height-1):
                print('*', end=' ')
            else:
                print('-', end=' ')
    print()


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
