import math


"""
julians model for up to 4 digits
"""


def main():
    a1 = int(input("a1: "))
    t1 = int(input("t1: "))
    a2 = int(input("a2: "))
    t2 = int(input("t2: "))
    a3 = int(input("a3: "))
    print("5 equation:", equation1(a1, t1, a2, t2, a3))


def equation1(a1, t1, a2, t2, a3):
    if t2 % 2 == 0:
        answer = even1(a1, t1, a2, t2, a3)
    else:
        answer = odd1(a1, t1, a2, t2, a3)
    return answer


# original; works for even t2
def even1(a1, t1, a2, t2, a3):
    A = a1 + a2 + a3
    T = t1 + t2

    original = (
        math.floor( (A + 1) / 2) * math.ceil( (A + 1) / 2)
    )

    if A % 2 == 0: # A Even
        secondary = math.ceil( (a1 * t1) / 2 )
    else: # A Odd
        secondary = math.floor( (a1 * t1) / 2 )
        
    if t2 > 0:
        alternating = [a1, a2, a3] * ((t2 // 2) + 1) # length of t2 +1 for good measure

        third = sum(alternating[:t2])

    return original + secondary + third


# for odd t2
def odd1(a1, t1, a2, t2, a3):
    A = a1 + a2 + a3
    T = t1 + t2

    original = (
        math.floor( (A + 1) / 2) * math.ceil( (A + 1) / 2)
    )

    if (t2 % 2 == 0):
        secondary = math.ceil( (a1 * t1) / 2 )
    else:
        secondary = math.floor( (a1 * t1) / 2 )

    if t2 > 0:
        alternating = [a1, a2, a3] * ((t2 // 2) + 5) # length of t2 +5 for good measure

        third = sum(alternating[:t2 - 1])
        third += math.floor(A / 2)

    else:
        third = 0

    if (a1 % 2 == 1) and (a2 % 2 == 0) and (t1 % 2 == 1) and (t2 % 2 == 1): 
        fourth = 1
    else:
        fourth = 0

    return original + secondary + third + fourth



if __name__ == "__main__":
    main()