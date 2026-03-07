# Host API Specification

**Source**: Z-Wave Alliance 2025-B Specification Package
**Date**: 2026-03-07
**Version**: 2025-B

## Overview

Serial API and host communication protocol

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
Z-Wave API Specification
Release 2.9.0

Z-Wave Alliance
Aug 20, 2025

Table of Contents
1

Introduction
1.1 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Audience and Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.5 Terminology And Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

9
9
9
9
9
9

2

Overview

10

3

Interface communication
3.1 Table Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2 Frame types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.1 Data Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.2 ACK Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.3 NAK Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.2.4 CAN Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3 Command frame flows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.1 Unacknowledged frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.2 Acknowledged frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.3 Acknowledged frame with response . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.4 Acknowledged frame with callback . . . . . . . . . . . . . . . . . . . . . . . . .
3.3.5 Acknowledged frame with response and callback . . . . . . . . . . . . . . . . .
3.3.6 Unsolicited frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4 Error handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.1 Retransmission timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.2 Missing Acknowledgment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.3 Collision . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.4 Frame reception timeout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3.4.5 Invalid frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

11
11
11
11
12
13
13
13
14
14
15
15
16
16
17
17
17
18
19
19

4

Z-Wave API Commands
4.1 Command format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2 Generic command elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

20
21
21

4.3

4.2.1 Session identifier (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.2 Rx Status (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.3 Tx Status (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.4 RSSI Measurements (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.5 Response status (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.6 Command Status (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.7 Basic Device Class (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.8 Tx Options (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.9 RF Region (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.10 Tx Status Report (N bytes) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.11 Route Speed (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.2.12 Repeater (4 bytes) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Z-Wave Capability API commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.1 Get Init Data Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.1.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.1.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.1.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.2 Set Application Node Information Command . . . . . . . . . . . . . . . . . . .
4.3.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.2.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.2.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.2.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.3 Set Application Node Information Command Classes Command . . . . . . . .
4.3.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.3.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.3.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.3.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.4 Get Controller Capabilities Command . . . . . . . . . . . . . . . . . . . . . . .
4.3.4.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.4.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.4.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.4.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.5 Get Capabilities Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.5.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.5.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.5.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.5.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.6 Get Long Range Nodes Command . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.6.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.6.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.6.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.6.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.7 Get Z-Wave Long Range Channel Command . . . . . . . . . . . . . . . . . . .
4.3.7.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.7.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.7.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.7.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.8 Set Z-Wave Long Range Channel Command . . . . . . . . . . . . . . . . . . . .
4.3.8.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.8.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.8.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.8.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.9 Get NLS Nodes Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.9.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.3.9.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.3.9.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.9.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.3.10 Get Protocol Version Command . . . . . . . . . . . . . . . . . . . . . . . . . .

21
21
23
23
24
24
24
24
25
26
29
30
31
32
32
32
32
34
35
35
35
36
36
37
37
37
38
38
39
39
39
39
40
41
41
41
41
42
43
43
44
44
45
46
46
46
46
47
48
48
48
48
49
50
50
50
51
52
53

4.4

4.3.10.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3.10.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . 53
4.3.10.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . . 53
4.3.10.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . . 54
4.3.11 Get Library Version Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.3.11.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.3.11.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . 55
4.3.11.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . . 55
4.3.11.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . . 56
4.3.12 Get Library Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.3.12.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.3.12.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . 57
4.3.12.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . . 57
4.3.12.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . . 57
4.3.13 Soft Reset Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.3.13.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.3.13.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . 58
4.3.13.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . . 58
4.3.13.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . . 58
4.3.14 Set Default Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.3.14.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.3.14.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . 59
4.3.14.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . . 59
4.3.14.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . . 59
4.3.15 Setup Z-Wave API Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.3.15.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.3.15.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . 60
4.3.15.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . . 60
4.3.15.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . . 61
4.3.16 Z-Wave API Setup sub-commands . . . . . . . . . . . . . . . . . . . . . . . . . 62
4.3.16.1 Z-Wave API Setup Get Supported Commands Sub Command . . . . 63
4.3.16.2 Z-Wave API Setup Set Tx Status Report Sub Command . . . . . . . 65
4.3.16.3 Z-Wave API Setup Set Max Long Range TX Powerlevel Sub Command 67
4.3.16.4 Z-Wave API Setup Set Powerlevel Sub Command . . . . . . . . . . . 69
4.3.16.5 Z-Wave API Setup Get Max Long Range Powerlevel Sub Command . 72
4.3.16.6 Z-Wave API Setup Set Long Range Max Node ID Sub Command . . 74
4.3.16.7 Z-Wave API Setup Get Long Range Max Node ID Sub Command . . 76
4.3.16.8 Z-Wave API Setup Get Powerlevel Sub Command . . . . . . . . . . . 78
4.3.16.9 Z-Wave API Setup Get Maximum Payload Size Sub Command . . . . 80
4.3.16.10 Z-Wave API Setup Get Z-Wave Long Range Maximum Payload Size
Sub Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.3.16.11 Z-Wave API Setup Set 16-bit Powerlevel Sub Command . . . . . . . . 84
4.3.16.12 Z-Wave API Setup Get 16-bit Powerlevel Sub Command . . . . . . . 86
4.3.16.13 Z-Wave API Setup Get Supported Regions Sub Command . . . . . . 88
4.3.16.14 Z-Wave API Setup Get Region Info Sub Command . . . . . . . . . . 90
4.3.16.15 Z-Wave API Setup Get RF Region Sub Command . . . . . . . . . . . 92
4.3.16.16 Z-Wave API Setup Set RF Region Sub Command . . . . . . . . . . . 94
4.3.16.17 Z-Wave API Setup Set NodeID Base Type Sub Command . . . . . . 96
4.3.17 Get Manufacturer Info Command . . . . . . . . . . . . . . . . . . . . . . . . . . 98
4.3.17.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
4.3.17.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . 98
4.3.17.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . . 98
4.3.17.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . . 99
Z-Wave API Network Management Commands . . . . . . . . . . . . . . . . . . . . . . 100
4.4.1 Common Network Management Commands . . . . . . . . . . . . . . . . . . . . 101
4.4.1.1 Send NOP Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
4.4.1.2 Get Node Information Protocol Data Command . . . . . . . . . . . . 104
4.4.1.3 Send Node Information Command . . . . . . . . . . . . . . . . . . . . 106
4.4.1.4 Request Node Information Command . . . . . . . . . . . . . . . . . . 108

4.5

4.6

4.4.1.5 Set Learn Mode Command . . . . . . . . . . . . . . . . . . . . . . . .
4.4.1.6 Get SUC NodeID Command . . . . . . . . . . . . . . . . . . . . . . .
4.4.1.7 Set SmartStart Inclusion Request Maximum Interval Command . . .
4.4.1.8 Explore Request Inclusion Command . . . . . . . . . . . . . . . . . .
4.4.1.9 Explore Request Exclusion Command . . . . . . . . . . . . . . . . . .
4.4.2 End Nodes Network Management . . . . . . . . . . . . . . . . . . . . . . . . . .
4.4.2.1 Request New Route Destinations Command . . . . . . . . . . . . . .
4.4.2.2 Is Node Within Direct Range Command . . . . . . . . . . . . . . . .
4.4.2.3 Get Network Statistics Command . . . . . . . . . . . . . . . . . . . .
4.4.2.4 Clear Network Statistics Command . . . . . . . . . . . . . . . . . . .
4.4.3 Controller Nodes Network Management . . . . . . . . . . . . . . . . . . . . . .
4.4.3.1 Add Node To Network Command . . . . . . . . . . . . . . . . . . . .
4.4.3.2 Add Controller And Assign Primary Controller Role Command . . .
4.4.3.3 Add Primary Controller Command . . . . . . . . . . . . . . . . . . .
4.4.3.4 Remove Node From Network Command . . . . . . . . . . . . . . . . .
4.4.3.5 Remove Specific Node From Network Command . . . . . . . . . . . .
4.4.3.6 Is Node Failed Command . . . . . . . . . . . . . . . . . . . . . . . . .
4.4.3.7 Remove Failed Node Command . . . . . . . . . . . . . . . . . . . . .
4.4.3.8 Replace Failed Node Command . . . . . . . . . . . . . . . . . . . . .
4.4.3.9 Delete Return Route Command . . . . . . . . . . . . . . . . . . . . .
4.4.3.10 Assign Return Route Command . . . . . . . . . . . . . . . . . . . . .
4.4.3.11 Assign SUC Return Route Command . . . . . . . . . . . . . . . . . .
4.4.3.12 Assign Priority Return Route Command . . . . . . . . . . . . . . . .
4.4.3.13 Assign Priority SUC Return Route Command . . . . . . . . . . . . .
4.4.3.14 Set Priority Route Command . . . . . . . . . . . . . . . . . . . . . . .
4.4.3.15 Get Priority Route Command . . . . . . . . . . . . . . . . . . . . . .
4.4.3.16 Get Neighbor Table Line Command . . . . . . . . . . . . . . . . . . .
4.4.3.17 Lock Unlock Last Route Command . . . . . . . . . . . . . . . . . . .
4.4.3.18 Get Routing Table Entries Command . . . . . . . . . . . . . . . . . .
4.4.3.19 Set SUC NodeID Command . . . . . . . . . . . . . . . . . . . . . . .
4.4.3.20 Delete SUC Return Route Command . . . . . . . . . . . . . . . . . .
4.4.3.21 Send SUC NodeID Command . . . . . . . . . . . . . . . . . . . . . .
4.4.3.22 Enable Node NLS command . . . . . . . . . . . . . . . . . . . . . . .
4.4.3.23 Get Node NLS State command . . . . . . . . . . . . . . . . . . . . . .
4.4.3.24 Request Node Neighbor Discovery Command . . . . . . . . . . . . . .
4.4.3.25 Request Node Type Neighbor Update Command . . . . . . . . . . . .
4.4.3.26 Request Network Update Command . . . . . . . . . . . . . . . . . . .
4.4.3.27 Set Virtual Node To Learn Mode Command . . . . . . . . . . . . . .
4.4.3.28 Virtual Node Send Node Information Command . . . . . . . . . . . .
4.4.3.29 Set Virtual Nodes Application Node Information Command . . . . . .
4.4.3.30 Set Z-Wave Long Range Shadow NodeIDs Commmand . . . . . . . .
4.4.3.31 Transfer Protocol Command Class command . . . . . . . . . . . . . .
Z-Wave API Memory Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1 Get Network IDs from Memory Command . . . . . . . . . . . . . . . . . . . . .
4.5.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.5.1.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.5.1.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.5.1.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
Z-Wave API Firmware Update Commands . . . . . . . . . . . . . . . . . . . . . . . . .
4.6.1 Firmware Update Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.6.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.6.1.2 Sub Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.6.1.3 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.6.1.4 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.6.1.5 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.6.1.6 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.6.1.7 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.6.1.8 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.6.1.9 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .

111
115
116
117
120
123
124
127
129
131
132
133
146
148
150
155
157
159
161
165
167
169
171
173
175
177
179
181
182
184
186
188
190
191
193
196
199
202
205
207
209
210
213
214
214
214
214
214
215
216
216
217
217
217
218
219
220
220
220

4.7

4.8

4.6.1.10 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
Z-Wave API Backup and Restore Commands . . . . . . . . . . . . . . . . . . . . . . .
4.7.1 Network Restore Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7.1.2 Sub Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7.1.3 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.7.1.4 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.5 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.6 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.7.1.7 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.8 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.9 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.7.1.10 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.11 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.12 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.7.1.13 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.14 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.15 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.7.1.16 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.17 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.18 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.7.1.19 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.1.20 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.2 NVM Operations Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7.2.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.7.2.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.7.2.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.7.3 Extended NVM Operations Command . . . . . . . . . . . . . . . . . . . . . . .
4.7.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.7.3.2 Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . . .
4.7.3.3 Response data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.7.3.4 Callback data frame (Z-Wave Module → host) . . . . . . . . . . . . .
Unsolicited Z-Wave API commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.1 Application Command Handler Command . . . . . . . . . . . . . . . . . . . . .
4.8.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.1.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.8.1.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.1.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.1.5 4. Unsolicited frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.8.2 Z-Wave API Started Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.2.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.8.2.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.2.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.2.5 4. Unsolicited frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.8.3 Application Update Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.3.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.8.3.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.3.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.3.5 4. Unsolicited frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.8.4 Promiscuous Application Command Handler Command . . . . . . . . . . . . .
4.8.5 Bridge Application Command Handler Command . . . . . . . . . . . . . . . . .
4.8.5.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.5.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.8.5.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.5.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.5.5 4. Unsolicited frame (Z-Wave Module → host) . . . . . . . . . . . . .

221
221
222
222
224
224
224
225
225
226
226
226
227
227
227
228
228
228
229
229
229
230
230
231
231
234
235
236
237
237
239
240
241
242
243
243
243
243
243
243
245
245
245
245
245
245
248
248
248
248
248
248
253
254
254
254
254
254
254

4.8.6

4.9

Nonce Update Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.6.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.8.6.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.8.6.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.6.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.8.6.5 4. Unsolicited frame (Z-Wave Module → host) . . . . . . . . . . . . .
Z-Wave API Miscellaneous Commands . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.1 Clear Tx Timers Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.1.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.1.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.1.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.2 Get Background RSSI Command . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.2.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.2.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.2.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.3 Get Tx Timer Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.3.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.3.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.3.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.4 Get Virtual Nodes Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.4.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.4.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.4.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.4.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.5 Get Z-Wave Module Protocol Status Command . . . . . . . . . . . . . . . . . .
4.9.5.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.5.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.5.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.5.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.6 Is Virtual Node Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.6.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.6.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.6.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.6.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.7 Set Listen Before Talk Threshold Command . . . . . . . . . . . . . . . . . . . .
4.9.7.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.7.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.7.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.7.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.8 Set RF Receive Mode Command . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.8.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.8.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.8.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.8.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.9 Set RF Power Level Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.9.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.9.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.9.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.9.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.10 Set Maximum Routing Attempts Command . . . . . . . . . . . . . . . . . . . .
4.9.10.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.10.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.10.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.10.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.11 Set RF Power Level Rediscovery Command . . . . . . . . . . . . . . . . . . . .
4.9.11.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

256
256
256
256
256
256
258
259
259
259
259
259
260
260
260
260
260
261
261
261
261
262
263
263
263
263
263
264
264
264
264
265
266
266
266
266
266
267
267
267
267
268
269
269
269
269
270
271
271
271
271
272
273
273
273
273
273
274
274

4.9.11.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.11.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.11.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.12 Start Watchdog Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.12.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.12.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.12.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.12.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.13 Stop Watchdog Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.13.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.13.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.13.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.13.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.14 Set Timeouts Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.14.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.14.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.14.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.14.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.15 Power Management Stay Awake Command . . . . . . . . . . . . . . . . . . . .
4.9.15.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.15.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.16 Power Management Cancel Command . . . . . . . . . . . . . . . . . . . . . . .
4.9.16.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.16.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.17 Initiate Shutdown Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.17.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.17.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.17.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.17.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.18 Radio Debug Get Protocol List Command . . . . . . . . . . . . . . . . . . . . .
4.9.18.1 Radio Debug Version Identification . . . . . . . . . . . . . . . . . . .
4.9.18.2 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.18.3 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.18.4 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.18.5 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.19 Radio Debug Enable Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.19.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.19.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.19.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.19.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.20 Radio Debug Status Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.20.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.20.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.20.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.20.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.21 Nonce Generation on Z-Wave Module Set Mode Command . . . . . . . . . . .
4.9.21.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.9.21.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.9.21.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.9.21.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10 Z-Wave API Transport Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.1 Controller Node Send Data Command . . . . . . . . . . . . . . . . . . . . . . .
4.10.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.1.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.10.1.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.1.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.2 Controller Node Send Data Multicast Command . . . . . . . . . . . . . . . . .
4.10.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.2.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .

274
274
274
275
275
275
275
275
276
276
276
276
276
277
277
277
277
278
279
279
279
280
280
280
281
281
281
281
281
282
282
282
282
282
283
284
284
284
285
285
286
286
286
286
287
288
288
288
288
289
290
291
291
291
292
292
293
293
293

Specifications

Z-Wave API Specification, Release 2.9.0

August 20, 2025

4.10.2.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.2.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.3 End Node Send Data Command . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.3.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.10.3.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.3.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.4 End Node Send Data Multicast Command . . . . . . . . . . . . . . . . . . . . .
4.10.4.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.4.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.10.4.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.4.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.5 Bridge Controller Node Send Data Command . . . . . . . . . . . . . . . . . . .
4.10.5.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.5.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.10.5.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.5.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.6 Bridge Controller Node Send Data Multicast Command . . . . . . . . . . . . .
4.10.6.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.6.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.10.6.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.6.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.7 Send Data Abort Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.7.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.7.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.10.7.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.7.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.8 Send Test Frame Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.8.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.8.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.10.8.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.8.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.9 Controller Node Send Protocol Data Command . . . . . . . . . . . . . . . . . .
4.10.9.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.10.9.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.10.9.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.10.9.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.11 Z-Wave API Security Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.11.1 Security Setup Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.11.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.11.1.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.11.1.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.11.1.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.11.2 Encrypt Data With AES Command . . . . . . . . . . . . . . . . . . . . . . . .
4.11.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.11.2.2 1. Initial data frame (host → Z-Wave Module) . . . . . . . . . . . . .
4.11.2.3 2. Response data frame (Z-Wave Module → host) . . . . . . . . . . .
4.11.2.4 3. Callback data frame (Z-Wave Module → host) . . . . . . . . . . .
4.11.3 Request Protocol Command Class Encryption command . . . . . . . . . . . . .
4.11.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4.11.3.2 1. Initial data frame (Z-Wave Module → host) . . . . . . . . . . . . .
4.11.3.3 2. Response data frame (host → Z-Wave Module) . . . . . . . . . . .
4.11.3.4 3. Callback data frame (host → Z-Wave Module) . . . . . . . . . . .
4.12 Proprietary Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
References

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

294
294
295
295
295
296
297
298
298
298
299
299
300
300
300
301
301
302
302
302
303
303
304
304
305
305
305
306
306
306
306
307
308
308
308
309
309
310
311
311
311
312
314
315
315
315
315
316
317
317
318
319
319
319
320

This document may only be copied and distributed internally. Page 8

Specifications

1

Introduction

1.1

Disclaimer

Z-Wave API Specification, Release 2.9.0

August 20, 2025

THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.

1.2

Purpose

This document specifies the communication and commands used by host processors to interface with
a module supporting a Z-Wave API.

1.3

Audience and Requirements

The audience of this document is the Z-Wave Alliance members and Z-Wave developers.

1.4

Terms

This document describes mandatory and optional aspects of the required compliance of a Z-Wave
product to the Z-Wave standard.
The guidelines outlined in RFC 2119 with respect to key words used to indicate requirement levels are
followed. Essentially, the key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL
NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this
document are to be interpreted as described in RFC 2119.

1.5

Terminology And Abbreviations

Terminology and abbreviations used in this document are listed in Table 1.1
Table 1.1: Terminology and abbreviations
Term

Abbreviation

Description

Always Listening

AL (node)

Frequently Listening

FL (node)

Least Significant Byte

LSB

Most Significant Byte

MSB

Non-Listening

NL (node)

Network Wide Inclusion

NWI

Transmitter

Tx

Z-Wave node that is Always Listening. Refer to
[zwave_nwk_spec] for details.
Z-Wave node that is Frequently Listening. Refer
to [zwave_nwk_spec] for details.
Byte in the bytestream that has the lowest
weight
Byte in the bytestream that has the highest
weight
Z-Wave node that is Non-Listening. Refer to
[zwave_nwk_spec] for details.
Inclusion method leveraging Explore NDPU
to include through repeaters.
Refer to
[zwave_nwk_spec] for details.
RF Transmitter

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 9

Specifications

2

Z-Wave API Specification, Release 2.9.0

August 20, 2025

Overview

The Z-Wave Applications Programming Interface (Z-Wave API) allows a host interface to communicate with a Z-Wave chip through any kind of physical interface.
The host may be PC or a less powerful embedded host CPU, e.g., in a remote control or in a gateway
device. Depending on the chip family, the Z-Wave API is typically accessed via RS-232 or USB
physical interfaces.
Here are some of the applications leveraging the Z-Wave API:
• Gateway Application
• PC Controller
• Conformance Testing Tool (CTT)
In this specification, we will refer to:
• The host application: It is the application making use of the Z-Wave API via the physical
interface.
• The Z-Wave API Module: It is the Z-Wave API implementation providing an API to make use
of its Z-Wave capabilities.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 10

Z-Wave API Specification, Release 2.9.0

Specifications

3

August 20, 2025

Interface communication

This chapter defines the frames and communications frame flows between a Z-Wave API supporting
module and a host application. Several frames types are defined to enable session-like communication.

3.1

Table Syntax

The data and command format tables contains a column with byte/bit numbering. This column
specifies what byte offset the shown field is in the complete data frame. In some cases this is not a
fixed number and special systax notations are used.
Table 3.1: Table Syntax

3.2

byte\bit

Description

4
8+N
…
5/(5..6)
6/7

This field is a 1 byte field in byte 4 of the data frame
This field is the last field of N identical fields starting in byte 8
This field is a number of identical fields
This field starts at byte 5 but can be both 1 or 2 bytes long
This field is a 1 byte field located either in gyte 6 or 7

Frame types

3.2.1 Data Frame
The Data frame is used to transmit a command. It can be used it both directions (Z-Wave module
to host, or host to Z-Wave module). All data frames MUST be formatted according to Table 3.2.
Table 3.2: Data frame format
byte\bit

7

6

1
2
3
4
4+1
…
4+L
4+L+1

5

4

3

2

1

0

Frame Type = SOF (0x01)
Length
Type
Z-Wave API Command ID
Z-Wave API Command Payload 1
…
Z-Wave API Command Payload L
Checksum

Frame Type (8 bits)
This field is used to detect the type of frame being transmitted. For a data frame, this field MUST
be set to 0x01, indicating a Start of Frame (SOF).
Length (8 bits)
The Length field is used to indicate the total length, in bytes, of the following fields:
• Length (this field)
• Type
• Z-Wave API Command ID
• Z-Wave API Command Payload
The following fields MUST NOT be included in the length calculation:
• Start of frame
© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 11

Z-Wave API Specification, Release 2.9.0

Specifications

August 20, 2025

• Checksum
Type (8 bits)
The Type field is used to indicate the type of Command being sent in the data frame. It MUST be
encoded according to Table 3.3.
Table 3.3: Data frame format - Type encoding
Value

Description

0x00

Request frame. This type MUST be used by the host application for unsolicited
new commands. Z-Wave API callbacks MUST also use the Request type.
Response frame. This type MUST be used by the Z-Wave Module to issue
responses to Request frames.
Reserved values MUST NOT be used and MUST be ignored by a receiving
interface

0x01
0x02..0xFF

Z-Wave API Command ID (8 bits)
This field is used to advertise a command identifier that enable a receiving interface to parse the
payload. Commands are described in section Z-Wave API Commands.
Z-Wave API Command Payload (L bytes)
This field is used to indicate the payload associated with the Z-Wave API command. The payload for
each command is described in the Z-Wave API Commands section.
Checksum (8 bits)
The Checksum field is used to validate the data received in the Data Frame. The Checksum calculation
MUST include the following fields:
• Length
• Type
• Z-Wave API Command ID
• Z-Wave API Command Payload
The Checksum field MUST be calculated using XOR operations: Checksum = 0xFF (XOR) Length
(XOR) Type (XOR) Z-Wave API Command ID (XOR) Z-Wave API Command Payload 1 (XOR) …
(XOR) Z-Wave API Command Payload N
An interface receiving a non-matching checksum MUST return a NAK Frame. An interface receiving
a matching checksum MUST return an ACK Frame.
3.2.2 ACK Frame
The ACK frame is used to indicate the successful reception of a Data Frame. It MUST be formatted
according to Table 3.4.
Table 3.4: ACK frame format
byte\bit

7

6

1

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

5

4

3

2

1

0

Frame Type = ACK (0x06)

This document may only be copied and distributed internally. Page 12

Z-Wave API Specification, Release 2.9.0

Specifications

August 20, 2025

3.2.3 NAK Frame
The NAK frame is used to indicate an error in the reception of a Data Frame. It MUST be formatted
according to Table 3.5.
Table 3.5: NAK frame format
byte\bit

7

6

1

5

4

3

2

1

0

Frame Type = NAK (0x15)

3.2.4 CAN Frame
The CAN frame is used to indicate the detection of a collision during Data Frame transmissions.
A CAN frame is most often returned when the UART is both transmitting and receiving at the same
time (a collision). This results in the receiving end receiving a frame it did not expect and thus it
drops the frame and returns a CAN. The transmitting end typically is also receiving a frame which
it must process and ACK and then retransmit the frame that was returned with a CAN after an
appropriate backoff interval.
It MUST be formatted according to Table 3.6.
Table 3.6: CAN frame format
byte\bit

7

6

1

3.3

5

4

3

2

1

0

Frame Type = CAN (0x18)

Command frame flows

The Z-Wave API has several possible command frame flows:
• Unacknowledged frame
• Acknowledged frame
• Acknowledged frame with response
• Acknowledged frame with callback
• Acknowledged frame with response and callback
• Unsolicited frame
In the following subsections and the rest of this specification, the frames are numbered as follow:
1. initial data frame: it is the initial (request type) data frame from the host to the Z-Wave module.
2. response data frame: it is a response type data frame returned to an initial data frame from the
Z-Wave module to the host.
3. callback data frame: it is a request type data frame sent from the Z-Wave module to the host, after
it has completed an action triggered by an initial data frame.
4. unsolicited data frame: it is a request type data frame sent from the Z-Wave module to the host.

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 13

Specifications

Z-Wave API Specification, Release 2.9.0

August 20, 2025

3.3.1 Unacknowledged frame
There MAY be data frames that will not be acknowledged by the destination because of hardware
or software restrictions. It can for example happen if the command instructs the Z-Wave module to
enter reprogramming mode or go offline.
The communication flow MUST be as shown in Figure 3.1

Figure 3.1: Unacknowledged frame
If a command is supposed to trigger an unacknowledged frame transmission, the host MUST NOT try
to retransmit the command if no ACK frame is received. The host MUST retransmit the command
if a NAK Frame or a CAN Frame is received.
3.3.2 Acknowledged frame
Acknowledged frames are frames that will not trigger any communication back from the Z-Wave
module, apart from an ACK Frame. The communication flow MUST be as shown in Figure 3.2

Figure 3.2: Acknowledged frame

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 14

Specifications

Z-Wave API Specification, Release 2.9.0

August 20, 2025

3.3.3 Acknowledged frame with response
Acknowledged frames with response are acknowledged frames that will trigger an immediate response
from the Z-Wave module. The communication flow MUST be as shown in Figure 3.3

Figure 3.3: Acknowledged frame with response
3.3.4 Acknowledged frame with callback
Acknowledged frames with callback are acknowledged frames that will trigger a callback after an
operation has been performed by the Z-Wave module. The communication flow MUST be as shown
in Figure 3.4

Figure 3.4: Acknowledged frame with callback

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 15

Z-Wave API Specification, Release 2.9.0

Specifications

August 20, 2025

In some cases, an Initial Data Frame MAY trigger several callback frames.
3.3.5 Acknowledged frame with response and callback
Acknowledged frames with response and callback are acknowledged frames that will trigger both an
immediate response and an additional callback after an operation has been performed by the Z-Wave
module. The communication flow MUST be as shown in Figure 3.5

Figure 3.5: Acknowledged frame with response and callback
In some cases, an Initial Data Frame MAY trigger several callback frames.
3.3.6 Unsolicited frame
Unsolicited frames are frames that are sent from the Z-Wave module to inform the host application
that an event happened. The communication flow MUST be as shown in Figure 3.6

Figure 3.6: Unsolicited frame

© 2025 Z-Wave Alliance, Inc. All Rights Reserved

This document may only be copied and distributed internally. Page 16

Z-Wave API Specification, Release 2.9.0

Specifications

3.4

August 20, 2025

Error handling

The following subsections show how to handle communications issues between the Z-Wave Module
and the host application.
3.4.1 Retransmission timing
In general, retransmissions of a Data Frame MUST apply back-off timers.
The minimum back-off in milliseconds MUST be calculated according to (3.1)
𝑇𝑛 = 100 + 𝑛 × 1000.

(3.1)

where:
• n is the retransmission number - 1. i.e. n=0 for the first retransmission.
A sending interface SHOULD add an additional random delay to the minimum back-off.
3.4.2 Missing Acknowledgment
By default, all data frames MUST be acknowledged by the receiving interface. Acknowledgement
consists in sending an ACK Frame.
A sending interface MUST wait for 1600ms or more for an ACK Frame after transmitting a Data
Frame.
In case of missing a

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

**Last Updated**: 2026-03-07T20:11:55.440014
