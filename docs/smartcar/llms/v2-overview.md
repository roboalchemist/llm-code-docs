# Source: https://smartcar.com/docs/api-reference/v2-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vehicles API v2.0 Overview

> Overview of the Smartcar Vehicles API v2.0 and deprecation notice.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

The Smartcar Vehicles API v2.0 is the previous version of our core API for accessing standardized vehicle data and current version for sending remote commands. It allows developers to:

* Retrieve real-time vehicle signals (e.g., battery level, odometer, fuel, tire pressure)
* Send remote commands (lock/unlock, start/stop charging, etc.)

All requests to v2.0 require an OAuth2 access token, which is obtained by having the vehicle owner authorize your app via [Smartcar Connect](/connect/what-is-connect).

## Base URL

```
https://api.smartcar.com/v2.0
```

For this API, the latency response times may vary per vehicle make and model. For more information, see [OEM Latency](/help/oem-latency).
