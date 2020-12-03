import sys


def rot13_a(message):
    trans_table = ''.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
        )

    return message.translate(trans_table)


def rot13_b(message):
    plain_text = ""
    dict_alphabet = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for index in range(len(alphabet)):
        dict_alphabet[index] = alphabet[index]

    for char in message:
        if char.isalpha():
            if chr(ord(char) + 13).isalpha():
                plain_text += chr(ord(char) + 13)
            else:
                upper_limit = ''
                if char.isupper():
                    upper_limit = ord('Z')
                    if dict_alphabet[0].islower():
                        for letter in dict_alphabet:
                            letter = letter.capitalize()
                if char.islower():
                    upper_limit = ord('z')
                    if dict_alphabet[0].isupper():
                        for letter in dict_alphabet:
                            letter = letter.lower()

                alphabet_index = (ord(char) + 13) - (upper_limit + 1)
                plain_text += dict_alphabet[alphabet_index]
        else:
            plain_text += char

    return plain_text


# Rotate function with helper function that can rotate/shift numbers from 0-9.


def rot13number_a(char_number):
    numbers = "0123456789"
    numbers_shifted = "4567890123"
    number_table = {}

    for index in range(len(numbers)):
        number_table[numbers[index]] = numbers_shifted[index]

    return number_table[char_number]


def rot13_rotnums(string, rot_numbers=False):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_shifted = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    rotated_text = []
    dict_table = {}

    for index in range(len(alphabet)):
        char = alphabet[index]
        rot_char = alphabet_shifted[index]
        dict_table[char] = rot_char

    for char in string:
        if char in alphabet:
            rotated_text.append(dict_table[char])
        elif (rot_numbers is True) and (char.isnumeric()):
            rotated_number = rot13number_a(char)
            rotated_text.append(rotated_number)
        else:
            rotated_text.append(char)

    return ''.join(rotated_text)


# Rotation function and helper function with variable rotation/shift times.


def rotate_left(array, n=1, return_string=False):
    backup = list(array).copy()
    new_array = list(array).copy()
    rotations_done = 0
    array_length = len(array)

    while rotations_done < n:
        for index in range(0, array_length-1):
            new_array[index] = backup[index+1]

        new_array[-1] = backup[0]
        backup = new_array.copy()
        rotations_done += 1

    if return_string is True:
        return ''.join(new_array)

    return new_array


def rot13number_b(string, rotations=13, return_list=False):
    lst_numbers = "0123456789"
    lst_numbers_shifted = rotate_left(
        array="0123456789",
        n=rotations
    )
    shift_table = {}
    str_rotated_string = ""

    for index in range(len(lst_numbers)):
        num = lst_numbers[index]
        rotated_num = lst_numbers_shifted[index]
        shift_table[num] = rotated_num

    for char in string:
        str_rotated_string += shift_table[char]

    if return_list is True:
        return list(str_rotated_string)

    return str_rotated_string


def shift_numbers(string, rotations):
    lst_rotated = list(string)
    lst_numberchars = []
    lst_numberchar_indexes = []

    for index in range(len(string)):
        char = string[index]

        if char.isnumeric():
            lst_numberchars.append(char)
            lst_numberchar_indexes.append(index)

    lst_numberchars = rot13number_b(
        string=lst_numberchars,
        rotations=rotations,
        return_list=False
    )

    for index in range(len(lst_numberchars)):
        numberchar_index = lst_numberchar_indexes[index]
        lst_rotated[numberchar_index] = lst_numberchars[index]

    return ''.join(lst_rotated)


def rot13_d(string, rotations=13, rotate_numbers=True, return_list=False):
    lst_rotated = list(string)
    alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
    alphabet_lowercase_shifted = rotate_left(
        array=alphabet_lowercase,
        n=rotations,
        return_string=True
        )

    alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_uppercase_shifted = rotate_left(
        array=alphabet_uppercase,
        n=rotations,
        return_string=True
    )

    shift_table = {}

    for index in range(len(alphabet_lowercase)):
        char = alphabet_lowercase[index]
        shift_table[char] = alphabet_lowercase_shifted[index]

    for index in range(len(alphabet_uppercase)):
        char = alphabet_uppercase[index]
        shift_table[char] = alphabet_uppercase_shifted[index]

    # print("Shift Table:\n", shift_table)

    if rotate_numbers is True:
        lst_rotated = list(shift_numbers(string, rotations=rotations))

    for index in range(len(string)):
        char = lst_rotated[index]

        if char.isalpha():
            lst_rotated[index] = shift_table[char]

    if return_list is True:
        return lst_rotated

    return ''.join(lst_rotated)


# Rotation function with helper functions for variable rotate/shift direction.


def rotate_right(A, n_times=1, return_string=False):
    if(len(A) == 0):
        return A
    if not (isinstance(A, list)):
        A = list(A)

    backup = [n for n in A]
    iterations = 0

    while(iterations < n_times):
        array_length = len(backup)
        for i in range(1, array_length):
            A[i] = backup[i - 1]

        A[0] = backup[-1]
        backup = A.copy()
        # print(iterations + 1, ':', A)
        iterations += 1

    return A


def rot13number_c(string, rotations=13, shift_left=True, return_list=False):
    lst_numbers = "0123456789"
    lst_numbers_shifted = ""

    if shift_left is True:
        lst_numbers_shifted = rotate_left(
            array=lst_numbers,
            n=rotations,
            return_string=True
        )
    else:
        lst_numbers_shifted = rotate_right(
            A=lst_numbers,
            n_times=rotations,
            return_string=True
        )

    shift_table = {}
    str_rotated_string = ""

    for index in range(len(lst_numbers)):
        num = lst_numbers[index]
        rotated_num = lst_numbers_shifted[index]
        shift_table[num] = rotated_num

    for char in string:
        str_rotated_string += shift_table[char]

    if return_list is True:
        return list(str_rotated_string)

    return str_rotated_string


def shift_numbers_b(string: str, rotations, shift_left: bool = True):
    lst_rotated = list(string)
    lst_numberchars = []
    lst_numberchar_indexes = []

    for index in range(len(string)):
        char = string[index]

        if char.isnumeric():
            lst_numberchars.append(char)
            lst_numberchar_indexes.append(index)

    lst_numberchars = rot13number_c(
        string=lst_numberchars,
        rotations=rotations,
        shift_left=shift_left
    )

    for index in range(len(lst_numberchars)):
        numberchar_index = lst_numberchar_indexes[index]
        lst_rotated[numberchar_index] = lst_numberchars[index]

    return ''.join(lst_rotated)


def rot13_e(
    string: str,
    shift_left: bool = True,
    rotations=13,
    return_list: bool = False,
    shift_numbers: bool = False
        ):

    lst_chars = list(string)
    alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
    alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lcase_shifted = ""
    alphabet_ucase_shifted = ""
    shift_table = {}

    if shift_left is True:
        alphabet_lcase_shifted = rotate_left(
            array=alphabet_lowercase,
            n=rotations,
            return_string=True
        )

        alphabet_ucase_shifted = rotate_left(
            array=alphabet_uppercase,
            n=rotations,
            return_string=True
        )
    else:
        alphabet_lcase_shifted = rotate_right(
            A=alphabet_lowercase,
            n_times=rotations,
            return_string=True
        )

        alphabet_ucase_shifted = rotate_right(
            A=alphabet_uppercase,
            n_times=rotations,
            return_string=True
        )

    for index in range(len(alphabet_lowercase)):
        char = alphabet_lowercase[index]
        shift_table[char] = alphabet_lcase_shifted[index]

    for index in range(len(alphabet_uppercase)):
        char = alphabet_uppercase[index]
        shift_table[char] = alphabet_ucase_shifted[index]

    if shift_numbers is True:
        lst_chars = list(
            shift_numbers_b(
                string=lst_chars,
                rotations=rotations,
                shift_left=shift_left
            )
        )

    for index in range(len(string)):
        char = lst_chars[index]

        if char.isalpha():
            lst_chars[index] = shift_table[char]

    if return_list is True:
        return lst_chars

    return ''.join(lst_chars)


def main():
    str_input = "EBG13 rknzcyr. mnmn"
    print(
        "ROT13 using Tranlation Table:\n",
        rot13_a(str_input)
        )

    print(
        "ROT13 Using For-loops and ASCII Values:\n",
        rot13_b(str_input)
    )

    print(
        "ROT13 Including Numbers:",
        rot13_rotnums(str_input, True)
    )

    print(
        "ROT13 Classic:\n",
        rot13_d(
            string=str_input,
            rotate_numbers=False
        )
    )

    print(
        "ROT13 Rotate Numbers:\n",
        rot13_d(
            string=str_input,
            rotations=13,
            rotate_numbers=True
        )
    )

    print(
        "ROT13 Rotate Letters by One and Return List:\n",
        rot13_d(
            string=str_input,
            rotations=1,
            rotate_numbers=False,
            return_list=True
        )
    )

    print(
        "ROT13 Rotate Letters by One and Return String (Defaul Setting):\n",
        rot13_d(
            string=str_input,
            rotations=1,
            rotate_numbers=False
        )
    )

    print(
        "ROT13 Rotate Letters and Numbers by One:\n",
        rot13_d(
            string=str_input,
            rotations=1,
            rotate_numbers=True
        )
    )

    print("==========\nMost Extended Version\n==========")
    print(
        "ROT13 Classic:\n",
        rot13_e(
            string=str_input,
            shift_numbers=False
        )
    )

    print(
        "ROT13 Rotate Numbers:\n",
        rot13_e(
            string=str_input,
            rotations=13,
            shift_numbers=True
        )
    )

    print(
        "ROT13 Rotate Letters by One and Return List:\n",
        rot13_e(
            string=str_input,
            rotations=1,
            shift_numbers=False,
            return_list=True
        )
    )

    print(
        "ROT13 Rotate Letters by One and Return String (Defaul Setting):\n",
        rot13_e(
            string=str_input,
            rotations=1,
            shift_numbers=False
        )
    )

    print(
        "ROT13 Rotate Letters and Numbers by One:\n",
        rot13_e(
            string=str_input,
            rotations=1,
            shift_numbers=True
        )
    )

    print(
        "\n=====CCwP=====\n`PRDRDFKF`:\n",
        rot13_e(
            string="PRDRDFKF",
            shift_left=False,
            rotations=17
        )
    )

    sys.exit()

    return None


if __name__ == "__main__":
    main()
