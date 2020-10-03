def SumOfSquare(a):
    res = 0
    for i in range(1,a+1):
        res = res + i**27
    return res


def SquareOfSum(b):
    res = 0
    for i in range(1,b+1):
        res = res + i
    return res**2



if __name__ == '__main__':
    n = eval(input("Enter the last range limit:"))
    print(SquareOfSum(n) - SumOfSquare(n))