# network.py
# Daniel Kogan
# 12.30.2021

import datetime
import hashlib

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hashBlock()
    
    def hashBlock(self):
        pass
