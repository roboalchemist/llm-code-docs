# Web Caching Solutions - Quick Reference

Fast lookup guide for choosing and implementing caching solutions.

---

## Decision Tree

```
Need to cache HTTP responses?
├─ YES → Need complex caching logic?
│  ├─ YES → Use Varnish Cache
│  └─ NO → Need load balancing?
│     ├─ YES → Use HAProxy with caching
│     └─ NO → Use Nginx proxy_cache
└─ NO → Need to cache application data?
   ├─ Complex data structures? → Use Redis
   ├─ Simple strings, max speed? → Use Memcached
   └─ API Gateway scenario?
      ├─ AWS native? → AWS API Gateway
      ├─ Kubernetes/Cloud-native? → Kong
      └─ Hybrid cloud? → Gravitee
```

---

## Quick Comparison Table

### HTTP/Proxy Caching

| Tool | Best For | Learning Curve | Performance | Cost |
|------|----------|-----------------|-------------|------|
| **Varnish** | Complex rules, e-commerce | High | Very High | Open Source |
| **Nginx** | General purpose | Low | Excellent | Open Source |
| **HAProxy** | Load balancing + caching | Medium | Excellent | Open Source |
| **Squid** | Corporate proxies | Medium | Good | Open Source |

### In-Memory Stores

| Tool | Best For | Throughput | Memory Usage | Complexity |
|------|----------|-----------|--------------|-----------|
| **Redis** | Sessions, complex data | High | Moderate | Low-Medium |
| **Memcached** | Simple caching, speed | Highest | Low | Very Low |

### API Gateways

| Tool | Environment | Caching | Cost |
|------|------------|---------|------|
| **Kong** | Kubernetes | Plugin-based | Open Source |
| **AWS API Gateway** | AWS | Built-in | Pay-per-use |
| **Azure API Mgmt** | Azure | Built-in | Pay-per-unit |
| **Traefik** | Containers | Via Redis | Open Source |

### GraphQL Caching

| Tool | Type | Normalized | Best For |
|------|------|-----------|----------|
| **Apollo Client** | Client-side | Yes | React, flexible |
| **Relay** | Client-side | Yes | Type-safe, large apps |
| **URQL** | Client-side | Optional | Lightweight apps |
| **Apollo Server** | Server-side | N/A | Response caching |

### Edge/CDN

| Service | Features | Free Tier | Best For |
|---------|----------|-----------|----------|
| **Cloudflare** | Workers, Rules, Tags | Yes | Global, edge compute |
| **AWS CloudFront** | Origin Shield, Lambda@Edge | 1 month free | AWS-native |
| **Fastly** | Real-time purge, VCL | No | Real-time, premium |

---

## Common Patterns

### Simple API Response Caching

```nginx
# Nginx reverse proxy caching
location /api/ {
    proxy_cache api_cache;
    proxy_cache_valid 200 10m;
    proxy_cache_valid 404 1m;
    proxy_cache_key "$scheme$request_method$host$request_uri";
    add_header X-Cache-Status $upstream_cache_status;
    proxy_pass http://backend;
}
```

### Database Query Caching

```python
# Redis cache-aside
import redis

cache = redis.Redis()

def get_user(user_id):
    key = f"user:{user_id}"
    cached = cache.get(key)
    if cached:
        return json.loads(cached)

    user = db.query(User).get(user_id)
    cache.setex(key, 3600, json.dumps(user.to_dict()))
    return user.to_dict()
```

### GraphQL Normalized Caching

```javascript
// Apollo Client
import { InMemoryCache } from '@apollo/client';

const cache = new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        user: {
          read(_, { args, toReference }) {
            return toReference({
              __typename: 'User',
              id: args.id
            });
          }
        }
      }
    }
  }
});
```

### N+1 Prevention with DataLoader

```javascript
// GraphQL resolver with batching
const postLoader = new DataLoader(async (userIds) => {
  const posts = await db.query(
    `SELECT * FROM posts WHERE user_id IN (${userIds})`
  );
  return userIds.map(id =>
    posts.filter(p => p.user_id === id)
  );
});

const resolvers = {
  User: {
    posts: (user) => postLoader.load(user.id)
  }
};
```

### HTTP Cache Headers

```javascript
// Express.js example
app.get('/api/products/:id', (req, res) => {
  const product = getProduct(req.params.id);

  // Cache for 1 hour, public cache
  res.set('Cache-Control', 'max-age=3600, public');

  // Add ETag for validation
  res.set('ETag', `"${product.version}"`);

  // Check If-None-Match (ETag)
  if (req.get('If-None-Match') === `"${product.version}"`) {
    return res.status(304).end();
  }

  res.json(product);
});
```

---

## Implementation Checklist

### Phase 1: Measure

- [ ] Identify slow endpoints
- [ ] Analyze access patterns
- [ ] Measure current latency
- [ ] Baseline database load

### Phase 2: Cache Selection

- [ ] Choose HTTP proxy (Nginx/Varnish/HAProxy)
- [ ] Choose application cache (Redis/Memcached)
- [ ] Plan cache invalidation strategy
- [ ] Design cache key structure

### Phase 3: Implementation

- [ ] Add Cache-Control headers to responses
- [ ] Implement cache store (Redis/Memcached)
- [ ] Deploy HTTP proxy
- [ ] Add monitoring/alerting

### Phase 4: Validation

- [ ] Verify cache hit ratios (target: 50-80%)
- [ ] Measure latency improvements
- [ ] Monitor memory usage
- [ ] Test cache invalidation

---

## Performance Targets

| Metric | Target | Notes |
|--------|--------|-------|
| Cache hit ratio | 50-80% | Depends on workload |
| Latency (cached) | <50ms | sub-100ms acceptable |
| Cache memory | <30% of heap | Prevent evictions |
| Hit/Miss ratio | >2:1 | More hits than misses |

---

## Monitoring Essentials

```python
# Redis cache metrics
KEYS = redis.dbsize()  # Total keys
HIT_RATIO = hits / (hits + misses)  # Hit ratio
AVG_LATENCY = sum(latencies) / len(latencies)  # Average latency
MEM_USED = redis.info()['used_memory_human']  # Memory usage
```

```nginx
# Nginx cache metrics
upstream_cache_status  # HIT, MISS, EXPIRED, etc.
X-Cache-Status header  # Add to responses
cache_hits / (cache_hits + cache_misses)  # Hit ratio
```

```javascript
// Apollo Client cache metrics
cache.stats()  // Size, entries, memory
cache.evict()  // Force eviction
cache.reset()  // Clear entire cache
```

---

## Architecture Patterns

### Single-Server (Development)

```
[Client] → [Nginx + proxy_cache] → [App + Redis] → [Database]
```

### Multi-Region (Production)

```
[Client]
  ↓
[Cloudflare] (global edge cache)
  ↓
[Regional Nginx] (reverse proxy cache)
  ↓
[Kong API Gateway] (with caching plugin)
  ↓
[Redis Cluster] (distributed cache)
  ↓
[Database Replica]
```

### Kubernetes (Cloud-Native)

```
[Ingress Controller] (Nginx/HAProxy with cache)
  ↓
[Service Mesh] (Istio/Linkerd with pooling)
  ↓
[Application Pods]
  ↓
[Redis StatefulSet]
  ↓
[Database]
```

---

## Cost Comparison

| Solution | Cost | Scale |
|----------|------|-------|
| Nginx | Free | Unlimited |
| Redis | Free (self-hosted) | Terabytes |
| Cloudflare | $20+/mo | Global |
| AWS API Gateway | $0.035 per million requests | Automatic scaling |
| Varnish | Free (enterprise support paid) | Unlimited |

---

## Common Pitfalls

1. **Cache invalidation too aggressive**: Defeats purpose, reduces hit ratio
2. **Not monitoring cache metrics**: Can't see if it's working
3. **Caching non-cacheable data**: User-specific data in shared cache
4. **Not handling cache misses**: Thundering herd on miss
5. **Missing error handling**: Failed cache should fallback to DB
6. **Not versioning cache keys**: Breaking changes affect cache
7. **Over-caching**: Memory bloat, unnecessary TTL extensions
8. **Not testing invalidation**: Stale data in production

---

## Tools & Libraries

| Language | In-Memory | HTTP Proxy | GraphQL |
|----------|-----------|-----------|---------|
| Node.js | Redis client, ioredis | N/A (use Nginx) | Apollo Client |
| Python | redis-py | N/A (use Nginx) | Strawberry GSS |
| Java | Jedis, Lettuce | N/A (use Nginx) | graphql-java |
| Go | go-redis | N/A (use Nginx) | gqlgen |
| PHP | Predis | N/A (use Nginx) | GraphQL-Core |

---

## Learning Resources

### HTTP Caching
- [MDN HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)
- [Nginx Caching Guide](https://nginx.org/en/docs/)
- [Varnish Docs](https://varnish-cache.org/)

### GraphQL Caching
- [Apollo Caching Documentation](https://www.apollographql.com/docs/apollo-client/caching/overview/)
- [Relay Cache Guide](https://relay.dev/docs/guides/caching/)

### Redis
- [Redis Documentation](https://redis.io/docs/)
- [Redis Stack](https://redis.io/stack/) (extended features)

### Service Mesh
- [Istio Caching](https://istio.io/)
- [Linkerd Architecture](https://linkerd.io/)

---

## When to Use Each

### Varnish
- Complex site with many cache rules
- High-traffic e-commerce
- Need edge-side includes
- Multi-level caching

### Nginx
- General web caching
- WordPress and LAMP stacks
- Simple, fast deployments
- Low operational overhead

### Redis
- Need to cache complex data
- Session storage
- Real-time leaderboards
- Distributed caching

### Memcached
- Pure speed is goal
- Simple string caching
- No persistence needed
- Stateless applications

### Kong
- Kubernetes/cloud-native
- API management focus
- Plugin extensibility needed
- Microservices architecture

### Cloudflare
- Need global CDN
- Edge compute (Workers)
- DDoS protection
- Serverless caching

### DataLoader
- GraphQL resolver optimization
- N+1 query prevention
- Batch request processing
- Any request-scoped batching

---

## References

- Complete Guide: `/CACHING_SOLUTIONS_COMPREHENSIVE.md`
- Varnish: https://varnish-cache.org/
- Nginx: https://nginx.org/
- Redis: https://redis.io/
- Kong: https://konghq.com/
- Apollo: https://www.apollographql.com/
- Cloudflare: https://www.cloudflare.com/
- DataLoader: https://github.com/graphql/dataloader

