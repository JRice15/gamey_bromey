class ATs:

    def __init__(self, at_list):
        for i in range(len(at_list)):
            if i % 2 == 0:
                letter = "a"
            else:
                letter = "t"
            number = str(i // 2 + 1)
            name = letter + number
            value = str(at_list[i])
            exec("self." + name + " = " + value)


