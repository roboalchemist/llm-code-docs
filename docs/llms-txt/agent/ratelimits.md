# Source: https://docs.agent.ai/ratelimits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limits

> Agent.ai implements rate limit logic to ensure a consistent user experience.

## **Rate Limits**

We implement the following rate limits to ensure a consistent user experience: 20 requests per minute and 1000 requests per day.

For each request, we expose the following rate limit headers so that you can monitor and adjust your application's behavior accordingly:

* `ratelimit-limit: 1000`: 1000
* `ratelimit-remaining`: 999
* `ratelimit-reset`: The timestamp when the rate limit resets.
* `ratelimit-reset-date`: The ISO UTC date when the rate limit resets.
* `retry-after`: The number of seconds to wait before retrying the request.
