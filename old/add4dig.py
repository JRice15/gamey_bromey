import model

known_append = open("known.tsv", "a")

# knowns len before running: to line 1115

for a1 in range(1, 11):
    for t1 in range(1, 11):
        for a2 in range(1, 11):
            for t2 in range(1, 11): 
                value = model.equation1(a1, t1, a2, t2)
                line = "{0}_{1}_{2}_{3}\t{4}\n".format(a1, t1, a2, t2, value)
                known_append.write(line)


known_append.close()