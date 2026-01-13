# Comprehensive Web Caching, HTTP Caching, and API Caching Solutions Guide

A thorough research guide covering production-ready caching tools and strategies for HTTP, REST APIs, GraphQL, and microservices architectures.

**Last Updated**: January 2026

---

## Table of Contents

1. [HTTP/Reverse Proxy Caching](#httpreverse-proxy-caching)
2. [API Gateway Caching](#api-gateway-caching)
3. [In-Memory Caching Stores](#in-memory-caching-stores)
4. [GraphQL-Specific Caching](#graphql-specific-caching)
5. [Service Mesh Caching](#service-mesh-caching)
6. [CDN and Edge Caching](#cdn-and-edge-caching)
7. [Database and Query Caching](#database-and-query-caching)
8. [REST API Caching Strategies](#rest-api-caching-strategies)
9. [Comparison Matrix](#comparison-matrix)

---

## HTTP/Reverse Proxy Caching

### Varnish Cache

**Type**: Dedicated HTTP accelerator and reverse proxy caching engine

**Key Features**:
- Custom VCL (Varnish Configuration Language) for complex caching rules
- Edge-Side Includes (ESI) for partial dynamic content caching
- Real-time content purging and invalidation
- Built-in DDoS protection
- Anonymous header stripping
- GZIP compression
- HTTP/2 support
- Custom memory management with threading

**Strengths**:
- Extremely flexible caching logic via VCL
- High throughput for cached content
- Excellent for complex, heterogeneous cache rules
- ESI enables partial dynamic page caching without full generation
- Cache hit rates up to 1000x speedup over non-cached origins (claims)

**Weaknesses**:
- Unix-only (no native Windows support)
- Limited SSL/HTTPS support (requires Nginx/HAProxy in front)
- VCL requires expertise to optimize
- More complex setup than simpler alternatives
- Single-threaded core (though with multiple workers)

**Performance Benchmarks**:
- WordPress scenario: Achieves ~26,440 requests/sec with ~100ms average response time
- Cache hit scenarios show 300-1000x speedup per official claims
- Raw throughput slightly lower than Nginx but dominates for dynamic content

**Best For**:
- E-commerce sites with complex caching rules
- Media sites with heterogeneous content
- High-traffic applications requiring fine-tuned cache control
- WordPress with intricate invalidation requirements
- Hybrid static/dynamic content serving

**Documentation**: https://varnish-cache.org/docs/

---

### Nginx (proxy_cache and FastCGI cache)

**Type**: Lightweight reverse proxy with integrated caching

**Key Features**:
- `proxy_cache` directive for HTTP reverse proxy caching
- `fastcgi_cache` for FastCGI backend caching
- ngx_cache_purge module (community) for dynamic purging
- Asynchronous, non-blocking event-driven architecture
- Master-worker process model for concurrency
- Full SSL/HTTPS support with certificate management
- HTTP/2 and HTTP/3 (QUIC) support
- Gzip, Brotli compression
- Rate limiting with `limit_req`

**Strengths**:
- Extremely lightweight (~1MB memory footprint vs. Varnish's heavier model)
- High concurrency through event-driven architecture
- Raw throughput often exceeds Varnish (27,170 req/s vs. 26,440)
- Simple, declarative configuration format
- Excellent for static content and simple caching
- Lower operational overhead
- Works natively on all platforms

**Weaknesses**:
- Limited built-in purging in open-source version (requires nginx-plus or third-party modules)
- Less flexible than VCL for complex conditional caching
- No ESI support natively
- Simpler caching model may need external tools for complex scenarios

**Performance Benchmarks**:
- Static content: 27,170 requests/sec, 82ms avg response
- WordPress FastCGI: Up to 10x speedup over non-cached
- Superior concurrency under high load
- Lower memory overhead than alternatives

**Best For**:
- General-purpose web caching and reverse proxy
- WordPress and other LAMP/LEMP stacks
- Static file serving with caching
- Situations requiring high concurrency and minimal overhead
- Single-server or simple multi-server architectures
- Mobile and low-resource deployments

**Configuration Example**:
```nginx
http {
    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m
                      max_size=1g inactive=60m use_temp_path=off;

    server {
        location / {
            proxy_cache my_cache;
            proxy_cache_valid 200 10m;
            proxy_cache_valid 404 1m;
            add_header X-Cache-Status $upstream_cache_status;
            proxy_pass http://backend;
        }
    }
}
```

**Documentation**: https://nginx.org/en/docs/

---

### Squid

**Type**: Mature forward/reverse proxy with advanced caching

**Key Features**:
- Advanced Access Control Lists (ACLs)
- Hierarchical caching for proxy chains
- Digest authentication
- SSL/TLS termination
- Memory and disk-based caching
- SMP (Symmetric Multi-Processing)
- Bandwidth throttling
- ICP (Internet Cache Protocol) for cache coordination

**Strengths**:
- Highly mature codebase (30+ years)
- Excellent for traditional proxy caching scenarios
- Advanced ACL and filtering capabilities
- Effective bandwidth optimization
- Good for corporate proxies and cache hierarchies
- Memory and disk storage combinations

**Weaknesses**:
- Less modern than Nginx/Varnish for web applications
- Complex configuration for basic setups
- Not optimized for modern API/microservices patterns
- Lower throughput than modern alternatives
- Steeper learning curve for setup and tuning

**Best For**:
- Corporate proxy caches and firewalls
- ISP-level caching infrastructure
- Traditional forward proxy scenarios
- Bandwidth-constrained networks
- Legacy infrastructure modernization

**Documentation**: http://www.squid-cache.org/

---

### HAProxy

**Type**: Load balancer with built-in HTTP caching capabilities

**Key Features**:
- In-memory HTTP response caching (relatively new)
- Layer 4/7 load balancing algorithms
- Stick tables for session persistence and rate limiting
- Health checking and automatic failover
- SSL/TLS termination
- Request rate limiting
- Header manipulation and rewriting

**Caching Capabilities**:
- Configuration:
  ```
  cache mycache
      total-max-size 4095  # MB
      max-age 30           # seconds
      max-object-size 100  # KB

  backend servers
      http-request cache-use mycache
      http-response cache-store mycache if { method GET }
  ```
- Short TTL caching (5-30 seconds typical)
- `X-Cache-Status: HIT/MISS` headers
- ACL-based caching decisions
- Compression alongside caching

**Strengths**:
- Excellent load balancing with integrated caching
- Very lightweight and performant
- Easy configuration for basic load balancing
- Good for API gateway scenarios
- Stick tables for distributed caching state

**Weaknesses**:
- Caching capabilities more limited than Varnish/Nginx
- Best for simple, short-TTL caching
- Not ideal for full-page caching complexity
- Stick tables are for persistence, not content caching

**Best For**:
- API gateways with load balancing
- Microservice layer 7 routing with light caching
- Semi-static content (news feeds, API responses)
- Short-TTL API response caching
- Load balanced deployments requiring session persistence

**Documentation**: https://www.haproxy.org/

---

## API Gateway Caching

### Kong

**Type**: Open-source API gateway with plugin ecosystem

**Key Features**:
- **proxy-cache plugin**: HTTP response caching
- **redis plugin**: Integration with Redis for distributed caching
- Semantic caching for AI/LLM applications
- Dynamic configuration without restart
- Rate limiting and quota management
- Authentication/authorization
- Request/response transformation
- Clustering and horizontal scaling

**Caching Architecture**:
```
Request → Kong Gateway → Cache Lookup → Hit: Return cached response
                             ↓ Miss
                        Upstream Service → Cache Store → Return response
```

**Strengths**:
- Highly extensible plugin architecture
- Perfect for cloud-native and Kubernetes deployments
- Excellent for microservices API management
- AI/semantic caching capabilities
- Active community and enterprise support
- Dynamic reload without restart

**Weaknesses**:
- Caching via plugin (not built-in)
- Requires plugin expertise for advanced scenarios
- Added operational complexity

**Configuration Example**:
```yaml
http {
    lua_shared_dict kong_cache 10m;

    server {
        location / {
            access_by_lua_block {
                local cache_key = ngx.var.request_uri
                local cached = ngx.shared.kong_cache:get(cache_key)
                if cached then
                    return ngx.say(cached)
                end
            }

            proxy_pass http://upstream;
        }
    }
}
```

**Best For**:
- Cloud-native and Kubernetes environments
- Microservice architectures
- High-volume API management
- AI/LLM applications with semantic caching
- Organizations needing plugin extensibility
- Multi-tenant API platforms

**Documentation**: https://docs.konghq.com/

---

### AWS API Gateway

**Type**: Fully managed API gateway service

**Key Features**:
- Built-in response caching for REST and HTTP APIs
- Configurable TTL per method/resource
- Stage-level cache settings
- CloudWatch metrics for cache performance
- Cache invalidation support
- Integration with AWS Lambda, RDS, SNS, etc.
- Request transformation and validation

**Caching Mechanism**:
- **Cache Size**: 0.5-500GB depending on tier
- **Cache Settings**: Per method or stage level
- **Cache Key**: URL + HTTP method + response headers
- **TTL Range**: 300 seconds (5 min) to 3600 seconds (1 hour)

**Cost**: Scale with cache size and region

**Strengths**:
- Seamless AWS integration
- Fully managed (no infrastructure)
- Simple setup with no code changes
- Automatic failover and scaling
- CloudWatch integration for monitoring
- Can absorb traffic spikes effectively
- Handles millions of requests/day

**Weaknesses**:
- Limited to API Gateway responses (not full HTTP caching)
- Costs scale with cache size
- TTL limited to 1 hour maximum
- Less flexible than self-hosted solutions
- Vendor lock-in

**Best For**:
- AWS-native architectures
- REST APIs with read-heavy patterns
- Traffic spike absorption
- Microservices with AWS backend
- Organizations valuing operational simplicity
- APIs with repetitive GET requests

**Typical Savings**: 50-80% reduction in backend calls for read-heavy APIs

**Documentation**: https://docs.aws.amazon.com/apigateway/

---

### Azure API Management

**Type**: Enterprise API management platform

**Key Features**:
- Built-in response caching with TTL
- Policy-based caching configuration
- Backend caching integration
- Cache invalidation
- Request/response transformation
- Rate limiting and quotas
- Developer portal and documentation

**Caching Policies**:
```xml
<cache-store duration="3600" />
<cache-lookup />
```

**Strengths**:
- Native Azure ecosystem integration
- Enterprise-grade policy engine
- Good for regulated industries
- Full API lifecycle management
- Developer portal included

**Weaknesses**:
- Limited caching flexibility vs. dedicated proxies
- Higher cost for enterprise features
- Less detailed caching insights

**Best For**:
- Azure-native organizations
- Enterprise API governance
- Regulated industries
- Organizations with existing Azure investments

**Documentation**: https://learn.microsoft.com/en-us/azure/api-management/

---

### Traefik

**Type**: Modern reverse proxy and API gateway

**Features**:
- Dynamic routing for containers/Kubernetes
- Let's Encrypt SSL automation
- Middleware ecosystem
- WebSocket support
- API dashboard

**Caching Note**: No native HTTP caching; requires middleware or Redis integration

**Best For**:
- Container orchestration (Docker, Kubernetes)
- Dynamic service discovery
- Simple edge routing
- Not caching-focused workloads

**Documentation**: https://doc.traefik.io/

---

### Gravitee

**Type**: Open-source API platform

**Features**:
- HTTP cache policy
- Plugin-based extensibility
- Full API lifecycle management
- Developer portal
- Analytics and monitoring

**Strengths**:
- Flexible policy-driven approach
- Multi-cloud deployment
- Strong policy ecosystem

**Best For**:
- Hybrid and multi-cloud deployments
- Policy-driven API management
- Organizations requiring fine-grained control

**Documentation**: https://documentation.gravitee.io/

---

## In-Memory Caching Stores

### Redis

**Type**: Advanced in-memory data structure store

**Key Characteristics**:
- **Single-threaded** with non-blocking I/O (per shard)
- **Data Structures**: Strings, Lists, Sets, Sorted Sets, Hashes, Geospatial, Bitmaps, HyperLogLog, Streams
- **Key/Value Limits**: Keys up to 512MB, values up to 512MB
- **Persistence**: RDB snapshots and AOF (Append-Only File) logs
- **Eviction Policies**: 6 strategies (LRU, LFU, volatile-only variants)
- **Replication**: Master-replica with partial resync
- **Transactions**: MULTI/EXEC with watch
- **Pub/Sub**: Channel-based messaging
- **Lua Scripting**: Atomic script execution
- **Cluster Mode**: Horizontal scaling with hash slots
- **TTL**: Per-key expiration with jitter support

**Performance**:
- Sub-millisecond latency for reads/writes
- 100,000+ operations/second per instance (workload-dependent)
- Non-blocking architecture enables high concurrency
- Clustering for horizontal scaling

**Memory Overhead**: Typically 10-25% for metadata (lower with modern allocators)

**API Caching Examples**:

```python
# Cache-aside pattern
import redis

r = redis.Redis(host='localhost')
cache_key = f"user:{user_id}:profile"

# Try cache first
cached = r.get(cache_key)
if cached:
    return json.loads(cached)

# Cache miss: fetch from DB
user = db.query(User).filter_by(id=user_id).first()

# Store with TTL (1 hour)
r.setex(cache_key, 3600, json.dumps(user.to_dict()))

return user.to_dict()
```

```python
# Session caching
r.hset(f"session:{session_id}", mapping={
    "user_id": user_id,
    "role": role,
    "login_time": timestamp
})
r.expire(f"session:{session_id}", 1800)  # 30 min TTL
```

```python
# Distributed rate limiting with counters
def rate_limit(user_id, max_requests=100, window=3600):
    key = f"ratelimit:{user_id}"
    count = r.incr(key)
    if count == 1:
        r.expire(key, window)
    return count <= max_requests
```

**Strengths**:
- Rich data structures reduce serialization overhead
- Persistence ensures data isn't lost
- Pub/Sub for real-time updates
- Lua scripting for atomic operations
- Excellent for complex data patterns
- Strong replication and clustering
- Eviction policies provide flexible memory management
- Transaction support with watch for optimistic locking

**Weaknesses**:
- Single-threaded per shard (though cluster helps)
- Persistence adds latency (RDB snapshots)
- Replication lag in distributed setups
- Memory-expensive for large datasets
- Higher operational complexity than Memcached

**Best For**:
- Complex caching with advanced data structures
- Session storage and state management
- Real-time leaderboards and analytics
- API response caching with relationships
- Distributed caching with replication
- Cache warming and preloading
- Any scenario requiring persistence or advanced features

**Cluster Architecture** (for horizontal scaling):
```
┌──────────────┐
│ Application  │
└──────┬───────┘
       │
  ┌────┴────┬─────────┬──────────┐
  ↓         ↓         ↓          ↓
[Node 1] [Node 2] [Node 3] ... [Node N]
Redis Cluster - Consistent hashing with 16,384 hash slots
```

**Documentation**: https://redis.io/

---

### Memcached

**Type**: Lightweight in-memory caching system

**Key Characteristics**:
- **Multi-threaded** leveraging multiple CPU cores
- **Data**: Simple strings only (key-value pairs)
- **Key/Value Limits**: Keys up to 250 bytes (typically), values up to 1MB (configurable to 128MB+)
- **Architecture**: Slab allocator for memory management
- **No Persistence**: Data lost on restart
- **Eviction**: LRU (Least Recently Used) only
- **TTL**: Per-key expiration

**Performance**:
- Sub-millisecond latency
- 100,000+ operations/second per instance
- Multi-threaded scaling on multi-core systems
- Often edges Redis for simple string caching

**Memory Overhead**: Slab overhead varies, typically efficient for uniform-sized objects

**API Caching Examples**:

```python
import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# Simple cache-aside
cache_key = f"api:user:{user_id}"
user = mc.get(cache_key)

if user is None:
    user = fetch_from_api()
    mc.set(cache_key, user, time=3600)  # 1 hour TTL

return user
```

```python
# Rate limiting counter
def rate_limit(ip, max=100):
    key = f"ratelimit:{ip}"
    count = mc.incr(key)
    if count == 1:
        mc.set(key, 1, 60)  # Reset after 60 seconds
    return count <= max
```

**Strengths**:
- Simplicity: easy to set up and understand
- Pure caching focus (no persistence overhead)
- Multi-threaded for scaling on multi-core
- Fast for simple string caching
- Low operational complexity
- Excellent throughput for basic patterns
- Memory efficient for uniform objects

**Weaknesses**:
- No persistence (data lost on restart)
- Simple strings only (no data structures)
- LRU eviction only
- Manual serialization for complex data
- No replication or clustering (third-party solutions exist)
- Less suitable for session storage (no persistence)
- Limited to 1MB values by default

**Best For**:
- Simple, high-speed string caching
- Database query result caching
- HTML fragment caching
- API rate limiting
- Lightweight deployments
- Stateless applications
- High-throughput, simple patterns
- Small/medium sites without persistence needs

**Deployment** (typically behind a consistent hashing layer):
```
┌──────────────┐
│ Application  │
└──────┬───────┘
       │
┌──────────────────────┐
│ Consistent Hashing   │
│ (ketama algorithm)   │
└──────┬───────────────┘
       │
   ┌───┴───┬──────┬──────┐
   ↓       ↓      ↓      ↓
[MC1]   [MC2]  [MC3] ... [MCN]
Memcached Instances
```

**Documentation**: https://memcached.org/

---

### Redis vs Memcached Comparison

| Feature | Redis | Memcached |
|---------|-------|-----------|
| **Data Structures** | Lists, Sets, Sorted Sets, Hashes, etc. | Strings only |
| **Threading** | Single-threaded per shard | Multi-threaded |
| **Persistence** | RDB, AOF | None |
| **Replication** | Master-replica | External solutions |
| **Clustering** | Native cluster mode | Consistent hashing layer |
| **Max Key Size** | 512MB | ~250 bytes |
| **Max Value Size** | 512MB | 1MB (configurable) |
| **TTL/Expiration** | Per-key with precise granularity | Per-key in seconds |
| **Eviction Policies** | 6 strategies (LRU, LFU, etc.) | LRU only |
| **Pub/Sub** | Yes | No |
| **Transactions** | MULTI/EXEC with WATCH | No |
| **Lua Scripting** | Yes | No |
| **Setup Complexity** | Moderate | Simple |
| **Use Case** | Complex apps, sessions, analytics | Simple caching, rate limiting |

**Choose Memcached for**:
- Maximum simplicity and speed for basic caching
- High-throughput simple string caching
- Stateless applications
- Cost-sensitive small deployments

**Choose Redis for**:
- Complex data structures
- Session storage and state
- Persistence needs
- Real-time analytics
- Distributed systems
- Replication and failover
- Any non-trivial application state

---

## GraphQL-Specific Caching

### Apollo Client (Normalized Caching)

**Type**: GraphQL client with in-memory normalized cache

**Key Features**:
- **InMemoryCache**: Normalizes GraphQL responses using object IDs
- **Automatic Updates**: Changes to one query automatically update related queries
- **Cache Directives**: `@cached`, `@skip`, `@include` for fine control
- **Partial Queries**: Request only needed fields to improve cache hit rates
- **Refetching**: Automatic or manual cache refresh
- **Local State Management**: Combine remote + local state seamlessly
- **Pagination Helpers**: `fetchMore` for cursor-based pagination
- **React Hooks**: `useQuery`, `useMutation` with built-in caching

**Normalized Cache Structure**:
```javascript
// GraphQL Query
query GetUser($id: ID!) {
  user(id: $id) {
    id
    name
    email
    posts { id title }
  }
  featured: posts(featured: true) { id title }
}

// Normalized cache representation
{
  "user:1": {
    id: "1",
    name: "Alice",
    email: "alice@example.com",
    posts: [ref("post:1"), ref("post:2")]
  },
  "post:1": { id: "1", title: "First Post" },
  "post:2": { id: "2", title: "Second Post" },
  "ROOT_QUERY": {
    "user({\"id\":\"1\"})": ref("user:1"),
    "featured({\"featured\":true})": [ref("post:1"), ref("post:2")]
  }
}
```

**Benefits**:
- Single update affects all related queries
- Automatic deduplication
- Efficient memory usage
- Client-side cache hits eliminate network roundtrips

**Configuration Example**:
```javascript
import { InMemoryCache } from '@apollo/client';

const cache = new InMemoryCache({
  typePolicies: {
    Query: {
      fields: {
        posts: {
          keyArgs: ['filter', 'sort'],
          merge(existing = [], incoming) {
            return [...existing, ...incoming];
          }
        }
      }
    },
    User: {
      keyFields: ['id'],
      fields: {
        email: {
          read(email) {
            return email ? email.toLowerCase() : email;
          }
        }
      }
    }
  }
});
```

**Best For**:
- React and Vue.js applications
- Complex data relationships
- Dynamic, frequently-changing data
- Applications with multiple queries fetching overlapping data
- Real-time collaborative applications

---

### Apollo Server (Server-Side Response Caching)

**Type**: GraphQL server implementation with caching

**Key Features**:
- **Response Caching Plugin**: Caches full responses to identical queries
- **Entity Caching**: Cache at field level using `@cacheControl` directives
- **Apollo Router**: Enterprise caching with granular control
- **Cache Directives**: `maxAge`, `scope` (PUBLIC/PRIVATE) per field
- **Cache Purging**: Automatic invalidation via mutations

**Cache Control Directives**:
```graphql
type Query {
  user(id: ID!): User
  # Cache for 1 hour in public cache
  posts(limit: Int = 10): [Post]
    @cacheControl(maxAge: 3600, scope: PUBLIC)
  # Never cache user-specific data
  me: User
    @cacheControl(maxAge: 0, scope: PRIVATE)
}

type Post {
  id: ID!
  title: String!
  author: User!
    @cacheControl(maxAge: 300)
}
```

**Server Configuration**:
```javascript
import { ApolloServer } from 'apollo-server-express';
import { ResponseCachePlugin } from 'apollo-server-plugin-response-cache';

const server = new ApolloServer({
  typeDefs,
  resolvers,
  plugins: [ResponseCachePlugin.default()],
  cacheControl: {
    stripFormattedFieldDetails: false
  }
});
```

**Apollo Router** (Enterprise):
- Fine-grained entity-level caching
- Automatic cache invalidation
- Distributed caching
- Traffic reduction to origin

**Best For**:
- GraphQL APIs with public content
- Content with predictable freshness requirements
- Reducing origin service load
- Distributed GraphQL execution

---

### Relay (Normalized Caching)

**Type**: GraphQL client with strict normalized caching

**Key Features**:
- **Globally Unique IDs**: Required across entire schema
- **Strict Typing**: Type safety built into cache operations
- **Automatic Cache Updates**: Changes propagate automatically
- **Declarative Fetching**: Inline fragments for query specifications
- **Refetch Behavior**: Fine control over data freshness
- **Pagination**: Cursor-based with connection pattern

**Example**:
```javascript
import { useFragment } from 'react-relay';

const UserProfile = ({ userRef }) => {
  const user = useFragment(
    graphql`
      fragment UserProfile_user on User {
        id
        name
        friends(first: 10) {
          edges {
            node {
              id
              name
            }
          }
        }
      }
    `,
    userRef
  );

  return <div>{user.name} has {user.friends.edges.length} friends</div>;
};
```

**Strengths**:
- Type-safe cache operations
- Strict schema patterns reduce bugs
- Automatic refetch on mutations
- Excellent for large applications

**Best For**:
- Large-scale applications with strict patterns
- Teams prioritizing type safety
- Applications with complex data relationships
- Facebook-sized applications

---

### URQL

**Type**: Lightweight GraphQL client

**Key Features**:
- **Document Caching**: Cache full responses
- **Request Policy**: Flexible cache strategies (`cache-first`, `network-only`, etc.)
- **Exchanges**: Middleware-like extensibility
- **Offline Mode**: Built-in offline support
- **Suspense**: React suspense integration

**Best For**:
- Lightweight applications
- Projects needing flexibility
- Custom caching strategies
- Smaller bundle size requirements

---

### Hasura

**Type**: GraphQL engine providing instant GraphQL APIs

**Key Features**:
- Auto-generates GraphQL from databases
- Integrates with client-side caches (Apollo, Relay)
- No built-in server-side caching (relies on client)
- Benefits from application-level caching (Redis/DataLoader)
- Cache-aware query optimization

**Caching Strategy**:
- Use Apollo Client/Relay on frontend (normalized caching)
- Use Redis with Hasura for application-level caching
- DataLoader for N+1 prevention
- Cache-Control headers for CDN caching

**Example** (with Redis):
```javascript
// Using Hasura with Apollo Client caching
const client = new ApolloClient({
  uri: 'https://my-hasura.example.com/v1/graphql',
  cache: new InMemoryCache(),
  link: new HttpLink({
    uri: '...',
    credentials: 'include'
  })
});
```

---

## Service Mesh Caching

### Istio with Envoy

**Type**: Service mesh using Envoy sidecar proxies

**Caching Capabilities**:
- **Envoy HTTP Cache**: Response caching via cache policies
- **Discovery Cache**: Internal caching for service discovery
- **Connection Pooling**: Cached connections for performance
- **TLS Session Caching**: Standard TLS resumption

**Cache Configuration** (VirtualService):
```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api
spec:
  hosts:
  - api.example.com
  http:
  - match:
    - uri:
        prefix: /cached
    route:
    - destination:
        host: api
        port:
          number: 8080
    # No native Envoy cache directive in Istio CRDs
    # Cache via external proxies (Nginx, Varnish) before mesh
```

**Typical Pattern**:
```
[Client] → [Nginx Cache] → [Istio Ingress] → [Envoy Sidecar] → [Service]
              (HTTP caching)  (mTLS termination) (load balancing)
```

**Best For**:
- Multi-level caching (edge + mesh)
- Microservices with complex routing
- mTLS security between services
- Large Kubernetes deployments

**Documentation**: https://istio.io/

---

### Linkerd

**Type**: Lightweight service mesh using Rust micro-proxies

**Caching Capabilities**:
- **Proxy Discovery Cache**: Caches service discovery information
- **Connection Pooling**: Cached TCP connections
- **No HTTP Response Caching**: Designed for simplicity

**Configuration** (via annotations):
```yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    config.linkerd.io/proxy-outbound-discovery-cache-unused-timeout: "60s"
spec:
  # Pod definition
```

**Strengths**:
- Lightweight Rust implementation
- Minimal resource overhead
- Simple operational model
- Excellent for latency-sensitive workloads

**Best For**:
- Lightweight microservices
- Resource-constrained environments
- Organizations prioritizing operational simplicity
- Latency-sensitive applications

---

### Caching in Kubernetes Service Mesh (General)

**Multi-Level Caching Architecture**:
```
┌────────────────────────────────────────────────────────┐
│ Client                                                 │
└────────────┬─────────────────────────────────────────┘
             │
┌────────────▼─────────────────────────────────────────┐
│ CDN Layer (Cloudflare, CloudFront)                   │
│ - Static asset caching                               │
│ - Geographic distribution                            │
└────────────┬─────────────────────────────────────────┘
             │
┌────────────▼─────────────────────────────────────────┐
│ Ingress Controller (Nginx/HAProxy)                   │
│ - HTTP response caching                              │
│ - Load balancing                                     │
└────────────┬─────────────────────────────────────────┘
             │
┌────────────▼─────────────────────────────────────────┐
│ Service Mesh (Istio/Linkerd)                         │
│ - Connection pooling                                 │
│ - mTLS with session caching                          │
│ - Service discovery cache                            │
└────────────┬─────────────────────────────────────────┘
             │
┌────────────▼─────────────────────────────────────────┐
│ Application Caching (Redis/Memcached)                │
│ - Query results                                      │
│ - Session data                                       │
│ - Computed results                                   │
└────────────┬─────────────────────────────────────────┘
             │
         [Databases/APIs]
```

---

## CDN and Edge Caching

### Cloudflare

**Type**: Global CDN with edge caching and worker functions

**Key Features**:

1. **Cache Rules** (evolved from Page Rules):
   - URL pattern matching
   - Cache level control (Bypass, Standard, Aggressive, Cache Everything)
   - Override Cache-Control headers
   - Dynamic rules based on headers, cookies, query strings

2. **Cache API** (in Workers):
   ```javascript
   // Store custom response in cache
   await caches.default.put(request, response);

   // Retrieve from cache
   const cached = await caches.default.match(request);

   // Delete from cache
   await caches.default.delete(request);
   ```

3. **Cloudflare Workers**:
   - Serverless compute at edge
   - Custom caching logic
   - Request/response modification
   - Time-based logic (location, time-based responses)

4. **Cache Tags**:
   - Group related cached items
   - Purge multiple items via API
   - Example: All product pages tagged with "products"

5. **TTL Management**:
   - Respect origin Cache-Control headers
   - Override defaults
   - Cache Reserve (persistent storage)
   - Tiered Cache (reduce origin load)

**Cache Configuration Example**:
```
Cache Rules:
- Pattern: api.example.com/posts/*
  - Cache level: Cache Everything
  - TTL: 1 hour
  - Browser TTL: 30 minutes

- Pattern: api.example.com/users/me
  - Cache level: Bypass (never cache)

- Pattern: *.jpg
  - Cache level: Aggressive
  - TTL: 30 days
```

**Cost**: Plan-dependent; Free tier includes basic caching

**Best For**:
- Global content delivery
- Static asset caching
- API response caching
- DDoS protection
- Rate limiting
- Bot management

**Documentation**: https://developers.cloudflare.com/cache/

---

### AWS CloudFront

**Type**: CDN with caching and distribution

**Key Features**:
- Origin shield for additional caching layer
- Lambda@Edge for edge compute
- Custom cache key patterns
- Origin access control
- Compression
- Signed requests

**Best For**:
- AWS-native architectures
- Global content distribution
- Private content with signed URLs

---

### Other CDNs

- **Akamai**: Enterprise CDN with advanced caching
- **Fastly**: Real-time purging, powerful VCL
- **Bunny CDN**: Cost-effective edge caching
- **KeyCDN**: Developer-friendly edge caching

---

## Database and Query Caching

### DataLoader Pattern

**Type**: Query batching and caching for N+1 prevention

**Key Features**:
- Batches multiple requests into single query
- Caches results within request lifecycle
- Prevents duplicate fetches
- Works with GraphQL resolvers and REST endpoints

**Problem (N+1)**:
```
Query 1: SELECT * FROM users WHERE id = 1
Query 2: SELECT * FROM posts WHERE user_id = 1
Query 3: SELECT * FROM posts WHERE user_id = 1  ← Duplicate!
Query 4: SELECT * FROM posts WHERE user_id = 1  ← Another duplicate!
```

**Solution with DataLoader**:
```javascript
import DataLoader from 'dataloader';

const postLoader = new DataLoader(async (userIds) => {
  // Receives [1, 1, 1, 2, 3, 3]
  // Batches into single query
  const posts = await db.query(
    `SELECT * FROM posts WHERE user_id IN (${userIds.join(',')})`
  );
  // Returns one result per input, in same order
  return userIds.map(id => posts.filter(p => p.user_id === id));
});

// In GraphQL resolver
{
  User: {
    posts: (user) => postLoader.load(user.id)
  }
}
```

**Benefits**:
- Eliminates N+1 queries
- Single batched query instead of N separate queries
- Per-request caching (local to request)
- Works seamlessly with GraphQL and REST

**Best For**:
- GraphQL resolvers
- REST endpoints with relationships
- Any scenario with potential N+1 queries
- Preventing database overload

**Library**: https://github.com/graphql/dataloader

---

### Redis for Query Result Caching

**Pattern**: Cache-aside with automatic invalidation

```python
def get_user_with_posts(user_id):
    cache_key = f"user:{user_id}:with_posts"

    # Try cache first
    cached = redis.get(cache_key)
    if cached:
        return json.loads(cached)

    # Cache miss: fetch from DB
    user = db.query(User).get(user_id)
    posts = db.query(Post).filter_by(user_id=user_id).all()

    result = {
        "user": user.to_dict(),
        "posts": [p.to_dict() for p in posts]
    }

    # Store with TTL (1 hour)
    redis.setex(cache_key, 3600, json.dumps(result))

    return result

# On user update, invalidate cache
def update_user(user_id, data):
    user = db.query(User).get(user_id)
    user.update(data)
    db.commit()

    # Invalidate cache
    redis.delete(f"user:{user_id}:with_posts")
    redis.delete(f"user:{user_id}:profile")
```

---

### Connection Pooling Caching

**Types**:
- **HikariCP** (Java): Pools and caches connections
- **PgBouncer** (PostgreSQL): Connection pool with statement cache
- **SQLAlchemy** (Python): Built-in pooling with statement cache
- **Prisma**: Automatic connection pooling

**Benefits**:
- Reduces connection overhead
- Reuses TCP connections
- Caches prepared statements
- Reduces latency for sequential queries

**Configuration Example** (SQLAlchemy):
```python
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://user:password@localhost/db',
    pool_size=20,           # Active connections
    max_overflow=40,        # Overflow connections
    pool_pre_ping=True,     # Test connections before use
    pool_recycle=3600       # Recycle connections hourly
)
```

---

### Database-Level Query Result Caching

- **MongoDB**: WiredTiger in-memory engine
- **PostgreSQL**: Shared buffers (check cache hit ratio)
- **MySQL**: Query cache (deprecated in MySQL 8.0)
- **Redis**: For application-level query caching

---

## REST API Caching Strategies

### HTTP Cache Headers

**Cache-Control Header**:
```http
Cache-Control: max-age=3600, public, must-revalidate
```

- `max-age=N`: Cache for N seconds
- `s-maxage=N`: Override for shared caches
- `public`: Cacheable by anyone
- `private`: Only client cache (not shared/CDN)
- `no-cache`: Revalidate before using
- `no-store`: Don't cache at all
- `must-revalidate`: Don't serve stale without validation
- `immutable`: Response never changes (versioned assets)

**Example Uses**:
```
Static assets (CSS, JS, images):
Cache-Control: max-age=31536000, immutable  # 1 year

API responses (data):
Cache-Control: max-age=300, public  # 5 minutes

User-specific data:
Cache-Control: max-age=0, private  # Revalidate always

Never cache:
Cache-Control: no-store
```

**ETag and Conditional Requests**:
```http
# Server response
HTTP/1.1 200 OK
ETag: "abc123"
Content-Length: 1234

{...}

# Client subsequent request
GET /api/data
If-None-Match: "abc123"

# Server response (if unchanged)
HTTP/1.1 304 Not Modified
ETag: "abc123"

# Saves bandwidth: No body sent, client reuses cached copy
```

**Last-Modified and Conditional Requests**:
```http
# Server response
HTTP/1.1 200 OK
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT

# Client request
GET /api/data
If-Modified-Since: Wed, 21 Oct 2025 07:28:00 GMT

# Server response
HTTP/1.1 304 Not Modified
```

---

### Caching Strategies

| Strategy | Use Case | Implementation |
|----------|----------|-----------------|
| **Cache-Aside** | Hot data | Client checks cache, misses fetch from DB, cache result |
| **Write-Through** | Consistent state | Update cache + DB atomically |
| **Write-Behind** | High throughput | Update DB, async cache later |
| **Time-Based TTL** | Simple invalidation | Set expiration time, let cache expire naturally |
| **Event-Based Invalidation** | Real-time freshness | On data change, purge related cache keys |
| **Granular Caching** | Memory efficiency | Cache fields/fragments, not full objects |
| **Preloading** | Reduced misses | Warm cache for hot endpoints before peak |

---

### REST API Caching Best Practices

1. **Cacheable Requests**:
   - GET requests only (idempotent)
   - HEAD requests (if applicable)
   - POST only if explicitly cacheable (rare)

2. **Cache Keys**:
   - URL + method + request headers (Accept, Authorization)
   - Content-Type variations
   - API version in URL

3. **TTL Selection**:
   - Static content: Hours to years
   - Dynamic data: Seconds to minutes
   - User-specific: No cache (private) or very short
   - Real-time data: No cache

4. **Invalidation**:
   - TTL expiration (simplest)
   - Explicit purge on mutations
   - Conditional requests (ETag/Last-Modified)
   - Cache tags for grouped purging

5. **Monitoring**:
   - Cache hit ratio (aim for 50-80%)
   - Hit/miss rates per endpoint
   - Cache memory usage
   - Latency improvements

---

## Comparison Matrix

### HTTP/Reverse Proxy Caching Solutions

| Solution | Type | Setup Complexity | Caching Flexibility | Performance | Best For |
|----------|------|------------------|-------------------|-------------|----------|
| **Varnish** | HTTP accelerator | High (VCL) | Excellent (complex rules) | High | Complex, high-traffic sites |
| **Nginx** | Web server + proxy | Low-Medium | Medium (basic directives) | Very High | General-purpose, simple |
| **HAProxy** | Load balancer | Medium | Low-Medium (simple rules) | Very High | APIs with load balancing |
| **Squid** | Proxy | Medium-High | High | Medium | Corporate proxies, hierarchies |

### In-Memory Caching Stores

| Solution | Data Structures | Persistence | Clustering | Throughput | Best For |
|----------|-----------------|-------------|-----------|-----------|----------|
| **Redis** | Advanced | RDB/AOF | Native | Very High | Complex apps, sessions |
| **Memcached** | Strings only | None | External | Highest | Simple, high-speed caching |

### API Gateway Caching

| Gateway | Caching Type | Setup | Best For |
|---------|--------------|-------|----------|
| **Kong** | Plugin-based | Medium | Cloud-native, microservices |
| **AWS API Gateway** | Built-in | Low | AWS-native stacks |
| **Azure API Mgmt** | Policy-based | Medium | Azure ecosystems |
| **Traefik** | External (Redis) | High | Container orchestration |

### GraphQL Client Caching

| Client | Cache Type | Data Structures | Best For |
|--------|-----------|-----------------|----------|
| **Apollo Client** | Normalized | Full | React apps, flexible |
| **Relay** | Normalized | Full | Type-safe, large apps |
| **URQL** | Flexible | Full | Lightweight apps |

### Edge/CDN Caching

| Service | Features | Cost | Best For |
|---------|----------|------|----------|
| **Cloudflare** | Rules, Workers, Tags | Free tier available | Global content, edge compute |
| **AWS CloudFront** | Origin Shield, Lambda@Edge | Per-request | AWS-native, private content |
| **Fastly** | Real-time purge, VCL | Premium | High-performance, real-time |

---

## Implementation Checklist

### Before Choosing a Caching Solution

- [ ] Identify cacheable vs. non-cacheable requests
- [ ] Analyze access patterns (hot data, TTL requirements)
- [ ] Measure current performance bottlenecks
- [ ] Determine cache hit ratio targets (aim for 50-80%)
- [ ] Plan invalidation strategy (TTL, event-based, manual)
- [ ] Consider operational overhead (setup, monitoring, failover)
- [ ] Evaluate cost vs. performance gains
- [ ] Plan for cache key collisions and conflicts
- [ ] Design monitoring and alerting

### Multi-Level Caching Architecture

For production systems:

```
[Client Browser Cache] ← HTTP Cache-Control headers
        ↓
[CDN/Edge Cache] ← Cloudflare/CloudFront
        ↓
[Reverse Proxy Cache] ← Nginx/Varnish/HAProxy
        ↓
[API Gateway Cache] ← Kong/AWS API Gateway
        ↓
[Application Cache] ← Redis/Memcached
        ↓
[Database] ← Query result caching, connection pooling
```

### Example Production Stack

```
Client
  ↓
Cloudflare (CDN, edge caching, workers)
  ↓
Nginx (HTTP reverse proxy caching)
  ↓
Kong (API gateway with caching plugin)
  ↓
Application (Apollo Client for GraphQL normalization)
  ↓
Redis (query result caching, sessions)
  ↓
PostgreSQL (database with connection pooling)
```

---

## Key Takeaways

1. **No single solution fits all**: Layer caching at multiple levels
2. **Varnish** for complex HTTP caching logic
3. **Nginx** for general-purpose, lightweight caching
4. **Redis** for application-level caching with complex data
5. **Memcached** for simple, high-speed string caching
6. **Kong** for cloud-native API gateway scenarios
7. **Apollo Client** for GraphQL normalized caching
8. **DataLoader** for GraphQL N+1 prevention
9. **Cloudflare** for global CDN and edge caching
10. **Multi-level** caching architecture for best performance

---

## Resources

- Varnish Documentation: https://varnish-cache.org/
- Nginx Caching: https://nginx.org/en/docs/
- HAProxy: https://www.haproxy.org/
- Redis: https://redis.io/
- Memcached: https://memcached.org/
- Kong: https://konghq.com/
- Apollo GraphQL: https://www.apollographql.com/
- Cloudflare Cache: https://developers.cloudflare.com/cache/
- AWS API Gateway Caching: https://docs.aws.amazon.com/apigateway/
- HTTP Caching: https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching

