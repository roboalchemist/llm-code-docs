# Source: https://electric-sql.com/use-cases/cache-invalidation.md

---
url: /use-cases/cache-invalidation.md
description: "Replace ttls and expiry policies with realtime\_sync and automated\_invalidation."
---

## Realtime caching with automatic invalidation

Caches are seperate local copies of data, maintained close to application code. They speed up data access, reducing latency and increasing scalability.

The challenge with caching is invalidation, i.e.: keeping the cache up-to-date. This is famously one of the hardest problems in computer science.

Electric solves cache invalidation for you by automatically keeping data in sync.

## The problem with stale data

A lot of systems today use ad-hoc mechanisms to maintain caches and keep them up-to-date. This leads to engineering complexity, stale data and bad user experience.

This applies both to the data plumbing and the algorithms used to expire data.

### Data plumbing

Say you're maintaining a cache of recently updated projects. What happens when one of those projects is renamed? You need to update the cache. So you need a mechanism for reliably propagating updates from your main data source to the cache.

This means you need durability, at-least-once delivery and to be able to recover from downtime. It's easy to get sucked into engineering complexity and it's easy to make mistakes, so a cache either gets stuck with stale data or wiped too often.

### Stale data

It's hard to know when a cache entry should be invalidated. Often, systems use ad-hoc expiry dates and "time to live" (or "ttls").

This leads to stale data, which can lead to confused users, integrity violations and having to write code to put safeguards around data you can't trust.

## Solved by Electric

Electric solves data plumbing with realtime sync and solves stale data with automated cache invalidation.

### Realtime sync

Electric syncs data into caches in realtime. [It's fast and reliable](/blog/2025/08/13/electricsql-v1.1-released), handles durability/delivery and reconnecting after downtime. You just declare the Shape of the data you want in the cache and Electric keeps it in sync.

### Automated cache invalidation

Electric automatically manages the data in your local cache for you. When the data changes, the changes are synced to the local cache which is automatically updated.

You don't need to manage cache invalidation seperately or set expiry dates of TTLs on the records in the cache. Electric handles it for you.

## Real world example

See the [Redis example](/demos/redis) and [integration page](/docs/integrations/redis) for a real world example, syncing data into a Redis cache with automatic invalidation.

## Next steps

Get started with Electric to simplify your stack and avoid stale data.
