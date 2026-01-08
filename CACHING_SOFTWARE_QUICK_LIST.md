# Caching Software, Libraries, and Tools - Quick Reference List

Alphabetically organized comprehensive catalog of caching solutions mentioned in research.

## Distributed Caching Systems

1. **Akamai** - CDN service
2. **Amazon ElastiCache** - Managed Redis/Memcached service
3. **Apache Ignite** - In-memory database and computing platform
4. **Bunny CDN** - Cost-effective CDN provider
5. **Cloudflare** - CDN/edge platform
6. **Cloudflare Workers** - Edge computing platform
7. **Dragonfly** - High-performance Redis-compatible in-memory database
8. **Fastly** - High-performance CDN service
9. **GemFire** - Distributed in-memory data store
10. **Hazelcast** - Distributed data structures and in-memory computing
11. **Infinispan** - Open-source distributed caching framework
12. **KeyDB** - Multi-threaded Redis fork
13. **Memcached** - Distributed memory object caching system
14. **Microsoft Azure Cache for Redis** - Managed Redis on Azure
15. **Nginx** - Web server/reverse proxy with caching
16. **Oracle Coherence** - Enterprise distributed caching platform
17. **Redis** - In-memory key-value store with rich data structures
18. **Squid** - Web proxy cache
19. **Terracotta BigMemory** - Large-scale in-memory data management
20. **Valkey** - Open-source Redis fork
21. **Varnish** - HTTP accelerator/caching proxy
22. **AWS CloudFront** - Amazon's CDN service

## Python Libraries

1. **cacheout** - Flexible in-memory caching with multiple eviction policies
2. **cachetools** - Caching library with various strategies
3. **diskcache** - Disk-backed caching with persistence
4. **functools.cache** - Unbounded function caching (Python 3.9+)
5. **functools.lru_cache** - LRU function caching decorator
6. **joblib.Memory** - File-based caching for computations

## Java Libraries

1. **Cache2k** - Specialized high-performance cache
2. **Caffeine** - High-performance in-memory cache
3. **Ehcache** - Mature, full-featured cache with JCache support
4. **Guava Cache** - Lightweight caching utility
5. **Spring Cache** - Abstraction layer for caching

## Go Libraries

1. **BigCache** - Cache for large datasets with low GC overhead
2. **FastCache** - High-performance caching
3. **Otter** - Next-gen cache with S3-FIFO eviction
4. **Ristretto** - TinyLFU-based caching library
5. **Theine** - High-performance cache with W-TinyLFU eviction
6. **go-cache** - Lightweight in-memory cache with TTL

## Rust Libraries

1. **cached** - Memoization library with TTL support
2. **dashmap** - Concurrent HashMap (cache-like use)
3. **fast-lru** - Stack-based LRU implementation
4. **lru** / **lrumap** - Simple LRU cache implementations
5. **moka** - High-performance concurrent cache (Caffeine-inspired)
6. **parking_lot** - Efficient lock primitives (used in caching)
7. **plain-cache** - Thread-safe basic cache
8. **quick_cache** - Lightweight concurrent cache with minimal overhead

## C# / .NET Libraries

1. **CacheManager** - Abstraction layer for caching with multiple providers
2. **EasyCaching** - Open-source caching abstraction with multiple backends
3. **EnyimMemcached** - Memcached client library
4. **HybridCache** - Built-in .NET 9+ hybrid caching
5. **IDistributedCache** - Microsoft abstraction for distributed caching
6. **IMemoryCache** - Microsoft built-in in-memory caching
7. **Microsoft.Extensions.Caching.StackExchangeRedis** - Official Redis provider
8. **NCache** - Enterprise distributed caching platform
9. **ServiceStack.Memcached** - High-performance Memcached client
10. **StackExchange.Redis** - High-performance Redis client

## JavaScript / Node.js Libraries

1. **Apollo Client (InMemoryCache)** - GraphQL client with normalized caching
2. **apicache** - HTTP response caching middleware
3. **cache-manager** - Multi-backend caching abstraction
4. **lru-cache** - LRU eviction cache
5. **memory-cache** - Basic in-memory caching
6. **node-cache** - Lightweight in-memory cache with TTL

## GraphQL Caching Tools

1. **Apollo Client** - GraphQL client with field-level caching
2. **Apollo Server** - GraphQL server with cache control directives
3. **Relay** - Meta's GraphQL framework with caching support
4. **responseCachePlugin** - Apollo Server plugin for response caching

## React / Frontend Caching

1. **Apollo Client** - GraphQL client with InMemoryCache
2. **RTK Query** - Redux Toolkit Query caching
3. **SWR** - HTTP fetch with stale-while-revalidate
4. **TanStack Query** (React Query) - Server state management and caching

## ORM Query Caching Tools

1. **Dogpile.cache** - Python caching library for SQLAlchemy
2. **django-cacheops** - ORM-aware caching for Django
3. **django-redis** - Redis integration for Django
4. **Flask-Caching** - Flask caching extension
5. **Flask-SQLAlchemy-Caching** - SQLAlchemy caching wrapper for Flask

## Browser / Client-Side Caching Technologies

1. **Cache API** - Service Worker cache storage
2. **IndexedDB** - Browser-based database storage
3. **localStorage** - Persistent key-value storage
4. **Service Workers** - Background scripts for advanced caching
5. **sessionStorage** - Session-scoped key-value storage

## Python Web Framework Caching

1. **Django** - Built-in caching framework
2. **FastAPI** - No built-in caching (uses external libraries)
3. **Flask** - Flask-Caching extension
4. **Werkzeug** - Caching utilities

## Java Web Framework Caching

1. **Jakarta EE** - JCache (JSR-107) standard support
2. **Quarkus** - Native support for Infinispan, Redis
3. **Spring** - Spring Cache abstraction layer
4. **Spring Boot** - Auto-configuration for caching providers

---

## Count Summary

- **Distributed Systems**: 22
- **Python Libraries**: 6
- **Java Libraries**: 5
- **Go Libraries**: 6
- **Rust Libraries**: 8
- **C# / .NET Libraries**: 10
- **JavaScript / Node.js Libraries**: 6
- **GraphQL Tools**: 4
- **React / Frontend**: 4
- **ORM Tools**: 5
- **Browser Technologies**: 5
- **Framework Integrations**: 8

**Total Unique Software/Libraries Documented**: 89+

---

## Commonly Co-Used Combinations

### Node.js + GraphQL
- Apollo Client + Apollo Server + cache-manager

### Python + Web
- Flask + Flask-Caching + Redis

### Python + Data Science
- Joblib.Memory + diskcache + NumPy

### Java + Microservices
- Spring Cache + Caffeine + Redis

### Go + High-Performance
- Otter/Theine + Redis

### C# + Enterprise
- Spring Cache + Ehcache + Hazelcast or StackExchange.Redis + NCache

### React + Data Fetching
- TanStack Query + Apollo Client + SWR

### PWA
- Service Workers + Cache API + localStorage/IndexedDB

---

## Selection Criteria by Priority

### Need: Maximum Speed (Single Server)
→ Caffeine (Java), Otter/Theine (Go), moka (Rust), functools.lru_cache (Python)

### Need: Distributed Caching
→ Redis, Hazelcast, Apache Ignite, Memcached

### Need: Enterprise Features
→ NCache (.NET), Oracle Coherence (Java), Infinispan (Java)

### Need: Minimal Dependencies
→ lru-cache (Node.js), node-cache (Node.js), Guava Cache (Java), quick_cache (Rust)

### Need: Framework Integration
→ Spring Cache (Java), Flask-Caching (Python), TanStack Query (React)

### Need: GraphQL Specific
→ Apollo Client/Server, Relay

### Need: HTTP/CDN Level
→ Varnish, Nginx, Cloudflare, AWS CloudFront

### Need: Database Query Caching
→ SQLAlchemy + CachingQuery + Redis, django-cacheops, Spring Cache + Hibernat

### Need: Progressive Web App
→ Service Workers + Cache API + localStorage/IndexedDB

---

Generated: January 2026
Research methodology: Comprehensive web search via Tavily AI and Perplexity CLI
