# Source: https://docs.espressosys.com/network/concepts/dapp/single-chain-dapps.md

# Single-chain Apps

Building a decentralized application (dapp) on a rollup integrated with Espresso **unlocks faster, more reliable confirmations without changing how you interact with the chain at the RPC level.**

Normally, rollup applications rely on the parent chain (e.g., Ethereum) to provide finality. For optimistic rollups, this can take up a few hours.

For most dapps, waiting for this kind of finality is too slow. Users need faster confirmations for actions like:

* Sending tokens
* Swapping in a DEX
* Playing a game
* Interacting with NFTs

Espresso provides fast, trust-minimized confirmations that dapps can rely on immediately. **By reading from a Caff Node, your app can present users with consistent and near-instant transaction results**.

### Typical Data Flow

Let’s walk through a transaction step by step:

**1. User submits a transaction**

The user signs and submits a transaction through your dapp’s frontend.

**2. Sequencing**

The transaction is forwarded to the rollup’s sequencer (which could be centralized or decentralized). Anyway, the Espresso Network provides confirmation of the transaction ordering.

**3. Caff Node derives the state**

The Caff Node listens to Espresso confirmations and derives the correct rollup state in real time.

It exposes this state via the **standard Ethereum-style JSON-RPC interface**.

**4. Frontend shows confirmation**

Your dapp queries the Caff Node just like it would a normal RPC.

Because Espresso confirmations are fast, the user sees their transaction confirmed almost instantly.

**5. Parent chain**

Later, the batch is posted to the parent chain (Ethereum, Arbitrum, etc.) but your app doesn’t need to wait for it to provide a smooth UX.

### Example: Token Swap on Rari

Suppose you’re building a DEX on Rari (an L3 integrated with Espresso).

**- Without Espresso:** A user swaps tokens, but your frontend can only show “pending” until the rollup batch is posted and eventually finalized on Arbitrum. This could take minutes to hours.

**- With Espresso:** The user submits the swap, Espresso confirms it within seconds, and your frontend shows the updated balances immediately by querying a Caff Node.

Later, Arbitrum finality and settlement guarantees long-term security, but the user never notices the delay.
