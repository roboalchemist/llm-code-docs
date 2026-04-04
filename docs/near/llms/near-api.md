# Source: https://docs.near.org/tools/near-api.md

---
id: near-api
title: NEAR API
sidebar_label: NEAR API
description: "Learn to use APIs in JavaScript, Rust, and Python to interact with the blockchain."
---




We offer a collection of language-specific libraries that allow developers to interact with the NEAR blockchain from both frontend and backend applications. The different APIs allow you to perform a variety of actions on the NEAR blockchain, including but not limited to:

1. Create and manage NEAR accounts
2. Call functions on smart contracts
3. Transfer tokens, including native NEAR, Fungible Tokens, Non-Fungible Tokens
4. Sign transactions/meta-transactions/messages and broadcasting them to the network
5. Deploy smart contracts

---

## Available APIs

We have APIs available for Javascript, Rust, and Python. Add them to your project using the following commands:

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

  ```bash
  npm i near-api-js
  ```

  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">

  ```bash
  npm i near-kit
  ```

  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```bash
  cargo add near-api
  ```
  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```shell
  pip install py-near
  ```
  </TabItem>
</Tabs>

:::tip Wallet Integration

If you are building a web app and need to add Wallet Login on it you will instead need a [`Wallet Connector`](../web3-apps/tutorials/wallet-login)

:::

---

## Account

### Get Balance {#get-balance}

Gets the available and staked balance of an account in yoctoNEAR.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
import { Account, JsonRpcProvider } from "near-api-js";
import { NEAR, FungibleToken } from "near-api-js/tokens";
import { USDT } from "near-api-js/tokens/testnet";

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const accountId: string = 'influencer.testnet';
const account = new Account(accountId, provider);

// ------- Fetch NEAR tokens balance -------
const nearTokensBalanceInt: bigint = await account.getBalance(NEAR);
console.log("NEAR: ", NEAR.toDecimal(nearTokensBalanceInt, 2));

// ------- Fetch USDT tokens balance -------
const usdtTokensBalanceInt: bigint = await account.getBalance(USDT);
console.log("USDT: ", USDT.toDecimal(usdtTokensBalanceInt, 2));

// ------- Fetch REF tokens balance in the smallest units as BigInt -------
const REF = new FungibleToken("ref.fakes.testnet", {
  decimals: 18,
  symbol: "REF",
  name: "REF Token",
});

const refTokensBalanceInt: bigint = await account.getBalance(REF);
console.log("REF: ", REF.toDecimal(refTokensBalanceInt, 2));

```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
import { Near } from "near-kit";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();

// Create a connection to testnet (no signing needed for view operations)
const near = new Near({ network: "testnet" });

// Get the account ID from environment or use a default
const accountId = process.env.ACCOUNT_ID || "example-account.testnet";

// Get NEAR balance for the account
const balance = await near.getBalance(accountId);

console.log(`Account: ${accountId}`);
console.log(`NEAR Balance: ${balance} NEAR`);

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
use near_api::{Account, AccountId, NetworkConfig, Tokens};

#[tokio::main]
async fn main() {
    let my_account_id: AccountId = "example-account.testnet".parse().unwrap();
    // Create an account object
    let my_account = Account(my_account_id.clone());

    // Create a connection to the NEAR testnet
    let network = NetworkConfig::testnet();

    // Gets the available, and staked balance in yoctoNEAR
    let near_balance = Tokens::account(my_account_id.clone())
        .near_balance()
        .fetch_from(&network)
        .await
        .unwrap();
    println!("{:?}", near_balance);

    // Account's state, including its code hash and storage usage
    let account_info = my_account.view().fetch_from(&network).await.unwrap();
    println!("{:?}", account_info);
}

```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

    ```python
    from py_near.account import Account

    account = Account(account_id="example-account.testnet", rpc_addr="https://rpc.testnet.pagoda.co")
    await account.startup()

    account_balance = account.get_balance()
    ```
  </TabItem>
</Tabs>

<hr class="subsection" />

### Get State {#get-state}

Get basic account information, such as its code hash and storage usage.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

  ```
import { Account, JsonRpcProvider } from "near-api-js";

// Option 1: Gather details through the RPC Provider
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

const rpcState = await provider.viewAccount({accountId: "example-account.testnet"});
console.log(rpcState);

// Option 2: Use an Account object
const account = new Account("example-account.testnet", provider);
const accountState = await account.getState();

console.log(accountState);

```

  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">

  ```
import { Near } from "near-kit";

// Create a connection to testnet
const near = new Near({ network: "testnet" });

// Get account balance using the Near instance
const accountId = "example-account.testnet";
const balance = await near.getBalance(accountId);

console.log(`Account: ${accountId}`);
console.log(`Balance: ${balance} NEAR`);

```

  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">
  
  ```
    let account_info = my_account.view().fetch_from(&network).await.unwrap();
    println!("{:?}", account_info);
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

    ```python
    from py_near.account import Account

    account = Account(account_id="example-account.testnet", rpc_addr="https://rpc.testnet.pagoda.co")
    await account.startup()

    account_state = account.fetch_state()
    ```
  </TabItem>
</Tabs>

<hr class="subsection" />

### Create Named Account {#create-named-account}

To create a named account like `user.testnet`, you need to call the `create_account` function on `near` (or `testnet`), passing as parameters the new account ID, and a public key to add as [FullAccess key](/protocol/access-keys#full-access-keys)

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

  ```
import dotenv from "dotenv";
import { Account, JsonRpcProvider, KeyPair, KeyPairString, nearToYocto } from "near-api-js";

dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const account = new Account(accountId, provider, privateKey); // example-account.testnet

// Generate a new accountId and key
const newAccountId: string = Date.now() + ".testnet";
const keyPair = KeyPair.fromRandom("ed25519");
const publicKey: string = keyPair.getPublicKey().toString();

await account.createAccount({
  newAccountId,
  publicKey,
  nearToTransfer: nearToYocto("0")
});

console.log(`Created ${newAccountId} with private key ${keyPair.toString()}`);

// Option 2: Call `testnet` directly
const newAccountId2: string = Date.now() + ".testnet";

await account.callFunction({
  contractId: "testnet",
  methodName: "create_account",
  args: {
    "new_account_id": newAccountId2,
    "new_public_key": publicKey
  }
});

console.log(`Created account ${newAccountId2} with privateKey: ${keyPair.toString()}`);

```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">

  ```
import { Near, generateKey } from "near-kit";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Generate a new key pair for the top-level account
const keyPair = generateKey();
const publicKey = keyPair.publicKey.toString();

// Create a unique top-level account name using timestamp
const newAccountId = `${Date.now()}.testnet`;

// Create the top-level account by calling the testnet contract
await near.call("testnet", "create_account", {
  new_account_id: newAccountId,
  new_public_key: publicKey,
});

console.log(`Created top-level account: ${newAccountId}`);
console.log(`Private key: ${keyPair.secretKey}`);

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    let private_key = signer::generate_secret_key().unwrap();
    let create_account_result = Account::create_account(new_account_id.clone()) // example-account.testnet
        .fund_myself(
            account_id.clone(),
            NearToken::from_millinear(100), // Initial balance for new account in yoctoNEAR
        )
        .public_key(private_key.public_key()).unwrap()
        .with_signer(signer.clone()) // Signer is the account that is creating the new account
        .send_to(&network)
        .await
        .unwrap();

    println!("Private key: {:?}", private_key.to_string());
    println!("Public key: {:?}", private_key.public_key().to_string());
    println!("{:?}", create_account_result);

    // Create a sub account
```

  <details>
    <summary>Creating an account from a seed phrase</summary>

    You can also create an account via a randomly generated seed phrase.

    ```
    let (seed_phrase, seed_pk) = signer::generate_seed_phrase().unwrap();
    let create_account_result = Account::create_account(new_account_id.clone()) // example-account.testnet
        .fund_myself(
            account_id.clone(),
            NearToken::from_millinear(100), // Initial balance for new account in yoctoNEAR
        )
        .public_key(seed_pk).unwrap()
        .with_signer(signer.clone()) // Signer is the account that is creating the new account
        .send_to(&network)
        .await
        .unwrap();

    println!("Seed phrase: {:?}", seed_phrase);
    println!("{:?}", create_account_result);
}

```

  </details>

  </TabItem>
  <TabItem value="python" label="🐍 py-near">
  
    ```python
    await account.function_call("testnet", "create_account", {"new_account_id": "example-account.testnet", "new_public_key": "ed25519:..."}, "30000000000000", 1 * NEAR)
    ```

  </TabItem>

</Tabs>

<hr class="subsection" />

### Create Sub-Account {#create-sub-account}

Accounts on NEAR can create sub-accounts under their own namespace, which is useful for organizing accounts by purpose — for example, `project.user.testnet`.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

  ```
import dotenv from "dotenv";
import { Account, JsonRpcProvider, KeyPair, KeyPairString, nearToYocto } from "near-api-js";

dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const account = new Account(accountId, provider, privateKey); // example-account.testnet

// Generate a new account prefix and key pair
const prefix: string = Date.now().toString();
const keyPair = KeyPair.fromRandom("ed25519");
const publicKey: string = keyPair.getPublicKey().toString();

await account.createSubAccount({
  accountOrPrefix: prefix,    // prefix for the sub account (e.g. sub.near.testnet)
  publicKey, // ed25519:2ASWc...
  nearToTransfer: nearToYocto("0") // Initial balance for new account in yoctoNEAR
});

console.log(`Created ${prefix}.${accountId} with private key ${keyPair.toString()}`);

```


  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">

  ```
import { Near, generateKey } from "near-kit";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Generate a new key pair for the subaccount
const keyPair = generateKey();
const publicKey = keyPair.publicKey.toString();

// Create a unique subaccount name using timestamp
const prefix = Date.now().toString();
const newAccountId = `${prefix}.${accountId}`;

// Create the subaccount using transaction builder with chained actions
await near
  .transaction(accountId)
  .createAccount(newAccountId)
  .transfer(newAccountId, "0.1 NEAR")
  .addKey(publicKey, { type: "fullAccess" })
  .send();

console.log(`Created subaccount: ${newAccountId}`);
console.log(`Private key: ${keyPair.secretKey}`);

```


  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    let private_key = signer::generate_secret_key().unwrap();
    let create_sub_account_result = Account::create_account(sub_account_id.clone()) // sub.example-account.testnet
        .fund_myself(
            account_id.clone(),
            NearToken::from_millinear(100), // Initial balance for sub account in yoctoNEAR
        )
        .public_key(private_key.public_key()).unwrap()
        .with_signer(signer.clone()) // Signer is the account that is creating the sub account
        .send_to(&network)
        .await
        .unwrap();

    println!("Private key: {:?}", private_key.to_string());
    println!("Public key: {:?}", private_key.public_key().to_string());
    println!("{:?}", create_sub_account_result);
}

```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

    Create a sub-account and fund it with your main account:

    ```python
    from py_near.account import Account
    from py_near.dapps.core import NEAR

    account = Account(account_id="example-account.testnet", private_key="ed25519:...", rpc_addr="https://rpc.testnet.pagoda.co")
    await account.startup()

    res = account.create_account(account_id="sub.example-account.testnet", public_key="...", initial_balance=1 * NEAR))
    ```
  </TabItem>
</Tabs>

:::info

Parent accounts have **no control** over their sub-accounts, they are completely independent.

:::

<hr class="subsection" />

### Delete Account {#delete-account}

Accounts on NEAR can delete themselves, transferring any remaining balance to a specified beneficiary account.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

  ```
const accountToDelete = new Account(deleteMe, provider, privateKey);

// Delete the account 
const beneficiary: string = process.env.ACCOUNT_ID!;
await accountToDelete.deleteAccount(beneficiary);
console.log(`Account ${deleteMe} was deleted`);
```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">

  ```
import { Near, generateKey } from "near-kit";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Generate a new key pair for the account to be deleted
const keyPair = generateKey();
const publicKey = keyPair.publicKey.toString();

// Create a unique top-level account name using timestamp
const accountToDelete = `${Date.now()}.testnet`;

// First, create the account by calling the testnet contract
await near.call("testnet", "create_account", {
  new_account_id: accountToDelete,
  new_public_key: publicKey,
});

console.log(`Created account: ${accountToDelete}`);

// Fund the new account so it can pay for the delete transaction
await near.send(accountToDelete, "0.01 NEAR");
console.log(`Funded account with 0.01 NEAR`);

// Create a new Near instance with the new account's key to delete it
const nearForNewAccount = new Near({
  network: "testnet",
  privateKey: keyPair.secretKey,
  defaultSignerId: accountToDelete,
});

// Delete the account, sending remaining balance to beneficiary
await nearForNewAccount
  .transaction(accountToDelete)
  .deleteAccount({ beneficiary: accountId })
  .send();

console.log(`Deleted account: ${accountToDelete}`);
console.log(`Beneficiary: ${accountId}`);

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    // Delete the account with account Id of the account object
    let delete_account_result = account_to_delete
        .delete_account_with_beneficiary(beneficiary_account_id.clone()) // example-beneficiary.testnet
        .with_signer(signer.clone()) // Signer is the account that is being deleted
        .send_to(&network)
        .await
        .unwrap();
    println!("{:?}", delete_account_result);
}

```

  </TabItem>
</Tabs>

:::info
Deleting an account **DOES NOT** affect its sub-accounts - they will remain active.
:::

:::danger The Beneficiary Only Receives NEAR Tokens
Fungible (FTs) or Non-Fungible tokens (NFTs) held by the account **ARE NOT** automatically transferred. These tokens are still associated with the account, even after the account is deleted. Make sure to transfer those assets manually before deletion, or you're risking losing them permanently! Once the account is gone, those assets are effectively stuck unless the same account is recreated by anyone (not necessarily you).
:::

:::danger Make Sure the Beneficiary Account Exists
If the beneficiary account doesn't exist, all NEAR tokens sent to it will be burned. Double-check the account ID before proceeding.
:::

---

## Transactions

### Send Tokens {#send-tokens}

Accounts can transfer different types of tokens to other accounts, including the native NEAR token and [NEP-141](https://github.com/near/NEPs/tree/master/neps/nep-0141.md) fungible tokens.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
import dotenv from "dotenv";
import { Account, JsonRpcProvider, KeyPairString } from "near-api-js";
import { NEAR, FungibleToken } from "near-api-js/tokens";
import { USDT } from "near-api-js/tokens/testnet";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const account = new Account(accountId, provider, privateKey); // example-account.testnet

// ------- Send NEAR tokens to another account -------
const sendNearTokensResult = await account.transfer({
  token: NEAR,
  amount: NEAR.toUnits("0.1"),
  receiverId: "influencer.testnet"
});
console.log(sendNearTokensResult);

// ------- Send USDT tokens to another account -------
// if a user isn't registered, the transfer will fail
// it a user is already registered, we'll just get funds back
await USDT.registerAccount({
  accountIdToRegister: "influencer.testnet" as unknown as Account,
  fundingAccount: account,
}).catch(() => {}); // ignore errors if already registered

// Use https://testnet.rhea.finance/#near|usdtt.fakes.testnet to get USDT token
const sendUsdtTokensResult = await account.transfer({
  token: USDT,
  amount: USDT.toUnits("1"), // Amount of USDT being sent
  receiverId: "influencer.testnet"
});
console.log(sendUsdtTokensResult);

// ------- Send REF tokens to another account -------
// Use https://testnet.rhea.finance/#near|ref.fakes.testnet to get REF tokens
const REF = new FungibleToken("ref.fakes.testnet", {
  decimals: 18,
  symbol: "REF",
  name: "REF Token",
});

await REF.registerAccount({
  accountIdToRegister: "influencer.testnet" as unknown as Account,
  fundingAccount: account,
});

const sendREFsResult = await account.transfer({
  token: REF,
  amount: REF.toUnits("1"), // Amount of REF tokens being sent
  receiverId: "influencer.testnet"
}).catch(() => {}); // ignore errors if already registered

console.log(sendREFsResult);

```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
import { Near } from "near-kit";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Send NEAR tokens to another account
const result = await near.send("receiver-account.testnet", "0.1 NEAR");

console.log("Transfer result:", result);

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    let send_tokens_result = Tokens::account(account_id.clone()) // example-account.testnet
        .send_to("receiver-account.testnet".parse().unwrap())
        .near(NearToken::from_near(1))
        .with_signer(signer.clone())
        .send_to(&network)
        .await
        .unwrap();
    println!("{:?}", send_tokens_result);
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

    ```python
    from py_near.account import Account
    from py_near.dapps.core import NEAR

    account = Account(account_id="example-account.testnet", private_key="ed25519:...", rpc_addr="https://rpc.testnet.pagoda.co")
    await account.startup()

    await account.send_money("receiver-account.testnet", 1 * NEAR))
    ```
  </TabItem>
</Tabs>

<hr class="subsection" />

### Call Function

A smart contract exposes its methods, and making a function call that modifies state requires a `Signer`/`KeyPair`. You can optionally attach a `NEAR` deposit to the call.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

  <Tabs groupId="api">
    <TabItem value="fc" label="function call">
    ```
import dotenv from "dotenv";
import { Account, JsonRpcProvider, teraToGas, KeyPairString, nearToYocto } from "near-api-js";

// Create an account object
dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a testnet provider
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// For read only calls, you can use the provider directly
const messages = await provider.callFunction({
  contractId: 'guestbook.near-examples.testnet',
  method: "get_messages",
  args: {},
});

console.log(messages);

// To modify state, you need an account to sign the transaction
const account = new Account(accountId, provider, privateKey);

// Call the contract
await account.callFunction({
  contractId: 'guestbook.near-examples.testnet',
  methodName: "add_message",
  args: { text: "Hello!" },
  gas: teraToGas('30'),
  deposit: nearToYocto('0.1'),
});

```
    :::tip Typed Result
    When using Typescript, you can type the return of `callFunction<T>`
    :::
    </TabItem>
    <TabItem value="tc" label="typed contract" default>
    ```
import { nearToYocto, Account, Contract, JsonRpcProvider, KeyPairString } from "near-api-js";
import abi from "./guestbook.abi.js";
import dotenv from "dotenv";

dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const account = new Account(accountId, provider, privateKey); // example-account.testnet

// Make a function call that modifies state
const contract = new Contract({
  contractId: "guestbook.near-examples.testnet",
  provider: provider,
  abi: abi,
});

contract.call.add_message({
  deposit: nearToYocto("0.1"),
  args: { text: "Hello, NEAR!" },
  account: account,
}); // TypeScript infers the type of this method

// Make a read-only function call
const totalMessages = await contract.view.total_messages();
console.log({ totalMessages });

// Send a tx to add message
const result = await contract.call.add_message({
  account,
  args: { text: "Hello, world!" },
});

console.log({ result });

```
    </TabItem>
  </Tabs>
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">

  <Tabs groupId="api">
    <TabItem value="fc" label="function call">
    ```
import dotenv from "dotenv";
import { Near } from "near-kit";

// Create a connection to testnet with credentials
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

const near = new Near({
  network: "testnet",
  privateKey,
  defaultSignerId: accountId
});

// For read only calls, you can use the provider directly
const messages = await near.view(
  'guestbook.near-examples.testnet',
  'get_messages',
  {}
);

console.log(messages);

// To modify state, call the contract method
await near.call(
  'guestbook.near-examples.testnet',
  'add_message',
  { text: "Hello!" },
  { gas: "30 Tgas" }
);

```
      :::tip Typed Result
      When using Typescript, you can type the return of `Near.view<T>` and `Near.call<T>`
      :::
    </TabItem>
    <TabItem value="tc" label="typed contract" default>
    ```
import { Near } from "near-kit";
import dotenv from "dotenv";

dotenv.config();

// Create a connection to testnet with credentials from environment
const near = new Near({
  network: "testnet",
  privateKey: process.env.PRIVATE_KEY,
  defaultSignerId: process.env.ACCOUNT_ID
});

// Define the contract interface
const guestbook = near.contract("guestbook.near-examples.testnet");

// View: get total messages
const totalMessages = await guestbook.view.total_messages();
console.log({ totalMessages });

// Call: add a message
const result = await guestbook.call.add_message({ text: "Hello from near-kit!" }, { gas: "30 Tgas" });
console.log({ result });

```
    </TabItem>
  </Tabs>
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    let contract_id: AccountId = "guestbook.near-examples.testnet".parse().unwrap();
    let contract = Contract(contract_id.clone());

```

  ```
    let args = json!({
        "text": "Hello, world!"
    });

    let function_call_result = contract
        .call_function("add_message", args)
        .unwrap()
        .transaction()
        .deposit(NearToken::from_near(1))
        .with_signer(account_id.clone(), signer.clone()) // Signer is the account that is calling the function
        .send_to(&network)
        .await
        .unwrap();
    println!("{:?}", function_call_result);
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```python
  await account.function_call("usn.near", "ft_transfer", {"receiver_id": "bob.near", "amount": "1000000000000000000000000"})
  ```
  </TabItem>
</Tabs>

<hr class="subsection" />

### Batch Actions

You can send multiple [actions](../protocol/transaction-anatomy.md#actions) in a batch to a **single** receiver. If one action fails then the entire batch of actions will be reverted.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
import dotenv from "dotenv";
import { Account, JsonRpcProvider, actions, teraToGas, nearToYocto, KeyPairString } from "near-api-js";

dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const account = new Account(accountId, provider, privateKey); // example-account.testnet

// Send the batch of actions
const batchActionsResult = await account.signAndSendTransaction({
  receiverId: "counter.near-examples.testnet",
  actions: [
    actions.functionCall("increment", {}, teraToGas("30"), 0n),
    actions.transfer(nearToYocto("0.001"))
  ],
});

console.log(batchActionsResult);

```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
import { Near } from "near-kit";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Batch multiple actions in one transaction
const result = await near.transaction(accountId)
  .functionCall("counter.near-examples.testnet", "increment", {}, { gas: "30 Tgas" })
  .transfer("counter.near-examples.testnet", "0.001 NEAR")
  .send();

console.log("Batch actions result:", result);

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    // Prepare the actions
    let call_action = Action::FunctionCall(Box::new(FunctionCallAction {
        method_name: "increment".to_string(),
        args: serde_json::json!({}).to_string().into_bytes(),
        gas: 30_000_000_000_000,
        deposit: 0,
    }));
    let transfer_action = Action::Transfer(TransferAction {
        deposit: 1_000_000_000_000_000_000_000_000,
    }); // Transfer 1 NEAR

    // Send the batch of actions
    let batch_actions_result = Transaction::construct(
        account_id.clone(),
        "counter.near-examples.testnet".parse().unwrap(),
    )
    .add_actions(vec![call_action, transfer_action])
    .with_signer(signer)
    .send_to(&network)
    .await
    .unwrap();
    println!("{:?}", batch_actions_result);
```

  </TabItem>
</Tabs>

<hr class="subsection" />

### Simultaneous Transactions

The only way to have true simultaneous transactions is to use multiple access keys on a same account. Each access key maintains its own nonce, allowing transactions signed with different keys to be processed in parallel:

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
import dotenv from "dotenv";
import { NEAR } from "near-api-js/tokens";
import { Account, actions, JsonRpcProvider, KeyPair, MultiKeySigner, KeyPairString } from "near-api-js";

dotenv.config(); // Loads .env
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create 10 keys and add them to the account
const account = new Account(accountId, provider, privateKey);

const keys: KeyPair[] = [];
const txActions: ReturnType<typeof actions.addFullAccessKey>[] = [];
for (let j = 0; j < 10; j++) {
  const newKeyPair = KeyPair.fromRandom('ed25519');
  keys.push(newKeyPair);
  txActions.push(actions.addFullAccessKey(newKeyPair.getPublicKey()));
}

await account.signAndSendTransaction({
  receiverId: accountId,
  actions: txActions
});

// Send NEAR tokens using multiple keys
const multiKeySigner = new MultiKeySigner(keys);
const multiAccount = new Account(accountId, provider, multiKeySigner);

const transfers = [...Array(100)].map(() =>
  multiAccount.transfer({
    token: NEAR,
    amount: NEAR.toUnits("0.001"),
    receiverId: "influencer.testnet"
  })
);

const sendNearTokensResults = await Promise.all(transfers);
sendNearTokensResults.forEach(result => console.log(result));

```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
import { Near, generateKey, RotatingKeyStore } from "near-kit";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a RotatingKeyStore for concurrent transactions
const keyStore = new RotatingKeyStore();

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Add multiple keys to the account for concurrent transactions
const keys = [];
for (let i = 0; i < 5; i++) {
  const newKey = generateKey();
  keys.push(newKey);

  // Add key to the account on-chain
  await near
    .transaction(accountId)
    .addKey(newKey.publicKey.toString(), { type: "fullAccess" })
    .send();

  // Add key to the rotating store
  await keyStore.add(accountId, newKey);
}

console.log(`Added ${keys.length} keys to account`);

// Create a new Near client with the rotating keystore
const nearWithRotating = new Near({
  network: "testnet",
  keyStore,
  defaultSignerId: accountId,
});

// Send multiple concurrent transactions
// The RotatingKeyStore will distribute keys to avoid nonce conflicts
const transfers = Array.from({ length: 10 }, (_, i) =>
  nearWithRotating.send("influencer.testnet", "0.001 NEAR")
);

const results = await Promise.all(transfers);
console.log(`Completed ${results.length} concurrent transfers`);

// Clean up: delete the keys we added
for (const key of keys) {
  await near
    .transaction(accountId)
    .deleteKey(accountId, key.publicKey.toString())
    .send();
}

console.log("Cleaned up keys");

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    // Prepare the transactions
    let args = serde_json::to_vec(&json!({
        "text": "Hello, world!"
    }))
    .unwrap();
    let action1 = Action::FunctionCall(Box::new(FunctionCallAction {
        method_name: "add_message".to_string(),
        args,
        gas: 100_000_000_000_000,
        deposit: 0,
    }));
    let tx1 = Transaction::construct(
        account_id.clone(),
        "guestbook.near-examples.testnet".parse().unwrap(),
    )
    .add_action(action1)
    .with_signer(signer.clone());

    let action2 = Action::FunctionCall(Box::new(FunctionCallAction {
        method_name: "increment".to_string(),
        args: vec![],
        gas: 100_000_000_000_000,
        deposit: 0,
    }));
    let tx2 = Transaction::construct(
        account_id.clone(),
        "counter.near-examples.testnet".parse().unwrap(),
    )
    .add_action(action2)
    .with_signer(signer.clone());

    // Send the transactions simultaneously
    let (tx1_result, tx2_result) = tokio::join!(tx1.send_to(&network), tx2.send_to(&network));
    println!("{:?}", tx1_result);
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```python
  import asyncio
  from py_near.account import Account

  account = Account(account_id="example-account.testnet", private_key="ed25519:...", rpc_addr="https://rpc.testnet.pagoda.co")
  await account.startup()

  # Prepare the transactions
  tx1 = account.function_call("guestbook.near-examples.testnet", "add_message", { "text": "Hello, world!" })
  tx2 = account.function_call("counter.near-examples.testnet", "increment", {})

  # Send the transactions simultaneously
  const transactionsResults = await asyncio.gather(tx1, tx2)
  ```

  </TabItem>
</Tabs>

:::warning Keep in mind
Simultaneous execution means there’s no guarantee of order or success. Any transaction may fail independently. If your use case requires strict ordering, then you should stick to sending transactions sequentially from a single key.
:::

<hr class="subsection" />

### Deploy a Contract {#deploy-a-contract}

On NEAR, a smart contract is deployed as a WASM file. Every account has the potential to become a contract — you simply need to deploy code to it.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
import { Account, JsonRpcProvider, KeyPairString } from "near-api-js";
import fs from "fs";
import dotenv from "dotenv";

dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const account = new Account(accountId, provider, privateKey); // example-account.testnet

// Deploy a contract to the account
const result = await account.deployContract(
  fs.readFileSync("../contracts/contract.wasm") // Path of contract WASM relative to the working directory
);

console.log(result);

```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
import { Near } from "near-kit";
import dotenv from "dotenv";
import fs from "fs";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Deploy a contract to the account
const wasmCode = fs.readFileSync("../contracts/contract.wasm");
const result = await near.transaction(accountId)
  .deployContract(accountId, wasmCode)
  .send();

console.log("Deploy contract result:", result);

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  Note that the `signer` here needs to be a signer for the same `account_id` as the one used to construct the `Contract` object.

  ```
    let deploy_result = Contract::deploy(account_id.clone())
        .use_code(include_bytes!("../../contracts/contract.wasm").to_vec()) // Path of contract WASM relative to this file
        .without_init_call()
        .with_signer(signer) // Signer is the account that is deploying the contract
        .send_to(&network)
        .await
        .unwrap();
    println!("{:?}", deploy_result);
}
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```python
  import asyncio
  from py_near.account import Account

  account = Account(account_id="example-account.testnet", private_key="ed25519:...", rpc_addr="https://rpc.testnet.pagoda.co")
  await account.startup()

  with open("contract.wasm", "rb") as f:
    contract_code = f.read()
  await account.deploy_contract(contract_code)
  ```
  </TabItem>
</Tabs>

<hr class="subsection" />

### Deploy a Global Contract {#deploy-a-global-contract}

[Global contracts](../smart-contracts/global-contracts.md) allow smart contracts to be deployed once and reused by any account without incurring high storage costs.

There are two ways to reference a global contract:
- **[By account](../smart-contracts/global-contracts.md#reference-by-account):** The contract code is tied to another account.
- **[By hash](../smart-contracts/global-contracts.md#reference-by-hash):** You reference the contract by its immutable code hash.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

  <Tabs groupId="global">
  <TabItem value="account" label="by account" default>
    ```
import { Account, JsonRpcProvider, KeyPair, KeyPairString } from "near-api-js";
import { NEAR } from "near-api-js/tokens";
import { readFileSync } from "fs";
import dotenv from "dotenv";

dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const deployer = new Account(accountId, provider, privateKey); // example-account.testnet

// Path of contract WASM relative to the working directory
const wasm: Uint8Array = new Uint8Array(readFileSync("../contracts/contract.wasm"));
const deployResult = await deployer.deployGlobalContract(wasm, "accountId");

console.log(deployResult);

```
  </TabItem>
  <TabItem value="hash" label="by hash" default>
    ```
import { Account, JsonRpcProvider, KeyPair, KeyPairString, baseEncode } from "near-api-js";
import { NEAR } from "near-api-js/tokens";
import { readFileSync } from "fs";
import { createHash } from "crypto";
import dotenv from "dotenv";

dotenv.config();
const privateKey = process.env.PRIVATE_KEY! as KeyPairString;
const accountId: string = process.env.ACCOUNT_ID!;

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Create an account object
const deployer = new Account(accountId, provider, privateKey); // example-account.testnet

// Path of contract WASM relative to the working directory
const wasm: Uint8Array = new Uint8Array(readFileSync("../contracts/contract.wasm"));
const deployResult = await deployer.deployGlobalContract(wasm, "codeHash");

console.log(deployResult);
await provider.viewTransactionStatus({ txHash: deployResult.transaction.hash, accountId: deployer.accountId });
```
  </TabItem>
  </Tabs>

  </TabItem>

  <TabItem value="nk" label="🌐 near-kit">

  <Tabs groupId="global">
  <TabItem value="account" label="by account" default>
    ```
import { Near, generateKey } from "near-kit";
import dotenv from "dotenv";
import fs from "fs";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Read the contract WASM
const wasmCode = fs.readFileSync("../contracts/contract.wasm");

// Publish as a global contract (identified by account ID)
// Other accounts can use this contract without deploying their own copy
const publishResult = await near
  .transaction(accountId)
  .publishContract(wasmCode, { identifiedBy: "account" })
  .send();

console.log("Published global contract:", publishResult.transaction.hash);

```
  </TabItem>
  <TabItem value="hash" label="by hash" default>
    ```
import { Near, generateKey } from "near-kit";
import dotenv from "dotenv";
import fs from "fs";
import { createHash } from "crypto";

// Load environment variables
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

// Create a connection to testnet with signing capabilities
const near = new Near({
  network: "testnet",
  privateKey: privateKey, // ed25519:5Fg2...
  defaultSignerId: accountId, // example-account.testnet
});

// Read the contract WASM
const wasmCode = fs.readFileSync("../contracts/contract.wasm");

// Calculate the code hash (SHA-256)
const codeHash = createHash("sha256").update(wasmCode).digest();

// Publish as a global contract (identified by code hash)
// This creates an immutable contract reference
const publishResult = await near
  .transaction(accountId)
  .publishContract(wasmCode, { identifiedBy: "hash" })
  .send();

console.log("Published global contract by hash:", publishResult.transaction.hash);

```
  </TabItem>
  </Tabs>

  </TabItem>

  <TabItem value="rust" label="🦀 near-api-rs">

  Once you've created an Account instance, you can deploy your regular contract as a global contract.

  <Tabs>
  <TabItem value="account" label="By Account" default>

  Let’s look at an example of deploying a global contract by account.
  
  To do this, use the `deploy_global_contract_code` function and use the method `as_account_id`, along with the contract’s code bytes.
  
  ```rust
    let global_account_id: AccountId = "nft-contract.testnet".parse().unwrap();
    let code = std::fs::read("path/to/your/contract.wasm").unwrap();
    let signer = Signer::new(Signer::from_secret_key(private_key)).unwrap();

    let result: FinalExecutionOutcomeView = Contract::deploy_global_contract_code(code)
        .as_account_id(global_account_id)
        .with_signer(signer)
        .send_to_testnet()
        .await.unwrap();
  ```

  <a href="https://github.com/near-examples/near-api-examples/blob/main/rust/examples/global_contract_accountid.rs" target="_blank" rel="noreferrer noopener" class="text-center">
    See full example on GitHub
  </a>
  </TabItem>

  <TabItem value="hash" label="By Hash" default>

  Let’s look at an example of deploying a global contract by hash.
  
  To do this, use the `deploy_global_contract_code` function and use the method `as_hash`, along with the contract’s code bytes.
  
  ```rust
    let account_id: AccountId = "my-account.testnet".parse().unwrap();
    let code = std::fs::read("path/to/your/contract.wasm").unwrap();
    let signer = Signer::new(Signer::from_secret_key(private_key)).unwrap();

    let result: FinalExecutionOutcomeView = Contract::deploy_global_contract_code(code)
        .as_hash()
        .with_signer(account_id, signer)
        .send_to_testnet()
        .await.unwrap();
  ```

  <a href="https://github.com/near-examples/near-api-examples/blob/main/rust/examples/global_contract_hash.rs" target="_blank" rel="noreferrer noopener" class="text-center">
    See full example on GitHub
  </a>
  </TabItem>
  </Tabs>

  </TabItem>

</Tabs>

### Use a Global Contract

Once a [global contract](../smart-contracts/global-contracts.md) has been [deployed](#deploy-a-global-contract), let’s see how you can reference and use it from another account.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    <Tabs groupId="global">
      <TabItem value="account" label="by account" default>
        ```
const consumer = new Account(
  consumerAccountId,
  provider,
  key.toString() as KeyPairString
);

await consumer.useGlobalContract({ accountId: deployer.accountId });

const contract = await consumer.getContractCode();
console.log("Size", contract.code.length, "Hash", contract.hash);

```
      </TabItem>
      <TabItem value="hash" label="by hash" default>
        ```
const consumer = new Account(
  consumerAccountId,
  provider,
  key.toString() as KeyPairString
);

const useResult = await consumer.useGlobalContract({
  codeHash: Uint8Array.from(Buffer.from(hash, 'base64')),
});
console.log(useResult);
await provider.viewTransactionStatus({ txHash: useResult.transaction.hash, accountId: consumer.accountId });

const contract = await consumer.getContractCode();
console.log("Size", contract.code.length, "Hash", contract.hash);

// delete consumer account and refund deployer
```
      </TabItem>
    </Tabs>
  </TabItem>

  <TabItem value="nk" label="🌐 near-kit">
    <Tabs groupId="global">
      <TabItem value="account" label="by account" default>
        ```
// Create a consumer account that will use the global contract
const consumerKey = generateKey();
const consumerAccountId = `${Date.now()}.${accountId}`;

await near
  .transaction(accountId)
  .createAccount(consumerAccountId)
  .transfer(consumerAccountId, "0.1 NEAR")
  .addKey(consumerKey.publicKey.toString(), { type: "fullAccess" })
  .send();

console.log("Created consumer account:", consumerAccountId);

// Consumer uses the global contract by referencing the publisher's account ID
const consumerNear = new Near({
  network: "testnet",
  privateKey: consumerKey.secretKey,
  defaultSignerId: consumerAccountId,
});

await consumerNear
  .transaction(consumerAccountId)
  .deployFromPublished({ accountId: accountId })
  .send();

console.log("Consumer is now using global contract from:", accountId);

// Clean up: delete consumer account
await consumerNear
  .transaction(consumerAccountId)
  .deleteAccount({ beneficiary: accountId })
  .send();

console.log("Cleaned up consumer account");

```
      </TabItem>
      <TabItem value="hash" label="by hash" default>
        ```
// Create a consumer account
const consumerKey = generateKey();
const consumerAccountId = `${Date.now()}.${accountId}`;

const createResult = await near
  .transaction(accountId)
  .createAccount(consumerAccountId)
  .transfer(consumerAccountId, "0.1 NEAR")
  .addKey(consumerKey.publicKey.toString(), { type: "fullAccess" })
  .send();

await near.getTransactionStatus(createResult.transaction.hash, accountId, "FINAL");
console.log("Created consumer account:", consumerAccountId);

// Consumer uses the global contract by referencing the code hash
const consumerNear = new Near({
  network: "testnet",
  privateKey: consumerKey.secretKey,
  defaultSignerId: consumerAccountId,
});

await consumerNear
  .transaction(consumerAccountId)
  .deployFromPublished({ codeHash: codeHash })
  .send();

console.log("Consumer is now using global contract by hash");

// Clean up: delete consumer account
await consumerNear
  .transaction(consumerAccountId)
  .deleteAccount({ beneficiary: accountId })
  .send();

console.log("Cleaned up consumer account");

```
      </TabItem>
    </Tabs>
  </TabItem>

  <TabItem value="rust" label="🦀 near-api-rs">

  <Tabs>
  <TabItem value="account" label="By Account" default>

  To reference a global contract by account, you need to call the `use_global_account_id` function and pass the source `accountId` where the contract was originally deployed.

  ```rust
    let global_account_id: AccountId = "nft-contract.testnet".parse().unwrap();
    let my_account_id: AccountId = "my-contract.testnet".parse().unwrap();
    let my_signer = Signer::new(Signer::from_secret_key(private_key)).unwrap();

    let result: FinalExecutionOutcomeView = Contract::deploy(my_account_id)
        .use_global_account_id(global_account_id)
        .without_init_call()
        .with_signer(my_signer)
        .send_to_testnet()
        .await.unwrap();
  ```

  <a href="https://github.com/near-examples/near-api-examples/blob/main/rust/examples/global_contract_accountid.rs" target="_blank" rel="noreferrer noopener" class="text-center">
    See full example on GitHub
  </a>
  </TabItem>

  <TabItem value="hash" label="By Hash" default>

  To reference a global contract by hash, you need to call the `use_global_hash` function and pass the source `hash` of the original contract.

  ```rust
    let global_hash: types::CryptoHash = "DxfRbrjT3QPmoANMDYTR6iXPGJr7xRUyDnQhcAWjcoFF".parse().unwrap();
    let account_id: AccountId = "my-contract.testnet".parse().unwrap();
    let signer = Signer::new(Signer::from_secret_key(private_key)).unwrap();

    let result: FinalExecutionOutcomeView = Contract::deploy(account_id)
        .use_global_hash(global_hash)
        .without_init_call()
        .with_signer(signer)
        .send_to_testnet()
        .await.unwrap();
  ```

  <a href="https://github.com/near-examples/near-api-examples/blob/main/rust/examples/global_contract_hash.rs" target="_blank" rel="noreferrer noopener" class="text-center">
    See full example on GitHub
  </a>
  </TabItem>
  </Tabs>

  </TabItem>

</Tabs>

---

## View Function

View functions are read-only methods on a smart contract that do not modify state. You can call them without using an account or signing a transaction.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
// Create a testnet provider
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// For read only calls, you can use the provider directly
const messages = await provider.callFunction({
  contractId: 'guestbook.near-examples.testnet',
  method: "get_messages",
  args: {},
});

console.log(messages);

```
    :::tip Typed Result
    When using Typescript, you can type the return of `callFunction<T>`
    :::
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
import dotenv from "dotenv";
import { Near } from "near-kit";

// Create a connection to testnet with credentials
dotenv.config();
const privateKey = process.env.PRIVATE_KEY;
const accountId = process.env.ACCOUNT_ID;

const near = new Near({
  network: "testnet",
  privateKey,
  defaultSignerId: accountId
});

// For read only calls, you can use the provider directly
const messages = await near.view(
  'guestbook.near-examples.testnet',
  'get_messages',
  {}
);

console.log(messages);

```
    :::tip Typed Result
    When using Typescript, you can type the return of `Near.view<T>`
    :::
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    // Create contract object
    let contract_id: AccountId = "guestbook.near-examples.testnet".parse().unwrap();
    let contract = Contract(contract_id.clone());

    // Make a view call to a contract
    let view_call_result: Data<u32> = contract
        .call_function("total_messages", ())
        .unwrap()
        .read_only()
        .fetch_from(&network)
        .await
        .unwrap();
    println!("{:?}", view_call_result.data);
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```python
  view_call_result = await account.view_function("guestbook.near-examples.testnet", "total_messages", {})
  # If args are required, they can be passed in like this in the 3rd argument:
  # {
  #   "from_index": "0",
  #   "limit": "10"
  # }
  print(view_call_result)
  ```
  </TabItem>
</Tabs>

---

## Keys

### Get All Access Keys {#get-all-access-keys}

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// Query keys with the provider
const keysProvider = await provider.viewAccessKeyList({ accountId });
console.log(keysProvider);

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    let keys = account.list_keys().fetch_from(&network).await.unwrap();
    println!("{:?}", keys);
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```python
  keys = await account.get_access_key_list()
  ```
  </TabItem>
</Tabs>

<hr class="subsection" />

### Add Full Access Key {#add-full-access-key}

A [Full Access key](/protocol/access-keys.md#full-access-keys) grants complete control over the account.

Anyone with this key can transfer funds, sign transactions, interact with contracts, or even delete the account entirely.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
// New keys
const fullKeyPair = KeyPair.fromRandom("ed25519");
const fnKeyPair = KeyPair.fromRandom("ed25519");

// Add a Full Access Key
await account.addFullAccessKey(
  fullKeyPair.getPublicKey().toString() // ed25519:2ASWc...
);

```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
// Generate new key pairs
const fullAccessKey = generateKey();
const functionCallKey = generateKey();

console.log("Generated Full Access Key:", fullAccessKey.publicKey.toString());
console.log("Generated Function Call Key:", functionCallKey.publicKey.toString());

// Add a Full Access Key using transaction builder
await near
  .transaction(accountId)
  .addKey(fullAccessKey.publicKey.toString(), { type: "fullAccess" })
  .send();

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    // Add full access key
    let new_full_private_key = signer::generate_secret_key().unwrap(); // Get the private key from the keypair
    let add_full_key_result = account
        .add_key(AccessKeyPermission::FullAccess, new_full_private_key.public_key())
        .with_signer(signer.clone())
        .send_to(&network)
        .await
        .unwrap();

    let new_full_public_key = new_full_private_key.public_key().to_string();
    println!("{:?}", new_full_public_key);
    println!("{:?}", add_full_key_result);

    // Add function call access key
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```python
  keys = await account.add_full_access_public_key("5X9WvUbRV3aSd9Py1LK7HAndqoktZtcgYdRjMt86SxMj")
  ```
  </TabItem>
</Tabs>

<hr class="subsection" />

### Add Function Call Key {#add-function-call-key}

A [Function Call access key](/protocol/access-keys.md#function-call-keys) is designed specifically to sign transactions that include only [`functionCall` actions](/protocol/transaction-anatomy#actions) to a specific contract.

You can further restrict this key by:
- Limiting which method names can be called
- Capping the amount of `NEAR` the key can spend on transaction fees

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
// Add Function Call Access Key
await account.addFunctionCallAccessKey({
  publicKey: fnKeyPair.getPublicKey(), // The new public key ed25519:2ASWc...
  contractId: "example-contract.testnet", // Contract this key is allowed to call (optional)
  methodNames: ["example_method"], // Methods this key is allowed to call (optional)
  allowance: NEAR.toUnits("0.25") // Gas allowance key can use to call methods (optional)
});

```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
// Add a Function Call Access Key using transaction builder
await near
  .transaction(accountId)
  .addKey(functionCallKey.publicKey.toString(), {
    type: "functionCall",
    receiverId: "example-contract.testnet",
    methodNames: ["example_method"],
    allowance: "0.25 NEAR",
  })
  .send();

console.log(`Added Function Call Key: ${functionCallKey.publicKey.toString()}`);

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    // Add function call access key
    let new_function_call_key = AccessKeyPermission::FunctionCall(FunctionCallPermission {
        allowance: Some(250_000_000_000_000_000_000_000), // Gas allowance key can use to call methods (optional)
        receiver_id: "example-contract.testnet".to_string(), // Contract this key is allowed to call
        method_names: vec!["example_method".to_string()], // Methods this key is allowed to call
    });

    let new_function_private_key = signer::generate_secret_key().unwrap();
    let add_function_key_result = account
        .add_key(new_function_call_key, new_function_private_key.public_key())
        .with_signer(signer.clone())
        .send_to(&network)
        .await
        .unwrap();

    let new_function_public_key = new_function_private_key.public_key().to_string();
    println!("{:?}", new_function_public_key);
    println!("{:?}", add_function_key_result);

    // Delete full access key
```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```python
  await account.add_public_key(
    "5X9WvUbRV3aSd9Py1LK7HAndqoktZtcgYdRjMt86SxMj",
    "example-contract.testnet", # Contract this key is allowed to call
    ["example_method"], # Methods this key is allowed to call (optional)
    0.25 * NEAR # Gas allowance key can use to call methods (optional)
  )
  ```
  </TabItem>

</Tabs>

:::tip
For security reasons, Function Call access keys **can only be used with function calls that attach zero `NEAR` tokens. Any attempt to include a deposit will result in a failed transaction.
:::

<hr class="subsection" />

### Delete Access Key {#delete-access-key}

Accounts on NEAR can delete their own keys.

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">
    ```
await account.deleteKey(fnKeyPair.getPublicKey().toString());
await account.deleteKey(fullKeyPair.getPublicKey().toString());
```
  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">
    ```
const nearWithNewKey = new Near({
  network: "testnet",
  privateKey: fullAccessKey.secretKey,
  defaultSignerId: accountId,
});

await nearWithNewKey
  .transaction(accountId)
  .deleteKey(accountId, functionCallKey.publicKey.toString())
  .send();

```
  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  ```
    // Delete full access key
    let public_key_to_delete = new_full_public_key;
    let delete_full_key_result = account
        .delete_key(public_key_to_delete.parse().unwrap())
        .with_signer(signer.clone())
        .send_to(&network)
        .await
        .unwrap();
    println!("{:?}", delete_full_key_result);
}

```

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

  ```python
  await account.delete_public_key("5X9WvUbRV3aSd9Py1LK7HAndqoktZtcgYdRjMt86SxMj")
  ```
  </TabItem>
</Tabs>

:::danger
Be very careful when deleting keys, remove all keys from an account and you will lose access to the account permanently
:::

---

## Validate Message Signatures

Users can sign messages using the `wallet-selector` `signMessage` method, which returns a signature. This signature can be verified using the following code:

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

    ```
import { verifyMessage } from "near-api-js/nep413";
import { JsonRpcProvider } from "near-api-js";

// Create a connection to testnet RPC
const provider = new JsonRpcProvider({
  url: "https://test.rpc.fastnear.com",
});

// This is the challenge given to the user to sign
const MESSAGE: string = "log me in";
const APP: string = "http://localhost:3000";
const CHALLENGE: Buffer = Buffer.from(Array.from(Array(32).keys()));

// This is the object returned by `wallet.signMessage` in wallet selector
const walletReturn = {
  "signature": "IfModLa3g3czlyPhkg/LSkTFSy7XCGreStZJTDIO1m3viEnYFLdXfpz1gYUVKYv3W2vwcV77TmGEzc9y0Nz+AA==",
  "accountId": "maguila.testnet",
  "publicKey": "ed25519:AtH7GEjv2qmBVoT8qoRhWXizXM5CC12DC6tiqY9iNoRm"
};

await verifyMessage({
  signerAccountId: walletReturn.accountId,
  signerPublicKey: walletReturn.publicKey,
  signature: new Uint8Array(Buffer.from(walletReturn.signature, 'base64')),
  payload: {
    message: MESSAGE,
    recipient: APP,
    nonce: CHALLENGE
  },
  provider
});

```

  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">

    ```
import { Near, verifyNep413Signature } from "near-kit";

// Create Near client for testnet (no signing needed for verification)
const near = new Near({ network: "testnet" });

// The challenge given to the user to sign
const MESSAGE = "log me in";
const APP = "http://localhost:3000";
const CHALLENGE = Buffer.from(Array.from(Array(32).keys()));

// The object returned by wallet.signMessage in wallet selector
const signedMessage = {
  signature:
    "IfModLa3g3czlyPhkg/LSkTFSy7XCGreStZJTDIO1m3viEnYFLdXfpz1gYUVKYv3W2vwcV77TmGEzc9y0Nz+AA==",
  accountId: "maguila.testnet",
  publicKey: "ed25519:AtH7GEjv2qmBVoT8qoRhWXizXM5CC12DC6tiqY9iNoRm",
};

// Verify the signature
const isValid = await verifyNep413Signature(
  signedMessage,
  {
    message: MESSAGE,
    recipient: APP,
    nonce: CHALLENGE,
  },
  { near, maxAge: Infinity }, // Disable timestamp check for this demo
);

console.log("Signature valid:", isValid);

```

  </TabItem>
</Tabs>

---

## Additional resources

<Tabs groupId="api">
  <TabItem value="naj" label="🌐 near-api-js">

  - [Documentation](https://near.github.io/near-api-js)
  - [Github](https://github.com/near/near-api-js)
  - [Full Examples](https://github.com/near-examples/near-api-examples/tree/main)

  </TabItem>
  <TabItem value="nk" label="🌐 near-kit">

  - [Github](https://github.com/r-near/near-kit/tree/main)
  - [Full Examples](https://github.com/near-examples/near-api-examples/tree/main/near-kit)

  </TabItem>
  <TabItem value="rust" label="🦀 near-api-rs">

  - [Documentation](https://docs.rs/near-api/latest/near_api/)
  - [Github](https://github.com/near/near-api-rs)
  - [Full Examples](https://github.com/near-examples/near-api-examples/tree/main/rust)

  </TabItem>
  <TabItem value="python" label="🐍 py-near">

    - [Github](https://github.com/pvolnov/py-near)

  </TabItem>
</Tabs>
