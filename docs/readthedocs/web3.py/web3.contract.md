# Contracts

Smart contracts are programs deployed to the Ethereum network. See the
ethereum.org docs [https://ethereum.org/en/developers/docs/smart-contracts]
for a proper introduction.

## Interacting with deployed contracts

In order to use an existing contract, you’ll need its deployed address and its ABI.
Both can be found using block explorers, like Etherscan. Once you instantiate a contract
instance, you can read data and execute transactions.

```
# Configure w3, e.g., w3 = Web3(...)
address = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F988'
abi = '[{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"minter_","type":"address"},...'
contract_instance = w3.eth.contract(address=address, abi=abi)

# read state:
contract_instance.functions.storedValue().call()
# 42

# update state:
tx_hash = contract_instance.functions.updateValue(43).transact()

```
