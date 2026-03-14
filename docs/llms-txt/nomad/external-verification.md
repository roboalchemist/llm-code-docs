# Source: https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/external-verification.md

# External Verification

[Natively verified systems](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/native-verification) have not gained traction because of their aforementioned challenges, namely engineering complexity, low reusability, and high operational costs.

However, **externally verified** constructions *have* proliferated given the market need for interoperability. Unlike light client relays, externally verified systems are easy to develop, highly reusable, and quite cheap / easily subsidized.

![Source: The Interoperability Trilemma](https://miro.medium.com/max/1400/1*rKVPhxnuGmpxNeLjQqmT3g.png)

Examples of externally verified systems include custodians, multi-sig addresses, validator / proof-of-stake (PoS) systems, and oracle networks. All fundamentally work the same way — they introduce an external verifier or set of verifiers who must collectively sign cross-chain messages beyond some threshold to be deemed valid on the destination chain.

Oftentimes, externally verified systems will use more complex language like MPC or TSS. Their meaning is simple:

* **MPC (Multi-party Computation)** — there are multiple signers who are responsible for verifying cross-chain messages. Essentially a multi-sig wallet address.
* **TSS (Threshold Signature Scheme)** — the multi-sig signers must reach some quorum or threshold to verify messages. Examples include Synapse (3-of-5) or Wormhole (13-of-19).

The drawback to external verification is that while it is expedient, it outsources security to third parties (ie. folks other than the validators of the two chains). If these validators' collective security is weaker than the underlying chains they bridge, then they become the weakest link in the system.
