#Import hash library
import hashlib
#Intialise String
string = 'Thankyouharsh'
#encode string
#then sending to md5
encrypted = hashlib.md5(string.encode())
print(encrypted.hexdigest())
