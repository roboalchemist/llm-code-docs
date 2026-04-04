# Source: https://upstash.com/docs/vector/api/endpoints/resumable-query/stop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Stop Resumable Query

> Ends a resumable query and releases associated resources.

## Request

<ParamField body="uuid" type="string" required>
  The unique identifier of the resumable query to end.
</ParamField>

## Response

<ResponseField name="result" type="string">
  A success message indicating the query was ended.
</ResponseField>

<RequestExample>
  ```sh curl theme={"system"}
  curl $UPSTASH_VECTOR_REST_URL/resumable-query-end \
    -X POST \
    -H "Authorization: Bearer $UPSTASH_VECTOR_REST_TOKEN" \
    -d '{
      "uuid": "550e8400-e29b-41d4-a716-446655440000"
    }'
  ```
</RequestExample>

<ResponseExample>
  ```json 200 OK theme={"system"}
  {
    "result": "Success"
  }
  ```
</ResponseExample>
