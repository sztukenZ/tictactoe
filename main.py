from player import Player

EXAMPLE_BOARD = '''
 1 | 2 | 3
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
'''

BOARD_VALUES = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]

POSITIONS_DICT = {
    "1": (0,0),
    "2": (0,1),
    "3": (0,2),
    "4": (1,0),
    "5": (1,1),
    "6": (1,2),
    "7": (2,0),
    "8": (2,1),
    "9": (2,2)
}


def refresh_board():
    board = f'''
     {BOARD_VALUES[0][0]} | {BOARD_VALUES[0][1]} | {BOARD_VALUES[0][2]}
    -----------
     {BOARD_VALUES[1][0]} | {BOARD_VALUES[1][1]} | {BOARD_VALUES[1][2]}
    -----------
     {BOARD_VALUES[2][0]} | {BOARD_VALUES[2][1]} | {BOARD_VALUES[2][2]}
    '''
    return board


def update_board(player):
    while True:
        position = input(f"Player {player.turn} enter, which field you want to mark (1-9): ")
        if int(position) not in range(10):
            continue
        else:

            print(POSITIONS_DICT[position])
            i = POSITIONS_DICT[position][0]
            j = POSITIONS_DICT[position][1]
            BOARD_VALUES[i][j] = player.sign
            board = refresh_board()
            print(board)
            flag = check_win()
            break
    return flag

def checkList(lst):
    if lst.count(" ") == 0:
        return len(set(lst)) == 1


def check_win():
    for row in BOARD_VALUES:
        if checkList(row):
            print(f"Winner is player {row[0]}")
            return True

    columns = list(map(list, zip(*BOARD_VALUES)))
    for column in columns:
        if checkList(column):
            print(f"Winner is player {column[0]}")
            print("Column")
            return True

    if BOARD_VALUES[1][1] != " ":
        if BOARD_VALUES[1][1] == BOARD_VALUES[0][0] and BOARD_VALUES[1][1] == BOARD_VALUES[2][2] \
                or BOARD_VALUES[1][1] == BOARD_VALUES[0][2] and BOARD_VALUES[1][1] == BOARD_VALUES[2][0]:
            print(f"Winner is player {BOARD_VALUES[1][1]}")
            print("Across")
            return True


# TODO 1: Choose player
# TODO 2: Take turns
# TODO 3: Quit game


def choose_player():
    choices = ["X", "O", "QUIT"]
    while True:
        print("Welcome to the Tic Tac Toe game!")
        choice = input("Please choose your sign(type 'X' or 'O') or type 'QUIT' to close the program: ")
        if choice.upper() not in choices:
            continue
        else:
            if choice.upper() == 'QUIT':
                break
            else:
                player1 = Player(choice.upper(), 1)
                player1.showInfo()
                if choice.upper() == "X":
                    player2 = Player("O", 2)
                    player2.showInfo()
                else:
                    player2 = Player("X", 2)
                    player2.showInfo()

                print("This is an example board:")
                print(EXAMPLE_BOARD)
                print("Now here comes the real board:")

                take_turns(player1, player2)


def take_turns(player_1, player_2):
    board = refresh_board()
    print(board)
    while not check_win():
        if update_board(player_1):
            break
        if update_board(player_2):
            break


if __name__ == '__main__':
    choose_player()

