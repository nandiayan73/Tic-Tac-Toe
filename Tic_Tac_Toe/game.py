def gameOver(board):
    # row check
    for row in board:
       if(row[0]==row[1]==row[2]):
          if(row[0]=='X'):
            return 1
          if(row[0]=='O'):
            return -1
    # column check
    for i in range(3):
       if(board[0][i]==board[1][i]==board[2][i]):
          if(board[0][i]=='X'):
             return 1
          if(board[0][i]=='O'):
             return -1
    # Diagonal-check
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 1
        elif board[0][0] == 'O':
            return -1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O':
            return -1
    # DRAW
    return 0





# Board
board = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['_', '_', '_']
]
gameOver(board)
print(gameOver(board))