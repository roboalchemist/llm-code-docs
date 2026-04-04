# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/03-ip-stack-fundamentals.md

# IP Stack Fundamentals

## Addressing

Devices in the Thread stack support IPv6 addressing architecture as defined in RFC 4291 ([https://tools.ietf.org/html/rfc4291](https://tools.ietf.org/html/rfc4291): _IP Version 6 Addressing Architecture_). Devices support a Unique Local Address (ULA), a Domain Unique Address (DUA) in a Thread domain model, and one or more Global Unicast Address (GUA) addresses based on their available resources.

The high-order bits of an IPv6 address specify the network and the rest specify particular addresses in that network. Thus, all the addresses in one network have the same first N bits. Those first N bits are called the "prefix". The "/64" indicates that this is an address with a 64-bit prefix. The device starting the network picks a /64 prefix that is then used throughout the network. The prefix is a ULA ([https://tools.ietf.org/html/rfc4193](https://tools.ietf.org/html/rfc4193): _Unique Local IPv6 Unicast Addresses)_. The network may also have one or more Border Router(s) that each may or may not have a /64 that can then be used to generate a ULA or GUA. The device in the network uses its EUI-64 (64-bit Extended Unique Identifier) address to derive its interface identifier as defined in Section 6 of RFC 4944 ([https://tools.ietf.org/html/rfc4944](https://tools.ietf.org/html/rfc4944): _Transmission of IPv6 Packets over IEEE 802.15.4 Networks_ ). The device will support a link local IPv6 address configured from the EUI-64 of the node as an interface identifier with the well-known link local prefix FE80::0/64 as defined in RFC 4862 ([https://tools.ietf.org/html/rfc4862](https://tools.ietf.org/html/rfc4862): _IPv6 Stateless Address Autoconfiguration)_ and RFC 4944.

The devices also support appropriate multicast addresses. This includes link-local all node multicast, link local all router multicast, solicited node multicast, and a mesh local multicast.  With the presence of a backbone border router in a domain model, devices can also support higher scope multicast addresses if they register for them.

Each device joining the network is assigned a 2-byte short address as per the IEEE 802.15.4-2006 specification. For routers, this address is assigned using the high bits in the address field. Children are then assigned a short address using their parent’s high bits and the appropriate lower bits for their address. This allows any other device in the network to understand the child’s routing location by using the high bits of its address field.

## 6LoWPAN

6LoWPAN stands for "IPv6 Over Low Power Wireless Personal Networks." The main goal of 6LoWPAN is to transmit and receive IPv6 packets over 802.15.4 links. In doing so it has to accommodate for the 802.15.4 maximum frame size sent over the air. In Ethernet links, a packet with the size of the IPv6 Maximum Transmission Unit (MTU) (1280 bytes) can be easily sent as one frame over the link. In the case of 802.15.4, 6LoWPAN acts as an adaptation layer between the IPv6 networking layer and the 802.15.4 link layer. It solves the issue of transmitting an IPv6 MTU by fragmenting the IPv6 packet at the sender and reassembling it at the receiver.

6LoWPAN also provides a compression mechanism that reduces the IPv6 header sizes sent over the air and thus reduces transmission overhead. The fewer bits that are sent over the air, the less energy is consumed by the device. Thread makes full use of these mechanisms to efficiently transmit packets over the 802.15.4 network. RFC 4944 ([](https://tools.ietf.org/html/rfc4944)) and RFC 6282 ([](https://tools.ietf.org/html/rfc6282)) describe in detail the methods by which fragmentation and header compression are accomplished.

## Link Layer Forwarding

Another important feature of the 6LoWPAN layer is link layer packet forwarding. This provides a very efficient and low overhead mechanism for forwarding multi hop packets in a mesh network. Thread uses IP layer routing with link layer packet forwarding.

Thread uses the link layer forwarding to forward packets based on the IP routing table. In order to accomplish this, the 6LoWPAN mesh header is used in each multi-hop packet (see the following figure).

![Mesh Header Format](/thread-fundamentals/0.1/images/mesh-header-format.jpg)

In Thread, the 6LoWPAN layer fills the Mesh Header information with the originator 16-bit short address and final destination 16-bit source address. The transmitter looks up the next hop 16-bit short address in the Routing Table, and then sends the 6LoWPAN frame to the next hop 16-bit short address as destination. The next hop device receives the packet, looks up the next hop in the Routing Table / Neighbor Table, decrements the hop count in the 6LoWPAN Mesh Header, and then sends the packet to the next hop or final destination 16-bit short address as destination.

## 6LoWPAN Encapsulation

6LoWPAN packets are constructed on the same principle as IPv6 packets and contain stacked headers for each added functionality. Each 6LoWPAN header is preceded by a dispatch value that identifies the type of header (see the following figure).

![General Format of a 6LoWPAN Packet](/thread-fundamentals/0.1/images/general-format-of-a-6lowpan-packet.jpg)

Thread uses the following types of 6LoWPAN headers:

- Mesh Header (used for link layer forwarding)
- Fragmentation Header (used for fragmenting the IPv6 packet into several 6LoWPAN packets)
- Header Compression Header (used for IPv6 headers compression)

The 6LoWPAN specification mandates that if more than one header is present, they must appear in the order mentioned above.

The following are examples of 6LoWPAN packets sent over the air.

In the following figure, the 6LoWPAN payload is composed of the compressed IPv6 header and the rest of the IPv6 payload.

![6LoWPAN Packet Containing IPv6 Payload with Compressed IPv6 Header](/thread-fundamentals/0.1/images/6lowpan-packet-containing-ipv6-payload-with-compressed-ipv6-header.jpg)

In the following figure, the 6LoWPAN payload contains the IPv6 header and part of the IPv6 payload.

![6LoWPAN Packet Containing Mesh Header, a Fragmentation Header, and a Compression Header](/thread-fundamentals/0.1/images/6lowpan-packet-containing-mesh-header-a-fragmentation-header-and-a-compression-header.jpg)

The rest of the payload will be transmitted in subsequent packets per the format in the following figure.

![6LoWPAN Subsequent Fragment](/thread-fundamentals/0.1/images/6lowpan-subsequent-fragment.jpg)

## ICMP

Thread devices support the Internet Control Message Protocol version 6 (ICMPv6) protocol as defined in RFC 4443, [Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6) Specification](https://datatracker.ietf.org/doc/html/rfc4443). They also support the echo request and echo reply messages.

## UDP

The Thread stack supports User Datagram Protocol (UDP) as defined in RFC 768, [User Datagram Protocol](https://datatracker.ietf.org/doc/html/rfc768).

## TCP

The Thread stack supports a Transport Control Protocol (TCP) variant called "TCPlp" (TCP Low Power) (See [usenix-NSDI20](https://www.usenix.org/system/files/nsdi20-paper-kumar.pdf)). A Thread-compliant device implements the TCP initiator and listener roles as described in:

- RFC 793, [Transmission Control Protocol](https://datatracker.ietf.org/doc/html/rfc793)
- RFC 1122, [Requirements for Internet Hosts](https://datatracker.ietf.org/doc/html/rfc1122)
- Thread Specification 1.3.0 and higher: Existing TCP implementations are typically not tuned to work optimally over wireless mesh networks and with the limited 802.15.4 frame sizes. Therefore, the specification defines those elements and parameter values required for an efficient TCP implementation over Thread Networks (see Thread Specification 1.3.0, section 6.2 TCP).

## SRP

Service Registration Protocol (SRP) as defined in [Service Registration Protocol for DNS-Based Service Discovery](https://datatracker.ietf.org/doc/html/draft-ietf-dnssd-srp)is utilized on Thread devices starting with Thread Specification 1.3.0. There must exist a Service Registry, maintained by a border router. SRP clients on the mesh network can register to offer various services. An SRP server accepts DNS-based discovery queries and additionally offers public key cryptography for security, along with other minor enhancements to better support constrained clients.