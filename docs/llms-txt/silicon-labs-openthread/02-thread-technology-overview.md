# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/02-thread-technology-overview.md

# Thread Technology Overview

## IEEE 802.15.4

The IEEE 802.15.4-2006 specification is a standard for wireless communication that defines the wireless Medium Access Control (MAC) and Physical (PHY) layers operating at 250 kbps in the 2.4 GHz band, with a roadmap to subGHz bands ([IEEE 802.15.4-2006 Specification](http://standards.ieee.org/findstds/standard/802.15.4-2006.html)). Designed with low power in mind, 802.15.4 is suitable for applications usually involving a large number of nodes.

The 802.15.4 MAC layer is used for basic message handling and congestion control. This MAC layer includes a Carrier Sense Multiple Access (CSMA) mechanism for devices to listen for a clear channel, as well as a link layer to handle retries and acknowledgement of messages for reliable communications between adjacent devices. MAC layer encryption is used on messages based on keys established and configured by the higher layers of the software stack. The network layer builds on these underlying mechanisms to provide reliable end-to-end communications in the network.

Starting with Thread Specification 1.2, several optimizations from the IEEE 802.15.4-2015 specification have been implemented to make Thread networks more robust, responsive and scalable:

- **Enhanced Frame Pending**: Improves the battery life and responsiveness of a sleepy end device (SED), by reducing the number of messages a SED can send over the air. Any data packet that arrives from an SED (not just data requests) can be acknowledged with the presence of upcoming pending data.
- **Enhanced Keepalive**: Reduces the amount of traffic required to maintain a link between a SED and a parent by treating any data message as a keepalive network transmission.
- **Coordinated Sampled Listening (CSL)**: This [IEEE 802.15.4-2015 Specification](https://standards.ieee.org/standard/802_15_4-2015.html) feature allows for better synchronization between a SED and a parent by scheduling synchronized transmit/receive periods without periodic data requests. This enables low-power devices that have low link latency and a network with a lower chance of message collisions.
- **Enhanced ACK Probing**: This [IEEE 802.15.4-2015 Specification](https://standards.ieee.org/standard/802_15_4-2015.html) feature allows an initiator granular control over link metric queries while saving energy by reusing regular data traffic patterns rather than separate probe messages.

## Thread Network Architecture

### Residential Architecture

Users communicate with a residential Thread network from their own device (smartphone, tablet, or computer) via Wi-Fi on their Home Area Network (HAN) or using a cloud-based application. The following figure illustrates the key device types in the Thread network architecture.

![Thread Network Architecture](/thread-fundamentals/0.1/images/thread-network-architecture.png)

The following device types are included in a Thread network, starting from the Wi-Fi network:

- **Border Routers** provide connectivity from the 802.15.4 network to adjacent networks on other physical layers (Wi-Fi, Ethernet, etc.). Border Routers provide services for devices within the 802.15.4 network, including routing services and service discovery for off network operations. There may be one or more Border Routers in a Thread network.
- A **Leader**, in a Thread network partition, manages a registry of assigned router IDs and accepts requests from router-eligible end devices (REEDs) to become routers. The Leader decides which should be routers, and the Leader, like all routers in a Thread network, can also have device-end children. The Leader also assigns and manages router addresses using CoAP (Constrained Application Protocol). However, all information contained in the Leader is present in the other Thread Routers. So, if the Leader fails or loses connectivity with the Thread network, another Thread Router is elected, and takes over as Leader without user intervention.
- **Thread Routers** provide routing services to network devices. Thread Routers also provide joining and security services for devices trying to join the network. Thread Routers are not designed to sleep and can downgrade their functionality and become REEDs.
- **REEDs** can become a Thread Router or a Leader, but not necessarily a Border Router that has special properties, such as multiple interfaces. Because of the network topology or other conditions, REEDs do not act as routers. REEDs do not relay messages or provide joining or security services for other devices in the network. The network manages and promotes router-eligible devices to routers if necessary, without user interaction.
- **End devices** that are not router-eligible can be either FEDs (full end devices) or MEDs (minimal end devices). MEDs do not need to explicitly synchronize with their parent to communicate.
- **Sleepy end devices** (SEDs) communicate only through their Thread Router parent and cannot relay messages for other devices.
- **Synchronized Sleepy End Devices** (SSEDs) are a class of Sleepy End Devices that use CSL from IEEE 802.15.4-2015 to maintain a synchronized schedule with a parent, avoiding the use of regular data requests.

### Commercial Architecture

The Thread Commercial model takes the key device types for a residential network and adds new concepts. Users communicate with a commercial network through devices (smartphone, tablet, or computer) via Wi-Fi or through their enterprise network. The following figure illustrates a commercial network topology.

![Commercial Network Topology](/thread-fundamentals/0.1/images/commercial-network-topology.png)

The concepts are:

- The **Thread Domain model** supports seamless integration of multiple Thread Networks as well as seamless interface to non-Thread IPv6 networks. The main benefit of the Thread Domain is that devices are to some extent flexible to join any available Thread Network configured with a common Thread Domain, which reduces the need for manual network planning or costly manual reconfigurations when network size or data volume are scaled up.
- **Backbone Border Routers** (BBRs) are a class of Border Router in the commercial space which facilitate Thread Domain synchronization of multiple network segments and allow large scope multicast propagation into and out of each single mesh in a Thread Domain. A Thread network that is part of a larger domain must have at least one "Primary" BBR and can have multiple "Secondary" BBRs for fail-safe redundancy. The BBRs communicate with each other over a backbone which connects all the Thread networks.
- A **Backbone Link** is a non-Thread IPv6 link to which a BBR connects using an external interface used to implement the Thread Backbone Link Protocol (TBLP) to synchronize with other BBRs.
- Thread Devices in a commercial implementation are configured using Thread Domains and **Domain Unique Addresses** (DUAs). A device’s DUA never changes over its lifetime of being part of a Thread domain. This facilitates migration across different Thread networks in a single domain and makes sure that the respective BBRs facilitate routing across multiple Thread networks.

These concepts are illustrated in the following figure:

![Thread Domain Model](/thread-fundamentals/0.1/images/thread-domain-model.png)

## No Single Point of Failure

The Thread stack is designed to not have a single point of failure. While there are a number of devices in the system that perform special functions, Thread is designed so they can be replaced without impacting the ongoing operation of the network or devices. For example, a sleepy end device requires a parent for communications, so this parent represents a single point of failure for its communications. However, the sleepy end device can and will select another parent if its parent is unavailable. This transition should not be visible to the user.

While the system is designed for no single point of failure, under certain topologies there will be individual devices that do not have backup capabilities. For example, in a system with a single Border Router, if the Border Router loses power, there is no means to switch to an alternative Border Router.  In this scenario, a reconfiguration of the Border Router must take place.

Starting with Thread Specification 1.3.0, Border Routers sharing an infrastructure link can facilitate no-single point of failure across a different medium (such as Wi-Fi or Ethernet) by utilizing a Thread Radio Encapsulation Link (TREL). With this feature, the probability of Thread partitions forming across links is reduced.
