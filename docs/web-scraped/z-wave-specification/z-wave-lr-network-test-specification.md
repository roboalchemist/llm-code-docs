# **Test Specification**

_**Release**_ _**2.9.0**_

## **Z-Wave Alliance**


**May** **30,** **2025**

## Table of contents


1 Preamble 4
1.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Revision Record . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.4 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6


2 INTRODUCTION 7
2.1 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Audience and Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


3 NETWORK-LAYER TEST CASE DESCRIPTIONS 8
3.1 General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2 Command Frames   - Z-Wave Long Range Protocol Command Class   - No Operation
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.2.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.3 Command Frames – Z-Wave Long Range Protocol Command Class – Node Information
Frame Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.4 Command Frames   - Z-Wave Long Range Protocol Command Class   - Request Node
Information Frame Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


3.4.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.5 Command Frames - Z-Wave Long Range Protocol Command Class - Assign IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.5.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.5.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.5.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.5.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.5.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.6 Command Frames - Z-Wave Long Range Protocol Command Class - Exclude Request
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.6.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.6.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.6.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.6.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.6.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.7 Command Frames - Z-Wave Long Range Protocol Command Class - SmartStart Included Node Information Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.7.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.7.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.7.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.7.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.7.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.8 Command Frames – Z-Wave Long Range Protocol Command Class – SmartStart Prime
Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.8.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.8.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.8.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.8.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.8.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.9 Command Frames - Z-Wave Long Range Protocol Command Class - SmartStart Inclusion Request Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.9.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.9.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.9.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.9.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.9.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.10 Command Frames - Z-Wave Long Range Protocol Command Class - Exclude Request
Confirmation Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.10.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.10.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.10.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.10.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.10.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.11 Command Frames - Z-Wave Long Range Protocol Command Class - Non-Secure Inclusion Step Complete Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.11.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.11.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.11.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.11.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.11.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.12 Compliance with Z-Wave Long Range NWK Layer Constants and Attributes . . . . . 29
3.12.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.12.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.12.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.12.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.12.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.13 Functional Description - Communication between Z-Wave Long Range nodes . . . . . 31
3.13.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


3.13.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.13.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.13.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.13.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.14 Functional Description  - Z-Wave Long Range Network Formation & Learn Mode. . . 32
3.14.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.14.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.14.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.14.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.14.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.15 Functional Description  - Z-Wave Long Range SmartStart . . . . . . . . . . . . . . . . 34
3.15.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.15.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.15.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.15.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.15.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.16 Functional Description  - Z-Wave Long Range Network Exclusion . . . . . . . . . . . . 36
3.16.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.16.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.16.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.16.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.16.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.17 Functional Description  - Z-Wave Long Range Network Exclusion from a foreign Network 38

3.17.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.17.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.17.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.17.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.17.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.18 Functional Description  - Z-Wave Long Range Dual Z-Wave and Z-Wave Long Range
Networks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.18.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.18.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.18.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.18.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.18.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.19 (3.5  - Negative Testing) Command Frames  - Z-Wave Long Range Protocol Command
Class     - Assign IDs Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.19.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.19.2 Test Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.19.3 Test Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.19.4 Pass Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.19.5 Fail Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43


References 44


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 3


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 1 Preamble 1.1 Description


Test Specification for the network layer of the Z-Wave Long Range protocol

Reviewed by the Z-Wave Alliance Core Stack Working Group (CSWG) and approved by the Z-Wave
Alliance Board of Directors.

## 1.2 Disclaimer


THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 4


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 1.3 Revision Record


Table 1.1: Revision History











© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 5


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 1.4 Abbreviations


Table 1.2: Abbreviations


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 6


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 2 INTRODUCTION 2.1 Purpose


The purpose of this document is to provide a set of tests that verifying compliance with the Network
layer of the Z-Wave Long Range protocol.

## 2.2 Audience and Prerequisites


Developers and testers of the Z-Wave Long Range protocol.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 7


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3 NETWORK-LAYER TEST CASE DESCRIPTIONS 3.1 General Assumptions


This test specification assumes that the PHY and MAC layers are functional and comply to the Z-Wave
Long Range PHY/MAC specification [ZWAPHYMAC] and has been verified with the test cases found
in the Z-Wave Long Range PHY and MAC test specifications. [ZWALPHYTEST] [ZWALMACTEST].

All components are defined by the Z-Wave and Z-Wave Long Range Network Layer Specification

[ZWANWK] and that document is the sole reference for this test specification.

For Long Range Inclusion in all instances, when the DSK of the device is introduced, in the Provisioning List view, the “Long Range” check mark should be enabled. Otherwise, the device will be
included using regular Smart Start without Long Range capabilities.

Test Cases towards the end of the spec are the Negative Testing complement to Test Cases described
earlier, they show the number and title of the Test Case they relate to for identification. These
Negative Testing Test Cases, at the current time of issuing of this spec, are not mandatory.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 8


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.2 Command Frames – Z-Wave Long Range Protocol Command Class – No Operation Command


All frames commanding the Z-Wave Long Range network function and maintenance functionalities
are constructed in a standard way.

The No Operation (NOP) Command is used to test the availability of a node in a network.


**3.2.1** **Prerequisites**


 - 1 x Z-Wave Long Range Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR NL End Node.

 - 1 x Z-Wave LR FL End Node.

 - 1 x Z-Wave LR AL End Node.


**3.2.2** **Test** **Setup**


1. The DSK of the LR AL End Node is entered into the Controllers Provisioning List.

2. The LR AL End Node is in direct range of the Controller and is powered up.

3. Include the LR AL End Node to the Controller’s network using SmartStart.

4. Send a singlecast to the LR AL End Node from the Controller with Payload = 0x0400 (NOP).

5. The Controller is set into Learn Mode Exclude.

6. The LR AL End Node enters Learn mode and is excluded from the Controllers Network.

7. Redo the Whole Test for the LR FL and LR NL End Node to go through all Pass Criteria.


**3.2.3** **Test** **Result**


3. The LR AL End Node is Successfully included to the Controllers Network using SmartStart.

4. A No Operation Frame is sent from the Controller to the LR AL End Node.

a. Observe that the LR AL End node answers with a Mac Layer acknowledgement frame,
notifying the Controller that the End Node is functional.

6. The LR AL End Node is Excluded from the Controllers Network.

a. The Controller Sends a NOP frame to the LR AL End Node to verify that the device has
been excluded from the network.

b. The LR AL End Node is excluded from the Network and does therefore not send an
Acknowledgement.

7. The FL and NL End Node will create the same overall test results as the LR AL End Node.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 9


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.2.4** **Pass** **Criteria**


1. The singlecast command is constructed as described by figure 6.3 (LR-NWK:000F.1).

2. The singlecast command has no additional encryption and has no additional payload from upper
layers (LR-NWK:000B.1).

3. All Command classes from 0x00  - 0x1F are NWK command classes, so it’s ID is within that
interval (LR-NWK:000C.1).

4. This command shall be sent using singlecast addressing and shall not be sent using broadcast
addressing   - This can be verified using the Z-Wave Long Range Sniffer (LR-NWK:0010.1).

5. This Command may be used to verifying if an excluded node is still part of the network. This
Command may also be used on application level e.g. checking if a node is still operational
(LR-NWK:000F.1).

6. The NOP frame is answered by the End Node regardless of the type of End Node. It has no
payload (LR-NWK:0011.1).

7. The End Nodes shall not do anything other than sending a MAC Layer acknowledgement notifying the Controller that the End Node is functional (LR-NWK:0012.1).

8. It is used as a probing tool and it can be seen both in the inclusion process and in the exclusion
process (LR-NWK:0011.1).


**3.2.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters in the NOP frame causes successful results when
they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 10


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.3 Command Frames – Z-Wave Long Range Protocol Command Class – Node Information Frame Command


All frames commanding the Z-Wave Long Range network function and maintenance functionalities
are constructed in a standard way. This will not be mentioned for further test cases and it is expected
to be true for all test cases part of this document.

This Command Class is used for Setup and Maintenance of Networks. The Node Information Frame
command is used to advertise the capabilities of the sending node.


**3.3.1** **Prerequisites**


 - 1 x Z-Wave Long Range Capable Sniffer.

 - 1 x Z-Wave LR capable Controller.

 - 1 x Z-Wave LR FL End Node.

 - 1 x Z-Wave LR AL End Node

 - 1 x Z-Wave LR NL End Node


**3.3.2** **Test** **Setup**


1. The DSK of the LR AL End Node is entered into the Controllers Provisioning List.

2. The LR AL End Node is in direct range of the Controller and is powered up.

3. Include the LR AL End Node to the Controller’s network using SmartStart.

4. Send Request Node Info from the Controller to the LR AL End Node.

5. The LR AL End Node sends a Node Information Frame to the Controller.

6. Make the Controller send out its own Node Information Frame using API or GUI.

7. Redo the Whole Test for the FL and NL End Nodes to go through all Pass Criteria.


**3.3.3** **Test** **Result**


3. LR AL End Node is included successfully to the network using SmartStart.

4. A Send a Request Node Info is sent from the Controller to the End Node.

5. The LR AL End Node’s NIF is sent as singlecast.

6. The Controller’s NIF is broadcasted.

7. The LR FL and LR NL End Nodes will create the same overall test results as the LR AL End
Node.

Here it should be noted that for the LR NL End Node shall be woken up for it to be able to
answer the Request Node Info frame.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 11


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.3.4** **Pass** **Criteria**


1. The singlecast commands are constructed as described by figure 6.2 (LR-NWK:000A.1).

2. The singlecast commands have no additional encryption and have no additional payload from
upper layers (LR-NWK:000B.1).

3. All Command classes from 0x00  - 0x1F are NWK command classes, so it’s ID is within that
interval (LR-NWK:000C.1).

4. Z-Wave Long Range Protocol Command Class shall be supported by all nodes
(LR-NWK:000D.1).

5. The Node Information Frame Command is formatted as per Table 6.4 (LR-NWK:0013.1):

a. Supported Speed (Max Baud Rate) field consists of 3 bits and should hold at least one
of the values from Table 6.5       - Here it is expected that all reserved fields are set to zero
(LR-NWK 0088.1).

b. Listening Bit advertises if the node Listens or Not. AL nodes shall set this field to 1
(NWK:006C.1)     - See (LR-NWK:0014.1) for reference (Same field as for Z-Wave).

c. Listening bit is set to 0 by NL and FL nodes (NWK:006D.1)      - See (LR-NWK:0014.1) for
reference (Same field as for Z-Wave).

d. The Controller bit determines if the emitting node is a Controller by setting it to 1, or if
it’s not by setting it to 0. This test has used only End Nodes so they should be set to 0
(NWK:0070.1)     - See (LR-NWK:0014.1) for reference (Same field as for Z-Wave).

e. The Sensor 1000ms bit should be set to 0, if the End Node is not a Z-Wave Long Range
FLiRS device and 1 if the Device is a Z-Wave Long Range FliRS device. (NWK:0077.1)     See (LR-NWK:0014.1) for reference (Same field as for Z-Wave).

f. Command Class Bytes list the Supported Command Classes. It shall not be longer
than 35 bytes. The Command Classes are in the range 0x21… 0xFFFF. Command
Classes in the Range 0x00 … 0x20 are not advertised (LR-NWK:0016.1, LR-NWK:0017.1,
LR-NWK:0018.1).

6. For the End Nodes, when they send their NIF: Its format matches the one described in the
Criteria 5.a    - 5.f. And the Data of the NIF shall be forwarded to the upper protocol layer of
the nodes within range (LR-NWK:0019.1).

7. When the Controller sends its NIF, its format is mostly the same as 5.a – 5.f but for the following
differences:

a. The Controller bit is set to 1 and the Node Information Frame includes a Basic Device
Type field (NWK:0070.1, NWK:0071.1)     - See (LR-NWK:0014.1) for reference (Same field
as for Z-Wave).


**3.3.5** **Fail** **Criteria**


1. The singlecast commands are NOT constructed as described by figure 6.2 (LR-NWK:000A.1).

2. The singlecast commands have additional encryption or have additional payload from upper
layers (LR-NWK:000B.1).

3. The command’s class ID of inclusion frames are higher than 0x1F (LR-NWK:000C.1).

4. The device does not support Z-Wave Long Range Protocol Command Class (LR-NWK:000D.1).

5. The Node Information Frame is not formatted as per Table 6.4 (LR-NWK:0013.1):

a. Supported Speed (Max Baud Rate) field is either more or less than of 3 bits or does not
hold any value from Table 6.5 (LR-NWK 0088.1), which is not reserved      - The reserved
fields are not set to zero.

b. The End Node sets its Listening Bit to 0 if it’s an AL node (NWK:006C.1)     - See
(LR-NWK:0014.1) for reference (Same field as for Z-Wave).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 12


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


m. The End Node sets its Listening Bit to 1 if it’s either an FL or NL node (NWK:006D.1)    See (LR-NWK:0014.1) for reference (Same field as for Z-Wave).

d. The Controller bit is set to 0 for the Controller or 1 for End Nodes (NWK:0070.1,
NWK:0072.1)     - See (LR-NWK:0014.1) for reference (Same field as for Z-Wave).

e. The Sensor 1000ms bit is set to 0, for a Z-Wave Long Range FLiRS device or if the bit is set
to 0 for a non-Z-Wave Long Range FLiRS device. (NWK:0077.1)      - See (LR-NWK:0014.1)
for reference (Same field as for Z-Wave).

f. Command class bytes are more than 35 bytes. Or Their values are outside the range 0x21…
0xFFFF. Or it advertises Command Classes in the Range 0x00 … 0x20 (LR-NWK:0016.1,
LR-NWK:0017.1, LR-NWK:0018.1).

6. When the Controller sends its NIF, its format met any of the failing conditions 5.a  - 5.e.

7. Any of the passing criteria is not met.

8. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 13


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.4 Command Frames – Z-Wave Long Range Protocol Command Class – Request Node Information Frame Command


This command is used to request a node to return a Node information Frame Command.

_For_ _future_ _Test_ _Cases_ _it_ _might_ _be_ _specified_ _that_ _a_ _node_ _is_ _included_ _using_ _SmartStart,_ _it_ _is_ _assumed_ _that_
_the_ _DSK_ _of_ _the_ _node_ _being_ _included_ _is_ _already_ _included_ _into_ _the_ _Controller_ _Provisioning_ _List_ _and_ _the_
_node_ _is_ _in_ _direct_ _range_ _of_ _the_ _Controller._


**3.4.1** **Prerequisites**


 - 1 x Z-Wave Long Range Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.

 - 1 x Frame Generator.


**3.4.2** **Test** **Setup**


1. The DSK of the End Node is entered into the Controllers Provisioning List.

2. The End Node is in direct range of the Controller and is powered up.

3. Include the End Node to the Controller’s network using SmartStart.

4. Send Request Node Information Frame to End Node.

5. Send Request Node Information Frame to End Node as multicast.

6. Configure the Frame generator to send Request Node Information Frame to the Controller as a
singlecast as if it was sent from the End Node.

7. Configure the Frame generator to send Request Node Information Frame to the Controller as a
multicast as if it was sent from the End Node.


**3.4.3** **Test** **Result**


3. End Node is included successfully to the network using SmartStart.

4. The End Node answers with a Node Information Frame as a singlecast.

5. The End Node does not answer the request that was sent as a multicast.

6. The Controller answers the request that was sent as a singlecast.

7. The Controller does not answer the request that was sent as a multicast.


**3.4.4** **Pass** **Criteria**


1. The singlecast command is constructed as described by figure 6.2 (LR-NWK:000A.1).

2. The singlecast command has no additional encryption and has no additional payload from upper
layers (LR-NWK:000B.1).

3. All Command classes from 0x00  - 0x1F are NWK command classes, so it’s ID is within that
interval (LR-NWK:000C.1).

4. The Request Node Information Frame Command is formatted as per Table 6.6
(LR-NWK:001A.1).

5. This command is only sent as a singlecast for both receiving nodes (LR-NWK:001B.1)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 14


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


6. The receiving node returns a Node Information Frame Command in response to the singlecast
command and ignores it when it’s sent as a multicast for both receiving nodes (LR-NWK:001D.1,
LR-NWK:001E.1).

7. The End Node answers the singlecast Request Node Information with a Node Information Frame
that follows the same format as described in Pass Criteria 5 of the previous Test Case.

8. The Controller answers the singlecast Request Node Information with a Node Information Frame
that follows the same format as described in Pass Criteria 7 in the previous Test Case.


**3.4.5** **Fail** **Criteria**


1. The singlecast command is NOT constructed as described by figure 6.2 (LR-NWK:000A.1).

2. The singlecast command has additional encryption or has additional payload from upper layers
(LR-NWK:000B.1).

3. The command’s class ID is higher than 0x1F (LR-NWK:000C.1).

9. The request Node Information Frame Command does not follow the format of Table 6.6
(LR-NWK:001A.1).

4. The command is sent as multicast by default for either receiving node (LR-NWK:001B.1)

5. Either of the receiving nodes answers to the Request Node Information Command with a
Node Information Frame regardless if it was sent as singlecast or multicast (LR-NWK:001D.1,
LR-NWK:001E.1).

6. The End Node answers with a Node Information Frame that meets any of the fail conditions
from the Fail Criteria 4 in the previous Test Case.

7. The Controller answers with a Node Information Frame that meets any of the fail conditions
from the Fail Criteria 5 in the previous Test Case.

8. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 15


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.5 Command Frames – Z-Wave Long Range Protocol Command Class – Assign IDs Command


This command is used to assign NodeID and HomeID to the receiving node.


**3.5.1** **Prerequisites**


 - 1 x Z-Wave Long Range Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.


**3.5.2** **Test** **Setup**


1. Include the End Node to the Controller’s network using SmartStart.

2. Send Assign ID command to End Node as a singlecast after inclusion.

3. Send Assign ID command to End Node as a multicast after inclusion.

4. Remove the End Node from the Controller’s network.


**3.5.3** **Test** **Result**


1. End Node is included successfully to the Controller’s Network.

2. End Node answers the singlecast Assign ID command with an Ack frame only after the Inclusion.

3. End Node ignores the multicast Assign ID.

4. End Node is removed from the network, to make sure it’s reset and ready for a new inclusion.


**3.5.4** **Pass** **Criteria**


1. During SmartStart inclusion of the End Node and the Controller, the “Assign ID” command is
sent as a singlecast and follows the format as per Table 6.7 (LR-NWK:001F.1, LR-NWK:0023.1).

2. The NodeID field of the command is not 0x00 and between 0x100..0xFA0 . (LR-NWK:0026.1,
LR-NWK:0021.1).

3. The HomeID values are not displayed in the Sniffer but are found in the frame. They match
the HomeID of the Network of the Controller in both cases (LR-NWK:0022.1).

4. The End Node accept both HomeID and NodeID as they have been put in SmartStart Learn
Mode and its inclusion is successful (LR-NWK:0024.1).

5. The End Node ignore the command once they have been included to the network and they are
no longer in SmartStart learning mode (LR-NWK:0024.1).

6. When the nodes are removed, the NodeID is set to 0x00 and the HomeID to the NWI HomeID
(LR-NWK:0072.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 16


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.5.5** **Fail** **Criteria**


1. The “Assign ID” command does not comply with the specified formant nor it’s sent as a singlecast
by default (LR-NWK:001F.1, LR-NWK:0023.1)

2. The NodeID field is set to 0x00 during inclusion or it’s not in-between 0x100 and 0xFA0
(LR-NWK:0021.1).

3. The HomeID values don’t match the HomeID of the Controller’s network (LR-NWK:0022.1).

4. The End Node don’t accept the command regardless of being set in SmartStart learning mode
(LR-NWK:0022.11).

5. The End Node change their Node ID or Home ID when receiving the “Assign ID” command
after being SmartStart included even if they are not in learning mode (LR-NWK:0024.1).

6. The NodeID and HomeID are not set by default to 0x00 when removing the nodes
(LR-NWK:0072.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 17


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.6 Command Frames – Z-Wave Long Range Protocol Command Class – Exclude Request Command


This command is used by a node looking to be excluded from its current network.


**3.6.1** **Prerequisites**


 - 1 x Z-Wave Long Range Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.


**3.6.2** **Test** **Setup**


1. Include the End Node to the Controller using SmartStart.

2. The Controller is put into Exclude Mode.

3. The End Node is put into Learn Mode Exclude.

4. The Exclude Request is sent to the broadcast destination (Node ID 0xFFF) from the End Node.

5. Include the End Node to the Controller using SmartStart.

6. The End Node is put into Learn Mode Exclude.

7. The Exclude Request is sent to the broadcast destination (Node ID 0xFFF) from the End Node.


**3.6.3** **Test** **Result**


1. The End Node is included in direct range to the Controller using SmartStart.

2. The Controller is put into Exclude Mode.

3. The Exclude request is send from the End Node to the broadcast destination (Node ID 0xFFF)
and is received by the Controller.

4. The Controller Answers with a Exclude Request Confirmation Command sent to the End Node.

a. The End Node is Excluded successfully from the Controllers Network.

5. The End Node is included in direct range to the Controller using SmartStart.

7. The Exclude request is send from the End Node to the broadcast destination (Node ID 0xFFF)
and is received by the Controller.

a. The Controller Ignores the Exclude Request, because it’s not trying to exclude, and the
End Node is not excluded from the Network.


**3.6.4** **Pass** **Criteria**


1. The format of the command follows the Table 6.8 (LR-NWK:0027.1).

2. This command extends its fields from the Node Information Frame (LR-NWK:0029.1).

3. This command is sent as a broadcast frame and is broadcasted to direction 0xFFF
(LR-NWK:0028.1).

4. This command proceeds to exclude a node only if currently in exclusion mode, it ignores the
command, otherwise (LR-NWK:002B.1, LR-NWK:002C.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 18


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.6.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 19


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.7 Command Frames – Z-Wave Long Range Protocol Command Class – SmartStart Included Node Information Command


This command is used by nodes to notify a controller that it was just powered up and is already part
of a network.


**3.7.1** **Prerequisites**


 - 1 x Z-Wave Long Range Capable Sniffer.

 - 2 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.


**3.7.2** **Test** **Setup**


1. Add the DSK number of the End Node to Controller-1s’ Provisioning List.

2. Make sure the End Node is in direct range of the Controller and power it up.

3. Let SmartStart inclusion of the End Node finish.

4. Remove power from the End Node.

5. Add the DSK number of the End Node to Controller-2.

6. Return power to the End Node.


**3.7.3** **Test** **Result**


3. The End Node is included to Controller-1’s network using SmartStart.

4. The End Node is powered down.

5. The Controller-2 holds the DSK of the End Node in its Provisioning List.

6. The End Node is powered up and emits a broadcast frame with the Included Node Info Command.

a. The Controller-2 does not attempt including the End Node.


**3.7.4** **Pass** **Criteria**


1. The SmartStart Included Node Information command follows the format from Table 6.9
(LR-NWK:002D.1).

2. The “NWI HomeID” field identifies that the Node has been included to the network with that
HomeID (Follows the same format as Z-Wave: NWK:0163.1).

3. The format of the bytes forming the “NWI HomeID” field is structured to match bytes 9 …
12 of the S2 DSK. Bits 7 & 6 of the “NWI HomeID 1” field are set to 1. Bit 0 of the “NWI
HomeID 4” field is set to 0   - Illustrated by Figure 4.55 (Follows the same format as Z-Wave:
NWK NWK:0164.1, NWK:0165.1, NWK:0166.1).

4. This SmartStart Include Node Information Frame is transmitted in a broadcast Frame and it’s
broadcasted to NodeID 0xFFF (LR-NWK:002E.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 20


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.7.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 21


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.8 Command Frames – Z-Wave Long Range Protocol Command Class – SmartStart Prime Command


This command is used to notify SmartStart including controllers that a node is about to make an
inclusion request.


**3.8.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR AL End Node.

 - 1 x Z-Wave LR FL End Node.

 - 1 x Z-Wave LR NL End Node.

_All_ _Z-Wave_ _Long_ _Range_ _Network_ _Layer_ _constant_ _used_ _in_ _this_ _test_ _case_ _can_ _be_ _found_ _in_ _table_ _6.4_
_(LR-NWK:0048.1)._


**3.8.2** **Test** **Setup**


1. Introduce the DSK value of the End Nodes into the Controller’s Provisioning List.

2. Power up the End Nodes.


**3.8.3** **Test** **Result**


1. The DSK of the End Nodes is in the Controller’s Provisioning List.

2. The End Nodes each issue a SmartStart Prime Command.

a. AL & FL nodes wait until their wakeup period is completed and then they send SmartStart
Prime Command after nwkSmartStartInclusionRequestDuration has passed.


**3.8.4** **Pass** **Criteria**


1. The format of the SmartStart Prime Command follows the format from figure 6.9 and it extends
from the Node Information Frame (LR-NWK:0030.1, LR-NWK:0031.1).

2. This command is sent in a broadcast frame, it must be addressed as a broadcast to node 0xFFF.
Must hold the NWIHomeID as HomeID. It is sent after nwkSmartStartInclusionRequestDuration has passed. Non-AL nodes may return to sleep between sending SmartStart Prime
Command and SmartStart Inclusion Request Command (LR-NWK:0032.1, LR-NWK:0033.1,
LR-NWK:0034.1, LR-NWK:0035.1).

3. When it’s received, the Controller compares the NWIHomeID to the one obtained in the DSK
keys in its Provisioning List. When finding a match, the Controller enters SmartStart Inclusion
when the node issues a SmartStart Inclusion Request. IF there are more DSK matches for the
received NWIHomeID, the Controller shall enter SmartStart Inclusion alternating between the
DSK candidates (LR-NWK:0036.1, LR-NWK:0037.1, LR-NWK:0038.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 22


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.8.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 23


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.9 Command Frames – Z-Wave Long Range Protocol Command Class – SmartStart Inclusion Request Command


This command is used to request to initiate a SmartStart inclusion.


**3.9.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR AL End Node.

 - 1 x Z-Wave LR FL End Node.

 - 1 x Z-Wave LR NL End Node.

_All_ _Z-Wave_ _Long_ _Range_ _Network_ _Layer_ _constant_ _used_ _in_ _this_ _test_ _case_ _can_ _be_ _found_ _in_ _table_ _6.14_ _and_
_table_ _6.15_ _(LR-NWK:0048.1,_ _LR-NWK:0049.1)._


**3.9.2** **Test** **Setup**


1. Introduce the DSK value of the End Nodes into the Controller’s Provisioning List.

2. Power up the End Nodes.


**3.9.3** **Test** **Result**


1. The DSK of the End Nodes is in the Controller’s Provisioning List.

2. The End Node each issue a SmartStart Prime Command.

a. AL & FL nodes wait until their wakeup period is completed and then they send SmartStart
Prime Command after nwkSmartStartInclusionRequestDuration has passed.

b. After the End Nodes have issued SmartStart Prime, they issue SmartStart Inclusion Request.

c. When the Controller receives SmartStart Inclusion Request, it will initiate SmartStart
inclusion by issuing the Assign ID Command.


**3.9.4** **Pass** **Criteria**


1. The format of the SmartStart Inclusion Request Command follows the format from figure 6.10
and it extends from the Node Information Frame (LR-NWK:0039.1, LR-NWK:003A.1).

2. This command is sent in an inclusion broadcast frame, it must be addressed as a broadcast
to node 0xFFF. Must hold the NWIHomeID as HomeID. The Sending node shall listen and
accept Assign IDs Command after the HomeID has been authenticated (LR-NWK:003B.1,
LR-NWK:003C.1, LR-NWK:003D.1).

3. When it’s received, the Controller compares the NWIHomeID to the one obtained in the DSK
keys in its Provisioning List. When finding a match the Controller begins SmartStart Inclusion
by issuing AssignID and it should authenticate the HomeID by constructing the 4 bytes of
NWIHomeID matching bytes 13 … 16 of the DSK, in its bits 7 & 6 of the Auth HomeID byte 1
are set to 1 and bit 0 of Auth HomeID byte 4 is set to 0 as per Figure 3.58 (LR-NWK:003E.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 24


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.9.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 25


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.10 Command Frames – Z-Wave Long Range Protocol Command Class – Exclude Request Confirmation Command


_The_ _Exclude_ _Request_ _Confirmation_ _Command_ _is_ _used_ _by_ _a_ _controller_ _node_ _to_ _confirm_ _to_ _a_ _node_ _that_
_it_ _can_ _leave_ _the_ _current_ _network._


**3.10.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.


**3.10.2** **Test** **Setup**


1. Introduce the DSK value of the End Node into the Controller’s Provisioning List.

2. Power up the End Node.

3. The End Node is included into the Controller Network using SmartStart.

4. The Controller sends a Exclude Request Confirmation command to the End Node.

5. Exclude the End Node from the network by setting the Controller in Learn Mode Exclude
followed by setting the End Node in Learn Mode and it expected network exclusion.


**3.10.3** **Test** **Result**


1. The DSK of the End Nodes is in the Controller’s Provisioning List.

3. The End Node is included into the network using SmartStart.

4. The End Node receives a Exclude Request Confirmation from the Controller and ignores the
command, because it’s not in Learn Mode Exclude.

5. The Controller is put into Learn Mode Exclude. The End Node sends out a Exclude Request
Command.

a. The Controller then sends a Exclude Request Confirmation Command to the End Node.
The Exclude Request Confirmation with the NodeID of the End Node sending the Exclude
Request Command and HomeID of the node sending the Exclude Request Command.

b. The Exclude Request Confirmation Command is then Acknowledged by the End Node.

c. The Controller sends out a No Operation Command Frame, if this is not acknowledged by
the End Node. The End Node have successfully been excluded.


**3.10.4** **Pass** **Criteria**


1. The format of the Exclude Request Confirmation Command follows the format from figure 6.11
(LR-NWK:003F.1).

2. The Exclude Request Confirmation Command is ignored, when the End Node is not in Learn
Mode Exclude. (LR-NWK:0043.1)

3. The Exclude Request Confirmation Command is sent to the End Node, which have issued a
Exclude Request. (LR-NWK:0040.1)

4. The controller has been instructed to exclude a node from a Z-Wave Long Range Network.
(LR-NWK:0041.1)

5. After the End Node have received the Exclude Request Confirmation it shall leave its current
network. (LR-NWK:0042.1)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 26


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.10.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 27


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.11 Command Frames – Z-Wave Long Range Protocol Command Class – Non-Secure Inclusion Step Complete Command


The Non-Secure Inclusion Step Complete Command is used by a controller node to indicate to a
joining node that the non-secure part of the network inclusion is completed.


**3.11.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.

_All_ _Z-Wave_ _Long_ _Range_ _Network_ _Layer_ _constant_ _used_ _in_ _this_ _test_ _case_ _can_ _be_ _found_ _in_ _table_ _6.14_ _and_
_table_ _6.15_ _(LR-NWK:0048.1,_ _LR-NWK:0049.1)._


**3.11.2** **Test** **Setup**


1. Introduce the DSK value of the End Node into the Controller’s Provisioning List.

2. Power up the End Node.

3. The End Node is included securely using SmartStart.


**3.11.3** **Test** **Result**


1. The DSK of the End Node is in the Controller’s Provisioning List.

3. The End Node is included into the network using SmartStart.

a. During the SmartStart Inclusion a Non-Secure Inclusion Step Complete command is sent
from the Controller to the End Node to signal that the Non-Secure part of the inclusion is
over. This will initiate the S2 Security Bootstrapping.


**3.11.4** **Pass** **Criteria**


1. The format of Non-Secure Inclusion Step Complete Command follows the format from figure
6.12 (LR-NWK:0044.1).

2. The Controller shall after issuing this command initiate the S2 Bootstrapping.
(LR-NWK:0045.1)

3. The End Node shall start its S2 TB1 timer upon reception of this command and its instructed
that the non-secure inclusion is completed and that the S2 bootstrapping shall now take place.
(LR-NWK:0046.1, LR-NWK:0047.1)


**3.11.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 28


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.12 Compliance with Z-Wave Long Range NWK Layer Constants and Attributes


Tables 6.4 and 6.5 define the Constants and Attributes the Network Layer can use for different
procedures.


**3.12.1** **Prerequisites**


 - 1 x Z-Wave LR capable Sniffer.

 - 2 x Z-Wave LR capable Controller.

 - 1 x Z-Wave LR End Node.

_All_ _Z-Wave_ _Long_ _Range_ _Network_ _Layer_ _constant_ _used_ _in_ _this_ _test_ _case_ _can_ _be_ _found_ _in_ _table_ _6.14_ _and_
_table_ _6.15_ _(LR-NWK:0048.1,_ _LR-NWK:0049.1)._


**3.12.2** **Test** **Setup**


1. The End Node is powered up.

2. After a while the DSK of the End Node is added in Controller-1’s Provisioning List.

3. The End Node is included intoController-1’s network using SmartStart.

4. The End Node is then put into Learn Mode Exclude.

5. After a While Controller-1 is then also put into Remove Mode.

6. The End Node is then put into Learn Mode Exclude again and is excluded from Controller-1
network.

7. Introduce the DSK of the End Node in the Controller-2’s Provisioning List.

8. Controller-1 is set to Remove Mode.

9. The End Node is set into Learn Mode Exclude and excluded from the network of Controller-2
using Controller-1.


**3.12.3** **Test** **Result**


3. During the First Inclusion using SmartStart the following durations should be checked:

a. The duration between the SmartStart prime Command and the SmartStart Inclusion Request Command. (Constant: nwkSmartStartInclusionRequestDuration)

b. The duration between the SmartStart inclusion requests     - this is the reason for the late
insertion of the DSK. (Constant: nwkSmartStartInclusionBackoffDuration)

c. The maximum time interval between the SmartStart Inclusion Requests. (Attribute: aNwkSmartStartMaxInclusionRequestInterval)

d. After sending Assign ID Command count the number of No Operation Command. (Constant: nwkAssignIDConfirmationRetries)

e. Verify that the time between each command of the non-secure part of the network inclusion
for joining nodes. (Constant: nwkNonSecureInclusionCommandTimeout)

6. During the first Exclusion of the End Node the following durations should be checked.

a. Minimum duration in which a node shall stay in Learn Mode during Network Exclusion.
(Constant: nwkLearnModeMinDuration)

7. The End Node is included into Controller-2’s network.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 29


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


9. During the second Exclusion of the End Node from Controller-1, the following durations should
be check:

a. Minimum back-off for a controller after an Exclude Request command to issue a Exclude
Request Confirmation command on a foreign Network. (Constant: nwkLRExcludeRequestForeignNetBackOff)


**3.12.4** **Pass** **Criteria**


1. All values correspond to table 6.4 and 6.5 (LR-NWK:0048.1, LR-NWK:0049.1).


**3.12.5** **Fail** **Criteria**


1. Neither value corresponds to either table 6.4 or 6.5 (LR-NWK:0048.1, LR-NWK:0049.1).

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 30


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.13 Functional Description – Communication between Z-Wave Long Range nodes


Functional description of communication between Z-Wave Long Range nodes.


**3.13.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.

_All_ _Z-Wave_ _Long_ _Range_ _Network_ _Layer_ _constant_ _used_ _in_ _this_ _test_ _case_ _can_ _be_ _found_ _in_ _table_ _6.14_ _and_
_table_ _6.15_ _(LR-NWK:0048.1,_ _LR-NWK:0049.1)._


**3.13.2** **Test** **Setup**


1. The End Node is included into the Controllers Z-Wave Long Range Network using SmartStart.

2. The End Node is then powered off.

3. The Controller continuously sends a Request Node Information Frame Command for a minimum
of nwkMinTransmitAttempts.


**3.13.3** **Test** **Result**


1. The End Node is included into the Z-Wave Long Range Controllers Network using SmartStart.

a. The End Node and Controller are communicating only using direct range and operating on
a Z-Wave Long Range PHY/MAC.

2. The End Node is powered off.

3. The End Node is powered off and can’t reply any messages from the Controller continuously
sending a Request Node Information Frame Command. After nwkMinTransmitAttempts the
End Node is marked as a failing node on the Controller.


**3.13.4** **Pass** **Criteria**


1. All communication between the End Node and Controller use direct range with operation on a
Z-Wave Long Range PHY/MAC. (LR-NWK:004A.1)

2. The Controller node shall issue a minimum of nwkMinTransmitAttempts direct range frames to
the End Node before concluding that the destination is failing. (LR-NWK:004B.1)


**3.13.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 31


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.14 Functional Description – Z-Wave Long Range Network Forma- tion & Learn Mode.


Functional description of Z-Wave Long Range Network Formation and Learn Mode.


**3.14.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.

_All_ _Z-Wave_ _Long_ _Range_ _Network_ _Layer_ _constant_ _used_ _in_ _this_ _test_ _case_ _can_ _be_ _found_ _in_ _table_ _6.14_ _and_
_table_ _6.15_ _(LR-NWK:0048.1,_ _LR-NWK:0049.1)._


**3.14.2** **Test** **Setup**


1. Power on the Controller

2. Include the DSK of the End Node into the Controllers Provisioning List.

3. Power on the End Node.

4. The End Node is included into Controllers Network using SmartStart.

5. The Controller is put into Remove Mode.

6. The End Node is also set into Learn Mode Exclude

7. The End Node is removed from the Controllers Network.


**3.14.3** **Test** **Result**


1. The Controller is not belonging to a Network and shall therefore start a new Z-Wave Long Range
Network by assigning itself with a HomeID and the NodeID 0x01. The HomeID (aNwkRandomHomeID) shall be generated using a random number generator.

2. The End Nodes DSK is inserted into the Controllers Provisioning List.

3. The End Node is powered up and is not part of a network and shall therefore wait until it gets
included into a network by a controller node. And until the End Node gets included into a
network it shall assign their NWI HomeID to itself.

4. The End Node is Included to the Controller network using SmartStart.

5. The Controller enters Remove Mode for a minimum period of nwkLearnModeMinDuration.

6. The End Node also enters Learn Mode Exclude.

7. The End Node is Excluded from the Controller Network


**3.14.4** **Pass** **Criteria**


1. The Controller starts Z-Wave Long Range Network and Assigns itself a HomeID and NodeID
0x01. The HomeID shall be generated using a random number generator. (LR-NWK:0053.1,
LR-NWK:0054.1)

2. The End Node shall not start a new network and shall wait until it gets included in a network
by a controller and shall assign itself with its NWI HomeID until it is included. This Controller
is now the Primary Controller. (LR-NWK:0051.1, LR-NWK:0052.1)

3. The Controller enters Learn Mode Exclude only when necessary. (LR-NWK:004E.1)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 32


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


4. The End Nodes enters Learn Mode Exclude for a minimum duration of nwkLearnModeMinDuration. (LR-NWK:004F.1)

5. The End Node is excluded from the Network.


**3.14.5** **Fail** **Criteria**


1. Any of the passing criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 33


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.15 Functional Description – Z-Wave Long Range SmartStart


SmartStart allows for an automatic inclusion if the user holds the DSK number of the device.


**3.15.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 2 x Z-Wave LR Capable Controller. (Controller-1 and Controller-2)

 - 2 x Z-Wave LR End Node. (End Node-1 and End Node-2)

 - 1 x End Node supporting both Z-Wave and Z-Wave Long Range. (End Node-3)


**3.15.2** **Test** **Setup**


1. Take the DSK from End Node-1 and add it to the Provisioning List of the Controller-1.

2. Place the End Nodes in direct range of both the Controllers.

3. Power on both the End Nodes.

4. The End Node-1 is included using SmartStart into the Controller-1s’ network.

5. Take the DSK from End Node-3, which support both Z-Wave and Z-Wave Long Rang and add
it to the Provisioning List of the Controller-1.

6. Power up End Node-3.

7. End Node-3 is included into the Controller-1s’ network using SmartStart and is Included as a
Z-Wave Long Range Device.


**3.15.3** **Test** **Result**


1. The DSK of the End Node-1 is included in Controller-1’s Provisioning List.

2. The End Nodes are in direct Range of both the Controllers, where only Controller-1 have its
DSK in its Provisioning List.

3. When the End Nodes 1 & 2 are powered up:

a. The End Node-2 is powered up and continuously send SmartStart Prime Commands and
SmartStart Inclusion Requests.

b. The End Node-1 is Powered up and sends a SmartStart Prime Command, which is then
Acknowledged by the Controller.

4. The End Node-1 then sends a SmartStart Inclusion Request Command and the SmartStart
inclusion is initiated.

a. The End Node-1 is Successfully included by Controller-1 and all the messages are ignored
by Controller-2.

5. The DSK of the End Node-3 is included in Controller-1’s Provisioning List.

6. The End Node-3 is powered up.

a. After Wakeup the End Node-3 issue SmartStart Prime and SmartStart Inclusion Request
both on the Z-Wave and Z-Wave Long Range channels.

7. End Node-3 is included into the Controller-1s’ network using SmartStart and is Included as a
Z-Wave Long Range Device.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 34


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.15.4** **Pass** **Criteria**


1. SmartStart supporting nodes go into SmartStart Learn Mode right as they are powered up
(LR-NWK:0055.1).

2. After powering up, node shall initiate SmartStart inclusion depending on their state
(LR-NWK:0056.1

3. A node Capable of operating both in Z-Wave and Z-Wave Long Range shall issue SmartStart
Prime and SmartStart Inclusion Request both on the Z-Wave and Z-Wave Long Range channels.
(LR-NWK:0056.1)

4. When a node is not part of a network, it shall issue SmartStart Prime and SmartStart Inclusion
Request in intervals (LR-NWK:0058.1, LR-NWK:0059.1).

5. SmartStart Inclusion request follows Figure 6.3 (LR-NWK:005A.1).

6. Nodes requesting SmartStart Inclusion do so as per Table 4.29 (NWK:01B3.1).

7. A node already included in a network sends a single SmartStart Included node Information upon
power up as per Figure 6.4 (LR-NWK:005D.1).

8. A Controller shall be Primary Controller to include nodes via SmartStart. (LR-NWK:005E.1)

9. A Controller needs the DSK of a node to include it via SmartStart (LR-NWK:005F.1).

10. A Controller including via SmartStart shall perform S2 bootstrapping (LR-NWK:0060.1).

11. Direct Smart Start inclusion follows Figure 6.5 (LR-NWK:0061.1).

12. When S2 bootstrapping fails, SmartStart Inclusion is considered failed (LR-NWK:0062.1,
LR-NWK:0063.1).

13. A node that fails being included leaves the network and considers itself not included to any
network and shall return to SmartStart Learn Mode (LR-NWK:0069.1, LR-NWK:006A.1).

14. A Controller that fails including a node, should consider the joining node removed from the
network. It may verify by issuing NOP commands (LR-NWK:006B.1, LR-NWK:006C.1).


**3.15.5** **Fail** **Criteria**


1. Any of the passing Criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 35


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.16 Functional Description – Z-Wave Long Range Network Exclu- sion


Nodes exit a Z-Wave Long Range network using direct range Network Exclusion.


**3.16.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 2 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.


**3.16.2** **Test** **Setup**


1. Take the DSK from the End Node and add it to the Provisioning List of the Controller.

2. Place the End Node in direct range of the Controller.

3. The End Node is included using SmartStart into the Controllers’ network.

4. The Controller is set into Z-Wave Long Range Network Exclusion

5. The End Node is inserted into Learn Mode and Expects network Exclusion.

6. The End Node is excluded from the network.

7. Set the second Controller in Learning Mode and set the first Controller in Remove Mode.


**3.16.3** **Test** **Result**


1. The DSK of the End Node is included in the Controller’s Provisioning List.

2. The End Node is in direct Range of the controllers.

3. The End Node is Successfully included into the Controllers network using SmartStart.

4. The Controller then enters Z-Wave Long Range Network Exclusion.

5. The End Node then enable Learn Mode and expects network exclusion.

6. The End Node is Excluded from the Controller’s Network and assumes it NWI HomeID and
NodeID 0x00.

7. The second Controller is Assigned NodeID 00 and HomeID 00 00 00 00.

a. The second Controller assumes NodeID 0x01 and a Random HomeID, starting its own new
network in this way.


**3.16.4** **Pass** **Criteria**


1. The Network Exclusion process will exclude the node from a network.

2. The Network Exclusion procedure shall be according to Figure 6.7 (LR-NWK:0070.1).

3. When starting Learn Mode Exclusion, a node shall issue an Exclude Request Command to the
broadcast destination NodeID (LR-NWK:0071.1).

4. End Nodes excluded from a network shall assume the NodeID 0x00 after the exclusion and shall
assume their NWI HomeID as HomeID (LR-NWK:0072.1).

5. Controller nodes excluded from a network shall start a new network (LR-NWK:0073.1).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 36


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.16.5** **Fail** **Criteria**


1. Any of the passing Criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 37


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.17 Functional Description – Z-Wave Long Range Network Exclu- sion from a foreign Network


Controllers instructed to remove a node shall also remove nodes from foreign networks.


**3.17.1** **Prerequisites**


 - 1 x Z-Wave LR Capable Sniffer.

 - 2 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.


**3.17.2** **Test** **Setup**


1. Take the DSK from the End Node and add it to the Provisioning List of Controller-1.

2. Place the End Node in direct range of both of the two Controllers.

3. The End Node is included using SmartStart into Controllers-1’ network.

4. Controller-2 is set into Z-Wave Long Range Network Exclusion.

5. The End Node is inserted into Learn Mode and Expects network Exclusion.

6. The End Node is excluded from the network using a foreign network.


**3.17.3** **Test** **Result**


1. The DSK of the End Node is included in Controller-1’s Provisioning List.

2. The End Node is in direct Range of the two Controllers.

3. The End Node is Successfully included into Controller-1s network.

4. Controller-2 then enters Z-Wave Long Range Network Exclusion.

5. The End Node then enables Learn Mode and expects network exclusion.

6. The End Node is Exclude from Controller-1’s Network using a foreign network and assumes it
NWI HomeID and NodeID 0x00.


**3.17.4** **Pass** **Criteria**


1. The Network Exclusion process will exclude the node from a foreign network and shall follow
the procedure as illustrated in figure 6.18.

2. A Controller that has started a node removal shall return an Exclude Request Confirmation
Command if an Exclude Request Command has been issued in another HomeID. The Exclude
Request Confirmation Command if issued by the excluding controller shall be on its own HomeID
(LR-NWK:0075.1, LR-NWK:0076.1).

3. A controller shall issue the Exclude Request Confirmation Command on its own HomeID. When
returning an Exclude Request Confirmation Command to a node in a foreign network, an MDPU
Ack shall not be requested (LR-NWK:0077.1).

4. A randomized delay in the range 0..1 second should be added by controller nodes to the nwkLRExcludeRequestForeignNetBackOff time (LR-NWK:0078.1).

5. A node in Learn Mode (exclusion) shall accept Exclude Request Confirmation Command if
issued in another HomeID. (LR-NWK:0079.1)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 38


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.17.5** **Fail** **Criteria**


1. Any of the passing Criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 39


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.18 Functional Description – Z-Wave Long Range Dual Z-Wave and Z-Wave Long Range Networks


Controllers may create both a Z-Wave and Z-Wave Long Range network that they operate on simultaneously. In this case, they shall use the same HomeID.


**3.18.1** **Prerequisites**


 - 1 x Z-Wave LR and Z-Wave Capable Sniffer.

 - 1 x Z-Wave LR and Z-Wave Capable Controller.

 - 2 x End Node Supporting Z-Wave and Z-Wave LR.


**3.18.2** **Test** **Setup**


1. Take only the DSK from End Node-1 and add it to the Provisioning List of the Controller.

2. Disable the “Long Range” check mark in the Provisioning List section of the Controller. Introduce the DSK of the End Node-2.

3. Make sure both of the End Nodes are in direct range of the Controller.

4. Power up both End Nodes.

5. End Node-1 is included using in Long Range to the Controller Network.

6. End Node-2 is included using Classic Inclusion to the Controller Network.


**3.18.3** **Test** **Result**


1. The DSK of End Node-1 is included in the Controller’s Provisioning List.

2. The DSK of End Node-2 is included as a Classic Node in the Controller’s Provisioning List.

3. The two End Nodes are placed in direct range of the Controller.

4. The two End Nodes are power up.

5. End Node-1 is included as a Z-Wave Long Range device using SmartStart and can communicate
with the Controller.

6. End Node-2 is included using Smart Start Inclusion and is included as a Z-Wave device and
communicate with the Controller.


**3.18.4** **Pass** **Criteria**


1. The End Nodes supporting both Z-Wave and Z-Wave Long Range shall issue a SmartStart Prime
and SmartStart Inclusion Request on both PHY/MAC. (LR-NWK:0086.1)

2. When the End Nodes are successfully included in a network, they shall only use the PHY/MAC
they got included with. (LR-NWK:0087.1)

3. The Controller may create both a Z-Wave And Z-Wave long Range Network that they operate on simultaneously. In this case, they shall use the same HomeID. (LR-NWK:0082.1,
LR-NWK:0083.1)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 40


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.18.5** **Fail** **Criteria**


1. Any of the passing Criteria is not met.

2. Variation outside of the allowed parameters causes successful results when they should not be


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 41


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.19 (3.5 – Negative Testing) Command Frames – Z-Wave Long Range Protocol Command Class – Assign IDs Command


This command is used to assign NodeID and HomeID to the receiving node.


**3.19.1** **Prerequisites**


 - 1 x Z-Wave Long Range Capable Sniffer.

 - 1 x Z-Wave LR Capable Controller.

 - 1 x Z-Wave LR End Node.

_Here_ _it_ _is_ _assumed_ _it_ _is_ _possible_ _to_ _send_ _the_ _Assign_ _ID_ _commands_ _when_ _not_ _including_ _a_ _node,_ _and_ _that_
_the_ _command_ _can_ _be_ _send_ _as_ _a_ _singlecast_ _and_ _a_ _multicast._ _This_ _could_ _be_ _done_ _using_ _a_ _frame_ _generator_
_or_ _a_ _Controller_ _with_ _these_ _functionalities._

_Furthermore,_ _when_ _specifying_ _removing_ _a_ _node_ _or_ _including_ _a_ _node_ _using_ _SmartStart_ _it_ _is_ _expected_ _to_
_follow_ _the_ _format_ _as_ _described_ _in_ _the_ _Functional_ _Description_ _in_ _the_ _end_ _of_ _this_ _document._

_This_ _test_ _case_ _goes_ _through_ _several_ _scenarios_ _and_ _therefore_ _is_ _the_ _End_ _Node_ _excluded_ _several_ _times_ _to_
_accommodate_ _this._


**3.19.2** **Test** **Setup**


1. Set Assign ID to be sent as multicast during SmartStart inclusion.

2. To make sure it’s reset and ready for a new inclusion, remove the End Node from the Controller’s
network.

3. Set Assign ID to be sent as singlecast during SmartStart inclusion.

4. Remove the End Node from the Controller’s network.

5. Include the End Node to the Controller’s network using SmartStart.

6. Set Assign ID to be sent as singlecast during inclusion and set the NodeID value to be greater
than 0xFA0.

7. Remove the End Node from the Controller’s network.

8. Include the End Node to the Controller’s network using SmartStart.

9. Set Assign ID to hold a value in its NodeID field to not be 0x00. Remove the End Node form
the Network.

10. Set Assign ID to hold a value in its HomeID field to not be 0x00. Remove the End Node form
the Network.


**3.19.3** **Test** **Result**


1. The End Node ignores the “Assign ID” command sent as Multicast during inclusion and inclusion
fails.

2. End Node is removed from the network, to make sure it’s reset and ready for a new inclusion.

3. The End Node is successfully included.

4. End Node is removed from the network, to make sure it’s reset and ready for a new inclusion.

6. The End Node ignores the “Assign ID” command sent with NodeID set higher than 0xFA0 and
inclusion fails.

7. End Node is removed from the network, to make sure it’s reset and ready for a new inclusion.

8. The End Node is included Successfully to the Network.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 42


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


9. The End Node does not accept the change in its NodeID and remains in the Network with the
same NodeID.

10. The End Node does not accept the change in its HomeID and remains in the Network with the
same NodeID and HomeID.


**3.19.4** **Pass** **Criteria**


1. The End Node the ignores the command when it’s issued as a multicast (NWK:0089.1).

2. The End Node ignores the Assign ID command when the NodeID field is set between 0x100 to
0xFA0 (LR-NWK:0021.1).

3. During exclusion the End Node ignores the command when the NodeID field is not set to 0x00
(LR-NWK:0026.1).

4. A receiving node shall ignore the command if it is received via broadcast addressing
(LR-NWK:0025.1).

5. During exclusion the End Node ignores the command when the HomeID field is not set to 0x00
(LR-NWK:0022.1).


**3.19.5** **Fail** **Criteria**


1. The nodes accepts the “Assign ID” command when it’s issued as multicast (LR-NWK:0025.1).

2. The nodes accept values outside the interval 0x100 to 0xFA0 for NodeID when being included
using SmartStart (LR-NWK:0021.1).

3. The nodes accept changing their NodeID to something other than 0x00 and remain in the same
Network (NWK:0087.1).

4. The nodes accept changing their HomeID to something other than the HomeID of the Controller’s Network while being excluded and retain their same NodeID (NWK:0088.1).

Variation outside of the allowed parameters causes successful results when they should not be.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 43


Specifcations **Z-Wave** **Long** **Range** **Network** **Layer** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## References


[ZWALMACTEST] ZWA LR MAC_TEST. Z-Wave Alliance Z-Wave Long Range MAC Layer Test
Specificaiton. [Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWALPHYTEST] ZWA LR PHY_TEST. Z-Wave Alliance Z-Wave Long Range PHY Layer Test
Specification. [Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWANWK] ZWA NWK. Z-Wave Alliance Z-Wave and Z-Wave Long Range Network Layer Specification. [Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)

[ZWAPHYMAC] ZWA PHY_MAC. Z-Wave Alliance Z-Wave Long Range PHY and MAC Layer
Specification. [Online]. URL: [https://sdomembers.z-wavealliance.org/.](https://sdomembers.z-wavealliance.org/)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 44


