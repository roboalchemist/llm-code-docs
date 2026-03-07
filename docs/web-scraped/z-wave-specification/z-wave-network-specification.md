# Network Layer Specification

**Source**: Z-Wave Alliance 2025-B Specification Package
**Date**: 2026-03-07
**Version**: 2025-B

## Overview

Network layer routing, addressing, and protocol mechanics

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
Z-Wave and Z-Wave Long Range
Network Layer Specification
Release 5.9.0

Z-Wave Alliance
Aug 20, 2025

Table of contents
1

Preamble
1.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Audience and Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Revision Record . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.5 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

8
8
8
8
9
11

2

INTRODUCTION
2.1 Z-Wave technology overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2 Z-Wave Long Range technology overview . . . . . . . . . . . . . . . . . . . . . . . . .
2.3 Network layer specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.4 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12
12
12
12
12

3

Z-WAVE PROTOCOL OVERVIEW
3.1 The Z-Wave protocol stack architecture . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Network Layer reference model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Z-Wave definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.1 Z-Wave network topology basic principles . . . . . . . . . . . . . . . . . . . . .
3.3.2 Controller and end nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.3 Network topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.4 Z-Wave controller roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.4.1 Primary Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.4.2 Secondary Controller . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.4.3 SUC Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.4.4 SIS Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.4.5 Inclusion Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.5 Node operation modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.5.1 Always Listening (AL) . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.5.2 Frequently Listening (FL) . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.5.3 Non-Listening (NL) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.6 Network addressing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

14
14
16
17
17
17
18
18
18
18
19
19
19
19
19
19
20
20

4

Z-WAVE NETWORK LAYER SPECIFICATION
4.1 General Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1.1 Z-Wave NWK Layer overview . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.1.2 Network Layer Data Entity (NLDE) . . . . . . . . . . . . . . . . . . . . . . . .
4.1.2.1 Network Layer Management Entity (NLME) . . . . . . . . . . . . . .
4.2 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.1 NPDU formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2 Routed NPDUs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1 General routing header format . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.1 Routed Speed Modified (1 bit) / Failed Hop (4 bits) . . . . .
4.2.2.1.2 Extended Header (1 bit) . . . . . . . . . . . . . . . . . . . .
4.2.2.1.3 R-Err (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.4 R-Ack (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.5 Direction (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.6 Repeaters (4 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.7 Hops (4 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.8 Repeater 0 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.9 Repeater 1 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.10 Repeater 2 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.11 Repeater 3 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.1.12 Destination Wake Up (8 bits) . . . . . . . . . . . . . . . . .
4.2.2.1.13 Extended Header Body Length (4 bits) . . . . . . . . . . . .
4.2.2.1.14 Extended Header Type (4 bits) . . . . . . . . . . . . . . . . .
4.2.2.2 Extended headers . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.2.1 Destination Wake Up Type . . . . . . . . . . . . . . . . . . .
4.2.2.2.2 Incoming Routed RSSI Type . . . . . . . . . . . . . . . . . .
4.2.2.3 Routing Frames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.3.1 Routed frame . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2.3.2 Routed Acknowledgment frame . . . . . . . . . . . . . . . . .
4.2.2.3.3 Routed Error frame . . . . . . . . . . . . . . . . . . . . . . .
4.2.3 Explore NPDUs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1 Explore frame general header format . . . . . . . . . . . . . . . . . . .
4.2.3.1.1 Version (3 bits) . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.2 Command (5 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.3 Direction (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.4 Source Routed (1 bit) . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.5 Stop (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.6 Session Tx Random Interval (8 bits) . . . . . . . . . . . . . .
4.2.3.1.7 TTL (4 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.8 Repeater Count (4 bits) . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.9 Repeater 0 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.10 Repeater 1 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.11 Repeater 2 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.1.12 Repeater 3 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.2 Normal Explore Frame . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.2.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.2.2 Fields description . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.2.3 Additional payload . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.3 Inclusion Request Explore Frame . . . . . . . . . . . . . . . . . . . . .
4.2.3.3.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.3.2 Fields description . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.3.3 Additional payload . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.4 Search Result Explore Frame . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.4.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.4.2 Fields description . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3.4.3 Additional payload . . . . . . . . . . . . . . . . . . . . . . . .
4.3 Command Frames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.1 No Operation Command Class . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2 Z-Wave Protocol Command Class . . . . . . . . . . . . . . . . . . . . . . . . .

21
21
21
21
22
23
23
24
24
25
25
26
26
26
26
26
27
27
27
27
27
27
27
28
28
28
29
29
30
30
30
30
31
31
31
31
31
32
32
32
32
32
33
33
33
33
33
33
34
34
34
34
35
35
35
36
37
38
38

4.3.2.1

Node Information Frame Command . . . . . . . . . . . . . . . . . . .
4.3.2.1.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.1.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.1.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.2 Request Node Information Frame Command . . . . . . . . . . . . . .
4.3.2.2.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.2.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.2.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.3 Assign IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.3.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.3.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.3.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.4 Find Nodes in Range Command . . . . . . . . . . . . . . . . . . . . .
4.3.2.4.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.4.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.4.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.5 Get Nodes in Range Command . . . . . . . . . . . . . . . . . . . . . .
4.3.2.5.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.5.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.5.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.6 Range Info Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.6.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.6.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.6.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.7 Command Complete Command . . . . . . . . . . . . . . . . . . . . .
4.3.2.7.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.7.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.7.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.8 Transfer Presentation Command . . . . . . . . . . . . . . . . . . . . .
4.3.2.8.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.8.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.8.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.9 Transfer Node Information Command . . . . . . . . . . . . . . . . . .
4.3.2.9.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.9.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.9.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.10 Transfer Range Information Command . . . . . . . . . . . . . . . . .
4.3.2.10.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.10.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.10.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.11 Transfer End Command . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.11.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.11.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.11.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.12 Assign Return Route Command . . . . . . . . . . . . . . . . . . . . .
4.3.2.12.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.12.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.12.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.13 New Node Registered Command . . . . . . . . . . . . . . . . . . . . .
4.3.2.13.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.13.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.13.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.14 New Range Registered Command . . . . . . . . . . . . . . . . . . . .
4.3.2.14.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.14.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.14.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.15 Transfer New Primary Controller Complete Command . . . . . . . . .
4.3.2.15.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.15.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .

40
40
43
43
44
44
44
44
45
45
45
45
46
46
47
47
49
49
49
49
50
50
51
51
52
52
52
52
53
53
53
54
55
55
55
55
56
56
56
56
57
57
58
58
59
59
60
60
61
61
61
62
63
63
64
64
65
65
65

4.3.2.15.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.16 Automatic Controller Update Start Command . . . . . . . . . . . . .
4.3.2.16.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.16.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.16.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.17 SUC Node ID Command . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.17.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.17.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.17.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.18 Set SUC Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.18.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.18.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.18.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.19 Set SUC ACK Command . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.19.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.19.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.19.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.20 Assign SUC Return Route Command . . . . . . . . . . . . . . . . . .
4.3.2.20.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.20.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.20.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.21 Static Route Request Command . . . . . . . . . . . . . . . . . . . . .
4.3.2.21.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.21.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.21.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.22 Lost Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.22.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.22.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.22.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.23 Accept Lost Command . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.23.1 Frame Format: . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.23.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.23.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.24 NOP Power Command . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.24.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.24.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.24.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.25 Reserve Node IDs Command . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.25.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.25.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.25.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.26 Reserved IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.26.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.26.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.26.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.27 Nodes Exist Command . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.27.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.27.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.27.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.28 Nodes Exist Reply Command . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.28.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.28.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.28.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.29 Set NWI Mode Command . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.29.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.29.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.29.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.30 Exclude Request Command . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.30.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .

65
66
66
66
66
67
67
67
67
68
68
68
68
69
69
69
69
70
70
70
70
71
71
71
71
72
72
72
72
74
74
74
74
75
75
76
76
77
77
77
77
78
78
78
78
79
79
79
79
80
80
80
80
81
81
81
81
82
82

4.4
4.5

4.3.2.30.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.30.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.31 Assign Return Route Priority Command . . . . . . . . . . . . . . . .
4.3.2.31.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.31.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.31.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.32 Assign SUC Return Route Priority Command . . . . . . . . . . . . .
4.3.2.32.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.32.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.32.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.33 SmartStart Included Node Information Command . . . . . . . . . . .
4.3.2.33.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.33.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.33.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.34 SmartStart Prime Command . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.34.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.34.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.34.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.35 SmartStart Inclusion Request Command . . . . . . . . . . . . . . . .
4.3.2.35.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.35.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.35.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Functional Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1 Routing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1.1 Assigning Return Routes . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1.2 Priority Routes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1.3 General Routing Requirements . . . . . . . . . . . . . . . . . . . . . .
4.5.1.3.1 AL Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1.3.2 Repeating Frames . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1.3.3 FL and NL Nodes . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1.4 Successfully Delivered Routed Frame . . . . . . . . . . . . . . . . . .
4.5.1.4.1 Channel Configuration 1,2 . . . . . . . . . . . . . . . . . . .
4.5.1.4.2 Channel Configuration 3 . . . . . . . . . . . . . . . . . . . .
4.5.1.5 Routed Singlecast to an FL Node Destination . . . . . . . . . . . . .
4.5.1.5.1 Channel Configuration 1,2 . . . . . . . . . . . . . . . . . . .
4.5.1.5.2 Channel Configuration 3 . . . . . . . . . . . . . . . . . . . .
4.5.1.6 Unsuccessful Routed Frame with Routed Error Frame . . . . . . . . .
4.5.1.7 Unsuccessful Routed Frame Without Routed Error Frame . . . . . . .
4.5.1.8 Normal and Search Result Explore frames . . . . . . . . . . . . . . . .
4.5.2 Learn Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.3 Network Formation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.4 Network Inclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.4.1 Classic Network Inclusion . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.4.2 Network Wide Inclusion (NWI) . . . . . . . . . . . . . . . . . . . . .
4.5.4.3 SmartStart Inclusion . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.4.3.1 SmartStart Supporting Nodes Power-Up . . . . . . . . . . .
4.5.4.3.2 Not Included Nodes . . . . . . . . . . . . . . . . . . . . . . .
4.5.4.3.3 Included Nodes . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.4.3.4 SmartStart Including Controllers . . . . . . . . . . . . . . . .
4.5.4.3.5 Successful SmartStart Inclusion . . . . . . . . . . . . . . . .
4.5.4.3.6 Unsuccessful SmartStart Inclusion . . . . . . . . . . . . . . .
4.5.5 Network Exclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.5.1 Classic Network Exclusion . . . . . . . . . . . . . . . . . . . . . . . .
4.5.5.2 Network Exclusion From a Foreign Network . . . . . . . . . . . . . .
4.5.5.3 Network Wide Exclusion (NWE) . . . . . . . . . . . . . . . . . . . . .
4.5.6 Failing Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.6.1 Remove a Failing Node . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.6.1.1 AL and FL Nodes . . . . . . . . . . . . . . . . . . . . . . . .

82
82
83
83
83
83
84
84
84
84
85
85
86
86
87
87
87
87
88
88
88
88
90
91
91
91
91
91
92
92
92
92
92
93
94
95
96
96
97
98
100
101
102
102
104
106
106
106
108
108
109
112
114
114
115
117
119
119
119

4.5.6.1.2 NL nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Controller Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.7.1 Role transitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.7.2 Primary Controller Shift . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.7.3 Give the SUC/SIS Role . . . . . . . . . . . . . . . . . . . . . . . . . .
Inclusion Controllers functionalities . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.8.1 Add New Nodes on behalf of the SIS . . . . . . . . . . . . . . . . . .
4.5.8.2 Remove Nodes on behalf of the SIS . . . . . . . . . . . . . . . . . . .
Network Maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.9.1 Automatic Controller Update . . . . . . . . . . . . . . . . . . . . . . .
4.5.9.2 SUC updates by the Primary Controller . . . . . . . . . . . . . . . . .
4.5.9.3 Controller Replication . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.9.4 Neighbour Discovery / Range Test . . . . . . . . . . . . . . . . . . . .
4.5.9.5 End Node Route Request . . . . . . . . . . . . . . . . . . . . . . . . .

120
120
120
121
122
124
124
125
127
127
130
131
132
134

5

Z-WAVE LONG RANGE PROTOCOL OVERVIEW
5.1 The Z-Wave Long Range Protocol Stack Architecture . . . . . . . . . . . . . . . . . .
5.2 Z-Wave Long Range Network Layer Reference Model . . . . . . . . . . . . . . . . . . .
5.3 Z-Wave Long Range Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.1 Z-Wave Long Range Network Principles . . . . . . . . . . . . . . . . . . . . . .
5.3.2 Controller and End Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.3 Network Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.4 Z-Wave Controller Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.5 Node Operation Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.5.1 Wake On Event End Node (WOEEN) . . . . . . . . . . . . . . . . . .
5.3.6 Network Addressing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

137
137
138
139
139
139
139
139
139
139
140

6

Z-WAVE LONG RANGE NETWORK LAYER SPECIFICATION
6.1 General Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.1 Z-Wave Long Range NWK Layer Overview . . . . . . . . . . . . . . . . . . . .
6.1.2 Network Layer Data Entity (NLDE) . . . . . . . . . . . . . . . . . . . . . . . .
6.1.2.1 Network Layer Management Entity (NLME) . . . . . . . . . . . . . .
6.2 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.1 NPDU formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3 Command Frames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1 Z-Wave Long Range Command Class . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.1 No Operation Command . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.1.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.1.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.1.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.2 Node Information Frame Command . . . . . . . . . . . . . . . . . . .
6.3.1.2.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.2.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.2.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.3 Request Node Information Frame Command . . . . . . . . . . . . . .
6.3.1.3.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.3.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.3.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.4 Assign IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.4.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.4.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.4.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5 Exclude Request Command . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.6 SmartStart Included Node Information Command . . . . . . . . . . .
6.3.1.6.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.6.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.6.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .

141
141
141
141
141
142
142
143
144
145
145
145
145
146
146
147
147
148
148
148
148
149
149
149
149
150
150
150
150
151
151
151
151

4.5.7

4.5.8
4.5.9

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

6.3.1.7

6.4
6.5

SmartStart Prime Command . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.7.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.7.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.7.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.8 SmartStart Inclusion Request Command . . . . . . . . . . . . . . . .
6.3.1.8.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.8.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.8.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.9 Exclude Request Confirmation Command . . . . . . . . . . . . . . . .
6.3.1.9.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.9.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.9.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.10 Non Secure Inclusion Step Complete Command . . . . . . . . . . . .
6.3.1.10.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.10.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.10.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . .
Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Functional Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1 Communication between Z-Wave Long Range Nodes . . . . . . . . . . . . . . .
6.5.1.1 Wake On Event End Node (WOEEN) . . . . . . . . . . . . . . . . . .
6.5.2 Learn Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.3 Network Formation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.4 Z-Wave Long Range Network Inclusion . . . . . . . . . . . . . . . . . . . . . .
6.5.4.1 SmartStart Inclusion . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.4.1.1 SmartStart Supporting Nodes Power-Up . . . . . . . . . . .
6.5.4.1.2 SmartStart Including Controllers . . . . . . . . . . . . . . . .
6.5.4.1.3 Successful SmartStart Inclusion . . . . . . . . . . . . . . . .
6.5.4.1.4 Unsuccessful SmartStart Inclusion . . . . . . . . . . . . . . .
6.5.4.1.5 Inclusion of Wake On Event End Nodes . . . . . . . . . . . .
6.5.5 Z-Wave Long Range Network Exclusion . . . . . . . . . . . . . . . . . . . . . .
6.5.5.1 Network Exclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.5.2 Network Exclusion From a Foreign Network . . . . . . . . . . . . . .
6.5.6 Failing nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.6.1 Remove a Failing Node . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.6.1.1 AL and FL Nodes . . . . . . . . . . . . . . . . . . . . . . . .
6.5.6.1.2 NL Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.6.1.3 Wake On Event End Nodes . . . . . . . . . . . . . . . . . . .
6.5.7 Controller Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.8 Dual Z-Wave and Z-Wave Long Range Networks . . . . . . . . . . . . . . . . .

References

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

152
152
152
152
153
153
153
153
154
154
154
154
155
155
155
155
156
157
157
157
158
159
160
160
160
162
162
164
166
167
167
168
170
170
170
171
171
172
173
174

This document may only be copied and distributed internally. Page 7

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

1
1.1

Preamble
Description

This specification defines the Network (NWK) layer for ITU-T G.9959 compliant transceivers and
Z-Wave long Range transceivers, which enables network operations and routing on Z-Wave networks.
Implementations claiming compliance with this specification can be used with an application layer to
certify Z-Wave and Z-Wave long range products.
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

This document may only be copied and distributed internally. Page 8

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

1.4

Revision Record
Table 1.1: Revision History

Doc. Date
Rev

By

Pages
Affected

Brief Description of Changes

0.1
0.3
0.5
0.7

2020.07.01
2020.09.01
2020.09.24
2020.09.28

CSWG
CSWG
CSWG
CSWG

Z-Wave Network Layer v.0.7 initial document
Z-Wave Long Range network layer added
Implemented review comments
Made document ready for Z-Wave alliance donation

0.7.1

2020.11.23

CSWG

ALL
ALL
ALL
Frontpage,
header and
footer
6.3.1.2
4.3.2.13
6.3

All
References
6.3.1.2.1.1
6.5.1
6.4

0.7.2

2021.02.26

CSWG

0.8
0.9
1.0

2021.03.01
2021.03.29
2021.08.27

None
Frontpage

1.5

2021.10.19

CSWG
CSWG
ZWA
Board
Sensative
AB
Silicon
Labs

4.5.4.3
6.5.4.1
4.5.4.2
4.3.2.13.2

1.7

2022.04.19

CSWG

Frontpage

1.9

2022.05.04

CSWG

Frontpage

2.5

2023.03.02

CSWG

Frontpage,
header and
footer
4.3.2.1
4.3.2.5
4.3.2.11
4.3.2.13
4.5.9.4
4.5.4.3.1.2
6.5.4.1.1.2
4.3.2.12.2

2.9

2023-0526

CSWG

Revision

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

Added speed bits to the LR Node Information Frame
Added description of Command Class field in New
Node Registered command
Fixed LR command class numbers in frame figures
Fixed LR command class numbers in frame figures
Fixed references to alliance documents
Added neighbour discovery to figures Figure 4.80 and
Figure 4.90
Replaced “slave node” with “end node”
Fixed reference names
Fixed table reference
Removed reference to undefined constant
Changed description of nwkLRExcludeRequestForeignNetBackOff to fit Long Range frame names
Initial review by TC done, updating revision to 0.8
Cleanup for IPR review
Approved for Publication
Updated SmartStart behavior for battery powered up
end devices
Added missing figure 4.68
Clarified the use of New Node Registered when removing a node
Reviewed by CSWG, Updated version to 1.7 for TC
review
Reviewed by TC, Updated version to 1.9 for IPR review
Updated version and dates
Updated the Routing text in the Node Information
Frame command
Added optional Wake Up Time field to the Get Nodes
In Range command
Updated Status text in the Network Transfer End
command
Fixed missing Speed Extension field in the New Node
Registered command
Added clarification on FL nodes optionally finding
other FL nodes in the neighbor discovery process
Updated description of INIF transmission to match
previous change to SmartStart triggering
Updated description of the use of Assign Return
Route to the SUC nodeID
Document approved by CSWG and TC
continues on next page
This document may only be copied and distributed internally. Page 9

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

Table 1.1 – continued from previous page
Doc. Date
Rev

By

3.0

2023.07.20

3.5
3.7

2023.11.28
2023.12.20

ZWA
BoD
CSWG
CSWG

3.7.1

2024.01.24

CSWG

4.5.0
4.5.1

2024.10.16
2024.10.31

CSWG
CSWG

4.5.2

2024.12.05

CSWG

4.5.3

2024.12.10

CSWG

4.5.4

2025.02.14

4.7.0
4.9.0
5.0.0

2025.03.25
2025.05.30
tbd

5.1.0

2025.07.22

MK
Logic
CSWG
CSWG
ZWA
BoD
WePower

5.7.0
5.9.0

2025.07.28
2025.08.20

CSWG
TC

Pages
Affected

Brief Description of Changes
Approved by the Z-Wave Alliance Board of Directors

6.4
Frontpage

Add constant nwkMinTransmitAttempts
Reviewed by CSWG, Updated version to x.7 for TC
review
6.5.1
Restore requirement LR-NWK:004B.1 (removed in
0.7.2)
all
Migration from Word to GitHub
all
Migration related fixes for formatting and missing requirement numbers
Frame For- Add requirement numbers for formats referenced by
mat
the test specifications (NWK:0205.1, NWK:0206.1,
NWK:0207.1, NWK:0208.1, NWK:0209.1, and
NWK:020A.1)
Get Nodes Fix duplicate requirement number on Wake Up
in
Range Time (optional) field.
Was NWK:00A6.1, now
Command
NWK:020B.1
Neighbour
Fix duplicate requirement number on requirement
Discovery / stating that FL nodes may be asked to find other
Range Test
FL nodes in the neighbour discover process. Was
NWK:01FC.1, now NWK:020C.1
NWK:0063.1 Rename Confusing field in Node Information Frame
NWK:00E1.2 Command (maximume speed => supported speed)
NWK:014B.1
NWK:0171.1
LR-NWK:0013.1
all
Rename Security bit in Node Information to RFU
(NWK:006E.1, GH-10)
4.3.*, 6.3.*
Fixed string identifiers of Command Classes and
Commands in accordance with the Z-Wave XML.
n/a
Ready for the TC review.
n/a
Approved by TC.
n/a
Approved by the Z-Wave Alliance Board of Directors
5.3.5
6.5.1
6.5.6
6.5.6.1
6.5.4.1
n/a
n/a

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

Added Subsection for Wake On Event End Node
Added Subsection for Wake On Event End Node
Added Exception for Wake On Event End Node
Added Subsection for Wake On Event End Node
Added Subsection for Wake On Event End Node
Ready for the TC review.
Approved by TC for IPR review.

This document may only be copied and distributed internally. Page 10

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

1.5

Abbreviations
Table 1.2: Abbreviations

Abbreviation

Explanation

AL
APL
DLPDU
FL
ISM
MAC
MPDU
NIB
NIF
NLDE
NL
NPDU
NLME
NSDU
NWI
NWK
NLDE-SAP
NLME-SAP
MLDE-SAP
MLME-SAP
OSI
PLDE-SAP
PLME-SAP
PHY
RFU
S2
S2 DSK
SAP
SAR
SIS
SUC
WOEEN

Always Listening
Application Layer
Data Link Protocol Data Unit
Frequently Listening
(unlicensed) Industrial Scientific and Medical
Medium Access Control
MAC Protocol Data Unit
Network Information Base
Node Information Frame Command. Refer to 4.3.2.1
Network Layer Data Entity
Non-Listening
Network Layer Protocol Data Unit
Network Layer Management Entity
Network Service Data Unit
Network Wide Inclusion
Network Layer
Network Layer Data Entity - Service Access Point
Network Layer Management Entity - Service Access Point
MAC Layer Data Entity - Service Access Point
MAC Layer Management Entity - Service Access Point
Open System Interconnection
Physical Layer Data Entity – Service Access Point
Physical Layer Management Entity – Service Access Point
Physical layer
Reserved for Future Use
Security 2 Command Class. Refer to [ZWATECC]
Security 2 Device Specific Key. Refer to [ZWATECC]
Service Access Point
Segmentation and Reassembly
SUC ID Server
Static Update Controller
Wake On Event End Node

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 11

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

2

INTRODUCTION

2.1

Z-Wave technology overview

Z-Wave is a wireless mesh protocol oriented to the residential control and automation market but
also suitable for light commercial applications. The Z-Wave technology offers a simple yet reliable
method to wirelessly control lights, door locks, thermostats and a range of systems in residential and
commercial environments. The Z-Wave protocol works in the unlicensed industrial, scientific, and
medical (ISM) bands. The specific frequency band varies from region to region and the frequency
bands are defined in [ITUTG9959].
It is known that any wireless radio network may suffer from frequent frame drops due to fading effects,
spurious noise and reflections. To combat such conditions, the Z-Wave protocol provides a low-level
retransmission approach. In addition, the Z-Wave protocol employs a network layer mesh routing
protocol to extend networks beyond what is possible in direct range.

2.2

Z-Wave Long Range technology overview

Z-Wave Long Range provides an extended range version of the Z-Wave technology, targeting deployments over a kilometer radius, suitable in both indoors and outdoors areas. All Z-Wave applications
can run using either the Z-Wave or the Z-Wave Long Range PHY/MAC.
The Z-Wave Long Range protocol does not use any mesh routing and employs only direct range
communication.
The Z-Wave Long Range protocol also operate in the unlicensed industrial, scientific, and medical
(ISM) bands. The specific frequency band varies from region to region and the frequency bands are
defined in [ZWALRPHY], [ZWALRMAC].

2.3

Network layer specification

This specification presents the Z-Wave and Z-Wave Long Range Network Layer definitions that will
be implemented by devices operating in Z-Wave and Z-Wave Long Range networks. The Network
Layer features in relation to the OSI reference model and other layers is presented in Section 3.1 and
Section 5.1.

2.4

Glossary

The key words shall, should and may are formally used to indicate requirement levels in this document:
• Shall:
This word indicates that the definition is an absolute requirement of the specification.
• Should:
This word indicates that there may exist valid reasons in particular circumstances to ignore an item,
but the full implications must be understood and carefully weighed before choosing a different course.
• May:
This word indicates that an item is truly optional. One vendor may choose to include the item because
a marketplace requires it or because the vendor feels that it enhances the product while another vendor
may omit the same item.
An implementation which does not include an option shall be prepared to interoperate with another
implementation which does include the option, though perhaps with reduced functionality. In the
same vein an implementation which does include an option shall be prepared to interoperate with

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 12

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

another implementation which does not include the option (except, of course, for the feature the
option provides.)
The use of the key words shall, should and may is compliant with the requirement levels used in ITU
recommendations.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 13

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

3

Z-WAVE PROTOCOL OVERVIEW

The Z-Wave protocol is a low bandwidth half duplex protocol designed for reliable wireless communication in a low-cost control network. The main purpose of the protocol is to enable short message
transportation in a reliable manner. The Z-Wave protocol is not designed to transfer a large amount
of data or any kind of streaming or timing critical data.

3.1

The Z-Wave protocol stack architecture

The Open System Interconnection (OSI) reference model is a representation system for characterizing
and standardizing the functions of a communication system in terms of abstraction layers. This
allows us to describe similar communication functionalities into logical layers. The 7 layers of the OSI
model are regarded by many as an idealized model; too abstract and fine-grained for most real-world
protocols. It is however useful to refer to the OSI model when describing a given communication
protocol framework. With respect to that, the Z-Wave protocol stack would be described using the
model as shown in Figure 3.1. Note that the Z-Wave application layer consists of the OSI stack layers
knows as transport, session, presentation and application.
Application (APL) Layer
Z-Wave Device Type

Application Command Classes

Z-Wave Role Type

Transport-Encapsulation Command Classes (i.e., Security 2 Command Class)

NLDE-SAP

NLME-SAP

Network (NWK) Layer
Routing Management

Network Management (i.e., node inclusion/exclusion)

MLDE-SAP

MLME-SAP

Medium Access Control (MAC) Layer
Domain Identification

Collision Avoidance

Frame

Acknowledged Frame

Validation

Delivery

Frame Retransmission

PLDE-SAP

PLME-SAP

Physical (PHY) Layer
900Mhz Radio Transceiver

Layer Interface

Frequency Selection

Clear Channel Assessment

Link Budget Assessment

Layer Function

Z-Wave Alliance
Defined

ITU-T G9959
Defined

Figure 3.1: Z-Wave Protocol Stack Architecture
As depicted in Figure 3.1, the Z-Wave protocol stack is made up of OSI layers where each layer
performs set of services for the upper layer. Each layer has two main interfaces to facilitate the
communication with upper layers through a Service Access Point (SAP). The interfaces are described
as a data entity and management entity that provide a data transmission service and all other services,
respectively.
[ITUTG9959] defines the physical and medium access control layers.
• The physical layer offers a data flow control between the MAC and PHY layers and adds
PHY-related management headers. The PHY layer is responsible for activation and deactiva© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 14

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

tion of the radio transceiver, data transmission and reception, frequency selection, clear channel
assessments, and the link budget assessment of received frames.
• The MAC layer defines the Z-Wave data transfer model and frame structure. During a Z-Wave
frame transmission, the MAC layer takes the payload data from higher layers and construct the
MAC data payload (MPDU) and the MPDU header. The header comprises addresses, frame
control and frame length information. The frame control field is about 16 bits in length and
contains information about the frame type and other control flags that can be used by higher
layer.
On the foundation of those two lower layers, the Z-Wave alliance defines the Network layer (NWK)
and application layers.
The Z-Wave Network Layer (NWK) defines a multi-hop routing protocol, that is employed by Z-Wave
nodes to extend their communication range. It means that the Z-Wave nodes can therefore send
frames to nodes that are not in direct radio communication range. Besides, the Z-Wave NWK layer
is responsible for network formation (i.e., inclusion/exclusion of nodes to/from a network) and its
maintenance. The Z-Wave NWK layer manages the network establishment using command frames
known as the Z-Wave Protocol Command Class (described in Section 4.3). These Z-Wave NWK
commands are designed for network formation specific purposes.
NWK:002E.1

The Z-Wave application layer is responsible for building applications using dedicated Command
Classes, (defined in [ZWAACC], [ZWAMCC], [ZWATECC], [ZWANPCC]). In order to be certifiable,
applications shall comply with Z-Wave device types defined in [ZWADT] and [ZWADTV2]. Finally,
the applications layer is also responsible for providing some network management functionalities using
the NWK interface (for details, refer to [ZWART]).
This specification defines NWK layer. The upper and lower layers are outside the scope of this
specification.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 15

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

3.2

Network Layer reference model

The Network Layer (NWK) provides an interface between the application layer and the MAC layer.
The NWK layer relies on services provided by the MAC layer and offers services to higher layers
though the Network Layer Data Entity (NLDE) and Network Layer Management Entity (NLME)
service point interfaces. The NLME provides management service interface where the NWK layer
management functionalities can be invoked. The NLME is responsible for maintaining a Network
Information Base (NIB) that contains the routing information of the network. Figure 3.2 illustrates
the components and interface of NWK layer.

Application Layer

NLDE-SAP

NLME-SAP

NLME

NLDE

NIB

NLDE-SAP

MLME-SAP

MAC Layer

Figure 3.2: Network Layer Reference Model
NWK:0022.1

The Z-Wave NWK layer shall provide two services to the Application layer that are accessed through
two SAPs:
• The data service, accessed through NLDE-SAP, and
• The network management service accessed through the NLME-SAP.
The detailed description of the Z-Wave NWK functional model is presented in Section 4.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 16

Specifications Z-Wave and Z-Wave Long Range Network Layer Specification, Release 5.9.0
August 20, 2025

3.3

Z-Wave definitions

3.3.1 Z-Wave network topology basic principles
The following is a summary of the basic Network topology principles established by [ITUTG9959]:
1. Groups of nodes are divided into domains:
• The division of physical nodes into domains is logical. Domains may fully or partially
overlap each other’s radio frequency ranges.
• The Z-Wave Network Layer supports up to 232 domains.
• Each domain is identified by a unique HomeID.
• Management of different domains in the same physical media is handled by individual
domain masters.
2. The domain is a set of nodes connected to the same medium:
• One node in the domain operates as a domain master, known as the Primary Controller.
• Each domain may contain up to 232 nodes (including the domain master).
• Each node in the domain is identified by a NodeID that is unique within the actual domain.
• Nodes of the same domain can communicate with each other either directly or via other
nodes in the same domain.
3. Nodes of different G.9959 domains:
• The Z-Wave Network Layer provides connectivity within one domain.
In some cases, frames from a foreign domain are repeated into the current domain.
Inter-domain communication is beyond the scope of this specification.
4. The network is self-healing:
• Nodes may autonomously establish new routes on demand.
Full mesh routing is supported. There is no requirement for star or tree network topologies.
3.3.2 Controller and end nodes
The Z-Wave network layer defines two networking node types: controller and end.
The controller nodes are responsible for setting up and maintaining the Z-Wave network. They
can include or exclude nodes and they are aware for the network topology. This allows controllers
to determine the possible routes between any two nodes in the network. Co

[Content truncated for size. See full PDF for complete specification.]

```

## References

- Z-Wave Alliance: https://z-wavealliance.org
- Z-Wave Specification Version: 2025-B
- Z-Wave Alliance Members Portal: https://sdomembers.z-wavealliance.org/

---

**Note**: This documentation is automatically extracted from official Z-Wave Alliance specifications.
For the most current and authoritative information, consult the official specification documents
available through the Z-Wave Alliance Members Portal.

**Last Updated**: 2026-03-07T20:11:55.174130
