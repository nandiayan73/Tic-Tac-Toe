# Function to evaluate the board and return a score
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 1
            elif row[0] == 'O':
                return -1

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 1
            elif board[0][col] == 'O':
                return -1

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

    # No winner
    return 0

# Function to check if any moves are left on the board
def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

# Minimax function
def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # If Maximizer has won the game
    if score == 1:
        return score

    # If Minimizer has won the game
    if score == -1:
        return score

    # If no more moves and no winner
    if not is_moves_left(board):
        return 0

    # Maximizing Player
    if is_maximizing:
        best = -float('inf')

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'  # Make the move

                    best = max(best, minimax(board, depth + 1, False))

                    board[i][j] = '_'  # Undo the move

        return best

    # Minimizing Player
    else:
        best = float('inf')

        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'  # Make the move

                    best = min(best, minimax(board, depth + 1, True))

                    board[i][j] = '_'  # Undo the move

        return best

# Function to find the best move for the maximizing player
def find_best_move(board):
    best_val = -float('inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'  # Make the move

                move_val = minimax(board, 0, False)

                board[i][j] = '_'  # Undo the move

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

# Example board
board = [
    ['X', 'O', '0'],
    ['O', 'O', 'X'],
    ['_', '_', '_']
]

best_move = find_best_move(board)
print(f"The best move is at position: {best_move}")
