# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/schemas/error.mdx

<EndpointSchemaSnippet endpoint="GET /error-schema" selector="response.body" />

<Aside>
  ```json Example
  {
    "category": "INVALID_REQUEST_ERROR",
    "code": "MISSING_REQUIRED_FIELD",
    "detail": "Missing required parameter.",
    "field": "field_a[2].field_b"
  }
  ```
</Aside>
