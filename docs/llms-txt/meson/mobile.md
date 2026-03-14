# Source: https://docs.meson.fi/guides/meson/mobile.md

# Swap on Mobile

This guide illustrates Meson swap process on mobile devices. Please refer to [Meson App](https://docs.meson.fi/guides/meson) for desktop guide for Meson Swap.

## Contents

* [Sign up with MetaMask](#sign-up-with-metamask)
* [Select Origin Network & Connect to MetaMask](#select-origin-network--connect-to-metamask)
* [Initiate Meson Swap](#initiate-meson-swap)
  1. [Enter Swap information](#1-Enter-Swap-information)
  2. [Approve](#2-approve)
  3. [Sign your transaction](#3-sign-your-transaction)
     * [1st Signature](#1st-signature-request-swap)
     * [2nd Signature](#2nd-signature-release-funds-to-the-destination)
* [Check Swap Status and History](#check-swap-status-and-history)
* [Looking for Help?](#looking-for-help)

## Sign up with MetaMask

Meson App requires a valid MetaMask connection in order to perform swap transactions. If you do not have a MetaMask wallet, refer to [MetaMask Official Documentation](https://metamask.io/faqs/) to set up your MetaMask wallet before you proceed.

## Select Origin Network & Connect to MetaMask

After entering the app, click on the top to see the networks that have been added.

![Select Origin Network in MetaMask](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-de666a6411024471e01ede1872f9a0f81eabf711%2Fm-1.png?alt=media)

Click the menu bar in the upper left corner of the interface, go to Settings, and select the Network option to add an RPC network.

![Add custom networks to MetaMask](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-ba5b9b66c89fdf9e52f1ff181c650361e0441a34%2Fm-2.png?alt=media)

Go to your browser in the menu bar, enter the URL: <https://meson.fi/> to open Meson, and click "CONNECT WALLET" in the upper right corner to connect MetaMask to Meson.

![Add custom networks to MetaMask](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-cac7c4caee2a3baf138d86082fc034a182082e8d%2Fm-3.png?alt=media)

{% hint style="info" %}
**Good to know:** Meson App currently supports these high performance EVM chains:

* Ethereum
* BNB Chain (formerly BSC)
* Polygon
* Evmos Mainnet
* Arbitrum
* Optimism
* Aurora (on NEAR)
* Conflux eSpace
* Avalanche C-chain
* Fantom
* Tron
* Harmony
* Moonriver
* Moonbeam
  {% endhint %}

{% hint style="info" %}
Refer to below tutorials to add custom networks in MetaMask.

* [BNB Chain (formerly BSC)](https://academy.binance.com/en/articles/connecting-metamask-to-binance-smart-chain)
* [Polygon](https://docs.polygon.technology/docs/develop/metamask/config-polygon-on-metamask/)
* [Evmos Mainnet](https://docs.evmos.org/users/wallets/metamask.html)
* [Arbitrum](https://developer.offchainlabs.com/docs/developer_quickstart#use-the-dapp)
* [Optimism](https://help.uniswap.org/en/articles/5404230-how-to-connect-to-optimistic-ethereum)
* [Aurora](https://doc.aurora.dev/interact/metamask/)
* [Conflux eSpace](https://developer.confluxnetwork.org/guides/en/user_metamask_interact_evmspace/)
* [Avalanche C-chain](https://support.avax.network/en/articles/4626956-how-do-i-set-up-metamask-on-avalanche)
* [Fantom](https://docs.fantom.foundation/tutorials/set-up-metamask)
* [Harmony](https://docs.harmony.one/home/general/wallets/browser-extensions-wallets/metamask-wallet/adding-harmony)
* [Moonriver](https://docs.moonbeam.network/builders/get-started/networks/moonriver/)
* [Moonbeam](https://docs.moonbeam.network/tokens/connect/metamask/)
  {% endhint %}

### Initiate Meson Swap

#### 1. Enter Swap information

* Select the initial (FROM) network and target (TO) network of stablecoin Swap;
* Select the stablecoin type that you want to Swap;
* Enter the amount of Swap (the exchange on Meson will always remain 1:1);
* Enter the wallet address that accepts Swap. By default, the wallet address is the same as the FROM address;

After information input and confirmation, click Swap to initiate the swap.

![Select Destination Network in Meson](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-1160f4261941c5a7193df2e9b4715a40f6cbd511%2Fm-4.png?alt=media)

#### 2. Approve

If you are swapping for the first time, you need to perform the **Approve** operation to grant the Meson smart contract access to the stablecoins in your wallet. Click the **Approve** button and sign with MetaMask to complete this step.

#### 3. Sign your transaction

Meson utilizes meta transactions so that it is the Liquidity Providers but not users who pays gas fees. That’s why you will see *sign* transactions instead of *send* transactions. You will be asked for **two signatures** during the swap process.

**1st Signature** Request Swap

After confirming the transaction information, click the button to complete the signature through the MetaMask pop-up window. The first signing represents publishing a Swap request to the Meson network.

The Meson network will have LP to match Swap requests posted by users. In this process, LP will use the user’s signature, invoke the Meson contract for the user, and transfer the corresponding amount of stablecoin into the Meson contract for locking. At the same time, LP will be locked in Swap’s target chain for a specified number of stablecoin.

This process usually lasts 1-2 minutes.

![Request Swap](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-137377f0d0a1a44b2b9e81c9859d62828fb7db1c%2Fm-5.png?alt=media)

**2nd Signature** Release funds to the destination

After the primary chain and target chain have locked the Swap amount, the Meson page will pop up a second signing window via MetaMask. The second signature can synchronously unlock the funds of the two chains, which means that the user transfers the exchange amount to LP in the initial chain and gets the exchange funds in the target chain. This process usually takes 30 seconds to a minute.

![Release Funds](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-92f1717ce3d8f9f205de8a3baeb78780a18aeaa1%2Fm-6.png?alt=media)

After the Swap is successful, users will find that the number of stable coins in the two wallets involved in the Swap changes, indicating that the Swap is successfully completed.

![Swap Success](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-a97727175023ba88c72230b42600fd44e230c6d8%2Fm-7.png?alt=media)

### Check Swap Status and History

Click the wallet button in the upper right corner, and you can see the current Swap and the historical Swap records on the popup window. If Swap needs to do something (such as signing a second time to release funds), it can do so through this page.

Users can also view swap status and history in [Meson Explorer](https://explorer.meson.fi/). Click [here](https://docs.meson.fi/guides/explorer) to learn more.

![Check Swap History](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-62e0b56f8c5f2e2e8c00c279b8950b92d187b52c%2Fm-8.png?alt=media)

### Looking for Help?

Having trouble with your transactions and looking for Meson support? Please click the question mark in the right lower corner, and contact us in discord #get-assists channel. We are more than happy to offer a one-on-one support to you.

![Check Swap History](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-3a7177ebcbbe5e62e4bfbb7e606ba1a076416a23%2Fm-9.png?alt=media)
