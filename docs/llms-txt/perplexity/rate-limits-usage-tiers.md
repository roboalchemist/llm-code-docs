# Source: https://docs.perplexity.ai/guides/rate-limits-usage-tiers.md

# Rate Limits & Usage Tiers

## What are Usage Tiers?

Usage tiers determine your **rate limits** and access to **beta features** based on your cumulative API spending. As you spend more on API credits over time, you automatically advance to higher tiers with increased rate limits.

<Info>
  You can check your current usage tier by visiting your [API settings page](https://www.perplexity.ai/settings/api).
</Info>

***

## Tier Progression

| Tier       | Total Credits Purchased | Status                       |
| ---------- | ----------------------- | ---------------------------- |
| **Tier 0** | \$0                     | New accounts, limited access |
| **Tier 1** | \$50+                   | Light usage, basic limits    |
| **Tier 2** | \$250+                  | Regular usage                |
| **Tier 3** | \$500+                  | Heavy usage                  |
| **Tier 4** | \$1,000+                | Production usage             |
| **Tier 5** | \$5,000+                | Enterprise usage             |

<Note>
  Tiers are based on **cumulative purchases** across your account lifetime, not current balance.
</Note>

***

## How Tiers Work

* **Automatic advancement** - Tiers increase based on your total lifetime credit purchases
* **Rate limit increases** - Higher tiers get significantly more requests per minute
* **Permanent status** - Once you reach a tier, you keep it (no downgrade)

## Rate Limits by Model

<Tabs>
  <Tab title="Tier 0">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 5                         |
    | `sonar-reasoning-pro`                      | 50                        |
    | `sonar-reasoning`                          | 50                        |
    | `sonar-pro`                                | 50                        |
    | `sonar`                                    | 50                        |
    | POST `/async/chat/completions`             | 5                         |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 1">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 10                        |
    | `sonar-reasoning-pro`                      | 50                        |
    | `sonar-reasoning`                          | 50                        |
    | `sonar-pro`                                | 50                        |
    | `sonar`                                    | 50                        |
    | POST `/async/chat/completions`             | 10                        |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 2">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 20                        |
    | `sonar-reasoning-pro`                      | 500                       |
    | `sonar-reasoning`                          | 500                       |
    | `sonar-pro`                                | 500                       |
    | `sonar`                                    | 500                       |
    | POST `/async/chat/completions`             | 20                        |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 3">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 40                        |
    | `sonar-reasoning-pro`                      | 1,000                     |
    | `sonar-reasoning`                          | 1,000                     |
    | `sonar-pro`                                | 1,000                     |
    | `sonar`                                    | 1,000                     |
    | POST `/async/chat/completions`             | 40                        |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 4">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 60                        |
    | `sonar-reasoning-pro`                      | 2,000                     |
    | `sonar-reasoning`                          | 2,000                     |
    | `sonar-pro`                                | 2,000                     |
    | `sonar`                                    | 2,000                     |
    | POST `/async/chat/completions`             | 60                        |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>

  <Tab title="Tier 5">
    | Model                                      | Requests per minute (RPM) |
    | ------------------------------------------ | ------------------------- |
    | `sonar-deep-research`                      | 100                       |
    | `sonar-reasoning-pro`                      | 2,000                     |
    | `sonar-reasoning`                          | 2,000                     |
    | `sonar-pro`                                | 2,000                     |
    | `sonar`                                    | 2,000                     |
    | POST `/async/chat/completions`             | 100                       |
    | GET `/async/chat/completions`              | 3000                      |
    | GET `/async/chat/completions/{request_id}` | 6000                      |
  </Tab>
</Tabs>

***

## Search Rate Limits

The Search API has separate rate limits that apply to all usage tiers:

| Endpoint       | Rate Limit            | Burst Capacity |
| -------------- | --------------------- | -------------- |
| POST `/search` | 3 requests per second | 3 requests     |

**Search Rate Limiter Behavior:**

* **Burst**: Can handle 3 requests instantly
* **Refill**: 1 token every 333ms
* **Sustained**: Exactly 3 QPS average over time

<Note>
  Search rate limits are independent of your usage tier and apply consistently across all accounts using the same leaky bucket algorithm.
</Note>

<Info>
  **Need Higher Search Rate Limits?**

  If you require increased rate limits for the Search API beyond the standard 3 requests per second, please fill out our [rate limit increase request form](https://perplexity.typeform.com/to/yctmfyVT). We'll review your use case and work with you to accommodate your needs.
</Info>

***

## How Rate Limiting Works

Our rate limiting system uses a **leaky bucket algorithm** that allows for burst traffic while maintaining strict long-term rate control.

### Technical Implementation

<AccordionGroup>
  <Accordion title="Leaky Bucket Algorithm Explained">
    The leaky bucket algorithm works like a bucket with a small hole in the bottom:

    * **Bucket Capacity**: Maximum number of requests you can make instantly (burst capacity)
    * **Leak Rate**: How quickly tokens refill over time (your rate limit)
    * **Token Refill**: New requests become available at regular intervals

    **Key Benefits:**

    * ✅ Allows legitimate burst traffic
    * ✅ Prevents sustained abuse
    * ✅ Predictable and fair rate enforcement
  </Accordion>

  <Accordion title="Rate Limiter Behavior Example">
    Let's examine how **3 requests per second** works in practice:

    **Parameters:**

    * Capacity: 3 tokens
    * Leak rate: 3 tokens/second
    * Refill: 1 token every 333ms

    **Scenario 1: Burst Traffic**

    ```
    Time 0.0s: Bucket full (3 tokens)
    → Send 3 requests instantly → ALL ALLOWED ✅
    → Send 4th request → REJECTED ❌ (bucket empty)

    Time 0.333s: 1 token refilled
    → Send 1 request → ALLOWED ✅
    → Send 2nd request → REJECTED ❌

    Time 0.666s: 1 more token refilled
    → Send 1 request → ALLOWED ✅
    ```

    **Scenario 2: Steady 3 QPS**

    ```
    Request every 333ms:
    Time 0.0s: Request → ✅ (3→2 tokens)
    Time 0.333s: Request → ✅ (2+1-1=2 tokens)
    Time 0.666s: Request → ✅ (2+1-1=2 tokens)
    ... maintains 2-3 tokens, all requests pass
    ```

    **Scenario 3: Slightly Over 3 QPS**

    ```
    Request every 300ms (≈3.33 QPS):
    → Eventually tokens deplete faster than refill
    → Some requests start getting rejected
    → Achieves exactly 3 QPS on average
    ```
  </Accordion>

  <Accordion title="Real-World Implications">
    **What this means for your applications:**

    **✅ Burst Tolerance:**

    * Can handle your full rate limit instantly
    * Perfect for batch operations or sudden traffic spikes
    * No need to artificially spread requests

    **✅ Predictable Behavior:**

    * Strict average rate enforcement over time
    * Quick recovery after burst usage
    * Consistent performance across different usage patterns

    **❌ Abuse Prevention:**

    * Prevents sustained over-limit usage
    * Blocks excessive burst attempts
    * Maintains fair resource allocation

    **Best Practices:**

    * Take advantage of burst capacity for batch operations
    * Monitor your usage patterns to optimize request timing
    * Implement proper error handling for 429 responses
  </Accordion>
</AccordionGroup>

***

## What Happens When You Hit Rate Limits?

When you exceed your rate limits:

1. **429 Error** - Your request gets rejected with "Too Many Requests"
2. **Continuous Refill** - Tokens refill continuously based on your rate limit
3. **Immediate Recovery** - New requests become available as soon as tokens refill

**Example Recovery Times:**

* **3 QPS limit**: 1 token refills every 333ms
* **50 QPS limit**: 1 token refills every 20ms
* **500 QPS limit**: 1 token refills every 2ms

<Tip>
  **Best Practices:**

  * Monitor your usage to predict when you'll need higher tiers
  * Consider upgrading your tier proactively for production applications
  * Implement exponential backoff with jitter in your code
  * Take advantage of burst capacity for batch operations
  * Don't artificially spread requests if you have available burst capacity
</Tip>

***

## Upgrading Your Tier

<Steps>
  <Step title="Check Current Tier">
    Visit your [API settings page](https://www.perplexity.ai/settings/api) to see your current tier and total spending.
  </Step>

  <Step title="Purchase More Credits">
    Add credits to your account through the billing section. Your tier will automatically upgrade once you reach the spending threshold.
  </Step>

  <Step title="Verify Upgrade">
    Your new rate limits take effect immediately after the tier upgrade. Check your settings page to confirm.
  </Step>
</Steps>

<Check>
  Higher tiers significantly improve your API experience with increased rate limits, especially important for production applications.
</Check>
