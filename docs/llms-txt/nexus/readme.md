# Source: https://docs.nexus.xyz/introduction/readme.md

# Introduction

Nexus will be a high-performance Exchange Layer 1 blockchain purpose-built for verifiable finance. Our vision is to create a decentralized Internet Exchange — a global, Layer 1 platform where every asset, market, and stream of information is instantly tradable with extreme performance and low latency, powered by a foundation of high-performance verifiable computation based on zero-knowledge proofs. We believe finance is the most important application of verifiable computation, forming the foundation for a new programmable economy.

Nexus targets the $1T+ in daily exchange TradFi volume market across global spot, perps, derivatives, options, RWAs, treasuries, FX, and prediction markets, bringing programmable and composable exchange markets to the Internet’s financial layer.

#### Technical Overview

Nexus presents a high-performance Layer 1 blockchain optimized from first principles for verifiable, high-throughput and low-latency exchange computation.&#x20;

The Nexus Layer 1 will introduce a custom parallelized co-processor architecture that will extend the NexusEVM with **NexusCore**: a bundle of high-performance, exchange-optimized computational engines enshrined directly at the protocol level.

These native co-processors will provide developers with:

* High-throughput matching engines
* Real-time price oracles and data feeds
* Automated liquidation systems
* Other specialized financial primitives

This design will enable the permissionless deployment of high-performance Internet markets (perpetual futures, options, prediction markets, etc.) with CEX-level throughput and latency.

Additionally, Nexus co-processors will expose CEX-like APIs directly at the L1 node level, allowing high-frequency trading strategies to be migrated onchain with minimal changes.

**Co-Designed for Performance and Verifiability**

* NexusBFT consensus will deliver sub-second block times with deterministic (instant) finality.
* The parallelized NexusEVM + NexusCore execution environment will run independent orderbook engines concurrently, eliminating head-of-line blocking.
* Every order, cancel, trade, settlement, and liquidation will be executed and verified fully onchain and transparently.

**Long-term Scalability via Verifiable Computation**

At the core of the system will be the Nexus zkVM – a high-performance zero-knowledge virtual machine designed to horizontally scale the network through distributed proof generation.

The Nexus zkVM:

* Is already deployed and running on millions of devices through the Nexus Network distributed prover network
* Is currently experimental but production-ready for select workloads
* Will enable millions of devices to collaboratively validate financial computations, pushing Nexus toward Internet-scale throughput while preserving full cryptographic verifiability

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2Fjl37gd9UBVVuoAvlDqTX%2F1.png?alt=media&#x26;token=cb94c17f-38d0-418a-928a-3c2327cc638b" alt=""><figcaption><p>The Nexus blockchain consists of two parallel state-machines, NexusEVM and NexusCore, <br>and a three-layer architecture, featuring Execution, Verification and Consensus.<br><br>*Stack-based visualization, showing NexusEVM and NexusCore as two parallel state-machines.</p></figcaption></figure>

### Architecture Overview

Nexus Layer 1 will be made up of the following components:

* **Execution Layer:** Processes all transactions and state transitions across two synchronized execution environments
  * **NexusCore**: High-performance execution environment that hosts *enshrined co-processors* with deterministic, sub-500 ms latency for specialized financial operations.
  * **NexusEVM:**  An Ethereum-compatible virtual machine providing general-purpose programmability, composability, and full EVM tooling support for decentralized applications.
* Consensus Layer:
  * **NexusBFT:** A custom Byzantine Fault Tolerant consensus protocol that finalizes dual-execution blocks, coordinates validators, and manages the on-chain registry of co-processors.
* Verification Layer:
  * **NexuszkVM:** A verifiable compute engine that generates zero-knowledge proofs attesting to the correctness of all Layer-1 execution,
  * **NexusNetwork:** Distributed proving network where nodes contribute computational power to produce and aggregate zkVM proofs, progressively moving the system toward a single *Universal Proof* of global state.

This unified system will enable users to build and access institutional-grade financial infrastructure onchain, with sub-second latency, shared native liquidity, and cryptographic proof of correctness, bringing the speed, depth, and reliability of traditional markets into a verifiable and composable blockchain environment.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2F5aBoOFkDXlAJzSuvsetC%2F2.png?alt=media&#x26;token=a7b8a514-43b0-4be7-bb46-1b5facc68556" alt=""><figcaption><p>Each layer is independently optimizable, and co-designed for high end-to-end performance.<br><br>*Stack-based visualization, showing each of the three layers in the Nexus blockchain <br>as independently optimizable, yet co-designed, components.</p></figcaption></figure>

### Product Overview

* **Perpetual futures** – the Alpha release for the Nexus Exchange offers perpetuals trading&#x20;
* **High-performance APIs -** Nexus will offer native trading APIs for submitting trades to the Exchange&#x20;
* **High-throughput, low latency** – order matching will be handled inside NexusCore, the Exchange coprocessor engine, for CEX-like speed with onchain security guarantees
* **The Internet Exchange -** spot, perps, options, RWAs, treasuries, FX, and other verifiable finance products and assets will roll out in subsequent product releases
