import os, struct, filecmp
import aes_impl as aes, helper_functions as helper

# Hard coded file path names, will be changed to command line args
test_file_path = 'test_img.jpg'
test_encrypt_path = 'test_encrypt.jpg'
test_decrypt_path = 'test_decrypt.jpg'

def pkcs7(size):
    """
    PKCS7 with hard coded 16 byte block length
    """
    amount_of_padding = 16 - (size % 16)
    return bytes(chr(amount_of_padding) * amount_of_padding, 'utf-8')

def read_chunks(file_handle, chunk_size, padding=pkcs7):
    """
    Generator to process files. Padding added by default.

    Args:
        file_handle: file handle to file to be processed (needs 'b' flag)
        chunk_size: the size of the chunk to pull from the file
        padding: function to add padding
    Returns:
        generator which will yield new chunks for processing
        until the entirety of the file has been read
    """
    while True:
        data = file_handle.read(chunk_size)
        if not padding and not data:
            yield None, True
            break
        elif len(data) != chunk_size:
            pad = padding(len(data))
            yield data + pad, False
            if len(pad) == 0:
                return pack(0), False
            break
        yield data, False

def encrypt_file(key_schedule, in_file, out_file=None, chunk_size=16, mode=aes.Mode.ecb, iv=None):
    """
    Encrypt a file using specified aes mode.
    
    Args:
        key_schedule: list(list(integer)), the key schedule for aes
        in_file: string, file path of file to be encrypted
        out_file: string [default: None], file path where the encrypted file should be stored
        chunk_size: integer [default: 16], the size of the blocks to be processed
        mode: string [default: "ECB"], aes.Mode.ecb or aes.Mode.cbc
        iv: list(integer) [default: None], initialization vector needed for aes some modes

    Returns:
        out_file: string [default: file_path + ".enc"], the filepath of the encrypted file
    """
    # If no output file name passed, creates one based on input file name
    if not out_file:
        out_file = in_file + '.enc'

    # Opens input file to be read as bytes
    # Opens output file to write bytes into
    with open(in_file, 'rb') as rfile, open(out_file, 'wb') as wfile:
        encrypt = None

        # Get the encryption function associated with the aes mode (ECB or CBC)
        if mode == aes.Mode.ecb:
            encrypt = aes.ecb_encryption(key_schedule)
        else:
            encrypt = aes.cbc_encryption(key_schedule, iv)

        for chunk,_ in read_chunks(rfile, chunk_size):
            # Process 16 length chunk into 4 lists containing 4 numbers
            processed_chunk = [list(chunk[i*4:(i+1)*4]) for i in range(len(chunk)//4)]

            # Perform aes encryption
            encrypted_chunk = encrypt(processed_chunk)

            # Convert the encrypted chunk back into a byte object
            encrypted_byte_object = b''.join(bytes(i) for i in encrypted_chunk)

            # Write chunk to output file
            wfile.write(encrypted_byte_object)

    return out_file

def decrypt_file(key_schedule, in_file, out_file=None, chunk_size=16, mode=aes.Mode.ecb, iv=None):
    """
    Decrypt a file using specified aes mode.

    Args:
        key_schedule: list(list(integer)), the key schedule for aes
        in_file: string, file path of file to be decrypted
        out_file: string [default: None], file path where the decrypted file should be stored
        chunk_size: integer [default: 16], the size of the blocks to be processed
        mode: string [default: "ECB"], aes.Mode.ecb or aes.Mode.cbc
        iv: list(integer) [default: None], initialization vector needed for aes some modes

    Returns:
        out_file: string [default: file_path without ".enc"], the filepath of the decrypted file
    """
    decrypt_filesize = os.path.getsize(in_file)

    # If no output file name passed, creates one based on input file name
    if not out_file:
        out_file = os.path.splitext(in_file)[0]

    # Opens input file to be read as bytes
    with open(in_file, 'rb') as rfile, open(out_file, 'wb') as wfile:
        decrypt = None
        padding_size = 0

        # Get the decryption function associated with the aes mode (ECB or CBC)
        if mode == aes.Mode.ecb:
            decrypt = aes.ecb_decryption(key_schedule)
        else:
            decrypt = aes.cbc_decryption(key_schedule, iv)

        # Iterates over entire file
        for chunk,done in read_chunks(rfile, chunk_size, None):
            if done:
                decrypt_filesize -= padding_size
                break
            # Process 16 length chunk into 4 lists containing 4 numbers
            processed_chunk = [list(chunk[i*4:(i+1)*4]) for i in range(len(chunk)//4)]

            # Perform aes decryption
            decrypted_chunk = decrypt(processed_chunk)

            # Convert the decrypted chunk back into a byte object
            decrypted_byte_object = b''.join(bytes(i) for i in decrypted_chunk)
            padding_size = decrypted_byte_object[-1]

            # Writes currently read chunk into the output file
            wfile.write(decrypted_byte_object)

        # Truncates output file to original size, removing buffer
        wfile.truncate(decrypt_filesize)

    return out_file
# Driving function for testing
def main():

    # Testing has been moved to aes_test.py

    key = helper.generate_random_key(16)
    key_schedule, _ = aes.gen_key_schedule(key)

    encrypt_file(key_schedule, test_file_path, test_encrypt_path)
    print(filecmp.cmp(test_file_path, test_encrypt_path))

    decrypt_file(key_schedule, test_encrypt_path, test_decrypt_path)
    # Testing to see if decrypted file is same as original
    print(filecmp.cmp(test_file_path, test_decrypt_path))

if __name__ == '__main__':
    main()
