# Source: https://docs.silabs.com/openthread/3.0.0/sisdk-ot-release-notes/sisdk-ot-multiprotocol-release-notes.md

# OpenThread - 802.15.4 Mesh + BLE Multiprotocol Version 3.0.0 - Release Notes (Jan 22, 2026)

[**OpenThread Version 3.0.0**](.)

This document provides release information for the 802.15.4 Mesh + BLE Multiprotocol SDK.

Click [here](https://github.com/SiliconLabs/simplicity_sdk/tags) for earlier releases.

## Release Summary

[Key Features](#key-features) | [API Changes](#api-changes) | [Bug Fixes](#bug-fixes) | [Chip Enablement](#chip-enablement)

### Key Features

- Concurrent Listening support with CMP on SiMG301x.
- Bi-directional Green Power support with CMP Zigbee NCP + OpenThread RCP.

### API Changes

None.

### Bug Fixes

Targeted quality improvements and bug fixes.

### Chip Enablement

- xGM270S Leopard SiP Module GA SW support.
- xG301 Explorer Kit and Pro-kit support.

## Key Features

[New Features](#new-features) | [Enhancements](#enhancements) | [Removed Features](#removed-features) | [Deprecated Features](#deprecated-features)

### New Features

#### Bi-directional Green Power support with CMP Zigbee NCP + OpenThread RCP

Added bi-directional Green Power support with CMP Zigbee NCP + OT RCP configuration, enabling Green Power Proxy functionality in NCP-RCP multiprotocol applications.

### Enhancements

None.

### Removed Features

None.

### Deprecated Features

None.

## API Changes

[New APIs](#new-ap-is) | [Modified APIs](#modified-ap-is) | [Removed APIs](#removed-ap-is) | [Deprecated APIs](#deprecated-ap-is)

### New APIs

None.

### Modified APIs

None.

### Removed APIs

None.

### Deprecated APIs

|Deprecated API Name|Planned Removal Date|
|---|---|
|[sl_802154_radio_set_scheduler_priorities](https://docs.silabs.com/zigbee/latest/zigbee-stack-api/stack-info-h#sl-802154-radio-set-scheduler-priorities)|2026 Q1|

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
            <td>1471746</td>
            <td>Fixed an issue where the Zigbee + Bluetooth NCP application examples did not appear in Studio.</td>
            <td>N/A</td>
            <td>Zigbee + Bluetooth NCP app</td>
        </tr>
        <tr>
            <td>1524505</td>
            <td>Fixed an issue that could pass an invalid mac layer packet to cause an assert.</td>
            <td>N/A</td>
            <td>All OPNs, boards, modes and interfaces</td>
        </tr>
        <tr>
            <td>1568095</td>
            <td>Changed default SL_BT_CONTROLLER_BUFFER_MEMORY value for OpenThread NCP + BLE RCP application to work on parts with 96kB RAM.</td>
            <td>N/A</td>
            <td>OpenThread NCP + BLE RCP app</td>
        </tr>
    </tbody>
</table>

## Chip Enablement

- **xGM270S Leopard SiP Module**: Added GA software support for xGM270S Leopard SiP Module.
- **xG301 Explorer Kit and Pro-kit Support**: Added support for Explorer Kit and Pro-kit boards for xG301 devices.

## Application Example Changes

[New Examples](#new-examples) | [Modified Examples](#modified-examples) | [Removed Examples](#removed-examples) | [Deprecated Examples](#deprecated-examples)

### New Examples

<table>
    <thead>
        <tr>
            <th>Example Name</th>
            <th>Description</th>
            <th>Supported Software Variants if applicable </th>
            <th>Supported Modes</th>
            <th>Supported OPNs / Boards / OPN Combinations</th>
            <th>Supported Host Interfaces</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>ot-ncp-ble-rcp</p>
                <p>See <a href="https://github.com/SiliconLabsSoftware/sisdk-release/blob/sisdk-2025.12/multiprotocol_app/protocol/openthread/sample-apps/ot-ncp/dmp/README-OT-NCP-BLE-RCP.md">README</a></p>
            </td>
            <td>
                New sample application that integrates DMP BLE-RCP components with OpenThread NCP FTD CPC application, enabling OpenThread NCP with BLE RCP support.
            </td>
            <td>
                N/A
            </td>
            <td>
                NCP
            </td>
            <td>
                All supported OPNs, boards, modes and interfaces
            </td>
            <td>
                CPC
            </td>
        </tr>
        <tr>
            <td>
                <p>zigbee_ncp_ot_rcp_uart_gp_multi_rail</p>
                <p>See <a href="https://github.com/SiliconLabsSoftware/sisdk-release/blob/sisdk-2025.12/multiprotocol_app/protocol/zigbee/app/projects/ncp/zigbee_ncp_ot_rcp_uart_gp_multi_rail/readme.md">README</a></p>
            </td>
            <td>
                New sample application providing bi-directional Green Power support with CMP Zigbee NCP + OT RCP configuration using multi-rail UART interface.
            </td>
            <td>
                N/A
            </td>
            <td>
                NCP/RCP
            </td>
            <td>
                All supported OPNs, boards, modes and interfaces
            </td>
            <td>
                UART
            </td>
        </tr>
    </tbody>
</table>

### Modified Examples

<table>
    <thead>
        <tr>
            <th>Example Name</th>
            <th>Changes</th>
            <th>Supported Software Variants if applicable </th>
            <th>Supported Modes</th>
            <th>Supported OPNs / Boards / OPN Combinations</th>
            <th>Supported Host Interfaces</th>
        </tr>
    </thead>
    <tbody>
    </tbody>
    <tbody>
        <tr>
            <td>
                <p>Zigbee - BLE Dynamic Multiprotocol Light SED</p>
                <p>See <a href="https://github.com/SiliconLabsSoftware/sisdk-release/tree/sisdk-2025.12/multiprotocol_app/protocol/zigbee/app/projects/multiprotocol/zigbee_ble_dynamic_multiprotocol_light_sed">sample here</a> </p>
            </td>
            <td>
                The Zigbee BLE - DynamicMultiprotocolLightSed sample project can now be built for boards with only one LED if the LED1 component is excluded from the project.
            </td>
            <td>
                N/A
            </td>
            <td>
                N/A
            </td>
            <td>
                N/A
            </td>
            <td>
                N/A
            </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td>
                <p>Zigbeed</p>
                <p>See <a href="https://github.com/SiliconLabsSoftware/sisdk-release/tree/sisdk-2025.12/zigbee_app/zigbeed">sample here</a></p>
            </td>
            <td>
                The Zigbeed sample application is now extended with the --conf parameter, so the location of the zigbeed.conf is now configurable and not being hardcoded to /usr/local/etc/zigbeed.conf
            </td>
            <td>
                N/A
            </td>
            <td>
                N/A
            </td>
            <td>
                N/A
            </td>
            <td>
                N/A
            </td>
        </tr>
    </tbody>
</table>

### Removed Examples

None.

### Deprecated Examples

None.

## Known Issues and Limitations

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
            <td>1209958</td>
            <td>The Zigbee + OpenThread + BLE RCP may stop working in endurance testing (~2 hours) on MG24 and MG21 devices with constant and concurrent traffic on all three stacks.</td>
            <td>N/A</td>
            <td>None</td>
            <td>Zigbee + OpenThread + BLE RCP app</td>
        </tr>
        <tr>
            <td>1385052</td>
            <td>Coex-enabled RCP may still occasionally transmit TX ACK after losing the Grant even when Acking is disabled and TX Abort is enabled.</td>
            <td>N/A</td>
            <td>This will be fixed in future releases.</td>
            <td>Coex-enabled RCP</td>
        </tr>
        <tr>
            <td>1385486</td>
            <td>TX from coex-enabled RCP may infrequently happen without the request after turning on the non-802.15.4 compliant MAC Holdoff coex option.</td>
            <td>N/A</td>
            <td>This will be fixed in future releases.</td>
            <td>Coex-enabled RCP</td>
        </tr>
        <tr>
            <td>1457086</td>
            <td>Coex-enabled EFR32MG24 RCP may sometimes output higher than expected grant denied counts in the PTA counters.</td>
            <td>N/A</td>
            <td>This will be fixed in future releases.</td>
            <td>Coex-enabled RCP</td>
        </tr>
        <tr>
            <td>1458795</td>
            <td>Using BLE GAP scanning stop command in the Zigbee DMP GP - Proxy app may not be able to stop BLE scanning on certain parts.</td>
            <td>N/A</td>
            <td>None</td>
            <td>Zigbee DMP GP - Proxy app</td>
        </tr>
        <tr>
            <td>1514786</td>
            <td>Wi-Fi coexistence on SixG301 is currently not supported.<br>Other references: 1514794, 1515385.</td>
            <td>N/A</td>
            <td>This will be supported in future releases.</td>
            <td>SixG301 devices</td>
        </tr>
        <tr>
            <td>1569847</td>
            <td>Using the CMP Zigbee NCP + OpenThread RCP application with Bi-directional Green Power support, bi-directional commissioning may intermittently fail.</td>
            <td>N/A</td>
            <td>None</td>
            <td>EFR32xG24 devices</td>
        </tr>
    </tbody>
</table>