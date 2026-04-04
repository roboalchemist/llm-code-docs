# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/payment.mdx

<EndpointSchemaSnippet endpoint="POST /payments" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "PWC_4nn21zy6t0v2yhqg5bvhk7xkq",
    "amount": 1500,
    "net_amount": 1000,
    "captured_amount": 1000,
    "voided_amount": 0,
    "refunded_amount": 100,
    "currency": "USD",
    "customer_id": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
    "merchant_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
    "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
    "status": "AUTHORIZED",
    "created_at": "2022-01-01T12:00:00Z",
    "updated_at": "2022-01-05T12:00:00Z",
    "refund_ids": [
      "PWCR_da1v3j4p3z15y47adpzzq0whj"
    ],
    "reference_id": "external-id",
    "metadata": {},
    "enrichments": {
      "recurring_series_id": "string"
    },
    "decline_errors": [
      {
        "category": "INVALID_REQUEST_ERROR",
        "code": "MISSING_REQUIRED_FIELD",
        "detail": "Missing required parameter.",
        "field": "field_a[2].field_b"
      }
    ]
  }
  ```
</Aside>
