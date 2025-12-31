# Source: https://docs.carv.io/svm-ai-agentic-chain/quick-start/writing-to-the-network.md

# Writing to the Network

Now that we understand how to read data from the CARV SVM Chain, let’s learn how to write data. On CARV SVM Chain, transactions consist of instructions—just like on Solana—but they benefit from CARV’s Layer 2 architecture. This architecture offers faster finality, lower costs, and seamless integration with Ethereum’s security guarantees.&#x20;

Let’s explore a common operation: transferring SOL, to understand how transactions work on CARV SVM Chain.

## **Transfer SOL**

To perform a simple transfer of SOL from one account to another, we invoke the `transfer` instruction on the System Program. Here’s how you can do it:

```javascript
import {
    LAMPORTS_PER_SOL, SystemProgram, Transaction,
    sendAndConfirmTransaction, Keypair,
} from "@solana/web3.js";

// Connect to CARV SVM Chain's RPC endpointconst rpcUrl = "https://rpc.testnet.carv.io/rpc";
const connection = new pg.Connection(rpcUrl);

// Get sender's keypair from the playground wallet
const sender = pg.wallet.keypair;

// Generate a new keypair for the receiver
const receiver = new Keypair();

// Create the transfer instruction
const transferInstruction = SystemProgram.transfer({
    fromPubkey: sender.publicKey, toPubkey: receiver.publicKey, lamports: 0.01 * LAMPORTS_PER_SOL,  // Transfer 0.01 SOL
});

// Add the instruction to a new transaction
const transaction = new Transaction().add(transferInstruction);

// Send and confirm the transaction
const transactionSignature = await sendAndConfirmTransaction(
    connection,
    transaction,
    [sender]
);

// Log the transaction URL using CARV’s explorer
console.log("Transaction Signature:",`https://explorer.ops.soo.network/?cluster=custom&customUrl=https%3A%2F%2Frpc.carv.testnet.soo.network%2Frpc%2Fcarv-McPrlbfMcW0ggpkvr07Tjs2YfviwpHaI/${transactionSignature}`);
```

Key Concepts:

* Creating Instructions: Specifies what the transaction will do (e.g., transfer funds).
* Building Transactions: Combines one or more instructions.
* Sending and Confirming: Executes the transaction and verifies its success.
* Explorer Integration: Links to CARV’s explorer for transaction details.

When you run this code, you’ll see a transaction signature and a link to view it in CARV’s explorer. Clicking the link provides transaction details, including the fast confirmation enabled by CARV SVM Chain.
