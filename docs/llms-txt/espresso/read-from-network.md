# Source: https://docs.espressosys.com/network/concepts/read-from-network.md

# Reading from the Espresso Network

Rollups integrated with Espresso gain access to fast and trust-minimized transaction confirmations. Applications and users do not need to wait for parent chain finality or rely and trust centralized sequencers to determine whether a transaction is final. Instead, they can use Espresso’s confirmation guarantees to safely treat transactions as finalized much earlier.

To enable this experience, integrated rollups must run a modified full node capable of reading Espresso confirmations and producing finalized state based on them. We call these modified nodes **Caffeinated Nodes**, or simply **Caff Nodes**. A Caff Node behaves like a standard full node of the chain, but with additional logic to consume finalized rollup blocks from the Espresso Network. From the perspective of a developer or application, a Caff Node exposes the same familiar RPC interface.

> It is important to note that Caff Nodes are functionally identical to operating a standard full node. This means running a Caff Node is as simple as running a full node with certain Espresso flags enabled in the node config so that it can read data from the Espresso Network. This also implies that Caff Nodes follow the standard [JSON RPC API](https://ethereum.org/developers/docs/apis/json-rpc/) and work seamlessly with existing tools and libraries with no extra code needed to integrate.

### Caff Nodes in the Rollup Architecture

In a traditional rollup architecture (without Espresso), the rollup sequencer is responsible for collecting, ordering, and publishing transactions. End users and applications can either:

* Rely on the sequencer for a *soft* confirmation, which is fast but requires trusting the sequencer, or
* Wait for the parent chain finality, which provides strong security guarantees but introduces significant latency.

Espresso removes this tradeoff. By integrating with Espresso, a rollup can achieve fast confirmations without requiring trust in a centralized sequencer.

Once Espresso confirms a transaction or rollup block, the Caff Node derives the resulting chain state and makes it available via the standard RPC — just as if the transaction had already finalized on the parent chain. For developers, this means no change to existing application integrations: the node behaves the same, but finality is faster and trust-minimized.\
\
For example, if Laura deposits **10 ETH** into an exchange on a chain integrated with Espresso, the exchange can safely treat the transaction as final as soon as Espresso confirms it. From that point on, there is no risk of the transaction being reordered. The front end can confidently reflect the deposit without waiting for L1 inclusion. This can happen naturally by having the exchange reading from the Caff Node RPC.

### Using the Caff Nodes

Functionally, a Caff Node behaves exactly like a standard full node — it exposes the same RPC interface and methods. The key difference is in how it determines the state of the chain.

* Get block by block number (on Rari testnet):

```bash
curl -X POST https://rari.caff.testnet.espresso.network \
    -H "Content-Type: application/json" \
    -d '{
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": ["<BLOCK-NUMBER>", true],
        "id": 1
    }'
```

Where `<BLOCK-NUMBER>` is the number of the block in hexadecimal.

* Get transaction by transaction hash (on Rari testnet):

```bash
curl -X POST https://rari.caff.testnet.espresso.network \
    -H "Content-Type: application/json" \
    -d '{
        "jsonrpc":"2.0",
        "method":"eth_getTransactionByHash",
        "params":["<TRANSACTION-HASH>"],
        "id":1
    }'
```

Where `<TRANSACTION-HASH>` is the hash of the transaction (prefixed with `0x`).
