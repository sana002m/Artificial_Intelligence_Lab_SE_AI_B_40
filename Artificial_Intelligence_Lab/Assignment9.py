import math

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
    print()

# Check for winner
def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

# Check if board is full
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Find best move for AI (X)
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("You are O, AI is X")
    print_board(board)

    while True:
        # Player move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] == " ":
            board[row][col] = "O"
        else:
            print("Invalid move, try again!")
            continue

        print_board(board)

        if check_winner(board) == "O":
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # AI move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = "X"
            print("AI plays:")
            print_board(board)

        if check_winner(board) == "X":
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()

