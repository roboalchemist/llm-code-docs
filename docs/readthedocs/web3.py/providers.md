# Providers

Using Ethereum requires access to an Ethereum node. If you have the means, you’re
encouraged to run your own node [https://ethereum.org/en/developers/docs/nodes-and-clients/run-a-node/]. (Note that you do not need to stake ether to
run a node.) If you’re unable to run your own node, you can use a remote node [https://ethereum.org/en/developers/docs/nodes-and-clients/nodes-as-a-service/].

Once you have access to a node, you can connect to it using a **provider**.
Providers generate JSON-RPC [https://ethereum.org/en/developers/docs/apis/json-rpc/] requests and return the response. This is done by submitting
the request to an HTTP, WebSocket, or IPC socket-based server.

Note

web3.py supports one provider per instance. If you have an advanced use case
that requires multiple providers, create and configure a new web3 instance
per connection.
