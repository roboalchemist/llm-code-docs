# Source: https://electric-sql.com/products.md

---
url: /products.md
description: Composable sync primitives from ElectricSQL
---

# Electric products

Composable sync primitives that work with your stack.

## How they fit together {#how-they-fit-together}

The sync primitives in the Electric stack are designed to work together and work with your API and existing infrastructure.

In the diagram below, the white boxes are your components / infra.

Postgres Sync connects to [your Postgres](/docs/guides/deployment#_1-running-postgres) and syncs data [over HTTP](/docs/api/http).

TanStack DB is the recommended client for application development. You can sync data into TanStack DB [from Electric](https://tanstack.com/db/latest/docs/collections/electric-collection) and/or [from a Durable Stream](/blog/2026/01/12/durable-sessions-for-collaborative-ai#reference-implementation). It also provides mutation primitives that work with your backend API.

PGlite is mainly used in [dev, test and sandbox environments](/blog/2025/06/05/database-in-the-sandbox). You can use it as a standalone embedded database or you can sync data into it [using Postgres Sync](https://pglite.dev/docs/sync).

## Which product should I use?

### Building web, mobile and desktop apps?

There are lots of options here. However, for most apps we recommend using [Postgres Sync](/products/postgres-sync) for data sync and [TanStack DB](/products/tanstack-db) for reactive state-management and optimistic mutations in the client.

See the [building super-fast apps on sync](/blog/2025/07/29/super-fast-apps-on-sync-with-tanstack-db) post for more info.

::: details App development alternatives

* simple apps can use the [TypeScript client](/docs/api/clients/typescript) directly
* TanStack DB apps can load data [from your API](https://tanstack.com/db/latest/docs/overview#1-tanstack-query) instead of using a sync engine
* apps can sync data [through Durable Streams](/products/durable-streams#wrapper-protocols) when it doesn't make sense to go through Postgres, including using [Durable State](https://github.com/durable-streams/durable-streams/tree/main/packages/state) for structured state sync alongside real-time streams
* web and desktop apps can use [PGlite](/products/pglite) in the client to access the Postgres query engine, data types and extensions like `pgvector` (if they can tolerate a slightly heavier WASM dependency)
* Elixir apps can use [Phoenix.Sync](https://hexdocs.pm/phoenix_sync/readme.html) with both LiveView and TanStack DB

:::

### Building AI apps and agentic systems?

Use [Durable Streams](/products/durable-streams) for core durable transport for resilience and resumeability. Combine with [TanStack DB](/products/tanstack-db) for [Durable Sessions](/blog/2026/01/12/durable-sessions-for-collaborative-ai#durable-session-pattern) with persistence and natural support for multi-user, multi-agent collaboration.

You can also use [Postgres Sync](/products/postgres-sync) to sync message history, metadata and structured elements and then [join this up into a single, unified, reactive, client data model](https://tanstack.com/db/latest/docs/overview#defining-collections) that combines structured and unstructured data using TanStack DB.

### Building your own database or sync protocol?

You can use the lower-level [protocol layers](/products/durable-streams#wrapper-protocols) of [Durable Streams](/products/durable-streams) to craft your own sync protocol. Including passing a [Standard Schema](https://standardschema.dev/) to the [Durable State](https://github.com/durable-streams/durable-streams/tree/main/packages/state) layer for an instant, type-safe sync protocol tailored to your data schema.

You can also integrate [your own sync engine or data source](https://tanstack.com/db/latest/docs/guides/collection-options-creator) into TanStack DB.

### Building a platform or agent runtime?

Embed [PGlite](/products/pglite) for a full, reactive Postgres in your runtime. Including support for extensions like `pgvector`. This works in any JavaScript runtime, [including WebContainers](/blog/2025/06/05/database-in-the-sandbox), avoiding the need for external infra dependencies.

You can also design your own [TanStack DB collections](https://tanstack.com/db/latest/docs/guides/collection-options-creator), to bake reactive data management and [custom actions](https://tanstack.com/db/latest/docs/guides/mutations#creating-custom-actions) into your runtime APIs.

## Next steps

Dive into the [individual product pages](/products/postgres-sync) and [documentation](/docs/intro).
