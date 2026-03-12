# Source: https://docs.meson.fi/protocol/system-design/relayer.md

# Relayer

{% hint style="info" %}
The relayer service will be continuously updated in the future to ensure high availability and robustness as the number of users and swap volumes increases.
{% endhint %}

When a user submits a swap request or a release signature, the data needs to be broadcast to the LP network. The relayer service will be responsible for broadcasting users’ swaps. Specifically, it will transmit swap information with request or release signatures to LPs who submit transactions to the blockchain. However, the service does not check the validity of the data, so it is up to the [LP service](https://docs.meson.fi/protocol/system-design/lp-service) to check of the swap information and signatures after receiving the data.

In Meson, we want to build an effective relay network to guarantee swap information will be efficiently transmitted. In order to achieve this target, our so-called relayer service is not a single service, but a mixture of various schemes. Multiple copies of the relayer are run distributedly, and each one will communicate with others for data synchronization. Users can choose to submit data to any relayer, and LPs can choose to listen to the right relayer based on geographic location and network latency. According to CAP theorem, under the premise of partitioning only one of availability and consistency can be achieved. Our relayer service will prioritize availability, so the data on different relayers may be inconsistent, meaning that a single relayer service cannot guarantee that all swap requests are received on time. This has less impact on users and LPs because we only need to ensure that once a user submits a request, *some* LPs will receive the data and match the swap.

The design goals of the relayer service are:

* **High availability:** users can use this service at any time;
* **Censorship free:** no one can block the transfer of information;
* **Guaranteed delivery:** within a certain period of time, the information must be delivered;
* **Fault tolerance:** we don't assume any service will work perfectly as designed so we will provide ample alternatives.

To achieve these goals, our relayer service integrates the following solutions

* Decentralized p2p network
* Distributed service
* Direct on-chain operation

### Peer-to-peer network

Decentralized p2p network can provide very good availability and accept any submitted data without censorship. Blockchain transactions are usually transmitted using p2p networks, proving their advantages in this regard. We will use a p2p network as the main route for swap propagation. Users can submit swap information and signatures to one or more nodes, and peers will be responsible for synchronizing the information to the entire network. LPs can listen to any node and get swap data submitted by users.

The p2p network does not guarantee data consistency, which may cause swaps seen by different peers and LPs to be different. This will not be a problem because when conflicting swaps are submitted to the blockchain, the consensus algorithm on-chain will ensure that only one can be finally confirmed.

However, a decentralized network does not guarantee the timing of data delivery. We want to ensure that swaps can be processed quickly, so this issues needs to be properly handled and optimized. The partial centralized service that will be introduced below will address this issue and accelerate information transmission.

While a fully distributed p2p network has many advantages, there are also many challenges to running such a network. A p2p network that just starts running usually has problems with stability due to lack of enough peers. Availability and efficiency may be low, and data synchronization and delivery are not sufficiently assured. This is another reason we designed partial centralized services.

### Partial centralized service (c-relayer)

A trusted centralized service can easily guarantee high availability and efficient data access. Therefore, we will build and run a centralized service, named c-relayer. which will accept user’s swap requests and signatures, let LPs obtain swap information, and synchronize swaps through the p2p network. C-relayer is partially centralized because others can also run it and users can submit swaps to anyone or more of them. Each c-relayer will maintain swaps it receives from users and synchronizes them over the p2p network (or through direct connections to other c-relayers). Instead of listening to the p2p network, LPs can also listen to c-relayers, presumably more than one to ensure that as many swaps as possible can be obtained.

Running the c-relayer also requires a database to store past swap information and provide APIs for historical swap records. Meson's swap explorer will render swap history based on the c-relayer we host, which will store and index all historical data. For self-hosted c-relayers, expired swaps can be cleared to reduce the burden of running c-relayer.

At the beginning of the p2p network formation process, c-relayers will provide reliable services to users and LPs. While the p2p network is growing, the c-relayer can also continue to run and provide more efficient swap processing. At that time, c-relayers will gradually integrate with the p2p network and become a part of the network. In other words, c-relayer will evolve into full-nodes in the p2p network, providing more functions such as API and data backup. Ordinary peers will become light-nodes which only provide basic broadcast features.

### Direct on-chain operation

In addition, meson also provides a route of directly interacting with on-chain contracts and completing transactions. In this process, the user's swap will be directly submitted to the blockchain, passing through the chain's own p2p network before packed into blocks. LPs may need to access some swap information and they can listen to the blockchain mempool or watch for recent blocks to extract swaps executed on meson. The shortcoming of direct on-chain execution is that users need to have wallets on both initial and target chains, and pay gas fees for transactions, but they can ensure the swap will be executed on-chain immediately. This scheme is more complicated in terms of user interaction, but we keep this as a backup plan to handle swaps.
