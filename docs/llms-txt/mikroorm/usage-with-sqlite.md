# Source: https://mikro-orm.io/docs/usage-with-sqlite.md

# Usage with SQLite

MikroORM supports SQLite through dedicated driver packages and a generic `SqliteDriver` that works with any SQLite library via [Kysely dialects](https://kysely.dev/docs/dialects).

## Using `better-sqlite3`[​](#using-better-sqlite3 "Direct link to using-better-sqlite3")

The `@mikro-orm/sqlite` package uses [better-sqlite3](https://github.com/WiseLibs/better-sqlite3) — the fastest SQLite binding for Node.js.

* npm
* Yarn
* pnpm
* Bun

```
npm install @mikro-orm/core @mikro-orm/sqlite
```

```
yarn add @mikro-orm/core @mikro-orm/sqlite
```

```
pnpm add @mikro-orm/core @mikro-orm/sqlite
```

```
bun add @mikro-orm/core @mikro-orm/sqlite
```

```
import { MikroORM } from '@mikro-orm/sqlite';

const orm = await MikroORM.init({
  entities: [...],
  dbName: 'my-database.sqlite3',
});
```

## Using libSQL / Turso[​](#using-libsql--turso "Direct link to Using libSQL / Turso")

The `@mikro-orm/libsql` package uses [libSQL](https://github.com/tursodatabase/libsql) and supports both local databases and remote [Turso](https://docs.turso.tech/introduction) databases.

* npm
* Yarn
* pnpm
* Bun

```
npm install @mikro-orm/core @mikro-orm/libsql
```

```
yarn add @mikro-orm/core @mikro-orm/libsql
```

```
pnpm add @mikro-orm/core @mikro-orm/libsql
```

```
bun add @mikro-orm/core @mikro-orm/libsql
```

```
import { defineConfig } from '@mikro-orm/libsql';

export default defineConfig({
  dbName: process.env.LIBSQL_URL,
  password: process.env.LIBSQL_AUTH_TOKEN,
});
```

To set additional options like `syncUrl` or `syncPeriod`, use the `driverOptions`:

```
import { defineConfig } from '@mikro-orm/libsql';

export default defineConfig({
  dbName: 'local.db',
  password: process.env.LIBSQL_AUTH_TOKEN,
  driverOptions: {
    syncUrl: process.env.LIBSQL_URL,
    syncPeriod: 0.5, // 500ms
  },
});
```

## Using `node:sqlite`[​](#using-nodesqlite "Direct link to using-nodesqlite")

The `@mikro-orm/sql` package provides a generic `SqliteDriver` and a built-in `NodeSqliteDialect` that uses the `node:sqlite` module — no native dependencies required. This works on Node.js 22.5+ and Deno 2.2+.

* npm
* Yarn
* pnpm
* Bun

```
npm install @mikro-orm/core @mikro-orm/sql kysely
```

```
yarn add @mikro-orm/core @mikro-orm/sql kysely
```

```
pnpm add @mikro-orm/core @mikro-orm/sql kysely
```

```
bun add @mikro-orm/core @mikro-orm/sql kysely
```

```
import { MikroORM, SqliteDriver, NodeSqliteDialect } from '@mikro-orm/sql';

const orm = await MikroORM.init({
  driver: SqliteDriver,
  entities: [...],
  dbName: ':memory:',
  driverOptions: new NodeSqliteDialect(':memory:'),
});
```

## Using Cloudflare D1[​](#using-cloudflare-d1 "Direct link to Using Cloudflare D1")

> **Experimental:** D1 support is experimental and has significant limitations. Use with caution.

[Cloudflare D1](https://developers.cloudflare.com/d1/) is a serverless SQLite database. Use the generic `SqliteDriver` with `kysely-d1`:

* npm
* Yarn
* pnpm
* Bun

```
npm install @mikro-orm/core @mikro-orm/sql kysely kysely-d1
```

```
yarn add @mikro-orm/core @mikro-orm/sql kysely kysely-d1
```

```
pnpm add @mikro-orm/core @mikro-orm/sql kysely kysely-d1
```

```
bun add @mikro-orm/core @mikro-orm/sql kysely kysely-d1
```

```
import { MikroORM, SqliteDriver } from '@mikro-orm/sql';
import { D1Dialect } from 'kysely-d1';

export default {
  async fetch(request: Request, env: Env) {
    const orm = await MikroORM.init({
      driver: SqliteDriver,
      entities: [...],
      // the `dbName` is not used when a dialect is provided, but it's still required
      dbName: 'd1',
      driverOptions: new D1Dialect({ database: env.DB }),
      // required: D1 does not support explicit transactions
      implicitTransactions: false,
    });

    // ...
  },
};
```

You can also pass a factory function if you need to create the dialect lazily:

```
driverOptions: () => new D1Dialect({ database: env.DB }),
```

### D1 Limitations[​](#d1-limitations "Direct link to D1 Limitations")

D1 has significant limitations compared to regular SQLite:

* **No transaction support:** D1 does not support explicit transaction statements (`BEGIN TRANSACTION`). You must set `implicitTransactions: false` for `em.flush()` to work. This means changes are not applied atomically - if an error occurs mid-flush, some changes may be persisted while others are not.
* **`em.transactional()` will not work:** Since there's no transaction support, wrapping code in `em.transactional()` provides no atomicity guarantees.
* **No query streaming:** Large result sets cannot be streamed and must be fetched entirely into memory.
* **Limited `ALTER TABLE`:** No support for `ALTER COLUMN` or `ADD CONSTRAINT`, which affects schema migrations.

See the [D1 SQL documentation](https://developers.cloudflare.com/d1/sql-api/sql-statements/) for more details on supported SQL statements.

## Using Bun SQLite[​](#using-bun-sqlite "Direct link to Using Bun SQLite")

Bun has a built-in [high-performance SQLite module](https://bun.sh/docs/api/sqlite) (`bun:sqlite`). Use the generic `SqliteDriver` with the `kysely-bun-sqlite` dialect:

```
bun add @mikro-orm/core @mikro-orm/sql kysely kysely-bun-sqlite
```

```
import { MikroORM, SqliteDriver } from '@mikro-orm/sql';
import { BunSqliteDialect } from 'kysely-bun-sqlite';
import { Database } from 'bun:sqlite';

const orm = await MikroORM.init({
  driver: SqliteDriver,
  entities: [...],
  dbName: 'my-database.sqlite3',
  driverOptions: new BunSqliteDialect({
    database: new Database('my-database.sqlite3'),
  }),
});
```

## Using Turso embedded database[​](#using-turso-embedded-database "Direct link to Using Turso embedded database")

[Turso's embedded database](https://github.com/tursodatabase/turso/tree/main/bindings/javascript) (`@tursodatabase/database`) provides native Rust-based SQLite bindings with a `better-sqlite3`-compatible API. Use the generic `SqliteDriver` with Kysely's built-in `SqliteDialect`:

* npm
* Yarn
* pnpm
* Bun

```
npm install @mikro-orm/core @mikro-orm/sql kysely @tursodatabase/database
```

```
yarn add @mikro-orm/core @mikro-orm/sql kysely @tursodatabase/database
```

```
pnpm add @mikro-orm/core @mikro-orm/sql kysely @tursodatabase/database
```

```
bun add @mikro-orm/core @mikro-orm/sql kysely @tursodatabase/database
```

```
import { MikroORM, SqliteDriver } from '@mikro-orm/sql';
import { SqliteDialect } from 'kysely';
import Database from '@tursodatabase/database/compat';

const orm = await MikroORM.init({
  driver: SqliteDriver,
  entities: [...],
  dbName: 'local.db',
  driverOptions: new SqliteDialect({ database: new Database('local.db') }),
});
```

## Using SQLite extensions[​](#using-sqlite-extensions "Direct link to Using SQLite extensions")

SQLite extensions like [sqlean](https://github.com/nalgeon/sqlean) can add many useful features that are notably missing by default (e.g. regexp).

Once you've downloaded the binaries for the extensions you wish to use, they can be added via the `onCreateConnection` hook:

```
const orm = await MikroORM.init({
  // ...
  onCreateConnection(connection) {
    connection.loadExtension('/.../sqlean-macos-arm64/sqlean');
  },
});
```

## Custom SQLite dialect[​](#custom-sqlite-dialect "Direct link to Custom SQLite dialect")

You can use any SQLite library by passing a [Kysely dialect](https://kysely.dev/docs/dialects) via the `driverOptions` config option:

```
import { MikroORM, SqliteDriver } from '@mikro-orm/sql';

const orm = await MikroORM.init({
  driver: SqliteDriver,
  entities: [...],
  dbName: ':memory:',
  driverOptions: myCustomKyselyDialect,
});
```
