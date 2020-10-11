def score(word):
    scr =0
    for i in word:
        scr += (ord(i) - 64)
    return scr

if __name__ == '__main__':
    names = sorted(open('names.txt').readline()[1:-1].split('","'))
    sum =0
    for ln, name in enumerate(names, 1):
        print(ln,names)
        sum += ln * score(name)
    print(sum)

