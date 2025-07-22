# Simple Cipher: Shift each letter by +1

def simple_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                shifted = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            result += shifted
        else:
            result += char  # Non-alphabet stays the same
    return result


if __name__ == "__main__":
    user_input = input("Enter text to cipher: ")
    cipher_text = simple_cipher(user_input)
    print(f"Ciphered Text: {cipher_text}")
