# Source: https://developers-classic.mailerlite.com/docs/api-rate-limits.md

# API rate limits

Our API has rate limits, which means that 60 requests on individual endpoints can be made per minute. If this limit is exceeded, you will need to wait until the quota resets.

Each endpoint with a rate limit has a \[Rate limited] tag on the [API reference page](https://developers-classic.mailerlite.com/reference).

Each API request comes back with four headers related specifically to rate limiting:

| Header                  | Meaning                                                                 |
| :---------------------- | :---------------------------------------------------------------------- |
| X-RateLimit-Limit       | The maximum number of API requests that the user can make per minute.   |
| X-RateLimit-Remaining   | The remaining number of API requests that the user can make per minute. |
| X-RateLimit-Reset       | A date and time value indicating when the remaining limit resets.       |
| X-RateLimit-Retry-After | Indicates the seconds remaining before you can make a new request.      |