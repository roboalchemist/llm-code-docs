_**Release**_ _**3.9.0**_

## **Z-Wave Alliance**


**May** **30,** **2025**

## Table of contents


1 Preamble 9
1.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.2 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.3 Revision Record . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.4 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11


2 INTRODUCTION 12
2.1 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2 Audience and Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12


3 NETWORK-LAYER TEST CASE DESCRIPTIONS 13
3.1 General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.2 Frame Format   - Routing information 2-channel frequencies . . . . . . . . . . . . . . . 14
3.2.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.2.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.2.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.2.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.2.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.3 Frame Format   - Routing information 3-channel frequencies . . . . . . . . . . . . . . . 15
3.3.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.3.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.4 Frame Format   - Explorer frame 2 & 3-channel frequencies . . . . . . . . . . . . . . . . 16
3.4.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.5 Frame Format   - Routed NPDU 2-channel frequencies, Header format, Normal function 18
3.5.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.5.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


3.5.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.5.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.5.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.6 Frame Format - Routed NPDU 3-channel frequencies, Header format, Normal function 20
3.6.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.7 Frame Format - Routed ACK NPDU 2-channel frequencies, Header format, Normal
function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.8 Frame Format - Routed ACK NPDU 3-channel frequencies, Header format, Normal
function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.8.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.8.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.8.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.8.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.8.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.9 Frame Format – Routed NPDU 2-channel frequencies, Header format, Routing to a FL
Node . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.9.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.9.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.9.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.9.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.9.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.10 Frame Format – Routed NPDU 3-channel frequencies, Header format, Routing to a FL
Node . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.10.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.10.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.10.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.10.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.10.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.11 Frame Format - Routed NPDU 2-channel frequencies, Header format, Routed Error . 30
3.11.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.11.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.11.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.11.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.11.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.12 Frame Format - Routed NPDU 3-channel frequencies, Header format, Routed Error . 32
3.12.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.12.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.12.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.12.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.12.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.13 Explorer Frame Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.13.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.13.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.13.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.13.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.13.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.14 Normal Explorer Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.14.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.14.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.14.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36


3.14.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.14.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.15 Inclusion Request Explore Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.15.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.15.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.15.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.15.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.15.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.16 Search Result Explore Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.16.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.16.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.16.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.16.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.16.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.17 Command Frames - No Operation Command Class . . . . . . . . . . . . . . . . . . . . 42
3.17.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.17.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.17.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.17.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.17.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.18 Command Frames – Z-Wave Protocol Command Class – Node Information Frame Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.18.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.18.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.18.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.18.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.18.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.19 Command Frames - Z-Wave Protocol Command Class - Request Node Information
Frame Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
3.19.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
3.19.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
3.19.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
3.19.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
3.19.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
3.20 Command Frames - Z-Wave Protocol Command Class - Assign IDs Command . . . . 49
3.20.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
3.20.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
3.20.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3.20.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3.20.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
3.21 Command Frames – Z-Wave Protocol Command Class – Find Nodes in Range Command 52

3.21.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.21.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.21.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.21.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
3.21.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
3.22 Command Frames - Z-Wave Protocol Command Class - Get Nodes in Range Command 55

3.22.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.22.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.22.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.22.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.22.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
3.23 Command Frames - Z-Wave Protocol Command Class - Range Info Command . . . . 56
3.23.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.23.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.23.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.23.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
3.23.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
3.24 Command Frames - Z-Wave Protocol Command Class - Command Complete Command 58


3.24.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.24.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.24.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.24.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.24.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
3.25 Command Frames – Z-Wave Protocol Command Class – Transfer Presentation Command 59

3.25.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.25.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.25.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.25.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3.25.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
3.26 Command Frames - Z-Wave Protocol Command Class - Transfer Node Information
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.26.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.26.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.26.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.26.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
3.26.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
3.27 Command Frames - Z-Wave Protocol Command Class - Transfer Ramge Information
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.27.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.27.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.27.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.27.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
3.27.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
3.28 Command Frames - Z-Wave Protocol Command Class - Transfer End Command . . . 65
3.28.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.28.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.28.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.28.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
3.28.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
3.29 Command Frames – Z-Wave Protocol Command Class – Assign Return Route Command 67

3.29.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
3.29.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
3.29.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
3.29.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
3.29.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
3.30 Command Frames – Z-Wave Protocol Command Class – New Node Registered Command 69

3.30.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
3.30.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
3.30.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
3.30.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
3.30.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
3.31 Command Frames – Z-Wave Protocol Command Class – New Range Registered Command 71

3.31.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
3.31.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
3.31.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
3.31.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
3.31.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
3.32 (Optional Test Case) Command Frames – Z-Wave Protocol Command Class – Transfer
New Primary Controller Complete Command . . . . . . . . . . . . . . . . . . . . . . . 73
3.32.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
3.32.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
3.32.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
3.32.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
3.32.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
3.33 Command Frames - Z-Wave Protocol Command Class - Automatic Controller Update
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
3.33.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75


3.33.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
3.33.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
3.33.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
3.33.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
3.34 Command Frames - Z-Wave Protocol Command Class - SUC NodeID Command . . . 77
3.34.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
3.34.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
3.34.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
3.34.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
3.34.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
3.35 Command Frames - Z-Wave Protocol Command Class - Get SUC Command . . . . . 79
3.35.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
3.35.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
3.35.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
3.35.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
3.35.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
3.36 Command Frames - Z-Wave Protocol Command Class - Set SUC ACK Command . . 81
3.36.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.36.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.36.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.36.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.36.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.37 Command Frames - Z-Wave Protocol Command Class - Assign SUC Return Route
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
3.37.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
3.37.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
3.37.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
3.37.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
3.37.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
3.38 Command Frames - Z-Wave Protocol Command Class - NOP Power Command . . . 84
3.38.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.38.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.38.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.38.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.38.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
3.39 Command Frames - Z-Wave Protocol Command Class - Reserve Node IDs Command 86
3.39.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
3.39.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
3.39.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
3.39.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
3.39.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
3.40 Command Frames - Z-Wave Protocol Command Class - Reserved IDs Command . . . 88
3.40.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.40.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.40.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.40.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.40.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
3.41 Command Frames - Z-Wave Protocol Command Class - Set NWI Mode Command . . 90
3.41.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
3.41.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
3.41.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
3.41.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
3.41.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
3.42 Command Frames - Z-Wave Protocol Command Class - Exclude Request Command . 92
3.42.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
3.42.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
3.42.3 Test Reslut . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
3.42.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
3.42.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93


3.43 Command Frames - Z-Wave Protocol Command Class - Assign Return Route Priority
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
3.43.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
3.43.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
3.43.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
3.43.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
3.43.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
3.44 Command Frames - Z-Wave Protocol Command Class - Assign SUC Return Route
Priority Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
3.44.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
3.44.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
3.44.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
3.44.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
3.44.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
3.45 Command Frames - Z-Wave Protocol Command Class - SmartStart Included Node
Information Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.45.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.45.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.45.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.45.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.45.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.46 Command Frames - Z-Wave Protocol Command Class - SmartStart Prime Command 102
3.46.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
3.46.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
3.46.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
3.46.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
3.46.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
3.47 Command Frames – Z-Wave Protocol Command Class - SmartStart Inclusion Request
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.47.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.47.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.47.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.47.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.47.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
3.48 Functional Description - Routing - Assigning Return Routes . . . . . . . . . . . . . . 106
3.48.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
3.48.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
3.48.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
3.48.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
3.48.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
3.49 Functional Description - Network Inclusion & Formation, NWI, Learn Mode . . . . . 108
3.49.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
3.49.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
3.49.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
3.49.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
3.49.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
3.50 Functional Description - Unsuccessful Routed frame without Routed Error . . . . . . 111
3.50.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.50.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.50.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
3.50.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
3.50.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
3.51 Functional Description - Network Exclusion, NWE, Removing Failing Nodes . . . . . 114
3.51.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.51.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
3.51.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
3.51.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
3.51.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
3.52 Functional Description - Smart Start . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117


3.52.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
3.52.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
3.52.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
3.52.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
3.52.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
3.53 Functional Description - Controller Roles and Network Operations . . . . . . . . . . . 120
3.53.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
3.53.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
3.53.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
3.53.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
3.53.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
3.54 Functional Description - Controller Functionalities and Network Maintenance . . . . . 123
3.54.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
3.54.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
3.54.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
3.54.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
3.54.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
3.55 (3.20 - Negative testing) Command Frames - Z-Wave Protocol Command Class - Assign IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
3.55.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
3.55.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
3.55.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
3.55.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
3.55.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
3.56 (3.21 – Negative testing) Command Frames – Z-Wave Protocol Command Class – Find
Nodes in Range Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
3.56.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
3.56.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
3.56.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
3.56.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
3.56.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
3.57 (3.22 - Negative Testing) Command Frames - Z-Wave Protocol Command Class - Get
Nodes in Range Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
3.57.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
3.57.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
3.57.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
3.57.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
3.57.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
3.58 (3.23 - Negative Testing) Command Frames - Z-Wave Protocol Command Class Range Info Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
3.58.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
3.58.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
3.58.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
3.58.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
3.58.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
3.59 (3.24 - Negative Testing) Command Frames - Z-Wave Protocol Command Class Command Complete Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
3.59.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
3.59.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
3.59.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
3.59.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
3.59.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
3.60 (3.26 - Negative Testing) Command Frames - Z-Wave Protocol Command Class Transfer Node Information Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
3.60.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
3.60.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
3.60.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
3.60.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
3.60.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


3.61 (3.27  - Negative Testing) Command Frames  - Z-Wave Protocol Command Class  Transfer Range Information Command . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
3.61.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
3.61.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
3.61.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
3.61.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
3.61.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
3.62 (3.28  - Negative Testing) Command Frames  - Z-Wave Protocol Command Class  Transfer End Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
3.62.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
3.62.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
3.62.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
3.62.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
3.62.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
3.63 (3.30 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – New
Node Registered Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
3.63.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
3.63.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
3.63.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
3.63.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
3.63.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
3.64 (3.31 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – New
Range Registered Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
3.64.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
3.64.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
3.64.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
3.64.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
3.64.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
3.65 (3.36  - Negative Testing) Command Frames  - Z-Wave Protocol Command Class  - Set
SUC ACK Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
3.65.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
3.65.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
3.65.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
3.65.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
3.65.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
3.66 (3.53  - Negative Testing) Functional Description  - Controller Roles and Network Operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
3.66.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
3.66.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
3.66.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
3.66.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146
3.66.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
3.67 (3.54  - Negative Testing) Functional Description  - Controller Functionalities and Network Maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
3.67.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
3.67.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
3.67.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
3.67.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
3.67.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150


References 151


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 8


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 1 Preamble 1.1 Description


Test Specification for the network layer of the Z-Wave protocol

Reviewed and approved by the Z-Wave Alliance Core Stack Working Group (CSWG).

## 1.2 Disclaimer


THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 9


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 1.3 Revision Record


Table 1.1: Revision History

























© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 10


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 1.4 Abbreviations


Table 1.2: Abbreviations


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 11


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 2 INTRODUCTION 2.1 Purpose


To provide a set of tests that help verify compliance with the Network layer of the Z-Wave technology.

## 2.2 Audience and Prerequisites


An RF sniffer hardware that can be tuned in on the valid frequencies for Z-Wave or a Z-Wave Zniffer
module and PC Application. Z-Wave PC controller or equivalent to execute communication between
the different nodes.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 12


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3 NETWORK-LAYER TEST CASE DESCRIPTIONS 3.1 General Assumptions


The PHY and MAC layers are functional and follow the specification in [ITUTG9959] and is verified
by the set of tests in [ZWAPHYTEST] and [ZWAMACTEST] respectively.

All components are defined by [ZWANWK] and that document is the sole reference for the present
Test Plan.

Services provided by the Network Layer shall be in accordance with requirement [NWK:0008.1].

Routing is assumed to be possible either by isolated routing boxes, physical distance or removing
antennas from the final destination Node and the Primary Controller.

It is assumed that at the beginning of each test each Controller is fully reset and no controller has
any role other than “Real Primary”.

Test Cases towards the end of the spec are the Negative Testing complement to Test Cases described
earlier, they show the number and title of the Test Case they relate to for identification. These
Negative Testing Test Cases, at the current time of issuing of this spec, are not mandatory.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 13


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.2 Frame Format – Routing information 2-channel frequencies


The Network Layer provides mesh routing functionality allowing to deliver messages through repeater
nodes. These nodes can be found through special frames called Explorer Frames. Both types of frames
should follow a specific type of format.


**3.2.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End nodes.


**3.2.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove one of the End Nodes to be one hop away. Send a singlecast frame with NPDU = 0x00
(NOP) frame to it.


**3.2.3** **Test** **Result**


2. Each End Node answers with an ACK frame.

3. The singlecast is routed to the end node through the repeater.


**3.2.4** **Pass** **Criteria**


1. The frame sent to the repeater and then to the end node has Routed information (NWK:0009.1):

a. The frame has the structure as Figure 4.2.

b. The Frame Control field follows the structure as Figure 4.3

c. The routed bit in the Frame Control field is set.

d. The header type is set to 0x01 (singlecast).


**3.2.5** **Fail** **Criteria**


1. The frame sent to the repeater and then to the end node has NO Routed information
(NWK:0009.1):

a. The frame Doesn’t have the structure as Figure 4.2.

b. The Frame Control field doesn’t follow the structure as Figure 4.3

c. The routed bit in the Frame Control field is NOT set.

d. The header type is different from 0x01 (singlecast).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 14


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.3 Frame Format – Routing information 3-channel frequencies


The Network Layer provides mesh routing functionality allowing to deliver messages through repeater
nodes. These nodes can be found through special frames called Explorer Frames. Both types of frames
should follow a specific type of format.


**3.3.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.3.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove one of the End Nodes to be one hop away. Send a frame to it.


**3.3.3** **Test** **Result**


2. Each End Node answers with an ACK frame.

3. The singlecast is routed to the end node through the repeater.


**3.3.4** **Pass** **Criteria**


1. The frame sent to the end node has Routed information (NWK:0009.1):

a. The frame has the structure as Figure 4.2.

b. The Frame Control field follows the structure as Figure 4.4.

c. The header type is set to 0x08 (Routed).


**3.3.5** **Fail** **Criteria**


1. The frame sent to the end node has NO Routed information (NWK:0009.1):

a. The frame Doesn’t have the structure as Figure 4.2.

b. The Frame Control field doesn’t follow the structure as Figure 4.4.

c. The header type is different from 0x08 (Routed).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 15


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.4 Frame Format – Explorer frame 2 & 3-channel frequencies


The Network Layer provides mesh routing functionality allowing to deliver messages through repeater
nodes. These nodes can be found through special frames called Explorer Frames. Both types of frames
should follow a specific type of format.


**3.4.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.4.2** **Test** **Setup**


1. Include the first End Node to PC Controller’s network.

2. Disable it by removing power from it or put it out of range for the controller.

3. Include the second End Node to PC Controller’s network.

4. Enable the first End Node (place it in close range). Place the second End Node one hop away
from the Controller.

5. Send a singlecast with Payload 0x00 (NOP) to the first End Node to verify communication.

6. Send a singlecast with Payload 0x00 (NOP) to the second End Node to verify communication.


**3.4.3** **Test** **Result**


5. The first End Node answers with an ACK frame.

6. The controller tries to reach the second End Node.

a. Controller is unable to reach the second End Node directly and sends an explorer frame.

b. The first End Node repeats this explorer frame and reaches the second End Node.

c. Controller receives an “Explorer Search Result” frame.


**3.4.4** **Pass** **Criteria**


1. The Explorer frames sent from the Controller, repeated by the First End Node and Answered
as an “Explorer Search Result” from the second End Node have information about Routing
(NWK:0009.1):

a. The frame has the structure as Figure 4.2.

b. The Frame Control field follows the structure as Figure 4.3

c. The routed bit in the Frame Control field is set to 0x00.

d. The Header type is 0x05 (Explorer).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 16


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.4.5** **Fail** **Criteria**


1. The Explorer frames have NO information about Routing (NWK:0009.1):

a. The frame Doesn’t have the structure as Figure 4.2.

b. The Frame Control field doesn’t follow the structure as Figure 4.3

c. The routed bit in the Frame Control field is NOT 0x00.

d. The header type is different from 0x05 (Explorer).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 17


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.5 Frame Format – Routed NPDU 2-channel frequencies, Header format, Normal function


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
They use a routing header described in Table 4.5 for 2-channel frequencies (NWK:0205.1).


**3.5.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.5.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove one of the End Nodes to be one hop away. Send a singlecast frame with NPDU = 0x00
(NOP) to it.


**3.5.3** **Test** **Result**


2. Each End Node answers with an ACK frame.

3. The singlecast is routed to the end node through the repeater.


**3.5.4** **Pass** **Criteria**


1. On the routed frames, look for the Routing header: it should follow the structure of Figure 4.7

2. The frame sent to the repeater and then to the end node is sent as a singlecast (Header type
0x01) (NWK:000A.1, NWK:0180.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 0 (NWK:0013.1).

4. The field “Routed Speed Modified” is set to 0 (NWK:000B.1).

5. The “Extended Header” bit is set to 0 (NWK:0011.1).

6. The “R-Ack” (Routed Ack) is set to 0 (NWK:0015.1).

7. The “Direction” bit is set to 0 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is set to 1, since there is only 1 repeater
(NWK:0019.1).

9. The first frame sent, in its “Hops” field holds the value 0 (NWK:001A.1, NWK:001B.1).

10. The second frame sent, in its “Hops” field holds the value 1 (NWK:001A.1, NWK:001D.1)

11. In the Zniffer, before Properties 5, the Field “Repeaters” holds only one NodeID value for
‘Repeater 0’ which is 2 (or the NodeID of the First End Node) (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. There is no “Destination Wake Up” field in the Routing Header (NWK:0023.1).

13. The DLPDU is 0x00 (NOP) (NWK:0034.1).

14. There is no RSSI Extended Header (NWK:0036.1).

15. The receiving node responds with an Acknowledgement frame using the same route
(NWK:0183.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 18


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


16. The delivery of a routed frame follows the basic diagram on Figure 4.13 (NWK:018D.1).


**3.5.5** **Fail** **Criteria**


1. The Routed frames do not have a Routing Header.

2. The frame is not a singlecast (Header type 0x01) (NWK:000A.1, NWK:0180.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 1 (NWK:0013.1).

4. The field “Routed Speed Modified” is NOT set to 0 (NWK:000B.1).

5. The “Extended Header” bit is NOT set to 0 (NWK:0011.1).

6. The “R-Ack” (Routed Ack) is set NOT to 0 (NWK:0015.1).

7. The “Direction” bit is set to 1 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is NOT set to 1, since there is only 1
repeater (NWK:0019.1).

9. The first frame sent, in its “Hops” field holds a value different from 0 (NWK:001A.1,
NWK:001B.1).

10. The second frame sent, in its “Hops” field holds a value different from 1 (NWK:001A.1,
NWK:001D.1)

11. In the Zniffer, before Properties 5, the Field “Repeaters” holds more than one NodeID value
for ‘Repeater 0’ which is 2 (or the NodeID of the First End Node (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. There is A “Destination Wake Up” field in the Routing Header (NWK:0023.1).

13. The routed frame does not include the corresponding Payload (NWK:0034.1).

14. The Routing frame does include RSSI extension (NWK:0036.1).

15. The receiving node responds with an Acknowledgement frame using a different route
(NWK:0183.1).

16. The delivery of the routed frame does not follow the basic diagram Figure 4.13 (NWK:018D.1).

17. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 19


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.6 Frame Format – Routed NPDU 3-channel frequencies, Header format, Normal function


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
They use a routing header described in Table 4.6 for 3-channel frequencies (NWK:0206.1).


**3.6.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.6.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove one of the End Nodes to be one hop away. Send a singlecast frame with NPDU = 0x00
(NOP) to it.


**3.6.3** **Test** **Result**


2. Each End Node answers with an ACK frame.

3. The singlecast is routed to the end node through the repeater.


**3.6.4** **Pass** **Criteria**


1. On the routed frames, look for the Routing header: it should follow the structure of Figure 4.8

2. The frame sent to the repeater and then to the end node is sent as a Routed (Header type 0x08)
(NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 0 (NWK:0013.1).

4. The field “Routed Speed Modified” is not shown in the Zniffer and the corresponding bits of the
frame are set to 0 (NWK:000E.1).

5. In “Properties2” the “Extended” bit is set to 0 (NWK:0011.1).

6. In “Properties3”, The “R-Ack” (Routed Ack) is set to 0 (NWK:0015.1).

7. The “Direction” bit is set to 0 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is set to 1, since there is only 1 repeater
(NWK:0019.1).

9. The first frame sent, in its “Hops” field holds the value 0 (NWK:001A.1, NWK:001B.1).

10. The second frame sent, in its “Hops” field holds the value 1 (NWK:001A.1, NWK:001D.1)

11. In the Zniffer, before “Properties 5”, the Field “Repeaters” holds only one NodeID value for
‘Repeater 0’ which is 2 (or the NodeID of the First End Node) (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. In “Properties5” the “Destination Wake Up” field is set to 0x00 if the second End Node is AL
and 0x02 if it’s a FL (NWK:0024.1, NWK:0025.1).

13. The DLPDU is 0x00 (NOP) (NWK:0034.1).

14. There is no RSSI Extended Header (NWK:0036.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 20


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


15. The receiving node responds with an Acknowledgement frame using the same route
(NWK:0183.1).

16. The delivery of a routed frame follows the basic diagram on Figure 4.14 (NWK:018E.1).


**3.6.5** **Fail** **Criteria**


1. The Routed frames do not have a Routing Header.

2. The frame is not a Routed (Header type 0x08) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 1 (NWK:0013.1).

4. The field “Routed Speed Modified” is shown in the Zniffer or its corresponding bits on the frame
are NOT set to 0 (NWK:000E.1).

5. In “Properties2” the “Extended” bit is NOT set to 0 (NWK:0011.1).

6. In “Properties3”, the “R-Ack” (Routed Ack) is set NOT to 0 (NWK:0015.1).

7. The “Direction” bit is set to 1 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is NOT set to 1, since there is only 1
repeater (NWK:0019.1).

9. The first frame sent, in its “Hops” field holds a value different from 0 (NWK:001A.1,
NWK:001B.1).

10. The second frame sent, in its “Hops” field holds a value different from 1 (NWK:001A.1,
NWK:001D.1)

11. In the Zniffer, before Properties 5, the Field “Repeaters” holds more than one NodeID value
for ‘Repeater 0’ which is 2 (or the NodeID of the First End Node (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. In “Properties5” the “Destination Wake Up” field is NOT set to 0x00 if the second End Node
is AL NOR 0x02 fi it’s a FL (NWK:0024.1, NWK:0025.1).

13. The routed frame does not include the corresponding Payload (NWK:0034.1).

14. The Routing frame does include RSSI extension (NWK:0036.1).

15. The receiving node responds with an Acknowledgement frame using a different route
(NWK:0183.1).

16. The delivery of a routed frame doesn’t follow the basic diagram on Figure 4.14 (NWK:018E.1).

17. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 21


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.7 Frame Format – Routed ACK NPDU 2-channel frequencies, Header format, Normal function


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
They use a routing header described in Table 4.5 for 2-channel frequencies (NWK:0205.1).


**3.7.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.7.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove one of the End Nodes to be one hop away. Send a singlecast frame with NPDU = 0x00
(NOP) to it.


**3.7.3** **Test** **Result**


2. Each End Node answers with an ACK frame.

3. The singlecast is routed to the end node through the repeater.

Routed Ack for an AL and a FL Node are exactly the same.


**3.7.4** **Pass** **Criteria**


1. On the routed Ack frames, look for the Routing header: it should follow the structure of Figure
4.7

2. The frame sent to the repeater and then to the Controller is sent as a singlecast (Header type
0x01) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 0 (NWK:0013.1).

4. The field “Routed Speed Modified” is set to 0 (NWK:000B.1).

5. The “Extended Header” bit is set to 1 (NWK:0011.1).

6. The “R-Ack” (Routed Ack) is set to 1 (NWK:0016.1).

7. The “Direction” bit is set to 1 (NWK:0018.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is set to 1, since there is only 1 repeater
(NWK:0019.1).

9. The first frame sent, in its “Hops” field holds the value 0 (NWK:001A.1, NWK:001C.1,
NWK:001D.1).

10. The second frame sent, in its “Hops” field holds the value 0x0F (NWK:001A.1, NWK:001E.1)

11. In the Zniffer, before Properties 5, the Field “Repeaters” holds only one NodeID value for
‘Repeater 0’ which is 2 (or the NodeID of the First End Node) (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. There is no “Destination Wake Up” field in the Routing Header (NWK:0023.1).

13. In “Properties5”, the “Extended Header Type” field is set to 0x01 (Incoming Routed RSSI Type)
(NWK:0026.1, NWK:002D.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 22


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


14. The “Extended Header Body Length” is set to 4 (NWK:002C.1, NWK:0030.1).

15. The “Extended Header Body” field is structured as Table 4.9 (NWK:002F.1).

16. In the first Routed Ack frame all 4 Bytes are set to 0x7F (NWK:0031.1, NWK:0039.1).

17. In the second Routed Ack frame the RSSI value is updated and set to a value according to Table
4.10 (NWK:0032.1, NWK:0033.1, NWK:0039.1).

18. The Routed Ack frames hold no DLPDU (NWK:0037.1).

19. The Routed Ack holds no “Destination Wake Up Extension” field (NWK:0038.1).


**3.7.5** **Fail** **Criteria**


1. The Routed frames do not have a Routing Header.

2. The frame is not a singlecast (Header type 0x01) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 1 (NWK:0013.1).

4. The field “Routed Speed Modified” is NOT set to 0 (NWK:000B.1).

5. The “Extended Header” bit is NOT set to 0 (NWK:0011.1).

6. The “R-Ack” (Routed Ack) is set NOT to 0 (NWK:0015.1).

7. The “Direction” bit is set to 1 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is NOT set to 1, since there is only 1
repeater (NWK:0019.1).

9. The first frame sent, in its “Hops” field holds a value different from 0 (NWK:001A.1,
NWK:001B.1).

10. The second frame sent, in its “Hops” field holds a value different from 1 (NWK:001A.1,
NWK:001D.1)

11. In the Zniffer, before Properties 5, the Field “Repeaters” holds more than one NodeID value
for ‘Repeater 0’ which is 2 (or the NodeID of the First End Node (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. There is A “Destination Wake Up” field in the Routing Header (NWK:0023.1).

13. In “Properties5”, the “Extended Header Type” field is NOT set to 0x01 (Incomming Routed
RSSI Type) (NWK:0026.1, NWK:002D.1).

14. The “Extended Header Body Length” is NOT set to 4 (NWK:002C.1, NWK:0030.1).

15. The “Extended Header Body” field does NOT follow the structure from Table 4.9 (NWK:002F.1).

16. In the first Routed Ack frame any Byte is different from 0x7F (NWK:0031.1, NWK:0039.1).

17. In the second Routed Ack frame the RSSI value is unchanged (NWK:0032.1, NWK:0033.1,
NWK:0039.1).

18. The Routed Ack frames hold some type of DLPDU (NWK:0037.1).

19. The Routed Ack holds “Destination Wake Up Extension” field (NWK:0038.1).

20. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 23


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.8 Frame Format – Routed ACK NPDU 3-channel frequencies, Header format, Normal function


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
They use a routing header described in Table 4.6 for 3-channel frequencies (NWK:0206.1).


**3.8.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.8.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove one of the End Nodes to be one hop away. Send a singlecast frame with NPDU = 0x00
(NOP) to it.


**3.8.3** **Test** **Result**


2. Each End Node answers with an ACK frame.

3. The singlecast is routed to the end node through the repeater.

Routed Ack for an AL and a FL Node are exactly the same.


**3.8.4** **Pass** **Criteria**


1. On the routed Ack frames, look for the Routing header: it should follow the structure of Figure
4.8

2. The frame sent to the repeater and then to the Controller is sent as a Routed (Header type
0x08) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 0 (NWK:0013.1).

4. The field “Routed Speed Modified” is not shown in the Zniffer and the corresponding bits of the
frame are set to 0 (NWK:000E.1).

5. In “Properties2” the “Extended” bit is set to 1 (NWK:0011.1).

6. In “Properties3”, The “R-Ack” (Routed Ack) is set to 1 (NWK:0016.1).

7. The “Direction” bit is set to 1(NWK:0018.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is set to 1, since there is only 1 repeater
(NWK:0019.1).

9. The first frame sent, in its “Hops” field holds the value 0 (NWK:001A.1, NWK:001C.1,
NWK:001D.1).

10. The second frame sent, in its “Hops” field holds the value 0x0F (NWK:001A.1, NWK:001E.1)

11. In the Zniffer, before “Properties 5”, the Field “Repeaters” holds only one NodeID value for
‘Repeater 0’ which is 2 (or the NodeID of the First End Node) (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. In “Properties5” the “Destination Wake Up” field is not present (NWK:0038.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 24


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


13. The is no DLPDU (NWK:0037.1).

14. In “Properties5”, the “Extended Header Type” (“Extension Type”) field is set to 0x01 (Incoming
Routed RSSI Type) (NWK:0026.1, NWK:002D.1).

15. The “Extended Header Body Length” (“Extension Legth”) is set to 4 (NWK:002C.1,
NWK:0030.1).

16. The “Extended Header Body” (“Extension”) field is structured as Table 4.9 (NWK:002F.1).

17. In the first Routed Ack frame all 4 Bytes are set to 0x7F (NWK:0031.1, NWK:0039.1).

18. In the second Routed Ack frame the RSSI value is updated and set to a value according to Table
4.10 (NWK:0032.1, NWK:0033.1, NWK:0039.1).

19. The first repeater (repeater 0) requests ACK MPDU (NWK:0182.1).


**3.8.5** **Fail** **Criteria**


1. The Routed frames do not have a Routing Header.

2. The frame is not a Routed (Header type 0x08) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 1 (NWK:0013.1).

4. The field “Routed Speed Modified” is shown in the Zniffer or its corresponding bits on the frame
are NOT set to 0 (NWK:000E.1).

5. In “Properties2” the “Extended” bit is NOT set to 0 (NWK:0011.1).

6. In “Properties3”, the “R-Ack” (Routed Ack) is set NOT to 0 (NWK:0015.1).

7. The “Direction” bit is set to 1 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is NOT set to 1, since there is only 1
repeater (NWK:0019.1).

9. The first frame sent, in its “Hops” field holds a value different from 0 (NWK:001A.1,
NWK:001B.1).

10. The second frame sent, in its “Hops” field holds a value different from 1 (NWK:001A.1,
NWK:001D.1)

11. In the Zniffer, before Properties 5, the Field “Repeaters” holds more than one NodeID value
for ‘Repeater 0’ which is 2 (or the NodeID of the First End Node (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. In “Properties5” the “Destination Wake Up” field is present (NWK:0038.1).

13. There is DLPDU present with value of 0x00 (NOP) or otherwise (NWK:0037.1).

14. In “Properties5”, the “Extended Header Type” field is set to 0x01 (Incoming Routed RSSI Type)
(NWK:0026.1, NWK:002D.1).

15. The “Extended Header Body Length” is set to 4 (NWK:002C.1, NWK:0030.1).

16. The “Extended Header Body” field is structured as Table 4.9 (NWK:002F.1).

17. In the first Routed Ack frame all 4 Bytes are set to 0x7F (NWK:0031.1, NWK:0039.1).

18. In the second Routed Ack frame the RSSI value is updated and set to a value according to Table
4.10 (NWK:0032.1, NWK:0033.1, NWK:0039.1).

19. The first repeater (repeater 0) doesn’t request ACK MPDU (NWK:0182.1).

20. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 25


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.9 Frame Format – Routed NPDU 2-channel frequencies, Header format, Routing to a FL Node


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
They use a routing header described in Table 4.5 for 2-channel frequencies (NWK:0205.1).


**3.9.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 1 x AL End Node.

 - 1 x FL End Node.


**3.9.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Wait 5 seconds to ensure FL is asleep. Send a singlecast with Payload 0x00 (NOP) to each End
Node to verify communication.

3. Remove the FL End Node to be one hop away. Wait 5 seconds to ensure FL is asleep. Send a
singlecast frame with NPDU = 0x00 (NOP) to it.


**3.9.3** **Test** **Result**


2. Each End Node answers with an ACK frame. The Controller sends Wake up Beams to the FL
End Node.

3. The singlecast is routed to the end node through the repeater. The repeater Beams to the FL
Node and then sends the routed singlecast.


**3.9.4** **Pass** **Criteria**


1. On the routed frames after the initial re-transmission, look for the Routing header: it should
follow the structure of Figure 4.7

2. The frame sent to the repeater and then to the end node is sent as a singlecast (Header type
0x01) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 0 (NWK:0013.1).

4. The field “Routed Speed Modified” is set to 0 (NWK:000B.1).

5. The “Extended Header” bit is set to 1 (NWK:0012.1). [It will contain Wake Up information].
It May be set to 0 in the first attempt to reach the FL Node (NWK:0185.1) [No Wake Up
Information].

6. The “R-Ack” (Routed Ack) is set to 0 (NWK:0015.1).

7. The “Direction” bit is set to 0 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is set to 1, since there is only 1 repeater
(NWK:0019.1).

9. The first frame sent, in its “Hops” field holds the value 0 (NWK:001A.1, NWK:001B.1).

10. The second frame sent, in its “Hops” field holds the value 1 (NWK:001A.1, NWK:001D.1)

11. In the Zniffer, before “Properties5”, the Field “Repeaters” holds only one NodeID value for
‘Repeater 0’ which is 2 (or the NodeID of the First End Node) (NWK:001F.1, NWK:0020.1,
NWK:0021.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 26


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


12. There is no “Destination Wake Up” field in the Routing Header (NWK:0023.1). [not used in
2-channels]

13. The “Properties5” field is configured following Table 4.7 (NWK:0026.1).

14. The “Extended Header Type” field is set to 0x00 (NWK:0027.1).

15. The “Extended Header Body Length” field is set to 1 (NWK:0028.1).

16. The “Extender Header Body” is configured following Table 4.8 (NWK:0029.1).

17. The DLPDU is 0x00 (NOP) (NWK:0034.1).

18. The “Destination Wake Up” extension is required (NWK:0035.1, NWK:018F.1).

19. There is no RSSI Extended Header (NWK:0036.1).

20. The last repeater returns an Acknowledgement frame to the penultimate repeater: the AL End
Node Sends an ACK back to the Controller even if ‘Ack Req’ bit is set to ‘0’ BEFORE Beaming
the FL End Node (NWK:0181.1).


**3.9.5** **Fail** **Criteria**


1. The Routed frames do not have a Routing Header.

2. The frame is not a singlecast (Header type 0x02) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 1 (NWK:0013.1).

4. The field “Routed Speed Modified” is NOT set to 0 (NWK:000B.1).

5. The “Extended Header” bit is NOT set to 0 (NWK:0012.1).

6. The “R-Ack” (Routed Ack) is set NOT to 0 (NWK:0015.1).

7. The “Direction” bit is set to 1 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is NOT set to 1, since there is only 1
repeater (NWK:0019.1).

9. The first frame sent, in its “Hops” field holds a value different from 0 (NWK:001A.1,
NWK:001B.1).

10. The second frame sent, in its “Hops” field holds a value different from 1 (NWK:001A.1,
NWK:001D.1)

11. In the Zniffer, before Properties 5, the Field “Repeaters” holds more than one NodeID value
for ‘Repeater 0’ or a different NodeID from the First End Node (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. There is A “Destination Wake Up” field in the Routing Header (NWK:0023.1).

13. The “Properties5” field is NOT configured following Table 4.7 (NWK:0026.1).

14. The “Extended Header Type” field is different than 0x00 (NWK:0027.1).

15. The “Extended Header Body Length” field is different than 1 (NWK:0028.1).

16. The “Extended Header Body” is NOT configured following Table 4.8 (NWK:0029.1).

17. The DLPDU is Different from 0x00 (NOP) or is missing (NWK:0034.1).

18. The “Destination Wake Up” extension is missing (NWK:0035.1, NWK:018F.1).

19. The Routing frame does include RSSI extension (NWK:0036.1).

20. The Last repeater does not send an Acknowledgement frame to the penultimate repeater: the
AL does not send an Ack frame to the Controller (NWK:0181.1).

21. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 27


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.10 Frame Format – Routed NPDU 3-channel frequencies, Header format, Routing to a FL Node


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
They use a routing header described in Table 4.6 for 3-channel frequencies (NWK:0206.1).


**3.10.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 1 x AL End Node.

 - 1 x FL End Node.


**3.10.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove the FL End Node to be one hop away. Send a singlecast frame with NPDU = 0x00
(NOP) to it.


**3.10.3** **Test** **Result**


2. Each End Node answers with an ACK frame. The Controller sends Wake up Beams to the FL
End Node.

3. The singlecast is routed to the end node through the repeater. The repeater Beams to the FL
Node and then sends the routed singlecast.


**3.10.4** **Pass** **Criteria**


1. On the routed frames after the initial re-transmission, look for the Routing header: it should
follow the structure of Figure 4.7

2. The frame sent to the repeater and then to the end node is sent as a Routed (Header type 0x08)
(NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 0 (NWK:0013.1).

4. The field “Routed Speed Modified” is not shown in the Zniffer and the corresponding bits of the
frame are set to 0 (NWK:000E.1).

5. In “Properties2” the “Extended” bit is set to 0 (NWK:0012.1).

6. In “Properties3”, the “R-Ack” (Routed Ack) is set to 0 (NWK:0015.1).

7. The “Direction” bit is set to 0 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is set to 1, since there is only 1 repeater
(NWK:0019.1).

9. The first frame sent, in its “Hops” field holds the value 0 (NWK:001A.1, NWK:001B.1).

10. The second frame sent, in its “Hops” field holds the value 1 (NWK:001A.1, NWK:001D.1)

11. In the Zniffer, before “Properties5”, the Field “Repeaters” holds only one NodeID value for
‘Repeater 0’ which is 2 (or the NodeID of the First End Node) (NWK:001F.1, NWK:0020.1,
NWK:0021.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 28


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


12. In “Properties5” the “Destination Wake Up” field is set to 0x02 if it’s a FL (NWK:0024.1,
NWK:0025.1).

13. The “Properties5” field is configured following Table 4.7 (NWK:0026.1).

14. The DLPDU is 0x00 (NOP) (NWK:0034.1).

15. There is no RSSI Extended Header (NWK:0036.1)


**3.10.5** **Fail** **Criteria**


1. The Routed frames do not have a Routing Header.

2. The frame is not a Routed frame (Header type 0x08) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 1 (NWK:0013.1).

4. The field “Routed Speed Modified” is shown in the Zniffer or its corresponding bits on the frame
are NOT set to 0 (NWK:000E.1).

5. In “Properties2” the “Extended” bit is NOT set to 0 (NWK:0011.1).

6. In “Properties3”, the “R-Ack” (Routed Ack) is set NOT to 0 (NWK:0015.1).

7. The “Direction” bit is set to 1 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is NOT set to 1, since there is only 1
repeater (NWK:0019.1).

9. The first frame sent, in its “Hops” field holds a value different from 0 (NWK:001A.1,
NWK:001B.1).

10. The second frame sent, in its “Hops” field holds a value different from 1 (NWK:001A.1,
NWK:001D.1)

11. In the Zniffer, before Properties 5, the Field “Repeaters” holds more than one NodeID value
for ‘Repeater 0’ or a different NodeID from the First End Node (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

12. In “Properties5”, there is no “Destination Wake Up” field or it’s not set to 0x02 (NWK:0024.1,
NWK:0025.1).

13. The “Properties5” field is NOT configured following Table 4.7 (NWK:0026.1).

14. The DLPDU is Different from 0x00 (NOP) or is missing (NWK:0034.1).

15. The Routing frame does include RSSI extension (NWK:0036.1).

16. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 29


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.11 Frame Format – Routed NPDU 2-channel frequencies, Header format, Routed Error


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
They use a routing header described in Table 4.5 for 2-channel frequencies (NWK:0205.1).


**3.11.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x AL End Node.


**3.11.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove power from the second End Node. Send a singlecast frame with NPDU = 0x00 (NOP)
to it.


**3.11.3** **Test** **Result**


2. Each End Node answers with an ACK frame.

3. The singlecast is routed to the end node through the first AL End Node as a repeater. The
repeater retransmits to the Node and then sends a Routed Error frame to the Controller after
it can’t reach the destination.

Routed Error for an AL and a FL Node are exactly the same.


**3.11.4** **Pass** **Criteria**


1. On the Routed Error frame after the initial re-transmission, look for the Routing header: it
should follow the structure of Figure 4.7

2. The Routed Error frame sent to the Controller is sent as a singlecast (Header type 0x01)
(NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 1 (NWK:0014.1).

4. The field “Failed Hop” appears instead of “Routed Speed Modified” (NWK:000F.1).

5. The field “Failed Hop” displays the number of the Hop that did not get an acknowledgement
for the routed frame (NWK:0010.1).

6. The “Extended Header Present” bit is set to 0 (NWK:0011.1).

7. The “R-Ack” (Routed Ack) is set to 0 (NWK:0015.1).

8. The “Direction” bit is set to 1 (NWK:0018.1).

9. In the Zniffer in “Properties4”, the “Repeaters” field is set to 1, since there is only 1 repeater
(NWK:0019.1).

10. The Routed Frame, in its “Hops” field holds the value 0x0F (NWK:001C.1, NWK:001E.1).

11. In the Zniffer, before “Properties5”, the Field “Repeaters” holds only one NodeID value for
‘Repeater 0’ which is 2 (or the NodeID of the First End Node) (NWK:001F.1, NWK:0020.1,
NWK:0021.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 30


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


12. There is no “Destination Wake Up” field in the Routing Header (NWK:0023.1). [not used in
2-channels]

13. The “Properties5” field is empty.

14. There is no DLPDU in the frame (NWK:003A.1).

15. There is no “Destination Wake Up” extension is required (NWK:003B.1).

16. There is no RSSI Extended Header (NWK:003C.1).

17. The first repeater (repeater 0) requests ACK MPDU (NWK:0182.1).

18. The repeater sending the Routed Error Frame sets the Source NodeID as the value of the
Destination NodeID which delivery failed (NWK:0190.1).


**3.11.5** **Fail** **Criteria**


1. The Routed frames do not have a Routing Header.

2. The frame is not a singlecast (Header type 0x01) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 0 (NWK:0014.1).

4. The field “Routed Speed Modified” appears instead of “Failed Hop” (NWK:000F.1).

5. The field “Failed Hop” displays a wrong number of the Hop that did not get an acknowledgement
for the routed frame (NWK:0010.1).

6. The “Extended Header Present” bit is not set to 1 (NWK:0011.1).

7. The “R-Ack” (Routed Ack) is set to 1 (NWK:0015.1).

8. The “Direction” bit is set to 0 (NWK:0018.1).

9. In the Zniffer in “Properties4”, the “Repeaters” field is NOT set to 1, since there is only 1
repeater (NWK:0019.1).

10. The Routed Frame, in its “Hops” field holds a different value than 0x0F (NWK:001C.1,
NWK:001E.1).

11. In the Zniffer, before “Properties5”, the Field “Repeaters” Doesn’t hold only one NodeID value
for ‘Repeater 0’ which would be 2 (or the NodeID of the First End Node) (NWK:001F.1,
NWK:0020.1, NWK:0021.1).

12. The field “Destination Wake Up” is present in the Routing Header (NWK:0023.1). [not used in
2-channels]

13. The “Properties5” field is NOT empty.

14. There is a DLPDU field in the frame (NWK:003A.1).

15. The “Destination Wake Up” extension is present (NWK:003B.1).

16. The Routing frame does include RSSI extension (NWK:003C.1).

17. The first repeater (repeater 0) doesn’t request ACK MPDU (NWK:0182.1).

18. The repeater sending the Routed Error Frame Doesn’t set the Source NodeID as the value of
the Destination NodeID which delivery failed (NWK:0190.1).

19. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 31


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.12 Frame Format – Routed NPDU 3-channel frequencies, Header format, Routed Error


Routed NPDUs are used to transmit a frame when the sending node knows a route to the destination.
They use a routing header described in Table 4.6 for 3-channel frequencies (NWK:0206.1).


**3.12.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.12.2** **Test** **Setup**


1. Include both End Nodes to PC Controller’s network.

2. Send a singlecast with Payload 0x00 (NOP) to each End Node to verify communication.

3. Remove power from one End Node. Send a singlecast frame with NPDU = 0x00 (NOP) to it.


**3.12.3** **Test** **Result**


2. Each End Node answers with an ACK frame.

3. The singlecast is routed to the end node through the repeater. The repeater retransmits to the
Node and then sends a Routed Error frame to the Controller after it can’t reach the destination.

Routed Error for an AL and a FL Node are exactly the same


**3.12.4** **Pass** **Criteria**


1. On the routed frames, look for the Routing header: it should follow the structure of Figure 4.8

2. The Routed Error frame sent to the Controller is sent as a Routed singlecast (Header type 0x08)
(NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 1 (NWK:0014.1).

4. The field “Routed Speed Modified” is not shown in the Zniffer and the corresponding bits of the
frame are set to 0 (NWK:000E.1).

5. In “Properties2” the “Extended” bit is set to 0 (NWK:0011.1).

6. In “Properties3”, The “R-Ack” (Routed Ack) is set to 0 (NWK:0015.1).

7. The “Direction” bit is set to 1 (NWK:0018.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is set to 1, since there is only 1 repeater
(NWK:0019.1).

9. The Routed Frame, in its “Hops” field holds the value 0x0F (NWK:001C.1, NWK:001E.1).

10. In the Zniffer, before “Properties 5”, the Field “Repeaters” holds only one NodeID value for
‘Repeater 0’ which is 2 (or the NodeID of the First End Node) (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

11. There is no “Destination Wake Up” in “Properties5” (NWK:003B.1).

12. There is no DLPDU in the frame (NWK:003A.1).

13. There is no RSSI Extended Header (NWK:003C.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 32


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.12.5** **Fail** **Criteria**


1. The Routed frames do not have a Routing Header.

2. The frame is not a Routed singlecast (Header type 0x08) (NWK:000A.1).

3. In the Zniffer in “Properties3”, the “R-Err” (Routed Error) bit is set to 0 (NWK:0014.1).

4. The field “Routed Speed Modified” is shown in the Zniffer or its corresponding bits on the frame
are NOT set to 0 (NWK:000E.1).

5. In “Properties2” the “Extended” bit is NOT set to 0 (NWK:0011.1).

6. In “Properties3”, the “R-Ack” (Routed Ack) is set NOT to 0 (NWK:0015.1).

7. The “Direction” bit is set to 1 (NWK:0017.1).

8. In the Zniffer in “Properties4”, the “Repeaters” field is NOT set to 1, since there is only 1
repeater (NWK:0019.1).

9. The Routed Frame, in its “Hops” field holds a different value than 0x0F (NWK:001C.1,
NWK:001E.1).

10. In the Zniffer, before Properties 5, the Field “Repeaters” holds MORE than one NodeID value
for ‘Repeater 0’ which is 2 (or the NodeID of the First End Node (NWK:001F.1, NWK:0020.1,
NWK:0021.1).

11. There is “Destination Wake Up” included in “Properties5” (NWK:003B.1).

12. There is ANY type of DLPDU in the frame (NWK:003A.1).

13. There IS RSSI Extended Header (NWK:003C.1).

14. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 33


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.13 Explorer Frame Format


Explore NPDUs are used to transmit a frame when the sending node does not know a route to the
destination. They use the header format described in Figure 4.11. All Explorer type of frames shall
abide to the format described in this Test Case. Each variation shall adjust its values as they are
defined in the subsequent Test Cases.


**3.13.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.13.2** **Test** **Setup**


1. Include The first End Node to the Controller’s network.

2. Remove power from the first End Node. Add the second End Node.

3. Return power to the first End Node. Create one hop in distance from the controller to the
second End Node, using the first one as a repeater.

4. Send a singlecast to the second End Node from the Controller.

5. Observe the format of the explorer frame.


**3.13.3** **Test** **Result**


1. First End Node is correctly included to the Controller’s Network.

2. Second End Node is added to the Controller’s Network and it does not count the first End Node
as a neighbor.

4. Controller tries reaching out to the second End Node directly and when it doesn’t reach, it starts
sending explorer frames.

5. Explorer frame corresponds to the format defined in Table 4.14 (NWK:0207.1)


**3.13.4** **Pass** **Criteria**


1. The version field consists of 3 bits and is set to 0x01 (NWK:003D.1).

2. The Command field consists of 5 bits and it’s encoded according to Table 4.15 (NWK:003E.1).

3. The Direction bit indicates whether it’s an outgoing or a returning frame (NWK:003F.1,
NWK:0040.1, NWK:0041.1, NWK:0042.1).

4. The Source Routed bit shows if the Explore Frame contains a route to follow or if listening
nodes shall repeat and add themselves when they forward the frame (NWK:0043.1, NWK:0044.1,
NWK:0045.1).

5. The Stop Bit Indicates whether an AL node should repeat the frame or not (NWK:0046.1).

6. The Session Tx Random Interval field consists of 8 bits indicates how long should a node wait
before repeating the Explore Frame (NWK:0047.1, NWK:0048.1, NWK:0049.1).

7. The TTL field consists of 4 bits and shows how many nodes can repeat the frame after the
current transmission (NWK:004A.1, NWK:004B.1, NWK:004C.1).

8. The repeater count field consists of 4 bits, and it shows the number of repeaters for the Explore
Frame (NWK:004D.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 34


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


9. The Repeater 0  - 3 fields consist of 8 bits that show the Node ID of the Repeater position for
each of the fields (NWK:004E.1, NWK:004F.1, NWK:0050.1, NWK:0051.1).


**3.13.5** **Fail** **Criteria**


1. Any of the fields described misses its size, description and constraints.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 35


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.14 Normal Explorer Frame


A normal explorer frame consists on the Explore Frame header with no specific payload.


**3.14.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.14.2** **Test** **Setup**


1. Include The first End Node to the Controller’s network.

2. Remove power from the first End Node. Add the second End Node.

3. Return power to the first End Node. Create one hop in distance from the controller to the
second End Node, using the first one as a repeater.

4. Send a singlecast to the second End Node from the Controller.

5. Observe the format of the explorer frame.


**3.14.3** **Test** **Result**


1. First End Node is correctly included to the Controller’s Network.

2. Second End Node is added to the Controller’s Network and it does not count the first End Node
as a neighbor.

4. Controller tries reaching out to the second End Node directly and when it doesn’t reach, it starts
sending explorer frames.

5. Explorer frame corresponds to the format defined in Table 4.14 (NWK:0207.1)


**3.14.4** **Pass** **Criteria**


1. The Normal Explore Frame follows the values in Table 4.16 (NWK:0208.1).

2. The version field consists of 3 bits and is set to 0x01 (NWK:003D.1).

3. The Command field consists of 5 bits and it’s set to 0x00 (NWK:003E.1).

4. The Direction bit is set to 0, (NWK:003F.1, NWK:0041.1).

5. The Source Routed bit is set to 0 (NWK:0043.1, NWK:0044.1).

6. The Stop bit is set to 0 (NWK:0046.1).

7. The Session Tx Random Interval field is more than 0, setting it to nwkRecommendedSessionTxRandomInterval (NWK:0047.1, NWK:0049.1).

8. The TTL field starts with value of 4 and it decreases on each following Explore Frame
(NWK:004A.1, NWK:004B.1).

9. The repeater count is set to 0 in the first frame and 1 in the second (NWK:004D.1).

10. Only the Repeater 0 field show the NodeID of the Repeater in the network, since there are no
more nodes in the network (NWK:004E.1).

11. The frame may hold additional DLPDU payload (NWK:0053.1)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 36


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.14.5** **Fail** **Criteria**


1. The version field is not set to 0x01 (NWK:003D.1).

2. The command field is different from 0x00 (NWK:003E.1).

3. The Direction bit is set to 1 (NWK:003F.1, NWK:0041.1).

4. The Source Routed bit is set to 1 (NWK:0043.1, NWK:0044.1).

5. The stop bit is set to 1 (NWK:0046.1).

6. The Session Tx Random Interval field is 0 (NWK:0047.1, NWK:0049.1).

7. The TTL field does not start with value of 4 nor decreases on each following Explore Frame
(NWK:004A.1, NWK:004B.1, NWK:004C.1).

8. The repeater count is not set to 0 in the first frame nor 1 in the second (NWK:004D.1).

9. The Repeater 0 field never shows the NodeID of the Repeater in the network. Other Repeater fields show a value different than 0, while there are no more repeaters in the network
(NWK:004E.1).

10. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 37


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.15 Inclusion Request Explore Frame


An Inclusion Request Explore Frame (displayed as “Explorer Autoinclusion” in the Zniffer trace) is
used for Network Wide Inclusion and signal nodes of the network to include that the node broadcasting
this frame is in Learning Mode and able to be included in the Network.


**3.15.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.15.2** **Test** **Setup**


1. Include The first End Node to the Controller’s network.

2. Create one hop in distance from the controller to the second End Node, using the first one as a
repeater. Add the second End Node.

3. Send a singlecast to the second End Node from the Controller.


**3.15.3** **Test** **Result**


1. First End Node is correctly included to the Controller’s Network.

2. Second End Node initiates broadcasting Explorer Autoinclusion frames.

a. Once the First End Node receives the “Transfer Presentation” Broadcast from the Controller, it will be able to repeat incoming inclusion requests.

b. There are two Explorer Autoinclusion frames before “Assign Node ID” is routed to the
second End Node.

c. Observe these two Explorer Autoinclusion frames.

3. The Controller routes through the First End Node to the second End Node successfully.


**3.15.4** **Pass** **Criteria**


1. The Explorer Autoinclusion Frame follows the values in Table 4.18 (NWK:0209.1).

2. The Explorer Autoinclusion Frame complies with Table 4.19 (NWK:0055.1).

3. The version field consists of 3 bits and is set to 0x01 (NWK:003D.1).

4. The Command field consists of 5 bits and it’s set to 0x01 (NWK:003E.1).

5. The Direction bit is set to 0, (NWK:003F.1, NWK:0041.1).

6. The Source Routed bit is set to 0 (NWK:0043.1, NWK:0044.1).

7. The Stop bit is set to 0 (NWK:0046.1).

8. The Session Tx Random Interval field is more than 0, setting it to nwkRecommendedSessionTxRandomInterval (NWK:0047.1, NWK:0049.1, NWK:0054.1).

9. The TTL field starts with value of 4 and it decreases on each following Explorer Autoinclusion
Frame (NWK:004A.1, NWK:004B.1).

10. On the second Explorer Autoinclusion frame, the repeater count is set to 1 (NWK:004D.1).

11. Only the Repeater 0 field show the NodeID of the Repeater in the network, since there are no
more nodes in the network (NWK:004E.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 38


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


12. After the 4 Repeaters field there are 4 bytes dedicated to hold a Home ID: 0x00000000 for the
first frame and the HomeID on the second one (NWK:0056.1, NWK:0057.1).

13. The frame carries the Node Information Command Classes on its payload and no other instructions besides the header and properties bytes (NWK:0058.1, NWK:0059.1).


**3.15.5** **Fail** **Criteria**


1. The Explorer Autoinclusion Frame does not comply with the values from Table 4.18
(NWK:0209.1).

2. The Explorer Autoinclusion Frame does not comply with Table 4.19 (NWK:0055.1).

3. The version field is not set to 0x01 (NWK:003D.1).

4. The command field is different from 0x01 (NWK:003E.1).

5. The Direction bit is set to 1 (NWK:003F.1, NWK:0041.1).

6. The Source Routed bit is set to 1 (NWK:0043.1, NWK:0044.1).

7. The stop bit is set to 1 (NWK:0046.1).

8. The Session Tx Random Interval field is 0 or different to nwkRecommendedSessionTxRandomInterval (NWK:0047.1, NWK:0049.1, NWK:0054.1).

9. The TTL field does not start with value of 4 nor decreases on each following Explorer Autoinclusion Frame (NWK:004A.1, NWK:004B.1, NWK:004C.1).

10. The repeater count is not set to 1 (NWK:004D.1).

11. The Repeater 0 field never shows the NodeID of the Repeater in the network. Other Repeater fields show a value different than 0, while there are no more repeaters in the network
(NWK:004E.1).

12. The Home ID of the Node broadcasting the Explore Frame is not shown after the Repeater fields
(NWK:0056.1, NWK:0057.1).

13. The Frames do not carry the Node Information Command Classes on its payload or includes
further information (NWK:0058.1, NWK:0059.1).

14. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 39


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.16 Search Result Explore Frame


A Search Result Explore Frame is used to communicate what repeaters are available in order to reach
a specific target node. Search Result Explore Frame is transmitted only in the return direction.


**3.16.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.16.2** **Test** **Setup**


1. Include The first End Node to the Controller’s network.

2. Remove power from the first End Node. Add the second End Node.

3. Return power to the first End Node. Create one hop in distance from the controller to the
second End Node, using the first one as a repeater.

4. Send a singlecast to the second End Node from the Controller.

5. Observe after the Explorer Frames, there are two Explorer Search Result frames.


**3.16.3** **Test** **Result**


1. First End Node is correctly included to the Controller’s Network.

2. Second End Node is added to the Controller’s Network and it does not count the first End Node
as a neighbor.

4. Controller tries reaching out to the second End Node directly and when it doesn’t reach, it starts
sending explorer frames.

5. The format of the Explorer Search Result frames corresponds to the format defined in Figure
4.15.


**3.16.4** **Pass** **Criteria**


1. The Search Result Explore Frame follows the values in Table 4.20 (NWK:020A.1).

2. The Search Result Explore Frame complies with Table 4.21 (NWK:005A.1).

3. The version field consists of 3 bits and is set to 0x01 (NWK:003D.1).

4. The Command field consists of 5 bits and it’s set to 0x02 (NWK:003E.1).

5. The Direction bit is set to 1 (NWK:0040.1, NWK:0042.1).

6. The Source Routed bit is set to 1 (NWK:0043.1, NWK:0045.1).

7. The Stop bit is set to 1 (NWK:0046.1).

8. The Session Tx Random Interval field is more than 0 in the first frame setting it to nwkRecommendedSessionTxRandomInterval and set to 0 on the second frame (NWK:0047.1, NWK:0048.1).

9. The TTL field is set to 3 and it increases on each following Explore Frame (NWK:004A.1,
NWK:004B.1).

10. The repeater count is set to 1 and then to 0 on the second frame (NWK:004D.1).

11. Only the Repeater 0 field show the NodeID of the Repeater in the network, since there are no
more nodes in the network (NWK:004E.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 40


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


12. After the 4 Repeaters field there is a one-byte field for the sending Node ID that should receive
the Result of Explorer Search Frames (4.2.3.4.2).

13. After the Node ID field, there is a one-byte field for Frame Handle. Which is the sequence
number of the normal Explore Frame for which the Search Result is returned (NWK:005B.1).

14. Following there are TTL result, Repeater Count result and four fields for Repeater Node IDs
(4.2.3.4.2).

15. There should not be any further payload in the Search Result Explore Frame (NWK:005C.1).


**3.16.5** **Fail** **Criteria**


1. The Search Result Explore Frame does not comply with Table 4.20 (NWK:020A.1).

2. The Search Result Explore Frame does not comply with Table 4.21 (NWK:005A.1).

3. The version field does not consist of 3 bits or is not set to 0x01 (NWK:003D.1).

4. The command field is different from 0x02 (NWK:003E.1).

5. The Direction bit is set to 0 (NWK:0040.1, NWK:0042.1).

6. The Source Routed bit is set to 0 (NWK:0043.1, NWK:0045.1).

7. The stop bit is set to 1 (NWK:0046.1).

8. The Session Tx Random Interval field is 0 in the first frame or different to nwkRecommendedSessionTxRandomInterval and set to something different to 0 on the second frame (NWK:0047.1,
NWK:0048.1).

9. The TTL field does not start with value of 4 nor decreases on each following Explore Frame
(NWK:004A.1, NWK:004B.1).

10. The repeater count is not set to 1in the first repeaters nor 0 on the second one (NWK:004D.1).

11. The Repeater 0 field never shows the NodeID of the Repeater in the network. Other Repeater fields show a value different than 0, while there are no more repeaters in the network
(NWK:004E.1).

12. There is no Node ID field, or it does not hold the same ID of the original sending node (4.2.3.4.2).

13. There is no  - field for Frame Handle. Or it’s different from the sequence number of the normal
Explore Frame for which the Search Result is returned (NWK:005B.1).

14. TTL result, Repeater Count result and/or four fields for Repeater Node ID fields are missing in
the Zniffer (4.2.3.4.2).

15. The Frame carries further data in its payload (NWK:005C.1).

16. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 41


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.17 Command Frames – No Operation Command Class


All frames commanding the Z-Wave network function and maintenance functionalities are constructed
in a standard way.


**3.17.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 1 x End Node.


**3.17.2** **Test** **Setup**


1. Include The End Node to the Controller’s network.

2. Send a singlecast to the End Node from the Controller with Payload = 0x00 (NOP).

3. Remove the Node from the Controller’s network.


**3.17.3** **Test** **Result**


2. Observe that the End Node answers with an Acknowledgement frame.

3. The Node ID of the End Node goes back to zero and its Home ID is random.


**3.17.4** **Pass** **Criteria**


1. The singlecast command is constructed as described by Figure 4.7 (NWK:0204.1).

2. The singlecast command has no additional encryption and has no additional payload from upper
layers (NWK:005E.1).

3. All Command classes from 0x00  - 0x1F are NWK command classes, so it’s ID is within that
interval (NWK:005F.2).

4. The NOP frame is answered by the End Node regardless of the type of End Node. It has no
payload (NWK:0060.1).

5. It is used as a probing tool and it can be seen both in the inclusion process and in the exclusion
process (NWK:0061.1).


**3.17.5** **Fail** **Criteria**


1. The singlecast command is NOT constructed as descrbed by Figure 4.7 (NWK:0204.1).

2. The singlecast command has additional encryption or has additional payload from upper layers
(NWK:005E.1).

3. The command’s class ID is higher than 0x1F (NWK:005F.2).

4. The NOP frame is Not answered by some of the End Node types. It has more payload than its
ID (NWK:0060.1).

5. It is used missing in the inclusion process or in the exclusion process (NWK:0061.1).

6. Any of the passing criteria is not met.

7. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 42


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.18 Command Frames – Z-Wave Protocol Command Class – Node Information Frame Command


All frames commanding the Z-Wave network function and maintenance functionalities are constructed
in a standard way. This Command Class is used for Setup and Maintenance of Networks. The Node
Information Frame command is used to advertise the capabilities of the sending node.


**3.18.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.18.2** **Test** **Setup**


1. Include the First End Node to the Controller’s network.

2. Send Node Information Frame from the second End Node (set it in learning Mode), but don’t
set the Controller in inclusion mode.

3. Make the Controller send out its own Node Information Frame.


**3.18.3** **Test** **Result**


1. End Node is included successfully to the network.

2. The second End Node’s NIF is broadcasted.

3. The Controller’s NIF is broadcasted.


**3.18.4** **Pass** **Criteria**


1. The inclusion singlecast commands are constructed as described by Figure 4.7 (NWK:0204.1).

2. The inclusion singlecast commands have no additional encryption and have no additional payload
from upper layers (NWK:005E.1).

3. All Command classes from 0x00  - 0x1F are NWK command classes, so it’s ID is within that
interval (NWK:005F.2).

4. Z-Wave Protocol Command Class shall be supported by all nodes (NWK:0062.1).

5. The Node Information Frame Command is formatted as per Table 4.25 (NWK:0063.1):

a. The Protocol Version Field consists of 3 bits and it’s formatted as per Table 4.26
(NWK:0064.1).

b. Supported Speed (Max Baud Rate) field consists of 3 bits and should hold at least one of
the values from Table 4.27 (NWK:0065.1).

c. If Supported Speed is set to 0, a receiving node shall assume the lower Speed of 9.6 kbps
(NWK:0066.1).

d. The bits in this field follow channel configuration from [G.9959] (NWK:0067.1).

e. Speed Extension field consists of 3 bits and signals if the node supports further Speeds.
It’s encoded as a bitmask following Table 4.28 (NWK:0068.1).

f. The bits in this field comply with channel configuration from [G.9959] (NWK:0069.1).

g. The routing bit indicates if the node can repeat Routed Frames. It’s set to 1 by AL Nodes
and 0 by FL and NL nodes (NWK:006A.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 43


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


h. A Controller shall assume that a node with Routing bit set to 1 and Listening bit set to 1
will repeat frames (NWK:006B.1).

i. Listening Bit advertises if the node Listens or Not. AL nodes shall set this field to 1
(NWK:006C.1).

j. Listening bit is set to 0 by NL and FL nodes (NWK:006D.1).

k. Reserved Bit is set to 0 (NWK:006E.1, NWK:006F.1).

l. The Controller bit determines if the emitting node is a Controller by setting it to 1, or if
it’s not by setting it to 0. This test has used only End Nodes so they should be set to 0
and the Routing End Node must be set to 1 (NWK:0070.1, NWK:0072.1).

m. The Specific Device Bit is set to 1 when the Specific Device Type byte-field is included in
the Node Information Frame (NWK:0073.1).

n. The Routing End Node bit is set to 1 if the node is a End Node. If it’s set to 1, the
Node Information Frame does not include a Basic Device Type field. If it’s set to 0, the
Controller bit shall be set to 1 (NWK:0074.1, NWK:0075.1, NWK:0076.1).

o. The Beam Capability it indicates if the Node Can issue Wake Up Beams. The value 0
indicates the sending node cannot wake up FL nodes. The value 1 indicates that it does
(NWK:0077.1).

p. The optional functionality bit indicates that the node supports additional application Command Classes to the mandatory minimum from [SDS10242]. A sending node should set
this field to 1 (NWK:0078.1).

q. Basic Device Type is omitted since the controller field is set to 0 (NWK:007A.1)

r. The Generic Device Class Byte identifies what type of Generic Device the node is
(NWK:007C.1).

s. The Specific Device Byte identifies what Specific device the node is (NWK:007D.1).

t. Command Class Bytes list the Supported Command Classes. It shall not be longer than
35 bytes. The Command Classes are in the range 0x21… 0xFFFF. Command Classes in
the Range 0x00 … 0x20 are not advertised (NWK:007E.1, NWK:007F.1).

6. Protocol version shall be set to 0x03 (NWK:0080.1, NWK:0081.1).

7. For the Second End Node, when it sends its NIF: Its format matches the one described in the
Criteria 5.a    - 5.t. And the Data of the NIF shall be forwarded to the upper protocol layer of
the nodes within range (NWK:0082.1).

8. When the Controller sends its NIF, its format is mostly the same as 5.a – 5.t but for the following
differences:

l. The Controller bit is set to 1 and the Node Information Frame includes a Basic Device
Type field (NWK:0070.1, NWK:0071.1).

n. The Routing End Node field is set to 0, The Node Information Frame includes a Basic
Device Type field and the Controller Bit is set to 1 (NWK:0075.1, NWK:0076.1).

q. Basic Device type is included because the Controller bit is set to 1. It is encoded according
to Table 4.29 (NWK:0079.1, NWK:007B.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 44


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.18.5** **Fail** **Criteria**


1. The inclusion singlecast commands are NOT constructed as described by Figure 4.7
(NWK:0204.1).

2. The inclusion singlecast commands have additional encryption or have additional payload from
upper layers (NWK:005E.1).

3. The command’s class ID of inclusion frames are higher than 0x1F (NWK:005F.2).

4. The device does not support Z-Wave Protocol Command Class (NWK:0062.1).

5. The Node Information Frame is not formatted as per Table 4.25 (NWK:0063.1):

a. The Protocol Version Field is either more or less than 3 bits or does not hold any value
from Table 4.26 (NWK:0064.1).

b. The Supported Speed (Max Baud Rate) field is either more or less than 3 bits or does not
follow the values from Table 4.27 (NWK:0065.1).

c. If the Supported Speed (Max Baud Rate) is set to 0, but the receiving node does not
assume the lower Speed of 9.6 kbps (NWK:0066.1).

d. The bits in this field do not comply with [G.9959] (NWK:0067.1).

e. The speed extension field is either more or less than 3 bits in length. It is not encoded as
a bitmask or does not follow Table 4.28 (NWK:0068.1).

f. The bits in this field do not comply with channel configuration from [G.9959]
(NWK:0069.1).

g. The routing bit does not reflect if the node is either AL, or FL/NL (NWK:006A.1).

h. The controller does not list the node correctly as AL or FL/NL after inclusion
(NWK:006B.1).

i. The End Node sets its Listening Bit to 0 if it’s an AL node (NWK:006C.1).

j. The End Node sets its Listening Bit to 1 if it’s either an FL or NL node (NWK:006D.1).

k. Security bit is not set to 1 if the node supports security S0 or S2 (listed in the Supported
Command Classes) (NWK:006E.1, NWK:006F.1).

l. The Controller bit is set to 1 and the Routing End Node bit is set to 0 (NWK:0070.1,
NWK:0072.1).

m. The Specific Device bit is set to 0 but there is a Specific Device field included in the NIF
(NWK:0073.1).

n. The routing End Node bit is set to 0 despite the node being a End Node. Or it includes
a Basic Device Type field. Or if it is set to 0 and the Controller bit is also set to 0
(NWK:0074.1, NWK:0075.1, NWK:0076.1).

o. The beam capability is not reflecting the capabilities of the End Node (NWK:0077.1).

p. The optional functionality is set     - 0 (NWK:0078.1).

q. Basic Device Type is included despite the Node not being a Controller (NWK:007A.1).

r. The Generic Device Class field is omitted, or it contains values not defined (NWK:007C.1).

s. The Specific Device Byte is missing or does not identify the what the node is
(NWK:007D.1).

t. Command class bytes are more than 35 bytes. Or Their values are outside the range 0x21…
0xFFFF. Or it advertises Command Classes in the Range 0x00 … 0x20 (NWK:007E.1,
NWK:007F.1).

6. Protocol version is not set to 0x03 (NWK:0080.1, NWK:0081.1).

7. For the Second End Node: Any of the Fail conditions from 5.a … 5.t are met. Or the Data of
the NIF is not forwarded to the upper protocol layer of the nodes within range (NWK:0082.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 45


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


8. When the Controller sends its NIF, its format met any of the failing conditions 5.a  - 5.t with
the following differences:

l. The Controller bit is set to 1 AND Node Information Frame does include a Basic Device
Type field and the Controller Bit is set to 1 (NWK:0070.1, NWK:0071.1).

n. The Routing End Node field is set to 1, Or it is set to 0 and The Node Information
Frame doesn’t include a Basic Device Type, or the Controller Bit is set to 0 (NWK:0075.1,
NWK:0076.1).

q. Basic Device Type is not included despite of the Controller bit is set to 1. Or it’s not
encoded as per Table 4.29 (NWK:0079.1, NWK:007B.1).

9. Any of the passing criteria is not met.

10. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 46


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.19 Command Frames – Z-Wave Protocol Command Class – Request Node Information Frame Command


This command is used to request a node to return a Node information Frame Command.


**3.19.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 1 x End Node.


**3.19.2** **Test** **Setup**


1. Include the First End Node to the Controller’s network.

2. Send Request Node Information Frame to End Node.

3. Include the secondary Controller to the first Controller’s network.

4. Send Request Node Information Frame to the Secondary Controller.

5. Send Request Node Information Frame to End Node as a multicast.

6. Sed Request Node Information Frame to the secondary Controller as a multicast.


**3.19.3** **Test** **Result**


1. End Node is included successfully to the network.

2. The End Node answers with a Node Information Frame as a singlecast.

3. The Secondary Controller is included successfully to the network.

4. The Secondary Controller answers with a Node Information Frame as a singlecast.

5. The End Node does not answer the request that was sent as a multicast.

6. The secondary Controller does not answer the request that was sent as a multicast.


**3.19.4** **Pass** **Criteria**


1. The singlecast command is constructed as described by Figure 4.7 (NWK:0204.1).

2. The singlecast command has no additional encryption and has no additional payload from upper
layers (NWK:005E.1).

3. All Command classes from 0x00  - 0x1F are NWK command classes, so it’s ID is within that
interval (NWK:005F.2).

4. The Request Node Information Frame Command is formatted as per Table 4.30 (NWK:0083.1).

5. This command is sent as a singlecast by default for both receiving nodes (NWK:0084.1).

6. The receiving node returns a Node Information Frame Command in response to the singlecast
command and ignores it when it’s sent as a multicast for both receiving nodes (NWK:0085.1).

7. The End Node answers with a Node Information Frame that follows the same format as described
in Pass Criteria 5 of the previous Test Case.

8. The Controller answers with a Node Information Frame that follows the same format as described
in Pass Criteria 8 in the previous Test Case.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 47


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.19.5** **Fail** **Criteria**


1. The singlecast command is NOT constructed as descrbed by Figure 4.7 (NWK:0204.1).

2. The singlecast command has additional encryption or has additional payload from upper layers
(NWK:005E.1).

3. The command’s class ID is higher than 0x1F (NWK:005F.2).

4. The request Node Information Frame Command does not follow the format of Table 4.30
(NWK:0083.1).

5. The command is sent as multicast by default for either receiving node (NWK:0084.1).

6. Either of the receiving nodes answers to the Request Node Information Command with a Node
Information Frame regardless if it was sent as singlecast or multicast (NWK:0085.1).

7. The End Node answers with a Node Information Frame that meets any of the fail conditions
from the Fail Criteria 5 in the previous Test Case.

8. The Controller answers with a Node Information Frame that meets any of the fail conditions
from the Fail Criteria 8 in the previous Test Case.

9. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 48


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.20 Command Frames – Z-Wave Protocol Command Class – Assign IDs Command


This command is used to assign NodeID and HomeID to the receiving node.


**3.20.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 1 x End Node.


**3.20.2** **Test** **Setup**


1. Include the End Node to the Controller’s network.

2. Send Assign ID command to End Node with a random value for Node ID and Home ID as a
singlecast (send as Hex [01 03 NN HH HH HH HH] on Command Classes view).

3. Send Assign ID command to End Node as a multicast with a random value for Node ID and
Home ID (send as Hex and enable “Force Multicast” in Command Classes View).

4. Include the secondary Controller to the first Controller’s network.

5. Send Assign ID command to the secondary Controller as a singlecast (send as Hex [01 03 NN
HH HH HH HH] on Command Classes view).

6. Send Assign ID command to the secondary Controller as a multicast multicast (send as Hex and
enable “Force Multicast” in Command Classes View).

7. Set Assign ID in Command Class view (in Hex) to hold a value in its NodeID field to be different
from 0x00 and Home ID to be 4x[00]

8. Set the End Node in learning mode and send the command from the Controller’s Command
Class view. Once it’s been received set the End Node Again in Learning Mode to Obesrve its
NIF.

9. Set the secondary Controller in learning mode and send the command from the Controller’s
Command Class view.

10. Set Assign ID to hold a value in its HomeID field to be different from 4x[0x00] and a Node ID
to be 0x00.

a. Afterwards: Reset the End Node and reinclude it replacing its previous ID in the Controller’s Node List by running “Is Failed” and then “Replace Failed” and setting the End
node in Learning Mode to reinclude it and occupy its previous ID.

b. Do the same for the Secondary Controller.

11. Set the End Node in learning mode and send the command from the Controller’s Command
Class view.

12. Set the secondary Controller in learning mode and send the command from the Controller’s
Command Class view.

13. Remove the End Node from the Controller’s network.

14. Remove the secondary Controller from the Controller’s network.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 49


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.20.3** **Test** **Result**


1. End Node is included successfully to the Controller’s Network.

2. End Node answers the command with an Ack frame only.

3. End Node ignores the multicast.

4. The secondary Controller is included successfully to the Controller’s Network.

5. The secondary Controller answers the command with an Ack frame only.

6. The secondary Controller ignores the multicast.

8. The End Node accepts the change in its NodeID and Home ID: They match with the values set.

10. The secondary Controller doesn’t accept the change in its NodeID; It resets its NodeID to 0x01,
HomeID to random but retains all the information of the network as if it was still included.

a. The End Node is included again under its previous Node ID.

b. Same for the secondary Controller

11. The End Node accepts the change in its HomeID and NodeID.

12. The secondary Controller accepts the change in its HomeID and NodeID; but retains all the
information of the network as if it was still included.

13. The End node is removed from the network.

14. The secondary Controller is removed from the network.


**3.20.4** **Pass** **Criteria**


1. During inclusion of the End Node and the Controller, the “Assign ID” command is sent as a
singlecast and follows the format as per Table 4.31 (NWK:0086.1, NWK:0089.1).

2. The NodeID field of the command is not 0x00 and it’s less than 0xE8 in both cases
(NWK:0087.1).

3. The HomeID values match the HomeID of the Network of the Controller in both cases
(NWK:0088.1).

4. The End Node and the Secondary Controller accept both HomeID and NodeID as they have
been put in learning mode and their inclusion is successful (NWK:008A.1).

5. The End Node and the Secondary Controller ignore the command once they have been included
to the network and they are no longer in learning mode (NWK:008B.1).

6. When the nodes are removed, the NodeID and HomeID fields are set to 0x00 (NWK:0087.1,
NWK:0088.1, NWK:008A.1).

7. While in learning mode, the End Node and the Secondary Controller accept the new NodeID
and accepting the value of HomeID whichever it is (NWK:0087.1) [It should only accept change
of Node ID to exclusion when aready included].

8. While in learning mode, the End Node and the Secondary Controller accept the command when
the HomeID field is not set to 0x00; The End Node and Secondary Controller should self-reset
when receiving the command with HomeID is set to 4 x [00] (NWK:0088.1) [It should only
accept change of HomeID to “random” when NodeID is 0x00 and self reset to a random one
when assigned Home ID 00].


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 50


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.20.5** **Fail** **Criteria**


1. The “Assign ID” command does not comply with the specified format nor it’s sent as a singlecast
by default (NWK:0086.1, NWK:0089.1).

2. The NodeID field is set to 0x00 during inclusion or it’s higher than 0xE8 (NWK:0087.1).

3. The HomeId values don’t match the HomeID of the Controller’s network (NWK:0088.1).

4. The End Node and secondary Controller don’t accept the command regardless of being set in
learning mode (NWK:008A.1).

5. The End Node and secondary Controller change their Node ID or Home ID when receiving the
“Assign ID” command after being included even if they are not in learning mode (NWK:008B.1).

6. The NodeID and HomeID are not set by default to 0x00 when removing the nodes (NWK:0087.1,
NWK:0088.1, NWK:008A.1).

7. The nodes accept changing their NodeID to something other than 0x00 and remain in the same
Network (NWK:0087.1).

8. The nodes accept changing their HomeID to something other than the HomeID of the Controller’s Network while being excluded and retain their same NodeID (NWK:0088.1).

9. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 51


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.21 Command Frames – Z-Wave Protocol Command Class – Find Nodes in Range Command


This command is used to request the receiving node to find the nodes in direct range.


**3.21.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 2 x AL End Node.

 - 2 x FL End Node.

 - 1 x NL End Node.

This Test Case needs to be performed under S0 or S2 inclusion.


**3.21.2** **Test** **Setup**


1. Include to the primary Controller’s Network the first AL End Node.

2. Include the NL End Node to the network.

3. Include the first FL End Node to the network.

4. Include the secondary Controller to the network.

5. Remove power from the secondary Controller. Include the second AL End Node.

6. Include the second FL End Node.


**3.21.3** **Test** **Result**


1. The first AL End Node is included to the Controller’s Network. Observe in the Zniffer trace
that Controller sends “Find nodes in Range” with Node ID 1 in the Mask Bytes. AL End Node
sends a NOP Power frame to the primary Controller.

2. The NL node is included, observe in the Zniffer trace that Controller sends “Find nodes in
Range” with Node ID 1 & 2 in the Mask Bytes. NL End Node sends a NOP Power frame to
the primary Controller, it sends a NOP frame to the first End Node included.

3. The first FL End Node is included, observe in the Zniffer trace that Controller sends “Find
nodes in Range” with Node ID 1 & 2 in the Mask Bytes. FL End Node sends a NOP frame to
the primary Controller, it sends a NOP Power frame only to the first End Node (it doesn’t try
with the NL End Node).

4. The secondary Controller is included, observe in the Zniffer trace that Controller sends “Find
nodes in Range” with Node ID 1 & 2 in the Mask Bytes. The secondary Controller sends a
NOP Power frame to the primary Controller, it sends a NOP frame to the first End Node. It
does not send anything to the NL End Node. The primary Controller sends one more “Find
Nodes in Range” Command with Node ID 3, the secondary Controller it tries sending a Wake
up Beam directly to the FL node, followed by finally completing sending the NOP Power to the
FL End Node.

5. The second AL End Node is included, observe in the Zniffer trace that Controller sends “Find
Nodes in Range” with Node ID 1, 2 & 5 in the Mask Bytes. It sends a NOP Power frame to the
primary Controller, it sends a NOP Power frame to the first End Node, it ignores the NL End
Node and it tries reaching first the secondary Controller. Then the primary Controller sends a
second “Find Nodes in Range” command, the second AL End Node tries reaching the FL End
Node (Node ID 3) with Wake Up beams.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 52


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


6. The second FL End Node is included, observe in the Zniffer trace that Controller sends “Find
nodes in Range” with Node ID 1, 2, 5 & 6 in the Mask Bytes. The second FL End Node sends
a NOP Power frame to the primary Controller, it sends a NOP Power frame to the first AL
End Node, it ignores the NL End Node and it tries reaching first the secondary Controller and
finally to the second AL End Node. Then the primary Controller sends a second “Find Nodes
in Range”, the second FL Save tries reaching the first FL End Node with Wake Up beams and
finally a regular NOP Power frame.


**3.21.4** **Pass** **Criteria**


1. The “Find Nodes in Range” Command in all instances follows the format described by Table
4.32 (NWK:008D.1).

2. The “Find Nodes in Range” command shall be sent as singlecast by default and it shall be ignored
as a multicast. The “Node Bitmask” field shall not be set to 0 (NWK:009D.1, NWK:009E.1,
NWK:00A1.1).

3. The first byte holds 2 reserved bits set to 0 in positions 6 & 5 (NWK:008E.1).

4. Reserved bit is set to 0 (false) and shall be ignored by the receiving node (NWK:008F.1
NWK:0090.1).

5. The Node Bitmask is displayed as “Mask Bytes”. It holds the Nodes the receiving Node shall
try to reach and no other values (NWK:0091.1).

6. The length of the Bitmask should match the number of bytes defined in the Bitmask Length
(NWK:0092.1).

7. The Node Bitmask is a mask where each bit represents a node corresponding to the bit position,
a bit set to 1 shall instruct the receiver to search for the node of matching number, set to 0 that it
shall not, so that the First byte of this field represents nodes 1 … 8 (NWK:0093.1, NWK:0094.1,
NWK:0095.1).

8. The Wake Up Time field is not displayed by the Zniffer, but it’s preset in the frame structure.
It’s used to define whether the receiving node shall use a Wake Up beam and its duration.
All nodes in the Node Bitmask field shall have the same Wake Up Time value (NWK:0096.1,
NWK:0097.1).

9. Wake Up Time shall be present in the “Find Node in Range” Command and the receiving node
shall validate it. If it’s not present, a receiving node shall use the Wakeup Time value 0x00
(NWK:0098.1, NWK:0099.1).

10. The Data Rate field is not displayed but it’s part of the frame’s structure. It’s used to set the
speed of transmission during Neighbor discovery. It shall be set by default to 0x01 or be encoded
as per Table 4.34. Its presence shall be verified by the receiving node and if it’s not present,
the default Data rate to be used should be that of value 0x01 (NWK:009A.1, NWK:009B.1,
NWK:009C.1).

11. The receiving node shall issue NOP to all NodeIDs in the Node Bitmask field and return a
“Command Complete” command to the node that requested the range test (NWK:009F.1).

12. All Z-Wave nodes shall keep a bitmask record of the last range test (NWK:00A0.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 53


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.21.5** **Fail** **Criteria**


1. The “Find Nodes in Range” does not comply with the specified format (NWK:008D.1).

2. The command is sent as multicast by default or the “Node Bitmask” field is set to 0
(NWK:009D.1, NWK:009E.1, NWK:00A1.1).

3. The reserved bits are not set to 0 (NWK:008E.1).

4. The Speed Present bit don’t correspond to the type of receiving nodes (NWK:008F.1,
NWK:0090.1).

5. The Node Bitmask hold values that don’t match to the NodeIDs the receiving node should try
to reach (NWK:0091.1).

6. The length of the Node Bitmask doesn’t match the number of bytes defined in Bitmask Length
(NWK:0091.2).

7. The Node Bitmask is not used as a mask matching bit positions to NodeIDs. Or the bits set to
1 are ignored while the ones set to 0 are searched for OR the first byte in Node Bitmask fields
is mapped to a different set of NodeIDs than 1 … 8 (NWK:0093.1, NWK:0094.1, NWK:0095.1).

8. The nodes defined in the command don’t require or don’t match the same Wake Up Time value
(NWK:0096.1, NWK:0097.1).

9. Wake Up Time is not present in the “Find Node in Range” or it’s not validated by the receiving
Node. When missing, the Node does not use Wake Up Time value of 0x00 (NWK:0098.1,
NWK:0099.1).

10. The Data Rate field is not set by default to 0x01 nor follows the Table 4.34 (NWK:009A.1,
NWK:009B.1, NWK:009C.1).

11. The receiving node does not issue NOP frames to the NodeIDs in the Node Bitmask field or
doesn’t return a “Command Complete” command to the originating node (NWK:009F.1).

12. The Z-Wave node doesn0t keep a bitmask record of the last range test (NWK:00A0.1).

13. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 54


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.22 Command Frames – Z-Wave Protocol Command Class – Get Nodes in Range Command


The Get Nodes in Range command is used to request the list of direct range neighbors detected with
the last range test.


**3.22.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 1 x End Nodes.


**3.22.2** **Test** **Setup**


1. Include the first End Node to the primary Controller’s network.

2. Include the secondary Controller to the primary Controller’s network.


**3.22.3** **Test** **Result**


1. Observe in the Zniffer trace that once the Neighbor Range Test is finished, the Controller sends
“Get Nodes in Range”. The receiver answers with “Range Info” containing only the primary
Controller.

2. Observe in the Zniffer trace that once the Neighbor Range Test is finished, the Controller
sends “Get Nodes in Range”. The receiver answers with “Range Info” containing the primary
Controller and the first End Node.


**3.22.4** **Pass** **Criteria**


1. The “Get Nodes in Range” command follows the format as Table 4.35 and it’s sent by default
as singlecast (NWK:00A2.1, NWK:00A3.1).

2. The receivers validate the command and return a “Range Info” command in response
(NWK:00A4.1).


**3.22.5** **Fail** **Criteria**


1. The “Get Node sin Range” command doesn’t follow the specified format, or it is sent as multicast
by default (NWK:00A2.1, NWK:00A3.1).

2. The nodes do not respond with a “Range Info” command in response (NWK:00A4.1).

3. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 55


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.23 Command Frames – Z-Wave Protocol Command Class – Range Info Command


The Range Info command is used to advertise the list of direct range neighbors detected with the last
range test.


**3.23.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 1 x AL End Node.

 - 1 x FL End Node.


**3.23.2** **Test** **Setup**


1. Include the AL End Node to the primary Controller’s network.

2. Include the FL End Node. Observe the “Node Range Info” it sends to the primary Controller.

3. Include the secondary Controller.

4. Send a NOP frame from the secondary Controller to the FL End Node.


**3.23.3** **Test** **Result**


1. During inclusion, the End Node responds to Get Nodes in Range with “Node Range Info”
command.

2. The FL End Node is included correctly. Its “Node Range Info” frame holds a “Node bitmask”
field containing the primary Controller and the first AL End Node only.

3. The secondary Controller is included, after it searches for the FL End Node with beams, it
responds to the primary Controller with “Node Range Info” including a Wake up Time field.

4. The secondary Controller beams to the FL End Node before delivering the NOP frame.


**3.23.4** **Pass** **Criteria**


1. The Node Range Info commands follow the format from Table 4.36 (NWK:00A6.1).

2. The Length in Bytes of the Node Bitmask field should be the same as the one defined by the
“Bitmask Length” field (NWK:00A7.1).

3. The Node Bitmask is treated as a Mask and not as the direct NodeID values. The bits set as
1 indicate that the corresponding NodeID is within range of the node sending this frame. The
first byte represents nodes 1…8 (NWK:00A8.1, NWK:00A9.1, NWK:00AA.1).

4. When the Wake-Up Time field is present, its value must be verified by the receiver. When it’s
not, the receiver assumes a value of 0x00 (NWK:00AB.1, NWK:00AC.1).

5. The Node Bitmasks holds the result of the last Range Test and not previous ones. If there were
no Tests, the Node Bitmask field is set to 0x00 (NWK:00AD.1, NWK:00AE.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 56


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.23.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 57


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.24 Command Frames – Z-Wave Protocol Command Class – Com- mand Complete Command


Used to advertise the completion of a given task.


**3.24.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 1 x AL End Node.

 - 1 x FL End Node.


**3.24.2** **Test** **Setup**


1. Include the AL End Node to the primary Controller’s network. Look for the Command Complete
frame.

2. Include the FL End Node to the network.

3. Include the secondary Controller to the network.


**3.24.3** **Test** **Result**


1. The AL End Node is successfully included. There is only 1 Command Complete frame.

2. The FL End Node is successfully included. There is only 1 Command Complete frame.

3. The secondary Controller is successfully included. There is 1 Command Complete frame after
reaching for the primary Controller and the AL End Node and 1 after beaming for the FL End
Node.


**3.24.4** **Pass** **Criteria**


1. Command Complete follows the format from Table 4.37 (NWK:00B0.1).

2. The Sequence Number field is set by default to 0 and the following frames don’t need a different
value (NWK:00B1.1).

3. The primary Controller Waits until Command Complete is issued and the Node issuing it can
receive commands right away (NWK:00B3.1).


**3.24.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 58


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.25 Command Frames – Z-Wave Protocol Command Class – Trans- fer Presentation Command


This command is used to indicate that the controller is trying to initiate Network Management Functions (Add node, remove node, perform Controller replication).


**3.25.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 2 x End Nodes.


**3.25.2** **Test** **Setup**


1. Set the primary Controller in inclusion mode.

2. Include the first End Node.

3. Create one hop between the primary Controller and the second End Node.

4. Set the primary Controller in Network Wide Inclusion.

5. Set the second End Node one hop away in Learning mode.

6. Set the primary Controller in Network Wide Inclusion mode.

7. Create one hop between the primary Controller and the second Controller. Set the secondary
Controller in Learning Mode NWI.

8. Set the primary Controller in Network Wide Inclusion mode.

9. Set the first End Node in Learning Mode.

10. Stop the primary Controller from being in NWI and send a “Transfer Presentation” command
to the first End Node [01 08 02]

11. Stop the first End Node from being in Learning Mode.

12. Set the primary Controller in Network Wide Exclusion mode.

13. Set the first End Node in Learning mode.

14. Set the primary Controller in Network Wide Exclusion mode.

15. Set the first End Node in Learning mode.


**3.25.3** **Test** **Result**


1. Observe the Controller broadcasts Transfer Presentation Command.

2. The first End Node is included correctly.

3. The primary Controller and the second End Node can’t reach each other directly.

4. The Controller broadcasts Transfer Presentation Command.

5. The second End Node is included through the repeater.

6. The Controller broadcasts Transfer Presentation Command.

7. The secondary Controller is included through repeaters.

8. The Controller broadcasts Transfer Presentation Command.

9. The first End Node transmits its Node Information Frame.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 59


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


10. The first End Node does not respond to the “Transfer Presentation” command while in learning
Mode.

11. The End node is no longer in Learning Mode. The Network is unaltered.

12. The controller broadcasts Transfer Presentation Command.

13. The first End Node is removed directly.

14. The Controller broadcasts Transfer Presentation Command.

15. The first End Node is assigned NodeID 0 again.


**3.25.4** **Pass** **Criteria**


1. The Command has the format described by Table 4.38 (NWK:00B7.1).

2. The Option field byte shall follow Table 4.39 and its bit 0 always be set to 1 (NWK:00B8.1,
NWK:00BB.1).

a. During inclusion the option Field is set to 5.

b. During Exclusion it’s set to 3.

3. Transfer Presentation Command should only be transmitted when the Controller is in Inclusion
or Exclusion mode (NWK:00B9.1).

4. It shall be sent only broadcast to destination 255 (NWK:00BA.1).

5. A node set in learning mode shall send a Node Information Frame when it receives Transfer
Presentation Command (NWK:00BC.1).

6. IF a node is not in learning mode or if it’s being included by another controller, it shall not send
its Node Information Frame (NWK:00BD.1).

7. For a node already included, while the Controller is in Inclusion Mode, the End Node should
not return Node Information if it’s set in learning mode (NWK:00BE.1).

8. A Node in SmartStart Learn Mode does not return Node Information Frame (NWK:00BF.1).


**3.25.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 60


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.26 Command Frames – Z-Wave Protocol Command Class – Trans- fer Node Information Command


This command is used for transferring the Node Information Frame from one controller to another.


**3.26.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 3 x End Nodes.


**3.26.2** **Test** **Setup**


1. Include all 3 End Nodes to the primary controller.

2. Include the secondary Controller to the primary Controller’s Network.

3. Remove the secondary Controller.


**3.26.3** **Test** **Result**


1. All 3 End Nodes are included to the Controller’s Network.

2. The secondary Controller is included.

a. Primary Controller sends 5 “Transfer Node Information” frames to the secondary Controller: one per each End Node already included and one for the first Controller and one
for the second Controller.

3. Secondary Controller is removed.


**3.26.4** **Pass** **Criteria**


1. Transfer Node Information Command follows the Format from Table 4.40, which extends from
the description of the fields of the regular Node Information Frame (NWK:00C0.1, NWK:00C1.1,
NWK:00C4.1).

2. Each sequence number is individual and unique for each Node Information being transferred
from one Controller to another (NWK:00C2.1).

3. Sequence Numbers are used to detect duplicates (NWK:00C3.1).

4. The command is sent only when including a secondary Controller (NWK:00C5.1).

5. The command is sent only singlecast (NWK:00C6.1).

6. When inclusion of the secondary Controller is finished, the secondary Controller has updated
its Node List (NWK:00C9.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 61


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.26.5** **Fail** **Criteria**


1. The command is not formatted as described, the values don’t match the ones of the reported
by the Node (NWK:00C0.1, NWK:00C1.1, NWK:00C4.1).

2. The sequence number on all Transfer Node Information frames is the same (NWK:00C2.1).

3. Sequence Numbers irrelevant to detect duplicates (NWK:00C3.1).

4. The command is sent outside the inclusion of a secondary Controller (NWK:00C5.1).

5. The command is not sent only as singlecast (NWK:00C6.1).

6. The secondary Controller does not update its internal Node List after finishing inclusion
(NWK:00C9.1).

7. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 62


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.27 Command Frames – Z-Wave Protocol Command Class – Trans- fer Ramge Information Command


This command is used to transfer a node’s range test result from one Controller to another.


**3.27.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 3 x End Nodes.


**3.27.2** **Test** **Setup**


1. Include all 3 End Nodes to the primary controller.

2. Include the secondary Controller to the primary Controller’s Network.

3. Include the third Controller to the primary Controller’s Network.


**3.27.3** **Test** **Result**


1. All 3 End Nodes are included to the Controller’s Network.

2. The secondary Controller is included.

a. Primary Controller sends 5 “Transfer Range Information” frames to the secondary Controller: one per each End Node already included and one for the first Controller and one
for the second Controller.

3. The third Controller is included.

a. Primary Controller sends 6 “Transfer Range Information” frames to the third Controller.

b. The secondary Controller ignores these commands.


**3.27.4** **Pass** **Criteria**


1. Transfer Range Information is formatted as per Table 4.41 and it extends from the Range Info
command (NWK:00CA.1, NWK:00CB.1).

2. The Sequence Number Field increases each time it’s sent, and if it remains static it’s ignored
(NWK:00CC.1, NWK:00CD.1).

3. It is sent as singlecast by default (NWK:00CE.1).

4. This command is only sent while including or transferring main role between controllers and not
with an End Node (NWK:00CF.1).

5. A Controller that is not in learning mode ignores the transmission of this command
(NWK:00D2.1).

6. After this command is received, the receiving Controller updates its internal routing table
(NWK:00D3.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 63


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.27.5** **Fail** **Criteria**


1. Transfer Range Info does not comply with Table 4.41 or its fields don’t match the basic Range
Info Command (NWK:00CA.1, NWK:00CB.1).

2. The Sequence Number Field remains static and it’s accepted regardless of being seemingly
duplicate (NWK:00C.1, NWK:00CD.1).

3. It is not sent as singlecast by default (NWK:00CE.1).

4. It is sent regardless of whether a Controller or a End Node is being included (NWK:00CF.1).

5. A Controller accepts this command regardless of whether it’s in learning mode or not
(NWK:00D2.1).

6. A receiving Controller does not update its internal routing table after receiving this command
(NWK:00D3.1).

7. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 64


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.28 Command Frames – Z-Wave Protocol Command Class – Trans- fer End Command


This command is used to advertise the end of the current network operation (Static route request,
Automatic controller update, Controller replication).


**3.28.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 1 x End Node.

Perform this test under Security 2 Inclusion.


**3.28.2** **Test** **Setup**


1. Include the End Node.

2. Include secondary Controller.

3. Remove all nodes and reset the primary Controller.

4. Include the secondary Controller.

5. Include End Node to the network with Primary Controller.

6. Include the Third Controller to the Network with Primary Controller.

7. Set the Third Controller in Learning mode and activate “Shift” in primary Controller.


**3.28.3** **Test** **Result**


1. End Node is included. Primary Controller states that it IS the Primary and SIS of the Network.

2. Secondary Controller is included.

a. Transfer End is sent by the primary Controller after transferring Node information and
Node Range information.

b. The status reported is “Transfer OK= 0x01”.

3. All nodes are removed. Primary Controller is reset.

4. The secondary Controller is included as SIS of the Network. Primary Controller is set as “Real
Primary”.

a. Secondary Controller sends Transfer End with Status “0x02” = transfer Update Done.

5. End Node is included to the network.

a. After secure inclusion is finished, Secondary Controller (SIS) sends Transfer End with
Status “0x02” = Transfer Update Done.

6. Third Controller is included to the network.

a. Primary Controller sends “Transfer End OK = 0x01” after transferring Node and Neighbors
information to it.

b. Secondary (SIS) Controller sends Transfer End with Status “0x02” = Transfer Update Done
to Primary Controller after Secure Inclusion.

7. The primary Controller transfers Node Information and Node Range information to the Third
Controller. The Third Controller is set as “Real Primary” Controller now.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 65


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.28.4** **Pass** **Criteria**


1. Transfer End follows the format from Table 4.42 (NWK:00D4.1).

2. The Status field notifies Network information. It is encoded as per Table 4.43 (NWK:00D5.2).

3. Transfer End is sent only after each Network Management operation and it always advertises
its status (NWK:00D6.1, NWK:00D7.1).


**3.28.5** **Fail** **Criteria**


1. Transfer End doesn’t follow the format from Table 4.42 (NWK:00D4.1).

2. The Status field does not follow Table 4.43 (NWK:00D5.2).

3. Transfer End is sent outside Network Management operations or the Status field is missing
(NWK:00D6.1, NWK:00D7.1).

4. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 66


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.29 Command Frames – Z-Wave Protocol Command Class – Assign Return Route Command


This command is used to advertise the assigned route to the receiving node. Most used for associations
between End Node devices.


**3.29.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 1 x End Node with more than 1 association group.

 - 2 x AL End Nodes.

 - 2 x FL End Nodes.


**3.29.2** **Test** **Setup**


1. Include the End Node with multiple association groups (AL1) and both AL End Nodes (AL2 &
AL3) to the network.

2. In PC Controller, go to the Associations perspective.

a. Select AL1 in the Nodes groups view.

b. Enable “Assign return routes” check box under the “Create” button.

c. Select one AL2 or AL3 in the Controller’s Node List.

d. Press “Create” to make an association from a group other than 1, to the End Node selected
in the Controller’s Node List.

e. Select the other End Node in the Controller’s Node List.

f. Press “Create” to make an association from the same group, to the End Node selected
second.

3. Execute the association created.

4. Remove both AL2 & AL3 and include both FL End Nodes.

5. Repeat Step 2 for both FL End Nodes and remove the existing associations to AL End Nodes.

6. Execute the associations created.

7. Include the secondary Controller. Assign Return Route is not used in this inclusion process.


**3.29.3** **Test** **Result**


1. The End Nodes are included in direct range of the Controller.

2. In associations Perspective, for the AL1:

a. Association is sent from the Controller to the End Node’s Association Group As well as 4
“Assign Return Routes” frames.

b. The second association is sent from the Controller to the End Node’s Association Group
as well as 4 or 8 “Assign Return Routes” frames this time.

3. Observe how the AL1 sends commands to each of the nodes associated.

4. AL2 & AL3 are removed, and FL End Nodes are included.

5. In Associations Perspective:

a. The associations to FL End Nodes are sent as well as “Assign Return Routes” Frames.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 67


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


b. Each of them holds a value in their “Destination Wake Up” field.

6. The associations are executed, and the FL nodes are targeted for singlecasts followed by beaming
to each of them.

7. Secondary Controller is included.


**3.29.4** **Pass** **Criteria**


1. Assign Return Route is formatted as per Table 4.44 (NWK:00D8.1).

2. It is not used during inclusion. In order to assign return routes to the SUC “Assign SUC Return
Route” is used, instead (NWK:00DF.1).

3. It shall not be sent when including Controllers (NWK:00DE.1).

4. A receiving node shall store its return routes when receiving it (NWK:00E0.1).

5. In its “Number of Hops/Repeaters” field, a value of 0 indicates a direct transmission and values
from 1 … 4 indicate the number of repeaters (NWK:00D9.1, NWK:00DA.1).

6. Route Number is the index of the route being assigned, the first one shall have route number 0
(NWK:00DB.1).

7. The “Destination Wake Up” field, indicates the Wake-Up time capability of the destination
Node. It’s encoded as per Table 4.45 (NWK:00DC.1).

8. The “Destination Speed” Field specifies the data rate capability of the destination node, it shall
be encoded as per Table 4.46 (NWK:00DD.1).


**3.29.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 68


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.30 Command Frames – Z-Wave Protocol Command Class – New Node Registered Command


This command is used to notify the SIS Controller that an inclusion controller has included a new
node in the network.


**3.30.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 2 x End Node.


**3.30.2** **Test** **Setup**


1. Set the primary controller to be SIS.

2. Include the secondary Controller.

3. Set the first End Node in Learning mode and the secondary Controller (Inclusion Controller) in
inclusion mode.

4. Set the first End Node in Learning Mode. Include the second End Node with the secondary
Controller.

5. Remove the first End Node with Inclusion Controller.


**3.30.3** **Test** **Result**


1. The primary Controller is set as SIS.

2. The secondary Controller is set as Inclusion Controller.

3. The End Node broadcasts its Node Info Frame and secondary Controller notifies the primary
Controller with a “New Node Registerd” frame about the inclusion.

4. The second End Node is included. The first End Node ignores “New Node Registered” sent to
the SIS.

5. The inclusion controller notifies the primary Controller of the removal with a New Node Registered.


**3.30.4** **Pass** **Criteria**


1. The frame is formatted as per Figure 4.33, it extends from the basic Node Information Frame
and it should contain the same values as the NodeID of the node being included (NWK:00E1.1,
NWK:00E2.1, NWK:00E3.1).

2. When the node is being excluded from the Network, the Generic Device Class field is set to 0
(NWK:00E4.1).

3. It is sent by default as a singlecast and it is ignored by any End Node listening during the
inclusion (NWK:00E5.1, NWK:00E6.1, NWK:00E7.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 69


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.30.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 70


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.31 Command Frames – Z-Wave Protocol Command Class – New Range Registered Command


This command is used to advertise the range test results that an inclusion controller has performed
when including a new node.


**3.31.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 2 x End Nodes.


**3.31.2** **Test** **Setup**


1. Include the first End Node to the primary Controller’s network.

2. Include the secondary Controller to the primary Controller’s network.

3. Create one Hop of distance between the first End Node and the second End Node (Remove their
antennas or place the network in a RF shielded wired system to control impedance of radio, so
that they don’t see each other during inclusion of the second End Node).

4. Use the Inclusion Controller to include the second End Node into the network.


**3.31.3** **Test** **Result**


1. The first End Node is included into the Controller’s network.

2. The second Controller is included, it becomes an Inclusion Controller.

3. Neither End Node is within range of the other, but in range of both Controllers.

4. The second End Node is included.

a. After probing the neighbor’s range, the Inclusion Controller sends the New Range Registered Command to the primary Controller.


**3.31.4** **Pass** **Criteria**


1. The New Range Registered Command follows the format from Figure 4.34, it is sent by default
as singlecast and only during an inclusion from an Inclusion Controller or Controller Update
(NWK:00E8.1, NWK:00F0.1, NWK:00F1.1).

2. The “NodeID” field corresponds to the node which the neighbors range test was performed
(NWK:00E9.1).

3. The “Neighbor Nodes Bitmask Length” field corresponds to the number of nodes within range
of the node being included. It should be set to the minimum of 1 (for both the SIS and the
Inclusion Controller in range) (NWK:00EA.1).

4. The “Neighbors Nodes Bitmask” field holds the list of NodeIDs that the node being included/just
performed the neighbors Range Test can reach, its length shall match the one described by the
“Neighbor Nodes Bitmask Length” field (NWK:00EB.1, NWK:00EC.1).

5. The “Neighbor Nodes Bitmask” field is an actual Bitmask, where the LSB represents NodeID
1, the value 0 represents the absence of said node as a neighbor to the node being included
and the value 1 represents that the node is a neighbor within range to the node being included
(NWK:00ED.1, NWK:00EF.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 71


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.31.5** **Fail** **Criteria**


1. The New Range Registered Command does not follow the specified format, it’s sent to any
Controller or it’s sent outside inclusion or Controller update (NWK:00E8.1, NWK:00F0.1,
NWK:00F1.1).

2. The “NodeID” field is not that of the node that performed the neighbors range test
(NWK:00E9.1).

3. The “Neighbor Nodes Bitmask Length” does not show the actual number of neighboring nodes,
not even the minimum set to 1 (NWK:00EA.1).

4. The “Neighbors Nodes Bitmask” field doesn’t hold the list of Nodes that the node being included/performed the Neighbors Range Test can reach. Its length is not matching that of the
“Neighbor Nodes Bitmask Length” field (NWK:00EB.1, NWK:00EC.1).

5. The “Neighbor Nodes Bitmask” field is not used as a bitmask matching bit positions to Node
IDs or the values set to 0 and 1 are inverted (NWK:00ED.1, NWK:00EF.1).

6. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 72


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.32 (Optional Test Case) Command Frames – Z-Wave Protocol Command Class – Transfer New Primary Controller Complete Command


This command is used to complete the Primary Controller role transfer procedure to another Controller
node.


**3.32.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.


**3.32.2** **Test** **Setup**


1. Include the second Controller to the network of the first one.

2. Include the third Controller to the first Controller’s network.

3. Set the third Controller in learning Mode.

4. In the RealPrimary Controller activate the “Shift” function.

5. In the third Controller (now RealPrimary) override the field “Controller Type” to a different
value than the actual Controller Type of the third Controller.

6. Don’t set the first Controller in learning Mode. Activate “Shift” in the third Controller.

7. Set the first Controller in learning Mode. Activate “Shift” in the third Controller.


**3.32.3** **Test** **Result**


1. The first Controller is set as RealPrimary, Inclusion Controller. The second one as SUC, SIS
Controller.

2. The third Controller is included and set as Inclusion Controller.

3. The Third Controller is set in learning Mode.

4. The RealPrimary begins Primary Controller Shift.

a. At the end it sends the Transfer New Primary Controller Complete Command.

5. The value of the “Controller Type” field is overridden.

6. Primary Controller Transfer tries to start.

a. It does not start since no other Controller Node is in learning Mode.

7. Primary Controller Transfer starts and at the end it’s not validated since the value of the
Controller Type does not match the Generic Device Class field in its Node Information Frame.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 73


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.32.4** **Pass** **Criteria**


1. The command Transfer New Primary Controller Complete is formatted as per Table 4.49
(NWK:00F4.1).

2. The “Controller Type” field matches the Generic Device Class field in the sender’s Node Information Frame Command (NWK:00F5.1)

3. The receiving node assumes the role of Primary Controller role and can start using Primary
Controller functionalities (NWK:00EE.1).

4. No transfer happens when there is no node in learning Mode (NWK:00F6.1).


**3.32.5** **Fail** **Criteria**


1. The command Transfer New Primary Controller Complete does not follow the specified format
(NWK:00F4.1).

2. The “Controller Type” field differs from the Generic Device Class field in the sender’s Node
Information Frame Command (NWK:00F5.1).

3. The receiving node remains as a regular Inclusion/secondary Controller after the Transfer New
Primary Controller function is completed by receiving the Transfer New Controller Complete
Command (NWK:00EE.1).

4. A controller node not set in Learning Mode accepts the command (NWK:00F6.1).

5. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 74


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.33 Command Frames – Z-Wave Protocol Command Class – Auto- matic Controller Update Command


This command is used to request transfer of the network topology information from the SUC/SIS
controller to another controller in the network.


**3.33.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 1 x End Node.


**3.33.2** **Test** **Setup**


1. Include the second Controller to the network of the first one.

2. Include the third Controller to the first Controler’s network.

3. Include the End Node to the network using the third Controller.

4. Observe the node List of the RealPrimary Controller.

5. On the RealPrimary Controller press the “Update” button (right next to the “shift” button).

6. Remove the End Node using the third Controller.

7. On the RealPrimary Controller, in Command Class pane, send ‘Controller Update Start’ (0x01
0x10) multicast with “Suppress Multicast Follow up” enabled.

8. On the RealPrimary Controller, remove the previous Override so that the command is sent as
a singlecast. select on the Node List to send it to the third Controller.

9. On the RealPrimary Controller press ‘Send’. It should be addressed to the third Controller.


**3.33.3** **Test** **Result**


1. The first Controller is set as RealPrimary, Inclusion Controller. The second one as SUC, SIS
Controller.

2. The third Controller is included and set as Inclusion Controller.

3. The Third Controller includes the End Node to the network.

a. Before the inclusion begins, Automatic Controller Update Start is sent from the third
Controller to the SUC/SIS.

4. Observe that the list does not have the End Node included to the network, but the SUC/SIS
Controller does.

5. The first Controller (RealPrimary) sends Automatic Controller Update Start to the SUC/SIS.

a. Its node list holds now the NodeID of the End Node included by the third Controller.

6. The End Node is removed from the network.

a. The RealPrimary Controller does not reflect this on its Node list.

7. The RealPrimary Controller sends Automatic Controller Update Start to the SUC/SIS as a
multicast.

a. It is ignored by the SIS.

b. The RealPrimary Controller does not remove the End Node from its node list.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 75


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


8. Real Primary Controller is set to send singlecast and selected the third Controller on its Node
List.

9. The third Controller answers to this with a SUC Node ID command with the NodeID of the
SUC/SIS.


**3.33.4** **Pass** **Criteria**


1. The Automatic Controller Update Start command follows the format from Figure 4.36. It is
sent in an automatic way by default as a singlecast to the SUC/SIS from an Inclusion Controller
before performing an inclusion (NWK:00F7.1, NWK:00F8.1, NWK:00F9.1).

2. When a SUC/SIS receives this command, it responds with topology updates to the sending node
using New Node Registered Commands (NWK:00FB.1).

3. If the receiving controller is not SUC/SIS, it responds with a SUC Node ID command to inform
the sending node of the correct NodeID of the SUC/SIS (NWK:00FC.1).

4. This command shall be ignored when it’s sent multicast (NWK:00FD.1).


**3.33.5** **Fail** **Criteria**


1. The Automatic Controller Update Start command doesn’t follow the specified format. It is not
sent automatically by default as a singlecast to the SUC/SIS from an Inclusion Controller before
performing an inclusion (NWK:00F7.1, NWK:00F8.1, NWK:00F9.1).

2. The SUC/SIS ignores this command or does not respond with topology updates to the sending
node (NWK:00FB.1).

3. The non-SUC/SIS controllers fail at reporting back the actual NodeID of the SUC/SIS Controller
if they get the command addressed to them (NWK:00FC.1).

4. SUC/SIS Controller answers to this command even when it’s sent as a multicast (NWK:00FD.1).

5. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 76


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.34 Command Frames – Z-Wave Protocol Command Class – SUC NodeID Command


This command is used to advertise the NodeID of the SUC and its capabilities.


**3.34.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.


**3.34.2** **Test** **Setup**


1. Include the second Controller to the primary one.

2. Include the third Controller using the RealPrimary Controller.

3. Reset the SUC/SIS Controller.

4. In the RealPRimary Controller’s Node list Select the second (SUC/SIS) Controller and click the
“it’s failed” button.

5. Activate “Remove Failed” button on RealPrimary Controller.

6. Repeat steps 4 & 5 on the third Controller.

7. Include the reset second Controller to the network with RealPrimary Controller.


**3.34.3** **Test** **Result**


1. The first Controller is set to RealPrimary, Inclusion Controller. The second Controller is set to
SUC/SIS Controller.

2. The third Controller is included as an Inclusion Controller.

a. During its inclusion, RealPrimary Controller sends SUC NodeID to it with the NodeID of
the second Controller      - SUC/SIS.

3. SUC/SIS Controller resets its NodeID to 1 and Home ID to random.

4. RealPrimary Controller probes the (self-reset) second (SUC/SIS) Controller by sending NOP
frames to it.

a. Upon failing to find it, it sets its Node ID in red in its Node list.

5. The reset SUC/SIS is removed from RealPRimary Controller’s Node List.

6. Verifications 4 & 5 apply for the third Controller.

7. The second Controller is included as SUC/SIS Controller.

a. During Inclusion RealPrimary Controller sends to the second Controller being re-included
SUC Node ID command with NodeID set to 0 (since there is currently no SUC/SIS Controller in the network).

b. At the end of the re-inclusion, the second Controller is set to be SUC/SIS.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 77


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.34.4** **Pass** **Criteria**


1. The SUC NodeID command follows the format of Table 4.51 (NWK:00FE.1).

2. During regular operation the “NodeID” field of SUC NodeID command is set to the NodeID
value of the SUC/SIS Controller. When there is no SUC/SIS in the network it’s set to 0
(NWK:00FF.1).

3. The “Capabilities” field follows Table 4.52 or it’s missing. When it’s missing it’s assumed to
have value 0x00 (NWK:0100.1, NWK:0101.1).

4. This command shall not be sent to the same NodeID that is contained in the “NodeID” field of
the command (NWK:0102.1).


**3.34.5** **Fail** **Criteria**


1. The SUC NodeID command is not formatted as specified (NWK:00FE.1).

2. The “NodeID” field is set to a value different from the SUC/SIS NodeID value, or it’s changing
without having changed the SUC/SIS, or it’s set to 0 as if there was no SUC/SIS when there is.
Or it retains the same value even after having verified the SUC/SIS Controller has failed and is
removed from the network (NWK:00FF.1).

3. The “Capabilities” field holds values outside the defined by Table 4.52 or in case of missing
altogether it’s not considered as 0x00 (NWK:0100.1, NWK:0101.1).

4. This command is sent to the same NodeID in its “NodeID” field, instead of using Set SUC
Command (NWK:0102.1).

5. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 78


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.35 Command Frames – Z-Wave Protocol Command Class – Get SUC Command


This command is used by a primary Controller to grant the SUC Role to another controller in the
network.


**3.35.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 1 x End Node.

Disable security in all PC Controllers


**3.35.2** **Test** **Setup**


1. Include the second Controller to the primary one.

2. Include the third Controller using the RealPrimary Controller.

3. Reset the SUC/SIS Controller.

4. Select the second Controller in the RealPrimary Controller’s Node list and click the “it’s failed”
button.

5. Activate “Remove Failed” button on RealPrimary Controller.

6. Repeat steps 3, 4 & 5 for the third Controller.

7. Using “Add Custom” and disabling “Automatically set as SIS” Include the End Node with
RealPrimary Controller.

8. Include the reset third Controller to the network with RealPrimary Controller using “Add Custom” with disabled “Automaticaly set as SIS”.

9. Send to the End Node “Set SUC” as a hex commad: {0x01 0x12 0x01 0x01}

10. Send it instead to the secondary Cotroller.


**3.35.3** **Test** **Result**


1. The first Controller is set to RealPrimary, Inclusion Controller. The second Controller is set to
SUC/SIS Controller.

a. The first Controller sends Set SUC Command after the Node Information interview.

2. The third Controller is included as an Inclusion Controller.

3. SUC/SIS Controller resets its NodeID to 1 and Home ID to random.

4. RealPrimary Controller probes the second Controller by sending NOP frames to it.

a. Upon failing to find it, it sets its Node ID in red in its Node list.

5. The reset SUC/SIS is removed from RealPRimary Controller’s Node List.

6. Verifications 3, 4 & 5 apply for the third Controller.

7. RealPrimary Controller includes the End Node to the Network.

8. The third Controller is included as secondary Controller.

9. End Node ignores the command.

10. The secondary Controller accepts the command answering with “Set SUC ACK” and setting its
role to “SUC, SIS, NodeIdServerPresent, OtherNetwork”.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 79


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.35.4** **Pass** **Criteria**


1. The Set SUC command follows the format from Table 4.53 (NWK:0103.1).

2. The “State” field advertises functionality and shall be set to 0x01. All other values are reserved
and must be ignored (NWK:0104.1, NWK:0105.1).

3. The “SUC Capabilities” field specifies the services the SUC should run. It follows Table 4.52 it
shall be set to 0x01 (NWK:0106.1, NWK:0107.1).

4. Set SUC command can only be issued by a Primary Controller, End Nodes shall ignore it
(NWK:0108.1).

5. A Controller being included that receives this command shall assume the SUC role and answer
with a Set SUC ACK command (NWK:0109.1, NWK:010A.1).


**3.35.5** **Fail** **Criteria**


1. The Set SUC command is not formatted as specified (NWK:0103.1).

2. The “State” field is not set to 0x01 (NWK:0104.1, NWK:0105.1).

3. The “SUC Capabilities” field doesn’t follow Table 4.52 and it’s not set to 0x01 (NWK:0106.1,
NWK:0107.1).

4. Set SUC command is issued by a non-Primary Controller and it’s ignored by End Nodes
(NWK:0108.1).

5. A Controller being included that received this command doesn’t assume the SUC role and fails
at answering with a Set SUC ACK command (NWK:0109.1, NWK:010A.1).

6. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 80


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.36 Command Frames – Z-Wave Protocol Command Class – Set SUC ACK Command


This command is used to respond to a Set SUC Command.


**3.36.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.


**3.36.2** **Test** **Setup**


1. Include the second Controller to the primary one.

2. Include the third Controller using the RealPrimary Controller.


**3.36.3** **Test** **Result**


1. The first Controller is set to RealPrimary, Inclusion Controller. The second Controller is set to
SUC/SIS Controller.

a. The second Controller responds to Set SUC Command with Set SUC ACK command.

2. The third Controller is included as an Inclusion Controller.


**3.36.4** **Pass** **Criteria**


1. The Set SUC ACK follows the format on Table 4.54 (NWK:010B.1).

2. When a Controller accepts the SUC role it sets its “Result” field is set to 0x01 (NWK:010C.1).

3. The “Capabilities” field is encoded as per Table 4.52 (NWK:010D.1).


**3.36.5** **Fail** **Criteria**


1. The Set SUC ACK doesn’t follow the specified format (NWK:010B.1).

2. When a Controller accepts the SUC role, it doesn’t set its “Result” is to 0x01 or it uses entirely
any other values (NWK:010C.1).

3. The “Capabilities” field doesn’t follow Table 4.52 (NWK:010D.1).

4. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 81


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.37 Command Frames – Z-Wave Protocol Command Class – Assign SUC Return Route Command


This command is used to notify the receiving node about the route on how to reach the SUC.


**3.37.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 2 x End Node.


**3.37.2** **Test** **Setup**


1. Include the first End Node to the network of the first Controller using “Add Custom”, disabling
“Automatically set as SIS” in direct range.

2. Include the second Controller to the first one.

3. Place the second End Node one hop away from the SIS Controller Controller using the first End
Node as a repeater. Proceed to start a Network Wide Inclusion on the SIS Controller.


**3.37.3** **Test** **Result**


1. The first End Node is included in direct range to the RealPrimary Controller.

a. Upon inclusion, the RealPrimary Controller Does not send Assign SUC Return Route to
the End Node.

2. The second Controller is included to the first one’s network.

a. The first Controller is set as RealPrimary, Inclusion Controller. The second is set as
SUC/SIS Controller.

3. The second End Node is included through the first End Node as a repeater.

a. The SIS Controller sends 8 times Assign SUC Return Route to the second End Node:

i. The first 4 set the SUC Node ID field to 0 for erasing any possible pre-existing SUC
Return Routes.

ii. The Next 4 are the ones used for defining the current SUC Return Routes (for the
SUC Return Commands that do not match an existing Return Route the SUC Node
ID field is set to Node ID 0).


**3.37.4** **Pass** **Criteria**


1. Assign SUC Return Route Command is formatted as per Figure 4.40, it extends from the Assign
Return Route Command (NWK:010E.1).

2. The “NodeID” field shall be set to the NodeID of the SUC Node (NWK:010F.1).

3. When there is no SUC/SIS in the network, the command is not sent (NWK:0110.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 82


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.37.5** **Fail** **Criteria**


1. Assign SUC Return Route doesn’t follow the specified format nor extends from the description
for Assign Return Route Command (NWK:010E.1).

2. The “NodeID” field does not correspond to the NodeID of the SUC Node (NWK:010F.1).

3. The command is sent regardless of not having a SUC Node in the network (NWK:0110.1).

4. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 83


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.38 Command Frames – Z-Wave Protocol Command Class – NOP Power Command


This command is used to verify if a node is in direct range and used for neighbor Discovery.


**3.38.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 2 x End Nodes.


**3.38.2** **Test** **Setup**


1. Include the first End Node in direct range to the first Controller.

2. Include the second End Node one hop away from the RealPrimary Controller.

3. Place the second Controller in direct range to the first Controller and the first End Node but
one hop away from the second End Node. Include it to the network.


**3.38.3** **Test** **Result**


1. The first End Node is included in direct range.

a. When included, the Controller initiates a Neighbors range test on it.

b. The first End Node can reach the RealPrimary Controller directly with NOP Power.

2. The second End Node is included through the first End Node as a Repeater.

a. When included, the Controller initiates a Neighbors range test on it.

b. The second End Node can only reach the first End Node directly with NOP Power.

3. The second Controller is included and can’t reach directly the second End Node.

a. When included, the Controller initiates a Neighbor’s range test on it.

b. The second Controller can reach the RealPrimary Controller and first End Node directly
but can’t reach the second End Node with NOP Power.


**3.38.4** **Pass** **Criteria**


1. The NOP Power command follows the format from Table 4.59 (NWK:0122.1).

2. The “Tx Power Register” is not used and shall be set to 0x00. In case the “Tx Power Dampening”
field is missing, it should follow the value Table 4.60 (NWK:0123.1, NWK:0126.1, NWK:0124.1).

3. The “Tx Power Dampening” field is used to indicate the transmit power to use in a responding MPDU Acknowledgement frame. The “Tx Power Dampening” field follows Table 4.61
(NWK:0125.1).

4. The NOP Power command is not routed through Hops and only reaches the nodes in direct
range (NWK:0127.1).

5. The sending node shall apply the same dampening stated in the “Tx Power Dampening” field
(NWK:0128.1).

6. Nodes receiving this command respond with an MPDU Acknowledgement frame transmitted
with a Tx Power corresponding to the parameters of this command (NWK:0129.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 84


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.38.5** **Fail** **Criteria**


1. The NOP Power command doesn’t follow the specified format (NWK:0122.1).

2. The “Tx Power Register” is used in conjunction with the “Tx Power Dampening” field, or if the
“Tx Power Dampening” field is missing, it doesn’t follow Table 4.60 or it’s just not set to 0x00
(NWK:0123.1, NWK:0126.1, NWK:0124.1).

3. The “Tx Power Dampening” field doesn’t follow Table 4.61 (NWK:0125.1).

4. The NOP Power command is routed and reaches nodes in indirect range (NWK:0127.1).

5. The sending node doesn’t apply the same dampening stated in the “TX Power Dampening” field
(NWK:0128.1).

6. Nodes receiving this command in direct range don’t respond with an Acknowledgement MPDU
or without dampening it to the corresponding Tx Power (NWK:0129.1).

7. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 85


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.39 Command Frames – Z-Wave Protocol Command Class – Reserve Node IDs Command


This command is used by an Inclusion Controller to request NodeID(s) to the SUC/SIS that can be
used to add new nodes in the network.


**3.39.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 2 x End Nodes.


**3.39.2** **Test** **Setup**


1. Include the second Controller to the first one.

2. Set both End Nodes in direct range to both controllers and set them both in learning mode
simultaneously.

3. Start NWI in the RealPrimary Inclusion Controller.


**3.39.3** **Test** **Result**


1. The second Controller is included to the first one’s network.

a. The first Controller is set to RealPrimary, Inclusion.

b. The second Controller is set to SUC/SIS Controller.

2. Both End Nodes broadcast their NodeId and start emitting Explorer Frames.

3. The RealPrimary controller signalizes the SUC/SIS that it will begin starting new nodes.

a. It will request an Automatic Controller Update.

b. It will send New Node Registered to SUC/SIS.

c. It will end by sending Reserve Node ID to the SUC/SIS.

d. SUC/SIS responds with Reserved ID Command.

e. Real Primary Controller will proceed to include both End Nodes and having the same
exchange for each of them.


**3.39.4** **Pass** **Criteria**


1. Reserved Node ID follows the format from Figure 4.46, it is sent only by Inclusion Controllers
to the SUC/SIS as a singlecast (NWK:012A.1, NWK:012C.1, NWK:012D.1, NWK:012E.1).

2. The “Number of Node IDs” field shall hold only values from 0…10. It should only be set to 1 to
avoid exhausting the NodeID pool from the SIS (NWL:012B.1).

3. The SIS responds with Reserved IDs command. It should not respond when it’s received via
multicast (NWK:012F.1).

4. It is ignored by non-SIS Controller nodes in the network (NWK:0130.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 86


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.39.5** **Fail** **Criteria**


1. Reserved Node ID doesn’t follow the specified format, it’s sent by any other type of controller
to other Controller that is not SUC/SIS or it’s sent as multicast by default (NWK:012A.1,
NWK:012C.1, NWK:012D.1, NWK:012E.1).

2. The “Number of Node IDs” field can hold values above 10 or it’s set to more than 1 by default
(NWK:012B.1).

3. The SIS doesn’t respond with Reserved IDs command or it responds with it’s sent as multicast
(NWK:012F.1).

4. Non-SIS Controller nodes in the network respond to this command (NWK:0130.1).

5. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 87


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.40 Command Frames – Z-Wave Protocol Command Class – Re- served IDs Command


This command is used by an Inclusion Controller to request NodeID(s) to the SUC/SIS that can be
used to add new nodes in the network.


**3.40.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 2 x End Nodes.


**3.40.2** **Test** **Setup**


1. Include the second Controller to the first one.

2. Set both End Nodes in direct range to both controllers and set them both in learning mode
simultaneously.

3. Start NWI in the RealPrimary Inclusion Controller.


**3.40.3** **Test** **Result**


1. The second Controller is included to the first one’s network.

a. The first Controller is set to RealPrimary, Inclusion.

b. The second Controller is set to SUC/SIS Controller.

2. Both End Nodes broadcast their NodeId and start emitting Explorer Frames.

3. The RealPrimary controller signalizes the SUC/SIS that it will begin starting new nodes.

a. It will request an Automatic Controller Update.

b. It will send New Node Registered to SUC/SIS.

c. It will end by sending Reserve Node ID to the SUC/SIS.

d. SUC/SIS responds with Reserved ID Command.

e. Real Primary Controller will proceed to include both End Nodes and having the same
exchange for each of them.


**3.40.4** **Pass** **Criteria**


1. Reserved IDs follows the format from Figure 4.47, it is sent only by Controllers with SIS function
and a SIS Controller may reuse to provide Reserved NodeIDs (NWK:0131.1, NWK:0135.1,
NWK:0136.1, NWK:0137.1).

2. The “Number of IDs” field shall be in the range 0 … 10 (NWK:0132.1).

3. The “Reserved NodeID” field represents a NodeID granted that the Inclusion Controllar can
use. The length of this field shall match the value in the field “Number of IDs” (NWK:0133.1,
NWK:0134.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 88


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.40.5** **Fail** **Criteria**


1. Reserved IDs doesn’t follow the specified format, it’s sent by any other type of controller to
(NWK:0131.1, NWK:0135.1, NWK:0136.1, NWK:0137.1).

2. The “Number of IDs” field is higher than 10 (NWK:0132.1).

3. The “Reserved NodeID” field is holding NodeID values for the Inclusion Controller to grant. Its
value is not matching the value in the field “Number of IDs” (NWK:0133.1).

4. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 89


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.41 Command Frames – Z-Wave Protocol Command Class – Set NWI Mode Command


This command is used to instruct AL nodes in the network to repeat Inclusion Request Explore Frames
and Routed frames sent on foreign HomeIDs.


**3.41.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC Controller.

 - 2 x End Nodes.


**3.41.2** **Test** **Setup**


1. Include the first End Node to the Controller.

2. Place the second End Node one hop away from the Controller with the first End Node placed
as a repeater.

3. Start Network Wide Inclusion (NWI) in the Controller.

4. Set the second End Node in Learning Mode.

5. Send a singlecast to each node to verify correct communication.

6. Start Network Wide Exclusion (NWE) in the Controller.

7. Set the second End Node in learning mode.


**3.41.3** **Test** **Result**


1. The End Node is included in direct range to the Controller.

2. The second End Node is not in direct range to the Controller and the first End Node can be
used as a repeater.

3. NWI is started.

a. The Controller emits an explorer frame with command Set NWI Mode.

b. In this frame, the first byte after the Command identifier is set to 0x01.

c. Timeout is either set to 0x00 or a specific value.

4. The second End Node is included through the first End Node as a repeater.

5. Each End Node answers with an Acknowledgement frame directly or routed, respectively.

6. NWE is started.

a. The Controller emits an explorer frame with command Set NWI Mode.

b. In this frame, the first byte after the Command identifier is set to 0x00.

7. The second End Node is excluded through the first End Node as a repeater.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 90


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.41.4** **Pass** **Criteria**


1. The command follows the format from Table 4.66 (NWK:0143.1).

2. The “Mode” field set to 0x00 or 0x01 respectively enables or disables the nodes receiving the
command to stop or start repeating inclusion requests (NWK:0144.1, NWK:0145.1).

3. The Timeout value 0x00 shall indicate the node to use a default timeout of nwkNWIModeDefaultTimeout.

4. Values outside this range indicate the number of minutes to remain repeating inclusion requests
(NWK:0146.1, NWK:0147.1, NWK:0148.1).

5. This command is transmitted using a normal explorer frame (NWK:0149.1).

6. When this command is received by an AL node, it shall activate or deactivate NWI mode
depending on the “Mode” field (NWK:014A.1).


**3.41.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 91


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.42 Command Frames – Z-Wave Protocol Command Class – Exclude Request Command


This command is used by a node looking to be excluded from its current network.


**3.42.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC Controller.

 - 2 x End Nodes.


**3.42.2** **Test** **Setup**


1. Include the first End Node to the Controller.

2. Place the second End Node one hop away from the Controller with the first End Node placed
as a repeater.

3. Start Network Wide Inclusion (NWI) in the Controller.

4. Set the second End Node in Learning Mode.

5. Send a singlecast to each node to verify correct communication.

6. Start Network Wide Exclusion (NWE) in the Controller.

7. Set the second End Node in learning mode.


**3.42.3** **Test** **Reslut**


1. The End Node is included in direct range to the Controller.

2. The second End Node is not in direct range to the Controller and the first End Node can be
used as a repeater.

3. NWI is started.

4. The second End Node is included through the first End Node as a repeater.

5. Each End Node answers with an Acknowledgement frame directly or routed, respectively.

6. NWE is started.

7. The second End Node broadcasts its Node Information Frame and goes into learning mode.

a. After broadcasting its Node Information Frame, it starts emitting Exclude Request Command as Explorer Frames.

b. The Explorer Frame containing the Exclude Request command is repeated to the Controller
and it proceeds to exclusion.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 92


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.42.4** **Pass** **Criteria**


1. The format of the command follows the Table 4.67 (NWK:014B.1).

2. This command extends its fields from the Node Information Frame (NWK:014E.1).

3. This command is transmitted in a Normal Explore Frame and is broadcasted to direction 255
(NWK:014C.1, NWK:014D.1).

4. This command proceeds to exclude a node only if currently in exclusion mode, it ignores the
command, otherwise (NWK:014F.1, NWK:0150.1).


**3.42.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 93


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.43 Command Frames – Z-Wave Protocol Command Class – Assign Return Route Priority Command


This command is used to assign the priority route to a NodeID destination.


**3.43.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 3 x End Nodes (one of which can trigger associations with buttons  - Like Wall Controller).


**3.43.2** **Test** **Setup**


1. Include two End Nodes (AL1 & AL2) in direct range to the RealPrimary Controller.

2. Include the third End Node (with associations enabled by buttons  - AL3) one hop away from
the RealPrimary Controller.

3. Place the second Controller one hop away from the third End Node. Include it to the network.

4. From RealPrimary Controller send Find Nodes in Range (check - NWK:008D.1) to AL3 with the
fields set so that the “Mask Bytes” field holds all nodes except for the RealPrimary Controller
and itself: On Command Class Pane, if the Network holds Nodes {1, 2, 3, 4 & 5} type the hex
command [01 04 01 16].

a. It’s delivered over one repeater.

5. Send Get Nodes in Range to the AL3 from RealPrimary Controller. Type Hex command [01
05] in Command Class pane.

6. Send Association Set to the AL3 so that the End Node reaches out to the second Controller
when triggering the associations by pressing a button: For Wall Controller, set Association to
Node 5 on group 2.

7. Send Assign Return Route to AL3.

a. Set the values of the fields so that the End Node reaches the second Controller though the
first repeater: Send hex [01 0C 05 01 02 20].

8. Send Assign Return Route to the third End Node.

a. Set the values of the fields so that the End Node reaches the second Controller though the
other repeater: Send hex [01 0C 05 11 03 20].

9. Send Assign Return Route Priority to the third End Node so that it used the second Route set:
Send hex [01 24 05 01].

10. Activate the association by pressing the corresponding button.

11. Send Assign Return Route Priority to the AL3 so that it used a Route that doesn’t exist: Send
hex [01 24 05 09].

12. Activate the association by pressing the corresponding button.

13. Disable the AL2. Activate the association again.

14. From the RealPrimary Controller send Assign Return Route to the second Controller.

a. Set the values of the fields so that it reaches the third End Node through the RealPrimary
Controller: Send Hex [01 0C 04 01 01 20].

15. Send Assign Return Route Priority to the second Controller to reach AL3 as the just set route:
Send hex [01 24 04 00].

16. Send a command from the second Controller to the Third End Node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 94


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.43.3** **Test** **Result**


1. AL1 & AL3 are in direct range to the RealPrimary Controller.

a. RealPrimary Controller is also set to SUC/SIS Controller.

2. AL3 is included using one of the other two End Nodes as repeaters.

3. The second Controller is included as an Inclusion Controller. It can reach AL3 through one
repeater.

4. AL3 performs a Neighbors Range Test in the nodes specified in the command.

5. AL3 responds with Node Range Info.

6. The association is set between AL3 and the second Controller.

7. Assign Return Route is sent with the AL1 set to be used as repeater between the AL3 and the
second Controller.

8. Assign Return Route is sent with AL2 set to be used as repeater between AL3 and the second
Controller instead of the AL1.

9. Assign Return Route Priority is sent setting the second route.

10. The association is activated, and AL3 reaches the second Controller through the route established
by Assign Return Route Priority Command.

11. Assign Return Route Priority is sent setting the 9th route instead of the first one.

12. The association is activated, and the AL3 the second Controller through the route established
by the previous Assign Return Route Priority Command, since the 9th Route does not exist.

13. The association is activated, and the AL3 tries reaching the second Controller through the route
established by Assign Return Route Priority Command. When it fails, it tries the other route.

14. The second Controller has return route set to AL3 go through the RealPrimary Controller.

15. The second Controller receives Assign Return Route Priority set to the route of the previous
command.

16. The second Controller tries reaching AL3 regardless of the priority route.


**3.43.4** **Pass** **Criteria**


1. The Assign Return Route Priority Command follows the format from Table 4.68 (NWK:0151.1).

2. The “Route Number” field is used to define the number of the route to set as the priority one
(NWK:0152.1).

3. The Route Number should exist and must have been issued by the same Controller sending this
command. An End Node does not send this command (NWK:0153.1, NWK:0154.1).

4. When the command is received, the End Node updates its priority route table, it must ignore
it if the route specified does not exist. A Controller receiving this command shall ignore it.
The route defined as priority shall be the first routing option when transmitting (NWK:0155.1,
NWK:0156.1, NWK:0157.1, NWK:0158.1, NWK:017D.1, NWK:017E.1).

5. The Priority Route that was set is attempted to be used before trying the other routes
(NWK:017F.1).

6. Controller nodes may ignore priority routes and use the route of their choice on the first transmission attempt (NWK:017E.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 95


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.43.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 96


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.44 Command Frames – Z-Wave Protocol Command Class – Assign SUC Return Route Priority Command


This command is used to assign the priority Route to the SUC.


**3.44.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 3 x End Nodes (one of which can trigger associations with buttons  - Like Wall Controller).


**3.44.2** **Test** **Setup**


1. Include two End Nodes (AL1 & AL2) in direct range to the RealPrimary Controller.

2. Include the third End Node (with associations enabled by buttons  - AL3) one hop away from
the RealPrimary Controller.

3. Include the second Controller to the network. After inclusion: Place it one hop away from the
third End Node.

4. From RealPrimary Controller send Find Nodes In Range (check - NWK:008D.1) to AL3 with the
fields set so that the “Mask Bytes” field holds all nodes except for the RealPrimary Controller
and itself: On Command Class Pane, if the Network holds Nodes {1, 2, 3, 4 & 5} type the hex
command [01 04 01 16].

a. It’s delivered over one repeater.

5. Send Get Nodes in Range to AL3 from RealPrimary Controller. Type Hex command [01 05] in
Command Class pane.

6. Send Association Set to AL3 so that it reaches out to the SUC/SIS Controller when triggering
the associations by pressing a button. For Wall Controller, set Association to Node 1 on group
2.

7. Send Assign SUC Return Route to AL3.

a. Set the values of the fields so that it reaches the SUC/SIS Controller though the first
repeater AL1: Send hex [01 14 01 11 02 20].

8. Send Assign SUC Return Route to AL3 using the second repeater AL2:

a. Set the values of the fields so that it reaches the SUC/SIS Controller through the other
repeater: Send hex [01 14 01 21 03 20].

9. Activate the association by pressing the corresponding button.

10. Send Assign SUC Return Route Priority to AL3 using the second return route:

a. Send hex [01 25 01 02].

11. Activate the association by pressing the corresponding button.

12. Send Assign SUC Return Route Priority to AL3 using a non-existent return route:

a. Send hex [01 25 01 06]

13. Activate the association by pressing the corresponding button.

14. From the RealPrimary Controller send Assign SUC Return Route to the second Controller.

a. Set the values of the fields so that it reaches the SIS Node through the first repeater AL1:
Send Hex [01 14 01 11 02 20].

15. Send Assign SUC Return Route Priority to the second Controller to reach the SIS Node as the
just sent route: Send Hex [01 25 01 01].


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 97


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


16. Send a command from the second Controller to the SIS Node.


**3.44.3** **Test** **Result**


1. AL1 & AL2 are in direct range to the RealPrimary Controller.

a. RealPrimary Controller is also set to SUC/SIS Controller.

2. AL3 is included using one of the other two End Nodes as repeaters.

a. Look at the inclusion trace and observe that there are a number of Assign SUC Return
Route frames sent at the end of the inclusion.

3. The second Controller is included as an Inclusion Controller. It can reach AL3 through one
repeater.

4. AL3 performs a Neighbors Range Test in the nodes specified in the command.

5. AL3 responds with Node Range Info.

6. The association is set between AL3 and the SUC/SIS Controller.

7. Assign SUC Return Route is sent with the selected repeater set to be used between AL3 and
the SUC/SIS Controller.

8. Assign SUC Return Route is sent with the selected repeater set to be used between AL3 and
the SUC/SIS Controller.

9. The association is activated, and AL3 reaches the SUC/SIS Controller through one of the routes.

10. Assign SUC Return Route Priority is sent setting the 2nd route.

11. The association is activated, and AL3 reaches the SUC/SIS Controller through the 2nd route.

12. Assign SUC Return Route Priority is sent setting the 2nd route.

13. The association is activated, and AL3 reaches the SUC/SIS Controller through the 2nd route,
ignoring the previous Assign SUC Return Route Priority.

14. The second Controller receives SUC Return Route set to the SIS Node through the AL1.

15. The second Controller receives Assign SUC Return Route set to the route of the previous
command.

16. The second Controller tries reaching the SIS Node directly regardless of the priority route.


**3.44.4** **Pass** **Criteria**


1. The Assign SUC Return Route Priority Command follows the format from Table 4.69 It extends
from the Assign Return Route Priority Command (NWK:0161.1).

2. The Return SUC Route Number should exist and must have been issued by the same Controller
sending this command. The NodeID field is the NodeID of the SUC/SIS. An End Node does
not send this command (NWK:0159.1, NWK:015A.1, NWK:015B.1).

3. When the command is received, the End Node updates its priority route to the SUC, it must
ignore it if the route specified does not exist. A Controller receiving this command shall ignore it.
The route defined as priority should be the first routing option to the SUC/SIS (NWK:015C.1,
NWK:015D.1, NWK:015E.1, NWK:015F.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 98


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.44.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 99


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.45 Command Frames – Z-Wave Protocol Command Class – Smart- Start Included Node Information Command


This command is used by nodes to notify a controller that it was just powered up and is already part
of a network.


**3.45.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 1 x End Node.


**3.45.2** **Test** **Setup**


1. Add the DSK number of the End Node to the first Controller. Let SmartStart inclusion of the
End Node to finish.

2. Remove power from the End Node.

3. Add the DSK number of the End Node to the second Controller.

4. Return power to the End Node.


**3.45.3** **Test** **Result**


1. The End Node is included to the first Controller’s network.

2. The End Node is powered down.

3. The second Controller holds the DSK of the End Node in its Provisioning List.

4. The End Node is powered up and emits an explorer frame with the Included Node Info Command.

a. The second Controller does not attempt including the End Node.


**3.45.4** **Pass** **Criteria**


1. The SmartStart Included Node Information command follows the format from Table 4.70
(NWK:0160.1).

2. The “NWI HomeID” field identifies that the Node has been included to the network with that
HomeID (NWK:0163.1).

3. The format of the bytes forming the “NWI HomeID” field is structured to match bytes 9 … 12 of
the S2 DSK. Bits 7 & 6 of the “NWI HomeID 1” field are set to 1. Bit 0 of the “NWI HomeID
4” field is set to 0   - Illustrated by Figure 4.11 (NWK:0164.1, NWK:0165.1, NWK:0166.1).

4. This frame is transmitted in an Inclusion Explorer Frame and it’s broadcasted to NodeID 0xFF
(NWK:0167.1, NWK:0168.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 100


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.45.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 101


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.46 Command Frames – Z-Wave Protocol Command Class – Smart- Start Prime Command


This command is used to notify SmartStart including controllers that a node is about to make an
inclusion request.


**3.46.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC Controller.

 - 1 x AL End Node.

 - 1 x FL End Node.

 - 1 x NL End Node.


**3.46.2** **Test** **Setup**


1. Introduce the DSK value of the End Nodes into the Controller’s Provisioning List.

2. Power up the End Nodes.


**3.46.3** **Test** **Result**


1. The DSK of the End Nodes is in the Controller’s Provisioning List.

2. The End Nodes each issue a SmartStart Prime Command.

a. AL & FL nodes wait until their wakeup period is completed and then they send SmartStart
Prime Command after nwkSmartStartInclusionRequestDuration has passed.


**3.46.4** **Pass** **Criteria**


1. The format of the SmartStart Prime Command follows the format from Table 4.71 and it extends
from the Node Information Frame (NWK:0169.1, NWK:016A.1).

2. This command is sent in an inclusion explorer frame, it must be addressed as a multicast to
node 0xFF. Must hold the NWIHomeID as HomeID. It is sent after nwkSmartStartInclusionRequestDuration has passed. Non-AL nodes may return to sleep between sending SmartStart
Prime Command and SmartStart Inclusion Request Command (NWK:016B.1, NWK:016C.1,
NWK:016D.1, NWK:016E.1).

3. When it’s received, the Controller compares the NWIHomeID to the one obtained in the DSK
keys in its Provisioning List. When finding a match, the Controller enters SmartStart Inclusion
when the node issues a SmartStart Inclusion Request. IF there are more DSK matches for the
received NWIHomeID, the Controller shall enter SmartStart Inclusion alternating between the
DSK candidates (NWK:016F.1, NWK:0170.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 102


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.46.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 103


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.47 Command Frames – Z-Wave Protocol Command Class – Smart- Start Inclusion Request Command


This command is used to request to initiate a SmartStart inclusion.


**3.47.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC Controller.

 - 1 x AL End Node.

 - 1 x FL End Node.

 - 1 x NL End Node.


**3.47.2** **Test** **Setup**


1. Introduce the DSK value of the End Nodes into the Controller’s Provisioning List.

2. Power up the End Nodes.


**3.47.3** **Test** **Result**


1. The DSK of the End Nodes is in the Controller’s Provisioning List.

2. The End Nodes each issue a SmartStart Prime Command.

a. AL & FL nodes wait until their wakeup period is completed and then they send SmartStart
Prime Command after nwkSmartStartInclusionRequestDuration has passed.

3. After the End Nodes have issued SmartStart Prime, they issue SmartStart Inclusion Request.

a. When the Controller receives SmartStart Inclusion Request, it start SmartStart inclusion
by issuing Assign Id.


**3.47.4** **Pass** **Criteria**


1. The format of the SmartStart Inclusion Request Command follows the format from Table 4.72
and it extends from the Node Information Frame (NWK:0171.1, NWK:0172.1).

2. This command is sent in an inclusion explorer frame, it must be addressed as a multicast to
node 0xFF. Must hold the NWIHomeID as HomeID. The Sending node shall listen and accept
Assign IDs Command after the HomeID has been authenticated (NWK:0173.1, NWK:0174.1,
NWK:0175.1).

3. When it’s received, the Controller compares the NWIHomeID to the one obtained in the DSK
keys in its Provisioning List. When finding a match the Controller begins SmartStart Inclusion
by issuing AssignID and it should authenticate the HomeID by constructing the 4 bytes of
NWIHomeID matching bytes 13 … 16 of the DSK, in its bits 7 & 6 of the Auth HomeID byte 1
are set to 1 and bit 0 of Auth HomeID byte 4 is set to 0 as per Figure 4.12 (NWK:0176.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 104


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.47.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 105


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.48 Functional Description – Routing – Assigning Return Routes


Return routes provide options for one node to reach another one. They are assigned on application
level.


**3.48.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 4 x End Nodes (one of which can trigger associations with buttons).


**3.48.2** **Test** **Setup**


1. Include the second Controller to the first one.

2. Place the first End Node (AL1) within reach of both SUC/SIS and the RealPrimary Controller.
Include it to the Network with the RealPRimary Controller.

3. Place the second End Node (AL2) one hop away from the RealPrimary Controller but in direct
range to the SUC/SIS Controller. Include AL2 with the SUC/SIS Controller.

4. Place the third End Node (AL3) outside reach of the SUC/SIS but direct range to the RealPrimary Controller. Include AL3 using the RealPrimary.

5. Include the fourth End Node with associations (triggered by buttons  - AL4) in direct range to
the SUC/SIS and one hop away from the RealPrimary Controller.

6. On the SUC/SIS Controller, enable “assign return routes” create an association from AL2 to
the AL2.

7. On the SUC/SIS Controller, disable “assign return routes” create an association from AL4 to
AL3.

8. Disable power in AL3.

9. Activate the association in AL4 by pressing the corresponding button.


**3.48.3** **Test** **Result**


1. The first Controller is set as RealPrimary and the second one as SUC/SIS Controller.

2. AL1 is within range of both Controllers. It’s included to the network and it’s featured in both
Controller’s Node lists.

3. AL2 is included by the SUC/SIS Controller and it’s not in direct range to the first Controller.

4. AL3 is included in over repeaters to the RealPrimary Controller and the SUC/SIS.

5. AL4 is included in direct range to the SUC/SIS and one hop away from the RealPrimary.

6. The association is set between AL4 and AL2 including return routes.

7. The association is set between AL4 and AL3 without return routes.

8. AL3 is disabled.

9. AL4 enables its associations.

a. AL4 reaches AL2 through the Route established.

b. AL4 tries reaching AL3 directly.

c. When it can’t reach AL3, it will issue Explorer frames trying to reach out to it.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 106


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.48.4** **Pass** **Criteria**


1. The Controller assigns the return routes between different End Nodes and Assign SUC Return
Route during Inclusion (NWK:0179.1).

2. The return routes are assigned by the Application Layer (NWK:017A.1).

3. There are 4 return routes assigned if possible (NWK:017B.1).

4. When there is no return route assigned, the End Node tries reaching directly. Then try by using
Explorer Frame if Direct transmission fails or request a static route from the SUC (NWK:017C.1,
NWK:0184.1).

5. AL nodes repeat Routed NPDUs on their HomeID, if their NodeID is in the repeater list
(NWK:0186.1).

6. AL Nodes repeat Normal Explore Frames in their HomeID (NWK:0187.1).

7. AL Nodes repeat Search Result Explore Frames sent on their HomeID, if their NodeID is in the
repeater list    - This is dependent from the type of routes assigned (NWK:0188.1).


**3.48.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 107


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.49 Functional Description – Network Inclusion & Formation, NWI, Learn Mode


Functional description of Network Wide inclusion, routing and Learn Mode.


**3.49.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 3 x AL End Nodes.

 - 1 x FL End Node.

 - 1 x NL End Node.


**3.49.2** **Test** **Setup**


1. Include the second Controller to the first one.

2. Set the first End Node (AL1) in learning mode. Let it time-out until it’s no longer in Inclusion
Mode.

3. Set it once more in learning mode.

4. Include AL1 to the network with the SUC/SIS Controller.

5. From SUC/SIC controller send Request Node Info to AL1.

6. Place the NL End Node in direct range to the SUC/SIS Controller. Set the NL End Node in
learning mode.

7. Start NWI in SUC/SIS Controller.

a. The SUC/SIS Controller sets AL1 in NWI mode

8. Remove power AL1. Set the SUC/SIS Controller in NWI.

9. Set the FL End Node one hop away from the SUC/SIS Controller. Set the FL End Node in
learning mode while the SUC/SIS Controller is in NWI mode.

10. Get the FL End Node in direct range to the SUC/SIS Controller and set it in learning mode
while the SUC/SIS Controller is in NWI mode.

11. Place the second AL End Node (AL2) one hop away from the SUC/SIS Controller. Set it in
learning mode while the SUC/SIS Controller is in NWI mode.

12. Enable power in AL1 in direct range to the SUC/SIS Controller.

13. Place the third AL End Node (the one with associations triggered by buttons  - AL3) in direct
range to AL2 (one hop away from the SUC/SIS). Set it in learning mode.


**3.49.3** **Test** **Result**


1. The first Controller is set as RealPrimary. The second one is set as SUC/SIS Controller.

2. AL1 is set in learning mode. No inclusion begins. The End Node waits for Transfer Presentation
to join a network. It eventually stops requesting being included (it lasts nwkLearnModeNetworkWideMinDuration ).

a. Its HomeID is set to a random value: It doesn’t assume any other network’s Home ID, nor
it starts its own by setting its Node ID to other than 0x00, just waiting to be included to
a network.

3. AL1 is in learning mode again.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 108


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


4. AL1 is included. The RealPrimary Controller doesn’t hold information of AL1 on its Node List.

5. AL1 answers with a Node Information frame as singlecast.

6. The NL End Node is set in learning mode.

a. It sends explorer frames requesting inclusion that are not repeated.

7. The SUC/SIS Controller includes directly the NL End Node.

a. The SUC/SIS controller is transmitting Transfer Presentation frames.

b. AL1 doesn’t repeat the inclusion frames.

8. The SUC/SIS Controller doesn’t set the NL End Node into NWI mode.

9. The FL End Node is not included, as the first End Node is not working, and the NL End Node
doesn’t repeat the frames.

10. The FL End Node is included in direct range by the SUC/SIS Controller.

11. AL2 is not included since AL1 is not active and neither NL nor FL End Nodes repeat frames.

12. The SUC/SIS sets AL1 in NWI mode and includes AL2.

13. It is included by NWI by the repeaters.


**3.49.4** **Pass** **Criteria**


1. AL nodes repeat frames on a foreign HomeID when their NodeID has been included in the
“Repeater List” in the Set NWI Mode command (NWK:0189.1).

2. AL nodes set in NWI repeat Inclusion Request Explorer Frames (NWK:018A.1).

3. AL nodes do not repeat Inclusion Request Nodes (Explorer Autoinclusion) when NWI is disabled
or the HomeID is different from 0x00000000 (NWK:018B.1).

4. FL & NL nodes do not repeat Routed and Explore NDPUs (NWK:018C.1).

5. Z-Wave Nodes can go into Learning Mode (NWK:0195.1).

6. Learn Mode only lasts during the time it’s needed (NWK:0196.1).

7. Nodes may enter Learn Mode to join or leave a network (NWK:0197.1).

8. Node scan accept Assign ID Commands when they are trying to join a network (NWK:0198.1).

9. A secondary Controller may also enter Learn Mode Inclusion to receive the Network Topology
(NWK:0199.1).

10. A node that enters Learn mode for Classic Inclusion/Exclusion shall remain in learn mode for
at least nwkLearnModeMinDuration (NWK:019A.1).

11. A node that enters Learn mode for Network Wide Incluson/Exclusion shall remain in Learn
mode for at least nwkLearnModeNetworkWideMinDuration (NWK:019B.1).

12. End Node shall not start a new network and wait until they are included by a controller. When
not in a network they assign themselves an HomeID (aNwkRandomHomeID) (NWK:019C.1).

13. Nodes included in direct range follow classic inclusion as in Figure 4.21 (NWK:019E.1).

14. Nodes in learn mode, wait for a Transfer Presentation and validate the value in the “Option”
field and issue a Node Information Frame Command to the Controller’s NodeID (NWK:019F.1).

15. IT may be ignored sending a Node Information Frame Command addressed to the broadcast
destination NodeID (NWK:01A0.1).

16. The Including Controller issue Assign ID command using the NodeId and HomeID used by the
joining node, even if they are outside of the valid NodeID range (NWK:01A1.1).

17. The Neighbor Discovery step (passing Criteria 13) follows the description in Figure 4.45
(NWK:01A2.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 109


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


18. Joining nodes may use NodeID 0xEF (NWK:01A3.1).

19. Learning mode is disabled at the end of inclusion in a Joining Node when it issues Range Info
Command (NWK:01A4.1).

20. Node Information Frame issued by joining nodes doesn’t request Acknowledgement frames
(NWK:01A5.1).

21. Classic inclusion is considered complete by a Controller when it issues SUC NodeID or SUC
Return Route (NWK:01A6.1).

22. NWI should be used as the default Learn mode (NWK:01A7.1).

23. When the Controller enters NWI it issues Set NWI Mode in a normal explorer frame
(NWK:01A8.1).

24. Network Wide Inclusion follows Figure 4.22 (NWK:01A9.1).

25. When a Node receives NWI learn mode, it issues Node Information Frame Command in an
Inclusion Request Explore Frame, it has the Acknowledgement Request set to 1 (NWK:01AA.1).

26. Controllers in NWI add mode set the “Option” field to 0x05 in the Transfer Presentation Command (NWK:01AB.1).

27. Acknowledgement frames must be routed using the same route during inclusion as the commands
they follow (NWK:01AC.1).

28. Neighbor discovery for NWI follows Figure 4.45 (NWK:01AD.1).


**3.49.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 110


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.50 Functional Description – Unsuccessful Routed frame without Routed Error


Functional description of failed routing.


**3.50.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 3 x End Nodes (one of which can trigger associations with buttons).

 - 1 x FL End Node.

 - 1 x NL End Node.


**3.50.2** **Test** **Setup**


1. Include the second Controller to the first one.

2. Include the first End Node (AL1) to the network with the SUC/SIS Controller.

3. Include the NL End Node in direct range to the SUC/SIS Controller

4. Set the FL End Node in direct range to the SUC/SIS Controller and set it in learning mode
while the SUC/SIS Controller is in NWI mode.

5. Place the second AL End Node (AL2) one hop away from the SUC/SIS Controller. Set it in
learning mode while the SUC/SIS Controller is in NWI mode.

6. Place the third AL End Node (the one with associations triggered by buttons  - AL3) in direct
range to the AL2 (one hop away from the SUC/SIS). Set it in learning mode.

7. Stop NWI mode in SUC/SIS.

8. On the RealPrimary Controller press the “Update” Button.

9. From SUC/SIS send a singlecast to the AL3 included by NWI.

10. Activate the Lifeline Notification in the AL3 by pressing Button 0.

11. Remove power from the SUC/SIS. Activate Lifeline Notification in the AL3 again.

12. Power Back the SUC/SIS.

13. From SUC/SIS set an association to AL3 so that it reaches RealPrimary Controller when the
association is activated with one of its buttons.

14. Remove power from the RealPrimary Controller.

15. Activate the Association in the AL3.

16. Return power to the RealPrimary Controller. Activate the association once more.

17. Activate the Association once more.

18. Remove power from AL1 & AL2. Activate the association once more.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 111


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.50.3** **Test** **Result**


1. The first Controller is set as RealPrimary. The second one is set as SUC/SIS Controller.

2. The AL1 is included. The RealPrimary Controller doesn’t hold information of the AL1 on its
Node List.

3. The SUC/SIS Controller directly includes the NL End Node.

4. The FL End Node is included in direct range by the SUC/SIS Controller.

5. The SUC/SIS sets the first End Node in NWI mode and includes the AL2 through repeaters.

6. It is included by NWI by the repeaters.

a. SUC/SIS sets up lifeline association at the end of the NWI.

7. NWI mode is stopped in the SUC/SIS.

8. The RealPrimary Controller requests an automatic update from the SUC/SIS.

a. The SUC/SIS performs a network update to RealPrimary Controller.

9. SUC/SIS reaches AL3 through one repeater.

10. Lifeline notification reaches the SUC/SIS through repeaters.

11. The AL3 tries reaching the SUC/SIS but it can’t.

a. AL3 receives a Routing Error frame.

12. The SUC/SIS is powered up.

13. The association is set from AL3 to the RealPrimary Controller.

14. The RealPrimary Controller is powered down.

15. The AL3 sends Lifeline Notification to the SUC/SIS through repeaters first and then it tries
reaching directly the Real Primary Controller.

a. AL3 can’t reach it and emits an explorer frame.

b. AL2 End Node repeats the explorer frame

16. The Real Primary controller is Powered Up again. AL3 sends Central Scene notification to the
SUC/SIS and tries reaching the Real Primary Controller with Nonce Get or Supervision Get
{Basic Set} then it tries with direct frames but it can’t reach the RealPrimary Controller.

a. The AL3 sends explorer frames reaching for the RealPrimary Controller. The explorer
frame is repeated by the first repeater and then by the nodes in reach of the first repeater:
in ‘Properties 5’ observe the ‘Repeater’ fields change in each new Explorer Frame.

b. The explorer frames reach the Real Primary Controller and it returns an Explorer Search
Result frame.

17. The AL3 reaches Real Primary Controller with routed frames from the beginning.

18. The last repeater has its power removed.

a. AL3 doesn’t receive a routed Acknowledgement frame.

b. AL3 times out and retries once routing its singlecast to the RealPrimary Controller.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 112


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.50.4** **Pass** **Criteria**


1. Sending nodes timeout after aNwkRoutedAckTimeout when Routed Acknowledgement or
Routed Error frames are not received (NWK:0191.1).

2. AL nodes in the same network repeat the first Normal Explorer Frames (NWK:0192.1).

3. Explore Frames are repeated like in Figures 4.65 & 4.66. Nodes in direct range are the first to
repeat them (NWK:0193.1).

4. Search result Explore Frames are returned using the same route that reached them
(NWK:0194.1).


**3.50.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 113


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.51 Functional Description – Network Exclusion, NWE, Removing Failing Nodes


Functional description of Exclusion, Network Wide Exclusion and Failing Nodes.


**3.51.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 3 x End Nodes (one of which can trigger associations with buttons).

 - 1 x FL End Node.

 - 1 x NL End Node.


**3.51.2** **Test** **Setup**


1. Include the second Controller to the first one.

2. Include the first End Node (AL1) to the network with the SUC/SIS Controller.

3. Include the NL End Node in direct range to the SUC/SIS Controller.

4. Configure the NL End Node to wake up every 20  - 30 seconds, so that SUC/SIS Controller can
track soon when it goes off-line.

5. Set the FL End Node in direct range to the SUC/SIS Controller and set it in learning mode
while the SUC/SIS Controller is in NWI mode.

6. Place the second AL End Node (AL2) one hop away from the SUC/SIS Controller. Set it in
learning mode while the SUC/SIS Controller is in NWI mode.

7. Place the third AL End Node (the one with associations triggered by buttons  - AL3) in direct
range to AL2 (one hop away from the SUC/SIS). Set it in learning mode.

8. Start Network Wide Exclusion in the SUC/SIS Controller.

9. Set AL3 in learning mode.

10. Exclude the FL End Node from the network with SUC/SIS.

11. Set the RealPRimary Controller in Learning Mode.

12. Stop NWE in the SUC/SIS.

13. Place the recently removed Controller in direct range to the first and second End Nodes.

14. Start Exclusion mode in the recently removed Controller.

15. Set AL2 in Learning Mode.

16. Set the NL End Node in Learning Mode. Exclude it with the Independent Controller.

17. On the SUC/SIS Probe AL2 removed to verify if it is failing.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 114


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.51.3** **Test** **Result**


1. The first Controller is set as RealPrimary. The second one is set as SUC/SIS Controller.

2. AL1 is included. The RealPrimary Controller doesn’t hold information of AL1 on its Node List.

3. The SUC/SIS Controller directly includes the NL End Node.

4. The NL End Node is set to wake up every 20-30 seconds.

a. It sends Wake Up notifications periodically.

5. The FL End Node is included in direct range by the SUC/SIS Controller.

6. The SUC/SIS sets AL1 in NWI mode and includes AL2.

7. It is included by NWI by the repeaters.

8. The Controller sets the network in Network Wide Exclusion.

a. It starts broadcasting Transfer Presentation commands.

9. The SUC/SIS removes AL3 from the network through repeaters.

10. The FL End Node is removed from the network in direct range.

11. The RealPrimary Controller is removed from the network by the SUC/SIS.

a. Exclusion ends with Transfer End.

12. NWE is stopped.

13. The first Controller has AL1 and AL2 in direct Range.

14. The Controller begins broadcasting Transfer Presentation.

15. The Controller removes AL2 from the Network.

a. The Controller sends to AL2 assign NodeID with value 0x00 and HomeID = 0x00000000.

16. The NL End Node is removed from the network by the removed Controller.

17. The SUC/SIS verifies that the node doesn’t respond and can be considered failing.


**3.51.4** **Pass** **Criteria**


1. When a Controller is not in a network it starts its own assigning themselves HomeID and NodeId
(aNwkRandomHomeID), set itself as Primary Controller and/or SUC/SIS (NWK:019D.1).

2. Classic exclusion is performed in direct range only (NWK:01BF1.1).

3. Classic exclusion follows Figure 4.29 (NWK:01C0.1).

4. A Node being excluded in learn Mode waits for Transfer Presentation with the “Option” field indicating exclusion, to which the Node responds with a Node information Frame to the Controller
(NWK:01C1.1).

5. The Node may ignore Transfer Presentation and issue Node Information Command to the broadcast destination (NWK:01C2.1).

6. Node Information command issued by leaving nodes Doesn’t request Acknowledgement frame
(NWK:01C3.1).

7. End Nodes excluded assume NodeID 0x00 and random HomeID (aNwkRandomHomeID). Controller nodes excluded start a new network (NWK:01C6.1).

8. A Controller in exclusion mode also removes nodes in a different network (NWK:01C7.1).

9. Controller in exclusion mode shall send Assign ID command in its own HomeID if it detects a
Node Information Frame (NWK:01C8.1).

10. A node in Learn Mode looking for exclusion accepts Assign ID Commands issued in a different
HomeID (NWK:01C9.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 115


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


11. Network Wide Exclusion follows Figure 4.31 (NWK:01CA.1).

12. When a node doesn’t respond it may be identified as failing (NWK:01CB.1).

13. It’s possible to remove non-responsive nodes from the Node List by Remove Failed Node
(NWK:01CD.1).

14. Before removing a non-responsive Node from the Node List, the Controller issues NOP frames
to it (NWK:01CE.1).

15. A responding node can only be removed by Classic exclusion or Network Wide Exclusion
(NWK:01CF.1).

16. A failing Node will be removed following Figure 4.32 (NWK:01D0.1).


**3.51.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 116


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.52 Functional Description – Smart Start


SmartStart allows for an automatic inclusion if the user holds the DSK number of the device.


**3.52.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 3 x End Nodes


**3.52.2** **Test** **Setup**


1. On the first Controller press “Set As SIS” so it becomes SUC/SIS and RealPrimary Controller.

2. Include the second Controller to the first one.

3. Make sure the first AL End Node (AL1) is not transmitting “Inclusion Request” frames (remove
power).

4. Place AL1 in direct range to both Controllers.

5. Introduce the DSK of AL1 in the Secondary Inclusion Controller’s Provisioning List. Reset/Power cycle/power up AL1 so that it starts requesting Smart Start inclusion.

6. Remove the DSK of AL1 from the Inclusion Controller. Press the Learning Mode button on
AL1 as soon as it’s powered up/reset.

a. Add the DSK of AL1 to the RealPrimary Controller.

b. Wait until it stops emitting Classic Inclusion requests.

7. Take the second End Node (AL2) and place it one hop away from the RealPrimary Controller.
Introduce its DSK in the Real Primary Controller.

8. Create a separate network including the DSK of the third End Node (AL3) in the third Controller.

9. Power down the AL3. Include its DSK in the RealPrimary Controller of the first network.

10. Power Up AL3. It emits a single SmartStart Included Node Information frame.

11. On the RealPrimary Controller set S2 Nonce Get to be sent within 15 seconds delay.

12. Remove the DSK of AL3 from the third Controller. Exclude it from its network. Remove power
from the AL3 .

13. Power up AL3, it starts emitting Smart Start Prime and SmartStart Include.


**3.52.3** **Test** **Result**


1. The first Controller becomes SUC/SIS and RealPrimary Controller.

2. The Controller is included and set as Secondary Inclusion Controller.

3. AL1 is not transmitting “Inclusion Request” frames.

4. AL1 is in direct reach for both Controllers.

5. The Secondary Inclusion Controller doesn’t include the End Node.

6. During the periodAL1 is in Classic Learning Mode it doesn’t emit SmartStart inclusion requests.
Once it finishes it begins requesting SmartStart inclusion again.

a. AL1 is included via SmartStart to the RealPrimary Controller.

7. RealPrimary Controller includes AL1 via SmartStart through repeaters.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 117


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


8. The third Controller broadcasts Set NWI Mode as soon as the DSK is included in its Provisioning
List. It includes AL3 via SmartStart.

9. The RealPrimary Controller holds the DSK of AL3 as well. It broadcasts a Set NWI Mode command, followed by AL1 and the secondary Controller (see on the Explorer frames the Repeater
0 field in “properties 5”).

10. The first Controller doesn’t try to include AL3 until its NodeID is reset.

11. The RealPrimary Controller sets S2 Nonce Get to be delayed 15s during inclusion.

12. The DSK of AL3 is removed and it’s removed from the third Controller’s network. AL3 is
powered down.

13. The RealPrimary Controller begins trying to include AL3.

a. S2 Inclusion fails.

b. AL3 self-resets.

c. SmartStart inclusion is attempted once again.


**3.52.4** **Pass** **Criteria**


1. SmartStart supporting nodes go into SmartStart Learn Mode right as they are powered up
(NWK:01AE.1).

2. After powering up, node shall initiate SmartStart inclusion depending on their state
(NWK:01AF.1).

3. When a node is not part of a network, it shall issue SmartStart Inclusion Request in intervals
(NWK:01B0.1).

4. SmartStart Inclusion request follows Figure 4.23 (NWK:01B1.1).

5. Nodes in Classic Inclusion or NWI Learn Mode stop issuing SmartStart inclusion requests until
they return to SmartStart Learn Mode (NWK:01B2.1).

6. Nodes requesting SmartStart Inclusion do so as per Table 4.75 (NWK:01B3.1).

7. A node already included in a network sends a single SmartStart Included node Information upon
power up as per Figure 4.24 (NWK:01B4.1).

8. A Controller shall be Primary Controller in order to include nodes via SmartStart. Secondary
and Inclusion Controllers can’t (NWK:01B5.1).

9. A Controller needs the DSK of a node to include it via SmartStart (NWK:01B6.1).

10. A Controller remains in SmartStart Inclusion mode for no less than nwkMinNWIModeSmartStartDuration minutes as per Figure 4.25 (NWK:01B7.1).

11. A Controller including via SmartStart shall perform S2 bootstrapping (NWK:01B8.1).

12. Direct Smart Start inclusion follows Figure 4.26. SmartStart inclusion through repeaters follows
Figure 4.27 (NWK:01B9.1).

13. Routing during SmartStart does the same as NWI when Assigning IDs Commands and routing
Acknowledgement frames back: Same new HomeID but the previous NodeID (NWK:01BA.1).

14. Neighbor Discovery follows Figure 4.45 (NWK:01BB.1).

15. When S2 bootstrapping fails, SmartStart Inclusion is considered failed (NWK:01BC.1).

16. A node that fails being included, leaves the network and considers itself not included to any
network (NWK:01BD.2).

17. A Controller that fails including a node, should consider the joining node removed from the
network. It may verify by issuing NOP commands (NWK:01BE.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 118


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.52.5** **Fail** **Criteria**


1. Any of the passing Criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 119


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.53 Functional Description – Controller Roles and Network Opera- tions


Controllers can change roles in a network following different procedures.


**3.53.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 2 x AL End Nodes.

 - 1 x FL End Node.


**3.53.2** **Test** **Setup**


1. Take two regular controllers. Set the first controller to be SUC/SIS. Include the second regular
Controller.

2. Reset both Controllers.

3. On the first one disable “Automatically Set as SIS”, include the second Controller to the first
one.

4. Reset both Controllers.

5. Take two regular controllers. Include the second Controller to the first one.

6. Include FL End Node to the Network with the RealPrimary Controller.

7. Include the first AL End Node to the Network using SUC/SIS Controller directly.

8. On the Third Controller, as a separate network, include the second AL End Node.

9. On the Primary Controller of the first network, start exclusion. Set the second AL End Node
(included to the third Controller) in Learning Mode.

10. Reset the Third Controller’s Network.

11. Set the SUC/SIS in inclusion Mode. Set the third Controller in Learning Mode.

12. On the Third Controller select the RealPrimary Controller and find the button “Set as SIS”.


**3.53.3** **Test** **Result**


1. During inclusion SUC/SIS issues a SUC NodeID command to the new Controller

2. Both Controllers are reset and set the NodeID to 1 and HomeID to random.

3. The Including Controller is set as RealPrimary Controller, the included Controller is set as
Secondary Controller.

4. Both Controllers are reset and set the NodeID to 1 and HomeID to random.

5. The Controller is included as Secondary Controller and assumes the SIS Role. The including
Controller assumes the role of RealPrimary Inclusion Controller.

6. Real Primary requests a Reserve Node ID to the SIS before starting Inclusion Mode.

a. Secure bootstrapping is handled by the SIS.

7. The SIS Controller includes the AL End Node and it performs a Neighbor and Range test on it.

a. The AL End Node probes both Controllers and the FL End Node.

8. The second AL End Node is included to the third Controller.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 120


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


9. The RealPrimary Controller removes the second AL End Node.

a. The RealPrimary Inclusion Controller does not notify the SUC/SIS about removing it.

10. The third Controller resets its network and drops the previous one.

11. The third Controller is included to the SUC/SIS Controller.

a. The third Controller updates its network information with the new one while in learning
mode.

b. The RealPrimary Controller does not update its Network information.

c. The third Controller probes all existing nodes in the network.

d. The third Controller is included as a Secondary Inclusion Controller.

12. The button is disabled. Secondary Controllers can’t give that role to another controller.


**3.53.4** **Pass** **Criteria**


1. A Controller included in a network shall assume the Secondary Controller role (NWK:01D3.1).

2. A secondary Controller receiving SUC NodeID with SUC Capabilities bit 0 set to 1 becomes an
Inclussion Controller (NWK:01D5.1).

3. A Controller receiving Set SUC Command from the Primary Controller shall assume the
SUC/SIS role (NWK:01D6.1, NWK:01D9.1).

4. Secondary Controllers don’t give the SUC role to other Controllers (NWK:01DA.1).

5. A SUC/SIS Controller that is the only controller in its network issues SUC NodeID to the other
Controllers in the network (NWK:01DE.1).

6. The SUC/SIS stores the network topology and updates it when the nodes are added/removed.
It updates nodes that request the network topology (NWK:01EA.1, NWK:01CC.1).

7. Inclusion Controllers update the topology with an Automatic Controller Update from the SUC
either by a full transfer of network information or a list of changes. The requesting Controller
does not erase the existing information of the same network and only updates it (NWK:01EB.1,
NWK:01EC.1, NWK:01ED.1). Result 10.a.

8. Inclusion Controller sends Automatic Controller Update Start to the SUC to start an Automatic
Update. The SUC sends the topology information using New Node Registered and New Range
Registered. A Node Exists Command is issued when updating over 64 changes (supported only
by Static Controller in 500s) (NWK:01EE.1). Result 10.a.

9. Automatic Controller update follows Figures 3.86 or 3.87. This is triggered on application Layer
(NWK:01EF.1, NWK:01F0.1). Result 10.a.

10. Controller Replication is initiated by the Primary Controller. The Controller that will be included/transfer Topology is in learning mode and the process follows Figure 4.44 (NWK:01F6.1,
NWK:01F7.1).

11. Any Controller starts a Neighbor Discovery as part of inclusion. Neighbor Discovery may be
done periodically by a Primary Controller to update its network topology. It shall follow Figure
4.45 or Figure 4.46 (NWK:01F8.1, NWK:01F9.1, NWK:01FA.1).

12. FL nodes of 250ms and 1000ms may be in the same Find Nodes In Range command setting the
“Wake Up Time” field to 0x01 as per Figure 4.46 (NWK:01FB.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 121


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.53.5** **Fail** **Criteria**


1. Any of the passing Criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 122


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.54 Functional Description – Controller Functionalities and Network Maintenance


Controllers can perform different functionalities depending on their role and maintain the status of
the network.


**3.54.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 2 x AL End Nodes.

 - 1 x FL End Node


**3.54.2** **Test** **Setup**


1. Include the second Controller setting it as SIS to the primary Controller.

2. Include FL End Node to the Network with the RealPrimary Controller.

3. Include the first AL End Node to the Network using SUC/SIS Controller directly.

4. On the Third Controller include the second AL End Node forming a separate network.

5. Set the RealPrimary Inclusion Controller in exclusion mode. Set the second AL End Node in
learning mode.

6. Reset the third Controller’s network.

7. Set the SUC/SIS in inclusion Mode. Set the third Controller in Learning Mode.

8. Include the second AL End Node to the third Controller.

9. Set the Secondary Inclusion (third) Controller in Learning Mode. On Real Primary Controller
press the Shift button to transfer the role of Primary Controller.

10. On the new RealPrimary (third) Controller select the first (now Secondary/Inclusion) Controller.
Press Set as SIS button.

11. Set the new RealPrimary in exclusion mode. Exclude the second AL Node.

12. In the new Secondary Controller press the Update button.

13. Remove the new Secondary (first) Controller from the network with the new RealPrimary (third)
Controller.


**3.54.3** **Test** **Result**


1. The Secondary Controller is included answers with Set SUC ACK (SUC Capability = 0x01) and
assumes the SIS Role.

a. The including Controller assumes the RealPrimary role.

2. Real Primary requests a Reserve Node ID to the SIS before starting Inclusion Mode.

a. Secure bootstrapping is handled by the SIS.

3. The SIS Controller includes the AL End Node and it performs a Neighbor and Range test on it.

a. The AL End Node probes both Controllers and the FL End Node.

4. The second AL End Node is included to the third Controller.

5. The second AL End Node is excluded from the second network.

a. The SUC/SIS is not notified of this exclusion.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 123


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


6. The third Controller’s Network is reset and it gets a new Home ID and it drops its Node List.

7. The third Controller is included to the SUC/SIS Controller.

a. The third Controller updates its network information.

b. The RealPrimary Controller does not update its Network information.

c. The third Controller probes all existing nodes in the network.

d. The third Controller is included as a Secondary Inclusion Controller.

8. The third Controller (Secondary Inclusion Controller) includes the second AL End Node to the
Network.

a. The Inclusion Controller requests an Automatic Controller Update before the Inclusion.

b. The Inclusion Controller requests a Reserved Node ID to the SIS.

c. The SUC/SIS Controller handles the secure Bootstrapping.

d. The second AL End Node probes all nodes in the network.

e. Only the SUC/SIS and Secondary Inclusion (third) Controllers update their Network information.

9. The RealPrimary Controller starts the process to shift Roles

a. RealPrimary Controller requests an Automatic Network Update to the SIS.

b. It transfers all Node Info and Range info it holds to the Secondary (Third) controller.

c. The transference ends with a Transfer New Primary Completed command and Transfer
End.

10. There can only be one SUC/SIS in the network. The attempt is rejected.

11. The new RealPrimary Controller excludes the second AL End Node.

a. It issues a New Node Registered Command to the SUC/SIS Controller.

b. The SUC Updates its Network Topology status.

12. The new Secondary Controller requests a Network Update by going in Learning Mode.

13. The new Secondary (first) Controller is removed from the Network.

a. The (second) SUC/SIS is notified of this change.

b. The new RealPrimary (third) Controller ends the exclusion issuing a Transfer End to
NodeID 0.


**3.54.4** **Pass** **Criteria**


1. A secondary Controller in Learning Mode must accept Transfer Primary Controller when received (NWK:01D4.1).

2. When shifting the Primary Controller role, it follows Figure 4.80. This role shall be accepted
(NWK:01D7.1, NWK:01D8.1).

3. Giving the SUC/SIS role follows Figure 4.81. Primary Controller doesn’t assign the SUC/SIS
role if there is one already present in the network (NWK:01DB.1, NWK:01DC.1).

4. A Primary Controller takes the Inclusion Controller role if the other controller accepts the
SUC/SIS role returning Set SUC Ack with “State” and “Capabilities” fields set to 0x01
(NWK:01DD.1).

5. Inclusion Controllers can add nodes on behalf of the SIS (NWK:01E1.1).

6. An Inclusion Controller requests an Automatic Controller Update to the SIS prior including a
node (NWK:01E2.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 124


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


7. Secondary Controller goes into Learn Mode to receive the network topology (NWK:0195.1,
NWK:0199.1).

8. Controllers excluding a Controller should issue a Transfer End command to HomeID 0x00000000
and NodeID 0x00 for backwards compatibility; The excluded Controller acknowledges the Transfer End (NWK:01C4.1, NWK:01C5.1).

9. Inclusion Controllers request NodeID to the SIS before inclusion (NWK:01E3.1).

10. Inclusion Controller issues New Node Registered and New Range Registered to the SIS after
successful inclusion (NWK:01E4.1).

11. Inclusion by an Inclusion Controller follows Figure 4.38 (NWK:01E5.1).

12. Inclusion Controller may remove nodes from the network on behalf of the SIS. Issuing a New
Node Registered to the SIS when it’s a node from the same network but not when it’s a foreign
Network. Exclusion by an Inclusion Controller follows Figure 4.39 (NWK:01E6.1, NWK:01E7.1,
NWK:01E8.1, NWK:01E9.1).

13. When the SUC is not the Primary Controller, the Primary Controllers update the SUC with
updated topology after including or excluding a node, by Issuing New Node Registered and New
Range Registered after a successful inclusion after Figure 4.42 (NWK:01F1.1, NWK:01F2.1).

14. A Primary Controller Issues New Node Registered to the SUC after successfully removing a
node in the same network, not when it’s in a different network and the exclusion update follows
Figure 4.43 (NWK:01F3.1, NWK:01F4.1, NWK:01F5.1).


**3.54.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 125


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.55 (3.20 – Negative testing) Command Frames – Z-Wave Protocol Command Class – Assign IDs Command


**3.55.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 1 x End Node.


**3.55.2** **Test** **Setup**


1. While the nodes haven’t been added to the Controller’s network: configure Assign ID to be sent
as multicast (header type 0x03).

2. Set End Node in learning mode and transmit the command from the emitter.

3. Set the secondary Controller in learning mode and transmit the command from the emitter.

4. Set Assign ID to be sent as singlecast and set the NodeID value to be greater than 0xE8.

5. Set End Node in learning mode and transmit the command from the emitter.

6. Set the secondary Controller in learning mode and transmit the command from the emitter.


**3.55.3** **Test** **Result**


2. The End Node ignores the “Assign ID” command sent as Multicast and doesn’t change its
NodeID nor Home ID: send NIF from the End Node and it hasn’t changed either ID.

3. The secondary Controller ignores the “Assign ID” command sent as Multicast and doesn’t change
its NodeID nor Home ID: send NIF from the End Node and it hasn’t changed either ID.

5. The End Node ignores the “Assign ID” command sent with NodeID set higher than 0xE8 and
doesn’t change its NodeID nor Home ID: send NIF from the End Node and it hasn’t changed
either ID.

6. The secondary Controller ignores the “Assign ID” command sent with NodeID set higher than
0xE8 and doesn’t change its NodeID nor Home ID: send NIF from the End Node and it hasn’t
changed either ID.


**3.55.4** **Pass** **Criteria**


1. The End Node and the Secondary Controller ignore the command when it’s issued as a multicast
(NWK:0089.1).

2. The End Node and the Secondary Controller ignore the Assign ID command when the NodeID
field is set higher than 0xE8 (NWK:008C.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 126


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.55.5** **Fail** **Criteria**


1. The nodes accept the “Assign ID” command when it’s issued as multicast (NWK:0089.1).

2. The nodes accept values higher than 0xE8 for NodeID when being included (NWK:008C.1).

3. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 127


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.56 (3.21 – Negative testing) Command Frames – Z-Wave Protocol Command Class – Find Nodes in Range Command


This command is used to request the receiving node to find the nodes in direct range.


**3.56.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 2 x AL End Node.

 - 2 x FL End Node.

 - 1 x NL End Node.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.56.2** **Test** **Setup**


1. Override the “Find Nodes in Range” command to be sent as a multicast.

2. Include to the primary Controller’s Network the first AL End Node.

3. Override the “Find Nodes in Range” command to be sent as a singlecast. Set the “Node Bitmask”
field to not include NodeID 1.

4. Include to the primary Controller’s Network the first AL End Node.

5. Override the “Find Nodes in Range” command to set the “Bitmask Length” field to be more
than 0x01.

6. Include to the primary Controller’s Network the first AL End Node.

7. Remove overrides and include the first AL End Node.

8. Override the “Find Nodes in Range” command to set the “Node Bitmask” only with NodeID 1
enabled.

9. Include the NL End Node to the network.

10. Override the “Find Nodes in Range” command to set the “Node Bitmask” to only include
NodeID of the NL node and to include the “Wake Up Time” field set to 0x01.

11. Include the first FL End Node to the network.

12. Override the “Find Nodes in Range” command to set the “Node Bitmask” to include NodeID
of all the End Nodes and override it so that it does not include the “Wake Up Time” field.

13. Include the secondary Controller to the network.

14. Override the “Find Nodes in Range” command to set the “Node Bitmask” to only include
NodeID of nodes not existing in the network and to include the “Wake Up Time” field set to
0x01.

15. Include the second AL End Node.

16. Override the “Find Nodes in Range” command to set the “Node Bitmask” to include NodeID
of the first FL node “Wake Up Time” field set to 0x01 and the value of the “Data Rate” field
to a value higher than 0x03.

17. Include the second FL End Node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 128


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.56.3** **Test** **Result**


2. The first AL End Node is not included to the Controller’s Network.

4. The first AL End Node’s inclusion fails.

6. The first AL End Node’s inclusion fails.

7. The first AL End Node is included.

9. The NL End Node is included. The NL End Node does not send NOP frame to the first AL
End Node.

11. The first FL End Node is included. It sends NOP frames to the primary Controller, the first
AL End Node and the controller sends a second “Find Nodes in Range” command with only the
NL NodeID. The first FL End Node tries sending Wake Up beams to the NL End Node. The
NL End Node does not wake up and it returns a Node Range Info frame empty.

13. The secondary Controller tries reaching out to the AL End Node, the NL End Node and the
FL End Node in the same Neighbors Test without using Beams. It returns to the Controller a
“Node Range Info” frame including only NodeID of the Controller and the first AL End Node.

15. Upon receiving the “Find Nodes in Range” command, the second AL End Node begins trying
to reach with NOP singlecasts and Wake Up beams to each of the NodeIDs listed in the “Node
Bitmask” field. It returns a “Node Range Info” empty to the Controller.

17. The second FL node sends NOP singlecast to the Controller, the first AL End Node and secondary Controller successfully, it ignores the NL End Node and the controller sends a second
“Find Nodes in Range” command with the “Data Rate” field set to a value higher than 0x03.
The second FL End Node ignores this command.


**3.56.4** **Pass** **Criteria**


1. The “Find Nodes in Range” Command in all instances follows the format described by Table
4.32 (NWK:008D.1).

2. The “Find Nodes in Range” command sent as multicast is ignored as a multicast. The
“Node Bitmask” field shall set to 0 is ignored and inclusion fails (NWK:009D.1, NWK:009E.1,
NWK:00A1.1).

3. The receiving node tries to reach to the NodeIDs included in the “Node Bitmask” field and
ignores any NodeID not included (NWK:0091.1).

4. The receiving nodes validate the Bitmask Length against the number of elements contained in
the “Node Bitmask”, if it doesn’t match the frame is rejected (NWK:0092.1).

5. The receiving Node will not beam a NodeID if it’s not included in the “Find Nodes in Range”
including the “wake Up Time” field (NWK:0096.1, NWK:0097.1).

6. The “Data Rate” field shall not be set to a value higher than 0x03, frames that don’t comply
are ignored (NWK:009A.1, NWK:009B.1, NWK:009C.1).


**3.56.5** **Fail** **Criteria**


1. If any of the pass criteria is not met (the expected behavior is not met, or the overrides produce
a successful behavior in spite of being configured against it).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 129


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.57 (3.22 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – Get Nodes in Range Command


The Get Nodes in Range command is used to request the list of direct range neighbors detected with
the last range test.


**3.57.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 2 x End Nodes.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.57.2** **Test** **Setup**


1. Override the “Get Nodes in Range” to be sent as multicast.

2. Include the End Node to the primary Controller’s network.

3. Include the secondary Controller to the primary Controller’s network.

4. Override “Get Nodes in Range” to change its Command number from 0x05 to something different.

5. Include the End Node.

6. Include the secondary Controller.


**3.57.3** **Test** **Result**


2. When the End Node receives “Get Nodes in Range” as a multicast it ignores it and inclusion
does not finish that step. Inclusion is unsuccessful and the node self-resets.

3. When the secondary Controller receives “Get Nodes in Range” as a multicast it ignores it and
inclusion does not finish that step. Inclusion is unsuccessful and the node self-resets.

5. When the primary Controller tries to issue “Get Nodes in Range”, it sends a command different
from 0x03. The receiving End Node does not respond sending a “Range Info” command.

6. When the primary Controller tries to issue “Get Nodes in Range”, it sends a command different from 0x03. The receiving secondary Controller does not respond sending a “Range Info”
command.


**3.57.4** **Pass** **Criteria**


1. When the command is sent as multicast or its number value is modified from 0x03, the receiver
does not return a “Range Info” in response (NWK:00A2.1, NWK:00A5.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 130


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.57.5** **Fail** **Criteria**


1. The receiving nodes respond with “Range Info” even when the “Get Nodes in Range” command is sent multicast or its command number value is different from 0x03 (NWK:00A2.1,
NWK:00A5.1).

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 131


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.58 (3.23 - Negative Testing) Command Frames – Z-Wave Protocol Command Class – Range Info Command


The Range Info command is used to advertise the list of direct range neighbors detected with the last
range test.


**3.58.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 1 x AL End Node.

 - 1 x FL End Node.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.58.2** **Test** **Setup**


1. Include the AL End Node to the primary Controller’s network.

2. Override the Range Info command in the secondary Controller so that it includes a Wakeup
Time field with value 0x01. Include the secondary Controller.

3. Remove overrides on the secondary Controller. Remove the secondary Controller from the
network.

4. Override the Range Info frame to hold a Bitmask Length larger than 1. Include the secondary
Controller.

5. Remove overrides on the secondary Controller. Remove the secondary Controller from the
network.

6. Include the FL End Node.

7. Override the “¬Node Range Info” frame on the secondary Controller to NOT include Wake UP
Time. Include the secondary Controller.

8. Send a NOP frame from the secondary Controller to the FL End Node. Then from the primary
Controller to the FL End Node.

9. Remove the secondary Controller. Set its “Node Range Info” command to be set as multicast
only.

10. Include the secondary Controller.


**3.58.3** **Test** **Result**


1. During inclusion, the End Node responds to Get Nodes in Range with “Node Range Info”
command.

2. After “Get Nodes in Range” command is received, the secondary Controller answers with a
“Nodes in Range” command containing the Wake up Time byte. The primary Controller ignores
this field.

3. The secondary Controller is removed.

4. During inclusion, secondary Controller sends Range Info frame with a Bitmask Length value
larger than 1. This frame is not accepted by the primary Controller since it doesn’t match the
actual contents of Node Bitmasks.

5. The secondary Controller is removed.

6. The FL End Node is included correctly.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 132


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


7. The secondary Controller is included and its “Node Range Info” frame is overridden, so after it
searches for the FL End Node with beams, it responds to the primary Controller with “Node
Range Info” not including a Wake up Time field.

8. The secondary Controller beams to the FL End Node before delivering the NOP frame. The
primary Controller doesn’t beam the FL End Node[?].

9. The secondary Controller is removed.

10. The secondary Controller issues “Node Range Info” as a multicast. The primary Controller does
not send an ACK frame for this.


**3.58.4** **Pass** **Criteria**


1. The Node Range Info commands follow the format from Table 4.36 (NWK:00A6.1).

2. The Length in Bytes of the Node Bitmask field should be the same as the one defined by the
“Bitmask Length” field (NWK:00A7.1).

3. The Node Bitmask is treated as a Mask and not as the direct NodeID values. The bits set as
1 indicate that the corresponding NodeID is within range of the node sending this frame. The
first byte represents nodes 1…8 (NWK:00A8.1, NWK:00A9.1, NWK:00AA.1).

4. When the Wake-Up Time field is present, its value must be verified by the receiver. When it’s
not, the receiver assumes a value of 0x00 (NWK:00AB.1, NWK:00AC.1).

5. The Node Bitmasks holds the result of the last Range Test and not previous ones. If there were
no Tests, the Node Bitmask field is set to 0x00 (NWK:00AD.1, NWK:00AE.1).

6. This command is only validated when it’s sent as singlecast and not multicast (NWK:00AF.1).


**3.58.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 133


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.59 (3.24 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – Command Complete Command


Used to advertise the completion of a given task.


**3.59.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC controller.

 - 1 x AL End Node.

 - 1 x FL End Node.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.59.2** **Test** **Setup**


1. Include the AL & FL End Nodes to the primary Controller’s network.

2. Override the Command Complete command so that it’s sent as multicast. Include it to the
network.

3. Remove the secondary Controller.

4. Override the Command Complete command so that it’s delayed for 5 seconds and holds a
Sequence Number field that increases on each use. Include it again to the network.

5. Remove the secondary Controller.

6. Override the Command Complete command so that it holds a Sequence Number field that is
unrelated to the previous one on each use. Include it again to the network.


**3.59.3** **Test** **Result**


1. The AL & FL End Nodes are successfully included.

2. The secondary Controller tries to be included. It sends Command Complete as multicast and
the frames are ignored.

3. Secondary Controller is removed.

4. The secondary Controller waits 5 seconds before sending “Command Complete” each time and
the primary Controller waits during this period. The secondary Controller assigns consecutive
Sequence Number values and inclusion is successful.

5. Secondary Controller is removed.

6. The secondary Controller assigns non-related Sequence Number values and those frames are
ignored. Inclusion fails.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 134


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.59.4** **Pass** **Criteria**


1. When Command Complete is issued as multicast, it’s ignored (NWK:00B4.1, NWK:00B6.1).

2. When the Sequence Number field changes sequentially, the frames are accepted, when they are
not sequential, the frames are ignored (NWK:00B2.1, NWK:00B5.1).


**3.59.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 135


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.60 (3.26 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – Transfer Node Information Command


This command is used for transferring the Node Information Frame from one controller to another.


**3.60.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 3 x End Nodes.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.60.2** **Test** **Setup**


1. Include all 3 End Nodes to the primary controller.

2. Override in the primary Controller Transfer Node Info to retain the same Sequence Number.

3. Include the secondary Controller.

4. Remove the secondary Controller.

5. Override in the primary Controller Transfer Node Info to send the command as multicast.

6. Include the secondary Controller.

7. Remove the second End Node.

8. Override primary Controller to force send Transfer Node Info during inclusion.

9. Include the removed End Node.


**3.60.3** **Test** **Result**


1. All 3 End Nodes are included to the Controller’s Network.

2. Sequence Number is set to a constant value.

3. Secondary Controller begins being included

a. Primary Controller sends each “Transfer Node Information” frame with the same Sequence
Number value.

b. The frames are detected as duplicate and they are ignored.

4. Secondary Controller is removed.

5. The command is set to be sent as multicast.

6. Secondary Controller begins being included

a. Primary Controller sends each “Transfer Node Information” frame as a multicast and the
secondary Controller ignores it.

7. The second End Node is removed.

8. Transfer Node Info is set to be sent forcefully.

9. The End Node inclusion begins.

a. Primary Controller sends Transfer Node Info to the End Node.

b. The End Node ignores the Transfer Node Info frames.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 136


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.60.4** **Pass** **Criteria**


1. Each sequence number is individual and unique for each Node Information being transferred
from one Controller to another (NWK:00C2.1).

2. Sequence Numbers are used to detect duplicates (NWK:00C3.1).

3. The command is sent only when including a secondary Controller (NWK:00C5.1).

4. The command is sent only singlecast and ignored when it’s sent multicast (NWK:00C6.1).

5. End Nodes ignore the frame when it’s sent to them during inclusion (NWK:00C7.1).

6. The secondary Controller ignores the commands when they were forcefully sent to the End Node
(NWK:00C8.1).


**3.60.5** **Fail** **Criteria**


1. The sequence number on all Transfer Node Information frames is the same (NWK:00C2.1).

2. Sequence Numbers irrelevant to detect duplicates (NWK:00C3.1).

3. The command is sent outside the inclusion of a secondary Controller (NWK:00C5.1).

4. The command is accepted when delivered as multicast (NWK:00C6.1).

5. End Nodes try to adjust an internal Node List when received during inclusion (NWK:00C7.1).

6. The secondary Controller adjusts its internal Node List when the command is sent to a End
Node (NWK:00C8.1).

7. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 137


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.61 (3.27 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – Transfer Range Information Command


This command is used to transfer a node’s range test result from one Controller to another.


**3.61.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 3 x End Nodes.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.61.2** **Test** **Setup**


1. Include all 3 End Nodes to the primary controller.

2. Override in the primary Controller Transfer Range Info to retain the same Sequence Number.

3. Include the secondary Controller.

4. Remove the secondary Controller.

5. Override in the primary Controller Transfer Range Info to send the command as multicast.

6. Include the secondary Controller.

7. Remove the second End Node.

8. Override primary Controller to force send Transfer Range Info during inclusion.

9. Include the removed End Node.


**3.61.3** **Test** **Result**


1. All 3 End Nodes are included to the Controller’s Network.

2. Sequence Number is set to a constant value.

3. Secondary Controller begins being included

a. Primary Controller sends each “Transfer Range Information” frame with the same Sequence
Number value.

b. The frames are detected as duplicate and they are ignored.

4. Secondary Controller is removed.

5. The command is set to be sent as multicast.

6. Secondary Controller begins being included

a. Primary Controller sends each “Transfer Range Information” frame as a multicast and the
secondary Controller ignores it.

7. The second End Node is removed.

8. Transfer Range Info is set to be sent forcefully.

9. The End Node inclusion begins.

a. Primary Controller sends Transfer Range Info to the End Node.

b. The End Node ignores the Transfer Range Info frames.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 138


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.61.4** **Pass** **Criteria**


1. The Sequence Number Field increases each time it’s sent, and if it remains static it’s ignored
(NWK:00CC.1, NWK:00CD.1).

2. It is sent as singlecast by default and it’s ignored when it’s sent as multicast (NWK:00CE.1,
NWK:00D0.1).

3. When this command is forcedly sent to an End Node, the End Node ignores it (NWK:00D1.1).


**3.61.5** **Fail** **Criteria**


1. The Sequence Number Field remains static and it’s accepted regardless of being seemingly
duplicate (NWK:00C.1, NWK:00CD.1).

2. It is not sent as singlecast by default or it’s accepted as valid when it’s sent as multicast
(NWK:00CE.1, NWK:00D0.1).

3. It is sent regardless of whether a Controller or a End Node is being included and the End Node
accepts it (NWK:00D.1).

4. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 139


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.62 (3.28 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – Transfer End Command


This command is used to advertise the end of the current network operation (Static route request,
Automatic controller update, Controller replication).


**3.62.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 1 x End Node.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.62.2** **Test** **Setup**


1. Include the secondary Controller.

2. Include End Node to the network with Primary Controller.

3. Include the Third Controller to the Network with Primary Controller.

4. In the primary Controller, Override Transfer End Status to be 0x00 (Transfer Failed).

5. Set the Third Controller in Learning mode and activate “Shift” in primary Controller.

6. In the primary Controller, Override Transfer End Status to be 0x03 (Transfer Aborted).

7. Set the first Controller in Learning mode and activate “Shift” in the third (primary) Controller.

8. In the primary Controller, Override Transfer End Status to be 0x04 (Transfer update Wait).

9. Set the third Controller in Learning mode and activate “shift” in the first (primary) Controller.

10. In the primary Controller, Override Transfer End Status to be 0x05 (Transfer update disabled).

11. Set the first Controller in Learning mode and activate “Shift” in the third (primary) Controller.

12. In the primary Controller, Override Transfer End Status to be 0x06 (Transfer update overflow).

13. Set the third Controller in Learning mode and activate “shift” in the first (primary) Controller.


**3.62.3** **Test** **Result**


1. The secondary Controller is included as SIS of the Network. Primary Controller is set as “Real
Primary”.

2. End Node is included to the network.

3. Third Controller is included to the network.

4. Status is overridden in primary Controller’s Transfer End.

5. The primary Controller transfers Node Information and Node Range information to the Third
Controller. The Third Controller is set as “Real Primary” Controller now.

a. When the first Controller sends “Transfer End” with status 0x00 (Transfer Failed), the
third Controller requests nodes and ranges information immediately (It continues getting
this status as long as it’s overridden).

6. Status is overridden in primary Controller’s Transfer End.

7. The primary Controller transfer Node Information and Node Range information to the First
Controller. The first Controller is set as “Real Primary” Controller now.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 140


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


a. When the third Controller sends “Transfer End” with status 0x03 (Transfer Update
Aborted), the first Controller requests nodes and ranges information after ‘nwkMinOperationBackOffTime’ has passed before trying again.

8. Status is overridden in primary Controller’s Transfer End.

9. The primary Controller transfers Node Information and Node Range information to the Third
Controller. The Third Controller is set as “Real Primary” Controller now.

a. When the first Controller sends “Transfer End” with status 0x04 (Transfer update wait),
the third Controller requests nodes and ranges information after ‘nwkMinOperationBackOffTime’ has passed before trying again.

10. Status is overridden in primary Controller’s Transfer End.

11. The primary Controller transfer Node Information and Node Range information to the First
Controller. The first Controller is set as “Real Primary” Controller now.

a. When the third Controller sends “Transfer End” with status 0x05 (Transfer Update disabled), the first Controller does not request nodes and ranges information again.

12. Status is overridden in primary Controller’s Transfer End.

13. The primary Controller transfers Node Information and Node Range information to the Third
Controller. The Third Controller is set as “Real Primary” Controller now.

a. When the first Controller sends “Transfer End” with status 0x06 (Transfer update overflow),
the third Controller requests nodes and ranges information again


**3.62.4** **Pass** **Criteria**


1. The Status field notifies Network information. It is encoded as per Table 4.43 (NWK:00D5.2).


**3.62.5** **Fail** **Criteria**


1. The Status field does not follow Table 4.43 (NWK:00D5.2).

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 141


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.63 (3.30 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – New Node Registered Command


This command is used to notify the SIS Controller that an inclusion controller has included a new
node in the network.


**3.63.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 1 x End Node.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.63.2** **Test** **Setup**


1. Set the primary controller to be SIS.

2. Include the secondary Controller.

3. Override “New Node Registered” Command by setting it to be sent Multicast.

4. Include the End Node with the Inclusion Controller.


**3.63.3** **Test** **Result**


1. The primary Controller is set as SIS.

2. The secondary Controller is set as Inclusion Controller.

3. “New Node Registered” is set to be sent multicast.

4. The inclusion process begins, and the secondary Controller sends “New Node Registered” as
Multicast.

a. The SIS ignores this frame.

b. Inclusion of the End Node is not concluded successfully.


**3.63.4** **Pass** **Criteria**


1. It is ignored when it’s sent as a multicast (NWK:00E6.1).


**3.63.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 142


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.64 (3.31 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – New Range Registered Command


This command is used to advertise the range test results that an inclusion controller has performed
when including a new node.


**3.64.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 2 x Z-Wave PC Controller.

 - 2 x End Nodes.

We assume it’s possible to override the fields of the command in advance to performing inclusion.


**3.64.2** **Test** **Setup**


1. Include the first End Node to the primary Controller’s network.

2. Include the secondary Controller to the primary Controller’s network.

3. Create one Hop of distance between the first End Node and the second End Node (Remove their
antennas or place the network in a RF shielded wired system to control impedance of radio, so
that they don’t see each other during inclusion of the second End Node).

4. Override the New Range Registered command to be sent as multicast.

5. Set the first End Node in learning Mode.

6. Include the second End Node with the Inclusion Controller.

7. Remove the second End Node with the Inclusion Controller.

8. Override the New Range Registered command to set the Neighbor Nodes Bitmask to values that
are not present in the network. Make sure to match it in the Neighbor Nodes Bitmask Length
field.

9. Include the second End Node with the Inclusion Controller.

10. Remove the second End Node with the Inclusion Controller.

11. Override the New Range Registered command to set the Neighbor Nodes Bitmask Length to
mismatch the amount of Neighbor Nodes Bitmask field.

12. Include the second End Node with the Inclusion Controller.


**3.64.3** **Test** **Result**


1. The first End Node is included into the Controller’s network.

2. The second Controller is included, it becomes an Inclusion Controller.

3. Neither End Node is within range of the other, but in range of both Controllers.

4. The command is overridden to be sent multicast.

5. The first End Node is in learning mode.

6. The second End Node is attempted to be included.

a. After probing the neighbor’s range, the Inclusion Controller sends as multicast the New
Range Registered Command.

b. Both the primary Controller and the first End Node ignore this multicast command.

c. Inclusion is unsuccessful.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 143


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


7. The second End Node is removed.

8. The values of the fields are overridden.

9. The second End Node is attempted to be included.

a. The Inclusion Controller sends to the primary Controller the New Range Registered Command as a singlecast with the Neighbor Nodes Bitmask values mismatching the existing
nodes in the network.

b. The primary Controller ignores this command.

10. The second End Node is removed.

11. The value of the field is overridden.

12. The second End Node is attempted to be included.

a. The Inclusion Controller sends to the primary Controller the New Range Registered Command as a singlecast with the Neigbor Nodes Bitmask Length mismatching the amount of
nodes in the network.

b. The primary Controller ignores this command.


**3.64.4** **Pass** **Criteria**


1. The “Neighbor Nodes Bitmask Length” field corresponds to the number of nodes within range of
the node being included. It should be set to the minimum of 1 (which is the Inclusion Controller)
(NWK:00EA.1).

2. The “Neighbors Nodes Bitmask” field holds the list of NodeIDs that the node being included/just
performed the neighbors Range Test can reach, its length should match the one described by
the “Neighbor Nodes Bitmask Length” field (NWK:00EB.1, NWK:00EC.1).

3. This command shall be ignored when received by an End Node also when it’s issued as a multicast
(NWK:00F2.1, NWK:00F3.1).


**3.64.5** **Fail** **Criteria**


1. The “Neighbor Nodes Bitmask Length” does not show the actual number of neighboring nodes,
not even the minimum set to 1 (NWK:00EA.1).

2. The “Neighbors Nodes Bitmask” field doesn’t hold the list of Nodes that the node being included/performed the Neighbors Range Test can reach. Its length is not matching that of the
“Neighbor Nodes Bitmask Length” field (NWK:00EB.1, NWK:00EC.1).

3. This command is not ignored by End Nodes or when it’s issued as multicast (NWK:00F2.1,
NWK:00F3.1).

4. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 144


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.65 (3.36 – Negative Testing) Command Frames – Z-Wave Protocol Command Class – Set SUC ACK Command


This command is used to respond to a Set SUC Command.


**3.65.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

We assume it’s possible to override the fields of the command in advance to performing inclusion


**3.65.2** **Test** **Setup**


1. In the second Controller override Set SUC ACK command to be set its “Result” field to 0x00.

2. Include the reset second Controller to the network with RealPrimary Controller.

3. Include the third Controller to the Primary Controller.


**3.65.3** **Test** **Result**


1. The Set SUC ACK command is overridden to be responded in the next inclusion.

2. The second Controller is included but doesn’t accept the SUC/SIS Controller role.

3. The third Controller is included and set as SIS.


**3.65.4** **Pass** **Criteria**


1. When a Controller rejects the SUC role, it sets its “Result” field to 0x00 (NWK:010C.1).

2. The “Capabilities” field is encoded as per Table 4.52 (NWK:010D.1).


**3.65.5** **Fail** **Criteria**


1. When a Controller rejects the SUC role, it fails at setting it to 0x00, or uses entirely any other
values (NWK:010C.1).

2. The “Capabilities” field doesn’t follow Table 4.52 (NWK:010D.1).

3. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 145


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.66 (3.53 – Negative Testing) Functional Description – Controller Roles and Network Operations


Controllers can change roles in a network following different procedures.


**3.66.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 1 x Z-Wave PC Controller.

 - 1 x Controller with variable SUC capabilities.

We assume it’s possible to override the fields of the command in advance to performing inclusion


**3.66.2** **Test** **Setup**


1. Set to “No SUC” the controller with variable SUC capabilities, include it to one of the regular
Controllers. Try assigning it the SUC/SIS Role.

2. Reset both Controllers.

3. Set only to “SUC” the controller with variable SUC capabilities, include it to one of the regular
Controllers. Try assigning it the SUC/SIS Role.

4. Reset both Controllers.

5. Override on the first Controller to send the SUC Node ID Command overridden with bit 0 of
“SUC Capabilities” field set to 1. Include the second Controller again.

6. From the Primary Controller send Set as SIS to the secondary Controller.


**3.66.3** **Test** **Result**


1. The Controller is included. It rejects the SUC/SIS role in the network as per Figure 3.82.

2. Both Controllers are reset and set the NodeID to 1 and HomeID to random.

3. The Controller is included. It rejects the SIS role in the network as per Figure 3,.83.

4. Both Controllers are reset and set the NodeID to 1 and HomeID to random.

5. The Controller is included as Secondary Controller, it answers with Set SUC ACK (SUC Capability = 0x00) and assumes the Inclusion Controller role.

a. The including Controller assumes the role of RealPrimary Inclusion Controller.

6. The Secondary Controller answers with Set SUC ACK (SUC Capability = 0x01) and assumes
the SIS Role.


**3.66.4** **Pass** **Criteria**


1. A Controller with no SUC Capabilities declines the role as per Figure 4.36 (NWK:01DF.1).

2. A Controller with only no SIS capabilities should decline the role as per Figure 4.37
(NWK:01E0.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 146


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.66.5** **Fail** **Criteria**


1. Any of the passing Criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 147


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## 3.67 (3.54 – Negative Testing) Functional Description – Controller Functionalities and Network Maintenance


Controllers can perform different functionalities depending on their role and maintain the status of
the network.


**3.67.1** **Prerequisites**


 - 1 x Z-Wave Zniffer.

 - 3 x Z-Wave PC Controller.

 - 2 x AL End Nodes

 - 1 x FL End Node

 - 1 x Z-Wave OPN with RAILTest flashed on it (configured to send Static Route Request Command)


**3.67.2** **Test** **Setup**


1. Include the second Controller setting it as SIS to the primary Controller.

2. Include FL End Node to the Network with the RealPrimary Controller.

3. Include the first AL End Node to the Network using SUC/SIS Controller directly.

4. Set the SUC/SIS in inclusion Mode. Set the third Controller in Learning Mode.

5. Include the second AL End Node to the third Controller.

6. Set the Secondary Inclusion Controller in Learning Mode. On Real Primary Controller press
the Shift button to transfer the role of Primary Controller.

7. Set the new RealPrimary in exclusion mode. Exclude the second AL Node.

8. Remove the new Secondary Controller from the network with the new RealPrimary Controller.

9. Place the excluded Secondary Controller one hop away from the SUC/SIS and the Real/Primary
Controller. Include it with NWI to the network using the AL End Node as a repeater.

10. Include the AL End Node using the Secondary Controller so that it has 1 or 2 hops distance to
the SUC/SIS.

11. Configure RAILTest to have the same NodeID and HomeID as this AL End Node. Power Off
the actual End Node to prevent confusion in the network.

12. Trigger the Static Route Request Command on the RAILTest device. Make sure it’s configured
to request return routes for up to 5 nodes.


**3.67.3** **Test** **Result**


1. The Secondary Controller is included answers with Set SUC ACK (SUC Capability = 0x01) and
assumes the SIS Role.

a. The including Controller assumes the RealPrimary role.

2. Real Primary requests a Reserve Node ID to the SIS before starting Inclusion Mode.

a. Secure bootstrapping is handled by the SIS.

3. The SIS Controller includes the AL End Node and it performs a Neighbor and Range test on it.

a. The AL End Node probes both Controllers and the FL End Node.

4. The third Controller is included to the SUC/SIS Controller.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 148


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


a. The third Controller updates its network information.

b. The RealPrimary Controller does not update its Network information.

c. The third Controller probes all existing nodes in the network.

d. The third Controller is included as a Secondary Inclusion Controller.

5. The third Controller (Secondary Inclusion Controller) includes the second AL End Node to the
Network.

a. The Inclusion Controller requests an Automatic Controller Update before the Inclusion.

b. The Inclusion Controller requests a Reserved Node ID to the SIS.

c. The SUC/SIS Controller handles the secure Bootstrapping.

d. The second AL End Node probes all nodes in the network.

e. Only the SUC/SIS and Secondary Inclusion Controllers update their Network information.

6. The RealPrimary Controller starts the process to shift Roles

a. RealPrimary Controller requests an Automatic Network Update to the SIS.

b. It transfers all Node Info and Range info it holds to the Secondary controller.

c. The transference ends with a Transfer New Primary Completed command and Transfer
End.

7. The new RealPrimary Controller excludes the AL End Node.

a. It issues a New Node Registered Command to the SUC/SIS Controller.

b. The SUC Updates its Network Topology status.

8. The new Secondary Controller is removed from the Network.

a. The SUC/SIS is notified of this change.

b. The new RealPrimary Controller ends the exclusion issuing a Transfer End to NodeID 0.

9. The Secondary Controller is reincluded to the network through a repeater.

10. The AL End Node is included to the network managing Secure bootstrapping by the SUC/SIS
through repeaters.

11. The RAILTest device is configured as the End Node. The actual End Node is Powered Off.

12. The SUC/SIS assigns return routes to the RAILTest device for the different nodes in the command.


**3.67.4** **Pass** **Criteria**


1. End Nodes shouldn’t calculate routes on their own, since they don’t have a full topology of
the network. They may request information to the SUC using Static Route Request command
following Figure 4.93. The SUC should assign nwkRecommendedNumberOfReturnRoutes return
routes for each NodeID in the command (NWK:01FC.1, NWK:01FD.1, NWK:01FE.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 149


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025


**3.67.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 150


Specifcations **Z-Wave** **Network** **Test** **Specifcation,** **Release** **3.9.0** May 30, 2025

## References


[ITUTG9959] ITU-T G.9959. Short range narrow-band digital radiocommunication transceivers PHY, MAC, SAR and LLC layer specifications. [Online]. URL: [https://www.itu.int/](https://www.itu.int/rec/T-REC-G.9959-201501-I)
[rec/T-REC-G.9959-201501-I.](https://www.itu.int/rec/T-REC-G.9959-201501-I)

[ZWAMACTEST] ZWA MAC_TEST. Z-Wave Alliance Z-Wave MAC Layer Test Specificaiton. [Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWANWK] ZWA NWK. Z-Wave Alliance Z-Wave and Z-Wave Long Range Network Layer Specification. [Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWAPHYTEST] ZWA PHY_TEST. Z-Wave Alliance Z-Wave PHY Layer Test Specification. [Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 151


