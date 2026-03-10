# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/webhook-endpoint.mdx

<EndpointSchemaSnippet endpoint="POST /webhook-endpoints" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "WC_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30",
    "api_key_id": "string",
    "reference_id": "string",
    "url": "http://example.com",
    "event_configurations": [
      {
        "event_type": "customer.created",
        "api_version": "v1"
      }
    ],
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z",
    "delivery_timeout": 5000,
    "max_delivery_frequency": null,
    "status": "APPROVED"
  }
  ```
</Aside>
