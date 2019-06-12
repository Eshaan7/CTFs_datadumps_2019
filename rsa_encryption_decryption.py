#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-25 14:33:10
# @Last Modified by:   john
# @Last Modified time: 2016-12-03 11:16:39

from Crypto.Util.number import getPrime, inverse
import binascii

'''
This Python code tries to illustrate how RSA is done at a basic level.
'''


# At RSA's core, there are two PRIME factors, p and q.
# With this code, I just generate two large random prime numbers.
# p and q are typically NOT given to you in an RSA challenge.
bits_size = 256
p = getPrime( bits_size )
q = getPrime( bits_size )


# These two prime factors multiply to create n, which is "the modulus".
# n is typically GIVEN to you in an RSA challenge.
n = p * q


# The plaintext is typically referred to as m. Since we are working 
# with numbers and math, we treat the string information as hex.
# Obviously this is NEVER given to you in an RSA challenge.
m = "This is the clear text message."
m = binascii.hexlify(m)
m = int(m, 16)


# Another value, called e, is "the exponent".
# Both e and n make up "the public key", which is meant to be common
# knowledge. This is why typically n and e are BOTH GIVEN in an RSA challenge.
# Typcially, e is 65537, which is 0x10001 in hex
e = 0x10001


# The ciphertext, c, is created by this ENCRYPTION formula here.
#    c = ( m ^ e ) % n
# See how e is the exponent and n is the modulus?
# That is how the ENCRYPTION takes place.
# Typically you are given the c in an RSA challenge and it is your task
# to DECRYPT it to the m value, the plaintext.
c = pow( m, e, n )


# Now how do we decrypt? We need "the private key"....
# We call this d in RSA. Thanks to some handy mathematical functions,
# you can find "Euler's Totient", or "the Phi function" of a number.
# This is 'the number of numbers that are less than a certain number and share
# a common denominator with that certain number'.
# I know that is hard to wrap your mind around here, but thankfully it is MUCH
# easier for a prime number. For a prime number, it is simply that number minus 1!

# So, if you are given n, what you need to do is find the factors of n. 
# Like we've seen, this is typically p and q. So, can we find the phi function
# of n? Well, n is prime, and so are its factors, p and q, so phi should just be: 
phi = ( q - 1 ) * ( p - 1 )


# Now, we can kind of unravel that modular arithmetic that was done during the
# ENCRYPTION formula. We can find the private key, d, with the MODULAR INVERSE,
# of e and phi.  
# I use a module to do this that is reworked to use Trey's function
#     https://github.com/JohnHammond/primefac_fork
d = inverse( e, phi )

# Now, we can do a similar thing like before, but this time for DECRYPTION.
#        m = ( c ^ d ) % n
# This time we raise to our private key as an exponent, but still take the modulus.
# And we have successfully decrypted RSA!
m = pow( c, d, n )
print repr(binascii.unhexlify(hex(m)[2:-1]))