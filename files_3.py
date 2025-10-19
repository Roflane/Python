import string, pickle

# Checks whether id exists or not
def isUnique_user(target_database, user_id):
    with open(target_database, 'rb') as file:
        try:
            content = pickle.load(file)
        except EOFError:
            content = []

    for line in content:
        if user_id in line:
            return False

    return True

# Checks whether db exists or not
def isDB_exist(target_database):
    try:
        open(target_database, 'rb')
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

def save_data(target_database, data, mode='wb'):
    with open(target_database, mode) as data_file:
        pickle.dump(data, data_file)

def load_data(target_database):
    try:
        with open(target_database, 'rb') as data_file:
            return pickle.load(data_file)
    except EOFError:
        return []

def database_logic(target_database):

    if isDB_exist(target_database):
        db_file = load_data(target_database)

        content = [ele.strip() for ele in db_file]
        print(f"DB Init: {content}\n")

        while True:
            print("1. Add a new user\n"
                  "2. Find a user\n"
                  "3. Delete the user by ID, Username and Email\n"
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
                    content.append(data_format)
                    save_data(target_database, content)
                    print("Log: The user has been successfully added to the file.\n")
                else:
                    print("Error: invalid data.\n")
            elif user_choice == 2:
                user_id = input("Enter an ID: ")

                if user_id:
                    user_name = ""
                    user_email = ""

                    for line in content:
                        if line.startswith(f"{user_id}:"):
                            found_data = line.strip().split(":")

                            if len(found_data) == 3:
                                user_name = found_data[1]
                                user_email = found_data[2]
                            break

                    if user_name and user_email:
                        print(f'Found user: User id: {user_id} | Username: {user_name} | User email: {user_email}\n')
                    else:
                        print(f"Notification: there isn't such user with the ID: {user_id}\n")
            elif user_choice == 3:
                user_id, user_name, user_email = get_user_data()
                data_format = f"{user_id}:{user_name}:{user_email}"

                if userdata_valiation(user_id, user_name, user_email):
                    updated_content = [line for line in content if line.strip() != data_format]

                    # updated_content = []
                    #
                    # for line in content:
                    #     if line.strip != data_format:
                    #         updated_content.append(line)

                    if len(content) != len(updated_content):
                        save_data(target_database, updated_content)
                        print(f"User {data_format} has been deleted successfully.\n")
                    else:
                        print(f"Error: User {data_format} not found.\n")
                else:
                    print("Error: invalid data.\n")

            elif user_choice == 4:
                break

database_logic(target_database='database.txt')