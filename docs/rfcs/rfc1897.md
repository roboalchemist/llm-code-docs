---
rfc: 1897
title: "IPv6 Testing Address Allocation"
date: January 1996
category: Experimental
---

## 1.0. Introduction

This document describes an allocation plan for IPv6 addresses to be
used in testing IPv6 prototype software.  These addresses are
temporary and will be reclaimed in the future.  Any IPv6 system using
these addresses will have to renumber at some time in the future.
These addresses will not to be routable in the Internet other than
for IPv6 testing.

The addresses described in this document are consistent with the IPv6
Addressing Architecture [ARCH].  They may be assigned to nodes
manually, with IPv6 Auto Address Allocation [AUTO], or with DHCP for
IPv6 [DHCPv6].

## 2.0. Address Format

The address format for the IPv6 test address is consistent with the
provider-based unicast address allocation [PRVD] which is as follows:

| 3 |  5 bits  |  16 bits | 8 |   24 bits  | 8 |    64 bits     |
+---+----------+----------+---+------------+---+----------------+
|010|RegistryID|ProviderID|RES|SubscriberID|RES|Intra-Subscriber|
+---+----------+----------+---+------------+---+----------------+

The specific allocation of each field of the test address format is
as follows:

| 3 |  5 bits  |  16 bits | 8 |   24 bits  | 8 | 16 bits|48 bits|
+---+----------+----------+---+------------+---+--------+-------+
|   |          |Autonomous|   |    IPv4    |   | Subnet | Intf. |
|010|  11111   |  System  |RES|   Network  |RES|        |       |
|   |          |  Number  |   |   Address  |   | Address|  ID   |
+---+----------+----------+---+------------+---+--------+-------+

where:

This is the Format Prefix used to identify provider-based
unicast addresses.

This is a Registry ID reserved by the IANA.  The initial use of
addresses in this Registry ID for IPv6 testing is temporary.
All users of these addresses will be required to renumber at
some time in the future.

Autonomous System Number

This is the current autonomous system number assigned to the
provider providing internet service to the an IPv6 testers
organization.  For example for IPv6 testers receiving internet
service from BBN Barrnet would use autonomous system number 189.
This would be coded in the autonomous system field of the
address as follows:

0000 0000 1011 1101 (binary)

The values for the autonomous system number of an organization's
provider can be obtained from that provider, or can be looked up
in the "whois" database maintained by the internic.net.

RES

This field is reserved and must be set to zero.

IPv4 Network Address

This is based on the current IPv4 routable address for the
subscriber which the interface is connected.  It is formed by
taking the high order 24 bits of the IPv4 address.  For example
for an IPv4 address (in IPv4 syntax):

IPv4 Address
------------
39.11.22.1

the value to put in this field of IPv6 address is:

IPv4 Format             Hex
------------            ------
39.11.22                270B16

This technique for generating values for this field only works
for subscribers which have IPv4 subscriber prefixes less than
equal to 24 bits long.  There may be subscribers using IPv4
addresses with longer subscriber prefixes, but this conflict is
expected to be very rare.  Subscribers with subscriber prefixes
larger than 24 bits should use the remaining bits in the IPv4
prefix as the high order bits in the Subnet Address field.

RES

This field is reserved and must be set to zero.

Subnet Address

The Subnet ID identifies a specific physical link on which the
interface is located.  There can be multiple subnets on the same
physical link.  A specific subnet can not span multiple physical
links.  The assignment of values for this field is left to an
individual subscriber.  One possible algorithm to generate
values for this field is to use the bits in the IPv4 address
which identify the IPv4 subnet.

Interface ID

This is the unique identifier of the interface on the link,
usually the 48-bit IEEE 802 MAC address of the interface if
available.

## 4.0. References

[ARCH]  Hinden, R., and S. Deering, Editors, "IP Version 6
Addressing Architecture", RFC 1884, Ipsilon Networks, Xerox
PARC, December 1995.

[AUTO]  Thomson, S., "IPv6 Stateless Address Autoconfiguration",
Work in Progress.

[DHCP6] Bound, J., "Host Configuration Protocol for IPv6", Work
in Progress.

[PROV]  Rekhter, Y., and P. Lothberg, "An IPv6 Provider-Based
Unicast Address Format", Work in Progress.

## 5.0. Security Considerations

Security issues are not discussed in this memo.

## 6.0. Authors' Addresses

Robert M. Hinden
Ipsilon Networks, Inc.
2191 E. Bayshore Road, Suite 100
Palo Alto, CA 94303
USA

Phone: +1 415 846 4604
Fax:   +1 415 855 1414
EMail: hinden@ipsilon.com

Jon Postel
Information Sciences Institute
4676 Admiralty Way
Marina del Rey, CA 90292-6695
USA

Phone: +1 310 822 1511
Fax:   +1 310 823 6714
EMail: postel@isi.edu
