# Source: https://docs.aws.amazon.com/freertos/latest/portingguide/llms.txt

# FreeRTOS Porting Guide

> Provides detailed information about porting FreeRTOS to a microcontroller platform.

- [FreeRTOS Porting](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-guide.html)
- [Downloading FreeRTOS for Porting](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-download.html)
- [Setting up your workspace and project for porting](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-set-up-project.html)
- [Migrating from MQTT Version 3 to coreMQTT](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-migration-mqtt.html)
- [Migrating from version 1 to version 3 for OTA applications](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-migration-ota.html)
- [Migrating from version 1 to version 3 for OTA PAL port](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-migration-ota-pal.html)
- [Document history](https://docs.aws.amazon.com/freertos/latest/portingguide/doc-history.html)

## [Porting the FreeRTOS libraries](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting.html)

- [Porting flowchart](https://docs.aws.amazon.com/freertos/latest/portingguide/porting-chart.html): Use the porting flowchart below as a visual aid, as you port FreeRTOS to your board.
- [FreeRTOS kernel](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-kernel.html): The cFreeRTOS kernel for porting FreeRTOS.
- [Implementing the library logging macros](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-library-logging-macros.html): The FreeRTOS libraries use the following logging macros, listed in increasing order of verbosity.
- [TCP/IP](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-tcp.html): This section provides instruction for porting and testing on-board TCP/IP stacks.
- [corePKCS11](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-pkcs.html): The corePKCS11 library for testing and porting FreeRTOS.
- [Network Transport Interface](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-network-transport-interface.html): Learn about the Network Transport Interface library for testing and porting FreeRTOS.
- [coreMQTT](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-mqtt.html): The coreMQTT library for testing and porting FreeRTOS.
- [coreHTTP](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-corehttp.html): The coreHTTP library for testing and porting FreeRTOS.
- [Over-the-Air (OTA) updates](https://docs.aws.amazon.com/freertos/latest/portingguide/afr-porting-ota.html): Port your version of the over-the-air (OTA) library to FreeRTOS
- [Cellular Interface](https://docs.aws.amazon.com/freertos/latest/portingguide/freertos-porting-cellular.html): Learn how to port the FreeRTOS Cellular Interface library.
