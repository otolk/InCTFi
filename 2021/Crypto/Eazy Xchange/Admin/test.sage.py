

# This file was *autogenerated* from the file test.sage
from sage.all_cmdline import *   # import sage library

_sage_const_4 = Integer(4); _sage_const_0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF = Integer(0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF); _sage_const_3 = Integer(3); _sage_const_0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B = Integer(0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B); _sage_const_16 = Integer(16); _sage_const_0 = Integer(0)
import os, hashlib, pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = os.urandom(_sage_const_4 )
FLAG = open('flag.txt', 'rb').read()
p = _sage_const_0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF 
a = p - _sage_const_3 
b = _sage_const_0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B 

def gen_key(G, pvkey):
	G = sum([i*G for i in pvkey])
	return G

def encrypt(msg, key):
	key = hashlib.sha256(str(key).encode()).digest()[:_sage_const_16 ]
	cipher = AES.new(key, AES.MODE_CBC, os.urandom(_sage_const_16 ))
	return {'cip': cipher.encrypt(pad(msg, _sage_const_16 )).hex(), 'iv': cipher.IV.hex()}

def gen_bob_key(EC, G):
	bkey = os.urandom(_sage_const_4 )
	B = gen_key(G, bkey)
	return B, bkey

def main():
	EC = EllipticCurve(GF(p), [a, b])
	G = EC.gens()[_sage_const_0 ]
	# Bx = int(input("Enter Bob X value: "))
	# By = int(input("Enter Bob Y value: "))
	# B = EC(Bx, By)
	B, bkey = gen_bob_key(EC, G)
	P = gen_key(G, key)
	SS = gen_key(B, key)
	assert sum(bkey)*sum(key)*G == SS
	print(sum(bkey)*sum(key))
	cip = encrypt(FLAG, SS.xy()[_sage_const_0 ])
	cip['G'] = str(G)
	return cip

if __name__ == '__main__':
	cip = main()
	pickle.dump(cip, open('enc.pickle', 'wb'))

