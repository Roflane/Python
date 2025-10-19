import random

def task_1():
    print("Task 1")
    nums = list(input("Enter 2 nums seperated by space: ").split())
    if len(nums) != 2:
        print("Only two numbers allowed")
        return

    sign_list = ["*", "/", "+", "-"] # possible operations
    sign_pick = input("Enter the arithmetic sign(*, /, +, -): ")

    if sign_pick == "*" == sign_list[0]:
        print(f"{nums[0]} * {nums[1]} = {int(nums[0]) * int(nums[1])}")
    elif sign_pick == "/" == sign_list[1]:
        print(f"{nums[0]} / {nums[1]} = {int(nums[0]) / int(nums[1])}")
    elif sign_pick == "+" == sign_list[2]:
        print(f"{nums[0]} + {nums[1]} = {int(nums[0]) + int(nums[1])}")
    elif sign_pick == "-" == sign_list[3]:
        print(f"{nums[0]} - {nums[1]} = {int(nums[0]) - int(nums[1])}")
    else:
        print(f"Warning: possible operations are only: {sign_list}")

    print()

def task_2():
    print("Task 2")
    list_size = random.randint(4, 9)
    general_list = []


    for i in range(list_size):
        general_list.append(random.randint(-99, 99))


    pnum_count = 0
    nnum_count = 0
    zero_count = 0
    for i in range(list_size):
        if general_list[i] == 0:
            zero_count += 1
        elif general_list[i] > 0:
            pnum_count += 1
        elif general_list[i] < 0:
            nnum_count += 1


    max_value = general_list[0]
    min_value = general_list[0]
    for num in general_list:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num


    print(f"{general_list}", "\n"
          f"Max number: {max_value} ", "\n"
          f"Min number: {min_value}", "\n"
          f"Count of positive numbers: {pnum_count}", "\n"
          f"Count of negative numbers: {nnum_count}", "\n"
          f"Count of zeros: {zero_count}", "\n")

if __name__ == '__main__':
    task_1()
    task_2()