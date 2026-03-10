# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/schemas/capture-payment.mdx

<EndpointSchemaSnippet endpoint="GET /capture-payment-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
    "merchantReference": "merchant-order-123",
    "amount": {
      "amount": "100.00",
      "currency": "AUD"
    },
    "paymentEventMerchantReference": "payment-ref-123"
  }
  ```
</Aside>
