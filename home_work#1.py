#!/usr/bin/env python

import os.path #to check if the file exists
import sys # for using an argument (argv)

FILE_PATH = sys.argv[1] #from first argument we take a path to file
IVASYK = 'IVASYK.txt' # id 0
DMYTRYK = 'DMYTRYK.txt' # id 1
OSTAP = 'OSTAP.txt' # id 2
LESYA = 'LESYA.txt' # id 3


dict_out = {0: [], 1: [], 2: [], 3: []} #to divide into a dict with lists

def check_args():
    if len(sys.argv) != 2:
        print("please run the program in this way:\n")
        print("python home_work#1 txt_file.txt")

# in case when file not exist program exit
def existsCheck(path):
    try:
        os.path.exists(path)
    except False:
        print("Not exists: exit\n")
        exit(1)

# IVASYK check
#Remember that empty line (\n) also is message!!!
def check_0(line):
    if (len(line)%2 == 0):
        return True

#DMYTRYK check
def check_1(line):
    if not check_0(line) and line[0].isupper():
        return True

#OSTAP check
def check_2(line):
    if not check_3(line) and not check_0(line) and not check_1(line):
        return True

#LESYA check
def check_3(line):
    if line.endswith(' end'):
        return True

#here we will forward each line to the correct key in dictionary
def forwardMessages(path):
    with open(path) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]
    for index in content:
        if check_0(index):
            dict_out[0].append(index) # adding line to to dictionary
        if check_1(index):
            dict_out[1].append(index)
        if check_3(index):
            dict_out[3].append(index)
        if check_2(index):
            dict_out[2].append(index)
          
    
#creating an output files
def createFiles(dict_to_divide):
    file_I = open(IVASYK, "w")
    for line in dict_to_divide[0]:
        file_I.write(line + "\n")
    file_I.close()
    file_D = open(DMYTRYK, "w")
    for line in dict_to_divide[1]:
        file_D.write(line + "\n")
    file_D.close()
    file_O = open(OSTAP, "w")
    for line in dict_to_divide[2]:
        file_O.write(line + "\n")
    file_O.close()
    file_L = open(LESYA, "w")
    for line in dict_to_divide[3]:
        file_L.write(line + "\n")
    file_L.close()

def main():
    check_args()
    existsCheck(FILE_PATH)
    forwardMessages(FILE_PATH)
    createFiles(dict_out)

if __name__ == "__main__":
    main()
