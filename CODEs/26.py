def Cycle(k):
    num = 1
    large = 1
    for n in range(3, k, 2):
        if n % 5 == 0:
            continue

        a = 1
        while (10 ** a) % n != 1:
            a += 1

        if a > large:
            num, large = n, a

    return num


if __name__ == '__main__':
    n = eval(input("enter nth range value : "))
    print(Cycle(n))


