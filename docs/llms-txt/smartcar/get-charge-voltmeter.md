# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-voltmeter.md

# Source: https://smartcar.com/docs/api-reference/gm/get-charge-voltmeter.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-voltmeter.md

# Source: https://smartcar.com/docs/api-reference/gm/get-charge-voltmeter.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-voltmeter.md

# Source: https://smartcar.com/docs/api-reference/gm/get-charge-voltmeter.md

# Source: https://smartcar.com/docs/api-reference/tesla/get-charge-voltmeter.md

# Source: https://smartcar.com/docs/api-reference/gm/get-charge-voltmeter.md

# Voltage

> When the vehicle is plugged in, returns the charging voltage measured by the vehicle. When the vehicle is not plugged in, this endpoint results in a vehicle state error.

<Note>
  This endpoint is currently available for `cadillac` and `chevrolet`.
</Note>

## Permission

`read_charge`

## Request

<Snippet file="api-reference/path-bse.mdx" />

<RequestExample>
  <Snippet file="api-reference/bse/get-charge-voltmeter.mdx" />
</RequestExample>

## Response

<ResponseField name="voltage" type="number">
  The potential difference measured by the vehicle in volts (V).
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "voltage": 240
  }
  ```
</ResponseExample>
