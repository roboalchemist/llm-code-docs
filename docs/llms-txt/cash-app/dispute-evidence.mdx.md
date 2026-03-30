# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/dispute-evidence.mdx

<EndpointSchemaSnippet endpoint="POST /disputes/{dispute_id}/evidence-text" selector="response.body" />

<Aside>
  ```json Example
  {
    "id": "EVD_dbdda8e161b7bad8519f7f73",
    "dispute_id": "DSPT_1fbjn9dg7rmz1xeyv6gkyh8vg",
    "category": "GENERIC_EVIDENCE",
    "file": {
      "filename": "string",
      "content_type": "application/pdf"
    },
    "text": "string",
    "type": "FILE",
    "created_at": "2022-01-01T12:00:00Z",
    "metadata": {
      "my-meta": "meta-value"
    }
  }
  ```
</Aside>
