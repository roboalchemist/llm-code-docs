# Source: https://docs.nomad.xyz/developers/application-developers/examples.md

# Examples

TODO: cleanup links from old monorepo

### Example Code <a href="#example-code" id="example-code"></a>

This repository has several examples one can use to build understanding around Cross-Chain Applications.

#### xApp Template <a href="#xapp-template" id="xapp-template"></a>

{% hint style="warning" %}
**Important!** The template supported Solidity version is **<0.8**!
{% endhint %}

[This is a template](https://github.com/nomad-xyz/nomad-monorepo/tree/main/solidity/nomad-xapps/contracts/xapp-template) provided by the Nomad team that shows the high-level components of an xApp, ready for one to fill in their own application logic and utilize a Nomad channel for cross-chain communication.

To implement a xApp, define the actions you would like to execute across chains. For each type of action,

* In the [xApp Router](https://github.com/nomad-xyz/nomad-monorepo/blob/main/solidity/nomad-xapps/contracts/xapp-template/RouterTemplate.sol):
  * implement a function like doTypeA to initiate the action from one domain to another (add your own parameters and logic)
  * implement a corresponding \_handle function to receive, parse, and execute this type of message on the remote domain
  * add logic to the handle function to route incoming messages to the appropriate \_handle function
* In the [Message library](https://github.com/nomad-xyz/nomad-monorepo/blob/main/solidity/nomad-xapps/contracts/xapp-template/MessageTemplate.sol):
  * implement functions to *format* the message to send to the other chain (encodes all necessary information for the action)
  * implement functions to *parse* the message once it is received on the other chain (decode all necessary information for the action)

#### Connection Management <a href="#connection-management" id="connection-management"></a>

The router implements the [`XappConnectionClient`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-router/contracts/XAppConnectionClient.sol) abstract contract. This contract provides convenience functions for working with a [`XAppConnectionManager`](https://github.com/nomad-xyz/monorepo/blob/main/packages/contracts-core/contracts/XAppConnectionManager.sol).

See the section on [Connection Management](https://docs.nomad.xyz/developers/building-xapps#connection-management).
