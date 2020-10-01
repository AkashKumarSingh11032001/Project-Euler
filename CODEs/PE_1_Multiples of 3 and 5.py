if __name__ == '__main__':
    n = eval(input("Enter range limit: "))
    print(sum([i for i in range(3, n) if i%3 == 0 or i%5 == 0]))
