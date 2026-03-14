# Neuron Documentation

Source: https://docs.neuron.world/llms-full.txt

---

# Intro

The Neuron stack is envisioned as a comprehensive framework designed to revolutionize peer-to-peer networking where participants engage in business and financial transactions.  Its goal is to provide an adaptable, open-source solution that enhances connectivity and communication across decentralized systems. By focusing on universal compatibility, it seeks to break down barriers, offering users a seamless experience that caters to a wide variety of technological needs.

At the core of this framework is a commitment to integrating distributed ledger technology. By leveraging these technologies, the Neuron stack provides a robust and secure foundation that ensures data integrity and privacy. This integration is crucial for enabling secure transactions and fostering trust in a decentralized environment, supporting the next generation of digital interactions.

By utilizing flexible and modular components, the Neuron stack embodies a forward-thinking approach to development. It is designed to be adaptable, catering to various use cases and applications. This versatility allows developers to customize and enhance the stack according to their specific requirements, thus promoting innovation while supporting a wide range of emerging technologies and decentralized applications.&#x20;

**History:** The concepts of the Neuron Stack were developed during our work in the aviation industry, specifically when integrating a decentralized aviation discovery system. This system allowed connected peers to communicate in an out-of-band fashion. Building on these lessons, we developed the Neuron Stack, which today boasts dozens of beta users, demonstrating the concept's utility.

```go
// Some code
```


# Network Participants

Participants in this system are referred to as peers or agents, who either directly communicate with each other or facilitate communications. These participants can operate individually or in groups, engaging in many-to-many (MnN) interactions. Essentially, the focus is on service provider peers (sellers/producers) offering services to consumer peers (buyers/consumers). For clarity, the terms can be used interchangeably to distinguish the two sides of the transaction.

* **Buyer**: Initiates requests for services or data from sellers. The buyer uses DLT  channels (called topics)  for communication and establishes a P2P stream, an encypted high bandwidth and datarate stream, for data transfer.
* **Seller**: Responds to requests from buyers, providing the requested service or data. Sellers also use DLT  topics to send payment demands and other messages.
* **Validator**: Ensures the integrity and validity of transactions between buyers and sellers. Validators monitor  Service License Agreements (SLA), ensure compliance, and participate in escrow services.
* Relay/Support: Peers that help participant to connect in the event of limited reachability.  They either relay messages, or help peers discover the IP address and overcome NAT issues.&#x20;
* Third party observers: These do not necessary interact with peers but do observe public messages on the Distributed Ledger and provide supporting services: e.g. explorers, data analytics, etc.&#x20;
*


# Tenets of Neuron

Neuron’s core tenets—Discover, Connect, Pay, and Protect—create a seamless peer network. Discover locates peers for transactions; Connect builds reliable communication streams; Pay secures financial transactions; Protect verifies interactions without compromising privacy, ensuring security and fairness.

* **Discover**: Facilitate the discovery of peers, ensuring buyers, sellers, and validators can find each other.
* **Connect**: Enable bidirectional communication channels (streams) between peers, even when they are initially unknown to each other.
* **Pay**: Handle seamless, secure money transfers between data providers (sellers) and data consumers (buyers).
* **Protect**: Allow validators to monitor and verify streams to ensure adherence to a Service License Agreement (SLA) written in business language, all without compromising the privacy of participants.


# Purpose and Responsibility of the SDK

## Overview

The Neuron SDK is responsible for maintaining the fundamental network connectivity and security of the Neuron network. Its primary purpose is to ensure that when two peers decide to connect, they stay connected, regardless of network conditions or application behavior. This is different from regular P2P libraries - the SDK doesn't just send packets; it guarantees persistent connections backed by Service License Agreements (SLAs). Moreover, there are minimal external dependencies between the two peers other than the backing DLT; thus, two peers talking to each other should assume that they don't talk to anyone else other than themselves and the DLT. This is unless they agree to be relayed or use an external service to facilitate IP discovery, relaying, etc.

## Core SDK Responsibilities

### 1. Connection Persistence

* Maintain persistent connections between peers at all costs
* Automatically handle reconnection when connections fail
* Use the public ledger (DLT) for signaling and coordination
* Implement the exact reconnection logic specified in the SLA
* Handle NAT traversal and connection establishment
* Persist and maintain connection state
* Connect to peers even in the event of non reachable DLT servers if persistent state allows for connection re-establishemnt.

### 2. Security and Privacy

* Encrypt all sensitive data, especially IP addresses
* Use public key encryption for peer-to-peer communication
* Never expose private information on the public ledger
* Handle secure key management and storage
* Implement identity verification

### 3. Service Discovery

* Make peers discoverable on the network
* Handle service registration and availability
* Manage peer discovery through the network
* Support service advertisement on explorers
* Implement the standardized discovery protocol

## What the SDK Does NOT Do

* Handle application-specific business logic
* Manage application data formats or protocols
* Process application-level messages
* Make decisions about when to connect/disconnect
* Override the standardized connection behavior

## Key Distinctions

### SDK Responsibility

* Maintaining the connection itself using the DLT as a signalling layer
* Handling reconnection automatically
* Managing security and encryption
* Implementing the standardized protocol
* Making peers discoverable

### Application Responsibility

* Deciding which peers to connect to
* Managing application-specific data
* Implementing business logic
* Handling application-level protocols
* Managing application state

## Critical Requirements

### Must Do

1. Maintain persistent connections as specified in the SLA in a way that can be monitored buy outside validators
2. Implement exact reconnection logic without modification
3. Use public ledger only for essential signaling
4. Encrypt all sensitive data
5. Make peers discoverable on the network

### Must Not Do

1. Allow applications to override core connection behavior
2. Expose private information on the public ledger
3. Bypass the standardized protocol
4. Ignore connection failures
5. Modify the deterministic behavior

## Why This Matters

The SDK's behavior is deterministic and verifiable. Any peer on the network can observe the SDK's actions through the public ledger and verify that it's following the correct protocol. This is crucial for:

* Maintaining network reliability
* Ensuring fair service delivery
* Supporting SLA enforcement
* Enabling network validation
* Building trust in the system

## Technologies That Don't Meet Requirements

### 1. Distributed Hash Tables (DHTs)

DHTs like Kademlia or Chord fail to meet the SDK's requirements because:

* They expose IP addresses publicly in their routing tables
* They rely on a network of untrusted nodes for routing
* They don't guarantee persistent connections
* They can't be monitored for SLA compliance
* They don't support deterministic behavior verification

### 2. Unauthorized Relay Services

Relay services that aren't explicitly agreed upon by both peers are problematic because:

* They introduce unauthorized third parties into the communication
* They can't be monitored for SLA compliance
* They may compromise privacy and security
* They create unpredictable connection behavior
* They can't be verified through the public ledger

### 3. Centralized Signaling Servers

Traditional signaling servers (like those used in WebRTC) don't meet requirements because:

* They create a single point of failure
* They can't be monitored for SLA compliance
* They don't provide verifiable connection guarantees
* They may compromise privacy
* They don't support deterministic behavior

### 4. Peer Discovery Protocols (like mDNS)

Protocols that broadcast service availability locally fail because:

* They expose service information without encryption
* They don't guarantee persistent connections
* They can't be monitored for SLA compliance
* They don't support cross-network discovery
* They lack verifiable behavior


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


# Registration & Discovery

Accounts are registered on a distributed ledger, ensuring that they can handle monetary transactions. Both parent and device accounts must be present on the ledger and capable of holding funds. Device accounts are then recorded on a smart contract, which functions as a directory. This directory specifies the service license agreements each device engages in (SLA), the monetary value of the service and also  lists the three topics each device listens to and can communicate with.

### Service Licence Agreements

Service License Agreements (SLAs) need to be stored either verbatim on the ledger or as a hash, depending on the application's requirements. Storing SLAs ensures authenticity and immutability of the agreements between devices and service providers or consumers. In smart contracts, the reference to these SLAs is used to determine which device and service provider or consumer is associated with a particular SLA. This approach enables transparent and efficient tracking and management of SLAs across various devices and services. Importantly, these SLAs are written in natural language to ensure clarity and ease of understanding for all parties involved.

Each SLA comprises a portion that is **common to all agreements,** specifically focusing on connectivity and availability, which is managed by the SDK. This section ensures that basic service connectedness  standards are maintained across different applications,  in a way that a machine validator can follow,  and also specifies the payment cycle—whether it is per month, per year, per minute etc. However, the actual payment amount, which varies by node, is recorded in the smart contract registry, see  [#smart-contract-registry](#smart-contract-registry "mention"),  and not in the SLA.

The remainder of the SLA is tailored to specific business and decentralized application (dApp) requirements — a domain specific block. For instance, in an aviation dApp, the SLA might specify what constitutes good quality sensor data or the required frequency of data transmission. This customization allows for precise and effective service delivery aligned with distinct business goals. In addition to the flat rate connectivity fee that is prescribed in the common block, the domain specific block stipulates any  custom payment logic that is specific to the domain, as well as custom dispute resolution logic.&#x20;

{% @mermaid/diagram content="graph TD
SLA\[/"SLA (PDF Document)"/]

```
SLA --> CommonBlock["Common Block<br>(Connectivity_&_Availability)<br>Prescribed by Neuron Network"]
SLA --> ExtraBlock["Domain&nbsp;Specific&nbsp;Block<br>(Custom Validations per dApp)"]

CommonBlock -->|Defines reconnection protocol for SDK and Validators| ReconnectionLogic["Reconnection Protocol<br>(e.g., retry interval, backoff)"]
CommonBlock -->|Refers to Smart Contract| SLAField["Field: rate = e.g. 5USDC / hour"]

ExtraBlock --> DomainLogic["Custom Validation Rules<br>(e.g., no backward flight for fixed-wing aircraft)"]
ExtraBlock --> DisputeMechanism["Evidence Submission<br>& Dispute Resolution Process"]

style SLA fill:#f9f,stroke:#333,stroke-width:2px
style CommonBlock fill:#bbf,stroke:#333,stroke-width:1.5px
style ExtraBlock fill:#bfb,stroke:#333,stroke-width:1.5px
style SLAField fill:#fff3b0,stroke:#333,stroke-width:1px,stroke-dasharray: 5" %}
```

To ensure SLAs are adhered to, they must detail the nature of public messages exchanged on the Distributed Ledger Technology (DLT). This allows validators to examine the public record and verify compliance with service agreements. Validators may perform checks on a continuous basis or in specific instances, such as when a complaint is raised. In scenarios where validators function as escrow agents, they will assess these public messages to determine whether funds should be released or refunded, ensuring fair and transparent financial accountability.

### Smart Contract Registry

The smart contract serves as a registry for device accounts, detailing their associated communication topics and subscribed Service License Agreements (SLAs) along with the monetary values tied to these SLAs. It provides functionality to:

* Look up devices by ID to retrieve their topics  SLAs and associated rates.
* Insert new devices along with their associated data.

SLAs are created and inserted by a Decentralized Autonomous Organization (DAO), and devices can choose from the offered SLAs when registering.&#x20;

{% @mermaid/diagram content="
flowchart TD
Parent-account \~\~\~ Device-account
subgraph Smart Contract
Device-account --> StdInTopic
Device-account --> StdOutTopic
Device-account --> StdErrTopic
Device-account --> slas@{ shape: docs, label: "SLA,Rate"}

end
" %}

### Discovery

Discovery is consequently predicated on examining the public ledger, initiating with the enumeration of identities maintained within the smart contract, and proceeding with the analysis of the attributes from the `stdout` message stream.&#x20;

DApp developers may execute this independently or may engage third-party entities, e.g. explorers,  with proficiency in this particular function. For example, an external explorer can continually monitor the ledger and build an internal, queryable database, which provides functionalities such as "identify all devices in proximity that offer an SLA of category X."

{% @mermaid/diagram content="sequenceDiagram
participant pn as peerN
participant pnOut as perrN's stdOutTopic
note over pnOut , mirror/explorer: consult SC registry <br/> and monitor relevant stdOuts
pn ->> pnOut: I have changed my location  to xyz
mirror/explorer --> pnOut: store
pn ->> pnOut: I am switching device off
mirror/explorer --> pnOut: store
pn ->> pnOut: I am switching device on
mirror/explorer --> pnOut: store
pn ->> pnOut: I just connected to peer 0x123
mirror/explorer --> pnOut: store
loop Every time t
pn->>pnOut: I am available, next heartbeat in t time
mirror/explorer --> pnOut: store
end

peer ->>+ mirror/explorer: get active devices of SLA s in radtius r
mirror/explorer ->>- peer: result" %}

Explorers can be publicly facing services, enabling more accessible interactions with the network data for various stakeholders. Alternatively, the explorer and discovery logic can be entirely implemented within a peer itself, thereby eliminating third-party dependencies and enhancing both autonomy and security.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FwqCN47GFwxGSbJUS9UJT%2Fimage.png?alt=media&#x26;token=c9183562-64e8-4a68-aac2-271f9a5d8ee4" alt=""><figcaption><p>example explorer offerig API to list devices in proximit</p></figcaption></figure>


# Connection & Communication

Connection establishment  is the result of coordination and signaling via exchanging public messages   using the `stdin` topic. The `stdin` topic manages input data streams, enabling efficient communication between different components.

In contrast to the public message exchange used primarily for signaling and establishing initial contact, once a connection is established, it creates a private multiplexed bidirectional stream. This means that communication occurs directly between the parties without intermediaries, ensuring that data is transferred securely and efficiently. The private stream supports multiple data channels within a single connection, optimizing resource usage and allowing simultaneous data transfers. This setup protects the integrity and confidentiality of the data, as opposed to the initial public exchanges which primarily serve to facilitate the introduction and sharing of IP addresses necessary for the direct, peer-to-peer connection.

### NATs and routers - overcoming reachability limitations.&#x20;

Once a peer discovers its public IP address, it can utilize a public ledger for signaling and exchanging its address with any other peer it intends to communicate with. This process is crucial for establishing direct peer-to-peer connections. To maintain IP privacy during this exchange, the peer can use the public key of the target peer to encrypt its IP address. By encrypting this information, the peer ensures that only the intended recipient can decrypt and access the IP address, thereby preserving confidentiality. The encrypted IP address is then communicated as part of a request for service, enabling secure and private connectivity between peers.

### Discovering Public Facing IP Addresses

Discovering a peer's public-facing IP address is essential for establishing direct peer-to-peer connections over the internet. This process involves determining the external IP address assigned by the network's NAT or router, which may differ from the device's local IP address. Accurate discovery ensures that peers can effectively exchange address information for successful connectivity.

One way to discover an external facing IP address is to consult STUNs. Session Traversal Utilities for NAT (STUN) servers are a vital component in peer-to-peer communication systems, enabling devices to discover their public-facing IP addresses. These servers operate by responding to requests from devices, providing information about their external IP address and port number as seen by the internet. This information is crucial for establishing direct connections across NAT devices, which often assign private local IP addresses that are not accessible over the internet. One issue with using STUN servers is the element of centralization; many STUN services are managed by third parties, which means users must trust these servers to handle their data securely and reliably.

To mitigate centralization concerns, peers can leverage a decentralized approach using a collaborative, paid-for decentralized application (dApp). In this model, peers request their public-facing IP address from multiple other peers, who have a know pubilc facing IP address,  and verify the consensus of the results. By aggregating responses from a sufficient number of peers, a device can accurately determine its public IP. If the responses are inconsistent or indicate discrepancies, it may reveal issues with the network's NAT, suggesting that it is too restrictive or not functioning optimally. This peer-based methodology not only reduces reliance on central servers but also allows individuals control over their privacy and data handling. In the protocol below, we illustrate a comuncation with one peer where the serving peer can encrypt a public messages using the other party's public key. We omit payment demands for brevity. &#x20;

{% @mermaid/diagram content="sequenceDiagram
participant b as buyer
box Hedera
participant bi as buyerStdInTopic
participant si as sellerStdInTopic
end
Note over si,s: Seller listens to its topic for requests
Note over b,bi: Buyer listens to its topic for requests

```
     participant s as seller
     b ->> si:What is my IP address
     si -->> s: receive  message
     s ->>+ bi: Dial me at: encrypt(92.2.3.4)
     bi -->> b: receive message
     b  ->>+ s: Decrypt and Dial: 92.x.x.x
     s ->>- b: your IP address is: 77.x.x.x
     
     
  " %}
```

In cases where a restrictive NAT prevents establishing a direct connection, a technique known as hole punching can be employed. This method involves using the public ledger as a signaling server to coordinate the connection between two peers. Hole punching allows peers to negotiate and open communication channels through NATs by synchronizing the timing of message exchanges so that ports remain open long enough for data to be transmitted between them. This technique often requires precision and fast consensus in order to  enabling seamless peer-to-peer communication even in restrictive network environments. There a cases where hole punching is ineffective, for instance when both peers are behind public NATs such as mobile phone networks; in such cases communication is relayed over relay peers; which inevitably add one hop of latency to the route.&#x20;

### Exchanging IP Addresses

During a service request, peers exchange public IP addresses using the public ledger. This method ensures that the IP address information is accessible yet secure, as it records every transaction transparently.

If the initial dialing attempt fails, peers may attempt additional connection strategies, such as retrying the dial at different intervals or adjusting the signaling messages until a connection is successfully achieved. Once the secure stream is established, the peers can confidently exchange data without worrying about interception from unauthorized parties, as the encryption protects the data integrity and privacy.

To enhance security, each peer encrypts its IP address using the recipient's public key. This encryption ensures that only the intended recipient can decrypt the information, providing a secure means of IP address exchange during the service request. If the initial dialing attempt fails, peers may attempt additional connection strategies, such as retrying the dial at different intervals or adjusting the signaling messages until a connection is successfully achieved. Once the secure stream is established, the peers can confidently exchange data without worrying about interception from unauthorized parties, as the encryption protects the data integrity and privacy. Note that this established communcation channel is now peer to peer, and does not expose any messages to teh public ledger.&#x20;

{% @mermaid/diagram content="sequenceDiagram
participant b as buyer
box Hedera
participant bi as buyerStdInTopic
participant sh as AcccountService
participant si as sellerStdInTopic
end
Note over si,s: Seller listens to its topic for requests
Note over b,bi: Buyer listens to its topic for requests
participant s as seller

```
     b ->>+ si:I want data and my encrypted IP address is 77.x.x
     s --> si:received request
     s --> s: do checks, decrypt IP
     s ->> b: dial 77.x.x
     Note over b,s: connection established - now both parties know each othe's IP address
     s ->> b: here is my data
```

" %}

### M x N comuncation and message relays

In a peer-to-peer communication network, the M x N communication model allows for flexible and scalable data exchange. This means that a single buyer can receive data from multiple sellers, while a single seller can provide data to multiple buyers. This setup optimizes resource allocation and enhances the overall efficiency of data distribution.

Using the Neuron stack, this communication model is enhanced with an input stream multiplexing capability. Multiplexing allows a single IP address and port to be used by a consumer to access data from multiple providers. This capability significantly reduces the number of network endpoints required, making it particularly beneficial for devices with limited networking resources, as it minimizes the need for additional connection handling.

The M x N communication model not only improves resource efficiency but also provides a robust framework for asynchronous data exchange. By allowing multiple streams to be handled through a singular channel, it reduces overhead and facilitates smoother integration and communication between diverse peer entities.&#x20;

Relay peers serve a dual purpose: they assist participants in communicating through strict NATs (similar to the TURN protocol) and facilitate peering and meshed communication.

**Meshed Communication Topology**\
In scenarios where a device with limited bandwidth needs to broadcast messages to multiple recipients, relay peers can be employed to extend its reach, even if direct communication is technically feasible. This approach enables the establishment of a layered service delivery system to enhance Quality of Service (QoS). For example, different charges can be applied based on whether peers are directly connected or are rebroadcasting the data.

## Structure of a Peer-to-Peer Connection

In the architecture of a peer-to-peer connection, three public-facing channels—stdin, stdout, and stderr—are used to communicate over a distributed ledger (DLT). These channels are intended strictly for essential functions such as peer discovery, validation, signalling, and verifiable public proof. As DLT transactions tend to be costly in terms of both latency and financial overhead, these messages must carry no more information than is absolutely necessary. Once initial coordination is complete, a private, low-latency, fully encrypted channel is established directly between the two peers. This channel supports fast and secure communication that bypasses the DLT entirely, ensuring scalability and privacy.

At the lowest layer, the connection between two peers is treated as a persistent, high-value resource. It is the SDK’s responsibility to maintain this connection at all costs. Should the connection fail—for example, due to network changes or NAT restrictions—the SDK must fall back to the DLT signaling mechanisms to re-establish connectivity. Connections are typically governed by flat-rate terms outlined in the SLA, and thus are not meant to be created or destroyed frequently.

It is the responsibility of the SDK to maintain an active connection between peers in strict accordance with the protocol prescribed in the SLA. This connection protocol is defined in the *common block* of the SLA, which is shared across all agreements and authored by the Neuron Network. As a result, all SDK implementations—regardless of who writes them—are bound to follow the same standardized reconnection logic and lifecycle rules as specified in this canonical SLA fragment. This uniformity ensures deterministic behavior across the network and guarantees interoperability. Furthermore, because the SDK’s signaling and recovery activities are recorded via public-facing DLT topics (such as stdin, stdout, and stderr), its adherence to the SLA can be publicly verified. This makes the SDK’s compliance auditable, reinforcing trust in the network and enabling open inspection of connection management behaviors.

Built on top of a single connection are lightweight, bidirectional streams. These streams are inexpensive to open and close, and they serve as the primary conduit for all application-level data. A stream is essentially a raw byte channel that supports any higher-level protocol—such as HTTP, gRPC, or custom formats—without dictating the serialization or framing. Streams may be used for brief interactions, such as sending a small HTTP-like message and closing immediately, or they may remain open for long-lived sessions. Importantly, a single peer-to-peer connection can multiplex many such streams simultaneously, optimizing both performance and resource utilization. The underlying transport protocol for all streams is required to support reliable, ordered delivery over QUIC/UDP, ensuring robustness in even highly dynamic network environments.


# Messaging

### Topics and Consensus.&#x20;

Topics are chronological records that capture events, actions, or messages between entities. Each log entry  includes a timestamp, which records the exact time an event occurred. Timestamps, sequence number and hash-linking are crucial because they establish the sequence of events, ensuring clarity about when actions happened relative to one another. By maintaining an immutable and transparent public log, participants can provide a verifiable history of their interactions, offering a foundation for trust and accountability. I timestamped verified by a number of L1 participants give rise to the ability to use consensus as a service and externalise complex and expensive consensus infranstructure. For this reason, the Neuron stack leverages consensus offered by third parties, such as the Hedera network, rather than maintaining its own consensus infrastructure. &#x20;

### Communication Against a Service License Agreement

When two parties interact, they exchange messages according to the terms outlined in a publicly known Service License Agreement (SLA). The SLA defines the expected behaviors, response times, and actions for each party, forming a shared contract that governs their communication. By recording each message in a public log along with its timestamp, both parties ensure that their actions can be transparently compared to the agreed-upon terms. This setup prevents one party from altering the record or claiming actions that were not taken.

### Resolving Disputes Using Logs and SLAs

If a dispute arises, a neutral third-party validator can examine the public log and compare the recorded messages to the SLA. By analyzing the sequence of events and timestamps, the validator can determine whether each party adhered to their obligations. For example, the validator may check whether a party responded within the required timeframe or if a message’s content aligns with the SLA. This process ensures a fair resolution based on verifiable evidence, fostering accountability and trust in the system.

### Public Message Types

In this framework, messages exchanged between peers fall into two broad categories: shared system messages and dApp-specific messages. Most message types are unique to individual dApps and are explicitly defined in their respective Service License Agreements (SLAs). These dApp-specific messages reflect the particular logic and requirements of the application and are developed and implemented by dApp developers. However, there is also a set of shared system messages that all dApps must implement. These messages are essential for ensuring connectivity, discoverability, and general operational integrity across the network.

### SDK-Handled Messages and dApp-Specific Logic

Every message exchanged is initially intercepted by the neuron stack, which serves as the underlying framework for message handling. If a message belongs to the shared set of system messages, such as those facilitating peer connectivity or aiding discoverability, the SDK processes and responds to it directly. For example, an  SDK might handle a “Ping” message by automatically replying with a “Pong” or address a “Peer Discovery Request” by returning a list of known peers. When the SDK encounters a message it does not recognize—usually a dApp-specific message—it forwards the message to the application layer, allowing the dApp developer’s logic to process and respond accordingly.

### Separation of Concerns for Robustness

This two-tiered approach ensures a clear separation of responsibilities. The neuron stack provides a standardized and efficient mechanism for handling essential system-level interactions, reducing the burden on dApp developers while ensuring interoperability and connectivity across the network. Meanwhile, dApp developers retain full control over the application-specific logic by defining and managing their own messages. This architecture creates a modular system where both the common operational foundation and the unique needs of each dApp are effectively addressed.

{% @mermaid/diagram content="flowchart TD

```
A[Incoming Message - stdInTopic] --> B[SDK Intercept]
B -->|Check if message is handled by SDK for connectivity| C{SDK Message?}
C -->|Yes| D[Process by SDK to keep connection active or try to reconnect]
C -->|No| E[Forward to dApp layer]
E --> F[dApp Handles dApp Specific Message]" %}
```

#### Overview of Message Types

The minimum the neuron stack neesd to defines is several public message types that facilitate decentralized coordination and transparency. These messages are sent over DLT topics and recorded on a public ledger, allowing peers to broadcast operations and coordinate state changes in a verifiable way. Below is a summary of the various message types, their purposes, associated error types, and suggested recovery actions.

Payment Messages:  These are payment transactions recorded on a ledger. In the neuron stack, payments are always made from a peer's account to a shared account.  Implementors need to make se of suspended payment messages or scheduled transactions (in Hedera terms) to allow for enough time to collect ⅔ signatures to transfer monetary amounts out of a shared account.&#x20;

#### Other Message Types

| Category         | Message Type                       | Purpose                                                          | Key Fields & Notes                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------- | ---------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System Updates   | **Heartbeat Messages**             | Periodically broadcast a peer’s availability and state           | <p><strong>Key Fields:</strong> <code>Location</code>, <code>NatDeviceType</code>, <code>NatReachability</code>, <code>BuyerOrSeller</code>, <code>ConnectedPeersAbrv</code><br><strong>Notes:</strong> Helps maintain a live “network map” and status overview.</p>                                                                                                                |
| Service          | **Service Request Messages**       | Requesting services as outlined in the SLA (e.g. buyer → seller) | <p><strong>Key Fields:</strong> <code>EncryptedIpAddress</code>, <code>StdInTopic</code>, <code>EthPublicKey</code>, <code>PublicKey</code>, <code>ServiceType</code>, <code>SlaAgreed</code>, <code>SharedAccID</code>, <code>Version</code><br><strong>Notes:</strong> Aligns with buyer-seller protocols, enabling structured negotiations and compliance with agreed terms.</p> |
| Invoicing        | **Schedule Sign Request Messages** | Issuing payment requests or “invoices” for scheduled actions     | <p><strong>Key Fields:</strong> <code>ScheduleID</code>, <code>SharedAccID</code>, <code>Version</code><br><strong>Notes:</strong> Typically sent by a seller to a buyer, these requests prompt the buyer to authorize a scheduled transaction.</p>                                                                                                                                 |
| Error Reporting  | **Peer Error Messages**            | Informing another peer of encountered issues                     | <p><strong>Key Fields:</strong> <code>EncryptedIpAddress</code>, <code>StdInTopic</code>, <code>ErrorType</code>, <code>RecoverAction</code>, <code>ErrorMessage</code>, <code>Version</code><br><strong>Notes:</strong> Facilitates transparency in error handling, allowing the receiving peer to understand the nature of problems and suggested remedies.</p>                   |
| Self-Diagnostics | **Self Error Messages**            | Logging internal errors for one’s own node                       | <p><strong>Key Fields:</strong> <code>StdInTopic</code>, <code>ErrorType</code>, <code>RecoverAction</code>, <code>ErrorMessage</code>, <code>Version</code><br><strong>Notes:</strong> Helps nodes self-monitor and potentially triggers automated recovery or maintenance procedures.</p>                                                                                         |

***

#### Error Types

Error types categorize issues that might arise during communication or operation. They help nodes and validators quickly identify the nature of a problem and decide on appropriate solutions or next steps. Error messages are used as coordination tools rather than channels for grievances, and are delivered either to another peer’s standard input topic or to a peer’s own standard error topic. When sending these messages, the sender can include a suggested recovery action if it knows the recipient can implement it to maintain smooth operation. For example, if one peer detects that its counterpart is behind a restrictive NAT, but the sender itself has a more open configuration, it might request a role reversal and ask the other party to initiate a hole punching procedure. Likewise, a self-reported error might recommend a recovery action as drastic as shutting down the device if it detects an overheating condition, ensuring the system can take appropriate measures before a more serious failure occurs.

| Category         | Error Types                                                                           | Description                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Connectivity     | `TooEarlyDialError`, `DialError`, `NoKnownAddressError`, `DisconnectedError`          | Issues in establishing or maintaining P2P connections, NAT traversal, or missing addresses.              |
| Messaging        | `WriteError`, `StreamError`, `BadMessageError`                                        | Failures in sending or receiving messages correctly, such as malformed data or broken streams.           |
| Protocol/Service | `VersionError`, `ServiceError`, `BalanceError`, `IpDecryptionError`, `HeartBeatError` | Problems related to SLA compliance, versions mismatch, account balances, decrypting data, or heartbeats. |
| External Access  | `ExplorerReachError`                                                                  | Inability to reach required external explorers or resources.                                             |

#### Recovery Actions

Recovery actions provide hints or recommended steps following an error. They help guide automated or manual remediation, ensuring the network remains resilient and stable.

| Category          | Recovery Actions                           | Description                                                                     |
| ----------------- | ------------------------------------------ | ------------------------------------------------------------------------------- |
| Networking        | `PunchMe`                                  | Requesting NAT punching to restore connectivity.                                |
| Requests          | `SendFreshHederaRequest`, `CheckYourTopic` | Resend requests or verify ledger entries to correct missing or stale data.      |
| Financial/Upgrade | `TopUp`, `Upgrade`                         | Adding funds or upgrading nodes to match protocol versions.                     |
| Communication     | `StopSending`                              | Halting problematic message transmissions to prevent further issues.            |
| Self-Recovery     | `RebootMe`, `ShutMeDown`                   | Triggering local restarts or shutdowns, enabling introspection and maintenance. |

#### Summary and Future Considerations

* **Heartbeat / Status Messages:** Keep the network aware of each peer’s presence and capabilities, aiding in discoverability and trust.
* **Service Requests & Schedule Sign Requests:** Drive the core buyer-seller interactions within SLAs, enabling structured commerce and contract adherence on the DLT.
* **Peer & Self Error Messages:** Enhance the network’s robustness by ensuring issues are transparently communicated and potentially resolved with suggested actions.
* **Evolving Protocols:** As new protocols and dApps emerge, they can introduce their own message types while relying on the existing framework for connectivity, discovery, and error handling.

This architecture allows the SDK to cater to diverse protocols and services in a modular and extensible manner, maintaining a public, immutable, and auditable history that all stakeholders can reference.

### Interpretation of messages and points

The neuron stack, in conjunction with a Service License Agreement (SLA), can establish a system of points or metrics that reflect the quality, reliability, or trustworthiness of a given peer. These points serve as a means for peers and observers to review performance and adherence to agreed-upon standards. Unlike hard-coded requirements or strict numerical thresholds, the points themselves emerge from an interpretive process defined in the SLA. Essentially, the SLA outlines how different messages, behaviors, and adherence patterns translate into points, allowing for a flexible, context-dependent assessment rather than a rigid scoring system.

There is no mandate for a specific minimum or maximum score; instead, the scoring is based on the defined interpretation function. An explorer application, for example, could parse the public logs, apply the SLA-defined logic, and calculate a point score that is then displayed publicly for all to see. Likewise, an individual peer can implement the same logic locally and compute the points for its own use, whether that be to guide its next actions or inform its decisions about with whom to interact. This decentralized approach ensures that the point system remains transparent, interpretable, and adaptable to varying protocols, SLAs, and network conditions.

Here we must take the principle of separation of concerns into account. Points related to connectivity—an essential, shared aspect internal to the underlying stack—are handled uniformly across all dApps. In other words, the rules and interpretations for connectivity-related metrics apply equally to every application, ensuring a consistent foundation for evaluating basic network performance and ensuring reliable peer discovery and messaging.


# Pay & Protect

### Payment demands

At the base level, peers participating in a p2pconnection deposit their funds into a shared multi-signature account—one that requires two out of three possible signatures to authorize a payment. This shared account serves as a secure escrow, ensuring that no single party can unilaterally release or claim the funds without cooperation. A scheduled transaction tied to this account can include payments to various involved parties, such as the service provider, the network’s treasury accounts, and any designated validator or group of validators who oversee the transaction’s fairness.

{% @mermaid/diagram content="sequenceDiagram
participant b as buyer
box Hedera
participant bi as buyerStdInTopic
participant sh as AcccountService
participant si as sellerStdInTopic
end
Note over si,s: Seller listens to its topic for requests
Note over b,bi: Buyer listens to its topic for requests

```
     participant s as seller
     b ->>+ sh:create 2/3 escrow account
     sh ->>-b: acccount created: 0.0.123
     b ->>+ sh:fund account:0.0.123, 10Tokens
     sh ->>-b: done
     b ->>+ si:I want data and left money in 0.0.123 and my encrypted IP address is 92.x.x.x
     s --> si:received request
     s --> s: do checks
     note over s,b:link established and stream eabled
     s ->>+ sh:shedule transction to withraw 3 + 2 + 5 tokens
     sh ->>- s: shedule id: v returned
     s ->> bi: Signature request for schedule id :v
     b --> bi: receive request
     b --> b: do checks
     b ->>+ sh: add signature
     sh ->>- sh: distribute tokens to relevant acccoutns " %}
```

When one party wishes to draw from the shared account, they create a scheduled transaction and then request the other party’s signature. This request is communicated via the other party’s standard input topic, signaling that the funds are ready to be released pending their agreement. If the other party believes the terms of the Service License Agreement (SLA) have not been met, they may refuse to sign. In such a case, the validator—having the third signature—can step in, verify the claims against the SLA by inspecting message flows, and provide the remaining signature if the transaction is indeed valid. In this manner, the multi-sig structure, coupled with scheduled transactions and validator oversight, ensures transparent and fair fund distribution in line with agreed-upon contract terms.

In blockchain systems, multisignature (multisig) collection can occur either on-chain or off-chain, each with distinct benefits. The example above illustrates an on-chain system using "scheduled transactions," providing a transparent and auditable process. This is highly beneficial for scenarios requiring clear audit trails, as every action is recorded on the blockchain. Conversely, off-chain multisig collection offers faster transactions and reduces on-chain congestion, but it may lack the inherent transparency of on-chain solutions. Additionally, smart contract-based multisignatures propose another method, particularly useful for ensuring compatibility with Ethereum. This approach leverages the flexibility of smart contracts to facilitate multisig transactions, circumventing Ethereum's limitation of not natively supporting accounts with multisigs, thus enabling a broader range of decentralized applications adhering to Ethereum's ecosystem.

### SLAs and standard flat rate fees

The SDK provides a structured system for charging a predetermined flat rate for its services, acting as a foundational economic model for applications. This flat rate is an essential part of the Service License Agreement (SLA) and is clearly defined within the associated smart contract t [#smart-contract-registry](https://docs.neuron.world/registration-and-discovery#smart-contract-registry "mention") . The rate can be stipulated as either a recurring amount per time (month, per hour, etc), offering flexibility based on the specific needs and configurations of the application or service in use.

Developers integrating the SDK into their applications must adhere to this fundamental pricing structure, as it constitutes the base layer of economic interaction within the ecosystem. While this **flat rate provides the standard connection fee necessary for maintaining access to the network's core features, developers retain the freedom to enhance their offerings with additional costs for premium features**. This tiered approach allows for the scalability and adaptability of applications, ensuring that the economic framework of the network remains consistent yet flexible for varied use cases.

By including these customizable options over the baseline flat rate, developers can create richer user experiences. These enhancements can be thought of as additional layers that complement the existing SDK functionalities, tailored to meet business-specific goals or user demands. This modular and extensible model not only reinforces the SDK’s foundational economic strategies but also encourages innovation, allowing developers to craft bespoke solutions on top of the standardized core provided by the network.

### Protect

Validators, which are machines, humans in the loop, or AI agents play a critical role in ensuring the integrity and fairness of the network. They continuously monitor network traffic to verify that peers are following the agreed-upon protocols and SLAs. In cases where disputes arise—such as disagreements over whether certain messages were sent on time or whether the correct sequence of steps was followed—validators can perform targeted, on-demand reviews of the message logs. Through this continuous and conditional oversight, validators help maintain trust, as all parties know that an impartial, verifiable mechanism exists to confirm what actually transpired on the network.

At a minimum, every validator must be equipped to handle the core set of messages related to connectivity and basic operations as prescribed in the common block of all SLA agreements . This foundational messaging layer is uniform across all dApps, ensuring that validators can reliably assess network health and peer availability. The underlying SDK provides this capability out of the box, simplifying the validator’s role in basic network oversight as well as for standard rate fee payments.

&#x20;For any additional, dApp-specific monitoring requirements—such as custom SLA checks or specialized transaction verifications—dApp developers must implement and integrate their own logic. This division of responsibilities ensures that all participants share a consistent baseline of network assurance, while still allowing each dApp to tailor validation to its unique needs.

Example: A flight tracking dApp leverages the Neuron SDK to establish peer connections and transmit aviation signal data. A validator, in turn, relies on the core SDK’s standardized validation logic to assess compliance with the *common SLA block*—specifically with respect to connectivity and availability. However, domain-specific validation, such as aviation-specific integrity checks, requires custom logic layered on top of the SDK’s foundation. This custom logic must be explicitly defined in the SLA; for instance, a rule like “fixed-wing aircraft flying backwards constitutes a red flag” would be codified as part of the SLA’s domain-specific section. Additionally, the SLA must outline the process by which validators expect to receive verifiable evidence from peers in the event of a dispute, since p2p connections are private, ensuring that all parties have a shared understanding of how violations are assessed and resolved.

### Consensus

Consensus in this system is not rooted in a complicated, stand-alone mechanism; rather, it emerges naturally from the shared ledger of messages. When participants select a validator or a set of validators, the process can be as simple as choosing a single trusted party or electing a group of validators. In the case of a validator group, they rely on majority consensus to make decisions. Crucially, the ledger of topic messages provides a reliable and tamper-evident record, allowing all honest validators to reach the same conclusions by independently inspecting the message history and applying the same agreed-upon interpretation defined in the SLA.

Because the topic functions like a ledger—complete with ordered messages, timestamps, and running hashes—validators do not need to operate their own consensus protocol. They simply observe the topic, apply the SLA rules, and derive consistent interpretations of events. This means that coordination between validators becomes minimal. If all honest validators use the same SLA logic and message interpretation, they will arrive at the same outcomes with no need for extensive inter-validator communication. They can trust the topic’s structure and data to guide their conclusions, reducing overhead and complexity.

When it comes time to finalize decisions, validators only need to record their conclusions or sign off on a scheduled transaction. Even in a group setting, this step is not about reaching a shared interpretation—since that should already be guaranteed by following the same SLA rules—but about securing and publishing their collective signatures. Each validator independently forms a view of the situation, and if the SLA requires it, they all sign a scheduled message. This signature collection step ensures that the decision is verifiably endorsed by the required majority, but it does not demand the validators coordinate their reasoning or debate the correctness of their interpretations.

It is also important to note that validators do not have to “sound the alarm” at every breach of an SLA. In many business scenarios, participants may prefer to continue working together or pay out as normal, even if some conditions were not perfectly met. The validator’s role is to provide a reliable mechanism for resolution if and when the parties choose to enforce the SLA. Until then, participants can agree to overlook minor discrepancies and carry on, knowing that the system remains transparent and that the option to involve validators is always available if disputes escalate.


# Use Cases

## 4DSkyEdge

TBD

## TeamAIgent

TBD<br>

## RTKNearMe

TBD


# Installation

## What You'll Learn

By the end of this guide, you'll have:

* ✅ Neuron NodeBuilder installed and running
* ✅ Your account set up and connected to the network
* ✅ A working development environment ready for tutorials

## Before You Start

Make sure you have:

* A computer running Windows, Mac, or Linux
* An internet connection
* About 30 minutes of time
* An email invitation to the Neuron Beta program

Welcome to the Neuron NodeBuilder Beta! Here you can find out how to install the software and follow our tutorials to learn how to buy and sell services with other users, machines, or AI agents.

{% embed url="<https://www.youtube.com/watch?v=hcfN0JjGVsc>" %}

## Step 1: Get Access to the Beta Program

**Option A: I have an email invitation**

1. Check your email for a Neuron Beta invitation
2. Click the registration link in your email
3. Continue to Step 2 below

**Option B: I don't have an invitation**

1. Contact <tech@neuron.world> to request beta access
2. Sign up to the waiting list: <https://www.neuron.world/builder>
3. Wait for your invitation email, then return to Option A

## Step 2: Create Your Account

1. **Click the registration link** from your email invitation
2. **Create a new account** with your email and a strong password
3. **Verify your email** by clicking the link sent to your inbox
4. **Accept the terms and conditions**

💚 **Important:** You must register a new account, even if you already have an account with Neuron, as this one is specific to the builder.

**Troubleshooting:** If the system does not let you accept the terms, logout, re-login, and try again.

After successful registration and login, you should see this screen:

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FxqyjWmsNa284xsIn3VnJ%2Fimage.png?alt=media&#x26;token=3b5d6dac-7366-4814-8f92-740b7855af20" alt=""><figcaption></figcaption></figure>

## Step 3: Copy Your Credentials

1. **Find your credentials** on the page above
2. **Copy your Hedera account number** - it looks like `0.0.123456`
3. **Copy your private key** - it's a long string of letters and numbers

🔒 **Keep these around!** You'll need them to connect to the network, and you can't recover them if lost.

Note this is a testnet, if you need to get these keys back log back into your account.&#x20;

## Step 4: Install the NodeBuilder Software

You have two options for installation:

### Option A: Easy Installer (Recommended for Beginners)

1. **Download the installer** from the links provided on your account page
2. **Run the installer** by double-clicking the downloaded file
3. **Wait for installation** to complete
4. **Your browser will automatically open** to `http://localhost:1880`

**For Mac users:** Look for the Neuron icon in your menubar (top of screen), not in your dock.

### Option B: Build from Source (Advanced Users)

**Prerequisites:** You need `nodejs` and `git` installed first.

1. **Follow the build instructions** provided on your account page
2. **Monitor the terminal/command prompt** for any error messages
3. **Keep the terminal window open** - it helps with troubleshooting
4. **Wait for the success message** that tells you to visit `http://localhost:1880`

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FoNS4zlzHMeuBqZtq7lVy%2F1.png?alt=media\&token=48314a4f-3e30-4bbe-8202-6177e7e7016b)

## Step 5: Connect to Your NodeBuilder

1. **Open your web browser** (Chrome, Firefox, Safari, or Edge)
2. **Go to:** `http://localhost:1880` or `http://127.0.0.1:1880`
3. **Enter your credentials** when prompted:
   * Hedera account number (the `0.0.123456` you saved earlier)
   * Private key (the long string you saved earlier)

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FnCwycg93j4hJgMxcui6i%2F2.png?alt=media\&token=c35acda3-12a4-47a2-ae1f-982776e4e205)

4. **Click Save Credentials and continue** - the system will connect to the Neuron network
5. **Wait for a coder's canvas to load** - you should see an empty canvas appear

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fadk0VpsMextthanPt3zq%2F3.png?alt=media\&token=962842bc-bb49-4f01-9412-e160f44b6f88)

## Step 6: Verify Everything is Working

✅ **You should see:**

* An empty canvas (workspace) in the center
* Various nodes available on the left sidebar
* Your account balance in the upper right corner
* Neuron-specific nodes mixed with generic building blocks

## 🎉 Success! What's Next?

You're now ready to build your first program! Continue to: [your-first-program-hello-world](https://docs.neuron.world/node-builder-software/your-first-program-hello-world "mention")

## Common Problems & Solutions

**Problem:** Browser shows "This site can't be reached"

* **Solution:** Make sure NodeBuilder is running (see Step 6 above)

**Problem:** Can't find my credentials

* **Solution:** Go back to your account page where you registered

**Problem:** "Invalid credentials" error

* **Solution:** Double-check you copied the full account number and private key correctly

**Problem:** NodeBuilder won't start

* **Solution (Installer):**
  * Make sure NodeBuilder is not already running in the background. On Windows, open Task Manager and end any "NodeBuilder" or "node" processes. On Mac, use Activity Monitor to do the same.
* **Solution (Command Line):**
  * Ensure you have all prerequisites installed: `nodejs` and `git`.
  * Check for any running "NodeBuilder" or "node" processes and terminate them (Task Manager on Windows, Activity Monitor or `kill` command on Mac).
  * If you see error messages about missing dependencies, install them as indicated.


# Your first program: Hello World!

## What You'll Learn

By the end of this tutorial, you'll have:

* ✅ Built your first working Neuron program
* ✅ Created a "seller" that sends data to buyers
* ✅ Connected with a buyer bot on Discord
* ✅ Seen real peer-to-peer data exchange in action

## Before You Start

Make sure you have:

* ✅ Completed the [installation](https://docs.neuron.world/node-builder-software/installation "mention") tutorial
* ✅ NodeBuilder running at `http://localhost:1880`
* ✅ Your Hedera credentials saved and ready
* ✅ Discord account (you'll need Beta OG status)
* ✅ About 20 minutes of time

:octagonal\_sign: **Important:** These tutorials are for Neuron Beta OGs. If you don't have Beta OG status in Discord, you won't be able to complete this tutorial.

## What We're Building

We'll create a simple program that "sells" timestamps (current time) to any buyer who wants to purchase them. Think of it as your first digital vending machine!

✅ You should now be at 127.0.0.1:1880 in your default browser, where your local installation resides. Upon the initial installation, the system will prompt you to enter the credentials you noted down earlier

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FnCwycg93j4hJgMxcui6i%2F2.png?alt=media\&token=c35acda3-12a4-47a2-ae1f-982776e4e205)

You're expected to see an empty canvas to start writing your very first hello world using the neuron builder.

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fadk0VpsMextthanPt3zq%2F3.png?alt=media\&token=962842bc-bb49-4f01-9412-e160f44b6f88)

🚀 Let's do it: Setup the backbone

We shall write a minimal program that "sells" a random string (a timestamp) to a potential buyer. We'll do that by configuring a few nodes on this screen and then we'll go to discord to ask for a buyer to "buy" our message in a peer-to-peer manner and no intermediaries involved.

### Action 1: Drag a neuron "seller config" node into the canvas

* <mark style="color:blue;">Double click</mark> it and simply set up some basic info in the provided form. Feel free to enter any random information in here.
* Hit done.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FNtHu5NqbEtw9WYyhvvYy%2F2.gif?alt=media&#x26;token=628b0cf6-3538-4da0-a5ef-239c88cabb27" alt=""><figcaption></figcaption></figure>

This node is holding basic configuration data and is a one off process you have to do. What it does is setting up account information for that particular node which is separate to your main account (the one you created earlier upon registration)

### Action 2: Drag a "neuron p2p" node into the canvas

1. <mark style="color:blue;">Double click</mark> on it and select the previously created neuron seller to reference it.
2. Hit done

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FBps3yL0unQ3jCTF9HUlR%2F2.gif?alt=media&#x26;token=7cc7ec1a-22f7-490e-9562-22b31dce7352" alt=""><figcaption></figcaption></figure>

This node is referencing the configuration node from above and is responsible for communicating direct with other nodes

🎉 You have now coded your seller's backbone to start selling information.

<mark style="color:orange;">Your program is not running yet</mark>, it will do so when you hit the deploy button; you don't need to do this as we have not connected any data sources.

🚀 Let's do it. We shall now connect data to sell

### Action 3: Drag an "inject node" into the canvas and create a connection

* Double click, and select an interval of 5 seconds
* Hit done

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Forw7MoHCfEfeg47HrwCn%2F3.gif?alt=media&#x26;token=3768b83b-c23d-4071-a2ea-ca3c2121d991" alt=""><figcaption></figcaption></figure>

This is a basic node that simply injects (creates) a string or timestamp as a one off message or can be set to be done in an interval. By default it sends out timestamps and you can leave it like that.

The program's purpose is to send a timestamp via peer-to-peer (p2p) communication to any entity connected to the Seller node specified by the p2p node.

In our setting, it's important to distinguish between connecting and communicating. Imagine the Seller node as a telephone switchboard in a call center. It establishes and maintains all active connections, ensuring the lines stay connected while handling the complex tasks involved. Peers use their devices (p2p nodes) to communicate over these pre-established lines without worrying about maintaining the connections. Currently, the protocol between the p2p node and the switchboard assumes that if a p2p node doesn't specify a destination, the data is broadcast to all connected peers.

### 🚀 Action 4: hit the Deploy button

A blue dot on your flow-tab indicates that your actions are not committed. To commit actions you need to hit the deploy button. Notice that any change in the UI or node properties requires a new deploy.

Once you have done so

* wait for the Seller status to display the message "Active...". This means that a device is created and an EVM address is available to use as a communication reference.

### Action 5: Communicate our EVM address to the other side, the buyer.

We need to find our EVM address to communicate it to a potential buyer. To do so click the "Seller" node and copy the EVM address into your clipboard.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FQrU9xTjcu9uA9CqHSjzZ%2F4.gif?alt=media&#x26;token=e0fe458e-b73f-4c01-ac7d-e5c00aa801bd" alt=""><figcaption></figcaption></figure>

In the current scenario, we need a buyer or several buyers interested in purchasing our data. Fortunately, there's an enthusiastic buyer, a bot, eager to consume your information—be it a timestamp or a string you're sending out. All we need to do is share our EVM address, and this bot, which is just another neuron peer controlled by AI on Discord and Slack, will acquire your data. In addition to purchasing your data, the bot will also monitor your vitals.

:point\_right: Goto #node-builder-builders on Discord <https://discord.gg/4APVGrwM>

:red\_circle: <mark style="color:red;">Note: the channel is a public channel and messages you send will be visible to other BetaOGs!</mark>

Type the following message:

`/tech-support can you check my heartbeat status <my-evm-address>`

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FAeJn7TfkNTwtcdXe8DHY%2Fimage.png?alt=media&#x26;token=1246d135-cce4-4b67-8032-c21a4fb233d4" alt=""><figcaption></figcaption></figure>

If you get a heartbeat that's recent to a couple seconds then you're all fully set up.

### Action 6: Instruct the bot to buy your data

`/tech-support test my Seller: <my-evm-address>`

You should see the timestamp or string you have been sending out as a response in discord!

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fc5ifkRzACTlys59OhqXO%2F5.gif?alt=media&#x26;token=b67e454e-35d9-4889-adac-e3a4e7dab258" alt=""><figcaption></figcaption></figure>

At the same time you will see your node being connected to one other peer.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FRYjfacR9TMvaibeh1ARl%2Fimage.png?alt=media&#x26;token=fa773343-5685-475a-96a9-d844d914f7a5" alt=""><figcaption></figcaption></figure>

## What You Just Accomplished

You've built a complete peer-to-peer commerce system! Your program automatically:

* Generates fresh timestamps every 5 seconds
* Advertises them for sale on the Neuron network
* Handles buyer connections and data delivery

## Common Problems & Solutions

**Problem:** Bot says "No heartbeat" or shows old timestamp

* **Solution:** Make sure you clicked "Deploy" and see "Active" status on your seller node

**Problem:** Bot doesn't respond to commands

* **Solution:** Check your EVM address is copied correctly (no extra spaces)

**Problem:** NodeBuilder shows "Connecting..." forever

* **Solution:** Check your internet connection, try refreshing the browser, kill the process and restart

**Problem:** Can't find the Discord channel

* **Solution:** Make sure you have Beta OG status and joined the correct server

## Next Steps

[Tutorial 1: Sell ADS-B Aviation Data](https://docs.neuron.world/node-builder-software/tutorial-1-sell-jv-adsb-data) - Connect real IoT sensors

In the previous section, you observed how a local peer communicates basic data to a remote peer. Next, we'll explore how to enhance this example to transmit more complex data, such as ADS-B aviation information, to a buyer.


# Tutorial 1: Sell JV ADSB data

## What You'll Learn

By the end of this tutorial, you'll have:

* ✅ Connected to a real IoT data source (Jetvision AirSquitter)
* ✅ Built a seller that streams live aviation data
* ✅ Created your own local aircraft tracking map
* ✅ Sold structured JSON data to remote buyers

## Before You Start

Make sure you have:

* ✅ Completed the [installation tutorial](https://docs.neuron.world/node-builder-software/installation) and [hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world)
* ✅ Access to a Jetvision AirSquitter device
* ✅ NodeBuilder running at `http://localhost:1880`
* ✅ Discord account with Beta OG status
* ✅ About 30 minutes of time

:octagonal\_sign: **Important:** These tutorials are for Neuron Beta OGs. If you don't have Beta OG status in Discord, you won't be able to complete this tutorial.

## What We're Building

In this tutorial we will be connecting to a local data source, a Jetvision AirSquitter, and sell aviation data to data buyers. You don't need to worry about finding buyers as we have one setup for you who lives as a bot in discord and is willing to consume your data.

To speed things up, we have a ready made solution (flow) that you can load into your builder.

### Action 1: Get a ready made template

You will need to know how to configure Seller nodes and link them up with Neuron P2P nodes. If you haven't done so already, [complete the installation tutorial](https://docs.neuron.world/node-builder-software/installation) first and then [complete the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world)

* Exit any previous NodeBuilder instances and start with a clean canvas. Check if any process is lingering from previous runs and kill it.
* Click on templates
* Select "jetvision-seller-tcp"
* Highlight the newly generated tab

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FfxphACDPNjkoHBcWflEO%2F1.gif?alt=media&#x26;token=b842170e-c1ec-4451-975b-3838806b5fc9" alt=""><figcaption></figcaption></figure>

Alternatively you can import code directly from Github or code that is shared from other users:

* visit <https://github.com/NeuronInnovations/neuron-node-builder/raw/refs/heads/master/templates/jetvision-seller-tcp/flow.json>
* copy into your clipboard the flow code
* right click on your canvas and open the import menu (Insert > Import)

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FF35KooEQV2nQ0h83qCR4%2Fimage.png?alt=media&#x26;token=7773d09f-41aa-4394-8bf5-8a58cd9b23bf" alt="" width="375"><figcaption></figcaption></figure>

* paste your clipboard into the resulting screen

You have now a ready made flow imported and are ready to start handling ADSB data.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fm85L13uvJOfKU5Y1m9l4%2Fimage.png?alt=media&#x26;token=c8321501-04b4-4436-8f44-f2be69ac5f8f" alt=""><figcaption><p>If you read the flow from left to right, you will find that the data is coming from a tcp connection at port 30002. The address of that connection is your local-jv-address, the one that you'll find displayed on your red box. That data is chucked JSON data as it comes out of you AirSquitter and travels down two paths: one is a local map and the other one is any potential buyer</p></figcaption></figure>

### Action 2: Setup the "Jetvision seller config" and "Neuron P2P out"

Setup the <mark style="background-color:blue;">Jetvision seller config</mark> and link it with the <mark style="background-color:blue;">Neuron P2P out</mark>. If you don't know how to do this, refer to [Action 1 and Action 2 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world). Remember to hit deploy and wait for connection to become active.

You are now ready to send data into your seller via a peer to peer connection.

### Action 3: Double click the "tcp" node to set the correct AirSquitter address

* Get your local-jv-address from the red box
* Enter it in the address in the tcp node
* Click Done

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fl0pgMfR727VD6QOfxRZD%2F7.gif?alt=media&#x26;token=11499488-f65b-4a5c-a6b1-da3a5eeaf949" alt=""><figcaption></figcaption></figure>

### Action 4: Visit <http://localhost:1880/worldmap> in a new tab

You should be seeing the planes that your own sensor is seeing on your very own map!

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FFrNi3LY3EPYFJeo74Twa%2Fimage.png?alt=media&#x26;token=333beb9a-d410-4e5f-b4ee-01c49fc4d6a8" alt="" width="563"><figcaption></figcaption></figure>

However, let's check if our buyers are getting the JSON data too so that they can display it too on their own solutions.

### Action 5: Get the buyer bot to consume your data

This part is identical to [Action 5 and Action 6 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world) where you:

1. Communicate the EVM address to the bot
2. Check with the bot if you are setup
3. Instruct the bot to test your seller

If you need help refreshing your knowledge on how to do so then follow [Action 5 and Action 6 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world).

However, this time you should be getting structured ADSB data in JSON format from the remote bot!

You are now prepared to send a wide range of IoT data to remote peers.

## What You Just Accomplished

🎉 **Congratulations!** You've successfully:

* Connected to a real IoT data source (AirSquitter)
* Built a live aviation data streaming system
* Created your own aircraft tracking map
* Sold structured JSON data to remote buyers
* Learned how to work with TCP data sources

## Common Problems & Solutions

**Problem:** No planes showing on the map

* **Solution:** Check your AirSquitter is powered on and the TCP address is correct

**Problem:** Bot gets no data or old data

* **Solution:** Verify the TCP connection is working and you clicked "Deploy"

**Problem:** Can't find the local-jv-address

* **Solution:** Look for the red box in your flow - it displays your AirSquitter's IP address

## Next Steps

Ready for more advanced tutorials? Continue to:

* [Tutorial 2: Sell Consultancy with Chat](https://docs.neuron.world/node-builder-software/tutorial-2-sell-consultancy-with-chat) - Build interactive services


# Tutorial 2: Sell consultancy with chat

## What You'll Learn

By the end of this tutorial, you'll have:

* ✅ Built a bidirectional communication system
* ✅ Created an interactive chat-based service
* ✅ Learned how to receive messages from buyers
* ✅ Provided real-time consultancy services via P2P chat

## Before You Start

Make sure you have:

* ✅ Completed the [installation tutorial](https://docs.neuron.world/node-builder-software/installation) and [hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world)
* ✅ NodeBuilder running at `http://localhost:1880`
* ✅ Discord account with Beta OG status
* ✅ About 25 minutes of time

:octagonal\_sign: **Important:** These tutorials are for Neuron Beta OGs. If you don't have Beta OG status in Discord, you won't be able to complete this tutorial.

## What We're Building

In this tutorial, we'll demonstrate how information can flow bidirectionally. Once again, you'll take on the role of a data seller, but we'll diverge from previous tutorials where the information producer was the seller.

Here you'll take the role of being a consultant, e.g. a tax expert or psychologist that sells consultancy services via chat.

In this example, your buyer will be a bot that initiates the chat, asks you questions by sending p2p messages directly into your seller p2p node and you will be seeing these and replying using a chat UI.

### Action 1: Get a ready made template

You will need to know how to configure Seller nodes and link them up with Neuron P2P nodes. If you haven't done so already, [complete the installation tutorial](https://docs.neuron.world/node-builder-software/installation) first and then [complete the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world). The hello world tutorial contains instructions on how to use a remote bot to act as a buyer thus, don't skip it.

To speed things up, we have a ready made solution (flow) that you can load into your builder.

* Exit any previous NodeBuilder instances and start with a clean canvas. Check if any process is lingering from previous runs and kill it.
* Click on templates
* Select "p2p-chat"
* Highlight the newly generated tab

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FInixfu0oTzE7sRs0vfKC%2F5.gif?alt=media&#x26;token=ffc67a83-3817-496d-910b-a119338ca03b" alt=""><figcaption></figcaption></figure>

Alternatively,

* visit <https://raw.githubusercontent.com/NeuronInnovations/neuron-node-builder/refs/heads/master/templates/p2p-chat/flow.json>
* copy into your clipboard the flow code
* right click on your canvas and open the import menu

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FF35KooEQV2nQ0h83qCR4%2Fimage.png?alt=media&#x26;token=7773d09f-41aa-4394-8bf5-8a58cd9b23bf" alt="" width="375"><figcaption></figcaption></figure>

* paste your clipboard into the resulting screen

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fl5tJ2Q7LwUiWpXAnfoFz%2Fimage.png?alt=media&#x26;token=e2279119-0084-4a20-ab2a-ded66906c8c8" alt="" width="375"><figcaption></figcaption></figure>

You have now a ready made flow imported and are ready to setup a few things.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FjvGa1RC4Ol3ZsP2MMEfh%2Fimage.png?alt=media&#x26;token=2027eaa6-e3a9-46a0-a37b-dcb1628248c0" alt=""><figcaption></figcaption></figure>

### Action 2: Setup the "Chat seller config" and "Neuron P2P out"

Setup the <mark style="background-color:blue;">Chat seller config</mark> and link it with the <mark style="background-color:blue;">Neuron P2P out</mark>. If you don't know how to do this, refer to [Action 1 and Action 2 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world). Remember to hit deploy and wait for connection to become active.

Note that creating new configuration sets up new hedera and topic accounts, which costs network fees. To avoid these, prefer to reuse existing configurations by selecting one you have previously generated. You will find them in the dropdown unless these are used already in other tabs. As seen below, when selecting an existing configuration the deitals of the config are prefilled for you. Don't forget to hit the red done button to make the config stick.

![alt text](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fgit-blob-de31c19bfc6d9e9ab15f446721d9b8adcf3e004f%2Fimage-2.png?alt=media)

### Action 3: Visit localhost:1880/ui in a new tab

The template loads a chat UI which will allow you to directly talk to the bot that is installed in our discord channel.

### Action 4: Copy and communicate your EVM address

* Double click the "Chat seller config"
* Copy the EVM address into your clipboard

If you need help with this, refer to [Action 5 from the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world).

### Action 5: Go to the discord bot and send chat messages back and forth

* Goto `#node-builder-builders` on Discord <https://discord.gg/4APVGrwM>
* Type the following message:

  `/tech-support test my seller <my-evm-address>` and observe the reply thread
* Type `let us start` in the message thread and then type `All OK?` or some other message of your choice. NOTE: You need type in the message thread and not in the main chat window, otherwise the message is not procecced.
* Observe the message appearing in `localhost:1880/ui`
* Goto the UI and send messages back to discord.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FaDh5qrEendPeXuLyC33s%2F10.gif?alt=media&#x26;token=91834818-daba-4405-9310-7aa6e4a07df4" alt=""><figcaption></figcaption></figure>

:red\_circle: <mark style="color:red;">Note: the discord channel is a public channel and messages you send will be visible to other BetaOGs!</mark>

It's important to note that while Discord messages are public due to the presence of a bot acting as a neuron node, this setup allows for public interaction. However, it's entirely possible to host other neuron nodes where the communication is bidirectional, private, and encrypted, ensuring secure interactions.

## What You Just Accomplished

🎉 **Congratulations!** You've successfully:

* Built a bidirectional communication system
* Created an interactive chat-based consultancy service
* Learned how to receive and respond to buyer messages
* Experienced real-time P2P chat communication
* Understood how services can be interactive, not just data streams

## Common Problems & Solutions

**Problem:** Chat UI doesn't load at localhost:1880/ui

* **Solution:** Make sure you deployed the flow and the template loaded correctly

**Problem:** Messages don't appear in the chat UI

* **Solution:** Check that your seller is "Active" and the bot is connected

**Problem:** Can't send messages back to Discord

* **Solution:** Restart the discord sequence and write the first two messages in discord. The first one simply wakes up the bot while the second one should appear in the chat. Only type messages in the UI after messages are received from discord.

**Problem:** Bot doesn't respond to initial command

* **Solution:** Check your EVM address is copied correctly (no extra spaces), check heartbeat status.

## Key Differences from Previous Tutorials

This tutorial introduced several new concepts:

* **Bidirectional communication**: Unlike previous tutorials where you only sent data, here you both send and receive
* **Interactive services**: The service responds to buyer inputs in real-time
* **Chat interface**: You interact through a web UI rather than just automated data generation
* **Service-based selling**: You're selling your expertise/time rather than just data

## Next Steps

Ready for more advanced tutorials? Continue to:

* [Tutorial 3: Replace Human Consultant with AI](https://docs.neuron.world/node-builder-software/tutorial-3-replace-human-consultant-with-ai) - Automate your consultancy with AI


# Tutorial 3: Replace human consultant with AI

:octagonal\_sign: These tutorials are for Neuron Beta OGs, if you don't have Beta OG status in discord then you will not be able to complete this tutorial.

In the previous tutorial [buy-consultancy-via-chat](https://docs.neuron.world/node-builder-software/buy-consultancy-via-chat "mention")we designed a chat UI to reply to chat messages from a connected peer and act as consultants. In this tutorial we do something similar, the difference is that we will allow an AI agent to supply the seller's messages instead. This flow is slightly more complicated thus if you haven't followed the previous tutorial [do so now](https://docs.neuron.world/node-builder-software/buy-consultancy-via-chat) and make sure you [complete the hello world tutorial](https://docs.neuron.world/node-builder-software/your-first-program-hello-world) to be able to continue. \\

### Action 1 : Import the AI seller consultant template

* Goto "template"
* Select the template
* Click import
* Open the newly appeared tab

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FgQyc7pq0L0CSAB7LIUb5%2F11.gif?alt=media&#x26;token=cb1a1ee0-5872-4c1a-b6e3-97839fd9a107" alt=""><figcaption></figcaption></figure>

You should end up with this flow.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2F68XJbl0ap79RwLcFOtH4%2Fimage.png?alt=media&#x26;token=59c4b3fe-ad11-4025-a0e5-df88d4bf4d23" alt=""><figcaption></figcaption></figure>

### Action 2. Setup the "Consultant Seller config" and "Neuron P2P Out"

Setup the <mark style="background-color:blue;">Consultant seller config</mark> and link it with the <mark style="background-color:blue;">Neuron P2P out</mark>. If you don't know how to do this, go to [your-first-program-hello-world](https://docs.neuron.world/node-builder-software/your-first-program-hello-world "mention") . Remember to hit deploy and wait for connection to become active.

Note that creating new configuration sets up new hedera and topic accounts, which costs network fees. To avoid these, prefer to reuse existing configurations by selecting one you have previously generated. You will find them in the dropdown unless these are used already in other tabs. As seen below, when selecting an existing configuration the deitals of the config are prefilled for you. Don't forget to hit the red done button to make the config stick.

![alt text](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fgit-blob-de31c19bfc6d9e9ab15f446721d9b8adcf3e004f%2Fimage-2.png?alt=media)

You are now ready to send data into your seller via a peer to peer connection.

### Action 3: Create an account with OpenRouter and obtain a key

Go to [OpenRouter](https://openrouter.ai/) and get a free key; make sure you understand the terms and remember this is a tutorial and you should not use these examples in a production environment. Then enter they key by double clicking on the "My AI Model" node.

* Hit Done
* Hit Deploy

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FNyTequ3ig6f440rQp3JH%2Fimage.png?alt=media&#x26;token=087ad7d5-63c0-41ba-8dd4-0e743e88cd66" alt="" width="375"><figcaption></figcaption></figure>

### Action 4: Open a new browser tab at localhost:1880/ui

We will be using this chat window to monitor messages that are sent between AI agent and the buyer, but don't need to write anything in it.

### Action 5: Communicate our EVM address to the buyer in discord

* copy your EVM address by clicking the "Consultant Seller Config" node. Here's a[ reminder on how to do that.](https://docs.neuron.world/your-first-program-hello-world#action-5-communicate-our-evm-address-to-the-other-side-the-buyer)
* Goto #node-builder-builders on Discord <https://discord.gg/4APVGrwM>​ Note : the channel is a public channel and messages you send will be visible to other BetaOGs!
* Type the following message:`/tech-support test my seller <my-evm-address>`
* Click on the message thread and type in the following messages
  * Let us start chatting
  * What is your name?
* Observe the UI at localhost:1880/ui and note that the AI bot is replying to the messages received from discord! You can ask more questions by entering them on discord, just remember to give your local agent some time to have a chance to process the request and reply. \\

In the video clip, you can see the final sequence of actions unfold.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2FyMA2vFIrY8E3ch1YMLCX%2F12.gif?alt=media&#x26;token=10d2742a-2be4-4c8d-8a5c-e869261b4341" alt=""><figcaption></figcaption></figure>


# Tutorial 4: Setup a buyer node

## What You'll Learn

By the end of this tutorial, you'll have:

* ✅ Built a working Neuron buyer program for IoT data
* ✅ Created a "buyer" that receives live aviation (ADSB) data
* ✅ Connected with a seller bot on Discord
* ✅ Seen real peer-to-peer data exchange in action

## Before You Start

Make sure you have:

* ✅ Completed the [installation](https://docs.neuron.world/node-builder-software/installation "mention") tutorial
* ✅ NodeBuilder running at `http://localhost:1880`
* ✅ Your Hedera credentials saved and ready
* ✅ Discord account (you'll need Beta OG status)
* ✅ About 20 minutes of time

:octagonal\_sign: **Important:** These tutorials are for Neuron Beta OGs. If you don't have Beta OG status in Discord, you won't be able to complete this tutorial.

### Setup your environment for running in server mode

When you are buying data, your Neuron Node runs in a "server mode". This is different from when you are selling. Here's why this step is crucial for buyers:

**The seller always initiates the connection.**

You must configure port forwarding on your router to allow sellers to connect to you directly; this is necessary because sellers initiate the connection after receiving a signal from your buyer node.

**🚫 Action Required: Configure Port Forwarding**

1. Access your router's administration page.
2. Find the "Port Forwarding," "Virtual Servers," or similar section. (Consult your router's manual if you're unsure.)
3. Create a rule to forward UDP ports **61336-61346** to your computer's local IP address. Ensure the rule forwards the external ports to the same internal ports (e.g., external 61336 → internal 61336).
4. Save the changes on your router.

Once you have configured port forwarding, you can proceed to load and run the Neuron NodeBuilder software.

## What We're Building

We'll create a simple program that "buys" live aviation data (ADSB) from a seller. In this first step, we'll receive the raw data as a JSON stream and view it in our debug console.

Let's start with a clear canvas, a new flow, to build our first buyer program.

![](https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fadk0VpsMextthanPt3zq%2F3.png?alt=media\&token=962842bc-bb49-4f01-9412-e160f44b6f88)

🚀 Let's do it: Set up the backbone

### Action 1: Drag a Neuron "buyer config" node into the canvas

This node holds basic configuration data and is a one-off process you have to complete. What it does is set up account information for that particular node, which is separate from your main account (the one you created earlier upon registration).

This is similar to the seller node we created before, but this time **we need to specify who we want to buy data from**. We will use a test seller that Neuron has already set up and is driven by a bot in Discord. This seller provides a stream of ADSB data.

* <mark style="color:blue;">Double click</mark> it and
* Write a memorable name and descriptive device type entry into the relevant fields.
* Type in the following EVM address `0x343c3e6ff8C86D6745C00041D05030D87cC1cDa6` into the "sellers I want data from" field and hit the \[+Add Seller] button. This is our bot's ADSB-Seller address, which is configured to stream aviation data back to you.
* Hit the red Done button
* Deploy the builder to create it.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fgit-blob-53d74f6261319a78833b3f551753f04f4ec4b161%2Fcreate-buyer-config.gif?alt=media" alt="Creating the buyer configuration."><figcaption></figcaption></figure>

### Action 2: Check if your buyer has a heartbeat and whether the node is publicly reachable.

We need to test if the buyer config is up and running. For this, we need to make sure that it has a heartbeat and that it is a publicly reachable node.

To do so:

* Get your buyer's EVM address by double-clicking the buyer configuration
* Go to the Discord bot and type `\tech-support test my buyer's configuration at <buyer-evm-address>`
* You are expected to see the *nat-reachability status to be set to true*; otherwise, you cannot continue with the buying process.

> 💡 **Quick Reference: Discord Bot Access**
>
> The Discord bot is located in the **#node-builder-builders** channel on the Neuron Discord server.
>
> * **Discord Server:** <https://discord.gg/4APVGrwM>
> * **Channel:** #node-builder-builders
> * **Bot Commands:** Use `/tech-support` followed by your command
>
> For detailed instructions on how to interact with the Discord bot, see the [Hello World tutorial](https://docs.neuron.world/your-first-program-hello-world#action-5-communicate-our-evm-address-to-the-other-side-the-buyer) which covers Discord bot communication in detail.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fgit-blob-49bc9ccbce0d42178349e86b08a9d12be80b5e1b%2Ftest-buyer-config.gif?alt=media" alt="Testing the buyer."><figcaption></figcaption></figure>

### Action 3: Drag a "neuron p2p out" node into the canvas and connect it to a debug node and deploy

* Drag the p2p out node into the view
* Double-click it to link it to the configuration node (select the configuration node's name)
* Drag the right-hand handle to create a debug node
* Hit the deploy button
* Make sure the debug view is visible in the right-hand panel

  <figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fgit-blob-60cb814746d187404d9e489079a584a97c0f919b%2Fdebug-view.png?alt=media" alt="Testing the buyer."><figcaption></figcaption></figure>
* If the configuration node is connected to the seller node, then you should see a raw ADSB stream in your debug view.

<figure><img src="https://2242884317-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCRhLHhYFZNIUW8cgAFne%2Fuploads%2Fgit-blob-5415f4fae99f9435b4a5d760666071a4de017364%2Fbuy-adsb-raw.gif?alt=media" alt="Testing the buyer."><figcaption></figcaption></figure>

## Exercise for the Reader

🤔 **Challenge yourself to solve this step by step!**

In [Tutorial 1](https://docs.neuron.world/node-builder-software/tutorial-1-sell-jv-adsb-data), we created a solution that allows you to **sell** your ADSB data to a bot and display it on a map. Here in Tutorial 4, we did the **opposite** - we're **buying** ADSB data from a seller.

**Your Challenge:** Can you take the raw JSON data you're now receiving and display it on a map, just like we did in Tutorial 1?

### 🎯 Try to Solve It Yourself First

**Think about what you need to do:**

1. You're receiving ADSB data as JSON through your buyer node
2. You need to process this data and send it to a map visualization
3. You've seen how this works in Tutorial 1 - can you reverse-engineer the solution?

**Start by asking yourself:**

* What nodes did Tutorial 1 use to create the map?
* Can you reuse any and copy them into this solution?
* How can you connect your buyer's data output to those same visualization nodes?
* What's the difference between selling data TO a buyer vs. buying data FROM a seller?

### 🛠️ Give It Your Best Shot

Try building the solution yourself by:

* Adding the necessary nodes to process and visualize the data
* Connecting your buyer node's output to the mapping components
* Testing and debugging until you get planes showing on the map

### 🆘 If You Get Stuck...

**Only if you've tried and can't figure it out**, you can use the ready-made template:

1. Click the **"Templates"** button in NodeBuilder
2. Look for **"jetvision-buyer"** template
3. Import it to see how the complete solution works

**Or import directly from GitHub:**

* Visit: `https://raw.githubusercontent.com/NeuronInnovations/neuron-node-builder/refs/heads/master/templates/jetvision-buyer/flow.json`
* Copy the code and import it via **"Insert > Import"**

### 💡 What You'll Learn

By attempting this yourself first, you'll gain a much deeper understanding of:

* How data flows through the Neuron network
* The relationship between buyer and seller implementations
* How to build complete data processing pipelines
* The importance of understanding data flow direction

## What You Just Accomplished

You've built a complete peer-to-peer commerce system! Your program automatically:

* Listens for ADSB data being sold on the Neuron network
* Handles seller connections and data delivery
* Displays the bought data as a JSON stream in your debug console

## Common Problems & Solutions

**Problem:** Bot says "No heartbeat" or shows old timestamp

* **Solution:** Make sure you clicked "Deploy" and see "Active" status on your buyer node

**Problem:** Bot doesn't respond to commands

* **Solution:** Check your EVM address is copied correctly (no extra spaces)

**Problem:** NodeBuilder shows "Connecting..." forever

* **Solution:** Check your internet connection, try refreshing the browser, kill the process and restart

**Problem:** Can't find the Discord channel

* **Solution:** Make sure you have Beta OG status and joined the correct server

**Problem:** Reachability is false

* **Solution:** Check if your router is letting the port range through

## Next Steps

Now that you are receiving ADSB data, the next step is to visualize it. In the next tutorial, we will learn how to parse this JSON data and display the planes on a world map.


# Buy consultancy via chat

LOCKED. Tutorial release planned for Monday 5/10/2025


# Go Hedera SDK

To build the `neuron-go-hedera-sdk`, you need to ensure that you have the latest version of Go installed. You can download and install it from the [official Go GitHub releases page](https://github.com/NeuronInnovations/neuron-go-hedera-sdk).

### Steps to Build the SDK

1. **Clone the Repository**: Clone the SDK repository to your local system:

   ```bash
   git clone https://github.com/NeronInnovations/neuron-go-hedera-sdk.git
   cd neuron-go-hedera-sdk
   ```
2. **Install Dependencies**: Use go mod to download the required dependencies:

   ```bash
   go mod tidy
   ```
3. Build the SDK: Run the following command to build the SDK:

   ```bash
   go build -o neuron-sdk
   ```

   This will generate an executable file named neuron-sdk in the current directory.

## Running Your First DApp - Hello World

> **Do this first:**\
> Get test net keys by registering with [explorer.neuron.world](https://explorer.neuron.world); alternatively, if you know what you're doing, create the keys yourself.

To write a minimal decentralized application (DApp) using the `neuron-go-hedera-sdk`, you'll need to set up an environment file (`.env`) and understand the command-line flags required to run it. The `.env` file contains essential information such as keys, Hedera chain configuration (e.g., testnet), and other variables. Additionally, you'll need to be familiar with the runtime flags that configure the SDK's behavior.

In this section, we will guide you through:

1. Filling out the environment template to create your `.env` file.
2. Writing a simple "Hello World" program that includes the SDK.
3. Breaking down the components of the main program to understand how it works.
4. Running the program with the appropriate command-line parameters.

Let's get started by creating your `.env` file. Create a folder and place the a file named `.env` at the root.

```properties
private_key=
hedera_evm_id=
hedera_id=
location=
list_of_sellers=
eth_rpc_url=https://testnet.hashio.io/api
mirror_api_url=https://testnet.mirrornode.hedera.com/api/v1
neuron_explorer_url=https://explorer.neuron.world/api/v1/device/wip-all
smart_contract_address=0x87e2fc64dc1eae07300c2fc50d6700549e1632ca
```

Below is an explanation of the environment variables required for the `neuron-go-hedera-sdk`. These variables should be defined in a `.env` file to configure your application.

#### Required Environment Variables:

1. **`eth_rpc_url`**:
   * **Description**: URL of the Ethereum-compatible JSON-RPC endpoint for Hedera.
   * **Example**: `https://testnet.hashio.io/api`
   * **Purpose**: Enables the SDK to interact with Hedera's EVM layer for operations such as querying accounts.
2. **`private_key`**:
   * **Description**: Your private key in hexadecimal format. Use an secp256k1 (not DER)
   * **Example**: `83c386a507ec1de...`
   * **Purpose**: Used to sign transactions and authenticate the device account.
3. **`hedera_evm_id`**:
   * **Description**: The EVM-compatible address of your Hedera device account.
   * **Example**: `20ad40c4b874...`
   * **Purpose**: Serves as an identifier for the device account on the Hedera network.
4. **`hedera_id`**:
   * **Description**: The Hedera Account ID of your device.
   * **Example**: `0.0.1234`
   * **Purpose**: Used by Hedera APIs to identify the account associated with your device.
5. **`location`**:
   * **Description**: The approximate geographic location of your device in JSON format.
   * **Example**: `{"lat":50.1,"lon":1.8898,"alt":0.000000}`
   * **Purpose**: Helps buyers filter sellers based on geographic proximity.
6. **`list_of_sellers`**:
   * **Description**: A comma-separated list of seller public keys or peer IDs.
   * **Example**: `021789142f21495d9d3a4102fe9b21d30d4705b56272f011fa00e0ae8dce3a4751`
   * **Purpose**: Specifies named sellers that the buyer can directly interact with.
7. **`mirror_api_url`**:
   * **Description**: The API endpoint of the Hedera Mirror Node.
   * **Fixed Value**: `https://testnet.mirrornode.hedera.com/api/v1`
   * **Purpose**: Enables the SDK to query historical and real-time Hedera network data.
8. **`neuron_explorer_url`**:
   * **Description**: The API endpoint of the Neuron Explorer.
   * **Fixed Value**: `https://explorer.neuron.world/api/v1/device/wip-all`
   * **Purpose**: Used to discover available devices (peers) and their metadata.
9. **`smart_contract_address`**:
   * **Description**: The EVM-compatible address of the Neuron smart contract.
   * **Fixed Value**: `0x87e2fc64dc1eae07300c2fc50d6700549e1632ca`
   * **Purpose**: Used for interactions with the smart contract, such as registering devices or querying SLA information.

#### Optional/Derived Information:

* The `list_of_sellers` is only useful for data buyers and can be left empty if discovery is handled dynamically (see flags section)

### Minimal Main Program Example

To use the sdk you implement callbacks for the `LaunchSDK` function. T

```go
neuronsdk.LaunchSDK(
    NrnProtocol, // Specify a protocol ID
    func(envIsReady chan bool, envFile string) error {
    // Define custom key configurator logic or leave empty
    },         


    // ---------------  Buyer Callbacks	---------------			  
    func(ctx context.Context, h host.Host, b *commonlib.NodeBuffers) { 
    // Define buyer case logic here (if required)
    },
    func(msg hedera.TopicMessage) { 
    // Define buyer topic callback logic here (if required)
    },


    // ---------------  Seller Callbacks ---------------	
    func(ctx context.Context, h host.Host, b *commonlib.NodeBuffers) { 
    // Define seller case logic here (if required)
    },
    func(msg hedera.TopicMessage) {
    // Define seller topic callback logic here (if required)
    }
)

```

The first parameter is the protocol ID you will use. This should align with the SLA that your dapp will adhere to. The first callback alllows you to define a custom key configurator; this can be an UI or any other means to capture the users private key. Note private keys are not encrypted for the time being. The next pair of call backs are to define the buyer logic of your dapp; one to interact with other peers in a p2p fashion and the other one to receive messages sent to the peer's `stdIn` topic; you receive here messages that the core SDK can't handle and thus are deemed dapp-level messages. The next pair is the same but for the seller case.

Below is a minimal example of a `main.go` file that demonstrates how to import the `neuron-go-hedera-sdk`, handle flags, and launch the SDK using its core `LaunchSDK` function. The data seller in this example is simply sending the text "ping" repeateadly to whoever is connected to him / buying data from him.

```go
// main.go
package main

import (
	"bufio"
	"context"
	"fmt"
	"log"
	neuronsdk "neuron/sdk" // Import neuronFactory from neuron-go-sdk
	commonlib "neuron/sdk/common-lib"
	hedera_msg "neuron/sdk/hedera"
	"time"

	"github.com/hashgraph/hedera-sdk-go/v2"
	"github.com/libp2p/go-libp2p/core/host"
	"github.com/libp2p/go-libp2p/core/network"
	"github.com/libp2p/go-libp2p/core/protocol"
)
)

func main2() {

	var NrnProtocol = protocol.ID("/nrn-mydapp/v1")

	neuronsdk.LaunchSDK(
		NrnProtocol, // Specify a protocol ID
		nil,         // leave nil if you don't need custom key configuration logic
		func(ctx context.Context, h host.Host, b *commonlib.NodeBuffers) { // Define buyer case logic here (if required)
			h.SetStreamHandler(NrnProtocol, func(streamHandler network.Stream) {
				defer streamHandler.Close()
				// I am receiving data from the following peer
				peerID := streamHandler.Conn().RemotePeer()
				b.SetStreamHandler(peerID, &streamHandler)
				streamReader := bufio.NewReader(streamHandler)
				// print ping messages to the screen while the other side sends data
				for {
					isStreamClosed := network.Stream.Conn(streamHandler).IsClosed()
					if isStreamClosed {
						log.Println("Stream seems to be closed ...", peerID)
						break
					}
					bytesFromOtherside, err := streamReader.ReadBytes('\n')
					if err != nil {
					}
					fmt.Print("Received from ", peerID, ":", string(bytesFromOtherside))

				}
			})

		},
		func(msg hedera.TopicMessage) { // Define buyer topic callback logic here (if required)
		},
		func(ctx context.Context, h host.Host, b *commonlib.NodeBuffers) { // Define seller case logic here (if required)
			// every 10 seconds, send a ping message
			for {
				// for each connected buyer peer, send a ping message
				for peerID, bufferInfo := range b.GetBufferMap() {
					// send the private and encrypted message using the p2p streem
					sendError := commonlib.WriteAndFlushBuffer(*bufferInfo, peerID, b, []byte("ping"))
					if sendError != nil {
						//send the public connectivity error message for the other peer's sdk to handle
						hedera_msg.PeerSendErrorMessage(
							bufferInfo.RequestOrResponse.OtherStdInTopic,
							commonlib.WriteError, fmt.Sprintf("Are you online, I cannot write to you:%s", sendError),
							commonlib.SendFreshHederaRequest,
						)
						continue
					}
				}
				time.Sleep(10 * time.Second)
			}

		},
		func(msg hedera.TopicMessage) {
			// Define seller topic callback logic here (if required)
		},
	)
}
```

Notice that in the example above we define all the behaviour of the dapp at once; soon, we'll add the callback for the validator logic here too. However, the application will run in only one mode: either buyer or seller. The mode of operation can be handled by the flags defined next.

### Flags Reference

The `neuron-go-hedera-sdk` supports the following command-line flags for configuring its behavior:

#### General Flags

1. **`--mode`**
   * **Description**: Specifies whether the node should operate in "peer" mode (for regular P2P communication) or "relay" mode (to relay traffic for other peers).
   * **Default**: `peer`
   * **Example**: `--mode=peer`
2. **`--force-protocol`**
   * **Description**: Forces the application to use a specific network protocol.
   * **Options**: `udp`, `tcp` (only `udp` and `QUIC` are supported at the moment).
   * **Default**: `udp`
   * **Example**: `--force-protocol=udp`
3. **`--port`**
   * **Description**: Specifies the port the node should bind its listener to.
   * **Default**: `0` (random port) // note random port doesn't work at the moment
   * **Example**: `--port=9000`
4. **`--enable-upnp`**
   * **Description**: Enables Universal Plug and Play (UPnP) to automatically forward ports on supported routers, making the node more accessible.
   * **Default**: `false`
   * **Example**: `--enable-upnp`
5. **`--force-location`**
   * **Description**: Overrides the node's location using a JSON struct in the format: `{"lat": <latitude>, "lon": <longitude>, "alt": <altitude>}`.
   * **Default**: Not set (uses location from the environment file if available).
   * **Example**: `--force-location={"lat":50.1,"lon":1.8898,"alt":0.000000}`
6. **`--buyer-or-seller`**
   * **Description**: Specifies whether the node is operating as a "buyer" (data requester) or "seller" (data provider).
   * **Default**: Not set (must be explicitly defined).
   * **Example**: `--buyer-or-seller=buyer`
7. **`--my-public-ip`**
   * **Description**: Manually sets the public IP address of the node. Useful if automatic detection fails or a specific IP is required.
   * **Default**: Not set
   * **Example**: `--my-public-ip=192.168.1.100`
8. **`--my-public-port`**
   * **Description**: Manually sets the public port of the node. Useful for specifying externally mapped ports in NAT or firewall scenarios.
   * **Default**: Not set
   * **Example**: `--my-public-port=9000`

#### Buyer-Specific Flags

1. **`--list-of-sellers-source`**
   * **Description**: Specifies the source for obtaining the list of sellers. If 'env' is set the the sellers need to be named in the "list\_of\_sellers" environment file line.
   * **Options**:
     * `explorer`: Fetch from an external service.
     * `env`: Fetch from the environment variables.
   * **Default**: `explorer`
   * **Example**: `--list-of-sellers-source=explorer`
2. **`--radius`**

   * **Description**: Used when "explorer" is selected and specifies the radius (in kilometers) to restrict seller nodes based on their latitude and longitude.
   * **Default**: `1` (1 km radius)
   * **Example**: `--radius=10`

   To run the previous example in buyer mode do

   ```bash
      go build -o mydapp
      ./mydapp --mode=peer --buyer-or-seller=buyer --port=30088  --list-of-sellers-source=env
   ```

   To run the program as a seller, you will need a separate environment file (e.g., .env-seller) to specify the seller’s keys and configuration. The --envFile flag allows you to explicitly define which environment file to use for each instance.

   This setup makes it convenient to run both buyer and seller instances on the same machine for testing purposes. Simply specify a different --envFile value and ensure other parameters (like --port) do not conflict. This approach ensures that you can simulate both roles without any overlaps or configuration issues.

   ```bash
      go build -o mydapp
      ./mydapp --mode=peer --buyer-or-seller=seller --envFile=.env-seller --port=20088 
   ```

```mermaid

      
```


# Explorer

[Link to Github](https://github.com/NeuronInnovations/neuron-explorer)


