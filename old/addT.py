known_file = open("known.tsv", "r")

known_lines = known_file.readlines()
known_lines = [i.split() for i in known_lines]

known_lines = [[i[0].split("_"), i[1]] for i in known_lines if len(i) > 0]

known_lines = [[int(j) for j in i[0]] + [int(i[1])] for i in known_lines]

# A1 T1 A2 T2 Value
# 0  1  2  3  4


for i in known_lines:
    a1, t1, a2, t2, v = i
    if a2 == 0 and t2 == 0:
        last_t = t1
    elif a2 == 0 and t2 > 0:
        last_t = t1 + t2
    elif a2 > 0:
        last_t = t2
    
    
    





known_file.close()