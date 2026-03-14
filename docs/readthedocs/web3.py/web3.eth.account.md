# Accounts

## Local vs Hosted Nodes

Hosted Node

A **hosted** node is controlled by someone else. You may also see these referred to
as **remote** nodes. View a list of commercial node providers [https://ethereum.org/en/developers/docs/nodes-and-clients/nodes-as-a-service/].

Local Node

A **local** node is started and controlled by you on your computer. For several reasons
(e.g., privacy, security), this is the recommended path, but it requires more resources
and work to set up and maintain. See ethereum.org [https://ethereum.org/en/developers/docs/nodes-and-clients/] for a guided tour.

## Local vs Hosted Keys

An Ethereum private key is a 256-bit (32 bytes) random integer.
For each private key, you get one Ethereum address,
also known as an Externally Owned Account (EOA).

In Python, the private key is expressed as a 32-byte long Python `bytes` object.
When a private key is presented to users in a hexadecimal format, it may or may
not contain a starting `0x` hexadecimal prefix.

Local Private Key

A local private key is a locally stored secret you import to your Python application.
Please read below how you can create and import a local private key
and use it to sign transactions.

Hosted Private Key

This is a legacy way to use accounts when working with unit test backends like
`EthereumTesterProvider` or Anvil [https://book.getfoundry.sh/reference/anvil/].
Calling `web3.eth.accounts` gives you a
predefined list of accounts that have been funded with test ETH.
You can use `send_transaction()` on any of these accounts
without further configuration.

In the past, around 2015, this was also a way to use private keys
in a locally hosted node, but this practice is now discouraged.

Warning

`web3.eth.send_transaction` does not work with modern node providers,
because they relied on a node state and all modern nodes are stateless.
You must always use local private keys when working with nodes hosted by
someone else.
