# Events and Logs

If you’re on this page, you’re likely looking for an answer to this question:
**How do I know when a specific contract is used?** You have several options:

-

Query blocks for transactions that include the contract address in the `"to"` field.
This contrived example is searching the latest block for any transactions sent to the
WETH [https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2#code] contract.

```
WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'

block = w3.eth.get_block('latest')
for tx_hash in block.transactions:
    tx = w3.eth.get_transaction(tx_hash)
    if tx['to'] == WETH_ADDRESS:
        print(f'Found interaction with WETH contract! {tx}')

```
