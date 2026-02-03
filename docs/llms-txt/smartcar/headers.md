# Source: https://smartcar.com/docs/api-reference/headers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Headers

Smartcar uses the following headers for requests and responses.

## Request

<ParamField header="SC-Unit-System" type="string" default="metric">
  Smartcar supports both `metric` and `imperial` unit systems of measurement.
</ParamField>

<RequestExample>
  ```bash Request Headers theme={null}
  SC-Unit-System: metric
  ```
</RequestExample>

## Response

<ResponseField name="SC-Data-Age" type="string">
  Indicates the timestamp (ISO-8601 format) of when the returned data was recorded by the vehicle.
</ResponseField>

<ResponseField name="SC-Fetched-At" type="string">
  Indicates the timestamp (ISO-8601 format) of when Smartcar fetched the data from the OEM.
</ResponseField>

<ResponseField name="SC-Unit-System" type="string">
  Indicates whether the unit system used in the returned data is `imperial` or `metric`.
</ResponseField>

<ResponseField name="SC-Request-Id" type="string">
  Each response from Smartcar's API has a unique request identifier. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.
</ResponseField>

<ResponseExample>
  ```bash Response Headers theme={null}
  SC-Data-Age: 2018-06-20T01:33:37.078Z
  SC-Fetched-At: 2018-06-20T01:48:37.078Z
  SC-Unit-System: metric
  SC-Request-Id: 26c14915-0c26-43c5-8e42-9edfc2a66a0f
  ```
</ResponseExample>
