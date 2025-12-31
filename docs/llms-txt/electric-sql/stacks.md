# Source: https://electric-sql.com/docs/stacks.md

---
url: /docs/stacks.md
description: >-
  Electric provides composable sync primitives that allow you to add real-time
  sync to your existing stack, without imposing technology choices, code changes
  or data silos.
---

# Sync with your stack

Electric provides [composable](/#works-with-section) sync primitives.

This allows you to add real-time sync to [your existing stack](/blog/2024/11/21/local-first-with-your-existing-api), without imposing technology choices, code changes or data silos.

## Sync stacks

We've picked four different sync stacks to illustrate four different ways of integrating Electric into your stack of choice.

### Core architecture

All of these sync stacks are based on the same core architecture.

[Electric](/docs/guides/deployment#_2-running-electric) always runs as a service in front of [Postgres](/docs/guides/deployment#_1-running-postgres), syncing into a [Client](/docs/guides/shapes#subscribing-to-shapes) process or store, via a [Proxy](/docs/guides/auth#requests-can-be-proxied) or backend API.

You can learn more about these by following [Deployment](/docs/guides/deployment) guide.

### Choosing a stack

We recommend using [TanStack DB](#tanstack-db) for web and mobile app development. It's super fast, lightweight, type-safe and gives you an [optimal, end-to-end, local-first sync stack](/blog/2025/07/29/local-first-sync-with-tanstack-db).

You can also combine TanStack DB with [Phoenix.Sync](#phoenix-sync) if you're building agentic systems with Elixir or looking for a batteries-included backend framework.

[PGlite](#pglite) and [Yjs](#yjs) are more for specialist use-cases where you're syncing into a dev, test or CI environment or crafting a multi-user collaboration system, respectively.

### Choosing a Postgres host

Electric works with [any Postgres with logical replication](/docs/guides/deployment#_1-running-postgres) enabled. [Neon](/docs/integrations/neon), [Supabase](/docs/integrations/supabase) and [Crunchy](/docs/integrations/crunchy) are all great choices for a Postgres host.

### Hosting your proxy

You can proxy requests to Electric either [through your backend API](/docs/guides/auth#it-s-all-http), or through a cloud worker. [Cloudflare](/docs/integrations/cloudflare) is a great choice for hosting workers because it only charges for actual processing time (not for wall clock time holding [sync connections](/docs/api/http#live-mode) open).

### Other stacks

The stacks on this page are just some options and recommendations. You can use Electric with any technology you like — as long as it speaks [HTTP and JSON](/docs/guides/client-development).

For example, sync into [LiveStore](https://docs.livestore.dev/reference/syncing/sync-provider/electricsql/) for a principled, event-sourcing based development model. Or [distributed SQlite](https://github.com/electric-sql/postgres-to-sqlite-sync-example) or [native iOS apps](https://github.com/paulharter/ElectricSync).

## &#x20;TanStack

| Database | Backend             | Schema  | Proxy      | Client           | Writes |
| -------- | ------------------- | ------- | ---------- | ---------------- | ------ |
| Postgres | TanStack Start | Drizzle | Cloudflare | TanStack DB | tRPC   |

[Tanstack DB](https://tanstack.com/db) is a reactive client store for [building super fast apps on sync](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query).

[Paired with Electric](/blog/2025/07/29/local-first-sync-with-tanstack-db) and [TanStack Start](https://tanstack.com/start), it gives you an end-to-end sync stack that's type-safe, declarative, incrementally adoptable and insanely fast.

### End-to-end Typescript

See the [tanstack-db-web-starter](https://github.com/electric-sql/electric/tree/main/examples/tanstack-db-web-starter) for an example of an end-to-end Typescript stack for web app development:

* based on Postgres, using [Drizzle](https://orm.drizzle.team/) for data schemas and migrations
* syncing data out of Electric through [TanStack Start server functions](https://tanstack.com/start/latest/docs/framework/react/server-functions)
* into [TanStack DB collections](https://tanstack.com/db/latest/docs/overview#defining-collections) for reactive, local-first client-side development
* using [tRPC mutation proceedures](https://trpc.io/docs/server/procedures) for type-safe write handling on the server

See also the [tanstack-db-expo-starter](https://github.com/electric-sql/electric/tree/main/examples/tanstack-db-expo-starter) for a similar stack for mobile app development.

### Incremental adoption

TanStack DB is designed to be incrementally adoptable into existing applications.

It's tiny — a few Kbs — so doesn't introduce a big dependency. It works with all major front-end reactivity frameworks. It works with API-based data loading and sync. So you can progressively adopt by first migrating API-based apps using TanStack Query and then migrate to sync without affecting the component code.

### Super fast 🔥

When you combine Electric with TanStack DB, you get blazing fast end-to-end reactivity.

Components use [live queries](https://tanstack.com/db/latest/docs/guides/live-queries) to react and when data changes. These are based on a [Typescript implementation of differential dataflow](https://github.com/electric-sql/d2ts). This means you can build complex client apps where everything reacts instantly, within a single animation frame.

#### More information

* [Local-first sync with TanStack DB and Electric](/blog/2025/07/29/local-first-sync-with-tanstack-db)
* [TanStack DB, the embedded client database for TanStack Query](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query)
* [An interactive guide to TanStack DB](https://frontendatscale.com/blog/tanstack-db)

## &#x20;Phoenix

| Database | Backend | Schema | Proxy   | Client           | Writes  |
| -------- | ------- | ------ | ------- | ---------------- | ------- |
| Postgres | Phoenix | Ecto   | Phoenix | TanStack DB | Phoenix |

[Phoenix](https://www.phoenixframework.org) is a full-stack web development framework for [Elixir](https://elixir-lang.org).

Electric is [developed in Elixir](/product/electric#how-does-it-work), has a first-class [Elixir client](/docs/api/clients/elixir) and a deep Phoenix framework integration in the form of the official [Phoenix.Sync](https://hexdocs.pm/phoenix_sync) library.

### Phoenix.Sync

Phoenix.Sync enables real-time sync for Postgres-backed [Phoenix](https://www.phoenixframework.org/) applications. You can use it to sync data into Elixir, `LiveView` and frontend web and mobile applications.

### Using with TanStack DB

Read-path sync works naturally with TanStack DB. Plus it provides:

* a [`Writer`](https://hexdocs.pm/phoenix_sync/readme.html#write-path-sync) module for ingesting TanStack DB mutations
* [`Igniter` and `Mix` commands](https://github.com/electric-sql/phoenix_sync/pull/102) to integrate TanStack DB with Phoenix

### Building agentic systems

Phoenix is built in [Elixir](https://elixir-lang.org), which runs on the [BEAM](https://blog.stenmans.org/theBeamBook/). The BEAM provides a robust agentic runtime environment with built-in primitives for [process supervision and messaging](https://hexdocs.pm/elixir/processes.html).

This makes Elixir and Phoenix a perfect match for agentic system development [without needing a seperate agent framework](https://goto-code.com/blog/elixir-otp-for-llms/).

#### More information

* [Burn](/demos/burn) agentic demo app
* [Bringing agents back down to earth](/blog/2025/08/12/bringing-agents-back-down-to-earth) blog post
* [Phoenix integration page](/docs/integrations/phoenix)
* [Phoenix.Sync documentation](https://hexdocs.pm/phoenix_sync)

## &#x20;PGlite

| Database | Client | Writes |
| -------- | ------ | ------ |
| Postgres | PGlite | Custom |

PGlite is an embeddable Postgres database.

Electric can sync data into PGlite to hydrate lightweight database instances for dev, test and sandboxed environments

### Lightweight developer database

Platforms including Google Firebase, Supabase and Prisma all use PGlite as a development database. It's proper Postgres that can run embedded, in-process. So you don't need any external processes or system packages to use it.

Having a Postgres database is as simple as:

```shell
npm install @electric-sql/pglite
```

```ts
import { PGlite } from '@electric-sql/pglite'

const db = new PGlite()
```

### Database in the sandbox

AI app builders like Bolt, Lovable and Replit can generate database-driven apps and run them in a sandboxed dev environment. However, to actually work, these apps need to connect to a database.

PGlite is a Postgres database that runs inside your dev environment. With it, you can one-shot database-driven apps that run without leaving the sandbox.

### Hydrating PGlite

Electric can be used to hydrate data into a PGlite instance using the [sync plugin](https://pglite.dev/docs/sync):

```ts
import { electricSync } from '@electric-sql/pglite-sync'

const pg = await PGlite.create({
  extensions: {
    electric: electricSync(),
  },
})
```

This supports individual tables and transactionally [syncing multiple tables](https://pglite.dev/docs/sync#syncshapestotables-api).

#### More information

* [PGlite website](https://pglite.dev) and [docs](https://pglite.dev/docs)
* [LinearLite demo](/demos/linearlite) using PGlite with Electric
* [Database.build](https://database.build/) by Supabase (running on PGlite)
* [Vibe coding with a database in the sandbox](/blog/2025/06/05/database-in-the-sandbox)

## &#x20;Yjs

| Database | Client | Writes |
| -------- | ------ | ------ |
| Postgres | Yjs    | Yjs    |

[Yjs](https://docs.yjs.dev) is a library for building collaborative applications.

### Conflict-free updates

Electric can be used as a transport layer with Yjs to create collaborative, multi-user applications on top of Postgres.

### Multi-user collaboration

This works by exposing a [Shape](/docs/guides/shapes) to sync changes for a [Y.Doc](https://docs.yjs.dev/api/y.doc). The `y-electric` package then automatically shares updates across all connected clients.

#### More information

* [Integration docs](/docs/integrations/yjs)
* [Notes demo](/demos/notes)
* [`y-electric` package](https://github.com/electric-sql/electric/tree/main/packages/y-electric)
