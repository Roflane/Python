def task1():
    print("Task 1")
    get_year = int(input("Enter the year: "))

    if (get_year % 4 == 0 and get_year % 100 != 0) or (get_year % 400 == 0):
        print(f"The year {get_year} is a leap year.", "\n")
    else:
        print(f"The year {get_year} is not a leap year.", "\n")


def task2():
    print("Task 2")
    user_input = int(input("Enter a number: "))

    if (user_input > 0) and (user_input <= 100):
        print(f"{user_input} is a positive integer within the allowed range (1-100).", "\n")
    elif user_input > 100:
        print(f"{user_input} is a positive integer exceeding the allowed range (1-100).", "\n")
    elif user_input < 0:
        print(f"{user_input} is a negative integer.", "\n")
    elif user_input == 0:
        print(f"{user_input} is zero, which is neither positive nor negative.", "\n")

def task3():
    print("Task 3")
    user_input = int(input("Enter a number: "))

    if 20 < user_input < 50 and user_input % 5 == 0:
        print(f"{user_input} is a positive integer within the allowed range (20-50) and divisible by 5.", "\n")
    elif 20 < user_input < 50:
        print(f"{user_input} is a positive integer within the allowed range (20-50), but not divisible by 5.", "\n")
    elif user_input % 5 == 0:
        print(f"{user_input} is divisible by 5 but is outside the allowed range (20-50).", "\n")
    else:
        print(f"{user_input} doesn't meet any conditions.", "\n")


def task4():
    print("Task 4")
    user_input = input("Enter a sound pattern: ")

    match user_input:
        case "meow" | "мяу":
            print("Cat is saying meow", "\n")
        case "bark" | "гав":
            print("Dog is barking", "\n")
        case "moo" | "му":
            print("Cow is doing moo", "\n")

        case _:
            print("Error: unknown sound pattern", "\n")

def task5():
    print("Task 5")
    user_input = int(input("Enter a month number: "))

    match user_input:
        case 12 | 1 | 2:
            print("Current season is Winter", "\n")
        case 3 | 4 | 5:
            print("Current season is Spring", "\n")
        case 6 | 7 | 8:
            print("Current season is Summer", "\n")
        case 9 | 10 | 11:
            print("Current season is Fall", "\n")

        case _:
            print("Error: unknown month number", "\n")

def task6():
    print("Task 6")
    user_input = input("Enter a month name: ")

    match user_input:
        case "January" | "March" | "May" | "July" | "August" | "Octomber" | "December":
            print(f"There are 31 days in {user_input}", "\n")
        case "April" | "June" | "September" | "November":
            print(f"There are 30 days in {user_input}", "\n")
        case "February":
            get_year = int(input("Enter the year: "))

            if (get_year % 4 == 0 and get_year % 100 != 0) or (get_year % 400 == 0):
                print(f"There are 29 days in {user_input}", "\n")
            else:
                print(f"There are 28 days in {user_input}", "\n")

        case _:
            print("Error: unknown month name")

if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()