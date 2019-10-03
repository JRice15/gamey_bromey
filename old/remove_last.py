open_file = open("known.tsv", "r")

lines = open_file.readlines()

newline_end = True
while newline_end:
    try:
        int(lines[-1])
        newline_end = False
    except ValueError:
        lines = lines[:-1]


count = int(lines[-1])

print("\nremoving {0} lines".format(count))

lines_new = lines[:-count - 2]

open_file.close()

open_write = open("known.tsv", "w")

for i in lines_new:
    open_write.write(i)

print("complete\n")