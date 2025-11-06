# Count vowels and consonants in a string

string = input("Enter a string: ")

# Convert to lowercase for easy checking
string = string.lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in string:
    if ch.isalpha():  # check if character is a letter
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
