num = int(input("Enter a number: "))

order = len(str(num))

sum_of_powers = 0

temp = num

while temp > 0:
    digit = temp % 10  
    sum_of_powers += digit ** order
    temp //= 10  # remove last digit

# Check if Armstrong
if num == sum_of_powers:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
