from aes_impl import *

data = "I am a donger and so are you!!!!"
data = [list(bytes(data[i*4:(i+1)*4].encode('utf-8'))) for i in range(len(data)//4)]

key = list(b'this is awesome.')

ks,inv_ks = gen_key_schedule(key)

enc = encrypt(data,ks)
print("encrypted: ", enc)
dec = decrypt(enc,ks)
print("decrytped: ", dec)
enc = encrypt(data,ks)
print("encrypted: ", enc)
b_dec = nice_decrypt(enc,ks)
print("other decrypted: ", b_dec)
