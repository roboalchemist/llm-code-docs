# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/05-routing-and-network-connectivity.md

# Routing and Network Connectivity

The Thread network has up to 32 active routers that use next-hop routing for messages based on the routing table. The routing table is maintained by the Thread stack to ensure all routers have connectivity and up-to-date paths for any other router in the network. All routers exchange with other routers their cost of routing to other routers in the network in a compressed format using Mesh Link Establishment (MLE).

## MLE Messages

Mesh Link Establishment (MLE) messages are used to establish and configure secure radio links, detect neighboring devices, and maintain routing costs between devices in the network. MLE operates below the routing layer and uses one hop link local unicasts and multicasts between routers.

MLE messages are used to identify, configure, and secure links to neighboring devices as the topology and physical environment change. MLE is also used to distribute configuration values that are shared across the network such as the channel and Personal Area Network (PAN) ID. These messages can be forwarded with simple flooding as specified by MPL ([Multicast Protocol for Low power and Lossy Networks (MPL)](https://tools.ietf.org/html/draft-ietf-roll-trickle-mcast-11)).

MLE messages also ensure asymmetric link costs are considered when establishing routing costs between two devices. Asymmetric link costs are common in 802.15.4 networks. To ensure two-way messaging is reliable, it is important to consider bidirectional link costs.

## Route Discovery and Repair

On-demand route discovery is commonly used in low-power 802.15.4 networks. However, on-demand route discovery is costly in terms of network overhead and bandwidth because devices broadcast route discovery requests through the network. In the Thread stack, all routers exchange one-hop MLE packets containing cost information to all other routers in the network. All routers have up-to-date path cost information to any other router in the network so on-demand route discovery is not required. If a route is no longer usable, the routers can select the next most suitable route to the destination.

Routing to child devices is done by looking at the high bits of the child’s address to determine the parent router address. Once the device knows the parent router, it knows the path cost information and next hop routing information for that device.

As route cost or the network topology change, the changes propagate through the network using the MLE single-hop messages. Routing cost is based on bidirectional link quality between two devices. The link quality in each direction is based on the link margin on incoming messages from that neighboring device. This incoming Received Signal Strength Indicator (RSSI) is mapped to a link quality from 0 to 3. A value of 0 means unknown cost.

When a router receives a new MLE message from a neighbor, either it already has a neighbor table entry for the device or one is added. The MLE message contains the incoming cost from the neighbor, so this is updated in the router’s neighbor table. The MLE message also contains updated routing information for other routers which is updated in the routing table.

The number of active routers is limited to the amount of routing and cost information that can be contained in a single 802.15.4 packet. This limit is currently 32 routers.

## Routing

Devices use normal IP routing to forward packets. A routing table is populated with network addresses and the appropriate next hop.

Distance vector routing is used to get routes to addresses that are on the local network. When routing on the local network, the upper six bits of this 16-bit address define the router destination. This routing parent is then responsible for forwarding to the final destination based on the remainder of the 16-bit address.

For off network routing, a Border Router notifies the Router Leader of the particular prefixes it serves and distributes this information as network data within the MLE packets. The network data includes prefix data, which is the prefix itself, the 6LoWPAN context, the Border Routers, and the Stateless Address Autoconfiguration (SLAAC) or DHCPv6 server for that prefix. If a device is to configure an address using that prefix, it contacts the appropriate SLAAC or DHCP server for this address. The network data also includes a list of routing servers that are the 16-bit addresses of the default Border Routers.

Additionally, in a commercial space with a Thread Domain model, a Backbone Border Router notifies the router leader of the Domain Unique Prefix it serves, to indicate that this mesh is part of the larger Thread domain. The network data for this includes prefix data, 6LoWPAN context, and the border router ALOC. There are no SLAAC or DHCPv6 flags set for this prefix set, however the address assignment follows the stateless model. Additionally, there are also service and server TLVs indicating the "backbone" service capability of this border router. Duplicate address detection capability over the backbone exists for any device that registers its Domain Unique Address (DUA) with the BBR. A device’s DUA never changes over its lifetime of being part of a Thread domain. This facilitates migration across different Thread networks in a single domain and makes sure that the respective BBRs facilitate routing across multiple Thread networks. Over the backbone, standard IPv6 routing technologies such as IPv6 Neighbor Discovery (NS/NA as per RFC 4861) and Multicast Listener Discovery (MLDv2 as per RFC 3810) are used.

A Leader is designated to keep track of router-eligible devices becoming routers or allowing routers to downgrade to router-eligible devices. This Leader also assigns and manages the router addresses using CoAP. However, all information contained in this Leader is also periodically advertised to the other routers. If the Leader goes off the network, another router is elected, and takes over as Leader without user intervention.

Border Routers are responsible for handling 6LoWPAN compression or expansion and addressing to off network devices. Backbone Border Routers are responsible for handling MPL with IP-in-IP encapsulation and decapsulation for larger scope multicasts going into and out of the mesh.

For more information on Border Routers, see [Using the Silicon Labs Co-processors with the OpenThread Border Router](/openthread/3.0.0/using-sl-coprocessors-with-openthread-border-router).

## Retries and Acknowledgements

While UDP messaging is used in the Thread stack, reliable message delivery is required and completed by these lightweight mechanisms:

- MAC-level retries–each device uses MAC acknowledgements from the next hop and will retry a message at the MAC layer if the MAC ACK message is not received.
- Application-layer retries– the application layer can determine if message reliability is a critical parameter. If so, an end-to-end acknowledgement and retry protocol can be used, such as CoAP retries.