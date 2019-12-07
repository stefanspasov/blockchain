import sys
import random
from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub


app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)

for i in range(3):
    blockchain.add_block(i)

@app.route('/')
def default():
    return 'Welcome to the blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transaction_data'
    blockchain.add_block(transaction_data)
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())

app.run(port=random.randint(5001, 6000))