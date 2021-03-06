
#Player class that holds, if they won and their colour
class Player:
    color = 'r'
    win = False

    def __init__(self, c):
        self.color = c

    def won(self):
        self.win = True