#!/usr/bin/python

import sys
import fractions
import re

# lowercase alphabet + digits [0..9]
ALPHABET_SIZE = 36

def encrypt_char(a, b, m, x):
    return ( a*x + b ) % m  # y = (ax + b) % m

def decrypt_char(a, b, m, y):
    a_inv = inverse(a, m)  # x = ( ( y - b ) / a ) INV_MOD m
    return ( a_inv * (y-b) ) % m

def inverse(x, m):
    possible_a_inv = [a for a in range(0,ALPHABET_SIZE) 
                        if fractions.gcd(a, ALPHABET_SIZE) == 1]
    for i in possible_a_inv:
        if (x*i)%m == 1:
            return i

def encrypt(a, b, x, m):
    y = []
    for i in x:
        y.append(chr(encrypt_char(a, b, m, ord(i))))

    return ''.join(y)

def decrypt(a, b, y, m):
    x = []
    for i in y:
        x.append(chr(decrypt_char(a, b, m, ord(i))))

    return ''.join(x)

def bruteforce():
    message = open('zakukozh.bin', 'r').read() #.replace('\n','')
    #reference = "FF D8 FF DB"
    possible_a = [a for a in range(0, ALPHABET_SIZE) 
                    if fractions.gcd(a, ALPHABET_SIZE) == 1]
    pattern = re.compile(r".*cybrick{.*}.*")
    for a in possible_a:
        for b in range(0, ALPHABET_SIZE):
            #if encrypt(a, b, reference, ALPHABET_SIZE) == message[0:len(reference)]:
                #print(encrypt(a, b, reference, ALPHABET_SIZE))
            possible_plaintext = re.match(pattern, decrypt(a, b, message, ALPHABET_SIZE))
            if possible_plaintext is not None:
                print('[+]',possible_plaintext.group())
            else:
                continue

def usage(command):
    print("Usage: " + command + " {-b | -d | -e} [a] [b] [message] [reference]")
    print("Options:")
    print("-b   bruteforce. Requires message and reference, ignores a and b")
    print("-d   decrypt. Requires key pair a and b and message, ignores reference")
    print("-e   encrypt. Requires key pair a and b and message, ignores reference")

def main(argv):
    if len(argv) < 2:
        usage(argv[0])

    elif argv[1] == "-b":
        print(bruteforce())

    elif argv[1] == "-d":
        a = int(argv[2])
        b = int(argv[3])
        y = argv[4]
        m = ALPHABET_SIZE
        print(decrypt(a, b, y, m))

    elif argv[1] == "-e":
        a = int(argv[2])
        b = int(argv[3])
        x = argv[4]
        m = ALPHABET_SIZE
        print(encrypt(a, b, x, m))

    else:
        usage(argv[0])


if __name__ == "__main__":
    main(sys.argv)



