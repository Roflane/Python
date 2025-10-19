import sys, random


def task_1():
    print("Task 1")
    user_input = int(input("Enter a number: "))

    for i in range(1, 10+1, 1):
        result = f"{user_input} * {i} = {user_input*i}"
        print(f"{result}")
    print()

def task_2():
    print("Task 2")

    running = True
    while running:
        print("Currency exchanger")

        rub = 100.20
        krw = 1394.54
        yuan = 7.24
        yen = 154.96

        print("Current USD exchange rate: ", "\n"
              f"RUB - {rub}", "\n"
              f"KRW - {krw}", "\n"
              f"YUAN - {yuan}", "\n"
              f"YEN - {yen}", "\n")

        print("What would you like to do? - Currency calculator[1], Update currency data[2], Exit[3]")

        option = int(input())
        if option == 1:
            print("Available currency data: RUB, KRW, YUAN, YEN")
            select = input().upper()
            usd = float(input("Enter USD amount: "))
            if select == "RUB":
                print(f"{usd}$ is {usd * rub} RUB", "\n")
            elif select == "KRW":
                print(f"{usd}$ is {usd * krw} KRW", "\n")
            elif select == "YUAN":
                print(f"{usd}$ is {usd * yuan} YUAN", "\n")
            elif select == "YEN":
                print(f"{usd}$ is {usd * yen} YEN", "\n")
            else:
                print("Invalid currency.\n")
        elif option == 2:
            print("Current USD exchange rate: ", "\n"
                  f"RUB - {rub}", "\n"
                  f"KRW - {krw}", "\n"
                  f"YUAN - {yuan}", "\n"
                  f"YEN - {yen}", "\n")
        elif option == 3:
            print("Terminating program.")
            running = False
            sys.exit()
        else:
            print("Invalid option. Force close")
            running = False
            sys.exit()

def task_3():
    print("Task 3")
    first_th = int(input("Enter first number of the range: "))
    second_th = int(input("Enter second number of the range: "))

    while True:
        user_input = int(input(f"Enter a number included in range ({first_th} to {second_th}): "))
        if first_th <= user_input <= second_th:

            for i in range(first_th, second_th + 1):
                if i == user_input:
                    print(f"!{i}!", end=" ")
                else:
                    print(i, end=" ")
            print()
            break
        else:
            print(f"Number {user_input} is out of range. Try again.")

def task_4():
    print("Task 4")

    rng = (1, 500)
    __x = random.randint(rng[0], rng[1])
    print(f"Integer from {rng[0]} to {rng[1]} has been generated\n")

    counter = 0

    while True:
        option = int(input("Guess integer[1], Exit[0]\n"))

        if option == 1:
            user_input = int(input("Enter an integer: "))
            if user_input == __x:
                print(f"Correct!\nGuess attempts: {counter}")
            elif user_input != __x:
                print("Wrong!\n")
                counter += 1
        elif option == 0:
            print("Successfully exited")
            sys.exit()

task_1()
task_2()
task_3()
task_4()