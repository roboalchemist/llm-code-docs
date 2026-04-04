# Source: https://docs.knock.app/api-reference/overview/batch-rate-limits.md

# Batch rate limits

Knock's batch and bulk endpoints may also have an additional layer of rate limiting applied. For these cases, Knock will also limit the number of times you can update a specific entity over a given scale. These limits are in place to prevent too many duplicate modifications applied to the same set of entities.

When you exceed a batch deduplication rate limit, Knock will still return a success (`2xx`) response if it is able to handle the request. For any entities not updated due to a rate limit hit, Knock will return the data as it exists at request time. Knock will also include an `x-ratelimited-{param}` header. The `{param}` value will be the name of the request param within which the rate limit was applied. The value will be a comma-delimited string of the param values that were rejected due to a rate limit hit.

Knock can apply batch deduplication rate limits to all or part of a request. If Knock rejects a subset of your batch, you can expect to see the full set of requested entities in the response body, and the IDs of those that were rejected in the `x-ratelimited-{param}` header.

, "1 update / second / entity"]]}
/>

```json title="Example request body"
{
  "message_ids": [1, 2, 3, 4]
}
```

```json title="Example response body"
[
  { "__typename": "Message", "id": 1 },
  { "__typename": "Message", "id": 2 },
  { "__typename": "Message", "id": 3 },
  { "__typename": "Message", "id": 4 }
]
```

```json title="Example response header"
{
  "x-ratelimited-message_ids": "2,4"
}
```
