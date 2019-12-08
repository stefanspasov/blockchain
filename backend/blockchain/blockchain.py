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

    def to_json(self):
        """
        Serialize the chain into a list of blocks
        """
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def from_json(chain_json):
        blockchain = Blockchain()
        blockchain.chain = list(
            map(lambda block_json: Block.from_json(block_json), chain_json)
        )
        return blockchain

    def replace_chain(self, new_chain):
        """
        Replace the local chain with the incoming one if the following applies:
         - The incoming chain is longer than the local
         - The incomng chain is valid
        """
        if len(new_chain) <= len(self.chain):
            raise Exception('Cannot replace. The incoming chain must be longer')

        try:
            Blockchain.is_valid_chain(new_chain)
        except Exception as e:
            raise Exception(f'Cannot replace. The incoming chain is invalid: {e}')

        self.chain = new_chain 

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