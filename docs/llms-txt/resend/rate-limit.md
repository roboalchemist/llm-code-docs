# Source: https://resend.com/docs/api-reference/rate-limit.md

# Rate Limit

> Understand rate limits and how to increase them.

The response headers describe your current rate limit following every request in conformance with the [sixth IETF standard draft](https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-ratelimit-headers-06):

| Header name           | Description                                                         |
| --------------------- | ------------------------------------------------------------------- |
| `ratelimit-limit`     | Maximum number of requests allowed within a window.                 |
| `ratelimit-remaining` | How many requests you have left within the current window.          |
| `ratelimit-reset`     | How many seconds until the limits are reset.                        |
| `retry-after`         | How many seconds you should wait before making a follow-up request. |

The default maximum rate limit is **2 requests per second**. This number can be increased for trusted senders upon request.

After that, you'll hit the rate limit and receive a `429` response error code. You can find all 429 responses by filtering for 429 at the [Resend Logs page](https://resend.com/logs?status=429).

To prevent this, we recommend reducing the rate at which you request the API. This can be done by introducing a queue mechanism or reducing the number of concurrent requests per second. If you have specific requirements, [contact support](https://resend.com/contact) to request a rate increase.
