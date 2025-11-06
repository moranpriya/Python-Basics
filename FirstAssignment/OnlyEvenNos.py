n = int(input("Enter the limit: "))

print("Even numbers from 1 to", n, ":")

for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")
