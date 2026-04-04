# Source: https://smartcar.com/docs/api-reference/get-tire-pressure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tire Pressure

> Returns the air pressure of each of the vehicle’s tires.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_tires`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-tire-pressure.mdx" />
</RequestExample>

## Response

<ResponseField name="frontLeft" type="number" default="kilopascals">
  The current air pressure of the front left tire.
</ResponseField>

<ResponseField name="frontRight" type="number" default="kilopascals">
  The current air pressure of the front right tire.
</ResponseField>

<ResponseField name="backLeft" type="number" default="kilopascals">
  The current air pressure of the back left tire.
</ResponseField>

<ResponseField name="backRight" type="number" default="kilopascals">
  The current air pressure of the back right tire.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "backLeft": 219.3,
      "backRight": 219.3,
      "frontLeft": 219.3,
      "frontRight": 219.3
  }
  ```
</ResponseExample>
