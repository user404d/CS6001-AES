import unittest
import aes_impl 
import helper_functions as helper

class AESTest(unittest.TestCase):

	def test_key_schedule_generation(self):
		pass

	def test_encryption_and_decryption(self):
		data = helper.get_byte_list_from("This is a secret message.")
		# key = list(b'this is awesome.')
		key = helper.generate_random_key_of_size(16)
		key_schedule, _ = aes_impl.gen_key_schedule(key)

		encrypted_data = aes_impl.encrypt(data, key_schedule)
		decrypted_data = aes_impl.decrypt(encrypted_data, key_schedule)
		self.assertTrue(data == decrypted_data)


if __name__ == "__main__":
	unittest.main()
