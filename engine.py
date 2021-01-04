def create_board(n, m):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    #width = int(input("Please enter the width: "))
    #height = int(input("Please enther the height: ")

    for i in range(1, n+1) : 
        for j in range(1, m+1) : 
            if (i == 1 or i == n or
                j == 1 or j == m) : 
                print("*", end="")             
            else : 
                print("-", end="")             
          
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
