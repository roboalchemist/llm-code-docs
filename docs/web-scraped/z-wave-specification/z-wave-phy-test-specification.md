_**Release**_ _**2.9.0**_

## **Z-Wave Alliance**


**May** **30,** **2025**

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
3.2 RF profiles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.2.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.3 Symbol rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.3.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.3.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.3.6 Exception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.4 Modulation and encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
3.4.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.4.6 Exception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.5 Symbol mapping . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


3.5.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.5.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.5.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.5.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.5.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6 Transmit power adjustment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.6.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.6.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.6.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.6.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.6.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.7 Receiver sensitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.7.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.7.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.7.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.7.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.7.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.8 Clear channel assessment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.8.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.8.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
3.8.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.8.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.8.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.8.6 Exception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.9 Receiver spurious requirement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.9.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.9.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.9.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.9.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.9.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.10 Receiver blocking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.10.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.10.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.10.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.10.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.10.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.10.6 Exception . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.11 Receiver Saturation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.11.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.11.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.11.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.11.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.11.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.12 TX to RX turnaround time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.12.1 Prerequisites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.12.2 Measurement setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.12.3 Measurement result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.12.4 Pass criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.12.5 Fail criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.13 RX-to-TX turnaround time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.14 Preamble field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.15 Start of Frame field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
3.16 End of Frame field (optional) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41


4 APPENDIX 42
4.1 Frequency, channel, and data rate overview . . . . . . . . . . . . . . . . . . . . . . . . 42


References 43


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 2


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 1 Preamble 1.1 Description


Test case descriptions for the Z-Wave Alliance PHY layer

Reviewed and approved by the Z-Wave Alliance Core Stack Working Group (CSWG).

## 1.2 Disclaimer


THIS SPECIFICATION IS BEING OFFERED WITHOUT ANY WARRANTY WHATSOEVER,
AND IN PARTICULAR, ANY WARRANTY OF NON-INFRINGEMENT IS EXPRESSLY DISCLAIMED. ANY USE OF THIS SPECIFICATION SHALL BE MADE ENTIRELY AT THE IMPLEMENTER’S OWN RISK, AND NEITHER THE ALLIANCE, NOR ANY OF ITS MEMBERS
OR SUBMITTERS, SHALL HAVE ANY LIABILITY WHATSOEVER TO ANY IMPLEMENTER
OR THIRD PARTY FOR ANY DAMAGES OF ANY NATURE WHATSOEVER, DIRECTLY OR
INDIRECTLY, ARISING FROM THE USE OF THIS SPECIFICATION.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 3


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 1.3 Revision Record


Table 1.1: Revision History



















© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 4


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


Table 1.1               - continued from previous page

















© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 5


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 1.4 Abbreviations


Table 1.2: Abbreviations


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 6


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 2 INTRODUCTION 2.1 Purpose


The purpose of this document is to outline a series of test cases which can prove, that an implementation of the Z-Wave protocol on a non-Silicon Labs chip / device adheres to the requirements given
in the ITU specification ITU [G.9].

The test cases described in the following sections are not detailed descriptions. The purpose of the
descriptions is to be able show what is needed and to discuss how it can be obtained, and once a
suitable level of understanding is found, the work detailing the individual tests can begin.

## 2.2 Audience and Prerequisites


Test Body / test lab with the capabilities to perform detailed RF measurements and with the experience of conducting measurements according to e.g. Bluetooth / Zigbee / Thread standards.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 7


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3 PHY TEST CASE DESCRIPTIONS


The test cases described in this section are all referring to the PHY requirements stated in the ITU
specification: ITU-T [G.9] (01/2015):

## 3.1 General assumptions


All references to tables in ITU-T G.9959 [G.9] (01/2015) in the following sections will be preceded
an ITU header, e.g. ITU table 7-5 will refer to the table 7-5 in the document ITU-T G.9959 [G.9]
(01/2015).

All references to sections in ITU-T G.9959 [G.9] (01/2015) in the following sections will be preceded
an ITU header, e.g. ITU section 7.1.2.5.2 will refer to section 7.1.2.5.2 in the document ITU-T G.9959

[G.9] (01/2015).

It is assumed, that a Z-Wave device can transmit a modulated RF signal according to the ITU-T
G.9959 [G.9] (01/2015) with any data content as well as a non-modulated signal, a Carrier Wave
signal (CW signal) at an RF frequency identical to fcenter_frequency according to ITU-T G.9959

[G.9] (01/2015) ITU table 7-5 and 7-6.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 8


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.2 RF profiles


A Z-Wave device must support all RF profiles as defined in ITU table 7-1.

The RF frequency for all RF profiles must be measured.


**3.2.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a CW signal.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted RF frequency of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all RF profiles as listed in ITU table 7-1.

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.


**3.2.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a constant carrier wave RF signal at each RF
profile as defined in ITU table 7-1

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to:


Table 3.1: RF Profile Spectrum Analyzer settings


The RF frequency of each RF profile must be measured using the “Peak search” feature of the spectrum
analyzer.


**3.2.3** **Measurement** **result**


The measurement result of the test is the measured RF frequency for each RF profile.

The RF frequency for each RF profile may not differ more than the accuracy given in ITU section
7.1.2.5.1.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 9


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


This accuracy is given as a maximum allowed frequency deviation after 5 years of operation and under
extreme temperature conditions.


**3.2.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. All RF frequencies as stated in ITU table 7-1 could be measured.

2. All RF frequencies measured are within the accuracy limits stated in ITU table 7-2 / ITU section
7.1.2.5.1. The accuracy measured should be better than +/-12ppm (12ppm is what is expected
to be a reasonable initial tolerance of a crystal excluding aging and temperature tolerances).


**3.2.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. A frequency as defined in ITU table 7-1 could not be initialized by the Z-Wave device and not
measured in the measurement setup.

2. A frequency measured on the Z-Wave device was measured to be less accurate than stated in
ITU table 7-2 / ITU section 7.1.2.5.1.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 10


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.3 Symbol rates


A Z-Wave device must support all the symbol rates / data rates as defined in ITU table 7-2 and at
each of the RF profiles as shown in ITU table 7-1.

The modulation parameters for each data rates are given in ITU tables 7-4, 7-5 and 7-6

The data rates for the RF profiles listed in ITU table 7-1 must be measured and verified.


**3.3.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a stream of modulated 0 and 1 symbols at the rates
defined in ITU table 7-2 and the modulation properties given in ITU tables 7-4, 7-5 and 7-6.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted modulation type of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all listed RF profiles and data rates as listed in ITU table 7-1.

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.

5. An analog demodulator option installed on the spectrum analyzer with the capabilities of at
least Keysight option “N9063A Analog Demod Measurement”.


**3.3.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a constant stream of modulated RF signal at each
RF profile as defined in ITU table 7-1. If test 3.2 pass, this test can be reduced to the following RF
profiles: 1-3, 4-6 and 19-21 as defined in ITU table 7-1.

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to:


Table 3.2: Symbol Rate Spectrum Analyzer Settings


The symbol rate of each RF profile must be measured using the marker features of the spectrum
analyzer:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 11


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

|Col1|N9063A Analog Demod Measurement screen on Spectrum analyzer|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||M1<br>M2|M1<br>M2|M1<br>M2|M1<br>M2|M1<br>M2|M1<br>M2|M1<br>M2|M1<br>M2|
||M1<br>M2||||||||
||||||||||



Time


Figure 3.1: Data rate measurement


**3.3.3** **Measurement** **result**


The measurement result of the test is the measured time for two transmitted symbols divided by two.

The measured symbol time may not differ more than 1 / (nominal symbol rate) +/- the accuracy as
given in ITU table 7-2.

This accuracy is given as a maximum allowed frequency deviation after 5 years of operation and under
extreme temperature conditions.


**3.3.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. The correct symbol rate for each RF profile as stated in ITU table 7-1 could be measured.

2. All symbol rates are within the accuracy limits as stated in ITU table 7-2.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 12


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.3.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. A frequency as defined in ITU table 7-1 could not be initialized by the Z-Wave device and not
measured in the measurement setup.

2. The accuracy of a measured symbol rate did not pass the specification as given in ITU table
7-2.


**3.3.6** **Exception**


In case the measurement device used to verify the symbol rate is not able to measure with a precision
as stated in ITU table 7-2, the measured precision of the symbol duration must be < 1/25th of the
nominal symbol duration.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 13


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.4 Modulation and encoding


Data transmitted by a Z-Wave device must be modulated according to the ITU tables 7-4, 7-5 and
7-6

The modulation parameters for each of the data rates listed in ITU table 7-4 must be measured and
verified.


**3.4.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a stream of modulated 0 and 1 symbols at the rates
defined in ITU table 7-2 and the modulation properties given in ITU tables 7-4, 7-5 and 7-6.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted modulation type of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all listed RF profiles and data rates as listed in ITU table 7-1.

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.

5. An analog demodulator option installed on the spectrum analyzer with the capabilities of at
least Keysight option “N9063A Analog Demod Measurement”.


**3.4.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a constant stream of modulated RF signal at each
RF profile as defined in ITU table 7-1. If test 3.2 pass, this test can be reduced to the following RF
profiles: 1-3, 4-6 and 19-21 as defined in ITU table 7-1.

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to below settings or similar:


Table 3.3: Modulation and encoding Spectrum Analyzer settings


The modulation properties of each data rate must be measured using the marker features of the
spectrum analyzer and the readings of the spectrum analyzer:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 14


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


N9063A Analog Demod Measurement screen on
Spectrum analyzer


Time


Figure 3.2: Modulation format measurement, FSK Data Rate R1 and R2


N9063A Analog Demod Measurement screen on
Spectrum analyzer


Time


Figure 3.3: Modulation format measurement, GFSK Data Rate R3


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 15


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.4.3** **Measurement** **result**


For data rates R1, R2 and R3 the measurement result of the test is measured frequency separation
and the f center + f offset.

For data rate R3, a further measurement result is the BT ratio.

The measured values must be within the limits given by ITU table 7-4.


**3.4.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For data rates R1, R2 and R3: At no time within the duration of a symbol may the frequency
of the symbol exceed the requirements of the Separation as given in ITU table 7-4.

2. For data rates R1, R2 and R3: The measured f center + f offset must be measured to match what
can be calculated for the particular data rate with the precision as stated in ITU table 7-2.

3. For data rate R3, the BT ratio must be measured to value 0.6, but the BT value is practically
impossible to measure. A device with a wrong BT will either fail local RF regulatory TX tests
or have a poor sensitivity.


**3.4.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. For data rates R1, R2 and R3: At any time within the duration of a symbol, the frequency of
the symbol exceeds the requirements of the Separation as given in ITU table 7-4.

2. For data rates R1, R2 and R3: The measured f center + f offset does no match with the calculated
center frequency for the particular data rate with the precision as stated in ITU table 7-2.


**3.4.6** **Exception**


When measuring the modulation and coding format, a transient frequency separation error for the
first transmitted symbol in a data stream is allowed, this to cater for the initialization and regulation
loop of the frequency synthesis of the Z-Wave device.

For each transmitted symbol, a transient overshoot/undershoot is allowed to exceed the requirements
for the frequency separation given in ITU table 7-4 if the duration of the transient is < 2/5th of the
expected frequency time:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 16


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


N9063A Analog Demod Measurement screen on
Spectrum analyzer



Allowed overshoot


Max: Diviation +20%


fcenter + foffset





Time


Figure 3.4: Frequency under/overshoot exception


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 17


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.5 Symbol mapping


Data bits transmitted by a Z-Wave device must be mapped / coded into RF frequencies according to
the ITU tables 7-5 and 7-6.

The symbol mapping / coding for each of the data rates listed in ITU table 7-4 must be measured
and verified.


**3.5.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a stream of modulated ‘10001000’binary data bits at
the rates defined in ITU table 7-2 and the modulation properties and coding properties given in
ITU tables 7-4, 7-5 and 7-6.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted modulation type of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all listed RF profiles and data rates as listed in ITU table 7-1.

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.

5. An analog demodulator option installed on the spectrum analyzer with the capabilities of at
least Keysight option “N9063A Analog Demod Measurement”.


**3.5.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a constant stream of modulated RF signal at each
RF profile as defined in ITU table 7-1. The data bits modulated must be a stream of ‘10001000’binary.
If test 3.2 pass, this test can be reduced to the following RF profiles: 1-3, 4-6 and 19-21 as defined in
ITU table 7-1.

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to below settings or a similar setting:


Table 3.4: Symbol mapping Spectrum Analyzer settings


The symbol mapping properties of each data rate must be measured using the readings of the spectrum
analyzer:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 18


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


N9063A Analog Demod Measurement screen on
Spectrum analyzer





Time


Figure 3.5: Symbol mapping measurement, FSK Data Rate R1, Manchester Coding

|Col1|N9063A Analog Demod Measurement screen on Spectrum analyzer|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
||||||
||||||



Time


Figure 3.6: Symbol mapping measurement, FSK Data Rate R2, NRZ Coding


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 19


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

|Col1|N9063A Analog Demod Measurement screen on Spectrum analyzer|
|---|---|
|||
||'1000'<br>'1000'|



Time


Figure 3.7: Symbol mapping measurement, FSK Data Rate R3, NRZ coding


**3.5.3** **Measurement** **result**


For data rates R1, R2 and R3 the measurement result of the test is a clear pattern of the demodulated
data stream identical to Figure 3.5, Figure 3.6, and Figure 3.7 and with frequency shifts according to
ITU tables 7-5 and 7-6.


**3.5.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For data rate R1: The demodulated data stream has frequency shifts according to ITU table
7-6.

2. For data rates R2 and R3: The demodulated data stream has frequency shifts according to ITU
table 7-5.


**3.5.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. For data rate R1: The demodulated data stream has frequency shifts different from ITU table
7-6.

2. For data rates R2 and R3: The demodulated data stream has frequency shifts different from
ITU table 7-5.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 20


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.6 Transmit power adjustment


The RF output power transmitted by a Z-Wave device must be adjustable according to ITU section
7.1.2.5.2.

The output power adjustability must be measured and verified.


**3.6.1** **Prerequisites**


1. A Z-Wave device capable of transmitting a CW RF signal at frequencies specified in ITU table
7-1.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the transmitted output power of the Z-Wave device, or pre-programmed
Z-Wave devices to cover all possible output powers for the Z-Wave device.

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.


**3.6.2** **Measurement** **setup**


The Z-Wave device must be initialized to transmit a CW RF signal at the nominal output power,
denoted OP nom at each RF profile as defined in ITU table 7-1. If the test 3.2 has been conducted
and all RF profiles passed the test, a sub-set of RF profiles may be selected for this test: RF profiles
1-3; 4-6 and 19-21 as defined in ITU table 7-1.

The Z-Wave device must be connected to a spectrum analyzer with a coaxial cable.

The spectrum analyzer should be initialized to below or similar settings:


Table 3.5: Transmit power Spectrum Analyzer settings


A series of power measurements must now be performed for each of the possible output power settings
of the Z-Wave device.

The measurements are performed using the “Peak search” functionality of the spectrum analyzer.


**3.6.3** **Measurement** **result**


The measurement result will be a table showing the measured output power for each possible output
power setting.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 21


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


The relationship between the measured output powers must full fill the statements in the ITU section
7.1.2.5.2


**3.6.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. It is possible to adjust the output power with a granularity of 2dB or better for power settings
down to OP nom   - 10dB.

2. It is possible to adjust the output power down to a value less than or identical to OP nom  20dB.


**3.6.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. It is not possible to adjust the output power with a granularity of 2dB or better for power
settings down to OP nom    - 10dB.

2. It is not possible to adjust the output power down to a value less than or identical to OP nom  20dB.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 22


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.7 Receiver sensitivity


The receiver of a Z-Wave must, under the test conditions given in ITU table 7-7, have a conducted
sensitivity identical to or better than described in ITU table 7-8. The sensitivity measurements must
be tested for all RF profiles listed in ITU table 7-1


**3.7.1** **Prerequisites**


1. A Z-Wave device capable of receiving, decoding and error handling Z-Wave frames formatted
according to ITU section 7.1.3. The Z-Wave device must be able to decode and data process at
transmissions rates stated in ITU table 7-2. The Z-Wave device must be able to indicate when
a frame is not correctly received. The Z-Wave receiver device is here after called DUT.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A Z-Wave transmitter, either a RF frequency generator which can transmit Z-Wave coded data
messages or a golden Silicon Labs Z-Wave device. Data must be transmitted according to ITU
tables 7-2 to 7-6 and formatted at described in ITU section 7.1.3. The output power of the
transmitter must be adjustable to reach the power levels stated in ITU table 7-8 when measured
at the input of the DUT. The Z-Wave transmitter is here after called test pattern generator.

4. A means to control the transmitted output power from the test pattern generator to the receiver
DUT.

5. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.


**3.7.2** **Measurement** **setup**


The Z-Wave receive device, the DUT, is connected to the Z-Wave pattern generator with a coax
cable. The pattern generator transmits Z-Wave test packages back to back to the DUT. The number
of correctly received packages and wrongly received packages must be recorded and the Frame Error
Rate can be calculated:





PDUT


Figure 3.8: Sensitivity measurement setup



© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 23


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


The received power at the Z-Wave DUT, P DUT, must be adjusted to match the sensitivity requirements as stated in ITU table 7-8.


**3.7.3** **Measurement** **result**


For each of the RF profile, at least 1000 frames must be transmitted by the test pattern generator
and received by the DUT.


**3.7.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For each data date and power setting given in ITU table 7-8, the frame error rate (FER) is <
0.01: FER = 1    - (Number of correctly received frames / Number of transmitted frames)


**3.7.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. For each data date and power setting given in ITU table 7-8, the frame error rate (FER) is  0.01: FER = 1    - (Number of correctly received frames / Number of transmitted frames)


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 24


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.8 Clear channel assessment


The Z-Wave device must be able to sample the RF input level, judge the received power level, and
only start to transmit if the received power level is less than what is stated in ITU section 7.1.2.5.4.
The clear channel assessment must be tested RF profiles listed in ITU table 7-1 where the local RF
authorities requires Clear Channel assessment, ie. RF profiles 19-21 and 25-27 according to ITU table
7-1.


**3.8.1** **Prerequisites**


1. A Z-Wave device capable of both receiving and transmitting Z-Wave frames formatted according
to ITU section 7.1.3. The Z-Wave device must be able to perform a clear channel assessment
and transmit data if the level of received power is below the limit given in ITU section 7.1.2.5.4.
The Z-Wave device is here after called DUT.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A RF frequency generator which can transmit a CW RF signal. The output power of the
generator must be adjustable to reach the level stated in ITU section 7.1.2.5.4. when measured
at the input of the DUT.

4. A means to control the transmitted CW signal power from the test pattern generator to the
receiver DUT.

5. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.

6. A 3 port RF resistive power combiner.


**3.8.2** **Measurement** **setup**


The DUT, RF generator and spectrum analyzer are all connected through the 3 port RF power
combiner:


PDUT


Figure 3.9: Clear Channel assessment measurement setup


The spectrum analyzer should be initialized to:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 25


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


Table 3.6: Clear channel assessment Spectrum Analyzer settings


The Z-Wave device must be initialized to transmit Z-Wave data packets. The output level of the RF
generator is adjusted around the threshold stated in ITU section 7.1.2.5.4. When the input power to
the Z-Wave device is < threshold, the Z-Wave device will transmit, and this will be captured by the
spectrum analyzer. When the input to the Z-Wave device is - threshold, the transmission of data
from the Z-Wave device must stop:


Screen on Spectrum analyzer when in Zero span


RF trigger
level


CCA level


Time


Output power from RF generator


Output power from Z-Wave device


Figure 3.10: CCA spectrum analyzer measurement


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 26


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.8.3** **Measurement** **result**


The measurement result is an assessment of when the Z-Wave device starts to transmit Z-Wave frames
given the output power of the RF generator.


**3.8.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. Transmission of Z-Wave frames from the Z-Wave device starts when the input power to the
Z-Wave device is < CCA threshold as stated in ITU section 7.1.2.5.4.


**3.8.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Transmission of Z-Wave frames from the Z-Wave device starts when the input power to the
Z-Wave device is   - CCA threshold as stated in ITU section 7.1.2.5.4.


**3.8.6** **Exception**


The test of the DUT must show, that the DUT is able to enable the transmission based on the measured
level of RF noise, but, the absolute level of noise is not important for this test. The absolute level of
noise at which the CCA will be active will be tested by local RF authorities.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 27


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.9 Receiver spurious requirement


A Z-Wave device in receive state may not desensitize other nearby Z-Wave receivers. The emitted LO
leakage may thus not exceed the level stated in ITU section 7.1.2.5.5. The receiver spurious must be
tested for all RF profiles listed in ITU table 7-1


**3.9.1** **Prerequisites**


1. A Z-Wave device in constant receive state.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A method to initialize the receiver the Z-Wave device, or pre-programmed Z-Wave devices to
cover all listed RF profiles and data rates as listed in ITU table 7-1.

4. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.


**3.9.2** **Measurement** **setup**


The Z-Wave device must be connected to the spectrum analyzer with a coax cable.

The spectrum analyzer should be initialized to:


Table 3.7: Receiver spurious requirements Spectrum Analyzer settings


A receiver spurious signal is found by using the Peak Search functionality of the spectrum analyzer.


**3.9.3** **Measurement** **result**


The measurement result is the power level of an RF spur found within the measurement bandwidth
of the spectrum analyzer.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 28


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.9.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. The highest found RF spur within the measurement bandwidth is < the limit stated in ITU
section 7.1.2.5.5.


**3.9.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. The highest found RF spur within the measurement bandwidth is  - the limit stated in ITU
section 7.1.2.5.5.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 29


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.10 Receiver blocking


The receiver of a Z-Wave must be able to receive Z-Wave frames even when subjected to blocking
CW RF signals transmitted by other RF devices. The level of the test Z-Wave RF communication
must be set according to ITU section 7.1.2.5.6 and the frequency location and signal strength of the
blocking CW RF signals must be adjusted to match the requirements given in ITU table 7-9. The
blocking measurements must be tested for all RF profiles listed in ITU table 7-1.


**3.10.1** **Prerequisites**


1. A Z-Wave device capable of receiving, decoding and error handling Z-Wave frames formatted
according to ITU section 7.1.3. The Z-Wave device must be able to decode and data process at
transmissions rates stated in ITU table 7-2. The Z-Wave device must be able to indicate when
a frame is not correctly received. The Z-Wave receiver device is here after called DUT.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A Z-Wave transmitter, either a RF frequency generator which can transmit Z-Wave coded data
messages or a golden Silicon Labs Z-Wave device. Data must be transmitted according to ITU
tables 7-2 to 7-6 and formatted at described in ITU section 7.1.3. The output power of the
transmitter must be adjustable to reach the power levels 3dB higher than stated in ITU table
7-8 when measured at the input of the DUT. The Z-Wave transmitter is here after called test
pattern generator.

4. A means to control the transmitted output power from the test pattern generator to the receiver
DUT.

5. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.

6. A CW RF generator to generate the interfering blocking signals at frequency locations and signal
strengths described in ITU table 7-9 when measured at the input of the DUT. The frequency
offsets stated in ITU table 7-9 are relative to the RF frequency of each RF profile in ITU table
7-1.

7. A 3 port resistive RF combiner.


**3.10.2** **Measurement** **setup**


The Z-Wave receive device, the DUT, the Z-Wave pattern generator and the interfering CW RF
generator are all connected to the 3 port RF combiner with coax cables. The pattern generator
transmits Z-Wave test packages back to back to the DUT, and the output power of the pattern
generator must be adjusted so that P DUT_Z-Wave traffic is 3dB above the level stated in ITU table 7-8 (please refer to Figure 3.11). The frequency of the CW RF generator is adjusted to: f

center frequency of RF profile_x in ITU table

7-1 [+/-] [f] frequency offset in ITU table 7-9 [,] [the] [amplitude] [is] [adjusted] [to] [the] [RF] [level] [as] [stated] [in] [ITU] [table]
7-9 for each offset, and the RF level is P DUT_blocking signal when measured at the input of the DUT
(please refer to Figure 3.11). Once the setup has been configured, for each frequency offset entry
in ITU table 7-9, the number of correctly received packages and wrongly received packages must be
recorded and the Frame Error Rate can be calculated. The measurement setup is shown in Figure
3.11 below:


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 30


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025











Figure 3.11: Blocking measurement setup



The RF levels P DUT_Z-Wave traffic and P DUT_blocking signal must be verified, and for this, the coax
connection between the Z-Wave device and the 3 port combiner can be disconnected and the 3 port
combiner can be connected to the spectrum analyzer for RF power level verification and RF CW
interferer frequency verification.


**3.10.3** **Measurement** **result**


For each of the RF profiles in ITU table 7-1 and frequency offsets in ITU table 7-9, at least 1000
frames must be transmitted by the test pattern generator and received by the DUT.

The test results will be a series of test observations which should include the following data:

(RF profile; Frequency offset; Number of frames with errors received; Number of frames transmitted)

For each (RF profile, Frequency offset), the frame error rate must be calculated, and the result must
be below the criterion stated in ITU table 7-7.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 31


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


**3.10.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For each RF profile and Frequency offset given in ITU table 7-9, the frame error rate (FER) is <
0.01: FER = 1 - (Number of correctly received frames / Number of transmitted frames)


**3.10.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Any RF profile and Frequency offset given in ITU table 7-9, has a frame error rate (FER) which
is - 0.01: FER = 1 - (Number of correctly received frames / Number of transmitted frames)


**3.10.6** **Exception**


To cater for the location of the Local Oscillator Frequency in the receiver with respect to the blocking
frequency, the DUT may fail the test at one frequency offset pr. RF profile.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 32


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.11 Receiver Saturation


The receiver of a Z-Wave must be able to receive Z-Wave frames transmitted at RF levels as described
under the test conditions given in ITU section 7.1.2.5.7. The receiver saturation measurements must
be tested for all RF profiles listed in ITU table 7-1.


**3.11.1** **Prerequisites**


1. A Z-Wave device capable of receiving, decoding and error handling Z-Wave frames formatted
according to ITU section 7.1.3. The Z-Wave device must be able to decode and data process at
transmissions rates stated in ITU table 7-2. The Z-Wave device must be able to indicate when
a frame is not correctly received. The Z-Wave receiver device is here after called DUT.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. A Z-Wave transmitter, either a RF frequency generator which can transmit Z-Wave coded data
messages or a golden Silicon Labs Z-Wave device. Data must be transmitted according to ITU
tables 7-2 to 7-6 and formatted at described in ITU section 7.1.3. The output power of the
transmitter must be adjustable to reach the power level stated in ITU section 7.1.2.5.7 when
measured at the input of the DUT. The Z-Wave transmitter is here after called test pattern
generator.

4. A means to control the transmitted output power from the test pattern generator to the receiver
DUT.

5. A spectrum analyzer with better or identical specifications to a Keysight CXA N9000A, 7.5GHz.


**3.11.2** **Measurement** **setup**


The Z-Wave receive device, the DUT, is connected to the Z-Wave pattern generator with a coax
cable. The pattern generator transmits Z-Wave test packages back-to-back to the DUT. The number
of correctly received packages and wrongly received packages must be recorded and the Frame Error
Rate can be calculated:





PDUT


Figure 3.12: Receiver saturation measurement setup



© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 33


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


The received power at the Z-Wave DUT, P DUT, must be adjusted to match the RF level as stated in
ITU section 7.1.2.5.7.


**3.11.3** **Measurement** **result**


For each of the RF profile, at least 1000 frames must be transmitted by the test pattern generator
and received by the DUT at the RF level stated in ITU section 7.1.2.5.7.

The measurement result is the number of correctly and wrongly received Z-Wave frames for each RF
profile.


**3.11.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. For each RF profile in ITU table 7-1, the frame error rate (FER) is < 0.01: FER = 1 - (Number
of correctly received frames / Number of transmitted frames) at the input power level stated in ITU
section 7.1.2.5.7.


**3.11.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Any RF profile given in ITU table 7-1, the frame error rate (FER) is - 0.01: FER = 1 - (Number
of correctly received frames / Number of transmitted frames) at the input power level stated in ITU
section 7.1.2.5.7.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 34


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.12 TX to RX turnaround time


The transceiver of a Z-Wave device must be fast enough to switch from transmission mode to receive
mode, the so-called TX-to-RX turnaround time. The TX-to-RX turnaround time must be measured
under the test conditions given in ITU section 7.1.2.5.8. The TX-to-RX turnaround time measurements must be tested for all RF profiles listed in ITU table 7-1.


**3.12.1** **Prerequisites**


1. A Z-Wave device capable of transmitting and receiving, decoding and error handling Z-Wave
frames formatted according to ITU section 7.1.3. The Z-Wave device must be able to decode
and data process at transmissions rates stated in ITU table 7-2. The Z-Wave device must be
able to indicate when a frame is not correctly received, and all incoming Z-Wave frames must
be acknowledged. The Z-Wave device must set a GPIO, available for measurements with an
oscilloscope, to a state when leaving its transmission state and reverse the state of the GPIO
when the receiver of the Z-Wave device is fully initialized and ready to receive preamble-bits
from a Z-Wave frame. The Z-Wave receiver device is here after called DUT.

2. The Z-Wave device must be mounted on a PCB enabling a cabled RF connection between a RF
measurement device and a 50 Ohms matched output of the Z-Wave device.

3. The PCB must further enable a measurement using an oscilloscope on the designated GPIO pin
used for measuring TX-to-RX turnaround time measurements.

4. A golden Silicon Labs Z-Wave device which can transmit and receive Z-Wave coded data messages. Data must be transmitted according to ITU tables 7-2 to 7-6 and formatted at described
in ITU section 7.1.3. The test pattern generator must acknowledge all incoming Z-Wave traffic.
The Z-Wave transmitter is here after called test pattern generator.

5. A means to control the transmission of a Z-Wave frame from the pattern generator.

6. An oscilloscope, equivalent to a R&S RTO 1204 or better.


**3.12.2** **Measurement** **setup**


The DUT and the Z-Wave pattern generator are connected to each other through a coax cable. The
oscilloscope is connected to the GPIO pin of the DUT. The Z-Wave pattern generator is started, and
the pulse widths of the pulsing GPIO pin is measured with the oscilloscope.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 35


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025









Figure 3.13: TX-to-RX turnaround time setup


Table 3.8: Oscilloscope settings for TX-to-RX turnaround measurements







|Col1|Oscilloscope screen|Col3|Col4|Col5|
|---|---|---|---|---|
||ttx_to_rx|ttx_to_rx|ttx_to_rx|V<br>O|
||||||
||End of TX<br>Ready to RX||||


Figure 3.14: TX-to-RX measurement result


The number of transmitted frames from the Z-Wave pattern generator as well as the number of
received frames at the DUT must be recorded.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 36


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025


Note: If another method for measuring TX-to-RX turn-around time is possible, e.g. using a spectrum
analyzer in zero-span, this method is allowed to be used as well.


**3.12.3** **Measurement** **result**


The measurement result is the duration, t tx_to_rx in Figure 3.14, of the state change of the GPIO pin
of the DUT during the communication between the DUT and the Z-Wave pattern generator measured
for at least 10 state changes.

The DUT must have received and acknowledged all the frames transmitted by the Z-Wave pattern
generator.


**3.12.4** **Pass** **criteria**


The Z-Wave device shall pass the test if:

1. The TX-to-RX turnaround time, t tx_to_rx measured at least 10 times are less than stated in ITU
table 7-27 and all transmitted frames by the Z-Wave generator were received and acknowledged
by the Z-Wave device.


**3.12.5** **Fail** **criteria**


The Z-Wave device shall fail the test if:

1. Any of 10 sampled TX-to-RX turnaround times, t tx_to_rx for at least 10 samples were higher
than stated in ITU table 7-27 or not all transmitted frames by the Z-Wave generator were
received and acknowledged by the Z-Wave device.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 37


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.13 RX-to-TX turnaround time


The response time of the transceiver of a Z-Wave device must be fast enough to switch from receive
mode to transmit mode, the so-called RX-to-TX turnaround time. The RX-to-TX turnaround time
must be measured under the test conditions given in ITU section 7.1.2.5.9. The RX-to-TX turnaround
time measurements must be tested for all RF profiles listed in ITU table 7-1.

RX-to-TX turnaround times are depending on the MAC layer implementation and is thus not a part
of a PHY test. Refer to MAC test 5.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 38


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.14 Preamble field


Data frames transmitted by a Z-Wave device be formatted as described in ITU section 7.1.3.1: With a
preamble field, a Start of Frame delimiter, payload and an End of Frame delimiter. The requirements
for the number of preamble bytes to transmit are stated in ITU table 7-10.

The preambles are coded according to ITU tables 7-2, 7-4, 7-5 and 7-6.

The number of preamble types transmitted for each type of Z-Wave frame must be tested according
to ITU table 7-10 and tested for all RF profiles listed in ITU table 7-1.

Preambles are inserted into Z-Wave frames by the MAC layer and is thus not a part of a PHY test.
Refer to MAC test 2 & 3.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 39


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.15 Start of Frame field


The transceiver of a Z-Wave must be able to correctly transmit and correctly receive Z-Wave start of
frame information as described in ITU section 7.1.3.3. The data content of the Start of Frame field is
described in ITU table 7-11. The handling of Start of Frame field in Z-Wave frames must be tested
for all RF profiles listed in ITU table 7-1.

Start of Frame is inserted into Z-Wave frames by the MAC layer and is thus not a part of a PHY
test. Refer to MAC test 4.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 40


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 3.16 End of Frame field (optional)


Data frames transmitted by a Z-Wave device must be formatted as described in ITU section 7.1.3.1:
With a preamble field, a Start of Frame delimiter, payload and an End of Frame delimiter. If the
Z-Wave packet is transmitted with the data rate R1, the requirements for End of Frame field is given
in ITU section 7.13.5.

The End of Frame delimiter for data rate R1 must be tested for all RF profiles listed in ITU table
7-1. The End of Frame field is inserted into Z-Wave frames by the MAC layer and is thus not a part
of a PHY test.


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 41


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## 4 APPENDIX 4.1 Frequency, channel, and data rate overview









© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 42


Specifcations **Z-Wave** **PHY** **Test** **Specifcation,** **Release** **2.9.0** May 30, 2025

## References


[G.9] ITU-T, G9959. (01/2015).


© 2025 Z-Wave Alliance, Inc. All Rights Reserved This document may only be copied and distributed internally. Page 43


