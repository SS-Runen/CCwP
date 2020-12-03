import timeit
import pprint

# string_alnum = r"""abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 0123456789
# """.replace("\n", "")


def make_list(string):
    return list(string)


def make_dict(string):
    dictionary = {}
    for char in string:
        dictionary[char] = None

    return dictionary


def make_dict_comprehension(string):
    return {char: None for char in string}


def search_list(string, lst):
    for char in string:
        if char in lst:
            continue

    return None


def search_dict(string, hashmap):
    for char in string:
        if char in hashmap:
            continue

    return None


str_makestring = r"""
string_alnum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
"""

str_setup_search = r"""
string_alnum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def make_list(string):
    return list(string)


def make_dict(string):
    dictionary = {}
    for char in string:
        dictionary[char] = None

    return dictionary


def make_dict_comprehension(string):
    return {char: None for char in string}


def search_list(string, lst):
    for char in string:
        if char in lst:
            continue

    return None


def search_dict(string, hashmap):
    for char in string:
        if char in hashmap:
            continue

    return None

dictionary = make_dict(string_alnum)
dictionary_comp = make_dict_comprehension(string_alnum)
lst = make_list(string_alnum)
"""

str_makelist = r"""
def make_list(string):
    return list(string)

make_list(string_alnum)
"""

str_makedict = r"""
def make_dict(string):
    dictionary = {}
    for char in string:
        dictionary[char] = None

    return dictionary

make_dict(string_alnum)
"""

str_makedict_comp = r"""
def make_dict_comprehension(string):
    return {char: None for char in string}

make_dict_comprehension(string_alnum)
"""

str_searchlist = """
search_list(string_alnum, lst)
"""

str_searchdict = """
search_dict(string_alnum, dictionary)
"""

str_searchdict_comp = """
search_dict(string_alnum, dictionary_comp)
"""

dict_creation_times = {}
for alias, creation_string in {
    "dict": str_makedict, "list": str_makelist, "dict_comp": str_makedict_comp
        }.items():

    exec_timer = timeit.Timer(
        stmt=creation_string,
        setup=str_makestring
    )
    try:
        dict_creation_times[alias] = exec_timer.timeit(
            number=10000
        )
    except Exception as e:
        exec_timer.print_exc()

pprint.pprint(dict_creation_times)

dict_searchtimes = {}
for alias, str_call in {
    "search_list": str_searchlist,
    "search_dict": str_searchdict,
    "search_dict_c": str_searchdict_comp
        }.items():

    s_exec_timer = timeit.Timer(
        stmt=str_call,
        setup=str_setup_search
    )
    try:
        dict_searchtimes[alias] = s_exec_timer.timeit(
            number=10000
        )
    except Exception as e:
        s_exec_timer.print_exc()

pprint.pprint(dict_searchtimes)
