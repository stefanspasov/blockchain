from backend.blockchain.block import Block

class Blockchain: 
    """
    Blockchain: a public ladger of transactions. 
    Implemented as a list of blocks - data sets of txns. 
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))
    
    def __repr__(self):
        return f'Blockchain: {self.chain}'

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
        Enforce the following rules of the blockchain. 
            - the chain must start with the genesis block 
            - all blocks must be valid
        """
        if chain[0] != Block.genesis():
            raise Exception('The chain must start with genesis')
        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)


def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    print(blockchain)

if __name__ == '__main__':
    main()