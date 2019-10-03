import random

rand_file = open("randoms.tsv", "w")

for _ in range(50):
    a1 = random.randint(1, 9)
    t1 = random.randint(1, 9)
    a2 = random.randint(1, 9)
    t2 = random.randint(1, 9)
    a3 = random.randint(1, 9)
    line = "{0}_{1}_{2}_{3}_{4}\n".format(a1, t1, a2, t2, a3)
    rand_file.write(line)

rand_file.close()