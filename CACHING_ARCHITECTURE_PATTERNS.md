# Caching Architecture Patterns & Decision Framework

Comprehensive guide to caching architecture patterns, design decisions, and implementation strategies for production systems.

---

## Table of Contents

1. [Multi-Tier Caching Architectures](#multi-tier-caching-architectures)
2. [Caching Patterns](#caching-patterns)
3. [Decision Framework](#decision-framework)
4. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
5. [Monitoring & Operations](#monitoring--operations)
6. [Migration Strategies](#migration-strategies)

---

## Multi-Tier Caching Architectures

### Three-Tier Cache Model (Standard 2025)

```
┌─────────────────────────────────────────┐
│ Client (Browser)                         │
│ ├─ HTTP Cache Headers                   │
│ └─ Local Storage / SessionStorage        │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│ CDN / Edge (Cloudflare, Fastly, etc.)   │
│ ├─ Geographic distribution              │
│ └─ Cache-Control: s-maxage              │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│ L1 - In-Memory (Redis / Valkey)          │
│ ├─ Per-application instance              │
│ ├─ Sub-millisecond latency              │
│ └─ Hot data (session, computed results) │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│ L2 - Distributed (Memcached / DynamoDB) │
│ ├─ Shared across app instances         │
│ ├─ 10-50ms latency                     │
│ └─ Larger datasets                      │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│ L3 - Persistent (DB / Vector DB)        │
│ ├─ Source of truth                      │
│ ├─ Pinecone / Weaviate for embeddings  │
│ └─ 100-500ms+ latency                  │
└──────────────┬──────────────────────────┘
               │
        Origin Database
```

**Efficiency Gain**: 40% improvement with predictive cache warming and stampede protection

---

### Two-Tier Caching (Simpler Deployments)

```
Application Instance
├─ L1: FusionCache / HybridCache (in-memory)
└─ L2: Shared Redis / Memcached
    └─ Distributed across nodes
```

**Best For**: Microservices, medium-scale applications

---

### Single-Layer Caching (Minimal)

```
Application
└─ Redis / Memcached (all caching needs)
```

**Best For**: Small applications, simple caching, embedded systems

---

## Caching Patterns

### Cache-Aside (Lazy Loading)
```
1. Check cache for data
2. If miss: Load from database
3. Store in cache
4. Return to client

Code pattern:
    data = cache.get(key)
    if not data:
        data = database.fetch(key)
        cache.set(key, data, ttl)
    return data
```

**Advantages**:
- Simple implementation
- Doesn't corrupt data (DB is source of truth)
- Works with any cache backend

**Disadvantages**:
- Cache misses cause slow requests
- Stale data possible without explicit invalidation

**Best For**: Read-heavy workloads, infrequent updates

---

### Write-Through
```
1. Write to cache first
2. Write to database
3. Return to client

Code pattern:
    cache.set(key, data)
    database.save(key, data)
    return response
```

**Advantages**:
- Cache always consistent with database
- No stale data window

**Disadvantages**:
- Slower writes (wait for both cache + DB)
- Cache miss on startup means extra DB writes

**Best For**: Critical data requiring strong consistency

---

### Write-Behind (Write-Through with Async DB)
```
1. Write to cache
2. Immediately return to client
3. Asynchronously write to database

Code pattern:
    cache.set(key, data)
    queue.enqueue(write_to_db_task, key, data)
    return response
```

**Advantages**:
- Fast writes (return immediately)
- Database writes batched/optimized

**Disadvantages**:
- Complex error handling
- Data loss if cache fails before DB write
- Eventual consistency model

**Best For**: Non-critical data, high-write scenarios, analytics

---

### Refresh-Ahead (Predictive)
```
1. Detect access patterns
2. Refresh cache before expiry
3. Reduce cache misses

Code pattern:
    # Background job monitors hit/miss rates
    # Predictively refreshes hot keys 80% through TTL
    for key in hot_keys:
        if key.age > ttl * 0.8:
            cache.refresh(key)
```

**Advantages**:
- Eliminates cache miss latency
- Improves user experience
- 40% efficiency gains reported

**Disadvantages**:
- Requires monitoring/AI
- Extra database load
- Complex implementation

**Best For**: High-traffic applications, predictable access patterns

---

### Cache Invalidation

#### Time-Based (TTL)
```
Cache-Control: max-age=3600  # 1 hour
```
- Simple, no coordination needed
- Risk: Stale data up to TTL duration
- Best for: Non-critical data with acceptable staleness window

#### Event-Based
```
# On data update
cache.delete(key)
cache.delete_pattern("user:*")  # Prefix invalidation
```
- Immediate consistency
- Complex coordination
- Best for: Critical data, financial systems

#### Tag-Based (Varnish pattern)
```
# Cache with tags
cache.set(key, data, tags=['user:123', 'profile'])

# On user profile update
cache.invalidate_by_tag('user:123')  # Clears all tagged items
```
- Flexible invalidation scope
- Widely supported (Varnish, Redis)
- Best for: Complex dependency management

#### Conditional Validation
```
# ETag validation
If-None-Match: "hash123"  # Browser asks: still current?
304 Not Modified          # Server: yes, use cache
```
- Reduces bandwidth (no full response)
- HTTP standard
- Best for: Static assets, API responses

---

## Decision Framework

### Decision Tree: Choosing Your Caching Layer

```
START: Need to cache data?
│
├─ Simple static content?
│  └─► CDN (Cloudflare, Fastly)
│
├─ Session/User-specific?
│  ├─ High read rate?
│  │  └─► Redis/Valkey (L1)
│  └─ Consistency critical?
│     └─► Write-Through pattern
│
├─ API responses?
│  ├─ Cloud-native?
│  │  └─► ElastiCache/Memorystore
│  ├─ Multiple app instances?
│  │  └─► Redis L1 + Memcached L2
│  └─ Need resilience?
│     └─► FusionCache (L1+L2 hybrid)
│
├─ Database query results?
│  ├─ Millions of concurrent users?
│  │  └─► Aerospike + Redis
│  ├─ Standard scale?
│  │  └─► Redis + L2 distributed
│  └─ Read-heavy analytics?
│     └─► Materialized views + Redis
│
├─ AI/ML embeddings?
│  ├─ Semantic search?
│  │  └─► Pinecone (managed) or Weaviate (self-hosted)
│  ├─ RAG system?
│  │  └─► Vector DB + Redis L1
│  └─ Fine-tuning?
│     └─► FSx for Lustre (high throughput)
│
└─ Rate limiting / Leaderboards?
   └─► Redis (purpose-built for these)
```

---

### Capability Matrix

| Requirement | Best System | Alternative |
|-------------|------------|-------------|
| **Sub-millisecond latency** | Redis, Valkey | Dragonfly |
| **Millions of concurrent users** | Aerospike | Redis cluster |
| **Write-heavy workload** | Dragonfly, Aerospike | Valkey |
| **Multi-protocol** | Pogocache | Redis (single protocol) |
| **Distributed, highly scalable** | Aerospike | Redis cluster + Memcached |
| **Managed service** | ElastiCache, Memorystore | Self-hosted Redis |
| **Open-source, no licensing** | Valkey, Dragonfly | Pogocache |
| **Embeddings/vectors** | Pinecone (managed) | Weaviate (OSS) |
| **Edge caching** | Cloudflare, Fastly | Varnish (self-hosted) |
| **Application-level hybrid** | FusionCache (.NET) | Custom implementation |

---

### Scale-Based Recommendations

#### Small Scale (Single Server)
- **In-Memory**: Redis or Memcached
- **CDN**: Cloudflare Free/Pro
- **Pattern**: Cache-Aside
- **TTL**: 1 hour default

#### Medium Scale (2-10 servers)
- **L1**: Redis on each instance (isolated)
- **L2**: Shared Memcached cluster
- **CDN**: Fastly or Cloudflare
- **Pattern**: Cache-Aside + TTL
- **Tools**: Health checks, monitoring

#### Large Scale (100+ servers)
- **L1**: FusionCache (.NET) or custom (stampede protection)
- **L2**: Redis cluster (sharded)
- **L3**: Memcached (for larger datasets)
- **CDN**: Akamai or Fastly
- **Pattern**: Refresh-Ahead + predictive caching
- **Tools**: OpenTelemetry, automated warming

#### Enterprise Scale (1000+ servers, multiple regions)
- **L1**: Distributed Redis cluster + Dragonfly for writes
- **L2**: Aerospike (hybrid memory, linear scaling)
- **L3**: Vector DB for embeddings
- **CDN**: Multi-CDN (Cloudflare + Akamai)
- **Geo**: Regional replication, cross-datacenter sync
- **Pattern**: Refresh-Ahead + event-based invalidation
- **Observability**: Full tracing, predictive models

---

## Anti-Patterns to Avoid

### Cache Stampede (Thundering Herd)
**Problem**: Multiple requests hit cache miss simultaneously, overload origin.

**Solution**:
```
# FusionCache: Built-in stampede protection
# Redis: Implement lock-based refresh
lock = redis.lock(f"refresh:{key}")
if lock.acquire(timeout=5):
    try:
        data = database.fetch(key)
        cache.set(key, data)
    finally:
        lock.release()
else:
    # Wait for other thread to refresh, then read
    data = cache.get(key)
```

---

### Cache Invalidation Complexity
**Problem**: "There are only two hard things in Computer Science: cache invalidation and naming things."

**Solution**:
- Use **TTL aggressively** (1-hour default)
- Implement **tag-based invalidation** for related items
- Use **conditional validation** (ETags) for HTTP
- Monitor **staleness** as a metric

---

### Storing Secrets in Cache
**Problem**: API keys, passwords leaked if cache compromised.

**Solution**:
```
# Good: Cache computed results, not secrets
Cache: {"user_id": 123, "profile": {...}}

# Bad: Never cache
DO NOT cache: auth_token, password_hash, api_key

# When needed: Short-lived, encrypted, separate storage
cache.set("auth_token", token, ttl=5*60)  # 5 minutes max
```

---

### Unbounded Cache Growth
**Problem**: Cache fills with stale data, memory exhausted.

**Solution**:
```
# Always set TTL
cache.set(key, value, ttl=3600)

# Use eviction policy
cache.config_set('maxmemory-policy', 'allkeys-lru')

# Monitor size
redis-cli info memory
# Watch: used_memory, used_memory_peak, evicted_keys
```

---

### Ignoring Cache Coherency
**Problem**: Different servers see different versions (split-brain).

**Solution**:
- **Single source of truth**: Database
- **Cache as view**: Invalidate on any write
- **Eventual consistency model**: Document TTL
- **Synchronization**: Use backplane (FusionCache), broadcast events

---

## Monitoring & Operations

### Key Metrics to Track

#### Cache Performance
```
Hit Rate = Cache Hits / (Cache Hits + Cache Misses)
    Target: >90% for hot data
    Alert: <70% indicates thrashing

Miss Rate = 1 - Hit Rate
    Monitor miss spike patterns

Eviction Rate = Keys evicted / Time
    High eviction = cache too small

Response Time (Cache) = <1ms (target)
Response Time (Origin) = Measure separately
    Gap = Cache efficiency
```

#### Memory Management
```
Memory Usage = Used / Total
    Alert: >80% fullness

Keys per Instance = Total keys / instances
    Monitor for uneven distribution

TTL Distribution = Histogram of remaining TTL
    Alert: Many keys expiring simultaneously
```

#### Business Metrics
```
Cache Efficiency = 1 - (Origin Load / Expected Load)
    Target: 70%+ reduction

Staleness = Cached data age / TTL
    Document acceptable staleness

Cost per Request = Cache cost / requests
    Compare vs. origin load cost
```

### Monitoring Tools

**Redis/Valkey Native**:
```bash
redis-cli info stats     # Hits, misses, evictions
redis-cli info memory    # Memory usage, evictions
redis-cli --latency      # Monitor latency
redis-cli --bigkeys      # Find large items
```

**CloudFlare**:
- Caching dashboard: Cache hit ratio, purges
- Real-time analytics
- Cache behavior logs

**Application Level**:
- OpenTelemetry (FusionCache, .NET)
- Prometheus metrics
- Custom instrumentation

---

## Migration Strategies

### From No Caching to Redis

#### Phase 1: Setup (Week 1)
```bash
# Deploy Redis cluster
docker run -d -p 6379:6379 redis:7-alpine

# Basic monitoring
redis-cli ping
redis-cli monitor  # Watch queries
```

#### Phase 2: Identify Hot Paths (Week 1-2)
```python
# Add logging to identify cacheable patterns
for endpoint in slow_endpoints:
    if endpoint.read_ratio > 0.8:
        candidates.append(endpoint)

# Profile database queries
slow_queries = database.explain_analyze(query)
if slow_queries.count > 100/sec:
    cache_this = True
```

#### Phase 3: Implement Selectively (Week 2-3)
```python
# Start with highest-impact queries
def get_user_profile(user_id):
    cache_key = f"profile:{user_id}"

    # Try cache
    profile = redis.get(cache_key)
    if profile:
        return json.loads(profile)

    # Cache miss
    profile = database.query("SELECT * FROM users WHERE id = ?", user_id)
    redis.setex(cache_key, 3600, json.dumps(profile))
    return profile
```

#### Phase 4: Monitor & Optimize (Week 3+)
```python
# Track metrics
cache_hit_rate = hits / (hits + misses)
print(f"Hit rate: {cache_hit_rate:.1%}")

# Adjust TTLs based on update frequency
if cache_hit_rate < 0.7:
    ttl = 1800  # Reduce TTL if too much staleness
elif cache_hit_rate > 0.95:
    ttl = 7200  # Increase if over-cached
```

---

### From Single-Tier to Multi-Tier

#### Before: Simple Redis
```
Application → Redis → Database
```

#### Migration: Add L2 Layer

```
1. Deploy Memcached cluster
   docker run -d -p 11211:11211 memcached

2. Update cache pattern
   def get_data(key):
       # L1: Redis (fast)
       data = redis.get(key)
       if data:
           return data

       # L2: Memcached (slower but distributed)
       data = memcached.get(key)
       if data:
           redis.set(key, data, 300)  # Repopulate L1
           return data

       # L3: Database
       data = db.fetch(key)
       memcached.set(key, data, 3600)  # L2
       redis.set(key, data, 300)       # L1
       return data

3. Monitor hit rates per layer
   redis_hits, memcached_hits, db_hits
   Target: 70% redis, 20% memcached, 10% db
```

---

### From Open-Source to Managed (ElastiCache Migration)

#### Phase 1: Parallel Deployment
```bash
# Keep existing Redis running
# Deploy ElastiCache cluster in VPC
# Test failover scenarios
```

#### Phase 2: Gradual Traffic Shift
```bash
# 10% → ElastiCache, 90% → On-premises Redis
# Monitor metrics for 24 hours
# Increase: 50/50, then 100% ElastiCache
```

#### Phase 3: Validation
```python
# Compare responses between both caches
def get_with_validation(key):
    old_value = old_redis.get(key)
    new_value = elasticache.get(key)

    assert old_value == new_value, "Cache divergence!"

    return new_value
```

#### Phase 4: Decommission Old Infrastructure
```bash
# After 2 weeks clean operation
# Stop old Redis instances
# Reallocate compute resources
```

---

## Performance Tuning Checklist

### Redis/Valkey
- [ ] Enable pipelining for batch operations
- [ ] Use connection pooling
- [ ] Monitor slow query log: `slowlog get 10`
- [ ] Adjust `timeout` and `tcp-backlog`
- [ ] Enable `appendonly no` if data loss acceptable
- [ ] Set `maxmemory-policy` (eviction strategy)
- [ ] Use `--lru-samples 10` for better LRU accuracy
- [ ] Enable replication for HA
- [ ] Monitor `connected_clients`, `rejected_connections`

### Application Layer
- [ ] Implement cache stampede protection
- [ ] Use async/await for non-blocking cache access
- [ ] Batch related cache operations
- [ ] Implement circuit breakers for cache failures
- [ ] Monitor cache operation latency (p50, p99)
- [ ] Use connection pooling (min 10, max 100 connections)

### CDN/Edge
- [ ] Set appropriate `Cache-Control: max-age`
- [ ] Use `s-maxage` for edge-specific TTL
- [ ] Implement cache key rules for variants
- [ ] Use `stale-while-revalidate` for resilience
- [ ] Monitor cache hit ratio (target >85%)
- [ ] Set up cache purging strategy

---

## Conclusion

Effective caching requires:
1. **Right tool for workload** (Redis vs. Memcached vs. Aerospike)
2. **Appropriate pattern** (Cache-Aside, Write-Through, Refresh-Ahead)
3. **Multi-tier architecture** for scale (L1+L2+L3)
4. **Strong monitoring** (hit rate, latency, memory)
5. **Careful invalidation strategy** (TTL + event-based)
6. **Graceful degradation** (cache failures shouldn't break app)

Performance gains of **40-80%** are typical when caching is implemented correctly.
