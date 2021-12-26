BOARD = f'''
 1 | 2 | 3
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 '''

BOARD_VALUES = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def check_win():
    for row in BOARD_VALUES:
        if row[0][0] == row[1][0] and row[0][0] == row[2][0]:
            pass

def run():
    print(BOARD)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


