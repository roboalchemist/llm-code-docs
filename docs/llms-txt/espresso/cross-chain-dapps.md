# Source: https://docs.espressosys.com/network/concepts/dapp/cross-chain-dapps.md

# Cross-chain Apps

Cross-chain apps require fast and reliable messaging between rollups. Today, most rollups rely on their parent chain (e.g., Ethereum) to finalize transactions before messages can safely be passed — a process that can take minutes to hours.

Espresso shortens this cycle by providing fast confirmations that middlewares like Hyperlane, intents frameworks, and solvers can rely on to bridge state between chains safely and quickly.

### Message Passing Protocol (like Hyperlane)

Espresso helps message passing protocols like Hyperlane at verious stages:

* Source chain: The validator reads events directly from a Caff Node, which exposes Espresso confirmations.
* Destination chain: Once Espresso confirms a transaction on the source, the relayer can immediately submit the corresponding message to the mailbox contract on the destination chain.

The message can be trusted as correct execution, since the Caff Node derives state directly from the Espresso Network.

#### Cross-chain Data Flow with Espresso + Hyperlane

Here’s the typical flow of a cross-chain message (e.g., Rari → Appchain):

**1. User transaction on source chain (Rari)**

User interacts with a dapp contract that calls the Hyperlane `Mailbox.dispatch` function.

**2. Espresso confirmation**

The transaction is confirmed by Espresso’s HotShot consensus.

**3. The Caff Node exposes the confirmed state.**

Validator picks up the message

Hyperlane’s validator observes the `Dispatch` event from the source chain Mailbox using the Caff Node.

**4. Relayer submits to destination**

Hyperlane’s relayer submits the message to the destination chain’s Mailbox contract.

**5. Dapp contract executes**

The destination dapp receives the message via `handle()` and executes the requested logic.

### Espresso + Intents Frameworks

A growing design pattern in Web3 is the intents-based architecture, exemplified by the Open Intents Framework (OIF):

* Users express what they want to achieve (e.g., “swap token A on Rari for token B on Appchain”).
* Solver networks compete to fulfill these intents efficiently.
* To act correctly, solvers must have access to the latest valid state of both the source and destination chains.

#### Where Espresso fits in:

By querying Caff Nodes, solvers can access fast, correct rollup state without waiting for finality on the parent chain. This significantly reduces both latency and execution risk, enabling cross-rollup intents to be executed safely and quickly.

### Beyond Intents: Other Middlewares

Espresso confirmations extend far beyond Hyperlane or intent frameworks. Middleware protocols such as:

* Across
* Relay (transaction relayers)
* Custom bridges

They all rely on having fast and reliable information about the source-chain state. By integrating with Caff Nodes, they can:

* Cut down the delay between user action and message delivery.
* Provide a Web2-like user experience with near-instant cross-rollup confirmation.
