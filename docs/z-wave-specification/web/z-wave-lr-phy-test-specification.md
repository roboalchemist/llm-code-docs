# **Specification**

_**Release**_ _**3.9.0**_

## **Z-Wave Alliance**


**Aug** **20,** **2025**

## Table of contents


1 Preamble 3
1.1 Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Disclaimer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Revision Record . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6


2 INTRODUCTION 7
2.1 Purpose . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Audience and Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7


3 PHY TEST CASE DESCRIPTIONS 8
3.1 General assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2 LRF profiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.2.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.3 Symbol rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.3.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4 Modulation, encoding and symbol mapping . . . . . . . . . . . . . . . . . . . . . . . . 15
3.4.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.4.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.4.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.4.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.5 Transmit power adjustment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


3.5.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.5.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.5.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.5.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.5.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.6 Receiver sensitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.6.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.6.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.7 Clear channel assessment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.7.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.7.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.7.6 Exception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.8 Receiver spurious requirement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.8.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.8.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.8.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.8.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.8.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.9 Receiver blocking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.9.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.9.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.9.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.9.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.9.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.9.6 Exception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.10 Receiver saturation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.10.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.10.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.10.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.10.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.10.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.11 TX to RX turnaround time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.11.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.11.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.11.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.11.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.11.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.12 RX-to-TX turnaround time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.13 Preamble field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.14 Start of Frame field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.15 Side-Lobe Suppression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.15.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.15.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.15.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.15.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.15.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41


References 42


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 2


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 1 Preamble 1.1 Description


This document outlines how to ensure, that a Z-Wave Long Range PHY is compliant with the Z-Wave
Long Range PHY Specification

Reviewed by Z-Wave Alliance and approved by the Z-Wave Alliance Board of Directors

## 1.2 Disclaimer


THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 3


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 1.3 Revision Record


Table 1.1: Revision History



















© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 4


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


Table 1.1               - continued from previous page















© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 5


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 1.4 Abbreviations


Table 1.2: Abbreviations


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 6


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 2 INTRODUCTION 2.1 Purpose


The purpose of this document is to outline a series of test cases which can prove, that an implementation of the Z-Wave Long Range protocol on RF transceiver adheres to the requirements given in the
Z-Wave Long Range PHY and MAC Specification as defined in the Z-Wave Alliance.

The test cases described in the following sections are not detailed descriptions. The purpose of the
descriptions is to be able show what is needed and to discuss how it can be obtained, and once a
suitable level of understanding is found, the work detailing the individual tests can begin.

## 2.2 Audience and Prerequisites


Test Body / test lab with the capabilities to perform detailed RF measurements and with the experience of conducting measurements according to e.g. Bluetooth / Zigbee / Thread standards.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 7


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3 PHY TEST CASE DESCRIPTIONS


The test cases described in this section are all referring to the PHY requirements stated in the Z-Wave
Alliance “Z-Wave Long Range PHY and MAC Specification”, [1].

## 3.1 General assumptions


All references to tables in [1] in the following sections will be preceded an ZWALR header, e.g. ZWALR
table 7-5 will refer to the table 7-5 in the document [1].

All references to sections in [1] in the following sections will be preceded an ZWALR header, e.g.
ZWALR section 7.1.2.5.2 will refer to section 7.1.2.5.2 in the document:cite: _1_ .

It is assumed, that a Z-Wave device can transmit a modulated RF signal according to the [1] with
any data content as well as a non-modulated signal, a Carrier Wave signal (CW signal) at an RF
frequency identical to fcenter_frequency according to [1].


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 8


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.2 LRF profiles


A Z-Wave device must support all LRF profiles as defined in ZWALR table 5-1.

The RF frequency for all LRF profiles must be measured.


**3.2.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a CW signal

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted RF frequency of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all LRF profiles as listed in ZWALR table 5-1

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz


**3.2.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a constant carrier wave RF signal at each LRF
profile as defined in ZWALR table 5-1

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to:


Table 3.1: RF Profile Spectrum Analyzer settings


The RF frequency of each LRF profile must be measured using the “Peak search” feature of the
spectrum analyzer.


**3.2.3** **Measurement** **result**


The measurement result of the test is the measured peak RF frequency for each LRF profile.

The RF frequency for each LRF profile may not differ more than the accuracy given in ZWALR table
5-2 / ZWALR section 5.2.2.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 9


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


This accuracy is given as a maximum allowed frequency deviation after 5 years of operation and under
extreme temperature conditions.


**3.2.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. All RF frequencies as stated in ZWALR table 5-1 could be measured

2. All RF frequencies measured are within the accuracy limits stated in ZWALR table 5-2 / ZWALR
section 5.2.2. The accuracy measured should be better than +/-12ppm (12ppm is what is expected to be a reasonable initial tolerance of a crystal excluding aging and temperature tolerances).


**3.2.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. A frequency as defined in ZWALR table 5-1 could not be initialized by the Z-Wave device and
not measured in the measurement setup

2. A frequency measured on the Z-Wave device was measured to be less accurate than stated in
ZWALR table 5-2 / ZWALR section 5.2.2


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 10


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.3 Symbol rates


A Z-Wave device must support all the symbol rates / data rates as defined in ZWALR table 5-2 and
at each of the LRF profiles as shown in ZWALR table 5-1.

The modulation and coding parameters for each data rates are given in ZWALR tables 5-4, 5-5 and
5-6

The data rates for the LRF profiles listed in ZWALR table 5-2 must be measured and verified.


**3.3.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a stream of modulated randomly mixed 0 and 1 data
bits at the rates defined in ZWALR table 5-2 and the modulation and coding properties given
in ZWALR tables 5-4, 5-5 and 5-6

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted modulation type of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all listed LRF profiles and data rates as listed in ZWALR table 5.1

4. A spectrum analyzer with better or identical specifications to a Rhode & Schwartz FSV3007,
7.5GHz

5. A digital VSA installed on the spectrum analyzer with the capabilities of at least Rhode &
Schwartz option FSV3-K70.


**3.3.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a constant stream of modulated RF signal at each
RF profile as defined in ZWALR table 5-1.

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to:


Table 3.2: Symbol Rate Spectrum Analyzer settings


The symbol rate of each LRF profile must be measured using IQ constellation diagram option of the
spectrum analyzer as well as the “Symbol Rate Error” from the Results Summary table of the VSA
software:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 11


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025









Q



IQ constellation diagram of

FSV3-K70 Option


|Region 1|Col2|Region 2|Col4|
|---|---|---|---|
|||||
|Region 3||Region 4||
|||||



|Result Summary table|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|||**Current**|**Peak**|**Unit**|
|**EVM Offset**|RMS|xxx|xxx|%|
|**EVM Offset**|Peak|xxx|xxx|%|
|**MER**|RMS|xxx|xxx|dB|
|**MER**|Peak|xxx|xxx|dB|
|**Phase Error**|RMS|xxx|xxx|deg|
|**Phase Error**|Peak|xxx|xxx|deg|
|**Magnitude Error**|PMS|xxx|xxx|%|
|**Magnitude Error**|Peak|xxx|xxx|%|
|**Carrier Frequency Error**||xxx|xxx|Hz|
|Symbol Rate Error||xxx|xxx|ppm|
|**I/Q Skew**||xxx|xxx|ps|
|**Rho**||xxx|xxx||
|**I/Q Offset**||xxx|xxx|dB|
|**I/Q Imbalance**||xxx|xxx|dB|
|**Gain Imbalance**||xxx|xxx|dB|
|**Quadrature Error**||xxx|xxx|deg|
|**Amplitute Droop**||xxx|xxx|dB/sym|
|**Power**||xxx|xxx|dBm|


Figure 3.1: Data rate measurement


**3.3.3** **Measurement** **result**


The measurement result of the test is the appearance of the IQ constellation diagram and the reading
of the Symbol Rate Error from the Results Summary table of the VSA software (Value highlighted
with green in Figure 3.1, Data rate measurement). In case the measurement devices do not support
Symbol Rate Error measurements, the Symbol Rate Error must be measured to less than 1/25th of
the chip rate.

There must be a clear distinction of dots between the 4 regions, and the distance between the center
of the regions must be identical and centered in the constellation diagram.

The Symbol Rate Error must be within the limits stated in ZWALR table 5-2 or, if the measurement
devices do not support such precision, less than 1/15th of the chip rate

This accuracy is given as a maximum allowed frequency deviation after 5 years of operation and under
extreme temperature conditions


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 12


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


**3.3.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. Constellation diagram shows 4 clear regions with no overlap between the regions 1 to 4 as shown
in Figure 3.2.

2. For each LRF profile as stated in ZWALR table 5-1, the analyzed Symbol Rate Error by the
VSA software is within the accuracy stated in ZWALR table 5-2. In case the measurement









Q



Passing condition

|Region 1|D1|Region 2|Col4|
|---|---|---|---|
|Region 1||||
||C||D2|
|Region 3<br>D4||Region 4||
||D3|||



I


|measurement, the Symbol Rate Error must be less ALR table 5-4.|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Result Summary table**|**Result Summary table**|**Result Summary table**|**Result Summary table**|**Result Summary table**|
|||**Current**|**Peak**|**Unit**|
|**EVM Offset**|RMS|xxx|xxx|%|
|**EVM Offset**|Peak|xxx|xxx|%|
|**MER**|RMS|xxx|xxx|dB|
|**MER**|Peak|xxx|xxx|dB|
|**Phase Error**|RMS|xxx|xxx|deg|
|**Phase Error**|Peak|xxx|xxx|deg|
|**Magnitude Error**|PMS|xxx|xxx|%|
|**Magnitude Error**|Peak|xxx|xxx|%|
|**Carrier Frequency Error**||xxx|xxx|Hz|
|Symbol Rate Error||YYY|ZZZ|ppm|
|**I/Q Skew**||xxx|xxx|ps|
|**Rho**||xxx|xxx||
|**I/Q Offset**||xxx|xxx|dB|
|**I/Q Imbalance**||xxx|xxx|dB|
|**Gain Imbalance**||xxx|xxx|dB|
|**Quadrature Error**||xxx|xxx|deg|
|**Amplitute Droop**||xxx|xxx|dB/sym|
|**Power**||xxx|xxx|dBm|



Figure 3.2: Passing condition for symbol rate measurements


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 13


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


**3.3.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Constellation diagram does not show 4 clear regions or there are overlap between the regions 1
to 4 as shown in Figure 3.3.

2. The analyzed Symbol Rate Error by the VSA software is above the accuracy stated in ZWALR









Q





Failing condition



|Region 1|Col2|Region 2|Col4|
|---|---|---|---|
|Region 1||||
||~~D1~~<br>C||D2|
|Region 3<br>D4|D3<br>|Region 4||
|||||


I




|does not support Symbol Rate Error, the chip-rate WALR 5-4.|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Result Summary table**|**Result Summary table**|**Result Summary table**|**Result Summary table**|**Result Summary table**|
|||**Current**|**Peak**|**Unit**|
|**EVM Offset**|RMS|xxx|xxx|%|
|**EVM Offset**|Peak|xxx|xxx|%|
|**MER**|RMS|xxx|xxx|dB|
|**MER**|Peak|xxx|xxx|dB|
|**Phase Error**|RMS|xxx|xxx|deg|
|**Phase Error**|Peak|xxx|xxx|deg|
|**Magnitude Error**|PMS|xxx|xxx|%|
|**Magnitude Error**|Peak|xxx|xxx|%|
|**Carrier Frequency Error**||xxx|xxx|Hz|
|Symbol Rate Error||OOO|PPP|ppm|
|**I/Q Skew**||xxx|xxx|ps|
|**Rho**||xxx|xxx||
|**I/Q Offset**||xxx|xxx|dB|
|**I/Q Imbalance**||xxx|xxx|dB|
|**Gain Imbalance**||xxx|xxx|dB|
|**Quadrature Error**||xxx|xxx|deg|
|**Amplitute Droop**||xxx|xxx|dB/sym|
|**Power**||xxx|xxx|dBm|



Figure 3.3: Failing condition for symbol rate measurements


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 14


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.4 Modulation, encoding and symbol mapping


Data transmitted by a Z-Wave device must be modulated and coded according to the ZWALR tables
5-4, 5-5 and 5-6

The modulation parameter offset EVM for each of the data rates listed in ZWALR table 5-2 must be
measured and verified.


**3.4.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a known stream containing all the symbols shown in
ZWALR table 5.5 at the rates defined in ZWALR table 5-2 and the modulation and coding
properties given in ZWALR tables 5-4, 5-5 and 5-6

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted modulation type of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all listed LRF profiles and data rates as listed in ZWALR table 5.1

4. A spectrum analyzer with better or identical specifications to a Rhode & Schwartz FSV3007,
7.5GHz

5. A digital VSA installed on the spectrum analyzer with the capabilities of at least Rhode &
Schwartz option FSV3-K70.


**3.4.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a constant stream of modulated RF signal at each
LRF profile as defined in ZWALR table 5-1.

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to:


Table 3.3: Modulation and encoding Spectrum Analyzer settings


The modulation properties of each data rate must be measured using demodulation feature of the
VSA FSV3-K70 option of the spectrum analyzer. Below is shown an example of how a demodulated
data stream could appear on the screen of the spectrum analyzer:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 15


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


Example of Demodulation

view of FSV3-K70 Option

|Row/<br>Line|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|1|0|2|1|3|3|0|2|1|
|2|1|0|1|3|0|0|1|3|
|3|2|0|1|1|3|1|3|2|
|4|3|3|0|1|3|2|1|0|
|5|2|2|3|0|1|0|2|1|
|6|1|2|3|2|1|0|3|2|



Figure 3.4: Example of demodulated symbols from OQPSK data stream


Further, the offset EVM must be measured for each of the data rates listed in ZWALR table 5-2.


**3.4.3** **Measurement** **result**


The result of the measurement is a table with demodulated symbols shown on the screen of the
spectrum analyzer as well as the offset EVM measurement.

For the data rate LR1 the demodulated symbols must be identical to the known transmitted data
stream when the timing and frequency settings of the VSA demodulator option is within the limits
given by the limits in ZWALR table 5-2.

For the offset EVM measurement, this must be below the number mentioned in ZWALR section 5.2.4
and measured across - 1000 chips.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 16


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


**3.4.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For data rate LR1: The demodulated symbols and the sequence of the demodulated symbols
must match the known transmitted data pattern.

2. All the symbols given in the ZWALR table 5-5 must be received and demodulated by the VSA
option of the spectrum analyzer.

3. The measured offset EVM across  - 1000 chips is below the number given in ZWALR section
5.2.4


**3.4.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. For data rate LR1: The VSA option of the spectrum analyzer fails to demodulate the transmitted
data stream.

2. Not all the symbols given in the ZWALR table 5-5 are received and demodulated by the VSA
option of the spectrum analyzer.

3. The offset EVM across  - 1000 chips is measured to be above what is stated in ZWALR section
5.2.4.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 17


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.5 Transmit power adjustment


The RF output power transmitted by a Z-Wave device must be adjustable according to ZWALR
section 5.2.5.2.

The output power adjustability must be measured and verified.


**3.5.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a CW RF signal at frequencies specified in ZWALR
table 5-1

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted output power of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all possible output powers for the Z-Wave device.

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz


**3.5.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a CW RF signal at each LRF profile as defined in
ZWALR table 5-1.

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to:


Table 3.4: Transmit power Spectrum Analyzer settings


A series of power measurements must now be performed for each of the possible output power settings
of the Z-Wave device.

The measurements are performed using the “Peak search” functionality of the spectrum analyzer.


**3.5.3** **Measurement** **result**


The measurement result will be a table showing the measured output power for each possible output
power setting.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 18


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


The relationship between the measured output powers must fulfill the statements in the ZWALR
section 5.2.5.2


**3.5.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. It is possible to adjust the output power with the granularity and ranges as described in ZWALR
section 5.2.5.2.


**3.5.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. It is not possible to adjust the output power with the granularity and ranges as described in
ZWALR section 5.2.5.2.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 19


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.6 Receiver sensitivity


The receiver of a Z-Wave device must, under the test conditions given in ZWALR table 5-7, have
a conducted sensitivity identical to or better than described in ZWALR table 5-8. The sensitivity
measurements must be tested for all LRF profiles listed in ZWALR table 5-1


**3.6.1** **Prerequisites**


1. A Z-Wave device capable of receiving, decoding and error handling Z-Wave frames formatted
according to ZWALR section 5.3.1. The Z-Wave device must be able to decode and data process
at transmission rates stated in ZWALR table 5-2. The Z-Wave device must be able to indicate
when a frame is not correctly received. The Z-Wave receiver device is hereafter called DUT

2. The DUT must be mounted on a PCB enabling a cabled RF connection between a RF measurement device and a 50 Ohms matched output of the DUT.

3. A Z-Wave transmitter, either a RF frequency generator which can transmit Z-Wave coded data
messages or a golden Z-Wave device. Data must be transmitted according to ZWALR tables 5-2
to 5-6 and formatted at described in ZWALR section 5.3.1. The output power of the transmitter
must be adjustable to reach the power levels stated in ZWALR table 5-8 when measured at the
input of the DUT. The Z-Wave transmitter is here after called test pattern generator.

4. A means to control the transmitted output power from the test pattern generator to the receiver
DUT.


**3.6.2** **Measurement** **setup**


The Z-Wave receive device, the DUT, is connected to the Z-Wave pattern generator with a coax
cable. The pattern generator transmits Z-Wave test packages back to back to the DUT. The number
of correctly received packages and wrongly received packages must be recorded and the Frame Error
Rate can be calculated:




### PDUT

Figure 3.5: Sensitivity measurement setup



© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 20


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


The received power at the Z-Wave DUT, PDUT, must be adjusted to match the sensitivity requirements
as stated in ZWALR table 5-8.


**3.6.3** **Measurement** **result**


At least 1000 frames formatted according to ZWALR table 5-7 must be transmitted by the test pattern
generator and received by the DUT.


**3.6.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For each data rate and power setting given in ZWALR table 5-8, the frame error rate (FER) is
< 0.01:

FER = 1   - (Number of correctly received frames / Number of transmitted frames)


**3.6.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. For each data rate and power setting given in ZWALR table 5-8, the frame error rate (FER) is

  - 0.01:

FER = 1   - (Number of correctly received frames / Number of transmitted frames)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 21


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.7 Clear channel assessment


The Z-Wave device must be able to sample the RF input level, judge the received power level, and
only start to transmit if the received power level is less than what is stated in ZWALR section 5.2.5.4.
The clear channel assessment must be tested for all LRF profiles listed in ZWALR table 5-1, where
the local RF authorities requires Clear Channel assessment.


**3.7.1** **Prerequisites**


1. A Z-Wave device capable of both receiving and transmitting Z-Wave frames formatted according
to ZWALR section 5.3.1. The Z-Wave device must be able to perform a clear channel assessment
and transmit data if the level of received power is below the limit given in ZWALR section 5.2.5.4.
The Z-Wave device is here after called DUT.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A RF frequency generator which can transmit a CW RF signal. The output power of the
generator must be adjustable to reach the level stated in ZWALR section 5.2.5.4. when measured
at the input of the DUT.

4. A means to control the transmitted CW signal power from the test pattern generator to the
receiver DUT.

5. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz

6. A 3 port RF resistive power combiner.


**3.7.2** **Measurement** **setup**


The DUT, RF generator and spectrum analyzer are all connected through the 3 port RF power
combiner:


PDUT


Figure 3.6: Clear channel assessment measurement setup


The spectrum analyzer should be initialized to:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 22


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


Table 3.5: Clear channel assessment Spectrum Analyzer settings


The Z-Wave device must be initialized to transmit Z-Wave data packets. The output level of the RF
generator is adjusted around the threshold stated in ZWALR section 5.2.5.4. When the input power
to the Z-Wave device is < threshold, the Z-Wave device must transmit, and this will be captured by
the spectrum analyzer. When the input to the Z-Wave device is > threshold, the transmission of data
from the Z-Wave device must stop:


Screen on Spectrum analyzer when in Zero span


RF trigger
level


CCA level


Time


Output power from RF generator


Output power from Z-Wave device


Figure 3.7: CCA spectrum analyzer measurement


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 23


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


**3.7.3** **Measurement** **result**


The measurement result is an assessment of when the Z-Wave device starts to transmit Z-Wave frames
given the output power of the RF generator.


**3.7.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. Transmission of Z-Wave frames from the Z-Wave device starts when the input power to the
Z-Wave device is < CCA threshold as stated in ZWALR section 5.2.5.4


**3.7.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Transmission of Z-Wave frames from the Z-Wave device starts when the input power to the
Z-Wave device is   - CCA threshold as stated in ZWALR section 5.2.5.4.


**3.7.6** **Exception**


The test of the DUT must show that the DUT is able to enable the transmission based on the measured
level of RF noise, but, the absolute level of noise is not important for this test. The absolute level of
noise at which the CCA will be active will be tested by local RF authorities.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 24


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.8 Receiver spurious requirement


A Z-Wave device in receive state may not desensitize other nearby Z-Wave receivers. The emitted LO
leakage may thus not exceed the level stated in ZWALR section 5.2.5.5. The receiver spurious must
be tested for all LRF profiles listed in ZWALR table 5-1


**3.8.1** **Prerequisites**


1. A Z-Wave device in constant receive state.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the receiver the Z-Wave device, or pre-programmed Z-Wave devices to
cover all listed LRF profiles and data rates as listed in ZWALR table 5-1

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz


**3.8.2** **Measurement** **setup**


The Z-Wave device must be connected to the spectrum analyzer with a coax cable.

The spectrum analyzer should be initialized to:


Table 3.6: Receiver spurious requirements Spectrum Analyzer settings


A receiver spurious signal is found by using the Peak Search functionality of the spectrum analyzer.


**3.8.3** **Measurement** **result**


The measurement result is the power level of an RF spur found within the measurement bandwidth
of the spectrum analyzer.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 25


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


**3.8.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. The highest found RF spur within the measurement bandwidth is < the limit stated in ZWALR
section 5.2.5.5.


**3.8.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. The highest found RF spur within the measurement bandwidth is > the limit stated in ZWALR
section 5.2.5.5.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 26


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.9 Receiver blocking


The receiver of a Z-Wave must be able to receive Z-Wave frames even when subjected to blocking
CW RF signals transmitted by other RF devices. The level of the test Z-Wave RF communication
must be set according to ZWALR section 5.2.5.6 and the frequency location and signal strength of
the blocking CW RF signals must be adjusted to match the requirements given in ZWALR table 5-9.
The blocking measurements must be tested for all LRF profiles listed in ZWALR table 5-1


**3.9.1** **Prerequisites**


1. A Z-Wave device capable of receiving, decoding and error handling Z-Wave frames formatted
according to ZWALR section 5.3.1. The Z-Wave device must be able to decode and data process
at transmissions rates stated in ZWALR table 5-2. The Z-Wave device must be able to indicate
when a frame is not correctly received. The Z-Wave receiver device is hereafter called DUT

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the DUT.

3. A Z-Wave transmitter, either a RF frequency generator which can transmit Z-Wave coded data
messages or a golden Z-Wave device. Data must be transmitted according to ZWALR tables 5-2
to 5-6 and formatted as described in ZWALR section 5.3.1. The output power of the transmitter
must be adjustable to reach the power level stated in ZWALR section 5.2.5.6 when measured at
the input of the DUT. The Z-Wave transmitter is here after called test pattern generator.

4. A means to control the transmitted output power from the test pattern generator to the receiver
DUT.

5. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz

6. A CW RF generator to generate the interfering blocking signals at frequency locations and
signal strengths described in ZWALR table 5-9 when measured at the input of the DUT. The
frequency offsets stated in ZWALR table 5-9 are relative to the RF frequency of each LRF profile
in ZWALR table 5-1.

7. A 3 port resistive RF combiner


**3.9.2** **Measurement** **setup**


The Z-Wave receive device, the DUT, the Z-Wave pattern generator and the interfering CW RF
generator are all connected to the 3 port RF combiner with coax cables. The pattern generator transmits Z-Wave test packages back to back to the DUT, and the output power of the pattern generator must be adjusted so that PDUT_Z-Wave traffic is matching the level stated in ZWALR
section 5.2.5.6 (please refer to Figure 3.8). The frequency of the CW RF generator is adjusted
to fcenter frequency of LRF profile_x in ZWALR table 5-1 +/- ffrequency offset in ZWALR table 5-9, the amplitude
is adjusted to the RF level as stated in ZWALR table 5-9 for each offset, and the RF level is
PDUT_blocking signal when measured at the input of the DUT (please refer to Figure 3.8). Once the
setup has been configured, for each frequency offset entry in ZWALR table 5-9, the number of correctly
received packages and wrongly received packages must be recorded and the Frame Error Rate can be
calculated. The measurement setup is shown in Figure 3.8 below:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 27


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025











Figure 3.8: Blocking measurement setup



The RF levels PDUT_Z-Wave traffic and PDUT_blocking signal must be verified, and for this, the coax
connection between the DUT and the 3 port combiner can be disconnected and the 3 port combiner
can be connected to the spectrum analyzer for RF power level verification and RF CW interferer
frequency verification.


**3.9.3** **Measurement** **result**


For each of the LRF profiles in ZWALR table 5-1 and frequency offsets in ZWALR table 5-9, at
least 1000 frames formatted according to ZWALR table 5-7 must be transmitted by the test pattern
generator and received by the DUT.

The test results will be a series of test observations which should include the following data:

(LRF profile; Frequency offset; Number of frames with errors received; Number of frames transmitted)

For each (LRF profile, Frequency offset), the frame error rate must be calculated, and the result must
be below the criterion stated in ZWALR table 5-9.


**3.9.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For each (LRF profile, Frequency offset) given in ZWALR table 5-9, the frame error rate (FER)
is < 0.01:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 28


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


FER = 1   - (Number of correctly received frames / Number of transmitted frames)


**3.9.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Any (LRF profile, Frequency offset) given in ZWALR table 5-9, has a frame error rate (FER)
which is   - 0.01:

FER = 1   - (Number of correctly received frames / Number of transmitted frames)


**3.9.6** **Exception**


To cater for the location of the Local Oscillator Frequency in the receiver with respect to the blocking
frequency, the DUT may fail the test at one frequency offset pr. RF profile.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 29


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.10 Receiver saturation


The receiver of a Z-Wave must be able to receive Z-Wave frames transmitted at RF levels as described
under the test conditions given in ZWALR section 5.2.5.7. The receiver saturation measurements
must be tested for all LRF profiles listed in ZWALR table 5-1


**3.10.1** **Prerequisites**


1. A Z-Wave device capable of receiving, decoding and error handling Z-Wave frames formatted
according to ZWALR section 5.3.1. The Z-Wave device must be able to decode and data process
at transmissions rates stated in ZWALR table 5-2. The Z-Wave device must be able to indicate
when a frame is not correctly received. The Z-Wave receiver device is here after called DUT

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A Z-Wave transmitter, either a RF frequency generator which can transmit Z-Wave coded data
messages or a golden Z-Wave device. Data must be transmitted according to ZWALR tables 5-2
to 5-6 and formatted as described in ZWALR section 5.3.1. The output power of the transmitter
must be adjustable to reach the power level stated in ZWALR section 5.2.5.7 when measured at
the input of the DUT. The Z-Wave transmitter is here after called test pattern generator.

4. A means to control the transmitted output power from the test pattern generator to the receiver
DUT.


**3.10.2** **Measurement** **setup**


The Z-Wave receive device, the DUT, is connected to the Z-Wave pattern generator with a coax
cable. The pattern generator transmits Z-Wave test packages back to back to the DUT. The number
of correctly received packages and wrongly received packages must be recorded and the Frame Error
Rate can be calculated:




### PDUT

Figure 3.9: Receiver saturation measurement setup



© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 30


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


The received power at the Z-Wave DUT, PDUT, must be adjusted to match the RF level as stated in
ZWALR section 5.2.5.7.


**3.10.3** **Measurement** **result**


For each of the LRF profile, at least 1000 frames must be transmitted by the test pattern generator
and received by the DUT at the RF level stated in ZWALR section 5.2.5.7.

The measurement result is the number of correctly and wrongly received Z-Wave frames for each LRF
profile.


**3.10.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For each LRF profile in ZWALR table 5-1, the frame error rate (FER) is < 0.01:

FER = 1   - (Number of correctly received frames / Number of transmitted frames) at the input
power level stated in ZWALR section 5.2.5.7


**3.10.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Any LRF profile given in ZWALR table 5-1, the frame error rate (FER) is  - 0.01:

FER = 1   - (Number of correctly received frames / Number of transmitted frames) at the input
power level stated in ZWALR section 5.2.5.7


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 31


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.11 TX to RX turnaround time


The transceiver of a Z-Wave device must be fast enough to switch from transmission mode to receive
mode, the so-called TX-to-RX turnaround time. The TX-to-RX turnaround time must be measured
under the test conditions given in ZWALR section 5.2.5.8. The TX-to-RX turnaround time measurements must be tested for all LRF profiles listed in ZWALR table 5-1


**3.11.1** **Prerequisites**


1. A Z-Wave device capable of transmitting and receiving, decoding and error handling Z-Wave
frames formatted according to ZWALR section 5.3.1. The Z-Wave device must be able to decode
and data process at transmissions rates stated in ZWALR table 5-2. The Z-Wave device must
be able to indicate when a frame is not correctly received, and all incoming Z-Wave frames must
be acknowledged. The Z-Wave device must set a GPIO, available for measurements with an
oscilloscope, to a state when exciting its transmission state and reverse the state of the GPIO
when the receiver of the Z-Wave device is fully initialized. The Z-Wave receiver device is here
after called DUT

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. The PCB must further enable a measurement using an oscilloscope on the designated GPIO pin
used for measuring TX-to-RX turnaround time measurements.

4. A golden Z-Wave device which can transmit and receive Z-Wave coded data messages. Data must
be transmitted according to ZWALR tables 5-2 to 5-6 and formatted as described in ZWALR
section 5.3.1. The test pattern generator must acknowledge all incoming Z-Wave traffic. The
Z-Wave transmitter is here after called test pattern generator.

5. A means to control the transmission of a Z-Wave frame from the pattern generator.

6. An oscilloscope, equivalent to a R&S RTO 1204 or better.


**3.11.2** **Measurement** **setup**


The DUT and the Z-Wave pattern generator are connected to each other through a coax cable. The
oscilloscope is connected to the GPIO pin of the DUT. The Z-Wave pattern generator is started, and
the pulse widths of the pulsing GPIO pin is measured with the oscilloscope.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 32


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025









Figure 3.10: TX-to-RX turnaround time setup


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 33


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


Table 3.7: Oscilloscope settings for TX-to-RX turnaround measurements


Oscilloscope screen







|Col1|t<br>tx_to_rx|Col3|Col4|V<br>O|
|---|---|---|---|---|
||||||
||End of TX<br>Ready to RX||||


Figure 3.11: TX-to-RX turnaround measurement result


The number of transmitted frames from the Z-Wave pattern generator as well as the number of
received frames at the DUT must be recorded.

Note: If another method for measuring TX-to-RX turn-around time is possible, e.g. using a spectrum
analyzer in zero-span, this method is allowed to be used as well.


**3.11.3** **Measurement** **result**


The measurement result is the duration, ttx_to_rx in Figure 3.11, of the state change of the GPIO pin
of the DUT during the communication between the DUT and the Z-Wave pattern generator measured
for at least 10 consecutive state changes measured on one device under test.

The DUT must have received and acknowledged all the frames transmitted by the Z-Wave pattern
generator.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 34


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


**3.11.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. The TX-to-RX turnaround time, ttx_to_rx for at least 10 consecutive samples are less than
stated in ZWALR table 5.27 and all transmitted frames by the Z-Wave generator were received
and acknowledged by the Z-Wave device.


**3.11.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Any of of the at least 10 sampled TX-to-RX turnaround times, ttx_to_rx were higher than stated
in ZWALR table 5.27 or not all transmitted frames by the Z-Wave generator were received and
acknowledged by the Z-Wave device.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 35


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.12 RX-to-TX turnaround time


The timing of the transceiver of a Z-Wave device must be so, that it allows a transmitting device
to switch from TX to RX, the so-called RX-to-TX turnaround time. The RX-to-TX turnaround
time must be measured under the test conditions given in ZWALR section 5.2.5.9. The RX-to-TX
turnaround time measurements must be tested for all LRF profiles listed in ZWALR table 5-1.

RX-to-TX turnaround times are depending on the MAC layer implementation and is thus not a part
of a PHY test. Refer to LR-MAC test 4.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 36


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.13 Preamble field


Data frames transmitted by a Z-Wave device be formatted as described in ZWALR section 5.3.1:
With a preamble field, a Start of Frame delimiter and payload. The requirements for the number of
preamble bytes to transmit are stated in ZWALR table 5-10.

The preambles are coded according to ZWALR tables 5-2, 5-4, 5-5 and 5-6.

The number of preamble types transmitted for each type of Z-Wave frame must be tested according
to ZWALR table 5-10 and tested for all LRF profiles listed in ZWALR table 5-1.

Preambles are inserted into Z-Wave frames by the MAC layer and is thus not a part of a PHY test.
Refer to LR-MAC test 2.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 37


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.14 Start of Frame field


The transceiver of a Z-Wave must be able to correctly transmit and correctly receive Z-Wave start of
frame information as described in ZWALR section 5.3.3. The data content of the Start of Frame field
is described in ZWALR table 5.11. The handling of Start of Frame field in Z-Wave frames must be
tested for all LRF profiles listed in ZWALR table 5-1.

Start of Frame is inserted into Z-Wave frames by the MAC layer and is thus not a part of a PHY
test. Refer to LR-MAC test 3.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 38


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## 3.15 Side-Lobe Suppression


To prevent false detection of preamble bits in a receiver, the transmitter of Z-Wave LR frames must
suppress the side-lobes adequately as described in ZWALR section 5.2.5.10.

The side-lobe suppression must be tested for LRF profiles listed in ZWALR Table 5.1.


**3.15.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a stream of randomly mixed 0 and 1 data bits at the
rates defined in ZWALR Table 5.2 and the modulation and coding properties given in ZWALR
Tables 5.4, 5.5, and 5.6.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted modulation type of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all LRF profiles and data rates as listed in ZWALR Table 5.1.

4. Output power setting must be 0 dBm or Pout.

5. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz


**3.15.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit randomly modulated data stream for each LRF
profile as defined in ZWALR Table 5.1.

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to:


Table 3.8: Transmit power Spectrum Analyzer settings


The measurements are performed using the “Markers” functionality of the spectrum analyzer and 2
markers are required pr. measurement.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 39


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025







Pdiff1



Figure 3.12: Side-lobe measurements



Pdiff2



The center frequency is set to the frequency of the LRF profile to test.

Two markers are set at the frequencies:

Marker1 = Fc - 2MHz*1

Marker2 = Fc - (2MHz*1-200kHz)

The power difference between the two markers is calculated as PDiff1 = PMarker 1 - PMarker2

For the same LRF profile, two new markers are set at the frequencies:

Marker1 = Fc + 2MHz*1

Marker2 = Fc + (2MHz*1-200kHz)

The power difference between the two markers is calculated as PDiff2 = PMarker 1 - PMarker2

Both PDiff1 and PDiff2 must be <= 1dB.

The measurements and calculations are repeated for the following marker frequency settings:

Marker1 = Fc +/- (2MHz*4)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 40


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025


Marker2 = Fc +/- (2MHz*4-200kHz)


**3.15.3** **Measurement** **result**


The side-lobes of the modulated signal must be so, that the PDiff1 and PDiff2 for x=1 and x=4 are
<= 1 dB as per ZWALR section 5.2.5.10.


**3.15.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. The measured power differences, PDiff1 and PDiff2, are both below the requirements stated in
ZWALR section 5.2.5.10 for x=1 and x=4.


**3.15.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. One of the measured power differences, PDiff1 or PDiff2, is above the requirements stated in
ZWALR section 5.2.5.10 for x=1 or x=4.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 41


Specifcations **Z-Wave** **Long** **Range** **PHY** **Layer** **Test** **Specifcation,** **Release** **3.9.0** August 20, 2025

## References


[1] Z-Wave Long Range PHY and MAC Specification, Z-Wave Alliance.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 42


