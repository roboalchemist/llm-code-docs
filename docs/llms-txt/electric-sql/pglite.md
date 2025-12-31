# Source: https://electric-sql.com/product/pglite.md

---
url: /product/pglite.md
description: 'Sync into a lightweight WASM Postgres with real-time, reactive bindings.'
---

# PGlite&#x20;

Sync into a lightweight WASM Postgres with
real-time, reactive bindings.

## Lightweight WASM Postgres

PGlite is a lightweight WASM Postgres build, packaged into a TypeScript library for the browser, Node.js, Bun and Deno. PGlite allows you to run Postgres in JavaScript, with no need to install any other dependencies. It is under 3MB gzipped.

```ts
import { PGlite } from '@electric-sql/pglite'

const db = new PGlite()
await db.query("select 'Hello world' as message;")
// -> { rows: [ { message: "Hello world" } ] }
```

Unlike previous "Postgres in the browser" projects, PGlite does not use a Linux virtual machine - it is simply Postgres in WASM, compiled directly in single-user mode.

It can be used as an ephemeral [in-memory database](https://pglite.dev/docs/filesystems#in-memory-fs), or with persistence either to the [filesystem](https://pglite.dev/docs/filesystems#node-fs) (Node/Bun) or [indexedDB](https://pglite.dev/docs/filesystems#indexeddb-fs) (in the browser). It's:

* **extendable**, with [dynamic extension loading](https://pglite.dev/extensions/), including support for [pgvector](https://pglite.dev/extensions/#pgvector)
* **reactive** with built in support for [sync](https://pglite.dev/docs/sync) and [live query](https://pglite.dev/docs/live-queries) primitives

### Syncing into PGlite

You can use [Electric](/product/electric) to sync between a cloud Postgres and an embedded PGlite instance. For example, to sync an `items` [Shape](/docs/guides/shapes) into an `items` table:

<<< @/src/partials/sync-into-pglite.tsx

## More information

See the PGlite website at [pglite.dev](https://pglite.dev) for comprehensive [Docs](https://pglite.dev/docs/), a list of [Examples](https://pglite.dev/examples) and a [live in-browser REPL](https://pglite.dev/repl/). The source code is on GitHub at [electric-sql/pglite](https://github.com/electric-sql/pglite).
