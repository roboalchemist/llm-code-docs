# Geth API

The `web3.geth` object exposes modules that enable you to interact with the JSON-RPC endpoints supported by Geth [https://github.com/ethereum/go-ethereum/wiki/Management-APIs] that are not defined in the standard set of Ethereum JSONRPC endpoints according to EIP 1474 [https://github.com/ethereum/EIPs/pull/1474].

## GethAdmin API

The following methods are available on the `web3.geth.admin` namespace.

The `web3.geth.admin` object exposes methods to interact with the RPC APIs under the
`admin_` namespace that are supported by the Geth client.

web3.geth.admin.datadir()

-

Delegates to `admin_datadir` RPC Method

Returns the system path of the node’s data directory.

```
>>> web3.geth.admin.datadir()
'/Users/snakecharmers/Library/Ethereum'

```
