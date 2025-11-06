def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

num = int(input("Enter a number : "))

print("Reverse of", num, "is :", reverse_number(num))