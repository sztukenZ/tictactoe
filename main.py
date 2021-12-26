BOARD = '''
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
    "1": BOARD_VALUES[0][0],
    "2": BOARD_VALUES[0][1],
    "3": BOARD_VALUES[0][2],
    "4": BOARD_VALUES[1][0],
    "5": BOARD_VALUES[1][1],
    "6": BOARD_VALUES[1][2],
    "7": BOARD_VALUES[2][0],
    "8": BOARD_VALUES[2][1],
    "9": BOARD_VALUES[2][2]
}

EMPTY_BOARD = f'''
 {POSITIONS_DICT["1"]} | {POSITIONS_DICT["2"]} | {POSITIONS_DICT["3"]}
-----------
 {POSITIONS_DICT["4"]} | {POSITIONS_DICT["5"]} | {POSITIONS_DICT["6"]} 
-----------
 {POSITIONS_DICT["7"]} | {POSITIONS_DICT["8"]} | {POSITIONS_DICT["9"]} 
'''


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
            print("Accross")
            return True


def choose_player():

    while True:
        player_1 = input("Please choose your sign(type 'X' or 'O'): ")
        if player_1.upper() == "X":
            print("Player 1 will be X, Player 2 - O")
            return player_1.upper()
        elif player_1.upper() == "O":
            print("Player 1 will be O, Player 2 - X")
            return player_1.upper()
        elif player_1.lower() == "quit":
            break
        else:
            print("Please choose between 'X' or 'O'!")


def run():

    while True:
        print("Welcome to the Tic Tac Toe game!")
        answer = choose_player()
        print(answer)
        if answer == "X" or answer == "Y":
            print("This is an example board:")
            print(BOARD)
            print("Now here comes the real board:")
            print(EMPTY_BOARD)
            while not check_win():
                position = input("Please enter, which field you want to mark (1-9): ")
                print(POSITIONS_DICT[position])
                POSITIONS_DICT[position] = "X"
                print(EMPTY_BOARD)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
