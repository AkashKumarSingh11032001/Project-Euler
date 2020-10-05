import sympy

def SumOfPrime(n):
    print(sum(list(sympy.primerange(0, n))))


if __name__ == '__main__':
    n = eval(input("Enter The last range digit :"))
    SumOfPrime(n)