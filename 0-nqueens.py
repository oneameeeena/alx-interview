#!/us/python3

import sys

def print_usage_and_exit(message):
    print(message)
    sys.exit(1)

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, N), range(col, N)):
        if board[i][j]:
            return False

    return True

def solve_nqueens_util(board, col, N, solutions):
    """Recursively solve the N Queens problem."""
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0

def solve_nqueens(N):
    """Solve the N Queens problem and return all solutions."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

