# Source: https://upstash.com/docs/workflow/rest/dlq/delete.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/delete.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/delete.md

# Source: https://upstash.com/docs/vector/api/endpoints/delete.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/delete.md

# Source: https://upstash.com/docs/search/sdks/py/commands/delete.md

# Source: https://upstash.com/docs/workflow/rest/dlq/delete.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/delete.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/delete.md

# Source: https://upstash.com/docs/vector/api/endpoints/delete.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/delete.md

# Source: https://upstash.com/docs/search/sdks/py/commands/delete.md

# Source: https://upstash.com/docs/workflow/rest/dlq/delete.md

# Source: https://upstash.com/docs/vector/sdks/ts/commands/delete.md

# Source: https://upstash.com/docs/vector/sdks/py/example_calls/delete.md

# Source: https://upstash.com/docs/vector/api/endpoints/delete.md

# Source: https://upstash.com/docs/search/sdks/ts/commands/delete.md

# Source: https://upstash.com/docs/search/sdks/py/commands/delete.md

# Source: https://upstash.com/docs/workflow/rest/dlq/delete.md

# Delete a failed workflow run from the DLQ

> Manually remove a failed workflow run from the DLQ

Delete a failed workflow run from the Dead Letter Queue (DLQ).

When a workflow run fails, it is moved to the DLQ. You can manually remove a failed workflow run from the DLQ using this endpoint. This is useful for cleaning up failed runs that you no longer wish to retry or analyze.

## Request

<ParamField path="dlqId" type="string">
  The DLQ id of the failed workflow run you want to remove. You will see this id when
  listing all workflow runs in the DLQ with the [/v2/workflows/dlq](/workflow/rest/dlq/list) endpoint.
</ParamField>

## Response

The endpoint doesn't return a response body. A status code of 200 means the workflow run was removed from the DLQ.
If the workflow run is not found in the DLQ (either it has already been removed by you, or automatically), the endpoint returns a 404 status code.

<RequestExample>
  ```sh  theme={"system"}
  curl -X DELETE https://qstash.upstash.io/v2/workflows/dlq/my-dlq-id \
    -H "Authorization: Bearer <token>"
  ```
</RequestExample>
