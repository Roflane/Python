#Font Style
class FS:
    reset = "\033[0m"
    ENABLE_ITALIC = "\033[3m"


def task1():
    first_number = second_number = select = None

    try:
        print("Task 1")
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        select = int(input(f"Select from the following {FS.ENABLE_ITALIC}Sum[1], Product[2]: {FS.reset}"))

        if select == 1:
            print(first_number + second_number, "\n")
        elif select == 2:
            print(first_number * second_number, "\n")
        else:
            print(F"Select is only one of the following {FS.ENABLE_ITALIC}Sum[1], Product[2]{FS.reset}")

    except ValueError as TYPE_INFO:
        if first_number is None:
            print(f"ValueError: first number {TYPE_INFO} to float.", "\n")
        elif second_number is None:
            print(f"ValueError: second number {TYPE_INFO} to float.", "\n")
        elif select is None:
            print(f"ValueError: select {TYPE_INFO} to int.", "\n")

def task2():
    print("Task 2")
    first_number = second_number = third_number = select = None

    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        third_number = float(input("Enter third number: "))

        select = int(input(f"Select from the following {FS.ENABLE_ITALIC}MAX[1], MIN[2], AVG[3]: {FS.reset}"))

        if select == 1:
            if first_number == second_number == third_number:
                print("All 3 inputs have the same value.", "\n")
            elif first_number > second_number > third_number:
                print("First number is max value", "\n")
            elif first_number < second_number > third_number:
                print("Second number is max value", "\n")
            elif first_number < second_number < third_number:
                print("Third number is max value", "\n")
        elif select == 2:
            if first_number == second_number == third_number:
                print("All 3 inputs have the same value.", "\n")
            elif first_number < second_number < third_number:
                print("First number is min value", "\n")
            elif first_number > second_number < third_number:
                print("Second number is min value", "\n")
            elif first_number > second_number > third_number:
                print("Third number is min value", "\n")
        elif select == 3:
            print((first_number + second_number + third_number) / 3, "\n")
        else:
            print(f"Select is only one of the following {FS.ENABLE_ITALIC}MAX[1], MIN[2], AVG[3]{FS.reset}", "\n")

    except ValueError as TYPE_INFO:
        if first_number is None:
            print(f"ValueError: first number {TYPE_INFO} to float.", "\n")
        elif second_number is None:
            print(f"ValueError: second number {TYPE_INFO} to float.", "\n")
        elif third_number is None:
            print(f"ValueError: third number {TYPE_INFO} to float.", "\n")
        elif select is None:
            print(f"ValueError: select {TYPE_INFO} to int.", "\n")

def task3():
    meter = select = None

    try:
        print("Task 3")
        meter = float(input("Enter a meter value: "))

        select = int(input(f"Select from the following {FS.ENABLE_ITALIC}Meter to Miles[1],"
                           f" Meter to Inches[2], Meter to Yard[3]: {FS.reset}"))

        if select == 1:
            result = meter * 0.000621371
            print(result)
        elif select == 2:
            result = meter * 39.3701
            print(result)
        elif select == 3:
            result = meter * 1.09361
            print(result)
        else:
            print(f"Select is only one of the following {FS.ENABLE_ITALIC}Meter to Miles[1],"
                  f"Meter to Inches[2], Meter to Yard[3]{FS.reset}", "\n")

    except ValueError as TYPE_INFO:
        if meter is None:
            print(f"ValueError: meter {TYPE_INFO} to float.", "\n")
        elif select is None:
            print(f"ValueError: select {TYPE_INFO} to int.", "\n")

if __name__ == '__main__':
    task1()
    task2()
    task3()