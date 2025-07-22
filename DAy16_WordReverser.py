# Word Reverser: Reverse individual words in a sentence

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    result = reverse_words(user_input)
    print("\nReversed Words Sentence:")
    print(result)
