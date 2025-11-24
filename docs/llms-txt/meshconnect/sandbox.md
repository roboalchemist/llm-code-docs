# Source: https://docs.meshconnect.com/testing/sandbox.md

# Sandbox

> Learn about the Sandbox environment, its features, limitations, and how to use it for API testing.

## What is the Sandbox?

The Sandbox is a dedicated testing environment that allows you to integrate and interact with our APIs in a safe and controlled manner. It is designed to mirror the Production environment but uses **mocked data** for exchange integrations and **testnet funds** for wallet transactions, ensuring a realistic experience without risking real assets.

### Key Features of the Sandbox

* **Isolated from Production:** Prevents any interference with your live application.
* **Mocked Exchange Data:** Simulates responses from centralized exchanges for testing API calls and transfer flows.
* **On-Chain Wallet Testing:** Supports the **Sepolia testnet** for validating real on-chain transactions with self-custody wallets.
* **Dedicated API Endpoint:** Access the Sandbox API at: `https://sandbox-integration-api.meshconnect.com`.

***

## **How to Test in the Sandbox: A Step-by-Step Guide**

> **‼️ Important: For Development & Testing Only**
>
> The Sandbox environment and Sandbox API keys are designed exclusively for your development and testing phases. **Never** use the Sandbox API endpoint or Sandbox keys in your live production application. Your production application must use your Production API keys and the production endpoint.

#### **Step 1: Get Your Sandbox API Keys**

Before you begin, you must generate API keys specifically for the Sandbox.

1. Go to **Account > API keys** in your Mesh Dashboard.
2. Generate a new key in the **"Sandbox"** section. Remember to store your `Client Secret` securely.

#### **Step 2: Test a Centralized Exchange (CEX) Transfer**

This flow uses mocked data to simulate a transfer from an exchange like Coinbase or Binance.

1. ****`Generate a linkToken:`**** From your backend, make a `POST` request to the Sandbox endpoint (`https://sandbox-integration-api.meshconnect.com/api/v1/linktoken`). Include a `transferOptions` object specifying a destination address.
2. **Initialize the Link SDK:** Pass the `linkToken` to your client-side SDK to open the Link UI.
3. **Select an Exchange:** In the Link UI, choose any supported exchange. You can use any credentials (e.g., "user123"/"pass123") as the data is mocked.
4. **Complete the Transfer:** Follow the on-screen prompts to initiate and confirm the transfer.
5. **Verify the Webhook:** After completing the flow, you should receive a webhook notification with a `succeeded` status for the simulated transfer.

#### **Step 3: Test a Self-Custody Wallet Transfer (On-Chain)**

This flow uses the **Sepolia testnet** to validate a real on-chain transaction without risking actual funds.

1. **Get Sepolia ETH:** To perform a testnet transaction, you need testnet tokens. You can get free Sepolia ETH from a public faucet. A reliable option is the Google Cloud Faucet: [https://cloud.google.com/application/web3/faucet/ethereum/sepolia](https://cloud.google.com/application/web3/faucet/ethereum/sepolia). Send these funds to a test wallet that you control, such as a test MetaMask account.
2. ****`Generate a linkToken:`**** From your backend, make a `POST` request to the Sandbox endpoint. In the `transferOptions`, specify the Sepolia network and a destination address you own.
   * **Token:** Sepolia ETH
   * **Network:** Sepolia
3. **Initialize the Link SDK:** Pass the `linkToken` to your client-side SDK.
4. **Select a Supported Wallet:** In the Link UI, choose one of the supported testnet wallets, such as **MetaMask** or **Rainbow**. Connect the test wallet that holds your Sepolia ETH.
5. **Confirm the Transaction:** You will be prompted by your wallet to sign and approve the on-chain transaction.
6. **Verify the Webhook & On-Chain Transaction:** You will receive a webhook notification once the transaction is confirmed on the Sepolia network. You can also verify this by checking a Sepolia block explorer.

***

### **Limitations of the Sandbox**

* **Mocked Integrations:** All CEX integrations return simulated responses; no real transactions occur.
* **Hardcoded Prices:** Asset prices are hardcoded and do not reflect real market values.
* **Limited Wallet Support:** On-chain testing is currently limited to the Sepolia testnet and a specific set of wallets (MetaMask, Rainbow).

***

## Frequently Asked Questions

<Accordion title="🔹 Can I perform real transactions in the Sandbox?">
  No, the Sandbox does not process real transactions. All payments, asset movements, and third-party API calls return mocked responses for testing purposes.
</Accordion>

<Accordion title="🔹 Does the Sandbox have the same API as Production?">
  Yes, the Sandbox API follows the same structure and endpoints as the Production API, but the responses are simulated.
</Accordion>

<Accordion title="🔹 Are Testnets supported?">
  Currently, Sepolia network is supported for Metamask and Rainbow. Please read more about how to set them up in your sandbox in this [Guide](/guides/quickstart-testnet-sandbox).
</Accordion>

<Accordion title="🔹 Are all exchange integrations supported in the Sandbox the same as in Production?">
  No, the Sandbox API supports Coinbase, Binance, and Robinhood.
</Accordion>

<Accordion title="🔹 How can I allow users to bypass authentication when they return to use Mesh again?">
  * To enable a seamless return experience without prompting users to authenticate again, you can pass a valid `accessToken` into the `createLink()` function when connecting an account via the Mesh Web SDK.
  * If you provide a valid `accessToken`, users will not need to reauthenticate.
  * If you pass **`no integrationId and no accessToken`**, the catalog will open, but users will be required to authenticate again when selecting an already linked integration.
  * **Important:** You must securely store and manage the `accessToken` on your side. For best practices on handling authentication tokens, refer to our guide: [Handling Auth Tokens](https://docs.meshconnect.com/guides/handling-auth-tokens#handling-auth-tokens).
</Accordion>
