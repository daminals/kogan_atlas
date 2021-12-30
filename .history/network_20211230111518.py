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
        block_encryption = hashlib.sha256()
        block_encryption.update(str(self.index)+(str(self.timestamp)+str(self.data)+str(self.prev_hash)))
        return block_encryption
