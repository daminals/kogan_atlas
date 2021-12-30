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
        protected_data = str(self.index)+str(self.timestamp)+str(self.data)+str(self.prev_hash)
        block_encryption.update(protected_data.encode('utf-8'))
        return block_encryption.hexdigest()
    
    def print(self): # print out block data
        print(f"ID: {self.index}\n" +
          f"Timestamp: {self.timestamp}\n" + 
          f"Block Hash: {self.hash}\n"+
          f"Prev Hash {self.prev_hash}\n")
    
    @staticmethod
    def genesis_block():
        return Block(0, datetime.now(), "create genesis block lol (like the terminator movie)", "")
    
    @staticmethod
    def new_block(last_block):
        index = last_block.index + 1
        timestamp = datetime.now()
        prev_hash_block = last_block.hash
        data = str(index) + 'lol im just an epic '
        return Block(index,timestamp,data,prev_hash_block)
    
blockchain = [Block.genesis_block()]
prev_block = blockchain[0]
prev_block.print()

for i in range(0,5):
    add_block = Block.new_block(prev_block)
    blockchain.append(add_block)
    prev_block = add_block
    
    add_block.print()