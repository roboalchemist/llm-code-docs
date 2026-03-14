# Source: https://docs.nomad.xyz/governance-bridge/overview.md

# Source: https://docs.nomad.xyz/token-bridge/overview.md

# Source: https://docs.nomad.xyz/the-nomad-protocol/overview.md

# Overview

Nomad is an interoperability protocol for sending arbitrary messages between blockchains.

In the same way [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) was built to facilitate *reliable* packet-routing in traditional IP networking, Nomad enables applications to transmit data to each other across various blockchains.&#x20;

Analogous to how the application layer in [the Internet protocol](https://en.wikipedia.org/wiki/Internet_protocol_suite) treats the transport layer as a black-box, Nomad developers can deploy cross-chain applications (xApps) without needing to know how the cross-chain transport layer works.&#x20;

Developers only need to implement [send and receive functions](https://docs.nomad.xyz/developers) and Nomad will securely deliver messages between chains.

## Architecture&#x20;

As described above, Nomad separates the transport and application layers so that application developers do not have to reason about the guts of cross-chain communications.

To that extent, when we describe the Nomad protocol, we only mean the message-passing layer, which is application agnostic. To learn more about the application layer and building cross-chain apps, [check out the Developers section](https://docs.nomad.xyz/developers).

### On-chain and Off-chain Components

The Nomad protocol consists of two core components, on-chain smart contracts and off-chain agents:

* [On-chain smart contracts](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts) implement Nomad's messaging API on-chain, enabling developers to enqueue messages and access replicated state on different chains.
* [Off-chain agents](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents) secure and relay state across chains, forming the backbone of the messaging layer.

Developers need not interface with off-chain agents directly, as the core contracts enforce logic around optimistic verification and ensure messages are securely transmitted.

### Optimistic Verification

Nomad uses an optimistic verification mechanism, which is patterned after optimistic systems. It sees an attestation of some data, and accepts it as valid after a timer elapses. While the timer is running, honest participants (ie. [Watchers](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents/watchers)) have a chance to respond to the attestation and submit fraud proofs.

Read more about [optimistic verification](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms/optimistic-verification) and how it compares to other [verification mechanisms](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms).
