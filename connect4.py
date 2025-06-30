def print_board():
    for list_index in board:
        print()
        for item in list_index:
            print(item,end=" ")
board = [[],[],[],[],[],[],[]]
for i in range(6):
    print()
    for _ in range(7):
        board[i].append("-")
print_board()
turn = "y"
running = True
while running:
    slot_chosen = int(input("Which slot would you like to throw a disc in?"))-1
    for i in range(6):
        if board[5-i][slot_chosen] == "-":
            board[5-i][slot_chosen] = turn
            print("Ok! Here is the new board:")
            print_board()
            if turn == "y":
                turn = "r"
            else:
                turn ="y"
            break
        elif i == 5:
            print("You cannot place a disc there!")
    for i in range(6):
        for j in range(4):
            if board[i][j]!="-" and board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2] and board[i][j] == board[i][j+3]:
               if turn == "y":
                turn = "r"
                print("Red wins!")
               else:
                turn ="y"
                print("Yellow wins!")
               running=False
    for i in range(3):
        for j in range(7):
            if board[i][j]!="-" and board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j] and board[i][j] == board[i+3][j]:
               if turn == "y":
                turn = "r"
                print("Red wins!")
               else:
                turn ="y"
                print("Yellow wins!")
               running=False
    for i in range(3):
        for j in range(4):
            if board[i][j]!="-" and board[i][j] == board[i+1][j+1] and board[i][j] == board[i+2][j+2] and board[i][j] == board[i+3][j+3]:
               if turn == "y":
                turn = "r"
                print("Red wins!")
               else:
                turn ="y"
                print("Yellow wins!")
               running=False
    for i in range(3):
        for j in range(4):
            if board[i+3][j]!="-" and board[i+3][j] == board[i+2][j+1] and board[i+3][j] == board[i+1][j+2] and board[i+3][j] == board[i][j+3]:
               if turn == "y":
                turn = "r"
                print("Red wins!")
               else:
                turn ="y"
                print("Yellow wins!")
               running=False