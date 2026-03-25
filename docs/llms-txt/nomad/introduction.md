# Source: https://docs.nomad.xyz/nomad-101/introduction.md

# Introduction

### Introducing: Nomad

[Nomad](https://nomad.xyz) is an optimistic interoperability protocol that enables secure cross-chain communication. &#x20;

Using Nomad:

* Users can bridge tokens between chains
* Asset issuers can deploy tokens across chains
* DAOs can facilitate the execution of cross-chain governance proposals
* Developers can build native cross-chain applications (xApps)

The goal of Nomad is to provide the connective tissue to enable users and developers to interact **securely** in a multi-chain world.

### How does Nomad work?

Nomad enables applications to send data between blockchains (including rollups). Applications interact with [Nomad core contracts](https://docs.nomad.xyz/the-nomad-protocol/smart-contracts) to enqueue messages to be sent, after which [off-chain agents](https://docs.nomad.xyz/the-nomad-protocol/off-chain-agents) verify and ferry these messages between chains.

In order to ensure that message-passing is secure, Nomad uses an [optimistic verification mechanism](https://docs.nomad.xyz/the-nomad-protocol/verification-mechanisms), inspired by fraud-proof based designs like optimistic rollups. This makes Nomad more secure, cheaper, and easier to deploy compared to validator / proof-of-stake based interoperability protocols.&#x20;

Our friends at Connext have written [a fantastic article on optimistic bridging](https://blog.connext.network/optimistic-bridges-fb800dc7b0e0), and why Nomad's optimistic bridging ushers in a new paradigm for cross-chain communication.

To learn more about how Nomad works, including advanced concepts, check out [the Protocol Section](https://docs.nomad.xyz/the-nomad-protocol).
