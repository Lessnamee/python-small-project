def create_board():
    lines = []
    for i in range(3):
        column = ['*', '*', '*']
        lines.append(column)
    return lines

def display(board):
    for i in range(3):
        print(board[i][0], '|', board[i][1], '|', board[i][2])
        print('---------')

def question(board, variable):
    line = int(input("Line: "))
    column = int(input("Column: "))
    board[line][column] = variable


def check(board, variable):
    for i in range(3):
        if board[i][0] == variable and board[i][1] == variable and board[i][2] == variable:
            return False
        if board[0][i] == variable and board[1][i] == variable and board[2][i] == variable:
            return False
    if board[0][0] == variable and board[1][1] == variable and board[2][2] == variable:
        return False
    if board[0][2] == variable and board[1][1] == variable and board[2][0] == variable:
        return False

    return True

def change_player(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'
board = create_board()

play = True
round = 'x'
while play:
    display(board)
    question(board, round)
    play = check(board, round)

    round = change_player(round)


display(board)
print("Win!")
