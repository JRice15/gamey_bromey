import math

             ### EDIT HERE
table = open("(A)(T).tsv", "r")
table_lines = table.readlines()
table_lines = [i.split() for i in table_lines]
table.close()


known_append = open("known.tsv", "a")

known_append.write("\n\n\n")

                    ### EDIT HERE
known_append.write("(A)(T)")

known_append.write("\n")

count = 0
for line in table_lines[:-1]:
    for ind in range(1, len(line)):
        y_axis = int(line[0])
        x_axis = int(table_lines[-1][ind - 1])
        value = line[ind]

                    ### EDIT HERE                                                                ---]
        line_app = "{0}{1}\t{2}_{3}\t{4}\n".format("A"*y_axis, "T"*x_axis, y_axis, x_axis, value)

        if int(value) != 0:
            known_append.write(line_app)
            count += 1

known_append.write(str(count))

known_append.close()