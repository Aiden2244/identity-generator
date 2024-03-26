'''
main.py

Copyright (c) 2024 Aiden R. McCormack
This file is a part of new-alias, released under the MIT License

This file implements the main logic for new-alias. As I have plans to implement this program as a web
app or a Chrome extension, the code has been structured in a way where each individual step of the
ID generation process is its own function, with its own respective print method.
'''

# IMPORTS
from random_address import *
from typing import Dict
import random
import pkg_resources
import argparse

# EXCEPTION CLASS FOR INVALID ARGUMENT
class InvalidArgument(Exception):
    pass

# CONSTANTS (will eventually replace with a real config file)
CAPITALIZE_FIRST = True         # in the get_random_line() function, determines whether


# FUNCTIONS

# READ RANDOM LINE
# read a random line from a given file
def get_random_line(file_path, capitalize=CAPITALIZE_FIRST):
    resource_path = pkg_resources.resource_filename(__name__, file_path)
    try:
        with open(resource_path, 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)

            if capitalize:
                random_line = random_line[0].upper() + random_line[1:len(random_line) - 1]
            else:
                random_line = random_line[:len(random_line) - 1]

            return random_line
    except FileNotFoundError as fnf:
        print("ERROR: There was an error reading file " + file_path)
        print(fnf)


# NAME GENERATION
def generate_name(first_source, last_source) -> Dict[str, str]:
    fname = get_random_line(first_source)
    lname = get_random_line(last_source)

    name = {"first": fname, "last": lname}

    return name


# ADDRESS GENERATION
def generate_address(state, zip) -> Dict[str, str]:
    if state != "any":
        state = state.upper()
        addy = real_random_address_by_state(state)
        if addy == {}:
            raise InvalidArgument(f"Invalid value for State: {state}")

    elif zip != "any":
        addy = real_random_address_by_postal_code(zip)
        if addy == {}:
            raise InvalidArgument(f"Invalid value for Zip Code: {zip}")
    else:
        addy = real_random_address()


    if addy == {}:
        raise InvalidArgument("Bad Address")

    return addy


# USERNAME GENERATION
def generate_username(uname_source) -> str:
    uname = get_random_line(uname_source) + get_random_line(uname_source)

    # append a random number to the end of the name
    uname += str(random.randint(100, 999))

    return uname



# PASSPHRASE GENERATION
def generate_passphrase(pass_source, length) -> str:
    passphrase = ""
    for i in range(length):
        passphrase += (get_random_line(pass_source) + "-")
    passphrase = passphrase[:len(passphrase) - 1]

    return passphrase


# PRINT FUNCTIONS
# print name
def print_name(name):
    if name == {}:
        print("Error: invalid name")
        return False

    print("NAME:")
    pname = name.get("first") + " " + name.get("last")
    print(pname)
    print()

# print address
def print_address(addy):
    if addy == {}:
        print("Error: invalid name")
        return False

    print("ADDRESS:")
    print(addy.get("address1"))
    if addy.get("address2") != "":
        print(addy.get("address2"))
    print(addy.get("city") + ", " + addy.get("state") + " " + addy.get("postalCode"))
    print()

# print uname
def print_username(uname):
    print("USERNAME:")
    print(uname)
    print()

# print passphrase
def print_passphrase(pphrase):
    print("PASSPHRASE:")
    print(pphrase)
    print()


# EXECUTE CODE
def main():

    # handle command line arguments
    parser = argparse.ArgumentParser(
        prog='new_alias',
        description='Generate alias for online privacy and anonymity.'
    )

    # state argument
    parser.add_argument(
        '--state',
        '-s',
        dest='state',
        action='store',
        default='any',
        help='Set the desired state for address generation',
    )

    # zip code argument
    parser.add_argument(
        '--zip',
        '-z',
        dest='zip',
        action='store',
        default='any',
        help='Set the desired zip code for address generation',
    )

    # passphrase length argument
    parser.add_argument(
        '--pass-length',
        '-p',
        dest='pass_length',
        action='store',
        type=int,
        choices=range(3, 50),
        default=6,
        help='Set the desired zip code for address generation',
    )

    args = parser.parse_args()

    # VARIABLES FOR GENERATION FINE TUNING
    ADDY_STATE = args.state                 # state to generate address in, default 'any'
    AREA_CODE = args.zip                    # area code to generate address in, default 'any'

    PASSPHRASE_LENGTH = args.pass_length    # number of words to generate passphrase, default 6

    # argument error handling
    if (args.state != "any" and args.zip != any):
        print("WARNING: specifying state and zip code might cause unpredictable behavior.")
        print("Generating answer based on zip code...\n")
        args.state = any

    # FILE SOURCES FOR RANDOM GENERATION
    FIRST_NAME_SOURCE = "attributes/first-names.txt"
    LAST_NAME_SOURCE = "attributes/last-names.txt"
    USERNAME_SOURCE = "attributes/uname_words.txt"
    PASSPHRASE_SOURCE = "attributes/pass_words.txt"

    try:

        print("Generating alias...\n")
        # generate alias
        name = generate_name(first_source=FIRST_NAME_SOURCE, last_source=LAST_NAME_SOURCE)
        addy = generate_address(state=ADDY_STATE, zip=AREA_CODE)
        uname = generate_username(uname_source=USERNAME_SOURCE)
        pphrase = generate_passphrase(pass_source=PASSPHRASE_SOURCE, length=PASSPHRASE_LENGTH)

        # print alias to user
        print_name(name)
        print_address(addy)
        print_username(uname)
        print_passphrase(pphrase)

    except InvalidArgument as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
