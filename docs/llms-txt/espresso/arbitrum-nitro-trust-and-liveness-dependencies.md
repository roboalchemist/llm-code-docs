# Source: https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/nitro/arbitrum-nitro-trust-and-liveness-dependencies.md

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
