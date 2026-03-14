# Source: https://docs.drip.re/developer/best-practices.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.drip.re/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices

> Production-ready patterns and tips for DRIP API development 🚀

Build robust, scalable, and secure DRIP integrations with these battle-tested best practices from the community.

## Security First 🔒

### API Key Management

<CardGroup cols={2}>
  <Card title="Environment Variables" icon="key">
    ```javascript  theme={"dark"}
    // ✅ Good
    const client = new DripClient(
      process.env.DRIP_API_KEY,
      process.env.DRIP_REALM_ID
    );

    // ❌ Never do this
    const client = new DripClient(
      'drip_1234567890abcdef',
      '507f1f77bcf86cd799439011'
    );
    ```
  </Card>

  <Card title="Key Rotation" icon="arrows-rotate">
    ```javascript  theme={"dark"}
    // Implement key rotation
    class SecureDripClient {
      async rotateApiKey(newKey) {
        // Test new key first
        const testClient = new DripClient(newKey, this.realmId);
        await testClient.getRealm();

        // If successful, update
        this.apiKey = newKey;
        console.log('✅ API key rotated');
      }
    }
    ```
  </Card>
</CardGroup>

### Scope Minimization

Only request the scopes you actually need:

```javascript  theme={"dark"}
// ✅ Good: Minimal scopes for analytics app
const analyticsScopes = [
  'realm:read',
  'members:read'
];

// ❌ Bad: Requesting unnecessary permissions
const badScopes = [
  'realm:read',
  'members:read',
  'members:write',  // Don't need this for analytics
  'admin:read',     // Way too broad
  'webhooks:write'  // Not needed
];
```

## Performance Optimization ⚡

### Batch Operations

Use batch endpoints whenever possible:

<Tabs>
  <Tab title="JavaScript">
    ```javascript  theme={"dark"}
    // ❌ Slow: Individual requests
    for (const member of members) {
      await updateMemberBalance(realmId, member.id, 10);
    }
    // 100 members = 100 API calls = slow

    // ✅ Fast: Batch request
    const updates = members.map(m => ({ 
      memberId: m.id, 
      tokens: 10 
    }));
    await batchUpdateBalances(realmId, updates);
    // 100 members = 1 API call = fast
    ```
  </Tab>

  <Tab title="Python">
    ```python  theme={"dark"}
    # ❌ Slow: Individual requests
    for member in members:
        update_member_balance(realm_id, member['id'], 10)
    # 100 members = 100 API calls

    # ✅ Fast: Batch request
    updates = [
        {'memberId': member['id'], 'tokens': 10}
        for member in members
    ]
    batch_update_balances(realm_id, updates)
    # 100 members = 1 API call
    ```
  </Tab>
</Tabs>

### Caching Strategy

Implement smart caching to reduce API calls:

```javascript  theme={"dark"}
class CachedDripClient extends DripClient {
  constructor(apiKey, realmId, cacheTtl = 300000) { // 5 minutes
    super(apiKey, realmId);
    this.cache = new Map();
    this.cacheTtl = cacheTtl;
  }

  async cachedRequest(cacheKey, requestFn) {
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.cacheTtl) {
      return cached.data;
    }

    const data = await requestFn();
    this.cache.set(cacheKey, {
      data,
      timestamp: Date.now()
    });

    return data;
  }

  async getRealm() {
    return this.cachedRequest(
      `realm:${this.realmId}`,
      () => super.getRealm()
    );
  }

  async searchMembers(type, values) {
    // Don't cache member searches as they change frequently
    return super.searchMembers(type, values);
  }
}
```

### Request Optimization

<AccordionGroup>
  <Accordion title="Parallel Requests">
    Run independent requests in parallel:

    ```javascript  theme={"dark"}
    // ❌ Slow: Sequential requests
    const realm = await client.getRealm();
    const members = await client.searchMembers('drip-id', 'all');
    const points = await client.getRealmPoints();

    // ✅ Fast: Parallel requests
    const [realm, members, points] = await Promise.all([
      client.getRealm(),
      client.searchMembers('drip-id', 'all'),
      client.getRealmPoints()
    ]);
    ```
  </Accordion>

  <Accordion title="Request Queuing">
    Implement request queuing to avoid rate limits:

    ```javascript  theme={"dark"}
    class QueuedDripClient extends DripClient {
      constructor(apiKey, realmId, maxConcurrent = 5) {
        super(apiKey, realmId);
        this.queue = [];
        this.running = 0;
        this.maxConcurrent = maxConcurrent;
      }

      async queueRequest(requestFn) {
        return new Promise((resolve, reject) => {
          this.queue.push({ requestFn, resolve, reject });
          this.processQueue();
        });
      }

      async processQueue() {
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
          setTimeout(() => this.processQueue(), 100); // Small delay
        }
      }
    }
    ```
  </Accordion>
</AccordionGroup>

## Error Handling 🛡️

### Comprehensive Error Handling

```javascript  theme={"dark"}
class RobustDripClient extends DripClient {
  async safeRequest(method, endpoint, data, options = {}) {
    const { retries = 3, retryDelay = 1000 } = options;
    
    for (let attempt = 0; attempt <= retries; attempt++) {
      try {
        return await this.request(method, endpoint, data);
      } catch (error) {
        const isLastAttempt = attempt === retries;
        
        // Don't retry client errors (4xx) except rate limits
        if (error.status >= 400 && error.status < 500 && error.status !== 429) {
          throw error;
        }
        
        // Handle rate limits
        if (error.status === 429) {
          const retryAfter = error.retryAfter || 60;
          if (!isLastAttempt) {
            console.log(`Rate limited. Retrying in ${retryAfter}s...`);
            await this.sleep(retryAfter * 1000);
            continue;
          }
        }
        
        // Retry server errors with exponential backoff
        if (error.status >= 500 && !isLastAttempt) {
          const delay = retryDelay * Math.pow(2, attempt);
          console.log(`Server error. Retrying in ${delay}ms...`);
          await this.sleep(delay);
          continue;
        }
        
        // If we get here, we've exhausted retries
        throw error;
      }
    }
  }
}
```

### Error Recovery Patterns

<Tabs>
  <Tab title="Circuit Breaker">
    ```javascript  theme={"dark"}
    class CircuitBreaker {
      constructor(threshold = 5, timeout = 60000) {
        this.failureCount = 0;
        this.threshold = threshold;
        this.timeout = timeout;
        this.state = 'CLOSED'; // CLOSED, OPEN, HALF_OPEN
        this.nextAttempt = Date.now();
      }

      async call(fn) {
        if (this.state === 'OPEN') {
          if (Date.now() < this.nextAttempt) {
            throw new Error('Circuit breaker is OPEN');
          }
          this.state = 'HALF_OPEN';
        }

        try {
          const result = await fn();
          this.onSuccess();
          return result;
        } catch (error) {
          this.onFailure();
          throw error;
        }
      }

      onSuccess() {
        this.failureCount = 0;
        this.state = 'CLOSED';
      }

      onFailure() {
        this.failureCount++;
        if (this.failureCount >= this.threshold) {
          this.state = 'OPEN';
          this.nextAttempt = Date.now() + this.timeout;
        }
      }
    }
    ```
  </Tab>

  <Tab title="Fallback Values">
    ```javascript  theme={"dark"}
    async function getMembersWithFallback(client) {
      try {
        return await client.searchMembers('drip-id', 'all');
      } catch (error) {
        console.error('Failed to fetch members, using cached data');
        return getCachedMembers(); // Fallback to cache
      }
    }

    async function getLeaderboardWithFallback(client) {
      try {
        return await client.getLeaderboard();
      } catch (error) {
        console.error('API unavailable, showing static leaderboard');
        return getStaticLeaderboard(); // Fallback to static data
      }
    }
    ```
  </Tab>
</Tabs>

## Code Organization 🏗️

### Modular Architecture

Organize your code into focused modules:

```javascript  theme={"dark"}
// services/drip.js
export class DripService {
  constructor(apiKey, realmId) {
    this.client = new DripClient(apiKey, realmId);
  }

  async getRealmInfo() {
    return this.client.getRealm();
  }
}

// services/members.js
export class MemberService extends DripService {
  async findMember(type, value) {
    const result = await this.client.searchMembers(type, value);
    return result.data?.[0] || null;
  }

  async awardPoints(memberId, points) {
    return this.client.updateMemberBalance(memberId, points);
  }
}

// services/analytics.js
export class AnalyticsService extends DripService {
  async getTopMembers(limit = 10) {
    const members = await this.client.searchMembers('drip-id', 'all');
    return members.data
      .sort((a, b) => (b.pointBalances[0]?.balance || 0) - (a.pointBalances[0]?.balance || 0))
      .slice(0, limit);
  }
}
```

### Configuration Management

Centralize your configuration:

```javascript  theme={"dark"}
// config/drip.js
export const dripConfig = {
  development: {
    apiKey: process.env.DEV_DRIP_API_KEY,
    realmId: process.env.DEV_DRIP_REALM_ID,
    baseUrl: 'https://api.drip.re/api/v1',
    rateLimit: {
      maxConcurrent: 3,
      delay: 200
    }
  },
  production: {
    apiKey: process.env.PROD_DRIP_API_KEY,
    realmId: process.env.PROD_DRIP_REALM_ID,
    baseUrl: 'https://api.drip.re/api/v1',
    rateLimit: {
      maxConcurrent: 10,
      delay: 50
    }
  }
};

export const getConfig = () => {
  const env = process.env.NODE_ENV || 'development';
  return dripConfig[env];
};
```

## Monitoring and Observability 📊

### Logging Best Practices

```javascript  theme={"dark"}
import winston from 'winston';

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  transports: [
    new winston.transports.File({ filename: 'drip-api.log' })
  ]
});

class LoggedDripClient extends DripClient {
  async request(method, endpoint, data) {
    const startTime = Date.now();
    const requestId = Math.random().toString(36).substring(7);
    
    logger.info('API request started', {
      requestId,
      method,
      endpoint,
      timestamp: new Date().toISOString()
    });

    try {
      const result = await super.request(method, endpoint, data);
      const duration = Date.now() - startTime;
      
      logger.info('API request completed', {
        requestId,
        duration,
        status: 'success'
      });
      
      return result;
    } catch (error) {
      const duration = Date.now() - startTime;
      
      logger.error('API request failed', {
        requestId,
        duration,
        status: 'error',
        error: error.message,
        stack: error.stack
      });
      
      throw error;
    }
  }
}
```

### Metrics Collection

```javascript  theme={"dark"}
class MetricsDripClient extends DripClient {
  constructor(apiKey, realmId) {
    super(apiKey, realmId);
    this.metrics = {
      requests: 0,
      errors: 0,
      totalDuration: 0,
      endpoints: new Map()
    };
  }

  async request(method, endpoint, data) {
    const startTime = Date.now();
    this.metrics.requests++;
    
    try {
      const result = await super.request(method, endpoint, data);
      this.recordSuccess(endpoint, Date.now() - startTime);
      return result;
    } catch (error) {
      this.recordError(endpoint, Date.now() - startTime);
      throw error;
    }
  }

  recordSuccess(endpoint, duration) {
    this.metrics.totalDuration += duration;
    this.updateEndpointMetrics(endpoint, duration, true);
  }

  recordError(endpoint, duration) {
    this.metrics.errors++;
    this.metrics.totalDuration += duration;
    this.updateEndpointMetrics(endpoint, duration, false);
  }

  updateEndpointMetrics(endpoint, duration, success) {
    if (!this.metrics.endpoints.has(endpoint)) {
      this.metrics.endpoints.set(endpoint, {
        requests: 0,
        errors: 0,
        totalDuration: 0
      });
    }
    
    const endpointMetrics = this.metrics.endpoints.get(endpoint);
    endpointMetrics.requests++;
    endpointMetrics.totalDuration += duration;
    if (!success) endpointMetrics.errors++;
  }

  getMetrics() {
    return {
      ...this.metrics,
      averageResponseTime: this.metrics.totalDuration / this.metrics.requests,
      errorRate: this.metrics.errors / this.metrics.requests,
      endpoints: Object.fromEntries(this.metrics.endpoints)
    };
  }
}
```

## Testing Strategies 🧪

### Unit Testing

```javascript  theme={"dark"}
// tests/drip-client.test.js
import { jest } from '@jest/globals';
import { DripClient } from '../src/drip-client.js';

describe('DripClient', () => {
  let client;
  let mockFetch;

  beforeEach(() => {
    mockFetch = jest.fn();
    global.fetch = mockFetch;
    client = new DripClient('test-key', 'test-realm');
  });

  test('should search members successfully', async () => {
    const mockResponse = {
      data: [{ id: '123', name: 'Test User' }]
    };

    mockFetch.mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse
    });

    const result = await client.searchMembers('discord-id', '123456789');
    
    expect(mockFetch).toHaveBeenCalledWith(
      expect.stringContaining('/members/search'),
      expect.objectContaining({
        headers: expect.objectContaining({
          'Authorization': 'Bearer test-key'
        })
      })
    );
    
    expect(result).toEqual(mockResponse);
  });

  test('should handle API errors gracefully', async () => {
    mockFetch.mockResolvedValueOnce({
      ok: false,
      status: 404,
      json: async () => ({ error: 'Not found' })
    });

    await expect(
      client.searchMembers('discord-id', 'invalid')
    ).rejects.toThrow('API Error: 404');
  });
});
```

### Integration Testing

```javascript  theme={"dark"}
// tests/integration.test.js
describe('DRIP API Integration', () => {
  let client;

  beforeAll(() => {
    client = new DripClient(
      process.env.TEST_DRIP_API_KEY,
      process.env.TEST_DRIP_REALM_ID
    );
  });

  test('should fetch realm information', async () => {
    const realm = await client.getRealm();
    
    expect(realm).toHaveProperty('id');
    expect(realm).toHaveProperty('name');
    expect(realm.id).toBe(process.env.TEST_DRIP_REALM_ID);
  });

  test('should handle member operations', async () => {
    // Create test member (if not exists)
    const testMemberId = 'test-member-123';
    
    // Award points
    const result = await client.updateMemberBalance(testMemberId, 100);
    expect(result).toHaveProperty('id');
    
    // Verify balance
    const members = await client.searchMembers('drip-id', testMemberId);
    expect(members.data[0].pointBalances[0].balance).toBeGreaterThanOrEqual(100);
  });
});
```

## Deployment Patterns 🚀

### Environment Configuration

```javascript  theme={"dark"}
// .env.example
DRIP_API_KEY=your_api_key_here
DRIP_REALM_ID=your_realm_id_here
NODE_ENV=production
LOG_LEVEL=info
CACHE_TTL=300000
RATE_LIMIT_MAX_CONCURRENT=10
```

### Health Checks

```javascript  theme={"dark"}
// health.js
export async function healthCheck() {
  const client = new DripClient(
    process.env.DRIP_API_KEY,
    process.env.DRIP_REALM_ID
  );

  try {
    // Simple API call to verify connectivity
    await client.getRealm();
    
    return {
      status: 'healthy',
      timestamp: new Date().toISOString(),
      services: {
        drip_api: 'up'
      }
    };
  } catch (error) {
    return {
      status: 'unhealthy',
      timestamp: new Date().toISOString(),
      services: {
        drip_api: 'down'
      },
      error: error.message
    };
  }
}
```

## Community Best Practices 🌟

### Code Reviews

When reviewing DRIP API code, check for:

* [ ] API keys not hardcoded
* [ ] Proper error handling
* [ ] Rate limit considerations
* [ ] Batch operations used where possible
* [ ] Appropriate scopes requested
* [ ] Caching implemented for static data
* [ ] Logging for debugging
* [ ] Tests covering happy and error paths

### Documentation

Document your integrations:

```javascript  theme={"dark"}
/**
 * Awards points to a member for completing a task
 * 
 * @param {string} memberId - The DRIP member ID
 * @param {number} points - Points to award (positive) or deduct (negative)
 * @param {string} reason - Reason for the point change (for logging)
 * @returns {Promise<Object>} Updated member balance
 * 
 * @example
 * await awardTaskPoints('member123', 50, 'Completed daily quest');
 */
async function awardTaskPoints(memberId, points, reason) {
  logger.info('Awarding points', { memberId, points, reason });
  
  try {
    return await client.updateMemberBalance(memberId, points);
  } catch (error) {
    logger.error('Failed to award points', { memberId, points, error });
    throw error;
  }
}
```

## Quick Checklist ✅

Before deploying your DRIP integration:

* [ ] API keys stored securely (environment variables)
* [ ] Error handling implemented with retries
* [ ] Rate limiting respected (batch operations, delays)
* [ ] Caching implemented for static data
* [ ] Logging and monitoring set up
* [ ] Tests written and passing
* [ ] Documentation updated
* [ ] Health checks implemented
* [ ] Minimal scopes requested and justified

<Info>
  **Need help?** Join our [Discord community](https://discord.gg/dripchain) to get advice from other developers and share your own best practices! 🚀
</Info>

Built with [Mintlify](https://mintlify.com).
