# Source: https://smartcar.com/docs/api-reference/webhooks/subscribe-webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscribe

> Subscribe a vehicle to a webhook.

## Request

**Path**

<Snippet file="api-reference/path-vehicle-id.mdx" />

<ParamField path="webhook_id" type="string" initialValue="9b6ae692-60cc-4b3e-89d8-71e7549cf805" required>
  The webhook id you are subscribing the vehicle to. This can be found in Dashboard under Webhooks.
</ParamField>

<Snippet file="code-group-subscribe.mdx" />

<RequestExample>
  <Snippet file="api-reference/core-sdk-methods/subscribe-webhook.mdx" />
</RequestExample>

## Response

<ResponseField name="vehicleId" type="string">
  The [vehicle id](/api-reference/all-vehicles) of the vehicle you are making a request to.
</ResponseField>

<ResponseField name="webhookId" type="string">
  The webhook id you are subscribing the vehicle to.
</ResponseField>

<ResponseExample>
  ```json ResponseExample theme={null}
  {
      "vehicleId": "dc6ea99e-57d1-4e41-b129-27e7eb58713e",
      "webhookId": "9b6ae692-60cc-4b3e-89d8-71e7549cf805"
  }   
  ```
</ResponseExample>
