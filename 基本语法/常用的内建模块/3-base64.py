
# Base64是一种用64个字符来表示任意二进制数据的方法。
import base64
print(base64.b64decode(b'minyahui=='))# 编码
print(base64.b64encode(b'\x9a)\xf2j\x1b\xa2'))# 解码
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

