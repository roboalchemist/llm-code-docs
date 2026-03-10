# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/disputes/schemas/dispute.mdx

<EndpointSchemaSnippet endpoint="GET /dispute-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "dp_N64jYg4RC4ZBUsXjLzE3W5",
    "order": "123456789",
    "amount": "48.46",
    "reason": "product_not_received",
    "status": "needs_response",
    "open": true,
    "responseDueBy": "1691884800",
    "createdAt": "1691880800",
    "openingNote": "Customer has no knowledge of the payment",
    "openingNoteAttachments": "[“fi_48vmw3sXdVqvtJGXbgKbAZ”]",
    "updatedAt": "1691884000",
    "closingReason": "merchant_accepted",
    "closingNote": "Merchant accepted the dispute",
    "merchantOrderId": "order54321",
    "transactionDate": "1691882800",
    "settlementAmount": "48.46",
    "meta": {
      "transactionAmount": "48.46",
      "network": "Visa",
      "networkReferenceId": "string",
      "orderType": "ONLINE"
    }
  }
  ```
</Aside>
