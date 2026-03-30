# Source: https://docs.espressosys.com/network/concepts/rollup-architecture.md

# Rollup Architecture

Espresso is the base layer for rollups. In order to understand what Espresso does and what benefits it brings, you must understand how rollups work at the high level.

### What is a Rollup?

A rollup is a type of blockchain that runs on top of another blockchain (called the parent chain or settlement layer). Instead of executing all transactions directly on the parent chain, the rollup executes transactions off-chain and then posts a compressed record of those transactions back to the parent.

This approach brings two key benefits:

* Scalability – rollups process many more transactions than the parent chain could handle on its own.
* Security – rollups inherit security from their parent chain, since all rollup data is anchored there.

There are two main types of rollups:

* Optimistic Rollups – batches are assumed valid by default, but can be challenged during a fraud window (typically \~7 days). Examples: Optimism, Arbitrum.
* ZK Rollups – each batch includes a cryptographic proof (a zero-knowledge proof) showing that the transactions were executed correctly. No challenge period is required. Examples: zkSync, Starknet.

### Finality vs. Settlement

These two concepts are central in the rollup ecosystem, but they’re often confused or misused.

#### Finality

Finality means you can consider a transaction done and no longer subject to reversal. In most rollups, this happens when your transaction is included in a batch and that batch is posted to the parent chain (e.g., Ethereum).

With Espresso, you don’t need to wait for the batch to reach the parent chain. Espresso provides its own confirmations, **backed by BFT consensus**, so you can trust your transaction as final immediately, knowing it will eventually be included on the parent chain.

#### Settlement

Settlement is about proving correctness to the parent chain. Once a batch is posted, someone posts a corresponding state commitment, and there's typically a 7-day challenge window where anyone can submit a fraud proof if the state is incorrect.

Importantly, this does not affect rollup execution: the rollup itself won’t roll back or halt because of a fraud proof. The challenge process only ensures that the state recorded on the parent chain matches what the rollup actually computed.

### The Transaction Lifecycle in a Rollup

In a usual rollup (not integrated with Espresso), the transaction flow is:

**1. User submits transactions**

The user signs and sends a transaction to the rollup.

**2. Sequencer**

The sequencer collects transactions, orders them, and produces blocks quickly.

**3. Batch posting**

The sequencer (or a separate batch poster) sends batches of ordered transactions to the parent chain for security anchoring. **The transactions included in the batch are considered final**.

**4. Verification on parent chain**

* For optimistic rollups, batches can be challenged during a fraud proof period.
* For ZK rollups, batches include a ZK proof that is verified immediately.

**5. Settlement**

After the fraud period (optimistic) or proof verification (ZK), **the batch is considered settled** and secured by the parent chain.

### The Transaction Lifecycle in an Espresso-integrated Rollup

**1. User submits a transaction**

The user signs and sends a transaction to the rollup.

**2. Sequencer**

The chain's sequencer, produces blocks.

**3.1 Confirmations (powered by Espresso confirmations)**

Espresso finalizes the ordering of transactions. The Espresso Network produces a block containing the transaction and finalizes its position in the global order.

**3.2 Data Availability (optional)**

If Espresso is also used as a DA layer, the transaction data is stored and made retrievable by Espresso’s DA.

If not, DA comes from the rollup’s parent chain or another DA layer (e.g., Celestia, EigenDA).

**NOTE:** If you are using Espresso for confirmations, Espresso DA comes *for free*.

**4. Caff Node derives chain state**

Caff Nodes (which stand for Caffeinated Nodes), which are full nodes instrumeted to read from the Espresso Network, derive execution results and make them available through an RPC (the exact same RPC endpoints you would use in a standard EVM RPC). Applications can query Caff Nodes to know instantly whether a transaction is confirmed.

**6. Batch posting to parent chain**

A batch poster sends transactions to the parent chain, along with a proof that these transactions have been confirmed in Espresso.

**NOTE:** This proof can take the form of a ZK proof, a signature from secure hardware (TEE), or something else. The parent chain immediately verifies this proof before finalizing the batch.

**7. Parent chain verification**

* On an optimistic rollup, the batch is subject to a fraud-proof window.
* On a ZK rollup, the validity proof is checked immediately.

**8. Settlement**

Once the fraud period ends (optimistic) or proof verification passes (ZK), the batch is settled on the parent chain.

The Espresso confirmation obtained in step 4 remains consistent with this final state, **assuming no bugs in the Caff Node**.

### What Espresso Is vs. What Espresso Is Not

Espresso is designed to solve a very specific problem in the rollup stack: ordering and fast confirmations. It is not responsible for execution. Understanding this distinction is key to knowing what Espresso can (and cannot) guarantee for your application.

#### What Espresso Is: The Ordering Layer

Espresso provides a shared global ordering service through its HotShot consensus protocol.

* Espresso’s job is to make sure everyone agrees, within seconds, which transaction came first and what order they should be executed in.
* Once Espresso confirms an ordering, sequencers can’t retroactively change it. This prevents manipulation like censorship, or reorgs at the ordering layer.
* Apps can rely on Espresso for fast, secure provisional confirmations before finality on the parent chain (e.g., Ethereum).

#### What Espresso Is Not: The Execution Layer

Espresso does not execute transactions. Execution still happens on the rollup itself and ultimately settles on the parent chain (Ethereum).

* Espresso does not check whether a transaction is validly executed — that’s the job of the rollup’s execution environment.

### Security Assumptions

**- Ordering guarantees:** Espresso is guaranteed to provide consistent ordering, as long as at least two-thirds of the staked tokens are controlled by honest parties.

**- Execution finality:** The ultimate correctness of transaction execution and cross-chain asset movements still depends on rollup execution and L1 settlement.

**- Enforce Espresso confirmations:**: The rollup's inbox has to correctly enforce Espresso confirmations on the batches being posted (e.g. by verifying a TEE attestation from the batcher), otherwise there is no guarantee that what the Caff Node executes is the same as what the L1 eventually settles. Also, there has to be at least one correct batcher, otherwise you can hit force inclusion that breaks Espresso confirmations.

**- Trusting Caff Nodes:** Interacting with Espresso typically happens through Caff Nodes. Assuming the code of the Caff Node has no bugs, you can rely on the execution results without waiting for L1 finality.

### The Role of Trusted Execution Environments (TEEs)

A TEE is a secure enclave inside modern processors (such as Intel SGX or AMD SEV) that guarantees:

* **Code integrity** – only the expected code can run inside the enclave.
* **Data confidentiality** – no one, not even the machine’s operator, can tamper with or inspect the enclave’s internal state.
* **Remote attestation** – anyone can verify that the enclave is running the correct code.

Espresso’s Caff Nodes and batch posters use TEEs to ensure that transaction ordering and execution are correct and cannot be tampered with by malicious operators. TEEs are powerful but not magic. They rely on hardware security guarantees from chip manufacturers. If a TEE is compromised (e.g., through a new hardware attack), the guarantees may break.
