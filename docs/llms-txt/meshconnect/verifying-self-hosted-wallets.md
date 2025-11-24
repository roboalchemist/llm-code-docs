# Source: https://docs.meshconnect.com/advanced/verifying-self-hosted-wallets.md

# Verifying Self-Hosted Wallets

> Using Mesh Verify for wallet verification

### Background on self-hosted wallet Travel Rule guidelines

Travel Rule regulations have long-existed in traditional financial markets as a way for regulators to enforce laws pertaining to the movement of money (eg. anti-money laundering, terrorist financing, sanctions, etc.). In short, regulated financial institutions are responsible for knowing who they are receiving assets from, and where they’re sending assets to. The crypto world has long-awaited clear Travel Rule guidelines for crypto, and on July 4th the European Banking Authority (EBA) released their final guidelines. Other global regulatory regimes are likely to follow soon as well. This guide dives into detail around Mesh’s support for verifying ownership of a self-hosted wallet.

### How does wallet verification work?

The nature of self-hosted wallets is that they don’t know who the user is. In other words, a user doesn’t KYC with MetaMask like they would with Coinbase or another centralized exchange. So verifying ownership of a self-hosted wallet is not about receiving user information from that wallet. Instead, it is about confirming that the user you know is in control of the wallet in question. Additionally, verification pertains to an address (ie. 0x31…cF98), not a wallet app (ie. MetaMask). Keep in mind that a user can interact with the same wallet (ie. address) from multiple wallet apps, and can also interact with multiple wallets from within the same wallet app.

The EBA specifies that one acceptable method of verifying ownership of a self-hosted wallet is having the user sign a self-attestation of ownership (ie. a message) in that wallet. The message doesn’t have to be anything specific, but the message the user signs must be the exact message requested by you. A message signature is an off-chain event (ie. it’s completely gasless), but is also fully verifiable with the combination of the signedMessageHash, the address, and message.

### Invoking wallet verification in Mesh Link

* Wallet verification can be completely independent of a transfer (ie. the user only connects their wallet and signs the message), or can be used in combination with a transfer (ie. the user connects their wallet, signs a message, and then continues to the transfer).
* In the request to `/api/v1/linktoken` to invoke the Mesh Link modal, there is a parameter called `verifyWalletOptions`. To have the user sign a message, you must:
  1. Select a `verificationMethods` (as of now the only option is `signedMessage`). We may also have other options in the future.
  2. Add a `message`. We recommend keeping this short. Do not include any PII in this message (ie. do not include a user name). If this is left blank, a generic message will be added.
* This will only impact the user experience for self-hosted wallets (ie. MetaMask, Trust Wallet, etc.). This will not change anything about the experience for centralized exchanges (ie. Binance, Coinbase, etc.).
* After connecting their wallet, the user will then be prompted to sign a message. As with connection requests and transfer requests, the user will not have to configure anything manually. Mesh will send the signature request, with the message, to the wallet app, and will open the wallet app on the user’s screen. All the user has to do is review it and sign it.

### What you’ll receive back from Mesh after a successful signature

After the user signs the message in their wallet, you will receive the SDK event: `walletMessageSigned` back from Mesh with the following payload:

* `signedMessageHash`
* `message`
* `address`
* `timeStamp`
* `isVerified` (boolean)

This data can be stored on your side for audit purposes, as well as to improve the return user experience within your UX.

**NOTE**: this is the only time that the `signedMessageHash` data will be provided, Mesh does not retain this data.
