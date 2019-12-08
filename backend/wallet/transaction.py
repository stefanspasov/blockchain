import uuid
import time
from backend.wallet.wallet import Wallet

class Transaction: 
    """
    Exchange of currency from a sender to recepient
    """
    def __init__(self, sender_wallet, recipient, amount):
        self.id = str(uuid.uuid4())[0:8]
        self.output = self.create_output(
            sender_wallet, 
            recipient, 
            amount
        )
        self.input = self.craete_input(sender_wallet, self.output)

    def create_output(self, sender_wallet, recipient, amount):
        """
        Structure the output data for the transaction. 
        """
        if amount > sender_wallet.balance:
            raise Exception('Amount exceeds balance')

        output = {}
        output[recipient] = amount
        output[sender_wallet.address] = sender_wallet.balance - amount

        return output

    def craete_input(self, sender_wallet, output):
        """
        Structure the input data for the transaction. 
        Sign the transaction and include the sender public key and address. 
        """
        return {
            'timestamp' : time.time_ns(),
            'amount': sender_wallet.balance, 
            'address': sender_wallet.address, 
            'public_key': sender_wallet.public_key,
            'signature': sender_wallet.sign(output)
        }

    def update(self, sender_wallet, recipient, amount):
        """
        Update transaction with an existing or new recipient. 
        """
        if amount > self.output[sender_wallet.address]:
            raise Exception('Amount exceeds balance')

        if recipient in self.output: 
            self.output[recipient] = self.output[recipient] + amount
        else: 
            self.output[recipient] = amount

        self.output[sender_wallet.address] = \
            self.output[sender_wallet.address] - amount
        
        self.input = self.craete_input(sender_wallet, self.output)


def main():
    txn = Transaction(Wallet(), 'recipient', 15)
    print(f'tnx.__dict__: {txn.__dict__}')

if __name__ == '__main__':
    main()