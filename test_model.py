import model
import math


colors = ['\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[91m']
styles = ['\033[1m', '\033[4m']
end =  '\033[0m'

known_file = open("known.tsv", "r")
known_lines = known_file.readlines()
known_file.close()

known_lines = [i.split() for i in known_lines]
known_lines = [[i[0].split("_"), i[1]] for i in known_lines if len(i) > 0]
known_lines = [[int(j) for j in i[0]] + [int(i[1])] for i in known_lines]


output_lines = []
for i in known_lines:
    if i[3] != 0:
        a1, t1, a2, t2 = i[:4]
        T = t1 + t2
        A = a1 + a2
        
        s1 = a1 +t1
        s2 = a2 + t2

        if t2 % 2 == 0:
            code = int(model.even2(a1, t1, a2, t2))
        else:
            code = int(model.odd2(a1, t1, a2, t2))
        real = i[4]
        diff = code - real

        

        guess = []

            #   0   1   2   3   4     5     6     7    
        line = [a1, t1, a2, t2, code, real, diff, guess]
        output_lines.append(line)


def selection_sort(unsorted, top_n, ind):
    sortedd = []
    unsorted2 = [abs(i[ind]) for i in unsorted]
    for _ in range(top_n):
        highest_ind = unsorted2.index(max(unsorted2))
        # if unsorted[highest_ind][3] % 2 != 0:
        sortedd.append(unsorted[highest_ind])
        unsorted2[highest_ind] = -1
    return sortedd


sorted_output = selection_sort(output_lines, len(output_lines), 6)


print("\033[1mATAT\t\tCode\tReal\tDiff\t[]\033[0m")

first = True
for i in sorted_output:
    a1, t1, a2, t2, code, real, diff, guess = i
    print_line = "{0}_{1}_{2}_{3}  \t{4}\t{5}\t{6}".format(\
            a1, t1, a2, t2, code, real, diff)
    for j in guess:
        print_line += "\t{0}".format(j)
    if first:
        if diff == 0:
            first = False
            print("\n")
    #for colorizing
    if diff > 0:
        col = colors[1]
        print(col + print_line + end)
    elif diff < 0:
        col = colors[0]
        print(col + print_line + end)
    else:
        print(print_line)
        pass
    

