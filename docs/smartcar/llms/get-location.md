# Source: https://smartcar.com/docs/api-reference/get-location.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Location

> Returns the vehicle's last known location.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_location`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-location.mdx" />
</RequestExample>

## Response

<ResponseField name="latitude" type="number">
  The latitude in degrees.
</ResponseField>

<ResponseField name="longitude" type="number">
  The longitude in degrees.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
    "latitude": 37.4292,
    "longitude": 122.1381
  }
  ```
</ResponseExample>
