# Source: https://docs.carv.io/svm-ai-agentic-chain/quick-start/reading-from-carv-svm-network.md

# Reading from CARV SVM Network

Let’s dive into how data operates on the CARV SVM Network. On CARV SVM, all data is organized within accounts—unique containers that store either data or program code. This guide will walk you through understanding and accessing the various types of accounts.

## **Read a Basic Account**

Let’s start with the simplest type of account on the CARV SVM Chain—your wallet. Open the following example and connect to the CARV SVM Chain using the RPC endpoint <https://rpc.testnet.carv.io/rpc>:

```javascript
// Connect to CARV SVM Chain's RPC endpointconst rpcUrl = "https://rpc.testnet.carv.io/rpc";
const connection = new pg.Connection(rpcUrl);

// Get your wallet's public key - this is your account's addressconst address = pg.wallet.publicKey;

// Fetch the account's information from the networkconst accountInfo = await connection.getAccountInfo(address);

// Display the account's detailsconsole.log("Your Wallet Account Info:");
console.log("======================");
console.log("Address:", address.toBase58());
console.log("Balance:", accountInfo.lamports / 1000000000, "SOL");
console.log("Owner:", accountInfo.owner.toBase58());
console.log("Executable:", accountInfo.executable);
console.log("Data length:", accountInfo.data.length);

// Set up a listener for account changesconsole.log("\nWatching for balance changes...");
const subscriptionId = connection.onAccountChange(
    address,(updatedInfo, context) => {console.log("\nBalance updated!");console.log("New balance:", updatedInfo.lamports / 1000000000, "SOL");
    }
);
```

Example Output:

```yaml
Your Wallet Account Info:
======================
Address: ATxydRH5uT8xivYQGH7e6KgFNkPvEn7UKMmABtFpgNkz
Balance: 1 SOL
Owner: 11111111111111111111111111111111Executable: falseData length: 0
```

Understanding the Output:

* Address: Your unique identifier on the CARV SVM Chain.
* Balance: Displays holdings in SOL (1 SOL = 1,000,000,000 lamports).
* Owner: All `1`s represent the System Program, which manages basic accounts.
* Executable: `false` indicates this account stores data, not code.
* Data length: `0` is standard for accounts holding only SOL balances.

## **Explore Token Accounts**

Now, let’s examine token accounts on the CARV SVM Chain:

```javascript
import { TOKEN_PROGRAM_ID } from "@solana/spl-token";

// Fetch information about the Token Programconsole.log("Token Program Info:");
console.log("=================");
const tokenProgramInfo = await connection.getAccountInfo(TOKEN_PROGRAM_ID);
console.log("Is executable:", tokenProgramInfo.executable);
console.log("Data length:", tokenProgramInfo.data.length);

// Fetch all token accounts owned by your walletconsole.log("\nYour Token Accounts:");
console.log("==================");
const tokenAccounts = await connection.getTokenAccountsByOwner(
    pg.wallet.publicKey,
    { programId: TOKEN_PROGRAM_ID }
);

if (tokenAccounts.value.length === 0) {console.log("No token accounts found - try creating one first!");
} else {
    tokenAccounts.value.forEach((account, i) => {console.log(`\nToken Account ${i + 1}:`);console.log("Address:", account.pubkey.toBase58());console.log("Data size:", account.account.data.length);
    });
}
```

Example Output:

```yaml
Token Program Info:
=================
Is executable: true
Data length: 133352

Your Token Accounts:
==================
No token accounts found - try creating one first!
```

Understanding the Output:

* Token Program:
  * Is executable: `true` because it contains the program code.
  * Data length: Indicates the size of program instructions.
* Token Accounts:
  * Lists all token accounts owned by your wallet.
  * If none are found, you'll need to create one first.

***

**Find Program Accounts**

You can also query all accounts owned by a specific program on the CARV SVM Chain:

```javascript
import { TOKEN_PROGRAM_ID } from "@solana/spl-token";
import { PublicKey } from "@solana/web3.js";

async function scanProgramAccounts(programId) {
    console.log(`Scanning accounts owned by program: ${programId.toString()}`);
    console.log("==========================================");
    const accounts = await connection.getProgramAccounts(programId, {
        dataSlice: { offset: 0, length: 0 }, filters: []
    });
    console.log(`Found ${accounts.length} accounts\n`);
    accounts.slice(0, 5).forEach((account, i) => {
        console.log(`Account ${i + 1}:`); 
        console.log("Address:", account.pubkey.toBase58()); 
        console.log("Balance:", account.account.lamports / 1000000000, "SOL"); 
        console.log("Data length:", account.account.data.length); console.log("-------------------");
    });
}

// Look at Token Program accountsawait scanProgramAccounts(TOKEN_PROGRAM_ID);
```

Example Output:

* Accounts Owned: Displays the number of accounts a program owns.
* Account Details: Shows their addresses, balances, and data sizes.

***

**Monitor Network Activity**

Real-time monitoring is essential for responsive applications. Use the following code to track changes in account balances and transactions:

```javascript
console.log("Starting transaction and account monitoring...");
console.log("============================================");

// Watch for account balance changes
const accountSub = connection.onAccountChange(
    pg.wallet.publicKey, (accountInfo, context) => {
        console.log("\nAccount Updated!");
        console.log("New balance:", accountInfo.lamports / 1000000000, "SOL");
        console.log("Slot:", context.slot);
    }
);

// Watch for transaction confirmations
const signatureSub = connection.onSignature(
    await connection.requestAirdrop(pg.wallet.publicKey, 1000000000), (signatureResult, context) => {
        console.log("\nTransaction Confirmed!");
        console.log("Signature:", signatureResult);
        console.log("Slot:", context.slot);
    }
);

console.log("Monitoring active - try requesting an airdrop to see updates!");
```

Example Output:

* Real-time balance updates when account changes occur.
* Transaction confirmations with signature and slot details.

***

**Next Steps**

Now that you understand how to read and monitor accounts on the CARV SVM Chain, you're ready to explore writing data through transactions. Continue to the next section to start deploying your own projects on the network.
