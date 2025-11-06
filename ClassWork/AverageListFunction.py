def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Numbers in list : ", numbers)
print("Average is : ", average(numbers))