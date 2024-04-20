import re, hashlib

secret_key = 'SCRUMDADDIES'

password = input('Password: ')

hash = password + secret_key
hash = hashlib.sha256(hash.encode())
password = hash.hexdigest()

print(password)