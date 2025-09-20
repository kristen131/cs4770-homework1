# CS 4770 - Assignment 1- Question 9 Fiestel Block Cipher Simulation
# Implement a 2-round Fiesstel network on an 8-bit block.
# Round function: f(R, K) = R XOR K
# Keys: K1 = 1010 (binary), K2 = 0101 (binary)

def round_function(R, K):
    """Compute the round function: f(R, K) = R XOR K."""
    # TODO: Implement the round function
    # Input: R (4-bit right half), K (4-bit key)
    # Output: Result of R XOR K (4-bit)
    result = ""
    print("This is key: ", K)
    print("This is R: ", R)
    for i in range(4):
        if (R[i] == "1" and K[i] == "0") or (R[i] == "0" and K[i] == "1"):
            result += "1"
        else:
            result += "0"
    print("I am result: ", result)
    return result
            
    

def encrypt_block(plaintext, K1, K2):
    """Encrypt an 8-bit plaintext using a 2-round Feistel network."""
    # TODO: Implement the encryption process
    # 1. Split plaintext into 4-bit halves (L0, R0)
    # 2. Perform Round 1: f1 = round_function(R0, K1), R1 = L0 XOR f1, L1 = R0
    # 3. Perform Round 2: f2 = round_function(R1, K2), R2 = L1 XOR f2, L2 = R1
    # 4. Combine L2 and R2 into 8-bit ciphertext
    # Return: ciphertext (8-bit), L2 (4-bit), R2 (4-bit) for printing steps
    binary = f"{plaintext:08b}"
    L0 = binary[:4]
    R0 = binary[4:]
    key1 = f"{K1:04b}"
    key2 = f"{K2:04b}"
    print("Here is the binary in encrypt block: ", binary)
    print("Here is the binary for L0 in encrypt block: ", L0)
    print("Here is the binary for L0 in encrypt block: ", R0)

    # Round 1
    L1 = R0
    R1 = round_function(L0, round_function(R0, key1))

    # Round 2
    L2 = R1
    R2 = round_function(L1, round_function(R1, key2))

    ciphertext = int(L2 + R2, 2)
    left = int(L2, 2)
    right = int(R2, 2)
    print("This is answer in encrypt block: ", ciphertext)
    return ciphertext, left, right
    

def decrypt_block(ciphertext, K1, K2):
    """Decrypt an 8-bit ciphertext using a 2-round Feistel network."""
    # TODO: Implement the decryption process
    # 1. Split ciphertext into 4-bit halves (L', R')
    # 2. Reverse Round 2: f'2 = round_function(L', K2), L1 = R' XOR f'2, R1 = L'
    # 3. Reverse Round 1: f'1 = round_function(L1, K1), L0 = R1 XOR f'1, R0 = L1
    # 4. Combine L0 and R0 into 8-bit decrypted text
    # Return: decrypted text (8-bit)
    pass

def main():
    # Get input: 8-bit binary string
    while True:
        plaintext_bin = input("Enter an 8-bit binary string (e.g., 10101010): ").strip()
        if len(plaintext_bin) == 8 and all(c in '01' for c in plaintext_bin):
            break
        print("Invalid input. Please enter exactly 8 bits (0s and 1s).")

    plaintext = int(plaintext_bin, 2)
    print(f"\nPlaintext (binary): {plaintext_bin}")
    print(f"Plaintext (decimal): {plaintext}")

    # Keys (4-bit each)
    K1 = 0b1010
    K2 = 0b0101
    print(f"\nKeys:\nK1 = {K1:04b} (decimal: {K1})\nK2 = {K2:04b} (decimal: {K2})")

    # Encrypt
    print("\n=== Encryption Process ===")
    result = encrypt_block(plaintext, K1, K2)
    if result is None:
        print("Encryption not implemented.")
        return
    ciphertext, L2, R2 = result
    ciphertext_bin = f"{L2:04b}{R2:04b}"
    print(f"\nEncrypted Text (binary): {ciphertext_bin}")
    print(f"Encrypted Text (decimal): {ciphertext}")

    # Decrypt
    print("\n=== Decryption Process ===")
    decrypted = decrypt_block(ciphertext, K1, K2)
    if decrypted is None:
        print("Decryption not implemented.")
        return
    decrypted_bin = f"{decrypted:08b}"
    print(f"\nDecrypted Text (binary): {decrypted_bin}")
    print(f"Decrypted Text (decimal): {decrypted}")

    # Verify
    if decrypted == plaintext:
        print("\nDecryption successful: Matches original plaintext.")
    else:
        print("\nDecryption failed: Does not match original plaintext.")

if __name__ == "__main__":
    main()