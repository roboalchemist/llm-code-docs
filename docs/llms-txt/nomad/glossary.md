# Source: https://docs.nomad.xyz/resources/glossary.md

# Glossary

### **General Terminology**

Bridge

> A piece of technology that connects one blockchain to another. It enables the flow of value and information across what would otherwise be siloed sets of data on different blockchains.

xApp

> A cross-chain application (pronounced "zapp").  Nomad does the heavy lifting of secure cross-chain messaging so that you don't have to! Learn how you can bring your application to the multi-chain future in our [Developer Quickstart Guide](https://docs.nomad.xyz/developers).

Channel

> The line of communication between two blockchains. Nomad enables xApps to pass messages via these channels. These messages consist of arbitrary byte data, which are encoded with application-specific instructions. They are decoded on the receiving chain and can even be used to call functions.

Token Representations

> In a lock/mint bridge (like Nomad's Token Bridge), when an asset is sent cross-chain, the original is locked and a representation of that asset is minted on the destination chain. Nomad representations are referred to as "mad" assets (e.g. madUSDC). A token that resides on its original chain is referred to as a "native" asset.

Merkle Tree (or Message Tree)

> A data structure that encodes data efficiently and securely. Used by the Home, Updater and Watcher to verify message authenticity.

### **Nomad-specific Terminology**

Domain

> The Nomad-specific id associated with a chain.

Core

> Reference to the core Nomad protocol, or the messaging channels implemented by the core protocol.

Token Bridge

> A xApp built and maintained by the Nomad team which allows users to send ERC-20 tokens between supported chains.

Optimistic Timeout Window/Period

> The time period during which a Watcher can report fraud (if any). Currently 30 minutes for each chain. Nomad's design makes it easy to detect and report fraud, so it includes a much shorter window compared to other optimistic models.

Processing or Claiming

> The final step of dispatching a message to the recipient. Processing gas fees are subsidized on most chains. However, due to high gas fees, when sending to Ethereum users are required to submit an additional transaction to process messages or token transfers.

#### Architecture

Home

> The on-chain contract that is responsible for managing production of the message tree and holding custody of the updater bond.

Replica

> The on-chain contract that is responsible for managing optimistic replication and dispatching messages to end recipients. There is a Replica responsible for each remote chain.

Updater

> The off-chain agent responsible for signing attestations of new message roots.

Watcher

> The off-chain agent responsible for reporting faulty attestations. Note that Nomad needs only *one* honest watcher to maintain security of the entire system, rather that relying on custodians or external validators. This allows Nomad to be decentralized and *highly* secure.

Relayer

> The off-chain agent which forwards updates from the home to one or more replicas.

Processor

> The off-chain agent which proves the validity of pending messages and sends them to end recipients.
