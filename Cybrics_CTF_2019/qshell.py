#!/usr/bin/python3

from PIL import Image
import qrcode
from pwn import *



qr_src = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr_src.add_data('cat flag.txt')
qr_src.make(fit=True)

qr = qr_src.make_image(fill_color="black", back_color="white")
qr = qr.resize((33,33))

#qr = Image.open('ls_generated.png','r')

width,height = qr.size

data = b''


for y in range(height):
	for x in range(width):
		if(qr.getpixel((x,y)) == (255)):
			data += chr(9608).encode()
		else:
			data += b' '
	data += b'\n'
data += b'\n\n.\n'
qr.close()

print(data.decode())
#r = remote('spbctf.ppctf.net', 37338)
#received = r.recvuntil(b'.')
#r.send(data)
#flag = open('flag_qshell.txt','w').write(r.recvuntil(b'.'))
#r.close()
