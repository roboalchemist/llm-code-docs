_**Release**_ _**2.9.0**_

## **Z-Wave Alliance**


**Aug** **20,** **2025**

## Table of Contents


1 Introduction 9
1.1 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.2 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.3 Audience and Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.4 Terms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.5 Terminology And Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


2 Overview 10


3 Interface communication 11
3.1 Table Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2 Frame types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2.1 Data Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.2.2 ACK Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2.3 NAK Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.2.4 CAN Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.3 Command frame flows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.3.1 Unacknowledged frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.3.2 Acknowledged frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.3.3 Acknowledged frame with response . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3.4 Acknowledged frame with callback . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3.5 Acknowledged frame with response and callback . . . . . . . . . . . . . . . . . 16
3.3.6 Unsolicited frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4 Error handling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.4.1 Retransmission timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.4.2 Missing Acknowledgment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.4.3 Collision . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.4.4 Frame reception timeout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.4.5 Invalid frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19


4 Z-Wave API Commands 20
4.1 Command format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.2 Generic command elements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21


4.2.1 Session identifier (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.2.2 Rx Status (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.2.3 Tx Status (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.2.4 RSSI Measurements (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.2.5 Response status (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.2.6 Command Status (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.2.7 Basic Device Class (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.2.8 Tx Options (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.2.9 RF Region (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.2.10 Tx Status Report (N bytes) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2.11 Route Speed (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.2.12 Repeater (4 bytes) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.3 Z-Wave Capability API commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.3.1 Get Init Data Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.3.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.3.1.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 32
4.3.1.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 32
4.3.1.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 34
4.3.2 Set Application Node Information Command . . . . . . . . . . . . . . . . . . . 35
4.3.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.3.2.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 35
4.3.2.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 36
4.3.2.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 36
4.3.3 Set Application Node Information Command Classes Command . . . . . . . . 37
4.3.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
4.3.3.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 37
4.3.3.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 38
4.3.3.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 38
4.3.4 Get Controller Capabilities Command . . . . . . . . . . . . . . . . . . . . . . . 39
4.3.4.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.3.4.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 39
4.3.4.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 39
4.3.4.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 40
4.3.5 Get Capabilities Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.3.5.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.3.5.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 41
4.3.5.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 41
4.3.5.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 42
4.3.6 Get Long Range Nodes Command . . . . . . . . . . . . . . . . . . . . . . . . . 43
4.3.6.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
4.3.6.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 44
4.3.6.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 44
4.3.6.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 45
4.3.7 Get Z-Wave Long Range Channel Command . . . . . . . . . . . . . . . . . . . 46
4.3.7.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.3.7.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 46
4.3.7.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 46
4.3.7.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 47
4.3.8 Set Z-Wave Long Range Channel Command . . . . . . . . . . . . . . . . . . . . 48
4.3.8.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
4.3.8.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 48
4.3.8.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 48
4.3.8.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 49
4.3.9 Get NLS Nodes Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
4.3.9.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
4.3.9.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 50
4.3.9.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 51
4.3.9.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 52
4.3.10 Get Protocol Version Command . . . . . . . . . . . . . . . . . . . . . . . . . . 53


4.3.10.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3.10.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 53
4.3.10.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 53
4.3.10.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 54
4.3.11 Get Library Version Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.3.11.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.3.11.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 55
4.3.11.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 55
4.3.11.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 56
4.3.12 Get Library Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.3.12.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.3.12.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 57
4.3.12.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 57
4.3.12.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 57
4.3.13 Soft Reset Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.3.13.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.3.13.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 58
4.3.13.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 58
4.3.13.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 58
4.3.14 Set Default Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.3.14.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.3.14.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 59
4.3.14.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 59
4.3.14.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 59
4.3.15 Setup Z-Wave API Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.3.15.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.3.15.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 60
4.3.15.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 60
4.3.15.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 61
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
4.3.17.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 98
4.3.17.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 98
4.3.17.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 99
4.4 Z-Wave API Network Management Commands . . . . . . . . . . . . . . . . . . . . . . 100
4.4.1 Common Network Management Commands . . . . . . . . . . . . . . . . . . . . 101
4.4.1.1 Send NOP Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
4.4.1.2 Get Node Information Protocol Data Command . . . . . . . . . . . . 104
4.4.1.3 Send Node Information Command . . . . . . . . . . . . . . . . . . . . 106
4.4.1.4 Request Node Information Command . . . . . . . . . . . . . . . . . . 108


4.4.1.5 Set Learn Mode Command . . . . . . . . . . . . . . . . . . . . . . . . 111
4.4.1.6 Get SUC NodeID Command . . . . . . . . . . . . . . . . . . . . . . . 115
4.4.1.7 Set SmartStart Inclusion Request Maximum Interval Command . . . 116
4.4.1.8 Explore Request Inclusion Command . . . . . . . . . . . . . . . . . . 117
4.4.1.9 Explore Request Exclusion Command . . . . . . . . . . . . . . . . . . 120
4.4.2 End Nodes Network Management . . . . . . . . . . . . . . . . . . . . . . . . . . 123
4.4.2.1 Request New Route Destinations Command . . . . . . . . . . . . . . 124
4.4.2.2 Is Node Within Direct Range Command . . . . . . . . . . . . . . . . 127
4.4.2.3 Get Network Statistics Command . . . . . . . . . . . . . . . . . . . . 129
4.4.2.4 Clear Network Statistics Command . . . . . . . . . . . . . . . . . . . 131
4.4.3 Controller Nodes Network Management . . . . . . . . . . . . . . . . . . . . . . 132
4.4.3.1 Add Node To Network Command . . . . . . . . . . . . . . . . . . . . 133
4.4.3.2 Add Controller And Assign Primary Controller Role Command . . . 146
4.4.3.3 Add Primary Controller Command . . . . . . . . . . . . . . . . . . . 148
4.4.3.4 Remove Node From Network Command . . . . . . . . . . . . . . . . . 150
4.4.3.5 Remove Specific Node From Network Command . . . . . . . . . . . . 155
4.4.3.6 Is Node Failed Command . . . . . . . . . . . . . . . . . . . . . . . . . 157
4.4.3.7 Remove Failed Node Command . . . . . . . . . . . . . . . . . . . . . 159
4.4.3.8 Replace Failed Node Command . . . . . . . . . . . . . . . . . . . . . 161
4.4.3.9 Delete Return Route Command . . . . . . . . . . . . . . . . . . . . . 165
4.4.3.10 Assign Return Route Command . . . . . . . . . . . . . . . . . . . . . 167
4.4.3.11 Assign SUC Return Route Command . . . . . . . . . . . . . . . . . . 169
4.4.3.12 Assign Priority Return Route Command . . . . . . . . . . . . . . . . 171
4.4.3.13 Assign Priority SUC Return Route Command . . . . . . . . . . . . . 173
4.4.3.14 Set Priority Route Command . . . . . . . . . . . . . . . . . . . . . . . 175
4.4.3.15 Get Priority Route Command . . . . . . . . . . . . . . . . . . . . . . 177
4.4.3.16 Get Neighbor Table Line Command . . . . . . . . . . . . . . . . . . . 179
4.4.3.17 Lock Unlock Last Route Command . . . . . . . . . . . . . . . . . . . 181
4.4.3.18 Get Routing Table Entries Command . . . . . . . . . . . . . . . . . . 182
4.4.3.19 Set SUC NodeID Command . . . . . . . . . . . . . . . . . . . . . . . 184
4.4.3.20 Delete SUC Return Route Command . . . . . . . . . . . . . . . . . . 186
4.4.3.21 Send SUC NodeID Command . . . . . . . . . . . . . . . . . . . . . . 188
4.4.3.22 Enable Node NLS command . . . . . . . . . . . . . . . . . . . . . . . 190
4.4.3.23 Get Node NLS State command . . . . . . . . . . . . . . . . . . . . . . 191
4.4.3.24 Request Node Neighbor Discovery Command . . . . . . . . . . . . . . 193
4.4.3.25 Request Node Type Neighbor Update Command . . . . . . . . . . . . 196
4.4.3.26 Request Network Update Command . . . . . . . . . . . . . . . . . . . 199
4.4.3.27 Set Virtual Node To Learn Mode Command . . . . . . . . . . . . . . 202
4.4.3.28 Virtual Node Send Node Information Command . . . . . . . . . . . . 205
4.4.3.29 Set Virtual Nodes Application Node Information Command . . . . . . 207
4.4.3.30 Set Z-Wave Long Range Shadow NodeIDs Commmand . . . . . . . . 209
4.4.3.31 Transfer Protocol Command Class command . . . . . . . . . . . . . . 210
4.5 Z-Wave API Memory Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
4.5.1 Get Network IDs from Memory Command . . . . . . . . . . . . . . . . . . . . . 214
4.5.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
4.5.1.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 214
4.5.1.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 214
4.5.1.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 214
4.6 Z-Wave API Firmware Update Commands . . . . . . . . . . . . . . . . . . . . . . . . . 215
4.6.1 Firmware Update Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
4.6.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
4.6.1.2 Sub Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
4.6.1.3 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 217
4.6.1.4 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 217
4.6.1.5 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 218
4.6.1.6 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 219
4.6.1.7 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 220
4.6.1.8 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 220
4.6.1.9 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 220


4.6.1.10 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 221
4.7 Z-Wave API Backup and Restore Commands . . . . . . . . . . . . . . . . . . . . . . . 221
4.7.1 Network Restore Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
4.7.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
4.7.1.2 Sub Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
4.7.1.3 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 224
4.7.1.4 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 224
4.7.1.5 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 225
4.7.1.6 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 225
4.7.1.7 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 226
4.7.1.8 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 226
4.7.1.9 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 226
4.7.1.10 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 227
4.7.1.11 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 227
4.7.1.12 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 227
4.7.1.13 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 228
4.7.1.14 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 228
4.7.1.15 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 228
4.7.1.16 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 229
4.7.1.17 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 229
4.7.1.18 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 229
4.7.1.19 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 230
4.7.1.20 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 230
4.7.2 NVM Operations Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
4.7.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 231
4.7.2.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 234
4.7.2.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 235
4.7.2.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 236
4.7.3 Extended NVM Operations Command . . . . . . . . . . . . . . . . . . . . . . . 237
4.7.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 237
4.7.3.2 Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . . 239
4.7.3.3 Response data frame (Z-Wave Module →host) . . . . . . . . . . . . . 240
4.7.3.4 Callback data frame (Z-Wave Module →host) . . . . . . . . . . . . . 241
4.8 Unsolicited Z-Wave API commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 242
4.8.1 Application Command Handler Command . . . . . . . . . . . . . . . . . . . . . 243
4.8.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
4.8.1.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 243
4.8.1.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 243
4.8.1.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 243
4.8.1.5 4. Unsolicited frame (Z-Wave Module →host) . . . . . . . . . . . . . 243
4.8.2 Z-Wave API Started Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
4.8.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
4.8.2.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 245
4.8.2.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 245
4.8.2.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 245
4.8.2.5 4. Unsolicited frame (Z-Wave Module →host) . . . . . . . . . . . . . 245
4.8.3 Application Update Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
4.8.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
4.8.3.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 248
4.8.3.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 248
4.8.3.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 248
4.8.3.5 4. Unsolicited frame (Z-Wave Module →host) . . . . . . . . . . . . . 248
4.8.4 Promiscuous Application Command Handler Command . . . . . . . . . . . . . 253
4.8.5 Bridge Application Command Handler Command . . . . . . . . . . . . . . . . . 254
4.8.5.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
4.8.5.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 254
4.8.5.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 254
4.8.5.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 254
4.8.5.5 4. Unsolicited frame (Z-Wave Module →host) . . . . . . . . . . . . . 254


4.8.6 Nonce Update Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
4.8.6.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
4.8.6.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 256
4.8.6.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 256
4.8.6.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 256
4.8.6.5 4. Unsolicited frame (Z-Wave Module →host) . . . . . . . . . . . . . 256
4.9 Z-Wave API Miscellaneous Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . 258
4.9.1 Clear Tx Timers Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
4.9.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
4.9.1.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 259
4.9.1.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 259
4.9.1.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 259
4.9.2 Get Background RSSI Command . . . . . . . . . . . . . . . . . . . . . . . . . . 260
4.9.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
4.9.2.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 260
4.9.2.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 260
4.9.2.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 260
4.9.3 Get Tx Timer Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
4.9.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
4.9.3.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 261
4.9.3.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 261
4.9.3.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 262
4.9.4 Get Virtual Nodes Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
4.9.4.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
4.9.4.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 263
4.9.4.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 263
4.9.4.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 263
4.9.5 Get Z-Wave Module Protocol Status Command . . . . . . . . . . . . . . . . . . 264
4.9.5.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264
4.9.5.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 264
4.9.5.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 264
4.9.5.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 265
4.9.6 Is Virtual Node Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
4.9.6.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 266
4.9.6.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 266
4.9.6.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 266
4.9.6.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 266
4.9.7 Set Listen Before Talk Threshold Command . . . . . . . . . . . . . . . . . . . . 267
4.9.7.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
4.9.7.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 267
4.9.7.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 267
4.9.7.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 268
4.9.8 Set RF Receive Mode Command . . . . . . . . . . . . . . . . . . . . . . . . . . 269
4.9.8.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269
4.9.8.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 269
4.9.8.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 269
4.9.8.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 270
4.9.9 Set RF Power Level Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
4.9.9.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
4.9.9.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 271
4.9.9.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 271
4.9.9.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 272
4.9.10 Set Maximum Routing Attempts Command . . . . . . . . . . . . . . . . . . . . 273
4.9.10.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
4.9.10.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 273
4.9.10.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 273
4.9.10.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 273
4.9.11 Set RF Power Level Rediscovery Command . . . . . . . . . . . . . . . . . . . . 274
4.9.11.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274


4.9.11.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 274
4.9.11.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 274
4.9.11.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 274
4.9.12 Start Watchdog Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
4.9.12.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
4.9.12.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 275
4.9.12.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 275
4.9.12.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 275
4.9.13 Stop Watchdog Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
4.9.13.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 276
4.9.13.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 276
4.9.13.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 276
4.9.13.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 276
4.9.14 Set Timeouts Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
4.9.14.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
4.9.14.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 277
4.9.14.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 277
4.9.14.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 278
4.9.15 Power Management Stay Awake Command . . . . . . . . . . . . . . . . . . . . 279
4.9.15.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
4.9.15.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 279
4.9.16 Power Management Cancel Command . . . . . . . . . . . . . . . . . . . . . . . 280
4.9.16.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
4.9.16.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 280
4.9.17 Initiate Shutdown Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
4.9.17.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
4.9.17.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 281
4.9.17.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 281
4.9.17.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 281
4.9.18 Radio Debug Get Protocol List Command . . . . . . . . . . . . . . . . . . . . . 282
4.9.18.1 Radio Debug Version Identification . . . . . . . . . . . . . . . . . . . 282
4.9.18.2 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
4.9.18.3 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 282
4.9.18.4 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 282
4.9.18.5 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 283
4.9.19 Radio Debug Enable Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
4.9.19.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
4.9.19.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 284
4.9.19.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 285
4.9.19.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 285
4.9.20 Radio Debug Status Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
4.9.20.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
4.9.20.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 286
4.9.20.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 286
4.9.20.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 287
4.9.21 Nonce Generation on Z-Wave Module Set Mode Command . . . . . . . . . . . 288
4.9.21.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
4.9.21.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 288
4.9.21.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 288
4.9.21.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 289
4.10 Z-Wave API Transport Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
4.10.1 Controller Node Send Data Command . . . . . . . . . . . . . . . . . . . . . . . 291
4.10.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
4.10.1.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 291
4.10.1.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 292
4.10.1.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 292
4.10.2 Controller Node Send Data Multicast Command . . . . . . . . . . . . . . . . . 293
4.10.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293
4.10.2.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 293


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


4.10.2.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 294
4.10.2.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 294
4.10.3 End Node Send Data Command . . . . . . . . . . . . . . . . . . . . . . . . . . 295
4.10.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
4.10.3.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 295
4.10.3.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 296
4.10.3.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 297
4.10.4 End Node Send Data Multicast Command . . . . . . . . . . . . . . . . . . . . . 298
4.10.4.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298
4.10.4.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 298
4.10.4.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 299
4.10.4.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 299
4.10.5 Bridge Controller Node Send Data Command . . . . . . . . . . . . . . . . . . . 300
4.10.5.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 300
4.10.5.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 300
4.10.5.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 301
4.10.5.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 301
4.10.6 Bridge Controller Node Send Data Multicast Command . . . . . . . . . . . . . 302
4.10.6.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
4.10.6.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 302
4.10.6.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 303
4.10.6.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 303
4.10.7 Send Data Abort Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
4.10.7.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304
4.10.7.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 305
4.10.7.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 305
4.10.7.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 305
4.10.8 Send Test Frame Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
4.10.8.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306
4.10.8.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 306
4.10.8.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 306
4.10.8.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 307
4.10.9 Controller Node Send Protocol Data Command . . . . . . . . . . . . . . . . . . 308
4.10.9.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 308
4.10.9.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 308
4.10.9.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 309
4.10.9.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 309
4.11 Z-Wave API Security Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 310
4.11.1 Security Setup Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
4.11.1.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311
4.11.1.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 311
4.11.1.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 312
4.11.1.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 314
4.11.2 Encrypt Data With AES Command . . . . . . . . . . . . . . . . . . . . . . . . 315
4.11.2.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
4.11.2.2 1. Initial data frame (host →Z-Wave Module) . . . . . . . . . . . . . 315
4.11.2.3 2. Response data frame (Z-Wave Module →host) . . . . . . . . . . . 315
4.11.2.4 3. Callback data frame (Z-Wave Module →host) . . . . . . . . . . . 316
4.11.3 Request Protocol Command Class Encryption command . . . . . . . . . . . . . 317
4.11.3.1 Frame flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
4.11.3.2 1. Initial data frame (Z-Wave Module →host) . . . . . . . . . . . . . 318
4.11.3.3 2. Response data frame (host →Z-Wave Module) . . . . . . . . . . . 319
4.11.3.4 3. Callback data frame (host →Z-Wave Module) . . . . . . . . . . . 319
4.12 Proprietary Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 319


References 320


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 8


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 1 Introduction 1.1 Disclaimer


THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.

## 1.2 Purpose


This document specifies the communication and commands used by host processors to interface with
a module supporting a Z-Wave API.

## 1.3 Audience and Requirements


The audience of this document is the Z-Wave Alliance members and Z-Wave developers.

## 1.4 Terms


This document describes mandatory and optional aspects of the required compliance of a Z-Wave
product to the Z-Wave standard.

[The guidelines outlined in RFC 2119 with respect to key words used to indicate requirement levels are](https://datatracker.ietf.org/doc/html/rfc2119.html)
followed. Essentially, the key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL
NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this
document are to be interpreted as described in RFC 2119.

## 1.5 Terminology And Abbreviations


Terminology and abbreviations used in this document are listed in Table 1.1


Table 1.1: Terminology and abbreviations


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 9


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 2 Overview


The Z-Wave Applications Programming Interface (Z-Wave API) allows a host interface to communicate with a Z-Wave chip through any kind of physical interface.

The host may be PC or a less powerful embedded host CPU, e.g., in a remote control or in a gateway
device. Depending on the chip family, the Z-Wave API is typically accessed via RS-232 or USB
physical interfaces.

Here are some of the applications leveraging the Z-Wave API:

 - Gateway Application

 - PC Controller

 - Conformance Testing Tool (CTT)

In this specification, we will refer to:

 - The host application: It is the application making use of the Z-Wave API via the physical
interface.

 - The Z-Wave API Module: It is the Z-Wave API implementation providing an API to make use
of its Z-Wave capabilities.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 10


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 3 Interface communication


This chapter defines the frames and communications frame flows between a Z-Wave API supporting
module and a host application. Several frames types are defined to enable session-like communication.

## 3.1 Table Syntax


The data and command format tables contains a column with byte/bit numbering. This column
specifies what byte offset the shown field is in the complete data frame. In some cases this is not a
fixed number and special systax notations are used.


Table 3.1: Table Syntax

## 3.2 Frame types


**3.2.1** **Data** **Frame**


The Data frame is used to transmit a command. It can be used it both directions (Z-Wave module
to host, or host to Z-Wave module). All data frames MUST be formatted according to Table 3.2.


Table 3.2: Data frame format


Frame Type (8 bits)

This field is used to detect the type of frame being transmitted. For a data frame, this field MUST
be set to 0x01, indicating a Start of Frame (SOF).

Length (8 bits)

The Length field is used to indicate the total length, in bytes, of the following fields:

 - Length (this field)

 - Type

 - Z-Wave API Command ID

 - Z-Wave API Command Payload

The following fields MUST NOT be included in the length calculation:

 - Start of frame


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 11


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


 - Checksum

Type (8 bits)

The Type field is used to indicate the type of Command being sent in the data frame. It MUST be
encoded according to Table 3.3.


Table 3.3: Data frame format             - Type encoding


Z-Wave API Command ID (8 bits)

This field is used to advertise a command identifier that enable a receiving interface to parse the
payload. Commands are described in section _Z-Wave_ _API_ _Commands_ .

Z-Wave API Command Payload (L bytes)

This field is used to indicate the payload associated with the Z-Wave API command. The payload for
each command is described in the _Z-Wave_ _API_ _Commands_ section.

Checksum (8 bits)

The Checksum field is used to validate the data received in the Data Frame. The Checksum calculation
MUST include the following fields:

 - Length

 - Type

 - Z-Wave API Command ID

 - Z-Wave API Command Payload

The Checksum field MUST be calculated using XOR operations: Checksum = 0xFF (XOR) Length
(XOR) Type (XOR) Z-Wave API Command ID (XOR) Z-Wave API Command Payload 1 (XOR) …
(XOR) Z-Wave API Command Payload N

An interface receiving a non-matching checksum MUST return a _NAK_ _Frame_ . An interface receiving
a matching checksum MUST return an _ACK_ _Frame_ .


**3.2.2** **ACK** **Frame**


The ACK frame is used to indicate the successful reception of a _Data_ _Frame_ . It MUST be formatted
according to Table 3.4.


Table 3.4: ACK frame format


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 12


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.2.3** **NAK** **Frame**


The NAK frame is used to indicate an error in the reception of a _Data_ _Frame_ . It MUST be formatted
according to Table 3.5.


Table 3.5: NAK frame format


**3.2.4** **CAN** **Frame**


The CAN frame is used to indicate the detection of a collision during _Data_ _Frame_ transmissions.

A CAN frame is most often returned when the UART is both transmitting and receiving at the same
time (a collision). This results in the receiving end receiving a frame it did not expect and thus it
drops the frame and returns a CAN. The transmitting end typically is also receiving a frame which
it must process and ACK and then retransmit the frame that was returned with a CAN after an
appropriate backoff interval.

It MUST be formatted according to Table 3.6.


Table 3.6: CAN frame format

## 3.3 Command frame flows


The Z-Wave API has several possible command frame flows:

 - _Unacknowledged_ _frame_

 - _Acknowledged_ _frame_

 - _Acknowledged_ _frame_ _with_ _response_

 - _Acknowledged_ _frame_ _with_ _callback_

 - _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_

 - _Unsolicited_ _frame_

In the following subsections and the rest of this specification, the frames are numbered as follow:

1. initial data frame: it is the initial (request type) data frame from the host to the Z-Wave module.

2. response data frame: it is a response type data frame returned to an initial data frame from the
Z-Wave module to the host.

3. callback data frame: it is a request type data frame sent from the Z-Wave module to the host, after
it has completed an action triggered by an initial data frame.

4. unsolicited data frame: it is a request type data frame sent from the Z-Wave module to the host.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 13


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.3.1** **Unacknowledged** **frame**


There MAY be data frames that will not be acknowledged by the destination because of hardware
or software restrictions. It can for example happen if the command instructs the Z-Wave module to
enter reprogramming mode or go offline.

The communication flow MUST be as shown in Figure 3.1


Figure 3.1: Unacknowledged frame


If a command is supposed to trigger an unacknowledged frame transmission, the host MUST NOT try
to retransmit the command if no ACK frame is received. The host MUST retransmit the command
if a _NAK_ _Frame_ or a _CAN_ _Frame_ is received.


**3.3.2** **Acknowledged** **frame**


Acknowledged frames are frames that will not trigger any communication back from the Z-Wave
module, apart from an _ACK_ _Frame_ . The communication flow MUST be as shown in Figure 3.2


Figure 3.2: Acknowledged frame


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 14


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.3.3** **Acknowledged** **frame** **with** **response**


Acknowledged frames with response are acknowledged frames that will trigger an immediate response
from the Z-Wave module. The communication flow MUST be as shown in Figure 3.3


Figure 3.3: Acknowledged frame with response


**3.3.4** **Acknowledged** **frame** **with** **callback**


Acknowledged frames with callback are acknowledged frames that will trigger a callback after an
operation has been performed by the Z-Wave module. The communication flow MUST be as shown
in Figure 3.4


Figure 3.4: Acknowledged frame with callback


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 15


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


In some cases, an Initial Data Frame MAY trigger several callback frames.


**3.3.5** **Acknowledged** **frame** **with** **response** **and** **callback**


Acknowledged frames with response and callback are acknowledged frames that will trigger both an
immediate response and an additional callback after an operation has been performed by the Z-Wave
module. The communication flow MUST be as shown in Figure 3.5


Figure 3.5: Acknowledged frame with response and callback


In some cases, an Initial Data Frame MAY trigger several callback frames.


**3.3.6** **Unsolicited** **frame**


Unsolicited frames are frames that are sent from the Z-Wave module to inform the host application
that an event happened. The communication flow MUST be as shown in Figure 3.6


Figure 3.6: Unsolicited frame


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 16


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 3.4 Error handling


The following subsections show how to handle communications issues between the Z-Wave Module
and the host application.


**3.4.1** **Retransmission** **timing**


In general, retransmissions of a _Data_ _Frame_ MUST apply back-off timers.

The minimum back-off in milliseconds MUST be calculated according to (3.1)


_𝑇𝑛_ = 100 + _𝑛_ _×_ 1000 _._ (3.1)


where:

 - n is the retransmission number  - 1. i.e. n=0 for the first retransmission.

A sending interface SHOULD add an additional random delay to the minimum back-off.


**3.4.2** **Missing** **Acknowledgment**


By default, all data frames MUST be acknowledged by the receiving interface. Acknowledgement
consists in sending an _ACK_ _Frame_ .

A sending interface MUST wait for 1600ms or more for an _ACK_ _Frame_ after transmitting a _Data_
_Frame_ .

In case of missing acknowledgement 1600 ms after a transmission, a transmitting interface SHOULD
retransmit the unacknowledged data frame.

This recommendation MAY be adjusted based on the physical medium used for communication between the two interfaces.

A transmitting interface SHOULD make 3 retransmissions attempts. This is shown in Figure 3.7.


Figure 3.7: Missing acknowledgment frame


In the unlikely event that the Z-Wave Module has been unresponsive for more than 4 seconds (or 3
consecutive _Data_ _Frame_ transmission attempts), it is RECOMMENDED to issue a hard reset to the
Z-Wave Module. If a hard reset is not available, a _Soft_ _Reset_ _Command_ SHOULD be issued.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 17


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.4.3** **Collision**


If the Z-Wave API module receives a _Data_ _Frame_ while it is waiting for an _ACK_ _Frame_, it MUST
return a _CAN_ _Frame_ .

A host application SHOULD NOT issue any _CAN_ _Frame_, even if it detects a collision. A host
application SHOULD initiate a back-off for its own frame, if it was not acknowledged.

When a collision occurs, the Z-Wave API Module SHOULD have priority for retransmission.

Examples are provided in Figure 3.8 and Figure 3.9


Figure 3.8: Collision detected by the host (example)


Figure 3.9: CAN frame from the Z-Wave API Module (example)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 18


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.4.4** **Frame** **reception** **timeout**


A receiving interface MUST abort an ongoing reception of a _Data_ _Frame_ if the reception has lasted
for more than 1500ms after the reception of the SOF byte.

When aborting the reception of a _Data_ _Frame_, an interface MUST NOT issue a _NAK_ _Frame_ .


**3.4.5** **Invalid** **frame**


A receiving interface receiving a _Data Frame_ with a _Checksum_ mismatch MUST return a _NAK Frame_ .

This is illustrated in Figure 3.10


Figure 3.10: Invalid frame


If more than 3 consecutive transmission result in checksum errors, it is RECOMMENDED to issue a
hard reset to the Z-Wave Module. If a hard reset is not available, a _Soft_ _Reset_ _Command_ SHOULD
be issued.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 19


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4 Z-Wave API Commands


This section lists all defined Z-Wave API commands. Note that all commands are not always supported
by a Z-Wave API Module.

The _Command_ _format_ details common features and fields shared among several commands.

The subsequent sections are grouping the Z-Wave API Commands in categories.

 - _Z-Wave_ _Capability_ _API_ _commands_ :

This subsection groups all the Z-Wave API commands to read the Z-Wave API Module capabilities and perform initialization and setup.

 - _Z-Wave_ _API_ _Network_ _Management_ _Commands_ :

This subsection groups all the Z-Wave API commands allowing to perform Network Management
operations. Most of these operations are defined in [zwave_nwk_spec] for details. It is split
into 3 subsubsections:

    - Commands available for all nodes: _Common_ _Network_ _Management_ _Commands_

    - Commands for controller nodes only: _Controller_ _Nodes_ _Network_ _Management_

    - Commands for end nodes only: _End_ _Nodes_ _Network_ _Management_

 - _Z-Wave_ _API_ _Transport_ _Commands_ :

This subsection groups all the Z-Wave API commands that can be used to transmit application
payloads.

 - _Z-Wave_ _API_ _Firmware_ _Update_ _Commands_ :

This subsection groups all the Z-Wave API commands that can be used to read and write the
firmware of the Z-Wave API module.

 - _Z-Wave_ _API_ _Security_ _Commands_ :

This subsection groups all the Z-Wave API commands related to security functionalities provided
by the Z-Wave API Module.

 - _Z-Wave_ _API_ _Memory_ _Commands_ :

This subsection groups all the Z-Wave API commands that can be used to read data that has
been saved by the Z-Wave API Module in its persistent memory.

 - _Unsolicited_ _Z-Wave_ _API_ _commands_ :

This subsection groups all the Z-Wave API commands that are sent as unsolicited frames (refer
to _Data_ _Frame_ and _Unsolicited_ _frame_ ) by the Z-Wave API Module.

 - _Z-Wave_ _API_ _Miscellaneous_ _Commands_ :

This subsection groups all the Z-Wave API commands that do not fit in any of the other
categories.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 20


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.1 Command format


In the following _Z-Wave API Commands_ section, each command description uses a _Data Frame_, where
only the _Z-Wave_ _API_ _Command_ _ID_ and _Z-Wave_ _API_ _Command_ _Payload_ fields are shown.

## 4.2 Generic command elements


**4.2.1** **Session** **identifier** **(8** **bits)**


Some commands contain a Session Identifier. This is a 1 byte value provided by the host application
for any given command that must be used by the Z-Wave module in callback commands triggered by
the initial data frame.

This Session Identifier can be used by a host application to track which command triggered the
incoming callbacks or to identify associated application user data. (e.g. the host needs to retrieve
data or perform actions associated to the initial command.)

When the Session Identifier is zero, the Z-Wave module SHOULD NOT return a callback.


**4.2.2** **Rx** **Status** **(8** **bits)**


The Rx Status field is used to indicate how a Z-Wave frame was received. This field MUST be encoded
according to Table 4.1


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 21


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.1: Rx Status Value encoding



























© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 22


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.2.3** **Tx** **Status** **(8** **bits)**


This field is used to advertise the outcome of a Z-Wave radio transmission attempt. This field MUST
be encoded according to Table 4.2


Table 4.2: Tx Status Value encoding


**4.2.4** **RSSI** **Measurements** **(8** **bits)**


All RSSI measurements MUST use signed representation and MUST be encoded according to Table
4.3


Table 4.3: RSSI value encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 23


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.2.5** **Response** **status** **(8** **bits)**


Some commands Response data frame contain Response status. It is a 1 byte field value that is used
indicate if the requested operation in the Initial Data Frame has been accepted and the Callback Data
Frame is expected or not. This field MUST be encoded as follow:

 - If this field is encoded to 0x00 and the Session Identifier is zero, the Z-Wave Module MUST not
send Callback data Frame to the host.

 - If this field is encoded different from 0x00 and the the Session Identifier is not zero, the Z-Wave
Module MUST send Callback data Frame to the host.


**4.2.6** **Command** **Status** **(8** **bits)**


When a Z-Wave API Module receives a command, it sometimes provides the execution status of the
commands using a _Command_ _Status_ field in the Response data frame.

The _Command_ _Status_ field MUST be encoded as follow:

 - The value 0x00 MUST indicate that the command was not accepted or an error occurred while
applying it.

 - The value 0x01 MUST indicate that the command was successfully executed.

 - Values in the range 0x02..0xFF MUST also be interpreted as a successful command execution.


**4.2.7** **Basic** **Device** **Class** **(8** **bits)**


Some commands contain Basic Device Class field which is used to identify the Z-Wave library used by
the application for a given device (Refer to [device_type_spec_v2]), and such field MUST be encoded
according to Table 4.4.


Table 4.4: Basic Device Class value encoding


**4.2.8** **Tx** **Options** **(8** **bits)**


This field is used to indicate the transmission options for sending Z-Wave frames.

This field MUST be treated as a bit mask and encoded according to Table 4.5


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 24


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.5: Tx Options encoding


**4.2.9** **RF** **Region** **(8** **bits)**


This field is used to indicate the Z-Wave RF Region, defining the number of channels and center
frequency on which the Z-Wave API Module operates.

This field MUST be encoded according to Table 4.6


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 25


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.6: RF Region encoding











**4.2.10** **Tx** **Status** **Report** **(N** **bytes)**


When a Z-Wave transmission has been completed, the Z-Wave API Module can issue a _Tx_ _Status_
_Report_ providing details about the transmission that was carried out.

The _Tx_ _Status_ _Report_ is a variable length field that has grown through the revisions of the Z-Wave
API. A host application MUST be resistant to unexpected length of this field (both shorter and
longer).

The _Tx_ _Status_ _Report_ field MUST be formatted according to Table 4.7


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 26


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.7: Tx Status Report field structure


Not all values can be expected to be valid when a tranmsit fails, e.g. all fields related to acknowledge
can not be expected to be valid when Tx Status is TRANSMIT_COMPLETE_NO_ACK

Transmit Ticks (16 bits)

This field is used to indicate the transmission time in multiples of 10ms. For example, the value 30
MUST indicate that the transmission took 300ms.

Number of repeaters (8 bits)

This field is used to indicate the number of repeaters used in the route to the destination.

The value 0 MUST indicate direct range communication. Values in the range 1..255 MUST indicate
the number of repeaters used to reached the destination.

ACK RSSI (8 bits)

This field is used to indicate ythe RSSI value of the acknowledgement frame. This field MUST be
encoded according to _RSSI_ _Measurements_ _(8_ _bits)_ and Table 4.3.

Measured incoming RSSI for Repeater 0 (8 bits)

This field is used to indicate the RSSI value measured from Repeater 0 for the incoming Acknowledgement frame. This field MUST be encoded according to _RSSI_ _Measurements_ _(8_ _bits)_ and Table
4.3.

Measured incoming RSSI for Repeater 1 (8 bits)

This field is used to indicate the RSSI value measured from Repeater 1 for the incoming Acknowledgement frame. This field MUST be encoded according to _RSSI_ _Measurements_ _(8_ _bits)_ and Table
4.3.

Measured incoming RSSI for Repeater 2 (8 bits)

This field is used to indicate the RSSI value measured from Repeater 2 for the incoming Acknowledgement frame. This field MUST be encoded according to _RSSI_ _Measurements_ _(8_ _bits)_ and Table
4.3.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 27


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Measured incoming RSSI for Repeater 3 (8 bits)

This field is used to indicate the RSSI value measured from Repeater 3 for the incoming Acknowledgement frame. This field MUST be encoded according to _RSSI_ _Measurements_ _(8_ _bits)_ and Table
4.3.

ACK Channel No (8 bits)

This field is used to indicate the channel number where the ACK received from.

Tx Channel No (8 bits)

This field is used to indicate the channel number that is used to transmit the data.

Route Scheme State (8 bits)

This field is used to indicate the state of the route resolution for the transmission attempt.

The encoding of this field is implementation specific. Refer to individual manufacturer documentation
for details.

Last Route Repeater 0 (8 bits)

This field is used to indicate the repeater 0 used in the route to communicate with the destination.
The value 0 MUST indicate that no repeater 0 was used for this route.

Last Route Repeater 1 (8 bits)

This field is used to indicate the repeater 1 used in the route to communicate with the destination.
The value 0 MUST indicate that no repeater 1 was used for this route.

Last Route Repeater 2 (8 bits)

This field is used to indicate the repeater 2 used in the route to communicate with the destination.
The value 0 MUST indicate that no repeater 2 was used for this route.

Last Route Repeater 3 (8 bits)

This field is used to indicate the repeater 3 used in the route to communicate with the destination.
The value 0 MUST indicate that no repeater 4 was used for this route.

1000ms Beam (1 bit)

This field is used to indicate if the destination requires a 1000ms beam (or a fragmented beam) to be
reached.

250ms Beam (1 bit)

This field is used to indicate if the destination requires a 250ms beam to be reached.

Last Route Speed (3 bits)

This field is used to indicate the transmission speed used in the route to communicate with the
destination.

The field MUST be encoded according to Table 4.8.


Table 4.8: Priority Route Data Rate Encoding









Routing Attempts (8 bits)

This field is used to indicate how many routing attempts have been made to transmit the payload to
the destination NodeID.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 28


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Last route failed link functional NodeID (8 bits)

This field is used when a route failed and it indicates the last functional NodeID in the last used route.

Last route failed link non-functional NodeID (8 bits)

This field is used when a route failed and it indicates the first non-functional NodeID in the last used
route.

Tx Power (8 bits)

This field is used to indicate the transmit power used for the transmission. This field MUST be
encoded using the signed representation and MUST be expressed in dBm.

Values in the range -127..126 MUST indicate the transmit power. The value 127 MUST indicate that
the value is not available.

Measured Noise Floor (8 bits)

This field is used to indicate the measured noise floor during the outgoing transmission. This field
MUST be encoded according to _RSSI_ _Measurements_ _(8_ _bits)_ and Table 4.3.

Destination Ack MPDU Tx Power (8 bits)

This field is used to advertise the Tx Power used by the destination in its Ack MPDU frame.

Values in the range -127..126 MUST indicate the transmit power. The value 127 MUST indicate that
the value is not available.

Destination Ack MPDU measured RSSI (8 bits)

This field is used to indicate the measured RSSI of the acknowledgement frame received from the
destination. This field MUST be encoded according to _RSSI_ _Measurements_ _(8_ _bits)_ and Table 4.3.

Destination Ack MPDU measured Noise floor (8 bits)

This field is used to indicate the measured noise floor by the destination during the MDPU Ack frame
transmission. This field MUST be encoded according to _RSSI_ _Measurements_ _(8_ _bits)_ and Table 4.3.


**4.2.11** **Route** **Speed** **(8** **bits)**


This field is used to advertise the routed packet data rate that shall be used through the return route.
The field MUST be encoded according to Table 4.9.


Table 4.9: Priority Route Data Rate Encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 29


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.2.12** **Repeater** **(4** **bytes)**


This field is used to indicate the list of repeaters that MUST be used in a return route.

Regardless of the configured NodeID basetype, each of the 4 bytes indicates the NodeID (8 bits each)
of a repeater.

Refer to _Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

If the route is using less than four repeating nodes, the unused entries in the _Repeater_ field MUST be
set to 0x00.

If the route is a direct route, the _Repeater_ field MUST be set to 0x00.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 30


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.3 Z-Wave Capability API commands


This section describes _Z-Wave_ _API_ _Commands_ that are used to initialize and configure the Z-Wave
module. It also comprises commands that are used to read the supported functionality of the Z-Wave
API module.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 31


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.1** **Get** **Init** **Data** **Command**


This command is used to request the initialization data and current node list in the network. The
Get Init Data Command Identifier is 0x02


**4.3.1.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.1.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.10


Table 4.10: Get Init Data Command


**4.3.1.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.11


Table 4.11: Get Init Data Command


Z-Wave API Version (8 bits)

This field is used to advertise the Z-Wave API version that the Z-Wave Module is currently running.

This field MUST be encoded according to Table 4.12


Table 4.12: Get Init Data Command - Z-Wave API Version encoding







Z-Wave API Capabilities (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 32


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to advertise the capabilities of the Z-Wave API running on the Z-Wave Module.
This field MUST be encoded as a bitmask and MUST be according to Table 4.13


Table 4.13: Get Init Data Command         - Z-Wave API Capabilities
encoding





















Z-Wave Node List Length (8 bits)

This field is used to indicate the length in bytes of the _Z-Wave_ _Node_ _List_ field.

End Nodes MUST set this field to 0. Controller Nodes MUST set this field to 29.

Z-Wave Node List (N bytes)

This field is used to advertise the list of nodes present in the current network.

The length of this field, in byte, MUST be according to the _Z-Wave_ _Node_ _List_ _Length_ field. This field
MUST be omitted if the _Z-Wave_ _Node_ _List_ _Length_ field is set to 0.

This field MUST encoded as a bitmask and interpreted as follow:

 - bit 0 in byte 7 MUST represent NodeID 1.

 - bit 1 in byte 7 MUST represent NodeID 2.

 - bit 7 in byte 7 MUST represent NodeID 8.

 - bit 0 in byte 8 MUST represent NodeID 9.

 - etc.

Chip Type (8 bits)

This field is used to advertise the chip type of the Z-Wave Module. This value SHOULD represent
the chip hardware version.

The value of this field is implementation specific. Refer to your manufacturer documentation for
details.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 33


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Chip Version (8 bits)

This field is used to advertise the chip version of the Z-Wave Module.

The value of this field is implementation specific. Refer to your manufacturer documentation for
details.


**4.3.1.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 34


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.2** **Set** **Application** **Node** **Information** **Command**


This command is used to generate the Node Information Frame (NIF) contents and store this information about node capabilities to the Z-Wave module. The host application may initially set up the
NIF prior to starting or joining a Z-Wave network.

The Set Application Node Information Command Identifier is 0x03.


**4.3.2.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**4.3.2.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.14


Table 4.14: Set Application Node Information Command


Device Option Mask (8 bits)

The device option mask is a bitmask where Listening and Optional functionality flags MUST be set
accordingly to the nodes capabilities. This field MUST comply with the format indicated in Table
4.15.


Table 4.15: Set Application Node Information Command         - Device
Option Mask encoding


Generic Device Type (8 bits)

The Generic Device Class field contains an identifier that identifies what Generic Device Class the
Z-Wave node MUST advertise and MUST be set by the application. For a detailed description of all
available Generic Device Classes, refer to [device_class_spec] for Z-Wave devices, [device_type_spec]
for Z-Wave Plus devices, and [device_type_spec_v2] for Z-Wave Plus v2 devices.

Specific Device Type (8 bits)

The Specific Device Class field contains an identifier that identifies what Specific Device Class the
Z-Wave node MUST advertise and MUST be set by the application. For a detailed description of all
available Generic Device Classes, refer to [device_class_spec] for Z-Wave devices, [device_type_spec]
for Z-Wave Plus devices, and [device_type_spec_v2] for Z-Wave Plus v2 devices.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 35


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Command Class List Length (8 bits)

This field MUST specify the length of the _Command_ _Class_ _List_ field in bytes.

Command Class List (N bytes)

This field is used to advertise the list of supported Command Classes by the node. The length of this
field MUST be according to the _Command_ _Class_ _List_ _Length_ field.


**4.3.2.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.3.2.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 36


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.3** **Set** **Application** **Node** **Information** **Command** **Classes** **Command**


This command is used to configure the list of supported Command Classes for each of the following
inclusion states:

 - Not included in a network

 - Included: Non-securely supported

 - Included: Securely supported

The Set Application Node Information Command Classes Command Identifier is 0x0C. This command
MUST only be supported by a Z-Wave Module that employs End Node libraries (Refer to _Get Library_
_Version_ _Command_ _-_ _Library_ _Type_ _encoding_ ).


**4.3.3.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.3.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.16.


Table 4.16: Set Application Node Information Command Classes
Command       - Initial data frame


Not Included Node Parameter Length (8 bits)

This field MUST specify the length of the _Not_ _Included_ _Node_ _Parameter_ field in bytes.

Not Included Node Parameter (N bytes)

This field is used to advertise the list of supported Command Classes before the node is included in
a Z-Wave Network.

Non-securely Included Node Parameter Length (8 bits)

This field MUST specify the length of the _Non-securely_ _Included_ _Node_ _Parameter_ field in bytes.

Non-securely Included Node Parameter (M bytes)

This field is used to advertise the list of non-securely supported Command Classes after the node is
included in a Z-Wave Network.

Securely Included Node Parameter Length (8 bits)

This field MUST specify the length of the _Securely_ _Included_ _Node_ _Parameter_ field in bytes.

Securely Included Node Parameter (G bytes)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 37


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to advertise the list of securely supported Command Classes after the node is included
in a Z-Wave Network.


**4.3.3.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.17.


Table 4.17: Set Application Node Information Command Classes
Command       - Response data frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


**4.3.3.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 38


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.4** **Get** **Controller** **Capabilities** **Command**


This command is used to request a controller from its current network capabilities.

The Get Controller Capabilities Command Identifier is 0x05


**4.3.4.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.4.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.18


Table 4.18: Get Controller Capabilities Command         - Initial data
frame


**4.3.4.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.19


Table 4.19: Get Controller Capabilities Command - Response data
frame


Z-Wave API Controller Capabilities (8 bits)

This field is used to advertise the Controller capabilities in the current network. This field MUST be
treated as a bitmask and encoded according to Table 4.20


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 39


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.20: Get Controller Capabilities Command         - Z-Wave API
Controller Capabilities encoding





























**4.3.4.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 40


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.5** **Get** **Capabilities** **Command**


This command is used to request the API capabilities of a Z-Wave Module. The Get Capabilities
Command identifier is 0x07.


**4.3.5.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.5.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


This Command MUST be formatted according to Table 4.21


Table 4.21: Get Capabilities Command


**4.3.5.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.22


Table 4.22: Get Capabilities Command


Z-Wave API version (8 bits)

This field is used to advertise the Z-Wave API application version number.

Z-Wave API revision (8 bits)

This field is used to advertise the Z-Wave API application revision number.

Z-Wave API manufacturer ID (16 bits)

This field is used to define the Manufacturer ID for the Z-Wave Module. Refer to

[zwave_manufacturer_ids] for details.

Z-Wave API Product Type (16 bits)

This field is used to advertise the Product Type of the Z-Wave Module. A host application MAY
use its own Product Type in the Manufacturer Specific Command Class Refer to the Manufacturer
Specific Command Class in [zwave_management_cc_spec]

Z-Wave API Product ID (16 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 41


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to advertise the Product ID of the Z-Wave Module. A host application MAY use
its own Product ID in the Manufacturer Specific Command Class Refer to the Manufacturer Specific
Command Class in [zwave_management_cc_spec]

Supported Z-Wave API commands bitmask (N bytes)

This field is used to advertise the list of Z-Wave API commands supported by the Z-Wave Module.

This field MUST encoded as a bitmask and interpreted as follow:

 - bit 0 in byte 13 MUST represent the _Z-Wave_ _API_ _Command_ _ID_ 1.

 - bit 1 in byte 13 MUST represent the _Z-Wave_ _API_ _Command_ _ID_ 2.

 - …

 - bit 7 in byte 13 MUST represent the _Z-Wave_ _API_ _Command_ _ID_ 8.

 - bit 0 in byte 14 MUST represent the _Z-Wave_ _API_ _Command_ _ID_ 9.

 - etc.

Each of the bits MUST be intepreted as follow:

 - A bit set to 1 MUST indicate that the corresponding Z-Wave API Command is supported.

 - A bit set to 0 MUST indicate that the corresponding Z-Wave API Command is not supported.


**4.3.5.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 42


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.6** **Get** **Long** **Range** **Nodes** **Command**


This command is used to request the list of Z-Wave Long Range nodes. The Get Long Range Nodes
Command Identifier is 0xDA.

There can be up to 4000 nodes a Z-Wave Long Range network. Nodes with NodeIDs smaller or equal
to 255 can be retrieved using the _Get_ _Init_ _Data_ _Command_ . NodeIDs higher than 255 can be read
using this command. The full list of NodeIDs (from 256 to 4000) can be represented using a bitmask
of 3745 bits, which can be comprised in 467 bytes.

This amount may too large to be sent in a single command, and an offset mechanism is used to fetch
the full list.


**4.3.6.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged frame with response_ . This command may require
multiple initial data frames and response data frames in order to read the full list. An example is
shown in Figure 4.1


Figure 4.1: Reading the Z-Wave Long Range Node List (Example)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 43


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.6.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.23.


Table 4.23: Get Long Range Nodes Command         - Initial data frame


Long Range Node List Start Offset (8 bits)

This field is used to indicate the number of bytes offset for which the Z-Wave Long Range node list
must start from.

A Z-Wave API Module MUST return a Response Data frame with the same Long Range Node List
Start Offset.


**4.3.6.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.24.


Table 4.24: Get Long Range Nodes Command         - Response data
frame


More Nodes (8 bits)

This field is used to indicate if the Z-Wave API Module has advertised the last Z-Wave Long Range
NodeID in the current response

This field MUST be set to 0 if the highest Z-Wave Long Range NodeID is advertised in the _Long_
_Range_ _Node_ _List_ field. This field MUST be set to 1 if there exist a Z-Wave Long Range node with a
higher NodeID than what is advertised in the _Long_ _Range_ _Node_ _List_ field.

A host application receiving a response data frame with this field set to 1 SHOULD issue an initial
data frame again with an increment of the last _Long_ _Range_ _Node_ _List_ _Start_ _Offset_ . Refer to Figure
4.1 for details.

Long Range Node List Start Offset (8 bits)

This field is used to indicate index where the _Long_ _Range_ _Node_ _List_ start from.

Each unit in this field’s value represent a 128-byte offset. For instance:

 - The value 1 represents 1x128 = 128 bytes.

 - The value 2 represents 2x128 = 256 bytes.

 - The value 3 represents 3x128 = 384 bytes

 - etc.

Long Range Node List Length (8 bits)

This field is used to indicate the length in bytes of the _Long_ _Range_ _Node_ _List_ field.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 44


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Long Range Node List (N bytes)

This field is used to advertise the list of Long Range nodes present in the current network.

The length of this field, in byte, MUST be according to the _Long_ _Range_ _Node_ _List_ _Length_ field. This
field MUST be omitted if the _Long_ _Range_ _Node_ _List_ _Length_ field is set to 0.

This field MUST represent NodeIDs as described in (4.1).


_𝑁_ = 256 + 8 _× 𝐽_ + _𝐼_ + 128 _×_ 8 _× 𝑂_ (4.1)


with:

 - N: The NodeID being represented.

 - I: the current bit I number in the current byte (from 0 to 7).

 - J: The current byte (from 0 to _Long_ _Range_ _Node_ _List_ _Length_ -1)

 - O: the value advertised in the _Long_ _Range_ _Node_ _List_ _Start_ _Offset_ field.

For example, with the _Long_ _Range_ _Node_ _List_ _Start_ _Offset_ field set to 0:

 - Bit 0 in Byte 1 MUST represent NodeID 256

 - Bit 1 in Byte 1 MUST represent NodeID 257

 - …

 - Bit 0 in Byte 2 MUST represent NodeID 264

with the _Long_ _Range_ _Node_ _List_ _Start_ _Offset_ field set to 1:

 - Bit 0 in Byte 1 MUST represent NodeID 1280

 - Bit 1 in Byte 1 MUST represent NodeID 1281

 - …

 - Bit 0 in Byte 2 MUST represent NodeID 1288

The value 0 for a given NodeID MUST indicate that the node is not present in the network.

The value 1 for a given NodeID MUST indicate that the node is present in the network.


**4.3.6.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 45


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.7** **Get** **Z-Wave** **Long** **Range** **Channel** **Command**


This command is used to request which the radio channel is in use for Z-Wave Long Range. The Get
Z-Wave Long Range Channel Command Identifier is 0xDB.


**4.3.7.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.7.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.25


Table 4.25: Get Z-Wave Long Range Channel Command         - Initial
data frame


**4.3.7.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.26


Table 4.26: Get Z-Wave Long Range Channel Command         - Response data frame


Z-Wave Long Range Channel (8 bits)

This field is used to advertise the currently configured Z-Wave Long Range Channel at the Z-Wave
API Module.

This field MUST be encoded according to Table 4.27.


Table 4.27: Get Z-Wave Long Range Channel Command         - Z-Wave
Long Range Channel Encoding


Z-Wave Long Range Channel Configuration (8 bits)

This field is used to advertise the automatic Long Range channel configuration of the Z-Wave API
running on the Z-Wave Module. This field MUST be encoded as a bitmask and MUST be according
to Table 4.28


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 46


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.28: Get Z-Wave Long Range Channel Command         - Z-Wave
Long Range Channel Configuration Encoding















**4.3.7.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 47


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.8** **Set** **Z-Wave** **Long** **Range** **Channel** **Command**


This command is used to configure which radio channel to use for Z-Wave Long Range. The Set
Z-Wave Long Range Channel Command Identifier is 0xDC.


**4.3.8.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged frame_ . The execution of this command SHOULD
be verified by a host application by issuing a _Get_ _Z-Wave_ _Long_ _Range_ _Channel_ _Command_ .


**4.3.8.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.29


Table 4.29: Set Z-Wave Long Range Channel Command         - Initial
data frame


Z-Wave Long Range Channel (8 bits)

This field is used to specify the Z-Wave Long Range Channel that the Z-Wave API Module MUST
use.

This field MUST be encoded according to Table 4.30.


Table 4.30: Set Z-Wave Long Range Channel Command         - Z-Wave
Long Range Channel Encoding


**4.3.8.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.31


Table 4.31: Set Z-Wave Long Range Channel Command - Response
data frame


Response Status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 48


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.8.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 49


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.9** **Get** **NLS** **Nodes** **Command**


This command is used to request the list of Z-Wave NLS nodes. The Get NLS Nodes Command
Identifier is 0xC0.


**4.3.9.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged frame with response_ . This command may require
multiple initial data frames and response data frames in order to read the full list. An example is
shown in Figure 4.2


Figure 4.2: Reading the Z-Wave NLS Nodes List (Example)


**4.3.9.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.32.


Table 4.32: Get NLS Nodes Command          - Initial data frame


NLS Nodes List Start Offset (8 bits)

This field is used to indicate the number of 128-bytes offset for which the Z-Wave NLS nodes list must
start from.

A Z-Wave API Module MUST return a Response Data frame with the same NLS Nodes List Start
Offset.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 50


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.9.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.33.


Table 4.33: Get NLS Nodes Command          - Response data frame


NLS Nodes List Start Offset (8 bits)

This field is used to indicate index where the _NLS_ _Nodes_ _List_ start from.

Each unit in this field’s value represent a 128-byte offset. For instance:

 - The value 1 represents 1x128 = 128 bytes offset.

 - The value 2 represents 2x128 = 256 bytes offset.

 - The value 3 represents 3x128 = 384 bytes offset.

 - etc.

More Nodes (1 bit)

This first bit of this field is used to indicate if the Z-Wave API Module has advertised the last enabled
Z-Wave NLS NodeID in the current response.

All other bits are reserved for future use.

This field MUST be set to 0 if the highest enabled Z-Wave NLS NodeID is advertised in the _NLS_
_Nodes_ _List_ field. This field MUST be set to 1 if there exist an enabled Z-Wave NLS node with a
higher NodeID than what is advertised in the _NLS_ _Nodes_ _List_ field.

A host application receiving a response data frame with this field set to 1 SHOULD issue an initial
data frame again with an increment of the last _NLS_ _Nodes_ _List_ _Start_ _Offset_ . Refer to Figure 4.2 for
details.

A host application receiving a response data frame with this field set to 0 SHOULD consider any
remaining nodes to have NLS disabled.

NLS Nodes List Length (8 bits)

This field is used to indicate the length in bytes of the _NLS_ _Nodes_ _List_ field.

NLS Nodes List (N bytes)

This field is used to advertise the list of NLS nodes present in the current network.

The length of this field, in byte, MUST be according to the _NLS_ _Nodes_ _List_ _Length_ field. This field
MUST be omitted if the _NLS_ _Nodes_ _List_ _Length_ field is set to 0.

The length must be 128 if the more nodes flag is set to 1. The length must be between 0 and 128 if
the more nodes flag is set to 0.

This field MUST represent NodeIDs as described in (4.2) for the nodes between 1-232 and as described
in (4.3) for the nodes starting from 256.


_𝑁_ = 1 + 8 _× 𝐽_ + _𝐼_ + 128 _×_ 8 _× 𝑂_ (4.2)


_𝑁_ = 24 + 8 _× 𝐽_ + _𝐼_ + 128 _×_ 8 _× 𝑂_ (4.3)

with:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 51


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


 - N: The NodeID being represented.

 - I: the current bit I number in the current byte (from 0 to 7).

 - J: The current byte (from 0 to _NLS_ _Nodes_ _List_ _Length_ -1)

 - O: the value advertised in the _NLS_ _Nodes_ _List_ _Start_ _Offset_ field.

For example, with the _NLS_ _Nodes_ _List_ _Start_ _Offset_ field set to 0:

 - Bit 0 in Byte 0 MUST represent NodeID 1

 - Bit 1 in Byte 0 MUST represent NodeID 2

 - …

 - Bit 0 in Byte 1 MUST represent NodeID 9

 - …

 - Bit 6 in Byte 28 MUST represent NodeID 231

 - Bit 7 in Byte 28 MUST represent NodeID 232

 - …

 - Bit 0 in Byte 29 MUST represent NodeID 256

 - Bit 1 in Byte 29 MUST represent NodeID 257

 - …

 - Bit 7 in Byte 127 MUST represent NodeID 1047

with the _NLS_ _Nodes_ _List_ _Start_ _Offset_ field set to 1:

 - Bit 0 in Byte 0 MUST represent NodeID 1048

 - Bit 1 in Byte 0 MUST represent NodeID 1049

 - …

 - Bit 7 in Byte 28 MUST represent NodeID 1279

A bit value of 0 MUST indicate that the corresponding node has NLS disabled.

A bit value of 1 MUST indicate that the corresponding node has NLS enabled.

Bits corresponding to the reserved NodeIDs 0 and 233-255 must not be sent.

Bits corresponding to the reserved NodeIDs 4002-4005 must be set to 0.


**4.3.9.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 52


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.10** **Get** **Protocol** **Version** **Command**


This command is used to request the Z-Wave Protocol version data. The Get Protocol Version
Command Identifier is 0x09.


**4.3.10.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.10.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.34


Table 4.34: Get Protocol Version Command         - Initial data frame


**4.3.10.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.35.

A host application MUST be resistant to unexpected lengths (too short or too small) for this command.


Table 4.35: Get Protocol Version Command - Response data frame


Z-Wave Protocol Type (8 bits)

This field is used to indicate the protocol type. This field MUST be encoded according to Table 4.206.


Table 4.36: Z-Wave Get Protocol Version Command - Z-Wave Protocol Type Encoding


Z-Wave Protocol Major Version Number (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 53


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to advertise the Major Version Number for the Z-Wave Protocol. This field MUST
be encoded as an unsigned integer.

Z-Wave Protocol Minor Version Number (8 bits)

This field is used to advertise the Minor Version Number for the Z-Wave Protocol. This field MUST
be encoded as an unsigned integer.

Z-Wave Protocol Revision Version Number (8 bits)

This field is used to advertise the Revision Version Number for the Z-Wave Protocol. This field MUST
be encoded as an unsigned integer.

Z-Wave Application Framework Build Number (16 bits)

This field is used to advertise the Revision Version Number for the Z-Wave Protocol. This field MUST
be encoded as an unsigned integer.

The value 0 MUST indicate that this value is not available. Values in the range 1..65535 MUST
indicate the build number for the application framework.

Git commit hash (16 bytes)

This field is used to advertise the git commit hash for the Z-Wave Protocol running in the Z-Wave
API Module. This field SHOULD be omitted or zeroed out if this information is not available.


**4.3.10.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 54


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.11** **Get** **Library** **Version** **Command**


This command is used to request the Z-Wave library basis version that runs on a Z-Wave Module.
The Get Library Command Identifier is 0x15.


**4.3.11.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.11.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.37


Table 4.37: Get Library Version Command         - Initial data frame


**4.3.11.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.38


Table 4.38: Get Library Version Command         - Response data frame


Z-Wave Library Version (12 bytes)

This field is used to advertise the Z-Wave API library version that runs on the Z-Wave Module using
the following text format:

 - Z-Wave x.y, where x and y are the major and minor library versions, respectively.

 - x and y MUST contain 1 or 2 digits

 - This value MAY NOT be zero-terminated

 - If the string is shorter than 12 bytes (x and or y contains 1 digit only), this field MUST be
padded with zero-characters

Library Type (8 bits)

This field is used to advertise the library type that runs on the Z-Wave Module.

This field MUST encoded according to Table 4.39


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 55


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.39: Get Library Version Command         - Library Type encoding


**4.3.11.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 56


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.12** **Get** **Library** **Command**


This command is used to is used to request the Z-Wave library type that runs on a Z-Wave Module.
The Get Library Command Identifier is 0xBD.


**4.3.12.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.12.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.40


Table 4.40: Get Library Type Command          - Initial data frame


**4.3.12.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.41


Table 4.41: Get Library Type Command         - Response data frame


Library Type (8 bits)

This field is used to advertise the library type that runs on the Z-Wave Module.

This field MUST encoded according to Table 4.39


**4.3.12.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 57


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.13** **Soft** **Reset** **Command**


This command is used to request the Z-Wave Module to perform a soft reset. The Soft Reset Command
Identifier is 0x08.


**4.3.13.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**4.3.13.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.42


Table 4.42: Soft Reset Command            - Initial data frame


**4.3.13.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.3.13.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


Note: A Z-Wave Module SHOULD issue a _Z-Wave_ _API_ _Started_ _Command_ when it has completed
the reset operation.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 58


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.14** **Set** **Default** **Command**


This command is used to set the Z-Wave API Module to its default state. It means that the Z-Wave
API Module will leave its current network and erase all information related to its current Z-Wave
network (topology, network keys, HomeID, etc.).

The Set Default Command Identifier is 0x42.


**4.3.14.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .


**4.3.14.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.43.


Table 4.43: Set Default Command           - Initial data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**4.3.14.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.3.14.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.44 after the Z-Wave
API Module has completed the set default operation.


Table 4.44: Set Default Command           - Callback data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 59


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.15** **Setup** **Z-Wave** **API** **Command**


This command is used to request and configure the Z-Wave Module and its API. The Setup Z-Wave
API Command Identifier is 0x0B.

This command contains sub-commands.


**4.3.15.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.15.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.45.


Table 4.45: Setup Z-Wave API Command          - Initial data frame


Sub Command (8 bits)

This field is used to advertise the Z-Wave API Setup Sub Command. The list of available Sub
Commands are available in _Z-Wave_ _API_ _Setup_ _sub-commands_ .

Sub Command Payload (N bytes)

This field is used to indicate the data payload that corresponds to a given Z-Wave API setup Sub
Command defined in Command field.

Each Sub Command payload MUST be interpreted in conjunction with the actual Sub Command.
refer to _Z-Wave_ _API_ _Setup_ _sub-commands_ .


**4.3.15.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.46.


Table 4.46: Setup Z-Wave API Command         - Response data frame


Command (8 bits)

This field is used to advertise the Z-Wave API Setup Sub Command. The list of available Sub
Commands are available in _Z-Wave_ _API_ _Setup_ _sub-commands_ .

A Z-Wave API module that has received a non-supported Z-Wave API Setup Sub Command MUST
return the value 0 in this field. Refer to _Z-Wave_ _API_ _Setup_ _Get_ _Supported_ _Commands_ _Sub_ _Command_
for the list of supported Z-Wave API setup commands.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 60


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


The value 0 MUST indicate that the received Z-Wave API setup sub command in the Initial data
frame is not supported. If this field is set to 0, the Sub Command Payload field MUST be 1 byte long
and MUST be set to the unsupported Z-Wave API Setup Sub Command received in the Initial data
frame

Sub Command Payload (N bytes)

This field is used to indicate the data payload that corresponds to a given Z-Wave API setup Sub
Command defined in Command field.

Each Sub Command payload MUST be interpreted in conjunction with the actual Sub Command.
refer to _Z-Wave_ _API_ _Setup_ _sub-commands_ .


**4.3.15.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 61


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16** **Z-Wave** **API** **Setup** **sub-commands**


This section describes subcommands of the _Setup_ _Z-Wave_ _API_ _Command_ that are used to configure
the Z-Wave module.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 62


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.1** **Z-Wave** **API** **Setup** **Get** **Supported** **Commands** **Sub** **Command**


This command is used to request the list of Z-Wave API Setup Sub Commands that are supported
by the Z-Wave API Module.

The Z-Wave API Setup Get Supported Commands Sub Command Identifier is 0x01


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.47


Table 4.47: Z-Wave API Setup Get Supported Commands Sub
Command       - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x01 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Supported_ _Commands_ _Sub_
_Command_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.48


Table 4.48: Z-Wave API Setup Get Supported Commands Sub
Command       - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x01 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Supported_ _Commands_ _Sub_
_Command_ .

Z-Wave API Setup Supported Sub Commands flags (8 bits)

This field is used to indicate the list of supported Z-Wave API setup Sub Commands by the Z-Wave
Module.

This field can only advertise support for functions that have identifiers that are powers of 2.

This field MUST be encoded as a bitmask and according to Table 4.49

 - A bit set to 0 MUST indicate that the corresponding Z-Wave API Setup Sub Command is not
supported.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 63


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


 - A bit set to 1 MUST indicate that the corresponding Z-Wave API Setup Sub Command is
supported


Table 4.49: Z-Wave API Setup Get Supported Commands         - Supported Sub Commands encoding







Extended Z-Wave API Setup Supported Sub Commands bitmask (N bytes)

This field is used to advertise the list of supported Sub Commands.

If this field is not present in the response data frame sent by a Z-Wave API Module, a host application
MUST assume that only the sub commands advertised in the _Z-Wave_ _API_ _Setup_ _Supported_ _Sub_
_Commands_ _flags_ field are supported.

This field MUST be treated as a bitmask and MUST be encoded as follow:

 - Bit 0 in Byte 1 MUST represent Sub Command Identifier 1.

 - Bit 1 in Byte 1 MUST represent Sub Command Identifier 2.

 - Bit 2 in Byte 1 MUST represent Sub Command Identifier 3.

 - …

 - Bit 7 in Byte 1 MUST represent Sub Command Identifier 8.

 - Bit 0 in Byte 2 MUST represent Sub Command Identifier 9.

 - Bit 1 in Byte 2 MUST represent Sub Command Identifier 10.

 - Bit 2 in Byte 2 MUST represent Sub Command Identifier 11.

 - …

The list of supported Commands in the _Z-Wave_ _API_ _Setup_ _Supported_ _Sub_ _Commands_ _bitmask_ field
MUST also be advertised as supported in this field.

The length of this field MUST be set to at least the minimum length that allows to advertise all
supported Z-Wave API Setup Sub Commands. The length of this field can be calculated from the
total length of the response data frame.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 64


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.2** **Z-Wave** **API** **Setup** **Set** **Tx** **Status** **Report** **Sub** **Command**


This command is used to configure the Z-Wave API Module to return detailed Tx Status Report after
sending a frame to a destination.

The Z-Wave API Setup Set Tx Status Report Sub Command Identifier is 0x02


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.50


Table 4.50: Z-Wave API Setup Set Tx Status Report Sub Command       - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x02 to indicate the _Z-Wave API Setup Set Tx Status Report Sub Command_
Command.

Enable Tx Status Report (8 bits)

This field is used to indicate if the Tx Status Report MUST be enabled.

 - The value 0x00 MUST indicate that the Tx Status Report MUST NOT be enabled.

 - All other values MUST indicate that the Tx Status Report MUST be enabled.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.51


Table 4.51: Z-Wave API Setup Set Tx Status Report Sub Command       - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x02 to indicate the _Z-Wave API Setup Set Tx Status Report Sub Command_ .

Command Status (8 bits)

This field is used to indicate if the setting indicated in the inital data frame was accepted and applied.

This field MUST be encoded according to _Command_ _Status_ _(8_ _bits)_


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 65


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 66


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.3** **Z-Wave** **API** **Setup** **Set** **Max** **Long** **Range** **TX** **Powerlevel** **Sub** **Command**


This command is used to configure the Max Long Range Tx Powerlevel setting of the Z-Wave API.

The power levels set by this function will first be used by the Z-Wave protocol next time the module
is restarted.

The Z-Wave API Setup Set Max Long Range TX Powerlevel Sub Command Identifier is 0x03


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


Z-Wave API version 7 and above: Table 4.21

The initial data frame MUST be formatted according to Table 4.52


Table 4.52: Z-Wave API Setup Set Powerlevel Sub Command
(v7+)        - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x03 to indicate the _Z-Wave API Setup Set Max Long Range TX Powerlevel_
_Sub_ _Command_ .

Max Long Range TX Powerlevel Setting (16 bits)

This field is used to indicate the requested maximum Long Range transmit powerlevel for transmitting
Z-Wave Long Range Frames.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 10 MUST represent 1 dBm

 - The value -20 MUST represent -2 dBm

Valid range for a 14dBm Board is -60 to 140 and for a 20dBm board, its -60 to 200.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.53


Table 4.53: Z-Wave API Setup Set Max Long Range TX Powerlevel
Sub Command        - Response data frame


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 67


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Sub Command (8 bits)

This field MUST be set to 0x03 to indicate the _Z-Wave API Setup Set Max Long Range TX Powerlevel_
_Sub_ _Command_ .

Command Status (8 bits)

This field is used to indicate if the setting indicated in the inital data frame was accepted and applied.

This field MUST be encoded according to _Command_ _Status_ _(8_ _bits)_


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 68


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.4** **Z-Wave** **API** **Setup** **Set** **Powerlevel** **Sub** **Command**


This command is used to configure the Tx Powerlevel setting of the Z-Wave API.

The power levels set by this function will first be used by the Z-Wave protocol next time the module
is restarted.

The Z-Wave API Setup Set Powerlevel Sub Command Identifier is 0x04


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


Z-Wave API version 7 and above: Table 4.21

The initial data frame MUST be formatted according to Table 4.54


Table 4.54: Z-Wave API Setup Set Powerlevel Sub Command
(v7+)        - Initial data frame


Z-Wave API version 6 and below: Table 4.21

The initial data frame MUST be formatted according to Table 4.55


Table 4.55: Z-Wave API Setup Set Powerlevel Sub Command (v6-)

            - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x04 to indicate the _Z-Wave_ _API_ _Setup_ _Set_ _Powerlevel_ _Sub_ _Command_ .

Normal Powerlevel Setting (8 bits)

This field is used to indicate the requested transmit powerlevel for transmitting Z-Wave Frames.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 10 MUST represent 1 dBm

 - The value -20 MUST represent -2 dBm


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 69


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Measured 0dBm Powerlevel Setting (8 bits)

This field is used to indicate the output power measured from the antenna when the _Normal Powerlevel_
_Setting_ field is set to 0.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 10 MUST represent 1 dBm

 - The value -20 MUST represent -2 dBm

NormalPowerChx (8 bits)

The power level used when transmitting frames at normal Tx power. This value is vendor specific and
should be provided by your stack vendor.

LowPowerCh0 (8 bits)

The power level used when transmitting frames at low Tx power

This field MUST be formatted according to Table 4.56


Table 4.56: Z-Wave API Setup Set Powerlevel Sub Command         Low Tx power encoding


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.57


Table 4.57: Z-Wave API Setup Set Powerlevel Sub Command         Response data frame


Sub Command (8 bits)

This field MUST be set to 0x04 to indicate the _Z-Wave_ _API_ _Setup_ _Set_ _Powerlevel_ _Sub_ _Command_ .

Command Status (8 bits)

This field is used to indicate if the setting indicated in the inital data frame was accepted and applied.

This field MUST be encoded according to _Command_ _Status_ _(8_ _bits)_


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 70


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 71


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.5** **Z-Wave** **API** **Setup** **Get** **Max** **Long** **Range** **Powerlevel** **Sub** **Command**


This command is used to request the Powerlevel setting of the Z-Wave API.

The Z-Wave API Setup Get Max Long Range Powerlevel Sub Command Identifier is 0x05


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.58


Table 4.58: Z-Wave API Setup Get Max Long Range Powerlevel
Sub Command        - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x05 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Max_ _Long_ _Range_ _Powerlevel_
_Sub_ _Command_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.59


Table 4.59: Z-Wave API Setup Get Max Long Range Powerlevel
Sub Command        - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x05 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Max_ _Long_ _Range_ _Powerlevel_
_Sub_ _Command_ .

Max Long Range Tx Powerlevel Setting (16 bits)

This field is used to advertise the currently configured transmit powerlevel for transmitting Z-Wave
Frames.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 10 MUST represent 1 dBm

 - The value -20 MUST represent -2 dBm


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 72


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 73


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.6** **Z-Wave** **API** **Setup** **Set** **Long** **Range** **Max** **Node** **ID** **Sub** **Command**


This command is used to configure the maximum Long Range node ID for the Z-Wave API before
it’ll wrap around to the original range of node ID values.

For example, if the configured value is 512, then the range of Long Range node IDs is 256-512. After
node ID 512 is used by the Z-Wave API and a new node ID needs to be assigned, the search will start
at 256 until an unassigned ID is found.

The maximum Long Range node ID set with this command MUST be persisted in NVM.

If the value set in this command is lower than an already assigned ID then the next ID assignment
would wrap around, and all existing assigned node IDs would remain unchanged.

The Z-Wave API Setup Set Long Range Max Node ID Sub Command Identifier is 0x06.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.60


Table 4.60: Z-Wave API Setup Set Long Range Max Node ID Sub
Command       - Initial data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.

This field MUST be set to 0x06 for the _Z-Wave_ _API_ _Setup_ _Set_ _Long_ _Range_ _Max_ _Node_ _ID_ _Sub_
_Command_ .

Max Node ID (16 bits)

This field is used to indicate the maximum Long Range node ID to be used by the Z-Wave API.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.61


Table 4.61: Z-Wave API Setup Set Long Range Max Node ID Sub
Command       - Response data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 74


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field MUST be set to 0x06 for the _Z-Wave_ _API_ _Setup_ _Set_ _Long_ _Range_ _Max_ _Node_ _ID_ _Sub_
_Command_ .

Command Status (8 bits)

This field is used to indicate if the setting indicated in the inital data frame was accepted and applied.

This field MUST be encoded according to _Command_ _Status_ _(8_ _bits)_ . With the value for the command
not being accepted used if the node ID in the _Z-Wave_ _API_ _Setup_ _Set_ _Long_ _Range_ _Max_ _Node_ _ID_ _Sub_
_Command_ was beyond the range of the maximum supported in the _Z-Wave_ _API_ _Setup_ _Get_ _Long_
_Range_ _Max_ _Node_ _ID_ _Sub_ _Command_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 75


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.7** **Z-Wave** **API** **Setup** **Get** **Long** **Range** **Max** **Node** **ID** **Sub** **Command**


This command is used to request the maximum Long Range node ID configured for the Z-Wave API.

The Z-Wave API Setup Get Long Range Max Node ID Sub Command Identifier is 0x07.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.62


Table 4.62: Z-Wave API Setup Get Long Range Max Node ID Sub
Command       - Initial data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.

This field MUST be set to 0x07 for the _Z-Wave_ _API_ _Setup_ _Get_ _Long_ _Range_ _Max_ _Node_ _ID_ _Sub_
_Command_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.63


Table 4.63: Z-Wave API Setup Get Long Range Max Node ID Sub
Command       - Response data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.

This field MUST be set to 0x07 for the _Z-Wave_ _API_ _Setup_ _Get_ _Long_ _Range_ _Max_ _Node_ _ID_ _Sub_
_Command_ .

Current Max Node ID (16 bits)

This field is used to indicate the maximum Long Range node ID that is currently in use by the Z-Wave
API.

Max Supported Node ID (16 bits)

This field is used to indicate the maximum Long Range node ID supported by the Z-Wave API.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 76


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 77


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.8** **Z-Wave** **API** **Setup** **Get** **Powerlevel** **Sub** **Command**


This command is used to request the Powerlevel setting of the Z-Wave API.

The Z-Wave API Setup Get Powerlevel Sub Command Identifier is 0x08


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.64


Table 4.64: Z-Wave API Setup Get Powerlevel Sub Command         Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x08 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Powerlevel_ _Sub_ _Command_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.65


Table 4.65: Z-Wave API Setup Get Powerlevel Sub Command         Response data frame


Sub Command (8 bits)

This field MUST be set to 0x08 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Powerlevel_ _Sub_ _Command_ .

Normal Powerlevel Setting (8 bits)

This field is used to advertise the currently configured transmit powerlevel for transmitting Z-Wave
Frames.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 10 MUST represent 1 dBm

 - The value -20 MUST represent -2 dBm

Measured 0dBm Powerlevel Setting (8 bits)

This field is used to indicate the configured output power measured from the antenna when the _Normal_
_Powerlevel_ _Setting_ field is set to 0.

This field MUST be expressed in deci dBm and MUST use signed encoding.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 78


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


For example:

 - The value 10 MUST represent 1 dBm

 - The value -20 MUST represent -2 dBm


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 79


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.9** **Z-Wave** **API** **Setup** **Get** **Maximum** **Payload** **Size** **Sub** **Command**


This command is used to request the maximum payload that the Z-Wave API Module can accept for
transmitting Z-Wave frames. This value depends on the RF Profile.

The Z-Wave API Setup Get Maximum Payload Size Sub Command Identifier is 0x10


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.66


Table 4.66: Z-Wave API Setup Get Maximum Payload Size Sub
Command       - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x10 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Maximum_ _Payload_ _Size_ _Sub_
_Command_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.67


Table 4.67: Z-Wave API Setup Get Maximum Payload Size Sub
Command       - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x10 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Maximum_ _Payload_ _Size_ _Sub_
_Command_ .

Maximum Payload Size (8 bits)

This field is used to advertise the Maximum Payload Size, in bytes, supported by the Z-Wave API
Module for sending frames.

Calls to Send Data functions will be ignored if the data length is longer than the value advertised in
this field.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 80


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 81


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.10** **Z-Wave** **API** **Setup** **Get** **Z-Wave** **Long** **Range** **Maximum** **Payload** **Size** **Sub** **Command**


This command is used to request the maximum payload that the Z-Wave API Module can accept for
transmitting Z-Wave Long Range frames.

Z-Wave API Setup Get Z-Wave Long Range Maximum Payload Size Sub Command Identifier is 0x11


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.68


Table 4.68: Z-Wave API Setup Get Z-Wave Long Range Maximum
Payload Size Sub Command        - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x11 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Z-Wave_ _Long_ _Range_ _Maximum_
_Payload_ _Size_ _Sub_ _Command_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.69


Table 4.69: Z-Wave API Setup Get Z-Wave Long Range Maximum
Payload Size Sub Command        - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x11 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Maximum_ _Payload_ _Size_ _Sub_
_Command_ .

Z-Wave Long Range Maximum Payload Size (8 bits)

This field is used to advertise the Maximum Payload Size, in bytes, supported by the Z-Wave API
Module for sending frames using the Z-Wave Long Range protocol.

Calls to Send Data functions to Z-Wave Long Range NodeID destionations will be ignored if the data
length is longer than the value advertised in this field.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 82


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 83


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.11** **Z-Wave** **API** **Setup** **Set** **16-bit** **Powerlevel** **Sub** **Command**


This command is used to configure the Tx Powerlevel setting of the Z-Wave API using 16-bit values.

The powerlevels set by this function will first be used by the Z-Wave protocol next time the module
is restarted.

The Z-Wave API Setup Set 16-bit Powerlevel Sub Command Identifier is 0x12


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.70


Table 4.70: Z-Wave API Setup Set 16-bit Powerlevel Sub Command       - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x12 to indicate the _Z-Wave API Setup Set 16-bit Powerlevel Sub Command_ .

Normal Powerlevel Setting (16 bits)

This field is used to indicate the requested transmit powerlevel for transmitting Z-Wave Frames.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 130 MUST represent 13 dBm

 - The value -130 MUST represent -13 dBm

Measured 0dBm Powerlevel Setting (16 bits)

This field is used to indicate the output power measured from the antenna when the _Normal Powerlevel_
_Setting_ field is set to 0.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 130 MUST represent 13 dBm

 - The value -130 MUST represent -13 dBm


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 84


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.71


Table 4.71: Z-Wave API Setup Set 16-bit Powerlevel Sub Command       - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x12 to indicate the _Z-Wave API Setup Set 16-bit Powerlevel Sub Command_ .

Command Status (8 bits)

This field is used to indicate if the setting indicated in the inital data frame was accepted and applied.

This field MUST be encoded according to _Command_ _Status_ _(8_ _bits)_


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 85


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.12** **Z-Wave** **API** **Setup** **Get** **16-bit** **Powerlevel** **Sub** **Command**


This command is used to request the 16-bit Powerlevel setting of the Z-Wave API.

The Z-Wave API Setup Get 16-bit Powerlevel Sub Command Identifier is 0x13


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.72


Table 4.72: Z-Wave API Setup Get 16-bit Powerlevel Sub Command       - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x13 to indicate the _Z-Wave API Setup Get 16-bit Powerlevel Sub Command_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.65


Table 4.73: Z-Wave API Setup Get 16-bit Powerlevel Sub Command       - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x13 to indicate the _Z-Wave API Setup Get 16-bit Powerlevel Sub Command_ .

Normal Powerlevel Setting (16 bits)

This field is used to advertise the currently configured transmit powerlevel for transmitting Z-Wave
Frames.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 130 MUST represent 13 dBm

 - The value -130 MUST represent -13 dBm


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 86


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Measured 0dBm Powerlevel Setting (16 bits)

This field is used to indicate the configured output power measured from the antenna when the _Normal_
_Powerlevel_ _Setting_ field is set to 0.

This field MUST be expressed in deci dBm and MUST use signed encoding.

For example:

 - The value 130 MUST represent 13 dBm

 - The value -130 MUST represent -13 dBm


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 87


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.13** **Z-Wave** **API** **Setup** **Get** **Supported** **Regions** **Sub** **Command**


This command is used to request the list of Regions that are supported by the Z-Wave implementation.

The Z-Wave API Setup Get Supported Regions Sub Command Identifier is 0x15


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.74


Table 4.74: Z-Wave API Setup Get Supported Regions Sub Command       - Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x15 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Supported_ _Regions_ _Sub_ _Com-_
_mand_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.75


Table 4.75: Z-Wave API Setup Get Supported Regions Sub Command       - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x15 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Supported_ _Regions_ _Sub_ _Com-_
_mand_ .

Number Of Supported Regions (8 bits)

This field contains the number of supported regions that is returned in the _Z-Wave_ _API_ _Setup_ _Get_
_Supported_ _Regions_ _Sub_ _Command_ _-_ _Response_ _data_ _frame_ response. This field MUST have a value
greater than 0.

RF Region (N bytes)

This field contains a list of identifiers of supported regions. The RF Region identifiers can be used
to set the region with the _Z-Wave_ _API_ _Setup_ _Set_ _RF_ _Region_ _Sub_ _Command_ command. To get more
information about the supported region use the _Z-Wave_ _API_ _Setup_ _Get_ _Region_ _Info_ _Sub_ _Command_ .

Each RF Region in this field MUST be encoded according to _RF_ _Region_ _(8_ _bits)_ and Table 4.6


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 88


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 89


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.14** **Z-Wave** **API** **Setup** **Get** **Region** **Info** **Sub** **Command**


This command is used to request information about a supported RF region.

The Z-Wave API Setup Get Region Info Sub Command Identifier is 0x16


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.76


Table 4.76: Z-Wave API Setup Get Region Info Sub Command         Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x16 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Region_ _Info_ _Sub_ _Command_ .

RF Region (8 bits)

This field contains the identifier of the requested RF Region. See _Z-Wave_ _API_ _Setup_ _Get_ _Supported_
_Regions_ _Sub_ _Command_ for information about the region identifier.

This field MUST be encoded according to _RF_ _Region_ _(8_ _bits)_ and Table 4.6


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.77


Table 4.77: Z-Wave API Setup Get Region Info Sub Command         Response data frame


Sub Command (8 bits)

This field MUST be set to 0x16 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _Region_ _Info_ _Sub_ _Command_ .

RF Region (8 bits)

This field MUST contain the identifier of the requested RF Region.

This field MUST be encoded according to _RF_ _Region_ _(8_ _bits)_ and Table 4.6

If the RF Region is not known by the Z-Wave module, this field MUST be set to the Unknown region
(0xFE). All other fields MUST be set to 0.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 90


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Reserved (6 bits)

This field is reserved for future use and MUST be set to 0.

Protocol Mode (2 bits)

This field is used to indicate the list of supported protocol modes for the specified region

This field MUST be encoded as a bitmask and according to Table 4.78

 - A bit set to 0 MUST indicate that the corresponding Z-Wave protocol mode is not supported.

 - A bit set to 1 MUST indicate that the corresponding Z-Wave protocol mode is supported


Table 4.78: Z-Wave API Setup Get Region Info         - Supported Protocol Modes encoding







More than one bit can be set if the region supports both Z-Wave and Z-Wave Long Range. If no bits
are set in this field the region is not supported.

Includes RF Region (8 bits)

This field specifies if this region is a superset of another RF Region. Some regions that support Z-Wave
Long Range may have a corresponding legacy region that does not support Z-Wave Long Range. In
that case the Region MUST use this field to specify the Region ID of the region that it is a superset
of.

This field MUST be encoded according to _RF_ _Region_ _(8_ _bits)_ and Table 4.6


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 91


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.15** **Z-Wave** **API** **Setup** **Get** **RF** **Region** **Sub** **Command**


This command is used to request the current RF region configured at the Z-Wave API Module.

The Z-Wave API Setup Get RF Region Sub Command Identifier is 0x20


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.79


Table 4.79: Z-Wave API Setup Get RF Region Sub Command         Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x20 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _RF_ _Region_ _Sub_ _Command_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.80


Table 4.80: Z-Wave API Setup Get RF Region Sub Command         Response data frame


Sub Command (8 bits)

This field MUST be set to 0x20 to indicate the _Z-Wave_ _API_ _Setup_ _Get_ _RF_ _Region_ _Sub_ _Command_ .

RF Region (8 bits)

This field is used to indicate the current RF Region setting.

This field MUST be encoded according to _RF_ _Region_ _(8_ _bits)_ and Table 4.6


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 92


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 93


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.16** **Z-Wave** **API** **Setup** **Set** **RF** **Region** **Sub** **Command**


This command is used to configure the RF region at the Z-Wave API Module.

The Z-Wave API Setup Set RF Region Sub Command Identifier is 0x40


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.81


Table 4.81: Z-Wave API Setup Get RF Region Sub Command         Initial data frame


Sub Command (8 bits)

This field MUST be set to 0x40 to indicate the _Z-Wave_ _API_ _Setup_ _Set_ _RF_ _Region_ _Sub_ _Command_ .

RF Region (8 bits)

This field is used to indicate the current RF Region setting.

This field MUST be encoded according to _RF_ _Region_ _(8_ _bits)_ and Table 4.6


Note: The RF Region value will be in used by the Z-Wave API Module only after it restarted. A
host application SHOULD issue a _Soft_ _Reset_ _Command_ after configuring the RF Region.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.82


Table 4.82: Z-Wave API Setup Set RF Region Sub Command         Response data frame


Sub Command (8 bits)

This field MUST be set to 0x40 to indicate the _Z-Wave_ _API_ _Setup_ _Set_ _RF_ _Region_ _Sub_ _Command_ .

Command Status (8 bits)

This field is used to indicate if the RF Region setting indicated in the inital data frame was accepted.

This field MUST be encoded according to _Command_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 94


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Note: The RF Region value will be in used by the Z-Wave API Module only after it restarted. A
host application SHOULD issue a _Soft_ _Reset_ _Command_ after configuring the RF Region.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 95


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.16.17** **Z-Wave** **API** **Setup** **Set** **NodeID** **Base** **Type** **Sub** **Command**


This command is used to configure the NodeID base type for the Z-Wave API.

The Z-Wave API Setup Set NodeID Base Type Sub Command Identifier is 0x80.

All Z-Wave API Commands MUST use the length defined in this Sub Command for encoding NodeID
fields. The default NodeID field length MUST be 8 bits. The NodeID Base Type set with this
command MUST be persisted in NVM.

Note: It is required that an implementation persists the Node ID Base Type in NVM. However, some
older implementations did not do this and when running on such an implementation it is necessary
to set the NodeID Base Type each time the Host API starts.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.83


Table 4.83: Z-Wave API Setup Set NodeID Base Type Sub Command       - Initial data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.

This field MUST be set to 0x80 for the _Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ .

NodeID Base Type (8 bits)

This field is used to indicate the desired base type for NodeID fields.

This field MUST be encoded according to Table 4.84. All other values are reserved.


Table 4.84: Z-Wave API Setup Set NodeID Base Type Sub Command       - NodeID Base Type encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 96


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.85


Table 4.85: Z-Wave API Setup Set NodeID Base Type Sub Command       - Response data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.

This field MUST be set to 0x80 for the _Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ .

Command Status (8 bits)

This field is used to indicate if the setting indicated in the inital data frame was accepted and applied.

This field MUST be encoded according to _Command_ _Status_ _(8_ _bits)_

 - The value 0 MUST indicate that the requested NodeID Base Type in the initial data frame was
not accepted or an error occurred. The NodeID Base Type was not applied and is set to the
default length. (8-bits)

 - The values 1..255 MUST indicate that the requested NodeID Base Type in the initial data frame
was accepted and applied successfully.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 97


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.3.17** **Get** **Manufacturer** **Info** **Command**


This command is used to request the Z-Wave Hardware, Protocol, and Host API manufacturer info.
The Get Manufacturer Info Command Identifier is 0xEA.


**4.3.17.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.3.17.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.34


Table 4.86: Get Manufacturer Info Command         - Initial data frame


**4.3.17.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.87.


Table 4.87: Get Manufacturer Info Command         - Response data
frame


Z-Wave Hardware Manufacturer ID (16 bits)

This field is used to define the Hardware Manufacturer ID for the Z-Wave Module. Refer to

[zwave_manufacturer_ids] for details.

Z-Wave Protocol Manufacturer ID (16 bits)

This field is used to define the Protocol Manufacturer ID for the Z-Wave Module. Refer to

[zwave_manufacturer_ids] for details.

Z-Wave Host API Manufacturer ID (16 bits)

This field is used to define the Host API Manufacturer ID for the Z-Wave Module. Refer to

[zwave_manufacturer_ids] for details.

Manufacturer Specific Chip Info Length (8 bits)

This field specifies the length of the following Manufacturer Specific Chip Info.

Manufacturer Specific Chip Info (N bytes)

The field is used to define the Manufacturer Specific Chip Info for the Z-Wave Module.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 98


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Example information that could be included:

 - The first byte is the chip generation

 - The second byte is the chip type (module or SoC)

 - The third byte is the chip SKU

 - The fourth byte is the chip revision

Refer to the individual manufacturer documentation for details.


**4.3.17.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 99


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.4 Z-Wave API Network Management Commands


This section describes _Z-Wave_ _API_ _Commands_ that are used to perform Z-Wave Network Management.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 100


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1** **Common** **Network** **Management** **Commands**


This section describes _Z-Wave API Commands_ that are used to perform Z-Wave Network Management
for any nodes (both controller nodes and end nodes).

The commands described in this subsection MUST be supported by all Z-Wave API modules.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 101


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.1** **Send** **NOP** **Command**


This command is used to send NOP Commands a destination to verify if it is responsive. This
command SHOULD NOT be used by a host application for NL Nodes outside their Wake Up period.
Refer to the [zwave_nwk_spec] for details. The Send NOP Command Identifier is 0xE9.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.88


Table 4.88: Send NOP Command           - Initial data frame


Destination NodeID (8 bits/16 bits)

This field is used to indicate the destination NodeID to send the Z-Wave Frame to.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.89


Table 4.89: Send NOP Command           - Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 102


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.90


Table 4.90: Send NOP Command           - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .

Tx Status Report (N bytes)

This field is used to report detailed information about the Z-Wave frame transmission. This field
MUST be omitted if the Z-Wave API module is not configured to enable Tx Status Reports in the
_Z-Wave_ _API_ _Setup_ _Set_ _Tx_ _Status_ _Report_ _Sub_ _Command_ .

For field description, refer to _Tx_ _Status_ _Report_ _(N_ _bytes)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 103


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.2** **Get** **Node** **Information** **Protocol** **Data** **Command**


This command is used to request the Node Information protocol data about a NodeID to the Z-Wave
API Module. The Get Node Information Protocol Data Command Identifier is 0x41.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.91


Table 4.91: Get Node Information Protocol Data Command         - Initial data frame


NodeID (8/16 bits)

This field is used to indicate the NodeID for which the Node Information protocol data is requested.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.92


Table 4.92: Get Node Information Protocol Data Command         - Response data frame



















Fields values in this command MUST be according to the _Node Information Frame Command_ received
by the NodeID being advertised. Refer to the [zwave_nwk_spec] for details.

If the NodeID requested in the Initial Data Frame is not part of the Network or is unknown to the
Z-Wave Module, the _Generic_ _Device_ _Class_ field MUST be set to 0. All other fields SHOULD also be
set to 0 and ignored by a receiving interface.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 104


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 105


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.3** **Send** **Node** **Information** **Command**


This command is used to trigger a transmission of Node Information Frame. The Send Node Information Command Command Identifier is 0x12.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.93.


Table 4.93: Send Node Information Command         - Initial data frame


Destination NodeID (8/16 bits)

This field is used to indicate the destination NodeID of the node where the Node Information Frame
is sent to.

Tx Option (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Session identifer (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.94.


Table 4.94: Send Node Information Command         - Response data
frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 106


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.95 after the module
transmit the node information frame to target node.


Table 4.95: Send Node Information Command         - Callback data
frame


Session identifier(8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Rx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 107


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.4** **Request** **Node** **Information** **Command**


This command is used to request the Node Information Frame from a Z-Wave Node. The Request
Node Information Command Identifier is 0x60.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .

This command will trigger additional unsolicited frames from the Z-Wave API Module. Examples of
the expected frame flows are shown in Figure 4.3 and Figure 4.4

If the Z-Wave API Module receives the requested _Node_ _Information_ _Frame_ _Command_,
it MUST issue an unsolicited _Application_ _Update_ _Command_ with the status set to UPDATE_STATE_NODE_INFO_RECEIVED.

If the Z-Wave API Module does not receive the requested _Node_ _Information_ _Frame_ _Com-_
_mand_, it MUST issue an unsolicited _Application_ _Update_ _Command_ with the status set to UPDATE_STATE_NODE_INFO_REQ_FAILED.


Figure 4.3: Request Node Information Command Success Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 108


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.4: Request Node Information Command Fail Example


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.96.


Table 4.96: Request Node Information Command         - Initial data
frame


NodeID (8/16 bits)

This field is used to indicate the NodeID for which the _Node_ _Information_ _Frame_ must be requested.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.97.


Table 4.97: Request Node Information Command         - Response data
frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 109


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 110


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.5** **Set** **Learn** **Mode** **Command**


This command is used to start or stop Learn Mode The Set Learn Mode Command Identifier is 0x50.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .

This command will trigger several callback frames. This is illustrated in Figure 4.5


Figure 4.5: Set Learn Mode Command Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 111


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.98


Table 4.98: Set Learn Mode Command          - Initial data frame


Learn Mode Intent (8 bits)

This field is used to indicate the Learn Mode Intent. Refer to [zwave_nwk_spec] for _Learn_ _Mode_
details.

This field MUST be encoded according to Table 4.99.


Table 4.99: Set Learn Mode Command         - Learn Mode Intent encoding


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 112


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.100


Table 4.100: Set Learn Mode Command         - Response data frame


Response Status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return issue a callback data frame formatted according to Table 4.101


Table 4.101: Set Learn Mode Command         - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Learn Mode Status (8 bits)

This field is used to indicate the current Learn Mode Status.

This field MUST be encoded according to Table 4.102.


Table 4.102: Learn Mode Status encoding


All other values are reserved.

NodeID (8 bits/16 bits)

This field is used to indicate the NodeID currently assigned to the Z-Wave API Module. If the node
is removed from the network, this field MUST be set to 0x00.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Status Message Length (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 113


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to advertise the length of _Status_ _Message_ in bytes.

Status Message (N bits)

The length of this field, in bytes, MUST be according to the _Status_ _Message_ _Length_ field.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 114


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.6** **Get** **SUC** **NodeID** **Command**


This command is used to get currently registered SUC/SIS NodeID in a Z-Wave network. The Get
SUC NodeID Command Identifier is 0x56.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.103.


Table 4.103: Get SUC NodeID Command          - Initial data frame


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.104.


Table 4.104: Get SUC NodeID Command         - Response data frame


SUC NodeID (8 bits)

This field is used to advertise the SUC NodeID in the Z-Wave network.

The value 0x00 MUST indicate that there is no SUC NodeID in the current network. All other values
MUST indicate the NodeID of the SUC in the current network.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 115


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.7** **Set** **SmartStart** **Inclusion** **Request** **Maximum** **Interval** **Command**


This command is used to set the maximum interval between SmartStart inclusion requests. The Set
Maximum SmartStart Inclusion Request Interval Command Identifier is 0xD6.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.105 to set the maximum number of
ticks between SmartStart inclusion requests.


Table 4.105: Set Maximum SmartStart Inclusion Request Interval
Command       - Initial data frame


Requested Intervals 1 (8 bits)

This field is used to indicate the maximum number of ticks between SmartStart inclusion requests.
Each ticks MUST have 128 seconds interval.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.106.


Table 4.106: Set Maximum SmartStart Inclusion Request Interval
Command       - Response data frame


Command Status (8 bits)

This field is used to advertise the status regarding the configuration of SmartStart inclusion request
interval. The field value MUST be encoded according to _Command_ _Status_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 116


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.8** **Explore** **Request** **Inclusion** **Command**


This command is used to initiate a Network-Wide Inclusion process. When the Z-Wave module
receives this command, the module MUST issue an explore frame for requesting inclusion (add) to a
Z-Wave network. The Explore Request Inclusion Command Identifier is 0x5E.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .

The host application MUST send _Set_ _Learn_ _Mode_ _Command_ with a _Learn_ _Mode_ _Intent_ field value
equals to 0x81 before sending _Explore_ _Request_ _Inclusion_ _command_ for requesting the Z-Wave API
module to trigger a Network-Wide Inclusion process. Once a _Set_ _Learn_ _Mode_ _callback_ _data_ _frame_
(that indicates the inclusion process has started) is received, the application MUST NOT send this
command to the Z-Wave API module. Figure 4.6 illustrates the usage of _Explore_ _Request_ _Inclusion_
_Command_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 117


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.6: Explore Request Inclusion Command Example


It is not recommended to use this command since _Set_ _Learn_ _Mode_ _Command_ with a _Learn_ _Mode_
_Intent_ field value equals to 0x81 can trigger the Inclusion process without issuing _Explore_ _Request_
_Inclusion_ _Command_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 118


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.107.


Table 4.107: Explore Request Inclusion Command         - Initial data
frame


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.108.


Table 4.108: Explore Request Inclusion Command - Response data
frame


Inclusion Request Status (8 bits)

This field is used to advertise the status regarding the acceptance of the _Explore_ _Request_ _Inclusion_
_Command_ _Initial_ _data_ _frame_ . This field MUST be encoded as follow:

 - The field value MUST set to 0x01, if the inclusion request is queued for transmission by the
Z-Wave module.

 - The field value MUST set to 0x00, if the Learn Mode is not set.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 119


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.1.9** **Explore** **Request** **Exclusion** **Command**


This command is used to initiate a Network-Wide Exclusion process. When the Z-Wave module
receives this command, the module MUST issue an explore frame for requesting exclusion (remove)
from a Z-Wave network. The Request Network Wide Exclusion Command Identifier is 0x5F.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .

The host application MUST send _Set_ _Learn_ _Mode_ _Command_ with _Learn_ _Mode_ _Intent_ field value
equals to 0x83 before sending _Explore_ _Request_ _Exclusion_ _command_ to the Z-Wave module. Once a
_Set_ _Learn_ _Mode_ _callback_ _data_ _frame_ (that indicates the Exclusion process has started) is received, the
application MUST NOT send this command to the Z-Wave module. Figure 4.7 illustrates the usage
of _Explore_ _Request_ _Exclusion_ _Command_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 120


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.7: Explore Request Exclusion Command Example


It is not recommended to use this command since _Set_ _Learn_ _Mode_ _Command_ with a _Learn_ _Mode_
_Intent_ field value equals to 0x83 can trigger the Exclusion process without issuing _Explore_ _Request_
_Exclusion_ _Command_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 121


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.109.


Table 4.109: Explore Request Exclusion Command         - Initial data
frame


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.110.


Table 4.110: Explore Request Exclusion Command - Response data
frame


Exclusion Request Status (8 bits)

This field is used to advertise the status regarding the acceptance of the _Explore_ _Request_ _Exclusion_
_Command_ _Initial_ _data_ _frame_ . This field MUST be encoded as follow:

 - The field value MUST set to 0x01, if the exclusion request is queued for transmission by the
Z-Wave module.

 - The field value MUST set to 0x00, if the Learn Mode is not set.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 122


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.2** **End** **Nodes** **Network** **Management**


This section describes _Z-Wave API Commands_ that are used to perform Z-Wave Network Management
for End Nodes.

The commands described in this subsection MUST be supported by Z-Wave API modules implementing an _End_ _Node_ library type (refer to Table 4.39).

The commands described in this subsection MUST NOT be supported by Z-Wave API modules
implementing a _Controller_ _Node_ library type (refer to Table 4.39).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 123


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.2.1** **Request** **New** **Route** **Destinations** **Command**


This command is used to request a new route for destination nodes from SUC/SIS node. The Request
New Route Destinations Command Identifier is 0x5C.

This commands MUST only be supported by a Z-Wave API module implementing a _Enhanced_ _232_
_End_ _Node_ _Library_ or _Routing_ _End_ _Node_ _library_ .


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .

When the Z-Wave API module receives _Request New Route Destinations Command_, it will send _Static_
_Route_ _Request_ _Commands_ for each Destination NodeIDs. This is illustrated in Figure 4.8


Figure 4.8: Request New Route Destinations Command Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 124


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.111.


Table 4.111: Request New Route Destinations Command         - Initial
data frame


Destinations NodeID (N bytes)

This field is used to indicates the new destination NodeIDs for which return routes are requested.

Each byte in this field MUST represent a NodeID. All NodeIDs MUST be encoded using 8 bits
regardless of the configured NodeID base Type. Refer to _Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_
_Sub_ _Command_ and Table 4.84.

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.112.


Table 4.112: Request New Route Destinations Command         - Response data frame


Request New Route Response (8 bits)

This field is used to advertise the response of the Z-Wave module regarding the acceptance of the
_Request_ _New_ _Route_ _Destinations_ _Command_ _Initial_ _data_ _frame_ . This field MUST be encoded as follow:

 - If the new route updating process is started, this field value MUST be set to 0x01.

 - If the protocol runs on Z-Wave module is busy or the SUC/SIS node is unknown to the protocol,
this field value MUST be set to 0x00.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.113.


Table 4.113: Request New Route Destinations Command         - Callback data frame


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 125


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Request New Route Callback Status (8 bits)

This field is used to notify status of the new route updating process. This field MUST be encoded
according to Table 4.114.


Table 4.114: Request New Route Destinations Callback Status
Value encoding









© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 126


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.2.2** **Is** **Node** **Within** **Direct** **Range** **Command**


This command is used to check if a given NodeID is marked as a direct range node (A node that can
be reached with a direct range communication from a Z-Wave API module) in any of the existing
return routes. Is Node Within Direct Range Command Identifier is 0x5D.

This commands MUST only be supported by a Z-Wave module that employs _Enhanced_ _232_ _End_ _Node_
_Library_ or _Routing_ _End_ _Node_ _library_ .


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.115.


Table 4.115: Is Node Within Direct Range Command - Initial data
frame


NodeID (8 bits)

This field is used to indicate the NodeID which will be examined if it is stored as a direct range node
in existing return routes.

This field MUST be encoded using 8 bits regardless of the configured NodeID base Type. Refer to
_Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.116.


Table 4.116: Is Node Within Direct Range Command         - Response
data frame


Direct Range Status (8 bits)

This field is used to indicate a status regarding the node presence in existing return route as a direct
range node. This field MUST be encoded as follow:

 - If the node is reachable within direct range, the field value MUST be set to 0x01.

 - If the node is beyond direct range or status is unknown to the Z-Wave protocol, the field value
MUST be set to 0x00.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 127


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 128


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.2.3** **Get** **Network** **Statistics** **Command**


This command is used to request the current Network Statistics as collected by a library runs on
the Z-Wave Module. It is expected that the library will continuously update any Network Statistics
counter until it reaches 65535, which then indicates that the specific counter has reached 65535 or
more occurrences. The Network Statistics counters shall be cleared either on module startup, or by
receiving Clear Network Statistics Command. The Get Network Statistics Command Identifier is
0x3A.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.117


Table 4.117: Get Network Statistics Command - Initial data frame


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.118


Table 4.118: Get Network Statistics Command         - Response data
frame


Tx Frames (2 bytes)

This field is used to indicate the transmitted frames. This field MUST be encoded as a 16-bits unsigned
integer.

Tx LBT BackOffs (2 bytes)

This field is used to advertise the numbers of times the Tx had to wait and postpone a transmission
due to a measured RSSI above the allowed LBT threshold.

This field MUST be encoded as a 16-bits unsigned integer.

Rx Frames (2 bytes)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 129


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to advertise the numner of received frames without any errors. This field MUST be
encoded as a 16-bits unsigned integer.

Rx Checksum Errors (2 bytes)

This field is used to advertise the number of received frames with checksum errors. This field MUST
be encoded as a 16-bits unsigned integer.

Rx CRC16 Errors (2 bytes)

This field is used to advertise the number of received frames with CRC16 checksum errors. This field
MUST be encoded as a 16-bits unsigned integer.

Rx Foreign HomeID (2 bytes)

This field is used to advertise the number of valid Z-Wave frames that has been received with a
HomeID not matching the HomeID of the receiving node. This field MUST be encoded as a 16-bits
unsigned integer.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 130


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.2.4** **Clear** **Network** **Statistics** **Command**


This command is used to clear the current Network Statistics collected by the Z-Wave API Module.
The Clear Network Statistics Command Identifier is 0x39.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.119


Table 4.119: Clear Network Statistics Command         - Initial data
frame


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.120


Table 4.120: Clear Network Statistics Command         - Response data
frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 131


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3** **Controller** **Nodes** **Network** **Management**


This section describes _Z-Wave API Commands_ that are used to perform Z-Wave Network Management
for Controller Nodes.

The commands described in this subsection MUST NOT be supported by Z-Wave API modules
implementing an _End_ _Node_ library type (refer to Table 4.39).

The commands described in this subsection MUST be supported by Z-Wave API modules implementing a _Controller_ _Node_ library type (refer to Table 4.39).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 132


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.1** **Add** **Node** **To** **Network** **Command**


This command is used to trigger a node inclusion to a Z-Wave network. The Add Node To Network
Command Identifier is 0x4A.

This Command MUST be supported by Controller Nodes Z-Wave API implementations. This Command MUST NOT be supported by End Nodes Z-Wave API implementations.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .

The host application may issue several 1. initial data frames several during an inclusion and the
Z-Wave API module may issue sereval 3. callback data frames during an inclusion.

Figure 4.9 shows an example of a successful network inclusion.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 133


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.9: Add Node To Network Command Success Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 134


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.10 shows an example of a host timeout for a network inclusion.


Figure 4.10: Add Node To Network Command Abort Example


Figure 4.11 shows an example of a SmartStart network inclusion.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 135


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


~~Figure~~ ~~4.11:~~ ~~Add~~ ~~Node~~ ~~To~~ ~~Network~~ ~~Command~~ ~~SmartStart~~ ~~Example~~
© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 136


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.12 shows an example of a Z-Wave Long Range SmartStart network inclusion.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 137


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


~~Figure~~ ~~4.12:~~ ~~Add~~ ~~Node~~ ~~To~~ ~~Network~~ ~~Command~~ ~~Z-Wave~~ ~~Long~~ ~~Range~~ ~~SmartStart~~ ~~Example~~
© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 138


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.13 shows an example of an inclusion with the option SFLND set to 1.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 139


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


~~Figure~~ ~~4.13:~~ ~~Add~~ ~~Node~~ ~~To~~ ~~Network~~ ~~Command~~ ~~with~~ ~~SFLND~~ ~~Example~~
© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 140


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.121


Table 4.121: Add Node To Network Command - Initial data frame


Power (1 bit)

This field is used to indicate which power to use for the Network Inclusion operation.

 - The value 0 MUST indicate that the Z-Wave Module MUST use reduced power for the network
inclusion.

 - The value 1 MUST indicate that the Z-Wave Module MUST use normal power for the network
inclusion.

NWI (1 bit)

This field is used to indicate if the operation must be a direct range Network Inclusion or NWI.

 - The value 0 MUST indicate that the Z-Wave Module MUST use direct range network inclusion
for the network inclusion.

 - The value 1 MUST indicate that the Z-Wave Module MUST use NWI for the network inclusion.

Protocol (1 bit)

This field is used to indicate if the operation must be carried out using Z-Wave or Z-Wave Long Range.

 - The value 0 MUST indicate that the Z-Wave Module MUST use Z-Wave for the Add mode
operation.

 - The value 1 MUST indicate that the Z-Wave Module MUST use Z-Wave Long Range for the
Add mode operation.

SFLND: Skip FL nodes in Neighbors Discovery (1 bit)

This field is used to indicate if the operation must skip FL nodes in the neighbors discovery of the
included node or not.

 - The value 0 MUST indicate that the Z-Wave Module MUST NOT skip FL nodes to be found
by the included node if a neighbors discovery is needed.

 - The value 1 MUST indicate that the Z-Wave Module MUST skip FL nodes to be found by the
included node if a neighbors discovery is needed.

Mode (4 bits)

This field is used to indicate which “Add Mode” operation the Z-Wave Module MUST carry out.

This field MUST encoded according to Table 4.122


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 141


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.122: Add Node To Network Command         - Mode encoding


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

NWI HomeID (4 bytes)

This field is used to indicate the NWI HomeID of the node that MUST be included using SmartStart.

If the _Mode_ field is not set to 0x08, this field and the Auth HomeID field MAY be omitted. If the
_Mode_ field is not set to 0x08, this field SHOULD be set to 0x00000000.

If the _Mode_ field is set to 0x08, this field MUST be set to the NWI HomeID of the DSK entry that
MUST be included by the Z-Wave API Module.

Auth HomeID (4 bytes)

This field is used to indicate the Auth HomeID of the node that MUST be included using SmartStart.

If the _Mode_ field is not set to 0x08, this field and the NWI HomeID field MAY be omitted. If the
_Mode_ field is not set to 0x08, this field SHOULD be set to 0x00000000.

If the _Mode_ field is set to 0x08, this field MUST be set to the Auth HomeID of the DSK entry that
MUST be included by the Z-Wave API Module.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 142


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.123


Table 4.123: Add Node To Network Command         - Callback data
frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Status (8 bits)

This field is used to advertise the current status of the inclusion process.

This field MUST be according to Table 4.124


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 143


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.124: Add Node To Network Command         - Status encoding


Assigned NodeID (8/16 bits)

This field is used to advertise the NodeID that was assigned during the inclusion process.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

The value 0 MUST indicate that no NodeID was assigned at that stage of the inclusion process.

Data Length (8 bits)

This field is used to advertise the length of subsequent data in bytes (the _Supported_ _Command_ _Class_
_List_ field size + 3).

Basic Device Type (8 bits)

This field is used to advertise the Basic Device Type reported by the node.

For a detailed description of the _Basic_ _Device_ _Type_ field, refer to [device_class_spec] for Z-Wave
nodes, [device_type_spec] for Z-Wave Plus nodes, and [device_type_spec_v2] for Z-Wave Plus v2
nodes.

Generic Device Type (8 bits)

This field is used to advertise the Generic Device Type reported by the node.

For a detailed description of the _Generic_ _Device_ _Type_ field, refer to [device_class_spec] for Z-Wave
nodes, [device_type_spec] for Z-Wave Plus nodes, and [device_type_spec_v2] for Z-Wave Plus v2
nodes.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 144


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Specific Device Type (8 bits)

This field is used to advertise the Specific Device Type reported by the node.

For a detailed description of the _Specific_ _Device_ _Type_ field, refer to [device_class_spec] for Z-Wave
nodes, [device_type_spec] for Z-Wave Plus nodes, and [device_type_spec_v2] for Z-Wave Plus v2
nodes.

Supported Command Class List (N bytes)

This field is used to advertise the list of supported Command Classes reported by the node during its
inclusion.

This list represents the non-secure supported Command Classes.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field ( _Data_ _Length_ - 3).

A host application SHOULD request the node’s capabilities again after S0/S2 bootstrapping.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 145


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.2** **Add** **Controller** **And** **Assign** **Primary** **Controller** **Role** **Command**


This command is used to include and give the Primary Controller Role to another controller node.
The Assign Primary Controller Role Command Identifier is 0x4C.

This command MUST be used by a host application only if the Z-Wave API Module is Secondary
Controller, has the SUC Role and the Primary Controller has been removed from the network.

This command MUST NOT be used in any other case.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.125


Table 4.125: Add Controller And Assign Primary Controller Role
Command       - Initial data frame


Power (1 bit)

This field is used to indicate which power to use for the Network Inclusion operation.

 - The value 0 MUST indicate that the Z-Wave Module MUST use reduced power for the network
inclusion.

 - The value 1 MUST indicate that the Z-Wave Module MUST use normal power for the network
inclusion.

NWI (1 bit)

This field is used to indicate if the operation must be a direct range Network Inclusion or NWI.

 - The value 0 MUST indicate that the Z-Wave Module MUST use direct range network inclusion
for the network inclusion.

 - The value 1 MUST indicate that the Z-Wave Module MUST use NWI for the network inclusion.

Mode (5 bits)

This field is used to indicate which “Add Mode” operation the Z-Wave Module MUST carry out.

This field MUST encoded according to Table 4.126


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 146


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.126: Add Controller And Assign Primary Controller Role
Command       - Mode encoding


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.127


Table 4.127: Add Controller And Assign Primary Controller Role
Command       - Callback data frame


For fields description, refer to _Add_ _Node_ _To_ _Network_ _Command_


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 147


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.3** **Add** **Primary** **Controller** **Command**


This command is used to include a controller node and assign it the Primary Controller Role. The
Add Primary Controller Command Identifier is 0x4D.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.128


Table 4.128: Add Primary Controller Command - Initial data frame


Power (1 bit)

This field is used to indicate which power to use for the Network Inclusion operation.

 - The value 0 MUST indicate that the Z-Wave Module MUST use reduced power for the network
inclusion.

 - The value 1 MUST indicate that the Z-Wave Module MUST use normal power for the network
inclusion.

NWI (1 bit)

This field is used to indicate if the operation must be a direct range Network Inclusion or NWI.

 - The value 0 MUST indicate that the Z-Wave Module MUST use direct range network inclusion
for the network inclusion.

 - The value 1 MUST indicate that the Z-Wave Module MUST use NWI for the network inclusion.

Mode (5 bits)

This field is used to indicate which “Add Mode” operation the Z-Wave Module MUST carry out.

This field MUST encoded according to Table 4.129


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 148


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.129: Add Primary Controller Command         - Mode encoding


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.130


Table 4.130: Add Primary Controller Command         - Callback data
frame


For fields description, refer to _Add_ _Node_ _To_ _Network_ _Command_


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 149


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.4** **Remove** **Node** **From** **Network** **Command**


This command is used to trigger a node removal operation from a Z-Wave network. It is also possible to
perform out-of-range removal of nodes from the network when repeater nodes are capable of forwarding
the new network wide exclusion (NWE) frame. The Remove Node From Network Command Identifier
is 0x4B.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .

The host application may issue several 1. initial data frames several during an inclusion and the
Z-Wave API module may issue sereval 3. callback data frames during an inclusion.

Figure 4.14 and Figure 4.15 show examples of successful network exclusion.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 150


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.14: Remove Node From Network Command Success Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 151


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.15: Remove Node From Network Command foreign network Success Example


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.131


Table 4.131: Remove Node From Network Command         - Initial data
frame


Power (1 bit)

This field is used to indicate which power to use for the removal node operation.

 - The value 0 MUST indicate that the Z-Wave Module MUST use reduced power for the removal
node operation.

 - The value 1 MUST indicate that the Z-Wave Module MUST use normal power for the removal
node operation.

NWE (1 bit)

This field is used to indicate if direct range Network Exclusion or NWE.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 152


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


 - The value 0 MUST indicate that the Z-Wave Module MUST use direct range exclusion for the
removal node operation.

 - The value 1 MUST indicate that the Z-Wave Module MUST use NWE for the removal node
operation.

Mode (4 bits)

This field is used to indicate which “Remove Mode” operation the Z-Wave Module MUST carry out.

This field MUST encoded according to Table 4.132


Table 4.132: Remove Node From Network Command         - Mode encoding


Session Identifier(8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.133


Table 4.133: Remove Node From Network Command         - Callback
data frame


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 153


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


For fields not described below, refer to _Add_ _Node_ _To_ _Network_ _Command_ _-_ _3._ _Callback_ _data_ _frame_ .

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Status (8 bits)

This field is used to advertise the current status of the node removal process.

This field MUST be according to Table 4.134


Table 4.134: Remove Node From Network Command         - Status encoding


Values that are not described in table_remove_node_from_network_status_encoding are reserved
and MUST NOT be used.

NodeID (8/16 bits)

This field indicates the NodeID of the node that was removed from a network.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

The value 0 MUST indicate that no node was removed (yet) in our current network. A Z-Wave API
Moduel MUST set this value to 0 if excluding a node from a foreign network.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 154


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.5** **Remove** **Specific** **Node** **From** **Network** **Command**


This command is used to trigger a specific node removal operation from a Z-Wave network. It is
also possible to perform out-of-range removal of specific node from the network when repeater nodes
are capable of forwarding the new network wide exclusion (NWE) frame. The Remove Specific Node
From Network Command Identifier is 0x3F.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.135.


Table 4.135: Remove Specific Node From Network Command         Initial data frame


Refer to _Remove_ _Node_ _From_ _Network_ _Command_ _Initial_ _data_ _frame_ for fields that are not described
below.

NodeID (8/16 bits)

This field is used to indicate the NodeID to be removed from a network.

Nodes with this NodeID seeking exclusion will be excluded from their network by the Z-Wave API
Module. Nodes with a different NodeID seeking exclusion will not be excluded from their network by
the Z-Wave API Module.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.136 after a specific
node removal operation is performed.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 155


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.136: Remove Specific Node From Network Command         Callback data frame


For fields description, refer to _Remove_ _Node_ _From_ _Network_ _Command_ _Callback_ _data_ _frame_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 156


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.6** **Is** **Node** **Failed** **Command**


This command is used to request if a given NodeID is considered as failed by the Z-Wave API Module.
Is Failed Node Command Identifier is 0x62.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.137 to check a given NodeID presence
in the Z-Wave API Module failed NodeID list.


Table 4.137: Is Failed Node Command          - Initial data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID that will be checked if it is stored in the controller failed
NodeID list.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.138.


Table 4.138: Is Failed Node Command          - Response data frame


FailedNodeID presence (8 bits)

This field is used to advertise the presence of a given NodeID in controller failed NodeID list. This
field MUST be encoded as follow:

 - The field value MUST be 0x00, if the NodeID is not stored in the controller failed NodeID list.

 - The field value MUST be 0x01, if the NodeID is stored in the controller failed NodeID list.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 157


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 158


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.7** **Remove** **Failed** **Node** **Command**


This command is used to request a non-responding node removal operation from the controller routing
table. When a node is non-responding, its’ NodeID shall be included in the failed NodeID list. If the
node responding again it shall be removed from the failed NodeID list. A failed node MUST only be
removed if the NodeID is in the failed NodeID list and extra precaution shall be considered before
the failed node is removed. A responding node MUST NOT be removed. The Remove Failed Node
Command Identifier is 0x61.

Note that this command MUST only be used by Primary Controller and an Inclusion Controller.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.139 to trigger a failed node removal
from the controller routing table.


Table 4.139: Remove Failed Node Command         - Initial data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID of a failed node that will be removed from the routing table.
This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.140.


Table 4.140: Remove Failed Node Command - Response data frame


Remove Failed Node Response Status (8 bits)

This field is used to indicate the Z-Wave module response regarding the remove failed node request.
This field MUST be encoded according to Table 4.141.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 159


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.141: Remove Failed Node Response Status value encoding


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.142 to notify the
application regarding the failed node removal operation status.


Table 4.142: Remove Failed Node Command - Callback data frame


Session identifier (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .

Remove Failed Node Operation Status (8 bits)

This field is used to notify the status of failed node removal operation. This field MUST be encoded
according to Table 4.143.


Table 4.143: Remove Failed Node Operation Status value encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 160


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.8** **Replace** **Failed** **Node** **Command**


This command is used to replace a non-responding node with a new node. Responding nodes MUST
NOT be replaced. The Replace Failed Node Command Identifier is 0x63.

Note that this command MUST only be used by Primary Controller and an Inclusion Controller.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .

Figure 4.16 shows an example of a successful failed node replacement.


Figure 4.16: Replace Failed Node Success Example


Figure 4.17 shows an example of an unsuccessful failed node replacement.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 161


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.17: Replace Failed Node Example


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.144 to replace a failed node with a
new node.


Table 4.144: Replace Failed Node Command         - Initial data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID of a failed node that will be assigned to a new node.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 162


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.145.


Table 4.145: Replace Failed Node Command - Response data frame


Replace Failed Node Response Status (8 bits)

This field is used to indicate the Z-Wave module response regarding the replace failed node request.
This field MUST be encoded according to Table 4.146.


Table 4.146: Remove Failed Node Response Status value encoding


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.147


Table 4.147: Replace Failed Node Command - Callback data frame


Session identifier (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .

Replace Failed Node Operation Status (8 bits)

This field is used to notify the status of replace failed node operation. This field MUST be encoded
according to Table 4.148.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 163


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.148: Replace Failed Node Operation Status value encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 164


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.9** **Delete** **Return** **Route** **Command**


This command is used to request the deletion of the static return routes. The Delete Return Route
Command Identifier is 0x47.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.149.


Table 4.149: Delete Return Route Command         - Initial data frame


NodeID (8/16 bits)

This field is used to indicates the NodeID for which the static return routes is requested to be deleted.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.150.


Table 4.150: Delete Return Route Command - Response data frame


Delete Return Route Response (8 bits)

This field is used to advertise the response of the Z-Wave module regarding the acceptance of the
_Delete_ _Return_ _Route_ _Command_ _Initial_ _data_ _frame_ . This field MUST be encoded as follow:

 - If delete return route operation is started, this field value MUST be set to 0x01.

 - If an “assign/delete return route” operation is already active, this field value MUST be set to
0x00.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 165


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.151.


Table 4.151: Delete Return Route Command - Callback data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 166


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.10** **Assign** **Return** **Route** **Command**


This command is used to assign return routes to end nodes in a network. Refer to [zwave_nwk_spec]
for details. The Assign Return Route Command Identifier is 0x46.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.152.


Table 4.152: Assign Return Route Command         - Initial data frame


NodeID (8 bits/16 bits)

This field is used to indicate the NodeID for which the return route for the destination must be
assigned by the Z-Wave API Module.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Destination NodeID (8 bits/16 bits)

This field is used to indicate the Destination NodeID for which the return route must be assigned by
the Z-Wave API Module.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.153


Table 4.153: Assign Return Route Command         - Response data
frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 167


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.154


Table 4.154: Assign Return Route Command - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 168


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.11** **Assign** **SUC** **Return** **Route** **Command**


This command is used to Assign a Return Route to the SUC NodeID.

The Assign SUC Return Route Command Identifier is 0x51


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.155


Table 4.155: Assign SUC Return Route Command         - Initial data
frame


NodeID (8 bits/16 bits)

This field is used to indicate the NodeID for which the return route for the SUC must be assigned by
the Z-Wave API Module.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.156


Table 4.156: Assign SUC Return Route Command - Response data
frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 169


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.157


Table 4.157: Assign SUC Return Route Command - Callback data
frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 170


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.12** **Assign** **Priority** **Return** **Route** **Command**


This command is used to assign priority route to end nodes. An end node MUST always use the
priority route for the first transmission attempt. Refer to [zwave_nwk_spec] for details. The Assign
Priority Return Route Command Identifier is 0x4F.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.158.


Table 4.158: Assign Priority Return Route Command - Initial data
frame


NodeID (8/16 bits)

This field is used to advertise the NodeID of the end node which shall receive defined priority route.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Route Destination NodeID (8/16 bits)

This field is used to indicate the destination NodeID which the end node shall use the defined priority
route while transmitting a packet to it.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Repeater (4 bytes)

Refer to _Repeater_ _(4_ _bytes)_ .

Route Speed (8 bits)

Refer to _Route_ _Speed_ _(8_ _bits)_ .

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 171


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.159.


Table 4.159: Assign Priority Return Route Command         - Response
data frame


Assign Priority Route Response (8 bits)

This field is used to advertise the response of the Z-Wave API module regarding the acceptance of the
_Assign_ _Priority_ _Return_ _Route_ _Command_ _Initial_ _data_ _frame_ . This field MUST be encoded as follow:

 - If assign priority return route operation is started, this field value MUST be set to 0x01.

 - If an “assign/delete return route” operation is already active, this field value MUST be set to
0x00.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.160.


Table 4.160: Assign Priority Return Route Command         - Callback
data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 172


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.13** **Assign** **Priority** **SUC** **Return** **Route** **Command**


This command is used to assign a priority return route to reach the SUC NodeID. The Assign Priority
SUC Return Route Command Identifier is 0x58.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.161.


Table 4.161: Assign Priority SUC Return Route Command - Initial
data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID of the end node which shall receive defined priority route
to reach SUC/SIS.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Repeater (4 bytes)

Refer to _Repeater_ _(4_ _bytes)_ .

Route Speed (8 bits)

Refer to _Route_ _Speed_ _(8_ _bits)_ .

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.162.


Table 4.162: Assign Priority SUC Return Route Command         - Response data frame


Assign Priority SUC Route Response (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 173


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to advertise the response of the Z-Wave API module regarding the acceptance of
the _Assign_ _Priority_ _SUC_ _Return_ _Route_ _Command_ _Initial_ _data_ _frame_ . This field MUST be encoded as
follow:

 - If assign priority SUC return route operation is started, this field value MUST be set to 0x01.

 - If an “assign/delete return route” operation is already active, this field value MUST be set to
0x00.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.163.


Table 4.163: Assign Priority SUC Return Route Command         - Callback data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 174


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.14** **Set** **Priority** **Route** **Command**


This command is used to set the Priority Route for a destination node. The Priority Route is the
route that shall be used as the first routing attempt by the Z-Wave protocol when transmitting to a
node. The existing Priority Route will be removed if the four byte list of Repeaters and Route Speed
are omitted. The Priority Route is expected to be stored in NVM of the Z-Wave module. The Set
Priority Route Command Identifier is 0x93.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.164 to set the Priority Route.


Table 4.164: Set Priority Route Command         - Initial data frame


NodeID (8/16 bits)

This field is used to indicate the destination NodeID for which the Priority Route is set to.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Repeater (4 bytes)

The Priority Route will be removed if these fields and the _Route_ _Speed_ are omitted. Refer to _Repeater_
_(4_ _bytes)_ .

Route Speed (8 bits)

The Priority Route will be removed if this field and the _Repeater_ are omitted. Refer to _Route_ _Speed_
_(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.165.


Table 4.165: Set Priority Route Command         - Response data frame


NodeID (8/16 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 175


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to indicate the destination NodeID for which the Priority Route attempted to be
set.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 176


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.15** **Get** **Priority** **Route** **Command**


This command is used to request the priority route that is defined in the Z-Wave API module. If
a route has been set to the module using _Set_ _Priority_ _Route_ _Command_, the module MUST provide
the priority route using _Get_ _Priority_ _Route_ _Command_ Response frame. If no priority route has
been set in the module, the _Get_ _Priority_ _Route_ _Command_ Response frame MUST contain either the
Last Working Route (LWR) or the Next to Last Working Route (NLWR). The Get Priority Route
Command Identifier is 0x92.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.166.


Table 4.166: Get Priority Route Command         - Initial data frame


NodeID (8/16 bits)

This field is used to indicate the destination NodeID for which the Priority Route is requested for.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.167.


Table 4.167: Get Priority Route Command         - Response data frame


NodeID (8/16 bits)

This field is used to indicate the destination NodeID for which the Priority Route corresponds to.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Route Kind (8 bits)

This field is used to advertise which kind of route was returned. The field MUST be encoded according
to Table 4.168.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 177


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.168: Get Priority Route Command - Route Kind encoding


Repeater (4 bytes)

Refer to _Repeater_ _(4_ _bytes)_ .

Route Speed (8 bits)

Refer to _Route_ _Speed_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 178


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.16** **Get** **Neighbor** **Table** **Line** **Command**


This command is used to request a line from the controller neighbor table.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.169.


Table 4.169: Get Neighbor Table Line Command         - Initial data
frame


NodeID (8 bits)

This field is used to indicate the destination NodeID for which the Neighbor Table Line is requested
for.

Remove Bad Link (1 bit)

If this bit is set, the controller will remove the latest bad link from the neighbor table line.

Remove Non Repeaters (1 bit)

If this bit is set, the controller will remove non repeaters from the neighbor table line. Repeaters nodes
have Listening bit and Routing bit set in the Node Information Frame. Others are non repeaters.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.170.


Table 4.170: Get Neighbor Table Line Command         - Response data
frame


Node Mask (29 bytes)

This field is used to indicate the bit mask of the node neighbors in a Z-Wave network. The field value
MUST be encoded according to:

 - If bit _𝑛_ in the NodeMask byte _𝑖_ is 1, it indicates that node _𝑖_ _*_ 8+ _𝑛_ +1 is a neighbor of the node.

 - If bit _𝑛_ in the NodeMask byte _𝑖_ is 0, it indicates that node _𝑖_ _*_ 8 + _𝑛_ + 1 is not a neighbor of the
node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 179


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 180


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.17** **Lock** **Unlock** **Last** **Route** **Command**


This command is used to lock or unlock all last working route. The Lock Unlock Last Route Command
Identifier is 0x90.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.171.


Table 4.171: Lock Unlock Last Route Command         - Initial data
frame


Lock mode (8 bits)

This command is used to indicate if the last working routes MUST be saved in the Z-Wave API
module. This field value MUST be encoded as follows:

 - The value MUST be set to 0x01, if the last working routes MUST be saved in the Z-Wave API
module.

 - The value MUST be set to 0x00, if the last working routes MUST NOT be saved in the Z-Wave
API module.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 181


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.18** **Get** **Routing** **Table** **Entries** **Command**


This command is used to request a entries from the controller routing table.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.172.


Table 4.172: Get Routing Table Entries Command         - Initial data
frame


NodeID (8 bits)

This field is used to indicate the destination NodeID for which the Routing Table Entries is requested
for.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.173.


Table 4.173: Get Routing Table Entries Command - Response data
frame


Routes Count (1 byte)

This field is used to indicate the number of route table entries reported for this node.

Routes N Type (1 byte)

This field is used to indicate the type of route table entry. This field MUST be encoded according to
Table 4.174. All other values are reserved.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 182


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.174: Z-Wave API Get Routing Table Entry Command         Route Type


Routes N Beam (2 bits)

This field is used to indicate the beam type used with this route table entry. This field MUST be
encoded according to Table 4.175. All other values are reserved.


Table 4.175: Z-Wave API Get Routing Table Entry Command         Route Beam Type


Routes N Speed (2 bits)

This field is used to indicate the speed used with this route table entry. This field MUST be encoded
according to Table 4.176. All other values are reserved.


Table 4.176: Z-Wave API Get Routing Table Entry Command         Route Speed Type


Routes N Hop M (1 byte)

This field is used to indicate the Mth hop of the route table entry.

Zero means the end of the route. All subsequent hop fields should also be be zero for this route.

A route with all hops equal to zero means direct range communication.


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 183


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.19** **Set** **SUC** **NodeID** **Command**


This command is used to configure a static/bridge controller to be a SUC/SIS node or not. The
Primary Controller should use this function to set a static/bridge controller to be the SUC/SIS node.
The Set SUC NodeID Command Identifier is 0x54.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.177.


Table 4.177: Set SUC NodeID Command          - Initial data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID of the controller node that MUST take the SUC/SIS node.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

SUC state (8 bits)

This field is used to enable/disable the SUC/SIS functionalities. The field MUST be encoded as follow:

 - If the static/bridge controller are targeted to be a SUC/SIS node, the field value MUST be set
to 0x01.

 - If the static/bridge controller should not be a SUC/SIS node, the field value MUST be set to
0x00.

Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Capabilities (8 bits)

This field is used to advertise the SUC capabilities that can be enabled on the Z-Wave API module.
This field MUST be encoded according to Table 4.178.


Table 4.178: Set SUC NodeID Capabilities Value encoding


Session identifier (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 184


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.179.


Table 4.179: Set SUC NodeID Command         - Response data frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.180.


Table 4.180: Set SUC NodeID Command         - Callback data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Set SUC Status (8 bits)

This field is used to indicate the statue regarding the configuration of a static/bridge controller to be
SUC/SIS node. This field MUST be encoded according to Table 4.181.


Table 4.181: Set SUC NodeID Status Value encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 185


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.20** **Delete** **SUC** **Return** **Route** **Command**


This command is used to request the deletion of the SUC/SIS return routes. The Delete Return Route
Command Command Identifier is 0x55.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.182.


Table 4.182: Delete SUC Return Route Command Command         Initial data frame


NodeID (8/16 bits)

This field is used to indicates the NodeID for which the SUC return routes is requested to be deleted.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.183.


Table 4.183: Delete SUC Return Route Command Command         Response data frame


Delete SUC Return Route Response (8 bits)

This field is used to advertise the response of the Z-Wave module regarding the acceptance of the
_Delete_ _SUC_ _Return_ _Route_ _Command_ _Initial_ _data_ _frame_ . This field MUST be encoded as follow:

 - If delete SUC return route operation is started, this field value MUST be set to 0x01.

 - If an “assign/delete return route” operation is already active, this field value MUST be set to
0x00.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 186


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.184.


Table 4.184: Delete SUC Return Route Command Command         Callback data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 187


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.21** **Send** **SUC** **NodeID** **Command**


This command is used to trigger the transfer of SUC/SIS NodeID from Primary/Static controller to
a given controller NodeID. The Send SUC NodeID Command Identifier is 0x57.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.185.


Table 4.185: Send SUC NodeID Command         - Initial data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID of a controller that will receive the current SUC/SIS NodeID.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.186


Table 4.186: Send SUC NodeID Command         - Response data frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 188


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.187.


Table 4.187: Send SUC NodeID Command         - Callback data frame


Session identifier(8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 189


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.22** **Enable** **Node** **NLS** **command**


This command is used to enable the state of network layer security (NLS) of an included node. NLS
state cannot be disabled after it has been enabled. The Enable Node NLS command Identifier is
0x6A.

The NLS state set with this command MUST be persisted in NVM.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.188.


Table 4.188: Enable Node NLS State Command - Initial data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID. A Z-Wave module receiving this command with its own
node ID should enable NLS.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.189.


Table 4.189: Enable Node NLS command         - Response data frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 190


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.23** **Get** **Node** **NLS** **State** **command**


This command is used to get the state of network layer security (NLS) on a node. The Get Node NLS
State command Identifier is 0x6B.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.190.


Table 4.190: Get Node NLS State Command         - Initial data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.191.


Table 4.191: Get Node NLS State command - Response data frame


NLS support (8 bits)

This field is used to advertise the support of NLS on the designated NodeID.

This field MUST be encoded according to Table 4.192. All other values are reserved.


Table 4.192: Z-Wave API Get Node NLS State Command         - NLS
Support


NLS state (8 bits)

This field is used to advertise the state of NLS on the designated NodeID.

A Z-Wave module receiving an initial data frame with it’s own node ID should issue a response data
frame with this field set to 1 if one or more nodes have NLS enabled on the network.

This field MUST be encoded according to Table 4.193. All other values are reserved.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 191


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.193: Z-Wave API Get Node NLS State Command         - NLS
State


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 192


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.24** **Request** **Node** **Neighbor** **Discovery** **Command**


This command is used to request a node to perform a new neighbor discovery and receive the updated
list of neighbors. The requested node will also try to discover FL nodes. The Request Node Neighbor
Discovery Command Identifier is 0x48.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .

This command may trigger several callback frames. Examples are given in Figure 4.18 and Figure
4.19


Figure 4.18: Request Node Neighbor Discovery Command Success Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 193


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.19: Request Node Neighbor Discovery Command Fail Example


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.194


Table 4.194: Request Node Neighbor Discovery Command - Initial
data frame


NodeID (8/16 bits)

This field indicates the NodeID that must perform a new discovery of its neighbors.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 194


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.195


Table 4.195: Request Node Neighbor Discovery Command         - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Neighbor Discovery Status (8 bits)

This field is used to indicate the current status of the Neighbor Discovery Process. Refer to

[zwave_nwk_spec] for details about the Neighbor Discovery Process.

This field MUST be encoded as a bitmask and according to Table 4.196


Table 4.196: Request Node Neighbor Discovery Command - Neighbor Discovery Status encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 195


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.25** **Request** **Node** **Type** **Neighbor** **Update** **Command**


This command is used to request a node to perform a new neighbor update and receive the updated
list of neighbors.

When using the command with Node Type 0x00, and 0x01, it will work as a normal neighbor update.

When using the command with Node Type 0x02, then the API will work as follow:

When the API is called with the node-id of the listening node and the nodes to discovery are FLIRS
nodes

1. Controller will send FIND NODES IN RANGE for each FLIRS node in the network where the
listening node is the only node in the bitmask

2. The Controller will create node-id bitmask for each FLIRS node that can reach the listening
node

3. The controller will update the routing info for the listening node

The Request Node Type Neighbor Update Command Identifier is 0x68.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .

This command may trigger several callback frames. Examples are given in Figure 4.18 and Figure
4.19


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.197


Table 4.197: Request Node Type Neighbor Update Command         Initial data frame


NodeID (8/16 bits)

This field indicates the NodeID that must perform a new discovery of its neighbors.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Node Type (8 bits)

This field indicates the type of Neighbor Discovery to perform. This field MUST be encoded according
to Table 4.198.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 196


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.198: Request Node Type Neighbor Update Command         Node Type encoding


NOTE: Node Type 0x02 can only be used for listening nodes.


Figure 4.20: Request Node Type Neighbor Update Command with Node Type FLiRS Example


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 197


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.199


Table 4.199: Request Node Type Neighbor Update Command         Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Neighbor Discovery Status (8 bits)

This field is used to indicate the current status of the Neighbor Discovery Process. Refer to

[zwave_nwk_spec] for details about the Neighbor Discovery Process.

This field MUST be encoded as a bitmask and according to Table 4.200


Table 4.200: Request Node Type Neighbor Update Command         Neighbor Discovery Status encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 198


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.26** **Request** **Network** **Update** **Command**


This command is used to instruct the Z-Wave API Module to request an Automatic Controller Update
to the SUC. The Request Network Update Command Identifier is 0x53.

A host application SHOULD use this command only if there is a SUC in the current network.

A Z-Wave API Module receiving Node information updates during the Automatic Controller Update
process MUST issue unsolicited _Application_ _Update_ _Command_ to the host application.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .

This command MAY trigger additional unsolicited frames from the Z-Wave API Module. An example
of the expected frame flow is shown in Figure 4.21


Figure 4.21: Request Network Update Command Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 199


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.201.


Table 4.201: Request Network Update Command         - Initial data
frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.202.


Table 4.202: Request Network Update Command         - Response data
frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.203


Table 4.203: Z-Wave API Setup Set NodeID Base Type Sub Command       - Callback data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Network Update Status (8 bits)

This field is used to advertise the outcome of the network update request. This field MUST be encoded
according to Table 4.204.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 200


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.204: Network Update Status Value encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 201


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.27** **Set** **Virtual** **Node** **To** **Learn** **Mode** **Command**


This command is used to enable or disable a virtual end node to _Learn_ _Mode_ operation that facilitates
the node to be included or removed to/from a Z-Wave Network. The Set Virtual Node Learn Mode
Command Identifier is 0xA4.

This command MUST only be supported by nodes implementing a Bridge Controller library type
(refer to Table 4.39).

NOTE: A _Learn_ _Mode_ should only be enabled on a virtual end node when necessary, and it should
always be disabled again as quickly as possible. It is recommended that the _Learn_ _Mode_ should not
enabled for more than 1 second on a virtual end node.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.205.


Table 4.205: Set Virtual Node To Learn Mode Command         - Initial
data frame


NodeID (8 bits)

This field is used to advertise the virtual NodeID that is set to _Learn_ _Mode_ .

This field MUST be encoded using 8 bits regardless of the configured NodeID base Type. Refer to
_Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Mode (8 bits)

This field is used to indicate the _Learn_ _Mode_ intent. This field MUST be encoded according to Table
4.206.


Table 4.206: Virtual End Node Learn Mode Encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 202


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.207.


Table 4.207: Set Virtual Node To Learn Mode Command         - Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.208 to notify the
status of the _Learn_ _Mode_ operation.


Table 4.208: Set Virtual Node To Learn Mode Command - Callback
data frame


Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Status (8 bits)

This field is used to indicate the status of the _Learn_ _Mode_ process. This field MUST be encoded
according to Table 4.209.


Table 4.209: Virtual End Node Learn Mode Status Encoding


Original NodeID (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 203


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to advertise the original NodeID of the virtual end node when it was set to _Learn_
_Mode_ operation.

This field MUST be encoded using 8 bits regardless of the configured NodeID base Type. Refer to
_Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

New NodeID (8 bits)

This field is used to advertise the new assigned NodeID. If the virtual end node is deleted, this field
MUST be set to 0x00.

This field MUST be encoded using 8 bits regardless of the configured NodeID base Type. Refer to
_Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 204


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.28** **Virtual** **Node** **Send** **Node** **Information** **Command**


This command is used to create and transmit a virtual end node _Node_ _Information_ _Frame_ . The
Virtual Node Send Node Information Command Identifier is 0xA2.

This command MUST only be supported by nodes implementing a Bridge Controller library type
(refer to Table 4.39).


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.210.


Table 4.210: Virtual Node Send Node Information Command         Initial data frame


Source NodeID (8/16 bits)

This field is used to indicate the virtual NodeID where the _Node_ _Information_ _Frame_ is sent from. The
field size could be 8 bits or 16 bits depends on employed physical layer module such as Z-Wave or
Z-Wave Long Range, respectively.

Destination NodeID (8/16 bits)

This field is used to indicate the destination NodeID where the _Node_ _Information_ _Frame_ will be sent
to. The field size could be 8 bits or 16 bits depends on employed physical layer module such as Z-Wave
or Z-Wave Long Range, respectively.

Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Session identifier(8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.211.


Table 4.211: Virtual Node Send Node Information Command         Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 205


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.212 after the _Node_
_Information_ _Frame_ transmission is performed.


Table 4.212: Virtual Node Send Node Information Command         Callback data frame


Session identifier(8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 206


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.29** **Set** **Virtual** **Nodes** **Application** **Node** **Information** **Command**


This command is used to configure the Node Information Data for the Virtual nodes own by the
Z-Wave API Module. The Set Virtual Node Application Node Information Command Identifier is
0xA0.

This command MUST only be supported by nodes implementing a Bridge Controller library type
(refer to Table 4.39). The frame flow for this command is an _Acknowledged_ _frame_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.213


Table 4.213: Set Virtual Nodes Application Node Information
Command


Virtual NodeID (8 bits)

This field is used to indicate the virtual NodeID for which the Node information frame data must be
configured.

This field MUST be encoded using 8 bits regardless of the configured NodeID base Type. Refer to
_Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Device Option Mask (8 bits)

The device option mask is a bitmask where Listening and Optional functionality flags MUST be set
accordingly to the nodes capabilities. This field MUST comply with the format indicated in Table
4.214.


Table 4.214: Set Application Node Information Command - Device
Option Mask encoding


Generic Device Type (8 bits)

The Generic Device Class field contains an identifier that identifies what Generic Device Class the
Z-Wave node MUST advertise and MUST be set by the application. For a detailed description of all
available Generic Device Classes, refer to [device_class_spec] for Z-Wave devices, [device_type_spec]
for Z-Wave Plus devices, and [device_type_spec_v2] for Z-Wave Plus v2 devices.

Specific Device Type (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 207


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


The Specific Device Class field contains an identifier that identifies what Specific Device Class the
Z-Wave node MUST advertise and MUST be set by the application. For a detailed description of all
available Generic Device Classes, refer to [device_class_spec] for Z-Wave devices, [device_type_spec]
for Z-Wave Plus devices, and [device_type_spec_v2] for Z-Wave Plus v2 devices.

Node Parameter length (8 bits)

This field MUST specify the length of the Node Parameter field in bytes.

Node Parameter (N bytes)

This field is used to advertise the list of supported Command Classes by the node.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 208


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.30** **Set** **Z-Wave** **Long** **Range** **Shadow** **NodeIDs** **Commmand**


This command is used to enable the use of Shadow NodeIDs in the Long Range capable controller.
The command will enable the controller to use more NodeIDs than its native NodeID to transmit and
receive frames. The shadow NodeID is assigned outside of the normal NodeID range for Z-Wave Long
Range nodes.

The Set Z-Wave Long Range Shadow NodeIDs Commmand Identifier is 0xDD.

This command MUST only be supported by Z-Wave API Module using the Controller Bridge library
types (refer to Table 4.39).


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.215


Table 4.215: Set Z-Wave Long Range Shadow NodeIDs Command

            - Initial data frame


Z-Wave Long Range Shadow NodeIDs bitmask (8 bits)

This field is used to indicate which shadow NodeIDs must be enabled by the Z-Wave API Module.

This field MUST encoded as a bitmask and interpreted as follow:

 - bit 0 MUST represent NodeID 4002.

 - bit 1 MUST represent NodeID 4003.

 - bit 2 MUST represent NodeID 4004.

 - bit 3 MUST represent NodeID 4005.

 - bit 4..7 are reserved.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 209


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.4.3.31** **Transfer** **Protocol** **Command** **Class** **command**


This command is used by the host application to transfer a protocol command to the Z-Wave API
module. The host application should drop the frame if received below highest security level. The
Transfer Protocol Command Class Command Identifier is 0x69.


**Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ . This commmand should
be sent on decryption of a Protocol Command Class by the host. An example flow is show in Figure
4.22


Figure 4.22: Transfer Protocol Command Class usage


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 210


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**1.** **Initial** **data** **frame** **(Host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.216.


Table 4.216: Transfer Protocol Command Class - Initial data frame


Source NodeID (8/16 bits)

This field is used to advertise the source node ID.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Decryption Key (8 bits)

This field is used to advertise the key used for decryption. This field MUST be encoded according to
Table 4.217


Table 4.217: Transfer Protocol CC            - Decryption Key


Payload Length (8 bits)

This field is used to advertise the length in bytes of the _Payload_ field

Payload (N bytes)

This field is used to report the decrypted payload.


**2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.218.


Table 4.218: Transfer Protocol Command Class         - Response data
frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 211


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 212


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.5 Z-Wave API Memory Commands


This section describes _Z-Wave_ _API_ _Commands_ that are used to interact with the Z-Wave Module
memory or storage.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 213


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.5.1** **Get** **Network** **IDs** **from** **Memory** **Command**


This command is used to get the HomeID and NodeID from the Z-Wave Module. The Get Network
IDs from Memory Command Identifier is 0x20.


**4.5.1.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.5.1.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.219


Table 4.219: Get Network IDs from Memory Command         - Initial
data frame


**4.5.1.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.220


Table 4.220: Get Network IDs from Memory Command - Response
data frame


HomeID (4 bytes)

This field is used to advertise the current HomeID of the Z-Wave API Module.

NodeID (8 bits/16 bits)

This field is used to indicate the NodeID currently assigned to the Z-Wave API Module.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**4.5.1.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 214


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.6 Z-Wave API Firmware Update Commands


This section describes _Z-Wave_ _API_ _Commands_ that are used to perform firmware update operations.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 215


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.6.1** **Firmware** **Update** **Command**


This command is used to perform Z-Wave API Module firmware and bootloader update.

The Firmware Update Command Identifier is 0x3E.


**4.6.1.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .

This command has sub-commands that allow writing part of the firmware/bootloader and perform
the update.

The recommended frame flow for restoring the network data of a Z-Wave API module is shown in
Figure 4.23


Figure 4.23: Firmware Update


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 216


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.6.1.2** **Sub** **Commands**


Supported Sub Commands are listed in _Firmware_ _Update_ _Sub_ _Commands_ .


Table 4.221: Firmware Update Sub Commands


**4.6.1.3** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.222.


Table 4.222: Firmware Update Command         - Prepare Initial data
frame


Sub Command (8 bits)

This field MUST be set to 0x00 in accordance to _Sub_ _Commands_ .


**4.6.1.4** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.223


Table 4.223: Firmware Update Command         - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x00 in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.224


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 217


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.224: Firmware Update Command         - Firmware Update status


None.


**4.6.1.5** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.225.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 218


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.225: Firmware Update Command         - Extended Initial data
frame


Sub Command (8 bits)

This field MUST be set to 0x01 in accordance to _Sub_ _Commands_ .

Offset (32 bits)

This field specifies the offset of the chunk to write from the beginning of the file.

Data Length (16 bits)

This field specifies the size of the chunk to write.

Data (N bytes)

This field provides firmware chunk to be written.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field.


**4.6.1.6** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.226


Table 4.226: Firmware Update Command         - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x01 in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.224


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 219


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.6.1.7** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.6.1.8** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.227.


Table 4.227: Firmware Update Command - Perform Update Initial
data frame


Sub Command (8 bits)

This field MUST be set to 0x02 in accordance to _Sub_ _Commands_ .

Update target (8 bits)

This field MUST be set in accordance to _Firmware_ _Update_ _Target_ to initiate firmware or bootloader
update.


Table 4.228: Firmware Update Target


**4.6.1.9** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.229


Table 4.229: Firmware Update Command         - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x02 in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.224


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 220


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.6.1.10** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.

## 4.7 Z-Wave API Backup and Restore Commands


This section describes _Z-Wave API Commands_ that are used to perform backup and restore operations.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 221


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.1** **Network** **Restore** **Command**


This command is used to write the firmware data of the Z-Wave API Module in an
implementation-independent way. It has the same purpose as _Extended_ _NVM_ _Operations_ _Command_
and _NVM_ _Operations_ _Command_, but this command does not rely on a specific NVM memory layout
and provides more interoperability between SDK versions and vendors.

If supported, the host should use this command instead of the legacy NVM Operations command and
Extended NVM Operations Command.

The Network Restore Command Identifier is 0x2F.


**4.7.1.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .

This command has sub-commands that allow restoring devices, home ID and node ID.

The recommended frame flow for restoring the network data of a Z-Wave API module is shown in
Figure 4.24


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 222


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


~~Figure~~ ~~4.24:~~ ~~Network~~ ~~Restore~~
© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 223


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


A _Set_ _Default_ _Command_ command should be called before starting the Network Restore sequence to
clear previous devices from memory.


**4.7.1.2** **Sub** **Commands**


Supported sub commands are listed in _Network_ _Restore_ _Sub_ _Commands_ .


Table 4.230: Network Restore Sub Commands


**4.7.1.3** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.231.


Table 4.231: Network Restore Command         - Extended Initial data
frame


Sub Command (8 bits)

This field MUST be set to 0x00 in accordance to _Sub_ _Commands_ .


**4.7.1.4** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.232


Table 4.232: Network Restore Command         - Response data frame


Sub Command (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 224


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field MUST be set to 0x00 in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.233


Table 4.233: Network Restore Command         - Network Restore status


**4.7.1.5** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.7.1.6** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.234.


Table 4.234: Network Restore Command         - Extended Initial data
frame


Sub Command (8 bits)

This field MUST be set to 0x01 in accordance to _Sub_ _Commands_ .

Home ID (32 bits)

This field is used to indicate the network home ID to use after restore.

Controller Node ID (8 bits)

This field is used to indicate the Controller’s own node ID to use after restore.

This field MUST NOT be encoded according to the configured NodeID base Type, but always use 1
byte notation. Refer to _Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 225


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.1.7** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.235


Table 4.235: Network Restore Command         - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x01 in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.233


**4.7.1.8** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.7.1.9** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.236.


Table 4.236: Network Restore Command         - Extended Initial data
frame


Sub Command (8 bits)

This field MUST be set to 0x02 in accordance to _Sub_ _Commands_ .

Node ID (8/16 bits)

This field is used to indicate the node ID for which the node information protocol data is restored.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Protocol Specific (40 bits)

This field is used to specify the Node Information protocol data.

Those five bytes represent bytes 5, 6, 7, 9 and 10 (in the same order) from the response of Get Node
Information Protocol Data Command as specified in _Get_ _Node_ _Information_ _Protocol_ _Data_ _Command_

_-_ _Response_ _data_ _frame_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 226


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.1.10** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.237


Table 4.237: Network Restore Command         - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x02 in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.233


**4.7.1.11** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.7.1.12** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.238.


Table 4.238: Network Restore Command         - Extended Initial data
frame


Sub Command (8 bits)

This field MUST be set to 0x03 in accordance to _Sub_ _Commands_ .

Node ID (8/16 bits)

This field is used to indicate the node ID for which the node information protocol data is restored.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Routing Table Line (232 bits)

This field is used to specify the list of Neighbours of Node ID. Bit set to 0 means not in neighbourhood,
bit set to 1 means devices are neighbours. Bit 0 represents node with ID 1, bit 1 represents node with
ID 2,… bit 231 represents node 232. Routing Table Line field is identical to the one reported by Get
Routing Table Line Command ( _Get_ _Neighbor_ _Table_ _Line_ _Command_ _-_ _Response_ _data_ _frame_ .).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 227


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.1.13** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.239


Table 4.239: Network Restore Command         - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x03 in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.233


**4.7.1.14** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.7.1.15** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.240.


Table 4.240: Network Restore Command         - Extended Initial data
frame


Sub Command (8 bits)

This field MUST be set to 0x04 in accordance to _Sub_ _Commands_ .

Node ID (8/16 bits)

This field is used to indicate the node ID for which the node information protocol data is restored.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 228


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Route Count, Route N Type, Route N Beam, Route N Speed, Route N Hop M

These fields are describing route entries and are identical to the set of fields reported by Get Routing
Table Entry Command ( _Get_ _Routing_ _Table_ _Entries_ _Command_ _-_ _Response_ _data_ _frame_ ).


**4.7.1.16** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.241


Table 4.241: Network Restore Command         - Response data frame


Sub Command (8 bits)

This field MUST be set to 0x04 in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.233


**4.7.1.17** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.7.1.18** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.242.


Table 4.242: Network Restore Command         - Extended Initial data
frame


Sub Command (8 bits)

This field MUST be set to 0xFF in accordance to _Sub_ _Commands_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 229


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.1.19** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.243


Table 4.243: Network Restore Command         - Response data frame


Sub Command (8 bits)

This field MUST be set to 0xFF in accordance to _Sub_ _Commands_ .

Response (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.233


**4.7.1.20** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 230


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.2** **NVM** **Operations** **Command**


This command is used to read and write the firmware data of the Z-Wave API Module. The NVM
Operations Command Identifier is 0x2E.

This command is considerd untrustworthy due to its implementation on part with 64Kbytes of NVM
(reporting a size of 0 because 0x10000 does not fit in 2 bytes). It should no longer be implemented
and replaced by _Network_ _Restore_ _Command_ or _Extended_ _NVM_ _Operations_ _Command_ .

Host could identify which command is available (Network Restore Commands, NVM Operations
Commands or NVM extended Operations Command) by using _Get_ _Capabilities_ _Command_


**4.7.2.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .

This command has sub-commands that allow either read or write operations.

The recommended frame flow for reading the firmware data of a Z-Wave API module is shown in
Figure 4.25


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 231


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.25: NVM Read Operation


The recommended frame flow for writing firmware data to a Z-Wave API module is shown in Figure
4.26. The host application MUST send a _Soft_ _Reset_ _Command_ in order to activate the new firmware.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 232


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Figure 4.26: NVM Write Operation


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 233


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.2.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.244


Table 4.244: NVM Operations Command          - Initial data frame


NVM Operation sub-command (8 bits)

This field is used to indicate which operation to perform. This field MUST be encoded according to
Table 4.245


Table 4.245: NVM Operations Command         - NVM Operation
sub-command encoding


Firmware Data Length (8 bits)

This field is used to specify the length of the data that should be read/written from/to the Z-Wave
API firmware data.

This field SHOULD be omitted for if the _NVM Operation sub-command_ is set to Open (0x00) or Close
(0x03).

If the _NVM_ _Operation_ _sub-command_ is set to Write (0x02), this field MUST indicate the length of
the _Firmware_ _Data_ field, in bytes.

Address Offset (16 bits)

This field is used to specify a memory address offset for read/write operations.

This field SHOULD be omitted for if the _NVM Operation sub-command_ is set to Open (0x00) or Close
(0x03).

If the _NVM_ _Operation_ _sub-command_ is set to Read (0x01) or Write (0x02), this field MUST indicate
the address offset for which the data must be read/written.

Firmware Data (N bytes)

This field is used to specify data to write to the Z-Wave API Module firmware memory.

This field SHOULD be omitted for if the _NVM_ _Operation_ _sub-command_ is set to a different value
than Write (0x02).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 234


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


The Z-Wave API Module MUST write the data indicated in this field starting at the address offset
indicated by the _Address_ _Offset_ field.


**4.7.2.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.246


Table 4.246: NVM Operations Command         - Response data frame


NVM Operation sub-command status (8 bits)

This field is used to indicate the status of the requested operation in the initial data frame. This field
MUST be encoded according to Table 4.247


Table 4.247: NVM Operations Command         - NVM Operation
sub-command status encoding


Firmware Data Length (8 bits)

This field is used to specify the length of the data that is present in the _Firmware_ _Data_ field.

This field will be different than 0 only for Read (0x01) operation responses.

Address Offset / NVM Size (16 bits)

This field is used to specify a memory address offset for read/write operations.

This field SHOULD be ignored for if the _NVM Operation sub-command_ is set to Write (0x02) or Close
(0x03).

If the _NVM_ _Operation_ _sub-command_ was set to Read (0x01) in the 1. Initial Data Frame, this field
MUST indicate the address offset for which the data is being read.

If the _NVM_ _Operation_ _sub-command_ was set to Open (0x00) in the 1. Initial Data Frame, this field
MUST indicate the total size of the Firmware Memory, in bytes.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 235


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Firmware Data (N bytes)

This field is used to adverties the read data from the Z-Wave API Module firmware memory.

This field SHOULD be ignored for if the _NVM_ _Operation_ _sub-command_ was set not to Read (0x01)
in the 1. Initial Data Frame.


**4.7.2.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 236


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.3** **Extended** **NVM** **Operations** **Command**


This command is used to read and write the firmware data of the Z-Wave API Module. It has the
same purpose as the _NVM_ _Operations_ _Command_, but this command supports 32-bit addresses. If
supported, host should use this command instead of the legacy NVM Operations command. The
extended NVM Operations Command Identifier is 0x3D.

This command is considerd untrustworthy due to different NVM layouts in different SDK versions. It
should no longer be implemented and replaced by _Network_ _Restore_ _Command_ .

Host could identify which command is available (Network Restore Commands, NVM extended Operations Command) by using _Get_ _Capabilities_ _Command_


**4.7.3.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .

This command has sub-commands that allow either read or write operations.

The recommended frame flow for reading the firmware data of a Z-Wave API module is shown in
Figure 4.27


Figure 4.27: Extended NVM Read Operation


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 237


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


The recommended frame flow for writing firmware data to a Z-Wave API module is shown in Figure
4.28. The host application MUST send a _Soft_ _Reset_ _Command_ in order to activate the new firmware.


Figure 4.28: Extended NVM Write Operation


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 238


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.7.3.2** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.248


Table 4.248: Extended NVM Operations Command         - Extended
Initial data frame


Extended NVM Operation sub-command (8 bits)

This field is used to indicate which operation to perform. This field MUST be encoded according to
Table 4.249


Table 4.249: Extended NVM Operations Command         - Extended
NVM Operation sub-command encoding


Firmware Data Length (8 bits)

This field is used to specify the length of the data that should be read/written from/to the Z-Wave
API firmware data.

This field SHOULD be omitted if the _Extended_ _NVM_ _Operation_ _sub-command_ is set to Open (0x00)
or Close (0x03).

If the _Extended_ _NVM_ _Operation_ _sub-command_ is set to Write (0x02), this field MUST indicate the
length of the _Firmware_ _Data_ field, in bytes.

Address Offset (32 bits)

This field is used to specify a memory address offset for read/write operations.

This field SHOULD be omitted for if the _Extended_ _NVM_ _Operation_ _sub-command_ is set to Open
(0x00) or Close (0x03).

If the _Extended_ _NVM_ _Operation_ _sub-command_ is set to Read (0x01) or Write (0x02), this field MUST
indicate the address offset for which the data must be read/written.

Firmware Data (N bytes)

This field is used to specify data to write to the Z-Wave API Module firmware memory.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 239


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field SHOULD be omitted for if the _Extended_ _NVM_ _Operation_ _sub-command_ is set to a different
value than Write (0x02).

The Z-Wave API Module MUST write the data indicated in this field starting at the address offset
indicated by the _Address_ _Offset_ field.


**4.7.3.3** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.250


Table 4.250: Extended NVM Operations Command         - Response
data frame


Extended NVM Operation sub-command status (8 bits)

This field is used to indicate the status of the requested operation in the _Initial_ _data_ _frame_ _(host_ _→_
_Z-Wave_ _Module)_ . This field MUST be encoded according to Table 4.251


Table 4.251: Extended NVM Operations Command         - Extended
NVM Operation sub-command status encoding


Firmware Data Length (8 bits)

This field is used to specify the length of the data that is present in the _Firmware_ _Data_ field.

This field will be different than 0 for Open (0x00) and Read (0x01) operation responses.

Address Offset / NVM Size (32 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 240


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to specify a memory address offset for read/write operations.

This field SHOULD be ignored for if the _Extended_ _NVM_ _Operation_ _sub-command_ is set to Write
(0x02) or Close (0x03).

If the _Extended_ _NVM_ _Operation_ _sub-command_ was set to Read (0x01) in the _Initial_ _data_ _frame_ _(host_
_→Z-Wave_ _Module)_, this field MUST indicate the address offset for which the data is being read.

If the _Extended_ _NVM_ _Operation_ _sub-command_ was set to Open (0x00) in the _Initial_ _data_ _frame_ _(host_
_→Z-Wave_ _Module)_, this field MUST indicate the total size of the Firmware Memory, in bytes.

Firmware Data (N bytes)

This field is used to advertie the read data from the Z-Wave API Module firmware memory.

This field SHOULD be ignored if the _Extended_ _NVM_ _Operation_ _sub-command_ was set not to Open
(0x00) or Read (0x01) in the _Initial_ _data_ _frame_ _(host_ _→Z-Wave_ _Module)_ .

If the _Extended_ _NVM_ _Operation_ _sub-command_ was set to Read (0x01) in the _Initial_ _data_ _frame_ _(host_
_→Z-Wave_ _Module)_, this field MUST indicate the content of the NVM.

If the _Extended_ _NVM_ _Operation_ _sub-command_ was set to Open (0x00) in the _Initial_ _data_ _frame_ _(host_
_→Z-Wave_ _Module)_, this field MUST advertise the list of _Extended_ _NVM_ _Operation_ _sub-command_
supported by the product. This field MUST be encoded as a bitmask and interpreted as follow:

 - bit 0 in byte 11 must represent the _Extended_ _NVM_ _Operation_ _sub-command_ 0 (Open).

 - bit 1 in byte 11 must represent the _Extended_ _NVM_ _Operation_ _sub-command_ 1 (Read).

 - bit 2 in byte 11 must represent the _Extended_ _NVM_ _Operation_ _sub-command_ 2 (Write).

 - bit 3 in byte 11 must represent the _Extended_ _NVM_ _Operation_ _sub-command_ 3 (Close).

 - …

 - bit 7 in byte 11 must represent the _Extended_ _NVM_ _Operation_ _sub-command_ 7 (Reserved for
future usage).

 - bit 0 in byte 12 must represent the _Extended_ _NVM_ _Operation_ _sub-command_ 8 (Reserved for
future usage).

 - etc

Each of the bits MUST be interpreted as follow:

 - A bit set to 1 MUST indicate that the corresponding _Extended_ _NVM_ _Operation_ _sub-command_
is supported.

 - A bit set to 0 MUST indicate that the corresponding _Extended_ _NVM_ _Operation_ _sub-command_
is not supported.

The value of missing bytes MUST be assumed to be 0. eg: if only one data byte is sent by the device,
all _Extended_ _NVM_ _Operation_ _sub-command_ upper to 7 must be considered as not supported by the
product.


**4.7.3.4** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 241


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.8 Unsolicited Z-Wave API commands


This section describes _Z-Wave_ _API_ _Commands_ that are used to intialize and configure the Z-Wave
module. It also comprises commands that are used to read the supported functionality of the Z-Wave
API module.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 242


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.8.1** **Application** **Command** **Handler** **Command**


This command is used by a Z-Wave module to notify a host application that a Z-Wave frame has been
received. The Application Command Handler Command Identifier is 0x04


**4.8.1.1** **Frame** **flow**


The frame flow for this command is an _Unsolicited_ _frame_ .


**4.8.1.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


None


**4.8.1.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.8.1.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.8.1.5** **4.** **Unsolicited** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue an unsolicited frame formatted according to Table 4.252


Table 4.252: Application Command Handler Command         - Unsolicited data frame


Rx Status (8 bits)

This field is used to advertise additional information about how the Z-Wave frame was received.

This field MUST be treated as a bitmask and encoded according to Table 4.1.

Source NodeID (8/16 bits)

This field is used to advertise the NodeID from which the Z-Wave Command was received.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Payload Length (8 bits)

This field is used to advertise the length in bytes of the _Payload_ field.

Payload (N bytes)

This field is used to report the payload that was received from the Source NodeID.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 243


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Rx RSSI Value (8 bits)

This field is used to report the measured RSSI value for the received Z-Wave frame. This field MUST
be encoded according to Table 4.3.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 244


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.8.2** **Z-Wave** **API** **Started** **Command**


This command is used by the Z-Wave Module to indicate that it is ready to be operated after a reboot
or reset operation.

The Z-Wave API Started Command Command Identifier is 0x0A


**4.8.2.1** **Frame** **flow**


The frame flow for this command is an _Unsolicited_ _frame_ .


**4.8.2.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


None


**4.8.2.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.8.2.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.8.2.5** **4.** **Unsolicited** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue an unsolicited frame formatted according to Table 4.253


Table 4.253: Z-Wave API Started Command         - Unsolicited data
frame


Wake Up Reason (8 bits)

This field is used to advertise the event that caused the Z-Wave API module to start. It MUST be
encoded according to Table 4.254.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 245


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.254: Z-Wave API Started         - Wake Up Reason encoding


Watchdog Started (8 bits)

This field is used to advertise if the Watchdog is enabled.

The value 0x00 MUST indicate that the watchdog is disabled. The value 0x01 MUST indicate that
the watchdog is enabled.

Device Option Mask (8 bits)

This field is used to advertise the currently configured listening capabilities configured for the Z-Wave
API Module.

The host application MAY change this using the _Set_ _Application_ _Node_ _Information_ _Command_ .

Generic Device Type (8 bits)

This field is used to advertise the currently configured Generic Device Type.

The host application MAY change this using the _Set_ _Application_ _Node_ _Information_ _Command_ .

Specific Device Type (8 bits)

This field is used to advertise the currently configured Specific Device Type.

The host application MAY change this using the _Set_ _Application_ _Node_ _Information_ _Command_ .

Command Class List Length (8 bits)

This field is used to advertise the length of the _Command_ _Class_ _List_ in bytes.

Command Class List (N bytes)

This field is used to advertise the list of supported Command Classes advertised by the Z-Wave API
Module upon request.

The host application MAY change this using the _Set_ _Application_ _Node_ _Information_ _Command_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 246


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Supported Protocols (8 bits)

This field is used to advertise additional supported protocols by the Z-Wave API module. This field
MUST be encoded as a bitmask and MUST be encoded according to Table 4.255.


Table 4.255: Z-Wave API Started Command - Supported Protocols
encoding







Manufacturer ID (16 bits)

This field is mandatory when the field /Reset Information/ is used, otherwise it is optional. In
this frame, the /Manufacturer ID/ is used to create namespace to avoid collisions between vendors. The /Manufacturer ID/ corresponds to the Z-Wave manufacturer ID [(https://github.com/](https://github.com/Z-Wave-Alliance/zwave_xml/blob/main/zw_manufacturers.xml)
[Z-Wave-Alliance/zwave_xml/blob/main/zw_manufacturers.xml),](https://github.com/Z-Wave-Alliance/zwave_xml/blob/main/zw_manufacturers.xml) that is assigned by the Z-Wave
Alliance.

Reset Information (16 bits)

This field and the field /Manufacturer ID/ MUST be interpreted together. Each owner has full
freedom of use in this field.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 247


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.8.3** **Application** **Update** **Command**


This command is used to update node information data structures and to control SmartStart inclusion.
The Application Update Command Identifier is 0x49.

This command is used by during the following conditions:

If the Z-Wave API Module runs an End Node library type (refer to Table 4.39), it MUST send this
command to the host application when:

 - It received a _Node_ _Information_ _Frame_ _Command_ .

If the Z-Wave API Module runs an Controller node library type (refer to Table 4.39), it MUST send
this command to the host application when:

 - It received a _Node_ _Information_ _Frame_ _Command_ .

 - It received a _SmartStart_ _Prime_ _Command_ and it is in SmartStart Add Mode.

 - It received an _Included_ _Node_ _Info_ _Frame_ _Command_ and it is in SmartStart Add Mode.

 - It has the SIS Role and a node is added or excluded from the network by a controller (Primary
or Inclusion controller).

 - It has received a change in the Node Information Frame data for a node during network topology
update process (either Automatic Controller Update or Controller Replication).

Refer to [zwave_nwk_spec] for details.


**4.8.3.1** **Frame** **flow**


The frame flow for this command is an _Unsolicited_ _frame_ .


**4.8.3.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


None.


**4.8.3.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.8.3.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.8.3.5** **4.** **Unsolicited** **frame** **(Z-Wave** **Module** **→host)**


The Z-Wave module issues several unsolicited Application Update request frames corresponding to
the information it receives over the Z-Wave media.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 248


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.a.** **Unsolicited** **Application** **Update** **Command** **generic** **format**


A Z-Wave API module MUST issue this unsolicited frame to the host application when one of the
events described in the event field happened.

A Z-Wave API module implementing a _Controller_ _Node_ library type (refer to Table 4.39) MUST also
issue this unsolicited frame when it receives a _Node_ _Information_ _Frame_ as part of a network inclusion
or when a node has been excluded from the network.

A Z-Wave module MUST issue this unsolicited frame formatted according to Table 4.256.


Table 4.256: Application Update Command         - Unsolicited data
frame


Event (8 bits)

This field is used indicate which event has triggered the transmission of this command. This field
MUST be encoded according to Table 4.257


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 249


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.257: Application Update Command          - Event encoding


Values that are not listed in Table 4.257 are reserved and MUST NOT be used.

Remote NodeID (8/16 bits)

This field is used to advertise the NodeID of the remote node for/with which the event occurred.

Supported Command Class List Length (8 bits)

This field is used to indicates the length of the _Supported_ _Command_ _Class_ _List_ field in bytes.

Basic Device Class (8 bits)

Refer to _Basic_ _Device_ _Class_ _(8_ _bits)_ .

Generic Device Type (8 bits)

This field is used to advertise the _Generic_ _Device_ _Type_ of the remote NodeID.

For a detailed description of all available Generic Device Classes, refer to [device_class_spec] for
Z-Wave devices, [device_type_spec] for Z-Wave Plus devices, and [device_type_spec_v2] for Z-Wave
Plus v2 devices.

Specific Device Type (8 bits)

This field is used to advertise the _Specific_ _Device_ _Type_ of the remote NodeID.

For a detailed description of all available Specific Device Classes, refer to [device_class_spec] for
Z-Wave devices, [device_type_spec] for Z-Wave Plus devices, and [device_type_spec_v2] for Z-Wave
Plus v2 devices.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 250


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Supported Command Class List (N bytes)

This field is used to advertise the list of non-secure supported Command Classes by the remote node.


**4.b.** **Unsolicited** **Application** **Update** **Command** **with** **SmartStart** **Prime** **events**


A Z-Wave API module implementing a _Controller_ _Node_ library type (refer to Table 4.39) MUST issue
a unsolicited frame formatted according to Table 4.258 to the host application when it receives a
_SmartStart_ _Prime_ _Command_ or a _SmartStart_ _Inclusion_ _Node_ _Information_ _Frame_ .


Table 4.258: Application Update Command         - SmartStart Prime
data frame


Refer to _4.a._ _Unsolicited Application Update Command generic format_ for fields that are not described
below.

Event (8 bits)

This field is used to inform the host application that a SmartStart Prime frame has been received.

This field MUST be set to one of the following values:

 - UPDATE_STATE_NODE_INFO_SMARTSTART_HOMEID_RECEIVED (0x85) if received
using the Z-Wave Protocol

 - UPDATE_STATE_NODE_INFO_SMARTSTART_HOMEID_RECEIVED_LR (0x87) if received using the Z-Wave Long Range Protocol

Refer to _Application_ _Update_ _Command_ _-_ _Event_ _encoding_ for details about these values.

Length (8 bits)

Length of the frame.

NWI HomeID (4 bytes)

This field is used to advertise the NWI HomeID on which the _SmartStart_ _Prime_ _Command_ was
received.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 251


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.c.** **Unsolicited** **Application** **Update** **Command** **with** **Include** **Node** **Information** **event**


A Z-Wave API module implementing a _Controller_ _Node_ library type (refer to Table 4.39) MUST issue
a unsolicited frame formatted according to Table 4.259 to the host application when it receives a
_SmartStart_ _Prime_ _Command_ or a _SmartStart_ _Inclusion_ _Node_ _Information_ _Frame_ .


Table 4.259: Application Update Command         - SmartStart INIF
data frame


Refer to _4.a._ _Unsolicited Application Update Command generic format_ for fields that are not described
below.

Event (8 bits)

This field is used to inform the host application that a SmartStart Included Node Information frame
has been received. This field MUST be set to UPDATE_STATE_INCLUDED_NODE_INFO_RECEIVED (0x86).

Refer to _Application_ _Update_ _Command_ _-_ _Event_ _encoding_ for defailts about these values.

Reserved (8 bits)

This field is obsoleted.

It SHOULD be set to 0 by a Z-Wave API Module and ignored by a Host Application.

Rx Status (8 bits)

Refer to _Rx_ _Status_ _(8_ _bits)_

NWI HomeID (4 bytes)

This field is used to advertise the NWI HomeID for which the _SmartStart_ _Inclusion_ _Node_ _Information_
_Frame_ was received.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 252


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.8.4** **Promiscuous** **Application** **Command** **Handler** **Command**


This command was used by a Z-Wave module to notify a host application that a foreign Z-Wave frame
has been received. The Promiscuous Application Command Handler Command Identifier is 0xd1

This command was DEPRECATED.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 253


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.8.5** **Bridge** **Application** **Command** **Handler** **Command**


This command is used by a Z-Wave module to notify a host application that a Z-Wave frame has been
received. The Bridge Application Command Handler Command Identifier is 0xA8.

This command MUST only be supported by Z-Wave API Modules implementing a _Bridge_ _Controller_
_library_ (refer to Table 4.39). Z-Wave API Modules with another library type MUST use the _Application_
_Command_ _Handler_ _Command_ instead.


**4.8.5.1** **Frame** **flow**


The frame flow for this command is an _Unsolicited_ _frame_ .


**4.8.5.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


None.


**4.8.5.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.8.5.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.8.5.5** **4.** **Unsolicited** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue an unsolicited frame formatted according to Table 4.260.


Table 4.260: Bridge Application Command Handler Command         Unsolicited data frame


Rx Status (8 bits)

Refer to _Rx_ _Status_ _(8_ _bits)_ .

Destination NodeID (8/16 bits)

This field is used to advertise the NodeID to which the Z-Wave Command is addressed.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 254


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

If received frame is a multicast frame, the _Destination_ _NodeID_ is not valid.

Source NodeID (8/16 bits)

This field is used to advertise the NodeID from which the Z-Wave Command was received.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Payload Length (8 bits)

This field is used to indicate the length of the _Payload_ field in bytes.

Payload (N bytes)

This field is used to advertise payload of the received Z-Wave frame. The very first byte will be a
Command Class identifier.

The length of this field, in bytes, MUST be according to the _Payload_ _Length_ field.

Multicast Destination Node Mask Length (8 bits)

This field is used to indicate the length of the _Multicast_ _Destination_ _Node_ _Mask_ field in bytes.

Multicast Destination Node Mask (M bytes)

This field is used to indicate the destination nodes IDs using multicast addressing.

The length of this field, in bytes, MUST be according to the _Multicast_ _Destination_ _Node_ _Mask_ _Length_
field.

Received RSSI (8 bits)

This field is used to indicate the received frame RSSI value. This field value MUST be encoded
according to Table 4.3.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 255


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.8.6** **Nonce** **Update** **Command**


This command is used by a Z-Wave module to notify a host application that a nonce has been generated
when a S2 Nonce Get Request was received. This command also indicates that the Z-Wave module
has replied to the S2 Nonce Get Command to the requesting node. The Nonce Update Command
Identifier is 0xEB, same as _Nonce_ _Generation_ _on_ _Z-Wave_ _Module_ _Set_ _Mode_ _Command_ . The Nonce
Update Sub Command Identifier is 0x02.


**4.8.6.1** **Frame** **flow**


The frame flow for this command is an _Unsolicited_ _frame_ .


**4.8.6.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


None


**4.8.6.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.8.6.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.8.6.5** **4.** **Unsolicited** **frame** **(Z-Wave** **Module** **→host)**


This command MUST be sent only if the Nonce Generation on Module is enabled. For details refer
to _Nonce_ _Generation_ _on_ _Z-Wave_ _Module_ _Set_ _Mode_ _Command_ . A Z-Wave module MUST issue an
unsolicited frame formatted according to Table 4.261


Table 4.261: Nonce Update Command- Unsolicited data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.

This field MUST be set to 0x02 for the _Nonce_ _Update_ _Command_ .

Source NodeID (8/16 bits)

This field is used to advertise the NodeID from which the S2 Nonce Get Command was received.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Payload Type (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 256


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


This field is used to indicate the type of Payload being sent. This field MUST be encoded according
to Table 4.262.


Table 4.262: Nonce Update Command         - Payload Type encoding


Payload Length (8 bits)

This field is used to advertise the length in bytes of the _Payload_ field.

Payload (N bytes)

This field is used to report the payload that contains information related to the updates regarding
the S2 Nonce from Z-Wave module.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 257


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.9 Z-Wave API Miscellaneous Commands


This section describes _Z-Wave_ _API_ _Commands_ that do not belong in any of the other categories.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 258


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.1** **Clear** **Tx** **Timers** **Command**


This command is used to clear/reset the Z-Wave Module internal Tx timers. The Tx timers are
updated by the module when a frame is sent. The Clear Tx Timers Command Identifier is 0x37


**4.9.1.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**4.9.1.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.263


Table 4.263: Clear Tx Timers Command          - Initial data frame


**4.9.1.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.9.1.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 259


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.2** **Get** **Background** **RSSI** **Command**


This command is used to request the most recent background RSSI levels detected. The Get Background RSSI Command Identifier is 0x3B.

NOTE: The RSSI shall only be measured when the radio is in receive mode.


**4.9.2.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.2.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.264


Table 4.264: Get Background RSSI Command         - Initial data frame


**4.9.2.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.265


Table 4.265: Get Background RSSI Command         - Response data
frame


RSSI (2 or 3 bytes)

The RSSI fields are used to indicate the measured RSSI.

If the Z-Wave Module operates on a 2 channel RF Profile, RSSI CH0, and RSSI CH1 field MUSTTt
contain the RSSI values of the first and second channel.

If the Z-Wave Module operates on a 3 channel RF profile, all three RSSI fields MUST contain RSSI
values.

All RSSI measurements MUST be encoded according to Table 4.3


**4.9.2.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 260


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.3** **Get** **Tx** **Timer** **Command**


This command is used to request the Z-Wave Module’s internal Tx timers. When the module receives
this command, it MUST return the Tx timer for each channel. The number of channels returned may
vary depending on the the Z-Wave API version. The Get Tx Timer Command Identifier is 0x38.


**4.9.3.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.3.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.266


Table 4.266: Get Tx Timer Command          - Initial data frame


**4.9.3.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.267


Table 4.267: Get Tx Timer Command          - Response data frame


Tx Timer Channel 0 (4 bytes)

This field is used to advertise time [in miliseconds] the tranmistter has been active on channel 0 since
the last reset.

Tx Timer Channel 1 (4 bytes)

This field is used to advertise time [in miliseconds] the tranmistter has been active on channel 1 since
the last reset.

Tx Timer Channel 2 (4 bytes)

This field is used to advertise time [in miliseconds] the tranmistter has been active on channel 2 since
the last reset.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 261


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Tx Timer Channel 3 (4 bytes)

This field is used to advertise time [in miliseconds] the tranmistter has been active on channel 3 since
the last reset.

Tx Timer Channel 4 (4 bytes)

This field is used to advertise time [in miliseconds] the tranmistter has been active on channel 4 since
the last reset.


**4.9.3.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 262


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.4** **Get** **Virtual** **Nodes** **Command**


This command is used to request available Virtual End Nodes in a Z-Wave Network. The Get Virtual
Nodes Command Identifier is 0xA5.


**4.9.4.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.4.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.268.


Table 4.268: Get Virtual Nodes Command         - Initial data frame


**4.9.4.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.269 to notify the
available Virtual End Nodes to the application that requests the list of virtual node using Get Virtual
Nodes Command request frame.


Table 4.269: Get Virtual Nodes Command         - Response data frame


NodeMask(N bytes)

This field is used to indicate the bit mask of the virtual end NodeIDs in a Z-Wave network. The field
value MUST be encoded according to:

 - If bit ‘n’ in the NodeMask byte ‘i’ is 1, it indicates that node (i*8)+n+1 is a virtual end node.

 - If bit ‘n’ in the NodeMask byte ‘i’ is 0, it indicates that node (i*8)+n+1 is not a virtual end
node.


**4.9.4.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 263


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.5** **Get** **Z-Wave** **Module** **Protocol** **Status** **Command**


This command is used to request the current status of the protocol runs on the Z-Wave module. The
Get Z-Wave Module Protocol Status Command Identifier is 0xBF.


**4.9.5.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.5.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.270 to request the protocol status.


Table 4.270: Get Z-Wave Module Protocol Status Command         - Initial data frame


**4.9.5.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.271 for notifying
the current status of the Z-Wave protocol to the host application.


Table 4.271: Get Z-Wave Module Protocol Status Command         - Response data frame


Status (8 bits)

This field is used to advertise the current status of the protocol runs on the Z-Wave module. This
field MUST be encoded according to Table 4.272


Table 4.272: Z-Wave protocol status encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 264


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.5.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 265


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.6** **Is** **Virtual** **Node** **Command**


This command is used to check if a given NodeID is a virtual end node. The Is Virtual Node Command
Identifier is 0xA6.


**4.9.6.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.6.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.273.


Table 4.273: Is Virtual Node Command          - Initial data frame


NodeID (8 bits)

This field is used to indicate the NodeID on node for which virtual node status is requested.

This field MUST be encoded using 8 bits regardless of the configured NodeID base Type. Refer to
_Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.


**4.9.6.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.274.


Table 4.274: Is Virtual Node Command         - Response data frame


Virtual node characteristic (8 bits)

This field is used to advertise characteristic of the request NodeID. This field MUST be encoded as
follow:

 - If the NodeID is a virtual node, this field MUST be set to 0x01.

 - If the NodeID is not a virtual node. this field MUST be set to 0x00.


**4.9.6.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 266


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.7** **Set** **Listen** **Before** **Talk** **Threshold** **Command**


This command is used to to set the “Listen Before Talk” RSSI threshold that controls at what RSSI
level a Z-Wave node will refuse to transmit because of noise. The default threshold value is set to a
value corresponding to the RF regulatory requirements in the specific country. The Set Listen Before
Talk Threshold Command Identifier is 0x3C.


**4.9.7.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .

This command SHOULD be used once for each channel configured by the Host Application.


**4.9.7.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.275


Table 4.275: Set Listen Before Talk Threshold Command         - Initial
data frame


Channel (8 bits)

This field is used to indicate the channel number where the RSSI threshold shall be set for. Valid
channel numbers are 0, 1, 2 and 3.

Channel values 0..2 MUST indicate the Z-Wave channel number. Channel value 3 MUST indicate the
Z-Wave Long Range Channel.

A Z-Wave API Module without Z-Wave Long Range support will ignore the channel value 3.

RSSI Threshold (8 bits)

This field is used to indicate the RSSI threshold that MUST be used by the Z-Wave API Module to
detect the channel availability.

This field MUST be encoded according to This field MUST be encoded according to _RSSI_ _Measure-_
_ments (8_ _bits)_ and Table 4.3. The values 125, 126 and 127 MUST NOT be used by a Host Application
in this command and MUST be ignored by a Z-Wave API Module if received.


**4.9.7.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.276


Table 4.276: Set Listen Before Talk Threshold Command         - Response data frame


Status (8 bits)

This field is used to indicate status regarding the Set Listen Before Talk Threshold request command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 267


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


 - If the Listen Before Talk Threshold value is accepted by the Z-Wave Module, the field value
MUST be set to 0x01.

 - If the Listen Before Talk Threshold value is not accepted, the field value MUST be set to 0x00.


**4.9.7.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 268


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.8** **Set** **RF** **Receive** **Mode** **Command**


This command is used to to power down the RF when not in use e.g., expects nothing to be received.
It can also be used to set the RF into receive mode. This functionality is useful in battery powered
Z-Wave nodes. The RF is automatic powered up when transmitting data.

The Set RF Receive Mode Command Identifier is 0x10.


**4.9.8.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.8.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.277


Table 4.277: Set RF Receive Mode Command         - Initial data frame


Mode (8 bits)

This field is used to advertise information about the Set RF Receive Mode operation mode. The field
MUST be encoded with the format indicated in Table 4.278.


Table 4.278: Set RF Receive Mode Command         - Mode encoding


**4.9.8.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.279


Table 4.279: Set Rf Receive Mode Command - Response data frame


Status (8 bits)

This field is used to advertise information about the status of the Set RF Receive Mode operation.
The field MUST be encoded according to:

 - 0x01, If the operation was successfull.

 - 0x00, If the operation was not successfull.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 269


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.8.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 270


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.9** **Set** **RF** **Power** **Level** **Command**


This command is used to set the power level used for RF transmission. The Set RF Power Level
Command Identifier is 0x17.

NOTE: This command should only be used in an install/test link situation and the power level should
always be set back to normal Power when the testing is done.

NOTE: This command is no longer implemented in controllers.


**4.9.9.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.9.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.280


Table 4.280: Set RF Power Level Command         - Initial data frame


Powerlevel (8 bits)

This field is used to indicate the power level that shall be used for the RF transmission. This field
MUST comply with the format indicated in Table 4.281.


Table 4.281: Set RF Power Level Command - Power Level encoding


**4.9.9.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.282


Table 4.282: Set RF Power Level Command - Response data frame


Powerlevel (8 bits)

This field is used to indicate the actual RF power level that can used for transmitting a given test
frame.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 271


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.9.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 272


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.10** **Set** **Maximum** **Routing** **Attempts** **Command**


This command is used to set the maximum number of source routing attempts based on the routing
table lookups, and this shall be used before the Z-Wave protocol layer starts the dynamic route
resolution. The Set Maximum Routing Retries Command Identifier is 0xD4.


**4.9.10.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.10.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.283 for setting the maximum source
routing attempts.


Table 4.283: Set Maximum Routing Attempts Command         - Initial
data frame


Max Routing Retries (8 bits)

This field is used to indicate the maximum source routing attempts that can be used before the Z-Wave
module triggers dynamic route resolution.


**4.9.10.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.284 when it is asked
to set the maximum source routing attempts.


Table 4.284: Set Maximum Routing Attempts Command         - Response data frame


Command Status (8 bits)

Refer _Command_ _Status_ _(8_ _bits)_ .


**4.9.10.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 273


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.11** **Set** **RF** **Power** **Level** **Rediscovery** **Command**


This command is used to set the power level to RF Module that can be used for finding neighboring
nodes. The Set RF Power Level Rediscovery Command Identifier is 0x1E.


**4.9.11.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**4.9.11.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.285


Table 4.285: Set RF Power Level Rediscovery Command         - Initial
data frame


Powerlevel (8 bits)

This field is used to indicate the power level that MUST be used by the node when performing the
neighbor discovery process.

This field MUST comply with the format indicated in Table 4.282.


**4.9.11.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.9.11.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 274


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.12** **Start** **Watchdog** **Command**


This command is used to start Watchdog functionality on Z-Wave module. The Start Watchdog
Command Identifier is 0xD2.


**4.9.12.1** **Frame** **flow**


The frame flow for this command is an _Unacknowledged_ _frame_ .


**4.9.12.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.286 for triggering the Watchdog
functionality on a Z-Wave module.


Table 4.286: Start Watchdog Command          - Initial data frame


**4.9.12.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.9.12.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 275


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.13** **Stop** **Watchdog** **Command**


This command is used to stop Watchdog functionality on Z-Wave module. The Start Watchdog
Command Identifier is 0xD3.


**4.9.13.1** **Frame** **flow**


The frame flow for this command is an _Unacknowledged_ _frame_ .


**4.9.13.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.287 for stopping the Watchdog
functionality on a Z-Wave module.


Table 4.287: Stop Watchdog Command          - Initial data frame


**4.9.13.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


**4.9.13.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 276


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.14** **Set** **Timeouts** **Command**


This command is used to set timeouts with 10ms ticks. The Set Timeouts Command Identifier is
0x06.


**4.9.14.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.14.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.288.


Table 4.288: Set Timeouts Command           - Initial data frame


Rx ACK Timeout (8 bits)

This field is used to indicate the maximum time to wait for ACK after frame transmission, in 10ms
ticks.

Rx BYTE Timeout (8 bits)

This field is used to indicate the maximum time to wait for next byte when receiving a new frame, in
10ms ticks.


**4.9.14.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.289.


Table 4.289: Set Timeouts Command          - Response data frame


Previous Rx ACK Timeout (8 bits)

This field is used to indicate previous Rx ACK timeout setting, in 10ms ticks.

Previous Rx BYTE Timeout (8 bits)

This field is used to indicate previous Rx BYTE timeout setting, in 10ms ticks.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 277


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.14.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 278


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.15** **Power** **Management** **Stay** **Awake** **Command**


This command is used to keep the Z-Wave module awake.

This command is used in the Z-Wave API for End Nodes by the certification tools (not recommended
for other use cases).

The Power Management Stay Awake Command Identifier is 0xD7.


**4.9.15.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**4.9.15.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.290 for keeping the Z-Wave module
awake.


Table 4.290: Power Management Stay Awake         - Initial data frame


Power Lock type

Select which peripheral should be kept awake. This field MUST be encoded according to Table 4.291.


Table 4.291: Power Management Stay Awake         - Power Lock type


Power Lock Timeout (32 bits)

This field is used to set how long the peripheral should stay awake. This value must be provided in
ms and MSB first. Value 0 could be used to keep the peripheral awake without time limitation.

Wake Up Timer Timeout (32 bits)

If the Power Lock Timeout is not 0, this field is used to trigger a wake up event in the Z-Wave module
(after Wake Up Timer timeout). This value must be provided in ms and MSB first. If the value is 0,
no wake up event is triggered.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 279


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.16** **Power** **Management** **Cancel** **Command**


This command is used to cancel a power lock set with the _Power_ _Management_ _Stay_ _Awake_ _Command_ .

The Power Management Cancel Command Identifier is 0xD8.


**4.9.16.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**4.9.16.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.292.


Table 4.292: Power Management Cancel          - Initial data frame


Power Lock type

This field is used to set which peripheral should have the power lock cancelled and MUST be encoded
according to Table 4.291.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 280


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.17** **Initiate** **Shutdown** **Command**


This command is used to instruct the Z-Wave API to go to sleep in order to remove the power. The
Initiate Shutdown Command Identifier is 0xD9.


**4.9.17.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.17.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.293


Table 4.293: Initiate Shutdown Command          - Initial data frame


**4.9.17.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.294


Table 4.294: Initiate Shutdown Command         - Response data frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


**4.9.17.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 281


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.18** **Radio** **Debug** **Get** **Protocol** **List** **Command**


This command is used to get the list of supported radio debug protocols and the Radio Debug
command versions used by the Z-Wave module.

The radio debug interface uses a specific hardware connection (other than the Z-Wave API) to provide
all frames sent and received by the Z-Wave module, and other information about the radio. This
command gives the list of protocols that could be used on this interface.

This command must be used for test purposes only.

Radio Debug commands exist in multiple versions. In version 1, this command ( _Radio_ _Debug_ _Get_
_Protocol_ _List_ _Command_ ) does not exist. Refer to _Radio_ _Debug_ _Version_ _Identification_ to determine
the version used by the Z-Wave module.

The Radio Debug Get Protocol List Command Identifier is 0xE6.


**4.9.18.1** **Radio** **Debug** **Version** **Identification**


The following table shows Radio Debug commands version based on the list of supported commands.


Table 4.295: Radio Debug Version Identification







**4.9.18.2** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.18.3** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.296.


Table 4.296: Radio Debug Get Protocol List         - Initial data frame


**4.9.18.4** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


The response data frame MUST be formatted according to Table 4.297.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 282


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.297: Radio Debug Get Protocol List - Response data frame


Radio Debug Commands Version

Version of _Radio_ _Debug_ _Get_ _Protocol_ _List_ _Command_ (0xE6), _Radio_ _Debug_ _Enable_ _Command_ (0xE7),
and _Radio_ _Debug_ _Status_ _Command_ (0xE8) commands.

Count of supported protocols

Count of radio debug protocols supported by the Z-Wave module. (Count of elements in Supported
radio debug protocol N).

Supported Radio debug protocol N (16 bits)

List of radio debug protocols supported by the Z-Wave module from Table 4.298.


Table 4.298: Radio Debug Enable          - Debug Interface Protocol


**4.9.18.5** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 283


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.19** **Radio** **Debug** **Enable** **Command**


This command is used to enable or disable the radio debug interface.

The radio debug interface uses a specific hardware connection (other than the Z-Wave API) to provide
all frames sent and received by the Z-Wave module, and other information about the radio.

This command must be used for test purposes only.

Legacy Z-Wave modules may use this command in the V1 format. However, the V1 format is deprecated and new Z-Wave modules should use the V2 format. Refer to _Radio Debug Version Identification_
to determine the version used by the Z-Wave module.

The Radio Debug Enable Command Identifier is 0xE7.


**4.9.19.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .


**4.9.19.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


**Initial** **data** **frame** **V1**


The initial data frame V1 MUST be formatted according to Table 4.299.


Table 4.299: Radio Debug Enable           - Initial data frame


Enable

1 to enable the radio debug interface, 0 to disable it.

The radio debug interface protocol requested is the PTI (refer to Table 4.298).


**Initial** **data** **frame** **V2**


The initial data frame V2 MUST be formatted according to Table 4.300.


Table 4.300: Radio Debug Enable           - Initial data frame


Enable

1 to enable the radio debug interface, 0 to disable it.

Debug Interface Protocol (16 bits)

Protocol to use on the debug interface according to Table 4.298.

If Enable is 0, this field should be ignored by Z-Wave module.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 284


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Configuration Size

Size of the Configuration field in bytes.

If the Configuration field exists in the frame, this field must be set.

Configuration (N bytes)

Configuration of Debug Interface Protocol. See the Table 4.298 for the content of this field.

If this field exists in the frame, the Configuration Size must be set.


**4.9.19.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.301.


Table 4.301: Radio Debug Enable           - Response data frame


Command Status (8 bits)

Refer to _Command_ _Status_ _(8_ _bits)_ .


**4.9.19.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 285


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.20** **Radio** **Debug** **Status** **Command**


This command is used to get the status of the radio debug interface.

This command must be used for test purposes only.

Legacy Z-Wave modules may use this command in the V1 format. However, the V1 format is deprecated and new Z-Wave modules should use the V2 format. Refer to _Radio Debug Version Identification_
to determine the version used by the Z-Wave module.

The Radio Debug Status Command Identifier is 0xE8.


**4.9.20.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.20.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.302.


Table 4.302: Radio Debug Status            - Initial data frame


**4.9.20.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


**Response** **data** **frame** **V1**


A response frame V1 must be formatted according to Table 4.303


Table 4.303: Radio Debug Status          - Response data frame V1


Debug Interface Status

1 if the debug interface is enabled, 0 otherwise.

The radio debug interface protocol used is the PTI (refer to Table 4.298).


**Response** **data** **frame** **V2**


A response frame V2 must be formatted according to Table 4.304


Table 4.304: Radio Debug Status          - Response data frame V2


Debug Interface Status


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 286


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


1 if the debug interface is enabled, 0 otherwise.

Debug Interface Protocol (16 bits)

Protocol used by the debug interface according to Table 4.298.

If Debug Interface Status is 0, the field is not relevant, and the host should not rely on it.


**4.9.20.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 287


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.9.21** **Nonce** **Generation** **on** **Z-Wave** **Module** **Set** **Mode** **Command**


This command is used to enable Nonce Generation on the Z-Wave Module if the S2 Nonce Get
command is received from the end node. Once enabled, the module will be responsible to:

 - Generate the Nonce

 - Send the nonce to the requesting node using the S2 Nonce Report command.

 - Send the generated Nonce to the Host using _Nonce_ _Update_ _Command_ .

The Nonce Generation on Z-Wave Module Command Identifier is 0xEB, same as _Nonce_ _Update_ _Com-_
_mand_ . The Nonce Generation on Z-Wave Module Sub Command Identifier is 0x01.


**4.9.21.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.9.21.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.305


Table 4.305: Nonce Generation on Z-Wave Module Set Mode Command       - Initial data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.

This field MUST be set to 0x01 for the _Nonce_ _Generation_ _on_ _Z-Wave_ _Module_ _Set_ _Mode_ _Command_ .

Nonce Generation Mode Command (8 bits)

The Nonce Generation Mode Command will be used to indicate whether to enable or disable the
nonce generation on Z-Wave module. 1 if the Nonce generation needs to be enabled, 0 if it needs to
be disabled.


**4.9.21.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.306


Table 4.306: Nonce Generation on Z-Wave Module Set Mode Command       - Response data frame


Sub Command (8 bits)

This field is used to indicate the Sub Command within the Z-Wave API Setup Command.

This field MUST be set to 0x01 for the _Nonce_ _Generation_ _on_ _Z-Wave_ _Module_ _Set_ _Mode_ _Command_ .

Command Status (8 bits)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 288


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Refer to _Command_ _Status_ _(8_ _bits)_ .


**4.9.21.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 289


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.10 Z-Wave API Transport Commands


This section describes _Z-Wave_ _API_ _Commands_ that are used to perform transport operations.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 290


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.1** **Controller** **Node** **Send** **Data** **Command**


This command is used to transmit contents of a data buffer to a single node or all nodes (broadcast).
The Controller Node Send Data Command Identifier is 0x13.

This command MUST only be supported by controller Z-Wave library types (refer to Table 4.39).


**4.10.1.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**4.10.1.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.307


Table 4.307: Controller Node Send Protocol Data Command         - Initial data frame


Destination NodeID (8/16 bits)

This field is used to indicate the destination NodeID to send the Z-Wave Frame to.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Data Length (8 bits)

This field is used to indicate the length in bytes of the _Data_ field. This field MUST be set to a value
greater than 0.

Data (N bytes)

This field is used to advertise the data payload that MUST be transmited on the Z-Wave radio to the
destination NodeID.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field.

Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 291


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.1.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.308


Table 4.308: Send Data Command          - Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


**4.10.1.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.309


Table 4.309: Send Data Command           - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .

Tx Status Report (N bytes)

This field is used to report detailed information about the Z-Wave frame transmission. This field
MUST be omitted if the Z-Wave API module is not configured to enable Tx Status Reports in the
_Z-Wave_ _API_ _Setup_ _Set_ _Tx_ _Status_ _Report_ _Sub_ _Command_ .

For field description, refer to _Tx_ _Status_ _Report_ _(N_ _bytes)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 292


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.2** **Controller** **Node** **Send** **Data** **Multicast** **Command**


This command is used to transmit a data buffer to a list of Z-Wave nodes (i.e., Multicast frame). The
Controller Node Send Data Multicast Command Identifier is 0x14.

This command MUST only be supported by Controller Z-Wave library types (refer to Table 4.39).
Z-Wave API Module supporting an End Node library MUST use _End_ _Node_ _Send_ _Data_ _Multicast_
_Command_ instead.


**4.10.2.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**4.10.2.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.310


Table 4.310: Send Data Multicast Command         - Initial data frame


NodeID Count (8 bits)

This field is used to advertise the number of NodeIDs contained in the _NodeID_ _List_ field.

For example, if there are 2 NodeIDs encoded in 4 bytes in the _NodeID_ _List_ field, this field MUST be
set to 2.

NodeID List (N bytes)

This field is used to advertise the list of destination NodeID’s.

Each 8 bits/16 bits groups in this field MUST represent a NodeID.

All NodeIDs in this field MUST be encoded according to the configured NodeID base Type. Refer to
_Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Data Length (8 bits)

This field is used to indicate the length in bytes of the _Data_ field. This field MUST be set to a value
greater than 0.

Data (M bytes)

This field is used to advertise the data payload that MUST be transmited on the Z-Wave radio to the
destination NodeIDs.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field.

Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 293


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**4.10.2.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.311


Table 4.311: Send Data Multicast Command - Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


**4.10.2.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.312


Table 4.312: Send Data Multicast Command - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 294


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.3** **End** **Node** **Send** **Data** **Command**


This command is used to transmit contents of a data buffer to a single node or all nodes (broadcast).
The End Node Send Data Command Identifier is 0x0E. This command MUST only be supported by
End node library types (refer to Table 4.39).


**4.10.3.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**4.10.3.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.313


Table 4.313: End Node Send Data Command         - Initial data frame


Destination NodeID (8/16 bits)

This field is used to indicate the Destination NodeID.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Data Length (8 bits)

This field is used to indicate the length in bytes of the _Data_ field. This field MUST be set to a value
greater than 0.

Data (N bytes)

This field is used to advertise the data payload that MUST be transmited on the Z-Wave radio to the
destination NodeID.

This field MUST represent the unencrypted data payload.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field.

Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Tx Security Options (8 bits)

This field is used to indicate the security 2 specific options. This field MUST be encoded according
to Table 4.314


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 295


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.314: End Node Send Data         - Tx Security Options encoding


Other Tx Security Options values are reserved. Reserved values MUST NOT be used and MUST be
ignored by a receiving interface.

The Singlecast follow-up frames will reuse the Multicast GroupID received in the last _End_ _Node_ _Send_
_Data_ _Multicast_ _Command_ .

Security Keys (8 bits)

This field is used to advertise the security key for the transmission. This field MUST be encoded
according to Table 4.315


Table 4.315: End Node Send Data          - Tx Security key encoding


Other Tx Security key values are reserved. Reserved values MUST NOT be used and MUST be
ignored by a receiving interface.

Tx Options 2 (8 bits)

This field is used to indicate more transmission options flags. It is reserved for future use. It MUST
be set to 0x00.

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**4.10.3.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.316


Table 4.316: End Node Send Data Command         - Response data
frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 296


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.3.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.317


Table 4.317: End Node Send Data Command - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .

Tx Status Report (N bytes)

This field is used to report detailed information about the Z-Wave frame transmission. This field
MUST be omitted if the Z-Wave API module is not configured to enable Tx Status Reports in the
_Z-Wave_ _API_ _Setup_ _Set_ _Tx_ _Status_ _Report_ _Sub_ _Command_ .

For field description, refer to _Tx_ _Status_ _Report_ _(N_ _bytes)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 297


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.4** **End** **Node** **Send** **Data** **Multicast** **Command**


This command is used to transmit a data buffer to a list of Z-Wave nodes (i.e., S2 Multicast frame).

The End Node Send Data Multicast Command Identifier is 0x0F. This command shall only be supported by End Node library types (refer to Table 4.39).


**4.10.4.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**4.10.4.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.318


Table 4.318: End Node Send Data Multicast Command         - Initial
data frame


Data Length (8 bits)

This field is used to indicate the length in bytes of the _Data_ field. This field MUST be set to a value
greater than 0.

Data (N bytes)

This field is used to advertise the data payload that MUST be transmited on the Z-Wave radio to the
destination NodeIDs.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field.

Multicast group ID (8 bits)

This field is used to indicate the destination GroupID assigned to the current Security 2 Multicast
frame.

This GroupID will be used in the S2 MGRP extension. Refer to [zwave_encapsulation_cc_spec] for
the S2 MGRP extension.

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 298


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.4.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.319


Table 4.319: End Node Send Data Multicast Command - Response
data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


**4.10.4.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.320


Table 4.320: End Node Send Data Multicast Command         - Callback
data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 299


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.5** **Bridge** **Controller** **Node** **Send** **Data** **Command**


This command is used to transmit contents of a data buffer to a single node or all nodes (broadcast).
The Bridge Controller Node Send Data Command Identifier is 0xA9.

This command MUST only be supported by nodes implementing a Bridge Controller library type
(refer to Table 4.39).


**4.10.5.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**4.10.5.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.321


Table 4.321: Bridge Controller Node Send Data Command - Initial
data frame


Source NodeID (8 bits / 16 bits)

This field is used to indicate the Source NodeID from which the Z-Wave Frame must be issued.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Setting Source NodeID to 0xFF/0xFFF will cause the protocol to automatically use the controllers
native NodeID

Destination NodeID (8 bits / 16 bits)

This field is used to indicate the destination NodeID.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Data Length (8 bits)

This field is used to indicate the length in bytes of the _Data_ field. This field MUST be set to a value
greater than 0.

Data (N bytes)

This field is used to advertise the data payload that MUST be transmited on the Z-Wave radio to the
destination NodeID.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 300


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Route (4 bytes)

This field is used to indicate the priority route to be used for transmitting a frame. If there are not
any routes, the field MUST set to zero.

Session identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**4.10.5.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.322


Table 4.322: Bridge Controller Node Send Data Command         - Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


**4.10.5.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.323


Table 4.323: Bridge Controller Node Send Data Command         - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .

Tx Status Report (N bytes)

This field is used to report detailed information about the Z-Wave frame transmission. This field
MUST be omitted if the Z-Wave API module is not configured to enable Tx Status Reports in the
_Z-Wave_ _API_ _Setup_ _Set_ _Tx_ _Status_ _Report_ _Sub_ _Command_ .

For field description, refer to _Tx_ _Status_ _Report_ _(N_ _bytes)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 301


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.6** **Bridge** **Controller** **Node** **Send** **Data** **Multicast** **Command**


This command is used to transmit a data buffer to a list of Z-Wave nodes (i.e., Multicast frame). The
Bridge Controller Node Send Data Multicast Command Identifier is 0xAB.

This command MUST only be supported by Z-Wave API Module using the Controller Bridge library
types (refer to Table 4.39).


**4.10.6.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**4.10.6.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.324


Table 4.324: Bridge Controller Node Send Data Multicast Command       - Initial data frame


Source NodeID (8/16 bits)

This field is used to indicate the Source NodeID from which the Z-Wave Frame MUST be issued.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Setting Source NodeID to 0xFF/0xFFF will cause the protocol to automatically use the controllers
native NodeID

NodeID Count (8 bits)

This field is used to advertise the number of NodeIDs contained in the _NodeID_ _List_ field.

For example, if there are 2 NodeIDs encoded in 4 bytes in the _NodeID_ _List_ field, this field MUST be
set to 2.

NodeID List (N bytes)

This field is used to advertise a list of NodeID destinations.

Each 8 bits/16 bits groups in this field MUST represent a NodeID.

All NodeIDs in this field MUST be encoded according to the configured NodeID base Type. Refer to
_Z-Wave_ _API_ _Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Data Length (8 bits)

This field is used to indicate the length in bytes of the _Data_ field. This field MUST be set to a value
greater than 0.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 302


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Data (M bytes)

This field is used to advertise the data payload that MUST be transmited on the Z-Wave radio to the
destination NodeIDs.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field.

Tx Options (8 bits)

Refer to _Tx_ _Options_ _(8_ _bits)_ .

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**4.10.6.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.325


Table 4.325: Bridge Controller Node Send Data Multicast Command       - Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


**4.10.6.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.326


Table 4.326: Bridge Controller Node Send Data Multicast Command       - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 303


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.7** **Send** **Data** **Abort** **Command**


This command is used to instruct the Z-Wave Module to abort an ongoing transmission started with
any of the following commands:

 - _Bridge_ _Controller_ _Node_ _Send_ _Data_ _Command_

 - _Bridge_ _Controller_ _Node_ _Send_ _Data_ _Multicast_ _Command_

 - _End_ _Node_ _Send_ _Data_ _Command_

 - _End_ _Node_ _Send_ _Data_ _Multicast_ _Command_

 - _Controller_ _Node_ _Send_ _Data_ _Command_

 - _Controller_ _Node_ _Send_ _Data_ _Multicast_ _Command_

 - _Send_ _NOP_ _Command_

The Send Data Abort Command Identifier is 0x16.


**4.10.7.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ .

If a host application aborts an ongoing transmission, the Z-Wave API Module MUST still issue a 3.
callback data frame for the ongoing transmission. This is illustrated in Figure 4.29. A Z-Wave API
Module MUST ignore this command if it is received when no transmission is ongoing.


Figure 4.29: Send Data Abort Command Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 304


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.7.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.327


Table 4.327: Send Data Abort Command          - Initial data frame


**4.10.7.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


None


**4.10.7.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 305


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.8** **Send** **Test** **Frame** **Command**


This command is used to send a test frame directly to a given node without any routing. The Send
Test Frame Command Identifier is 0xBE.

Note that this command shall only be used during installation and testing the wireless communication
link path. And the test will be done using 9600 kbit/s transmission rate.


**4.10.8.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**4.10.8.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.328.


Table 4.328: Send Test Frame Command          - Initial data frame


NodeID (8/16 bits)

This field is used to advertise the NodeID of the node where the test frame is sent to.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Powerlevel (8 bits)

This field is used to advertise the power level which the Z-Wave module shall use for the RF transmission of the test frame. This field MUST comply with the format indicated in _Set_ _RF_ _Power_ _Level_
_Command_ initial data frame section.

Session identifer (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


**4.10.8.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.329 when the Send
Test Frame Command data is received by the Z-Wave Module.


Table 4.329: Send Test Frame Command         - Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 306


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.8.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.330 when the transmission of the test frame is executed.


Table 4.330: Send Test Frame Command         - Callback data frame


Session identifer (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 307


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.9** **Controller** **Node** **Send** **Protocol** **Data** **Command**


This command is used in case of NLS, to transmit the contents of an encrypted data buffer to a single
node. It must only be used on reception of _Request_ _Protocol_ _Command_ _Class_ _Encryption_ _command_ .
The Controller Node Send Protocol Data Command Identifier is 0xAC.

This command MUST only be supported by controller Z-Wave library types (refer to Table 4.39).


**4.10.9.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ _and_ _callback_ .


**4.10.9.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.331


Table 4.331: Controller Node Send Protocol Data Command         - Initial data frame


Destination NodeID (8/16 bits)

This field is used to indicate the destination NodeID to send the Z-Wave frame to.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Data Length (8 bits)

This field is used to indicate the length in bytes of the _Data_ field. This field MUST be set to a value
greater than 0.

Data (N bytes)

This field is used to advertise the data payload that MUST be transmitted on the Z-Wave radio to
the destination NodeID.

The length of this field, in bytes, MUST be according to the _Data_ _Length_ field.

Payload Meta Data Length (8 bits)

This field is used to advertise the length in bytes of the _Payload_ _Meta_ _Data_ field.

Payload Meta Data (M bytes)

This field is used to maintain the context in the Z-Wave application. This field MUST be identical to
Payload Meta Data from the initial request in _Request Protocol Command Class Encryption command_

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 308


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.10.9.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.332


Table 4.332: Controller Node Send Protocol Data Command         - Response data frame


Response status (8 bits)

Refer to _Response_ _status_ _(8_ _bits)_ .


**4.10.9.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST issue a callback frame formatted according to Table 4.333


Table 4.333: Controller Node Send Protocol Data Command - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .

Tx Status Report (N bytes)

This field is used to report detailed information about the Z-Wave frame transmission. This field
MUST be omitted if the Z-Wave API module is not configured to enable Tx Status Reports in the
_Z-Wave_ _API_ _Setup_ _Set_ _Tx_ _Status_ _Report_ _Sub_ _Command_ .

For field description, refer to _Tx_ _Status_ _Report_ _(N_ _bytes)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 309


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025

## 4.11 Z-Wave API Security Commands


This section describes _Z-Wave_ _API_ _Commands_ that are used to perform security bootstrapping operations.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 310


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.11.1** **Security** **Setup** **Command**


This command is used to set the Requested Security Keys and Requested Authentication method prior
to inclusion (add). The Requested Security Keys and Authentication is requested by the protocol
during S2 inclusion. The Security Setup Command Identifier is 0x9C.

This command MUST only be supported by Z-Wave API Module implementing an _End_ _Node_ library
type (e.g. _End_ _Node_ _library_, _Enhanced_ _232_ _End_ _Node_ _Library*_ or _Routing_ _End_ _Node_ _library_ ). Refer
to Table 4.39).


**4.11.1.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.11.1.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.334.


Table 4.334: Security Setup Command          - Initial data frame


Security Mode (8 bits)

This field is used to indicate the mode that represents the requested security functionalities. This
field MUST be encoded according to Table 4.335


Table 4.335: The security mode value encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 311


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Parameter Length (8 bits)

This field is used to indicate the length in bytes of the _Parameter_ field. This field MUST be set to a
value greater than 0.

Parameter (N bytes)

This field is used to advertise additional parameters required for the value specified in the _Security_
_Mode_ field. The length of this field, in bytes, MUST be according to the _Parameter_ _Length_ field. This
field MUST be encoded according to Table 4.336


Table 4.336: Security Setup Command         - Initial Frame Parameter
Field Encoding



























**4.11.1.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.337.


Table 4.337: Security Setup Command          - Response data frame


Refer _Security_ _Setup_ _Command_ _-_ _Initial_ _data_ _frame_ field descriptions for the fields that are not
described below.

Parameter (N bytes)

This field is used to advertise parameters corresponds to the security mode flag used in _Security_ _Mode_
field. The length of this field, in bytes, MUST be according to the _Parameter_ _Length_ field. This field
MUST be encoded according to Table 4.338


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 312


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.338: Security Setup Command Response Frame Parameter
Field Encoding



































Table 4.339: The security keys bitmask value encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 313


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.11.1.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 314


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.11.2** **Encrypt** **Data** **With** **AES** **Command**


This command is used to request the Z-Wave API module to encrypt a Z-Wave frame payload using
AES-128 Electronic CookBook mode. The Encrypt Data With AES Command Identifier is 0x67.


**4.11.2.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _response_ .


**4.11.2.2** **1.** **Initial** **data** **frame** **(host** **→Z-Wave** **Module)**


The initial data frame MUST be formatted according to Table 4.340.


Table 4.340: Encrypt Data With AES Command         - Initial data
frame


Keys (16 bytes)

This field is used to advertise the encryption key.

Input Data (16 bytes)

This field is used to indicate the data to be encrypted.


**4.11.2.3** **2.** **Response** **data** **frame** **(Z-Wave** **Module** **→host)**


A Z-Wave module MUST return a response frame formatted according to Table 4.341.


Table 4.341: Encrypt Data With AES Command         - Response data
frame


Output Data (16 bytes)

This field is used to advertise the encrypted data.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 315


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.11.2.4** **3.** **Callback** **data** **frame** **(Z-Wave** **Module** **→host)**


None.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 316


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.11.3** **Request** **Protocol** **Command** **Class** **Encryption** **command**


This command is used by the Z-Wave API module to request a host application to encrypt a Z-Wave
protocol frame payload. The Request Protocol Command Class Encryption Command Identifier is
0x6C.


**4.11.3.1** **Frame** **flow**


The frame flow for this command is an _Acknowledged_ _frame_ _with_ _callback_ . This command should be
sent on desired encryption of a Protocol Command Class by the Z-Wave Module. An example flow is
show in Figure 4.30


Figure 4.30: Request Protocol Command Class Encryption usage


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 317


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.11.3.2** **1.** **Initial** **data** **frame** **(Z-Wave** **Module** **→host)**


The initial data frame MUST be formatted according to Table 4.342.


Table 4.342: Request Protocol Command Class Encryption - Initial
data frame


Destination NodeID (8/16 bits)

This field is used to advertise the destination node ID.

This field MUST be encoded according to the configured NodeID base Type. Refer to _Z-Wave_ _API_
_Setup_ _Set_ _NodeID_ _Base_ _Type_ _Sub_ _Command_ and Table 4.84.

Payload Length (8 bits)

This field is used to advertise the length in bytes of the _Payload_ field.

Payload (N bytes)

This field is used to report the payload to be encrypted by the host application.

Payload Meta Data Length (8 bits)

This field is used to advertise the length in bytes of the _Payload_ _Meta_ _Data_ field.

Payload Meta Data (M bytes)

This field is used to maintain the context in the Z-Wave application and MUST be reported as is in
the Payload Meta Data field in the reply sent using _Controller_ _Node_ _Send_ _Protocol_ _Data_ _Command_ .

Use Supervision (1 bit)

This field is used to indicate if the Z-Wave API Module requests the Supervision encapsulation for
this command.

 - The value 0 MUST indicate that the Z-Wave Module MUST NOT use Supervision encaspulation.

 - The value 1 MUST indicate that the Z-Wave Module MUST use Supervision encapsulation.

Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 318


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


**4.11.3.3** **2.** **Response** **data** **frame** **(host** **→Z-Wave** **Module)**


None.


**4.11.3.4** **3.** **Callback** **data** **frame** **(host** **→Z-Wave** **Module)**


A maximum time of 65 seconds is expected for the callback. A Z-Wave module MUST issue a callback
frame formatted according to Table 4.343


Table 4.343: Request Protocol Command Class Encryption         - Callback data frame


Session Identifier (8 bits)

Refer to _Session_ _identifier_ _(8_ _bits)_ .

Tx Status (8 bits)

Refer to _Tx_ _Status_ _(8_ _bits)_ .

Tx Status Report (N bytes)

This field is used to report detailed information about the Z-Wave frame transmission.

For field description, refer to _Tx_ _Status_ _Report_ _(N_ _bytes)_ .

## 4.12 Proprietary Commands


A Z-Wave module manufacturer MAY implement proprietary Z-Wave API commands. The command
identifier for the proprietary command MUST be one of the identifiers allocated in Table 4.344. Refer
to the manufacturer’s documentation for details on which command identifiers they use.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 319


Specifcations **Z-Wave** **API** **Specifcation,** **Release** **2.9.0** August 20, 2025


Table 4.344: Proprietary Commands

Command Identifer

0xDE
0xDF
0xF0
0xF1
0xF2
0xF3
0xF4
0xF5
0xF6
0xF7
0xF8
0xF9
0xFA
0xFB
0xFC
0xFD
0xFE

## References


[device_type_spec_v2] Z-Wave Alliance, Z-Wave Plus v2 Device Type Specification

[device_type_spec] Z-Wave Alliance, Z-Wave Plus Device Type Specification

[device_class_spec] Z-Wave Alliance, Z-Wave Device Class Specification

[zwave_nwk_spec] Z-Wave Alliance, ZWA_Z-Wave and Z-Wave Long Range Network Layer Specification_SPE.

[zwave_manufacturer_ids] Z-Wave Alliance, List of defined Manufacturer IDs.

[zwave_management_cc_spec] Z-Wave Alliance, Z-Wave Management Command Class Specification

[zwave_encapsulation_cc_spec] Z-Wave Alliance, Z-Wave Transport-Encapsulation Command Class
Specification


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 320


