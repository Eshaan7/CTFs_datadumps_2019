#!/usr/bin/env python2

from pwn import *
from pyfiglet import Figlet
from PIL import Image, ImageDraw, ImageFont

r = remote('104.154.120.223', 8083) # nc 104.154.120.223 8083

#r.send("Hello world!\n")
resp = r.recv()
print resp.encode('utf-8')
print r.recvuntil(">>>")

img = Image.new('RGB', (400, 400), color = 'white')
d = ImageDraw.Draw(img)
d.text((200,200), resp, fill=(0,0,0))
 
img.save('pil_text.png')

#r.send(str(input()))
#f = Figlet(font='banner')
#print f.renderText('Forensics')




'''
import socket

def get_expr(resp):
	#resp = resp.split('\n')
	#return resp[len(resp) - 2]

def parse_expr(expr):
	expr = expr.split(' ')
	x = int(expr[0])
	y = int(expr[2])
	operator = expr[1]
	if operator == '+':
		return x + y
	if operator == '-':
    	return x - y
	if operator == '*':
		return x * y
	if operator == '/':
		return x / y
	if operator == '%':
   		return x % y


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('104.154.120.223', 8083))
resp = conn.recv(4096)

print resp

while '>>>' not in resp:
    res = parse_expr(get_expr(resp))
    print res
    #conn.send(str(res) + '\n')
    resp = conn.recv(4096)

print resp
'''