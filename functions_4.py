import random

def count_bigger_num(_list, count=0):
    for num in range(1, len(_list)):
        if _list[num] > _list[num - 1]:
            count += 1
    return count

def unique_elements(_list):
    new_list = []

    for num in _list:
        if num not in new_list:
            new_list.append(num)
        elif num in new_list:
            new_list.pop()

    return new_list

def longest_seq(_list):
    current_list = []
    longest_list = []

    for i in range(len(_list)):
        if i == 0 or _list[i] > _list[i - 1] :
            current_list.append(_list[i])
        else:
            if len(current_list) > len(longest_list):
                longest_list = current_list
            current_list = [_list[i]]

    if len(current_list) > len(longest_list):
        longest_list = current_list

    return longest_list

def shift_elements(_list, n):
    n = n % len(_list)
    return _list[-n:] + _list[:-n]

def gen_random_list(a, b, size):
    return [random.randint(a, b) for _ in range(size)]

def merged_list(_list1, _list2):
    return _list1 + _list2

def common_unique_list(_list1, _list2):
    return unique_elements(_list1 + _list2)

def common_list(_list1, _list2):
    new_list = []

    for num in _list1:
        if num in _list2:
            new_list.append(num)

    return new_list

def unique_list(_list1, _list2):
    return unique_elements(_list1) + unique_elements(_list2)

def min_max_elements(_list1, _list2):
    return [min(_list1), max(_list1), min(_list2), max(_list2)]

def alt_sort(_list):
    new_list = []

    _list.sort()

    while _list:
        new_list.append(_list.pop(0))
        if _list:
            new_list.append(_list.pop(-1))

    return new_list


user_input = input("Input numbers by whitespace splitted: ").split()
# _list = []
# for num in user_input:
#     _list.append(int(num))

# _list = list(map(int, user_input.split()))

_list = [int(num) for num in user_input]
print(f'Element count: {count_bigger_num(_list)}\n')
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
user_input = input("Input numbers by whitespace splitted: ").split()
# _list = []
# for num in user_input:
#     _list.append(int(num))

# _list = list(map(int, user_input.split()))

_list = [int(num) for num in user_input]
print(f'Unique elements: {unique_elements(_list)}\n')
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
user_input = input("Input numbers by whitespace splitted: ").split()
# _list = []
# for num in user_input:
#     _list.append(int(num))

# _list = list(map(int, user_input.split()))

_list = [int(num) for num in user_input]

print(longest_seq(_list))
print(f'Sequence length: {len(longest_seq(_list))}\n')
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
user_input = input("Input numbers by whitespace splitted: ").split()
# _list = []
# for num in user_input:
#     _list.append(int(num))

# _list = list(map(int, user_input.split()))

_list = [int(num) for num in user_input]
print(f'Shifted elements:{shift_elements(_list, n=2)}\n')
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
_list1 = gen_random_list(10, 40, size=10)
_list2 = gen_random_list(10, 40, size=10)

print(f'First list: {_list1}')
print(f'Second list: {_list2}')
print(merged_list(_list1, _list2))
print(common_unique_list(_list1, _list2))
print(common_list(_list1, _list2))
print(unique_list(_list1, _list2))
print(min_max_elements(_list1, _list2))
print()
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# # _list = []
# # for num in user_input:
# #     _list.append(int(num))

# # _list = list(map(int, user_input.split()))

user_input = input("Input numbers by whitespace splitted: ").split()
_list = [int(num) for num in user_input]

print(alt_sort(_list))