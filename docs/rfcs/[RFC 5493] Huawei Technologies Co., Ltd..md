---
rfc: 5493
title: "Huawei Technologies Co., Ltd."
date: April 2009
category: Informational
---

# Abstract

From a carrier perspective, the possibility of turning a permanent
connection (PC) into a soft permanent connection (SPC) and vice
versa, without actually affecting data plane traffic being carried
over it, is a valuable option.  In other terms, such operation can be
seen as a way of transferring the ownership and control of an
existing and in-use data plane connection between the management
plane and the control plane, leaving its data plane state untouched.

This memo sets out the requirements for such procedures within a
Generalized Multiprotocol Label Switching (GMPLS) network.

# Table of Contents

  - [1. Introduction](#1-introduction)
    - [1.1. Conventions Used in This Document](#11-conventions-used-in-this-document)
  - [2. Label Switched Path Terminology](#2-label-switched-path-terminology)
  - [3. LSP within GMPLS Control Plane](#3-lsp-within-gmpls-control-plane)
    - [3.1. Resource Ownership](#31-resource-ownership)
    - [3.2. Setting Up a GMPLS-Controlled Network](#32-setting-up-a-gmpls-controlled-network)
  - [4. Typical Use Cases](#4-typical-use-cases)
    - [4.1. PC-to-SC/SPC Conversion](#41-pc-to-scspc-conversion)
    - [4.2. SC-to-PC Conversion](#42-sc-to-pc-conversion)
  - [5. Requirements](#5-requirements)
    - [5.1. Data Plane LSP Consistency](#51-data-plane-lsp-consistency)
    - [5.2. No Disruption of User Traffic](#52-no-disruption-of-user-traffic)
    - [5.3. Transfer from Management Plane to Control Plane](#53-transfer-from-management-plane-to-control-plane)
    - [5.4. Transfer from Control Plane to Management Plane](#54-transfer-from-control-plane-to-management-plane)
    - [5.5. Synchronization of State among Nodes during Conversion](#55-synchronization-of-state-among-nodes-during-conversion)
    - [5.6. Support of Soft Permanent Connections](#56-support-of-soft-permanent-connections)
    - [5.7. Failure of Transfer](#57-failure-of-transfer)
  - [6. Security Considerations](#6-security-considerations)
  - [7. Contributors](#7-contributors)
  - [8. Acknowledgments](#8-acknowledgments)
  - [9. References](#9-references)
    - [9.1. Normative References](#91-normative-references)
    - [9.2. Informational References](#92-informational-references)

# 1. Introduction

In a typical, traditional transport network scenario, data plane
connections between two end-points are controlled by means of a
Network Management System (NMS) operating within the management plane
(MP).  The NMS/MP is the owner of such transport connections, being
responsible of their setup, teardown, and maintenance.  Provisioned
connections of this type, initiated and managed by the management
plane, are known as permanent connections (PCs) [G.8081].

When the setup, teardown, and maintenance of connections are achieved
by means of a signaling protocol owned by the control plane (CP),
such connections are known as switched connections (SCs) [G.8081].

In many deployments, a hybrid connection type will be used.  A soft
permanent connection (SPC) is a combination of a permanent connection
segment at the source-user-to-network side, a permanent connection
segment at the destination-user-to-network side, and a switched
connection segment within the core network.  The permanent parts of
the SPC are owned by the management plane, and the switched parts are
owned by the control plane [G.8081].

Note, some aspects of a control-plane-initiated connection must be
capable of being queried/controlled by the management plane.  These
aspects should be independent of how the connection was established.

## 1.1. Conventions Used in This Document

Although this requirements document is an informational document, not
a protocol specification, the key words "MUST", "MUST NOT",
"REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT",
"RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in RFC 2119 [RFC2119] for clarity of
requirement specification.

# 2. Label Switched Path Terminology

A Label Switched Path (LSP) has different semantics depending on the
plane in which the term is used.

In the data plane, an LSP indicates the data plane forwarding path.
It defines the forwarding or switching operations at each network
entity.  It is the sequence of data plane resources (links, labels,
cross-connects) that achieves end-to-end data transport.

RFC 5493         Conversion between PC and SC in GMPLS        April 2009

In the management plane, an LSP is the management plane state
information (such as the connection attributes and path information)
associated with and necessary for the creation and maintenance of a
data plane connection.

In the control plane, an LSP is the control plane state information
(such as the RSVP-TE [RFC3473] Path and Resv state) associated with
and necessary for the creation and maintenance of a data plane
connection.

A permanent connection has an LSP presence in the data plane and the
management plane.  A switched connection has an LSP presence in the
data plane and the control plane.  An SPC has an LSP presence in the
data plane for its entire length, but has a management plane presence
for part of its length and a control plane presence for part of its
length.

In this document, when we discuss the LSP conversion between
management plane and control plane, we mainly focus on the conversion
of control plane state information and management plane state
information.

# 3. LSP within GMPLS Control Plane

GMPLS ([RFC3471], [RFC3473], and [RFC3945]) defines a control plane
architecture for transport networks.  This includes both routing and
signaling protocols for the creation and maintenance of LSPs in
networks whose data plane is based on different technologies, such as
Time Division Multiplexing (SDH/SONET, G.709 at ODUk level) and
Wavelength Division Multiplexing (G.709 at OCh level).

## 3.1. Resource Ownership

A resource used by an LSP is said to be 'owned' by the plane that was
used to set up the LSP through that part of the network.  Thus, all
the resources used by a permanent connection are owned by the
management plane, and all the resources used by a switched connection
are owned by the control plane.  The resources used by an SPC are
divided between the management plane (for the resources used by the
permanent connection segments at the edge of the network) and the
control plane (for the resources used by the switched connection
segments in the middle of the network).

The division of resources available for ownership by the management
and control planes is an architectural issue.  A carrier may decide
to pre-partition the resources at a network entity so that LSPs under
management plane control use one set of resources and LSPs under

RFC 5493         Conversion between PC and SC in GMPLS        April 2009

control plane control use another set of resources.  Other carriers
may choose to make this distinction resource-by-resource as LSPs are
established.

It should be noted, however, that even when a resource is owned by
the control plane it will usually be the case that the management
plane has a controlling interest in the resource.  For example,
consider the basic safety requirements that management commands must
be able to put a laser out of service.

## 3.2. Setting Up a GMPLS-Controlled Network

The implementation of a new network using a Generalized Multiprotocol
Label Switching (GMPLS) control plane may be considered as a green
field deployment.  But in many cases, it is desirable to introduce a
GMPLS control plane into an existing transport network that is
already populated with permanent connections under management plane
control.

In a mixed scenario, permanent connections owned by the management
plane and switched connections owned by the control plane have to
coexist within the network.

It is also desirable to transfer the control of connections from the
management plane to the control plane so that connections that were
originally under the control of an NMS are now under the control of
the GMPLS protocols.  In case such connections are in service, such
conversion must be performed in a way that does not affect traffic.

Since attempts to move an LSP under GMPLS control might fail due to a
number of reasons outside the scope of this document, it is also
highly desirable to have a mechanism to convert the control of an LSP
back to the management plane.

Note that a permanent connection may be converted to a switched
connection or to an SPC, and an SPC may be converted to a switched
connection as well (PC to SC, PC to SPC, and SPC to SC).  So the
reverse mappings may also be needed (SC to PC, SPC to PC, and SC to
SPC).

Conversion to/from control/management will occur in MIBs or in
information stored on the device (e.g., cross-connect, label
assignment, label stacking, etc.) and is identified as either
initiated by a specific control protocol or by manual operation
(i.e., via an NMS).  When converting, this hop-level owner
information needs to be completed for all hops.  If conversion cannot
be done for all hops, then the conversion must be done for no hops,

RFC 5493         Conversion between PC and SC in GMPLS        April 2009

the state of the hop-level information must be restored to that
before the conversion was attempted, and an error condition must be
reported to the management system.

In either case of conversion, the management plane shall initiate the
change.  When converting from a PC to an SC, the management system
must indicate to each hop that a control protocol is now to be used,
and then configure the data needed by the control protocol at the
connection endpoints.  When converting from an SC to a PC, the
management plane must change the owner of each hop.  Then the
instance in the control plane must be removed without affecting the
data plane.

The case where the CP and/or MP fail at one or more nodes during the
conversion procedure must be handled in the solution.  If the network
is viewed as the database of record (including data, control, and
management plane elements), then a solution that has procedures
similar to those of a two-phase database commit process may be needed
to ensure integrity and to support the need to revert to the state
prior to the conversion attempt if there is a CP and/or MP failure
during the attempted conversion.

# 4. Typical Use Cases

## 4.1. PC-to-SC/SPC Conversion

A typical scenario where a PC-to-SC (or SPC) procedure can be a
useful option is at the initial stage of control plane deployment in
an existing network.  In such a case, all the network connections,
possibly carrying traffic, are already set up as PCs and are owned by
the management plane.

At a latter stage, when the network is partially controlled by the
management plane and partially controlled by the control plane (PCs
and SCs/SPCs coexist) and it is desired to extend the control plane,
a PC-to-SC procedure can be used to transfer a PC or SPC to a SC.

In both cases, a connection, set up and owned by the management
plane, needs to be transferred to control plane control.  If a
connection is carrying traffic, its control transfer has to be done
without any disruption to the data plane traffic.

## 4.2. SC-to-PC Conversion

The main need for an SC-to-PC conversion is to give an operator the
capability of undoing the action of the above introduced PC-to-SC
conversion.

RFC 5493         Conversion between PC and SC in GMPLS        April 2009

In other words, the SC-to-PC conversion is a back-out procedure and
as such is not specified as mandatory in this document, but it is
still a highly desirable function.

Again, it is worth stressing the requirement that such an SPC-to-PC
conversion needs to be achieved without any effect on the associated
data plane state so that the connection continues to be operational
and to carry traffic during the transition.

# 5. Requirements

This section sets out the basic requirements for procedures and
processes that are used to perform the functions of this document.
Notation from [RFC2119] is used to clarify the level of each
requirement.

## 5.1. Data Plane LSP Consistency

The data plane LSP MUST stay in place throughout the whole control
transfer process.  It MUST follow the same path through the network
and MUST use the same network resources.

## 5.2. No Disruption of User Traffic

The transfer process MUST NOT cause any disruption of user traffic
flowing over the LSP whose control is being transferred or over any
other LSP in the network.

SC-to-PC conversion and vice-versa SHALL occur without generating
alarms towards the end users or the NMS.

## 5.3. Transfer from Management Plane to Control Plane

It MUST be possible to transfer the ownership of an LSP from the
management plane to the control plane.

## 5.4. Transfer from Control Plane to Management Plane

It SHOULD be possible to transfer the ownership of an LSP from the
control plane to the management plane.

## 5.5. Synchronization of State among Nodes during Conversion

It MUST be assured that the state of the LSP is synchronized among
all nodes traversed by it before the conversion is considered
complete.

RFC 5493         Conversion between PC and SC in GMPLS        April 2009

## 5.6. Support of Soft Permanent Connections

It MUST be possible to segment an LSP such that it can be converted
to or from an SPC.

## 5.7. Failure of Transfer

It MUST be possible for a transfer from one plane to the other to
fail in a non-destructive way, leaving the ownership unchanged and
without impacting traffic.

If during the transfer procedure issues arise causing an unsuccessful
or unexpected result, it MUST be assured that:

1.  Traffic over the data plane is not affected.

2.  The LSP status is consistent in all the network nodes involved in
the procedure.

Point 2, above, assures that even in case of some failure during the
transfer, the state of the affected LSP is brought back to the
initial one and is fully under the control of the owning entity.

# 6. Security Considerations

Allowing control of an LSP to be taken away from a plane introduces a
possible way in which services may be disrupted by malicious
intervention.

A solution to the requirements in this document will utilize the
security mechanisms supported by the management plane and GMPLS
control plane protocols, and no new security requirements over the
general requirements described in [RFC3945] are introduced.  It is
expected that solution documents will include an analysis of the
security issues introduced by any new protocol extensions.

The management plane interactions MUST be supported through protocols
that can offer adequate security mechanisms to secure the
configuration and protect the operation of the devices that are
managed.  These mechanisms MUST include at least cryptographic
security and the ability to ensure that the entity giving access to
configuration parameters is properly configured to give access only
to those principals (users) that have legitimate rights to
read/create/change/delete the parameters.  IETF standard management
protocols (Netconf [RFC4741] and SNMPv3 [RFC3410]) offer these
mechanisms.

RFC 5493         Conversion between PC and SC in GMPLS        April 2009

Note also that implementations may support policy components to
determine whether individual LSPs may be transferred between planes.

# 7. Contributors

Nicola Ciulli
NextWorks
Corso Italia 116
56125 Pisa, Italy
EMail: n.ciulli@nextworks.it

Han Li
China Mobile Communications Co.
53 A Xibianmennei Ave. Xuanwu District
Deijing 100053 P.R. China
Phone: 10-66006688 ext.3092
EMail: lihan@chinamobile.com

Daniele Ceccarelli
Ericsson
Via A. Negrone 1/A
Genova-Sestri Ponente, Italy
Phone: +390106002515
EMail: daniele.ceccarelli@ericsson.com

# 8. Acknowledgments

We wish to thank the following people (listed randomly): Adrian
Farrel for his editorial assistance to prepare this document for
publication; Dean Cheng, Julien Meuric, Dimitri Papadimitriou,
Deborah Brungard, Igor Bryskin, Lou Berger, Don Fedyk, John Drake,
and Vijay Pandian for their suggestions and comments on the CCAMP
list.

# 9. References

## 9.1. Normative References

[RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
Requirement Levels", BCP 14, RFC 2119, March 1997.

[RFC3410]  Case, J., Mundy, R., Partain, D., and B.
Stewart,"Introduction and Applicability Statements for
Internet-Standard Management Framework", RFC 3410,
December 2002.

RFC 5493         Conversion between PC and SC in GMPLS        April 2009

## 9.2. Informative References

[RFC3471]  Berger, L., Ed., "Generalized Multi-Protocol Label
Switching (GMPLS) Signaling Functional Description", RFC
3471, January 2003.

[RFC3473]  Berger, L., Ed., "Generalized Multi-Protocol Label
Switching (GMPLS) Signaling Resource ReserVation
Protocol-Traffic Engineering (RSVP-TE) Extensions", RFC
3473, January 2003.

[RFC3945]  Mannie, E., Ed., "Generalized Multi-Protocol Label
Switching (GMPLS) Architecture", RFC 3945, October 2004.

[RFC4741]  Enns, R., Ed., "NETCONF Configuration Protocol", RFC 4741,
December 2006.

```
   [G.8081]   International Telecommunications Union, "Terms and
              definitions for Automatically Switched Optical Networks
              (ASON)", Recommendation G.8081/Y.1353, June 2004.

```

RFC 5493         Conversion between PC and SC in GMPLS        April 2009

# Authors' Addresses

Diego Caviglia
Ericsson
Via A. Negrone 1/A
Genova - Sestri Ponente
Italy

EMail: diego.caviglia@ericsson.com

Dino Bramanti
Ericsson
Via Moruzzi 1 C/O Area Ricerca CNR
Pisa
Italy

EMail: dino.bramanti@ericsson.com

Dan Li
Huawei Technologies Co., Ltd.
Shenzhen 518129
Huawei Base, Bantian, Longgang
China

EMail: danli@huawei.com

Dave McDysan
Verizon
Ashburn, VA
USA

EMail: dave.mcdysan@verizon.com
