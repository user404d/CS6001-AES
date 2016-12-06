import unittest
import aes_impl as aes
import helper_functions as helper
import aes_io 
import filecmp

class AESTest(unittest.TestCase):

        test_file_path = 'test_img.jpg'
        test_encrypt_path = 'test_encrypt.jpg'
        test_decrypt_path = 'test_decrypt.jpg'

        def test_ecb_on_file(self):
                key = helper.generate_random_key(16)
                key_schedule, _ = aes.gen_key_schedule(key)

                aes_io.encrypt_file(key_schedule, self.test_file_path, self.test_encrypt_path, mode=aes.Mode.ecb)
                self.assertFalse(filecmp.cmp(self.test_file_path, self.test_encrypt_path))
                
                aes_io.decrypt_file(key_schedule, self.test_encrypt_path, self.test_decrypt_path, mode=aes.Mode.ecb)
                self.assertTrue(filecmp.cmp(self.test_file_path, self.test_decrypt_path))

        def test_ecb_on_string(self):
                data = helper.get_byte_list_from("This is a secret message. Such secret. Much crypto. Wow aes. xD.")

                key = helper.generate_random_key(16)
                key_schedule, _ = aes.gen_key_schedule(key)

                encrypt = aes.ecb_encryption(key_schedule)
                encrypted_data = encrypt(data)

                decrypt = aes.ecb_decryption(key_schedule)
                decrypted_data = decrypt(encrypted_data)

                self.assertTrue(data == decrypted_data)
                self.assertTrue(not data is decrypted_data)

        def test_cbc_on_file(self):
                data_size = 16

                key = helper.generate_random_key(data_size)
                key_schedule, _ = aes.gen_key_schedule(key)

                iv = helper.initialization_vector(data_size)

                aes_io.encrypt_file(key_schedule, self.test_file_path, self.test_encrypt_path, 
                                    chunk_size=data_size, mode=aes.Mode.cbc, iv=iv)
                self.assertFalse(filecmp.cmp(self.test_file_path, self.test_encrypt_path))
                
                aes_io.decrypt_file(key_schedule, self.test_encrypt_path, self.test_decrypt_path, 
                                    chunk_size=data_size, mode=aes.Mode.cbc, iv=iv)
                self.assertTrue(filecmp.cmp(self.test_file_path, self.test_decrypt_path))

        def test_cbc_on_string(self):
                data = helper.get_byte_list_from("1234567891234567")

                data_size = len(data) * 4

                key = helper.generate_random_key(data_size)
                key_schedule, _ = aes.gen_key_schedule(key)

                iv = helper.initialization_vector(data_size)

                encrypt = aes.cbc_encryption(key_schedule, iv)
                encrypted_data = encrypt(data)

                decrypt = aes.cbc_decryption(key_schedule, iv)
                decrypted_data = decrypt(encrypted_data)

                self.assertTrue(data == decrypted_data)
                self.assertTrue(not data is decrypted_data)

if __name__ == "__main__":
        unittest.main()
