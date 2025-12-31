# Source: https://electric-sql.com/product/electric.md

---
url: /product/electric.md
description: Sync little subsets of your Postgres data into local apps and services.
---

# Electric

Sync little subsets of your Postgres data into
local apps and services.

> \[!Warning] Electric 1.0 release
> Electric is now 1.0! See the [release post here](/blog/2025/03/17/electricsql-1.0-released).

## Electric sync engine

The Electric sync engine syncs [little subsets](/docs/guides/shapes) of data out of Postgres into local apps and services — wherever you need the data.

You can sync data into:

* web and mobile apps, [replacing data fetching with data sync](/use-cases/data-sync)
* edge workers and services, for example maintaining a low-latency [edge data cache](/use-cases/cache-invalidation)
* local AI systems, for example [running RAG using pgvector](/use-cases/local-ai)
* dev and test environments, for example syncing data into [an embedded PGlite](/product/pglite) database

## How does it work?

The Electric sync engine is an [Elixir](https://elixir-lang.org) application, developed at [packages/sync-service](https://github.com/electric-sql/electric/tree/main/packages/sync-service).

It connects to your Postgres using a [`DATABASE_URL`](/docs/api/config#database-url), consumes the logical replication stream and fans out data into [Shapes](/docs/guides/shapes), which [Clients](/docs/api/clients/typescript) then consume and sync.

This enables a massive number of clients to query and get real-time updates to subsets of the database. In this way, Electric turns Postgres into a real-time database.

## More information

See the [Docs](/docs/intro), [Quickstart](/docs/quickstart) and [Demos](/demos). You can [self-host](/docs/guides/deployment) or use the [Electric Cloud](/product/cloud).
