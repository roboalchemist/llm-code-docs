# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/schemas/grant.mdx

<EndpointSchemaSnippet endpoint="GET /grant-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
    "intent": "ON_FILE",
    "type": "CASHAPP",
    "details": {
      "status": "ACTIVE",
      "cashapp": {
        "customerId": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
        "cashtag": "$someCashTag"
      },
      "createdAt": "2024-07-08T22:42:46.039Z",
      "updatedAt": "2024-07-08T22:42:46.039Z",
      "expiresAt": "2034-07-08T22:42:46.039Z"
    }
  }
  ```
</Aside>
