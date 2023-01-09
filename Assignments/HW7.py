from constraint import *


MATRIX = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def apply_box_constraint(problem, x, y):
    box = list()
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            box.append(i * 10 + j)

    problem.addConstraint(AllDifferentConstraint(), box)


def sudoku_solver(matrix):
    prblm = Problem()

    for i in range(1, 10):
        prblm.addVariables(range(i * 10 + 1, i * 10 + 10), range(1, 10))

    # Every row has to be different values
    for i in range(1, 10):
        prblm.addConstraint(AllDifferentConstraint(),
                            range(i*10 + 1, i*10 + 10))

    # Every column has to be different values
    for i in range(1, 10):
        prblm.addConstraint(AllDifferentConstraint(),
                            range(10 + i, 100 + i, 10))

    # Each 3x3 box has to be different values
    for i in range(1, 10, 3):
        for j in range(1, 10, 3):
            apply_box_constraint(prblm, i, j)

    # add unary constraints for cells with initial non-zero values
    for i in range(1, 10):
        for j in range(1, 10):
            value = matrix[i - 1][j - 1]
            if value:
                prblm.addConstraint(lambda var, val=value: var == val, (i * 10 + j, ))

    return prblm.getSolution()


if __name__ == "__main__":
    result = sudoku_solver(MATRIX)

    if result is None:
        print('No Solution Found!')
    else:
        row = 1
        for k, v in sorted(result.items()):
            if k // 10 == row:
                print(v, end=" ")
            else:
                row += 1
                print(f"\n{v}", end=" ")
