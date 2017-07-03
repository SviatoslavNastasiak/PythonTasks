#!/usr/bin/env python

''' module to forward messages from input file to addressants in separetade packets. Remember that one messages could be addressed to many addressants'''

import os
import sys

# global constants

FILE_PATH = sys.argv[1]
IVASYK = 'IVASYK'
DMYTRYK = 'DMYTRYK'
OSTAP = 'OSTAP'
LESYA = 'LESYA'
EXTENSION = '.txt'
LESYA_SIGNAL = ' end'

receivers = (IVASYK, DMYTRYK, OSTAP, LESYA)

DICT_OUT = {contact: [] for contact in receivers}  # to divide into a dict with lists


def check_args():

    ''' this function needs to check numbers of arguments from command line'''

    if len(sys.argv) != 2:
        print("please run the program in this way:\n")
        print("python home_work#1 txt_file.txt")
        exit(1)


def exists_check(path):

    '''here we check if file exists'''

    try:
        os.path.exists(path)
    except FileNotFoundError:
        print("Not exists: exit\n")
        exit(1)

# Remember that empty line (\n) also is message!!!
def check_ivasyk(line):

    '''here we check @line for IVASYK and return a boolean'''

    return (len(line) % 2 == 0)


def check_dmytryk(line):

    '''here we check @line for DMYTRYK and return a boolean'''

    return (not check_ivasyk(line) and line[0].isupper())


def check_lesya(line):

    '''here we check @line for LESYA and return a boolean'''

    return (line.endswith(LESYA_SIGNAL))


def forward_messages(path):

    '''here we will forward each line to the correct key in       dictionary'''

    with open(path) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    for lines in content:
        if check_lesya(lines):
            DICT_OUT[LESYA].append(lines)  # adding line to to dictionary
        elif check_ivasyk(lines):
            DICT_OUT[IVASYK].append(lines)
        elif check_dmytryk(lines):
            DICT_OUT[DMYTRYK].append(lines)
        else:
            DICT_OUT[OSTAP].append(lines)


def create_files(dict_to_divide):

    ''' here we create an output files which will contain an    messagess for each receiver'''

    for contact in receivers:
        with open(contact + EXTENSION, 'w') as out_f:
            for line in dict_to_divide[contact]:
                out_f.write(line + '\n')


def main():
    check_args()
    exists_check(FILE_PATH)
    forward_messages(FILE_PATH)
    create_files(DICT_OUT)

if __name__ == "__main__":
    main()

