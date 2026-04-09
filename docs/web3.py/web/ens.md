# ENS API

Ethereum Name Service (ENS) has a friendly overview.

Continue below for the detailed specs on each method and class in the ens module.

## ens.ens module

*class*ens.ens.ENS(*provider: BaseProvider = None*, *addr: ChecksumAddress = None*, *middleware: Sequence [https://docs.python.org/3/library/typing.html#typing.Sequence][tuple [https://docs.python.org/3/library/stdtypes.html#tuple][Middleware, str [https://docs.python.org/3/library/stdtypes.html#str]]] | None [https://docs.python.org/3/library/constants.html#None] = None*)

Quick access to common Ethereum Name Service functions,
like getting the address for a name.

Unless otherwise specified, all addresses are assumed to be a str in
checksum format [https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md],  # blocklint: pragma # noqa: E501
like: `"0x314159265dD8dbb310642f98f50C066173C1259b"`

*classmethod*from_web3(*w3: Web3*, *addr: ChecksumAddress = None*) → ENS

Generate an ENS instance from a Web3 instance

Parameters:

-

**w3** (*web3.Web3*) – to infer connection, middleware, and codec information

-

**addr** (*hex-string*) – the address of the ENS registry on-chain. If not
provided, defaults to the mainnet ENS registry address.

address(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *coin_type: int [https://docs.python.org/3/library/functions.html#int] | None [https://docs.python.org/3/library/constants.html#None] = None*) → ChecksumAddress | None [https://docs.python.org/3/library/constants.html#None]

Look up the Ethereum address that name currently points to.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – an ENS name to look up

-

**coin_type** (*int* [https://docs.python.org/3/library/functions.html#int]) – if provided, look up the address for this coin type

Raises:

-

**InvalidName** – if name has invalid syntax

-

**ResolverNotFound** – if no resolver found for name

-

**UnsupportedFunction** – if the resolver does not support the `addr()`
function

setup_address(*name: str*, *address: ~eth_typing.evm.Address | ~eth_typing.evm.ChecksumAddress | ~eth_typing.evm.HexAddress = <object object>*, *coin_type: int | None = None*, *transact: TxParams | None = None*) → HexBytes [https://hexbytes.readthedocs.io/en/latest/hexbytes.html#hexbytes.main.HexBytes] | None [https://docs.python.org/3/library/constants.html#None]

Set up the name to point to the supplied address.
The sender of the transaction must own the name, or
its parent name.

Example: If the caller owns `parentname.eth` with no subdomains
and calls this method with `sub.parentname.eth`,
then `sub` will be created as part of this call.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name to set up

-

**address** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – name will point to this address, in checksum format.
If `None`, erase the record. If not specified, name will point
to the owner’s address.

-

**coin_type** (*int* [https://docs.python.org/3/library/functions.html#int]) – if provided, set up the address for this coin type

-

**transact** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – the transaction configuration, like in
`send_transaction()`

Raises:

-

**InvalidName** – if `name` has invalid syntax

-

**UnauthorizedError** – if `'from'` in transact does not own name

name(*address: ChecksumAddress*) → str [https://docs.python.org/3/library/stdtypes.html#str] | None [https://docs.python.org/3/library/constants.html#None]

Look up the name that the address points to, using a
reverse lookup. Reverse lookup is opt-in for name owners.

Parameters:

**address** (*hex-string*)

setup_name(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *address: ChecksumAddress | None [https://docs.python.org/3/library/constants.html#None] = None*, *transact: TxParams | None [https://docs.python.org/3/library/constants.html#None] = None*) → HexBytes [https://hexbytes.readthedocs.io/en/latest/hexbytes.html#hexbytes.main.HexBytes]

Set up the address for reverse lookup, aka “caller ID”.
After successful setup, the method `name()` will return
name when supplied with address.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name that address will point to

-

**address** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – address to set up, in checksum format

-

**transact** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – the transaction configuration, like in
`send_transaction()`

Raises:

-

**AddressMismatch** – if the name does not already point to the address

-

**InvalidName** – if name has invalid syntax

-

**UnauthorizedError** – if `'from'` in transact does not own name

-

**UnownedName** – if no one owns name

owner(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*) → ChecksumAddress

Get the owner of a name. Note that this may be different from the
deed holder in the ‘.eth’ registrar. Learn more about the difference
between deed and name ownership in the ENS Managing Ownership docs [http://docs.ens.domains/en/latest/userguide.html#managing-ownership]

Parameters:

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name to look up

Returns:

owner address

Return type:

str [https://docs.python.org/3/library/stdtypes.html#str]

setup_owner(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *new_owner: ChecksumAddress = None*, *transact: TxParams | None [https://docs.python.org/3/library/constants.html#None] = None*) → ChecksumAddress | None [https://docs.python.org/3/library/constants.html#None]

Set the owner of the supplied name to new_owner.

For typical scenarios, you’ll never need to call this method directly,
simply call `setup_name()` or `setup_address()`. This method does *not*
set up the name to point to an address.

If new_owner is not supplied, then this will assume you
want the same owner as the parent domain.

If the caller owns `parentname.eth` with no subdomains
and calls this method with `sub.parentname.eth`,
then `sub` will be created as part of this call.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name to set up

-

**new_owner** – account that will own name. If `None`, set owner to
empty addr. If not specified, name will point to the parent domain
owner’s address.

-

**transact** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – the transaction configuration, like in
`send_transaction()`

Raises:

-

**InvalidName** – if name has invalid syntax

-

**UnauthorizedError** – if `'from'` in transact does not own name

Returns:

the new owner’s address

resolver(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*) → Contract | None [https://docs.python.org/3/library/constants.html#None]

Get the resolver for an ENS name.

Parameters:

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – The ENS name

get_text(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *key: str [https://docs.python.org/3/library/stdtypes.html#str]*) → str [https://docs.python.org/3/library/stdtypes.html#str]

Get the value of a text record by key from an ENS name.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name to look up

-

**key** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name’s text record key

Returns:

ENS name’s text record value

Return type:

str [https://docs.python.org/3/library/stdtypes.html#str]

Raises:

-

**UnsupportedFunction** – If the resolver does not support
the “0x59d1d43c” interface id

-

**ResolverNotFound** – If no resolver is found for the provided name

set_text(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *key: str [https://docs.python.org/3/library/stdtypes.html#str]*, *value: str [https://docs.python.org/3/library/stdtypes.html#str]*, *transact: TxParams = None*) → HexBytes [https://hexbytes.readthedocs.io/en/latest/hexbytes.html#hexbytes.main.HexBytes]

Set the value of a text record of an ENS name.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name

-

**key** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – Name of the attribute to set

-

**value** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – Value to set the attribute to

-

**transact** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – The transaction configuration, like in
`send_transaction()`

Returns:

Transaction hash

Return type:

HexBytes

Raises:

-

**UnsupportedFunction** – If the resolver does not support
the “0x59d1d43c” interface id

-

**ResolverNotFound** – If no resolver is found for the provided name

## ens.async_ens module

*class*ens.async_ens.AsyncENS(*provider: AsyncBaseProvider | None [https://docs.python.org/3/library/constants.html#None] = None*, *addr: ChecksumAddress | None [https://docs.python.org/3/library/constants.html#None] = None*, *middleware: Sequence [https://docs.python.org/3/library/typing.html#typing.Sequence][tuple [https://docs.python.org/3/library/stdtypes.html#tuple][Middleware, str [https://docs.python.org/3/library/stdtypes.html#str]]] | None [https://docs.python.org/3/library/constants.html#None] = None*)

Quick access to common Ethereum Name Service functions,
like getting the address for a name.

Unless otherwise specified, all addresses are assumed to be a str in
checksum format [https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md],  # blocklint: pragma # noqa: E501
like: `"0x314159265dD8dbb310642f98f50C066173C1259b"`

*classmethod*from_web3(*w3: AsyncWeb3[Any]*, *addr: ChecksumAddress = None*) → AsyncENS

Generate an AsyncENS instance with web3

Parameters:

-

**w3** (*web3.Web3*) – to infer connection information

-

**addr** (*hex-string*) – the address of the ENS registry on-chain. If not
provided, defaults to the mainnet ENS registry address.

*async*address(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *coin_type: int [https://docs.python.org/3/library/functions.html#int] | None [https://docs.python.org/3/library/constants.html#None] = None*) → ChecksumAddress | None [https://docs.python.org/3/library/constants.html#None]

Look up the Ethereum address that name currently points to.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – an ENS name to look up

-

**coin_type** (*int* [https://docs.python.org/3/library/functions.html#int]) – if provided, look up the address for this coin type

Raises:

**InvalidName** – if name has invalid syntax

*async*setup_address(*name: str*, *address: ~eth_typing.evm.Address | ~eth_typing.evm.ChecksumAddress | ~eth_typing.evm.HexAddress = <object object>*, *coin_type: int | None = None*, *transact: TxParams | None = None*) → HexBytes [https://hexbytes.readthedocs.io/en/latest/hexbytes.html#hexbytes.main.HexBytes] | None [https://docs.python.org/3/library/constants.html#None]

Set up the name to point to the supplied address.
The sender of the transaction must own the name, or
its parent name.

Example: If the caller owns `parentname.eth` with no subdomains
and calls this method with `sub.parentname.eth`,
then `sub` will be created as part of this call.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name to set up

-

**address** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – name will point to this address, in checksum format.
If `None`, erase the record. If not specified, name will point
to the owner’s address.

-

**coin_type** (*int* [https://docs.python.org/3/library/functions.html#int]) – if provided, set up the address for this coin type

-

**transact** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – the transaction configuration, like in
`send_transaction()`

Raises:

-

**InvalidName** – if `name` has invalid syntax

-

**UnauthorizedError** – if `'from'` in transact does not own name

*async*name(*address: ChecksumAddress*) → str [https://docs.python.org/3/library/stdtypes.html#str] | None [https://docs.python.org/3/library/constants.html#None]

Look up the name that the address points to, using a
reverse lookup. Reverse lookup is opt-in for name owners.

Parameters:

**address** (*hex-string*)

*async*setup_name(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *address: ChecksumAddress | None [https://docs.python.org/3/library/constants.html#None] = None*, *transact: TxParams | None [https://docs.python.org/3/library/constants.html#None] = None*) → HexBytes [https://hexbytes.readthedocs.io/en/latest/hexbytes.html#hexbytes.main.HexBytes]

Set up the address for reverse lookup, aka “caller ID”.
After successful setup, the method `name()` will return
name when supplied with address.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name that address will point to

-

**address** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – address to set up, in checksum format

-

**transact** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – the transaction configuration, like in
`send_transaction()`

Raises:

-

**AddressMismatch** – if the name does not already point to the address

-

**InvalidName** – if name has invalid syntax

-

**UnauthorizedError** – if `'from'` in transact does not own name

-

**UnownedName** – if no one owns name

*async*owner(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*) → ChecksumAddress

Get the owner of a name. Note that this may be different from the
deed holder in the ‘.eth’ registrar. Learn more about the difference
between deed and name ownership in the ENS Managing Ownership docs [http://docs.ens.domains/en/latest/userguide.html#managing-ownership]

Parameters:

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name to look up

Returns:

owner address

Return type:

str [https://docs.python.org/3/library/stdtypes.html#str]

*async*setup_owner(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *new_owner: ChecksumAddress = None*, *transact: TxParams | None [https://docs.python.org/3/library/constants.html#None] = None*) → ChecksumAddress | None [https://docs.python.org/3/library/constants.html#None]

Set the owner of the supplied name to new_owner.

For typical scenarios, you’ll never need to call this method directly,
simply call `setup_name()` or `setup_address()`. This method does *not*
set up the name to point to an address.

If new_owner is not supplied, then this will assume you
want the same owner as the parent domain.

If the caller owns `parentname.eth` with no subdomains
and calls this method with `sub.parentname.eth`,
then `sub` will be created as part of this call.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name to set up

-

**new_owner** – account that will own name. If `None`,
set owner to empty addr.  If not specified, name will point
to the parent domain owner’s address.

-

**transact** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – the transaction configuration, like in
`send_transaction()`

Raises:

-

**InvalidName** – if name has invalid syntax

-

**UnauthorizedError** – if `'from'` in transact does not own name

Returns:

the new owner’s address

*async*resolver(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*) → AsyncContract | None [https://docs.python.org/3/library/constants.html#None]

Get the resolver for an ENS name.

Parameters:

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – The ENS name

*async*get_text(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *key: str [https://docs.python.org/3/library/stdtypes.html#str]*) → str [https://docs.python.org/3/library/stdtypes.html#str]

Get the value of a text record by key from an ENS name.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name to look up

-

**key** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name’s text record key

Returns:

ENS name’s text record value

Return type:

str [https://docs.python.org/3/library/stdtypes.html#str]

Raises:

-

**UnsupportedFunction** – If the resolver does not support
the “0x59d1d43c” interface id

-

**ResolverNotFound** – If no resolver is found for the provided name

*async*set_text(*name: str [https://docs.python.org/3/library/stdtypes.html#str]*, *key: str [https://docs.python.org/3/library/stdtypes.html#str]*, *value: str [https://docs.python.org/3/library/stdtypes.html#str]*, *transact: TxParams = None*) → HexBytes [https://hexbytes.readthedocs.io/en/latest/hexbytes.html#hexbytes.main.HexBytes]

Set the value of a text record of an ENS name.

Parameters:

-

**name** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – ENS name

-

**key** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – The name of the attribute to set

-

**value** (*str* [https://docs.python.org/3/library/stdtypes.html#str]) – Value to set the attribute to

-

**transact** (*dict* [https://docs.python.org/3/library/stdtypes.html#dict]) – The transaction configuration, like in
`send_transaction()`

Returns:

Transaction hash

Return type:

HexBytes

Raises:

-

**UnsupportedFunction** – If the resolver does not support
the “0x59d1d43c” interface id

-

**ResolverNotFound** – If no resolver is found for the provided name

## ens.exceptions module

*exception*ens.exceptions.ENSException

Bases: `Exception` [https://docs.python.org/3/library/exceptions.html#Exception]

Base class for all ENS Errors

*exception*ens.exceptions.ENSValueError

Bases: `ENSException`, `ValueError` [https://docs.python.org/3/library/exceptions.html#ValueError]

An ENS exception wrapper for ValueError, for better control over
exception handling.

*exception*ens.exceptions.ENSTypeError

Bases: `ENSException`, `TypeError` [https://docs.python.org/3/library/exceptions.html#TypeError]

An ENS exception wrapper for TypeError, for better control over
exception handling.

*exception*ens.exceptions.AddressMismatch

Bases: `ENSException`

In order to set up reverse resolution correctly, the ENS name should first
point to the address. This exception is raised if the name does
not currently point to the address.

*exception*ens.exceptions.InvalidName

Bases: `IDNAError`, `ENSException`

Raised if the provided name does not meet the normalization
standards specified in ENSIP-15
<https://docs.ens.domains/ens-improvement-proposals/ensip-15-normalization-standard>`_.

*exception*ens.exceptions.UnauthorizedError

Bases: `ENSException`

Raised if the sending account is not the owner of the name
you are trying to modify. Make sure to set `from` in the
`transact` keyword argument to the owner of the name.

*exception*ens.exceptions.UnownedName

Bases: `ENSException`

Raised if you are trying to modify a name that no one owns.

If working on a subdomain, make sure the subdomain gets created
first with `setup_address()`.

*exception*ens.exceptions.ResolverNotFound

Bases: `ENSException`

Raised if no resolver was found for the name you are trying to resolve.

*exception*ens.exceptions.UnsupportedFunction

Bases: `ENSException`

Raised if a resolver does not support a particular method.

*exception*ens.exceptions.BidTooLow

Bases: `ENSException`

Raised if you bid less than the minimum amount

*exception*ens.exceptions.InvalidBidHash

Bases: `ENSException`

Raised if you supply incorrect data to generate the bid hash.

*exception*ens.exceptions.InvalidLabel

Bases: `ENSException`

Raised if you supply an invalid label

*exception*ens.exceptions.OversizeTransaction

Bases: `ENSException`

Raised if a transaction you are trying to create would cost so
much gas that it could not fit in a block.

For example: when you try to start too many auctions at once.

*exception*ens.exceptions.UnderfundedBid

Bases: `ENSException`

Raised if you send less wei with your bid than you declared
as your intent to bid.

*exception*ens.exceptions.ENSValidationError

Bases: `ENSException`

Raised if there is a validation error
