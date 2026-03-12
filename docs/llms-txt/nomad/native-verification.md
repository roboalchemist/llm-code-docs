# Source: https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/native-verification.md

# Native Verification

If every cross-chain communication method requires some TTP to provide verification, then the most trust-minimized method is **native verification**.

![Source: The Interoperability Trilemma](https://miro.medium.com/max/1400/1*m2RHMo8aAwu4rJRBvNpSKg.png)

Natively verified constructions leverage the underlying validator (or miner) sets of the two chains communicating to verify cross-chain messages. This way, there is no external verifier set introduced, and the security of the bridge reflects trust assumptions users have *already* made by using the two chains in the first place.

Put in other words, if you don't trust the validators sets of the two chains you are sending messages between, then you shouldn't be bridging between them at all!

### How It Works

Native verification is performed by running a light client of the sending chain, encoded as a smart contract, on the destination chain. As long as the sending chain's validator set is honest, the light client state can be used as the source of truth on the destination. Deployed in both directions, this creates a trust-minimized bidirectional channel.

These systems are called *light client relays*, and examples include IBC, TBTC, and Near's Rainbow Bridge (in the Ethereum --> Near direction).

![Source: How Bridges Can Be the Next Big Risk in Crypto](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F61fe08bb-d1d7-45e4-a1ac-566075d2736d_1114x496.png)

The downside of light client relays includes:

* **Difficulty of implementation and maintenance:** \
  Relays need to enshrine logic on-chain, which requires efficient design and implementation of light client logic as smart contracts. If precompiles and curves associated with the sending chain's consensus mechanism aren't available, they need to be lobbied for and added locally in order to reduce gas costs of operation. Finally, any hard fork or change in consensus needs to be reflected in light clients, requiring on-going maintenance.
* **Lack of extensibility / reusability:**\
  As described above, light clients are coupled to the consensus of their underlying chain. This means that a light client contract implemented for Avalanche cannot be repurposed for Polygon or another EVM chain, since their consensus mechanisms are different. This means that each heterogeneous communication channel requires bespoke implementation and effort, reducing the ability of the system to scale and be reused across many environments.
* **Cost of operation:**\
  In order to provide correct state, light clients need to have block or epoch headers constantly provided such that they do not become stale. For proof-of-work, this involves submitting block headers in order on-chain. For proof-of-stake, this involves submitting epoch headers with validator addresses/signatures without breaking synchrony. These gas costs for operation must be borne by someone.&#x20;

Given these factors, light client relays / natively verified systems have not gained much adoption, excepting Cosmos, which has made a concerted effort over many years, subsidized IBC, and maintained homogeneity of Layer 1 environments.
