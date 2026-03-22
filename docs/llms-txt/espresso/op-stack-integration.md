# Source: https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release/op-stack-integration.md

# Source: https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/op-stack-integration.md

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
