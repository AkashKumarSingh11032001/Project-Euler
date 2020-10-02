def PalindromeProductNumber(n):
    upper = 0
    lower = 0
    # Calculating upper bound
    for i in range(1, n + 1):
        upper = upper * 10
        upper = upper + 9

    # Calculating lower bound
    lower = 1 + lower // 10

    max_mul = 0
    for i in range(upper, lower - 1, -1):
        for j in range(i, lower - 1, -1):
            # calculating products in a range
            mul = i * j
            if (mul < max_mul):
                break
            number = mul
            reverse_num = 0
            # checking whether a number is palindrome
            while (number != 0):
                reverse_num = reverse_num * 10 + number % 10
                number = number // 10
            # updating product
            if (mul == reverse_num and mul > max_mul):
                max_mul = mul

    return max_mul

if __name__ == '__main__':
    n = eval(input("Enter Parameter: "))
    print(PalindromeProductNumber(n))