def evaluate(board):
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

# check for game-over
def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

def minimax(board,isMaximizer):
   score=evaluate(board)
   
#    user or bot wins
   if(score==-1 or score==1):
     return score
#    its a draw
   if not is_moves_left(board):
     return 0
   
#    maximizer move:
   if isMaximizer:
      best=-float('inf')
      for i in range(3):
         for j in range(3):
            if(board[i][j]=='_'):
                # make the move
               board[i][j]='X'
                # calculate the value
               val=minimax(board,False)
                #store the highest score    
               best=max(val,best)
                #undo the move    
               board[i][j]='_'
         return best
#    minimizer move:
   if not isMaximizer:
      best=float('inf')
      for i in range(3):
         for j in range(3):
            if(board[i][j]=='_'):
                # make the move
               board[i][j]='O'
                # calculate the value
               val=minimax(board,True)
                #store the lowest score    
               best=min(val,best)
                #undo the move    
               board[i][j]='_'
         return best

def playGame(board):
   maxPoint=-float('inf')
   pos=(-1,-1)
   for i in range(3):
      for j in range(3):
        if(board[i][j]=='_'):
            # make the move
            board[i][j]='X'
            # calculate the score
            posPoint=minimax(board,False)
            # undo the move
            board[i][j]='_'
            # the best move will have the best score
            if(posPoint>maxPoint):
               maxPoint=posPoint
               pos=(i,j)
   board[pos[0]][pos[1]]='X'
   score=evaluate(board)
   return score


def printBoard(board):
   for i in range(3):
    for j in range(3):
       print(board[i][j],end=" ")
    print()
      

def Game(board):
    score=evaluate(board)
    while is_moves_left(board) and score==0:
        i=int(input("enter the i value:\t"))
        j=int(input("enter the i value:\t"))
        score=evaluate(board)
        if(score==-1):
           break
        board[i][j]='O'
        printBoard(board)
        print("Opponent's move:")
        score=playGame(board)
        printBoard(board)

    score=evaluate(board)
    if(score==-1):
        print("User wins")
    elif(score==1):
        print("Bot wins")
    else:
       print("Draw")
# Board
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]
Game(board)