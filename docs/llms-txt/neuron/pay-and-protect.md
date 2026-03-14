# Source: https://docs.neuron.world/neuron-concepts/pay-and-protect.md

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
