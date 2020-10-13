def fibronic():
    a = 1
    b = 1
    li = [a,b]
    for i in range(1,100):
        c = a+b
        li.append(c)
        a,b = b,c
    return li

def countDigit(lis,n):
    k = []
    for i in lis:
        if len(str(i)) == n:
            return lis.index(i,1)+1
            break

if __name__ == '__main__':
    n = eval(input("Enter the number of digit: "))
    print(countDigit(fibronic(),n))


