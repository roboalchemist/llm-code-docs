# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/schemas/grant.mdx

<EndpointSchemaSnippet endpoint="GET /grant-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
    "customer_id": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
    "request_id": "GRR_1hrxhz136krcq6ezdte2ha5q",
    "action": {
      "amount": 2500,
      "currency": "USD",
      "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
      "type": "ONE_TIME_PAYMENT"
    },
    "status": "ACTIVE",
    "type": "ONE_TIME",
    "channel": "ONLINE",
    "created_at": "2019-08-24T14:15:22Z",
    "updated_at": "2019-08-24T14:15:22Z",
    "expires_at": "2022-04-01T12:00:00Z"
  }
  ```
</Aside>
