from urllib import request
import requests
import base64
import random
import string

from PIL import Image

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad 


from io import BytesIO
# from django.core.files.base import ContentFile

#Randomly generate 16 strings composed of lowercase letters
def key_generator(size = 16, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

key = "wyhpsvsaifjboinqqjiaglhcqelwglip"

PUBLIC_KEY =  "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC1EHQm5s2/6nfeOKI9Gj3MNcwZ\nLwpUS7VGpl+DpnCe9j1lsRZ0wLkSaqJ+WMDHFqQCF/8os45Bw/68UPYSs5NLCTob\nWSutZfTWqxkd6I1r55yccW6tPoHG0431oDgZ5e2iEizr3KO+WE8k2ncsIz/s0zvW\nm1j/ggCEg4w3/PZdswIDAQAB\n-----END PUBLIC KEY-----",
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC1EHQm5s2/6nfeOKI9Gj3MNcwZLwpUS7VGpl+DpnCe9j1lsRZ0\nwLkSaqJ+WMDHFqQCF/8os45Bw/68UPYSs5NLCTobWSutZfTWqxkd6I1r55yccW6t\nPoHG0431oDgZ5e2iEizr3KO+WE8k2ncsIz/s0zvWm1j/ggCEg4w3/PZdswIDAQAB\nAoGAWUEdILgRoJNCN4cPYrN21x2F2Lw5iUgwufz1hH4dch7MMT7UZQVDtfJe242A\nqiNdAbM2kqfAbmbhQY9fXeSrrDMl622Ug1remX2V0msBsdLrpPKs8Vog1VMI21/l\njHan2bEYSu/XbfpvJHIWb8Ttd+cD/1D+wAR0EMoxSS5dNxECQQDeg2Pnpb87RaJz\nZ3NHH9UXbRD3ge1vY52hWJpXVmEbCPvwEx4nKoWGxCpwYQ1q65BmrwtpknT9gPzu\nR2GtNQCvAkEA0FAwOntiOtWWCGBAxbA9uWZdm7r8IreH3CZgZdRb1vuofLTdUYvQ\nSIIgtdnRWlqxnxdq4CPA7n3vV0DZKsMMPQJAC4X+bIa26pjmmtdmru5FGNt7H3ZJ\nF5WvGiX+iDte+Al1Eq/Kxfh7xcju8bb0/O6KIec6zhLZoC9H6gckVdYC3QJAEoFt\nJ2TanxtmTqwuVOGJOjUrz6/WwkbHnPkTyzgISJrmpt1yY9Il2KsmuMD25i30ZYux\nBORoOUeawYeTQ0c8iQJBAMJhrkZJgCofPMaFfAz8q4K9rnm+h0xSQoIZ34Yp5x9Y\nrn2K4kil29d7CW/nc2aVEin6m1DjAF0JYaJA4lb+ezg=\n-----END RSA PRIVATE KEY-----"

# CBC Encryption
def aes_cbc_encrypt(key, data, mode=AES.MODE_CBC):
    #IV is a random value
    IV = key_generator(16)
    aes = AES.new(str.encode(key), mode, str.encode(IV))

    # b64_data = base64.b64encode(pad(data.encode('utf-8'), AES.block_size))
    cipher = aes.encrypt(pad(data.encode('utf-8'), AES.block_size))
    cipher_to_b64 = base64.b64encode(cipher)
    return IV + bytes.decode(cipher_to_b64)

with open('example.pdf', 'rb') as f:
    file_to_b64 = base64.b64encode(f.read()).decode('utf-8')

    enc_pdf = aes_cbc_encrypt(key, file_to_b64)

    data = {
        "pdf" : enc_pdf
    }

    url = "http://127.0.0.1:8000"
    endpoint = url + "/accounts/input-sensitive"


    res = requests.post(url=endpoint, json=data)

    print(res.content)


