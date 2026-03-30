# Source: https://docs.silabs.com/openthread/3.0.0/openthread-developing-debugging-overview/index.md

# Developing and Debugging Silicon Labs OpenThread Applications

These pages provide details on developing and debugging OpenThread applications. Content
includes:

- [**Configuring and Building OpenThread Applications for Sleepy Devices**](/openthread/3.0.0/openthread-sleepy-devices): Describes how to configure OpenThread applications to operate on a proprietary sub-GHz band using the Silicon Labs OpenThread SDK and Simplicity Studio with a compatible mainboard. It also provides details on the proprietary radio PHY supported with this feature.
- [**Single-Band Proprietary Sub-GHz Support with OpenThread**](/openthread/3.0.0/openthread-single-band-proprietary-sub-ghz): Describes how to configure OpenThread applications to operate on a proprietary sub-GHz band using the Silicon Labs OpenThread SDK and Simplicity Studio with a compatible mainboard. It also provides details on the proprietary radio PHY supported with this feature.
- [**Using OpenThread with Free RTOS**](/openthread/3.0.0/openthread-with-free-rtos): Describes how to build OpenThread applications with FreeRTOS.
- [**Configuring OpenThread Applications for Thread 1.3**](/openthread/3.0.0/configuring-openthread-apps-for-thread-1-3): Provides instructions for configuring OpenThread SoC and Border Router applications to use Thread 1.3 features.
- [**Configuring OpenThread Applications for Thread 1.4**](/openthread/3.0.0/configuring-openthread-apps-for-thread-1-4): Provides instructions for configuring OpenThread SoC and Border Router applications to use Thread 1.4 features.

## Development Tools

**Simplicity Studio and the Simplicity IDE**: Simplicity Studio® is the unified development environment for all Silicon Labs technologies, SoCs, and modules. It provides you with access to the target device-specific web and SDK resources, software and hardware configuration tools, and an integrated development environment (IDE) featuring industry-standard code editors, compilers, and debuggers. See the [Simplicity Studio page](https://www.silabs.com/developers/simplicity-studio) to download the tools and for more information.

**Network Analyzer**: Simplicity Studio's Network Analyzer enables debugging of complex wireless systems. This tool captures a trace of wireless network activity that can be examined in detail live or at a later time. See the Network Analyzer section of the Simplicity Studio User's Guide for more information.

**Wireshark**: Download instructions are provided for [Windows/Mac users](https://www.wireshark.org/download.html) or [Linux users](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallUnixInstallBins.html). Simplicity Studio supports live interaction between the application running on a Silicon Labs device and Wireshark.

**Energy Profiler**: Simplicity Studio's Energy Profiler enables you to visualize the energy consumption of individual devices, multiple devices on one target system, or a network of interacting wireless devices to analyze and improve the power performance of these systems. Real-time information on current consumption is correlated with the program counter providing advanced energy software monitoring capabilities. It also provides a basic level of integration with the Network Analyzer network analysis tool. See the Energy Profiler section of the Simplicity Studio User's Guide for more information.

**Simplicity Commander**: Simplicity Commander is a single, all-purpose tool to be used in a production environment. It is invoked using a simple Command Line Interface (CLI) that is also scriptable. Simplicity Commander enables customers to complete essential tasks such as configuring and building applications and bootloaders and flashing images to their devices. Simplicity Commander is available through Simplicity Studio or can be downloaded through [system-specific installers](https://www.silabs.com/developers/mcu-programming-options#programming). The Simplicity Commander User's Guide provides more information.

**Silicon Labs Configurator (SLC)**: SLC offers command-line access to application configuration and generation functions. Software Project Generation and Configuration with SLC-CLI provides instructions on downloading and using the SLC-CLI tool.