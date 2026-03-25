# Formatters

Formatters are a core part of web3.py’s data transformation pipeline. They convert
data between Python-friendly formats and the hexadecimal formats required by the
Ethereum JSON-RPC specification. This page explains how formatters work, what the
default formatters do, and how to customize them.

Note

For a deep dive into how requests flow through web3.py, including formatters,
see the excellent blog post:
Web3.py Internals: JSON-RPC Round Trips [https://snakecharmers.ethereum.org/web3py-internals-json-rpc-round-trips/]
