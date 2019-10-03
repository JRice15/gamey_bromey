import random as rd
import sys

def read_file():
    file = sys.argv[1]
    with open(file, 'r') as f:
        lines = f.readlines().strip()
    with open("output_{}.tsv".format(rd.randint(0, 1000)), "w") as f:
        for ln in lines:
            string = convert_nums(ln)
            value = mystery_program(string)
            f.write(ln + "\t" + str(value))




def convert_nums(num_str):
    nums = num_str.split("_")
    letter = 'a'
    full_string = ''
    for i in nums:
        for _ in range(int(i)):
            full_string += letter
        if letter == 'a':
            letter = 't'
        else:
            letter = 'a'
    return full_string


def mystery_program(string):
    pass


if __name__ == "__main__":
    read_file()