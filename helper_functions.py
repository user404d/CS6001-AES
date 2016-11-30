"""
Helper Functions 
"""
import random
import string

def generate_random_key(key_size):
    """
    Generates a random key from uppercase characters and digits.
    Args: 
        key_size: an integer; the desired list length
    Returns:
        A list of bytes corresponding to the randomly generated key.
    """
    chars = string.ascii_uppercase + string.digits
    random_key_string = ''.join(random.choice(chars) for _ in range(key_size))
    return list(bytes(random_key_string, 'utf-8'))

def initialization_vector(block_size=16):
    """
    Generate an initialization vector for AES Cipher Block Chaining Mode
    See aes_test.py test_cbc_on_file function for example of use.
    block_size should be the same size as the key_size.

    Args:
        block_size: an integer

    Returns:
        4 by block_size/4 sized matrix of integers. 
    """
    chars = string.ascii_uppercase + string.digits
    random_key_string = ''.join(random.choice(chars) for _ in range(block_size))
    byte_list = list(bytes(random_key_string, 'utf-8'))
    return [byte_list[i*4:(i+1)*4] for i in range(block_size//4)]
