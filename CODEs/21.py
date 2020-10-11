def divisor(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum += i
    return sum

if __name__ == '__main__':
    n = eval(input("Enter : "))
    SUM = 0
    for a in range(1, n):
        b = divisor(a)
        if a != b and divisor(b) == a:
            SUM += a + b

    print(SUM // 2)
