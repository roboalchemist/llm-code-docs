---
rfc: 3228
title: "IPv4 Internet Group Management Protocol (IGMP)"
date: February 2002
category: Best
---

# Abstract

This memo requests that the IANA create a registry for fields in the
IGMP (Internet Group Management Protocol) protocol header, and
provides guidance for the IANA to use in assigning parameters for
those fields.

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. IANA Considerations for fields in the IPv4 IGMP header](#2-iana-considerations-for-fields-in-the-ipv4-igmp-header)
  - [3. Assignments for testing and experimentation](#3-assignments-for-testing-and-experimentation)
  - [4. Security Considerations](#4-security-considerations)
  - [5. Normative References](#5-normative-references)
  - [6. Informative References](#6-informative-references)
  - [7. Author's Address](#7-authors-address)
  - [8. Full Copyright Statement](#8-full-copyright-statement)

# 1. Introduction

This memo requests that the IANA create a registry for fields in the
IGMP protocol header.

The terms "Specification Required", "Expert Review", "IESG Approval",
"IETF Consensus", and "Standards Action", are used in this memo to
refer to the processes described in [2].

# 2. IANA Considerations for fields in the IPv4 IGMP header

The IPv4 IGMP header [1] contains the following fields that carry
values assigned from IANA-managed name spaces: Type and Code.  Code
field values are defined relative to a specific Type value.

Values for the IPv4 IGMP Type fields are allocated using an IESG
Approval or Standards Action processes.  Code Values for existing
IPv4 IGMP Type fields are allocated using IESG Approval or Standards
Action processes.  The policy for assigning Code values for new IPv4
IGMP Types should be defined in the document defining the new Type
value.

# 3. Assignments for testing and experimentation

Instead of suggesting temporary assignments as in [3], this document
follows the lead of [4] and assigns a range of values for
experimental use.  The IGMP Code values 240-255 inclusive (0xf0 -
0xff) are reserved for protocol testing and experimentation.

Systems should silently ignore IGMP messages with unknown Code
values.

# 4. Security Considerations

Security analyzers such as firewalls and network intrusion detection
monitors often rely on unambiguous interpretations of the fields
described in this memo.  As new values for the fields are assigned,
existing security analyzers that do not understand the new values may
fail, resulting in either loss of connectivity if the analyzer
declines to forward the unrecognized traffic, or loss of security if
it does forward the traffic and the new values are used as part of an
attack.  This vulnerability argues for high visibility (which the
Standards Action and IETF Consensus processes ensure) for the
assignments whenever possible.

# 5. Normative References

[1]   Fenner, W., "Internet Group Management Protocol, Version 2",
RFC 2236, November 1997.

[2]   Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA
Considerations Section in RFCs", BCP 26, RFC 2434, October
1998.

# 6. Informative References

[3]   Bradner, S. and V. Paxson, "IANA Allocation Guidelines For
Values In the Internet Protocol and Related Headers", BCP 37,
RFC 2780, March 2000.

[4]   Narten, T., "Assigning Experimental and Testing Numbers
Considered Useful", Work in Progress.

# 7. Author's Address

Bill Fenner
AT&T Labs -- Research
75 Willow Rd
Menlo Park, CA 94025
USA

EMail: fenner@research.att.com

# 8. Full Copyright Statement

Copyright (C) The Internet Society (2002).  All Rights Reserved.

This document and translations of it may be copied and furnished to
others, and derivative works that comment on or otherwise explain it
or assist in its implementation may be prepared, copied, published
and distributed, in whole or in part, without restriction of any
kind, provided that the above copyright notice and this paragraph are
included on all such copies and derivative works.  However, this
document itself may not be modified in any way, such as by removing
the copyright notice or references to the Internet Society or other
Internet organizations, except as needed for the purpose of
developing Internet standards in which case the procedures for
copyrights defined in the Internet Standards process must be
followed, or as required to translate it into languages other than
English.

The limited permissions granted above are perpetual and will not be
revoked by the Internet Society or its successors or assigns.

This document and the information contained herein is provided on an
"AS IS" basis and THE INTERNET SOCIETY AND THE INTERNET ENGINEERING
TASK FORCE DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION
HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF
MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
