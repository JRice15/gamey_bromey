import math

known_append = open("known.tsv", "a")

                   # EDIT HERE

file_read = open("4digits.tsv", "r")

file_lines = file_read.readlines()
file_lines = [i.split() for i in file_lines if len(i.split()) > 0]

file_read.close()

# EDIT THIS
count = 0
for l in file_lines:
    inputs = l[0]
    value = int(l[1])
    A1, T1, A2, T2 = int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3])
    if value != 0:
        line = "{0}_{1}_{2}_{3}\t{4}\n".format(A1, T2, A2, T2, value)
        known_append.write(line)
        count += 1


known_append.close()