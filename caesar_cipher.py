# ================================
# Caesar Cipher - Encryption Tool
# DecodeLabs - Project 2
# Cybersecurity Analyst Track
# ================================

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result


def brute_force(text):
    print("\n🔓 BRUTE FORCE ATTACK - All possible decryptions:")
    print("=" * 50)
    for shift in range(1, 26):
        print(f"Shift {shift:2d}: {decrypt(text, shift)}")
    print("=" * 50)


# Main Program
while True:
    print("\n")
    print("=" * 40)
    print("   🔴 DECODELABS CAESAR CIPHER TOOL")
    print("=" * 40)
    print("  1. Encrypt a message")
    print("  2. Decrypt a message")
    print("  3. Brute Force Attack")
    print("  4. Quit")
    print("=" * 40)

    choice = input("Choose option (1-4): ")

    if choice == "1":
        message = input("\nEnter message to encrypt: ")
        shift = int(input("Enter shift key (1-25): "))
        encrypted = encrypt(message, shift)
        print("\n==============================")
        print(f"Original:  {message}")
        print(f"Shift Key: {shift}")
        print(f"Encrypted: {encrypted}")
        print("==============================")

    elif choice == "2":
        message = input("\nEnter message to decrypt: ")
        shift = int(input("Enter shift key (1-25): "))
        decrypted = decrypt(message, shift)
        print("\n==============================")
        print(f"Encrypted: {message}")
        print(f"Shift Key: {shift}")
        print(f"Decrypted: {decrypted}")
        print("==============================")

    elif choice == "3":
        message = input("\nEnter encrypted message to brute force: ")
        brute_force(message)

    elif choice == "4":
        print("\n🔐 Stay secure! Goodbye!")
        break

    else:
        print("❌ Invalid option! Choose 1-4")