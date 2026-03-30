# Source: https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging.md

# Cross-chain Messaging

Cross-chain messaging is a subset of [the oracle problem](https://blog.chain.link/what-is-the-blockchain-oracle-problem/), where the provenance of the desired data is *another* blockchain. In order to push data from one chain into another, we have no choice but to rely on someone in the real world to verify and relay this data. The goal of all cross-chain messaging systems is, ostensibly, to reduce the trust assumptions in [this verification process](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/background-on-verification).

Nomad achieves this by leveraging an [optimistic mechanism](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification) that relies on an off-chain [Updater](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater) to attest to data, and [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) to provide checks and balances. Each Updater is responsible for a [Home contract](#the-home-contract) that broadcasts uni-directionally to any number of [Replica contracts](#replica-contracts), each corresponding to a destination chain.

This section will cover how Nomad channels work and how they are secured.

## Nomad Channels

All cross-chain messaging channels are uni-directional. As mentioned above, chains cannot pull data from or push data out to any external system.&#x20;

To facilitate secure two-way communications between chains, we need to establish dual simplex channels, meaning two one-way channels that form a composite bi-directional channel.

### The Home Contract

Nomad does this by following a uni-directional [broadcast model](#broadcast-channels), where each sending chain is the source of truth, and contains a Nomad [Home contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) where messages are enqueued.

Messages from all applications are committed in a Merkle tree (the “message tree”). Each new message is stored as a leaf, with the root of the tree serving as an accumulator. New roots are calculated upon each message insertion, and inserted into a queue that tracks all roots, current and historic.

Periodically, the Updater signs an `update`, which acts as an attestation. Updates commit to the previous root and a new root, and are relayed to Replica contracts corresponding to the Home. Updates can happen as frequently as new roots are generated, or be batched to reduce costs.

### Replica Contracts

Every destination chain that wishes to replicate the state and receive messages from a given Home contract must maintain a [Replica contract](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Replica.sol), corresponding to that Home.

Any chain can maintain a Replica, which holds knowledge of the corresponding Home's Updater and the current root. Signed updates are held by the Replica, and accepted after a timeout (the optimistic dispute window).

The Replica effectively replays a series of updates to reach the same root as the Home chain. Because the root commits to the message tree, once the root has been transmitted and settled, honest messages can be proven against the root.

### Broadcast Channels&#x20;

Unlike other cross-chain messaging channels which facilitate 1-to-1 comms between chains, Nomad by default allows for 1-to-n messaging. This is because Nomad follows a single-producer, multi-consumer model.&#x20;

Each Home contract acts as a broadcast channel, whose corresponding Replicas can receive updates from without any bespoke logic.

Because the messages need not be coupled with the destination, we anticipate novel use cases that leverage this pattern and enable quick one-to-many comms between blockchains.
