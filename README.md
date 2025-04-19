# NS_RSA_Algorithm
RSA Algorithm implementation

## Project Overview
This repository contains a Python implementation of the RSA (Rivest-Shamir-Adleman) encryption and decryption algorithm. The project demonstrates the core principles of RSA, including key generation, encryption, and decryption, along with explanations of the underlying mathematical concepts.

## Repository Contents
- **`CS22B1039_Report.docx`**: The detailed project report explaining the RSA algorithm, implementation, sample output and security considerations.
- **`main.py`**: The Python script containing the RSA implementation.
- **`output.png`**: A sample output image showcasing the program's execution.
- **`RSA_algorithm.png`**: An image illustrating the RSA algorithm.

## Key Features
1. **Prime Number Check**: Uses an optimized trial division method to verify prime numbers.
2. **Key Generation**: Generates public and private key pairs using large prime numbers.
3. **Encryption and Decryption**: Encrypts plaintext messages and decrypts ciphertext using RSA.
4. **User Interface**: Provides a command-line interface for inputting primes and messages.

## How to Run the Program
1. Ensure you have Python installed on your system.
2. Clone this repository or download the `main.py` file.
3. Open a terminal and navigate to the directory containing `main.py`.
4. Run the program using the command:
   ```bash
   python main.py
   ```
5. Follow the on-screen instructions to input prime numbers and a message for encryption/decryption.

## Sample Output
The program will display:
- The generated public and private keys.
- The encrypted message (as a list of numbers).
- The decrypted original message.

Example:
```
Public Key (e, n): (65537, 3233)
Private Key (d, n): (2753, 3233)
Encrypted Message: 3106 1484 2551
Decrypted Message: Hello
```
