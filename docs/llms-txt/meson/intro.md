# Source: https://docs.meson.fi/intro.md

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
