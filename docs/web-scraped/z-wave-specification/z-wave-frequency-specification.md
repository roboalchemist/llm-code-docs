# Frequency Region Allocation

**Source**: Z-Wave Alliance 2025-B Specification Package
**Date**: 2026-03-07
**Version**: 2025-B

## Overview

Frequency bands and regional specifications

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

```text
Specifications

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

Z-Wave Alliance Frequency and
Region List
Release 1.9.0

Z-Wave Alliance
May 30, 2025

Table of contents
1

Preamble
1.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Audience and Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Revision Record . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.5 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2
2
2
2
3
4

2

INTRODUCTION
2.1 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

5
5

3

Z-WAVE COUNTRY, REGIONS AND FREQUENCIES

6

4

Z-WAVE LONG RANGE COUNTRIES, REGIONS AND FREQUENCIES

8

5

HOW TO ADD A REGION OR COUNTRY TO THE LIST

9

References

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

10

This document may only be copied and distributed internally. Page 1

Specifications

1
1.1

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

Preamble
Description

List of Z-Wave frequency allocation in different regions
Reviewed and approved by the Z-Wave Alliance Core Stack Working Group (CSWG).

1.2

Disclaimer

THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.

1.3

Audience and Requirements

The audience of this document is the Z-Wave Alliance members and Z-Wave developers.
Recipients of this document are requested to submit, with their comments, notification of any relevant
patent claims or other intellectual property rights of which they may be aware that might be infringed
by any implementation of the Specification set forth in this document, and to provide supporting
documentation.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 2

Specifications

1.4

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

Revision Record
Table 1.1: Revision History

Doc.
Rev

Date

0.1
0.5

2021/04/08 CSWG
2021/08/23 CSWG

0.5.1

0.5.5
0.5.6

2021/10/26 Silicon
Labs
2022/03/16 Silicon
Labs
2023/04/24 Silicon
Labs
2023/06/06 Silicon
Labs
2024/10/22 CSWG
2025/01/16 CSWG

0.7.0
0.9.0
1.0.0
1.5.0

2025/01/23
2025/01/31
2025/04/16
2025/03/11

0.5.2
0.5.3
0.5.4

1.5.1
1.7.0
1.9.0

By

CSWG
CSWG
CSWG
MK
Logic
2025/03/21 CSWG
2025/03/25 CSWG
2025/05/30 TC

Pages
fected

Af-

Brief Description of Changes

ALL
Front page,
header,
footer
None

Initial Version
Cleanup for Alliance review

None
Section 4
Table 3, Table 4
All
Table 4.1
n/a
n/a
n/a
Table Table
3.2
Table 3.2
n/a
n/a

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

CSWG review done. Adding Pakistan region as requested in review comment.
Nicaragua and Dominican Republic frequency allocations obsoleted
Adding Z-Wave LR for Canada and renaming USLR
to US_LR
Added Z-Wave Long Range for Europe
Conversion from Microsoft Word to RST.
Shift EU_LR frequency to comply with ETSI regulation.
Ready for the TC review.
Approved by TC. Ready for the IPR review.
Approved for Publication.
Fixed table header.
Add Kenya in the Z-Wave country list.
Ready for the TC review.
Approved for IPR review.

This document may only be copied and distributed internally. Page 3

Specifications

1.5

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

Abbreviations
Table 1.2: Abbreviations

Abbreviation

Explanation

RF

Radio Frequency

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 4

Specifications

2
2.1

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

INTRODUCTION
Purpose

This document lists the approved regions and frequencies within the Z-Wave ecosystem.
This document is the basis for the selections available in the Certification Form.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 5

Specifications

3

May 30, 2025

Z-Wave Alliance Frequency and Region List, Release 1.9.0

Z-WAVE COUNTRY, REGIONS AND FREQUENCIES
Table 3.1: Z-Wave Frequency Plans

Frequency
Plan

Channel
Config*

ANZ
2
CN
2
EU
2
HK
2
IL
2
IN
2
JP
3
KR
3
RU
2
US
2
* Refer to ITU-T G.9959

Center Frequency (MHz)

Data Rate*

F1
919.80
868.40
869.85
919.80
916.00
865.20
922.50
920.90
869.00
916.00

F1
R3
R1+R2+R3
R3
R3
R1+R2+R3
R1+R2+R3
R3
R3
R1+R2+R3
R3

F2
921.40
–
868.40
919.80
–
–
923.90
921.70
–
908.40

F3
–
–
–
–
–
–
926.30
923.10
–
–

F2
R2+R1
–
R2+R1
R2+R1
–
–
R3
R3
–
R2+R1

F3
–
–
–
–
–
–
R3
R3
–
–

Table 3.2: Country-Region Frequency List
Country/Region

Standard

Frequency Plan

Algeria
Argentina
Armenia
Australia
Bahamas
Bahrain
Barbados
Bermuda
Bolivia
Brazil
British Virgin Islands
Canada
Cayman Islands
CEPT* Cyprus Moldova
Chile
China

EN 300 220
FCC CFR47 Part 15.249
EN 300 220
AS/NZS 4268
FCC CFR47 Part 15.249
EN 300 220
FCC CFR47 Part 15.249
FCC CFR47 Part 15.249
FCC CFR47 Part 15.249
ANATEL Resolution 506
FCC CFR47 Part 15.249
FCC CFR47 Part 15.249
FCC CFR47 Part 15.249
EN 300 220
AS/NZS 4268
CNAS / EN 300 220 / CMIIT
2016DJ7232
FCC CFR47 Part 15.249
ARIB T96, ARIB STD-T108
ARCOTEL Resolution 12-09ARCOTEL-2107,Note EQA.45
EN 300 220
AS/NZS 4268
EN 300 220
EN 300 220
FCC CFR47 Part 15.249
FCC CFR47 Part 15.249
FCC CFR47 Part 15.249
HKTA 1035
CSR 564 (E)
Regulation No.161 Tahun 2019
EN 300 220

HK
US
EU
ANZ
US
EU
US
US
US
ANZ
US
US
US
EU
ANZ
CN

Colombia
Costa Rica
Ecuador
Egypt
El Salvador
French Guiana
Georgia
Guatemala
Haiti
Honduras
Hong Kong
India
Indonesia
Iraq
Israel
Jamaica

FCC CFR47 Part 15.249

US
JP
ANZ
EU
ANZ
EU
EU
US
US
US
HK
IN
ANZ
EU
IL
US
continues on next page

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 6

Specifications

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

Table 3.2 – continued from previous page
Country/Region

Standard

Frequency Plan

Japan
Jordan
Kazakstan
Kenya
Kuwait
Lebanon
Libya
Macau

ARIB STD-T108
EN 300 220
EN 300 220
EN 300 220
EN 300 220
EN 300 220
EN 300 220
Clause 2, Article 58-2 of Radio
Waves Act
MCMC MTSFBTC T007:2014
EN 300 220
EN 300 220
FCC CFR47 Part 15.249
CNAS / EN 300 220 / CMIIT
2016DJ7232
AS/NZS 4268
EN 300 220
EN 300 220
SRO 287(I)/2016
FCC CFR47 Part 15.249
AS/NZS 4268
AS/NZS 4268
EN 300 220
EN 300 220
GKRCh/EN 300 220
EN 300 220
IMDA TS SRD
ICASA/EN 300 220
Clause 2, Article 58-2 of Radio
Waves Act
FCC CFR47 Part 15.249
FCC CFR47 Part 15.249
Changed from JP May 2017
Clause 2, Article 58-2 of Radio
Waves Act
FCC CFR47 Part 15.249
EN 300 220
FCC CFR47 Part 15.249
EN 300 220
AS/NZS 4268
FCC CFR47 Part 15.249
Uz.SMT.01.334.1961745

JP
EU
EU
EU
EU
EU
EU
KR

Malaysia
Maldives
Mauritius
Mexico
Morocco
New Zealand
Nigeria
Oman
Pakistan
Panama
Paraguay
Peru
Philippines
Qatar
Russia
Saudi Arabia
Singapore
South Africa
South Korea
St Kitts & Nevis
Suriname
Taiwan
Thailand
Trinidad & Tabago
Turkmenistan
Turks & Caicos Islands
UAE
Uruguay
USA
Uzbekistan
Venezuela
Vietnam
Yemen

AS/NZS 4268
EN 300 220

ANZ
EU
EU
US
CN
ANZ
EU
EU
IN
US
ANZ
ANZ
EU
EU
RU
EU
KR
EU
KR
US
US
KR
KR
US
EU
US
EU
ANZ
US
EU
ANZ
ANZ
EU

Frequency allocation obsoleted because of changes in locate RF regulatory rules. Z-Wave Alliance is
working on a solution.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 7

Specifications

4

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

Z-WAVE LONG RANGE COUNTRIES, REGIONS AND FREQUENCIES
Table 4.1: Z-Wave Long Range Frequency Plans

Frequency
Plan

Channel
Config*

Center Frequency (MHz)

Data Rate*

FLR1
FLR2
FLR1
US_LR
1, 2
912.00
920.00
LR1
EU_LR
1, 2
864.00
866.00
LR1
* Refer to ZWA_Z-Wave Long Range PHY and MAC Layer Specification_SPE

FLF2
LR1
LR1

Table 4.2: Z-Wave Long Range Country-Region Frequency List
Country/Region

Standard

Frequency Plan

USA
FCC CFR47 Part 15.247
US_LR
Canada
FCC CFR47 Part 15.247
US_LR
Europe*
EN 300 220
EU_LR
* Note that there are special regulatory requirements for LBT, duty cycle and transmit times in
this region

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 8

Specifications

5

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

HOW TO ADD A REGION OR COUNTRY TO THE LIST

Existing frequency plans must be used whenever possible, but any member of the Z-Wave Alliance
may request support for a new country or region within the Z-Wave eco-system.
Member must provide references to the country/region’s RF regulatory and email it to the Core Stack
Working Group CSWG-chair@sdomembers.z-wavealliance.org for approval.
Once approved the CSWG will update and share this list with the Product Certification & Ecosystem
Working Group for certification update.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 9

Specifications

Z-Wave Alliance Frequency and Region List, Release 1.9.0

May 30, 2025

References
[1] ITU-T, G.9959. (01/2015).
[2] Z-Wave Alliance. ZWA_Z-Wave Long Range PHY and MAC Layer Specification.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 10


```

## References

- Z-Wave Alliance: https://z-wavealliance.org
- Z-Wave Specification Version: 2025-B
- Z-Wave Alliance Members Portal: https://sdomembers.z-wavealliance.org/

---

**Note**: This documentation is automatically extracted from official Z-Wave Alliance specifications.
For the most current and authoritative information, consult the official specification documents
available through the Z-Wave Alliance Members Portal.

**Last Updated**: 2026-03-07T20:11:55.857384
