import hashlib

hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)

hash_result = hashlib.blake2b(b'Hello World')
print(hash_result.digest())

hash_res = hashlib.new('ripemd160')
hash_res.update(b'Hello World')
print(hash_res.hexdigest())