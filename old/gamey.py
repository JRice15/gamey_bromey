T = 1

while T not in ("e", "exit"):
    print("enter T: ", end="")
    T = int(input())


    sum_T = 0
    for i in range(T+1):
        sum_T += -2 * ( (-1)**i - 1)

    print(sum_T, "\n")