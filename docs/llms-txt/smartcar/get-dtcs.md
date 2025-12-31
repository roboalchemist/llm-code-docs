# Source: https://smartcar.com/docs/api-reference/get-dtcs.md

# Diagnostic Trouble Codes

> Provides a list of active Diagnostic Trouble Codes (DTCs) reported by the vehicle. Currently supporting GM brands including Chevrolet and GMC.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_diagnostics`

<RequestExample>
  ```bash cURL theme={null}
  curl "https://api.smartcar.com/v2.0/vehicles/{id}/diagnostics/dtcs" \
      -H "Authorization: Bearer {token}" \
      -X "GET"
  ```

  ```python Python theme={null}
  diagnostic_trouble_codes = vehicle.diagnostic_trouble_codes()
  ```

  ```js Node theme={null}
  const diagnosticTroubleCodes = await vehicle.diagnosticTroubleCodes();
  ```

  ```java Java theme={null}
  VehicleDiagnosticTroubleCodes diagnosticTroubleCodes = vehicle.diagnosticTroubleCodes();
  ```

  ```ruby Ruby theme={null}
  diagnostic_trouble_codes = vehicle.diagnostic_trouble_codes
  ```
</RequestExample>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

## Response

<ResponseField name="activeCodes" type="array">
  Array of active diagnostic trouble codes.

  <Expandable>
    <ResponseField name="code" type="string">
      The Diagnostic Trouble Code reported by the vehicle.
    </ResponseField>

    <ResponseField name="timestamp" type="timestamp">
      The date and time the trouble code last became active.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
    {
      "activeCodes": [
        {
          "code": "P302D",
          "timestamp": "2024-09-05T14:48:00.000Z"
        },
        {
          "code": "xxxxx",
          "timestamp": null
        }
        
        ... 
      ]
    }
  ```
</ResponseExample>
