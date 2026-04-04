# Source: https://io.net/docs/guides/architecture/io-network.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# IO Network

> This article explores the concepts of mesh VPN networks and how we leverage their benefits to improve performance and reliability in the io.net protocol.

**IO Network** is a cutting-edge networking backend that utilizes a secured mesh VPN to allow ultra-low latency communication between the antMiners nodes or 'workers'.

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5bd43f5-cluster.png?fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=0a8fc4ae52a6dd96112f3ba55f7704fa" alt="" data-og-width="2360" width="2360" data-og-height="2160" height="2160" data-path="images/docs/5bd43f5-cluster.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5bd43f5-cluster.png?w=280&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=8f9fe07448d5e45e00eeedbb0653a7dd 280w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5bd43f5-cluster.png?w=560&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=42c8d9b82620b3c2a5bbbb507c2486ff 560w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5bd43f5-cluster.png?w=840&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=0bd68f04601a5d2c9a291be89f22f49c 840w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5bd43f5-cluster.png?w=1100&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=b2b0e5531f2f66d4f193db61d5b8f08e 1100w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5bd43f5-cluster.png?w=1650&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=2383917b844403e911eaab203c135e47 1650w, https://mintcdn.com/ionet-cca8037f/H3cruHjLxCt9GNvH/images/docs/5bd43f5-cluster.png?w=2500&fit=max&auto=format&n=H3cruHjLxCt9GNvH&q=85&s=9baa911c71b07f13121c7088224e0d5c 2500w" />
</Frame>

### Understanding Mesh VPN Networks

A *Mesh VPN network* is a type of virtual private network (VPN) that connects nodes in a non-hierarchical, decentralized manner. Unlike traditional hub-and-spoke VPN architectures, which rely on a central concentrator or gateway, mesh VPN networks allow each node to connect directly to every other node in the network. This structure ensures data packets can travel along multiple paths, increasing redundancy, fault tolerance, and better load distribution.

<Frame caption="Mesh VPN">
    <img src="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c03fca9-2_1.png?fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=3ba7535bddc81c08f5507499189ebcdd" alt="" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/docs/c03fca9-2_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c03fca9-2_1.png?w=280&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=6dff405ca020816f0da3419257660b8c 280w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c03fca9-2_1.png?w=560&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=ab579b5e96a6e76fa1621c97fba200ca 560w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c03fca9-2_1.png?w=840&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=15b225e0b168d04cce347fe251ada5a3 840w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c03fca9-2_1.png?w=1100&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=d36f35570e458cef63ab7f93c6937189 1100w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c03fca9-2_1.png?w=1650&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=c6cf151addb6442448a088e0927339e1 1650w, https://mintcdn.com/ionet-cca8037f/4P4zg-ApBHAWcHCz/images/docs/c03fca9-2_1.png?w=2500&fit=max&auto=format&n=4P4zg-ApBHAWcHCz&q=85&s=274782f67251c5d01b8143ce5a9c31b0 2500w" />
</Frame>

<Frame caption="Hub-and-spoke VPN ( legacy - slow )">
    <img src="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cb54a4-3_1.png?fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=1a2bacb2baa2a840c59aa5fd52b29cb7" alt="" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/docs/8cb54a4-3_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cb54a4-3_1.png?w=280&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=fc092d6d2fbc36fee1747dde9cbe63dd 280w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cb54a4-3_1.png?w=560&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=8131f51cb49111cbe2e5132edd88c0b6 560w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cb54a4-3_1.png?w=840&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=8b1e87dabc1dfc37eddad666a8dd7088 840w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cb54a4-3_1.png?w=1100&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=d2a904578389756d3a8125e4416f3a7f 1100w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cb54a4-3_1.png?w=1650&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=a251aeb1ec6c3ef3e8fbc0e4508e8e26 1650w, https://mintcdn.com/ionet-cca8037f/6jhzMWiJ6_JlNBB6/images/docs/8cb54a4-3_1.png?w=2500&fit=max&auto=format&n=6jhzMWiJ6_JlNBB6&q=85&s=9103b49a1fa8b8dbda5c3872b168c72f 2500w" />
</Frame>

#### Advantages of *Mesh VPN networks*:

1. **Robust**: Mesh networks are resilient to individual node failures, as there are multiple paths for data to travel. This redundancy ensures that the network remains operational when one or more nodes experience issues.
2. **Scalability**: Adding new nodes to a mesh network does not significantly impact the overall network performance, making it easy to expand the network as needed.
3. **Low Latency**: By connecting nodes directly, mesh networks reduce the number of *hops* needed for data to travel between nodes. This reduction in latency enhances the performance of real-time applications and distributed computing.
4. **Optimized Load Distribution**: Mesh networks distribute traffic more evenly across nodes, preventing bottlenecks and ensuring optimal performance.

### Implementation of the *io.net Network*

We built an io.net network that creates an efficient, resilient, and scalable networking backend. By adopting mesh networking principles, io.net delivers the following benefits to its users:

1. **Enhanced Performance**: io.net's mesh network architecture minimizes latency by allowing data to travel along the most efficient paths, optimizing application performance and user experience.
2. **Improved Resilience**: The decentralized nature of io.net's mesh network ensures that it remains operational even when individual nodes fail. This resilience translates to increased reliability and uptime for users.
3. **Seamless Scalability**: io.net's mesh network can easily grow to accommodate more nodes as the user base expands, ensuring consistent performance and adaptability.
4. **Distributed Computing**: By allowing direct connections between nodes, io.net's mesh network facilitates efficient distributed computing, which enables resource sharing and collaborative processing across the network.

### Decentralized Architecture and Privacy

The decentralized nature of mesh VPN networks contributes to their security and privacy. Some notable aspects include:

1. **No Single Points of Failure**: The absence of a central concentrator or gateway in mesh VPN networks eliminates the risk of a single point of failure, ensuring that the network remains operational even if individual nodes are compromised or experience issues.
2. **Anonymity**: Since data travels along multiple paths within the mesh network, it becomes more difficult for an attacker to trace the origin or destination of the data, enhancing privacy for users.
3. **Traffic Obfuscation**: Mesh VPN networks can employ techniques like packet padding and timing obfuscation to make it harder for eavesdroppers to analyze traffic patterns and identify specific users or data streams.

### Network Access Control and Monitoring

Next for io.net Network includes:

1. **Access Control Lists (ACLs)**: Nodes must define and enforce ACLs to restrict communication between specific nodes or groups of nodes, ensuring that sensitive data is only accessible to authorized parties and only available during the time they are hired for a specific cluster.
2. **Regular Auditing and Logging**: To maintain security and compliance, the io.net mesh VPN must be configured to allow us to perform regular audits and maintain logs of network activities, enabling administrators to identify and address potential vulnerabilities or breaches.
