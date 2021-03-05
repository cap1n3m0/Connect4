class Player:
    color = 'r'
    win = False

    def __init__(self, c):
        self.color = c

    def won(self):
        self.win = True
