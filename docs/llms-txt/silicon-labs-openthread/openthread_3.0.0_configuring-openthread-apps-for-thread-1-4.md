# Source: https://docs.silabs.com/openthread/3.0.0/configuring-openthread-apps-for-thread-1-4/index.md

# Configuring OpenThread Applications for Thread 1.4

> **NOTE: This section replaces _AN1499: Configuring OpenThread Applications for Thread 1.4_. Further updates to this application note will be provided here**.

Thread 1.4 builds on Thread’s robust foundation. Thread 1.4 border routers seamlessly allow onboarding devices by making use of a standardized way to share credentials and join Thread networks. Device manufacturers can add compelling new features and offer dynamic support and cloud-powered features. Thread 1.4 also allows enhanced mesh diagnostics by providing more thorough visibility into a Thread mesh topology. Additionally, for professional installations and commercial building scenarios, Thread 1.4 defines secure commissioning at scale by using authenticated transport layers over standards such as Bluetooth.

> **Note**: Silicon Labs includes the OpenThread stack with the current default protocol version 1.4 (=5). All mandatory features in 1.3, 1.2, and 1.1 are automatically enabled, and the stack is backwards compatible.

Please note that the Thread 1.3 border router certification program is being sunset at the end of 2025, after which only Thread 1.4 border router certification applications may be submitted. Thread 1.3 components and end products may still be certified.

Silicon Labs provides components and configuration options that enable you to configure Thread 1.4 features with sample applications. These features are compatible with EFR32MG1x and EFR32MG2x SoCs, RCPs, and modules. This application note assumes you have a basic understanding of how Thread is implemented on EFR32 devices. For more information, see [Thread Fundamentals](/openthread/{build-docspace-version}/thread-fundamentals).

## Key Points

- Including Thread 1.4 features in SoC Applications.
- Including Thread 1.4 features in an OpenThread Border Router.