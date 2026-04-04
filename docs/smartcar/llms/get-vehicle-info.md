# Source: https://smartcar.com/docs/api-reference/get-vehicle-info.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vehicle Attributes

> Returns a single vehicle object, containing identifying information.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

## Permission

`read_vehicle_info`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/get-vehicle-info.mdx" />
</RequestExample>

## Response

<ResponseField name="id" type="string">
  The ID for the vehicle.
</ResponseField>

<ResponseField name="make" type="string">
  The manufacturer of the vehicle.
</ResponseField>

<ResponseField name="model" type="string">
  The model of the vehicle.
</ResponseField>

<ResponseField name="year" type="integer">
  The model year.
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "id": "36ab27d0-fd9d-4455-823a-ce30af709ffc",
      "make": "TESLA",
      "model": "Model S",
      "year": "2014"
  }
  ```
</ResponseExample>
