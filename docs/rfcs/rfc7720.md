---
rfc: 7720
title: "DNS Root Name Service Protocol and Deployment Requirements"
date: December 2015
category: Best
obsoletes: [2870]
---

# Abstract

The DNS root name service is a critical part of the Internet
architecture.  The protocol and deployment requirements for the DNS
root name service are defined in this document.  Operational
requirements are out of scope.

# Status of This Memo

This memo documents an Internet Best Current Practice.

This document is a product of the Internet Engineering Task Force
(IETF).  It represents the consensus of the IETF community.  It has
received public review and has been approved for publication by the
Internet Engineering Steering Group (IESG).  Further information on
BCPs is available in Section 2 of RFC 5741.

Information about the current status of this document, any errata,
and how to provide feedback on it may be obtained at
http://www.rfc-editor.org/info/rfc7720.

# Copyright Notice

Copyright (c) 2015 IETF Trust and the persons identified as the
document authors.  All rights reserved.

This document is subject to BCP 78 and the IETF Trust's Legal
Provisions Relating to IETF Documents
(http://trustee.ietf.org/license-info) in effect on the date of
publication of this document.  Please review these documents
carefully, as they describe your rights and restrictions with respect
to this document.  Code Components extracted from this document must
include Simplified BSD License text as described in Section 4.e of
the Trust Legal Provisions and are provided without warranty as
described in the Simplified BSD License.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [1.1.  Relationship to RFC 2870](#11-relationship-to-rfc-2870)
  - [2.  Protocol Requirements](#2-protocol-requirements)
  - [3.  Deployment Requirements](#3-deployment-requirements)
  - [4.  Security Considerations](#4-security-considerations)
  - [5.  Informative References](#5-informative-references)
  - [Acknowledgements](#acknowledgements)
  - [Authors' Addresses](#authors-addresses)

The keywords MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD,
SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL, when they appear in this
document, are to be interpreted as described in BCP 14, [RFC2119].

## 1.1. Relationship to RFC 2870

This document obsoletes [RFC2870].

This document and [RSSAC-001] together functionally replace
[RFC2870].

# 2. Protocol Requirements

This section describes the minimum high-level protocol requirements.
Operative details are documented in [RSSAC-001].

The root name service:

o  MUST implement core DNS [RFC1035] and clarifications to the DNS
[RFC2181].

o  MUST support IPv4 [RFC791] and IPv6 [RFC2460] transport of DNS
queries and responses.

o  MUST support UDP [RFC768] and TCP [RFC793] transport of DNS
queries and responses.

o  MUST generate checksums when sending UDP datagrams and MUST verify
checksums when receiving UDP datagrams containing a non-zero
checksum.

o  MUST implement DNSSEC [RFC4035] as an authoritative name service.

o  MUST implement extension mechanisms for DNS (EDNS(0)) [RFC6891].

# 3. Deployment Requirements

The root name service:

o  MUST answer queries from any entity conforming to [RFC1122] with a
valid IP address.

o  MUST serve the unique [RFC2826] root zone [ROOTZONE].

# 4. Security Considerations

This document does not specify a new protocol.  However, the root
name service is a key component of the Internet architecture and play
a key role into the overall security of the Internet [RFC2826].
Specific security considerations on the DNS protocols are discussed
in their respective specifications.  The security considerations on
the operational side of the root name servers are discussed in
[RSSAC-001].

# 5. Informative References

[ARPAZONE]  IANA, ".ARPA Zone Management",
<http://www.iana.org/domains/arpa>.

[RFC768]    Postel, J., "User Datagram Protocol", STD 6, RFC 768,
DOI 10.17487/RFC0768, August 1980,
<http://www.rfc-editor.org/info/rfc768>.

[RFC791]    Postel, J., "Internet Protocol", STD 5, RFC 791,
DOI 10.17487/RFC0791, September 1981,
<http://www.rfc-editor.org/info/rfc791>.

[RFC793]    Postel, J., "Transmission Control Protocol", STD 7,
RFC 793, DOI 10.17487/RFC0793, September 1981,
<http://www.rfc-editor.org/info/rfc793>.

[RFC1035]   Mockapetris, P., "Domain names - implementation and
specification", STD 13, RFC 1035, DOI 10.17487/RFC1035,
November 1987, <http://www.rfc-editor.org/info/rfc1035>.

[RFC1122]   Braden, R., Ed., "Requirements for Internet Hosts -
Communication Layers", STD 3, RFC 1122,
DOI 10.17487/RFC1122, October 1989,
<http://www.rfc-editor.org/info/rfc1122>.

[RFC2119]   Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119,
DOI 10.17487/RFC2119, March 1997,
<http://www.rfc-editor.org/info/rfc2119>.

[RFC2181]   Elz, R. and R. Bush, "Clarifications to the DNS
Specification", RFC 2181, DOI 10.17487/RFC2181, July
1997, <http://www.rfc-editor.org/info/rfc2181>.

[RFC2460]   Deering, S. and R. Hinden, "Internet Protocol, Version 6
(IPv6) Specification", RFC 2460, DOI 10.17487/RFC2460,
December 1998, <http://www.rfc-editor.org/info/rfc2460>.

[RFC2826]   Internet Architecture Board, "IAB Technical Comment on
the Unique DNS Root", RFC 2826, DOI 10.17487/RFC2826, May
2000, <http://www.rfc-editor.org/info/rfc2826>.

[RFC2870]   Bush, R., Karrenberg, D., Kosters, M., and R. Plzak,
"Root Name Server Operational Requirements", BCP 40,
RFC 2870, DOI 10.17487/RFC2870, June 2000,
<http://www.rfc-editor.org/info/rfc2870>.

[RFC3172]   Huston, G., Ed., "Management Guidelines & Operational
Requirements for the Address and Routing Parameter Area
Domain ("arpa")", BCP 52, RFC 3172, DOI 10.17487/RFC3172,
September 2001, <http://www.rfc-editor.org/info/rfc3172>.

[RFC4035]   Arends, R., Austein, R., Larson, M., Massey, D., and S.
Rose, "Protocol Modifications for the DNS Security
Extensions", RFC 4035, DOI 10.17487/RFC4035, March 2005,
<http://www.rfc-editor.org/info/rfc4035>.

[RFC6891]   Damas, J., Graff, M., and P. Vixie, "Extension Mechanisms
for DNS (EDNS(0))", STD 75, RFC 6891,
DOI 10.17487/RFC6891, April 2013,
<http://www.rfc-editor.org/info/rfc6891>.

[ROOTZONE]  "Root Zone", <ftp://rs.internic.net/domain/root.zone>.

[RSSAC-001] Root Server System Advisory Committee (RSSAC), "Service
Expectations of Root Servers", November 2014,
<https://www.icann.org/en/system/files/files/
rssac-001-root-service-expectations-04dec15-en.pdf>.

# Acknowledgements

Some text was taken from [RFC2870].  The editors of this document
would like to sincerely thank the following individuals for valuable
contributions to the text: Andrew Sullivan, Simon Perreault,
Jean-Philippe Dionne, Dave Thaler, Russ Housley, Alissa Cooper, Joe
Abley, Joao Damas, Daniel Karrenberg, Jacques Latour, Eliot Lear,
Bill Manning, David Conrad, Paul Hoffman, Terry Manderson, Jari
Arkko, and Mark Andrews.

# Authors' Addresses

Marc Blanchet
Viagenie
246 Aberdeen
Quebec, QC  G1R 2E1
Canada

Email: Marc.Blanchet@viagenie.ca
URI:   http://viagenie.ca

Lars-Johan Liman
Netnod Internet Exchange
Box 30194
SE-104 25 Stockholm
Sweden

Email: liman@netnod.se
URI:   http://www.netnod.se/
