'''
trim_words.py

This file contains a function that, in the general case, parses a text file and eliminates all lines that are
less than the MIN and greater than the MAX constants, inclusive. The result is a text file that contains only
the lines whose length is in the range [MIN, MAX].

For this project, I used this file to eliminate the smallest and largest words from the "words_alpha.txt" file.
This creates usernames that are both interesting as well as within most character limits.
'''

INPUT_FILE = "attributes/words_alpha.txt"
UNAME_MIN = 6
UNAME_MAX = 8
PASS_MIN = 6
PASS_MAX = 6


def filter_text_file(input_file, output_file, min, max):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if min <= len(line.strip()) <= max]

    with open(output_file, 'w') as file:
        file.writelines(filtered_lines)

# create the username file
filter_text_file(INPUT_FILE, "uname_words.txt", UNAME_MIN, UNAME_MAX)

# create the password file
filter_text_file(INPUT_FILE, "pass_words.txt", PASS_MIN, PASS_MAX)
