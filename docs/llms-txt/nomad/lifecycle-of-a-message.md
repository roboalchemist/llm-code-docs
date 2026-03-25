# Source: https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging/lifecycle-of-a-message.md

# Lifecycle of a Message

In this document, we'll walk through an end-to-end example of sending a cross-chain message using Nomad.

![Cross-chain message lifecycle](https://lh4.googleusercontent.com/wcEcZaPvz61_fWomSFmaK_khv8Vv9Pj_lWoWskPVsJ1k6aezPsbXDMRlAvtPRh06twfnvNlC0Xgxcd-K87sYX9eV-OfSbECTBK8sek7QLbuYK_gJXU8lr-TGK1rQuG3cB4w8t7oSflxzUjirgM_zRHQ)

Let's use an example of a user, Alice, who wants to send 1000 USDC from her account on Ethereum to the same one on Moonbeam, using the Nomad Token Bridge application.

{% hint style="info" %}
While this example will focus on the ERC-20 token bridging use case, the core logic on how messages get sent in the Nomad protocol is identical for all use cases.
{% endhint %}

### **1. User Initiates Action on Origin Chain**

The first step is Alice uses some interface (either the Token Bridge GUI or Etherscan) to construct a transaction to be sent to the BridgeRouter contract [deployed on Ethereum](https://etherscan.io/address/0x88a69b4e698a4b090df6cf5bd7b2d47325ad30a3).

[The BridgeRouter contract](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol) is an example of a xApp contract that follows [the Router pattern](https://docs.nomad.xyz/developers/application-developers/advanced/router-pattern). It exists as the entry point for users like Alice to interact with on the origin chain.

In this case, Alice's transaction will call the [`send` function](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L134) on the BridgeRouter.

### **2. xApp Dispatch Logic Executes on Origin Chain**

The BridgeRouter contract, triggered by Alice's transaction, will begin executing its business logic (as encoded by the app developer). In this case, it will:

* Perform basic validation (eg. `_amount > 0`)
* Check whether the token to be sent is local or remote (USDC is local)
* Accordingly escrow or burn the amount to be sent (USDC will be escrowed)
* Format the message to be sent, adhering to the [BridgeMessage](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeMessage.sol) contract

After the business logic is executed, the BridgeRouter contract will call `dispatch` on the Home contract, enqueuing the message to be sent.

### **3. Core Contract Logic Executes on Origin Chain**

Once [`dispatch`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L175) has been called on the Ethereum Home contract, the application router contract's job is done. This is where the Nomad protocol's work begins.

[The Home contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/home) formats and hashes the message, and inserts it into its Merkle tree. The Merkle tree in the Home contract is the core data structure in Nomad, and contains *all* the messages to be sent from that Home.

The new message is inserted as a leaf, and then merkelized to generate a new Merkle root, which is stored in the Home's queue. Finally, a `Dispatch` event is emitted, which signals to all relevant parties (ie. the Updater) that a new root has been generated.

### **4. Updater Signs an Update on the Origin Chain**

As new roots are generated, the Updater calls [the `update` function](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/Home.sol#L221) on the Ethereum Home contract, committing to the current root and the new root with their digital signature. This signature acts as an attestation on the accumulator root, which can now be relayed to a destination chain.

This function emits an `update` event which signals to Relayers that a new update has occurred.

### **5. Update is Relayed to the Replica on the Destination Chain**

Once an update has been made on the Home, anyone may call `update` on any [Replica contract](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts/replica) to effectively relay the new root to the destination chain.

{% hint style="info" %}
**Note two things:**

1. While this function has the same name `update`, it has completely different logic in a Replica contract.
2. An update on the Ethereum Home may be relayed to any number of Replicas corresponding to this Home, per [the broadcast channel model](https://docs.nomad.xyz/the-nomad-protocol/cross-chain-messaging/..#broadcast-channels). In this example, we will only cover the Moonbeam Replica.
   {% endhint %}

A Relayer (which is trustless and permissionless), will call `update` passing in the `_oldRoot`, `_newRoot`, and the `_signature` which the Updater generated. This will "kick off" the dispute window for the new root, after which messages can be proven and processed.

### **6. Message is Proven and Processed on the Destination Chain**

After [the dispute window](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period) elapses, individual messages (ie. Alice's transaction to bridge 1000 USDC) can be proved against the new root.&#x20;

To prove a message, anyone can call `prove` on the Replica contract, passing in a leaf corresponding to the message, merkle path and index of the leaf to prove inclusion in the new root.

If this succeeds, the message will be processed, meaning it will be forwarded to the corresponding application router on the destination chain.

In this case, a Processor (which is also trustless and permissionless) will prove inclusion of Alice's message in the new root, and then call `process` on the Replica. The Replica will then forward the message to the BridgeRouter contract on Moonbeam, and invoke [its `handle` function](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-bridge/contracts/BridgeRouter.sol#L105).

{% hint style="warning" %}
Astute readers may notice that we assumed that Nomad's optimistic dispute window elapsed without fraud being flagged. To learn more about how fraud detection, flagging and recovery works in Nomad, please check out [the Fraud documentation](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud) in the Security section.
{% endhint %}

### 7. **xApp Handle Logic Executes on Destination Chain**

Once `handle` is called on the Moonbeam BridgeRouter, the BridgeRouter will execute application business logic on its side to complete the bridging process for Alice. In this case, it will mint 1000 Nomad USDC (or madUSDC) to Alice's address on the Moonbeam side.&#x20;

{% hint style="info" %}
Note that the BridgeRouter contract is *isomorphic*, meaning has the same code deployed on both chains. As long as `dispatch` and `handle` are implemented, they will be able to communicate with each other, with messages brokered by Nomad's messaging passing layer.
{% endhint %}

Voila! We have successfully bridged tokens and sent a message via Nomad.
