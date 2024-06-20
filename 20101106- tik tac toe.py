import random
import math

# Tic tac toe board printing function
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# check if a player has won
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):                                                           #ooo/xxx
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):                                             #ooo/xxx
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):    #2 diagonals
        return True

    return False

# check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)                       #checking empty space

# Function for the computer's move using minimax with alpha-beta pruning
def computer_move(board, player):
    if player == 'O':
        best_score = -math.inf                                                      ##'O' aims to maximize the score
        best_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = minimax(board, 0, False)                                 #initial depth, O's turn to maximize the score
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_moves = [(i, j)]
                    elif score == best_score:
                        best_moves.append((i, j))
        return random.choice(best_moves) if best_moves else None
    else:
        best_score = math.inf                                                       #'X' aims to minimize the score
        best_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = minimax(board, 0, True)                                  #'X's turn to minimize the score
                    board[i][j] = ' '
                    if score < best_score:
                        best_score = score
                        best_moves = [(i, j)]
                    elif score == best_score:
                        best_moves.append((i, j))
        return random.choice(best_moves) if best_moves else None

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    scores = {'X': -1, 'O': 1, 'draw': 0}

    if check_win(board, 'X'):
        return scores['X']
    if check_win(board, 'O'):
        return scores['O']
    if is_board_full(board):
        return scores['draw']

    if is_maximizing:
        best_score = -math.inf                                                     # 'O' wants to maximize the score of itself
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)          #deep, turn of x
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:                                              # x will not select this branch
                        break
        return best_score
    else:
        best_score = math.inf                                                      # 'X' wants to minimize the score of its opponent
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)           #deep, turn of o
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:                                               # o will not select this branch
                        break
        return best_score

# Main game loop for computer vs computer
def play_computer_vs_computer():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    random.shuffle(players)                                                          # shuffle the players to determine the first move

    print("Welcome to Computer vs Computer Tic Tac Toe!")

    while True:
        print_board(board)
        current_player = players[0]

        if current_player == 'X':
            print("Computer X is thinking...")
            move = computer_move(board, 'X')
        else:
            print("Computer O is thinking...")
            move = computer_move(board, 'O')

        if move:                                                                     #update cell
            row, col = move
            board[row][col] = current_player

        if check_win(board, 'X'):
            print_board(board)
            print("Computer X wins!")
            break

        if check_win(board, 'O'):
            print_board(board)
            print("Computer O wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        
        players.reverse()                                                              # swap the current player for the next turn

# Main game loop for computer vs human
def play_computer_vs_human():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    random.shuffle(players)                                                             # shuffle the players to determine the first move

    print("Welcome to Computer vs Human Tic Tac Toe!")


    print(f"{players[0]} goes first!")

    while True:
        print_board(board)
        current_player = players[0]

        if current_player == 'O':
            # human's turn
            try:
                position = int(input("Enter your move (1-9): "))
                if 1 <= position <= 9:
                    row = (position - 1) // 3                                           #indexing+row/column set
                    col = (position - 1) % 3
                    if board[row][col] == ' ':
                        board[row][col] = 'O'
                    else:
                        print("Invalid move, the cell is already in use.")
                        continue
                else:
                    print("Invalid input, please enter a number from 1 to 9.")
                    continue
            except ValueError:
                print("Invalid input, please enter a number from 1 to 9.")
                continue
        else:
            # computer's turn
            print("Computer is thinking...")
            move = computer_move(board, 'X')
            if move:
                row, col = move
                board[row][col] = 'X'

        if check_win(board, 'O'):
            print_board(board)
            print("Human wins!")
            break

        if check_win(board, 'X'):
            print_board(board)
            print("Computer wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # swap the current player for the next turn
        players.reverse()
        
        
# Menu
while True:
    print("Welcome to Tic Tac Toe!")
    print("Choose a game mode to continue:")
    print("1. Computer vs Human")
    print("2. Computer vs Computer")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        play_computer_vs_human()
    elif choice == '2':
        play_computer_vs_computer()
    elif choice == '3':
        print("Game Over!")
        break
    else:
        print("Invalid choice, please enter 1, 2 or 3.")
