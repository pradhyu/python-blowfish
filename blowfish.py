from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack

bs = Blowfish.block_size
key = b'jaas is the key'
iv = Random.new().read(bs)
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
plaintext = b'monday123'
plen = bs - divmod(len(plaintext),bs)[1]
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg = iv + cipher.encrypt(plaintext + padding)
print("encrypted")
print(msg)
ciphertext=msg


print("hex to ")
msg.decode("utf-8")

#ciphertext = b'\xe2:\x141vp\x05\x92\xd7\xfa\xb5@\xda\x05w.\xaaRG+U+\xc5G\x08\xdf\xf4Xua\x88\x1b'
print("_____________________")
iv = ciphertext[:bs]
ciphertext = ciphertext[bs:]

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(ciphertext)
print(msg)
last_byte = msg[-1]
msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
print(repr(msg))