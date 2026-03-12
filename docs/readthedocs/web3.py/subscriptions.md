# Event Subscriptions

Most Ethereum clients include `eth_subscribe` support, allowing you to listen for specific events as they occur. This applies to a limited set of events: new block headers, the syncing status of a node, new pending transactions, and emitted logs from smart contracts.

Warning

Subscriptions require a persistent socket connection between you and the Ethereum client. For that reason, you must use web3.py’s `WebSocketProvider` or `AsyncIPCProvider` to utilize subscriptions. As it is the more common of the two, examples in this guide will leverage the `WebSocketProvider`.
