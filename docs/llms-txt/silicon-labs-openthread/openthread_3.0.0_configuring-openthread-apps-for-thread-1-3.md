# Source: https://docs.silabs.com/openthread/3.0.0/configuring-openthread-apps-for-thread-1-3/index.md

# Configuring OpenThread Applications for Thread 1.3

> **NOTE: This section replaces _AN1372: Configuring OpenThread Applications for Thread 1.3_. Further updates to this application note will be provided here**.

Thread 1.3 builds on Thread 1.1 and Thread 1.2’s robust foundation. It defines enhancements and additions to the Thread Border Router definition to enable bidirectional IPv6 connectivity, service discovery using DNS, and IPv4-backwards support using NAT. It includes support for Thread-over-infrastructure (non-802.15.4 IPv6) links. Finally, to remedy throughput concerns, the specification defines support for TCP as a standard component and protocol.

> **Note**: Starting with the **Simplicity SDK 2024.12.0** release, Silicon Labs includes the OpenThread stack with the current default protocol version 1.4 (=5). Prior releases defaulted to protocol version 1.3. For information on configuring OpenThread Applications for Thread 1.4, see [Configuring OpenThread Applications for Thread 1.4](/openthread/{build-docspace-version}/configuring-openthread-apps-for-thread-1-4).

Note that the Thread 1.3 border router certification program was sunset at the end of 2025, after which only Thread 1.4 border router certification applications may be submitted. Thread 1.3 components and end products may still be certified.

Silicon Labs provides components and configuration options that enable you to configure Thread 1.3 features with sample applications. These features are compatible with EFR32MG1x and EFR32MG2x SoCs, RCPs, and modules. This application note assumes you have a basic understanding of how Thread is implemented on EFR32 devices. For more information, see [Thread Fundamentals](/openthread/{build-docspace-version}/thread-fundamentals).

## Key Points

- Including Thread 1.3 features in SoC Applications.
- Including Thread 1.3 features in an OpenThread Border Router.