def series(num , a, b , ls):
    for i in range(num - 2):
        c = a + b
        if (c > num):
            break
        else:
            ls.append(c)
            a, b = b, c
    print(ls)
def sum(ls):
    sum = 0
    size = len(ls)
    for i in range(size):
        if ls[i] % 2 == 0:
            sum = sum + ls[i]
    print(sum)


if __name__ == '__main__':
    num = eval(input("Enter The Number Limit : "))
    a, b = 1, 2
    ls = [a, b]
    series(num , a, b , ls)
    sum(ls)