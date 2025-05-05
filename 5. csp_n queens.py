def is_safe(board, row, col, n):
    # Check this column on previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_bt(board, row, n):
    if row == n:
        return True  # All queens placed

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_bt(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack
    return False

def print_board(board):
    for row in board:
        print(" ".join('Q' if x == 1 else '.' for x in row))
    print()

def n_queens_backtracking(n=4):
    board = [[0] * n for _ in range(n)]
    if solve_n_queens_bt(board, 0, n):
        print("✅ 4-Queens Solution using Backtracking:\n")
        print_board(board)
    else:
        print("❌ No solution found using backtracking.")

def solve_n_queens_bb(board, row, n, col_used, left_diag, right_diag):
    if row == n:
        return True

    for col in range(n):
        if not col_used[col] and not left_diag[row - col] and not right_diag[row + col]:
            board[row][col] = 1
            col_used[col] = left_diag[row - col] = right_diag[row + col] = True

            if solve_n_queens_bb(board, row + 1, n, col_used, left_diag, right_diag):
                return True

            # Backtrack
            board[row][col] = 0
            col_used[col] = left_diag[row - col] = right_diag[row + col] = False
    return False

def n_queens_branch_and_bound(n=4):
    board = [[0] * n for _ in range(n)]
    col_used = [False] * n
    left_diag = {}
    right_diag = {}

    for i in range(-n+1, n):  # Diagonal ranges
        left_diag[i] = False
    for i in range(2*n - 1):
        right_diag[i] = False

    if solve_n_queens_bb(board, 0, n, col_used, left_diag, right_diag):
        print("✅ 4-Queens Solution using Branch and Bound:\n")
        print_board(board)
    else:
        print("❌ No solution found using branch and bound.")

if __name__ == "__main__":
    n_queens_backtracking()
    n_queens_branch_and_bound()

