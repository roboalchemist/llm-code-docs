# Source: https://docs.nomad.xyz/the-nomad-protocol/security/attack-vectors/economic-attacks.md

# Economic Attacks

Unlike key compromise attacks, which hijack the root-of-trust verification mechanism by stealing keys, economic attacks leverage the built-in mechanics of the system to corrupt messages.

The best example of an economic attack in crypto is the [51% attack](https://en.wikipedia.org/wiki/Double-spending#51%_attack), which has happened multiple times already, particularly [in the context of Ethereum Classic](https://www.coindesk.com/markets/2020/08/29/ethereum-classic-hit-by-third-51-attack-in-a-month/). While this example is only applicable to Proof of Work chains, the fundamental concept of one logical actor acquiring enough resources to Sybil attack a system is relevant to all crypto-economic systems.

## How They Work

Economic attacks are highly variable as they are influenced by the design of the systems they target. There are many kinds of economic attacks, including:

* **51% attacks** — this can be generalized to cover attacks where the adversary purchases enough of the underlying resource (hashpower in PoW or cryptoasset in PoS) in a blockchain network to gain control of block production. Note that while this can at worst lead to double spends of&#x20;
* **Oracle attacks** — if the system uses an oracle for price feeds or other economic information, attackers can compromise the oracle or exploit its mechanism to adjust spot prices for their benefit.&#x20;
  * An example is [the Compound oracle exploit](https://decrypt.co/49657/oracle-exploit-sees-100-million-liquidated-on-compound) where the DAI spot price on Coinbase was manipulated to $1.30, which the Coinbase Oracle fed to Compound as the canonical price. This led to a cascade of liquidations on Compound, despite the market price across other exchanges showing DAI much closer to its peg of $1.
* **Governance attacks** — if the system uses a governance token for making core decisions about the protocol, then attackers may be able to purchase enough of the token required to reach quorum within a governance process. Like any plutocratic system, wealth will continue to beget wealth.&#x20;
  * An example is [the Beanstalk governance exploit](https://blockworks.co/algo-stablecoin-protocol-beanstalk-cut-down-by-governance-hijack/) where an attacker used a flash loan to game a poorly designed governance system, giving them control of all of the protocol's assets. Proper governance mechanism design must take into account not only flash loans, but other means by which attackers can acquire a significant amount of the governance asset and corrupt the system.

### Validator-based Interoperability Protocols

The economic attacks and examples covered above are meant to illustrate the wide ranging nature of potential vectors an attacker can use. However, in interoperability, one particularly important case to consider is economic attacks on validator or Proof of Stake based interoperability protocols.&#x20;

Validator-based bridges seek to increase the number of [external verifiers](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification) by introducing a token to coordinate them. In other words, validator-based protocols use token voting via Proof of Stake to *elect* a multisig for a given period of time (often called epochs).

The benefits of these systems include:

* More external parties can verify cross-chain messages (ie. \~100 in Tendermint consensus) thereby decreasing risk of collusion and increasing liveness guarantees
* The elected multi-sig is dynamic, meaning that new verifiers may join by acquiring the token
* Malicious / negligent verifiers may be punished via social slashing

However, these benefits come with significant downsides — namely, being able to join the verifier set by purchasing the staking token. An adversary just needs to purchase enough of the staking token to reach quorum within the validator set, after which they can corrupt cross-chain messages, purely by playing within the rules of the system. In other words, bribery is enshrined on-chain by using Proof of Stake.

**The key invariant here is that the value of assets needed to take over block production must&#x20;*****always*****&#x20;exceed the amount secured by the protocol.** Otherwise, an attacker can profit by purchasing the asset and corrupting the system, even if they are slashed in totality.

Though these attacks have not happened yet, as Proof of Stake based interoperability systems grow, attackers will begin to explore these vectors. All it takes is one dislocation similar to the Compound oracle exploit for an economic attack against these systems to be insanely profitable.

## Defense

The best defense against an economic attack is to avoid relying on crypto-economics for core mechanisms. In other words, if your system does not need to rely on a token, it's probably best to avoid introducing one.

![Can't buy 2/3 of the validator set, if you don't use Proof of Stake](https://memegenerator.net/img/images/16782779.jpg)

Unfortunately, not all systems can avoid economic mechanisms altogether, so it's best to keep surface area minimal and introduce economics only where absolutely needed to strengthen other aspects of the protocol.

### Nomad's Economic Design

In Nomad's case, there is no staking token that an attacker can purchase to corrupt cross-chain messages. Period.&#x20;

However, Nomad is following a progressively decentralization model that will require the introduction of economics such as:

* Bonding the Updater to enable slashing upon misbehavior
* Introducing fees or incentives for Watcher liveness (currently Watchers are run by the Nomad team, and external parties that are incentive aligned without on-chain fees)
* Having Relayers compete in a fee market to enable greater liveness fault tolerance

With each of these points, there will be considerations around economic design that Nomad will consider to ensure a robust defense against economic attacks.

#### Updater Bond

Nomad will require that Updaters post a bond before enrolled. This bond will be subject to slashign conditions such as downtime and signing fraudulent updates.

The most common questions around this parameter are:

* "How high does the Updater bond need to be?"
* "Does it have to be greater than the value secured by the protocol?"

The answers are:

* "High enough to deter an Updater from *trying* to commit fraud"
* "No!"

The key reason the value bonded can be lower than what's at stake is because Nomad ensures that fraud is preventable. This means that unlike validator-based systems where fraud will *always* go through, Nomad will *never* let fraud go through (observing a 1-of-N live Watcher assumption).&#x20;

Thus, while validator systems require bonds greater than the value secured to act as punishment, Nomad just needs the bond to be high enough to deter adversarial behavior. Put more simply — if I know that I will almost certainly lose 5 ETH for even trying to commit fraud, I won't even bother.

#### Watcher Liveness Incentives

Initially, we anticipate enrolling Watcher operators that are mission and incentive aligned, and are willing to operate these nodes without receiving on-chain incentives. However, Watchers do cost money to run, given they are off-chain nodes, and we anticipate having in protocol economics for external agent operators.

There are no concrete designs yet, but we anticipate needing to incentivize liveness to avoid free rider problems. Ie. We need all Watchers to maintain liveness even when there isn't fraud, and avoid passing the buck to other Watchers in the system. We will update this section when we have a more concrete design.
