def encrypt(message, shiftby):
    encrypted_text = ""
    for character in message:
        if character.isalpha():
            shift_amount = shiftby % 26
            shifted_char = ord(character) + shift_amount
            if character.islower():
                if shifted_char > ord('z'):
                    shifted_char =shifterd_char- 26
                encrypted_text += chr(shifted_char)
            elif character.isupper():
                if shifted_char > ord('Z'):
                    shifted_char =shifted_char- 26
                encrypted_text =encrypted_text+ chr(shifted_char)
        else:
            encrypted_text =encrypted_text+ character
    return encrypted_text

def decrypt(message, shiftby):
    return encrypt(message, -shiftby)

def main():
    while True:
        choice = input("Enter E to encrypt a message or D to decrypt a message? (Enter 'Q' to quit): ")
        if choice == 'Q':
            print("Exiting the program.")
            break
        elif choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")
            continue
        
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if choice == 'E':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'D':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()