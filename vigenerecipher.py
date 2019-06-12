#!/usr/bin/env python

import collections
import string
import itertools


message = "ATTACKATDAWN"
key = "LEMON"

def encrypt(message, key, multiplier = -1):
	compressed_message = message.replace(' ', '').lower()

	for punc in str(string.punctuation):
		compressed_message = compressed_message.replace(punc, '')

	key = key.lower()
	cycler = itertools.cycle( key )
	long_key = ''.join([ cycler.next() for _ in range(len(compressed_message))])

	coded = []
	for num in range(len(long_key)):
		cipher_letter = compressed_message[num]
		key_letter = long_key[num]
		cipher_index = string.lowercase.index(cipher_letter)
		key_index = string.lowercase.index(key_letter)

		lowercase = collections.deque( string.lowercase ) # or ( string.lowercase + string.digits )
		lowercase.rotate( multiplier * key_index)
		new_alph = ''.join(list(lowercase))
		new_char = new_alph[cipher_index]
		coded.append(new_char)

	return ''.join(coded)

def decrypt():
	return encrypt(message, key, 1)


def permute_sha256(encrypted):
	for p in itertools.permutations(string.lowercase, 4):
		key = ''.join(p)
		decrypted = decrypt(encrypted[:5], key)
		
		if decrypted == "tjctf":
			print "We found the correct key"
			print key
			break

	start_of_key = key[:5]

	for p in itertools.permutations(string.lowercase, 4):
		key = start_of_key + ''.join(p)
		decrypted = decrypt(encrypted, key)
		flag = decrypted[:5] + '{' + decrypted[5:] + '}'

		s = hashlib.sha256()
		s.update(flag)
		that_hash = s.hexdigest()
		if that_hash == given_hash:
			print "We got it!"
			print flag
			break

print(encrypt(message, key))

encrypted = ""

	