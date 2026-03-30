# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/dispute.mdx

<EndpointSchemaSnippet endpoint="POST /disputes/:dispute_id/accept" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "DSPT_1fbjn9dg7rmz1xeyv6gkyh8vg",
    "payment_id": "PWC_4nn21zy6t0v2yhqg5bvhk7xkq",
    "amount": 1500,
    "customer_credited_amount": 1250,
    "reason": "FR10",
    "settlement_withholding": "NOT_WITHHELD",
    "state": "RESPONSE_REQUIRED",
    "created_at": "2022-01-01T12:00:00Z",
    "response_due_at": "2022-05-01T00:00:00Z",
    "updated_at": "2022-01-05T12:00:00Z",
    "merchant_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x"
  }
  ```
</Aside>
