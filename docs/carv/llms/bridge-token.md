# Source: https://docs.carv.io/svm-ai-agentic-chain/quick-start/bridge-token.md

# Bridge Token

This page explains how to bridge the gas token, sepolia ETH to CARV's SVM testnet and bridge the token back.

## Before you start

#### SVM Wallet

You need to prepare a SVM wallet, [Backpack wallet](https://backpack.app/) is recommended.

You will need to add CARV's RPC node to the wallet. Using [Backpack wallet](https://backpack.app/) as an example:

**Step 1:** Open your Backpack wallet and click open the account menu from the **top left** corner.

![Screenshot of Backpack wallet 1](https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FtAPyFhVSQ3XkhTkDDllI%2F%E6%88%AA%E5%B1%8F2025-01-12%20%E4%B8%8B%E5%8D%8811.43.22.png?alt=media\&token=ef8740d6-9569-45ef-a1c9-f7996dbd57d8)

**Step 2:** Click Settings > Solana

![Screenshot of Backpack wallet 2](https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FwLOVzrmQiThNIMrlQWg6%2F%E6%88%AA%E5%B1%8F2025-01-12%20%E4%B8%8B%E5%8D%8811.47.18.png?alt=media\&token=2268a0e7-8285-4cb9-a285-e8a6507db6c6)

**Step 3:** Click RPC Connection > Custom

![Screenshot of Backpack wallet 3](https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FijRBLY5rkGjoXj5q5nDL%2F%E6%88%AA%E5%B1%8F2025-01-12%20%E4%B8%8B%E5%8D%8811.47.51.png?alt=media\&token=b3816b18-4187-4ed1-9074-ca6e61e359cd)

![Screenshot of Backpack wallet 4](https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FoW1uGomKZIfrF6B0Vbdt%2F%E6%88%AA%E5%B1%8F2025-01-12%20%E4%B8%8B%E5%8D%8811.48.33.png?alt=media\&token=67a64aaa-fc94-4baf-b361-e037421e9aee)

**Step 4:** Paste <https://rpc.testnet.carv.io/rpc>. Click **Update**. Your CARV SVM RPC is set up in Backpack now. You should see a "✓" next to the Custom RPC field.

![Screenshot of Backpack wallet 5](https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2Fz4dZjcBnezRkKNdWC4rQ%2FScreenshot%202025-06-30%20at%207.40.04%E2%80%AFPM.png?alt=media\&token=72680c6c-98a1-40b2-ad07-9827dac40c59)

That's it! You have successfully set Backpack to use CARV SVM RPC.

#### Sepolia ETH

You will need Sepolia ETH as the native gas token on CARV's SVM chain. There are multiple different ways you can get Sepolia ETH:<br>

* <https://faucet.soo.network/>
* <https://www.alchemy.com/faucets/ethereum-sepolia>
* <https://cloud.google.com/application/web3/faucet/ethereum/sepolia>

Once you have enough Sepolia ETH, you can proceed with the bridge.

## Token bridge

You can access the bridge page by heading to <https://bridge.testnet.carv.io/>

## Deposit

To deposit token from Sepolia ETH to CARV SVM Chain, you need to set from as Sepolia and to as SOON Ops0. Once txs are signed you will be able to have your Sepolia ETH bridged to CARV SVM Chain.

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FmhHlPvhA5Ad8SrCzKPrC%2F%E6%88%AA%E5%B1%8F2025-01-12%20%E4%B8%8B%E5%8D%8811.55.25.png?alt=media&#x26;token=7eebb8bb-701d-440a-ad2a-b58ff9d9de58" alt="" width="563"><figcaption><p>Deposit Sepolia ETH to CARV SVM Chain</p></figcaption></figure>

{% hint style="info" %}
Make sure you have rpc\_url=[ https://rpc.testnet.carv.io/rpc](https://rpc.testnet.carv.io/rpc) in your URL so you can correctly bridge the token to the CARV SVM Chain.
{% endhint %}

## Withdraw

To withdraw token, you can simply switch the token pair.

<figure><img src="https://758822945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6A1MZN6YkMg4U1B64H4g%2Fuploads%2FlZ0L0QQsveA4IyrKPjZ6%2F%E6%88%AA%E5%B1%8F2025-01-12%20%E4%B8%8B%E5%8D%8811.59.50.png?alt=media&#x26;token=a2cd8f47-c887-4b83-a76e-435d943ff046" alt="" width="563"><figcaption><p>Withdraw token</p></figcaption></figure>
