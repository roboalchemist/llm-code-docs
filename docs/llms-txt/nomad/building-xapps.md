# Source: https://docs.nomad.xyz/developers/application-developers/building-xapps.md

# Building xApps

A xApp (pronounced "zap") is a cross-chain application built on top of the [Nomad Protocol](https://docs.nomad.xyz/the-nomad-protocol).

Nomad sends messages from one chain to another in the form of raw bytes. A xApp that wishes to *use* Nomad will need to define the rules for [sending](https://docs.nomad.xyz/developers/quickstart/send-messages) and [receiving](https://docs.nomad.xyz/developers/quickstart/receive-messages) messages for its use case.

Each cross-chain application must implement its own messaging interface. By convention, we call the contracts that implement this protocol the application's **Router contracts.** These Router contracts must:

* **Maintain a permissioned set** of the contract(s) on remote chains from which it will accept messages via Nomad — this could be a single owner of the application on one chain; it could be a registry of other applications implementing the same rules on various chains
* **Maintain a permissioned registry of connections** via the `XappConnectionManager` contract (see [Connection Management](#connection-management)).
* **Encode messages in a standardized format**, so they can be decoded by the Router contract on the destination chain
* **Handle messages** from remote Router contracts
* **Dispatch messages** to remote Router contracts

By implementing these pieces of functionality within a Router contract and deploying it across multiple chains, we create a working xApp using a common language and set of rules. Applications of this kind may use Nomad message passing channels as the cross-chain courier for sending and receiving messages between chains.

### Connection Management <a href="#connection-management" id="connection-management"></a>

The router implements the [`XappConnectionClient`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-router/contracts/XAppConnectionClient.sol) abstract contract. This contract provides convenience functions for working with a [`XAppConnectionManager`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/XAppConnectionManager.sol).

The XCM is the primary permissioning point for channels. It provides functions by which

* xApp administrators can enroll or unenroll `Replica` contracts for inbound messages
* xApp administrators can enroll or unenroll a `Home` contract for outbound messages
* xApp administrators can permission or de-permission watchers
* watchers can unenroll `Replica` contracts

When deploying a xApp `Router`, the xApp administrators must select an existing `XappConnectionManager`, or deploy their own. The address of the `XappConnectionManager` must be passed to the router's initialization method.<br>
