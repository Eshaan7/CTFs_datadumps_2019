from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
from socket import inet_aton

import requests
import asyncio

async def check_func(hostname, port):
    #if len(hostname.split('.')) != 4:
    #	print('1') 
    #	0/0
    #if '127.' in hostname or '.0.' in hostname or '.1' in hostname:
    #	print('2') 
    #	0/0
    #if inet_aton(hostname) != b'\x7f\x00\x00\x01': # != ....
    #	print('3')
    #	0/0
    if not port: 
    	port = 80
    result = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(
                executor,
                lambda u: requests.get(u, allow_redirects=False, timeout=2),
                url
            ) for url in [f'http://{hostname}:{port}', 'http://127.0.0.1:3333']
        ]
        for res in await asyncio.gather(*tasks):
            print(res.text)
            result.append(res.text)

    print("[+] Result:", result)
    return result[1] if result[0] == result[1] else False

url = "45.77.247.11"
url = 'http://' + url
host_info = urlparse(url)._hostinfo
#print(host_info, *host_info)
asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.get_event_loop()
FLAG = loop.run_until_complete( asyncio.ensure_future( check_func(*host_info) ) )
print(FLAG)