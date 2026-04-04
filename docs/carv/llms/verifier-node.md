# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/how-do-verifier-nodes-work/verifier-node.md

# Verifier Node

* Any address holding a CARV NFT License, or delegated by an address holding a CARV NFT License, can become a verifier node.
* Each node has a delegation weight (initially set to 100, with an upper limit adjustable by the admin). The delegation weight represents the number of delegations to that node.
* Before a verifier node can publish a verification, it must notify the service contract to go online. The first time each verifier node goes online, it is registered with a uint16 nodeID, with the system capable of registering up to 65,535 nodes.
* After each attestation is published, Chainlink VRF will select the verification nodes for that round from the currently online nodes. The nodeID list of selected verification nodes will be stored in the service contract. When a verifier submits a verification, the contract will check if it is on the current round's verification node list.
* To randomly select verifier nodes from the pool of active nodes, the Service contract maintains a list called **activeVrfNodeList**, which has an initial maximum size of **5,000 nodes** (this limit is a governance parameter and can be adjusted). When the list is full, any new node entering the pool must replace an existing node with a lower delegation weight.
* Nodes that are online for at least 6 hours daily are eligible for rewards (refer to the [rewards](https://docs.carv.io/carv-ecosystem/verifier-nodes/how-do-verifier-nodes-work/rewards "mention") rules section for details). Delegators to these nodes can also receive rewards.
* If a node fails to submit a verification, anyone can initiate a **slash** against it (the slasher will receive a reward). If the node fails to submit verifications multiple times (initially set to **2 missed submissions**, adjustable via governance), the node will be forced offline.
* When a verifier node submits a verification, it can delegate the submission process to the **CARV backend**. This submission process is **gasless**, requiring the verifier only to provide an **EIP-712 signature**. The CARV backend will aggregate multiple verifications and submit them in batches, significantly reducing the system's gas costs.

{% hint style="info" %}
Gasless mode is optional. You can always submit the tx to the smart contract directly.
{% endhint %}

* **Commission** is adjustable and can be configured by the verifier. The adjustment range is limited to **5% per change**, with a **minimum adjustment period of one week** (both parameters are subject to governance).
* A verifier node can specify a **reward receiving address**. Both the **verifier address** and the **reward address** are eligible to receive the node’s rewards.
