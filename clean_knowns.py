# add trailing _0 to get to 4 digitis, remove duplicates

known = open("known.tsv", "r")
known_lines = known.readlines()
known.close()


# add _0's
second_known_lines = []
for i in known_lines:
    line_vals = i.split()
    if len(line_vals) != 0:
        underscores = line_vals[0].count("_")
        if underscores == 1:
            line_vals[0] += "_0_0_0"
        elif underscores == 2:
            line_vals[0] += "_0_0"
        elif underscores == 3:
            line_vals[0] += "_0"
        else:
            pass
        new_line = "{0}\t{1}\n".format(line_vals[0], line_vals[1])
        second_known_lines.append(new_line)


# removes duplicates
count = 0
new_known_lines = []
removed = []
for i in range(len(second_known_lines)):
    if second_known_lines[i] not in second_known_lines[:i]:
        new_known_lines.append(second_known_lines[i])
    else:
        count += 1
        removed.append(second_known_lines[i])
        
print("\nremoved {0} lines:".format(count))
for i in removed:
    print(i)

open_write = open("known.tsv", "w")

for i in new_known_lines:
    open_write.write(i)

print("complete\n")

open_write.close()