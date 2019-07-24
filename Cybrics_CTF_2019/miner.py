#!/usr/bin/env python3

from http import client
import threading

def makerequest():
	host = '45.77.201.191'

	conn = client.HTTPConnection(host)
	headers = {"Cookie":"name=lolcat; password=password",
				"Origin":"http://45.77.201.191",
				"Content-Type":"application/x-www-form-urlencoded",
				"Referer": "http://45.77.201.191/index.php"}

	url = "http://45.77.201.191/index.php"
	body = "mine=1"
	response = ''
	for i in range(0, 99999):
		conn.request('POST', url, body, headers)
		response = conn.getresponse()
		print(i, '|', response.status)
		conn.close()

for i in range(0, 5):
	process = threading.Thread(None, makerequest, None)
	process.start()
