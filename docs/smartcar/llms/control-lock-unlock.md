# Source: https://smartcar.com/docs/api-reference/control-lock-unlock.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lock & Unlock

> Lock or unlock the vehicle.

<Note>
  2.0 is still the only supported version for sending remote commands. If you need to send commands, please continue using v2.0 until commands are supported in the latest version later this year.
</Note>

## Permission

`control_security`

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

**Body**

<ParamField body="action" type="string" initialValue="UNLOCK" required>
  `LOCK` or `UNLOCK` the vehicle’s doors.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/control-lock-unlock.mdx" />
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
