from math import gcd
from functools import reduce


def lcm(a,b):
    return a*b//gcd(a,b)


if __name__ == '__main__':
    n = eval(input("Enter The last limit Of range : "))
    result = reduce(lcm, range(1,n))
    print(result)
