def powerDigit(n):
    sum =0
    x = 2**n
    for i in str(x):
        sum = sum + int(i)
    return sum



if __name__ == '__main__':
    n = eval(input("Enter The power :"))
    print(powerDigit(n))