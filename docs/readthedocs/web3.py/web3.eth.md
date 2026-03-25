# web3.eth API

*class*web3.eth.Eth

The `web3.eth` object exposes the following properties and methods to
interact with the RPC APIs under the `eth_` namespace.

By default, when a property or method returns a mapping of keys to values, it
will return an `AttributeDict` which acts like a `dict` but you can
access the keys as attributes and cannot modify its fields. For example,
you can find the latest block number in these two ways:

```
>>> block = web3.eth.get_block('latest')
AttributeDict({
  'hash': '0xe8ad537a261e6fff80d551d8d087ee0f2202da9b09b64d172a5f45e818eb472a',
  'number': 4022281,
  # ... etc ...
})

>>> block['number']
4022281
>>> block.number
4022281

>>> block.number = 4022282
Traceback # ... etc ...
TypeError: This data is immutable -- create a copy instead of modifying

```
