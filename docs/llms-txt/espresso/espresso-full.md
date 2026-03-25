# Espresso Documentation

Source: https://docs.espressosys.com/llms-full.txt

---

# INTRODUCTION

Espresso is a high-performance base layer for rollups, making L2 transactions safe, fast, and seamless for users. Espresso is trusted by leading teams including Oﬀchain Labs (Arbitrum), Polygon, ApeChain, Cartesi, RARI Chain, Celo.

L2s and rollups that use Espresso as a decentralized base layer benefit from industry-leading speed in finalizing transactions. The confirmations that Espresso provides underpin cross-chain applications that can tap into liquidity and users of all connected Espresso-chains.

### Use Cases

Like any base layer or L1, Espresso can be used in a variety of ways by the L2s that leverage it. These use cases include fast finality and / or data availability. Unlike some other base layers, Espresso can be used as a standalone L1 or in tandem with another settlement layer like Ethereum.

Espresso is used by layer-2 chains to upgrade their security and UX.

● Security : Espresso is a decentralized consensus layer designed to replace reliance on vulnerable centralized components of layer-2 chains (e.g. bridge reliance on centralized sequencer preconfirmations).

● Interoperability : Espresso is designed to support near-real-time communication between its integrated chains and a diverse array of financial systems, including both traditional financial databases as well as other blockchain-based protocols and products.

● Performance : Espresso’s high-throughput system is designed with the future in mind: chains that integrate Espresso can have confidence that as demand for their blockspace expands, their costs won’t need to grow at the same rate.

### Get Started

#### Rollup Operators

Espresso is currently integrated with the Arbitrum Nitro stack, Cartesi's Linux-based stack, and will release its OP Stack integration by the end of 2025.

[Launch an Arbitrum Orbit chain with Espresso](https://docs.espressosys.com/network/guides/rollup-developers/nitro/deploy-a-new-orbit-chain) :arrow\_right:

[Integrate an existing Orbit chain](https://docs.espressosys.com/network/guides/rollup-developers/nitro/migrate-orbit-chains-to-espresso) :arrow\_right:

#### App & Protocol Builders

Read from Espresso to build native cross-chain apps or gain faster, safer interoperability with Espresso-integrated chains.

[Reading from the Espresso Network](https://docs.espressosys.com/network/concepts/read-from-network) :arrow\_right:

#### Node Operators

Run nodes that power Espresso’s consensus and data availability.

[Run an Espresso Node](https://docs.espressosys.com/network/guides/node-operators/running-a-sequencer-node) :arrow\_right:


# Using Espresso

How Espresso can be used for fast finality, data availability and decentralized sequencing

The Espresso Network has been designed with multiple use cases in mind. We have seen that developers are best able to innovate when they have flexibility around designing their stack.

Espresso offers several benefits for chain operators and their developers to choose from:

* Fast finality: All chains that leverage Espresso benefit from fast, reliable [confirmations](https://hackmd.io/@EspressoSystems/bft-and-proposer-promised-preconfirmations)—replacing the need for users, bridges, and beyond to depend on preconfirmations that come from centralized sequencers.
* Data availability: All chains using Espresso also benefit from highly efficient [data availability](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu) offered by the Espresso Network. However, many of the chains that are using Espresso also choose to leverage another form of DA, such as EigenDA, Celestia, Avail, or Ethereum itself. We have designed Espresso to respect and to be additively compatible with these choices.
* Decentralized sequencing: Rollups can use Espresso to set up their own decentralized sequencer, gaining better censorship resistance and liveness guarantees without sacrificing on latency, while using their own token to elect their sequencer set.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-429159b1a8ae5ddcba95b585a6f2d43e206c4195%2FModularity%20Scratch%20(6).png?alt=media" alt=""><figcaption></figcaption></figure>

A few examples of how Ethereum rollups can use the Espresso network include:

* A standard rollup or validium that uses the L1 or an alternative data availability solution, leverages its own centralized sequencer, and settles to Ethereum may leverage Espresso for confirmations.
* A based rollup that uses Ethereum for DA, relies on the Ethereum proposer for sequencing, and looks to the L1 for settlement may also use Espresso for fast, reliable confirmations.
* A validium that leverages its own centralized sequencer can use Espresso for data availability and also for more robust confirmations than the preconfirmations that its sequencer could offer.
* A rollup or validium that wants to decentralize its sequencing without using the L1 proposer may use the Espresso leader as its sequencer for any given round and use Espresso for confirmations – while using its own choice of data availability.
* A rollup that uses Espresso for DA, sequencing, and confirmations is what we like to call a caffeinated chain.

While we only cover Ethereum rollups here, this also applies to sovereign rollups and beyond.


# Rollup Architecture

Espresso is the base layer for rollups. In order to understand what Espresso does and what benefits it brings, you must understand how rollups work at the high level.

### What is a Rollup?

A rollup is a type of blockchain that runs on top of another blockchain (called the parent chain or settlement layer). Instead of executing all transactions directly on the parent chain, the rollup executes transactions off-chain and then posts a compressed record of those transactions back to the parent.

This approach brings two key benefits:

* Scalability – rollups process many more transactions than the parent chain could handle on its own.
* Security – rollups inherit security from their parent chain, since all rollup data is anchored there.

There are two main types of rollups:

* Optimistic Rollups – batches are assumed valid by default, but can be challenged during a fraud window (typically \~7 days). Examples: Optimism, Arbitrum.
* ZK Rollups – each batch includes a cryptographic proof (a zero-knowledge proof) showing that the transactions were executed correctly. No challenge period is required. Examples: zkSync, Starknet.

### Finality vs. Settlement

These two concepts are central in the rollup ecosystem, but they’re often confused or misused.

#### Finality

Finality means you can consider a transaction done and no longer subject to reversal. In most rollups, this happens when your transaction is included in a batch and that batch is posted to the parent chain (e.g., Ethereum).

With Espresso, you don’t need to wait for the batch to reach the parent chain. Espresso provides its own confirmations, **backed by BFT consensus**, so you can trust your transaction as final immediately, knowing it will eventually be included on the parent chain.

#### Settlement

Settlement is about proving correctness to the parent chain. Once a batch is posted, someone posts a corresponding state commitment, and there's typically a 7-day challenge window where anyone can submit a fraud proof if the state is incorrect.

Importantly, this does not affect rollup execution: the rollup itself won’t roll back or halt because of a fraud proof. The challenge process only ensures that the state recorded on the parent chain matches what the rollup actually computed.

### The Transaction Lifecycle in a Rollup

In a usual rollup (not integrated with Espresso), the transaction flow is:

**1. User submits transactions**

The user signs and sends a transaction to the rollup.

**2. Sequencer**

The sequencer collects transactions, orders them, and produces blocks quickly.

**3. Batch posting**

The sequencer (or a separate batch poster) sends batches of ordered transactions to the parent chain for security anchoring. **The transactions included in the batch are considered final**.

**4. Verification on parent chain**

* For optimistic rollups, batches can be challenged during a fraud proof period.
* For ZK rollups, batches include a ZK proof that is verified immediately.

**5. Settlement**

After the fraud period (optimistic) or proof verification (ZK), **the batch is considered settled** and secured by the parent chain.

### The Transaction Lifecycle in an Espresso-integrated Rollup

**1. User submits a transaction**

The user signs and sends a transaction to the rollup.

**2. Sequencer**

The chain's sequencer, produces blocks.

**3.1 Confirmations (powered by Espresso confirmations)**

Espresso finalizes the ordering of transactions. The Espresso Network produces a block containing the transaction and finalizes its position in the global order.

**3.2 Data Availability (optional)**

If Espresso is also used as a DA layer, the transaction data is stored and made retrievable by Espresso’s DA.

If not, DA comes from the rollup’s parent chain or another DA layer (e.g., Celestia, EigenDA).

**NOTE:** If you are using Espresso for confirmations, Espresso DA comes *for free*.

**4. Caff Node derives chain state**

Caff Nodes (which stand for Caffeinated Nodes), which are full nodes instrumeted to read from the Espresso Network, derive execution results and make them available through an RPC (the exact same RPC endpoints you would use in a standard EVM RPC). Applications can query Caff Nodes to know instantly whether a transaction is confirmed.

**6. Batch posting to parent chain**

A batch poster sends transactions to the parent chain, along with a proof that these transactions have been confirmed in Espresso.

**NOTE:** This proof can take the form of a ZK proof, a signature from secure hardware (TEE), or something else. The parent chain immediately verifies this proof before finalizing the batch.

**7. Parent chain verification**

* On an optimistic rollup, the batch is subject to a fraud-proof window.
* On a ZK rollup, the validity proof is checked immediately.

**8. Settlement**

Once the fraud period ends (optimistic) or proof verification passes (ZK), the batch is settled on the parent chain.

The Espresso confirmation obtained in step 4 remains consistent with this final state, **assuming no bugs in the Caff Node**.

### What Espresso Is vs. What Espresso Is Not

Espresso is designed to solve a very specific problem in the rollup stack: ordering and fast confirmations. It is not responsible for execution. Understanding this distinction is key to knowing what Espresso can (and cannot) guarantee for your application.

#### What Espresso Is: The Ordering Layer

Espresso provides a shared global ordering service through its HotShot consensus protocol.

* Espresso’s job is to make sure everyone agrees, within seconds, which transaction came first and what order they should be executed in.
* Once Espresso confirms an ordering, sequencers can’t retroactively change it. This prevents manipulation like censorship, or reorgs at the ordering layer.
* Apps can rely on Espresso for fast, secure provisional confirmations before finality on the parent chain (e.g., Ethereum).

#### What Espresso Is Not: The Execution Layer

Espresso does not execute transactions. Execution still happens on the rollup itself and ultimately settles on the parent chain (Ethereum).

* Espresso does not check whether a transaction is validly executed — that’s the job of the rollup’s execution environment.

### Security Assumptions

**- Ordering guarantees:** Espresso is guaranteed to provide consistent ordering, as long as at least two-thirds of the staked tokens are controlled by honest parties.

**- Execution finality:** The ultimate correctness of transaction execution and cross-chain asset movements still depends on rollup execution and L1 settlement.

**- Enforce Espresso confirmations:**: The rollup's inbox has to correctly enforce Espresso confirmations on the batches being posted (e.g. by verifying a TEE attestation from the batcher), otherwise there is no guarantee that what the Caff Node executes is the same as what the L1 eventually settles. Also, there has to be at least one correct batcher, otherwise you can hit force inclusion that breaks Espresso confirmations.

**- Trusting Caff Nodes:** Interacting with Espresso typically happens through Caff Nodes. Assuming the code of the Caff Node has no bugs, you can rely on the execution results without waiting for L1 finality.

### The Role of Trusted Execution Environments (TEEs)

A TEE is a secure enclave inside modern processors (such as Intel SGX or AMD SEV) that guarantees:

* **Code integrity** – only the expected code can run inside the enclave.
* **Data confidentiality** – no one, not even the machine’s operator, can tamper with or inspect the enclave’s internal state.
* **Remote attestation** – anyone can verify that the enclave is running the correct code.

Espresso’s Caff Nodes and batch posters use TEEs to ensure that transaction ordering and execution are correct and cannot be tampered with by malicious operators. TEEs are powerful but not magic. They rely on hardware security guarantees from chip manufacturers. If a TEE is compromised (e.g., through a new hardware attack), the guarantees may break.


# The Espresso Network

The universal base layer

The Espresso Network is a base layer (L1) for L2 chains, providing secure confirmations for transaction ordering and data across chains. Its globally distributed network of validators run a BFT consensus protocol (HotShot) to maintain an available and consistent database of transactions. L2 sequencers write transaction blocks to this database, which serves as a source of truth for the list of transactions that define L2 state. The advantages an L2 stands to gain from using Espresso Network include higher-throughput, lower operating costs, and faster transaction finality.

Whereas L2 transaction blocks written to Ethereum L1 take at least 15 minutes to finalize, L2 transaction blocks written to Espresso Network reach finality within a few seconds, enabling any L2 node to derive and confirm the L2 state with confidence. This is guaranteed by the safety of Espresso Network's consensus protocol. To break the integrity of Espresso Network transaction confirmations, an adversary would need to both compromise the L2 sequencer as well as control 33% of Espresso Network's distributed validators (and in the future 33% of $ESP), similar to other proof-of-stake consensus protocols. The transaction confirmation guarantees of Espresso thus mirror that of Ethereum L1.

An L2 using Espresso Network may have canonical bridges to other chains, including other L2s, Ethereum L1, Solana, Avalanche, etc. A canonical bridge allows for assets to be locked on the parent chain (e.g., Ethereum L1), minted on the L2 where it can be transferred between accounts or interact with other applications, and withdrawn back to the parent chain. In order for an asset to be withdrawn, a smart contract on the parent chain needs to receive and verify the state of the L2, a process often referred to as \`\`settlement". There are several different methods for doing so, including optimistic fraud games, zero-knowledge proofs, or TEE attestations. In all cases, the parent chain contract verifies that the state it receives is correctly calculated from the list of transactions posted by the authorized L2 sequencer and finalized by Espresso Network.

An L2 on Espresso Network may also choose to use another base layer for finality in addition to Espresso, such as Ethereum L1. In this case the confirmation from Espresso Network may be called a pre-confirmation. The L2 sequencer first writes the transaction blocks to Espresso Network and once it confirms that they were finalized by Espresso Network it subsequently publishes them to the second base layer (e.g. Ethereum L1). L2 clients can pre-confirm transactions by reading L2 transaction blocks from Espresso Network even before the second base layer has received them. L2 clients can also wait for confirmation from the second base layer. There is a mechanism to ensure that the second base layer finalizes the same list of L2 transactions as Espresso Network. Several implementations are possible: for example, a contract on the second base layer can filter blocks that weren't first finalized by Espresso, or L2 nodes reading transactions from the second base layer can apply this filtering directly when calculating L2 state.

Many L2 chains using Espresso Network continue to use Ethereum L1 as a second base layer and have a canonical bridge to Ethereum L1. These chains get pre-confirmations from Espresso Network that are more resilient than those relying only on centralized sequencers for pre-confirmations, which can be broken as a result of hacks or bad actors.

Applications that interact between multiple chains, such as bridges or cross-chain exchanges, are especially sensitive to the security and latency of transaction confirmations and are better able to serve chains that use Espresso Network.


# System Overview

Chains (e.g. L2 rollups) interact with Espresso and with the layer 1 blockchain to facilitate trustless state checkpoints. Specifically, when we refer to L1 and L2s we mean the following:

* **The L1 (layer 1) blockchain:** This is the blockchain that chains using Espresso post [state checkpoints](https://docs.espressosys.com/network/appendix/interacting-with-l1) to. HotShot must also checkpoint its state and history on the layer-1, which will serve as an interface to the rollups. Initially Espresso will run a smart contract on Ethereum that tracks HotShot's state commitments. Other projects can recycle these state commitments to reuse on other chains if they wish.
* **The L2 (layer 2) chains:** These are the chains that use Espresso for fast confirmation. They could be anything from app-specific chains to fully-featured smart contract systems in their own right (like EVM rollups). Each chain is assumed here to be structured as a rollup: after receiving an ordered sequence of transactions, the transactions are executed off-chain in some deterministic VM, and periodically state updates are posted to the layer-1, along with a proof of validity (for ZK-rollups) or a potential fraud proof (for optimistic rollups).

This diagram shows the flow of information through the entire system, starting with transaction submission through clients to various integrated rollups and finally to being certified and checkpointed on the layer-1.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-6f8e77c2f7b6999c7f2d7d7c38eb4dd94a769ee6%2Fconfirmation%20layer.png?alt=media" alt=""><figcaption></figcaption></figure>

The next sections dive into these components and their interactions in more detail.

## Rollup Components

The internal architecture of each rollup will vary greatly depending on the type of rollup (e.g., ZK/optimistic; EVM/app-specific) but all rollups will have a few similar basic components. The internal structure of Rollup 1 is shown in detail in the diagram (for simplicity, the other rollups are abstracted).

A rollup must provide an interface for clients to interact with it. This can be any kind of **API**, although Ethereum-compatible **JSON-RPC** will be common. The API responds to queries about the rollup state by reading from a **state database**, which is populated by the **executor**, a component which executes every block provided by the sequencer. Finally, a **prover** (which may be part of a decentralized prover network) is triggered by updates to the state and is responsible for justifying those state updates. For ZK-rollups, the prover will be triggered by every block and produce a validity proof for the state update. For optimistic rollups, the prover will only be triggered if another node publishes an invalid state update, in which case the prover will generate a fraud proof.

In addition to answering state queries, the rollup API may also serve as an endpoint for clients to submit transactions. While clients can submit transactions directly to the Espresso Network's mempool, doing so may be inconvenient for a few reasons:

* The Espresso Network's transaction submission interface is not specific to any one rollup. Clients will have to wrap their rollup-specific transactions into a more generic kind of transaction before submitting.
* It requires clients to interact with two different services: the rollup API for state queries and the Espresso Network (HotShot) for transaction submissions. Depending on the client software, this may not even be possible. MetaMask, for example, requires a single URL for each chain that it can use for queries and transaction submission.

It is therefore recommended that rollup servers provide a transaction submission interface as part of their API, for those clients who are already using the rest of the API. Such an interface is actually required for conforming JSON-RPC implementations, since the `eth_sendRawTransaction` RPC method allows clients of the RPC to submit a transaction. Whatever its interface, the implementation of the rollup’s submission API can be as simple as wrapping rollup transactions into generic transactions and forwarding them to the HotShot mempool.

## Transaction Flow

Once a transaction is forwarded or submitted, it will be included in a block, and confirmed and made available by HotShot, after which blocks propagate back through the rollups’ executors and provers, which in turn forward their blocks to the L1. Espresso also sends a block commitment to the layer 1 sequencer contract, along with a quorum certificate that the contract uses to authenticate the block. This allows layer 1 rollup contracts to compare the rollup state update proof against a block commitment which is certified as having been finalized by HotShot consensus.

The diagram below shows in more detail the flow of a single transaction from a client through the system.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-98c1eec8673ebe7fab1c9139136057abacfaaea8%2Fsequence%20diagram%20conf%20layer.png?alt=media" alt=""><figcaption></figcaption></figure>

## Transaction Lifecycle

1. User sends a transaction to a chain's server (e.g. an RPC service).
2. The chain forwards the transaction, along with an identifier for that rollup, to the chain's sequencer.
3. The chain's sequencer includes the transaction in a block, which is broadcast to subscribers. One of these subscribers, the rollup node, executes the transaction (along with any other transactions in the block belonging to that rollup). In the case of a ZK rollup, the node may produce a proof of correct execution, which can be broadcast to clients to quickly convince them of the new state.
4. A commitment to the block containing the transaction is persisted in the L1 sequencer contract (along with a proof that the block has been finalized by consensus).
5. A rollup node which has executed the block sends the new rollup state to the L1. It may include a validity proof (for ZK rollups) or open a window for fraud proofs (optimistic rollups).
6. The L1 rollup contract verifies any proofs related to the state update, using the certified block commitment from the sequencer contract to check that the state update corresponds to the correct block.

## Confirmations

Centralized sequencers may give rollup users a pre-confirmation that their transaction will eventually be included in the finalized rollup state. These guarantees typically depend on trust assumptions such as reputation, security bonds, and/or fraud proofs. Users must also assume that the sequencer has not been compromised.

Alternatively, clients can also opt read from a stronger confirmation provided by HotShot (step 3). As long as no adversary controls more than one third of the HotShot stake, the client's transaction can never be rolled back. This is especially usefull for bridging, as they are sensitive to reorgs in the source chain of a bridge transaction.

In the case that a rollup posts their tx data to the L1, clients can also wait for their tx to be finalized on the L1, though in the case of Ethereum, this guarantee can take 15 minutes to attain, as opposed to a few seconds in the case of HotShot.

Once a transaction is finalized, clients may want to read the updated rollup state, either to check the results of their transaction's execution or to prepare another transaction. They have several options (listed below) for doing this, depending on who they trust and how much work they are willing to do themselves. Depending on which option they choose, each client can get their preferred tradeoff between latency, trust, and the amount of work they are required to perform.

* They can rely on the pre-confirmation provided by the sequencer to compute the next rollup state.
* They can leverage Espresso and immediately execute it themselves to compute the new state.
* They can get a state update, at the cost of additional trust assumptions, by trusting a rollup server who has executed the transaction to give them the new state, even before a state update proof is generated.
* In the case of a ZK rollup, they can wait for a state update proof to be generated (step 3) and check that proof. This requires less computation than executing the block, and it is still trustless.
* Finally, if a client does not want to do any computation on their own (or in the case of an optimistic rollup, where there is no validity proof for the client to check) and does not want to trust a rollup server, they can wait until a state update is certified by the L1 (step 6) to fetch the updated state with no trust or computation.


# Properties of HotShot

HotShot’s design intentionally aims to give chains fast confirmations to transactions, while being able to scale to a large number of participating nodes. However, the participating nodes do not execute transactions; hence, individual nodes only need assurance of data availability to vote in consensus, not to have full access to the data. This alleviates high hardware requirements for participation, without sacrificing throughput.

HotShot is based on the consensus techniques used within HotStuff and HotStuff-2.

{% hint style="info" %}
For more details on HotShot and EspressoDA, see our post, [*Designing the Espresso Network: Combining HotShot Consensus with Espresso's Data Availability Layer*](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu)
{% endhint %}

## Key Properties of HotShot

### Separating data availability (DA) and execution from consensus

The HotShot implementation is purpose-built for providing fast confirmations to a large number of generic chains. In particular, it does not perform execution, and the data availability requirement (i.e., ensuring the system has access to data) is handled by a separate DA solution (integrating chains can use the DA solution of their choice, but have default access to use our custom, low-cost DA layer, [EspressoDA](https://docs.espressosys.com/network/espresso-architecture/the-espresso-network/properties-of-hotshot/espresso-data-availability-layer)). This enables HotShot to process more data than typical state machine replication protocols. Such modularity also allows the use of various appropriate sub-protocols as needed.

### Scalability

HotShot relies on all-to-leader and leader-to-all communication, thus reducing the consensus communication complexity to linear in the number of nodes. Since HotShot does not require every node to get a full copy of transaction data, low consensus communication is especially important. HotShot combines this optimistically with a content delivery network (CDN) to efficiently route data and perform computation. This reduces the leader bottleneck and supports a system with a heterogeneous set of nodes, without sacrificing safety and liveness guarantees. These improvements will help HotShot to scale to thousands of nodes, such that it can be run by a large number of Ethereum validators through restaking.

### Responsiveness

HotShot is optimistically responsive and thus, under favorable conditions, commits new blocks as fast as the network allows. This ensures that the protocol’s performance is directly related to the state of the network—under optimistic conditions, the protocol can have low latency and consequently high throughput, too. In HotShot, using a CDN at the network layer synergizes with the optimistic responsiveness property to provide even better performance.


# EspressoDA

{% hint style="info" %}
For a detailed technical overview of EspressoDA, see [*EspressoDA: Our Three-Layered DA Solution*](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu#Part-III-EspressoDA-Our-Three-Layered-DA-Solution).
{% endhint %}

Data availability is the requirement that all transaction data included in blocks is available to every node participating in consensus before a decision can be reached. Because the amount of data can be quite large, requiring each node to download and verify the data before reaching consensus presents a fundamental bottleneck in the throughput of consensus protocols (i.e., the [data availability problem](https://ethereum.org/en/developers/docs/data-availability/#the-data-availability-problem)).

EspressoDA resolves this bottleneck while ensuring data availability via a three-layer system we've designed to balance performance and security:

* **VID Layer:** Stores erasure-coded data chunks across all nodes.
* **DA Committee Layer:** A small committee stores the full data and guarantees efficient recovery of data.
* **CDN Layer:** Uploads full data for retrieval efficiency.

### VID Layer

EspressoDA eliminates the need for each storage node to download all block data by using [Verifiable Information Dispersal](https://eprint.iacr.org/2021/1544.pdf) (VID), a technique that encodes block data into erasure-coded chunks, which are disseminated among node[^1]s in a way that recoverability is ensured. Nodes only need to store their chunk rather than the entire block. This method is more efficient than data availability sampling (DAS) as it limits unnecessary redundancies.

By using VID, EspressoDA guarantees a block will only be finalized if data is verified to be available.

### DA Committee Layer

A small DA committee, selected from the network's nodes, receives the entire data blob and allows for very fast data retrievability, with the VID protocol acting as a fallback in case the DA committee fails to make data available.

EspressoDA ensures data is made available for rollups (optimistically by the DA committee, and guaranteed through VID) without incurring the high costs of posting transactions to the Ethereum L1 (though rollups may still choose to do so). It also avoids centralized DA solutions, which allow the DA operators to freeze the rollup and censor its users.

### CDN Layer

We provide EspressoDA with web2-level performance by using a content delivery network (CDN) to quickly share a block’s data to many different nodes. It can massively accelerate data dissemination. [Benchmarks](https://docs.espressosys.com/network/releases/testnets/cappuccino-testnet-release/benchmarks) from our Cappuccino testnet show a data dissemination of around 5.7 MB/s with 100 nodes. The CDN can also help with efficient recovery of subsets of the data, such as single transactions.

Importantly, the CDN is not trusted for security and thus doesn’t present a single point of failure. EspressoDA works perfectly fine without the CDN, which is only helpful for accelerating the DA and can easily be replaced or removed.

[^1]: in Espresso, each node participating in consensus is also such a storage node


# How It Works

A step-by-step guide on the data availability process

### **Overview**

The data availability process initiates with sequencers submitting blocks to HotShot. Each view[^1], a leader is selected within [HotShot](https://github.com/EspressoSystems/HotShot/blob/main/docs/HotShotDocs/main.md) who bundles these blocks into a single block within HotShot. Rather than sending the full block data to other HotShot nodes, the leader only sends a commitment to the block for other nodes to vote on. All HotShot nodes also participate as storage nodes in the VID protocol and receive a small chunk representing their VID share of the respective block. The [DA leader](#user-content-fn-2)[^2] sends a [DA proposal](#user-content-fn-3)[^3] to the randomly sampled DA committee and all HotShot nodes. After receiving enough votes from the DA committee and the nodes in the network, the DA leader constructs a data availability certificate (DAC).

The DAC is composed of an optimistic DAC obtained from the DA committee and a retrievability certificate from the VID protocol. The optimistic DAC certifies that the proposed data is available to a quorum of the DA committee. The retrievability certificate in turn certifies that VID chunks are available to a quorum of nodes. The DAC design thus enables the best of both worlds, fast DA through DA committees, and robustness through VID. By combining the block commitment with the DAC, Tiramisu ensures that HotShot blocks will only finalized if data is guaranteed to be available.

**Exhibit A: DA and Rollup Architecture**

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-b43689a93843fad8c7d65bc6ea441ab1d4419fec%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### **Process Steps**

**Step 1:** The DA leader begins a broadcast to ensure data is available for all nodes in the network that consists of:

* Sending the DA proposal to the DA committee.
* Sending the VID chunks to all replicas/nodes.
* Gradually sending the DA proposal to all replicas/nodes. Broadcasting proceeds concurrently, prioritized by order of initialization.

A DA proposal will be rejected in either of the following cases:

* The view number is earlier than the view corresponding to the latest valid [quorum certificate](#user-content-fn-4)[^4] (QC).
* The proposal is not from the correct leader.

**Step 2:** Nodes receive the DA proposal (and/or VID share) and submit the data availability vote.

Anyone who receives and approves the DA proposal sends a strong DA vote to the DA leader, while anyone who only receives the VID share sends a normal DA vote.

**Step 3:** The DAC is formed.

The DAC is formed with the creation of the retrievability certificate and optimistic DAC certificate.

The retrievability certificate can be formed by:

* The DA leader receives f + 1 strong votes, which may come from nodes on the committee or just regular nodes who happened to receive the DA proposal quickly enough. f = number of faulty nodes (nodes not performing correct function) in the entire network.
* f + m normal votes, where m is the number of VID shares the block was split into.

The optimistic DAC can be formed in the following way:

1\. The DA leader receives 2f + 1 strong votes from the DA committee (where, unlike above, f is the number faulty nodes in the committee, not in the entire network)

The DA leader stops broadcasting to the nodes after the DAC is formed, or when the quorum certificate from the next leader is received.

**Step 4:** The block commitment proposal is sent to replicas/nodes. The block commitment is a a cryptographic proof that a block is valid and has guaranteed DA.

The leader, once getting sufficient quorum votes for the previous view and the DAC is obtained, sends the commitment proposal. A block can only be applied to a chain if consensus on the commitment proposal is reached by HotShot consensus nodes. The leader also sends the QC to the next leader if one can be constructed.

**Step 5:** The HotShot nodes validate the commitment proposal.

The replicas/nodes validate the commitment proposal if either of the following set is received:

* Commitment proposal and the DAC.
* Commitment proposal and DA proposal, which is simply a block and the view number proposed

The node will send a quorum vote to the next consensus leader once the commitment proposal is validated. As long as over 2/3 of HotShot stake is honest, it is impossible for an adversary, even if bribing the DA committee, to forge a DAC. Utilizing the randomly elected DA committee alongside VID thus enables fast and secure DA, and disincentivizes bribery attacks.

**Exhibit B: DA Process Overview**

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-6e8454f48747acdc354c687ce81f60e5ff549d53%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### **Implementation Options**

By integrating with the Espresso Network, chains can utilize EspressoDA without any additional integration work. However, chains retain the flexibility to use the DA solution of their choice (i.e., chains can use the Espresso Network for fast confirmations, but use Ethereum or another third-party provider for DA).

[^1]: *A view is a period of time during which nodes in the network perform their tasks. For each view, a leader is selected. The leader and nodes coordinate in the view to try to reach consensus.*

[^2]: This is always the same entitiy as the HotShot leader

[^3]: a proposal on a data blob for data availability that consists of the block's transaction data and view number

[^4]: certificate of all the votes nodes have sent to the leader for some specific block


# Interfaces

This section defines in detail the interfaces between each major component in the system architecture.


# Espresso ↔ Rollup

In order to keep HotShot nodes themselves as generic and simple as possible, there is no rollup-specific logic in Espresso itself, and thus Espresso never actively communicates with any rollup. Instead, HotShot *query service* nodes present a public interface which rollups are expected to query in order to integrate with Espresso. This interface takes the form of a REST API. See the [API reference](https://docs.espressosys.com/network/api-reference/espresso-api) for details.

## Usage

Rollup nodes may use these APIs differently depending on the role they are playing in the system (e.g., prover, full node, etc.). A prover can use the API to stream block data from a node, so that it can execute blocks as they are finalized and generate proofs. The prover also interacts with the L1, since it can only verify a rollup proof on the L1 if the L1 has already verified the sequencing of the corresponding block.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-d1cee4a68eed45407797c9f66b77bc12459af0cd%2FUntitled.png?alt=media" alt=""><figcaption><p>Prover / Sequencer Integration</p></figcaption></figure>

A rollup may also include full nodes which store and provide access to rollup-related state, but do not run a prover. Such a full node can stream blocks and verify consensus proofs (QCs) directly from the HotShot APIs, without interacting with the L1. Avoiding interaction with the L1 allows state updates to be computed faster.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-219fe66ae8a681a8a098b7a5721e63d9e6765660%2FUntitled2.png?alt=media" alt=""><figcaption><p>Full Node / Sequencer Integration</p></figcaption></figure>

The rollup also interacts with HotShot via the `submit` API. This interaction is completely independent of the streaming interaction illustrated above. It is simply used to add transactions to HotShot’s mempool so that they may eventually be included in the sequence. Any rollup node which serves a rollup API (e.g. JSON-RPC) should be able to handle transaction submissions through HotShot's `submit` API.

The body of `submit` requests includes the transaction to submit as well as a rollup-specific numeric identifier. This identifier is associated with the transaction in the final sequence, so rollup proofs can use the ID to easily exclude transactions intended for other rollups. Each rollup should have its own protections against cross-rollup replay attacks, such as an EVM chain ID, in addition to this rollup ID.


# Espresso ↔ L1

Espresso interacts with the L1 via the sequencer contract, which validates HotShot consensus and provides a certified, trustless interface for other participants to check the sequence of blocks. Note that the contract only deals with short block commitments, not full blocks, in order to minimize the cost of sending data to the L1. Anyone who has verified a commitment against the contract can get the corresponding block—and authenticate it against the commitment—from the HotShot availability API.

Espresso interacts with the sequencer contract via an interface like:

{% code title="// HotShot.sol" %}

```solidity
struct QC { /* Fields omitted */ } 

// Root of a Merkle tree accumulating the verified sequence of block commitments.
bytes32 public commitmentsRoot;

// Event emitted when new blocks are sequenced.
event NewBlocks(uint firstBlockNumber, uint256[] commitments, bytes32[] frontier);
 
// Called to append a chain of new blocks, given proof that consensus has finalized them.
function newBlocks(QC[] calldata qcs, bytes calldata proof, bytes32[] calldata frontier) external;
```

{% endcode %}

The `newBlocks` method allows a sequencer node to append a list of newly sequenced block commitments to the log stored in the contract. It takes a list of quorum certificates, a validity proof, and a [Merkle frontier](https://iammichaelconnor.medium.com/timber-7db8a5130849) corresponding to `commitmentsRoot`, and it validates that

* Each QC extends from the previous QC in the chain (starting with the previously sequenced QC)
* Each QC is properly signed (the contract will need to store and keep up-to-date the stake table)
* There are enough QCs to prove finality for one or more block commitments. HotShot consensus currently requires a chain of at least 3 QCs before the first QC in the chain is considered finalized (an upcoming version of HotShot will only require a 2-chain of QCs)

If validation succeeds, it updates `commitmentsRoot`, which can then be used by other contracts to validate proofs of inclusion of block commitments in the sequence. On success, `newBlocks` emits a `NewBlocks` event informing clients (e.g. rollup provers) that new blocks have been appended. Those clients can read the new block commitments from the event logs using an Ethereum client. The event logs also include a snapshot of the Merkle frontier just before the new blocks were appended. A client can construct a Merkle path for any given commitment by appending commitments to the snapshotted frontier.

`newBlocks` will fail if the given batch has already been sequenced, since `qcs` will fail the check that it must extend from the last sequenced QC. This ensures that each batch of blocks will only be sequenced once — whoever calls this method first will be the one to sequence it. It is an open question whether the contract will explicitly incentivize sequencer nodes to call `newBlocks`.

To learn more about the sequencer contract, how it stores data, and how it validates QCs, read the section on [its internal functionality](https://github.com/EspressoSystems/gitbook/blob/main/espresso-sequencer-architecture/internal-functionality/sequencer-contract/README.md).


# Rollup ↔ L1

Each rollup communicates with the L1 via its own rollup contract, which can have a unique public interface. In order to verify state updates sent from the rollup (either proactively with validity proofs in the case of ZK-rollups, or when presented with a fraud proof in the case of optimistic rollups), each rollup contract must have access to the certified sequence of blocks which led to the claimed state update.

When using Espresso, the authoritative sequence of blocks is the output of HotShot, which is replicated to the L1 and certified by the HotShot contract. Therefore, rollup contracts will interface with the HotShot contract. The interface which allows rollup contracts to query the certified sequence of block commitments is very simple: the sequencer contract provides a public `sequencedCommitments` field, which is an array of block commitments which have been verified by the contract.


# Internal Functionality

This section describes in detail the internal workings of each component in Espresso.

## Contracts Overview

Core Contracts:

* [`LightClient`](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/light-client)
* [`FeeContract`](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/fee-token)
* [`StakeTable`](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/stake-table/stake-table) (not used for Mainnet 0)


# Espresso Node

An *Espresso node* is a participant in the HotShot consensus protocol which also makes available some services to support L2 clients. The Espresso node is L2 agnostic: it does not provide services specifically tailored to any particular L2. It merely exposes all available information about HotShot and the log of blocks which have been sequenced. Any L2 may query this information and interpret the blocks according to its own execution rules in order to implement a prover, executor, RPC service, etc.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-128398b48bdb67a03cfa3c2ee0295a8225f9f13c%2Fimage%20(12).png?alt=media" alt=""><figcaption><p>Internal components of an Espresso node and their possible usage by various participants in an L2</p></figcaption></figure>

The main internal components of the Espresso node and their respective functions are:

* **HotShot node:** The component which actually runs consensus and communicates with other nodes.
* **HotShot query service:** The query service maintains a database containing the history and current state of HotShot, including all committed blocks and QCs, consensus-specific data like view numbers and stake tables, and status information like validator uptime. It populates this data using events provided by the HotShot validator and provides a REST API for querying the data. There is also a WebSockets-based API which allows clients to subscribe to notifications when new blocks and QCs are produced. The query service does not provide any L2-specific information. The contents of the blocks it provides are the generic transactions that HotShot itself understands.
* [**Submit API**](https://docs.espressosys.com/network/api-reference/espresso-api/submit-api)**:** The Espresso node also provides an interface allowing clients to submit transactions to the HotShot mempool. It takes as input a transaction serialized into bytes and an L2 identifier, and it wraps these into HotShot's generic transaction type.


# Light Client Contract

{% hint style="info" %}
The source code for the light client contract can be found on [GitHub](https://github.com/EspressoSystems/espresso-sequencer/blob/b1884c4bea3246a86cbd430853a5a69e4def0f0a/contracts/src/LightClient.sol).
{% endhint %}

The *light client contract* is responsible for maintaining state about HotShot consensus on the layer 1 blockchain that Espresso (and L2 rollups) checkpoint to.

`LightClient` validates the HotShot state through cryptographic proofs (SNARK proofs). Rollups can use the new `finalizedState` from the contract to confirm the validity and finality of transactions that have been bundled and processed.

```solidity
LightClientState public finalizedState;
```

## Light Client State

This `LightClientState` includes information such as:

* the latest view number, `viewNum`, and block height, `blockHeight`, of the finalized HotShot chain
* the Merkle root of finalized block commitments, `blockCommRoot`

```solidity
struct LightClientState {
    uint64 viewNum;
    uint64 blockHeight;
    BN254.ScalarField blockCommRoot;
}
```

The most important part of the LightClientState is the `blockCommRoot`, which is the root of an [append-only Merkle tree](https://iammichaelconnor.medium.com/timber-7db8a5130849) of all blocks sequenced by Espresso. This root is public, allowing other contracts to use succinct Merkle proofs to verify the inclusion of a certain block commitment at a certain height and to update the root when new blocks are appended.

At any given time, the `LightClientState` contains Espresso block commitments from height 0 up to (but not including) the current block height, `blockHeight`. All commitments for heights greater or equal to `blockHeight` are not present — the corresponding leaf is empty in the tree.

There's another struct, `StakeTableState`, which is used to store the initial stake table commitments. The stake table is currently fixed, meaning it is initialized once and stored in the `genesisStakeTableState` variable when the Light Client contract is first deployed. The initial stake table commitments include the BLS and Schnorr verification keys and the amounts the validators staked.

```solidity
    struct StakeTableState {
        uint256 threshold;
        BN254.ScalarField blsKeyComm;
        BN254.ScalarField schnorrKeyComm;
        BN254.ScalarField amountComm;
    }
```

However, in future versions, the stake table is will become dynamic. This will allow validators' stake commitments and key information to be updated in real-time, allowing the system to adjust to changes in stake amounts, the registration of new validators, or the withdrawal of existing ones.

### Rollups and the Light Client Contract

Rollup contracts on L1 must use the `blockCommRoot` when validating a state transition to ensure that the rollup block claimed to have been executed is indeed the next block in the canonical sequence.

The proposer of a rollup state transition must provide a proof, relative to `blockCommRoot`, showing that the Espresso state commitment at a specified height is consistent with the rollup block commitment.

For rollups to integrate with Espresso, they need to modify their contract on L1 to prove that their state is derived from the Espresso state. For instance, consider a scenario where the Espresso prover pushes a new Espresso state commitment to the light client contract every 1 minute, and the rollup prover submits a new rollup block commitment every 10 minutes to their rollup contract. The rollup prover needs to prove that the block commitment it publishes to the rollup contract corresponds to all its rollup transactions contained in the Espresso blocks during the 10-minute period.

Each Espresso block commitment also commits to a list of rollup transactions (among other metadata) which facilitates lightweight proofs with transaction granularity for arbitrarily old rollup blocks. This approach allows for the verification of these rollups blocks on Espresso's chain and enables the light client contract to operate with a constant amount of storage, irrespective of the HotShot chain's length.

### Data Availability

Since the actual block commitments (let alone the full blocks) are not stored on-chain, it is important to understand the data availability properties ensuring that clients can always retrieve an old block, block commitment, or a block's Merkle proof.

Clients can fetch a Merkle proof for any block from an archival query service and authenticate it against the block root in the light client state. Failing that, they can fetch the individual blocks from [HotShot DA](https://docs.espressosys.com/network/concepts/the-espresso-network/properties-of-hotshot/espresso-data-availability-layer/how-it-works) and extract the proof themselves.

### ZK Proofs, SNARK Proofs, and ZK Circuits

A circuit defines the computation to be proven. Zero-knowledge proof (ZKP) systems can generate cryptographic proofs attesting to the validity of statements described by the circuit without revealing underlying witness. In our context, we rely on SNARK proofs (a special kind of ZKP), whose succinct nature is especially valuable for verifying computation in smart contracts where gas costs are a critical concern. Irrespective of the number of signatures/consensus votes, the size and verification cost of the proof remain constant.

In a zero-knowledge protocol there are two main roles: (i) the *prover* and (ii) the *verifier*.

The *prover* uses a combination of secret inputs (HotShot nodes' Schnorr signatures), also called witnesses, public inputs (the `LightClientState`), and a circuit description in order to generate a SNARK proof.

The *verifier* uses the public inputs and the SNARK proof to verify that the rules defined by the ZK circuit are satisfied. In this case, the `LightClient` contract acts as the verifier for this ZK proof via the `verifyProof` method which is invoked within the `newFinalizedState` function.

Finally, both the prover and verifier use some public parameters. These public parameters are derived from the circuit and a structured reference string (SRS) that requires a trusted setup to be generated but can be reused for other circuits.

### The Light Client Circuit

Let the following circuit $$\mathcal{C}\_{\sf qc}$$ over prime field $$\mathbb{F}\_p$$, the corresponding Jubjub curve group $$\mathbb{G}=\langle g\rangle$$ whose scalar field is $$\mathbb{F}\_r$$ and base field is exactly $$\mathbb{F}\_p$$, so that each group element $$\in \mathbb{F}\_p \times\mathbb{F}\_p$$.

* Public input:
  * stake table commitment: $$\mathsf{cm}\_\mathcal{T} \in \mathbb{F}\_p$$
    * A stake table entry now composes of a triple $$(bls\_ver\_key, schnorr\_ver\_key, stake\_amount)$$. BLS verification key is under `ark_bn254::Fq`, Schnorr verification key is under `ark_bn254::Fr`, and the stake amount is within the range of `ark_bn254::Fr`. The commitment should be computed in the following way: first serialize all BLS keys into elements of `ark_bn254::Fr`, follows by a list of Schnorr keys and then the stake amount. The commitment is the rescue hash of this list.
  * quorum Threshold: $$T \in \mathbb{F}\_p$$
  * attested new finalized hotshot state: $$m:=(v, h, \mathsf{root\_{cm}, cm\_{ledger}, cm\_{stake\_table}}) \in \mathbb{F}\_p^5$$
    * the merkle tree for block commitments can use any hash function (e.g. SHA2) and best if there is an injective mapping between the root value to a $$\mathbb{F}\_p$$ element.
* Secret witness:
  * signers indicator vector: $$\vec{v}\_S$$
  * stake table vector (consists of public key, weight pair): $$\mathcal{T}=\[(pk\_i \in\mathbb{G}, w\_i \in \mathbb{F}*p)]*{i\in\[n]}$$
  * list of schnorr signatures: $${\sigma\_i = (s\_i, R\_i) \in \mathbb{F}*r \times \mathbb{G}}*{i\in \[n]}$$
* Relation:
  * the input signers indicator vector $$\vec{v}\_S$$ is a bit vector
  * correct stake table commitment: $$\mathsf{cm}\_\mathcal{T}= \mathtt{commit}(\mathcal{T})$$
    * we use Rescue-based commitment, thus all operations are native
  * accumulated weighted sum exceeds threshold: $$\sum\_{i\in S}{w\_i} > T$$
    * assumption: there’s no overflow!! NOTE: outside the circuit, the client software that’s in charge of stake table management needs to check the accumulated sum does not exceed modulus $$p$$ AT ALL TIMES! ⚠️
  * signature verification (on each): $$\mathsf{Vfy}(pk\_i, m, \sigma\_i) = 1$$ for all $$\forall i\in \[n]$$.
    * $$c = H(R, m, ..)$$: rescue-based hash to get challenge
    * $$x = g^s$$: a fixed-base scalar mul
      * internally, involves bit-decomposition of $$s$$ and elliptic curve addition based on the bits.
    * $$y = R + pk^c$$: a variable-base scalar multiplication + an elliptic curve addition.
    * $$x\overset{?}{=}y$$: point equality check

### Updating and Verifying LightClientState

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-be6a855187b3742ee4fcbab0096e185e4567a9a6%2FLightClientWorkflow.png?alt=media" alt=""><figcaption></figcaption></figure>

The `LightClientState` is updated by any state prover that submits valid updates to the `LightClient` contract via the `newFinalizedState` method which sets the latest `finalizedState`.

```solidity
function newFinalizedState(
    LightClientState memory newState,
    IPlonkVerifier.PlonkProof memory proof
) external {
  //...
}
```

We assume an *altruistic, honest prover* for now and leave the design of prover market to future work.

For replicas:

* upon receiving new QC from the leader, generate a Schnorr signature over the updated finalized HotShot state, and send it over to the CDN *and* store it locally for a while.
* the local storage for the Schnorr signatures (for each block) can be a sliding window of a fixed size where older signatures got pruned. The window size can be set based on the expected interval for on-chain update plus some buffer accounting for temporarily failing prover.

For the altruistic prover:

* will continuously listen passively for the HotShot state changes, e.g. when a new block has been decided
* periodically requests the Schnorr signatures from the DA layer by sending a request on a specific view $$v$$. This will be the signature for the new finalized state from the consensus nodes
  * For convenience of signature collection, prover will first fetch from CDN (we refer to as the relay server) for the list of Schnorr signatures, if failed, then ask each individual replica (note: not small DA committee, or VID, but each node individually).
* Once a sufficient amount of valid signatures is collected, some provers can then generate a SNARK proof which is submitted alongside the new finalized state to the light client contract.

{% hint style="warning" %}
The contract has the ability to be in permissioned mode where it only accepts proofs from one prover. For the next release, only a permissioned prover, doing the computations, will call this function.
{% endhint %}

Replica nodes update the snapshot of the stake table at the beginning of an epoch and this snapshot is used to define the set of stakers for the next epoch. The light client state must be updated at least once per epoch.

{% hint style="warning" %}
For the next release, we are not using epochs so `numBlockPerEpoch` is set to `type(uint32).max` during deployment.
{% endhint %}

## HotShot state authentication via Schnorr signatures

When a set of HotShot nodes reach consensus and the finalized HotShot state has been updated, they each sign a Schnorr signature on this updated HotShot state. These signatures assert that the signer agrees with the state of each proposed block. The signatures are stored locally on the DA layer, and to save space, older signatures are pruned using a sliding window mechanism. The window size can be set based on the expected interval for on-chain update plus some buffer accounting for a temporarily failing prover.

When a prover (an entity that confirms the truth of a claim) retrieves these signatures, a SNARK proof is then generated. This proof, is used by the `LightClient` contract to efficiently verify these Schnorr signatures. The state of the sequencer contract can be updated only if a correct SNARK proof is provided. This is a critical step that ensures the validity and security of state updates in Espresso's consensus protocol⁠.

The proof of the Schnorr signatures is sent to the `newFinalizedState` function of the `LightClient` contract.

## Verifying the Signatures and Light Client State

The `LightClient` contract also does the work of verifying the proof that is sent by the prover on L1. The `verifyProof` method accepts the proof and a set of public inputs (the `LightClientState`) to check whether the proof correctly verifies the new state being submitted.

```solidity
function verifyProof(LightClientState memory state, IPlonkVerifier.PlonkProof memory proof)
        internal
        virtual
    {
        IPlonkVerifier.VerifyingKey memory vk = VkLib.getVk();
        uint256[] memory publicInput = preparePublicInput(state);

        if (!PlonkVerifier.verify(vk, publicInput, proof, bytes(""))) {
            revert InvalidProof();
        }
    }
```

Verifying a SNARK proof requires a constant amount of space and computation, no matter how many HotShot node signatures are involved. This is unlike verifying the signatures directly, which would require space and computation proportional to the number of signers.

The proof itself contains the HotShot state, the stake table info and the list of Schnorr signatures of the HotShot nodes that formed a Quorum and came to consensus on that state.

This `verifyProof` method is executed when the `newFinalizedState` method is called so that the new state is accepted only if the proof succeeds.

## Escape Hatch Functionality

Rollup contracts keep track of their rollup VM states and depend on our Light Client contract for finalized consensus states. They usually support escape hatches in case of liveness failures on L2. Since different rollups impose different predicates when deciding whether L2 is down, our Light Client contract provides some helper functions to detect delays in HotShot updates. The Rollup contracts can then implement their escape hatch logic based on this info.

Two such helper functions are:

* `function getHotShotCommitment(uint256 hotShotBlockHeight)`
  * Returns the root of the HotShot block commitment tree, where each leaf contains the HotShot block commitment at a new height
* `function lagOverEscapeHatchThreshold(uint256 blockNumber, uint256 threshold)`
  * Returns whether there has been delay between updates
  * Checks if the HotShot state updates lag behind the specified threshold based on the provided L1 block number.
  * The rollup chooses the threshold based on their liveness criteria.
  * HotShot would be considered down if the gap between two consecutive updates where the provided L1 block number should have been recorded, exceeds the specified threshold

Periodically, the light client contract is updated with the latest validated HotShot state. We store a 10 day sliding window of historical Hotshot state roots, `stateHistoryCommitments`, so that optimistic rollups' dispute handling contracts can access required HotShot commitment data during disputes (which is usually during 7 day windows).

## Public Write Methods

### newFinalizedState

This method updates the latest finalized light client state. It is updated per epoch. An update for the last block for every epoch has to be submitted before any newer state can be accepted since the stake table commitments of that block become the snapshots used for vote verifications later on.

*The contract has the ability to be in permissioned mode where there is only one prover that has the ability to call this function. In the next release, only a permissioned prover doing the computations will call this function*

```solidity
function newFinalizedState(LightClientState memory newState, IPlonkVerifier.PlonkProof memory proof)
    external;
```

**Parameters**

| Name       | Type                        | Description            |
| ---------- | --------------------------- | ---------------------- |
| `newState` | `LightClientState`          | new light client state |
| `proof`    | `IPlonkVerifier.PlonkProof` | Plonk proof            |

### computeStakeTableComm

Given the light client state, compute the short commitment of the stake table

```solidity
function computeStakeTableComm(LightClientState memory state) public pure returns (bytes32);
```

## Light Client Contract UML

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-acabb82289537ab480c9f08761d3772ccf0a81ec%2FLightClientUML.png?alt=media" alt=""><figcaption></figcaption></figure>

## Light Client Contract Interaction Diagram

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-6207ed1a69b78ce511f7f54b819b4cf88e790f50%2FLightClientGraph.png?alt=media" alt=""><figcaption></figcaption></figure>


# Fee Token Contract

{% hint style="info" %}
The source code for the fee token contract can be found on [GitHub](https://github.com/EspressoSystems/espresso-sequencer/blob/b1884c4bea3246a86cbd430853a5a69e4def0f0a/contracts/src/FeeContract.sol).
{% endhint %}

The fee token contract enables builders to deposit ETH which allows them to pay for a data processing fee associated with HotShot. While the fee token contract facilitates deposits, HotShot itself manages and tracks the working balance of builder deposits. Initially, the fee token contract only supports deposits. Withdrawals are planned to be enabled in a future release.

```solidity
function deposit(address user) public payable {
    //...
}
```

The contract defines a minimum and maximum amount for deposits to avoid errors and prevent the fee table from being filled with dust.

```solidity
uint256 public immutable MAX_DEPOSIT_AMOUNT = 1 ether;
uint256 public immutable MIN_DEPOSIT_AMOUNT = 0.001 ether;
```

{% hint style="warning" %}
In the Mainnet 0 release, withdrawals are not enabled and thus the `MAX_DEPOSIT_AMOUNT` aims to minimize how much ETH is locked by a builder.
{% endhint %}

## Public Write Methods

### deposit

Allows anyone to deposit an ETH balance for any user

*the deposit amount is less than a specified threshold to prevent accidental errors*

```solidity
function deposit(address user) public payable;
```

## Fee Token Contract UML

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-b6381b695569d6c399a02de0220106e58e55a2d7%2FFeeTokenUML.png?alt=media" alt=""><figcaption></figcaption></figure>

## Fee Token Contract Dependency Graph

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-28fab38c3e6d1b7d76874a7592cb641694107dbb%2FFeeTokenGraph.png?alt=media" alt=""><figcaption></figcaption></figure>


# Stake Table

The s*take table contract* maintains the canonical stake table for HotShot and enables nodes to stake their tokens to participate in HotShot. This contract will be responsible for:

* staking
* unstaking
* delegating

{% hint style="warning" %}
In the Mainnet 0 release, a fixed stake table is used so stake table commitments are not updated.
{% endhint %}


# How the Stake Table Contract Works

The HotShot contract, which verifies and stores Espresso state updates, also stores the entirety of the latest HotShot stake table. By taking this to be not just a mirror of the stake table but the canonical version of it, we gain a number of advantages, including the potential for the L1 itself to make changes to the stake table, a requirement for implementing [restaking](#restaking).

## Restaking

Restaking is a [critical part of the Espresso roadmap](https://hackmd.io/@EspressoSystems/EspressoSequencer#3-Interactions-with-Ethereum-Validators-via-Restaking), since it allows Espresso to share a security budget with Ethereum and aids in incentive alignment between the Ethereum operator set and rollups integrated with Espresso. But to enable restaking using a system like [Eigenlayer](https://www.eigenlayer.com/), the restaking contracts must be able to change the state of the Espresso stake table, such that new entries can be added when new L1 validators opt into restaking for Espresso.

By treating the stake table stored on the L1 as the canonical stake table, we allow L1 smart contracts to do exactly this, merely by writing to another contract on the same L1. Espresso nodes will then read the updated stake table back from the L1 at the start of the next epoch[^1] and begin using the stake table with the restaker's entry for validating future consensus decisions.

This does require every HotShot consensus participant to run an L1 light client in order to make trustless reads from the HotShot smart contract. However, Ethereum's proof-of-stake consensus enables very efficient, lightweight, trustless clients, and this Ethereum client can be bundled directly into the HotShot client executable for a seamless user experience.

## Consensus Sync

In order to verify consensus decisions, a HotShot client must know the stake table that was used to authenticate each decision, so that it can accurately account for the number of votes endorsing each decision. This means that, naively, if a new HotShot client or consensus participant wanted to sync with the current state of consensus, it would have to replay from genesis at least every block which updated the stake table. By storing verified snapshots of the stake table on a trusted L1, new HotShot nodes can instead read the latest snapshot from the L1 and start replaying blocks from there, trusting the L1 validator set to have already verified each block which led up to the snapshot. This is very similar to how rollups can enable fast, trustless sync for their clients by leveraging L1 state updates.

## Exit Escrow Period

When a delegator undelegates or a validator exits, the staked funds are locked for an **exit escrow period** before they can be withdrawn. The default exit escrow period is 7 days.

[^1]: In HotShot consensus, the stake table is only updated at fixed intervals known as *epochs*.


# Staking Rewards Calculation

Espresso uses a proof of stake consensus mechanism where validators and their delegators earn rewards for securing the network. Anyone can participate by delegating ESP tokens to a validator (minimum 1 ESP).

To be eligible for rewards, validators must:

* Have at least one delegator with non-zero stake
* Meet the minimum stake threshold: at least 1/1000th of the largest validator's stake. For example, if the largest validator has 10,000,000 ESP staked, validators need at least 10,000 ESP to be eligible.
* Be in the top 100 validators by total stake

Validators earn rewards when they propose blocks, and those rewards are shared with delegators based on their stake proportion minus the validator's commission.

Key points:

* Rewards are distributed every block to the block proposer and their delegators
* The reward rate adjusts dynamically based on network staking participation
* Delegations become active 2 epochs after being finalized on Ethereum
* Rewards do not auto compound

## Block Reward Calculation

The block reward is dynamic, meaning it changes based on how much of the total token supply is staked. Espresso adjusts rewards to maintain a healthy staking participation level. When fewer tokens are staked, rewards increase to attract more stakers. When more tokens are staked, rewards decrease to keep inflation low.

### Reward Rate Function

The reward rate R(p) depends on the staking participation ratio p = total\_stake / total\_supply:

```
        ⎧  0.03 / √(2 × 0.01)    if 0 ≤ p ≤ 0.01
R(p) =  ⎨
        ⎩  0.03 / √(2 × p)       if 0.01 < p ≤ 1
```

Annual inflation is calculated as:

```
annual inflation = p × R(p)
```

When p ≤ 1%, the formula uses a floor of 0.01, capping the maximum reward rate at 21.21%. This keeps the reward rate between 2.12% and 21.21%, and annual inflation between 0.21% and 2.12%.

The denominator √(2 × p) determines how the reward rate changes with participation. When staking participation is low, √(2 × p) is small, making the reward rate high (21.21%). High rewards attract more stakers. When staking participation is high, √(2 × p) is large, making the reward rate low (down to 2.12%). Lower rewards prevent excessive inflation and maintain token liquidity.

#### Example Reward Rates

| Stake Ratio | Reward Rate | Annual Inflation |
| ----------- | ----------- | ---------------- |
| 1.00%       | 21.21%      | 0.212%           |
| 5.00%       | 9.49%       | 0.475%           |
| 10.00%      | 6.71%       | 0.671%           |
| 25.00%      | 4.24%       | 1.06%            |
| 50.00%      | 3.00%       | 1.50%            |
| 100.00%     | 2.12%       | 2.12%            |

### Block Reward Formula

```
annual inflation = stake ratio × reward rate
block reward = (total supply × annual inflation) / blocks per year
```

Where:

* **Total supply** = initial supply + all rewards distributed so far
* **Blocks per year** = milliseconds per year / average block time in ms
* **Average block time** is measured from the previous epoch

The block reward is fixed for the entire epoch and recalculated for each new epoch.

## Reward Distribution

Validators only earn rewards when they successfully propose a block which is accepted and finalized by consensus. For each view, a leader is randomly selected from the active validator set, with selection probability proportional to stake. Over time, the number of blocks a validator proposes is proportional to their share of the total network stake.

Delegations become active 2 epochs after being finalized on Ethereum. This delay exists because the Espresso network reads the stake table from L1 and applies it with a 2-epoch lag. For example, if your delegation is finalized on Ethereum during epoch 5, your stake becomes active in epoch 7. Rewards begin in the third epoch since the first two epochs don't have the stake table from L1 available.

When a validator proposes a block, rewards are distributed as follows:

First, the portion available to delegators is calculated based on the validator's commission rate, expressed in basis points where 10,000 = 100%:

```
delegator pool = block reward × (10,000 - commission) / 10,000
```

For example, if commission is 1,000 (10%), delegators receive 90% of the block reward. Each delegator then receives a share proportional to their stake:

```
delegator reward = (delegator's stake / validator's total stake) × delegator pool
```

The validator receives everything remaining after delegator rewards:

```
validator commission = block reward - total delegator rewards
```

## Undelegating

You can undelegate some or all of your staked tokens from a validator at any time. When you undelegate, your tokens are removed from the validator's stake on L1. This change takes effect on Espresso 2 epochs after being finalized on Ethereum, the same delay as delegations.

The tokens then enter an escrow period (see [Exit Escrow Period](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/stake-table#exit-escrow-period)). After the escrow period ends, you can claim your tokens.

You can only have one pending undelegation per validator at a time. You must claim your withdrawal before initiating another undelegation from the same validator.

## Do Rewards Compound?

**No, rewards do not automatically compound.** To compound your rewards:

1. Claim rewards to your wallet
2. Re delegate the claimed tokens to a validator


# Smart Contract Upgradeability

The following smart contracts are upgradeable:

* [LightClient](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/light-client)
* [FeeContract](https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/fee-token)

These contracts use the *universally upgradeable proxy pattern (UUPS)* to make it possible to upgrade functionality in the contract, e.g., adding a new method for a future launch.

## How it works

A proxy contract directs calls to the implementation contract, which contains the logic of the system.

When an upgrade is needed, a new implementation contract is deployed and the proxy contract's storage is updated so that it will now route requests to the new implementation. This allows for modifications to be made without affecting the state stored in the contract. Espresso users can continue interacting with the same contract address (the address of the proxy) to access the updated functionalities of the implementation contract. Careful consideration will be made to ensure backward compatibility and data consistency during the upgrade process.


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


# dApp Developers

As a dApp developer, **you don’t need to understand all the internals of how rollups or the Espresso Network work**. What matters is how Espresso can help you build applications that feel faster, safer, and more user-friendly.

By reading from Caff Nodes, you can access this confirmed state almost immediately. For you as a builder, this means:

* **Single-chain apps** can give users fast, reliable feedback that their transactions won’t be reverted.
* **Cross-chain apps** can safely act on messages between chains without waiting minutes, using frameworks like Hyperlane or intents-based systems.

Whether you’re building a wallet, a DeFi protocol, a cross-chain bridge, or a solver in an intents framework, Espresso confirmations reduce latency, improve user experience, and provide stronger security assumptions compared to relying on a sequencer alone.


# Single-chain Apps

Building a decentralized application (dapp) on a rollup integrated with Espresso **unlocks faster, more reliable confirmations without changing how you interact with the chain at the RPC level.**

Normally, rollup applications rely on the parent chain (e.g., Ethereum) to provide finality. For optimistic rollups, this can take up a few hours.

For most dapps, waiting for this kind of finality is too slow. Users need faster confirmations for actions like:

* Sending tokens
* Swapping in a DEX
* Playing a game
* Interacting with NFTs

Espresso provides fast, trust-minimized confirmations that dapps can rely on immediately. **By reading from a Caff Node, your app can present users with consistent and near-instant transaction results**.

### Typical Data Flow

Let’s walk through a transaction step by step:

**1. User submits a transaction**

The user signs and submits a transaction through your dapp’s frontend.

**2. Sequencing**

The transaction is forwarded to the rollup’s sequencer (which could be centralized or decentralized). Anyway, the Espresso Network provides confirmation of the transaction ordering.

**3. Caff Node derives the state**

The Caff Node listens to Espresso confirmations and derives the correct rollup state in real time.

It exposes this state via the **standard Ethereum-style JSON-RPC interface**.

**4. Frontend shows confirmation**

Your dapp queries the Caff Node just like it would a normal RPC.

Because Espresso confirmations are fast, the user sees their transaction confirmed almost instantly.

**5. Parent chain**

Later, the batch is posted to the parent chain (Ethereum, Arbitrum, etc.) but your app doesn’t need to wait for it to provide a smooth UX.

### Example: Token Swap on Rari

Suppose you’re building a DEX on Rari (an L3 integrated with Espresso).

**- Without Espresso:** A user swaps tokens, but your frontend can only show “pending” until the rollup batch is posted and eventually finalized on Arbitrum. This could take minutes to hours.

**- With Espresso:** The user submits the swap, Espresso confirms it within seconds, and your frontend shows the updated balances immediately by querying a Caff Node.

Later, Arbitrum finality and settlement guarantees long-term security, but the user never notices the delay.


# Cross-chain Apps

Cross-chain apps require fast and reliable messaging between rollups. Today, most rollups rely on their parent chain (e.g., Ethereum) to finalize transactions before messages can safely be passed — a process that can take minutes to hours.

Espresso shortens this cycle by providing fast confirmations that middlewares like Hyperlane, intents frameworks, and solvers can rely on to bridge state between chains safely and quickly.

### Message Passing Protocol (like Hyperlane)

Espresso helps message passing protocols like Hyperlane at verious stages:

* Source chain: The validator reads events directly from a Caff Node, which exposes Espresso confirmations.
* Destination chain: Once Espresso confirms a transaction on the source, the relayer can immediately submit the corresponding message to the mailbox contract on the destination chain.

The message can be trusted as correct execution, since the Caff Node derives state directly from the Espresso Network.

#### Cross-chain Data Flow with Espresso + Hyperlane

Here’s the typical flow of a cross-chain message (e.g., Rari → Appchain):

**1. User transaction on source chain (Rari)**

User interacts with a dapp contract that calls the Hyperlane `Mailbox.dispatch` function.

**2. Espresso confirmation**

The transaction is confirmed by Espresso’s HotShot consensus.

**3. The Caff Node exposes the confirmed state.**

Validator picks up the message

Hyperlane’s validator observes the `Dispatch` event from the source chain Mailbox using the Caff Node.

**4. Relayer submits to destination**

Hyperlane’s relayer submits the message to the destination chain’s Mailbox contract.

**5. Dapp contract executes**

The destination dapp receives the message via `handle()` and executes the requested logic.

### Espresso + Intents Frameworks

A growing design pattern in Web3 is the intents-based architecture, exemplified by the Open Intents Framework (OIF):

* Users express what they want to achieve (e.g., “swap token A on Rari for token B on Appchain”).
* Solver networks compete to fulfill these intents efficiently.
* To act correctly, solvers must have access to the latest valid state of both the source and destination chains.

#### Where Espresso fits in:

By querying Caff Nodes, solvers can access fast, correct rollup state without waiting for finality on the parent chain. This significantly reduces both latency and execution risk, enabling cross-rollup intents to be executed safely and quickly.

### Beyond Intents: Other Middlewares

Espresso confirmations extend far beyond Hyperlane or intent frameworks. Middleware protocols such as:

* Across
* Relay (transaction relayers)
* Custom bridges

They all rely on having fast and reliable information about the source-chain state. By integrating with Caff Nodes, they can:

* Cut down the delay between user action and message delivery.
* Provide a Web2-like user experience with near-instant cross-rollup confirmation.


# Rollup Developers


# Optimistic Rollup Integration

In this section, we will outline how an optimistic rollup can be adapted to use fast and secure confirmations from the Espresso Network.

### High-level Optimistic Rollup Architecture

In an optimistic rollup, user transactions are first received by the sequencer, which orders them and produces blocks. These blocks are then sent to the batch poster, which compresses them and posts the batches to the parent chain. The batches are subsequently verified by validators, resulting in a new finalized rollup state.

### High Level Integration Flow

In our integration, the sequencer/batch poster sends blocks to the Espresso network. Once the network confirms them, the batch poster retrieves those blocks, assembles them into batches, and submits the batches to the parent chain. To ensure the data posted to the parent chain matches what the Espresso network confirmed, we run the batch poster inside a Trusted Execution Environment (TEE). With each batch, the poster includes a TEE attestation (proof), which a contract on the parent chain verifies to confirm that the batcher is indeed running inside a TEE.

![Arbitrum Nitro integration flow with Espresso](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-947cd4624c7f64ab388c04f20c95b5b53898b276%2Foptimistic-rollup-overview.png?alt=media)

### Reading Espresso Confirmations

We’ve also built **Caff Nodes**, which are rollup full nodes that get data from the Espresso Network. Bridges and apps can use them to read the rollup state.

![Reading confirmations from the Espresso Network](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-49037a7e6df5756582bde5d816809c47def0ecac%2Fcaff-node.png?alt=media)


# OP Stack Integration

This document outlines key components, design considerations, and special features of the integration that are *specific to the OP Stack*. The general design of an Espresso integration in the context of optimistic rollups  can be found [here](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup).

## Key Components

### OP Batcher

The Espresso integration leverages the **parallel architecture** of the standard OP batcher. In the vanilla OP Stack, the batcher operates two concurrent loops: one that loads blocks from the sequencer, and another that publishes compressed frames to L1. This separation allows to insert Espresso confirmations as an intermediate step without disrupting the existing L1 posting cadence.

**The integrated version of the OP batcher has three loops:**

1. **Fast path to Espresso**: As soon as new blocks arrive from the sequencer (`op-geth`), they are immediately submitted to the Espresso Network for fast confirmation via HotShot consensus.
2. **Confirmation wait**: The batcher waits for Espresso to finalize the batch, then validates that the confirmed data matches what was submitted.
3. **Slow path to L1**: Only after Espresso confirmation does the batcher compress the data into frames and post to L1—maintaining the same L1 transaction frequency as an unmodified batcher.

This design ensures that **blocks reach Espresso as fast as possible** (for fast confirmations) while **L1 costs remain unchanged** (batches are still compressed and posted at the normal rate).

**TEE Enforcement:**

The batcher runs inside an AWS Nitro Enclave (TEE) to guarantee that it cannot post anything to L1 that wasn't first confirmed by Espresso. The TEE manages two keys:

* **Batcher Key**: The centralized sequencing authority registered in the rollup config.
* **Ephemeral Key**: Generated inside the enclave, used to sign batch attestations that prove TEE provenance.

### Base Layer Batch Validation

The base layer verifies that each batch comes from a modified OP batcher running in a TEE. This is achieved through two additional contracts that replace the original [EOA Batch Inbox address](https://specs.optimism.io/protocol/system-config.html?highlight=%22batch%20inbox%22#batch-inbox).

The two contracts work together in a two-step process: first, the batcher registers its TEE-generated ephemeral key with the **Batch Authentication Contract** by providing a TEE attestation, then for each batch it authenticates the batch hash with a signature from that ephemeral key. When the batcher subsequently posts the actual batch data to the **Batch Inbox Contract**, the inbox contract queries the authentication contract to verify the batch was pre-approved by a valid TEE before accepting it. This separation allows the inbox contract to receive raw batch data while the authentication contract handles the cryptographic verification of TEE provenance.

### OP Espresso Streamer

The streamer fetches messages from the Espresso network needed by both the Caff node and the batcher. It:

* Tracks which Espresso blocks are finalized
* Handles out-of-order batch delivery through buffering
* Validates batches against L1 finality requirements
* Manages L1 reorg scenarios

#### OP Caffeinated Node (Caff Node)

The Caff node allows anyone to derive the finalized state of the OP rollup as soon as it is confirmed by Espresso. Key use cases include:

* Applications requiring faster state confirmation (e.g. Centralized Exchange).
* Bridge operators validating cross-chain transactions.

## Special Features

### Allowing Different Batchers

The integration supports scenarios where multiple batchers can post to the inbox contract. This provides resilience and flexibility:

**How It Works:**

* Two batchers can be configured: one TEE batcher and one non-TEE batcher (running on standard hardware)
* Each batcher has a different address, defined at contract deployment
* Only one batcher can be active at any time
* A **Monitor** system controls which batcher is active

**Use Case Example - Failover Mechanism:**

1. A new component, the Monitor, continuously checks the health of the TEE batcher
2. If the TEE batcher is unresponsive for a specified duration, the Monitor activates the non-TEE batcher
3. When the TEE batcher recovers, the Monitor waits for the non-TEE batcher to close its channel on L1, then reactivates the TEE batcher

This ensures the rollup chain keeps progressing even if the TEE batcher malfunctions or the Espresso network temporarily loses liveness.

### Support for OP Succinct Lite

[OP Succinct](https://succinctlabs.github.io/op-succinct/) is a project by Succinct Labs that brings ZK proofs to OP Stack rollups. It offers two modes:

* **Validity Mode**: Converts the rollup into a full ZK rollup with validity proofs for every state transition
* **Fault Proof Mode (Lite)**: Uses ZK proofs within a dispute game system for single-round dispute resolution

[**OP Succinct Lite**](https://succinctlabs.github.io/op-succinct/fault_proofs/fault_proof_architecture.html) implements a ZK-enabled fault proof system that replaces the standard OP Stack interactive bisection game. Instead of multiple rounds of bisection to identify a disputed state, challengers simply submit a challenge and the proposer (or anyone) can submit a ZK proof to resolve the dispute in a single round.

**Why OP Succinct Lite is Orthogonal to the Espresso Integration:**

OP Succinct Lite and the Espresso integration solve two different problems and can be used independently or together:

| Aspect             | Espresso Integration                     | OP Succinct Lite                               |
| ------------------ | ---------------------------------------- | ---------------------------------------------- |
| **Problem solved** | *When* you get confirmations             | *How* disputes are resolved                    |
| **Mechanism**      | Fast confirmations via HotShot consensus | Single-round ZK dispute resolution             |
| **Trust model**    | TEE ensures L1 consistency with Espresso | ZK proofs to resolve challenges                |
| **Timeline**       | Seconds (vs. 12-15 min L1 finality)      | Proof on challenge (vs. multi-round bisection) |

**Independence:**

* An OP Stack chain can use Espresso for fast confirmations **without** OP Succinct (using traditional fraud proofs)
* An OP Stack chain can use OP Succinct **without** Espresso (ZK fault proofs with standard L1 batch posting)
* An OP Stack chain can use **both together**: Espresso provides fast confirmations while OP Succinct Lite provides ZK-based dispute resolution.

**How they are combined in this integration:** The derivation pipeline modifications for Espresso (reading batches from Espresso instead of just L1) must be reflected in the ZK-provable Kona implementation. This ensures that ZK proofs can correctly verify state transitions derived from Espresso-confirmed batches. The integration uses a maintained [fork of Kona](https://github.com/EspressoSystems/kona-celo-fork) that includes Espresso-specific derivation logic, in which transactions sent to the Batch Inbox contract that revert are deliberately ignored.

### Resources

* [GitHub Repository of OP Stack Integration](https://github.com/EspressoSystems/optimism-espresso-integration)
* [Espresso Engineering Wiki - OP Stack Integration](https://eng-wiki.espressosys.com/mainch36.html)


# Nitro Chain Integration

TL;DR - Chains and Rollup-as-a-Service (”RaaS”) providers can leverage the Espresso Network to provide users with faster, more secure confirmations on their transactions. The Espresso Network also provides chain operators with information about the state of their own chain and the states of other chains, all of which is important for improved UX and ultimately, cross-chain composability. This document outlines the steps for chains/RaaS to integrate with the Espresso Network.

Integration at a glance - Integrating with the Espresso Network requires minimal changes to Arbitrum Nitro's existing rollup design, and the key change is running the Arbitrum Nitro batch poster inside a Trusted Execution Environment (”TEE”). See [here](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/nitro/using-tee-with-nitro) for an explanation of this design and see [here](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/nitro/arbitrum-nitro-trust-and-liveness-dependencies) for trust assumptions that partners should be aware of when integrating. Today, Espresso has developed software to run the batch poster using SGX in Microsoft Azure. We plan to release a version compatible with AWS Nitro (not to be confused with Arbitrum Nitro) by EOQ1’25.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-b8a469b05b6ef33da30973e1a68260881fb0180c%2Fimage.png?alt=media" alt=""><figcaption><p>See here for the technical integration diagram</p></figcaption></figure>

### Prerequisites & Requirements (1-3 days\*)

\**Assumes familiarity with TEEs. Teams may want to allocate up to 7 days to upskill and deploy this technology for the first time.*

We will host a kick-off call to walk through your technical architecture, including what cloud providers you work with. In an effort to expedite the integration process, we ask that you please share with Espresso:

1. A config file that we can work from. Note: This is only needed if Espresso is running the batch poster.
2. Direct access to your RPC node (instead of through an intermediary). Note: This is only needed if Espresso is running the batch poster.
3. Confirmation that you are able to run the TEE within your existing infrastructure. Note: Espresso is able to run it on your behalf; however we prefer to support you to run it using your own infrastructure.
4. Confirmation of the integrating chain's current Arbitrum Nitro version.
5. Other pre-requisites include understanding how a TEE operates, if you aren't already familiar:
   * Docs specific to AWS Nitro Enclaves:
     * [Review Hello Enclaves sample application](https://docs.aws.amazon.com/enclaves/latest/user/getting-started.html)
     * [Install AWS Nitro on Linux](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-cli-install.html) OR
     * [Install AWS Nitro on Windows](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-cli-install-win.html)
   * Docs specific to SGX:
     * [Guide to determine which hardware/cloud providers support SGX](https://github.com/ayeks/SGX-hardware#hardware-with-sgx2-support)
     * [Guide to enable a prover using SGX](https://docs.taiko.xyz/guides/node-operators/enable-a-prover/) (note this links to Taiko’s docs, as Taiko currently uses SGX)

### Run deployments (2-3 weeks)

We require that teams run a testnet and mainnet deployment; however chains and RaaS providers have the opportunity to also run internal devnet deployments beforehand (this is recommended if it's our first time working together). This process will allow us time to fix any issues and bugs that may occur during testing and will ultimately ensure a more seamless transition to mainnet. An illustrative integration timeline may look like this (see diagram below):

* An internal deployment (3-4 days) is optional but is recommended for new architecture or a RaaS provider that has not previously integrated with Espresso.
* A devnet deployment (3-7 days) is optional but is recommended for new architecture or a RaaS provider that has not previously integrated with Espresso.
* A testnet deployment (5-7 days) is required, and we look to run a testnet for 5-7 days with no incidents before we consider deploying to mainnet.
* A mainnet deployment would follow a successful testnet deployment.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-0904f1d7e0254337da38e830ba4e5caa98cba165%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Migration Flow (1-3 hours)

1. Run the batch poster inside the TEE (e.g. AWS Nitro or SGX)
2. Deploy the EspressoTEEVerifier contract
3. Stop the batch poster node and copy the batch poster’s databases files to the TEE
4. Perform the sequencer inbox migration
5. New batch poster starts catching up messages and building up state

### Support (0.5-1 hour per week)

* Espresso engineers will support your chain and RaaS provider as you navigate the integration process through relevant devops services, async tech support, and calls to run through integration steps.
* Espresso has a 24x7 support model and tracks the health and frequency of batch posting to ensure that there are no delays. If something isn't working, Espresso will automatically trigger an on-call procedure to investigate the incident. We recommend that our integrated chains also monitor these health metrics and have an incident management procedure.

### FAQ

1. How much does it cost a chain or RaaS provider to integrate with Espresso?
   1. Fees are paid by the builder of each block. Initially, in Mainnet 0.0/Decaf 0.0, Espresso will run a simple builder and cover fees. Fees will not be collected from rollups using Espresso or their users. There will be no third party builders during Mainnet 0.0/Decaf 0.0.
2. What is Espresso’s latency for blocks? How long does it take blocks to reach finality?
   1. Espresso confirmations are faster than waiting for Ethereum finality, which takes 12-15 minutes. Using Espresso, the current latency for blocks is 2-9s (1-3s with transactions, 8s with no transactions) with HotShot finality reached after 3 consecutive blocks, typically in 6-20s (slower when blocks are empty). There are future roadmap improvements to decrease latency and time to finality (including an adjustment to finalize after 2 consecutive blocks, rather than 3, which should result in a 20-30% reduction in latency).
3. What is Espresso’s throughput per second?
   1. During some recent heavy load testing, we achieved \~100 TPS with small transactions (\~200 bytes each). We currently have a 1MB limit on the block size, which performed well under the same load testing. We plan to use our Proof of Stake upgrade in March 2025 to significantly improve network throughput and latency with (i) an increase to the block limit, and (ii) adding erasure coding via [Verifiable Information Dispersal](https://espresso.discourse.group/t/faster-vid-on-espresso-s-critical-path/39).


# Using TEE with Nitro

The Espresso Network is a confirmation layer that provides chains with information about the state of their own chain and the states of other chains, which is important for cross-chain composability. Espresso confirmations can be used in addition to the soft confirmations from a centralized sequencer, are backed by the security of the Espresso Network, and are faster than waiting for Ethereum finality (12-15 minutes).

Purpose: This document describes how the Espresso Network provides fast confirmations to Arbitrum Orbit chains. Espresso has developed a TEE based integration, which is ready for chain operators and rollup-as-a-service providers to implement. There is some assumed familiarity with the [Arbitrum Nitro stack](https://docs.arbitrum.io/launch-orbit-chain/orbit-gentle-introduction).

How it works: In a regular chain, the transaction lifecycle will look something like this: A user transacts on an Arbitrum chain. The transaction is processed by the chain’s sequencer, which provides a soft-confirmation to the user, and the transactions are packaged into a block. The sequencer is responsible for collecting these blocks, compressing, and submitting them to the base layer. If the base layer is Arbitrum One or Ethereum, then the transaction will take at least 12-15 minutes to finalize, or longer depending on how frequently the sequencer posts to the base layer. In this transaction lifecycle, the user must trust that the chain’s sequencer provided an honest soft-confirmation and will not act maliciously. There are limited ways to verify that the sequencer and batcher acted honestly or did not censor transactions.

However, if the chain is integrated with the Espresso Network: The sequencer provides a soft-confirmation to the user, while the transactions are also sent to the Espresso Network to provide a stronger confirmation secured by BFT consensus. A software component of the sequencer called the batch poster (or “batcher”) is run inside a TEE and must honor the Espresso Network confirmation. It cannot change the ordering or equivocate. This gives a strong guarantee that the transaction will ultimately be included and finalized by the base layer.

* Implication: The user must trust that the chain’s sequencer provided an honest soft-confirmation; however the Espresso Network provides a stronger confirmation that keeps the sequencer accountable and prevents the sequencer from equivocating or acting maliciously. The initial implementation of the batch poster is permissioned and the user must trust that it will not reorder blocks produced by the sequencer.

Integration considerations: \*\*Integrating with the Espresso Network requires minimal changes to Arbitrum Nitro’s existing rollup design. The key change is running the Arbitrum Nitro batch poster (which collects multiple transactions, organizes them into batches, and compresses the data to post to the base layer) inside a Trusted Execution Environment (“TEE”). Espresso’s preferred TEE for this integration is built using Intel SGX, and we plan to support other approaches in the future.

Effort required: We would kick off the integration process with a full walkthrough of your architecture. Espresso will provide a config file that chains and RaaS providers can leverage during integration. We prefer to have direct access to your node (instead of through an intermediary).

### **Goal**

The Espresso Network’s fast confirmation layer provides users with faster, more secure confirmations on their transactions as well as chain operators with information about the state of their own chain and the states of other chains, all of which is important for improved UX and ultimately, cross-chain composability.

The goal of this document is to integrate the Espresso Network’s fast confirmation layer with minimal changes to Arbitrum Nitro's existing rollup design. By leveraging Espresso’s fast confirmations, a rollup accepts a batch only after it has been finalized by the Espresso Network. This integration ensures that each batch processed by the rollup is consistent with the blocks finalized via the Espresso Network.

This approach involves running an Arbitrum Nitro node with only the batcher enabled, operating in a TEE environment (such as Intel SGX). The batcher signs the combined hash of `blob hashes` and add this signature to the L1 transaction calldata.

#### **Assumption**

This document assumes that the batch poster sends only blob transactions to L1. However, in some [cases](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/batch_poster.go#L1212), it does post the data in calldata. The flow remains the same in this scenario, except that the batcher signs the [data](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/batch_poster.go#L1049) directly, and the Sequencer Inbox contract verifies the signature accordingly.

### **Batch Consistency Checks**

To ensure that the batch has been finalized by the Espresso Network (“HotShot” is the name of the consensus protocol), the following checks are required:

1. **Namespace Validation:** Ensure that the set of transactions in an Arbitrum Nitro batch corresponds to an Arbitrum Nitro/Orbit chain namespace. Namespacing allows multiple chains to use Espresso’s fast confirmation layer simultaneously by associating each chain’s transactions with a unique namespace within the Espresso Network blocks.
2. **Espresso Block Merkle Proof Check:** Confirm that the Arbitrum Nitro batch maps to a valid HotShot block. Specifically, verify that the HotShot block associated with an Arbitrum Nitro batch is a valid leaf in the Merkle tree maintained by the light client contract, which stores the state of HotShot on Ethereum.

#### **Integration Design**

The integration flow is as follows:

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-c743273efb40ac444259cedd6a8f25e838adab3e%2Fimage.png?alt=media" alt=""><figcaption><p>Arbitrum Nitro integration flow with Espresso</p></figcaption></figure>

The flow is as follows:

1. The sequencer calls `WriteSequencerMsg` on the transaction streamer.
2. The batcher fetches the message from the transaction streamer and submits the transaction to HotShot via the transaction streamer. Code for this is already implemented in the batcher [here](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/batch_poster.go#L523).
3. The batcher then calls the query API to check if the transaction has been finalized by HotShot. This code is also written and can be found [here](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/transaction_streamer.go#L1205).
4. Once the transaction is finalized, the batcher performs batch consistency checks.
5. The batcher computes the hashes of the blobs it plans to submit. (Note: Arbitrum uses [blob](https://eips.ethereum.org/EIPS/eip-4844) transactions.) This allows the batcher to sign the combined hash of the blobs, along with other calldata fields, before sending the transaction. The signature is then included in the transaction’s calldata. If blob transactions are not being used, the batcher instead signs the [l2MessageData](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/batch_poster.go#L1049) along with the other calldata fields.
6. The `Sequencer Inbox` contract must be modified to verify the batcher’s signature. If the signature is invalid, it will revert the transaction.

### **Batching Flow Changes**

#### **Running Arbitrum Nitro batch poster in TEE**

The first set of changes require running the `batch-poster` in a Trusted Execution Environment (TEE), specifically [Intel SGX](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/software-guard-extensions.html).

* Several LibOSes have been developed to run applications on SGX, including [Gramine](https://gramineproject.io/), [Occlum](https://occlum.io/) and [EGo](https://github.com/edgelesssys/ego). We selected Gramine due to its maturity, stability, and comprehensive documentation.
* We implemented [Remote Attestation](https://en.wikipedia.org/wiki/Trusted_Computing#Remote_attestation) support, enabling anyone to verify the SGX proof. This is accomplished by generating a Remote Attestation TLS (RA-TLS) certificate during startup, which embeds the SGX attestation report (more info [here](https://github.com/gramineproject/gramine/pull/1039)).

#### **Submitting Transactions to the Espresso Network (HotShot)**

Most of the necessary [code](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/batch_poster.go#L523) for this function (which allows the batcher to submit transactions to Espresso after receiving transactions from the sequencer) is already implemented in our batcher.

#### **Checking for HotShot Finalization**

We have existing [code](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/batch_poster.go#L532) in place where the batcher prepares an Espresso justification once HotShot finalizes a transaction.

#### **Verifying Batch Consistency**

Batch consistency verification involves checking the block Merkle proof and the namespace proof. [Jellyfish](https://github.com/EspressoSystems/jellyfish), Espresso’s cryptography library, is written in Rust. We created an `espresso-crypto-helper` Rust package that allows us to [verify the Merkle proof](https://github.com/EspressoSystems/nitro-espresso-integration/blob/56b488969e4ea1a9868ec44732a5d46f1279f313/arbitrator/espresso-crypto-helper/src/lib.rs#L63) and [namespace proof](https://github.com/EspressoSystems/nitro-espresso-integration/blob/56b488969e4ea1a9868ec44732a5d46f1279f313/arbitrator/espresso-crypto-helper/src/lib.rs#L104).

To enable the Go-based batcher to use these Rust functions, we implemented a Foreign Function Interface (FFI) to expose the Rust verification functions to Go.

#### **Sending Transactions to L1**

We add the batcher’s signature to the [transaction calldata](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/batch_poster.go#L1039) over the blob hashes, which can be constructed using the [ComputeCommitmentAndHashes](https://github.com/EspressoSystems/nitro-espresso-integration/blob/79b53b811bc01b71c2a54901553449fbb3950e9c/util/blobs/blobs.go#L113) method. We sign `blob hashes` instead of the blob data itself because, in a Blob Commitment transaction, the blob data is unavailable on the execution layer, only `blob hashes` are accessible in Solidity via the `blobhash` [opcode](https://github.com/ethereum/solidity/blob/879d8e69f884419a9bc4a0cfe17a6d73ae14d836/libevmasm/Instruction.h#L92).

In a scenario when a chain is not using blob transactions, the batcher will sign the [l2MessageData](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/arbnode/batch_poster.go#L1049).

### **Sequencer Inbox Contract**

* The Sequencer Inbox’s [methods](https://github.com/OffchainLabs/nitro-contracts/blob/main/src/bridge/SequencerInbox.sol#L407) will need to be modified to accept the batcher signature as a parameter.
* These methods verify that the signature is valid

### **Escape Hatch**

We also have an escape hatch where the batch poster calls [IsHotshotLive](https://github.com/EspressoSystems/espresso-sequencer-go/blob/b786a91eaacb8b2fee57e691b32fd98417616589/light-client/light_client_reader.go#L18) on the LightClientContract before posting a batch. Each batch poster configuration allows the chain to choose between two behaviors: (i) waiting for Hotshot to go live before posting the batch, or, (ii) if Hotshot is not live, proceeding without checking batch consistency with Hotshot. This flexibility enables chains to tailor their approach as needed.


# Arbitrum Nitro Trust & Liveness Dependencies

TL;DR - The Espresso Network is a confirmation layer that provides chains with information about the state of their own chain and the states of other chains, which is important for cross-chain composability. Espresso confirmations can be used in addition to the soft confirmations from a centralized sequencer, are backed by the security of the [Espresso Network](https://docs.espressosys.com/network/guides/using-the-espresso-network), and are faster than waiting for Ethereum finality (12-15 minutes).

Recap: optimistic chain architecture - There are two components of the Arbitrum Nitro stack:

1. The validator, the fraud proof mechanism, and everything that exists to secure the integrity of the chain.
2. The sequencer, which includes the batcher, and exists to drive progress and have some influence (in that they can re-order transactions) without the ability to corrupt the chain and steal user funds.

What Espresso is changing and why -

* What? Espresso is not changing how sequencing is done; instead we are ensuring that what gets sequenced is immediately posted to the Espresso Network and what is ultimately published to the L1, is consistent with the Espresso Network. On a technical level, we do this by modifying the software module (the batcher), ensuring that the batcher publishes batches to the Espresso Network. The batcher module is run inside a TEE so that even if hacked the batcher will never publish something to the L1 that is inconsistent with what was published and finalized on the Espresso Network.
* Why? These additional checks confirm the order of transactions and prevent equivocation prior to finality. These confirmations provide stronger guarantees to chains wanting to verify their own state, or the state of chains they want to compose with. Importantly these changes are limited in power and do not provide the ability to directly steal user funds, although there may still be chain reorganization risk for applications like bridges that rely on soft-confirmations (instead of waiting for chain finality).

**Resources:**

* This document outlines key trust and liveness dependencies to help chains to understand the design.
* The detailed technical design is outlined [here](https://github.com/EspressoSystems/gitbook/blob/main/concepts/rollup/integrating-an-optimistic-rollup/nitro/broken-reference/README.md) for reference.

### **Liveness Dependencies**

#### **Batch Poster**

*ELI5*: The chain’s sequencer batches individual transactions into blocks, and the chain’s batch poster is responsible for collecting these blocks and submitting them to the base layer (for example, an Arbitrum Orbit L3 would typically post batches to Arbitrum One, an L2). If the batch poster were to crash, customers could still use the chain regularly and would only be limited in their ability to withdraw funds (as delays in batch posting impact the fraud proof window).

*Technical explainer*: the batch poster does play a role in the liveness of `withdrawals`. Any downtime experienced by the batch poster adds to the latency of withdrawals initiated during its outage. This is because the challenge period cannot begin until the batch poster comes back online and posts a batch containing the withdrawal. Given that the challenge period for an optimistic rollup is seven days, the delay caused by a batch poster outage would only become *noticeable* to users if the batch poster remains down for several days, rather than just a few minutes. While this scenario is unlikely, it remains a potential risk. An extended delay in batch posting (>72 hours) may trigger Arbitrum Nitro’s [force-inclusion mechanism](https://docs.arbitrum.io/learn-more/faq#can-i-withdraw-my-funds-from-arbitrum-back-to-ethereum-without-going-through-the-sequencer-what-about-funds-that-are-in-a-contract) and may result in a chain reorganization that may impact clients or applications that rely on soft confirmations. See [batch posting](https://docs.arbitrum.io/how-arbitrum-works/sequencer#batch-posting) for details.

*Integration considerations*: The responsibility of running infrastructure (whether operated by your Rollup-as-a-Service (”RaaS”) provider or your chain) is unchanged. In either case, your chain (or your RaaS provider) will be required to run a fork of the Nitro batch poster developed by Espresso Systems. The batch poster will need to be run in a Trusted Execution Environment (”TEE”) that is SGX/AWS Nitro supported, with support for TDX coming soon. Espresso can share a getting-started guide, links to relevance code, and technical/integration support.

#### **Espresso Network**

*ELI5*: The Espresso Network is designed to enhance the security of soft confirmations, which are given when a transaction has been included in a pending, recent block but has not yet been finalized. In doing this, Espresso Network’s confirmations speed up the process of a transaction reaching finality (when a transaction is considered irreversible and the network has reached consensus that the transaction is valid) by providing a quicker indication that a transaction is likely to be valid. In the unlikely event that the Espresso Network goes offline, there may be an impact on a users’ ability to withdraw funds as outlined above (see [Batch Poster](#batch-poster)). Chains can choose to (i) disable the escape hatch, or (ii) enable the escape hatch in the event that the Espresso Network is offline. Chains that enable the escape hatch may result in clients and bridges building an incorrect state due to their reliance on soft confirmations.

*Technical explainer*: Similarly, if the Espresso Network goes offline, there can be a similar impact on `withdrawals` as outlined above (see [Batch Poster](#batch-poster)). While the likelihood of such downtime is low, it remains a possibility.

#### **Hotshot URL**

*ELI5*: The Espresso Network provides updates on state via the HotShot URL, similar to an RPC. If the HotShot URL were to go offline or provide an incorrect state, this may trigger a failure that could delay batch posting.

*Technical explainer*: The batch poster configuration specifies a `Hotshot URL`, which is analogous to an `RPC URL`. This URL is used to connect to the node running the Hotshot network to retrieve updates.

There is a liveness dependency on the `Hotshot URL`. If this URL provides incorrect state, it will lead to Espresso Network specific checks failing and thus preventing the batch poster from being able to post batches. The likelihood of this is low but still possible.

*Integration considerations*: None. Please note that chains can verify liveness by checking the [Espresso Explorer](https://explorer.main.net.espresso.network/) and [Query Service](https://query.main.net.espresso.network/v0/status/metrics) to verify that the Espresso Network is live and the HotShot URL is working as intended. If there have been no updates for 15-30 minutes, please assume there is an issue that we will investigate via on-call procedures and resolve.

### **Trust Dependencies**

#### **L1 URL**

We retrieve the Arbitrum state from an RPC node. This introduces a trust dependency on the RPC node to provide accurate state information. You may configure the batcher to use the same Arbitrum RPC that it is currently using.

#### **Light Client Contract**

A light client contract has been deployed on the Arbitrum network. This contract maintains the state of the Hotshot network. There is a trust dependency that this contract remains secure, unhacked, and consistently contains the correct state.

#### **SGX Intel/AWS Infrastructure**

We have built our design using Intel SGX/AWS Nitro, so there is a trust dependency that Intel/AWS is behaving honestly and their infrastructure is secure and trustworthy.


# ZK Attestation Verification

Our rollup integrations now use on-chain verifiable zero-knowledge proofs for TEE attestation reports on AWS Nitro. This improves on our [previous design](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup#high-level-integration-flow), where TEE attestation proofs were verified directly on-chain.

### Introduction

TEE attestation report verification for AWS Nitro was extremely expensive on-chain in our previous design, costing around **63 million gas** to validate an attestation when no certificates had been previously verified.

After the Fusaka upgrade and the resulting changes to gas costs for certain opcodes, on-chain attestation verification became infeasible for L2s and L3s. To address this, we integrated with **Automata Network’s AWS Nitro ZK proof generation** [**SDK**](https://github.com/automata-network/aws-nitro-enclave-attestation/tree/main), which enables the creation of zero-knowledge proofs for verification of TEE attestation reports, and their **NitroEnclaveVerifier** [**contract**](https://github.com/automata-network/aws-nitro-enclave-attestation/blob/main/contracts/src/NitroEnclaveVerifier.sol), which allows these ZK proofs to be verified on-chain.

Under the hood, Automata uses **Succinct’s SP1** for proof [generation](https://docs.succinct.xyz/docs/sp1/getting-started/install) and **sp1-**[**contracts**](https://github.com/succinctlabs/sp1-contracts) for on-chain ZK proof verification. This integration reduced gas costs from **63 million to approximately 260k**, representing roughly a \~240× improvement

### High Level Integration Flow

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2FX3ngkMs1gBMMIba5Hx2c%2Fzk_attestation.png?alt=media&#x26;token=3890df01-2947-4470-a118-86bb003eaf3a" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: Our previous flow can be found [here](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup#high-level-integration-flow)
{% endhint %}

**Updated Flow:**

* The batch poster running inside a TEE creates a TEE attestation and sends it to Espresso’s attestation verifier service.
* The attestation verifier service calls Automata’s Nitro ZK Attestation SDK, which gathers all required inputs and calls the Succinct Network to generate a zero-knowledge proof over the verification of the TEE attestation
* The Succinct Network returns the proof, which Espresso’s Attestation SDK then passes back to the batch poster.
* The batch poster submits the ZK proof to L1 along with other batch data, where it is verified by a set of on-chain contracts.

### Requirements & Trust Dependencies

With this new flow, we require the rollups/RaaS providers to have a few new trust dependencies and requirements

**Trust Dependencies**

* Succinct Network
* Automata’s Nitro ZK Attestation SDK

**Requirements**

* Rollup/RaaS needs to run Espresso’s Attestation Verifier service
* Succinct Network tokens in-order for the network to generate the ZK Proof. It is estimated to cost around 0.3 PROVE tokens for each request. New request will be made every time there is a new code update or a new restart ( the restart requirement will be removed soon) and batcher needs to generate a new TEE attestation.

### On-chain Cost Analysis

Cost analysis based on prices on Jan 8th, 2026.&#x20;

```
Base Fee on Ethereum: 0.53 GWEI
Ether Price: 3,091.47USD
Prove token prices: $0.4349 USD
```

\
**Calculations based on every code update**

| Design                                             | On-chain Costs                                         | Additional Costs         | Total Cost  |
| -------------------------------------------------- | ------------------------------------------------------ | ------------------------ | ----------- |
| AWS Nitro attestation report Verification on-chain | (63 million \* 0.53 GWEI) \~ 0.03 Ether \~ 93 USD      | None                     | \~ 93 USD   |
| ZK Proof Verification on-chain                     | <p>(270k  \* 0.53 GWEI) <br>0.0001378 ETH \~ $0.4 </p> | 0.3 PROVE token \~ $0.13 | \~$0.53 USD |


# ZK Rollup Integration (WIP)

Espresso ZK rollup integration is not yet available, but it is on our roadmap for upcoming releases.


# dApp Developers


# Create a Single-Chain Application Reading From a Caff Node

This guide showcases how to use Espresso Caff Nodes to enable instant token swaps inside a single rollup chain. Specifically, we create a Swap application on Rari testnet where users can swap TokenA ↔ TokenB with fast confirmation from Espresso.

The flow is the following:

* User calls swap() on the smart contract.
* The Sequencer orders the transaction, Batch Poster posts to the Parent Chain.
* Espresso Caff Node immediately indexes the swap result and exposes it via API.
* The dApp frontend queries the Caff Node to show the updated balance instantly.

### Before You Begin

* Clone the repo: <https://github.com/enoldev/espresso-examples>, and move to the `instant-swap` folder.
* Install Foundry and ensure forge, cast, and anvil are available.
* Have ETH on Rari testnet (for deployment and gas fees).
* Ensure you have an Espresso Caff Node running (use the provided testnet endpoint or spin up your own).

### The Instant Swap Application

We’ll implement a very simple Automated Market Maker (AMM) smart contract:

* Users can deposit TokenA and TokenB into the pool.
* Users can call swapAForB(amount) or swapBForA(amount).
* The contract uses the constant product formula (x \* y = k) for swaps.

#### Inspect the Code

In order to test the AMM contract, we will need to mock the ERC20 tokens. The following contract is a very simple `MockERC20`:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract MockERC20 {
    string public name;
    string public symbol;
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);

    constructor(string memory _name, string memory _symbol) {
        name = _name;
        symbol = _symbol;
    }

    function mint(address to, uint256 amount) external {
        balanceOf[to] += amount;
        totalSupply += amount;
        emit Transfer(address(0), to, amount);
    }

    function transfer(address to, uint256 amount) external returns (bool) {
        require(balanceOf[msg.sender] >= amount, "ERC20: insufficient");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        uint256 allowed = allowance[from][msg.sender];
        require(allowed >= amount, "ERC20: allowance");
        require(balanceOf[from] >= amount, "ERC20: from balance");
        allowance[from][msg.sender] = allowed - amount;
        balanceOf[from] -= amount;
        balanceOf[to] += amount;
        emit Transfer(from, to, amount);
        return true;
    }
}
```

The AMM contract includes very simple logic for token swaps (TokenA and TokenB):

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

interface IERC20Minimal { // 1.
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

contract SimpleAMM {
    IERC20Minimal public tokenA;
    IERC20Minimal public tokenB;

    uint256 public reserveA; // 2.
    uint256 public reserveB;

    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB);
    event SwapAForB(address indexed trader, uint256 amountAIn, uint256 amountBOut);

    constructor(address _tokenA, address _tokenB) { // 3.
        tokenA = IERC20Minimal(_tokenA);
        tokenB = IERC20Minimal(_tokenB);
    }

    function _updateReserves() internal {
        reserveA = tokenA.balanceOf(address(this));
        reserveB = tokenB.balanceOf(address(this));
    }

    /// @notice Add liquidity (caller must approve this contract)
    function addLiquidity(uint256 amountA, uint256 amountB) external { // 4.
        require(amountA > 0 && amountB > 0, "zero amounts");
        require(tokenA.transferFrom(msg.sender, address(this), amountA), "transferA failed");
        require(tokenB.transferFrom(msg.sender, address(this), amountB), "transferB failed");
        _updateReserves();
        emit LiquidityAdded(msg.sender, amountA, amountB);
    }

    /// @notice Swap exact amountA for tokenB. Very simple pricing: amountOut = amountAIn * reserveB / (reserveA + amountAIn)
    function swapExactAForB(uint256 amountAIn, uint256 minBOut) external returns (uint256 amountBOut) { // 5.
        require(amountAIn > 0, "zero in");
        // transfer A in
        require(tokenA.transferFrom(msg.sender, address(this), amountAIn), "transferFrom A failed");

        // read reserves before adding amountAIn
        uint256 oldReserveA = reserveA;
        uint256 oldReserveB = reserveB;
        require(oldReserveA > 0 && oldReserveB > 0, "empty pool");

        // Simple constant product without fees:
        // amountBOut = amountAIn * reserveB / (reserveA + amountAIn)
        amountBOut = (amountAIn * oldReserveB) / (oldReserveA + amountAIn);
        require(amountBOut >= minBOut, "insufficient output amount");

        // send B to trader
        require(tokenB.transfer(msg.sender, amountBOut), "transfer B failed");

        // update reserves
        _updateReserves();

        emit SwapAForB(msg.sender, amountAIn, amountBOut);
    }
}
```

1. We declare a minimal ERC20 interface (`IERC20Minimal`) with only the functions we need: transferFrom, transfer, and balanceOf. This avoids importing the full OpenZeppelin ERC20 implementation, keeping the example lightweight.
2. The contract stores two ERC20 tokens (TokenA, TokenB) that can be swapped. `reserveA` and `reserveB` track the balances of each token held in the contract — representing the liquidity pool.
3. The constructor sets the token addresses for TokenA and TokenB that this AMM will support.
4. `addLiquidity` lets a user deposit both TokenA and TokenB into the pool. The caller must first approve the AMM contract to spend their tokens. Transfers the tokens in, updates reserves, and emits a LiquidityAdded event.
5. `swapExactAForB` allows a user to swap a specific amount of TokenA for TokenB. It first requires the user to approve TokenA spending. Then it pulls amountAIn into the contract

#### Deploy the Smart Contracts

The `script/Deploy.s.sol` file contains the logic to deploy two tokens: `TKA` and `TKB`, and the `AMM` contract. It also sends the tokens to the *deployer* address (the address used to deploy the contracts).

```bash
forge script script/Deploy.s.sol:Deploy \
  --rpc-url https://rari-testnet.calderachain.xyz/http \
  --private-key $PRIVATE_KEY \
  --broadcast -vv
```

After executing the script, the addresses of the deployer, tokens and AMM contract will be displayed in the logs. Create the environment variables.

```bash
export AMM_ADDR=0x
export TKA=0x
export TKB=0x
export DEPLOYER=0x
```

#### Test the App

Now, you can use the Rari Testnet Caff Node to test the application:

1. First, check the balance of the deployer address for each token. If the deployment script has been executed correctly, the deployer address must be funded with both tokens.

```bash
cast call $TKA "balanceOf(address)(uint256)" $DEPLOYER --rpc-url https://rari.caff.testnet.espresso.network
```

```bash
cast call $TKB "balanceOf(address)(uint256)" $DEPLOYER --rpc-url https://rari.caff.testnet.espresso.network
```

1. Then, execute the `approve(...)` function in the `TKA` smart contract (this is necessary to comply with the ERC20 standard).

```bash
cast send $TKA "approve(address,uint256)" $AMM_ADDR 1000000000000000000000 \
  --private-key $PRIVATE_KEY --rpc-url https://rari.caff.testnet.espresso.network
```

2. Now, you will be able to call the `swapExactAForB(...)` function:

```bash
cast send $AMM_ADDR "swapExactAForB(uint256,uint256)" 1000000000000000000 0 \ 
  --private-key $PRIVATE_KEY --rpc-url https://rari.caff.testnet.espresso.network
```


# Create a Crosschain Application Using Hyperlane

This guide showcases how to use Hyperlane to perform cross-chain message passing. Specifically, **this example uses Rari testnet and Appchain testnet** (along with the Hyperlane contracts deploy on each chain) to create a **Counter application**. It **assumes a Hyperlane validator and a relayer running, and listening**. The flow is the following:

1. The user triggers the “increment” of the counter on Rari (source chain).
2. Hyperlane relays the message to Appchain.
3. The counter is incremented on Appchain (destination chain).

In order for this to work, you will need a Hyperlane validator and relayer correctly configured to perform `Rari -> Appchain` message passing.

* **Rari Hyperlane Mailbox:** `0xb0bb23B185A7Ba519426C038DEcAFaB4D0a9055b`
* **Appchain Hyperlane Mailbox:** `0x4C58973d0Eb3CeB8aBfd933A1C6EE6f8EA178064`

### Before Your Begin

* Download the <https://github.com/enoldev/espresso-hyperlane-example> GitHub repository and open it in an IDE of you choice (e.g. VSCode)
* Have Foundry and all its dependencies installed (you can use other frameworks like HardHat, but Foundry is used in the following examples)
* Have ETH on Rari testnet. This is necessary to initiate transactions on the source chain.
* Have ETH on Appchain testnet. This is necessary to deploy the smart contract on the destination chain.

### The Counter Application

The simplest version of the application, which hardcodes most of the configuration parameters. In this case, the communication only happens from Rari to Appchain (Rari -> Appchain).

#### Understand the Flow

#### Inspect the Code

**There are two different versions of the Counter application: `src/Counter.sol` and `src/CounterBidirectional.sol`.**

**NOTE:** In the examples below the Caldera RPCs are used. It is also possible to use the Espresso Caff Nodes for testing, but here we assume the Espresso integration happens on the Hyperlane infra.

* The `espresso-app` folder contains the Foundry project. The `src` is used to store the smart contract source code (in this case, `Counter.sol`). The `scripts` folder contains the logic to deploy the smart contract on the blockchain.
* Open the `src/Counter.sol` file and review the code logic. For simplicity, the smart contract contains the logic of both source and destination chain. The `sendMessage` function is used on the source chain (Rari) to trigger the counter. Then, Hyperlane calls the `handle` function on the destination chain (Appchain)

```solidity
contract Counter {
    uint256 public number;
    
    // 1.
    address constant mailboxAddress = 0xb0bb23B185A7Ba519426C038DEcAFaB4D0a9055b;
    // 2.
    address constant mailboxAddressDestination = 0x4C58973d0Eb3CeB8aBfd933A1C6EE6f8EA178064;

		// --------------- SOURCE: Logic for sending message ---------------
    function sendMessage(address appDestinationAddress) public returns (bytes32) {
        uint32 destinationChainId = 4661; // 3.

        IMailbox mailbox = IMailbox(mailboxAddress); // 4.
        bytes32 appDestinationAddressBytes32 = addressToBytes32(appDestinationAddress); // 5.
        bytes32 messageId = mailbox.dispatch(destinationChainId, appDestinationAddressBytes32, bytes("Hello, world")); // 6.

        return messageId;
    }

    function addressToBytes32(address _addr) internal pure returns (bytes32) {
        return bytes32(uint256(uint160(_addr)));
    }

    // --------------- DESTINATION: Logic for receiving a message ----------------------
    function handle(uint32 _origin, bytes32 _sender, bytes calldata _body) external onlyMailbox { // 7.
        // Just increment the local counter when receiving the message
        number++;
    }
    
    modifier onlyMailbox() {
        require(msg.sender == mailboxAddressDestination);
        _;
    }
}
```

1. Hyperlane Mailbox address on the source chain (Rari). This is where the smart contract will send the message to trigger the counter.
2. Hyperlane Mailbox address on the destination chain (Appchain). This is where the message will get delivered.
3. Chain where the message will be delivered. 4661 corresponds to Appchain testnet.
4. In order to send a message to the source chain Hyperlane Mailbox, you import the Mailbox’s interface and initialize it with the actual smart contract address.
5. The address of the smart contract that will receive the message in the destination chain. In this example, the smart contract will be the Counter.sol contract deployed on the destination chain (because this contract is used for both sending and receiving messages).
6. Once you have the Mailbox initialized with the corresponding address, you execute the “dispatch” function with three parameters: the destination chain ID, the smart contract address and the message to deliver. In this example, the message is “Hello world” because you are only interested in triggering the function, not in the actual message.
7. The “handle” function is where Hyperlane will deliver the message in the destination chain. In this example, it increments the counter. The “onlyMailbox” modifier is used to ensure that only the Hyperlane Mailbox can execute the function.

#### Deploy the Smart Contracts

1. In a command-line terminal, run the following `forge` command to deploy the smart contract on Rari:

```bash
forge script script/Counter.s.sol \
  --rpc-url https://rari-testnet.calderachain.xyz/ \
  --private-key <PRIVATE-KEY> \
  --broadcast \
  --chain-id 1918988905
```

Replace with the actual private key of the address that you will use to deploy the contract. ​

2. The logs will provide you with the smart contract address on Rari. You will use this address to interact with the contract. Now, do the same to deploy on Appchain and save the resulting contract address.

```bash
forge script script/Counter.s.sol \
  --rpc-url https://appchaintestnet.rpc.caldera.xyz/http \
  --private-key <PRIVATE-KEY> \
  --broadcast \
  --chain-id 4661
```

#### Test the Application

1. To trigger the counter, you execute the `sendMessage` function with the Appchain’s smart contract address as parameter:

```solidity
cast send <SMART-CONTRACT-ADDRESS-ON-RARI> \
  "sendMessage(address)" <SMART-CONTRACT-ADDRESS-ON-APPCHAIN> \
  --rpc-url https://rari-testnet.calderachain.xyz/http \
  --private-key <PRIVATE-KEY> --chain 1918988905
```

2. Now, Hyperlane will pick up the message and relay it to the destination chain. To verify the counter, call the `number()` function on the Appchain’s contract.

```bash
cast call <SMART-CONTRACT-ADDRESS-ON-APPCHAIN> "number()" \
  --rpc-url https://appchain.caff.testnet.espresso.network
```

### The CounterBidirectional Application

A modified version of the `Counter.sol` contract that can be used for bidirectional communication. The Hyperlane Mailbox is passed in the constructor, so it can be used to pass messages **from Rari to Appchain** and **from Appchain to Rari**.

#### Deploy the Contracts

1. Deploy the contract on Rari:

```bash
MAILBOX=0xb0bb23B185A7Ba519426C038DEcAFaB4D0a9055b forge script script/CounterBidirectional.s.sol \
  --rpc-url https://rari-testnet.calderachain.xyz/http \
  --private-key <PRIVATE-KEY> \
  --broadcast \
  --chain-id 1918988905
```

You will get the smart contract address on Rari. Save this for later.

2. Deploy the contract on Appchain:

```bash
MAILBOX=0x4C58973d0Eb3CeB8aBfd933A1C6EE6f8EA178064 forge script script/CounterBidirectional.s.sol \
  --rpc-url https://appchaintestnet.rpc.caldera.xyz/http \
  --private-key <PRIVATE-KEY> \
  --broadcast \
  --chain-id 4661
```

You will get the smart contract address on Appchain. Save this for later.

#### Test the application

**Rari -> Appchain**

1. Trigger the counter on Rari chain by calling the `sendMessage(...)` function with the Appchain's smart contract data:

```bash
cast send <SMART-CONTRACT-ADDRESS-ON-RARI> \
  "sendMessage(uint32,address,bytes)" 4661 <SMART-CONTRACT-ADDRESS-ON-APPCHAIN> 0x48656c6c6f20776f726c64 \
  --rpc-url https://rari-testnet.calderachain.xyz/http \
  --private-key $PRIVATE_KEY \
  --chain 1918988905
```

2. Now, the Hyperlane infra will pick up the message and deliver it to Appchain. To get the number of the counter:

```bash
cast call <SMART-CONTRACT-ADDRESS-ON-APPCHAIN> "number()" \
  --rpc-url https://appchaintestnet.rpc.caldera.xyz/http
```

**Appchain -> Rari**

1. Trigger the counter on Appchain by calling the `sendMessage(...)` function with the Rari's smart contract data:

```bash
cast send <SMART-CONTRACT-ADDRESS-ON-APPCHAIN> \
  "sendMessage(uint32,address,bytes)" 1918988905 <SMART-CONTRACT-ADDRESS-ON-RARI> 0x48656c6c6f20776f726c64 \
  --rpc-url https://appchaintestnet.rpc.caldera.xyz/http \
  --private-key $PRIVATE_KEY \
  --chain 4661
```

2. Now, the Hyperlane infra will pick up the message and deliver it to Rari. To get the number of the counter:

```bash
cast call <SMART-CONTRACT-ADDRESS-ON-RARI> "number()" \
  --rpc-url https://rari-testnet.calderachain.xyz/http
```


# Deploy and Use Presto, a Crosschain Minting Framework

Presto is a crosschain framework that lets users mint NFTs on one chain (the destination chain) while paying on another (the source chain). Crucially, this requires **no manual bridging of liquidity**. Instead, the user simply pays on the source chain, and the destination chain is securely convinced that these funds have been paid.

In this tutorial, you will learn how to deploy the Presto framework.

## Before Your Begin

* Clone the [composables-xchain-mint GitHub repository](https://github.com/EspressoSystems/composables-xchain-mint). \*\*This the original GitHub repo, which contains the contracts, scripts and configurations files.
* Clone the [presto-deployment-example GitHub repository](https://github.com/enoldev), which contains simplified version the configuration files you will use.
* Install the [Hyperlane CLI](https://docs.hyperlane.xyz/docs/reference/developer-tools/cli).
* Install [Docker](https://docs.docker.com/engine/install/) and Docker Compose.
* Install [Foundry](https://getfoundry.sh/).

In this tutorial, you will work with two different repositories: `composables-xchain-mint` contains the source code of Presto, docs, and many utility scripts. `presto-deployment-example` tries to abstract the complexity by focusing only on the necessary to deploy a simple version of Presto. However, you will still need to compile the contracts from the original source code using Foundry.

## Presto Architecture

For a complete overview of Presto's architecture, please [check out this Medium article](https://docs.espressosys.com/network/guides/dapp/deploy-presto). It is important to get familiar with the flow and the contracts involved before you start deploying.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-da06de2e4090553acfa0c6c71fca08dc64f8199a%2Fpresto-architecture.png?alt=media" alt=""><figcaption></figcaption></figure>

## Deployment

**IMPORTANT:** In this tutorial, you will deploy a bidirectional minting flow (`source -> destination` and `destination -> source`). However, you may only deploy one path.

### Overview

Deploying Presto involves several components that work together across chains:

**- Hyperlane Core Contracts:** the standard contracts required by Hyperlane to relay messages across chains (e.g., Mailbox, ProxyAdmin, ISM). You can either deploy your own instances or use Hyperlane’s canonical deployments on each chain.

**- Hyperlane Warp Routes:** contracts used to bridge value via Hyperlane. They convert native tokens on the source chain into synthetic representations on the destination chain (i.e., a representation of the source chain’s native token).

**- Hyperlane Warp Routes Upgrade:** Presto relies on a modified version of the Warp Routes contracts. After deploying the standard Warp Routes, they must be upgraded to use the Espresso-specific implementations.

**- NFT Contract:** the NFT contract deployed on the destination chain. This should be a standard ERC721 implementation.

**- Hyperlane Validator and Relayer:** the off-chain Hyperlane services responsible for observing messages on the source chain and delivering them to the destination chain. These components perform the actual cross-chain message passing.

### `.env` file

Throughout the tutorial, you will need to add the required addresses to the `.env` of the `presto-deployment-example` repo. Later, you will copy the file to `composables-xchain-mint/contracts`. This will be necessary to run the scripts and Foundry commands later.

At this moment, complete the following env variables:

* `DEPLOYER_ADDRESS`: address that you will use to deploy the contracts.
* `DEPLOYER_PRIVATE_KEY`: the private key of the deployer.
* `SOURCE_CHAIN_RPC_URL`: source chain's RPC.
* `DESTINATION_CHAIN_RPC_URL`: destination chain's RPC.
* `SOURCE_CHAIN_ID`: source chain's ID.
* `DESTINATION_CHAIN_ID`: destination chain's ID.
* `VALIDATOR_ADDRESS`: the address used by the validator to sign messages.

### Hyperlane Core Contracts

**NOTE:** If Hyperlane is officially deployed in both chains, you can skip this part and use Hyperlane's canonical Mailboxes and other contracts. However, for the purpose of this tutorial, it is recommended that you deploy everything from scratch.

1. In the `hyperlane/chains` folder of `presto-deployment-example` you will find the configuration file for both source and destination chain (in this case, Rari and Apechain).
2. If you want to deploy on different chains, update accordingly the `metadata.yaml` file with the correct RPC and metadata for your chain. **Move this `metadata.yaml` files to your Hyperlane path (usually, at `~/.hyperlane/chains`). This is where Hyperlane looks for chain configurations**
3. In the `core-config.yaml`, replace `<YOUR_OWNER_ADDRESS>` with the actual address that you will use as owner of the Hyperlane contract. The `core-config.yaml` file is the configuration file for the Hyperlane core contracts.
4. Deploy the Hyperlane core contracts (source chain) using the previous configuration files.

```bash
hyperlane core deploy  --config hyperlane/chains/source/core-config.yaml
```

4. Deploy the Hyperlane core contracts (destination chain) using the previous configuration files.

```bash
hyperlane core deploy  --config hyperlane/chains/destination/core-config.yaml
```

For both deployments, you will get the addresses of the deployed contracts. Include those addresses in the `.env` file:

* `SOURCE_MAILBOX_ADDRESS`
* `DESTINATION_MAILBOX_ADDRESS`
* `SOURCE_PROXY_ADMIN_ADDRESS`
* `DESTINATION_PROXY_ADMIN_ADDRESS`

You can also find the addresses in the `addresses.yaml` file that was generated.

### Hyperlane Warp Routes

Now, you will deploy the standard Hyperlane Warp Routes contracts, which you will later upgrade with the Espresso-specific versions.

1. In the `deployments/warp_routes/ETH` directory, you will find the deploy configurations for the Warp Routes.
2. Update the configuration files (`destination-deploy.yaml` and `source-deploy.yaml`) to include your owner address, the relayer address and the proxy admin address.
3. From the root directory (`presto-deployment-example`), run the following command to deploy the routes

```bash
hyperlane warp deploy  --registry hyperlane
```

**NOTE:** Run it two times: one for the source chain and another one for the destination chain.

4. As a result, you will get two files, `source-config.yaml` and `destination-config.yaml`, which include the addresses of the contract that were deployed.
5. In the `destination-config.yaml` file, you will find the source chain's `HypNative` contract and the destination's chain `HypSynthentic` contracts.

```yaml
# Native contract on source chain
- addressOrDenom: "<SOURCE_NATIVE_TOKEN_ADDRESS>"
    chainName: source
    ...
    standard: EvmHypNative
    symbol: ECWETH
```

```yaml
# Synthetic contract address on destination chain
- addressOrDenom: "<DESTINATION_SYNC_TOKEN_ADDRESS>"
    chainName: destination
    ...
    standard: EvmHypSynthetic
    symbol: ECWETH
```

The `source-config.yaml` file contains the address for the opposite flow (destination to source).

Include the addresses in the `.env` file:

```bash
DESTINATION_NATIVE_TOKEN_ADDRES=
DESTINATION_SYN_TOKEN_ADDRES=

SOURCE_NATIVE_TOKEN_ADDRESS=
SOURCE_SYN_TOKEN_ADDRESS=
```

### NFTs

**IMPORTANT:** First, move to the `composables-xchain-mint/contracts` folder (in the source code repository) and copy the `.env` file of the `presto-deployment-example` repo. The environment variables will be used for the deployment of the contracts.

Deploy the NFT contracts. In this case, you will deploy a very simple `MockERC721` contract.

1. Move to the `composables-xchain-mint/contracts` folder and build the contracts with Foundry (`forge build`).
2. Deploy the Mock contract on the source chain:

```bash
forge create MockERC721 --rpc-url $SOURCE_CHAIN_RPC_URL --private-key $PRIVATE_KEY --broadcast --via-ir --constructor-args $DEPLOYER_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export SOURCE_MARKETPLACE_ADDRESS=
```

3. Deploy the Mock contract on the destination chain:

```bash
forge create MockERC721 --rpc-url $DESTINATION_CHAIN_RPC_URL --private-key $PRIVATE_KEY --broadcast --via-ir --constructor-args $DEPLOYER_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export DESTINATION_MARKETPLACE_ADDRESS=
```

### Upgrade Warp Contracts

Now, you will replace the standard `HypNative` and `HypERC20` contracts with the Espresso-modified versions.

#### Upgrade the Source -> Destination Path

1. Deploy the `EspHypNative` contract on the source chain:

```bash
forge create src/EspHypNative.sol:EspHypNative \
  --private-key $DEPLOYER_PRIVATE_KEY --broadcast --via-ir --rpc-url $SOURCE_CHAIN_RPC_URL \
  --constructor-args 1 $SOURCE_MAILBOX_ADDRESS
```

Include the resulting address in the `.env` file:

```bash
export SOURCE_NATIVE_ADDRESS=
```

2. Prepare the data for the upgrade:

```bash
INITIALIZE_DATA=$(cast calldata "initializeV2(uint256,uint32)" \
  $NFT_SALE_PRICE_WEI $DESTINATION_CHAIN_ID)
```

3. Perform the actual upgrade:

```bash
cast send $SOURCE_PROXY_ADMIN_ADDRESS \
  "upgradeAndCall(address,address,bytes)" \
  $SOURCE_NATIVE_TOKEN_ADDRESS $SOURCE_NATIVE_ADDRESS "$INITIALIZE_DATA" \
  --rpc-url $SOURCE_CHAIN_RPC_URL \
  --private-key $DEPLOYER_PRIVATE_KEY
```

4. Deploy the `EspHypERC20` contract:

```bash
forge create src/EspHypERC20.sol:EspHypERC20 --private-key $DEPLOYER_PRIVATE_KEY  --broadcast --via-ir --rpc-url $DESTINATION_CHAIN_RPC_URL --constructor-args 18 1 $DESTINATION_MAILBOX_ADDRESS --from $DEPLOYER_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export DESTINATION_ERC20_ADDRESS=
```

5. Prepare the data for the upgrade:

```bash
INITIALIZE_DATA=$(cast calldata "initializeV2(address,address,uint32,uint256)" \
  "$DESTINATION_MARKETPLACE_ADDRESS" \
  "$TREASURY_ADDRESS" \
  "$SOURCE_CHAIN_ID" \
  "$BRIDGE_BACK_PAYMENT_AMOUNT_WEI")
```

6. Perform the actual upgrade of the `EspHypERC20`:

```bash
cast send $DESTINATION_PROXY_ADMIN_ADDRESS \
  "upgradeAndCall(address,address,bytes)" \
  $DESTINATION_SYN_TOKEN_ADDRES $DESTINATION_ERC20_ADDRESS "$INITIALIZE_DATA" \
  --rpc-url $DESTINATION_CHAIN_RPC_URL \
  --private-key $DEPLOYER_PRIVATE_KEY \
  --value 0
```

#### Upgrade the Destination -> Source Path

1. Deploy the `EspHypNative` contract on the destination chain:

```bash
forge create src/EspHypNative.sol:EspHypNative \
  --private-key $DEPLOYER_PRIVATE_KEY --broadcast --via-ir --rpc-url $DESTINATION_CHAIN_RPC_URL \
  --constructor-args 1 $DESTINATION_MAILBOX_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export DESTINATION_NATIVE_ADDRESS=
```

2. Prepare the data for the upgrade:

```bash
INITIALIZE_DATA=$(cast calldata "initializeV2(uint256,uint32)" \
  $NFT_SALE_PRICE_WEI $SOURCE_CHAIN_ID)
```

3. Perform the actual upgrade:

```bash
cast send $DESTINATION_PROXY_ADMIN_ADDRESS \
  "upgradeAndCall(address,address,bytes)" \
  $DESTINATION_NATIVE_TOKEN_ADDRES $DESTINATION_NATIVE_ADDRESS "$INITIALIZE_DATA" \
  --rpc-url $DESTINATION_CHAIN_RPC_URL \
  --private-key $DEPLOYER_PRIVATE_KEY \
  --value 0
```

4. Deploy the `EspHypERC20` contract on the source chain:

```bash
forge create src/EspHypERC20.sol:EspHypERC20 --private-key $DEPLOYER_PRIVATE_KEY --broadcast --via-ir --rpc-url $SOURCE_CHAIN_RPC_URL --constructor-args 18 1 $SOURCE_MAILBOX_ADDRESS --from $DEPLOYER_ADDRESS
```

Add the resulting address to the `.env` file:

```bash
export SOURCE_ERC20_ADDRESS=
```

5. Prepare the data for the upgrade:

```bash
INITIALIZE_DATA=$(cast calldata \
  "initializeV2(address,address,uint32,uint256)" \
  "$SOURCE_MARKETPLACE_ADDRESS" \
  "$TREASURY_ADDRESS" \
  "$DESTINATION_CHAIN_ID" \
  "$BRIDGE_BACK_PAYMENT_AMOUNT_WEI")
```

6. Perform the actual upgrade:

```bash
cast send $SOURCE_PROXY_ADMIN_ADDRESS \
  "upgradeAndCall(address,address,bytes)" \
  $SOURCE_SYN_TOKEN_ADDRESS $SOURCE_ERC20_ADDRESS "$INITIALIZE_DATA" \
  --rpc-url $SOURCE_CHAIN_RPC_URL \
  --private-key $DEPLOYER_PRIVATE_KEY \
  --value 0
```

### Hyperlane Validator and Relayer

Now, you will need to set up the validator and relayers nodes, which are Docker images.

1. Move to the `validator-relayer-setup` folder, which contains all the files needed to deploy the infra.
2. Update the `config/agent.json` file with all the needed configurations (Hyperlane address, validator private key, chain IDs and RPC URLs).
3. Run the Docker Compose command:

```bash
docker compose up -d
```

## Front-end Integration

Once you have the contracts deployed, you can easily create a front-end application that listens for the specific contract events, which will allow you to track the progress of a mint.

### Source Chain

1. Initialize the mint on the `initiateCrossChainNftPurchase` function of `EspHypNative` contract. You will need to provide the receipt address of the NFT (on the destination chain). Note that the caller address must have enough funds to pay for the NFT and gas fees.
2. Track the `TransferRemote` event from the `EspHypNative` contract and the `DispatchId` event from the Hyperlane Mailbox. **Save the Hyperlane's message ID in your application's state**.

By tracking the events above, you will know if writing the message to the Hyperlane Mailbox has succeded. Then, the validator and relayer must pick up the message and write to the destination chain.

### Destination Chain

1. Listen for `Transfer` events on the NFT contracts. For every `Transfer` event, check out `ProcessId` event (from Hyperlane's mailbox) event, which contains the message ID received.
2. Match the `ProcessId` event with the message ID that you saved previously.


# Rollup Developers


# Nitro

Arbitrum integration with Espresso

Espresso has developed an integration with the Arbitrum Nitro tech stack that allows [Arbitrum Orbit](https://arbitrum.io/orbit) chains to easily integrate with Espresso. The first version of this integration enables Espresso confirmations for Orbit chains. The integration will later be updated with functionality to enable enhanced cross-chain interoperability, new forms of sequencing (i.e., decentralized/shared sequencing), and support for Espresso DA.

The first production release of the Espresso-Arbitrum Nitro integration is planned for January 2025, at which point Arbitrum Orbit chains will simply be able to download a Docker image that allows them to deploy onto Espresso (or ask their RaaS provider to do so on their behalf).

{% hint style="info" %}
If you just want to see the steps for getting up and running, you can [skip to the guide](https://docs.espressosys.com/network/guides/rollup-developers/nitro/migrate-orbit-chains-to-espresso).
{% endhint %}

## Integration overview

This integration makes minimal changes to the Arbitrum Nitro stack, and ensures that each batch processed by the rollup is consistent with HotShot-finalized blocks within its namespace.

To ensure that the batch has been finalized by HotShot, the following checks are performed:

1. **Namespace validation:** Ensure that the set of transactions in a rollup's batch corresponds to the correct namespace. Namespacing allows multiple chains to use Espresso’s fast confirmation layer simultaneously by associating each chain’s transactions with a unique namespace within HotShot blocks.
2. **Espresso block Merkle proof check:** Confirm that the rollup's batch maps to a valid HotShot block. Specifically, verify that the HotShot block associated with a rollup batch is a valid leaf in the Merkle tree maintained by the light client contract, which stores the state of HotShot on L1.
3. The sequencer calls `WriteSequencerMsg` on the transaction streamer.
4. The batcher fetches the message from the transaction streamer and submits the transaction to HotShot via the transaction streamer.
5. The batcher then calls the query API to check if the transaction has been finalized by HotShot.
6. Once the transaction is finalized, the batcher performs batch consistency checks.
7. The batcher signs the transaction calldata that would be sent to the `Sequencer Inbox` contract.
8. The `Sequencer Inbox` contract is modified to verify the batcher’s signature.

This approach involves running a Nitro node with only the batcher enabled, operating in a TEE environment (such as Intel SGX). The batcher will sign the transaction calldata. In case the TEE is broken, the batch poster can't impact the safety of the Orbit chain. It could, however, temporarily halt the chain's progress, thereby breaking liveness. Bridges relying on Espresso confirmations for faster settlement need to trust the TEE as well in this integration. In a future update, the dependency on TEEs will be removed entirely.


# Deploy a New Orbit Chain

### TL;DR

This guide provides a step-by-step approach to deploying a rollup or Arbitrum Orbit chain with the Espresso Network. It emphasizes testing the integration in a controlled environment and includes guidance for mainnet deployment. The instructions cover both local and cloud setups using Docker.

> **Note:** This guide assumes certain trust conditions and may not be suitable for production.

### Background

The Espresso Network is a confirmation layer that provides chains with information about the state of their own chain and the states of other chains, which is important for cross-chain composability. Espresso confirmations can be used in addition to the soft confirmations from a centralized sequencer, are backed by the security of the Espresso Network, and are faster than waiting for Ethereum finality (12-15 minutes).

#### How It Works

In a regular chain, the transaction lifecycle will look something like this:

1. A user transacts on an Arbitrum chain.
2. The transaction is processed by the chain's sequencer, which provides a soft-confirmation to the user, and the transactions are packaged into a block.
3. The sequencer, responsible for collecting these blocks, compressing, and submitting, submits the transactions to the base layer.
   * If the base layer is Arbitrum One or Ethereum, the transaction will take at least 12-15 minutes to finalize, or longer, depending on how frequently the sequencer posts to the base layer.
   * In this transaction lifecycle, the user must trust that the chain's sequencer provided an honest soft-confirmation and will not act maliciously. There are limited ways to verify that the sequencer and batcher acted honestly or did not censor transactions.

This reliance on trust is a strong assumption, and it's where the Espresso Network provides significant benefits. When the chain is integrated with the Espresso Network, the following enhancements occur:

* The sequencer provides a soft confirmation to the user, while the transactions are also sent to the Espresso Network to receive a stronger confirmation secured by Byzantine Fault Tolerance (BFT) consensus.
* A software component of the sequencer, called the batch poster (henceforth referred to as "batcher"), operates inside a Trusted Execution Environment (TEE) and must honor the Espresso Network confirmation. It cannot change the ordering or equivocate.
* This setup provides a strong guarantee that the transaction will ultimately be included and finalized by the base layer.

While the user must still trust that the chain's sequencer has provided an honest soft confirmation, the Espresso Network offers a stronger confirmation that holds the sequencer accountable and prevents it from equivocating or acting maliciously. The initial implementation of the batch poster is permissioned, and the user must trust that it will not reorder blocks produced by the sequencer.

For a comprehensive overview of how the Espresso Network integrates with your rollup—including details on the architecture, component interactions, and overall flow—please refer to [this integration guide](https://docs.espressosys.com/network/guides/using-the-espresso-network/using-the-espresso-network-as-an-arbitrum-orbit-chain).

#### Running Your Own

Integrating with the Espresso Network requires minimal changes to Arbitrum Nitro's existing rollup design. The Espresso Team has already done that, and in the following sections we will provide a comprehensive guide for running your own instance and building on Espresso!

#### Components

We model the rollup as a collection of three components:

* The sequencer
* The batcher
* The TEE contract (which we mock in this example)

### Deploying The Cloud Arbitrum Orbit Chain

Please note that these documents are to facilitate the deployment of a **testable** instance of the Arbitrum Orbit Chain with Espresso and should **not** be assumed to be production-ready infrastructure.

> **Note:** This guide is based on deploying your on own rollup on Arbitrum Sepolia. A dedicated section at the end of the guide outlines all the modifications needed for deployment on Arbitrum One.

#### 0. Install Requisite Dependencies

Ensure you have Node.js 16, yarn, foundry, git and build-essential tools installed on your system before proceeding.

#### 1. Deploy the Contracts

First, clone the contracts repository and set up the development environment:

```bash
git clone https://github.com/EspressoSystems/nitro-contracts.git
cd nitro-contracts
git checkout develop
```

Install the dependencies and build the project (this may take several minutes):

```bash
yarn install && forge install
yarn build:all
```

Create a `.env` file with the following variables:

```bash
ARBISCAN_API_KEY="YOUR_KEY_HERE"
DEVNET_PRIVKEY="YOUR_PRIVATE_KEY"
ESPRESSO_TEE_VERIFIER_ADDRESS="0x8354db765810dF8F24f1477B06e91E5b17a408bF"
```

You can get your Arbiscan API key by going to [here](https://arbiscan.io/myapikey). You need an account in order to get one. As for the private key, choose any address you want to use as the owner of the rollup. The amount required to deploy all the rollup contracts is arount 0.15 ETH.

This contract above is a mock TEE verifier that will be used to test the rollup by always returning true for any input. In this guide, we are thus assuming that the batch poster will not act maliciously because it is not operating inside a TEE.

#### 2. Configure Deployment

There is a config.example.ts file in the `scripts` folder that show you how the config file should look like. There is also a config.template.ts file that you can use to create your own config file.

1. Rename `config.template.ts` to `config.ts` 2.Update the following values in `config.ts`:

```bash
owner: "OWNER_ADDRESS",
chainId: ethers.BigNumber.from('YOUR_CHAIN_ID'), // Update with your desired chain ID
// Chain configuration
chainConfig: {
    "chainId": ChainID, // Update with the same chain ID,
    "InitialChainOwner": "YOUR_OWNED_ADDRESS",
}
validators: ["AN_OWNED_ADDRESS"],
batchPosterAddress: ["ANOTHER_OWNED_ADDRESS"],
batchPosterManager: "ANOTHER_OWNED_ADDRESS",
```

> **Important Notes:**
>
> * **chainId:** Ensure that the `chainId` values in both configuration fields are identical and unique.
> * **initialChainOwner:** The `initialChainOwner` should be the same as the `owner` address. Don't forget to modify this value at the end of the chain configuration.
> * **Validators/Stackers:** The `validators` array only requires one address, though you may add more if needed. These addresses need a minimal amount of funds (approximately 0.00003 ETH \~ ArbSepolia) each time they stake.
> * **Batch Poster:** The `batchPosterAddress` and `batchPosterManager` can be the same, but they should differ from the validators. A very small amount of funds (approximately 0.00001 ETH \~ ArbSepolia) is required for posting batches.

#### 3. Run Deployment

Execute the deployment script:

```bash
npx hardhat run scripts/deployment.ts --network arbSepolia
```

> **Note:** You can ignore the message "env var ESPRESSO\_LIGHT\_CLIENT\_ADDRESS not set..." - this is only needed for RollupCreator deployment.

**Add deployed rollup creator address to .env**

The previous deployment script will output the address of the rollup creator. Add this address to your `.env`:

```bash
ROLLUP_CREATOR_ADDRESS="DEPLOYED_ADDRESS"
```

**Deploy the Rollup Proxy Contract**

```bash
npx hardhat run scripts/createEthRollup.ts --network arbSepolia
```

> **Note:** You can keep the terminal opened with the logged addresses and the block number. This is the easiest way to find the deployed contract addresses when configuring the chain in the latest sections of this guide.

**Find the Deployed Contract Addresses**

To find the addresses of your deployed contracts:

1. Go to [Arbiscan Sepolia](https://sepolia.arbiscan.io/) (or [Arbiscan](https://arbiscan.io/) for mainnet)
2. Search for the address associated with your `DEVNET_PRIVKEY` from the `.env` file
3. In the transactions list, look for a transaction with the method name `Create Rollup`
4. Click on the transaction to view its details
5. Click on the "Logs(x)" tab and scroll down to the bottom of the page to find all deployed contract addresses.

> 📝 **Note:** You can also find most of the contract addresses in `espresso-deployments/arbSepolia.json`. The upgrade executor contract address from this JSON file will be needed for the next section.

### Configuring and Running the Chain

The docker configuration can be found in the [espresso-build-something-real](https://github.com/EspressoSystems/espresso-build-something-real) repository.

#### 1. Clone and Configure the Repository

```bash
git clone https://github.com/EspressoSystems/espresso-build-something-real
cd espresso-build-something-real
```

#### 2. Update Configuration Files

You'll need to modify two configuration files with the deployment addresses, keys, ids and rpc url from the previous steps:

**Files to update:**

* `config/full_node.json`
* `config/l2_chain_info.json`

**Required updates:**

* In `config/l2_chain_info.json`:
  * Set `chainId` under `chain-config` to match your rollup's chain ID
  * Set `InitialChainOwner` to the address of the rollup owner
  * Set the rollup smart contract addresses from the previous deployment
  * Update `deployed-at` to the block number where rollup proxy was created
* In `config/full_node.json`:
  * Add the rpc provider's arbitrum URL with your API key to the `url` field (e.g., infura, alchemy, etc.)
  * Set `id` under `chain` to match your rollup's chain ID
  * Update `private-key` for both stacker (validator) and batch poster addresses

> **Note:** Make sure you do not push your private keys to your repository if it is public. Or use environment variables to store your private keys.

#### 3. Run the Chain

For those seeking to evaluate their infrastructure and to get a clearer picture of what a "working" implementation looks like, we have made available a Docker Compose configuration for local development. The configuration included in this repository is ready to use as is – it will run your rollup locally. For cloud deployment details, see the Cloud Configuration [section](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#cloud-configuration) at the end of the guide.

```yaml
version: '2.2'
services:
  nitro:
    image: ghcr.io/espressosystems/nitro-espresso-integration/nitro-node:integration
    container_name: nitro-node
    ports:
      - "8547:8547"
      - "8548:8548"
      - "8549:8549"
    command: --conf.file /config/full_node.json
    volumes:
      - ./config:/config
      - ./wasm:/home/user/wasm/
      - ./database:/home/user/.arbitrum
    depends_on:
      - validation_node

  validation_node:
    image: ghcr.io/espressosystems/nitro-espresso-integration/nitro-node:integration
    container_name: validation_node
    ports:
      - "8949:8549"
    volumes:
      - ./config:/config
    entrypoint: /usr/local/bin/nitro-val
    command: --conf.file /config/validation_node_config.json
```

Start the chain using Docker:

```bash
docker compose up -d
```

**Understanding the Startup Process**

During startup, you'll see various logs and warnings. Here's what to expect and how to interpret them:

1. **Initial Staker Warnings**

   ```
   WARN [02-11|18:54:23.102] error acting as staker
   err="error advancing stake from node 5: block validation is still pending"
   WARN [02-11|18:55:00.911] Large gap between last seen and current block number, skipping check for reverts 
   last=122,990,253 current=122,990,485
   ```

   This is normal, this means that staker doesnt have any new nodes to stake on.
2. **Batch Validation Process**

   ```
   INFO [02-11|19:33:42.369] Batch validation status: hasBatchBeenValidated=false
   INFO [02-11|18:55:52.264] Fetching Merkle Root at hotshot height=1,173,100
   ```

   These logs show the batch poster working to validate and process transactions.
3. **Successful Batch Processing** When you see the following logs, it indicates successful batch processing:

   ```
   INFO [02-11|19:36:28.868] Batch validation status: hasBatchBeenValidated=true
   INFO [02-11|19:36:29.688] DataPoster sent transaction
   INFO [02-11|19:36:29.691] BatchPoster: batch sent
   ```

   > **Important Notes:**
   >
   > * Update to Batch posting can take from 1-30 minutes after a user has sent the transaction.
   > * Verify successful operation by checking the sequencerInbox contract on the Arbitrum Sepolia explorer.
   > * Occasional staker warnings occur when there are no new nodes to stake on.
4. **RPC Rate Limiting Issues**

   You may encounter errors indicating you've exceeded the RPC provider's rate limits:

   ```
   2025-02-27 11:12:54 INFO [02-27|16:12:54.607] rpc response method=eth_getLogs logId=199 err="Too Many Requests" result=null
   2025-02-27 11:12:54 WARN [02-27|16:12:54.609] error reading inbox err="Too Many Requests"
   ```

   These errors can occur when resyncing the entire rollup history after deleting the database folder or when using an RPC provider with strict rate limits.

   **Solutions:**

   * Adjust polling intervals in configuration files to reduce request frequency
   * Use one provider for initial sync, then switch to another for ongoing operations
   * Upgrade to a higher tier with your RPC provider

#### 4. Testing the Chain

To verify your chain is running correctly:

1. Check Confirmed Nodes by the Validator/Staker

```bash
cast call --rpc-url https://arbitrum-sepolia-rpc.publicnode.com YOUR_ROLLUP_PROXY_ADDRESS "latestConfirmed()(uint256)"
```

2. Test bridge functionality:

```bash
cast send --rpc-url https://arbitrum-sepolia-rpc.publicnode.com YOUR_INBOX_CONTRACT_ADDRESS 'depositEth() external payable returns (uint256)' --private-key YOUR_PRIVATE_KEY  --value 10000000000 -vvvv
```

> **Note:** Bridging transactions can take up to 15 minutes to finalize.

3. Verify your balance:

```bash
cast balance YOUR_PRIVATE_KEY_PUBLIC_ADDRESS --rpc-url http://127.0.0.1:8547
```

4. Test sending transactions:

```bash
cast send ANY_ADDRESS --value 1 --private-key YOUR_PRIVATE_KEY_WITH_FUNDS --rpc-url http://127.0.0.1:8547
```

For a more consistent test, you can also continuously send transactions to the rollup. This approach simulates a more realistic environment by continually submitting transactions, allowing you to see how the system handles ongoing activity. (See the next [section](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#transaction-flow-generator) for details.)

5. Check recipient balance:

```bash
cast balance ANY_ADDRESS --rpc-url http://127.0.0.1:8547
```

If successful, the recipient's balance should show 1 wei or the amount you sent if different.

#### Transaction Flow Generator

If you want to generate test transactions on your rollup, navigate to the `tx-generator` repository subfolder and follow the README instructions:

```bash
cd tx-generator
```

This script continuously generates transactions to help you evaluate your rollup and the Espresso Network.

### Hotshot Query Tool

You can also use this project in conjunction with the transaction generator to verify that the transactions you generate are properly submitted to Hotshot. By inputting the correct chain ID in the config, the [Hotshot Query Tool](https://github.com/EspressoSystems/hackathon-example)—a simple Go project—fetches and prints namespace transactions from the Hotshot query service. This tool sends HTTP requests and can be easily adapted for other API endpoints as needed.

### Deploying Your Rollup on Mainnet

To deploy your rollup on Arbitrum mainnet, update your configuration files with the appropriate parameters and follow the guide. Below are the key changes you need to make, along with references to the relevant sections of this guide:

* **TEE Verifier Address**:\
  Set the mock Espresso TEE verifier address to:
  * Mainnet: `0xE68c322e548c3a43C528091A3059F3278e0274Ed`
  * Testnet: `0x8354db765810dF8F24f1477B06e91E5b17a408bF`\
    Refer to [Deploy the Contracts](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#1-deploy-the-contracts).
* **Network Selection**:\
  Change the network in the nitro-contracts repository from `arbSepolia` to `arb1` when running smart contract and deployment scripts.\
  Refer to [Run Deployment](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#3-run-deployment).
* **Batch Poster Settings**:\
  Update the batch-poster configuration in the `config/full_node.json` file by:
  * Changing the hotshot URL to `https://query.main.net.espresso.network/v0`
  * Setting the light-client address to `0x47495bb99CCCBB1bda9F15b32B69093137F886Db`.\
    Refer to [Update Configuration Files](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#2-update-configuration-files).
* **Parent Chain ID**:\
  In `l2_chain_info.json`, change the `parent-chain-id` from `421614` to `42161` and optionally adjust the `chain-name`.\
  Refer to [Update Configuration Files](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#2-update-configuration-files).
* **RPC Endpoint**:
  * In `full_node.json`, update the RPC URL to the mainnet endpoint.
  * When testing, change the RPC URL from `https://arbitrum-sepolia-rpc.publicnode.com` to `https://arbitrum-one-rpc.publicnode.com`.\
    Refer to both [Update Configuration Files](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#2-update-configuration-files) and [Testing the Chain](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#4-testing-the-chain).

Apply these modifications to ensure your rollup is properly configured for mainnet deployment.

### Cloud Configuration

> **Info:** If you want to get up and running with this and you already know about cloud configuration, you can take the docker compose file and modify it as needed. If you aren't familiar with cloud environments, read on. (Note: This setup is for AWS, but it should work with any cloud.)

#### Booting A Chain on EC2

The first step is to launch an ec2 instance, which is a simple process. First, go into the console and either search for ec2, or select it from the quick select if you've used it before.

From here, we can configure the EC2 launch configuration. You can leave everything default, but feel free to change the settings if you've done this before. Under `Instance Type` you can select `t3.medium` or `t3.large`, but any cloud instance with at least 4 gigabytes of RAM and 2 CPU cores should be sufficient.

> **Info:** Please note that in our testing `t3.medium` seems to meet the requirements, but if you encounter instability, you might need to upgrade to the larger instance.

From here, make sure you configure your key pair, otherwise you will **not** have SSH access to the machine. You can use the auto generated security group for the instance. Make sure you allow SSH traffic as well. The following image should mostly reflect your configuration:

> **Security Note:** Keep your key pair secure and do not share it with others. Ensure that the permissions on your key file are set to be readable only by you (e.g., `chmod 400 your-key.pem`).

#### Setting up CloudWatch logging (Optional)

If you want to have access to the logs of your rollup without having to each time SSH into the instance, you can enable CloudWatch logging and send the logs to a CloudWatch log group. You will then be able to view the logs in the CloudWatch console. Follow the steps below to enable this:

1. **Create IAM Role**:

* In the advanced details section, create a new IAM profile to enable logging if you don't have one already.
* Click on **Create role** then select **EC2** as the use case in the next screen.
* Click "Next" then select the **AmazonAPIGatewayPushToCloudWatchLogs** policy in the next screen.
* Name your role in the next screen (e.g., "CloudWatchLogsRole") and create the role.

2. **Attach Role to EC2**:

* Return to the EC2 instance creation screen.
* In Advanced settings, select the role you just created and click **Launch instance**.

3. **Create Log Group**:
   * Navigate to the CloudWatch console and create two log groups for your rollup:
   * You can name them both `nitro-node-logs` and `validation-node-logs` or something similar. This is the name we give them in the docker-compose.yml file at the following step.
4. **Update Docker Configuration**: Modify your docker-compose.yml to include CloudWatch logging:

   ```yaml{19-24,42-47}
   version: '2.2'
   services:
     nitro:
       image: ghcr.io/espressosystems/nitro-espresso-integration/nitro-node:integration
       container_name: nitro-node
       ports:
         - "8547:8547"
         - "8548:8548"
         - "8549:8549"
       command: --conf.file /config/full_node.json
       volumes:
         - ./config:/config
         - ./wasm:/home/user/wasm/
         - ./database:/home/user/.arbitrum
       depends_on:
         - validation_node
       # ===== CloudWatch Configuration Start =====
       logging:
         driver: "awslogs"
         options:
           awslogs-region: "us-east-2" # Update to your EC2 instance's region
           awslogs-group: "nitro-node-logs"
           awslogs-stream: "nitro-node"
       # ===== CloudWatch Configuration End =====

     validation_node:
       image: ghcr.io/espressosystems/nitro-espresso-integration/nitro-node:integration
       container_name: validation_node
       ports:
         - "8949:8549"
       volumes:
         - ./config:/config
       entrypoint: /usr/local/bin/nitro-val
       command: --conf.file /config/validation_node_config.json
       # ===== CloudWatch Configuration Start =====
       logging:
         driver: "awslogs"
         options:
           awslogs-region: "us-east-2" # Update to your EC2 instance's region
           awslogs-group: "validation-node-logs"
           awslogs-stream: "validation-node"
       # ===== CloudWatch Configuration End =====
   ```

   > 📝 **Note:** Make sure to update the `awslogs-region` to match your EC2 instance's region.

#### Preparing Your Environment

1. **Move Key to .ssh Folder**:
   * Move your key from the downloads folder or any other folder to the `.ssh` folder:

     ```bash
     mv ~/Downloads/'your-key.pem' ~/.ssh/
     ```
2. **Test Your Connection**:
   * Use `ping` to test your connection with the IPv4 address:

     ```bash
     ping 'your-host'
     ```
   * If you encounter "Connection refused" or "Communication prohibited by filter," try using a different network, like mobile data.
3. **Connect to Your EC2 Instance**:
   * Run this command to connect to your EC2 instance using your key:

     ```bash
     ssh -i ~/.ssh/'your-key.pem' ec2-user@'your-host'
     ```

     > **Note:** Replace `your-host` with either the public DNS or IP address of your EC2 instance.

#### Transferring Files to Your EC2 Instance

1. **Create Config Folder**:
   * On another terminal, run the following to create a config folder on your instance:

     ```bash
     ssh -i ~/.ssh/'your-key.pem' ec2-user@'your-host' "mkdir -p ~/rollup/config"
     ```

     > **Note:** For this first step, you can also run the mkdir command from the instance terminal.
2. **Move Config Files to Instance**:
   * From the root of your git repo, transfer your config files to the instance's config folder:

     ```bash
     scp -i ~/.ssh/'your-key.pem' config/* ec2-user@'your-host':~/rollup/config/
     ```
3. **Move Docker File to Instance**:
   * Similarly, transfer the Docker Compose file to your instance:

     ```bash
     scp -i ~/.ssh/'your-key.pem' docker-compose.yml ec2-user@'your-host':~/rollup/
     ```

#### Configuring Docker

From inside your instance, install docker with the following steps:

```bash
sudo yum update -y && \
    sudo yum install -y docker && \
    sudo service docker start && \
    sudo usermod -aG docker ec2-user
```

You can now log out and back in, and your user, ec2-user, should have Docker access without needing sudo. The last thing we need is Docker Compose. Unfortunately, at the time of writing, Amazon Linux 2023 has an older distribution of Docker, which does not yet support the compose subcommand. To access Docker Compose, you need to download it by executing the following steps:

> **Note:** Before continuing, exit and reconnect to your instance by running `exit` in the terminal.

```bash
# First, pull docker compose
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# Then, add execute permissions
sudo chmod +x /usr/local/bin/docker-compose

# Verify
docker-compose version
```

#### Running Docker Compose

1. **Connect to EC2 Instance**:
   * Return to the terminal connected to your EC2 instance, or reconnect if you have logged out. You can find the connection command in the [Preparing Your Environment](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#preparing-your-environment) section.
2. **Run Docker Compose**:
   * From the rollup folder, execute the following command to start your services:

     ```bash
     docker-compose up
     ```

     > **Note:** You can add the `-d` flag to run the containers in the background.
3. **Handle Permission Errors**:
   * If you encounter a permission error like:

     ```
     nitro-node | Fatal configuration error: unable to create chain directory: mkdir /home/user/.arbitrum/local: permission denied
     ```
   * Create the necessary folders and set permissions:

     ```bash
     mkdir -p database wasm
     sudo chown -R 1000:1000 database wasm
     ```
   * This gives Docker container's user permission to write to these directories.

#### Testing the Connection

You can now that the connection to your rollup by for example checking your balance:

```bash
cast balance 'your-address' --rpc-url http://your-host:8547
```


# Deploy Your Own Orbit Chain Caff Node

This guide introduces a Go project that reads from the Espresso Network and monitors for specific transactions, filtering them by value and sender address. You can imagine this project as being a bot that alerts you when your wallet gets drained.

## Overview

The hackathon-example [repository](https://github.com/EspressoSystems/hackathon-example/) provides a foundation for building applications that interact with the Espresso Network. You can use this project as a starting point for developing applications or more sophisticated monitoring and analysis tools.

## Prerequisites

Before proceeding with this guide, you'll need:

* A running Arbitrum Orbit chain integrated with the Espresso Network, either locally or in the cloud
* Access to a Caffeinated node, which serves as your interface to the Espresso Network

For convenience, the Caffeinated node setup is available in the same espresso-build-something-real [repository](https://github.com/EspressoSystems/espresso-build-something-real) as the previous guide, under the `caff-node` directory. If you've already deployed your rollup following the earlier instructions, you're ready to proceed with this monitoring project.

## The Caffeinated Node

The Caffeinated node is a full node and your interface to the Espresso Network. It processes Hotshot blocks, maintains state, and provides a JSON-RPC endpoint for monitoring transactions. The monitoring tool we'll build uses these capabilities to track specific transactions based on sender address and value.

## Setup Instructions

Navigate to the [espresso-build-something-real](https://github.com/EspressoSystems/espresso-build-something-real) repository and follow these steps to configure and run your caffeinated node locally:

#### 1. Update the config

Update the `caff-node/config/caff_node.json` file with:

```json
{
  "chain": {
      "id": 1000000,
      ...
  },
  ...
  "next-hotshot-block": 9999,
  "namespace": 1000000,
  "parent-chain-node-url": "WEBSOCKET_ARBITRUM_SEPOLIA_RPC_URL",
}   
```

* **Namespace and Chain ID**: Both should match your rollup chain ID. Update both values.
* **Next Hotshot Block**:
  * Find the latest Hotshot block height at <https://explorer.decaf.testnet.espresso.network/>. Update this value just before running the Caffeinated node to avoid resyncing the entire chain.
* **Parent Chain Node URL**: Enter your Arbitrum Sepolia or mainnet RPC URL (must be a WebSocket URL).

  > 📝 **Note:** We recommend using a different RPC URL for the caff node to avoid hitting rate limits (free tier should be enough).

#### 2. Set Up and Run

1. **Copy Configuration Files**:

   * Copy the `l2_chain_info.json` file into the `caff-node/config` folder

   * Copy the `database` folder from the repository root to the `caff-node` directory.

   > 📝 **Note:** Make sure the node is not running when you do this.
2. **Start the Services**:
   * First, run `docker compose up` at the root of the repository.
   * Then, run `docker compose up` in the `caff-node` folder.

## Setting Up the Example Project

Instructions can be found on the [README](https://github.com/EspressoSystems/hackathon-example/blob/main/README.md) to set this project up but we will go over the steps here in more detail.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/EspressoSystems/hackathon-example --recursive
   cd hackathon-example
   ```

   If you've already cloned the repository without the `--recursive` flag (e.g., through your IDE), you can fetch the go-ethereum submodule with:

   ```bash
   git submodule update --init --recursive
   ```

   The reason we are doing this is because we want to use a forked version of the go-ethereum library from offchainlabs to interact with the caffeinated node.
2. **Install Dependencies**

   ```bash
   go mod tidy
   ```
3. **Configure the Application**

   You should configure the following settings in the `/config/config.json` file:

   ```json
   {
       "caff_node_url": "http://YOUR_HOST:8550",
       "polling_interval": 1,
       "value": 1,
       "from": "0x0000000000000000000000000000000000000000"
   }
   ```

   * **caff\_node\_url**: Change `YOUR_HOST` to either:
     * `localhost` if running locally.
     * Your EC2 instance's IPv4 address if running on the cloud.

   * **polling\_interval**:
     * Controls how frequently the application checks for new transactions.
     * Adjust based on your needs, but keep it low enough to avoid missing transactions.

   * **value**: Set the minimum transaction value (in wei) that you want to monitor.

   * **from**: Enter the Ethereum address you want to monitor transactions from.

   > 📝 **Note:** The docker setup exposes the Caffeinated node on port 8550. 📝 **Note:** The code divides the polling value by 2 to determine the actual polling interval.
4. **Run the Application** At the root of the repository, run the following command:

   ```terminal
   go run .
   ```

   This will start the application and monitor the Espresso Network for transactions that match your rollup and the specified criteria.

   > 📝 **Note:** This monitoring tool simply logs matching transactions to the console. You can extend it to perform more complex actions when transactions are detected.
5. **Send Transactions**

   Now that you have both your rollup and Caffeinated node running, you can send test transactions to your rollup. You have two options:

   * Use a simple command-line transaction:

   ```bash
   cast send ANY_ADDRESS --value 1 --private-key YOUR_PRIVATE_KEY_WITH_FUNDS --rpc-url http://127.0.0.1:8547
   ```

   * Use the transaction generator script in the `espresso-build-something-real/tx-generator` directory, which can continuously generate test transactions. See the [README](https://github.com/EspressoSystems/espresso-build-something-real/blob/main/tx-generator/README.md) in that repository for detailed instructions.

   These transactions will be processed by your rollup and should appear in the monitoring tool's output if they match your configured criteria.

   > 📝 **Note:** The block number shown in the logs is not the latest block height of the espresso network but the latest block processed by your rollup.

## Troubleshooting

If you've followed the guide carefully and paid attention to the notes, you shouldn't encounter many issues. However, here are solutions to some common problems:

#### Normal Warning Messages

The following logs are normal and not cause for concern:

```bash
2025-02-27 13:29:11 WARN [02-27|18:29:11.645] unable to get next message               err="no message found"
2025-02-27 13:29:13 WARN [02-27|18:29:13.273] failed to fetch the transactions         err="no majority consensus reached"
```

These messages simply indicate that the node is listening to the rollup but there are no new transactions to process.

#### Transaction Detection Messages

The following logs indicate that the node is correctly listening to the rollup and has detected a new transaction:

```bash
2025-03-06 INFO [03-06|21:38:50.671] Added message to queue message=487
...
2025-03-06 INFO [03-06|21:38:50.765] Now processing hotshot block "block number"=2,056,058
...
2025-03-06 INFO [03-06|21:38:52.099] Initial State lastBlockHash=6033cf..9f3bef lastBlockStateRoot=35ca02..3749dc
2025-03-06 INFO [03-06|21:38:52.103] Produced block block=751811..23907a blockNumber=487 receipts=2
```

#### Syncing to the Latest Hotshot Block

If you see many logs like these at startup, your Caffeinated node is simply syncing to the latest Hotshot block:

```bash
2025-02-27 11:22:32 INFO [02-27|16:22:32.835] No transactions found in the hotshot block "block number"=1,850,985
2025-02-27 11:22:32 INFO [02-27|16:22:32.835] Now processing hotshot block             "block number"=1,850,986
```

**Solution**: To reduce syncing time, update the `next-hotshot-block` value in `caff-node/config/caff_node.json` to the latest block height from the [espresso explorer](https://explorer.decaf.testnet.espresso.network/) before starting the node.

#### Restarting Docker Containers

If you stop and restart both your rollup and Caffeinated node, you might need to recopy the database folder to your `/caff-node` folder. Failing to do this can cause your rollup and Caffeinated node to fall out of sync.

> 📝 **Note:** This can result in transactions not being detected by the monitoring tool.

#### Rate Limiting Issues

If you're experiencing rate limiting from your RPC provider, you can adjust polling intervals in the configuration files:

```json
// In caff-node/config/caff_node.json
"caff-node-config": {
    "hotshot-polling-interval": "1ms",
    "retry-time": "2s",
},

// In config/full_node.json
"staker": {
    "staker-interval": "120s",
    "make-assertion-interval": "120s",
}
"parent-chain-reader": {
    "poll-interval": "120s"
}
```

Increasing these intervals will reduce the frequency of RPC calls, helping you stay within rate limits.

#### Monitoring Issue

If you don't see logs indicating successful block processing, your Caffeinate node might not be properly connected to or in sync with the rollup. This often happens when the database directory isn't properly configured. You should see logs like:

```bash
2025/03/01 10:00:00 Searching for transaction at last processed block number: 123456
```

If these logs are missing, check that:

* Your repository structure is correct.
* The docker-compose.yml file is properly configured and indented.
* Your caffeinated node is properly syncing with the rollup.

## Update for Listening to Mainnet

To ensure your setup is ready for Arbitrum and Espresso mainnet, you'll need to make the following changes in addition to those described in the `Deploying Your Rollup on Mainnet` [section](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#deploying-your-rollup-on-mainnet) in the previous guide:

1. **Update Caffeinated Node Configuration**: In `caff-node/config/caff_node.json`, update the following values:

   ```json
   parent-chain-node-url: "WEBSOCKET_ARBITRUM_MAINNET_RPC_URL",
   espresso-tee-verifier-addr: "0xE68c322e548c3a43C528091A3059F3278e0274Ed",
   hotshot-url: "https://query.main.net.espresso.network/v0"
   ```

   > 📝 **Note:** Make sure to use a WebSocket URL (starting with `wss://`) for your Arbitrum mainnet RPC provider.
2. **Update Hotshot Block Height**: Find the latest Hotshot block height at the [mainnet espresso explorer](https://explorer.main.net.espresso.network/) and update the `next-hotshot-block` value in your configuration.

## Deploying your caffeinated node on the cloud

Similarly to the preceding guide, the next step would be to deploy your caffeinated node on the cloud. You can follow the instructions in the `Cloud Configuration` [section](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#cloud-configuration) of the previous guide for building your EC2 instance and installing the required docker configs. Here are the steps to migrate your caffeinated node to the cloud:

1. Start off from the `Set Up and Run` [section](#2-set-up-and-run) of this guide. The steps on how to run your rollup in the cloud have been covered in the previous guide. You can use the same rollup config files.
2. **Create and configure the caff-node directory structure on your EC2 instance**:

   ```bash
   # Create directory structure
   ssh -i ~/.ssh/your-key.pem ec2-user@YOUR_HOST "mkdir -p ~/rollup/caff-node/{config,database,wasm}"

   # Set permissions for directories that need write access
   ssh -i ~/.ssh/your-key.pem ec2-user@YOUR_HOST "sudo chown -R 1000:1000 ~/rollup/caff-node/database ~/rollup/caff-node/wasm"
   ```

   > 📝 **Note:**
   >
   > * The `config` directory remains owned by ec2-user for configuration files
   > * `database` and `wasm` directories need write permissions for the Docker container user (1000:1000)
3. **Transfer the config files to your EC2 instance**: From the root of the repository, run the following command:

   ```bash
   scp -i ~/.ssh/your-key.pem -r ./caff-node/config/* ec2-user@YOUR_HOST:~/rollup/caff-node/config/
   ```
4. **Copy the database from your rollup to the caff-node directory**: From outside the EC2 instance, run the following command:

   ```bash
   ssh -i ~/.ssh/your-key.pem ec2-user@YOUR_HOST "cp -r ~/rollup/database ~/rollup/caff-node/database"
   ```

   Or from inside the EC2 instance, run the following command:

   ```bash
   cp -r ~/rollup/database ~/rollup/caff-node/database
   ```

   > 📝 **Note:** Make sure you sync and stop the rollup service before copying the database. This step is crucial and is often the cause of issues.
5. **Enable CloudWatch Logging (Optional)**:

   If you want to monitor your caffeinated node logs in CloudWatch:

   * Create a log group for your caffeinated node in the CloudWatch console, similar to how you created log groups in the `Setting up CloudWatch logging` [section](https://github.com/EspressoSystems/gitbook/blob/main/guides/rollup/nitro/running-the-espresso-network-with-arbitrum-cloud.md#setting-up-cloudwatch-logging-optional) of the previous guide.
   * Modify your `caff-node/docker-compose.yml` file to include CloudWatch logging:

     ```yaml
      version: '2.2'
      services:
      caff_node:
         image: ghcr.io/espressosystems/nitro-espresso-integration/nitro-node@sha256:bf63374a00a5d6676ca39af79ac4b0f053128cb7438bcdaa746dba6656c12658
         container_name: caff_node
         ports:
            - "8550:8547"
            - "8551:8548"
            - "8552:8549"
         command: --conf.file /config/caff_node.json
         volumes:
            - ./config:/config
            - ./wasm:/home/user/wasm/
            - ./database:/home/user/.arbitrum
         logging:
           driver: "awslogs"
           options:
             awslogs-region: "us-east-2" # Update to your EC2 instance's region
             awslogs-group: "caff-node-logs"
             awslogs-stream: "caff-node"
     ```

     > 📝 **Note:** Make sure to update the `awslogs-region` to match your EC2 instance's region.

   Whether you enabled logging or not, you can now transfer the `docker-compose.yml` file inside your instance. From outside the EC2 instance, run the following command:

   ```bash
   scp -i ~/.ssh/your-key.pem ./caff-node/docker-compose.yml ec2-user@YOUR_HOST:~/rollup/caff-node/
   ```

   > 📝 **Note:** Your rollup folder structure should be very similar to the repository structure of the espresso-build-something-real [repository](https://github.com/EspressoSystems/espresso-build-something-real). 📝 **Note:** You can always update the docker-compose.yml file using nano or by copying again the file from the repository.
6. **Connect to your EC2 instance and start the services**:

   ```bash
   ssh -i ~/.ssh/your-key.pem ec2-user@YOUR_HOST
   cd rollup
   docker-compose up -d
   cd caff-node
   docker-compose up -d
   ```

> 📝 **Note:** Do not forget to update the latest hotshot block height in the `caff-node/config/caff_node.json` from the [espresso explorer](https://explorer.main.net.espresso.network/) to avoid resyncing the entire chain. 📝 **Note:** You can stop the services by running `docker compose down` in the `rollup` and `caff-node` directories. 📝 **Note:** You can remove the `-d` flag to run see the logs of the containers in the terminal.

## Run the monitoring application

Once your caffeinated node is running on the cloud, update the `caff_node_url` in the hackathon-example repository's config to point to your EC2 instance's public IP address. Then try running the application with the updated config.

**Configuring Network Access**

If you encounter connection timeouts when trying to access your EC2 instance (e.g., `dial tcp YOUR_HOST:8550: i/o timeout`), you need to open the required ports in your EC2 security group:

1. In the AWS EC2 Console, navigate to your instance
2. Select the "Security" tab in the bottom panel
3. Click on the security group ID (e.g., "sg-0123456789abcdef")
4. In the security group page, select the "Inbound rules" tab
5. Click "Edit inbound rules"
6. Add two new rules:
   * Type: Custom TCP, Port range: 8547, Source: Custom 0.0.0.0/0 (or your IP for better security)
   * Type: Custom TCP, Port range: 8550, Source: Custom 0.0.0.0/0 (or your IP for better security)
7. Click "Save rules"

This enables external connections to your Caffeinated node (port 8550) and rollup node (port 8547).


# Migrate an Existing Orbit Chain to Espresso

## Espresso Nitro Integration

{% hint style="info" %}
You may wish to familiarize yourself with the [security audits](https://github.com/EspressoSystems/espresso-audits/blob/main/external-reviews/EspressoNitroIntegration-2025.pdf) for this integration.
{% endhint %}

The target audience for this document are developers who would like to migrate an existing Arbitrum Orbit chain to use Espresso's Global Confirmation Layer (GCL). The document should also be interesting for developers who are thinking of deploying a new Arbitrum Orbit chain that uses Espresso's GCL.

The goal of this document is to describe how to migrate an Arbitrum Orbit chain to using Espresso's global confirmation layer for fast confirmations. By leveraging Espresso's fast confirmations, a rollup will only accept a batch after it has been finalized by Espresso. This integration ensures that each batch processed by the rollup is consistent with HotShot-finalized blocks within its namespace.

### Quickstart

The quickest way to get familiar with what the migration entails is to run through our [migration test](https://github.com/EspressoSystems/nitro-testnode/blob/integration/espresso-tests/migration-test.bash).

The script creates up an ephemeral Nitro chain on the local computer and migrates it to using Espresso's Global Confirmation Layer (also running locally on the computer). This test mocks out the TEE part by using a mocked TEE verifier contract and configured the batch poster to bypass the TEE interactions. Thereby it's possible to run through the migration locally, without requiring a special CPU and extra software to support the TEE.

{% hint style="warning" %}
For a safe production deployment the TEE is required and the real TEE verifier contract must be deployed.
{% endhint %}

The test requires [Docker](https://docs.docker.com/engine/install/), [Foundry](https://book.getfoundry.sh/getting-started/installation), [Yarn](https://classic.yarnpkg.com/lang/en/docs/install), `openssl` and `jq` to be installed.

For convenience the nix package manager can take care of installing all dependencies except for Docker. Nix can be installed by running

```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```

To run the test first some setup:

```bash
git clone --recursive https://github.com/EspressoSystems/nitro-testnode
cd nitro-testnode
git checkout integration
nix develop # omit if you have foundry, yarn, jq, openssl installed already
```

Now you can run the test itself.

```bash
espresso-tests/migration-test.bash
```

You may need to run the following command to ensure the submodules are initialized:

```bash
git submodule update --init --recursive
```

You should see substantial output. The first time you run this, it can take up to 15-20 minutes due to initial setup steps like installing dependencies. Subsequent runs should take less than 10 minutes.

After some time, if successful, you should see **Migration successfully completed!**.

> **⚠️ Warning:** If you see "Waiting for confirmed nodes" logs for more than 60 seconds, it's recommended to restart the process.

It's encouraged to read through the [migration test](https://github.com/EspressoSystems/nitro-testnode/blob/integration/espresso-tests/migration-test.bash) to get an idea of all the steps involved and what information is required for each step. For the real migration using `.env` files instead of environment variables to provide the necessary inputs may be more convenient.

Once familiar, you might run some commands to further your understanding. Transfer some eth, for example:

```bash
cast send $RECIPIENT_ADDRESS --value 1ether --rpc-url $CHILD_CHAIN_RPC_URL --private-key $PRIVATE_KEY
```

### Assumptions

Before attempting a migration please verify that the assumptions listed here make sense for your nitro deployment. If not, please get in touch with us via our [contact form](https://y3at7jy5knf.typeform.com/to/KgayxNsX?typeform-source=www.espressosys.com).

1. The Orbit chain to be migrated is using vanilla Nitro stack, or Celestia DA via the [Celestia fork of nitro](https://github.com/celestiaorg/nitro). If your Orbit chain is using Celestia for DA you need to use the `celestia-integration` branches of Espresso's nitro forks.
2. You are able to run the batch poster in an SGX TEE environment. This is required to provide TEE attestations that the L2 transactions have been finalized by Espresso. These attestations are verified in the TEE verifier smart contract on the parent chain as part of the batch submission.

### Production Setup Requirements

For production migrations, you will need the following system requirements (note: these are not needed for running the test migration):

* SGX
* Gramine
* [16GB RAM](https://docs.arbitrum.io/run-arbitrum-node/run-full-node#minimum-hardware-configuration)

You will also need these Espresso projects. Depending on whether you use celestia DA or not, you will need either the `integration` branch or `celestia-integration` branch. Please take the time to review each project's respective README.

* <https://github.com/EspressoSystems/nitro-espresso-integration>
* <https://github.com/EspressoSystems/nitro-contracts>
* <https://github.com/EspressoSystems/nitro-testnode>
* <https://github.com/EspressoSystems/orbit-actions>
* <https://github.com/EspressoSystems/gsc>

As well as [Espresso's nitro-node](https://github.com/EspressoSystems/nitro-espresso-integration/pkgs/container/nitro-espresso-integration%2Fnitro-node) docker image:

```
 ghcr.io/espressosystems/nitro-espresso-integration/nitro-node:v3.3.2-fcd633f
```

## Migration Flow

{% hint style="info" %}
This flow is more precisely defined in our [migration test](https://github.com/EspressoSystems/nitro-testnode/blob/integration/espresso-tests/migration-test.bash). Since that script is intended for testing migrations, it does not not require SGX. Therefore it should not be use for production deployments.
{% endhint %}

1. Run the new batch poster inside SGX and get the `MREnclave` and `MRSigner` values (which is the hash of the code running inside the SGX). These values are needed to deploy the EspressoTEEVerifier contract.
2. Deploy the `EspressoTEEVerifier` contract.
3. Stop Nitro node with the batch poster and copy the batch poster's databases files to the TEE.
4. Perform the sequencer inbox migration.
5. Run new Batch poster. You will notice it starts catching up messages and building up state.

{% hint style="info" %}
Please also be aware of [steps to revert a migration](https://github.com/EspressoSystems/orbit-actions/tree/integration/migration#5-reverting) should you need them.
{% endhint %}

### Verify SGX Setup

{% hint style="info" %}
Setup of SGX TEE is beyond the scope of this document. We have had success with [Azure SGX VMs](https://learn.microsoft.com/en-us/azure/confidential-computing/virtual-machine-solutions-sgx)
{% endhint %}

First verify you have linux version with in-kernel SGX. To ensure you have in-kernel SGX run the following command to verify you are running a Linux kernel greater than version `5.11`.

```bash
uname -r
```

Ensure that your machine has an [Intel SGX2](https://www.intel.com/content/www/us/en/architecture-and-technology/software-guard-extensions.html) (Software Guard Extensions) enabled CPU to run our batch poster (See [here](https://www.kernel.org/doc/html/next/x86/sgx.html) and [here](https://github.com/intel/SGXDataCenterAttestationPrimitives/blob/main/driver/linux/README.kernel.md#transition-from-dcap-driver-to-kernel)). You can verify if your CPU supports SGX2 on Linux by inspecting CPU information:

```
grep -i sgx /proc/cpuinfo
```

If your CPU supports SGX, the output should resemble the following. If it does not, your CPU either doesn't support SGX2, or it isn't enabled in the BIOS.

```
 SGX2 supported                           = true
```

### Install Gramine

To install gramine follow the following instructions:

1. Install [software packages](https://gramine.readthedocs.io/projects/gsc/en/latest/#software-packages)
2. Setup [host configuration](https://gramine.readthedocs.io/projects/gsc/en/latest/#host-configuration)
3. Install the [SGX software stack](https://gramine.readthedocs.io/en/stable/devel/building.html#install-dependencies)
4. If your machine is running on Microsoft Azure, you can refer to [this document](https://learn.microsoft.com/en-us/azure/security/fundamentals/trusted-hardware-identity-management) for configuring aesm.

You don't need to follow the [build gramine steps](https://gramine.readthedocs.io/en/stable/devel/building.html#build-gramine) as we will be using [Gramine Shielded Containers (GSC)](https://gramine.readthedocs.io/projects/gsc/en/latest/#host-configuration)

At this point `systemctl status aesmd` should report a healthy service (**Active: active (running)**).

If you see any errors here, ensure your `aesmd` is configured properly. If your machine is running on Microsoft Azure, you can refer to [this document](https://learn.microsoft.com/en-us/azure/security/fundamentals/trusted-hardware-identity-management) for configuring `aesm`.

### Running the Batch Poster Inside SGX

#### Building the Poster Image

{% hint style="warning" %}
These steps need to happen inside SGX
{% endhint %}

Use our default [`Dockerfile.sgx-poster`](https://github.com/EspressoSystems/nitro-espresso-integration/blob/integration/Dockerfile.sgx-poster) or the Celestia [`Dockerfile.sgx-poster`](https://github.com/EspressoSystems/nitro-espresso-integration/blob/celestia-integration/Dockerfile.sgx-poster) to build the sgx-poster Docker image.

First obtain the source:

```
git clone https://github.com/EspressoSystems/nitro-espresso-integration
cd nitro-espresso-integration
```

* Alternative 1: using default Nitro stack

  ```
    git checkout integration
  ```
* Alternative 2: using Celestia DA

  ```
    git checkout celestia-integration
  ```

Then build the image.

```bash
docker build -f Dockerfile.sgx-poster -t sgx-poster .
```

#### Building the Gramine Image

Once the docker image is built, you need to build a Gramine Shielded Container (GSC) image.

The `gsc` python script requires a few python packages. For ubuntu 24.04 run

```bash
sudo apt-get install -y python3 python3-docker python3-jinja2 python3-tomli python3-tomli-w python3-yaml
```

For more information see the [GSC docs](https://gramine.readthedocs.io/projects/gsc/en/latest/#software-packages).

Clone Espresso's `gsc` repo and build the Gramine image:

```
git clone https://github.com/EspressoSystems/gsc.git
cd gsc
git checkout master
cp config.yaml.template config.yaml
./gsc build sgx-poster ./nitro-espresso.manifest
```

Now before building the gramine image, you need to edit your `poster_config.json` file to include the following fields (given parent chain is arbitrum sepolia):

```
"batch-poster": {
    "hotshot-url": "https://query.decaf.testnet.espresso.network/v0",
    "light-client-address": "0x08d16cb8243b3e172dddcdf1a1a5dacca1cd7098",
    "resubmit-espresso-tx-deadline": "2m"
},
"transaction-streamer": {
    "user-data-attestation-file": "/dev/attestation/user_report_data",
    "quote-file": "/dev/attestation/quote"
}
```

You need the sha256 hash of your poster\_config.json file. You can get the hash using the following command:

```bash
sha256sum poster_config.json
```

Replace the `nitro-espresso.manifest` in the gsc with these contents and replace the `<YOUR_SHA256_HERE>` with the sha256 of your poster\_config.json file.

```
sys.enable_extra_runtime_domain_names_conf = true
sgx.edmm_enable = true
sgx.remote_attestation = "dcap"
sgx.use_exinfo = true
sys.experimental__enable_flock = true
fs.mounts = [
    { path = "/home/user/.arbitrum/", uri = "file:/home/user/.arbitrum"},
    { path = "/config/", uri = "file:/config"}
]
sgx.allowed_files = ["file:/home/user/.arbitrum"]
[[sgx.trusted_files]]
uri = "file:/home/user/kzg10-aztec20-srs-1048584.bin"
sha256 = "cded83e82e4b49fee4cb2e0f374f996954fe12548ad39100432ee493069ef09d"
[[sgx.trusted_files]]
uri = "file:/config/poster_config.json"
sha256 = "<YOUR_SHA256_HERE>"
```

Next we will need to sign the image in order to run this container inside the SGX enclave.

Generate the signing key (if you don't already have one).

```
openssl genrsa -3 -out enclave-key.pem 3072
```

**PLEASE KEEP THIS KEY SAFE in some local private storage, but delete it from the server after you have signed.**

Sign the container

```
./gsc sign-image sgx-poster enclave-key.pem
```

The final step is to run the container inside the SGX enclave. This requires a `config` folder which contains the `poster_config.json` file (available from the legacy batch poster).

Finally we also need a `.arbitrum` folder which contains the state of the batch poster. At this point it can be an empty folder but once the legacy batch poster is shut down, we should fill this up with the contents of the legacy batch poster and re-start the poster.

Run the batch poster using the following command, replacing `$CONFIG_PATH` with the actual path to these folders on your host machine.

{% hint style="info" %}
These folders are mounted in the docker container, so any changes to them on the host change them in the container.
{% endhint %}

```bash
docker run \
    --device=/dev/sgx_enclave \
    -v /var/run/aesmd/aesm.socket:/var/run/aesmd/aesm.socket \
    -v $CONFIG_PATH/.arbitrum:/home/user/.arbitrum \
    -v $CONFIG_PATH/config:/config \
    gsc-sgx-poster
```

At this stage, you will see an attestation report similar to the following. The hex value, is the report data which contains the `MR_ENCLAVE` (the hash of the code running inside SGX) and the `MR_SIGNER`. After you see the attestation report, you can shut down the batch poster.

```
0e0e100fffff010000000000000000000100000000000000000000000000
0000000000000000000000000000000000000500000000000000e7000000
000000001f43237dce5a5deecd51d834e6467af7cc9856c7455dcabab6bb
2e7a2012c4c8000000000000000000000000000000000000000000000000
00000000000000000458a0e62674775ca9a048016f817f39b0bd40153000
aceb44a5128ded30555e0000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000888ae654e178
b8fa82cc685faa45a521000000000000000000000000000000009cc8bb48
d11c1dd7039a0ceadbdc1c77
Successfully read attestation report.
```

You can decode all this information using the following steps:

1. Create a `report.txt` file with the hex value and create a bin file as follows:

   ```bash
   xxd -r -p report.txt report.bin
   ```
2. Use [this](https://github.com/EspressoSystems/nitro-espresso-integration/blob/celestia-integration/decode_report_data.sh) bash script to decode the binary, it will print out the `MR_ENCLAVE` and `MR_SIGNER`.

### Deploying the `EspressoTEEVerifier` contract

#### Contract Deployment

You will need to use our version of [nitro contracts](https://github.com/EspressoSystems/nitro-contracts/tree/celestia-integration). The instructions below assume you are using celestia for DA. If not, simply checkout on `integration` branch instead.

Please clone this repo at the given branch to follow the next steps.

```
git clone --recurse-submodules git@github.com:EspressoSystems/nitro-contracts.git
git checkout celestia-integration
```

To run this script to deploy a rollup on arbSepolia follow the given steps:

**Compile the contracts using `yarn`**

```
yarn install && forge install
yarn build:all
```

**Create a `.env` file with variables from the previous steps**

```
DEVNET_PRIVKEY="" # Private key with funds on Arbitrum Sepolia.
MR_ENCLAVE="MR_ENCLAVE_VALUE" # MR_ENCLAVE value from the last step
MR_SIGNER="MR_SIGNER_VALUE" # MR_SIGNER value from the last step
ARBISCAN_API_KEY="" # [Arbscan API Key](https://docs.arbiscan.io/getting-started/viewing-api-usage-statistics)
```

**Deploy the contract**

```
npx hardhat run scripts/deployEspressoTEEVerifier.ts --network arbSepolia
```

#### Sequencer Inbox Migration

**Obtain the Contracts**

In this section we will be working out of our `orbit-actions`repo. Again the choice of `integration` or `celestia-integration` depends on DA.

```
git clone git@github.com:EspressoSystems/nitro-contracts.git
```

Be aware that the contract to deploy the sequencer inbox needs to locally deploy a mock ArbitrumChecker to prevent foundry from declaring calls to precompiles as invalid opcodes. This shouldn't affect on chain deployment from these scripts, nor should it affect the onchain execution of the migration action.

**Configuration**

Create a `.env` file in the orbit-actions directory that contains the following values:

```
#The private key for use during the migration. This should be the rollup owner's private key for steps involving performing the migration.
PRIVATE_KEY=""
# Environment variables for chain name and rpc_url
# These are essential for the upgrade
PARENT_CHAIN_CHAIN_ID=""
PARENT_CHAIN_RPC_URL=""
# Addresses to the upgrade executors on both chains.
# These are essential for the upgrade
PARENT_CHAIN_UPGRADE_EXECUTOR=""
# Environment variables for the sequencer inbox migration action contract
ROLLUP_ADDRESS=""
PROXY_ADMIN_ADDRESS=""

# The reader address should be set to the zero address for orbit chains, for other chains, set this to the same address as your current reader for the sequencer inbox
READER_ADDRESS="0x0"
IS_USING_FEE_TOKEN=""

MAX_DATA_SIZE="104857" #for orbit chains, use this value, for chains posting to ethereum, use 117964
# The old batch poster address will be removed from the sequencer inbox proxy to ensure only the batch poster running in the TEE will be allowed to post batches.
OLD_BATCH_POSTER_ADDRESS=""
NEW_BATCH_POSTER_ADDRESS=""
# The new batch poster address and batch poster manager address will be provided to you to run the migration.
BATCH_POSTER_MANAGER_ADDRESS=""
# This should be the address of the contract you deployed in the last step.
ESPRESSO_TEE_VERIFIER_ADDRESS=""
# This will allow you to deploy a reverting sequencer inbox migration action if desired (there are additional steps in the migration readme)
IS_REVERT=""
```

Source it.

```
source ./.env
```

Install all dependencies.

```
yarn
yarn prepare
yarn build
```

**Run the migration deployment scripts**

Run the migration deployment scripts for the parent chain. Including both `DeployAndInitEspressoSequencerInbox.s.sol`, and `DeployEspressoSequencerInboxMigrationAction.s.sol`. From the base directory of the orbit actions repo, you can use the following commands to run these scripts:

**`DeployAndInitEspressoSequencerInbox.s.sol`**

```
forge script --chain $PARENT_CHAIN_CHAIN_ID contracts/parent-chain/espresso-migration/DeployAndInitEspressoSequencerInbox.s.sol:DeployAndInitEspressoSequencerInbox --rpc-url $PARENT_CHAIN_RPC_URL --broadcast -vvvv --skip-simulation
```

**Before you proceed:** make sure to store the address of the new SequencerInbox in the environment variable `NEW_SEQUENCER_INBOX_IMPL_ADDRESS`

**`DeployEspressoSequencerInboxMigrationAction.s.sol`**

```
forge script --chain $PARENT_CHAIN_CHAIN_ID contracts/parent-chain/espresso-migration/DeployEspressoSequencerMigrationAction.s.sol:DeployEspressoSequencerMigrationAction --rpc-url $PARENT_CHAIN_RPC_URL --broadcast -vvvv --skip-simulation
```

**Before you proceed:** make sure to store the address of the new SequencerInbox in the environment variable `SEQUENCER_MIGRATION_ACTION`

**Execute the Upgrade**

The final step for executing the migration involves using cast to call the `perform()` function of the sequencer inbox migration action via the upgrade executor. You can use the following command to accomplish this:

```
cast send $PARENT_CHAIN_UPGRADE_EXECUTOR "execute(address, bytes)" $SEQUENCER_MIGRATION_ACTION $(cast calldata "perform()") --rpc-url $PARENT_CHAIN_RPC_URL --private-key $PRIVATE_KEY
```

After running this command, your rollup contracts should be set up to accept batches from your new batch poster.

#### Run the Batch Poster with Legacy State

[As stated in upstream documentation](https://docs.arbitrum.io/node-running/faq#how-can-i-migrate-the-date-of-one-synced-node-to-a-new-one), you need to copy the contents of the `.arbitrum` folder of the legacy batch poster to the `.arbitrum` folder of the new

Then re-start the batch poster.

#### Verify the Migration

You should be able to see `batch sent` logs once the batcher starts posting batches. This would indicate that the batcher has started successfully.


# Cartesi

The [Cartesi](https://cartesi.io/) team has built an integration that enables Cartesi applications to use Espresso for fast confirmations, low-cost DA, and decentralized sequencing. The integration is fully functional, but it is brand new and is still undergoing review, and should therefore be used with caution.\
Developers interested in deploying their own Cartesi application using Espresso should get in touch with the Cartesi team via their [Discord](https://discord.gg/pfXMwXDDfW), where they can find a [channel](https://discord.com/channels/600597137524391947/1288373906578866268) dedicated to the Espresso integration.

## Integration overview

The integration enables Cartesi applications to configure their source of transactions to be their specific namespace in the Espresso Network.

<figure><img src="https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcA0EA7JWTWkxFZYjVjimdKn07YELVb6qNZQTeTNLzQzVmMacrH5q9JxriEJZe9P50_npiJs4RuwogS4nNfF5kAIpPPzm8aZtp1J6yw6PiHLCJrGZgBL_n65-CZiEBYxcMuypWkMog6G5mmMkjijCUaOMIz3Oqh=s2048?key=X5eFEwcfpIztjaB5KnksbA" alt=""><figcaption><p>Overview of a Cartesi application using Espresso</p></figcaption></figure>

The integration is based on the concept that inputs to Cartesi dApps are of two fundamentally different natures:

* L2 transactions: these refer to common interactions of users with the application, and refer to application-specific actions such as “swap token”, “post message”, “attack goblin”, etc.; these transactions do not require any direct information or logic from the base layer (i.e., the L1);
* L1 -> L2 messages: these refer to information that is relayed from the base layer to the rollup application, such as informing about deposits done via the Portals, relaying the dApp’s address, ensuring base layer validation for a given input, etc.

This integration proposes that L2 transactions are to be processed “immediately” (i.e., as soon as they are sequenced), whereas L1 -> L2 messages are only processed when they are finalized on L1, meaning that they are processed “with a delay”.

Aside from that, from the application’s point of view, few things change:

* Back-end: both L2 transactions and L1 -> L2 messages are received as regular inputs;
* Front-end: L2 transactions are signed by the client and submitted to an L2 submission endpoint on the node, which will then forward them to Espresso; L1 -> L2 messages are submitted exactly in the same way as current regular Cartesi rollup inputs (i.e., as a transaction that eventually calls the `InputBox` contract’s `addInput` method).


# Optimism

Espresso is developing an integration for [OP Chains](https://docs.optimism.io/stack/getting-started). Here we provide an overview of the integration and details on how to deploy or migrate an existing chain will be provided shortly.

## Integration overview

The Espresso-OP Stack integration ensures that each batch processed by the rollup is consistent with Espresso-finalized blocks.

To ensure that the batch has been finalized by Espresso, the following checks are performed:

1. **Namespace validation:** Namespacing allows multiple chains to use Espresso’s fast confirmation layer simultaneously by associating each chain’s transactions with a unique namespace within Espresso blocks. This check ensures that the set of transactions in an OP batch corresponds to the correct namespace.
2. **Espresso finalization check:** Confirms that the OP batch maps to a valid Espresso finalized block.

The flow is as follows:

1. A user submits either a deposit transaction to the L1 or an L2 transaction.
2. The rollup node (`op-node`, running in sequencer mode) fetches any deposit transactions from L1.
3. The rollup node constructs the payload attributes and sends them to `op-geth`, which executes them to create blocks.
4. The `op-batcher` queries the blocks and creates batches accordingly.
5. The batcher then submits these batches to HotShot for finalization via the [submit API](https://github.com/EspressoSystems/gitbook/blob/main/guides/api-reference/espresso-api/submit-api.md).
6. Periodically, the batcher also calls the [availability API](https://docs.espressosys.com/sequencer/api-reference/espresso-api/availability-api) to check for finalized HotShot blocks containing these batches and performs batch consistency checks.
7. The batcher signs the transaction calldata that would be sent to the `Batch Inbox` contract.
8. In the integration, the `Batch Inbox` address is converted from an EOA to a contract containing only a fallback function. This fallback function receives all transactions sent to the contract and verifies the signature to ensure it originates from the trusted batcher:

A small change to the derivation pipeline filters out transactions sent to the batch inbox that caused the contract to revert.

This approach involves running an `op-batcher` in a TEE environment (such as Intel SGX). The batcher signs the transaction calldata. In case the TEE is broken, the batch poster can't impact the safety of the chain. It could, however, temporarily halt the chain's progress, thereby breaking liveness. Bridges relying on Espresso confirmations for faster settlement however need to trust the TEE as well in this integration. In a future update the dependency on TEEs will be removed entirely.


# Node Operators

\#Node Operators


# Running a Builder

Information about running a builder for the Espresso Network

### **Overview**

Participants creating blocks for the Espresso Network must run a builder, a piece of software which tracks the state of [HotShot consensus](https://github.com/EspressoSystems/gitbook/blob/main/guides/learn/the-espresso-network/README.md) so that it is able to and propose blocks at the correct time. The builder functions to create a block filled with transactions, drawing from transactions accessible in Espresso's public mempool as well as its own private mempool.

Espresso provides a simple builder implementation, which participants can run out-of-the-box or build their own software on top of. This document describes how to run the basic builder software.

For comprehensive guidance on the design of an Espresso builder, it is recommended to refer to the [`hotshot-builder-core`](https://github.com/EspressoSystems/hotshot-builder-core) repository. Furthermore, to gain insight into the process of enabling builder services for a sequencer, pertinent information can be found at [`espresso-sequencer-builder`](https://github.com/EspressoSystems/espresso-sequencer/tree/main/builder). For access to the most recent builder Docker images, please visit [here](https://github.com/EspressoSystems/espresso-sequencer/pkgs/container/espresso-sequencer%2Fbuilder).

### Usage

```bash
# Clone the espresso-sequencer repository
git clone https://github.com/EspressoSystems/espresso-sequencer

# Build the executable in release mode
cargo build --release

# Run a builder natively
target/release/permissionless-builder [options]

# To understand more about the available builder options
target/release/permissionless-builder -h

# Run a node with the builder docker image
docker run -it \
  [-e ENV=VALUE...] \
  ghcr.io/espressosystems/espresso-sequencer/builder:main
```

For a quick start, we recommend referring to the `espresso-sequencer` [docker-compose](https://github.com/EspressoSystems/espresso-sequencer/blob/main/docker-compose.yaml) file, and looking particularly at [`permissionless-builder`](https://github.com/EspressoSystems/espresso-sequencer/blob/270393c5bc5d1c974652d46edb5034251fa16bd7/docker-compose.yaml#L415C1-L435C35).

### Parameters & options

<table><thead><tr><th>Environment variable</th><th width="157">CLI flag</th><th>Description</th></tr></thead><tbody><tr><td>ESPRESSO_SEQUENCER_HOTSHOT_EVENT_STREAMING_API_URL</td><td>--hotshot-event-streaming-url</td><td>URL of hotshot events API running on Espresso Sequencer DA committee node. A builder will subscribe to this server to receive hotshot events. (e.g. http://localhost:8081)</td></tr><tr><td>ESPRESSO_BUILDER_ETH_MNEMONIC</td><td>--eth-mnemonic</td><td>Mnemonic phrase for builder account (e.g. "test test test test test test test test test test test junk")</td></tr><tr><td>ESPRESSO_BUILDER_ETH_ACCOUNT_INDEX</td><td>--eth-account-index</td><td>Index of a funded account. <strong>Note</strong>: This account must be funded in <em>Espresso</em>, meaning ETH must be bridged from the L1</td></tr><tr><td>ESPRESSO_BUILDER_L1_PROVIDER</td><td>--l1-provider-url</td><td>A Url builder will use for RPC communication with L1 (e.g. http://demo-l1-network:8545)</td></tr><tr><td>ESPRESSO_SEQUENCER_STATE_PEERS</td><td>--state-peers</td><td>Peer nodes use to fetch missing state</td></tr><tr><td>ESPRESSO_SEQUENCER_CHAIN_ID</td><td>--chain-id</td><td>Unique identifier for an instance of the sequencer network</td></tr><tr><td>ESPRESSO_SEQUENCER_MAX_BLOCK_SIZE</td><td>--max-block-size</td><td>Maximum allowed size (in bytes) for a block</td></tr><tr><td>ESPRESSO_SEQUENCER_BASE_FEE</td><td>--base-fee</td><td>Minimum fee in WEI per byte of payload</td></tr><tr><td>ESPRESSO_BUILDER_SERVER_PORT</td><td>--port</td><td>Port to run builder server on through which sequencer node can query builder provided APIs (e.g 41003)</td></tr><tr><td>ESPRESSO_BUILDER_BOOTSTRAPPED_VIEW</td><td>--view-number</td><td>Bootstrapping View number (e.g. 0)</td></tr><tr><td>ESPRESSO_BUILDER_CHANNEL_CAPACITY</td><td>--channel-capacity</td><td>The most outstanding hotshot events a builder wants at a point in time (e.g. 1024)</td></tr><tr><td>ESPRESSO_BUILDER_WEBSERVER_RESPONSE_TIMEOUT_DURATION</td><td>--max-api-timeout-duratio</td><td>The amount of time a builder can wait before timing out a request to the API (e.g 1s)</td></tr><tr><td>ESPRESSO_BUILDER_BUFFER_VIEW_NUM_COUNT</td><td>--buffer-view-num-count</td><td>The number of views to buffer before a builder garbage collects its state (e.g. 15)</td></tr></tbody></table>

## Hardware requirements

Hardware requirements are subject to change as new features are added, but for now we recommend the following:

* **Memory**: 4-8 GB
* **CPU:** 2-4 Cores


# Running a Caff Node

To read confirmations from the Espresso Network, you need to run a "Caff Node". To understand more about Caff Nodes, refer to the following [docs](https://docs.espressosys.com/network/concepts/read-from-network).

## Running Caff Node

Follow the instructions in [Caff Node Run](https://github.com/EspressoSystems/caff-node-run) repo to run caff nodes for various Espresso integrated chains.


# Espresso Network Benchmarks

Providing faster finality is Espresso's core priority. The engineering team has worked on reducing block finality from 10s to 2s, and thus has performed some benchmarking tests on an internal network, which emulates Espresso's Decaf netwok.

## Summary

**- Finality latency:** 2 seconds to finalize a block (5 MB blocks).

**- Throughput:** Increased from 1 MB/s → 5 MB/s.

**- Benchmark network:** 100 globally distributed nodes + 21 DA nodes.

## Why This Matters

One of Espresso’s core goals is to enable chains to communicate quickly and securely, helping solve the problem of liquidity fragmentation across the blockchain ecosystem.

The faster crosschain applications can securely react to on-chain events, the more usable and unified liquidity becomes, thus bringing us closer to a truly interconnected ecosystem.

These latest benchmark results represent a major step forward. And Espresso is far from finished: **the team is already working toward sub-second block finality in the coming year.**

## What Enabled the Performance Gains

### 1. High-bandwidth TCP tuning

Default operating system TCP settings severely limit global throughput (≈30 Mbps). By optimizing TCP parameters for high-latency, high-bandwidth networking, nodes now utilize virtually the full 1 Gbps capacity available on AWS machines.

### 2. Regional Builders

Requesting blocks from a remote [Builder](https://docs.espressosys.com/network/guides/node-operators/running-a-builder) introduced large global round-trip delays. Espresso now runs a Builder in every region, each sharing the same mempool. Validators fetch blocks locally, cutting block preparation time in half.

### 3. Earlier block preparation in the pipeline

Leaders nodes now begin block assembly as soon as they receive the proposal, instead of waiting for the previous view to be finished, saving roughly 200 ms per view.

## Future Improvements

### 1. Faster block retrieval

The Builder block exchange currently takes \~500 ms per view. Moving to a single round-trip request could significantly reduce the time.

### 2. Smarter networking

Today, all messages route through a central CDN, adding an extra hop. Seding smaller messages over a dedicated p2p network could further improve latency.

### 3. Removing the DA committee bottleneck

Removing the Data Availability Commitee could reduce time in around 800ms.

## Benchmarking Set-up

* 100 nodes and 21 DA nodes geographically distributed across `ap-southeast-1`, `eu-central-1`, `us-east-1`, `ap-southeast-2` and `sa-east-1` regions.
* 1 CDN (located in `us-east-2`, run on `c8gn.large`).
* A Builder located in each region and run on `c8g.xlarge`.


# Espresso Chains Reference

The following are Espresso-integrated chains and useful information about them, such as RaaS provider, the main public RPC or the Espresso's Caff Node available (if any).

To learn more about Caff Nodes, check out [this page](https://docs.espressosys.com/network/concepts/read-from-network).

### Celo (Devnet - unstable)

* **Sequencer's RPC:** <https://sequencer-geth.op-devnet.devnet.on.espresso.network>
* **Espresso's Caff Node:** <https://caff-node-geth.op-devnet.devnet.on.espresso.network>
* **Block Explorer:** <https://celo-x-espresso.cloud.blockscout.com/>

### ApeChain

* **RaaS provider:** Caldera.

#### Mainnet

* **Caldera's RPC:** <https://rpc.apechain.com/http>
* **Caldera's Hub:**: <https://apechain.hub.caldera.xyz/>

#### Testnet

* **Caldera's RPC:** <https://apechain-tnet.rpc.caldera.xyz/http>
* **Caldera's Hub:**: <https://apechain-tnet.hub.caldera.xyz/>
* **Espresso's Caff Node:** <https://apechain.caff.testnet.espresso.network/>

### Rari

* **RaaS provider:** Caldera.

#### Mainnet

* **Caldera's RPC:** <https://rari.calderachain.xyz/http>
* **Caldera's Hub:**: <https://rari.hub.caldera.xyz/>

#### Testnet

* **Caldera's RPC:** <https://rari-testnet.calderachain.xyz/http>
* **Caldera's Hub:**: <https://rari-testnet.hub.caldera.xyz/>
* **Espresso's Caff Node:** <https://rari.caff.testnet.espresso.network/>

### AppChain

* **RaaS provider:** Caldera.

#### Mainnet

* **Caldera's RPC:** <https://rpc.appchain.xyz/http>
* **Caldera's Hub:**: <https://appchain.hub.caldera.xyz/>

#### Testnet

* **Caldera's RPC:** <https://appchaintestnet.rpc.caldera.xyz/http>
* **Caldera's Hub:**: <https://appchaintestnet.hub.caldera.xyz/>
* **Espresso's Caff Node:** <https://appchain.caff.testnet.espresso.network/>

### Molten

* **RaaS provider:** Caldera.

#### Mainnet

* **Caldera's RPC:** <https://molten.calderachain.xyz/http>
* **Caldera's Hub:**: <https://molten.hub.caldera.xyz/>

### T3rn

* **RaaS provider:** Caldera.

#### Mainnet

* **Caldera's RPC:** <https://t3rn.calderachain.xyz/>
* **Caldera's Hub:**: <https://t3rn.hub.caldera.xyz/>

### NodeOps

* **RaaS provider:** Caldera.

#### Mainnet

* **Caldera's RPC:** <https://nodewatch-network.rpc.caldera.xyz/http>
* **Caldera's Hub:**: <https://nodewatch-network.hub.caldera.xyz/>

#### Testnet

* **Caldera's RPC:** <https://nodeops-orchestrator-network.calderachain.xyz/http>
* **Caldera's Hub:**: <https://nodeops-orchestrator-network.hub.caldera.xyz/>

### Rufus

* **RaaS provider:** Caldera.

#### Mainnet

* **Caldera's RPC:** <https://rufus.calderachain.xyz/http>
* **Caldera's Hub:** <https://rufus.hub.caldera.xyz/>

#### Testnet

* **Caldera's RPC:** <https://rufus-sepolia-testnet.rpc.caldera.xyz/http>
* **Caldera's Hub:** <https://rufus-sepolia-testnet.hub.caldera.xyz/>

### Huddle01

* **RaaS provider:** Caldera.

#### Mainnet

* **Caldera's RPC:** <https://huddle01.calderachain.xyz/http>
* **Caldera's Hub:** <https://huddle01.hub.caldera.xyz/>

#### Testnet

* **Caldera's RPC:** <https://huddle-testnet.rpc.caldera.xyz/http>
* **Caldera's Hub:** <https://huddle-testnet.hub.caldera.xyz/>


# Delegate $ESP Tokens

If you don’t run an Espresso validator, you can still put your $ESP tokens to work by **delegating** them. Delegation means you temporarily assign your tokens to an Espresso validator, who stakes them on your behalf. In return, you earn staking rewards, minus the validator’s commission.

**To delegate your tokens please visit:** [**https://staking.main.net.espresso.network/**](https://staking.main.net.espresso.network/)

## Connecting Your Wallet

* Click `Connect Your Wallet`.
* Once connected, you’ll see key account information, such as your available balance, your staked amount or your claimable rewards.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-d991c5a1492a8878c88475c0e44f87becd00c29b%2Fdelegation2.png?alt=media" alt=""><figcaption></figcaption></figure>

## Choosing a Validator

Each validator sets a commission rate, which is deducted from your rewards in exchange for running the infrastructure that stakes your tokens. When selecting a validator, you can consider helpful data including: total stake, commission rate or missed slots.

**NOTE:** Only top 100 validators are eligible to receive rewards. If you delegate to a validator outside the top 100, you will **not** receive rewards till they enter the top 100.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-572cfa9556dac48c69ce222139b6beea23d39369%2Fdelegation3.png?alt=media" alt=""><figcaption></figcaption></figure>

## Delegating Your Tokens

* Once you select a validator, click `Delegate`.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-3b9a86ca6de3d3f4b41cf950cec172759216f8fe%2Fdelegation4.png?alt=media" alt=""><figcaption></figcaption></figure>

* Review key validator details (e.g., APY, commission), then choose the amount of $ESP you want to delegate.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-f47fd8bcf2a8923c95946ef006b410f95f03aa04%2Fdelegation5.png?alt=media" alt=""><figcaption></figcaption></figure>

* Approve the transaction.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-e1aaa0a8861c8939a0158bec91361f2c8bca7d99%2Fdelegation6.png?alt=media" alt=""><figcaption></figcaption></figure>

* Confirm the delegation.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-33fc99a40eb86ca131c63d263fb97687fb5f86c4%2Fdelegation7.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-5688261f9da4b2eb2806cde6990adee989d626f6%2Fdelegation8.png?alt=media" alt=""><figcaption></figcaption></figure>

## Manage Your Stakes

After your delegation transaction has been confirmed, you will start getting rewards. You can check your current stakes in the `My Stakes` section.

* Click `Manage` next to the validator you want to adjust.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-6adf239bd1adc143f540b26be98e814b20bcddea%2Fdelegation9.png?alt=media" alt=""><figcaption></figcaption></figure>

* From here, you can **delegate more** or **undelegate**.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-09ac725f61388c288870235ff261c9bab39f4264%2Fdelegation10.png?alt=media" alt=""><figcaption></figcaption></figure>

* When undelegating, you may choose to **remove all your stake** or **only part of it**.
* Note that it takes around 7 days to complete your undelegation, and you can only have one pending undelegation per validator at any given time.&#x20;


# Espresso API

Reference for REST APIs served by Espresso nodes and query services

## Modularity

The Espresso API comprises several independent modules serving different purposes and requiring different resources. A given node may serve one, or all, or any combination of these modules, depending on its role in the system and the resources available to it. To see a list of the modules available from a particular node, navigate to the root URL of that node's API.

In brief, the available API modules are:

* [status-api](https://docs.espressosys.com/network/api-reference/espresso-api/status-api "mention"): node-specific state and consensus metrics
* [catchup-api](https://docs.espressosys.com/network/api-reference/espresso-api/catchup-api "mention"): serves recent consensus state to allow peers to catch up with the network
* [availability-api](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api "mention"): serves data recorded by the [Tiramisu DA layer](https://github.com/EspressoSystems/gitbook/blob/main/learn/the-espresso-network/properties-of-hotshot/espresso-data-availability-layer/README.md), such as committed blocks
* [node-api](https://docs.espressosys.com/network/api-reference/espresso-api/node-api "mention"): complements the availability API by serving eventually consistent data that is not (yet) necessarily agreed upon by all nodes
* [state-api](https://docs.espressosys.com/network/api-reference/espresso-api/state-api "mention"): serves consensus state derived from finalized blocks
* [events-api](https://docs.espressosys.com/network/api-reference/espresso-api/events-api "mention"): streams events from HotShot
* [submit-api](https://docs.espressosys.com/network/api-reference/espresso-api/submit-api "mention"): allows users to submit transactions to the public mempool

## Content Types

All APIs support JSON and binary formats in both request and response bodies.

* The JSON format is a straightforward serialization of the data types used internally by consensus nodes. In the future, a formal specification will be published, and the API will conform to that specification.
* The binary format is the [bincode](https://docs.rs/bincode/latest/bincode/) serialization of consensus data types, prefixed with an 8-byte version header. In the future, this will be replaced with a binary format with better cross-language support, and the data types will be defined by a published schema, rather than generated from code.

In requests and responses, the JSON format is denoted by the MIME type `application/json`, and the binary format by `application/octet-stream`. For requests with a body, the content type of the body must be set via the `Content-Type` header. The desired content type of the response can be controlled via the `Accept` header of the request. If the `Accept` header does not preference either format, JSON will be used by default.

## Server-Hosted Documentation

All Espresso API servers provide self-hosted API documentation, which makes it easy to see exactly what APIs the server supports, and can be easier to browse than these docs. The root URL of an application, e.g. `my-server.xyz`, lists the supported API modules and versions. Clicking on any API module, or navigating to the root of that API, e.g. `my-server.xyz/status`, documents the endpoints available in that module.

## Versioning and Stability

A node may serve multiple major versions of a given API at the same time. The desired version can be selected via a URL prefix. For example, `my-server.xyz/v0/status/metrics` and `my-server.xyz/v1/status/metrics` both hit the same endpoint, but in different API versions. A URL with no version segment will get a permanent redirect response to the latest supported version. In this case, `/status/metrics` would redirect to `/v1/status/metrics`.

Whenever a breaking change is made to an API, a new major version will be created, and the old version will continue to be served for some time, giving clients time to upgrade to the new version whenever it is convenient for them. Note that non-breaking changes, such as adding new endpoints, may be made in place to existing versions.

To see a list of versions of an API supported by a server, visit the root URL of that server.

### Version Support

<table><thead><tr><th width="79.67578125">Version</th><th width="277.54296875">Status</th><th>Comment</th></tr></thead><tbody><tr><td>v1</td><td>available on testnet April 15, 2025</td><td>Some APIs are changed and some endpoints added to support proof of stake</td></tr><tr><td>v0</td><td>latest version</td><td></td></tr></tbody></table>

This guide documents the most recent version `v1`, but archive API references are available for [earlier supported versions](https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions).

## Types

These types are used in requests and responses across many of the API modules.

### Primitives

#### Integer

We use `integer` to represent any JSON integer, with a maximum size of at least `2^63 - 1`. Of special note, byte arrays are sometimes represented as arrays of integers (`[integer]`). When the type `[integer]` is used as a byte array, each integer therein is restricted to the range `[0, 255]`.

#### Hex

In the following, we use the type `hex` to indicate a hex-encoded binary string, with `0x` prefix.

#### Base 64

In the following, we use the type `base64` to indicate a base64-encoded binary string, using the standard base 64 alphabet with padding.

#### Tagged Base 64

Some types use an enhanced [tagged base 64](https://docs.rs/tagged-base64/latest/tagged_base64/) encoding, which consists of a prefix identifying the type of the encoded object, a `~`, and then a base 64 string using the URL-safe base 64 alphabet without padding. The base 64 string encodes the binary representation of a typed object, plus a checksum. Because the encoding is URL-safe, these strings can be used not only in request and response bodies, but also in URL paths. The checksum allows the server to provide useful errors if a tagged base 64 string is mistyped or corrupted. The tag makes it easy for a human to tell different types of objects apart.

For example, a transaction hash might be encoded like `TX~QDuwVkmexu1fWgJbjxshXcGqXku838Pa9cTn0d-v3hZ-`, while a block hash could look like `BLOCK~00ISpu2jHbXD6z-BwMkwR4ijGdgUSoXLp_2jIStmqBrD`.

We use the type `tagged<TAG>` to indicate a tagged base 64 object with the given tag, as in `tagged<TX>` or `tagged<BLOCK>`.

### `NamespaceTable`

```json
{
    "bytes": base64
}
```

### `ChainConfig`

A chain config determines properties of consensus, such as the base fee for sequencing and the chain ID. To save space, it can be represented either as the full config object (`Left` variant below) or as a commitment to the chain config (`Right` variant). The genesis header will always contain the full config, so clients can fetch the full config from genesis and then compare its commitment against any other header.

```json
{
    "chain_config": 
        { "Left": { "chain_id": hex, "max_block_size": integer, "base_fee": hex } }
        | { "Right": tagged<CHAIN_CONFIG> }
}
```

### `Header`

```json
{
    "version": {
        "Version": {
            "major": integer,
            "minor": integer
        }
    },
    "fields": {
        "height": integer,
        "timestamp": integer,
        "l1_head": integer,
        "l1_finalized": null | {
            "number": integer,
            "timestamp": hex,
            "hash": hex
        },
        "payload_commitment": tagged<HASH>,
        "builder_commitment": tagged<BUILDER_COMMITMENT>,
        "ns_table": NamespaceTable,
        "block_merkle_tree_root": tagged<MERKLE_COMM>,
        "fee_merkle_tree_root": tagged<MERKLE_COMM>,
        "reward_merkle_tree_root": tagged<MERKLE_COMM>,
        "fee_info": { "account": hex, "amount": hex },
        "chain_config": ChainConfig
    }
}

```

### `Payload`

```json
{
    "raw_payload": base64,
    "ns_table": NamespaceTable
}
```

### `VidCommon`

```json
{
    "V0": {
        "poly_commits": tagged<FIELD>,
        "all_evals_digest": tagged<FIELD>,
        "payload_byte_len": integer,
        "num_storage_nodes": integer,
        "multiplicity": integer
    }
} | {
    "V1": {
        "total_weights": integer,
        "recovery_threshold": integer
    }  
}
```

### `Leaf`

```json
{
    "view_number": integer,
    "justify_qc": QC,
    "next_epoch_justify_qc": null | NextEpochQC,
    "parent_commitment": string,
    "block_header": Header,
    "upgrade_certificate": null | UpgradeCertificate,
    "view_change_evidence": null | ViewChangeEvidence,
    "next_drb_result": null | DrbResult,
    "with_epoch": bool
}
```

### `Transaction`

```json
{
    "namespace": integer,
    "payload": base64
}
```

{% hint style="warning" %}
If using the Rust API, you may notice that [`namespace`](https://github.com/EspressoSystems/espresso-sequencer/blob/main/types/src/v0/v0_1/transaction.rs#L41) is represented by a `u64`. However, some internal sub-protocols represent the namespace as a `u32`, and thus the maximum allowable namespace ID is `4294967295` (2^32 - 1). Larger namespace IDs will be rejected on transaction submission.
{% endhint %}

### `MerkleProof`

The low-level proof type for a Merklized data structure. The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`MerkleProof`](https://jellyfish.docs.espressosys.com/jf_primitives/merkle_tree/prelude/struct.MerkleProof.html) type.

### `NsIndex`

The 0-based position of a namespace in a [`NamespaceTable`](#namespacetable). The index is a little-endian byte-encoded 4-byte integer, as in `[3, 2, 1, 255]` (`0xff010203`).

### `NsProof`

A proof that a certain list of transactions corresponds to a certain namespace in a block.

```json
{
    "V0": {
        "ns_index": NsIndex,
        "ns_payload": base64, // binary encoding of the namespace data
        "ns_proof": {
            "prefix_elems": tagged<FIELD>,
            "suffix_elems": tagged<FIELD>,
            "prefix_bytes": [integer],
            "suffix_bytes": [integer]
        }
    }
} | {
    "V1": {
        "ns_index": NsIndex,
        "ns_payload": [integer],
        "ns_proof": MerkleProof
    }   
}
```

`V0.ns_proof` is a low-level range proof in the Espresso ADVZ VID scheme. The details of this proof are out of scope of this document, but this JSON object corresponds to the [`LargeRangeProofType`](https://hotshot.docs.espressosys.com/hotshot_types/vid/struct.LargeRangeProofType.html), and can be manipulated in Rust using that type.


# Status API

Node-specific state and consensus metrics

This API provides insight into the inner workings of consensus. It is primarily useful to the operator of the node, as many of the metrics provided here make for useful [alerts](https://github.com/EspressoSystems/gitbook/blob/main/guides/running-a-sequencer-node.md#monitoring).

## Endpoints

### GET `/status/block-height`

The last known block height of the chain.

#### Returns `integer`

### GET `/status/success-rate`

The view success rate since genesis. This equals the number of views completed divided by the number of successful views, i.e. the block height.

#### Returns `float`

### GET `/status/time-since-last-decide`

The elapsed time, in seconds, since consensus last decided on a block. Useful to alert when consensus is stalled or this node has been disconnected from consensus.

#### Returns `integer`

### GET `/status/metrics`

Exposes all metrics recorded by consensus in Prometheus format.


# Catchup API

Serves recent consensus state to allow peers to catch up with the network

The primary customer of this API is peer consensus nodes who may have recently joined the network or were temporarily disconnected. These nodes need the very latest state, one which hasn't even been finalized yet, in order to start voting and proposing in consensus.

In HotShot, all state required to participate is represented in the form of Merkle trees or Merkle tries, so this API is able to provide select segments of the state with a proof that will convince the client that the returned segment is accurate, as long as they know the corresponding state *commitment*.

## Types

### `Account`

```json
{
    // Account balance in WEI. Serialized as a hex string so as not to exceed the
    // range of JSON integers.
    "balance": hex,
    // Merkle proof justifying "balance" relative to the state commitment.
    "proof": {
        "account": hex,
        "proof":
            { "Presence": MerkleProof },
          | { "Absence": MerkleProof }
        }
    }       
}
```

## Endpoints

### GET `/catchup/:height/:view/account/:address`

Get the balance of the requested fee account in the state from the requested consensus height and view. This is used to fetch the state for *unfinalized* views, to facilitate rapid catchup. If `:view` has already been finalized, this endpoint may fail with error 404.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>The account (Ethereum address) to look up</td></tr></tbody></table>

#### Returns `Account`

### POST `/catchup/:height/:view/accounts`

Bulk version of `/catchup/:height/:view/account`. The request body should be a JSON array consisting of `TaggedBase64`-encoded fee accounts.

The response is a `FeeMerkleTree` containing sub-trees for each of the requested accounts, which is\
a more condensed way to represent the union of account proofs for each requested account. Individual\
Merkle proofs for each account can be extracted from this tree.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr></tbody></table>

#### Returns `FeeMerkleTree`

### GET `/catchup/:height/:view/blocks`

Get the Merkle frontier (path to most recently inserted element) of the accumulator of blocks, from the requested consensus view. This is used to fetch the state for *unfinalized* views, to facilitate rapid catchup. If `:view` has already been finalized, this endpoint may fail with error 404.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the frontier</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the frontier</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/catchup/chain-config/:commitment`

Get the chain config with the given hash.

#### Parameters

<table><thead><tr><th width="126.4453125">Name</th><th width="215.55859375">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>commitment</code></td><td><code>tagged&#x3C;CHAIN_CONFIG></code></td><td>The hash of the chain config to look up</td></tr></tbody></table>

**Returns** `ChainConfig`

### GET `/catchup/:height/leafchain`

Get a leaf chain which decides a specified block height. This endpoint can be used for catching up the stake table, where `:height` is the block height of the epoch root you want to catch up to.

#### Parameters

<table><thead><tr><th width="126.4453125">Name</th><th width="215.55859375">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height decided by the desired leaf chain</td></tr></tbody></table>

**Returns** `[Leaf]`

### GET `/catchup/:height/:view/reward-account/:address`

Get the balance of the requested reward account in the state from the requested consensus height and view. This is used to fetch the state for *unfinalized* views, to facilitate rapid catchup. If `:view` has already been finalized, this endpoint may fail with error 404.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>The account (Ethereum address) to look up</td></tr></tbody></table>

#### Returns `Account`

### POST `/catchup/:height/:view/reward-accounts`

Bulk version of `/catchup/:height/:view/reward-account`. The request body should be a JSON array consisting of `TaggedBase64`-encoded fee accounts.

The response is a `RewardsMerkleTree` containing sub-trees for each of the requested accounts, which is a more condensed way to represent the union of account proofs for each requested account. Individual Merkle proofs for each account can be extracted from this tree.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr></tbody></table>

#### Returns `RewardsMerkleTree`


# Availability API

Serves data recorded by the Tiramisu DA layer, such as committed blocks

The availability API is the place to get onchain data, like blocks and transactions. It is the primary interface for downstream components like rollups and end users.

The API is designed to be *robust* and *pure*. Robust means that if the node hosting the API misses some data, for example from being offline when a certain block was finalized, it will automatically fetch the missing data from a peer, and will eventually fetch and store all finalized data. Pure means that each endpoint is a pure function -- with the exception of occasionally returning 404 for missing data, each endpoint will always give the same response given the same parameters.

Due to purity, this API provides no aggregate queries, like block or transaction counts, which might change as missing data is fetched. Likewise, every endpoint takes some specification of the exact point in the chain the client is looking for, like a block height or hash. There is no "latest block" query. Thus, most real-world use cases will need to complement the availability API with use of the [node API](https://docs.espressosys.com/network/api-reference/espresso-api/node-api).

## Organization

While this API has many endpoints, don't be intimidated -- there is a method to the madness. The API is organized around collections of different resources, each of which corresponds to blocks and can be indexed by block height or hash.

### Resources

* Leaves
* Headers
* Blocks
* Block summaries
* Payloads
* VID common

### Indices

Each of these resources can be addressed in the following ways:

* `<resource>/:height`
* `<resource>/hash/:hash`
* `<resource>/payload-hash/:payload-hash`

{% hint style="warning" %}
Not all of the indices are implemented for all resources, although in principle they can be. The supported indices are documented below for each endpoint. Future releases will fill in the missing functionality.
{% endhint %}

{% hint style="warning" %}
Leaves are currently indexed slightly differently from other resources. See documentation on leaf endpoints. Future versions of this API will merge the concept of a leaf and a header, resolving this discrepancy.
{% endhint %}

In addition, there are endpoints to fetch a range of each resource (`<resource>/:form/:until`) and to subscribe to a WebSockets stream (`/stream/<resource>/:from`).

## Types

### `BlockSummary`

```json
{
    "header": Header,
    "hash": tagged<BLOCK>,
    "size": integer,
    "num_transactions": integer
}
```

### `BlockResponse`

```json
{
    "header": Header,
    "payload": Payload,
    "hash": tagged<BLOCK>,
    "size": integer,
    "num_transactions": integer
}
```

### `LeafResponse`

```json
{
    "leaf": Leaf,
    "qc": QC,
}
```

### `PayloadResponse`

```json
{
    "data": Payload,
    "height": integer,
    "size": integer,
    "block_hash": tagged<BLOCK>,
    "hash": tagged<HASH>
}
```

### `VidCommonResponse`

```json
{
    "common": VidCommon,
    "block_hash": tagged<BLOCK>,
    "payload_hash": tagged<HASH>
}
```

## Endpoints

### GET `/availability/leaf`

#### Paths

* `/availability/leaf/:height`
* `/availability/leaf/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the leaf to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;COMMIT></code></td><td>Hash of the leaf to fetch</td></tr></tbody></table>

#### Returns `LeafResponse`

### GET `/availability/leaf/:from/:until`

Retrieve a range of consecutive leaves.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first leaf to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last leaf to fetch</td></tr></tbody></table>

#### Returns `[LeafResponse]`

### GET `/availability/stream/leaves/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of leaves, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first leaf to yield</td></tr></tbody></table>

#### Yields `LeafResponse`

### GET `/availability/header`

#### Paths

* `/availability/header/:height`
* `/availability/header/hash/:hash`
* `/availability/header/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the header to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the header to fetch</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the header to fetch. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `Header`

### GET `/availability/header/:from/:until`

Retrieve a range of consecutive headers.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first header to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last header to fetch</td></tr></tbody></table>

#### Returns `[Header]`

### GET `/availability/stream/headers/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of headers, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first header to yield</td></tr></tbody></table>

#### Yields `Header`

### GET `/availability/block`

#### Paths

* `/availability/block/:height`
* `/availability/block/hash/:hash`
* `/availability/block/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block to fetch</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block to fetch. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `BlockResponse`

### GET `/availability/block/:from/:until`

Retrieve a range of consecutive blocks.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first block to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last block to fetch</td></tr></tbody></table>

#### Returns `[BlockResponse]`

### GET `/availability/stream/blocks/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of blocks, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first block to yield</td></tr></tbody></table>

#### Yields `BlockResponse`

### GET `/availability/block/summary`

#### Paths

* `/availability/block/summary/:height`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block to fetch</td></tr></tbody></table>

#### Returns `BlockSummary`

### GET `/availability/block/summaries/:from/:until`

Retrieve a range of consecutive block summaries.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first block summary to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last block summary to fetch</td></tr></tbody></table>

#### Returns `[BlockSummary]`

### GET `/availability/payload`

#### Paths

* `/availability/payload/:height`
* `/availability/payload/block-hash/:block-hash`
* `/availability/payload/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose payload should be fetched</td></tr><tr><td><code>block-hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose payload should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload to fetch. Note that block payloads are not necessarily unique. If there are multiple payloads matching this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `PayloadResponse`

### GET `/availability/payload/:from/:until`

Retrieve a range of consecutive payloads.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first payload to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last payload to fetch</td></tr></tbody></table>

#### Returns `[PayloadResponse]`

### GET `/availability/stream/payloads/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of payloads, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first payload to yield</td></tr></tbody></table>

#### Yields `PayloadResponse`

### GET `/availability/vid/common`

#### Paths

* `/availability/vid/common/:height`
* `/availability/vid/common/hash/:hash`
* `/availability/vid/common/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose VID common data should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose VID common data should be fetched</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block whose VID common data should be fetched. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `VidCommonResponse`

### GET `/availability/stream/vid/common/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of VID common objects, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first VID common to yield</td></tr></tbody></table>

#### Yields `VidCommonResponse`

### GET `/availability/block/:height/namespace/:namespace`

Get the list of transactions in a block from a given namespace, along with a proof that these are only and all such transactions from that block. Note that the proof may be `null` if `transactions` is empty, in which case the caller should check the namespace table for the specified block to confirm that `:namespace` is not present.

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block containing the desired namespace</td></tr><tr><td><code>namespace</code></td><td><code>integer</code></td><td>ID of the desired namespace</td></tr></tbody></table>

#### Returns

```json
{
    "transactions": [Transaction],
    "proof": NsProof | null
}
```

### GET `/availability/transaction`

#### Paths

* `/availability/transaction/:height/:index`
* `/availability/transaction/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block containing the desired transaction</td></tr><tr><td><code>index</code></td><td><code>integer</code></td><td>0-based position of the desired transaction in its block</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;TX></code></td><td>Hash of the desired transaction. Note that transactions are not necessarily unique. If there are multiple transactions matching this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns

```json
{
    "transaction": Transaction,
    "hash": tagged<TX>,
    "index": integer,
    "proof": TransactionInclusionProof,
    "block_hash": tagged<BLOCK>,
    "block_height": integer
}
```

The response contains the hash of the transaction, the hash and height of the block that contains it, and its index within that block. It also contains a `TransactionInclusionProof`, which proves inclusion of this transaction in the block with `block_hash`. The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`TxInclusionProof`](https://github.com/EspressoSystems/espresso-sequencer/blob/8ff3c9200b6bdefa9fa6f30b46b16a1b69cea5a1/sequencer/src/block/queryable.rs#L174) type.

### GET `/availability/limits`

Get implementation-defined limits restricting certain requests.

* `small_object_range_limit`: the maximum number of small objects which can be loaded in a single range query. Currently small objects include leaves only. In the future this limit will also apply to headers, block summaries, and VID common, however
  * loading of headers and block summaries is currently implemented by loading the entire block
  * imperfect VID parameter tuning means that VID common can be much larger than it should
* `large_object_range_limit`: the maximum number of large objects which can be loaded in a single range query. Large objects include anything that *might* contain a full payload or an object proportional in size to a payload. Note that this limit applies to the entire class of objects: we do not check the size of objects while loading to determine which limit to apply. If an object belongs to a class which might contain a large payload, the large object limit always applies.

**Returns**

```json
{
    "large_object_range_limit": integer,
    "small_object_range_limit": integer
}
```

### GET `/state-cert/epoch`

Get the light client state update certificate for the given epoch.

The light client state update certificate consists of the list of Schnorr signatures of the light client state at the end of the epoch. This is used to update light client state in the contract so that it have the new stake table information for the next epoch.

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>epoch</code></td><td><code>integer</code></td><td>Epoch number containing the desired state cert</td></tr></tbody></table>

**Returns**

```json
{
    "epoch": integer,
    "light_client_state": {
        "viewNum": integer,
        "blockHeight": integer,
        "blockCommRoot": BN256.ScalarField
    },
    "next_stake_table_state": tagged<STAKE_TABLE_STATE>,
    "signatures": [[tagged<SCHNORR_VER_KEY>, tagged<SCHNORR_SIG>]]
}
```

[^1]: This breaks purity. This will be addressed in a future version of the API.


# Node API

Complements the availability API by serving eventually consistent data that is not necessarily agreed upon by all nodes

The [availability API](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api) provides a pure view of snapshots of the Espresso blockchain at various points in time. Because it strives for robustness and purity, it does not include aggregate statistics like block or transaction counts, which may briefly return incorrect results and will gradually correct themselves as missing data is fetched. The node API does provide this data, making it a useful complement to the availability API.

In other words, while the availability API is a view of the blockchain abstractly, the node API provides information about *this node's* view of the chain, at the present moment in time.

## Endpoints

### GET `/node/block-height`

Get the height of the chain as known to this node. This is equal to one more than the height of the latest known block. It is *not* a count of the blocks in this node's database, as blocks earlier than the latest known block could be missing.

#### Returns `integer`

### GET `/node/transactions/count`

Get the number of finalized transactions. This count may be too low if blocks are missing from the database.

#### Returns `integer`

### GET `/node/payloads/total-size`

Get the total size, in bytes, of all finalized block payloads. This count may be too low if blocks are missing from the database.

#### Returns `integer`

### GET `/node/vid/share`

Get the VID share belonging to this node for a given block.

#### Paths

* `/node/vid/share/:height`
* `/node/vid/share/hash/:hash`
* `/node/vid/share/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="183">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose VID share should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose VID share should be fetched</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block whose VID share should be fetched. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, it is unspecified which one is returned.</td></tr></tbody></table>

#### Returns `VidShare`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`VidShare`](https://hotshot.docs.espressosys.com/hotshot_types/vid/type.VidShare.html) type.

### GET `/node/sync-status`

Get the node's progress in syncing with the latest state of blockchain.

If the node is fully synced (that is, all the `missing` counts are 0 and `pruned_height` is `null` or 0) other endpoints in this API should give accurate results.

#### Returns

```json
{
    "missing_blocks": integer,
    "missing_leaves": integer,
    "missing_vid_common": integer,
    "missing_vid_shares": integer,
    "pruned_height": null | integer,
}
```

### GET `/node/header/window`

Get a range of consecutive headers by timestamp window.

Returns all available headers, in order, whose timestamps fall between `:start` (inclusive) and `:end` (exclusive), or between the block indicated by `:height` or `:hash` (inclusive) and `:end` (exclusive). The response also includes one block before the desired window (unless the window includes the genesis block) and one block after the window. This proves to the client that the server has not omitted any blocks whose timestamps fall within the desired window.

It is possible that not all blocks in the desired window are available when this endpoint is called. In that case, whichever blocks are available are included in the response, and `next` is `null` to indicate that the response is not complete. The client can then use one of the `/from/` forms of this endpoint to fetch the remaining blocks from where the first response left off, once they become available. If no blocks are available, not even `prev`, this endpoint will return an error.

#### Paths

* `/node/header/window/:start/:end`
* `/node/header/window/from/:height/:end`
* `/node/header/window/from/hash/:hash/:end`

#### Parameters

<table><thead><tr><th width="184">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>start</code></td><td><code>integer</code></td><td>Timestamp in seconds where the window should start</td></tr><tr><td><code>end</code></td><td><code>integer</code></td><td>Timestamp in seconds where the window should end</td></tr><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height where the window should start</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Block hash where the window should start</td></tr></tbody></table>

#### Returns

```json
{
    "window": Header,
    "prev": null | Header,
    "next": null | Header
}
```

### GET `/node/stake-table/current` , `/node/stake-table/:epoch`

Get the active stake table for the current epoch or the specified one.

<table><thead><tr><th width="184">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>epoch</code></td><td><code>integer</code></td><td>The epoch number for which to get the stake table.</td></tr></tbody></table>

**Returns**

```json
{
    hex /* address */: {
        "account": hex, // address used to pay fees and collect rewards
        "stake_table_key": tagged<BLS_VER_KEY>,
        "state_ver_key": tagged<SCHNORR_VER_KEY>,
        "stake": integer,
        "commission" integer,
        "delegators": {
            hex /* address */: integer
        }
    }
}
```


# State API

Serves consensus state derived from finalized blocks

All state derived from block data is represented in the form of Merkle trees or Merkle tries, so this API is able to provide select segments of the state with a proof that will convince the client that the returned segment is accurate, as long as they know the corresponding state *commitment* (part of each block header).

## Endpoints

### GET `/fee-state`

Get a Merkle proof proving the balance of a certain fee account in a given snapshot of the state. The element in the returned Merkle proof contains the balance of the requested account, or `null` if the account has no balance.

#### Paths

* `/fee-state/:height/:account`
* `/fee-state/commit/:commit/:account`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>account</code></td><td><code>hex</code></td><td>Fee account to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/fee-state/block-height`

The latest block height for which fee state is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the fee state storage is updated asynchronously.

#### Returns `integer`

## GET `/fee-state/fee-balance/latest/:account`

Convenience endpoint to get the current balance of an account from a trusted node.

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>account</code></td><td><code>hex</code></td><td>Fee account to look up</td></tr></tbody></table>

**Returns** the balance as a plain integer, without proof.

### GET `/block-state`

Get a Merkle proof proving the inclusion of a certain block at a position in the history. The element in the returned Merkle proof contains the commitment of the block at the requested position in history.

#### Paths

* `/block-state/:height/:index`
* `/block-state/commit/:commit/:index`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>index</code></td><td><code>integer</code></td><td>Height of the block to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/block-state/block-height`

The latest block height for which block state is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the block state storage is updated asynchronously.

#### Returns `integer`

## Reward State

The reward state API has two versions:

* **Protocol V3**: Uses reward state v1 with SHA3 hashing (`RewardMerkleTreeV1`)
* **Protocol V4+**: Uses reward state v2 with Keccak256 hashing (`RewardMerkleTreeV2`)

### GET `/reward-state`

Get a Merkle proof proving the balance of a certain reward account in a given snapshot of the state. The element in the returned Merkle proof contains the balance of the requested account, or `null` if the account has no balance.

This endpoint returns a V1 Merkle tree proof.

#### Paths

* `/reward-state/:height/:account`
* `/reward-state/commit/:commit/:account`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>account</code></td><td><code>hex</code></td><td>Reward account to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/reward-state/block-height`

The latest block height for which reward state is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the reward state storage is updated asynchronously.

#### Returns `integer`

### GET `/reward-state/proof/:height/:address`

Get the Merkle proof for a reward account at a given block height. Returns a `RewardAccountQueryDataV1` type, containing the balance and a `RewardAccountProofV1`. This proof is based on `RewardMerkleTreeV1`, which uses the SHA3 hashing algorithm.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height to get proof for</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>Account address to get proof for</td></tr></tbody></table>

#### Returns `RewardAccountQueryDataV1`

```json
{
  "balance": "0x...",
  "proof": {
    "account": "0x...",
    "proof": { /* merkle proof */ }
  }
}
```

**`RewardAccountQueryDataV1`** fields:

<table><thead><tr><th width="135">Field</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>balance</code></td><td><code>U256</code></td><td>The reward account balance</td></tr><tr><td><code>proof</code></td><td><code>RewardAccountProofV1</code></td><td>Merkle proof for the account</td></tr></tbody></table>

**`RewardAccountProofV1`** fields:

<table><thead><tr><th width="135">Field</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>account</code></td><td><code>Address</code></td><td>The reward account address</td></tr><tr><td><code>proof</code></td><td><code>RewardMerkleProofV1</code></td><td>Merkle proof using SHA3 hashing</td></tr></tbody></table>

## Reward State V2

Reward state v2 is used by consensus protocol V4 and above which uses Keccak256 based Merkle proofs for improved compatibility with Ethereum smart contracts.

### GET `/reward-state-v2`

Get a Merkle proof proving the balance of a certain reward account in a given snapshot of the state. The element in the returned Merkle proof contains the balance of the requested account, or `null` if the account has no balance.

#### Paths

* `/reward-state-v2/:height/:account`
* `/reward-state-v2/commit/:commit/:account`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>account</code></td><td><code>hex</code></td><td>Reward account to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/reward-state-v2/block-height`

The latest block height for which reward state v2 is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the reward state storage is updated asynchronously.

#### Returns `integer`

### GET `/reward-state-v2/reward-balance/latest/:address`

Get current balance in reward state.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>address</code></td><td><code>hex</code></td><td>Ethereum address in hex format</td></tr></tbody></table>

#### Returns

The current reward balance as an integer.

### GET `/reward-state-v2/reward-balance/:height/:address`

Get balance in reward state at a specific height.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height to query</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>Ethereum address in hex format</td></tr></tbody></table>

#### Returns

The reward balance at the specified height as an integer.

### GET `/reward-state-v2/proof/:height/:address`

Get the Merkle proof for a reward account at a given block height. Returns a `RewardAccountQueryDataV2` type, containing the balance and a `RewardAccountProofV2`. This proof is based on `RewardMerkleTreeV2`, which uses the Keccak256 hashing algorithm.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of proof for</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>Account address to get proof for</td></tr></tbody></table>

#### Returns `RewardAccountQueryDataV2`

```json
{
  "balance": "0x...",
  "proof": {
    "account": "0x...",
    "proof": {
      "Presence": { /* membership proof */ }
    }
  }
}
```

**`RewardAccountQueryDataV2`** fields:

<table><thead><tr><th width="135">Field</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>balance</code></td><td><code>U256</code></td><td>The reward account balance</td></tr><tr><td><code>proof</code></td><td><code>RewardAccountProofV2</code></td><td>Merkle proof for the account</td></tr></tbody></table>

**`RewardAccountProofV2`** fields:

<table><thead><tr><th width="135">Field</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>account</code></td><td><code>Address</code></td><td>The reward account address</td></tr><tr><td><code>proof</code></td><td><code>RewardMerkleProofV2</code></td><td>Merkle proof</td></tr></tbody></table>

**`RewardMerkleProofV2`** is an enum with two variants:

* **`Presence`**: Merkle proof demonstrating account membership in the tree
* **`Absence`**: Merkle proof demonstrating account non-membership in the tree

### GET `/reward-state-v2/reward-claim-input/:height/:address`

Get the reward claim input data formatted for use with Solidity reward claim contracts. This endpoint is only available for consensus protocol V4+.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Espresso block height (must match Light Client finalized height)</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>Account address to generate claim input for</td></tr></tbody></table>

#### Returns `RewardClaimInput`

```json
{
  "lifetime_rewards": "0x...",
  "auth_data": {
    // Authentication data including Merkle proof
  }
}
```

<table><thead><tr><th width="180">Field</th><th width="180">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>lifetime_rewards</code></td><td><code>U256</code></td><td>Total lifetime rewards for the account</td></tr><tr><td><code>auth_data</code></td><td><code>RewardAuthData</code></td><td>Merkle proof and authentication data for on-chain verification</td></tr></tbody></table>

* The `height` parameter **must match** the finalized block height in the Light Client contract
* Returns error if the account has zero rewards
* The returned data is formatted to be passed directly to reward claim contract functions

#### Error

* **`ZeroRewardError`**: Account has no rewards to claim
* **Conversion Error**: Failed to convert proof to claim input format


# Events API

Streams events from HotShot

This API allows a client, not participating in consensus, to follow along with consensus in a trustless manner, by streaming and verifying events produced by consensus. It is especially useful for block builders, who need to maintain their own view of the internal consensus state at all times, so that they can intelligently propose blocks on top of not-yet-finalized proposed parent blocks.

{% hint style="warning" %}
This API is often served on a different port than other APIs, for reasons that will be resolved in future releases.
{% endhint %}

## Types

### `LeafInfo`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`LeafInfo`](https://hotshot.docs.espressosys.com/hotshot_types/event/struct.LeafInfo.html) type.

### `DAProposal`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`Proposal`](https://hotshot.docs.espressosys.com/hotshot_types/message/struct.Proposal.html) type.

### `QuorumProposal`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`Proposal`](https://hotshot.docs.espressosys.com/hotshot_types/message/struct.Proposal.html) type.

## Endpoints

### GET `/hotshot-events/events`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to consensus events.

#### Yields

```json
{
    "view_number": integer,
    "event":
        {
            "StartupInfo": {
                "known_node_with_stake": [
                    {
                    }
                ]
            }
        }
      | { "HotshotError": { "error": ... } }
      | { "HotshotTransactions": { "transactions": [Transaction] } }
      | {
            "HotshotDecide": {
                "leaf_chain": [LeafInfo],
                "block_size": null | integer
            }
        }
      | {
            "HotshotDAProposal": {
                "proposal": DAProposal,
                "sender": tagged<BLS_VER_KEY>
            }
        }
      | {
            "HotshotQuorumProposal": {
                "proposal": QuorumProposal,
                "sender": tagged<BLS_VER_KEY>
            }
        }
      | "Unknown"
}
```


# Submit API

Submit transactions to the public mempool

## Endpoints

### POST `/submit/submit`

Returns the hash of the transaction if it was successfully submitted. This does not mean the transaction has yet been sequenced. The user can check for inclusion of the transaction using `/availability/transaction/hash/:hash` from the [availability API](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api).

{% hint style="warning" %}
This endpoint will fail with a 400 status code if the submitted transaction has a `namespace` ID larger than 4294967295 (2^32 - 1).
{% endhint %}

#### Request Body `Transaction`

#### Returns `tagged<TX>`


# Earlier Versions

This section contains archive API references for earlier supported versions. Each version includes change notes detailing the differences between it and the subsequent version, as well as a full API reference for that version.


# v0

Reference for v0 REST APIs served by Espresso nodes and query services

API `v0`was the default API version from genesis until the proof-of-stake upgrade. Proof-of-stake is scheduled for April 15, 2025 on testnet and TBD on mainnet, after which `v1` will be the default API version. `v0`will continue to be supported indefinitely, however certain endpoints will fail when querying for data originating after the proof-of-stake upgrade, and fields of certain types which were added in the proof-of-stake upgrade are not accessible via this API.

The differences between `v0`and the subsequent version `v1`are:

* `v0`lacks new fields which were added to the `Leaf`type in `v1` . For leaves created before the proof-of-stake upgrade, the leaf structure without these fields is equivalent to the new structure. However, for leaves created after the proof-of-stake upgrade, it will be impossible to compute accurate commitments or verify consensus artifacts using the `v0`API.
  * `next_epoch_justify_qc`
  * `next_drb_result`
  * `with_epoch`
* `v0`lacks new fields which were added to the `QC` type in `v1` . For QCs created before the proof-of-stake upgrade, the QC structure without these fields is equivalent to the new structure. However, for QCs created after the proof-of-stake upgrade, it will be impossible to compute accurate commitments or verify consensus artifacts using the `v0`API.
  * `epoch`
* The types of VID artifacts (VID shares, [VID common](https://docs.espressosys.com/network/api-reference/espresso-api/..#vidcommon), and [namespace proofs](https://docs.espressosys.com/network/api-reference/espresso-api/..#nsproof)) are different in `v0`and `v1`. For blocks created before the proof-of-stake upgrade, the VID types are equivalent, and any proofs using these types can still be verified using the information returned by the `v0`API. However, the new version of the Rust SDK will not be able to deserialize the `v0`types, and for blocks created after the proof-of-stake upgrade, the `v0`endpoints will return errors.
* `v0`lacks all APIs related to rewards state
* `v0`lacks the `availability/state-cert/:epoch`and `catchup/:height/leafchain`APIs which are necessary for running a consensus client after proof of stake
* `v0`lacks the convenience endpoint `node/stake-table`for fetching the latest stake table from a trusted server


# Status API

Node-specific state and consensus metrics

This API provides insight into the inner workings of consensus. It is primarily useful to the operator of the node, as many of the metrics provided here make for useful [alerts](https://github.com/EspressoSystems/gitbook/blob/main/guides/running-a-sequencer-node.md#monitoring).

## Endpoints

### GET `/status/block-height`

The last known block height of the chain.

#### Returns `integer`

### GET `/status/success-rate`

The view success rate since genesis. This equals the number of views completed divided by the number of successful views, i.e. the block height.

#### Returns `float`

### GET `/status/time-since-last-decide`

The elapsed time, in seconds, since consensus last decided on a block. Useful to alert when consensus is stalled or this node has been disconnected from consensus.

#### Returns `integer`

### GET `/status/metrics`

Exposes all metrics recorded by consensus in Prometheus format.


# Catchup API

Serves recent consensus state to allow peers to catch up with the network

The primary customer of this API is peer consensus nodes who may have recently joined the network or were temporarily disconnected. These nodes need the very latest state, one which hasn't even been finalized yet, in order to start voting and proposing in consensus.

In HotShot, all state required to participate is represented in the form of Merkle trees or Merkle tries, so this API is able to provide select segments of the state with a proof that will convince the client that the returned segment is accurate, as long as they know the corresponding state *commitment*.

## Types

### `Account`

```json
{
    // Account balance in WEI. Serialized as a hex string so as not to exceed the
    // range of JSON integers.
    "balance": hex,
    // Merkle proof justifying "balance" relative to the state commitment.
    "proof": {
        "account": hex,
        "proof":
            { "Presence": MerkleProof },
          | { "Absence": MerkleProof }
        }
    }       
}
```

## Endpoints

### GET `/catchup/:height/:view/account/:address`

Get the balance of the requested fee account in the state from the requested consensus height and view. This is used to fetch the state for *unfinalized* views, to facilitate rapid catchup. If `:view` has already been finalized, this endpoint may fail with error 404.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>The account (Ethereum address) to look up</td></tr></tbody></table>

#### Returns `Account`

### POST `/catchup/:height/:view/accounts`

Bulk version of `/catchup/:height/:view/account`. The request body should be a JSON array consisting of `TaggedBase64`-encoded fee accounts.

The response is a `FeeMerkleTree` containing sub-trees for each of the requested accounts, which is\
a more condensed way to represent the union of account proofs for each requested account. Individual\
Merkle proofs for each account can be extracted from this tree.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr></tbody></table>

#### Returns `FeeMerkleTree`

### GET `/catchup/:height/:view/blocks`

Get the Merkle frontier (path to most recently inserted element) of the accumulator of blocks, from the requested consensus view. This is used to fetch the state for *unfinalized* views, to facilitate rapid catchup. If `:view` has already been finalized, this endpoint may fail with error 404.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the frontier</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the frontier</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/catchup/chain-config/:commitment`

Get the chain config with the given hash.

#### Parameters

<table><thead><tr><th width="126.4453125">Name</th><th width="215.55859375">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>commitment</code></td><td><code>tagged&#x3C;CHAIN_CONFIG></code></td><td>The hash of the chain config to look up</td></tr></tbody></table>

**Returns** `ChainConfig`


# Availability API

Serves data recorded by the Tiramisu DA layer, such as committed blocks

The availability API is the place to get onchain data, like blocks and transactions. It is the primary interface for downstream components like rollups and end users.

The API is designed to be *robust* and *pure*. Robust means that if the node hosting the API misses some data, for example from being offline when a certain block was finalized, it will automatically fetch the missing data from a peer, and will eventually fetch and store all finalized data. Pure means that each endpoint is a pure function -- with the exception of occasionally returning 404 for missing data, each endpoint will always give the same response given the same parameters.

Due to purity, this API provides no aggregate queries, like block or transaction counts, which might change as missing data is fetched. Likewise, every endpoint takes some specification of the exact point in the chain the client is looking for, like a block height or hash. There is no "latest block" query. Thus, most real-world use cases will need to complement the availability API with use of the [node API](https://docs.espressosys.com/network/api-reference/espresso-api/node-api).

## Organization

While this API has many endpoints, don't be intimidated -- there is a method to the madness. The API is organized around collections of different resources, each of which corresponds to blocks and can be indexed by block height or hash.

### Resources

* Leaves
* Headers
* Blocks
* Block summaries
* Payloads
* VID common

### Indices

Each of these resources can be addressed in the following ways:

* `<resource>/:height`
* `<resource>/hash/:hash`
* `<resource>/payload-hash/:payload-hash`

{% hint style="warning" %}
Not all of the indices are implemented for all resources, although in principle they can be. The supported indices are documented below for each endpoint. Future releases will fill in the missing functionality.
{% endhint %}

{% hint style="warning" %}
Leaves are currently indexed slightly differently from other resources. See documentation on leaf endpoints. Future versions of this API will merge the concept of a leaf and a header, resolving this discrepancy.
{% endhint %}

In addition, there are endpoints to fetch a range of each resource (`<resource>/:form/:until`) and to subscribe to a WebSockets stream (`/stream/<resource>/:from`).

## Types

### `BlockSummary`

```json
{
    "header": Header,
    "hash": tagged<BLOCK>,
    "size": integer,
    "num_transactions": integer
}
```

### `BlockResponse`

```json
{
    "header": Header,
    "payload": Payload,
    "hash": tagged<BLOCK>,
    "size": integer,
    "num_transactions": integer
}
```

### `LeafResponse`

```json
{
    "leaf": Leaf,
    "qc": QC,
}
```

### `PayloadResponse`

```json
{
    "data": Payload,
    "height": integer,
    "size": integer,
    "block_hash": tagged<BLOCK>,
    "hash": tagged<HASH>
}
```

### `VidCommonResponse`

```json
{
    "common": VidCommon,
    "block_hash": tagged<BLOCK>,
    "payload_hash": tagged<HASH>
}
```

## Endpoints

### GET `/availability/leaf`

#### Paths

* `/availability/leaf/:height`
* `/availability/leaf/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the leaf to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;COMMIT></code></td><td>Hash of the leaf to fetch</td></tr></tbody></table>

#### Returns `LeafResponse`

### GET `/availability/leaf/:from/:until`

Retrieve a range of consecutive leaves.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first leaf to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last leaf to fetch</td></tr></tbody></table>

#### Returns `[LeafResponse]`

### GET `/availability/stream/leaves/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of leaves, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first leaf to yield</td></tr></tbody></table>

#### Yields `LeafResponse`

### GET `/availability/header`

#### Paths

* `/availability/header/:height`
* `/availability/header/hash/:hash`
* `/availability/header/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the header to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the header to fetch</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the header to fetch. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `Header`

### GET `/availability/header/:from/:until`

Retrieve a range of consecutive headers.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first header to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last header to fetch</td></tr></tbody></table>

#### Returns `[Header]`

### GET `/availability/stream/headers/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of headers, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first header to yield</td></tr></tbody></table>

#### Yields `Header`

### GET `/availability/block`

#### Paths

* `/availability/block/:height`
* `/availability/block/hash/:hash`
* `/availability/block/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block to fetch</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block to fetch. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `BlockResponse`

### GET `/availability/block/:from/:until`

Retrieve a range of consecutive blocks.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first block to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last block to fetch</td></tr></tbody></table>

#### Returns `[BlockResponse]`

### GET `/availability/stream/blocks/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of blocks, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first block to yield</td></tr></tbody></table>

#### Yields `BlockResponse`

### GET `/availability/block/summary`

#### Paths

* `/availability/block/summary/:height`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block to fetch</td></tr></tbody></table>

#### Returns `BlockSummary`

### GET `/availability/block/summaries/:from/:until`

Retrieve a range of consecutive block summaries.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first block summary to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last block summary to fetch</td></tr></tbody></table>

#### Returns `[BlockSummary]`

### GET `/availability/payload`

#### Paths

* `/availability/payload/:height`
* `/availability/payload/block-hash/:block-hash`
* `/availability/payload/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose payload should be fetched</td></tr><tr><td><code>block-hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose payload should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload to fetch. Note that block payloads are not necessarily unique. If there are multiple payloads matching this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `PayloadResponse`

### GET `/availability/payload/:from/:until`

Retrieve a range of consecutive payloads.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first payload to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last payload to fetch</td></tr></tbody></table>

#### Returns `[PayloadResponse]`

### GET `/availability/stream/payloads/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of payloads, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first payload to yield</td></tr></tbody></table>

#### Yields `PayloadResponse`

### GET `/availability/vid/common`

#### Paths

* `/availability/vid/common/:height`
* `/availability/vid/common/hash/:hash`
* `/availability/vid/common/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose VID common data should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose VID common data should be fetched</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block whose VID common data should be fetched. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `VidCommonResponse`

### GET `/availability/stream/vid/common/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of VID common objects, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first VID common to yield</td></tr></tbody></table>

#### Yields `VidCommonResponse`

### GET `/availability/block/:height/namespace/:namespace`

Get the list of transactions in a block from a given namespace, along with a proof that these are only and all such transactions from that block. Note that the proof may be `null` if `transactions` is empty, in which case the caller should check the namespace table for the specified block to confirm that `:namespace` is not present.

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block containing the desired namespace</td></tr><tr><td><code>namespace</code></td><td><code>integer</code></td><td>ID of the desired namespace</td></tr></tbody></table>

#### Returns

```json
{
    "transactions": [Transaction],
    "proof": NsProof | null
}
```

### GET `/availability/transaction`

#### Paths

* `/availability/transaction/:height/:index`
* `/availability/transaction/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block containing the desired transaction</td></tr><tr><td><code>index</code></td><td><code>integer</code></td><td>0-based position of the desired transaction in its block</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;TX></code></td><td>Hash of the desired transaction. Note that transactions are not necessarily unique. If there are multiple transactions matching this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns

```json
{
    "transaction": Transaction,
    "hash": tagged<TX>,
    "index": integer,
    "proof": TransactionInclusionProof,
    "block_hash": tagged<BLOCK>,
    "block_height": integer
}
```

The response contains the hash of the transaction, the hash and height of the block that contains it, and its index within that block. It also contains a `TransactionInclusionProof`, which proves inclusion of this transaction in the block with `block_hash`. The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`TxInclusionProof`](https://github.com/EspressoSystems/espresso-sequencer/blob/8ff3c9200b6bdefa9fa6f30b46b16a1b69cea5a1/sequencer/src/block/queryable.rs#L174) type.

### GET `/availability/limits`

Get implementation-defined limits restricting certain requests.

* `small_object_range_limit`: the maximum number of small objects which can be loaded in a single range query. Currently small objects include leaves only. In the future this limit will also apply to headers, block summaries, and VID common, however
  * loading of headers and block summaries is currently implemented by loading the entire block
  * imperfect VID parameter tuning means that VID common can be much larger than it should
* `large_object_range_limit`: the maximum number of large objects which can be loaded in a single range query. Large objects include anything that *might* contain a full payload or an object proportional in size to a payload. Note that this limit applies to the entire class of objects: we do not check the size of objects while loading to determine which limit to apply. If an object belongs to a class which might contain a large payload, the large object limit always applies.

**Returns**

```json
{
    "large_object_range_limit": integer,
    "small_object_range_limit": integer
}
```

[^1]: This breaks purity. This will be addressed in a future version of the API.


# Node API

Complements the availability API by serving eventually consistent data that is not necessarily agreed upon by all nodes

The [availability API](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api) provides a pure view of snapshots of the Espresso blockchain at various points in time. Because it strives for robustness and purity, it does not include aggregate statistics like block or transaction counts, which may briefly return incorrect results and will gradually correct themselves as missing data is fetched. The node API does provide this data, making it a useful complement to the availability API.

In other words, while the availability API is a view of the blockchain abstractly, the node API provides information about *this node's* view of the chain, at the present moment in time.

## Endpoints

### GET `/node/block-height`

Get the height of the chain as known to this node. This is equal to one more than the height of the latest known block. It is *not* a count of the blocks in this node's database, as blocks earlier than the latest known block could be missing.

#### Returns `integer`

### GET `/node/transactions/count`

Get the number of finalized transactions. This count may be too low if blocks are missing from the database.

#### Returns `integer`

### GET `/node/payloads/total-size`

Get the total size, in bytes, of all finalized block payloads. This count may be too low if blocks are missing from the database.

#### Returns `integer`

### GET `/node/vid/share`

Get the VID share belonging to this node for a given block.

#### Paths

* `/node/vid/share/:height`
* `/node/vid/share/hash/:hash`
* `/node/vid/share/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="183">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose VID share should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose VID share should be fetched</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block whose VID share should be fetched. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, it is unspecified which one is returned.</td></tr></tbody></table>

#### Returns `VidShare`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`VidShare`](https://hotshot.docs.espressosys.com/hotshot_types/vid/type.VidShare.html) type.

### GET `/node/sync-status`

Get the node's progress in syncing with the latest state of blockchain.

If the node is fully synced (that is, all the `missing` counts are 0 and `pruned_height` is `null` or 0) other endpoints in this API should give accurate results.

#### Returns

```json
{
    "missing_blocks": integer,
    "missing_leaves": integer,
    "missing_vid_common": integer,
    "missing_vid_shares": integer,
    "pruned_height": null | integer,
}
```

### GET `/node/header/window`

Get a range of consecutive headers by timestamp window.

Returns all available headers, in order, whose timestamps fall between `:start` (inclusive) and `:end` (exclusive), or between the block indicated by `:height` or `:hash` (inclusive) and `:end` (exclusive). The response also includes one block before the desired window (unless the window includes the genesis block) and one block after the window. This proves to the client that the server has not omitted any blocks whose timestamps fall within the desired window.

It is possible that not all blocks in the desired window are available when this endpoint is called. In that case, whichever blocks are available are included in the response, and `next` is `null` to indicate that the response is not complete. The client can then use one of the `/from/` forms of this endpoint to fetch the remaining blocks from where the first response left off, once they become available. If no blocks are available, not even `prev`, this endpoint will return an error.

#### Paths

* `/node/header/window/:start/:end`
* `/node/header/window/from/:height/:end`
* `/node/header/window/from/hash/:hash/:end`

#### Parameters

<table><thead><tr><th width="184">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>start</code></td><td><code>integer</code></td><td>Timestamp in seconds where the window should start</td></tr><tr><td><code>end</code></td><td><code>integer</code></td><td>Timestamp in seconds where the window should end</td></tr><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height where the window should start</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Block hash where the window should start</td></tr></tbody></table>

#### Returns

```json
{
    "window": Header,
    "prev": null | Header,
    "next": null | Header
}
```


# State API

Serves consensus state derived from finalized blocks

All state derived from block data is represented in the form of Merkle trees or Merkle tries, so this API is able to provide select segments of the state with a proof that will convince the client that the returned segment is accurate, as long as they know the corresponding state *commitment* (part of each block header).

## Endpoints

### GET `/fee-state`

Get a Merkle proof proving the balance of a certain fee account in a given snapshot of the state. The element in the returned Merkle proof contains the balance of the requested account, or `null` if the account has no balance.

#### Paths

* `/fee-state/:height/:account`
* `/fee-state/commit/:commit/:account`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>account</code></td><td><code>hex</code></td><td>Fee account to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/fee-state/block-height`

The latest block height for which fee state is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the fee state storage is updated asynchronously.

#### Returns `integer`

## GET `/fee-state/fee-balance/latest/:account`

Convenience endpoint to get the current balance of an account from a trusted node.

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>account</code></td><td><code>hex</code></td><td>Fee account to look up</td></tr></tbody></table>

**Returns** the balance as a plain integer, without proof.

### GET `/block-state`

Get a Merkle proof proving the inclusion of a certain block at a position in the history. The element in the returned Merkle proof contains the commitment of the block at the requested position in history.

#### Paths

* `/block-state/:height/:index`
* `/block-state/commit/:commit/:index`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>index</code></td><td><code>integer</code></td><td>Height of the block to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/block-state/block-height`

The latest block height for which block state is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the block state storage is updated asynchronously.

#### Returns `integer`


# Events API

Streams events from HotShot

This API allows a client, not participating in consensus, to follow along with consensus in a trustless manner, by streaming and verifying events produced by consensus. It is especially useful for block builders, who need to maintain their own view of the internal consensus state at all times, so that they can intelligently propose blocks on top of not-yet-finalized proposed parent blocks.

{% hint style="warning" %}
This API is often served on a different port than other APIs, for reasons that will be resolved in future releases.
{% endhint %}

## Types

### `LeafInfo`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`LeafInfo`](https://hotshot.docs.espressosys.com/hotshot_types/event/struct.LeafInfo.html) type.

### `DAProposal`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`Proposal`](https://hotshot.docs.espressosys.com/hotshot_types/message/struct.Proposal.html) type.

### `QuorumProposal`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`Proposal`](https://hotshot.docs.espressosys.com/hotshot_types/message/struct.Proposal.html) type.

## Endpoints

### GET `/hotshot-events/events`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to consensus events.

#### Yields

```json
{
    "view_number": integer,
    "event":
        {
            "StartupInfo": {
                "known_node_with_stake": [
                    {
                    }
                ]
            }
        }
      | { "HotshotError": { "error": ... } }
      | { "HotshotTransactions": { "transactions": [Transaction] } }
      | {
            "HotshotDecide": {
                "leaf_chain": [LeafInfo],
                "block_size": null | integer
            }
        }
      | {
            "HotshotDAProposal": {
                "proposal": DAProposal,
                "sender": tagged<BLS_VER_KEY>
            }
        }
      | {
            "HotshotQuorumProposal": {
                "proposal": QuorumProposal,
                "sender": tagged<BLS_VER_KEY>
            }
        }
      | "Unknown"
}
```


# Submit API

Submit transactions to the public mempool

## Endpoints

### POST `/submit/submit`

Returns the hash of the transaction if it was successfully submitted. This does not mean the transaction has yet been sequenced. The user can check for inclusion of the transaction using `/availability/transaction/hash/:hash` from the [availability API](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api).

{% hint style="warning" %}
This endpoint will fail with a 400 status code if the submitted transaction has a `namespace` ID larger than 4294967295 (2^32 - 1).
{% endhint %}

#### Request Body `Transaction`

#### Returns `tagged<TX>`


# Builder API

The following describes the API endpoints a builder needs to support in order to build blocks in Espresso.

{% hint style="warning" %}
These API endpoints are actively maintained and might change going forward.
{% endhint %}

### **GET `block_info/availableblocks/:parent_hash/:view_number/:sender/:signature:`**

This endpoint allows a sequencer node to query a builder for a list of available blocks that the builder can provide, ensuring consistency with the ongoing consensus defined by the specified `parent_hash`.

#### Parameters

<table><thead><tr><th width="163">Name</th><th width="157">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>parent_hash</code></td><td><code>TaggedBase64</code></td><td>The hash of the parent block in the current consensus chain. This parameter ensures that the returned blocks are valid continuations of the existing chain.</td></tr><tr><td><code>view_number</code></td><td><code>Integer</code></td><td>View number in Hotshot.</td></tr><tr><td><code>sender</code></td><td><code>TaggedBase64</code></td><td>The address or identifier of the entity making the request (i.e., the sequencer node).</td></tr><tr><td><code>signature</code></td><td><code>TaggedBase64</code></td><td>A cryptographic signature generated by the sequencer node, authenticating the request and proving its authenticity</td></tr></tbody></table>

#### Returns

```json
[
    { 
        "block_hash": TaggedBase64,
        "block_size": integer,
        "offered_fee": integer,
        "signature": TaggedBase64,
        "sender": TaggedBase64
    }
]
```

### GET `block_info/claimblock/:block_hash/:view_number/:sender/:signature:`

Upon receiving the metadata about available blocks through the previously mentioned endpoint, the sequencer node will utilize this dedicated endpoint to retrieve the complete and comprehensive content of *chosen* block. This endpoint will provide the sequencer node with the entirety of the block data, including all transactions, consensus data, and any other pertinent information encapsulated within the block. By leveraging this endpoint, the sequencer node can access and process the complete block content, enabling it to perform its designated functions effectively inside the Hotshot consensus.

Parameters

<table><thead><tr><th width="163">Name</th><th width="157">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>block_hash</code></td><td><code>TaggedBase64</code></td><td>The hash of the block provided as a response in previous API.</td></tr><tr><td><code>view_number</code></td><td><code>Integer</code></td><td>View number in Hotshot.</td></tr><tr><td><code>sender</code></td><td><code>TaggedBase64</code></td><td>The address or identifier of the entity making the request (i.e., the sequencer node).</td></tr><tr><td><code>signature</code></td><td><code>TaggedBase64</code></td><td>A cryptographic signature generated by the sequencer node, authenticating the request and proving its authenticity</td></tr></tbody></table>

#### Returns

```json
{ 
    "block_payload": Payload,
    "metadata": MetaData,
    "signature": TaggedBase64,
    "sender": TaggedBase64
}
```

### **GET** `block_info/claimheaderinput/:block_hash/:view_number/:sender/:signature`

This endpoint enables a sequencer node to retrieve the relevant fee information associated with a specific block, facilitating a transparent payout mechanism for the builder responsible for constructing that block.

{% hint style="info" %}
**Note:** The `block_hash` should match the one requested in previous API i.e `claim_block` for consistent fee payoff.
{% endhint %}

Parameters

<table><thead><tr><th width="163">Name</th><th width="157">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>block_hash</code></td><td><code>TaggedBase64</code></td><td>The hash of the block provided as a response in first API.</td></tr><tr><td><code>view_number</code></td><td><code>Integer</code></td><td>View number in Hotshot.</td></tr><tr><td><code>sender</code></td><td><code>TaggedBase64</code></td><td>The address or identifier of the entity making the request (i.e., the sequencer node).</td></tr><tr><td><code>signature</code></td><td><code>TaggedBase64</code></td><td>A cryptographic signature generated by the sequencer node, authenticating the request and proving its authenticity</td></tr></tbody></table>

#### Returns

```json
{ 
    "vid_commitment": VidCommitment, 
    "vid_precompute_data": VidPrecomputeData,
    "fee_signature": TaggedBase64,
    "signature": "TaggedBase64,
    "sender" = TaggedBase64 
}
```

### POST `/txn_submit/submit`

It enables external user to submit directly to builder's private transactions mempool.

* Returns the hash of the transaction if it was successfully submitted. This does not mean the transaction has yet been sequenced. The user can check for inclusion of the transaction using `/availability/transaction/hash/:hash` from the [availability API](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api).
  * Request Body `Transaction`
  * Returns `tagged<TX>`

### POST `/txn_submit/batch`

It enables external user to submit a list of transactions to builder's private transactions mempool.

* Returns the corresponding list of transaction hashes if it were successfully submitted. This does not mean the transaction has yet been sequenced. The user can check for inclusion of the transaction using `/availability/transaction/hash/:hash` from the [availability API](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api).
  * Request Body `Vec<Transaction>`
  * Returns `Vec<tagged<TX>>`

### GET `/txn_submit/status/:transaction_hash`

It enables external user to track the status of submitted transactions in short period, old transaction will be pruned if the map doesn't have enough space.

* Returns the status of the queried transaction commitment if successfully retrieved. The status will be one of the following: "Pending", "Unknown" or "Rejected" (with a reason message). The status "Sequenced" is not yet supported. While this information can be obtained from the query service or block explorer, transactions with a "Sequenced" status will appear as "Pending" when retrieved. An error will be returned if the request fails due to issues like malformed input, incorrect deserialization, or missing data.
  * Request Body `tagged<TX>`

#### Returns

```json
  { "Pending" }
```

or

```json
  { "Unknown" }
```

or

```json
  { "Rejected": { "reason": TaggedBase64 } }
```

or

```json
  {  "error": TaggedBase64 }
```


# Mainnet 1

Espresso Mainnet 1 release

Mainnet 1 upgrades the Espresso network to support permissionless participation through delegated proof of stake.

The upgrade goes live on [Decaf testnet](https://docs.espressosys.com/network/releases/testnets/decaf-testnet) April 18, 2025. Mainnet upgrade will follow, date to be announced.


# Running a Mainnet 1 Node

This page provides the specific configuration used to run different types of nodes in Mainnet 1.

{% hint style="info" %}
🫵 TL;DR: For operator running Mainnet 0 nodes, the critical changes from that configuration are as follows:

* The new container image version is <https://github.com/EspressoSystems/espresso-network/pkgs/container/espresso-sequencer%2Fsequencer/703041349?tag=20260223>
* Use v1 APIs for all peer URLs
* The `state`API module is now required. It will be enabled automatically and should no longer be specified on the command line.
* Both `ESPRESSO_SEQUENCER_L1_PROVIDER` and `ESPRESSO_SEQUENCER_L1_WS_PROVIDER` now need to be provided. See the variables listed below for details
  {% endhint %}

The container image to use for this deployment is

* [Tag 20260302](https://github.com/EspressoSystems/espresso-network/pkgs/container/espresso-sequencer%2Fsequencer/713568135?tag=20260302)
* Which is built of the branch: [release-mainnet-1.0.1-rc](https://github.com/EspressoSystems/espresso-network/tree/release-mainnet-1.0.1-rc) if you are building from source

{% hint style="info" %}
The configuration for all node types includes `ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml`. This file is built into the official Docker images. Operators building their own images will need to ensure [this file](https://github.com/EspressoSystems/espresso-network/blob/20241120-patch5/data/genesis/mainnet.toml) is included and their nodes are pointed at it.
{% endhint %}

## Staking

Regardless of the type of node being operated, if you are starting a node for the first time, it will need to be registered in the stake table and have some stake delegated to it in order to participate in consensus.

{% hint style="info" %}
With the initial release of Mainnet 1, participation is limited to a dynamic, permissionless set of 100 nodes. In each epoch (period of roughly 24 hours) the 100 nodes with the most delegated stake form the active participation set.
{% endhint %}

### Registering a Node

In order for a node to participate, it must be registered in the stake table contract on Ethereum. During this process, the node's consensus keys are associated with a unique Ethereum address. This Ethereum address will receive commission, but does not exist on the node itself.

Interfacing with the stake table can be done using the `staking-cli`. Here is the command to use to register a node in the stake table:

```bash
docker run -e L1_PROVIDER -e STAKE_TABLE_ADDRESS -e MNEMONIC -e ACCOUNT_INDEX \
	-e CONSENSUS_PRIVATE_KEY -e STATE_PRIVATE_KEY \
	ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
	staking-cli register-validator \
	--commission $COMMISSION
```

Where:

| Environment Variable    | Meaning                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `L1_PROVIDER`           | The RPC provider URL to use when interacting with the L1                                                                                                                                             |
| `STAKE_TABLE_ADDRESS`   | The Mainnet stake table address. This is 0xCeF474D372B5b09dEfe2aF187bf17338Dc704451                                                                                                                  |
| `MNEMONIC`              | The Ethereum mnemonic to use in combination with `ACCOUNT_INDEX` to derive an Ethereum keypair unique to this node                                                                                   |
| `ACCOUNT_INDEX`         | The Ethereum account index to use in combination with `MNEMONIC` to derive an Ethereum keypair unique to this node                                                                                   |
| `CONSENSUS_PRIVATE_KEY` | The node's staking-specific consensus key. This key looks something like: `BLS_SIGNING_KEY~...`                                                                                                      |
| `STATE_PRIVATE_KEY`     | The node's state-specific consensus key. This key looks something like: `SCHNORR_SIGNING_KEY~...`                                                                                                    |
| `COMMISSION`            | The proportion of rewards that the validator will earn, expressed as a decimal between 0 and 1 with up to two decimal places. The remaining rewards will be distributed proportionally to delegators |

Here are some additional requirements:

* Each Ethereum account used (derived from `MNEMONIC` + `ACCOUNT_INDEX`) must have enough gas funds on the L1 to call the registration method of the contract.
* Each BLS (Espresso) key can be registered only once.
* The commission cannot be changed later. One would need to deregister the validator, register another one, and direct delegators to redelegate in order to change it.
* Remember, each Ethereum account can only be used to register a single validator once. For multiple validators, at a minimum, different account indices (or mnemonics) must be used.

\
The output of a successful register transaction command should be of the following form:

{% code overflow="wrap" %}

```
2025-04-08T13:47:14.516160Z  INFO staking_cli: Registering validator 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 with commission 12.34 %
2025-04-08T13:47:14.829268Z  INFO staking_cli: Success! transaction hash: 0xa632dfea882d80855d2cc5e6713d9fc839cdd5df5aa29f6e9ce8d5a5ec8da615
```

{% endcode %}

### Deregistering a Node

At any time after registration, you may choose to stop participating by deregistering. This will automatically remove all of your delegators.

```bash
docker run \
    -e MNEMONIC -e ACCOUNT_INDEX -e L1_PROVIDER -e ESP_TOKEN_ADDRESS=0x031De51F3E8016514Bd0963d0B2AB825A591Db9A \
    -e STAKE_TABLE_ADDRESS=0xCeF474D372B5b09dEfe2aF187bf17338Dc704451 \
    ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
        staking-cli deregister-validator
```

### Delegation

In order for a node to participate after it is registered, it must have Espresso tokens delegated to it. These can come from any users who hold Espresso tokens and wish to secure the network and earn rewards through staking. To bootstrap, it is possible for the node operator themselves to delegate to their own node, if they hold Espresso tokens.

To delegate to a registered node, the `staking-cli`can also be used:

```bash
docker run \
    -e MNEMONIC -e ACCOUNT_INDEX -e L1_PROVIDER -e ESP_TOKEN_ADDRESS=0x031De51F3E8016514Bd0963d0B2AB825A591Db9A \
    -e STAKE_TABLE_ADDRESS=0xCeF474D372B5b09dEfe2aF187bf17338Dc704451 \
    ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
        delegate --validator-address $ADDRESS --amount $DELEGATION_AMOUNT
```

The delegation can always be removed using the `undelegate`command with the same arguments.

### More commands (+ Ledger support)

For more information on the staking CLI (including information on how to use it with a Ledger device), visit the README [here](https://github.com/EspressoSystems/espresso-network/blob/1fce836c0fcef7e0a2d0a2e981a22f122c22950a/staking-cli/README.md).

## Environment

When starting a node for the first time, set `ESPRESSO_SEQUENCER_CONFIG_PEERS`to the URL of a trusted node. This is used to fetch configuration required to join the P2P network. For example, this could be set to `https://cache.main.net.espresso.network` to use the Espresso Systems-operated nodes to fetch the config.

Once your node has successfully joined the network once, it should store the config locally, and this parameter will not be required on future restarts.

## 1. Regular Node

#### Command

```
sequencer -- http -- catchup -- status
```

Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_EMBEDDED_DB=true
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics and healthchecks
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to store sqlite database
ESPRESSO_SEQUENCER_STORAGE_PATH # e.g. /mount/sequencer/store/

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

**Volumes**

* `$ESPRESSO_SEQUENCER_STORAGE_PATH`
* `$ESPRESSO_SEQUENCER_KEY_FILE`

Note: Instead of using the above variable `$ESPRESSO_SEQUENCER_KEY_FILE` to load your keys from a file, you can also set the following two individually:

* `$ESPRESSO_SEQUENCER_PRIVATE_STAKING_KEY` -> `BLS_SIGNING_KEY~...`
* `$ESPRESSO_SEQUENCER_PRIVATE_STATE_KEY` -> `SCHNORR_SIGNING_KEY~...`

## 2. DA Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server. There is no need to run a DA node unless you are included in the DA committee. Most operators can ignore this.
{% endhint %}

#### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

#### Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_POSTGRES_PRUNE="true"
ESPRESSO_SEQUENCER_IS_DA="true"
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network/v1
ESPRESSO_SEQUENCER_API_PEERS=https://query.main.net.espresso.network/v1
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and DA API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

#### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

#### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

#### Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_IS_DA=true
ESPRESSO_SEQUENCER_ARCHIVE=true
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network/v1
ESPRESSO_SEQUENCER_API_PEERS=https://query.main.net.espresso.network/v1
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and query API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

#### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

Note: Instead of using the above variable `$ESPRESSO_SEQUENCER_KEY_FILE` to load your keys from a file, you can also set the following two individually:

* `$ESPRESSO_SEQUENCER_PRIVATE_STAKING_KEY` -> `BLS_SIGNING_KEY~...`
* `$ESPRESSO_SEQUENCER_PRIVATE_STATE_KEY` -> `SCHNORR_SIGNING_KEY~...`

## Hardware requirements

Hardware requirements are still in flux, but for now we recommend the following:

**Non-DA Node**: 1 Core CPU, 8GB memory\
\
**DA Node**: (Sequencer) 4 core CPU, 8GB memory + (Database) 2 Core, 4GB memory.

**Storage (DA node):** 1.2 TB SSD minimum, ability to scale on demand.

**Storage (Pruning DA node):** 100 GB

**Storage (non-DA Node):** Negligible, kilobytes


# Contracts

## Fee Contract

This contract is used for depositing $ETH for paying fees in the Espresso network.

[0x7f15ff3f783acd4d09c6a79d098ed5069a2bd39a](https://etherscan.io/address/0x7f15ff3f783acd4d09c6a79d098ed5069a2bd39a)

## Stake Table Contract

Mainnet 1 adds a contract for staking and delegation.

TBD

## Light Client Contracts

Espresso Mainnet maintains [light client contracts](https://github.com/EspressoSystems/gitbook/blob/main/learn/the-espresso-network/internal-functionality/light-client.md) that rollups and other applications integrating with Espresso can use to read the state of the Espresso network in a trust-minimized way.

* Light client on Ethereum (for L2s integrating Espresso): [0x95ca91cea73239b15e5d2e5a74d02d6b5e0ae458](https://etherscan.io/address/0x95ca91cea73239b15e5d2e5a74d02d6b5e0ae458)
* Light client on Arbitrum (for Orbit L3s integrating Espresso): [0x47495bb99cccbb1bda9f15b32b69093137f886db](https://arbiscan.io/address/0x47495bb99cccbb1bda9f15b32b69093137f886db)


# Rollup Migration Guide

Migrating rollup integrations from Mainnet 0 to Mainnet 1

If you have a rollup using the Espresso network version 0 for confirmations, some changes are necessary in order to be compatible with version 1. These changes should be minimal. They must be completed before April 15 for the Decaf testnet. There is no date yet for upgrading Mainnet rollups.

**Estimated Effort:** 1 engineer-day

## Rust Integrations

1. Update dependencies:

<pre class="language-toml"><code class="lang-toml">hotshot-types = { git = "https://github.com/EspressoSystems/espresso-network", default-features = false, tag = "20250412-dev-node-pos-preview" }
<strong>hotshot-query-service = { git = "https://github.com/espressosystems/espresso-network", tag = "20250412-dev-node-pos-preview" }
</strong>espresso-types = { git = "https://github.com/espressosystems/espresso-network", tag = "20250412-dev-node-pos-preview" }
</code></pre>

2. The following types have been moved to different modules, so you may have to adjust some import statements:

```rust
use hotshot_query_service::VidCommon;
use hotshot_types::{data::VidCommitment, light_client::hash_bytes_to_field};
```

## Go Integrations

1. Update the Espresso Go SDK:

```go-module
require github.com/EspressoSystems/espresso-network-go v0.0.35
```

## All Integrations

1. Change the API you use to connect to the Espresso query service from `v0`to `v1`(as in `https://query.decaf.testnet.espresso.network/v1`or `https://query.main.net.espresso.network/v1`.
2. Test your integration with the new version of Espresso. You can run a local Espresso network in `v1`mode using a fork of the Espresso dev node, with the usual options: `ghcr.io/espressosystems/espresso-sequencer/espresso-dev-node:20250412-dev-node-pos-preview`


# Mainnet 0

Espresso Mainnet 0 release — October 2024

Mainnet 0 marks the production release of the Espresso Network. This release is an important step towards enabling Espresso's vision of an ecosystem of open, composable and permissionless applications.

Espresso’s Global Confirmation Layer will support applications such as rollups with faster bridging, and lays the groundwork for chains to improve coordination amongst each other, enhancing cross-chain interoperability.

Underpinning the Espresso Network is HotShot, which will be run in a production setting for the first time. During the initial stages of Mainnet 0, HotShot will be run by a set of 20 node operators, running 100 nodes in total. An important upcoming milestone will be to open up participation to more node operators and increase economic security through proof-of-stake.

During the initial release, block size has conservatively been set to 1 MB, with plans to scale up to 5 MB in the short term if there is sufficient demand. We expect it to take around \~8 seconds for a transaction to be confirmed in the initial release. In the short term, an update to HotShot will implement ideas from HotStuff-2 to reduce this time to \~5-6 seconds. In the medium term, [a VID update is in the works](https://espresso.discourse.group/t/faster-vid-on-espresso-s-critical-path/39) that will enable confirmation latency of \~3 seconds, even as we scale to thousands of consensus nodes. This will also enable us to increase the blocksize further without greatly impacting latency.

You can track activity on Mainnet in our [block explorer](https://explorer.main.net.espresso.network), and you can interact with it via the [public API endpoint](https://query.main.net.espresso.network).


# Running a Mainnet 0 Node

This page provides the specific configuration used to run different types of nodes in Mainnet 0.

{% hint style="warning" %}
Note: during Mainnet 0 only a fixed set of preregistered operators can run a node. The Espresso Network will upgrade to proof-of-stake in a later release.
{% endhint %}

{% hint style="info" %}
🫵 TL;DR: For operator running Decaf nodes, the critical changes from that configuration are as follows:

* All URLs supplied by Espresso have changed
* The new container image version is `20250228-patch3`
* The JSON-RPC endpoints specified by `ESPRESSO_SEQUENCER_L1_PROVIDER` and `ESPRESSO_SEQUENCER_L1_WS_PROVIDER` should be Ethereum mainnet endpoints instead of Sepolia
  {% endhint %}

The container image to use for this deployment is

* `ghcr.io/espressosystems/espresso-sequencer/sequencer:20250228-patch3` (if using Espresso's images)
* built off of the branch `20250228-patch3` (if building from source)

{% hint style="info" %}
The configuration for all node types includes `ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml`. This file is built into the official Docker images. Operators building their own images will need to ensure [this file](https://github.com/EspressoSystems/espresso-network/blob/20241120-patch5/data/genesis/mainnet.toml) is included and their nodes are pointed at it.
{% endhint %}

## 1. Regular Node

#### Command

```
sequencer -- http -- catchup -- status
```

Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-kdrhoi6lwz.main.net.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics and healthchecks
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to store consensus state
ESPRESSO_SEQUENCER_STORAGE_PATH # e.g. /mount/sequencer/store/

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

**Volumes**

* `$ESPRESSO_SEQUENCER_STORAGE_PATH`
* `$ESPRESSO_SEQUENCER_KEY_FILE`

## 2. DA Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

#### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

#### Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-kdrhoi6lwz.main.net.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_POSTGRES_PRUNE="true"
ESPRESSO_SEQUENCER_IS_DA="true"
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.main.net.espresso.network
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and DA API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

#### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

#### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query -- state`

#### Environment

**Same for all nodes**

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-kdrhoi6lwz.main.net.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.main.net.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.main.net.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/mainnet.toml
ESPRESSO_SEQUENCER_IS_DA=true
ESPRESSO_SEQUENCER_ARCHIVE=true
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"
# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.main.net.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.main.net.espresso.network
```

**Chosen by operators**

```
# An HTTP JSON-RPC endpoint for Ethereum Mainnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://mainnet.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Ethereum Mainnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://mainnet.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and query API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

#### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

## Hardware requirements

Hardware requirements are still in flux, but for now we recommend the following:

**Non-DA Node**: 1 Core CPU, 2GB memory\
\
**DA Node**: (Sequencer) 4 core CPU, 8GB memory + (Database) 2 Core, 4GB memory.

**Storage (DA node):** 1.2 TB SSD minimum, ability to scale on demand.

**Storage (non-DA Node):** Negligible, kilobytes


# Contracts

Espresso Mainnet maintains [light client contracts](https://github.com/EspressoSystems/gitbook/blob/main/learn/the-espresso-network/internal-functionality/light-client.md) that rollups and other applications integrating with Espresso can use to read the state of the Espresso network in a trust-minimized way.

* Light client on Ethereum (for L2s integrating Espresso): [0x95ca91cea73239b15e5d2e5a74d02d6b5e0ae458](https://etherscan.io/address/0x95ca91cea73239b15e5d2e5a74d02d6b5e0ae458)
* Light client on Arbitrum (for Orbit L3s integrating Espresso): [0x47495bb99cccbb1bda9f15b32b69093137f886db](https://arbiscan.io/address/0x47495bb99cccbb1bda9f15b32b69093137f886db)


# Testnets

Overview of current and past testnets

Espresso Systems has released and deployed several testnets since 2022:

* [Decaf](https://docs.espressosys.com/network/releases/testnets/decaf-testnet), our ongoing persistent testnet
* [Cappuccino](https://docs.espressosys.com/network/releases/testnets/cappuccino-testnet-release) (May 2024)
* [Gibraltar](https://docs.espressosys.com/network/releases/testnets/gibraltar-testnet-release) (January 2024)
* [Cortado](https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release) (September 2023)
* [Doppio](https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release) (July 2023)
* [Americano](https://docs.espressosys.com/network/releases/testnets/americano-testnet-release) (November 2022)


# Decaf Testnet Release

Espresso Persistent Testnet (Decaf) — September 2024

In September of 2024, we launched Decaf, which will run as a persistent testnet of the Espresso system alongside the upcoming Mainnet release.

Decaf continues the process of decentralizing Espresso, by onboarding an additional 13 node operators, bringing the total operator set to 24. These 24 operators will run 100 geographically distributed nodes, all participating in HotShot consensus together.\
\
You can track activity on the Decaf testnet in our [block explorer](https://explorer.decaf.testnet.espresso.network/), and you can interact with Decaf via the [public API endpoint](https://query.decaf.testnet.espresso.network/v1/).


# Running a Node

Configuration for Decaf nodes

{% hint style="warning" %}
Decaf node operators are limited to a select group. If you are interested in running a node in a future release of Espresso, [contact us](https://y3at7jy5knf.typeform.com/to/KgayxNsX?typeform-source=webflow.com).
{% endhint %}

This page give the configuration used to run different types of nodes in the Decaf testnet. For general information on running an Espresso node, see <https://docs.espressosys.com/network/guides/node-operators/running-a-sequencer-node>.

All nodes in Decaf use the `ghcr.io/espressosystems/espresso-sequencer/sequencer:20251106-patch1` Docker image, or an equivalent image built from source. Depending on the type of node, the configuration varies.

{% hint style="info" %}
The configuration for all node types includes `ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/decaf.toml`. This file is built into the official Docker images. Operators building their own images will need to ensure [this file](https://github.com/EspressoSystems/espresso-network/blob/20250910-patch1/data/genesis/decaf.toml) is included and their nodes are pointed at it.
{% endhint %}

## Staking

Regardless of the type of node being operated, if you are starting a node for the first time, it will need to be registered in the stake table and have some stake delegated to it in order to participate in consensus.

{% hint style="info" %}
With the initial release of Proof-of-stake, participation is limited to a dynamic, permissionless set of 100 nodes. In each epoch (period of roughly 24 hours) the 100 nodes with the most delegated stake form the active participation set.
{% endhint %}

### Registering a Node

In order for a node to participate, it must be registered in the stake table contract on Ethereum Sepolia. During this process, the node's consensus keys are associated with a unique Ethereum address. This Ethereum address will receive commission, but does not exist on the node itself.

Interfacing with the stake table can be done using the `staking-cli`. Here is the command to use to register a node in the stake table:

```bash
docker run -e L1_PROVIDER -e STAKE_TABLE_ADDRESS -e MNEMONIC -e ACCOUNT_INDEX \
	-e CONSENSUS_PRIVATE_KEY -e STATE_PRIVATE_KEY \
	ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
	staking-cli register-validator \
	--commission $COMMISSION
```

Where:

| Environment Variable    | Meaning                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `L1_PROVIDER`           | The RPC provider URL to use when interacting with the L1. This should be an Ethereum Sepolia endpoint for Decaf                                                                                      |
| `STAKE_TABLE_ADDRESS`   | The Decaf stake table address. This is `0x40304fbe94d5e7d1492dd90c53a2d63e8506a037`                                                                                                                  |
| `MNEMONIC`              | The Ethereum mnemonic to use in combination with `ACCOUNT_INDEX` to derive an Ethereum keypair unique to this node                                                                                   |
| `ACCOUNT_INDEX`         | The Ethereum account index to use in combination with `MNEMONIC` to derive an Ethereum keypair unique to this node                                                                                   |
| `CONSENSUS_PRIVATE_KEY` | The node's staking-specific consensus key. This key looks something like: `BLS_SIGNING_KEY~...`                                                                                                      |
| `STATE_PRIVATE_KEY`     | The node's state-specific consensus key. This key looks something like: `SCHNORR_SIGNING_KEY~...`                                                                                                    |
| `COMMISSION`            | The proportion of rewards that the validator will earn, expressed as a decimal between 0 and 1 with up to two decimal places. The remaining rewards will be distributed proportionally to delegators |

Here are some additional requirements:

* Each Ethereum account used (derived from `MNEMONIC` + `ACCOUNT_INDEX`) must have enough gas funds on the L1 to call the registration method of the contract.
* Each BLS (Espresso) key can be registered only once.
* The commission cannot be changed later. One would need to deregister the validator, register another one, and direct delegators to redelegate in order to change it.
* Remember, each Ethereum account can only be used to register a single validator once. For multiple validators, at a minimum, different account indices (or mnemonics) must be used.

\
The output of a successful register transaction command should be of the following form:

{% code overflow="wrap" %}

```
2025-04-08T13:47:14.516160Z  INFO staking_cli: Registering validator 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266 with commission 12.34 %
2025-04-08T13:47:14.829268Z  INFO staking_cli: Success! transaction hash: 0xa632dfea882d80855d2cc5e6713d9fc839cdd5df5aa29f6e9ce8d5a5ec8da615
```

{% endcode %}

### Deregistering a Node

At any time after registration, you may choose to stop participating by deregistering. This will automatically remove all of your delegators.

```bash
docker run \
    -e MNEMONIC -e ACCOUNT_INDEX -e L1_PROVIDER \
    -e STAKE_TABLE_ADDRESS=0x40304fbe94d5e7d1492dd90c53a2d63e8506a037 \
    -e ESP_TOKEN_ADDRESS=0xb3e655a030e2e34a18b72757b40be086a8f43f3b \
    ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
        staking-cli deregister-validator
```

### Delegation

In order for a node to participate after it is registered, it must have Espresso tokens delegated to it. These can come from any users who hold Espresso tokens and wish to secure the network and earn rewards through staking. To bootstrap, it is possible for the node operator themselves to delegate to their own node, if they hold Espresso tokens.

To delegate to a registered node, the `staking-cli`can also be used:

```bash
docker run \
    -e MNEMONIC -e ACCOUNT_INDEX -e L1_PROVIDER \
    -e STAKE_TABLE_ADDRESS=0x40304fbe94d5e7d1492dd90c53a2d63e8506a037 \
    -e ESP_TOKEN_ADDRESS=0xb3e655a030e2e34a18b72757b40be086a8f43f3b \
    ghcr.io/espressosystems/espresso-sequencer/staking-cli:main \
        delegate --validator-address $ADDRESS --amount $DELEGATION_AMOUNT
```

The delegation can always be removed using the `undelegate`command with the same arguments.

### More commands (+ Ledger support)

For more information on the staking CLI (including information on how to use it with a Ledger device), visit the README [here](https://github.com/EspressoSystems/espresso-network/blob/1fce836c0fcef7e0a2d0a2e981a22f122c22950a/staking-cli/README.md).

## Environment

When starting a node for the first time, set `ESPRESSO_SEQUENCER_CONFIG_PEERS`to the URL of a trusted node. This is used to fetch configuration required to join the P2P network. For example, this could be set to `https://cache.decaf.testnet.espresso.network` to use the Espresso Systems-operated nodes to fetch the config.

Once your node has successfully joined the network once, it should store the config locally, and this parameter will not be required on future restarts.

## 1. Regular Node

### Command

`sequencer -- http -- catchup -- status`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-UZAFTUIMZOT.decaf.testnet.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.decaf.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/decaf.toml
RUST_LOG="warn,hotshot_libp2p_networking=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.decaf.testnet.espresso.network
```

#### Chosen by operators

```
# An HTTP JSON-RPC endpoint for Sepolia testnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Sepolia testnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://sepolia.infura.io/v3/<API-KEY>

# Port on which to host metrics and healthchecks
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to store consensus state
ESPRESSO_SEQUENCER_STORAGE_PATH # e.g. /mount/sequencer/store/

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

**Volumes**

* `$ESPRESSO_SEQUENCER_STORAGE_PATH`
* `$ESPRESSO_SEQUENCER_KEY_FILE`

Note: Instead of using the above variable `$ESPRESSO_SEQUENCER_KEY_FILE` to load your keys from a file, you can also set the following two individually:

* `$ESPRESSO_SEQUENCER_PRIVATE_STAKING_KEY` -> `BLS_SIGNING_KEY~...`
* `$ESPRESSO_SEQUENCER_PRIVATE_STATE_KEY` -> `SCHNORR_SIGNING_KEY~...`

## 2. DA Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-UZAFTUIMZOT.decaf.testnet.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.decaf.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/decaf.toml
ESPRESSO_SEQUENCER_POSTGRES_PRUNE="true"
ESPRESSO_SEQUENCER_IS_DA="true"

RUST_LOG="warn,hotshot_libp2p_networking=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.decaf.testnet.espresso.network
```

#### Chosen by operators

```
# An HTTP JSON-RPC endpoint for Sepolia testnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Sepolia testnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://sepolia.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and DA API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

## Archival Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator-UZAFTUIMZOT.decaf.testnet.espresso.network/
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.decaf.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/decaf.toml
ESPRESSO_SEQUENCER_IS_DA=true
ESPRESSO_SEQUENCER_ARCHIVE=true

RUST_LOG="warn,hotshot_libp2p_networking=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.decaf.testnet.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.decaf.testnet.espresso.network
```

#### Chosen by operators

```
# An HTTP JSON-RPC endpoint for Sepolia testnet. This is required
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# A `ws://` or `wss://` endpoint for Sepolia testnet. This is optional but
# recommended since it decreases the load on your provider.
ESPRESSO_SEQUENCER_L1_WS_PROVIDER # e.g. wss://sepolia.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and query API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD

# The address to bind Libp2p to in host:port form. Other nodes should be able to
# access this; i.e. port must be open for UDP.
ESPRESSO_SEQUENCER_LIBP2P_BIND_ADDRESS

# The address we should advertise to other nodes as being our Libp2p endpoint
# (in host:port form). It should resolve a connection to the above bind address; i.e.
# should use public IP address or hostname, and forward to the port given in the bind
# address.
ESPRESSO_SEQUENCER_LIBP2P_ADVERTISE_ADDRESS
```

**Volumes**

* `$ESPRESSO_SEQUENCER_STORAGE_PATH`
* `$ESPRESSO_SEQUENCER_KEY_FILE`

Note: Instead of using the above variable `$ESPRESSO_SEQUENCER_KEY_FILE` to load your keys from a file, you can also set the following two individually:

* `$ESPRESSO_SEQUENCER_PRIVATE_STAKING_KEY` -> `BLS_SIGNING_KEY~...`
* `$ESPRESSO_SEQUENCER_PRIVATE_STATE_KEY` -> `SCHNORR_SIGNING_KEY~...`

## TCP optimizations

We ask also that operators perform some TCP optimizations to improve the networking performance of their nodes. Listed below are the different ways to apply them depending on how your node is set up:

### When using Docker Compose

Add the following to your `sequencer` service:

```
sysctls:
    net.ipv4.tcp_congestion_control: "bbr"
    net.ipv4.tcp_rmem: "8192 262144 67108864"
    net.ipv4.tcp_wmem: "4096 16384 536870912"
    net.ipv4.tcp_adv_win_scale: "0"
    net.ipv4.tcp_notsent_lowat: "131072"
    net.ipv4.tcp_slow_start_after_idle: "0"
```

### When just using Docker

Modify your `docker run` command like so:

```
docker run \
    --sysctl net.ipv4.tcp_congestion_control="bbr" \
    --sysctl net.ipv4.tcp_rmem="8192 262144 67108864" \
    --sysctl net.ipv4.tcp_wmem="4096 16384 536870912" \
    --sysctl net.ipv4.tcp_adv_win_scale="0" \
    --sysctl net.ipv4.tcp_notsent_lowat="131072" \
    --sysctl net.ipv4.tcp_slow_start_after_idle="0" \	
    ..
```

### When running natively

1. Create a file at `/etc/sysctl.d/espresso-opts.conf`
2. Add the following to it:

   ```
   net.ipv4.tcp_congestion_control=bbr
   net.ipv4.tcp_rmem=8192 262144 67108864
   net.ipv4.tcp_wmem=4096 16384 536870912 
   net.ipv4.tcp_adv_win_scale=0
   net.ipv4.tcp_notsent_lowat=131072
   net.ipv4.tcp_slow_start_after_idle=0
   ```
3. Run this command to apply the new settings without rebooting:

   ```
   sudo sysctl -p /etc/sysctl.d/espresso-opts.conf
   ```

Note: this will apply the TCP optimizations to *all* TCP connections on your machine.

## Hardware requirements

Hardware requirements are still in flux, but for now we recommend the following:

**Non-DA Node**: 1 Core CPU, 2GB memory\
\
**DA Node**: (Sequencer) 4 core CPU, 8GB memory + (Database) 2 Core, 4GB memory.

**Storage (DA node):** 1.2 TB SSD minimum, ability to scale on demand.

**Storage (non-DA Node):** Negligible, kilobytes


# Contracts

Decaf testnet maintains [light client contracts](https://github.com/EspressoSystems/gitbook/blob/main/learn/the-espresso-network/internal-functionality/light-client.md) that rollups and other applications integrating with the testnet can use to read the state of the Decaf network in a trust-minimized way.

* Light client on Sepolia testnet (for L2 testnets integrating Espresso): [0x303872bb82a191771321d4828888920100d0b3e4](https://sepolia.etherscan.io/address/0x303872bb82a191771321d4828888920100d0b3e4)
* Light client on Arbitrum Sepolia (for Orbit L3 testnets integrating Espresso): [0x08d16cb8243b3e172dddcdf1a1a5dacca1cd7098](https://sepolia.arbiscan.io/address/0x08d16cb8243b3e172dddcdf1a1a5dacca1cd7098)


# Cappuccino Testnet Release

Espresso testnet 5 (Cappuccino)—May 2024

{% hint style="warning" %}
With the release of [Decaf](https://docs.espressosys.com/network/releases/testnets/decaf-testnet), Espresso's persistent testnet, the Cortado testnet is currently paused.
{% endhint %}

In May 2024, we announced the Cappuccino release of Espresso.

Cappuccino continues the process of decentralizing Espresso, by onboarding a total of 10 operators to participate in Cappuccino. The 10 operators will be running a total of 100 geographically distributed nodes, all participating in HotShot together.

The Tiramisu DA layer is now also further upgraded and supports VID, which ensures that data is recoverable, even if the CDN and DA committee fail to be responsive.

As part of the Arbitrum tech stack integration, Espresso now supports Arbitrum Nitro fraud proofs, which enables Arbitrum chains to be fully productized on top of Espresso. We will be releasing test versions of Arbitrum Orbit chains in collaboration with Caldera and AltLayer.\
You can track activity on the Cappuccino testnet in our new block explorer here: <https://explorer.cappuccino.testnet.espresso.network/>\
\
And you can interact with Cappuccino via the public endpoint here:\
<https://query.cappuccino.testnet.espresso.network/v0/>


# Running a Node

Configuration for Cappuccino nodes

{% hint style="warning" %}
Cappuccino node operators are limited to a select group. If you are interested in running a node in a future release of Espresso, [contact us](https://y3at7jy5knf.typeform.com/to/KgayxNsX?typeform-source=webflow.com).
{% endhint %}

This page give the configuration used to run different types of nodes in the Cappuccino testnet. For general information on running an Espresso node, see [https://github.com/EspressoSystems/gitbook/blob/main/guides/running-a-sequencer-node.md](https://github.com/EspressoSystems/gitbook/blob/main/guides/running-a-sequencer-node.md "mention").

All nodes in Cappuccino use the `ghcr.io/espressosystems/espresso-sequencer/sequencer:cappuccino` Docker image. Depending on the type of node, the configuration varies.

## Regular Node

### Command

`sequencer -- http -- catchup -- status`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator.cappuccino.testnet.espresso.network
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.cappuccino.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.cappuccino.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/cappuccino.toml
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.cappuccino.testnet.espresso.network
```

#### Chosen by operators

```
# JSON-RPC endpoint for Sepolia testnet
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# Port on which to host metrics and healthchecks
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to store consensus state
ESPRESSO_SEQUENCER_STORAGE_PATH # e.g. /mount/sequencer/store/

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env
```

### Volumes

* `$ESPRESSO_SEQUENCER_STORAGE_PATH`
* `$ESPRESSO_SEQUENCER_KEY_FILE`

## DA Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator.cappuccino.testnet.espresso.network
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.cappuccino.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.cappuccino.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/cappuccino.toml
ESPRESSO_SEQUENCER_POSTGRES_PRUNE="true"
ESPRESSO_SEQUENCER_PRUNER_PRUNING_THRESHOLD="549755813888" # 0.5 TB
ESPRESSO_SEQUENCER_PRUNER_MINIMUM_RETENTION="1d"
ESPRESSO_SEQUENCER_PRUNER_TARGET_RETENTION="7d"
ESPRESSO_SEQUENCER_PRUNER_BATCH_SIZE=5000
ESPRESSO_SEQUENCER_IS_DA="true"
ESPRESSO_SEQUENCER_FETCH_RATE_LIMIT=25

RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.cappuccino.testnet.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.cappuccino.testnet.espresso.network
```

#### Chosen by operators

```
# JSON-RPC endpoint for Sepolia testnet
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and DA API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD
```

### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`

## Archival Node

{% hint style="info" %}
Requires operator to additionally run a Postgres server
{% endhint %}

### Command

`sequencer -- storage-sql -- http -- catchup -- status -- query -- state`

### Environment

#### Same for all nodes

```
ESPRESSO_SEQUENCER_ORCHESTRATOR_URL=https://orchestrator.cappuccino.testnet.espresso.network
ESPRESSO_SEQUENCER_CDN_ENDPOINT=cdn.cappuccino.testnet.espresso.network:1737
ESPRESSO_STATE_RELAY_SERVER_URL=https://state-relay.cappuccino.testnet.espresso.network
ESPRESSO_SEQUENCER_GENESIS_FILE=/genesis/cappuccino.toml
ESPRESSO_SEQUENCER_FETCH_RATE_LIMIT=25
RUST_LOG="warn,libp2p=off"
RUST_LOG_FORMAT="json"

# At least one state peer is required. The following URL provided by Espresso works.
# Optionally, add endpoints for additional peers, separated by commas.
ESPRESSO_SEQUENCER_STATE_PEERS=https://query.cappuccino.testnet.espresso.network
ESPRESSO_SEQUENCER_API_PEERS=https://query.cappuccino.testnet.espresso.network
```

#### Chosen by operators

```
# JSON-RPC endpoint for Sepolia testnet
ESPRESSO_SEQUENCER_L1_PROVIDER # e.g. https://sepolia.infura.io/v3/<API-KEY>

# Port on which to host metrics, healthchecks, and query API
ESPRESSO_SEQUENCER_API_PORT # e.g. 80

# Path in container to keystore
ESPRESSO_SEQUENCER_KEY_FILE # e.g. /mount/sequencer/keys/0.env

# Connection to Postgres
ESPRESSO_SEQUENCER_POSTGRES_HOST
ESPRESSO_SEQUENCER_POSTGRES_USER
ESPRESSO_SEQUENCER_POSTGRES_PASSWORD
```

### Volumes

* `$ESPRESSO_SEQUENCER_KEY_FILE`


# Deploying a Rollup on Cappuccino

Users interested in deploying their own rollup on Cappuccino can make use of the following

* Query Service: <https://query.cappuccino.testnet.espresso.network>
* Light client contract address: `0xfdbf8b5ed2c16650aa835315a67d83eda5c98872`

For more information on deploying an Arbitrum Nitro chain to Cappuccino, please see the following [guide](https://espressosys.notion.site/Espresso-Nitro-Integration-Configuration-265fd4460c6741199e29159eb77cb879). This makes use of our Arbitrum Nitro integration with Espresso.


# Benchmarks

Performance metrics for HotShot consensus and Tiramisu data availability in Espresso's Cappuccino testnet release

As a part of launching the Cappuccino testnet and releasing our implementation of HotShot under the MIT license, we are publishing benchmarks related to performance of this release. Compared to [earlier benchmarks](https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release/benchmarks), these results benchmark the addition of [Tiramisu DA's Savoiardi layer](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu) to the HotShot protocol.

In our evaluations, we progressively increased the block size from 50KB to 20MB and tested on network sizes ranging from 10 to 1000 nodes. In all settings, a subset of 10 nodes serves both as validators and the committee for Tiramisu DA's Mascarpone layer. As shown in the below figure, throughput rises with the increasing load without a corresponding increase in latency, up to a certain point of saturation. Beyond this point, latency begins to increase while throughput either remains steady or shows a slight increase. In the below table, we show the benchmark data for block sizes of 5MB block size, which is approximately the turning point.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-8ce603cfa536650389f2058a6ff3df1bba1bbb71%2Fhotshot-cappuccino-benchmarks.png?alt=media" alt=""><figcaption><p>HotShot throughput vs. end-to-end latency for varying network sizes and increasing block sizes</p></figcaption></figure>

<table><thead><tr><th data-type="number">Network Size</th><th data-type="number">Mascarpone Committee Size</th><th data-type="number">Block Size (MB)</th><th>Average Latency (s)</th><th data-type="number">Average View Time (s)</th><th data-type="number">Throughput (MB/s)</th></tr></thead><tbody><tr><td>10</td><td>10</td><td>5</td><td>3</td><td>1.08</td><td>4.58</td></tr><tr><td>100</td><td>10</td><td>5</td><td>2</td><td>0.85</td><td>5.76</td></tr><tr><td>200</td><td>10</td><td>5</td><td>4</td><td>1.21</td><td>4.04</td></tr><tr><td>500</td><td>10</td><td>5</td><td>9</td><td>1.97</td><td>2.48</td></tr><tr><td>1000</td><td>10</td><td>5</td><td>21</td><td>5.56</td><td>0.88</td></tr></tbody></table>

## Experimental Setup

These benchmarks were run on HotShot version 0.5.63.

We conducted our experiments on two types of machines:

* CDN Instances: Our CDN (repository located [here](https://github.com/EspressoSystems/Push-CDN)) is a distributed and fault-tolerant system responsible for routing messages between validators. The CDN was run across 3 Amazon EC2 `m6a.xlarge` instances located in the `us-east-2` region. Each instance ran a broker, which is the component responsible for forwarding messages to their intended recipients. One instance also ran the marshal service, which is the service that facilitates the authentication and marshaling of validators to a specific broker. Each instance had 4 vCPUs and 16.0 GiB memory.
* Validator Instances: HotShot nodes were run on Amazon ECS tasks with 2 vCPUs and 4 GiB memory. Nodes were equally distributed among the `us-east-2a`, `us-east-2b` and `us-east-2c` availability zones.

## Data Calculation

Each benchmark was run until 100 blocks were committed. After each benchmark run, nodes reported:

* the total time elapsed for the run
* the throughput per second
* the total latency
* the total number of blocks committed
* the total number of views it took to reach 100 commits
* the number of failed views (views that failed to make progress)

These values were collected and averaged in the final results. Note that throughput is measured in megabytes per second, not mebibytes per second.

## Analysis of Results

* Our implementation of the Tiramisu data availability protocol achieves better maximum throughput in large networks than standard consensus protocols where data is sent to all nodes. That being said, this particular implementation’s latency is worse in large networks. However, we’ve identified several implementation-specific bottlenecks to fix this issue.
* During benchmarks where the network is unsaturated with data, small network sizes (10 and 100 nodes) achieve finality in \~1s, and large network sizes (500, and 1000 nodes) achieve finality between 2-5s.
* The primary bottlenecks of this particular implementation are twofold:
  * Our current implementation of Tiramisu DA's Savoiardi layer is compute-intensive. This causes builders, leaders, and Mascarpone DA committee members to spend additional time computing Savoiardi shares during each view. This bottleneck can be addressed by more optimally parallelizing intensive compute, dynamically tuning Savoiardi parameters such as multiplicity to optimally encode block data, experimenting with different hardware such as GPUs, and having the Cocoa layer optimistically calculate Savoiardi shares.
  * The builder used in these benchmarks is a simple, naive builder. Unlike a sophisticated builder, this builder does no optimistic execution or optimistic Savoiardi calculations. The simple builder does not begin building blocks until the HotShot leader requests it to do so. This causes the builder to be slow in returning block data to the HotShot leader, thus adding unneeded latency each view. This bottleneck can be addressed by using a sophisticated builder that optimistically builds blocks.
* This implementation of HotShot uses the HotStuff-1 protocol. We plan to upgrade to the HotStuff-2 protocol in the future, which will reduce commit latency significantly.

## Notes

* These benchmarks did not use a public transaction mempool. Instead, block builders were configured to build predetermined-sized blocks each view. This configuration is equivalent to block builders only building blocks with privately-sent transactions. A public mempool is part of the current HotShot implementation, however, and will be included in future benchmarks. Note that throughput and latency results will differ with the inclusion of the public mempool.
* **Multiplicity:** Tiramisu DA's Savoiardi VID scheme is inspired by Ethereum's danksharding proposal, where the block payload is viewed as a list of polynomial coefficients. Ordinarily, these coefficients are partitioned into multiple polynomials, and each storage node gets one evaluation from each of those polynomials. At the other extreme, one could instead gather these coefficients into a single high-degree polynomial, and give each storage node multiple evaluations from this polynomial. We use the word “multiplicity” to denote the number of evaluations per polynomial sent to each storage node. Multiplicity is a parameter that can be tuned between two extremes to optimize performance.


# Gibraltar Testnet Release

Espresso testnet 4 (Gibraltar)—January 2024

{% hint style="warning" %}
With the release of [Cappuccino](https://docs.espressosys.com/network/releases/testnets/cappuccino-testnet-release) (testnet 5), the Cortado testnet is currently paused.
{% endhint %}

In January 2024, we announced the Gibraltar release of Espresso.

Gibraltar includes a number of key highlights. Firstly, we have built an integration with Arbitrum Nitro, allowing anyone to easily deploy an instance of the Arbitrum technology stack on Espresso. Secondly, we have made important progress on [Savoiardi](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu#Part-III-Tiramisu-The-Three-Layered-Espresso-DA), an implementation of verifiable information dispersal (VID), which forms the backbone of our Tiramisu DA solution. VID is what allows us to effectively move transaction dissemination from the critical path of consensus, while retaining full DA guarantees. This enables extremely high data throughput and low latency while maintaining a large consensus set.

As part of the Gibraltar public testnet release, Caldera will be deploying an instance of Arbitrum Nitro called [Milan](https://milan.caldera.dev/) onto Espresso. Caldera's OP stack rollup, Vienna, will also be migrated to Gibraltar. This marks the first time these rollup stacks will run alongside each other on Espresso. Cartesi has also made their own integration (of [Rickroll](https://twitter.com/EspressoSys/status/1712199798973972773) fame) even easier to use, and we will be adding docs to easily deploy your own Cartesi rollup on Espresso in the coming weeks.

Gibraltar also marks the first time that Espresso is being run by a set of external node operators, in collaboration with Blockdaemon, marking an important step towards the decentralization of the protocol.


# Interacting with Gibraltar

{% hint style="warning" %}
**Note:** The Gibraltar testnet deployment will be frequently reset, thereby wiping out all user balances and history.
{% endhint %}

{% hint style="warning" %}
**Note:** The Vienna OP stack rollup will not be deployed immediately after the release of Gibraltar, but we will make an announcement when it is running soon after. The Milan Arbitrm Nitro rollup will be available to use immediately.
{% endhint %}

1. If not yet set up, install [MetaMask](https://metamask.io/) and set up a new wallet.
2. In MetaMask, click on the upper left icon to select a network.
3. Click "Add network" -> "Add a network manually".

![](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-e5024f533dcc74f22e547044acecc48925d60376%2Fimage.png?alt=media)

4. To interact with Milan, the Arbitrum Nitro rollup, add a network with these parameters:
   * Network name: `Gibraltar Milan`
   * New RPC URL: `https://milan-devnet.rpc.caldera.xyz/http`
   * Chain ID: `83782`
   * Block explorer URL: `https://milan-devnet.explorer.caldera.xyz/`
   * Currency symbol: `SepoliaETH`
5. To interact with Vienna, the OP Stack rollup, add a network with these parameters:
   * Network name: `Gibraltar Vienna`
   * New RPC URL: `https://vienna.calderachain.xyz/http`
   * Chain ID: `0xc0ffee1`
   * Block explorer URL: `https://vienna.calderaexplorer.xyz`
   * Currency symbol: `SepoliaETH`

## Preconfirmations

As in our previous testnet, Espresso uses the HotShot consensus protocol to provide fast confirmations of new blocks. These confirmations are secure, in that a block confirmed by HotShot is guaranteed to execute in the order determined by HotShot unless at least 1/3 of the total value staked in consensus is corrupt. They are also fast: a block may be confirmed by HotShot well before the same block is eventually processed by the layer 1 blockchain.

For the Gibraltar testnet, the Vienna OP chain as well as the Milan Arbitrum Nitro chain are both using these preconfirmations, so you should experience low latency on the order of a few seconds for both rollups. However, note that MetaMask only refreshes pending transactions every 7 seconds. You may find it easier to observe low latency in the Vienna and Milan block explorers.

For Vienna go to`https://vienna.calderaexplorer.xyz/address/<address>`, replacing `<address>` with your address in MetaMask. For Milan, go to `https://milan-gibraltar.explorer.caldera.xyz/address/<address>` and input your address. At the bottom you will see a section titled "Transactions", showing all the transactions made by this address. Now make a transfer in MetaMask on the Gibraltar Vienna or Milan network and see how fast it appears in the block explorer!

## Faucet

For the Gibraltar Vienna OP stack rollup, you can requests funds from the [faucet](https://vienna.caldera.dev/). Similarly, for the Milan Arbitrum Nitro rollup you can request funds from the [faucet](https://milan.caldera.dev/faucet). You can also directly deposit Sepolia ETH into the rollup using the [Vienna bridge](https://vienna.calderabridge.xyz/) or [Milan bridge](https://milan-gibraltar.calderabridge.xyz/). Sepolia ETH can be obtained from the [Sepolia faucet](https://sepoliafaucet.com/).


# Arbitrum Nitro integration


# Deploying a Rollup on Gibraltar

Users interested in deploying their own rollup on Gibraltar can make use of the following endpoint: <https://query.gibraltar.aws.espresso.network/>

The contract address for Gibraltar is: `0x44abe4628415ABAE6e41f95644d7198800A35786`

We will also be adding a guide to easily deploy a Cartesi rollup on the Gibraltar testnet in the coming weeks.


# Cortado Testnet Release

Espresso testnet 3 (Cortado)—September 2023

{% hint style="warning" %}
With the release of [Gibraltar](https://docs.espressosys.com/network/releases/testnets/gibraltar-testnet-release) (testnet 4), the Cortado testnet is currently paused.
{% endhint %}

In September 2023, we announced the Cortado release of Espresso.

The primary highlight of the Cortado release is the integration of a second rollup stack with Espresso: the [OP Stack](https://stack.optimism.io/). This integration is a direct result of the work that Espresso completed in [developing a leader election interface for the OP Stack](https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release/op-stack-integration/optimism-leader-election-rfp), for which Espresso was awarded an Optimism RFP in July 2023. Details on the OP Stack integration can be found [here](https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release/op-stack-integration).

We've deployed a public Cortado testnet, integrated with two rollups of different stacks: an OP Stack rollup (called Vienna, deployed in collaboration with [Caldera](https://caldera.xyz/)) and a Polygon zkEVM rollup. Instructions for interacting with this testnet can be found [here](https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release/interacting-with-doppio).


# Interacting with Cortado

{% hint style="warning" %}
**Note:** The Cortado testnet deployment will be frequently reset, thereby wiping out all user balances and history.
{% endhint %}

1. If not yet set up, install [MetaMask](https://metamask.io/) and set up a new wallet.
2. In MetaMask, click on the upper left icon to select a network.
3. Click "Add network" -> "Add a network manually".

![](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-e5024f533dcc74f22e547044acecc48925d60376%2Fimage.png?alt=media)

4. To interact with Vienna, the OP Stack rollup, add a network with these parameters:
   * Network name: `Cortado Vienna`
   * New RPC URL: `https://vienna.calderachain.xyz/http`
   * Chain ID: `0xc0ffee1`
   * Block explorer URL: `https://vienna.calderaexplorer.xyz`
   * Currency symbol: `SepoliaETH`
5. To interact with the Polygon zkEVM stack rollup, add a network with these parameters:

   * Network name: `Cortado Polygon`
   * New RPC URL: `https://polygon-preconfirmations.cortado.espresso.network`
   * Chain ID: `0xc0ffee2`

   For "Currency symbol", anything can be set (the native currency on the Polygon zkEVM stack rollup is a dummy testnet token produced by the faucet, and there is no bridge to SepoliaETH). "Block explorer URL" should be left blank.

## Preconfirmations

The Espresso Sequencer uses the HotShot consensus protocol to provide fast confirmations of new blocks. These confirmations are secure, in that a block confirmed by HotShot is guaranteed to execute in the order determined by HotShot unless at least 1/3 of the total value staked in consensus is corrupt. They are also fast: a block may be confirmed by HotShot well before the same block is eventually processed by the layer 1 blockchain.

The RPC node for Cortado Polygon that you connected to above uses these "preconfirmations" from HotShot to achieve low latency, but there is a second RPC node that does not. In MetaMask, try going to Settings -> Networks -> Cortado Polygon and changing RPC URL to `https://polygon.cortado.espresso.network`. Then transfer some ETH on the Cortado Polygon network. Do you notice a difference in the speed with which the transaction gets confirmed?

For the Cortado testnet, the Vienna OP chain is only running a single RPC node, which does use preconfirmations, so you should experience low latency on the order of a few seconds there as well. However, note that MetaMask only refreshes pending transactions every 7 seconds. You may find it easier to observe low latency in the Vienna block explorer. Go to `https://vienna.calderaexplorer.xyz/address/<address>`, replacing `<address>` with your address in MetaMask. At the bottom you will see a section titled "Transactions", showing all the transactions made by this address. Now make a transfer in MetaMask on the Cortado Vienna network. How quickly does the new transaction appear in the block explorer?

## Faucet

For the Cortado Vienna OP stack rollup, you can requests funds from the [faucet](https://vienna.caldera.dev/). You can also directly deposit Sepolia ETH into the rollup using the [Caldera bridge](https://vienna.calderabridge.xyz/). Sepolia ETH can be obtained from the [Sepolia faucet](https://sepoliafaucet.com/).

For the Polygon zkEVM stack rollup, you can request funds in the [Discord](https://discord.com/invite/YHZPk5dbcq) `#faucet` channel with the following command: `/faucet <address>` To copy your MetaMask address, click on the address at the top of the MetaMask panel.


# OP Stack Integration

Proof-of-concept integration with the OP (Optimism) stack

Espresso has created a proof-of-concept integration of the OP Stack with Espresso. This integration highlights Espresso’s vision of connecting and decentralizing rollups without compromising the scale and speed that rollup users have grown accustomed to.

## Integration Design

We designed this integration with the following goals in mind:

1. The L2 block sequence should be deterministically derivable by the derivation inputs on the L1. [L2 derivation inputs](https://github.com/ethereum-optimism/optimism/blob/develop/specs/glossary.md#l2-derivation-inputs) consist of deposits, transactions that are forced-included, system configuration updates, and with this integration, a justification proving that L2 transactions were sequenced by Espresso.
2. The L2 block sequence should be deterministically derivable from the output of Espresso. This allows for faster transaction confirmations because the HotShot network underlying Espresso has a lower latency than the L1.

We accomplished (1) and (2) by modifying the L2 derivation pipeline to enforce that each L2 batch is determined by Espresso, using information available on the L1 (see [*Mapping the HotShot Block Stream to an OP Batch Stream*](#mapping-the-hotshot-block-stream-to-an-op-batch-stream)).

## Integration Architecture Walkthrough

### **Sequencing Flow**

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-d566b668bac44296fc992822879ceec83d36541c%2Fsequence-gitbook.drawio.svg?alt=media&#x26;token=838f10ae-6eb9-4ca3-8db9-9bacfa21c1ba" alt=""><figcaption><p>Diagram of the OP integration sequencing flow</p></figcaption></figure>

The transaction sequencing flow through the OP-Espresso integration is as follows:

1. User submits a deposit transaction to the L1 directly. This deposit will be used to fund L2 activity.
2. User submits an L2 transaction to a [proxy service](#user-content-fn-1)[^1].
3. The proxy forwards transaction data to Espresso. Other RPC requests are routed to an `op-geth` instance so that clients like MetaMask can continue to operate normally.
4. The OP node scans the L1, fetches transaction receipts, and derives deposits from them.
5. The OP node fetches blocks containing sequenced transactions from Espresso and metadata necessary for justifying the eventual transaction batch. Special care must be taken to ensure that the L2 block sequence can be deterministically derived from the HotShot and L1 transaction sequences (see [*Mapping the HotShot Block Stream to an OP Batch Stream*](#mapping-the-hotshot-block-stream-to-an-op-batch-stream)).
6. The OP node submits the batch payload to an `op-geth` instance.
7. `op-geth` executes the payload, which contains a combination of transactions sequenced by Espresso and L1 derivation inputs.
8. The OP batcher queries recently executed L2 batches.
9. The OP batcher posts batches to the batch inbox.

### Validation Flow

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-e6d16552beb4dc7b8e0f615d13468955ad197db5%2Fvalidation-gitbook.svg?alt=media&#x26;token=b0bb3ab2-c631-433e-8c1b-c46cc2e924f2" alt=""><figcaption><p>Diagram of the OP integration validation flow</p></figcaption></figure>

The transaction validation flow through the OP-Espresso integration is as follows:

1. A HotShot commitment task fetches recently sequenced block commitments from Espresso.
2. The HotShot commitment task posts these commitments to the [HotShot sequencer contract](https://docs.espressosys.com/sequencer/espresso-sequencer-architecture/internal-functionality/sequencer-contract).
3. An OP node in validator mode fetches deposits from the L1.
4. The OP node fetches batches from the batch inbox contract.
5. The OP node fetches block commitments corresponding to the HotShot blocks contained in the batches.
6. The OP node validates batches according to the [OP derivation constraints](https://github.com/ethereum-optimism/optimism/blob/65ec61dde94ffa93342728d324fecf474d228e1f/specs/derivation.md). Espresso-specific rules that map the HotShot sequence deterministically into an L2 sequence are also validated (see [*Mapping the HotShot Block Stream to an OP Batch Stream*](#mapping-the-hotshot-block-stream-to-an-op-batch-stream)). Additionally, all Espresso transactions are validated against the commitments posted to the HotShot sequencer contract. The namespace proof that the batches contain the complete set of OP transactions in a given window is currently mocked.
7. The OP node submits the batch payload to the `op-geth` instance.

## Mapping the HotShot Block Stream to an OP Batch Stream

One interesting challenge posed by this integration was the need to transform HotShot, which is responsive, into a fixed-rate L2 batch stream that satisfies [OP derivation constraints](https://github.com/ethereum-optimism/optimism/blob/develop/specs/derivation.md#overview). This challenge prompted a new feature in HotShot: certifying a recent L1 block number and a timestamp in each block. With certified timestamps, it becomes possible to deterministically derive a batch `B` from the HotShot block stream by requiring that it contains all and only the OP transactions from HotShot blocks whose timestamps fall within the sequencing window for `B`:

* [`B.timestamp`](#user-content-fn-2)[^2]`= B.parent.timestamp + rollupConfig.L2BlockTime`
* `B.transactions` includes, in order, all of the HotShot transactions in the range `i+1` to `j-1`, where
  1. `HotShot[i].header.timestamp` < `B.timestamp`
  2. `HotShot[i+1].header.timestamp` >= `B.timestamp`
  3. `HotShot[j-1].header.timestamp` < `B.timestamp + rollupConfig.L2BlockTime`
  4. `HotShot[j].header.timestamp` >= `B.timestamp + rollupConfig.L2BlockTime`

(1) and (4) prove that there were no additional blocks within the window before or after the HotShot blocks that were included (this is why indices `i` and `j` are necessary even though the batch transactions are in the block range `i+1` to `j-1`).

An OP batch also requires an `L1Origin`, the L1 block that contains derivation inputs. For this integration, we define the `L1Origin` the following way:

1. Set the `L1Origin` as the L1 block certified by the last block in a batch.
2. Adjust the `L1Origin` backwards if necessary (e.g. if the `L1Origin` is newer than the L2 batch), or forwards in the rare case that HotShot is very far behind the L1 and `L1Origin` is stale.

This definition of`L1Origin` satisfies these properties:

1. It is a block in the past, so the OP nodes don't have to block waiting for it to be produced
2. It is relatively recent, so it likely satisfies the OP constraints that would reject a stale `L1Origin`.
3. It is deterministic based on the HotShot block stream.

If after readjustment, the `L1Origin` is still invalid (it is too far behind the L2 with respect to the [sequencer drift rules](https://github.com/ethereum-optimism/optimism/blob/develop/specs/derivation.md#overview)), we allow (and require) the OP node to produce an empty batch.

## DA Flexibility

Unlike the [Espresso-Polygon zkEVM integration](https://docs.espressosys.com/sequencer/releases/doppio-testnet-release/polygon-zkevm-stack-integration), which uses HotShot for [DA](https://docs.espressosys.com/sequencer/espresso-sequencer-architecture/espresso-data-availability-layer), the OP Stack integration currently uses the L1 for DA. OP nodes in validator mode derive the L2 chain from data [submitted to the L1](https://github.com/ethereum-optimism/optimism/blob/develop/specs/batcher.md#batch-submitter).

This underscores the flexibility that rollups have in using Espresso: rollups can opt for any DA solution as long as the data stored can be eventually verified against the HotShot block stream.

## Preconfirmations

Because an OP transaction batch is determined by HotShot consensus even before it is sent to the L1, it is possible to preconfirm[^3] a transaction. Here we describe some motivating applications enabled by preconfirmations[^4].

In certain bridge designs, bonders put up collateral and execute L2 transactions off-chain to allow users of the bridge to transfer tokens cross-chain faster than can strictly be verified on-chain. For example, in [Hop](https://hop.exchange/whitepaper.pdf), the time to bridge between Optimism and Base is [25 minutes](https://docs.hop.exchange/basics/how-long-does-a-transfer-take), because that’s the amount of time a bonder needs to be certain the rollup from which the transfer originates won’t reorg. If a transaction was initiated to move funds between rollups using Espresso, the bonder could instead use the pre-confirmations provided by HotShot consensus. This would bring down the bridging time for users from 25 minutes to a couple of seconds.

Similarly, in [Across](https://across.to/bridge), [relayers](https://docs.across.to/v/developer-docs/developers/running-a-relayer) assist users in cross-chain bridging by sending them tokens on the destination chain after a pre-determined minimum number of block confirmations. With HotShot’s finality guarantees, relayers could safely send users their funds on the destination chain after a transaction is 3 HotShot blocks deep. If both rollups involved in a bridge transaction are using Espresso, then 1 block is enough, as they can’t independently reorg.

The pre-confirmations that HotShot provides serve to make cross-chain bridging safer and more capital efficient for parties such as bonders and relayers, and faster for the end user.

## Code Repository

The code for the OP Stack integration proof-of-concept can be found on GitHub: [`op-espresso-integration`](https://github.com/EspressoSystems/op-espresso-integration).

[^1]: We added this proxy service to avoid modifying [op-geth](https://github.com/ethereum-optimism/op-geth) to forward transaction data to the sequencer. This service isn’t fundamentally necessary as part of the architecture.

[^2]: This is the batch timestamp according to the [OP specification](https://github.com/ethereum-optimism/optimism/blob/develop/specs/derivation.md#overview).

[^3]: A “preconfirmed” transaction is a transaction that is considered finalized the instant it is sequenced by HotShot, rather than when it is confirmed on the L1.

[^4]: The OP stack implicitly supports preconfirmations because a node in sequencing mode constructs an L2 chain without relying on batch data posted to the L1. In our integration, sequencer nodes post an additional justification proving that they sequenced HotShot transactions correctly. Validating nodes, which derive the L2 chain from L1 batch data, will later validate this justification.


# Optimism Leader Election RFP

The OP-Espresso integration is a result of our work on Optimism's [request for proposals](https://github.com/ethereum-optimism/ecosystem-contributions/issues/63) of a leader election proof-of-concept against the OP Stack.

On 1 June 2023, Optimism solicited proposals for this RFP, with submitted proposals due June 28. [Espresso Systems' proposal](https://github.com/ethereum-optimism/ecosystem-contributions/issues/63#issuecomment-1610795492) to the RFP divided the project into several tasks:

* [T1: contract interface](https://github.com/EspressoSystems/op-leader-election/issues/2)
* [T2: basic PoC contract](https://github.com/EspressoSystems/op-leader-election/issues/3)
* [T3: batch submission updates](https://github.com/EspressoSystems/op-leader-election/issues/4)
* [T4: derivation pipeline updates](https://github.com/EspressoSystems/op-leader-election/issues/11)
* T5: basic testing

Several non-required extras were added as stretch tasks T6-T10:

* [T6: batch inbox address in system config](https://github.com/EspressoSystems/op-leader-election/issues/15)
* [T7: specification of a fee address set by sequencer](https://github.com/EspressoSystems/op-leader-election/issues/16)
* [T8: hardfork flag](https://github.com/EspressoSystems/op-leader-election/issues/17)
* [T9: alternative contract implementing interface](https://github.com/EspressoSystems/op-leader-election/issues/18)
* [T10: documentation](https://github.com/EspressoSystems/op-leader-election/issues/19)

Espresso's proposal was [selected](https://github.com/ethereum-optimism/ecosystem-contributions/issues/63#issuecomment-1640457319), and with the Cortado release, we have completed, or are about to complete, the specified tasks for the minimum viable fulfillment of the RFP. Further details and updates can be found in the [same GitHub issue](https://github.com/ethereum-optimism/ecosystem-contributions/issues/63#issuecomment-1668438963).


# Doppio Testnet Release

Espresso testnet 2 (Doppio)—July 2023

{% hint style="warning" %}
With the release of [Cortado](https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release) (testnet 3), the Doppio testnet is currently paused.
{% endhint %}

In July 2023, we [revealed the Doppio release of the Espresso Sequencer](https://medium.com/@espressosys/releasing-the-espresso-sequencer-testnet-ii-doppio-bcc46c315c30). In early August 2023, we also [deployed a public testnet of Doppio](https://medium.com/@espressosys/opening-the-doppio-testnet-to-the-public-904680bd07b1). Instructions for interacting with this testnet can be found [here](https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release/interacting-with-doppio).

Doppio includes both integration with a [minimal rollup](https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release/minimal-rollup) as well as an integration with the [Polygon zkEVM stack](https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release/polygon-zkevm-stack-integration).


# Interacting with Doppio

{% hint style="warning" %}
With the deployment of [Cortado](https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release) (testnet 3), the instructions in this document for connecting to Doppio no longer work. See [*Interacting with Cortado*](https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release/interacting-with-cortado) for instructions for interacting with Cortado.
{% endhint %}

1. If not yet set up, install [MetaMask](https://metamask.io/) and set up a new wallet.
2. In MetaMask, click on the upper left icon to select a network.
3. Click "Add network" -> "Add a network manually".

![](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-e5024f533dcc74f22e547044acecc48925d60376%2Fimage.png?alt=media)

Use the following parameters:

* Network name: `espresso-polygon-zkevm-0`
* New RPC URL: <https://zkevm-0-preconfirmations.doppio.espresso.network>
* Chain ID: `1001`

To interact with the second rollup, add a network with these parameters:

* Network name: `espresso-polygon-zkevm-1`
* New RPC URL: <https://zkevm-1.doppio.espresso.network>
* Chain ID: `1002`

For "Currency symbol", anything can be set and "Block explorer URL" should be left blank.

## Preconfirmations

The Espresso Sequencer uses the HotShot consensus protocol to provide fast confirmations of new blocks. These confirmations are secure, in that a block confirmed by HotShot is guaranteed to execute in the order determined by HotShot unless at least 1/3 of the total value staked in consensus is corrupt. They are also fast: a block may be confirmed by HotShot well before the same block is eventually processed by the layer 1 blockchain.

The RPC node for zkevm-0 that you connected to above uses these "preconfirmations" from HotShot to achieve low latency, but the RPC node for zkevm-1 does not. Try transferring some ETH on each network. Do you notice a difference in the speed with which the transaction gets confirmed?

For a more direct comparison, Doppio also includes an additional RPC node for zkevm-0 which fetches new blocks from the L1 rollup contract instead of directly from the Espresso Sequencer. You can try this "slow" RPC node to compare the latency with and without preconfirmations on the same L2.

To connect your MetaMask wallet to the slow RPC, go to Settings -> Networks and change the RPC URL for `espresso-polygon-zkevm-0` to <https://zkevm-0.doppio.espresso.network>.

## Faucet

You can request funds in the [Discord](https://discord.com/invite/YHZPk5dbcq) #faucet channel with the following command: `/faucet <address>`

To copy your MetaMask address, click on the address at the top of the MetaMask panel.

## Transaction Submission Using MetaMask

The end-user experience for submitting transactions to an instance of the Polygon zkEVM running on the Espresso Sequencer via MetaMask is identical to the user experience of submitting transactions to Polygon rollup today. Additionally, gas savings are realized by utilizing Espresso DA rather than storing transactions in Ethereum L1 calldata.


# Polygon zkEVM Stack Integration

Proof-of-concept integration with Polygon zkEVM stack

Espresso Systems has created a proof-of-concept integration with the Polygon zkEVM stack in Espresso. This integration highlights Espresso Systems’ vision of connecting and decentralizing rollups without compromising the scale and speed that rollup users have grown accustomed to.

The [integration demo](https://github.com/EspressoSystems/espresso-polygon-zkevm-demo) consists of two instances of the Polygon zkEVM using Espresso for fast confirmations and data availability in tandem. The following section is a brief walkthrough of both the technical architecture and the end-user experience for the integration.

## Integration Architecture Walkthrough

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-134bc6d3f0d23014d9425f066a9ea603e5ba3554%2FzkEVM%20diagram.png?alt=media" alt="" width="563"><figcaption><p>Diagram of the zkEVM integration</p></figcaption></figure>

The transaction flow through Polygon zkEVM-Espresso integration is as follows:

* The user submits transaction to Polygon JSON-RPC interface.
* The EVM transaction is sent to the L2 adapter and then sent to Espresso's submission API.
* The transaction is wrapped in a HotShot transaction and propagated to the [HotShot network](https://medium.com/@espressosys/espresso-hotshot-consensus-designed-for-rollups-8df9654d4213).
* HotShot generates a block that includes the transaction.
* The transaction is available to the [HotShot query service](https://github.com/EspressoSystems/hotshot-query-service/).
* The HotShot commitment service sends the batch commitment and quorum certificate to the L1 HotShot contract, which verifies that quorum certificate is valid and emits the event that a new quorum certificate has been posted.
* The Synchronizer component of the zkEVM node gets the event via Etherman and queries the HotShot query service to obtain the full data for the batch (including the submitted transaction).
* The zkEVM node computes the proof.
* The proof is posted through Etherman library to the Polygon rollup contract.
* The rollup contract verifies the proof and that the transactions are sequenced by HotShot (not yet implemented in Doppio).

## Code Repository

The code for the Polygon zkEVM integration proof-of-concept can be found on GitHub: [`espresso-polygon-zkevm-demo`](https://github.com/EspressoSystems/espresso-polygon-zkevm-demo).


# Minimal Rollup Example

The example rollup represents a simple key/value account store that receives ordered transactions from Espresso, executes them in the rollup VM, and publishes mock state proofs to an L1 (Ethereum) smart contract. The rollup contains a simple API for submitting transactions and querying account balances.\
\
More details on the example rollup can be found in the [`espresso-sequencer`](https://github.com/EspressoSystems/espresso-sequencer/blob/main/example-l2/README.md) repository on GitHub.


# Benchmarks

Performance metrics for HotShot consensus in Espresso's Doppio testnet release

As a part of launching the Doppio testnet, we are publishing benchmarks related to performance of this release of the Espresso Sequencer. The benchmarks show that a network of 1000 nodes attains very high throughput comparable to that of 10 nodes.

The benchmarks for the Doppio testnet are listed below.

<table><thead><tr><th data-type="number">Network Size</th><th data-type="number">Committee Size</th><th>Average View Time (s)</th><th>Throughput (MB/s)</th></tr></thead><tbody><tr><td>1000</td><td>10</td><td>1.10</td><td>29.41</td></tr><tr><td>500</td><td>10</td><td>1.18</td><td>28.74</td></tr><tr><td>100</td><td>10</td><td>1.10</td><td>28.52</td></tr><tr><td>10</td><td>10</td><td>0.97</td><td>25.25</td></tr></tbody></table>

## Experimental Setup

### Node Information

* Nodes are run as [ECS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) tasks in 3 availability zones in the AWS US East 2 (Ohio) region
  * AWS does not release network bandwidth statistics for Fargate. According to [this](https://www.stormforge.io/blog/aws-fargate-network-performance/) blog post trying to detect the bandwidth for Fargate, the bandwidth can vary during short-term runs, but is stable over the long term (as expected for a cloud service provider).
  * All benchmarks are run with 2 vCPUs and 16 GB memory ECS tasks.
  * ECS tasks are connected to the CDN-like nodes using an AWS VPC (virtual private cloud). They are abstracted such that we see them as being in the same network; in reality they are hosted on AWS VMs that we have little insight into.
* Each node runs the [HotShot examples](https://github.com/EspressoSystems/HotShot/tree/main/examples) inside a Docker container
  * The example application pre-generates transactions before the run starts. The transactions are randomly generated, dummy transactions about 100 bytes in size. The examples pre-generate transactions so the RNG doesn’t affect performance. Each transaction is then padded with zeros so it is the desired size.
  * We preselect 10 dedicated nodes to submit transactions throughout the benchmark.

### CDN Information

* Two CDN-like servers were run to simulate optimistic conditions: one to handle consensus messages and the other to handle data availability messages (including raw transactions)
* Each server was an [m6a.xlarge](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) EC2 instance with 4 vCPUS, 16 GB memory, and *up to* 12.5 Gigabit [bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose-instances.html#general-purpose-network-performance)
* Each server ran 1 instance of the [HotShot web server](https://github.com/EspressoSystems/HotShot/tree/main/web_server) and 1 instance of Nginx
* The consensus web server also ran the [HotShot orchestrator](https://github.com/EspressoSystems/HotShot/tree/main/orchestrator), which orchestrates the start of a run with certain parameters
* Nodes poll the CDNs and orchestrator at regular intervals using HTTP/1.1. This interval is configurable, but is always set to 100ms unless otherwise noted

### Benchmark Run Info

* Benchmarks were run for 102 views (in order to reach 100 decide events)
* At the end of each run each node outputs its statistics: total run time; how many transactions committed; how many views happened
* The reported benchmarks are averaged across 3 runs of the same benchmark

### Data Calculation

* **Total run time** = average total run time from all nodes
* **Average view time** = number of views completed / total run time
* **Total transactions submitted** = total transactions submitted to the CDN-like node
* **Total transactions committed** = total transactions committed by HotShot during the run
* **Transactions / sec** = total transactions committed / total run time
  * The transactions in our benchmarks are configured to be quite large (on the order of 1 MB). We configure transactions to be large to more closely simulate the PBS scenario and to avoid extra tuning of parameters that could affect performance (e.g. the batch size of transactions that the CDN node returns per request)
* **Throughput** = size per transaction \* total transactions committed / total run time
  * Throughput uses 1000 as the divisor for KB, MB, etc. instead of 1024


# Americano Testnet Release

Espresso testnet 1 (Americano)—November 2022

In November 2022, we revealed the first testnet of Espresso—Americano. See more details on the [announcement blog post](https://medium.com/@espressosys/releasing-espresso-testnet-1-americano-45d6c44d2a5c).


# Interacting with L1

Espresso is intended primarily for use with rollups, and an essential feature of rollups is that they periodically send verified checkpoints of their state to some other blockchain, the layer 1. In the case of Espresso we have two types of checkpoints:

* **HotShot checkpoints** record the history and state of HotShot. This includes commitments to all blocks that have been sequenced and the state that is needed to verify new blocks (such as the stake table) starting from the latest checkpoint. These checkpoints are recorded in the sequencer contract and shared by all applications using Espresso.
* **Rollup checkpoints** record the state of individual rollups, such as the state of an EVM instance. Each rollup records its own checkpoints in its rollup contract. When recording a new checkpoint, the rollup contract will validate the checkpoint against the committed sequence of blocks by reading the historical sequence of block commitments from a corresponding HotShot checkpoint.

Many rollups will not only write their state to the L1, but will also allow information from the L1 to flow back into the rollup. In this case, the interaction with the rollup contract becomes a [bridge](https://docs.espressosys.com/network/appendix/interacting-with-l1/bridging) between the L1 and the rollup, allowing tokens and other information to be exchanged bidirectionally.

Espresso is interesting in that HotShot itself *also* allows this bidirectional flow of information to and from the L1, specifically regarding the *stake table*. This allows operations on the L1 to interact with the Espresso staking token, a crucial requirement for implementing restaking, which allows Espresso to share the security budget of the L1 and pass value generated by the sequencer back to L1 validators.

Since state updates are not only written to the L1 but also read back into the HotShot and rollup states, we will hereafter eschew the "checkpoint" terminology and instead refer to **HotShot state updates** and **rollup state updates**.

The following sections dive into the use cases for these state updates and explore some of the utility and security properties that L2s are able to derive from the L1 that they use for state updates.


# Trustless Sync

One of the main reasons to use blockchains is to decentralize trust. However, the current Ethereum ecosystem often compromises on this principle by using trusted query services like [Infura](https://www.infura.io/) for clients to access the blockchain. This trades off trustlessness for convenience and scalability, since a client that trusts a query service does not need to verify any Ethereum block data.

However, Ethereum's switch to proof-of-stake and its rollup-centric roadmap offer the potential to break out of this tradeoff, enabling efficient and user-friendly clients that retain decentralized trust. When rollups post their state updates to Ethereum or a similar L1, each L1 validator independently validates the state transition for the rollup by executing the rollup's smart contract. This means that any user who trusts the collective L1 validator set can quickly sync with the latest state of the rollup simply by reading a recent, verified state update from the L1 state.

Of course, this only pushes the problem of fast, trustless sync to the L1. This is nonetheless a substantial improvement. In the case of Ethereum, the proof-of-stake consensus protocol and the fixed block time enable the creation of L1 light clients which sync far faster than real time. For instance, [Helios](https://github.com/a16z/helios) is an Ethereum light client which manages trustless sync in only 2 seconds. By verifying HotShot and rollup states on Ethereum, any such Ethereum client can be turned into a client for any rollup merely by syncing with Ethereum and then reading rollup state from the appropriate smart contract.


# Fork Recovery

When we think of rollups checkpointing to an L1, one of the first things that comes to mind is allowing the rollups to inherit the security of the L1. This subject is subtle, and discussions of it often lack a clear accounting of the security properties we hope for the rollup to obtain and how exactly they are inherited. This section will detail how rollups that checkpoint to an L1 inherit an extra level of *finality* from the L1.

First, it is important to note that Espresso, on its own, even without any form of checkpointing, already offers extremely strong finality guarantees. In order to break finality, and adversary must cause a safety violation in the HotShot finality gadget, but HotShot is a secure BFT protocol—violating its security requires an adversary to control over 1/3 of the total stake, a massive investment once HotShot reaches a critical mass of adoption.

Nevertheless, we can consider what happens in the extremely unlikely event that HotShot does suffer a safety violation, and some block which was considered final according to the HotShot protocol is removed from the history of the ledger. In this case, we can maintain finality by using the HotShot checkpoints on L1 to decide on an immutable, canonical chain.

Let's look at how such a scenario could happen. There are two ways an adversary could compromise HotShot's finality.

First, if they control more than 1/3 of the total stake at any given time, they can cause or exploit a failure in the network connecting honest nodes, partitioning honest nodes controlling 1/3 of the stake each into two disjoint sub-networks. The adversary, being Byzantine, can then use their 1/3 of the stake to vote for conflicting blocks in each partition, committing both conflicting blocks with a 2/3 quorum each, and thus creating a fork.

Second, an adversary can create a fork without even controlling 1/3 of the current stake via a *long range attack*. In a long range attack, an adversary compromises some old private keys which were used to sign a quorum certificate many blocks ago. This may be substantially cheaper than compromising current private keys, as the owners of the old private keys may already have withdrawn their stake and thus may not be very invested in maintaining the security of their keys.

While compromising old keys does not directly enable the adversary to append new invalid blocks, they can build a new fork including signed QCs starting from the block at which they compromised the keys, and unilaterally grow this fork until it is similar in length to the canonical chain.

Once an adversary has created a fork, they can compromise finality by convincing honest nodes to switch from the canonical branch of the fork to the malicious branch. Blocks which were considered finalized on the canonical branch may not have been committed at all on the malicious branch.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-40c09e84edc07631dd20dcce5f11193104099e9c%2Fimage%20(1)%20(1).png?alt=media" alt=""><figcaption><p>Fork choice between two conflicting QCs without L1 checkpoints</p></figcaption></figure>

The adversary does this by taking advantage of an ambiguity which honest nodes must somehow resolve when they are joining the network for the first time or catching up after being offline for some time. In order to catch up, such nodes will look for signed QCs attesting to HotShot state changes, so they can figure out which state to sync with. Since they cannot tell the difference between honest peers and adversaries, and adversary who can provide QCs from the malicious fork faster than honest peers can provide QCs from the canonical fork can convince honest nodes in catchup to sync to the malicious fork. Over time, the adversary may convince enough honest nodes to switch that the malicious fork becomes the "canonical" one, and blocks which were committed in the old canonical fork are permanently lost.

By leveraging the L1 checkpoints, we can prevent an adversary from tricking honest nodes onto the wrong branch of a fork, even if the adversary can present signed QCs. We simply use the checkpointed state on L1 as a deterministic *fork choice rule*: when presented with conflicting QCs during catchup, an honest node will choose the one which is compatible with the state checkpointed on L1. In this way, the L1 checkpoint plays for the Espresso blockchain the same role that [weak subjectivity checkpoints](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/weak-subjectivity/) play for Ethereum.

Choosing a fork consistent with the latest L1 checkpoint only requires a node to check the history between the latest L1 checkpoint and the QCs justifying each branch of the fork, which should be a fairly small, bounded amount of work, assuming checkpoints are posted at a fixed rate and fairly frequently. This is far more practical than storing and validating the entire history, which a node would have to do in order to detect a fork arbitrarily far in the past without using a trusted checkpoint.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-8adbea99d9b0a2d1196fcc7c383afedd8151d6d4%2Fimage.png?alt=media" alt=""><figcaption><p>Fork choice between two conflicting QCs, facilitated by L1 checkpoints</p></figcaption></figure>

In order to ensure that this fork choice rule uniquely specifies a branch, the L1 sequencer contract enforces a linear history. This is easy enough to do by storing the latest block commitment and checking that each new block specifies the previous block commitment as its parent (and has the correct height). This is difficult to do in a node because it requires the node to receive every single block in order, but in practice nodes are not always online, and when they recover from an outage they catch up immediately to the head of the chain without validating consensus for every intermediate block. The contract, on the other hand, does behave as if it is always online and directly validates the QC for every block consecutively, because **anyone** can drive the contract forward by providing a block and a QC to append, so we only require that **some** honest node is online for every block in order for the contract to remain live.

By forcing the L1 checkpoints to be linear and ensuring that honest nodes always work on a fork which is compatible with those checkpoints, we gain L1-level finality for any blocks which have been included in an L1 checkpoint. Note that this checkpointing scheme does *not* prevent an adversary from causing a fork—the L1 HotShot contract will not distinguish between "malicious" and "canonical" forks when appending a new block, so long as that block has a valid QC and follows from its parent. It will take whichever block it sees first. However, it will ensure that once a block is added to the contract, its fork *becomes* canonical, and the block will forever remain in the canonical chain.


# Bridging

Rollup state updates facilitate interoperability between the layer 1 and the rollup. If the state of the rollup is verified and stored by the layer 1, then the layer 1 can also validate claims against that state, such as a claim that some tokens have been deposited into a bridge contract on the rollup. The L1 can also *write* to the state which is maintained by the L1, and the rollup can thus receive messages and tokens from the L1.

This is the idea used by the [LX-to-LY bridge](https://docs.hermez.io/zkEVM/Overview/Overview/#the-lx-to-ly-bridge), which [Polygon zkEVM](https://wiki.polygon.technology/docs/zkEVM) uses to bridge ETH between the layer 1 and layer 2. In this design, part of the L1 state, a Merkle tree of messages to be sent to the L2, is represented directly in the L2 VM semantics. Since the canonical execution of L2 transactions happens in a smart contract on the L1, this executor is able to read from the appropriate L1 state when executing operations in the L2 VM.




---

[Next Page](/network/llms-full.txt/1)

