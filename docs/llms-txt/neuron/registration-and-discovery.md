# Source: https://docs.neuron.world/neuron-concepts/registration-and-discovery.md

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
