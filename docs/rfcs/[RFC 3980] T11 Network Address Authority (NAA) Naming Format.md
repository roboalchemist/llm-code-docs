---
rfc: 3980
title: "T11 Network Address Authority (NAA) Naming Format"
date: February 2005
category: Standards
updates: [3720]
---

# Abstract

Internet Small Computer Systems Interface (iSCSI) is a SCSI transport
protocol that maps the SCSI family of protocols onto TCP/IP.  This
document defines an additional iSCSI node name type format to enable
use of the "Network Address Authority" (NAA) worldwide naming format
defined by the InterNational Committee for Information Technology
Standards (INCITS) T11 - Fibre Channel (FC) protocols and used by
Serial Attached SCSI (SAS).  This document updates RFC 3720.

# Table of Contents

  - [1.  Introduction](#1-introduction)
  - [2.  Background](#2-background)
  - [3.  Motivation](#3-motivation)
  - [4.  iSCSI NAA Name Structure](#4-iscsi-naa-name-structure)
    - [4.1.  Type "naa." - Network Address Authority](#41-type-naa-network-address-authority)
  - [5.  Terminology](#5-terminology)
    - [5.1.  IQN](#51-iqn)
    - [5.2.  SRP](#52-srp)
    - [5.3.  SAS](#53-sas)
    - [5.4.  NAA](#54-naa)
    - [5.5.  InfiniBand](#55-infiniband)
    - [5.6.  INCITS](#56-incits)
    - [5.7.  T10](#57-t10)
    - [5.8.  T11](#58-t11)
  - [6.  Security Considerations](#6-security-considerations)
  - [7.  References](#7-references)
    - [7.1.  Normative References](#71-normative-references)
    - [7.2.  Informative References](#72-informative-references)
  - [Authors' Addresses](#authors-addresses)
  - [Full Copyright Statement](#full-copyright-statement)

# 1. Introduction

This document discusses the motivation for adding an NAA type format
as an iSCSI node naming format and defines this format in accordance
with the iSCSI naming conventions [RFC3720].  Defining this format
will enable SCSI storage devices containing both iSCSI ports and SAS
ports to use the same NAA-based SCSI device name.

# 2. Background

A number of networked transports currently provide port abstractions
to the SCSI protocol.  These transports all incorporate some form of
world-wide unique name construction format.  The following table
summarizes the current protocols and their naming formats.

SCSI Transport Protocol     Naming Format
-----------------------------------------------
|                            | EUI-64| NAA |IQN |
|----------------------------|-------|-----|----|
|    iSCSI (Internet SCSI)   |   X   |     | X  |
|----------------------------|-------|-----|----|
|     FCP (Fibre Channel)    |       |  X  |    |
|----------------------------|-------|-----|----|
| SAS (Serial Attached SCSI) |       |  X  |    |
|----------------------------|-------|-----|----|
|    SRP (for InfiniBand)    |   X   |     |    |
-----------------------------------------------

The INCITS T11 Framing and Signaling Specification [FC-FS] defines a
format called the Network Address Authority (NAA) format for
constructing worldwide unique identifiers that use various identifier
registration authorities.  This identifier format is used by the
Fibre Channel and SAS SCSI transport protocols.  As most existing
networked SCSI ports today are either FC or SAS, the NAA format is
the most commonly used identifier format for SCSI transports.

# 3. Motivation

If iSCSI included a naming format that allowed direct representation
of an NAA-format name, it would facilitate construction of a target
device name that translates easily across multiple namespaces for a
SCSI storage device containing ports served by different transports.

This document defines an NAA type iSCSI naming format so that one NAA
identifier can be assigned as the basis for the SCSI device name for
a SCSI target with both SAS ports and iSCSI ports.

INCITS T10 SCSI has defined a string format SCSI target device name
in [SPC3] that is reported in the VPD page 83 device identifier page.
[SAM3] specifies that a SCSI device shall have no more than one
(i.e., zero or one) SCSI device name in the SCSI name string format
regardless of the number of SCSI transport protocols supported by the
SCSI device.  Adding the INCITS T11-defined NAA format as a defined
type for iSCSI device names would make the iSCSI device naming format
more consistent across all current SCSI networked transports that
define an NAA format SCSI device name.  This would facilitate the
creation of SCSI device names that are transport-independent.  It
would also contribute to the creation of SCSI Logical Unit (LU) names
based on this SCSI device name.

# 4. iSCSI NAA Name Structure

This document defines an additional iSCSI name type:

type "naa." - the remainder of the string is an INCITS T11 defined
Network Address Authority identifier in ASCII-encoded
hexadecimal.

## 4.1. Type "naa." - Network Address Authority

[FC-FS] defines a format for constructing globally unique
identifiers, referred to as the Network Address Authority (NAA)
format.

The iSCSI NAA naming format is "naa.", followed by an NAA identifier
represented in ASCII-encoded hexadecimal digits.

An example of an iSCSI name with a 64-bit NAA value follows:

Type  NAA identifier (ASCII-encoded hexadecimal)
+--++--------------+
|  ||              |

naa.52004567BA64678D

An example of an iSCSI name with a 128-bit NAA value follows:

Type  NAA identifier (ASCII-encoded hexadecimal)
+--++------------------------------+
|  ||                              |

naa.62004567BA64678D0123456789ABCDEF

The iSCSI NAA naming format might be used in an implementation when
the infrastructure for generating NAA worldwide unique names is
already in place because the device contains both SAS and iSCSI SCSI
ports.

The NAA identifier formatted in an ASCII-hexadecimal representation
has a maximum size of 32 characters (128 bit NAA format).  As a
result, there is no issue with this naming format exceeding the
maximum size for iSCSI node names.

# 5. Terminology

## 5.1. IQN

iSCSI qualified name, an identifier format defined by the iSCSI
protocol [RFC3720].

## 5.2. SRP

SCSI RDMA Protocol.  SRP defines a SCSI protocol mapping onto the
InfiniBand (tm) Architecture and/or functionally similar cluster
protocols [SRP].

## 5.3. SAS

Serial Attached SCSI.  The Serial Attached SCSI (SAS) standard
contains both a physical layer compatible with Serial ATA, and
protocols for transporting SCSI commands to SAS devices and ATA
commands to SATA devices [SAS].

## 5.4. NAA

Network Address Authority, a naming format defined by the INCITS T11
Fibre Channel protocols [FC-FS].

## 5.5. InfiniBand

An I/O architecture originally intended to replace PCI and to address
high performance server interconnectivity [IB].

## 5.6. INCITS

INCITS stands for InterNational Committee of Information Technology
Standards.  The INCITS has a broad standardization scope within the
field of Information and Communications Technologies (ICT),
encompassing storage, processing, transfer, display, management,
organization, and retrieval of information.  INCITS serves as ANSI's
Technical Advisory Group for the ISO/IEC Joint Technical Committee 1
(JTC 1).  See http://www.incits.org.

## 5.7. T10

A technical committee within INCITS that develops standards and
technical reports on I/O interfaces, particularly the series of SCSI
(Small Computer Systems Interface) standards.  See
http://www.t10.org.

## 5.8. T11

A technical committee within INCITS responsible for standards
development in the areas of Intelligent Peripheral Interface (IPI),
High-Performance Parallel Interface (HIPPI) and Fibre Channel (FC).
See http://www.t11.org.

# 6. Security Considerations

This iSCSI naming format does not introduce any new security concerns
for the iSCSI protocol beyond those of the other iSCSI naming
formats.  Please refer to [RFC3720], Section 8, for information on
the security considerations for the iSCSI protocol.

# 7. References

## 7.1. Normative References

[RFC3720]  Satran, J., Meth, K., Sapuntzakis, C., Chadalapaka, M.,
and E. Zeidner, "Internet Small Computer Systems Interface
(iSCSI)", RFC 3720, April 2004.

[FC-FS]    INCITS 373-2003, Fibre Channel Framing and Signaling
Interface (FC-FS).

## 7.2. Informative References

[SPC3]     T10/1416-D, SCSI Primary Commands - 3 (SPC-3).

[SAM3]     T10/1561-D, SCSI Architecture Model - 3 (SAM-3).

[IB]       InfiniBand{tm} Architecture Specification, Vol. 1, Rel.
1.0.a, InfiniBand Trade Association
(http://www.infinibandta.org).

[SRP]      INCITS 365-2002, SCSI RDMA Protocol (SRP).

[SAS]      INCITS 376-2003, Serial Attached SCSI (SAS).

# Authors' Addresses

Marjorie Krueger
Hewlett-Packard Company
8000 Foothills Blvd.
Roseville, CA 95747-5668, USA

EMail: marjorie_krueger@hp.com

Mallikarjun Chadalapaka
Hewlett-Packard Company
8000 Foothills Blvd.
Roseville, CA 95747-5668, USA

EMail: cbm@rose.hp.com

Rob Elliott
Hewlett-Packard Company
MC 140801
PO Box 692000
Houston, TX 77269-2000, USA

EMail: elliott@hp.com

Full Copyright Statement

Copyright (C) The Internet Society (2005).

This document is subject to the rights, licenses and restrictions
contained in BCP 78, and except as set forth therein, the authors
retain all their rights.

This document and the information contained herein are provided on an
"AS IS" basis and THE CONTRIBUTOR, THE ORGANIZATION HE/SHE REPRESENTS
OR IS SPONSORED BY (IF ANY), THE INTERNET SOCIETY AND THE INTERNET
ENGINEERING TASK FORCE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE
INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED
WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

Intellectual Property

The IETF takes no position regarding the validity or scope of any
Intellectual Property Rights or other rights that might be claimed to
pertain to the implementation or use of the technology described in
this document or the extent to which any license under such rights
might or might not be available; nor does it represent that it has
made any independent effort to identify any such rights.  Information
on the IETF's procedures with respect to rights in IETF Documents can
be found in BCP 78 and BCP 79.

Copies of IPR disclosures made to the IETF Secretariat and any
assurances of licenses to be made available, or the result of an
attempt made to obtain a general license or permission for the use of
such proprietary rights by implementers or users of this
specification can be obtained from the IETF on-line IPR repository at
http://www.ietf.org/ipr.

The IETF invites any interested party to bring to its attention any
copyrights, patents or patent applications, or other proprietary
rights that may cover technology that may be required to implement
this standard.  Please address the information to the IETF at ietf-
ipr@ietf.org.

Acknowledgement

Funding for the RFC Editor function is currently provided by the
Internet Society.
