# Source: https://docs.nexus.xyz/architecture/nexuscore.md

# NexusCore

NexusCore will be the high-performance, specialized execution environment within the Nexus Layer 1. NexusCore is designed for financial primitives that demand deterministic performance and sub-100 ms latency. It will host *enshrined co-processors;* native execution engines built directly into the protocol that provide the performance and extensibility that give rise to new kinds of high-frequency trading, lending, payments, and other markets and market operations.

### Overview

Traditional smart contract environments like the EVM are flexible but limited by latency and gas constraints. NexusCore will extend the capability of an EVM Layer 1 by introducing engines optimized for specialized financial workloads.

Each co-processor will be an independent state machine with its own logic, memory, and data models, enabling CEX-level performance while part of a decentralized and transparent on-chain ecosystem.

**Key characteristics**

* Deterministic execution across validators
* Resource isolation for consistent performance
* Native protocol integration (enshrined within consensus)
* Dual interfaces for both EVM contracts and external systems

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FgjODU6ptEUONHbFz1Aud%2F4.png?alt=media&#x26;token=c7b242ab-4fe5-461d-99a2-e52010fe84b4" alt=""><figcaption><p>NexusCore is home to extensible, special-purpose, execution cores.</p></figcaption></figure>

### Architecture

#### Co-Processor Model

A *co-processor* will be a native module integrated into NexusCore to perform a specific category of financial computation. Unlike contracts that interpret bytecode, co-processors will execute pre-compiled logic with direct access to protocol resources.

Each will operate through three layers of state management:

| Layer             | Function                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------ |
| **State Layer**   | Maintains isolated data structures and deterministic state transitions                     |
| **Machine Layer** | Executes specialized algorithms for the co-processor’s function                            |
| **I/O Layer**     | Manages dual interfaces — native APIs and EVM precompiles — for cross-domain communication |

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FjnLdcYfJ6O9gxnpuHyre%2F8.png?alt=media&#x26;token=bbac8d31-6dcb-4632-ae83-d8c3e790ad0a" alt=""><figcaption><p>Co-processors within NexusCore, such as the Exchange Engine, <br>are independent state-machines enshrined directly into the blockchain.<br><br>Each co-processor is isolated and independently executable, parallelizable, and optimizable.</p></figcaption></figure>

#### State Machine Independence

Every co-processor in NexusCore will operate independently but under shared consensus validation, via NexusBFT. State isolation, modular execution, and resource separation allow:

* Parallel processing across co-processors
* Safe upgrades and new module introduction
* Consensus safety and determinism under load

### Dual Interface Architecture

Co-processors will be accessed via:

* **Native APIs:** enabling direct, low-latency off-chain integration (e.g., through REST or WebSocket endpoints).
* **EVM Precompiles:** allowing on-chain smart contracts to trigger co-processor functions atomically within a single transaction.

This dual access model will enable *both high-frequency trading strategies and DeFi composability* to coexist within the same network.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FuUsOsFhprYMKHvqJ3En7%2F3.png?alt=media&#x26;token=2e6c5f7d-b338-4268-8b8f-baa2e2026d6a" alt=""><figcaption><p>The Execution Layer is comprised of a parallel dual-core architecture, <br>featuring both general-purpose and special-purpose financial state-machines.</p></figcaption></figure>

### Core Example: Exchange Co-Processor

The first co-processor implemented in NexusCore will be the **Exchange**, a high-performance perpetual futures exchange integrated directly into the Layer 1. <br>

The Nexus Exchange will feature:

* Performance capabilities exceeding 100,000 orders per second
* Real-time risk management and liquidation mechanisms
* CCXT-compatible APIs for migrating existing trading infrastructure
* On-chain EVM precompiles for composable DeFi integrations

### Modular Expansion

NexusCore will support a modular co-processor ecosystem, enabling incremental growth of Layer 1 capabilities through the expansion of NexusCore.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2F8b9EKPlGF7RPqbd1MZ8y%2F7.png?alt=media&#x26;token=e0d60baf-f633-4b26-aef1-7ba345edb00f" alt=""><figcaption><p>NexusCore: A Modular Exchange Engine — Enabling Verifiable Markets for Anything<br><br>NexusCore’s co-processor architecture enables developers to deploy permissionless, revenue-generating DEXs for any asset class — leveraging shared engines for margining, risk, and order execution to compose high-frequency financial applications within NexusEVM.</p></figcaption></figure>
