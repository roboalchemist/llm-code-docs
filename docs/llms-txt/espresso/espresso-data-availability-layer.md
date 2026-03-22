# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/properties-of-hotshot/espresso-data-availability-layer.md

# EspressoDA

{% hint style="info" %}
For a detailed technical overview of EspressoDA, see [*EspressoDA: Our Three-Layered DA Solution*](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu#Part-III-EspressoDA-Our-Three-Layered-DA-Solution).
{% endhint %}

Data availability is the requirement that all transaction data included in blocks is available to every node participating in consensus before a decision can be reached. Because the amount of data can be quite large, requiring each node to download and verify the data before reaching consensus presents a fundamental bottleneck in the throughput of consensus protocols (i.e., the [data availability problem](https://ethereum.org/en/developers/docs/data-availability/#the-data-availability-problem)).

EspressoDA resolves this bottleneck while ensuring data availability via a three-layer system we've designed to balance performance and security:

* **VID Layer:** Stores erasure-coded data chunks across all nodes.
* **DA Committee Layer:** A small committee stores the full data and guarantees efficient recovery of data.
* **CDN Layer:** Uploads full data for retrieval efficiency.

### VID Layer

EspressoDA eliminates the need for each storage node to download all block data by using [Verifiable Information Dispersal](https://eprint.iacr.org/2021/1544.pdf) (VID), a technique that encodes block data into erasure-coded chunks, which are disseminated among node[^1]s in a way that recoverability is ensured. Nodes only need to store their chunk rather than the entire block. This method is more efficient than data availability sampling (DAS) as it limits unnecessary redundancies.

By using VID, EspressoDA guarantees a block will only be finalized if data is verified to be available.

### DA Committee Layer

A small DA committee, selected from the network's nodes, receives the entire data blob and allows for very fast data retrievability, with the VID protocol acting as a fallback in case the DA committee fails to make data available.

EspressoDA ensures data is made available for rollups (optimistically by the DA committee, and guaranteed through VID) without incurring the high costs of posting transactions to the Ethereum L1 (though rollups may still choose to do so). It also avoids centralized DA solutions, which allow the DA operators to freeze the rollup and censor its users.

### CDN Layer

We provide EspressoDA with web2-level performance by using a content delivery network (CDN) to quickly share a block’s data to many different nodes. It can massively accelerate data dissemination. [Benchmarks](https://docs.espressosys.com/network/releases/testnets/cappuccino-testnet-release/benchmarks) from our Cappuccino testnet show a data dissemination of around 5.7 MB/s with 100 nodes. The CDN can also help with efficient recovery of subsets of the data, such as single transactions.

Importantly, the CDN is not trusted for security and thus doesn’t present a single point of failure. EspressoDA works perfectly fine without the CDN, which is only helpful for accelerating the DA and can easily be replaced or removed.

[^1]: in Espresso, each node participating in consensus is also such a storage node
