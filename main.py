import random
import math

def is_prime(n):
    """Check if a number is prime using optimized trial division."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    """Compute greatest common divisor using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def modular_inverse(e, phi):
    """Find modular inverse using extended Euclidean algorithm (incorporated version)."""
    original_phi = phi
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    
    while phi != 0:
        quotient = e // phi
        e, phi = phi, e % phi
        x1, x2 = x2, x1 - quotient * x2
        y1, y2 = y2, y1 - quotient * y2
    
    if e != 1:
        raise ValueError("Modular inverse doesn't exist")
    
    # Ensure the result is positive
    return x1 % original_phi

def generate_keypair(p, q):
    """Generate RSA public and private key pair."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal")
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    d = modular_inverse(e, phi)
    
    return ((e, n), (d, n))

def rsa_encrypt(pk, plaintext):
    """Encrypt plaintext using RSA public key."""
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def rsa_decrypt(pk, ciphertext):
    """Decrypt ciphertext using RSA private key."""
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

def get_prime_input(prompt):
    """Get and validate prime number input from user."""
    while True:
        try:
            num = int(input(prompt))
            if not is_prime(num):
                print("Please enter a valid prime number.")
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    print("RSA Encryption/Decryption Tool")
    print("-----------------------------")
    
    # Get validated prime numbers
    p = get_prime_input("Enter first prime number: ")
    q = get_prime_input("Enter second different prime number: ")
    while p == q:
        print("Numbers must be different.")
        q = get_prime_input("Enter second different prime number: ")
    
    print("\nGenerating keys...")
    public_key, private_key = generate_keypair(p, q)
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")
    
    message = input("\nEnter a message to encrypt: ")
    
    # Encryption
    encrypted_msg = rsa_encrypt(public_key, message)
    print("\nEncrypted Message:", ' '.join(map(str, encrypted_msg)))
    
    # Decryption
    decrypted_msg = rsa_decrypt(private_key, encrypted_msg)
    print("\nDecrypted Message:", decrypted_msg)

if __name__ == '__main__':
    main()