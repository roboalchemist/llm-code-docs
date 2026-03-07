# Source: https://docs.silabs.com/openthread/3.0.0/configuring-antenna-diversity-for-openthread/03-configuring-antenna-diversity-command-line-interface.md

# Configuring Antenna Diversity Command Line Interface

OpenThread SDK releases beginning with 1.1.0.0 provide a means to query and set Rx and Tx diversity modes using the Antenna Diversity CLI. Support for the Antenna Diversity CLI is:

- Enabled by default.
- Available as a configuration option on the **OpenThread Antenna Diversity** component.
- Requires the OpenThread CLI and Antenna Diversity components installed in your project.  
  > **Note**: For Silicon Labs OpenThread SDK releases prior to 1.2.0.0, the Antenna Diversity CLI is available as a configuration option on the OpenThread CLI component.

The complete list of supported Antenna Diversity CLI commands is summarized in the following table.

<table>
    <tbody>
        <tr>
            <th>Command</th>
            <th>Command Description</th>
            <th>API Function</th>
            <th colspan="3">Arguments</th>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>antenna get-tx-mode</td>
            <td>Returns the current setting for the Antenna Tx Diversity mode.</td>
            <td>sl_rail_util_ant_div_get_tx_antenna_mo de</td>
            <td>N/A</td>
            <td>N/A</td>
            <td rowspan="4">Interpretation of returned results for get operations and permissible values for set
                operations are as follows: SL_RAIL_UTIL_ANTENNA_MODE_DISABLED: 0 (Don't alter antenna selection)
                SL_RAIL_UTIL_ANTENNA_MODE_ENABLE1: 1 (Use antenna 1) SL_RAIL_UTIL_ANTENNA_MODE_ENABLE2: 2 (Use antenna
                2) SL_RAIL_UTIL_ANTENNA_MODE_DIVERSITY: 3 (Choose antenna 1 or 2 dynamically)</td>
        </tr>
        <tr>
            <td>antenna set-tx-mode</td>
            <td>Sets Tx Diversity mode to argument.</td>
            <td>sl_rail_util_ant_div_set_tx_antenna_mo de</td>
            <td>Tx Antenna Mode</td>
            <td>uint8_t</td>
        </tr>
        <tr>
            <td>antenna get-rx-mode</td>
            <td>Returns the current setting for Antenna Rx Diversity mode.</td>
            <td>sl_rail_util_ant_div_get_rx_antenna_mode</td>
            <td>N/A</td>
            <td>N/A</td>
        </tr>
        <tr>
            <td>antenna set-rx-mode</td>
            <td>Sets Rx Diversity mode to argument.</td>
            <td>sl_rail_util_ant_div_set_rx_antenna_mode</td>
            <td>Rx Antenna Mode</td>
            <td>uint8_t</td>
        </tr>
        <tr>
            <td>antenna get-active-phy</td>
            <td>Returns the current PHY being used.</td>
            <td>sl_rail_util_get_active_radio_config</td>
            <td>N/A</td>
            <td>N/A</td>
            <td>-</td>
        </tr>
    </tbody>
</table>

Tx diversity settings can be changed using the CLI without any restriction. However, Rx Diversity options that require switching from standard PHY to diversity PHY or vice-versa are only permitted when the **Runtime PHY Select** configuration option on the RAIL Utility Antenna Diversity Configuration component is enabled, as shown in the following figure:

![Chip-external Antenna Diversity Configuration](/configuring-antenna-diversity-for-openthread/0.2/images/sld701-image10.png)

## Disable Antenna Diversity CLI Support

1. Open the configuration options of the OpenThread **Antenna Diversity** component.
2. Disable the option.  
   ![Disable Antenna Diversity CLI Support](/configuring-antenna-diversity-for-openthread/0.2/images/sld701-image12.png)

> **Note**: For Silicon Labs OpenThread SDK releases prior to 1.2.0.0, disable the Antenna Diversity CLI configuration option on the OpenThread CLI component.
