import math

known_read = open("known.tsv", "r")

known_lines = known_read.readlines()
known_lines = [i.split() for i in known_lines]

known_read.close()

known_append = open("known.tsv", "a")

known_append.write("\n\n")

                   # EDIT HERE
known_append.write("(A)(T)(A) by formula\n")


# EDIT THIS
count = 0
for A1 in range(10):
    for T in range(10):
        for A2 in range(10):
            tot_A = A1 + A2
            initials = (1/8) * ( (2 * (tot_A ** 2)) + (4 * tot_A) + ((-1) ** (tot_A + 1)) + 1)
            if tot_A % 2 == 0:
                val_2 = math.ceil(A1 * T / 2)
            else:
                val_2 = math.floor(A1 * T / 2)
            total = int(initials + val_2)
            if total != 0:
                line = "{0}{1}{2}\t{3}_{4}_{5}\t{6}\n".format("A"*A1, "T"*A2, "A"*A2, A1, T, A2, total)
                known_append.write(line)
                count += 1



known_append.write(str(count))

known_append.close()