# Source: https://smartcar.com/docs/api-reference/webhooks/unsubscribe-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Unsubscribe

> Unsubscribe a vehicle from a webhook.

## Request

**Header**

<ParamField header="Authorization" type="string" initialValue="Bearer {application_management_token}" required>
  In the format `Bearer {application_management_token}`. You can find your `application_management_token` under
  your Application Configuration in Dashboard.
</ParamField>

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<ParamField path="webhook_id" type="string" initialValue="9b6ae692-60cc-4b3e-89d8-71e7549cf805" required>
  The [webhook id](/api-reference/management/get-vehicle-connections) you are unsubscribing the vehicle from.
</ParamField>

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/unsubscribe-webhook.mdx" />
</RequestExample>

## Response

<ResponseField name="status" type="string">
  Status of the request.
</ResponseField>

<ResponseExample>
  ```json Example Response theme={null}
  {
      "status": "success"
  }
  ```
</ResponseExample>
