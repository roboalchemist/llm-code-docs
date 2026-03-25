# Meson Documentation

Source: https://docs.meson.fi/llms-full.txt

---

# Meson Docs

Welcome to the official documentation site for Meson Protocol which aims to provide minutes-fast swaps with almost-zero fee & slippage across all major blockchains.

## Meson is now LIVE!

Welcome to Meson! Meson is the faster and safer way to execute low-cost, zero-slippage universal cross-chain swaps across all leading blockchains and layer-2 rollups.

Meson has launched on 16 high-performance chains including Ethereum, BNB Chain, Tron, Avalanche, Polygon, Fantom, Aurora (NEAR), Cronos (Cosmos), Conflux eSpace, Moonbeam (Polkadot), Moonriver (Kusama), Aptos and EOS as well as Layer-2 rollups such as Arbitrum, Optimism and zkSync. Meson will continue to work on network expansion for the rest of 2023 with plan to roll out on more L2 rollups and non-EVM chains like Sui, Algorand and Solana.

In the meantime, Meson closely monitors the token market as it evolves and plans to introduce more widely-adopted stablecoins, such as DAI, etc. as well as tokens such as BTC/wBTC, to meet the growing demand on the market.

Thanks to the all-new product design and technology stacks, Meson achieves fast swap finality by out-of-order processing the swap from the origin to destination chains, where HTLC guarantees eventual execution of the swap. This innovative operating model also frees Meson from existing cross-chain bridges and significantly reduce our cost, offering lowest fee on the market. Meson protocol can be connected to any public chain that runs smart contracts.

Liquidity Providers are welcomed to join Meson to enjoy best available yields with industry-leading security commitments.

Meson protocol has been repeatedly audited by SSLabs at Georgia Institute of Technology and is currently going through robust code review by Trail of Bits. Further internal and external security reviews will be conducted by Meson Team and renowned auditors regularly to ensure compliance with highest level of security standards.

## Guides: Jump right in

Follow our handy guides to get started on the basics as quickly as possible:

{% content-ref url="guides/meson" %}
[meson](https://docs.meson.fi/guides/meson)
{% endcontent-ref %}

{% content-ref url="guides/explorer" %}
[explorer](https://docs.meson.fi/guides/explorer)
{% endcontent-ref %}

## Technical Materials: Dive a little deeper

Learn the fundamentals of Meson to get a deeper understanding of our main features:

{% content-ref url="protocol/background" %}
[background](https://docs.meson.fi/protocol/background)
{% endcontent-ref %}

{% content-ref url="protocol/background/htlc" %}
[htlc](https://docs.meson.fi/protocol/background/htlc)
{% endcontent-ref %}

{% content-ref url="protocol/meson" %}
[meson](https://docs.meson.fi/protocol/meson)
{% endcontent-ref %}

{% content-ref url="protocol/system-design" %}
[system-design](https://docs.meson.fi/protocol/system-design)
{% endcontent-ref %}

## Official Links

Find us on your favorite social platforms for latest Meson news and talk to real Meson people!

* **Twitter** <https://twitter.com/mesonfi>
* **Discord** [https://discord.gg/mesonfi](https://discord.gg/mesonfi/)
* **Telegram** <https://t.me/mesonfi>
* **Medium** <https://medium.com/@mesonfi>


# Introducing Meson

### Why Called Meson?

[Meson](https://en.wikipedia.org/wiki/Meson) is the name of a class of particles in quantum mechanics. For a long time, physicists didn't understand why protons and neutrons could come together to form atomic nuclei, and therefore failed to explain where more than one hundred of atoms came from.

In the 1930s, physicist [Hideki Yukawa](https://en.wikipedia.org/wiki/Hideki_Yukawa) proposed the meson theory for which he won the Nobel Prize in Physics. The word meson comes from Greek which means "middle". In Hideki's theory, mesons transmit the attractive interaction between protons and neutrons, acting as a bridge between them. It is because of the existence of mesons that a few types of elementary particles can be combined to produce countless possibilities, thus forming the colorful world we see.

We named our protocol *Meson* with the hope that we can act as the connection of different blockchains. Like meson particles, we believe connections will enrich possibilities and incubate a thriving application ecology.

### Meson‘s Philosophy?

Meson's philosophy is to provide a safe and convenient cross-chain product for ordinary users.

We believe that with the multi-blockchain ecological development in the past year or so, cross-chain has evolved from a technical implementation problem to a user experience problem. The Meson protocol is built on the existing technical solutions of cross-chain bridges, and the goal of Meson is to allow users to enjoy a more convenient, faster, lower-cost, and more secure cross-chain swaps. Meson will focus on stablecoins and selected tokens, so a lot of optimization can be performed to maximize the user's experience.

### Why Choosing Meson?

The existing cross-chain bridges solve the problem of cross-chain circulation of digital assets. Meson builds on their technical foundation to help users improve their experience. In fact, when individual users are using Meson, the LPs that provide users with swap services may be using the existing bridges protocol. This is like when you are calling a taxi using Uber, you don't need to understand TCP/IP protocol, but these underlying protocols are running behind the applications which ensure you can quickly get a ride.

* **Faster speed:** A swap on Meson is usually completed in 1-2 minutes.
* **Lower cost:** Meson has applied a lot of optimization from protocol design to contract implementation in order to minimize the cost for users. Meson also innovatively applied *meta transactions* which allow that users do not even need to pay gas fees, and transactions can be completed without native tokens. Meta transactions enable LPs to pay gas fees for users, but by moving the gas fee to the LP, we can also use more means for gas optimization, thus reducing the overall transaction cost.
* **Direct exchange:** Meson uses the most widely accepted tokens on each chain directly, and can directly perform cross-chain exchanges between token of same value like USDT ↔ USDC. There is also no need to temporarily hold any wrapped stable coins in an intermediate state during the transaction. No matter which chain you are on, you can directly get the most mainstream stablecoins and selected tokens through Meson.
* **Funds are more secure:** While Meson runs on top of cross-chain bridges, it's not a strong dependency. This means that funds do not need to be locked in the pools of bridges, and the core assets will have a higher utilization under the premise of absolute security. The safety hazards or instability of the bridge itself will not affect the operation of Meson. In addition, Meson uses the technology of [Atomic Swap](https://docs.meson.fi/protocol/background/htlc) which means that assets do not have to pass through the hands of a third party and will not be stuck in the contract. Although there will be multiple intermediate states in a transaction, the assets of both parties will only exist in their own hands or pay to the other party.


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


# Premium

| Type                                   | Early Supporter Discount                                       | Premium Lite          | Premium               | Premium Plus          | Extra Pack             | LP Privilege                                                                                                                                                                           |
| -------------------------------------- | -------------------------------------------------------------- | --------------------- | --------------------- | --------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Price                                  | Free                                                           | -                     | $6.99 USDT/USDC/BUSD  | $26.99 USDT/USDC/BUSD | $6.99 USDT/USDC/BUSD   | Liquidity Provider with > 5000 USDT/USDC/BUSD staked, same validity period as Premium, will expire in 3 days if staked < 5000, requalify if staked > 5000 and with allowance refreshed |
| Subscription                           | -                                                              | -                     | Yes                   | Yes                   | -                      | -                                                                                                                                                                                      |
| Validity period                        | Same day                                                       | 7 days                | 30 days               | 30 days               | same as user's Premium | -                                                                                                                                                                                      |
| Service Fee waived for                 | first $3,000 or 3 swaps / day (whichever occurs first applies) | $21,000               | $100,000              | $500,000              | $100,000               | -                                                                                                                                                                                      |
| Maximum amount allowed per swap        | 5,000 USDC/USDT/BUSD                                           | 10,000 USDT/USDT/BUSD | 10,000 USDT/USDT/BUSD | -                     | -                      |                                                                                                                                                                                        |
| Service Fee thereafter                 | 0.05% (min $0.5)                                               | 0.05% (min $0.5)      | 0.05% (min $0.5)      | 0.05% (min $0.5)      | -                      | -                                                                                                                                                                                      |
| Claim Premium Role                     | -                                                              | Yes                   | Yes                   | Yes                   | -                      | -                                                                                                                                                                                      |
| Hide My Transactions                   | -                                                              | Yes                   | Yes                   | Yes                   | -                      | -                                                                                                                                                                                      |
| Get Extra Pack                         | -                                                              | -                     | Yes                   | Yes                   | -                      | -                                                                                                                                                                                      |
| Bind EVM/non-EVM Addresses             | -                                                              | Yes                   | Yes                   | Yes                   | -                      | -                                                                                                                                                                                      |
| Customized Profile Picture             | -                                                              | Yes                   | Yes                   | Yes                   | -                      | -                                                                                                                                                                                      |
| View Liquidity Dashboard (coming soon) | -                                                              | Yes                   | Yes                   | Yes                   | -                      | -                                                                                                                                                                                      |
| VIP Services (coming soon)             | -                                                              | -                     | -                     | Yes                   | -                      | -                                                                                                                                                                                      |
| Loyalty Points (coming soon)           | -                                                              | Yes                   | Yes                   | Yes                   | -                      | -                                                                                                                                                                                      |
| New Blockchain Trial (coming soon)     | -                                                              | -                     | Yes                   | Yes                   | Yes                    | -                                                                                                                                                                                      |
| Annual Subscription(coming soon)       | -                                                              | -                     | TBD                   | TBD                   | -                      | -                                                                                                                                                                                      |

LP Fees, including USDT <> USDC conversion fee and Ethereum gas fee, are not covered by the Meson Premium fee waiver.

### Extra pack

Premium Mesoners are eligible to purchase extra pack to increase Service Fee waiver allowance by`N * 100,000` ,where `N` is the number of Extra Pack you purchased. For example, if you are currently enrolled in Premium membership and purchase `N` extra packs within same membership period, you will be waived Service Fee for a total of `100,000 + N * 100,000` accumulatively. Please refer to the above table for details of Extra Pack.

### Hide my transactions

Preimum Mesoners are eligible to opt in to hide transactions on [Meson Explorer](https://explorer.meson.fi). When opt-in, all transaction history associated with the Premium Mesoners' address will be hidden from [Meson Explorer](https://explorer.meson.fi).

Please note, hidden transaction history remain visible to the Premium Mesoner on [Meson App](https://meson.fi) by clicking the `wallet` button on the top-right corner. Please be cautious when sharing the explorer link starting with `https://explorer.meson.fi/swap/0xAAAA...` to others, as anyone may access the swap details with the explorer link.

### How to purchase, renew Meson Premium, buy extra pack or opt in to hide transctions for existing Meson Premium?

* How to become a Premium Mesoner?

Step 1 Please go <https://meson.fi/> and connect your wallet.

Step 2 Please click the wallet button at the upper right corner, you will see the premium service,and Click the `BUY` button.

Step 4 Make a payment and then your Meson Premium will be activated.

* How to renew Meson Premium?

Step 1 Please go <https://meson.fi/> and connect your wallet.

Step 2 Please click the wallet button at the upper right corner, you will see the premium service, and then click the `DETAILS` button.

Step 3 Click the `RENEW` button.

Step 4 Make a payment and then your Meson Premium will be renewed.

* How to purchase Extra Pack?

Step 1 Please go <https://meson.fi/> and connect your wallet

Step 2 Please click the wallet button at the upper right corner, you will see the premium service, and then click the `DETAILS` button.

Step 3 Click the `+` button next to `Free swaps used` column.

Step 4 Make a payment and your extra pack will be applied on the membership.

* How to hide my transactions?

Step 1 Please go <https://meson.fi/> and connect your wallet

Step 2 Please click the wallet button at the upper right corner, you will see the premium service, and then click the `DETAILS` button.

Step 3 Find the `Hide my transactions on Meson Explorer` option, tick the box to enroll.

Step 4 All transtion history associated with the address will now be hidden from Meson Explorer.

### Terms & Conditions

* Meson Premium is not transferrable and only valid for use by the wallet address that purchased the premium membership.
* Meson Premium is not automatically renewable. We will send you an expiry alert to you seven days before your Premium expiry date.
* Meson Premium is a non-refundable membership plan and is valid for a consecutive 30 days upon purchase. All extra packs purchased within the membership validity period expire when membership ends.
* Premium renewed before the expiry date will lead to immediate invalidation of current membership, where all benefits including remaining free swap quota, and membership period will be discarded.
* You must be a Premium Mesoner with active membership at the time of puchasing Extra Pack. Purchasing extra pack does not extend or renew your premium membership.

### Need Assistance?

If you have questions, please join [Meson Discord](https://discord.gg/mesonfi) to get one-on-one help.


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


# Meson Explorer

## Access Meson Explorer

Meson Explorer is a useful tool to track swap transactions submitted to Meson App. You may access Meson Explorer at <https://explorer.meson.fi>. Meson Explorer displays all swap transactions submitted to Meson App, inlcuding *swap id*, *status*, *swap origin*, *swap destination*, *swap amount* and *duration*.

![explorer.png](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-7c96d7003f47f0a4c6bafc74dc51a37cabadb509%2Fmeson_explorer.png?alt=media)

## Check Swap Details

Click on swap id to check swap detail in the popup window.

![swap\_details.png](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-437f08656546e0bcd8043fb881bf1e79dc509c46%2Fswap_details.png?alt=media)

Swap Details gives all corresponding information to the swap transactions, including associated contract or transaction id for each step in the process. Users may also click to view the transaction details in respective official chain block explorer.


# Background

Multi-chain coexistence is the current and future market landscape of the blockchain world. The transfer of assets between different chains makes cross-chain protocols a rigid requirement for users on blockchains. At present, there are two main ways to achieve cross-chain transactions. The first is cross-chain liquidity aggregators that combine assets on different chains into a swapping pool. Users can exchange their assets from different chains with the pool. The second is cross-chain bridges which provide a channel between two blockchains. Native assets are hosted and staked in the original chain, and the other chain can obtain the asset status through cross-chain nodes. Therefore, a mapped version of the asset can be minted by 1:1 ratio on the target chain.

Among all digital assets, stablecoins are the most important type. In 2021, the supply of USD-based stablecoins increased from $29 billion at the beginning of the year to more than $140 billion, an increase of more than 300%. While the application layer is growing rapidly, stablecoins benefit from their characteristics and act as multiple roles including transaction payment intermediaries, trading settlement units, market hedging tools, etc., and naturally grow rapidly with the expansion of the cryptocurrencies market. According to the definition of stablescoins, an ideal stablecoin should maintain a 1:1 exchange rate with fiat USD currency. Since different types of stablecoins are distributed on different chains, the conversion rates between them, including in-chain and cross-chain swaps, should also maintain at 1:1.

With the advantages of simpler product form, wider ecological coverage, and more flexible connection, cross-chain bridges and protocols have surpassed centralized services and become the main channel for carrying cross-chain asset flows. Cross-chain bridges can be divided into two types: trusted and trustless. However, these two types of bridges both have certain problems in realizing the cross-chain swap for stablecoins. Trusted bridges require additional trusted third parties and are not suitable as the basis for products with a large number of users and volumes. An ideal trustless bridge would better satisfy the trust requirements, but due to its decentralization needs, it would take extra time (usually more than 1 hour) and incur extra costs (tens of dollars) in order to establish consensus. For stablecoins that are expected to remain 1:1 conversion rate, users are generally unwilling to pay this conversion cost. In addition, the connection method of cross-chain bridges is one-to-one, which makes a fully connected network using bridges between multiple chains a complicated and laborious issue.


# Hash Time Lock Contract (HTLC)

The demand for cross-chain asset exchange has already been discussed in depth in the early days of blockchain development. In 2013, the HTLC process was proposed ([ref](https://bitcointalk.org/index.php?topic=193281.msg2058662#msg2058662)) to implement *atomic swap* in order to accomplish trustless exchange between Bitcoin and Litecoin. The process of atomic swap works as follows.

1. Alice and Bob confirm their willingness to transact offchain in advance. For example, Alice wants to exchange 1 BTC for Bob's 100 LTC.
2. Alice chooses a random number `r` and calculates its hash `H`. Then, Alice posts a transaction on the Bitcoin network using `H` to lock 1 BTC with unlocking conditions to be either a) 1 BTC will be transferred to Bob with the given `r` (satisfying the condition `Hash(r) = H`, or b) 1 BTC will be returned to Alice after a certain wait time (e.g. 6 hours). Note that, Alice only discloses `H` but not `r` in this step.
3. Once Bob confirms Alice's transaction, He should use `H` to publish a transaction to lock 100 LTC on the Litecoin network. The unlock conditions are either a) 100 LTC will be transferred to Alice with the given `r` satisfying the condition `Hash(r) = H`, or b) 100 LTC will be returned to Bob after a certain wait period (need to be less than Alice's time, such as 3 hours).
4. Alice sees Bob's transaction, confirms the authenticity of the transaction, then uses the `r` to unlock Bob's transaction on the Litecoin network. As a result, Alice receives Bob's 100 LTC. This step will also disclose `r` to the network.
5. When Bob sees `r`, he can proceed to unlock Alice's transaction on the Bitcoin network and receives 1 BTC from Alice as a result of the transaction.

The key point of this process is that a ciphertext `r` can unlock a transaction on two separate unrelated blockchains, controlling both transactions to be either completed or dismissed at the same time. This is why this process is also known as *atomic swaps*.

HTLC was proposed long before cross-chain facilities such as cross-chain bridges and oracles were designed and implemented. As can be seen, this process does not involve additional decentralization establishment or consensus formation mechanisms and therefore is much faster and cheaper.

However, atomic swaps based on HLTC also has certain problems, such as

* **Order matching problem:** Transactions need to be matched on a one-to-one. It takes time for the initiator of a transaction to find a user willing to match his amount and price, thus making the process less efficient.
* **Free option problem:** In the above example, Alice can observe the price movement of BTC/LTC within 3 hours and execute the transaction only if the price is in her favor. Otherwise, she could just leave the order and wait for expiry. This is equivalent to Alice getting a free LTC call option, which hurts Bob‘s interests.

The second problem is not significant in stablecoin and ETH-wETH tradings because the margin of their exchanges are usually very small. We improved the order matching problem in Meson by designing a set of off-chain services. See [system design](https://docs.meson.fi/protocol/system-design) for more details. Therefore, Meson can benefit from HTLC’s fast speed and low cost, and take the user experience to a higher level.


# The Meson Protocol

In order to enable fast and low-cost circulation of tokens between any public chains, we propose the Meson protocol, which differs from the HTLC-based atomic swap in the following ways.

* We recommend the party that matches a swap lock their token assets in a liquidity pool in advance, as demonstrating the willingness to transact. Therefore, the initiator of a swap (usually the user) can be matched quickly. We refer to the matching party as the *Liquidity Provider (LP)*;
* Waive blockchain network fees (gas fee) for users by using the technique of *meta transactions*;
* Using signatures as the credential to unlock transactions, thus avoiding the security risks from unsafe random number generators and hash collisions.

There are three major stages in a swap on Meson.

* **Preparation stage**: In the preparation stage, LPs can deposit tokens they are willing to provide for cross-chain swap into the liquidity pool in the Meson contract in advance to ensure liquidity during a swap.
* **Swap stage**: A user who wants to do cross-chain token swap can complete the process with an LP without the need of using bridges. Therefore, this process would be fast and inexpensive.
* **Rebalance stage**: After the LP has accumulated a certain amount of swaps, he can go through the rebalance stage if he wants to adjust his fund pool sizes on different chains. In this stage, other long-term cross-chain methods (bridges, exchanges, etc) can be used to perform the actual cross-chain transfer of assets. However, this process is not time-sensitive, and because LPs can accumulate many swaps and perform a single cross-chain operation in a unified manner, it also saves cross-chain fees.

Users’ swap requests can be better matched with our improved HTLC scheme. Similar to atomic swap, both parties swap their assets on two chains in Meson's process. For the user, it is equivalent to getting tokens directly at the destination chain with fast confirmation and no cross-chain facility fees.

For LPs, using the Meson protocol also provides better capital utilization efficiency - LPs can choose to provide one pool of funds for one-way swap, two pools for swaps between two tokens, or `n` pools for swaps between `n` tokens. The last scenario requires `n(n-1)/2` transaction pairs if implemented by one-to-one cross-chain bridges, which means `n(n-1)` pools are involved.

[Meson smart contracts](https://docs.meson.fi/implementation/smart-contracts) are implementations of the Meson protocol and can be written in any language, including Solidity, Rust, C++, etc. This means that the Meson protocol not only supports various EVM-compatible public chains but also non-EVM public chains and layer-2 networks. When supporting a new public chain, implementation and deployment of the Meson smart contract on that chain will automatically enable token swaps between the new chain and all previous chains. As the number of public chains grows, the workload of Meson to support multiple chains grows linearly, compared to the quadratic difficulty growth of connecting multiple chains with cross-chain bridges.

To summarize, the Meson protocol for cross-chain swaps has several advantages.

* **Connectivity**: Cross-chain swaps can be done on any two chains without the need for a direct cross-chain bridge connection between the two;
* **Compatibility**: The two chains involved in a swap can be any public chain that can execute smart contracts and does not require EVM compatibility;
* **Cost**: During the swap process, the user does not need to pay the gas fee for the blockchain network; this fee are paid by LP;
* **Time**: The swap is completed only by waiting for the confirmation of the contracts on chains X and Y. There is no need to wait for cross-chain bridge confirmation. If the confirmation time for both X and Y chains is short, cross-chain swaps can be done quickly;
* **Security**: Meson does not rely on cross-chain services such as cross-chain bridges and oracles during the swap stage, so it is not affected by security issues of third-party services.


# Swap Process

On each chain, in order to ensure the convenience of users, Meson will directly use the widely accepted tokens on the chain. For each Meson-backed token on each chain, the Meson smart contract will provide a liquidity pool to provide swap services for that token.

### Preparation Stage

LPs who want to provide swap services can call the [`deposit`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Pools/MesonPools.sol#L22) method of Meson and inject tokens that are willing to participate in the cross-chain swap into the Meson contract.

### Swap Stage

1. **Swap request:** The user (U) constructs a swap request off-chain which specifies the swap amount, the initial chain (X), the target chain (Y) and token type, as well as other necessary information. To publish the swap request, the user needs to sign it which authorizes the Meson contract to lock the swap amount + swap fee for matching LP. The signed swap will be broadcasted to the LP network through [Meson relayer](https://docs.meson.fi/protocol/system-design/relayer) and wait for an LP to match. Since this process does not require actual on-chain transactions, users do not need to pay any gas fees (for ERC20 tokens, users need to `approve` in advance and gas fees still need to be paid for this step). The signature for a swap request will be checked by Meson's smart contract ([source](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/utils/MesonHelpers.sol#L145)) for the next step to proceed.
2. **Post and bond a swap:** LP needs to validate the swap request after receiving it. For a valid swap request, an LP can post the swap by calling the [`postSwap`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Swap/MesonSwap.sol#L36) method of Meson on the initial chain X and bond it to himself. Meson contract will check the signature, transfer user's swap amount + fee, and lock them for a certain time (tentatively set to 1-2 hours). During this period, the swap will be bonded to the LP for subsequent steps. At the same time, at most one LP can complete the bonding.
3. **Lock the swap:** For an LP successfully bonded to a swap, he needs to call the [`lock`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Pools/MesonPools.sol#L79) method of Meson on the target chain Y to lock the swap funds (step 5) (tentatively 20 minutes) to ensure that the user can get paid;
4. **Release signature:** After the user validates the transactions in step 2 & 3, it is necessary to construct a signature for releasing funds within the lock period, specify the recipient address, and broadcast to inform the LP. This operation also does not require users to pay gas fees. The signature will also be checked by Meson's smart contract ([source](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/utils/MesonHelpers.sol#L187)) for the next two steps to proceed.
5. **Release fund:** After the user's release signature is made public, anyone (including the user himself) can call the [`release`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Pools/MesonPools.sol#L127) method of the Meson contract on the target chain Y. When this transaction is executed, the validity of the signature will be checked. The funds locked in step 3 will be paid to the recipient designated by the user;
6. **Receive initial funds:** Finally, the LP uses the same release signature to call the [`executeSwap`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Swap/MesonSwap.sol#L112) method of the Meson contract on the initial chain X to obtain the funds (including swap fees) deposited by the user initially. LPs can choose to withdraw this part of funds or transfer them to his liquidity pool on chain X.

![Flow of a Cross-chain Swap on Meson](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-4e00e5b8ec3a06fd65431077f9814d72cf1b3e9f%2FMeson-swap-flow.png?alt=media)

In steps 1 and 4, the use of relayer service is not mandatory. Users can also post swap requests or release signatures directly on-chain. However, this requires the user to invoke the on-chain contract and pay the gas fee. The actual process is as follows

* Posting a swap request: The user should call the `postSwap` contract method directly without LP information on the initial chain. Once processed, the LP can call the [`bondSwap`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Swap/MesonSwap.sol#L69) method to bond the swap. The consequence of the prior two is the same as an LP executing `postSwap`.
* Release the swap: The user should call the `release` contract method directly on the target chain. The LP can then see the release signature from that transaction and subsequently call the `executeSwap` method on the initial chain.

Please refer to the following diagram for the sequential process of swap.

### Rebalance Stage

After an LP provides swaps for a period of time, the distribution of his funds on different chains may be different from the initial state. If LP provides swaps in both directions of X → Y and Y → X, the overlapping parts can cancel each other so the funds that LP needs to rebalance are lower than the actual total swap amount.

When the LP rebalances the distribution of its fund pools, he can withdraw some funds from the pool by calling the [`withdraw`](https://github.com/MesonFi/meson-contracts-solidity/blob/main/contracts/Pools/MesonPools.sol#L60) method, and use the existing cross-chain solutions (cross-chain bridges, centralized exchanges, etc.) for asset movement. The time requirement for this process is relatively low, and LPs can accumulate a certain amount of funds before rebalancing. Therefore, the ratio of cross-chain fees to the swap amount would become much lower.


# Trusted Verifiers

A draft Meson Improvement Proposal

In a standard atomic swap process, the initiator of the swap (usually the user) needs to perform a second signature. This step is necessary for security reasons:

1. The user can personally verify that the counterparty (usually an LP) has correctly locked the corresponding funds on the target chain.
2. The user's funds are locked for a longer period than the LP's funds, so the user needs to sign a second time within the LP's lock period.

However, this can somewhat affect the user experience. The user needs to wait in the application interface for a period of time after initiating the swap to complete the second signature. To improve the user experience, we propose the role of *Trusted Verifiers*.

Trusted Verifiers perform the check on behalf of the user whether the LP has correctly locked funds on the target chain. They can represent the user or be neutral. This means that in a swap, the Trusted Verifier and the LP are different, and there should be no mutual interest between them.

A Trusted Verifier can be global meaning that it can be trusted by all users. Alternatively, a Trusted Verifier can be trusted by only one or a few users. The verification process is done through a signature, so a Trusted Verifier can be an individual or a group with multisig or other cryptographic settings.

Trusted Verifiers must be online at all times. The process of a swap involving a Trusted Verifier is as follows:

1. The user (she) can confirm in advance which verifiers she trusts;
2. The user publishes a swap request as in the normal process and her funds will be locked on the initial chain. Then, the LP (he) willing to match the swap completes the fund locking on the target chain;
3. The user can leave after she submits the swap request. The Trusted Verifier she trusts will verify that the LP's operation is correct, and after confirmation, will release a *verification signature*;
4. The verification signature contains a valid *release window* which is within the LP's fund locking period and shorter (for example, 10 minutes). The LP needs to complete his operation within this release window;
5. After receiving the verification signature, the matching LP can generate the release signature by himself. This release signature can be executed by anyone on both the initial and target chains to transfer the locked funds to the user and the LP, respectively;
6. To prioritize the user's receive of the swap funds, the release signature generated from verification can only release the LP's locked funds during the release window. However, during the entire LP fund locking period, LP's locked funds can be released to the user. The LP should prioritize releasing funds to the user within the release window. Otherwise, after the release window, anyone can still execute the release signature, but the LP will be penalized.

The main advantage of this process is that the user can stop paying attention to the swap process after submitting the swap request. The subsequent steps will be completed by her Trusted Verifiers and the matching LP. The user can set her trust strategy based on her security needs, such as trusting more verifiers for small swaps but trusting only a few or no other verifiers for large swaps. In the latter case, the user still signs twice to complete the entire swap process.


# Swap Fee

Using Meson to move stablecoins or ETH token cross chain might incur a small amount of fee. The fee primarily consists of two parts;

* The *service fee* is a constant 0.5% service charge (mininum $0.5 USDT/USDC/BUSD, or equivalent) levied by Meson protocol. Currently, service fee is waived for each address up to $3,000 or 3 swaps on a daily basis, whichever limit occurs first applies. *Meson Premium/Premium Plus* members are entitled to a maximum of $100,000/$500,000 or equivalent free swaps during each membership period.
* *LP fees* are levied by the Liquidity Providers (LPs) to compensate for their gas expense and cost of token conversions. Just like the first few years of the Bitcoin network, most LPs do not charge LP fees between most networks, but it might change according to network condition and market markups.

All fees are deducted on the target chain, so user will receive lesser amount of stablecoins or ETH token on the target chain. Please pay attention to the fee info in the *Swap Summary* pop-up window during the use of Meson to understand the actual fees for your cross-chain swaps. Fees illustrated in the *Comments* section are promotional rates and are therefore subject to change without notice. Meson reserved all rights on the interpretation of fees.

| Type          |       Pay to      | Amount (USD or equivalent) | Comments                                                                                                                                                                                                                              |
| ------------- | :---------------: | :------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service Fee   |   Meson Protocol  |      0.05%(min $0.5u)      | Currently waived for first 3,000 USD / 3 swaps (whichever occurs first applies) per address per day ; free for *Meson Premium/Premium Plus* up to 100,000/500,000 USD                                                                 |
| Gas & LP fees | Blockchains & LPs |        market based        | Gas fee is charged in compensation to the gas cost Meson pays on target chain and is *subject to market gas* , LP fees (up to \~1%) may also incur to compensate the cost to acquiring or unlocking liquidity on origin/target chains |

When users interact with Meson for the first time, they also need to make `approve` transactions required by the ERC20 protocol (upon first time interaction with Meson smart contracts), and therefore pay relevant gas fees.

## Service Fee

The Meson service fee is levied by Meson protocol and set to be 0.05% of the swap amount regardless of networks and token pairs.

The service fee is currently waived for all users for swaps up to daily maximum of 3,000 USD. Please note this fee waiver is temporary and is subject to change without notice.

*Meson Premium* is a membership program offering zero service-fee swaps up to 500,000 USD (Premium Plus member) during its 30-day period. Please refer to Meson Premium section for more details.

For swaps that incure service fees, Meson smart contract on the target chain will deduct the release amount by `0.05% * swap amount` or `swap amount - 0.5 USDT/USDC/BUSD` whichever is smaller, so the recipient address will receive `swap amount - 0.05% * swap amount - lp fee (if applicable)` or `swap amount - (swap amount - 0.5 USDT/USDC/BUSD) - lp fee (if applicable)` whichever is larger.

## LP Fees

LP might charge a fee to compensate their gas expenses on different networks as well as costs of token conversion. LP might adjust their accepted or preferred fee range based on network & gas conditions, market exchange rates among other factors. Currently, most LPs charge 0 fee on most swap routes and tokens.

As Meson uses LayerZero stablecoins for Aptos swaps, LP might charge a fee to compensate cost to burn LayerZero stablecoins on Aptos via LayerZero bridge. This fee is subject to the fee levied by LayerZero for use of LayerZero bridge.

LP might charge a fee to small swaps to compensate the operating cost for the use of Meson protocol. Currently, swaps below 5 USD (excluding 5 USD) will be considered small swaps and therefore see a surcharge of 0.1 USD.

Each LP predefines its fee ruleset. Upon user submission of swap, Meson app will automatically select and construct swap request with the most favorable fee offered by LPs for the swap. The LP fee is thus encoded in the swap and eventually confirmed by user's signature, and then be broadcasted and submitted for execution by the Meson smart contract. User will hence receive `swap amount - lp fee - service fee (if applicable)` on the target chain for his/her cross-chain swap.


# Liquidity Providers

Liquidity Providers (LPs) of Meson are responsible for matching incoming swap orders submitted by users. A swap is completed when user sends the designated fund to the LP pool on the initial chain, followed by the release of fund to the user from the LP pool on the target chain. Meson's atomic swap mechanism guarantees that either transfers of funds happen on both networks or neither happens at all, enforcing funds security for both users and LPs.

Pool owner is the designated owner of LP. Any valid wallet address signing up to become a LP of Meson is designated by Meson as the pool owner. Signing up for LP requires depositing liquidity to more than one networks supported by Meson. LPs can have their own choices of supported networks and tokens and deposit liquidity accordingly to the Meson smart contract on respective networks.

Each LP manage and operate his/her own independent liquidity pools designated by a unique pool index. LP is required to register a pool index (see `depositAndRegister` method) when they deposit liquidity for the first time. When a cross-chain swap is requested, LPs are opt to make independent decision whether they would like to match this specific swap order (which requires signature). However, only one LP will eventually match and complete the swap with the user. Therefore, there will be one unique pool index matching every successful swap, representing the pair of atomic swaps between user and the designated LP pool on the origin and target chains.

## Access to LP Pools

### Pool owner

Each LP pool has an *owner*. Owner address is the sole wallet address that is permitted to perform depositing and withdrawing liquidity opreations on LP pools. When an LP deposit liquidity to Meson for the first time and register a pool index, the signer address will be recorded as the owner for the LP pool created. Each address is only allowed to own one LP pool per network.

#### Permitted interactions for pool owners

Only the pool owner is permitted to call the following contract methods:

* `depositAndRegister`: First-time deposit of liquidity and register pool index; Caller becomes the pool owner;
* `deposit`: Deposit of liquidity to an existing LP pool
* `withdraw`: Withdrawal of liquidity from an existng LP pool

![Operations of Pool Owners](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-bfe951fc36f8c932de6b6a889f11dd44a9a136ff%2FMeson-LP-flow.png?alt=media)

### Authorized addresses

As LPs are required to sign for each swap, Meson allows the pool owner to grant others as *authorized addresses* to perform swaps on its behalf. Please note the pool owner is always an authorized address of its own pool.

In this design of authorization, LPs no longer need to expose their private key every time to perform swaps after depositing liquidity, whereas authorized addresses could call Meson smart contract to perform swaps with the liquidity available in the pools. Funds only moves around the designated LP pools on different networks and therefore exposes to very low security risk by authorizing swaps. Authorized addresses are not permitted to withdraw liquidity under any circumstances, as only the pool owner is permitted to do so.

#### Permitted interactions for authorized addresses

Authorized addresses are permitted to call the following contract methods:

* `bondSwap`: Upon acknowledgement of user's swap request, call on the initial chain to match the user swap order (no pool fund movement involved);
* `lock`: Upon acknowledgement of user swap request, call on the target chain to lock in funds in the pool, which will be releasd to user in the following `release` call;
* `release`: Upon successful order match (both `bondSwap` and `lock` executed), call on the target chain to release the locked funds to the user to complete the swap (meanwhile, call to `executeSwap` will be exectued to acquire the inbound fund from user and add it to the LP pool on the initial chain).

![Operations of Authorized Addresses](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-aabe8b0a1f3030f80d33692029ad3acea8361fb2%2FMeson-LP-flow-authAccess.png?alt=media)


# System Design

The original HTLC design only described the process of the on-chain part and did not say how to efficiently and safely conduct the off-chain communication. In Meson, a set of off-chain services can ensure that users' swaps can be responded and completed stably and quickly, bringing a better user experience.

The Meson system architecture primarily consists of 4 components:

![Meson App Architecture.png](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-e6d8deb5c5b7af0c5f2081299f607d279c06b4cb%2Fmeson_arch.png?alt=media)

* **Frontend apps** are the user-facing frontend applications
  * **Meson app** is the main app for users allowing them to contruct and submit cross-chain swaps on Meson. Users can also track progress of recent swaps.
  * **Meson explorer** is Meson's explorer outlining details of swaps submitted to Meson protocol, including swap information and step details with reference to transactions on each respective chain. The Meson explorer is maintained with persistent data storage of all submitted swaps and display them through the explorer user interface. Users can also search for swaps through the explorer.
* **Relayer** is a distributed messaging API service sitting between Meson app and LP services. Relayer receives initial swap request and following swap release data, performs basic checks and broadcasts to LP services for further processing. It behaves in the similar way to P2P network of Bitcoin or Ethereum blockchains.
* **LP services** are executables that process and issue swap transactions on behalf of LPs. They receive swap data from the relayer, verify checks, process it and post to the respective blockchains. Since LP services are posting the actual on-chain transactions, they will pay gas fees for users. LP services cannot tamper or modify swap data as it has been signed by the user. This service is like the miner program of a public chain.
* **Smart contracts** are the implemenatation of Meson protocol on each blockchain. They will receive swap data, check signatures, and orchestrates the whole Meson swap process on respective chains.

A typical flow of Meson swap across different systems is as follows

* A swap request is inititated and signed by a user on Meson app.
* The swap request along with the signature are submitted to the relayer and consequently be broadcasted to LP services.
* LP services will receive the incoming swap request, construct the respective transaction, and execute the Meson smart contracts. Notice that only one LP will finally match a given swap on chain.
* The same process will be repeated for processing the swap release to finish the entire swap.

Meson protocol also provides a backup plan that users can directly post swap request and release to the blockchain and pay gas fees themselves. In this case, LP services will receive swap data from on-chain events instead of the relayer, and complete their corresponding part of the swap.

## Roles

There are three roles in Meson: users, liquidity providers (LPs) and relayers.

* *Users*, also named *initiators* in swap encoding, are those who demand for cross-chain stablecoin swaps. They usually follow the [User Guide](https://docs.meson.fi/guides/meson) to use Meson.
* *Liquidity Providers (LPs)* provide stablecoin liquidities to Meson and match cross-chain swaps with users. They or their authorized addresses should run LP services to complete swaps. Please refer to [Liquidity Providers](https://github.com/MesonFi/docs/blob/main/protocol/meson/meson-lp/README.md) and [LP service](https://docs.meson.fi/protocol/system-design/lp-service) to learn more details.
* *Relayers* are runnings the Meson relayer service to broadcast swap data. The registration for becoming a relayer is not opened for now, but you can read [Relayer Service](https://docs.meson.fi/protocol/system-design/relayer) and learn more about how it works.


# Relayer

{% hint style="info" %}
The relayer service will be continuously updated in the future to ensure high availability and robustness as the number of users and swap volumes increases.
{% endhint %}

When a user submits a swap request or a release signature, the data needs to be broadcast to the LP network. The relayer service will be responsible for broadcasting users’ swaps. Specifically, it will transmit swap information with request or release signatures to LPs who submit transactions to the blockchain. However, the service does not check the validity of the data, so it is up to the [LP service](https://docs.meson.fi/protocol/system-design/lp-service) to check of the swap information and signatures after receiving the data.

In Meson, we want to build an effective relay network to guarantee swap information will be efficiently transmitted. In order to achieve this target, our so-called relayer service is not a single service, but a mixture of various schemes. Multiple copies of the relayer are run distributedly, and each one will communicate with others for data synchronization. Users can choose to submit data to any relayer, and LPs can choose to listen to the right relayer based on geographic location and network latency. According to CAP theorem, under the premise of partitioning only one of availability and consistency can be achieved. Our relayer service will prioritize availability, so the data on different relayers may be inconsistent, meaning that a single relayer service cannot guarantee that all swap requests are received on time. This has less impact on users and LPs because we only need to ensure that once a user submits a request, *some* LPs will receive the data and match the swap.

The design goals of the relayer service are:

* **High availability:** users can use this service at any time;
* **Censorship free:** no one can block the transfer of information;
* **Guaranteed delivery:** within a certain period of time, the information must be delivered;
* **Fault tolerance:** we don't assume any service will work perfectly as designed so we will provide ample alternatives.

To achieve these goals, our relayer service integrates the following solutions

* Decentralized p2p network
* Distributed service
* Direct on-chain operation

### Peer-to-peer network

Decentralized p2p network can provide very good availability and accept any submitted data without censorship. Blockchain transactions are usually transmitted using p2p networks, proving their advantages in this regard. We will use a p2p network as the main route for swap propagation. Users can submit swap information and signatures to one or more nodes, and peers will be responsible for synchronizing the information to the entire network. LPs can listen to any node and get swap data submitted by users.

The p2p network does not guarantee data consistency, which may cause swaps seen by different peers and LPs to be different. This will not be a problem because when conflicting swaps are submitted to the blockchain, the consensus algorithm on-chain will ensure that only one can be finally confirmed.

However, a decentralized network does not guarantee the timing of data delivery. We want to ensure that swaps can be processed quickly, so this issues needs to be properly handled and optimized. The partial centralized service that will be introduced below will address this issue and accelerate information transmission.

While a fully distributed p2p network has many advantages, there are also many challenges to running such a network. A p2p network that just starts running usually has problems with stability due to lack of enough peers. Availability and efficiency may be low, and data synchronization and delivery are not sufficiently assured. This is another reason we designed partial centralized services.

### Partial centralized service (c-relayer)

A trusted centralized service can easily guarantee high availability and efficient data access. Therefore, we will build and run a centralized service, named c-relayer. which will accept user’s swap requests and signatures, let LPs obtain swap information, and synchronize swaps through the p2p network. C-relayer is partially centralized because others can also run it and users can submit swaps to anyone or more of them. Each c-relayer will maintain swaps it receives from users and synchronizes them over the p2p network (or through direct connections to other c-relayers). Instead of listening to the p2p network, LPs can also listen to c-relayers, presumably more than one to ensure that as many swaps as possible can be obtained.

Running the c-relayer also requires a database to store past swap information and provide APIs for historical swap records. Meson's swap explorer will render swap history based on the c-relayer we host, which will store and index all historical data. For self-hosted c-relayers, expired swaps can be cleared to reduce the burden of running c-relayer.

At the beginning of the p2p network formation process, c-relayers will provide reliable services to users and LPs. While the p2p network is growing, the c-relayer can also continue to run and provide more efficient swap processing. At that time, c-relayers will gradually integrate with the p2p network and become a part of the network. In other words, c-relayer will evolve into full-nodes in the p2p network, providing more functions such as API and data backup. Ordinary peers will become light-nodes which only provide basic broadcast features.

### Direct on-chain operation

In addition, meson also provides a route of directly interacting with on-chain contracts and completing transactions. In this process, the user's swap will be directly submitted to the blockchain, passing through the chain's own p2p network before packed into blocks. LPs may need to access some swap information and they can listen to the blockchain mempool or watch for recent blocks to extract swaps executed on meson. The shortcoming of direct on-chain execution is that users need to have wallets on both initial and target chains, and pay gas fees for transactions, but they can ensure the swap will be executed on-chain immediately. This scheme is more complicated in terms of user interaction, but we keep this as a backup plan to handle swaps.


# Relayer APIs

The relayer provides the following APIs to receive swap request and release, and to query recent swaps.

The current Meson relayer is running at <https://relayer.meson.fi>.

### Submit a Swap Request

Receives an incoming swap request submitted by Meson app. Calling this API requires the swap request data and a valid user signature. The relayer will perform preliminary checks and broadcast the data to connected LP services if deemed valid.

```
POST https://relayer.meson.fi
```

**Request Body**

Example:

```json
// TODO give an example
{
  "encoded": ""
}
```

### Submit a Swap Release

Receives an incoming swap release submitted by Meson app. Calling this API requires the swap release data and a valid user signature. The relayer will perform preliminary checks and broadcast the data to connected LP services if deemed valid.

```
PUT https://relayer.meson.fi
```

**Request Body**

Example:

```json
// TODO give an example
{
  "encoded": ""
}
```

### Query Recent Swaps

Returns swaps form the pending pool, which are swaps that were submitted to the relayer recently but have not completed the entire swap process.

```
GET https://relayer.meson.fi
```

**Returns**

Example:

```json
// TODO give an example
[
  {
    "encoded": ""
  },
  ...
]
```


# LP Service

In Meson's swap process, users and LPs need to conduct multiple rounds of information exchange and verification. This process happens off-chain and requires LP to run a service, complete the necessary verification, signature, call Meson contract and other operations. We will provide an open source service that any LP can run to complete the redemption process. The LP needs to run this service on its own server, actively monitor the swap initiated by the user, lock funds for the swap, and finally complete the swap on the two chains. We will release an open source LP service that can complete the above process for most LPs to use. For LPs with independent trading strategies, they can modify and design specific workflow in the swap process according to the Meson protocol and the open-sourced LP services to meet their specific trading preferences.


# Security Precautions

In order to ensure the safety of the funds of both parties of users and LPs, some necessary matters need to be paid attention to during the swap process.

Worth mentioning that Meson does not rely on cross-chain services such as bridges and oracles in its swap process, so it will not be affected by the security issues of third-party services.

### Precautions for Users

#### Swap signature phishing

Severity: 🟥🟥🟥

Attackers might attempt to forge a website for Meson and phish for users' signatures. This attempt, if succeeded, could mislead users to sign for unintended cross-chain swaps that transfer funds to attackers' addresses, causing a loss of funds to users. Users should exercise a high degree of caution to make sure they're on Meson's official website (\[<https://meson.fi>]) while making cross-chain swaps.

#### Congested target chain

Severity: 🟥🟥🟥

When the target chain of a cross-chain swap becomes congested, the swap might not be able to complete. Users might need to pay a higher gas fee to support the execution of `release` operation within the lock period. Otherwise, the LP could `unlock` the fund after the lock ends, causing a loss of funds to the user.

We recommend against cross-chain swaps when the network is very congested. Usually in this case, the initial step of the swap `bondSwap` cannot be completed.

**WIP**

#### Release too late

Severity: 🟥🟥🟥

If the user posts the release signature after the lock period, the LP could `unlock` his/her fund and use the release signature to retrieve the user's fund, causing a loss of fund to the user. We strongly recommend users only post the release signature in a timely manner and do not attempt to sign for release if it's deemed too late. The Meson app has procedures in place to deal with such circumstances.

#### Release too early

Severity: 🟨🟨⬜️

If the user does not wait for enough block confirmations and posts the release signature too soon, the `lock` transaction might be reverted and the user will not be able to get swapped funds on the target chain. We strongly recommend users wait for enough block confirmations before signing the release signature. The Meson app has procedures in place to deal with such circumstances.

#### No release

Severity: 🟨🟨⬜️

Upon receiving the release signature from the user, a misbehaved LP could only call `execute` but not `release`. This LP will hence retrieve the user's fund on the initial chain without paying out to the user on the target chain. If the `release` operation is not called within the lock period, the LP could `unlock` and the user will not be able to get swapped funds. However, anyone, including the user, could complete the release process once the release signature is revealed. Meson will guarantee the execution of `release` operation within the proper time period.

In the future, We will introduce penalties for such misbehaved LPs.

#### No lock

Severity: 🟩⬜️⬜️

The swap process will not continue if a misbehaved LP does not `lock` after successful `bondSwap` operation. However, such LPs will have to pay gas fees but receive no benefit at all. Users will need to wait until expiration to withdraw their funds and restart a new swap.

In the future, We will introduce penalties for such misbehaved LPs.

#### Front-running

Severity: 🟩⬜️⬜️

When a swap request is submitted, attackers might forge a fake swap with the same encoding and execute it on the initial chain to block the user's swap, as only one swap is allowed per encoding. However, the attacker will have to lock his/her own fund for 1-2 hours and pay gas fees, but receive no benefit at all. Users who encountered this type of issue can simply bypass it by resubmitting another swap.

### Precautions for LPs

#### Congested initial chain

Severity: 🟥🟥🟥

When the initial chain of a cross-chain swap becomes congested, swaps might not be able to complete. LPs might need to pay a higher gas fee to support the execution of `executeSwap` operation to retrieve users' funds. Otherwise, the user could withdraw the fund after the swap expires, causing a loss of funds to the LP.

We recommend against cross-chain swaps when the network is very congested. Usually in this case, the initial step of the swap `lock` cannot be completed.

**WIP**

#### Lock too late

Severity: 🟥🟥🟥

If the LP `lock`s a swap too late causing the fund remains locked beyond the swap's expiration time, the user could temporarily hold his/her release signature till the swap expires. Hereafter, the user could execute `cancelSwap` to withdraw his/her fund and attempt `release` operation to retrieve the LP's fund, causing loss of fund to the LP. We strongly recommend LPs call `lock` operation in a timely manner and do not attempt to `lock` when it's deemed too late. The Meson LP service has procedures in place to deal with such circumstances.

#### Lock too early

Severity: 🟨🟨⬜️

If the LP does not wait for enough block confirmations of `postSwap/bondSwap` operations before calling `lock`, the `postSwap/bondSwap` transaction might be reverted and LPs will not be able to get swapping funds on the initial chain. We strongly recommend LPs wait for enough block confirmations before calling `lock`. The Meson LP service has procedures in place to deal with such circumstances.

#### No release signature

Severity: 🟩⬜️⬜️

A misbehaved user might choose not to post the release signature after submission of swap request and fund being locked. Although funds on both intial and target chains stay safe, a part of LP's liquidity will be locked for a period of time and paid gas fees were wasted. However, the user's fund will also be locked for longer time.

In the future, We will introduce penalties for such misbehaved users.

#### Double spending

Severity: 🟩⬜️⬜️

A misbehaved user might repeatedly submit multiple swap requests without enough available stablecoins in his/her address. The Meson contract need to acquire swapping fund when executing `postSwap`, whereas the lack of balance or approval will lead to execution failure. In this case, the LP may waste some gas fees for failed transactions. We recommend LPs perform balance and approval checks before processing users' swap requests.

In the future, We will introduce penalties for such misbehaved users.

### Attack to Relayers

#### Spamming

Severity: 🟨🟨⬜️

Attackers may spam the Meson relayer with excessive trash messages to congest the relayer service. The Meson relayer will check each received request to confirm the data conforms to the Meson protocol and the swap initiator has enough balance to carry out the cross-chain swap. Meson also requires at least US$0.01 in stablecoins to be transferred per swap. After the conditions are met, the relayer will broadcast the data to other connected nodes or LP services. In this way, the spamming attack will only affect one relayer node, and other relayers can still continue to operate.


# Waiting Time

### How long to wait for a transaction on each chain?

In the process of atomic swaps, participants need to wait for the previous step to be executed and safely confirmed before proceeding to the next step. This will determine the overall time of the swap. During the process of a Meson swap, we recommend the following waiting times.

#### From `postSwap` → `bondSwap`

Right away. If `postSwap` transaction is reverted, `bondSwap` cannot be executed. If `postSwap` tx is replaced by another swap with the same encoding but different initiator, the LP can still bond to it because the swap properties are the same.

Notice that `postSwap` may specify the bonded provider. In this case `bondSwap` is not needed and cannot be executed.

#### From `postSwap` / `bondSwap` → `lock`

Wait for enough confirmations on the initial chains. Otherwise, `postSwap` or `bondSwap` transaction may be reverted.

#### From `lock` → publish release signature

Wait for enough confirmations on the target chains. Otherwise, the `lock` transaction may be reverted.

#### From publish release signature → `release` & `executeSwap`

Right away. The order doesn’t matter.


# Smart Contracts

The Meson protocol can be implemented in different smart contract languages. We currently provide an implementation of [Solidity](https://docs.meson.fi/implementation/smart-contracts/solidity). We are also working on support for other languages.


# Meson in Solidity

We have implemented the Meson protocol with Solidity smart contracts, and deployed to the following EVM-compatible public chains:

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

### Chain-specific System Invariates

The chain-specific invariants are given in the `MesonConfig.sol` file. The [compile and deploy script](https://github.com/MesonFi/meson-contracts-solidity#deployment) will automatically set this config file.

* `SHORT_COIN_TYPE` (uint16): The identifier of the chain. We use the last 2 bytes of [SLIP-44](https://github.com/satoshilabs/slips/blob/master/slip-0044.md) as the unique ID of a chain:

  | Chain     | Short Coin Type |
  | --------- | --------------- |
  | Ethereum  | 0x003c          |
  | Tron      | 0x00c3          |
  | Conflux   | 0x01f7          |
  | Optimism  | 0x0266          |
  | BNB Chain | 0x02ca          |
  | Polygon   | 0x03c6          |
  | Fantom    | 0x03ef          |
  | Harmony   | 0x03ff          |
  | Moonbeam  | 0x0504          |
  | Moonriver | 0x0505          |
  | Aurora    | 0x0a0a          |
  | Evmos     | 0x11bc          |
  | Avalanche | 0x2328          |
  | Arbitrum  | 0x2329          |
* `MIN_BOND_TIME_PERIOD` (uint256) & `MAX_BOND_TIME_PERIOD` (uint256): The minimal and maximum expire time when bonding a swap, set to 1 hour and 2 hours, respectively. The swap encoding will include a timestamp `expireTs` before which the user's assets will be locked on the initial chain. The LP should call `executeSwap` before `expireTs` to take away the swapping fund. The `expireTs` needs to satisfy `ts_bonded_tx + MIN_BOND_TIME_PERIOD < expireTs < ts_bonded_tx + MAX_BOND_TIME_PERIOD`, where `ts_bonded_tx` is the block time for the executed `postSwap` transaction.
* `LOCK_TIME_PERIOD` (uint256): The time length when an LP locks a swap, sets to 40 minutes. The initiator should sign the release signature to get swapped assets on the target chain before the time `ts_locked_tx + LOCK_TIME_PERIOD`, where `ts_locked_tx` is the block time for the executed `lock` transaction.
* `REQUEST_TYPE_HASH` (bytes32): Equals to `keccak256(bytes32 "Sign to request a swap on Meson")` or `keccak256(bytes32 "Sign to request a swap on Meson (Testnet)")`. It's used when checking the request signature.
* `RELEASE_TYPE_HASH` (bytes32): Equals to `keccak256(bytes32 "Sign to release a swap on Meson" + bytes32 [Recipient])` or `keccak256(bytes32 "Sign to release a swap on Meson (Testnet)" + bytes32 "[Recipient]")`. It's used when checking the release signature.

### Source Code

{% embed url="<https://github.com/MesonFi/meson-contracts-solidity>" %}
Meson Smart Contracts
{% endembed %}


# Time

### Bond time and lock time

In the process of an atomic swap, both parties need to lock the funds on the initial and target chains respectively for a certain period of time. In order to ensure the safety and smoothness of swaps, the lock time for Meson is based on the related chains and swap amount. For chains that require longer confirmation times or swaps that have larger amounts, longer lock times are required.

### Time to finish a swap

Total time equals the sum of

* Time for `postSwap` / `bondSwap` with confirmations (confirmation time on the initial chain)
* Time for `lock` with confirmations (confirmation time on target chain)
* The duration between the swap is securely locked and the user publishes the release signature
* Time for `release` (confirmation time on target chain)

The time for broadcasting swap requests and swap releases on the relayer can be neglected which only takes \~1 second.

If the user signs for release right away, the total time for the swap equals one confirmation time on the initial chain plus two confirmation times on the target chain. For example,

* Ethereum → Non-Ethereum: 3-12 min
* Non-Ethereum → Ethereum: 6-20 min
* Non-Ethereum → Non-Ethereum: \~3 min

For some swaps of small amounts between non-Ethereum chains, users can even receive swapped amounts within 1 minute.


# Applications

We built a [web application for Meson](https://beta.meson.fi) which users can access it to complete cross-chain stablecoin swaps.

We also built a [swap explorer](https://explorer.meson.fi) where user can search for swap history and monitor the progress.

### Source Code

{% embed url="<https://github.com/MesonFi/meson-app>" %}

{% embed url="<https://github.com/MesonFi/meson-explorer>" %}


# Audits

## First Round of Audit

**Auditor : SSLab at Georgia Institute of Technology**

**Date of Report : February 26th 2022**

Report can be viewed [here](https://static.meson.fi/MesonFi-Audit-Report-R1-2022Feb.pdf)

## Second Round of Audit - Design Review

**Auditor :** [**Trail of Bits**](https://www.trailofbits.com/)

**Date of Report : July 15th 2022**

Report can be viewed [here](https://static.meson.fi/MesonFi-Audit-Report-R2-2022Jul.pdf)

## Third Round of Audit - Security Review

**Auditor :** [**Trail of Bits**](https://www.trailofbits.com/)

**Date of Report : October 3rd 2022**

Report can be viewed [here](https://static.meson.fi/MesonFi-Audit-Report-R3-2022Oct.pdf)

## Fourth Round of Audit - Fix Review

**Auditor :** [**Trail of Bits**](https://www.trailofbits.com/)

**Date of Report : October 3rd 2022**

Fix Review consists of a review of all fixes in reponse to the security vulnerabilities foundings in Round 3. Report can be viewed [here](https://static.meson.fi/MesonFi-Audit-Report-R4-2022Oct.pdf)

We will continue to invite worlds' leading smart contract auditors to perform robust audits on Meson Protocol, Smart Contracts and Apps. Please check back for more updates and audit deliveries!


# Stablecoins supported by Meson

Below summarizes all supported tokens accepted by Meson Protocol as intake tokens, and the payout tokens user should expect to receive at the end of a Meson swap as well.

### Disclaimer

**The list of supported tokens is subject to change without notice, based on market situations and availability.** Meson is solely the provider of the cross-chain services, while Meson aim to support the natively issued stablecoins or tokens on each of the blockchain, some emerging blockchains do not have native stablecoins or tokens available yet. In such circumstances, Meson supports the most circulating stablecoins or wrapped tokens in lieu of native stablecoins and tokens.

**Meson is NOT the issuer of the tokens listed below.** Please research before your make cross-chain swap as the value of the token assets on chain may change due to unforeseenable events. Should you have any questions, please inquire directly to the issuer of the token.

Ethereum

| Coins | Address                                    | Decimals | Issuer |
| ----- | ------------------------------------------ | -------- | ------ |
| ETH   | -                                          | 18       | Native |
| USDT  | 0xdAC17F958D2ee523a2206206994597C13D831ec7 | 6        | Native |
| USDC  | 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 | 6        | Native |
| BUSD  | 0x4Fabb145d64652a948d72533023f6E7A623C7C53 | 6        | Native |

BNB CHAIN

| Coins | Address                                    | Decimals | Issuer |
| ----- | ------------------------------------------ | -------- | ------ |
| USDT  | 0x55d398326f99059fF775485246999027B3197955 | 18       | Native |
| USDC  | 0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d | 18       | Native |
| BUSD  | 0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56 | 18       | Native |

Polygon

| Coins | Address                                    | Decimals | Issuer |
| ----- | ------------------------------------------ | -------- | ------ |
| USDT  | 0xc2132D05D31c914a87C6611C10748AEb04B58e8F | 6        | Native |
| USDC  | 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174 | 6        | Native |

Avalanche

| Coins | Address                                    | Decimals | Issuer   |
| ----- | ------------------------------------------ | -------- | -------- |
| USDt  | 0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7 | 6        | Bitfinex |
| USDC  | 0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E | 6        | Native   |

Arbitrum

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| ETH   | -                                          | 18       | Native          |
| USDT  | 0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9 | 6        | Official Bridge |
| USDC  | 0xaf88d065e77c8cC2239327C5EDb3A432268e5831 | 6        | Native          |

Optimism

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| ETH   | -                                          | 18       | Native          |
| USDT  | 0x94b008aA00579c1307B0EF2c499aD98a8ce58e58 | 6        | Official Bridge |
| USDC  | 0x7F5c764cBc14f9669B88837ca1490cCa17c31607 | 6        | Official Bridge |

Tron

| Coins | Address                            | Decimals | Issuer |
| ----- | ---------------------------------- | -------- | ------ |
| USDT  | TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t | 6        | Native |
| USDC  | TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8 | 6        | Native |

Fantom (Currently unavailable)

| Coins | Address                                    | Decimals | Issuer     |
| ----- | ------------------------------------------ | -------- | ---------- |
| USDC  | 0x04068DA6C83AFCFA0e13ba15A6696662335D5B75 | 6        | Multichain |

Aurora

| Coins  | Address                                    | Decimals | Issuer          |
| ------ | ------------------------------------------ | -------- | --------------- |
| ETH    | -                                          | 18       | Native          |
| USDT.e | 0x4988a896b1227218e4A686fdE5EabdcAbd91571f | 6        | Official Bridge |
| USDC.e | 0xB12BFcA5A55806AaF64E99521918A4bf0fC40802 | 6        | Official Bridge |

Conflux e-Space

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| USDT  | 0xfe97e85d13abd9c1c33384e796f10b73905637ce | 6        | Official Bridge |
| USDC  | 0x6963efed0ab40f6c3d7bda44a05dcf1437c44372 | 6        | Official Bridge |

Moonbeam

| Coins  | Address                                    | Decimals | Issuer |
| ------ | ------------------------------------------ | -------- | ------ |
| xcUSDT | 0xffffffffea09fb06d082fd1275cd48b191cbcd1d | 6        | Native |

Moonriver (Currently unavailable)

| Coins | Address                                    | Decimals | Issuer     |
| ----- | ------------------------------------------ | -------- | ---------- |
| USDC  | 0xE3F5a90F9cb311505cd691a46596599aA1A0AD7D | 6        | Multichain |

Cronos

| Coins | Address                                    | Decimals | Issuer     |
| ----- | ------------------------------------------ | -------- | ---------- |
| USDT  | 0x66e428c3f67a68878562e79A0234c1F83c208770 | 6        | Crypto.com |
| USDC  | 0xc21223249CA28397B4B6541dfFaEcC539BfF0c59 | 6        | Crypto.com |

Aptos

| Coins | Address                                                                         | Decimals | Issuer    |
| ----- | ------------------------------------------------------------------------------- | -------- | --------- |
| zUSDT | 0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT | 8        | LayerZero |
| zUSDC | 0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC | 8        | LayerZero |

Sui

| Coins | Address                                                                        | Decimals | Issuer              |
| ----- | ------------------------------------------------------------------------------ | -------- | ------------------- |
| USDT  | 0xc060006111016b8a020ad5b33834984a437aaa7d3c74c18e09a95d48aceab08c::COIN::COIN | 9        | Wormhole (Ethereum) |
| USDC  | 0x5d4b302506645c37ff133b98c4b50a5ae14841659738d6d733d59d0d217a93bf::COIN::COIN | 9        | Wormhole (Ethereum) |

zkSync Era

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| ETH   | -                                          | 18       | Native          |
| USDC  | 0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4 | 6        | Official Bridge |

Polygon zkEVM

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| ETH   | -                                          | 18       | Native          |
| USDT  | 0x1E4a5963aBFD975d8c9021ce480b42188849D41d | 6        | Official Bridge |
| USDC  | 0xA8CE8aee21bC2A48a5EF670afCc9274C7bbbC035 | 6        | Official Bridge |

EOS EVM

| Coins | Address                                    | Decimals | Issuer     |
| ----- | ------------------------------------------ | -------- | ---------- |
| USDT  | 0xfA9343C3897324496A05fC75abeD6bAC29f8A40f | 6        | Multichain |

Linea

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| ETH   | -                                          | 18       | Native          |
| USDT  | 0x176211869cA2b568f2A7D4EE941E073a821EE1ff | 6        | Official Bridge |
| USDC  | 0xA219439258ca9da29E9Cc4cE5596924745e12B93 | 6        | Official Bridge |

BASE

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| ETH   | -                                          | 18       | Native          |
| USDbC | 0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA | 6        | Official Bridge |

KAVA EVM

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| USDT  | 0x919C1c267BC06a7039e03fcc2eF738525769109c | 6        | Official Bridge |

Metis

| Coins  | Address                                    | Decimals | Issuer          |
| ------ | ------------------------------------------ | -------- | --------------- |
| m.USDT | 0xbB06DCA3AE6887fAbF931640f67cab3e3a16F4dC | 6        | Official Bridge |
| m.USDC | 0xEA32A96608495e54156Ae48931A7c20f0dcc1a21 | 6        | Official Bridge |

Skale | Europa Liquidity Hub

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| USDT  | 0x1c0491E3396AD6a35f061c62387a95d7218FC515 | 6        | Official Bridge |
| USDC  | 0x5F795bb52dAC3085f578f4877D450e2929D2F13d | 6        | Official Bridge |

Skale | Nebula Gaming Hub

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| USDC  | 0xCC205196288B7A26f6D43bBD68AaA98dde97276d | 6        | Official Bridge |

Manta Pacific

| Coins | Address | Decimals | Issuer |
| ----- | ------- | -------- | ------ |
| ETH   | -       | 18       | Native |

Mantle

| Coins | Address                                    | Decimals | Issuer          |
| ----- | ------------------------------------------ | -------- | --------------- |
| USDT  | 0x201EBa5CC46D216Ce6DC03F6a759e8E766e956aE | 6        | Official Bridge |
| USDC  | 0x09Bc4E0D864854c6aFB6eB9A9cdF58aC190D0dF9 | 6        | Official Bridge |

Nautilus

| Coins | Address                                    | Decimals | Issuer    |
| ----- | ------------------------------------------ | -------- | --------- |
| USDT  | 0xBDa330Ea8F3005C421C8088e638fBB64fA71b9e0 | 6        | Hyperlane |
| USDC  | 0xB2723928400AE5778f6A3C69D7Ca9e90FC430180 | 6        | Hyperlane |


