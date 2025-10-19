import string

# Checks wether id exists or not
def isUnique_user(target_database, user_id):
    with open(target_database, 'r') as file:
        content = file.readlines()

    for line in content:
        if user_id in line:
            return False

    return True

# Checks wether db exists or not
def isDB_exists(target_database):
    try:
        open(target_database, 'r')
    except FileNotFoundError as ERROR_LOG:
        print(f'{ERROR_LOG}')
        return False

    return True

# Checks whether email is valid or not
def isEmail_valid(user_email):
    if '@' not in user_email or '.' not in user_email:
        return False

    allowed_characters = f"{string.ascii_letters + string.digits}@.-_"
    for symbol in user_email:
        if symbol not in allowed_characters:
            return False

    return True

# Whitespace check
def userdata_valiation(user_id, user_name, user_email):
    if not user_id or not user_name or not user_email:
        return False

    return True

def get_user_data():
    user_id = input("Enter an ID: ").strip()
    user_name = input("Enter a username: ").strip()
    user_email = input("Enter an email: ").strip()

    return user_id, user_name, user_email


def database_logic(target_database):

    if isDB_exists(target_database):
        with open(target_database, 'r') as file:
            content = file.readlines()

        content = [ele.strip() for ele in content]
        print(f"DB Init: {content}\n")

        while True:
            print("1. Add a new user\n"
                  "2. Find a user\n"
                  "3. Delete the user by ID, Username and email\n"
                  "4. Exit\n")

            try:
                user_choice = int(input("Your choice: "))
                if not 1 <= user_choice <= 4:
                    print("Error: invalid user choice. (1-4 expected)")
            except ValueError as ERROR_LOG:
                print(f"Error: {ERROR_LOG}\n")
                continue

            if user_choice == 1:
                user_id, user_name, user_email = get_user_data()

                data_format = f"{user_id}:{user_name}:{user_email}"

                if userdata_valiation(user_id, user_name, user_email) and isUnique_user(target_database, str(user_id)) and isEmail_valid(user_email):
                    with open(target_database, 'a') as file:
                        file.write(data_format + '\n')
                        print("Log: The user has been successfully added to the file.\n")
                else:
                    print("Error: invalid data.\n")


            elif user_choice == 2:
                user_id = input("Enter an ID: ")

                if user_id:
                    with open(target_database, 'r') as src:
                        content = src.readlines()

                    user_name = ""
                    user_email = ""

                    for line in content:
                        if line.startswith(f"{user_id}:"):
                            symbols = line.strip().split(":")
                            if len(symbols) >= 3:
                                user_name = symbols[1]
                                user_email = symbols[2]
                            break

                    if user_name and user_email:
                        print(f'Found user: User id: {user_id} | Username: {user_name} | User email: {user_email}\n')
                    else:
                        print(f"Notification: there isn't such user with the ID: {user_id}\n")

            elif user_choice == 3:
                user_id, user_name, user_email = get_user_data()

                data_format = f"{user_id}:{user_name}:{user_email}"

                if userdata_valiation(user_id, user_name, user_email):
                    with open(target_database, 'r') as file:
                        content = file.readlines()

                    with open(target_database, 'w') as file:
                        found = False
                        for line in content:
                            if line.strip() == data_format:
                                found = True
                            else:
                                file.write(line)

                        if found:
                            print(f"User {data_format} has been deleted successfully.\n")
                        else:
                            print(f"Error: User {data_format} not found.\n")
                else:
                    print("Error: invalid data.\n")

            elif user_choice == 4:
                break

database_logic(target_database='database.txt')