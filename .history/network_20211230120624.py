# network.py
# Daniel Kogan
# 12.30.2021

from datetime import datetime
import hashlib

class Blockchain:
    difficulty = 2
    
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = [Block.genesis_block()]
        
    def proof_of_work(self, block):
        #block.nonce =
        while not block.hash.startswith('0'* Blockchain.difficulty):
            block.nonce += 1
            block.hash = block.hash_block()
        return block.hash
            
    def add_block(self, block, proof):
        prev_hash = self.last_block.hash
        if prev_hash != block.prev_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
    
    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.hash_block())
    
    def add_new_data(self, transaction):
        self.unconfirmed_transactions.append(transaction)
        
    def mine(self):
        if not self.unconfirmed_transactions:
            return False
        last_block = self.last_block
        new_block = Block(last_block.index + 1, datetime.now(), )
    
    @property
    def last_block(self):
        return self.chain[-1]
    
class Block:
    def __init__(self, index, timestamp, data, prev_hash, nonce=0):
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
        data = str(index) + 'lol im just an epic block in an epic world'
        return Block(index,timestamp,data,prev_hash_block)
    
blockchain = Blockchain()
prev_block = blockchain.chain[0]
prev_block.print()

for i in range(0,5):
    add_block = Block.new_block(prev_block)
    blockchain.chain.append(add_block)
    prev_block = add_block
    
    add_block.print()
    
