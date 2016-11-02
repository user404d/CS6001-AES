import os, struct, filecmp, aes_impl as aes, helper_functions as helper

# Hard coded file path names, will be changed to command line args
test_file_path = 'test_img.jpg'
test_encrypt_path = 'test_encrypt.jpg'
test_decrypt_path = 'test_decrypt.jpg'

def encrypt_file(key_schedule, in_file, out_file=None, chunk_size=16):

    # Calculating initial file size
    filesize = os.path.getsize(in_file)

    # If no output file name passed, creates one based on input file name
    if not out_file:
        out_file = in_file + '.enc'

    # Opens input file to be read as bytes
    with open(in_file, 'rb') as rfile:
        # Opens output file to write bytes into
        with open(out_file, 'wb') as wfile:

            # Storing initial filesize in first line
            wfile.write(struct.pack('<Q', filesize))

            while True:
                # Reads file a chunk at a time
                chunk = rfile.read(chunk_size)
                # Exits while loop if chunk is empty
                if len(chunk) == 0:
                    break
                # Appends buffer to chunk if below 16 bytes
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                # Process 16 length chunk into 4 lists containing 4 numbers
                processed_chunk = [list(chunk[i*4:(i+1)*4]) for i in range(len(chunk)//4)]

                # Perform aes encryption 
                encrypted_chunk = aes.encrypt(processed_chunk, key_schedule)

                # Convert the encrypted chunk back into a byte object
                encrypted_byte_object = b''.join(bytes(i) for i in encrypted_chunk)

                # Write chunk to output file
                wfile.write(encrypted_byte_object) 

def decrypt_file(key_schedule, in_file, out_file=None, chunk_size=16):

    # If no output file name passed, creates one based on input file name
    if not out_file:
        out_file = os.path.splittext(in_file)[0]

    # Opens input file to be read as bytes
    with open(in_file, 'rb') as rfile:

        # Retrieves original file size from first line of encrypted file
        origsize = struct.unpack('<Q', rfile.read(struct.calcsize('Q')))[0]

        # Opens output file to write bytes into
        with open(out_file, 'wb') as wfile:

            # Iterates over entire file
            while True:
                # Reads from input file one chunk at a time
                chunk = rfile.read(chunk_size)
                # If chunk is empty, exits the while loop
                if len(chunk) == 0:
                    break

                # Process 16 length chunk into 4 lists containing 4 numbers
                processed_chunk = [list(chunk[i*4:(i+1)*4]) for i in range(len(chunk)//4)]

                # Perform aes decryption 
                decrypted_chunk = aes.decrypt(processed_chunk, key_schedule)

                # Convert the encrypted chunk back into a byte object
                decrypted_byte_object = b''.join(bytes(i) for i in decrypted_chunk)

                # Writes currently read chunk into the output file
                wfile.write(decrypted_byte_object) 

            # Truncates output file to original size, removing buffer
            wfile.truncate(origsize)

# Driving function for testing
def main():
    key = helper.generate_random_key_of_size(16)
    key_schedule, _ = aes.gen_key_schedule(key)

    encrypt_file(key_schedule, test_file_path, test_encrypt_path)
    decrypt_file(key_schedule, test_encrypt_path, test_decrypt_path)

    # Testing to see if decrypted file is same as original
    print(filecmp.cmp(test_file_path, test_decrypt_path))

if __name__ == '__main__':
    main()
