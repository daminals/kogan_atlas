# wallet.py
# Daniel Kogan
# 12.31.2021

# TODO: create a wallet with public and private tokens in order to create transactions and ownership
import random, hashlib, string, requests
from Crypto.PublicKey import RSA

def create_wallet():
    #chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    #return ''.join(random.choice(chars) for _ in range(65))
    return RSA.generate(2048)

class Wallet:
    def __init__(self, private):
        self.private = private
        self.public = self.make_public(self.private.encode()).hexdigest()
            
    def make_public(self, private):
        return hashlib.sha256(private)
    
    def send(self, address, data):
        send_data = {'data': {
            'from': self.private,
            'to': address,
            'data': data
        }}
        
key = create_wallet()
print(key)
print(key.publickey())

#my_wallet = Wallet(create_wallet())
#print(my_wallet.public)