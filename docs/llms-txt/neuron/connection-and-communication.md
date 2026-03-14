# Source: https://docs.neuron.world/neuron-concepts/connection-and-communication.md

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
