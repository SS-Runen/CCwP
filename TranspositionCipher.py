"""
Review:
This problem would have been solved 20-30 minutes faster if
the initial variable groups_tomake had been printed out.
The idea of printing or value-checking all variables even
if they look correct in code was not followed. The error was
missed due to human error in reading the variable names.

Next, visualization should be done either on paper or
using print statements, not just in-your-head. References
are needed to make visualization fast and accurate. Using
the pprint.pprint function on the arrays would have made
visualizing and simulation much easier. Also, the images
for the problem and manual solution were not looked at for
long enough. If these images or the pprint method were used,
the reason why a few letters were misplaced with most others
being correctly translated would have been found earlier.

Special note:
The operation where every letter in each "column" becomes a
part of the cipher text appears to be a matrix transposition.
Attempt to use NumPy on this step later.
"""
import math
import pprint


def encrypt_transposition(plaintext, key):

    ciphertext = ""
    lst_plaintext = list(plaintext)
    lst_rows = []
    groups_tomake = (len(plaintext) // key) + 1
    # print("Groups:", groups_tomake)

    for counter in range(groups_tomake):
        lst_group_asrow = []

        for group_index in range(key):
            try:
                # print(group_index, lst_plaintext[0])
                lst_group_asrow.append(lst_plaintext.pop(0))
            except IndexError:
                # lst_group_asrow.append(' ')
                break

        # print(lst_group_asrow, counter)
        lst_rows.append(lst_group_asrow)

    pprint.pprint(lst_rows)
    # print(''.join([''.join(group) for group in lst_rows]))

    for column_index in range(key):

        for group in lst_rows:
            try:
                ciphertext += group[column_index]
            except IndexError:
                continue

    return ciphertext


def decrypt_transposition(ciphertext, key):
    # Key is always equal to plaintext column count.
    lst_ciphertext = list(ciphertext)
    str_plaintext = ""
    lst_plaintext_columns = []
    plaintext_column_size = math.ceil(len(ciphertext) / key)
    blank_columntails_count = (key * plaintext_column_size) - len(ciphertext)
    full_columns_count = (key - blank_columntails_count)
    print(
        "Number of items in columns created in encrypting plain text:",
        plaintext_column_size
        )
    print(
        """Number of columns of plaintext is equal to key.
            Key, i.e. Column Count:""",
        key
        )
    print(
        "Number of columns filled completely during encryption:",
        full_columns_count
        )

    for column_number in range(key):
        lst_column = []

        for column_index in range(plaintext_column_size):
            try:
                if (
                    column_number > (full_columns_count - 1) and
                    column_index == (plaintext_column_size - 1)
                        ):

                    lst_column.append("")
                else:
                    lst_column.append(lst_ciphertext.pop(0))

            except IndexError:
                break

        lst_plaintext_columns.append(lst_column)

    pprint.pprint(lst_plaintext_columns)

    for column_member in range(plaintext_column_size):
        for column_number in range(key):
            try:
                head_char = lst_plaintext_columns[column_number].pop(0)
                str_plaintext += head_char
            except IndexError:
                # Break and process next column.
                break

    # return str_plaintext.strip()
    return str_plaintext


def main(string, key):
    str_encrypted = encrypt_transposition(string, key)
    print(str_encrypted + '|')
    print(decrypt_transposition(str_encrypted, key))
    return None


if __name__ == "__main__":
    message = "Common sense is not so common."
    key = 8
    main(message, key)
