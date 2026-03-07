# Source: https://docs.silabs.com/openthread/3.0.0/openthread-single-band-proprietary-sub-ghz/index.md

# Single-Band Proprietary Sub-GHz Support with OpenThread

**NOTE: This section replaces _AN1350: Single-Band Proprietary Sub-GHz Support with OpenThread_. Further updates to this application note will be provided here.**

This application note describes how to configure OpenThread applications to operate on a proprietary sub-GHz band using the Silicon Labs OpenThread software development kit (SDK) and Simplicity Studio with a compatible wireless starter kit (WSTK). It also provides details on the proprietary Radio PHY supported with this feature.

Sub-GHz radios, like 2.4 GHz ones, can offer relatively simple wireless solutions. When compared to 2.4 GHz, sub-GHz offers several advantages, depending on the target application.

Some notable advantages of using sub-GHz radios are:

- Longer range
- Less signal fading in congested environments
- Low interference
- Low power

This application note provides a step-by-step guide to creating, building, and running an OpenThread application on a sub-GHz band.

As Thread is a 2.4GHz protocol and the specification currently does not support a sub-GHz feature, sub-GHz support has been added using:

- Proprietary radio PHY made available with the SDK and,
- Proprietary radio configurations supported by the OpenThread stack.

> **Note**: This feature currently supports single-band operation only and so requires all the nodes in a mesh to be operating on the same sub-GHz band.

Our newest embedded software platform, the Simplicity Software Development Kit (SDK), is designed specifically for our Series 2 and Series 3 devices. The Simplicity SDK is a significant advancement in IoT development, providing our customers with a cohesive development environment for wireless innovation. It enables wireless developers to utilize advanced features and capabilities with the most recent Silicon Labs IoT devices.

Meanwhile, our Gecko Software Development Kit (GSDK) will continue to be available for users of our Series 0 and Series 1 devices. For additional information on Series 0 and Series 1 devices, refer to Series 0 and Series 1 EFM32/EZR32/EFR32 devices on silabs.com.

## Proprietary Sub-GHz Radio PHY

For wireless applications to operate on a particular frequency band, the applications typically need the radio implementation to provide the necessary PHY support. For OpenThread applications supported on Silicon Labs platforms, the platform abstraction layer supports the 2.4GHz band by default. For the sub-GHz feature, proprietary radio PHY support has been added.

This section describes the proprietary radio PHY specifications that have been used to support this feature. The PHY specifications are compliant with the NA FCC Part 15.247 regulations.

### Modulation Details

The proprietary radio PHY currently supported with the OpenThread SDK uses the following modulation specifications.

|Parameter|Configuration|
|---|---|
|Modulation|2-Level GFSK|
|Data Rate|500 kbps|
|Tx Filter BT|0.5 (Gaussian)|
|Modulation Index|0.76|

### Channel and Frequency Specifications

Similarly, the channel and frequency specifications for the proprietary radio PHY, and the center frequency for the supported channels have been captured in the following tables.

#### Proprietary Sub-GHz PHY Band Parameters

|Band Parameters|Value|
|---|---|
|Channel Page|23|
|Frequency Band (MHz)|902- 928|
|Channel Spacing (MHz)|1.0|
|Total Channels|25|
|Channel Numbers|0 – 24|
|1st Channel Center Freq. (MHz)|903.0|

#### Channels and Center Frequencies for 902-928 MHz Band

|Chan. #|Fc (MHz)|
|---|---|
|0|903.0|
|1|904.0|
|…|…|
|23|926.0|
|24|927.0|

### PHR Length

The proprietary radio PHY supports 2-byte PHR. With a supported PSDU of 127 bytes, the last 7 bits of the 2nd byte represent the Frame Length.

## Hardware Limitations

The proprietary sub-GHz feature is currently supported on radio boards supporting the 915 MHz band and using EFR32MG12 or EFR32MG13 parts only. Radio boards that could be used to test this feature are BRD4164a, BRD4170a and BRD4158a.