def Largest_Prime(num):
    factor = 1
    i = 2
    while i <= num/i:
        if num%i == 0:
            factor += 1
            num /= i
        else:
            i += 1

    if factor < num:
        factor = num


    return factor



if __name__ == '__main__':
    while True:
        num = eval(input("Enter Number :"))
        print(int(Largest_Prime(num)))
