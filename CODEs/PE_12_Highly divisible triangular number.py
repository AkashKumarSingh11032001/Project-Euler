import sympy

def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum =sum+i
    return sum

def divisor(n):
    li = []
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
        li.append(sum)
    return li

def print_factors(x):
   t = []
   for i in range(1, x + 1):
       if x % i == 0:
           t.append(i)
   return t

def Prime(lis):
    k =[]
    r = []
    for z in lis:
        x = print_factors(z)
        r.append(len(x))
    print(r)
    for h in r:
        if h > 5:
            print(h)
            break












n = 7
print(sum(n))
lis = divisor(n)
print(lis)
print(Prime(lis))