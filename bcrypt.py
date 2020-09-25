from Crypto.Cipher import Blowfish
from Crypto.Util.number import long_to_bytes

def tobytestring(val, nbits):
    """Convert an integer (val, even negative) to its byte string representation.
    Parameter nbits is the length of the desired byte string (in bits).
    """
    return long_to_bytes((val + (1 << nbits)) % (1 << nbits), nbits/8)

key = b'jaas is the way'
c1  = Blowfish.new(key, Blowfish.MODE_ECB)

fromjava = b"-27038292d345798947e2852756afcf0a"
# We don't know the real length of the ciphertext, assume it is 16 bytes
ciphertext = tobytestring(int(fromjava, 16), 16*8)
print(c1.decrypt(ciphertext))