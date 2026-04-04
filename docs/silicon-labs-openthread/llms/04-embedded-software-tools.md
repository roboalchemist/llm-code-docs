# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-overview/04-embedded-software-tools.md

# Embedded Software Tools

The embedded software application could be a standalone test application or the customer’s own application with a test mode included. Silicon Labs provides different test applications depending on the protocol being used. These applications are discussed in detail in [Manufacturing Test Guidelines for the EFR32](https://docs.silabs.com/zigbee/latest/mfg-test-guidelines-efr32/).

The following table summarizes the test tools provided by Silicon Labs.

|**Software Tool**|**Family**|**Protocol**|
|---|---|---|
|NodeTest|EFR32|Zigbee|
|Manufacturing Library|EFR32|Zigbee|
|RAILtest|EFR32|Zigbee / Bluetooth LE / OpenThread / Proprietary/Z-Wave|
|Direct Test Mode (DTM)|EFR32|Bluetooth LE|

**NodeTest**

The NodeTest standalone application is provided with the EmberZNet SDK (Software Development Kit). Silicon Labs recommends NodeTest for any test stage in which the customer’s Zigbee application is not yet mature enough to include a test mode. NodeTest provides a serial command line interface to the Silicon Labs device. Instructions for using NodeTest are provided in _AN1019: Using the NodeTest Application_.

**Manufacturing Library**

Silicon Labs recommends that customers use the manufacturing library in mature applications, regardless of the testing phase. Customers without mature applications can build a simple Zigbee sample application with the manufacturing library enabled to access this functionality. The manufacturing library provides access to a test mode within the application and removes the need for multiple application bootloads or multiple programming steps within the manufacturing process. The manufacturing library is available as a configurable plugin in the EmberZNet SDK. The guidelines for enabling the manufacturing library plugin and using the manufacturing library CLI commands for manufacturing tests are provided in [Using the Manufacturing Library for EmberZNet](https://docs.silabs.com/zigbee/latest/using-manufacturing-library-for-emberznet/).

**RAILtest**

The RAILtest standalone application is provided with the Flex SDK. It provides customers with a simple tool for testing the radio and the functionality of the RAIL library. For any advanced usage customers should write their own software with a custom radio configuration. RAILtest is documented in [RAILtest User's Guide](https://docs.silabs.com/rail/latest/railtest-users-guide/), [EFR32 RF Evaluation Guide](https://docs.silabs.com/rail/latest/efr32-rf-eval-guide/), and [Bring-up/Test HW Development](https://docs.silabs.com/z-wave/latest/z-wave-bring-up-test-hardware-development/).

**Direct Test Mode protocol (DTM)**

The DTM protocol is defined in the Bluetooth specification as a means for testing the radio performance of Bluetooth low energy products Bluetooth-enabled Silicon Labs EFR32xG SoCs and the BGM/MGM modules support both the DTM upper and lower testers. DTM testing is described in _AN1046: Radio Frequency Physical Layer Evaluation in the Bluetooth® SDK v2.x_ and [Radio Frequency Physical Layer Evaluation in Bluetooth® SDK v3.x](https://docs.silabs.com/bluetooth/latest/bt-rf-phy-evaluation-using-dtm-sdk-v3x/).