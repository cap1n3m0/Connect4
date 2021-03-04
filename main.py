print("this is a tset")
print("testing recieved")

board = [
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],
["o", "o", "o", "o", "o", "o", "o"],]

def printboard(board):
    for i in board:
        print("| ", end="")
        for l in i:
            print(l, end="")
            print(" | ", end="")
        print("")
        print("-----------------------------")
