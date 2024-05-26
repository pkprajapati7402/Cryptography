from cryptography.fernet import Fernet

# Function to generate a key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from the file
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    choice = input("Choose (E)ncrypt or (D)ecrypt: ").strip().upper()
    if choice == 'E':
        message = input("Enter the message to encrypt: ").strip()
        encrypted_message = encrypt_message(message)
        print(f"Encrypted message: {encrypted_message.decode()}")
    elif choice == 'D':
        encrypted_message = input("Enter the message to decrypt: ").strip().encode()
        try:
            decrypted_message = decrypt_message(encrypted_message)
            print(f"Decrypted message: {decrypted_message}")
        except Exception as e:
            print("An error occurred during decryption. Please check the input.")
    else:
        print("Invalid choice! Please choose either 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    # Check if the key file exists, if not, generate it
    try:
        load_key()
    except FileNotFoundError:
        write_key()
    
    main()
