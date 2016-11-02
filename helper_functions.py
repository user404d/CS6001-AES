"""
Helper Functions 
"""
import random
import string

def get_byte_list_from(data_string):
    """
    4 bit lists, not bytes?

    Args: 
        data_string: a string to convert to bytes
    Return:
        A list of lists with bytes corresponding to the data_string
    """
    return [list(bytes(data_string[i*4:(i+1)*4].encode('utf-8'))) for i in range(len(data_string)//4)]

def generate_random_key_of_size(key_size):
    """
    Generates a random key from uppercase characters and digits.
    Args: 
        key_size: an integer; the desired key size
    Returns:
        A list of bytes corresponding to the randomly generated key.
    """
    chars = string.ascii_uppercase + string.digits
    random_key_string = ''.join(random.choice(chars) for _ in range(key_size))
    return list(bytes(random_key_string, 'utf-8'))
