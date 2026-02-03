# Source: https://docs.chatling.ai/api-reference/v2/rate-limiting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate limiting

> Our API has rate limits to prevent abuse and ensure fair usage.

We enforce rate limits to balance the load on our servers and provide a fair environment for all developers to interact with the Chatling API.

Therefore, the number of requests you send to the API will be measured and throttled if you surpass the allowed rate limit.

## Rate limit

The default rate limit is **300 API calls per minute** for each API key. We may adjust these limits in the future.

When you exceed the rate limit, you will receive a 429 status code with the following response:

```json  theme={null}
{
    "status": "error",
    "message": "Too many requests"
}
```

## When does the rate limit reset?

The rate limit lasts 1 minute, and the number of requests you've sent within that window will reset at the next minute.
