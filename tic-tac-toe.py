def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for combination in winning_combinations:
        if all(board[row][col] == player for row, col in combination):
            return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = {
        (0, 0): ' ', (0, 1): ' ', (0, 2): ' ',
        (1, 0): ' ', (1, 1): ' ', (1, 2): ' ',
        (2, 0): ' ', (2, 1): ' ', (2, 2): ' '
    }
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            
            if board[(row, col)] == ' ':
                board[(row, col)] = current_player
                if check_win(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    current_player = 'X' if current_player == 'O' else 'O'
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, KeyError):
            print("Invalid input. Please enter a valid row and column (0, 1, 2).")

if __name__ == "__main__":
    tic_tac_toe()
