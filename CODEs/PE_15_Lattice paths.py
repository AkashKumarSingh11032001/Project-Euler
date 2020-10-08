import math

def lactices(n):
    num = math.factorial(n)
    return math.factorial(n+n)//num//num

print(lactices(9))


'''
Formula : 
(m+n)!/m!n!

'''