import random
from art import logo, x_wins, o_wins, is_a_draw


# Function to draw the game board
def drawBoard(x, o):
    # Create an empty board with dashes
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Fill in X's and O's in their respective positions
    for i in x:
        board[i - 1] = "X"

    for i in o:
        board[i - 1] = "0"

    # Print the game board
    print(f' {board[0]} | {board[1]} | {board[2]} \n'
          f'____________\n'
          f' {board[3]} | {board[4]} | {board[5]} \n'
          f'____________\n'
          f' {board[6]} | {board[7]} | {board[8]} \n')


# Function to let the player select their symbol
def selectPlayer(players):
    # Prompt the user to select 'X' or 'O' for the game
    real_player = input('Select [X / 0] for the game: ').capitalize()
    print("\n")

    # Validate the input
    while not ((real_player == "X") or (real_player == "0")):
        real_player = input('Select [X / O] for the game: ').capitalize()
        print("\n")

    # Assign symbols to players based on user input
    if real_player == "X":
        players[0] = "X"
        players[1] = "0"
    elif real_player == "0":
        players[0] = "0"
        players[1] = "X"

    return players


# Function to assign numbers to X and O
def asignNumbers(players, x, o):
    global end_game

    # Check if the game is a draw
    if (len(x) + len(o)) >= 9:
        print(is_a_draw)
        end_game = True
        return end_game

    # Prompt the player to select a position
    number = int(input('Select an available position from 1-9 : '))
    print("\n")

    # Check if the selected position is valid
    if 1 <= number <= 9:
        if players[0] == "X":
            # Check if the position is already occupied
            while (number in x) or (number in o):
                number = int(input('Select an available position from 1-9 : '))
                print("\n")
            # Add the position to the X list
            x.append(number)
            # Generate a random position for O
            if (len(x) + len(o)) < 9:
                number_pc = random.randint(1, 9)
                while (number_pc in x) or (number_pc in o):
                    number_pc = random.randint(1, 9)
                o.append(number_pc)
        elif players[0] == "0":
            while (number in x) or (number in o):
                number = int(input('Select an available position from 1-9 : '))
                print("\n")
            o.append(number)
            if (len(x) + len(o)) < 9:
                number_pc = random.randint(1, 9)
                while (number_pc in x) or (number_pc in o):
                    number_pc = random.randint(1, 9)
                x.append(number_pc)
    return x, o


# Function to check for a winner
def checkWinner(x, o):
    global end_game

    # Possible winning combinations
    winers_group_values = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    # Check if any winning combination is present for X
    for group in winers_group_values:
        if all(elem in x for elem in group):
            print(x_wins)
            end_game = True
            return end_game

        # Check if any winning combination is present for O
        elif all(elem in o for elem in group):
            print(o_wins)
            end_game = True
            return end_game


# Initial setup
print(logo)
x = []
o = []
players = ["", ""]
end_game = False
continue_game = True

# Main game loop
while continue_game:
    x = []
    o = []
    selectPlayer(players)
    drawBoard(x, o)
    while not end_game:
        asignNumbers(players, x, o)
        drawBoard(x, o)
        checkWinner(x, o)

    # Ask the player if they want to continue playing
    replay = input('Do you want to continue [Y/N]: ').capitalize()

    if replay == "Y":
        continue_game = True
        end_game = False
    else:
        continue_game = False
