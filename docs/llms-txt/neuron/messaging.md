# Source: https://docs.neuron.world/neuron-concepts/messaging.md

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
