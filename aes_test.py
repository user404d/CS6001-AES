import unittest
import aes_impl as aes
import helper_functions as helper
import aes_io 
import filecmp

class AESTest(unittest.TestCase):

	def test_file_encryption_and_decryption(self):
		test_file_path = 'test_img.jpg'
		test_encrypt_path = 'test_encrypt.jpg'
		test_decrypt_path = 'test_decrypt.jpg'

		key = helper.generate_random_key_of_size(16)
		key_schedule, _ = aes.gen_key_schedule(key)

		aes_io.encrypt_file(key_schedule, test_file_path, test_encrypt_path)
		aes_io.decrypt_file(key_schedule, test_encrypt_path, test_decrypt_path)

		self.assertTrue(filecmp.cmp(test_file_path, test_decrypt_path))

	def test_encryption_and_decryption(self):
		data = helper.get_byte_list_from("This is a secret message.")

		key = helper.generate_random_key_of_size(16)
		key_schedule, _ = aes.gen_key_schedule(key)

		encrypted_data = aes.encrypt(data, key_schedule)
		decrypted_data = aes.decrypt(encrypted_data, key_schedule)
		self.assertTrue(data == decrypted_data)


if __name__ == "__main__":
	unittest.main()
