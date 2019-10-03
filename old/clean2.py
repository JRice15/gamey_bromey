# shift for zeroes in data, remove blank lines

known_file = open("known.tsv", "r")
known_lines = known_file.readlines()
known_file.close()

known_lines = [i.split() for i in known_lines]
known_lines = [[i[0].split("_"), i[1]] for i in known_lines if len(i) > 0]
known_lines = [[int(j) for j in i[0]] + [int(i[1])] for i in known_lines]

# A1 T1 A2 T2 Value
# 0  1  2  3  4

new_known = []
for i in known_lines:
    a1, t1, a2, t2, v = i
    if a2 == 0 and t2 > 0:
        t1 += t2
        t2 = 0
    if t1 == 0:
        a1 += a2
        t1 += t2
        a2 = 0
        t2 = 0
    new_line = "{0}_{1}_{2}_{3}\t{4}\n".format(a1, t1, a2, t2, v)
    new_known.append(new_line)
    

open_write = open("known2.tsv", "w")

for i in new_known:
    open_write.write(i)

print("complete\n")    
    
open_write.close()


