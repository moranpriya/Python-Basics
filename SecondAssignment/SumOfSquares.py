# Sum of squares from 1 to n

n = int(input("Enter a number: "))

sum_of_squares = 0

for i in range(1, n+1):
    sum_of_squares += i * i

print("Sum of squares from 1 to", n, "is:", sum_of_squares)
