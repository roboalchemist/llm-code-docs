# ITU Specification Errata

**Source**: Z-Wave Alliance 2025-B Specification Package
**Date**: 2026-03-07
**Version**: 2025-B

## Overview

Corrections and updates to Z-Wave specifications

This documentation is extracted from the official Z-Wave Alliance specification document.

## Table of Contents

- [Key Concepts](#key-concepts)
- [Specification Details](#specification-details)
- [References](#references)

## Key Concepts

This specification covers critical aspects of Z-Wave protocol implementation. For complete details, refer to the official Z-Wave specification documents.

## Specification Details

### Extracted Content

The following content has been extracted from the official Z-Wave specification:

```
Z-Wave Alliance ITU Specification
Errata List
Release 0.9.0

Z-Wave Alliance
May 30, 2025

Table of contents
1

Preamble
1.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Revision Record . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

3
3
3
4
5

2

INTRODUCTION
2.1 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Audience and Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

6
6
6

3

ERRATA LIST
3.1 Preamble length . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1.1 Reason for change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1.2 Existing text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.1.3 Proposed text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Beam addressing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.1 Reason for change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.2 Existing text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.3 Proposed text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Retransmission description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.1 Reason for change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.2 Existing text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.3 Proposed text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4 Transport Service Command Class . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.1 Reason for change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.2 Existing text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.3 Proposed text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.5 End of Frame field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.5.1 Reason for change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.5.2 Existing text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.5.3 Proposed text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

7
7
7
7
8
8
8
8
9
9
9
9
9
9
9
9
9
10
10
10
10

Specifications

4

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

Z-WAVE LONG RANGE PHY/MAC

References

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

May 30, 2025
11
12

This document may only be copied and distributed internally. Page 2

Specifications

1
1.1

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

May 30, 2025

Preamble
Description

This document contains a list of proposed changes to the ITU G.9959 OHY and MAC layer specification.
Reviewed and approved by the Z-Wave Alliance Core Stack Working Group (CSWG).

1.2

Disclaimer

THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 3

Specifications

1.3

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

May 30, 2025

Revision Record
Table 1.1: Revision History

Doc.
Rev

Date

By

Pages
fected

0.5.0
0.5.1
0.7.0
0.9.0

2022/06/23
2024/10/22
2025/03/21
2025/05/30

CSWG
CSWG
CSWG
TC

ALL
ALL
n/a
n/a

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

Af-

Brief Description of Changes
Initial Version
Conversion from Microsoft Word to RST.
Ready for the TC review.
Approved for IPR review.

This document may only be copied and distributed internally. Page 4

Specifications

1.4

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

May 30, 2025

Abbreviations
Table 1.2: Abbreviations

Abbreviation

Explanation

ITU
MAC
PHY

The International Telecommunication Union
Media Access Control layer
Physical layer

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 5

Specifications

2
2.1

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

May 30, 2025

INTRODUCTION
Purpose

This document holds a list of changes and bug fixes that the Z-Wave alliance would like to get updated
in the ITU G.9959 specification [1], when a cooperation between ITU and the Z-Wave alliance has
been established.

2.2

Audience and Prerequisites

Z-Wave MAC and PHY layer developers and certification testers.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 6

Specifications

3

May 30, 2025

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

ERRATA LIST

This section contains a number of proposed changes to the ITU G.9959 specification.
The changes and bug fixes in this specification will be used by Z-Wave protocol implementations and
all implementations of Z-Wave PHY/MAC shall follow the descriptions in section 3, instead of the
ITU G.9995 sections mentioned in each issue.

3.1

Preamble length

3.1.1 Reason for change
ITU G.9959 specifies that the minimum number of preamble bytes is different for singlecast/broadcast
frames and multicast frames. That is a strange requirement as a radio will always be designed to be
able to detect the minimum number of preambles, so setting a higher minimum for multicast seems
like a waste of bandwidth and added complexity for no apparent reason.
3.1.2 Existing text
Table 3.1: Table 7-10 - Minimum Preamble Length
Channel
Configurations

1
2
3

Rate

Minimum Preamble length in bytes

R1
R2
R3
R1
R2
R3
R1
R2
R3

Singlecast/
broadcast
10
10
n/a
10
10
40
n/a
n/a
24

Multicast

Beam

10
20
n/a
10
20
40
n/a
n/a
24

n/a
20
n/a
n/a
20
n/a
n/a
n/a
8

Table 3.2: Table A-10 - Minimum Preamble Length
Channel
Configurations

1
2
3

Rate

Minimum Preamble length in bytes

R1
R2
R3
R1
R2
R3
R1
R2
R3

Singlecast/
broadcast
10
10
n/a
10
10
40
n/a
n/a
24

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

Multicast

Beam

10
20
n/a
10
20
40
n/a
n/a
24

n/a
20
n/a
n/a
20
n/a
n/a
n/a
8

This document may only be copied and distributed internally. Page 7

Specifications

May 30, 2025

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

3.1.3 Proposed text
Table 3.3: Table 7-10 - Minimum Preamble Length
Channel
Configurations

1
2
3

Rate

Minimum Preamble length in bytes

R1
R2
R3
R1
R2
R3
R1
R2
R3

Singlecast/
broadcast
10
10
n/a
10
10
40
n/a
n/a
24

Multicast

Beam

10
10
n/a
10
10
40
n/a
n/a
24

n/a
20
n/a
n/a
20
n/a
n/a
n/a
8

Table 3.4: Table A-10 - Minimum Preamble Length
Channel
Configurations

1
2
3

3.2

Rate

Minimum Preamble length in bytes

R1
R2
R3
R1
R2
R3
R1
R2
R3

Singlecast/
broadcast
10
10
n/a
10
10
40
n/a
n/a
24

Multicast

Beam

10
10
n/a
10
10
40
n/a
n/a
24

n/a
20
n/a
n/a
20
n/a
n/a
n/a
8

Beam addressing

3.2.1 Reason for change
Z-Wave has introduced a multicast beaming feature. For optimizing that feature for fragmented
beaming, it should be allowed to send and acknowledge to a broadcast beam so the sender of the
fragmented beam can stop transmission when an ack is received from all expected destinations.
3.2.2 Existing text
ITU G.9959 Section 8.1.3.11
“… A receiving node may interrupt the transmission of a fragmented beam by acknowledging a singlecast beam fragment. A receiving node shall not acknowledge a broadcast beam fragment…”

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 8

Specifications

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

May 30, 2025

3.2.3 Proposed text
ITU G.9959 Section 8.1.3.11
“… A receiving node may interrupt the transmission of a fragmented beam by acknowledging a singlecast beam fragment. A receiving node should acknowledge a broadcast beam fragment so the sender
can determine when to stop the transmission…”

3.3

Retransmission description

3.3.1 Reason for change
The retransmission description in section 8.1.5.1.4.3 and A.4.4.1.4.3 describes that when a node has
been waiting for an ACK for aMacMinAckWaitDuration it should deem the transmission failed and
start a retransmission after a random backoff. This wording prevents an implementation from deeming
a transmission successful if the ACK is received during the random backoff period.
3.3.2 Existing text
“…If an ACK MPDU is not received within aMacMinAckWaitDuration symbols, the transmission
attempt has failed. The originator shall repeat the process of transmitting the MPDU and waiting
for the ACK MPDU up to aMacMaxFrameRetries times. Before retransmitting, the node shall wait
for a random backoff period (see clause 8.1.5.1.4.4).”
3.3.3 Proposed text
““…If an ACK MPDU is not received within aMacMinAckWaitDuration symbols, the originator of
shall start the random backoff period (see clause 8.1.5.1.4.4) and repeat the process of transmitting
the MPDU and wait for the ACK MPDU up to aMacMaxFrameRetries times.”

3.4

Transport Service Command Class

3.4.1 Reason for change
The SAR layer and the transport service command class seems like it doesn’t belong to the PHY/MAC
specification, and it seems like a more natural approach is to remove the transport service command
class from the ITU specification and host in the Z-Wave alliance command class specifications, where
all other command classes are defined.
3.4.2 Existing text
Section 10.
3.4.3 Proposed text
Move section 10 to the Z-Wave alliance command class specification or network layer specification.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 9

Specifications

3.5

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

May 30, 2025

End of Frame field

3.5.1 Reason for change
The End of Frame delimiter in section 7.1.3.5 for data rate R1 is no longer used in Z-Wave implementations. It is not being transmitted and the receiver does not expect to receive it either.
3.5.2 Existing text
“…The EOF delimiter field shall be sent only when transmitting at data rate R1. The field shall
carry a sequence of 8 Manchester code violations each denoted E. Each violation, E, shall be a symbol
without transition. Refer to Figure 7-7.”
3.5.3 Proposed text
“…The EOF delimiter fields shall not be sent as it is considered obsolete, however receivers shall
handle receiving an End of Frame delimiter on data rate R1 consisting of a sequence of 8 Manchester
violations each denoted E.”

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 10

Specifications

4

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

May 30, 2025

Z-WAVE LONG RANGE PHY/MAC

The Z-Wave Long Range PHY and MAC layer specification is currently hosted by the Z-Wave alliance
NOT the ITU. Long term the Z-Wave alliance will work on getting both PHY/MAC specifications
under one standardization organization.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 11

Specifications

Z-Wave Alliance ITU Specification Errata List, Release 0.9.0

May 30, 2025

References
[1] ITU-T, G.9959. (01/2015).
[2] Z-Wave Alliance. ZWA_Z-Wave Long Range PHY and MAC Layer Specification.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 12


```

## References

- Z-Wave Alliance: https://z-wavealliance.org
- Z-Wave Specification Version: 2025-B
- Z-Wave Alliance Members Portal: https://sdomembers.z-wavealliance.org/

---

**Note**: This documentation is automatically extracted from official Z-Wave Alliance specifications.
For the most current and authoritative information, consult the official specification documents
available through the Z-Wave Alliance Members Portal.

**Last Updated**: 2026-03-07T20:11:55.897966
