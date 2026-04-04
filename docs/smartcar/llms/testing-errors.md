# Source: https://smartcar.com/docs/errors/testing-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing Errors

> By launching Connect in [simulated mode](/docs/connect/advanced-config/modes), you're able to test your application against certain errors.

## Testing Connect Errors

You can use the following emails to test a subset of Connect errors:

| Error                  | Email                                                                         | VIN               |
| ---------------------- | ----------------------------------------------------------------------------- | ----------------- |
| `invalid_subscription` | [smartcar@invalid-subscription.com](mailto:smartcar@invalid-subscription.com) | 0SCAUDI0155C49A95 |
| `vehicle_incompatible` | [smartcar@vehicle-incompatible.com](mailto:smartcar@vehicle-incompatible.com) | 0SCAUDI012FE3B132 |

Visit the [Connect Errors](/api-reference/api-errors#connect-errors) page for more details.

## Testing API Errors

You can use use the following emails to test these API error types:

* `COMPATIBILITY`
* `CONNECTED_SERVICES_ACCOUNT`
* `UPSTREAM`
* `VEHICLE_STATE`

| Type                         | Code                          | Email                                                                                                                                    | VIN               |
| ---------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `COMPATIBILITY`              | `MAKE_NOT_COMPATIBLE`         | [COMPATIBILITY.MAKE\_NOT\_COMPATIBLE@smartcar.com](mailto:COMPATIBILITY.MAKE_NOT_COMPATIBLE@smartcar.com)                                | 0SCLR000270BE6600 |
| `COMPATIBILITY`              | `SMARTCAR_NOT_CAPABLE`        | [COMPATIBILITY.SMARTCAR\_NOT\_CAPABLE@smartcar.com](mailto:COMPATIBILITY.SMARTCAR_NOT_CAPABLE@smartcar.com)                              | 0SCLR0002DC18F57F |
| `COMPATIBILITY`              | `VEHICLE_NOT_CAPABLE`         | [COMPATIBILITY.VEHICLE\_NOT\_CAPABLE@smartcar.com](mailto:COMPATIBILITY.VEHICLE_NOT_CAPABLE@smartcar.com)                                | 0SCLR00024C7CDF7A |
| `CONNECTED_SERVICES_ACCOUNT` | `ACCOUNT_ISSUE`               | [CONNECTED\_SERVICES\_ACCOUNT.ACCOUNT\_ISSUE@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.ACCOUNT_ISSUE@smartcar.com)                 | 0SCLR00026BAAA136 |
| `CONNECTED_SERVICES_ACCOUNT` | `AUTHENTICATION_FAILED`       | [CONNECTED\_SERVICES\_ACCOUNT.AUTHENTICATION\_FAILED@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.AUTHENTICATION_FAILED@smartcar.com) | 0SCLR00021D803C7B |
| `CONNECTED_SERVICES_ACCOUNT` | `NO_VEHICLES`                 | [CONNECTED\_SERVICES\_ACCOUNT.NO\_VEHICLES@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.NO_VEHICLES@smartcar.com)                     | 0SCLR00027671837B |
| `CONNECTED_SERVICES_ACCOUNT` | `SUBSCRIPTION`                | [CONNECTED\_SERVICES\_ACCOUNT.SUBSCRIPTION@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.SUBSCRIPTION@smartcar.com)                    | 0SCLR0002B9BAF29F |
| `CONNECTED_SERVICES_ACCOUNT` | `VEHICLE_MISSING`             | [CONNECTED\_SERVICES\_ACCOUNT.VEHICLE\_MISSING@smartcar.com](mailto:CONNECTED_SERVICES_ACCOUNT.VEHICLE_MISSING@smartcar.com)             | 0SCLR00024E29EEBD |
| `UPSTREAM`                   | `INVALID_DATA`                | [UPSTREAM.INVALID\_DATA@smartcar.com](mailto:UPSTREAM.INVALID_DATA@smartcar.com)                                                         | 0SCLR000298A0A649 |
| `UPSTREAM`                   | `KNOWN_ISSUE`                 | [UPSTREAM.KNOWN\_ISSUE@smartcar.com](mailto:UPSTREAM.KNOWN_ISSUE@smartcar.com)                                                           | 0SCLR0002A8760B72 |
| `UPSTREAM`                   | `NO_RESPONSE`                 | [UPSTREAM.NO\_RESPONSE@smartcar.com](mailto:UPSTREAM.NO_RESPONSE@smartcar.com)                                                           | 0SCLR0002C23E43AB |
| `UPSTREAM`                   | `UNKNOWN_ISSUE`               | [UPSTREAM.UNKNOWN\_ISSUE@smartcar.com](mailto:UPSTREAM.UNKNOWN_ISSUE@smartcar.com)                                                       | 0SCLR0002D4878901 |
| `VEHICLE_STATE`              | `ASLEEP`                      | [VEHICLE\_STATE.ASLEEP@smartcar.com](mailto:VEHICLE_STATE.ASLEEP@smartcar.com)                                                           | 0SCLR0002E8896323 |
| `VEHICLE_STATE`              | `CHARGING_IN_PROGRESS`        | [VEHICLE\_STATE.CHARGING\_IN\_PROGRESS@smartcar.com](mailto:VEHICLE_STATE.CHARGING_IN_PROGRESS@smartcar.com)                             | 0SCLR000221F1E672 |
| `VEHICLE_STATE`              | `CHARGING_PLUG_NOT_CONNECTED` | [VEHICLE\_STATE.CHARGING\_PLUG\_NOT\_CONNECTED@smartcar.com](mailto:VEHICLE_STATE.CHARGING_PLUG_NOT_CONNECTED@smartcar.com)              | 0SCLR0002CBFC7C21 |
| `VEHICLE_STATE`              | `DOOR_OPEN`                   | [VEHICLE\_STATE.DOOR\_OPEN@smartcar.com](mailto:VEHICLE_STATE.DOOR_OPEN@smartcar.com)                                                    | 0SCLR0002F8BD90B8 |
| `VEHICLE_STATE`              | `FULLY_CHARGED`               | [VEHICLE\_STATE.FULLY\_CHARGED@smartcar.com](mailto:VEHICLE_STATE.FULLY_CHARGED@smartcar.com)                                            | 0SCLR00029CD9D894 |
| `VEHICLE_STATE`              | `HOOD_OPEN`                   | [VEHICLE\_STATE.HOOD\_OPEN@smartcar.com](mailto:VEHICLE_STATE.HOOD_OPEN@smartcar.com)                                                    | 0SCLR000219CD4A2C |
| `VEHICLE_STATE`              | `IGNITION_ON`                 | [VEHICLE\_STATE.IGNITION\_ON@smartcar.com](mailto:VEHICLE_STATE.IGNITION_ON@smartcar.com)                                                | 0SCLR00021D49E58A |
| `VEHICLE_STATE`              | `IN_MOTION`                   | [VEHICLE\_STATE.IN\_MOTION@smartcar.com](mailto:VEHICLE_STATE.IN_MOTION@smartcar.com)                                                    | 0SCLR00024F6EE640 |
| `VEHICLE_STATE`              | `REMOTE_ACCESS_DISABLED`      | [VEHICLE\_STATE.REMOTE\_ACCESS\_DISABLED@smartcar.com](mailto:VEHICLE_STATE.REMOTE_ACCESS_DISABLED@smartcar.com)                         | 0SCLR0002588A5CC1 |
| `VEHICLE_STATE`              | `TRUNK_OPEN`                  | [VEHICLE\_STATE.TRUNK\_OPEN@smartcar.com](mailto:VEHICLE_STATE.TRUNK_OPEN@smartcar.com)                                                  | 0SCLR00023C607FDB |
| `VEHICLE_STATE`              | `UNKNOWN`                     | [VEHICLE\_STATE.UNKNOWN@smartcar.com](mailto:VEHICLE_STATE.UNKNOWN@smartcar.com)                                                         | 0SCLR0002E6CC0314 |
| `VEHICLE_STATE`              | `UNREACHABLE`                 | [VEHICLE\_STATE.UNREACHABLE@smartcar.com](mailto:VEHICLE_STATE.UNREACHABLE@smartcar.com)                                                 | 0SCLR000247EBF067 |
| `VEHICLE_STATE`              | `VEHICLE_OFFLINE_FOR_SERVICE` | [VEHICLE\_STATE.VEHICLE\_OFFLINE\_FOR\_SERVICE@smartcar.com](mailto:VEHICLE_STATE.VEHICLE_OFFLINE_FOR_SERVICE@smartcar.com)              | 0SCLR0002AF1D71A1 |
