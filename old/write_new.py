

known_append = open("known.tsv", "a")

in_value = []

known_append.write("\n")

while "exit" not in in_value:
    in_value = []
    print("\nenter ATAT values then result:")
    in_value.append(input())
    in_value.append(input())
    in_value.append(input())
    in_value.append(input())
    in_value.append(input("result: "))
    line = "{0}_{1}_{2}_{3}\t{4}\n".format(in_value[0], in_value[1], in_value[2], in_value[3], in_value[4])
    print("line:", line)
    print("write data? [y/n]: ", end="")
    proceed = input()
    if proceed == "y":
        known_append.write(line)
    if proceed == "exit":
        in_value = ["exit"]


known_append.close()