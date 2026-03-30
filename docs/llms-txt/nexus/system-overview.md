# Source: https://docs.nexus.xyz/network/overview/system-overview.md

# System Overview

## System Overview

Nexus is a Layer 1 blockchain that integrates high-performance execution, deterministic consensus, and verifiable computation into a unified protocol architecture.&#x20;

The system will be structured as a three-layer model (Execution, Consensus, and Verification) which cleanly separates runtime computation from block production and long-term trust minimization.

### Three-Layer Architecture

#### Execution Layer

The execution layer will consist of two parallel state machines:

* **NexusEVM** — an Ethereum-compatible environment for general-purpose smart contracts, and composable application development.
* **NexusCore** — a high-performance runtime hosting *enshrined co-processors*, each implemented as an independent, deterministic state machine optimized for specialized financial operations.

Both environments will execute concurrently and communicate via atomic cross-domain message passing, ensuring a single, globally consistent execution state across **NexusEVM, NexusCore** and **Cross-Domain** states. &#x20;

This dual-execution model will resolve the programmability–performance trade-off by allowing developers to retain full EVM flexibility while leveraging CEX-grade computational paths for latency-sensitive logic.

#### Consensus Layer

The **NexusBFT** protocol will finalize blocks, validates execution commitments, and governs the activation and evolution of co-processors.&#x20;

Each block will contain:

* A Merkle commitment to the execution state
* Validator signatures and metadata
* Optional registry updates that modify the set of active co-processors via **CPregistry**

Nexus will enable protocol-level extensibility without hard forks or execution-layer disruption, by placing co-processor registration and lifecycle management in the consensus layer.

#### Verification Layer

The verification layer will provide trustless validation of the entire chain through the **Nexus zkVM**, a zero-knowledge virtual machine.&#x20;

The **Nexus Network** will generate these proofs, progressively compressing chain execution into a single recursive Universal Proof. This architecture enables horizontally scalable validation where even low-resource devices can independently verify the chain.

### Design Goals

The system is engineered to achieve:

* **High-frequency execution:** Sub-100 ms Core latency and sub-second EVM confirmation.
* **Composable programmability:** Seamless integration between general smart contracts and specialized co-processors.
* **Deterministic coordination:** Predictable block timing and atomic cross-domain operations.
* **Progressive verifiability:** zkVM integration enables recursive proof aggregation for full-chain validation.
* **Scalable decentralization:** Performance scales with hardware and validator participation, not fragmentation across rollups.

### Summary

Nexus will unify execution, consensus, and verifiable computation into a single architecture capable of delivering high-performance financial computation with mathematically provable correctness. By embedding verifiability directly at the base layer and enabling deterministic, parallel execution through co-processors, Nexus will provide a foundation for globally scalable applications, markets, and autonomous agents
