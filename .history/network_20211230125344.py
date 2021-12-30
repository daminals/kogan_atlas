# network.py
# Daniel Kogan
# 12.30.2021

from datetime import datetime
import hashlib, json

class Blockchain:
    difficulty = 2
    
    def __init__(self):
        self.unconfirmed_data = []
        self.chain = [Block.genesis_block()]
        
    def proof_of_work(self, block):
        #block.nonce =
        while not block.hash.startswith('0'* Blockchain.difficulty):
            #print(block.hash)
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
    
    def add_new_data(self, data):
        self.unconfirmed_data.append(data)
        
    def mine(self):
        if not self.unconfirmed_data:
            return False
        last_block = self.last_block
        #print(last_block)
        new_block = Block(last_block.index + 1, datetime.now(), self.unconfirmed_data[0], last_block.prev_hash)
        #print(new_block)
        proof = self.proof_of_work(new_block)
        print(proof)
        self.add_block(new_block, proof)
        self.unconfirmed_data = self.unconfirmed_data[0:]
        print(self.unconfirmed_data)
        return new_block.index
    
    def print(self):
        for i in self.chain:
            i.print()
    
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
        self.nonce = nonce
    
    def hash_block(self):
        print(self.__dict__)
        protected_data = json.dumps(self.__dict__)
        block_encryption = hashlib.sha256(protected_data.encode())
        return block_encryption.hexdigest()
    
    def data_dict(self):
        return {'index': str(self.index), 'timestamp': str(self.timestamp), 'data': str(self.data), 'prev'}
    
    def print(self): # print out block data
        block_data = self.data_dict()
        for key, value in block_data.items():
            print(key+': '+value)
        
    @staticmethod
    def genesis_block():
        return Block(0, datetime.now(), "create genesis block lol (like the terminator movie)", "")
        
blockchain = Blockchain()
prev_block = blockchain.chain[0]
blockchain.add_new_data("among us impostor")
print(blockchain.unconfirmed_data)
blockchain.mine()

blockchain.print()

