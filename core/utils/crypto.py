import io
import base64
import random
import string

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from django.core.files.base import ContentFile


key = "wyhpsvsaifjboinqqjiaglhcqelwglip"


def aes_decrypt(cipher_text):
    # IV 분리
    iv = cipher_text[:AES.block_size]

    # cipher 데이터 base64 복호화
    cipher = base64.b64decode(cipher_text[AES.block_size:])

    aes = AES.new(str.encode(key), AES.MODE_CBC, str.encode(iv))
    plain = aes.decrypt(cipher)

    return bytes.decode(unpad(plain, AES.block_size))


def image_to_file(image):
    in_memory_file = io.BytesIO()
    image.save(in_memory_file, format="PNG")
    in_memory_file.seek(0)

    return ContentFile(content=in_memory_file.getvalue())