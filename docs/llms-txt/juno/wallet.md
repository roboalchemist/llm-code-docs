# Source: https://juno.build/docs/miscellaneous/wallet.md

# Wallet

This section provides guidance on managing your assets and cycles with your [wallet](/docs/terminology.md#wallet), which are essential for maintaining and providing enough resources for your modules in the Juno ecosystem.

**Important:**

Just like your modules, your wallet is fully under your control â Juno cannot access, move, or recover the ICP or cycles held inside.

Because of this non-custodial model, there are no refunds, reversals, or recovery options. Always double-check destination addresses before sending funds.

As a best practice, we recommend not holding large amounts of ICP in your Juno wallet unless necessary. Use it as a utility wallet for fueling your modules â not as a long-term vault.

We also recommend enabling [monitoring](/docs/management/monitoring.md) to ensure your Mission Control stays alive and responsive at all times.

---

## What are ICP?

ICP are the native cryptocurrency of the [Internet Computer](https://internetcomputer.org). They provide utility for powering the network and are also used for governance.

One key usage is converting ICP tokens to cycles, which are used to cover the computational and storage costs of running modules.

---

## Why do I need ICP?

Given that Juno is built on top of the Internet Computer (see [architecture](/docs/miscellaneous/architecture.md)), your modules require cycles to stay alive.

While you donât necessarily need ICP in the Juno ecosystem since you can acquire cycles with Stripe through [cycle.express](https://cycle.express), having some ICP can still be interesting.

It provides independence by allowing you to top up your modules without relying on third-party services. Depending on how you obtain your tokens, using ICP can also help lower transaction costs and offers interoperability with other Internet Computer projects, making it a flexible and practical option.

---

## Buying ICP

To get ICP from the outside world into your wallet, you can use most cryptocurrency exchange platforms that allow you to buy ICP (refer to this [list](https://coinranking.com/fr/coin/aMNLwaUbY+internetcomputerdfinity-icp/exchanges) of major ones). These platforms let you convert dollars (or other currencies) into ICP. Keep in mind that exchanges charge a fee for this service.

Once you have obtained ICP on those platforms, you can initiate a transaction to send it to your wallet. For this purpose, you will need to provide a destination address where the ICP should be sent. This destination address corresponds to the [Account Identifier](/docs/terminology.md#account-identifier) of your wallet.

You can locate the destination address in Juno's [console](https://console.juno.build). Once you've logged in, go to your [wallet](https://console.juno.build/wallet) and click "Receive".

![A screenshot of the wallet with the &quot;Receive&quot; button](/assets/images/wallet-receive-dbb873738cb48ce074e1201c3fff535f.png)

Select "Account identifier".

![A screenshot of the wallet &quot;Receive&quot; modal with an arrow pointing to the Account Identifier option](/assets/images/wallet-receive-account-identifier-e320146e191bcf52d00d22238a92bb4b.png)

Either copy your account identifier or use the provided QR code. This is the address you should use to receive ICP from the outside world.

![A screenshot of the Account Identifier and QR code](/assets/images/wallet-receive-account-identifier-qrcode-ea0f266be5c83547e4843d4a4b5a7a4b.png)

---

## Receiving ICP

If you already hold ICP, you can transfer it from wallets within the ecosystem such as the [NNS dapp](https://nns.internetcomputer.org/), [OISY](https://oisy.com) or [others](https://internetcomputer.org/ecosystem?tag=Wallet).

To initiate a transaction to send it to your wallet, you will need to provide a destination address, which in this case is your wallet ID.

You can locate your wallet ID in Juno's [console](https://console.juno.build). Once you've logged in, go to your [wallet](https://console.juno.build/wallet), where the information is easy to find.

![A screenshot of the wallet with &quot;Wallet ID&quot; information](/assets/images/wallet-id-a806ae0c58411c9129c604868d98f7b0.png)

If you wish to use a QR code, click "Receive" and select "Wallet ID".

![A screenshot of the wallet &quot;Receive&quot; modal with an arrow pointing to the Wallet ID option](/assets/images/wallet-receive-wallet-id-da09f22b7fe82d18b42836c013d451cd.png)

Either copy your account identifier or use the provided QR code. This is the address you should use to transfer ICP within the ecosystem.

![A screenshot of the Wallet ID and QR code](/assets/images/wallet-receive-wallet-id-qrcode-de9cc6b8681da618c8758a364fb18d05.png)

If you are using OISY, you can also connect this third-party wallet to Juno's console to initiate the transaction and proceed with the approval. This eliminates the need to copy, paste, or scan any addresses.

![A screenshot of the wallet &quot;Receive&quot; modal with an arrow pointing to the OISY option](/assets/images/wallet-receive-oisy-a6dabf8ca3d87e45da773c58f8a0eda3.png)

---

## Send ICP

Sending ICP to the ecosystem or the outside world can be initiated from your wallet in Juno's [console](https://console.juno.build). To start a transaction, click "Send".

![A screenshot of the wallet with the &quot;Send&quot; button](/assets/images/wallet-send-09f0b1267286be0ebb67a985e432deb8.png)

Enter the destination wallet ID or account identifier where you want to send ICP, along with the amount.

![A screenshot of the wallet send form](/assets/images/wallet-send-form-03440e3f0718c16c0b08a70cfa18d0ee.png)

Review the transaction details and confirm to execute it.

![A screenshot of the wallet send review mask](/assets/images/wallet-send-review-52b726f5d9cc0977a04dba319dfa1ec3.png)