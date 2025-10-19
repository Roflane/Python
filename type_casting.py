def task1():
    print("Task 1")
    a = int(input("Enter a frist number: "))
    b = int(input("Enter a second number: "))
    c = int(input("Enter a third number: "))

    print(f"Result is: {str(a)+str(b)+str(c)}.", "\n")


def task2():
    print("Task 2")
    num = input("Enter a 4-digit number: ")

    if len(num) == 4 and num.isdigit():
        num = int(num)

        a = num % 10000 // 1000
        b = num % 1000 // 100
        c = num % 100 // 10
        d = num % 10

        print(f"Product of digits is: {a * b * c * d}.", "\n")
    else:
        print("Error: Please enter a valid 4-digit number.", "\n")


def task3():
    print("Task 3")

    unit = None

    try:
        unit = float(input("Enter meters: "))

        print(f"Meters to santimeters: {unit*100}.", "\n"
              f"Meters to decimeters: {unit*10}.", "\n"
              f"Meters to millimeters: {unit*1000}.", "\n"
              f"Meters to miles: {unit * 0.000621371}.", "\n")

    except ValueError as TYPE_INFO:
        if unit is None:
            print(f"ValueError: unit {TYPE_INFO} to float.", "\n")


def task4():
    print("Task 4")

    base = None
    height = None

    try:
        base = float(input("Enter a base: "))
        height = float(input("Enter a height: "))
        area = 0.5 * (base * height)

        print(f"Area of triangle is: {area}.", "\n")

    except ValueError as TYPE_INFO:
        if base is None:
            print(f"ValueError: base {TYPE_INFO} to float.", "\n")
        elif height is None:
            print(f"ValueError: height {TYPE_INFO} to float.", "\n")


def task5():
    print("Task 5")

    num = None

    try:
        num = int(input("Enter a 4-digit number: "))

        a = num % 10000 // 1000
        b = num % 1000 // 100
        c = num % 100 // 10
        d = num % 10

        if a == b == c == d:
            print("All numbers are identical.")
        else:
            print(f"Reversed number is: {str(d) + str(c) + str(b) + str(a)}.")

    except ValueError as TYPE_INFO:
        if num is None:
            print(f"ValueError: {TYPE_INFO} to int.", "\n")


if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()