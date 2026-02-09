# Source: https://smartcar.com/docs/api-reference/evs/get-charge-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Charge Status

> Returns the charge status for the vehicle.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_charge`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-charge-status.mdx" />
</RequestExample>

## Response

<ResponseField name="isPluggedIn" type="bool">
  Indicates whether a charging cable is currently plugged into the vehicle’s charge port.
</ResponseField>

<ResponseField name="state" type="string">
  Returns the current charge status of a vehicle. A vehicle can be `FULLY_CHARGED` at less than 100% SoC if its [Charge Limit](/api-reference/evs/get-charge-limit) is less than `1`.

  <Expandable title="states">
    <ResponseField name="CHARGING" />

    <ResponseField name="FULLY_CHARGED" />

    <ResponseField name="NOT_CHARGING" />
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "isPluggedIn": true,
      "state": "FULLY_CHARGED"
  }
  ```
</ResponseExample>
