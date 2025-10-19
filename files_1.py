# regular_text = input()
# newline_text = '\n' + input()

# try:
#     file = open('test.txt', 'r')
#     result = file.read()
#     print(result)
# except FileNotFoundError as ERROR_LOG:
#     print(f'{ERROR_LOG}')


import string
punctuation = string.punctuation

# doesn't work as intended
def task1(source_file, dest_file):
    store_str = ''

    with open(source_file, 'r') as src:
        for line in src:
            words = line.split()
            for word in words:
                modified_word = word.strip(punctuation)
                if len(modified_word) >= 7:
                    store_str += modified_word + ' '

    with open(dest_file, 'w') as newf:
        newf.write(store_str.strip())

task1(source_file='test.txt', dest_file='new_file.txt')

def task6(source_file, dest_file):
    with open(source_file, 'r') as src:
        content = src.readlines()

    store_str = ''

    star = '*'
    ampersand = '&'

    modified_line = ''

    for line in content:
        if star in line and ampersand in line:
            modified_line = line.replace(star, '#').replace(ampersand, star).replace('#', ampersand)
        elif star in line:
            modified_line = line.replace(star, ampersand)
        elif ampersand in line:
            modified_line = line.replace(ampersand, star)

        store_str += modified_line

    with open(dest_file, 'w') as newf:
        newf.write(store_str)




# task6(source_file='test.txt', dest_file='new_file.txt')


def task8(source_file, _list):
    file = open(source_file, 'w')

    for i in range(len(_list)):
        file.write(_list[i] + '\n')



# strlist = ['kfdias', '5e23y81xx', '0xxd']
# task8(source_file='test.txt', _list=strlist)


def task9(source_file):
    with open(source_file, 'r') as src:
        file_content = src.read()
        print(len(file_content))

# task9(source_file='test.txt')

def task10(source_file):
    with open(source_file, 'r') as src:
        file_content = src.readlines()
        print(len(file_content))

# task10(source_file='test.txt')