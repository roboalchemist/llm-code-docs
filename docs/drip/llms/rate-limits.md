# Source: https://docs.drip.re/developer/rate-limits.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limits

> Understanding API rate limits, quotas, and best practices for efficient usage

The DRIP API implements rate limiting to ensure fair usage and maintain system performance for all users. This guide explains how rate limits work and how to handle them in your applications.

## Rate Limit Overview

DRIP uses a sliding window rate limiting system that tracks requests over time periods. Different endpoints may have different limits based on their resource intensity.

### Current Limits

#### Free

| Endpoint | Requests per Minute | Requests per Month |
| -------- | ------------------- | ------------------ |
| Points   | 24                  | 100,000            |

#### Pro

| Endpoint    | Requests per Minute | Requests per Month |
| ----------- | ------------------- | ------------------ |
| Points      | 300                 | 1,000,000          |
| Quests      | 120                 | 100,000            |
| Social data | 600                 | 25,000             |

#### Enterprise

| Endpoint    | Requests per Minute | Requests per Month |
| ----------- | ------------------- | ------------------ |
| Points      | 500                 | 5,000,000          |
| Quests      | 200                 | 1,000,000          |
| Social data | 1,200               | 250,000            |

<Info>
  Rate limits are applied per Realm, not per API key.
</Info>

## Rate Limit Headers

Every API response includes headers that show your current rate limit status:

```http  theme={"dark"}
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1642694400
X-RateLimit-Window: 60
```

### Header Descriptions

| Header                  | Description                                    |
| ----------------------- | ---------------------------------------------- |
| `X-RateLimit-Limit`     | Maximum requests allowed in the current window |
| `X-RateLimit-Remaining` | Requests remaining in the current window       |
| `X-RateLimit-Reset`     | Unix timestamp when the window resets          |
| `X-RateLimit-Window`    | Window duration in seconds                     |

## Handling Rate Limits

### 429 Too Many Requests

When you exceed the rate limit, the API returns a `429 Too Many Requests` status with a `Retry-After` header:

```json  theme={"dark"}
{
  "error": "Rate limit exceeded",
  "message": "Too many requests. Try again in 30 seconds.",
  "retryAfter": 30
}
```

### Implementation Examples

<CodeGroup>
  ```javascript JavaScript theme={"dark"}
  class DripClient {
    constructor(apiKey) {
      this.apiKey = apiKey;
      this.baseUrl = 'https://api.drip.re/api/v1';
    }

    async request(method, endpoint, data = null, retries = 3) {
      const url = `${this.baseUrl}${endpoint}`;
      
      for (let attempt = 0; attempt <= retries; attempt++) {
        try {
          const response = await fetch(url, {
            method,
            headers: {
              'Authorization': `Bearer ${this.apiKey}`,
              'Content-Type': 'application/json'
            },
            body: data ? JSON.stringify(data) : null
          });

          // Log rate limit info
          console.log(`Rate limit: ${response.headers.get('X-RateLimit-Remaining')}/${response.headers.get('X-RateLimit-Limit')}`);

          if (response.status === 429) {
            const retryAfter = parseInt(response.headers.get('Retry-After') || '60');
            
            if (attempt < retries) {
              console.log(`Rate limited. Retrying in ${retryAfter} seconds...`);
              await this.sleep(retryAfter * 1000);
              continue;
            }
            
            throw new Error(`Rate limit exceeded after ${retries} retries`);
          }

          if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
          }

          return response.json();
        } catch (error) {
          if (attempt === retries) throw error;
          
          // Exponential backoff for other errors
          const delay = Math.pow(2, attempt) * 1000;
          await this.sleep(delay);
        }
      }
    }

    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    }
  }

  ```

  ```python Python theme={"dark"}
  import requests
  import time
  from typing import Optional, Dict, Any

  class DripClient:
      def __init__(self, api_key: str):
          self.api_key = api_key
          self.base_url = 'https://api.drip.re/api/v1'
          self.session = requests.Session()
          self.session.headers.update({
              'Authorization': f'Bearer {api_key}',
              'Content-Type': 'application/json'
          })

      def request(self, method: str, endpoint: str, data: Optional[Dict] = None, retries: int = 3) -> Dict[Any, Any]:
          url = f"{self.base_url}{endpoint}"
          
          for attempt in range(retries + 1):
              try:
                  response = self.session.request(method, url, json=data)
                  
                  # Log rate limit info
                  remaining = response.headers.get('X-RateLimit-Remaining', 'unknown')
                  limit = response.headers.get('X-RateLimit-Limit', 'unknown')
                  print(f"Rate limit: {remaining}/{limit}")
                  
                  if response.status_code == 429:
                      retry_after = int(response.headers.get('Retry-After', 60))
                      
                      if attempt < retries:
                          print(f"Rate limited. Retrying in {retry_after} seconds...")
                          time.sleep(retry_after)
                          continue
                      
                      raise Exception(f"Rate limit exceeded after {retries} retries")
                  
                  response.raise_for_status()
                  return response.json()
                  
              except requests.exceptions.RequestException as e:
                  if attempt == retries:
                      raise e
                  
                  # Exponential backoff
                  delay = (2 ** attempt)
                  time.sleep(delay)
          
          raise Exception("Max retries exceeded")
  ```

</CodeGroup>

## Best Practices

### 1. Monitor Rate Limit Headers

Always check the rate limit headers in your responses to avoid hitting limits:

```javascript  theme={"dark"}
function checkRateLimit(response) {
  const remaining = parseInt(response.headers.get('X-RateLimit-Remaining'));
  const limit = parseInt(response.headers.get('X-RateLimit-Limit'));
  
  if (remaining < limit * 0.1) { // Less than 10% remaining
    console.warn('Approaching rate limit. Consider slowing down requests.');
  }
}
```

### 2. Implement Exponential Backoff

Use exponential backoff for retries to avoid thundering herd problems:

```javascript  theme={"dark"}
async function exponentialBackoff(attempt, maxDelay = 60000) {
  const delay = Math.min(Math.pow(2, attempt) * 1000, maxDelay);
  const jitter = Math.random() * 0.1 * delay; // Add 10% jitter
  
  await new Promise(resolve => setTimeout(resolve, delay + jitter));
}
```

### 3. Batch Operations

Use batch endpoints when available to reduce API calls:

```javascript  theme={"dark"}
// Instead of multiple individual updates
for (const member of members) {
  await updateMemberBalance(realmId, member.id, 10); // 100 API calls
}

// Use batch update
await batchUpdateBalances(realmId, members.map(m => ({
  memberId: m.id,
  tokens: 10
}))); // 1 API call
```

### 4. Cache Frequently Accessed Data

Implement caching to reduce redundant API calls:

```javascript  theme={"dark"}
class CachedDripClient extends DripClient {
  constructor(apiKey, cacheTtl = 300000) { // 5 minutes
    super(apiKey);
    this.cache = new Map();
    this.cacheTtl = cacheTtl;
  }

  async getRealm(realmId) {
    const cacheKey = `realm:${realmId}`;
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.cacheTtl) {
      return cached.data;
    }

    const realm = await this.request('GET', `/realms/${realmId}`);
    this.cache.set(cacheKey, {
      data: realm,
      timestamp: Date.now()
    });

    return realm;
  }
}
```

## Endpoint-Specific Limits

Some endpoints have additional restrictions:

### Batch Operations

* **Batch member updates**: Maximum 100 members per request
* **Member search**: Maximum 50 values per search

### File Operations

* **Asset uploads**: 10 MB maximum file size
* **Bulk imports**: Maximum 1,000 records per import

### Webhooks

* **Webhook calls**: Maximum 5 retries per event
* **Webhook timeout**: 30 seconds maximum response time

## Monitoring and Alerts

### Track Your Usage

Implement usage tracking to monitor your API consumption:

```javascript  theme={"dark"}
class UsageTracker {
  constructor() {
    this.requests = [];
  }

  recordRequest(endpoint, status, remaining) {
    this.requests.push({
      endpoint,
      status,
      remaining,
      timestamp: Date.now()
    });

    // Keep only last hour of data
    const oneHourAgo = Date.now() - 3600000;
    this.requests = this.requests.filter(r => r.timestamp > oneHourAgo);
  }

  getUsageStats() {
    const totalRequests = this.requests.length;
    const errorRequests = this.requests.filter(r => r.status >= 400).length;
    const rateLimitedRequests = this.requests.filter(r => r.status === 429).length;

    return {
      totalRequests,
      errorRate: errorRequests / totalRequests,
      rateLimitRate: rateLimitedRequests / totalRequests
    };
  }
}
```

### Set Up Alerts

Create alerts for approaching rate limits:

```javascript  theme={"dark"}
function checkForAlerts(usageStats, rateLimitRemaining, rateLimitLimit) {
  const usagePercentage = (rateLimitLimit - rateLimitRemaining) / rateLimitLimit;
  
  if (usagePercentage > 0.8) {
    console.warn('WARNING: Using 80% of rate limit');
    // Send alert to monitoring system
  }
  
  if (usageStats.rateLimitRate > 0.05) {
    console.error('ERROR: High rate limit rejection rate');
    // Send alert to monitoring system
  }
}
```

## Upgrading Limits

If you consistently hit rate limits, consider upgrading your plan:

<CardGroup cols={3}>
  <Card title="Analyze Usage" icon="chart-line">
    Review your API usage patterns and identify peak times
  </Card>

  <Card title="Optimize Code" icon="code">
    Implement caching, batching, and efficient request patterns
  </Card>

  <Card title="Upgrade Plan" icon="arrow-up">
    Contact support to discuss higher rate limits for your use case
  </Card>
</CardGroup>

## Rate Limit Errors

### Common Error Scenarios

<AccordionGroup>
  <Accordion title="Burst Limit Exceeded">
    **Cause**: Too many requests in a very short time period

    **Solution**: Implement request queuing and spacing between calls

    ```javascript  theme={"dark"}
    class RequestQueue {
      constructor(maxConcurrent = 5, delayMs = 100) {
        this.queue = [];
        this.running = 0;
        this.maxConcurrent = maxConcurrent;
        this.delayMs = delayMs;
      }

      async add(requestFn) {
        return new Promise((resolve, reject) => {
          this.queue.push({ requestFn, resolve, reject });
          this.process();
        });
      }

      async process() {
        if (this.running >= this.maxConcurrent || this.queue.length === 0) {
          return;
        }

        this.running++;
        const { requestFn, resolve, reject } = this.queue.shift();

        try {
          const result = await requestFn();
          resolve(result);
        } catch (error) {
          reject(error);
        } finally {
          this.running--;
          setTimeout(() => this.process(), this.delayMs);
        }
      }
    }
    ```
  </Accordion>

  <Accordion title="Sustained High Usage">
    **Cause**: Consistently high request volume over time

    **Solution**: Implement better caching and consider plan upgrade
  </Accordion>

  <Accordion title="Inefficient Polling">
    **Cause**: Frequent polling for updates instead of using webhooks

    **Solution**: Switch to webhook-based updates for real-time data
  </Accordion>
</AccordionGroup>

## Testing Rate Limits

### Development Environment

Test your rate limit handling in development:

```javascript  theme={"dark"}
async function testRateLimit() {
  const client = new DripClient(process.env.DRIP_API_KEY);
  
  // Make rapid requests to trigger rate limiting
  const promises = [];
  for (let i = 0; i < 150; i++) {
    promises.push(client.getRealm('YOUR_REALM_ID'));
  }
  
  try {
    await Promise.all(promises);
  } catch (error) {
    console.log('Rate limit handling test:', error.message);
  }
}
```

<Warning>
  Only test rate limits in development environments with test API keys to avoid impacting production systems.
</Warning>

## Summary

Effective rate limit handling involves:

1. **Monitor** rate limit headers in all responses
2. **Implement** exponential backoff and retry logic
3. **Use** batch operations and caching to reduce calls
4. **Track** usage patterns and set up alerts
5. **Optimize** your integration for efficiency

Following these practices will ensure your integration remains reliable and performs well within DRIP's rate limits.

Built with [Mintlify](https://mintlify.com).
