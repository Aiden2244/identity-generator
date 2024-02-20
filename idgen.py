from random_address import *
import random

# CONSTANTS (will eventually replace with a real config file)
PASSPHRASE_LENGTH = 6
ADDY_STATE = "any"
AREA_CODE = "any"

# NAME GENERATION
# read a random line from the file
def get_random_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)
            random_line = random_line[0].upper() + random_line[1:len(random_line) - 1]
            return random_line
    except FileNotFoundError as fnf:
        print("ERROR: There was an error reading file " + file_path)
        print(fnf)


# Get names from first name and last name
first = get_random_line("first-names.txt")
last = get_random_line("last-names.txt")
print("NAME:")
print(first + " " + last)
print()


# ADDRESS GENERATION

if ADDY_STATE != "any":
    ADDY_STATE = ADDY_STATE.upper()
    addy = real_random_address_by_state(ADDY_STATE)
elif AREA_CODE != "any":
    addy = real_random_address_by_postal_code(AREA_CODE)
else:
    addy = real_random_address()

if addy != {}:
    print("ADDRESS:")
    print(addy.get("address1"))
    if addy.get("address2") != "":
        print(addy.get("address2"))
    print(addy.get("city") + ", " + addy.get("state") + " " + addy.get("postalCode"))
    print()
else:
    print("ERROR: Invalid Zip code or State")
    print("Zip Code: \'" + AREA_CODE + "\'")
    print("State: \'" + ADDY_STATE + "\'")
    print("Skipping address generation\n")
    


# USERNAME GENERATION
# get two random words from the uname_words.txt file
uname = get_random_line("uname_words.txt") + get_random_line("uname_words.txt")

# append a random number to the end of the name
uname += str(random.randint(100, 999))
print("USERNAME:")
print(uname)
print()


# PASSPHRASE GENERATION
# generate a unique passphrase with the random words list
passphrase = ""
for i in range(PASSPHRASE_LENGTH):
    passphrase += (get_random_line("pass_words.txt") + "-")
passphrase = passphrase[:len(passphrase) - 1]
print("PASSPHRASE:")
print(passphrase)
print()