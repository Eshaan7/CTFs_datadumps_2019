import requests
import json

MAP = {97: '10', 98: '120', 99: '140', 100: '1450', 101: '150', 102: '1240', 103: '12450', 104: '1250', 105: '240', 106: '2450', 107: '130', 108: '1230', 109: '1340', 110: '13450', 111: '1350', 112: '12340', 113: '123450', 114: '12350', 115: '2340', 116: '23450', 117: '1360', 118: '12360', 119: '24560', 120: '13460', 121: '134560', 122: '13560'}
MAP[ord(",")] = "20"
MAP[ord(";")] = "230"
MAP[ord(":")] = "250"
MAP[ord(".")] = "2560"
MAP[ord("!")] = "2350"
MAP[ord("?")] = "2360"
MAP[ord("/")] = "340"
MAP[ord("'")] = "30"
MAP[ord("-")] = "360"
MAP[ord(" ")] = "00"
MAP[ord("=")] = "5023560"
MAP[ord("+")] = "502350"
MAP[ord('"')] = "5023560"
MAP[ord("0")] = "34562450"
MAP[ord("1")] = "345610"

f = lambda x: ''.join([MAP[ord(e)] for e in x])

url="https://bnv.web.ctfcompetition.com/api/search"
headers = {'Content-type': 'application/json'}

datasend = json.dumps({
    'message': f('zurich+paris'),
})

print "[+] Post data: ",datasend

r = requests.post(url=url, data=datasend, headers=headers)
print "\n[+] ResponseJson: ", r.text
#print "\n[+] ResponseHeaders: ", r.headers