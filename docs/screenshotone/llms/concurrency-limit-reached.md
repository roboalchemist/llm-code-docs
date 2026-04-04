# Source: https://screenshotone.com/docs/errors/concurrency-limit-reached/

# Concurrency Limit Reached

It is an API error returned when the request concurrency limit has been reached.

```json
{
    "is_successful": false,
    "error_code": "concurrency_limit_reached",
    "error_message": "You reached the request concurrency limit, retry after a while. Or feel free to upgrade your current plan—https://dash.screenshotone.com/subscription.",
    "documentation_url": "https://screenshotone.com/docs/errors/concurrency-limit-reached/"
}
```

## Reasons and how to fix

### Exceeded Concurrency Limit

The most common reason for the "concurrency_limit_reached" error is that you have reached the maximum number of concurrent requests allowed by your current subscription plan.

To fix this, you can:

1. **Wait and retry**: Wait for some of the current requests to complete and then retry your request.
2. **Upgrade your plan**: Visit the [subscription page](https://dash.screenshotone.com/subscription) to upgrade your plan, which will increase your concurrency limit.

### High Traffic Periods

During high traffic periods, you might hit the concurrency limit more frequently if multiple requests are being made simultaneously.

To fix this, consider:

1. **Load balancing**: Implementing load balancing strategies to distribute requests more evenly over time.
2. **Queueing requests**: Queueing requests and processing them in batches to avoid hitting the concurrency limit.

### Inefficient Request Handling

If your application is not handling requests efficiently, it might lead to a buildup of concurrent requests, hitting the limit.

To fix this, review your application’s request handling logic to ensure that requests are being processed and completed as efficiently as possible.

## Reach out to support

If you continue to face issues, please reach out to `support@screenshotone.com`, and we will assist you as soon as possible.