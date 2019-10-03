import math

# Works

def main():
    a1 = int(input("a1: "))
    t1 = int(input("t1: "))
    a2 = int(input("a2: "))
    t2 = int(input("t2: "))
    print("Equation2:", equation2(a1, t1, a2, t2))


def equation2(a1, t1, a2, t2):

    if t2 % 2 == 0:
        answer = even2(a1, t1, a2, t2)
    else:
        answer = odd2(a1, t1, a2, t2)
    return answer

def even2(a1, t1, a2, t2):
    A = a1 + a2
    T = t1 + t2


    original = (
        math.floor( (A + 1) / 2) * math.ceil( (A + 1) / 2)
    )

    if A % 2 == 0: # A Even
        secondary = math.ceil( (a1 * t1) / 2 )
    else: # A Odd
        secondary = math.floor( (a1 * t1) / 2 )
        
    if t2 > 0:
        alternating = [a1, a2] * ((t2 // 2) + 1) # length of t2 +1 for good measure

        third = sum(alternating[:t2])

    return original + secondary + third


# for odd t2
def odd2(a1, t1, a2, t2):
    A = a1 + a2
    T = t1 + t2


    original = (
        math.floor( (A + 1) / 2) * math.ceil( (A + 1) / 2)
    )

    secondary = math.ceil( (a1 * t1) / 2 )

    if t2 > 0:
        alternating = [a1, a2] * ((t2 // 2) + 5) # length of t2 +5 for good measure

        third = sum(alternating[:t2 - 1])
        third += math.floor((a1 + a2) / 2)

    else:
        third = 0

    if (a1 % 2 == 1) and (a2 % 2 == 1) and (t1 % 2 == 1) and (t2 % 2 == 1):
        #fourth = 0
        fourth = -1
        
    else:
        fourth = 0

    return original + secondary + third + fourth


if __name__ == "__main__":
    main()
