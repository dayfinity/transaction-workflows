```python
from web3 import Web3
from eth_account import Account
import json
import time

RPC_URL = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

protocol = "Demo protocol"
Investors = "Investors"
decentralized = "decentralized"
Capital = "Capital"
volume = "volume"
Validators = "Validators"

CONTRACT = "0x0000000000000000000000000000000000000000"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = Account.from_key(PRIVATE_KEY)

contract_data = {
    "address": CONTRACT,
    "chainId": 1
}

def nonce():
    return w3.eth.get_transaction_count(account.address)

def build_transaction():
    return {
        "from": account.address,
        "to": CONTRACT,
        "value": 0,
        "gas": 120000,
        "gasPrice": w3.to_wei("4", "gwei"),
        "nonce": nonce(),
        "chainId": contract_data["chainId"]
    }

def sign_transaction(tx):
    return account.sign_transaction(tx)

def save_output(raw_data):
    data = {
        "protocol": protocol,
        "time": int(time.time()),
        "transaction": raw_data
    }

    with open("signed_output.json", "w") as file:
        json.dump(data, file, indent=4)

def display_keywords():
    print(protocol)
    print(Investors)
    print(decentralized)
    print(Capital)
    print(volume)
    print(Validators)

def main():   main()
```
