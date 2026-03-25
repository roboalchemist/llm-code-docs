# Source: https://docs.meson.fi/protocol/background/htlc.md

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
