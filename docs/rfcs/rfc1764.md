---
rfc: 1764
title: "The PPP XNS IDP Control Protocol (XNSCP)"
date: March 1995
category: Standards
---

# Abstract

The Point-to-Point Protocol (PPP) [1] provides a standard method for
transporting multi-protocol datagrams over point-to-point links.  PPP
defines an extensible Link Control Protocol, and proposes a family of
Network Control Protocols for establishing and configuring different
network-layer protocols.

This document defines the Network Control Protocol for establishing
and configuring the Xerox Network Systems (XNS) Internet Datagram
Protocol (IDP) over PPP.

# Table of Contents

  - [1.     Introduction](#1-introduction)
    - [1.1       Specification of Requirements](#11-specification-of-requirements)
    - [1.2       Terminology](#12-terminology)
  - [2.     A PPP Network Control Protocol for XNS IDP](#2-a-ppp-network-control-protocol-for-xns-idp)
    - [2.1       Sending XNS IDP Datagrams](#21-sending-xns-idp-datagrams)
  - [SECURITY CONSIDERATIONS](#security-considerations)
  - [REFERENCES](#references)
    - [ACKNOWLEDGEMENTS](#acknowledgements)
  - [CHAIR'S ADDRESS](#chairs-address)
  - [AUTHOR'S ADDRESS](#authors-address)

3. A family of Network Control Protocols for establishing and
configuring different network-layer protocols.

In order to establish communications over a point-to-point link, each
end of the PPP link must first send LCP packets to configure and test
the data link.  After the link has been established and optional
facilities have been negotiated as needed by the LCP, PPP must send
XNSCP packets to choose and configure the XNS IDP network-layer
protocol.  Once XNSCP has reached the Opened state, XNS IDP datagrams
can be sent over the link.

The link will remain configured for communications until explicit LCP
or XNSCP packets close the link down, or until some external event
occurs (an inactivity timer expires or network administrator
intervention).

## 1.1. Specification of Requirements

In this document, several words are used to signify the requirements
of the specification.  These words are often capitalized.

MUST      This word, or the adjective "required", means that the
definition is an absolute requirement of the specification.

MUST NOT  This phrase means that the definition is an absolute
prohibition of the specification.

SHOULD    This word, or the adjective "recommended", means that there
may exist valid reasons in particular circumstances to
ignore this item, but the full implications must be
understood and carefully weighed before choosing a
different course.

MAY       This word, or the adjective "optional", means that this
item is one of an allowed set of alternatives.  An
implementation which does not include this option MUST be
prepared to interoperate with another implementation which
does include the option.

## 1.2. Terminology

This document frequently uses the following terms:

datagram  The unit of transmission in the network layer (such as IP).
A datagram may be encapsulated in one or more packets
passed to the data link layer.

frame     The unit of transmission at the data link layer.  A frame
may include a header and/or a trailer, along with some
number of units of data.

packet    The basic unit of encapsulation, which is passed across the
interface between the network layer and the data link
layer.  A packet is usually mapped to a frame; the
exceptions are when data link layer fragmentation is being
performed, or when multiple packets are incorporated into a
single frame.

peer      The other end of the point-to-point link.

silently discard
This means the implementation discards the packet without
further processing.  The implementation SHOULD provide the
capability of logging the error, including the contents of
the silently discarded packet, and SHOULD record the event
in a statistics counter.

# 2. A PPP Network Control Protocol for XNS IDP

The XNS IDP Control Protocol (XNSCP) is responsible for configuring,
enabling, and disabling the XNS IDP protocol modules on both ends of
the point-to-point link.  XNSCP uses the same packet exchange
mechanism as the Link Control Protocol (LCP).  XNSCP packets may not
be exchanged until PPP has reached the Network-Layer Protocol phase.
XNSCP packets received before this phase is reached should be
silently discarded.

The XNS IDP Control Protocol is exactly the same as the Link Control
Protocol [1] with the following exceptions:

Frame Modifications

The packet may utilize any modifications to the basic frame format
which have been negotiated during the Link Establishment phase.

Data Link Layer Protocol Field

Exactly one XNSCP packet is encapsulated in the Information field
of a PPP Data Link Layer frame, where the PPP Protocol field
indicates type hex 8025 (XNS IDP Control Protocol).

Code field

Only Codes 1 through 7 (Configure-Request, Configure-Ack,
Configure-Nak, Configure-Reject, Terminate-Request, Terminate-Ack
and Code-Reject) are used.  Other Codes should be treated as
unrecognized and should result in Code-Rejects.

Timeouts

XNSCP packets may not be exchanged until PPP has reached the
Network-Layer Protocol phase.  An implementation should be
prepared to wait for Authentication and Link Quality Determination
to finish before timing out waiting for a Configure-Ack or other
response.  It is suggested that an implementation give up only
after user intervention or a configurable amount of time.

Configuration Option Types

XNSCP has no Configuration Options.

## 2.1. Sending XNS IDP Datagrams

Before any XNS IDP packets may be communicated, PPP must reach the
Network-Layer Protocol phase, and the XNS IDP Control Protocol must
reach the Opened state.

Exactly one XNS IDP packet is encapsulated in the Information field
of a PPP Data Link Layer frame where the Protocol field indicates
type hex 0025 (XNS IDP datagram).

The maximum length of a XNS IDP datagram transmitted over a PPP link
is the same as the maximum length of the Information field of a PPP
data link layer frame.  Since there is no standard method for
fragmenting and reassembling XNS IDP datagrams, PPP links supporting
XNS IDP MUST allow at least 576 octets in the information field of a
data link layer frame.

The format of the Information field itself is the same as that
defined in [2].

# Security Considerations

Security issues are not discussed in this memo.

# References

[1] Simpson, W., "The Point-to-Point Protocol (PPP)", STD 51, RFC
1661, Daydreamer, July 1994.

[2] Xerox, "Internet Transport Protocols", January 1991, Order No.
XNSS 029101.

# Acknowledgements

Some of the text in this document is taken from previous documents
produced by the Point-to-Point Protocol Working Group of the Internet
Engineering Task Force (IETF).

In particular, Bill Simpson provided the boiler-plate used to create
this document.

Chair's Address

The working group can be contacted via the current chair:

Fred Baker
Cisco Systems
519 Lado Drive
Santa Barbara, California 93111

Phone: (805) 681-0115
EMail: fred@cisco.com

# Author's Address

Questions about this memo can also be directed to:

Steven J. Senum
DigiBoard
6400 Flying Cloud Drive
Eden Prairie, Minnesota 55344

Phone: (612) 943-9020
EMail: sjs@digibd.com
