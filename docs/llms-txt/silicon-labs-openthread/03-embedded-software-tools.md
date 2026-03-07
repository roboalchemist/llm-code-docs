# Source: https://docs.silabs.com/openthread/3.0.0/mfg-test-guidelines-efr32/03-embedded-software-tools.md

# Embedded Software Tools

Silicon Labs supports multiple embedded software tools for manufacturing test for the EFR32. This supports testing with a standalone test application or a test mode within the customer application.

## NodeTest

The NodeTest is a pre-built standalone application is provided with the EmberZNet SDK (Software Development Kit). Silicon Labs recommends that NodeTest be used only for radio boards in the kit for evaluation purposes. NodeTest provides a serial command line interface to the Silicon Labs device. Instructions for using NodeTest are provided in _AN1019: Using the NodeTest Application_. Note that NodeTest has been deprecated in EmberZNet SDK 7.0.

## Manufacturing Library

Silicon Labs recommends that customers use the manufacturing library in mature applications, regardless of the testing phase. Customers without mature applications can build a simple Zigbee sample application with the manufacturing library enabled to access this functionality. The manufacturing library provides access to a test mode within the application and removes the need for multiple application bootloads or multiple programming steps within the manufacturing process. The manufacturing library is available as a configurable component/plugin in the EmberZNet SDK. The guidelines for enabling the manufacturing library component/plugin and using the manufacturing library CLI commands for manufacturing tests are provided in [Using the Manufacturing Library for EmberZNet](https://docs.silabs.com/zigbee/latest/using-manufacturing-library-for-emberznet/).

## RAILtest

The RAILtest standalone application is provided with the Flex SDK. It provides customers with a simple tool for testing the radio and the functionality of the RAIL library. For any advanced usage customers should write their own software with a custom radio configuration. RAILtest is documented in [RAILtest User's Guide](https://docs.silabs.com/rail/latest/railtest-users-guide/), [EFR32 RF Evaluation Guide](https://docs.silabs.com/rail/latest/efr32-rf-eval-guide/), and [Bring-up/Test HW Development](https://docs.silabs.com/z-wave/latest/z-wave-bring-up-test-hardware-development/).

## Direct Test Mode protocol (DTM)

The DTM protocol is defined in the Bluetooth specification as a means for testing the radio performance of Bluetooth low energy products. Bluetooth-enabled Silicon Labs EFR32xG SoCs and the xGM modules support two approaches for RF PHY testing offered by DTM. One approach is where the RF PHY tester controls the DUT over the standardized HCI (host control interface) of the DUT. In another approach, the tester had direct access to the DUT through a dedicated 2-wire connection to control the radio tests on the DUT. More information on DTM testing is described in _AN1046: Bluetooth Radio Frequency Physical Layer Evaluation_.
