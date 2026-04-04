# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/webhook-event.mdx

<EndpointSchemaSnippet endpoint="GET /webhook-event-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "WE_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30",
    "webhook_endpoint_id": "WC_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30",
    "event_type": "customer.created",
    "status": "PENDING",
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z",
    "expires_at": "2019-08-24T14:15:22Z",
    "event_data": {
      "event_id": "WE_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30",
      "type": "customer.created",
      "created_at": "2019-08-24T14:15:22Z",
      "data": {
        "id": "string",
        "object": {
          "customer": {}
        },
        "type": "customer"
      }
    },
    "api_version": "string"
  }
  ```
</Aside>
