# Source: https://grafbase.com/docs/gateway/errors.md

# Gateway Errors

Our implementation follows the [GraphQL-over-HTTP](https://github.com/graphql/graphql-over-http/blob/main/spec/GraphQLOverHTTP.md) specification, which defines three main request scenarios:

- The server might deny requests due to missing authentication, rate limits, invalid JSON, or similar issues. In these cases, it returns an appropriate `4xx` or `5xx` status code.
- For a well-formed GraphQL-over-http request, your `Accept` header determines:
  - For `application/json`, the server returns a `200` status code.
  - For `application/graphql-response+json`:
    - When errors occur without any `data`, the server returns the appropriate `4xx` or `5xx` status code.
    - When the server generates at least a partial response, it returns a `200` status code.

## Status Codes

When you send a request with the `Accept` header value `application/graphql-response+json`, you receive the following status codes when the server denies your request:

- `400`: Invalid format in GraphQL-over-http request (for example: invalid JSON)
- `401`: Request needs authentication
- `406`: Request has missing or unsupported `Accept` header
- `429`: Request exceeded rate limit
- `500`: Server encountered an internal error

## Error Codes

All GraphQL errors include an error `code` in `extensions`. Each code corresponds to a HTTP status code. For request errors (where `data` is not present), these codes specify the response when the client sends `Accept: application/graphql-response+json`. When multiple errors occur, the server prioritizes client error `4xx` over server error `5xx`.

Error codes can be changed with the [error code mapping](https://grafbase.com/docs/gateway/configuration/error-code-mapping.md).

### Status Code: 400

- `BAD_REQUEST`: Server detected a client error and refused to process the request.
- `TRUSTED_DOCUMENT_ERROR`: System can't load or find the trusted document.
- `PERSISTED_QUERY_ERROR`: Automatic persisted query fails.
- `PERSISTED_QUERY_NOT_FOUND`: System requires an automatic persisted query that doesn't exist.
- `OPERATION_PARSING_ERROR`: Operation parsing fails.
- `OPERATION_VALIDATION_ERROR`: Operation validation fails.
- `OPERATION_PLANNING_ERROR`: Operation planning fails.

### Status Code: 401

- `UNAUTHENTICATED`: User is not authenticated.

### Status Code: 403

- `UNAUTHORIZED`: User is not authorized.

### Status Code: 429

- `RATE_LIMITED`: Request was rate limited.

### Status Code: 500

- `INTERNAL_SERVER_ERROR`: Internal server error.
- `HOOK_ERROR`: Hook failed or returned an error.

### Status Code: 502

- `SUBGRAPH_ERROR`: GraphQL error coming from the subgraph.
- `SUBGRAPH_INVALID_RESPONSE_ERROR`: Subgraph returned an invalid response.
- `SUBGRAPH_REQUEST_ERROR`: Request to the subgraph failed.

### Status Code: 504

- `GATEWAY_TIMEOUT`: Request execeed the global timeout.