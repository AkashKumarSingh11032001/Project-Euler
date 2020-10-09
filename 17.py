import inflect
p = inflect.engine()
#print(p.number_to_words(100))

def counting(li):

    l =[]
    for i in li:
        l.append(len(i)-i.count(" ")-i.count("-"))
    return l

def list_sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum

if __name__ == '__main__':
    n = eval(input("Enter range limit :"))
    li = []
    for i in range(1,n+1):
        li.append(p.number_to_words(i))
    print(li)

    x = counting(li)
    print(x)
    y = list_sum(x)
    print(y)
