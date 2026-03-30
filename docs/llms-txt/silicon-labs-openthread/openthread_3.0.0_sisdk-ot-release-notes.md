# Source: https://docs.silabs.com/openthread/3.0.0/sisdk-ot-release-notes/index.md

# OpenThread Version 3.0.0 - Release Notes (Jan 22, 2026)

The OpenThread SDK is an enhanced version of the open-source OpenThread implementation released by Google that has been tailored to work with Silicon Labs hardware.

Click [here](https://github.com/SiliconLabs/simplicity_sdk/tags) for earlier releases.

## Release Summary

<table>
    <thead>
        <tr>
            <th>Release Item</th>
            <th>Version</th>
            <th>Release Date</th>
            <th>Release Notes</th>
            <th>Key Features</th>
            <th>API Changes</th>
            <th>Bug Fixes</th>
            <th>Chip Enablement</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>OpenThread SDK</p>
            </td>
            <td>
                <p>3.0.0</p>
            </td>
            <td>
                <p>Jan 22, 2026</p>
            </td>
            <td>
                <p><a href="sisdk-ot-sdk-release-notes">Release Notes</a></p>
            </td>
            <td>
                <ul>
                    <li>Continued compliance for Thread 1.4 on SoC and OTBR</li>
                    <li>OpenThread Border Router in NCP mode with Thread 1.3 feature support</li>
                    <li>Multi-PAN support for Thread in SoC mode</li>
                </ul>
            </td>
            <td>Refer to API changes as documented <a href="https://openthread.io/reference/api-updates">here</a> starting with the changes on May 23, 2025 and ending with the changes on November 11, 2025.</td>
            <td>
                <ul>
                    <li>Added sample app board restrictions</li>
                    <li>Studio Configuration Fixes</li>
                    <li>Targeted quality improvements and bug fixes</li>
                </ul>
            </td>
            <td>None</td>
        </tr>
        <tr>
            <td>
                <p>802.15.4 Mesh + BLE Multiprotocol</p>
            </td>
            <td>
                <p>3.0.0</p>
            </td>
            <td>
                <p>Jan 22, 2026</p>
            </td>
            <td>
                <p><a href="sisdk-ot-multiprotocol-release-notes">Release Notes</a></p>
            </td>
            <td>
                <ul>
                    <li>Concurrent Listening support with CMP on SiMG301x.</li>
                    <li>Bi-directional Green Power support with CMP Zigbee NCP + OpenThread RCP.</li>
                </ul>
            </td>
            <td>None</td>
            <td>Targeted quality improvements and bug fixes.</td>
            <td>
                <ul>
                    <li>xGM270S Leopard SiP Module GA SW support.</li>
                    <li>xG301 Explorer Kit and Pro-kit support.</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

## Impact of Release Changes

[Impact Statements](#impact-statements) | [Migration Guide](#migration-guide)

### Impact Statements

<table>
    <thead>
        <tr>
            <th>Change </th>
            <th>Impact</th>
            <th>Affected Software Variants if applicable</th>
            <th>Affected Modes</th>
            <th>Affected OPNs / Boards / OPN Combinations</th>
            <th>Affected Host Interfaces</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>NCP upgrades</p>
            </td>
            <td>Need to update existing applications.</td>
            <td>
                <p>NCP</p>
            </td>
            <td>
                <p>All</p>
            </td>
            <td>
                <p>All</p>
            </td>
            <td>
                <p></p>
            </td>
        </tr>
    </tbody>
</table>

### Migration Guide

**NCP upgrades**: When upgrading NCP sample applications to sisdk-2025.12, any customized component configurations must be re-applied to the upgraded project.

## Using This Release

[What's in the Release?](#what-s-in-the-release) | [Compatible Software](#compatible-software) | [Installation and Use](#installation-and-use) | [Help and Feedback](#help-and-feedback)

### What's in the Release?

- Silicon Labs OpenThread stack
- Silicon Labs OpenThread sample applications
- Silicon Labs OpenThread border router

### Compatible Software

<table>
    <thead>
        <tr>
            <th>Software</th>
            <th>Compatible Version or Variant</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Simplicity SDK</td>
            <td>2025.12.0</td>
        </tr>
        <tr>
            <td>GCC (The GNU Compiler Collection)</td>
            <td>12.2.1 (provided with Simplicity Studio)</td>
        </tr>
    </tbody>
</table>

### Installation and Use

The OpenThread SDK is part of the Simplicity SDK, the suite of Silicon Labs SDKs. To quickly get started with OpenThread and the Simplicity SDK, install [Simplicity Studio](https://www.silabs.com/developer-tools/simplicity-studio), which will set up your development environment and walk you through Simplicity SDK installation. Simplicity Studio includes everything needed for IoT product development with Silicon Labs devices, including a resource and project launcher, software configuration tools, full IDE with GNU toolchain, and analysis tools.

Alternatively, Simplicity SDK may be installed manually by downloading or cloning the latest from GitHub. See [https://github.com/SiliconLabsSoftware/sisdk-release](https://github.com/SiliconLabsSoftware/sisdk-release) for more information.

Documentation specific to the SDK version is installed with the SDK. API references and other information about this release are available
on [https://docs.silabs.com/openthread/latest/](https://docs.silabs.com/openthread/latest/). Select your SDK version in the upper right.

For more information about the OpenThread SDK see [Silicon Labs OpenThread QuickStart Guide](https://docs.silabs.com/openthread/latest/openthread-quick-start-guide/).

If you are new to Thread see [Thread Fundamentals](https://docs.silabs.com/openthread/latest/thread-fundamentals/).

To review Security and Software Advisory notifications and manage your notification preferences:

1. Go to [https://community.silabs.com/](https://community.silabs.com/).
2. Log in with your account credentials.
3. Click your profile icon in the upper-right corner of the page.
4. Select **Notifications** from the dropdown menu.
5. In the Notifications section, go to the **My Product Notifications** tab to review historical Security and Software Advisory notifications
6. To manage your preferences, use the **Manage Notifications** tab to customize which product updates and advisories you receive.

To learn more about the software in this release, dive into our [online documentation](https://docs.silabs.com/openthread/2.7.2/openthread-start/).

#### Additional Information

- **OpenThread GitHub Repository**  
  The Silicon Labs OpenThread SDK includes all changes from the OpenThread GitHub repo [https://github.com/openthread/openthread](https://github.com/openthread/openthread) up to and including commit **61e43cffb**. An enhanced version of the OpenThread repo can be found in the following Simplicity Studio 5 GSDK location: <GSDK Installation Location>\util\third_party\openthread
- **OpenThread Border Router GitHub Repository**  
  The Silicon Labs OpenThread SDK includes all changes from the OpenThread border router GitHub repo [https://github.com/openthread/ot-br-posix](https://github.com/openthread/ot-br-posix) up to and including commit **ab0c1351e**. An enhanced version of the OpenThread repo can be found at the following location: [https://github.com/SiliconLabsSoftware/sisdk-release/tree/sisdk-2025.12/openthread_stack/util/third_party/openthread](https://github.com/SiliconLabsSoftware/sisdk-release/tree/sisdk-2025.12/openthread_stack/util/third_party/openthread).
- **Using the Border Router**  
  For ease of use, Silicon Labs recommends the use of a Docker container for your OpenThread border router. Refer to [Using the Silicon Labs RCP with the OpenThread Border Router](https://docs.silabs.com/openthread/latest/using-sl-rcp-with-openthread-border-router/index.html) for details on how to set up the correct version of OpenThread border router Docker container. It is available at [https://hub.docker.com/r/siliconlabsinc/openthread-border-router](https://hub.docker.com/r/siliconlabsinc/openthread-border-router). If you are manually installing a border router, using the copies provided with the Silicon Labs OpenThread SDK, refer to [Using the Silicon Labs RCP with the OpenThread Border Router](https://docs.silabs.com/openthread/latest/using-sl-rcp-with-openthread-border-router/index.html) for more details. Although updating the border router environment to a later GitHub version is supported on the OpenThread website, it may make the border router incompatible with the OpenThread RCP stack in the SDK.
- **Secure Vault Integration**  
  When deployed to Secure Vault High devices, sensitive keys are protected using the Secure Vault Key Management functionality. The following table shows the protected keys and their storage protection characteristics.  
  Wrapped keys that are marked as “Non-Exportable” can be used but cannot be viewed or shared at runtime.  
  Wrapped keys that are marked as “Exportable” can be used or shared at runtime but remain encrypted while stored in flash.  
  For more information on Secure Vault Key Management functionality, see [Secure Key Storage](https://docs.silabs.com/openthread/latest/efr32-secure-key-storage/).

<table>
    <thead>
        <tr>
            <th>Wrapped Key</th>
            <th>Exportable / Non-Exportable</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                Thread Master Key
            </td>
            <td>
                Exportable
            </td>
            <td>
                Must be exportable to form the TLVs
            </td>
        </tr>
        <tr>
            <td>
                PSKc
            </td>
            <td>
                Exportable
            </td>
            <td>
                Must be exportable to form the TLVs
            </td>
        </tr>
        <tr>
            <td>
                Key Encryption Key
            </td>
            <td>
                Exportable
            </td>
            <td>
                Must be exportable to form the TLVs
            </td>
        </tr>
        <tr>
            <td>
                MLE Key
            </td>
            <td>
                Non-Exportable
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                Temporary MLE Key
            </td>
            <td>
                Non-Exportable
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                MAC Previous Key
            </td>
            <td>
                Non-Exportable
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                MAC Current Key
            </td>
            <td>
                Non-Exportable
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                MAC Next Key
            </td>
            <td>
                Non-Exportable
            </td>
            <td>
            </td>
        </tr>
    </tbody>
</table>

- **Thread Certification**  
  This release has been qualified for Thread 1.4 compliance for the SoC and Border Router (Host-RCP architecture) using the Thread Test Harness v64.0 (latest available Member Release). For this release Silicon Labs recommends using the above TH version for qualification. Also included with this release is a set of OpenThread stack libraries that may be used for Thread certification by inheritance.

### Help and Feedback

- Contact [Silicon Labs Support](https://www.silabs.com/support).
- To use our **Ask AI** tool to get answers, see the search field at the top of [this page](https://docs.silabs.com/).  
  > **Note:** **Ask AI** is experimental.
- Get help from our [developer community](https://community.silabs.com/s/?language=en_US).

## Feature Matrix

[Supported Features](#supported-features) | [Unsupported Features](#unsupported-features)

### Supported Features

<table>
    <thead>
        <tr>
            <th>Feature Name</th>
            <th>Description</th>
            <th>Quality</th>
            <th>Related API Names</th>
            <th>Supported Software Variants, Hardware, Modes, Host Interfaces</th>
            <th>Related Example Names</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Thread 1.4</td>
            <td>All features as defined by the Thread Specification up to and including version 1.4.</td>
            <td>Production</td>
            <td><a href="https://docs.silabs.com/openthread/3.0.0/openthread-api/">OpenThread API</a></td>
            <td>None</td>
            <td>None</td>
        </tr>
    </tbody>
</table>

### Unsupported Features

This release includes support for running the OpenThread Border Router in a HOST / NCP architecture. However, at the time of the release, the following features were not complete when using this architecture: NAT64, Service Discovery.

## SDK Release and Maintenance Policy

See our [SDK Release and Maintenance Policy](https://www.silabs.com/developer-tools/sdk-release-and-maintenance-policy).