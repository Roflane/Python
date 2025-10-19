database = [
    ["User1", 30, 100],
    ["User2", 35, 200],
    ["User3", 40, 300],
    ["User4", 45, 400],
    ["User4", 45, 400]
]

while True:
    print("1. Show users\n"
          "2. Add a new user\n"
          "3. Delete the user by username/age/salary\n"
          "4. Exit\n")


    user_choice = input("Your choice: ").strip()
    if not user_choice.isdigit():
        print("Error: choice should be only digit value.\n")
        continue

    user_choice = int(user_choice)
    if not 1 <= user_choice <= 4:
        print("Error: the number should be between 1 and 4.\n")
        continue


    if user_choice == 1:
        if not database:
            print("List is empty")
            continue

        user_count = 0
        for user in database:
            user_count += 1
            print(f"No.{user_count}")
            print(f"Name: {user[0]}\n"
                  f"Age: {user[1]}\n"
                  f"Salary: {user[2]}\n")


    elif user_choice == 2:
        user_name = input("Enter name: ").strip()
        user_age = input("Enter age: ").strip()
        user_salary = input("Enter salary: ").strip()

        if not user_age.isdigit():
            print("Error: age should be a valid integer value.\n")
            continue

        user_age = int(user_age)
        if not 18 <= user_age <= 65:
            print("Error: The age should be between 18 and 65.\n")
            continue

        if user_salary.isdigit():
            user_salary = float(user_salary)
        else:
            temp_salary = user_salary.split('.')
            if len(temp_salary) != 2 or not temp_salary[0].isdigit() or not temp_salary[1].isdigit():
                print("Error: salary should be either a decimal or a floating-point value.\n")
                continue
            user_salary = float(user_salary)


        database.append([user_name, user_age, user_salary])
        print("Log: the user has been successfully added to the list.\n")

    elif user_choice == 3:
        print("Remove user by options: username[1], age[2] or salary[3].\n")

        remove = input("").strip()

        if remove == "":
            print("Error: invalid remove option value.\n")
            continue
        if not remove.isdecimal():
            print("Error: remove option should be a digit value.\n")
            continue

        remove = int(remove)
        if not 1 <= remove <= 3:
            print("Error: the number should be between 0 and 3.\n")
            continue


        if remove == 1:
            get_username = input("Enter a username in order to delete user: ").strip()

            if get_username == "":
                print("Error: invalid username value.\n")
                continue
            if not get_username.isalnum():
                print("Error: username should be alphabetic or digit value.\n")
                continue

            count = 0
            unique_database = []

            i = 0
            while i < len(database):
                if database[i][0] == get_username:
                    unique_database.append(i)
                    count += 1
                i += 1

            if count == 0:
                print(f"No user found with username '{get_username}'.\n")
                continue
            elif count == 1:
                database.pop(unique_database[0])
                print(f"User {get_username} successfully removed.\n")
            else:
                print(f"Multiple users found with username '{unique_database}':")
                
                for j in range(len(unique_database)):
                    user = database[unique_database[j]]
                    print(f"{j + 1}. Age: {user[1]}, Salary: {user[2]}")


                choice = input("Enter the number of the user to delete: ").strip()

                if not choice.isdigit() or not (1 <= int(choice) <= len(unique_database)):
                    print("Error: invalid choice.\n")
                    continue

                choice = int(choice) - 1
                database.pop(unique_database[choice])
                print(f"User {get_username} successfully removed.\n")


        elif remove == 2:
            get_age = input("Enter an age in order to delete user: ").strip()

            if get_age == "":
                print("Error: invalid age value.\n")
                continue
            if not get_age.isdecimal():
                print("Error: age should be a decimal value.\n")
                continue

            get_age = int(get_age)

            count = 0
            unique_database = []

            i = 0
            while i < len(database):
                if database[i][1] == get_age:
                    unique_database.append(i)
                i += 1

            if not unique_database:
                print(f"No user found with age '{get_age}'.\n")
                continue

            if len(unique_database) == 1:
                database.pop(unique_database[0])
                print(f"User with age {get_age} successfully removed.\n")
            else:
                print(f"Multiple users found with age '{unique_database}':")

                for j in range(len(unique_database)):
                    user = database[unique_database[j]]
                    print(f"{j + 1}. Username: {user[0]}, Age: {user[1]}, Salary: {user[2]}")

                choice = input("Enter the number of the user to delete: ").strip()

                if not choice.isdigit() or not (1 <= int(choice) <= len(unique_database)):
                    print("Error: invalid choice.\n")
                    continue

                choice = int(choice) - 1
                database.pop(unique_database[choice])
                print(f"User with age {get_age} successfully removed.\n")

        elif remove == 3:
            get_salary = input("Enter a salary in order to delete user: ").strip()

            if get_salary == "":
                print("Error: invalid salary value.\n")
                continue

            get_salary = float(get_salary)
            unique_database = []

            i = 0
            while i < len(database):
                if database[i][2] == get_salary:
                    unique_database.append(i)
                i += 1

            if not unique_database:
                print(f"No user found with salary '{get_salary}'.\n")
                continue

            if len(unique_database) == 1:
                database.pop(unique_database[0])
                print(f"User with salary {get_salary} successfully removed.\n")
            else:
                print(f"Multiple users found with salary '{get_salary}':")

                for j in range(len(unique_database)):
                    user = database[unique_database[j]]
                    print(f"{j + 1}. Username: {user[0]}, Age: {user[1]}, Salary: {user[2]}")

                choice = input("Enter the number of the user to delete: ").strip()

                if not choice.isdigit() or not (1 <= int(choice) <= len(unique_database)):
                    print("Error: invalid choice.\n")
                    continue

                choice = int(choice) - 1
                database.pop(unique_database[choice])
                print(f"User with salary {get_salary} successfully removed.\n")

    elif user_choice == 4:
        break