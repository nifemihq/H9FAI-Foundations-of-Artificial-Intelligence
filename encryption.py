from cryptography.fernet import Fernet

# Generate a key for encryption/decryption (you can save this for reuse)
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'encryption_key.key'.")
    return key

# Load the key from a file
def load_key():
    try:
        with open("encryption_key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found. Generate a key first!")
        return None

# Encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message


if __name__ == "__main__":
    print("Encryption Agent")
    print("1. Generate Key")
    print("2. Encrypt Message")
    print("3. Decrypt Message")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        key = load_key()
        if key:
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Encrypted Message: {encrypted_message.decode()}")

    elif choice == "3":
        key = load_key()
        if key:
            encrypted_message = input("Enter the encrypted message: ").encode()
            try:
                decrypted_message = decrypt_message(encrypted_message, key)
                print(f"Decrypted Message: {decrypted_message}")
            except Exception as e:
                print(f"Decryption failed: {e}")

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
