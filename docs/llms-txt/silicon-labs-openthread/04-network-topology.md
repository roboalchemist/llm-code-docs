# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/04-network-topology.md

# Network Topology

## Network Address and Devices

The Thread stack supports full mesh connectivity between all routers in the network. The actual topology is based on the number of routers in the network. If there is only one router, then the network forms a star. If there is more than one router then a mesh is automatically formed (see [Thread Technology Overview](./02-thread-technology-overview)).

## Mesh Networks

Embedded mesh networks make radio systems more reliable by allowing radios to relay messages for other radios. For example, if a node cannot send a message directly to another node, the embedded mesh network relays the message through one or more intermediary nodes. As discussed in section [Routing and Network Connectivity](./05-routing-and-network-connectivity), all router nodes in the Thread stack maintain routes and connectivity with each other so the mesh is constantly maintained and connected. There is a limit of 64 router addresses in the Thread network, but they cannot all be used at once. This allows time for the addresses of deleted devices to be reused.

In a mesh network, the sleepy end devices or router-eligible devices do not route for other devices. These devices send messages to a parent that is a router. This parent router handles the routing operations for its child devices.