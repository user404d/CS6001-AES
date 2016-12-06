"""
Helper Functions 
"""
import random
import string


def get_byte_list_from(data_string):
    """
    Args: 
        data_string: a string to convert to bytes
                     length should be a multiple of 4
    Return:
        A list of lists with bytes corresponding to the data_string
    """
    return [list(bytes(data_string[i:i+4], 'utf-8')) for i in range(0,len(data_string), 4)]

def generate_random_key(key_size):
    """
    Generates a random key from uppercase characters and digits.
    Args: 
        key_size: an integer; the desired list length
    Returns:
        A list of bytes corresponding to the randomly generated key.
    """
    rand_key = bytes(random.randint(0,255) for _ in range(key_size))
    return list(rand_key)

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
    byte_list = generate_random_key(block_size)
    return [byte_list[i*4:(i+1)*4] for i in range(block_size//4)]
