---
rfc: 2013
title: "SNMPv2 Management Information Base"
date: November 1996
category: Standards
updates: [1213]
---

# Table of Contents

  - [1. Introduction](#1-introduction)
  - [2. Definitions](#2-definitions)
  - [2.1 The UDP Group](#21-the-udp-group)
  - [2.2 Conformance Information](#22-conformance-information)
  - [2.2.1 Compliance Statements](#221-compliance-statements)
  - [2.2.2 Units of Conformance](#222-units-of-conformance)
  - [3. Acknowledgements](#3-acknowledgements)
  - [4. References](#4-references)
  - [5. Security Considerations](#5-security-considerations)
  - [6. Editor's Address](#6-editors-address)

# 1. Introduction

A management system contains: several (potentially many) nodes, each
with a processing entity, termed an agent, which has access to
management instrumentation; at least one management station; and, a
management protocol, used to convey management information between
the agents and management stations.  Operations of the protocol are
carried out under an administrative framework which defines
authentication, authorization, access control, and privacy policies.

Management stations execute management applications which monitor and
control managed elements.  Managed elements are devices such as
hosts, routers, terminal servers, etc., which are monitored and
controlled via access to their management information.

Management information is viewed as a collection of managed objects,
residing in a virtual information store, termed the Management
Information Base (MIB).  Collections of related objects are defined
in MIB modules.  These modules are written using a subset of OSI's
Abstract Syntax Notation One (ASN.1) [1], termed the Structure of
Management Information (SMI) [2].

This document is the MIB module which defines managed objects for
managing implementations of the User Datagram Protocol (UDP) [3].

The managed objects in this MIB module were originally defined using
the SNMPv1 framework as a part of MIB-II [4].  This document defines
the same objects for UDP using the SNMPv2 framework.

# 2. Definitions

UDP-MIB DEFINITIONS ::= BEGIN

IMPORTS
MODULE-IDENTITY, OBJECT-TYPE, Counter32,
IpAddress, mib-2                   FROM SNMPv2-SMI
MODULE-COMPLIANCE, OBJECT-GROUP    FROM SNMPv2-CONF;

udpMIB MODULE-IDENTITY
LAST-UPDATED "9411010000Z"
ORGANIZATION "IETF SNMPv2 Working Group"
CONTACT-INFO
"        Keith McCloghrie

Postal: Cisco Systems, Inc.

# 170. West Tasman Drive

San Jose, CA  95134-1706
US

Phone:  +1 408 526 5260
Email:  kzm@cisco.com"

"The MIB module for managing UDP implementations."
REVISION      "9103310000Z"
DESCRIPTION
"The initial revision of this MIB module was part of MIB-
II."
::= { mib-2 50 }

-- the UDP group

udp      OBJECT IDENTIFIER ::= { mib-2 7 }

udpInDatagrams OBJECT-TYPE
SYNTAX      Counter32
MAX-ACCESS  read-only
STATUS      current
DESCRIPTION
"The total number of UDP datagrams delivered to UDP users."
::= { udp 1 }

udpNoPorts OBJECT-TYPE
SYNTAX      Counter32
MAX-ACCESS  read-only
STATUS      current
DESCRIPTION
"The total number of received UDP datagrams for which there
was no application at the destination port."
::= { udp 2 }

udpInErrors OBJECT-TYPE
SYNTAX      Counter32
MAX-ACCESS  read-only
STATUS      current
DESCRIPTION
"The number of received UDP datagrams that could not be
delivered for reasons other than the lack of an application
at the destination port."
::= { udp 3 }

udpOutDatagrams OBJECT-TYPE
SYNTAX      Counter32
MAX-ACCESS  read-only
STATUS      current
DESCRIPTION
"The total number of UDP datagrams sent from this entity."
::= { udp 4 }

-- the UDP Listener table

-- The UDP listener table contains information about this
-- entity's UDP end-points on which a local application is
-- currently accepting datagrams.

udpTable OBJECT-TYPE
SYNTAX      SEQUENCE OF UdpEntry
MAX-ACCESS  not-accessible
STATUS      current
DESCRIPTION
"A table containing UDP listener information."
::= { udp 5 }

udpEntry OBJECT-TYPE
SYNTAX      UdpEntry
MAX-ACCESS  not-accessible
STATUS      current
DESCRIPTION
"Information about a particular current UDP listener."
INDEX   { udpLocalAddress, udpLocalPort }
::= { udpTable 1 }

UdpEntry ::= SEQUENCE {
udpLocalAddress  IpAddress,
udpLocalPort     INTEGER
}

udpLocalAddress OBJECT-TYPE
SYNTAX      IpAddress
MAX-ACCESS  read-only
STATUS      current
DESCRIPTION
"The local IP address for this UDP listener.  In the case of
a UDP listener which is willing to accept datagrams for any
IP interface associated with the node, the value 0.0.0.0 is
used."
::= { udpEntry 1 }

udpLocalPort OBJECT-TYPE
SYNTAX      INTEGER (0..65535)
MAX-ACCESS  read-only
STATUS      current
DESCRIPTION
"The local port number for this UDP listener."
::= { udpEntry 2 }

-- conformance information

udpMIBConformance OBJECT IDENTIFIER ::= { udpMIB 2 }

udpMIBCompliances OBJECT IDENTIFIER ::= { udpMIBConformance 1 }
udpMIBGroups      OBJECT IDENTIFIER ::= { udpMIBConformance 2 }

-- compliance statements

udpMIBCompliance MODULE-COMPLIANCE
STATUS  current
DESCRIPTION
"The compliance statement for SNMPv2 entities which
implement UDP."
MODULE  -- this module
MANDATORY-GROUPS { udpGroup
}
::= { udpMIBCompliances 1 }

-- units of conformance

udpGroup OBJECT-GROUP
OBJECTS   { udpInDatagrams, udpNoPorts,
udpInErrors, udpOutDatagrams,
udpLocalAddress, udpLocalPort }
STATUS    current
DESCRIPTION
"The udp group of objects providing for management of UDP
entities."
::= { udpMIBGroups 1 }

END

# 3. Acknowledgements

This document contains a modified subset of RFC 1213.

# 4. References

[1]  Information processing systems - Open Systems Interconnection
Specification of Abstract Syntax Notation One (ASN.1),
International Organization for Standardization.  International
Standard 8824, (December, 1987).

[2]  McCloghrie, K., Editor, "Structure of Management Information
for version 2 of the Simple Network Management Protocol
(SNMPv2)", RFC 1902, Cisco Systems, January 1996.

[3]  Postel, J., "User Datagram Protocol", STD 6, RFC 768, USC-ISI,
August 1980.

[4]  McCloghrie, K., and Rose, M., "Management Information Base for
Network Management of TCP/IP-based internets: MIB-II", STD 17,
RFC 1213, March 1991.

# 5. Security Considerations

Security issues are not discussed in this memo.

# 6. Editor's Address

Keith McCloghrie
Cisco Systems, Inc.
170 West Tasman Drive
San Jose, CA  95134-1706
US

Phone: +1 408 526 5260
EMail: kzm@cisco.com
