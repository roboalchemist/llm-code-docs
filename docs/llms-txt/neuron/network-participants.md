# Source: https://docs.neuron.world/neuron-concepts/network-participants.md

# Network Participants

Participants in this system are referred to as peers or agents, who either directly communicate with each other or facilitate communications. These participants can operate individually or in groups, engaging in many-to-many (MnN) interactions. Essentially, the focus is on service provider peers (sellers/producers) offering services to consumer peers (buyers/consumers). For clarity, the terms can be used interchangeably to distinguish the two sides of the transaction.

* **Buyer**: Initiates requests for services or data from sellers. The buyer uses DLT  channels (called topics)  for communication and establishes a P2P stream, an encypted high bandwidth and datarate stream, for data transfer.
* **Seller**: Responds to requests from buyers, providing the requested service or data. Sellers also use DLT  topics to send payment demands and other messages.
* **Validator**: Ensures the integrity and validity of transactions between buyers and sellers. Validators monitor  Service License Agreements (SLA), ensure compliance, and participate in escrow services.
* Relay/Support: Peers that help participant to connect in the event of limited reachability.  They either relay messages, or help peers discover the IP address and overcome NAT issues.&#x20;
* Third party observers: These do not necessary interact with peers but do observe public messages on the Distributed Ledger and provide supporting services: e.g. explorers, data analytics, etc.&#x20;
*
