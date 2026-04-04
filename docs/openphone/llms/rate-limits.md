# Source: https://www.quo.com/docs/mdx/api-reference/rate-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate limits

> Quo implements rate limiting to ensure API stability and fair usage.

Each API key may make up to **10 requests per second.**

Exceeding this limit may result in `429` status code errors.

<Tip>
  Implement request throttling in your application to stay within rate limits and optimize API usage.
</Tip>
