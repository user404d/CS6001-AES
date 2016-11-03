import unittest
import rsa_impl as rsa

class RSATest(unittest.TestCase):

	def test_encryption_and_decryption(self):
		p = 17
		q = 19

		public_key, private_key = rsa.generate_keypair(p, q)
		message = "Secret message"
		encrypted_message = rsa.encrypt(public_key, message)
		self.assertFalse(message == encrypted_message)

		decrypted_message = rsa.decrypt(private_key, encrypted_message)
		self.assertTrue(message == decrypted_message)


if __name__ == "__main__":
	unittest.main()
