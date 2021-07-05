#Import hash library
import hashlib

#import random for salting
import random, string

#Intialise the string/password to be hashed
Password = 'hereiam'

#salting

def randomword():
	letters = string.ascii_lowercase
	return''.join(random.choice(letters)for i in range(5))
Salt = randomword()

Salted_Word = Password + Salt
#print(Salted_Word)
encrypted = hashlib.md5(Salted_Word.encode())
print(encrypted.hexdigest())