#!/usr/bin/env python3

import gmpy2
ciphertext = open('zakukozh.bin','br').read()

def getCoPrimes(m):
	coprimes = []
	dummy = 0
	for i in range(2,m):
		try:
			dummy = gmpy2.invert(i,m)
			coprimes.append(dummy)
		except:
			pass
	return coprimes
byte = []
coprimes = []
decrypted_data = b''
for m in range(26,255):
	coprimes = getCoPrimes(m)
	for a in coprimes:
		for b in range(1,255):
			decrypted_data = b''
			a_in = gmpy2.invert(a,m)
			for index in ciphertext:
				if chr(ciphertext[index]) not in byte:
					byte.append(chr(ciphertext[index]))
					decrypted_data = ciphertext.replace(chr(ciphertext[index]).encode(),chr((a*(a_in-ciphertext[index]))%m).encode())
				if decrypted_data.find(b'cybrics{') is not -1:
					print(decrypted_data[decrypted_data.lfind(b'cybrics'):decrypted_data.rfind(b'}')])