class Affine(object):
	DIE = 128
	KEY = (7, 3, 55)
	def __init__(self):
		pass
	def encryptChar(self, char): # y = (ax + b) % SIZE
		K1, K2, KI = self.KEY
		return chr((K1 * ord(char) + K2) % self.DIE) 
		
	def encrypt(self, string):
		return "".join(map(self.encryptChar, string)) 

	def decryptChar(self, char):  # x = ( ( y - b ) / a ) INV_MOD SIZE
		K1, K2, KI = self.KEY
		return chr(KI * (ord(char) - K2) % self.DIE)

	def decrypt(self, string): 
		return "".join(map(self.decryptChar, string))

	#def bruteforce(self):
		
affine = Affine()

print affine.encrypt('Affine Cipher')
f = open('zakukozh.bin', 'rb').read().replace('\n','')
print affine.decrypt(f)