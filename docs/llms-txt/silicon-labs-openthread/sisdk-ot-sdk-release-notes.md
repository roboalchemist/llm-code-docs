# Source: https://docs.silabs.com/openthread/3.0.0/sisdk-ot-release-notes/sisdk-ot-sdk-release-notes.md

# OpenThread SDK Version 3.0.0 - Release Notes (Jan 22, 2026)

[**OpenThread Version 3.0.0**](.)

Thread is a secure, reliable, scalable, and upgradeable wireless IPv6 mesh networking protocol. It provides low-cost bridging to other IP networks while optimized for low-power/battery-backed operation. The Thread stack is designed specifically for Connected Home applications where IP-based networking is desired and a variety of application layers may be required.

OpenThread, released by Google, is an open-source implementation of Thread. Google has released OpenThread to accelerate the development of products for the connected home and commercial buildings. With a narrow platform abstraction layer and a small memory footprint, OpenThread is highly portable. It supports system-on-chip (SoC), network co-processor (NCP), and radio co-processor (RCP) designs.

Silicon Labs has developed an OpenThread-based SDK tailored to work with Silicon Labs hardware. The Silicon Labs OpenThread SDK is a fully tested enhanced version of the GitHub source. It supports a broader range of hardware than does the GitHub version and includes documentation and example applications not available on GitHub.

Click [here](https://github.com/SiliconLabs/simplicity_sdk/tags) for earlier releases.

## Release Summary

[Key Features](#key-features) | [API Changes](#api-changes) | [Bug Fixes](#bug-fixes) | [Chip Enablement](#chip-enablement)

### Key Features

- Continued compliance for Thread 1.4 on SoC and OTBR.
- OpenThread Border Router in NCP mode with Thread 1.3 feature support.
- Multi-PAN support for Thread in SoC mode.

### API Changes

Refer to API changes as documented [here](https://openthread.io/reference/api-updates), starting with the changes on May 23, 2025 and ending with the changes on November 11, 2025.

### Bug Fixes

- Added sample app board restrictions.
- Studio Configuration Fixes.
- Targeted quality improvements and bug fixes.

### Chip Enablement

None.

## Key Features

[New Features](#new-features) | [Enhancements](#enhancements) | [Removed Features](#removed-features) | [Deprecated Features](#deprecated-features)

### New Features

#### Continued compliance for Thread 1.4 on SoC and OTBR

Thread 1.4 specification introduces the following mandatory features for the Border Router:

- **Thread Credential Sharing**  
  - Provides a standard protocol to allow Administrator access to Thread Border Routers.  
  - Enables authentication via a short one-time/ephemeral “Thread Administrator Passcode”.
- **Diagnostics: Network Management and Troubleshooting**  
  With Mesh devices having transient roles and being difficult to troubleshoot, this feature:  
  - Enables enumeration of network participants and means to recreate network state at any time.  
  - Disambiguates distinctions between various network layers.  
  - Helps classify network diagnostic information for user purposes.
- **Thread over Infrastructure aka TREL**  
  - Allows Thread to utilize Wi-Fi/Ethernet links in the Thread mesh topology.  
  - Enables merging of Thread Partitions over Wi-Fi/Ethernet.
- **Public Internet Connectivity IPv4 / IPv6 support**  
  DHCPv6 prefix delegation supports IPv6 prefix delegation and distribute prefixes in the interior network. Also enables DHCPv6-PD client support in the external IPv6 network.
- **Outbound IPv4 connectivity**  
  To support stateful NAT64 as a solution for IPv6/IPv4 translation.
- **DNS Recursive Resolver**  
  Allows subscriptions over TLS/TCP (where TCP is preferred over UDP because service lists can lead to quite large packets).
- **TCP (Bulk Transfer Protocol)**  
  Support for TCP as a standard component/protocol on Thread stacks to remedy throughput shortcomings for Bulk Transfer.

#### OpenThread Border Router in NCP mode with Thread 1.3 feature support

This release adds Thread 1.3 support to the OpenThread Thread Border Router using the Network Co-Processor (NCP) architecture.

#### Multi-PAN support for Thread in SoC mode

This release adds Multi-PAN (multi-instance) support for Thread in SoC mode to the OpenThread Platform Abstraction Layer (PAL). OpenThread typically supports only a single instance per device. Enabling multiple instances allows one device to participate in multiple independent Thread networks simultaneously. This is useful for applications that require network isolation or concurrent operation of separate Thread networks.

This feature is distinct from Multi-PAN RCP. In a Multi-PAN Radio Co-Processor (RCP) configuration, a host processor manages multiple IEEE 802.15.4 networks through a single RCP. The RCP does not maintain network state; it simply provides radio services for multiple networks managed by the host. This setup is often used to run a Zigbee and a Thread network concurrently. By contrast, in a multi-instance SoC application, multiple OpenThread stacks run directly on the SoC, allowing the device itself to join and operate in several independent Thread networks using its own local resources.

This release also includes three new sample applications that demonstrate multi-instance support:

- ot-cli-ftd-multi-instance
- ot-cli-mtd-multi-instance
- ot-ble-dmp-multi-instance

These sample applications extend the existing ot-cli-ftd, ot-cli-mtd, and ot-ble-dmp applications by adding multi-instance support and the new multi-instance CLI component. This component enables you to switch between, control, and monitor individual Thread instances from a single command-line interface. You can:

- List all active instances
- Switch the CLI context to a specific instance
- Perform instance-specific operations: attach, detach, form network, and more

### Enhancements

- Multi-instance support for OpenThread SoC apps  
  Added support for multiple static OpenThread instances for SoC app configurations. The following sample apps were added to show the use of this multi-instance support: ot-cli-ftd-multi-instance, ot-cli-mtd-multi-instance, and ot-ble-dmp-multi-instance.
- Reorganization of ot-ncp sample application folders  
  The ot-ncp sample application variants have been reorganized into separate folders based on whether they require CPC or Bluetooth.
- OPENTHREAD_CONFIG_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS  
  The OPENTHREAD_CONFIG_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS option has been removed from certification configurations, as it can lead to sub-optimal power consumption for sleepy devices
- Source match table size validation  
  When the source match table in spinel on the host is larger than the source match tables on the RCP an error of "NoBufs" can be returned by the RCP after an RCP reset and during the restoration process of the source match table. This is because the host has more entries than the RCP tables can hold. To address this we now ensure the size of the RCP Source Match Table is large enough to support the maximum number of children for all interfaces on the host, including Zigbee in a multiprotocol environment.

### Removed Features

None.

### Deprecated Features

None.

## API Changes

Refer to API changes as documented [here](https://openthread.io/reference/api-updates) starting with the changes on May 23, 2025 and ending with the changes on November 11, 2025.

## Bug Fixes

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Issue Description</th>
            <th>GitHub / Salesforce Reference (if any)</th>
            <th>Affected Software Variants, Hardware, Modes, Host Interfaces</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1187748</td>
            <td>Use the RAIL API RAIL_IEEE802154_SetRxToEnhAckTx to selectively set higher RxToTx for enhanced ACKs only. Previously, we were globally setting this higher RxToTx value for all ACKs.</td>
            <td>None</td>
            <td>All OPNs, boards, modes and interfaces</td>
        </tr>
        <tr>
            <td>1415275, 1503788</td>
            <td>Addressed a RAIL issue dealing with wraps of the microsecond timer.</td>
            <td>00332010</td>
            <td>All OPNs, boards, modes and interfaces</td>
        </tr>
        <tr>
            <td>1475140</td>
            <td>Addressed an issue where the txpower cli command would report the power as a negative number when the txpower was set at or above 13dBm.</td>
            <td>None</td>
            <td>All OPNs, boards, modes and interfaces</td>
        </tr>
        <tr>
            <td>1476240</td>
            <td>For Debian bookworm-based installations, when installing the ot-br-posix debian file, make sure the dhcpcd package on your target system is higher than the recommended bookworm version of 9.4.1-24, which has a known issue. The bookworm-backports apt source provides version 10.1.0 which is highly recommended. If not, we recommend updating your dhcpcd package version to at least 9.5.1.</td>
            <td>None</td>
            <td>Host processors using Debian packages</td>
        </tr>
        <tr>
            <td>1491593</td>
            <td>In Simplicity Studio, the rcp-spi-802154 and rcp-spi-802154-blehci sample apps are no longer available for boards chosen without a SPI capable external header.</td>
            <td>None</td>
            <td>Boards without a SPI capable external header</td>
        </tr>
        <tr>
            <td>1499349</td>
            <td>The OpenThread BLE DMP – SoC FreeRTOS (TrustZone) sample app should not show up as an available app for xGM270s modules and has been removed.</td>
            <td>None</td>
            <td>270S Module</td>
        </tr>
        <tr>
            <td>1507808</td>
            <td>Fixed a hard fault which could occur when utilsSoftSrcMatchShortFindEntry was called with an invalid Iid.</td>
            <td>00331602</td>
            <td>All OPNs, boards, modes and interfaces</td>
        </tr>
        <tr>
            <td>1511829</td>
            <td>In Simplicity Studio, the sleepy_demo_ftd, sleepy_demo_mtd, and sleepy_demo_ssed sample apps are no longer available for boards that don't have at least 2 buttons.</td>
            <td>None</td>
            <td>Boards without 2 buttons</td>
        </tr>
        <tr>
            <td>1560101</td>
            <td>Addressed issues where configurable component options were not showing up correctly in the configuration editor in Simplicity Studio.</td>
            <td>None</td>
            <td>All OPNs, boards, modes and interfaces</td>
        </tr>
    </tbody>
</table>

## Chip Enablement

None.

## Application Example Changes

[New Examples](#new-examples) | [Modified Examples](#modified-examples) | [Removed Examples](#removed-examples) | [Deprecated Examples](#deprecated-examples)

### New Examples

<table>
    <thead>
        <tr>
            <th>Example Name</th>
            <th>Description</th>
            <th>Supported Software Variants (if applicable)</th>
            <th>Supported Modes</th>
            <th>Supported OPNs / Boards / OPN Combinations</th>
            <th>Supported Host Interfaces</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>ot-ncp-ftd-cpc</p>
                <p> See <a href="https://github.com/SiliconLabsSoftware/sisdk-release/blob/sisdk-2025.12/openthread_app/ot-ncp/ot/README-OT-NCP.md"> README.</a></p>
            </td>
            <td>This is a simple OpenThread Full Thread Device NCP application with CPC. This is equivalent to the ot-ncp-ftd application in the OpenThread GitHub repo.</td>
            <td>Full Thread Device</td>
            <td>NCP</td>
            <td>All OPNs, boards, modes and interfaces</td>
            <td>All interfaces</td>
        </tr>
        <tr>
            <td>
                <p>ot-ncp-mtd-cpc</p>
                <p> See <a href="https://github.com/SiliconLabsSoftware/sisdk-release/blob/sisdk-2025.12/openthread_app/ot-ncp/ot/README-OT-NCP.md"> README.</a>
                </p>
            </td>
            <td>This is a simple OpenThread Minimal Thread Device NCP application. This is equivalent to the ot-ncp-mtd application in the OpenThread GitHub repo.</td>
            <td>Minimal Thread Device</td>
            <td>NCP</td>
            <td>All OPNs, boards, modes and interfaces</td>
            <td>All interfaces</td>
        </tr>
        <tr>
            <td>
                <p>ot-ble-dmp-multi-instance</p>
                <p> See <a href="https://github.com/SiliconLabsSoftware/sisdk-release/tree/sisdk-2025.12/openthread_app/ot-ble-dmp/multi-instance/README.md"> README.</a></p>
            </td>
            <td>This is a simple application to test DMP (Dynamic MultiProtocol) with OpenThread multi-instance and Bluetooth running on FreeRTOS.</td>
            <td>Full Thread Device, DMP, multi-instance</td>
            <td>SoC</td>
            <td>All OPNs, boards, modes and interfaces</td>
            <td>All interfaces</td>
        </tr>
    </tbody>
</table>

### Modified Examples

- The following CPC enabled sample apps have been moved from sample-apps/ot-ncp to sample-apps/ot-ncp/cpc  
  - ot-ncp-ftd-cpc.slcp  
  - ot-ncp-mtd-cpc.slcp  
  - rcp-spi-802154.slcp  
  - rcp-uart-802154.slcp
- The following non-CPC enabled sample apps have been moved from sample-apps/ot-ncp to sample-apps/ot-ncp/ot  
  - ot-ncp-ftd.slcp  
  - ot-ncp-mtd.slcp  
  - ot-rcp-spi.slcp  
  - ot-rcp.slcp
- The following BLE DMP enabled RCP sample apps have been moved from sample-apps/ot-ncp to sample-apps/ot-ncp/dmp  
  - rcp-spi-802154-blehci.slcp  
  - rcp-uart-802154-blehci.slcp

### Removed Examples

None.

### Deprecated Examples

None.

## Known Issues and Limitations

Issues in bold were added since the previous release.

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Issue or Limitation Description</th>
            <th>GitHub / Salesforce Reference (if any)</th>
            <th>Workaround (if any)</th>
            <th>Affected Software Variants, Hardware, Modes, Host Interfaces</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1506512</td>
            <td>OpenThread applications may experience sporadic failures when instruction cache (ICACHE) is disabled on SixG301 devices.</td>
            <td>None</td>
            <td>It is recommended to keep ICACHE enabled to ensure stable operation.</td>
            <td>SixG301 devices</td>
        </tr>
        <tr>
            <td>1559163</td>
            <td>When running in a Host/NCP architecture and repeatedly sending factory resets to the NCP, after approximately 15 times the host will stop sending messages to the NCP.</td>
            <td>None</td>
            <td>The correct procedure when factory resetting the NCP is to also reset the host at the same time.</td>
            <td>Host / NCP architectures</td>
        </tr>
        <tr>
            <td>1566197</td>
            <td>Thread communication can be disrupted between a pair of devices in which a ble connection is re-opened after previously being closed.</td>
            <td>None</td>
            <td>None</td>
            <td>SoC DMP architectures with BLE</td>
        </tr>
    </tbody>
</table>