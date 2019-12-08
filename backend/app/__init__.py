import sys
import requests
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

ROOT_PORT = 5000
PORT = ROOT_PORT

try: 
    print('Peer')
    if sys.argv[1] == 'peer':
        PORT = random.randint(5001, 6000)
        result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
        result_blockchain = Blockchain.from_json(result.json())

        blockchain.replace_chain(result_blockchain.chain)
        print(f'result.json: {result.json()}')
        
except Exception as e: 
    print(f'Not a peer or error: {e}')

app.run(port=PORT)