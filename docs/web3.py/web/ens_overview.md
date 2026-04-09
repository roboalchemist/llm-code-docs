# Ethereum Name Service (ENS)

The Ethereum Name Service (ENS) is analogous to the Domain Name Service. It
enables users and developers to use human-friendly names in place of error-prone
hexadecimal addresses, content hashes, and more.

The `ens` module is included with web3.py. It provides an interface to look up
domains and addresses, add resolver records, or get and set metadata.

## Setup

Create an `ENS` object (named `ns` below) in one of three ways:

-

Automatic detection

-

Specify an instance of a provider

-

From an existing `web3.Web3` object

```
# automatic detection
from ens.auto import ns

# or, with a provider
from web3 import IPCProvider
from ens import ENS

provider = IPCProvider(...)
ns = ENS(provider)

# or, with a w3 instance
# Note: This inherits the w3 middleware from the w3 instance and adds a stalecheck middleware to the middleware onion.
# It also inherits the provider and codec from the w3 instance, as well as the ``strict_bytes_type_checking`` flag value.
from ens import ENS
w3 = Web3(...)
ns = ENS.from_web3(w3)

```
