# Source: https://smartcar.com/docs/api-reference/batch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch

> Returns a list of responses from multiple Smartcar `GET` endpoints, all combined into a single request.

<Warning>
  The Vehicles API v2.0 will be deprecated by **Q3 of 2026**. We recommend migrating to the [latest version](/api-reference/vehicles-api-intro) as soon as possible to ensure continued support and access to new features.
</Warning>

<Info>
  Each endpoint in the batch counts against your [request limit](/errors/api-errors/billing-errors) for a vehicle.
</Info>

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="requests" type="array" required>
  An array of requests to make.

  <Expandable>
    <ParamField body="path" type="string" required>
      The Smartcar endpoint to request data from.
    </ParamField>
  </Expandable>
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/batch.mdx" />
</RequestExample>

## Response

<ResponseField name="responses" type="array">
  The responses from Smartcar.

  <Expandable title="response" defaultOpen="true">
    <ResponseField name="headers" type="object">
      The headers for this response.

      <Expandable title="headers">
        <ResponseField name="sc-unit-system" type="string">
          The unit system to use for the request.
        </ResponseField>

        <ResponseField name="sc-data-age" type="string">
          The timestamp (ISO-8601 format) of when the returned data was recorded by the vehicle.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="code" type="number">
      The HTTP response status code.
    </ResponseField>

    <ResponseField name="path" type="string">
      The Smartcar endpoint to request data from.
    </ResponseField>

    <ResponseField name="body" type="string">
      The response body of this request. The structure of this object will vary by endpoint. See the corresponding endpoint specification.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
    "responses": [
      {
        "path": "/odometer",
        "body": {
          "distance": 37829
        },
        "code": 200,
        "headers": {
          "sc-data-age": "2019-10-24T00:43:46.000Z",
          "sc-unit-system": "metric"
        }
      },
      {
        "path": "/location",
        "body": {
          "latitude": 37.4292,
          "longitude": 122.1381
        },
        "code": 200,
        "headers": {
          "sc-data-age": "2019-10-24T00:43:46.000Z"
        }
      }
    ]
  }
  ```
</ResponseExample>
