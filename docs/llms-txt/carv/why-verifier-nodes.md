# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/why-verifier-nodes.md

# Why Verifier Nodes

CARV is renowned for developing both applications and a foundational, modular data layer protocol known as the CARV Protocol. This protocol manages end-to-end data flow, including identity aggregation through [CARV ID](https://docs.carv.io/carv-ecosystem/verifier-nodes/broken-reference) ([ERC7231](https://eips.ethereum.org/EIPS/eip-7231)), data authentication ([CARVLink](https://docs.carv.io/carv-ecosystem/verifier-nodes/broken-reference)), storage ([CARV DB](https://docs.carv.io/carv-ecosystem/verifier-nodes/broken-reference)), processing, and AI model training. Results from these processes are posted across multiple blockchains to ensure fair value distribution.

To safeguard the security, decentralization, and privacy of this complete flow, it is critical to incorporate community-operated verifier nodes. These nodes scrutinize the outcomes at each protocol layer, ensuring integrity and compliance with set standards. Currently, these nodes are primarily focused on verifying results from the data processing and AI model training layers. Computations and model training are conducted within Trusted Execution Environment (TEE) clusters to protect user data privacy. The outcomes are then recorded on the blockchain, accompanied by TEE attestation to verify that the processes are secure and private, enabling equitable redistribution of data value among various stakeholders.

However, to prevent system manipulation and ensure a fair distribution of data value, involving a third-party to verify the TEE attestation is essential. This necessity drives our active pursuit of community participation to strengthen the protocol by operating these verifier nodes.

A single honest node can detect fraudulent activity, but achieving significant enforcement against misbehaving TEE nodes and protecting user data requires that at least half of the nodes operate honestly. Therefore, establishing a decentralized network of community nodes is crucial not only for securing the protocol but also for its scalability.

Looking ahead to Q3 2024, these nodes will take on additional responsibilities such as verifying CARV DB, an Autonomous Virtual Storage (AVS) built on Eigenlayer, to ensure reliable content storage for each operator. By Q4 2024, the scope will broaden to include securing CARV Link, an on-chain Oracle/Attestation service that seamlessly imports data from both web2 and web3 sources into the CARV protocol, thereby creating value for users and businesses. Expanding our community node base is vital to support these growing responsibilities and ensure the ongoing robustness of the CARV ecosystem.

<br>
