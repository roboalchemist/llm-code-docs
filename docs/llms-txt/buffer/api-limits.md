# Source: https://developers.buffer.com/guides/api-limits.md

Rate limits are applied using a dual-layer strategy to ensure fair usage across all accounts and clients.

### Rate Limits by Client Type

- **Third-party Clients**: 100 requests per 15 minutes
- **Unknown/Unauthenticated**: 50 requests per 15 minutes
- **Account Overall** (all clients combined): 2000 requests per 15 minutes

### How It Works

Rate limits are applied in two layers:

1. **Client + Account**: Limits requests per client and account combination. This prevents a single client from overwhelming the API for a specific account.
2. **Account Overall**: Limits total requests per account across all clients. This prevents bypassing limits by using multiple clients simultaneously.

### Response Headers

Rate limit information is included in the response headers:

```http
RateLimit-Limit: 1000
RateLimit-Remaining: 850
RateLimit-Reset: 2024-01-01T12:00:00.000Z
```

### Error Response

When a rate limit is exceeded, you will receive an HTTP `429 Too Many Requests` response:

```json
{
  "errors": [
    {
      "message": "Too many requests from this client. Please try again later.",
      "extensions": {
        "code": "RATE_LIMIT_EXCEEDED",
        "limitType": "CLIENT_ACCOUNT",
        "retryAfter": 900
      }
    }
  ]
}
```

Use the `retryAfter` value (in seconds) to determine when you can make requests again.

## Query Limits

In addition to rate limits, the API enforces query-level limits to protect against overly complex or expensive GraphQL queries.

### Query Complexity

Each query is assigned a cost based on the fields it requests:

- **Scalar fields** (e.g., `id`, `name`): 1 point each
- **Object fields** (e.g., `organization`, `channel`): 2 points each
- **Nesting multiplier**: Nested fields are multiplied by a factor of 1.5x per level of depth

The maximum allowed query cost is **175,000 points**. If your query exceeds this, you will receive an error asking you to simplify it.

### Query Depth

Queries are limited to a maximum depth of **25 levels**. Deeply nested queries can cause exponential resource consumption, so keep your queries as flat as possible.

### Aliases

A maximum of **30 aliases** are allowed per query. Aliases let you rename fields in a response, but excessive use can be used to amplify query cost.

### Directives

Queries are limited to a maximum of **50 directives**.

### Tokens

Queries are limited to a maximum of **15,000 tokens**. This is a parser-level limit on the overall size of the query document.

### Query Limit Error Responses

When a query limit is exceeded, you will receive a GraphQL error response:

```json
{
  "errors": [
    {
      "message": "Query exceeds maximum allowed complexity. Please simplify your query."
    }
  ]
}
```

The error message will indicate which limit was exceeded (complexity, depth, aliases, directives, or tokens).

These limits may change as we continue to evolve the API, so please ensure you monitor your usage accordingly.