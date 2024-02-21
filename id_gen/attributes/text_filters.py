'''
text_filters.py

Copyright (c) 2024 Aiden R. McCormack
This file is a part of id-gen, released under the MIT License

This file contains a function that, in the general case, parses a text file and eliminates all lines that are
less than the MIN and greater than the MAX constants, inclusive. The result is a text file that contains only
the lines whose length is in the range [MIN, MAX].

For this project, I used this file to eliminate the smallest and largest words from the "words_alpha.txt" file.
This creates usernames that are both interesting as well as within most character limits.

'''

# CONSTANTS FOR CONFIG (note while functions are general, the constants are for this specific use)
UNAME_INFILE = "./words_alpha.txt"       # file to process for username generation
UNAME_OUTFILE = "./uname_words.txt"                 # file to write processed uname output to
UNAME_MIN = 6                                       # minimum word length for username generation
UNAME_MAX = 8                                       # maximum word length for username generation

PASS_INFILE = "./1-1000.txt"        # file to process for passphrase generation
PASS_OUTFILE = "./pass_words.txt"                   # file to write processed pphrase output to
START_NUMBER = 100                                  # first word to consider from pass file
PASS_MIN = 4                                        # minimum word length for pphrase generation
PASS_MAX = 30                                       # maximum word length for pphrase generation

# generates new file with words lengths in range [min, max]
def trim_file_by_word_length(input_file, output_file, min=1, max=30):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if min <= len(line.strip()) <= max]

    with open(output_file, 'w') as file:
        file.writelines(filtered_lines)
        
# omit words before a given start index
def cut_file_by_line_number(input_file, output_file, line_no):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        
    filtered_lines = [line for index, line in enumerate(lines) if index >= line_no - 1]
        
    with open(output_file, 'w') as file:
        file.writelines(filtered_lines)


def main():
    # idiotproof check
    assert UNAME_MAX >= UNAME_MIN, "UNAME_MIN must be less than UNAME_MAX"
    assert PASS_MAX >= PASS_MIN, "PASS_MIN must be less than PASS_MAX"
    
    # create the username file
    trim_file_by_word_length(UNAME_INFILE, UNAME_OUTFILE, UNAME_MIN, UNAME_MAX)

    # create the password file
    cut_file_by_line_number(PASS_INFILE, PASS_OUTFILE, START_NUMBER)
    trim_file_by_word_length(PASS_OUTFILE, PASS_OUTFILE, PASS_MIN, PASS_MAX)
    
if __name__ == "__main__":
    main()
