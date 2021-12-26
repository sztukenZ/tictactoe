BOARD = f'''
 1 | 2 | 3
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
'''

BOARD_VALUES = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]


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


def run():
    while True:
        print(BOARD)
        if check_win():
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
