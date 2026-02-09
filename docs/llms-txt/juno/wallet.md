# Source: https://juno.build/docs/miscellaneous/wallet.md

# Wallet

This section provides guidance on managing your cycles with your wallet (your account), which are essential for maintaining and providing enough resources for your modules in the Juno ecosystem.

**Important:**

Just like your modules, your wallet is under your control â Juno cannot access, move, or recover the cycles held inside.

Because of this model, there are no refunds, reversals, or recovery options. Always double-check destination addresses before sending funds.

As a best practice, we recommend not holding large amounts of cycles unless necessary. Use it as a utility for fueling your modules â not as a long-term vault.

We also recommend enabling [monitoring](/docs/management/monitoring.md) to ensure your projects and analytics stay alive and responsive at all times.

---

## What are Cycles?

Cycles are used to pay for infrastructure usage. Your Satellite, Mission Control or Orbiter consume cycles while they are active.

The amount of cycles available determines whether a module will be active, inactive, or eventually decommissioned (deleted).

This ensures that related costs cannot surpass the amount of cycles available.

Think of cycles like prepaid mobile data:

*   Just like your mobile plan allows you to make calls and browse the internet, cycles enable your containers to process computations and store data.
*   When your data (cycles) runs out, your service becomes inactive.
*   To keep your modules running smoothly, you need to top up your cycles regularly (manually or automatically).
*   If you donât top it up, after some time, it will be decommissioned, similar to losing your prepaid number due to prolonged inactivity.

---

## Buying Cycles

The easiest way to purchase cycles â and get the best deal â is through [Cycle.express](https://cycle.express), which lets you pay with a credit card via Stripe.

The service is integrated directly into the Juno Console. From your wallet, click "Buy" and follow the steps.

**Note:**

The default purchase amount is $1 USD. You can change this amount on Stripe's payment page (maximum $100).

![A screenshot of where to find the call to action Buy](/assets/images/wallet-buy-fddf8fcc9927dd1923600a7e2283aeef.png)

---

## Receiving Cycles

If you already hold cycles or want to swap some, you can use the [OISY Wallet](https://oisy.com).

To initiate a transaction manually, you will need to provide a destination address. To find it in the [console](https://console.juno.build), open the shortcut to your [wallet](https://console.juno.build/wallet) and click "Receive" select "Wallet ID".

![A screenshot of where to find the call to action Receive](/assets/images/wallet-receive-78153f6bf10b0507baf66fb0d01fec5d.png)

![A screenshot of where to find the link to the Wallet ID](/assets/images/wallet-receive-wallet-id-b4f97e0e100bf750a8a962309f6d05df.png)

You can also connect OISY to Juno's console to initiate the transaction and proceed with the approval. This eliminates the need to copy, paste, or scan any addresses.

![A screenshot of the wallet &quot;Receive&quot; modal with an arrow pointing to the OISY option](/assets/images/wallet-receive-oisy-a48815e1d68d20fc10c13548b53fbc69.png)

---

## Send Cycles

Sending Cycles to the ecosystem or the outside world can be initiated from your wallet in Juno's [console](https://console.juno.build). To start a transaction, click "Send".

**Important:**

Sending cycles transfers them to another wallet. To add manually cycles (resources) to your modules (Satellites, Orbiters, or Mission Control), use the **Top-up** feature instead.

![A screenshot of the wallet with the &quot;Send&quot; button](/assets/images/wallet-send-966cfbae083d2287efaa23ad4a754177.png)

Enter the destination wallet ID or account identifier where you want to send cycles, along with the amount.

![A screenshot of the wallet send form](/assets/images/wallet-send-form-53bc9d2aa33d85a71542462d52464313.png)

Review the transaction details and confirm to execute it.

![A screenshot of the wallet send review mask](/assets/images/wallet-send-review-0d7e6b1fac55e36bdf0fe94f47dea223.png)

---

## ICP

For convenience, the developer wallet can hold ICP tokens as well. When its balance is greater than zero, a conversion feature lets you easily convert them to cycles.

You can also receive and send ICP for backwards compatibility with Mission Control.

Cycles remain the recommended approach for all operations.