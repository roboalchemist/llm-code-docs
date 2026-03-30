# Source: https://io.net/docs/guides/payment/io-cloud-payments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> This document describes how to add crypto wallets and pay using the wallet or with credit cards.

io.net offers IO Cloud users different payment methods. Users may also pay at different points in the cluster deployment process.

## Table of Contents

* [Fees](/guides/payment/io-cloud-payments#fees)
* [Add Wallet for Crypto](/guides/payment/io-cloud-payments#adding-a-wallet-for-crypto-payments)
* [Manage funds page](/guides/payment/io-cloud-payments#manage-funds-page)
* [Deploy Cluster and Pay with \$IO Coin, USDC Crypto or Fiat](/guides/payment/deploy-cluster-and-pay)
* [Extending Your Cluster and Pay with \$IO Coin or USDC Crypto](/guides/payment/extending-your-cluster-and-pay)

### Fees

There are fees associated with reserving GPU & CPU and for payments made in USDC.

* Payments made in USDC are subject to **2% facilitation fee**.
* The IOG Network charges users a **0.25% reservation fee** on the total cost to reserve the compute. This is added to the Renter’s cost when reserving. There are fees associated with reserving GPU & CPU and for payments made in \$IO Coin.
* Payments made in \$IO Coin **incur no fees**.
* The IOG Network charges users a **0.25% reservation fee** on the total cost to reserve the compute. This is added to the Renter’s cost when reserving. To learn more, see [IO Coin.](https://internet-of-gpus.readme.io/docs/what-is-io-coin).

All suppliers must add at least three **(3) self-custodial Solana wallets** to their IO ID account to remain eligible for **Block Rewards**. This requirement is effective as of **23:59:59 UTC on April 30, 2025.**

You can associate up to **10 Solana wallets** with your account. One wallet will be designated as the **Primary Wallet**, which will serve as the default for all transactions **except Block Rewards Distribution.**

Please ensure your account meets this requirement to continue participating in the reward program.

For detailed steps on adding and managing wallets, please refer to the instructions below:

## Adding a Wallet for Crypto Payments

If you plan to pay using crypto, you must add a wallet to your account. **Credit card users don't need to complete this step.**

### Connect a Single Solana Wallet

To learn how to create your own Solana wallet, check out this [short guide](/guides/workers/solana). When you create your account, you are promoted to add a wallet. You can also skip the step and add your wallet in **Account Settings**.

Follow the steps below to add a wallet to your account:

1. Click on your icon in the upper right and select **Account Settings**.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d2b2ce74100be67815492648ce295031603b55055dd32341deedfe26d31c4e-step1.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=c6689675f3f94359b99b729cde2e27a5" alt="" className="mx-auto" style={{ width:"49%" }} data-og-width="588" width="588" data-og-height="612" height="612" data-path="images/docs/70d2b2ce74100be67815492648ce295031603b55055dd32341deedfe26d31c4e-step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d2b2ce74100be67815492648ce295031603b55055dd32341deedfe26d31c4e-step1.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=2f95e918e2e8e24e5267836f50883f6d 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d2b2ce74100be67815492648ce295031603b55055dd32341deedfe26d31c4e-step1.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=07f8d7e8c332bfab2dd411f39680d450 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d2b2ce74100be67815492648ce295031603b55055dd32341deedfe26d31c4e-step1.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=b58efeae82c2b35bd45a7f2b62ba570c 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d2b2ce74100be67815492648ce295031603b55055dd32341deedfe26d31c4e-step1.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=7e0206f4f2c9e5ece0d889310c4d382f 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d2b2ce74100be67815492648ce295031603b55055dd32341deedfe26d31c4e-step1.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=4c1df1ce7c833b318ab80485c6c88df4 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/70d2b2ce74100be67815492648ce295031603b55055dd32341deedfe26d31c4e-step1.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=a2038fee051df69f4c0c7fc80a6da2de 2500w" />
   </Frame>
2. In Account Settings, find the **Solana Wallet Address** block and click the **Add Wallet** button.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/db926f4751a512ab40397490b23a21eb894b89fbf773967b30ba35909af8d940-step2.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=5d0ecd56df13a81ffa2ae232dbda2f53" alt="" className="mx-auto" style={{ width:"83%" }} data-og-width="1612" width="1612" data-og-height="448" height="448" data-path="images/docs/db926f4751a512ab40397490b23a21eb894b89fbf773967b30ba35909af8d940-step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/db926f4751a512ab40397490b23a21eb894b89fbf773967b30ba35909af8d940-step2.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=ea541e7e8541ce4c88338a41d6fcc7cb 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/db926f4751a512ab40397490b23a21eb894b89fbf773967b30ba35909af8d940-step2.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=8e7623f03e661330f379140c864feeab 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/db926f4751a512ab40397490b23a21eb894b89fbf773967b30ba35909af8d940-step2.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=3905d5705695f824fd3a880758507538 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/db926f4751a512ab40397490b23a21eb894b89fbf773967b30ba35909af8d940-step2.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=6a7f50b663697d617ff94dca297d6136 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/db926f4751a512ab40397490b23a21eb894b89fbf773967b30ba35909af8d940-step2.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=03de6f32688d5d91d803dbb620b15d2c 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/db926f4751a512ab40397490b23a21eb894b89fbf773967b30ba35909af8d940-step2.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=aee37e97f81644282d2a8d3fb4afb994 2500w" />
   </Frame>
3. In the appearing popup, enter your new **Solana wallet address**
4. Click **Connect** to add the new address.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/83dad721d308292a8b16bcfb03629f2b5ca9b840f8d3912dc829204d421ba78d-Step3.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=7d43a595facda28000ffd467a3401097" alt="" className="mx-auto" style={{ width:"77%" }} data-og-width="1582" width="1582" data-og-height="644" height="644" data-path="images/docs/83dad721d308292a8b16bcfb03629f2b5ca9b840f8d3912dc829204d421ba78d-Step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/83dad721d308292a8b16bcfb03629f2b5ca9b840f8d3912dc829204d421ba78d-Step3.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ec26344964da2ddec710caa2e2cf9ddf 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/83dad721d308292a8b16bcfb03629f2b5ca9b840f8d3912dc829204d421ba78d-Step3.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c05bb62eeb7b3363c3351ad990ce7d5f 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/83dad721d308292a8b16bcfb03629f2b5ca9b840f8d3912dc829204d421ba78d-Step3.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=7746c0fb31a7426729c0bbddbd52c8e6 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/83dad721d308292a8b16bcfb03629f2b5ca9b840f8d3912dc829204d421ba78d-Step3.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=4080a885429db6fa656a09f55b83d319 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/83dad721d308292a8b16bcfb03629f2b5ca9b840f8d3912dc829204d421ba78d-Step3.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=ea5441d0a308838ecfd002309eafd131 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/83dad721d308292a8b16bcfb03629f2b5ca9b840f8d3912dc829204d421ba78d-Step3.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=64602b00b95a84a2e713877d5f180cb9 2500w" />
</Frame>

5. As a result, your wallet will be successfully connected to the IO ecosystem.

### Connect a Single Aptos Wallet

To learn how to create your own Aptos wallet, check out this [short guide](/guides/workers/aptos-wallet). When you create your account, you are promoted to add a wallet. You can also skip the step and add your wallet in **Account Settings**.

1. Click on your icon in the upper right and select **Account Settings**.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d7389af90d6fbe7644393c325b1f40424c849441a12b790e06f84052ccda726b-step1.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=07c22829f13d6f0cd218c3d6c442d087" alt="" className="mx-auto" style={{ width:"48%" }} data-og-width="588" width="588" data-og-height="612" height="612" data-path="images/docs/d7389af90d6fbe7644393c325b1f40424c849441a12b790e06f84052ccda726b-step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d7389af90d6fbe7644393c325b1f40424c849441a12b790e06f84052ccda726b-step1.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=536756087e133a94422daa65604f273b 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d7389af90d6fbe7644393c325b1f40424c849441a12b790e06f84052ccda726b-step1.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=896c3148a97928d81e06fd0a8d429be5 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d7389af90d6fbe7644393c325b1f40424c849441a12b790e06f84052ccda726b-step1.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=4159e09915197131aa590acb3b42787e 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d7389af90d6fbe7644393c325b1f40424c849441a12b790e06f84052ccda726b-step1.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=fba7ec5edd33d27290469c4ba6d22d84 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d7389af90d6fbe7644393c325b1f40424c849441a12b790e06f84052ccda726b-step1.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=e9a21ab21650d6a10116a9b0886ed569 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/d7389af90d6fbe7644393c325b1f40424c849441a12b790e06f84052ccda726b-step1.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=227152199663d24960d765b566eced1f 2500w" />
   </Frame>
2. In the **Aptos Wallet** section, click **Add Wallet.**

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a219cf94a71111549298dd846e3b2c137c6c071fdcb6373b145efa6a8ff07cd7-step2_-2.jpg?fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=0191125ba2d285a03eb49c131f494942" alt="" className="mx-auto" style={{ width:"77%" }} data-og-width="1612" width="1612" data-og-height="448" height="448" data-path="images/docs/a219cf94a71111549298dd846e3b2c137c6c071fdcb6373b145efa6a8ff07cd7-step2_-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a219cf94a71111549298dd846e3b2c137c6c071fdcb6373b145efa6a8ff07cd7-step2_-2.jpg?w=280&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4a71abdd8e006d74a40e538f5d3eb81e 280w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a219cf94a71111549298dd846e3b2c137c6c071fdcb6373b145efa6a8ff07cd7-step2_-2.jpg?w=560&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=a489bf87d6b968d7fb582d0dd8d1e3dc 560w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a219cf94a71111549298dd846e3b2c137c6c071fdcb6373b145efa6a8ff07cd7-step2_-2.jpg?w=840&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=4852e705f73cfe74e3d36448a99921fc 840w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a219cf94a71111549298dd846e3b2c137c6c071fdcb6373b145efa6a8ff07cd7-step2_-2.jpg?w=1100&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=73671d39749adda6a17c86f766b4e6f3 1100w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a219cf94a71111549298dd846e3b2c137c6c071fdcb6373b145efa6a8ff07cd7-step2_-2.jpg?w=1650&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=5cecc4830ac29f0dd842f639fc281fa5 1650w, https://mintcdn.com/ionet-cca8037f/9uES21HxjDw9p-Ee/images/docs/a219cf94a71111549298dd846e3b2c137c6c071fdcb6373b145efa6a8ff07cd7-step2_-2.jpg?w=2500&fit=max&auto=format&n=9uES21HxjDw9p-Ee&q=85&s=d583ded7176bf403453c4bb12ab7d97a 2500w" />
   </Frame>
3. Enter your wallet address in the **Connect New Aptos Wallet** field and click **Connect**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/16c47b63befe7d1e33ed10829d257ccaa842c53b6c61b5abf7547bed0463fa1f-Step-3-2.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=ac986a932822ca37974844fe02065d7b" alt="" className="mx-auto" style={{ width:"73%" }} data-og-width="1582" width="1582" data-og-height="644" height="644" data-path="images/docs/16c47b63befe7d1e33ed10829d257ccaa842c53b6c61b5abf7547bed0463fa1f-Step-3-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/16c47b63befe7d1e33ed10829d257ccaa842c53b6c61b5abf7547bed0463fa1f-Step-3-2.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=cf73d2cb6c033bb7fcd2cc99a76fbfae 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/16c47b63befe7d1e33ed10829d257ccaa842c53b6c61b5abf7547bed0463fa1f-Step-3-2.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e923b10cf3fba35924e2769654c9c86a 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/16c47b63befe7d1e33ed10829d257ccaa842c53b6c61b5abf7547bed0463fa1f-Step-3-2.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=709daf718c83d69deb7baf9b77a6ec4b 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/16c47b63befe7d1e33ed10829d257ccaa842c53b6c61b5abf7547bed0463fa1f-Step-3-2.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=877218e53cb9d656a9177f3297f01d53 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/16c47b63befe7d1e33ed10829d257ccaa842c53b6c61b5abf7547bed0463fa1f-Step-3-2.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=13944c9699808a155771a2cde984ba62 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/16c47b63befe7d1e33ed10829d257ccaa842c53b6c61b5abf7547bed0463fa1f-Step-3-2.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=bddf2ebb55dd1ca986e4c6801960dfd8 2500w" />
</Frame>

## Adding Multiple Wallets

The **multi-wallet feature** allows you to add up to **10 Solana wallets** to your IO.net account, providing flexibility in managing **rewards, payments, and assets.**

This is particularly useful if one of your wallets becomes **inaccessible, lost, or compromised**, ensuring you still receive your rewards. Additionally, you can distribute rewards across different wallets for better **organization and security.**

You can add up to 10 wallets to your account. Here’s how to add additional wallets:

1. Underneath your first wallet address, find and click the **Add New Solana Wallet Address link**.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/1615a954e3ea6fab8691bbeb040c139790727acb4469d10c7c31da7361e9ee5e-Step4.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=df80eed0cb53824368d3d489d917de95" alt="" className="mx-auto" style={{ width:"91%" }} data-og-width="1904" width="1904" data-og-height="432" height="432" data-path="images/docs/1615a954e3ea6fab8691bbeb040c139790727acb4469d10c7c31da7361e9ee5e-Step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/1615a954e3ea6fab8691bbeb040c139790727acb4469d10c7c31da7361e9ee5e-Step4.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=d880c13905def00af2c6d3d90f7d4229 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/1615a954e3ea6fab8691bbeb040c139790727acb4469d10c7c31da7361e9ee5e-Step4.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e34115c2ae07cf2dc6e35fd5ab18394a 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/1615a954e3ea6fab8691bbeb040c139790727acb4469d10c7c31da7361e9ee5e-Step4.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=9017d2aeb2cd36c86196b4559019a267 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/1615a954e3ea6fab8691bbeb040c139790727acb4469d10c7c31da7361e9ee5e-Step4.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=2d02ed6e25d668af9adb56e0c7ca191d 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/1615a954e3ea6fab8691bbeb040c139790727acb4469d10c7c31da7361e9ee5e-Step4.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=8ce20ac3d6cdcd25b6292dad0f46f4a9 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/1615a954e3ea6fab8691bbeb040c139790727acb4469d10c7c31da7361e9ee5e-Step4.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=7c2a616c275b0954c4bedcc948dbb47b 2500w" />
   </Frame>
2. In the appearing popup, enter your new **Solana wallet address** just like you did for your first wallet.
3. Click **Connect** to add the new additional address.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/90a450125f796991010c06beeaed5165987154af57d59036bc52a5e87490aa19-Step5.jpg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f668c23c2f7137bf712644bbd091b4d7" alt="" className="mx-auto" style={{ width:"79%" }} data-og-width="1582" width="1582" data-og-height="644" height="644" data-path="images/docs/90a450125f796991010c06beeaed5165987154af57d59036bc52a5e87490aa19-Step5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/90a450125f796991010c06beeaed5165987154af57d59036bc52a5e87490aa19-Step5.jpg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=aee68cf7ac4196c8d45a07a80dece431 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/90a450125f796991010c06beeaed5165987154af57d59036bc52a5e87490aa19-Step5.jpg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=73a28805d8ac64784c0dbb78c9887571 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/90a450125f796991010c06beeaed5165987154af57d59036bc52a5e87490aa19-Step5.jpg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=aa9281ddf47c9f3e5d86a089a5b3084f 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/90a450125f796991010c06beeaed5165987154af57d59036bc52a5e87490aa19-Step5.jpg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=e512855b58b23e6434a6eaa6cee8b5a6 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/90a450125f796991010c06beeaed5165987154af57d59036bc52a5e87490aa19-Step5.jpg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=2ee39c2627f0d34df9b853019e86572a 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/90a450125f796991010c06beeaed5165987154af57d59036bc52a5e87490aa19-Step5.jpg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=c5dd0e643ded5a536324e760343f2ecb 2500w" />
   </Frame>
4. Your new wallet will be successfully added to the IO ecosystem.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/443b974762b2971b3ef5dd39f3d1be0ec66377f96a64487f5b675322f93849f8-step6.jpg?fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=6ecd783627ccb4e3a5c9b51bf18309b6" alt="" className="mx-auto" style={{ width:"90%" }} data-og-width="1786" width="1786" data-og-height="598" height="598" data-path="images/docs/443b974762b2971b3ef5dd39f3d1be0ec66377f96a64487f5b675322f93849f8-step6.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/443b974762b2971b3ef5dd39f3d1be0ec66377f96a64487f5b675322f93849f8-step6.jpg?w=280&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=44b38ea07b38d04f2d34d8564efc861d 280w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/443b974762b2971b3ef5dd39f3d1be0ec66377f96a64487f5b675322f93849f8-step6.jpg?w=560&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=8c49ce866e5a4d41073af5385a0496e0 560w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/443b974762b2971b3ef5dd39f3d1be0ec66377f96a64487f5b675322f93849f8-step6.jpg?w=840&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=d85d540500d35f6ef3b1347a1b8b2037 840w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/443b974762b2971b3ef5dd39f3d1be0ec66377f96a64487f5b675322f93849f8-step6.jpg?w=1100&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=93b6b65e62bee7c171ab786b46adcdc4 1100w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/443b974762b2971b3ef5dd39f3d1be0ec66377f96a64487f5b675322f93849f8-step6.jpg?w=1650&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=70b7ac4efaecf4245ca6a81e57fad674 1650w, https://mintcdn.com/ionet-cca8037f/HFkfFyCkAaAMMbBx/images/docs/443b974762b2971b3ef5dd39f3d1be0ec66377f96a64487f5b675322f93849f8-step6.jpg?w=2500&fit=max&auto=format&n=HFkfFyCkAaAMMbBx&q=85&s=14e27e023de3dbd50afdfbfe329e28cd 2500w" />
   </Frame>

## Primary Wallet Address

By default, your first wallet becomes the primary one. However, if you add more than one wallet, you can set another wallet as the primary. The primary wallet will be used for Block Rewards and payment transactions instead of the old address.

To change your primary wallet, hover your mouse over the desired wallet address and click on the blue star beneath the field. The selected wallet will then become the primary one.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62d593f062a7c7a2ddb9a9fe1777a5dceda1dbe3ea6f734824a6a3eb37ab3ff1-step7.jpg?fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=aed431f8ae4338c307cd9d2a65e8254d" alt="" className="mx-auto" style={{ width:"56%" }} data-og-width="368" width="368" data-og-height="318" height="318" data-path="images/docs/62d593f062a7c7a2ddb9a9fe1777a5dceda1dbe3ea6f734824a6a3eb37ab3ff1-step7.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62d593f062a7c7a2ddb9a9fe1777a5dceda1dbe3ea6f734824a6a3eb37ab3ff1-step7.jpg?w=280&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=240b83dfb6ccec097f98616cceeada7b 280w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62d593f062a7c7a2ddb9a9fe1777a5dceda1dbe3ea6f734824a6a3eb37ab3ff1-step7.jpg?w=560&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=349c4a8f55d462faa0436c26c96c483e 560w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62d593f062a7c7a2ddb9a9fe1777a5dceda1dbe3ea6f734824a6a3eb37ab3ff1-step7.jpg?w=840&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=2d6a61b38b09f2cf6c3258473ddaa802 840w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62d593f062a7c7a2ddb9a9fe1777a5dceda1dbe3ea6f734824a6a3eb37ab3ff1-step7.jpg?w=1100&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=85b0166ca8b5366b391e407bbb73aa8b 1100w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62d593f062a7c7a2ddb9a9fe1777a5dceda1dbe3ea6f734824a6a3eb37ab3ff1-step7.jpg?w=1650&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=3ddb9a068a5593e42e166b77ceb2a05a 1650w, https://mintcdn.com/ionet-cca8037f/b1mYj6ho_VzomCTc/images/docs/62d593f062a7c7a2ddb9a9fe1777a5dceda1dbe3ea6f734824a6a3eb37ab3ff1-step7.jpg?w=2500&fit=max&auto=format&n=b1mYj6ho_VzomCTc&q=85&s=190cc8a52b6063b7a543332adb0f8532 2500w" />
</Frame>

## Removing a Wallet

You can remove any of your wallet addresses at any time. Here’s how:

1. Hover over the wallet address you want to remove.
2. A **red Trash** icon will appear. Click on it to remove the selected wallet.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8843476d7904a13937d80241f93a9391b1460febd47e6d904cc406c7739aed9-step8.jpg?fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=85dc1dae463536ffc423ebd685687231" alt="" className="mx-auto" style={{ width:"56%" }} data-og-width="382" width="382" data-og-height="386" height="386" data-path="images/docs/e8843476d7904a13937d80241f93a9391b1460febd47e6d904cc406c7739aed9-step8.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8843476d7904a13937d80241f93a9391b1460febd47e6d904cc406c7739aed9-step8.jpg?w=280&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=22b3a06fb8064d757b8d592becc51977 280w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8843476d7904a13937d80241f93a9391b1460febd47e6d904cc406c7739aed9-step8.jpg?w=560&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=51955e9a80ebffbc1e97da0ee0cd00b5 560w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8843476d7904a13937d80241f93a9391b1460febd47e6d904cc406c7739aed9-step8.jpg?w=840&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=39adc2f9710e81e0c10fc2fd07054919 840w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8843476d7904a13937d80241f93a9391b1460febd47e6d904cc406c7739aed9-step8.jpg?w=1100&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=705ecfbb798bccaf09950f3716c51ad0 1100w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8843476d7904a13937d80241f93a9391b1460febd47e6d904cc406c7739aed9-step8.jpg?w=1650&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=24443729a4b7d5d11f2886da3fb4aef2 1650w, https://mintcdn.com/ionet-cca8037f/dIsHanY7VlXGrCcR/images/docs/e8843476d7904a13937d80241f93a9391b1460febd47e6d904cc406c7739aed9-step8.jpg?w=2500&fit=max&auto=format&n=dIsHanY7VlXGrCcR&q=85&s=712930675f39d800e32d34349272bffe 2500w" />
   </Frame>
3. A pop-up will appear to double-check your action to ensure you want to remove the wallet.

   <Frame>
     <img src="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0c4ca16603944865b500a341ba4971bb6ad60d8f4a6c41f70d6b72436084f0ea-step9.jpg?fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=6bdd7505219aad18d2d46827d1239a79" alt="" className="mx-auto" style={{ width:"71%" }} data-og-width="1046" width="1046" data-og-height="338" height="338" data-path="images/docs/0c4ca16603944865b500a341ba4971bb6ad60d8f4a6c41f70d6b72436084f0ea-step9.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0c4ca16603944865b500a341ba4971bb6ad60d8f4a6c41f70d6b72436084f0ea-step9.jpg?w=280&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=c3d36e9f51d86e93a506a3f2dd145613 280w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0c4ca16603944865b500a341ba4971bb6ad60d8f4a6c41f70d6b72436084f0ea-step9.jpg?w=560&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=f38a33da5d14da72fadc763f4ade56ef 560w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0c4ca16603944865b500a341ba4971bb6ad60d8f4a6c41f70d6b72436084f0ea-step9.jpg?w=840&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=e85e4f6b40e66c94b80ef2ed40b1dff3 840w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0c4ca16603944865b500a341ba4971bb6ad60d8f4a6c41f70d6b72436084f0ea-step9.jpg?w=1100&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=5a3c5610461e0f0590e1038ae41b05ba 1100w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0c4ca16603944865b500a341ba4971bb6ad60d8f4a6c41f70d6b72436084f0ea-step9.jpg?w=1650&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=f488250770c7820f5956d8c5504c6fc5 1650w, https://mintcdn.com/ionet-cca8037f/TfxJXBgQCsMMTJrc/images/docs/0c4ca16603944865b500a341ba4971bb6ad60d8f4a6c41f70d6b72436084f0ea-step9.jpg?w=2500&fit=max&auto=format&n=TfxJXBgQCsMMTJrc&q=85&s=1d722e4d28d89bd104701ac4e285420c 2500w" />
   </Frame>

<Warning>
  If you remove your wallet from the IO ecosystem, you will no longer receive block rewards, payments, or any other rewards associated with that wallet. Please be sure to remove wallets only when necessary.
</Warning>

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/565f4056259ac991c159ce65423f91f9e55b9098aa8ab3df1e132db28e37da54-step10.jpg?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=3236bae29d0313511bf215f99f9133c8" alt="" className="mx-auto" style={{ width:"65%" }} data-og-width="1040" width="1040" data-og-height="432" height="432" data-path="images/docs/565f4056259ac991c159ce65423f91f9e55b9098aa8ab3df1e132db28e37da54-step10.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/565f4056259ac991c159ce65423f91f9e55b9098aa8ab3df1e132db28e37da54-step10.jpg?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=05b27a6084191177b1a720ca4c976e2c 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/565f4056259ac991c159ce65423f91f9e55b9098aa8ab3df1e132db28e37da54-step10.jpg?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=adf933feee21f6e5c95b44dd9c706815 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/565f4056259ac991c159ce65423f91f9e55b9098aa8ab3df1e132db28e37da54-step10.jpg?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=d40a477c6e3f3a6afad7720ddabf6974 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/565f4056259ac991c159ce65423f91f9e55b9098aa8ab3df1e132db28e37da54-step10.jpg?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=1435439e6278035b1ad4243f3bdefc75 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/565f4056259ac991c159ce65423f91f9e55b9098aa8ab3df1e132db28e37da54-step10.jpg?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=a7e0d9ec670300f5c375b380d6e10cef 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/565f4056259ac991c159ce65423f91f9e55b9098aa8ab3df1e132db28e37da54-step10.jpg?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=15c531f1ce1a0244218f108afb76952c 2500w" />
</Frame>

### Manage funds page

In the upper-right corner of the screen, click **Manage Funds**.

<Frame>
  <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55df45bc6433c20adac959ec1f33cb67eb9e044796f347dcd5970dd78a1ef9fc-Artboard.png?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=e057cdcc2ce729262fb778e4308cefc9" alt="" className="mx-auto" style={{ width:"66%" }} data-og-width="642" width="642" data-og-height="118" height="118" data-path="images/docs/55df45bc6433c20adac959ec1f33cb67eb9e044796f347dcd5970dd78a1ef9fc-Artboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55df45bc6433c20adac959ec1f33cb67eb9e044796f347dcd5970dd78a1ef9fc-Artboard.png?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=5a3b2b94a3e836cf8b5c49de03e27045 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55df45bc6433c20adac959ec1f33cb67eb9e044796f347dcd5970dd78a1ef9fc-Artboard.png?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=6f03f8bd1e2c3f0ea52910aad47dee94 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55df45bc6433c20adac959ec1f33cb67eb9e044796f347dcd5970dd78a1ef9fc-Artboard.png?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=5ccf1d67cdf8035dddc8a36ad8fd66d8 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55df45bc6433c20adac959ec1f33cb67eb9e044796f347dcd5970dd78a1ef9fc-Artboard.png?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=a4ee14c02e71989b0f82f27d0a113f83 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55df45bc6433c20adac959ec1f33cb67eb9e044796f347dcd5970dd78a1ef9fc-Artboard.png?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=951ec4dd754550dd1a5d879b48b58514 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/55df45bc6433c20adac959ec1f33cb67eb9e044796f347dcd5970dd78a1ef9fc-Artboard.png?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=36bb78e76a55cb42b6b5b34153e9bd4f 2500w" />
</Frame>

This will open the **Manage Funds** page, where you can:

* View your lifetime Block Rewards earnings for your Workers.
* View the Block rewards already claimed for your Workers.
* View your current Cloud balance in USDC.
* View your current Cloud balance in \$IO Coin.
* See your **Worker Earnings** and Claim rewards.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5c8c9e575e5fcc54be88cada8a2e1dee21b322214ec3088cd747f86aaecd2dc4-managefunds.png?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=7361d3a6ec40652a8fad30d9dc96b1f6" alt="" data-og-width="1291" width="1291" data-og-height="412" height="412" data-path="images/docs/5c8c9e575e5fcc54be88cada8a2e1dee21b322214ec3088cd747f86aaecd2dc4-managefunds.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5c8c9e575e5fcc54be88cada8a2e1dee21b322214ec3088cd747f86aaecd2dc4-managefunds.png?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=1a5a2cdf00971c6adabac8634754b7a5 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5c8c9e575e5fcc54be88cada8a2e1dee21b322214ec3088cd747f86aaecd2dc4-managefunds.png?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=24e7d267259d4a8a5bfb345944a5d9f5 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5c8c9e575e5fcc54be88cada8a2e1dee21b322214ec3088cd747f86aaecd2dc4-managefunds.png?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=a9c68e2b21b8ba1721980a1aa6b258ff 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5c8c9e575e5fcc54be88cada8a2e1dee21b322214ec3088cd747f86aaecd2dc4-managefunds.png?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=45aa161a2204b673ade44bc92c1714f3 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5c8c9e575e5fcc54be88cada8a2e1dee21b322214ec3088cd747f86aaecd2dc4-managefunds.png?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=d0f38c843886dcb253dd99e38f5daf09 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5c8c9e575e5fcc54be88cada8a2e1dee21b322214ec3088cd747f86aaecd2dc4-managefunds.png?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=68c4eecfb1db03c26ec551fbe0b0dcc2 2500w" />
</Frame>

**List of Transactions**

This section also includes a **List of Transactions.** You can filter transactions by date within any allowed period and by categories such as:

* Reloaded
* Earnings
* Refunded
* Withdrawal
* Promo Credit

Additionally, you can filter transactions by sections in the IO system, such as:

* Worker
* Cloud

Clicking on a specific transaction will open a page with detailed information about it.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b38c14-pic6.jpeg?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=a08935069fdd2927ef50a5194a2bcced" alt="" data-og-width="2582" width="2582" data-og-height="954" height="954" data-path="images/docs/8b38c14-pic6.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b38c14-pic6.jpeg?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=e6f43c7ef4018b710750856dd30682a1 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b38c14-pic6.jpeg?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=56fce676eea609a9e3cd7d454918445d 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b38c14-pic6.jpeg?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=58f30911d353040c74517b98cee3a8f8 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b38c14-pic6.jpeg?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=da6abbfc3cacc8337cb7474df2afd43f 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b38c14-pic6.jpeg?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=48a4871075ca935637328c8ebefa3a0e 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8b38c14-pic6.jpeg?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=f02bae46fd574e891ba5c1dca9921fc5 2500w" />
</Frame>

**View a specific transaction**

The detailed transaction page shows:

* Amount and type of currency received
* Transaction type
* Platform used
* Status
* Date
* Transaction ID
