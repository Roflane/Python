size = int(input("Enter matrix size: "))
max_width = len(str(size * size))

print("Options: Show default matrix[1], Show matrix with swapped diagonals[2], Show rotated matrix[3]")
choice = input("Choose an option: ")

if choice == "1":
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(i * size + j + 1)
        matrix.append(row)

    for row in matrix:
        for num in row:
            print(f"{num:{max_width}}", end=" ")
        print()

elif choice == "2":
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(i * size + j + 1)
        matrix.append(row)

    for i in range(size):
        if i == 0 or i == size - 1:
            matrix[i] = matrix[i][::-1]

    for row in matrix:
        for num in row:
            print(f"{num:{max_width}}", end=" ")
        print()

elif choice == "3":
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(i * size + j + 1)
        matrix.append(row)

    rotated_matrix = []

    for j in range(size):
        new_row = []
        for i in range(size-1, -1, -1):
            new_row.append(matrix[i][j])
        rotated_matrix.append(new_row)

    for row in rotated_matrix:
        for num in row:
            print(f"{num:{max_width}}", end=" ")
        print()
else:
    print("Wrong option.")