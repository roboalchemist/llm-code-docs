# Source: https://www.quo.com/docs/mdx/api-reference/rate-limits.md

# Rate limits

> Quo implements rate limiting to ensure API stability and fair usage.

Each API key may make up to **10 requests per second.**

Exceeding this limit may result in `429` status code errors. If you'd like to request a higher rate limit, reach out to us at [support+developers@quo.com](mailto:support+developers@quo.com).

<Tip>
  Implement request throttling in your application to stay within rate limits and optimize API usage.
</Tip>
