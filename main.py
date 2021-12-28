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
        choice = input("Please choose your sign(type 'X' or 'O') or type 'QUIT' to close the program: ")
        if choice.upper() not in choices:
            continue
        else:
            if choice.upper() == 'QUIT':
                break
            else:
                player1 = Player(choice, 1)
                player1.showInfo()
                if choice == "X":
                    player2 = Player("O", 2)
                    player2.showInfo()
                else:
                    player2 = Player("X", 2)
                    player2.showInfo()





# def choose_player():
#
#     while True:
#         player_1 = input("Please choose your sign(type 'X' or 'O'): ")
#         if player_1.upper() == "X":
#             print("Player 1 will be X, Player 2 will be O")
#             return player_1.upper()
#         elif player_1.upper() == "O":
#             print("Player 1 will be O, Player 2 will be X")
#             return player_1.upper()
#         elif player_1.lower() == "quit":
#             break
#         else:
#             print("Please choose between 'X' or 'O'!")
#
#
# def run():
#
#     while True:
#         print("Welcome to the Tic Tac Toe game!")
#         answer = choose_player()
#         print(answer)
#         if answer == "X" or answer == "Y":
#             print("This is an example board:")
#             print(EXAMPLE_BOARD)
#             print("Now here comes the real board:")
#             board = refresh_board()
#             print(board)
#             sign = answer
#             round = 0
#             while not check_win():
#                 position = input("Please enter, which field you want to mark (1-9): ")
#                 round += 1
#                 print(round)
#                 if round % 2 == 0:
#                     if sign == "O":
#                         sign = "X"
#                     elif sign == "X":
#                         sign = "O"
#
#                 print(POSITIONS_DICT[position])
#                 i = POSITIONS_DICT[position][0]
#                 j = POSITIONS_DICT[position][1]
#                 BOARD_VALUES[i][j] = sign
#                 board = refresh_board()
#                 print(board)


if __name__ == '__main__':
    choose_player()
    pass
    # run()
