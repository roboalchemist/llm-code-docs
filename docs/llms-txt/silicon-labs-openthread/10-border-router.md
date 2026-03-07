# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/10-border-router.md

# Border Router

A Thread Border Router is a device that connects a Thread wireless network to other IP-based networks (such as Wi-Fi or Ethernet) in the outside world via a local home or enterprise network. Unlike gateways in other wireless solutions, it is fully transparent to the transport and application protocols that reside above the network layer. As a result, applications can communicate securely from end-to-end without any application layer translation.

A Thread Border Router minimally supports the following functions:

- End-to-end IP connectivity via routing between Thread devices and other external IP networks.
- External Thread Commissioning (for example, a mobile phone) to authenticate and join a Thread device to a Thread network.

There can be multiple Border Routers in a network, eliminating a "single point of failure" in the event one of them malfunctions. The Border Router enables every Thread device to directly connect to global cloud services, when enterprise networks run IPv6 and IPv4, or IPv4 only.

## Border Router Features for Off-Mesh Communication

Thread can be immediately implemented in current working situations, before partial or full transition to IPv6 and Thread enables IPv4 backwards compatibility using Network Address Translation (NAT). NAT64 translates IPv6 packets to IPv4, and NAT64 translates IPv4 packets to IPv6. A Thread Border Router can function as an IPv4 host on the wide area network (WAN), capable of obtaining an IPv4 interface and router address. It can acquire an address using DHCP from an IPv4 address pool. The Thread Border Router may also implement Port Control Protocol (PCP) to control how incoming IPv4 packets are translated and forwarded and support static mappings. Most of the IPv4 to IPv6 (and vice versa) translations can be handled by the Thread Border Router, with minimal changes needed to an existing network.

Additionally, Thread Border Routers support bidirectional IPv6 connectivity with IPv6 neighbor discovery, router advertisements, multicast discovery, and packet forwarding.

## Thread over Infrastructure

Thread Networks automatically organize into separate Thread Network Partitions when there is no connectivity between two or more sets of devices. Thread Partitions allow devices to maintain communication with other devices in the same Thread Partition but not with Thread Devices in other partitions.

Thread over Infrastructure allows Thread devices to incorporate IP-based link technologies (for example, Wi-Fi and Ethernet) into the Thread topology. These additional Thread links over other link technologies reduce the probability of occurrence of multiple Thread Network Partitions, while backward-compatibility with existing Thread 1.1 and 1.2 devices is guaranteed. These benefits are obtained for any network topology that includes at least two Border Routers connected via a shared adjacent infrastructure link.

For more information, refer to Thread Specification 1.4.0, Chapter 15 (Thread over Infrastructure).

## OpenThread Border Router

OpenThread's implementation of a Border Router is called an OpenThread Border Router (OTBR). It supports a mesh interface using Radio co-processor (RCP) or a Network co-processor (NCP) models. Silicon Labs provides an implementation (supported on the Raspberry Pi) and source code as part of the Silicon Labs GSDK. For more information, see [Using the Silicon Labs Co-processors with the OpenThread Border Router](/openthread/3.0.0/using-sl-coprocessors-with-openthread-border-router).

Documentation on the setup and architecture of the OTBR is available at [https://openthread.io/guides/border-router](https://openthread.io/guides/border-router).