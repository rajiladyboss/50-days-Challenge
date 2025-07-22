import re

def count_details(paragraph):
    # Count characters (excluding spaces)
    char_count = len(paragraph.replace(" ", ""))
    
    # Count words (split by spaces)
    word_count = len(paragraph.split())
    
    # Count sentences (using regex for . ! ? )
    sentence_count = len(re.findall(r'[.!?]', paragraph))
    
    return char_count, word_count, sentence_count

# Input from user
paragraph = input("Enter your paragraph:\n")

chars, words, sentences = count_details(paragraph)

print(f"\nCharacter Count (excluding spaces): {chars}")
print(f"Word Count: {words}")
print(f"Sentence Count: {sentences}")
