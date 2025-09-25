# CS 4770/5770 Assignment 1 Question 8: Classical Cipher Implementation [10 points]
# Implement the Caesar cipher in Python. The program should:
# • Take plaintext and key (shift) as input
# • Output ciphertext
# • Then decrypt back to plaintext

def caesar_cipher(text, shift, decrypt=False):
    """
    Encrypts or decrypts text using Caesar cipher.

    Args:
        text (str): The text to encrypt/decrypt
        shift (int): Number of positions to shift (0-25)
        decrypt (bool): If True, decrypts the text; if False, encrypts

    Returns:
        str: The encrypted or decrypted text
    """
    # TODO: Implement the Caesar cipher logic
    # 1. If decrypting, adjust the shift
    # 2. Process each character:
    #    - If it's a letter, shift it while preserving case
    #    - If it's not a letter, keep it unchanged
    # 3. Return the resulting string

    result = ""
    if decrypt == False:
        for i in range(len(text)):
            if text[i].isalpha() == False:
                result += text[i]
            if text[i].islower() == True:
                num = (ord(text[i]) - 97) + shift    # Shift by 97 so that a = 0, b = 1, etc...
                num = (num % 26) + 97
                result += chr(num)
            if text[i].isupper() == True:            # This checks that the letter is within the ASCII code for the alphabet
                num = (ord(text[i]) - 65) + shift    # Shift by 65 so that A = 0, B = 1, etc...
                num = (num % 26) + 65
                result += chr(num)
    else:
        for i in range(len(text)):
            if text[i].isalpha() == False:
                result += text[i]
            if text[i].islower() == True:
                num = (ord(text[i]) - 97) - shift    # Shift by 97 so that a = 0, b = 1, etc...
                num = (num % 26) + 97
                result += chr(num)
            if text[i].isupper() == True:            # This checks that the letter is within the ASCII code for the alphabet
                num = (ord(text[i]) - 65) - shift    # Shift by 65 so that A = 0, B = 1, etc...
                num = (num % 26) + 65
                result += chr(num)

    return result


def main():
    """
    Main function to demonstrate Caesar cipher functionality.
    Should take user input for text and shift, then show both
    encryption and decryption results.
    """
    try:
        # Get user input
        text = input("Enter text: ")
        shift = int(input("Enter shift amount (0-25): "))

        # Validate shift
        if not 0 <= shift <= 25:
            print("Shift must be between 0 and 25!")
            return

        # Perform encryption
        encrypted = caesar_cipher(text, shift)
        print(f"Encrypted: {encrypted}")

        # Perform decryption
        decrypted = caesar_cipher(encrypted, shift, decrypt=True)
        print(f"Decrypted: {decrypted}")

    except ValueError:
        print("Please enter a valid number for shift!")


if __name__ == "__main__":
    main()