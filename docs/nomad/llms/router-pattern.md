# Source: https://docs.nomad.xyz/developers/application-developers/advanced/router-pattern.md

# Router Pattern

Nomad sends messages from one chain to another in the form of raw bytes. A cross-chain application (xApp) that wishes to use Nomad will need to define the rules for [sending](https://docs.nomad.xyz/developers/quickstart/send-messages) and [receiving](https://docs.nomad.xyz/developers/quickstart/receive-messages) messages for its use case.

Each xApp must implement its own interface. We call the contracts that implement this interface "Router" contracts, as their function is broadly similar to routers in local networks. Router contracts ensure that incoming and outgoing messages are in the correct format defined by the application developers, and facilitate handling and dispatch to their destination contracts.

**Router contracts must:**

* maintain a permissioned set of the contract(s) on remote chains from which it will accept messages via Nomad — this could be a single owner of the application on one chain; it could be a registry of other applications implementing the same rules on various chains
* encode messages in a standardized format, so they can be decoded by the Router contract on the destination chain
* handle messages from remote Router contracts
* dispatch messages to remote Router contracts

By implementing these pieces of functionality within a Router contract and deploying it across multiple chains, we create a working cross-chain application using a common language and set of rules. Applications of this kind may use Nomad as the cross-chain courier for sending and receiving messages to each other.
