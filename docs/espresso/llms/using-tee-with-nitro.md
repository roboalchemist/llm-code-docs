# Source: https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/nitro/using-tee-with-nitro.md

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
