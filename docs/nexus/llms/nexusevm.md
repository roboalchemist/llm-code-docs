# Source: https://docs.nexus.xyz/architecture/nexusevm.md

# NexusEVM

NexusEVM will be the general-purpose execution environment of the Nexus Layer 1. It will maintain full Ethereum compatibility while integrating natively with NexusCore and a dual-block architecture.\
NexusEVM will provide developers with a familiar toolchain but will operate within a system capable of sub-second block times and atomic integration with high-frequency co-processors. This system is designed to marry the capabilites of specialized and general-purpose computation in one unified environment.

### Architecture

#### EVM Compatibility

NexusEVM will adhere to the Ethereum Virtual Machine standard:

* Same contract bytecode and gas semantics
* Compatible with standard RPCs and developer tools
* Supports Solidity and Vyper contract deployment without modification

This will ensure that existing Ethereum contracts can migrate directly onto Nexus with minimal refactoring.

#### Dual Execution Integration

In the dual execution model, NexusEVM will operate in parallel with NexusCore. Contracts deployed on NexusEVM will be able to call Core-level co-processors through EVM precompiles or cross-domain messages.

**Cross-domain guarantees**

* **Atomicity:** If either side fails, the transaction reverts globally
* **Determinism:** Ordered processing ensures consistent state transitions across validators
* **Predictability:** EVM block intervals occur deterministically (every 4–10 Core blocks)

#### Developer Experience

Developers on NexusEVM will be able to:

* Build standard EVM contracts and integrate with NexusCore co-processors via library precompiles
* Compose financial logic that leverage the speed and liquidity of Core modules
* Use familiar deployment flows with added access to native on-chain APIs and cross-domain event hooks

### Role in the System

NexusEVM will provide the expressive layer of the Nexus architecture. While NexusCore will deliver raw execution power, NexusEVM will ensure programmability, composability, and developer accessibility, allowing any contract to interact with financial co-processors and verifiable computation through atomic cross-domain transactions.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FtK3Sdcw4Vznd2mNwRErt%2F9.png?alt=media&#x26;token=b2057354-8c15-4bc9-8f96-08aad2f5c2cb" alt=""><figcaption><p>NexusCore capabilities are accessible to NexusEVM applications, enabling developers <br>to compose and extend NexusCore with custom logic</p></figcaption></figure>
