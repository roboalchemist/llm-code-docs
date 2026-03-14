# Source: https://docs.neuron.world/neuron-concepts/identities-and-accounts.md

# Identities & Accounts

The SDK utilizes several types of addresses, most of which operate transparently in the background. However, the most significant identifier is the **secp256k1 private key**, as depicted in the diagram. This private key is foundational, deriving the **public key**, which also serves as the  DLT identifier such as an Hedera alias. This design is preferred over conventional  account identifiers to facilitate cross-chain compatibility in the future.

### Keys

From the public key, we derive **peer IDs**, which are IPFS-compatible addresses used for direct peer-to-peer (P2P) communication. Similarly, other addresses, such as **EVM addresses** or identifiers for other blockchains (e.g., XYZ chain), are also derived, ensuring the system remains flexible and interoperable with various networks.

{% @mermaid/diagram content="graph
A\[secp256k1 Private Key] --> B\[Public Key / Alias key]
B --> C\[IPFS peerID]
B --> D\[EVM Address]
B -.-> E\[XYZ Chain  Address]" %}

### Accounts

A peer in the Neuron network requires two  ledger accounts: a **parent account** and a **device account and one or more shared account which can be created on demand.** These accounts are linked by a parent-child relationship, but only the device and shared account is explicitly used by the SDK users.

> Device accounts are meant to hold just enough tokens to send and receive public topic messages, while parent accounts are meant to receive data payments.

#### Shared Escrow Accounts

Each device account has the ability to spawn intermediate accounts, hereby called "shared accounts".  A shared account is a multisignature monetary escrow account shared between a buyer,  the parent of a seller and a set of named validators. They are ment to temporarily hold funds until released upon satisfactory conclusion of a business transaction.  &#x20;

#### The **device account** must have three associated topics:

* **stdIn**: For receiving public requests and communications from other peers. Such request can request for service, demands for payments, error messages sent by other peers or dapp specific messages.&#x20;
* **stdOut**: Input: For publicly advertising status messages, such as heartbeat or general status changes that pertain to either availability and connectedness or dapp specific public announcements.&#x20;
* **stdErr**: For logging and reporting self-errors.

{% @mermaid/diagram content="flowchart TD
Parent-account --> Device-account
Device-account --> StdInTopic
Device-account --> StdOutTopic
Device-account --> StdErrTopic" %}

> Topics are public synchronization channels and are intended to maintain node connectivity and provide a verifiable record of events. Communication here should be concise and not overly conversational. Private communications will occur on an encrypted peer to peer channel.

### Topics

Buyers, sellers, and validators use ledger topics to exchange messages. These topics serve as public communication channels visible on the ledger network. Each agent uses following topics

* **stdIn**: used by an agent to listen for messages from other peers. These might be service requests, payment demands, complaints, etc.

* **stdOut**: used by an agent to advertise status messages, heartbeats, and general information about its own situation.

* **stdEr**: this is similar to stdOut, but meant for a peer to log error messages about his own situation.

#### Considerations for Implementing Topics

When implementing topics on a ledger network, it is essential to evaluate factors such as cost, message volume, and the specific needs of the application. Choosing a network that aligns with these considerations can optimize performance and efficiency. Networks with native topic support, like Hedera, may offer inherent advantages, while others might require additional implementation efforts to simulate similar functionalities. The requirement here is to have timestamped strict order on messages and the ability to securely chain messages together. In many consensus networks, this can be achieved with basic building blocks.&#x20;

{% @mermaid/diagram content="

```
flowchart LR

A[Message 1
Sequence 1
Timestamp T1
Message Body Body1
Running Hash h1] --> B[Message 2
Sequence 2
Timestamp T2
Message Body Body2
Running Hash h2 = Hash h1 + Body2 ] --> C[Message 3
Sequence 3
Timestamp T3
Message Body Body3
Running Hash h3 = Hash h2 + Body3]" %}
```

In highly dynamic environments, where message rates are variable, leveraging an economical network can make a significant difference in operational costs. It's crucial to balance the need for frequent communication with the network's capabilities and costs to maximize both functionality and budgetary efficiency.
