# Source: https://docs.carv.io/d.a.t.a.-ai-framework/architecture.md

# Source: https://docs.carv.io/svm-ai-agentic-chain/introduction/architecture.md

# Architecture

CARV SVM Chain is an **SVM Layer 2 solution** built on Ethereum Layer 1, leveraging **Decoupled SVM Rollup Architecture** to achieve unparalleled scalability, security, and cross-layer operability. This architecture redefines the integration of SVM into non-Solana ecosystems, enabling a seamless, high-performance environment for AI agents.

### **Key Features**:

1. **Decoupled SVM Framework**:
   1. Enables the deployment of SVM rollups on Ethereum without dependency on Solana’s Layer 1.
   2. Provides high TPS, native fraud-proof mechanisms, and reduced data availability (DA) costs.
2. **Merklization**:
   1. Implements **Merkle Patricia Trie (MPT)** and **UniqueEntry** within the SVM to solve Merklization challenges.
   2. Features state root verification, inclusion proofs, and stateless execution to improve cross-layer operations and enhance bridge security.
3. **Horizontal Scaling**:
   1. Scales transaction processing by distributing workload across nodes using a **Producer-Consumer architecture**, **SIMD83 optimization**, and **TPU distribution**.
   2. Achieves theoretically infinite growth by allowing each node to handle a portion of transactions independently.
4. **Rollup Integration**:
   1. CARV SVM Layer 2 integrates directly with Ethereum’s Layer 1, ensuring settlement, state root verification, and zk-rollup proof submission for added security.
