known = open("known_old.tsv", "r")

known_lines = known.readlines()
known_lines = [i.split() for i in known_lines]
known_lines = [i[1:] for i in known_lines]

print(known_lines[:20])

known.close()




open_write = open("known.tsv", "w")

for i in known_lines:
    if len(i) == 0:
        line = "\n"
    else:
        line = "{0}\t{1}\n".format(i[0], i[1])
    open_write.write(line)

print("complete\n")

open_write.close()