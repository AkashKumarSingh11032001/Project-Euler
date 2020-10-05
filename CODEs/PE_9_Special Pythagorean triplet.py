def Pythagorean(ls,n):
    for i in range(1,n):
        for j in range(i,n):
            z = n-i-j
            if z > 0:
                if z**2 == i**2 + j**2:
                    return i*j*z
                    break

if __name__ == '__main__':
    n = eval(input("Enter The n value: "))
    ls = [x for x in range(1,100)]
    print(Pythagorean(ls,n))