# Vowel Counter Program

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Input from user
word = input("Enter a word: ")
vowel_count = count_vowels(word)

print(f"The number of vowels in '{word}' is: {vowel_count}")
