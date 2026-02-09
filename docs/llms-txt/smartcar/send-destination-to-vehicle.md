# Source: https://smartcar.com/docs/api-reference/send-destination-to-vehicle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Destination

> Send destination coordinates to the vehicle's navigation system.

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

## Permission

`control_navigation`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="latitude" type="number" initialValue="51.5007" required>
  The latitude of the location you wish to set the vehicle's navigation to.
</ParamField>

<ParamField body="longitude" type="number" initialValue="0.1246" required>
  The longitude of the location you wish to set the vehicle's navigation to.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/send-destination-to-vehicle.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  If the request is successful, Smartcar will return “success” (HTTP 200 status).
</ResponseField>

<ResponseField name="message" type="string">
  If the request is successful, Smartcar will return a message (HTTP 200 status).
</ResponseField>

<ResponseExample>
  ```json Example Response  theme={null}
  {
      "message": "Successfully sent request to vehicle",
      "status": "success"
  }   
  ```
</ResponseExample>
