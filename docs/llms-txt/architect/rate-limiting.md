# Source: https://docs.architect.co/concepts/rate-limiting.md

# Rate-Limiting

{% hint style="warning" %}
Effective December 19, 2025, Architect will enforce rate limits by user ID. The rate limits will impact any application, script, or manual usage that communicates excessively with the Architect API.

It is essential to review your code and the Architect documentation to ensure best practices in optimizing requests.
{% endhint %}

Architect limits the rate of incoming gRPC requests per user (including usage of the SDK) to ensure services are reliable and responsive. Rate limiting is enforced on a per-user basis, meaning each authenticated user has their own independent rate limit quota.

## Overview

Rate limiting applies to all gRPC requests made through the Architect API, including:

* Direct gRPC calls
* SDK usage (Python, TypeScript, Rust)
* Any application or script that communicates with Architect services

## How Rate Limiting Works

### Per-User Enforcement

Rate limits are enforced based on the authenticated user ID. When you make a request:

1. Architect extracts your user ID
2. The rate limiter checks your personal quota
3. If you have available tokens, the request proceeds
4. If your quota is exhausted, the request is rejected with a rate limit error

Note that multiple accounts under a single user share a single token bucket.

### Token Bucket Algorithm

The rate limiter uses a token bucket algorithm with the following characteristics:

* **Burst Capacity**: You can make a burst of requests up to your configured limit
* **Refill Rate**: Tokens are replenished over time according to your quota

For example, if your rate limit is 10 requests per second with a 100 burst capacity:

* You can make up to 100 requests immediately (burst)
* After consuming tokens, they refill at a rate of 10 per second
* If you exceed the burst capacity, you must wait for tokens to refill

## Default Rate Limits

By default the server will enforce rate limits with a **burst capacity** of 100 requests and a **refill rate** of 10 requests per second. This applies per user (not per account). However, Architect reserves the right to change these limits at any time depending on server capacity and use cases.

## Rate Limit Responses

When you exceed your rate limit, Architect returns a gRPC error with the following characteristics:

### Error Details

1. **gRPC Status Code**: `RESOURCE_EXHAUSTED` (code 8)
2. **Error Message**: `"rate limit exceeded"`
3. **Retry-After Header**: Provides the recommended wait time in milliseconds before retrying

### Handling the Error in Python Example

When using the Python SDK, you'll receive an `AioRpcError`:

**Example Error Output**:

```
AioRpcError: <AioRpcError of RPC that terminated with:
	status = StatusCode.RESOURCE_EXHAUSTED
	details = "rate limit exceeded"
	debug_error_string = "UNKNOWN:Error received from peer  {grpc_message:"rate limit exceeded", grpc_status:8}"
```

```python
from grpc import StatusCode
from grpc.aio import AioRpcError

try:
    # Some client request here
    for i in range(1000):
        _ = await client.list_accounts()
except AioRpcError as e:
    if e.code() == StatusCode.RESOURCE_EXHAUSTED:
        # Rate limit exceeded
        retry_after = e.trailing_metadata().get("retry-after")
        print(f"Rate limit exceeded: {e.details()}. Retry after {retry_after}")
    else:
        # Handle other errors
        raise
```

### Rust Example

When using the Rust SDK:

```rust
use tonic::{Code, Status};
use tokio::time::{sleep, Duration};
use humantime::parse_duration;

match client.list_accounts().await {
    Ok(response) => { /* Handle success */ }

    Err(status) if status.code() == Code::ResourceExhausted => {

        let duration = status.metadata()
            .get("retry-after")
            .and_then(|h| h.to_str().ok())
            .and_then(|s| humantime::parse_duration(s).ok())
            .unwrap_or(Duration::from_secs(1));

        eprintln!("Rate limit hit. Waiting {:?}...", duration);
        sleep(duration).await;
        // Place your retry logic here
    }
    Err(e) => {
        // Handle all other errors
        return Err(e);
    }
}
```

## Best Practices

### Use Streaming Channels Instead of Polling

The most effective way to stay within rate limits is to use Architect's streaming channels instead of repeatedly calling unary endpoints.

**Rate limit tokens are consumed per gRPC call, not per message on a stream.** Establishing a streaming connection like `orderflow` consumes only one token—all subsequent messages sent over that stream (PlaceOrder, CancelOrder, GetOrder, etc.) do not consume additional tokens.

| Approach                             | Rate Limit Impact                        |
| ------------------------------------ | ---------------------------------------- |
| Polling `get_order` in a loop        | 1 token per call ❌                       |
| Using `orderflow` channel            | 1 token to connect, unlimited messages ✅ |
| Subscribing to `subscribe_orderflow` | 1 token to connect, unlimited updates ✅  |

**Example: Prefer orderflow over polling**

```python

# Bad: Polling consumes rate limit tokens on every call
while True:
    order = await client.get_order('some_order')
    print(f" --> {order}")

# Good: Streaming uses only 1 token for the connection
async for event in client.stream_orderflow():
    print(f" --> {event}")
```

### Batch and Cache Where Possible

* **Batch requests**: Use batch endpoints (e.g., `place_batch_order`) instead of making multiple individual calls
* **Cache static data**: Cache infrequently changing data like account lists or product definitions to reduce redundant API calls

### Request Backoff

Clients should treat `RESOURCE_EXHAUSTED` as a signal to alleviate pressure. Retrying after a delay is recommended, and doubling the delay upon each consecutive `RESOURCE_EXHAUSTED` message is often best practice. You can apply some [jitter](https://en.wikipedia.org/wiki/Jitter) to avoid the [thundering herd problem](https://en.wikipedia.org/wiki/Thundering_herd_problem).

###

## FAQs

### What happens when I exceed the rate limit?

When you exceed your rate limit, your request is immediately rejected with a `RESOURCE_EXHAUSTED` error. Note that this differs from throttling (where requests are slowed down). Crucially, this means that rejected calls need to be resent (if still needed).

You must wait for tokens to refill before making additional requests. The error response includes a `Retry-After` header indicating how long you should wait.

### How do I know what my rate limit is?

Rate limit quotas are configured per deployment. Default rates will be posted, but contact the Architect team to learn the specific rate limits for your environment.

### Can I request a higher rate limit?

Rate limit quotas are configured based on system capacity and fair usage policies. Contact the Architect team to discuss your specific needs.

### Do rate limits apply to all gRPC methods?

Yes, rate limiting applies to all gRPC requests made to Architect services, regardless of the specific method or service being called.

### How are rate limits enforced across multiple connections?

Rate limits are enforced per user ID, not per connection. If you have multiple connections or clients using the same user credentials, they all share the same rate limit quota.
