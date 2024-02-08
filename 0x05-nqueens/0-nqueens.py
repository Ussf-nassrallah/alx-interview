#!/usr/bin/python3
""" N queens """
import sys


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: nqueens N")
        exit(1)

    n_value = int(sys.argv[1])

    if n_value < 4:
        print("N must be at least 4")
        exit(1)

    solve_n_queens(n_value)


def queens_positions(
    n,
    i=0,
    col_positions=[],
    diag1_positions=[],
    diag2_positions=[]
):
    """ Find possible positions for queens """
    if i < n:
        for j in range(n):
            if j not in col_positions \
                and i + j not in diag1_positions\
                    and i - j not in diag2_positions:
                yield from queens_positions(
                    n,
                    i + 1,
                    col_positions + [j],
                    diag1_positions + [i + j],
                    diag2_positions + [i - j]
                )
    else:
        yield col_positions


def solve_n_queens(n):
    """ Solve the N queens problem """
    solution_list = []
    row_index = 0

    for solution in queens_positions(n, 0):
        for col in solution:
            solution_list.append([row_index, col])
            row_index += 1

        print(solution_list)
        solution_list = []
        row_index = 0


if __name__ == "__main__":
    main()
