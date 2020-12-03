import os
import pprint
import math
import sys
import datetime as dt
from pathlib import Path

import RotateCipher
import ShiftCipher
import TranspositionCipher


def process_textfile(
    string_path: str,
    encryption_algorithm: str,
    algorithm_key: float,
    output_folderpath: str = str(
        Path(os.path.expandvars("$HOME")).anchor
    ) + r"/EncryptDecrypt/",
    output_filename: str = r"EncryptDecrypt.txt",
    to_decrypt=False,
    **kwargs
        ):

    encryption_algorithm = encryption_algorithm.lower()
    available_algorithms = ["rotate", "transposition"]
    if encryption_algorithm not in available_algorithms:
        pprint.pprint(
            ["Enter an algorithm from the list. Not case-sensitive.",
                available_algorithms]
        )
        return None

    # A single dictionary may be passed as a **kwarg if it is the
    # ONLY KEY-WORD ARGUMENT. Else, error is thrown.
    lst_kwargs = list(kwargs.values())
    if len(lst_kwargs) == 1 and (isinstance(lst_kwargs[0], dict)):
        kwargs = lst_kwargs[0]

    # Key in **kwargs overwrites `algorithm_key` function parameter.
    if "algorithm_key" in kwargs:
        algorithm_key = float(kwargs["algorithm_key"])

    # Convert strings saying "True" or "False" to booleans.
    for key, value in kwargs.items():
        str_value = str(value)
        if str_value.lower() == "False":
            kwargs[key] = False
        elif str_value.lower() == "True":
            kwargs[key] = True

    output_filename = ('/' + output_filename)
    if not (output_filename.endswith(".txt")):
        output_filename += ".txt"

    full_outputpath = output_folderpath + output_filename
    path_input = Path(string_path)

    # fileobj_target = open(path_input, 'r')  # Only for Python 3.6 and later.
    fileobj_target = open(str(path_input), 'r')
    lst_input = fileobj_target.readlines()
    # str_input = '\n'.join(lst_input)
    str_input = "".join(lst_input)
    output_string = "None"

    print(
        """Started processing.
    Key-word arguments for %s algorithm:""" % encryption_algorithm
    )
    pprint.pprint(kwargs)

    if (encryption_algorithm == "transposition") and to_decrypt is True:
        output_string = ''.join(
            TranspositionCipher.decrypt_transposition(
                str_input, int(algorithm_key)
                )
            )
    elif encryption_algorithm == "transposition" and not to_decrypt:
        output_string = ''.join(
            TranspositionCipher.encrypt_transposition(
                str_input, int(algorithm_key)
                )
        )
    elif encryption_algorithm == "rotate":
        warning = """
        When the algorithm is set to rotate, the "to_decrypt" parameter
        is ignored. To decrypt, set the key-word argument shift left
        so that it reverses the shift direction during encryption.
        Ex: If the text was shifted left, i.e. values were swapped
        with those "higher" up on the list read from left to right, pass
        the key-word argument shift_left=False to decrypt.

        RotateCipher's methods can return a list. However, it is
        forced to always return a string. Passing return_list=True as
        a key-word argument will have no effect. The argument is not
        passed to RotateCipher.
        """
        # pprint.pprint(warning)  # Included literl \n and single quotes.
        print(warning)

        to_shiftleft = True
        if "shift_left" in kwargs:
            to_shiftleft = kwargs["shift_left"]

        process_numbers = False
        if "shift_numbers" in kwargs:
            process_numbers = kwargs["shift_numbers"]

        output_string = RotateCipher.rot13_e(
                string=str_input,
                shift_left=to_shiftleft,
                rotations=int(algorithm_key),
                # return_list=kwargs["return_list"],  # Removed for safety.
                shift_numbers=process_numbers
            )

    if not (os.path.exists(output_folderpath)):
        os.mkdir(output_folderpath)

    fileobj_output = open(
        full_outputpath,
        'a'  # Create a file and open it for writing. Append if exists.
    )
    fileobj_output.write(
        "\n=====\nEncryptDecrypt Output on\n%s\n=====\n" %
        dt.datetime.now()
        )
    fileobj_output.write(output_string)
    fileobj_output.close()
    print("Done processing. Output folder:\n{}".format(
        Path(full_outputpath)
        )
    )

    return {
        "output_file": Path(full_outputpath).resolve(),
        "output_text": output_string
        }


def manual_test():
    dict_processedtext = process_textfile(
            string_path=r"C:\Users\Rives\Downloads\Quizzes\Quiz 0 Overwrite Number 1.txt",
            encryption_algorithm="rotate",
            algorithm_key=1,
            shift_left=True
        )
    print("Encrypt ROT1 with default values.")
    # pprint.pprint(
    #     dict_processedtext
    # )
    print(dict_processedtext["output_file"])

    dict_processedtext2 = process_textfile(
            string_path=dict_processedtext["output_file"],
            encryption_algorithm="rotate",
            algorithm_key=1,
            output_folderpath=r"C:\Users\Rives\Downloads\Decryptions",
            output_filename="Quiz 0 Overwrite Number 1 Decrypted",
            shift_left=False
        )
    print("Decrypt ROT1 with all values user-supplied.")
    print(dict_processedtext["output_file"])

    for i in range(2):
        dict_processedtext3a = process_textfile(
                string_path=r"C:\Users\Rives\Downloads\Quizzes\Quiz 0 Overwrite Number 2.txt",
                encryption_algorithm="rotate",
                algorithm_key=1,
                output_folderpath=r"C:\Users\Rives\Downloads\Encryptions"
            )
        print(dict_processedtext3a["output_file"])

        dict_processedtext3b = process_textfile(
                string_path=dict_processedtext3a["output_file"],
                encryption_algorithm="rotate",
                algorithm_key=1,
                output_folderpath=r"C:\Users\Rives\Downloads\Decryptions",
                output_filename="Quiz 0 Overwrite Number 2 Decrypted",
                shift_left=False
            )
        print(dict_processedtext3b["output_file"])

    return None


def main():

    while True:
        print("Press Enter or New Line to skip entering any input.\t")
        task = input("Encrypt or decrypt? Encrypts by default. Press E/D.\t")
        algo = input("Algorithm? Uses Rotate by default.\t")
        algorithm_key = float(input("Key? Uses 1 by default.\t"))
        input_filepath = input(
            """Mandatory / Required.
            Full path of target file. Includes file name and extension.\n""")
        output_folder = input(
            "Optional. Give the path of the output folder.\n"
            )
        output_file = input(
            "Optional. Default output file name is EncryptDecrypt.txt.\n")
        keyword_arguments = input(
            """Last question. Depends on algorithm.
            Format: "key=value,key2,value2,...".
            Use comma with no space as separator for two or more items.\n"""
        )

        while len(input_filepath) == 0:
            input_filepath = input(
                """Mandatory / Required.
                Full path of target file.
                Includes file name and extension.\n"""
                )

        dict_kwargs = dict()
        for pair in keyword_arguments.split(','):
            try:
                key, pair = tuple(pair.split('='))
                dict_kwargs[key] = pair
            except ValueError:
                break

        to_decrypt = False
        if task.lower().startswith('d'):
            to_decrypt = True

        if len(output_folder) == 0:
            output_folder = str(Path.cwd().parent / r"/EncryptDecrypt/")

        if len(output_file) == 0:
            output_file = "EncryptDecrypt.txt"

        if len(algo) == 0:
            algo = "rotate"

        pprint.pprint(
            process_textfile(
                string_path=input_filepath,
                encryption_algorithm=algo,
                algorithm_key=algorithm_key,
                output_folderpath=output_folder,
                output_filename=output_file,
                to_decrypt=to_decrypt,
                kwargs_dict=dict_kwargs
            )
        )
        print(
            """Done Running.
    Press Q to quit, any other key to process another file.""")

        to_quit = input()
        if to_quit.lower().startswith("q"):
            sys.exit()
        else:
            continue
    # manual_test()

    return None


if __name__ == "__main__":
    main()

"""
Notes:

*
The declared parameter data types in python functions are not enforced as of
version 3.4.

*
For some reason, even if the name "key" was a parameter for process_textfile,
it was being passed to rot13_e as a string. In the function process_textfile,
Visual Basic also listed "key" as a string when passed to rot13_e even though
the function definition specified its data type as a float and the user input
for "key" was also converted to a float in the main function. This was caused
by a for-loop. When VS Code followed the definition of key (F12) when it
was passed to rot13_e, VS Code pointed to the temporary variable "key" in a
for-loop. The parameter name was changed as a quick fix.

- Adding an else clause to the for-loop did not fix it.
- The for-loop declaration was funciton-level code while the call to rot13_e
that bugged was inside an else-clause. The else-clause holding the call to
rot13_e was also function-level, same as the for-loop declaration. The call
to RotateCipher.rot13_e was assigned to output_string.
"""
