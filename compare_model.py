import model4
import model4_2
import math
import number_trouble

known_file = open("known.tsv", "r")
known_lines = known_file.readlines()
known_file.close()

known_lines = [i.split() for i in known_lines]
known_lines = [[i[0].split("_"), i[1]] for i in known_lines if len(i) > 0]
known_lines = [[int(j) for j in i[0]] + [int(i[1])] for i in known_lines]


print("input\t\t model1\t model2\t num trub\t actual")
for i in known_lines:
    a, b, c, d, e = i[0:5]
    if (e == 0) and (10 > d > 0) and (a < 10) and (b < 10) and (c < 10):
        formula1 = model4.equation1(a, b, c, d)
        formula2 = model4_2.equation2(a, b, c, d)
        num_input = str(a) + str(b) + str(c) + str(d)
        num_trouble = number_trouble.output(num_input)
        actual = i[5]
        if (formula1 != formula2) or (formula1 != num_trouble):
            print(i[0:4], "\t", formula1, "\t", formula2, "\t", num_trouble, "\t", actual)

