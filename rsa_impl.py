import math
import itertools
import random

def gcd(a, b):
    """
    Find the greatest common divisor using the euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def find_multiplicative_inverse(n, phi):
    """
    Find the multiplicative inverse of two numbers using the extended euclidean algorithm.
    """
    # mutable phi copy of original phi
    _phi = phi

    # mutable n copy of original n
    _n = n
    x0, x1, y0, y1 = 1, 0, 0, 1

    while _n != 0:
        q, _phi, _n = _phi // _n, _n, _phi % _n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    if _phi == 1:
        return y0 + phi
    else:
        raise Exception('Modular inverse does not exist')

def is_prime(n):
    """
    Check for primality of an integer.
    """
    if n < 2: 
        return False
    
    for number in itertools.islice(itertools.count(2), int(math.sqrt(n) - 1)):
        if not n % number:
            return False

    return True

def find_e_that_is_coprime_with(phi):
    """
    Find an integer that is coprime with phi
    """
    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)

    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    return e

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('One or both of the numbers are not prime.')
    elif p == q:
        raise ValueError('p should not be equal to q.')

    n = p * q
    phi = (p-1) * (q-1)
    e = find_e_that_is_coprime_with(phi)

    # Generate a private key using the extended euclidian algorithm 
    d = find_multiplicative_inverse(e, phi)
    
    public_key = (e, n)
    private_key = (d, n)
    return (public_key, private_key)

def encrypt(private_key_pair, plaintext):
    """
    Encrypt the plaintext.
    """
    key, n = private_key_pair

    # Encrypt each char using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]

    return cipher

def decrypt(public_key_pair, ciphertext):
    """ 
    Decrypt the ciphertext.
    """
    key, n = public_key_pair

    # Decrypt each char using a^b mod m
    plain = [chr(pow(char, key, n)) for char in ciphertext]

    return ''.join(plain)

if __name__ == '__main__':
    p = 17
    q = 19
    
    public_key, private_key = generate_keypair(p, q)
    message = "Secret message"
    encrypted_message = encrypt(public_key, message)
    print("Encrypted message is different: ", (message == encrypted_message) == False)
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Same message: ", message == decrypted_message)


