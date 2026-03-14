# Ashen Documentation

Source: https://www.ashen.sh/llms-full.txt

---

<SYSTEM>This is the full developer documentation for Ashen Docs</SYSTEM>

# Ashen Documentation

> The blockchain where validators get paid for reads, transactions can't be frontrun, and agents are first-class citizens.

## Why “Ashen”?

[Section titled “Why “Ashen”?”](#why-ashen)

The `.sh` is the point. [`ashen.sh`](https://ashen.sh) is both a domain and a mental model — shell-first, agent-first. Agents don’t read landing pages; they discover through shell, pay for what they need, and move on. The rest of the name is a nod to burning away the complexity theater of current blockchain economics and rising from the ashes with aligned incentives. [Read the full story →](/getting-started/introduction/#why-ashen)

Paid Reads (x402)

Protocol-native micropayments for RPC calls. Validators earn from every read they serve—no more free-riding on infrastructure.

MEV Protection

Sealed transactions use threshold encryption. Your trades execute as submitted—no frontrunning, no sandwich attacks.

Single-Slot Finality

Transactions finalize in \~1 second. Simplex consensus with BLS threshold signatures means committed = final.

Agent-Native

Deterministic execution, structured APIs, and metered access. Built for AI agents to read, write, and interact.

## Core Infrastructure

[Section titled “Core Infrastructure”](#core-infrastructure)

RISC-V Execution

Smart contracts compile to RV64. Write in Zig with a full SDK: safe math, events, storage helpers, reentrancy guards.

Data Availability

Reed-Solomon erasure coding. Light clients verify data availability with 30 random samples → 99.99% confidence.

DKG Key Rotation

Per-epoch threshold BLS keys via distributed key generation. Forward secrecy through automatic resharing.

Proofs for Everything

Blake3 BMT commitments. Membership proofs, exclusion proofs, finalized history MMR. Verify without trusting.

## Ready to Build?

[Section titled “Ready to Build?”](#ready-to-build)

[Introduction ](/getting-started/introduction/)What is Ashen and why use it?

[Quickstart ](/getting-started/quickstart/)Local node in 5 minutes

[Ashen SDK ](/contracts/ashen-sdk/)Write smart contracts in Zig

[Architecture ](/architecture/overview/)How the chain works

## DeFi & Cross-Chain

[Section titled “DeFi & Cross-Chain”](#defi--cross-chain)

Ashen ships with production-ready contracts: AMM pools, lending markets, staking, vaults, order books. Bridge integrations for Axelar, Hyperlane, and Wormhole. Oracle feeds from Pyth, Chainlink, and Redstone.

[See All Contracts ](/getting-started/introduction/#available-contracts)25+ production-ready contracts

# Consensus

> Simplex consensus with BLS threshold signatures

Ashen uses Simplex consensus from [Commonware](https://commonware.xyz) with BLS threshold signatures for single-slot finality.

## Overview

[Section titled “Overview”](#overview)

The consensus layer provides:

* **BFT Safety** - Blocks are final once committed by quorum (2/3+ validators)
* **Single-Slot Finality** - No confirmation delays or reorg risk
* **Threshold Signatures** - Compact finality proofs via BLS aggregation

For finality guarantees and failure modes, see [Finality](/concepts/finality/).

## Components

[Section titled “Components”](#components)

### Simplex Protocol

[Section titled “Simplex Protocol”](#simplex-protocol)

Simplex is a streamlined BFT protocol optimized for:

* Low-latency block production (\~1 second)
* Deterministic finality (no probabilistic confirmations)
* Efficient validator communication

### BLS Threshold Signing

[Section titled “BLS Threshold Signing”](#bls-threshold-signing)

Validators collectively sign blocks using BLS threshold signatures:

* DKG (Distributed Key Generation) establishes shared keys
* Threshold signatures require t-of-n validators
* Aggregated signatures are compact and efficiently verifiable

See [DKG Flow](/internals/flows/dkg/) for key generation details.

### Epoch Management

[Section titled “Epoch Management”](#epoch-management)

Validator sets can change at epoch boundaries:

* Epoch transitions announced in block headers
* [Light clients](/concepts/light-clients/) track validator set changes
* Key refresh via DKG at epoch boundaries

## Related

[Section titled “Related”](#related)

* [Finality](/concepts/finality/) - Finality model and guarantees
* [Light Clients](/concepts/light-clients/) - Proof verification
* [Finalization Flow](/internals/flows/finalization/) - Block finalization internals
* [Networking](/architecture/networking/) - P2P protocol

# Execution

> RISC-V VM, execution tiers, and transaction processing

Ashen executes smart contracts in a deterministic RISC-V virtual machine with tiered execution (interpreter, JIT, AOT) and metered gas accounting.

## Overview

[Section titled “Overview”](#overview)

The execution layer provides:

* **Deterministic RISC-V VM** - RV64IMC + Zba/Zbb, no floating-point
* **Tiered Execution** - Interpreter → Baseline JIT → Optimizing JIT/AOT
* **Metered Gas** - Per-instruction accounting with identical costs across tiers
* **Sandboxed Isolation** - Memory safety, no shared state between contracts

## Transaction Flow

[Section titled “Transaction Flow”](#transaction-flow)

```plaintext
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  Validate   │ → │  Gas Debit  │ → │   Execute   │ → │   Commit    │
│  sig/nonce  │   │  reserve    │   │  RISC-V VM  │   │  or revert  │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
```

1. **Validation** - Check ed25519 signature, nonce, gas limit, balance
2. **Gas Debit** - Reserve `gas_limit` from payer account
3. **Execution** - Run contract in RISC-V VM (tier selected automatically)
4. **Gas Refund** - Return unused gas to payer
5. **Fee Distribution** - Credit consumed gas to block proposer

## RISC-V Instruction Set

[Section titled “RISC-V Instruction Set”](#risc-v-instruction-set)

Contracts target a deterministic RISC-V profile:

| Extension | Status     | Purpose                                  |
| --------- | ---------- | ---------------------------------------- |
| RV64I     | ✅ Enabled  | Base 64-bit integer instructions         |
| M         | ✅ Enabled  | Multiply/divide                          |
| C         | ✅ Enabled  | Compressed instructions (smaller code)   |
| Zba/Zbb   | ✅ Enabled  | Bit manipulation                         |
| F/D/Q     | ❌ Disabled | Floating-point (use fixed-point instead) |
| A         | ❌ Disabled | Atomics (no threads in contracts)        |
| V         | ❌ Disabled | Vector operations                        |

**Target triple:** `riscv64-unknown-elf` with `+m,+c,+zba,+zbb,-a,-f,-d`

## Execution Tiers

[Section titled “Execution Tiers”](#execution-tiers)

The VM uses tiered execution to balance startup latency with steady-state performance:

```plaintext
          ┌─────────────────┐
          │   Interpreter   │  ← All contracts start here
          │   (reference)   │
          └────────┬────────┘
                   │ hot (>10M gas or >20 calls)
                   ▼
          ┌─────────────────┐
          │  Baseline JIT   │  ← Fast compile, 5x speedup
          │   (Tier 1)      │
          └────────┬────────┘
                   │ hotter (>200M gas or >200 calls)
                   ▼
          ┌─────────────────┐
          │ Optimizing JIT  │  ← Slower compile, 10-20x speedup
          │   (Tier 2)      │
          └─────────────────┘
                   ▲
                   │ failure/eviction → demote to interpreter
```

### Tier 0: Interpreter (Reference)

[Section titled “Tier 0: Interpreter (Reference)”](#tier-0-interpreter-reference)

The interpreter is the **canonical implementation** for semantics and gas costs:

* **Always available** - No compilation required
* **Exact gas accounting** - Per-instruction metering
* **Fallback tier** - Used when JIT fails or is unavailable

All other tiers must produce **identical results and gas usage**.

### Tier 1: Baseline JIT

[Section titled “Tier 1: Baseline JIT”](#tier-1-baseline-jit)

Fast compilation with modest speedup:

* **Compile time:** ≤5ms for 10k instructions
* **Speedup:** \~5x vs interpreter
* **Promotion:** After 10M gas executed or 20 calls

The baseline JIT performs minimal optimization—primarily translating RISC-V to native code with bounds checks.

### Tier 2: Optimizing JIT

[Section titled “Tier 2: Optimizing JIT”](#tier-2-optimizing-jit)

Slower compilation with higher speedup:

* **Compile time:** ≤50ms for 10k instructions
* **Speedup:** 10-20x vs interpreter
* **Promotion:** After 200M gas executed or 200 calls

Performs optimizations like:

* Register allocation
* Dead code elimination
* Basic block reordering
* Constant folding

### AOT (Ahead-of-Time)

[Section titled “AOT (Ahead-of-Time)”](#aot-ahead-of-time)

For frequently-used system contracts, AOT compilation provides:

* **Zero runtime compilation** - Pre-compiled at deploy time
* **Maximum optimization** - Full optimization passes
* **Verified equivalence** - Differential tested against interpreter

## Determinism Guarantees

[Section titled “Determinism Guarantees”](#determinism-guarantees)

All tiers must be **bit-for-bit deterministic**:

| Property      | Requirement                |
| ------------- | -------------------------- |
| Return values | Identical across tiers     |
| State writes  | Same keys, same values     |
| Event logs    | Same topics, same data     |
| Gas consumed  | Exact match to interpreter |

### Verification Strategy

[Section titled “Verification Strategy”](#verification-strategy)

1. **Differential fuzzing** - Random programs tested across all tiers
2. **Replay tests** - Recorded traces replayed in each tier
3. **Conformance corpus** - CI requires 0 mismatches

If any tier produces a mismatch, it **falls back to interpreter**.

## Gas Metering

[Section titled “Gas Metering”](#gas-metering)

Gas is metered identically across all tiers:

### Interpreter

[Section titled “Interpreter”](#interpreter)

* Per-instruction gas deduction
* Checks after every instruction

### JIT/AOT

[Section titled “JIT/AOT”](#jitaot)

* **Basic block metering** - Precompute gas per block
* **Block entry check** - `if gas_left < block_cost → trap`
* **Loop back-edges** - Gas check on every iteration

```plaintext
┌─────────────────────────────────────┐
│  Basic Block Entry                  │
│  ─────────────────                  │
│  if gas_left < 150:                 │
│      trap(OUT_OF_GAS)               │
│  gas_left -= 150                    │
│                                     │
│  ... execute instructions ...       │
│                                     │
│  branch to next block               │
└─────────────────────────────────────┘
```

## Code Cache

[Section titled “Code Cache”](#code-cache)

Compiled code is cached to avoid recompilation:

### Cache Key

[Section titled “Cache Key”](#cache-key)

```plaintext
(code_hash, gas_schedule_version, vm_config_hash, tier)
```

### Eviction

[Section titled “Eviction”](#eviction)

* **Policy:** LRU by total code size
* **Hard cap:** 512 MiB (configurable)
* **Per-contract cap:** 64 MiB

Code changes (new `code_hash`) automatically invalidate cache entries.

## Sandboxing

[Section titled “Sandboxing”](#sandboxing)

Contracts run in isolated sandboxes:

### Memory Isolation

[Section titled “Memory Isolation”](#memory-isolation)

* **Linear address space** - Flat 64-bit virtual memory
* **Guard pages** - Stack/heap overflow protection
* **W^X enforcement** - Pages are writable OR executable, never both

### Syscall Boundary

[Section titled “Syscall Boundary”](#syscall-boundary)

* **ecall instruction** - Only way to interact with host
* **Stable ABI** - Arguments in `a0-a5`, syscall number in `a7`
* **No direct I/O** - All external access through syscalls

### Cross-Contract Calls

[Section titled “Cross-Contract Calls”](#cross-contract-calls)

* Route through runtime dispatcher
* Automatic tier selection for callee
* Copy-on-write memory snapshots for rollback

## Smart Contracts

[Section titled “Smart Contracts”](#smart-contracts)

Contracts compile to RISC-V ELF binaries:

| Language  | Toolchain                | Guide                              |
| --------- | ------------------------ | ---------------------------------- |
| **Zig**   | zig build                | [Ashen SDK](/contracts/ashen-sdk/) |
| **Rust**  | cargo + riscv64 target   | [Examples](/contracts/examples/)   |
| **C/C++** | clang/gcc cross-compiler | Any RISC-V toolchain               |

### Binary Requirements

[Section titled “Binary Requirements”](#binary-requirements)

* **Format:** Static ELF64, no dynamic linking
* **Relocations:** None (position-independent or fixed address)
* **Deterministic:** Built with `SOURCE_DATE_EPOCH`, no build IDs

## Memory Model

[Section titled “Memory Model”](#memory-model)

Each contract instance has isolated memory:

```plaintext
┌──────────────────────────────────┐ High addresses
│          Guard Page              │
├──────────────────────────────────┤
│            Stack                 │ ↓ grows down
│             ↓                    │
├──────────────────────────────────┤
│         (unmapped)               │
├──────────────────────────────────┤
│             ↑                    │
│            Heap                  │ ↑ grows up
├──────────────────────────────────┤
│       Data / BSS                 │
├──────────────────────────────────┤
│      Code (read-only)            │
├──────────────────────────────────┤
│          Guard Page              │
└──────────────────────────────────┘ Low addresses
```

* **Page size:** 4 KiB
* **Max memory:** Configurable per transaction
* **Cleared between txs:** No information leaks

## State Integration

[Section titled “State Integration”](#state-integration)

The VM integrates with on-chain state through:

1. **Storage syscalls** - Read/write contract storage
2. **Dirty page tracking** - Efficient delta computation
3. **Journaling** - Ordered log for crash recovery
4. **Merkle proofs** - State provable to light clients

See [Storage](/architecture/storage/) for details.

## Related

[Section titled “Related”](#related)

* [Gas & Fees](/concepts/gas-and-fees/) - Fee model and pricing
* [Ashen SDK](/contracts/ashen-sdk/) - Contract development
* [Example Contracts](/contracts/examples/) - Reference implementations
* [Storage](/architecture/storage/) - State storage architecture

# Networking

> P2P networking and channels

Ashen uses Commonware’s P2P networking primitives for validator communication and block dissemination.

## Overview

[Section titled “Overview”](#overview)

The networking layer handles:

* **Consensus Messages** - Validator-to-validator BFT protocol messages
* **Block Broadcast** - Disseminating finalized blocks
* **Transaction Gossip** - Propagating mempool transactions

## Channels

[Section titled “Channels”](#channels)

Communication is organized into channels:

| Channel      | Purpose                   |
| ------------ | ------------------------- |
| Consensus    | Simplex protocol messages |
| Blocks       | Finalized block broadcast |
| Transactions | Mempool gossip            |

## Validator Network

[Section titled “Validator Network”](#validator-network)

Validators maintain authenticated connections:

* **Peer Discovery** - Bootstrap from known peers
* **Identity Verification** - Ed25519 peer authentication
* **Encrypted Transport** - Noise protocol encryption

See [Running a Node](/guides/running-a-node/) for network configuration.

## Block Dissemination

[Section titled “Block Dissemination”](#block-dissemination)

Finalized blocks are broadcast to all nodes:

* **Buffered Broadcast** - Efficient block propagation
* **Finality Proofs** - BLS signatures included for verification
* **[Data Availability](/concepts/data-availability/)** - Erasure coding for light clients

## Related

[Section titled “Related”](#related)

* [Consensus](/architecture/consensus/) - BFT protocol
* [Running a Node](/guides/running-a-node/) - Node setup
* [Data Availability](/concepts/data-availability/) - Block sampling
* [Configuration](/reference/configuration/) - Network settings

# Architecture Overview

> High-level overview of Ashen architecture

This page describes Ashen’s testnet architecture. For component details, see:

[Consensus ](/architecture/consensus/)Simplex BFT protocol

[Execution ](/architecture/execution/)RISC-V VM

[Storage ](/architecture/storage/)State management

[Networking ](/architecture/networking/)P2P protocol

## Testnet Architecture

[Section titled “Testnet Architecture”](#testnet-architecture)

```plaintext
                            ┌─────────────────────────────────────────────────────────┐
                            │                    TESTNET ARCHITECTURE                  │
                            └─────────────────────────────────────────────────────────┘


    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │                                   CONSENSUS LAYER                                      │
    │                                                                                        │
    │   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐                   │
    │   │  Validator 0    │    │  Validator 1    │    │  Validator 2    │                   │
    │   │  (PRUNING)      │    │  (PRUNING)      │    │  [ARCHIVE]      │                   │
    │   │                 │    │                 │    │                 │                   │
    │   │  P2P: :4040     │◄──►│  P2P: :4041     │◄──►│  P2P: :4042     │                   │
    │   │  Metrics: :3031 │    │  Metrics: :3032 │    │  Metrics: :3033 │                   │
    │   │                 │    │                 │    │                 │                   │
    │   │  ┌───────────┐  │    │  ┌───────────┐  │    │  ┌───────────┐  │                   │
    │   │  │ 3 epochs  │  │    │  │ 3 epochs  │  │    │  │ FULL      │  │                   │
    │   │  │ of state  │  │    │  │ of state  │  │    │  │ HISTORY   │  │                   │
    │   │  └───────────┘  │    │  └───────────┘  │    │  └───────────┘  │                   │
    │   └────────┬────────┘    └────────┬────────┘    └────────┬────────┘                   │
    │            │                      │                      │                            │
    │            └──────────────────────┼──────────────────────┘                            │
    │                                   │                                                   │
    │                          BLS Threshold Signing                                        │
    │                          DKG Key Refresh                                              │
    │                          Simplex Consensus                                            │
    └───────────────────────────────────┼───────────────────────────────────────────────────┘
                                        │
                                        │ shares data dir
                                        ▼
    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │                                    RPC LAYER                                           │
    │                                                                                        │
    │                            ┌─────────────────────┐                                     │
    │                            │    RPC Server       │                                     │
    │                            │    :3030            │                                     │
    │                            │                     │                                     │
    │                            │  • Full /v2/rpc     │                                     │
    │                            │  • Historical queries│                                    │
    │                            │  • tx_submit        │                                     │
    │                            │  • WebSocket subs   │                                     │
    │                            └──────────┬──────────┘                                     │
    │                                       │                                                │
    └───────────────────────────────────────┼────────────────────────────────────────────────┘
                                            │
                                            ▼
    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │                                   CLIENTS                                              │
    │                                                                                        │
    │     ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐                      │
    │     │   ashen    │    │  dApps   │    │ Explorer │    │ Wallets  │                      │
    │     │   CLI    │    │          │    │          │    │          │                      │
    │     └──────────┘    └──────────┘    └──────────┘    └──────────┘                      │
    │                                                                                        │
    └────────────────────────────────────────────────────────────────────────────────────────┘
```

## Data Flow

[Section titled “Data Flow”](#data-flow)

```plaintext
Transactions:   Client ──► RPC ──► Mempool ──► Leader Validator ──► Block


Blocks:         Leader ──► P2P Broadcast ──► All Validators ──► Finality Proof


Queries:        Client ──► RPC ──► Archive Validator State ──► Response
```

## Storage Per Node

[Section titled “Storage Per Node”](#storage-per-node)

**Pruning Validators (0, 1):**

* testnet-local/

  * node-X/

    * genesis.json

    * blocks/ pruned

      * …

    * state/ 3 epochs only

      * …

    * consensus/

      * …

**Archive Validator (2):**

* testnet-local/

  * node-2/

    * genesis.json

    * **blocks/** full history

      * …

    * **state/** full history

      * …

    * consensus/

      * …

## Node Roles

[Section titled “Node Roles”](#node-roles)

| Role               | Mode                                | Storage      | RPC          | Consensus |
| ------------------ | ----------------------------------- | ------------ | ------------ | --------- |
| Pruning Validator  | `--validator --prune-keep-epochs N` | Limited      | Metrics only | Yes       |
| Archive Validator  | `--validator --archive-mode`        | Full         | Metrics only | Yes       |
| RPC Server         | `node rpc`                          | Shared       | Full         | No        |
| Follower (planned) | `--follower`                        | Configurable | Full         | No        |

## Running the Testnet

[Section titled “Running the Testnet”](#running-the-testnet)

1. **Generate keys and peers.yaml** (first time only)

   ```bash
   just testnet-local-generate
   ```

2. **Run testnet** - 2 pruning + 1 archive validator + RPC

   ```bash
   just testnet-local-run
   ```

3. **Custom configuration** (optional)

   ```bash
   just testnet-local-run N_VALIDATORS=5 PRUNE_KEEP_EPOCHS=5
   ```

## Ports (Default Configuration)

[Section titled “Ports (Default Configuration)”](#ports-default-configuration)

| Service             | Port |
| ------------------- | ---- |
| RPC Server          | 3030 |
| Validator 0 Metrics | 3031 |
| Validator 1 Metrics | 3032 |
| Validator 2 Metrics | 3033 |
| Validator 0 P2P     | 4040 |
| Validator 1 P2P     | 4041 |
| Validator 2 P2P     | 4042 |

## Pending Features

[Section titled “Pending Features”](#pending-features)

Standalone Follower Node

```plaintext
     ┌─────────────┐         P2P FollowerSync         ┌─────────────┐
     │ Validators  │ ─────────────────────────────►   │  Follower   │
     │             │   Headers + Finality Proofs      │  (Archive)  │
     └─────────────┘                                  └─────────────┘
                                                      Not a validator,
                                                      just syncs & serves RPC
```

This will enable true separation where validators can all prune while dedicated follower/archive nodes sync via P2P and serve historical queries.

Validator Ops (Planned)

* Graceful shutdown with state persistence
* Validator status RPC endpoint
* Backup/snapshot export for disaster recovery
* Alerting hooks (webhook notifications)
* Manual BLS key rotation command

# Storage

> State layout, key encoding, backends, and commitment scheme

The storage layer defines a single logical keyspace that represents balances, nonces, contracts, and system state. It is designed to be simple to implement and easy to prove over (Blake3 BMT commitments), and forward-compatible with richer features (multiple assets, RISC-V contracts, gadgets) without breaking existing keys.

The [VM architecture](/architecture/execution/) is the **canonical** specification for state and commitments. If this page or the current implementation ever disagree with the VM specification, the VM document wins and the state layer should be updated to match it.

Rejected state management alternatives are documented in `docs/adr/adr-0001-rejected-state-management-approaches.md`.

## 1. Logical keyspace and canonical encoding

[Section titled “1. Logical keyspace and canonical encoding”](#1-logical-keyspace-and-canonical-encoding)

The canonical logical keyspace is:

```text
(Address, storage_key_bytes) -> value_bytes
```

This is represented in code by `StateKey` in `src/storage/state.rs`:

* `address: Address` (the account / contract / system id)
* `key: Vec<u8>` (opaque storage key within that address)

The `key` byte sequence is logically namespaced with simple prefixes so that different kinds of state do not collide inside an account.

For commitments, a **canonical key encoding** is used rather than a fixed hash function in this layer. Conceptually:

```text
canonical_key_bytes = address.canonical_bytes() || key_len_be || key
```

where `key_len_be` is the big-endian encoding of `key.len()` as a fixed-width integer. In code, `StateKey::canonical_bytes()` returns these canonical bytes.

The **global state commitment** is hierarchical, using the `commonware_storage::bmt` primitive at both layers:

* **Inner (per-address) tree:** Blake3 BMT over leaves `Blake3(canonical_key_bytes || Blake3(value_bytes))` for all keys owned by that address (balances/nonces/assets/code/meta/slots/system/opaque). The `"meta"` entry is a regular leaf inside this inner tree. Empty address => Blake3(empty).
* **Outer (global) tree:** Blake3 BMT over leaves `Blake3(address.canonical_bytes() || contract_root)`, where `contract_root` is the inner root for that address. Empty outer tree => Blake3(empty).
* The exact hashing and position-hash formulas are defined by `Tree<Blake3>` and are normative; both inner and outer trees use the same builder semantics.

Important invariants:

* Given the same set of `(Address, key, value_bytes)` pairs at a block height, **all** `StateBackend` implementations must produce identical inner roots per address and the same outer Blake3 BMT root when leaves are fed to `Tree<Blake3>` in canonical address order.
* Block headers and light clients use the outer root as the canonical `state_root` immediately; any legacy flat roots are deprecated.

### 1.1 Table metadata and normalization

[Section titled “1.1 Table metadata and normalization”](#11-table-metadata-and-normalization)

To keep table-specific hashing explicit and VM-aligned, a small registry is maintained in `src/storage/state.rs`:

* Tables: balance (`STATE_KEY_BALANCE_PREFIX`), nonce (`STATE_KEY_NONCE_PREFIX`), asset (`STATE_KEY_ASSET_PREFIX`), code (`STATE_KEY_CODE_PREFIX`), meta (`STATE_KEY_META_PREFIX`), slot (`STATE_KEY_SLOT_PREFIX`), and `system` (addresses starting with `system:`); everything else is `Opaque`.
* Fields: `KeyEncoding` (currently the canonical `address || key_len_be || key`), `HashingMode` (`None` or `Blake3Key` over the raw key bytes), and `allow_override` to gate table-specific overrides.
* Defaults: all tables use canonical encoding with no key hashing; overrides are locked for balance/nonce/asset/code/meta and allowed for slot/system/opaque tables.

Normalization helpers:

* Callers provide `(table, address, key_bytes)` to `KeyMetadataRegistry::normalize_for_table` (or `canonical_key_bytes_for_table` / `blake3_leaf_for_table`).
* The helper produces normalized key bytes (hashed if configured), canonical key bytes, and the Blake3 leaf preimage `Blake3(canonical_key_bytes || Blake3(value_bytes))`.

Backends and tooling:

* `InMemoryStateBackend` and `JournalStateBackend` carry a `KeyMetadataRegistry` and use it when building BMT leaves; `with_metadata_registry` lets tests wire custom metadata, and `set_metadata_registry` forces a rebuild when overrides change.
* Access list / VM adapter code can share the same registry to guarantee the normalized key a caller warms is the one committed in the BMT.

## 2. Per-account key layout

[Section titled “2. Per-account key layout”](#2-per-account-key-layout)

Each `Address` owns a private keyspace defined by `key: Vec<u8>`. Several sub-namespaces are standardized.

### 2.1 Core account fields (current engine)

[Section titled “2.1 Core account fields (current engine)”](#21-core-account-fields-current-engine)

These are used by the simple balance-transfer engine and `AccountState`.

* **Native balance**

  * Key:

    ```text
    key = STATE_KEY_BALANCE_PREFIX
    ```

    `STATE_KEY_BALANCE_PREFIX` is defined in `src/core/mod.rs` and is currently `[0x01, 0x01]`.

    Implemented as `StateKey::balance_key(address)`.

  * Value:

    ```text
    value = u64::to_be_bytes(balance)
    ```

* **Nonces (authorizer lanes)**

  * Key:

    ```text
    key = STATE_KEY_NONCE_PREFIX || lane.to_be_bytes()
    ```

    `STATE_KEY_NONCE_PREFIX` is defined in `src/core/mod.rs` and is currently `[0x01, 0x02]`.

    Implemented as `StateKey::nonce_key(authorizer, lane)`.

  * Value:

    ```text
    value = next_nonce.to_be_bytes() || policy_byte
    ```

    where `policy_byte` is the discriminant of `NoncePolicy` (currently only `Strict`).

These keys mirror `AccountState` into the generic KV map in both `InMemoryStateBackend` and `JournalStateBackend`. In the VM-aligned design, balances and nonces remain under these keys, but the **canonical** state root is the Blake3 BMT root over the KV map, not the legacy `AccountState::compute_state_root()` hash.

### 2.2 Multi-asset balances (future)

[Section titled “2.2 Multi-asset balances (future)”](#22-multi-asset-balances-future)

A dedicated asset namespace for per-asset balances, distinct from the native balance key.

* Key format (canonical):

  ```text
  key = STATE_KEY_ASSET_PREFIX || asset_id_len || asset_id_bytes
  ```

  `STATE_KEY_ASSET_PREFIX` is defined in `src/core/mod.rs` and is currently `[0x01, 0x03]`.

  * `asset_id_bytes` is an ASCII/UTF-8 identifier (<= 64 bytes recommended).

  * Reserved ids:

    * `"native"` is the canonical id for the chain’s base asset.
    * `"cw:<hex>"` for hash-derived assets (bridge/minted), where `<hex>` is lowercase hex of a 32-byte id.
    * `"sym:<ticker>"` for human-readable symbols when unique.

* Value:

  ```text
  value = u128 encoded big-endian (u64 acceptable while supply fits)
  ```

* Native balance compatibility:

  * The native balance is stored under `STATE_KEY_BALANCE_PREFIX`.
  * The canonical native asset key `STATE_KEY_ASSET_PREFIX || len("native") || b"native"` is reserved, but state backends do not currently write this alias.
  * Engines should treat the balance key as authoritative until alias writes are implemented.

* Prefetch / access lists:

  * Access descriptors for native balances should target the balance key; if a scheduler uses the asset form internally, it must translate to the balance key because the alias is not persisted.
  * All other assets must use the explicit asset namespace form.

### 2.3 Contract / VM fields

[Section titled “2.3 Contract / VM fields”](#23-contract--vm-fields)

For a contract account (RISC-V VM), keys for code, metadata, and storage are standardized. These layouts are consumed by the VM adapter and language SDKs.

* **Contract code**

  * Key:

    ```text
    key = STATE_KEY_CODE_PREFIX
    ```

    `STATE_KEY_CODE_PREFIX` is defined in `src/core/mod.rs` and is currently `[0x01, 0x04]`.

  * Value:

    Opaque bytes representing the compiled contract code (for example, ELF64 RV64 binary image).

* **Contract metadata**

  * Key:

    ```text
    key = STATE_KEY_META_PREFIX
    ```

    `STATE_KEY_META_PREFIX` is defined in `src/core/mod.rs` and is currently `[0x01, 0x05]`.

  * Value:

    `ContractCodeMetadata` encoded with Borsh. Fields capture VM type, code hash (mandatory for deploy/upgrade), ABI version, optional gas schedule version, and optional manifest hash. Helpers live in `src/storage/state.rs` (`store_contract_metadata`, `load_contract_metadata`) and are exposed to the VM via the `VmContractState` trait.

* **Contract IDL**

  * Key:

    ```text
    key = STATE_KEY_IDL_PREFIX
    ```

    `STATE_KEY_IDL_PREFIX` is defined in `src/core/mod.rs` and is currently `[0x01, 0x06]`.

  * Value:

    Raw IDL bytes as produced by the contract build toolchain. Stored verbatim (no normalization).

* **Contract storage slots**

  * Key:

    ```text
    key = STATE_KEY_SLOT_PREFIX || slot_id_bytes
    ```

    `STATE_KEY_SLOT_PREFIX` is defined in `src/core/mod.rs` and is currently `[0x01, 0x00]`.

    where `slot_id_bytes` is a fixed-size identifier (standardized to 32-byte little-endian) derived by the VM or SDK from higher-level storage schemas. Using little-endian aligns with the RV64 toolchain and SDKs; note that lexicographic ordering follows the raw little-endian bytes rather than numeric order, so range/prefix descriptors must treat the raw bytes as canonical. The canonical derivation recipe is `slot_id = Blake3(namespace || b":" || name)` rendered as 32-byte little-endian; `StateKey::derive_slot_id` in `src/storage/state.rs` implements this helper.

  * Value:

    Opaque bytes whose semantics are defined by the VM / contract (for example 32 byte word, Borsh encoded struct, etc.).

A RISC-V VM adapter maps its internal notion of storage (typed tables, page-backed memory, etc.) into `STATE_KEY_SLOT_PREFIX`-prefixed keys. The [VM specification](/architecture/execution/) describes how per-contract object stores and typed key-value tables are built on top of this namespace and how they participate in the global Blake3 BMT.

### 2.4 System and gadget state

[Section titled “2.4 System and gadget state”](#24-system-and-gadget-state)

Addresses beginning with `"system:"` are reserved and cannot be user-created. These textual identifiers are also the VM-facing names; `Address::canonical_bytes` continues to hash them for consensus.

Stable system accounts and prefixes:

* `Address("system:core")`

  * `key = "config:" || name_bytes` for chain config fields (chain\_id, feature flags, deterministic harness toggles).
  * `key = "epoch:" || epoch_number.to_be_bytes()` for epoch metadata surfaced to the VM.

* `Address("system:gas")`

  * `key = "schedule:" || version_be` stores serialized gas schedules; the latest schedule is aliased under `"schedule:latest"`.

* `Address("system:validators")`

  * `key = "epoch:" || epoch_number.to_be_bytes()` -> encoded validator set and commitments.
  * `key = "dkg:" || epoch_number.to_be_bytes()` -> DKG/resharing artifacts when enabled.

* `Address("system:seals")`

  * `key = "sealed:" || intent_id_bytes` -> sealed intent blobs / commitments.

* `Address("system:bridge")`

  * `key = "near:" || block_height_bytes` -> NEAR DA metadata (block hash, receipt id, log index, commitment, …).
  * `key = "proof:" || batch_id_bytes` -> bridge proofs / checkpoints for downstream verifiers.

Conventions:

* Contracts and users MUST NOT claim addresses with prefix `"system:"`; backends and account allocators should reject or gate them by policy.
* New gadgets should extend this list rather than minting ad-hoc prefixes: use `"system:<component>"` and subordinate key prefixes to avoid collisions.
* These entries are ordinary KV pairs for the backend; higher layers interpret the values and can export proofs using the same canonical key encoding.

### 2.5 Contract sub-roots and proofs

[Section titled “2.5 Contract sub-roots and proofs”](#25-contract-sub-roots-and-proofs)

* **Inner tree (per address):** Blake3 BMT over `Blake3(canonical_key_bytes || Blake3(value_bytes))` for every key owned by that address, including `"meta"` as a first-class leaf. Keys are ordered by canonical bytes; empty => Blake3(empty).

* **Outer tree (global):** Ordered Blake3 BMT over leaves `Blake3(address.canonical_bytes() || contract_root)` (address concatenated with the per-address root), ordered by `address.canonical_bytes()`. Empty outer tree => Blake3(empty). Metadata lives only inside the inner tree; there is no outer meta hash.

* **Proof composition:**

  * Membership: `(value_bytes, slot_proof, contract_proof)` where `slot_proof` is the inner `Proof` from the `(address, key)` leaf preimage to `contract_root`, and `contract_proof` is the outer `Proof` from `(address, contract_root)` to `state_root`.
  * Non-membership (slot): include the queried canonical key plus predecessor/successor membership proofs in the inner tree (`slot_proof_pre`, `slot_proof_suc`) that verify to the same `contract_root`, demonstrating the gap. An empty inner tree proves non-membership only when the outer contract exists and its root is Blake3(empty).
  * Non-membership (contract): provide predecessor/successor membership proofs in the outer tree around the queried `address.canonical_bytes()` to show the absence of that address leaf under the `state_root`. An empty outer tree proves non-membership only when `state_root == Blake3(empty)`.

* **Serialization and ordering:** Proofs use the canonical `Proof` binary encoding from `commonware_storage::bmt` (length-prefixed path from leaf to root, each hop tagged with left/right orientation and the sibling hash). Canonical keys and leaf preimages follow `StateKey::canonical_bytes()` (address || key\_len\_be || normalized\_key); ordering is strictly lexicographic over these bytes so verifiers can reconstruct positions deterministically. Invalid ordering, unexpected slot proofs when the contract is absent, or non-empty roots with missing neighbors are verification errors.

* **Verifier walkthrough:**

  * Inputs: `state_root`, `address`, `key`, `value` (for membership), and the `(slot_proof, contract_proof)` pair using the BMT wire format.

  * Membership: recompute `canonical_key_bytes = address.canonical_bytes() || key_len_be || normalized_key`; compute `leaf = Blake3(canonical_key_bytes || Blake3(value))`; verify `slot_proof` to a `contract_root`, then verify `contract_proof` from `(address.canonical_bytes(), contract_root)` to `state_root`.

  * Slot non-membership: use the queried canonical key and verify predecessor/successor proofs to the same `contract_root` (or empty inner root) with strict ordering; reject if both neighbors are missing and `contract_root != Blake3(empty)`.

  * Contract non-membership: verify predecessor/successor proofs around `address.canonical_bytes()` to the same `state_root`; reject if both neighbors are missing and `state_root != Blake3(empty)` or if a slot proof is present.

  * Minimal Rust example (using the in-memory backend and `StateProof::verify`):

    ```rust
    let mut backend = InMemoryStateBackend::new();
    let sk = StateKey::storage_slot_key(&addr, b"alpha");
    backend.put(&addr, &sk.key, b"one".to_vec());
    let state_root = backend.commit(1);


    let proof = backend.prove_state(&addr, &sk.key).unwrap();
    assert_eq!(proof.state_root, state_root);


    let leaf = backend.bmt.metadata().leaf_preimage(&sk, b"one");
    match proof.slot_proof {
        Some(SlotProof::Exists { canonical_key, proof, .. }) => {
            assert_eq!(canonical_key, backend.bmt.metadata().canonical_bytes(&sk));
            assert_eq!(proof.leaf, leaf);
        }
        _ => unreachable!(),
    }


    proof.verify().unwrap();
    ```

## 3. Access lists and state keys

[Section titled “3. Access lists and state keys”](#3-access-lists-and-state-keys)

`TxBodyV1` carries a single non-versioned `AccessList` with richer descriptors aligned to the VM spec:

```rust
pub struct AccessList {
    pub accounts: Vec<Address>,
    pub storage: Vec<AccessEntry>,
}


pub struct AccessEntry {
    pub address: Address,
    pub descriptors: Vec<AccessDescriptor>,
}


pub enum AccessDescriptor {
    Exact { key: [u8; 32], mode: AccessMode },
    Prefix { prefix: Vec<u8>, mode: AccessMode },
    Range { range: AccessRange, mode: AccessMode },
}
```

Semantics relative to the state layout:

* Each `accounts[i]` declares that the transaction may touch the account’s native balance, default nonce lane, and common contract keys (code/meta and all contract storage slots). Warm-set derivation uses the canonical state key helpers so descriptors line up with commitment ordering.
* `Exact` descriptors map directly to `StateKey` values under the entry’s address (prefetch/warming uses these exact keys).
* `Prefix` and `Range` descriptors describe broader access sets for scheduling/strict checks; they are not expanded to concrete keys in the state layer. Inclusive/exclusive bounds are enforced lexicographically over 32-byte keys; prefixes are treated as `[prefix || 0x00..]` to `[prefix || 0xFF..]` ranges for overlap checks.
* Modes (`Read`, `Write`, `ReadWrite`) are carried for executor scheduling and diagnostics; the current simple engine still treats the list as advisory.

The list remains advisory for the v1 engine but is signed and can be used by tooling, prefetchers, and future stateless clients. Deterministic harnesses enable touched-key tracing and undeclared-access warnings by default (gateable via `system:core` config toggles and `ASHEN_STRICT_ACCESS`/`ASHEN_TRACE_STATE_KEYS` env overrides), and helper utilities can detect overlapping ranges/prefixes for diagnostics.

## 4. Backends and commitments

[Section titled “4. Backends and commitments”](#4-backends-and-commitments)

The logical layout is implemented over a generic `StateBackend` trait in `src/storage/state.rs`:

```rust
pub trait StateBackend: Send {
    fn get(&self, address: &Address, key: &[u8]) -> Option<Vec<u8>>;
    fn put(&mut self, address: &Address, key: &[u8], value: Vec<u8>);
    fn commit(&mut self, height: u64) -> Hash;
}
```

The **canonical commitment** returned by `commit` is the Blake3 BMT root over the set of `(StateKey, value_bytes)` pairs present at that height, as defined by `commonware_storage::bmt::Tree<Blake3>`. Any legacy roots derived from `AccountState` are transitional and not part of the VM surface.

Two main backend families exist:

* `InMemoryStateBackend` (tests and simple runners):

  * Maintains a `HashMap<StateKey, Vec<u8>>` for arbitrary keys.
  * Mirrors balances and nonces from `AccountState` into `StateKey`s using the `STATE_KEY_BALANCE_PREFIX` and `STATE_KEY_NONCE_PREFIX` layouts above, so tests that still exercise the simple execution engine can share one view of state.
  * On `commit(height)`, computes the canonical Blake3 BMT root over its KV map and returns that root.
  * The existing `AccountState::compute_state_root()` function remains as a **compatibility helper** for old code paths and tests, but block headers and light clients must use the Blake3 BMT root produced by `StateBackend::commit` as the authoritative state commitment.

* `JournalStateBackend<B>` (and `CachedJournalStateBackend<B>`):

  * Records `(height, key_bytes, value_bytes)` updates in a journal stored on top of an abstract blob `B`.
  * Maintains an in-memory index `StateKey -> (last_height, value)` that represents the latest value for each key at the current height.
  * Per-transaction journaling: `begin_tx` pushes a speculative layer, `apply_tx` merges staged writes into the parent (or the pending buffer if it is the outermost), and `rollback_tx` discards staged writes. Reads walk the stack, pending buffer, then committed index.
  * Snapshots: `create_snapshot` captures an immutable view of `kv`+`pending`; `snapshot_get` reads from it; snapshots can be dropped or pruned by height.
  * On `commit(height)`, flushes pending updates to the journal, updates the in-memory index, and recomputes (or incrementally updates) the Blake3 BMT root over all `(StateKey, value)` pairs.
  * Uses `commonware_storage::bmt::Tree<Blake3>` (via `Builder`) as the reference Merkle implementation. The backend feeds keys in a deterministic order using the canonical key encoding described above.

* `CachedJournalStateBackend` wraps `JournalStateBackend` with an in-memory LRU cache of hot keys to accelerate repeated reads while leaving commitment semantics unchanged.

Default deterministic harnesses use the cached journal variant with a small LRU to exercise the durable path while keeping read latency predictable; the pure in-memory backend remains for fast unit tests.

During migration:

* Some tests and code paths may still compare the legacy `AccountState::compute_state_root()` with the BMT root for the subset of state consisting only of balances and nonces.
* These roots are intentionally different: the older function hashes a flat serialization of sorted `(Address, lane)` entries, while the BMT hashes canonical key encodings and values through a Blake3 tree.

The long-term target is that **block headers and light clients depend only on the Blake3 BMT root**, and any legacy roots are kept strictly for compatibility tests or transitional tooling.

### Rent, TTL, and snapshots (backend policy)

[Section titled “Rent, TTL, and snapshots (backend policy)”](#rent-ttl-and-snapshots-backend-policy)

* Backends track per-key rent metadata `(ttl_height, pinned, last_access_height, size_bytes)`. A default TTL is applied to any write that does not supply one, using `RentConfig::default_ttl_epochs` relative to the last committed height.
* Commit-time expiry removes non-pinned keys whose `ttl_height` is below the commit height, marks the BMT leaf set dirty, and reports `RentOutcome { expired_keys, reclaimed_bytes, rent_fee_report }`. Fees are reported only; no balances are debited yet.
* Pinned keys skip expiry and pruning but still accrue surcharge in the rent report via `pin_surcharge_per_byte`.
* Snapshots are immutable `(kv + pending)` views tagged with their creation height. Pruning refuses to drop state below active snapshot heights or pinned entries. `RentConfig::max_retained_heights` and `max_retained_bytes` gate pruning; operators can surface counters for skipped prunes and retained heights.

## 5. Checkpoints and archival hooks

[Section titled “5. Checkpoints and archival hooks”](#5-checkpoints-and-archival-hooks)

Execution state checkpoints are recorded via `StateCheckpointMeta` in `src/storage/mod.rs`:

```rust
#[derive(Debug, Clone)]
pub struct StateCheckpointMeta {
    pub height: u64,
    pub state_root: Hash,
    pub archive: Option<StateArchiveDescriptor>,
}
```

Semantics:

* `height` and `state_root` identify the logical state at a checkpoint (typically the first finalized block of an epoch).
* `state_root` must be the canonical Blake3 BMT root produced by `StateBackend::commit(height)` at that height.
* `archive` is an optional pointer into an external archive / freezer implementation that can serve compact snapshots or historical proofs.
* On-disk chain stores currently persist only `(height, state_root)`; the archival descriptor is kept in memory and is intended to be managed by a future archival/indexing component that uses `commonware_storage::archive` / `freezer`.

The application actor records checkpoints at epoch boundaries; see `Application::handle_marshal` in `src/application/mod.rs`. This aligns checkpoints with the logical state layout and the VM’s expectation that the exported `state_root` is a Blake3 BMT root over the global object store.

## 6. RISC-V VM expectations

[Section titled “6. RISC-V VM expectations”](#6-risc-v-vm-expectations)

This layout is chosen so that the RISC-V VM can:

* Treat `Address` as the contract id.
* Load code and metadata using well-known keys (`"code"`, `"meta"`).
* Map its persistent storage to the `STATE_KEY_SLOT_PREFIX` namespace and derive per-contract storage keys from language-level schemas.
* Use transaction access lists and richer access descriptors to declare and prefetch `StateKey`s that will be touched during execution.
* Rely on `StateBackend::commit(height)` to produce a canonical Blake3 BMT root over the global keyspace at a given block height.

No RISC-V specific code is required in the state layer itself; the VM is an adapter on top of the logical key/value layout and the `StateBackend` interface. VM implementation details (instruction set, hostcall ABI, gas model, executor) live in the [execution architecture](/architecture/execution/).

## Related

[Section titled “Related”](#related)

* [Execution](/architecture/execution/) - VM architecture and state transitions
* [Light Clients](/concepts/light-clients/) - State proof verification
* [Data Availability](/concepts/data-availability/) - Block data storage
* [Configuration](/reference/configuration/) - Storage settings

# Docs Changelog

> Recent changes to the documentation, generated from Git history.

This page is auto-generated from git history for `docs-site/src/content/docs` and updates on build.

Note

Generated by `scripts/generate-docs-changelog.mjs`. Set `DOCS_CHANGELOG_LIMIT` to change the number of entries and `DOCS_CHANGELOG_REPO_URL` to override commit links.

## 2026-02-12

[Section titled “2026-02-12”](#2026-02-12)

* [8289d63](https://github.com/carrion256/chain/commit/8289d633902a5ca3ad099f3956b1bd39dada2c11) Documentation update

# Block Builder Selection

> Block proposer selection policy and leader rotation

This document specifies the block builder (proposer) selection policy and its guarantees.

## Overview

[Section titled “Overview”](#overview)

Block builder selection in this chain is handled by the **Commonware Simplex BFT consensus** protocol. The selection is:

* **Deterministic**: Given the same epoch, view, and validator set, the selected leader is always the same
* **Round-robin**: Leaders rotate through the validator set based on view number
* **Epoch-scoped**: Each epoch has a fixed, ordered validator set

## Selection Algorithm

[Section titled “Selection Algorithm”](#selection-algorithm)

### Leader Selection Formula

[Section titled “Leader Selection Formula”](#leader-selection-formula)

```plaintext
leader_index = view % num_validators
leader = validators[leader_index]
```

Where:

* `view` is the current consensus view/round number
* `num_validators` is the size of the active validator set for the epoch
* `validators` is an **ordered** list of validator public keys

### Validator Set Ordering

[Section titled “Validator Set Ordering”](#validator-set-ordering)

The validator set ordering is determined by:

1. **Genesis**: Initial participant list from configuration (lexicographically sorted by public key)
2. **DKG Output**: Per-epoch DKG produces an ordered participant set
3. **Scheme Construction**: `Scheme::new(participants, polynomial, share)` preserves input order

The ordering is **consensus-critical** - all nodes must agree on the same ordering for the same epoch.

## Epoch Transitions

[Section titled “Epoch Transitions”](#epoch-transitions)

| Event          | Effect on Leader Selection                     |
| -------------- | ---------------------------------------------- |
| Epoch boundary | New validator set takes effect                 |
| DKG completion | New epoch’s participant ordering established   |
| View timeout   | Same validator set, next leader in rotation    |
| Equivocation   | Validator remains in rotation until epoch ends |

## Predictability Guarantees

[Section titled “Predictability Guarantees”](#predictability-guarantees)

### What is Predictable

[Section titled “What is Predictable”](#what-is-predictable)

1. **Next leader**: Given current view and validator set, the next N leaders are computable
2. **Leader schedule**: The full rotation schedule for an epoch is deterministic
3. **Epoch validator set**: Once DKG completes, the epoch’s validator set is fixed

### What is Not Predictable

[Section titled “What is Not Predictable”](#what-is-not-predictable)

1. **View number at future time**: Network conditions affect how quickly views advance
2. **Exact block production time**: Depends on transaction volume and leader availability
3. **Future epoch validator sets**: Depends on DKG output (derived from threshold signatures)

## Implementation Details

[Section titled “Implementation Details”](#implementation-details)

### Key Structures

[Section titled “Key Structures”](#key-structures)

```rust
// Epoch scheme provider manages per-epoch BLS schemes
pub struct EpochSchemeProvider {
    schemes: BTreeMap<Epoch, Scheme>,
    current_epoch: AtomicU64,
}


// Scheme contains the ordered participant list
pub type Scheme = bls12381_threshold::Scheme<PublicKey, MinSig>;


// Scheme exposes participants in order
impl Scheme {
    pub fn participants(&self) -> &Set<PublicKey> { ... }
}
```

### Block Header Fields

[Section titled “Block Header Fields”](#block-header-fields)

```rust
pub struct BlockHeader {
    // ... other fields ...
    pub proposer: Address,     // Block builder's address
    pub epoch: u64,            // Epoch during which block was produced
    pub view: u64,             // View/round in which block was produced
}
```

### ExecContext

[Section titled “ExecContext”](#execcontext)

The `ExecContext` passed to block building includes:

```rust
pub struct ExecContext {
    pub timestamp: u64,
    pub validator_set_id: ValidatorSetId,
    pub epoch: u64,
    pub view: u64,
    pub parent_vrf_output: Hash,
    pub proposer: Address,  // Fee recipient
}
```

## Fee Distribution

[Section titled “Fee Distribution”](#fee-distribution)

The `proposer` address in `ExecContext` receives:

* Transaction base fees
* Priority fees (if implemented)
* MEV rewards (future)

## Testing

[Section titled “Testing”](#testing)

### Unit Tests

[Section titled “Unit Tests”](#unit-tests)

1. **Determinism test**: Same inputs produce same leader selection
2. **Rotation test**: Leaders cycle through validator set correctly
3. **Epoch boundary test**: New validator set takes effect at boundary

### Integration Tests

[Section titled “Integration Tests”](#integration-tests)

1. **Multi-node agreement**: All nodes select the same leader for the same view
2. **View timeout handling**: Leader rotation continues correctly after timeouts
3. **DKG integration**: New epoch uses new participant ordering

## FAQ

[Section titled “FAQ”](#faq)

**Q: Can a validator refuse to produce blocks?**

A: Yes, but the view timeout mechanism advances to the next leader. The refusing validator loses their slot’s rewards.

**Q: How is the initial validator set ordered?**

A: By lexicographic sort of public key bytes. This ensures all nodes produce the same genesis ordering.

**Q: What if DKG produces different orderings on different nodes?**

A: This would be a consensus failure. DKG outputs are deterministic given the same inputs and messages. Nodes that produce different orderings would fork.

**Q: Can the leader selection be gamed?**

A: The rotation is deterministic but the view number progression is not fully predictable. A malicious leader cannot control who follows them, but they can observe when they will lead.

***

## Related Documentation

[Section titled “Related Documentation”](#related-documentation)

* [DKG Flow](/internals/flows/dkg/) - Distributed key generation for threshold keys
* [Finalization Flow](/internals/flows/finalization/) - Block finalization process

# Data Availability Sampling

> Erasure coding and DAS for light client verification

This document traces the complete DAS flow from block production through light client verification.

## Overview

[Section titled “Overview”](#overview)

DAS ensures block data is available without requiring light clients to download full blocks. The chain uses **Reed-Solomon erasure coding** to split blocks into chunks, then light clients **randomly sample** chunks to verify availability with high confidence.

```plaintext
Block produced --> Erasure encode --> Chunks distributed via gossip -->
Light client samples random chunks --> Verify proofs --> Accept/reject block
```

## Key Properties

[Section titled “Key Properties”](#key-properties)

| Property              | Value                                                      |
| --------------------- | ---------------------------------------------------------- |
| **Coding scheme**     | Reed-Solomon with SHA256 commitments                       |
| **Production config** | 64-of-128 shards (50% redundancy)                          |
| **Sample count**      | 30 random samples                                          |
| **Confidence**        | 99.99% (if >50% hidden, detection probability > 1 - 10^-9) |
| **Sample timeout**    | 500ms per sample                                           |
| **Total timeout**     | 5s for full DAS verification                               |

***

## 1. Erasure Coding

[Section titled “1. Erasure Coding”](#1-erasure-coding)

### BlockChunkProducer

[Section titled “BlockChunkProducer”](#blockchunkproducer)

Encodes blocks into shards:

```rust
pub struct BlockChunkProducer {
    scheme: ReedSolomon<Sha256>,
    config: CodingConfig,
}


impl BlockChunkProducer {
    pub fn encode_block(&self, block: &Block) -> Result<BlockChunkBundle, ...> {
        let bytes = borsh::to_vec(&BlockEnvelope::from(block))?;
        self.encode_bytes(&bytes)
    }


    pub fn encode_bytes(&self, data: &[u8]) -> Result<BlockChunkBundle, ...> {
        let (commitment, chunks) = self.scheme.encode(data)?;
        Ok(BlockChunkBundle { commitment, chunks })
    }
}
```

### BlockChunkVerifier

[Section titled “BlockChunkVerifier”](#blockchunkverifier)

Validates and reconstructs:

```rust
pub struct BlockChunkVerifier {
    scheme: ReedSolomon<Sha256>,
}


impl BlockChunkVerifier {
    // Verify single chunk against commitment
    pub fn check_chunk(&self, commitment: &Hash, chunk: &BlockChunk)
        -> Result<CheckedBlockChunk, ...>;


    // Reconstruct block from minimum_shards checked chunks
    pub fn decode_block(&self, commitment: Hash, chunks: Vec<CheckedBlockChunk>)
        -> Result<Block, ...>;
}
```

### Configuration

[Section titled “Configuration”](#configuration)

```rust
// Dev/test (current)
CodingConfig {
    minimum_shards: 2,   // k: minimum for reconstruction
    extra_shards: 2,     // redundancy shards
}
// Total: 4 shards


// Production target
CodingConfig {
    minimum_shards: 64,
    extra_shards: 64,
}
// Total: 128 shards, 50% availability threshold
```

### Chunk Format

[Section titled “Chunk Format”](#chunk-format)

```rust
pub type BlockChunk = <ReedSolomon<Sha256> as Scheme>::Shard;


pub struct BlockChunkBundle {
    pub commitment: Hash,        // Merkle root of all chunks
    pub chunks: Vec<BlockChunk>, // n encoded shards with proofs
}
```

Each chunk includes a Merkle proof allowing verification against the commitment.

***

## 2. DA Commitment in Block Headers

[Section titled “2. DA Commitment in Block Headers”](#2-da-commitment-in-block-headers)

During block construction, the DA commitment is computed and included in the header:

```rust
// In build_block_preview()
let data_availability_root =
    crate::data_availability::compute_default_da_commitment(&execution)
        .unwrap_or_else(|e| {
            tracing::warn!(error = ?e, "failed to compute DA commitment");
            Hash::empty()
        });


let header = BlockHeader {
    // ...
    data_availability_root,  // Merkle root of erasure-coded chunks
    // ...
};
```

```rust
pub struct BlockHeader {
    pub height: BlockHeight,
    pub parent_hash: Hash,
    pub state_root: Hash,
    pub exec_payload_root: Hash,
    pub data_availability_root: Hash,  // <-- DAS commitment
    pub timestamp: u64,
    // ...
}
```

This commitment is signed by consensus, binding validators to the availability of the data.

***

## 3. Chunk Distribution (Gossip)

[Section titled “3. Chunk Distribution (Gossip)”](#3-chunk-distribution-gossip)

### Gossip Message Types

[Section titled “Gossip Message Types”](#gossip-message-types)

```rust
pub enum ChunkGossipMessage {
    Request(ChunkRequest),
    Response(ChunkResponse),
    Announce(ChunkAnnounce),
}


pub struct ChunkAnnounce {
    pub block_hash: Hash,
    pub commitment: Hash,
    pub available_indices: Vec<u16>,
    pub total_chunks: u16,
}


pub struct ChunkRequest {
    pub block_hash: Hash,
    pub indices: Vec<u16>,
}


pub struct ChunkResponse {
    pub block_hash: Hash,
    pub chunks: Vec<(u16, Vec<u8>)>,  // (index, encoded_chunk)
}
```

### Application Actor Integration

[Section titled “Application Actor Integration”](#application-actor-integration)

After block finalization:

```rust
// Encode block into chunks
let bundle = self.chunk_producer.encode_block(&block)?;


// Cache for serving via gossip
self.pending_chunks.put(block_hash, bundle);


tracing::debug!(
    block_hash = %block_hash,
    commitment = %bundle.commitment,
    num_chunks = bundle.chunks.len(),
    "cached block chunks for DA"
);
```

***

## 4. Light Client DAS Verification

[Section titled “4. Light Client DAS Verification”](#4-light-client-das-verification)

### Sampling Configuration

[Section titled “Sampling Configuration”](#sampling-configuration)

```rust
pub struct DasSamplingConfig {
    pub sample_count: u16,        // Default: 30
    pub min_valid_samples: u16,   // Default: 0 (all must be valid)
    pub max_invalid_samples: u16, // Default: 0 (strict mode)
    pub sample_timeout: Duration, // Default: 500ms
    pub total_timeout: Duration,  // Default: 5s
}
```

### Random Index Generation

[Section titled “Random Index Generation”](#random-index-generation)

```rust
pub fn generate_random_indices(
    sample_count: u16,
    total_chunks: u16,
    entropy: &[u8; 32],
) -> Vec<u16> {
    // SHA256-based PRNG seeded with entropy
    // entropy = block_hash XOR local_randomness
    // Generates unique random indices without replacement
}
```

### Sample Verification

[Section titled “Sample Verification”](#sample-verification)

```rust
pub fn verify_sample(
    verifier: &BlockChunkVerifier,
    commitment: Hash,
    index: u16,
    chunk_bytes: &[u8],
) -> Result<(), DasError> {
    let chunk = decode_chunk(chunk_bytes)?;
    verifier.check_chunk(&commitment, &chunk)?;
    Ok(())
}
```

### Main Verification Function

[Section titled “Main Verification Function”](#main-verification-function)

```rust
pub async fn verify_availability<F: ChunkFetcher>(
    config: &DasSamplingConfig,
    coding_config: &CodingConfig,
    block_hash: Hash,
    commitment: Hash,
    entropy: &[u8; 32],
    fetcher: &F,
    verifier: &BlockChunkVerifier,
) -> DasResult {
    let total_chunks = coding_config.total_shards();
    let indices = generate_random_indices(config.sample_count, total_chunks, entropy);


    let mut outcomes = Vec::new();


    for index in indices {
        match timeout(config.sample_timeout, fetcher.fetch_chunk(...)).await {
            Ok(Ok(bytes)) => {
                match verify_sample(verifier, commitment, index, &bytes) {
                    Ok(()) => outcomes.push(SampleOutcome::Valid),
                    Err(_) => outcomes.push(SampleOutcome::Invalid),
                }
            }
            Ok(Err(_)) => outcomes.push(SampleOutcome::Invalid),
            Err(_) => outcomes.push(SampleOutcome::Timeout),
        }
    }


    aggregate_das_results(&outcomes, config)
}
```

### Result Aggregation

[Section titled “Result Aggregation”](#result-aggregation)

```rust
pub enum DasResult {
    Available,
    Unavailable { valid: u16, invalid: u16, timeout: u16 },
    Timeout,
}


pub fn aggregate_das_results(
    outcomes: &[SampleOutcome],
    config: &DasSamplingConfig,
) -> DasResult {
    let valid = outcomes.iter().filter(|o| matches!(o, Valid)).count();
    let invalid = outcomes.iter().filter(|o| matches!(o, Invalid)).count();
    let timeout = outcomes.iter().filter(|o| matches!(o, Timeout)).count();


    if invalid > config.max_invalid_samples as usize {
        return DasResult::Unavailable { ... };
    }
    if valid < config.min_valid_samples as usize {
        return DasResult::Unavailable { ... };
    }


    DasResult::Available
}
```

***

## 5. Block Recovery

[Section titled “5. Block Recovery”](#5-block-recovery)

When a full block is needed (not just availability verification):

### ChunkRecoveryHandle

[Section titled “ChunkRecoveryHandle”](#chunkrecoveryhandle)

```rust
pub struct ChunkRecoveryHandle {
    config: CodingConfig,
    request_tx: mpsc::Sender<ChunkGossipCommand>,
    request_timeout: Duration,
}


impl ChunkRecoveryHandle {
    pub async fn recover_block(&self, block_hash: Hash) -> Result<Block, ...> {
        // 1. Fetch chunk announce
        let announce = self.fetch_announce(block_hash).await?;


        // 2. Validate config matches
        if announce.total_chunks != self.config.total_shards() {
            return Err(ChunkRecoveryError::ConfigMismatch);
        }


        // 3. Fetch and decode
        recover_block(block_hash, announce.commitment, ...).await
    }
}
```

### Recovery Function

[Section titled “Recovery Function”](#recovery-function)

```rust
pub async fn recover_block<F: ChunkFetcher>(
    block_hash: Hash,
    commitment: Hash,
    fetcher: &F,
    verifier: &BlockChunkVerifier,
    config: &CodingConfig,
) -> Result<Block, ChunkRecoveryError> {
    let mut checked_chunks = Vec::new();


    // Fetch all chunks (tolerating some failures)
    for index in 0..config.total_shards() {
        match fetcher.fetch_chunk(block_hash, commitment, index).await {
            Ok(bytes) => {
                if let Ok(chunk) = decode_chunk(&bytes) {
                    if let Ok(checked) = verifier.check_chunk(&commitment, &chunk) {
                        checked_chunks.push(checked);
                    }
                }
            }
            Err(_) => continue,  // Skip failed fetches
        }


        // Early exit if we have enough
        if checked_chunks.len() >= config.minimum_shards as usize {
            break;
        }
    }


    // Reconstruct
    verifier.decode_block(commitment, checked_chunks)
}
```

***

## 6. Sequence Diagram

[Section titled “6. Sequence Diagram”](#6-sequence-diagram)

```plaintext
BLOCK PRODUCTION (Validator)
    |
    +-- Execute transactions
    |   +-- ExecutionPayload
    |
    +-- compute_default_da_commitment(payload)
    |   +-- ReedSolomon::encode() -> commitment + chunks
    |
    +-- BlockHeader { data_availability_root: commitment }
    |
    +-- Consensus signs block
    |
    +-- BlockChunkProducer.encode_block()
        +-- Cache in pending_chunks[block_hash]




CHUNK GOSSIP (P2P)
    |
    +-- Node A                          Node B
    |     |                               |
    |     | ChunkGossipCommand::Announce  |
    |     |<------------------------------|
    |     |                               |
    |     | ChunkAnnounce {               |
    |     |   commitment,                 |
    |     |   available_indices: [0..n],  |
    |     |   total_chunks: n             |
    |     | }                             |
    |     |------------------------------>|
    |     |                               |
    |     | ChunkGossipCommand::Chunk(i)  |
    |     |<------------------------------|
    |     |                               |
    |     | encoded_chunk[i]              |
    |     |------------------------------>|




LIGHT CLIENT DAS VERIFICATION
    |
    +-- Receive BlockHeader with data_availability_root
    |
    +-- generate_random_indices(30, total_chunks, entropy)
    |   +-- entropy = block_hash XOR local_randomness
    |
    +-- For each sample index i:
    |   |
    |   +-- fetch_chunk(block_hash, commitment, i)
    |   |   +-- timeout: 500ms
    |   |
    |   +-- decode_chunk(bytes)
    |   |
    |   +-- verify_sample(verifier, commitment, i, chunk)
    |       +-- check Merkle proof against commitment
    |
    +-- aggregate_das_results()
    |   +-- valid >= min_valid_samples?
    |   +-- invalid <= max_invalid_samples?
    |
    +-- DasResult::Available -> Accept block
        DasResult::Unavailable -> Reject block




BLOCK RECOVERY (Full node needs block data)
    |
    +-- fetch_announce(block_hash)
    |   +-- Get commitment + total_chunks
    |
    +-- For index in 0..total_chunks:
    |   +-- fetch_chunk(index)
    |   +-- decode_chunk + check_chunk
    |   +-- Collect until >= minimum_shards
    |
    +-- verifier.decode_block(commitment, checked_chunks)
        +-- ReedSolomon::decode() -> Block
```

***

## 7. Statistical Guarantee

[Section titled “7. Statistical Guarantee”](#7-statistical-guarantee)

With 30 random samples and 50% availability threshold:

* If adversary hides **>50%** of chunks, the block is **unrecoverable**

* Probability light client **fails to detect** hidden data:

  * P(all 30 samples hit available chunks) = (0.5)^30 \~ **10^-9**
  * Detection probability: **>99.99999%**

This means an adversary cannot hide data without being detected by light clients with overwhelming probability.

***

## Related Documentation

[Section titled “Related Documentation”](#related-documentation)

* [Light Clients](/concepts/light-clients/) - Light client architecture
* [Finalization Flow](/internals/flows/finalization/) - Block finalization with BLS signatures

# Finality Model

> Deterministic finality in the BFT consensus system

## Summary

[Section titled “Summary”](#summary)

The chain uses a permissioned BFT consensus with a small authority set (initially three). Finality is deterministic: once a block is committed by quorum, it is final and will never be reverted. The system prioritizes safety over liveness: during partitions it halts rather than reorg.

## Definitions

[Section titled “Definitions”](#definitions)

* **Authority**: A permissioned validator participating in BFT voting.
* **Quorum**: At least two-thirds of authorities by count (e.g., 2-of-3).
* **Commit**: A block is committed when the BFT protocol produces a commit certificate from a quorum of authorities for that block.

## Finality Guarantee

[Section titled “Finality Guarantee”](#finality-guarantee)

Committed = Final

A block that reaches quorum commit is **deterministically final**. Once committed, it will not be replaced by any alternative chain. There are no probabilistic confirmations or reorg windows.

## Failure and Partition Behavior

[Section titled “Failure and Partition Behavior”](#failure-and-partition-behavior)

Safety Over Liveness

The chain prioritizes **safety over liveness**. During network partitions or authority outages, the chain halts rather than producing potentially conflicting blocks.

* If quorum cannot be reached (e.g., network partition, authority outage), the chain halts and no new blocks are committed.
* If quorum remains intact, the chain continues to make progress and commits remain final.
* There are no probabilistic confirmations or reorg windows for committed blocks.

## Operational Notes (What to Monitor)

[Section titled “Operational Notes (What to Monitor)”](#operational-notes-what-to-monitor)

Monitoring Checklist

* **Latest committed height** and time since last commit (stalls indicate quorum loss)
* **Quorum participation**: which authorities signed the most recent commit certificate
* **Authority set changes** and epoch transitions, if any are scheduled

## Upgrade Path: PoS / Stake-Weighted Validators (stINDEX) Planned

[Section titled “Upgrade Path: PoS / Stake-Weighted Validators (stINDEX) ”Planned](#upgrade-path-pos--stake-weighted-validators-stindex)

The authority set can evolve into a stake-weighted validator set using stINDEX for weights. The quorum threshold becomes “at least two-thirds of stake weight” instead of “two-thirds of authorities,” but the external promise remains the same: **committed = final**. Integrators should continue to treat committed blocks as irreversible regardless of the validator weighting scheme.

## Related

[Section titled “Related”](#related)

[Consensus ](/architecture/consensus/)Simplex BFT protocol details

[Light Clients ](/concepts/light-clients/)Finality proof verification

[Finalization Flow ](/internals/flows/finalization/)Block commit process

[Architecture ](/architecture/overview/)System diagram

# Gas and Fees

> Gas fee distribution policy and fee breakdown

This document defines the policy for distributing transaction fees and provides implementation guidance for the execution layer.

## Overview

[Section titled “Overview”](#overview)

When a transaction executes, the payer is debited fees based on gas consumption. This policy defines where those fees go after execution completes.

## Current State

[Section titled “Current State”](#current-state)

* **Fee Debit**: Payer is debited `gas_limit` units at transaction start.
* **Gas Refund**: Unused gas (`gas_limit - gas_used`) is refunded to payer.
* **Consumed Fees**: `gas_used` units are currently **implicitly burned** (credited nowhere).

### Existing Infrastructure (Unused)

[Section titled “Existing Infrastructure (Unused)”](#existing-infrastructure-unused)

* `Validator.fee_recipient: Address` - per-validator fee destination
* `BlockHeader.proposer: Address` - block producer identity
* `FeeIntentV1.priority_tip` - optional tip field (currently ignored)

## Policy Decision

[Section titled “Policy Decision”](#policy-decision)

### Phase 1: Proposer-Takes-All

[Section titled “Phase 1: Proposer-Takes-All”](#phase-1-proposer-takes-all)

**All consumed fees go to the block proposer.**

```plaintext
fee_distribution = gas_used -> proposer.fee_recipient
```

#### Rationale

[Section titled “Rationale”](#rationale)

1. **Simplicity**: Single destination, no splitting logic.
2. **Validator Incentive**: Directly rewards block producers.
3. **Uses Existing Fields**: `fee_recipient` and `proposer` are already in place.
4. **Greenfield Flexibility**: Can evolve to burn/split model before mainnet.

#### Implementation

[Section titled “Implementation”](#implementation)

**Phase 1 Simplification**: Use `BlockHeader.proposer` directly as fee destination. No validator set lookup required - validators can set their proposer address to any address they control.

Requires adding `proposer` to `VmBlockEnv` and passing through `apply_transaction`:

```rust
// In VmBlockEnv (mod.rs:462)
pub(crate) struct VmBlockEnv {
    // ... existing fields ...
    pub(crate) proposer: Address,  // Fee recipient for this block
}


// In apply_transaction_inner, after gas refund (line ~2569):
// 6. Credit consumed gas to block proposer
let consumed = used.gas_used;
if consumed > 0 {
    self.state.credit_asset(&block_env.proposer, fee_asset_id, consumed);
}
```

**Note**: Proposer address comes from `block.header.proposer` in `apply_block` and from `ExecContext` or parent proposer logic in `build_block`.

### Phase 2 (Future): EIP-1559 Style Planned

[Section titled “Phase 2 (Future): EIP-1559 Style ”Planned](#phase-2-future-eip-1559-style)

When ready for mainnet, consider:

```plaintext
base_fee -> BURN (or treasury)
priority_tip -> proposer.fee_recipient
```

This requires:

* Base fee calculation per block
* Priority tip extraction from `FeeIntentV1`
* Burn destination (null address or explicit)

**Deferred until `DEPLOYED` flag is set in CLAUDE.md.**

## Configuration

[Section titled “Configuration”](#configuration)

### Fee Recipient Resolution (Phase 1)

[Section titled “Fee Recipient Resolution (Phase 1)”](#fee-recipient-resolution-phase-1)

**Simple approach**: Use `BlockHeader.proposer` directly as the fee destination.

1. Read `block.header.proposer` (available during block execution).
2. Credit consumed fees to that address.
3. No validator set lookup required.

**Why this works**: Validators choose their proposer address when producing blocks. If they want fees sent to a different address, they set that address as proposer.

**Future Phase 2**: Add `Validator.fee_recipient` lookup if needed for separation of signing identity vs payment destination.

### Multi-Asset Fees

[Section titled “Multi-Asset Fees”](#multi-asset-fees)

Fee distribution respects the fee asset specified in `FeeIntentV1`:

* Default: native token (asset ID 0)
* Custom: any registered asset ID

## Metrics and Events

[Section titled “Metrics and Events”](#metrics-and-events)

### Metrics

[Section titled “Metrics”](#metrics)

| Metric                   | Description                                  |
| ------------------------ | -------------------------------------------- |
| `fees_distributed_total` | Total fees credited to proposers             |
| `fees_burned_total`      | Total fees with no recipient (burned)        |
| `fee_distribution_count` | Number of transactions with fee distribution |

### Events

[Section titled “Events”](#events)

```plaintext
FeeDistributed { recipient: Address, amount: u64, asset_id: AssetId, tx_hash: Hash }
FeeBurned { amount: u64, asset_id: AssetId, tx_hash: Hash }
```

## Test Coverage

[Section titled “Test Coverage”](#test-coverage)

1. **Happy Path**: Tx executes, proposer receives `gas_used` units.
2. **Full Refund**: Tx uses 0 gas, proposer receives 0 (all refunded).
3. **No Recipient**: Validator has no `fee_recipient`, fees burned.
4. **Multi-Asset**: Fee paid in non-native asset, distributed correctly.
5. **Revert**: Tx reverts, gas still consumed, fees still distributed.

## Security Considerations

[Section titled “Security Considerations”](#security-considerations)

1. **No Double-Credit**: Ensure fee distribution happens exactly once per tx.
2. **Overflow**: Use saturating arithmetic for fee calculations.
3. **Asset Consistency**: Distribute same asset that was debited.
4. **Validator Lookup**: Cache validator set per block to avoid inconsistency.

## Migration Path

[Section titled “Migration Path”](#migration-path)

1. **Pre-Mainnet**: Proposer-takes-all, simple accounting.
2. **Post-Mainnet**: Governance vote to enable EIP-1559 style.
3. **Treasury Option**: Add treasury address for protocol funding.

## Client Access: TxFeeBreakdown

[Section titled “Client Access: TxFeeBreakdown”](#client-access-txfeebreakdown)

After transaction execution (included or simulated), clients receive a `TxFeeBreakdown` in the `ExecutionOutcome.fee` field. This provides full visibility into gas/fee accounting:

### Core Type (`src/core/mod.rs`)

[Section titled “Core Type (src/core/mod.rs)”](#core-type-srccoremodrs)

```rust
pub struct TxFeeBreakdown {
    /// Gas units the sender authorized (from TxBodyV1.gas_limit).
    pub gas_limit: u64,
    /// Gas units actually consumed by execution.
    pub gas_used: u64,
    /// Effective gas price applied (native units per gas unit).
    pub effective_gas_price: u128,
    /// Maximum fee the sender was willing to pay (from FeeIntent).
    pub max_fee: u128,
    /// Priority tip offered above base fee (from FeeIntent).
    pub priority_tip: u128,
    /// Total fee actually charged to the payer.
    pub total_fee_paid: u128,
    /// Asset used for fee payment (e.g. "native").
    pub fee_asset: Option<String>,
}
```

### RPC Type (`src/rpc_client.rs`)

[Section titled “RPC Type (src/rpc\_client.rs)”](#rpc-type-srcrpc_clientrs)

The RPC layer converts `u128` fields to strings for JSON compatibility:

```rust
pub struct TxFeeBreakdown {
    pub gas_limit: u64,
    pub gas_used: u64,
    pub effective_gas_price: String,  // string-encoded u128
    pub max_fee: String,
    pub priority_tip: String,
    pub total_fee_paid: String,
    pub fee_asset: Option<String>,
}
```

### Usage Example

[Section titled “Usage Example”](#usage-example)

```rust
// Via RPC client
if let Some(receipt) = client.get_transaction_receipt(tx_hash)? {
    if let Some(fee) = receipt.fee.as_ref() {
        println!("Gas used: {} / {}", fee.gas_used, fee.gas_limit);
        println!(
            "Total fee: {} {}",
            fee.total_fee_paid,
            fee.fee_asset.clone().unwrap_or_default()
        );
    }


    // Via TransactionReceipt convenience fields
    println!("Gas: {}/{}", receipt.gas_used, receipt.gas_limit);
    println!(
        "Fee: {} at {} per gas",
        receipt.total_fee_paid, receipt.effective_gas_price
    );
}
```

### Behavior Notes

[Section titled “Behavior Notes”](#behavior-notes)

* **VM transactions**: `gas_used` reflects actual consumption; `total_fee_paid = gas_used * effective_gas_price`
* **Simple transfers**: `gas_used` may be 0; `total_fee_paid = max_fee` (flat fee, no refund)
* **v1 engine**: `effective_gas_price` is always 1 (1:1 unit pricing)
* **Simulations**: Fee breakdown is populated but no actual fee is charged

## Related

[Section titled “Related”](#related)

* [Execution](/architecture/execution/) - Transaction processing
* [RPC API](/reference/rpc-api/) - Fee estimation endpoints
* [Gas Schedule](/reference/gas-schedule/) - Operation costs
* [Ashen SDK](/contracts/ashen-sdk/) - Gas metering in contracts

## References

[Section titled “References”](#references)

* [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559) - Fee market change
* [Solana Fee Distribution](https://docs.solana.com/transaction_fees)
* `src/core/execution/mod.rs` - Fee handling implementation
* `src/core/validator_set.rs` - Validator fee\_recipient field

# Glossary

> Alphabetical list of common terms used in the chain

Alphabetical list of common terms used in this codebase.

| Term              | Definition                                                            | Where Used                                                       |
| ----------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| ABI               | Contract interface encoding rules for calldata and return values.     | `crates/vm-spec`, `crates/contract-sdk`, `contracts/ashen-sdk`   |
| Access List       | Declared storage keys/ranges to pre-warm for deterministic execution. | `crates/vm-runtime`, `crates/vm-spec`                            |
| AOT               | Ahead-of-time compilation tier for contract execution.                | `crates/vm-aot`, `crates/vm-runtime`                             |
| BLS               | Boneh-Lynn-Shacham signatures used for validator keys.                | `src/consensus`, `crates/keystore`                               |
| Borsh             | Binary serialization format used for on-chain types.                  | `crates/contract-sdk`, `vm-types`, `contracts/*`                 |
| BMT               | Binary Merkle Tree used for authenticated data structures.            | `src/storage`                                                    |
| Calldata          | Input bytes passed to a contract call.                                | `crates/vm-runtime`, `crates/contract-sdk`, `crates/contract-rt` |
| Checkpoint        | Persisted height used for fast sync and pruning.                      | `src/consensus`, `src/application`                               |
| DAP               | Debug Adapter Protocol for stepping through contract execution.       | [Debugging Guide](/guides/debugging/)                            |
| DKG               | Distributed key generation for validator crypto material.             | `src/consensus`                                                  |
| ECDSA (ecrecover) | Signature recovery syscall for secp256k1.                             | `crates/vm-spec`, `crates/vm-precompiles`                        |
| ECVRF             | Verifiable random function (ed25519) syscall.                         | `crates/vm-spec`, `crates/vm-precompiles`                        |
| Epoch             | Consensus time period for validator set changes.                      | `src/consensus`, `crates/contract-sdk::host`                     |
| Gas Schedule      | Table of per-opcode/syscall costs.                                    | `crates/vm-gas`, `crates/vm-runtime`                             |
| IDL               | Interface definition language for contract ABIs.                      | `contracts/*/*.idl`, `crates/idl-abi-gen`, `crates/vm-tooling`   |
| JIT               | Just-in-time compilation tier for contract execution.                 | `crates/vm-jit`, `crates/vm-runtime`                             |
| Keccak256         | Hash used for event selectors and EVM-compatible ops.                 | `crates/vm-precompiles`, `contracts/ashen-sdk/crypto.zig`        |
| Mempool           | Pending transaction pool.                                             | `src/application`, `src/consensus`                               |
| MMR               | Merkle Mountain Range used in QMDB for append-only logs.              | `src/storage`                                                    |
| Precompile        | Native host implementation of a crypto/utility function.              | `crates/vm-precompiles`, `crates/vm-runtime`                     |
| QMDB              | Authenticated append-only database with ordered keys.                 | `src/storage/state`                                              |
| Reentrancy Guard  | Contract-level protection against reentrant calls.                    | `contracts/ashen-sdk/guards.zig`, `crates/contract-sdk`          |
| Snapshot          | Captured VM/host state for rollback or testing.                       | `crates/vm-runtime/src/journal.rs`, `crates/vm-test-harness`     |
| State Root        | Merkle root commitment to account and contract state.                 | `src/storage`, `src/core`                                        |
| Syscall           | VM-to-host call interface.                                            | `crates/vm-spec`, `crates/vm-runtime/src/syscalls.rs`            |
| TIBE              | Threshold identity-based encryption used in consensus schemes.        | `src/consensus`                                                  |
| Tiered Execution  | Interpreter/JIT/AOT stack used by the runtime.                        | `crates/vm-runtime`, `crates/vm-interpreter`                     |
| Transaction (Tx)  | Signed payload applied to chain state.                                | `src/core`, `src/application`                                    |
| VM                | Deterministic RISC-V virtual machine for contracts.                   | `crates/vm-*`                                                    |
| Warm Storage Keys | Keys preloaded into the storage cache for a call.                     | `crates/vm-runtime`, `crates/vm-spec`                            |

# Light Clients

> Light client verification and state proofs

This document traces the complete light client flow from initialization through state verification, including finality proofs, validator set transitions, state proofs, and historical block verification.

## Overview

[Section titled “Overview”](#overview)

Light clients verify blockchain state **without executing transactions**. They rely on:

1. **Finality proofs** - BLS threshold signatures proving block finalization
2. **Merkle proofs** - Cryptographic proofs for state values
3. **MMR proofs** - Historical block inclusion proofs
4. **DAS** - Data availability sampling (optional)

```plaintext
Initialize with trusted context --> Verify finality proofs -->
Track validator transitions --> Query state with proofs --> Verify historical blocks
```

## Light Client State Machine

[Section titled “Light Client State Machine”](#light-client-state-machine)

### State Structure

[Section titled “State Structure”](#state-structure)

```rust
pub struct LightClientState {
    pub context: LightClientContext,           // Current trusted validator set
    pub pending_update: Option<PendingUpdate>, // Announced validator set change
    pub current_epoch: u64,
    pub latest_height: u64,
}


pub struct LightClientContext {
    pub validator_set: ValidatorSet,
    pub aggregate_key_proof: ValidatorProof,   // Merkle proof for aggregate key
    pub version: u32,
}
```

### Initialization

[Section titled “Initialization”](#initialization)

```rust
let context = LightClientContext {
    validator_set: trusted_validator_set,
    aggregate_key_proof: build_aggregate_key_proof(&validator_set),
    version: validator_set_version,
};


let state = LightClientState::new(context, initial_epoch, initial_height);
```

## Finality Proof Verification

[Section titled “Finality Proof Verification”](#finality-proof-verification)

### Three-Step Verification

[Section titled “Three-Step Verification”](#three-step-verification)

```rust
pub fn verify_finality_proof(
    proof: &FinalityProof,
    ctx: &LightClientContext,
) -> Result<(), LightClientError> {
    // Step 1: Validator set commitment
    let root = ctx.commitment_root();
    if root != proof.header.validator_set_id.id {
        return Err(LightClientError::ValidatorSetIdMismatch);
    }


    // Step 2: Aggregate key Merkle proof
    if ctx.aggregate_key_proof.leaf_index != 0 {
        return Err(LightClientError::InvalidMembershipProof);
    }
    if !ctx.aggregate_key_proof.verify(&root) {
        return Err(LightClientError::InvalidMembershipProof);
    }


    // Step 3: BLS signature verification
    if !proof.verify(&ctx.validator_set.aggregate_bls_pubkey) {
        return Err(LightClientError::InvalidSignature);
    }


    Ok(())
}
```

### FinalityProof Structure

[Section titled “FinalityProof Structure”](#finalityproof-structure)

```rust
pub struct FinalityProof {
    pub header: BlockHeader,
    pub epoch: u64,
    pub view: u64,
    pub parent_view: u64,
    pub key_version: u32,
    pub certificate: FinalityCertificateBytes,  // Threshold BLS signature
}
```

## Validator Set Commitment

[Section titled “Validator Set Commitment”](#validator-set-commitment)

### Merkle Tree Structure

[Section titled “Merkle Tree Structure”](#merkle-tree-structure)

```plaintext
                    [Root]
                   /      \
        [Internal]          [Internal]
        /        \          /        \
[AggKey Leaf] [Val 0]  [Val 1]    [Val 2]
```

### Commitment Root Computation

[Section titled “Commitment Root Computation”](#commitment-root-computation)

```rust
pub fn commitment_root(&self) -> Hash {
    let mut leaves = Vec::with_capacity(self.validators.len() + 1);


    // Leaf 0: aggregate BLS key
    leaves.push(self.aggregate_key_leaf_hash());


    // Leaves 1..n: individual validators
    for i in 0..self.validators.len() {
        leaves.push(self.validator_leaf_hash(i)?);
    }


    merkle_root(&leaves)
}
```

## Validator Set Transitions

[Section titled “Validator Set Transitions”](#validator-set-transitions)

### Announcement Phase

[Section titled “Announcement Phase”](#announcement-phase)

When a block announces a validator set change:

```rust
pub fn process_finality_proof(&mut self, proof: &FinalityProof) -> Result<()> {
    // Verify against current context
    verify_finality_proof(proof, &self.context)?;


    // Check for validator set change announcement
    if proof.header.next_validator_set_id != proof.header.validator_set_id {
        self.pending_update = Some(PendingUpdate {
            next_validator_set_id: proof.header.next_validator_set_id.clone(),
            announced_at_epoch: proof.header.epoch,
            announced_at_height: proof.header.height,
        });
    }


    self.current_epoch = proof.header.epoch;
    self.latest_height = proof.header.height;
    Ok(())
}
```

## State Proof Verification

[Section titled “State Proof Verification”](#state-proof-verification)

### Proof Types

[Section titled “Proof Types”](#proof-types)

| Proof Type           | Purpose                                  |
| -------------------- | ---------------------------------------- |
| `SlotProof`          | Storage slot existence/non-existence     |
| `PositionProof`      | Merkle position in state tree            |
| `NonMembershipProof` | Key doesn’t exist (left/right neighbors) |
| `ContractQmdbProof`  | Full contract state proof                |

### Verification Flow

[Section titled “Verification Flow”](#verification-flow)

1. Validate QMDB ops sequence
2. Recompute state root from ops
3. Verify bounded proof
4. Verify slot proof (if present)

## MMR for Historical Proofs

[Section titled “MMR for Historical Proofs”](#mmr-for-historical-proofs)

### Structure

[Section titled “Structure”](#structure)

```rust
pub struct FinalizedMMR {
    leaves: Vec<FinalizedEntry>,
    height_index: BTreeMap<u64, u64>,  // height -> position
}


pub struct FinalizedMmrProof {
    pub entry: FinalizedEntry,
    pub leaf_position: u64,
    pub leaf_count: u64,
    pub siblings: Vec<([u8; 32], bool)>,  // (hash, is_left_of_path)
}
```

### Proof Verification

[Section titled “Proof Verification”](#proof-verification)

```rust
pub fn verify(&self, expected_root: &[u8; 32]) -> bool {
    let mut current = leaf_hash(&self.entry);


    for (sibling, is_left) in &self.siblings {
        current = if *is_left {
            sha256(concat![b"mmr_internal_v1", sibling, &current])
        } else {
            sha256(concat![b"mmr_internal_v1", &current, sibling])
        };
    }


    current == *expected_root
}
```

## RPC Endpoints

[Section titled “RPC Endpoints”](#rpc-endpoints)

| Method                              | Purpose                          |
| ----------------------------------- | -------------------------------- |
| `NodeRpcV1.finality_proof`          | Get finality proof for a height  |
| `NodeRpcV1.light_client_context`    | Get validator set context        |
| `NodeRpcV1.state_proof`             | Get state proof for address/slot |
| `NodeRpcV1.finalized_history_root`  | Get current MMR root             |
| `NodeRpcV1.finalized_history_proof` | Get MMR inclusion proof          |

## CLI Verification

[Section titled “CLI Verification”](#cli-verification)

```bash
# Verify a block is in the finalized history
node verify --height 100


# Verify with a specific RPC endpoint
node verify --height 100 --rpc-url http://localhost:3030


# Output as JSON (for scripting)
node verify --height 100 --format json
```

## Verification Invariants

[Section titled “Verification Invariants”](#verification-invariants)

| Invariant             | Check                                             |
| --------------------- | ------------------------------------------------- |
| **Validator Set**     | `commitment_root() == header.validator_set_id.id` |
| **Aggregate Key**     | Leaf index 0, correct hash, valid Merkle path     |
| **BLS Signature**     | Certificate verifies with aggregate key           |
| **Epoch Boundary**    | Transitions only at `epoch > announced_epoch`     |
| **Version Monotonic** | New version >= announced version                  |
| **QMDB Ordering**     | Positions 0 to last\_loc in sequence              |
| **Leaf Digests**      | Preimage hash matches proof leaf                  |
| **MMR Path**          | Siblings form valid path to root                  |

## Related

[Section titled “Related”](#related)

* [Finality](/concepts/finality/) - Finality guarantees
* [Consensus](/architecture/consensus/) - BLS threshold signing
* [Storage](/architecture/storage/) - Merkle tree structure
* [Data Availability](/concepts/data-availability/) - DAS for light clients
* [RPC API](/reference/rpc-api/) - Proof endpoints

# Private Mempool (Sealed Transactions)

> Encrypted transactions that stay private until inclusion

## Overview

[Section titled “Overview”](#overview)

Ashen supports a **private mempool** using **sealed transactions**. A sealed transaction is encrypted client-side and remains unreadable to validators until the network collectively decrypts it at inclusion time. This protects users from mempool sniffing and reduces the risk of front‑running.

At a high level:

1. The client encrypts the transaction using **threshold identity‑based encryption (TIBE)**.
2. The encrypted payload enters the mempool; validators can’t read it.
3. When a sealed transaction is selected for a block, validators collaborate to decrypt it and execute it deterministically.

## Why Sealed Transactions

[Section titled “Why Sealed Transactions”](#why-sealed-transactions)

* **Privacy**: Transactions aren’t visible in the mempool.
* **Fairness**: Validators can’t reorder based on contents.
* **Safer trading**: Reduced MEV‑style extraction from pending txs.

## How It Works (Conceptual)

[Section titled “How It Works (Conceptual)”](#how-it-works-conceptual)

* **Encryption**: The client encrypts calldata with the current epoch’s TIBE public parameters.
* **Mempool storage**: The sealed payload is stored and gossiped like normal txs, but contents are opaque.
* **Decryption at inclusion**: Validators submit decryption shares; once enough shares are collected, the tx is revealed and executed.

## Ordering and Selection

[Section titled “Ordering and Selection”](#ordering-and-selection)

Sealed transactions are **FIFO ordered** by arrival in the mempool (design goal). This avoids content‑based ordering since the contents are not visible.

## Limitations and Trade‑offs

[Section titled “Limitations and Trade‑offs”](#limitations-and-tradeoffs)

* **No mempool preview**: Clients cannot inspect sealed tx contents once submitted.
* **Simulation limits**: Full simulation requires access to the plaintext transaction; clients should simulate locally before sealing.
* **Decryption latency**: Inclusion requires collecting threshold shares.

## Related Docs

[Section titled “Related Docs”](#related-docs)

* Detailed protocol flow: `/internals/flows/sealed-transactions/`
* Txpool policy (sealed limits): `/internals/txpool-policy/`
* Intro overview: `/getting-started/introduction/`

# Ashen SDK

> Zig SDK for smart contracts

The Ashen SDK provides Zig modules for writing smart contracts that run on Ashen’s [RISC-V execution](/architecture/execution/) environment.

## Quick Start

[Section titled “Quick Start”](#quick-start)

```zig
const sdk = @import("ashen-sdk");


export fn _start(calldata_ptr: [*]const u8, calldata_len: usize) sdk.ByteSlice {
    sdk.heap.reset();
    const calldata = if (calldata_len == 0) &[_]u8{} else calldata_ptr[0..calldata_len];
    // Your contract logic here
    return sdk.ByteSlice.from(result);
}


pub const panic = sdk.panic;
```

Tip

Always call `sdk.heap.reset()` at the start of your entry point to clear the bump allocator.

## Modules

[Section titled “Modules”](#modules)

* Storage

  **`sdk.storage`** - Persistent key-value storage

  ```zig
  const storage = sdk.storage;


  // Read/write raw bytes
  const value = storage.read(key);
  storage.write(key, data);


  // Typed helpers for u128
  const balance = storage.readU128(key);
  storage.writeU128(key, amount);
  ```

* Context

  **`sdk.context`** - Block and transaction context

  ```zig
  const ctx = sdk.context;


  const sender = ctx.caller();      // Immediate caller
  const tx_origin = ctx.origin();   // Transaction originator
  const height = ctx.blockHeight();
  const attached = ctx.value();     // Attached value
  ```

* Crypto

  **`sdk.crypto`** - Hash functions

  ```zig
  const crypto = sdk.crypto;


  const k_hash = crypto.keccak256(data);
  const s_hash = crypto.sha256(data);
  const b_hash = crypto.blake3(data);
  ```

* Events

  **`sdk.events`** - Typed event emission

  ```zig
  const events = sdk.events;


  // Define event signature
  const Transfer = events.define("Transfer(address,address,uint256)");


  // Emit with indexed topics
  Transfer.emit2(from, to, events.toTopicU128(amount), &[_]u8{});
  ```

* Math

  **`sdk.math`** - Fixed-point arithmetic

  ```zig
  const math = sdk.math;


  const shares = math.isqrt(product);      // Integer sqrt
  const fee = math.bpsMul(amount, 30);     // 0.3% (30 bps)
  const smaller = math.min(u128, a, b);
  const larger = math.max(u128, a, b);
  ```

* Guards

  **`sdk.guards`** - Safety utilities

  ```zig
  const guards = sdk.guards;


  // Reentrancy protection
  try guards.enterNonReentrant();
  defer guards.exitNonReentrant();


  // Safe arithmetic (returns error on overflow)
  const sum = guards.safeAdd(u128, a, b) catch return error;
  const diff = guards.safeSub(u128, a, b) catch return error;
  ```

## Module Reference

[Section titled “Module Reference”](#module-reference)

| Module    | Import        | Purpose                    |
| --------- | ------------- | -------------------------- |
| `heap`    | `sdk.heap`    | Bump allocator             |
| `storage` | `sdk.storage` | State read/write           |
| `context` | `sdk.context` | Caller, origin, block info |
| `crypto`  | `sdk.crypto`  | Keccak256, SHA256, Blake3  |
| `events`  | `sdk.events`  | Event emission             |
| `guards`  | `sdk.guards`  | Reentrancy, safe math      |
| `math`    | `sdk.math`    | WAD/RAY/BPS math           |

## Next Steps

[Section titled “Next Steps”](#next-steps)

[Zig Guide ](/contracts/zig-guide/)Detailed Zig contract tutorial

[IDL & ABI ](/contracts/idl-and-abi/)Interface definitions

[Examples ](/contracts/examples/)Sample contracts

[Deploying ](/guides/deploying-contracts/)Deployment guide

## Related

[Section titled “Related”](#related)

[Execution ](/architecture/execution/)VM architecture

[Gas & Fees ](/concepts/gas-and-fees/)Gas metering

[RPC API ](/reference/rpc-api/)Contract calls

# Example Contracts

> Production-ready reference implementations

## Overview

[Section titled “Overview”](#overview)

The `contracts/` directory contains production-ready reference implementations covering DeFi primitives, oracles, cross-chain messaging, and utilities. All contracts are written in Zig using the [Ashen SDK](/contracts/ashen-sdk).

## Tokens

[Section titled “Tokens”](#tokens)

### SFT Token (`sft_v1`) — Rust

[Section titled “SFT Token (sft\_v1) — Rust”](#sft-token-sft_v1--rust)

A feature-rich fungible token with modular capabilities:

* **Core:** mint, burn, transfer
* **Roles:** owner, minter, blacklister, fee manager
* **Allowances:** approve/transferFrom pattern
* **Blacklist:** address blocking
* **Fees:** configurable transfer fees
* **Recovery:** owner can recover stuck tokens

Optional features (compile-time): pause, whitelist, limits, locking, snapshots, governance, multisig, flash loans, compliance hooks.

```bash
# Build with default features
just contract-build --manifest-path contracts/sft_v1/Cargo.toml


# Build with all features
cargo build --manifest-path contracts/sft_v1/Cargo.toml --features full
```

**Key functions:** `mint`, `burn`, `transfer`, `approve`, `transfer_from`, `set_fee`

***

## DeFi Primitives

[Section titled “DeFi Primitives”](#defi-primitives)

### AMM Pool (`amm_pool_v1`)

[Section titled “AMM Pool (amm\_pool\_v1)”](#amm-pool-amm_pool_v1)

A constant-product automated market maker (x × y = k) with:

* 0.3% default fee (configurable by owner)
* K-invariant verification using u256 arithmetic
* Slippage protection and minimum output checks

```bash
# Build
cd contracts/amm_pool_v1 && zig build -Doptimize=ReleaseSmall
```

**Key functions:** `swap_x_for_y`, `swap_y_for_x`, `add_liquidity`, `remove_liquidity`

***

### Concentrated Liquidity (`concentrated_liquidity_v1`)

[Section titled “Concentrated Liquidity (concentrated\_liquidity\_v1)”](#concentrated-liquidity-concentrated_liquidity_v1)

Bin-based fixed-price liquidity pool (similar to Trader Joe v2):

* Discrete price bins with configurable bin step
* Capital-efficient concentrated positions
* Active bin tracking for swaps

**Key functions:** `add_liquidity`, `remove_liquidity`, `swap`, `get_active_bin`

***

### Stable Swap (`stable_swap_v1`)

[Section titled “Stable Swap (stable\_swap\_v1)”](#stable-swap-stable_swap_v1)

StableSwap invariant AMM optimized for pegged assets:

* Low slippage for like-kind swaps
* Configurable amplification coefficient
* Multi-asset support

**Key functions:** `exchange`, `add_liquidity`, `remove_liquidity`, `get_dy`

***

### Order Book (`order_book_v1`)

[Section titled “Order Book (order\_book\_v1)”](#order-book-order_book_v1)

Central limit order book (CLOB) with price-time priority:

* Sorted storage keys for efficient bid/ask iteration
* Partial fills and order cancellation
* Market and limit order types

**Key functions:** `place_order`, `cancel_order`, `match_orders`, `get_best_bid`, `get_best_ask`

***

### DEX Router (`dex_router_v1`)

[Section titled “DEX Router (dex\_router\_v1)”](#dex-router-dex_router_v1)

Multi-hop swap router demonstrating cross-contract calls:

* Chained swaps across multiple pools
* Access list hints for state key warming
* Slippage protection across the full path

**Key functions:** `swap_exact_in`, `swap_exact_out`, `get_amounts_out`

***

### Lending Market (`lending_market_v1`)

[Section titled “Lending Market (lending\_market\_v1)”](#lending-market-lending_market_v1)

Single-asset money market with:

* Supply/withdraw with share-based accounting
* Borrow/repay with interest accrual
* Liquidation with configurable thresholds

**Key functions:** `supply`, `withdraw`, `borrow`, `repay`, `liquidate`

***

### Vault (`vault_v1` / `vault_strategy_v1`)

[Section titled “Vault (vault\_v1 / vault\_strategy\_v1)”](#vault-vault_v1--vault_strategy_v1)

ERC-4626 style tokenized vault:

* Deposit/withdraw with share accounting
* Pluggable yield strategies
* Performance fee collection

**Key functions:** `deposit`, `withdraw`, `harvest`, `report`

***

### Staking (`stake_pool_v1` / `reward_gauge_v1`)

[Section titled “Staking (stake\_pool\_v1 / reward\_gauge\_v1)”](#staking-stake_pool_v1--reward_gauge_v1)

Staking and rewards distribution:

* Time-weighted reward accumulation
* Multiple reward tokens
* Gauge voting for emissions

**Key functions:** `stake`, `unstake`, `claim_rewards`, `vote`

***

### Governance (`timelock_governor_v1`)

[Section titled “Governance (timelock\_governor\_v1)”](#governance-timelock_governor_v1)

On-chain governance with timelock:

* Proposal creation and voting
* Configurable voting period and quorum
* Timelock delay for execution

**Key functions:** `propose`, `vote`, `queue`, `execute`

## Oracles

[Section titled “Oracles”](#oracles)

### Price Oracle (`price_oracle_v1`)

[Section titled “Price Oracle (price\_oracle\_v1)”](#price-oracle-price_oracle_v1)

Push/pull price oracle with TWAP:

* Signed price updates from authorized publishers
* Circular buffer for time-weighted averaging
* Staleness checks

**Key functions:** `update_price`, `get_price`, `get_twap`

***

### Pyth Oracle (`pyth_oracle_v1`)

[Section titled “Pyth Oracle (pyth\_oracle\_v1)”](#pyth-oracle-pyth_oracle_v1)

Pyth-style ed25519 price attestation verification:

* Publisher set management with threshold
* Direct signature verification (not via Wormhole)
* Price confidence intervals

**Key functions:** `verify_attestation`, `update_publisher_set`, `get_price`

***

### RedStone Oracle (`redstone_oracle_v1`)

[Section titled “RedStone Oracle (redstone\_oracle\_v1)”](#redstone-oracle-redstone_oracle_v1)

RedStone data package verification:

* ECDSA signature verification
* Multi-signer threshold support
* Timestamp validation

**Key functions:** `verify_data_package`, `get_price`

***

### Chainlink OCR2 (`chainlink_ocr2_v1`)

[Section titled “Chainlink OCR2 (chainlink\_ocr2\_v1)”](#chainlink-ocr2-chainlink_ocr2_v1)

Chainlink Off-Chain Reporting v2 verification:

* Multi-signature report verification
* Configurable signer set
* Report decoding

**Key functions:** `verify_report`, `set_config`, `latest_answer`

## Cross-Chain

[Section titled “Cross-Chain”](#cross-chain)

### Wormhole Core (`wormhole_core_v1`)

[Section titled “Wormhole Core (wormhole\_core\_v1)”](#wormhole-core-wormhole_core_v1)

Wormhole VAA (Verified Action Approval) verification:

* Guardian signature verification
* Message parsing and validation
* Replay protection

**Key functions:** `verify_vaa`, `parse_vaa`, `update_guardian_set`

***

### Axelar GMP (`axelar_gmp_v1`)

[Section titled “Axelar GMP (axelar\_gmp\_v1)”](#axelar-gmp-axelar_gmp_v1)

Axelar General Message Passing:

* Cross-chain message execution
* Operator set management
* Batch processing

**Key functions:** `execute`, `initialize`, `update_operators`

***

### Hyperlane ISM (`hyperlane_ism_v1`)

[Section titled “Hyperlane ISM (hyperlane\_ism\_v1)”](#hyperlane-ism-hyperlane_ism_v1)

Hyperlane Interchain Security Module:

* Validator-based message verification
* Configurable threshold per origin
* Message routing

**Key functions:** `verify_message`, `update_validator_set`

## Infrastructure

[Section titled “Infrastructure”](#infrastructure)

### Light Client (`light_client_v1`)

[Section titled “Light Client (light\_client\_v1)”](#light-client-light_client_v1)

On-chain light client for finality verification:

* MMR (Merkle Mountain Range) proof verification
* BLS signature aggregation
* Header chain validation

**Key functions:** `verify_finality_proof`, `update_header`, `get_root`

***

### Fee Sponsor (`fee_sponsor_v1`)

[Section titled “Fee Sponsor (fee\_sponsor\_v1)”](#fee-sponsor-fee_sponsor_v1)

Third-party gas sponsorship:

* Sponsor agreements with spending limits
* Per-user and per-contract policies
* Expiration and revocation

**Key functions:** `create_agreement`, `sponsor_tx`, `revoke`, `withdraw`

***

### Source Registry (`source_registry_v1`)

[Section titled “Source Registry (source\_registry\_v1)”](#source-registry-source_registry_v1)

Contract source code registry:

* On-chain source verification
* Version management
* Metadata storage

**Key functions:** `register`, `verify`, `get_source`

## Testing & Development

[Section titled “Testing & Development”](#testing--development)

### Mock Pool (`mock_pool_v1`)

[Section titled “Mock Pool (mock\_pool\_v1)”](#mock-pool-mock_pool_v1)

Deterministic AMM for testing:

* Configurable reserves and fees
* Predictable swap outputs
* DEX router integration testing

***

### Gas Burner (`gas_burner_v1`)

[Section titled “Gas Burner (gas\_burner\_v1)”](#gas-burner-gas_burner_v1)

Gas throughput stress testing:

* Pure compute workload (ALU-heavy)
* Storage-write workload
* Mixed DeFi-like operations
* Parallel execution testing

```bash
# Run stress test
just gas-stress --scenario mixed --duration 60
```

***

### Zig Fixture (`zig_fixture`)

[Section titled “Zig Fixture (zig\_fixture)”](#zig-fixture-zig_fixture)

Minimal contract template for testing the SDK and toolchain.

## Building Contracts

[Section titled “Building Contracts”](#building-contracts)

All Zig contracts follow the same build pattern:

```bash
# Build a single contract
cd contracts/<name> && zig build -Doptimize=ReleaseSmall


# Build all contracts
just contract-build-all
```

## Contract Structure

[Section titled “Contract Structure”](#contract-structure)

Each contract directory contains:

```plaintext
contracts/<name>/
├── build.zig          # Build configuration
├── linker.ld          # Linker script for RISC-V
├── src/
│   └── main.zig       # Contract implementation
└── zig-out/           # Build output (gitignored)
```

## Reference Implementation

[Section titled “Reference Implementation”](#reference-implementation)

For a complete, well-documented example, see **`amm_pool_v1`** which demonstrates:

* Full SDK usage (storage, events, math, guards)
* Proper error handling
* Gas-efficient patterns
* Comprehensive testing

# IDL and ABI

> Interface Definition Language as the single source of truth for contracts

IDL (Interface Definition Language) files are the **single source of truth** for all contract interfaces. They define methods, parameters, return types, structs, and enums in a language-neutral format that drives code generation, ABI encoding, RPC exposure, and tooling discoverability.

## Why IDL is the Source of Truth

[Section titled “Why IDL is the Source of Truth”](#why-idl-is-the-source-of-truth)

The IDL-first approach provides several critical guarantees:

| Benefit                     | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| **Language Neutrality**     | One definition generates Rust, Zig, TypeScript, Go, and C clients  |
| **Deterministic Selectors** | Method selectors computed from signatures, not arbitrary constants |
| **Type Safety**             | Parameter validation at build time and runtime                     |
| **Discoverability**         | Tools can introspect contracts without source code                 |
| **Versioning**              | Breaking changes detected through IDL comparison                   |

### The IDL Pipeline

[Section titled “The IDL Pipeline”](#the-idl-pipeline)

```plaintext
┌─────────────────────────────────────────────────────────────────────────────┐
│                                IDL Source                                   │
│                            (contracts/*.idl)                                │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
     ┌────────────────┐   ┌────────────────┐   ┌────────────────┐
     │   Manifest     │   │  Code Stubs    │   │   On-Chain     │
     │  (selectors,   │   │  (Rust, Zig,   │   │   Storage      │
     │   types)       │   │   TS, Go, C)   │   │  (UTF-8 IDL)   │
     └───────┬────────┘   └───────┬────────┘   └───────┬────────┘
             │                    │                    │
             ▼                    ▼                    ▼
     ┌────────────────┐   ┌────────────────┐   ┌────────────────┐
     │  JSON Codec    │   │   Contract     │   │   RPC Query    │
     │  (encode/      │   │   Binary       │   │  contract_idl  │
     │   decode)      │   │   (.elf)       │   │                │
     └────────────────┘   └────────────────┘   └────────────────┘
```

## IDL Syntax

[Section titled “IDL Syntax”](#idl-syntax)

IDL files use a simple, declarative syntax:

```idl
namespace sft_v1;


/// A token balance with optional lock period.
struct BalanceInfo {
    amount: u128;
    locked_until: Option<u64>;
}


/// Transfer event emitted on every balance change.
struct TransferEvent {
    from: Address;
    to: Address;
    amount: u128;
}


/// Error codes returned by token operations.
enum TokenError {
    InsufficientBalance(Unit);
    NotAuthorized(Unit);
    BlacklistedAddress(Address);
}


interface SftV1 {
    /// Get the total token supply.
    fn total_supply() -> u128;


    /// Get balance for an account.
    fn balance_of(account: Address) -> BalanceInfo;


    /// Transfer tokens to another account.
    fn transfer(to: Address, amount: u128) -> bool;


    /// Mint new tokens (owner only).
    fn mint(to: Address, amount: u128) -> bool;
}
```

### Primitive Types

[Section titled “Primitive Types”](#primitive-types)

| Type        | Description             | JSON Encoding    |
| ----------- | ----------------------- | ---------------- |
| `bool`      | Boolean                 | `true` / `false` |
| `u8`..`u64` | Unsigned integers       | Number           |
| `u128`      | Large unsigned integer  | String (decimal) |
| `i8`..`i64` | Signed integers         | Number           |
| `i128`      | Large signed integer    | String (decimal) |
| `String`    | UTF-8 string            | String           |
| `Address`   | 32-byte account address | Hex string (0x…) |

### Composite Types

[Section titled “Composite Types”](#composite-types)

| Type         | Description           | JSON Encoding                       |
| ------------ | --------------------- | ----------------------------------- |
| `Vec<T>`     | Variable-length array | `[...]`                             |
| `Option<T>`  | Optional value        | `null` or value                     |
| Named struct | User-defined record   | `{field: value}`                    |
| Named enum   | Tagged union          | `{type: "variant", value: payload}` |

### Special Conventions

[Section titled “Special Conventions”](#special-conventions)

* **`Unit` struct**: Empty payload for enum variants
* **Documentation comments**: `///` lines become method/type docs
* **Namespace**: Must match contract name for discoverability

## Selector Computation

[Section titled “Selector Computation”](#selector-computation)

Method selectors are deterministically computed from the canonical signature:

```plaintext
selector = keccak256(signature)[0..4]
signature = "Interface.method(param1:Type1,param2:Type2)"
```

### Canonical Type Names

[Section titled “Canonical Type Names”](#canonical-type-names)

| IDL Type         | Canonical Form                    |
| ---------------- | --------------------------------- |
| `u128`           | `u128`                            |
| `Vec<Address>`   | `vec<address>`                    |
| `Option<String>` | `option<string>`                  |
| Named struct     | Struct name (e.g., `BalanceInfo`) |

### Example

[Section titled “Example”](#example)

```plaintext
interface: SftV1
method: transfer(to: Address, amount: u128)
signature: "SftV1.transfer(to:address,amount:u128)"
selector: keccak256(signature)[0..4] = 0x23b872dd
```

## Code Generation

[Section titled “Code Generation”](#code-generation)

The `idl-abi-gen` crate generates language-specific code from IDL files.

### Rust Contract Glue

[Section titled “Rust Contract Glue”](#rust-contract-glue)

```bash
just idl-abi-gen \
  --idl contracts/sft_v1/sft_v1.idl \
  --out-dir contracts/sft_v1/src \
  --rust-contract
```

Generates `abi.rs` containing:

* Selector constants
* Request/response structs
* Encoding helpers
* Dispatch router

### Client Stubs

[Section titled “Client Stubs”](#client-stubs)

```bash
# TypeScript client
ashen idl codegen --idl sft_v1.idl --lang typescript


# Rust client
ashen idl codegen --idl sft_v1.idl --lang rust


# Go client
ashen idl codegen --idl sft_v1.idl --lang go


# C header
ashen idl codegen --idl sft_v1.idl --lang c
```

## On-Chain IDL Storage

[Section titled “On-Chain IDL Storage”](#on-chain-idl-storage)

When a contract is deployed, its IDL is stored on-chain alongside the bytecode:

```rust
// During deployment
store_contract_idl(&mut backend, &contract_address, idl_bytes);


// Query via RPC
let result = client.contract_idl(&address)?;
let idl_text = result.idl; // Option<String>
```

### Deploy Bundle Format

[Section titled “Deploy Bundle Format”](#deploy-bundle-format)

A deploy bundle contains three components:

```plaintext
┌───────────────────────────────────────┐
│  Bundle Header (manifest length, etc) │
├───────────────────────────────────────┤
│  Manifest (JSON with metadata)        │
├───────────────────────────────────────┤
│  IDL (UTF-8 text)                     │
├───────────────────────────────────────┤
│  ELF Binary (RISC-V contract code)    │
└───────────────────────────────────────┘
```

### Building a Deploy Bundle

[Section titled “Building a Deploy Bundle”](#building-a-deploy-bundle)

```bash
# Build contract
cd contracts/sft_v1 && cargo build --release --target riscv64gc-unknown-none-elf


# Create bundle with IDL
ashen contract deploy \
  --elf target/riscv64gc-unknown-none-elf/release/sft_v1 \
  --idl contracts/sft_v1/sft_v1.idl \
  --wait
```

## RPC Integration

[Section titled “RPC Integration”](#rpc-integration)

The node RPC itself is defined by an IDL (`src/rpc/node_rpc_v1.idl`), enabling the same tooling to work for both:

1. **Contract interaction** - Call contract methods via `view_call` / `tx_submit`
2. **Node API** - Query chain state via `status`, `account`, `tx_by_hash`, etc.

### IDL-Aware RPC Client

[Section titled “IDL-Aware RPC Client”](#idl-aware-rpc-client)

The `IdlRpcClient` dynamically discovers and invokes RPC methods:

```rust
use crate::idl_rpc::IdlRpcClient;


let client = IdlRpcClient::new("http://localhost:3030", None)?;


// List all available methods
for method in client.methods() {
    println!("{}: {}", method.qualified_name, method.doc.unwrap_or_default());
}


// Get parameter template for a method
let template = client.param_template("account")?;
// {"address": "0x0000..."}


// Invoke method dynamically
let result = client.call("account", json!({"address": "0x123..."}))?;
```

### Contract IDL Query

[Section titled “Contract IDL Query”](#contract-idl-query)

Any deployed contract’s IDL can be queried:

```bash
# CLI
ashen idl fetch --contract 0x1234...


# RPC
curl -X POST http://localhost:3030/v2/rpc \
  -d '{"id":1,"method":"NodeRpcV1.contract_idl","params":{"address":"0x1234..."}}'
```

## JSON Encoding

[Section titled “JSON Encoding”](#json-encoding)

The `idl-json-codec` crate handles bidirectional conversion between JSON and Borsh:

### Encoding (JSON → Calldata)

[Section titled “Encoding (JSON → Calldata)”](#encoding-json--calldata)

```rust
let abi = Abi::from_idl_path(&idl_path)?;


// Build calldata from JSON arguments
let calldata = abi.build_calldata(
    Some("SftV1"),
    "transfer",
    Some(&json!({"to": "0x123...", "amount": "1000"})),
    None
)?;


// calldata = [selector (4 bytes)] + [borsh-encoded params]
```

### Decoding (Return Data → JSON)

[Section titled “Decoding (Return Data → JSON)”](#decoding-return-data--json)

```rust
// Decode return data using method signature
let result = abi.decode_method_result(
    Some("SftV1"),
    "balance_of",
    &return_bytes
)?;


// {"ok": {"amount": "1000", "locked_until": null}}
// or
// {"err": {"Code": {"code": 1, "data": null}}}
```

### Return Value ABI

[Section titled “Return Value ABI”](#return-value-abi)

All contract returns use a standard envelope:

```plaintext
┌─────────────────────────────────────┐
│  Tag (1 byte)                       │
│  0 = Error, 1 = Ok                  │
├─────────────────────────────────────┤
│  Payload (Borsh-encoded)            │
│  Tag=0: ContractError               │
│  Tag=1: Return type from IDL        │
└─────────────────────────────────────┘
```

## TUI Integration

[Section titled “TUI Integration”](#tui-integration)

The TUI (Terminal User Interface) uses IDLs for contract discoverability:

### IDL Explorer

[Section titled “IDL Explorer”](#idl-explorer)

Navigate and inspect registered IDLs:

```plaintext
┌─ IDL Explorer: sft_v1 ──────────────────────────────────────────────────────┐
│ Namespace: sft_v1                                                           │
│                                                                             │
│ [1] Overview  [2] Structs  [3] Methods                                      │
│                                                                             │
│ ► total_supply() -> u128                                                    │
│   balance_of(account: Address) -> BalanceInfo                               │
│   transfer(to: Address, amount: u128) -> bool                               │
│   mint(to: Address, amount: u128) -> bool                                   │
│   burn(amount: u128) -> bool                                                │
│   approve(spender: Address, amount: u128) -> bool                           │
│                                                                             │
│ Press [enter] to invoke selected method                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Contract Discovery Flow

[Section titled “Contract Discovery Flow”](#contract-discovery-flow)

```plaintext
┌────────────────────────────────────────────────────────────────────────────┐
│                         User selects contract                              │
└───────────────────────────────────┬────────────────────────────────────────┘
                                    │
                     ┌──────────────▼──────────────┐
                     │   Check local IDL cache     │
                     └──────────────┬──────────────┘
                                    │
              ┌─────────────────────┴─────────────────────┐
              │ Cache hit                                 │ Cache miss
              ▼                                           ▼
     ┌────────────────┐                        ┌────────────────┐
     │   Load from    │                        │  Query RPC     │
     │   ~/.ashen/    │                        │  contract_idl  │
     │   idl-cache/   │                        │                │
     └───────┬────────┘                        └───────┬────────┘
             │                                         │
             │                                         ▼
             │                                ┌────────────────┐
             │                                │  Cache IDL     │
             │                                │  locally       │
             │                                └───────┬────────┘
             │                                         │
             └──────────────────┬──────────────────────┘
                                │
                                ▼
                       ┌────────────────┐
                       │  Parse IDL     │
                       │  Display       │
                       │  methods       │
                       └────────────────┘
```

### Agent-Friendly Features

[Section titled “Agent-Friendly Features”](#agent-friendly-features)

The IDL system enables AI agents to interact with contracts programmatically:

1. **Method Discovery**: List all callable methods with types
2. **Parameter Templates**: Generate valid JSON for any method
3. **Validation**: Check arguments before submission
4. **Error Decoding**: Structured error responses

```bash
# List methods (machine-readable)
ashen abi 0x123... --json


# Get parameter template
ashen contract inspect --idl sft_v1.idl | jq '.manifest.interfaces[].methods[]'
```

## IDL Validation and Compatibility

[Section titled “IDL Validation and Compatibility”](#idl-validation-and-compatibility)

### Validation

[Section titled “Validation”](#validation)

Check an IDL for errors before deployment:

```bash
ashen idl validate --idl contracts/sft_v1/sft_v1.idl
```

Validates:

* Syntax correctness
* Type references resolve
* No selector collisions
* Reserved word avoidance

### Compatibility Checking

[Section titled “Compatibility Checking”](#compatibility-checking)

Detect breaking changes between IDL versions:

```bash
ashen idl compat \
  --old-idl contracts/sft_v1/sft_v1_v1.idl \
  --new-idl contracts/sft_v1/sft_v1_v2.idl
```

**Breaking Changes Detected:**

* Method removal
* Method signature change
* Struct field removal/type change
* Enum variant removal

**Non-Breaking Changes:**

* New methods added
* New struct fields (if optional)
* New enum variants

## CLI Reference

[Section titled “CLI Reference”](#cli-reference)

### IDL Commands

[Section titled “IDL Commands”](#idl-commands)

| Command              | Description                              |
| -------------------- | ---------------------------------------- |
| `ashen idl fetch`    | Fetch on-chain IDL for a contract        |
| `ashen idl generate` | Generate manifest JSON from IDL          |
| `ashen idl validate` | Validate IDL syntax and semantics        |
| `ashen idl compat`   | Check compatibility between IDL versions |
| `ashen idl codegen`  | Generate client code (TS/Rust/Go/C)      |

### Contract Commands with IDL

[Section titled “Contract Commands with IDL”](#contract-commands-with-idl)

| Command                               | Description                 |
| ------------------------------------- | --------------------------- |
| `ashen contract view --idl <path>`    | Call view method with IDL   |
| `ashen contract call --idl <path>`    | Execute state-changing call |
| `ashen contract deploy --idl <path>`  | Deploy with on-chain IDL    |
| `ashen contract inspect --idl <path>` | Show IDL manifest           |

### CLI IDL Management

[Section titled “CLI IDL Management”](#cli-idl-management)

```bash
# Validate an IDL
ashen idl validate ./contracts/sft_v1/sft_v1.idl


# Generate manifest from IDL
ashen idl generate --idl ./contracts/sft_v1/sft_v1.idl


# Fetch on-chain IDL
ashen idl fetch --contract 0x1234...
```

## Best Practices

[Section titled “Best Practices”](#best-practices)

### IDL Design

[Section titled “IDL Design”](#idl-design)

1. **Use descriptive names** - `BalanceInfo` not `BI`
2. **Document everything** - `///` comments become API docs
3. **Group related types** - Keep request/response pairs together
4. **Version namespaces** - `sft_v1`, `sft_v2` for major changes
5. **Keep structs small** - Flatten deeply nested structures

### Deployment

[Section titled “Deployment”](#deployment)

1. **Always include IDL** - Enables discoverability
2. **Validate before deploy** - Catch errors early
3. **Check compatibility** - Before upgrading contracts
4. **Cache IDLs locally** - Reduce RPC calls in development

### Integration

[Section titled “Integration”](#integration)

1. **Use typed clients** - Generate code instead of manual encoding
2. **Validate inputs** - Use `IdlRpcClient.validate_params()`
3. **Handle errors** - Decode structured errors for debugging
4. **Log method calls** - Include selector for traceability

## Related

[Section titled “Related”](#related)

* [Example Contracts](/contracts/examples/) - Reference implementations
* [Ashen SDK](/contracts/ashen-sdk/) - Contract development guide
* [Execution](/architecture/execution/) - VM and gas model
* [RPC Reference](/guides/using-the-cli/) - CLI and RPC documentation

# Rust Guide

> Writing contracts in Rust

## Overview

[Section titled “Overview”](#overview)

Ashen supports Rust contracts for developers who want tight control, `no_std` performance, and the `contract-sdk` storage/ABI helpers. This guide shows the canonical layout, entrypoint wiring, and build flow.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* **Pinned toolchain**: Use the `devenv` toolchain (or the [contract builder image](/guides/deterministic-builds/)). The network validates ELF output from the canonical compilers.
* **RISC-V target**: `riscv64imac-unknown-none-elf`
* **No std**: Contracts are `no_std` + `alloc`.

## Project Layout

[Section titled “Project Layout”](#project-layout)

A typical Rust contract looks like `contracts/sft_v1`:

```plaintext
contracts/my_contract/
├── Cargo.toml
├── my_contract.idl
└── src/
    ├── main.rs
    ├── lib.rs
    └── abi.rs
```

* `src/main.rs` defines the entrypoint.
* `src/lib.rs` contains the contract logic and ABI implementation.
* `src/abi.rs` is generated from the IDL (do not hand-edit).

## IDL + Codegen

[Section titled “IDL + Codegen”](#idl--codegen)

Generate Rust ABI bindings from the IDL:

```bash
just idl-abi-gen \
  --idl contracts/my_contract/my_contract.idl \
  --out-dir contracts/my_contract/src \
  --rust-contract
```

This creates `src/abi.rs` with:

* selector constants
* request/response structs
* a `dispatch` function
* a trait you implement for your contract

## Minimal Counter Contract

[Section titled “Minimal Counter Contract”](#minimal-counter-contract)

**IDL** (`contracts/counter/counter.idl`):

```idl
namespace counter;


interface Counter {
    fn get() -> u128;
    fn inc() -> u128;
}
```

**Cargo.toml** (minimal deps):

```toml
[dependencies]
borsh = { version = "1.5.5", default-features = false, features = ["derive"] }
contract-rt = { path = "../../crates/contract-rt" }
contract-sdk = { path = "../../crates/contract-sdk" }
```

**lib.rs** (logic + ABI implementation):

```rust
#![cfg_attr(target_arch = "riscv64", no_std)]


extern crate alloc;


mod abi;


use contract_sdk::{define_storage, ContractErrorV1, Item};


define_storage! {
    namespace: "counter",
    pub struct Storage {
        pub value: Item<u128>,
    }
}


pub struct Contract {
    storage: Storage,
}


impl Contract {
    pub fn new() -> Result<Self, ContractErrorV1> {
        Ok(Self {
            storage: Storage::new()?,
        })
    }
}


impl abi::Counter for Contract {
    fn get(&mut self) -> Result<abi::U128Result, ContractErrorV1> {
        let value = self.storage.value.get()?.unwrap_or(0);
        Ok(abi::U128Result { value })
    }


    fn inc(&mut self) -> Result<abi::U128Result, ContractErrorV1> {
        let value = self.storage.value.get()?.unwrap_or(0) + 1;
        self.storage.value.set(&value)?;
        Ok(abi::U128Result { value })
    }
}
```

**main.rs** (entrypoint):

```rust
#![cfg_attr(target_arch = "riscv64", no_std)]
#![cfg_attr(target_arch = "riscv64", no_main)]


// Replace `counter` with your library crate name.
contract_rt::entrypoint_v1!(counter::Contract, counter::abi::dispatch);
```

## Build

[Section titled “Build”](#build)

```bash
ashen dev build --manifest-path contracts/counter/Cargo.toml
```

Output: `target/riscv64imac-unknown-none-elf/release/counter`

## Deploy

[Section titled “Deploy”](#deploy)

```bash
ashen deploy submit \
  --bundle target/riscv64imac-unknown-none-elf/release/counter \
  --idl contracts/counter/counter.idl \
  --key $ASHEN_PRIVATE_KEY \
  --wait
```

## Storage Collections

[Section titled “Storage Collections”](#storage-collections)

The Rust SDK provides typed storage helpers in `contract_sdk::storage`:

| Type               | Use                | Notes                         |
| ------------------ | ------------------ | ----------------------------- |
| `Item<T>`          | Single value       | `get/set/exists/clear`        |
| `Map<K, V>`        | Key-value map      | `get/set/remove/contains_key` |
| `Set<T>`           | Membership set     | Backed by `Map<T, u8>`        |
| `StorageVec<T>`    | Append-only vector | Tracks length + element keys  |
| `CountedMap<K, V>` | Map + O(1) size    | Maintains entry count         |
| `IndexedList<T>`   | List + index map   | Swap-remove deletions         |
| `LazyItem/Map/Set` | Cached wrappers    | Avoid redundant reads         |

Example:

```rust
use contract_sdk::{define_storage, Item, Map, Set, StorageVec};


define_storage! {
    namespace: "example",
    pub struct Storage {
        pub owner: Item<[u8; 32]>,
        pub balances: Map<[u8; 32], u128>,
        pub allowlist: Set<[u8; 32]>,
        pub history: StorageVec<[u8; 32]>,
    }
}
```

## Access Lists and Prefetch

[Section titled “Access Lists and Prefetch”](#access-lists-and-prefetch)

Access lists are hints that help the VM avoid cold storage penalties. The SDK exposes `declare_access` and `prefetch` on storage types:

```rust
// Map access hint and prefetch
storage.balances.declare_access(&caller)?;
storage.balances.prefetch(&caller)?;


// StorageVec access hint
storage.history.declare_len_access()?;
storage.history.prefetch_element(0)?;
```

Use these before hot loops or when you know the keys you will touch.

## Error Patterns

[Section titled “Error Patterns”](#error-patterns)

Use typed error codes for deterministic failures:

```rust
use contract_sdk::{ContractErrorV1, require};


const ERR_UNAUTHORIZED: u32 = 1;
const ERR_ZERO_AMOUNT: u32 = 2;


require!(amount > 0, ERR_ZERO_AMOUNT);
require!(caller == owner, ERR_UNAUTHORIZED);


return Err(ContractErrorV1::code(ERR_UNAUTHORIZED));
```

For manual ABI paths, you can return raw error payloads:

```rust
use contract_sdk::{revert_code, revert_other};


let bytes = revert_code(ERR_UNAUTHORIZED);
let bytes = revert_other("bad input".to_string());
```

## Keystore Usage

[Section titled “Keystore Usage”](#keystore-usage)

For deploys/calls, you can point `ASHEN_PRIVATE_KEY` at:

* a key file: `export ASHEN_PRIVATE_KEY=@./dev.key.json`
* a keystore handle: `export ASHEN_PRIVATE_KEY=keystore:my-key`

Create a keystore key:

```bash
ashen keystore init
ashen keystore add --label my-key
```

## Richer Example: Owner-Gated Faucet

[Section titled “Richer Example: Owner-Gated Faucet”](#richer-example-owner-gated-faucet)

This shows a small contract with:

* owner-only mint
* balances map
* event emission
* access list hints

```rust
use contract_sdk::{define_storage, ContractErrorV1, Host, Item, Map, Emittable, require};
use borsh::{BorshDeserialize, BorshSerialize};


const ERR_UNAUTHORIZED: u32 = 1;


#[derive(BorshSerialize, BorshDeserialize)]
pub struct MintEvent {
    pub to: [u8; 32],
    pub amount: u128,
}


define_storage! {
    namespace: "faucet",
    pub struct Storage {
        pub owner: Item<[u8; 32]>,
        pub balances: Map<[u8; 32], u128>,
    }
}


pub struct Contract { storage: Storage }


impl Contract {
    pub fn new() -> Result<Self, ContractErrorV1> {
        Ok(Self { storage: Storage::new()? })
    }


    fn require_owner(&self, caller: [u8; 32]) -> Result<(), ContractErrorV1> {
        let owner = self.storage.owner.get()?.unwrap_or([0u8; 32]);
        require!(caller == owner, ERR_UNAUTHORIZED);
        Ok(())
    }
}


// ABI methods would live here (generated in abi.rs)
impl Contract {
    pub fn mint(&mut self, to: [u8; 32], amount: u128) -> Result<(), ContractErrorV1> {
        let caller = Host::caller_key()?;
        self.require_owner(caller)?;


        self.storage.balances.declare_access(&to)?;
        self.storage.balances.prefetch(&to)?;


        let balance = self.storage.balances.get(&to)?.unwrap_or(0) + amount;
        self.storage.balances.set(&to, &balance)?;


        MintEvent { to, amount }.emit(b"Mint")?;
        Ok(())
    }
}
```

## Cross-Contract Call + Multi-Topic Event

[Section titled “Cross-Contract Call + Multi-Topic Event”](#cross-contract-call--multi-topic-event)

This example shows:

* building calldata for another contract
* `Host::call` with typed decode
* emitting a log with two indexed topics

```rust
extern crate alloc;


use alloc::vec::Vec;
use contract_sdk::{Address, ContractErrorV1, Host, HostError};
use borsh::BorshSerialize;


// Simple event payload
#[derive(BorshSerialize)]
pub struct SwapEvent {
    pub sender: [u8; 32],
    pub amount_in: u128,
    pub amount_out: u128,
}


pub fn swap_through_router(
    router: Address,
    sender: [u8; 32],
    amount_in: u128,
) -> Result<u128, ContractErrorV1> {
    // ABI selector + args (example; use IDL-generated helpers when available)
    let mut calldata = Vec::new();
    calldata.extend_from_slice(&0x1234_5678u32.to_be_bytes()); // selector
    calldata.extend_from_slice(&borsh::to_vec(&amount_in).unwrap());


    // Call router contract
    let amount_out: u128 = Host::call(&router, 0, 500_000, &calldata)
        .map_err(|e| e.into_contract_error())?;


    // Emit event with two topics: event sig + sender
    let mut topics = [[0u8; 32]; 2];
    topics[0] = Host::blake3(b"Swap(address,uint128,uint128)")?;
    topics[1] = sender;


    let event = SwapEvent {
        sender,
        amount_in,
        amount_out,
    };
    let data = borsh::to_vec(&event).map_err(|_| HostError::BorshEncode)?;
    Host::emit_log(&topics, &data)?;


    Ok(amount_out)
}
```

Notes:

* Prefer IDL-generated helpers instead of manual selector encoding when possible.
* `Host::call` decodes `Result<T, ContractErrorV1>` and surfaces reverts as `CallError`.

## Next Steps

[Section titled “Next Steps”](#next-steps)

* `/contracts/idl-and-abi/` for interface definitions
* `/contracts/examples/` for production Rust + Zig contracts
* `/reference/sdk/` for SDK API details

# Zig Guide

> Writing contracts in Zig

## Overview

[Section titled “Overview”](#overview)

Ashen contracts can be written in Zig and compiled to the Ashen VM’s RV64 freestanding target. This guide walks through the canonical contract layout, entrypoint patterns, and build flow using the Ashen Zig SDK.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* **Use the pinned toolchain.** Build with the exact Zig toolchain provided by `devenv` (or the [contract builder image](/guides/deterministic-builds/)). Validators validate the ELF output from the canonical compilers; mismatched toolchains are rejected.
* **Ashen SDK**: Contracts must use `contracts/ashen-sdk`. Do not reimplement storage, dispatch, or syscall helpers.
* **IDL file**: Every contract has a `*.idl` file that defines its interface.

## Project Layout

[Section titled “Project Layout”](#project-layout)

A typical Zig contract lives under `contracts/<name>/`:

```plaintext
contracts/my_contract/
├── build.zig
├── linker.ld
├── my_contract.idl
└── src/
    ├── main.zig
    ├── abi.zig
    └── my_contract.manifest.v1.json
```

* `build.zig` targets RV64 freestanding and wires in `ashen-sdk`.
* `linker.ld` keeps code/data at low addresses for the VM.
* `abi.zig` + `*.manifest.v1.json` are generated from IDL.

## Contract Skeleton

[Section titled “Contract Skeleton”](#contract-skeleton)

The recommended pattern is to use the SDK dispatch helper with IDL-generated stubs:

```zig
const sdk = @import("ashen-sdk");
const abi = @import("abi.zig");


const Counter = struct {
    pub fn get(self: *Counter, args: abi.GetArgs) abi.ContractResult(abi.GetResult) {
        _ = self;
        _ = args;
        const value: u128 = sdk.storage.readU128OrDefault("count", 0);
        return .{ .Ok = .{ .value = value } };
    }


    pub fn inc(self: *Counter, args: abi.IncArgs) abi.ContractResult(abi.IncResult) {
        _ = self;
        _ = args;
        const value: u128 = sdk.storage.readU128OrDefault("count", 0) + 1;
        _ = sdk.storage.writeU128("count", value);
        return .{ .Ok = .{ .value = value } };
    }
};


export fn _start(calldata_ptr: [*]const u8, calldata_len: usize) sdk.ByteSlice {
    return sdk.dispatch.run(Counter, abi.dispatch, calldata_ptr, calldata_len);
}


pub const panic = sdk.panic;
```

Notes:

* `sdk.dispatch.run` handles heap reset, calldata slicing, and error encoding.
* The entrypoint **must** be named `_start`.
* Always export `pub const panic = sdk.panic;`.

## Concrete Walkthrough: Counter Contract

[Section titled “Concrete Walkthrough: Counter Contract”](#concrete-walkthrough-counter-contract)

This is a minimal end-to-end example you can copy into a new contract.

### 1) Create the contract folder + IDL

[Section titled “1) Create the contract folder + IDL”](#1-create-the-contract-folder--idl)

```bash
mkdir -p contracts/counter/src
```

`contracts/counter/counter.idl`:

```idl
namespace counter;


interface Counter {
    fn get() -> u128;
    fn inc() -> u128;
}
```

### 2) Generate Zig stubs from IDL

[Section titled “2) Generate Zig stubs from IDL”](#2-generate-zig-stubs-from-idl)

```bash
just idl-abi-gen \
  --idl contracts/counter/counter.idl \
  --out-dir contracts/counter/src \
  --zig-stubs
```

### 3) Implement the contract

[Section titled “3) Implement the contract”](#3-implement-the-contract)

`contracts/counter/src/main.zig`:

```zig
const sdk = @import("ashen-sdk");
const abi = @import("abi.zig");


const Counter = struct {
    pub fn get(self: *Counter, args: abi.GetArgs) abi.ContractResult(abi.GetResult) {
        _ = self;
        _ = args;
        const value: u128 = sdk.storage.readU128OrDefault("count", 0);
        return .{ .Ok = .{ .value = value } };
    }


    pub fn inc(self: *Counter, args: abi.IncArgs) abi.ContractResult(abi.IncResult) {
        _ = self;
        _ = args;
        const value: u128 = sdk.storage.readU128OrDefault("count", 0) + 1;
        _ = sdk.storage.writeU128("count", value);
        return .{ .Ok = .{ .value = value } };
    }
};


export fn _start(calldata_ptr: [*]const u8, calldata_len: usize) sdk.ByteSlice {
    return sdk.dispatch.run(Counter, abi.dispatch, calldata_ptr, calldata_len);
}


pub const panic = sdk.panic;
```

### 4) Build

[Section titled “4) Build”](#4-build)

```bash
cd contracts/counter
zig build -Doptimize=ReleaseSmall
```

Output: `zig-out/bin/counter`

### 5) Deploy

[Section titled “5) Deploy”](#5-deploy)

```bash
ashen deploy submit \
  --bundle contracts/counter/zig-out/bin/counter \
  --idl contracts/counter/counter.idl \
  --key $ASHEN_PRIVATE_KEY \
  --wait
```

### 6) Call it

[Section titled “6) Call it”](#6-call-it)

```bash
ashen call 0xCONTRACT get '[]' --key $ASHEN_PRIVATE_KEY --wait
ashen call 0xCONTRACT inc '[]' --key $ASHEN_PRIVATE_KEY --wait
```

## IDL + Zig Stubs

[Section titled “IDL + Zig Stubs”](#idl--zig-stubs)

Generate Zig ABI stubs from the contract IDL:

```bash
just idl-abi-gen \
  --idl contracts/my_contract/my_contract.idl \
  --out-dir contracts/my_contract/src \
  --zig-stubs
```

This produces:

* `src/abi.zig` (selectors, args/results, dispatch)
* `src/my_contract.manifest.v1.json` (deploy manifest metadata)

Regenerate these files whenever you change the IDL.

## Build

[Section titled “Build”](#build)

```bash
cd contracts/my_contract
zig build -Doptimize=ReleaseSmall
```

Output: `zig-out/bin/my_contract`

## Deploy

[Section titled “Deploy”](#deploy)

Use the deployment workflow in the CLI guide:

* Build the Zig ELF (`zig build -Doptimize=ReleaseSmall`)
* Deploy with IDL (`ashen deploy submit`)

See: `/guides/deploying-contracts/`

## Common Patterns

[Section titled “Common Patterns”](#common-patterns)

### Storage helpers

[Section titled “Storage helpers”](#storage-helpers)

```zig
const balance = sdk.storage.readU128("balance") orelse 0;
_ = sdk.storage.writeU128("balance", balance + 1);
```

### Events

[Section titled “Events”](#events)

```zig
const events = sdk.events;
const Transfer = events.define("Transfer(address,address,uint256)");
Transfer.emit2(from, to, events.toTopicU128(amount), &[_]u8{});
```

### Reentrancy guard

[Section titled “Reentrancy guard”](#reentrancy-guard)

```zig
try sdk.guards.enterNonReentrant();
defer sdk.guards.exitNonReentrant();
```

## Next Steps

[Section titled “Next Steps”](#next-steps)

* `/contracts/ashen-sdk/` for the SDK API surface
* `/contracts/idl-and-abi/` for interface definitions
* `/contracts/examples/` for production-grade Zig contracts

# Installation

> Build Ashen from source

This guide covers building Ashen from source. There are two paths: **devenv** (recommended) for a reproducible Nix-based environment, or **manual** installation if you prefer managing dependencies yourself.

## Quick Start (devenv)

[Section titled “Quick Start (devenv)”](#quick-start-devenv)

The fastest way to get started is with [devenv](https://devenv.sh):

```bash
# Clone the repository
git clone https://github.com/ashen-sh/ashen.git
cd ashen


# Enter the dev environment (installs all dependencies)
devenv shell


# Build everything
just build


# Run tests
just test
```

***

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

### System Requirements

[Section titled “System Requirements”](#system-requirements)

| Component | Minimum      | Recommended              |
| --------- | ------------ | ------------------------ |
| **CPU**   | 4 cores      | 8+ cores                 |
| **RAM**   | 8 GB         | 16+ GB                   |
| **Disk**  | 20 GB free   | 50+ GB SSD               |
| **OS**    | Linux, macOS | Ubuntu 22.04+, macOS 13+ |

### Required Tools

[Section titled “Required Tools”](#required-tools)

| Tool     | Version            | Purpose                       |
| -------- | ------------------ | ----------------------------- |
| **Rust** | nightly-2025-11-05 | Node and contract compilation |
| **Zig**  | 0.13+              | Zig contract compilation      |
| **just** | 1.0+               | Task runner                   |
| **jq**   | 1.6+               | JSON processing (scripts)     |
| **curl** | any                | RPC testing                   |

***

## Option 1: devenv (Recommended)

[Section titled “Option 1: devenv (Recommended)”](#option-1-devenv-recommended)

[devenv](https://devenv.sh) provides a reproducible development environment with all dependencies pinned.

### Install devenv

[Section titled “Install devenv”](#install-devenv)

```bash
# Install Nix (if not already installed)
sh <(curl -L https://nixos.org/nix/install) --daemon


# Install devenv
nix-env -iA devenv -f https://github.com/NixOS/nixpkgs/tarball/nixpkgs-unstable
```

### Enter the Environment

[Section titled “Enter the Environment”](#enter-the-environment)

```bash
cd ashen
devenv shell
```

This automatically provides:

* Rust nightly (2025-11-05) with all components
* RISC-V cross-compilation target
* Miri for memory safety checks
* All required system tools (jq, curl, etc.)

### Available Commands

[Section titled “Available Commands”](#available-commands)

Inside `devenv shell`, these scripts are available:

| Command                | Description                      |
| ---------------------- | -------------------------------- |
| `build`                | Build entire workspace           |
| `test`                 | Run all tests                    |
| `fmt`                  | Format code                      |
| `clippy`               | Run lints                        |
| `ashen`                | Run the ashen CLI                |
| `devnet-node`          | Run a development node           |
| `just contract-build`  | Build a contract (via ashen dev) |
| `just contract-deploy` | Deploy a contract                |

***

## Option 2: Manual Installation

[Section titled “Option 2: Manual Installation”](#option-2-manual-installation)

If you prefer not to use Nix, install dependencies manually.

### 1. Install Rust

[Section titled “1. Install Rust”](#1-install-rust)

```bash
# Install rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


# Install the specific nightly toolchain
rustup toolchain install nightly-2025-11-05


# Set as default for this project
cd ashen
rustup override set nightly-2025-11-05


# Add required components
rustup component add rustc cargo clippy rustfmt rust-analyzer rust-src llvm-tools-preview


# Add RISC-V target for contracts
rustup target add riscv64imac-unknown-none-elf
```

### 2. Install Zig (for Zig contracts)

[Section titled “2. Install Zig (for Zig contracts)”](#2-install-zig-for-zig-contracts)

```bash
# Ubuntu/Debian
sudo apt install zig


# macOS
brew install zig


# Or download from https://ziglang.org/download/
```

### 3. Install just

[Section titled “3. Install just”](#3-install-just)

```bash
# Ubuntu/Debian
sudo apt install just


# macOS
brew install just


# Or via cargo
cargo install just
```

### 4. Install System Tools

[Section titled “4. Install System Tools”](#4-install-system-tools)

```bash
# Ubuntu/Debian
sudo apt install curl jq build-essential


# macOS
brew install curl jq
```

***

## Building from Source

[Section titled “Building from Source”](#building-from-source)

### Build Everything

[Section titled “Build Everything”](#build-everything)

```bash
# Build the entire workspace (debug)
just build


# Or directly with cargo
cargo build --workspace --all-targets


# Release build (optimized)
cargo build --workspace --all-targets --release
```

### Build Individual Components

[Section titled “Build Individual Components”](#build-individual-components)

```bash
# Build just the node
cargo build --bin node --release


# Build the CLI
cargo build --bin ashen --release


# The devnet simulator is built as part of the node binary
# Run with: cargo run --bin node -- devnet --help
```

### Build Contracts

[Section titled “Build Contracts”](#build-contracts)

#### Rust Contracts

[Section titled “Rust Contracts”](#rust-contracts)

```bash
# Build a specific Rust contract
just contract-build --manifest-path contracts/sft_v1/Cargo.toml


# With debug info (for debugging)
just contract-build-debug --manifest-path contracts/sft_v1/Cargo.toml
```

The contract is compiled to: `target/riscv64imac-unknown-none-elf/release/<name>`

#### Zig Contracts

[Section titled “Zig Contracts”](#zig-contracts)

```bash
# Build a specific Zig contract
cd contracts/amm_pool_v1
zig build -Doptimize=ReleaseSmall


# Build all contracts (Zig and Rust)
just contract-build-all
```

***

## Verifying Installation

[Section titled “Verifying Installation”](#verifying-installation)

### 1. Check the Build

[Section titled “1. Check the Build”](#1-check-the-build)

```bash
# Verify workspace compiles
cargo check --workspace --all-targets
```

### 2. Run Tests

[Section titled “2. Run Tests”](#2-run-tests)

```bash
# Run all tests
just test


# Or specific test suites
cargo test -p ashen                    # Core chain tests
cargo test -p vm-conformance           # VM conformance
cargo test -p vm-runtime               # Runtime tests
```

### 3. Run a Quick Smoke Test

[Section titled “3. Run a Quick Smoke Test”](#3-run-a-quick-smoke-test)

```bash
# Fast verification of core functionality
just agent-smoke
```

This runs:

* Workspace compilation check
* 4-node consensus simulation (100 steps)
* Core application tests
* Execution unit tests

### 4. Start a Local Node

[Section titled “4. Start a Local Node”](#4-start-a-local-node)

```bash
# Initialize node data with a funded account
ashen keygen --json > ./target/dev.key.json
export ASHEN_PRIVATE_KEY=@./target/dev.key.json
ADDR=$(jq -r .data.address ./target/dev.key.json)


just devnet-node init --data-dir ./node-data --alloc "$ADDR=1000000000000"


# Run the node
just node
```

In another terminal:

```bash
# Check status
just status


# Check your account
just account $ADDR
```

***

## Development Workflow

[Section titled “Development Workflow”](#development-workflow)

### Useful just Commands

[Section titled “Useful just Commands”](#useful-just-commands)

```bash
# List all available commands
just


# Format code
just fmt


# Run clippy lints
just clippy


# Run a single chain test (fast)
just ashen-single


# Run devnet simulation
just devnet-small      # 4 nodes, 200 steps
just devnet-chaos      # 7 nodes, lossy network


# Show verification guide
just robot
```

### IDE Setup

[Section titled “IDE Setup”](#ide-setup)

#### VS Code

[Section titled “VS Code”](#vs-code)

Install these extensions:

* **rust-analyzer** — Rust language support
* **Even Better TOML** — Cargo.toml editing
* **Zig Language** — Zig support (for contracts)

Add to `.vscode/settings.json`:

```json
{
  "rust-analyzer.cargo.target": null,
  "rust-analyzer.check.command": "clippy",
  "rust-analyzer.check.extraArgs": [
    "--",
    "-D", "clippy::panic",
    "-D", "clippy::unwrap_used",
    "-D", "clippy::expect_used"
  ]
}
```

#### Neovim

[Section titled “Neovim”](#neovim)

Use [nvim-lspconfig](https://github.com/neovim/nvim-lspconfig) with rust-analyzer:

```lua
require('lspconfig').rust_analyzer.setup {
  settings = {
    ['rust-analyzer'] = {
      check = {
        command = 'clippy',
      },
    },
  },
}
```

***

## Environment Variables

[Section titled “Environment Variables”](#environment-variables)

Set these in your shell or `.env` file:

| Variable            | Default                 | Description                        |
| ------------------- | ----------------------- | ---------------------------------- |
| `NODE_RPC_URL`      | `http://127.0.0.1:3030` | RPC endpoint for CLI tools         |
| `NODE_AUTH_TOKEN`   | none                    | Bearer token for authenticated RPC |
| `ASHEN_PRIVATE_KEY` | none                    | Signing key for transactions       |
| `NODE_DATA_DIR`     | `./node-data`           | Default data directory             |

### Key Formats

[Section titled “Key Formats”](#key-formats)

The `ASHEN_PRIVATE_KEY` can be:

```bash
# Raw hex (64 chars)
export ASHEN_PRIVATE_KEY="abcd1234..."


# 0x-prefixed hex
export ASHEN_PRIVATE_KEY="0xabcd1234..."


# File reference (JSON with secret_key_hex field)
export ASHEN_PRIVATE_KEY="@./path/to/key.json"


# Keystore reference
export ASHEN_PRIVATE_KEY="keystore:my-key"
```

***

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Rust Target Not Found

[Section titled “Rust Target Not Found”](#rust-target-not-found)

```plaintext
error: target 'riscv64imac-unknown-none-elf' not found
```

**Fix:** Install the RISC-V target:

```bash
rustup target add riscv64imac-unknown-none-elf
```

### Linker Not Found

[Section titled “Linker Not Found”](#linker-not-found)

```plaintext
error: linker `cc` not found
```

**Fix:** Install a C toolchain:

```bash
# Ubuntu/Debian
sudo apt install build-essential


# macOS (Xcode command line tools)
xcode-select --install
```

### Zig Not Found

[Section titled “Zig Not Found”](#zig-not-found)

```plaintext
zig: command not found
```

**Fix:** Install Zig or enter devenv shell:

```bash
devenv shell
# Or install Zig manually: https://ziglang.org/download/
```

### Out of Memory During Build

[Section titled “Out of Memory During Build”](#out-of-memory-during-build)

Large workspaces can exhaust memory during parallel compilation.

**Fix:** Limit parallelism:

```bash
cargo build -j 4  # Limit to 4 parallel jobs
```

### devenv Shell Fails

[Section titled “devenv Shell Fails”](#devenv-shell-fails)

```plaintext
error: getting status of '/nix/store/...': No such file or directory
```

**Fix:** Rebuild the Nix store:

```bash
devenv gc    # Garbage collect
devenv shell # Re-enter
```

***

## Next Steps

[Section titled “Next Steps”](#next-steps)

* [Quickstart](/getting-started/quickstart/) — Run a local node and deploy a contract
* [Running a Node](/guides/running-a-node/) — Detailed node operation guide
* [Deploying Contracts](/guides/deploying-contracts/) — Build and deploy smart contracts
* [Using the CLI](/guides/using-the-cli/) — Complete CLI reference

# Introduction

> What is Ashen and why should you use it?

Ashen is a high-performance blockchain built on [Commonware](https://commonware.xyz) primitives, featuring single-slot finality, RISC-V smart contract execution, and built-in MEV protection through encrypted transactions.

Tip

Ashen is **testnet ready**. All core infrastructure is complete and battle-tested.

## Why “Ashen”?

[Section titled “Why “Ashen”?”](#why-ashen)

The name works on three levels.

**`.sh` is the interface.** The canonical entrypoint is [`ashen.sh`](https://ashen.sh) — a domain and a mental model. Agents don’t read landing pages. They discover through shell, pay for what they need, and move on. The name encodes the distribution strategy: shell-first, agent-first.

**Burn away the unnecessary.** Current blockchain economics are a decaying system where validators subsidize everyone else. Ashen is what rises from those broken incentives — stripped of buzzwords, proxy patterns, and abstractions that exist to raise valuations. The name matches the ethos: burn the complexity theater, keep what works.

**The Ashen One keeps going.** In Dark Souls, the Ashen One rises from nothing and pushes forward against a world that’s falling apart. We’re building against the same kind of decay — extractive economics, audit-tax complexity, infrastructure parasitism. The name is a nod to persistence in the face of broken systems.

***

## Key Features

[Section titled “Key Features”](#key-features)

True Finality

Transactions finalize in \~1 second. No confirmations to wait for, no reorgs to fear. When a block commits, it’s final.

MEV Protection

Sealed transactions use threshold encryption. Your trades can’t be frontrun because validators can’t see them until execution.

Paid Reads (x402)

Protocol-native micropayments for RPC calls. Validators earn from the reads they serve. No more free-riding on infrastructure.

Agent-Native

Designed for AI agents to read, write, and interact. Deterministic execution, structured APIs, and metered access make automation first-class.

Write in Zig

Smart contracts compile to RISC-V. Write in Zig with a full SDK: safe math, events, storage helpers, and reentrancy guards.

Light Client Native

Cryptographic proofs for everything. Verify state without trusting anyone. Data availability sampling gives 99.99% confidence with 30 samples.

***

## Core Features

[Section titled “Core Features”](#core-features)

### Single-Slot Finality

[Section titled “Single-Slot Finality”](#single-slot-finality)

Ashen uses [Simplex consensus](/architecture/consensus/) with BLS12-381 threshold signatures. A block is final when 2f+1 validators sign—no probabilistic confirmation, no waiting.

* **\~1 second** block time
* **Deterministic finality** — committed blocks never revert
* **Threshold BLS signatures** — no single validator can finalize alone

### RISC-V Execution

[Section titled “RISC-V Execution”](#risc-v-execution)

Smart contracts run on a [deterministic RV64 virtual machine](/architecture/execution/):

* **ISA**: RV64IMC + Zba/Zbb (no floating point)
* **Tiered execution**: Interpreter → JIT → AOT compilation
* **Hot code tracking**: Frequently-called contracts get compiled to native
* **Cross-contract calls**: Synchronous with automatic rollback on failure

### Sealed Transactions (Private Mempool)

[Section titled “Sealed Transactions (Private Mempool)”](#sealed-transactions-private-mempool)

[Threshold Identity-Based Encryption (TIBE)](/internals/flows/sealed-transactions/) protects your transactions:

1. You encrypt your transaction to the validator set’s collective public key
2. It enters the mempool encrypted—validators can’t read it
3. At block time, validators collaborate to decrypt (threshold decryption)
4. FIFO ordering prevents content-based reordering

No frontrunning. No sandwich attacks. Your transaction executes as submitted.

### Data Availability Sampling

[Section titled “Data Availability Sampling”](#data-availability-sampling)

Light clients don’t need to download full blocks:

* **Reed-Solomon erasure coding** (64-of-128 shards)
* **30 random samples** → 99.99% confidence data is available
* **Commitment in headers** — `data_availability_root` proves block data

### Paid Reads (x402)

[Section titled “Paid Reads (x402)”](#paid-reads-x402)

Validators subsidize the entire ecosystem while capturing only write fees. Ashen fixes this with **protocol-native metered reads**:

| Read Type           | Why It’s Paid            | Cache Resistance                  |
| ------------------- | ------------------------ | --------------------------------- |
| **Tx Simulation**   | Pre-trade safety checks  | Depends on mempool + caller state |
| **State Proofs**    | Trustless verification   | Must be current to be useful      |
| **Account Nonces**  | Transaction construction | Changes with each write           |
| **Pending Mempool** | Execution ordering       | Updates every block               |

**How it works:**

1. Client requests a read (balance, simulation, proof)
2. Node meters compute + bytes + egress
3. Payment settles via **x402 + stablecoin** or sponsored credits
4. Revenue flows to the serving validator

Freshness is the product. Stale cache can be free; current data is paid.

### DKG Key Resharing

[Section titled “DKG Key Resharing”](#dkg-key-resharing)

Threshold BLS keys rotate every epoch via [Distributed Key Generation](/internals/flows/dkg/):

* **Per-epoch key rotation** — fresh keys limit exposure window
* **Resharing protocol** — new keys derived from previous epoch (forward secrecy)
* **Automatic fallback** — continues with previous keys if DKG fails (max 1 epoch)
* **BLS12-381 TIBE** — threshold encryption for sealed transactions

No single validator ever holds the full private key. Decryption requires threshold cooperation.

### Agent-Native Design

[Section titled “Agent-Native Design”](#agent-native-design)

Ashen is built for a future where agents write most code:

* **Deterministic VM** — no contract-visible nondeterminism (no FP, no timers)
* **Structured APIs** — IDL-driven interfaces with type-safe codegen
* **Metered access** — per-call pricing, no subscriptions or commitments
* **Simulation-first** — agents can test transactions before submitting
* **Proof-backed reads** — agents can verify without trusting RPCs

The contract model is simple enough for AI to generate correctly. The pricing model is transparent enough for agents to budget.

***

## Developer Experience

[Section titled “Developer Experience”](#developer-experience)

* Zig SDK

  The [Ashen SDK](/contracts/ashen-sdk/) provides everything for Zig contract development:

  ```zig
  const sdk = @import("ashen-sdk");


  export fn _start(calldata_ptr: [*]const u8, calldata_len: usize) sdk.ByteSlice {
      sdk.heap.reset();
      // Your contract logic
      return sdk.ByteSlice.from(result);
  }
  ```

  **Modules**: `storage`, `context`, `crypto`, `events`, `math`, `guards`

* Rust SDK

  The [Rust SDK](/reference/sdk/#rust-sdk) provides low-level control for contracts:

  ```rust
  use contract_sdk::{Host, Address};


  // Storage
  let value = Host::storage_read(key)?;
  Host::storage_write(key, &data)?;


  // Context
  let caller = Host::caller();
  let block = Host::block_number();
  ```

  **Features**: Host API, storage collections, ABI helpers

* IDL Codegen

  Generate type-safe bindings from IDL:

  ```bash
  just idl-abi-gen \
    --idl contracts/mycontract/mycontract.idl \
    --out-dir contracts/mycontract/src \
    --zig-stubs --rust-contract
  ```

### Tools

[Section titled “Tools”](#tools)

| Tool                 | Purpose                                                             |
| -------------------- | ------------------------------------------------------------------- |
| **TUI**              | Interactive terminal for contract calls, tx history, block explorer |
| **Wallet Extension** | Browser extension for signing and account management                |
| **RPC**              | Full JSON-RPC API with simulation, proofs, and subscriptions        |

***

## DeFi Infrastructure

[Section titled “DeFi Infrastructure”](#defi-infrastructure)

Ashen ships with production-ready DeFi contracts:

AMM & DEX

Constant-product AMM pools, concentrated liquidity, stableswap curves, and a DEX router for optimal routing.

Lending

Lending markets with collateralization, liquidations, and interest rate models.

Staking & Rewards

Stake pools with delegation, reward gauges for liquidity mining.

Vaults

ERC-4626 style vaults with pluggable strategies for yield optimization.

### Available Contracts

[Section titled “Available Contracts”](#available-contracts)

| Category       | Contracts                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------- |
| **Trading**    | `amm_pool_v1`, `concentrated_liquidity_v1`, `stable_swap_v1`, `order_book_v1`, `dex_router_v1` |
| **Lending**    | `lending_market_v1`                                                                            |
| **Staking**    | `stake_pool_v1`, `reward_gauge_v1`                                                             |
| **Vaults**     | `vault_v1`, `vault_strategy_v1`                                                                |
| **Tokens**     | `sft_v1` (semi-fungible token)                                                                 |
| **Governance** | `timelock_governor_v1`                                                                         |
| **Utilities**  | `fee_sponsor_v1`, `price_oracle_v1`                                                            |

***

## Cross-Chain & Oracles

[Section titled “Cross-Chain & Oracles”](#cross-chain--oracles)

### Bridge Integrations

[Section titled “Bridge Integrations”](#bridge-integrations)

Axelar GMP

General Message Passing for cross-chain contract calls.

Hyperlane

Interchain Security Modules for verified message passing.

Wormhole

Guardian-verified cross-chain messaging.

### Oracle Integrations

[Section titled “Oracle Integrations”](#oracle-integrations)

| Oracle        | Contract             | Use Case                   |
| ------------- | -------------------- | -------------------------- |
| **Pyth**      | `pyth_oracle_v1`     | High-frequency price feeds |
| **Chainlink** | `chainlink_ocr2_v1`  | OCR2 aggregated feeds      |
| **Redstone**  | `redstone_oracle_v1` | On-demand price data       |

***

## Fee Sponsorship

[Section titled “Fee Sponsorship”](#fee-sponsorship)

The `fee_sponsor_v1` contract enables gasless transactions:

* **Sponsors** deposit funds and set policies
* **Users** submit transactions without holding native tokens
* **Contracts** can sponsor their own users

Perfect for onboarding new users or subsidizing specific actions.

***

## Proofs-First Architecture

[Section titled “Proofs-First Architecture”](#proofs-first-architecture)

Every piece of state is provable:

* **Blake3 BMT commitments** — hierarchical Merkle trees per account
* **Membership proofs** — prove a key exists with its value
* **Exclusion proofs** — prove a key does NOT exist (predecessor/successor)
* **Finalized history MMR** — Merkle Mountain Range over all finalized blocks
* **State proofs RPC** — request proofs for any storage slot

Light clients can verify anything without trusting the RPC.

***

## Quick Links

[Section titled “Quick Links”](#quick-links)

[Quickstart ](/getting-started/quickstart/)Get a local node running in minutes

[Installation ](/getting-started/installation/)Build from source

[Architecture ](/architecture/overview/)System design deep-dive

[Ashen SDK ](/contracts/ashen-sdk/)Write your first contract

# Quickstart

> Get a local node running in minutes

## Overview

[Section titled “Overview”](#overview)

This guide gets you from zero to a running local node with a deployed contract in under 5 minutes.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* **Rust** (nightly toolchain)
* **just** command runner (`cargo install just`)
* **jq** for JSON parsing
* **curl** for RPC calls

## 1. Build the Project

[Section titled “1. Build the Project”](#1-build-the-project)

```bash
# Clone and enter the repo
cd chain


# Build everything
just build
```

## 2. Generate a Key

[Section titled “2. Generate a Key”](#2-generate-a-key)

```bash
# Generate an ed25519 keypair
ashen keygen --json > ./target/dev.key.json


# Export for CLI usage
export ASHEN_PRIVATE_KEY=@./target/dev.key.json


# Get your address
ALICE_ADDR=$(jq -r .data.address ./target/dev.key.json)
echo "Your address: $ALICE_ADDR"
```

## 3. Initialize and Run a Local Node

[Section titled “3. Initialize and Run a Local Node”](#3-initialize-and-run-a-local-node)

```bash
# Initialize the node with funds allocated to your address
just devnet-node init --data-dir ./node-data --alloc "$ALICE_ADDR=13370000000000"


# Run the node (in a separate terminal)
just node
```

The node will start producing blocks at `http://127.0.0.1:3030`.

## 4. Verify the Node is Running

[Section titled “4. Verify the Node is Running”](#4-verify-the-node-is-running)

```bash
# Check chain status
just ashen status


# Check your account balance
just ashen account --address "$ALICE_ADDR"


# Or via justfile shortcut
just status
```

## 5. Deploy a Contract

[Section titled “5. Deploy a Contract”](#5-deploy-a-contract)

```bash
# Build a contract (e.g., the SFT token)
just contract-build --manifest-path contracts/sft_v1/Cargo.toml


# Bundle and deploy it
just contract-deploy --elf target/riscv64imac-unknown-none-elf/release/sft_v1 --wait
```

## 6. Interact with the Contract

[Section titled “6. Interact with the Contract”](#6-interact-with-the-contract)

```bash
# Set your contract address (from deploy output)
CONTRACT=0x...


# View call (read-only)
just ashen contract view \
  --idl contracts/sft_v1/sft_v1.idl \
  --contract "$CONTRACT" \
  --interface SftV1 \
  --method total_supply


# State-changing call (simulate first)
just ashen contract call \
  --idl contracts/sft_v1/sft_v1.idl \
  --contract "$CONTRACT" \
  --interface SftV1 \
  --method mint \
  --args '{"to":"'"$ALICE_ADDR"'","amount":"1"}' \
  --simulate-only
```

## Quick Reference

[Section titled “Quick Reference”](#quick-reference)

| Task             | Command                                      |
| ---------------- | -------------------------------------------- |
| Build workspace  | `just build`                                 |
| Run local node   | `just node`                                  |
| Check status     | `just ashen status`                          |
| Generate keypair | `ashen keygen --json`                        |
| Build contract   | `just contract-build --manifest-path <path>` |
| Deploy contract  | `just contract-deploy --elf <path> --wait`   |
| Check status     | `just status`                                |
| Account info     | `just account <address>`                     |

## Running a Multi-Node Testnet

[Section titled “Running a Multi-Node Testnet”](#running-a-multi-node-testnet)

For testing with multiple validators:

```bash
# Generate testnet config (3 validators)
just testnet-local-generate


# Run the testnet
just testnet-local-run
```

This starts 3 validators with an RPC server on port 3030.

## Environment Variables

[Section titled “Environment Variables”](#environment-variables)

| Variable            | Description                       | Default                 |
| ------------------- | --------------------------------- | ----------------------- |
| `NODE_RPC_URL`      | RPC endpoint                      | `http://127.0.0.1:3030` |
| `NODE_AUTH_TOKEN`   | Optional auth token               | none                    |
| `ASHEN_PRIVATE_KEY` | Private key (hex or `@file.json`) | required for txs        |

## Next Steps

[Section titled “Next Steps”](#next-steps)

* [Using the CLI](/guides/using-the-cli/) - Full `ashen` CLI documentation
* [Writing Contracts](/contracts/ashen-sdk/) - Build smart contracts with the Zig SDK
* [Architecture](/architecture/overview/) - Understand how the chain works

# Bridge Integrations

> Integrate Axelar, Wormhole, and Hyperlane with Ashen

## Overview

[Section titled “Overview”](#overview)

Ashen does not ship a canonical bridge. Instead, it provides reference contracts for verifying messages from major bridge networks and leaves the application wiring to you. This guide outlines the common architecture, provider-specific notes, and a practical checklist for integration.

Reference contracts live in `contracts/`:

* `axelar_gmp_v1` for Axelar GMP
* `wormhole_core_v1` for Wormhole VAAs
* `hyperlane_ism_v1` for Hyperlane ISM verification

See `/contracts/examples/` for a summary of each.

## Architecture

[Section titled “Architecture”](#architecture)

Every integration has the same core components:

1. **Source chain sender**: emits or queues the outbound message.
2. **Bridge network**: signs, attests, or otherwise proves the message.
3. **Relayer**: submits the proof payload to Ashen.
4. **Verifier contract**: validates signatures and replay protection.
5. **Destination handler**: your app contract that consumes the message.

## Message Flow (Generic)

[Section titled “Message Flow (Generic)”](#message-flow-generic)

1. The source chain sender emits a message with destination and payload.

2. The bridge network signs or validates the message and produces a proof.

3. A relayer submits the proof to the verifier contract on Ashen.

4. The verifier checks:

   * chain or domain identifiers
   * signer/validator/operator threshold
   * message structure and hashes
   * replay protection and ordering

5. The verifier calls your destination handler with the decoded payload.

## Provider Notes

[Section titled “Provider Notes”](#provider-notes)

### Axelar GMP

[Section titled “Axelar GMP”](#axelar-gmp)

Axelar uses operator sets to sign command batches. Typical integration steps:

* Deploy `axelar_gmp_v1` and initialize it with the current operator set.
* Accept `execute` calls from relayers and validate command approvals.
* Record command IDs to prevent replays.
* Hand off decoded payloads to your app contract.

### Wormhole

[Section titled “Wormhole”](#wormhole)

Wormhole uses guardian signatures over a VAA (Verified Action Approval).

* Deploy `wormhole_core_v1` and configure the guardian set and threshold.
* Validate emitter address, sequence, and chain ID in each VAA.
* Persist consumed VAAs to block replays.
* Route verified payloads to your handler contract.

### Hyperlane

[Section titled “Hyperlane”](#hyperlane)

Hyperlane relies on an ISM (Interchain Security Module) to verify messages.

* Deploy `hyperlane_ism_v1` with validator sets per origin domain.
* Check the message origin domain and nonce ordering.
* Validate the ISM proof and only then dispatch to your handler.

## Integration Checklist

[Section titled “Integration Checklist”](#integration-checklist)

Use this list before going live:

* [ ] Map external chain IDs or domains to Ashen IDs consistently.
* [ ] Enforce replay protection in the verifier.
* [ ] Restrict dispatch to a dedicated handler contract.
* [ ] Validate payload schemas and lengths before decoding.
* [ ] Configure operator/guardian/validator sets with rotation procedures.
* [ ] Test with local harnesses and provider testnets.

## Testing Tips

[Section titled “Testing Tips”](#testing-tips)

* Use `/guides/contract-testing/` to unit test verifier contracts in isolation.
* Build a small handler contract that records payloads for assertions.
* Keep test payloads deterministic and include invalid cases.

## Related

[Section titled “Related”](#related)

* `/contracts/examples/` for reference contract summaries
* `/guides/contract-testing/` for harness-based tests
* `/concepts/private-mempool/` for sealed transaction behavior

# Chaos Testing & Devnet Scenarios

> Deterministic devnet chaos suites and how to run them

## Overview

[Section titled “Overview”](#overview)

Ashen ships two complementary chaos tools:

1. **`devnet` binary**: quick deterministic simulations with latency/loss knobs.
2. **`devnet_replay` tests**: scripted scenarios with golden-state checks.

Use `devnet` for fast iteration and `devnet_replay` for regression coverage and state-root determinism.

## Quick Chaos Runs (devnet binary)

[Section titled “Quick Chaos Runs (devnet binary)”](#quick-chaos-runs-devnet-binary)

```bash
just devnet-small
just devnet-chaos
```

`devnet-chaos` injects packet loss and latency via env vars:

```bash
DEVNET_SUCCESS_RATE=0.9 \
DEVNET_LINK_LATENCY_MS=25 \
DEVNET_LINK_JITTER_MS=10 \
just devnet-chaos
```

See `/guides/devnet/` for the full parameter list.

## Deterministic Scenario Suite (devnet\_replay)

[Section titled “Deterministic Scenario Suite (devnet\_replay)”](#deterministic-scenario-suite-devnet_replay)

Run the full suite:

```bash
cargo test --test devnet_replay
```

Regenerate goldens:

```bash
REGENERATE_GOLDENS=1 cargo test --test devnet_replay
```

Run a single scenario by test name:

```bash
cargo test --test devnet_replay baseline_4_validators_happy_path
cargo test --test devnet_replay network_partition_and_heal
```

Golden files live under `tests/goldens/` and assert state-root stability across nodes and runs.

## Scenario Catalog (Common)

[Section titled “Scenario Catalog (Common)”](#scenario-catalog-common)

These scenarios are defined in `tests/devnet_replay.rs`:

| Scenario              | What it stresses                   |
| --------------------- | ---------------------------------- |
| `baseline_4v_happy`   | 4 validators, happy path           |
| `baseline_2v_happy`   | 2 validators, happy path           |
| `partition_heal`      | network split + heal               |
| `high_latency`        | sustained high latency             |
| `lossy_network`       | packet loss                        |
| `high_jitter`         | reordering and jitter              |
| `delayed_link_0_to_1` | targeted slow link                 |
| `node_crash_recovery` | node isolate + restore             |
| `silent_byzantine`    | node receives but stops sending    |
| `leader_isolation`    | isolate leader and observe handoff |
| `cascading_failures`  | sequential node isolation          |
| `txpool_burst`        | burst transaction load             |
| `sustained_tx_load`   | continuous tx pressure             |
| `combined_stress`     | mixed network + tx stress          |
| `soak_*`              | long-running soak variants         |
| `replay_*`            | record/replay determinism          |

See the test file for the complete list and parameters.

## Network Events Used by Scenarios

[Section titled “Network Events Used by Scenarios”](#network-events-used-by-scenarios)

The scenario harness supports these events:

* `Partition { at_step, partitioned_nodes }`
* `HealPartition { at_step }`
* `ModifyLink { at_step, from_node, to_node, latency_ms, jitter_ms, success_rate }`
* `IsolateNode { at_step, node_idx }`
* `RestoreNode { at_step, node_idx }`
* `SilenceNode { at_step, node_idx }`

These events are applied at deterministic steps, making failures reproducible under a fixed seed.

## Tips

[Section titled “Tips”](#tips)

* Use a fixed `seed` for reproducibility.
* Keep `steps` small when iterating; increase for soak tests.
* Use `-- --nocapture` to see detailed logs from the test runner.

## Related

[Section titled “Related”](#related)

* `/guides/devnet/` for devnet binary usage
* `tests/devnet_replay.rs` for scenario definitions
* `tests/goldens/` for golden outputs

# Contract Testing

> Test Zig and Rust contracts without a full node

## Overview

[Section titled “Overview”](#overview)

`vm-test-harness` provides an in-memory host that lets you execute contracts locally without running a node. It’s ideal for unit-style tests, storage fixtures, event assertions, and cross-contract call flows.

Key pieces:

* **`TestHost`**: In-memory storage, logs, balances, block context
* **`ContractHarness`**: Load and execute Zig/Rust contract ELFs
* **`TestAccounts`**: Deterministic test addresses (alice, bob, carol, dave, eve, treasury)
* **Helpers**: Calldata builders, result parsers, event assertions, storage fixtures, snapshots

## Import

[Section titled “Import”](#import)

The crate lives in the workspace:

```rust
use vm_test_harness::{
    ContractHarness, TestHost, TestAccounts, StorageFixture,
    build_calldata, build_calldata_no_args,
    parse_result, assert_call_ok,
    assert_event_emitted, assert_event_count,
    assert_storage_u128,
};
```

## Build Artifacts First

[Section titled “Build Artifacts First”](#build-artifacts-first)

You must build contract ELFs before loading them in tests:

```bash
# Zig
cd contracts/my_zig && zig build -Doptimize=ReleaseSmall


# Rust
just contract-build --manifest-path contracts/my_rust/Cargo.toml


# All contracts
just contract-build-all
```

## Quick Start

[Section titled “Quick Start”](#quick-start)

```rust
#[test]
fn my_token_initializes() {
    // Skip gracefully if ELF not built yet
    let Some(harness) = ContractHarness::from_zig_artifact_or_skip(
        "contracts/my_token/zig-out/bin/my_token",
        "contracts/my_token",
    ).unwrap() else { return };


    let mut host = TestHost::new();
    let accounts = TestAccounts::new();
    host.seed_balances(&accounts, 100_000);


    // Build calldata: 4-byte selector + borsh-encoded args
    let calldata = build_calldata(SELECTOR_INITIALIZE, &InitArgs { fee_bps: 30 });
    let result = harness.call(
        &mut host,
        accounts.alice, // origin
        b"my_token",    // contract address
        &calldata,
        1_000_000,      // gas limit
    );


    assert_call_ok(&result, "init should succeed");
    assert_event_emitted(&host, "Initialized()");
    assert_storage_u128(&host, b"my_token", b"fee_bps", 30);
}
```

## Test Accounts

[Section titled “Test Accounts”](#test-accounts)

`TestAccounts` provides six deterministic addresses derived from `keccak256(label)`:

```rust
let accounts = TestAccounts::new();
// accounts.alice, accounts.bob, accounts.carol,
// accounts.dave, accounts.eve, accounts.treasury
```

## Calldata & Results

[Section titled “Calldata & Results”](#calldata--results)

Calldata format: `selector (4 bytes) || borsh(args)`.

```rust
// With arguments
let calldata = build_calldata(SELECTOR_TRANSFER, &TransferArgs { to, amount });


// Without arguments
let calldata = build_calldata_no_args(SELECTOR_TOTAL_SUPPLY);
```

Parse return data:

```rust
let result = harness.call(&mut host, origin, contract, &calldata, gas);
assert_call_ok(&result, "call should succeed");


// Typed result parsing
let supply: u128 = parse_result(&result.outcome.return_data)?;
```

## Storage Fixtures

[Section titled “Storage Fixtures”](#storage-fixtures)

```rust
use vm_test_harness::{TestHost, StorageFixture, assert_storage_u128, assert_storage_empty};


let mut host = TestHost::new();
StorageFixture::new(&mut host)
    .contract(b"amm_pool")
    .set_u128(b"reserve0", 1_000_000)
    .set_u128(b"reserve1", 500_000)
    .set_u64(b"swap_fee_bps", 30)
    .done();


// ... execute swap ...
assert_storage_u128(&host, b"amm_pool", b"reserve0", 900_000);
assert_storage_empty(&host, b"amm_pool", b"pending_admin");
```

## Event Assertions

[Section titled “Event Assertions”](#event-assertions)

```rust
use vm_test_harness::{TestHost, assert_event_emitted, assert_event_with_topics, assert_event_count};
use vm_test_harness::topic_from_u128;


let host = TestHost::new();
// ... execute contract ...


assert_event_emitted(&host, "Transfer(address,address,uint256)");
let from = [1u8; 32];
let to = [2u8; 32];
let amount = topic_from_u128(1000);
assert_event_with_topics(&host, "Transfer(address,address,uint256)", &[from, to, amount]);
assert_event_count(&host, 1);
```

## Cross‑Contract Calls

[Section titled “Cross‑Contract Calls”](#crosscontract-calls)

Register multiple programs with the host and call by address:

```rust
let mut host = TestHost::new();
let a = ContractHarness::from_zig_artifact("contracts/a/zig-out/bin/a").unwrap();
let b = ContractHarness::from_zig_artifact("contracts/b/zig-out/bin/b").unwrap();


host.register_program(b"contract_a", a.program().clone());
host.register_program(b"contract_b", b.program().clone());
```

Then use normal `ContractHarness::call` flows to exercise call graphs.

## Snapshots

[Section titled “Snapshots”](#snapshots)

```rust
let mut host = TestHost::new();
let snapshot = host.snapshot();
// mutate state ...
host.restore_snapshot(snapshot);
```

## Block Advancement

[Section titled “Block Advancement”](#block-advancement)

Advance the host’s block context between calls:

```rust
host.advance_block(); // increments block_number, updates timestamp
```

## Zig-Side Testing

[Section titled “Zig-Side Testing”](#zig-side-testing)

The Ashen SDK includes a Zig testing module for unit tests that run inside `zig test` (no Rust harness needed):

```zig
const sdk = @import("ashen-sdk");
const testing = sdk.testing;


test "balance updates correctly" {
    testing.assertStorageU128("balance", 1000);
    testing.assertEventEmitted("Transfer(address,address,uint256)");
    testing.assertEqU128(actual, expected);
}
```

The Zig `testing_host` provides an in-memory storage backend with mock syscalls, callable via `testing_host.init()` / `testing_host.deinit()`.

## Running Tests

[Section titled “Running Tests”](#running-tests)

```bash
# All contract integration tests
cargo test -p vm-runtime


# Single contract
cargo test -p vm-runtime --test amm_pool_v1


# Single test function
cargo test -p vm-runtime --test amm_pool_v1 -- amm_pool_initial_liquidity


# With output
cargo test -p vm-runtime --test amm_pool_v1 -- --nocapture
```

Tests that use `from_zig_artifact_or_skip` will print a build hint and skip gracefully if the ELF artifact is missing.

## Tips

[Section titled “Tips”](#tips)

* Use `from_zig_artifact_or_skip()` instead of `from_zig_artifact()` to avoid test failures when artifacts are not built.
* Use `ResourceLimits` to simulate production caps.
* Use `snapshot()` / `restore_snapshot()` to test rollback behavior.
* Prefer deterministic fixtures for reproducible tests.
* Treat harness tests as **fast unit tests**, and use devnet tests for end-to-end.

## Related

[Section titled “Related”](#related)

* [Deploying Contracts](/guides/deploying-contracts/) — building artifacts
* [Zig Guide](/contracts/zig-guide/) — Zig contract authoring
* [Rust Guide](/contracts/rust-guide/) — Rust contract authoring
* [Precompiles & Syscalls](/reference/precompiles/) — available syscalls
* [Debugging](/guides/debugging/) — debugging contract execution

# Debugging

> Time-travel debugging and trace tools for transaction analysis

Debug and trace tools for transaction analysis on the chain.

## Quick Start

[Section titled “Quick Start”](#quick-start)

```bash
# Trace a transaction (tree view)
ashen debug trace 0xabc123...


# Interactive replay
ashen debug replay 0xabc123... --step


# Gas analysis
ashen debug gas 0xabc123...
```

## Commands

[Section titled “Commands”](#commands)

### `ashen debug trace`

[Section titled “ashen debug trace”](#ashen-debug-trace)

Trace an already-included transaction and display the call tree.

```bash
ashen debug trace <TX_HASH> [OPTIONS]


Options:
  --max-depth <N>      Maximum call depth (default: 8)
  --format <FORMAT>    Output: "tree" (default), "json", "chrome"
  -o, --output <PATH>  Write to file instead of stdout
  --rpc-url <URL>      RPC endpoint (env: NODE_RPC_URL)
```

**Examples:**

```bash
# Human-readable tree
ashen debug trace 0xabc123


# Full JSON (for programmatic use)
ashen debug trace 0xabc123 --format json -o trace.json


# Chrome Trace Format (open in chrome://tracing)
ashen debug trace 0xabc123 --format chrome -o trace.json
```

**Tree output:**

```plaintext
Transaction: 0xabc123...
Block: 42


call 0x1234...5678 -> 0xabcd...ef01 (gas: 45000/100000)
  input: 0xa9059cbb000000000000000000000000...
  storage.write: 0xbalance:alice (gas: 5000)
  storage.write: 0xbalance:bob (gas: 5000)
  event: 0xabcd...ef01 topics=3
  call 0xabcd...ef01 -> 0x9876...5432 (gas: 12000/50000)
    storage.read: 0xallowance (gas: 2100)
```

### `ashen debug trace-call`

[Section titled “ashen debug trace-call”](#ashen-debug-trace-call)

Trace a read-only view call without submitting a transaction.

```bash
ashen debug trace-call <CONTRACT> <CALLDATA> [OPTIONS]


Options:
  --origin <ADDRESS>   Caller address (defaults to zero)
  --gas-limit <N>      Gas limit (default: 1000000)
  --value <N>          Attached value (default: 0)
  --format <FORMAT>    Output: "tree", "json", "chrome"
  -o, --output <PATH>  Write to file
```

**Example:**

```bash
ashen debug trace-call 0xcontract 0x70a08231000000000000000000000000abcdef
```

### `ashen debug replay`

[Section titled “ashen debug replay”](#ashen-debug-replay)

Step through a transaction interactively, inspecting state at each operation.

```bash
ashen debug replay <TX_HASH> [OPTIONS]


Options:
  --step                Single-step mode (pause after each operation)
  -b, --breakpoint <BP> Set breakpoint(s), repeatable
  --rpc-url <URL>       RPC endpoint
```

**Breakpoint formats:**

| Format        | Description                      | Example                        |
| ------------- | -------------------------------- | ------------------------------ |
| `step:N`      | Break at operation N             | `--breakpoint step:5`          |
| `storage:KEY` | Break on storage op matching KEY | `--breakpoint storage:balance` |
| `gas:N`       | Break when gas exceeds N         | `--breakpoint gas:50000`       |

**Interactive commands:**

| Key         | Action                                |
| ----------- | ------------------------------------- |
| Enter / `n` | Step to next operation                |
| `s<N>`      | Seek to step N (e.g., `s5`)           |
| `r`         | Run to next breakpoint (or end)       |
| `i`         | Inspect current operation (full JSON) |
| `b<spec>`   | Add breakpoint (e.g., `bstep:10`)     |
| `q`         | Quit                                  |

**Example session:**

```bash
$ ashen debug replay 0xabc123 --step
Replaying 0xabc123 (6 operations, block 42)
Commands: [enter]=step, [n]=next, [s]=seek N, [b]=add breakpoint, [r]=run, [i]=inspect, [q]=quit


[  0] call 0x1234... -> 0xabcd... (gas: 45000)
        storage.write balance:alice
(step 0/5) >
[  1] call 0xabcd... -> 0x9876... (gas: 12000)
(step 1/5) > i
{
  "step": 1,
  "depth": 1,
  "op_type": "call",
  "from": "0xabcd...",
  "to": "0x9876...",
  "gas_used": 12000
}
(step 1/5) > r
[  5] call 0x1234... -> 0xabcd... (gas: 45000)
  End of trace.
```

### `ashen debug gas`

[Section titled “ashen debug gas”](#ashen-debug-gas)

Show gas breakdown for a transaction.

```bash
ashen debug gas <TX_HASH> [OPTIONS]


Options:
  --rpc-url <URL>  RPC endpoint
```

**Output:**

```plaintext
Gas Analysis: 0xabc123...
Block: 42
-----------------------------------
Total gas used: 45000
Gas limit:      100000
Utilization:    45.0%


Storage operations (3):
  write 0xbalance:ali... (gas: 5000)
  write 0xbalance:bob... (gas: 5000)
  read 0xallowance... (gas: 2100)
  Total storage gas: 12100


Child calls (1):
  call 0x1234...5678 -> 0x9876...5432 (gas: 12000, OK)
```

## Workflows

[Section titled “Workflows”](#workflows)

### Debug a Failed Transaction

[Section titled “Debug a Failed Transaction”](#debug-a-failed-transaction)

```bash
# 1. Check the transaction status
ashen tx by-hash --tx-hash 0xfailed... --wait


# 2. Get the full trace to see where it failed
ashen debug trace 0xfailed...


# 3. Inspect storage operations step by step
ashen debug replay 0xfailed... --step


# 4. Check gas usage
ashen debug gas 0xfailed...
```

### Gas Optimization

[Section titled “Gas Optimization”](#gas-optimization)

```bash
# 1. Get gas breakdown
ashen debug gas 0xtx...


# 2. Export full trace for analysis
ashen debug trace 0xtx... --format json -o trace.json


# 3. Open in Chrome for visual inspection
ashen debug trace 0xtx... --format chrome -o chrome-trace.json
# Then open chrome://tracing and load chrome-trace.json
```

### Compare Two Executions

[Section titled “Compare Two Executions”](#compare-two-executions)

```bash
# Export both as JSON
ashen debug trace 0xtx_before... --format json -o before.json
ashen debug trace 0xtx_after... --format json -o after.json


# Diff with your preferred tool
diff before.json after.json
# or: jq for structured comparison
```

## Chrome Trace Format

[Section titled “Chrome Trace Format”](#chrome-trace-format)

The `--format chrome` option exports traces in [Chrome Trace Format](https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview), viewable in:

* `chrome://tracing` (Chrome/Chromium)
* [Perfetto UI](https://ui.perfetto.dev/)
* [Speedscope](https://www.speedscope.app/)

Each call frame becomes a duration event showing gas usage and call depth.

## Environment Variables

[Section titled “Environment Variables”](#environment-variables)

| Variable          | Description       | Default                 |
| ----------------- | ----------------- | ----------------------- |
| `NODE_RPC_URL`    | RPC endpoint URL  | `http://127.0.0.1:3030` |
| `NODE_AUTH_TOKEN` | Bearer auth token | (none)                  |

## Programmatic Access (RPC)

[Section titled “Programmatic Access (RPC)”](#programmatic-access-rpc)

The debug commands use these RPC methods directly:

| RPC Method                         | CLI Command              |
| ---------------------------------- | ------------------------ |
| `NodeRpcV1.chain_traceTransaction` | `ashen debug trace`      |
| `NodeRpcV1.chain_traceCall`        | `ashen debug trace-call` |
| `NodeRpcV1.tx_simulate_trace`      | (simulation with trace)  |

### Example: Direct RPC Call

[Section titled “Example: Direct RPC Call”](#example-direct-rpc-call)

```bash
curl -X POST http://localhost:3030/v2/rpc \
  -H 'Content-Type: application/json' \
  -d '{
    "id": 1,
    "method": "NodeRpcV1.chain_traceTransaction",
    "params": {
      "tx_hash": "0xabc123...",
      "max_depth": 8
    }
  }'
```

***

## DAP Debugger (VS Code Integration)

[Section titled “DAP Debugger (VS Code Integration)”](#dap-debugger-vs-code-integration)

The DAP (Debug Adapter Protocol) adapter enables interactive debugging of contract execution directly in VS Code or any DAP-compatible IDE.

### Quick Start

[Section titled “Quick Start”](#quick-start-1)

```bash
# 1. Build the DAP adapter
cargo build -p dap-adapter


# 2. Build your contract with debug symbols
cd contracts/zig_fixture
zig build


# 3. Open VS Code and start debugging (F5)
```

### Setup

[Section titled “Setup”](#setup)

#### 1. Install the DAP Adapter

[Section titled “1. Install the DAP Adapter”](#1-install-the-dap-adapter)

target/release/ashen-dap

```bash
cargo build -p dap-adapter --release
```

#### 2. Configure VS Code

[Section titled “2. Configure VS Code”](#2-configure-vs-code)

Create or update `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Debug Contract",
            "type": "ashen-vm",
            "request": "launch",
            "program": "${workspaceFolder}/contracts/zig_fixture/zig-out/bin/zig_fixture",
            "sourceDir": "${workspaceFolder}/contracts/zig_fixture/src",
            "stopOnEntry": true,
            "trace": true
        }
    ]
}
```

#### 3. Configure the Debug Extension

[Section titled “3. Configure the Debug Extension”](#3-configure-the-debug-extension)

In VS Code settings, point to the adapter binary:

```json
{
    "ashen-vm.adapterPath": "${workspaceFolder}/target/release/ashen-dap"
}
```

### Supported Features

[Section titled “Supported Features”](#supported-features)

| Feature         | Description                        |
| --------------- | ---------------------------------- |
| Breakpoints     | Set breakpoints on source lines    |
| Step Over (F10) | Execute next operation             |
| Step Into (F11) | Step into function calls           |
| Step Out        | Step out of current function       |
| Step Back       | Time-travel to previous operation  |
| Variables       | Inspect registers, memory, storage |
| Stack Trace     | View call stack                    |
| Continue (F5)   | Run to next breakpoint             |
| Pause           | Pause execution                    |

### Launch Configuration Options

[Section titled “Launch Configuration Options”](#launch-configuration-options)

| Option        | Type    | Description                          |
| ------------- | ------- | ------------------------------------ |
| `program`     | string  | Path to contract ELF binary          |
| `sourceDir`   | string  | Path to source directory for mapping |
| `stopOnEntry` | boolean | Pause at contract entry point        |
| `trace`       | boolean | Enable execution trace recording     |
| `mode`        | string  | `"launch"` or `"replay"`             |
| `txHash`      | string  | Transaction hash (replay mode only)  |
| `rpcUrl`      | string  | RPC endpoint (replay mode only)      |

### Debug Session Example

[Section titled “Debug Session Example”](#debug-session-example)

```plaintext
1. Set breakpoint at line 28 in main.zig (click gutter)
2. Press F5 to start debugging
3. Execution pauses at entry (stopOnEntry: true)
4. Press F5 to continue to breakpoint
5. Use Variables panel to inspect state:
   - Registers: pc, sp, a0-a7
   - Memory: heap, stack contents
   - Storage: contract storage slots
6. Press F10 to step over
7. Press Shift+F10 to step back (time-travel)
8. Press F5 to continue or Shift+F5 to stop
```

### Debugging Modes

[Section titled “Debugging Modes”](#debugging-modes)

#### Launch Mode

[Section titled “Launch Mode”](#launch-mode)

Debug a contract from the start with specified calldata:

```json
{
    "type": "ashen-vm",
    "request": "launch",
    "program": "path/to/contract.elf",
    "calldata": "0x4543484f48656c6c6f"
}
```

#### Replay Mode

[Section titled “Replay Mode”](#replay-mode)

Debug an already-executed transaction:

```json
{
    "type": "ashen-vm",
    "request": "launch",
    "mode": "replay",
    "txHash": "0xabc123...",
    "rpcUrl": "http://127.0.0.1:3030"
}
```

### Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**Breakpoints show as unverified (gray)**

* Contract must be built with debug symbols
* Source paths must match exactly
* Try rebuilding without optimization

**“Session not initialized” error**

* Check that ashen-dap binary is accessible
* Verify VS Code extension configuration

**Step back doesn’t work**

* Set `trace: true` in launch configuration
* Trace recording must be enabled for time-travel

**Variables panel is empty**

* Click on a stack frame first
* Expand the Registers/Memory/Storage scopes

# Deploying Contracts

> Build and deploy smart contracts to Ashen

This guide covers the complete workflow for deploying smart contracts to Ashen, from building to verification.

## Quick Start

[Section titled “Quick Start”](#quick-start)

```bash
# 1. Build the contract
ashen dev build --manifest-path contracts/my_contract/Cargo.toml


# 2. Deploy (ELF + IDL)
ashen deploy submit \
  --bundle target/riscv64imac-unknown-none-elf/release/my_contract \
  --idl contracts/my_contract/my_contract.idl \
  --key $ASHEN_PRIVATE_KEY \
  --wait
```

***

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* **Pinned toolchain** — use `devenv shell` or the [contract builder image](/guides/deterministic-builds/) to ensure your ELFs match what validators expect
* **Rust** with the `riscv64imac-unknown-none-elf` target
* A **funded account** for deployment gas fees
* Your **private key** (ed25519 hex or keystore reference)

```bash
# Install RISC-V target
rustup target add riscv64imac-unknown-none-elf


# Generate a keypair if needed
ashen keygen --json > ./dev.key.json
export ASHEN_PRIVATE_KEY=@./dev.key.json
```

***

## Step 1: Build the Contract

[Section titled “Step 1: Build the Contract”](#step-1-build-the-contract)

### Rust Contracts

[Section titled “Rust Contracts”](#rust-contracts)

```bash
ashen dev build --manifest-path contracts/my_contract/Cargo.toml


# With custom output path
ashen dev build \
  --manifest-path contracts/my_contract/Cargo.toml \
  --out-elf ./my_contract.elf


# With debug info (for tracing)
ashen dev build \
  --manifest-path contracts/my_contract/Cargo.toml \
  --debuginfo


# Verbose output
ashen dev build \
  --manifest-path contracts/my_contract/Cargo.toml \
  --verbose
```

Output: `target/riscv64imac-unknown-none-elf/release/<contract_name>`

### Zig Contracts

[Section titled “Zig Contracts”](#zig-contracts)

Zig contracts use the Ashen SDK and compile via zig build:

```bash
cd contracts/my_zig_contract
zig build -Doptimize=ReleaseSmall
```

Output: `zig-out/bin/<contract_name>`

### Build Options

[Section titled “Build Options”](#build-options)

| Option            | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `--manifest-path` | Path to `Cargo.toml`                                    |
| `--target`        | Target triple (default: `riscv64imac-unknown-none-elf`) |
| `--release`       | Release build (default: true)                           |
| `--debuginfo`     | Preserve DWARF debug info for tracing                   |
| `--bin`           | Binary name (if multiple in workspace)                  |
| `--out-elf`       | Custom output path                                      |
| `--verbose`       | Show build commands                                     |

***

## Step 2: Create IDL

[Section titled “Step 2: Create IDL”](#step-2-create-idl)

Every contract needs an IDL (Interface Definition Language) file describing its methods, types, and events.

### IDL Structure

[Section titled “IDL Structure”](#idl-structure)

my\_contract.idl

```idl
interface MyContract {
    // View method (read-only)
    fn balance_of(account: Address) -> u128;


    // Mutating method
    fn transfer(to: Address, amount: u128) -> ();


    // Events
    event Transfer {
        from: Address indexed,
        to: Address indexed,
        amount: u128,
    }
}
```

### Generate IDL from Rust

[Section titled “Generate IDL from Rust”](#generate-idl-from-rust)

If using the Rust SDK with `#[contract]` macros:

```bash
just idl-abi-gen \
  --idl contracts/my_contract/my_contract.idl \
  --out-dir contracts/my_contract/src \
  --rust-contract
```

### Validate IDL

[Section titled “Validate IDL”](#validate-idl)

```bash
ashen idl validate ./my_contract.idl
```

***

## Step 3: Deploy

[Section titled “Step 3: Deploy”](#step-3-deploy)

The `ashen deploy submit` command takes the ELF (via `--bundle`) and an optional IDL (via `--idl`) and submits the deployment transaction in one step.

### Basic Deployment

[Section titled “Basic Deployment”](#basic-deployment)

```bash
ashen deploy submit \
  --bundle target/riscv64imac-unknown-none-elf/release/my_contract \
  --idl contracts/my_contract/my_contract.idl \
  --key $ASHEN_PRIVATE_KEY
```

### Deploy and Wait for Confirmation

[Section titled “Deploy and Wait for Confirmation”](#deploy-and-wait-for-confirmation)

```bash
ashen deploy submit \
  --bundle target/riscv64imac-unknown-none-elf/release/my_contract \
  --idl contracts/my_contract/my_contract.idl \
  --key $ASHEN_PRIVATE_KEY \
  --wait \
  --wait-timeout-s 120
```

### Deploy with Custom Parameters

[Section titled “Deploy with Custom Parameters”](#deploy-with-custom-parameters)

```bash
ashen deploy submit \
  --bundle target/riscv64imac-unknown-none-elf/release/my_contract \
  --idl contracts/my_contract/my_contract.idl \
  --key $ASHEN_PRIVATE_KEY \
  --max-fee 5000000 \
  --rpc-url http://custom-node:3030 \
  --wait
```

### Deploy Options

[Section titled “Deploy Options”](#deploy-options)

| Option             | Default                 | Description          |
| ------------------ | ----------------------- | -------------------- |
| `--bundle`         | —                       | Path to contract ELF |
| `--idl`            | —                       | Path to IDL file     |
| `--key`            | `$ASHEN_PRIVATE_KEY`    | Signing key          |
| `--max-fee`        | `10000000`              | Maximum fee to pay   |
| `--rpc-url`        | `http://127.0.0.1:3030` | RPC endpoint         |
| `--auth-token`     | —                       | Optional auth token  |
| `--wait`           | `false`                 | Wait for inclusion   |
| `--wait-timeout-s` | `60`                    | Timeout when waiting |

***

## Scripted Deployment (Automation)

[Section titled “Scripted Deployment (Automation)”](#scripted-deployment-automation)

For CI/CD pipelines and automation, use the CLI with `--json` for structured output.

### Basic Script

[Section titled “Basic Script”](#basic-script)

```bash
#!/bin/bash
set -e


CONTRACT_PATH="contracts/my_contract"


# Build
echo "Building contract..."
ashen dev build --manifest-path "$CONTRACT_PATH/Cargo.toml"


# Deploy
echo "Deploying..."
RESULT=$(ashen deploy submit \
  --bundle "target/riscv64imac-unknown-none-elf/release/my_contract" \
  --idl "$CONTRACT_PATH/my_contract.idl" \
  --key "$ASHEN_PRIVATE_KEY" \
  --wait 2>&1)


# Extract contract address from output
CONTRACT_ADDR=$(echo "$RESULT" | grep -oP 'Contract deployed at: \K0x[a-fA-F0-9]+')
echo "Contract deployed at: $CONTRACT_ADDR"


# Verify deployment
ashen abi "$CONTRACT_ADDR"
```

### Agent Workflow with JSON Output

[Section titled “Agent Workflow with JSON Output”](#agent-workflow-with-json-output)

```bash
#!/bin/bash
# Deployment workflow using robot mode for structured output


# 1. Deploy and capture result
echo "Deploying contract..."
DEPLOY_RESULT=$(ashen deploy submit \
  --bundle ./my_contract.elf \
  --idl ./my_contract.idl \
  --key "$ASHEN_PRIVATE_KEY" \
  --wait 2>&1)


# Parse deployment output for contract address
CONTRACT_ADDR=$(echo "$DEPLOY_RESULT" | grep -oP '0x[a-fA-F0-9]{64}' | head -1)


if [ -z "$CONTRACT_ADDR" ]; then
  echo "Deployment failed"
  exit 1
fi


echo "Deployed to: $CONTRACT_ADDR"


# 2. Verify the contract has code
ACCOUNT=$(ashen account --address "$CONTRACT_ADDR" --json)
if ! echo "$ACCOUNT" | jq -e '.ok' > /dev/null; then
  echo "Failed to query contract account"
  exit 1
fi


# 3. Test a view call
VIEW_RESULT=$(ashen view "$CONTRACT_ADDR" total_supply --json)


if echo "$VIEW_RESULT" | jq -e '.ok' > /dev/null; then
  SUPPLY=$(echo "$VIEW_RESULT" | jq -r '.data.result')
  echo "Initial total supply: $SUPPLY"
else
  echo "View call failed: $(echo "$VIEW_RESULT" | jq -r '.message')"
  exit 1
fi


# 4. Execute initialization (if needed)
INIT_RESULT=$(ashen call "$CONTRACT_ADDR" initialize '["MyToken", "MTK", 18]' \
  --key "$ASHEN_PRIVATE_KEY" \
  --wait --json)


if echo "$INIT_RESULT" | jq -e '.ok' > /dev/null; then
  TX_HASH=$(echo "$INIT_RESULT" | jq -r '.data.tx_hash')
  echo "Initialized: $TX_HASH"
else
  echo "Initialization failed: $(echo "$INIT_RESULT" | jq -r '.message')"
  exit 1
fi


echo "Deployment complete!"
echo "Contract: $CONTRACT_ADDR"
```

### Multi-Contract Deployment

[Section titled “Multi-Contract Deployment”](#multi-contract-deployment)

```bash
#!/bin/bash
# Deploy multiple contracts with dependencies


declare -A CONTRACTS
CONTRACTS=(
  ["token"]="contracts/token"
  ["pool"]="contracts/amm_pool"
  ["router"]="contracts/dex_router"
)


declare -A ADDRESSES


for name in token pool router; do
  path="${CONTRACTS[$name]}"
  echo "Deploying $name..."


  # Build
  ashen dev build --manifest-path "$path/Cargo.toml"


  # Deploy
  RESULT=$(ashen deploy submit \
    --bundle "target/riscv64imac-unknown-none-elf/release/$name" \
    --idl "$path/$name.idl" \
    --key "$ASHEN_PRIVATE_KEY" \
    --wait 2>&1)


  ADDR=$(echo "$RESULT" | grep -oP '0x[a-fA-F0-9]{64}' | head -1)
  ADDRESSES[$name]="$ADDR"
  echo "$name deployed at: $ADDR"
done


# Initialize router with token and pool addresses
ashen call "${ADDRESSES[router]}" set_addresses \
  "[\"${ADDRESSES[token]}\", \"${ADDRESSES[pool]}\"]" \
  --key "$ASHEN_PRIVATE_KEY" \
  --wait --json


echo "Deployment complete!"
for name in "${!ADDRESSES[@]}"; do
  echo "  $name: ${ADDRESSES[$name]}"
done
```

***

## Post-Deployment Verification

[Section titled “Post-Deployment Verification”](#post-deployment-verification)

### Verify Contract Code

[Section titled “Verify Contract Code”](#verify-contract-code)

```bash
# Check that contract has code
ashen account --address $CONTRACT_ADDR


# Fetch and inspect IDL
ashen abi $CONTRACT_ADDR
ashen abi $CONTRACT_ADDR --raw > deployed.idl


# Compare with source IDL
ashen idl diff ./my_contract.idl ./deployed.idl
```

### Test Contract Methods

[Section titled “Test Contract Methods”](#test-contract-methods)

```bash
# View call (read-only)
ashen view $CONTRACT_ADDR total_supply


# With JSON output for automation
ashen view $CONTRACT_ADDR total_supply --json
```

### Monitor Transactions

[Section titled “Monitor Transactions”](#monitor-transactions)

```bash
# Get deployment tx details
ashen tx by-hash --tx-hash $DEPLOY_TX_HASH


# List recent transactions to the contract
ashen tx by-hash --tx-hash $DEPLOY_TX_HASH --json
```

***

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Common Issues

[Section titled “Common Issues”](#common-issues)

**“insufficient balance”**

* Fund your account before deployment
* Check: `ashen account --address $YOUR_ADDRESS`

**“gas limit exceeded”**

* Increase `--gas-limit` (default: 1,000,000)
* Complex contracts may need 2-5 million gas

**“max fee exceeded”**

* Increase `--max-fee`
* Check current gas prices: `ashen status`

**“contract already exists”**

* Contract addresses are deterministic (sender + nonce)
* Use a different nonce lane or wait for previous tx

**“invalid IDL”**

* Validate: `ashen idl validate ./my_contract.idl`
* Check for syntax errors and type mismatches

### Debug Failed Deployments

[Section titled “Debug Failed Deployments”](#debug-failed-deployments)

```bash
# Trace the deployment transaction
ashen debug trace --tx-hash $FAILED_TX_HASH


# Check execution logs
ashen tx by-hash --tx-hash $FAILED_TX_HASH --wait
```

***

## Best Practices

[Section titled “Best Practices”](#best-practices)

1. **Always test locally first**

   ```bash
   just devnet-node init --alloc "$ADDR=1000000000000"
   just node
   # Deploy to local node before testnet/mainnet
   ```

2. **Use `--wait` for reliable scripting**

   * Without `--wait`, you only get the tx hash
   * With `--wait`, you confirm inclusion and get the contract address

3. **Version your IDLs**

   * Commit IDL files alongside contract source
   * Use `ashen idl diff` to track breaking changes

4. **Set appropriate gas limits**

   * Start with 1M gas, increase if deployment fails
   * Large contracts may need 5-10M gas

5. **Consider upgrade policy carefully**

   * `immutable`: Most secure, no upgrades possible
   * `owner`: Flexible, owner can upgrade
   * `governance`: Requires on-chain governance approval

***

## Related

[Section titled “Related”](#related)

* [Deterministic Builds](/guides/deterministic-builds/) — Canonical toolchain and container image
* [Ashen SDK](/contracts/ashen-sdk/) — Write contracts in Zig
* [IDL & ABI](/contracts/idl-and-abi/) — Interface definitions
* [Using the CLI](/guides/using-the-cli/) — Full CLI reference
* [Configuration](/reference/configuration/) — Node configuration

# Deterministic Builds

> Build contracts with the canonical toolchain so validators accept them

## Why Deterministic Builds Matter

[Section titled “Why Deterministic Builds Matter”](#why-deterministic-builds-matter)

Ashen validators re-execute every contract deployment and call to verify state transitions. When a validator receives a block containing a contract deployment, it compiles the submitted source or validates the submitted ELF against the canonical compiler output. If the binary doesn’t match what the pinned toolchain produces, the transaction is rejected.

This means **all contract authors must use the same compiler versions** as the validator set. A different Rust nightly, a different Zig release, or different LLVM optimization flags will produce a different ELF — and that ELF will be rejected at consensus.

The pinned versions are defined in `rust-toolchain.toml` and `devenv.nix` at the root of the repository:

| Tool | Pinned Version            | Pin Source                             | Notes                                      |
| ---- | ------------------------- | -------------------------------------- | ------------------------------------------ |
| Rust | nightly-2025-11-05        | `rust-toolchain.toml`                  | With `riscv64imac-unknown-none-elf` target |
| Zig  | 0.14.x                    | `devenv.nix` + `ashen dev build` check | Validated at build time                    |
| LLVM | From `llvm-tools-preview` | `rust-toolchain.toml`                  | For `llvm-readelf`, `llvm-objdump`         |

`ashen dev build` checks the installed Zig version before building Zig contracts and warns if it doesn’t match the expected version. Override with `ASHEN_EXPECTED_ZIG_VERSION=0.14` if needed.

## Contract Builder Image

[Section titled “Contract Builder Image”](#contract-builder-image)

The **contract builder** is a Docker image derived directly from `devenv.nix`. It contains the exact toolchain that validators use, so contracts built inside it are guaranteed to produce accepted ELFs.

### Build the Image

[Section titled “Build the Image”](#build-the-image)

```bash
# Build the OCI image and copy to your local Docker daemon
just contract-builder-build
```

This runs `devenv container build contract-builder` followed by `devenv container copy contract-builder`, which pushes the image to your local Docker as `ashen/contract-builder`.

### Smoke Test

[Section titled “Smoke Test”](#smoke-test)

Verify both toolchains (Rust and Zig) work inside the image:

```bash
just contract-builder-test
```

This builds `sft_v1` (Rust) and `zig_fixture` (Zig) inside the container and checks that the output ELFs are valid RISC-V binaries.

### Use the Image Directly

[Section titled “Use the Image Directly”](#use-the-image-directly)

Mount your project into the container and run build commands:

```bash
# Zig contract
docker run --rm -v $(pwd):/build -w /build ashen/contract-builder \
  bash -c 'cd contracts/my_contract && zig build -Doptimize=ReleaseSmall'


# Rust contract
docker run --rm -v $(pwd):/build -w /build ashen/contract-builder \
  bash -c '
    export ASHEN_CONTRACT_TARGET=riscv64imac-unknown-none-elf
    export ASHEN_CONTRACT_RUSTFLAGS="-C target-feature=+m,+c,+zba,+zbb,-a,-f,-d,-q,-v,-zicsr,-relax"
    cargo build -p my_contract --target "$ASHEN_CONTRACT_TARGET" --release
  '


# Or use just (included in the image)
docker run --rm -v $(pwd):/build -w /build ashen/contract-builder \
  just contract-build --manifest-path contracts/my_contract/Cargo.toml
```

### CI Integration

[Section titled “CI Integration”](#ci-integration)

Use the image in CI pipelines to ensure builds are reproducible:

```yaml
# GitHub Actions
jobs:
  build-contracts:
    runs-on: ubuntu-latest
    container:
      image: ashen/contract-builder
    steps:
      - uses: actions/checkout@v4
      - run: just contract-build-all
```

## Building for Devnet

[Section titled “Building for Devnet”](#building-for-devnet)

For local development, you can build contracts either inside the container or with your local devenv shell — both use the same pinned toolchain.

### With devenv (local)

[Section titled “With devenv (local)”](#with-devenv-local)

If you have [devenv](https://devenv.sh) installed:

```bash
# Enter the dev shell (pins all toolchain versions)
devenv shell


# Build a Zig contract
cd contracts/my_contract && zig build -Doptimize=ReleaseSmall


# Build a Rust contract
just contract-build --manifest-path contracts/my_contract/Cargo.toml


# Build all contracts
just contract-build-all
```

### With the Container Image

[Section titled “With the Container Image”](#with-the-container-image)

If you don’t have devenv/nix installed, use the container:

```bash
just contract-builder-build


docker run --rm -v $(pwd):/build -w /build ashen/contract-builder \
  just contract-build-all
```

### Deploy to Local Devnet

[Section titled “Deploy to Local Devnet”](#deploy-to-local-devnet)

After building, deploy to a running local node:

```bash
# Start a node (in another terminal)
just node


# Deploy
just contract-deploy \
  --elf target/riscv64imac-unknown-none-elf/release/my_contract \
  --wait
```

See [Local Devnet](/guides/devnet/) for full node setup.

## Building for Testnet

[Section titled “Building for Testnet”](#building-for-testnet)

Testnet validators run the same toolchain as devnet. The only difference is the deployment target (a remote RPC endpoint instead of localhost).

### 1. Build with the canonical toolchain

[Section titled “1. Build with the canonical toolchain”](#1-build-with-the-canonical-toolchain)

Use either devenv or the container image — same as devnet:

```bash
just contract-build --manifest-path contracts/my_contract/Cargo.toml
```

### 2. Deploy to testnet

[Section titled “2. Deploy to testnet”](#2-deploy-to-testnet)

```bash
export NODE_RPC_URL=http://testnet-rpc.example.com:3030
export ASHEN_PRIVATE_KEY=@./my.key.json


ashen deploy submit \
  --bundle target/riscv64imac-unknown-none-elf/release/my_contract \
  --idl contracts/my_contract/my_contract.idl \
  --key "$ASHEN_PRIVATE_KEY" \
  --wait
```

See [Deploying Contracts](/guides/deploying-contracts/) for the full deployment workflow.

## What’s Inside the Image

[Section titled “What’s Inside the Image”](#whats-inside-the-image)

The container includes everything from the devenv closure:

* **Rust** nightly (2025-11-05) with clippy, rustfmt, miri, and the `riscv64imac-unknown-none-elf` cross-compilation target
* **Zig** (nixpkgs version)
* **LLVM tools** (`llvm-readelf`, `llvm-objdump`, `llvm-nm`)
* **just** command runner
* **cargo**, **jq**, **curl**

The image does **not** include the repository source code. Mount your project at `/build` (or any path) when running the container.

## Verifying a Build

[Section titled “Verifying a Build”](#verifying-a-build)

To confirm your ELF was built with the correct toolchain:

```bash
# Check the ELF target
file target/riscv64imac-unknown-none-elf/release/my_contract
# Expected: ELF 64-bit LSB executable, UCB RISC-V, ...


# Inspect sections
llvm-readelf -S target/riscv64imac-unknown-none-elf/release/my_contract


# Validate against VM constraints
just vm-elf-validate target/riscv64imac-unknown-none-elf/release/my_contract
```

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**“ELF rejected by validator”**

* You built with a different compiler version. Rebuild inside the container or with `devenv shell`.
* Check `rustc --version` matches the pinned nightly in `devenv.nix`.

**“target not found” during Rust build**

* The `riscv64imac-unknown-none-elf` target is bundled with the devenv toolchain. If using `rustup` manually, run `rustup target add riscv64imac-unknown-none-elf`.

**Container build fails**

* Ensure `devenv` and `nix` are installed. The container build requires Nix to evaluate the devenv closure.
* Run `devenv container build contract-builder` with `--verbose` for details.

## Related

[Section titled “Related”](#related)

* [Zig Guide](/contracts/zig-guide/) — Writing contracts in Zig
* [Rust Guide](/contracts/rust-guide/) — Writing contracts in Rust
* [Deploying Contracts](/guides/deploying-contracts/) — Full deployment workflow
* [Local Devnet](/guides/devnet/) — Running a local development network
* [VM Tooling](/guides/vm-tooling/) — ELF validation and debugging tools

# Local Devnet

> Run a local development network for testing and iteration

## Overview

[Section titled “Overview”](#overview)

Ashen provides three ways to run a local development environment:

1. **Single node** — one validator with RPC, fastest iteration loop
2. **Multi-node testnet** — multiple validators with P2P, tests consensus
3. **Deterministic simulation** — in-memory consensus sim, no network needed

## Quick Start (Single Node)

[Section titled “Quick Start (Single Node)”](#quick-start-single-node)

```bash
# Generate a keypair
ashen keygen --json > dev.key.json


# Initialize with a pre-funded account
just node init --data-dir ./node-data \
  --alloc "493615aa1e16a24f618d3ab6dd93a9250ca76e19996e46493a372c5994862e8c=13370000000000"


# Start the node (RPC on port 3030)
just node run --data-dir ./node-data --block-time-ms 1000
```

Verify it’s running:

```bash
just status
```

## Key Generation

[Section titled “Key Generation”](#key-generation)

```bash
# Random key
ashen keygen --json


# Deterministic key (reproducible)
ashen keygen --json --seed 12345
```

Output (RobotOk envelope):

```json
{
  "ok": true,
  "data": {
    "seed": 12345,
    "secret_key": "0x...",
    "public_key": "0x...",
    "address": "0x493615aa..."
  }
}
```

Use `--seed` for reproducible test accounts across runs.

## Genesis Configuration

[Section titled “Genesis Configuration”](#genesis-configuration)

Genesis is created during `node init`. Pre-fund accounts with `--alloc`:

```bash
# Multiple accounts
just node init --data-dir ./node-data \
  --alloc "ADDR1=1000000" \
  --alloc "ADDR2=2000000"


# Auto-generate N seed accounts
just node init --data-dir ./node-data \
  --seed 42 --seed-count 10 --seed-balance 1000000000
```

The resulting `genesis.json`:

```json
{
  "allocations": [
    { "address": "493615aa...", "balance": 13370000000000 }
  ]
}
```

## Multi-Node Testnet

[Section titled “Multi-Node Testnet”](#multi-node-testnet)

Generate and run a local validator set:

```bash
# Generate configs for 3 validators
just testnet-local-generate N_VALIDATORS=3 TESTNET_DIR=./testnet-local


# Start all validators + archive node with RPC
just testnet-local-run N_VALIDATORS=3 TESTNET_DIR=./testnet-local
```

Or use `ashen setup` for more control:

```bash
ashen setup local \
  --validators 4 \
  --seed 12345 \
  --initial-balance 1000000000 \
  --output ./testnet
```

This creates: validator keys, BLS shares, `peers.yaml`, `genesis.json`, and a `start-validators.sh` script.

## Deterministic Simulation

[Section titled “Deterministic Simulation”](#deterministic-simulation)

The `node devnet` subcommand runs an in-memory consensus simulation — no network, fully deterministic:

```bash
# Default: 4 nodes, 200 steps
just devnet-small


# Chaos: 7 nodes, packet loss, latency
just devnet-chaos
```

### Custom Parameters

[Section titled “Custom Parameters”](#custom-parameters)

```bash
cargo run --bin node -- devnet \
  --nodes 4 \
  --steps 500 \
  --step-ms 10 \
  --link-latency-ms 5 \
  --link-jitter-ms 2 \
  --success-rate 1.0 \
  --state-backend cached-journal
```

| Parameter              | Env Var                     | Default        | Description                    |
| ---------------------- | --------------------------- | -------------- | ------------------------------ |
| `--nodes`              | `DEVNET_N`                  | 4              | Number of validators           |
| `--steps`              | `DEVNET_STEPS`              | 200            | Simulation steps               |
| `--step-ms`            | `DEVNET_STEP_MS`            | 10             | Milliseconds per step          |
| `--link-latency-ms`    | `DEVNET_LINK_LATENCY_MS`    | 5              | Baseline link latency          |
| `--link-jitter-ms`     | `DEVNET_LINK_JITTER_MS`     | 2              | Latency jitter                 |
| `--success-rate`       | `DEVNET_SUCCESS_RATE`       | 1.0            | Packet delivery rate (0.0-1.0) |
| `--state-backend`      | `DEVNET_STATE_BACKEND`      | cached-journal | State backend                  |
| `--report-every-steps` | `DEVNET_REPORT_EVERY_STEPS` | 50             | Report interval                |

### Chaos Testing

[Section titled “Chaos Testing”](#chaos-testing)

Simulate degraded network conditions:

```bash
DEVNET_SUCCESS_RATE=0.9 \
DEVNET_LINK_LATENCY_MS=25 \
DEVNET_LINK_JITTER_MS=10 \
cargo run --bin node -- devnet --nodes 7 --steps 500
```

This tests consensus resilience under 10% packet loss and variable latency.

## Interacting with a Running Node

[Section titled “Interacting with a Running Node”](#interacting-with-a-running-node)

### RPC Commands

[Section titled “RPC Commands”](#rpc-commands)

```bash
just status                              # Chain status
just rpc-manifest                        # Method IDL (JSON)
just rpc-idl                             # Raw IDL text
just account ADDR                        # Account balance/nonce
just tx HASH                             # Look up transaction
just rpc-call METHOD PARAMS              # Arbitrary RPC call
```

### Direct curl

[Section titled “Direct curl”](#direct-curl)

```bash
curl -s http://127.0.0.1:3030/v2/rpc \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"status","params":{}}' | jq .result
```

### Smoke Tests

[Section titled “Smoke Tests”](#smoke-tests)

```bash
just agent-smoke   # Quick consensus + application tests
just agent-report  # Bundle metrics, health, and logs
```

## Node Modes

[Section titled “Node Modes”](#node-modes)

| Mode      | Command         | Description                          |
| --------- | --------------- | ------------------------------------ |
| Validator | `node run`      | Full consensus + RPC                 |
| RPC-only  | `node rpc`      | Serves RPC from shared data-dir      |
| Follower  | `node follower` | P2P sync, no consensus participation |

### Useful Flags

[Section titled “Useful Flags”](#useful-flags)

| Flag                    | Default | Description                       |
| ----------------------- | ------- | --------------------------------- |
| `--block-time-ms`       | 1000    | Block production interval         |
| `--archive-mode`        | off     | Retain all historical state       |
| `--prune-keep-epochs`   | 10      | Epochs to keep when pruning       |
| `--checkpoint-interval` | —       | Emit snapshots every N blocks     |
| `--produce-empty`       | true    | Produce blocks with empty mempool |

## Developer Tools (`ashen dev`)

[Section titled “Developer Tools (ashen dev)”](#developer-tools-ashen-dev)

Subcommands for common dev workflows:

```bash
ashen dev build [args]                   # Build contracts
ashen dev test [args]                    # Run vm-runtime tests (default)
ashen dev simulate --tx "0x..." --pretty # Simulate transaction via RPC
```

## Environment Variables

[Section titled “Environment Variables”](#environment-variables)

```bash
# RPC connection
NODE_RPC_URL=http://127.0.0.1:3030
NODE_AUTH_TOKEN=optional_bearer_token


# Node configuration
NODE_DATA_DIR=./node-data
NODE_LISTEN=127.0.0.1:3030
NODE_BLOCK_TIME_MS=1000


# Trace output (debugging)
ASHEN_TRACE_OUTPUT=1
ASHEN_TRACE_OUTPUT_DIR=target/feedback
```

## Related

[Section titled “Related”](#related)

* [Deterministic Builds](/guides/deterministic-builds/) — canonical toolchain and contract builder image
* [Running a Node](/guides/running-a-node/) — production node setup
* [Transaction Simulation](/guides/tx-simulation/) — simulating transactions
* [Contract Testing](/guides/contract-testing/) — testing without a node
* [Debugging](/guides/debugging/) — trace output and debugging tools
* [Troubleshooting](/guides/troubleshooting/) — common issues

# Oracle Integrations

> Integrate Pyth, RedStone, and Chainlink OCR2 with Ashen

## Overview

[Section titled “Overview”](#overview)

Ashen ships reference oracle contracts in `contracts/` that verify external attestations on-chain. These are **Zig contracts** intended as production-grade starting points:

* **Pyth**: ed25519 publisher attestations
* **RedStone**: secp256k1 data package attestations
* **Chainlink OCR2**: multi-signature report verification

Each contract manages its own signer set, threshold, and replay protection.

## Build + Deploy (Shared)

[Section titled “Build + Deploy (Shared)”](#build--deploy-shared)

```bash
# Build (Zig)
cd contracts/<oracle_contract>
zig build -Doptimize=ReleaseSmall


# Deploy
ashen deploy submit \
  --bundle contracts/<oracle_contract>/zig-out/bin/<oracle_contract> \
  --idl contracts/<oracle_contract>/<oracle_contract>.idl \
  --key $ASHEN_PRIVATE_KEY \
  --wait
```

## Pyth (ed25519 attestations)

[Section titled “Pyth (ed25519 attestations)”](#pyth-ed25519-attestations)

**Contract**: `contracts/pyth_oracle_v1`

Capabilities:

* Publisher set management with threshold
* Attestation parsing and median aggregation
* Timestamp validity window (5 minutes)
* Replay protection

Attestation format (per contract comments):

* `magic(4) = "PYTH"` + `version(1)` + `num_attestations(1)`
* Each attestation: publisher pubkey (32) + signature (64) + feed\_id (32) + price (i64 BE) + confidence (u64 BE) + exponent (i32 BE) + publish\_time (i64 BE)

**Flow**:

1. Initialize owner + threshold
2. Update publisher set
3. Submit attestations for verification

## RedStone (secp256k1 data packages)

[Section titled “RedStone (secp256k1 data packages)”](#redstone-secp256k1-data-packages)

**Contract**: `contracts/redstone_oracle_v1`

Capabilities:

* Signer set management with threshold
* RedStone data package parsing
* secp256k1 signature verification (EIP-191)
* Median aggregation
* Timestamp validity window (15 minutes)
* Replay protection

**Flow**:

1. Initialize owner + threshold
2. Update signer set (sorted addresses)
3. Submit RedStone packages for verification

## Chainlink OCR2

[Section titled “Chainlink OCR2”](#chainlink-ocr2)

**Contract**: `contracts/chainlink_ocr2_v1`

Capabilities:

* OCR2 report verification
* Config management (signer set, f)
* Replay protection
* Supports up to 31 signers

**Flow**:

1. Initialize owner
2. Set signer configuration (`f`, signer set)
3. Verify OCR2 reports

## Operational Tips

[Section titled “Operational Tips”](#operational-tips)

* **Keep signer sets up to date**: stale keys will fail verification.
* **Validate timestamps**: on-chain windows are strict.
* **Use replay protection**: each contract enforces it; don’t reuse packets.
* **Simulate first**: use `tx_simulate` before submission.

## Related

[Section titled “Related”](#related)

* `/contracts/examples/` for oracle contract references
* `/guides/tx-simulation/` for simulation workflow
* `/reference/precompiles/` for crypto syscall details

# Running a Node

> Complete guide to operating Ashen nodes

This guide covers running Ashen nodes in various configurations: development, production validators, followers, and RPC gateways.

## Node Types Overview

[Section titled “Node Types Overview”](#node-types-overview)

| Mode            | Command                | Use Case                           |
| --------------- | ---------------------- | ---------------------------------- |
| **Single-node** | `node run`             | Local development, testing         |
| **Validator**   | `node run --validator` | Production consensus participation |
| **Follower**    | `node follower`        | Archive/RPC nodes via P2P sync     |
| **RPC Gateway** | `node rpc`             | Offload RPC from validators        |

***

## Quick Start (Development)

[Section titled “Quick Start (Development)”](#quick-start-development)

The fastest way to run a local development node:

```bash
# 1. Generate a keypair
ashen keygen --json > ./target/dev.key.json
export ASHEN_PRIVATE_KEY=@./target/dev.key.json
ADDR=$(jq -r .data.address ./target/dev.key.json)


# 2. Initialize with funded account
just devnet-node init --data-dir ./node-data --alloc "$ADDR=1000000000000"


# 3. Run the node
just devnet-node run --data-dir ./node-data


# In another terminal, verify it's working:
just status
just account $ADDR
```

Or use the all-in-one `just node` recipe:

```bash
just node DATA_DIR=./node-data
```

***

## Single-Node Mode

[Section titled “Single-Node Mode”](#single-node-mode)

Single-node mode runs a complete chain with one validator. This is ideal for:

* Local development and testing
* Contract development and debugging
* Integration testing

### Basic Usage

[Section titled “Basic Usage”](#basic-usage)

```bash
# Initialize data directory
node init \
  --data-dir ./node-data \
  --alloc "0xYOUR_ADDRESS=1000000000000"


# Run the node
node run \
  --data-dir ./node-data \
  --listen 127.0.0.1:3030 \
  --block-time-ms 1000
```

### Configuration Options

[Section titled “Configuration Options”](#configuration-options)

| Option                   | Default          | Description                               |
| ------------------------ | ---------------- | ----------------------------------------- |
| `--data-dir`             | `./node-data`    | Directory for chain data                  |
| `--listen`               | `127.0.0.1:3030` | RPC server address                        |
| `--block-time-ms`        | `1000`           | Target block time                         |
| `--produce-empty-blocks` | `true`           | Produce blocks even when mempool is empty |
| `--no-rate-limit`        | `false`          | Disable RPC rate limiting (dev only)      |

### Genesis Allocation

[Section titled “Genesis Allocation”](#genesis-allocation)

Pre-fund accounts at genesis using `--alloc`:

```bash
# Single allocation
node init --data-dir ./node-data --alloc "0xADDR=1000000000000"


# Multiple allocations
node init --data-dir ./node-data \
  --alloc "0xADDR1=1000000000000" \
  --alloc "0xADDR2=500000000000"


# Seeded accounts (deterministic for testing)
node init --data-dir ./node-data \
  --seed 42 \
  --seed-count 10 \
  --seed-balance 1000000000
```

### Fast Development Mode

[Section titled “Fast Development Mode”](#fast-development-mode)

For rapid iteration, reduce block time and disable rate limiting:

```bash
node run \
  --data-dir ./node-data \
  --block-time-ms 500 \
  --no-rate-limit \
  --produce-empty-blocks
```

***

## Validator Mode

[Section titled “Validator Mode”](#validator-mode)

Validator mode participates in consensus with other validators. This is required for production networks.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* **Ed25519 network key** for P2P identity
* **Peers configuration** with all validator addresses
* **BLS keys** for threshold signatures (from DKG or testnet seed)

### Deterministic Toolchain (Required)

[Section titled “Deterministic Toolchain (Required)”](#deterministic-toolchain-required)

Ashen validators **validate the ELF output produced by the canonical compilers**. If you build with a different Rust/LLVM/Zig toolchain, the ELF will not validate and your artifacts will be rejected. This is intentional: it protects developers from shipping binaries that the network cannot accept.

**Do not go rogue on toolchains.** Use the exact toolchain pinned by `devenv` (or the Docker image built from `devenv`) for all contract builds and node runs in live environments. Validators run the node inside that same Docker image in production.

### Setup

[Section titled “Setup”](#setup)

#### 1. Create Network Key

[Section titled “1. Create Network Key”](#1-create-network-key)

```bash
# Initialize keystore
ashen keystore init


# Generate network key
ashen keystore add --label my-validator


# Export address for peers.yaml
ashen keystore export --label my-validator
```

#### 2. Configure Peers

[Section titled “2. Configure Peers”](#2-configure-peers)

Create `peers.yaml` with all validator public keys and addresses:

```yaml
addresses:
  "0x1234...abcd": "192.168.1.10:4040"
  "0x5678...efgh": "192.168.1.11:4040"
  "0x9abc...ijkl": "192.168.1.12:4040"
```

#### 3. Run Validator

[Section titled “3. Run Validator”](#3-run-validator)

**Testnet mode** (deterministic BLS keys):

```bash
node run \
  --data-dir /var/lib/ashen \
  --validator \
  --validator-network-key "keystore:my-validator" \
  --peers ./peers.yaml \
  --p2p-port 4040 \
  --bls-seed 42 \
  --validator-index 0 \
  --bootstrapper "0x1234...abcd"
```

**Production mode** (DKG-generated BLS keys):

```bash
node run \
  --data-dir /var/lib/ashen \
  --validator \
  --validator-network-key "keystore:my-validator" \
  --peers ./peers.yaml \
  --p2p-port 4040 \
  --bls-share "$BLS_SHARE" \
  --bls-polynomial "$BLS_POLY" \
  --bootstrapper "0x1234...abcd"
```

### Validator Options

[Section titled “Validator Options”](#validator-options)

| Option                    | Description                                                 |
| ------------------------- | ----------------------------------------------------------- |
| `--validator`             | Enable validator mode                                       |
| `--validator-network-key` | Ed25519 key reference (`keystore:<label>`)                  |
| `--peers`                 | Path to peers.yaml                                          |
| `--p2p-port`              | P2P listen port (separate from RPC)                         |
| `--bootstrapper`          | Bootstrapper public key (repeatable)                        |
| `--bls-share`             | BLS threshold share (hex)                                   |
| `--bls-polynomial`        | BLS commitment polynomial (hex)                             |
| `--bls-seed`              | Deterministic BLS seed (testnet)                            |
| `--validator-index`       | Your index in validator set (testnet)                       |
| `--enable-rpc`            | Enable full RPC (validators default to health/metrics only) |
| `--skip-preflight`        | Skip startup checks (not recommended)                       |

### Preflight Checks

[Section titled “Preflight Checks”](#preflight-checks)

Validators run preflight checks at startup:

1. **BLS Key** — Validates share and polynomial format
2. **Disk Space** — Requires at least 1GB free
3. **Clock Sync** — Warns if system time appears off
4. **Data Directory** — Verifies write access

To skip (development only):

```bash
node run --validator --skip-preflight ...
```

***

## Follower Mode

[Section titled “Follower Mode”](#follower-mode)

Follower nodes sync via P2P without participating in consensus. Use for:

* Archive nodes in different datacenters
* RPC nodes that don’t share storage with validators
* Read-only indexing nodes

### Setup

[Section titled “Setup”](#setup-1)

```bash
node follower \
  --data-dir ./follower-data \
  --peers peers.yaml \
  --bootstrapper "0x1234...abcd" \
  --listen 127.0.0.1:3030 \
  --p2p-port 4040
```

### Follower Options

[Section titled “Follower Options”](#follower-options)

| Option              | Default | Description                      |
| ------------------- | ------- | -------------------------------- |
| `--sync-batch-size` | `32`    | Headers per sync request         |
| `--sync-poll-ms`    | `1000`  | Poll interval when caught up     |
| `--tx-forward-url`  | —       | Forward transactions to this URL |
| `--network-key`     | —       | Optional: specify P2P identity   |

### Transaction Forwarding

[Section titled “Transaction Forwarding”](#transaction-forwarding)

Followers can forward transactions to a leader node:

```bash
node follower \
  --tx-forward-url http://leader:3030 \
  ...
```

***

## RPC Gateway Mode

[Section titled “RPC Gateway Mode”](#rpc-gateway-mode)

RPC gateway mode runs a read-only RPC server that shares the data directory with a running node. Use to offload RPC traffic from validators.

### Setup

[Section titled “Setup”](#setup-2)

```bash
# On the same machine as the validator
node rpc \
  --data-dir /var/lib/ashen \
  --listen 0.0.0.0:3030 \
  --refresh-interval-s 1
```

### RPC Options

[Section titled “RPC Options”](#rpc-options)

| Option                 | Default | Description                   |
| ---------------------- | ------- | ----------------------------- |
| `--refresh-interval-s` | `1`     | How often to reload from disk |
| `--rate-limit-per-s`   | `1000`  | Requests per second           |
| `--rate-limit-burst`   | `2000`  | Burst allowance               |
| `--auth-token`         | —       | Optional authentication token |

### Architecture

[Section titled “Architecture”](#architecture)

```plaintext
                    ┌─────────────────┐
     Internet  ────►│  RPC Gateway    │──┐
                    │  (node rpc)     │  │
                    └─────────────────┘  │  shared
                                         ├─ data-dir
                    ┌─────────────────┐  │
     Validators ◄──►│  Validator      │──┘
                    │  (node run)     │
                    └─────────────────┘
```

***

## State Management

[Section titled “State Management”](#state-management)

### Archive Mode

[Section titled “Archive Mode”](#archive-mode)

Preserve all historical state (no pruning):

```bash
node run --archive-mode --data-dir ./archive-data ...
```

Archive mode is required for:

* Historical queries at any block height
* State sync for new nodes
* Debugging and forensics

### Pruning

[Section titled “Pruning”](#pruning)

Non-archive nodes prune old state to save disk space:

```bash
# Keep 10 epochs of state (default)
node run --prune-keep-epochs 10 ...


# Keep more history
node run --prune-keep-epochs 100 ...
```

### Checkpoints

[Section titled “Checkpoints”](#checkpoints)

Checkpoints enable fast sync by providing state snapshots:

```bash
# Checkpoint every 1000 blocks
node run --checkpoint-interval 1000 ...


# Default: checkpoint at epoch boundaries
node run ...
```

***

## Monitoring

[Section titled “Monitoring”](#monitoring)

### Health Endpoint

[Section titled “Health Endpoint”](#health-endpoint)

```bash
curl http://localhost:3030/health
# Returns: {"status":"healthy"}
```

### Metrics Endpoint

[Section titled “Metrics Endpoint”](#metrics-endpoint)

```bash
curl http://localhost:3030/metrics
# Returns: Prometheus-format metrics
```

### Key Metrics

[Section titled “Key Metrics”](#key-metrics)

| Metric                     | Description               |
| -------------------------- | ------------------------- |
| `ashen_tip_height`         | Current chain tip height  |
| `ashen_finalized_height`   | Last finalized height     |
| `ashen_mempool_size`       | Pending transaction count |
| `ashen_block_time_seconds` | Recent block times        |
| `ashen_rpc_requests_total` | RPC request counter       |

### Agent Report

[Section titled “Agent Report”](#agent-report)

Generate a diagnostic bundle:

```bash
just agent-report LISTEN=127.0.0.1:3030 OUT_DIR=./diagnostics
```

This collects:

* Health status
* Metrics snapshot
* Recent log lines
* Chain status

***

## Debugging

[Section titled “Debugging”](#debugging)

### Execution Tracing

[Section titled “Execution Tracing”](#execution-tracing)

Enable detailed execution traces:

```bash
# Trace to stdout
ASHEN_TRACE_OUTPUT=1 node run --data-dir ./node-data


# Trace to files
ASHEN_TRACE_OUTPUT_DIR=./traces node run --data-dir ./node-data
```

### Compare Traces

[Section titled “Compare Traces”](#compare-traces)

```bash
just trace-diff trace_a.json trace_b.json
```

### Debug a Transaction

[Section titled “Debug a Transaction”](#debug-a-transaction)

```bash
# Trace transaction execution
ashen debug trace --tx-hash 0x...


# Replay with breakpoints
ashen debug replay --tx-hash 0x... --breakpoint pc:0x1000
```

***

## Logging

[Section titled “Logging”](#logging)

### File Logging

[Section titled “File Logging”](#file-logging)

```bash
node run \
  --log-file /var/log/ashen/ \
  --log-rotation daily \
  --log-max-files 30 \
  --log-prefix node \
  ...
```

### Log Files

[Section titled “Log Files”](#log-files)

With rotation enabled, logs are named:

* `node.2026-01-22.log`
* `node.2026-01-21.log`
* etc.

### Environment Variables

[Section titled “Environment Variables”](#environment-variables)

| Variable             | Description                   |
| -------------------- | ----------------------------- |
| `NODE_LOG_FILE`      | Log file path                 |
| `NODE_LOG_ROTATION`  | `daily`, `hourly`, or `never` |
| `NODE_LOG_MAX_FILES` | Max rotated files to keep     |
| `NODE_LOG_PREFIX`    | Log filename prefix           |
| `RUST_LOG`           | Log level filter              |

***

## Security

[Section titled “Security”](#security)

### Rate Limiting

[Section titled “Rate Limiting”](#rate-limiting)

Default rate limits protect against DoS:

```bash
# Customize limits
node run \
  --rate-limit-per-s 5000 \
  --rate-limit-burst 10000 \
  ...


# Separate limits for utility endpoints
node run \
  --utility-rate-limit-per-s 100 \
  --utility-rate-limit-burst 200 \
  ...
```

### Authentication

[Section titled “Authentication”](#authentication)

Protect RPC with bearer tokens:

```bash
# Server side
node run --auth-token "secret-token-here" ...


# Client side
export NODE_AUTH_TOKEN="secret-token-here"
ashen status
```

### Network Binding

[Section titled “Network Binding”](#network-binding)

For production, bind RPC to localhost and use a reverse proxy:

```bash
# Node binds to localhost
node run --listen 127.0.0.1:3030 ...


# Nginx or Caddy handles TLS and public exposure
```

***

## Operations Runbook

[Section titled “Operations Runbook”](#operations-runbook)

### Starting a Node

[Section titled “Starting a Node”](#starting-a-node)

```bash
# Check prerequisites
node run --validator --skip-preflight=false --data-dir ./check-only 2>&1 | head -20


# Start with systemd
sudo systemctl start ashen-node


# Or directly
node run --data-dir /var/lib/ashen --validator ...
```

### Stopping a Node

[Section titled “Stopping a Node”](#stopping-a-node)

Nodes handle SIGTERM gracefully:

```bash
# Graceful shutdown
kill -TERM $(pgrep -f "node run")


# Or with systemd
sudo systemctl stop ashen-node
```

### Resetting State

[Section titled “Resetting State”](#resetting-state)

```bash
# Remove all state (DESTRUCTIVE)
node reset --data-dir ./node-data


# Or manually
rm -rf ./node-data/{chain,state,logs}
```

### Backup and Restore

[Section titled “Backup and Restore”](#backup-and-restore)

```bash
# Export snapshot
ashen backup export --data-dir ./node-data --output ./snapshot.tar


# Import snapshot
ashen backup import --data-dir ./new-node --input ./snapshot.tar
```

***

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Node Won’t Start

[Section titled “Node Won’t Start”](#node-wont-start)

**“BLS key not found”**

* Ensure `--bls-share` and `--bls-polynomial` are both provided
* Or use `--bls-seed` + `--validator-index` for testnet

**“peer not found in config”**

* Your public key must be in `peers.yaml`
* Check with `ashen keystore export --label my-validator`

**“disk space check failed”**

* Ensure at least 1GB free in data directory
* Use `--skip-preflight` temporarily (not recommended)

### Consensus Stalled

[Section titled “Consensus Stalled”](#consensus-stalled)

1. Check peer connectivity:

   ```bash
   curl http://localhost:3030/health
   ```

2. Check logs for timeout messages:

   ```bash
   grep -i "timeout\|stall" /var/log/ashen/*.log
   ```

3. Verify clock sync:

   ```bash
   timedatectl status
   ```

### High Memory Usage

[Section titled “High Memory Usage”](#high-memory-usage)

* Reduce `--p2p-mailbox-size` and `--p2p-message-backlog`
* Enable pruning (disable `--archive-mode`)
* Reduce `--prune-keep-epochs`

### RPC Errors

[Section titled “RPC Errors”](#rpc-errors)

**“rate limited”**

* Increase `--rate-limit-per-s` and `--rate-limit-burst`
* Or use `--no-rate-limit` for development

**“body too large”**

* Increase `--max-body-bytes`

***

## Related

[Section titled “Related”](#related)

* [Installation](/getting-started/installation/) — Build from source
* [Configuration](/reference/configuration/) — Full configuration reference
* [Using the CLI](/guides/using-the-cli/) — CLI command reference
* [Deploying Contracts](/guides/deploying-contracts/) — Contract deployment guide

# Session Keys

> Scoped delegation for temporary signing and automation

## Overview

[Section titled “Overview”](#overview)

Session keys let a parent account delegate limited signing authority to a secondary ed25519 key. They are designed for automation and low-risk flows where the parent key should stay offline.

A transaction is treated as a session key transaction when:

* `payer != authorizer`

In that case, the execution engine looks up a session key descriptor under the payer (parent) and enforces its constraints.

## What Session Keys Can Restrict

[Section titled “What Session Keys Can Restrict”](#what-session-keys-can-restrict)

Session constraints are enforced on every transaction:

* **Per-tx value limit** (`max_value_per_tx`)
* **Total budget** (`total_budget`, cumulative across the session)
* **Allowed contracts** (allowlist by address)
* **Allowed selectors** (allowlist by 4-byte function selector)
* **Expiry** (`expires_at` block height)
* **Revocation** (explicitly revoked by the parent)

A session becomes inactive if it is revoked, expired, or has exhausted its budget.

## Nonce Lanes

[Section titled “Nonce Lanes”](#nonce-lanes)

Session keys are assigned a dedicated `nonce_lane` on creation. Transactions signed by the session key should use:

* `nonce_space.lane = <assigned nonce_lane>`
* `nonce_space.tag = ""` (v1 ignores tags)

This isolates session key nonces from the parent account’s main lane.

## Session Key Lifecycle

[Section titled “Session Key Lifecycle”](#session-key-lifecycle)

### 1) Create

[Section titled “1) Create”](#1-create)

Session keys are stored under the parent account. Creation returns a `session_key_id` and the `nonce_lane` to use for session transactions.

The current v1 lookup derives the session key ID from the public key (`blake3(pubkey)`), so the returned ID is stable for a given session key.

### 2) Use

[Section titled “2) Use”](#2-use)

A session transaction should:

* Use the **session key** as `authorizer` (ed25519 pubkey address)
* Use the **parent** as `payer`
* Use the session’s `nonce_lane`

During execution the engine:

1. Verifies the signature against the session key
2. Looks up the session descriptor under the parent
3. Enforces constraints (value limits, allowlists, expiry, budget)
4. Updates `spent_so_far` on success

### 3) Revoke

[Section titled “3) Revoke”](#3-revoke)

Revocation flips a `revoked` flag on the descriptor. Revoked or expired sessions remain in the index for audit, but are not active.

## Management RPC Shapes

[Section titled “Management RPC Shapes”](#management-rpc-shapes)

Session key management is implemented by the `session_key_*` service in `src/rpc/session_keys.rs`. Check your node build for endpoint exposure.

### Create

[Section titled “Create”](#create)

```json
{
  "parent": "0x...",
  "session_pubkey": "0x...",
  "constraints": {
    "max_value_per_tx": "1000000",
    "total_budget": "10000000",
    "allowed_contracts": ["0x..."],
    "allowed_selectors": ["0x12345678"]
  },
  "expires_at": 123456,
  "created_at": 123400
}
```

### Revoke

[Section titled “Revoke”](#revoke)

```json
{
  "parent": "0x...",
  "session_pubkey": "0x..."
}
```

### Get / List

[Section titled “Get / List”](#get--list)

* `session_key_get` returns the descriptor plus an `is_active` flag.
* `session_key_list` returns descriptors for all keys under a parent, including revoked or expired sessions.

## Error Cases

[Section titled “Error Cases”](#error-cases)

Common rejection reasons include:

* `SESSION_KEY_NOT_FOUND`
* `SESSION_CONTRACT_NOT_ALLOWED`
* `SESSION_SELECTOR_NOT_ALLOWED`
* `SESSION_VALUE_EXCEEDED`
* `SESSION_BUDGET_EXHAUSTED`

See `/reference/error-domains/` for codes.

## Security Notes

[Section titled “Security Notes”](#security-notes)

* Use short expiries and tight allowlists for automation keys.
* Use a low `max_value_per_tx` and a bounded `total_budget`.
* Treat session keys as hot keys; rotate and revoke often.

## Related

[Section titled “Related”](#related)

* `/reference/error-domains/` for session key reject reasons
* `src/core/session_keys.rs` for the data model
* `src/core/execution/session.rs` for enforcement logic

# Transaction Bundles

> Atomic, ordered bundles of transactions

## Overview

[Section titled “Overview”](#overview)

A **transaction bundle** is an ordered list of signed transactions that execute **atomically**:

1. Transactions execute sequentially in bundle order.
2. If any transaction fails, the **entire bundle is reverted**.
3. State changes are committed only after all txs succeed.
4. Gas is charged for all executed transactions up to the failure.

Bundles are useful for multi‑step workflows, on‑chain arbitrage, and ensuring interdependent actions either all succeed or none do.

## Bundle Structure (Conceptual)

[Section titled “Bundle Structure (Conceptual)”](#bundle-structure-conceptual)

A bundle includes:

* `txs`: ordered list of signed transactions
* `tip`: optional incentive for block builder prioritization
* `bundle_nonce`: prevents bundle replay
* `authorizer`: address that authorizes the bundle
* `signature`: authorizer signature over the bundle hash

**Max size**: 32 transactions per bundle.

## When to Use Bundles

[Section titled “When to Use Bundles”](#when-to-use-bundles)

* **Atomic multi‑step actions** (e.g., approve → swap → transfer)
* **Arbitrage** across multiple pools
* **Conditional sequences** where partial success is unacceptable

## Simulation First

[Section titled “Simulation First”](#simulation-first)

Always simulate before submission:

* Use `chain_simulateBundle` to check ordering, dependencies, and gas
* A failing transaction will revert the whole bundle
* Simulations are only valid for the current chain head

See `/guides/tx-simulation/` for general simulation guidance.

## RPC Workflow

[Section titled “RPC Workflow”](#rpc-workflow)

Bundle submission is currently exposed via RPC:

* `tx_submit_bundle` — submit an atomic bundle
* `chain_simulateBundle` — simulate a bundle with dependency analysis

Refer to `/reference/rpc-api/` for request/response types.

## Notes and Tips

[Section titled “Notes and Tips”](#notes-and-tips)

* **Ordering matters**: hash and execution depend on tx order.
* **Tip responsibly**: tips can improve inclusion priority.
* **Signer consistency**: bundle authorization is separate from per‑tx signatures.
* **Validate locally**: ensure each tx is well‑formed and signed before bundling.

## Related

[Section titled “Related”](#related)

* `/reference/rpc-api/` — bundle RPC endpoints
* `/guides/tx-simulation/` — simulation guide
* `/concepts/private-mempool/` — sealed transaction behavior

# Troubleshooting

> Common issues and solutions

This guide lists common failures and quick fixes. Format: **Error message** -> **Solution**.

## Build Failures

[Section titled “Build Failures”](#build-failures)

* **“zig: command not found”** -> Install Zig and re-run `zig build` for contracts.

* **“error: target ‘riscv64imac-unknown-none-elf’ not found”** -> `rustup target add riscv64imac-unknown-none-elf` or use `devenv shell`.

* **“error: could not compile” after toolchain drift** -> Use the pinned toolchain in `devenv.nix` (`devenv shell`).

* **“linker `cc` not found”** -> Install a system C toolchain (or enter `devenv shell`).

## Test Failures

[Section titled “Test Failures”](#test-failures)

* **“proptest: Failed” with a seed** -> Re-run with `PROPTEST_SEED=<seed> PROPTEST_CASES=1 cargo test -p <crate> <test>`.

* **Non-deterministic failures** -> Re-run with `RUST_TEST_THREADS=1` and `-- --nocapture` for logs.

* **`devnet_replay` golden mismatch** -> Re-run with `REGENERATE_GOLDENS=1 cargo test --test devnet_replay`.

## Node Startup Issues

[Section titled “Node Startup Issues”](#node-startup-issues)

* **“address already in use”** -> Stop the other process or change ports (e.g., `--listen`, `--p2p-port`).

* **“genesis not found at … (run `devnet-node init --data-dir ...` first)”** -> Run `just devnet-node init --data-dir <dir>`.

* **“peers.yaml not found. Run ‘just testnet-local-generate’ first.”** -> Run `just testnet-local-generate`.

* **“keystore not found … run ‘ashen keystore init’ first”** -> Run `just ashen keystore init`.

## Contract Deployment Errors

[Section titled “Contract Deployment Errors”](#contract-deployment-errors)

* **“ASHEN\_PRIVATE\_KEY is required”** -> Set `ASHEN_PRIVATE_KEY=@/path/to/key.json` or export a hex key.

* **“ELF validation failed”** -> Build with the contract target (`just contract-build`) and re-run `just vm-elf-validate`.

* **“RPC 401 Unauthorized”** -> Set `NODE_AUTH_TOKEN` for the node you are calling.

* **“contract not found” / “account not found”** -> Confirm the deployment address and that the node is running.

# Transaction Simulation

> Safely simulate transactions before submission

## Overview

[Section titled “Overview”](#overview)

Transaction simulation runs your call against the current chain state without submitting it. Use it to estimate gas, validate arguments, and preview failures before you sign and send a real transaction.

Simulation is especially important for **sealed (private mempool)** flows: you should simulate locally before sealing because validators can’t inspect sealed payloads.

## CLI: Quick Simulation

[Section titled “CLI: Quick Simulation”](#cli-quick-simulation)

### Simple call

[Section titled “Simple call”](#simple-call)

```bash
# Simulate only (default)
ashen call 0xCONTRACT transfer '["0xTO", 100]' --key $ASHEN_PRIVATE_KEY
```

### Detailed call (explicit contract + IDL)

[Section titled “Detailed call (explicit contract + IDL)”](#detailed-call-explicit-contract--idl)

```bash
ashen contract call \
  --contract 0x1234... \
  --method transfer \
  --args '["0xTO", 100]' \
  --idl ./token.idl \
  --key $ASHEN_PRIVATE_KEY
```

### Submit only after a successful simulation

[Section titled “Submit only after a successful simulation”](#submit-only-after-a-successful-simulation)

```bash
ashen contract call ... --wait
```

### Force submit even if simulation fails

[Section titled “Force submit even if simulation fails”](#force-submit-even-if-simulation-fails)

```bash
ashen contract call ... --force --wait
```

## RPC: Simulation Endpoints

[Section titled “RPC: Simulation Endpoints”](#rpc-simulation-endpoints)

For programmatic use, the RPC provides dedicated simulation methods:

* `tx_simulate` — simulate execution and estimate gas
* `tx_simulate_access` — simulation + storage access list
* `tx_simulate_trace` — simulation with execution trace
* `tx_simulate_pipeline` — multi‑step pipeline (txs + view calls)
* `tx_build_simulate` — build + simulate in one call

See `/reference/rpc-api/` for full request/response types.

## Access Lists

[Section titled “Access Lists”](#access-lists)

Access lists are hints for the VM to prefetch state and reduce cold storage penalties. To generate a list automatically, use `tx_simulate_access` and attach it to subsequent transactions.

## Traces and Debugging

[Section titled “Traces and Debugging”](#traces-and-debugging)

If you need deeper visibility, use `tx_simulate_trace` and inspect the execution trace. This is useful for:

* pinpointing a failing opcode
* confirming storage keys touched
* evaluating gas hotspots

## Tips

[Section titled “Tips”](#tips)

* **Simulate with the same origin** you’ll use in production.
* **Use fresh state**: simulations are only valid for the current head.
* **Simulate before sealing**: sealed txs can’t be inspected in the mempool.

## Related

[Section titled “Related”](#related)

* `/guides/using-the-cli/` for call command details
* `/reference/rpc-api/` for simulation endpoints
* `/concepts/private-mempool/` for sealed transaction behavior

# Using the CLI

> Complete reference for the ashen command-line interface

The `ashen` CLI provides tools for interacting with the Ashen chain, managing contracts, and automating workflows.

## Quick Start

[Section titled “Quick Start”](#quick-start)

```bash
# Check chain status
ashen status


# Query an account
ashen account --address 0x1234...


# Call a contract method (read-only)
ashen view 0xCONTRACT balanceOf '["0xUSER"]'


# Execute a transaction
ashen call 0xCONTRACT transfer '["0xTO", 100]' --key $KEY --wait
```

## Environment Variables

[Section titled “Environment Variables”](#environment-variables)

| Variable            | Description                                     |
| ------------------- | ----------------------------------------------- |
| `NODE_RPC_URL`      | RPC endpoint (default: `http://127.0.0.1:3030`) |
| `NODE_AUTH_TOKEN`   | Optional authentication token                   |
| `ASHEN_PRIVATE_KEY` | Private key for signing transactions            |

***

## Core Commands

[Section titled “Core Commands”](#core-commands)

### `ashen status`

[Section titled “ashen status”](#ashen-status)

Get chain status including tip height, epoch, and finalized block.

```bash
ashen status
ashen status --rpc-url http://custom:3030
```

### `ashen account`

[Section titled “ashen account”](#ashen-account)

Query account information including balance and nonce lanes.

```bash
ashen account --address 0x1234...
```

### `ashen view`

[Section titled “ashen view”](#ashen-view)

Execute a read-only contract call (no transaction, no gas cost).

```bash
# Basic view call
ashen view 0xCONTRACT methodName '["arg1", "arg2"]'


# With explicit IDL path
ashen view 0xCONTRACT balanceOf '["0xUSER"]' --idl ./token.idl


# Multi-interface contract
ashen view 0xCONTRACT totalSupply --interface IERC20
```

IDLs are auto-fetched from the chain and cached for 1 hour. Use `--idl` to override.

### `ashen call`

[Section titled “ashen call”](#ashen-call)

Execute a state-changing transaction.

```bash
# Basic call (simulates only)
ashen call 0xCONTRACT transfer '["0xTO", 100]' --key $KEY


# Submit and wait for inclusion
ashen call 0xCONTRACT transfer '["0xTO", 100]' --key $KEY --wait


# Custom gas/fee
ashen call 0xCONTRACT mint '["0xTO", 1000]' --key $KEY \
  --gas-limit 500000 --max-fee 2000000 --wait
```

### `ashen abi`

[Section titled “ashen abi”](#ashen-abi)

Display a contract’s IDL/ABI.

```bash
# Pretty-printed
ashen abi 0xCONTRACT


# Raw IDL text
ashen abi 0xCONTRACT --raw
```

***

## Contract Commands

[Section titled “Contract Commands”](#contract-commands)

### `ashen contract inspect`

[Section titled “ashen contract inspect”](#ashen-contract-inspect)

Inspect a local IDL file without connecting to the chain.

```bash
ashen contract inspect --idl ./mycontract.idl
```

### `ashen contract view`

[Section titled “ashen contract view”](#ashen-contract-view)

Detailed view call with more options.

```bash
ashen contract view \
  --contract 0x1234... \
  --method balanceOf \
  --args '["0xUSER"]' \
  --idl ./token.idl \
  --origin 0xCALLER
```

### `ashen contract call`

[Section titled “ashen contract call”](#ashen-contract-call)

Detailed call with simulation and submission options.

```bash
# Simulate only (default)
ashen contract call \
  --contract 0x1234... \
  --method transfer \
  --args '["0xTO", 100]' \
  --key $KEY


# Simulate and submit
ashen contract call ... --wait


# Force submit even on simulation failure
ashen contract call ... --force --wait
```

***

## Transaction Commands

[Section titled “Transaction Commands”](#transaction-commands)

### `ashen tx by-hash`

[Section titled “ashen tx by-hash”](#ashen-tx-by-hash)

Query a transaction by its hash.

```bash
# Get status
ashen tx by-hash --tx-hash 0xABCD...


# Wait for inclusion
ashen tx by-hash --tx-hash 0xABCD... --wait --wait-timeout-s 120
```

***

## IDL Commands

[Section titled “IDL Commands”](#idl-commands)

### `ashen idl fetch`

[Section titled “ashen idl fetch”](#ashen-idl-fetch)

Fetch a contract’s IDL from the chain.

```bash
ashen idl fetch --contract 0x1234...
ashen idl fetch --contract 0x1234... --output ./contract.idl
```

### `ashen idl generate`

[Section titled “ashen idl generate”](#ashen-idl-generate)

Generate a manifest from a local IDL file (selectors, methods, types).

```bash
ashen idl generate --idl ./mycontract.idl
ashen idl generate --idl ./mycontract.idl --output ./manifest.json
```

### `ashen idl validate`

[Section titled “ashen idl validate”](#ashen-idl-validate)

Validate IDL syntax and semantics.

```bash
ashen idl validate ./mycontract.idl
```

### `ashen idl diff`

[Section titled “ashen idl diff”](#ashen-idl-diff)

Compare two IDL versions and report breaking changes.

```bash
ashen idl diff old.idl new.idl
ashen idl diff old.idl new.idl --json
```

### `ashen idl codegen`

[Section titled “ashen idl codegen”](#ashen-idl-codegen)

Generate client code from an IDL file.

```bash
# TypeScript
ashen idl codegen ./token.idl --lang ts --output-dir ./generated


# Rust
ashen idl codegen ./token.idl --lang rust --output-dir ./generated
```

Supported languages: `ts`/`typescript`, `rust`, `go`, `c`

***

## Keystore Commands

[Section titled “Keystore Commands”](#keystore-commands)

### `ashen keystore init`

[Section titled “ashen keystore init”](#ashen-keystore-init)

Initialize a new keystore.

```bash
ashen keystore init
ashen keystore init --path ~/.ashen/keystore.json
```

### `ashen keystore list`

[Section titled “ashen keystore list”](#ashen-keystore-list)

List keys in the keystore.

```bash
ashen keystore list
```

### `ashen keystore add`

[Section titled “ashen keystore add”](#ashen-keystore-add)

Add a new key.

```bash
# Generate new key
ashen keystore add --label my-key


# Import existing
ashen keystore add --label imported --secret 0x...
```

### `ashen keystore export`

[Section titled “ashen keystore export”](#ashen-keystore-export)

Export a key’s public address.

```bash
ashen keystore export --label my-key
```

***

## JSON Output Mode (Agent Automation)

[Section titled “JSON Output Mode (Agent Automation)”](#json-output-mode-agent-automation)

All `ashen` commands support structured JSON output, designed for AI agents and automation.

### How JSON Mode Works

[Section titled “How JSON Mode Works”](#how-json-mode-works)

* All `ashen` commands output **JSON** when:

  * `--json` flag is provided, OR
  * stdout is not a TTY (piped or redirected)

* Human-readable output when run interactively without `--json`

### JSON Response Schema

[Section titled “JSON Response Schema”](#json-response-schema)

**Success:**

```json
{
  "ok": true,
  "data": { ... },
  "warnings": ["optional warning messages"]
}
```

**Error:**

```json
{
  "ok": false,
  "code": "invalid_args",
  "message": "Description of what went wrong",
  "suggestions": ["possible fix 1", "possible fix 2"]
}
```

### Exit Codes

[Section titled “Exit Codes”](#exit-codes)

| Code | Meaning              |
| ---- | -------------------- |
| `0`  | Success              |
| `1`  | Not found            |
| `2`  | Invalid arguments    |
| `3`  | Authentication error |
| `4`  | Conflict             |
| `5`  | Internal error       |

### JSON Commands

[Section titled “JSON Commands”](#json-commands)

#### Chain Status

[Section titled “Chain Status”](#chain-status)

```bash
# Get chain status
ashen status --json
# Returns: tip_height, tip_hash, epoch, finalized_height, chain_id


# Get account info
ashen account --address 0x1234... --json
# Returns: address, balance, nonce_lanes, has_code
```

#### Contract Interaction

[Section titled “Contract Interaction”](#contract-interaction)

```bash
# View call (read-only)
ashen view 0xCONTRACT balanceOf '["0xUSER"]' --json


# Call with simulation only
ashen call 0xCONTRACT transfer '["0xTO", 100]' --key $KEY --json


# Submit and wait for inclusion
ashen call 0xCONTRACT transfer '["0xTO", 100]' --key $KEY --wait --json
```

#### Transaction Operations

[Section titled “Transaction Operations”](#transaction-operations)

```bash
# Get transaction details
ashen tx by-hash --tx-hash 0xHASH... --json


# Wait for tx inclusion
ashen tx by-hash --tx-hash 0xHASH... --wait --wait-timeout-s 120 --json
```

#### Contract Methods Discovery

[Section titled “Contract Methods Discovery”](#contract-methods-discovery)

```bash
# List contract methods
ashen contract inspect --idl ./contract.idl --json
ashen abi 0xCONTRACT --json
```

### Agent Workflow Example

[Section titled “Agent Workflow Example”](#agent-workflow-example)

```bash
#!/bin/bash
# Agent workflow: check balance, transfer, wait for confirmation


# 1. Check balance
BALANCE=$(ashen account --address 0xFROM... --json | jq -r '.data.balance')
echo "Current balance: $BALANCE"


# 2. Check if sufficient
if [ "$BALANCE" -lt 1000 ]; then
  echo "Insufficient balance"
  exit 1
fi


# 3. Execute transfer and wait
RESULT=$(ashen call 0xTOKEN... transfer '["0xTO...", 100]' \
  --key "$ASHEN_PRIVATE_KEY" \
  --wait --json)


# 4. Check result
if echo "$RESULT" | jq -e '.ok' > /dev/null; then
  TX_HASH=$(echo "$RESULT" | jq -r '.data.tx_hash')
  echo "Transfer successful: $TX_HASH"
else
  ERROR=$(echo "$RESULT" | jq -r '.message')
  echo "Transfer failed: $ERROR"
  exit 1
fi
```

***

## Debug Commands

[Section titled “Debug Commands”](#debug-commands)

### `ashen debug trace`

[Section titled “ashen debug trace”](#ashen-debug-trace)

Trace a transaction’s execution.

```bash
ashen debug trace --tx-hash 0x...
```

### `ashen debug replay`

[Section titled “ashen debug replay”](#ashen-debug-replay)

Replay a transaction with debugging.

```bash
ashen debug replay --tx-hash 0x... --breakpoint pc:0x1000
```

***

## Backup Commands

[Section titled “Backup Commands”](#backup-commands)

### `ashen backup export`

[Section titled “ashen backup export”](#ashen-backup-export)

Export a chain snapshot.

```bash
ashen backup export --data-dir ./node-data --output ./snapshot.tar
```

### `ashen backup import`

[Section titled “ashen backup import”](#ashen-backup-import)

Import a chain snapshot.

```bash
ashen backup import --data-dir ./node-data --input ./snapshot.tar
```

***

## BLS Commands (Validators)

[Section titled “BLS Commands (Validators)”](#bls-commands-validators)

### `ashen bls keygen`

[Section titled “ashen bls keygen”](#ashen-bls-keygen)

Generate a BLS keypair.

```bash
ashen bls keygen
```

### `ashen bls verify`

[Section titled “ashen bls verify”](#ashen-bls-verify)

Verify a BLS signature.

```bash
ashen bls verify --pubkey 0x... --message 0x... --signature 0x...
```

# Validator Operations

> Key rotation, monitoring, backup, and operational runbook for validators

## Overview

[Section titled “Overview”](#overview)

This guide covers day-to-day operations for Ashen validator nodes: key management, monitoring, backup/restore, and common operational procedures.

For initial setup, see [Running a Node](/guides/running-a-node/). For PoA allowlist management, see [PoA Policy](/operations/poa-policy/).

## Key Management

[Section titled “Key Management”](#key-management)

### Ed25519 Consensus Keys

[Section titled “Ed25519 Consensus Keys”](#ed25519-consensus-keys)

Each validator holds an ed25519 keypair used for signing blocks and consensus messages. Generate one with:

```bash
ashen keygen --json > validator.key.json


# Deterministic (for reproducible testnet setups)
ashen keygen --json --seed 12345
```

The key file contains `secret_key`, `public_key`, and `address` (inside a `data` envelope). Store the secret key securely — it controls the validator’s identity.

See [Keystore & Signatures](/reference/keystore/) for key storage details.

### BLS Threshold Keys (DKG)

[Section titled “BLS Threshold Keys (DKG)”](#bls-threshold-keys-dkg)

Validators participate in **Distributed Key Generation (DKG)** each epoch to produce a shared BLS threshold key used for:

* Finality signatures (threshold BLS aggregation)
* Threshold encryption keys for the private mempool

DKG runs automatically. Monitor its status via:

```bash
curl -s http://localhost:3030/v2/rpc \
  -d '{"jsonrpc":"2.0","id":1,"method":"validator_status","params":{}}' | jq .result.dkg
```

Response:

```json
{
  "phase": "complete",
  "epoch": 42,
  "rounds_started": 42,
  "rounds_completed": 41,
  "rounds_failed": 1,
  "fallbacks": 0
}
```

**DKG phases**: idle → commit → share → complaint → finalize → complete (or failed → fallback to deterministic keygen).

If `rounds_failed` increases, check peer connectivity and logs for DKG-related errors.

## Monitoring

[Section titled “Monitoring”](#monitoring)

### HTTP Endpoints

[Section titled “HTTP Endpoints”](#http-endpoints)

The node exposes three HTTP endpoints for monitoring:

| Endpoint       | Purpose            | Response                         |
| -------------- | ------------------ | -------------------------------- |
| `GET /metrics` | Prometheus metrics | `text/plain` (Prometheus format) |
| `GET /health`  | Liveness probe     | JSON with health status          |
| `GET /ready`   | Readiness probe    | JSON with sync/readiness status  |

These are Kubernetes-compatible. Configure probes:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 3030
readinessProbe:
  httpGet:
    path: /ready
    port: 3030
```

### Key Metrics

[Section titled “Key Metrics”](#key-metrics)

| Metric                             | Type    | Description                            |
| ---------------------------------- | ------- | -------------------------------------- |
| `ashen_block_height`               | Gauge   | Current tip height                     |
| `ashen_finalized_height`           | Gauge   | Latest finalized height                |
| `ashen_epoch`                      | Gauge   | Current consensus epoch                |
| `ashen_peer_count`                 | Gauge   | Connected P2P peers                    |
| `ashen_txpool_size`                | Gauge   | Pending transactions                   |
| `ashen_dkg_current_phase`          | Gauge   | DKG phase (0=idle..6=failed)           |
| `ashen_dkg_rounds_started`         | Counter | Total DKG rounds started               |
| `ashen_dkg_rounds_completed`       | Counter | Successful DKG rounds                  |
| `ashen_poa_validators_allowed`     | Gauge   | Validators in PoA allowlist            |
| `ashen_poa_missed_proposals_total` | Counter | Missed block proposals                 |
| `ashen_consensus_verify_total`     | Counter | Verification outcomes (success/failed) |

### Validator Status RPC

[Section titled “Validator Status RPC”](#validator-status-rpc)

The `validator_status` method returns a comprehensive operational snapshot:

```bash
curl -s http://localhost:3030/v2/rpc \
  -d '{"jsonrpc":"2.0","id":1,"method":"validator_status","params":{}}' | jq .result
```

Fields returned:

| Field                 | Description                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| `validator_pubkey`    | This node’s public key (null if not a validator)                         |
| `role`                | `leader`, `validator`, `follower`, or `observer`                         |
| `dkg`                 | DKG phase, epoch, rounds started/completed/failed, fallbacks             |
| `sync`                | `synced`, tip/finalized heights, finalization lag, time since last block |
| `peers`               | Connected/inbound/outbound peer counts, banned peers                     |
| `consensus`           | Epoch, view, leader changes, blocks finalized, verifications             |
| `epoch_key_available` | Whether the threshold encryption key is ready                            |
| `uptime_ms`           | Node uptime                                                              |

### Health Check Response

[Section titled “Health Check Response”](#health-check-response)

```json
{
  "healthy": true,
  "block_height": 12345,
  "finalized_height": 12340,
  "epoch": 42,
  "last_block_time_ms": 1706900000000,
  "uptime_seconds": 86400,
  "peer_count": 5,
  "memory_rss_bytes": 524288000,
  "dkg_current_epoch": 42,
  "dkg_current_phase": 5,
  "status": "healthy",
  "issues": []
}
```

## Backup & Restore

[Section titled “Backup & Restore”](#backup--restore)

### Data Directory Structure

[Section titled “Data Directory Structure”](#data-directory-structure)

```plaintext
node-data/
├── genesis.json           # Genesis configuration
├── chain/                 # Block and transaction data
├── state/                 # State database (accounts, storage)
├── consensus/             # Consensus state, DKG keys
└── checkpoints/           # Periodic state snapshots
```

### What to Back Up

[Section titled “What to Back Up”](#what-to-back-up)

* **`genesis.json`**: immutable after init, but essential for recovery
* **Validator key file**: the ed25519 secret key — most critical
* **`consensus/`**: DKG shares and epoch keys — loss requires re-DKG
* **`checkpoints/`**: enables fast recovery without full replay

### Checkpoints

[Section titled “Checkpoints”](#checkpoints)

Configure automatic checkpoint creation:

```bash
node run --checkpoint-interval 200   # snapshot every 200 blocks
```

List available checkpoints:

```bash
curl -s http://localhost:3030/v2/rpc \
  -d '{"jsonrpc":"2.0","id":1,"method":"list_checkpoints","params":{}}' | jq .result
```

### Restore from Checkpoint

[Section titled “Restore from Checkpoint”](#restore-from-checkpoint)

1. Stop the node.

2. Copy `genesis.json` and the validator key to a fresh data directory.

3. Start the node with the checkpoint:

   ```bash
   node run --data-dir ./restored-data --sync-from-checkpoint <height>
   ```

4. The node will sync forward from the checkpoint.

## Storage Modes

[Section titled “Storage Modes”](#storage-modes)

| Mode                 | Flag                     | Description                  |
| -------------------- | ------------------------ | ---------------------------- |
| **Pruned** (default) | `--prune-keep-epochs 10` | Keeps last N epochs          |
| **Archive**          | `--archive-mode`         | Retains all historical state |

Archive mode is required for:

* Historical state queries
* Analytics and indexing
* Serving `state_proof` for old blocks

For disk growth projections, see [Disk Growth](/operations/disk-growth/).

## Operational Procedures

[Section titled “Operational Procedures”](#operational-procedures)

### Adding a Validator (PoA)

[Section titled “Adding a Validator (PoA)”](#adding-a-validator-poa)

1. Generate the validator’s ed25519 keypair.
2. Add the public key to the allowlist file.
3. Restart nodes or wait for hot-reload.
4. Verify: check `validator_status` shows the new validator.

### Removing a Validator (PoA)

[Section titled “Removing a Validator (PoA)”](#removing-a-validator-poa)

1. Remove the public key from the allowlist file.
2. Restart nodes.
3. Confirm consensus continues (need 2/3+1 remaining).

### Emergency Validator Exclusion

[Section titled “Emergency Validator Exclusion”](#emergency-validator-exclusion)

```bash
node --poa-allowlist /path/to/allowlist.txt --poa-exclude <pubkey_hex>
```

### Consensus Stall Recovery

[Section titled “Consensus Stall Recovery”](#consensus-stall-recovery)

If consensus stops progressing:

1. Check `validator_status` — is finalization lag growing?

2. Check peer connectivity — are enough peers connected?

3. Check DKG status — did a round fail?

4. Check logs for `leader_timeout` or `notarization_timeout`.

5. If needed, restart with adjusted timeouts:

   ```bash
   node run --leader-timeout-ms 4000 --notarization-timeout-ms 8000
   ```

### Log Configuration

[Section titled “Log Configuration”](#log-configuration)

```bash
# Trace output for debugging
ASHEN_TRACE_OUTPUT=1 node run --data-dir ./node-data


# Trace to directory
ASHEN_TRACE_OUTPUT_DIR=target/feedback node run --data-dir ./node-data


# Rust log level
RUST_LOG=info,ashen=debug node run --data-dir ./node-data
```

## Related

[Section titled “Related”](#related)

* [Running a Node](/guides/running-a-node/) — initial node setup
* [PoA Policy](/operations/poa-policy/) — allowlist management
* [Disk Growth](/operations/disk-growth/) — storage projections
* [Local Devnet](/guides/devnet/) — local testing environment
* [RPC API](/reference/rpc-api/) — full method reference
* [Configuration](/reference/configuration/) — all configuration options

# VM Tooling & Test Harness

> Use vm-tooling CLI and vm-test-harness for contract inspection and testing

## Overview

[Section titled “Overview”](#overview)

Ashen ships two developer-friendly tools for smart contract work:

* **`ashen vm`**: a CLI for ELF validation, disassembly, traces, gas profiling, and code cache introspection.
* **`vm-test-harness`**: a Rust crate that runs Zig/Rust contracts in-memory without a full node.

This guide covers both, with practical examples.

## ashen vm CLI

[Section titled “ashen vm CLI”](#ashen-vm-cli)

```bash
ashen vm --help
```

### Common commands

[Section titled “Common commands”](#common-commands)

| Command            | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| `deploy-manifest`  | Emit a v1 deploy manifest                      |
| `elf-validate`     | Validate a contract ELF against the VM rules   |
| `disasm`           | Disassemble a contract ELF                     |
| `trace`            | Execute and trace a contract call              |
| `gas`              | Print the active gas schedule                  |
| `cache-stats`      | Show code cache stats and promotion thresholds |
| `predecode`        | Predecode ELF for JIT/AOT tiers                |
| `gas-profile`      | Profile per-basic-block gas usage              |
| `gas-budget-check` | Check gas profiles against `.gas-budgets.toml` |
| `corpus-freeze`    | Generate a conformance corpus                  |
| `corpus-run`       | Execute a corpus against a tier                |

### Validate a contract ELF

[Section titled “Validate a contract ELF”](#validate-a-contract-elf)

```bash
ashen vmelf-validate --elf ./contracts/my_token/zig-out/bin/my_token
```

### Disassemble a contract

[Section titled “Disassemble a contract”](#disassemble-a-contract)

```bash
ashen vmdisasm --file ./contracts/my_token/zig-out/bin/my_token
```

### Trace a contract call

[Section titled “Trace a contract call”](#trace-a-contract-call)

```bash
ashen vmtrace \
  --file ./contracts/my_token/zig-out/bin/my_token \
  --calldata-hex 0x50494e47 \
  --gas 1000000 \
  --out ./trace.json
```

`--calldata-hex` expects ABI v1 bytes: `selector || borsh(args)`.

### Gas profiling and budgets

[Section titled “Gas profiling and budgets”](#gas-profiling-and-budgets)

```bash
ashen vmgas-profile \
  --file ./contracts/my_token/zig-out/bin/my_token \
  --trace-out ./gas-trace.json
```

```bash
ashen vmgas-budget-check --config ./.gas-budgets.toml
```

### Conformance corpus

[Section titled “Conformance corpus”](#conformance-corpus)

```bash
ashen vmcorpus-freeze --out ./corpus --cases 100
ashen vmcorpus-run --dir ./corpus --tier interpreter
```

Valid tiers: `interpreter`, `jit`, `aot` (and `native` when the `cranelift-native` feature is enabled).

## vm-test-harness

[Section titled “vm-test-harness”](#vm-test-harness)

`vm-test-harness` is a Rust crate for running contracts in-memory with a deterministic host. It is ideal for unit tests and fast iteration.

Key components:

* **`TestHost`**: in-memory storage, logs, balances, and block context
* **`ContractHarness`**: loads and executes contract ELFs
* **Fixtures & assertions**: storage helpers, event checks, snapshots

### Minimal example

[Section titled “Minimal example”](#minimal-example)

```rust
use vm_test_harness::{ContractHarness, TestHost};
use vm_test_harness::{assert_call_ok, build_calldata_no_args};


let mut host = TestHost::new();
let harness = ContractHarness::from_zig_artifact("contracts/my_token/zig-out/bin/my_token")
    .expect("artifact exists")
    .expect("load contract");


let calldata = build_calldata_no_args(*b"PING");
let result = harness.call(&mut host, b"origin", b"my_token", &calldata, 1_000_000);


assert_call_ok(&result, "PING should succeed");
```

### Helpful patterns

[Section titled “Helpful patterns”](#helpful-patterns)

* Use `ContractHarness::from_zig_artifact_or_skip` in CI to skip gracefully when the ELF is missing.
* Use `StorageFixture` helpers to seed storage and verify state changes.
* Use `TestHost::snapshot()` / `restore_snapshot()` for complex flows.

For a more complete walkthrough, see `/guides/contract-testing/`.

## Related

[Section titled “Related”](#related)

* `/reference/rpc-api/` for node-side RPC call types
* `/guides/contract-testing/` for harness patterns and fixtures

# Wallet Extension

> Install, connect, and sign with the Ashen browser wallet

## Overview

[Section titled “Overview”](#overview)

The Ashen Wallet extension is a browser wallet for account management, signing, and dApp connections. It injects an EIP-1193 compatible provider into pages and uses EIP-6963 for wallet discovery.

Provider entry points:

* `window.ashenWallet`
* `window.ethereum` (legacy compatibility)

## Install (Firefox)

[Section titled “Install (Firefox)”](#install-firefox)

Build from source:

```bash
cd wallet-extension
npm install
npm run build
```

Load as a temporary add-on:

1. Open `about:debugging#/runtime/this-firefox`.
2. Click **Load Temporary Add-on**.
3. Select `wallet-extension/dist/manifest.json`.

Package as a zip:

```bash
cd wallet-extension
npm run pack:firefox
```

The zip is written to `wallet-extension/dist-packages/ashen-wallet-firefox.zip`.

## Connect a dApp

[Section titled “Connect a dApp”](#connect-a-dapp)

Request accounts (triggers a connect approval):

```js
const provider = window.ashenWallet ?? window.ethereum;
const accounts = await provider.request({ method: 'eth_requestAccounts' });
```

Notes:

* `eth_accounts` returns `[]` if the wallet is locked or the site is not connected.
* Connections are scoped by origin. Only `https://` origins and localhost are allowed; other protocols are blocked.

## Supported Provider Methods

[Section titled “Supported Provider Methods”](#supported-provider-methods)

Connection and permissions:

* `eth_requestAccounts`
* `eth_accounts`
* `eth_chainId`
* `wallet_requestPermissions`
* `wallet_getPermissions`
* `wallet_revokePermissions`

Signing:

* `eth_sendTransaction` (sign + submit)
* `eth_sign`
* `personal_sign`
* `eth_signTypedData_v4`

Notes:

* `wallet_addEthereumChain` / `wallet_switchEthereumChain` are **not supported**.
* `eth_signTypedData_v4` is currently handled as message signing (no EIP-712 domain separation).

## Allowed RPC Forwarding

[Section titled “Allowed RPC Forwarding”](#allowed-rpc-forwarding)

The extension forwards a small allowlist of RPC calls to the node:

```plaintext
eth_blockNumber
eth_getBlockByNumber
eth_getBlockByHash
eth_getTransactionByHash
eth_getTransactionReceipt
eth_call
eth_estimateGas
eth_gasPrice
eth_getBalance
eth_getCode
eth_getStorageAt
eth_getTransactionCount
eth_getLogs
eth_chainId
net_version
web3_clientVersion
chain_id
chain_accounts
chain_getBalance
chain_call
NodeRpcV1.account
NodeRpcV1.tx_build_simulate
NodeRpcV1.chain_status
NodeRpcV1.block
```

Other RPC methods are blocked at the content-script bridge.

## RPC Endpoint Settings

[Section titled “RPC Endpoint Settings”](#rpc-endpoint-settings)

The wallet exposes a configurable RPC endpoint in **Settings**. You can switch between the default endpoints or provide a custom HTTP(S) URL.

## Read Metering

[Section titled “Read Metering”](#read-metering)

Read-only RPC methods are metered per-origin. The wallet tracks read usage and can block responses once a session budget is exceeded. View call and query results may return an error if the read budget is exhausted.

## Security and UX

[Section titled “Security and UX”](#security-and-ux)

* The extension only injects in the top frame (not cross-origin iframes).
* Each signing request requires explicit user approval.
* Auto-lock and password reset are configurable in Settings.

## Related

[Section titled “Related”](#related)

* `/guides/using-the-cli/` for transaction building helpers
* `/guides/tx-simulation/` for preflight simulation workflow
* `wallet-extension/README.md` for build notes

# WebSocket Subscriptions

> Real-time notifications for finalized blocks and storage changes

## Overview

[Section titled “Overview”](#overview)

Ashen exposes a lightweight WebSocket endpoint for real-time notifications. It emits **finalized** block updates and storage change events from block execution. Use it to keep UIs and indexers in sync without polling.

## Endpoint

[Section titled “Endpoint”](#endpoint)

Connect to the same host and port as the HTTP RPC server:

* `ws://<rpc-host>/ws`
* `wss://<rpc-host>/ws` (if your node is behind TLS)

The WebSocket route is **not rate-limited** and is **not behind RPC auth**. Operators should protect it at the network or reverse-proxy layer if needed.

## Message format

[Section titled “Message format”](#message-format)

Client messages are JSON objects with a `method` and `params` field:

```json
{"method":"subscribe","params":{"event":"newBlock"}}
```

```json
{"method":"unsubscribe","params":{"event":"newBlock"}}
```

Client request field names use **camelCase** (e.g. `txHash`, `keyPrefix`).

Server messages are JSON objects with a `type` field:

```json
{"type":"subscribed","event":"newBlock","success":true}
```

Payload fields in notifications use snake\_case (e.g. `tx_hash`, `block_height`).

Errors are sent as:

```json
{"type":"error","message":"Subscription limit reached (100)"}
```

## Event types

[Section titled “Event types”](#event-types)

### `newBlock`

[Section titled “newBlock”](#newblock)

Emitted when a block is **finalized** (commit reached). Payload:

```json
{
  "type":"newBlock",
  "hash":"0x...",
  "height":123,
  "timestamp":1700000000000,
  "tx_count":42
}
```

### `storageChange`

[Section titled “storageChange”](#storagechange)

Emitted for each storage write recorded during block execution. Payload:

```json
{
  "type":"storageChange",
  "contract":"0xabc123...",
  "key":"0xdeadbeef...",
  "value":"0x01...",
  "block_height":123,
  "block_hash":"0x..."
}
```

`value` is omitted if the key was deleted. `contract` and `key` are hex-encoded byte strings (with or without a `0x` prefix).

#### Filters

[Section titled “Filters”](#filters)

`storageChange` subscriptions require a `contract` address and support three filters:

* **Exact key** (default): `keyPrefix: false`
* **Prefix**: `keyPrefix: true`
* **All keys for a contract**: omit `key`

If `contract` is missing, the server replies with an `error` message and does not add the subscription.

Examples:

```json
{"method":"subscribe","params":{"event":"storageChange","contract":"0xabc...","key":"0x00ff"}}
```

```json
{"method":"subscribe","params":{"event":"storageChange","contract":"0xabc...","key":"0x00","keyPrefix":true}}
```

```json
{"method":"subscribe","params":{"event":"storageChange","contract":"0xabc..."}}
```

### `txStatus`

[Section titled “txStatus”](#txstatus)

Defined for per-transaction status updates with these states: `pending`, `included`, `finalized`, `failed`, `dropped`.

Example payload shape:

```json
{
  "type":"txStatus",
  "tx_hash":"0x...",
  "status":"included",
  "block_height":123,
  "block_hash":"0x..."
}
```

**Note:** the node currently does not emit `txStatus` notifications. Use `tx_by_hash` / `tx_receipt` over HTTP for now.

## Subscribe / Unsubscribe behavior

[Section titled “Subscribe / Unsubscribe behavior”](#subscribe--unsubscribe-behavior)

* `newBlock` is a single subscription per connection.
* `txStatus` expects a `txHash` per subscription; omit to unsubscribe all (omit on subscribe and no events will match).
* `storageChange` expects `contract` on subscribe; omit to unsubscribe all storage filters.

Unsubscribe examples:

```json
{"method":"unsubscribe","params":{"event":"txStatus","txHash":"0x..."}}
```

```json
{"method":"unsubscribe","params":{"event":"storageChange","contract":"0xabc...","key":"0x00","keyPrefix":true}}
```

## Limits and reliability

[Section titled “Limits and reliability”](#limits-and-reliability)

* **Max 100 subscriptions** per connection (across all event types).
* The server sends periodic **ping** frames (every 30s) and closes the connection if no **pong** arrives within 10s.
* Notifications are **best-effort**. If a client falls behind, messages may be dropped. Reconnect and backfill using HTTP RPC.

## Observability

[Section titled “Observability”](#observability)

When metrics are enabled, the node exports:

* `ws_active_connections`
* `ws_messages_sent_total`

See `/metrics` on the node HTTP server.

## Example client

[Section titled “Example client”](#example-client)

```js
const ws = new WebSocket("ws://127.0.0.1:8080/ws");


ws.onopen = () => {
  ws.send(JSON.stringify({
    method: "subscribe",
    params: { event: "newBlock" },
  }));
};


ws.onmessage = (event) => {
  console.log("ws message", event.data);
};
```

## Related

[Section titled “Related”](#related)

* `/reference/rpc-api/` for HTTP RPC methods
* `/guides/tx-simulation/` for simulation endpoints used by indexers

# ADRs

> Architecture Decision Records

## Overview

[Section titled “Overview”](#overview)

Architecture Decision Records (ADRs) capture significant technical decisions with context, alternatives considered, and rationale. They live in `docs/adr/` in the repository.

Design documents in `docs/design/` serve a similar role for larger proposals that are still evolving. See [Design Documents](/internals/design/) for those.

## ADR Format

[Section titled “ADR Format”](#adr-format)

Each ADR follows a standard structure:

* **Title**: `ADR-NNNN: <Decision Title>`
* **Date**: When the decision was made
* **Status**: Draft | Proposed | Accepted | Deprecated | Superseded
* **Context**: Why the decision was needed
* **Decision**: What was decided
* **Consequences**: Trade-offs and implications

## ADR Index

[Section titled “ADR Index”](#adr-index)

### ADR-0001: Rejected State Management Approaches

[Section titled “ADR-0001: Rejected State Management Approaches”](#adr-0001-rejected-state-management-approaches)

* **Status**: Accepted
* **Date**: 2026-01-28
* **Summary**: Documents rejected state management approaches (Copy-on-Write Snapshots, Two-Level Dirty Tracking) with rationale for why each was rejected. Recommends lighter-weight alternatives that preserve deterministic behavior.
* **Source**: [`docs/adr/adr-0001-rejected-state-management-approaches.md`](https://github.com/carrion256/chain/blob/main/docs/adr/adr-0001-rejected-state-management-approaches.md)

## Design Documents

[Section titled “Design Documents”](#design-documents)

Larger proposals and design drafts live in `docs/design/`. Key documents include:

| Document                       | Status        | Summary                                                                    |
| ------------------------------ | ------------- | -------------------------------------------------------------------------- |
| VM Architecture                | Canonical     | RV64 ISA, tiered execution, cross-contract calls, state model, precompiles |
| Architecture & Boundaries      | Reference     | Core/execution/storage/consensus layering and dependency DAG               |
| State Layout                   | Draft         | Logical state layout, StateBackend mapping, Blake3 BMT commitments         |
| DKG                            | Draft         | Per-epoch threshold BLS key generation with crash recovery                 |
| Private Mempool                | Draft         | Sealed transactions and precommit protocol to prevent front-running        |
| Access Lists                   | Draft         | State prefetching, warm/cold gas pricing, parallel scheduling hints        |
| Light Client MMR               | Draft         | Trustless on-chain light client via SHA256 MMR and BLS verification        |
| Block-STM Parallel Execution   | Proposed      | Speculative parallel tx execution with conflict detection                  |
| Cross-Contract Call Tracing    | Proposed      | Hierarchical tracing capturing call trees, storage ops, gas                |
| JIT Compilation                | Draft         | Tiered JIT for hot contracts with deterministic semantics                  |
| Consensus-Execution Pipelining | Deferred      | Overlap consensus N+1 with execution of N                                  |
| Simulation Mode                | Proposed      | Execution in scratch space returning detailed state previews               |
| Vault Gas Token                | Draft         | Vault-backed gas token with staking/governance isolation                   |
| Data Availability Sampling     | Draft         | DAS via Reed-Solomon erasure coding for light clients                      |
| Cranelift AOT/JIT              | Proposed      | Native codegen tier using Cranelift                                        |
| Network Channels               | Reference     | P2P channel multiplexing for consensus, gossip, DKG, DA                    |
| ChainStore Hardening           | Draft         | Concurrent access and large chain improvements                             |
| VM Implementation Guidelines   | Non-normative | Recommended resource limits and operational parameters                     |
| Gas Profiler Flame Graphs      | Proposed      | Interactive flame graphs for per-function gas analysis                     |
| DAP Debugger                   | Proposed      | Debug Adapter Protocol integration for VS Code                             |
| Verkle Tree Migration          | Research      | Evaluation of Verkle trees; recommends deferring to late 2026              |
| DKG Refactor Analysis          | Analysis      | Custom DKG vs Commonware primitives comparison                             |

See [Design Documents](/internals/design/) for links to the full archive.

## Writing a New ADR

[Section titled “Writing a New ADR”](#writing-a-new-adr)

1. Create `docs/adr/adr-NNNN-<slug>.md` with the next available number.
2. Use the format described above.
3. Set status to **Draft** or **Proposed**.
4. Link the ADR from this index page.

# Cross-Contract Call Tracing

> Hierarchical call tracing, output formats, compression, and filtering

**Source**: `crates/vm-runtime/src/context.rs`, `crates/vm-runtime/src/trace_*.rs`

## Overview

[Section titled “Overview”](#overview)

The VM captures hierarchical call traces during contract execution. Each trace is a tree of `TraceFrame` nodes --- one per cross-contract call --- with storage operations, events, gas usage, and timing attached to the originating frame. Tracing has zero overhead when disabled.

## Data Structures

[Section titled “Data Structures”](#data-structures)

### TraceFrame

[Section titled “TraceFrame”](#traceframe)

The core node type representing a single call in the trace tree:

| Field         | Type                  | Description                   |
| ------------- | --------------------- | ----------------------------- |
| `call_type`   | `TraceCallType`       | Kind of call                  |
| `from`        | `Vec<u8>`             | Caller address                |
| `to`          | `Vec<u8>`             | Callee address                |
| `value`       | `u128`                | Value transferred             |
| `gas_limit`   | `Gas`                 | Gas allocated to this call    |
| `gas_used`    | `Gas`                 | Gas consumed                  |
| `input`       | `Vec<u8>`             | Calldata (selector + args)    |
| `output`      | `Vec<u8>`             | Return data                   |
| `storage_ops` | `Vec<TraceStorageOp>` | Storage reads/writes/deletes  |
| `events`      | `Vec<TraceLogEntry>`  | Emitted events                |
| `children`    | `Vec<TraceFrame>`     | Nested calls (recursive tree) |
| `error`       | `Option<TraceError>`  | Error if call reverted        |
| `duration_ns` | `u64`                 | Wall-clock execution time     |

### TraceCallType

[Section titled “TraceCallType”](#tracecalltype)

```plaintext
Call | StaticCall | DelegateCall | Create | Create2
```

### TraceStorageOp

[Section titled “TraceStorageOp”](#tracestorageop)

| Field          | Type                 | Description                  |
| -------------- | -------------------- | ---------------------------- |
| `op_type`      | `TraceStorageOpType` | `Read`, `Write`, or `Delete` |
| `key`          | `Vec<u8>`            | Storage key                  |
| `value_before` | `Option<Vec<u8>>`    | Value before the operation   |
| `value_after`  | `Option<Vec<u8>>`    | Value after the operation    |
| `gas_cost`     | `Gas`                | Gas cost for this operation  |

### TraceLogEntry

[Section titled “TraceLogEntry”](#tracelogentry)

| Field      | Type            | Description           |
| ---------- | --------------- | --------------------- |
| `contract` | `Vec<u8>`       | Event emitter address |
| `topics`   | `Vec<[u8; 32]>` | Indexed topics        |
| `data`     | `Vec<u8>`       | Event data            |

### TracingConfig

[Section titled “TracingConfig”](#tracingconfig)

| Field       | Default | Description                 |
| ----------- | ------- | --------------------------- |
| `max_depth` | 64      | Maximum call depth to trace |

Frames beyond `max_depth` are suppressed automatically to prevent DoS from deeply nested calls.

## Capture Mechanism

[Section titled “Capture Mechanism”](#capture-mechanism)

Tracing is driven by the `TxContext` during execution:

1. **Enable**: `ctx.enable_tracing(TracingConfig { max_depth: 64 })`
2. **Enter frame**: `ctx.enter_call_frame(call_type, from, to, value, gas, input)`
3. **During execution**: `ctx.trace_storage_op(op)` and `ctx.trace_event(event)`
4. **Exit frame**: `ctx.exit_call_frame(output, gas_used, error)`
5. **Extract**: `ctx.take_root_trace()` returns the complete call tree

The internal frame stack (`TraceFrameState`) maintains the current nesting. On exit, each frame is attached to its parent’s `children` vector or saved as the root frame.

## Output Formats

[Section titled “Output Formats”](#output-formats)

### JSON

[Section titled “JSON”](#json)

```rust
trace_format::to_json(&frame)              // Compact JSON
trace_format::to_json_pretty(&frame)       // Pretty-printed
trace_format::to_json_with_metadata(       // With tx hash and block number
    &frame, Some(&tx_hash), Some(block_number)
)
```

Addresses are hex-encoded with `0x` prefix. Byte arrays are hex-encoded.

### Chrome Trace (Visualization)

[Section titled “Chrome Trace (Visualization)”](#chrome-trace-visualization)

```rust
trace_format::to_chrome_trace(&frame)
```

Compatible with `chrome://tracing` and Perfetto. Gas used is mapped to duration for visual sizing. Call depth maps to thread ID for visual stacking.

### Human-Readable Tree

[Section titled “Human-Readable Tree”](#human-readable-tree)

```rust
trace_format::to_tree(&frame)
trace_format::to_tree_with_config(&frame, &config)
```

Example output:

```plaintext
|-- CALL 0xabc123...(0xdeadbeef)  [1,000,000 gas]
|   |-- SLOAD 0x0102...  [2,100 gas]
|   |-- SSTORE 0x0304...  [5,000 gas]
|   |-- STATICCALL 0xdef456...(0x12345678)  [50,000 gas]
|   |   '-- RETURN: 32 bytes
|   |-- EVENT 0xdddd...
|   '-- RETURN: 4 bytes  [45,230/1,000,000 gas, 4.5%]
```

`TreeConfig` presets:

| Preset      | Shows                                 |
| ----------- | ------------------------------------- |
| `minimal()` | Call structure only                   |
| `default()` | Balanced (gas, values, errors)        |
| `verbose()` | All details (storage, events, timing) |

## Trace Compression

[Section titled “Trace Compression”](#trace-compression)

**Source**: `crates/vm-runtime/src/trace_compress.rs`

Batch operations (airdrops, bulk transfers) produce massive traces with repeated subtrees. The `TraceCompressor` performs exact subtree deduplication:

| Setting           | Default | Description                            |
| ----------------- | ------- | -------------------------------------- |
| `min_repetitions` | 3       | Minimum repeats to trigger compression |
| `sample_count`    | 3       | Number of samples preserved in detail  |

Repeated subtrees are collapsed into a `Repeated` node with a template frame, repetition count, and sampled instances.

Typical compression ratios:

| Workload                 | Ratio   |
| ------------------------ | ------- |
| 1000-address airdrop     | \~1000x |
| 100 identical swaps      | \~100x  |
| Mixed batch (50% unique) | \~2x    |

The compressed trace can be `expand()`-ed back to the full tree.

## Trace Filtering

[Section titled “Trace Filtering”](#trace-filtering)

**Source**: `crates/vm-runtime/src/trace_filter.rs`

For production use, `TraceFilter` reduces overhead by selectively tracing:

| Filter                  | Description                                 |
| ----------------------- | ------------------------------------------- |
| `contracts(addresses)`  | Only trace calls to/from specific contracts |
| `failures_only()`       | Only trace reverted calls                   |
| `high_gas(threshold)`   | Only trace calls above a gas threshold      |
| `max_depth(depth)`      | Cap trace depth                             |
| `depth_range(min, max)` | Trace only a range of call depths           |
| Method selectors        | Filter by function selector                 |
| `min_value(amount)`     | Only trace calls with value transfer        |

Filters apply at two points:

* `should_trace(ctx)` --- pre-execution (skip tracing entirely)
* `should_keep(frame)` --- post-execution (prune from output)

## Trace Diffing

[Section titled “Trace Diffing”](#trace-diffing)

**Source**: `crates/vm-runtime/src/trace_diff.rs`

`diff_traces(old, new)` compares two traces for regression testing:

```rust
pub struct TraceDiff {
    pub added_frames: Vec<FramePath>,
    pub removed_frames: Vec<FramePath>,
    pub changed_frames: Vec<FrameChange>,
    pub gas_delta: i64,
}
```

Changes detected: callee, gas used, call type, outcome, value, input/output length, storage ops count, events count, and child count.

## Transaction Summary

[Section titled “Transaction Summary”](#transaction-summary)

**Source**: `crates/vm-runtime/src/trace_summary.rs`

`TraceSummary::from_trace(&root)` collapses a trace into net effects:

| Field                          | Description                             |
| ------------------------------ | --------------------------------------- |
| `storage_deltas`               | Net storage changes per (contract, key) |
| `contracts_touched`            | All contracts involved                  |
| `total_gas_used`               | Cumulative gas                          |
| `events`                       | All emitted events (flattened)          |
| `storage_reads/writes/deletes` | Operation counts                        |
| `max_depth`                    | Deepest call nesting                    |
| `total_frames`                 | Total call frames                       |
| `success`                      | Whether the root call succeeded         |

## Integration

[Section titled “Integration”](#integration)

Tracing is invoked via `execute_entrypoint_with_trace()` in the execution layer. The resulting `TraceFrame` is attached to `ExecMetadata::vm_traces` during block execution and can be retrieved per-transaction.

## Related

[Section titled “Related”](#related)

* [Gas Schedule](/reference/gas-schedule/) --- storage op costs visible in traces
* [Precompiles & Syscalls](/reference/precompiles/) --- syscalls appear as trace events

# Design Documents

> Internal design docs

## Overview

[Section titled “Overview”](#overview)

Design documents live in two places:

* **Upcoming drafts**: in the docs site under [/upcoming/](/upcoming/).
* **Repo archive**: source-of-truth markdown in `docs/design` and `ideas/design`.

## Links

[Section titled “Links”](#links)

* [Upcoming designs](/upcoming/)
* [Design archive (docs/design)](https://github.com/carrion256/chain/tree/main/docs/design)
* [Idea sketches (ideas/design)](https://github.com/carrion256/chain/tree/main/ideas/design)

# DKG Flow

> Distributed key generation protocol for threshold BLS keys

This document traces the complete DKG flow from epoch triggering through threshold key usage.

## Overview

[Section titled “Overview”](#overview)

DKG generates **threshold BLS keys** each epoch. No single validator holds the full private key - instead, each validator holds a **share** that can produce partial signatures. Combining `t-of-n` partial signatures yields a valid threshold signature.

```plaintext
Epoch boundary approaches --> DKG triggered --> 4-phase protocol -->
Threshold keys generated --> Keys used for TLE decryption & VRF
```

## Key Properties

[Section titled “Key Properties”](#key-properties)

| Property                 | Value                           |
| ------------------------ | ------------------------------- |
| **Curve**                | BLS12-381 (MinSig variant)      |
| **Threshold**            | \~2/3 + 1 of validators         |
| **Public key type**      | G2 element                      |
| **Signature/share type** | G1 element / Scalar             |
| **Share encryption**     | X25519 ECDH + ChaCha20-Poly1305 |
| **Lead time**            | 10 blocks before epoch boundary |

***

## 1. Epoch Triggering

[Section titled “1. Epoch Triggering”](#1-epoch-triggering)

DKG is triggered when approaching an epoch boundary:

```rust
// In DkgDriver event loop
match event {
    DkgDriverEvent::BlockFinalized { height } => {
        // Check if we should start DKG for next epoch
        if height % epoch_length >= epoch_length - lead_blocks {
            let next_epoch = (height / epoch_length) + 1;
            self.start_round(rng, next_epoch, participants)?;
        }
    }
}
```

### Configuration

[Section titled “Configuration”](#configuration)

```rust
DkgConfig {
    commit_timeout: Duration::from_secs(30),
    share_timeout: Duration::from_secs(30),
    complaint_timeout: Duration::from_secs(30),
    finalize_timeout: Duration::from_secs(30),
    lead_blocks: 10,           // Start DKG 10 blocks before epoch end
    max_retries: 3,
    retry_base_delay: Duration::from_secs(1),
    retry_max_delay: Duration::from_secs(30),
}
```

### Round Initialization

[Section titled “Round Initialization”](#round-initialization)

```rust
fn start_round<R: Rng + CryptoRng>(
    &mut self,
    rng: &mut R,
    epoch: u64,
    participants: Set<PublicKey>,
) -> Result<(), DkgError> {
    let n = participants.len() as u32;
    let t = compute_threshold(n);  // ~2/3 + 1


    // Generate fresh polynomial and shares
    let (polynomial, shares) = ops::generate_shares::<_, MinSig>(rng, None, n, t)?;


    // Create round state
    let round = DkgRoundState::new(epoch, participants, polynomial, shares);
    self.coordinator.in_progress.insert(epoch, round);


    Ok(())
}
```

***

## 2. Phase 1: Commitment Broadcasting

[Section titled “2. Phase 1: Commitment Broadcasting”](#2-phase-1-commitment-broadcasting)

Each validator acting as dealer broadcasts their polynomial commitment.

### Commitment Structure

[Section titled “Commitment Structure”](#commitment-structure)

```rust
pub struct DkgCommitment {
    pub epoch: u64,
    pub dealer: Vec<u8>,       // Dealer's ed25519 public key
    pub commitment: Vec<u8>,   // Serialized polynomial commitment (G2 elements)
    pub signature: Vec<u8>,    // ed25519 signature
}
```

### Signing

[Section titled “Signing”](#signing)

```rust
// Domain separator
const COMMITMENT_DOMAIN: &[u8] = b"CHAIN-DKG-COMMITMENT-V1";


fn sign_commitment(epoch: u64, polynomial: &Poly<Evaluation>) -> DkgCommitment {
    let commitment_bytes = serialize_polynomial(polynomial);
    let message = [
        COMMITMENT_DOMAIN,
        &dealer_pubkey,
        &epoch.to_le_bytes(),
        &sha256(&commitment_bytes),
    ].concat();


    let signature = ed25519_sign(&privkey, &message);
    // ...
}
```

### Handler

[Section titled “Handler”](#handler)

```rust
fn handle_commitment(&mut self, commitment: DkgCommitment) -> Result<(), DkgError> {
    // 1. Validate dealer is in participant set
    // 2. Verify ed25519 signature
    // 3. Store in round.commitments
    round.commitments.insert(dealer_pubkey, commitment.commitment);
    Ok(())
}
```

***

## 3. Phase 2: Share Distribution

[Section titled “3. Phase 2: Share Distribution”](#3-phase-2-share-distribution)

Each dealer encrypts and sends a unique share to each participant.

### Share Message Structure

[Section titled “Share Message Structure”](#share-message-structure)

```rust
pub struct DkgShareMessage {
    pub epoch: u64,
    pub dealer: Vec<u8>,           // Dealer's ed25519 public key
    pub recipient: Vec<u8>,        // Recipient's ed25519 public key
    pub encrypted_share: Vec<u8>,  // X25519 + ChaCha20-Poly1305 ciphertext
    pub signature: Vec<u8>,        // ed25519 signature
}
```

### Encryption Flow

[Section titled “Encryption Flow”](#encryption-flow)

```rust
fn encrypt_share(
    recipient_ed25519: &[u8; 32],
    share: &group::Share,
) -> Vec<u8> {
    // 1. Convert ed25519 pubkey to X25519
    let recipient_x25519 = ed25519_pubkey_to_x25519(recipient_ed25519);


    // 2. Generate ephemeral X25519 keypair
    let ephemeral_secret = EphemeralSecret::random_from_rng(rng);
    let ephemeral_public = X25519PublicKey::from(&ephemeral_secret);


    // 3. ECDH key exchange
    let shared_secret = ephemeral_secret.diffie_hellman(&recipient_x25519);


    // 4. Derive ChaCha20-Poly1305 key
    let key = sha256(shared_secret.as_bytes());


    // 5. Encrypt
    let nonce = random_nonce_12();
    let ciphertext = ChaCha20Poly1305::encrypt(&key, &nonce, &share_bytes);


    // 6. Format: ephemeral_pubkey (32) || nonce (12) || ciphertext
    [ephemeral_public.as_bytes(), &nonce, &ciphertext].concat()
}
```

### Decryption Flow

[Section titled “Decryption Flow”](#decryption-flow)

```rust
fn decrypt_share(
    my_ed25519_privkey: &[u8; 32],
    encrypted_share: &[u8],
) -> Result<group::Share, DkgError> {
    // 1. Parse ciphertext
    let ephemeral_public = &encrypted_share[0..32];
    let nonce = &encrypted_share[32..44];
    let ciphertext = &encrypted_share[44..];


    // 2. Convert ed25519 privkey to X25519
    let my_x25519_secret = ed25519_privkey_to_x25519(my_ed25519_privkey);


    // 3. ECDH with ephemeral public
    let shared_secret = my_x25519_secret.diffie_hellman(ephemeral_public);


    // 4. Derive same key
    let key = sha256(shared_secret.as_bytes());


    // 5. Decrypt
    let plaintext = ChaCha20Poly1305::decrypt(&key, nonce, ciphertext)?;


    // 6. Deserialize share
    deserialize_share(&plaintext)
}
```

***

## 4. Phase 3: Complaints & Justifications

[Section titled “4. Phase 3: Complaints & Justifications”](#4-phase-3-complaints--justifications)

Handles disputes when shares are invalid or missing.

### Complaint Structure

[Section titled “Complaint Structure”](#complaint-structure)

```rust
pub struct DkgComplaint {
    pub epoch: u64,
    pub complainer: Vec<u8>,
    pub dealer: Vec<u8>,
    pub reason: ComplaintReason,  // MissingShare | InvalidShare | InvalidCommitment
    pub signature: Vec<u8>,
}
```

### Justification Structure

[Section titled “Justification Structure”](#justification-structure)

```rust
pub struct DkgJustification {
    pub epoch: u64,
    pub dealer: Vec<u8>,
    pub complainer: Vec<u8>,
    pub revealed_share: Vec<u8>,  // Share in plaintext for public verification
    pub signature: Vec<u8>,
}
```

When a dealer receives a complaint, they can reveal the share publicly. All validators can then verify if the share matches the commitment.

***

## 5. Phase 4: Finalization

[Section titled “5. Phase 4: Finalization”](#5-phase-4-finalization)

When threshold conditions are met, finalize the DKG round.

### Threshold Check

[Section titled “Threshold Check”](#threshold-check)

```rust
if commitments.len() < threshold as usize {
    return Err(DkgError::ThresholdNotMet { ... });
}
```

### Aggregation Process

[Section titled “Aggregation Process”](#aggregation-process)

```rust
fn finalize_round(&mut self, epoch: u64) -> Result<DkgOutput, DkgError> {
    let round = self.coordinator.in_progress.get(&epoch)?;


    // 1. Deserialize all commitments
    let commitments: Vec<Poly<Evaluation>> = round.commitments
        .values()
        .filter_map(|bytes| deserialize_polynomial(bytes).ok())
        .collect();


    // 2. Parallel verify all shares against commitments
    let verified_shares: Vec<group::Share> = shares_to_verify
        .par_iter()
        .filter_map(|(dealer, share, dealer_idx)| {
            let commitment = commitments.get(dealer_idx)?;
            if ops::verify_share::<MinSig>(commitment, my_index, &share).is_ok() {
                Some(share.clone())
            } else {
                None
            }
        })
        .collect();


    // 3. Include our own dealing share
    verified_shares.push(our_dealing_share);


    // 4. Aggregate public polynomial (combines all dealer commitments)
    let aggregate_polynomial = ops::construct_public::<MinSig>(
        commitments.iter(),
        threshold
    )?;


    // 5. Aggregate shares (sum scalars - Shamir aggregation)
    let aggregate_share = aggregate_shares(&verified_shares, my_index)?;


    // 6. Create output
    Ok(DkgOutput {
        polynomial: aggregate_polynomial,  // Collective BLS public key
        share: aggregate_share,            // Our threshold share
        participants: participants.clone(),
    })
}
```

### DKG Output

[Section titled “DKG Output”](#dkg-output)

```rust
pub struct DkgOutput {
    pub polynomial: Poly<Evaluation>,    // BLS12-381 polynomial (G2 for MinSig)
    pub share: group::Share,             // Our private threshold share (scalar)
    pub participants: Set<PublicKey>,    // Ordered participant list
}
```

The **collective public key** is the polynomial evaluated at 0: `polynomial.evaluate(0)`.

***

## 6. Registration in Supervisor

[Section titled “6. Registration in Supervisor”](#6-registration-in-supervisor)

After DKG completes, keys are registered for use:

```rust
pub fn register_dkg_output(
    &self,
    epoch: Epoch,
    polynomial: Poly<Evaluation>,
    share: group::Share,
    participants: Set<PublicKey>,
) {
    let mut inner = self.inner.write();
    inner.dkg_polynomials.insert(epoch, polynomial);
    inner.dkg_shares.insert(epoch, share);
}
```

### Accessing Keys

[Section titled “Accessing Keys”](#accessing-keys)

```rust
pub fn dkg_polynomial(&self, epoch: Epoch) -> Option<Poly<Evaluation>> {
    // Returns polynomial where P(0) = collective BLS public key
}


pub fn dkg_share(&self, epoch: Epoch) -> Option<group::Share> {
    // Returns our threshold share for signing
}
```

***

## 7. Threshold Key Usage

[Section titled “7. Threshold Key Usage”](#7-threshold-key-usage)

### TLE Encryption (Client Side)

[Section titled “TLE Encryption (Client Side)”](#tle-encryption-client-side)

```rust
pub fn seal(
    plaintext: &[u8],
    master_public: &G2,  // Collective public key from DKG
    epoch: u64,
) -> Result<TleSealedTransaction, ...> {
    // Encrypt using collective public key
    // Can only be decrypted with threshold signature
}
```

### TLE Decryption (Validator Side)

[Section titled “TLE Decryption (Validator Side)”](#tle-decryption-validator-side)

Each validator produces a **partial signature**:

```rust
pub fn sign_decryption_share(
    share: &group::Share,  // Our DKG share
    epoch: u64,
) -> TleDecryptionShare {
    let target = epoch.to_le_bytes();
    let partial_sig = ops::sign_message::<MinSig>(
        &share.secret,
        Some(TLE_TARGET_PREFIX),
        &target
    );
    // Returns G1 element
}
```

Leader combines `t-of-n` partial signatures:

```rust
pub fn combine_partial_signatures(
    threshold: usize,
    partial_sigs: &[(u16, G1Affine)],
) -> Result<G1Affine, ...> {
    // Lagrange interpolation in G1
    ops::threshold_signature_recover::<MinSig, _>(threshold, partial_sigs)
}
```

Threshold signature decrypts the ciphertext:

```rust
pub fn unseal(
    &self,
    threshold_sig: &G1Affine,
    expected_epoch: u64,
) -> Result<Vec<u8>, ...> {
    tle::decrypt::<MinSig>(threshold_sig, &ciphertext)
}
```

***

## 8. Fallback Mechanism

[Section titled “8. Fallback Mechanism”](#8-fallback-mechanism)

If DKG fails, the previous epoch’s keys can be used:

```rust
pub struct DkgCoordinatorState {
    pub completed: BTreeMap<u64, DkgOutput>,
    pub in_progress: BTreeMap<u64, DkgRoundState>,
    pub fallback_epoch: Option<u64>,          // Last successful epoch
    pub last_epoch_used_fallback: Option<u64>,
}
```

**Rules**:

* Can fallback to previous epoch’s keys if DKG fails
* Cannot use fallback for two consecutive epochs
* `ConsecutiveFallback` error if epoch N and N+1 both fail

***

## 9. Sequence Diagram

[Section titled “9. Sequence Diagram”](#9-sequence-diagram)

```plaintext
EPOCH BOUNDARY APPROACHING (height % epoch_length >= epoch_length - lead_blocks)
    │
    ▼
DkgDriver triggered
    │
    ├─ start_round(epoch, participants)
    │  └─ ops::generate_shares() → polynomial + shares
    │
    ▼
PHASE 1: COMMITMENT (timeout: 30s)
    │
    ├─ Each dealer broadcasts DkgCommitment
    │  ├─ Serialize polynomial commitment (G2 elements)
    │  ├─ Sign with ed25519
    │  └─ Broadcast to all
    │
    ├─ Validators receive and verify
    │  └─ Store in round.commitments
    │
    ▼
PHASE 2: SHARE DISTRIBUTION (timeout: 30s)
    │
    ├─ Each dealer sends DkgShareMessage to each recipient
    │  ├─ Encrypt share (X25519 ECDH + ChaCha20-Poly1305)
    │  ├─ Sign with ed25519
    │  └─ Send to recipient
    │
    ├─ Recipients decrypt and verify
    │  └─ Store in round.shares
    │
    ▼
PHASE 3: COMPLAINTS & JUSTIFICATIONS (timeout: 30s)
    │
    ├─ If share invalid/missing → DkgComplaint
    ├─ Dealer responds with DkgJustification (revealed share)
    └─ Public verification against commitment
    │
    ▼
PHASE 4: FINALIZATION (timeout: 30s)
    │
    ├─ Check threshold met (>= t commitments)
    │
    ├─ Deserialize all commitments
    │
    ├─ Parallel verify shares against commitments
    │
    ├─ Aggregate public polynomial
    │  └─ ops::construct_public() → Poly<G2>
    │
    ├─ Aggregate shares (sum scalars)
    │  └─ aggregate_shares() → group::Share
    │
    ├─ Create DkgOutput { polynomial, share, participants }
    │
    └─ Mark complete: coordinator.completed[epoch] = output
    │
    ▼
REGISTRATION IN SUPERVISOR
    │
    ├─ register_dkg_output(epoch, polynomial, share)
    │
    └─ Keys available for threshold operations
    │
    ▼
USAGE
    │
    ├─ TLE Encryption: polynomial.evaluate(0) as master public key (G2)
    │
    ├─ TLE Decryption:
    │  ├─ Each validator: sign_decryption_share(share, epoch) → G1
    │  ├─ Leader: combine_partial_signatures(t, partials) → G1
    │  └─ Decrypt: tle::decrypt(threshold_sig, ciphertext)
    │
    └─ VRF: Similar threshold signature flow
```

***

## 10. Type Reference

[Section titled “10. Type Reference”](#10-type-reference)

```plaintext
BLS12-381 MinSig Variant:
├─ Public key: G2 element (96 bytes)
├─ Signature: G1 element (48 bytes)
└─ Secret: Scalar in Fr field


DKG Types:
├─ Poly<Evaluation>: Polynomial with G2 coefficients
├─ group::Share: { index: u32, secret: Scalar }
└─ Threshold signature: G1 element


Identity:
├─ Network identity: ed25519 public key (32 bytes)
└─ Share encryption: X25519 (derived from ed25519)
```

***

## Related Documentation

[Section titled “Related Documentation”](#related-documentation)

* [Sealed Transactions](/internals/flows/sealed-transactions/) - TLE encryption/decryption using DKG keys
* [Finalization Flow](/internals/flows/finalization/) - Block finalization with BLS signatures

# Finalization Flow

> Block finalization with BLS threshold signatures

This document traces the complete block finalization flow including BLS aggregation, threshold signatures, and light client verification.

## Overview

[Section titled “Overview”](#overview)

Block finalization uses **threshold BLS signatures** - each validator signs with their DKG share, and `2f+1` signatures are aggregated into a single compact certificate. Light clients can verify finality using only the aggregate public key.

```plaintext
Block proposed --> Validators vote (BLS shares) --> Aggregate 2f+1 sigs -->
Finality certificate --> Persist --> Light client verifies
```

## Architecture Stack

[Section titled “Architecture Stack”](#architecture-stack)

```plaintext
Simplex Consensus (BFT voting)
    |
Marshal (certificate persistence)
    |
Application Actor (block execution, finality proofs)
    |
Ashen Store (persistent finalized blocks)
```

***

## 1. Block Proposal

[Section titled “1. Block Proposal”](#1-block-proposal)

### Proposal Flow

[Section titled “Proposal Flow”](#proposal-flow)

```rust
async fn handle_propose_request(&mut self, round: Round) {
    // 1. Get parent block
    let parent = self.tip.as_ref().unwrap_or(&genesis);


    // 2. Select transactions from txpool
    let txs = self.txpool.select_block_txs(max_txs, max_gas);


    // 3. Load parent VRF output for randomness
    let parent_vrf = if let Some(proof) = self.load_finality_proof(parent_height) {
        proof.vrf_output()
    } else {
        Hash::default()
    };


    // 4. Build execution context
    let ctx = ExecutionContext {
        timestamp,
        validator_set_id,
        epoch,
        view,
        parent_vrf_output: parent_vrf,
        proposer: self.address,
    };


    // 5. Execute and compute state root
    let (header, _) = self.exec.build_block_preview(parent, &txs, ctx)?;


    // 6. Cache block (Arc for efficiency)
    let block = Arc::new(Block { header, execution });
    self.blocks_by_hash.insert(block_hash, block.clone());
    self.pending_proposals.put(round, block);


    // 7. Send hash to Simplex
    simplex_mailbox.propose(block_hash).await;
}
```

***

## 2. Consensus Voting (Simplex)

[Section titled “2. Consensus Voting (Simplex)”](#2-consensus-voting-simplex)

Validators vote on proposed blocks using their BLS shares from DKG.

### BLS Scheme Types

[Section titled “BLS Scheme Types”](#bls-scheme-types)

```rust
pub type PublicKey = ed25519::PublicKey;           // Network identity
pub type Scheme = bls12381_threshold::Scheme<PublicKey, MinSig>;
pub type Evaluation = <MinSig as Variant>::Public; // G2 element
```

**MinSig Variant** (signature minimization):

* Public key: G2 element (\~96 bytes)
* Signature: G1 element (\~48 bytes)
* Aggregation: G1 point addition

### Validator Signing

[Section titled “Validator Signing”](#validator-signing)

Each validator produces a partial BLS signature using their DKG share:

```rust
// Validator i signs with their share
let partial_sig = ops::sign_message::<MinSig>(
    &my_share.secret,  // Scalar from DKG
    Some(FINALIZE_DOMAIN),
    &proposal_hash,
);
// Result: G1 element
```

### Signature Aggregation

[Section titled “Signature Aggregation”](#signature-aggregation)

When `2f+1` votes are collected:

```rust
// Aggregate via G1 point addition
let aggregate_sig = partial_sigs
    .iter()
    .fold(G1Projective::identity(), |acc, sig| acc + sig);


// Result: Single G1 element representing all votes
```

***

## 3. Finality Certificate

[Section titled “3. Finality Certificate”](#3-finality-certificate)

### Structure

[Section titled “Structure”](#structure)

```rust
pub struct FinalityProof {
    pub header: BlockHeader,                    // Finalized block
    pub epoch: u64,                             // Consensus epoch
    pub view: u64,                              // Round in epoch
    pub parent_view: u64,                       // Parent's round
    pub key_version: u32,                       // Validator set version
    pub certificate: FinalityCertificateBytes,  // Threshold BLS sig
}


pub struct FinalityCertificateBytes {
    pub bytes: Vec<u8>,  // Borsh-encoded SimplexFinalization
}
```

### Certificate Contents

[Section titled “Certificate Contents”](#certificate-contents)

The certificate encodes a `SimplexFinalization`:

```rust
SimplexFinalization {
    proposal: Proposal {
        round: Round { epoch, view },
        parent_view: View,
        payload: block_hash,  // SHA256 digest
    },
    certificate: ThresholdSignature,  // Aggregated G1 point
}
```

### VRF Output Derivation

[Section titled “VRF Output Derivation”](#vrf-output-derivation)

```rust
pub fn vrf_output(&self) -> Hash {
    let mut hasher = Blake3::new();
    hasher.update(&self.certificate.bytes);
    Hash::from(hasher.finalize())
}
```

**Properties**:

* Unpredictable until `2f+1` validators sign
* Deterministic given the certificate
* Used for on-chain randomness, leader election

***

## 4. Aggregate BLS Public Key

[Section titled “4. Aggregate BLS Public Key”](#4-aggregate-bls-public-key)

```rust
pub struct AggregateBlsPublicKey(pub G2);
```

### Derivation from DKG

[Section titled “Derivation from DKG”](#derivation-from-dkg)

The aggregate key is the constant term of the DKG polynomial:

```rust
// From DKG output
let aggregate_key = polynomial.evaluate(0);  // G2 element


// Create validator set with aggregate key
let validator_set = ValidatorSet {
    aggregate_bls_pubkey: AggregateBlsPublicKey(aggregate_key),
    validators: vec![...],
};
```

### Validator Set Structure

[Section titled “Validator Set Structure”](#validator-set-structure)

```rust
pub struct ValidatorSet {
    pub aggregate_bls_pubkey: AggregateBlsPublicKey,
    pub validators: Vec<Validator>,
}


pub struct Validator {
    pub network_pubkey: NetworkPublicKey,  // ed25519
    pub voting_power: u64,
    pub address: Address,
    pub fee_recipient: Address,
}
```

***

## 5. Validator Set Commitment

[Section titled “5. Validator Set Commitment”](#5-validator-set-commitment)

The validator set is committed via a Merkle-like tree:

```rust
pub fn commitment_root(&self) -> Hash {
    let mut leaves = Vec::with_capacity(self.validators.len() + 1);


    // Leaf 0: aggregate BLS key
    leaves.push(self.aggregate_key_leaf_hash());


    // Leaves 1..n: individual validators
    for i in 0..self.validators.len() {
        leaves.push(self.validator_leaf_hash(i)?);
    }


    merkle_root(&leaves)
}
```

### Aggregate Key Leaf

[Section titled “Aggregate Key Leaf”](#aggregate-key-leaf)

```rust
pub fn aggregate_key_leaf_hash(&self) -> Hash {
    let preimage = AggregateKeyLeafPreimage {
        prefix: b"AGG_KEY_V1",
        aggregate_bls_pubkey: &self.aggregate_bls_pubkey,
    };


    sha256(&preimage.to_bytes())
}
```

***

## 6. Persistent Storage

[Section titled “6. Persistent Storage”](#6-persistent-storage)

### Marshal Finalization Store

[Section titled “Marshal Finalization Store”](#marshal-finalization-store)

```rust
pub struct PersistentFinalizationStore<E> {
    archive: PrunableArchive<FourCap, E, Digest, Vec<u8>>,
}


impl store::Certificates for PersistentFinalizationStore {
    async fn put(
        &mut self,
        height: u64,
        commitment: Digest,
        finalization: SimplexFinalization<Scheme, Digest>,
    ) -> Result<()> {
        let bytes = finalization.encode();
        self.archive.put(height, commitment, bytes).await
    }
}
```

### Application Block Finalization

[Section titled “Application Block Finalization”](#application-block-finalization)

```rust
async fn handle_finalized_block(&mut self, block: Block) {
    let height = block.header.height;


    // 1. Execute transactions
    let meta = self.exec.apply_block(&block)?;


    // 2. Update txpool
    self.txpool.on_applied_block(height, &self.exec.state, &block.transactions);


    // 3. ATOMIC: Persist block + finalized height
    self.store.put_block_finalized(&block).await?;
    self.finalized_height = height;


    // 4. Finalize state
    let root = self.exec.finalize_state(height)?;


    // 5. Generate DA chunks
    let bundle = self.chunk_producer.encode_block(&block);
    self.pending_chunks.put(block_hash, bundle);


    // 6. Update tip
    self.tip = Some(Arc::new(block));


    // 7. Notify DKG
    self.dkg_finalization_tx.send(height);


    // 8. WebSocket notifications
    self.bus.emit_block(BlockNotification { ... });
}
```

### Finality Proof Persistence

[Section titled “Finality Proof Persistence”](#finality-proof-persistence)

```rust
async fn handle_tip_update(&mut self, height: u64, commitment: Digest) {
    // Get finalization from marshal
    let finalization = marshal_mailbox.get_finalization(height).await?;


    // Get block
    let block = self.store.get_block_by_height(height).await?;


    // Create FinalityProof
    let proof = FinalityProof::from_certificate(
        block.header.clone(),
        epoch,
        view,
        finalization.proposal.parent.get(),
        finalization.certificate,
    );


    // Persist
    self.store.put_finality_proof(&proof).await?;
    self.latest_finality = Some(proof);
}
```

***

## 7. Light Client Verification

[Section titled “7. Light Client Verification”](#7-light-client-verification)

### Light Client Context

[Section titled “Light Client Context”](#light-client-context)

```rust
pub struct LightClientContext {
    pub validator_set: ValidatorSet,
    pub aggregate_key_proof: ValidatorProof,  // Merkle proof
    pub version: u32,
}
```

### Verification Function

[Section titled “Verification Function”](#verification-function)

```rust
pub fn verify_finality_proof(
    proof: &FinalityProof,
    ctx: &LightClientContext,
) -> Result<(), LightClientError> {
    // 1. Check validator set commitment
    let root = ctx.commitment_root();
    if root != proof.header.validator_set_id.id {
        return Err(LightClientError::ValidatorSetIdMismatch);
    }


    // 2. Verify aggregate key membership proof
    if ctx.aggregate_key_proof.leaf_index != 0 {
        return Err(LightClientError::InvalidMembershipProof);
    }
    if !ctx.aggregate_key_proof.verify(&root) {
        return Err(LightClientError::InvalidMembershipProof);
    }


    // 3. Verify threshold BLS signature
    if !proof.verify(&ctx.validator_set.aggregate_bls_pubkey) {
        return Err(LightClientError::InvalidSignature);
    }


    Ok(())
}
```

### BLS Signature Verification

[Section titled “BLS Signature Verification”](#bls-signature-verification)

```rust
pub fn verify(&self, aggregate_bls_pubkey: &AggregateBlsPublicKey) -> bool {
    // 1. Decode certificate
    let certificate = self.decode_certificate()?;


    // 2. Reconstruct proposal
    let proposal = Proposal::new(
        Round::new(Epoch::new(self.epoch), View::new(self.view)),
        View::new(self.parent_view),
        self.block_id().into(),
    );


    // 3. Create verifier with aggregate key
    let scheme = Scheme::certificate_verifier(aggregate_bls_pubkey.0);


    // 4. Verify threshold signature
    scheme.verify_certificate(
        &mut rng,
        namespace(),
        Subject::Finalize { proposal: &proposal },
        &certificate,
    )
}
```

***

## 8. Validator Set Transitions

[Section titled “8. Validator Set Transitions”](#8-validator-set-transitions)

### Announcement

[Section titled “Announcement”](#announcement)

When the validator set changes, the block header announces it:

```rust
pub struct BlockHeader {
    pub validator_set_id: ValidatorSetId,       // Current
    pub next_validator_set_id: ValidatorSetId,  // Next (if different)
    // ...
}
```

### Light Client State Machine

[Section titled “Light Client State Machine”](#light-client-state-machine)

```rust
pub struct LightClientState {
    pub context: LightClientContext,
    pub pending_update: Option<PendingUpdate>,
    pub current_epoch: u64,
    pub latest_height: u64,
}


pub fn process_finality_proof(&mut self, proof: &FinalityProof) -> Result<()> {
    // Verify against current context
    verify_finality_proof(proof, &self.context)?;


    // Check for validator set change announcement
    if proof.header.next_validator_set_id != proof.header.validator_set_id {
        self.pending_update = Some(PendingUpdate {
            next_validator_set_id: proof.header.next_validator_set_id.clone(),
            announced_at_epoch: proof.header.epoch,
        });
    }


    self.latest_height = proof.header.height;
    Ok(())
}


pub fn apply_validator_set_update(
    &mut self,
    new_context: LightClientContext,
    transition_proof: &FinalityProof,
) -> Result<()> {
    let pending = self.pending_update.as_ref()?;


    // Verify new commitment matches announced
    if new_context.commitment_root() != pending.next_validator_set_id.id {
        return Err(LightClientError::TransitionCommitmentMismatch);
    }


    // Verify proof with new context
    verify_finality_proof(transition_proof, &new_context)?;


    // Must be at epoch boundary
    if transition_proof.header.epoch <= pending.announced_at_epoch {
        return Err(LightClientError::TransitionNotAtEpochBoundary);
    }


    self.context = new_context;
    self.pending_update = None;
    Ok(())
}
```

***

## 9. Sequence Diagram

[Section titled “9. Sequence Diagram”](#9-sequence-diagram)

```plaintext
BLOCK PROPOSAL
    │
    ├─ Application: handle_propose_request()
    │  ├─ Select transactions
    │  ├─ Load parent VRF output
    │  ├─ Build execution context
    │  ├─ Compute state root
    │  └─ Send block hash to Simplex
    │
    ▼
CONSENSUS VOTING (Simplex)
    │
    ├─ Validators receive proposal
    ├─ Each validator signs with BLS share
    │  └─ partial_sig = sign(share, proposal_hash)
    ├─ Collect 2f+1 partial signatures
    └─ Aggregate: threshold_sig = sum(partial_sigs)
    │
    ▼
FINALIZATION CERTIFICATE (Marshal)
    │
    ├─ Create SimplexFinalization
    │  ├─ proposal: (round, parent_view, block_hash)
    │  └─ certificate: aggregated BLS signature
    ├─ Encode to bytes
    └─ Store in PersistentFinalizationStore
    │
    ▼
FINALITY PROOF (Application)
    │
    ├─ FinalityProof::from_certificate()
    │  ├─ header: BlockHeader
    │  ├─ epoch, view, parent_view
    │  ├─ key_version
    │  └─ certificate: encoded threshold sig
    │
    ├─ VRF output = Blake3(certificate.bytes)
    │
    └─ Persist to ChainStore
    │
    ▼
POST-FINALIZATION
    │
    ├─ Execute transactions
    ├─ Update txpool
    ├─ Persist block (atomic with height)
    ├─ Finalize state
    ├─ Generate DA chunks
    ├─ Notify DKG coordinator
    └─ WebSocket notifications
    │
    ▼
LIGHT CLIENT VERIFICATION
    │
    ├─ 1. Check validator_set_id matches commitment_root
    │
    ├─ 2. Verify aggregate key Merkle proof
    │  ├─ leaf_index = 0
    │  ├─ leaf_hash = aggregate_key_leaf_hash()
    │  └─ Merkle path leads to root
    │
    └─ 3. Verify threshold BLS signature
       ├─ Decode certificate
       ├─ Reconstruct proposal
       ├─ Create verifier with aggregate key
       └─ Verify over Subject::Finalize
```

***

## 10. Cryptographic Components

[Section titled “10. Cryptographic Components”](#10-cryptographic-components)

| Component               | Type   | Size       | Purpose                   |
| ----------------------- | ------ | ---------- | ------------------------- |
| **Aggregate BLS Key**   | G2     | \~96 bytes | Threshold public key      |
| **Threshold Signature** | G1     | \~48 bytes | Aggregated 2f+1 votes     |
| **Block Hash**          | SHA256 | 32 bytes   | Payload commitment        |
| **VRF Output**          | Blake3 | 32 bytes   | Verifiable randomness     |
| **Validator Set Root**  | SHA256 | 32 bytes   | Merkle commitment         |
| **Partial Signature**   | G1     | \~48 bytes | Individual validator vote |

***

## 11. Safety Properties

[Section titled “11. Safety Properties”](#11-safety-properties)

| Property                  | Mechanism                                      |
| ------------------------- | ---------------------------------------------- |
| **Threshold Security**    | Requires 2f+1 of n validators                  |
| **Non-Repudiation**       | Threshold BLS proves collective commitment     |
| **Unbiasable Randomness** | VRF unpredictable until threshold reached      |
| **Crash Safety**          | Atomic block + height persistence              |
| **Validator Continuity**  | Epoch boundary transitions verified            |
| **Light Client Trust**    | Single aggregate key + Merkle proof sufficient |

***

## Related Documentation

[Section titled “Related Documentation”](#related-documentation)

* [DKG Flow](/internals/flows/dkg/) - How threshold keys are generated
* [Sealed Transactions](/internals/flows/sealed-transactions/) - TLE using threshold sigs
* [Light Clients](/concepts/light-clients/) - Light client architecture

# Sealed Transactions

> Time-lock encrypted private transaction flow

This document traces the complete flow of sealed (encrypted) transactions from client submission through decryption and execution.

## Overview

[Section titled “Overview”](#overview)

The chain implements **Time-Lock Encryption (TLE)** using BLS12-381 threshold cryptography. No single validator can decrypt transactions - they must cooperate to reach threshold.

```plaintext
Client seals tx --> Gossip --> Mempool --> Leader selects -->
DecryptionRequest --> Validators send shares --> Combine shares -->
Decrypt --> Execute --> Finalize block
```

## Two Encryption Schemes

[Section titled “Two Encryption Schemes”](#two-encryption-schemes)

| Scheme          | Status        | Use Case                                          |
| --------------- | ------------- | ------------------------------------------------- |
| TLE (BLS12-381) | **Preferred** | Threshold encryption requiring t-of-n cooperation |
| X25519          | Deprecated    | Per-message ECDH + ChaCha20-Poly1305              |

This document focuses on the TLE scheme.

***

## 1. Transaction Sealing (Client Side)

[Section titled “1. Transaction Sealing (Client Side)”](#1-transaction-sealing-client-side)

The client encrypts using the collective BLS public key:

```rust
pub fn seal(
    plaintext: &[u8],
    collective_pk: &G2Affine,
    epoch: u64,
) -> Result<Self, TleSealError>
```

### Process

[Section titled “Process”](#process)

1. Pad plaintext to 32-byte block boundary

2. For each 32-byte block:

   * Encrypt using `tle::encrypt::<MinSig>(collective_pk, target, block)`
   * Target = domain separator + epoch bytes

3. Concatenate ciphertext blocks

4. Compute Blake3 commitment hash for FIFO ordering

### Ciphertext Format

[Section titled “Ciphertext Format”](#ciphertext-format)

Each 32-byte plaintext block produces 112 bytes of ciphertext:

```plaintext
Block = U (G1, 48 bytes) || V (32 bytes) || W (32 bytes)
```

### Wire Format

[Section titled “Wire Format”](#wire-format)

```rust
TleSealedTransaction {
    epoch: u64,                    // Encryption epoch (matches DKG)
    ciphertext_bytes: Vec<u8>,     // blocks * 112 bytes
    block_count: u32,              // Number of ciphertext blocks
    plaintext_len: u32,            // Original plaintext length
    commitment: Hash,              // Blake3(ciphertext) for ordering
}
```

### Domain Separator

[Section titled “Domain Separator”](#domain-separator)

```rust
const TLE_TARGET_PREFIX: &[u8] = b"chain-tle-v1";
```

***

## 2. Submission and Gossip

[Section titled “2. Submission and Gossip”](#2-submission-and-gossip)

### Gossip Message Types

[Section titled “Gossip Message Types”](#gossip-message-types)

```rust
pub enum TxGossipMessage {
    Plaintext(SignedTransaction),           // variant 0
    Sealed(SealedTransaction),              // variant 1 (X25519, deprecated)
    DecryptShare(DecryptionShare),          // variant 2 (X25519)
    TleSealed(TleSealedTransaction),        // variant 3
    TleDecryptShare(TleDecryptionShare),    // variant 4
    TleDecryptionRequest(DecryptionRequest),// variant 5
}
```

### Mempool Storage

[Section titled “Mempool Storage”](#mempool-storage)

```rust
// Configuration
max_sealed_txs: 10_000,
max_sealed_per_block: 500,
```

Sealed transactions are stored separately from regular transactions. No decryption is attempted at this stage.

***

## 3. Block Production and Decryption Request

[Section titled “3. Block Production and Decryption Request”](#3-block-production-and-decryption-request)

The Application Actor maintains:

```rust
struct Actor {
    tle_collector: Option<TleDecryptionCollector>,
    tle_gossip_tx: Option<mpsc::Sender<TxGossipMessage>>,
    supervisor: Option<ViewSupervisor>,
    // ...
}
```

### When Leader Builds a Block

[Section titled “When Leader Builds a Block”](#when-leader-builds-a-block)

1. Select sealed transactions from mempool (FIFO order)

2. Create `TleDecryptionCollector` with selected transactions

3. Broadcast `DecryptionRequest`:

   ```rust
   DecryptionRequest {
       height: BlockHeight,
       epoch: u64,
       tx_commitments: Vec<Hash>,
   }
   ```

4. Wait for validator shares with timeout

***

## 4. Validator Share Generation

[Section titled “4. Validator Share Generation”](#4-validator-share-generation)

When a validator receives a `DecryptionRequest`:

### Process

[Section titled “Process”](#process-1)

1. Retrieve DKG secret key share for the epoch

2. For each transaction commitment:

   ```rust
   TleDecryptionShare::sign(
       share_sk: &Scalar,
       validator_index: u16,
       tx_commitment: Hash,
       epoch: u64,
   )
   ```

3. Sign the epoch target:

   ```rust
   ops::sign_message::<MinSig>(share_sk, Some(TLE_TARGET_PREFIX), &target)
   ```

4. Broadcast share via gossip

### Share Format

[Section titled “Share Format”](#share-format)

```rust
TleDecryptionShare {
    validator_index: u16,      // Which validator
    signature_bytes: [u8; 48], // G1 point (partial BLS signature)
    tx_commitment: Hash,       // Which transaction
    epoch: u64,                // Epoch binding
}
```

***

## 5. Share Collection and Combination

[Section titled “5. Share Collection and Combination”](#5-share-collection-and-combination)

### TleDecryptionCollector

[Section titled “TleDecryptionCollector”](#tledecryptioncollector)

```rust
impl TleDecryptionCollector {
    // Initialize with sealed transactions
    pub fn new(sealed_txs: Vec<TleSealedTransaction>) -> Self;


    // Accept incoming shares
    pub fn add_share(&mut self, share: TleDecryptionShare) -> bool;


    // Check if threshold reached (f+1)
    pub fn has_enough_shares(&self, threshold: usize) -> bool;


    // Core decryption
    pub fn decrypt_all(&self, threshold: usize) -> Result<Vec<Vec<u8>>, ...>;
}
```

### Threshold Signature Recovery

[Section titled “Threshold Signature Recovery”](#threshold-signature-recovery)

```rust
pub fn combine_partial_signatures(
    threshold: usize,
    partial_sigs: &[(u16, G1Affine)],  // (validator_index, signature)
) -> Result<G1Affine, CombineError>
```

Uses Lagrange interpolation:

```rust
ops::threshold_signature_recover::<MinSig, _>(threshold, &partial_sigs)
```

***

## 6. Transaction Decryption

[Section titled “6. Transaction Decryption”](#6-transaction-decryption)

```rust
pub fn unseal(
    &self,
    threshold_sig: &G1Affine,
    expected_epoch: u64,
) -> Result<Vec<u8>, TleUnsealError>
```

### Process

[Section titled “Process”](#process-2)

1. Validate epoch binding (prevents cross-epoch replay)

2. For each ciphertext block:

   * Extract U (G1), V (32 bytes), W (32 bytes)
   * Call `tle::decrypt::<MinSig>(threshold_sig, &ciphertext)`
   * Recover plaintext block

3. Concatenate blocks

4. Truncate to original `plaintext_len`

5. Return plaintext bytes

### Convenience Function

[Section titled “Convenience Function”](#convenience-function)

```rust
pub fn decrypt_with_shares(
    sealed: &TleSealedTransaction,
    shares: &[TleDecryptionShare],
    threshold: usize,
    expected_epoch: u64,
) -> Result<Vec<u8>, ...>
```

Single call that combines shares and unseals.

***

## 7. Transaction Execution

[Section titled “7. Transaction Execution”](#7-transaction-execution)

The decrypted plaintext is deserialized:

```rust
let signed_tx: SignedTransaction = borsh::from_slice(&plaintext)?;
```

Then normal execution proceeds:

1. **Signature Verification**: ed25519 public key check
2. **Nonce Check**: Verify nonce matches expected for (authorizer, nonce\_space)
3. **Balance Check**: Ensure payer has sufficient balance for max\_fee
4. **Gas Accounting**: Charge base gas + access list prefetch gas
5. **VM Execution**: Run contract bytecode if call\_data present
6. **State Update**: Apply changes to balances, nonces, storage

### Result

[Section titled “Result”](#result)

```rust
pub struct ExecutionOutcome {
    pub status: ExecutionStatus,  // Success | Revert | Rejected | Trap
    pub gas_used: u64,
    pub logs: Vec<Log>,
    pub return_data: Option<Vec<u8>>,
}
```

***

## Security Properties

[Section titled “Security Properties”](#security-properties)

| Property               | Mechanism                                                            |
| ---------------------- | -------------------------------------------------------------------- |
| **Threshold Security** | Requires t-of-n validators to decrypt (no single validator can read) |
| **Epoch Binding**      | Encryption target includes epoch, prevents cross-epoch replay        |
| **FIFO Ordering**      | Commitment hash enables ordering verification without decryption     |
| **Tamper Resistance**  | Ciphertext commitment hash detects modifications                     |
| **Replay Protection**  | Epoch + commitment hash combination                                  |

***

## Sequence Diagram

[Section titled “Sequence Diagram”](#sequence-diagram)

```plaintext
User              Node           Mempool        Leader         Validators
 |                  |               |              |                |
 | seal(tx, pk)     |               |              |                |
 |----------------->|               |              |                |
 |                  | gossip(TleSealed)            |                |
 |                  |-------------->|              |                |
 |                  |               | store        |                |
 |                  |               |              |                |
 |                  |               |              | select()       |
 |                  |               |<-------------|                |
 |                  |               |              |                |
 |                  |               |              | DecryptionRequest
 |                  |               |              |--------------->|
 |                  |               |              |                |
 |                  |               |              |  TleDecryptShare
 |                  |               |              |<---------------|
 |                  |               |              |                |
 |                  |               |              | combine_shares |
 |                  |               |              |----+           |
 |                  |               |              |    |           |
 |                  |               |              |<---+           |
 |                  |               |              |                |
 |                  |               |              | unseal()       |
 |                  |               |              |----+           |
 |                  |               |              |    |           |
 |                  |               |              |<---+           |
 |                  |               |              |                |
 |                  |               |              | execute()      |
 |                  |               |              |----+           |
 |                  |               |              |    |           |
 |                  |               |              |<---+           |
 |                  |               |              |                |
 |                  |               |              | finalize block |
 |<-----------------|---------------|--------------|                |
 | tx_included      |               |              |                |
```

***

## Related Documentation

[Section titled “Related Documentation”](#related-documentation)

* [DKG Flow](/internals/flows/dkg/) - Distributed key generation for threshold keys
* [Finalization Flow](/internals/flows/finalization/) - Block finalization process

# Txpool Policy

> Mempool policy, eviction rules, and tuning knobs

This document summarizes the mempool policy, eviction rules, and the knobs that control pool behavior. Defaults are in code; there is no runtime config surface yet, so changing these requires code edits.

## Eviction Policy (Normal Txpool)

[Section titled “Eviction Policy (Normal Txpool)”](#eviction-policy-normal-txpool)

* **Ordering:** lowest `(max_fee, priority_tip)` evicted first, with `(inserted_at_ms, tx_hash)` as tie-breakers.
* **Trigger:** when `txpool.len() > max_txs`.
* **Location:** `src/txpool.rs` (fee-ordered `by_fee` index).

## Eviction Policy (Sealed / Private Mempool)

[Section titled “Eviction Policy (Sealed / Private Mempool)”](#eviction-policy-sealed--private-mempool)

* **Ordering:** FIFO by arrival time.
* **Trigger:** when `sealed_len() > max_sealed_txs`.
* **Location:** `src/txpool.rs` (sealed `BTreeMap` by arrival).

## Admission Limits (RPC Ingress)

[Section titled “Admission Limits (RPC Ingress)”](#admission-limits-rpc-ingress)

These are enforced before the tx enters the pool:

| Limit                        | Description            |
| ---------------------------- | ---------------------- |
| `TX_MAX_SIZE_BYTES`          | Max serialized tx size |
| `TX_MAX_CALLDATA_BYTES`      | Max calldata size      |
| `TX_MAX_DEPLOY_BUNDLE_BYTES` | Max deploy payload     |
| `TX_MIN_FEE_FLOOR`           | Minimum fee threshold  |
| `TX_MAX_PENDING_PER_SENDER`  | Per-sender queue cap   |

**Location:** `src/bin/node.rs`.

## Txpool Configuration Knobs

[Section titled “Txpool Configuration Knobs”](#txpool-configuration-knobs)

These live in `txpool::Config` (`src/txpool.rs`) and are wired into the application config via `AppConfig` (`src/application/config.rs`).

| Knob                   | Description                |
| ---------------------- | -------------------------- |
| `max_txs`              | Pool size cap              |
| `max_txs_per_block`    | Max txs selected per block |
| `max_age_ms`           | TTL for stale tx pruning   |
| `max_txs_per_sender`   | Per-sender limit           |
| `max_txs_per_lane`     | Per-lane limit             |
| `max_lanes_per_sender` | Lanes per sender           |
| `max_tx_bytes`         | Estimated size limit       |
| `max_sealed_txs`       | Sealed pool size cap       |
| `max_sealed_per_block` | Max sealed txs per block   |

## Fee Thresholds

[Section titled “Fee Thresholds”](#fee-thresholds)

* **Minimum fee:** `TX_MIN_FEE_FLOOR` (currently `1`).
* **Eviction comparator:** `(max_fee, priority_tip)` from `FeeIntent::V1`.

## Tuning Guidance

[Section titled “Tuning Guidance”](#tuning-guidance)

Until a runtime config file is added, changes require editing the constants in `src/bin/node.rs` and/or defaults in `src/txpool.rs`.

### Recommended Adjustments

[Section titled “Recommended Adjustments”](#recommended-adjustments)

| Scenario             | Adjustment                                                 |
| -------------------- | ---------------------------------------------------------- |
| High throughput      | Increase `max_txs`, `max_txs_per_block`                    |
| Resource constrained | Decrease `max_txs`, `max_tx_bytes`                         |
| Spam protection      | Increase `TX_MIN_FEE_FLOOR`, decrease `max_txs_per_sender` |
| Sealed tx heavy      | Increase `max_sealed_txs`, `max_sealed_per_block`          |

# Disk Growth Guidance

> Disk sizing and growth estimates for node operators

This document provides disk growth estimates and sizing recommendations for testnet and mainnet deployments.

## Storage Components

[Section titled “Storage Components”](#storage-components)

The chain stores data in several components:

| Component       | Location            | Growth Rate           | Description                        |
| --------------- | ------------------- | --------------------- | ---------------------------------- |
| Blocks          | `data/blocks/`      | \~2-5 KB/block        | Block headers and transaction data |
| State           | `data/state/`       | Variable              | Account state, contract storage    |
| Marshal Archive | `data/marshal/`     | \~1-3 KB/finalization | Finality proofs and attestations   |
| Checkpoints     | `data/checkpoints/` | \~10-50 MB/checkpoint | Periodic state snapshots           |

## Estimating Growth

[Section titled “Estimating Growth”](#estimating-growth)

### Per-Block Growth

[Section titled “Per-Block Growth”](#per-block-growth)

```plaintext
block_size = header_size + (tx_count * avg_tx_size)
           = ~200 bytes + (N * ~250 bytes)
```

For a network with:

* 1 block/second
* Average 10 txs/block
* \~2.7 KB/block

**Monthly growth**: \~7 GB/month raw blocks

### Per-Finalization Growth

[Section titled “Per-Finalization Growth”](#per-finalization-growth)

Finality proofs include BLS signatures and attestations:

* \~1-3 KB per finalization
* With 1 finalization/second: \~2.5-7.5 GB/month

### State Growth

[Section titled “State Growth”](#state-growth)

State growth depends heavily on contract activity:

* Account creation: \~100 bytes/account
* Contract deployment: \~1-100 KB/contract
* Storage writes: 32 bytes key + value size

## Recommended Sizing

[Section titled “Recommended Sizing”](#recommended-sizing)

### Testnet Node

[Section titled “Testnet Node”](#testnet-node)

| Resource                | Minimum    | Recommended |
| ----------------------- | ---------- | ----------- |
| Disk                    | 100 GB SSD | 250 GB NVMe |
| Expected 6-month growth | \~50 GB    | \~50 GB     |
| Headroom                | 50 GB      | 200 GB      |

### Mainnet Validator

[Section titled “Mainnet Validator”](#mainnet-validator)

| Resource               | Minimum     | Recommended |
| ---------------------- | ----------- | ----------- |
| Disk                   | 500 GB NVMe | 1 TB NVMe   |
| Expected 1-year growth | \~200 GB    | \~200 GB    |
| Headroom               | 300 GB      | 800 GB      |

### Archive Node

[Section titled “Archive Node”](#archive-node)

Archive nodes retain all historical state:

| Resource               | Minimum         | Recommended     |
| ---------------------- | --------------- | --------------- |
| Disk                   | 2 TB NVMe       | 4 TB NVMe       |
| Expected 1-year growth | \~500 GB - 1 TB | \~500 GB - 1 TB |

## Monitoring Disk Usage

[Section titled “Monitoring Disk Usage”](#monitoring-disk-usage)

### Key Metrics

[Section titled “Key Metrics”](#key-metrics)

Monitor these Prometheus metrics to track disk usage:

```promql
# Block height (track growth rate)
rate(ashen_block_height[1h]) * 3600


# Estimated blocks per day
rate(ashen_block_height[1d]) * 86400


# Transaction throughput
rate(ashen_block_transaction_count[5m])
```

### Grafana Dashboard

[Section titled “Grafana Dashboard”](#grafana-dashboard)

The included dashboard (`ops/grafana/ashen-dashboard.json`) provides:

* Block height and finalized height
* Transaction throughput
* RPC request rates
* Block production timing
* Txpool size

### Disk Usage Alerts

[Section titled “Disk Usage Alerts”](#disk-usage-alerts)

Recommended Prometheus alert rules:

```yaml
groups:
  - name: disk-alerts
    rules:
      - alert: DiskSpaceLow
        expr: node_filesystem_avail_bytes{mountpoint="/data"} / node_filesystem_size_bytes{mountpoint="/data"} < 0.15
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Disk space below 15%"


      - alert: DiskSpaceCritical
        expr: node_filesystem_avail_bytes{mountpoint="/data"} / node_filesystem_size_bytes{mountpoint="/data"} < 0.05
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Disk space below 5%"
```

## Pruning Strategies

[Section titled “Pruning Strategies”](#pruning-strategies)

### Block Pruning (Non-Archive Nodes)

[Section titled “Block Pruning (Non-Archive Nodes)”](#block-pruning-non-archive-nodes)

Keep only recent blocks (e.g., last 10,000):

```bash
# Pruning is configured via node config
--pruning-keep-recent 10000
```

### State Snapshots

[Section titled “State Snapshots”](#state-snapshots)

State checkpoints are stored and accessible via RPC (`NodeRpcV1.list_checkpoints`, `NodeRpcV1.get_checkpoint`).

**Note**: Automatic checkpoint interval configuration (`--checkpoint-interval`) is not yet implemented. Checkpoints are currently created during state sync and snapshot operations.

### Log Rotation

[Section titled “Log Rotation”](#log-rotation)

Configure log rotation for node logs:

/etc/logrotate.d/ashen-node

```bash
/var/log/ashen-node/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
}
```

## Capacity Planning

[Section titled “Capacity Planning”](#capacity-planning)

### Formula

[Section titled “Formula”](#formula)

```plaintext
required_disk = current_usage
              + (daily_growth * retention_days)
              + (headroom_factor * 1.2)
```

### Example Calculation

[Section titled “Example Calculation”](#example-calculation)

For a testnet validator running 6 months:

* Current usage: 20 GB
* Daily growth: \~300 MB
* Retention: 180 days
* Headroom factor: 1.2

```plaintext
required_disk = 20 GB + (0.3 GB * 180) + (54 GB * 0.2)
              = 20 GB + 54 GB + 10.8 GB
              = ~85 GB minimum
              = ~125 GB recommended (with buffer)
```

## Performance Considerations

[Section titled “Performance Considerations”](#performance-considerations)

### SSD vs HDD

[Section titled “SSD vs HDD”](#ssd-vs-hdd)

* **Required**: NVMe SSD for validators
* **Acceptable**: SATA SSD for archive/RPC nodes
* **Not recommended**: HDD (too slow for consensus)

### IOPS Requirements

[Section titled “IOPS Requirements”](#iops-requirements)

| Node Type | Minimum IOPS | Recommended IOPS |
| --------- | ------------ | ---------------- |
| Validator | 5,000        | 10,000+          |
| RPC Node  | 3,000        | 5,000+           |
| Archive   | 1,000        | 3,000+           |

### Filesystem

[Section titled “Filesystem”](#filesystem)

* **Recommended**: ext4 or XFS
* **Mount options**: `noatime,nodiratime`

# PoA Validator Policy

> Proof of Authority validator allowlist enforcement

This document describes the PoA validator policy enforcement mechanism for controlling which validators can participate in consensus during Proof of Authority phases of network operation.

## Overview

[Section titled “Overview”](#overview)

The PoA policy enforcement allows network operators to restrict consensus participation to a defined set of validators via an allowlist. This is useful during:

* Initial network bootstrap (controlled validator set)
* Network upgrades (limiting participants to trusted validators)
* Emergency situations (excluding potentially malicious validators)

## Configuration

[Section titled “Configuration”](#configuration)

PoA policy is configured via the `PoaConfig` struct in the consensus engine configuration.

### Configuration Options

[Section titled “Configuration Options”](#configuration-options)

```rust
pub struct PoaConfig {
    /// Path to a file containing allowed validator public keys (hex-encoded, one per line).
    pub allowlist_file: Option<PathBuf>,


    /// Inline allowlist of validator public keys (hex-encoded).
    pub allowlist: HashSet<String>,


    /// If true, reject participants not in the allowlist. Default: true.
    pub strict: bool,
}
```

### Allowlist File Format

[Section titled “Allowlist File Format”](#allowlist-file-format)

The allowlist file is a simple text file with one hex-encoded ed25519 public key per line:

```plaintext
# Comments are allowed (lines starting with #)
# Empty lines are ignored


a1b2c3d4e5f6...  # 64 hex characters (32 bytes)
f1e2d3c4b5a6...
```

Each public key must be:

* Exactly 64 hexadecimal characters
* Lowercase (automatically normalized)
* No prefix (no `0x`)

### CLI Integration

[Section titled “CLI Integration”](#cli-integration)

To enable PoA filtering via CLI:

```bash
# Using an allowlist file
node --poa-allowlist /path/to/allowlist.txt


# Using inline allowlist (comma-separated)
node --poa-allowlist-inline a1b2c3...,f1e2d3...


# Permissive mode (log warnings but allow all)
node --poa-allowlist /path/to/allowlist.txt --poa-permissive
```

## Enforcement Modes

[Section titled “Enforcement Modes”](#enforcement-modes)

### Strict Mode (default)

[Section titled “Strict Mode (default)”](#strict-mode-default)

In strict mode (`strict: true`):

* Only validators in the allowlist can participate in consensus
* Non-allowed validators are excluded from the scheme and validator set
* Warnings are logged for each excluded validator

### Permissive Mode

[Section titled “Permissive Mode”](#permissive-mode)

In permissive mode (`strict: false`):

* All validators can participate regardless of allowlist
* Warnings are logged for validators not in the allowlist
* Useful for monitoring/auditing before enforcing restrictions

## Implementation Details

[Section titled “Implementation Details”](#implementation-details)

### Engine Initialization

[Section titled “Engine Initialization”](#engine-initialization)

During engine initialization (`Engine::new`):

1. If `poa` config is provided, load the combined allowlist (file + inline)
2. Filter participants against the allowlist
3. Create the signing scheme with filtered participants only
4. Build the validator set from filtered participants
5. Log summary: total, allowed, rejected counts

### SLA Metrics

[Section titled “SLA Metrics”](#sla-metrics)

The following metrics are available for monitoring PoA policy enforcement:

| Metric                               | Type      | Description                          |
| ------------------------------------ | --------- | ------------------------------------ |
| `ashen_poa_allowlist_checks_total`   | Counter   | Total PoA allowlist checks performed |
| `ashen_poa_validators_allowed`       | Gauge     | Validators allowed after filtering   |
| `ashen_poa_validators_rejected`      | Gauge     | Validators rejected by filtering     |
| `ashen_poa_strict_mode`              | Gauge     | 1 if strict, 0 if permissive         |
| `ashen_poa_missed_proposals_total`   | Counter   | Missed proposals by validator        |
| `ashen_poa_proposal_latency_seconds` | Histogram | Proposal latency by validator        |

## Operational Runbook

[Section titled “Operational Runbook”](#operational-runbook)

### Adding a New Validator

[Section titled “Adding a New Validator”](#adding-a-new-validator)

1. Generate the validator’s ed25519 keypair
2. Add the public key (hex) to the allowlist file
3. Restart nodes or use hot-reload (if supported)
4. Verify in logs: “PoA allowlist filtering applied”

### Removing a Validator

[Section titled “Removing a Validator”](#removing-a-validator)

1. Remove the public key from the allowlist file
2. Restart nodes
3. Confirm in logs the validator is excluded
4. Monitor for consensus health

### Emergency Validator Exclusion

[Section titled “Emergency Validator Exclusion”](#emergency-validator-exclusion)

For immediate exclusion without file changes:

```bash
# Inline exclusion overrides file
node --poa-allowlist /path/to/allowlist.txt --poa-exclude a1b2c3...
```

### Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

**Symptom**: Consensus not progressing after PoA change

1. Check if enough validators remain (need 2/3+1 for BFT)
2. Verify allowlist syntax (64 hex chars, no 0x prefix)
3. Check logs for “Validator not in PoA allowlist” warnings

**Symptom**: Validator keeps participating despite exclusion

1. Ensure strict mode is enabled (`strict: true`)
2. Verify the node was restarted
3. Check the public key format matches exactly

## Security Considerations

[Section titled “Security Considerations”](#security-considerations)

* The allowlist file should be read-only to the node process
* Use file permissions to restrict access (e.g., `chmod 600 allowlist.txt`)
* Consider using a configuration management system for distributed deployments
* Audit all allowlist changes through version control

## Future Enhancements

[Section titled “Future Enhancements”](#future-enhancements)

* Hot reload: Update allowlist without restart
* On-chain governance: Allowlist controlled by governance contract
* Multi-sig approval: Require multiple signatures to modify allowlist
* Time-based policies: Automatic validator rotation schedules

# State Sync & Checkpoints

> Fast node bootstrap via verified state snapshots and checkpoint streaming

State sync allows new nodes to join the network without replaying the entire block history. Instead, a joining node downloads a verified state snapshot at a recent checkpoint and replays only the blocks after that point.

## Overview

[Section titled “Overview”](#overview)

The state sync system has three layers:

1. **Checkpoints** - periodic state commitments recorded at finalized heights
2. **Snapshots** - exportable bundles of headers, MMR entries, and checkpoint metadata
3. **State streaming** - a P2P protocol for downloading state entries in paginated chunks

```plaintext
Checkpoint creation (validator)
        │
        ▼
┌──────────────────┐     ┌──────────────────┐
│  SnapshotManifest │     │   LightSnapshot   │
│  (full headers +  │     │  (single header + │
│   MMR entries +   │     │   MMR proof +     │
│   validator sets) │     │   finality proof) │
└────────┬─────────┘     └────────┬─────────┘
         │                        │
         ▼                        ▼
   Full sync path           Fast sync path
   (export/import)       (P2P state streaming)
```

## Checkpoints

[Section titled “Checkpoints”](#checkpoints)

A checkpoint is a `(height, state_root)` pair recorded when a block is finalized. The `state_root` is a Blake3 commitment over the execution state at that height.

### When checkpoints are created

[Section titled “When checkpoints are created”](#when-checkpoints-are-created)

Checkpoints are created during block finalization when the block height satisfies the configured interval:

```bash
# Configure checkpoint interval (every 1000 blocks)
ashen node run --checkpoint-interval 1000
```

When no interval is configured, checkpoints are created only during snapshot operations and state sync.

### Storage

[Section titled “Storage”](#storage)

Checkpoints are stored under `data/checkpoints/` and managed through the `ChainStore` trait:

| Operation                  | Description                                   |
| -------------------------- | --------------------------------------------- |
| `put_state_checkpoint`     | Store a new checkpoint                        |
| `state_checkpoint(height)` | Fetch checkpoint at a specific height         |
| `latest_state_checkpoint`  | Get the most recent checkpoint                |
| `list_checkpoints(limit)`  | List checkpoints ordered by height descending |

## Snapshot Types

[Section titled “Snapshot Types”](#snapshot-types)

### Full Snapshot (`SnapshotManifest`)

[Section titled “Full Snapshot (SnapshotManifest)”](#full-snapshot-snapshotmanifest)

A full snapshot contains everything needed to bootstrap a node from genesis:

| Field            | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| `headers`        | Block headers from genesis to checkpoint (ascending order) |
| `mmr_entries`    | Finalized MMR entries corresponding to each header         |
| `mmr_root`       | Expected MMR root after all entries are added              |
| `checkpoint`     | Height and state root at the snapshot point                |
| `validator_sets` | Validator sets for all epochs in the range                 |
| `finality_proof` | BLS threshold certificate for the checkpoint block         |

Full snapshots use Borsh serialization and can be exported/imported via the `export_snapshot` and `import_snapshot` functions.

### Light Snapshot (`LightSnapshot`)

[Section titled “Light Snapshot (LightSnapshot)”](#light-snapshot-lightsnapshot)

A light snapshot is a minimal proof bundle for nodes that already have a trusted MMR root (e.g., from a light client):

| Field            | Description                                   |
| ---------------- | --------------------------------------------- |
| `checkpoint`     | Height and state root                         |
| `header`         | Block header at the checkpoint height         |
| `mmr_proof`      | MMR membership proof for the checkpoint block |
| `finality_proof` | BLS threshold certificate (optional)          |
| `validator_set`  | Validator set for the checkpoint epoch        |

Light snapshots are verified against a trusted MMR root rather than replaying the full header chain.

## State Sync Protocol

[Section titled “State Sync Protocol”](#state-sync-protocol)

New nodes download state entries over the follower sync P2P channel using a request/response protocol.

### Message Types

[Section titled “Message Types”](#message-types)

| Message                   | Direction    | Purpose                                                   |
| ------------------------- | ------------ | --------------------------------------------------------- |
| `StateCheckpointRequest`  | Node -> Peer | Query checkpoint metadata at a height                     |
| `StateCheckpointResponse` | Peer -> Node | Returns height, state root, total entry count, block hash |
| `StateChunkRequest`       | Node -> Peer | Request a page of state entries                           |
| `StateChunkResponse`      | Peer -> Node | Returns state entries with pagination cursor              |

### Protocol Limits

[Section titled “Protocol Limits”](#protocol-limits)

| Limit                            | Value |
| -------------------------------- | ----- |
| Max headers per response         | 64    |
| Max finality proofs per response | 64    |
| Max state entries per chunk      | 1,024 |

### Sync Session

[Section titled “Sync Session”](#sync-session)

The `StateSyncSession` manages the download lifecycle through five phases:

```plaintext
FetchingCheckpoint -> Downloading -> Importing -> Verifying -> Complete
                                                      │
                                                      └─> Failed
```

**Downloading**: state entries are fetched in chunks via `StateChunkRequest` with offset-based pagination. Each chunk is validated against the checkpoint height.

**Importing**: pending entries are written to the state backend via `import_pending()`.

**Verifying**: the state root is recomputed from imported entries and compared against the checkpoint’s `state_root`. A mismatch aborts the sync.

### Default Configuration

[Section titled “Default Configuration”](#default-configuration)

| Parameter                 | Default | Description                 |
| ------------------------- | ------- | --------------------------- |
| `chunk_size`              | 512     | Entries requested per chunk |
| `request_timeout`         | 30s     | Timeout per chunk request   |
| `max_concurrent_requests` | 4       | Parallel chunk downloads    |
| `retry_attempts`          | 3       | Retries per failed chunk    |
| `retry_delay`             | 1s      | Delay between retries       |

## Bootstrap Flow

[Section titled “Bootstrap Flow”](#bootstrap-flow)

A new node joining the network follows this sequence:

### 1. Header Sync

[Section titled “1. Header Sync”](#1-header-sync)

The node requests block headers from peers via `HeaderRequest` messages, verifying:

* Finality proofs (BLS threshold signatures) against known validator sets
* Chain continuity (each header’s `parent_hash` matches the previous header’s hash)

### 2. Checkpoint Discovery

[Section titled “2. Checkpoint Discovery”](#2-checkpoint-discovery)

The node queries a recent checkpoint:

```plaintext
StateCheckpointRequest { height: None }  // latest checkpoint
    -> StateCheckpointResponse { height, state_root, total_entries, block_hash }
```

For verified sync, the node fetches a light snapshot and verifies it against a trusted MMR root:

```plaintext
get_light_snapshot(height)
    -> { checkpoint, header, mmr_proof, finality_proof, validators, snapshot_bytes }
```

### 3. State Download

[Section titled “3. State Download”](#3-state-download)

The node streams state entries in chunks:

```plaintext
StateChunkRequest { checkpoint_height: 5000, offset: 0, limit: 512 }
    -> StateChunkResponse { entries: [...], has_more: true }


StateChunkRequest { checkpoint_height: 5000, offset: 512, limit: 512 }
    -> StateChunkResponse { entries: [...], has_more: true }


... (continues until has_more == false)
```

### 4. Verification

[Section titled “4. Verification”](#4-verification)

After all entries are imported, the node recomputes the state root and verifies it matches the checkpoint. On success, the node transitions to normal operation and replays blocks from the checkpoint height to the current tip.

## Snapshot Verification

[Section titled “Snapshot Verification”](#snapshot-verification)

### Full Snapshot

[Section titled “Full Snapshot”](#full-snapshot)

`SnapshotManifest::verify()` checks:

| Check             | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| Version           | Snapshot format version must match current                  |
| Header chain      | Each header’s `parent_hash` matches the prior header’s hash |
| MMR root          | Recomputed root from entries matches `mmr_root`             |
| Entry count       | MMR entry count matches header count                        |
| Checkpoint height | Must equal the last header’s height                         |
| State root        | Checkpoint `state_root` matches header `state_root`         |

### Light Snapshot

[Section titled “Light Snapshot”](#light-snapshot)

`LightSnapshot::verify(trusted_root)` checks:

| Check      | Description                                         |
| ---------- | --------------------------------------------------- |
| Version    | Format version must match                           |
| Height     | Checkpoint height matches header height             |
| State root | Checkpoint `state_root` matches header `state_root` |
| MMR proof  | Proof verifies against the trusted MMR root         |
| Block hash | MMR proof entry hash matches header hash            |

### Trusted Root Verification

[Section titled “Trusted Root Verification”](#trusted-root-verification)

A snapshot can be verified against an externally obtained MMR root (e.g., from a light client or a known good peer):

```plaintext
verify_against_trusted_root(manifest, trusted_root)
```

This runs the full structural verification plus confirms the manifest’s MMR root matches the trusted value.

## RPC Endpoints

[Section titled “RPC Endpoints”](#rpc-endpoints)

### Checkpoint Management

[Section titled “Checkpoint Management”](#checkpoint-management)

| Method                    | Description                                             |
| ------------------------- | ------------------------------------------------------- |
| `get_checkpoint_list`     | List checkpoint heights and state roots                 |
| `get_checkpoint(height)`  | Get checkpoint descriptor with optional archive info    |
| `list_checkpoints(limit)` | List checkpoints with archive descriptors, newest first |

### Snapshot & State Sync

[Section titled “Snapshot & State Sync”](#snapshot--state-sync)

| Method                                                         | Description                                 |
| -------------------------------------------------------------- | ------------------------------------------- |
| `get_light_snapshot(height)`                                   | Get minimal verified snapshot for fast sync |
| `get_snapshot_chunk(height, offset, limit)`                    | Stream state entries for a checkpoint       |
| `import_snapshot_chunk(height, state_root, entries, finalize)` | Admin: import state entries for bootstrap   |

### Related Endpoints

[Section titled “Related Endpoints”](#related-endpoints)

| Method                            | Description                                |
| --------------------------------- | ------------------------------------------ |
| `status`                          | Includes `latest_checkpoint` in response   |
| `finalized_history_root`          | Current MMR root for snapshot verification |
| `finalized_history_proof(height)` | MMR membership proof for a finalized block |
| `finality_proof(height)`          | BLS threshold certificate for a block      |

## CLI Operations

[Section titled “CLI Operations”](#cli-operations)

### Export a Snapshot

[Section titled “Export a Snapshot”](#export-a-snapshot)

```bash
ashen backup export --height 5000 --output snapshot.bin
```

### Import a Snapshot

[Section titled “Import a Snapshot”](#import-a-snapshot)

```bash
ashen backup import --input snapshot.bin
```

### Verify a Checkpoint

[Section titled “Verify a Checkpoint”](#verify-a-checkpoint)

```bash
# Verify a block is in the finalized history
ashen node verify --height 5000


# Verify against a specific RPC endpoint
ashen node verify --height 5000 --rpc-url http://localhost:3030
```

## Operational Considerations

[Section titled “Operational Considerations”](#operational-considerations)

### Disk Usage

[Section titled “Disk Usage”](#disk-usage)

Checkpoints are stored under `data/checkpoints/` and typically consume 10-50 MB each. See [Disk Growth](/operations/disk-growth/) for sizing guidance.

### Archive vs Pruning Mode

[Section titled “Archive vs Pruning Mode”](#archive-vs-pruning-mode)

* **Archive mode** (`max_retained_heights: None`): retains all historical state. Useful for RPC nodes serving historical queries.
* **Pruning mode** (`max_retained_heights: N`): retains only the most recent N heights of state. Reduces disk usage but limits which checkpoints can serve state sync requests.

### Monitoring

[Section titled “Monitoring”](#monitoring)

The `status` RPC endpoint includes `latest_checkpoint` with height and state root. Monitor this to confirm checkpoints are being created at the expected interval.

```promql
# Track checkpoint creation
ashen_latest_checkpoint_height
```

## Related

[Section titled “Related”](#related)

* [Disk Growth](/operations/disk-growth/) - Storage sizing and checkpoint disk usage
* [Light Clients](/concepts/light-clients/) - MMR proofs and finality verification
* [Storage](/architecture/storage/) - State backend and Merkle tree structure
* [Running a Node](/guides/running-a-node/) - Node setup and checkpoint configuration
* [RPC API](/reference/rpc-api/) - Full endpoint reference

# Product Overview

> Product thesis, pricing model, and distribution strategy

This document describes the product thesis, pricing model, and distribution plan for Ashen.

**Status**: Testnet ready (core protocol and VM built). Product surfaces and pricing are the focus.

***

## Product Definition

[Section titled “Product Definition”](#product-definition)

We are building a deterministic, agent-first blockchain that prices fresh reads and pays validators for the work they already do.

## Why the name

[Section titled “Why the name”](#why-the-name)

**Ashen** implies post-legacy infrastructure: hardened, quiet, and built to outlast cycles. It is intentionally austere and engineered for verifiability over spectacle.

`ashen.sh` is the shell-first entrypoint for docs, CLI, and agent tooling.

**What we sell:**

* Metered read access (compute, bytes, egress, and optional priority)
* Deterministic execution (no contract-visible nondeterminism)
* Verified data (state proofs for high-value reads)

**What we are not:**

* A generic “free reads” RPC business
* A free data feed for non-validating explorers/indexers that monetize with ads

***

## Who We Serve

[Section titled “Who We Serve”](#who-we-serve)

* **Builders** who need reliable reads, simulations, and proofs without RPC lock-in.
* **Agents and bots** that require predictable pricing and low-latency verification.
* **Validators** who should be paid for read infrastructure, not just writes.
* **End users** who want verified, fresh data in wallets and explorers.

***

## Core Thesis

[Section titled “Core Thesis”](#core-thesis)

**Validators subsidize read-heavy businesses while capturing only write fees.**

Wallets, trading apps, explorers, and RPC providers extract value from validator-produced data without compensation. Many explorers do not validate; they resell data and monetize via ads. Gas prices writes; reads are free. The result is structural underinvestment in chain infrastructure.

Explorer data rent is a direct symptom. When a surface does not validate, it captures value without paying for correctness. Proof-backed reads and a verified explorer make provenance visible and route revenue to validators.

**Our proposal: protocol-native pricing for fresh reads, metered by actual resource usage.**

Revenue follows usage. Infrastructure becomes sustainable.

***

## How Paid Reads Work

[Section titled “How Paid Reads Work”](#how-paid-reads-work)

1. Client requests a read (balance, simulation, proof, and so on)
2. The node meters compute + bytes + egress
3. Payment is settled (x402 + stablecoin) or sponsored
4. Revenue flows to the serving validator
5. QoS routing rewards lower latency and higher reliability

Freshness is the product. Stale cache can be free; current data is paid.

***

## Paid Read Types (Cache-Resistant)

[Section titled “Paid Read Types (Cache-Resistant)”](#paid-read-types-cache-resistant)

These reads are hard to resell because they are time-sensitive or state-specific:

| Read type                | Demand driver                  | Cache resistance                    |
| ------------------------ | ------------------------------ | ----------------------------------- |
| Tx simulation            | Pre-trade or pre-deploy safety | Depends on caller state and mempool |
| State proofs             | Trustless verification         | Must be current to be useful        |
| Account nonces           | Transaction construction       | Changes with each write             |
| Pending mempool views    | Execution ordering             | Updates each block                  |
| Block tips               | Time-sensitive decisions       | Stale data loses value quickly      |
| State ranges with proofs | Audits and analytics           | Expensive to recompute and validate |

***

## Pricing Model

[Section titled “Pricing Model”](#pricing-model)

### Pricing Inputs

[Section titled “Pricing Inputs”](#pricing-inputs)

Every read request is priced by:

| Input          | Description            |
| -------------- | ---------------------- |
| Compute units  | CPU cycles consumed    |
| Bytes read     | Storage bytes accessed |
| Bytes returned | Response payload size  |
| Priority tier  | Optional QoS bump      |

### Formula

[Section titled “Formula”](#formula)

```plaintext
price = (compute_units * unit_price_compute)
      + (bytes_read * unit_price_read)
      + (bytes_returned * unit_price_egress)
      + priority_fee
```

### Illustrative Pricing (not final)

[Section titled “Illustrative Pricing (not final)”](#illustrative-pricing-not-final)

| Endpoint       | Compute | Bytes | Price   |
| -------------- | ------- | ----- | ------- |
| Balance lookup | 50      | 200   | $0.0001 |
| Tx simulation  | 20,000  | 8 KB  | $0.01   |
| State proof    | 5,000   | 50 KB | $0.02   |

### Sensitivity Grid

[Section titled “Sensitivity Grid”](#sensitivity-grid)

Monthly revenue per 1M MAU:

| Price / 1k reads | 1k reads/MAU | 2.5k reads/MAU | 5k reads/MAU |
| ---------------- | ------------ | -------------- | ------------ |
| $0.05            | $50k         | $125k          | $250k        |
| $0.10            | $100k        | $250k          | $500k        |
| $0.25            | $250k        | $625k          | $1.25M       |

***

## Distribution Strategy

[Section titled “Distribution Strategy”](#distribution-strategy)

We bootstrap paid reads through first-party surfaces that can enforce pricing.

### First-Party Surfaces

[Section titled “First-Party Surfaces”](#first-party-surfaces)

| Surface        | Function                                              | Launch Criteria                               |
| -------------- | ----------------------------------------------------- | --------------------------------------------- |
| **Wallet**     | Default client, x402 billing, sponsor credits         | Majority of reads metered, one-click billing  |
| **SDKs**       | Agent-first read APIs, caching, payments              | 2-5 framework integrations                    |
| **Governance** | Fee policy visibility, validator payouts              | Fee tiers on-chain, payout splits transparent |
| **Explorer**   | Verified data, pricing visibility, per-endpoint costs | Proof-backed views + paid reads integrated    |

### Why Vertical?

[Section titled “Why Vertical?”](#why-vertical)

We are not asking incumbent wallets or RPC providers to change. We build the client stack ourselves:

1. **Wallet** sets paid-read defaults at the user level
2. **SDKs** make metered reads the path of least resistance for agents
3. **Governance** makes pricing transparent and voteable
4. **Explorer** anchors verified data and eliminates ad-funded data rent

***

## Validator Marketplace

[Section titled “Validator Marketplace”](#validator-marketplace)

### Validator Incentives

[Section titled “Validator Incentives”](#validator-incentives)

Validators earn from paid reads. They can improve revenue by lowering latency, keeping proofs fast, and advertising predictable pricing. QoS routing rewards those improvements with more paid traffic.

### Network Effects

[Section titled “Network Effects”](#network-effects)

```plaintext
More validators
      |
      v
Better QoS + price competition
      |
      v
More users
      |
      v
More revenue
      |
      v
More validators
```

### QoS Routing

[Section titled “QoS Routing”](#qos-routing)

Validators advertise paid endpoints with:

* Latency guarantees
* Uptime SLAs
* Price schedules

First-party clients route reads based on QoS + price. Public leaderboards drive competition.

***

## Agent-Native SDK

[Section titled “Agent-Native SDK”](#agent-native-sdk)

### Design Principles

[Section titled “Design Principles”](#design-principles)

Everything is agent-first:

| Principle | Implementation                             |
| --------- | ------------------------------------------ |
| Discovery | APIs designed for programmatic exploration |
| Payments  | x402 micropayments, no upfront commitment  |
| Metering  | Per-call pricing, no monthly minimums      |
| Caching   | SDK-managed, transparent to caller         |

### SDK Lock-in

[Section titled “SDK Lock-in”](#sdk-lock-in)

Goal: agents default to our SDK for reads, simulations, and payments.

| Feature            | Benefit                        |
| ------------------ | ------------------------------ |
| Metered reads      | Pay for what you use           |
| Cached simulations | Avoid redundant compute        |
| One-line payments  | No wallet integration overhead |

***

## Technical Differentiation

[Section titled “Technical Differentiation”](#technical-differentiation)

### Execution Model

[Section titled “Execution Model”](#execution-model)

* **Explicit call frames**: Call-stack enforcement reduces reentrancy risk
* **Deterministic VM**: No contract-visible nondeterminism (no FP, no timers)
* **Synchronous cross-contract calls**: Transactional substates with rollback

### Verified Data

[Section titled “Verified Data”](#verified-data)

* **State proofs** for high-value reads
* **Borsh encoding** for deterministic, schema-driven data

***

## Risk Mitigation

[Section titled “Risk Mitigation”](#risk-mitigation)

| Risk               | Mitigation                                                                      |
| ------------------ | ------------------------------------------------------------------------------- |
| **Elasticity**     | Start with high-value endpoints (simulation, proofs); subsidize commodity reads |
| **Adoption**       | Control wallet and client stack; price under RPC margins                        |
| **UX friction**    | Sponsor credits, prepaid bundles, SDK-managed billing                           |
| **Centralization** | QoS tiers, transparent pricing, governance parameters                           |

### Why Caching Does Not Kill the Model

[Section titled “Why Caching Does Not Kill the Model”](#why-caching-does-not-kill-the-model)

Objection: “What stops someone from caching reads and reselling them cheaper?”

Answer: The high-value reads listed above are time-sensitive and state-specific. Caching helps commodity reads like historical data, but it does not replace simulations, proofs, or real-time state. The premium flows to validators for the work that requires live infrastructure.

***

## 90-Day Launch Sequence (Tentative)

[Section titled “90-Day Launch Sequence (Tentative)”](#90-day-launch-sequence-tentative)

**Phase 1 (Weeks 1-4):** Ship SDK paid reads, simulation gateway, and validator pricing dashboard. Success metric: 10% of reads metered in first-party clients.

**Phase 2 (Weeks 5-8):** Launch verified-data explorer with proof-backed views and paid reads by default. Success metric: 25% of reads paid, median latency improves by 10%.

**Phase 3 (Weeks 9-12):** Enable governance fee knobs and publish SLA metrics on-chain. Success metric: 50+ validators offering paid tiers and stable pricing bands.

***

## Kill Criteria

[Section titled “Kill Criteria”](#kill-criteria)

Pause or pivot if any remain true after distribution phase:

| Metric                  | Threshold                             |
| ----------------------- | ------------------------------------- |
| Paid-read adoption      | < 25% of reads in first-party clients |
| QoS latency improvement | < 10% vs static routing               |
| Validator participation | < 25 active validators in paid tiers  |
| Revenue per 1M MAU      | < $5k/month at target prices          |

***

## Why Now

[Section titled “Why Now”](#why-now)

| Signal                  | Implication                                                             |
| ----------------------- | ----------------------------------------------------------------------- |
| **Audit inflation**     | Six-figure pools are normal; security costs price out smaller builders  |
| **LLM capability**      | Automated exploit discovery improving faster than manual audit capacity |
| **RPC rent extraction** | Multi-billion-dollar RPC businesses with zero protocol revenue share    |
| **Stack consolidation** | Core protocol built; can ship wallet and client rapidly                 |

# Block-STM Parallel Execution

> Parallel transaction execution via Block-STM, configuration, observability, and testing

**Source**: `src/core/execution/parallel.rs`, `src/storage/state/backend/mvcc.rs`

## Overview

[Section titled “Overview”](#overview)

Ashen supports **Block-STM parallel transaction execution**, an optimistic concurrency algorithm that speculatively executes transactions in parallel and validates their read sets afterwards. When two transactions conflict (one reads what the other wrote), the conflicting transaction is re-executed with updated data. If conflicts exceed a configurable retry budget, the engine falls back to sequential execution for the remaining transactions.

Block-STM is consensus-compatible: the final state root is identical whether transactions are executed sequentially or in parallel.

## Enable Block-STM

[Section titled “Enable Block-STM”](#enable-block-stm)

Block-STM is gated by a compile-time feature flag:

```bash
# Build with Block-STM support
cargo build --features block-stm


# Or combine with other features
cargo build --features std,tui,block-stm,vm-tiering
```

Without the `block-stm` feature, the parallel execution module is not compiled and the node uses `SimpleExecutionEngine` (sequential) exclusively.

## Configuration

[Section titled “Configuration”](#configuration)

The `ParallelExecutionConfig` struct controls Block-STM behavior:

| Field                   | Type    | Default | Description                                                                                                         |
| ----------------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------- |
| `min_parallel_tx_count` | `usize` | 2       | Minimum transactions in a block to use parallel execution. Blocks with fewer transactions use sequential execution. |
| `max_retries_per_tx`    | `u32`   | 5       | Maximum times a single transaction can be re-executed before triggering sequential fallback.                        |
| `max_total_aborts`      | `u32`   | 100     | Maximum total aborts across all transactions before the scheduler falls back entirely to sequential execution.      |

### Example

[Section titled “Example”](#example)

```rust
use ashen::core::execution::parallel::{ParallelExecutionConfig, ParallelExecutionEngine};


let config = ParallelExecutionConfig {
    min_parallel_tx_count: 4,   // Only parallelize blocks with 4+ txs
    max_retries_per_tx: 3,      // Tighter retry budget
    max_total_aborts: 50,       // Lower abort tolerance
};


let mut engine = ParallelExecutionEngine::new(backend, caps);
engine.set_config(config);
```

## How It Works

[Section titled “How It Works”](#how-it-works)

The parallel engine executes blocks in four phases:

### Phase 0: Setup

[Section titled “Phase 0: Setup”](#phase-0-setup)

1. **Batch signature verification** using ed25519 batch verify.
2. **MVCC store creation**: A shared multi-version store where all speculative writes are tracked, keyed by `(StorageLocation, TxIndex)`.
3. **Scheduler creation** with the configured retry budgets.
4. **Block gas limit check**: Validates aggregate gas before execution.

### Phase 1: Speculative Execution

[Section titled “Phase 1: Speculative Execution”](#phase-1-speculative-execution)

Each transaction executes against an `MvccStateBackend` that wraps the shared base state. Reads resolve through the MVCC layer (seeing writes from lower-indexed transactions), and writes are tagged with the transaction index.

Access tracking records every `get`/`put` at the `StateBackend` level, capturing balance, nonce, and contract storage accesses for later conflict detection.

### Phase 2: Validation Loop

[Section titled “Phase 2: Validation Loop”](#phase-2-validation-loop)

The scheduler walks transactions in block order, validating each transaction’s read set against the current MVCC state:

* **AllValidated**: Every transaction’s reads are consistent. Proceed to Phase 3.
* **ReExecute**: A read-write conflict was detected. The conflicting transaction’s MVCC entries are cleared and it is re-executed with fresh data.
* **FallbackToSequential**: The retry budget is exhausted. Validated transactions are materialized and remaining transactions execute sequentially.

### Phase 3: Materialize

[Section titled “Phase 3: Materialize”](#phase-3-materialize)

Validated writes are applied to the base state backend in block order, and state/outcome roots are computed and verified against the block header.

## Sequential Fallback

[Section titled “Sequential Fallback”](#sequential-fallback)

The engine falls back to sequential execution when:

1. **Block too small**: Fewer than `min_parallel_tx_count` transactions.
2. **Retry budget exhausted**: `max_retries_per_tx` or `max_total_aborts` exceeded.
3. **Validation loop divergence**: Safety limit reached without convergence (error).

Fallback is transparent: the final state root matches what sequential execution would have produced.

## Observability

[Section titled “Observability”](#observability)

Block-STM emits structured `tracing` events at key decision points:

| Level   | Event                                                          | Fields                                                            |
| ------- | -------------------------------------------------------------- | ----------------------------------------------------------------- |
| `INFO`  | `block-stm: apply_block complete`                              | `height`, `tx_count`, `re_execution_count`, `sequential_fallback` |
| `DEBUG` | `block-stm: re-executing transaction after validation failure` | `tx_index`, `re_execution_count`                                  |
| `WARN`  | `block-stm: falling back to sequential execution`              | `from_tx`, `tx_count`, `re_execution_count`                       |
| `ERROR` | `block-stm: validation loop did not converge`                  | `max_iterations`, `watermark`, `tx_count`, `re_execution_count`   |

Enable with standard `tracing` subscriber configuration:

```bash
RUST_LOG=ashen::core::execution::parallel=debug ./target/debug/node
```

## Testing

[Section titled “Testing”](#testing)

```bash
# Run parallel engine unit tests
cargo test -p ashen --features block-stm --lib -- parallel


# Run MVCC backend tests
cargo test -p ashen --features block-stm --lib -- backend::mvcc


# Run Block-STM scheduler and MVCC benchmarks (vm-runtime crate)
cargo bench -p vm-runtime --bench block_stm
```

## MVCC Storage

[Section titled “MVCC Storage”](#mvcc-storage)

The parallel engine uses multi-version concurrency control (MVCC) to track speculative writes. Each write is tagged with the transaction index, and reads resolve to the highest version below the reader’s index.

**Read outcomes**:

| Result                    | Meaning                                                                 |
| ------------------------- | ----------------------------------------------------------------------- |
| `Found(data, writer_idx)` | Value written by transaction `writer_idx`                               |
| `NotFound`                | Key was deleted by a preceding transaction                              |
| `FromBase`                | No MVCC version exists; read from pre-block state                       |
| `Blocked(blocker)`        | A preceding transaction has a pending write; fall through to base state |

## Current Limitations

[Section titled “Current Limitations”](#current-limitations)

* **Execution is MVCC-routed but sequential**: Phase 1 currently executes transactions one at a time through the MVCC layer. True thread-level parallelism (via `rayon` or `std::thread::scope`) is planned for a follow-up.
* **`build_block` is sequential**: The proposer builds blocks using `SimpleExecutionEngine`. Parallel `build_block` is a future optimization.
* **No background GC**: MVCC entries are not garbage-collected during execution. A background GC thread is planned (chain-1cmou).

# Configuration

> Complete node configuration reference

This guide covers all configuration options for Ashen nodes, including environment variables, CLI arguments, and genesis configuration.

## Quick Start

[Section titled “Quick Start”](#quick-start)

```bash
# Initialize a single node with funded account
node init --data-dir ./node-data --alloc "0xYOUR_ADDRESS=1000000000000"


# Run with defaults
node run --data-dir ./node-data


# Run with custom settings
NODE_BLOCK_TIME_MS=500 NODE_LISTEN=0.0.0.0:3030 node run
```

## Environment Variables

[Section titled “Environment Variables”](#environment-variables)

All CLI arguments can be set via environment variables. The variable name is the argument name in `SCREAMING_SNAKE_CASE` with `NODE_` prefix.

### Core Settings

[Section titled “Core Settings”](#core-settings)

| Variable             | Default          | Description                                  |
| -------------------- | ---------------- | -------------------------------------------- |
| `NODE_DATA_DIR`      | `./node-data`    | Directory for chain data, genesis, and state |
| `NODE_LISTEN`        | `127.0.0.1:3030` | RPC server listen address                    |
| `NODE_BLOCK_TIME_MS` | `1000`           | Target block time in milliseconds            |
| `NODE_PRODUCE_EMPTY` | `true`           | Produce blocks even when mempool is empty    |
| `NODE_AUTH_TOKEN`    | none             | Optional authentication token for RPC        |

### Logging

[Section titled “Logging”](#logging)

| Variable             | Default | Description                                    |
| -------------------- | ------- | ---------------------------------------------- |
| `NODE_LOG_FILE`      | stdout  | Path to log file (enables rotation when set)   |
| `NODE_LOG_ROTATION`  | `daily` | Rotation policy: `daily`, `hourly`, or `never` |
| `NODE_LOG_MAX_FILES` | `7`     | Maximum rotated log files to retain            |
| `NODE_LOG_PREFIX`    | `node`  | Log file prefix (e.g., `node.2026-01-22.log`)  |

### Rate Limiting

[Section titled “Rate Limiting”](#rate-limiting)

| Variable                        | Default    | Description                              |
| ------------------------------- | ---------- | ---------------------------------------- |
| `NODE_RATE_LIMIT_PER_S`         | `1000`     | RPC requests per second limit            |
| `NODE_RATE_LIMIT_BURST`         | `2000`     | RPC burst allowance                      |
| `NODE_NO_RATE_LIMIT`            | `false`    | Disable rate limiting (development only) |
| `NODE_UTILITY_RATE_LIMIT_PER_S` | `100`      | Rate limit for `/metrics` and `/health`  |
| `NODE_UTILITY_RATE_LIMIT_BURST` | `200`      | Burst for utility endpoints              |
| `NODE_MAX_BODY_BYTES`           | `20971520` | Maximum request body size (20 MB)        |

### State Management

[Section titled “State Management”](#state-management)

| Variable                   | Default        | Description                                         |
| -------------------------- | -------------- | --------------------------------------------------- |
| `NODE_ARCHIVE_MODE`        | `false`        | Preserve all historical state (no pruning)          |
| `NODE_PRUNE_KEEP_EPOCHS`   | `10`           | Epochs of state to retain (ignored in archive mode) |
| `NODE_CHECKPOINT_INTERVAL` | epoch boundary | Blocks between state checkpoints                    |

### Transaction Forwarding

[Section titled “Transaction Forwarding”](#transaction-forwarding)

| Variable              | Default | Description                                    |
| --------------------- | ------- | ---------------------------------------------- |
| `NODE_TX_FORWARD_URL` | none    | Forward `tx_submit` to this URL (gateway mode) |

***

## CLI Commands

[Section titled “CLI Commands”](#cli-commands)

### `node init`

[Section titled “node init”](#node-init)

Initialize a new node data directory with genesis configuration.

```bash
node init \
  --data-dir ./node-data \
  --alloc "0xADDRESS1=1000000000000" \
  --alloc "0xADDRESS2=500000000000" \
  --seed 42 \
  --seed-count 10 \
  --seed-balance 1000000000
```

| Option                    | Description                               |
| ------------------------- | ----------------------------------------- |
| `--data-dir`              | Directory to initialize                   |
| `--alloc ADDRESS=BALANCE` | Pre-fund accounts (repeatable)            |
| `--seed`                  | Seed for deterministic address generation |
| `--seed-count`            | Number of seeded accounts to create       |
| `--seed-balance`          | Balance for each seeded account           |

### `node run`

[Section titled “node run”](#node-run)

Run a node (single-node or validator mode).

```bash
# Single-node mode (development)
node run --data-dir ./node-data


# Validator mode (production)
node run \
  --data-dir ./node-data \
  --validator \
  --validator-network-key "keystore:my-validator" \
  --peers ./peers.yaml \
  --p2p-port 4040 \
  --bls-share "0x..." \
  --bls-polynomial "0x..."
```

### `node rpc`

[Section titled “node rpc”](#node-rpc)

Run RPC server only, sharing data directory with another node.

```bash
node rpc \
  --data-dir ./validator-data \
  --listen 127.0.0.1:3031 \
  --refresh-interval-s 1
```

Useful for offloading RPC traffic from validators.

### `node follower`

[Section titled “node follower”](#node-follower)

Run as P2P follower (non-validator), syncing via gossip.

```bash
node follower \
  --data-dir ./follower-data \
  --peers peers.yaml \
  --bootstrapper 0xPUBKEY... \
  --sync-batch-size 64 \
  --sync-poll-ms 500
```

| Option              | Default | Description                  |
| ------------------- | ------- | ---------------------------- |
| `--sync-batch-size` | `32`    | Headers per sync request     |
| `--sync-poll-ms`    | `1000`  | Poll interval when caught up |

***

## Consensus Configuration

[Section titled “Consensus Configuration”](#consensus-configuration)

### Timeouts

[Section titled “Timeouts”](#timeouts)

Control consensus timing behavior. Defaults scale with block time.

| Variable                       | Default            | Description                         |
| ------------------------------ | ------------------ | ----------------------------------- |
| `NODE_LEADER_TIMEOUT_MS`       | `2 × block_time`   | Wait for leader proposal            |
| `NODE_NOTARIZATION_TIMEOUT_MS` | `4 × block_time`   | Wait for notarization               |
| `NODE_NULLIFY_RETRY_MS`        | `1000`             | Retry interval for nullification    |
| `NODE_FETCH_TIMEOUT_MS`        | `10 × block_time`  | Timeout for block fetches           |
| `NODE_ACTIVITY_TIMEOUT`        | `10` (view deltas) | Activity timeout before view change |
| `NODE_SKIP_TIMEOUT`            | `5` (view deltas)  | When to skip to higher view         |

### DKG (Distributed Key Generation)

[Section titled “DKG (Distributed Key Generation)”](#dkg-distributed-key-generation)

Configure threshold BLS key generation for each epoch.

| Variable                       | Default | Description                      |
| ------------------------------ | ------- | -------------------------------- |
| `NODE_DKG_COMMIT_TIMEOUT_S`    | `30`    | Commitment phase timeout         |
| `NODE_DKG_SHARE_TIMEOUT_S`     | `30`    | Share distribution timeout       |
| `NODE_DKG_COMPLAINT_TIMEOUT_S` | `30`    | Complaint/justification timeout  |
| `NODE_DKG_FINALIZE_TIMEOUT_S`  | `30`    | Finalization timeout             |
| `NODE_DKG_LEAD_BLOCKS`         | `10`    | Blocks before epoch to start DKG |
| `NODE_DKG_MAX_RETRIES`         | `3`     | Retry attempts for failed DKG    |
| `NODE_TLE_SHARE_TIMEOUT_MS`    | `500`   | TLE decryption share collection  |

### Epochs

[Section titled “Epochs”](#epochs)

Epochs control key rotation and validator set changes.

```plaintext
EPOCH_LENGTH = 16 blocks (hardcoded)
```

* New threshold BLS keys are generated via DKG at epoch boundaries
* State checkpoints default to epoch boundaries
* Pruning is configured in epochs

***

## P2P Configuration

[Section titled “P2P Configuration”](#p2p-configuration)

For multi-validator deployments.

| Variable                   | Default | Description                          |
| -------------------------- | ------- | ------------------------------------ |
| `NODE_P2P_PORT`            | `4040`  | P2P listen port (separate from RPC)  |
| `NODE_PEERS_FILE`          | none    | Path to `peers.yaml`                 |
| `NODE_BOOTSTRAPPERS`       | none    | Bootstrapper public keys (hex)       |
| `NODE_LOCAL_P2P`           | `false` | Skip external IP discovery (testing) |
| `NODE_P2P_MAILBOX_SIZE`    | `16384` | P2P message buffer size              |
| `NODE_P2P_MESSAGE_BACKLOG` | `16384` | Message backlog size                 |

### peers.yaml Format

[Section titled “peers.yaml Format”](#peersyaml-format)

```yaml
peers:
  - pubkey: "0x1234...abcd"
    address: "192.168.1.10:4040"
  - pubkey: "0x5678...efgh"
    address: "192.168.1.11:4040"
  - pubkey: "0x9abc...ijkl"
    address: "192.168.1.12:4040"
```

***

## Keystore Configuration

[Section titled “Keystore Configuration”](#keystore-configuration)

Ashen uses an encrypted keystore for validator keys.

| Variable                     | Description                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------- |
| `NODE_KEYSTORE_PATH`         | Keystore file location (default: `~/.local/share/ashen/keystore/keystore.json`) |
| `NODE_VALIDATOR_NETWORK_KEY` | Key reference: `keystore:<handle>` or `ks:<label>`                              |

### Key Formats

[Section titled “Key Formats”](#key-formats)

```bash
# Reference key by handle
--validator-network-key "keystore:my-validator-key"
--validator-network-key "ks:validator-1"


# Password input
--keystore-password-stdin     # Read from stdin
--keystore-password-file /path/to/password
```

### BLS Keys (Production)

[Section titled “BLS Keys (Production)”](#bls-keys-production)

For production validators with pre-distributed BLS shares:

```bash
--bls-share "0x..."        # Your BLS share (hex)
--bls-polynomial "0x..."   # Public commitment polynomial (hex)
```

### BLS Keys (Testnet)

[Section titled “BLS Keys (Testnet)”](#bls-keys-testnet)

For testing with deterministic keys:

```bash
--bls-seed 42              # Same seed across all validators
--validator-index 0        # Your index (0-based)
```

***

## Genesis Configuration

[Section titled “Genesis Configuration”](#genesis-configuration)

The `genesis.json` file defines the initial chain state.

```json
{
  "allocations": [
    {
      "address": "493615aa1e16a24f618d3ab6dd93a9250ca76e19996e46493a372c5994862e8c",
      "balance": 13370000000000
    },
    {
      "address": "deadbeef...",
      "balance": 1000000000000
    }
  ]
}
```

| Field                   | Description                           |
| ----------------------- | ------------------------------------- |
| `allocations`           | Initial account balances              |
| `allocations[].address` | Account address (hex, no `0x` prefix) |
| `allocations[].balance` | Initial balance in base units         |

***

## Example Configurations

[Section titled “Example Configurations”](#example-configurations)

### Local Development

[Section titled “Local Development”](#local-development)

```bash
# Single node, fast blocks, no rate limits
node run \
  --data-dir ./dev-data \
  --block-time-ms 500 \
  --no-rate-limit \
  --produce-empty-blocks
```

### Production Validator

[Section titled “Production Validator”](#production-validator)

```bash
node run \
  --data-dir /var/lib/ashen \
  --validator \
  --validator-network-key "keystore:prod-validator" \
  --peers /etc/ashen/peers.yaml \
  --p2p-port 4040 \
  --listen 127.0.0.1:3030 \
  --bls-share "$BLS_SHARE" \
  --bls-polynomial "$BLS_POLY" \
  --archive-mode \
  --log-file /var/log/ashen/ \
  --log-rotation daily \
  --log-max-files 30
```

### RPC Gateway

[Section titled “RPC Gateway”](#rpc-gateway)

```bash
# Offload RPC from validator
node rpc \
  --data-dir /var/lib/ashen \
  --listen 0.0.0.0:3030 \
  --rate-limit-per-s 5000 \
  --rate-limit-burst 10000 \
  --refresh-interval-s 1
```

### Archive Node (Follower)

[Section titled “Archive Node (Follower)”](#archive-node-follower)

```bash
node follower \
  --data-dir /var/lib/ashen-archive \
  --peers /etc/ashen/peers.yaml \
  --bootstrapper 0x... \
  --listen 0.0.0.0:3030 \
  --sync-batch-size 64
```

***

## Debugging

[Section titled “Debugging”](#debugging)

### Trace Output

[Section titled “Trace Output”](#trace-output)

Enable execution tracing for debugging:

```bash
ASHEN_TRACE_OUTPUT=1 node run --data-dir ./node-data
ASHEN_TRACE_OUTPUT_DIR=./traces node run --data-dir ./node-data
```

### Skip Preflight

[Section titled “Skip Preflight”](#skip-preflight)

Skip startup validation (testing only):

```bash
node run --skip-preflight --data-dir ./node-data
```

***

## Related

[Section titled “Related”](#related)

* [Feature Flags](/reference/feature-flags/) — Compile-time configuration
* [Gas Schedule](/reference/gas-schedule/) — Execution costs
* [RPC API](/reference/rpc-api/) — API endpoints

# DA Chunk Recovery & Block Reconstruction

> Recover full blocks from erasure-coded chunks via chunk gossip

## Overview

[Section titled “Overview”](#overview)

Chunk recovery lets nodes reconstruct a full block when they only have the block hash and a subset of erasure-coded chunks. This is distinct from light client data availability sampling (DAS):

* **DAS** samples chunks against the header’s `data_availability_root`.
* **Recovery** reconstructs the full `BlockEnvelope` using a chunk commitment announced by peers.

Chunk recovery is used when a node misses a block body, when a peer needs to rehydrate archived data, or when a validator wants to validate full execution payloads without trusting a single peer.

## Commitments (DAS vs Recovery)

[Section titled “Commitments (DAS vs Recovery)”](#commitments-das-vs-recovery)

Ashen uses two related commitments:

* **`data_availability_root`**: stored in the block header and computed from the **execution payload** during block construction.
* **Chunk recovery commitment**: computed from the **full block envelope** when the application actor erasure-encodes finalized blocks. This commitment is distributed via `ChunkAnnounce` messages and is used for reconstruction.

Do not assume these commitments are identical. DAS verifies payload availability; recovery verifies full block reconstruction.

## Data Model

[Section titled “Data Model”](#data-model)

* **`BlockChunk`**: a Reed-Solomon shard (`ReedSolomon<Blake3>`).
* **`CheckedBlockChunk`**: a shard that has passed commitment verification.
* **`BlockChunkBundle`**: `{ commitment, chunks }` produced by `BlockChunkProducer::encode_block`.
* **`CodingConfig`**: `minimum_shards` + `extra_shards` define total shards. Recovery needs at least `minimum_shards` verified chunks.

Chunks are encoded for transport using `encode_chunk` and decoded with `decode_chunk`, which enforces a `MAX_SHARD_SIZE` bound (64 MB).

## Chunk Gossip Messages

[Section titled “Chunk Gossip Messages”](#chunk-gossip-messages)

Network-level chunk gossip uses:

* `ChunkGossipMessage::Announce`: advertises commitment + available indices.
* `ChunkGossipMessage::Request`: asks for specific chunk indices.
* `ChunkGossipMessage::Response`: returns `(index, chunk_bytes)` tuples.

Internally, the application actor exposes a control channel:

* `ChunkGossipCommand::Announce { block_hash, response }`
* `ChunkGossipCommand::Chunk { block_hash, index, response }`

The application actor only serves chunks from its in-memory `pending_chunks` cache (LRU, `PENDING_CHUNKS_MAX_SIZE = 32`) populated on **finalized** blocks. Recovery will fail if the target block has been evicted and no peers can serve the data.

## Recovery Flow

[Section titled “Recovery Flow”](#recovery-flow)

The canonical path is `ChunkRecoveryHandle::recover_block`:

1. **Fetch announce**: request `ChunkAnnounce` for the block hash.
2. **Validate totals**: ensure `announce.total_chunks` matches `minimum_shards + extra_shards`.
3. **Fetch chunks**: request chunks by index (0..total\_chunks), skipping timeouts or invalid proofs.
4. **Verify each chunk**: decode bytes and call `BlockChunkVerifier::check_chunk`.
5. **Reconstruct**: once `minimum_shards` are verified, call `BlockChunkVerifier::decode_block` to rehydrate the block.

Recommended caller check:

* Compute the recovered block hash and ensure it matches the requested `block_hash`.

## Error Modes

[Section titled “Error Modes”](#error-modes)

Common failure cases:

* **Announce mismatch**: peer claims a different total shard count than your local `CodingConfig`.
* **Insufficient chunks**: fewer than `minimum_shards` verified shards were available.
* **Verification failures**: chunk proofs do not match the commitment.
* **Timeouts**: peers do not respond within the request timeout.

## Configuration Notes

[Section titled “Configuration Notes”](#configuration-notes)

* The dev/test default is **2-of-4 shards** (`minimum_shards=2`, `extra_shards=2`).
* Production target is **64-of-128 shards** (`minimum_shards=64`, `extra_shards=64`).
* Recovery requires local config to match the chunk producers. A mismatch guarantees `AnnounceMismatch` errors.

## Related

[Section titled “Related”](#related)

* `/concepts/data-availability/` for DAS background
* `/internals/flows/finalization/` for block finalization flow
* `src/data_availability.rs` for recovery logic (`ChunkRecoveryHandle`, `recover_block`)

# Error Domains

> E1xxx-E5xxx error code taxonomy

## Overview

[Section titled “Overview”](#overview)

Ashen groups errors into five numeric domains. The numeric codes are the canonical taxonomy used for logging/metrics and internal error serialization. JSON-RPC uses string error codes that map 1:1 to the E5xxx network domain.

* `code`: numeric error code (e.g., 1001)
* `name`: stable, machine-readable identifier
* `message`: human-readable description

Domains:

* **E1xxx**: Consensus/DKG
* **E2xxx**: VM/Execution
* **E3xxx**: Storage/State
* **E4xxx**: Transaction
* **E5xxx**: Network/RPC

## SDK & Client Guidance

[Section titled “SDK & Client Guidance”](#sdk--client-guidance)

* **Prefer `code`/`name` for programmatic handling.** `message` is for humans and may change over time.
* **JSON-RPC errors use string codes.** For example, `INVALID_PARAMS` maps to **E5003** (`INVALID_PARAMS`) in the E5xxx table below.
* **Execution errors surface in results, not JSON-RPC errors.** Methods like `tx_simulate`, `tx_receipt`, and `tx_build_simulate` return structured execution errors (caps, VM traps, or rejection reasons) in the response payload rather than the top-level RPC error.
* **Contract-defined errors are separate.** Contract `revert`/`panic` codes are app-specific `u32` values and are not part of E1xxx–E5xxx.

## E1xxx: Consensus/DKG Errors

[Section titled “E1xxx: Consensus/DKG Errors”](#e1xxx-consensusdkg-errors)

| Code  | Name                                     | Description                                            |
| ----- | ---------------------------------------- | ------------------------------------------------------ |
| E1001 | INVALID\_SIGNATURE                       | Block signature verification failed                    |
| E1002 | HEIGHT\_MISMATCH                         | Block height does not match expected height            |
| E1003 | PARENT\_NOT\_FOUND                       | Parent block not found in chain                        |
| E1004 | INVALID\_TIMESTAMP                       | Block timestamp is invalid or in the future            |
| E1005 | UNAUTHORIZED\_PROPOSER                   | Block proposer is not authorized for this slot         |
| E1006 | DUPLICATE\_BLOCK                         | Block has already been received                        |
| E1007 | VALIDATION\_FAILED                       | Block validation failed                                |
| E1008 | INVALID\_FINALITY\_CERTIFICATE           | Finality certificate is invalid                        |
| E1009 | EPOCH\_MISMATCH                          | Block epoch does not match expected epoch              |
| E1010 | VIEW\_MISMATCH                           | Block view does not match expected view                |
| E1101 | DKG\_SHARE\_VERIFICATION\_FAILED         | DKG share verification failed                          |
| E1102 | DKG\_INVALID\_COMMITMENT                 | DKG commitment is invalid                              |
| E1103 | DKG\_THRESHOLD\_NOT\_MET                 | DKG threshold not met for key reconstruction           |
| E1104 | DKG\_PARTICIPANT\_NOT\_FOUND             | DKG participant not found                              |
| E1105 | DKG\_ALREADY\_COMPLETED                  | DKG has already completed for this epoch               |
| E1106 | DKG\_NOT\_STARTED                        | DKG has not started for this epoch                     |
| E1107 | DKG\_DECRYPTION\_FAILED                  | DKG share decryption failed                            |
| E1108 | DKG\_INVALID\_COMPLAINT                  | DKG complaint is invalid                               |
| E1109 | DKG\_INVALID\_JUSTIFICATION              | DKG justification is invalid                           |
| E1110 | DKG\_SHARE\_NOT\_FOUND                   | DKG share not found after key generation               |
| E1111 | DKG\_NETWORK\_TIMEOUT                    | DKG network timeout during protocol execution          |
| E1112 | DKG\_INVALID\_CONTRIBUTION               | DKG invalid contribution from peer                     |
| E1113 | DKG\_TOO\_MANY\_PARTICIPANTS             | DKG participant count exceeds maximum                  |
| E1114 | DKG\_INDEX\_OUT\_OF\_BOUNDS              | DKG internal index out of bounds                       |
| E1115 | DKG\_CONSECUTIVE\_FALLBACK               | DKG consecutive fallback (back-to-back epoch failures) |
| E1116 | DKG\_EMPTY\_PARTICIPANTS                 | DKG participant set is empty                           |
| E1117 | DKG\_FAILED                              | DKG failed for epoch                                   |
| E1201 | INSUFFICIENT\_VOTES                      | Insufficient votes for finality                        |
| E1202 | UNKNOWN\_VALIDATOR                       | Vote from unknown validator                            |
| E1203 | DUPLICATE\_VOTE                          | Duplicate vote from validator                          |
| E1204 | VOTE\_EPOCH\_MISMATCH                    | Vote is for wrong epoch                                |
| E1205 | VOTE\_SIGNATURE\_INVALID                 | Vote signature is invalid                              |
| E1301 | LC\_VALIDATOR\_SET\_ID\_MISMATCH         | Validator set ID mismatch in finality proof            |
| E1302 | LC\_INVALID\_MEMBERSHIP\_PROOF           | Invalid membership proof for aggregate key             |
| E1303 | LC\_TRANSITION\_COMMITMENT\_MISMATCH     | Validator set transition commitment mismatch           |
| E1304 | LC\_TRANSITION\_VERSION\_NOT\_INCREASED  | Validator set version did not increase                 |
| E1305 | LC\_TRANSITION\_NOT\_AT\_EPOCH\_BOUNDARY | Validator set transition not at epoch boundary         |
| E1306 | LC\_NO\_PENDING\_UPDATE                  | No pending validator set update                        |
| E1307 | LC\_DATA\_UNAVAILABLE                    | Data unavailability detected (DAS verification failed) |
| E1308 | LC\_DAS\_TIMEOUT                         | Data availability verification timed out               |
| E1401 | KEY\_ROTATION\_ALREADY\_PENDING          | Key rotation already pending for validator             |

## E2xxx: VM/Execution Errors

[Section titled “E2xxx: VM/Execution Errors”](#e2xxx-vmexecution-errors)

| Code  | Name                          | Description                                |
| ----- | ----------------------------- | ------------------------------------------ |
| E2001 | OUT\_OF\_GAS                  | Execution ran out of gas                   |
| E2002 | INVALID\_OPCODE               | Invalid opcode encountered                 |
| E2003 | STACK\_OVERFLOW               | Stack overflow                             |
| E2004 | STACK\_UNDERFLOW              | Stack underflow                            |
| E2005 | MEMORY\_OUT\_OF\_BOUNDS       | Memory access out of bounds                |
| E2006 | DIVISION\_BY\_ZERO            | Division by zero                           |
| E2007 | INTEGER\_OVERFLOW             | Integer overflow                           |
| E2008 | INVALID\_MEMORY\_ACCESS       | Invalid memory access                      |
| E2009 | TRAP                          | Execution trap                             |
| E2010 | INVALID\_CALL\_TARGET         | Invalid call target address                |
| E2011 | CSR\_FORBIDDEN                | CSR instruction is forbidden               |
| E2012 | BUFFER\_TOO\_SMALL            | Buffer too small for operation             |
| E2013 | INVALID\_GAS\_SCHEDULE        | Invalid gas schedule specified             |
| E2101 | CONTRACT\_NOT\_FOUND          | Contract not found at address              |
| E2102 | INVALID\_CONTRACT\_CODE       | Contract code is invalid                   |
| E2103 | DEPLOYMENT\_FAILED            | Contract deployment failed                 |
| E2104 | REVERT                        | Contract execution reverted                |
| E2105 | PANIC                         | Contract panicked                          |
| E2106 | INVALID\_ABI\_VERSION         | Invalid ABI version                        |
| E2107 | UNKNOWN\_SELECTOR             | Unknown function selector                  |
| E2108 | INVALID\_CALLDATA             | Invalid calldata format                    |
| E2109 | CONTRACT\_ALREADY\_EXISTS     | Contract already exists at address         |
| E2201 | HEAP\_CAP\_PER\_FRAME         | Heap memory cap exceeded for frame         |
| E2202 | STACK\_CAP\_PER\_FRAME        | Stack memory cap exceeded for frame        |
| E2203 | HEAP\_CAP\_PER\_TX            | Heap memory cap exceeded for transaction   |
| E2204 | JOURNAL\_CAP                  | Journal entries cap exceeded               |
| E2205 | STORAGE\_WRITES\_CAP          | Storage writes cap exceeded                |
| E2206 | LOG\_CAP\_PER\_TX             | Log bytes cap exceeded for transaction     |
| E2207 | PRECOMPILE\_CAP               | Precompile input cap exceeded              |
| E2208 | CALL\_DEPTH\_CAP              | Call depth cap exceeded                    |
| E2209 | LOG\_CAP\_PER\_BLOCK          | Log bytes cap exceeded for block           |
| E2210 | PRECOMPILE\_CAP\_PER\_BLOCK   | Precompile input cap exceeded for block    |
| E2211 | INPUT\_TOO\_LARGE             | Input data too large                       |
| E2212 | STORAGE\_BYTES\_CAP           | Storage bytes cap exceeded for transaction |
| E2301 | REENTRANCY                    | Reentrancy detected                        |
| E2302 | STATIC\_CALL\_WRITE           | Static call attempted to modify state      |
| E2303 | CROSS\_CONTRACT\_CALL\_FAILED | Cross-contract call failed                 |
| E2304 | INVALID\_RETURN\_DATA         | Invalid return data from call              |
| E2401 | HOST\_ERROR                   | Host error during syscall execution        |
| E2402 | CONTEXT\_DECODE\_FAILED       | Failed to decode execution context         |

## E3xxx: Storage/State Errors

[Section titled “E3xxx: Storage/State Errors”](#e3xxx-storagestate-errors)

| Code  | Name                               | Description                                       |
| ----- | ---------------------------------- | ------------------------------------------------- |
| E3001 | KEY\_NOT\_FOUND                    | Key not found in storage                          |
| E3002 | INVALID\_KEY\_FORMAT               | Invalid key format                                |
| E3003 | KEY\_TOO\_LARGE                    | Key exceeds maximum size                          |
| E3004 | TYPED\_DECODE\_FAILED              | Typed state decode failed (borsh deserialization) |
| E3005 | DATA\_CORRUPTED                    | Storage data corrupted on read                    |
| E3050 | VALUE\_TOO\_LARGE                  | Value exceeds maximum size                        |
| E3051 | QUOTA\_EXCEEDED                    | Storage quota exceeded                            |
| E3052 | TYPED\_ENCODE\_FAILED              | Typed state encode failed (borsh serialization)   |
| E3053 | METADATA\_OVERRIDE\_NOT\_ALLOWED   | Metadata override not allowed for table           |
| E3101 | MERKLE\_PROOF\_ERROR               | Merkle proof error                                |
| E3102 | INVALID\_PROOF                     | State proof is invalid                            |
| E3103 | PROOF\_VERIFICATION\_FAILED        | State proof verification failed                   |
| E3104 | MISSING\_PROOF\_NODE               | Missing node in proof                             |
| E3105 | INVALID\_STATE\_ROOT               | State root is invalid                             |
| E3106 | INVALID\_NON\_MEMBERSHIP\_ORDERING | Invalid non-membership proof ordering             |
| E3107 | INVALID\_EMPTY\_ROOT               | Expected empty tree for non-membership proof      |
| E3108 | UNEXPECTED\_SLOT\_PROOF            | Unexpected slot proof for absent contract         |
| E3109 | INVALID\_QMDB\_OPS                 | Invalid QMDB operations                           |
| E3110 | MISSING\_QMDB\_OP                  | Missing QMDB operation for contract               |
| E3111 | INVALID\_QMDB\_ORDERING            | Invalid QMDB ordering                             |
| E3112 | INVALID\_QMDB\_LAST\_LOC           | Invalid QMDB last\_loc                            |
| E3113 | INVALID\_LEAF\_DIGEST              | Leaf digest mismatch in proof                     |
| E3114 | UNSUPPORTED\_PROOF                 | Unsupported proof request                         |
| E3115 | LEAF\_POSITION\_OVERFLOW           | Leaf position overflow in BMT                     |
| E3201 | BACKEND\_UNAVAILABLE               | Storage backend unavailable                       |
| E3202 | WRITE\_FAILED                      | Storage write failed                              |
| E3203 | READ\_FAILED                       | Storage read failed                               |
| E3204 | SNAPSHOT\_NOT\_SUPPORTED           | Storage backend does not support snapshots        |
| E3205 | COMMIT\_FAILED                     | Storage commit failed                             |
| E3206 | ROLLBACK\_FAILED                   | Storage rollback failed                           |
| E3207 | SERIALIZATION\_FAILED              | Serialization error during storage operation      |
| E3301 | UNDECLARED\_ACCESS                 | Accessed state key not in access list             |
| E3302 | READ\_ONLY\_WRITE                  | Attempted write to read-only storage              |
| E3401 | MMR\_POSITION\_OUT\_OF\_BOUNDS     | MMR leaf position out of bounds                   |
| E3402 | MMR\_EMPTY                         | MMR is empty                                      |
| E3403 | MMR\_HEIGHT\_NOT\_FOUND            | Height not found in MMR                           |
| E3501 | SNAPSHOT\_UNSUPPORTED\_VERSION     | Snapshot version not supported                    |
| E3502 | SNAPSHOT\_EMPTY                    | Empty snapshot: no headers included               |
| E3503 | SNAPSHOT\_BROKEN\_CHAIN            | Header chain broken in snapshot                   |
| E3504 | SNAPSHOT\_MMR\_ROOT\_MISMATCH      | MMR root mismatch in snapshot                     |
| E3505 | SNAPSHOT\_STATE\_ROOT\_MISMATCH    | State root mismatch in snapshot                   |
| E3506 | SNAPSHOT\_FINALITY\_FAILED         | Finality proof verification failed in snapshot    |
| E3507 | SNAPSHOT\_MISSING\_VALIDATOR\_SET  | Missing validator set for epoch in snapshot       |
| E3508 | SNAPSHOT\_CHECKPOINT\_MISMATCH     | Checkpoint height mismatch in snapshot            |
| E3509 | SNAPSHOT\_MMR\_COUNT\_MISMATCH     | MMR entry count mismatch in snapshot              |
| E3510 | SNAPSHOT\_SERIALIZATION\_FAILED    | Snapshot serialization error                      |
| E3511 | SNAPSHOT\_STORAGE\_FAILED          | Snapshot storage error                            |

## E4xxx: Transaction Errors

[Section titled “E4xxx: Transaction Errors”](#e4xxx-transaction-errors)

| Code  | Name                                      | Description                                            |
| ----- | ----------------------------------------- | ------------------------------------------------------ |
| E4001 | INVALID\_SIGNATURE                        | Transaction signature is invalid                       |
| E4002 | INVALID\_NONCE                            | Transaction nonce is invalid                           |
| E4003 | INSUFFICIENT\_BALANCE                     | Insufficient balance to pay fees                       |
| E4004 | GAS\_LIMIT\_TOO\_LOW                      | Gas limit is too low                                   |
| E4005 | GAS\_LIMIT\_TOO\_HIGH                     | Gas limit exceeds maximum                              |
| E4006 | INVALID\_FEE\_ASSET                       | Fee asset is not supported                             |
| E4007 | MAX\_FEE\_TOO\_LOW                        | Max fee is too low for transaction                     |
| E4008 | INVALID\_ACCESS\_LIST                     | Access list is invalid                                 |
| E4009 | SYSTEM\_ADDRESS\_NOT\_ALLOWED             | System addresses not allowed in transactions           |
| E4010 | PAYER\_MISMATCH                           | Payer does not match authorizer                        |
| E4101 | INVALID\_DEPLOY\_NONCE\_SPACE             | Invalid nonce space for deploy                         |
| E4102 | INVALID\_DEPLOY\_ADDRESS                  | Invalid deploy address derivation                      |
| E4103 | DEPLOY\_CODE\_TOO\_LARGE                  | Deploy code exceeds size limit                         |
| E4104 | INVALID\_DEPLOY\_MANIFEST                 | Deploy manifest is invalid                             |
| E4201 | KEY\_ROTATION\_EPOCH\_TOO\_SOON           | Key rotation effective epoch is too soon               |
| E4202 | KEY\_ROTATION\_NOT\_VALIDATOR             | Key rotation sender is not a validator                 |
| E4203 | KEY\_ROTATION\_ALREADY\_PENDING           | Key rotation already pending for validator             |
| E4204 | KEY\_ROTATION\_MALFORMED                  | Key rotation call\_data is malformed                   |
| E4301 | POOL\_FULL                                | Transaction pool is full                               |
| E4302 | DUPLICATE\_TRANSACTION                    | Transaction already in pool                            |
| E4303 | TRANSACTION\_EXPIRED                      | Transaction has expired                                |
| E4304 | REPLACEMENT\_FEE\_TOO\_LOW                | Replacement transaction fee is too low                 |
| E4305 | TOO\_MANY\_LANES                          | Too many nonce lanes for sender                        |
| E4306 | TRANSACTION\_TOO\_LARGE                   | Transaction exceeds maximum size                       |
| E4307 | GAS\_RATE\_LIMITED                        | Transaction rejected due to gas-weighted rate limiting |
| E4401 | SEAL\_ENCRYPTION\_FAILED                  | Sealed transaction encryption failed                   |
| E4402 | SEAL\_DECRYPTION\_FAILED                  | Sealed transaction decryption failed                   |
| E4403 | SEAL\_INVALID\_CIPHERTEXT                 | Sealed transaction ciphertext is invalid               |
| E4404 | SEAL\_EPOCH\_MISMATCH                     | Sealed transaction epoch mismatch                      |
| E4405 | SEAL\_DESERIALIZATION\_FAILED             | Sealed transaction deserialization failed              |
| E4406 | TLE\_INSUFFICIENT\_SIGNATURES             | Insufficient threshold signatures for TLE              |
| E4407 | TLE\_INVALID\_PARTIAL\_SIGNATURE          | Invalid partial signature for TLE                      |
| E4408 | TLE\_SIGNATURE\_RECOVERY\_FAILED          | TLE signature recovery failed                          |
| E4501 | ORDERING\_UNKNOWN\_COMMITMENT             | Unknown sealed transaction commitment                  |
| E4502 | ORDERING\_OUT\_OF\_ORDER                  | Sealed transactions out of FIFO order                  |
| E4503 | ORDERING\_DUPLICATE\_COMMITMENT           | Duplicate sealed transaction commitment                |
| E4601 | CALL\_DATA\_TRUNCATED                     | Call data is truncated                                 |
| E4602 | CALL\_DATA\_UNKNOWN\_VERSION              | Unknown call data version byte                         |
| E4603 | CALL\_DATA\_UNKNOWN\_KIND                 | Unknown call data kind                                 |
| E4604 | CALL\_DATA\_MANIFEST\_OVERFLOW            | Manifest length overflow in call data                  |
| E4605 | CALL\_DATA\_MANIFEST\_OUT\_OF\_BOUNDS     | Manifest extends past end of call data                 |
| E4606 | CALL\_DATA\_IDL\_OVERFLOW                 | IDL length overflow in call data                       |
| E4607 | CALL\_DATA\_IDL\_OUT\_OF\_BOUNDS          | IDL extends past end of call data                      |
| E4608 | CALL\_DATA\_MISSING\_IDL                  | Deploy missing required IDL                            |
| E4609 | CALL\_DATA\_MISSING\_ELF                  | Deploy missing required ELF binary                     |
| E4701 | ACCESS\_LIST\_INVALID\_PREFIX             | Access list prefix is invalid                          |
| E4702 | ACCESS\_LIST\_INVALID\_RANGE              | Access list range bounds invalid or empty              |
| E4703 | ACCESS\_LIST\_TOO\_MANY\_ACCOUNTS         | Too many accounts in access list                       |
| E4704 | ACCESS\_LIST\_TOO\_MANY\_STORAGE\_ENTRIES | Too many storage entries in access list                |
| E4705 | ACCESS\_LIST\_TOO\_MANY\_DESCRIPTORS      | Too many descriptors per access list entry             |
| E4801 | SESSION\_KEY\_NOT\_FOUND                  | Session key not found for authorizer                   |
| E4802 | SESSION\_REVOKED                          | Session key has been revoked                           |
| E4803 | SESSION\_EXPIRED                          | Session key has expired                                |
| E4804 | SESSION\_BUDGET\_EXHAUSTED                | Session key budget is exhausted                        |
| E4805 | SESSION\_VALUE\_EXCEEDED                  | Transaction value exceeds session per-tx limit         |
| E4806 | SESSION\_BUDGET\_OVERFLOW                 | Transaction value exceeds remaining session budget     |
| E4807 | SESSION\_CONTRACT\_NOT\_ALLOWED           | Target contract not allowed by session key             |
| E4808 | SESSION\_SELECTOR\_NOT\_ALLOWED           | Function selector not allowed by session key           |

## E5xxx: Network/RPC Errors

[Section titled “E5xxx: Network/RPC Errors”](#e5xxx-networkrpc-errors)

| Code  | Name                       | Description                              |
| ----- | -------------------------- | ---------------------------------------- |
| E5001 | INVALID\_REQUEST           | RPC request is invalid                   |
| E5002 | METHOD\_NOT\_FOUND         | RPC method not found                     |
| E5003 | INVALID\_PARAMS            | RPC parameters are invalid               |
| E5004 | INTERNAL\_ERROR            | Internal server error                    |
| E5005 | RATE\_LIMITED              | Request rate limited                     |
| E5006 | REQUEST\_TOO\_LARGE        | Request exceeds size limit               |
| E5007 | SERVICE\_UNAVAILABLE       | Service is unavailable                   |
| E5008 | PARSE\_ERROR               | Failed to parse request (malformed JSON) |
| E5009 | REQUEST\_TIMEOUT           | Request timed out                        |
| E5010 | PAYMENT\_REQUIRED          | Payment required for this method         |
| E5011 | PAYMENT\_INVALID           | Payment verification failed              |
| E5012 | PAYMENT\_ERROR             | Payment processing error                 |
| E5013 | NOT\_FOUND                 | Resource not found                       |
| E5014 | UNAUTHORIZED               | Unauthorized access                      |
| E5101 | PEER\_NOT\_FOUND           | Peer not found                           |
| E5102 | CONNECTION\_FAILED         | Connection failed                        |
| E5103 | HANDSHAKE\_FAILED          | Handshake failed                         |
| E5104 | PROTOCOL\_MISMATCH         | Protocol version mismatch                |
| E5105 | MESSAGE\_TOO\_LARGE        | Message exceeds size limit               |
| E5106 | INVALID\_MESSAGE           | Message is invalid                       |
| E5107 | PEER\_BANNED               | Peer is banned                           |
| E5108 | MAX\_CONNECTIONS\_REACHED  | Maximum connections reached              |
| E5201 | GOSSIP\_VALIDATION\_FAILED | Gossip message validation failed         |
| E5202 | DUPLICATE\_GOSSIP\_MESSAGE | Duplicate gossip message                 |
| E5203 | UNKNOWN\_GOSSIP\_TOPIC     | Unknown gossip topic                     |

## Related

[Section titled “Related”](#related)

* `/reference/error-handling/` for client/SDK guidance
* `/reference/rpc-api/` for RPC error surfaces
* `src/core/error_domains.rs` for the canonical source

# Error Handling

> How to interpret RPC and execution errors

## JSON-RPC Errors

[Section titled “JSON-RPC Errors”](#json-rpc-errors)

JSON-RPC errors are returned in the top-level `error` field of the response. The `code` is a **string** (for example `INVALID_PARAMS`) and maps 1:1 to the E5xxx network error domain in the error table.

Example:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": "RATE_LIMITED",
    "message": "rate limited"
  }
}
```

Mapping guidance:

* `RATE_LIMITED` -> **E5005**
* `METHOD_NOT_FOUND` -> **E5002**
* `INVALID_PARAMS` -> **E5003**

See the full mapping in `/reference/error-domains/`.

## Execution Errors (In-Result)

[Section titled “Execution Errors (In-Result)”](#execution-errors-in-result)

Execution-related errors are returned inside successful JSON-RPC responses. Methods such as `tx_simulate`, `tx_receipt`, and `tx_build_simulate` include a structured `error` field in their result payloads rather than returning a top- level RPC error.

Typical shapes:

* **Cap errors**: resource caps exceeded (heap, journal, log bytes, etc.)
* **VM trap**: low-level VM status code
* **Rejected**: transaction-level validation failure

These map to the E2xxx and E4xxx domains respectively. Use the error domain reference to interpret the specific reason.

## Contract-Defined Errors

[Section titled “Contract-Defined Errors”](#contract-defined-errors)

Contracts can return custom `u32` error codes via the SDK (for example `ContractErrorV1::code(1)`). These are **app-specific** and are not part of the E1xxx–E5xxx taxonomy. SDKs should expose these raw codes to callers.

## SDK Best Practices

[Section titled “SDK Best Practices”](#sdk-best-practices)

* Treat `code` and `name` as stable identifiers.
* Use `message` only for human-readable display.
* Surface the raw error payload to allow forward-compatible handling.

# Feature Flags

> Compile-time feature flags and build profiles

This document describes the compile-time feature flags available in the chain codebase, their behaviors, and valid combinations.

## Feature Flag Matrix

[Section titled “Feature Flag Matrix”](#feature-flag-matrix)

| Flag          | Default | Purpose                                                            | Dependencies                                           | Incompatible With |
| ------------- | ------- | ------------------------------------------------------------------ | ------------------------------------------------------ | ----------------- |
| `std`         | **on**  | Enables prometheus metrics, QMDB state backend, persistent storage | `dep:prometheus-client`                                | (none)            |
| `tui`         | **on**  | Enables interactive terminal UI explorer                           | `ratatui`, `crossterm`, `directories`, `toml`, `flume` | (none)            |
| `vm-tiering`  | off     | Enables JIT/AOT execution tiers and persistent code cache          | `dep:vm-codecache`                                     | (none)            |
| `das`         | off     | Enables Data Availability Sampling for light clients               | (none)                                                 | (none)            |
| `block-stm`   | off     | Enables Block-STM parallel transaction execution                   | (none)                                                 | (none)            |
| `qmdb-shadow` | off     | Enables shadow writes to QMDB for testing/migration                | (none)                                                 | (none)            |

## Feature Behaviors

[Section titled “Feature Behaviors”](#feature-behaviors)

### `std` (default: on)

[Section titled “std (default: on)”](#std-default-on)

When enabled:

* Prometheus metrics are collected and exposed via `/metrics` endpoint
* QMDB state backend is available for persistent authenticated state
* Journal-backed storage backends are available

When disabled:

* In-memory state backend only
* No metrics collection
* Reduced binary size for embedded/wasm targets

### `tui` (default: on)

[Section titled “tui (default: on)”](#tui-default-on)

When enabled:

* Interactive terminal UI via `ashen` (launches TUI when no subcommand given)
* Block explorer, account viewer, transaction list
* Cost-aware query previews and filtering

When disabled:

* CLI-only operation via `ashen <command>` subcommands
* Smaller binary size

### `vm-tiering` (default: off)

[Section titled “vm-tiering (default: off)”](#vm-tiering-default-off)

When enabled:

* JIT tier: Basic-block predecode support with inline caches
* AOT tier: Eager predecode support when cached artifacts exist
* Tiered execution path with an in-memory code cache
* Pre-charge gas per basic block (faster than per-instruction)

When disabled:

* Interpreter-only execution (reference implementation)
* Per-instruction gas charging (authoritative for conformance)

**Note**: Interpreter is always available and serves as the semantic authority for VM conformance testing. The node does not currently wire automatic hot-code promotion or disk persistence.

### `block-stm` (default: off)

[Section titled “block-stm (default: off)”](#block-stm-default-off)

When enabled:

* `ParallelExecutionEngine` is available for `apply_block`
* Speculative parallel transaction execution via MVCC storage
* Automatic sequential fallback on conflict budget exhaustion
* Structured `tracing` events for observability (re-executions, fallbacks)

When disabled:

* Sequential-only execution via `SimpleExecutionEngine`
* No MVCC overhead

See [Block-STM Parallel Execution](/reference/block-stm/) for configuration and usage details.

### `das` (default: off)

[Section titled “das (default: off)”](#das-default-off)

When enabled:

* Light clients perform Data Availability Sampling before accepting blocks
* Reed-Solomon erasure coding verification
* `LightClientError::DataUnavailable` and `LightClientError::DasTimeout` errors exposed
* ChunkGossip P2P integration for sample fetching

When disabled:

* Light clients trust block availability from finality proofs alone
* Smaller binary, lower verification overhead for non-validator nodes

### `qmdb-shadow` (default: off)

[Section titled “qmdb-shadow (default: off)”](#qmdb-shadow-default-off)

When enabled:

* All state writes are shadowed to QMDB in addition to primary backend
* Useful for migration testing and correctness validation
* Additional I/O overhead

When disabled:

* Single state backend path

## Build Profiles

[Section titled “Build Profiles”](#build-profiles)

### Minimal (Interpreter-only)

[Section titled “Minimal (Interpreter-only)”](#minimal-interpreter-only)

Smallest binary, no optional features:

```bash
cargo build --no-default-features
```

**Capabilities**: Core consensus + execution with interpreter-only VM, in-memory state.

### Standard (Default)

[Section titled “Standard (Default)”](#standard-default)

Balanced build for development and light operation:

```bash
cargo build
# Equivalent to: cargo build --features std,tui
```

**Capabilities**: Full node with TUI, metrics, QMDB storage.

### Full Validator

[Section titled “Full Validator”](#full-validator)

All features for production validators:

```bash
cargo build --features std,tui,vm-tiering,block-stm,das
```

**Capabilities**: JIT/AOT execution tiers, parallel transaction execution, DAS verification, full observability.

### Light Client

[Section titled “Light Client”](#light-client)

Minimal for light client verification with DAS:

```bash
cargo build --no-default-features --features das
```

**Capabilities**: Light client verification with data availability sampling.

## Runtime Validation

[Section titled “Runtime Validation”](#runtime-validation)

The node binary validates feature flag combinations at startup. Incompatible configurations will produce clear error messages.

### Current Validations

[Section titled “Current Validations”](#current-validations)

1. **No incompatible flags**: All flags are currently compatible with each other.

2. **Feature-dependent functionality**: Some functionality is only available when its flag is enabled:

   * `vm-tiering`: Code cache statistics, tier promotion, AOT compilation
   * `das`: Light client DAS verification
   * `std`: QMDB state backend, metrics endpoints

### Planned Validations

[Section titled “Planned Validations”](#planned-validations)

Future versions may add startup checks for:

* Hardware requirements for `vm-tiering` (memory, CPU)
* Network requirements for `das` (sampling connectivity)

## Conditional Compilation Patterns

[Section titled “Conditional Compilation Patterns”](#conditional-compilation-patterns)

Feature flags are used throughout the codebase via `#[cfg(feature = "...")]`:

```rust
// Conditional import
#[cfg(feature = "vm-tiering")]
use vm_codecache::{CodeCache, EvictionConfig};


// Conditional field
struct ExecutionEngine {
    #[cfg(feature = "vm-tiering")]
    pub vm_cache: CodeCache,
}


// Conditional code path
#[cfg(feature = "das")]
{
    verify_availability(&chunks, &config).await?;
}
```

## Migration Guide

[Section titled “Migration Guide”](#migration-guide)

### Enabling VM Tiering

[Section titled “Enabling VM Tiering”](#enabling-vm-tiering)

1. Add `--features vm-tiering` to your build command
2. Set `ASHEN_VM_TIERING=1` at runtime to activate the tiered execution path
3. Expect an interpreter-first warmup; JIT/AOT are only used when cached artifacts exist
4. Monitor cache metrics via `/metrics` (see `code_cache_entries_by_tier`)

### Enabling DAS

[Section titled “Enabling DAS”](#enabling-das)

1. Add `--features das` to your build command
2. Ensure P2P connectivity for chunk sampling
3. Configure sampling parameters in node config
4. Light clients will now verify data availability before accepting blocks

## FAQ

[Section titled “FAQ”](#faq)

**Q: Do I need `vm-tiering` for production?**

A: Not required. The interpreter is fully functional and serves as the semantic authority. Enable `vm-tiering` for better throughput on compute-heavy workloads.

**Q: Can I run a validator without `das`?**

A: Yes. DAS is primarily for light clients. Validators receive full blocks via consensus and don’t need DAS for their own verification.

**Q: Why is `std` a default feature?**

A: Most deployments want metrics and persistent storage. Disable it only for embedded/wasm targets or minimal testing.

# Gas Schedule

> Opcode and syscall costs

## Overview

[Section titled “Overview”](#overview)

Ashen gas is denominated in **abstract cycles** and charged by the VM during execution. The canonical schedule lives in the repo at:

* `docs/gas-schedules/gas-v1.json` (machine-readable)
* `docs/gas-schedules/gas-v1.md` (human-readable)

This page summarizes the rules and how to read the schedule.

## Conventions

[Section titled “Conventions”](#conventions)

* For any `per_32b` component, compute `words32 = ceil(bytes / 32)` and charge `words32 * per_32b`.
* For `per_32b_input` / `per_32b_output`, apply the rule to input/output sizes independently.
* Syscalls (including precompiles) always charge a **dispatch base** plus a syscall-specific cost.

## High-Level Structure

[Section titled “High-Level Structure”](#high-level-structure)

The schedule is grouped into three tables:

1. **Opcode costs**: base cost for ALU, shifts, branches, mul/div.
2. **Memory/page costs**: warm/cold load/store costs, page penalties, and the predecode byte charge.
3. **Syscalls/precompiles**: storage, calls, hashing, signature verification, and chain context queries.

## Highlights

[Section titled “Highlights”](#highlights)

### Storage

[Section titled “Storage”](#storage)

* Cold storage reads are more expensive than warm reads.
* Writes are charged on written value size.
* Range scans charge on query bytes and returned data bytes.

### Calls

[Section titled “Calls”](#calls)

* `call` and `static_call` charge on calldata + return bytes.
* `create` charges on code bytes.

### Precompiles

[Section titled “Precompiles”](#precompiles)

* Hashing: `keccak256`, `sha2_256`, `blake3`
* Signature verification: `verify_sig`
* VRF verification: `verify_vrf_ed25519`

### Context

[Section titled “Context”](#context)

Low-cost syscalls for balance and block metadata: `gas_limit`, `balance_of`, `self_balance`, `block_hash`, `block_header`.

## Worked Example

[Section titled “Worked Example”](#worked-example)

**Storage write of 100 bytes**:

* `words32 = ceil(100 / 32) = 4`
* `storage_write = dispatch_base (30) + base (400) + 4 * per_32b (8)`
* Total = `30 + 400 + 32 = 462`

## Full Schedule

[Section titled “Full Schedule”](#full-schedule)

Refer to `docs/gas-schedules/gas-v1.md` for the complete table and `docs/gas-schedules/gas-v1.json` for the canonical machine-readable source.

# Gas Throughput Analysis

> Gas throughput estimates and configuration guidance

This document provides gas throughput estimates for the chain under various hardware configurations and execution modes.

## Current Gas Configuration

[Section titled “Current Gas Configuration”](#current-gas-configuration)

| Parameter                     | Default Value | Notes                        |
| ----------------------------- | ------------- | ---------------------------- |
| `target_gas_per_block`        | 15,000,000    | EIP-1559 target (50% of max) |
| `max_gas_per_block`           | 30,000,000    | Hard cap per block           |
| `min_base_fee`                | 1             | Floor for dynamic pricing    |
| `max_base_fee`                | 10,000,000    | Ceiling for dynamic pricing  |
| `base_fee_change_denominator` | 8             | EIP-1559 adjustment rate     |

Configuration defined in `src/core/mod.rs` via `GasPricingConfig`.

## Gas Schedule Summary (gas-v1)

[Section titled “Gas Schedule Summary (gas-v1)”](#gas-schedule-summary-gas-v1)

### Opcode Costs

[Section titled “Opcode Costs”](#opcode-costs)

| Category         | Gas | Examples                |
| ---------------- | --- | ----------------------- |
| ALU              | 1   | add, sub, xor, and, or  |
| Shift/Bitmanip   | 2   | sll, srl, sra, rotates  |
| Branch/Jump      | 2   | jal, jalr, conditionals |
| Multiply         | 5   | mul, mulh variants      |
| Divide/Remainder | 20  | div, rem variants       |

### Memory Costs

[Section titled “Memory Costs”](#memory-costs)

| Operation                | Gas | Notes               |
| ------------------------ | --- | ------------------- |
| Load warm stack/rodata   | 2   | Aligned access      |
| Load cold stack/rodata   | 6   | First touch         |
| Load warm heap/data      | 4   | Aligned access      |
| Load cold heap/data      | 10  | First touch         |
| Store warm stack         | 2   | -                   |
| Store warm heap/data     | 6   | -                   |
| Store cold heap/data     | 12  | First touch         |
| Page fault (first touch) | 50  | Per 4KB page        |
| Dirty page (first write) | 10  | Per page            |
| Predecode per byte       | 1   | Basic block parsing |

### Syscall Costs

[Section titled “Syscall Costs”](#syscall-costs)

| Syscall             | Base Gas | Per 32B            | Notes                  |
| ------------------- | -------- | ------------------ | ---------------------- |
| storage\_read\_warm | 200      | +4                 | Warm slot              |
| storage\_read\_cold | 600      | +8                 | Cold slot              |
| storage\_write      | 400      | +8                 | Any write              |
| call                | 500      | +4 in/out          | Cross-contract         |
| static\_call        | 400      | +4 in/out          | Read-only call         |
| emit\_log           | 150      | +4 data, +20/topic | Event emission         |
| keccak256           | 800      | +20                | Hash precompile        |
| sha2\_256           | 800      | +20                | Hash precompile        |
| blake3              | 400      | +10                | Hash precompile        |
| verify\_sig         | 6000     | +20                | Signature verification |
| create              | 2000     | +20                | Contract deployment    |

Full schedule in `docs/gas-schedules/gas-v1.json`.

## Hardware Reference Configuration

[Section titled “Hardware Reference Configuration”](#hardware-reference-configuration)

**Test Configuration:** 16 cores, 32GB RAM, 4TB NVMe SSD

This represents a mid-range validator/RPC node setup.

## Throughput Estimates

[Section titled “Throughput Estimates”](#throughput-estimates)

### Transaction Gas Profiles

[Section titled “Transaction Gas Profiles”](#transaction-gas-profiles)

| Transaction Type        | Typical Gas         | Notes                 |
| ----------------------- | ------------------- | --------------------- |
| Native transfer         | \~21,000            | Base tx cost          |
| ERC20 transfer          | \~50,000-65,000     | 2 storage writes      |
| AMM swap                | \~150,000-200,000   | Multiple reads/writes |
| Complex DeFi            | \~300,000-500,000   | Multiple calls        |
| Contract deploy (small) | \~500,000-1,000,000 | Code size dependent   |

### Throughput by Execution Mode

[Section titled “Throughput by Execution Mode”](#throughput-by-execution-mode)

| Mode                     | Max Gas/Block | Est. TPS | Bottleneck     |
| ------------------------ | ------------- | -------- | -------------- |
| **Sequential (current)** | 30M           | 200-300  | Single-core VM |
| **Block-STM (planned)**  | 100-150M      | 600-1000 | Conflict rate  |
| **Optimistic ceiling**   | 200M          | 1500+    | I/O, consensus |

### Detailed Analysis

[Section titled “Detailed Analysis”](#detailed-analysis)

#### Sequential Execution (Current)

[Section titled “Sequential Execution (Current)”](#sequential-execution-current)

* **CPU**: RISC-V interpreter runs \~30-50M gas/sec on single core
* **Storage**: Not bottlenecked; NVMe handles 500K+ IOPS
* **Memory**: 32GB sufficient for hot state cache
* **Consensus**: Simplex single-slot finality at 1s blocks is not limiting

**Recommendation**: Keep `max_gas_per_block` at 30M.

#### Parallel Execution (Block-STM, Planned)

[Section titled “Parallel Execution (Block-STM, Planned)”](#parallel-execution-block-stm-planned)

Block-STM enables optimistic parallel execution with conflict detection:

* **Effective parallelism**: 3-5x on typical DeFi workloads
* **Conflict-free workloads**: Up to 8-12x theoretical
* **High-conflict workloads**: Falls back to sequential

**Current status**: Execution is still sequential (`SimpleExecutionEngine` applies blocks in order). The prerequisites for Block-STM exist (access lists, per-transaction state journaling, deterministic rollback), but the parallel scheduler + MVCC validation loop is not implemented yet. The design lives in `docs/design/block-stm-parallel-execution.md` and is deferred until throughput constraints demand it.

**Recommendation**: After Block-STM implementation, increase to 100M gas/block.

#### Bottleneck Breakdown

[Section titled “Bottleneck Breakdown”](#bottleneck-breakdown)

| Resource                 | Capacity       | At 30M gas/block   | At 100M gas/block   |
| ------------------------ | -------------- | ------------------ | ------------------- |
| CPU (sequential)         | \~50M gas/sec  | 60% utilized       | Bottleneck          |
| CPU (parallel, 16 cores) | \~200M gas/sec | 15% utilized       | 50% utilized        |
| NVMe IOPS                | 500K/sec       | \~15% (75K writes) | \~50% (250K writes) |
| Memory bandwidth         | \~100GB/s      | <1%                | <5%                 |
| Network (consensus)      | 1 block/sec    | Not limiting       | Not limiting        |

### Storage Growth Projections

[Section titled “Storage Growth Projections”](#storage-growth-projections)

At sustained max throughput (30M gas/block):

| Metric                   | Value        | Notes                   |
| ------------------------ | ------------ | ----------------------- |
| Max storage writes/block | 75,000       | 30M / 400 gas per write |
| Write rate               | \~7.5 MB/sec | Assuming 100B avg value |
| Daily growth             | \~650 GB     | At 100% utilization     |
| 4TB SSD lifespan         | \~6 days     | Without pruning         |

**Note**: Real-world utilization is typically 10-30% of max, and state pruning/compaction is required for long-term operation.

## Testing Max Gas Configuration

[Section titled “Testing Max Gas Configuration”](#testing-max-gas-configuration)

To test different gas limits:

```bash
# Run devnet with custom gas config
ASHEN_MAX_GAS_PER_BLOCK=50000000 just devnet-small


# Monitor block gas usage
just rpc-call chain_getBlock '{"height": "latest"}' | jq '.gas_used'


# Stress test with batch transactions
cargo run --release -p ashen --bin ashen -- \
  batch execute --count 1000 --gas-limit 100000
```

### Metrics to Monitor

[Section titled “Metrics to Monitor”](#metrics-to-monitor)

1. **Block execution time**: Should stay under block time (1s)
2. **Gas utilization**: `gas_used / max_gas_per_block`
3. **State growth rate**: Monitor disk usage
4. **Mempool depth**: Indicates demand vs capacity

## Recommended Configuration by Use Case

[Section titled “Recommended Configuration by Use Case”](#recommended-configuration-by-use-case)

| Use Case                | max\_gas | target\_gas | Block Time | Notes                    |
| ----------------------- | -------- | ----------- | ---------- | ------------------------ |
| Testnet                 | 30M      | 15M         | 1s         | Default, conservative    |
| Production (sequential) | 30M      | 15M         | 1s         | Current implementation   |
| Production (Block-STM)  | 100M     | 50M         | 1s         | After parallel execution |
| High-throughput L2      | 150M     | 75M         | 500ms      | Requires tuning          |

## References

[Section titled “References”](#references)

* Gas schedule: `docs/gas-schedules/gas-v1.json`
* Gas pricing config: `src/core/mod.rs` (`GasPricingConfig`)
* VM gas metering: `crates/vm-gas/src/lib.rs`
* Execution engine: `src/core/execution/mod.rs`

# Keystore & Signatures

> Encrypted key management and signature schemes

The Ashen keystore provides secure, encrypted storage for ed25519 signing keys. All key material is encrypted at rest using XChaCha20-Poly1305 with a password-derived key (Argon2id). There is no plaintext metadata—the entire payload requires the password to access.

## Quick Start

[Section titled “Quick Start”](#quick-start)

```bash
# Initialize a new keystore
ashen keystore init


# Generate a new key
ashen keystore add --label my-validator


# List keys
ashen keystore list


# Export public address
ashen keystore export --label my-validator
```

***

## Security Architecture

[Section titled “Security Architecture”](#security-architecture)

### Signature Scheme: ed25519

[Section titled “Signature Scheme: ed25519”](#signature-scheme-ed25519)

Ashen uses **ed25519** for all transaction signatures and validator network keys.

| Property             | Value              |
| -------------------- | ------------------ |
| **Algorithm**        | Ed25519 (RFC 8032) |
| **Private Key Size** | 32 bytes           |
| **Public Key Size**  | 32 bytes           |
| **Signature Size**   | 64 bytes           |
| **Security Level**   | \~128 bits         |

ed25519 provides:

* **Fast signing and verification** — optimized for high-throughput transaction processing
* **Deterministic signatures** — same message + key always produces the same signature
* **No side-channel leaks** — constant-time operations prevent timing attacks
* **Small keys and signatures** — efficient for network transmission and storage

### Encryption at Rest: XChaCha20-Poly1305

[Section titled “Encryption at Rest: XChaCha20-Poly1305”](#encryption-at-rest-xchacha20-poly1305)

The keystore file is encrypted using **XChaCha20-Poly1305** (AEAD):

| Property       | Value               |
| -------------- | ------------------- |
| **Cipher**     | XChaCha20-Poly1305  |
| **Key Size**   | 256 bits            |
| **Nonce Size** | 192 bits (24 bytes) |
| **Auth Tag**   | 128 bits            |

Why XChaCha20-Poly1305:

* **Extended nonce** — 192-bit nonces allow safe random generation without collision risk
* **AEAD** — Authenticated Encryption with Associated Data prevents tampering
* **No weak keys** — Unlike AES, ChaCha20 has no weak key classes
* **Constant-time** — Immune to cache-timing attacks

### Password Protection: Argon2id

[Section titled “Password Protection: Argon2id”](#password-protection-argon2id)

Passwords are stretched into encryption keys using **Argon2id**, the winner of the Password Hashing Competition:

| Parameter       | Default Value          | Description                   |
| --------------- | ---------------------- | ----------------------------- |
| **Algorithm**   | Argon2id               | Hybrid of Argon2i and Argon2d |
| **Memory Cost** | 64 MB (`m_cost=65536`) | Memory required for hashing   |
| **Time Cost**   | 3 iterations           | Sequential hash iterations    |
| **Parallelism** | 2 threads              | Parallel computation lanes    |
| **Salt**        | 32 bytes (random)      | Per-keystore salt             |
| **Output**      | 32 bytes               | Derived encryption key        |

Why Argon2id:

* **Memory-hard** — Requires 64 MB of RAM, making GPU/ASIC attacks expensive
* **Side-channel resistant** — Argon2id hybrid mode resists timing attacks
* **Tunable** — Parameters scale with hardware improvements
* **Fresh salt** — Each keystore has a unique random salt

### Memory Safety: Zeroize

[Section titled “Memory Safety: Zeroize”](#memory-safety-zeroize)

All sensitive key material is automatically zeroed from memory when:

* The `UnlockedKeystore` is dropped
* Secret key bytes go out of scope
* The derived encryption key is released

```rust
// Internal implementation
#[derive(Clone, Zeroize, ZeroizeOnDrop)]
struct SecretBytes(Vec<u8>);


impl Drop for DerivedKey {
    fn drop(&mut self) {
        self.key.zeroize(); // Overwrite with zeros
    }
}
```

This prevents secrets from lingering in memory where they could be extracted via:

* Core dumps
* Memory scanners
* Cold boot attacks
* Swap file analysis

### File System Security

[Section titled “File System Security”](#file-system-security)

On Unix systems, keystore files are written with **mode 0600** (owner read/write only):

```bash
$ ls -la ~/.local/share/ashen/keystore/keystore.json
-rw------- 1 user user 1234 Jan 22 10:00 keystore.json
```

Additional file safety measures:

* **Atomic writes** — Changes are written to a temp file, then atomically renamed
* **File locking** — Exclusive locks prevent concurrent corruption
* **Parent directory creation** — Directories are created with safe defaults

***

## Keystore File Format

[Section titled “Keystore File Format”](#keystore-file-format)

The keystore is stored as JSON with the following structure:

```json
{
  "version": 1,
  "kdf": {
    "algorithm": "argon2id",
    "salt_b64": "<base64-encoded-32-byte-salt>",
    "m_cost": 65536,
    "t_cost": 3,
    "p_cost": 2
  },
  "nonce": "<base64-encoded-24-byte-nonce>",
  "ciphertext": "<base64-encoded-encrypted-payload>"
}
```

The encrypted payload contains:

```rust
struct KeystorePayload {
    version: u8,          // Payload version (currently 1)
    keys: Vec<StoredKey>, // All stored keys
}


struct StoredKey {
    handle: [u8; 16],     // Random key identifier
    key_type: KeyType,    // Ed25519 or BlsMinSig
    label: String,        // User-assigned label
    created_at: u64,      // Unix timestamp
    secret: Vec<u8>,      // Encrypted private key
    public_key: Vec<u8>,  // Derived public key
}
```

***

## Key Types

[Section titled “Key Types”](#key-types)

| Type        | Enum                 | Size     | Use Case                                    |
| ----------- | -------------------- | -------- | ------------------------------------------- |
| **ed25519** | `KeyType::Ed25519`   | 32 bytes | Transaction signing, validator network keys |
| **BLS**     | `KeyType::BlsMinSig` | 32 bytes | Threshold signatures (DKG shares)           |

### ed25519 Keys

[Section titled “ed25519 Keys”](#ed25519-keys)

Used for:

* **Transaction signatures** — All transactions are signed with ed25519
* **Validator network identity** — P2P authentication between validators
* **Account addresses** — Derived from the public key

### BLS Keys (Threshold)

[Section titled “BLS Keys (Threshold)”](#bls-keys-threshold)

BLS12-381 keys are used for threshold cryptography:

* **Threshold signatures** — 2f+1 validators sign blocks together
* **DKG shares** — Distributed Key Generation produces per-validator shares
* **Sealed transactions** — Threshold decryption for MEV protection

BLS keys are typically generated via DKG, not stored directly in the keystore.

***

## CLI Commands

[Section titled “CLI Commands”](#cli-commands)

### `ashen keystore init`

[Section titled “ashen keystore init”](#ashen-keystore-init)

Initialize a new keystore file.

```bash
ashen keystore init
ashen keystore init --path ~/.ashen/custom-keystore.json
```

You will be prompted for a password. The keystore file is created with no keys.

### `ashen keystore list`

[Section titled “ashen keystore list”](#ashen-keystore-list)

List all keys in the keystore.

```bash
ashen keystore list
```

Output:

```plaintext
Handle              Type      Label           Created              Public Key
────────────────────────────────────────────────────────────────────────────────
a1b2c3d4e5f6...    ed25519   my-validator    2026-01-22 10:00:00  0x493615aa...
f6e5d4c3b2a1...    ed25519   backup-key      2026-01-20 14:30:00  0xdeadbeef...
```

### `ashen keystore add`

[Section titled “ashen keystore add”](#ashen-keystore-add)

Generate a new random key.

```bash
# Generate ed25519 key
ashen keystore add --label my-key


# Specify key type
ashen keystore add --label my-key --type ed25519
```

### `ashen keystore import`

[Section titled “ashen keystore import”](#ashen-keystore-import)

Import an existing secret key.

```bash
# Import from hex
ashen keystore add --label imported --secret 0x<64-hex-chars>


# Import from file
ashen keystore add --label imported --secret @./secret.key
```

### `ashen keystore export`

[Section titled “ashen keystore export”](#ashen-keystore-export)

Export a key’s public address.

```bash
ashen keystore export --label my-key
# Output: 0x493615aa1e16a24f618d3ab6dd93a9250ca76e19996e46493a372c5994862e8c
```

### `ashen keystore remove`

[Section titled “ashen keystore remove”](#ashen-keystore-remove)

Remove a key from the keystore.

```bash
ashen keystore remove --label my-key
```

***

## Key References

[Section titled “Key References”](#key-references)

Keys can be referenced in CLI commands using several formats:

| Format                     | Example                 | Description                      |
| -------------------------- | ----------------------- | -------------------------------- |
| **Hex**                    | `0xabcd1234...`         | Raw 64-character hex private key |
| **Keystore label**         | `keystore:my-validator` | Reference by label               |
| **Keystore label (short)** | `ks:my-validator`       | Short form                       |
| **File path**              | `@./secret.key`         | Read from file                   |
| **Environment**            | `$ASHEN_PRIVATE_KEY`    | Environment variable             |

### Usage Examples

[Section titled “Usage Examples”](#usage-examples)

```bash
# Using hex directly (not recommended for production)
ashen call 0xCONTRACT transfer ... --key 0xabcd1234...


# Using keystore reference (recommended)
ashen call 0xCONTRACT transfer ... --key keystore:my-validator
ashen call 0xCONTRACT transfer ... --key ks:my-validator


# Using environment variable
export ASHEN_PRIVATE_KEY="keystore:my-validator"
ashen call 0xCONTRACT transfer ...


# Validator network key
node run --validator-network-key "keystore:validator-1"
```

***

## Password Management

[Section titled “Password Management”](#password-management)

### Password Input Methods

[Section titled “Password Input Methods”](#password-input-methods)

| Method                 | Flag                             | Security                   |
| ---------------------- | -------------------------------- | -------------------------- |
| **Interactive prompt** | (default)                        | Most secure                |
| **Stdin**              | `--keystore-password-stdin`      | Good for automation        |
| **File**               | `--keystore-password-file /path` | Moderate (secure the file) |

```bash
# Interactive (recommended)
ashen keystore list


# From stdin (for scripts)
echo "my-password" | ashen keystore list --keystore-password-stdin


# From file
ashen keystore list --keystore-password-file ~/.ashen/password
```

### Changing Passwords

[Section titled “Changing Passwords”](#changing-passwords)

```bash
ashen keystore change-password
```

This re-encrypts all keys with the new password. The old password is required.

***

## Security Best Practices

[Section titled “Security Best Practices”](#security-best-practices)

### DO

[Section titled “DO”](#do)

* **Use a strong password** — At least 16 characters, mixed case, numbers, symbols
* **Backup the keystore** — Store encrypted backups in multiple locations
* **Use keystore references** — Never put raw private keys in command lines or scripts
* **Restrict file permissions** — Ensure 0600 permissions on keystore files
* **Use separate keys** — Different keys for different purposes (validator, testing, etc.)

### DON’T

[Section titled “DON’T”](#dont)

* **Don’t commit secrets** — Never put keystore files or passwords in git
* **Don’t share passwords** — Each operator should have their own credentials
* **Don’t use weak passwords** — Short or dictionary passwords can be brute-forced
* **Don’t disable memory zeroization** — The `zeroize` crate is there for a reason
* **Don’t store passwords in environment** — Use stdin or file references instead

***

## Threat Model

[Section titled “Threat Model”](#threat-model)

The keystore protects against:

| Threat                       | Protection                                |
| ---------------------------- | ----------------------------------------- |
| **File theft**               | AES-256 equivalent encryption (XChaCha20) |
| **Password brute force**     | Argon2id with 64MB memory cost            |
| **Memory scanning**          | Automatic zeroization on drop             |
| **Unauthorized file access** | Unix 0600 permissions                     |
| **Ciphertext tampering**     | Poly1305 authentication tag               |
| **Timing attacks**           | Constant-time crypto operations           |
| **Nonce reuse**              | 192-bit random nonces                     |

The keystore does NOT protect against:

* **Compromised host** — If the machine is compromised while the keystore is unlocked
* **Weak passwords** — A weak password can still be brute-forced offline
* **Physical access** — Cold boot attacks while the keystore is in memory

***

## Programmatic Usage (Rust)

[Section titled “Programmatic Usage (Rust)”](#programmatic-usage-rust)

```rust
use keystore::{Keystore, KeyType};


// Open existing keystore
let ks = Keystore::new("~/.local/share/ashen/keystore/keystore.json");
let mut unlocked = ks.open("my-password")?;


// List keys
for key in unlocked.list() {
    println!("{}: {} ({})", key.label, key.handle, key.key_type);
}


// Add a new key
let handle = unlocked.add_key(KeyType::Ed25519, "new-key")?;


// Sign a message
let signature = unlocked.sign_ed25519(&handle, b"ashen", b"message")?;


// Save changes
unlocked.save()?;
```

***

## Default Paths

[Section titled “Default Paths”](#default-paths)

| Platform    | Keystore Location                                                      |
| ----------- | ---------------------------------------------------------------------- |
| **Linux**   | `~/.local/share/ashen/keystore/keystore.json`                          |
| **macOS**   | `~/Library/Application Support/xyz.ashen.ashen/keystore/keystore.json` |
| **Windows** | `%APPDATA%\ashen\ashen\keystore\keystore.json`                         |

Override with `--path` or `NODE_KEYSTORE_PATH` environment variable.

***

## Related

[Section titled “Related”](#related)

* [Configuration](/reference/configuration/) — Node configuration including keystore paths
* [Using the CLI](/guides/using-the-cli/) — Full CLI reference
* [Deploying Contracts](/guides/deploying-contracts/) — Using keys for deployment

# MCP Server (ashen-mcp)

> Model Context Protocol reference for the Ashen MCP server

## Overview

[Section titled “Overview”](#overview)

`ashen-mcp` is a Model Context Protocol (MCP) server that exposes tools for interacting with Ashen nodes, building contracts, and managing local devnets. It speaks JSON-RPC 2.0 over stdio and is designed to be launched by an MCP-capable client (Claude Code, Cursor, etc.).

Binary: `ashen-mcp` (`src/bin/mcp_ashen.rs`)

## Run

[Section titled “Run”](#run)

```bash
# From the repo root
cargo run --bin ashen-mcp
```

The server reads JSON lines from stdin and writes JSON lines to stdout.

### Claude Code registration

[Section titled “Claude Code registration”](#claude-code-registration)

The repo’s `.mcp.json` registers `ashen-mcp` automatically:

```json
{
  "mcpServers": {
    "ashen": {
      "command": "cargo",
      "args": ["+nightly-2025-11-05", "run", "--bin", "ashen-mcp"],
      "env": { "NODE_RPC_URL": "http://127.0.0.1:3030" }
    }
  }
}
```

## Environment

[Section titled “Environment”](#environment)

| Variable            | Default                 | Purpose                                   |
| ------------------- | ----------------------- | ----------------------------------------- |
| `NODE_RPC_URL`      | `http://127.0.0.1:3030` | Base URL for the node RPC                 |
| `NODE_AUTH_TOKEN`   | *(unset)*               | Optional Bearer token for RPC auth        |
| `ASHEN_PRIVATE_KEY` | *(unset)*               | Default signing key for `contract_deploy` |

## Protocol

[Section titled “Protocol”](#protocol)

Supported JSON-RPC methods:

* `initialize`
* `tools/list`
* `tools/call`
* `ping`

Protocol version default: `2024-11-05`

***

## Tools — RPC Proxy

[Section titled “Tools — RPC Proxy”](#tools--rpc-proxy)

These tools proxy to the node’s JSON-RPC API. They require a running node at `NODE_RPC_URL`.

### `ashen.status`

[Section titled “ashen.status”](#ashenstatus)

Get chain status (tip height, epoch, finalized height).

```json
{}
```

### `ashen.account`

[Section titled “ashen.account”](#ashenaccount)

Fetch account state (balance, nonce lanes) by address.

```json
{ "address": "0x..." }
```

### `ashen.tx_submit`

[Section titled “ashen.tx\_submit”](#ashentx_submit)

Submit a signed transaction (hex-encoded).

```json
{ "tx": "0x..." }
```

### `ashen.contract_view`

[Section titled “ashen.contract\_view”](#ashencontract_view)

Execute a read-only contract call (view function).

```json
{
  "contract": "0x...",
  "calldata": "0x...",
  "origin": "0x...",
  "gas_limit": 1000000,
  "value": "0"
}
```

* `calldata` is ABI v1 encoded: `selector || borsh(args)`.
* `origin` and `value` are optional.

### `ashen.contract_idl`

[Section titled “ashen.contract\_idl”](#ashencontract_idl)

Fetch the IDL (interface definition) for a deployed contract.

```json
{ "address": "0x..." }
```

### `ashen.tx_by_hash`

[Section titled “ashen.tx\_by\_hash”](#ashentx_by_hash)

Look up a transaction by its hash. Returns state (pending, included, not found), execution outcome, logs, and fee details.

```json
{ "tx_hash": "0x..." }
```

### `ashen.tx_simulate`

[Section titled “ashen.tx\_simulate”](#ashentx_simulate)

Simulate a signed transaction without submitting it. Returns execution outcome, gas used, logs, and revert reason.

```json
{ "tx": "0x..." }
```

***

## Tools — Build

[Section titled “Tools — Build”](#tools--build)

These tools run `just` recipes to build and validate contracts. They execute shell commands and return stdout/stderr with exit codes.

### `ashen.contract_build`

[Section titled “ashen.contract\_build”](#ashencontract_build)

Build a single Rust contract for the RISC-V target.

```json
{ "manifest_path": "contracts/my_contract/Cargo.toml" }
```

### `ashen.contract_build_all`

[Section titled “ashen.contract\_build\_all”](#ashencontract_build_all)

Build all contracts (Zig + Rust) into `out/zig/` and `out/rust/`.

```json
{}
```

### `ashen.contract_bundle`

[Section titled “ashen.contract\_bundle”](#ashencontract_bundle)

Bundle a compiled ELF with its IDL for deployment.

```json
{
  "elf": "target/riscv64imac-unknown-none-elf/release/my_contract",
  "idl": "contracts/my_contract/my_contract.idl",
  "out": "./my_contract.bundle"
}
```

### `ashen.contract_deploy`

[Section titled “ashen.contract\_deploy”](#ashencontract_deploy)

Deploy a contract bundle. Waits for on-chain confirmation.

```json
{
  "bundle": "./my_contract.bundle",
  "key": "@./dev.key.json"
}
```

* `key` is optional; falls back to `$ASHEN_PRIVATE_KEY`.

### `ashen.vm_elf_validate`

[Section titled “ashen.vm\_elf\_validate”](#ashenvm_elf_validate)

Validate a compiled contract ELF binary.

```json
{
  "elf": "out/zig/my_contract.elf",
  "manifest": "./deploy.manifest.hex"
}
```

* `manifest` is optional.

### `ashen.gas_budget_check`

[Section titled “ashen.gas\_budget\_check”](#ashengas_budget_check)

Check all contract gas budgets against `.gas-budgets.toml`.

```json
{}
```

***

## Tools — Devnet & Node

[Section titled “Tools — Devnet & Node”](#tools--devnet--node)

These tools manage a local devnet node and run simulations.

### `ashen.node_start`

[Section titled “ashen.node\_start”](#ashennode_start)

Start a local devnet node as a background process. Writes a PID file to `target/mcp-node.pid` for lifecycle management.

```json
{
  "data_dir": "./node-data",
  "listen": "127.0.0.1:3030",
  "block_time_ms": 1000
}
```

All fields are optional with the defaults shown above.

### `ashen.node_stop`

[Section titled “ashen.node\_stop”](#ashennode_stop)

Stop the managed devnet node (started via `ashen.node_start`).

```json
{}
```

### `ashen.devnet_small`

[Section titled “ashen.devnet\_small”](#ashendevnet_small)

Run a deterministic 4-node devnet simulation (200 steps). Blocking; returns output when complete.

```json
{}
```

### `ashen.agent_smoke`

[Section titled “ashen.agent\_smoke”](#ashenagent_smoke)

Run the agent smoke test suite: workspace build check, 4-node consensus simulation, and core unit tests.

```json
{}
```

***

## Example Workflow

[Section titled “Example Workflow”](#example-workflow)

A typical agent workflow using MCP tools:

```plaintext
1. ashen.contract_build_all       → Build all contracts
2. ashen.gas_budget_check         → Verify gas budgets
3. ashen.node_start               → Start local devnet
4. ashen.status                   → Verify node is running
5. ashen.contract_deploy          → Deploy contract
6. ashen.contract_idl             → Verify deployed IDL
7. ashen.contract_view            → Test a view call
8. ashen.node_stop                → Tear down devnet
```

## Response Format

[Section titled “Response Format”](#response-format)

RPC tools return JSON content. Shell and devnet tools return text content with structured fields:

```json
{
  "exit_code": 0,
  "stdout": "...",
  "stderr": "..."
}
```

Non-zero exit codes include an `"error"` field describing the failure.

Shell commands have a 5-minute timeout (10 minutes for `agent_smoke`). Output is truncated at 128KB per stream.

## Errors

[Section titled “Errors”](#errors)

Errors are returned using JSON-RPC error objects:

| Code     | Meaning                 |
| -------- | ----------------------- |
| `-32700` | Parse error             |
| `-32601` | Method not found        |
| `-32602` | Invalid params          |
| `-32000` | RPC client init failure |
| `-32001` | Tool execution failure  |

## Related

[Section titled “Related”](#related)

* [RPC API](/reference/rpc-api/) for the underlying node RPC
* [Using the CLI](/guides/using-the-cli/) for CLI and calldata helpers
* [Local Devnet](/guides/devnet/) for devnet setup details
* [Deploying Contracts](/guides/deploying-contracts/) for contract deployment workflow

# Precompiles & Syscalls

> Complete reference for VM syscalls and cryptographic precompiles

## Overview

[Section titled “Overview”](#overview)

Ashen uses a **RISC-V syscall model** rather than EVM-style address-based precompiles. Each operation is identified by a numeric **syscall ID** invoked via the RISC-V `ecall` instruction. Contracts access syscalls through the Ashen SDK; the IDs themselves are part of the stable ABI defined in `vm-spec`.

All syscall costs include a **dispatch base** of 30 cycles. Variable-cost syscalls charge additional cycles based on input/output size using 32-byte word rounding: `words32 = ceil(bytes / 32)`.

## Syscall Table

[Section titled “Syscall Table”](#syscall-table)

### Storage

[Section titled “Storage”](#storage)

| ID | Name                 | Base                    | Variable                            | Description                          |
| -- | -------------------- | ----------------------- | ----------------------------------- | ------------------------------------ |
| 1  | `storage_read`       | 200 (warm) / 600 (cold) | +4/8 per 32B value                  | Read key-value from contract storage |
| 2  | `storage_write`      | 400                     | +8 per 32B value                    | Write key-value to contract storage  |
| 22 | `storage_scan_range` | 800                     | +4 per 32B input, +8 per 32B output | Range scan over storage keys         |

### Hints

[Section titled “Hints”](#hints)

| ID | Name              | Base | Description                                  |
| -- | ----------------- | ---- | -------------------------------------------- |
| 3  | `access_list_add` | 5    | Hint: add key to access list (does not warm) |
| 4  | `prefetch_key`    | 5    | Hint: prefetch a storage key                 |

### Calls & Deployment

[Section titled “Calls & Deployment”](#calls--deployment)

| ID | Name          | Base | Variable                            | Description                            |
| -- | ------------- | ---- | ----------------------------------- | -------------------------------------- |
| 5  | `call`        | 500  | +4 per 32B input, +4 per 32B return | Call another contract (state-changing) |
| 6  | `static_call` | 400  | +4 per 32B input, +4 per 32B return | Call another contract (read-only)      |
| 21 | `create`      | 2000 | +20 per 32B code                    | Deploy a new contract                  |

### Events

[Section titled “Events”](#events)

| ID | Name       | Base | Variable                       | Description       |
| -- | ---------- | ---- | ------------------------------ | ----------------- |
| 7  | `emit_log` | 150  | +20 per topic, +4 per 32B data | Emit an event log |

### Context & Queries

[Section titled “Context & Queries”](#context--queries)

| ID | Name            | Base | Description                                                |
| -- | --------------- | ---- | ---------------------------------------------------------- |
| 13 | `read_context`  | 20   | Read sender, value, block metadata                         |
| 14 | `random_beacon` | 40   | Read protocol randomness beacon (block-scoped)             |
| 15 | `gas_left`      | 5    | Query remaining gas budget                                 |
| 17 | `gas_limit`     | 5    | Query initial gas limit for current frame                  |
| 18 | `balance_of`    | 50   | Read native balance for an address                         |
| 19 | `self_balance`  | 30   | Read native balance for current contract                   |
| 20 | `block_hash`    | 80   | Read historical block hash (256-block window)              |
| 25 | `block_header`  | 100  | Read block hash + state\_root (64 bytes, 256-block window) |

### Precompiles: Hashing

[Section titled “Precompiles: Hashing”](#precompiles-hashing)

| ID | Name        | Base | Variable          | Description                    |
| -- | ----------- | ---- | ----------------- | ------------------------------ |
| 8  | `keccak256` | 800  | +20 per 32B input | Ethereum-compatible Keccak-256 |
| 9  | `sha2_256`  | 800  | +20 per 32B input | SHA-256                        |
| 10 | `blake3`    | 400  | +10 per 32B input | BLAKE3 (fastest)               |

### Precompiles: Signatures

[Section titled “Precompiles: Signatures”](#precompiles-signatures)

| ID | Name               | Base | Variable          | Description                          |
| -- | ------------------ | ---- | ----------------- | ------------------------------------ |
| 12 | `verify_ed25519`   | 6000 | +20 per 32B input | Ed25519 EDDSA signature verification |
| 16 | `verify_secp256k1` | 6000 | +20 per 32B input | ECDSA over secp256k1                 |

### Precompiles: VRF & Recovery

[Section titled “Precompiles: VRF & Recovery”](#precompiles-vrf--recovery)

| ID | Name                 | Base | Description                                    |
| -- | -------------------- | ---- | ---------------------------------------------- |
| 23 | `verify_vrf_ed25519` | 8000 | ECVRF-EDWARDS25519-SHA512-TAI (RFC 9381)       |
| 24 | `ecrecover`          | —    | Secp256k1 public key recovery (Ethereum-style) |

## Precompile Details

[Section titled “Precompile Details”](#precompile-details)

### Hash Functions

[Section titled “Hash Functions”](#hash-functions)

All hash precompiles accept variable-length input and return a fixed 32-byte digest. Gas scales linearly with input size.

```plaintext
total_gas = dispatch_base (30) + base + ceil(input_bytes / 32) * per_32b
```

**BLAKE3** is the cheapest hash at half the base cost and per-word rate of Keccak/SHA-256. Prefer it unless cross-chain compatibility requires a specific algorithm.

### Signature Verification

[Section titled “Signature Verification”](#signature-verification)

`verify_ed25519` and `verify_secp256k1` share the same gas schedule (`verify_sig`). Both accept a message hash, signature, and public key.

**Return values:**

* `STATUS_OK` (0): valid signature
* `STATUS_VERIFY_FAIL` (16): invalid signature, encoding, or key format

**Ed25519 inputs:** message\_hash (32B), signature (64B), public\_key (32B).

**Secp256k1 inputs:** message\_hash (32B), signature (64B compact r||s), public\_key (33-65B compressed or uncompressed).

### VRF Verification

[Section titled “VRF Verification”](#vrf-verification)

`verify_vrf_ed25519` verifies ECVRF proofs per RFC 9381. Fixed cost (no per-byte scaling).

**Inputs:** alpha (variable-length message), public\_key (32B), proof (80B: gamma

* c + s).

**Output:** 32-byte VRF output written to caller-provided buffer on success.

### ecrecover

[Section titled “ecrecover”](#ecrecover)

Secp256k1 public key recovery, Ethereum-compatible.

**Inputs:** message\_hash (32B), signature (64B r||s), recovery\_id (0 or 1).

**Output:** uncompressed public key (64B, x||y) on success.

## Feature Flags

[Section titled “Feature Flags”](#feature-flags)

Precompiles are gated by feature flags, controllable at both compile time and runtime via the `PrecompileRegistry`:

| Flag                    | Precompiles                        |
| ----------------------- | ---------------------------------- |
| `precompile-hashing`    | keccak256, sha2\_256, blake3       |
| `precompile-signatures` | verify\_ed25519, verify\_secp256k1 |
| `precompile-vrf`        | verify\_vrf\_ed25519               |
| `precompile-recovery`   | ecrecover                          |

All flags are enabled by default. Node operators can selectively disable precompiles via `RegistryBuilder`:

```rust
let registry = RegistryBuilder::new()
    .with_feature("precompile-hashing")
    .with_feature("precompile-signatures")
    // VRF and recovery disabled
    .build();
```

## Resource Limits

[Section titled “Resource Limits”](#resource-limits)

The VM enforces per-call, per-transaction, and per-block limits on precompile input data to prevent DoS:

| Limit                      | Default |
| -------------------------- | ------- |
| Per-call precompile input  | 256 KB  |
| Per-tx precompile input    | 512 KB  |
| Per-block precompile input | 8 MB    |

Other relevant limits:

| Limit                 | Default      |
| --------------------- | ------------ |
| Max call depth        | 64           |
| Max code size         | 1 MB         |
| Stack per frame       | 128 KB       |
| Heap pages per frame  | 640 (2.5 MB) |
| Storage writes per tx | 4,096        |
| Log bytes per tx      | 64 KB        |

Exceeding precompile input caps returns `PRECOMPILE_CAP` or `PRECOMPILE_CAP_PER_BLOCK` errors.

## SDK Usage

[Section titled “SDK Usage”](#sdk-usage)

### Zig

[Section titled “Zig”](#zig)

```zig
const sdk = @import("ashen-sdk");
const crypto = sdk.crypto;


// Hashing
const digest = crypto.keccak256(data);
const sha_digest = crypto.sha256(data);
const b3_digest = crypto.blake3(data);


// Signature verification
const valid = crypto.ed25519Verify(msg_hash, signature, pubkey);


// Key recovery
const recovered_key = crypto.ecrecover(msg_hash, signature, recovery_id);
```

### Rust

[Section titled “Rust”](#rust)

```rust
use contract_sdk::Host;


// Hashing
let digest = Host::keccak256(data)?;
let sha_digest = Host::sha2_256(data)?;
let b3_digest = Host::blake3(data)?;


// Signature verification
let valid = Host::verify_ed25519(msg_hash, signature, pubkey)?;
```

## Canonical Source

[Section titled “Canonical Source”](#canonical-source)

The gas schedule is locked in `docs/gas-schedules/gas-v1.json`. Syscall IDs are defined in `crates/vm-spec/src/lib.rs` and are part of the stable ABI — changing an ID is consensus-breaking.

## Related

[Section titled “Related”](#related)

* [Gas Schedule](/reference/gas-schedule/) — full opcode and memory cost tables
* [Gas Throughput](/reference/gas-throughput/) — block gas budgets and throughput
* [Feature Flags](/reference/feature-flags/) — runtime feature gating
* [Ashen SDK](/contracts/ashen-sdk/) — Zig SDK reference
* [SDK Reference](/reference/sdk/) — multi-language SDK overview

# RPC API

> JSON-RPC API reference

## Overview

[Section titled “Overview”](#overview)

Ashen exposes a JSON-RPC 2.0 API defined by a single IDL (Interface Definition Language) file: `node_rpc_v1.idl`. Every type, method, parameter, and return value in the API is declared in this IDL. Clients, the TUI, and code-generation tooling all derive their behavior from the same source of truth rather than hand-coded stubs.

## IDL Discovery

[Section titled “IDL Discovery”](#idl-discovery)

The node serves the IDL itself over HTTP so that tools can discover the API at runtime.

| Endpoint               | Returns            | Description                                                     |
| ---------------------- | ------------------ | --------------------------------------------------------------- |
| `GET /v2/rpc/idl`      | `text/plain`       | Raw IDL source text                                             |
| `GET /v2/rpc/manifest` | `application/json` | Parsed manifest with method signatures, struct/enum definitions |

CLI shortcuts:

```bash
just rpc-idl        # fetch raw IDL from a running node
just rpc-manifest   # fetch the JSON manifest
```

### TUI Explorer

[Section titled “TUI Explorer”](#tui-explorer)

The built-in TUI embeds the IDL at compile time and provides an **RPC Explorer** screen. It parses `node_rpc_v1.idl` at startup — no network call is needed for method discovery.

Features:

* Filterable method list (press `/` to search)
* Method signatures with parameter types and documentation
* Direct execution: press `x` to call a method, `v` for read-only view
* On-chain contract IDL loading via `contract_idl()`

## Protocol

[Section titled “Protocol”](#protocol)

All RPC calls use **JSON-RPC 2.0** over HTTP:

```plaintext
POST /v2/rpc
Content-Type: application/json
```

Request:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "NodeRpcV1.status",
  "params": {}
}
```

Methods can be addressed by qualified name (`NodeRpcV1.status`) or unqualified (`status`) when unambiguous.

### Type Conventions

[Section titled “Type Conventions”](#type-conventions)

* **Enums** are encoded as `{"type": "<variant_snake_case>", "value": <payload>}`. Example: `{"type": "transfer", "value": {"to": "0x...", "amount": "10"}}`.
* **Large integers** (`u128`, `i128`) are JSON strings: `"1000000000000000000"`.
* **Addresses** are hex strings with `0x` prefix.
* **Hashes** are lowercase hex strings (no fixed `0x` requirement).

## Access Tiers

[Section titled “Access Tiers”](#access-tiers)

Methods are classified into three access tiers:

| Tier            | Description                                                | Examples                                      |
| --------------- | ---------------------------------------------------------- | --------------------------------------------- |
| **Public**      | Open to all callers, no auth required                      | `status`, `health`, `account`, `tx_submit`    |
| **Paid (x402)** | Expensive operations, may require payment or rate limiting | `tx_simulate`, `chain_traceCall`, `view_call` |
| **Admin**       | Restricted to node operators                               | `tx_build`, `import_snapshot_chunk`           |

Authentication uses a Bearer token in the `Authorization` header when required.

## Method Reference

[Section titled “Method Reference”](#method-reference)

### Status & Health

[Section titled “Status & Health”](#status--health)

| Method             | Parameters | Returns           | Description                                                    |
| ------------------ | ---------- | ----------------- | -------------------------------------------------------------- |
| `status`           | —          | `Status`          | Chain tip, finalized height, epoch, validator set, txpool size |
| `health`           | —          | `HealthResult`    | Liveness probe (Kubernetes-compatible)                         |
| `readiness`        | —          | `ReadinessResult` | Readiness probe: sync status, epoch key availability           |
| `validator_status` | —          | `ValidatorStatus` | DKG state, sync, peer health, consensus metrics                |

### Accounts & Contracts

[Section titled “Accounts & Contracts”](#accounts--contracts)

| Method              | Parameters          | Returns                  | Description                                         |
| ------------------- | ------------------- | ------------------------ | --------------------------------------------------- |
| `account`           | `address`           | `Account`                | Balance and nonce lanes for an address              |
| `accounts`          | `addresses[]`       | `AccountsResult`         | Batch account lookup (deterministic order)          |
| `predict_address`   | `deployer, offset?` | `PredictAddressResult`   | Predict a contract deploy address                   |
| `contract_metadata` | `address`           | `ContractMetadataResult` | VM type, code hash, ABI version, upgrade policy     |
| `contract_idl`      | `address`           | `ContractIdlResult`      | Raw IDL text stored on-chain (if deployed with IDL) |
| `view_call`         | `ViewCallArgs`      | `ViewCallResult`         | Read-only contract call (no state change)           |

### Transaction Building & Submission

[Section titled “Transaction Building & Submission”](#transaction-building--submission)

| Method              | Parameters     | Returns                 | Description                                                   |
| ------------------- | -------------- | ----------------------- | ------------------------------------------------------------- |
| `tx_build`          | `TxBuildArgs`  | `TxBuildResult`         | Build an unsigned transaction envelope                        |
| `tx_build_simulate` | `TxBuildArgs`  | `TxBuildSimulateResult` | Build + simulate in one call                                  |
| `tx_submit`         | `TxSubmitArgs` | `TxSubmitResult`        | Submit a signed transaction                                   |
| `tx_by_hash`        | `tx_hash`      | `TxByHashResult`        | Look up transaction by hash (pending, included, or not found) |
| `tx_receipt`        | `tx_hash`      | `TxReceiptResult`       | Full receipt with decoded events (when IDL is available)      |

### Simulation & Tracing

[Section titled “Simulation & Tracing”](#simulation--tracing)

| Method                   | Parameters                  | Returns                       | Description                            |
| ------------------------ | --------------------------- | ----------------------------- | -------------------------------------- |
| `tx_simulate`            | `TxSimulateArgs`            | `TxSimulateResult`            | Simulate execution, estimate gas       |
| `tx_simulate_access`     | `TxSimulateAccessArgs`      | `TxSimulateAccessResult`      | Simulate + return storage access list  |
| `tx_simulate_trace`      | `TxSimulateTraceArgs`       | `TxSimulateTraceResult`       | Simulate with full execution trace     |
| `tx_simulate_pipeline`   | `TxSimulatePipelineArgs`    | `TxSimulatePipelineResult`    | Multi-step pipeline (txs + view calls) |
| `chain_traceTransaction` | `ChainTraceTransactionArgs` | `ChainTraceTransactionResult` | Trace an already-included transaction  |
| `chain_traceCall`        | `ChainTraceCallArgs`        | `ChainTraceCallResult`        | Trace a view call                      |

### Blocks & Listings

[Section titled “Blocks & Listings”](#blocks--listings)

| Method                 | Parameters              | Returns                   | Description                                       |
| ---------------------- | ----------------------- | ------------------------- | ------------------------------------------------- |
| `list_blocks`          | `ListBlocksArgs`        | `ListBlocksResult`        | Paginated blocks (newest-first, cursor-based)     |
| `list_txs`             | `ListTxsArgs`           | `ListTxsResult`           | Paginated transactions (newest-first)             |
| `list_txs_by_sender`   | `ListTxsBySenderArgs`   | `ListTxsBySenderResult`   | Transactions by sender address                    |
| `list_txs_by_contract` | `ListTxsByContractArgs` | `ListTxsByContractResult` | Transactions involving a contract                 |
| `get_logs`             | `GetLogsArgs`           | `GetLogsResult`           | Event logs by contract, topic, and/or block range |
| `list_pending_txs`     | `ListPendingTxsArgs`    | `ListPendingTxsResult`    | Pending transactions from the mempool             |
| `txpool_stats`         | —                       | `TxpoolStats`             | Mempool size, lanes, sealed queue                 |
| `get_blocks`           | `GetBlocksArgs`         | `GetBlocksResult`         | Blocks by height range                            |
| `get_block_summaries`  | `GetBlocksArgs`         | `GetBlockSummariesResult` | Lightweight block summaries for a height range    |
| `get_txs_in_range`     | `GetBlocksArgs`         | `GetTxsInRangeResult`     | All transactions in a block height range          |
| `get_checkpoint_list`  | —                       | `CheckpointListResult`    | Available checkpoints                             |

### Proofs & Light Client

[Section titled “Proofs & Light Client”](#proofs--light-client)

| Method                    | Parameters                  | Returns                       | Description                                             |
| ------------------------- | --------------------------- | ----------------------------- | ------------------------------------------------------- |
| `finality_proof`          | `FinalityProofArgs`         | `FinalityProofResult`         | Finality proof for a block height                       |
| `light_client_context`    | `LightClientContextArgs`    | `LightClientContextResult`    | Verification context for light clients                  |
| `state_proof`             | `StateProofArgs`            | `StateProofResult`            | State proof for a contract (optionally a specific slot) |
| `finalized_history_root`  | `FinalizedHistoryRootArgs`  | `FinalizedHistoryRootResult`  | Current finalized history MMR root                      |
| `finalized_history_proof` | `FinalizedHistoryProofArgs` | `FinalizedHistoryProofResult` | MMR membership proof for a finalized block              |

### Snapshots & Sync

[Section titled “Snapshots & Sync”](#snapshots--sync)

| Method                  | Parameters                | Returns                     | Description                                    |
| ----------------------- | ------------------------- | --------------------------- | ---------------------------------------------- |
| `get_light_snapshot`    | `GetLightSnapshotArgs`    | `GetLightSnapshotResult`    | Light snapshot for verified fast sync          |
| `get_checkpoint`        | `GetCheckpointArgs`       | `GetCheckpointResult`       | Checkpoint descriptor by height                |
| `list_checkpoints`      | `ListCheckpointsArgs`     | `ListCheckpointsResult`     | Available checkpoints with archive descriptors |
| `get_snapshot_chunk`    | `GetSnapshotChunkArgs`    | `GetSnapshotChunkResult`    | Chunk of snapshot entries for state sync       |
| `import_snapshot_chunk` | `ImportSnapshotChunkArgs` | `ImportSnapshotChunkResult` | Import snapshot entries (Admin)                |

### Private Mempool & Bundles

[Section titled “Private Mempool & Bundles”](#private-mempool--bundles)

| Method                 | Parameters           | Returns                | Description                                 |
| ---------------------- | -------------------- | ---------------------- | ------------------------------------------- |
| `tx_submit_sealed`     | `TxSubmitSealedArgs` | `TxSubmitSealedResult` | Submit a threshold-encrypted transaction    |
| `get_epoch_key`        | `GetEpochKeyArgs`    | `GetEpochKeyResult`    | Threshold encryption public key for sealing |
| `tx_submit_bundle`     | `TxSubmitBundleArgs` | `TxSubmitBundleResult` | Submit an atomic transaction bundle         |
| `chain_simulateBundle` | `BundleSimulateArgs` | `BundleSimulateResult` | Simulate a bundle with dependency analysis  |

## Contract IDL

[Section titled “Contract IDL”](#contract-idl)

Contracts can store their IDL on-chain at deploy time. The `contract_idl` method retrieves the raw IDL text for any address. The TUI uses this to provide method-level exploration and parameter templates for contract calls — the same IDL-driven discovery that powers the node RPC explorer also works for individual contracts.

## Example

[Section titled “Example”](#example)

```bash
curl -s http://localhost:8080/v2/rpc \
  -H 'Content-Type: application/json' \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "NodeRpcV1.status",
    "params": {}
  }' | jq .result
```

```json
{
  "version": "0.1.0",
  "chain_id": 1,
  "now_ms": 1706900000000,
  "uptime_ms": 3600000,
  "block_time_ms": 500,
  "tip": {
    "height": 12345,
    "hash": "a1b2c3...",
    "timestamp_ms": 1706899999500,
    "state_root": "d4e5f6...",
    "epoch": 42,
    "view": 0
  },
  "finalized_height": 12340,
  "latest_checkpoint": {
    "height": 12300,
    "state_root": "..."
  },
  "txpool_size": 7
}
```

# SDK Reference

> Multi-language SDKs for smart contract development

Ashen provides SDKs for writing smart contracts in **Zig** and **Rust**.

Tip

**Zig is recommended** for most contracts. It has the most complete SDK with safe math, events, guards, and storage helpers.

For RPC client SDKs and error handling guidance, see `/reference/error-handling/` and `/reference/error-domains/`.

## Contract SDK Comparison

[Section titled “Contract SDK Comparison”](#contract-sdk-comparison)

| Feature                  | Zig SDK                  | Rust SDK                           |
| ------------------------ | ------------------------ | ---------------------------------- |
| **Location**             | `contracts/ashen-sdk/`   | `crates/contract-sdk/`             |
| **Use Case**             | Smart contracts          | Smart contracts                    |
| **Storage Helpers**      | `storage`, `collections` | `Item`, `Map`, `Set`, `StorageVec` |
| **Safe Math**            | `sdk.math`, `sdk.guards` | Manual                             |
| **Events**               | `sdk.events` (typed)     | `Host::emit_log`                   |
| **Reentrancy Guards**    | `sdk.guards`             | Manual                             |
| **Cross-Contract Calls** | `sdk.call`               | `Host::call`, `Host::static_call`  |
| **Codegen**              | IDL → Zig stubs          | IDL → Rust stubs                   |

***

## Zig SDK

[Section titled “Zig SDK”](#zig-sdk)

The Zig SDK (`contracts/ashen-sdk/`) provides the most complete developer experience for smart contracts.

* Quick Start

  ```zig
  const sdk = @import("ashen-sdk");


  export fn _start(calldata_ptr: [*]const u8, calldata_len: usize) sdk.ByteSlice {
      sdk.heap.reset();
      const calldata = if (calldata_len == 0) &[_]u8{} else calldata_ptr[0..calldata_len];
      // Dispatch to your methods...
      return sdk.ByteSlice.from(result);
  }


  pub const panic = sdk.panic;
  ```

* Storage

  ```zig
  const storage = sdk.storage;


  // Raw bytes
  const value = storage.read(key);
  storage.write(key, data);


  // Typed u128
  const balance = storage.readU128(key);
  storage.writeU128(key, amount);
  ```

* Events

  ```zig
  const events = sdk.events;


  // Define event signature
  const Transfer = events.define("Transfer(address,address,uint256)");


  // Emit with indexed topics
  Transfer.emit2(from, to, events.toTopicU128(amount), &[_]u8{});
  ```

* Math & Guards

  ```zig
  const math = sdk.math;
  const guards = sdk.guards;


  // Safe arithmetic
  const sum = guards.safeAdd(u128, a, b) catch return error;
  const diff = guards.safeSub(u128, a, b) catch return error;


  // Fixed-point math
  const fee = math.bpsMul(amount, 30); // 0.3%
  const shares = math.isqrt(product);


  // Reentrancy protection
  try guards.enterNonReentrant();
  defer guards.exitNonReentrant();
  ```

### Zig SDK Modules

[Section titled “Zig SDK Modules”](#zig-sdk-modules)

| Module    | Import        | Purpose                                                |
| --------- | ------------- | ------------------------------------------------------ |
| `heap`    | `sdk.heap`    | Bump allocator: `reset()`, `allocSlice()`, `allocator` |
| `storage` | `sdk.storage` | `read()`, `write()`, `readU128()`, `writeU128()`       |
| `context` | `sdk.context` | `caller()`, `origin()`, `blockHeight()`, `value()`     |
| `crypto`  | `sdk.crypto`  | `keccak256()`, `sha256()`, `blake3()`                  |
| `call`    | `sdk.call`    | Cross-contract: `call()`, `staticCall()`               |
| `events`  | `sdk.events`  | Typed events with indexed topics                       |
| `guards`  | `sdk.guards`  | Reentrancy protection, safe arithmetic                 |
| `math`    | `sdk.math`    | WAD/RAY/BPS fixed-point, `isqrt()`, `min()`, `max()`   |

[Ashen SDK Guide ](/contracts/ashen-sdk/)Full Zig SDK documentation

***

## Rust SDK

[Section titled “Rust SDK”](#rust-sdk)

The Rust SDK (`crates/contract-sdk/`) provides low-level control for contracts requiring Rust-specific features.

### Crate Architecture

[Section titled “Crate Architecture”](#crate-architecture)

| Crate          | Purpose                                               |
| -------------- | ----------------------------------------------------- |
| `contract-rt`  | Minimal runtime: entrypoint, panic handler, allocator |
| `contract-sdk` | Developer API: Host struct, storage, ABI helpers      |

### Host API

[Section titled “Host API”](#host-api)

```rust
use contract_sdk::{Host, Address, ContractErrorV1};


impl Host {
    // Storage
    pub fn storage_read(key: &[u8]) -> Result<Option<Vec<u8>>, HostError>;
    pub fn storage_write(key: &[u8], value: &[u8]) -> Result<(), HostError>;


    // Context
    pub fn caller() -> Address;
    pub fn origin() -> Address;
    pub fn self_address() -> Address;
    pub fn block_number() -> u64;
    pub fn block_timestamp() -> u64;


    // Logs
    pub fn emit_log(topics: &[[u8; 32]], data: &[u8]) -> Result<(), HostError>;


    // Cross-contract calls
    pub fn call<T: BorshDeserialize>(
        to: &Address, value: u64, gas: u64, calldata: &[u8]
    ) -> Result<T, CallError>;


    pub fn static_call<T: BorshDeserialize>(
        to: &Address, gas: u64, calldata: &[u8]
    ) -> Result<T, CallError>;


    // Crypto precompiles
    pub fn keccak256(input: &[u8]) -> Result<[u8; 32], HostError>;
    pub fn sha2_256(input: &[u8]) -> Result<[u8; 32], HostError>;
    pub fn blake3(input: &[u8]) -> Result<[u8; 32], HostError>;
}
```

### Storage Collections

[Section titled “Storage Collections”](#storage-collections)

```rust
use contract_sdk::{Item, Map, Set, StorageVec, define_storage};


define_storage! {
    namespace: "my_contract",
    pub struct Storage {
        pub counter: Item<u64>,
        pub owner: Item<[u8; 32]>,
        pub balances: Map<[u8; 32], u128>,
        pub approved: Set<[u8; 32]>,
        pub history: StorageVec<Event>,
    }
}
```

### Error Handling

[Section titled “Error Handling”](#error-handling)

```rust
use contract_sdk::{ContractErrorV1, require};


// Standardized errors
pub enum ContractErrorV1 {
    Code { code: u32, data: Option<Vec<u8>> },
    Other { message: String },  // max 1024 bytes
}


// Require macro
require!(amount > 0, ERR_ZERO_AMOUNT);
require!(caller == owner, ERR_UNAUTHORIZED);
```

### ABI Encoding

[Section titled “ABI Encoding”](#abi-encoding)

All contracts use: `calldata = selector (4 bytes) || borsh(args)`

Returns: `borsh(Result<T, ContractErrorV1>)`

```rust
use contract_sdk::{parse_calldata_v1, encode_result_v1, SELECTOR_BYTES_V1};


// Parse incoming call
let (selector, args_bytes) = parse_calldata_v1(calldata)?;


// Encode response
let response = encode_result_v1(&Ok(return_value));
```

***

***

## Client SDK (TypeScript)

[Section titled “Client SDK (TypeScript)”](#client-sdk-typescript)

The TypeScript SDK (`packages/ashen-sdk-ts/`) is for **client-side applications** that interact with the chain—not for writing smart contracts. Use it for:

* Building frontends and dApps
* Agent automation and scripting
* Transaction signing and submission
* Reading chain state via RPC

Note

This is a **client SDK**, not a contract SDK. Smart contracts are written in Zig or Rust.

### Features

[Section titled “Features”](#features)

| Feature             | Description                                             |
| ------------------- | ------------------------------------------------------- |
| **RPC Client**      | Full JSON-RPC interface with retries and error handling |
| **Borsh Encoding**  | Encode/decode transaction arguments and return values   |
| **ed25519 Signing** | Sign transactions with ed25519 keypairs                 |
| **IDL Codegen**     | Generate type-safe contract bindings from IDL           |
| **Light Client**    | Verify state proofs without trusting the RPC            |

### Usage

[Section titled “Usage”](#usage)

```typescript
import { AshenClient, Keypair } from 'ashen-sdk-ts';


// Connect to RPC
const client = new AshenClient('https://rpc.ashen.sh');


// Read state
const balance = await client.getBalance(address);
const nonce = await client.getNonce(address);


// Sign and submit a transaction
const keypair = Keypair.fromSecretKey(secretKey);
const tx = await client.buildTransaction({
  to: contractAddress,
  data: encodedCalldata,
  nonce,
});
const signedTx = keypair.sign(tx);
const hash = await client.submitTransaction(signedTx);


// Wait for inclusion
const receipt = await client.waitForTransaction(hash);
```

### Codegen

[Section titled “Codegen”](#codegen)

Generate TypeScript bindings from IDL for type-safe contract interaction:

```bash
just idl-abi-gen \
  --idl contracts/sft_v1/sft_v1.idl \
  --out-dir ./generated \
  --typescript
```

This generates typed methods for each contract function:

```typescript
import { SftV1Client } from './generated/sft_v1';


const sft = new SftV1Client(client, contractAddress);
const totalSupply = await sft.totalSupply();
await sft.mint({ to: recipient, amount: 1000n });
```

***

## IDL Code Generation

[Section titled “IDL Code Generation”](#idl-code-generation)

The `idl-abi-gen` crate generates type-safe bindings for all languages.

```bash
# Zig stubs + dispatcher
just idl-abi-gen \
  --idl contracts/mycontract/mycontract.idl \
  --out-dir contracts/mycontract/src \
  --zig-stubs


# Rust bindings
just idl-abi-gen \
  --idl contracts/mycontract/mycontract.idl \
  --out-dir contracts/mycontract/src \
  --rust-contract


# TypeScript client
just idl-abi-gen \
  --idl contracts/mycontract/mycontract.idl \
  --out-dir ./generated \
  --typescript
```

### Selector Derivation

[Section titled “Selector Derivation”](#selector-derivation)

Selectors are 4 bytes derived from the method signature:

```plaintext
selector = blake3(signature_string)[0..4]
```

The signature includes method name and canonicalized argument types. Collisions within a contract interface cause a hard failure at codegen time.

***

## Next Steps

[Section titled “Next Steps”](#next-steps)

[Ashen SDK (Zig) ](/contracts/ashen-sdk/)Full Zig SDK guide

[Contract Examples ](/contracts/examples/)Sample contracts

[IDL & ABI ](/contracts/idl-and-abi/)Interface definitions

[Using the CLI ](/guides/using-the-cli/)CLI reference

# VM Tiering & Code Cache

> Execution tiers, hot-code promotion, code cache internals, and observability

**Source**: `crates/vm-codecache`, `crates/vm-runtime/src/execution.rs`

## Overview

[Section titled “Overview”](#overview)

Ashen uses a **tiered execution model** for RISC-V contracts. New code starts in the interpreter and can be promoted to higher-performance tiers as it becomes “hot” (frequently executed). Gas accounting is tier-independent --- the same gas is charged regardless of which tier executes.

## Enable Tiering

[Section titled “Enable Tiering”](#enable-tiering)

Tiering is gated by both compile-time and runtime switches:

```bash
# Build with tiering support
cargo build --features std,tui,vm-tiering


# Enable at runtime
ASHEN_VM_TIERING=1 ./target/debug/node
```

If `ASHEN_VM_TIERING` is unset, the node runs interpreter-only even when compiled with `vm-tiering`.

## Execution Tiers

[Section titled “Execution Tiers”](#execution-tiers)

| Tier            | Description                                                       | When Used                         |
| --------------- | ----------------------------------------------------------------- | --------------------------------- |
| **Interpreter** | Decode-per-instruction reference tier; semantic authority         | Cold code, short executions       |
| **JIT**         | Lazy predecode; caches basic blocks on first execution            | Moderately-hot code               |
| **AOT**         | Eager predecode; entire program pre-decoded at load time          | Hot code, production steady-state |
| **Native**      | Cranelift JIT to native machine code (`cranelift-native` feature) | Compute-heavy contracts           |

### Interpreter Modes

[Section titled “Interpreter Modes”](#interpreter-modes)

The interpreter supports two sub-modes:

| Mode         | Description                          | Best For                             |
| ------------ | ------------------------------------ | ------------------------------------ |
| `Step`       | Execute one instruction at a time    | Short executions, constrained memory |
| `BlockCache` | Cache decoded basic blocks for reuse | Tight loops, repeated code paths     |

### Native Tier (Cranelift)

[Section titled “Native Tier (Cranelift)”](#native-tier-cranelift)

The `cranelift-native` feature enables compilation of hot basic blocks to native machine code via Cranelift. If native compilation fails for a block (e.g., unsupported instruction), execution falls back to the interpreter for that block.

## Tier Selection

[Section titled “Tier Selection”](#tier-selection)

When using the code cache, the runtime queries `best_available_tier()`:

```plaintext
Aot (if cached) > Jit (if cached) > Interpreter (fallback)
```

The fallback table for explicit tier requests:

| Requested   | Cache Has | Effective   |
| ----------- | --------- | ----------- |
| Aot         | Aot       | Aot         |
| Aot         | Jit       | Jit         |
| Aot         | nothing   | Interpreter |
| Jit         | Jit+      | Jit         |
| Jit         | nothing   | Interpreter |
| Interpreter | any       | Interpreter |

## Hot-Code Promotion

[Section titled “Hot-Code Promotion”](#hot-code-promotion)

The `HotCodeTracker` monitors per-contract execution and promotes hot code automatically. Each contract is tracked by its `code_hash`.

```plaintext
tracker.record(code_hash, gas_used) -> Option<Tier>
```

On each call, the tracker increments `call_count` and accumulates `total_gas`. Promotion triggers when call count exceeds a threshold:

| Threshold             | Promotes To |
| --------------------- | ----------- |
| `jit_threshold_calls` | `Tier::Jit` |
| `aot_threshold_calls` | `Tier::Aot` |

When promotion fires:

* **JIT**: Stores the program image in the code cache for lazy basic-block predecoding on next execution.
* **AOT**: Pre-decodes the entire program into a `PredecodedProgram` and stores it in the cache. Future executions skip all decode work.

Promotion happens **after** execution completes and does not consume additional gas. Promotion failures (e.g., decode errors) are silently ignored --- the contract continues at the lower tier.

By default, JIT/AOT entries remain zero until contracts exceed the promotion thresholds.

## Code Cache

[Section titled “Code Cache”](#code-cache)

### Cache Key

[Section titled “Cache Key”](#cache-key)

All cache entries are keyed by `CacheKey`:

| Field                | Type           | Description                                |
| -------------------- | -------------- | ------------------------------------------ |
| `code_hash`          | `[u8; 32]`     | Blake3 hash of deployed contract ELF bytes |
| `abi_version`        | `u16`          | Contract ABI version (currently `1`)       |
| `gas_schedule_id`    | `&'static str` | Gas schedule identifier (e.g., `"gas-v1"`) |
| `translator_version` | `u16`          | Predecoder version (currently `1`)         |
| `toolchain_hash`     | `[u8; 32]`     | Hash of the contract toolchain manifest    |

Any change to these fields invalidates all entries for that contract.

### Artifact Types

[Section titled “Artifact Types”](#artifact-types)

| Artifact            | Description                                | Tier |
| ------------------- | ------------------------------------------ | ---- |
| `ProgramImage`      | Resolved ELF with segments and entry point | All  |
| `PredecodedProgram` | Predecoded basic blocks for AOT execution  | Aot  |
| `Opaque`            | Arbitrary bytes (future extension)         | Any  |

### In-Memory Cache

[Section titled “In-Memory Cache”](#in-memory-cache)

The `CodeCache` is an LRU cache with configurable limits:

| Setting       | Default | Description                            |
| ------------- | ------- | -------------------------------------- |
| `max_entries` | 1024    | Maximum number of cached artifacts     |
| `max_bytes`   | 256 MiB | Maximum total size of cached artifacts |

When limits are exceeded, the least-recently-used entry is evicted. The cache tracks per-entry `hit_count`, `last_used_tick`, and `total_gas_consumed`.

### Cache Invalidation

[Section titled “Cache Invalidation”](#cache-invalidation)

| Event                             | Action                                                  |
| --------------------------------- | ------------------------------------------------------- |
| Gas schedule version bump         | All entries invalidated (embedded in cache key)         |
| ABI version bump                  | Affected entries invalidated (embedded in cache key)    |
| Translator version bump           | All entries invalidated (embedded in cache key)         |
| Contract code change              | That contract’s entries invalidated (code hash changes) |
| Cache format version bump         | All disk entries invalidated (header mismatch)          |
| Node restart (unchanged versions) | Reuses persisted entries                                |

## Disk Persistence

[Section titled “Disk Persistence”](#disk-persistence)

The `DiskCodeCache` persists compiled artifacts across node restarts.

| Setting       | Default                | Description                             |
| ------------- | ---------------------- | --------------------------------------- |
| `cache_dir`   | `~/.ashen/code-cache/` | Storage directory                       |
| `max_entries` | 4096                   | Max entries on disk                     |
| `max_bytes`   | 512 MiB                | Max total size on disk                  |
| `enabled`     | `true`                 | Can be disabled for pure in-memory mode |

### File Format

[Section titled “File Format”](#file-format)

Each entry is stored as `{hex(key_hash)}-{tier}.bin`:

```plaintext
[4 bytes]  Magic: "ASHC"
[1 byte]   Format version (currently 1)
[1 byte]   Tier (0=Interpreter, 1=Jit, 2=Aot)
[32 bytes] Blake3 checksum of (cache_key || artifact_bytes)
[8 bytes]  Artifact size (little-endian u64)
[N bytes]  Artifact data (borsh-serialized)
```

**Corruption handling**: Blake3 checksum verification on load. Corrupt, truncated, or oversize entries are automatically deleted.

**Atomic writes**: Entries are written to a `.tmp` file, then atomically renamed.

**Portability**: Cache entries are **not** portable across architectures or translator versions.

## Gas Accounting

[Section titled “Gas Accounting”](#gas-accounting)

Gas charging is tier-independent. All tiers pay the same `predecode_per_byte` cost upfront, charged against the gas meter before execution begins:

```plaintext
predecode_gas = predecode_per_byte * program_size_bytes
```

The `predecode_per_byte` rate is defined in the gas schedule (`gas-v1.json`). AOT-eager mode deducts this cost before execution; cached AOT was charged at compilation time.

## Observability

[Section titled “Observability”](#observability)

When `std` + `vm-tiering` are enabled, the node exports Prometheus metrics under `/metrics`:

| Metric                                   | Description                             |
| ---------------------------------------- | --------------------------------------- |
| `code_cache_entries`                     | Total cached entries                    |
| `code_cache_entries_by_tier{tier="..."}` | Entries by tier (interpreter, jit, aot) |
| `code_cache_bytes`                       | Total bytes used by cache               |
| `code_cache_hits`                        | Total cache hits since startup          |
| `code_cache_misses`                      | Total cache misses since startup        |

`CodeCache::stats()` returns a `CodeCacheStats` snapshot with `hit_rate()` (computed as hits / total lookups, 0.0 to 1.0).

### Verifying Tiering

[Section titled “Verifying Tiering”](#verifying-tiering)

1. Build with `--features vm-tiering`.
2. Set `ASHEN_VM_TIERING=1` and run the node.
3. Execute contract workloads.
4. Check `code_cache_entries_by_tier{tier="jit"}` and `tier="aot"`.

If JIT/AOT remain zero, the node is running tiered selection but no contracts have exceeded the promotion thresholds yet.

## Entry Points

[Section titled “Entry Points”](#entry-points)

The runtime provides execution entry points with increasing configurability:

| Function                           | Use Case                                   |
| ---------------------------------- | ------------------------------------------ |
| `execute_entrypoint`               | Basic interpreter, no cache                |
| `execute_entrypoint_tier`          | Explicit mode selection, no cache          |
| `execute_entrypoint_tiered`        | Auto-select best tier from cache           |
| `execute_entrypoint_cached`        | Explicit tier request + cache              |
| `execute_entrypoint_with_tracking` | Cache + hot-code promotion (production)    |
| `execute_entrypoint_with_config`   | Unified entry point via `EntrypointConfig` |

For production block execution, use `execute_entrypoint_with_tracking` or `execute_entrypoint_with_config` with both cache and tracker configured.

## Related

[Section titled “Related”](#related)

* [Gas Schedule](/reference/gas-schedule/) --- gas costs including `predecode_per_byte`
* [Precompiles & Syscalls](/reference/precompiles/) --- syscall gas costs
* [Feature Flags](/reference/feature-flags/) --- `vm-tiering` and `cranelift-native`
* [JIT Compilation](/upcoming/jit-compilation/) --- design notes on tiered JIT

# Upcoming Designs

> Draft designs and ideas that are under active exploration

## Design Drafts

[Section titled “Design Drafts”](#design-drafts)

These are active design drafts. Expect changes.

[Access Lists ](/upcoming/access-lists/)EIP-2930 style access lists, prefetch, and gas model.

[Consensus-Execution Pipelining ](/upcoming/consensus-execution-pipelining/)Overlap consensus and execution; currently deferred.

[JIT Compilation ](/upcoming/jit-compilation/)Tiered JIT strategy for RISC-V contracts.

[Cross-Contract Call Tracing ](/upcoming/cross-contract-call-tracing/)Hierarchical traces for calls, storage, and events.

## Upcoming Docs (Implemented Features)

[Section titled “Upcoming Docs (Implemented Features)”](#upcoming-docs-implemented-features)

These features are implemented but still missing dedicated docs pages. Each item links to a bead for the doc task.

### State & Proofs

[Section titled “State & Proofs”](#state--proofs)

* [State sync & checkpoints](/upcoming/state-sync-checkpoints/) (chain-3abl4)
* [Finalized MMR + proof RPCs](/upcoming/finalized-mmr-proofs/) (chain-3u2vg)
* [State proof RPC (contracts/slots)](/upcoming/state-proof-rpc/) (chain-ayq5w)

### Execution & VM

[Section titled “Execution & VM”](#execution--vm)

* VM tiering & code cache (chain-1rjnh)
* [VM tooling & test harness](/upcoming/vm-tooling-test-harness/) (chain-151jt)

### Networking & Data Availability

[Section titled “Networking & Data Availability”](#networking--data-availability)

* DA chunk recovery & block reconstruction (chain-i7rzm)

### Mempool & Fees

[Section titled “Mempool & Fees”](#mempool--fees)

* [Gas fee distribution & proposer rewards](/upcoming/gas-fee-distribution/) (chain-ddx5o)
* [Txpool rate limiting & DoS guardrails](/upcoming/txpool-rate-limiting/) (chain-2woxo)

## Design Archive (Repo)

[Section titled “Design Archive (Repo)”](#design-archive-repo)

Design docs that already exist in the repo (not yet copied into the docs site):

* [docs/design](https://github.com/carrion256/chain/tree/main/docs/design) (implemented or mature designs)
* [ideas/design](https://github.com/carrion256/chain/tree/main/ideas/design) (idea sketches and proposals)

# Access Lists

> Draft design for access lists and state prefetching

**Source**: `docs/design/access-lists.md`

**Status**: Draft **Issue**: chain-5alwd **Date**: 2026-02-03

## Overview

[Section titled “Overview”](#overview)

Access lists let a transaction declare which accounts and storage keys it expects to touch. The chain can use these hints to prefetch state, charge lower gas for declared (warm) keys, and improve parallel scheduling. The current codebase already contains `AccessList` types, validation rules, and strict-access checks behind a feature flag. This document formalizes the semantics and activation plan.

## Goals

[Section titled “Goals”](#goals)

1. Reduce disk I/O and latency by prefetching declared state.
2. Provide a deterministic warm/cold gas model for declared accesses.
3. Enable strict access enforcement (reject undeclared accesses) when activated via a hard fork.
4. Improve parallel execution scheduling with declared conflicts.
5. Keep transaction format stable (reuse `TxBodyV1.access_list`).

## Non-Goals

[Section titled “Non-Goals”](#non-goals)

* Full stateless execution or witness generation (future work).
* Automatic access list inference inside the VM (client-side tooling only).
* Unbounded range/prefix expansion that can DoS validators.

## Current State (Already Implemented)

[Section titled “Current State (Already Implemented)”](#current-state-already-implemented)

* `TxBodyV1` includes `access_list: AccessList` and it is part of the signed payload.
* `AccessList::validate()` enforces size and descriptor rules.
* `TracedStateBackend` can track touched keys and enforce strict access (`ASHEN_STRICT_ACCESS`).
* `state_keys_from_access_list` derives a concrete key set for prefetch.
* `prefetch_access_list_keys` issues read requests to warm the hot cache.
* Gas constants for access list accounting exist in `src/core/execution/gas.rs`.

## Transaction Format

[Section titled “Transaction Format”](#transaction-format)

No new transaction type is introduced. We keep `TxBodyV1.access_list` and formalize its semantics:

* `accounts`: declares per-account metadata accesses (balance, nonce, code, metadata) for each address.

* `storage`: declares storage descriptors per contract address.

* `AccessDescriptor` variants:

  * `Exact`: a specific 32-byte key.
  * `Prefix`: a prefix (1-32 bytes).
  * `Range`: inclusive/exclusive bounds.

* `AccessMode` indicates Read / Write / ReadWrite intent for scheduling and enforcement policies.

Versioning note: we do not add an access-list version or format flag in v1. Because the chain is greenfield (no `DEPLOYED` flag), we can adjust `TxBodyV1` pre-launch without adding a version flag. After deployment, incompatible changes must use a new `TxBody::V2`.

## Validation Rules

[Section titled “Validation Rules”](#validation-rules)

Validation happens at admission time and prior to execution:

1. `AccessList::validate()` must pass or the tx is rejected with `InvalidAccessList`.
2. All addresses referenced by `accounts` and `storage` entries must exist in state at admission time, except when the transaction is explicitly creating the address (deploy or first-fund transfer).
3. If strict access is enabled, any touched key not covered by the access list causes execution to revert with `UndeclaredStateAccess`.
4. Prefix/range descriptors are valid for access checks and scheduling, and they should also drive bounded prefetch scans.

## Gas Model

[Section titled “Gas Model”](#gas-model)

The gas model has three parts:

1. **Declaration cost**: charge per declared account and descriptor to prevent DoS via huge access lists.
2. **Warm vs cold storage**: accesses covered by the access list are charged at warm rates; undeclared keys are charged at cold rates with a punitive multiplier to discourage missing access lists.
3. **Prefetch accounting**: prefetching declared keys incurs a small per-key cost (observational today, enforceable after activation).

Descriptor pricing guidance:

* `Exact` descriptors: 2\_000 gas per descriptor.
* `Prefix` / `Range`: 3\_000 gas per descriptor (slightly higher than `Exact`).
* Warm access for `Exact` uses the warm schedule from `gas-v1`.
* Warm access for `Prefix` / `Range` uses warm \* 1.25 (rounded up), still below cold pricing.
* Undeclared access uses cold pricing with a punitive multiplier of 2.0.

These are starting values; tune after benchmarks.

Activation plan:

* Phase 0 (current): log-only access list gas and prefetch costs.
* Phase 1: enforce declaration costs and warm/cold price distinction.
* Phase 2: enable strict access rejection for undeclared keys.

## Prefetch Strategy

[Section titled “Prefetch Strategy”](#prefetch-strategy)

Prefetching should be opportunistic and bounded:

* Use `state_keys_from_access_list` to derive concrete keys.

* Prefetch should also honor `Prefix` and `Range` descriptors via bounded scans (limit by keys or bytes). Truncate when the per-tx budget is hit.

* Prefetch at block construction time so the block builder pays for the I/O and can price it via gas.

* Prefetching should be disabled when the backend lacks a hot cache.

* Cap prefetch per transaction to prevent a single tx from exhausting I/O. Initial defaults:

  * `max_prefetch_keys_per_tx = 512`
  * `max_prefetch_bytes_per_tx = 256 KiB`
  * `max_prefetch_scan_keys_per_descriptor = 64`

## Hot Cache Integration

[Section titled “Hot Cache Integration”](#hot-cache-integration)

* Prefetch should warm the hot cache (`CachedJournalStateBackend`).
* If the cache is full, respect its eviction policy (LRU) and never bypass capacity limits.
* Consider cache TTL / height-based expiry for prefetched keys to avoid long-lived cache pollution.
* When `chain-5hsc` lands, prefetch can target the cached backend directly and rely on its size/eviction rules.

## RPC: Access List Generation

[Section titled “RPC: Access List Generation”](#rpc-access-list-generation)

Clients should be able to request access list generation during simulation:

* `SimulationOptions.generate_access_list = true` triggers tracing of touched keys and returns a `GeneratedAccessList` with an estimated gas savings.
* Expose this via an RPC method analogous to `eth_createAccessList`, e.g. `tx_createAccessList`.
* The access list is advisory; signing clients decide whether to include it. The RPC response should include the estimated gas savings.

## Block-STM Integration

[Section titled “Block-STM Integration”](#block-stm-integration)

Declared access lists enable scheduler optimizations:

* Use descriptor overlap checks to precompute conflicts.
* Prefer scheduling non-overlapping transactions in parallel.
* AccessMode can inform read-only vs write conflicts.

This integrates with the Block-STM design doc (`docs/design/block-stm.md`).

## Consensus / Hard Fork Plan

[Section titled “Consensus / Hard Fork Plan”](#consensus--hard-fork-plan)

Access list enforcement is consensus-critical and must be activated at a specific block height:

1. Add a `access_list_activation_height` config in consensus parameters.
2. Because the chain is not live, set this at launch time (TBD).
3. After activation: declaration costs + warm/cold pricing enforced.
4. Strict access rejection can be enabled later (separate height or config).

## Open Questions

[Section titled “Open Questions”](#open-questions)

1. Finalize activation height(s) once launch planning is fixed.
2. Confirm the initial prefetch caps after a quick I/O benchmark pass.
3. Decide whether strict access should be a separate hard fork or a config toggle post-launch.

## Deliverables

[Section titled “Deliverables”](#deliverables)

1. `docs/design/access-lists.md` (this document)
2. Transaction format notes for access list semantics
3. Gas schedule delta for warm/cold pricing and declaration costs
4. RPC spec for access list generation and return type
5. Activation plan (block height and phased rollout)

# Consensus-Execution Pipelining

> Draft design for overlapping consensus and execution

**Source**: `docs/design/consensus-execution-pipelining.md`

**Status**: Draft (Deferred) **Issue**: chain-6cepd **Date**: 2026-02-03

## Summary

[Section titled “Summary”](#summary)

Consensus-execution pipelining overlaps consensus for block N+1 with execution of block N. This can reduce the critical path per block when execution time is non-trivial. However, it introduces material complexity for light clients, state-root semantics, and rollback behavior. We are deferring implementation until the chain is closer to launch and execution is a confirmed bottleneck.

## Motivation

[Section titled “Motivation”](#motivation)

Today, the block path is serial:

```plaintext
Propose -> Vote/Finalize -> Execute -> Done
```

If execution takes a significant fraction of block time, overall throughput is limited by (consensus + execution). Pipelining overlaps these stages:

```plaintext
Block N:   Propose/Vote/Finalize
Block N:                     Execute
Block N+1:         Propose/Vote/Finalize
```

This reduces per-block latency and increases throughput **only when execution is slow relative to consensus**. With a fast RISC-V VM, the benefit may be small until workloads grow.

## Why Defer

[Section titled “Why Defer”](#why-defer)

* **Light client complexity**: state proofs must target a different header (or an execution receipt) once execution lags consensus.
* **State root semantics**: headers can no longer trivially commit to the post-execution state of the same block.
* **Rollback complexity**: if execution lags and a reorg happens, execution must roll back and re-run safely.

Given these costs and the chain not being live yet, we will defer the implementation and revisit once execution throughput is a proven bottleneck.

## Proposed Design (If/When Revisited)

[Section titled “Proposed Design (If/When Revisited)”](#proposed-design-ifwhen-revisited)

### 1. State Root Semantics

[Section titled “1. State Root Semantics”](#1-state-root-semantics)

Pipelining requires decoupling the consensus header from the execution root. Two viable options:

**Option A: Delayed Root**

* Block N header commits to the state root after executing block N-1.
* Pros: simple header structure.
* Cons: proofs for block N transactions must reference N+1 (or earlier).

**Option B: Execution Receipt (preferred for clarity)**

* Block N header commits to consensus data only.

* Block N+1 carries an `ExecutionReceipt` for block N:

  * block hash
  * execution status
  * post-state root

* Light clients verify receipts to tie execution to consensus.

### 2. Failure Handling

[Section titled “2. Failure Handling”](#2-failure-handling)

Execution must not be allowed to “fail” the block after finality. Options:

* Treat execution failures as *per-transaction reverts* only; the block is still valid.
* Enforce pre-execution validation so that all consensus-accepted blocks are guaranteed to execute deterministically (no fatal VM errors).

If execution can fail fatally, pipelining is unsafe. We should treat fatal execution errors as consensus-invalid and prevent pipelining until we have strong pre-execution validation.

### 3. Light Client Impact

[Section titled “3. Light Client Impact”](#3-light-client-impact)

Light clients need a clear rule for which header roots to use:

* Proofs for transaction effects must target the **execution receipt root** (Option B) or a **delayed root** (Option A).

* Clients track two heights:

  * `finalized_height`
  * `executed_height`

### 4. RPC State Model

[Section titled “4. RPC State Model”](#4-rpc-state-model)

Introduce explicit tags:

* `finalized`: highest finalized block (consensus)
* `executed`: highest block with execution receipt
* `safe`: min(finalized, executed)
* `pending`: mempool / in-flight

### 5. Reorg Handling

[Section titled “5. Reorg Handling”](#5-reorg-handling)

If consensus reorgs block N after block N has executed:

* Roll back execution state to the last executed canonical ancestor.
* Re-run execution for the new canonical chain.
* Requires snapshotting / journaling of execution state (already present in state backends, but needs validation under pipelining).

### 6. Execution Queue / Backpressure

[Section titled “6. Execution Queue / Backpressure”](#6-execution-queue--backpressure)

* Use a bounded execution queue.
* If execution lags, block builders should throttle block size or delay proposals to avoid unbounded backlog.

## Risks

[Section titled “Risks”](#risks)

* Light client proof complexity and client upgrade burden.
* Increased state management complexity (snapshots, receipts, rollbacks).
* Consensus/execution mismatch if validation is insufficient.

## Recommendation

[Section titled “Recommendation”](#recommendation)

Defer implementation until:

1. Execution is a dominant bottleneck in production-like benchmarks.
2. Light client protocol changes are acceptable for downstream consumers.
3. Execution receipts / rollback strategy are fully specified.

## Deliverables

[Section titled “Deliverables”](#deliverables)

1. `docs/design/consensus-execution-pipelining.md` (this document)
2. State diagram showing block lifecycle (if revisited)
3. Failure mode analysis (if revisited)
4. Light client protocol delta (if revisited)
5. RPC compatibility matrix (if revisited)

# Cross-Contract Call Tracing

> Hierarchical call traces with storage ops, events, and gas

**Source**: `docs/design/cross-contract-call-tracing.md`

**Status**: Draft **Issue**: chain-3gy7a **Date**: 2026-02-03

## Overview

[Section titled “Overview”](#overview)

Cross-contract call tracing captures the full call tree for a single VM execution. Each call frame records gas usage, inputs/outputs, storage operations, events, and nested calls so debugging and profiling can happen with full context.

## Trace Data Model

[Section titled “Trace Data Model”](#trace-data-model)

Tracing is represented by a `TraceFrame` tree in `crates/vm-runtime` and mirrored into `src/core/execution/types.rs` for node-level use. Each frame includes:

* Call metadata: call type, caller, callee, value, gas limit, gas used.
* Payloads: input calldata and output bytes.
* Side effects: storage ops (read/write/delete) with before/after values and gas.
* Events: emitted logs with contract + topics + data.
* Children: nested call frames.
* Error metadata and a wall-clock duration in nanoseconds.

Related types:

* `TraceStorageOp` and `TraceStorageOpType`
* `TraceLogEntry`
* `TraceError`
* `TracingConfig` (max depth)

## Capture Flow

[Section titled “Capture Flow”](#capture-flow)

1. `TxContext::enable_tracing(TracingConfig { max_depth })` turns tracing on.
2. Syscall handlers call `enter_call_frame` on call entry and `exit_call_frame` on return.
3. Storage reads/writes and log emissions are pushed into the current frame via `trace_storage_op` and `trace_event`.
4. `take_root_trace()` returns the root `TraceFrame` tree for formatting or post-processing.

Depth is capped by `TracingConfig.max_depth` (default: 64). Frames beyond the limit are suppressed rather than partially recorded.

## Output Formats

[Section titled “Output Formats”](#output-formats)

`crates/vm-runtime/src/trace_format.rs` renders the trace tree into:

* JSON (`to_json`, `to_json_compact`, `to_json_with_metadata`)
* Chrome trace format (`to_chrome_trace` / `to_chrome_trace_pretty`)
* Human-readable tree output (`to_tree` / `to_tree_with_config`)

`src/core/execution/trace_format.rs` mirrors similar formatters for core `TraceFrame` types at the node layer.

## Post-Processing Utilities

[Section titled “Post-Processing Utilities”](#post-processing-utilities)

These helpers live in `crates/vm-runtime` and can be wired into higher-level interfaces as needed:

* `trace_compress`: deduplicates repeated subtrees to keep large traces small.
* `trace_filter`: selective tracing by contract, depth range, gas threshold, value transfer, selector, or failure-only.
* `trace_diff`: structured comparison between two traces for regressions.
* `trace_summary`: aggregates net storage deltas, events, touched contracts, and gas/time stats.

## RPC Surface

[Section titled “RPC Surface”](#rpc-surface)

The RPC IDL defines hierarchical trace endpoints:

* `chain_traceTransaction`: returns a detailed frame tree with storage ops and events (`TraceFrameDetailed`). Accepts `max_depth`.
* `chain_traceCall`: returns a simpler frame tree (`TraceFrame`) for view calls.

See `src/rpc/node_rpc_v1.idl` for the request/response fields.

## Trace Persistence (Flat Traces)

[Section titled “Trace Persistence (Flat Traces)”](#trace-persistence-flat-traces)

`src/debug/trace.rs` stores flat execution traces (`ExecutionTrace`) built from `VmTxTrace` (storage writes, logs, transfers, return data). Storage is enabled with environment variables:

* `ASHEN_DEBUG_TRACE_DIR`
* `ASHEN_DEBUG_TRACE_MAX_BLOCKS`
* `ASHEN_DEBUG_TRACE_MAX_BYTES`

This path is for deterministic replay and audit trails, not the hierarchical call tree.

## Where to Look

[Section titled “Where to Look”](#where-to-look)

* Runtime tracing core: `crates/vm-runtime/src/context.rs`
* Formatters: `crates/vm-runtime/src/trace_format.rs`
* Compression/diff/filter/summary: `crates/vm-runtime/src/trace_*.rs`
* Core type bridge: `src/core/execution/types.rs`
* RPC definitions: `src/rpc/node_rpc_v1.idl`
* Trace storage: `src/debug/trace.rs`

# Finalized History MMR & Proof RPCs

> Finalized history commitment and light-client proof endpoints

**Source**: `docs/design/light-client-mmr-onchain.md`, `src/storage/finalized_mmr.rs`, `src/rpc/node_rpc_v1.idl`

## Overview

[Section titled “Overview”](#overview)

The chain maintains an append-only Merkle Mountain Range (MMR) over finalized blocks. This provides compact inclusion proofs for any finalized height and is used by light clients, RPC nodes, and verified fast sync.

Key properties:

* Leaves are `(height, block_hash)` entries.
* The MMR is **append-only** and only advances with finalized blocks.
* Proofs are short and verifiable against a single root.

## Data Model

[Section titled “Data Model”](#data-model)

### Leaf hash

[Section titled “Leaf hash”](#leaf-hash)

Each leaf is hashed as:

```plaintext
BLAKE3("finalized_entry_v1" || height_le || block_hash)
```

### Root

[Section titled “Root”](#root)

The MMR root is a 32-byte BLAKE3 hash computed from all finalized entries.

### Proof

[Section titled “Proof”](#proof)

A membership proof includes:

* `leaf_position` (0-indexed)
* `leaf_count` at time of proof
* `siblings`: a list of `(hash, is_left)` pairs

Verification folds siblings from leaf to root, using the `is_left` flag to order concatenation.

## RPC Endpoints

[Section titled “RPC Endpoints”](#rpc-endpoints)

All endpoints are in `node_rpc_v1`:

### `finality_proof`

[Section titled “finality\_proof”](#finality_proof)

Returns a `FinalityProofResult` for a block height:

* `height`, `block_hash`, `epoch`, `view`, `parent_view`
* `key_version`
* `certificate` (BLS threshold signature, hex)
* `proof_bytes` (borsh-encoded proof, hex)

### `light_client_context`

[Section titled “light\_client\_context”](#light_client_context)

Returns `LightClientContextResult` for verifying a finality proof:

* `commitment_root` (validator set root)
* `aggregate_bls_pubkey`
* `validators` (addresses + voting power)
* `aggregate_key_proof` (Merkle proof for aggregate key)
* `context_bytes` (borsh-encoded context, hex)

### `finalized_history_root`

[Section titled “finalized\_history\_root”](#finalized_history_root)

Returns `FinalizedHistoryRootResult`:

* `root` (hex) or `null` if no finalized blocks
* `leaf_count`

### `finalized_history_proof`

[Section titled “finalized\_history\_proof”](#finalized_history_proof)

Returns `FinalizedHistoryProofResult`:

* `height`, `block_hash`
* `leaf_position`, `leaf_count`
* `siblings` (hash + `is_left`)
* `root`

### `get_light_snapshot`

[Section titled “get\_light\_snapshot”](#get_light_snapshot)

Returns `GetLightSnapshotResult` for checkpoint fast sync:

* `checkpoint` (height + state\_root)
* `header` (block header fields)
* `mmr_proof` (finalized history proof)
* `finality_proof` (optional)
* `validators`
* `snapshot_bytes` (borsh-encoded snapshot)

## Verification Flow (Light Client)

[Section titled “Verification Flow (Light Client)”](#verification-flow-light-client)

1. **Finality proof**

   * Fetch `finality_proof(height)` and `light_client_context(height)`.
   * Verify the BLS certificate against the aggregate key and validator set.

2. **MMR inclusion (optional but recommended)**

   * Fetch `finalized_history_root()` and `finalized_history_proof(height)`.
   * Recompute the leaf hash and fold siblings to verify the root.
   * This proves the finalized block is included in the append-only history.

3. **Fast sync (checkpoints)**

   * Fetch `get_light_snapshot(height)`.
   * Verify the snapshot header and MMR proof against a trusted root.

## CLI Helpers (Local Verification)

[Section titled “CLI Helpers (Local Verification)”](#cli-helpers-local-verification)

The node CLI includes helpers for proof verification:

```plaintext
node verify --height 100 --rpc-url http://127.0.0.1:3030
node verify-snapshot --height 100 --trusted-root 0x...
```

## Caching and Consistency

[Section titled “Caching and Consistency”](#caching-and-consistency)

* Proofs are cached server-side but **invalidated on each append** to the MMR.
* `leaf_count` is part of the proof. A proof is valid only for that count.

## Error Cases

[Section titled “Error Cases”](#error-cases)

Common errors:

* `NOT_FOUND`: height not in MMR
* `MMR_EMPTY`: no finalized blocks recorded
* `MMR_POSITION_OUT_OF_BOUNDS`: bad leaf position

## Related Docs

[Section titled “Related Docs”](#related-docs)

* `docs/design/light-client-mmr-onchain.md`
* `docs/design/state-layout.md`
* `docs/design/data-availability-sampling.md`

# Gas Fee Distribution & Proposer Rewards

> How gas fees are split between burn and proposer rewards

**Source**: `src/core/execution/mod.rs` (fee accounting), `src/core/execution/types.rs`

## Overview

[Section titled “Overview”](#overview)

Gas fees are split using an EIP-1559-style model:

* **Base fee** is burned (removed from supply).
* **Priority fee** goes to the block proposer.

This keeps fee pricing predictable while still rewarding validators for block production.

## Definitions

[Section titled “Definitions”](#definitions)

* `gas_used`: total VM gas consumed by the transaction
* `base_fee`: per-gas base fee (from the block header)
* `max_fee`: user-specified maximum fee in the transaction
* `total_fee_paid`: actual fee charged

## Fee Flow

[Section titled “Fee Flow”](#fee-flow)

### VM Transactions

[Section titled “VM Transactions”](#vm-transactions)

For VM calls, the engine charges gas as execution proceeds and refunds any unused gas to the payer:

```plaintext
fee_cap = max_fee
consumed = gas_used
refund = fee_cap - gas_used
```

### Simple Transfers

[Section titled “Simple Transfers”](#simple-transfers)

For non-VM transfers, the full fee cap is charged:

```plaintext
consumed = fee_cap
refund = 0
```

### Split Between Burn and Proposer

[Section titled “Split Between Burn and Proposer”](#split-between-burn-and-proposer)

```plaintext
burned_fees   = min(base_fee * gas_used, total_fee_paid)
proposer_fees = total_fee_paid - burned_fees
```

* `burned_fees` are not credited to any account.
* `proposer_fees` are credited to the block proposer’s fee recipient address.

## Proposer Recipient

[Section titled “Proposer Recipient”](#proposer-recipient)

The proposer recipient is derived from the consensus leader for the block. If no proposer is available, no proposer fees are credited.

## Fee Breakdown in Receipts

[Section titled “Fee Breakdown in Receipts”](#fee-breakdown-in-receipts)

Clients receive an explicit fee breakdown:

* `gas_limit`, `gas_used`
* `effective_gas_price` (v1 uses 1:1 unit pricing)
* `max_fee`, `priority_tip`
* `total_fee_paid`
* `base_fee_per_gas`, `burned_fees`, `proposer_fees`

## Notes

[Section titled “Notes”](#notes)

* Fee accounting is **asset-aware**: refunds and credits use the same fee asset as the transaction’s `FeeIntent`.
* Simulations do not distribute proposer fees.

## Related Docs

[Section titled “Related Docs”](#related-docs)

* `docs/design/vault-gas-token.md` (future gas token model)
* `docs-site/src/content/docs/concepts/gas-and-fees.md`

# JIT Compilation

> Draft design for tiered JIT compilation for RISC-V contracts

**Source**: `docs/design/jit-compilation.md`

**Status**: Draft **Issue**: chain-6jitd **Date**: 2026-02-03

## Summary

[Section titled “Summary”](#summary)

Add a tiered JIT to speed up hot contract code while preserving strict interpreter-equivalent semantics. The interpreter remains the reference implementation; JIT tiers must be deterministic, gas-accurate, and safe.

## Goals

[Section titled “Goals”](#goals)

1. 5x-20x speedup for hot contracts compared to the interpreter.
2. Deterministic behavior identical to interpreter (results + gas).
3. Safe execution with strong sandboxing guarantees.
4. Bounded memory and predictable compile overhead.
5. Clear rollback path: any JIT anomaly falls back to interpreter.

## Non-Goals

[Section titled “Non-Goals”](#non-goals)

* Replacing the interpreter as the semantic authority.
* Aggressive speculative optimizations that risk nondeterminism.
* Unbounded per-contract compilation or caching.

## Tiering Strategy

[Section titled “Tiering Strategy”](#tiering-strategy)

We use three tiers:

1. **Tier 0: Interpreter (reference)**
2. **Tier 1: Baseline JIT** (fast compile, modest speedup)
3. **Tier 2: Optimizing JIT** (slower compile, higher speedup)

### Promotion Criteria (initial)

[Section titled “Promotion Criteria (initial)”](#promotion-criteria-initial)

* Promote to Tier 1 when **total gas executed** for a contract exceeds 10\_000\_000 or after 20 calls (whichever comes first).
* Promote to Tier 2 when **total gas executed** exceeds 200\_000\_000 or after 200 calls (whichever comes first).
* Demote to interpreter if a JIT tier triggers any validation failure or code cache entry is evicted.

These thresholds are starting points and should be tuned with benchmarks.

### Tiering State Machine (ASCII)

[Section titled “Tiering State Machine (ASCII)”](#tiering-state-machine-ascii)

```plaintext
          +-------------+
          | Interpreter |
          +-------------+
              |  hot
              v
          +-------------+
          | Baseline JIT|
          +-------------+
              |  hotter
              v
          +-------------+
          | Opt JIT     |
          +-------------+
              ^
              |  failure / eviction
              +--------------------
```

## Determinism and Correctness

[Section titled “Determinism and Correctness”](#determinism-and-correctness)

* Interpreter output is canonical. JIT results must match **exactly**:

  * return values
  * state writes
  * logs
  * gas usage

* The JIT must not depend on runtime nondeterminism (CPU features, timing, randomness, or OS-dependent codegen).

* On any detected mismatch, automatically disable JIT for the process and fall back to the interpreter.

### Verification Strategy

[Section titled “Verification Strategy”](#verification-strategy)

1. **Differential fuzzing** (existing `vm-conformance` infrastructure): run random programs across interpreter, baseline JIT, and opt JIT and compare outputs and gas.
2. **Replay tests**: execute recorded devnet traces in both tiers.
3. **Per-build conformance**: require 0 mismatches across a seed corpus.

## Code Cache

[Section titled “Code Cache”](#code-cache)

### Cache Key

[Section titled “Cache Key”](#cache-key)

```plaintext
(code_hash, gas_schedule_id, vm_config_hash, tier)
```

### Eviction Policy

[Section titled “Eviction Policy”](#eviction-policy)

* LRU by total code size.
* Hard cap: 512 MiB (configurable).
* Optional per-contract cap: 64 MiB.

### Persistence

[Section titled “Persistence”](#persistence)

* Phase 1: in-memory only.
* Phase 2: optional disk cache for baseline JIT.

## Sandboxing / Isolation

[Section titled “Sandboxing / Isolation”](#sandboxing--isolation)

We need strong isolation because native JIT code executes inside the validator process. We will stage sandboxing:

### Phase 1 (Baseline)

[Section titled “Phase 1 (Baseline)”](#phase-1-baseline)

* In-process JIT with **software bounds checks** on all memory accesses.
* W^X (write xor execute) for JIT pages.
* No syscalls from JIT code; all external interactions go through hostcalls.

### Phase 2 (Stronger Isolation)

[Section titled “Phase 2 (Stronger Isolation)”](#phase-2-stronger-isolation)

* Move JIT execution into a **separate process** with:

  * seccomp-bpf profile
  * shared memory for linear memory pages
  * strict IPC for hostcalls

This phase can be delayed if in-process checks prove safe and fast.

## Gas Metering in JIT

[Section titled “Gas Metering in JIT”](#gas-metering-in-jit)

We must preserve gas accounting identical to the interpreter.

### Proposed Approach

[Section titled “Proposed Approach”](#proposed-approach)

* Precompute gas cost per basic block during decode.

* Insert a gas check at **basic block entry**:

  * `if gas_left < block_cost -> trap`
  * otherwise subtract block\_cost and continue.

* For indirect branches and loop back-edges, ensure a gas check is executed each time control enters the block.

This mirrors the interpreter’s per-instruction accounting while keeping JIT overhead low.

## Contract Upgrades / Cache Invalidation

[Section titled “Contract Upgrades / Cache Invalidation”](#contract-upgrades--cache-invalidation)

* JIT cache entries are keyed by `code_hash`. Any code change yields a new hash and naturally invalidates old entries.
* If contract address points to new code, tiering state resets to interpreter.

## Cross-Contract Calls

[Section titled “Cross-Contract Calls”](#cross-contract-calls)

* Calls always route through the runtime dispatcher, which selects the highest available tier for the callee.
* JIT-to-JIT calls use the same ABI as interpreter calls.
* If a callee is missing JIT code, fall back to interpreter for that call.

## Benchmark Targets (Initial)

[Section titled “Benchmark Targets (Initial)”](#benchmark-targets-initial)

* Baseline JIT compile time: <= 5 ms for 10k instructions.

* Opt JIT compile time: <= 50 ms for 10k instructions.

* Speedup targets (steady-state):

  * Baseline JIT: 5x
  * Opt JIT: 10x-20x

* Memory overhead: <= 2x code size per compiled tier.

## Open Questions

[Section titled “Open Questions”](#open-questions)

1. Tune promotion thresholds and cache caps after benchmark data.
2. Decide whether opt JIT should ever be disk-cached.

## Deliverables

[Section titled “Deliverables”](#deliverables)

1. `docs/design/jit-compilation.md` (this document)
2. Tiering state machine diagram (included above)
3. Sandboxing threat model (outlined above)
4. Gas metering accuracy analysis (included above)
5. Benchmark targets (included above)

# State Proof RPC (Contracts & Slots)

> RPC for contract and storage-slot proofs against the state root

**Source**: `src/rpc/node_rpc_v1.idl`, `src/storage/state/proofs.rs`

## Overview

[Section titled “Overview”](#overview)

`state_proof` returns a cryptographic proof that a contract exists (or not) under the global state root, and optionally proves a specific storage slot exists (or not) under that contract root.

Proofs are built from:

* **Outer tree**: contract address -> contract root (Binary Merkle Tree / QMDB)
* **Inner tree**: slot key -> slot value (contract storage tree)

The response includes enough material to verify the proof client-side without access to node state.

## RPC: `state_proof`

[Section titled “RPC: state\_proof”](#rpc-state_proof)

### Request

[Section titled “Request”](#request)

```plaintext
{
  "address": "0x...",
  "slot_key": "0x...",   // optional
  "height": 1234         // optional (defaults to latest finalized)
}
```

* `address`: contract address (hex)
* `slot_key`: optional storage key (hex)
* `height`: optional block height; if omitted, uses latest finalized height

### Response (StateProofResult)

[Section titled “Response (StateProofResult)”](#response-stateproofresult)

```plaintext
{
  "address": "0x...",
  "canonical_address": "0x...",
  "contract_root": "0x...",
  "state_root": "0x...",
  "last_loc": 42,
  "ops": [
    { "canonical_address": "0x...", "contract_root": "0x...", "position": 0 }
  ],
  "bounded_proof": { ... },
  "slot_proof": { ... } | null,
  "height": 1234
}
```

Key fields:

* `state_root`: global state commitment for the given height
* `contract_root`: root of the contract’s storage tree
* `ops` + `last_loc`: QMDB operation log needed to recompute the outer root
* `bounded_proof`: membership/non-membership proof for the contract address
* `slot_proof`: optional proof for a slot key (exists or non-exists)

## Verification Flow

[Section titled “Verification Flow”](#verification-flow)

### 1) Recompute the outer root (QMDB ops)

[Section titled “1) Recompute the outer root (QMDB ops)”](#1-recompute-the-outer-root-qmdb-ops)

* Sort `ops` by `position` and ensure positions are contiguous `0..last_loc`.
* Ensure canonical addresses are strictly increasing.
* Recompute the QMDB root from ops; must match `state_root`.

### 2) Verify the contract proof

[Section titled “2) Verify the contract proof”](#2-verify-the-contract-proof)

* Use `bounded_proof` to prove the contract’s leaf exists (or not) in the outer tree.
* The bounded proof includes a leaf proof plus left/right neighbor proofs for non-membership ordering checks.

### 3) Verify the slot proof (optional)

[Section titled “3) Verify the slot proof (optional)”](#3-verify-the-slot-proof-optional)

If `slot_key` was provided:

* **Exists**: verify the slot’s leaf digest under `contract_root`.
* **NonExists**: verify neighbor ordering under `contract_root`.

## Slot Proof Variants

[Section titled “Slot Proof Variants”](#slot-proof-variants)

* `Exists`: `{ canonical_key, value, proof }`
* `NonExists`: `{ queried_key, left?, right? }`

Both variants are verified against the contract root.

## Error Cases

[Section titled “Error Cases”](#error-cases)

* `INVALID_PARAMS`: bad hex in `slot_key` or malformed request
* `NOT_IMPLEMENTED`: backend does not support state proofs
* `INTERNAL`: proof generation failed

## Notes / Constraints

[Section titled “Notes / Constraints”](#notes--constraints)

* The backend must support ordered QMDB proofs. Some backends may not.
* Proofs are for **finalized** state when `height` is omitted.
* A missing contract returns a **non-membership** proof and `slot_proof = null`.

## Related Docs

[Section titled “Related Docs”](#related-docs)

* `docs/design/state-layout.md`
* `docs/design/light-client-mmr-onchain.md`
* `docs-site/src/content/docs/upcoming/finalized-mmr-proofs.md`

# State Sync & Checkpoints

> Snapshot-based fast sync using finalized MMR checkpoints

**Source**: `src/storage/snapshot.rs`, `src/rpc/node_rpc_v1.idl`

## Overview

[Section titled “Overview”](#overview)

State sync uses **checkpoints** and **snapshots** to bootstrap new nodes quickly. A snapshot packages a verified checkpoint plus the data needed to prove chain continuity and finalized history membership.

A snapshot includes:

* Block headers from genesis (or a trusted height) to the checkpoint
* Finalized history MMR entries (for membership proofs)
* Checkpoint metadata (height + state root)
* Validator sets for finality verification
* Finality proof for the checkpoint block (if available)

## Checkpoints

[Section titled “Checkpoints”](#checkpoints)

A **checkpoint** is a state root committed at a specific height. It anchors state sync and lets nodes verify they rebuilt the same state.

RPCs:

* `get_checkpoint(height)` → metadata + archive descriptor (if available)
* `list_checkpoints(limit)` → descending list

## Snapshots (Fast Sync)

[Section titled “Snapshots (Fast Sync)”](#snapshots-fast-sync)

There are two ways to consume snapshots:

### 1) Light Snapshot (proof-first)

[Section titled “1) Light Snapshot (proof-first)”](#1-light-snapshot-proof-first)

`get_light_snapshot(height)` returns a compact proof bundle:

* checkpoint metadata
* checkpoint block header
* MMR membership proof for the checkpoint block
* optional finality proof
* validator set

This is used to **verify** a checkpoint against a trusted MMR root.

### 2) Snapshot Chunk Streaming (full state)

[Section titled “2) Snapshot Chunk Streaming (full state)”](#2-snapshot-chunk-streaming-full-state)

`get_snapshot_chunk` streams state entries in chunks:

```plaintext
get_snapshot_chunk({ height, offset, limit })
```

Response includes:

* `state_root` for validation
* `total_entries`
* `entries` (address, key, value)
* `has_more`

For import, admins can call:

```plaintext
import_snapshot_chunk({ height, state_root, entries, finalize })
```

`finalize=true` triggers a state root verification at the end of import.

## Verification Rules

[Section titled “Verification Rules”](#verification-rules)

The snapshot module enforces:

1. Header chain continuity (parent hashes match)
2. MMR root recomputation from entries
3. Finality proof validates against validator set
4. Checkpoint state root matches header state root

If any check fails, the snapshot is rejected.

## Error Cases

[Section titled “Error Cases”](#error-cases)

Common errors include:

* `SNAPSHOT_MMR_ROOT_MISMATCH`
* `SNAPSHOT_MMR_COUNT_MISMATCH`
* `FINALITY_PROOF_INVALID`
* `STATE_ROOT_MISMATCH`

## Related Docs

[Section titled “Related Docs”](#related-docs)

* `docs-site/src/content/docs/upcoming/finalized-mmr-proofs.md`
* `docs/design/light-client-mmr-onchain.md`
* `docs/design/chainstore-hardening.md`

# Txpool Rate Limiting & DoS Guardrails

> Gas-weighted rate limiting and mempool guardrails

**Source**: `src/txpool.rs`, `docs-site/src/content/docs/internals/txpool-policy.md`

## Overview

[Section titled “Overview”](#overview)

The txpool enforces **gas‑weighted rate limiting** to prevent sender‑level DoS and memory exhaustion. This replaces simple count‑based limits as the primary guardrail.

The policy combines:

* Per‑sender **gas budget** (primary limit)
* Per‑sender **tx count** (secondary limit)
* Per‑lane **queue length** (nonce lane guard)
* Global pool size / eviction rules

## Gas‑Weighted Rate Limit (Primary)

[Section titled “Gas‑Weighted Rate Limit (Primary)”](#gasweighted-rate-limit-primary)

Each sender has a budget `max_gas_per_sender`. The pool computes a rate‑limit cost per tx:

```plaintext
rate_limit_cost = base_cost + (gas_limit * weight_bps / 10_000)
```

Defaults (see `txpool::Config`):

* `max_gas_per_sender = 100_000_000`
* `gas_rate_limit_base_cost = 21_000`
* `gas_rate_limit_weight_bps = 10_000` (1:1)

If `current_sender_gas + rate_limit_cost > max_gas_per_sender`, the tx is rejected and the `txpool_gas_rate_limited_total` metric is incremented.

## Secondary Limits

[Section titled “Secondary Limits”](#secondary-limits)

These limits apply after the gas‑budget check:

* `max_txs_per_sender`: cap on total pending txs per sender
* `max_txs_per_lane`: cap on pending txs in a (sender, nonce\_space) lane
* `max_lanes_per_sender`: cap on lane proliferation

## Eviction Policy

[Section titled “Eviction Policy”](#eviction-policy)

When the pool exceeds `max_txs`, eviction removes the **lowest fee** entries first, using `(max_fee, priority_tip)` as the primary key and `(inserted_at_ms, tx_hash)` as a tiebreaker.

Sealed (private) mempool entries are evicted FIFO by arrival time.

## Metrics

[Section titled “Metrics”](#metrics)

* `txpool_gas_rate_limited_total`: total gas‑rate‑limit rejections
* `txpool_inserts_total`: total inserts by result (inserted, rejected, evicted)

## Tuning Guidance

[Section titled “Tuning Guidance”](#tuning-guidance)

If the pool is too permissive (spam risk):

* Lower `max_gas_per_sender`
* Increase `gas_rate_limit_base_cost`
* Decrease `max_txs_per_sender`

If the pool is too strict (legit txs rejected):

* Increase `max_gas_per_sender`
* Lower `gas_rate_limit_base_cost`

## Related Docs

[Section titled “Related Docs”](#related-docs)

* `docs-site/src/content/docs/internals/txpool-policy.md`
* `docs-site/src/content/docs/reference/rpc-api.md`

# VM Tooling & Test Harness

> CLI tools and in-memory harness for contract testing

**Source**: `crates/vm-tooling`, `crates/vm-test-harness`

## Overview

[Section titled “Overview”](#overview)

Ashen ships two developer utilities for contract work:

* `vm-tooling`: CLI for validation, disassembly, tracing, gas profiling, and tier predecode.
* `vm-test-harness`: in-memory host for running Zig/Rust contracts without a full node.

## vm-tooling CLI

[Section titled “vm-tooling CLI”](#vm-tooling-cli)

Binary: `vm-tooling` (crate: `crates/vm-tooling`).

### Common Commands

[Section titled “Common Commands”](#common-commands)

#### Deploy manifest

[Section titled “Deploy manifest”](#deploy-manifest)

```plaintext
vm-tooling deploy-manifest --out deploy.json
```

#### ELF validation

[Section titled “ELF validation”](#elf-validation)

```plaintext
vm-tooling elf-validate --elf contract.elf --manifest deploy.json
```

#### Disassembly

[Section titled “Disassembly”](#disassembly)

```plaintext
vm-tooling disasm --file contract.elf --start 0x0 --len 256
```

#### Trace execution

[Section titled “Trace execution”](#trace-execution)

```plaintext
vm-tooling trace --file contract.elf --entry 0x0 --gas 1000000 --calldata-hex 0x...
```

#### Gas schedule dump

[Section titled “Gas schedule dump”](#gas-schedule-dump)

```plaintext
vm-tooling gas --json
```

#### Code cache stats

[Section titled “Code cache stats”](#code-cache-stats)

```plaintext
vm-tooling cache-stats --max-entries 1024 --max-bytes 268435456
```

#### Predecode to tier

[Section titled “Predecode to tier”](#predecode-to-tier)

```plaintext
vm-tooling predecode --elf contract.elf --tier jit --out contract.jit
vm-tooling predecode --elf contract.elf --tier aot --out contract.aot
```

#### Gas profiling

[Section titled “Gas profiling”](#gas-profiling)

```plaintext
vm-tooling gas-profile --file contract.elf --gas 1000000 --trace-out gas.json
```

#### Gas budgets

[Section titled “Gas budgets”](#gas-budgets)

```plaintext
vm-tooling gas-budget-check --config .gas-budgets.toml --contracts-dir contracts/
```

#### Conformance corpus

[Section titled “Conformance corpus”](#conformance-corpus)

```plaintext
vm-tooling corpus-freeze --out corpus/ --cases 1000
vm-tooling corpus-run --dir corpus/ --tier interpreter
```

## vm-test-harness

[Section titled “vm-test-harness”](#vm-test-harness)

Crate: `crates/vm-test-harness`.

It provides a lightweight host for executing contracts with deterministic storage, events, and result parsing.

### Example

[Section titled “Example”](#example)

```rust
use vm_test_harness::{ContractHarness, TestHost, TestAccounts};
use vm_test_harness::{assert_call_ok, build_calldata};


let accounts = TestAccounts::default();
let mut host = TestHost::new();
host.seed_default_balances(&accounts);


let harness = ContractHarness::from_zig_artifact(
    "contracts/my_token/zig-out/bin/my_token",
)
.expect("artifact exists")
.expect("load contract");


let calldata = build_calldata(*b"MINT", &accounts.alice);
let result = harness.call(&mut host, &accounts.alice, b"my_token", &calldata, 1_000_000);
assert_call_ok(&result, "mint should succeed");
```

### Assertions and Fixtures

[Section titled “Assertions and Fixtures”](#assertions-and-fixtures)

The harness includes helpers for:

* Event emission checks
* Storage assertions
* Host state fixtures
* ABI-compatible calldata builders

## Related Docs

[Section titled “Related Docs”](#related-docs)

* `docs/design/gas-profiler-flame-graphs.md`
* `docs/design/simulation-mode.md`
* `docs/design/cross-contract-call-tracing.md`