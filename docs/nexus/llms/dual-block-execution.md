# Source: https://docs.nexus.xyz/architecture/dual-block-execution.md

# Dual-Block Execution

### Dual-Block Execution

To achieve predictable performance, NexusCore will participate in a dual-block architecture:

* NexusCore blocks will execute continuously at 50–100 ms intervals for real-time trading and risk operations.
* NexusEVM blocks will occur every 4–10 Core blocks, providing synchronization and composability between NexusCore and NexusEVM.

This scheduling will ensure that NexusCore operations never wait for EVM overhead, maintaining deterministic latency across financial workloads.

<figure><img src="https://1928578818-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fmi9nUlZMKVkCp0Tab0VD%2Fuploads%2FXw9RXWHQi0nPP0ks1adY%2F10.png?alt=media&#x26;token=947e214d-6e30-400f-aee3-9af22438a84d" alt=""><figcaption><p>To achieve high performance, Nexus introduces a high-frequency dual-block architecture. <br>It features fast NexusCore mini-blocks providing high-frequency and low-latency orderbook transactions, <br>and slower NexusEVM blocks featuring the full programmability of the EVM.</p></figcaption></figure>

### Benefits

* Sub-100 ms latency for trading and risk computation
* Parallelized throughput scaling with hardware cores
* Native economic integration with validator and fee rewards
* Composable APIs bridging high-frequency execution with programmable contracts

NexusCore will transform the base chain into a verifiable financial engine, capable of supporting institutional-grade market infrastructure on-chain.
