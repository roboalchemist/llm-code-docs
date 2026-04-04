# Source: https://docs.silabs.com/openthread/3.0.0/thread-fundamentals/07-management.md

# Management

## ICMP

All devices support Internet Control Message Protocol for IPv6 (ICMPv6) error messages, as well as the echo request and echo reply messages.

## Device Management

The application layer on a device has access to a set of device management and diagnostics information that can be used locally or collected and sent to other management devices.

At the 802.15.4 PHY and MAC layers, the device provides the following information to the management layer:

- EUI 64 address
- 16-bit short address
- Capability information
- PAN ID
- Packets sent and received
- Octets sent and received
- Packets dropped on transmit or receive
- Security errors
- Number of MAC retries

## Network Management

The network layer on the device also provides information on management and diagnostics that can be used locally or sent to other management devices. The network layer provides the IPv6 address list, the neighbor and child table, and the routing table.