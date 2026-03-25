# Source: https://docs.meson.fi/protocol/meson.md

# Source: https://docs.meson.fi/guides/meson.md

# Meson App

This guide illustrates Meson swap process on desktop devices. Please refer to [Swap on Mobile](https://docs.meson.fi/guides/meson/mobile) for mobile guide for Meson Swap.

## Contents

* [Prepare Your Wallet](#Prepare-Your-Wallet)
* [Swap on Meson App](#Swap-on-Meson-App)
  1. [Select origin network](#1-select-origin-network)
  2. [Connect wallet](#2-connect-wallet)
     * [Approve Meson App to add network to your wallet](#approve-meson-app-to-add-network-to-your-wallet)
     * [Don’t see your token in MetaMask?](#don’t-see-your-token-in-metaMask?)
  3. [Enter swap information](#3-enter-swap-information)
  4. [Approve your wallet](#4-approve-your-wallet)
  5. [Sign your transaction](#5-sign-your-transaction)
     * [1st signature](#1st-signature)
     * [2nd signature](#2nd-signature)
* [Check Swap Status and History](#Check-Swap-Status-and-History)
* [RPC Node](#RPC-Node)
* [URL Parameters](#URL-Parameters)
* [Looking for help?](#Looking-for-help?)

## Prepare Your Wallet

Meson App requires a valid wallet connection in order to perform swap transaction. If you do not have a wallet, refer to the following links to set up your wallet before you proceed.

* [MetaMask Official Documentation](https://metamask.io/faqs/)
* [TronLink Official Documentation](https://tronlinkorg.zendesk.com/hc/en-us)

## Swap on Meson App

### 1. Select origin network

Access Meson App at [meson.fi](https://meson.fi/), click the network dropdown menu and select origin FROM network. According to the origin network you select, Meson App will automatically match the rightful wallet for you to connect and proceed.

![Meson App](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-7406e9ec1831f62b7fc9290bd8a205c3f5f9f057%2F1.png?alt=media)

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

### 2. Connect wallet

Click **CONNECT WALLET** in the upper right corner to establish a connection to your wallet. If you select Tron as FROM network, you will need to connect to TronLink to proceed; For all other networks, connect to MetaMask to proceed.

![Connect wallet](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-be2d85280a90d823668d6bb96169936bd719cae2%2F2.png?alt=media)

{% hint style="info" %}
**Good to know:** If you’re swapping from Tron to other networks or the other way around, you’ll need to manually key in the destination wallet address.
{% endhint %}

#### Approve Meson App to add network to your wallet

In order to proceed, Meson App requires to add origin network in your wallet. By clicking APPROVE in MetaMask, the network will be added to your wallet automatically.

![Connect wallet](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-c45282dbb389fdf0e21ffba7bb88f8f9c9562c35%2F3.png?alt=media)

You may need to manually add the respective network to your MetaMask wallet if you don’t see the network added to your wallet right away.

![Connect wallet](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-89b57d895ceb6dcf27add1f26e5942d6052364fd%2F4.png?alt=media)

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

#### Don’t see your token in MetaMask?

Once you selected corresponding network in MetaMask, Meson App will show the token balance on the screen. You may also check the balance in your MetaMask. If you’re not able to see the token, you may need to add custom token to your MetaMask first in order to view the balance. Please refer to MetaMask official documentation here How to add custom token in MetaMask to add custom tokens to your wallet.

{% hint style="info" %}
**Good to know:** You will be asked token contract address when adding tokens to MetaMask. Tokens are minted by a specific smart contract on each chain, therefore address of the contract is unique for any specified token on a chain. To figure out the correct contract address, only refers to the official explorer on each chain.

[Etherscan](https://etherscan.io)

[BSCScan](https://bscscan.com/)

[Polygonscan](https://polygonscan.com/)

[Evmos](https://evm.evmos.org/)

[Arbitrum](https://arbiscan.io/)

[Optimism](https://optimistic.etherscan.io/)

[Aurora](https://aurorascan.dev/)

[Conflux Scan](https://confluxscan.io)

[Avalanche C-Chain (Snowtrace)](https://snowtrace.io/)

[Fantom](https://ftmscan.com/)

[FTMscan](https://ftmscan.com/)

[Tron](https://tronscan.org/#/)

[Harmony](https://explorer.harmony.one/)

[Moonriver](https://moonriver.moonscan.io/)

[Moonbeam](https://moonscan.io/)
{% endhint %}

### 3. Enter Swap Information

1. Select the origin **FROM** network of Cross-chain Swap;
2. Select the token type that you want to Swap;
3. Enter the amount of Swap (the exchange on Meson will always remain 1:1);
4. Select the destination **TO** network of Cross-chain Swap;
5. Enter the wallet address that accepts Swap. By default, the wallet address is the same as the FROM address;

After information input and confirmation, click Swap to initiate the swap.

![Information input and confirmation](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-e0879461c6b6cbc26fae5d9ba0392c5009f9a39d%2F5.png?alt=media)

### 4. Approve your wallet

If you are swapping for the first time, you need to perform the Approve operation to grant the Meson smart contract access to the stablecoins in your wallet. Click the Approve button and sign with your wallet to complete this step.

![Approve your wallet](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-4c2289b1a69b7b05450eeda5e6873c1db8b6056c%2F6.jpeg?alt=media)

{% hint style="info" %}
**Gas fee for `Approve` transaction**

Meson utlizes meta-transaction mechanism in our project development. As a result, Meson bears the gas fee incurred on both origin and destination networks instead of the user during every swap.

However user are still required to pay for gas fee for `approve` transactions. `Approve` is required for wallet that is connected to Meson to swap for first time, allowing Meson's smart contract to access the funds in user's wallet in order to process swaps. This is a common practice for DeFi projects on the market as well. User will need to have sufficient native token to pay for the gas consumed on the origin network for the `approve` transaction, whose amount is subject to the origin network and its network conditions. Meson has no control on the gas fee levied on a particular network.
{% endhint %}

### 5. Sign your transaction

Meson utilize meta transactions so that it is the Liquidity Providers but not users who pays gas fees. That’s why you will see sign transaction instead of send transactions. You will be asked for two signatures during the swap process.

#### 1st Signature: Request Swap

After confirming the transaction information, click the button to complete the signature through the wallet pop-up window. The first signing represents publishing a Swap request to the Meson network.

The Meson network will have LP to match Swap requests posted by users. In this process, LP will use the user’s signature, invoke the Meson contract for the user, and transfer the corresponding amount of stablecoin into the Meson contract for locking. At the same time, LP will be locked in Swap’s target chain for a specified number of stablecoin.

This process usually lasts 1-2 minutes.

![1st Signature](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-7a651f58495e7b2ce991238e255d8b3cbd431637%2F7.png?alt=media)

#### 2nd Signature: Release funds to destination

After the primary chain and target chain have locked the Swap amount, the Meson page will pop up a second signing window via your wallet. The second signature can synchronously unlock the funds of the two chains, which means that the user transfers the exchange amount to LP in the initial chain and gets the exchange funds in the target chain. This process usually takes 30 seconds to a minute.

![2nd Signature](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-22be081a6e904af5909209e4f182285b709151bb%2F8.png?alt=media)

After the Swap is successful, users will find that the number of stable coins in the two wallets involved in the Swap changes, indicating that the Swap is successfully completed.

![Swap successfuly Toast](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-48221f67956f3d408772d6bb8b5de30de69d460b%2F9.png?alt=media)

## Check Swap Status and History

Click the wallet button in the upper right corner, and you can see the current Swap and the historical Swap records in the popup page. If Swap needs to do something (such as signing a second time to release funds), it can do so through this page.

![Wallet Page](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-dd7c4786d7165c08fc7ee9a8b4b1c2b69db61932%2F10.png?alt=media)

Users can also view swap status and history in [Meson Explorer](https://explorer.meson.fi). Click [here](https://docs.meson.fi/guides/explorer) to learn more.

![Meson Explorer](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-043aab58bdb9089086c595034acd3e0c51ec87f5%2F11.png?alt=media)

## RPC Node

All dApps (decentralized applications) need a way to communicate with blockchains. The RPC Node status bar in the lower left corner of the Meson home page shows the connection status of the RPC Node between Meson and the target blockchain. The number after the dot represents the block number of the target blockchain. Green indicates that the connection is normal, and yellow indicates that the connection is faulty.

![RPC Node](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-74b4f42fd04e3e3e7b7f4dd140108aae5c954dde%2Frpcnode.png?alt=media)

## URL Parameters

Meson app supports URL paramerters which allows user to directly land on the desired network pair when accessing Meson app. To access Meson using URL parameters, append respective parameter(s) as follows:

**<https://meson.fi?from={origin\\_blockchain\\_name}\\&to={target\\_blockchain\\_name}>**

where *origin\_blockchain\_name* refers to the blockchain name of the origin network, *target\_blockchain\_name* refers to name of the target network. Please refer to [Meson Developers Doc](https://meson.dev/getting-started/supported) for the most accurate and updated set of blockchain names supported by Meson.

## Looking for Help？

Having trouble with your transactions and looking for Meson support? Please click the question mark in the right lower corner, and contact us in discord #get-assists channel. We are more than happy to offer a one-on-one support to you.

![Help Support](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-1b95f286c49c0a18eabcda4c9490fcf5d9f8f35d%2F12.jpeg?alt=media)
