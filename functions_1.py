def split(str_object: str, separator: str) -> str:
    """
    Splits a string into a list of substrings based on the given separator.

    str_object: The string to be split.
    separator: The separator used to divide the string into parts. Must be a string.
    return: A list of substrings obtained by splitting the input string.
    """

    _list = []
    _temp_string = ""

    if not separator:
        print("ValueError: empty separator")
        return ""

    for char in str_object:
        if char == separator:
            _list.append(_temp_string)
            _temp_string = ""
        elif char != separator:
            _temp_string += char

    if _temp_string:
        _list.append(_temp_string)
    if str_object[-1] == " ":
         _list.append("")


    return _list



def strip(str_object: str, remove_element: str) -> str:
    """
    Removes an element and puts into string based on the given string value.

    str_object: String object
    remove_element: Remove by string object
    return: Returns string
    """

    _Size = len(str_object)

    start = 0
    while start < _Size and str_object[start] in remove_element:
        start += 1

    end = _Size - 1
    while end > start and str_object[end] in remove_element:
        end -= 1

    return str_object[start:end + 1]



def insert(list_object: list, index: int, value: str | int | float | bool) -> list:
    """
    Inserts a value into a list by given index.

    list_object: List type object
    index: Index of the list object
    value: Value may be represented as string/int/float/bool
    return: Returns list
    """

    _Size = len(list_object)
    _new_list = []

    if index > _Size:
        _new_list = list_object + [value]
    elif index >= 0:
        for ele in range(_Size):
            _current_ele = list_object[ele]

            if ele == index:
                _new_list.append(value)
            _new_list.append(_current_ele)
    elif index < 0:
        pos_index = _Size + index

        if pos_index < 0:
            _new_list.append(value)
            _new_list.extend(list_object)
        else:
            for ele in range(_Size):
                _current_ele = list_object[ele]

                if ele == pos_index:
                    _new_list.append(value)
                _new_list.append(_current_ele)


    return _new_list


# custom split
split_test = "I J. d@!"
print(split(split_test, " "))

# embedded split
print(split_test.split(" "))


print()


# custom strip
strip_test = "  banana,k  "
print(strip(strip_test, " ,k"))

# embedded strip
print(strip_test.strip(" ,k"))


print()


# custom insert
insert_test = ["start", 1, 0.3, True, 22, "end"]
print(insert(insert_test, 3, 3))

# embedded insert
insert_test.insert(3, 3)
print(insert_test)