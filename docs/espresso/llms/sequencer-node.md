# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/sequencer-node.md

# Espresso Node

An *Espresso node* is a participant in the HotShot consensus protocol which also makes available some services to support L2 clients. The Espresso node is L2 agnostic: it does not provide services specifically tailored to any particular L2. It merely exposes all available information about HotShot and the log of blocks which have been sequenced. Any L2 may query this information and interpret the blocks according to its own execution rules in order to implement a prover, executor, RPC service, etc.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-128398b48bdb67a03cfa3c2ee0295a8225f9f13c%2Fimage%20(12).png?alt=media" alt=""><figcaption><p>Internal components of an Espresso node and their possible usage by various participants in an L2</p></figcaption></figure>

The main internal components of the Espresso node and their respective functions are:

* **HotShot node:** The component which actually runs consensus and communicates with other nodes.
* **HotShot query service:** The query service maintains a database containing the history and current state of HotShot, including all committed blocks and QCs, consensus-specific data like view numbers and stake tables, and status information like validator uptime. It populates this data using events provided by the HotShot validator and provides a REST API for querying the data. There is also a WebSockets-based API which allows clients to subscribe to notifications when new blocks and QCs are produced. The query service does not provide any L2-specific information. The contents of the blocks it provides are the generic transactions that HotShot itself understands.
* [**Submit API**](https://docs.espressosys.com/network/api-reference/espresso-api/submit-api)**:** The Espresso node also provides an interface allowing clients to submit transactions to the HotShot mempool. It takes as input a transaction serialized into bytes and an L2 identifier, and it wraps these into HotShot's generic transaction type.
