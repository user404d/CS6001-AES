import unittest
import aes_impl as aes
import helper_functions as helper

class AESTest(unittest.TestCase):

	def test_key_schedule_generation(self):
		pass

	def test_encryption_and_decryption(self):
		data = helper.get_byte_list_from("This is a secret message.")
		key = helper.generate_random_key_of_size(16)
		key_schedule, _ = aes.gen_key_schedule(key)

		encrypted_data = aes.encrypt(data, key_schedule)
		decrypted_data = aes.decrypt(encrypted_data, key_schedule)
		self.assertTrue(data == decrypted_data)


if __name__ == "__main__":
	unittest.main()
