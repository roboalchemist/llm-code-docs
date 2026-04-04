# Source: https://docs.espressosys.com/network/appendix/interacting-with-l1/trustless-sync.md

# Trustless Sync

One of the main reasons to use blockchains is to decentralize trust. However, the current Ethereum ecosystem often compromises on this principle by using trusted query services like [Infura](https://www.infura.io/) for clients to access the blockchain. This trades off trustlessness for convenience and scalability, since a client that trusts a query service does not need to verify any Ethereum block data.

However, Ethereum's switch to proof-of-stake and its rollup-centric roadmap offer the potential to break out of this tradeoff, enabling efficient and user-friendly clients that retain decentralized trust. When rollups post their state updates to Ethereum or a similar L1, each L1 validator independently validates the state transition for the rollup by executing the rollup's smart contract. This means that any user who trusts the collective L1 validator set can quickly sync with the latest state of the rollup simply by reading a recent, verified state update from the L1 state.

Of course, this only pushes the problem of fast, trustless sync to the L1. This is nonetheless a substantial improvement. In the case of Ethereum, the proof-of-stake consensus protocol and the fixed block time enable the creation of L1 light clients which sync far faster than real time. For instance, [Helios](https://github.com/a16z/helios) is an Ethereum light client which manages trustless sync in only 2 seconds. By verifying HotShot and rollup states on Ethereum, any such Ethereum client can be turned into a client for any rollup merely by syncing with Ethereum and then reading rollup state from the appropriate smart contract.
