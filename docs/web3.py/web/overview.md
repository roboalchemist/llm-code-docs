# Overview

The purpose of this page is to give you a sense of everything web3.py can do
and to serve as a quick reference guide. You’ll find a summary of each feature
with links to learn more.

## Configuration

After installing web3.py (via `pip install web3`), you’ll need to configure
a provider endpoint and any middleware you want to use beyond the defaults.

### Providers

Providers are how web3.py connects to a blockchain. The library comes with the
following built-in providers:

-

`HTTPProvider` for connecting to http and https based JSON-RPC servers.

-

`IPCProvider` for connecting to ipc socket based JSON-RPC servers.

-

`AsyncHTTPProvider` for connecting to http and https based JSON-RPC servers asynchronously.

-

`AsyncIPCProvider` for connecting to ipc socket based JSON-RPC servers asynchronously via a persistent connection.

-

`WebSocketProvider` for connecting to websocket based JSON-RPC servers asynchronously via a persistent connection.

#### Examples

```
>>> from web3 import Web3, AsyncWeb3

# IPCProvider:
>>> w3 = Web3(Web3.IPCProvider('./path/to/filename.ipc'))
>>> w3.is_connected()
True

# HTTPProvider:
>>> w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
>>> w3.is_connected()
True

# AsyncHTTPProvider:
>>> w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider('http://127.0.0.1:8545'))
>>> await w3.is_connected()
True

# -- Persistent Connection Providers -- #

# WebSocketProvider:
>>> w3 = await AsyncWeb3(AsyncWeb3.WebSocketProvider('ws://127.0.0.1:8546'))
>>> await w3.is_connected()
True

# AsyncIPCProvider
>>> w3 = await AsyncWeb3(AsyncWeb3.AsyncIPCProvider('./path/to/filename.ipc'))
>>> await w3.is_connected()
True

```
