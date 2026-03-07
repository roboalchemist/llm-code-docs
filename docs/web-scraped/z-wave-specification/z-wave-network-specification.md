# **Network Layer Specification**

_**Release**_ _**5.9.0**_

## **Z-Wave Alliance**


**Aug** **20,** **2025**

## Table of contents


1 Preamble 8
1.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.2 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.3 Audience and Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.4 Revision Record . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.5 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11


2 INTRODUCTION 12
2.1 Z-Wave technology overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2 Z-Wave Long Range technology overview . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3 Network layer specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.4 Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


3 Z-WAVE PROTOCOL OVERVIEW 14
3.1 The Z-Wave protocol stack architecture . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.2 Network Layer reference model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.3 Z-Wave definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.3.1 Z-Wave network topology basic principles . . . . . . . . . . . . . . . . . . . . . 17
3.3.2 Controller and end nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.3.3 Network topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3.4 Z-Wave controller roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3.4.1 Primary Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3.4.2 Secondary Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3.4.3 SUC Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.3.4.4 SIS Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.3.4.5 Inclusion Controllers . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.3.5 Node operation modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.3.5.1 Always Listening (AL) . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.3.5.2 Frequently Listening (FL) . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.3.5.3 Non-Listening (NL) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.3.6 Network addressing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20


4 Z-WAVE NETWORK LAYER SPECIFICATION 21
4.1 General Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.1.1 Z-Wave NWK Layer overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
4.1.2 Network Layer Data Entity (NLDE) . . . . . . . . . . . . . . . . . . . . . . . . 21
4.1.2.1 Network Layer Management Entity (NLME) . . . . . . . . . . . . . . 22
4.2 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.2.1 NPDU formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4.2.2 Routed NPDUs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
4.2.2.1 General routing header format . . . . . . . . . . . . . . . . . . . . . . 24
4.2.2.1.1 Routed Speed Modified (1 bit) / Failed Hop (4 bits) . . . . . 25
4.2.2.1.2 Extended Header (1 bit) . . . . . . . . . . . . . . . . . . . . 25
4.2.2.1.3 R-Err (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2.2.1.4 R-Ack (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2.2.1.5 Direction (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2.2.1.6 Repeaters (4 bits) . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2.2.1.7 Hops (4 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2.2.1.8 Repeater 0 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . 27
4.2.2.1.9 Repeater 1 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . 27
4.2.2.1.10 Repeater 2 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . 27
4.2.2.1.11 Repeater 3 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . 27
4.2.2.1.12 _Destination_ Wake Up (8 bits) . . . . . . . . . . . . . . . . . 27
4.2.2.1.13 Extended Header Body Length (4 bits) . . . . . . . . . . . . 27
4.2.2.1.14 Extended Header Type (4 bits) . . . . . . . . . . . . . . . . . 27
4.2.2.2 Extended headers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.2.2.2.1 Destination Wake Up Type . . . . . . . . . . . . . . . . . . . 28
4.2.2.2.2 Incoming Routed RSSI Type . . . . . . . . . . . . . . . . . . 28
4.2.2.3 Routing Frames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.2.2.3.1 Routed frame . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.2.2.3.2 Routed Acknowledgment frame . . . . . . . . . . . . . . . . . 30
4.2.2.3.3 Routed Error frame . . . . . . . . . . . . . . . . . . . . . . . 30
4.2.3 Explore NPDUs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.2.3.1 Explore frame general header format . . . . . . . . . . . . . . . . . . . 30
4.2.3.1.1 Version (3 bits) . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.2.3.1.2 Command (5 bits) . . . . . . . . . . . . . . . . . . . . . . . . 31
4.2.3.1.3 Direction (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.2.3.1.4 Source Routed (1 bit) . . . . . . . . . . . . . . . . . . . . . . 31
4.2.3.1.5 Stop (1 bit) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.2.3.1.6 Session Tx Random Interval (8 bits) . . . . . . . . . . . . . . 32
4.2.3.1.7 TTL (4 bits) . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.2.3.1.8 Repeater Count (4 bits) . . . . . . . . . . . . . . . . . . . . . 32
4.2.3.1.9 Repeater 0 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . 32
4.2.3.1.10 Repeater 1 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . 32
4.2.3.1.11 Repeater 2 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2.3.1.12 Repeater 3 (8 bits) . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2.3.2 Normal Explore Frame . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2.3.2.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2.3.2.2 Fields description . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2.3.2.3 Additional payload . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2.3.3 Inclusion Request Explore Frame . . . . . . . . . . . . . . . . . . . . . 34
4.2.3.3.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.2.3.3.2 Fields description . . . . . . . . . . . . . . . . . . . . . . . . 34
4.2.3.3.3 Additional payload . . . . . . . . . . . . . . . . . . . . . . . . 34
4.2.3.4 Search Result Explore Frame . . . . . . . . . . . . . . . . . . . . . . . 35
4.2.3.4.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.2.3.4.2 Fields description . . . . . . . . . . . . . . . . . . . . . . . . 35
4.2.3.4.3 Additional payload . . . . . . . . . . . . . . . . . . . . . . . . 36
4.3 Command Frames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
4.3.1 No Operation Command Class . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.3.2 Z-Wave Protocol Command Class . . . . . . . . . . . . . . . . . . . . . . . . . 38


4.3.2.1 Node Information Frame Command . . . . . . . . . . . . . . . . . . . 40
4.3.2.1.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.3.2.1.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 43
4.3.2.1.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 43
4.3.2.2 Request Node Information Frame Command . . . . . . . . . . . . . . 44
4.3.2.2.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 44
4.3.2.2.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 44
4.3.2.2.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 44
4.3.2.3 Assign IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.3.2.3.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.3.2.3.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.3.2.3.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.3.2.4 Find Nodes in Range Command . . . . . . . . . . . . . . . . . . . . . 46
4.3.2.4.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.3.2.4.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.3.2.4.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 47
4.3.2.5 Get Nodes in Range Command . . . . . . . . . . . . . . . . . . . . . . 49
4.3.2.5.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.3.2.5.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.3.2.5.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.3.2.6 Range Info Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
4.3.2.6.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 50
4.3.2.6.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.3.2.6.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 51
4.3.2.7 Command Complete Command . . . . . . . . . . . . . . . . . . . . . 52
4.3.2.7.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.3.2.7.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.3.2.7.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.3.2.8 Transfer Presentation Command . . . . . . . . . . . . . . . . . . . . . 53
4.3.2.8.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3.2.8.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3.2.8.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 54
4.3.2.9 Transfer Node Information Command . . . . . . . . . . . . . . . . . . 55
4.3.2.9.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.3.2.9.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.3.2.9.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 55
4.3.2.10 Transfer Range Information Command . . . . . . . . . . . . . . . . . 56
4.3.2.10.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.3.2.10.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.3.2.10.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.3.2.11 Transfer End Command . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.3.2.11.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 57
4.3.2.11.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.3.2.11.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 58
4.3.2.12 Assign Return Route Command . . . . . . . . . . . . . . . . . . . . . 59
4.3.2.12.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 59
4.3.2.12.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.3.2.12.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.3.2.13 New Node Registered Command . . . . . . . . . . . . . . . . . . . . . 61
4.3.2.13.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 61
4.3.2.13.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 61
4.3.2.13.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 62
4.3.2.14 New Range Registered Command . . . . . . . . . . . . . . . . . . . . 63
4.3.2.14.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.3.2.14.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 64
4.3.2.14.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 64
4.3.2.15 Transfer New Primary Controller Complete Command . . . . . . . . . 65
4.3.2.15.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 65
4.3.2.15.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 65


4.3.2.15.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 65
4.3.2.16 Automatic Controller Update Start Command . . . . . . . . . . . . . 66
4.3.2.16.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 66
4.3.2.16.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 66
4.3.2.16.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 66
4.3.2.17 SUC Node ID Command . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.3.2.17.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.3.2.17.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.3.2.17.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.3.2.18 Set SUC Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.3.2.18.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.3.2.18.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.3.2.18.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.3.2.19 Set SUC ACK Command . . . . . . . . . . . . . . . . . . . . . . . . . 69
4.3.2.19.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 69
4.3.2.19.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 69
4.3.2.19.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 69
4.3.2.20 Assign SUC Return Route Command . . . . . . . . . . . . . . . . . . 70
4.3.2.20.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.3.2.20.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.3.2.20.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.3.2.21 Static Route Request Command . . . . . . . . . . . . . . . . . . . . . 71
4.3.2.21.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 71
4.3.2.21.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 71
4.3.2.21.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 71
4.3.2.22 Lost Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
4.3.2.22.1 Frame format . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
4.3.2.22.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 72
4.3.2.22.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 72
4.3.2.23 Accept Lost Command . . . . . . . . . . . . . . . . . . . . . . . . . . 74
4.3.2.23.1 Frame Format: . . . . . . . . . . . . . . . . . . . . . . . . . . 74
4.3.2.23.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 74
4.3.2.23.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 74
4.3.2.24 NOP Power Command . . . . . . . . . . . . . . . . . . . . . . . . . . 75
4.3.2.24.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 75
4.3.2.24.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.3.2.24.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.3.2.25 Reserve Node IDs Command . . . . . . . . . . . . . . . . . . . . . . . 77
4.3.2.25.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.3.2.25.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.3.2.25.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.3.2.26 Reserved IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.3.2.26.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.3.2.26.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.3.2.26.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.3.2.27 Nodes Exist Command . . . . . . . . . . . . . . . . . . . . . . . . . . 79
4.3.2.27.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 79
4.3.2.27.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 79
4.3.2.27.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 79
4.3.2.28 Nodes Exist Reply Command . . . . . . . . . . . . . . . . . . . . . . . 80
4.3.2.28.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 80
4.3.2.28.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 80
4.3.2.28.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 80
4.3.2.29 Set NWI Mode Command . . . . . . . . . . . . . . . . . . . . . . . . 81
4.3.2.29.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 81
4.3.2.29.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 81
4.3.2.29.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 81
4.3.2.30 Exclude Request Command . . . . . . . . . . . . . . . . . . . . . . . . 82
4.3.2.30.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 82


4.3.2.30.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.3.2.30.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.3.2.31 Assign Return Route Priority Command . . . . . . . . . . . . . . . . 83
4.3.2.31.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 83
4.3.2.31.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 83
4.3.2.31.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 83
4.3.2.32 Assign SUC Return Route Priority Command . . . . . . . . . . . . . 84
4.3.2.32.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 84
4.3.2.32.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 84
4.3.2.32.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 84
4.3.2.33 SmartStart Included Node Information Command . . . . . . . . . . . 85
4.3.2.33.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 85
4.3.2.33.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.3.2.33.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.3.2.34 SmartStart Prime Command . . . . . . . . . . . . . . . . . . . . . . . 87
4.3.2.34.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 87
4.3.2.34.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 87
4.3.2.34.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 87
4.3.2.35 SmartStart Inclusion Request Command . . . . . . . . . . . . . . . . 88
4.3.2.35.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 88
4.3.2.35.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 88
4.3.2.35.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 88
4.4 Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
4.5 Functional Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
4.5.1 Routing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
4.5.1.1 Assigning Return Routes . . . . . . . . . . . . . . . . . . . . . . . . . 91
4.5.1.2 Priority Routes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
4.5.1.3 General Routing Requirements . . . . . . . . . . . . . . . . . . . . . . 91
4.5.1.3.1 AL Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
4.5.1.3.2 Repeating Frames . . . . . . . . . . . . . . . . . . . . . . . . 92
4.5.1.3.3 FL and NL Nodes . . . . . . . . . . . . . . . . . . . . . . . . 92
4.5.1.4 Successfully Delivered Routed Frame . . . . . . . . . . . . . . . . . . 92
4.5.1.4.1 Channel Configuration 1,2 . . . . . . . . . . . . . . . . . . . 92
4.5.1.4.2 Channel Configuration 3 . . . . . . . . . . . . . . . . . . . . 93
4.5.1.5 Routed Singlecast to an FL Node Destination . . . . . . . . . . . . . 94
4.5.1.5.1 Channel Configuration 1,2 . . . . . . . . . . . . . . . . . . . 95
4.5.1.5.2 Channel Configuration 3 . . . . . . . . . . . . . . . . . . . . 96
4.5.1.6 Unsuccessful Routed Frame with Routed Error Frame . . . . . . . . . 96
4.5.1.7 Unsuccessful Routed Frame Without Routed Error Frame . . . . . . . 97
4.5.1.8 Normal and Search Result Explore frames . . . . . . . . . . . . . . . . 98
4.5.2 Learn Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
4.5.3 Network Formation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
4.5.4 Network Inclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
4.5.4.1 Classic Network Inclusion . . . . . . . . . . . . . . . . . . . . . . . . . 102
4.5.4.2 Network Wide Inclusion (NWI) . . . . . . . . . . . . . . . . . . . . . 104
4.5.4.3 SmartStart Inclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
4.5.4.3.1 SmartStart Supporting Nodes Power-Up . . . . . . . . . . . 106
4.5.4.3.2 Not Included Nodes . . . . . . . . . . . . . . . . . . . . . . . 106
4.5.4.3.3 Included Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . 108
4.5.4.3.4 SmartStart Including Controllers . . . . . . . . . . . . . . . . 108
4.5.4.3.5 Successful SmartStart Inclusion . . . . . . . . . . . . . . . . 109
4.5.4.3.6 Unsuccessful SmartStart Inclusion . . . . . . . . . . . . . . . 112
4.5.5 Network Exclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
4.5.5.1 Classic Network Exclusion . . . . . . . . . . . . . . . . . . . . . . . . 114
4.5.5.2 Network Exclusion From a Foreign Network . . . . . . . . . . . . . . 115
4.5.5.3 Network Wide Exclusion (NWE) . . . . . . . . . . . . . . . . . . . . . 117
4.5.6 Failing Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
4.5.6.1 Remove a Failing Node . . . . . . . . . . . . . . . . . . . . . . . . . . 119
4.5.6.1.1 AL and FL Nodes . . . . . . . . . . . . . . . . . . . . . . . . 119


4.5.6.1.2 NL nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
4.5.7 Controller Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
4.5.7.1 Role transitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
4.5.7.2 Primary Controller Shift . . . . . . . . . . . . . . . . . . . . . . . . . 121
4.5.7.3 Give the SUC/SIS Role . . . . . . . . . . . . . . . . . . . . . . . . . . 122
4.5.8 Inclusion Controllers functionalities . . . . . . . . . . . . . . . . . . . . . . . . . 124
4.5.8.1 Add New Nodes on behalf of the SIS . . . . . . . . . . . . . . . . . . 124
4.5.8.2 Remove Nodes on behalf of the SIS . . . . . . . . . . . . . . . . . . . 125
4.5.9 Network Maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
4.5.9.1 Automatic Controller Update . . . . . . . . . . . . . . . . . . . . . . . 127
4.5.9.2 SUC updates by the Primary Controller . . . . . . . . . . . . . . . . . 130
4.5.9.3 Controller Replication . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
4.5.9.4 Neighbour Discovery / Range Test . . . . . . . . . . . . . . . . . . . . 132
4.5.9.5 End Node Route Request . . . . . . . . . . . . . . . . . . . . . . . . . 134


5 Z-WAVE LONG RANGE PROTOCOL OVERVIEW 137
5.1 The Z-Wave Long Range Protocol Stack Architecture . . . . . . . . . . . . . . . . . . 137
5.2 Z-Wave Long Range Network Layer Reference Model . . . . . . . . . . . . . . . . . . . 138
5.3 Z-Wave Long Range Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
5.3.1 Z-Wave Long Range Network Principles . . . . . . . . . . . . . . . . . . . . . . 139
5.3.2 Controller and End Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
5.3.3 Network Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
5.3.4 Z-Wave Controller Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
5.3.5 Node Operation Modes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
5.3.5.1 Wake On Event End Node (WOEEN) . . . . . . . . . . . . . . . . . . 139
5.3.6 Network Addressing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140


6 Z-WAVE LONG RANGE NETWORK LAYER SPECIFICATION 141
6.1 General Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
6.1.1 Z-Wave Long Range NWK Layer Overview . . . . . . . . . . . . . . . . . . . . 141
6.1.2 Network Layer Data Entity (NLDE) . . . . . . . . . . . . . . . . . . . . . . . . 141
6.1.2.1 Network Layer Management Entity (NLME) . . . . . . . . . . . . . . 141
6.2 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
6.2.1 NPDU formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
6.3 Command Frames . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
6.3.1 Z-Wave Long Range Command Class . . . . . . . . . . . . . . . . . . . . . . . 144
6.3.1.1 No Operation Command . . . . . . . . . . . . . . . . . . . . . . . . . 145
6.3.1.1.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 145
6.3.1.1.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 145
6.3.1.1.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 145
6.3.1.2 Node Information Frame Command . . . . . . . . . . . . . . . . . . . 146
6.3.1.2.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 146
6.3.1.2.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 147
6.3.1.2.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 147
6.3.1.3 Request Node Information Frame Command . . . . . . . . . . . . . . 148
6.3.1.3.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 148
6.3.1.3.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 148
6.3.1.3.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 148
6.3.1.4 Assign IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
6.3.1.4.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 149
6.3.1.4.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 149
6.3.1.4.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 149
6.3.1.5 Exclude Request Command . . . . . . . . . . . . . . . . . . . . . . . . 150
6.3.1.5.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 150
6.3.1.5.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 150
6.3.1.5.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 150
6.3.1.6 SmartStart Included Node Information Command . . . . . . . . . . . 151
6.3.1.6.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 151
6.3.1.6.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 151
6.3.1.6.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 151


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


6.3.1.7 SmartStart Prime Command . . . . . . . . . . . . . . . . . . . . . . . 152
6.3.1.7.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 152
6.3.1.7.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 152
6.3.1.7.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 152
6.3.1.8 SmartStart Inclusion Request Command . . . . . . . . . . . . . . . . 153
6.3.1.8.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 153
6.3.1.8.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 153
6.3.1.8.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 153
6.3.1.9 Exclude Request Confirmation Command . . . . . . . . . . . . . . . . 154
6.3.1.9.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.3.1.9.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.3.1.9.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.3.1.10 Non Secure Inclusion Step Complete Command . . . . . . . . . . . . 155
6.3.1.10.1 Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . 155
6.3.1.10.2 When Generated . . . . . . . . . . . . . . . . . . . . . . . . . 155
6.3.1.10.3 Effect on Receipt . . . . . . . . . . . . . . . . . . . . . . . . . 155
6.4 Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
6.5 Functional Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
6.5.1 Communication between Z-Wave Long Range Nodes . . . . . . . . . . . . . . . 157
6.5.1.1 Wake On Event End Node (WOEEN) . . . . . . . . . . . . . . . . . . 157
6.5.2 Learn Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
6.5.3 Network Formation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
6.5.4 Z-Wave Long Range Network Inclusion . . . . . . . . . . . . . . . . . . . . . . 160
6.5.4.1 SmartStart Inclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . 160
6.5.4.1.1 SmartStart Supporting Nodes Power-Up . . . . . . . . . . . 160
6.5.4.1.2 SmartStart Including Controllers . . . . . . . . . . . . . . . . 162
6.5.4.1.3 Successful SmartStart Inclusion . . . . . . . . . . . . . . . . 162
6.5.4.1.4 Unsuccessful SmartStart Inclusion . . . . . . . . . . . . . . . 164
6.5.4.1.5 Inclusion of Wake On Event End Nodes . . . . . . . . . . . . 166
6.5.5 Z-Wave Long Range Network Exclusion . . . . . . . . . . . . . . . . . . . . . . 167
6.5.5.1 Network Exclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
6.5.5.2 Network Exclusion From a Foreign Network . . . . . . . . . . . . . . 168
6.5.6 Failing nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
6.5.6.1 Remove a Failing Node . . . . . . . . . . . . . . . . . . . . . . . . . . 170
6.5.6.1.1 AL and FL Nodes . . . . . . . . . . . . . . . . . . . . . . . . 170
6.5.6.1.2 NL Nodes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
6.5.6.1.3 Wake On Event End Nodes . . . . . . . . . . . . . . . . . . . 171
6.5.7 Controller Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172
6.5.8 Dual Z-Wave and Z-Wave Long Range Networks . . . . . . . . . . . . . . . . . 173


References 174


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 7


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 1 Preamble 1.1 Description


This specification defines the Network (NWK) layer for ITU-T G.9959 compliant transceivers and
Z-Wave long Range transceivers, which enables network operations and routing on Z-Wave networks.
Implementations claiming compliance with this specification can be used with an application layer to
certify Z-Wave and Z-Wave long range products.

Reviewed and approved by the Z-Wave Alliance Core Stack Working Group (CSWG).

## 1.2 Disclaimer


THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.

## 1.3 Audience and Requirements


The audience of this document is the Z-Wave Alliance members and Z-Wave developers.

Recipients of this document are requested to submit, with their comments, notification of any relevant
patent claims or other intellectual property rights of which they may be aware that might be infringed
by any implementation of the Specification set forth in this document, and to provide supporting
documentation.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 8


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 1.4 Revision Record


Table 1.1: Revision History



























© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 9


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Table 1.1               - continued from previous page





























© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 10


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 1.5 Abbreviations


Table 1.2: Abbreviations


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 11


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 2 INTRODUCTION 2.1 Z-Wave technology overview


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

## 2.2 Z-Wave Long Range technology overview


Z-Wave Long Range provides an extended range version of the Z-Wave technology, targeting deployments over a kilometer radius, suitable in both indoors and outdoors areas. All Z-Wave applications
can run using either the Z-Wave or the Z-Wave Long Range PHY/MAC.

The Z-Wave Long Range protocol does not use any mesh routing and employs only direct range
communication.

The Z-Wave Long Range protocol also operate in the unlicensed industrial, scientific, and medical
(ISM) bands. The specific frequency band varies from region to region and the frequency bands are
defined in [ZWALRPHY], [ZWALRMAC].

## 2.3 Network layer specification


This specification presents the Z-Wave and Z-Wave Long Range Network Layer definitions that will
be implemented by devices operating in Z-Wave and Z-Wave Long Range networks. The Network
Layer features in relation to the OSI reference model and other layers is presented in Section 3.1 and
Section 5.1.

## 2.4 Glossary


The key words shall, should and may are formally used to indicate requirement levels in this document:

 - Shall:

This word indicates that the definition is an absolute requirement of the specification.

 - Should:

This word indicates that there may exist valid reasons in particular circumstances to ignore an item,
but the full implications must be understood and carefully weighed before choosing a different course.

 - May:

This word indicates that an item is truly optional. One vendor may choose to include the item because
a marketplace requires it or because the vendor feels that it enhances the product while another vendor
may omit the same item.

An implementation which does not include an option shall be prepared to interoperate with another
implementation which does include the option, though perhaps with reduced functionality. In the
same vein an implementation which does include an option shall be prepared to interoperate with


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 12


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


another implementation which does not include the option (except, of course, for the feature the
option provides.)

The use of the key words shall, should and may is compliant with the requirement levels used in ITU
recommendations.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 13


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 3 Z-WAVE PROTOCOL OVERVIEW


The Z-Wave protocol is a low bandwidth half duplex protocol designed for reliable wireless communication in a low-cost control network. The main purpose of the protocol is to enable short message
transportation in a reliable manner. The Z-Wave protocol is not designed to transfer a large amount
of data or any kind of streaming or timing critical data.

## 3.1 The Z-Wave protocol stack architecture


The Open System Interconnection (OSI) reference model is a representation system for characterizing
and standardizing the functions of a communication system in terms of abstraction layers. This
allows us to describe similar communication functionalities into logical layers. The 7 layers of the OSI
model are regarded by many as an idealized model; too abstract and fine-grained for most real-world
protocols. It is however useful to refer to the OSI model when describing a given communication
protocol framework. With respect to that, the Z-Wave protocol stack would be described using the
model as shown in Figure 3.1. Note that the Z-Wave application layer consists of the OSI stack layers
knows as transport, session, presentation and application.





Routing Management Network Management (i.e., node inclusion/exclusion)














|MLDE-SAP MLME-SAP|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|
||PLDE-SAP||PLME-SAP||
|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|



Z-Wave Alliance
Layer Interface Layer Function
Defined


Figure 3.1: Z-Wave Protocol Stack Architecture



ITU-T G9959
Defined



As depicted in Figure 3.1, the Z-Wave protocol stack is made up of OSI layers where each layer
performs set of services for the upper layer. Each layer has two main interfaces to facilitate the
communication with upper layers through a Service Access Point (SAP). The interfaces are described
as a data entity and management entity that provide a data transmission service and all other services,
respectively.

[ITUTG9959] defines the physical and medium access control layers.

 - The physical layer offers a data flow control between the MAC and PHY layers and adds
PHY-related management headers. The PHY layer is responsible for activation and deactiva

© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 14


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


tion of the radio transceiver, data transmission and reception, frequency selection, clear channel
assessments, and the link budget assessment of received frames.

    - The MAC layer defines the Z-Wave data transfer model and frame structure. During a Z-Wave
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

The Z-Wave application layer is responsible for building applications using dedicated Command
NWK:002E.1 Classes, (defined in [ZWAACC], [ZWAMCC], [ZWATECC], [ZWANPCC]). In order to be certifiable,
applications shall comply with Z-Wave device types defined in [ZWADT] and [ZWADTV2]. Finally,
the applications layer is also responsible for providing some network management functionalities using
the NWK interface (for details, refer to [ZWART]).

This specification defines NWK layer. The upper and lower layers are outside the scope of this
specification.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 15


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 3.2 Network Layer reference model


The Network Layer (NWK) provides an interface between the application layer and the MAC layer.
The NWK layer relies on services provided by the MAC layer and offers services to higher layers
though the Network Layer Data Entity (NLDE) and Network Layer Management Entity (NLME)
service point interfaces. The NLME provides management service interface where the NWK layer
management functionalities can be invoked. The NLME is responsible for maintaining a Network
Information Base (NIB) that contains the routing information of the network. Figure 3.2 illustrates
the components and interface of NWK layer.







Figure 3.2: Network Layer Reference Model


NWK:0022.1 The Z-Wave NWK layer shall provide two services to the Application layer that are accessed through
two SAPs:

    - The data service, accessed through NLDE-SAP, and

    - The network management service accessed through the NLME-SAP.

The detailed description of the Z-Wave NWK functional model is presented in Section 4.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 16


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 3.3 Z-Wave definitions


**3.3.1** **Z-Wave** **network** **topology** **basic** **principles**


The following is a summary of the basic Network topology principles established by [ITUTG9959]:

1. Groups of nodes are divided into domains:

  - The division of physical nodes into domains is logical. Domains may fully or partially
overlap each other’s radio frequency ranges.

  - The Z-Wave Network Layer supports up to 2 [32] domains.

  - Each domain is identified by a unique HomeID.

  - Management of different domains in the same physical media is handled by individual
domain masters.

2. The domain is a set of nodes connected to the same medium:

  - One node in the domain operates as a domain master, known as the Primary Controller.

  - Each domain may contain up to _232_ nodes (including the domain master).

  - Each node in the domain is identified by a NodeID that is unique within the actual domain.

  - Nodes of the same domain can communicate with each other either directly or via other
nodes in the same domain.

3. Nodes of different G.9959 domains:

  - The Z-Wave Network Layer provides connectivity within one domain.

In some cases, frames from a foreign domain are repeated into the current domain.
Inter-domain communication is beyond the scope of this specification.

4. The network is self-healing:

  - Nodes may autonomously establish new routes on demand.

Full mesh routing is supported. There is no requirement for star or tree network topologies.


**3.3.2** **Controller** **and** **end** **nodes**


The Z-Wave network layer defines two networking node types: controller and end.

The controller nodes are responsible for setting up and maintaining the Z-Wave network. They
can include or exclude nodes and they are aware for the network topology. This allows controllers
to determine the possible routes between any two nodes in the network. Controllers can exchange
network topology with each other.

End nodes can only be added or removed from a network by a controller, they do not calculate
routes, and they simply rely on route information provided by the controllers. Note that end nodes
can send commands to other nodes and “control” other nodes functionalities at the application level.
Both controller and end nodes can participate in mesh routing. It enables nodes within a network to
communicate with each other even when they are out of direct communication range.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 17


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**3.3.3** **Network** **topology**


In this specification, network topology refers to the list of nodes present in a network as well the list
of direct range neighbours for each node.

Figure 3.3 illustrates the concept of network topology.


Direct range connectivity

Network node
Topology Data:










|Node|Neighbors|
|---|---|
|10|4, 8|
|4|10, 8, 6|
|6|4, 8, 3|
|8|10, 4, 6, 5|
|3|6|
|5|8|





Figure 3.3: Network Topology Example


**3.3.4** **Z-Wave** **controller** **roles**


A Z-Wave controller is a node that has the capability to provide network management functionalities such as adding/removing nodes to/from a network and distributing network topology to other
controllers. The NWK layer defines several controller roles in a network:


**3.3.4.1** **Primary** **Controller**


The Primary Controller is by default the controller that starts the network. The Primary Controller
can always be used to set up and maintain a network. It can add/remove nodes and knows the network
topology.

There can be only one Primary Controller in a network.

The Primary Controller may offer additional services to other controllers:

A Primary Controller can handover the Primary Controller (and/or SUC/SIS) role to another controller.


**3.3.4.2** **Secondary** **Controller**


All controllers that are not the Primary Controller are Secondary Controllers.

If the Primary Controller does not have any SUC/SIS capability, a Secondary Controller cannot
include nodes, exclude nodes, or receive updated network topology automatically.

If a SUC is present in the network, a Secondary Controller can request updated network topology at
any time.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 18


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**3.3.4.3** **SUC** **Controller**


A Static Update Controller (SUC) is the controller that has the responsibility to keep the network
topology and distribute it to other controllers, on demand.

There can be only one SUC in a network. Both Primary Controllers and Secondary Controllers can
be SUC.


**3.3.4.4** **SIS** **Controller**


A SUC ID Server (SIS) Controller is a controller that has both the SUC Controller role and the
Primary Controller role. In addition, it provides the SIS functionality. The SIS functionality consists
in the ability to reserve NodeIDs to other controllers for enabling them to include and exclude nodes.


**3.3.4.5** **Inclusion** **Controllers**


If the Primary Controller is the SIS, Secondary Controllers in the same network become Inclusion
Controllers. Inclusion Controllers are secondary controllers that can include and exclude nodes on
behalf of the SIS.


**3.3.5** **Node** **operation** **modes**


Z-Wave nodes may operate in three different receiving modes.


**3.3.5.1** **Always** **Listening** **(AL)**


AL nodes’ RF receiver is always on and these nodes participate in mesh routing by repeating Routed
NPDUs and Explore NPDUs.


**3.3.5.2** **Frequently** **Listening** **(FL)**


FL nodes’ RF receiver is turned off most of the time. The RF receiver is turned on at regular intervals
for a short duration to listen the Wake Up Beams. AL nodes can reach FL nodes by issuing a Wake
Up Beam prior to issuing commands to the FL nodes.

FL nodes do not participate in routing and do not repeat Routed NPDUs and Explore NPDUs.

[ITUTG9959] defines two possible Wake Up intervals FL nodes: 250ms and 1000ms, and three channel
configurations.

When operating with a channel configuration 1 and 2, some NWK commands/frames indicate which
setting to use (250ms or 1000ms).

When operating with channel configuration 3, the 1000ms setting is always used in frames/commands,
despite using fragmented beams.

For more details, refer to [ITUTG9959].


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 19


NWK:0001.1


NWK:0002.1



Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**3.3.5.3** **Non-Listening** **(NL)**


NL nodes cannot be awakened by another node. They wake up and transmit frames at fixed configured
intervals to a single NodeID destination.

NL nodes reporting can be configured using the Wake Up Command Class. For more details, refer to

[ZWAMCC].


**3.3.6** **Network** **addressing**


Z-Wave supports the following types of addressing:

 - Singlecast

 - Multicast

 - Broadcast

The type of addressing and its frame format are defined in the MPDU Header (refer to [ITUTG9959]).

In this specification, some commands shall not be sent using multicast addressing and shall be ignored
if received via multicast addressing. In these cases, the Z-Wave Multicast frame and the broadcast
NodeID (0xFF) shall both be considered multicast addressing methods.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 20


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 4 Z-WAVE NETWORK LAYER SPECIFICATION 4.1 General Description


The Z-Wave Network Layer provides transmission services for higher layers using services provided
by the MAC layer. The Z-Wave NWK layer services include:

    - multi-hop routing.

    - route discovery.

    - routing acknowledgment.

    - managing the information that enables communication to FL nodes.

    - network formation and maintenance.

The Z-Wave NWK accommodates delivery of the application messages across multiple hops.


**4.1.1** **Z-Wave** **NWK** **Layer** **overview**


The network layer is required to provide functionality to ensure correct operation of the [ITUTG9959]
MAC sub-layer, and it provide a suitable service interface to the application layer. To interface with
the application layer, the network layer conceptually includes two service entities that provide the
necessary functionalities. These service entities are the data service and the management service. The
Z-Wave NWK layer data entity (NLDE) provides the data transmission service via its associated SAP
(NLDE-SAP), and the Z-Wave NWK layer management entity (NLME) provides the management
service via its associated SAP (NLME-SAP). The NLME utilizes the NLDE to achieve some of its
management tasks and it also maintains a database known as the Network Information Base (NIB)
that contains information regarding the network topology.


**4.1.2** **Network** **Layer** **Data** **Entity** **(NLDE)**


NWK:0003.1 The NLDE shall provide a data service for the application layer to transport Data Link Protocol Data
Unit (DLPDU) to a destination located in the same network.

[ITUTG9959] introduces the DLPDU, and it must contain the application data as depicted Figure
4.1.

|1/2|1|0/n|
|---|---|---|
|Command Class|Command|Command payload|
|DLPDU header<br>DLPDU|DLPDU header<br>DLPDU|DLPDU header<br>DLPDU|



Figure 4.1: DLPDU Format


NWK:0004.1 The NLDE shall provide the following services:



NWK:0005.1


NWK:0006.1




 - Generation of NPDUs (Network Protocol Data Unit): The NLDE shall be capable to generate
appropriate NPDUs from application data.

 - Routing: The NLDE shall be able to transmit an NPDU to the appropriate node that will either
be a repeater along the route or the destination.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 21


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.1.2.1** **Network** **Layer** **Management** **Entity** **(NLME)**


NWK:0007.1 The NLME shall provide a management service to leverage the network’s routing capabilities. The

NWK:0008.1 NLME shall provide the following services:

    - Route Discovery: this is the ability to discover a valid route to a destination for subsequent
messages.

    - Reception Control: this is the ability to ensure that a routed NPDU can be delivered correctly,
including communication control information for FL nodes.

    - Routing: this is the ability to leverage AL nodes in the network as repeaters to carry a message
to a destination that is not in direct range.

    - Network Inclusion: This is the ability to join or create a network.

    - Network Exclusion: This is the ability to leave a network.

    - Network Maintenance: This is the ability to monitor the health of a network and create a
neighbour topology and a routing table.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 22


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 4.2 Frame Format


The Z-Wave Network layer routing provides mesh networking functionality allowing to deliver messages
through repeater nodes.

The Network layer also provides route discovery, using special frames called Explore Frames.

NWK:0009.1 When the network layer receives data units from upper layers, it shall add routing information and
forward the received data to the MAC layer.


**4.2.1** **NPDU** **formats**


This clause specifies the format of the NPDU. Each NPDU consists of the following components:

    - An optional NPDU Header, comprising routing information

    - NSDU (Network Service Data Unit), encapsulating frame specific data payload.







|Col1|Col2|Col3|NSDU|Col5|Col6|
|---|---|---|---|---|---|
|PHY Header|MPDU Header|NPDU Header|DLPDU|FCS|End of Frame|
|||NPDU|NPDU|||


Figure 4.2: General NPDU Format


[ITUTG9959] introduces a Frame Control field in the MPDU Header. This field dictates the format
of the NPDU. The Frame Control field format is shown for information in Table 4.1 and Table 4.2,


Table 4.1: MDPU Header Frame Control Field (Channel configuration 1,2)


Table 4.2: MDPU Header Frame Control Field (Channel configuration 3)


This document specifies two types of network layer frames:

1. Routed NPDUs

2. Explore NPDUs

Table 4.3 shows the MPDU Frame Control configuration for a Routed NPDU.


Table 4.3: Routed NPDU Configuration


The Routed NPDU shall use the format outlined in Figure 4.3.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 23


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025







|n|Col2|Col3|NSDU|Col5|Col6|
|---|---|---|---|---|---|
|PHY Header|MPDU Header|Routing Header|DLPDU|FCS|End of Frame|
|||NPDU|NPDU|||


Figure 4.3: Routed NPDU Format


Table 4.4 shows the MPDU Frame Control configuration for an Explore NPDU.


Table 4.4: Explore NPDU Configuration


In this case, the NPDU shall use the format outlined in Figure 4.4.












|8 n|Col2|Col3|Col4|NSDU|Col6|Col7|
|---|---|---|---|---|---|---|
|PHY Header|MPDU Header|Explore Frame<br>generic header|Explore Frame<br>specific payload|DLPDU|FCS|End of Frame|
|||NPDU|NPDU|NPDU|||



Figure 4.4: Explore NPDU Format


**4.2.2** **Routed** **NPDUs**


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
NWK:000A.1 Routed NPDUs shall use Singlecast addressing.


**4.2.2.1** **General** **routing** **header** **format**


NWK:0205.1 Routed NPDUs shall use a routing header that can be described in a general manner according

NWK:0206.1 to Table 4.5 for channel configuration 1,2 (NWK:0205.1) and Table 4.6 for channel configuration 3
(NWK:0206.1).


Table 4.5: General Routing Header Format, channel configuration
1,2











© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 24


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Table 4.6: General Routing Header Format, channel configuration
3











**4.2.2.1.1** **Routed** **Speed** **Modified** **(1** **bit)** **/** **Failed** **Hop** **(4** **bits)**


If the R-Err field is set to 0:

NWK:000B.1 - This field shall be parsed as Routed Speed Modified (1 bit).

    - This field is used to indicate if the current frame is a retransmission for which the link speed
has been downgraded.

For channel configuration 1,2:

NWK:000C.1 - This field may be set to 1 to indicate that this is a retransmission at lower speed and the
destination should not reuse this route as main route.

NWK:000D.1 - The “Speed Modified” subfield from the MPDU Frame Control [ITUTG9959] shall be ignored
and this field shall be used instead when a routing header is present.

For channel configuration 3:

NWK:000E.1 - This field is reserved. It shall be set to 0 by a sending node and ignored by a receiving node.

If the _R-Err_ field is set to 1:

NWK:000F.1 - This field shall be parsed as Failed Hop (4 bits).

NWK:0010.1 - This field shall indicate the Hop (repeater number) that did not get an acknowledgement for
the routed frame.


**4.2.2.1.2** **Extended** **Header** **(1** **bit)**


This field indicates if the current Routing Header contains an Extended Header.

NWK:0011.1 The value 0 shall indicate that the Routing Header does not contain any Extended Header field and
stops after the last Repeater field.

NWK:0012.1 The value 1 shall indicate that the Routing Header contains an Extended Header and includes the
Extended Header Type and Extended Header Body fields.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 25


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.2.2.1.3** **R-Err** **(1** **bit)**


This field is used to indicate that a routed frame could not be delivered to the next hop or destination
NodeID.

NWK:0013.1 The value 0 shall indicate no transmission error.

NWK:0014.1 The value 1 shall indicate that a routed frame was not delivered to the next Hop.


**4.2.2.1.4** **R-Ack** **(1** **bit)**


This field is used to indicate that a routed frame was delivered correctly to the destination NodeID.

NWK:0015.1 The value 0 shall indicate that a routed frame was not (yet) acknowledged by the destination NodeID.

NWK:0016.1 The value 1 shall indicate that a routed frame was acknowledged by the destination NodeID.


**4.2.2.1.5** **Direction** **(1** **bit)**


The Direction field indicates the direction of the frame.

NWK:0017.1 A node sending out a routed frame shall set this field to 0 (outgoing routed frame).

NWK:0018.1 A node replying with a Routed Error/Routed Acknowledgement shall set this field to 1. (reply to an
outgoing Routed Frame)


**4.2.2.1.6** **Repeaters** **(4** **bits)**


This field is used to indicate the total number of repeaters for the routed frame.

NWK:0019.1 This field shall be in the range 1…4.


**4.2.2.1.7** **Hops** **(4** **bits)**


This field is used to indicate the progress of the frame through the route. The Hops value represents
NWK:001A.1 the index of the next repeater that shall repeat (or receive) the routed frame.

NWK:001B.1 The source NodeID shall set this field to 0 when sending a routed frame and each repeater shall
increment this field when they forward the frame if the Direction field is set to 0.

NWK:001C.1 Each repeater shall decrement this field when they forward the frame if the Direction field is set to 1.

In general, the value shall be set to the next repeater in charge of repeating the frame. (i.e. the value
NWK:001D.1 0x00 indicates that repeater 0 shall repeat this frame, value 0x01 indicates that repeater 1 shall repeat
this frame, etc.).

The last repeater will set this field to the total number of repeaters + 1.

NWK:001E.1 When a routed frame returns to the source NodeID (e.g. a Routed Ack / Error), the Repeater 0 node
shall set this field to 0x0F.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 26


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.2.2.1.8** **Repeater** **0** **(8** **bits)**


This field is used to indicate the NodeID of the first repeater for this route.


**4.2.2.1.9** **Repeater** **1** **(8** **bits)**


This field is used to indicate the NodeID of the second repeater for this route.

NWK:001F.1 This field shall be omitted if the Repeaters field value is less than 2.


**4.2.2.1.10** **Repeater** **2** **(8** **bits)**


This field is used to indicate the NodeID of the third repeater for this route.

NWK:0020.1 This field shall be omitted if the Repeaters field value is less than 3.


**4.2.2.1.11** **Repeater** **3** **(8** **bits)**


This field is used to indicate the NodeID of the fourth repeater for this route.

NWK:0021.1 This field shall be omitted if the Repeaters field value is less than 4.


**4.2.2.1.12** _**Destination**_ **Wake** **Up** **(8** **bits)**


For channel configuration 1,2:

NWK:0023.1 - This field shall be omitted.

For channel configuration 3:

    - This field is used to indicate if the destination of the frame is an FL node and requires beaming
prior to delivering the frame.

NWK:0024.1 - The value 0x00 shall indicate that the destination is an AL node and can be forwarded the frame
immediately.

NWK:0025.1 - The value 0x02 shall indicate that the destination requires a Fragmented Beam prior to deliver
a frame.


**4.2.2.1.13** **Extended** **Header** **Body** **Length** **(4** **bits)**


This field is used to indicate the length in bytes of the _Extended_ _header_ _Body_ field.


**4.2.2.1.14** **Extended** **Header** **Type** **(4** **bits)**


NWK:0026.1 This field is used to indicate the type of the extended header. It shall be encoded according to Table
4.7.


Table 4.7: Extended Header Type Encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 27


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.2.2.2** **Extended** **headers**


**4.2.2.2.1** **Destination** **Wake** **Up** **Type**


This extended header is used to carry beaming information relative to the source NodeID and destination NodeID for the actual route.

When using this extension:

NWK:0027.1 - The Extended Header Body Length field shall be set to 1

NWK:0028.1 - The Extended Header Type field shall be set to 0.

NWK:0029.1 The Extended Header Body shall be a bitmask encoded according to Table 4.8.


Table 4.8: Destination Wake Up Extension Encoding















Destination beaming 1000ms (1 bit)

If this bit is set to 1, it indicates if the destination NodeID requires a Long Continuous Beam before
the frame can be delivered.

Destination beaming 250ms (1 bit)

If this bit is set to 1, it indicates if the destination NodeID requires a short Continuous Beam before
the frame can be delivered.

Source beaming 250ms (1 bit)

NWK:002A.1 This field is obsoleted. It shall be set to 0 by a sending node and ignored by a receiving node.

Source beaming 1000ms (1 bit)

NWK:002B.1 This field is obsoleted. It shall be set to 0 by a sending node and ignored by a receiving node.


**4.2.2.2.2** **Incoming** **Routed** **RSSI** **Type**


This extension is used to report RSSI levels when returning a Routed Acknowledgment frame.

When using this extension:

NWK:002C.1 - The Extended Header Body Length field shall be set to 4

NWK:002D.1 - The Extended Header Type field shall be set to 1.

NWK:002F.1 The _Extended_ _Header_ _Body_ field shall be encoded as shown in Table 4.9.


Table 4.9: Incoming Routed RSSI Type Extension Format


NWK:0030.1 The length of this extension shall always be 4 bytes, even if fewer repeaters are involved in routing
the frame.

NWK:0031.1 A node returning a Routed Acknowledgement shall set these fields to 0x7F.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 28


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Repeater 0 RSSI (8 bits)

This field indicates the RSSI with which the routed frame was received from Repeater 1 (or the
destination NodeID).

Repeater 1 RSSI (8 bits)

This field indicates the RSSI with which the routed frame was received from Repeater 2 (or the
destination NodeID).

Repeater 2 RSSI (8 bits)

This field indicates the RSSI with which the routed frame was received from Repeater 3 (or the
destination NodeID).

Repeater 3 RSSI (8 bits)

This field indicates the RSSI with which the routed frame was received from the destination NodeID.

NWK:0032.1 Each repeater shall update its respective RSSI byte with the RSSI value it measured when receiving
the repeated frame.

NWK:0033.1 Each RSSI value shall be encoded using signed representation and shall be according to Table 4.10.


Table 4.10: Repeater RSSI Field Encoding


**4.2.2.3** **Routing** **Frames**


**4.2.2.3.1** **Routed** **frame**


Table 4.11 shows the allowable frame subfield configuration for a Routed frame. Note that all frames
with this configuration are Routed frames.


Table 4.11: Routed Frame Subfield Configuration


NWK:0034.1 A routed frame may comprise a DLPDU data payload.

NWK:0035.1 If transmitting using Channel Configuration 1,2 to a FL node destination, a sending node shall include
the Destination Wake Up Extension if beaming is required prior to delivering the frame.

NWK:0036.1 A node sending a Routed frame shall not include the Incoming Routed RSSI Extension.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 29


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.2.2.3.2** **Routed** **Acknowledgment** **frame**


Table 4.12 shows the allowable frame subfield configuration for a Routed Acknowledgement frame.
Note that all frames with this configuration are Routed Acknowledgement frames.


Table 4.12: Routed Acknowledgement Frame Subfield Configuration


NWK:0037.1 A Routed Acknowledgement frame shall not comprise a DLPDU data payload.

NWK:0038.1 A node returning a Routed Acknowledgement shall not include the Destination Wake Up Extension.

NWK:0039.1 A node returning a Routed Acknowledgement should include the Incoming Routed RSSI Extension.
If using the Incoming Routed RSSI Extension, a sending node shall set the repeater 0..4 values to
0x7F.


**4.2.2.3.3** **Routed** **Error** **frame**


Table 4.13 shows the allowable frame subfield configuration for a Routed Error frame. Note that all
frames with this configuration are Routed Error frames


Table 4.13: Routed Error Frame Subfield Configuration


NWK:003A.1 A Routed Error frame shall not comprise a DLPDU data payload.

NWK:003B.1 A node returning a Routed Error shall not include the Destination Wake Up Extension.

NWK:003C.1 A node returning a Routed Error shall not include the Incoming Routed RSSI Extension.


**4.2.3** **Explore** **NPDUs**


Explore NPDUs are used to transmit a frame when the sending node does not know a route to the
destination.


**4.2.3.1** **Explore** **frame** **general** **header** **format**


NWK:0207.1 Explore NPDUs shall use a general header outlined in Table 4.14.


Table 4.14: Explore Frame General Header


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 30


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.2.3.1.1** **Version** **(3** **bits)**


NWK:003D.1 The _Version_ field indicates the type of explore frame being sent. A sending node shall set this field
to 0x01. All other values are reserved.


**4.2.3.1.2** **Command** **(5** **bits)**


NWK:003E.1 The _Command_ field indicates the type of Explore Frame being sent. It shall be encoded according to
Table 4.15.


Table 4.15: Explore Frame Header::Command Field Encoding


**4.2.3.1.3** **Direction** **(1** **bit)**


The _Direction_ field indicates the direction of the frame.

NWK:003F.1 A node sending out an Explore frame shall set this field to 0 (outgoing frame).

NWK:0040.1 A node returning an Explore Frame in response to another shall set this field to 1.

NWK:0041.1 The value 0 shall indicate that Repeater 0 shall be the first to repeat the frame.

NWK:0042.1 The value 1 shall indicate that the last repeater in the list shall be the first to repeat the frame.


**4.2.3.1.4** **Source** **Routed** **(1** **bit)**


NWK:0043.1 The Source Routed field indicates if the Explore Frame contains a valid route that repeaters shall
follow or if the repeaters shall add themselves when they forward the frame.

NWK:0044.1 The value 0 shall indicate that the initial repeater list is zeroed out and each node receiving the frame
will add itself into the repeater list and repeat the frame.

NWK:0045.1 The value 1 shall indicate that the initial repeater list is defined and shall be respected by repeaters.


**4.2.3.1.5** **Stop** **(1** **bit)**


The _Stop_ field is used to stop all current Explore Frame repeating. This is used to ensure that a frame
can be sent without excessive interference from Explore Frame repeating.

NWK:0046.1 The Stop field indicates that AL nodes shall abort repeating any queued Explore Frame.

A queued Explore Frame is an Explore Frame that has been queued for repeating but is waiting the
Session Tx Random Interval to expire before being sent.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 31


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.2.3.1.6** **Session** **Tx** **Random** **Interval** **(8** **bits)**


NWK:0047.1 The _Session_ _Tx_ _Random_ _Interval_ field shall indicate the back off time for each repeater, i.e. a delay
to apply before repeating an Explore Frame.

NWK:0048.1 This field shall be ignored if the _Command_ field is set to 0x02 (Explore Command Search Result), in
this case, the Explore Frame shall be repeated immediately.

NWK:0049.1 For an outgoing Explore Frame, repeater shall apply a back off in ms given by:


{︃



_𝑇𝑥𝑅𝑎𝑛𝑑𝑜𝑚𝐼𝑛𝑡𝑒𝑟𝑣𝑎𝑙_ =



50 + 200 _*_ ( _𝑅_ _−_ 1) + 2 _* 𝑅𝑎𝑛𝑑_ ( _𝑆_ ) _, 𝑅>_ 0


[0 _..𝑆_ ] _, 𝑅_ = 0



With:

    - R the Repeater Number (hop)

    - S the Session Tx Random Interval

    - Rand(x) a function returning a random number between 0 and x


**4.2.3.1.7** **TTL** **(4** **bits)**


NWK:004A.1 The _TTL_ field indicates how many more repeaters can the frame go through. A node sending a new
Explore Frame shall set this field to 4 and each repeater shall decrement this field.

NWK:004B.1 A node repeating an Explore frame shall:

    - decrement this field if the Direction field is set to 0.

    - increment this field if the Direction field is set to 1.

NWK:004C.1 If the _TTL_ field is set to 0x00 and the Direction field is set to 0, a receiving node shall not repeat the
Explore Frame.


**4.2.3.1.8** **Repeater** **Count** **(4** **bits)**


This field is used to indicate the total number of repeaters for the Explore Frame.

NWK:004D.1 This field shall be in the range 1..4.


**4.2.3.1.9** **Repeater** **0** **(8** **bits)**


The _Repeater_ _0_ field is used to indicate the NodeID of the first repeater for this Explore Frame.

NWK:004E.1 The value 0 shall indicate that the Explore Frame has not been repeated yet.


**4.2.3.1.10** **Repeater** **1** **(8** **bits)**


The _Repeater_ _1_ field is used to indicate the NodeID of the second repeater for this Explore Frame.

NWK:004F.1 The value 0 shall indicate that the Explore Frame has not been repeated by a second repeater yet.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 32


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.2.3.1.11** **Repeater** **2** **(8** **bits)**


The Repeater 2 field is used to indicate the NodeID of the third repeater for this Explore Frame.

NWK:0050.1 The value 0 shall indicate that the Explore Frame has not been repeated by a third repeater yet.


**4.2.3.1.12** **Repeater** **3** **(8** **bits)**


The _Repeater_ _3_ field is used to indicate the NodeID of the fourth repeater for this Explore Frame.

NWK:0051.1 The value 0 shall indicate that the Explore Frame has not been repeated by a fourth repeater yet.


**4.2.3.2** **Normal** **Explore** **Frame**


NWK:0208.1 The Subfield Configuration shall be formatted as illustrated in Table 4.16 for Normal Explore Frames.
Note that all frames with the _Command_ subfield set to 0x00 are Normal Explore Frames.


Table 4.16: Normal Explore Frame Subfield Configuration


NWK:0052.1 A sending node should set the Session Tx Random Interval subfield to _nwkRecommendedSession-_
_TxRandomInterval_ .


**4.2.3.2.1** **Frame** **format**


The Normal Explore Frame has no explore frame specific payload. Its format is shown in Table 4.17.


Table 4.17: Normal Explore Frame Format


**4.2.3.2.2** **Fields** **description**


There is no Command Specific Payload for a Normal Explore Frame, it will only comprise the Explore
Frame general header described in Section 4.2.3 Explore frame general header format.


**4.2.3.2.3** **Additional** **payload**


NWK:0053.1 A Normal Explore Frame may carry a DLPDU payload. Refer to Figure 4.4.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 33


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.2.3.3** **Inclusion** **Request** **Explore** **Frame**


NWK:0209.1 The Subfield Configuration shall be formatted as illustrated in Table 4.18 for Inclusion Request Explore
Frames. Note that all frames with the _Command_ subfield set to 0x01 are Inclusion Request Explore
frames.


Table 4.18: Inclusion Request Explore Frame Subfield Configuration


NWK:0054.1 A sending node should set the Session Tx Random Interval subfield to _nwkRecommendedSession-_
_TxRandomInterval_ .


**4.2.3.3.1** **Frame** **format**


NWK:0055.1 The Inclusion Request Explore Frame format shall comply with Table 4.19.


Table 4.19: Inclusion Request Explore Frame Format


**4.2.3.3.2** **Fields** **description**


Network HomeID (4 bytes)

This field is used to indicate the HomeID of the repeating nodes.

NWK:0056.1 This field shall be set to 0 by a node sending an Inclusion Request Explore Frame.

NWK:0057.1 A node repeating an Inclusion Request Explore Frame shall set this field to its HomeID.

This is the HomeID of the node repeating the frame. When NWI Mode is enabled, Inclusion Request
Explore Frames are repeated even if they belong to another HomeID.


**4.2.3.3.3** **Additional** **payload**


NWK:0058.1 An Inclusion Request Explore Frame shall carry a DLPDU using the Z-Wave Protocol Command
Class and one of the following commands:

    - Node Information Frame Command

    - SmartStart Prime Command

    - SmartStart Inclusion Request Command

    - SmartStart Included Node Information Command

NWK:0059.1 An Inclusion Request Explore Frame shall not carry any other commands than the list mentioned
above. This is illustrated in Figure 4.5.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 34


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025













|8 4|Col2|Col3|Col4|NSDU|Col6|Col7|
|---|---|---|---|---|---|---|
|PHY Header|MPDU Header|Inclusion Request<br>Explore Frame|Network<br>HomeID|NWK Command|FCS|End of Frame|
|||NPDU|NPDU|NPDU|||


Figure 4.5: Inclusion Request Explore Frame with Z-Wave NWK Command


**4.2.3.4** **Search** **Result** **Explore** **Frame**


NWK:020A.1 The Subfield Configuration shall be formatted as illustrated in Table 4.20 for Search Result Explore
Frames. Note that all frames with the _Command_ subfield set to 0x02 are Search Result Explore
frames.


Table 4.20: Search Result Explore Frame Subfield Configuration


**4.2.3.4.1** **Frame** **format**


NWK:005A.1 The Search Result Explore Frame format shall comply with Table 4.21.


Table 4.21: Search Result Explore Frame Format


**4.2.3.4.2** **Fields** **description**


NodeID (8 bits)

The _NodeID_ field is used to indicate the sending NodeID of the Normal Explore Frame for which the
Search Result Explore frame is returned.

Frame Handle (8 bits)

NWK:005B.1 The _Frame Handle_ field shall contain the Sequence number found in the MPDU Header of the Normal
Explore Frame for which the Search result Explore Frame is returned.

TTL result (4 bits)

The _TTL_ _Result_ field contains the value of the _TTL_ field as it was received by the destination NodeID
in the Normal Explore Frame that triggered the Search Result Explore Frame to be returned.

Repeater Count Result (4 bits)

The _Repeater_ _Count_ _Result_ field contains the value of the _Rpeater_ _Count_ field as it was received by
the destination NodeID in the Normal Explore Frame that triggered the Search Result Explore Frame
to be returned.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 35


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Repeater 0 Result (8 bits)

The _Repeater_ _0_ _Result_ field contains the value of the _Repeater_ _0_ field as it was received by the
destination NodeID in the Normal Explore Frame that triggered the Search Result Explore Frame to
be returned.

Repeater 1 Result (8 bits)

The _Repeater_ _1_ _Result_ field contains the value of the _Repeater_ _1_ field as it was received by the
destination NodeID in the Normal Explore Frame that triggered the Search Result Explore Frame to
be returned.

Repeater 2 Result (8 bits)

The _Repeater_ _2_ _Result_ field contains the value of the _Repeater_ _2_ field as it was received by the
destination NodeID in the Normal Explore Frame that triggered the Search Result Explore Frame to
be returned.

Repeater 3 Result (8 bits)

The _Repeater_ _3_ _Result_ field contains the value of the _Repeater_ _3_ field as it was received by the
destination NodeID in the Normal Explore Frame that triggered the Search Result Explore Frame to
be returned.


**4.2.3.4.3** **Additional** **payload**


NWK:005C.1 A Search Result Explore Frame shall not carry a DLPDU. This is illustrated in Figure 4.6.















|8 1 1 5|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|PHY Header|MPDU Header|Search Results<br>Explore Frame|NodeID|Frame<br>Handle|Search Results|FCS|End of Frame|
|||NPDU|NPDU|NPDU|NPDU|||


Figure 4.6: Search Result Explore Frame Format


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 36


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 4.3 Command Frames


The commands defined by the Z-Wave NWK layer are categorized in Command Classes. These
Command Classes are listed in Table 4.22.


Table 4.22: Z-Wave NWK Layer Command Classes







These Command Classes are designed for Z-Wave network formation and maintenance functionaliNWK:005D.1 ties. The following sections illustrates how the Network Layer Management (NLME) shall build the
individual commands for transmission.

NWK:0204.1 During the transmission of each of these commands, the NLME shall construct the network layer
protocol data (NPDU) part of the frame as illustrated in Figure 4.7.










|Col1|Col2|Col3|NSDU with NWK Command|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|0/n|0/n|0/n|1<br>0/1<br>0/m|1<br>0/1<br>0/m|1<br>0/1<br>0/m|||
|PHY Header|MPDU Header|NPDU Header|Command Class|Command|Command payload|FCS|End of Frame|
|||NPDU|NPDU|NPDU|NPDU|||



Figure 4.7: Z-Wave Network Layer Command Frame Format


The command format is identical to the DLPDU format defined in [ITUTG9959], comprising one
Command Class byte, one (optional) Command byte and an optional variable length Command Payload.

NWK:005E.1 NWK Commands shall not use any segmentation or encryption. No application payload shall be
added from upper layers. These are illustrated in Figure 4.8.

NWK:005F.2 Command Classes in the range 0x00..0x1F shall be considered as NWK Command Classes (both for
Z-Wave and Z-Wave Long Range).


### DLPDU





NWK with Command Class


(0x00..0x1F


MAC


PHY


|Col1|Appli. Command Classes<br>(0x20..0xFFFF)|
|---|---|
||S0/S2 Encryption (SEC)|
||Segmentation (SAR)|
||NWK|
||MAC|
||PHY|



Figure 4.8: Z-Wave and Z-Wave Long Range NWK Command Encapsulation


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 37


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.1** **No** **Operation** **Command** **Class**


This Command Class is a special command frame that is used by a Z-Wave network manager entity
to test the availability of a node in a network.

NWK:0060.1 The No Operation Command Class (NOP) shall be supported by all Z-Wave nodes. This command
class shall not have any associated commands or payload. Therefore, the network layer protocol
data shall only be composed of a Command Class byte with no payload during the transmission this
Command Class. This is shown in Table 4.23.


Table 4.23: NOP Command Class Format


NWK:0061.1 This Command Class may be used to verifying if an excluded node is still part of the network. This
Command may also be used on application level e.g. checking if a SUC/SIS is reachable from a new
node in the network.


**4.3.2** **Z-Wave** **Protocol** **Command** **Class**


This Command Class is used for setup and maintenance of networks. The Z-Wave Protocol Command
NWK:0062.1 Class shall be supported by all nodes. Some commands are used only for certain nodes types or network
roles (e.g. end nodes or controllers); and in this case, it will be indicated in the command themselves.

The Command frames defined by this Command Class are listed in Table 4.24.


Table 4.24: Z-Wave Protocol Command Class Commands









© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 38


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Table 4.24               - continued from previous page









© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 39


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.1** **Node** **Information** **Frame** **Command**


The Node Information Frame command is used to advertise the capabilities of the sending node.


**4.3.2.1.1** **Frame** **Format**


NWK:0063.1 The Node Information Frame Command shall be formatted as illustrated in Table 4.25.


Table 4.25: Node Information Frame Command Format

























Protocol Version (3 bits)

This field is used to advertise the version of the protocol that is implemented by the sending node.
NWK:0064.1 The Protocol Version field shall be formatted as indicated in Table 4.26.


Table 4.26: Protocol Version Bit Description


Supported Speed (3 bits)

The _Supported_ _Speed_ field indicates the transmission data rate supported by the sending node. This
NWK:0065.1 field shall be treated as a bitmask and shall have at least one speed bits set as depicted in Table 4.27.


Table 4.27: Speed Supported by the Node


NWK:0066.1 If this field is set to 0, (no bit is set to 1), a receiving node shall assume that the maximum supported
speed by the sending node is 9.6 kbits/second.

NWK:0067.1 The bits set in this field shall comply with channel configuration requirements from [ITUTG9959].

Speed Extension (3 bits)


NWK:0068.1


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 40


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


The _Speed_ _Extension_ field is used to describe the if the node support additional data rate to the ones
advertised in the Supported Speed field. This field shall be treated as a bitmask and shall be encoded
according to Table 4.28.

NWK:0069.1 The bits set in this field shall comply with channel configuration requirements from [ITUTG9959].


Table 4.28: Node Information Frame Command Speed Extension
Description


Routing (1 bit)

The _Routing_ field is used to indicate if the node can repeat Routed NPDUs and Explore NDPUs.

NWK:006A.2 This field shall be set if the network layer supports being a repeater. If the network layer does not
support being a repeater this field shall be set to 0.

NWK:006B.1 Controller nodes trying to calculate routes shall assume that nodes with both the _Routing_ field set to
1 and the _Listening_ field set to 1 will repeat frames.

Listening (1 bit)

The _Listening_ field is used to advertise if the node is always listening or not.

NWK:006C.1 AL nodes shall be set this field to 1.

NWK:006D.1 FL and NL nodes shall set this field to 0.

** RFU (1 bit)**

Reserved for future use.

For the record, previous specifications used this bit to indicate if a node supports secure communication. No implementation used this bit in the past. Therefore, this bit can be reused in the future.

Controller (1 bit)

NWK:0070.1 The _Controller_ field shall be set to 1 if the sending node is a controller, and to 0 if the sending node
is an end node.

NWK:0071.1 If this field is set to 1, the Node Information Frame Command shall include a _Basic_ _Device_ _Type_ field.

NWK:0072.1 If this field is set to 0, the _Routing_ _End_ _Node_ field shall be set to 1.

Specific Device (1 bit)

NWK:0073.1 This bit field shall set to 1 when the node information frame contains specific device type field.

Routing End Node (1 bit)

NWK:0074.1 The _Routing_ _End_ _Node_ field shall be set to 1 if the sending node is an end node.

NWK:0075.1 If this field is set to 1, the Node Information Frame Command shall not include a Basic Device Type
field.

NWK:0076.1 If this field is set to 0, the Controller bit field shall be set to 1.

Beam capability (1 bit)

This field is used to indicate if the sending node can issue Wake Up beams.

NWK:0077.1 The value 0 shall indicate that the sending node cannot wake up FL nodes.

The value 1 shall indicate that the sending node can wake up FL nodes.

Sensor 250ms (1 bit)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 41


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


This bit is set to 1 when the node is a FLiRS node and wakes up every 250ms to check if a wakeup
beam is present.

Sensor 1000ms (1 bit)

This bit is set to 1 when the node is a FLiRS node and wakes up every 1000ms to check if a wakeup
beam is present.

Optional Functionality (1 bit)

The _Optional_ _Functionality_ field is used to indicate that this node supports additional application
Command Classes to the mandatory minimum for the advertised Generic/Specific Device Class defined
in [ZWADC].

NWK:0078.1 Sending nodes should set this field to 1.

Basic Device Type (8 bits)

NWK:0079.1 The _Basic_ _Device_ _Type_ field shall be included in the Node Information Frame Command if the Controller field is set to 1.

NWK:007A.1 This field shall be omitted if the Controller field is set to 0.

NWK:007B.1 This field shall be encoded according to Table 4.29.


Table 4.29: Node Information Frame Command              - Basic Device
Type Encoding


Generic Device Class (8 bits)

The _Generic_ _Device_ Class field contains an identifier that identifies what Generic Device Class this
NWK:007C.1 node is part of and shall be set by the application.

For a detailed description of all available Generic Device Classes, refer to [ZWADC] for Z-Wave devices,

[ZWADT] for Z-Wave Plus devices, and [ZWADTV2] Z-Wave Plus v2 devices.

Specific Device Class (8 bits)

The _Specific_ _Device_ _Class_ field specifies what Specific Device Class is implemented by the node, and
NWK:007D.1 this shall be set by the application.

For a detailed description of all available Specific Device Classes, refer to [ZWADC] for Z-Wave devices,

[ZWADT] for Z-Wave Plus devices, and [ZWADTV2] Z-Wave Plus v2 devices.

Command Class (N bytes)

This field is used to advertise the list of Command Classes (Refer to [ZWAACC] [ZWAMCC], [ZWATECC] and [ZWANPCC]) supported by the sending node using non-secure communication.

NWK:007E.1 The _Command_ _Class_ field shall not be longer than 35 bytes.

The field shall advertise the list of Command Classes that the node supports. Command Classes
NWK:007F.1 advertised in this field shall be in the range 0x21..0xFFFF. Command Classes in the range 0x00..0x20
shall not be advertised in this field.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 42


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.1.2** **When** **Generated**


NWK:0080.1 When generated, the fields shall be configured as follow:

NWK:0081.1 - Protocol Version field shall be set to 0x03


**4.3.2.1.3** **Effect** **on** **Receipt**


On receipt of this command, a receiving node is notified of the sender’s Z-Wave capabilities and
non-secure supported Command Classes.



NWK:0082.1



If the network layer does not expect to receive a Node Information Frame Command (i.e. not in add
mode or did not issue a Request Node Information Frame Command), the command (or its data)
shall be forwarded to the upper protocol layer (application).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 43


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.2** **Request** **Node** **Information** **Frame** **Command**


This command is used to request a node to return a Node Information Frame Command.


**4.3.2.2.1** **Frame** **Format**


NWK:0083.1 The Request Node Information Frame Command shall be formatted as illustrated in Table 4.30.


Table 4.30: Request Node Information Frame Command Format


**4.3.2.2.2** **When** **Generated**


NWK:0084.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing.


**4.3.2.2.3** **Effect** **on** **Receipt**


NWK:0085.1 On receipt of this command, a receiving node shall return a Node Information Frame Command in
response. A receiving node shall not return a response if this command is received via multicast
addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 44


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.3** **Assign** **IDs** **Command**


This command is used to assign NodeID and HomeID to the receiving node.


**4.3.2.3.1** **Frame** **Format**


NWK:0086.1 The Assign IDs Command shall be formatted as illustrated in Table 4.31.


Table 4.31: Assign IDs Command Format









NodeID (8 bits)

The _NodeID_ field is used to assign or unassign a NodeID to a node.

NWK:0087.1 The value 0x00 shall indicate the node that it shall be excluded from the network.

Values in the range 0x01..0xE8 shall indicate the new NodeID assigned to the receiving node.

HomeID (4 bytes)

The _HomeID_ field is used to assign or unassign the HomeID to a node.

NWK:0088.1 The value 0x00000000 shall indicate the node that it shall be excluded from the network and assign
itself a random HomeID or NWI HomeID based on its S2 DSK.

Other values shall indicate the new HomeID assigned to the receiving node.


**4.3.2.3.2** **When** **Generated**


NWK:0089.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing.


**4.3.2.3.3** **Effect** **on** **Receipt**


NWK:008A.1 On receipt of this command, a receiving node shall update its HomeID and NodeID if and only if it
is currently in Learn Mode.

NWK:008B.1 A receiving node shall ignore the command if it is received via multicast addressing.

A receiving node shall ignore this command if is not in learn mode.

NWK:008C.1 A receiving node shall ignore this command if the NodeID field is set to a value greater than 0xE8.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 45


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.4** **Find** **Nodes** **in** **Range** **Command**


This command is used to request the receiving node to find the nodes in direct range.


**4.3.2.4.1** **Frame** **Format**


NWK:008D.1 The Find Nodes in Range Command shall be formatted as illustrated in Table 4.32.


Table 4.32: Find Nodes in Range Command Format









Reserved (2 fields)

NWK:008E.1 Reserved fields shall be set to 0 by a sending node and shall be ignored by a receiving node.

Speed Present (1 bit)

This field is used to advertise if this command frame contains the data rate to be used during neighbour
discovery.

NWK:008F.1 This field shall be set to 0 if the data rate option is not defined.

NWK:0090.1 This field shall be set to 1 if the data rate to be used is defined.

Bitmask Length (5 bits)

This field is used to advertise the length in bytes of the _Node_ _Bitmask_ field.

Node Bitmask (N bytes)

NWK:0091.1 This field is used to advertise the neighbouring nodes ID mask that the receiving node shall try to
reach in direct range during the range test.

NWK:0092.1 The length of this field in bytes shall be according to the _Bitmask_ _Length_ field value.

NWK:0093.1 This field shall be treated as a bit mask, and LSB in Node bitmask 1 represents Node 1. This field
shall be encoded as follow:

    - Bit 0 in Node bitmask 1 indicates the NodeID 1

    - Bit 1 in Node bitmask 1 indicates the NodeID 2

    - …

NWK:0094.1 The bit value 0 shall be used to advertise that the corresponding node should not try to find the node.

The bit value 1 shall be used to advertise that the corresponding node should try to find the node.

NWK:0095.1 The first byte of this field shall represent node 1..8.

Wake Up Time (optional Rx) (8 bits)

NWK:0096.1 This field is used to indicate the Wake Up beam duration that shall be used for waking up the all the
destination nodes present in the bitmask.

NWK:0097.1 All nodes present in the Node Bitmask field shall have the same Wake Up Time setting.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 46


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Table 4.33: Wake Up Time


NWK:0098.1 Note: This field shall be present in the frame when transmitting the Find Node in Range command,
and a receiving node shall verify if the field is present in the frame when parsing the frame.

NWK:0099.1 If this field is not present in the frame, a receiving node shall use the Wakeup Time value 0x00.

Data rate (optional Rx) (3 bits)

NWK:009A.1 The data rate to be used during neighbour discovery. Speed present bit shall be set to 1 when this
field is included. This field value shall be encoded according to Table 4.34.


Table 4.34: Find Node in Range Data Rate Encoding


NWK:009B.1 This field shall be present in the frame when a node transmits the Find Nodes in Range command,
and a receiving node shall verify if the field is present in the frame when parsing the frame.

NWK:009C.1 If this field is not present in the frame, a receiving node shall use the Data Rate value 0x01.


**4.3.2.4.2** **When** **Generated**


NWK:009D.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing.

NWK:009E.1 This command shall not be sent with the Node Bitmask field set to 0.


**4.3.2.4.3** **Effect** **on** **Receipt**


NWK:009F.1 On receipt of this command, a receiving node shall issue a NOP Power Command to all NodeIDs
indicated by the Node Bitmask field and subsequently return a Command Complete Command to the
node that initiated the range test.

NWK:00A0.1 All Z-Wave nodes shall keep a bitmask record of the last range test.

NWK:00A1.1 A receiving node shall ignore the command if it is received via multicast addressing.

This procedure is depicted in Figure 4.9.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 47


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.9: Range Test Procedure


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 48


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.5** **Get** **Nodes** **in** **Range** **Command**


The Get Nodes in Range Command is used to request the list of direct range neighbours detected
with the last range test.


**4.3.2.5.1** **Frame** **Format**


NWK:00A2.1 The Get Nodes in Range Command shall be formatted as illustrated in Table 4.35.


Table 4.35: Get Nodes in Range Command Format





Wake Up Time (optional)

NWK:020B.1 This field shall be identical to the field of the same name in the Find Nodes In Range command in
Section 4.3.2.4.


**4.3.2.5.2** **When** **Generated**


NWK:00A3.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing.


**4.3.2.5.3** **Effect** **on** **Receipt**


NWK:00A4.1 On receipt of this command, a receiving node shall return a Range Info Command.

NWK:00A5.1 A receiving node shall not return a response if this command is received via multicast addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 49


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.6** **Range** **Info** **Command**


The Range Info Command is used to advertise the list of direct range neighbours detected with the
last range test.


**4.3.2.6.1** **Frame** **Format**


NWK:00A6.1 The Range Info Command shall be formatted as illustrated in Table 4.36.


Table 4.36: Range Info Command Format









Reserved (3 bits)

Unused and must be set to zero.

Bitmask Length (5 bits)

This field advertise the length in bytes of the Node bitmask field.

Node bitmask (N bytes)

This field used to advertise the neighbouring nodes ID mask that describes the list of nodes in the
sending node vicinity.

NWK:00A7.1 The length of this field in bytes shall be according to the Bitmask Length field value.

NWK:00A8.1 This field shall be treated as a bit mask, and LSB in Node bitmask 1 represents Node 1. This field
shall be encoded as follow:

    - Bit 0 in Node bitmask 1 indicates the NodeID 1

    - Bit 1 in Node bitmask 1 indicates the NodeID 2

    - …

NWK:00A9.1 The bit value 0 shall be used to advertise that the corresponding node is not a neighbouring node that
the sending node can communicate with in direct range. The bit value 1 shall be used to advertise
that the corresponding node is a neighbouring node.

NWK:00AA.1 The first byte of this field shall represent node 1…8.

Wake up Time (optional Rx) (8 bits)

This field specifies the wakeup beam duration that was specified in the Find Nodes In Range frame.

NWK:00AB.1 Note: This field shall be present in the frame when transmitting the Range Info Command, and a
receiving node shall verify if the field is present in the frame when parsing the frame.

NWK:00AC.1 If this field is not present in the frame, a receiving node shall assume a Wakeup Time value 0x00.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 50


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.6.2** **When** **Generated**


NWK:00AD.1 The node bitmask field shall contain the result of the last range test initiated by the Find Nodes in
Range Command.

NWK:00AE.1 If no range test was initiated for the current network, the Node Bitmask field shall be set to 0x00.


**4.3.2.6.3** **Effect** **on** **Receipt**


On receipt of this command, a receiving node is notified of a list of nodes in direct range for the
sending node.

NWK:00AF.1 A receiving node shall not return a response if this command is received via multicast addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 51


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.7** **Command** **Complete** **Command**


This command is used to advertise the completion of a given task (i.e., range test, controller replication,
…) by the sending node.


**4.3.2.7.1** **Frame** **Format**


NWK:00B0.1 The Command Complete Command shall be formatted as illustrated in Table 4.37.


Table 4.37: Command Complete Command Format









Sequence Number (8 bits)

This field is used for duplicate detection for transmissions sequences that require multiple Command
Complete Commands.

NWK:00B1.1 If this field is set to 0x00, it shall indicate that the Sequence Number is not in use and it shall be
ignored by the receiving node.

NWK:00B2.1 If this field is in the range 0x01..0xFF, it shall indicate a unique sequence number for the current
operation.


**4.3.2.7.2** **When** **Generated**


NWK:00B3.1 When generated, the sending node shall be ready to receive more commands immediately after sending
the command. If the sending node needs to be unavailable for a short time, this command shall be
generated only when the node is available again.

NWK:00B4.1 This command shall not be sent via multicast addressing.

NWK:00B5.1 If used, the _Sequence_ _Number_ field value shall be incremented at each new transmission of the Command Complete Command.


**4.3.2.7.3** **Effect** **on** **Receipt**


On receipt of this command, a receiving node is notified of the sender’s has completed a requested
operation (optionally identified by the _Sequence_ _Number_ field).

NWK:00B6.1 A receiving node shall ignore this command if it is received via multicast addressing


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 52


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.8** **Transfer** **Presentation** **Command**


The Transfer Presentation Command is used by controller nodes to indicate that they are trying to
initiate network management functions, such as:

    - Add new nodes in the network

    - Remove nodes from a network

    - Perform a controller replication


**4.3.2.8.1** **Frame** **Format**


NWK:00B7.1 The Transfer Presentation Command shall be formatted as illustrated in Table 4.38.


Table 4.38: Transfer Presentation Command Format


Option (8 bits)

NWK:00B8.1 The _Option_ field is used to indicate the intent of the sending node. It shall be treated as a bitmask
and shall be encoded according to Table 4.39.


Table 4.39: Transfer Presentation Command              - Option Field Encoding


**4.3.2.8.2** **When** **Generated**


NWK:00B9.1 When generated, the sending node shall be ready to include or exclude a node from the network.

NWK:00BA.1 This command shall be sent to the broadcast destination (NodeID 0xFF).

NWK:00BB.1 The Option field bit 0 shall always be set to 1 by a sending node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 53


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.8.3** **Effect** **on** **Receipt**


NWK:00BC.1 On receipt of this command, a receiving node in learn mode shall return a Node Information Frame
Command to the sending node if the Option field matches the intent of the receiving node.

NWK:00BD.1 If the receiving node is not in learn mode or has already started an inclusion/exclusion procedure, it
shall not return a Node Information Frame Command.

If the receiving node current learn mode does not match the include/exclude options in the command,
NWK:00BE.1 it shall not return a Node Information Frame Command.

NWK:00BF.1 If the receiving node is in SmartStart Learn Mode, it shall not return a Node Information Frame
Command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 54


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.9** **Transfer** **Node** **Information** **Command**


This command is used for transferring a node’s Node Information Frame Command data from one
controller to another.


**4.3.2.9.1** **Frame** **Format**


NWK:00C0.1 The Transfer Node Information Command shall be formatted as illustrated in Table 4.40.


Table 4.40: Transfer Node Information Command Format



























NWK:00C1.1 All fields not described below shall be identical to the fields in the Node Information Frame Command.

Sequence number (8 bits)

NWK:00C2.1 A sending node shall specify a unique sequence number starting from a random value. Each new
message shall carry an increment of the value carried in the previous singlecast command.

NWK:00C3.1 A receiving node shall use this field for singlecast duplicate detection.

NodeID (8 bits)

This field is used to advertise the NodeID of the node to which belongs the node information data
carried in this command.


**4.3.2.9.2** **When** **Generated**


NWK:00C4.1 When generated, the Node Information Frame Command fields shall be set to identical values as
reported by the NodeID indicated in the _NodeID_ field in its Node Information Frame Command.

NWK:00C5.1 This command shall be sent as part of the inclusion of a controller as specified in Section 4.5.7 Primary
Controller Shift and Section 4.5.9 Controller Replication.


**4.3.2.9.3** **Effect** **on** **Receipt**


NWK:00C6.1 This command shall be ignored if it is received using multicast addressing.

NWK:00C7.1 This command shall be ignored if the receiving node is an end node.

NWK:00C8.1 This command shall be ignored if the receiving node is a controller node and it is received outside a
controller replication or inclusion process. Refer to Section 4.5.7.2 and Section 4.5.9.3.

NWK:00C9.1 On receipt of this command, a controller in learn mode shall update its internal node table with the
node information received in this command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 55


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.10** **Transfer** **Range** **Information** **Command**


This command is used to transfer a node’s range test results from one controller to another.


**4.3.2.10.1** **Frame** **Format**


NWK:00CA.1 The Transfer Range Information Command shall be formatted as illustrated in Table 4.41.


Table 4.41: Transfer Range Information Command Format





NWK:00CB.1 All fields not described below shall be identical to the fields in the Range Info Command.

Sequence number (8 bits)

NWK:00CC.1 A sending node shall specify a unique sequence number starting from a random value. Each new
message shall carry an increment of the value carried in the previous singlecast command.

NWK:00CD.1 A receiving node shall use this field for singlecast duplicate detection.

NodeID (8 bits)

This field is used to advertise the NodeID of the node to which belongs the range test results carried
in this command.


**4.3.2.10.2** **When** **Generated**


NWK:00CE.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing.

NWK:00CF.1 This command shall be sent as part of a controller replication or controller inclusion process. Refer
to Section 4.5.7.2 and Section 4.5.9.3 for details.


**4.3.2.10.3** **Effect** **on** **Receipt**


NWK:00D0.1 This command shall be ignored if it is received using multicast addressing.

NWK:00D1.1 This command shall be ignored if the receiving node is an end node.

NWK:00D2.1 This command shall be ignored if the receiving node is a controller and it is received outside a controller
replication process.

NWK:00D3.1 On receipt of this command, a controller in learn mode shall update its internal routing table with
the range information received in this command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 56


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.11** **Transfer** **End** **Command**


This command is used to advertise the end of the current network operation, which can be:

    - Static route request

    - Automatic controller update

    - Controller replication


**4.3.2.11.1** **Frame** **Format**


NWK:00D4.1 The Transfer End Command shall be formatted as illustrated in Table 4.42


Table 4.42: Transfer End Command Format









Status (8 bits)

NWK:00D5.2 This field is used to notify the Z-Wave network information transfer status. This field value shall be
encoded as shown in Table 4.43


Table 4.43: Z-Wave Network Transfer Status


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 57


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.11.2** **When** **Generated**


NWK:00D6.1 When generated, this command shall indicate that the current network management operation is
completed and shall advertise its status.

NWK:00D7.1 This command shall not be sent outside network management operations.


**4.3.2.11.3** **Effect** **on** **Receipt**


On receipt of this command, the receiving node can conclude that the sending node has completed
the requested actions and is ready to receive new commands or initiate new network management
operations.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 58


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.12** **Assign** **Return** **Route** **Command**


This command is used to advertise the assigned route to the receiving node.


**4.3.2.12.1** **Frame** **Format**


NWK:00D8.1 The Assign Return Route Command shall be formatted as illustrated in Table 4.44.


Table 4.44: Assign Return Route Command Format


Node ID (8 bits)

This field is used to advertise the NodeID of the destination for the assigned route.

The NodeID field may be different from the NodeID of the sending node.

Number of hops (4 bits)

This field is used to indicate the number of repeaters present in the frame.

NWK:00D9.1 The value 0 shall indicate that the route to the NodeID destination shall be a direct range transmission.

NWK:00DA.1 Values in the range 1..4 shall indicate the number of repeaters used in the route.

Route Number (3 bits)

NWK:00DB.1 This field is used to indicate a number of index to assign to the indicate route. The first assigned
route shall have route number 0.

Repeater (4 bytes)

This field is used to indicate the list of repeaters to be used in the route.

Destination Wake Up (2 bits)

NWK:00DC.1 This field indicates the destination node Wake Up time capability. The field shall be encoded as shown
in Table 4.45.


Table 4.45: Assign Return Route Command::Destination Wake Up
Encoding


Destination Speed (3 bits)

NWK:00DD.1 This bit field specifies the data rate capability of the destination node. This field shall encodes as
shown in Table 4.46.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 59


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Table 4.46: Assign Return Route Command::Destination Speed
Encoding


**4.3.2.12.2** **When** **Generated**


NWK:00DE.1 This command shall not be sent to controller nodes (i.e. nodes that set the Controller field to 1 in
their Node Information Frame Command).

NWK:00DF.1 This command shall not be sent for the SUC NodeID unless the return route is set as part of an
application level association. The Assign SUC Return Route Command shall be used instead if the
return route is set by the protocol.


**4.3.2.12.3** **Effect** **on** **Receipt**


NWK:00E0.1 On receipt of this command, an end node that supports storing return routes shall store the specified
route for use when transmitting frames to the destination specified in the frame.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 60


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.13** **New** **Node** **Registered** **Command**


This command is used to notify the SIS controller that an inclusion controller has included a new
node in the Z-Wave network.


**4.3.2.13.1** **Frame** **Format**


NWK:00E1.2 The New Node Registered Command shall be formatted as illustrated in Table 4.47.


Table 4.47: New Node Registered Command Format

























NWK:00E2.1 All fields not described below shall be identical to the Node Information Frame Command fields
described in Section 4.3.2.1.

NodeID (8 bits)

This field is used to advertise the NodeID that has been assigned to the new node.

Command Class 1-n (n*8 bits)

This field is used to advertise the supported Command Classes in the included node. This field should
contain the Command Classes received in the Node Information frame if available when sendiong this
frame.


**4.3.2.13.2** **When** **Generated**


NWK:00E3.1 When generated, except for the NodeID field, the fields values in this command shall contain the
values reported by the included node’s Node Information Frame Command during its inclusion.

NWK:00E4.2 If generated for a node removed from the network, the Generic Device Class field shall be set to 0 in
this command. All other fields after the NodeID may be set to zero.

NWK:00E5.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 61


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.13.3** **Effect** **on** **Receipt**


NWK:00E6.1 On receipt of this command, a controller node is notified of a new node added in the network. This
command shall be ignored by end nodes.

NWK:00E7.1 This command shall be ignored if it was received using multicast addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 62


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.14** **New** **Range** **Registered** **Command**


This command is used to advertise the range test results that a controller has performed when including
a new node in the Z-Wave network.


**4.3.2.14.1** **Frame** **Format**


NWK:00E8.1 The New Range Registered Command shall be formatted as illustrated in Table 4.48.


Table 4.48: New Range Registered Command Format









NodeID (8 bits)

NWK:00E9.1 This field shall indicate the NodeID for which the neighbour nodes (nodes in range) are advertised in
the Neighbour Nodes Bitmask field.

Neighbour Nodes Bitmask Length (5 bits)

NWK:00EA.1 This field shall advertise the length in bytes of the Neighbour Nodes Bitmask field. This field should
be set to the minimum value allowing to advertise all neighbour nodes for the advertised NodeID.

Neighbour Nodes Bitmask (N bytes)

NWK:00EB.1 This field shall indicate the NodeIDs that are reported as direct range neighbours by the last range
test for the actual NodeID.

NWK:00EC.1 The length of this field in bytes shall be according to the Neighbour Nodes Bitmask Length field value.

NWK:00ED.1 This field shall be treated as a bitmask, and the first bit in the LSB represents NodeID 1. This field
shall be encoded as follow:

    - Bit 0 in Node bitmask 1 shall represent the NodeID 1

    - Bit 1 in Node bitmask 1 shall represent the NodeID 2

    - …

NWK:00EF.1 The bit value 0 shall be used to advertise that the corresponding NodeID is not a neighbour for the
actual NodeID (advertised in the NodeID field).

The bit value 1 shall be used to advertise that the corresponding NodeID is a neighbour for the actual
NodeID (advertised in the NodeID field).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 63


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.14.2** **When** **Generated**


NWK:00F0.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing.

NWK:00F1.1 This command shall only be sent as part of the following procedures:

    - Section 4.5.8.1 Add new nodes on behalf of the SIS

    - Section 4.5.9.1 Automatic Controller Update


**4.3.2.14.3** **Effect** **on** **Receipt**


On receipt of this command, the receiving node is notified of the new direct range topology around
the NodeID advertised in the command.

NWK:00F2.1 End nodes shall ignore this command.

NWK:00F3.1 This command shall be ignored if it was received using multicast addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 64


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.15** **Transfer** **New** **Primary** **Controller** **Complete** **Command**


This command is used to complete the Primary Controller role transfer procedure to another controller
node.


**4.3.2.15.1** **Frame** **Format**


NWK:00F4.1 The Transfer New Primary Controller Complete Command shall be formatted as illustrated in Table
4.49.


Table 4.49: Transfer New Primary Controller Complete Command
Format


Controller Type (8 bits)

This field is used to indicate the type of the controller.

NWK:00F5.1 A sending node shall set this field to the same value as the Generic Device Class field in its Node
Information Frame Command.


**4.3.2.15.2** **When** **Generated**


The Transfer New Primary Controller Complete Command is generated as part of the Primary Controller Shift procedure. Refer to Section 4.5.7.2 Primary Controller Shift for details.


**4.3.2.15.3** **Effect** **on** **Receipt**


On receipt of this command, the receiving node is notified it has now the Primary Controller role in
the network.

NWK:00EE.1 If the receiving node is in learn mode, it shall assume the Primary Controller role and may use Primary
Controller functionalities. Refer to Section 4.5.7 Controller Roles for details.

NWK:00F6.1 If the receiving node is not in learn mode, it shall ignore this command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 65


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.16** **Automatic** **Controller** **Update** **Start** **Command**


This command is used to request transfer of the network topology information from the SUC/SIS
controller to another controller in a network.


**4.3.2.16.1** **Frame** **Format**


NWK:00F7.1 The Automatic Controller Update Start Command shall be formatted as illustrated in Table 4.50.


Table 4.50: Automatic Controller Update Command Format


**4.3.2.16.2** **When** **Generated**


NWK:00F8.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing. This command should only be sent to the SUC/SIS controller.

NWK:00F9.1 This command shall be sent from an Inclusion Controller in a network with a SUC/SIS controller
before starting to add a new node to the network.

Refer to Section 4.5.8.1 Add New Nodes on Behalf of the SIS.

NWK:00FA.1 This command may be sent periodically by an inclusion controller to ensure that its network topology
is updated. It should not be more than once a day.


**4.3.2.16.3** **Effect** **on** **Receipt**


NWK:00FB.1 If the receiving node is a SUC/SIS controller, it shall send topology updates to the sending node using
New Node Registered Commands and New Range Registered Commands. Refer to Section 4.5.9.1
Automatic Controller Update for details.

NWK:00FC.1 If the receiving node is not a SUC/SIS controller, it should return a SUC Node ID command to the
sending node to inform the correct Node ID of the SUC/SIS.

NWK:00FD.1 This command shall be ignored if it was received using multicast addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 66


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.17** **SUC** **Node** **ID** **Command**


This command is used to advertise the Node ID of the SUC and its capabilities.


**4.3.2.17.1** **Frame** **Format**


NWK:00FE.1 The SUC Node ID Command shall be formatted as illustrated in Table 4.51.


Table 4.51: SUC Node ID Command Format









NodeID (8 bits)

This field is used to advertise the NodeID of the SUC Controller.

NWK:00FF.1 The value 0x00 shall indicate that there is no SUC in the network.

Values in the range 1..232 shall indicate the NodeID of the SUC Controller for this network.

SUC Capabilities (optional Rx) (8 bits)

NWK:0100.1 This field is used to indicate the capabilities of the SUC node. It shall be treated as a bitmask and
shall be encoded according to Table 4.52.


Table 4.52: SUC Node ID Command              - SUC Capabilities Encoding


NWK:0101.1 Older implementations may omit this field from the command. If this field is not present in the frame,
the value 0x00 shall be assumed.


**4.3.2.17.2** **When** **Generated**


NWK:0102.1 A sending node shall not send this command to the NodeID indicated in the _NodeID_ field.


**4.3.2.17.3** **Effect** **on** **Receipt**


On receipt of this command, the receiving node is notified of the SUC’s identity and its capabilities
(SUC only or with SIS functionality).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 67


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.18** **Set** **SUC** **Command**


This command is used by a Primary Controller to grant the SUC Role to another controller for the
current network.


**4.3.2.18.1** **Frame** **Format**


NWK:0103.1 The Set SUC Command shall be formatted as illustrated in Table 4.53.


Table 4.53: Set SUC Command Format









State (8 bits)

NWK:0104.1 This field is used to advertise the state of the controller functionality. The field value shall be set to
0x01 to enable the SUC functionality.

NWK:0105.1 All other values are reserved and shall by ignored by receiving nodes.

SUC Capabilities (8 bits)

NWK:0106.1 This field is used to specify which service the SUC should be running. It shall be treated as a bitmask
and encoded according to Table 4.52.


**4.3.2.18.2** **When** **Generated**


NWK:0107.1 The SUC Capabilities field shall be set to 0x01.

NWK:0108.1 This command shall only be sent by a node that has the Primary Controller role. This command shall
not be transmitted to end nodes and shall only be sent to controllers.


**4.3.2.18.3** **Effect** **on** **Receipt**


NWK:0109.1 On receipt of this command, the receiving node shall assume the SUC role if it has the capabilities.

NWK:010A.1 A receiving node shall return a Set SUC ACK Command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 68


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.19** **Set** **SUC** **ACK** **Command**


This command is used to respond to a Set SUC Command.


**4.3.2.19.1** **Frame** **Format**


NWK:010B.1 The Set SUC ACK Command shall be formatted as illustrated in Table 4.54.


Table 4.54: Set SUC ACK Command Format









Result (8 bits)

This field is used to advertise a status of taking the SUC role for the network.

NWK:010C.1 If the sending node has accepted to take the SUC role, this field shall be set to 0x01.

If the sending node has not accepted or cannot take the SUC role, this field shall be set to 0x00.

SUC Capabilities (8 bits)

NWK:010D.1 This field is used to indicate the capabilities of the SUC node. It shall be treated as a bitmask and
shall be encoded according to Table 4.52.


**4.3.2.19.2** **When** **Generated**


The SUC Node ID Command is generated in response to the Set SUC Command.


**4.3.2.19.3** **Effect** **on** **Receipt**


On receipt of this command, the node that initiated a SUC role transfer is notified of the operation’s
result together with the capabilities of the SUC node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 69


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.20** **Assign** **SUC** **Return** **Route** **Command**


This command is used to notify the receiving node about the route on how to reach the SUC.


**4.3.2.20.1** **Frame** **Format**


NWK:010E.1 The Assign SUC Return Route Command shall be formatted as illustrated in Table 4.55.


Table 4.55: Assign SUC Return Route Command Format


The fields from this command are identical to the fields in the Assign Return Route Command.


**4.3.2.20.2** **When** **Generated**


NWK:010F.1 The _NodeID_ field shall be set to the SUC NodeID.

NWK:0110.1 This command shall be sent by a controller when it includes an end node and a SUC/SIS is present
in the network. Refer to Section 4.5.4.1 and Section 4.5.4.2 Classic Network Inclusion and Network
Wide Inclusion (NWI).


**4.3.2.20.3** **Effect** **on** **Receipt**


NWK:0111.1 On receipt of this command, the node should update its route for the SUC NodeID and learns which
NodeID is the SUC in the network.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 70


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.21** **Static** **Route** **Request** **Command**


This command is used to request static routes for one or more NodeID destinations.


**4.3.2.21.1** **Frame** **Format**


NWK:0112.1 The Static Route Request Command shall be formatted as illustrated in Table 4.56.


Table 4.56: Static Route Request Command Format


Destination NodeID (5 bytes)

This field is used to indicate a list of destination for which return routes are needed.

NWK:0113.1 For each byte, a value in the range 1..232 shall indicate a NodeID for which a return route is requested.

NWK:0114.1 For each byte, the value 0x00 shall indicate that the byte is unused.


**4.3.2.21.2** **When** **Generated**


NWK:0115.1 This command should not be sent. Refer to Section 4.5.1.1 Assigning Return routes.

NWK:0116.1 If used, this command shall be sent to the SUC/SIS.


**4.3.2.21.3** **Effect** **on** **Receipt**


NWK:0117.1 On receipt of this command, a controller node shall respond with Assign Return Route Commands
to the sending node. Routes shall be assigned for all the Destination NodeIDs in the command. For
details, refer to Section 4.5.9.5 End Node Route Request.

NWK:0118.1 An end node shall ignore this command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 71


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.22** **Lost** **Command**


This command is used to request help from another node in the network to locate the SUC/SIS in
the network.


**4.3.2.22.1** **Frame** **format**


NWK:0119.1 The Lost Command shall be formatted as illustrated in Table 4.57.


Table 4.57: Lost Command Format









NodeID (8 bits)

The node ID of the node that originally requested help.


**4.3.2.22.2** **When** **Generated**


NWK:011A.1 This command is obsoleted and shall not be transmitted.


**4.3.2.22.3** **Effect** **on** **Receipt**


NWK:011B.1 On receipt of this command a Non SUC/SIS node shall forward this command to the SUC/SIS if it
knows the SUC/SIS NodeID. This command shall be ignored in a network without SUC/SIS.

NWK:011C.1 On receipt of this command, a SUC/SIS controller should send an Accept Lost Command, perform a
Neighbour Discovery (refer to Section 4.5.9.4 Neighbour Discovery / Range test), issue an Assign SUC
Return Route Command and Transfer End Command to the lost end node. This process is illustrated
in Figure 4.10


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 72


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.10: Lost End Node Recovery Process


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 73


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.23** **Accept** **Lost** **Command**


The Accept Lost Command is used to indicate that the SUC has accepted to help a lost node.


**4.3.2.23.1** **Frame** **Format:**


NWK:011D.1 The Accept Lost Command shall be formatted as illustrated in Table 4.58.


Table 4.58: Accept Lost Command Format









Accepted (8 bits)

This field is used to indicate if the SUC node has accepted to help the lost end node.

NWK:011E.1 The value 0x04 shall indicate that the sending node has refused to help the lost end node.

The value 0x05 shall indicate that the sending node has accepted to help the lost end node.

NWK:011F.1 All other values are reserved. Reserved values shall not be used by a sending node and shall be ignored
by a receiving node.


**4.3.2.23.2** **When** **Generated**


NWK:0120.1 When generated, a SUC Controller shall perform a Neighbour Discovery (refer to Section 4.5.9.4
Neighbour Discovery / Range test), issue an Assign SUC Return Route Command and Transfer End
Command to the lost end node. This process is illustrated in Figure 4.10.

NWK:0121.1 This command shall not be sent by a node that does not have the SUC role in the network.


**4.3.2.23.3** **Effect** **on** **Receipt**


On receipt of this command, lost end nodes are informed that the lost recovery process has started.

This process is illustrated in Figure 4.10.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 74


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.24** **NOP** **Power** **Command**


This command is used to verify if a node is in direct range and used for Neighbour Discovery.


**4.3.2.24.1** **Frame** **Format**


NWK:0122.1 The NOP Power Command shall be formatted as illustrated in Table 4.59.


Table 4.59: NOP Power Command Format











Tx Power Register (Obsolete) (8 bits)

NWK:0123.1 This field shall not be used when sending this command.

NWK:0124.1 If no _Tx Power Dampening_ field is present in the command, this field should be converted to dampening
according to Table 4.60.


Table 4.60: NOP Power                - Tx Power Register Encoding


Tx Power Dampening (8 bits)

NWK:0125.1 This field is used to indicate which transmit power to use for sending a MPDU Ack to this frame.
This field shall be encoded according to Table 4.61.


Table 4.61: NOP Power               - Tx Power Dampening Encoding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 75


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.24.2** **When** **Generated**


NWK:0126.1 When generated, the Tx Power Register field shall be set to 0x00.

NWK:0127.1 The NOP Power Command shall be sent in direct range only, it shall not be sent in a Routed NPDU
or an Explore NPDU.

NWK:0128.1 A sending node shall apply the Tx Power Dampening indicated by the Tx Power Dampening field for
sending this command.


**4.3.2.24.3** **Effect** **on** **Receipt**


NWK:0129.1 On receipt of this command, the MPDU Ack frame should be transmitted with a Tx power that is
lowered according to the parameters in the frame. The dampening should be done from the default
Tx power configured in the receiving node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 76


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.25** **Reserve** **Node** **IDs** **Command**


This command is used by an inclusion controller to request NodeID(s) to the SIS that can be used to
add new nodes in the network.


**4.3.2.25.1** **Frame** **Format**


NWK:012A.1 The Reserved Node IDs Command shall be formatted as illustrated in Table 4.62.


Table 4.62: Reserve Node IDs Command Format


Number of Node IDs (bytes)

This field is used to indicate the number of requested NodeIDs.

NWK:012B.1 This field shall be in the range 1..10. This field should be set to 1 to avoid exhausting the NodeID
pool from the SIS.


**4.3.2.25.2** **When** **Generated**


NWK:012C.1 The Reserved Node IDs Command shall be sent to the SUC Node ID. It shall only be sent if the SUC
has Server ID Capabilities (SIS).

NWK:012D.1 This command shall only be sent by Inclusion Controller nodes.

NWK:012E.1 This command shall be sent using singlecast addressing and shall not be sent using multicast addressing.


**4.3.2.25.3** **Effect** **on** **Receipt**


NWK:012F.1 On receipt of this command, the SIS controller shall return a Reserved IDs Command in response. A
receiving node shall not return a response if this command is received via multicast addressing.

NWK:0130.1 All nodes that are not SIS controller in the network shall ignore this command.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 77


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.26** **Reserved** **IDs** **Command**


This command is used to advertise the granted NodeIDs to an Inclusion Controller.


**4.3.2.26.1** **Frame** **Format**


NWK:0131.1 The Reserved IDs Command shall be formatted as illustrated in Table 4.63.


Table 4.63: Reserved IDs Command Format









Number of IDs (8 bits)

This field is used to advertise the number of granted NodeIDs.

NWK:0132.1 This field shall be in the range 0..10.

Reserved NodeID (N bytes)

This field is used to advertise a list of granted NodeIDs.

NWK:0133.1 Each byte shall represent a granted NodeID that the Inclusion Controller can use for Network Inclusion.

NWK:0134.1 The length of this field shall be according to the value of the _Number_ _of_ _IDs_ field.


**4.3.2.26.2** **When** **Generated**


NWK:0135.1 The SIS node should provide as many reserved IDs as requested by the Inclusion Controller node in
the Reserved IDs Command.

NWK:0136.1 A SIS node may refuse to provide reserved NodeIDs.

NWK:0137.1 A node without the SIS role in the network shall not send this command.


**4.3.2.26.3** **Effect** **on** **Receipt**


On receipt of this command, an inclusion controller is notified of the NodeIDs that have been reserved
for it. These NodeID values can be used to include new nodes.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 78


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.27** **Nodes** **Exist** **Command**


The Nodes Exist Command is used to advertise a list of nodes currently present in the network.


**4.3.2.27.1** **Frame** **Format**


NWK:0138.1 The Node Exist Command shall be formatted as illustrated in Table 4.64.


Table 4.64: Nodes Exist Command Format











Node Mask Type (8 bits)

This field is used to advertise the type of nodes that the Node Mask advertises in this command.

NWK:0139.1 The value 0 shall indicate that all existing nodes present in the network are advertised in the Node
Mask field.

All other values are reserved.

Node Mask Length (8 bits)

This field is used to indicate the length of the Node Mask field in bytes.

Node Mask (N bytes)

This field is used to advertise the list of nodes present in the network for the type advertised by the
Node Mask Type field.

NWK:013A.1 The length of this field in bytes shall be according to the _Node_ _Mask_ _Length_ field value.


**4.3.2.27.2** **When** **Generated**


NWK:013B.1 When generated, this command shall contain the list of nodes matching the advertised type. Nodes
without the SIS controller role shall not send this command.

This command is generated as part of the Automatic Controller Update process. Refer to Section
4.5.9.1 Automatic Controller Update.


**4.3.2.27.3** **Effect** **on** **Receipt**


NWK:013C.1 On receipt of this command, a receiving controller node shall return a Nodes Exist Reply Command
with the Node Mask Type field set to the value received in this command.

If this command is received as part of an Automatic Controller Update process, a receiving Inclusion
NWK:013D.1 Controller shall remove non-existing nodes from its network topology.

NWK:013E.1 If this command is received outside an Automatic Controller Update process, a receiving node should
not remove non/existing nodes from its network topology.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 79


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.28** **Nodes** **Exist** **Reply** **Command**


The Nodes Exist Command is used to advertise if a Node Exist Command has been understood.


**4.3.2.28.1** **Frame** **Format**


NWK:0162.1 The Node Exist Reply Command shall be formatted as illustrated in Table 4.65


Table 4.65: Nodes Exist Command Format









Node Mask Type (8 bits)

This field is used to advertise the type of nodes that the Node Mask advertises in this command.

NWK:013F.1 This field shall be set to the same value as the Nodes Exist Command Reserved field that triggered
this command to be sent.

Status (8 bits)

This field is used to advertise the status of the Nodes Exist Command execution.

NWK:0140.1 The value 0 shall indicate that the Node Mask Type field value is not known by the node or the Node
Mask data has not been used to update the node list of the current network.

NWK:0141.1 The value 1 shall indicate that the Node Mask Type field value is known by the node and the Node
Mask data has been used to update the node list of the current network.

All other values are reserved.


**4.3.2.28.2** **When** **Generated**


NWK:0142.1 This command is generated in response of the Nodes Exist Command. A sending node shall advertise
if its network node list has been updated with the _Status_ Field.


**4.3.2.28.3** **Effect** **on** **Receipt**


On receipt of this command, a controller node is notified if the Nodes Exist Command has been
understood by the sending node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 80


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.29** **Set** **NWI** **Mode** **Command**


The Set NWI Mode Command is used to instruct AL nodes in the network to repeat Inclusion Request
Explore Frames and Routed frames sent on foreign HomeIDs.


**4.3.2.29.1** **Frame** **Format**


NWK:0143.1 The Set NWI Mode Command shall be formatted as illustrated in Table 4.66.


Table 4.66: Set NWI Mode Command Format









Mode (8 bits)

The _Mode_ field is used to indicate if the NWI mode must be enabled or disabled.

NWK:0144.1 The value 0x00 shall indicate that the receiving node shall disable NWI mode and shall not repeat
Inclusion Request Explore Frames.

NWK:0145.1 The value 0x01 shall indicate that the receiving node shall enable NWI mode and shall repeat Inclusion
Request Explore Frames.

Timeout (8 bits)

The _Timeout_ field is used to indicate how long the NWI mode must be enabled.

NWK:0146.1 The _Timeout_ field shall be ignored if the _Mode_ field is set to 0x00.

NWK:0147.1 The value 0x00 shall indicate the node to use a default timeout _nwkNWIModeDefaultTimeout_ .

NWK:0148.1 Values in the range 0x01..0xFF shall indicate the number of minutes that the receiving node shall
wait before disabling NWI mode.


**4.3.2.29.2** **When** **Generated**


NWK:0149.1 This command shall be transmitted using a Normal Explore Frame. Refer to Section 4.2.3.2.


**4.3.2.29.3** **Effect** **on** **Receipt**


NWK:014A.1 On receipt of this command, AL nodes shall activate or deactivate NWI mode according to the fields
present in this command.

For details about NWI mode, refer to Section 4.5.1.3 General Routing Requirements.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 81


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.30** **Exclude** **Request** **Command**


The Exclude Request Command is used by a node looking to be excluded from its current network.


**4.3.2.30.1** **Frame** **Format**


NWK:014B.1 The Exclude Request Command shall be formatted as illustrated in Table 4.67.


Table 4.67: Exclude Request Command Format

























For fields description, refer to Section 4.3.2.1 Node Information Frame Command.


**4.3.2.30.2** **When** **Generated**


NWK:014C.1 This command shall be transmitted using a Normal Explore Frame. Refer to Section 4.2.3.2.

NWK:014D.1 This command shall be sent to the broadcast destination (NodeID 0xFF).

NWK:014E.1 The fields values set in the Exclude Request Command shall be identical to the fields set by the
sending node in its Node Information Frame Command.

The Exclude Request Command shall be sent only if send sending node is in Learn Mode Exclusion
and supports NWE. Refer to Section 4.5.5.3 Network Wide Exclusion (NWE) for details.


**4.3.2.30.3** **Effect** **on** **Receipt**


NWK:014F.1 On receipt of this command, a controller node currently trying to remove a node shall return a Assign
IDs Command with the _HomeID_ and _NodeID_ fields set to 0 to the sending node.

NWK:0150.1 Controllers nodes not trying to exclude a node shall ignore this command.

Refer to Section 4.5.5.3 Network Wide Exclusion (NWE) for details.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 82


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.31** **Assign** **Return** **Route** **Priority** **Command**


The Assign Return Route Priority Command is used to assign the priority route to a NodeID destination.


**4.3.2.31.1** **Frame** **Format**


NWK:0151.1 The Assign Return Route Priority Command shall be formatted as illustrated in Table 4.68.


Table 4.68: Assign Return Route Priority Command Format


NodeID (8 bits)

This field is used to indicate the destination NodeID for the priority route.

Route Number (8 bits)

NWK:0152.1 This field is used to indicate the Route Number that shall be used as priority route for the NodeID.

Route Numbers are set with the Assign Return Route Command.


**4.3.2.31.2** **When** **Generated**


NWK:0153.1 A node sending this command shall have issued an Assign Return Route Command with the Route
Number prior to sending this command.

NWK:0154.1 End nodes shall not send this command.


**4.3.2.31.3** **Effect** **on** **Receipt**


NWK:0155.1 On receipt of this command, an end node shall update its priority route to the route number indicated
in this command.

NWK:0156.1 This command shall be ignored if the Route Number does not match any defined route.

NWK:0157.1 Controller nodes shall ignore this command.

NWK:0158.1 End nodes receiving this command with a valid route number shall always use that route as the
first routing attempt when starting a transmission. For details about priority routes, refer to Section
4.5.1.2 Priority Routes.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 83


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.32** **Assign** **SUC** **Return** **Route** **Priority** **Command**


The Assign SUC Return Route Priority Command is used to assign the priority route to the SUC.


**4.3.2.32.1** **Frame** **Format**


NWK:0161.1 The Assign SUC Return Route Priority Command shall be formatted as illustrated in Table 4.69.


Table 4.69: Assign SUC Return Route Priority Command Format


The fields from this command are identical to the fields in the Assign Return Route Priority Command.


**4.3.2.32.2** **When** **Generated**


NWK:0159.1 A node sending this command shall have issued an Assign SUC Return Route Command with the
Route Number prior to sending this command.

NWK:015A.1 The _NodeID_ field of this command shall be set to the NodeID of the SUC.

NWK:015B.1 End nodes shall not send this command.


**4.3.2.32.3** **Effect** **on** **Receipt**


NWK:015C.1 On receipt of this command, an end node shall update its priority route to the route number indicated
in this command for the SUC.

NWK:015D.1 This command shall be ignored if the Route Number does not match any defined route for the SUC.

NWK:015E.1 Controller nodes shall ignore this command.

NWK:015F.1 End nodes receiving this command with a valid route number shall always use that route as the first
routing attempt when starting a transmission to the SUC/SIS. For details about priority routes, refer
to Section 4.5.1.2 Priority Routes


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 84


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.33** **SmartStart** **Included** **Node** **Information** **Command**


The SmartStart Included Node Info Frame command is used by nodes to notify a controller that it
was just powered up and is already part of a network.


**4.3.2.33.1** **Frame** **Format**


NWK:0160.1 The SmartStart Included Node Information Frame Command shall be formatted as illustrated in
Table 4.70.


Table 4.70: SmartStart Included Node Information Command Format









NWI HomeID (4 bytes)

NWK:0163.1 The _NWI_ _HomeID_ field is used to uniquely identify the sending node. This field shall be constructed
from the S2 DSK of the node as follow:



NWK:0164.1


NWK:0165.1


NWK:0166.1




 - NWI HomeID 1..4 shall match byte 9..12 of the S2 DSK.

Additionally:

 - Bits 7 and 6 of the NWI HomeID 1 shall be set to 1.

 - Bit 0 of the NWI HomeID 4 byte shall be set to 0.

This is illustrated in Figure 4.11.


S2 Authenticated Learn Mode ECDH Public Key (32 bytes)

|Bytes 1..16|Bytes 17..32|Col3|
|---|---|---|
|S2 DSK (16 bytes)|S2 DSK (16 bytes)|S2 DSK (16 bytes)|
|Bytes 1..8|Bytes 9..12|Bytes 13..16|



NWI HomeID (4 bytes)






|NWI HomeID 1|Col2|NWI HomeID 2|NWI HomeID 3|NWI HomeID 4|Col6|
|---|---|---|---|---|---|
|1|1|1|1|1|0|



Figure 4.11: SmartStart NWI HomeID construction


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 85


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.33.2** **When** **Generated**


NWK:0167.1 When generated, this command shall be transmitted using a Inclusion Request Explore Frame. Refer
to Section 4.2.3.3.

NWK:0168.1 This command shall be sent to the broadcast destination (NodeID 0xFF).


**4.3.2.33.3** **Effect** **on** **Receipt**


On receipt of this command, a controller node trying to perform a SmartStart inclusion of a node
whose S2 DSK matches the NWI HomeID field of this command should indicate to the application
layer that the node to be included is currently included in another network and needs to be removed
from the foreign network before it can be included.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 86


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.34** **SmartStart** **Prime** **Command**


The Smart Prime command is used to notify SmartStart including controllers that a node is about to
make an inclusion request.


**4.3.2.34.1** **Frame** **Format**


NWK:0169.1 The SmartStart Prime Command shall be formatted as illustrated in Table 4.71.


Table 4.71: SmartStart Prime Command Format

























NWK:016A.1 All fields configuration shall be identical to the Node Information Frame Command described in
Section 4.3.2.1.


**4.3.2.34.2** **When** **Generated**


NWK:016B.1 When generated, this command shall be transmitted using a Inclusion Request Explore Frame. Refer
to Section 4.2.3.3.

NWK:016C.1 This command shall be sent to the broadcast destination (NodeID 0xFF).

This command shall be sent on the _NWI_ _HomeID_ HomeID and shall not be sent on the currently
assigned HomeID. Refer to Section 4.3.2.33.1 NWI HomeID (4 bytes) for details.

NWK:016D.1 The sending node shall subsequently send a SmartStart Inclusion Request Command after _nwkSmart-_
_StartInclusionRequestDuration_ seconds.

NWK:016E.1 Nodes not operating in AL mode may return to sleep between issuing the SmartStart Prime Command
and the SmartStart Inclusion Request Command.


**4.3.2.34.3** **Effect** **on** **Receipt**


On receipt of this command, a controller node that intends to include any node using SmartStart
shall verify if the Network HomeID of the Inclusion Request Explore Frame. header matches the NWI
HomeID of any of the DSKs present in its SmartStart list.

NWK:016F.1 If it finds a match, the controller node shall enter SmartStart Inclusion and attempt to include the
node when it issues a SmartStart Inclusion Request Command.

NWK:0170.1 In the unlikely event of several DSK matches for the received NWI HomeID, the controller node shall
enter SmartStart Inclusion alternating between the possible DSK candidates.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 87


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.3.2.35** **SmartStart** **Inclusion** **Request** **Command**


The SmartStart Inclusion Request Command is used to request to initiate a SmartStart inclusion.


**4.3.2.35.1** **Frame** **Format**


NWK:0171.1 The SmartStart Inclusion Request Command shall be formatted as illustrated in Table 4.72.


Table 4.72: SmartStart Inclusion Request Command Format

























NWK:0172.1 All fields configuration shall be identical to the Node Information Frame Command described in
Section 4.3.2.1.


**4.3.2.35.2** **When** **Generated**


NWK:0173.1 When generated, this command shall be transmitted using a Inclusion Request Explore Frame. Refer
to Section 4.2.3.3.

NWK:0174.1 This command shall be sent to the broadcast destination (NodeID 0xFF). This command shall be
sent on the _NWI_ _HomeID_ HomeID and shall not be sent on the currently assigned HomeID. Refer to
Section 4.3.2.33.1 NWI HomeID (4 bytes) for details.

NWK:0175.1 The sending node shall listen and accept Assign IDs Command using the Auth HomeID. More details
are provided in Figure 4.12 and Section 4.5.4.3 SmartStart Inclusion.


**4.3.2.35.3** **Effect** **on** **Receipt**


On receipt of this command, a controller node that intends to include the sending node shall return
an Assign IDs Command using the SmartStart Auth HomeID.

NWK:0176.1 The Auth HomeID is used to confirm the sending node that the sending controller possesses its S2
DSK. This field shall be constructed from the S2 DSK of the node as follow:

    - NWI HomeID 1..4 shall match byte 13..16 of the S2 DSK.

    - Bits 7 and 6 of the Auth HomeID 1 shall be set to 1.

    - Bit 0 of the Auth HomeID 4 byte shall be set to 0.

The Auth HomeID derivation is illustrated in Figure 4.12. Refer to Section 4.5.4.3 SmartStart Inclusion for more details.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 88


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


S2 Authenticated Learn Mode ECDH Public Key (32 bytes)






|Auth HomeID 1|Col2|Auth HomeID 2|Auth HomeID 3|Auth HomeID 4|Col6|
|---|---|---|---|---|---|
|1|1|1|1|1|0|



Figure 4.12: SmartStart Authentication HomeID Construction


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 89


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 4.4 Constants


NWK:0177.1 The constants that define the Z-Wave NWK layer are presented in Table 4.73. Implementations shall
comply with these values.


Table 4.73: NWK Layer Constants

























NWK:0178.1 The attributes defined by the Z-Wave NWK layer are presented in Table 4.74. Implementations shall
comply with the indicated ranges.


Table 4.74: NWK Layer Attributes















© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 90


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 4.5 Functional Description


NWK:0200.1 Z-Wave NWK commands in frame flows contained in this section shall use the No Operation Command
Class and the Z-Wave Protocol Command Class. (refer to Section 4.3.1 and Section 4.3.2).


**4.5.1** **Routing**


This section details how routing takes places in the network.


**4.5.1.1** **Assigning** **Return** **Routes**


NWK:0179.1 A controller node shall assign return routes to end nodes, to provide them with reliable routes for
reaching destinations in the network. This is done using the Assign Return Route Command (and
Assign SUC Return Route Command for the SUC NodeID).

NWK:017A.1 The application layer shall be able to instruct the NWK layer to assign return routes for nodes.

NWK:017B.1 A controller should assign up to 4 return routes to a destination if possible.

NWK:017C.1 End nodes without return route assigned to a destination should try direct range transmission. If
direct range transmission fails, they should issue their command using a Normal Explore Frame or may
request a static route to the SUC. Refer to Section 4.5.9.5 End Node Route Request. Controller nodes
should ignore return routes and calculate their own route using the network topology information.


**4.5.1.2** **Priority** **Routes**


If a Priority Route has been set for a NodeID destination (i.e. an Assign Return Route Priority
NWK:017D.1 Command or Assign SUC Return Route Priority Command has been received), an end node shall try
to use this route for the first transmit attempt.

NWK:017E.1 Controller nodes may ignore priority routes and use the route of their choice for the first transmission
attempt.

NWK:017F.1 An end node with a priority route set for a destination may try to use alternative routes only if at
least one transmission using the priority route was unsuccessful.


**4.5.1.3** **General** **Routing** **Requirements**


NWK:0180.1 A node sending or repeating a routing frame should not request a MPDU Acknowledgement (ACK
Req subfield set to 0 in the MPDU Frame Control). The sending node should instead listen for the
next repeater repeat frame and use this as a silent acknowledgement.



NWK:0181.1



When routing to a FL node destination, the penultimate repeater will not be able to make use of
the silent acknowledgement functionality when the last repeater must send a Wake Up beam prior
to repeating the routed frame to the destination NodeID. Therefore, the last repeater shall return an
ACK MPDU to the penultimate repeater even if Ack Req was set to 0 in the MPDU Frame Control.



NWK:0182.1 The repeater 0 node shall request an ACK MPDU to the destination NodeID when it repeats a Routed
NPDU with the Direction field set to 1 (Routed Error or Routed Acknowledgement frame).

NWK:0183.1 A node receiving a Routed Frame shall return a Routed Acknowledgement using the same route as in
the received Routed Frame.

NWK:0184.1 Nodes shall issue a minimum of _nwkMinTransmitAttemptsBeforeExploreFrame_ Routed Frames or direct range frames to a destination before issuing a Normal Explore Frame to find a new route.

All Routed Frame transmissions attempts may use the same route. Controllers should try to calculate
new routes based on their network topology information.

In general, the following route resolution is recommended:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 91


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


    - Priority route (if any) or last working route

    - Calculated routes for controllers / Assigned return routes for end nodes

    - Explorer Frames

NWK:0185.1 Nodes may omit the Wake Up Destination information for a FL node destination in the first Routed
Frame transmission attempt to minimize beaming (in case the destination node is already awake).


**4.5.1.3.1** **AL** **Nodes**


**4.5.1.3.2** **Repeating** **Frames**


In normal operation:

NWK:0186.1 AL nodes shall repeat Routed NPDUs sent on their HomeID, if their NodeID is in the repeater list.

NWK:0187.1 AL nodes shall repeat all new Normal Explore Frames sent on their HomeID.

NWK:0188.1 AL nodes shall repeat all Search Result Explore Frames sent on their HomeID, if their NodeID is in
the repeater list.

NWI mode:

NWK:0189.1 If NWI mode is enabled, AL nodes shall repeat Routed Frames sent on a foreign HomeID, if their
NodeID is in the repeater list.

NWK:018A.1 If NWI mode is enabled, AL nodes shall repeat Inclusion Request Explore Frames when:

    - The Network HomeID set to 0x00000000

    - The Network HomeID set to the repeating’s node HomeID.

NWK:018B.1 AL nodes shall not repeat Inclusion Request Explore Frames if:

    - NWI mode is disabled

    - The Network HomeID is set to a foreign HomeID (and different than 0x00000000)


**4.5.1.3.3** **FL** **and** **NL** **Nodes**


NWK:018C.1 FL and NL nodes shall not repeat Routed and Explore NDPUs.


**4.5.1.4** **Successfully** **Delivered** **Routed** **Frame**


This section specifies the procedure for routing a message across multiple hops to a destination.


**4.5.1.4.1** **Channel** **Configuration** **1,2**


Figure 4.13 depicts an example of a routed frame with 2 repeaters to a destination NodeID using
Channel Configuration 1,2.

NWK:018D.1 The repeater list presented as Repeater = [2, 3] shall indicate that the _Repeater_ _0_ field is set to 2 and
the _Repeater_ _1_ field is set to 3.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 92


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.13: Routed Frame to an AL Node (Channel Configuration 1,2)


**4.5.1.4.2** **Channel** **Configuration** **3**


NWK:018E.1 A node using Channel Configuration 3 shall set the Destination Wake Up field to 0 when transmitting
to an AL node. An example is depicted in Figure 4.14.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 93


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.14: Routed Frame to an AL Node (Channel Configuration 3)


**4.5.1.5** **Routed** **Singlecast** **to** **an** **FL** **Node** **Destination**


NWK:018F.1 In the case of a FL node destination, the last repeater shall use the Destination Wake Up extension
or field to wake up the destination with a Wake Up beam prior to repeating the routed message.

This process is illustrated in subsections Section 4.5.1.5.1 and Section 4.5.1.5.2.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 94


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.1.5.1** **Channel** **Configuration** **1,2**


Figure 4.15: Routed Frame to an FL Node (Channel Configuration 1,2)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 95


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.1.5.2** **Channel** **Configuration** **3**


Figure 4.16: Routed Frame to an FL Node (Channel Configuration 3)


**4.5.1.6** **Unsuccessful** **Routed** **Frame** **with** **Routed** **Error** **Frame**


Figure 4.17 depicts the failed delivery of a routed frame. Retransmissions triggered by the MAC layer
are not shown.

NWK:0190.1 A repeater node failing to transmit to the next hop shall return a Routed Error frame. The repeater
node sending the Routed Error Frame shall set the Source NodeID of the frame as the value of the
Destination NodeID of the Routed Frame which delivery failed.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 96


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.17: Unsuccessful Routed Frame Delivery


**4.5.1.7** **Unsuccessful** **Routed** **Frame** **Without** **Routed** **Error** **Frame**


In the unlikely event that a Routed Acknowledgment frame or Routed Error frame is not returned
NWK:0191.1 to the sending node, the sending node shall timeout after a duration of their choice denoted _aN-_
_wkRoutedAckTimeout_ .

Figure 4.18 depicts the failed delivery of a routed frame with a failure to transmit the Routed Error
Frame. Retransmissions triggered by the MAC layer are not shown.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 97


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.18: Routing        - Timeout Waiting for Routed Ack/Error Frame


**4.5.1.8** **Normal** **and** **Search** **Result** **Explore** **frames**


Figure 4.19 depicts how a Normal Explore frame reaches its destination. It illustrates how NodeID 1
is looking for a route to NodeID 9. Figure 4.20 depicts the route result.



Source NodeID

Destination NodeID

All Nodes

Other Nodes





A: Explore Normal (Src Routed=0, Direction=0, Stop=0, TTL=4, Rep Count= 0, Repeaters=[0,0,0,0])


B: Explore Normal (Src Routed=0, Direction=0, Stop=0, TTL=3, Rep Count= 1, Repeaters=[4,0,0,0])


C: Explore Normal (Src Routed=0, Direction=0, Stop=0, TTL=2, Rep Count= 2, Repeaters=[4,8,0,0])


D: Explore Normal (Src Routed=0, Direction=0, Stop=0, TTL=1, Rep Count= 3, Repeaters=[4,8,5,0])



























Figure 4.19: Normal Explore Frame Example


NWK:0192.1 Every AL Node part of the same HomeID shall repeat Normal Explore frames the first time they
receive it. Explore Frames are identified using the following fields from the MPDU Header:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 98


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


    - Source NodeID

    - Sequence Number

NWK:0193.1 Frame A is received by NodeID 6, 4 and 10. NodeID 6, 4 and 10 shall repeat frame A. NodeID 8
receives the repeated frame for the first time from NodeID 4 (Frame B), which also gets repeated.

NWK:0194.1 When NodeID 9 receives the Normal Explore Frame, it shall return a Search Result Explore Frame,
using the same route as the first Normal Explore Frame that it received.



Source NodeID

Destination NodeID

All Nodes

Other Nodes


2



A: Explore Search Result (Src Routed=1, Direction=1, Stop=1, TTL=1, Rep Count= 3, Repeaters=[4,8,5,0],...)


B: Explore Search Result (Src Routed=1, Direction=1, Stop=1, TTL=2, Rep Count= 2, Repeaters=[4,8,5,0],...)


C: Explore Search Result (Src Routed=1, Direction=1, Stop=1, TTL=3, Rep Count= 1, Repeaters=[4,8,5,0],...)


D: Explore Search Result (Src Routed=1, Direction=1, Stop=1, TTL=4, Rep Count= 0, Repeaters=[4,8,5,0],...)


All A, B, C and D Frames contain the same search results:

NodeID=1, Frame Handle=X, TTL Result=1, Rep Count Result=3, Repeater Result=[4,8,5,0])





















Figure 4.20: Search Result Explore Frame Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 99


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.2** **Learn** **Mode**


NWK:0195.1 Z-Wave nodes shall provide functionalities that enable them to learn about the existing current network
or a new network.

Learn Mode is used for several purposes:

    - It is used for a node to accept changing network (joining or leaving).

    - It is at times used for a controller node to accept receiving updated network topology information.

NWK:0196.1 Learn mode should only be enabled when necessary and disabled again as quickly as possible. The
application layer may determine when learn mode is to be enabled/disabled.

NWK:0197.1 Nodes typically enter Learn Mode to join or leave a network. When a node enters to Learn Mode, it
may have the following intents:

    - Learn Mode Inclusion: the node is expecting a network inclusion.

    - Learn Mode Exclusion: the node is expecting a network exclusion.

    - SmartStart Learn Mode: the node operates with the SmartStart procedure for inclusion.

NWK:0198.1 When learn mode is enabled on a node, it shall accept Assign IDs Commands only if the payload
matches their intent. More details are given in the individual scenarios described in Section 4.5.3 and
Section 4.5.5.

NWK:0199.1 A Secondary Controller may also enter to Learn Mode Inclusion to receive the network topology.

NWK:019A.1 A node, that supports Classic Inclusion/Exclusion entering Learn mode, shall stay in Learn mode for
a minimum duration of _nwkLearnModeMinDuration_ .

NWK:019B.1 A node, that supports Network Wide Inclusion/Exclusion entering Learn mode, shall stay in Learn
mode for a minimum duration of _nwkLearnModeNetworkWideMinDuration_ .


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 100


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.3** **Network** **Formation**


NWK:019C.1 End nodes shall not start a new network and shall wait until they get included in a network by
a controller node. When not included in a network, end nodes shall assign themselves a HomeID
( _aNwkRandomHomeID_ ) using a random number generator.

NWK:019D.1 Controller nodes that do not belong to a network shall start a new network automatically by:

    - Assigning themselves a HomeID and NodeID. The HomeID ( _aNwkRandomHomeID_ ) shall be
generated using a random number generator.

    - Assuming the Primary Controller role

    - Deciding if they take the SUC/SIS role.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 101


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.4** **Network** **Inclusion**


Several procedures can be used for including a node into a network. They are:

    - Classic network inclusion.

    - Network wide Inclusion (NWI)

    - SmartStart Inclusion (which is also network-wide)


**4.5.4.1** **Classic** **Network** **Inclusion**


The Classic Network inclusion process will include new nodes to a network, using direct range communication only. No Routed NPDUs or Explore NPDUs are used in this case.

NWK:019E.1 The Classic Network Inclusion procedure shall be according to Figure 4.21.

NWK:019F.1 When starting a Learn Mode, a node should listen for Transfer Presentation Commands with the
Option field indicating a controller trying to include a node. Upon reception, the joining node shall
issue a Node Information Frame Command to the NodeID of the controller.

NWK:01A0.1 Alternatively, a node may ignore Transfer Presentation Commands and issue a Node Information
Frame Command to the broadcast destination NodeID.

NWK:01A1.1 The including controller shall issue the Assign IDs Command using the NodeID and HomeID used by
the joining node in its Node Information Frame Command, even if the NodeID is not a part of the
valid NodeID range.

NWK:01A2.1 The Neighbour Discovery step in Figure 4.21 shall follow the description illustrated in Figure 4.45.

NWK:01A3.1 Joining nodes may use source NodeID 0xEF (instead of 0x00) while in learn mode to support old
controller implementations.

NWK:01A4.1 Joining nodes shall consider network inclusion to be completed and learn mode to be deactivated
automatically when they return a Range Info Command to the including controller.

NWK:01A5.1 Joining nodes shall not request MPDU Acknowledgement when issuing Node Information Frame
Command, even if it is issued using Singlecast addressing.

NWK:01A6.1 Including controllers shall consider network inclusion to be completed and should deactivate add mode
automatically when:

    - they issued the SUC NodeID Command to an included controller node.

    - they assigned the SUC Return Route to an included end node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 102


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.21: Network Inclusion          - Classic Inclusion Procedure


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 103


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.4.2** **Network** **Wide** **Inclusion** **(NWI)**


Network-Wide Inclusion (NWI) allows a new node to be included across an existing Z-Wave network
without direct range connectivity between the including controller and the joining node.

This procedure leverages Routed NPDUs and Explore NDPUs during the inclusion process.

NWK:01A7.1 NWI should be used as the default learn mode to ensure compatibility with all implementations of
Z-Wave nodes.

NWK:01A8.1 When a controller node enters NWI add mode, it shall enable NWI Mode using the Set NWI Mode
Command in a Normal Explore Frame.

NWK:01A9.1 The Network Wide Inclusion procedure shall be according to Figure 4.22.

NWK:01AA.1 When a node enters NWI Learn mode, it shall issue a Node Information Frame Command encapsulated
in an Inclusion Request Explore Frame. This frame shall be sent with the MPDU Header Ack Request
subfield set to 1.

NWK:01AB.1 Including controllers in NWI add mode shall send Transfer Presentation Commands with the Option
field set to 0x05.

NWK:01AC.1 If routing is used for issuing an Assign IDs Command to the joining node, the Routed Acknowledgment
frame returned by the joining node shall use the newly assigned HomeID. However, the Routed
Acknowledgment frame shall use the same NodeIDs that were used in the Routed frame carrying the
Assign IDs Command.

This is made to ensure that the repeaters will repeat the Routed Acknowledgment frame back to the
including controller.

NWK:01AD.1 The Neighbour Discovery step in Figure 4.22 shall be according to Figure 4.45.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 104


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


~~Figure~~ ~~4.22:~~ ~~Network~~ ~~Inclusion~~ ~~-~~ ~~NWI~~
© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 105


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.4.3** **SmartStart** **Inclusion**


The Z-Wave SmartStart inclusion removes the user interactions and lets nodes join a network automatically if the including controller possesses the S2 DSK (refer to [ZWATECC]) of the node to be
included.

NWK:01AE.2 Nodes supporting to be included using SmartStart inclusion shall provide at least one of the following
methods for entering SmartStart

1. Enter SmartStart Learn Mode automatically after powering on

2. Provide a mechanism to enter SmartStart Learn Mode if already powered up.


**4.5.4.3.1** **SmartStart** **Supporting** **Nodes** **Power-Up**


NWK:01AF.2 Nodes supporting SmartStart inclusion should initiate an inclusion procedure after powering up or
alternatively it should initiate an inclusion procedure when triggered manually after power-up. This
procedure depends on the inclusion state of a node and is described in the following subsections Section
4.5.4.3.2 and Section 4.5.4.3.3.


**4.5.4.3.2** **Not** **Included** **Nodes**


NWK:01B0.1 Nodes that are not part of a network shall issue SmartStart Inclusion Requests at regular intervals.
A SmartStart Inclusion Request shall consist of a SmartStart Prime Command and a SmartStart
Inclusion Request Command.

NWK:01B1.1 It shall be according to Figure 4.23. The NWI HomeID construction is specified in Section 4.3.2.33
NWI HomeID (4 bytes).

NWK:01B2.1 Nodes entering Classic Inclusion or NWI Learn Mode shall stop issuing SmartStart inclusion requests
until they return into SmartStart Learn Mode.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 106


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.23: Network Inclusion            - SmartStart not Included Node Power On


NWK:01B3.1 The timing of the inclusion requests shall be according to Table 4.75. When a range is indicated as
duration, nodes shall use a new unique random value in that range every time.


Table 4.75: SmartStart Backoff Duration for Inclusion Requests


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 107


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.4.3.3** **Included** **Nodes**


NWK:01B4.1 A node already part of a network shall send a single SmartStart Included Node Information Command
when entering SmartStart, i. e. after power up or when triggered manually. This is illustrated in
Figure 4.24.


Figure 4.24: Network Inclusion             - SmartStart Included Node Power On


**4.5.4.3.4** **SmartStart** **Including** **Controllers**


NWK:01B5.1 A controller shall have the Primary Controller role in the network to perform a SmartStart inclusion.
Secondary Controllers (and Inclusion Controllers) shall not perform SmartStart inclusions.

NWK:01B6.1 A controller shall be given the S2 DSK of a node to perform a SmartStart inclusion. Refer to

[ZWATECC].

NWK:01B7.1 When a SmartStart including controller has received the DSK of a node for inclusion, it shall keep
NWI Mode enabled for at least _nwkMinNWIModeSmartStartDuration_ minutes if the node does not
get included. This is illustrated in Figure 4.25.


Figure 4.25: Network Inclusion              - SmartStart NWI Mode Enabling


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 108


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.4.3.5** **Successful** **SmartStart** **Inclusion**


NWK:01B8.1 A controller performing a SmartStart network inclusion shall perform S2 bootstrapping. (even if the
joining node does not show the S2 Command Class in its supported Command Class list). Refer to

[ZWATECC] for the detailed S2 bootstrapping procedure.

NWK:01B9.1 A SmartStart inclusion shall be according to Figure 4.26. Figure 4.27 depicts a SmartStart inclusion
using one repeater.

NWK:01BA.1 As for NWI, if routing is used for issuing an Assign IDs Command to the joining node, the Routed
Acknowledgment frame returned by the joining node shall use the newly assigned HomeID. However,
the Routed Acknowledgment frame shall use the same NodeIDs that were used in the Routed frame
carrying the Assign IDs Command.

This is made to ensure that the repeaters will repeat the Routed Acknowledgment frame back to the
including controller.

NWK:01BB.1 The Neighbour Discovery step in Figure 4.26 and Figure 4.27 shall be according to Figure 4.45.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 109


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.26: Successful SmartStart Inclusion (Direct Range)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 110


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


~~Figure~~ ~~4.27:~~ ~~Successful~~ ~~SmartStart~~ ~~Inclusion~~ ~~(Using~~ ~~One~~ ~~Repeater)~~
© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 111


NWK:01BC.1



Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.4.3.6** **Unsuccessful** **SmartStart** **Inclusion**


SmartStart inclusion attempts may be unsuccessful, as the S2 Bootstrapping procedure is added
to the inclusion. Any SmartStart inclusion attempt that does not complete with a successful S2
Bootstrapping shall be considered as unsuccessful.

Refer to [ZWATECC] for S2 Bootstrapping.



NWK:0201.1 If an error occurred during S2 bootstrapping (S2 bootstrapping started and aborted), the inclusion
attempt shall not be considered successful.

NWK:0202.1 If S2 bootstrapping did not start, the inclusion attempt shall not be considered successful.

NWK:0203.1 If the including controller granted fewer keys than what the joining node requested, the inclusion
attempt shall be considered successful.

In case of an unsuccessful SmartStart inclusion:



NWK:01BD.2


NWK:01BE.1




 - The joining node shall leave the network automatically and consider itself not included in any
network. The joining node shall return to SmartStart learn mode.

 - The joining node may continue with SmartStart learn mode until successful SmartStart inclusion
or re-try at least up to 2 times and give up.

 - The including controller should consider the joining node removed from the network. It may
verify if the joining node has left the network properly using the NOP Command Class.

An example is given in Figure 4.28.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 112


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.28: Unsuccessful SmartStart Inclusion Example


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 113


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.5** **Network** **Exclusion**


Several procedures can be used for excluding a node from a network. They are:

    - Classic Network Exclusion

    - Network Wide Exclusion


**4.5.5.1** **Classic** **Network** **Exclusion**


NWK:01BF.1 The Classic Network inclusion process will exclude nodes from a network, using direct range communication only. No Routed NPDU or Explore NPDUs shall be used in this case.

NWK:01C0.1 The Classic Network Exclusion procedure shall be according to Figure 4.29.

NWK:01C1.1 When starting Learn Mode, a node should listen for Transfer Presentation Commands with the Option
field indicating a controller trying to exclude a node. Upon reception, the leaving node shall issue a
Node Information Frame Command to the NodeID of the controller.

NWK:01C2.1 Alternatively, a node may ignore Transfer Presentation Commands and issue a Node Information
Frame Command to the broadcast destination NodeID.

NWK:01C3.1 Leaving nodes shall not request acknowledgement when issuing the Node Information Frame Command, even if it is issued using singlecast addressing.

NWK:01C4.1 Excluding controllers should issue a Transfer End Command, using HomeID 0x00000000 and NodeID
0x00 if they exclude a controller to increase compatibility with old implementations.

NWK:01C5.1 If the excluded node is a controller, it shall acknowledge Transfer End Commands issued to HomeID
0x00000000 and NodeID 0x00 shortly after network exclusion.

NWK:01C6.1 End nodes excluded from a network shall assume the NodeID 0x00 after exclusion and shall assume a
new random HomeID ( _aNwkRandomHomeID_ ). The new HomeID shall be generated using a random
number generator.

Controller nodes excluded from a network shall start a new network (refer to Section 4.5.3 Network
Formation).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 114


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.29: Network Exclusion: Classic Network Exclusion


**4.5.5.2** **Network** **Exclusion** **From** **a** **Foreign** **Network**


NWK:01C7.1 Controllers instructed to remove a node shall also remove nodes from foreign networks.

NWK:01C8.1 A controller that has started to remove a node using Classic Exclusion or NWE shall return an Assign
IDs Command if a Node Information Frame Command has been issued in another HomeID. The
Assign IDs Command issued by the excluding controller shall be on its own HomeID.

NWK:01C9.1 A node in Learn Mode (exclusion) shall accept Assign IDs Command issued in another HomeID.

Exclusions from foreign networks will only work in direct range. Figure 4.30 illustrates a network
exclusion in a foreign network.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 115


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.30: Network Exclusion From a Foreign HomeID


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 116


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.5.3** **Network** **Wide** **Exclusion** **(NWE)**


Network-Wide Exclusion (NWE) allows a node to be removed across an existing Z-Wave network
without direct range connectivity between the excluding controller and the leaving node.

This procedure leverages Routed NPDUs and Explore NDPUs during the exclusion process.

NWK:01CA.1 The Network Wide Exclusion procedure shall be according to Figure 4.31. All frames in Figure 4.31
shall use the same HomeID.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 117


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.31: Network Wide Exclusion: NWE


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 118


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.6** **Failing** **Nodes**


NWK:01CB.1 In a Z-Wave network, a node may be considered to be failing or non-responsive when a controller
cannot reach the node, using routing and explorer frames.


**4.5.6.1** **Remove** **a** **Failing** **Node**


**4.5.6.1.1** **AL** **and** **FL** **Nodes**


NWK:01CD.1 A Remove Failed Node procedure may be used to remove non-responsive nodes from a network.

NWK:01CE.1 Before removing a non-responsive NodeID from a network, a controller shall issue NOP commands to
the non-responsive NodeID. If the node is not responding, the controller shall proceed with removing
the NodeID and updating the network.

NWK:01CF.1 A responding node shall not be removed from the network by a controller without using Classic
Exclusion or Network Wide Exclusion.

NWK:01D0.1 Removing a failing AL or FL node shall be according to Figure 4.32.


Figure 4.32: Removing a Failed AL or FL Node from a Network


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 119


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.6.1.2** **NL** **nodes**


NWK:01D1.1 NL nodes should be considered as failing after missing more than two consecutive Wake Up Periods
(no commands were received or transmitted to the node). Refer to the Wake Up Command Class for
more details [ZWAMCC].

NWK:01D2.1 A controller may remove an NL node after any arbitrary duration without receiving any frame from
the node.

This is illustrated in Figure 4.33.


Figure 4.33: Removing a Failed NL Node from a Network


**4.5.7** **Controller** **Roles**


Controllers can change roles in a network using several procedures. The following subsections describe
possible transitions and associated procedures.


**4.5.7.1** **Role** **transitions**


Controllers starting a network are the Primary Controllers for their network. (refer to Section 4.5.3
Network Formation)

NWK:01D3.1 A controller being included in a network shall assume the Secondary Controller role by default.

A Secondary Controller receiving a Transfer New Primary Controller Complete Command while it is
NWK:01D4.1 in Learn Mode shall assume the Primary Controller role. (refer to Section 4.5.7.2 Primary Controller
Shift)


NWK:01D5.1


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 120


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


A Secondary Controller receiving a SUC Node ID Command with the _SUC_ _Capabilities_ field bit 0 set
to 1 shall assume the Inclusion Controller role.

NWK:01D6.1 A controller node receiving a Set SUC Command from the Primary Controller (and accepting it) shall
assume the SUC/SIS role.


**4.5.7.2** **Primary** **Controller** **Shift**


NWK:01D7.1 Primary controllers may give the Primary Controller role to a Secondary Controller. This procedure
may be done as part of an inclusion, or with a node that is already part of the network. The procedure
shall be according to Figure 4.34.

NWK:01D8.1 All controller nodes shall accept to become Primary Controller.


Figure 4.34: Primary Controller                - Primary Controller Shift


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 121


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.7.3** **Give** **the** **SUC/SIS** **Role**


NWK:01D9.1 Primary Controllers may give the SUC role to another controller by issuing a Set SUC Command.
The NWK layer shall not perform this procedure automatically. The application layer shall be able
to instruct the NWK layer to give the SUC/SIS role to another controller.

NWK:01DA.1 Secondary Controllers and Inclusion Controller shall not give the SUC role to another controller.

NWK:01DB.1 Primary controllers shall not assign the SUC/SIS role if another node already has this role in the
network.

NWK:01DC.1 The procedure shall be according to Figure 4.35.

NWK:01DD.1 A Primary Controller shall take the Inclusion Controller role if the other controller accepted the
SUC/SIS role by returning a Set SUC ACK Command with the _State_ and _SUC_ _Capabilities_ fields set
to 0x01.

NWK:01DE.1 Controllers with SUC/SIS capabilities that start a network (first node in the network) should assign
themselves the SUC/SIS role (silently, without sending commands).

Controllers with SUC/SIS capabilities included in a network that are handed over the Primary Controller role and assigning themselves the SUC/SIS role should issue a SUC Node ID Command to all
controllers present in the network.


Figure 4.35: Primary controllers           - Give the SUC/SIS Role to Another Controller


NWK:01DF.1 Controller with no SUC capabilities shall decline the SUC/SIS role in the network. This is illustrated
in Figure 4.36


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 122


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.36: Primary Controllers        - Give the SUC/SIS Role to Another Controller Declined


NWK:01E0.1 Controllers with no SIS capabilities should decline the SUC role. However, in the event where a
controller only supports the SUC capability, the primary controller shall keep the primary controller
role. This is illustrated in Figure 4.37.


Figure 4.37: Primary Controllers      - Give the SUC/SIS Role to Another Controller Partially Accepted


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 123


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.8** **Inclusion** **Controllers** **functionalities**


When a SIS is present in a network, it enables Inclusion Controllers to perform network management
operations.

A SUC with SIS capability will enable Inclusion Controller to perform network inclusions and exclusions on its behalf.

Inclusion Controllers network management operations are described in the sections below.


**4.5.8.1** **Add** **New** **Nodes** **on** **behalf** **of** **the** **SIS**


NWK:01E1.1 Inclusion controller may add new nodes to a network on behalf of the SIS.

NWK:01E2.1 An Inclusion Controller shall make an Automatic Controller Update request to the SIS prior to
attempting a network inclusion.

NWK:01E3.1 An Inclusion Controller shall request a reserved NodeID, to use for the network inclusion, to the SIS
controller prior to attempting a network inclusion.

NWK:01E4.1 An Inclusion Controller shall issue a New Node Registered Command and a New Range Registered
Command to the SIS after a successful network inclusion.

NWK:01E5.1 A network inclusion by an Inclusion Controller shall be according to Figure 4.38.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 124


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.38: Inclusion Controllers               - Add on behalf of the SIS


**4.5.8.2** **Remove** **Nodes** **on** **behalf** **of** **the** **SIS**


NWK:01E6.1 Inclusion controller may remove nodes from a network on behalf of the SIS.

NWK:01E7.1 An inclusion controller shall issue a New Node Registered Command to the SIS after a successful
network exclusion of a node that belongs to the same network.

NWK:01E8.1 An inclusion controller shall not issue a New Node Registered Command if excluding a node from a
foreign network.

NWK:01E9.1 A network exclusion by an Inclusion Controller shall be according to Figure 4.39.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 125


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.39: Network Exclusion by an Inclusion Controller


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 126


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.9** **Network** **Maintenance**


**4.5.9.1** **Automatic** **Controller** **Update**


NWK:01EA.1 In a Z-Wave network, the SUC shall store the network topology and it shall keep it updated when
new nodes are added/removed.

NWK:01CC.1 The SUC shall deliver the network topology to any nodes that request a network topology update.

A non-SUC controller’s network topology is dated from last time a node was included or it requested a
NWK:01EB.1 network update from the SUC. To get updated, the Inclusion Controller may request updated network
topology using the Automatic Controller Update process.

NWK:01EC.1 The SUC shall provide the network topology information to controllers when requested. The SUC
controller may provide this information in two ways:

1. It may transfer all available network topology information.

2. It may transfer the list of changes since the last time the specific controller requested the network
topology.

NWK:01ED.1 During Automatic Controller Updates, the requesting controller shall not erase network topology, but
instead it shall update the topology using the data provided by the SUC.

NWK:01EE.1 An Inclusion Controller shall send an Automatic Controller Update Start Command to the SUC to
start an Automatic Controller Update procedure. The SUC shall send the topology information to
the controller using New Node Registered Commands, New Range Registered Commands. A Nodes
Exist Command shall be sent if performing a full update.

NWK:01EF.1 The Automatic Controller Update procedure shall be according to Figure 4.40 or Figure 4.41.

NWK:01F0.1 The application layer shall be able to instruct the NWK layer to trigger an Automatic Controller
Update.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 127


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.40: Automatic Controller Update (Full Update)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 128


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.41: Automatic Controller Update (Partial Update)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 129


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**4.5.9.2** **SUC** **updates** **by** **the** **Primary** **Controller**


NWK:01F1.1 In a network where the SUC is not the Primary Controller, Primary Controllers shall update the SUC
with the updated network topology after including or excluding a node.

NWK:01F2.1 A Primary Controller shall issue a New Node Registered Command and a New Range Registered
Command to the SUC after a successful network inclusion.

The network inclusion update shall be according to Figure 4.42.


Figure 4.42: Primary Controller Includes a Node and Notifies the SUC


NWK:01F3.1 A Primary Controller shall issue a New Node Registered Command to the SUC after a successful
network exclusion of a node that belongs to the same network.

NWK:01F4.1 A Primary Controller shall not issue a New Node Registered Command if excluding a node from a
foreign network.

NWK:01F5.1 The network exclusion update shall be according to Figure 4.43.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 130


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.43: Primary Controller Excludes a Node and Notifies the SUC


**4.5.9.3** **Controller** **Replication**


A Controller Replication is a procedure that can be initiated by a Primary Controller and intents to:

    - Optionally include a new controller into the network

    - Transfer the network topology to another controller.

NWK:01F6.1 The controller receiving the Controller Replication shall be in Learn Mode to accept initiating the
procedure.

NWK:01F7.1 The Controller Replication procedure shall be as illustrated in Figure 4.44.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 131


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.44: Network Maintenance                - Controller Replication


**4.5.9.4** **Neighbour** **Discovery** **/** **Range** **Test**


This procedure is used to request a node to perform a discovery of its direct range neighbours.

NWK:01F8.1 A SIS/SUC or Inclusion Controller shall perform a Neighbour Discovery as part of the network inclusion (refer to Section 4.5.3).

NWK:01F9.1 A Primary or SUC/SIS controller may perform a Neighbour Discovery periodically to keep the network
topology accurate.

NWK:01FA.1 The Neighbour Discovery procedure shall be as illustrated in Figure 4.45 or Figure 4.46.

NWK:01FB.1 250ms FL nodes and 1000ms FL nodes may be included in the same Find Nodes In Range Command
if the _Wake_ _Up_ Time field is set to 0x01 (1000ms). (250ms FL nodes will wake up with a 1000ms
beam). This is shown in Figure 4.46.

NWK:020C.1 FL nodes may be asked to find other FL nodes in the neighbor discovery process, but it is not required
as FL nodes are not acting as repeaters.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 132


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.45: Network Maintenance   - Neighbour Discovery (FL Nodes in Separate Bitmasks)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 133


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.46: Network Maintenance        - Neighbour discovery (FL Nodes in the Same Bitmask)


**4.5.9.5** **End** **Node** **Route** **Request**


NWK:01FC.1 End nodes should not try to calculate routes automatically, as they do not have a full network topology
available.

NWK:01FD.1 End nodes may request network update information to the SUC using the Static Route Request
Command.

End nodes learn about the identity of the SUC node when they receive an Assign SUC Return Route
Command or Assign SUC Return Route Priority Command.

NWK:01FE.1 The process of end node route request shall follow the procedure illustrated in Figure 4.47. The
SUC Controller should assign _nwkRecommendedNumberOfReturnRoutes_ return routes for each NodeID
destination.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 134


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.47: Network Maintenance        - End Node Route Request Process


If the SUC is busy carrying another network operation, it may return a Transfer End Command with
the Status field set 0x04. This is illustrated in Figure 4.48.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 135


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 4.48: Network Maintenance       - Static Route Request with SUC Busy


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 136


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 5 Z-WAVE LONG RANGE PROTOCOL OVERVIEW 5.1 The Z-Wave Long Range Protocol Stack Architecture


The Z-Wave Long Range protocol stack is similar to the Z-Wave protocol stack. This is illustrated in
Figure 5.1.



Network Management (i.e., node inclusion/exclusion)













|MLDE-SAP MLME-SAP|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|Medium Access Control (MAC) Layer<br>Domain Identification<br>Collision Avoidance<br>Frame<br>Validation<br>Acknowledged Frame<br>Delivery<br>Frame Retransmission|
||PLDE-SAP||PLME-SAP||
|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|Physical (PHY) Layer<br>900Mhz Radio Transceiver<br>Frequency Selection<br>Clear Channel Assessment<br>Link Budget Assessment|


Z-Wave Alliance
Layer Interface Layer Function
Defined


Figure 5.1: Z-Wave Long Range Protocol Stack Architecture


Each layer has two main interfaces to facilitate the communication with upper layers through an SAP.
The interfaces are described as a data entity and management entity that provide a data transmission
service and all other services, respectively.

[ZWALRPHY] defines the physical layer and [ZWALRMAC] defines the medium access control layer.

On the foundation of those two lower layers, the Z-Wave alliance defines the Network layer (NWK)
and application layers.

The Z-Wave Long Range NWK layer is responsible for network formation (i.e., inclusion/exclusion of
nodes to/from a network). The Z-Wave Long Range NWK layer manages the network establishment
using command frames known as the Z-Wave Long Range Command Class (defined in Section 6.3).
These NWK commands are designed for network formation specific purposes.

The Z-Wave application layer is responsible for building applications using dedicated Command
Classes, (defined in [ZWAACC], [ZWAMCC], [ZWATECC], [ZWANPCC]).In order to be certifiable,
applications shall comply with Z-Wave device types defined in [ZWADT] and [ZWADTV2]. Finally,
the applications layer is also responsible for providing some network management functionalities using
the NWK interface (for details, refer to [ZWART]).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 137


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 5.2 Z-Wave Long Range Network Layer Reference Model


The Z-Wave Long Range NWK layer provides an interface between the application layer and the
MAC layer. The Z-Wave Long Range NWK layer relies on services provided by the MAC layer
and offers services to higher layers though the Network Layer Data Entity (NLDE) and Network
Layer Management Entity (NLME) service point interfaces. Figure 3.2 illustrates the components
and interface of the Z-Wave Long Range NWK layer.

LR-NWK:0001.1 The Z-Wave Long Range NWK layer shall provide two services to the Application layer that are
accessed through two SAPs:

     - The data service, accessed through NLDE-SAP, and

     - The network management service accessed through the NLME-SAP.

The detailed description of the Z-Wave Long Range NWK functional model is presented in Section 6.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 138


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 5.3 Z-Wave Long Range Definitions


**5.3.1** **Z-Wave** **Long** **Range** **Network** **Principles**


The following is a summary of the network principles established by [ZWALRPHY], [ZWALRMAC]:

1. Groups of nodes are divided into domains:

      - The division of physical nodes into domains is logical. Domains may fully or partially
overlap each other’s radio frequency ranges.

      - The Z-Wave Network Layer supports up to 2 [32] domains.

      - Each domain is identified by a unique HomeID.

2. The domain is a set of nodes connected to the same medium:

      - Each domain may contain up to _4000_ nodes.

      - Each node in the domain is identified by a NodeID that is unique within the actual domain.

      - Nodes of the same domain can only communicate with the controller using direct range
transmissions.


**5.3.2** **Controller** **and** **End** **Nodes**


Refer to Section 3.3.4 Z-Wave controller roles.


**5.3.3** **Network** **Topology**


Refer to Section 3.3.3 Network topology.

Nodes added to a network using Z-Wave Long Range will only have one known neighbour, which is
the Primary Controller.


**5.3.4** **Z-Wave** **Controller** **Roles**


Refer to Section 3.3.4 Z-Wave controller roles.

LR-NWK:0002.1 A controller starting a Z-Wave Long Range network shall assume the Primary controller role.

The SUC/SIS functionalities will not be used in a Z-Wave Long Range network and included controllers
will be Secondary Controllers.


**5.3.5** **Node** **Operation** **Modes**


Refer to Section 3.3.5 Node operation modes for nodes supporting with Z-Wave and Z-Wave Long
range protocols.


**5.3.5.1** **Wake** **On** **Event** **End** **Node** **(WOEEN)**


A WOEEN has the same behavior as a NL node except without periodic wake ups.

Reporting of a WOEEN cannot be configured via the Wake Up Command Class and is dependent on
external events.

LR-NWK:009A.1 WOEENs should use an external power source in configuration mode.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 139


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**5.3.6** **Network** **Addressing**


Z-Wave Long Range supports the following type of addressing:

     - Singlecast

     - Broadcast

The type of addressing and its frame format are defined in the MPDU Header (refer to [ZWALRMAC]).

LR-NWK:0003.1 In this specification, some commands shall not be sent using broadcast addressing (0xFFF) and shall
be ignored if received via broadcast addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 140


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 6 Z-WAVE LONG RANGE NETWORK LAYER SPECIFICATION 6.1 General Description


The Network Layer provides transmission services for higher layers using services provided by the
MAC layer. The Z-Wave Long Range NWK layer services only include network formation.


**6.1.1** **Z-Wave** **Long** **Range** **NWK** **Layer** **Overview**


The network layer is required to provide functionality to ensure correct operation of the MAC sub-layer
and provide a suitable service interface to the application layer. To interface with the application layer,
the network layer conceptually includes two service entities that provide the necessary functionalities.
These service entities are the data service and the management service. The Z-Wave Long Range NWK
layer data entity (NLDE) provides the data transmission service via its associated SAP (NLDE-SAP),
and the Z-Wave Long Range NWK layer management entity (NLME) provides the management service
via its associated SAP (NLME-SAP). The NLME utilizes the NLDE to achieve some of network
management tasks. Also, the NLME maintains a database known as the Network Information Base
(NIB) that contains information regarding the network topology.


**6.1.2** **Network** **Layer** **Data** **Entity** **(NLDE)**


LR-NWK:0004.1 The NLDE shall provide a data service for the application layer to transport Data Link Protocol Data
Unit (DLPDU) to a destination located in the same network. The DLPDU format is shown in Figure
4.1.

LR-NWK:0005.1 The NLDE shall provide the following services:

LR-NWK:0006.1 - Generation of NPDUs (Network Protocol Data Unit): The NLDE shall be capable to generate
appropriate NPDUs from application data.


**6.1.2.1** **Network** **Layer** **Management** **Entity** **(NLME)**


LR-NWK:0007.1 The NLME shall provide a management service to leverage the network’s routing capabilities. The

LR-NWK:0008.1 NLME shall provide the following services:

     - Network Inclusion: This is the ability to join or create a network.

     - Network Exclusion: This is the ability to leave a network.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 141


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 6.2 Frame Format


The Z-Wave Long Range Network layer does not provide any functionality other than network management.


**6.2.1** **NPDU** **formats**


LR-NWK:0009.1 When using a Z-Wave Long Range PHY/MAC, the Z-Wave Long Range NWK layer shall add a
DLPDU payload, either containing a Z Wave Long Range NWK command or a command received
from the application layer.

This is illustrated in Figure 6.1.



Figure 6.1: General Z-Wave Long Range NPDU Format





© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 142


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 6.3 Command Frames


The commands defined by the Z Wave Long Range NWK layer are categorized in Command Classes.
These Command Classes are listed in Table 6.1.


Table 6.1: Z-Wave Long Range NWK Layer Command Classes











The following sections illustrates how the Network Layer Management (NLME) shall build the individual commands for transmission.

LR-NWK:000A.1 During the transmission of each of these commands, the NLME shall construct the network layer
protocol data (NPDU) part of the frame as illustrated in Figure 6.2.









Figure 6.2: The Z-Wave Long Range Network Layer Command Frame Format


LR-NWK:000B.1 Z-Wave Long Range NWK Commands shall not use any segmentation or encryption. No application
payload shall be added from upper layers when using NWK Commands. This is illustrated in Figure
4.8.

LR-NWK:000C.1 Command Classes in the range 0x00..0x1F shall be considered as NWK Commands.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 143


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1** **Z-Wave** **Long** **Range** **Command** **Class**


This Command Class is used for including and excluding nodes in a Z-Wave Long Range network.

LR-NWK:000D.1 The Z-Wave Long Range Command Class shall be supported by all nodes operating with Z-Wave
Long Range.

The Command frames defined by this Command Class are listed in Table 6.2.


Table 6.2: Z-Wave Long Range Network Formation Command
Class Commands













LR-NWK:000E.1 All commands in this command class shall be supported by a node operating on a Z-Wave Long Range
network.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 144


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.1** **No** **Operation** **Command**


The No Operation Command is used to test the availability of a node in a network.

LR-NWK:000F.1 This Command may be used to verifying if an excluded node is still part of the network. This
Command may also be used on application level e.g. checking if a node is still operational.


**6.3.1.1.1** **Frame** **Format**


The No Operation Command shall be formatted as illustrated in Table 6.3.


Table 6.3: Z-Wave Long Range No Operation Command Format


**6.3.1.1.2** **When** **Generated**


LR-NWK:0010.1 This command shall be sent using singlecast addressing and shall not be sent using broadcast addressing.

LR-NWK:0011.1 The application layer shall be able to instruct the NWK layer to issue a No Operation Command to
a node.


**6.3.1.1.3** **Effect** **on** **Receipt**


LR-NWK:0012.1 On receipt of this command, a receiving node shall not do anything. The sending node will be notified
that the receiving node is operational by receiving a MAC layer acknowledgment.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 145


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.2** **Node** **Information** **Frame** **Command**


The Node Information Frame command is used to advertise the capabilities of the sending node.


**6.3.1.2.1** **Frame** **Format**


LR-NWK:0013.1 The Node Information Frame Command shall be formatted as illustrated in Table 6.4.


Table 6.4: Node Information Frame Command Format



















LR-NWK:0014.1 All fields not described below shall be identical to the Node Information Frame Command described
in Section 4.3.2.1.

Supported Speed (3 bits)

LR-NWK 0088.1 The _Supported_ _Speed_ field indicates the transmission data rate supported by the sending node. This
field shall be treated as a bitmask and shall have at least one speed bits set as depicted in Table 6.5.


Table 6.5: Speed Supported by the Node


Command Class List Length (8 bits)

This field is used to advertise the length in bytes of the _Command_ _Class_ field.

Command class (N bytes)

This field is used to advertise the list of Command Classes (Refer to [ZWAACC], [ZWAMCC], [ZWATECC] and [ZWANPCC]) supported by the sending node using non-secure communication.

LR-NWK:0015.1 The length of this field in bytes shall be according to the Command Class List Length field value.



LR-NWK:0016.1


LR-NWK:0017.1


LR-NWK:0018.1



The field shall advertise the list of Command Classes that the node supports. Command Classes
advertised in this field shall be in the range 0x21..0xFFFF. Command Classes in the range 0x00..0x20
shall not be advertised in this field.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 146


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.2.2** **When** **Generated**


No requirement


**6.3.1.2.3** **Effect** **on** **Receipt**


On receipt of this command, a receiving node is notified of the sender’s Z-Wave Long Range capabilities
and non-secure supported Command Classes.

LR-NWK:0019.1 If the network layer does not expect to receive a Node Information Frame Command (i.e. did not
issue a Request Node Information Frame Command), the command (or its data) shall be forwarded
to the upper protocol layer (application).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 147


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.3** **Request** **Node** **Information** **Frame** **Command**


This command is used to request a node to return a Node Information Frame Command.


**6.3.1.3.1** **Frame** **Format**


LR-NWK:001A.1 The Request Node Information Frame Command shall be formatted as illustrated in Table 6.6.


Table 6.6: Z-Wave Long Range Request Node Information Frame
Command Format


**6.3.1.3.2** **When** **Generated**


LR-NWK:001B.1 This command shall be sent using singlecast addressing and shall not be sent using broadcast addressing.

LR-NWK:001C.1 The application layer shall be able to instruct the NWK layer to issue a Request Node Information
Frame Command to a node.


**6.3.1.3.3** **Effect** **on** **Receipt**


LR-NWK:001D.1 On receipt of this command, a receiving node shall return a Node Information Frame Command in

LR-NWK:001E.1 response. A receiving node shall not return a response if this command is received via broadcast
addressing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 148


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.4** **Assign** **IDs** **Command**


This command is used to assign a new NodeID and HomeID to the receiving node.


**6.3.1.4.1** **Frame** **Format**


LR-NWK:001F.1 The Assign IDs Command shall be formatted as illustrated in Table 6.7.


Table 6.7: Z-Wave Long Range Assign IDs Command Format









Reserved (4 bits)

LR-NWK:0020.1 The Reserved field shall be set to 0 by a sending node and shall be ignored by a receiving node.

NodeID (12 bits)

The _NodeID_ field is used to assign a NodeID to a node.

LR-NWK:0021.1 Values in the range 0x100..0xFA0 shall indicate the new NodeID assigned to the receiving node.

HomeID (4 bytes)

The _HomeID_ field is used to assign an HomeID to a node.

LR-NWK:0022.1 This field shall indicate the new HomeID assigned to the receiving node.


**6.3.1.4.2** **When** **Generated**


LR-NWK:0023.1 This command shall be sent using singlecast addressing and shall not be sent using broadcast addressing.


**6.3.1.4.3** **Effect** **on** **Receipt**


LR-NWK:0024.1 On receipt of this command, a receiving node shall update its HomeID and NodeID if and only if it
is currently in SmartStart Learn Mode after issuing a SmartStart Inclusion Request Command and it
is received on the Auth HomeID.

Refer to 6.5.4.1 SmartStart Inclusion for details.

LR-NWK:0025.1 A receiving node shall ignore the command if it is received via broadcast addressing.

LR-NWK:0026.1 A receiving node shall ignore this command if the NodeID field is set to 0x00.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 149


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.5** **Exclude** **Request** **Command**


The Exclude Request Command is used by a node looking to be excluded from its current network.


**6.3.1.5.1** **Frame** **Format**


LR-NWK:0027.1 The Exclude Request Command shall be formatted as illustrated in Table 6.8.


Table 6.8: Z-Wave Long Range Exclude Request Command Format


**6.3.1.5.2** **When** **Generated**


LR-NWK:0028.1 This command shall be sent to the broadcast destination (NodeID 0xFFF).

LR-NWK:0029.1 The fields values set in the Exclude Request Command shall be identical to the fields set by the
sending node in its Node Information Frame Command.

LR-NWK:002A.1 The Exclude Request Command shall be sent only if send sending node is in Learn Mode Exclusion.
Refer to Section 6.5.5 Z-Wave Long Range Network Exclusion for details.


**6.3.1.5.3** **Effect** **on** **Receipt**


LR-NWK:002B.1 On receipt of this command, a controller node that has been instructed to remove a node shall return
an Exclude Request Confirmation Command to the sending node.

LR-NWK:002C.1 Controllers nodes not trying to exclude a node shall ignore this command.

Refer to Section 6.5.5 Z-Wave Long Range Network Exclusion for details.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 150


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.6** **SmartStart** **Included** **Node** **Information** **Command**


The SmartStart Included Node Info Frame command is used by nodes to notify a controller that it
was just powered up and is already part of a network.


**6.3.1.6.1** **Frame** **Format**


LR-NWK:002D.1 The SmartStart Included Node Information Frame Command shall be formatted as illustrated in
Table 6.9.


Table 6.9: Z-Wave Long Range SmartStart Included Node Information Frame Command Format









NWI HomeID (4 bytes)

Refer to Section 4.3.2.33.1 NWI HomeID (4 bytes).


**6.3.1.6.2** **When** **Generated**


LR-NWK:002E.1 This command shall be sent to the broadcast destination (NodeID 0xFFF).


**6.3.1.6.3** **Effect** **on** **Receipt**


LR-NWK:002F.1 On receipt of this command, a controller node trying to perform a SmartStart inclusion of a node
whose S2 DSK matches the _NWI_ _HomeID_ field of this command should indicate to the application
layer that the node to be included is currently included in another network and needs to be removed
from the foreign network before it can be included.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 151


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.7** **SmartStart** **Prime** **Command**


The Smart Prime command is used to notify SmartStart including controllers that a node is about to
make an inclusion request.


**6.3.1.7.1** **Frame** **Format**


LR-NWK:0030.1 The SmartStart Prime Command shall be formatted as illustrated in Table 6.10.


Table 6.10: Z-Wave Long Range SmartStart Prime Command Format























LR-NWK:0031.1 All fields configuration shall be identical to the Node Information Frame Command described in
section Section 4.3.2.1.


**6.3.1.7.2** **When** **Generated**


LR-NWK:0032.1 This command shall be sent to the broadcast destination (NodeID 0xFFF).

LR-NWK:0033.1 This command shall be sent on the NWI HomeID HomeID and shall not be sent on the currently
assigned HomeID. Refer to Section 4.3.2.33.1 NWI HomeID (4 bytes) for details.

LR-NWK:0034.1 The sending node shall subsequently send a SmartStart Inclusion Request Command after _nwkSmart-_
_StartInclusionRequestDuration_ seconds.

LR-NWK:0035.1 Nodes not operating in AL mode may return to sleep between issuing the SmartStart Prime Command
and the SmartStart Inclusion Request Command.


**6.3.1.7.3** **Effect** **on** **Receipt**


LR-NWK:0036.1 On receipt of this command, a controller node that intends to include any node using SmartStart shall
verify if the Network HomeID of the frame header matches the NWI HomeID of any of the DSKs
present in its SmartStart list.

LR-NWK:0037.1 If it finds a match, the controller node shall enter SmartStart Inclusion and attempt to include the
node when it issues a SmartStart Inclusion Request Command.

LR-NWK:0038.1 In the unlikely event of several DSK matches for the received NWI HomeID, the controller node shall
enter SmartStart Inclusion alternating between the possible DSK candidates.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 152


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.8** **SmartStart** **Inclusion** **Request** **Command**


The SmartStart Inclusion Request Command is used to request to initiate a SmartStart inclusion.


**6.3.1.8.1** **Frame** **Format**


LR-NWK:0039.1 The SmartStart Inclusion Request Command shall be formatted as illustrated in Table 6.11.


Table 6.11: Z-Wave Long Range SmartStart Inclusion Request
Command Format























LR-NWK:003A.1 All fields configuration shall be identical to the Node Information Frame Command described in
Section 4.3.2.1.


**6.3.1.8.2** **When** **Generated**


LR-NWK:003B.1 This command shall be sent to the broadcast destination (NodeID 0xFFF). This command shall be

LR-NWK:003C.1 sent on the NWI HomeID and shall not be sent on the currently assigned HomeID. Refer to Section
4.3.2.33.1 NWI HomeID (4 bytes) for details.

LR-NWK:003D.1 The sending node shall listen to and accept Assign IDs Commands using the Auth HomeID. More
details are provided in Figure 4.12 and Section 4.5.4 SmartStart Inclusion.


**6.3.1.8.3** **Effect** **on** **Receipt**


LR-NWK:003E.1 On receipt of this command, a controller node that intends to include the sending node shall return
an Assign IDs Command using the SmartStart Auth HomeID.

For SmartStart Auth HomeID definition, refer to Section 4.3.2.35.3 Effect on Receipt


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 153


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.9** **Exclude** **Request** **Confirmation** **Command**


The Exclude Request Confirmation Command is used by a controller node to confirm to a node that
it can leave the current network.


**6.3.1.9.1** **Frame** **Format**


LR-NWK:003F.1 The Exclude Request Confirmation Command shall be formatted as illustrated in Table 6.12.


Table 6.12: Z-Wave Long Range Exclude Request Confirmation
Command Format









Requesting NodeID (12 bits)

This field is used to indicate the NodeID that has issued an Exclude Request Command for which
this command is returned.

Requesting HomeID (4 bytes)

This field is used to indicate the HomeID on which the Exclude Request Command was issued.


**6.3.1.9.2** **When** **Generated**


LR-NWK:0040.1 This command shall be sent to a node that has issued an Exclude Request Command.

LR-NWK:0041.1 The Exclude Request Confirmation Command shall be sent by a controller that has been instructed
to exclude a node from a Z-Wave Long Range network.

Refer to Section 6.5.5 Z-Wave Long Range Network Exclusion for details.


**6.3.1.9.3** **Effect** **on** **Receipt**


LR-NWK:0042.1 On receipt of this command, a node currently trying to be excluded from its network shall leave its
current network.

LR-NWK:0043.1 Nodes shall ignore this command if they are not in Learn Mode Exclusion.

Refer to Section 6.5.5 Z-Wave Long Range Network Exclusion for details.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 154


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.3.1.10** **Non** **Secure** **Inclusion** **Step** **Complete** **Command**


The Non Secure Inclusion Step Complete Command is used by a controller node to indicate to a
joining node that the non-secure part of the network inclusion is completed.


**6.3.1.10.1** **Frame** **Format**


LR-NWK:0044.1 The Non-Secure Inclusion Step Complete Command shall be formatted as illustrated in Table 6.13.


Table 6.13: Non Secure Inclusion Step Complete Command Format


**6.3.1.10.2** **When** **Generated**


LR-NWK:0045.1 A sending node shall initiate S2 Security Bootstrapping after issuing this command.

Refer to Section 6.5.4 Z-Wave Long Range Network Inclusion for details.


**6.3.1.10.3** **Effect** **on** **Receipt**


LR-NWK:0046.1 On receipt of this command, a joining node is instructed that the non-secure inclusion is completed,
and the S2 Security Bootstrapping shall now take place.

LR-NWK:0047.1 A receiving node shall start its S2 TB1 timer upon reception of this command. Refer to [ZWATECC]
for details.

Refer to Section 6.5.4 Z-Wave Long Range Network Inclusion for details.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 155


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 6.4 Constants


LR-NWK:0048.1 The constants that define the Z-Wave Long Range NWK layer are presented in Table 6.14. Implementations shall comply with these values.


Table 6.14: Z-Wave Long Range NWK Layer Constants























LR-NWK:0049.1 The attributes defined by the Z-Wave Long Range NWK layer are presented in Table 6.15. Implementations shall comply with the indicated ranges.


Table 6.15: Z-Wave Long Range NWK Layer Attributes









© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 156


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## 6.5 Functional Description


NWK commands in frame flows contained in this section shall use the Z-Wave Long Range Command
Class. (refer to Section 6.3.1)


**6.5.1** **Communication** **between** **Z-Wave** **Long** **Range** **Nodes**


LR-NWK:004A.1 All communications shall use direct range when operating on a Z-Wave Long Range PHY/MAC.

LR-NWK:004B.1 Controller nodes shall issue a minimum of _nwkMinTransmitAttempts_ direct range frames to a destination before concluding that the destination is failing.


**6.5.1.1** **Wake** **On** **Event** **End** **Node** **(WOEEN)**


LR-NWK:0089.1 In Self-Powered Mode, a WOEEN is allowed to not request an ACK from any other node to save
power by not listening for an ACK.

LR-NWK:0090.1 A controller shall not request an ACK from a WOEEN in subsequent messages if the WOEEN did
not request an ACK from the controller.

LR-NWK:0091.1 Re-tranmission of messages shall be handled by the application layer.

**LR-NWK:009** 29 **.1** A WOEEN, in self-powered mode, may intiate the security handshake on both LR channels. Further
communication shall continue on the successful channel.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 157


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.2** **Learn** **Mode**


LR-NWK:004C.1 Z-Wave Long Range nodes shall provide functionalities that enable them to learn about the existing
current network or a new network.

On a Z-Wave Long Range network, Learn Mode is used for a node to accept changing network (joining
or leaving).

LR-NWK:004D.1 Nodes typically enter Learn Mode to join or leave a network. When a node enters to Learn Mode, it
may have the following intents:

     - Learn Mode Exclusion: the node is expecting a network exclusion.

     - SmartStart Learn Mode: the node operates with the SmartStart procedure for inclusion.

LR-NWK:004E.1 Learn Mode Exclusion should only be enabled when necessary and disabled again as quickly as possible.

LR-NWK:004F.1 A node entering Learn Mode Exclusion sha**ll stay in Learn Mode Exclusion for a minimum duration
of _nwkLearnModeMinDuration_ .

LR-NWK:0050.1 The application layer may determine when Learn Mode Exclusion is to be enabled/disabled.

More details are given in the individual scenarios described in Section 6.5.4 and Section 6.5.5.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 158


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.3** **Network** **Formation**


LR-NWK:0051.1 End nodes shall not start a new network and shall wait until they get included in a network by

LR-NWK:0052.1 a controller node. When not included in a network, end nodes shall assign themselves their NWI
HomeID (refer to Section 4.3.2.33.1 NWI HomeID (4 bytes)).

LR-NWK:0053.1 Controller nodes that do not belong to a network shall start a new Z-Wave Long Range network
automatically by:

LR-NWK:0054.1 - Assigning themselves a HomeID and the NodeID 0x01. The HomeID ( _aNwkRandomHomeID_ )
shall be generated using a random number generator.

     - Assuming the Primary Controller role.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 159


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.4** **Z-Wave** **Long** **Range** **Network** **Inclusion**


Nodes join a Z-Wave Long Range network using SmartStart Inclusion


**6.5.4.1** **SmartStart** **Inclusion**


The Z-Wave SmartStart inclusion removes the user interactions and lets nodes join a network automatically if the including controller possesses the S2 DSK (refer to [ZWATECC]) of the node to be
included.

LR-NWK:0055.2 Nodes supporting to be included using SmartStart inclusion shall provide at least one of the following
methods for entering SmartStart

1. Enter SmartStart Learn Mode automatically after powering on

2. Provide a mechanism to enter SmartStart Learn Mode if already powered up.


**6.5.4.1.1** **SmartStart** **Supporting** **Nodes** **Power-Up**


LR-NWK:0056.2 Nodes supporting SmartStart inclusion should initiate an inclusion procedure after powering up or
alternatively it should initiate an inclusion procedure when triggered manually after power-up. This
procedure depends on the inclusion state of a node and is described in subsections Section 6.5.4.1.1
_Not_ _Included_ _Nodes_ and Section 6.5.4.1.1 _Included_ _Nodes_ below.

LR-NWK:0057.1 Nodes capable of operating both on Z-Wave and Z-Wave Long Range shall issue SmartStart Prime
and SmartStart Inclusion Requests both on the Z-Wave and Z-Wave Long Range channels.

Not Included Nodes

LR-NWK:0058.1 Nodes that are not part of a network shall issue SmartStart Inclusion Requests at regular intervals.

LR-NWK:0059.1 A SmartStart Inclusion Request shall consist of a SmartStart Prime Command and a SmartStart
Inclusion Request Command.

LR-NWK:005A.1 It shall be according to Figure 6.3. The NWI HomeID construction is specified in Section 4.3.2.33.1
NWI HomeID (4 bytes).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 160


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 6.3: Z-Wave Long Range Network Inclusion         - SmartStart Not Included Node Power On


LR-NWK:005B.1 The timing of the inclusion requests shall be according to Table 4.75. When a range is indicated as

LR-NWK:005C.1 duration, nodes shall use a new unique random value in that range every time.

Included Nodes

LR-NWK:005D.1 A node already part of a network shall send a single SmartStart Included Node Information Command
when entering SmartStart, i. e. after power up or when triggered manually. This is illustrated in
Figure 6.4.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 161


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 6.4: Z-Wave Long Range Network Inclusion          - SmartStart Included Node Power On


**6.5.4.1.2** **SmartStart** **Including** **Controllers**


LR-NWK:005E.1 A controller shall have the Primary Controller role in the network to perform a SmartStart inclusion.
Secondary Controllers shall not perform SmartStart inclusions.

LR-NWK:005F.1 A controller shall be given the S2 DSK of a node to perform a SmartStart inclusion. Refer to

[ZWATECC].


**6.5.4.1.3** **Successful** **SmartStart** **Inclusion**


LR-NWK:0060.1 A controller performing a SmartStart network inclusion shall perform S2 bootstrapping (even if the
joining node does not show the S2 Command Class in its supported Command Class list). Refer to

[ZWATECC] for the detailed S2 bootstrapping procedure.

LR-NWK:0061.1 A SmartStart inclusion shall be according to Figure 6.5.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 162


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 6.5: Successful Z-Wave Long Range SmartStart Inclusion


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 163


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.4.1.4** **Unsuccessful** **SmartStart** **Inclusion**


LR-NWK:0062.1 SmartStart Network inclusion attempts may be unsuccessful. Any SmartStart Network Inclusion
attempt that does not complete with a successful S2 Bootstrapping shall be considered as unsuccessful.

LR-NWK:0063.1 If an error occurred during S2 bootstrapping (S2 bootstrapping started and aborted), the inclusion
attempt shall not be considered successful.

LR-NWK:0064.1 If S2 bootstrapping did not start, the inclusion attempt shall not be considered successful.

LR-NWK:0065.1 If the including controller did not grant any key requiring authentication (Public Key Report bytes
obfuscated by zeros), the inclusion attempt shall not be considered successful.

LR-NWK:0066.1 If the including controller granted fewer keys than what the joining node requested, the inclusion
attempt shall be considered successful if at least one authenticated key was granted.

LR-NWK:0067.1 If more than _nwkNonSecureInclusionCommandTimeout_ seconds elapsed between receiving commands
part of the SmartStart inclusion prior to S2 bootstrapping, a joining node shall abort the inclusion
attempt and shall not consider the inclusion successful.

LR-NWK:0068.1 If more than _nwkNonSecureInclusionCommandTimeout_ seconds elapsed between receiving acknowledgements for commands part of the SmartStart inclusion prior to S2 bootstrapping, a controlling
node shall abort the inclusion attempt and shall not consider the inclusion successful.

Refer to [ZWATECC] for S2 Bootstrapping.

In case of an unsuccessful SmartStart Network Inclusion:



LR-NWK:0069.1


LR-NWK:006A.1


LR-NWK:006B.1


LR-NWK:006C.1


LR-NWK:006D.1


LR-NWK:006E.1


LR-NWK:006F.1




 - The joining node shall leave the network automatically and consider itself not included in any
network. The joining node shall return to SmartStart learn mode.

 - The joining node may continue with SmartStart learn mode until successful SmartStart inclusion
or re-try at least up to 2 times and give up.

 - The including controller should consider the joining node removed from the network. It may
verify if the joining node has left the network properly using the NOP Command.

An example is given in Figure 6.6. MAC layer Ack frames are omitted from Figure 6.6.

If receiving no MPDU acknowledgement, an including controller may issue up to _nwkAssignIDCon-_
_firmationRetries_ No Operation Command frames to verify that the node was included. It should not
send the Non Secure Inclusion Step Complete Command and should not initiate the S2 bootstrapping procedure if the node is non-responsive and in this case it shall consider the network inclusion
unsuccessful.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 164


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


~~Figure~~ ~~6.6:~~ ~~Unsuccessful~~ ~~Z-Wave~~ ~~Long~~ ~~Range~~ ~~SmartStart~~ ~~Inclusion~~ ~~Example~~
© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 165


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.4.1.5** **Inclusion** **of** **Wake** **On** **Event** **End** **Nodes**


LR-NWK:0093.1 All WOEENs shall follow the same inclusion process.

LR-NWK:0094.1 Inclusion should be done in configuration mode.

LR-NWK:0095.1 An external power source may be used for inclusion if needed.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 166


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.5** **Z-Wave** **Long** **Range** **Network** **Exclusion**


Nodes exit a Z-Wave Long Range network using direct range Network Exclusion.


**6.5.5.1** **Network** **Exclusion**


The Network Exclusion process will exclude nodes from a network.

LR-NWK:0070.1 The Network Exclusion procedure shall be according to Figure 6.7.

LR-NWK:0071.1 When starting Learn Mode Exclusion, a node shall issue an Exclude Request Command to the broadcast destination NodeID.

LR-NWK:0072.1 End nodes excluded from a network shall assume the NodeID 0x00 after exclusion and shall assume
their NWI HomeID as new HomeID.

LR-NWK:0073.1 Controller nodes excluded from a network shall start a new network (refer to Section 6.5.3 Network
Formation).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 167


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 6.7: Z-Wave Long Range Network Exclusion


**6.5.5.2** **Network** **Exclusion** **From** **a** **Foreign** **Network**


LR-NWK:0074.1 Controllers instructed to remove a node shall also remove nodes from foreign networks.



LR-NWK:0075.1


LR-NWK:0076.1



A controller that has started a node removal shall return an Exclude Request Confirmation Command if an Exclude Request Command has been issued in another HomeID. The Exclude Request
Confirmation Command if issued by the excluding controller shall be on its own HomeID.



LR-NWK:0077.1 A controller shall issue the Exclude Request Confirmation Command on its own HomeID. When
returning an Exclude Request Confirmation Command to a node in a foreign network, an MDPU Ack
shall not be requested.

LR-NWK:0078.1 A randomized delay in the range 0..1 second should be added by controller nodes to the _nwkLREx-_
_cludeRequestForeignNetBackOff_ time.


LR-NWK:0079.1


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 168


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


A node in Learn Mode (exclusion) shall accept Exclude Request Confirmation Command if issued in
another HomeID.

Figure 6.8 illustrates a network exclusion in a foreign network.


Figure 6.8: Z-Wave Long Range Network Exclusion From a Foreign HomeID


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 169


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.6** **Failing** **nodes**


LR-NWK:007A.1 In a Z-Wave network, a node may be considered failing or non-responsive when a controller cannot
reach the node, except for a WOEEN.


**6.5.6.1** **Remove** **a** **Failing** **Node**


**6.5.6.1.1** **AL** **and** **FL** **Nodes**


LR-NWK:007B.1 A Remove Failed Node procedure may be used to remove non-responsive nodes from a network.

LR-NWK:007C.1 Before removing a non-responsive NodeID from a network, a controller shall issue No Operation

LR-NWK:007D.1 Commands to the non-responsive NodeID. If the node is not responding, the controller shall proceed
with removing the NodeID and updating the network.

LR-NWK:007E.1 A responding node shall not be removed from the network by a controller without using Network
Exclusion.

LR-NWK:007F.1 Removing a failing AL or FL node shall be according to Figure 6.9.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 170


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


Figure 6.9: Z-Wave Long Range Removing a Failed AL or FL Node from a Network


**6.5.6.1.2** **NL** **Nodes**


LR-NWK:0080.1 The process shall be identical to Section 4.5.6.1.2 NL Nodes.


**6.5.6.1.3** **Wake** **On** **Event** **End** **Nodes**


LR-NWK:0088.1 A Wake On Event Node shall not be considered a failing node because communication with the node
can be done without acknowledgements, and there are no periodical frames from the node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 171


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.7** **Controller** **Roles**


LR-NWK:0081.1 Controllers in a Z-Wave Long Range network cannot change role. The controller that has created the
network shall be Primary Controller and all other subsequently included controllers shall be Secondary
Controllers.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 172


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025


**6.5.8** **Dual** **Z-Wave** **and** **Z-Wave** **Long** **Range** **Networks**


LR-NWK:0082.1 Controllers may create both a Z-Wave and Z-Wave Long Range network that they operate on simul
LR-NWK:0083.1 taneously. In this case, they shall use the same HomeID.

LR-NWK:0084.1 Controllers using S2 shall use different key for identical S2 Security Classes in the Z-Wave and the
Z-Wave Long Range network. i.e. the S2 Authenticated key in the Z-Wave network cannot decrypt
S2 Authenticated messages from the Z-Wave Long Range network.

LR-NWK:0085.1 All other nodes in that network shall operate either on the Z-Wave or Z-Wave Long Range PHY/MAC,
but not both simultaneously.

LR-NWK:0086.1 Nodes supporting both Z-Wave and Z-Wave Long Range entering SmartStart learn mode shall issue
SmartStart Prime and SmartStart Inclusion Requests on both PHY/MAC.

LR-NWK:0087.1 Nodes included in a network shall only use the PHY/MAC that they got included with. i.e. a node
included with Z-Wave Long Range shall not operate on Z-Wave and vice-versa.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 173


Specifcations **Z-Wave** **and** **Z-Wave** **Long** **Range** **Network** **Layer** **Specifcation,** **Release** **5.9.0** August 20, 2025

## References


[ITUTG9959] ITU-T G.9959. Short range narrow-band digital radiocommunication transceivers PHY, MAC, SAR and LLC layer specifications. [Online]. URL: [https://www.itu.int/](https://www.itu.int/rec/T-REC-G.9959-201501-I)
[rec/T-REC-G.9959-201501-I.](https://www.itu.int/rec/T-REC-G.9959-201501-I)

[ZWAACC] ZWA ACC. Z-Wave Alliance Application Command Class Specificaiton. [Online]. URL:
[https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWADC] ZWA DC. Z-Wave Alliance Z-Wave Device Class Specificaiton. [Online]. URL: [https:](https://sdomembers.z-wavealliance.org/)
[//sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWADTV2] ZWA DTV2. Z-Wave Alliance Z-Wave Plus v2 Device Type Specificaiton. [Online]. URL:

[https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWADT] [ZWA DT. Z-Wave Alliance Z-Wave Plus Device Type Specificaiton. [Online]. URL: https:](https://sdomembers.z-wavealliance.org/)
[//sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWALRMAC] ZWA LR_MAC. Z-Wave Alliance Long Range MAC Layer Specificaiton. [Online].
URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWALRPHY] ZWA LR_PHY. Z-Wave Alliance Long Range PHY Layer Specificaiton. [Online].
URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWAMCC] ZWA MCC. Z-Wave Alliance Management Command Class Specificaiton. [Online]. URL:

[https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWANPCC] ZWA NPCC. Z-Wave Alliance Network Protocol Command Class Specificaiton. [Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWANPITR] ZWA NPITR. Z-Wave Alliance Node Provisioning Information Type Registry. [Online].
URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWART] ZWA RT. Z-Wave Alliance Z-Wave Plus Role Type Specificaiton. [Online]. URL: [https:](https://sdomembers.z-wavealliance.org/)
[//sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWATECC] ZWA TECC. Z-Wave Alliance Transport-Encapsulation Command Class Specificaiton.

[Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 174


