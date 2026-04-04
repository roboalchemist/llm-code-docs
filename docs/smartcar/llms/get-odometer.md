# Source: https://smartcar.com/docs/api-reference/get-odometer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Odometer

> Returns the vehicle’s last known odometer reading.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_odometer`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-odometer.mdx" />
</RequestExample>

## Response

<ResponseField name="distance" type="number" default="kilometers">
  The current odometer of the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "distance": 104.32
  }
  ```
</ResponseExample>
