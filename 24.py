from itertools import permutations

def lex_permut(n,k):
    l =[]
    perm = sorted(''.join(i) for i in permutations(n))
    for x in perm:
        l.append(int(x))
    return l[k]



if __name__ == '__main__':
    k = eval(input("Enter nth value : "))
    n = "0123456789"
    print(lex_permut(n,k))