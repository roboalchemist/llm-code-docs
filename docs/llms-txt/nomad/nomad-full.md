# Nomad Documentation

Source: https://docs.nomad.xyz/llms-full.txt

---

# Funds Recovery

## **Attention: White Hat Hacker Friends**

### Please return ETH or ERC-20 tokens to this wallet addres&#x73;**:** [0x94a84433101a10aeda762968f6995c574d1bf154](https://etherscan.io/address/0x94a84433101a10aeda762968f6995c574d1bf154)

### Learn more about our bounty

{% embed url="<https://twitter.com/nomadxyz_/status/1555293965049630722>" %}

# Introduction

A high-level introduction to Nomad

### Introducing: Nomad

[Nomad](https://nomad.xyz) is an optimistic interoperability protocol that enables secure cross-chain communication. &#x20;

Using Nomad:

* Users can bridge tokens between chains
* Asset issuers can deploy tokens across chains
* DAOs can facilitate the execution of cross-chain governance proposals
* Developers can build native cross-chain applications (xApps)

The goal of Nomad is to provide the connective tissue to enable users and developers to interact **securely** in a multi-chain world.

### How does Nomad work?

Nomad enables applications to send data between blockchains (including rollups). Applications interact with [Nomad core contracts](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts) to enqueue messages to be sent, after which [off-chain agents](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents) verify and ferry these messages between chains.

In order to ensure that message-passing is secure, Nomad uses an [optimistic verification mechanism](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms), inspired by fraud-proof based designs like optimistic rollups. This makes Nomad more secure, cheaper, and easier to deploy compared to validator / proof-of-stake based interoperability protocols.&#x20;

Our friends at Connext have written [a fantastic article on optimistic bridging](https://blog.connext.network/optimistic-bridges-fb800dc7b0e0), and why Nomad's optimistic bridging ushers in a new paradigm for cross-chain communication.

To learn more about how Nomad works, including advanced concepts, check out [the Protocol Section](https://docs.nomad.xyz/the-nomad-protocol).

# Our Mission

Why we are building Nomad, and the future we envision

The Nomad core team's mission is simple:

> ### To enable value and information to flow securely between blockchains

In service of this mission, we are building [Nomad](https://docs.nomad.xyz/the-nomad-protocol/overview). Our goal is to ensure that all smart contract chains can interoperate using simple, gas-efficient, and trust-minimized standards.

### The Arc of the Internet

We believe that crypto / web3 ushers in a new paradigm for computing, showing the way for a new internet model that minimizes capture and enables users to transact more freely.

Yet, this paradigm shift is in its infancy, and one of the major limitations right now stems from chains being siloed. This limits composability and standardization, preventing [the next wave of applications](https://www.usv.com/writing/2018/10/the-myth-of-the-infrastructure-phase/) from being deployed and reaching a world-scale audience.

The good news is that we've seen this play out before.

![Arpanet access points in 1980 (Source)](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FouKGi35KXQSrJuo4p8Hk%2Fimage.png?alt=media\&token=629fb944-3049-4945-b81d-c9207af8b9d6)

Before the modern Internet as we know it today, we had [ARPANET](https://en.wikipedia.org/wiki/ARPANET). From the Wikipedia article:

> The **Advanced Research Projects Agency Network** (**ARPANET**) was the first wide-area [packet-switched network](https://en.wikipedia.org/wiki/Packet-switched_network) with distributed control and one of the first networks to implement the [TCP/IP](https://en.wikipedia.org/wiki/Internet_protocol_suite) protocol suite. Both technologies became the technical foundation of the [Internet](https://en.wikipedia.org/wiki/Internet).

As you can see on the map above, the various access points each corresponded to local university or research institute, which through ARPANET, became connected to each other via a common standard.

Until ARPANET, each access point or intranet was effectively siloed and required a separate interface to access. Bob Taylor, a director at APRA recollects the headaches involved:

> Taylor recalls the circumstance: "For each of these three terminals, I had three different sets of user commands. So, if I was talking online with someone at S.D.C., and I wanted to talk to someone I knew at Berkeley, or M.I.T., about this, I had to get up from the S.D.C. terminal, go over and log into the other terminal and get in touch with them. I said, "Oh Man!", it's obvious what to do: If you have these three terminals, there ought to be one terminal that goes anywhere you want to go. That idea is the ARPANET".

To current crypto users, the experience described above is eerily reminiscent. This is because we are fundamentally in a similar era regarding the maturity of web3 infrastructure.

### The Era of Ad-hoc Interoperability

To interact with an application on a new blockchain today, many users must determine which chain the app is deployed on, withdraw funds from existing on-chain positions on a different chain, bridge their funds over to the new chain, change their wallet RPC connection, and then interact with the application. This is obviously far from an ideal user experience.

In the best case scenario, the user has to context-switch multiple times, use several disparate interfaces, and pay gas fees multiple times. In the worst case scenario, users are at risk of losing all their funds, as evidenced by [multiple](https://en.wikipedia.org/wiki/Poly_Network_exploit) [nine-figure](https://www.theverge.com/2022/2/3/22916111/wormhole-hack-github-error-325-million-theft-ethereum-solana) [bridge](https://www.coindesk.com/tech/2022/03/29/axie-infinitys-ronin-network-suffers-625m-exploit/) [hacks](https://techcrunch.com/2022/06/24/harmony-blockchain-crypto-hack/), totaling to over $1.5 billion USD exploited.

As a result of this complexity, many have opined that cross-chain interoperability is fundamentally unsafe, and that "wrapped assets" generated by bridges can never be secure. This is a fatalistic argument that insists we stay in the walled-off intranet era, and ignores first principles knowledge on how to build secure bridges.&#x20;

While many of today's cross-chain experiences may in fact be unsafe, these issues stem from the ad-hoc and patchwork nature of current interoperability solutions, which prevents users and developers from having transparent understanding of risk. In order for the cross-chain future to be robust and secure, we need trust-minimized solutions.

### The Future: Seamlessly Connected Chains

Nomad takes inspiration from protocols like [IBC](https://coinbase.com/cloud/discover/dev-foundations/ibc-protocol) in Cosmos, or [XCMP](https://wiki.polkadot.network/docs/learn-crosschain) in Polkadot, in our quest to create a secure, lightweight, and easy to deploy standard for chains to communicate with each other.

As outlined in our [design philosophy](https://blog.nomad.xyz/the-nomad-design-philosophy-6fc0eacf3263), Nomad prioritizes:

* Users Over Systems
* Simple Over Complex
* Safety Over Formalism

We envision a future where **users** can interact with censorship-resistant applications without knowing what chains they are interfacing with.&#x20;

Developers will be able to design and write applications once, and deploy on many chains simultaneously, leveraging a **simple** interface that abstracts away the underlying infrastructure.

Underlying this will be a composite topology of chains, connected by a standardized cross-chain communication protocol that is **safe** for everyone to use.

If this vision resonates with you, reach out at <gm@nomad.xyz> to [help us build](https://boards.greenhouse.io/nomad) this future.

# Getting Started

To get started with Nomad, please click through the section that best matches your use case:

* Retail Users: [Token Bridging](https://docs.nomad.xyz/token-bridge)
* Asset Issuers: [Multi-chain Token Deployment](https://docs.nomad.xyz/token-bridge/asset-issuers)
* DAO Contributors: [Cross-chain Governance](https://docs.nomad.xyz/governance-bridge)
* Developers: [Cross-chain Application (xApp) Development](https://docs.nomad.xyz/developers)

If you are unsure where to begin, [learn more about the Nomad protocol](https://docs.nomad.xyz/the-nomad-protocol).

If your use case or needs aren't met here, please email the Nomad core team at <gm@nomad.xyz>.

# Overview

Nomad is an interoperability protocol for sending arbitrary messages between blockchains.

In the same way [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) was built to facilitate *reliable* packet-routing in traditional IP networking, Nomad enables applications to transmit data to each other across various blockchains.&#x20;

Analogous to how the application layer in [the Internet protocol](https://en.wikipedia.org/wiki/Internet_protocol_suite) treats the transport layer as a black-box, Nomad developers can deploy cross-chain applications (xApps) without needing to know how the cross-chain transport layer works.&#x20;

Developers only need to implement [send and receive functions](https://docs.nomad.xyz/developers) and Nomad will securely deliver messages between chains.

## Architecture&#x20;

As described above, Nomad separates the transport and application layers so that application developers do not have to reason about the guts of cross-chain communications.

To that extent, when we describe the Nomad protocol, we only mean the message-passing layer, which is application agnostic. To learn more about the application layer and building cross-chain apps, [check out the Developers section](https://docs.nomad.xyz/developers).

### On-chain and Off-chain Components

The Nomad protocol consists of two core components, on-chain smart contracts and off-chain agents:

* [On-chain smart contracts](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts) implement Nomad's messaging API on-chain, enabling developers to enqueue messages and access replicated state on different chains.
* [Off-chain agents](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents) secure and relay state across chains, forming the backbone of the messaging layer.

Developers need not interface with off-chain agents directly, as the core contracts enforce logic around optimistic verification and ensure messages are securely transmitted.

### Optimistic Verification

Nomad uses an optimistic verification mechanism, which is patterned after optimistic systems. It sees an attestation of some data, and accepts it as valid after a timer elapses. While the timer is running, honest participants (ie. [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers)) have a chance to respond to the attestation and submit fraud proofs.

Read more about [optimistic verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification) and how it compares to other [verification mechanisms](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms).

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

# Lifecycle of a Message

In this document, we'll walk through an end-to-end example of sending a cross-chain message using Nomad.

![Cross-chain message lifecycle](https://lh4.googleusercontent.com/wcEcZaPvz61_fWomSFmaK_khv8Vv9Pj_lWoWskPVsJ1k6aezPsbXDMRlAvtPRh06twfnvNlC0Xgxcd-K87sYX9eV-OfSbECTBK8sek7QLbuYK_gJXU8lr-TGK1rQuG3cB4w8t7oSflxzUjirgM_zRHQ)

Let's use an example of a user, Alice, who wants to send 1000 USDC from her account on Ethereum to the same one on Moonbeam, using the Nomad Token Bridge application.

{% hint style="info" %}
While this example will focus on the ERC-20 token bridging use case, the core logic on how messages get sent in the Nomad protocol is identical for all use cases.
{% endhint %}

### **1. User Initiates Action on Origin Chain**

The first step is Alice uses some interface (either the Token Bridge GUI or Etherscan) to construct a transaction to be sent to the BridgeRouter contract [deployed on Ethereum](https://etherscan.io/address/0x88a69b4e698a4b090df6cf5bd7b2d47325ad30a3).

[The BridgeRouter contract](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol) is an example of a xApp contract that follows [the Router pattern](https://docs.nomad.xyz/developers/application-developers/advanced/router-pattern). It exists as the entry point for users like Alice to interact with on the origin chain.

In this case, Alice's transaction will call the [`send` function](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L134) on the BridgeRouter.

### **2. xApp Dispatch Logic Executes on Origin Chain**

The BridgeRouter contract, triggered by Alice's transaction, will begin executing its business logic (as encoded by the app developer). In this case, it will:

* Perform basic validation (eg. `_amount > 0`)
* Check whether the token to be sent is local or remote (USDC is local)
* Accordingly escrow or burn the amount to be sent (USDC will be escrowed)
* Format the message to be sent, adhering to the [BridgeMessage](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeMessage.sol) contract

After the business logic is executed, the BridgeRouter contract will call `dispatch` on the Home contract, enqueuing the message to be sent.

### **3. Core Contract Logic Executes on Origin Chain**

Once [`dispatch`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L175) has been called on the Ethereum Home contract, the application router contract's job is done. This is where the Nomad protocol's work begins.

[The Home contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) formats and hashes the message, and inserts it into its Merkle tree. The Merkle tree in the Home contract is the core data structure in Nomad, and contains *all* the messages to be sent from that Home.

The new message is inserted as a leaf, and then merkelized to generate a new Merkle root, which is stored in the Home's queue. Finally, a `Dispatch` event is emitted, which signals to all relevant parties (ie. the Updater) that a new root has been generated.

### **4. Updater Signs an Update on the Origin Chain**

As new roots are generated, the Updater calls [the `update` function](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L221) on the Ethereum Home contract, committing to the current root and the new root with their digital signature. This signature acts as an attestation on the accumulator root, which can now be relayed to a destination chain.

This function emits an `update` event which signals to Relayers that a new update has occurred.

### **5. Update is Relayed to the Replica on the Destination Chain**

Once an update has been made on the Home, anyone may call `update` on any [Replica contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/replica) to effectively relay the new root to the destination chain.

{% hint style="info" %}
**Note two things:**

1. While this function has the same name `update`, it has completely different logic in a Replica contract.
2. An update on the Ethereum Home may be relayed to any number of Replicas corresponding to this Home, per [the broadcast channel model](https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging/..#broadcast-channels). In this example, we will only cover the Moonbeam Replica.
   {% endhint %}

A Relayer (which is trustless and permissionless), will call `update` passing in the `_oldRoot`, `_newRoot`, and the `_signature` which the Updater generated. This will "kick off" the dispute window for the new root, after which messages can be proven and processed.

### **6. Message is Proven and Processed on the Destination Chain**

After [the dispute window](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period) elapses, individual messages (ie. Alice's transaction to bridge 1000 USDC) can be proved against the new root.&#x20;

To prove a message, anyone can call `prove` on the Replica contract, passing in a leaf corresponding to the message, merkle path and index of the leaf to prove inclusion in the new root.

If this succeeds, the message will be processed, meaning it will be forwarded to the corresponding application router on the destination chain.

In this case, a Processor (which is also trustless and permissionless) will prove inclusion of Alice's message in the new root, and then call `process` on the Replica. The Replica will then forward the message to the BridgeRouter contract on Moonbeam, and invoke [its `handle` function](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L105).

{% hint style="warning" %}
Astute readers may notice that we assumed that Nomad's optimistic dispute window elapsed without fraud being flagged. To learn more about how fraud detection, flagging and recovery works in Nomad, please check out [the Fraud documentation](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud) in the Security section.
{% endhint %}

### 7. **xApp Handle Logic Executes on Destination Chain**

Once `handle` is called on the Moonbeam BridgeRouter, the BridgeRouter will execute application business logic on its side to complete the bridging process for Alice. In this case, it will mint 1000 Nomad USDC (or madUSDC) to Alice's address on the Moonbeam side.&#x20;

{% hint style="info" %}
Note that the BridgeRouter contract is *isomorphic*, meaning has the same code deployed on both chains. As long as `dispatch` and `handle` are implemented, they will be able to communicate with each other, with messages brokered by Nomad's messaging passing layer.
{% endhint %}

Voila! We have successfully bridged tokens and sent a message via Nomad.

# Verification Mechanisms

Nomad's primary design difference from other cross-chain messaging protocols is its usage of [**optimistic verification**](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification).

By leveraging an optimistic mechanism, Nomad reduces the trust assumptions relative to [externally verified systems](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification) (eg. multisig, PoS, and oracle based designs). While these systems require an honest majority (k-of-n) to function safely, Nomad only requires **a single honest watcher (1-of-n).**&#x20;

This section will provide:

* [A background on verification in the context of cross-chain communications](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/background-on-verification)
* A description of the different verification mechanisms:
  * [Native verification — why it is the ideal, but impractical](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/native-verification)
  * [External verification — why it has proliferated, but is insecure](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification)
  * [Optimistic verification — how it reaches a via media, and what it trades off](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification)
* [A comparison of the different mechanisms and popular constructions](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/comparing-mechanisms)&#x20;

# Background on Verification

### Verifying Cross-chain Communication

Cross-chain communication at its core is the act of synchronizing two independent blockchain networks:

* A user makes a state change on Chain A, the origin chain. This involves the submission of a transaction on-chain, which the validator set of Chain A confirms by including it in a block.&#x20;
* Once finalized, this state change must be ***verified*** by one or more off-chain actors, ie. Verifiers, who apply their signature over the state.
* Once verified, any party may relay this signed commitment to the destination chain, Chain B, by sending a transaction on-chain, which the validator set of Chain B includes in a block and confirms.
* Finally, the state from Chain A can be acted upon within Chain B, **provided that the Verifier(s) behaved honestly.**

The critical caveat is that cross-chain communication is *impossible* without a trusted third party (TTP) (formalized as an impossibility result in [this paper by Zamyatin et al](https://eprint.iacr.org/2019/1128.pdf)).&#x20;

Every cross-chain messaging system must rely on some *verifier* set to act as the TTP, and ensure that messages being sent to a destination chain reflects the correct state on the sending chain.

### Root of Trust Insecurity

This is why we consider the verification mechanism the **root of trust (RoT)** within cross-chain communication systems. If the RoT fails, the entire protocol (regardless of any other features) is vulnerable to safety failures. As such, the bulk of the work and scrutiny in any interoperability protocol must be on the verification mechanism used.

However, as we've seen from recent hacks, the majority of cross-chain messaging systems are insecure because the root-of-trust relies on a few centralized parties. For example, [the Ronin Bridge hack resulted from the compromise of 5 validator keys](https://roninblockchain.substack.com/p/community-alert-ronin-validators?s=w), in a 5-of-9 multi-signature address which served as the verifier set.

In the following sections, we'll explore the different mechanisms used for verifying cross-chain messages and the various trade-offs each makes with regards to security, extensibility, and generalizability.

# Native Verification

If every cross-chain communication method requires some TTP to provide verification, then the most trust-minimized method is **native verification**.

![Source: The Interoperability Trilemma](https://miro.medium.com/max/1400/1*m2RHMo8aAwu4rJRBvNpSKg.png)

Natively verified constructions leverage the underlying validator (or miner) sets of the two chains communicating to verify cross-chain messages. This way, there is no external verifier set introduced, and the security of the bridge reflects trust assumptions users have *already* made by using the two chains in the first place.

Put in other words, if you don't trust the validators sets of the two chains you are sending messages between, then you shouldn't be bridging between them at all!

### How It Works

Native verification is performed by running a light client of the sending chain, encoded as a smart contract, on the destination chain. As long as the sending chain's validator set is honest, the light client state can be used as the source of truth on the destination. Deployed in both directions, this creates a trust-minimized bidirectional channel.

These systems are called *light client relays*, and examples include IBC, TBTC, and Near's Rainbow Bridge (in the Ethereum --> Near direction).

![Source: How Bridges Can Be the Next Big Risk in Crypto](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F61fe08bb-d1d7-45e4-a1ac-566075d2736d_1114x496.png)

The downside of light client relays includes:

* **Difficulty of implementation and maintenance:** \
  Relays need to enshrine logic on-chain, which requires efficient design and implementation of light client logic as smart contracts. If precompiles and curves associated with the sending chain's consensus mechanism aren't available, they need to be lobbied for and added locally in order to reduce gas costs of operation. Finally, any hard fork or change in consensus needs to be reflected in light clients, requiring on-going maintenance.
* **Lack of extensibility / reusability:**\
  As described above, light clients are coupled to the consensus of their underlying chain. This means that a light client contract implemented for Avalanche cannot be repurposed for Polygon or another EVM chain, since their consensus mechanisms are different. This means that each heterogeneous communication channel requires bespoke implementation and effort, reducing the ability of the system to scale and be reused across many environments.
* **Cost of operation:**\
  In order to provide correct state, light clients need to have block or epoch headers constantly provided such that they do not become stale. For proof-of-work, this involves submitting block headers in order on-chain. For proof-of-stake, this involves submitting epoch headers with validator addresses/signatures without breaking synchrony. These gas costs for operation must be borne by someone.&#x20;

Given these factors, light client relays / natively verified systems have not gained much adoption, excepting Cosmos, which has made a concerted effort over many years, subsidized IBC, and maintained homogeneity of Layer 1 environments.

# External Verification

[Natively verified systems](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/native-verification) have not gained traction because of their aforementioned challenges, namely engineering complexity, low reusability, and high operational costs.

However, **externally verified** constructions *have* proliferated given the market need for interoperability. Unlike light client relays, externally verified systems are easy to develop, highly reusable, and quite cheap / easily subsidized.

![Source: The Interoperability Trilemma](https://miro.medium.com/max/1400/1*rKVPhxnuGmpxNeLjQqmT3g.png)

Examples of externally verified systems include custodians, multi-sig addresses, validator / proof-of-stake (PoS) systems, and oracle networks. All fundamentally work the same way — they introduce an external verifier or set of verifiers who must collectively sign cross-chain messages beyond some threshold to be deemed valid on the destination chain.

Oftentimes, externally verified systems will use more complex language like MPC or TSS. Their meaning is simple:

* **MPC (Multi-party Computation)** — there are multiple signers who are responsible for verifying cross-chain messages. Essentially a multi-sig wallet address.
* **TSS (Threshold Signature Scheme)** — the multi-sig signers must reach some quorum or threshold to verify messages. Examples include Synapse (3-of-5) or Wormhole (13-of-19).

The drawback to external verification is that while it is expedient, it outsources security to third parties (ie. folks other than the validators of the two chains). If these validators' collective security is weaker than the underlying chains they bridge, then they become the weakest link in the system.

# Optimistic Verification

Given the complexity of native verification and risks of external verification, Nomad offers a third way — **Optimistic Verification**.

![Source: Optimistic Bridges, A New Paradigm for Crosschain Communication](https://miro.medium.com/max/1400/1*j36ZAhVvVQGRBIOhPrlrAQ.png)

Optimistically verified systems like Nomad are slightly weaker in security than natively verified systems, but simpler, more cost-efficient, and easier to deploy / reuse.&#x20;

Conversely, optimistic systems are naturally more complex than a multi-sig and most other externally verified systems, but are more trust-minimized and offer greater security.

### How It Works

Optimistic verification doesn't use light clients and natively verify cross-chain messages. Instead, messages are *optimistically* signed on the origin chain, and a timeout period is enforced on the destination, during which the message can be inspected and vetoed if anything awry is noticed.

The key is that this design introduces a new set of actors, called [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) in Nomad, who are responsible for maintaining liveness and flagging fraud on-chain if detected. Nomad is only safe if there is *at least* one honest Watcher is observing the system and flagging fraud.

In other words, rather than pessimistically assuming that we need to verify each message natively, Nomad relies on local verification by participants, with the opportunity to flag it in the system. This tradeoff allows Nomad to save significantly on gas fees compared to pessimistic relays, while still maintaining a high degree of security.

To learn more about how fraud is handled in Nomad, [read more here](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud).

## The Trade-Offs

### Latency

The main trade-off with this design is mild latency — optimistic systems sacrifice speed in order to allow for a timeout period where fraudulent messages can be challenged. This is the nature of all optimistic designs, but in cross-chain interoperability, this window can be much lower than with optimistic rollups (ie. 30 minutes rather than 7 days).

All interoperability protocols are asynchronous by nature, and will experience latency from:

* Chain finality rules (eg. waiting 20 block confirmations for Ethereum's probabilistic finality)&#x20;
* Off-chain agent operations (messages may be batched to reduce cost)

Optimistic systems simply add a third reason for latency, which is the optimistic timeout period. Nomad's design acknowledges that no interoperability protocol will be instantaneous, and a mild additional latency is a small price to pay for vastly greater security.

Read more about Nomad's [optimistic-timeout-period](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period "mention").

# Comparing Mechanisms

Each of the previously discussed verification mechanisms ([native](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/native-verification), [external](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification), [optimistic](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification)) has its benefits and costs. As the famous economist, Thomas Sowell, once said:

> “There are no solutions. There are only trade-offs.”

Therefore, there is no *best* solution for all use cases, rather trade-offs that must be made by the application developer deciding to use the messaging system. In this section, we will present a simplified exploration of the trade-off space.

### Comparison of Mechanisms

<table><thead><tr><th width="150">Verification Mechanism</th><th width="150">Trust Assumption</th><th width="150">Security</th><th width="150">Extensibility / Reusability</th><th width="150">Cost</th></tr></thead><tbody><tr><td>Light Client Relay</td><td>Untrusted with synchrony assumptions</td><td><mark style="background-color:green;">Very High</mark></td><td><mark style="background-color:red;">Low</mark></td><td><mark style="background-color:red;">High</mark></td></tr><tr><td>Optimistic</td><td>Honest 1-of-n</td><td><mark style="background-color:green;">High</mark></td><td><mark style="background-color:green;">High</mark></td><td><mark style="background-color:yellow;">Medium</mark></td></tr><tr><td>Validator / PoS</td><td>Honest k-of-n with social slashing</td><td><mark style="background-color:yellow;">Medium</mark></td><td><mark style="background-color:green;">High</mark></td><td><mark style="background-color:yellow;">Medium</mark></td></tr><tr><td>Multi-signature Addresses</td><td>Honest k-of-n</td><td><mark style="background-color:red;">Low</mark></td><td><mark style="background-color:green;">Very High</mark></td><td><mark style="background-color:green;">Low</mark></td></tr></tbody></table>

# Security

{% hint style="info" %}

#### **Pre-requisite Reading**

The following material assumes an understanding of how cross-chain communication works and specifically how messages are verified.

If you are not familiar with these concepts, it is highly recommended that you read the section on [Verification Mechanisms](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms) before jumping into this section, which covers security in detail.
{% endhint %}

Security is paramount for Nomad. As described in the section on [Optimistic Verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification), Nomad's design philosophy centers around trust-minimization and a bias towards safety, which are core components of security when it comes to addressing[root of trust insecurity](https://docs.nomad.xyz/verification-mechanisms/background-on-verification#root-of-trust-insecurity).

This section will cover the three following topics:

1. [**Nomad's Root of Trust**](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust)\
   Our goal with Nomad is to create cross-chain communication that is resilient against critical attack vectors. Accordingly, this topic will cover the advanced aspects of Nomad's verification mechanism design, including fraud prevention, app-specific design, and liveness assumptions.

2. [**Attack Vectors**<br>](https://docs.nomad.xyz/the-nomad-protocol/security/attack-vectors)This section will cover the common attack vectors used to compromise interoperability protocols, including compromising keys, economic attacks, and smart contract vulnerabilities unrelated to a compromised root-of-trust.<br>

3. [**Long-term Security**](https://docs.nomad.xyz/the-nomad-protocol/security/long-term-security)\
   We believe that for crypto to take on the responsibility of onboarding the world's users and becoming the primary rails for finance, we need to think long-term. This means considering financial controls and other common security measures taken in traditional finance. This section is more exploratory in nature.

Note that this Security documentation primarily focuses on protocol security and Nomad's design. To learn more details about Nomad's operational security, check out the [Operational Security](https://docs.nomad.xyz/operational-security)section.

# Root of Trust

The root of trust is the lynchpin of an interoperability protocol's security. As the name suggests, it lies at the heart of the system — any trust assumptions are only as strong as the root of trust itself.

Nomad's [optimistic verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification) mechanism is its root of trust. The mechanism ensures that state is not corrupted, and must be bulletproof for any application building on top of Nomad.

There are two primary components when it comes to Nomad's root of trust security:

1. [**Fraud Detection**](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud) — Nomad enables Watchers to monitor the system and flag fraud if they detect anything abnormal. Nomad **requires only one honest** **Watcher** to maintain liveness to protect the system. This ensures that malicious Updaters are not able to confirm corrupt messages within Nomad.
2. [**App-Governed Root of Trust**](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/app-governed-root-of-trust) — Unlike other cross-chain messaging systems that offer monolithic security for all applications, Nomad enables application governance to decide which Watchers they permit to flag fraud and notify their application on-chain.

This section and its associated pages will break down the various components of Nomad's root of trust including:

* How fraud is prevented with the optimistic mechanism
* Why application governed root of trust returns consent to users
* Inherent liveness and economic security assumptions of optimistic verification

# Fraud

As described in the section on [optimistic verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification), Nomad's design introduces the possibility of the [Updater](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater) committing fraud.

Though this possibility exists, Nomad minimizes the chance of fraud by guaranteeing that:

1. Fraud is easily observed by anyone
2. Fraud is costly. Anyone can slash a fraudulent updater
3. Fraud will be blocked. Permissioned Watchers can block Fraud before it takes effect in order to protect applications.

Because honest Watchers have time to observe and react to fraud, Nomad ensures the safety of the system while preserving other desirable properties like low cost and extensibility.

### What Constitutes Fraud?

The Updater is the only actor in the Nomad system that can commit fraud in an attempt to cause safety failures. By fraud, we simply mean any case where an Updater signs an attestation to a merkle root that did not actually exist on the Home chain.

For example:

* The canonical merkle root is `0xabcd...1234` — it reflects a commitment to all honest messages enqueued by applications and their users.
* The Updater signs a fraudulent update attesting to merkle root `0xefgh...6789` — this root contains a malicious inserted message which sends all the funds escrowed in the[Nomad token bridge](https://docs.nomad.xyz/token-bridge) to the Updater's address.

If the latter fraudulent state root is submitted to a Replica contract, then the malicious message can be authenticated against it after the optimistic timeout, which would enable the Updater to abscond with all of the escrowed funds.

{% hint style="info" %}
For more details on Updaters, including their role and purpose in Nomad, please check out the[Updater documentation](https://docs.nomad.xyz/off-chain-agents/updater#updater-selection).
{% endhint %}

### Preventing Fraud

In order to prevent the malicious message from taking effect, Nomad enforces a dispute window during which all submitted roots remain pending. During this window, any honest [Watcher](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) can block the Replica from processing messages, which prevents the malicious message from settling.

#### Detecting Fraud

Detecting fraud is Nomad is very simple. Per the example above, fraud is easily noticed on the Home by observing for two distinct forms of fraud:

1. **Improper updates** — where the Updater commits to an entirely invalid update
2. **Double updates** — where the Updater commits to two conflicting updates

Double updates are easy to detect — if the Updater ever signs two updates where the old root is the same, but new roots conflict, this constitutes fraud.

Improper updates are also easy to detect. The Home contract maintains a [queue of roots](https://docs.nomad.xyz/smart-contracts/home#queue-of-roots) which contains every root generated — one for each message enqueued. If the Updater signs a root which isn't contained in this queue, this also constitutes fraud.

The reason fraud is easy to detect in Nomad is we only need to check that state on remote chains is equal to the canonical state on the origin chain. Fundamentally, all we're doing is checking equivalence and inclusion of hashes, both of which can be done very quickly.

#### Proving Fraud on the Home

Importantly, fraud can always be **proven** to the Home contract on the origin chain. The Home contains the canonical message tree and the queue of roots, so any fraud attempted by the Updater can be proven deterministically on-chain and punished.

Thus, the Updater must submit a bonded stake on the origin chain which can be slashed as punishment. Anyone can permissionlessly prove fraud.

#### Blocking Fraud on the Replica

Unfortunately, certain types of fraud can't be objectively proven on the receiving chain; Replicas can't know which messages were sent on the origin chain and therefore can't check message tree validity in all cases.

Therefore, we rely on permissioned Watchers to **block** fraud on the Replica. Blocking Fraud simply involves unenrolling a Replica with a fraudulent root from the application's xAppConnectionManager contract, which disconnects the applications from receiving messages from that Replica. This effectively pauses message passing until Fraud has been remediated, keeping the application (and any funds or sensitive permissions therein) safe.

To learn more about how xApps disconnect from Replicas, please read more on [App-Governed Root of Trust](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/app-governed-root-of-trust).

# Optimistic Timeout Period

Nomad's optimistic design assumes a window during which honest watchers can submit fraud proofs on-chain and prevent fraud from being settled within the system.

This section aims to cover common questions that are asked around the timeout period design.

### What happens during the timeout to prove fraud?

As described in the [parent section on Fraud](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud), Nomad requires Watchers to inform both the Home and Replica contracts about fraud.

The current Watcher response to fraud is as follows:

1. Fraud occurs on any Replica
2. Watcher observes the fraud
3. Watcher submits transaction on origin chain, slashing the Updater and shutting down the Home contract
4. Watcher submits transaction on all destination chains, shutting down message processing from Replicas

The optimistic timeout period is enforced on the Replica, expressed as [`optimisticSeconds`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Replica.sol#L38). Step #4 needs to be completed within the optimistic window.

### How long is the timeout period right now?

Currently, the window is configured to be 30 minutes for all chains. This is conservatively parameterized and anchored against the assumption that it is not economically feasible for an adversary to censor transactions on any chain Nomad is deployed on for over 30 minutes.

### How is it calculated?

When calculating the timeout period, we must ask a few questions:

* For any given chain, what is the **uncensorable period**? I.e. how long must we wait for it to be highly unlikely that an adversary could block a Watcher’s transaction proving fraud?
  * In other words, can the adversary purchase the blockspace on this chain for longer than the timeout period? If so, it is insufficient.
  * How much of the gas token, in dollars, can we reasonably expect a Watcher to lock up in their hot key to submit transactions? I.e. what is the maximum capital requirement?
  * What is the max `gasPrice` we can configure to submit the transaction blocking fraud, given the amount of capital we can lock up?
* What is the **buffer time** that a Watcher must be given to to observe fraud ahead of submitting a transaction?
  * This can be automated and shaved down over time, but we must be conservative initially.

Given that a watcher must submit a proof on both the Home and the Replica, as described in the previous section, then our calculation depends on three values for any given chain pair (X, Y):

1. Buffer (C) - a small constant to provide buffer for the Watcher to observe fraud
2. Uncensorable period for origin chain X (U\_x)
3. Uncensorable period for destination chain Y (U\_y)

Therefore, we posit that the fraud period can be calculated using:

*Replica(X, Y) = max(U\_x, U\_y) + C*

### Why doesn't it have to be 7 days like optimistic rollups?

Optimistic rollups like Optimism or Arbitrum, and Nomad share a common lineage of using optimistic mechanics with fraud games.

Both systems attempt to post state transitions from one domain to another.

* *Optimistic rollups*: state transitions on L2; source of truth on L1
* *Optimistic interoperability*: state transitions on origin domain; source of truth on destination domain. Note that this implies an L1 or L2 on either end.

In optimistic interoperability, **state transitions happen at the source of truth**. Therefore, fraud games are simple; incorrect state transitions can be easily compared to the canonical state transitions on the origin chain, which is also the source of truth and has full data availability.

In rollups, fraud games are way more complicated. Any incorrect state transitions must go through an intense proving process on the L1, which doesn’t have a record of the state transitions, but is the source of truth.

This is why the 7 day period exists for rollups -- not because of any computational time limit, but rather to allow for social consensus on what the truth is, since it cannot be verified on L1. Comparatively, Nomad's fraud period can be 30 minutes or shorter since data availability exists on the origin, allowing for a quick equivalence check off-chain, followed by instant on-chain fraud proving.

Additionally, because of the difference in complexity here, fraud games for rollups are more difficult to implement. Rollups like Optimism initially launched without fraud games being implemented. In Nomad however, fraud games have already been implemented and have been live in production since day 1.

# Fraud Recovery

The ideal scenario is that fraud never happens. In the event that it does however, Nomad has a built-in mechanism via the [optimistic timeout period](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period) to prevent it. Once fraud has been prevented, the system will need to be recovered and set back into normal operations. This section covers that process from a high level.

Post-fraud, the state on-chain is as follows:

* The [Home](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) where fraud was flagged is in the `FAILED` state. This means that the Home can no longer accept new Updates.
* Replicas are un-enrolled in the xAppConnectionManager for all xApps. Replicas CAN accept new Updates, but message processing is paused for all xApps.

### How does Nomad Recover?

When Fraud has occurred, there are three main categories of action that must be taken to recover the channel:

1. [Block Further Fraud](#block-further-fraud)
2. [Erase Past Fraud](#erase-past-fraud)
3. [Restore the Channel](#revive-the-system)&#x20;

{% hint style="info" %}
**Note:** In this document, Fraud Recovery is defined / considered within the context of one single Updater’s lifecycle.
{% endhint %}

### Block Further Fraud&#x20;

[Fraud](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud) being detected implies that Updater is either malicious, compromised, or (unfortunately) the victim of a large re-org on the origin chain. In any case, the Updater must be removed from their position of power, in order to prevent them from submitting any further fraudulent Updates in the future.

**Home**

* The Home is in a `FAILED` state, and the fraudulent Updater can no longer submit any Updates&#x20;
* Therefore, further Fraud from this Updater is automatically blocked

**Replica**

* The Updater can keep submitting Updates indefinitely while they still hold the Updater role&#x20;
* In order to block ongoing fraud attempts from a malicious Updater, they must be un-seated from their privileged role
* This must be done **before** attempting to erase past fraud; otherwise, there is no definitive cap on the amount of fraudulent state that must be erased

### Erase Past Fraud

**Home**

* By definition, fraudulent roots cannot be stored on the Home — data availability on the home guarantees that it will be [detected by the smart contract and automatically prevented](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L228)
  * Therefore, “erasing fraud” is irrelevant within the context of the Home

**Replica**

* Fraudulent roots CAN be submitted to the Replica at any time
* As long as a fraudulent root is set in the [`confirmAt`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Replica.sol#L42) mapping on the Replica, it is or will soon be possible to attempt to prove messages against it
* Once the Updater has been un-seated from their role, they can no longer continue to submit fraudulent updates
* Therefore, there is a finite number of fraudulent roots *from that Updater* which can be present on the Replica
* In order to restore the integrity of the Replica, Nomad governance must erase fraudulent Updates from all Replicas affected
* When this is done, the state on the Replica will once again appropriately reflect the state of the Home
* At this point, processing messages from the Replica is once again safe

### Restore the Channel&#x20;

Once the attempted damage done by a fraudulent Updater has been mitigated, it is safe to allow the system to continue operating. In order to do so, we must rotate the Updater role to a new key, with which the system can have a renewed sense of (optimistic) trust.

**Home**

* We must rotate the Updater role to a new, un-compromised public key
* We must transition the Home contract state from `FAILED` to `ACTIVE`
* This will allow the Home contract to begin to accept Updates from the new Updater, such that the channel can continue operating as normal

**Replica**&#x20;

* Applications must re-enroll the Replica on their xAppConnectionManager contract&#x20;
* This will allow processing of messages for the xApp to resume as usual

# App-Governed Root of Trust

In addition to providing an optimistic timeout period during which fraud can be challenged, Nomad's design has a secondary component to increase root of trust security — application specific governance having a say in its root of trust.

Functionally, this means cross-chain applications (or [xApps](https://docs.nomad.xyz/developers/application-developers/building-xapps)) built on Nomad can delegate Watcher permissions as they prefer. By enabling this choice at the *application* layer, Nomad ensures that local governance has a stake in preserving the safety of cross-chain messages processed by its respective application.

### Application-Specific Watcher Sets

As described in the previous sections on [fraud](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud), Nomad relies on [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) to flag any fraudulent attestations by the Updater. Because [Replicas](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/replica) wait for the optimistic timeout window to process messages, Watchers have the ability to inform the Replica of fraud via submitting a transaction and prevent processing of dishonest messages.&#x20;

Instead of having a system-level Watcher set, Nomad enables applications via the [Router pattern](https://docs.nomad.xyz/developers/application-developers/advanced/router-pattern) to define their own Watcher sets by deploying a xAppConnectionManager.&#x20;

#### [xAppConnectionManager](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/xappconnectionmanager)&#x20;

Every application must deploy a  contract that maintains a nested mapping called `watcherPermissions`. This data structure contains the following mappings:

`watcher address => replica remote domain id => permission boolean`

For example, a specific application may dictate that address `0xabcd` has permissions to disconnect its application from a Replica for Moonbeam, but not Evmos.

This level of granular permissions ensures that application developers have a full say on which watchers they delegate the responsibility of keeping their apps safe.&#x20;

For low overhead, applications can use the Nomad default set of watchers by using the Nomad-managed xAppConnectionManager. This xAppConnectionManager protects the Nomad Bridge and is a great option for developers wishing to bootstrap their application.

For more granular control, applications can configure their own set of Watchers by deploying a new xAppConnectionManager. Customized Watchers could be run by the application developer themselves, or any number of additional trusted parties who the app team wishes to include.

Furthermore, applications can switch from one xAppConnectionManager to another at any time. This makes it easy to begin with the default set of Watchers for ease of use, then graduate to a custom set of Watchers over time.

# Liveness Assumptions

All interoperability systems have safety and liveness assumptions, and Nomad is no exception. By safety and liveness, we mean the following:

* **Safety:** The property of a system that ensures that only the rightful owner of any funds or data can decide what to do with it.
  * I.e. Bob cannot send Alice's money through Nomad to his account.
* **Liveness:** The property of a system that ensures that the owner of any funds or data can access them at any given time.
  * I.e. Alice can *always* send her money through Nomad.

The previous sections largely focused on safety assumptions, and this one will focus on liveness.

The bulk of Nomad's liveness assumptions are around its [off-chain agents](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents). Since these agents are responsible for ensuring that messages get safely shuttled between chains, Nomad seeks to minimize any liveness issues occurring from negligent or malicious agent behavior.

### Agent Liveness Assumptions

#### Updater

Updaters are permissioned.

Nomad reduces the overhead of cross-chain communication by only relying on one external party, [the Updater](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater), to verify state. The downside of this is that if the Updater suffers downtime, its associated [Home](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) can no longer receive updates, leading to a liveness failure on the outbound channel.

This will be mitigated by adding Updater downtime slashing, where an Updater that has failed to sign for some number of blocks may have their bond slashed. Additionally, an Updater rotation model may be considered to enable standby Updaters to step in if a primary Updater is experiencing downtime. A rotation may also be performed manually through governance.

#### Watcher

Watchers are permissioned.

Nomad's core security assumption is that *at least* one honest Watcher maintain liveness and be ready to flag fraud in the event of a malicious Updater.&#x20;

Watcher liveness failures in isolation are not an issue, as there will be multiple other Watchers running at any given time. However, all Watchers experiencing liveness failures is a massive risk to the system as the Updater's signatures would be taken as word after the optimistic timeout period.

For this reason, we recommend that all Watcher operators run multiple redundant setups, where the same Watcher key may be used. This ensures that even if any key enclave is breached, that there is another setup running the Watcher hot key which can still be used to flag fraud. Unlike validator-based systems, there is also no risk of equivocation or double-signing faults.

We address [watcher griefing attacks](#undefined) in the section below.

**Relayer**

Relayers are fully permission-less and trust-less — they are functionally similar to IBC relayers.

All Relayers experiencing downtime will cause liveness failures on any channels the Relayers are supporting. As long as one party spins up a relayer and maintains liveness, this issue is mitigated.&#x20;

#### Processor

Processors are fully permission-less and trust-less.

All Processors experiencing downtime will prevent messages from being proven against Replicas' updated state, and dispatched the end xApp. Processors, similar to Relayers, are convenience agents. If Processors experience downtime, *anyone* may spin up a Processor, or manually process their messages.

### Watcher Griefing

One of the criticisms of Nomad is that malicious Watchers can "grief", or cause liveness failures to Nomad channels. While this is not entirely correct, critics are right to point out in that Nomad's current design, an adversarial Watcher *can* prevent applications from processing messages even if no fraud actually occurred.

Nomad's current Watcher design requires that Watchers [publish occurrence of fraud on the Replica](https://docs.nomad.xyz/the-nomad-protocol/security/fraud#publishing-fraud-on-the-replica). In this model, any application that delegates permissions to the Watcher publishing fraud will automatically halt processing messages from the Replica, aka become disconnected from the Replica.

If fraud did occur, then the application would be protected. In the event that fraud did *not* occur, the application would then be prevented from processing honest messages, constituting a liveness failure for its users. **However, channel-wide liveness failures are not possible.**

Under the [app-governed root of trust model](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/app-governed-root-of-trust), applications delegate Watcher disconnection permissions per their xAppConnectionManager contract. If a Watcher publishes fraud on a Replica, it may still continue to get Updates from an Updater. This ensures that an adversarial watcher can never cause total liveness failures on a channel.

If an application is disconnected from the Replica by a malicious watcher, it can leverage its own governance to remove the watcher from its permissioned set and re-establish connection.

# Attack Vectors

Given that interoperability protocols and bridges have been targeted by sophisticated black-hat hackers (including state-sponsored actors), it is imperative that we have an understanding of the most common ways these protocols have been targeted.

After going through the most recent exploits and vulnerabilities, we've grouped the attack vectors into three large buckets:

* [**Key compromise**](https://docs.nomad.xyz/the-nomad-protocol/security/attack-vectors/key-compromise) via server exploits and basic phishing attacks
* [**Economic attacks**](https://docs.nomad.xyz/the-nomad-protocol/security/attack-vectors/economic-attacks), including [Sybil attacks](https://en.wikipedia.org/wiki/Sybil_attack) on validator sets
* [**Smart contract bugs**](https://docs.nomad.xyz/the-nomad-protocol/security/attack-vectors/smart-contract-bugs) and code quality vulnerabilities

Each of these considerations warrants its own discussion, and will be covered in the following sections. We will also discuss how the Nomad system architecture and the Nomad core team operating processes helps reduce risks on each of these fronts.

# Key Compromise

One of the more common attacks in the traditional info-sec world is to compromise private keys which are responsible for safeguarding data or value. In interoperability protocols, key compromise strikes at the root-of-trust, and allows attackers to compromise the verification mechanism itself.

In the interoperability category, the best example is the [Ronin Network Bridge Exploit](https://roninblockchain.substack.com/p/back-to-building-ronin-security-breach), which led to over $600M being stolen once 5-of-9 validator keys were breached.

## How They Work

Key compromise attacks are the most brute force way of compromising trust-network based systems. In [externally verified systems](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification) like multisigs, validator systems and oracle networks, a majority of keys being breached is sufficient to execute an attack on the system. In the common security adage — defense always has to be right, whereas offense only has to be right *once*.

There are two primary vectors that attackers probe to compromise keys — infrastructure vulnerabilities and social engineering.

### Infrastructure Vulnerabilities

Private keys in interoperability systems often are ["hot" keys](https://www.fireblocks.com/blog/hot-vs-warm-vs-cold-which-crypto-wallet-is-right-for-me/), which means that they are exposed to a public network (aka the internet) in order to be able to receive requests and sign messages without human intervention. Contrast this to "cold" keys which are often stored on a hardware device like a Ledger and require manual intervention to sign messages.

Naturally, hot key setups allows for greater speed and liveness guarantees in the context of bridging. However, the trade-off is that they need to expose an interface to the internet at all times.

This is precisely what attackers target in infrastructure attacks — they probe external verifiers' setups looking for a hole by which they can access and decrypt keyfiles, and sign messages without the honest verifiers' knowledge.&#x20;

### Social Engineering

Often, [phishing](https://en.wikipedia.org/wiki/Phishing) and other social engineering techniques are used to gain access to confidential information, which is then used to attack or compromise the system. While not as technically sophisticated as infrastructure attacks, social engineering maneuvers are often much cheaper and far more effective, as humans are more malleable and dynamic than computer systems.

Methods leveraged by attackers include:

* Posing as a coworker or friend and asking for sensitive information
* Exposing links that look authentic but lead to malware or spyware being installed
* Infiltrating organizations, building rapport, and accessing confidential information through clearance

These may seem farfetched, but per the Ronin Network attack described above, these attacks do happen and the ROI is extremely high for attackers. Once attackers socially engineer their way into accessing keys, the end result is the same as infra attacks — the system gets rugged.

## Defense

### Nomad's Revocation-Centric Design

Nomad's design is inherently defensive against key compromise by splitting responsibility across two classes of actors:

1. [**Updaters**](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater) — have the permissions to verify cross-chain messages
2. [**Watchers**](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) — have the permissions to revoke, or disconnect, applications from Replicas

The key insight here (pun yet again intended :drum:) is that Watchers cannot *permit* messages to be sent cross-chain. They only have *revocation* permissions. **Therefore, even if all Watcher keys in Nomad are compromised and collude with the Updater, as long as the honest Watcher operator has a backup key, they may always prevent fraud in Nomad.**

For example, let's examine a setup where Nomad has one Updater and 8 Watchers. A common question we get is, "isn't this functionally equivalent to a 9-of-9 multisig address?"

The answer is **no**. In the multisig setup, if all 9 keys are compromised, cross-chain messages can be corrupted. In Nomad, even if all 9 keys are compromised, as long as any one Watcher operator has a redundant setup with a copy of the key, they can still sign messages to flag fraud and protect the system.

The worst case scenario in Nomad is if all keys are compromised, then malicious Watcher keys may be used to temporarily grief or censor applications from messages. Once this Watcher key is rotated out, the system resumes normal operations. We cover this in greater detail in the[#watcher-griefing](https://docs.nomad.xyz/the-nomad-protocol/root-of-trust/liveness-assumptions#watcher-griefing "mention") sub-section.

### **Operational Security**

In addition to being designed to resist key compromise, the Nomad core team also follows security best practices to reduce the chances of any infrastructure or core team members being compromised.

From an infrastructure standpoint, we:

* Have an internal SRE team following best practices in key management
* Conduct regular internal audits on our systems
* Provision strict access to sensitive key material
* Run redundant setups of critical agents
* Are progressively decentralizing the system to include more agent operators

From a social standpoint, we:

* Remain vigilant and have internal guidance around social attacks
* Only give access to sensitive information on a need-to-know basis
* Conduct fake attacks to ensure team members are responding appropriately
* [Don't act a fool](https://www.youtube.com/watch?v=DJnKm6ftPu0)

For obvious reasons, we are only sparingly sharing details right now, while we determine what is acceptable to share. We will continue to add more details in the [operational-security](https://docs.nomad.xyz/operational-security "mention") section.

# Economic Attacks

Unlike key compromise attacks, which hijack the root-of-trust verification mechanism by stealing keys, economic attacks leverage the built-in mechanics of the system to corrupt messages.

The best example of an economic attack in crypto is the [51% attack](https://en.wikipedia.org/wiki/Double-spending#51%_attack), which has happened multiple times already, particularly [in the context of Ethereum Classic](https://www.coindesk.com/markets/2020/08/29/ethereum-classic-hit-by-third-51-attack-in-a-month/). While this example is only applicable to Proof of Work chains, the fundamental concept of one logical actor acquiring enough resources to Sybil attack a system is relevant to all crypto-economic systems.

## How They Work

Economic attacks are highly variable as they are influenced by the design of the systems they target. There are many kinds of economic attacks, including:

* **51% attacks** — this can be generalized to cover attacks where the adversary purchases enough of the underlying resource (hashpower in PoW or cryptoasset in PoS) in a blockchain network to gain control of block production. Note that while this can at worst lead to double spends of&#x20;
* **Oracle attacks** — if the system uses an oracle for price feeds or other economic information, attackers can compromise the oracle or exploit its mechanism to adjust spot prices for their benefit.&#x20;
  * An example is [the Compound oracle exploit](https://decrypt.co/49657/oracle-exploit-sees-100-million-liquidated-on-compound) where the DAI spot price on Coinbase was manipulated to $1.30, which the Coinbase Oracle fed to Compound as the canonical price. This led to a cascade of liquidations on Compound, despite the market price across other exchanges showing DAI much closer to its peg of $1.
* **Governance attacks** — if the system uses a governance token for making core decisions about the protocol, then attackers may be able to purchase enough of the token required to reach quorum within a governance process. Like any plutocratic system, wealth will continue to beget wealth.&#x20;
  * An example is [the Beanstalk governance exploit](https://blockworks.co/algo-stablecoin-protocol-beanstalk-cut-down-by-governance-hijack/) where an attacker used a flash loan to game a poorly designed governance system, giving them control of all of the protocol's assets. Proper governance mechanism design must take into account not only flash loans, but other means by which attackers can acquire a significant amount of the governance asset and corrupt the system.

### Validator-based Interoperability Protocols

The economic attacks and examples covered above are meant to illustrate the wide ranging nature of potential vectors an attacker can use. However, in interoperability, one particularly important case to consider is economic attacks on validator or Proof of Stake based interoperability protocols.&#x20;

Validator-based bridges seek to increase the number of [external verifiers](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification) by introducing a token to coordinate them. In other words, validator-based protocols use token voting via Proof of Stake to *elect* a multisig for a given period of time (often called epochs).

The benefits of these systems include:

* More external parties can verify cross-chain messages (ie. \~100 in Tendermint consensus) thereby decreasing risk of collusion and increasing liveness guarantees
* The elected multi-sig is dynamic, meaning that new verifiers may join by acquiring the token
* Malicious / negligent verifiers may be punished via social slashing

However, these benefits come with significant downsides — namely, being able to join the verifier set by purchasing the staking token. An adversary just needs to purchase enough of the staking token to reach quorum within the validator set, after which they can corrupt cross-chain messages, purely by playing within the rules of the system. In other words, bribery is enshrined on-chain by using Proof of Stake.

**The key invariant here is that the value of assets needed to take over block production must&#x20;*****always*****&#x20;exceed the amount secured by the protocol.** Otherwise, an attacker can profit by purchasing the asset and corrupting the system, even if they are slashed in totality.

Though these attacks have not happened yet, as Proof of Stake based interoperability systems grow, attackers will begin to explore these vectors. All it takes is one dislocation similar to the Compound oracle exploit for an economic attack against these systems to be insanely profitable.

## Defense

The best defense against an economic attack is to avoid relying on crypto-economics for core mechanisms. In other words, if your system does not need to rely on a token, it's probably best to avoid introducing one.

![Can't buy 2/3 of the validator set, if you don't use Proof of Stake](https://memegenerator.net/img/images/16782779.jpg)

Unfortunately, not all systems can avoid economic mechanisms altogether, so it's best to keep surface area minimal and introduce economics only where absolutely needed to strengthen other aspects of the protocol.

### Nomad's Economic Design

In Nomad's case, there is no staking token that an attacker can purchase to corrupt cross-chain messages. Period.&#x20;

However, Nomad is following a progressively decentralization model that will require the introduction of economics such as:

* Bonding the Updater to enable slashing upon misbehavior
* Introducing fees or incentives for Watcher liveness (currently Watchers are run by the Nomad team, and external parties that are incentive aligned without on-chain fees)
* Having Relayers compete in a fee market to enable greater liveness fault tolerance

With each of these points, there will be considerations around economic design that Nomad will consider to ensure a robust defense against economic attacks.

#### Updater Bond

Nomad will require that Updaters post a bond before enrolled. This bond will be subject to slashign conditions such as downtime and signing fraudulent updates.

The most common questions around this parameter are:

* "How high does the Updater bond need to be?"
* "Does it have to be greater than the value secured by the protocol?"

The answers are:

* "High enough to deter an Updater from *trying* to commit fraud"
* "No!"

The key reason the value bonded can be lower than what's at stake is because Nomad ensures that fraud is preventable. This means that unlike validator-based systems where fraud will *always* go through, Nomad will *never* let fraud go through (observing a 1-of-N live Watcher assumption).&#x20;

Thus, while validator systems require bonds greater than the value secured to act as punishment, Nomad just needs the bond to be high enough to deter adversarial behavior. Put more simply — if I know that I will almost certainly lose 5 ETH for even trying to commit fraud, I won't even bother.

#### Watcher Liveness Incentives

Initially, we anticipate enrolling Watcher operators that are mission and incentive aligned, and are willing to operate these nodes without receiving on-chain incentives. However, Watchers do cost money to run, given they are off-chain nodes, and we anticipate having in protocol economics for external agent operators.

There are no concrete designs yet, but we anticipate needing to incentivize liveness to avoid free rider problems. Ie. We need all Watchers to maintain liveness even when there isn't fraud, and avoid passing the buck to other Watchers in the system. We will update this section when we have a more concrete design.

# Smart Contract Bugs

The third set of attacks we've seen on interoperability protocols are those exploiting smart contract vulnerabilities. Unlike key compromise and economic attacks however, smart contract bugs do not explicitly target the root of trust — meaning they do not attempt to take control of keys.

Rather, they find holes in the application or networking logic that were enshrined on-chain. A perfect example of this was [the Wormhole exploit](https://blog.chainalysis.com/reports/wormhole-hack-february-2022/), where the attacker exploited faulty smart contract code that allowed them to mint 120,000 WETH on Solana without escrowing the necessary collateral on the Ethereum side.

## How They Work

Smart contract vulnerabilities, like economic attacks, are myriad. Anytime logic interacting with user funds is deployed on-chain, it has the potential to introduce unintended behavior. As such, we've seen a range of smart contract vulnerabilities over time which eventually become well understood, like  [re-entrancy attacks](https://quantstamp.com/blog/what-is-a-re-entrancy-attack).

At their core, smart contract hacks involve hackers exploiting logic that does something different from what the app developer intended. The most severe outcome is the loss of all funds the contracts manage. Rather than enumerate the different categories of smart contract bugs here, we will point you to [this list of known attacks compiled by Consensys](https://consensys.github.io/smart-contract-best-practices/attacks/).

## Defense

Smart contract bugs are unfortunately incredibly common, and the only way to defend against them is to follow established and safe patterns, thoroughly test code, get multiple audits, and then pray that nobody missed anything.

Unfortunately, whenever on-chain logic begins interacting with and custodying significant value, one must expect hackers to comb through the code looking for vulnerabilities. Rather than repeating what many security experts have said here, we will point to [OpenZeppelin's documentation](https://docs.openzeppelin.com/).

In the context of interoperability, we need to ensure that both the messaging passing layer, as well as any cross-chain applications like token bridges have been thoroughly tested and audited by developers. In the case of Nomad, all of our smart contracts have been fully[audited by Quantstamp](https://docs.nomad.xyz/operational-security/audits), and we also have [ImmuneFi bug bounties](https://docs.nomad.xyz/operational-security/bug-bounty) paying out $1M for critical vulnerabilities.

# Long-Term Security

TODO

Section that covers Nomad's longer-term focus around security, as the interoperability space evolves

# Permissionless Watchers

TODO

# Financial Controls

TODO

Topics:

* What financial controls are in the traditional world
* Automatic circuit breakers
  * The absurdity of letting $100M exit in one transaction without any circuit breakers
* How Nomad Watchers can enable this, thanks to the optimistic timeout period

# Cross-Domain MEV

TODO

# Smart Contracts

Codebase: <https://github.com/nomad-xyz/monorepo/tree/main/packages/contracts-core>

{% content-ref url="smart-contracts/home" %}
[home](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home)
{% endcontent-ref %}

{% content-ref url="smart-contracts/replica" %}
[replica](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/replica)
{% endcontent-ref %}

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

# Replica

The Replica [(contract code)](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Replica.sol) is the core contract deployed on all chains that wish to *receive* inbound messages. It serves as the "inbox" for all messages sent from a specific [Home contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home). For example, the [uni-directional channel](https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging) from Ethereum to Moonbeam is generated by deploying a Home on Ethereum, and an Ethereum Replica on Moonbeam.

### Updates on the Replica

Before accepting an update, a Replica places it into a queue of pending updates. Each update must wait for some time parameter ([the optimistic dispute window](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period)) before being accepted. While a Replica cannot know that an update is certainly valid, the dispute window guarantees that fraud is publicly visible on the Home before being accepted by the Replica.

In other words, the security guarantee of the system is that all fraud may be detected by any participant and published via a proof on-chain during the window to react. Therefore updates that are not flagged by [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) are sufficiently trustworthy for the Replica to accept.

# XAppConnectionManager

Contract code: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/XAppConnectionManager.sol>

TODO

# Off-chain Agents

* [Updater](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/updater)
* [Relayer](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/relayer)
* [Processor](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/processor)
* [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers)

# Updater

Updater Code: <https://github.com/nomad-xyz/rust/tree/main/agents/updater>

**The Updater is an off-chain agent that does the following:**

* Observe [the Home contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) on the origin chain
* Sign attestations to new roots
* Publish the signed attestation to the Home

The Home contract permissions an "updater" that must attest to the state of the message tree. The updater places a bond on the home chain and is required to periodically sign attestations (updates or U). Each attestation contains the root from the previous attestation (U\_prev), and a new root (U\_new).

### Performing Updates

The Updater maps logically to a single Home contract. Its entire job is to observe the Home to ensure that new messages (and hence new roots) are notarized such that they can be relayed to any number of Replicas.&#x20;

The Updater listens for events on the Home, and calls functions to perform its job.

#### Listening for New Roots

Cross-chain applications enqueue messages to be sent by calling [`dispatch`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L175) on the Home contract. Once the message is enqueued in the Home's message tree, the Home emits the following event:

```solidity
emit Dispatch(
    _messageHash,
    count() - 1,
    _destinationAndNonce(_destinationDomain, _nonce),
    committedRoot,
    _message
);
```

Updaters listen for these events, and after batching some number of messages (per their SLA), will sign an update over the old root and new root.

#### Publishing an Update

Updaters sign attestations off-chain and publish them by calling [`update`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L221) on the Home contract:

```solidity
function update(
    bytes32 _committedRoot,
    bytes32 _newRoot,
    bytes memory _signature
) external notFailed {
    // check that the update is not fraudulent;
    // if fraud is detected, Updater is slashed & Home is set to FAILED state
    if (improperUpdate(_committedRoot, _newRoot, _signature)) return;
    // clear all of the intermediate roots contained in this update from the queue
    while (true) {
        bytes32 _next = queue.dequeue();
        if (_next == _newRoot) break;
    }
    // update the Home state with the latest signed root & emit event
    committedRoot = _newRoot;
    emit Update(localDomain, _committedRoot, _newRoot, _signature);
}
```

Once the update has been performed, a [Relayer](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/relayer) may relay the new update to [Replica contracts](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/replica) on destination chains.

### Updater Selection

Updaters are selected and enrolled on the Home contract by the [UpdaterManager contract](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/UpdaterManager.sol), which is established at initialization time.&#x20;

The UpdaterManager can be changed by calling [`_setUpdaterManager`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L161). This function can only be called by the `owner` role, which belongs to [Nomad governance](https://docs.nomad.xyz/operational-security/governance).

At a given time, there is only one Updater enrolled per Home contract. This helps reduce overhead of verification, relative to externally verified systems that require many validators or guardians.

### Updater Slashing

If an Updater ever attempts to commit fraud (by attesting to an invalid root), the Home contract will be set to a failed state, at which point the Updater will be slashed:

```solidity
function _fail() internal {
    // set contract to FAILED
    state = States.Failed;
    // slash Updater
    updaterManager.slashUpdater(msg.sender);
    emit UpdaterSlashed(updater, msg.sender);
}
```

The [`slashUpdater`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/UpdaterManager.sol#L89) function in the UpdaterManager will be implemented when updater bonding and rotation are also implemented in the future.

# Watchers

The watcher observes the Updater's interactions with the Home contract (by watching the Home contract) and reacts to malicious or faulty attestations. It also observes any number of replicas to ensure the Updater does not bypass the Home and go straight to a replica.

**It is an off-chain actor that does the following:**

* Observe the home
* Observe 1 or more replicas
* Maintain a DB of seen updates
* Submit double-update proofs
* Submit invalid update proofs
* If configured, issue an emergency halt transaction

# Relayer

{% hint style="info" %}
Relayers are **permission-less and trust-less**. This means that anyone can operate a Relayer for channels they are interested in.
{% endhint %}

The relayer forwards updates from the home to one or more replicas.

**It is an off-chain actor that does the following:**

* Observe the home
* Observe 1 or more replicas
* Polls home for new signed updates (since replica's current root) and submits them to replica
* Polls replica for confirmable updates (that have passed their optimistic time window) and confirms if available (updating replica's current root)

# Processor

{% hint style="info" %}
Processors are **permission-less and trust-less**. This means that anyone can operate a Processor for channels they are interested in.
{% endhint %}

The processor proves the validity of pending messages and sends them to end recipients.

**It is an off-chain actor that does the following:**

* Observe the home
* Maintain local merkle tree with all leaves
* Observe 1 or more replicas
* Maintain list of messages corresponding to each leaf
* Generate and submit merkle proofs for pending (unproven) messages
* Dispatch proven messages to end recipients

# Overview

The Nomad protocol's flagship use case is bridging tokens between chains. A common example of this is bridging USDC from Ethereum to Moonbeam.

To begin using the token bridge, you can use several front-ends that have integrated with Nomad:

* [The Connext Bridge GUI](https://bridge.connext.network/)
* [The Nomad Bridge GUI](https://app.nomad.xyz/)

### Token Bridge Taxonomy

TODO

# How to Bridge

### Nomad vs Connext, which should I use? <a href="#nomad-vs-connext-which-should-i-use" id="nomad-vs-connext-which-should-i-use"></a>

There are two options available to send funds through [the Nomad token bridge web app](https://app.nomad.xyz), Nomad and [Connext](https://www.connext.network/). These are two distinct protocols that are complementary to one another. We have partnered with Connext to provide an optimal experience for users!

Nomad is a secure, gas-efficient cross-chain messaging protocol. The Nomad token bridge leverages Nomad message passing channels to enable users to bridge funds between networks. This takes, on average, 35-60 minutes due to Nomad's [optimistic security window](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period). There are no Nomad imposed fees, just pay gas fees on the underlying chains!

Connext provides cross-chain liquidity pools for Nomad assets, meaning users can receive funds on the destination chain much faster (less than 10 minutes) for a small fee. Connext is not available for every asset and may not be available for larger sums. We recommend using Nomad if you intend to send large transfers.

### Bridging Through Nomad[#](https://docs.nomad.xyz/bridge/nomad-gui.html#bridging-through-nomad) <a href="#bridging-through-nomad" id="bridging-through-nomad"></a>

Bridging assets using Nomad is intuitive and easy with the Nomad GUI. In this tutorial, we will walk through the steps required to bridge your assets.

Please find our production bridge GUI at [app.nomad.xyz](https://app.nomad.xyz/).

If you would like to test our bridge using testnet funds before using real funds, please visit our development GUI at [development.app.nomad.xyz](https://development.app.nomad.xyz/).

Connect to MetaMask:

![Connect Metamask](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FnCMXI7VcvEFLMaE5G56G%2Fconnect-metamask.png?alt=media\&token=1543eb9f-f3fc-4532-85f1-fd6f7cd18adb)

Select origin and destination networks:

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FGmnEP208OcuNC3zMh2kg%2Fselect-networks.png?alt=media\&token=66ce7234-83bd-4eac-8324-666ddfe63864)

(Optional) Change Destination address. This is set as your wallet address by default. Click "edit". A modal will pop up, click "change" inside the input. Then copy your address, click to paste, and save.

{% hint style="danger" %}
Sending assets to an address you do not control can result in a permanent loss of funds!
{% endhint %}

![Edit recipient address](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FpnLjNqMfxGFTRAQA0mxX%2Fchange-dest-1.png?alt=media\&token=436a5f69-817f-4f91-a812-904f8636a338) ![Save recipient address](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FLq0PsPIHqULgehvlmLug%2Fchange-dest-2.png?alt=media\&token=6c5b3006-cfc5-4cbd-9239-c023a6b0e549)

Select the asset you want to send using the asset dropdown menu and the amount you want to send using the input prompt:

![Select asset and enter amount](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FANuHfxgtiaopiWSikgmr%2Fselect-token.png?alt=media\&token=dc3cdde5-b130-4370-bab1-47d3dba12d9a)

Click `Next`:

![Input transfer data](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F5pxvFWbkvAlndbZpsy5e%2Finput-data.png?alt=media\&token=6f5d407b-cc14-4bf3-b53c-0aae2cd1d14d)

Review your transaction details and associated fees. Check if Connext liquidity is available for your transfer for a faster bridging experience! If proceeding with Connext, continue reading [here](#fast-transfers-with-connext).

![Select protocol and review](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F9kfCw7x6g76swHo6To6z%2Freview.png?alt=media\&token=1fe86254-640e-488d-94dd-08144785ed88)

Click `Bridge Tokens` and approve the transaction in Metamask:

![Approve Bridge Transaction](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FHSHHz1UqGN6cgJRSAPvw%2Fsending.png?alt=media\&token=6012e8ed-c695-4f0e-85be-8bacfd830dd0)

After approving the transaction, you will be taken to the transaction details page. Here, you will see the estimated time remaining for your transfer to complete. Please save your transaction hash for convenience. If you lose it, you can visit your wallet address on the block explorer of the origin network and find the transaction again.

{% hint style="info" %}
You must return to the Transaction Page after bridging has concluded to pay for gas and complete your transfer. Nomad may cover the processing and gas fees for some chains.
{% endhint %}

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F7x7qn3Jdr5y0O4VWfpsa%2Ftransfer-pending.png?alt=media\&token=741dcba0-ed29-42fa-a949-1b3c6499fbc5)

You can expand the time estimate tab to track your transaction status by clicking the down arrow in the blue box:

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F1nhJHas7jkxrAU9i1kX9%2Fexpand-status.png?alt=media\&token=0aa7b52c-7df2-4e39-8e94-049870e060e8)

(Optional) If you navigated away from the GUI at any point and want to find your transfer's progress page again, visit <https://app.nomad.xyz/tx> and enter the origin network and your transfer's transaction hash.

![Search bridge transfer](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FkAEpP6suEFxczQiefzN9%2FScreen%20Shot%202022-06-30%20at%2010.25.18%20AM.png?alt=media\&token=395f519e-a9da-4c2e-8eb1-9d2c34d197e9)

Once your transfer has completed, you should see the below display and your funds will be in the account of your destination address. If your transfer is taking longer than expected, please reach out to us on [Discord](https://discord.gg/RurtmJApqm) in the #support channel:

![Finished](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FkILcCDa4Y9BXJME5DhbL%2Ftransfer-complete.png?alt=media\&token=f24915aa-08e5-4de9-98c9-6e808113667e)

### Completing a Transfer (Ethereum Destination Only)

If you are sending to Ethereum, there is one additional processing step due to the high cost of processing transactions on Ethereum. You will see the following display and should click "Complete Transfer" and complete the MetaMask transaction. After this, your funds should be at your destination on Ethereum!

![Claim on Ethereum](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FfimCFHA1tlInMXmMV6z3%2Fcomplete-transfer.png?alt=media\&token=ff4d87bc-0d13-428d-982f-ee246a960a9b)

## Fast Transfers with Connext

Fill out data for your transfer and click "Next." Select "Connext." If there is liquidity available for your transfer, it will calculate associated fees for your transaction. Note that Connext collects gas fees in the asset that is being sent.

If there is not liquidity available, you can [continue by using Nomad](#bridging-through-nomad).

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FLSqU2uCxbMFdQYILQkYo%2Fcheck-connext.png?alt=media\&token=04a226ca-1959-4015-bf52-be75667183b1)

Click `Send` and approve the transaction in MetaMask!

In a few minutes, you will see your transfer appear in a table below. Click "Claim" to submit a transaction to receive your funds on the destination chain.

Click "View" to go to your transaction in the ConnextScan block explorer. Or you can visit `https://connextscan.io/tx/<yourtransactionhash>`.

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FSPM2G9Y2nlBV2D8YtVGm%2Fconnext-claim.png?alt=media\&token=aafdf26d-fc9a-4d0b-b78a-f6a4f94b8f6b)

# Using Etherscan

TODO

# Asset Issuers

One common use case of the Nomad token bridge is to instantly take single-chain assets multi-chain.

Examples:

* [Covalent took $CQT, their network staking token, from Ethereum to Moonbeam.](https://www.covalenthq.com/blog/cqt-staking-live/)
* [Elasticswap took $TIC, their rebasing token, from Avalanche to Ethereum.](https://twitter.com/ElasticSwap/status/1523811687354159106)
* [Hummingbot took $HBOT, their governance token, from Ethereum to Avalanche](https://twitter.com/hummingbot_io/status/1535316005777448974), and more chains soon™.

{% embed url="<https://hummingbot.io/en/blog/2022-06-hbot-tokens-now-on-avalanche-nomad/>" %}
Learn more about why Hummingbot chose Nomad to take HBOT cross-chain
{% endembed %}

If you are an asset issuer interested in taking an existing token multi-chain or deploying your token for the first time on multiple chains, please [fill out this form](https://forms.clickup.com/14205595/f/dhgmv-13960/GQOZTT48N80YE9ELN3). Once you have filled it out, we will get back to you within a week.

# Custom Representations

Description of how partners can enroll custom token implementations (vetted by governance) and migrate from bridge tokens to custom tokens

# Deployed Tokens

Tokens are a product of the bridge&#x20;

In many ways tokens are the product that touch the most end users - in AMMs, lending protocols, etc

TODO: Write a JS script that dynamically populates this table with deployed token addresses.

# Mainnet

## Networks

* [Ethereum](#undefined)
* [Moonbeam](#moonbeam)
* [Evmos](#evmos)
* [Milkomeda C1](#milkomeda-c1)
* [Avalanche](#avalanche)
* [Gnosis Chain](#gnosis-chain)

## Ethereum

<table><thead><tr><th width="150">Name</th><th width="150">Symbol</th><th width="150">Origin</th><th width="531">Address</th><th width="150" data-type="number">Decimals</th></tr></thead><tbody><tr><td>Wrapped GLMR</td><td>WGLMR</td><td>Moonbeam</td><td>0xba8d75BAcCC4d5c4bD814FDe69267213052EA663</td><td>18</td></tr></tbody></table>

## Moonbeam

<table><thead><tr><th width="150">Name</th><th width="150">Symbol</th><th width="150">Origin</th><th width="462">Address</th><th width="150" data-type="number">Decimals</th></tr></thead><tbody><tr><td>Wrapped Ether</td><td>WETH</td><td>Ethereum</td><td>0x30D2a9F5FDf90ACe8c17952cbb4eE48a55D916A7</td><td>18</td></tr><tr><td>USD Coin</td><td>USDC</td><td>Ethereum</td><td>0x8f552a71EFE5eeFc207Bf75485b356A0b3f01eC9</td><td>6</td></tr><tr><td>Tether USD</td><td>USDT</td><td>Ethereum</td><td>0x8e70cD5B4Ff3f62659049e74b6649c6603A0E594</td><td>6</td></tr><tr><td>Wrapped Bitcoin</td><td>WBTC</td><td>Ethereum</td><td>0x1DC78Acda13a8BC4408B207c9E48CDBc096D95e0</td><td>8</td></tr><tr><td>Dai</td><td>DAI</td><td>Ethereum</td><td>0xc234A67a4F840E61adE794be47de455361b52413</td><td>18</td></tr><tr><td>Frax</td><td>FRAX</td><td>Ethereum</td><td>0x8d6e233106733c7cc1ba962f8de9e4dcd3b0308e</td><td>18</td></tr><tr><td>Frax Share</td><td>FXS</td><td>Ethereum</td><td>0x21a8daca6a56434bdb6f39e7616c0f9891829aec</td><td>18</td></tr><tr><td>Covalent</td><td>CQT</td><td>Ethereum</td><td>0x5130ca61bf02618548dfc3fdef50b50b36b11f2b</td><td>18</td></tr></tbody></table>

## Evmos

<table><thead><tr><th width="150">Name</th><th width="150">Symbol</th><th width="150">Origin</th><th width="446">Address</th><th width="150" data-type="number">Decimals</th></tr></thead><tbody><tr><td>Wrapped Ether</td><td>WETH</td><td>Ethereum</td><td>0x5842C5532b61aCF3227679a8b1BD0242a41752f2</td><td>18</td></tr><tr><td>USD Coin</td><td>USDC</td><td>Ethereum</td><td>0x51e44FfaD5C2B122C8b635671FCC8139dc636E82</td><td>6</td></tr><tr><td>Tether USD</td><td>USDT</td><td>Ethereum</td><td>0x7FF4a56B32ee13D7D4D405887E0eA37d61Ed919e</td><td>6</td></tr><tr><td>Wrapped Bitcoin</td><td>WBTC</td><td>Ethereum</td><td>0xF80699Dc594e00aE7bA200c7533a07C1604A106D</td><td>8</td></tr><tr><td>Dai</td><td>DAI</td><td>Ethereum</td><td>0x63743ACF2c7cfee65A5E356A4C4A005b586fC7AA</td><td>18</td></tr><tr><td>Frax</td><td>FRAX</td><td>Ethereum</td><td>0x28eC4B29657959F4A5052B41079fe32919Ec3Bd3</td><td>18</td></tr><tr><td>Frax Share</td><td>FXS</td><td>Ethereum</td><td>0xd0ec216A38F199B0229AE668a96c3Cd9F9f118A6</td><td>18</td></tr></tbody></table>

## Milkomeda C1

<table><thead><tr><th width="150">Name</th><th width="150">Symbol</th><th width="150">Origin</th><th width="531">Address</th><th width="150" data-type="number">Decimals</th></tr></thead><tbody><tr><td>Wrapped Ether</td><td>WETH</td><td>Ethereum</td><td>0x5950F9B6EF36f3127Ea66799e64D0ea1f5fdb9D1</td><td>18</td></tr><tr><td>USD Coin</td><td>USDC</td><td>Ethereum</td><td>0x5a955FDdF055F2dE3281d99718f5f1531744B102</td><td>6</td></tr><tr><td>Tether USD</td><td>USDT</td><td>Ethereum</td><td>0xab58DA63DFDd6B97EAaB3C94165Ef6f43d951fb2</td><td>6</td></tr><tr><td>Wrapped Bitcoin</td><td>WBTC</td><td>Ethereum</td><td>0x48AEB7584BA26D3791f06fBA360dB435B3d7A174</td><td>8</td></tr><tr><td>Dai</td><td>DAI</td><td>Ethereum</td><td>0x41eAFC40CD5Cb904157A10158F73fF2824dC1339</td><td>18</td></tr><tr><td>Frax</td><td>FRAX</td><td>Ethereum</td><td>0x362233f1ef554ca08555ca191b4887c2c3132834</td><td>18</td></tr><tr><td>Frax Share</td><td>FXS</td><td>Ethereum</td><td>0xe5e25df85f6a17fc5681dee7b6b080933476630d</td><td>18</td></tr><tr><td>Wrapped Star</td><td>WSTR</td><td>Ethereum</td><td>0x0c2d8604c89d126133bed39967e69272960bc430</td><td>18</td></tr></tbody></table>

## Avalanche

<table><thead><tr><th width="158">Name</th><th width="150">Symbol</th><th width="150">Origin</th><th width="531">Address</th><th width="150" data-type="number">Decimals</th></tr></thead><tbody><tr><td>Hummingbot</td><td>HBOT</td><td>Ethereum</td><td><a href="https://snowtrace.io/token/0x38dcf0532699b880e6a125f7d918380524cd60a6">0x38Dcf0532699b880E6a125F7d918380524CD60a6</a></td><td>18</td></tr></tbody></table>

## Gnosis Chain

TODO

# Testnet

## Networks

* [Rinkeby](#rinkeby)
* [Kovan](#kovan)
* [Goerli](#goerli)
* [Moonbase Alpha](#moonbase-alpha) (Moonbeam Testnet)
* [Evmos Testnet](#evmos-testnet)
* [Milkomeda C1 Testnet](#milkomeda-c1-testnet)

## Rinkeby

**Domain ID:** `2000`

<table><thead><tr><th width="150">Name</th><th width="150">Symbol</th><th width="150">Decimals</th><th>Address</th><th>Origin Domain</th></tr></thead><tbody><tr><td>Wrapped Ether</td><td>WETH</td><td><code>18</code></td><td>0xf1A137F67aa6aE2FEba192de252f7D4FC244766A</td><td>3000</td></tr><tr><td>Test Token</td><td>TEST</td><td><code>18</code></td><td>0xf4CF3FcC8dC7E5171Bb08bef75EDe3fEf00F46E6</td><td>3000</td></tr><tr><td>USD Coin</td><td>USDC</td><td><code>6</code></td><td>0x238Afa01c004CD2a82908D3B80CF421040601244</td><td>3000</td></tr><tr><td>Wrapped wADA</td><td>WWADA</td><td><code>18</code></td><td>0xeBe76a234bC185606601C807352876Ae757b54D5</td><td>8000</td></tr><tr><td>Wrapped MOVR</td><td>WMOVR</td><td><code>18</code></td><td>0x6FAe8aee3A8681B604837a72b203A72C93987562</td><td>5000</td></tr><tr><td>Wrapped wADA</td><td>WWADA</td><td><code>18</code></td><td>0xc7D9c115e40Bd0a362270A9240975C0009E97c31</td><td>8000</td></tr><tr><td>Random ERC20</td><td>rERC20</td><td><code>18</code></td><td>0x2D997F0917Ce644B6d31303300913E17178F3F3F</td><td>3000</td></tr><tr><td>Wrapped ADA</td><td>WADA</td><td><code>18</code></td><td>0xA9aE90E9D541F726ae8Fb39C5172F2c9D09E2E54</td><td>8000</td></tr><tr><td>Wrapped Ether</td><td>WETH</td><td><code>18</code></td><td>0x12a89f0Cdf44082aEEF0194924A5280Cc178073A</td><td>9000<br></td></tr></tbody></table>

## Kovan

**Domain ID:** `3000`

| Name          | Symbol | Decimals | Address                                    | Origin Domain |
| ------------- | ------ | -------- | ------------------------------------------ | ------------- |
| Wrapped Ether | WETH   | `18`     | 0x6A8a5FB1bd977849b4fEcFb1e104ABfeB23b440b | 2000          |
| USD Coin      | USDC   | `6`      | 0x10e8BD2aEa9d43439aC072bF4C68Fb41fa6eB73A | 2000          |

## Goerli

TODO

## Moonbase Alpha

**Domain ID:** `5000`

<table><thead><tr><th width="150">Name</th><th width="150">Symbol</th><th width="150">Decimals</th><th>Address</th><th>Origin Domain</th></tr></thead><tbody><tr><td>Wrapped Ether</td><td>WETH</td><td><code>18</code></td><td>0x6A8a5FB1bd977849b4fEcFb1e104ABfeB23b440b</td><td>2000</td></tr><tr><td>USD Coin</td><td>USDC</td><td><code>6</code></td><td>0x10e8BD2aEa9d43439aC072bF4C68Fb41fa6eB73A</td><td>2000</td></tr></tbody></table>

## Evmos Testnet

TODO

## Milkomeda C1 Testnet

**Domain ID:** `8000`

<table><thead><tr><th width="150">Name</th><th width="150">Symbol</th><th width="150">Decimals</th><th>Address</th><th>Origin Domain</th></tr></thead><tbody><tr><td>Wrapped Ether</td><td>WETH</td><td><code>18</code></td><td>0x6A8a5FB1bd977849b4fEcFb1e104ABfeB23b440b</td><td>2000</td></tr><tr><td>USD Coin</td><td>USDC</td><td><code>6</code></td><td>0x10e8BD2aEa9d43439aC072bF4C68Fb41fa6eB73A</td><td>2000</td></tr></tbody></table>

# Smart Contracts

Codebase: <https://github.com/nomad-xyz/monorepo/tree/main/packages/contracts-bridge>

{% content-ref url="smart-contracts/bridgerouter" %}
[bridgerouter](https://docs.nomad.xyz/token-bridge/smart-contracts/bridgerouter)
{% endcontent-ref %}

{% content-ref url="smart-contracts/tokenregistry" %}
[tokenregistry](https://docs.nomad.xyz/token-bridge/smart-contracts/tokenregistry)
{% endcontent-ref %}

{% content-ref url="smart-contracts/bridgetoken" %}
[bridgetoken](https://docs.nomad.xyz/token-bridge/smart-contracts/bridgetoken)
{% endcontent-ref %}

{% content-ref url="smart-contracts/bridgemessage" %}
[bridgemessage](https://docs.nomad.xyz/token-bridge/smart-contracts/bridgemessage)
{% endcontent-ref %}

# BridgeRouter

Contract code: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol>

The BridgeRouter contract is the entry point for the token bridge application and implements its interface, per [the Router pattern](https://docs.nomad.xyz/developers/application-developers/advanced/router-pattern). It enables users to “send” tokens from Chain A to Chain B via a lock-and-mint mechanism.

### Sending and Receiving Tokens

#### Sending&#x20;

The sending side logic is implemented in the [`send`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L134) function:

```solidity
// ======== External: Send Token =========

/**
 * @notice Send tokens to a recipient on a remote chain
 * @param _token The token address
 * @param _amount The token amount
 * @param _destination The destination domain
 * @param _recipient The recipient address
 */
function send(
    address _token,
    uint256 _amount,
    uint32 _destination,
    bytes32 _recipient,
    bool /*_enableFast - deprecated field, left argument for backwards compatibility */
) external;
```

#### Receiving

The receiving side logic is implemented in the [`handle`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L96) function:

```
// ======== External: Handle =========

/**
 * @notice Handles an incoming message
 * @param _origin The origin domain
 * @param _nonce The unique identifier for the message from origin to destination
 * @param _sender The sender address
 * @param _message The message
 */
function handle(
    uint32 _origin,
    uint32 _nonce,
    bytes32 _sender,
    bytes memory _message
) external override onlyReplica onlyRemoteRouter(_origin, _sender);
```

#### Lock-and-Mint Mechanism

The BridgeRouter enforces the following strict invariant:

> The amount locked on the chain where the token originates must always be equal to the circulation of representational tokens minted on all destination chains.

You can see this in the codebase here:

* Sending side: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L149>
* Receiving side: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L278>

### Enrolling Custom Representations

The BridgeRouter enables custom tokens to be enrolled by calling [`enrollCustom`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L200):

```solidity
    // ======== External: Custom Tokens =========

    /**
     * @notice Enroll a custom token. This allows projects to work with
     * governance to specify a custom representation.
     * @param _domain the domain of the canonical Token to enroll
     * @param _id the bytes32 ID of the canonical of the Token to enroll
     * @param _custom the address of the custom implementation to use.
     */
    function enrollCustom(
        uint32 _domain,
        bytes32 _id,
        address _custom
    ) external onlyOwner {
        // Sanity check. Ensures that human error doesn't cause an
        // unpermissioned contract to be enrolled.
        IBridgeToken(_custom).mint(address(this), 1);
        IBridgeToken(_custom).burn(address(this), 1);
        tokenRegistry.enrollCustom(_domain, _id, _custom);
    }
```

# TokenRegistry

Contract code: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/TokenRegistry.sol>

# BridgeToken

Contract code: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeToken.sol>

# BridgeMessage

Contract code: <https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeMessage.sol>

# Architecture

### Summary <a href="#summary" id="summary"></a>

The Token Bridge xApp implements a bridge that is capable of sending tokens across blockchains.

Features:

* Ensures that circulating token supply remains constant across all chains.

### Limitations <a href="#limitations" id="limitations"></a>

The Token Bridge xApp only supports standard, non-rebasing ERC20-compliant tokens.

### Protocol <a href="#protocol" id="protocol"></a>

#### Handling Messages <a href="#handling-messages" id="handling-messages"></a>

* the BridgeRouter contract only accepts messages from other remote BridgeRouter contracts, which are registered by each BridgeRouter
  * therefore, every message received follows the same "rules" that the local BridgeRouter expects
  * for example, any tokens sent in a message are ensured to be valid, because the remote BridgeRouter sending the message should locally enforce that a user has custody before sending the message to the remote chain
* the messages from remote BridgeRouter contracts must be sent via Nomad, dispatched by a local Replica contract, which are registered with the xAppConnectionManager contract
  * thus, the BridgeRouter depends on the xAppConnectionManager contract for a valid registry of local Replicas
* if another chain has sent a token that's "native" to this chain, we send that token from the Router contract's escrow to the recipient on this chain
* if we're receiving a token that's not "native" to this chain,
  * we check whether a representation token contract has already been deployed by the Router contract on this chain; if not, we deploy that representation token contract and add its address to the token registry
  * we mint representation tokens on this chain and send them to the recipient

#### Dispatching Messages <a href="#dispatching-messages" id="dispatching-messages"></a>

* **TODO**: describe rules — person must approve token to Router on local chain (if it's a native token) proving they have ownership over that token and can send to the native chain
* sending tokens
  * the user uses ERC-20 `approve` to grant allowance for the tokens being sent to the local BridgeRouter contract
  * the user calls send on the local BridgeRouter to transfer the tokens to a remote
* if the token being sent is "native" to the BridgeRouter's chain, the BridgeRouter contract holds the token in escrow
* if the token being sent is not "native" to the chain, then the local token is a representation token contract deployed by the BridgeRouter in the first place; the BridgeRouter contract burns the tokens before sending them to another chain

#### Message Format <a href="#message-format" id="message-format"></a>

* **TODO**: specify how messages are encoded for this application

### Smart Contracts <a href="#architecture" id="architecture"></a>

TODO: Update links + combine with Smart Contracts section

**BridgeRouter (**[**code**](https://github.com/nomad-xyz/nomad-monorepo/blob/main/solidity/nomad-xapps/contracts/bridge/BridgeRouter.sol)**)**

* Receives incoming messages from local `Replica` contracts sending tokens from another chain
* Dispatches outgoing messages to local `Home` contract in order to send tokens to other chains
* Manages a registry of representation ERC-20 token contracts that it deploys on its local chain
* Maintains a registry of remote `BridgeRouter` contracts to
  * authenticate that incoming messages come from a remote `BridgeRouter` contract
  * properly address outgoing messages to remote `BridgeRouter` contracts

**TokenRegistry (**[**code**](https://github.com/nomad-xyz/nomad-monorepo/blob/main/solidity/nomad-xapps/contracts/bridge/TokenRegistry.sol)**)**

* Responsible for deploying and keeping track of representation ERC-20 token contracts on this chain
* When a new token is transferred, deploys a new representation token contract on this chain, and stores a two-way mapping between the information of the original token contract & the address of the representation on this chain
* Inherited by the `BridgeRouter`, who uses this to make sure a representation of the token exists on this chain before minting/burning

**BridgeMessage library (**[**code**](https://github.com/nomad-xyz/nomad-monorepo/blob/main/solidity/nomad-xapps/contracts/bridge/BridgeMessage.sol)**)**

* Library for handling all the nitty gritty of encoding / decoding messages in a standardized way so they can be sent via Nomad

### Message Flow <a href="#message-flow" id="message-flow"></a>

The logical steps and flow of information involved in sending tokens from one chain to another.

* **Chain A**
  * User wants to send their tokens to Chain B
    * If it's a native token, the user must first `approve` tokens to the local `BridgeRouter-A`
  * User calls `send` on the local `BridgeRouter-A`
    * If it's a native token, tokens are pulled from the User's wallet to `BridgeRouter-A` and held in escrow
    * If it's a non-native token, tokens are burned from User's wallet by `BridgeRouter-A`
      * *Note:* `BridgeRouter-A` can burn non-native tokens because the representative contract for the token on its non-native chain was originally deployed by `BridgeRouter-A` when it received a message sending the token from another chain. The router has administrative rights on representations
  * `BridgeRouter-A` constructs a message to `BridgeRouter-B`
    * `BridgeRouter-A` keeps a mapping of `BridgeRouter` contracts on other chains so it knows where to send the message on Chain B
  * `BridgeRouter-A` calls `enqueue` on `Home-A` contract to send the message to Chain B
* **Off-Chain**
  * Standard Nomad behavior. Updater → Relayer → Processor
  * Relayers see message on `Home-A`
  * Relayers pass message to `Replica-A` on Chain B
* **Chain B**
  * After waiting for the acceptance timeout, `Replica-A` processes the message and dispatches it to `BridgeRouter-B`
  * `BridgeRouter-B` keeps a mapping `Replica` contracts that it trusts on the local chain. It uses this to authenticate that the incoming message came from chain A
  * `BridgeRouter-B` keeps a mapping of `BridgeRouter` contracts on other chains, so it can authenticate that this message came from `BridgeRouter-A`
  * `BridgeRouter-B` looks for the corresponding ERC-20 token contract in its registry, and deploys a new representative one if it doesn't already exist
  * `BridgeRouter-B` sends the token to the recipient
    * If it's a native token, `BridgeRouter-B` sends the tokens from the pool it's holding in escrow
    * If it's a non-native token, `BridgeRouter-B` mints the token to the recipient (
      * *Note:* `BridgeRouter-B` can mint non-native tokens because the representative contract for the token on its non-native chain is deployed by `BridgeRouter-B` when it received a message sending the token from another chain. The router has administrative rights on representations.

### Tracing a Message <a href="#tracing-a-message" id="tracing-a-message"></a>

Nomad is currently still under active development. Because Nomad batches messages and sends only tree roots, there is no way to track individual messages on-chain once a message is passed to the Home contract. A agent-querying tool could be built to query off-chain agents for individual transactions, but such a tool does not currently exist.

What this means for the token bridge is that there is going to be a state of unknown during the time of send and receipt. You can think of this as snail mail without any tracking but with delivery confirmation. The only things that can be confirmed on-chain are:

1. A transaction was sent on chain A to the BridgeRouter contract
2. The recipient addressed received a token mint on chain B

#### Pseudo-tracking <a href="#pseudo-tracking" id="pseudo-tracking"></a>

1. Start by locating the `bridgeRouter` contract you are looking for, addresses in the config dir:

* [Dev Contracts](https://github.com/nomad-xyz/nomad-monorepo/tree/main/rust/config/development)
* [Staging Contracts](https://github.com/nomad-xyz/nomad-monorepo/tree/main/rust/config/staging)
* [Prod Contracts](https://github.com/nomad-xyz/nomad-monorepo/tree/main/rust/config/mainnet)

1. Verify that a transaction was sent to the BridgeRouter contract on the Home chain
   * *Wait time*: dependent on block confirmation times for each chain
2. Verify a transaction was sent on the Home contract
   * *Wait time*: dependent on block confirmation for each chain, but should be shortly after transaction is sent to BridgeRouter contract
   * There is not a way to query for a particular transactions at this time. Cross-check timestamps with BridgeRouter transaction.
3. After acceptance period, verify a transaction was sent on the destination Replica
   * *Wait time*: acceptance period. Currently 30 minutes
   * Cross-check timestamps
4. Verify a transaction was sent on the destination BridgeRouter
   * *Wait time*: acceptance period + block confirmation time
5. Verify that the recipient address received a token mint
   1. *Wait time*: block confirmation time for chain A + acceptance period + block confirmation time for chain B

### The Token Registry <a href="#the-token-registry" id="the-token-registry"></a>

The Token Bridge xApp relies on a [`TokenRegistry`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/TokenRegistry.sol) smart contract. This contract handles mapping canonical Nomad token identifiers to their local representation (or native local deployment) and vice versa.

For most tokens there is a 1:1 relationship between the canonical identifier and the local version. Regrettably, tokens are not always that simple. The token registry allows us to support more complex use cases by adjusting the relationship between identifiers and local tokens.

#### Custom Tokens <a href="#custom-tokens" id="custom-tokens"></a>

To support teams desiring specific token functionality, the registry supports enrolling "custom" tokens. Governance may instruct the token registry to change the official local representation of a token to a new address. Any ERC20-compliant contract that allows the Bridge Router to mint & burn tokens may be enrolled as a custom token.

When a custom token is enrolled, that token no longer has a 1:1 correspondence between local representation and canonical identifier. Instead, there are >1 local representations. Incoming transfers mint the **latest** representation (the most recently enrolled custom token), while outgoing transfer may burn **any** previous representation. This ensures that users' tokens are never invalidated, but new users get the best version.

For convenience, we also expose a `migrate` function that allows users to immediately exchange any previous representation for the **latest** representation. This allows a user to upgrade outdated representations and receive the latest without dispatching a cross-chain message.

#### Dust <a href="#dust" id="dust"></a>

We provide the users with `dust` in order to facilitate their onboarding to the chain (all chains apart from Ethereum).

We provide no guarantees to the end users that they will necessarily receive gas from the Dust feature. We provide it in **good faith** that it won't be abused and will be used by users who need it.

Dust is donated by people who are incentivized for users to have gas after they bridge. Large $$$ values of dust should not be donated at any given time and we are actively talking with teams to avoid doing so.

It is hoped that the gas is used for genuine users, but not a concern if the gas is used improperly, as it should be of negligible importance to the donor.

# FAQ

### Bridge Features <a href="#nomad-bridge-features" id="nomad-bridge-features"></a>

#### What assets are available to bridge? <a href="#what-assets-are-available-to-bridge-updated-01-13-2022" id="what-assets-are-available-to-bridge-updated-01-13-2022"></a>

You can bridge any ERC-20 permissionlessly using the Nomad token bridge. The Nomad core team doesn't control or deploy tokens manually. [Nomad token bridge smart contracts](https://docs.nomad.xyz/token-bridge/smart-contracts) automatically deploy bridged token contracts when assets are bridged for the first time.

For a complete list of tokens and their addresses see the [Deployed Tokens List](https://docs.nomad.xyz/token-bridge/deployed-tokens/mainnet).

#### Why can't I see `<a specific token>` in the Nomad bridge application?

The Nomad core team adds tokens on a case-by-case basis in the web application.

We are actively adding more assets. If you would like an asset listed, make your voice heard in the Nomad [Discord](https://discord.gg/RurtmJApqm)!

You can also [use Etherscan](https://docs.nomad.xyz/token-bridge/how-to-bridge/using-etherscan) to bridge tokens that we have not listed in the web app.

#### Do you have `<blank>` feature? <a href="#do-you-have-blank-feature" id="do-you-have-blank-feature"></a>

We are adding new features and making updates on a daily basis. Some things we have in the works:

* Transaction History View
* Adding Custom Tokens
* General UI Improvements

If you'd like to see a specific feature added, please reach out in the Nomad [Discord](https://discord.gg/RurtmJApqm).

### Bridging 101 <a href="#bridging-101" id="bridging-101"></a>

#### I bridged over my assets with `someOtherBridgeNotNomad`, why can’t I see them?[#](https://docs.nomad.xyz/bridge/faq.html#i-bridged-over-my-assets-with-someotherbridgenotnomad-why-can%E2%80%99t-i-see-them) <a href="#i-bridged-over-my-assets-with-someotherbridgenotnomad-why-cant-i-see-them" id="i-bridged-over-my-assets-with-someotherbridgenotnomad-why-cant-i-see-them"></a>

Each bridge deploys their own token contracts, so assets bridged using one Bridge A are not compatible with assets bridged using Bridge B, even though they started out with the same original asset.

If you want to bridge over with Nomad but you've already used another bridge, you'll need to bridge *back* to the origin chain, and then bridge again with Nomad. This will get you back on track.

#### How long does it take to bridge? <a href="#how-long-does-it-take-to-bridge" id="how-long-does-it-take-to-bridge"></a>

Bridging using Nomad usually takes around 35 mins, but can be up to +60 mins depending on on- and off- chain activity (see our [docs on the Nomad architecture](https://docs.nomad.xyz/) for more information).

However, we've partnered with Connext to give users an option to have a faster cross-chain experience! For a small fee, you can use Connext to enable faster transfers--around 7-15 mins!

#### It's been longer than the estimated time--where are my tokens? <a href="#it-s-been-longer-than-the-estimated-time-where-are-my-tokens" id="it-s-been-longer-than-the-estimated-time-where-are-my-tokens"></a>

Ocassionally there are times where it takes longer to process a transaction. This could be due to on-chain activity, or a delay in agent processing.

This could also be due to missing a step in the process, such as when sending assets back to Ethereum. You'll need to manually process the transaction. See [this answer](https://docs.nomad.xyz/bridge/faq.html#why-is-gas-estimate-so-high-to-get-my-funds-on-ethereum).

#### Do I get WETH or ETH? <a href="#do-i-get-weth-or-eth" id="do-i-get-weth-or-eth"></a>

You can bridge over WETH or ETH from Ethereum, but you will always receive WETH on the destination. If you bridge over ETH, the contract will automatically call a helper function to wrap your ETH for you.

If you use Connext to bridge your WETH back to Ethereum, you will receive ETH automatically through the Connext process.

If you use Nomad to bridge your WETH back to Ethereum, you will receive WETH and will need to unwrap it manually if you want ETH again.

#### Do you have a development/testnet site? <a href="#do-you-have-a-development-testnet-site" id="do-you-have-a-development-testnet-site"></a>

Yes! It is available at [development.app.nomad.xyz](https://development.app.nomad.xyz/)

### Connext + Nomad <a href="#connext-nomad" id="connext-nomad"></a>

#### What is your relationship with Connext? <a href="#what-is-your-relationship-with-connext" id="what-is-your-relationship-with-connext"></a>

Nomad and Connext are complementary pieces that work together to provide a better cross-chain experience for users. Connext is an interoperability protocol that allows users to swap/transact over liquidity that already exists on the chain. Nomad is at its core protocol for passing generalized data between arbitrary chains, and the Nomad Bridge is an application built to pass specific kinds of messages that allow you to bridge tokens.

Connext routers set up cross-chain liquidity pools for Nomad assets. For a small fee, these liquidity pools allow users to make faster swaps, since the assets have already been bridged over.

#### I bridged using Connext, where are my tokens? <a href="#i-bridged-using-connext-where-are-my-tokens" id="i-bridged-using-connext-where-are-my-tokens"></a>

When you bridge with Connext, you'll need to manually claim your tokens after the transaction has processed. You can claim your transaction using the [Nomad bridge](https://app.nomad.xyz/), or you can also use the Connext UI at `https://connextscan.io/tx/<txId>`

### Bridging to Ethereum <a href="#bridging-to-ethereum" id="bridging-to-ethereum"></a>

#### I'm trying to bridge my assets back to Ethereum and it's taking a long time. <a href="#i-m-trying-to-bridge-my-assets-back-to-ethereum-and-it-s-taking-a-long-time" id="i-m-trying-to-bridge-my-assets-back-to-ethereum-and-it-s-taking-a-long-time"></a>

When you bridge back to Ethereum, you'll need to process the transaction manually to disperse your funds at the end. You can do this by going to: `https://app.nomad.xyz/tx/nomad/<origin-chain>/<tx-id>`

### General <a href="#general" id="general"></a>

#### What is madWETH? <a href="#what-is-madweth" id="what-is-madweth"></a>

These are the same assets! Often times applications will prefix assets depending on the bridge that was used. Nomad assets are listed with either no prefix (WETH), or the mad- prefix (madWETH). We prefer to use no prefix or the mad- prefix and will kindly ask applications to change this for us, but sometimes there may be a delay in this change.

#### Why does my recently-bridged token have a funny name like `0006648936.eb48`? <a href="#why-does-my-recently-bridged-token-have-a-funny-name-like-0006648936-eb48" id="why-does-my-recently-bridged-token-have-a-funny-name-like-0006648936-eb48"></a>

In order to avoid sending redundant data like the token name and symbol with every message, the first time a bridged ERC-20 Token representation is deployed, metadata is pulled from the originating chain after initial deployment. This involves a round-trip between the replica and originating chain wherein data about name/symbol/decimals is synced.

This is expected behavior, and the explorer will update after a day or two.

#### Why is the ERC-20 token placeholder name like that? <a href="#why-is-the-erc-20-token-placeholder-name-like-that" id="why-is-the-erc-20-token-placeholder-name-like-that"></a>

`0006648936.eb48` is the Nomad domain ID for Ethereum and the last 4 letters of the token address on Ethereum

`6648936 == 0x657468` -- the utf8 encoding of 'eth'

USDC's address is `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`

Note the `eb48` at the end.

# Overview

While many people believe the "killer app" for interoperability is token bridges, we believe there is an equally important and exciting opportunity in enabling effective cross-chain governance. That's why Nomad partnered with Gnosis to create the [Zodiac Nomad Module](https://docs.nomad.xyz/governance-bridge/zodiac-nomad-module) (ZNM) - which gives DAOs/protocols access to an out-of-the-box cross-chain governance solution that is simple, trust-minimized, and standardized.

The sections below will provide context on the need for effective cross-chain governance, how DAOs/protocols have attempted to implement cross-chain governance to-date, and why the ZNM module is an improvement over other governance solutions available.

If you are interested in using Nomad for cross-chain governance, please reach to us at <gm@nomad.xyz>.

## Governance: A Brief History

#### **The Early Days of Decentralized Governance**

Cross-chain governance is a pain point that DAOs are now beginning to experience as they expand beyond Ethereum. In order to understand how we arrived here, we need to look at recent history to understand the current governance landscape.

Following Compound's launch of $COMP in the summer of 2020 (DeFi Summer), many DeFi protocols/apps and DAOs began decentralizing ownership to their communities via a governance token. This ownership model allowed early users and believers of a protocol to become governance stakeholders and shepherd its growth through a DAO rather than a core team.

Compound's governance framework quickly became the status quo, and its [Governor Bravo design](https://blog.tally.xyz/understanding-governor-bravo-69b06f1875da) still continues to serve as the gold standard for governance frameworks to this day. In large part, the playbook for governance is now straightforward, and many DAOs have adopted it successfully - enabling their token holders to propose, vote, and execute governance actions on-chain.

#### More Chains, More Problems

Initially, when most protocols launched decentralized token-based governance, they deployed these systems exclusively on Ethereum Mainnet.&#x20;

Today, many of these DAOs are faced with a problem: their governance is deployed on one chain (typically Ethereum), but their protocol is deployed on many chains. This leads to a setup where the collective "brain" lives on one chain, with many "satellites" deployments that need to mirror the core deployment.

![Governance on Ethereum has no way to communicate to Polygon or Optimism](https://lh5.googleusercontent.com/V1O2-iSAf-Km4bYc8pwMKST8v6nNMFPdAkMuiZYq3Vpj2mNSYw5NaHu4KjVGS09ROrniCQf2kPIlNTDWK9yVkWEP6gIu-etcvqwPVZe_qaQelWL6OoBcpbNo_fXsrrRovwPtyFK521mV8tfB-A)

In a multi-chain world, DAOs are effectively limited in their ability to govern their own protocols on different chains. **Without some way to communicate the results of a governance vote to their satellite deployments, protocols become out of sync and inconsistent.**

#### Attempted Solutions for Cross-Chain Governance

Many of the earliest DeFi protocols that decentralized to a community-governed DAO have experienced this pain directly. In order to govern multi-chain protocol deployments, DAOs have largely tried three strategies, each with pros and cons:

1. **Patching together existing solutions by chain** — this strategy conforms governance proposals to the interface of the "canonical" bridge where each satellite deployment lives. For example, a Polygon deployment and Arbitrum deployment would each require a bespoke implementation and process to manage proposals over the respective bridges, as each was developed independently
   * **Pros:** leverages existing "canonical" bridges
   * **Cons:** more overhead and complexity to implement, no standardization&#x20;
2. **Rolling your own solution** — some DAOs like Aave have [developed their own governance bridges](https://github.com/aave/governance-crosschain-bridges), in an effort to standardize governance across their deployments. This requires building everything from scratch and managing the contracts and infrastructure to pass governance messages to each deployment.
   * **Pros:** no external dependencies, standardized locally
   * **Cons:** major lift for an protocol/app core team to maintain, not standardized across protocols/apps
3. **Not worrying about decentralization** — the last strategy is to simply not worry about decentralized cross-chain governance, and to use a multi-sig for governance of satellite deployments. In this approach, a protocol/app can avoid token governance entirely, or simply elect multi-sig key holders who are expected to mirror the flagship deployment's governance processes.
   * **Pros:** simple and straightforward
   * **Cons:** totally centralized and defeats the purpose of token-based governance

**The fact is, none of these solutions satisfies the core need — trust-minimized, standardized, and simple to implement/maintain bridge for cross-chain governance.**

### A better solution: Zodiac + Nomad&#x20;

We built [the Zodiac Nomad Module](https://docs.nomad.xyz/governance-bridge/zodiac-nomad-module) (ZNM) because we believe cross-chain governance matters, and Nomad's protocol is uniquely designed (optimistic and security-first) to meet this use case better than any other interoperability solution out there. It's through understanding this problem that we teamed up with Gnosis to develop it (originally nicknamed "Gnomad" 😁).

The Zodiac Nomad Module provides an out-of-the-box solution for cross-chain governance that is simple, trust-minimized, and standardized. DAOs can leverage the ZNM anywhere Nomad [messaging channels](https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging) are deployed to ensure executed governance proposals can be passed to all of their deployments.

To learn more about the ZNM, [check out the docs here](https://docs.nomad.xyz/governance-bridge/zodiac-nomad-module).

If you are a contributor to a DAO or protocol/app that is considering cross-chain governance, please reach out to us via email (<gm@nomad.xyz>) to learn more about cross-chain governance and how Nomad can support your use case!

# Zodiac: Nomad Module

Nomad has partnered with Gnosis to develop the [Zodiac Nomad Module](https://github.com/gnosis/zodiac-module-nomad) (ZNM) that enables accounts and contracts on one chain to control an "avatar" on another chain using Nomad's message passing layer. Using the ZNM, users can vote on a "home" chain where governance tokens are deployed (usually Ethereum) and pass results to another chain (eg. Gnosis Chain) using Nomad.

Codebase: <https://github.com/gnosis/zodiac-module-nomad>

# Smart Contracts

Codebase: <https://github.com/gnosis/zodiac-module-nomad>

# NomadModule

Contract code: <https://github.com/gnosis/zodiac-module-nomad/blob/main/contracts/NomadModule.sol>

# Architecture

TODO:

* Migrate references to ZNM
* Update links to stale documentation + old monorepo

### Summary <a href="#summary" id="summary"></a>

#### Purpose <a href="#purpose" id="purpose"></a>

This document describes **a governable system for executing permissioned actions across chains**.

We aim to clearly describe

* **what** contracts comprise the system for calling permissioned functions across chains
* **which** functions will be delegated to this system at launch, and
* (directionally) **who** will have permission to call these functions at launch and in the future

#### Out of Scope <a href="#out-of-scope" id="out-of-scope"></a>

This document does NOT describe a system for **how** governance actions will be proposed, voted on, and/or approved before being executed.

It does not describe how contract upgrades will be written, reviewed, verified.

#### Overview <a href="#overview" id="overview"></a>

{% hint style="info" %}
**Pre-requisite Reading**

* If you're not familiar with how Nomad cross-chain messaging passing works, we recommend checking out the Protocol section on [Cross-chain Messaging](https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging).
* It may also help to familiarize yourself with the [Router Pattern](https://docs.nomad.xyz/developers/application-developers/advanced/router-pattern). The `GovernanceRouter` described below follows this pattern in the context of a cross-chain governance xApp.
  {% endhint %}

We define a role, `governor`, with the power to perform permissioned actions across chains. In order to empower the `governor`, we deploy a cross-chain application comprised of a `GovernanceRouter` contract on each chain.

Each `GovernanceRouter` can be delegated control over an arbitrary set of permissioned functions on its local chain. The only way to access the permissioned functionality is to call the function via the `GovernanceRouter` contract.

Each `GovernanceRouter` is programmed to accept messages ***only*** from the `governor`, which is deployed on only one chain. The `governor` may call the contract locally (if it is deployed on the same chain), or it may send it messages remotely via Nomad. Because of its exclusive power over the `GovernanceRouter` contracts, the `governor` has exclusive rights to perform **all** of the permissioned roles that are delegated to the `GovernanceRouter` on each chain.

The system receives orders from the `governor` and carries out their effects across chains; it is agnostic to how the `governor` chooses to operate. This maintains flexibility to design the governance proposal process in the future.

At launch, the core functionality that will be delegated to the `GovernanceRouter` on each chain is the power to upgrade the implementation of the `Home` and `Replica` contracts. This way, the `governor` will have the power to conduct upgrades of the Nomad system on every chain. More details on the upgradability system can be found [here](https://docs.nomad.xyz/dev/upgrade-setup.html).

At launch, the `governor` will be a multisig of trusted team and community members. In the near future, the `governor` role will most likely be transferred to a more fully-featured set of contracts capable of accepting proposals, tallying votes, and executing successful proposals.

### Message Flow Diagram <a href="#message-flow-diagram" id="message-flow-diagram"></a>

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FyGE0t2b2lc8mGI6Qbucq%2Fimage.png?alt=media\&token=d7e203a7-2bcf-4daf-8dc0-33def54a546d)

1. `governor` sends message to its local `GovernanceRouter`
2. `GovernanceRouter` dispatches the message...
   1. if the recipient is local, to the recipient directly (→ process finished)
   2. if the recipient is remote, via Nomad to the local Home contract (→ continue to 3)
3. Message is relayed from local `Home` to remote `Replica` via Nomad
4. `Replica` dispatches message to the remote `GovernanceRouter`
5. `GovernanceRouter` dispatched the message directly to the local recipient

**Note on message recipient:**

* the recipient may be a `Replica` or `Home` contract
* it may be an `UpgradeBeacon` that controls the implementation of `Replica` or `Home`
* it may be any other app

For simplicity & clarity to show the message flow, this diagram represents the recipient as a generic "App"

### Specification <a href="#specification" id="specification"></a>

#### Glossary of Terms <a href="#glossary-of-terms" id="glossary-of-terms"></a>

* **xApp** - Cross-Chain Application
* **role** —
  * an address stored in a smart contract's state that specifies an entity with special permissions on the contract
  * permission to call certain functions is usually implemented using a function modifier that requires that the caller of the function is one of the roles with permission to call it; all contract calls sent from callers that do not have valid permission will revert
  * *example*: `owner` is the **role** set on all [Ownable](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol) contracts upon deployment; the `owner` **role** has exclusive permission to call functions with the `onlyOwner` modifier
* **permissioned function** —
  * any smart contract function that restricts callers of the function to a certain role or roles
  * *example*: functions using the `onlyOwner` modifier on [Ownable](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol) contracts
* **permissioned call** — a call to a **permissioned function**
* **governor chain** —
  * the chain on which the `governor` is deployed
  * the chain whose `GovernanceRouter` is also the special `GovernorRouter` which can *send* messages; all `GovernanceRouters` on other chains can only *receive* governance messages

#### On-Chain Components <a href="#on-chain-components" id="on-chain-components"></a>

**GovernanceRouter**

* xApp designed to perform permissioned roles on core Nomad contracts on all chains
* State Variables
* **governor** state variable
  * if the `governor` is local, `governor` will be set to the EVM address of the `governor`
  * if the `governor` is remote, `governor` will be `address(0)`
* **governorDomain** state variable
  * the Nomad domain of the **governor chain**
  * stored as a state variable on all `GovernanceRouters`; should be the same on all `GovernanceRouters`; always non-zero
    * if the `governor` is local, `governorDomain` is equal to the `originDomain` of the local `Home` contract
    * if the `governor` is remote, `governorDomain` is equal to the `originDomain` of the remote `Home` contract
  * equal to the `originDomain` of the local `Home` contract on the chain of the `GovernorRouter`
  * used by all `GovernanceRouters` to determine whether an incoming Nomad message was sent from the `GovernorRouter`
    * if the message is from the `GovernorRouter`, the `GovernanceRouter` will handle the incoming message
    * if not, it will revert
* **routers** state variable
  * a mapping of domain → address of the remote `GovernanceRouter` on every other chain
* **domains** state variable
  * an array of all domains that are registered in `routers`
  * used to loop through and message all other chains when taking governance actions
  * there is the possibility that some domains in the array are null (if a chain has been de-registered)
* **GovernorRouter**
  * the special `GovernanceRouter` that has *permission to send* governance messages to all other `GovernanceRouters`
  * the `GovernanceRouter` on the **governor chain**

**Governor**

* via the `GovernanceRouter` system, it has the unique ability to call permissioned functions on **any contract** on **any chain** that transfers permission to the local `GovernanceRouter`
* the **role** with permission to send messages to the `GovernorRouter`
  * the `GovernorRouter` has exclusive permission to send messages via Nomad to all other `GovernanceRouters`
  * the `GovernanceRouters` can have arbitrary permissions delegated to them by any contract on their local chain
  * therefore, the `governor` is the entity with the power to call any **permissioned function** delegated to any `GovernanceRouter` on any chain
* there is only one `governor` throughout the Nomad system; it can be deployed on any chain
* the `governor` role can always be transferred to another contract, on the same chain **or** a different remote chain
* stored as a state variable on `GovernanceRouters`; set to zero on all `GovernanceRouters` except on the **governor chain**
* **Any contract** on **any chain** that wishes for this governance system to have discretion to call a set of its functions can create a role & a function modifier giving exclusive permission to that role to call the function(s) (similar pattern to Ownable). The contract must then set the local `GovernanceRouter` to the permissioned role, which — by extension — gives the `governor` exclusive permission to call those functions (regardless of whether the `governor` is remote or local)

#### Failure States[#](https://docs.nomad.xyz/dev/governance.html#failure-states) <a href="#failure-states" id="failure-states"></a>

If there is fraud on the Nomad `Home` contract on the **governor chain**, this is currently a "catastrophic failure state" — no further governance actions can be rolled out to remote chains; we must create a plan to recover the system in this case.

***

### Message Types <a href="#message-types" id="message-types"></a>

#### Executing (Arbitrary) Calls <a href="#executing-arbitrary-calls" id="executing-arbitrary-calls"></a>

1. **for each chain**, the `governor` constructs the array of `(to, data)` calls to the permissioned functions on the contracts that will perform the upgrades on that chain
2. the `governor` sends a transaction to the `GovernanceRouter.callRemote` function on its local the , passing in the `domain` of the remote chain and the array of `(to, data)` calls of transactions to execute on that chain
3. the local `GovernanceRouter` constructs an Nomad-compatible message from the array of calls, addresses the message to the remote `GovernanceRouter`, and sends the message to the local `Home` contract
4. the message is relayed from the local `Home` to the remote `Replica` contract on the specified `domain`
5. the `Replica` dispatches the message to the specified recipient, which is the local `GovernanceRouter`
6. the `GovernanceRouter` parses the message to decode the array of `(to, data)` calls
7. the `GovernanceRouter` uses low-level call to execute each of the transactions in the array within the local chain

#### **Transferring Governor** <a href="#transferring-governor" id="transferring-governor"></a>

**Possible State Transitions**

1. called by the local owner to transfer ownership to another local owner (`domain` does not change, `owner` changes to a new `bytes32` address)
2. called by the local owner to transfer ownership to a remote owner (`domain` changes to the remote, `owner` changes from a non-zero `bytes32` to `bytes32(0)`)
3. called by a remote owner to transfer ownership to a local owner (`domain` changes to the local domain, `owner` changes from `bytes32(0)` to a non-zero `bytes32`)
4. called by a remote owner to transfer ownership to another remote owner (`domain` changes to the new remote owner, `owner` remains `bytes32(0)`)

#### Enrolling a Router <a href="#enrolling-a-router" id="enrolling-a-router"></a>

* used when a new chain is added to Nomad after we've already set up the system and transferred governorship
* add a new domain → address mapping to the `routers` mapping on every other `GovernanceRouter`

***

### Functionality at Launch <a href="#functionality-at-launch" id="functionality-at-launch"></a>

#### Permissioned Roles <a href="#permissioned-roles" id="permissioned-roles"></a>

At launch, the `GovernanceRouter` system **will have the following permissions**:

1. upgrade the implementation of `Home` (via `UpgradeBeacon` pattern)
2. upgrade the implementation of all `Replicas` (via 1-to-N `UpgradeBeacon` pattern)
3. upgrade the implementation of itself (via `UpgradeBeacon` pattern)

The `GovernanceRouter` **will NOT have permission** to:

* un-enroll a `Replica` from the `UsingNomad` contract, which will require a specialized role that can act quickly

#### Governor <a href="#governor-1" id="governor-1"></a>

The flexibility of this system will support a move to progressive decentralization.

Initially, the `governor` will most likely be a multisig controlled by trusted team and community members

Later, the `governor` role will most likely be transferred to a decentralized governance contract

# Quickstart

Your one-stop shop to start building cross-chain applications (xApps).

Developing on Nomad is easy as pie. Plug your app into our smart contracts to begin [**sending**](https://docs.nomad.xyz/developers/quickstart/send-messages) and [**receiving**](https://docs.nomad.xyz/developers/quickstart/receive-messages) cross-chain messages.

### Getting Started

Read our **tutorial** to learn how to build cross-chain with Nomad.

### **Time to BUIDL**

Fork our **template repo** to get started.

### Example Apps

Look here at our [**example xApps**](https://docs.nomad.xyz/developers/application-developers/examples).&#x20;

### Need Inspiration?

Peep some **xApp ideas** we'd like to see built on Nomad.

### Got Questions?

We've got answers! Check out our **FAQ** or hop in our [**Discord**](https://discord.gg/RurtmJApqm) to chat

# Send Messages

The on-chain API for sending cross-chain messages

Send messages to other chains by calling the `dispatch()` method on the `Home` contract.

### Interface

The `dispatch` method is simple. Just specify the destination chain, the message recipient, and the message you want to send!

* `_destination` is a Nomad domain. List of domains **here**
* `_recipient` is the address that will receive the message on the destination chain. The `_recipient` must be set up to **receive** Nomad messages by implementing `handle`.
* `_message` contains the contents of your cross-chain message&#x20;

```solidity
/*
 * @notice Dispatch the message to the destination domain & recipient
 * @param _destination Domain of destination chain
 * @param _recipient Address of recipient on destination chain as bytes32
 * @param _message Raw bytes content of message
 */
 function dispatch(
     uint32 _destination,
     bytes32 _recipient,
     bytes memory _message
 ) external {
   // message is sent to recipient address on destination chain
 }
```

### Hello World

The example app we know and love - but make it cross-chain :handshake:&#x20;

```solidity
 import {TypeCasts} from "@nomad-xyz/contracts-core/libs/TypeCasts.sol";
 
 contract HelloWorld {
    // address of the Nomad Home contract
    immutable address public home;

    /*
     * @notice Send a Hello message to another chain :)
     * @param _destination Domain of destination chain
     * @param _recipient Address of recipient on destination chain
     */
    function hello(uint32 _destination, address _recipient) {
        // craft your hello message
        bytes memory _message = "hello world >:~)";
        // cast recipient to bytes32
        bytes32 _recip = TypeCasts.addressToBytes32(_recipient);
        // dispatch your message across chains!
        home.dispatch(_destination, _recipient, _message);
    }
}
```

### Example Usage

Ready to get a little more advanced? Let's play PingPong across chains :ping\_pong:

```solidity
contract PingPong {
    // registry of opponents on each chain
    mapping(uint32 => bytes32) public opponents;

    /**
     * @notice Start a PingPong match with the destination chain
     * by serving the ball.
     * @param _destination The domain to initiate the match with
     */
    function serve(uint32 _destination) external {
        // serve to your opponent on the destination domain
        bytes32 _recipient = opponents[_destination];
        // Create a message for the first volley.
        // the PingPong match always begins with a Ping
        bool _ping = true;
        // the volley count always starts at 0
        uint256 _volley = 0;
        // encode the PingPong message using abi.encode
        bytes memory _message = abi.encode(_ping, _volley);
        // dispatch your message across chains!
        home.dispatch(_destination, _recipient, _message);
    }

}
```

### Advanced Examples

* `BridgeRouter.sol` [send](https://github.com/nomad-xyz/monorepo/blob/93daaf931378b79c53e3c494af9671c59e843ee1/packages/contracts-bridge/contracts/BridgeRouter.sol#L134)
* `GovernanceRouter.sol` [executeGovernanceActions](https://github.com/nomad-xyz/monorepo/blob/497a0f702100800db7e37576ca16f76c180830f5/packages/contracts-core/contracts/governance/GovernanceRouter.sol#L254)

### **FAQs**

**Why domains instead of chain IDs?**

Chain IDs change during intentional consensus splits such as the merge to Eth2.0; additionally, not all chains even have a Chain ID! We created Nomad domains to have a clean standard for chains supported by Nomad which didn't suffer from these challenges. &#x20;

**Why are recipients `bytes32` instead of `address`?**

We use `bytes32` instead of `address` so that, in the future, messages will be compatible with other chain VMs like Cosmos and Polkadot. In the EVM, addresses are 20 bytes long, but most other chains have 32 byte addresses. Worry not - we have a `TypeCasts.sol` library to help convert between these types easily.

# Receive Messages

The on-chain API for receiving cross-chain messages

Receive messages from other chains by implementing the `handle()` method in your cross-chain application.

### Interface

The `handle` method passes a cross-chain message to the application.

* `_origin` is a Nomad domain. List of domains **here**
* `_nonce` is unique for each message within a (`origin` domain, `destination` domain) tuple. Many apps won't need to use this field, but it can be used to ensure uniqueness of a message.
* `_sender` is the address that **sent** the message on the origin domain
* `_message` contains the contents of the cross-chain message&#x20;

```solidity
/*
 * @notice Receive a message from a sender on the origin domain 
 * @param _origin Domain of the origin chain
 * @param _nonce Unique nonce for the (origin, destination) tuple. 
 * @param _sender Address of sender on origin chain as bytes32
 * @param _message Raw bytes content of message
 */
 function handle(
    uint32 _origin,
    uint32 _nonce,
    bytes32 _sender,
    bytes memory _message
) external;
```

### Hello World

The example app we know and love - but make it cross-chain :handshake:&#x20;

```solidity
 import {TypeCasts} from "@nomad-xyz/contracts-core/libs/TypeCasts.sol";
 
 contract HelloWorld {
    // emitted when a Hello message is received   
    event Hello(uint32 origin, address sender, string memory message);
    
   /*
    * @notice Receive a Hello message from any sender :) 
    * @param _origin Domain of the origin chain
    * @param _sender Address of sender on origin chain as bytes32
    * @param _message Raw bytes content of message
    */
    function handle(
       uint32 _origin,
       uint32 _nonce,
       bytes32 _sender,
       bytes memory _message
    ) onlyReplica {
       address _sendr = TypeCasts.bytes32ToAddress(_sender);
       // emit the message so off-chain friends can see it
       emit Hello(_origin, _sendr, _message);
    }
}
```

### Example Usage

Ready to get a little more advanced? Let's play PingPong across chains :ping\_pong:

```solidity
contract PingPong {
    // registry of opponents on each chain
    mapping(uint32 => bytes32) public opponents;
    
    // emitted when a Ping volley is received
    event Ping(uint32 domain, bytes32 opponent, uint256 volleyNumber);
    // emitted when a Pong volley is received
    event Pong(uint32 domain, bytes32 opponent, uint256 volleyNumber);

    /**
     * @notice Start a PingPong match with the destination chain
     * by serving the ball.
     * @param _destination The domain to initiate the match with
     */
    function handle(
       uint32 _origin,
       uint32 _nonce,
       bytes32 _sender,
       bytes memory _message
    ) onlyReplica {
        // validate the message comes from a known opponent
        require(opponents[_origin] == _sender, "not a registered opponent!");
        // decode the message contents using abi.decode
        bool _ping;
        uint256 _volley;
        (_ping, _volley) = abi.decode(_message, (bool, uint256));
        // emit an event for your off-chain spectators
        if (ping) {
            emit Ping(_origin, _sender, _volley);
        } else {
            emit Pong(_origin, _sender, _volley);
        }
        // send a PingPong message back to your opponent!
        bytes memory _message = abi.encode(!_ping, _volley + 1);
        // dispatch your message across chains
        home.dispatch(_origin, _sender, _message);
    }
}
```

### Advanced Examples

* `BridgeRouter.sol`[handle](https://github.com/nomad-xyz/monorepo/blob/93daaf931378b79c53e3c494af9671c59e843ee1/packages/contracts-bridge/contracts/BridgeRouter.sol#L105)
* `GovernanceRouter.sol` [handle](https://github.com/nomad-xyz/monorepo/blob/497a0f702100800db7e37576ca16f76c180830f5/packages/contracts-core/contracts/governance/GovernanceRouter.sol#L222)
* Gnosis `NomadModule.sol` [handle](https://github.com/gnosis/zodiac-module-nomad/blob/609a044936a95d51dcd6063b902494ea9baafa8a/contracts/NomadModule.sol#L153)

### **FAQs**

**Why ensure messages come from `onlyReplica`?**

This ensures that the message is a real cross-chain message coming from the Nomad system, not an impostor!&#x20;

# Environments

Interact with Nomad across testnet and mainnet environments

Nomad is currently deployed on both mainnet and testnets of various networks, across three environments:

* Development
* Staging
* Production

### Contract Addresses

The addresses of Nomad contracts deployed on-chain can be found in our [configuration](https://github.com/nomad-xyz/config) package.&#x20;

Our [development](https://github.com/nomad-xyz/config/blob/main/development.json) environment is deployed on testnets and intended for Nomad core team to test new features and debug. It is unstable!

Our [staging](https://github.com/nomad-xyz/config/blob/main/staging.json) environment is deployed on testnets so that developers can test their cross-chain applications.

Our [production](https://github.com/nomad-xyz/config/blob/main/production.json) environment is deployed on mainnets for real-world application usage.

### Bridge App

The Nomad bridge app is available in both environments.

Production: [https://app.nomad.xyz/](https://staging.app.nomad.xyz/)

Staging: <https://staging.app.nomad.xyz/>

Development: <https://development.app.nomad.xyz/>

# Domain (Chain) IDs

{% hint style="warning" %}
Domain IDs do not map to networks' `ChainID` — they are entirely separate, and only used within Nomad.
{% endhint %}

### Mainnet <a href="#mainnet" id="mainnet"></a>

| Domain              | ID         |
| ------------------- | ---------- |
| Ethereum            | 6648936    |
| Moonbeam            | 1650811245 |
| Evmos               | 1702260083 |
| Milkomeda C1        | 25393      |
| Avalanche           | 1635148152 |
| Gnosis Chain (xdai) | 2019844457 |

### Testnet - Staging <a href="#testnet" id="testnet"></a>

| Domain       | ID   |
| ------------ | ---- |
| Evmostestnet | 4441 |
| Goerli       | 3331 |
| Neontestnet  | 5551 |
| Rinkeby      | 1111 |

### Testnet - Development

| Domain          | ID   |
| --------------- | ---- |
| Arbitrumrinkeby | 6661 |
| Goerli          | 3001 |
| Neontestnet     | 5001 |
| Evmostestnet    | 4001 |

# Application Developers

# Building xApps

A xApp (pronounced "zap") is a cross-chain application built on top of the [Nomad Protocol](https://docs.nomad.xyz/the-nomad-protocol).

Nomad sends messages from one chain to another in the form of raw bytes. A xApp that wishes to *use* Nomad will need to define the rules for [sending](https://docs.nomad.xyz/developers/quickstart/send-messages) and [receiving](https://docs.nomad.xyz/developers/quickstart/receive-messages) messages for its use case.

Each cross-chain application must implement its own messaging interface. By convention, we call the contracts that implement this protocol the application's **Router contracts.** These Router contracts must:

* **Maintain a permissioned set** of the contract(s) on remote chains from which it will accept messages via Nomad — this could be a single owner of the application on one chain; it could be a registry of other applications implementing the same rules on various chains
* **Maintain a permissioned registry of connections** via the `XappConnectionManager` contract (see [Connection Management](#connection-management)).
* **Encode messages in a standardized format**, so they can be decoded by the Router contract on the destination chain
* **Handle messages** from remote Router contracts
* **Dispatch messages** to remote Router contracts

By implementing these pieces of functionality within a Router contract and deploying it across multiple chains, we create a working xApp using a common language and set of rules. Applications of this kind may use Nomad message passing channels as the cross-chain courier for sending and receiving messages between chains.

### Connection Management <a href="#connection-management" id="connection-management"></a>

The router implements the [`XappConnectionClient`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-router/contracts/XAppConnectionClient.sol) abstract contract. This contract provides convenience functions for working with a [`XAppConnectionManager`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/XAppConnectionManager.sol).

The XCM is the primary permissioning point for channels. It provides functions by which

* xApp administrators can enroll or unenroll `Replica` contracts for inbound messages
* xApp administrators can enroll or unenroll a `Home` contract for outbound messages
* xApp administrators can permission or de-permission watchers
* watchers can unenroll `Replica` contracts

When deploying a xApp `Router`, the xApp administrators must select an existing `XappConnectionManager`, or deploy their own. The address of the `XappConnectionManager` must be passed to the router's initialization method.<br>

# SDK

#### Core <a href="#core" id="core"></a>

* [npm package](https://www.npmjs.com/package/@nomad-xyz/sdk)
* [docs](https://docs.nomad.xyz/sdk/)

#### Bridge <a href="#bridge" id="bridge"></a>

* [npm package](https://www.npmjs.com/package/@nomad-xyz/sdk-bridge)
* [docs](https://docs.nomad.xyz/sdk-bridge/)

#### Governance <a href="#governance" id="governance"></a>

* [npm package](https://www.npmjs.com/package/@nomad-xyz/sdk-govern)
* [docs](https://docs.nomad.xyz/sdk-govern/)

#### Multi Provider <a href="#multi-provider" id="multi-provider"></a>

* [npm package](https://www.npmjs.com/package/@nomad-xyz/multi-provider)

# Contracts SDK

# Typescript SDK

# Examples

TODO: cleanup links from old monorepo

### Example Code <a href="#example-code" id="example-code"></a>

This repository has several examples one can use to build understanding around Cross-Chain Applications.

#### xApp Template <a href="#xapp-template" id="xapp-template"></a>

{% hint style="warning" %}
**Important!** The template supported Solidity version is **<0.8**!
{% endhint %}

[This is a template](https://github.com/nomad-xyz/nomad-monorepo/tree/main/solidity/nomad-xapps/contracts/xapp-template) provided by the Nomad team that shows the high-level components of an xApp, ready for one to fill in their own application logic and utilize a Nomad channel for cross-chain communication.

To implement a xApp, define the actions you would like to execute across chains. For each type of action,

* In the [xApp Router](https://github.com/nomad-xyz/nomad-monorepo/blob/main/solidity/nomad-xapps/contracts/xapp-template/RouterTemplate.sol):
  * implement a function like doTypeA to initiate the action from one domain to another (add your own parameters and logic)
  * implement a corresponding \_handle function to receive, parse, and execute this type of message on the remote domain
  * add logic to the handle function to route incoming messages to the appropriate \_handle function
* In the [Message library](https://github.com/nomad-xyz/nomad-monorepo/blob/main/solidity/nomad-xapps/contracts/xapp-template/MessageTemplate.sol):
  * implement functions to *format* the message to send to the other chain (encodes all necessary information for the action)
  * implement functions to *parse* the message once it is received on the other chain (decode all necessary information for the action)

#### Connection Management <a href="#connection-management" id="connection-management"></a>

The router implements the [`XappConnectionClient`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-router/contracts/XAppConnectionClient.sol) abstract contract. This contract provides convenience functions for working with a [`XAppConnectionManager`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/XAppConnectionManager.sol).

See the section on [Connection Management](https://docs.nomad.xyz/developers/building-xapps#connection-management).

# Ping Pong

{% hint style="warning" %}
The Ping Pong xApp is for reference only. Please do not deploy!
{% endhint %}

[The PingPong xApp](https://github.com/nomad-xyz/nomad-monorepo/tree/main/solidity/nomad-xapps/contracts/ping-pong) is capable of initiating PingPong "matches" between two chains. A match consists of "volleys" sent back-and-forth between the two chains via Nomad.

The first volley in a match is always a Ping volley.

* When a Router receives a Ping volley, it returns a Pong.
* When a Router receives a Pong volley, it returns a Ping.

The Routers keep track of the number of volleys in a given match, and emit events for each Sent and Received volley so that spectators can watch.

# Advanced

# Router Pattern

Nomad sends messages from one chain to another in the form of raw bytes. A cross-chain application (xApp) that wishes to use Nomad will need to define the rules for [sending](https://docs.nomad.xyz/developers/quickstart/send-messages) and [receiving](https://docs.nomad.xyz/developers/quickstart/receive-messages) messages for its use case.

Each xApp must implement its own interface. We call the contracts that implement this interface "Router" contracts, as their function is broadly similar to routers in local networks. Router contracts ensure that incoming and outgoing messages are in the correct format defined by the application developers, and facilitate handling and dispatch to their destination contracts.

**Router contracts must:**

* maintain a permissioned set of the contract(s) on remote chains from which it will accept messages via Nomad — this could be a single owner of the application on one chain; it could be a registry of other applications implementing the same rules on various chains
* encode messages in a standardized format, so they can be decoded by the Router contract on the destination chain
* handle messages from remote Router contracts
* dispatch messages to remote Router contracts

By implementing these pieces of functionality within a Router contract and deploying it across multiple chains, we create a working cross-chain application using a common language and set of rules. Applications of this kind may use Nomad as the cross-chain courier for sending and receiving messages to each other.

# Node Operators

* [Running Agents Guide](https://docs.nomad.xyz/developers/node-operators/running-agents-guide) - How to Configure/Run Agents
* [Running a Watcher](https://docs.nomad.xyz/developers/node-operators/running-a-watcher) - How to Setup/Run a Watcher
* [Agent Operations](https://docs.nomad.xyz/developers/node-operators/agent-operations) - How to Operate Agents in Production
* [Agent Gas Values](https://docs.nomad.xyz/developers/node-operators/agent-gas-values) - Reasoning Behind Custom Gas Limits for Agent Contract Calls
* [The Keymaster](https://docs.nomad.xyz/developers/node-operators/the-keymaster) - Tooling for Agent Wallets

# Running Agents Guide

### Overview <a href="#overview" id="overview"></a>

Nomad agent processes observe and index on-chain events, interacting with multiple blockchains in order to facilitate cross-chain messaging.

{% hint style="info" %}
See the [Off-Chain Agents](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents) section for details on each agent role.
{% endhint %}

#### Home/Replica Model

Nomad channels are d*ual-simplex*. This simply means they are composite bi-directional communication channels between two given blockchains. Each composite channel is composed of a single data channel flowing in one direction paired with a corresponding data channel flowing in the opposite direction.  These data channels flow outward from the [Home contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) on each blockchain.&#x20;

Agents are architected in a Home-centric model, meaning that by default agents must be configured with secrets like signing keys and RPC endpoints for each blockchain that the configured Home has a Replica on.

This means if you want to facilitate bi-directional communication between two or more networks (or *Watch* both directions of a channel), *you must run one agent instance per Home.*

{% hint style="info" %}
If that didn't make much sense, go read [Cross-Chain Messaging](https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging) and come back.
{% endhint %}

### Configuring an Agent <a href="#configuring-an-agent" id="configuring-an-agent"></a>

Agents are simple Rust binaries that are easily run inside [Docker Containers](https://www.docker.com/). Agents read runtime configuration from a mix of JSON config files and environment variables.&#x20;

Configuration is loaded in the following order:&#x20;

1. Built-In Configuration&#x20;
2. Configuration File&#x20;
3. Environment Variables

#### Nomad Configuration Repository

Nomad publishes JSON configurations for each of the three public environments we operate, they can be found in the [Nomad Configuration Repository](https://github.com/nomad-xyz/config) on Github. These configs provide public network info such as contract addresses and chain finality settings which the agents consume.&#x20;

By default, agents get compiled with the JSON environment configuration that was available at compile-time, however this config can be optionally overridden at runtime via the `CONFIG_PATH` environment variable. &#x20;

#### Environment Variables&#x20;

The agent has specific required environment variables, but additionally supports specific additional configuration overrides. The key fields one must specify are detailed below.&#x20;

{% hint style="info" %}
Note:`DEFAULT`\_ values are only used if a network-specific override is not provided.
{% endhint %}

#### **Run Environment**

* `RUN_ENV`: Used to switch between built-in environments \
  `development`, `staging`, or `production`&#x20;

#### **Agent Home**

* `AGENT_HOME_NAME`: A network name which the agent will treat as *Home*, see [built-in configs](https://github.com/nomad-xyz/config) for details

#### **Agent Replicas**

* Specify networks:
  * `AGENT_REPLICA_0_NAME`, `AGENT_REPLICA_1_NAME`, `AGENT_REPLICA_2_NAME`, etc...
  * What replica(s) the agent will run against
* Default to all connected networks:
  * `AGENT_REPLICAS_ALL`
  * Expects all connected replicas if `true`
  * Expects specified networks if `false` or not set

#### **RPC Info**

* Network-specific:
  * `{network}_RPCSTYLE`: What RPC style `network` is; "ethereum" for all EVM chains
  * `{network}_CONNECTION_URL`: RPC endpoint url
* Default:
  * `DEFAULT_RPCSTYLE`: Default rpc style for any network not explicitly configured

#### **Transaction Submission Info**

* Network-specific:
  * Transaction Submission Type:
    * `{network}_SUBMITTER_TYPE`
    * `local` for local signing/submitting
    * `gelato` if you are integrated with Gelato Relay
  * Local Submission:
    * Transaction signer key:
      * Hex key:
        * `{network}_TXSIGNER_KEY`
        * Raw 0x-prefixed hex key
      * AWS Key:
        * `{network}_TXSIGNER_ID`
        * AWS key id
  * Gelato Submission (ignore if you do not plan on using Gelato Relay):
    * Sponsor signer:
      * Hex key:
        * `{network}_GELATO_SPONSOR_KEY`
        * Raw 0x-prefixed hex key
      * AWS Key:
        * `{network}_GELATO_SPONSOR_ID`
        * AWS key id
    * Fee token
      * `{network}_GELATO_SPONSOR_FEETOKEN`
      * 0x-prefixed token contract address
* Default:
  * Default for any network not explicitly configured
  * Same as network-specific (above) but replacing specific `{network}` with `DEFAULT`
  * Example:
    * `DEFAULT_SUBMITTER_TYPE=local`
    * `DEFAULT_TXSIGNER_ID=some_aws_id`
    * All networks use `local` transaction submission with the default txsigner key

#### **Attestation Signer (optional)**

* Required *only* for updater and watcher
* Hex key:
  * `ATTESTATION_SIGNER_KEY`
  * Raw 0x-prefixed hex key
* AWS Key:
  * `ATTESTATION_SIGNER_ID`
  * AWS key id<br>

**Agent Configuration Overrides (optional)**

Agents also have configuration settings that can be optionally overridden by environment variables. If present, these variables will override values given by configuration files.

#### **All Agents**

* Agent interval:
  * `{agent}_INTERVAL`
  * The frequency at which an agent runs its loop in milliseconds

#### **Kathy**

* Chat config:
  * Recipient:
    * `KATHY_CHAT_RECIPIENT`
    * 0x-prefixed recipient address
  * Message:
    * `KATHY_CHAT_MESSAGE`
    * A message string
  * Message list:
    * `KATHY_CHAT_MESSAGES`
    * A quoted, comma separated list of message strings
  * Random messages:
    * `KATHY_CHAT_RANDOM`
    * An integer value for the number of random messages to send

#### **Processor**

* Allowed senders:
  * `PROCESSOR_ALLOWED`
  * A comma separated list of 0x-prefixed sender addresses
* Denied senders:
  * `PROCESSOR_DENIED`
  * A comma separated list of 0x-prefixed sender addresses
* Subsidized remotes:
  * `PROCESSOR_SUBSIDIZED_REMOTES`
  * A comma separated list of network names
* S3 Bucket:
  * AWS Bucket:
    * `PROCESSOR_S3_BUCKET`
    * AWS bucket id
  * AWS Region:
    * `PROCESSOR_S3_REGION`
    * AWS region id

For an example of agent configuration overrides, please see our [example overrides env file](https://github.com/nomad-xyz/rust/blob/main/fixtures/env.test-agents).

### Running Agent <a href="#running-agent" id="running-agent"></a>

AWS Keys: Note that the AWS `key_id` field can be a key id, key name, alias name, or alias ARN, as documented in the [Rusoto KMS docs](https://docs.rs/rusoto_kms/latest/rusoto_kms/struct.GetPublicKeyRequest.html#structfield.key_id). For more information on configuring AWS credentials, please refer to the [Rusoto AWS credentials usage documentation](https://github.com/rusoto/rusoto/blob/master/AWS-CREDENTIALS.md#credentials).

For more info on our different run environments and key configuration/provisioning, please refer to our [agents operations page](https://docs.nomad.xyz/developers/node-operators/agent-operations).

You can see an example .env file below:

```
# Only runs agent for Ethereum <> Moonbeam channel (production)
RUN_ENV=production
AGENT_HOME_NAME=ethereum
AGENT_REPLICA_0_NAME=moonbeam

# can provide default rpc style for all networks, or specify network specific
# network-specific values always override the default
DEFAULT_RPCSTYLE=ethereum
ETHEREUM_RPCSTYLE=ethereum
MOONBEAM_RPCSTYLE=ethereum

# provide network-specific RPC endpoints
ETHEREUM_CONNECTION_URL=https://main-light.eth.linkpool.io/
MOONBEAM_CONNECTION_URL=https://rpc.api.moonbeam.network

# we will default to local transaction signing/submission
DEFAULT_SUBMITTER_TYPE=local

# can provide tx signer as hex key (for ethereum) or aws key (for moonbeam)
# again, default tx signer is overriden by network-specifics
DEFAULT_TXSIGNER_KEY=0x1111111111111111111111111111111111111111111111111111111111111111
ETHEREUM_TXSIGNER_KEY=0x1111111111111111111111111111111111111111111111111111111111111111
MOONBEAM_TXSIGNER_ID=dummy_id

# can provide attestation signer as aws or hex key
ATTESTATION_SIGNER_ID=dummy_id
```

If you would like to configure an agent to run against all connected networks (against all replicas the home is connected to), see [this example](https://github.com/nomad-xyz/rust/blob/main/fixtures/env.test). For more examples of .env files, see our [test fixtures folder](https://github.com/nomad-xyz/rust/tree/main/fixtures).

Once you have populated a .env file, running an agent is as simple as running the following command:

`env $(cat .env | xargs) cargo run --bin <AGENT>`

This will build the codebase and run the specified `<AGENT>` binary (updater, relayer, processor, or watcher) using the provided environment variables.

### Agents Release Process <a href="#agents-release-process" id="agents-release-process"></a>

Our release process follows a monthly cadence. We follow [Semantic Versioning](https://semver.org/), where breaking changes constitute changes that break agent configuration compatibility.

We manage releases through GitHub. You can find new per-agent releases [here](https://github.com/nomad-xyz/rust/releases).

### Production Builds <a href="#production-builds" id="production-builds"></a>

When making changes to the Rust codebase, it is important to ensure the Docker build used in production environments still works. You can check this automatically in CI as it is built on every PR ([see docker workflow here](https://github.com/nomad-xyz/rust/blob/main/.github/workflows/docker.yml)), however you can check it much faster usually by attempting to build it locally.

You can build the docker image by running the following script in the `rust` directory:

`./build.sh latest`

If that goes smoothly, you can rest assured it will most likely also work in CI.

# Troubleshooting

Hints for dealing with common (and not so common) Agent failures.

## Common Errors

### ProverSync found new root but could not find leaf under it

The `eth_getLogs` RPC call is used by Agents to query for events from a given EVM-compatible blockchain. This error manifests when an Agent is unable to locate a `Dispatch` event for a given message. This sometimes manifests on some novel EVM-compatible networks non-deterministically and can be hard to debug. \
\
The error lists the current root and the leaf index of the message that was not properly indexed. \
\
A special case of this Error is when the Agent cannot locate the first leaf with index `0`. This usually indicates a deviation from the behavior of an Ethereum Geth node, which has event data indexed in a separate data structure than block data.\
\
This is generally fixed by switching your RPC to an Archive node, such that all the required data to format the response to `eth_getLogs` is available at query-time. \
\
Below is an example of an error in this special case: &#x20;

> ProverSync found new root 0x6f46…504c but could not find leaf under it. Leaf index of missing leaf: 0.

# Running a Watcher

### Overview <a href="#overview" id="overview"></a>

[Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) are a crucial component of the Nomad security model. Watchers secure applications built on Nomad by observing the updater's attestations on the home contract. In the case of any malicious or faulty attestations, the watcher will disconnect its given application from the underlying messaging channel, eliminating the impact of fraud on that app.

### Steps to Running a Watcher <a href="#steps-to-running-a-watcher" id="steps-to-running-a-watcher"></a>

#### High Level <a href="#high-level" id="high-level"></a>

1. Provision a watcher attestation key
2. Enroll the attestation key address on the desired networks \[Nomad governance]
3. Provision transaction signer key(s)
4. Fund the transaction signer address(es) on the desired networks
5. Choose RPC endpoint(s) for desired networks.
6. Setup agent monitoring
7. Place the information from steps 1-5 into the watcher's environment and run the agent

#### Details <a href="#details" id="details"></a>

**Step 1: Provision Watcher Key**

The watcher attestation key is used to sign attestations that fraud occurred. Every cross-chain app will enroll a set of watcher attestation addresses. If the app receives an attestation of fraud from an enrolled watcher, the app will disconnect from the messaging channel.

The operator must provision a key for the application to enroll. Agents accept either raw hex keys or AWS KMS keys.

**Step 2: Enroll Watcher Key**

The agent operator should forward the newly provisioned watcher address to the Nomad team. Nomad governance will then enroll the address on the desired application for the appropriate networks.

**Step 3: Provision Transaction Signer Key(s)**

In order for the watcher to submit an attestation of fraud, it must submit a transaction. The agent operator must provision one or more transaction signer keys. These can be the same across all networks or unique per-network.

**Step 4: Fund Transaction Signers**

The agent operator must fund the transaction signer address(es) on all networks. We recommend funding *each address on each chain* with the a minimum of the values documented [here](#watcher-transaction-signer-funding), according to the network. The agent should have at least the minimum amount at all times.

**Step 5: Choose RPC Endpoints**

The watcher must connect to all chains involved in the channels it watches over. We recommend using private RPC endpoints for the best reliability. This would include connecting through an internally run local node or through top-quality node providers.

**Step 6**

All Nomad agents produce logs and metrics. It is up to the agent operator how they setup the reception of this data. Agents expose Prometheus metrics at port `9090` by default. Agents output logs to stdout in JSON format, following standard [12-factor-app](https://12factor.net/logs) methodology.

**Step 7**

In order to run a watcher, you must configure the watcher's environment to receive the information from steps 1-5. See our [guide on running agents](https://docs.nomad.xyz/developers/node-operators/running-agents-guide) for more info on configuration and running the agent.

### Watcher Transaction Signer Funding <a href="#watcher-transaction-signer-funding" id="watcher-transaction-signer-funding"></a>

<table><thead><tr><th width="183.66590389016017">Chain</th><th>Funding Amount</th></tr></thead><tbody><tr><td>Ethereum</td><td>3 ETH</td></tr><tr><td>Moonbeam</td><td>5 GLMR</td></tr><tr><td>Milkomeda C1</td><td>5 milkADA</td></tr><tr><td>Evmos</td><td>5 EVMOS</td></tr><tr><td>xDai</td><td>5 xDAI</td></tr><tr><td>Avalanche</td><td>4 AVAX</td></tr><tr><td>Polygon</td><td>5 MATIC</td></tr><tr><td>Arbitrum</td><td>TBD</td></tr><tr><td>Optimism</td><td>TBD</td></tr></tbody></table>

**Reasoning for Funding Amounts**

The highest daily average gas price on Ethereum to-date is \~710 gwei. A watcher `unenrollReplica` transaction is \~120k gas while a `doubleUpdate` transaction is \~200k gas. If we 10x the highest daily average gas price, we get 7100 gwei. This means that calling `unenrollReplica` will cost 0.852 ETH and calling `doubleUpdate` will cost 1.42 ETH.

unenrollReplica: (710 x 10 x 120,000) / 1e9 = 0.852 ETH

doubleUpdate: (710 x 10 x 200,000) / 1e9 = 1.42 ETH

A minimum of 3 ETH worth of funds per watcher transaction signer is recommended. For networks outside of Ethereum, the funding amount is inflated due to the fact that the dollar cost of funds is much cheaper on other chains.

# Agent Operations

### Agent Overview <a href="#agent-overview" id="agent-overview"></a>

Agents are the off-chain component of the Nomad system, their purpose is to ferry data between the constituent `Domains` that make up the Nomad network. Agents are written in Rust and globally share the following properties:

* Agents are modeled after a [12-factor app](https://12factor.net/)
  * Deployable via a Docker container
  * Configurable via Environment Variables (or a configuration file if necessary)
  * Suitable for use in Infrastructure automation systems
* Agents funded Transaction Signers to pay for gas when sending transactions
* Agents are (optionally) deployable via the [nomad-bridge Helm Chart](https://github.com/nomad-xyz/helm-charts/tree/main/charts/nomad-bridge)

There are 4 production agent roles, with an optional additional agent that is only suitable for use in Development environments:

* **Updater**
  * The `Updater` is the most important Agent in regards to *Liveness*.
  * The `Updater` issues attestations of merkle root transitions and is bonded to disincentivize fraud.
* **Relayer**
  * Relays root transitions from home to replica(s)
* **Processor**
  * The `Processor` is entirely optional, however it implements the property of *subsidized channels*. The `Processor` polls for messages that have reached the expiration of their fraud proof window, and claims them on behalf of the user, obviating the need for the user to do so on their own or pay the required gas.
  * The `Processor` can be tuned to look for a subset of messages to process, such that it can be deployed by a particuar xApp operator who would like to subsidize transactions on behalf of the users of their xApp *exclusively*.
  * The Nomad Core Team operates processors for most Domains with execution environments that are affordable, with the main notable unsubsidized Domain being Ethereum.
* **Watcher**
  * The `Watcher` is the most importent Agent in regards to *Safety*.
  * The `Watcher` *watches* a designated Home contract and its corresponding replicas on remote domains. It keeps an internal state of root transitions, and if an improper update is detected, it proves it to the protocol -- slashing the Updater and preventing further fraudulant updates from being passed.
* **Kathy**
  * `Kathy` (aka Chatty Kathy) is a development agent which sends Nomad messages on an interval in order to test bridge channels.
  * It is not advised that you deploy `Kathy` to a production environment as it will spend your hard-earned money with no regards.

### Deployment Environments <a href="#deployment-environments" id="deployment-environments"></a>

There will exist several logical deployments of Nomad to enable us to test new code/logic before releasing it to Mainnet. Each environment encompasses the various Home/Replica contracts deployed to many blockchains, as well as the agent deployments and their associated account secrets.

The environments have various purposes and can be described as follows:

#### Development <a href="#development" id="development"></a>

Purpose: Allows us to test changes to contracts and agents. *Bugs should be found here.*

* Deployed against testnets
* Agent Accounts: HexKeys stored in a secret manager for ease of rotation/access
* Agent Infrastructure: Nomad core team will operate agent infrastructure for this.
* Node Infrastructure: Forno/Infura
* Agent Deployments: Automatic, continuous deployment
* Contract Deployments: Automatic, with human intervention required for updating the [UpgradeBeacon](https://docs.nomad.xyz/dev/upgrade-setup.html).

**Current Dev Contract Deployment:**

[Development](https://github.com/nomad-xyz/rust/tree/main/configuration/configs/development.json)

#### Staging <a href="#staging" id="staging"></a>

Purpose: Allows us to test the full-stack integration, specifically surrounding the KMS access control and federated secret management. *Issues with process should be found here.*

* Deployed against testnets, mirrors Mainnet deployment.
* Agent Accounts: KMS-provisioned keys
* Agent Infrastructure: Agent operations will be decentralized
* Node Infrastructure: Node infrastructure will be decentralized
* Agent Deployments: Determined by whoever is running the agents
* Contract Deployments: Automatic, with human intervention required for updating the [UpgradeBeacon](https://docs.nomad.xyz/dev/upgrade-setup.html).

**Current Staging Contract Deployment:**

[Staging](https://github.com/nomad-xyz/rust/tree/main/configuration/configs/staging.json)

#### Production <a href="#production" id="production"></a>

Purpose: Where the magic happens, **things should not break here.**

* Deployed against Mainnets
* Agent Accounts: KMS-provisioned keys
* Agent Infrastructure: Agent operations will be decentralized
* Node Infrastructure: Node infrastructure will be decentralized
* Agent Deployments: Determined by whoever is running the agents
* Contract Deployments: ***Manual*** - Existing tooling can be used, but deploys will be gated and require approval as contract deployments are expensive on Mainnet.

**Current Production Contract Deployment:**

[Production](https://github.com/nomad-xyz/rust/tree/main/configuration/configs/production.json)

### Key Material <a href="#key-material" id="key-material"></a>

Keys for Staging and Production environments will be stored in AWS KMS, which is a highly flexible solution in terms of granting access. It guarantees nobody will ever have access to the key material itself, while still allowing granular permissions over access to remote signing.

At the outset, the Nomad team will have full control over agent keys, and any contracted party will simply be granted access through existing IAM tooling/roles.

#### Provision KMS Keys <a href="#provision-kms-keys" id="provision-kms-keys"></a>

There exists a script in the Rust repo [`provision_kms_keys.py`](https://github.com/nomad-xyz/rust/blob/main/provision_kms_keys.py) that facilitates KMS key provisioning for agent roles.

The script will produce a single set of keys per "environment." Where an **environment** is a logical set of smart contract deployments, as documented [here](https://docs.nomad.xyz/dev/agents/agent-operations.html#deployment-environments). By default there are two environments configured, `staging` and `production`.

**Keys Explained**

**Transaction Signers**

One signer key should be provisioned for each agent per-network. These keys are used to sign transactions on the respective networks Nomad is deployed to.

**Attestation Signers**

One additional key is provisioned for both the Watcher and Updater Agents. The Updater uses its key to sign updates to its assigned Home contract, while the Watcher uses its key to sign fraud proofs when it observes the Updater commiting fraud.

Note: Attestation signer addresses are used as input to the contract deployment process. They can be configured in the `nomad-deploy` package [like so](https://github.com/nomad-xyz/nomad-monorepo/blob/main/typescript/nomad-deploy/config/testnets/kovan.ts#L28-L30).

You may configure the script to generate arbitrary signer keys on a per-environment basis.

```
# Agent Keys
agent_keys = {
    "staging": [
        "watcher-signer",
        "watcher-attestation",
        "updater-signer",
        "updater-attestation",
        "processor-signer",
        "relayer-signer",
        "kathy-signer"
    ],
    "production": [
        "watcher-signer",
        "watcher-attestation",
        "updater-signer",
        "updater-attestation",
        "processor-signer",
        "relayer-signer",
    ]
}
```

Additionally, the supported networks for each environment are configured below.

```
networks = {
    "production": [
        "ethereum",
        "moonbeam",
        "evmos"
    ],
    "staging": [
        "moonbasealpha",
        "kovan"
    ]
}
```

**Run the Key Provisioning Script**

```
AWS_ACCESS_KEY_ID=accesskey AWS_SECRET_ACCESS_KEY=secretkey python3 provision_kms_keys.py
```

If the required keys are not present, the script will generate them. If they keys *are* present, their information will be fetched and displayed non-destructively.

Upon successful operation, the script will output a table of the required keys, their ARNs, ETH addresses (for funding the accounts), and their regions.

**Provision IAM Policies and Users**

This is an opinionated setup that works for most general agent operations use-cases. The same permissions boundaries can be achieved through different means, like using only [Key Policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html).

Background Reading/Documentation:

* [KMS Policy Conditions](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.htm)
* [KMS Policy Examples](https://docs.aws.amazon.com/kms/latest/developerguide/customer-managed-policies.html)
* [CMK Alias Authorization](https://docs.aws.amazon.com/kms/latest/developerguide/alias-authorization.html)

The following sequence describes how to set up IAM policies staging and production deployments.

* Create two users
  * nomad-signer-staging
  * nomad-signer-production
  * kms-admin
  * Save IAM credential CSV
* Create staging signer policies

  * staging-processor-signer
  * staging-relayer-signer
  * staging-updater-signer
  * staging-watcher-signer
  * With the following policy, modified appropriately:

  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "NomadStagingPolicy",
        "Effect": "Allow",
        "Action": ["kms:GetPublicKey", "kms:Sign"],
        "Resource": "arn:aws:kms:*:11111111111:key/*",
        "Condition": {
          "ForAnyValue:StringLike": {
            "kms:ResourceAliases": "alias/staging-processor*"
          }
        }
      }
    ]
  }
  ```

  * production-processor-signer
  * production-relayer-signer
  * production-updater-signer
  * production-watcher-signer
  * With the following policy, modified appropriately:

  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "NomadProductionPolicy",
        "Effect": "Allow",
        "Action": ["kms:GetPublicKey", "kms:Sign"],
        "Resource": "arn:aws:kms:*:11111111111:key/*",
        "Condition": {
          "ForAnyValue:StringLike": {
            "kms:ResourceAliases": "alias/production-processor*"
          }
        }
      }
    ]
  }
  ```

* Create kms-admin policy

  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "KMSAdminPolicy",
        "Effect": "Allow",
        "Action": [
          "kms:DescribeCustomKeyStores",
          "kms:ListKeys",
          "kms:DeleteCustomKeyStore",
          "kms:GenerateRandom",
          "kms:UpdateCustomKeyStore",
          "kms:ListAliases",
          "kms:DisconnectCustomKeyStore",
          "kms:CreateKey",
          "kms:ConnectCustomKeyStore",
          "kms:CreateCustomKeyStore"
        ],
        "Resource": "*"
      },
      {
        "Sid": "VisualEditor1",
        "Effect": "Allow",
        "Action": "kms:*",
        "Resource": [
          "arn:aws:kms:*:756467427867:alias/*",
          "arn:aws:kms:*:756467427867:key/*"
        ]
      }
    ]
  }
  ```

  * Create IAM groups
    * staging-signer
    * production-signer
    * kms-admin
  * Add previously created users to the corresponding groups
    * nomad-signer-staging -> staging-signer
    * nomad-signer-production -> production-signer
    * kms-admin -> kms-admin

### Funding Addresses <a href="#funding-addresses" id="funding-addresses"></a>

Each agent should be configured with a unique wallet to be used to signing transactions and paying gas. In order to automate the process of monitoring and topping up agent wallets, the Nomad core team built a CLI tool called [The Keymaster](https://docs.nomad.xyz/dev/agents/the-keymaster.html).

The Keymaster, upon configuration, enables the manual one-off topping up of agent wallets on an arbitrary number of netorks. Additionally, it is capable of running this functionality as a service, topping up accounts on an interval and exposing prometheus metrics about the addresses it is monitoring for use in dashboards.

### Self-Service Proofs in S3 <a href="#self-service-proofs-in-s3" id="self-service-proofs-in-s3"></a>

In order to facilitate users processing their own proofs in the GUI, agents (specifically the Processor), have the functionality to upload raw proofs to an AWS S3 bucket. In the default configuration, the bucket is publicly accessible and allows end-users to fetch them via the GUI and submit them in a transaction to the apropriate blockchain.

#### Pre-Requisites <a href="#pre-requisites" id="pre-requisites"></a>

* AWS Account
* Agent Infrastructure

#### Bucket Setup <a href="#bucket-setup" id="bucket-setup"></a>

Setup is simple, create a bucket in your desired region via the AWS UI, ensuring to uncheck "Block Public Access" as the desired outcome is for the contents of this bucket to be publicly accessible on the internet.

Use the following bucket policy to enable public access to `s3:getObject` in your newly created bucket:

```
{
    "Version": "2012-10-17",
    "Id": "S3PublicRead",
    "Statement": [
        {
            "Sid": "IPAllow",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:getObject",
            "Resource": "arn:aws:s3:::<BUCKET-NAME>/*"
        }
    ]
}
```

#### AWS IAM Permissions <a href="#aws-iam-permissions" id="aws-iam-permissions"></a>

NOTE: Currently, Agents only support a single AWS key for both KMS Signing and S3 Upload. This enforces a non-functional requirement that the S3 bucket proofs are uploaded to and the KMS keys used to sign transactions are in the same logical AWS account.

Create an IAM policy that allows a user to write to the S3 bucket you created in the previous step:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ListObjectsInBucket",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<BUCKET-NAME>"
            ]
        },
        {
            "Sid": "AllObjectActions",
            "Effect": "Allow",
            "Action": "s3:*Object*",
            "Resource": [
                "arn:aws:s3:::<BUCKET-NAME>/*"
            ]
        }
    ]
}
```

Attach this policy to an IAM user and provision/download AWS keys.

#### Configuring the Agent <a href="#configuring-the-agent" id="configuring-the-agent"></a>

The Processor agent has special config for S3 proof indexing, located in the code [here](https://github.com/nomad-xyz/nomad-monorepo-archive/blob/main/rust/agents/processor/src/settings.rs#L9-L24).

Buckets can be configured at agent runtime via the following environment variables:

`OPT_PROCESSOR_S3_BUCKET` -> Name of the bucket. Ex. `nomadxyz-development-proofsOPT_PROCESSOR_S3_REGION` -> AWS region the bucket lives in. Ex. `us-west-1`

If you are using the helm chart, these values can be passed via [`values.yaml`](https://github.com/nomad-xyz/nomad-monorepo/blob/main/rust/helm/nomad-agent/values.yaml#L147-L149) like so:

```
processor:
...
  s3Proofs:
    bucket: nomadxyz-development-proofs
    region: us-west-1
```

# Agent Gas Values

### Context <a href="#context" id="context"></a>

Gas estimation is hard. `eth_estimateGas` calls have historically caused our agents many issues across different RPC providers and networks. Given that we now have a reasonable dataset on how much gas is needed for different contract methods, we are moving to custom-coding our gas limits using estimates from previous gas usage data.

### Standard EVM <a href="#standard-evm" id="standard-evm"></a>

#### Home <a href="#home" id="home"></a>

Update:

* Take average limit for one message (50k) and double base to 100k
* Each additional message dequeued is \~5k gas so double that cost to 10k per message
* `100k + (num_messages * 10k)`

Improper Update:

* Subset of `update` gas (`update` calls `improperUpdate`)
* Using same estimation as `update`
* `100k + (num_messages * 10k)`

DoubleUpdate:

* Signature check is \~`50k`
* Double that for two signature checks in double update `100k`
* Double total for safety to `200k`

#### Replica <a href="#replica" id="replica"></a>

Update:

* `70k` on average
* Double that to `140k` (constant)

Prove:

* `100k` on average
* Double that to `200k` (constant since merkle proofs always same size)

Process:

* Minimum `850k` required
* Double minimum to `1.7M`

ProveAndProcess:

* `1.7M` for process
* `200k` for prove
* `1.9M` total

DoubleUpdate:

* Signature check is \~`50k`
* Double that for two signature checks in double update `100k`
* Double total for safety to `200k`

#### XAppConnectionManager <a href="#xappconnectionmanager" id="xappconnectionmanager"></a>

UnenrollReplica:

* `60k` average
* Double that to `120k`

OwnerUnenrollReplica:

* Cheaper version of normal `unenrollReplica` without signature check
* Use same estimate of `120k`

# The Keymaster

[*I am Vinz, Vinz Clortho, Keymaster of Gozer...Volguus Zildrohoar, Lord of the Seboullia. Are you the Gatekeeper?*](https://www.youtube.com/watch?v=xSp5QwKRwqM)

![Keymaster from Ghostbusters](https://i.pinimg.com/originals/9d/5b/a0/9d5ba02875ce7921d092038d1543b1f4.jpg)

### Summary <a href="#summary" id="summary"></a>

The Keymaster is a tool that is used to manage funds for Nomad Agent Wallets. Due to the sheer number of networks Nomad supports, and the necessity for having a unique set of keys for each home, managing funds and ensuring agents can continue to function quickly becomes difficult as the network of Nomad channels grows.

Example:

For 4 homes (alfajores, kovan, rinkeby, rinkarby) with 5 addresses each (kathy, watcher, updater, processor, relayer), this means there will be 20 unique addresses and each address has to be funded on each network resulting in 20 \* 4 = 80 unique accounts across all networks which must be funded and topped up regularly.

Generalized: num\_homes^2 \* num\_addresses

The Keymaster stores metadata about addresses, sources of funds, network RPC endpoints, and more to facilitate solving this problem.

### Using The Keymaster <a href="#using-the-keymaster" id="using-the-keymaster"></a>

Note: Before you do *anything*, [call the Ghostbusters](https://www.youtube.com/watch?v=Fe93CLbHjxQ).

The Keymaster is a simple Python-based CLI program, the entrypoint is `keymaster.py`

Install the requirements via pip:

`pip3 install -r requirements.txt`

The Keymaster can be invoked via `python3` like so:

```
$ python3 keymaster.py --help
Usage: keymaster.py [OPTIONS] COMMAND [ARGS]...

Options:
  --debug / --no-debug
  --config-path TEXT
  --help                Show this message and exit.

Commands:
  top-up
```

Subcommands can be invoked by passing them as arguments to the CLI:

```
$ python3 keymaster.py top-up --help
Usage: keymaster.py top-up [OPTIONS]

Options:
  --help  Show this message and exit.
```

### Configuration File <a href="#configuration-file" id="configuration-file"></a>

The Keymaster relies on a JSON configuration file, by default located at `./keymaster.json`. You can pass a new path to the file using the `--config-path` argument.

An example can be found at `./keymaster-example.json` and its contents are repeated here for convenience:

```
{
    "networks": {
        "alfajores": {
            "endpoint": "https://alfajores-forno.celo-testnet.org",
            "bank": {
                "signer": "<hexKey>",
                "address": "<address>"
            },
            "threshold": 500000000000000000
        },
        "kovan": {
            "endpoint": "<RPCEndpoint>",
            "bank": {
                "signer": "<hexKey>",
                "address": "<address>"
            },
            "threshold": 500000000000000000
        }
    },
    "homes": {
        "alfajores": {
            "replicas": ["kovan"],
            "addresses": {
                "kathy": "<address>",
                "watcher": "<address>",
                "updater": "<address>",
                "relayer": "<address>",
                "processor": "<address>"
            }
        },
        "kovan": {
            "replicas": ["alfajores"],
            "addresses": {
                "kathy": "<address>",
                "watcher": "<address>",
                "updater": "<address>",
                "relayer": "<address>",
                "processor": "<address>"
            }
        }
    }
}
```

In the `top-up` command, The Keymaster will load the contents of this file and use it to dynamically query the configured accounts and determine if they need to be topped up.

# Core Developers

# Upgrade Setup

We will use the `UpgradeBeacon` pattern to implement three upgradable contract types: `Home`, `Replica`, and `GovernanceRouter`.

Each upgradable contract will have:

* **Proxy**
  * the permanent address of the contract that external entities interact with
  * holds the storage of the contract
  * uses the logic specified by `Implementation`
  * uses `delegatecall` to forward contract calls from `Proxy` → `UpgradeBeacon` → `Implementation`
* **UpgradeBeacon**
  * stores the (mutable) address of the `Implementation`
  * forwards `delegatecalls` to the `Implementation`
  * accepts new `Implementation` addresses from its `Controller` (thereby performing upgrades for all `Proxies`)
* **Implementation**
  * specifies the logic of the contract
  * code is the same as a normal, non-upgradable contract implementation (though it should use upgrade-safe storage)

Each of the three `UpgradeBeacon` contracts will share a the same `Controller` — the contract with the power to perform upgrades.

The **Controller** contract will have two roles: controller and saver.

* `controller`
  * is a transferrable role that should be performing upgrades in almost every case.
  * will be set to the `GovernanceRouter Proxy`, so that the Governance xApp ultimately controls the upgrades of the entire system. Note that this creates a circular dependency which makes upgrades of the `GovernanceRouter Implementation` particularly sensitive.
* `saver`
  * is a transferrable(?) role that is responsible for recovering the system in a catastrophic failure case. Actions performed by the `saver` will be subject to a timelock enforced by the Controller contract.
  * will be set to a multisig contract where the signatories are a set of known / trusted community members. the signatories for the `saver` multisig be the same on every chain

### Diagrams[#](https://docs.nomad.xyz/dev/upgrade-setup.html#diagrams) <a href="#diagrams" id="diagrams"></a>

![Upgrade Setup Diagram 1](https://docs.nomad.xyz/Upgrade-Setup-1.png)

![Upgrade Setup Diagram 2](https://docs.nomad.xyz/Upgrade-Setup-2.png)

# Deploying Contracts

# Development

TODO: update links from old monorepo

## Deploying Dev Setup <a href="#deploying-dev-setup" id="deploying-dev-setup"></a>

This section goes through the steps of adding a new development network to `nomad-deploy` and deploying a new set of dev contracts. If you will not be adding a new network, please skip to [Deploying the Contracts to Dev](#deploying-the-contracts-to-dev). If you are looking to deploy a new network to the production setup, please refer to the separate page on deploying new contracts to production.

### Add a New Network Config <a href="#add-a-new-network-config" id="add-a-new-network-config"></a>

If you are looking to add a new network to your dev setup, you will need to create a new config file for that network in `typescript/nomad-deploy/config/testnets`.

1. Copy the contents of one of the existing network's files into a new file titled `<new_network_name>.ts`.
2. Rename the `process.env` variables (deployer key and RPC URL) such that they pull from the `.env` variables for your new network.
3. Set the `chainJson` fields appropriately. For dev, this usually just means updating the following fields: `name`, `domain`, `timelag`.
4. Set the `devConfig` and `stagingConfig` object fields appropriately. In practice, for dev, you leave `devConfig` the same and only update `stagingConfig.optimisticSeconds`.

### Writing a New Deploy Script <a href="#writing-a-new-deploy-script" id="writing-a-new-deploy-script"></a>

Now that you've added a new network config, you must write a new deploy script that includes your new network.

1. Duplicate the contents of an existing folder in `typescript/nomad-deploy/scripts` (`core.ts` and `bridge.ts`) and put them in a new folder for your new deploy script.
2. In `core.ts` and `bridge.ts` adjust any import paths to pull in your new network config from `typescript/nomad-deploy/config/testnets`.
3. Add or remove any other existing networks in `core.ts` and `bridge.ts` and ensure that the `CoreDeploy` objects for the desired networks are used in the `deployTwoChains` or `deployNChains` calls at the bottom of the files.
4. Add new npm scripts to `typescript/nomad-deploy/package.json` that execute your new `core.ts` and `bridge.ts` files. The scripts will look like the following:

```
"scripts": {
    ...
    "deploy-<script_folder_name>-core": npx ts-node scripts/<script_folder_name>/core.ts,
    "deploy-<script_folder_name>-bridge": npx ts-node scripts/<script_folder_name>/bridge.ts
    ...
}
```

### Deploying the Contracts to Dev <a href="#deploying-the-contracts-to-dev" id="deploying-the-contracts-to-dev"></a>

The following section walks through the steps for deploying a new set of contracts to dev.

1. Clone the monorepo and take a look at [nomad-deploy](https://github.com/nomad-xyz/nomad-monorepo/tree/main/typescript/nomad-deploy).
2. Populate `.env.example` with the required RPC endpoints and funded deployer keys -- place it at `typescript/nomad-deploy/.env`, [see the example](https://github.com/nomad-xyz/nomad-monorepo/blob/main/typescript/nomad-deploy/.env.example)
3. Prepare Local Dependencies

`nomad-deploy` is configured to use the local versions of the Nomad typechain interface and the Nomad SDK, as such the local Node modules must be initialized.

```
# Install dependencies for typechain
$ cd typescript/typechain
$ npm i

...

# Install dependencies for nomad-sdk
$ cd typescript/nomad-sdk
$ npm i
```

1. Install Dependencies

```
$ cd typescript/nomad-deploy
$ npm i
# Links local modules to nomad-deploy
$ npm run relink-all
```

1. Execute a Deploy Script

Note: See below for more details about the available deployment scripts.

```
# Deploy core contracts first
$ npm run deploy-<your_script_folder_name>-core

# Then deploy bridge contracts
$ npm run deploy-<your_script_folder_name>-bridge
```

1. Commit Outputted Configs

If all goes according to plan, you will have a new folder at `rust/config/<timestamp>` containing JSON files that are used by the Off-Chain Agents. Please rename this folder appropriately (`development` if this will become the new dev setup). When committed to the monorepo, the config files are automatically bundled into the resultant Agent docker image in CI.

Note: Deployment environments may be overridden by replacing the environment's config folder with the contents of your new timestamped configuration.

### Updating Nomad SDK Dev Addresses <a href="#updating-nomad-sdk-dev-addresses" id="updating-nomad-sdk-dev-addresses"></a>

If your newly deployed setup will become the new dev setup, you will need to adjust the hardcoded domains, indexing parameters, and addresses in the Nomad SDK. Go to `typescript/nomad-sdk/src/nomad/domains/dev.ts`. For each `NomadDomain` object:

1. Update the indexing parameters (`blocks` and `from`) with the `chunk` and `from` fields from `rust/config/development/<network>_config.json`.
2. Replace all addresses with those in the the newly outputted config file `rust/config/development/<network>_contracts.json`. For the home and replica addresses, use the *proxy* addresses.
3. If you deployed a new network that has not been seen before, add a new `NomadDomain` object and fill it with the correct fields.

<br>

# Production

## Incrementally Deploying New Networks <a href="#incrementally-deploy-new-network-to-production-setup" id="incrementally-deploy-new-network-to-production-setup"></a>

TODO

# Audits

### Primary Audit

Nomad was audited by Quantstamp in June 2022. The audit covers the following packages:

* [Nomad Core Contracts](https://github.com/nomad-xyz/monorepo/tree/main/packages/contracts-core)
* [Nomad Token Bridge Contracts](https://github.com/nomad-xyz/monorepo/tree/main/packages/contracts-bridge)
* [Nomad Router Contracts](https://github.com/nomad-xyz/monorepo/tree/main/packages/contracts-router)
* [Gnosis Zodiac Nomad Module Contracts](https://github.com/gnosis/zodiac-module-nomad)

You can find the full audit here: <https://certificate.quantstamp.com/full/nomad>

{% embed url="<https://certificate.quantstamp.com/full/nomad>" %}

### Secondary Audit

The [Zodiac Nomad Module](https://github.com/gnosis/zodiac-module-nomad) was also audited by the G0 Group in May 2022.&#x20;

You can find the audit here: <https://github.com/gnosis/zodiac-module-nomad/blob/audit/audits/ZodiacGnomadModuleMay2022.pdf>

# Bug Bounty

Nomad has partnered with Immunefi to offer a bug bounty for any vulnerabilities found in Nomad smart contracts. You can visit the bug bounty page here: <https://immunefi.com/bounty/nomad/>

The payouts are tiers are:

* Critical Level: Up to USD $1,000,000
* High Level: USD $100,000

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.1](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-1/).

# Governance

Nomad smart contracts are upgradable and are currently governed by a multi-sig address deployed as a Gnosis Safe contract on Ethereum Mainnet.

### Governor

**Details:** [Etherscan](https://etherscan.io/address/0x93277b8f5939975b9e6694d5fd2837143afbf68a), [Gnosis Safe](https://gnosis-safe.io/app/eth:0x93277b8f5939975b9E6694d5Fd2837143afBf68A/settings/owners)

**Policy:** 3 of 5 - of the five total signers, three signatures are required to execute a transaction

**Signers:**

* [Layne Haber](https://twitter.com/LayneHaber): `0xC69b66cc2811B509829448FBFfb2553c4CBb627e`
* [Praneeth Srikanti](https://twitter.com/bees_neeth): `0x9bdD76b2a69Db43Fa695a10f5977b8FD891225f3`
* [Katherine Wu](https://twitter.com/katherineykwu): `0x83865712c50f702fA4650C7fadEd90A54242046e`
* [Pranay Mohan](https://twitter.com/pranaymohan): `0xab0614cE8d53ea2c67B87f8ad4d8Fac7A4a516e5`
* [Anna Carroll](https://twitter.com/annascarroll): `0x25270d2e6980C5b343C4866Aea904a9A9bCA733F`

### Recovery Manager

#### Moonbeam Recovery Manager <a href="#moonbeam-recovery-manager" id="moonbeam-recovery-manager"></a>

**Details:** [Moonscan](https://moonbeam.moonscan.io/address/0x2D23B3865D5B7CD88Ce9CE7514a13545672d9eF7), [Gnosis Safe](https://multisig.moonbeam.network/mbeam:0x2D23B3865D5B7CD88Ce9CE7514a13545672d9eF7/settings/owners)

**Policy:** 3 of 5 - of the five total signers, three signatures are required to execute a transaction

**Signers:**

* [Barbara Liau](https://twitter.com/barbaraliau): `0xDE9cfb1216889Dee0cAB8afB04c63911427659E4`
* [Conner Swann](https://twitter.com/YourBuddyConner): `0xea24Ac04DEFb338CA8595C3750E20166F3b4998A`
* [Alberto Viera](https://twitter.com/theAlbertoV19): `0x4E8ee1AEFEf37c431c6B68F1F5fE6e309ba44376`
* [Arthur Kaseman](https://www.purestake.com/about/): `0x9A23197B7d8bA57E8fe62c3047003C8854F688Cc`
* [Aaron Evans](https://www.linkedin.com/in/aaron-evans-a2366/): `0x3DfED02fEFDDA06A80E21f35097fb910a4a790ef`

# Contracts

## Contract Addresses

Contracts are deployed and verified.

All details can be found in [the config repo](https://github.com/nomad-xyz/config).

* [Ethereum](#ethereum)
* [Moonbeam](#moonbeam)
* [Evmos](#evmos)
* [Milkomeda C1](#milkomeda-c1)
* [Gnosis Chain](#gnosis-chain)
* [Avalanche](#avalanche)

### Ethereum

#### Core Contracts

```
"ethereum": {
      "deployHeight": 13983724,
      "governanceRouter": {
        "beacon": "0x67833a48b3f509d4252ac2c19cd604556ed6c981",
        "implementation": "0x569d80f7fc17316b4c83f072b92ef37b72819de0",
        "proxy": "0x3009c99d370b780304d2098196f1ebf779a4777a"
      },
      "home": {
        "beacon": "0x063e871f8db991cead34b557a00b157b360084cc",
        "implementation": "0x8f184d6aa1977fd2f9d9024317d0ea5cf5815b6f",
        "proxy": "0x92d3404a7e6c91455bbd81475cd9fad96acff4c8"
      },
      "replicas": {
        "avalanche": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0x5d94309e5a0090b165fa4181519701637b6daeba"
        },
        "evmos": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0x5bae47bf29f4e9b1e275c0b427b84c4daa30033a"
        },
        "milkomedaC1": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0xef989866b66a491e7b6c7473d73b589450d0f766"
        },
        "moonbeam": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0x049b51e531fd8f90da6d92ea83dc4125002f20ef"
        },
        "xdai": {
          "beacon": "0x0876dfe4acae0e1c0a43302716483f5752298b71",
          "implementation": "0x7f58bb8311db968ab110889f2dfa04ab7e8e831b",
          "proxy": "0x0a627a6398f429b62969cd475fb5ba8e04a4eb70"
        }
      },
      "updaterManager": "0x9272c9d5fa902ef3804ec81e0333ae420d57f715",
      "upgradeBeaconController": "0xdb378579c2af11817eea21474a39f95b5b9dfd7e",
      "xAppConnectionManager": "0xfe8874778f946ac2990a29eba3cfd50760593b2f"
    },
```

#### Token Bridge Contracts

```
"ethereum": {
  "bridgeRouter": {
    "beacon": "0xb70588b1a51f847d13158ff18e9cac861df5fb00",
    "implementation": "0xd3dfd3ede74e0dcebc1aa685e151332857efce2d",
    "proxy": "0x88a69b4e698a4b090df6cf5bd7b2d47325ad30a3"
  },
  "bridgeToken": {
    "beacon": "0x8ca56e6235d83ff2f4e779f0b35a6c856d5a2fb2",
    "implementation": "0x4ad6444b55729f657a71a82a5448f85ac8aa47ba",
    "proxy": "0x9f7ea856ba1fb88d35e000c45e75f134a756ac4f"
  },
  "customs": [],
  "deployHeight": 13983724,
  "ethHelper": "0x2d6775c1673d4ce55e1f827a0d53e62c43d1f304",
  "tokenRegistry": {
    "beacon": "0x4d5ff8a01ed833e11aba43821d2881a5f2911f98",
    "implementation": "0xa7e4fea3c1468d6c1a3a77e21e6e43daed855c1b",
    "proxy": "0x0a6f564c5c9bebd66f1595f1b51d1f3de6ef3b79"
  }
```

### Moonbeam

### Evmos

### Milkomeda C1

### Gnosis Chain

### Avalanche

# Agent Operations

Agents are currently operated by the Nomad core team.

More information around agent keys and operations will be added soon.

To run a Nomad watcher, [please read more here](https://docs.nomad.xyz/developers/node-operators/running-a-watcher).

# Awesome Interoperability

Inspired by the [Awesome Lists](https://github.com/sindresorhus/awesome) on various subjects, we created a the [Awesome Interop repo](https://github.com/nomad-xyz/awesome-interop) that contains the best resources on interoperability and bridging that we've found:

{% embed url="<https://github.com/nomad-xyz/awesome-interop>" %}

You can find some of these links for convenience below as well:

#### Primers

* [Blockchain Bridges: Building Networks of Cryptonetworks](https://medium.com/1kxnetwork/blockchain-bridges-5db6afac44f8) by Dmitriy Berenzon
* [CSCON\[0\] Breaking Down Bridges](https://www.youtube.com/watch?v=b0mC-ZqN8Oo) by James Prestwich
* [Ethereum Bridges Documentation](https://ethereum.org/en/developers/docs/bridges/) by Corwin Smith

#### Advanced Primers

* [SoK: Communication Across Distributed Ledgers](https://eprint.iacr.org/2019/1128) by Zamyatin et al
* [Cross-app Communication Panel](https://youtube.com/watch?v=EYzYAokCVgM) featuring Illia Polosukhin, Justin Drake, Christopher Goes, Alistair Stewart, and moderated by James Prestwich

#### Security and Trust

* [The Interoperability Trilemma](https://blog.connext.network/the-interoperability-trilemma-657c2cf69f17) by Arjun Bhuptani
* [With Bridges, Trust is a Spectrum](https://blog.li.fi/li-fi-with-bridges-trust-is-a-spectrum-354cd5a1a6d8) by Arjun Chand
* [Clusters: how trusted & trust-minimized bridges shape the multi-chain landscape](https://blog.celestia.org/clusters/) by Mustafa Al-Bassam
* [Burning Bridges: The Pitfalls of Multisig Bridges](https://www.youtube.com/watch?v=0L9G1zKjpqA) featuring Arjun Bhuptani, Conner Swann, Daniel Goldman, Pranay Mohan

#### Optimistic Interoperability

* [Optimistic Bridges: A New Paradigm for Crosschain Communication](https://blog.connext.network/optimistic-bridges-fb800dc7b0e0) by Arjun Bhuptani
* [The Zero Knowledge Podcast: Designing Optimistic Interoperability with Nomad](https://www.youtube.com/watch?v=jBGVy2uVy2U) featuring Anna Carroll, James Prestwich

#### Zero Knowledge Interoperability

* [Zero-Knowledge Proofs in Cross-Chain Communication](https://www.youtube.com/watch?v=6HftDh9mk-8) by James Prestwich

#### Cross-Domain MEV

* [Unity is Strength: A Formalization of Cross-Domain Maximal Extractable Value](https://arxiv.org/abs/2112.01472) by Obadia et al
* [Overcommitted: MEV in Message Passing](https://www.youtube.com/watch?v=jCKumKWtYVQ) by James Prestwich
* [MEV at the liquidity layer of bridges](https://www.youtube.com/watch?v=F_zi9oToHtU) by Arjun Bhuptani
* [The multichain world is centralized 🙁 - studying cross-domain MEV](https://www.youtube.com/watch?v=dv5-Lzntv5M) by Alex Obadia

# Brand Kit

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F8sXvUjiuBODxR0EpOYD9%2FNomad-Black-medium%20\(1\).svg?alt=media\&token=cc3d7b94-f663-4807-9f03-807676a4fa8e) ![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FA71Y8kLnuuL62K7YFtWn%2FNomad-White-inverted-medium%20\(1\).svg?alt=media\&token=94e46f3f-2bad-45f4-bb86-d9aee81823b3)

[Download the Nomad Brand Kit](https://old-docs.nomad.xyz/nomad-brand-assets.zip)

# FAQ

### General <a href="#general" id="general"></a>

#### What is Nomad's security model? How does it compare to other well-known models, such as header verification? <a href="#what-is-nomad-s-security-model-how-does-it-compare-to-other-well-known-models-such-as-header-verific" id="what-is-nomad-s-security-model-how-does-it-compare-to-other-well-known-models-such-as-header-verific"></a>

Every cross-chain message passing system is going to have [trade-offs](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/comparing-mechanisms), and we've carefully considered how security is affected with design choices. Nomad adopts an [optimistic mechanism](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification) inspired by optimistic roll-ups like Optimism and Arbitrum, which is a different approach than block header verification, or [native verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/native-verification). Check out the section on [verification mechanisms](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms) to read more about the various designs and their trade-offs.

#### Wen token? <a href="#wen-token" id="wen-token"></a>

Nomad does not have a token at this time. If you hear any references to a Nomad token, they are definitely scams.

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
