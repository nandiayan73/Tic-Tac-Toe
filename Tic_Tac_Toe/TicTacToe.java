public class TicTacToe {

    public static int evaluate(char[][] board) {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
                if (board[i][0] == 'X') return 1;
                if (board[i][0] == 'O') return -1;
            }
        }

        for (int i = 0; i < 3; i++) {
            if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
                if (board[0][i] == 'X') return 1;
                if (board[0][i] == 'O') return -1;
            }
        }

        if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
            if (board[0][0] == 'X') return 1;
            if (board[0][0] == 'O') return -1;
        }

        if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
            if (board[0][2] == 'X') return 1;
            if (board[0][2] == 'O') return -1;
        }

        return 0;
    }

    public static boolean isMovesLeft(char[][] board) {
        for (char[] row : board) {
            for (char c : row) {
                if (c == '_') return true;
            }
        }
        return false;
    }

    public static int minimax(char[][] board, int depth, boolean isMaximizing) {
        int score = evaluate(board);
        if (score == 1 || score == -1) return score;
        if (!isMovesLeft(board)) return 0;

        if (isMaximizing) {
            int best = Integer.MIN_VALUE;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (board[i][j] == '_') {
                        board[i][j] = 'X';
                        best = Math.max(best, minimax(board, depth + 1, false));
                        board[i][j] = '_';
                    }
                }
            }
            return best;
        } else {
            int best = Integer.MAX_VALUE;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (board[i][j] == '_') {
                        board[i][j] = 'O';
                        best = Math.min(best, minimax(board, depth + 1, true));
                        board[i][j] = '_';
                    }
                }
            }
            return best;
        }
    }

    public static int[] findBestMove(char[][] board) {
        int bestVal = Integer.MIN_VALUE;
        int[] bestMove = {-1, -1};

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == '_') {
                    board[i][j] = 'X';
                    int moveVal = minimax(board, 0, false);
                    board[i][j] = '_';

                    if (moveVal > bestVal) {
                        bestVal = moveVal;
                        bestMove[0] = i;
                        bestMove[1] = j;
                    }
                }
            }
        }
        return bestMove;
    }

    public static void main(String[] args) {
        char[][] board = {
            {'0', '_', 'O'},
            {'_', '0', 'X'},
            {'X', '_', 'X'}
        };

        int[] bestMove = findBestMove(board);
        System.out.println("The best move is at position: (" + bestMove[0] + ", " + bestMove[1] + ")");
    }
}
