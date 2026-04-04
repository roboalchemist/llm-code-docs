# PHY and MAC Layer Specification

**Source**: Z-Wave Alliance 2025-B Specification Package
**Date**: 2026-03-07
**Version**: 2025-B

## Overview

Physical layer and MAC layer details

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
Z-Wave Long Range PHY and MAC Layer
Specification
Release 3.9.0

Z-Wave Alliance
Aug 20, 2025

Table of contents
1

Preamble
1.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Revision Record . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

6
6
6
7
8

2

DEFINITIONS

10

3

INTRODUCTION
3.1 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Audience and Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

12
12
12

4

Z-WAVE LONG RANGE PROTOCOL STACK OVERVIEW AND REFERENCE MODEL
4.1 Generic Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Basic Principles of Z-Wave Long Range Networking . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3 Z-Wave Long Range protocol stack overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.1 PHY Layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2 MAC Layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.3 Logical Link layer (LLC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4 Z-Wave Long Range TRX Reference models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4.1 Protocol reference model of a transceiver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4.2 Functional description of the interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4.3 Functional model of a transceiver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5 Operation modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.6 Concept of service primitives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

13
13
13
14
15
15
15
16
16
17
17
19
20

5

Z-WAVE LONG RANGE PHY SPECIFICATION
5.1 General . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.1 Features of the PHY layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.1.2 Data wrapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2 Transceiver front-end specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.1 LRF profiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.2 Data rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

21
21
21
21
22
22
22

5.2.3
5.2.4
5.2.5

5.3

5.4

Channel configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Modulation and encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Transmitter and receiver requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.1 Transmit frequency error . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.2 Transmit power adjustments (conducted) . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.3 Receiver sensitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.4 Clear channel assessment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.5 Receiver spurious requirement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.6 Receiver blocking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.7 Receiver saturation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.8 TX-to-RX turnaround time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.9 RX-to-TX turnaround time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.2.5.10 Side-lobe suppression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
PPDU format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.1 General PHY frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.2 Preamble field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.3 Start of frame field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.3.4 PSDU field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
PHY service specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1 PHY data service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.1 PD-DATA.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.1.1 Semantics of the PHY data request primitive . . . . . . . . . . . . . . . . . . .
5.4.1.1.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.1.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.2 PD-DATA.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.2.1 Semantics of the PHY data confirm primitive . . . . . . . . . . . . . . . . . . .
5.4.1.2.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.2.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.3 PD-DATA.indication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.3.1 Semantics of the PHY data indication primitive . . . . . . . . . . . . . . . . .
5.4.1.3.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.1.3.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2 PHY management service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.1 PLME-SOF.indication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.1.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.1.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.1.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.2 PLME-GET-CCA.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.2.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.2.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.2.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.3 PLME-GET-CCA.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.3.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.3.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.3.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.4 PLME-GET.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.4.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.4.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.4.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.5 PLME-GET.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.5.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.5.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.5.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.6 PLME-SET-TRX-MODE.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.6.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.6.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.6.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.7 PLME-SET-TRX-MODE.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.7.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.7.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.7.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

22
23
25
25
26
26
26
26
27
28
28
28
28
31
31
31
32
32
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
35
35
36
36
36
36
37
37
37
37
37
37
38
38
38
38
38
38
39
39
39
39
39
40
40
40
40
40
41
41
41
41

5.4.2.8

PLME-SET.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.8.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.8.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.8.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.9 PLME-SET.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.9.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.9.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.9.3 Effect on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.4.2.9.4 PHY enumerations description . . . . . . . . . . . . . . . . . . . . . . . . . . .
PHY constants and MIB attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.5.1 PHY constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5.5.2 PHY MIB attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

42
42
42
42
43
43
43
43
43
45
45
45

Z-WAVE LONG RANGE MAC LAYER SPECIFICATION
6.1 General . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.1 Features of the MAC layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.2 Bootstrapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3 Functional overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.1 MPDU formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.1.1 Singlecast MPDU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.1.2 Acknowledgment MPDU . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.2 Network Robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.2.1 Clear Channel Assessment . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.2.2 Acknowledgment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.2.3 Retransmissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.2.4 Data Validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.2.5 Channel selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.3 Power Consumption Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1.3.3.1 Communication with a Frequently Listening node . . . . . . . . . . . . . . . .
6.2 MAC Layer Service Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.1 MAC enumerations description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2 MAC Data Service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.1 MD-DATA.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.1.1 Semantics of the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.1.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.1.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.2 MD-DATA.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.2.1 Semantics of the PHY data confirm primitive . . . . . . . . . . . . . . . . . . .
6.2.2.2.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.2.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.3 MD-DATA.indication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.3.1 Semantics of the PHY data indication primitive . . . . . . . . . . . . . . . . .
6.2.2.3.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.3.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.2.4 Data service sequence chart . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3 MAC management service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.1 MLME_GET.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.1.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.1.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.1.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.2 MLME-GET.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.2.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.2.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.2.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.3 MLME-SET.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.3.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.3.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.3.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.4 MLME-SET.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.4.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.4.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

46
46
46
46
46
46
47
47
47
48
48
48
48
48
48
48
49
49
50
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
54
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
57
57
57
57
58
58
58

5.5

6

6.2.3.4.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
MLME-RESET.request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.5.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.5.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.5.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.6 MLME-RESET.confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.6.1 Semantics for the service primitive . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.6.2 When generated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.6.3 Effects on receipt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
MPDU Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1 General MPDU format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.1 HomeID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.2 Source NodeID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.3 Destination NodeID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.4 Length . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5 Frame Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5.1 Ack Req subfield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5.2 Extend subfield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5.3 Header Type subfield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.5.4 Reserved . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.6 Sequence Number . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.7 Noise Floor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.8 Tx Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.9 Data Payload . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.1.10 FCS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.2 Singlecast MPDU format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.2.1 Destination NodeID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.2.2 Frame Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.2.2.1 Header Type subfield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.2.3 Data Payload . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.3 Acknowledgement MPDU format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.3.1 Destination NodeID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.3.2 Frame Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.3.2.1 Ack Req subfield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.3.2.2 Header type subfield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.3.3 Sequence Number . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.3.4 Received RSSI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.3.5 Data Payload . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.4 Broadcast MPDU format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.4.1 Destination NodeID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.4.2 Frame Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.4.2.1 Ack Req subfield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.4.2.2 Header type subfield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.4.3 Data Payload . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.5 MPDU header extension format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.5.1 Frame Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.5.1.1 Extension type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.5.1.2 Discard unknown . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.5.1.3 Extension length . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.6 Beam Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.6.1 Beam Tag . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.6.2 Tx Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.6.3 Destination nodeID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.6.4 HomeID hash . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.7 Fragmented beam format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.3.7.1 Broadcast beaming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
MAC constants and MIB attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.1 MAC constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.4.2 MIB attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
MAC Functional description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1 Transmission, Reception and Acknowledgement . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.2.3.5

6.3

6.4
6.5

58
59
59
59
59
59
59
60
60
61
61
61
62
62
63
63
63
63
63
64
64
64
65
65
65
66
66
66
66
66
66
67
67
67
67
67
67
68
68
68
68
68
68
68
68
69
69
69
69
69
70
70
71
71
71
72
73
73
74
75
75

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

Specifications

6.5.1.1
6.5.1.2

6.5.2

August 20, 2025

Clear Channel Assessment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Transmission . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1.2.1 Dynamic Tx Power . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1.3 Reception and Rejection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1.3.1 RX Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1.4 Backup channel handling (Channel configuration 3) . . . . . . . . . . . . . . . . . . . .
6.5.1.5 Use of Acknowledgement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1.5.1 No Acknowledgement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1.5.2 Acknowledgement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1.5.3 Retransmissions (Channel configuration 1 and 2) . . . . . . . . . . . . . . . . .
6.5.1.5.4 Retransmissions (Channel configuration 3) . . . . . . . . . . . . . . . . . . . .
6.5.1.5.5 Random backoff . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.5.1.6 Idle mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Transmission Scenarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

References

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

75
75
75
75
76
76
76
76
77
77
77
78
78
78
80

This document may only be copied and distributed internally. Page 5

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

1 Preamble
1.1 Description
Z-Wave Long Range PHY and MAC layer specification
Reviewed by the Z-Wave Alliance Core Stack Working Group (CSWG) and approved by the Z-Wave Alliance
Technical Committee.

1.2 Disclaimer
THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER, AND IN
PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE
OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND
NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS OR SUBMITTERS, SHALL HAVE ANY LIABILITY
WHATSOEVER TO ANY IMPLEMENTER OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE
WHATSOEVER, DIRECTLY OR INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 6

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

1.3 Revision Record
Table 1.1: Revision History
Doc.
Rev

Date

By

Pages
Affected

Brief Description of Changes

0.3
0.5
0.7
0.7.1

2020.09.01
2020.09.23
2020.09.28
2020.12.14

CSWG
CSWG
CSWG
CSWG

ALL
ALL
ALL
6.5.1.5.5
Table 6.15
6.5.1.2
5.3.3
6.5.1.5.4
5.3 & 6.3
6.5.1.2.1

0.7.2

2021.02.26

CSWG

6.3.6.3

0.8
0.8.1

2021.03.01
2021.03.16

CSWG
CSWG

None
5.2.2
5.2.4

0.9
1.0

2021.03.29
2021.08.27

Frontpage

1.5
1.8
2.0

2023.06.20
2023.07.03
2023.08.17

2.5.0
2.5.1
2.5.2
2.7.0
2.9.0
3.0.0

2024.10.21
2024.10.22
2024.10.22
2025/03/21
2025/05/30
tbd

3.1.0

2025/07/22

CSWG
ZWA
Board
CSWG
CSWG
ZWA
Board
CSWG
CSWG
CSWG
CSWG
TC
ZWA
Board
WePower

PHY section completed and some MAC sections started
PHY and MAC sections ready for 0.5 review
Review of 0.5 completed and document moved to 0.7
Changed retransmit wording to allow reception of ack during
random backoff
Added NodeID 4001-4004 as valid ID’s for virtual nodes
Allow acknowledge to be send without CCA
Fixed bit order of SOF
Added description of retransmission on secondary channel
Fixed PHY bit order description
Added shall about Tx power Control
Fixed wrong bit size of destination Node ID in wakeup beam
description
Updated to revision 0.8 after initial TC review
Updated with comments from TC review
Removed references to US region
Changed EVM to Offset EVM
Cleanup for IPR review
Approved for Publication

3.7.0
3.9.0

2025/07/28
2025/08/20

CSWG
TC

n/a
n/a

Table 5.5
Frontpage

Corrected symbol mapping.
Approved by CSWG and TC, updated for members review.
Approved for Publica�on

All
5.2.5.10
5.2.5.6
n/a
n/a
n/a

Migration from Word to GitHub
Add specification for Side-Lobe suppression in Long Range
Fix incorrect receiver blocking test description
Ready for the TC review.
Approved for IPR review.
Approved for publication.

6.3.1.7
6.5.1.2.1

Added description for noise level value for WOEEN
Added description for Dynamic TX Power Algorithm for
WOEEN
Ready for the TC review.
Approved by TC

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 7

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

1.4 Abbreviations
Table 1.2: Abbreviations
Abbreviation

Explanation

ACK
ADP
AE
AIS
AL
CC
CCA
CP
CRC
DSSS
Dst
EOF
EIRP
EMC
ERP
FCS
FER
FL
FLN
FSK
GFSK
HAN
EHR
EVM
ID
IDB
ISI
ISM
Kcps
Ksps
LBT
LLC
LR1
LR2
LR3
LFR
LSB
MAC
MD
MD-SAP
MDI
MFR
MHR
MIB
MLME
MLME-SAP
MPDU
MSB
MSDU
MSK
NPDU
NRZ
OQPSK
OSI

Acknowledgement
Application Data Primitives
Application Entity
Application Interface Sublayer
Always Listening
Channel Configuration
Clear Channel Assessment
Consumer Premises
Cyclic Redundancy Check
Direct Sequence Spread Spectrum
Destination
End of Frame delimiter
Effective Isotropic Radiated Power
Electromagnetic Compatibility
Effective Radiated Power
Frame Check Sequence
Frame Error Rate
Frequently Listening
Frequently Listening Node
Frequency Shift Keying
Gaussian Frequency Shift Keying
Home Area Network
End Header
Error Vector Magnitude
Identification
Inter-Domain Bridge
Inter-Symbol Interference
Industrial, Scientific and Medical
(Kilo Chips Per Second)
Kilo Symbols Per Second
Listen Before Talk
Logical Link Control
Long range Rate type 1 (100 kbit/s, 800 kcps)
Long range Rate type 2 (XX kbit/s, YY kcps)
Long range Rate type 3 (UU kbit/s, ZZ kcps)
Long range Radio Frequencies
Least Significant Bit
Medium Access Control
MAC Data
MAC Data – Service Access Point
Medium-Dependent Interface
MAC Footer
MAC Header
Management Information Base
MAC Layer Management Entity
MAC Layer Management Entity – Service Access Point
MAC Protocol Data Unit
Most Significant Bit
MAC Service Data Unit
Minimum Shift Keying
Network layer Protocol Data Unit
Non Return to Zero
Offset Quadrature Phase Shift Key
Open System Interconnect
continues on next page

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 8

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

Table 1.2 – continued from previous page
Abbreviation

Explanation

PD
PD-SAP
PDU
PHR
PHY
PLME
PLME-SAP
PMI
PPDU
PPM
PSDU
R1
R2
R3
RF
RSSI
RX
SAP
Src
SDU
SOF
SHR
SNR
TRX
TX
WOEEN

PHY Data
PHY Data – Service Access Point
Protocol Data Unit
PHY Header
Physical layer
Physical Layer Management Entity
Physical Layer Management Entity – Service Access Point
Physical Medium-Independent interface
PHY Protocol Data Unit
Parts Per Million
PHY Service Data Unit
Data Rate type 1 (9.6 kbit/s)
Data Rate type 2 (40 kbit/s)
Data Rate type 3 (100 kbit/s)
Radio Frequency
Receive Signal Strength Indication
Receive/Receiver
Service Access Point
Source
Service Data Unit
Start of Frame delimiter
Start Header
Signal to Noise Ratio
Transceiver
Transmit/Transmitter
Wake On Event End Node

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 9

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

2 DEFINITIONS
This specification defines the following terms:
Alien domain: Any group of nodes that is not compliant with this recommendation or G.9959 [G9959] connected to
the same or a different medium (wired or wireless). These domains can be used as backbones to this network domain
or as separate networks. The bridging function to an alien domain, as well as coordination with an alien domain to
avoid mutual interference is beyond the scope of this Recommendation.
Broadcast: A type of communication where a node sends a MAC frame which is simultaneously received by all other
nodes within a direct range. In a multi-hop domain, some nodes of the domain may not receive the broadcast frame.
Channel: A transmission path between nodes. Logically a channel is an instance of a communication medium being
used for the purpose of passing data between two or more nodes.
Clear channel assessment (CCA): Provided by the receiver, a CCA indicates if the medium is busy, e.g. if a PHY
frame is currently transmitted on the medium by another node.
Data: Bits or bytes transported over the medium or via a reference point that individually convey information. Data
includes user (application) data and any other auxiliary information (overhead, control, management, etc.). Data
does not include bits or bytes that, by themselves, do not convey any information, such as the preamble.
Data rate: The rate, in bits per second, at which data is transmitted by a node onto the medium. Data rate is
calculated only for time periods of continuous transmission.
Domain: A collection of nodes compliant with this recommendation comprising the domain master and all those
nodes that are registered with the same domain master. In the context of this Recommendation,
Domain ID: A unique identifier of a domain. Refer to HomeID.
Domain master: A node with extended management capabilities which allows it to handle registration and
maintenance of the nodes in its domain.
Home area network (HAN): A network capable of connecting devices in home premises.
HomeID: Information unit used as a domain ID in G.9959 [G9959].
Inclusion: The process adding a new node to a domain in a way so that the node can communicate with other nodes
in the domain and filter out traffic from other domains.
Inter-domain bridge (IDB): A bridging function to interconnect nodes of two different domains.
ISM band: Frequency bands for industrial, scientific and medical use, allocated by the Z-Wave alliance.
Latency: A measure of the delay from the instant that a frame has been transmitted through a reference point of
the transmitter protocol stack to the instant when a frame reaches the corresponding reference point of the receiver
protocol stack.
Logical (functional) interface: An interface in which the semantic, syntactic, and symbolic attributes of information
flows are defined. Logical interfaces do not define the physical properties of signals used to represent the information.
It is defined by a set of primitives.
Medium: The radio waves carrying the signals. Walls and other building components may affect the quality of the
medium. Nodes communicating via the same medium may interfere with each other.
Multicast: A type of communication where a node sends a MAC frame which is simultaneously received by one or
more other nodes in the domain.
Network: One or more, potentially overlapping, domains.
Node: Any device that contains an transceiver in compliance with this recomandation. . The term ‘alien node’ means
a a device with a transiever not compliant with this recomendation.
Node ID: A unique identifier allocated to a node during its registration in a domain.
Physical interface: An interface defined in terms of the physical properties of the signals used to represent the
information transfer. A physical interface is defined by signal parameters like power (power spectrum density) and
timing.
Primitives: Variables and functions used to define logical interfaces and reference points.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 10

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

Reference point: A location in a signal flow, either logical or physical, that provides a common point for observation
and or measurement of the signal flow.
Symbol frame: A frame composed of bits of a single modulation symbol period.
Symbol rate: The rate, in symbols per second, at which modulation symbols are transmitted by a node onto a
medium. Symbol rate is calculated only for time periods of continuous transmission.
Transmission overhead: A part of the available data rate used to support transmission over the media (e.g.,
preamble, inter-frame gaps, and silent periods).
Unicast: A type of communication when a node sends the frame to another single node.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 11

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

3 INTRODUCTION
3.1 Purpose
The purpose of this document is to describe the PHY and MAC layer of the Z-Wave long range protocol

3.2 Audience and Prerequisites
The audience for this document is Z-Wave alliance members

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 12

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

4 Z-WAVE LONG RANGE PROTOCOL STACK OVERVIEW AND
REFERENCE MODEL
4.1 Generic Description
Z-Wave Long Range provides an extended range version of the Z-Wave technology, targeting deployments over a
kilometer radius, suitable in both indoors and outdoors areas.

4.2 Basic Principles of Z-Wave Long Range Networking
The following are the basic principles of the Z-Wave Long Range network architecture:
1. The network is divided into domains:
• The division of physical nodes into domains is logical.
• Domains may fully or partially overlap as there is no physical separation.
• The number of domains is limited by the 32-bit HomeID identifier.
• Each domain is identified by a unique HomeID.
• Nodes of different domains may communicate with each other via inter-domain bridges (IDB).
• Operation of different domains is handled by individual domain masters.
2. The domain is a set of nodes connected to the same medium:
• One node in the domain operates as a domain master.
• Each domain may contain up to 4000 nodes (including the domain master).
• Each node in the domain is identified by a NodeID that is unique inside the domain. A NodeID is a
12-bit short address. The first node in a Z-wave Long Range network hands out the HomeID and unique
NodeIDs to all other nodes added to the domain.
• All nodes that belong to the same domain are identified by the same HomeID. A node can belong to only
one domain.
• Nodes of the same domain can only communicate with the domain master.
3. Nodes of different Z-Wave Long Range domains:
• Nodes in different domains can communicate via inter-domain bridges (IDB). The IDB function is a
bridging function associated with the domain master in each network domain.
The details of domain operation rules and the functionalities of domain master and endpoint nodes are beyond
the scope of this specification. In addition, inter-domain bridges communications are also beyond the scope of this
specification.
The main scope of this specification is limited to the PHY and MAC of Z-Wave Long Range radio communication
transceivers.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 13

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

4.3 Z-Wave Long Range protocol stack overview
Similar to Z-Wave protocol, the Z-Wave Long Range protocol stack is defined in terms of layers. Each layer is
responsible for one part of the operation and offers services to the higher layers through two service access points
(SAP), knows as a data service entity and a management service entity. The data entity provides a data transmission
service; and a management entity provides other services related to the actual layer. The data and management
entities define the logical links between the layers.
A Z-Wave Long Range node implements the PHY layer, which contains the RF TRX along with its low-level control
mechanism, a data link layer that provides access to the physical channel for all types of transfers, a network layer
that controls a network formation and maintenance , and a combined application layer that collapses the OSI stack
layers transport, session, and presentation.
Figure 4.1 shows the Z-Wave Long Range protocol stack overview

Application Layer
Application Layer interface sublayer
Management

Data
SAP

SAP

Network (NWK) Layer
Data
SAP

Management

SAP

Logical Link Control (LLC)
Data Link Layer

Medium Access Control (MAC)
Data
SAP

Management

SAP

Physical (PHY) Layer

Z-Wave Long Range
Physical Medium
Figure 4.1: Z-Wave Long Range protocol stack layers
This specification document defines only the PHY and Data Link layers. Upper layers are outside the scope of this
specification.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 14

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

4.3.1 PHY Layer
The features of the PHY are activation and deactivation of the RF TRX, frequency selection, and transmitting as
well as receiving frames. The RF receiver can perform a clear channel assessment. The RF TRX operates in a one,
two, or three-channel configuration located in the license-free ISM frequency bands.
The PHY provides two services:
• the physical layer data service accessed through the PD-SAP; and
• the PHY management service interfacing with the physical layer management entity service access point
(PLME-SAP).
The PD service enables the transmission and reception of PPDUs across the physical radio channel.
Section 5 contains the full specification of the Z-Wave Long Range PHY layer.
4.3.2 MAC Layer
The features of the MAC layer are channel access, frame validation, acknowledged frame delivery, and
retransmissions.
The MAC layer provides two services:
• the MAC data service, accessed through the MD-SAP, and
• the MAC management service interfacing with the MAC layer management entity service access point
(MLME-SAP).
The MAC data service enables the transmission and reception of MPDUs across the PD service.
Section 6 contains the full specification of the Z-Wave Long Range MAC layer.
4.3.3 Logical Link layer (LLC)
The logical link control (LLC) layer is the upper part of the data link layer that enables access of different instances
of network protocol stacks to the MAC layer. The purpose of the LLC layer is to enable de-multiplexing of incoming
MPDUs. The LLC layer shall not change the contents of the data link PDU (DLPDU) payload.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 15

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

4.4 Z-Wave Long Range TRX Reference models
4.4.1 Protocol reference model of a transceiver
The protocol reference model of a transceiver is presented in Figure 4.2. It includes four reference points: the data
link layer interface (DLI), the MAC layer interface (MLI), the physical medium-independent interface (PMI), and the
medium-dependent interface (MDI)
The MDI is a physical interface defined in terms of the physical signals transmitted over a medium (Section 4.4.3).
The PMI is both medium independent and application independent. The PMI, MLI and DLI interfaces are defined as
functional interfaces, in terms of sets of primitives exchanged across the interface.

Data link layer interface (DLI)
LLC
MAC layer interface (MLI)
MAC
Physical medium-dependent interface (PMI)
PHY
Medium-dependent interface (MDI)
Z-Wave Long Range transmission medium
Figure 4.2: Protocol reference model of Z-Wave Long Range TRX
The logical link control (LLC) layer is a logical link that enables access of different instances of network protocol
stacks to the MAC layer.
The medium access control layer (MAC) controls access of the node to the medium using the medium access
protocols defined. The MAC layer also provides checksum protection to the MAC information.
The physical layer (PHY) provides bit rate adaptation (data flow control) between the MAC and PHY and adds
PHY-related control and management overhead. The PHY layer provides encoding of the PHY frame content (header
and payload) and modulates the encoded PHY frames for transmission over the medium.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 16

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

4.4.2 Functional description of the interface
This section contains the functional description of the TRX interfaces (reference points) based on the protocol
reference model presented in Figure 4.2. The interfaces shown in Figure 4.3 are defined in this specification.

LLC
MAC_MGMT

MLI_DATA
MAC

PMI_MGMT

PMI_DATA
PHY
MDI
Z-Wave Long Range transmission medium

Figure 4.3: Z-Wave Long Range TRX reference points related to PHY/MAC
The reference model in Figure 4.3 shows interfaces related to the application data path (MLI_DATA, PMI_DATA,
and MDI) and the management interfaces between data and management planes of the PHY (PHY_MGMT). All
interfaces are specified as reference points in terms of primitive flows exchanged between the corresponding entities.
The description does not imply any specific implementation of the interfaces.
4.4.3 Functional model of a transceiver
The functional model of a Z-Wave Long Range TRX is presented in Figure 4.4.

DLI

DLPDU
LLC

MLI

MPDU

MAC_MGMT

Physical frames

PMI_MGMT

MPDU
MAC

PMI
PHY
MDI

Z-Wave Long Range transmission medium
Figure 4.4: Functional model of a Z-Wave Long Range TRX

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 17

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

The detail description of the PHY later is presented in Section 5. The detail description of the MAC layer is
presented in Section 6. The MAC layer interface (MLI) may deviate from the open system interconnection (OSI)
reference stack in that it exchanges MAC PDUs (MPDU) with the MAC layer rather than MAC service data units
(MSDUs). This allows the upper layers to perform security encapsulation, segmentation or IP header compression
operation, based on the information carried out in MPDU header. The detail of the LLC layer is out of scope for this
recomnendation.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 18

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

4.5 Operation modes
Similar to the Z-Wave nodes, the Z-Wave Long Range nodes may operate in two different receiving modes: always
listening (AL) and frequently listening (FL). The long-range node may operate in either of the two modes and
dynamically alternate between the two modes.
In AL mode, the receiver stays on at all time.
In FL mode, the receiver is turned off most of the time. At a regular interval, the receiver is turned on for a short
duration. This mode saves energy while still allowing for frame reception. The drawback of FL mode is an increased
transmission latency due to the low receiver duty cycle.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 19

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

4.6 Concept of service primitives
This clause provides a brief overview of the concept of service primitives (operations) that is applied to describe the
Z-Wave Long Range protocol stack layers interaction. Refer to [b ITU T X.210] for more detailed information about
the concept of service primitive. The services of a layer are the capabilities it offers to the user in the next higher
layer or sublayer by building its functions on the services of the next lower layer. This concept is illustrated in Figure
4.5, showing the service hierarchy and the relationship of the two correspondent N-users and their associated N-layer
(or sublayer) peer protocol entities.

Service User
(N-User)

Service Provider
(N-Layer)

Service User
(N-User)

Request
Indication
Response
Confirm
Time
Figure 4.5: Service primitives
The services are specified by describing the information flow between the N-user and the N-layer. This information
flow is modelled by discrete, instantaneous events, which characterize the provision of a service. Each event consists
of passing a service primitive from one layer to the other through a service access point (SAP) associated with an
N-user. Service primitives convey the required information by providing a particular service. These service primitives
are an abstraction because they specify only the provided service rather than the means by which it is provided. This
definition is independent of any other interface implementation.
Services are specified by describing the service primitives and parameters that characterize it. A service may have
one or more related primitives that constitute the activity that is related to that particular service. Each service
primitive may have zero or more parameters that convey the information required to provide the service.
A primitive can be one of four generic types:
• Request: the request primitive is passed from the N-user to the N-layer to request that a service is initiated.
• Indication: the indication primitive is passed from the N-layer to the N-user to indicate an internal N-layer
event that is significant to the N-user. This event may be logically related to a remote service request, or it may
be caused by an N-layer internal event.
• Response: the response primitive is passed from the N-user to the N-layer to complete a procedure previously
invoked by an indication primitive.
• Confirm: the confirm primitive is passed from the N-layer to the N-user to convey the results of one or more
associated previous service requests.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 20

Specifications

Z-Wave Long Range PHY and MAC Layer Specification, Release 3.9.0

August 20, 2025

5 Z-WAVE LONG RANGE PHY SPECIFICATION
5.1 General
The PHY layer defines modulation schemes, data rates, synchronization methods and a frame format for use in
high-power, wide-bandwidth control networks. If a device claims to adhere to the following PHY specification, it
must also support all the requirements stated in Section 7 of [G9959].
5.1.1 Features of the PHY layer
The PHY layer is responsible for the following tasks:
• assignment of RF profiles to physical channels,
• activation and deactivation of the radio transceiver,
• transmission and reception,
• clear channel assessment,
• frequency selection, and
• link quality assessment for received frames
The RF transceiver shall be able to operate in a one, two, three, four or five channel configuration in license-free RF
bands (the RF channels as defined in Section 7 of [G9959] and what is defined in Section 5.2).
The PHY shall provide two services: (1) the PHY data service accessed via the PHY data (PD) service access point
(PD-SAP) and (2) the PHY management service accessed via the physical layer management entity (PLME) service
access point (PLME-SAP). The PHY data service enables the transmission and reception of PHY protocol data units
(PPDUs) over the physical radio channel. See Section 5.4 for a detailed description.
Constants and attributes that are specified and maintained by the PHY are written in italics. Constants have a
gen

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

**Last Updated**: 2026-03-07T20:11:55.815147
