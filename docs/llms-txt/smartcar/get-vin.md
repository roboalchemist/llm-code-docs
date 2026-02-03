# Source: https://smartcar.com/docs/api-reference/get-vin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# VIN

> Returns the vehicle’s manufacturer identifier.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_vin`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-vin.mdx" />
</RequestExample>

## Response

<ResponseField name="vin" type="string">
  The manufacturer unique identifier.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "vin": "5YJSA1CN5DFP00101"
  }
  ```
</ResponseExample>
