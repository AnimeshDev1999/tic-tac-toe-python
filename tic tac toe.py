board = [" " for i in range(9)]

print("Welcome to the Tic Tac Toe!")

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(mark):

    if mark == "X":
        num = 1
    elif mark == "O":
        num = 2

    print("Its your turn player {}".format(num))
    
    choice = int(input("Enter your move (1-9): ").strip())
    if (board[choice -1] == " "):
        board[choice -1] = mark
    else:
        print()
        print("Spot has already been marked!")

def win(mark):
    if(board[0] == mark and board[1] == mark and board[2] == mark) or\
      (board[3] == mark and board[4] == mark and board[5] == mark) or\
      (board[6] == mark and board[7] == mark and board[8] == mark) or\
      (board[0] == mark and board[3] == mark and board[6] == mark) or\
      (board[1] == mark and board[4] == mark and board[7] == mark) or\
      (board[2] == mark and board[5] == mark and board[8] == mark) or\
      (board[0] == mark and board[4] == mark and board[8] == mark) or\
      (board[2] == mark and board[4] == mark and board[6] == mark):
        return True
    else:
        return False

def draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if win("X"):
        print("X Wins! Congratulations")
        break
    elif draw():
        print("Its a draw!")
        break
    player_move("O")
    if win("O"):
        print_board()
        print("O Wins! Congratulations")
        break
    elif draw():
        print("Its a draw!")
        break
