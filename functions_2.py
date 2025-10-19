def unique_swap(_list) -> list:
    unique_list = [_list[:]]

    for i in range(len(_list)):
        for j in range(i + 1, len(_list)):

            temp = _list[:]
            temp[i], temp[j] = temp[j], temp[i]

            if temp not in unique_list:
                unique_list.append(temp)

    return unique_list

_list = [1, 2, 2]
print(unique_swap(_list)) # [[1, 2, 2], [2, 1, 2], [2, 2, 1]]


def list_filter(list, start, end) -> list:
    for sublist in list:
        for num in sublist[:]:
            if not start <= num < end:
                sublist.remove(num)

    return list


list = [[1, 5, 8], [10, 3, 7], [4, 9, 6]]
print(list_filter(list, start=4, end=8)) #[[5], [7], [4, 6]]


def group_parceling(list, n) -> list:
    new_list = []

    for i in range(0, len(list), n):
        new_list.append(list[i:i + n])

    return new_list

list = [1, 2, 3, 4, 5, 6, 7, 8]
print(group_parceling(list, 3)) # [[1, 2, 3], [4, 5, 6], [7, 8]]

def find_target(list, target) -> list:
    new_list = []

    for i in range(1, len(list)):
        if list[i] + list[i-1] == target:
            new_list.append([list[i-1], list[i]])

        if list[i] == target:
            new_list.append([list[i]])

    return new_list

list = [1, 2, 3, 4, 5]
print(find_target(list, 5)) # [[2, 3], [5]]


def to_spiral(matrix) -> list:
    new_list = []

    while matrix:
        new_list.extend(matrix.pop(0))

        if matrix and matrix[0]:
            for row in matrix:
                new_list.append(row.pop())

        if matrix:
            new_list.extend(matrix.pop()[::-1])

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                new_list.append(row.pop(0))

    return new_list



list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(to_spiral(list))


def isPalindrome(list) -> bool:
    unique_nums = []

    for num in list:
        if num in unique_nums:
            unique_nums.remove(num)
        else:
            unique_nums.append(num)


    return len(unique_nums) <= 1


_list = [1, 2, 3, 2, 1]
print(isPalindrome(list)) # True