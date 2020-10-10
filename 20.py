import math

if __name__ == '__main__':
    n = eval(input("Enter number: "))
    sum = 0
    fact = str(math.factorial(n))
    #print(fact)
    for i in fact:
        sum += int(i)
    print(sum)