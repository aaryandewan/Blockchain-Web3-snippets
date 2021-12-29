import solcx
from solcx import compile_standard, install_solc
import json

from web3 import Web3


with open("./simpleStorage.sol") as file:
    simple_storage_file = file.read()


compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)


w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xcca4A3ca184090BE522dbba63154Abd649337162"
private_key = "0x7a5d7bf70bc82ca49a9297e8ee350d8d955c6648daa7d0d589d0fc53760fb348"
