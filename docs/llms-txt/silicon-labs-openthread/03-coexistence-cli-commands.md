# Source: https://docs.silabs.com/openthread/3.0.0/zigbee-openthread-coexistence-wifi/03-coexistence-cli-commands.md

# Coexistence CLI Commands

The Coexistence CLI commands can support run-time console control of PTA enable/disable, PTA run-time configuration (ptaOptions), and PTA debug counters. These custom CLI commands are not only useful in manual testing of various coexistence configurations, but also support run-time reconfiguration.

## Coexistence CLI Commands (using AppBuilder for Zigbee)

For Zigbee, the Coexistence CLI commands are currently supported in both Host and SoC applications.

The following figure shows a partial listing of the coexistence plugin commands. For more details about the CLI commands and parameters, refer to `coexistence-cli.c`.

![Coexistence CLI Console Commands (partial listing)](/zigbee-openthread-coexistence-wifi/0.1/images/sld515-image30.png)

## Coexistence CLI Commands (using Component Editor for Zigbee and OpenThread)

For Zigbee, support for Coexistence CLI is enabled by installing the **Zigbee Utility, Coexistence CLI** component under **Platform > Radio components**.

![image](/zigbee-openthread-coexistence-wifi/0.1/images/sld515-image31.png)

For OpenThread, support for Coexistence CLI is:

- Enabled by default for all applications.
- Available as a configuration option on the **OpenThread Coexistence** component.
- Requires that you have already installed the **OpenThread CLI** and the **Coexistence** components in your project.

For Silicon Labs OpenThread SDK releases prior to 1.2.0.0, the Coexistence CLI commands are:

- Supported in SoC applications only and,
- Available as a configuration option on the OpenThread CLI component.

The complete list of support commands is summarized in the following table. For more details about the CLI commands and parameters, refer to `sl_zigbee_coexistence_cli.c` for Zigbee and `coexistence_cli.c` for OpenThread.

|Command|Command Description|API Function|
|---|---|---|
|coexistence get-dp-state|Returns the Directional PRIORITY state along with pulse width (µs).|sl_rail_util_coex_get_directional_priority_pulse_width|
|coexistence set-dp-state|Set Directional PRIORITY state.|sl_rail_util_coex_set_directional_priority_pulse_width|
|coexistence get-gpio-input|Returns GPIO Input override from console.|sl_rail_util_coex_get_gpio_input_override|
|coexistence set-gpio-input|Sets GPIO Input override from console.|sl_rail_util_coex_set_gpio_input_override|
|coexistence get-phy-state|Returns PHY select state.|sl_rail_util_coex_get_phy_select_timeout|
|coexistence set-phy-state|Sets PHY select timeout.|sl_rail_util_coex_set_phy_select_timeout|
|coexistence get-pta-options|Returns ptaOptions.|sl_rail_util_coex_get_options|
|coexistence set-pta-options|Sets ptaOptions.|sl_rail_util_coex_set_options|
|coexistence get-pta-state|Returns PTA state.|sl_rail_util_coex_is_enabled|
|coexistence set-pta-state|Sets PTA state.|sl_rail_util_coex_set_enable|
|coexistence get-pwm-state|Returns PWM state from console with period and duty cycle.|sl_rail_util_coex_get_request_pwm_args|
|coexistence set-pwm-state|Sets PWM State.|sl_rail_util_coex_get_request_pwm_args|
|coexistence reset-counters|Clears coex counters.|efr32RadioClearCoexCounters|
|coexistence get-counters|Returns the PTA-specific debug counter values.|efr32RadioGetCoexCounters|

> **Note**: For Zigbee, the coexistence CLI command to get the PTA specific debug counters is _coexistence result-counters._

To disable Coexistence CLI support:

1. Open the configuration options of the OpenThread Coexistence component.  
   ![image](/zigbee-openthread-coexistence-wifi/0.1/images/sld515-image32.png)
2. Disable the option.  
   ![image](/zigbee-openthread-coexistence-wifi/0.1/images/sld515-image33.png)

> **Note**: For Silicon Labs OpenThread SDK releases prior to 1.2.0.0, disable the Coexistence CLI configuration option on the OpenThread CLI component.

## PTA-specific Debug Counters

For Zigbee, MAC and APS stack counters are documented in the stack API documentation and can also be accessed via CLI. The following table describes the six coexistence PTA-specific debug counters.

|Counter Index|Meaning|
|---|---|
|EMBER_COUNTER_PTA_LO_PRI_REQUESTED|Occurrences of REQUEST asserted with low priority.|
|EMBER_COUNTER_PTA_HI_PRI_REQUESTED|Occurrences of REQUEST asserted with high priority.|
|EMBER_COUNTER_PTA_LO_PRI_DENIED|Occurrences of GRANT denied with low priority REQUEST.|
|EMBER_COUNTER_PTA_HI_PRI_DENIED|Occurrences of GRANT denied with high priority REQUEST.|
|EMBER_COUNTER_PTA_LO_PRI_TX_ABORTED|Occurrences of TX aborted by GRANT de-asserted with low priority REQUEST.|
|EMBER_COUNTER_PTA_HI_PRI_TX_ABORTED|Occurrences of TX aborted by GRANT de-asserted with high priority REQUEST.|

For OpenThread, support for coexistence PTA-specific debug counters are:

- Enabled by default.
- Available as a configuration option on the **OpenThread Coexistence** component.
- Requires that you have already installed the **OpenThread Coexistence** component in your project.

The following table describes the six coexistence PTA-specific debug counters for OpenThread.

|Counter Index|Meaning|
|---|---|
|SL_RAIL_UTIL_COEX_EVENT_LO_PRI_REQUESTED|Occurrences of REQUEST asserted with low priority.|
|SL_RAIL_UTIL_COEX_EVENT_HI_PRI_REQUESTED|Occurrences of REQUEST asserted with high priority.|
|SL_RAIL_UTIL_COEX_EVENT_LO_PRI_DENIED|Occurrences of GRANT denied with low priority REQUEST.|
|SL_RAIL_UTIL_COEX_EVENT_HI_PRI_DENIED|Occurrences of GRANT denied with high priority REQUEST.|
|SL_RAIL_UTIL_COEX_EVENT_LO_PRI_TX_ABORTED|Occurrences of TX aborted by GRANT de-asserted with low priority REQUEST.|
|SL_RAIL_UTIL_COEX_EVENT_HI_PRI_TX_ABORTED|Occurrences of TX aborted by GRANT de-asserted with high priority REQUEST.|

### OpenThread Specific Debug Counters

OpenThread offers several coexistence debug counters to help with development. These are enabled by default when **OpenThread Coexistence** component is pulled into an application.

The following table describes OpenThread specific debug counters.

|Counter Index|Meaning|
|---|---|
|mNumTxRequest|Number of Tx Requested = mNumTxGrantImmediate + mNumTxGrantWait.|
|mNumTxGrantImmediate|Number of tx requests while grant was active.|
|mNumTxGrantWait|Number of tx requests while grant was inactive.|
|mNumTxGrantWaitActivated|Number of tx requests while grant was inactive that were ultimately granted.|
|mNumTxGrantWaitTimeout|Number of tx requests while grant was inactive that timed out.|
|mNumTxGrantDeactivatedDuringRequest|Number of tx that were in progress when grant was deactivated.|
|mNumTxDelayedGrant|Number of tx requests that were not granted within 50us.|
|mAvgTxRequestToGrantTime|Average time in usec from tx request to grant.|
|mNumRxRequest|Number of rx requests.|
|mNumRxGrantImmediate|Number of rx requests while grant was active.|
|mNumRxGrantWait|Number of rx requests while grant was inactive.|
|mNumRxGrantWaitActivated|Number of rx requests while grant was inactive that were ultimately granted.|
|mNumRxGrantWaitTimeout|Number of rx requests while grant was inactive that timed out.|
|mNumRxGrantDeactivatedDuringRequest|Number of rx that were in progress when grant was deactivated.|
|mNumRxDelayedGrant|Number of rx requests that were not granted within 50us.|
|mAvgRxRequestToGrantTime|Average time in usec from rx request to grant.|
