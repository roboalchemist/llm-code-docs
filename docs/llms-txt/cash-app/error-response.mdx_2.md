# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/customer-request-api/schemas/error-response.mdx

<EndpointSchemaSnippet endpoint="GET /error-response-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "errors": [
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
