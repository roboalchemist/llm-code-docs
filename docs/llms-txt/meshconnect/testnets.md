# Source: https://docs.meshconnect.com/testing/testnets.md

# Testnets

# What It Is

Mesh now supports testnet transactions in our sandbox environment, allowing developers to validate on-chain transactions without risking real funds.

<aside>
  ℹ️

  Currently, we only support the **Sepolia testnet** and **Sepolia ETH** test tokens.
</aside>

# Why It's Important

Previously, our sandbox environment did not support wallet transactions, requiring customers to use real funds for testing. With testnets, developers can now configure transfers using Sepolia testnet and obtain test tokens from a [faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia), ensuring a risk-free and seamless integration experience.

## What Are Testnets and Test Tokens?

* **Testnets** are blockchain networks used for testing purposes, replicating mainnet functionality without real economic consequences.
* **Test Tokens** are tokens issued on testnets that simulate real assets, allowing developers to conduct transactions, test smart contracts, and validate integrations before deploying on the mainnet.

By enabling testnet support, we remove a major barrier to integration, speeding up contract signing and reducing implementation friction for prospective PSP clients.

# How to Use It

1. Reference our updated sandbox documentation: [Sandbox Documentation](https://docs.meshconnect.com/guides/sandbox)
2. Access our demo environment: [Mesh Demo Environment](https://dashboard.meshconnect.com/demos/mesh-deposit)
3. Configure a transfer using the following:
   * **Token:** Sepolia ETH

   * **Network:** Sepolia
4. **Obtaining testnet tokens:** There are two ways in which customers can obtain testnet tokens:
   **Acquire test tokens from a faucet**: Customers can obtain Sepolia ETH from a public faucet for testing. e.g. [https://cloud.google.com/application/web3/faucet/ethereum/sepolia](https://cloud.google.com/application/web3/faucet/ethereum/sepolia)

## Additional Notes

* Expanding testnet coverage is part of our future roadmap.
  * Please reach out to product with any additional testnet expansion request.
* Currently, only MetaMask and Rainbow wallets are supported
  * Please reach out to product to enable additional wallet support
* Sales and CS teams should proactively inform customers about this feature to accelerate integration timelines.
* For further assistance, customers should reach out to their assigned CS representative.

## Reference Docs

[https://docs.meshconnect.com/guides/sandbox](https://docs.meshconnect.com/guides/sandbox)
