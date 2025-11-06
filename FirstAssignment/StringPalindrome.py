text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")
