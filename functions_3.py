def print_max_square(matrix, row=0, col=0, max_size=0):
    max_row = len(matrix)
    max_col = len(matrix[0])

    def square_size(matrix, row, col, size):
        nonlocal max_row, max_col
        # max_row = len(matrix)
        # max_col = len(matrix[0])

        if row + size >= max_row or col + size >= max_col:
            return size

        if (matrix[row + size][col] == matrix[row][col] and
                matrix[row][col + size] == matrix[row][col] and
                matrix[row + size][col + size] == matrix[row][col]):
            return square_size(matrix, row, col, size + 1)

        return size

    if row >= max_row:
        return max_size

    # Iterate row
    if col >= max_col:
        return print_max_square(matrix, row + 1, 0, max_size)

    if matrix[row][col] != 0:
        size = square_size(matrix, row, col, 0)
        if size > max_size:
            max_size = size

    # Goto next column
    return print_max_square(matrix, row, col + 1, max_size)

def swap_matrix_r(_list, i=0, j=0, result = None):
    if result is None:
        result = []

    if i == len(_list):
        return result

    if len(result) <= j:
        result.append([])

    result[j].append(_list[i][j])


    if j == len(_list[0]) - 1:
        return swap_matrix_r(_list, i + 1, 0, result)
    else:
        return swap_matrix_r(_list, i, j + 1, result)

def diagonal_sum_r(_list, i=0, j=0, result = 0):
    if i == len(_list):
        return result

    result += _list[i][j]

    return diagonal_sum_r(_list, i+1, j+1, result)


_list = [
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [0 ,0, 1, 1],
    [0, 0, 1, 1]
]
print(f"largest square size: {print_max_square(_list)}")


_list = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(f"swapped matrix: {swap_matrix_r(_list)}")


_list = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(f"sum of diagonals: {diagonal_sum_r(_list)}")