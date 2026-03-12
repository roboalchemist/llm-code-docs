# Clockwork Documentation

Source: https://docs.clockwork.xyz/llms-full.txt

---

# What is Clockwork?

**Clockwork** **is an open-source automation engine for the** [**Solana**](https://solana.com/) **blockchain**. Developers can use Clockwork to schedule transactions and build automated, event-driven smart-contracts.&#x20;

{% embed url="<https://www.youtube.com/watch?v=1iBG1U3VE6Y>" %}
Clockwork presentation at Breakpoint 2022.
{% endembed %}

### **Blockchains**

**Blockchains represent a major paradigm shift in software engineering.** Where applications are traditionally hosted in large centrally managed data centers, blockchains like Solana offer an alternative computing environment – one that's run by a decentralized community of stakeholders. On a blockchain, computing is secured by smart-contracts and data is automatically replicated to thousands of servers around the world. This helps makes information more transparent to users and tamperproof from malicious actors. These qualities make blockchains an ideal choice for applications where cryptographically-secured truth is important.&#x20;

### Automated smart-contracts

**Clockwork helps bring smart-contracts to life.** We often want applications to run automatically, according a schedule, or to be triggered by some unplanned event. Developers can use Clockwork to encode these rules directly into their smart-contracts. Once these rules are in place, the Clockwork worker network (i.e. Solana RPC nodes) will monitor for the events your programs care about and submit transactions on your program's behalf. In this way, you can build fully autonomous smart-contracts without having to build and maintain your own expensive off-chain infrastructure.&#x20;

### Why Solana?

**Solana is the most performant and scalable public blockchain in the world.** With its affordable fees, reliable transactions, and globally distributed validator network, Solana is a favorite amongst users and developers alike. Currently humming along at [**\~40,000,000**](https://dune.com/kroeger0x/Solana-Metrics) transactions per day, Solana processes more transactions than many other notable blockchains combined. And with over [**2,000**](https://solana.com/news/validator-health-report-august-2022) validators running on six different continents around the world, Solana is by many metrics one the most decentralized blockchains in the world.

# Quickstart

## Getting started

In this quickstart, you will learn how to automate a SOL transfer using Clockwork. We will install the Clockwork CLI and spawn a Clockwork thread from a Typescript application. Within 10 minutes, you will have your first automation up and running.

{% hint style="info" %}
All code in this quickstart is open-source and free to fork [**on Github**](https://github.com/clockwork-xyz/examples/tree/main/0-quickstart_transfer)**.**
{% endhint %}

## 1. Create your first automation (5 min)

Let's begin by creating a new vanilla Node Typescript project:

```sh
mkdir clockwork_quickstart
cd clockwork_quickstart
```

Create a new `tsconfig.json` file:

```tsconfig
{
  "compilerOptions": {
    "lib": ["es2015"],
    "module": "commonjs",
    "target": "es6",
    "esModuleInterop": true
  }
}
```

Create a new `package.json` file with the below content. The main dependencies you really need in your project are the [**Clockwork SDK**](https://www.npmjs.com/package/@clockwork-xyz/sdk) and Anchor.

```json
{
  "scripts": {
    "test": "yarn run ts-mocha -p tsconfig.json -t 1000000 ./tests/main.ts"
  },
  "dependencies": {
    "@solana/web3.js": "^1.73.0",
    "@coral-xyz/anchor": "^0.27.0",
    "@clockwork-xyz/sdk": "^0.3.4"
  },
  "devDependencies": {
    "@types/chai": "^4.3.3",
    "@types/mocha": "^9.1.1",
    "chai": "^4.3.6",
    "mocha": "^10.0.0",
    "ts-mocha": "^10.0.0",
    "typescript": "^4.8.3"
  }
}
```

After this, create a new file called `main.ts`. Import the necessary libraries and set up a Clockwork provider.

```ts
import { expect } from "chai";
import {
    Connection,
    Keypair,}
    LAMPORTS_PER_SOL,
    PublicKey,
    Transaction,
} from "@solana/web3.js";
import * as anchor from "@coral-xyz/anchor";
import NodeWallet from "@coral-xyz/anchor/dist/cjs/nodewallet";
import { ClockworkProvider, PAYER_PUBKEY } from "@clockwork-xyz/sdk";

const connection = new Connection("http://localhost:8899", "processed");
const payer = Keypair.fromSecretKey(
    Buffer.from(JSON.parse(require("fs").readFileSync(
        require("os").homedir() + "/.config/solana/id.json",
        "utf-8"
    )))
);

// Prepare clockworkProvider
const provider = new anchor.AnchorProvider(
    connection,
    new NodeWallet(payer),
    anchor.AnchorProvider.defaultOptions()
);
const clockworkProvider = ClockworkProvider.fromAnchorProvider(provider);
```

Next, we'll prepare a `SystemTransfer` instruction and automate it with a Clockwork thread. Threads are the basic building blocks of automations on Solana. Every thread has a trigger condition and a set of instructions to run. In the code sample below, we create a thread that schedules a SOL transfer to happen every 10 seconds.&#x20;

```typescript
...

describe("transfer", async () => {
    it("Transfers SOL every 10 seconds", async () => {
      const threadId = "sol_transferjs" + new Date().getTime();
      const [threadAddress] = clockworkProvider.getThreadPDA(
          payer.publicKey,   // authority
          threadId
       )
  
      const recipient = Keypair.generate().publicKey;
      console.log(`🫴  recipient: ${recipient.toString()}\n`);

      // 1️⃣  Prepare an instruction to be automated.
      const transferIx = SystemProgram.transfer({
          fromPubkey: PAYER_PUBKEY,
          toPubkey: recipient,
          lamports: LAMPORTS_PER_SOL,
      });
  
      // 2️⃣  Define a trigger condition.
      const trigger = {
          cron: {
              schedule: "*/10 * * * * * *",
              skippable: true,
          },
      };
  
      // 3️⃣ Create the thread.
      const ix = await clockworkProvider.threadCreate(
          payer.publicKey,           // authority
          threadId,                  // id
          [transferIx],              // instructions
          trigger,                   // trigger
          LAMPORTS_PER_SOL,      // amount to fund the thread with
      );
      const tx = new Transaction().add(ix);
      const signature = await clockworkProvider.anchorProvider.sendAndConfirm(tx);
      console.log(`🗺️  explorer: https://app.clockwork.xyz/threads/${threadAddress}?cluster=custom&customUrl=${connection.rpcEndpoint}\n`);
      
      // Check balance of recipient address
      await new Promise((resolve) => setTimeout(resolve, 10 * 1000));
      let balance = await connection.getBalance(recipient) / LAMPORTS_PER_SOL;
      console.log(`✅ recipient balance: ${balance} SOL\n`);
      expect(balance).to.eq(1);

      await new Promise((resolve) => setTimeout(resolve, 10 * 1000));
      balance = await connection.getBalance(recipient) / LAMPORTS_PER_SOL;
      console.log(`✅ recipient balance: ${balance} SOL\n`);
      expect(balance).to.eq(2);
    });
});
```

We can see the `threadCreate` function asks for 5 arguments. These include some basic information needed to initialize the thread account.

* `authority` – The owner of the thread. This account must be the transaction signer and will have permission to delete, pause, resume, stop, and update the thread.
* `id` – An identifier for the thread (can also use buffer or vec u8).
* `instructions` – The list of instructions to execute when the trigger condition becomes valid.
* `trigger` – The trigger condition for the thread. When this condition is valid, the thread will begin executing the provided instructions.
* `amount` – The number of lamports to fund the thread account with. Remember to provide a small amount of SOL. Read more about how fees are calculated [**here**](https://docs.clockwork.xyz/developers/threads/fees).

## 2. Run the tests (2 min)

Now we need to get our app running. If you have not done so already, you will need to install the Clockwork CLI by running the cargo command below. If you face any trouble here, please refer to the [**installation**](https://docs.clockwork.xyz/welcome/installation) docs.&#x20;

```shell
cargo install -f --locked clockwork-cli
```

Now that we have Clockwork installed, we can go ahead and spin up a local Clockwork node:

```bash
clockwork localnet
```

In a separate terminal window, we'll run the test:

```bash
yarn test
```

And voila:

<figure><img src="https://2516514367-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F64lLSRIas17CYMPkc7Zc%2Fuploads%2FODlR1NaKr9OTg9jiuYMg%2FScreenshot%202023-06-01%20at%2001.48.01.png?alt=media&#x26;token=9a0da762-787f-4b79-9882-17617e1b0233" alt=""><figcaption></figcaption></figure>

## 3. Monitor your automation (1 min)

You can now watch your automation run all on its own. Grab the Clockwork explorer link that was printed out to the console. Using the Clockwork explorer, you can get simulation logs and inspect your thread. For example, here's mine: <https://app.clockwork.xyz/threads/GB7YgYK3bKF8J4Rr9Z2oeA3hwxrJdvW5zgXuNaxWWmUF?cluster=devnet>

<figure><img src="https://2516514367-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F64lLSRIas17CYMPkc7Zc%2Fuploads%2F89lrpQPS9vE6MAyTIZIh%2Fimage.png?alt=media&#x26;token=3aa2cafa-12e4-4afa-82bd-b14511b0668f" alt=""><figcaption></figcaption></figure>

Of course you can also look up your thread account in your favorite Solana explorer. You can alternatively use the Solana CLI to stream program logs by running the command provided below. Here's [**an example thread**](https://explorer.solana.com/address/3ohRKgNyLS1iTGiUqnzoiFiQcrCLGmr3NWHzq4HW8BdJ?cluster=devnet) that was created in a test on May 24th, 2023.

```bash
solana logs -u l YOUR_PROGRAM_ID
```

<figure><img src="https://user-images.githubusercontent.com/8634334/222591908-bbaa04c5-83b4-46c2-b83b-68e1fef473eb.png" alt=""><figcaption></figcaption></figure>

## Key insights

1. Threads are an automation primitive for Solana.
2. You can use threads to automate any program instruction on Solana.&#x20;
3. [**Triggers**](https://docs.clockwork.xyz/reference/threads/triggers) allow you to define when a thread should begin execution.
4. Threads must be funded with a small amount of SOL to pay for [**automation fees**](https://docs.clockwork.xyz/reference/threads/fees).&#x20;

## Continue learning

* Many more examples can be found in the [**guides section**](https://docs.clockwork.xyz/developers/guides)**.**
* Ask questions on [**Discord**](https://discord.gg/epHsTsnUre).

# Installation

## Rust

Go [**here**](https://www.rust-lang.org/tools/install) to install Rust.

## Solana

Go [**here**](https://docs.solana.com/cli/install-solana-cli-tools) to install Solana, and then run `solana-keygen new` to create a local keypair for development.&#x20;

## Anchor

Go [**here**](https://www.anchor-lang.com/docs/installation) to install Anchor. Anchor is a popular framework for building Solana smart-contracts. We will reference Anchor frequently in these docs and guides.

## Clockwork

To install Clockwork on your local machine, simply run the following cargo install command:

```sh
cargo install -f --locked clockwork-cli
```

If you are on Linux, you may need to additionally install these dependencies:

```sh
sudo apt-get update && \
sudo apt-get upgrade && \
sudo apt-get install -y pkg-config build-essential libudev-dev libssl-dev
```

# 1. Scheduling an SPL transfer

## What you will learn

In this guide, you will learn how to schedule an SPL token transfer using Clockwork. This example will demonstrate many key concepts of working with Clockwork:

1. How the Clockwork program model works.
2. How to sign transactions with threads.
3. How to monitor an automation.

{% hint style="info" %}
All code in this guide is open-source and free to fork [**on Github**](https://github.com/clockwork-xyz/examples)**.**
{% endhint %}

## 1. The Clockwork programming model

Let's start with the big picture. Solana is a really fast, globally distributed computer. Just as programs on a traditional computer needs to be able to execute an automated series of instructions, so do programs on Solana. Clockwork threads are an automation primitive analogous to [**computer threads**](https://en.wikipedia.org/wiki/Thread_\(computing\)) that developers can use to automate programs on Solana. In simple terms, this means we can point Clockwork at any Solana program to automate it. A model of this relationship is presented in the diagram below.&#x20;

![The Clockwork programming model.](https://user-images.githubusercontent.com/8634334/222291232-ce195a01-7bdc-4567-8907-14485d19ee91.png)

## 2. Setting up our project

Let's begin by creating a new vanilla Node Typescript project:

```sh
mkdir spl_transfer
cd spl_transfer
```

Create a new `tsconfig.json` file:

```tsconfig
{
  "compilerOptions": {
    "lib": ["es2015"],
    "module": "commonjs",
    "target": "es6",
    "esModuleInterop": true
  }
}
```

Create a new `package.json` file with the below content. The main dependencies you really need in your project are:

* `@clockwork-xyz/sdk` for interacting with Clockwork.
* `@solana/spl-token` to build token transfer instructions.

```json
{
  "name": "spl-transfer",
  "version": "1.0.0",
  "description": "SPL Transfer Example",
  "scripts": {
    "test": "yarn run ts-mocha -p tsconfig.json -t 1000000 main.ts"
  },
  "dependencies": {
    "@clockwork-xyz/sdk": "^0.3.4",
    "@coral-xyz/anchor": "^0.27.0",
    "@solana/spl-token": "^0.3.6",
    "@solana/web3.js": "^1.73.0"
  },
  "devDependencies": {
    "@types/chai": "^4.3.3",
    "@types/mocha": "^9.1.1",
    "chai": "^4.3.6",
    "mocha": "^10.0.0",
    "ts-mocha": "^10.0.0",
    "typescript": "^4.8.3"
  }
}
```

Install the dependencies by running:

```
yarn
```

Now, let's scaffold a simple test in `main.ts`:

```typescript
import { expect } from "chai";
import {
  Connection,
  Keypair,
  LAMPORTS_PER_SOL,
  PublicKey,
  Transaction,
} from "@solana/web3.js";
import {
  createMint,
  getAccount,
  getOrCreateAssociatedTokenAccount,
  createTransferInstruction,
  mintTo,
} from "@solana/spl-token";
import { AnchorProvider } from "@coral-xyz/anchor";
import NodeWallet from "@coral-xyz/anchor/dist/cjs/nodewallet";
import { ClockworkProvider } from "@clockwork-xyz/sdk";


describe("spl-transfer", async () => {
  it("It transfers tokens every 10s", async () => {
    const connection = new Connection("http://localhost:8899", "processed");
    const payer = keypairFromFile(
      require("os").homedir() + "/.config/solana/id.json"
    );

    // Prepare clockworkProvider
    const provider = new AnchorProvider(
      connection,
      new NodeWallet(payer),
      AnchorProvider.defaultOptions()
    );
    const clockworkProvider = ClockworkProvider.fromAnchorProvider(provider);
  });
});
```

* We use your default paper keypair as the payer, this of course will change depending on your use case.
* Finally, we initialize a `ClockworkProvider`. This will be required later to create your thread.

## 3. Signing with threads

In this section, we will focus on how signing works with Threads. But first, let's prepare the accounts needed for the SPL Transfer Instruction to be scheduled. If you ever worked with Solana, you might know by now that SPL Transfers don't happen between system accounts, but instead between associated token accounts.

```typescript
/**
 * Construct a Transfer instruction
 *
 * @param source       Source account (ATA)
 * @param destination  Destination account (ATA)
 * @param owner        Owner of the source account
 * @param amount       Number of tokens to transfer
 * ...
 *
 * @return Instruction to add to a transaction
 */
export function createTransferInstruction(
    source: PublicKey,
    destination: PublicKey,
    owner: PublicKey,
    amount: number | bigint,
    ...
): TransactionInstruction
```

&#x20;Let's start by creating the associated token account for the recipient account.

> In another guide, we will see how to lazily create the recipient ata.

```typescript
describe("spl-transfer", async () => {
  it("It transfers tokens every 10s", async () => {
    ...
    
    // Prepare dest
    const dest = Keypair.generate().publicKey;
    const destAta = (await getOrCreateAssociatedTokenAccount(
      connection,
      payer,
      mint,        // the address of the mint
      dest,
      false        // is dest a pda?
    )).address;
    console.log(`dest: ${dest}, destAta: ${destAta}`);    
  });
});
```

Then, let's start do the same with the source account. I have already prepared a function called `fundSource` which helps fund our source account with some SPL token. You probably won't need this in a real world scenario.

```typescript
describe("spl-transfer", async () => {
  it("It transfers tokens every 10s", async () => {
    // Prepare dest
    ...
    
    // Prepare source
    const source = ?
    const [sourceAta] = await fundSource(connection, payer, source);
    console.log(`source: ${source}, sourceAta: ${sourceAta}`);
  });
});
```

**Let's talk about the elephant in the room, who should be the source account?**

When doing a a transfer we need to deduct fund and authorize this debit, thus source should be a signer. This works fine in a traditional scenario, you provide the signer when submitting the transaction and voila!

When working with Threads, we schedule our instructions to be executed by Threads, more precisely by the Clockwork thread program. For this reason, the signer for your automated instruction is actually your **thread**:

```typescript
  it("It transfers tokens every 10s", async () => {
    // Prepare dest
    ...
    
    // Prepare source
    const threadId = "spljs" + new Date().getTime();
    const [thread] = clockworkProvider.getThreadPDA(
      provider.wallet.publicKey,  // thread authority
      threadId                    // thread id
    );
    console.log(`Thread id: ${threadId}, address: ${thread}`);

    // We will use the thread pda as the source and fund it with some tokens
    const source = thread;
    const [sourceAta] = await fundSource(connection, payer, source);
    console.log(`source: ${source}, sourceAta: ${sourceAta}`);
  });
});    
```

## 4. Scheduling a SPL token transfer instruction

Now that we have the ingredients in place, we can finally build our SPL token transfer instruction and schedule a thread to run this instruction:

```typescript
it("Transfers SOL every 10 seconds", async () => {
  ...
  
  // 1️⃣ Build the SPL Transfer Instruction
  const targetIx = createTransferInstruction(sourceAta, destAta, source, amount);

  // 2️⃣  Define a trigger condition for the thread.
  const trigger = {
    cron: {
      schedule: "*/10 * * * * * *",
      skippable: true,
    },
  };

  // 3️⃣  Create the thread.
  const ix = await clockworkProvider.threadCreate(
    provider.wallet.publicKey,    // authority
    threadId,                     // id
    [targetIx],                   // instructions to execute
    trigger,                      // trigger condition
    LAMPORTS_PER_SOL              // amount to fund the thread with for execution fees
  );
  const tx = new Transaction().add(ix);
  const sig = await clockworkProvider.anchorProvider.sendAndConfirm(tx);
  console.log(`Thread created: ${sig}`);
});
```

We can see the `threadCreate` function asks for 5 arguments. These include some basic information needed to initialize the thread account.

* `authority` – The owner of the thread. This account must be the transaction signer and will have permission to delete, pause, resume, stop, and update the thread.
* `id` – An identifier for the thread (can also use buffer or vec u8).
* `instructions` – The list of instructions to execute when the trigger condition becomes valid.
* `trigger` – The trigger condition for the thread. When this condition is valid, the thread will begin executing the provided instructions. You can read more about [triggers](https://docs.clockwork.xyz/developers/threads/triggers).
* `amount` – The number of lamports to fund the thread account with. Remember to provide a small amount of SOL. Read more about how fees are calculated [here](https://docs.clockwork.xyz/developers/threads/fees).

## 5. Running the tests

Now we need to get our app running. If you have not done so already, you will need to install the Clockwork CLI by running the cargo command below. If you face any trouble here, please refer to the [**installation**](https://docs.clockwork.xyz/welcome/installation) docs.&#x20;

```shell
cargo install -f --locked clockwork-cli
```

Now that we have Clockwork installed, we can go ahead and spin up a local Clockwork node:

```bash
clockwork localnet
```

In a separate terminal window, we'll run the test:

```bash
yarn test
```

## 6. Monitoring our automation

If you setup everything correctly, you can now watch your automated program run all on its own. Grab the Clockwork explorer link that was printed out to the console. Using the Clockwork explorer, you can get simulation logs and inspect if your thread is not running and why. For example, here's mine: <https://app.clockwork.xyz/threads/GB7YgYK3bKF8J4Rr9Z2oeA3hwxrJdvW5zgXuNaxWWmUF?cluster=devnet>

<figure><img src="https://2516514367-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F64lLSRIas17CYMPkc7Zc%2Fuploads%2F89lrpQPS9vE6MAyTIZIh%2Fimage.png?alt=media&#x26;token=3aa2cafa-12e4-4afa-82bd-b14511b0668f" alt=""><figcaption></figcaption></figure>

Of course you can also look up your thread account in your favorite Solana explorer. You can alternatively use the Solana CLI to stream program logs by running the command provided below. Here's [**an example thread**](https://explorer.solana.com/address/3ohRKgNyLS1iTGiUqnzoiFiQcrCLGmr3NWHzq4HW8BdJ?cluster=devnet) that was created in a test on May 24th, 2023.

```bash
solana logs YOUR_PROGRAM_ID
```

<figure><img src="https://user-images.githubusercontent.com/8634334/222591908-bbaa04c5-83b4-46c2-b83b-68e1fef473eb.png" alt=""><figcaption></figcaption></figure>

## Key insights

1. Threads are an automation primitive for Solana.
2. You can use threads to automate any program instruction on Solana.&#x20;
3. [**Triggers**](https://docs.clockwork.xyz/reference/threads/triggers) allow you to define when a thread should begin execution.
4. Threads must be funded with a small amount of SOL to pay for [**automation fees**](https://docs.clockwork.xyz/reference/threads/fees).&#x20;
5. The signer for your instruction is your thread pda.

## Appendix

This guide was written using the following environment dependencies.

<table><thead><tr><th width="340">Dependency</th><th>Version</th></tr></thead><tbody><tr><td>Anchor</td><td>v0.27.0</td></tr><tr><td>Clockwork</td><td>v2.0.17</td></tr><tr><td>Clockwork TS SDK</td><td>v0.3.4</td></tr><tr><td>Rust</td><td>v1.65.0</td></tr><tr><td>Solana</td><td>v1.14.16</td></tr><tr><td>Ubuntu</td><td>v20.04</td></tr></tbody></table>

## Continue learning

* A complete copy of all code provided in this guide can be found in the [**examples repo**](https://github.com/clockwork-xyz/examples) on GitHub.
* Ask questions on [**Discord**](https://discord.gg/epHsTsnUre).

# 2. Auto-incrementing counter

## Goals

In this guide, we will learn how programs can create and manage threads directly using [**CPIs**](https://docs.solana.com/developing/programming-model/calling-between-programs#cross-program-invocations)**.**

1. Learn how to create a thread via CPI.
2. Build an automated counter program that increments itself.
3. Secure our program endpoints against spam and unwanted callers.&#x20;

{% hint style="info" %}
All code are open source and tested, feel free to grab and fork the [**examples**](https://github.com/clockwork-xyz/examples)**.**
{% endhint %}

## 1. Building a counter program

```bash
anchor init counter
cd counter
```

Let's begin by opening up the program file located at `programs/counter/src/lib.rs`. Here, we'll build a simple counter program that tracks an incrementing integer.&#x20;

1. `struct Counter` – We start by defining a `Counter` account to hold our counter state.
2. `fn increment()` – We declare an instruction to increment the counter value.
3. `struct Increment<'info>` – We create an [**Anchor accounts struct**](https://www.anchor-lang.com/docs/the-accounts-struct) to set up constraints on the `increment` instruction. We will see in the next section,  how to use the `thread` and `thread_authority` fields.

```rust
use anchor_lang::prelude::*;

// 1️⃣ We define an account to hold our counter state
#[account]
pub struct Counter {
    pub current_value: u64, // the value of the counter
    pub updated_at: i64,    // last time the counter has been updated
}

#[program]
pub mod counter {
    use super::*;
    
    // 2️⃣ We define an instruction to mutate the `Counter`
    pub fn increment(ctx: Context<Increment>) -> Result<()> {    
        ctx.accounts.counter.current_value = ctx.accounts.counter.current_value.checked_add(1).unwrap();
        ctx.accounts.counter.updated_at = Clock::get().unwrap().unix_timestamp;
        Ok(())
    }
}

/// Seed for `Counter` account Program Derived Address
/// ⚠ Make sure it matches whatever you are using on the client-side
pub const SEED_COUNTER: &[u8] = b"counter";

// 3️⃣ We define constraints for the `increment` instruction with Anchor macros
#[derive(Accounts)]
pub struct Increment<'info> {
     /// The counter account.
    #[account(mut, seeds = [SEED_COUNTER], bump)]
    pub counter: Account<'info, Counter>,

    /// Verify that only this thread can execute the Increment Instruction
    #[account(signer, constraint = thread.authority.eq(&thread_authority.key()))]
    pub thread: Account<'info, Thread>,

    /// The Thread Admin
    /// The authority that was used as a seed to derive the thread address
    /// `thread_authority` should equal `thread.thread_authority`
    #[account(seeds = [THREAD_AUTHORITY_SEED], bump)]
    pub thread_authority: SystemAccount<'info>,
}
```

## 2. Getting familiar with the thread program

In the previous guide, we created threads using the Typescript SDK. In Solana, everything is an account and threads are no different. We were just asking the Clockwork thread program to create thread accounts for us. Similar to the Token Program maintained by the Solana team, the Clockwork Thread Program is a program deployed and maintained by the Clockwork team.

Instead of submitting transactions to the RPC, we can very well interact with that program using CPIs. Here's an example of instructions provided by the [**thread program**](https://docs.rs/clockwork-sdk/latest/clockwork_sdk/cpi/index.html) via the [**Clockwork SDK**](https://crates.io/crates/clockwork-sdk) for programs.

* [`thread_create`](https://docs.rs/clockwork-sdk/latest/clockwork_sdk/cpi/fn.thread_create.html) – Create a Thread with a target instruction to run.
* [`thread_delete`](https://docs.rs/clockwork-sdk/latest/clockwork_sdk/cpi/fn.thread_delete.html) –  Delete a Thread and withdraw the funds.
* [`thread_pause`](https://docs.rs/clockwork-sdk/latest/clockwork_sdk/cpi/fn.thread_pause.html) – Pause a Thread execution.
* [`thread_resume`](https://docs.rs/clockwork-sdk/latest/clockwork_sdk/cpi/fn.thread_resume.html) – Resume a Thread execution.
* [`thread_update`](https://docs.rs/clockwork-sdk/latest/clockwork_sdk/cpi/fn.thread_update.html) – Update a Thread settings; instructions, triggers, etc.

## 3. Creating a thread via CPI

We will take the increment counter instruction and instead of running it by ourselves, we create a thread and make it increment the counter on our behalf. Let's create that thread, instead of crafting the instructions by hand, let's install the[**Clockwork SDK**](https://crates.io/crates/clockwork-sdk):

```bash
cargo add clockwork-sdk@~2.0.1
```

Let's head back to our program file located at `programs/counter/src/lib.rs`, what follows are the typical steps to create a thread via CPI:

1. `target_ix` – We start by defining the instruction to run by our thread.
2. `trigger` – We define the conditions for our thread to wake and execute.
3. `clockwork_sdk::cpi::thread_create` – We use this helper to create thread CPI.

```rust
use anchor_lang::prelude::*;
use anchor_lang::InstructionData;
use anchor_lang::solana_program::{
    instruction::Instruction,
    native_token::LAMPORTS_PER_SOL,
    system_program
};

// 0️⃣ Import the Clockwork SDK.
use clockwork_sdk::state::{Thread, ThreadAccount};

...

pub mod counter {
    ...
    pub fn increment(ctx: Context<Increment>) -> Result<()> { ... }
    
    pub fn initialize(ctx: Context<Initialize>, thread_id: Vec<u8>)
     -> Result<()> {
        // Get accounts.
        let system_program = &ctx.accounts.system_program;
        let clockwork_program = &ctx.accounts.clockwork_program;
        let payer = &ctx.accounts.payer;
        let thread = &ctx.accounts.thread;
        let thread_authority = &ctx.accounts.thread_authority;
        let counter = &mut ctx.accounts.counter;
    
        // 1️⃣ Prepare an instruction to automate. 
        //    In this case, we will automate the Increment instruction.
        let target_ix = Instruction {
            program_id: ID,
            accounts: crate::accounts::Increment {
                counter: counter.key(),
                thread: thread.key(),
                thread_authority: thread_authority.key(),
            }
            .to_account_metas(Some(true)),
            data: crate::instruction::Increment {}.data(),
        };
    
        // 2️⃣ Define a trigger for the thread.
        let trigger = clockwork_sdk::state::Trigger::Cron {
            schedule: "*/10 * * * * * *".into(),
            skippable: true,
        };
    
        // 3️⃣ Create a Thread via CPI
         let bump = *ctx.bumps.get("thread_authority").unwrap();
        clockwork_sdk::cpi::thread_create(
            CpiContext::new_with_signer(
                clockwork_program.to_account_info(),
                clockwork_sdk::cpi::ThreadCreate {
                    payer: payer.to_account_info(),
                    system_program: system_program.to_account_info(),
                    thread: thread.to_account_info(),
                    authority: thread_authority.to_account_info(),
                },
                &[&[THREAD_AUTHORITY_SEED, &[bump]]],
            ),
            LAMPORTS_PER_SOL,       // amount
            thread_id,              // id
            vec![target_ix.into()], // instructions
            trigger,                // trigger
        )?;
    
        Ok(())
    }
}

/// Seed for deriving the `Counter` account PDA.
pub const SEED_COUNTER: &[u8] = b"counter";

/// Seed for thread_authority pda
/// ⚠️ Make sure it matches whatever you are using on the client-side
pub const THREAD_AUTHORITY_SEED: &[u8] = b"authority";

#[derive(Accounts)]
#[instruction(thread_id: Vec < u8 >)]
pub struct Initialize<'info> {
    /// The counter account to initialize.
    #[account(
        init,
        payer = payer,
        seeds = [SEED_COUNTER],
        bump,
        space = 8 + std::mem::size_of::< Counter > (),
    )]
    pub counter: Account<'info, Counter>,

    /// The signer who will pay to initialize the program.
    /// (not to be confused with the thread executions).
    #[account(mut)]
    pub payer: Signer<'info>,

    /// The Clockwork thread program.
    #[account(address = clockwork_sdk::ID)]
    pub clockwork_program: Program<'info, clockwork_sdk::ThreadProgram>,

    /// The Solana system program.
    #[account(address = system_program::ID)]
    pub system_program: Program<'info, System>,

    /// Address to assign to the newly created thread.
    #[account(mut, address = Thread::pubkey(thread_authority.key(), thread_id))]
    pub thread: SystemAccount<'info>,

    /// The pda that will own and manage the thread.
    #[account(seeds = [THREAD_AUTHORITY_SEED], bump)]
    pub thread_authority: SystemAccount<'info>,
}
```

Finally, the trickiest part is to define our `Initialize` instruction constraints with Anchor macros properly. Note that the thread [authority](https://docs.clockwork.xyz/reference/threads/authority) is a PDA account. Only this program has the authority to administrate the thread; pause, start, create, delete the thread, etc.

## 4. Testing our automation

Let's add a test case to initialize our program and get it running. Here, we will simply calculate the required PDAs and call our program's `Initialize` instruction. From there, our program will create a thread and begin running all on its own.

{% code overflow="wrap" %}

```typescript
...
import { ClockworkProvider } from "@clockwork-xyz/sdk";

const provider = anchor.AnchorProvider.env();
anchor.setProvider(provider);
const wallet = provider.wallet;
const program = anchor.workspace.Counter as Program<Counter>;
const clockworkProvider = ClockworkProvider.fromAnchorProvider(provider);


it("It increments every 10 seconds", async () => {    
    // 1️⃣ Prepare thread address
    const threadId = "counter";
    const [threadAuthority] = PublicKey.findProgramAddressSync(
        // Make sure it matches on the prog side
        [anchor.utils.bytes.utf8.encode("authority")], 
        program.programId
    );
    
    const [threadAddress, threadBump] = clockworkProvider.getThreadPDA(threadAuthority, threadId)
    
    // 2️⃣ Ask our program to initialize a thread via CPI
    // and thus become the admin of that thread
   await program.methods
    .initialize(Buffer.from(threadId))
    .accounts({
        payer: wallet.publicKey,
        systemProgram: SystemProgram.programId,
        clockworkProgram: clockworkProvider.threadProgram.programId,
        thread: threadAddress,
        threadAuthority: threadAuthority,
        counter: counter,
    })
    .rpc();
}
```

{% endcode %}

Finally, let's run the test using `anchor test`. You modify the test to print the thread address and look up the thread in your favorite Solana explorer. You should see the counter being auto-increment every 10 seconds by our thread.

<figure><img src="https://2516514367-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F64lLSRIas17CYMPkc7Zc%2Fuploads%2FAcWc1klgfFmy50zsZVBJ%2Fimage.png?alt=media&#x26;token=51632552-5f70-4db3-84a5-9d3da5fb29e7" alt=""><figcaption></figcaption></figure>

## Key Learnings

1. Programs can create threads via CPIs.&#x20;
2. When creating threads via CPIs, use a "program authority" PDA to act as the owner of the thread and manage its permissions.&#x20;

## Appendix

This guide was written using the following environment dependencies.

<table><thead><tr><th width="340">Dependency</th><th>Version</th></tr></thead><tbody><tr><td>Anchor</td><td>v0.26.0</td></tr><tr><td>Clockwork</td><td>v2.0.1</td></tr><tr><td>Clockwork TS SDK</td><td>v0.3.0</td></tr><tr><td>Rust</td><td>v1.65.0</td></tr><tr><td>Solana</td><td>v1.14.16</td></tr><tr><td>Ubuntu</td><td>v20.04</td></tr></tbody></table>

## Learn more

* A complete copy of all code provided in this guide can be found in the [**examples repo**](https://github.com/clockwork-xyz/examples/tree/main/2-counter)[](https://github.com/clockwork-xyz/examples/tree/main/1-counter)on GitHub.
* Ask questions on [**Discord**](https://discord.gg/epHsTsnUre).

# Threads

**Threads** are an automation primitive for Solana developers. Just as traditional applications use threads to execute instructions on a computer, smart-contracts can use Clockwork threads to execute a series of instructions on Solana. To create a thread, developers must provided two critical pieces of information:

1. **A trigger** – Some scenario or condition that will gate execution and can verified by a smart-contract.
2. **A set of instructions** – These are instructions that will be executed. They can be either statically defined or built dynamically at runtime.

# Account

{% embed url="<https://github.com/clockwork-xyz/clockwork/blob/main/programs/thread/src/state/thread.rs>" %}
thread.rs
{% endembed %}

On Solana, we often say that everything is an account. Threads are no different. A thread account simply holds the on-chain state needed to schedule and execute a series of static and/or dynamic instructions on Solana.&#x20;

```rust
pub struct Thread {
    /// The owner of this thread.
    pub authority: Pubkey,
    /// The bump, used for PDA validation.
    pub bump: u8,
    /// The cluster clock at the moment the thread was created.
    pub created_at: ClockData,
    /// The context of the thread's current execution state.
    pub exec_context: Option<ExecContext>,
    /// The number of lamports to payout to workers per execution.
    pub fee: u64,
    /// The id of the thread, given by the authority.
    pub id: Vec<u8>,
    /// The instructions to be executed.
    pub instructions: Vec<SerializableInstruction>,
    /// The name of the thread.
    pub name: String,
    /// The next instruction to be executed.
    pub next_instruction: Option<SerializableInstruction>,
    /// Whether or not the thread is currently paused.
    pub paused: bool,
    /// The maximum number of execs allowed per slot.
    pub rate_limit: u64,
    /// The triggering event to kickoff a thread.
    pub trigger: Trigger,

}
```

# Address

{% embed url="<https://github.com/clockwork-xyz/clockwork/blob/781b42fd06f2926899597ce5ea1f19b8ecd3d2e4/programs/thread/src/state/thread.rs#L38>" %}
fn pubkey()
{% endembed %}

A thread's **public address** is derived deterministically from its `authority` and `id`. These properties are immutable and may never change throughout the lifetime of the thread account. To verify a Clockwork thread account in your programs, you can use the `pubkey()` helper function provided by the SDK:

```rust
#[account(
    address = thread.pubkey(),
    constraint = thread.id.eq("my_thread"),
    has_one = authority,
)]
pub thread: Account<'info, Thread>
```

# Authority

{% embed url="<https://github.com/clockwork-xyz/clockwork/blob/781b42fd06f2926899597ce5ea1f19b8ecd3d2e4/programs/thread/src/state/thread.rs#L11>" %}
authority: Pubkey
{% endembed %}

On Solana, the **“authority”** property is often used by convention to refer to the user-space owner of a particular account. For Clockwork, a thread's authority is its creator – the account which signed the transaction to create the thread. A thread's authority has the following permissions:

* Pause and resume the thread.
* Update the thread’s `trigger` and `instructions`.
* Withdraw from the thread’s balance.
* Close the thread account.

An authority may be any valid public address (i.e. a wallet pubkey or PDA). When the authority is a PDA, we occasionally refer to this as a “program authority” since the account is managed by a program. If you are unfamiliar with PDAs, the Solana Cookbook has a [great writeup](https://solanacookbook.com/core-concepts/pdas.html) on what they are and how to build secure programs with them.

# Fees

{% embed url="<https://github.com/clockwork-xyz/clockwork/blob/781b42fd06f2926899597ce5ea1f19b8ecd3d2e4/programs/thread/src/state/thread.rs#L19>" %}
fee: u64
{% endembed %}

**Fees** are a cost, paid by threads (and their funders), for the automation services provided by the workernet. The automation fee base fee is **0.000001 SOL / executed instruction.** Thread creators may choose to set a higher fees to prioritize their threads with worker network.&#x20;

# Payers

{% embed url="<https://github.com/clockwork-xyz/clockwork/blob/781b42fd06f2926899597ce5ea1f19b8ecd3d2e4/utils/src/thread.rs#L13>" %}
PAYER\_PUBKEY: Pubkey
{% endembed %}

Anchor currently does not support PDAs as payers for account initialization. This means that if one of your automated instructions initializes a new account, you must specify a keypair signer as the `payer`. For this, we provide a special Clockwork payer address:

```rust
C1ockworkPayer11111111111111111111111111111
```

You can import that address with the [Typescript SDK](https://www.npmjs.com/package/@clockwork-xyz/sdk):

```typescript
import { PAYER_PUBKEY } from "@clockwork-xyz/sdk";
```

You can import that address with the [Rust SDK](https://docs.rs/clockwork-sdk/latest/clockwork_sdk/utils/static.PAYER_PUBKEY.html):

```rust
use clockwork_sdk::utils::PAYER_PUBKEY;
```

If an account in your automated instruction references the Clockwork payer account, workers will automatically inject their address in its place. By doing this, the worker node will pay for any account initializations your program needs to do, and Clockwork will reimburse the worker from your thread's account balance.

{% hint style="info" %}
When Anchor adds support for PDA payers (expected in the next release), this “dynamic payer” feature may be deprecated in favor of using PDAs to pay for account initializations.

<https://github.com/coral-xyz/anchor/pull/1938>
{% endhint %}

# Triggers

{% embed url="<https://github.com/clockwork-xyz/clockwork/blob/781b42fd06f2926899597ce5ea1f19b8ecd3d2e4/utils/src/thread.rs#L46>" %}
enum Trigger
{% endembed %}

Clockwork provides 5 different **trigger conditions** for scheduling a thread's execution. These trigger conditions support a wide variety of use-cases and allow you to subscribe to time-based as well as event-based changes. If none of the trigger conditions currently provided support your team's use-case, please reach out in the [**Clockwork Discord**](https://docs.clockwork.xyz/reference/localnet) to propose a new one.

### Account

Allows a thread to begin execution whenever an account's data changes. This can be useful for listening to account updates, process realtime events, or subscribing to an oracle data stream. This trigger type requires 3 arguments.

* `address` – The address of the account to listen to.
* `offset` – The byte offset of the account data to monitor.
* `size` – The size of the byte slice to monitor (must be less than 1kb).

### Cron

Allows a thread to begin execution whenever a [**cron schedule**](https://en.wikipedia.org/wiki/Cron) is valid. This can be useful for scheduling one-off or periodically recurring actions. This trigger type requires 2 arguments.

* `schedule` – A schedule in cron syntax.&#x20;
* `skippable` – Boolean value indicating whether an scheduled invocation can be skipped if the Solana network is unavailable. If false, any missed invocations will be executed as soon as the Solana network is online.&#x20;

### Now

Allows a thread to begin execution immediately. This can be useful when a new calculation needs to be immediately kicked off. This trigger condition takes no arguments.

### Slot

Allows a thread to begin executing when a specified slot has passed. This can be useful for scheduling processes related to staking an Solana epoch transitions. This trigger condition requires 1 argument.

* `slot` – The slot to begin execution on.&#x20;

### Epoch

Allows a thread to begin executing when a specified epoch becomes active. This can be useful for scheduling processes related to staking and Solana epoch transitions. This trigger condition requires 1 argument.&#x20;

* `epoch` – The epoch to begin execution on.&#x20;

### Timestamp

Allows a thread to begin executing when a specified unix timestamp has passed. This can be useful for scenarios where you have an exact date in the future when you want a program to begin running.

* `unix_ts` – The unix timestamp to begin execution on.&#x20;

### Pyth

Allows a thread to begin executing when a price threshold has been crossed. This can be useful for scheduling actions that are driven by price movements such as automated stop-loss and take-profit orders.&#x20;

* `price_feed` – The Pyth price feed account to monitor. Please refer to the [**Pyth website**](https://pyth.network/price-feeds?cluster=mainnet-beta) for these addresses.
* `equality` – The equality operator (≥ or ≤) used to compare the the price feed to the limit price.
* `limit` – The limit price to compare the price feed to. When this threshold has been crossed, the thread will execute.&#x20;

# Localnet

## Run a local Clockwork node

To deploy Clockwork on your machine for local development, you must first [**install the CLI**](https://docs.clockwork.xyz/welcome/installation). When this is done, you can launch a local Clockwork instance with the following command:

```bash
clockwork localnet
```

## Deploy your program

To deploy your own programs to the localnet, you can use either the Anchor CLI, Clockwork CLI, or Solana CLI. As a shortcut, the Clockwork CLI provides a `--bpf-program` flag for deploying the localnet with a pre-built program binary.&#x20;

{% tabs %}
{% tab title="Anchor" %}

```sh
anchor deploy
```

{% endtab %}

{% tab title="Clockwork" %}

```sh
clockwork localnet \
    --bpf-program <ADDRESS_OR_KEYPAIR> <PROGRAM_FILEPATH>
```

{% endtab %}

{% tab title="Solana" %}

```bash
solana program deploy \ 
    --program-id <ADDRESS_OR_KEYPAIR> <PROGRAM_FILEPATH>
```

{% endtab %}
{% endtabs %}

The Clockwork localnet additionally works out of the box with your Anchor tests. To run Anchor tests with the localnet, use the following command:

```sh
anchor test --skip-local-validator
```

## Stream logs

To stream logs from your localnet, you can use the Solana CLI.

```bash
solana logs --url l
```

# SDK

## Rust

For Rust clients and on-chain CPI integrations, use the `clockwork-sdk` crate.&#x20;

{% embed url="<https://crates.io/crates/clockwork-sdk>" %}

## Typescript

For Typescript clients and frontend integrations, use the `@clockwork-xyz/sdk` package.

{% embed url="<https://www.npmjs.com/package/@clockwork-xyz/sdk>" %}

# Support

{% hint style="info" %}
If you have a question, you can ask the community in the [**Clockwork Discord**](https://discord.gg/6zGyWF7mP4). If you would rather have a private word with the team, please file a ticket in the support channel.&#x20;
{% endhint %}

## Why is my thread not executing?

* Is your thread funded account with enough SOL? Check it's balance and airdrop some SOL to it. See the [**Fees**](https://docs.clockwork.xyz/reference/broken-reference) section for more information.
* Is your thread paused? Check its status in the [**Clockwork explorer**](https://app.clockwork.xyz/?cluster=devnet).
* Check for programming errors. Use the [**Clockwork explorer**](https://app.clockwork.xyz/?cluster=devnet) to browse for your thread and click the check if your thread is able to simulate your instructions without errors.&#x20;

#### Common errors

> InstructionDidNotDeserialize and others

Serialization errors can happen when there is a mismatch between your validator's clockwork engine version and the clockwork libraries you are using. Naturally these two need to match:

* Note the version of your `clockwork-client`
* Note the version of your `clockwork-sdk`
* Make sure to checkout and run the same version of the clockwork engine.

> (code -32002) Transaction simulation failed: Attempt to load a program that does not exist

This often happens on localnet. You are probably trying to create a thread by calling the thread program, but that program cannot be found. This is most likely due to running `solana-test-validator` or `anchor localnet` instead of `clockwork localnet`.

> I see in the validator logs: "Expected an executable account"

You created a thread, but that thread is trying to execute an instruction whose program does not exist (hence the not an executable account). You haven't deployed your program yet.

## How can my instruction pay for account initialization?

<https://docs.clockwork.xyz/developers/threads/payers>

## Why is localnet not working?

> My validator stopped after ⠚ Initializing..

The Clockwork plugins depends on a specific of Solana *(for know we recommend that you use the exact same version)*. Make sure your Solana validator uses the same version as Clockwork by installing it again if needed `solana-install init x.y.z`.

* Check the [**release notes**](https://github.com/clockwork-xyz/clockwork/releases) in doubt.
* If for some reason you cannot install the same version, please talk to us.

> How do I know which version of Solana the Clockwork Engine (geyser plugin) depends on?

Run `cat test-ledger/validator.log | grep "crate-info"`

## How do I write a cron schedule?

The easiest way to test your cron string before even playing with thread, is to install the [**clockwork-cli**](https://docs.clockwork.xyz/localnet#1.-install-the-clockwork-cli) and run `clockwork crontab YOUR_STRING`.

You can use [**https://crontab.guru**](https://crontab.guru/) as reference to build your cron string. Note that crontab guru is a 5 columns cron while the Clockwork [**cron parser**](https://github.com/clockwork-xyz/clockwork/tree/main/cron) is a 7 columns cron. It includes **seconds** (left most column) and **year** (right most column).

### Anchor 0.28

We don't support anchor 0.28 yet, if you encounter build issue related to -

* AnchorDeserialize not implemented
* spl-token-2022 failed to compile

Please check these two solutions:

{% embed url="<https://discord.com/channels/889725689543143425/951718079925202954/1126059435995955281>" %}

{% embed url="<https://discord.com/channels/889725689543143425/951718079925202954/1124240787379597312>" %}

# Deploy a worker

## 1. Download the geyser plugin

To turn your Solana validator or RPC into a Clockwork worker, you simply need to install the Clockwork [geyser plugin](https://docs.solana.com/developing/plugins/geyser-plugins). You can get the binary either by [building from source](https://docs.clockwork.xyz/reference/localnet#build-from-source) or installing the pre-built binary:

```
curl -s https://api.github.com/repos/clockwork-xyz/clockwork/releases/latest | grep "clockwork-geyser-plugin-release-x86_64-unknown-linux-gnu.tar" | cut -d : -f 2,3 | tr -d \" | wget -qi -
tar -xjvf clockwork-geyser-plugin-release-x86_64-unknown-linux-gnu.tar.bz2
rm clockwork-geyser-plugin-release-x86_64-unknown-linux-gnu.tar.bz2
```

## 2. Create a keypair

Next, create a new keypair for signing Clockwork txs. Load this keypair with a small amount of SOL (\~0.01 ◎). You will be compensated for lamports spent by the transactions your worker automates.&#x20;

```
solana-keygen new -o clockwork-worker-keypair.json
```

Create a System Account for this key by funding the address with at least 0.1 ◎ SOL.

```bash
solana balance $(solana address -k clockwork-worker-keypair.json)
```

## 3. Get a worker ID

Register your worker and get a worker ID:

```
clockwork worker create clockwork-worker-keypair.json
```

## 4. Configure your node

Then, setup the plugin config file in a folder where your validator startup script can reference it. Note, the `libpath` and `keypath` values should point to the binary and keypair mentioned in the steps above.

```
{
  "libpath": "/home/sol/clockwork-geyser-plugin-release/lib/libclockwork_plugin.so",
  "keypath": "/home/sol/clockwork-worker-keypair.json",
  "rpc_url": "http://127.0.0.1:8899",
  "transaction_timeout_threshold": 150,
  "thread_count": 10,
  "worker_id": 👈 Set this to your worker ID!
}
```

## 5. Restart your validator

Finally, add an additional line to your startup script to run your validator with the Clockwork plugin (often located at `/home/sol/bin/validator.sh`):

```
#!/bin/bash

exec solana-validator \
    --identity /home/sol/validator-keypair.json \
    --known-validator dv1ZAGvdsz5hHLwWXsVnM94hWf1pjbKVau1QVkaMJ92 \
    --known-validator dv2eQHeP4RFrJZ6UeiZWoc3XTtmtZCUKxxCApCDcRNV \
    --known-validator dv4ACNkpYPcE3aKmYDqZm9G5EB3J4MRoeE7WNDRBVJB \
    --known-validator dv3qDFk1DTF36Z62bNvrCXe9sKATA6xvVy6A798xxAS \
    --only-known-rpc \
    --full-rpc-api \
    --no-voting \
    --ledger /mnt/ledger \
    --accounts /mnt/accounts \
    --log /home/sol/solana-rpc.log \
    --rpc-port 8899 \
    --rpc-bind-address 0.0.0.0 \
    --dynamic-port-range 8000-8020 \
    --entrypoint entrypoint.devnet.solana.com:8001 \
    --entrypoint entrypoint2.devnet.solana.com:8001 \
    --entrypoint entrypoint3.devnet.solana.com:8001 \
    --entrypoint entrypoint4.devnet.solana.com:8001 \
    --entrypoint entrypoint5.devnet.solana.com:8001 \
    --expected-genesis-hash EtWTRABZaYq6iMfeYKouRu166VU2xqa1wcaWoxPkrZBG \
    --wal-recovery-mode skip_any_corrupted_record \
    --limit-ledger-size \
    
    # Add this line! 👇🏼
    --geyser-plugin-config /home/sol/geyser-plugin-config.json
```

Now simply restart your validator however you normally would!<br>
