import math

known_file = open("known.tsv", "r")

known_lines = known_file.readlines()
known_lines = [i.split() for i in known_lines]

known_lines = [[i[0].split("_"), i[1]] for i in known_lines]

known_lines = [[int(j) for j in i[0]] + [int(i[1])] for i in known_lines]

# A1 T1 A2 T2 Value

operations = []
for i in known_lines:
    a1, t1, a2, t2, v = i
    tot = a1 + t1 + a2 + t2
    A = a1 + a2
    T = t1 + t2
    avg = tot / 4
    q1 = avg / v
    q2 = A / v
    q3 = T / v
    q4 = tot / v
    q5 = (a1 + t1) / v
    q6 = (a2 + t1) / v
    list1 = [tot, A, T, avg, q1, q2, q3, q4, q5, q6]
    operations.append(list1)


for i in range(len(operations[0])):
    for j in operations:
        count = 0
        for k in operations:
            if abs(j[i] - k[i]) < (10 ** -4):
                count += 1
        print("op", i, ":", j[i], count)
    




known_file.close()