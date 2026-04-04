# Source: https://docs.meshconnect.com/advanced/best-ux-practices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best UX Practices & Examples

Mesh provides a faster, safer, and more reliable way for users to move funds from exchanges and wallets directly into your platform. By replacing error-prone QR codes and manual address entry with a seamless, embedded flow, you can significantly increase conversion and user satisfaction.

**Key Advantages:**

* **Fast and Easy:** One-click payments and deposits from Binance, Coinbase, MetaMask, and 300+ other sources.
* **Error-Free:** Prevents wrong addresses, wrong networks, and address poisoning scams.
* **Higher Conversion:** Reduces user drop-off compared to manual flows.
* **Customer-Friendly:** A familiar, secure connection process, similar to linking an account with Plaid or PayPal.

***

### **Placement Best Practices**

How you present the Mesh option in your UI is critical for adoption.

* **Prioritize the Embedded Flow:** Place the "Pay with Crypto" or "Deposit with Crypto" button prominently in your checkout or wallet UI, above any manual QR code options.
* **Use QR Codes as a Backup:** Maintain the manual/QR code option as a secondary choice for users who prefer it.
* **Use Action-Oriented Labels:** Highlight Mesh as the recommended option with labels like **Smart Pay**, **Easy Deposit**, or **Instant Transfer**.
* **Lead with Trusted Brands:** Instead of "Pay with Mesh," use the logos of top exchanges and wallets your users trust, like Binance, Coinbase, and MetaMask.

***

### **The User Journey: A Phased Approach**

The goal is to move users from a simple first-time setup to a frictionless, one-click experience.

#### **1. First-Time User Experience (Smart Pay / Smart Deposit)**

For a new user connecting an account, the flow is simple and builds trust.

* The user selects "Pay with Crypto" or "Deposit from Exchange/Wallet."
* Mesh securely authenticates their account once.
* The user chooses an asset, previews the transaction, and confirms.

This is equivalent to adding a card to Apple Pay: a small, one-time setup that unlocks a seamless experience for all future use.

**📸 Example (Payment Use Case): A "Pay with Crypto" button in a checkout flow.**

<img src="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/payWithCrypto.png?fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=77a14df54358491c86a526f135859cec" alt="Pay With Crypto Pn" title="Pay With Crypto Pn" className="mx-auto" style={{ width:"49%" }} data-og-width="686" width="686" data-og-height="472" height="472" data-path="images/payWithCrypto.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/payWithCrypto.png?w=280&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=a18420a5b9b9dfec4b187a17f5501ca0 280w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/payWithCrypto.png?w=560&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=2276b1fb856b1ed1a03973963e7d7048 560w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/payWithCrypto.png?w=840&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=8915c6d0a2f99ea2a3bd748a33c5c90e 840w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/payWithCrypto.png?w=1100&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=ab75c3c92124933017e191d8808ed180 1100w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/payWithCrypto.png?w=1650&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=accd4a5936a418e5427a1acc4d9447e4 1650w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/payWithCrypto.png?w=2500&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=7b21aec6f6a6480a09bf4f44cf247fdc 2500w" />

**📸 Example (Deposit Use Case): "Deposit from Wallet" with trusted brand options.**

<img src="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet.png?fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=dab7410af5f2862ce0bacc1a2769b9af" alt="deposit" className="mx-auto" style={{ width:"57%" }} data-og-width="550" width="550" data-og-height="220" height="220" data-path="images/depositFromWallet.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet.png?w=280&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=b04a4d86857034bd782bbb6f3d51eaf4 280w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet.png?w=560&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=67c23384587ad445a938cf72784bb1fa 560w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet.png?w=840&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=40ec212a1d3f490824f287cb48c9525e 840w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet.png?w=1100&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=9e9cd470f4386664b5885c76660d7140 1100w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet.png?w=1650&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=ec3814a43e07b5e9ec07a9d671399822 1650w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet.png?w=2500&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=68c7d8f708bb599fb5116b3917c5d9a3 2500w" />

<img src="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet1.png?fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=de9a08a7529814fb0d803455e8b09794" alt="deposit1" className="mx-auto" style={{ width:"39%" }} data-og-width="264" width="264" data-og-height="512" height="512" data-path="images/depositFromWallet1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet1.png?w=280&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=e0d07b3b8319c4089e86e0d479694c18 280w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet1.png?w=560&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=29bb9946dc9a1bec8161bf88ef490310 560w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet1.png?w=840&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=7eaf179c2db5cc4593caf117621f8ce9 840w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet1.png?w=1100&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=1a2c74090fa8b40acb3db51ef0d6765c 1100w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet1.png?w=1650&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=d3275744aaba75ced292313c2e4a91b1 1650w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet1.png?w=2500&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=dad4e7a4f6aef3bb5300f9744faf9f06 2500w" />

<img src="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet2.png?fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=d5ccd33c9108765f4474093324de3046" alt="deposit2" className="mx-auto" style={{ width:"51%" }} data-og-width="512" width="512" data-og-height="387" height="387" data-path="images/depositFromWallet2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet2.png?w=280&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=2ec82c14b24f331f0d8e35c496e11e6e 280w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet2.png?w=560&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=f923781fdfcf5a70f893b789de487e2d 560w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet2.png?w=840&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=23fcb76ec7b7bc9196ff2b78c118c2c4 840w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet2.png?w=1100&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=2df45038fd6571b03055290fcf562a67 1100w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet2.png?w=1650&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=33ea988fd61f0a0042aea88ac965c3ed 1650w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/depositFromWallet2.png?w=2500&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=2065ae44244b7c9b9d5b076c198d96e6 2500w" />

#### **2. Returning User Experience (Easy Pay / Easy Deposit)**

This is where the power of Mesh becomes clear. Once an account is connected, returning users get a one-click experience.

* You use the stored `auth_token` to initialize Mesh.
* The user is taken **directly to the confirmation screen**, skipping the login steps.
* You can create dedicated, personalized buttons like **"Pay with your Binance account"** or **"Deposit from MetaMask."**

**📸 Example: A personalized deposit button for a return user.**

<img src="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/ReturnUser.png?fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=ee2049e740120d2d2f3811dacb64f899" alt="returnUserDeposit" className="mx-auto" style={{ width:"56%" }} data-og-width="512" width="512" data-og-height="262" height="262" data-path="images/ReturnUser.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/ReturnUser.png?w=280&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=03d56bc4584ff77ec8ded4a26079c2cc 280w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/ReturnUser.png?w=560&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=d0d9b900da6013e927eb45456b4aa959 560w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/ReturnUser.png?w=840&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=816b59135e9931472e0bafe20bae7f5d 840w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/ReturnUser.png?w=1100&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=4714a7233d66286e0622a53ca64cd1d4 1100w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/ReturnUser.png?w=1650&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=648436c2bdb4911005b64abc70e4792c 1650w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/images/ReturnUser.png?w=2500&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=34b4b65e0c4d6bc6ceb13b18464f7bfd 2500w" />

#### **3. Power User Experience (Fast Pay / Fast Deposit)**

For frequent users, you can create an even faster flow by pre-selecting the token and network.

* The `linkToken` is configured with a single, pre-defined asset.
* The user is taken directly into the transfer flow, bypassing all selection steps.
* This is ideal for high-frequency use cases like iGaming platforms.

<img src="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/FastDeposit.png?fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=2b505d4690667464fa5e651fb43d814d" alt="FastDeposit" title="" style={{ width:"96%" }} data-og-width="1064" width="1064" data-og-height="252" height="252" data-path="FastDeposit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/FastDeposit.png?w=280&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=ee7b9cafbacd19728c592d9068134ee4 280w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/FastDeposit.png?w=560&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=769d2fe29632dc578948075bedd6d28a 560w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/FastDeposit.png?w=840&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=6f5162c7da63469e88819479ea8d1d49 840w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/FastDeposit.png?w=1100&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=1bded0d2d2d6cb030771d80630747d5c 1100w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/FastDeposit.png?w=1650&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=60138966a3150dc6f3e6a789f9e9bc5c 1650w, https://mintcdn.com/mesh-40/Zg_aIClCeM2bFVIx/FastDeposit.png?w=2500&fit=max&auto=format&n=Zg_aIClCeM2bFVIx&q=85&s=88f264934aac6f68e9878ab572f1c24b 2500w" />

***

### **Key Feature for Payments: SmartFunding**

For all use cases, enabling SmartFunding is the most effective way to maximize conversion.

* **What it is:** SmartFunding allows users to complete a payment even if they don't have enough of the required token by **auto-converting** their other assets in the background.
* **Why it's critical for payments:** It prevents transaction failures due to insufficient funds of a specific asset, turning a potential "failed payment" into a successful one.

***

### **Technical Integration Tips**

* **Token Management:** Always store and refresh the user's `auth_token` to enable the "Easy Pay/Deposit" return user experience.
* \*\*Use \*\*`integrationId`**s:** Deep-link directly to specific providers (e.g., Binance, Coinbase) to create shortcuts in your UI.
* **Support Multi-Asset Arrays:** In your `linkToken` request, pass an array of all the tokens/networks you support to give users maximum flexibility.

***

### **Business Impact**

By adopting this UX strategy, our partners see measurable improvements:

* **Higher Conversion Rates (20-30% lift):** Users complete payments and deposits more often.
* **Increased Volume:** Faster flows encourage more frequent and larger transactions.
* **Reduced Support Tickets:** Eliminates user errors like sending to the wrong address or network.
* **Stronger Retention (2-6x repeat conversions):** Account-linked flows keep users engaged on your platform.
