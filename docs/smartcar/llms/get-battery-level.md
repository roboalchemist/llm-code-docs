# Source: https://smartcar.com/docs/api-reference/evs/get-battery-level.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Battery Level

> Returns the state of charge and the remaining range of an electric vehicle's high voltage battery.

## Permission

`read_battery`

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

<Note>
  This endpoint is only available for BEVs and PHEVs.
</Note>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-battery-level.mdx" />
</RequestExample>

## Response

<ResponseField name="percentRemaining" type="number">
  The EV's state of charge as a percentage.
</ResponseField>

<ResponseField name="range" type="number" default="kilometers">
  The estimated remaining distance the vehicle can travel powered by its high voltage battery.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "percentRemaining": 0.3,
      "range": 40.5
  }
  ```
</ResponseExample>
