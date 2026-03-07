# Z-Wave Application Specification

**Source**: Z-Wave Alliance 2025-B Specification Package
**Date**: 2026-03-07
**Version**: 2025-B

## Overview

Complete command classes, device types, and application layer protocols

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
Application Work Group Z-Wave
Specifications

Release 2025B

Z-Wave Alliance
Aug 18, 2025

Table of Contents
1 Introduction
1.1 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.2 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.3 Audience and Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.4 Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.5 Terminology And Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

40
40
40
40
40
41

2 Application Command Classes
2.1 Command Class Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.2 Command class format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.2.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.2.1.1 Command class . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.2.1.2 Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.2.1.3 Command data (N bytes) . . . . . . . . . . . . . . . . . . . .
2.1.2.2 Command class versioning . . . . . . . . . . . . . . . . . . . . . . . .
2.1.3 Controlled and Supported Command Classes . . . . . . . . . . . . . . . . . . .
2.1.4 Node Information Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.4.1 Z-Wave Protocol Specific Part . . . . . . . . . . . . . . . . . . . . . .
2.1.4.2 Application Specific Part . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.4.3 NIF and Multi Channel/Security Command Classes . . . . . . . . . .
2.1.4.3.1 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.4.4 Command Class specific NIF rules . . . . . . . . . . . . . . . . . . . .
2.1.5 Multicast and broadcast commands . . . . . . . . . . . . . . . . . . . . . . . .
2.1.6 Actuator Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.6.1 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.6.2 Reporting values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.6.3 Command values vs. hardware values . . . . . . . . . . . . . . . . . .
2.1.6.4 Supporting multiple actuator Command Classes . . . . . . . . . . . .
2.1.7 Common fields and encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.7.1 Reserved and Res fields . . . . . . . . . . . . . . . . . . . . . . . . . .

42
42
42
42
42
42
43
43
43
44
44
45
45
46
47
48
49
49
49
50
50
50
50
50

2.2

2.1.7.2 Reserved values and reserved bits . . . . . . . . . . . . . . . . . . . .
2.1.7.3 Duration encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.7.4 Unsigned encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.7.5 Signed encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1.7.6 Fields values and version . . . . . . . . . . . . . . . . . . . . . . . . .
Command Class Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1 Active Schedule Command Class, version 1 [NEVER CERTIFIED] . . . . . . .
2.2.1.1 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1.1.1 Targets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1.1.2 Schedules . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1.1.3 Schedule Enabled Definitions . . . . . . . . . . . . . . . . . .
2.2.1.1.4 Schedule Metadata . . . . . . . . . . . . . . . . . . . . . . . .
2.2.1.2 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.1.3 Active Schedule Capabilities Get Command . . . . . . . . . . . . . . .
2.2.1.4 Active Schedule Capabilities Report Command . . . . . . . . . . . . .
2.2.1.5 Active Schedule Enable Set Command . . . . . . . . . . . . . . . . . .
2.2.1.6 Active Schedule Enable Get Command . . . . . . . . . . . . . . . . .
2.2.1.7 Active Schedule Enable Report Command . . . . . . . . . . . . . . .
2.2.1.8 Active Schedule Year Day Schedule Set Command . . . . . . . . . . .
2.2.1.9 Active Schedule Year Day Schedule Get Command . . . . . . . . . . .
2.2.1.10 Active Schedule Year Day Schedule Report Command . . . . . . . . .
2.2.1.11 Active Schedule Daily Repeating Schedule Set Command . . . . . . .
2.2.1.12 Active Schedule Daily Repeating Schedule Get Command . . . . . . .
2.2.1.13 Active Schedule Daily Repeating Schedule Report Command . . . . .
2.2.2 Alarm Command Class, version 1 [DEPRECATED] . . . . . . . . . . . . . . .
2.2.2.1 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.2.2 Alarm Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.2.3 Alarm Report Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.3 Alarm Command Class, version 2 [DEPRECATED] . . . . . . . . . . . . . . .
2.2.3.1 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.3.2 Alarm Set Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.3.3 Alarm Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.3.4 Alarm Report Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.3.5 Alarm Type Supported Get Command . . . . . . . . . . . . . . . . .
2.2.3.6 Alarm Type Supported Report Command . . . . . . . . . . . . . . . .
2.2.4 Alarm Sensor Command Class, version 1 [DEPRECATED] . . . . . . . . . . .
2.2.4.1 Alarm Sensor Get Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.4.2 Alarm Sensor Report Command . . . . . . . . . . . . . . . . . . . . .
2.2.4.3 Alarm Sensor Supported Get Command . . . . . . . . . . . . . . . . .
2.2.4.4 Alarm Sensor Supported Report Command . . . . . . . . . . . . . . .
2.2.5 Alarm Silence Command Class, version 1 . . . . . . . . . . . . . . . . . . . . .
2.2.5.1 Alarm Silence Set Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.6 All Switch Command Class, version 1 [OBSOLETED] . . . . . . . . . . . . . .
2.2.6.1 All Switch Set Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.6.2 All Switch Get Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.6.3 All Switch Report Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.6.4 All Switch On Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.6.5 All Switch Off Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.7 Anti-theft Command Class, version 1 [OBSOLETED] . . . . . . . . . . . . . .
2.2.8 Anti-theft Command Class, version 2 [DEPRECATED] . . . . . . . . . . . . .
2.2.8.1 Anti-theft Set Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.8.2 Anti-theft Get Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.8.3 Anti-theft Report Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.8.4 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.8.4.1 Example of a non-secure Thermostat . . . . . . . . . . . . .
2.2.8.4.2 Example of a security enabled Thermostat . . . . . . . . . .
2.2.9 Anti-theft Command Class, version 3 . . . . . . . . . . . . . . . . . . . . . . . .
2.2.9.1 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.9.1.1 Command Class dependencies . . . . . . . . . . . . . . . . .

51
51
51
52
52
53
54
54
54
55
56
56
56
56
57
58
58
59
59
62
63
64
65
66
67
67
67
68
69
69
69
70
70
71
71
73
73
74
74
75
76
76
77
77
77
78
78
78
79
80
81
82
82
84
84
84
86
86
86

2.2.9.1.2 Lock/Unlock requirements . . . . . . . . . . . . . . . . . . .
2.2.9.1.3 Multi Channel Considerations . . . . . . . . . . . . . . . . .
2.2.9.2 Anti-Theft Set Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.9.3 Anti-theft Get Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.9.4 Anti-Theft Report Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.10 Anti-theft Unlock Command Class, version 1 . . . . . . . . . . . . . . . . . . .
2.2.10.1 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.10.1.1 Multi Channel Considerations . . . . . . . . . . . . . . . . .
2.2.10.2 Anti-Theft Unlock State Get Command . . . . . . . . . . . . . . . . .
2.2.10.3 Anti-Theft Unlock State Report Command . . . . . . . . . . . . . . .
2.2.10.4 Anti-Theft Unlock Set Command . . . . . . . . . . . . . . . . . . . .
2.2.11 Authentication Command Class, version 1 [NEVER CERTIFIED] . . . . . . .
2.2.11.1 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.11.2 Interoperability Considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.11.3 Authentication Capability Get Command . . . . . . . . . . . . . . . .
2.2.11.4 Authentication Capability Report Command . . . . . . . . . . . . . .
2.2.11.5 Authentication Data Set Command . . . . . . . . . . . . . . . . . . .
2.2.11.6 Authentication Data Get Command . . . . . . . . . . . . . . . . . . .
2.2.11.7 Authentication Data Report Command . . . . . . . . . . . . . . . . .
2.2.11.8 Authentication Technologies Combination Set Command . . . . . . .
2.2.11.9 Authentication Technologies Combination Get Command . . . . . . .
2.2.11.10 Authentication Technologies Combination Report Command . . . . .
2.2.11.11 Authentication Checksum Get Command . . . . . . . . . . . . . . . .
2.2.11.12 Authentication Checksum Report Command . . . . . . . . . . . . . .
2.2.11.13 Examples and use-cases . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.12 Authentication Media Write Command Class, version 1 [NEVER CERTIFIED]
2.2.12.1 Authentication Media Capability Get Command . . . . . . . . . . . .
2.2.12.2 Authentication Media Capability Report Command . . . . . . . . . .
2.2.12.3 Authentication Media Write Start Command . . . . . . . . . . . . . .
2.2.12.4 Authentication Media Write Stop Command . . . . . . . . . . . . . .
2.2.12.5 Authentication Media Write Status Command . . . . . . . . . . . . .
2.2.13 Barrier Operator Command Class, version 1 . . . . . . . . . . . . . . . . . . . .
2.2.13.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.13.1.1 Node Information Frame (NIF) . . . . . . . . . . . . . . . . .
2.2.13.1.2 Command Class dependencies . . . . . . . . . . . . . . . . .
2.2.13.2 Barrier Operator Set Command . . . . . . . . . . . . . . . . . . . . .
2.2.13.2.1 Error Handling . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.13.3 Barrier Operator Get Command . . . . . . . . . . . . . . . . . . . . .
2.2.13.4 Barrier Operator Report Command . . . . . . . . . . . . . . . . . . .
2.2.13.5 Barrier Operator Get Signaling Capabilities Supported Command . .
2.2.13.6 Barrier Operator Report Signaling Capabilities Supported Command
2.2.13.7 Barrier Operator Event Signal Set Command . . . . . . . . . . . . . .
2.2.13.8 Barrier Operator Event Signaling Get Command . . . . . . . . . . . .
2.2.13.9 Barrier Operator Event Signaling Report Command . . . . . . . . . .
2.2.14 Basic Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.14.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.14.1.1 Node Information Frame (NIF) . . . . . . . . . . . . . . . . .
2.2.14.2 Basic Set Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.14.3 Basic Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.14.4 Basic Report Command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.15 Basic Command Class, version 2 . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.15.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.15.2 Basic Report Command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.16 Basic Tariff Information Command Class, version 1 [NEVER CERTIFIED] . .
2.2.16.1 Basic Tariff Information Get Command . . . . . . . . . . . . . . . . .
2.2.16.2 Basic Tariff Information Report Command . . . . . . . . . . . . . . .
2.2.17 Basic Window Covering Command Class, version 1 [OBSOLETED] . . . . . .
2.2.17.1 Basic Window Covering Start Level Change Command . . . . . . . .
2.2.17.2 Basic Window Covering Stop Level Change Command . . . . . . . . .

86
87
87
88
89
91
91
91
91
91
93
94
94
94
95
95
97
98
99
101
104
105
107
108
110
112
112
112
113
114
114
116
116
116
116
116
117
117
118
118
119
119
120
120
121
121
121
121
122
122
123
123
123
125
125
125
128
128
128

2.2.18 Binary Sensor Command Class, version 1 [DEPRECATED] . . . . . . . . . . .
2.2.18.1 Binary Sensor Get Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.18.2 Binary Sensor Report Command . . . . . . . . . . . . . . . . . . . . .
2.2.19 Binary Sensor Command Class, version 2 [DEPRECATED] . . . . . . . . . . .
2.2.19.1 Binary Sensor Get Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.19.2 Binary Sensor Report Command . . . . . . . . . . . . . . . . . . . . .
2.2.19.3 Binary Sensor Get Supported Sensor Command . . . . . . . . . . . .
2.2.19.4 Binary Sensor Supported Sensor Report Command . . . . . . . . . .
2.2.20 Binary Switch Command Class, version 1 . . . . . . . . . . . . . . . . . . . . .
2.2.20.1 Binary Switch Set Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.20.2 Binary Switch Get Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.20.3 Binary Switch Report Command . . . . . . . . . . . . . . . . . . . . .
2.2.21 Binary Switch Command Class, version 2 . . . . . . . . . . . . . . . . . . . . .
2.2.21.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.21.2 Binary Switch Set Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.21.3 Binary Switch Report Command . . . . . . . . . . . . . . . . . . . . .
2.2.22 Binary Toggle Switch Command Class, version 1 [OBSOLETED] . . . . . . . .
2.2.22.1 Binary Toggle Switch Set Command . . . . . . . . . . . . . . . . . . .
2.2.22.2 Binary Toggle Switch Get Command . . . . . . . . . . . . . . . . . .
2.2.22.3 Binary Toggle Switch Report Command . . . . . . . . . . . . . . . . .
2.2.23 Central Scene Command Class, version 1 [OBSOLETED] . . . . . . . . . . . .
2.2.23.1 Central Scene Supported Get Command . . . . . . . . . . . . . . . . .
2.2.23.2 Central Scene Supported Report Command . . . . . . . . . . . . . . .
2.2.23.3 Central Scene Notification Command . . . . . . . . . . . . . . . . . .
2.2.24 Central Scene Command Class, version 2 [OBSOLETED] . . . . . . . . . . . .
2.2.24.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.24.2 Central Scene Supported Report Command . . . . . . . . . . . . . . .
2.2.24.3 Central Scene Notification Command . . . . . . . . . . . . . . . . . .
2.2.25 Central Scene Command Class, version 3 . . . . . . . . . . . . . . . . . . . . .
2.2.25.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.25.1.1 Central Scene Configuration commands support . . . . . . .
2.2.25.1.2 Multi Channel considerations . . . . . . . . . . . . . . . . . .
2.2.25.2 Central Scene Configuration Set Command . . . . . . . . . . . . . . .
2.2.25.3 Central Scene Configuration Get Command . . . . . . . . . . . . . . .
2.2.25.4 Central Scene Configuration Report Command . . . . . . . . . . . . .
2.2.25.5 Central Scene Supported Get Command . . . . . . . . . . . . . . . . .
2.2.25.6 Central Scene Supported Report Command . . . . . . . . . . . . . . .
2.2.25.7 Central Scene Notification Command . . . . . . . . . . . . . . . . . .
2.2.26 Climate Control Schedule Command Class, version 1 [DEPRECATED] . . . .
2.2.26.1 Schedule Set Command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.26.2 Schedule Get Command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.26.3 Schedule Report Command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.26.4 Schedule Changed Get Command . . . . . . . . . . . . . . . . . . . .
2.2.26.5 Schedule Changed Report Command . . . . . . . . . . . . . . . . . .
2.2.26.6 Schedule Override Set Command . . . . . . . . . . . . . . . . . . . . .
2.2.26.7 Schedule Override Get Command . . . . . . . . . . . . . . . . . . . .
2.2.26.8 Schedule Override Report Command . . . . . . . . . . . . . . . . . .
2.2.27 Clock Command Class, version 1 [DEPRECATED] . . . . . . . . . . . . . . . .
2.2.27.1 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.27.2 Multi Channel Considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.27.3 Clock Set Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.27.4 Clock Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.27.5 Clock Report Command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.28 Color Switch Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . .
2.2.28.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.28.1.1 Command Class dependencies . . . . . . . . . . . . . . . . .
2.2.28.2 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.28.3 Color Switch Supported Get Command . . . . . . . . . . . . . . . . .
2.2.28.4 Color Switch Supported Report Command . . . . . . . . . . . . . . .

129
129
129
130
130
131
131
132
133
133
133
134
135
135
135
135
137
137
137
137
138
139
139
139
142
142
142
143
145
145
146
146
146
146
147
147
148
148
150
151
152
152
152
153
153
155
155
156
156
156
156
157
157
158
158
158
158
159
159

2.2.28.5 Color Switch Get Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.28.6 Color Switch Report Command . . . . . . . . . . . . . . . . . . . . .
2.2.28.7 Color Switch Set Command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.28.8 Color Switch Start Level Change Command . . . . . . . . . . . . . .
2.2.28.9 Color Switch Stop Level Change Command . . . . . . . . . . . . . . .
2.2.29 Color Switch Command Class, version 2 . . . . . . . . . . . . . . . . . . . . . .
2.2.29.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.29.1.1 Command Class dependencies . . . . . . . . . . . . . . . . .
2.2.29.2 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.29.3 Color Switch Set Command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.30 Color Switch Command Class, version 3 . . . . . . . . . . . . . . . . . . . . . .
2.2.30.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.30.1.1 Command Class dependencies . . . . . . . . . . . . . . . . .
2.2.30.2 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.30.3 Color Switch Report Command . . . . . . . . . . . . . . . . . . . . .
2.2.30.4 Color Switch Start Level Change Command . . . . . . . . . . . . . .
2.2.31 Configuration Command Class, version 1 . . . . . . . . . . . . . . . . . . . . .
2.2.31.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.31.1.1 “Default” flag . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.31.2 Configuration Set Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.31.3 Configuration Get Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.31.4 Configuration Report Command . . . . . . . . . . . . . . . . . . . . .
2.2.32 Configuration Command Class, version 2 . . . . . . . . . . . . . . . . . . . . .
2.2.32.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.32.1.1 “Default” flag . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.32.2 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.32.3 Configuration Set Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.32.4 Configuration Bulk Set Command . . . . . . . . . . . . . . . . . . . .
2.2.32.5 Configuration Bulk Get Command . . . . . . . . . . . . . . . . . . . .
2.2.32.6 Configuration Bulk Report Command . . . . . . . . . . . . . . . . . .
2.2.33 Configuration Command Class, version 3 . . . . . . . . . . . . . . . . . . . . .
2.2.33.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.33.1.1 “Default” flag . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.33.1.2 Configuration Properties Report . . . . . . . . . . . . . . . .
2.2.33.2 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.33.3 Configuration Name Get Command . . . . . . . . . . . . . . . . . . .
2.2.33.4 Configuration Name Report Command . . . . . . . . . . . . . . . . .
2.2.33.5 Configuration Info Get Command . . . . . . . . . . . . . . . . . . . .
2.2.33.6 Configuration Info Report Command . . . . . . . . . . . . . . . . . .
2.2.33.7 Configuration Properties Get Command . . . . . . . . . . . . . . . . .
2.2.33.8 Configuration Properties Report Command . . . . . . . . . . . . . . .
2.2.34 Configuration Command Class, version 4 . . . . . . . . . . . . . . . . . . . . .
2.2.34.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.34.1.1 Multi Channel Consideration . . . . . . . . . . . . . . . . . .
2.2.34.1.2 “Default” flag . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.34.1.3 Configuration Properties Report . . . . . . . . . . . . . . . .
2.2.34.1.4 “Altering capabilities” flag . . . . . . . . . . . . . . . . . . .
2.2.34.1.5 “Advanced” flag . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.34.1.6 Parameters value and network inclusion/exclusion . . . . . .
2.2.34.1.7 Bulk commands support . . . . . . . . . . . . . . . . . . . .
2.2.34.2 Configuration Set Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.34.3 Configuration Bulk Set Command . . . . . . . . . . . . . . . . . . . .
2.2.34.4 Configuration Properties Report Command . . . . . . . . . . . . . . .
2.2.34.5 Configuration Default Reset Command . . . . . . . . . . . . . . . . .
2.2.35 Controller Replication Command Class, version 1 . . . . . . . . . . . . . . . . .
2.2.35.1 Transfer group command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.35.2 Transfer Group Name Command . . . . . . . . . . . . . . . . . . . . .
2.2.35.3 Transfer scene command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.35.4 Transfer Scene Name Command . . . . . . . . . . . . . . . . . . . . .

159
160
160
161
162
163
163
163
163
163
165
165
165
165
165
166
167
167
167
167
169
169
170
170
170
170
170
171
172
173
175
175
176
176
176
176
177
177
178
179
180
182
182
182
182
182
183
183
183
183
184
184
185
186
187
187
187
188
188

2.2.36 Demand Control Plan Configuration Command Class, version 1 . . . . . . . . .
2.2.36.1 DCP list supported get command . . . . . . . . . . . . . . . . . . . .
2.2.36.2 DCP list supported report command . . . . . . . . . . . . . . . . . .
2.2.36.3 DCP list set command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.36.4 DCP list remove . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.37 Demand Control Plan Monitor Command Class, version 1 . . . . . . . . . . . .
2.2.37.1 DCP list get command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.37.2 DCP list report command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.37.3 DCP event status get . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.37.4 DCP event status report . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.38 Door Lock Command Class, version 1-2 . . . . . . . . . . . . . . . . . . . . . .
2.2.38.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.38.2 Door Lock Operation Set Command . . . . . . . . . . . . . . . . . . .
2.2.38.3 Door Lock Operation Get Command . . . . . . . . . . . . . . . . . .
2.2.38.4 Door Lock Operation Report Command . . . . . . . . . . . . . . . . .
2.2.38.5 Door Lock Configuration Set Command . . . . . . . . . . . . . . . . .
2.2.38.6 Door Lock Configuration Get Command . . . . . . . . . . . . . . . .
2.2.38.7 Door Lock Configuration Report Command . . . . . . . . . . . . . . .
2.2.39 Door Lock Command Class, version 3 . . . . . . . . . . . . . . . . . . . . . . .
2.2.39.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.39.2 Door Lock Operation Report Command . . . . . . . . . . . . . . . . .
2.2.40 Door Lock Command Class, version 4 . . . . . . . . . . . . . . . . . . . . . . .
2.2.40.1 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.40.2 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.40.3 Door Lock Operation Set Command . . . . . . . . . . . . . . . . . . .
2.2.40.4 Door Lock Operation Get Command . . . . . . . . . . . . . . . . . .
2.2.40.5 Door Lock Operation Report Command . . . . . . . . . . . . . . . . .
2.2.40.6 Door Lock Configuration Set Command . . . . . . . . . . . . . . . . .
2.2.40.7 Door Lock Configuration Get Command . . . . . . . . . . . . . . . .
2.2.40.8 Door Lock Configuration Report Command . . . . . . . . . . . . . . .
2.2.40.9 Door Lock Capabilities Get Command . . . . . . . . . . . . . . . . . .
2.2.40.10 Door Lock Capabilities Report Command . . . . . . . . . . . . . . . .
2.2.41 Door Lock Logging Command Class, version 1 . . . . . . . . . . . . . . . . . .
2.2.41.1 Door Lock Logging Records Supported Get Command . . . . . . . . .
2.2.41.2 Door Lock Logging Records Supported Report Command . . . . . . .
2.2.41.3 Door Lock Logging Record Get Command . . . . . . . . . . . . . . .
2.2.41.4 Door Lock Logging Record Report Command . . . . . . . . . . . . .
2.2.42 Energy Production Command Class, version 1 [NEVER CERTIFIED] . . . . .
2.2.42.1 Energy Production Get Command . . . . . . . . . . . . . . . . . . . .
2.2.42.2 Energy Production Report Command . . . . . . . . . . . . . . . . . .
2.2.43 Entry Control Command Class, version 1 . . . . . . . . . . . . . . . . . . . . .
2.2.43.1 Interoperability Considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.43.2 Security Considerations . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.43.3 Handling user supplied data . . . . . . . . . . . . . . . . . . . . . . .
2.2.43.4 Handling Incorrect Entry . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.43.5 Entry Control Notification Command . . . . . . . . . . . . . . . . . .
2.2.43.6 Entry Control Key Supported Get Command . . . . . . . . . . . . . .
2.2.43.7 Entry Control Key Supported Report Command . . . . . . . . . . . .
2.2.43.8 Entry Control Event Supported Get Command . . . . . . . . . . . . .
2.2.43.9 Entry Control Event Supported Report Command . . . . . . . . . . .
2.2.43.10 Entry Control Configuration Set Command . . . . . . . . . . . . . . .
2.2.43.11 Entry Control Configuration Get Command . . . . . . . . . . . . . .
2.2.43.12 Entry Control Configuration Report Command . . . . . . . . . . . . .
2.2.43.13 Event Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.44 Generic Schedule Command Class, version 1 [OBSOLETED] [NEVER CERTIFIED] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.44.1 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.44.2 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.44.3 Generic Schedule Capabilities Get Command . . . . . . . . . . . . . .

189
189
189
190
193
195
195
195
196
196
198
198
198
199
199
201
202
203
204
204
204
205
205
205
206
206
207
209
212
212
213
213
216
216
216
216
217
220
220
220
222
222
222
223
223
224
225
225
226
226
227
228
228
229
230
230
230
230

2.2.44.4 Generic Schedule Capabilities Report Command . . . . . . . . . . . .
2.2.44.5 Generic Schedule Time Range Set Command . . . . . . . . . . . . . .
2.2.44.5.1 Time Range parameters and rules . . . . . . . . . . . . . . .
2.2.44.5.2 All parameters specified . . . . . . . . . . . . . . . . . . . . .
2.2.44.5.3 Some parameters undefined in parameter groups . . . . . . .
2.2.44.5.4 All parameters missing from a parameter group . . . . . . .
2.2.44.6 Generic Schedule Time Range Get Command . . . . . . . . . . . . . .
2.2.44.7 Generic Schedule Time Range Report Command . . . . . . . . . . . .
2.2.44.8 Generic Schedule Set Command . . . . . . . . . . . . . . . . . . . . .
2.2.44.8.1 Schedules and Time Ranges examples . . . . . . . . . . . . .
2.2.44.8.2 Example 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.44.8.3 Example 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.44.8.4 Example 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.44.8.5 Example 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.44.9 Generic Schedule Get Command . . . . . . . . . . . . . . . . . . . . .
2.2.44.10 Generic Schedule Report Command . . . . . . . . . . . . . . . . . . .
2.2.45 Geographic Location Command Class, version 1 [OBSOLETED] . . . . . . . .
2.2.45.1 Multi Channel Considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.45.2 Geographic Location Set Command . . . . . . . . . . . . . . . . . . .
2.2.45.3 Geographic Location Get Command . . . . . . . . . . . . . . . . . . .
2.2.45.4 Geographic Location Report Command . . . . . . . . . . . . . . . . .
2.2.46 Geographic Location Command Class, version 2 [NEVER CERTIFIED] . . . .
2.2.46.1 Z-Wave Geographic Location Command Class V2 obsoletes V1 . . . .
2.2.46.2 Multi Channel Considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.46.3 Geographic Location V2 Features . . . . . . . . . . . . . . . . . . . .
2.2.46.4 Geographic Location V2 Examples . . . . . . . . . . . . . . . . . . . .
2.2.46.5 Geographic Location Set Command . . . . . . . . . . . . . . . . . . .
2.2.46.6 Geographic Location Get Command . . . . . . . . . . . . . . . . . . .
2.2.46.7 Geographic Location Report Command . . . . . . . . . . . . . . . . .
2.2.47 HRV Status Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . .
2.2.47.1 HRV Status Get Command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.47.2 HRV Status Report Command . . . . . . . . . . . . . . . . . . . . . .
2.2.47.3 HRV Status Supported Get Command . . . . . . . . . . . . . . . . . .
2.2.47.4 HRV Status Supported Report Command . . . . . . . . . . . . . . . .
2.2.48 HRV Control Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . .
2.2.48.1 HRV Mode Set Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.48.2 HRV Mode Get Command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.48.3 HRV Mode Report Command . . . . . . . . . . . . . . . . . . . . . .
2.2.48.4 HRV Bypass Set Command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.48.5 HRV Bypass Get Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.48.6 HRV Bypass Report Command . . . . . . . . . . . . . . . . . . . . . .
2.2.48.7 HRV Ventilation Rate Set Command . . . . . . . . . . . . . . . . . .
2.2.48.8 HRV Ventilation Rate Get Command . . . . . . . . . . . . . . . . . .
2.2.48.9 HRV Ventilation Rate Report Command . . . . . . . . . . . . . . . .
2.2.48.10 HRV Mode Supported Get Command . . . . . . . . . . . . . . . . . .
2.2.48.11 HRV Mode Supported Report Command . . . . . . . . . . . . . . . .
2.2.49 Humidity Control Mode Command Class, version 1 . . . . . . . . . . . . . . . .
2.2.49.1 Humidity Control Mode Set Command . . . . . . . . . . . . . . . . .
2.2.49.2 Humidity Control Mode Get Command . . . . . . . . . . . . . . . . .
2.2.49.3 Humidity Control Mode Report Command . . . . . . . . . . . . . . .
2.2.49.4 Humidity Control Mode Supported Get Command . . . . . . . . . . .
2.2.49.5 Humidity Control Mode Supported Report Command . . . . . . . . .
2.2.50 Humidity Control Operating State Class, version 1 . . . . . . . . . . . . . . . .
2.2.50.1 Humidity Control Operating State Get Command . . . . . . . . . . .
2.2.50.2 Humidity Control Operating State Report Command . . . . . . . . .
2.2.51 Humidity Control Setpoint Command Class, version 1-2 . . . . . . . . . . . . .
2.2.51.1 Humidity Control Setpoint Set Command . . . . . . . . . . . . . . . .
2.2.51.2 Humidity Control Setpoint Get Command . . . . . . . . . . . . . . .
2.2.51.3 Humidity Control Setpoint Report Command . . . . . . . . . . . . . .

231
232
235
235
235
236
236
237
238
239
239
239
239
240
240
240
242
242
242
243
243
244
244
244
244
245
245
246
247
249
249
249
250
250
252
252
252
253
253
253
254
254
254
255
255
255
257
257
257
258
258
258
260
260
260
261
261
262
262

2.2.51.4 Humidity Control Setpoint Supported Get Command . . . . . . . . .
2.2.51.5 Humidity Control Setpoint Supported Report Command . . . . . . .
2.2.51.6 Humidity Control Setpoint Scale Supported Get Command . . . . . .
2.2.51.7 Humidity Control Setpoint Scale Supported Report Command . . . .
2.2.51.8 Humidity Control Setpoint Capabilities Get Command . . . . . . . .
2.2.51.9 Humidity Control Setpoint Capabilities Report Command . . . . . .
2.2.52 IR Repeater Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . .
2.2.52.1 IR Repeater Capabilities Get Command . . . . . . . . . . . . . . . . .
2.2.52.2 IR Repeater Capabilities Report Command . . . . . . . . . . . . . . .
2.2.52.3 IR Repeater IR Code Learning Start Command . . . . . . . . . . . .
2.2.52.4 IR Repeater IR Code Learning Stop Command . . . . . . . . . . . . .
2.2.52.5 IR Repeater IR Code Learning Status Command . . . . . . . . . . . .
2.2.52.6 IR Repeater Learnt IR Code Remove Command . . . . . . . . . . . .
2.2.52.7 IR Repeater Learnt IR Code Get Command . . . . . . . . . . . . . .
2.2.52.8 IR Repeater Learnt IR Code Report Command . . . . . . . . . . . .
2.2.52.9 IR Repeater Learnt IR Code Readback Get Command . . . . . . . .
2.2.52.10 IR Repeater Learnt IR Code Readback Report Command . . . . . . .
2.2.52.11 IR Repeater Configuration Set Command . . . . . . . . . . . . . . . .
2.2.52.12 IR Repeater Configuration Get Command . . . . . . . . . . . . . . .
2.2.52.13 IR Repeater Configuration Report Command . . . . . . . . . . . . . .
2.2.52.14 IR Repeater Repeat Learnt Code Command . . . . . . . . . . . . . .
2.2.52.15 IR Repeater Repeat Command . . . . . . . . . . . . . . . . . . . . . .
2.2.53 Irrigation Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . . . .
2.2.53.1 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.53.2 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.53.2.1 Multi Channel considerations . . . . . . . . . . . . . . . . . .
2.2.53.3 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . .
2.2.53.3.1 Controlling methods . . . . . . . . . . . . . . . . . . . . . . .
2.2.53.4 Irrigation System Info Get Command . . . . . . . . . . . . . . . . . .
2.2.53.5 Irrigation System Info Report Command . . . . . . . . . . . . . . . .
2.2.53.6 Irrigation System Status Get Command . . . . . . . . . . . . . . . . .
2.2.53.7 Irrigation System Status Report Command . . . . . . . . . . . . . . .
2.2.53.8 Irrigation System Config Set Command . . . . . . . . . . . . . . . . .
2.2.53.9 Irrigation System Config Get Command . . . . . . . . . . . . . . . . .
2.2.53.10 Irrigation System Config Report Command . . . . . . . . . . . . . . .
2.2.53.11 Irrigation Valve Info Get Command . . . . . . . . . . . . . . . . . . .
2.2.53.12 Irrigation Valve Info Report Command . . . . . . . . . . . . . . . . .
2.2.53.13 Irrigation Valve Config Set Command . . . . . . . . . . . . . . . . . .
2.2.53.14 Irrigation Valve Config Get Command . . . . . . . . . . . . . . . . . .
2.2.53.15 Irrigation Valve Config Report Command . . . . . . . . . . . . . . . .
2.2.53.16 Irrigation Valve Run Command . . . . . . . . . . . . . . . . . . . . .
2.2.53.17 Irrigation Valve Table Set Command . . . . . . . . . . . . . . . . . .
2.2.53.18 Irrigation Valve Table Get Command . . . . . . . . . . . . . . . . . .
2.2.53.19 Irrigation Valve Table Report Command . . . . . . . . . . . . . . . .
2.2.53.20 Irrigation Valve Table Run Command . . . . . . . . . . . . . . . . . .
2.2.53.21 Irrigation System Shutoff Command . . . . . . . . . . . . . . . . . . .
2.2.54 Language Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . . . .
2.2.54.1 Language Set Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.54.2 Language Get Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.54.3 Language Report Command . . . . . . . . . . . . . . . . . . . . . . .
2.2.55 Lock Command Class, version 1 [DEPRECATED] . . . . . . . . . . . . . . . .
2.2.55.1 Lock Set Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.55.2 Lock Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.55.3 Lock Report Command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.56 Manufacturer Proprietary Command Class, version 1 [OBSOLETED] . . . . .
2.2.56.1 Manufacturer Proprietary Command . . . . . . . . . . . . . . . . . .
2.2.57 Meter Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.57.1 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.57.2 Meter Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . .

263
263
264
264
264
265
266
266
266
268
269
270
270
271
271
272
272
274
275
275
276
276
280
280
280
280
281
281
281
282
282
283
285
286
287
287
288
289
291
292
292
293
294
294
294
295
296
296
297
297
298
298
298
298
300
300
301
301
301

2.2.57.3 Meter Report Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.58 Meter Command Class, version 2 . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.58.1 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.58.2 Meter Supported Get Command . . . . . . . . . . . . . . . . . . . . .
2.2.58.3 Meter Supported Report Command . . . . . . . . . . . . . . . . . . .
2.2.58.4 Meter Reset Command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.58.5 Meter Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.58.6 Meter Report Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.59 Meter Command Class, version 3 . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.59.1 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.59.2 Meter Supported Report Command . . . . . . . . . . . . . . . . . . .
2.2.59.3 Meter Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.59.4 Meter Report command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.60 Meter Command Class, version 4 . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.60.1 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.60.2 Meter Supported Report Command . . . . . . . . . . . . . . . . . . .
2.2.60.3 Meter Get Command . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.60.4 Meter Report Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.61 Meter Command Class, version 5 . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.61.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.61.2 Meter Supported Report Command . . . . . . . . . . . . . . . . . . .
2.2.61.3 Meter Report Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.62 Meter Command Class, version 6 . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.62.1 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.62.2 Meter Reset Command . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.63 Meter Table Configuration Command Class, version 1 . . . . . . . . . . . . . .
2.2.63.1 Meter Table Point Adm Number Set Command . . . . . . . . . . . .
2.2.64 Meter Table Monitor Command Class, version 1 . . . . . . . . . . . . . . . . .
2.2.64.1 Meter Table Point Adm. Number Get Command . . . . . . . . . . . .
2.2.64.2 Meter Table Point Adm. Number Report Command . . . . . . . . . .
2.2.64.3 Meter Table ID Get Command . . . . . . . . . . . . . . . . . . . . . .
2.2.64.4 Meter Table ID Report Command . . . . . . . . . . . . . . . . . . . .
2.2.64.5 Meter Table Capability Get Command . . . . . . . . . . . . . . . . .
2.2.64.6 Meter Table Capability Report Command . . . . . . . . . . . . . . . .
2.2.64.7 Meter Table Status Supported Get Command . . . . . . . . . . . . .
2.2.64.8 Meter Table Status Supported Report Command . . . . . . . . . . . .
2.2.64.9 Meter Table Status Depth Get Command . . . . . . . . . . . . . . . .
2.2.64.10 Meter Table Status Date Get Command . . . . . . . . . . . . . . . . .
2.2.64.11 Meter Table Status Report Command . . . . . . . . . . . . . . . . . .
2.2.64.12 Meter Table Current Data Get Command . . . . . . . . . . . . . . . .
2.2.64.13 Meter Table Current Data Report Command . . . . . . . . . . . . . .
2.2.64.14 Meter Table Historical Data Get Command . . . . . . . . . . . . . . .
2.2.64.15 Meter Table Historical Data Report Command . . . . . . . . . . . . .
2.2.65 Meter Table Monitor Command Class, version 2 . . . . . . . . . . . . . . . . .
2.2.65.1 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.65.2 Meter Table Point Adm. Number Report Command . . . . . . . . . .
2.2.65.3 Meter Table ID Report Command . . . . . . . . . . . . . . . . . . . .
2.2.65.4 Meter Table Capability Report Command . . . . . . . . . . . . . . . .
2.2.65.5 Meter Table Current Data Report Command . . . . . . . . . . . . . .
2.2.65.6 Meter Table Historical Data Report Command . . . . . . . . . . . . .
2.2.66 Meter Table Monitor Command Class, version 3 . . . . . . . . . . . . . . . . .
2.2.66.1 Compatibility Considerations . . . . . . . . . . . . . . . . . . . . . . .
2.2.67 Meter Table Push Configuration Command Class, version 1 [OBSOLETED] . .
2.2.67.1 Meter Table Push Configuration Set Command . . . . . . . . . . . . .
2.2.67.2 Meter Table Push Configuration Get Command . . . . . . . . . . . .
2.2.67.3 Meter Table Push Configuration Report Command . . . . . . . . . .
2.2.68 Move to Position Window Covering Command Class, version 1 . . . . . . . . .
2.2.68.1 Move To Position Set Command . . . . . . . . . . . . . . . . . . . . .
2.2.68.2 Move To Position Get Command . . . . . . . . . . . . . . . . . . . . .

302
303
303
303
303
304
304
305
307
307
307
307
308
309
309
309
310
311
313
313
313
314
317
317
317
318
318
319
319
319
319
320
320
321
322
322
323
323
325
326
327
329
330
333
333
333
333
334
334
335
337
337
338
338
339
339
340
340
340

2.2.68.3 Move To Position Report Command . . . . . . . . . . . . . . . . . . . 341
2.2.69 Multilevel Sensor Command Class, version 1-4 . . . . . . . . . . . . . . . . . . 342
2.2.69.1 Multilevel Sensor Get Command . . . . . . . . . . . . . . . . . . . . . 342
2.2.69.2 Multilevel Sensor Report Command . . . . . . . . . . . . . . . . . . . 342
2.2.70 Multilevel Sensor Command Class, version 5-11 . . . . . . . . . . . . . . . . . . 344
2.2.70.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . . 344
2.2.70.1.1 Unknown Multilevel Sensor Types and Scales . . . . . . . . . 344
2.2.70.2 Multilevel Sensor Get Supported Sensor Command . . . . . . . . . . 345
2.2.70.3 Multilevel Sensor Supported Sensor Report Command . . . . . . . . . 345
2.2.70.4 Multilevel Sensor Get Supported Scale Command . . . . . . . . . . . 346
2.2.70.5 Multilevel Sensor Supported Scale Report Command . . . . . . . . . 346
2.2.70.6 Multilevel Sensor Get Command . . . . . . . . . . . . . . . . . . . . . 347
2.2.70.7 Multilevel Sensor Report Command . . . . . . . . . . . . . . . . . . . 347
2.2.70.7.1 Detailed description: Sensor Types for Movement and Rotation348
2.2.70.7.2 Sensor Type = Acceleration . . . . . . . . . . . . . . . . . . 351
2.2.70.7.3 Detailed description: Smoke Density . . . . . . . . . . . . . . 351
2.2.70.7.4 Detailed description: RF Signal Strength . . . . . . . . . . . 352
2.2.71 Multilevel Switch Command Class, version 1 . . . . . . . . . . . . . . . . . . . 353
2.2.71.1 Multilevel Switch Set Command . . . . . . . . . . . . . . . . . . . . . 353
2.2.71.2 Multilevel Switch Get Command . . . . . . . . . . . . . . . . . . . . . 353
2.2.71.3 Multilevel Switch Report Command . . . . . . . . . . . . . . . . . . . 354
2.2.71.4 Multilevel Switch Start Level Change Command . . . . . . . . . . . . 354
2.2.71.5 Multilevel Switch Stop Level Change Command . . . . . . . . . . . . 355
2.2.72 Multilevel Switch Command Class, version 2 . . . . . . . . . . . . . . . . . . . 356
2.2.72.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . . 356
2.2.72.2 Multilevel Switch Set Command . . . . . . . . . . . . . . . . . . . . . 356
2.2.72.3 Multilevel Switch Start Level Change Command . . . . . . . . . . . . 356
2.2.73 Multilevel Switch Command Class, version 3 . . . . . . . . . . . . . . . . . . . 358
2.2.73.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . . 358
2.2.73.2 Multilevel Switch Supported Get Command . . . . . . . . . . . . . . 358
2.2.73.3 Multilevel Switch Supported Report Command . . . . . . . . . . . . . 359
2.2.73.4 Multilevel Switch Start Level Change Command . . . . . . . . . . . . 360
2.2.74 Multilevel Switch Command Class, version 4 . . . . . . . . . . . . . . . . . . . 362
2.2.74.1 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . . 362
2.2.74.2 Multilevel Switch Report Command . . . . . . . . . . . . . . . . . . . 362
2.2.75 Multilevel Toggle Switch Command Class, version 1 . . . . . . . . . . . . . . . 363
2.2.75.1 Multilevel Toggle Switch Set Command . . . . . . . . . . . . . . . . . 363
2.2.75.2 Multilevel Toggle Switch Get Command . . . . . . . . . . . . . . . . . 363
2.2.75.3 Multilevel Toggle Switch Report Command . . . . . . . . . . . . . . . 363
2.2.75.4 Multilevel Toggle Switch Start Level Change Command . . . . . . . . 364
2.2.75.5 Multilevel Toggle Switch Stop Level Change Command . . . . . . . . 364
2.2.76 Notification Command Class, version 3-8 . . . . . . . . . . . . . . . . . . . . . 365
2.2.76.1 Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365
2.2.76.2 Compatibility considerations . . . . . . . . . . . . . . . . . . . . . . . 367
2.2.76.2.1 Notifications and Command Class version . . . . . . . . . . . 367
2.2.76.2.2 Push mode requirements . . . . . . . . . . . . . . . . . . . . 367
2.2.76.2.3 Pull mode requirements . . . . . . . . . . . . . . . . . . . . . 368
2.2.76.2.4 Multi Channel considerations . . . . . . . . . . . . . . . . . . 368
2.2.76.2.5 Multi Channel Push nodes . . . . . . . . . . . . . . . . . . . 368
2.2.76.2.6 State idle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 369
2.2.76.2.7 Version 3 [DEPRECATED] . . . . . . . . . . . . . . . . . . . 370
2.2.76.2.8 Version 4 [DEPRECATED] . . . . . . . . . . . . . . . . . . . 370
2.2.76.2.9 Version 5 [DEPRECATED] . . . . . . . . . . . . . . . . . . . 373
2.2.76.2.10 Version 6 [DEPRECATED] . . . . . . . . . . . . . . . . . . . 373
2.2.76.2.11 Version 7 [DEPRECATED] . . . . . . . . . . . . . . . . . . . 373
2.2.76.2.12 Version 8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374
2.2.76.3 Interoperability considerations . . . . . . . . . . . . . . . . . . . . . . 374
2.2.76.3.1 Push nodes Basic control . . . . . . . . . . . . . . . . . . . . 374
2.2.76.3.2 Event flood . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374

2.2.76.4 Notification Set Command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.76.5 Notification Get Command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.76.6 Notification Report Command . . . . . . . . . . . . . . . . . . . . . .
2.2.76.6.1 Event / State parameter encapsulation . . . . . . . . . . . .
2.2.76.7 Notification Supported Get Command . . . . . . . . . . . . . . . . . .
2.2.76.8 Notification Supported Report Command . . . . . . . . . . . . . . . .
2.2.76.9 Event Supported Get Command . . . . . . . . . . . . . . . . . . . . .
2.2.76.10 Event Supported Report Command . . . . . . . . . . . . . . . . . . .
2.2.77 Prepayment Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . .
2.2.77.1 Prepayment Balance Get Command . . . . . . . . . . . . . . . . . . .
2.2.77.2 Prepayment Balance Report Command . . . . . . . . . . . . . . . . .
2.2.77.3 Prepayment Supported Get Command . . . . . . . . . . . . . . . . .
2.2.77.4 Prepayment Supported Report Command . . . . . . . . . . . . . . . .
2.2.78 Prepayment Encapsulation Command Class, version 1 [NEVER CERTIFIED] .
2.2.78.1 Prepayment encapsulation command . . . . . . . . . . . . . . . . . . .
2.2.79 Proprietary Command Class, version 1 [OBSOLETED] . . . . . . . . . . . . .
2.2.79.1 Proprietary set command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.79.2 Proprietary get command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.79.3 Proprietary report command . . . . . . . . . . . . . . . . . . . . . . .
2.2.80 Protection Command Class, version 1 . . . . . . . . . . . . . . . . . . . . . . .
2.2.80.1 Protection Set Command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.80.2 Protection get command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.80.3 Protection report command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.81 Protection Command Class, version 2 . . . . . . . . . . . . . . . . . . . . . . .
2.2.81.1 Protection set command . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.81.2 Protection report command . . . . . . . . . . . . . . . . . . . . . . . .
2.2.81.3 Protection supported get command . . . . . . . . . . . . . . . . . . .
2.2.81.4 Protection supported report command . . . . . . . . . . . . . . . . . .
2.2.81.5 Protection exclusive control . . . . . . . . . . . . . . . . . . . . . . . .
2.2.81.5.1 Protection exclusive control set command . . . . . . . . . . .
2.2.81.5.2 Protection exclusive control get command . . . . . . . . . . .
2.2.81.5.3 Protection exclusive control report command . . . . . . . . .
2.2.81.6 Protection timeout . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.2.81.6.1 Protection timeout set command . . . . . . . . . . . . . . . .
2.2.81.6.2 Protection timeout get command . . . . . . . . . . . . . . . .
2.2.81.6.3 Protection timeout report 

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

**Last Updated**: 2026-03-07T20:11:54.843392
