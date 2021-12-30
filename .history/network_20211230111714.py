# network.py
# Daniel Kogan
# 12.30.2021

from datetime import datetime
import hashlib

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()
    
    def hash_block(self):
        block_encryption = hashlib.sha256()
        block_encryption.update(str(self.index)+(str(self.timestamp)+str(self.data)+str(self.prev_hash)))
        return block_encryption.hexdigest()
    
    @staticmethod
    def genesis_block():
        return Block(0, datetime.now(), "create block_encryption  block lol")
