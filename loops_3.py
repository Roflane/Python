def task_1():
    print("Task 1")
    x = int(input("x: "))
    print()

    for i in range(1, x):
        stars = "* " * (x - i)
        spaces = "  " * (i - 1) + "*"
        print(stars + spaces)

    print("* " * x)


    print()


def task_2():
    print("Task 2\n")
    n = 5

    for i in range(1, n - 2):
        spaces = " " * (n - i - 1)


        if i == 1:
            stars = ("*") + "      " + "*"
        else:
            stars = ("*" + " " * (2 * (i - 1) - 1)) + ("*" + "    " + "* *")
        print(spaces + stars)


    for i in range(1, n - 1):
        spaces = " " * i
        middle_spaces = " " * (2 * (n - i - 2) - 1)

        if i == n - 2:
            print(spaces + "*" + "      " + "*")
        elif i == 1:
            print((spaces + "*" + middle_spaces + "*") + (" " * (i + 1) + "*   *"))
        elif i == 2:
            print((spaces + "*" + middle_spaces + "*") + (" " * (i + 1) + " " + "* *"))
        elif i == 3:
            print((spaces + "*" + middle_spaces + "*") + (" " * (i + 1) + "*"))


    print()


def task_3():
    print("Task 3\n")
    n = 10


    #\ /
    for i in range(1, n - 1):
        line = [str(j) for j in range(i, min(n, i + 9))]
        print(" " * i + " ".join(line))

    #/ \
    for i in range(n - 1, 0, -1):
        line = [str(j) for j in range(i, min(n, i + 9))]
        print(" " * i + " ".join(line))


task_1()
task_2()
task_3()