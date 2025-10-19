import string, random

def check_seq(pw):
    for i in range(1, len(pw)):
        if pw[i] == pw[i - 1]:
            return True
    return False


def except_patterns(pw, name):
    blacklist_patterns = ['12345', 'qwerty', name]
    for pattern in blacklist_patterns:
        if pattern in pw:
            return True
    return False


def generate_pw(length, char_types):
    pw = ""
    rand_upper = string.ascii_uppercase
    rand_lower = string.ascii_lowercase
    rand_digit = string.digits
    rand_symbol = string.punctuation

    if char_types == 1:
        for i in range(length):
            pw += random.choice(rand_upper + rand_lower + rand_digit + rand_symbol)

        if rand_digit not in pw:
            rng = random.randint(0, len(pw) - 1)
            pw = pw[:rng] + random.choice(rand_digit) + pw[rng + 1:]

    elif char_types == 2:
        for i in range(length):
            pw += random.choice(rand_upper + rand_lower)
    elif char_types == 3:
        for i in range(length):
            pw += random.choice(rand_digit + rand_symbol)
    elif char_types == 4:
        for i in range(length):
            pw += random.choice(rand_upper + rand_digit)
    elif char_types == 5:
        for i in range(length):
            pw += random.choice(rand_lower + rand_symbol)

    return pw


def main():
    print("Введите длину пароля от 8 до 16, чтобы сгенерировать случайный пароль.")
    print("Паттерны символов: 1 - Все, 2 - Заглавные и строчные, "
          "3 - Цифры и специальные символы, 4 - Заглавные и цифры, 5 - Строчные и специальные символы.")

    min_len = 8
    max_len = 16
    min_type = 1
    max_type = 5


    name = input("Введите ваше имя: ")
    if not name.strip():
        print("Ошибка: имя не может быть пустым.")
        return
    elif not name.isalpha():
        print("Ошибка: имя должно содержать только буквы.")
        return


    length = int(input("Введите длину пароля: "))
    char_types = int(input("Введите номер паттерна символов: "))


    if not min_len <= length <= max_len or char_types not in range(1, char_types + 1):
        print(f"Уведомление: допустимой длиной является {min_len} - {max_len}")
        print(f"Уведомление: допустимыми номерами паттерна являются {min_type} - {max_type}")
        return

    print()

    pw = generate_pw(length, char_types)
    while check_seq(pw) or except_patterns(pw, name):
        pw = generate_pw(length, char_types)
    print(f"Сгенерированный пароль: {pw}")

main()