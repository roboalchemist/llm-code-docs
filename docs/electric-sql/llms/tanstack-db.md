# Source: https://electric-sql.com/products/tanstack-db.md

---
url: /products/tanstack-db.md
description: >-
  Reactive client store for building super-fast apps. With sub-millisecond
  reactivity and instant local writes.
---

# TanStack DB

Reactive client store for building super-fast apps. With sub-millisecond reactivity and instant local writes.

## What is TanStack DB?

[TanStack DB](https://tanstack.com/db) is a reactive, client-first store that keeps your UI reactive, consistent and blazing fast 🔥

## Why do we need it?

TanStack DB lets you query your data however your components need it, with a blazing-fast local query engine, real-time reactivity and instant optimistic updates:

* avoid endpoint sprawl and network waterfalls
* optimise client performance and re-rendering
* take the network off the interaction path

Data loading is optimized. Interactions feel instantaneous. Your backend stays simple and your app stays blazing fast. No matter how much data you load.

### Use cases

TanStack DB is ideal for:

* modern apps that need fast, responsive UI
* collaborative apps where multiple users edit shared data
* applications combining structured data (via Postgres Sync) with real-time streams (via Durable Streams)
* applications that combine real-time sync with API-based data fetching
* any app that needs a reactive, queryable client-side data store

## How it works

Built on a Typescript implementation of [differential dataflow](https://github.com/electric-sql/d2ts), TanStack DB provides three core primitives:

1. [collections](https://tanstack.com/db/latest/docs/overview#defining-collections) a unified data layer to load data into
2. [live queries](https://tanstack.com/db/latest/docs/guides/live-queries) super-fast reactivity using differential dataflow
3. [optimistic mutations](https://tanstack.com/db/latest/docs/guides/mutations) that tie into the sync machinery

### Data flow

TanStack DB acts as the client-side data layer in [the Electric ecosystem](/products/#how-they-fit-together). Data flows from your backend through Electric's sync primitives into TanStack DB, which then powers your reactive UI components.

You can load and sync data into it from multiple sources, including [your API](https://tanstack.com/blog/tanstack-db-0.1-the-embedded-client-database-for-tanstack-query), [Postgres Sync](/products/postgres-sync) and [Durable Streams](/products/durable-streams).

TanStack DB then provides a unified, reactive interface to the data.

### Query-driven sync

When used with Postgres Sync, TanStack DB leverages [progressive data loading](/docs/guides/shapes#progressive-data-loading) to implement [query-driven sync](https://tanstack.com/blog/tanstack-db-0.5-query-driven-sync).

This means that you can progressively sync data into your app, in response to navigation, user input and events, just by defining live queries against your local client store.

### Learn more

See the blog post on [query-driven sync](https://tanstack.com/blog/tanstack-db-0.5-query-driven-sync) and the [interactive guide to TanStack DB](https://frontendatscale.com/blog/tanstack-db), how it works and why it might change the way you build apps:

## Showcase

See applications built with TanStack DB in the [TanStack Showcase](https://tanstack.com/showcase?page=1\&libraryIds=%5B%22db%22%5D).

## Related posts

## More information

See the [Quickstart](/docs/quickstart) and [TanStack docs](https://tanstack.com/db/latest/docs/overview).
