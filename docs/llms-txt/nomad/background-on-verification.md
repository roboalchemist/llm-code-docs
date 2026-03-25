# Source: https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/background-on-verification.md

# Background on Verification

### Verifying Cross-chain Communication

Cross-chain communication at its core is the act of synchronizing two independent blockchain networks:

* A user makes a state change on Chain A, the origin chain. This involves the submission of a transaction on-chain, which the validator set of Chain A confirms by including it in a block.&#x20;
* Once finalized, this state change must be ***verified*** by one or more off-chain actors, ie. Verifiers, who apply their signature over the state.
* Once verified, any party may relay this signed commitment to the destination chain, Chain B, by sending a transaction on-chain, which the validator set of Chain B includes in a block and confirms.
* Finally, the state from Chain A can be acted upon within Chain B, **provided that the Verifier(s) behaved honestly.**

The critical caveat is that cross-chain communication is *impossible* without a trusted third party (TTP) (formalized as an impossibility result in [this paper by Zamyatin et al](https://eprint.iacr.org/2019/1128.pdf)).&#x20;

Every cross-chain messaging system must rely on some *verifier* set to act as the TTP, and ensure that messages being sent to a destination chain reflects the correct state on the sending chain.

### Root of Trust Insecurity

This is why we consider the verification mechanism the **root of trust (RoT)** within cross-chain communication systems. If the RoT fails, the entire protocol (regardless of any other features) is vulnerable to safety failures. As such, the bulk of the work and scrutiny in any interoperability protocol must be on the verification mechanism used.

However, as we've seen from recent hacks, the majority of cross-chain messaging systems are insecure because the root-of-trust relies on a few centralized parties. For example, [the Ronin Bridge hack resulted from the compromise of 5 validator keys](https://roninblockchain.substack.com/p/community-alert-ronin-validators?s=w), in a 5-of-9 multi-signature address which served as the verifier set.

In the following sections, we'll explore the different mechanisms used for verifying cross-chain messages and the various trade-offs each makes with regards to security, extensibility, and generalizability.
