# Source: https://smartcar.com/docs/api-reference/get-engine-oil-life.md

# Oil Life

> Returns the remaining life span of a vehicle’s engine oil.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_engine_oil`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-engine-oil-life.mdx" />
</RequestExample>

## Response

<ResponseField name="lifeRemaining" type="number">
  The engine oil’s remaining life span based on the current quality of the oil as a percentage.
  `1` indicates the oil was changed recently and `0` indicates the oil should be changed immediately.
  It is not a representation of how much oil is left in the vehicle.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "lifeRemaining": 0.35
  }
  ```
</ResponseExample>
