# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/06-joining-and-network-operation.md

# Joining and Network Operation

Thread allows two joining methods:

- Share commissioning information directly to a device using an out-of-band method. This allows steering the device to the proper network using this information.
- Establish a commissioning session between a joining device and a commissioning application on a smartphone, tablet, or the web.
- For a commercial network with a Thread domain model, an Autonomous Enrollment process without user intervention that provisions operational certificates on joiners after authentication is specified by Thread Specification 1.2. The operational certificate encodes the domain information for the device and allows secure Network Master Key provision. This model requires a registrar or Thread Registrar Interface (TRI) on a backbone border router and facilitates communication with an external authority (MASA) using the ANIMA/BRSKI/EST protocols. A network that supports this commissioning model is called a CCM network.

For more information on commissioning Thread networks, see [Device Commissioning](./11-device-commissioning).

The frequently used 802.15.4 method of joining with the permit joining flag in the beacon payload is not used in Thread networks. This method is most commonly used for push button type joining where there is no user interface or out-of-band channel to devices. This method has issues with device steering in situations where there are multiple networks available and it can also pose security risks.

In Thread networks, all joining is user-initiated. After joining, a security authentication is completed at the application level with a commissioning device. This security authentication is discussed in [Security](./09-security).

Devices join a network as either a sleepy end device, end device (MED or FED), or a REED. Only after a REED has joined and learned the network configuration can it potentially request to become a Thread Router. Upon joining, a device is provided a 16-bit short address based on its parent. If a router-eligible device becomes a Thread Router, it is assigned a router address by the Leader. Duplicate address detection for Thread Routers is ensured by the centralized router address distribution mechanism which resides on the Leader. The parent is responsible for avoiding duplicate addresses for host devices because it assigns addresses to them upon joining.

## Network Discovery

Network discovery is used by a joining device to determine what 802.15.4 networks are within radio range. The device scans all channels, issues an MLE discovery request on each channel, and waits for MLE discovery responses. The 802.15.4 MLE discovery response contains a payload with network parameters, including the network Service Set Identifier (SSID), extended PAN ID, and other values that indicate if the network is accepting new members and whether it supports native commissioning.

Network discovery is not required if the device has been commissioned onto the network because it knows the channel and extended PAN ID for the network. These devices then attach to the network using the commissioning material provided.

## MLE Data

Once a device has attached to a network, there is a variety of information required for it to participate in the network. MLE provides services for a device to send a unicast to a neighboring device to request network parameters and update link costs to neighbors. When a new device joins, it also conducts a challenge response to set security frame counters as discussed in [Security](./09-security).

All devices support transmission and reception of MLE link configuration messages. This includes "link request", "link accept", and "link accept and request" messages.

The MLE exchange is used to configure or exchange the following information:

- The 16-bit short and 64-bit EUI 64 long address of neighboring devices
- Device capabilities information, including if it is a sleepy end device and the sleep cycle of the device
- Neighbor link costs if a Thread Router
- Security material and frame counters between devices
- Routing costs to all other Thread Routers in the network
- Collecting and distributing Link Metrics about various link configuration values

> **Note**:  MLE messages are encrypted except during the initial node bootstrapping operations when the new device has not obtained the security material.

## CoAP

Constrained Application Protocol (CoAP) as defined in RFC 7252 ([https://tools.ietf.org/html/rfc7252](https://tools.ietf.org/html/rfc7252): _The Constrained Application Protocol (CoAP)_) is a specialized transport protocol for use with constrained nodes and low-power networks. CoAP provides a request/response interaction model between application endpoints, supports built-in discovery of services and resources, and includes key concepts of the web such as URLs. CoAP is used in Thread to configure mesh-local addresses and multicast addresses required by devices. Additionally, CoAP is also used for management messages such as to get and set diagnostic information and other network data on active Thread routers.

## DHCPv6

DHCPv6 as defined in RFC 3315 is used as a client-server protocol to manage configuration of devices within the network. DHCPv6 uses UDP to request data from a DHCP server ([https://www.ietf.org/rfc/rfc3315.txt](https://www.ietf.org/rfc/rfc3315.txt): _Dynamic Host Configuration Protocol for IPv6 (DHCPv6)_).

The DHCPv6 service is used for configuration of:

- Network addresses
- Multicast addresses required by devices

Because short addresses are assigned from the server using DHCPv6, duplicate address detection is not required. DHCPv6 is also used by Border Routers that are assigning addresses based on the prefix they provide.

## SLAAC

SLAAC (Stateless Address Autoconfiguration) as defined in RFC 4862 ([https://tools.ietf.org/html/rfc4862](https://tools.ietf.org/html/rfc4862): _IPv6 Stateless Address Autoconfiguration_) is a method in which a Border Router assigns a prefix, and then the last 64 bits of its address are derived by the router. The IPv6 stateless autoconfiguration mechanism requires no manual configuration of hosts, minimal (if any) configuration of routers, and no additional servers. The stateless mechanism allows a host to generate its own addresses using a combination of locally available information and information advertised by routers.

## SRP

Service Registration Protocol (SRP) as defined in [Service Registration Protocol for DNS-Based Service Discovery](https://datatracker.ietf.org/doc/html/draft-ietf-dnssd-srp) is utilized on Thread devices starting with Thread Specification 1.3.0. There must exist a Service Registry, maintained by a border router. SRP clients on the mesh network can register to offer various services. An SRP server accepts DNS-based discovery queries and additionally offers public key cryptography for security, along with other minor enhancements to better support constrained clients.