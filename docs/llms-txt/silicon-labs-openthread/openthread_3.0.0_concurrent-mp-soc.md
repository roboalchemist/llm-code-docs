# Source: https://docs.silabs.com/openthread/3.0.0/concurrent-mp-soc/index.md

# Running Matter with OpenThread, Zigbee, and Bluetooth Concurrently on a System-on-Chip

> **Note: This section replaces _AN1418: Running Zigbee, OpenThread, and Bluetooth Concurrently on a System-on-Chip_. Further updates to this application note will be provided here**.

This application note describes how to run a combination of Zigbee, Matter with OpenThread, and Bluetooth networking stacks and the Zigbee application layer on a System-on-Chip (SoC). One of the main functions of a Concurrent Multiprotocol (CMP) device is to act as a bridge between Zigbee and OpenThread networks.

Note that, depending on the chip, memory size restrictions may prevent running Matter on SoC devices.