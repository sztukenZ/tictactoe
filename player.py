class Player:

    def __init__(self, sign, turn):
        self.sign = sign
        self.turn = turn

    def showInfo(self):
        print(f"Player {self.turn} will be using {self.sign} sign")