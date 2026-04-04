# Source: https://docs.near.org/ai/shade-agents/getting-started/quickstart/components.md

---
id: components
title: Key Components
sidebar_label: Key Components
description: "Learn about the components of a simple Shade Agent."
---



In this section, we'll explore the main components of the [quickstart template](https://github.com/NearDeFi/shade-agent-template) to understand how to develop a Shade Agent. We'll also look at how to modify the template to build an agent for your use case.


---

## Template Structure

The template we're using is a simple Shade Agent built with Hono and written in TypeScript that acts as a verifiable ETH price oracle. It takes prices from two different APIs, takes the average, and then pushes the price to an Ethereum contract. The template also comes with a frontend to make it easier to interact with the Shade Agent.

The project has three different APIs:
1) [**agentAccount**](https://github.com/NearDeFi/shade-agent-template/blob/main/src/routes/agentAccount.ts) - This API simply fetches the agent's NEAR account ID and its balance by using the `agentAccountId` and `agent("getBalance")` functions from the `shade-agent-js` library.
2) [**ethAccount**](https://github.com/NearDeFi/shade-agent-template/blob/main/src/routes/ethAccount.ts) - This API returns the `Ethereum Sepolia account` that the Shade Agent uses to update the price of Ethereum in the Sepolia contract. This API is used so the user knows which account to fund for gas.
3) [**transaction**](https://github.com/NearDeFi/shade-agent-template/blob/main/src/routes/transaction.ts) - This is where the core logic of the agent is defined. When this API is called, the agent will build and sign a transaction. We'll look deeper into this API route in the next part.

---

## Signing Transactions

In the [transaction API Route](https://github.com/NearDeFi/shade-agent-template/blob/main/src/routes/transaction.ts), the `requestSignature` function from the `shade-agent-js` library is used to sign a transaction.

In this example, we're signing a transaction to call an Ethereum contract to update the stored price of ETH. First, we retrieve the price of ETH (in this example, the function queries two different APIs and calculates the average).

```
    const ethPrice = await getEthereumPriceUSD();
    if (!ethPrice) {
```

Next, we build the `transaction payload` to be signed. To do this, we're using the `chainsig.js` library.
Using this library, we:
1. `Derive the Ethereum address` that will be sending the transaction. This function takes the agent contract account ID since this is the predecessor account that is calling the Chain Signatures [MPC contract](https://github.com/Near-One/mpc/tree/main/libs/chain-signatures/contract), and a path. The path can be whatever string you like, different paths will derive different addresses.
2. Create the `data`. This is what action we're performing, in this case, a function call to update the price in the contract.
3. `Build the transaction and the transaction payload` by inputting the derived address, the target Ethereum smart contract, and the data.

```
  // Derive the price pusher Ethereum address
  const { address: senderAddress } = await Evm.deriveAddressAndPublicKey(
    contractId,
    "ethereum-1",
  );
  // Create a new JSON-RPC provider for the Ethereum network
  const provider = new JsonRpcProvider(ethRpcUrl);
  // Create a new contract interface for the Ethereum Oracle contract
  const contract = new Contract(ethContractAddress, ethContractAbi, provider);
  // Encode the function data for the updatePrice function
  const data = contract.interface.encodeFunctionData("updatePrice", [ethPrice]);
  // Prepare the transaction for signing 
  const { transaction, hashesToSign } = await Evm.prepareTransactionForSigning({
    from: senderAddress,
    to: ethContractAddress,
    data,
  });

```

Once we have the payload (also known as the hash), we can call the `requestSignature` function to sign the transaction. We specify the `keyType` as `Ecdsa` as we're signing for a blockchain that uses the `secp256k1` signature scheme.

```
    const signRes = await requestSignature({
      path: "ethereum-1",
      payload: uint8ArrayToHex(hashesToSign[0]),
      keyType: "Ecdsa",
    });
    console.log("signRes", signRes);
```

The result is the `signature`.

We then attach the signature to the Ethereum transaction and broadcast it to the target network.

```
    // Reconstruct the signed transaction
    const signedTransaction = Evm.finalizeTransactionSigning({
      transaction,
      rsvSignatures: [toRSV(signRes)],
    });

    // Broadcast the signed transaction
    const txHash = await Evm.broadcastTx(signedTransaction);

```

---

## Using Different Chains

We set up a chain adapter for Ethereum Sepolia in the [Ethereum.ts](https://github.com/NearDeFi/shade-agent-template/blob/main/src/utils/ethereum.ts) file using the `chainsig.js` library. This library allows us to easily construct transaction payloads to be signed by the agent.

```
// Set up a public client for the Ethereum network
const publicClient = createPublicClient({
  transport: http(ethRpcUrl),
});

// Set up a chain signatures chain adapter for the Ethereum network
export const Evm = new chainAdapters.evm.EVM({
  publicClient,
  contract: MPC_CONTRACT,
}) as any;

```

You can set up chain adapters for a variety of chains, including EVM, Bitcoin, NEAR, Solana, SUI, XRP, Cosmos, and more to allow your agent to interact with multiple different chains. You can see a full list of the chains currently supported [here](https://github.com/NearDeFi/chainsig.js/tree/main?tab=readme-ov-file#supported-chains), but feel free to contribute any chain that is not yet supported.

Implementation details differ slightly from chain to chain; as such, we recommend you review our [chain signature docs](../../../../chain-abstraction/chain-signatures/implementation.md). Note that step 3 of requesting a signature is different; we use the `requestSignature` function from `shade-agent-js` instead.

If you are using a chain that uses the `ed25519` signature scheme (NEAR, Solana, SUI, Aptos, etc.), you should specify the `keyType` as `Eddsa` when calling `requestSignature`.

---

## Next Steps

Now that you've explored the basics of Shade Agents, we recommend diving deeper into the [framework overview](../../concepts/framework-overview.md) to understand the core concepts needed for building production-ready Shade Agents.

<SigsSupport />