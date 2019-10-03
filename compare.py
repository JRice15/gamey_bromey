import model4
import model4_2


def main():
    a1 = int(input("a1: "))
    t1 = int(input("t1: "))
    a2 = int(input("a2: "))
    t2 = int(input("t2: "))
    print("Equation1:", model4.equation1(a1, t1, a2, t2))
    print("Equation2:", model4_2.equation2(a1, t1, a2, t2))




if __name__ == "__main__":
    main()