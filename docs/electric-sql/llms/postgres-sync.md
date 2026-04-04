# Source: https://electric-sql.com/products/postgres-sync.md

---
url: /products/postgres-sync.md
description: >-
  Read-path sync engine for Postgres that handles partial replication, data
  delivery and fan-out.
---

# Postgres Sync

Read-path sync engine for Postgres that handles partial replication,

data delivery and

fan-out.

## Postgres sync engine

Postgres Sync is a sync engine that syncs [subsets of your data](/docs/guides/shapes) out of your Postgres database, into local apps and services.

You can sync data into anything you like. From web, mobile and desktop apps and client stores like [TanStack DB](/products/tanstack-db) to databases like [PGlite](/products/pglite).

> \[!Warning] 🎓  A quick note on naming
> Postgres Sync used to just be called "Electric" or the "Electric sync engine". Some docs and package names still use the old naming.

## How does it work?

Postgres Sync connects to your Postgres using a [`DATABASE_URL`](/docs/api/config#database-url), consumes the logical replication stream and fans out data into [Shapes](/docs/guides/shapes), which [Clients](/docs/api/clients/typescript) then consume and sync.

Technically, Postgres Sync is an [Elixir](https://elixir-lang.org) application, developed at [packages/sync-service](https://github.com/electric-sql/electric/tree/main/packages/sync-service). It runs as a seperate service, [between your API and your database](/docs/guides/deployment). Clients consume data over an [HTTP API](/docs/api/http) that [works with CDNs](/docs/api/http#caching) to scale data delivery and fan-out.

This allows you to have [millions of concurrent users](/docs/reference/benchmarks) subscribing to real-time updates to your database with minimal additional load on your database.

## Related posts

## More information

See the [Quickstart](/docs/quickstart), [Docs](/docs/intro) and [Demos](/demos).
