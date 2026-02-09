# Source: https://docs.near.org/web3-apps/tutorials/wallet-login.md

---
id: wallet-login
title: Wallet Login
description: "Connect users to NEAR wallets with a secure, sandbox-based connector library"
---



The `@hot-labs/near-connect` library provides a secure, zero-dependency wallet connector for NEAR blockchain with a unique sandbox-based architecture.

![Preview](https://github.com/user-attachments/assets/c4422057-38bb-4cd9-8bd0-568e29f46280)

:::tip Example

We have a [working example](https://github.com/near-examples/hello-near-connector), which you can easily get through `create-near-app`:

```bash
npx create-near-app@latest
```

:::

---

## Why NEAR Connect?

Unlike traditional wallet selectors, it offers a dynamic manifest system that allows wallets to be added and updated without requiring developers to update their dependencies.

- **Secure Execution**: Wallet scripts run in isolated sandboxed iframes for maximum security
- **Dynamic Wallets**: Wallets are loaded from a manifest and can be updated without code changes
- **Zero Dependencies**: Lightweight library with no external dependencies
- **Automatic Detection**: Supports both injected wallets (extensions) and manifest-based wallets

---

## Installation

You can add the NEAR Connect library to your project in two ways:

<Tabs>
  <TabItem value="manual" label="library">
  Install the `@hot-labs/near-connect` and `near-api-js` packages manually:

  ```bash
  npm install @hot-labs/near-connect near-api-js
  ```

  </TabItem>
  <TabItem value="hooks" label="hooks">
  If you are using React, we recommend installing the `near-connect-hooks` package which provides convenient hooks for integrating NEAR Connect into your app:

  ```bash
  npm install near-connect-hooks
  ```

  </TabItem>
</Tabs>

---

## Initializing the Connector

Initialize the `NearConnector` instance in your application:

<Tabs>
  <TabItem value="manual" label="library">
    ```
    const connector = new NearConnector({
      manifest: process.env.NODE_ENV === "production" ? undefined : "/near-connect/repository/manifest.json",
      providers: { mainnet: ["https://relmn.aurora.dev"] },
      walletConnect,
      network,
      logger,
    });

```
  </TabItem>
  <TabItem value="hooks" label="hooks">
     ```
import { Navigation } from "@/components/navigation";
import { NearProvider } from "near-connect-hooks";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <NearProvider>
      <Navigation />
      <Component {...pageProps} />
    </NearProvider>
  );
}

```
  </TabItem>
</Tabs>

<details>

<summary> Selecting Wallets </summary>

Unlike traditional wallet selectors that bundle wallet code, NEAR Connect uses a **manifest-based approach**:

1. Wallet providers register their integration scripts in a public manifest
2. The connector dynamically loads wallet scripts when users want to connect

This architecture eliminates the need to install individual wallet packages and ensures wallet code can be updated independently from your app.

```tsx
connector = new NearConnector({
  network: "testnet", // or "mainnet"
  features: {
    signMessage: true,  // Only show wallets that support message signing
    signTransaction: true,
    signInWithoutAddKey: true,
    signAndSendTransaction: true,
    signAndSendTransactions: true
  },
});
```

</details>

---

## Signing In / Out

<Tabs>
  <TabItem value="manual" label="library">
    The connector uses the Observer Pattern (pub/sub), for which we need to subscribe to the `wallet:signIn" and `wallet:signOut` events
    
    ```
    connector.on("wallet:signIn", async (t) => {
      setWallet(await connector.wallet());
      setAccount(t.accounts[0]);
    });

    connector.on("wallet:signOut", async () => {
      setWallet(undefined);
      setAccount(undefined);
    });

```

    Then, call the `connect` function to open a modal where the user can select a wallet and sign in, and `disconnect` to sign out

    ```
  const connect = async () => {
    if (networkAccount != null) return connector.disconnect();
    await connector.connect();
  };

```

  </TabItem>
  <TabItem value="hooks" label="hooks">
    The `near-connect-hooks` package provides a `useNearWallet` hook that simplifies the sign-in process, first import the hook:
    ```
import { useNearWallet } from 'near-connect-hooks';

```
    
    Then, import the `signIn` and `signOut` method from the hook and call them when needed:
    ```
   const { signedAccountId, loading, signIn, signOut } = useNearWallet();

  const handleAction = () => {
    if (signedAccountId) {
      signOut();
    } else {
      signIn();
    }
  };

```
  </TabItem>
</Tabs>

---

## Calling Contract Method

<Tabs>
  <TabItem value="manual" label="library">
    To call a contract method, first get the connected wallet instance using `connector.wallet()`, then use the wallet's `signAndSendTransaction` method to make a function call:

    ```tsx
    // Get the connected wallet
    const wallet = await connector.wallet();

    // Call a change method
    const result = await wallet.signAndSendTransaction({
      receiverId: "hello.near-examples.testnet",
      actions: [
        {
          type: "FunctionCall",
          params: {
            methodName: "set_greeting",
            args: { greeting: "Hello from NEAR Connect!" },
            gas: "30000000000000", // 30 TGas
            deposit: "0", // No deposit
          },
        },
      ],
    });

    console.log("Transaction:", result.transaction.hash);
    ```

  </TabItem>
  <TabItem value="hooks" label="hooks">
    To call a contract method, you can use the `callFunction` method provided by the `useNearWallet` hook:
    ```
    callFunction({ contractId: HelloNearContract, method: 'set_greeting', args: { greeting: newGreeting } })
      .then(async () => {
```
  </TabItem>
</Tabs>

---

## Calling Read-only Methods

<Tabs>
  <TabItem value="manual" label="library">

  The `near-connector` does not provide a built-in way to call read-only (view) methods.

  However, you can use the `near-api-js` package (or any of your preferred APIs) to create a JSON-RPC provider and call view methods directly:

  ```tsx
  import { JsonRpcProvider } from "near-api-js";

  const provider = new JsonRpcProvider({ url: "https://test.rpc.fastnear.com" });

  const greeting = await provider.callFunction(
    "hello.near-examples.testnet",
    "get_greeting",
    {}
  );
  ```
  </TabItem>
  <TabItem value="hooks" label="hooks">
    You can use the `viewFunction` method provided by the `useNearWallet` hook to call read-only methods on the contract:

    ```
    viewFunction({ contractId: HelloNearContract, method: 'get_greeting' }).then((greeting) => setGreeting(greeting as string));
  }, [viewFunction]);
```

  </TabItem>
</Tabs>

---

## Get Balance

<Tabs>
  <TabItem value="manual" label="library">

  The `near-connector` does not provide a built-in way to get the account balance.

  However, you can use the `near-api-js` package (or any of your preferred APIs) to create a JSON-RPC provider and query the account balance directly:

  ```tsx
  import { JsonRpcProvider } from "near-api-js";

  const provider = new JsonRpcProvider({ url: "https://test.rpc.fastnear.com" });

  const greeting = await provider.viewAccount({ accountId: "hello.near-examples.testnet" });
  ```
  </TabItem>
  <TabItem value="hooks" label="hooks">
    You can use the `getBalance` method provided by the `useNearWallet` hook to call read-only methods on the contract:

    ```jsx
    import { useNearWallet } from 'near-connect-hooks';
    import { yoctoToNear } from 'near-api-js';

    const { getBalance } = useNearWallet();
    const balance = await getBalance();
    console.log(`Balance: ${yoctoToNear(balance.available, 2)} NEAR`);
    ```

  </TabItem>
</Tabs>

---

## Send Multiple Transactions

<Tabs>
  <TabItem value="manual" label="library">

    You can request the user to sign and send multiple transactions in parallel through a single prompt:

    ```tsx
    const wallet = await connector.wallet();

    const results = await wallet.signAndSendTransactions({
      transactions: [
        {
          receiverId: "token.near",
          actions: [
            {
              type: "FunctionCall",
              params: {
                methodName: "ft_transfer",
                args: {
                  receiver_id: "alice.near",
                  amount: "1000000",
                },
                gas: "30000000000000",
                deposit: "1", // 1 yoctoNEAR for security
              },
            },
          ],
        },
        {
          receiverId: "nft.near",
          actions: [
            {
              type: "FunctionCall",
              params: {
                methodName: "nft_mint",
                args: {
                  token_id: "token-1",
                  receiver_id: "alice.near",
                },
                gas: "30000000000000",
                deposit: "10000000000000000000000", // 0.01 NEAR
              },
            },
          ],
        },
      ],
    });

    console.log(`Completed ${results.length} transactions`);
    ```
  </TabItem>
  <TabItem value="hooks" label="hooks">
    You can use the `signAndSendTransactions` method provided by the `useNearWallet` hook to send multiple transactions in a single request:

    ```tsx
    import { useNearWallet } from 'near-connect-hooks';

    ...

    const { signAndSendTransactions } = useNearWallet();

    const results = await signAndSendTransactions({
      transactions: [
        {
          receiverId: "token.near",
          actions: [
            {
              type: "FunctionCall",
              params: {
                methodName: "ft_transfer",
                args: {
                  receiver_id: "alice.near",
                  amount: "1000000",
                },
                gas: "30000000000000",
                deposit: "1", // 1 yoctoNEAR for security
              },
            },
          ],
        },
        {
          receiverId: "nft.near",
          actions: [
            {
              type: "FunctionCall",
              params: {
                methodName: "nft_mint",
                args: {
                  token_id: "token-1",
                  receiver_id: "alice.near",
                },
                gas: "30000000000000",
                deposit: "10000000000000000000000", // 0.01 NEAR
              },
            },
          ],
        },
      ],
    });
    console.log(`Completed ${results.length} transactions`);
    ```
  </TabItem>
</Tabs>

---

### Sign Messages (NEP-413)

In NEAR, users can sign messages for authentication purposes without needing to send a transaction:


<Tabs>
  <TabItem value="manual" label="library">
    You can request the user to sign a message using the wallet's `signMessage` method:

    ```tsx
    const wallet = await connector.wallet();

    const signature = await wallet.signMessage({
      message: "Please sign this message to authenticate",
      recipient: "your-app.near",
      nonce: Buffer.from(crypto.randomUUID()),
    });

    console.log("Signature:", signature.signature);
    console.log("Public Key:", signature.publicKey);

    // Verify the signature on your backend
    ```
  </TabItem>
  <TabItem value="hooks" label="hooks">
    You can use the `signMessage` method provided by the `useNearWallet` hook to request the user to sign a message:

    ```tsx
    import { useNearWallet } from 'near-connect-hooks';

    ...

    const { signNEP413Message } = useNearWallet();

    const signature = await signMessage({
      message: "Please sign this message to authenticate",
      recipient: "your-app.near",
      nonce: Buffer.from(crypto.randomUUID()),
    });

    console.log("Signature:", signature.signature);
    console.log("Public Key:", signature.publicKey);
    ```
  </TabItem>
</Tabs>