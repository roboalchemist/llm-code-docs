# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/event-data.mdx

<EndpointSchemaSnippet endpoint="GET /event-data-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "event_id": "WE_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30",
    "type": "customer.created",
    "created_at": "2019-08-24T14:15:22Z",
    "data": {
      "id": "string",
      "object": {
        "customer": {
          "id": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
          "cashtag": "string",
          "reference_id": "CUST_123"
        }
      },
      "type": "customer"
    }
  }
  ```
</Aside>
