# wallet.py
# Daniel Kogan
# 12.31.2021

# TODO: create a wallet with public and private tokens in order to create transactions and ownership
import random, hashlib, string
import firebase_admin
from firebase_admin import credentials, firestore

def create_wallet():
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    return ''.join(random.choice(chars) for _ in range(65))

class Wallet:
    length = 20
    def __init__(self, private=None):
        if private:
            self.private
            
    def func(self):
        pass

print(create_wallet())