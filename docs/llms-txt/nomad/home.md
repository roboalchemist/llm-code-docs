# Source: https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home.md

# Home

The Home ([contract code](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol)) is the core contract deployed on all chains that wish to send outbound messages. It serves as the "outbox" for *all* applications and users sending messages from the chain it is deployed on.

Nomad creates an authenticated data structure via the Home, and relays updates to that data structure on any number of [Replicas](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/replica) deployed on destination chains. As a result, the Home and all Replicas will agree on the state of the data structure. By embedding data ("messages") in this data structure we can propagate it between chains with a high degree of confidence.

### Data Structures

#### Message Tree

As described above, the primary data structure is the message tree. The Home enforces rules on the creation of this data structure. In the current design, this data structure is a [sparse Merkle tree](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/libs/Merkle.sol) based on the design used in the Eth2 deposit contract. This tree commits to the vector of all previous messages.&#x20;

The Home contract enforces an addressing and message scheme for messages and calculates the tree root. This root is what is relayed to Replicas.

#### Queue of Roots

The Home also maintains a queue of roots (one for each enqueued message). The Home must maintain a list of roots in order to provide data availability. By doing so, it makes it trivial to prove fraud.

### Updates on the Home

The Home permissions an [Updater](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater) (as elected by [governance](https://docs.nomad.xyz/operational-security/governance)) that must attest to the state of the message tree. The updater places a bond on the Home and is required to periodically sign updates, `U`. Each update contains the root from the previous update `U_prev`, and a new root `U_new`.

Any [Watcher](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) can flag fraud on the Home chain if it sees two conflicting updates (`U` and `U'` where `U_i_prev == U_i'_prev && U_i_new != U_i'_new` or a single update where `U_new` is not an element of the queue. The new root MUST be a member of the queue. E.g a list of updates `U_1`...`U_i` should follow the form \[(A, B), (B, C), (C, D)...].

Semantically, updates represent a batch commitment to the messages between the two roots. Updates contain one or more messages that ought to be propagated to Replicas. Updates may occur at any frequency, as often as once per message. Because updates are chain-independent, any Home's update may be presented to any Replica. In other words, data availability of signed updates is guaranteed by the Home contract deployed on each sending chain.
