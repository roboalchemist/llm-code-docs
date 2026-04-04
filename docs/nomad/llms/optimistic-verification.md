# Source: https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification.md

# Optimistic Verification

Given the complexity of native verification and risks of external verification, Nomad offers a third way — **Optimistic Verification**.

![Source: Optimistic Bridges, A New Paradigm for Crosschain Communication](https://miro.medium.com/max/1400/1*j36ZAhVvVQGRBIOhPrlrAQ.png)

Optimistically verified systems like Nomad are slightly weaker in security than natively verified systems, but simpler, more cost-efficient, and easier to deploy / reuse.&#x20;

Conversely, optimistic systems are naturally more complex than a multi-sig and most other externally verified systems, but are more trust-minimized and offer greater security.

### How It Works

Optimistic verification doesn't use light clients and natively verify cross-chain messages. Instead, messages are *optimistically* signed on the origin chain, and a timeout period is enforced on the destination, during which the message can be inspected and vetoed if anything awry is noticed.

The key is that this design introduces a new set of actors, called [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers) in Nomad, who are responsible for maintaining liveness and flagging fraud on-chain if detected. Nomad is only safe if there is *at least* one honest Watcher is observing the system and flagging fraud.

In other words, rather than pessimistically assuming that we need to verify each message natively, Nomad relies on local verification by participants, with the opportunity to flag it in the system. This tradeoff allows Nomad to save significantly on gas fees compared to pessimistic relays, while still maintaining a high degree of security.

To learn more about how fraud is handled in Nomad, [read more here](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud).

## The Trade-Offs

### Latency

The main trade-off with this design is mild latency — optimistic systems sacrifice speed in order to allow for a timeout period where fraudulent messages can be challenged. This is the nature of all optimistic designs, but in cross-chain interoperability, this window can be much lower than with optimistic rollups (ie. 30 minutes rather than 7 days).

All interoperability protocols are asynchronous by nature, and will experience latency from:

* Chain finality rules (eg. waiting 20 block confirmations for Ethereum's probabilistic finality)&#x20;
* Off-chain agent operations (messages may be batched to reduce cost)

Optimistic systems simply add a third reason for latency, which is the optimistic timeout period. Nomad's design acknowledges that no interoperability protocol will be instantaneous, and a mild additional latency is a small price to pay for vastly greater security.

Read more about Nomad's [optimistic-timeout-period](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period "mention").
