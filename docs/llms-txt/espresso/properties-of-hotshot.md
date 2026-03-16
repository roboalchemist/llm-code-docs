# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/properties-of-hotshot.md

# Properties of HotShot

HotShot’s design intentionally aims to give chains fast confirmations to transactions, while being able to scale to a large number of participating nodes. However, the participating nodes do not execute transactions; hence, individual nodes only need assurance of data availability to vote in consensus, not to have full access to the data. This alleviates high hardware requirements for participation, without sacrificing throughput.

HotShot is based on the consensus techniques used within HotStuff and HotStuff-2.

{% hint style="info" %}
For more details on HotShot and EspressoDA, see our post, [*Designing the Espresso Network: Combining HotShot Consensus with Espresso's Data Availability Layer*](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu)
{% endhint %}

## Key Properties of HotShot

### Separating data availability (DA) and execution from consensus

The HotShot implementation is purpose-built for providing fast confirmations to a large number of generic chains. In particular, it does not perform execution, and the data availability requirement (i.e., ensuring the system has access to data) is handled by a separate DA solution (integrating chains can use the DA solution of their choice, but have default access to use our custom, low-cost DA layer, [EspressoDA](https://docs.espressosys.com/network/espresso-architecture/the-espresso-network/properties-of-hotshot/espresso-data-availability-layer)). This enables HotShot to process more data than typical state machine replication protocols. Such modularity also allows the use of various appropriate sub-protocols as needed.

### Scalability

HotShot relies on all-to-leader and leader-to-all communication, thus reducing the consensus communication complexity to linear in the number of nodes. Since HotShot does not require every node to get a full copy of transaction data, low consensus communication is especially important. HotShot combines this optimistically with a content delivery network (CDN) to efficiently route data and perform computation. This reduces the leader bottleneck and supports a system with a heterogeneous set of nodes, without sacrificing safety and liveness guarantees. These improvements will help HotShot to scale to thousands of nodes, such that it can be run by a large number of Ethereum validators through restaking.

### Responsiveness

HotShot is optimistically responsive and thus, under favorable conditions, commits new blocks as fast as the network allows. This ensures that the protocol’s performance is directly related to the state of the network—under optimistic conditions, the protocol can have low latency and consequently high throughput, too. In HotShot, using a CDN at the network layer synergizes with the optimistic responsiveness property to provide even better performance.
