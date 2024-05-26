# 🔒 Encryption and Decryption Program

This is a Python program that uses the `cryptography` library's `Fernet` method for encryption and decryption. It provides a simple command-line interface to choose between encrypting and decrypting a message.

## 🚀 Features

- Encrypt any message using the Fernet encryption method.
- Decrypt any previously encrypted message using the same method.
- Automatically generates and uses a secret key for encryption and decryption.

## 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/encryption-decryption.git
   cd encryption-decryption
   ```

2. Install the required dependencies:

   ```bash
   pip install cryptography
   ```

## 🛠️ Usage

1. Run the program:

   ```bash
   python main.py
   ```

2. Choose between encryption (`E`) and decryption (`D`):

   - For encryption, enter the message you want to encrypt.
   - For decryption, enter the encrypted message.

## 🔑 Key Management

- The program generates a `secret.key` file if it doesn't exist.
- This key is used for both encryption and decryption.
- **Keep the `secret.key` file safe**. Losing this file will make it impossible to decrypt any messages encrypted with it.

## 📄 Example

```plaintext
Choose (E)ncrypt or (D)ecrypt: E
Enter the message to encrypt: Hello, world!
Encrypted message: gAAAAABeJc2V-MvhF7L3qfjzIHHGJ9tF5MEP3Gj2Pi8Y5kbU6iE4z6MSv1JazbTtXRXFwG1Y1NRpkRznlx0Kigc=
```

```plaintext
Choose (E)ncrypt or (D)ecrypt: D
Enter the message to decrypt: gAAAAABeJc2V-MvhF7L3qfjzIHHGJ9tF5MEP3Gj2Pi8Y5kbU6iE4z6MSv1JazbTtXRXFwG1Y1NRpkRznlx0Kigc=
Decrypted message: Hello, world!
```

## 📂 File Structure

```plaintext
encryption-decryption/
│
├── main.py         # The main script to run the program
├── secret.key      # The secret key file (auto-generated)
└── README.md       # This README file
```

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---

Made with ❤️ by [Prince](https://github.com/pkprajapati7402)
```
