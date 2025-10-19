def task_1():
    print("Task 1")
    start = int(input("Start: "))
    end = int(input("End: "))

    for i in range(start, end, 1):
        if i % 7 == 0:
            print(i)


def task_2():
    print("\nTask 2")
    start = int(input("Start: "))
    end = int(input("End: "))


    print("\nDefault order of numbers:")
    for i in range(end, start, 1):
        print(i, end=" ")
    print("\n")


    print("\nReversed order of numbers:")
    for i in range(start, end - 1, -1):
        print(i, end=" ")
    print("\n")


    print("\nDivisible by 7:")
    for i in range(start, end - 1, -1):
        if i % 7 == 0:
            print(i, end=" ")
    print("\n")


    count = 0
    for i in range(start, end - 1, -1):
        if i % 5 == 0:
            count += 1
    print(f"\nAmount of divisible by 5: {count}")


def task_3():
    print("\nTask 3")
    start = int(input("Start: "))
    end = int(input("End: "))

    print("\n")
    for i in range(start, end - 1, -1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

task_1()
task_2()
task_3()