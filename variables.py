#task 1
def result():
    try:
        print("Task 1")
        A = float(input("Enter value A: "))
        B = float(input("Enter value B: "))
        C = float(input("Enter value C: "))

        sum = A + B + C
        mult = A * B * C
        print (f"The sum is: {sum}\nThe product of numbers is: 3{mult}\n")

    except Exception as e:
        print(e, "\n")

#task 2
def remains():
    try:
        print("Task 2")
        salary = float(input("Enter the salary amount: "))
        toPay = float(input("Enter the credit payment amount: "))
        charge = float(input("Enter the utility bill amount: "))

        result = salary - toPay - charge
        print(f"Your money now is: {result}\n")

    except Exception as e:
        print(e, "\n")


#task 3
def formula():
    try:
        print("Task 3")
        d1 = float(input("Enter the 1st diagonal: "))
        d2 = float(input("Enter the 2nd diagonal: "))

        result = d1 * d2 / 2
        print(f"The area of a rhoumbus is: {result}\n")

    except Exception as e:
        print(e, "\n")


if __name__ == '__main__':
    result()
    remains()
    formula()