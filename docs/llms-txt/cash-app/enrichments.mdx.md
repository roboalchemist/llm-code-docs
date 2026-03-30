# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/enrichments.mdx

<EndpointSchemaSnippet endpoint="GET /enrichments-schema" selector="response.body" />

<Aside>
  ```json Example
  {
    "initiation": {
      "actor": "CUSTOMER"
    },
    "recurring_series_id": "string",
    "statement_descriptor": "string",
    "restricted_categories": [
      "ALCOHOL"
    ]
  }
  ```
</Aside>
