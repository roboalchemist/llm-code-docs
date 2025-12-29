---
rfc: 5516
title: "Orange Labs"
date: April 2009
category: Informational
---

# Abstract

This document registers a set of IANA Diameter Command Codes to be
used in new vendor-specific Diameter applications defined for the
Third Generation Partnership Project (3GPP) Evolved Packet System
(EPS).  These new Diameter applications are defined for Mobile
Management Entity (MME)- and Serving GPRS (General Packet Radio
Service) Support Node (SGSN)-related interfaces in in the
architecture for the Evolved 3GPP Packet Switched Domain, which is
also known as the Evolved Packet System (EPS).

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. Terminology](#2-terminology)
  - [3. Command Codes](#3-command-codes)
  - [4. IANA Considerations](#4-iana-considerations)
  - [5. Security Considerations](#5-security-considerations)
  - [6. Acknowledgements](#6-acknowledgements)
  - [7. References](#7-references)
    - [7.1. Normative References](#71-normative-references)
    - [7.2. Informative References](#72-informative-references)

# 1. Introduction

The Third Generation Partnership Project (3GPP) is defining the
Evolved 3GPP Packet Switched Domain - also known as the Evolved
Packet System (EPS).  As part of this architecture, the interfaces
based on the Diameter protocol [RFC3588] require the definition of
two new Diameter applications.

As defined in [TS29.272], the 3GPP S6a/S6d application (vendor-
specific application id: 16777251) enables the transfer of
subscriber-related data between the Mobile Management Entity (MME)
and the Home Subscriber Server (HSS) on the S6a interface and between
the Serving GPRS Support Node (SGSN) and the Home Subscriber Server
(HSS) on the S6d interface.

Also defined in [TS29.272], the 3GPP S13/S13' application (vendor-
specific application id: 16777252) enables the Mobile Equipment
Identity check procedure between the Mobile Management Entity (MME)
and the Equipment Identity Register (EIR) on the S13 interface and
between the Serving GPRS Support Node (SGSN) and the Equipment
Identity Register (EIR) on the S13' interface.

Both Diameter applications are defined under the 3GPP vendor-id
"10415".  This document defines the assigned values of the command
codes used in these applications.

# 2. Terminology

The base Diameter specification (Section 1.3 of [RFC3588]) defines
most of the terminology used in this document.  Additionally, the
terms and acronyms defined in [TS29.272] are used in this document.

# 3. Command Codes

The 3GPP S6a/S6d application described in Section 5 of [TS29.272]
requires the allocation of command code values for the following
command pairs:

o  3GPP-Update-Location-Request/Answer (ULR/ULA)

o  3GPP-Cancel-Location-Request/Answer (CLR/CLA)

o  3GPP-Authentication-Information-Request/ Answer (AIR/AIA)

o  3GPP-Insert-Subscriber-Data-Request/Answer (IDR/IDA)

o  3GPP-Delete-Subscriber-Data-Request/Answer (DSR/DSA)

o  3GPP-Purge-UE-Request/Answer (PUR/PUA)

o  3GPP-Reset-Request/Answer (RSR/RSA)

o  3GPP-Notify-Request/Answer (NOR/NOA)

The 3GPP S13/S13 application described in Section 6 of [TS29.272]
requires the allocation of a command code value for the following
command pair:

o  3GPP-ME-Identity-Check-Request/Answer (ECR/ECA)

# 4. IANA Considerations

This section provides guidance to the Internet Assigned Numbers
Authority (IANA) regarding registration of values related to the
Diameter protocol, in accordance with BCP 26 [RFC5226].

This document defines values in the namespace that has been defined
in the Diameter base specification [RFC3588].  Section 11 of
[RFC3588] (that document's IANA Considerations) details the
assignment criteria.  IANA allocated the following command code
values:

+----------------------------------------------------------------------+
| Code Command Name                            Abbrev.  Defined in     |
+----------------------------------------------------------------------+
| 316  3GPP-Update-Location-Request            ULR      3GPP TS 29.272 |
| 316  3GPP-Update-Location-Answer             ULA      3GPP TS 29.272 |
| 317  3GPP-Cancel-Location-Request            CLR      3GPP TS 29.272 |
| 317  3GPP-Cancel-Location-Answer             CLA      3GPP TS 29.272 |
| 318  3GPP-Authentication-Information-Request AIR      3GPP TS 29.272 |
| 318  3GPP-Authentication-Information-Answer  AIA      3GPP TS 29.272 |
| 319  3GPP-Insert-Subscriber-Data-Request     IDR      3GPP TS 29.272 |
| 319  3GPP-Insert-Subscriber-Data-Answer      IDA      3GPP TS 29.272 |
| 320  3GPP-Delete-Subscriber-Data-Request     DSR      3GPP TS 29.272 |
| 320  3GPP-Delete-Subscriber-Data-Answer      DSA      3GPP TS 29.272 |
| 321  3GPP-Purge-UE-Request                   PUR      3GPP TS 29.272 |
| 321  3GPP-Purge-UE-Answer                    PUA      3GPP TS 29.272 |
| 322  3GPP-Reset-Request                      RSR      3GPP TS 29.272 |
| 322  3GPP-Reset-Answer                       RSA      3GPP TS 29.272 |
| 323  3GPP-Notify-Request                     NOR      3GPP TS 29.272 |
| 323  3GPP-Notify-Answer                      NOA      3GPP TS 29.272 |
| 324  3GPP-ME-Identity-Check-Request          ECR      3GPP TS 29.272 |
| 324  3GPP-ME-Identity-Check-Answer           ECA      3GPP TS 29.272 |
+----------------------------------------------------------------------+

# 5. Security Considerations

This document describes command codes used in applications that build
on top of the Diameter base protocol and the same security
considerations described in [RFC3588] are applicable to this
document.  No further extensions are required beyond the security
mechanisms offered by [RFC3588].

# 6. Acknowledgements

We would like to thank the 3GPP CT4 delegates, Victor Fajardo, and
Glen Zorn for their review and comments.  We would also like to thank
Dan Romascanu for volunteering to be AD sponsor and Hannes Tschofenig
for volunteering to be Document Shepherd.

# 7. References

## 7.1. Normative References

[RFC3588]   Calhoun, P., Loughney, J., Guttman, E., Zorn, G., and J.
Arkko, "Diameter Base Protocol", RFC 3588,
September 2003.

```
   [TS29.272]  3rd Generation Partnership Project, "3GPP TS 29.272;
```

Technical Specification Group Core Network and Terminals;
Evolved Packet System; Mobility Management Entity (MME)
and Serving GPRS Support Node (SGSN) Related Interfaces
Based on Diameter Protocol",
http://www.3gpp.org/ftp/Specs/html-info/29272.htm.

## 7.2. Informative References

[RFC5226]   Narten, T. and H. Alvestrand, "Guidelines for Writing an
IANA Considerations Section in RFCs", BCP 26, RFC 5226,
May 2008.

# Authors' Addresses

Mark Jones
Bridgewater Systems

EMail: mark.jones@bridgewatersystems.com

Lionel Morand
Orange Labs

EMail: lionel.morand@orange-ftgroup.com
