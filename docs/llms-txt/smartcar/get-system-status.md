# Source: https://smartcar.com/docs/api-reference/get-system-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# System Status

> Provides a list of vehicle systems and their current health status. Currently supporting FCA and GM brands including RAM, Jeep, Chrysler, Dodge, Fiat, Alfa Romeo, Buick, Cadillac, Chevrolet and GMC. See [Diagnostic Systems](/docs/help/diagnostic-systems) for a complete list of Smartcar System IDs.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_diagnostics`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/diagnostics/system_status" \\
      -H "Authorization: Bearer {token}" \\
      -X "GET"
  ```

  ```python Python theme={null}
  diagnostic_system_status = vehicle.diagnostic_system_status()
  ```

  ```js Node theme={null}
  const diagnosticSystemStatus = await vehicle.diagnosticSystemStatus();
  ```

  ```java Java theme={null}
  VehicleDiagnosticSystemStatus diagnosticSystemStatus = vehicle.diagnosticSystemStatus();
  ```

  ```ruby Ruby theme={null}
  diagnostic_system_status = vehicle.diagnostic_system_status
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

## Response

<ResponseField name="systems" type="array">
  An overview of systems reported by the vehicle.
</ResponseField>

<ResponseField name="systemID" type="string">
  The unique identifier of a system reported by the vehicle.
</ResponseField>

<ResponseField name="status" type="string">
  The status of a vehicle, expected as "OK" or "ALERT".
</ResponseField>

<ResponseField name="description" type="string | null">
  A plain-text description of the status, if available.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
        "systems": [
            {
                // System ID from Smartcar unified system definition list
                "systemId": "SYSTEM_TPMS",
                "status": "ALERT",
                "description": "Left rear tire sensor battery low"
            },
            {
                "systemId": "SYSTEM_AIRBAG",
                "status": "OK",
                "description": null
            },
            {
                "systemId": "SYSTEM_MIL",
                "status": "OK",
                "description": null
            },
            ...
        ]
  }
  ```
</ResponseExample>
