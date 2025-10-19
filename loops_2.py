def draw_triangle_1():
    print("Task 1")
    n = int(input("n: ")) # height

    for i in range(n):
        a = " " * (n - i - 1) # spaces
        b = "*" * (2 * i + 1) # stars
        print(a + b)

    print()

def draw_triangle_2():
    print("Task 2")
    n = int(input("n: "))

    for i in range(n):
        a = " " * (n - i - 1)

        if i == 0:
            b = "*" * (2 * i + 1)

        elif i == n - 1:
            b = "*" * (2 * i + 1)
        else:
            b = "*" + " " * (2 * i - 1) + "*"

        print(a + b)

draw_triangle_1()
draw_triangle_2()