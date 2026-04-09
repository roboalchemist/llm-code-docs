# Utils

The `utils` module houses public utility functions and classes.

## ABI

web3.utils.abi.get_abi_element_info(*abi: Sequence [https://docs.python.org/3/library/typing.html#typing.Sequence][ABIFunction | ABIConstructor | ABIFallback | ABIReceive | ABIEvent | ABIError]*, *abi_element_identifier: str [https://docs.python.org/3/library/stdtypes.html#str] | type [https://docs.python.org/3/library/functions.html#type][FallbackFn] | type [https://docs.python.org/3/library/functions.html#type][ReceiveFn]*, **args: Sequence [https://docs.python.org/3/library/typing.html#typing.Sequence][Any [https://docs.python.org/3/library/typing.html#typing.Any]] | None [https://docs.python.org/3/library/constants.html#None]*, *abi_codec: Any [https://docs.python.org/3/library/typing.html#typing.Any] | None [https://docs.python.org/3/library/constants.html#None] = None*,***kwargs: dict [https://docs.python.org/3/library/stdtypes.html#dict][str [https://docs.python.org/3/library/stdtypes.html#str], Any [https://docs.python.org/3/library/typing.html#typing.Any]] | None [https://docs.python.org/3/library/constants.html#None]*) → ABIElementInfo

Information about the function ABI, selector and input arguments.

Returns the ABI which matches the provided identifier, named arguments (`args`)
and keyword args (`kwargs`).

Parameters:

-

**abi** (ABI) – Contract ABI.

-

**abi_element_identifier** (ABIElementIdentifier) – Find an element ABI with matching identifier.

-

**args** (Optional[Sequence[Any]]) – Find a function ABI with matching args.

-

**abi_codec** (Optional[Any]) – Codec used for encoding and decoding. Default with     strict_bytes_type_checking enabled.

-

**kwargs** (Optional[Dict[str, Any]]) – Find an element ABI with matching kwargs.

Returns:

Element information including the ABI, selector and args.

Return type:

ABIElementInfo

```
>>> from web3.utils.abi import get_abi_element_info
>>> abi = [
...     {
...         "constant": False,
...         "inputs": [
...             {"name": "a", "type": "uint256"},
...             {"name": "b", "type": "uint256"},
...         ],
...         "name": "multiply",
...         "outputs": [{"name": "result", "type": "uint256"}],
...         "payable": False,
...         "stateMutability": "nonpayable",
...         "type": "function",
...     }
... ]
>>> fn_info = get_abi_element_info(abi, "multiply", *[7, 3])
>>> fn_info["abi"]
{'constant': False, 'inputs': [{'name': 'a', 'type': 'uint256'}, {'name': 'b', 'type': 'uint256'}], 'name': 'multiply', 'outputs': [{'name': 'result', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}
>>> fn_info["selector"]
'0x165c4a16'
>>> fn_info["arguments"]
(7, 3)

```
