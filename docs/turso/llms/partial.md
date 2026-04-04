# Source: https://docs.turso.tech/sync/partial.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Partial sync

> Sync only what you need. Faster cold starts and lower bandwidth by lazily fetching database pages on demand.

<Note>
  This particular usage uses the Turso Cloud to sync the local Turso databases and assumes that you have an account.
</Note>

Partial sync lets your app open and use a database without downloading the entire file.
The client lazily fetches pages of the database file from the Turso Cloud when a query touches data that is not present locally.
This reduces startup time and network usage for large databases, while remaining fully compatible with the push/pull methods used
by Turso's standard `sync` solution.

<Note>
  * Reads on not-yet-downloaded data transparently trigger on-demand page fetches.
  * Writes still apply locally first and are pushed as logical statements.
</Note>

## Modes

Two bootstrap strategies define what is present locally at connect time:

* **Prefix bootstrap**: download the first N bytes of the database file.
  * Good default when you want a minimal, predictable starting footprint.
* **Query bootstrap**: download pages touched by running a server-side SQL query.
  * Ideal to hydrate only a narrow working set (e.g., a single user's rows, small tables with metadata, references, etc).

Both modes continue to lazily fetch missing pages on demand.

### Prefix bootstrap

<CodeGroup>
  ```ts TypeScript theme={null}
  import { connect } from '@tursodatabase/sync';

  const db = await connect({
    path: './app.db',
    url: 'libsql://...',
    authToken: process.env.TURSO_AUTH_TOKEN,
    partialSync: {
      bootstrapStrategy: { kind: 'prefix', length: 128 * 1024 }, // 128 KiB
    },
  });
  ```

  ```py Python theme={null}
  import os
  import turso.sync

  conn = turso.sync.connect(
      path="./app.db",
      remote_url="libsql://...",
      remote_auth_token=os.environ["TURSO_AUTH_TOKEN"],
      partial_sync_opts=turso.sync.PartialSyncOpts(
          bootstrap_strategy=turso.sync.PartialSyncPrefixBootstrap(length=128 * 1024),
      ),
  )
  ```

  ```go Go theme={null}
  import (
  	"turso"
  )

  db, err := turso.NewTursoSyncDb(context.Background(), turso.TursoSyncDbConfig{
    Path:            "./app.db",
    RemoteUrl:       "libsql://...",
    RemoteAuthToken: os.Getenv("TURSO_AUTH_TOKEN"),
    PartialSyncConfig: turso.TursoPartialSyncConfig{
      BoostrapStrategyPrefix: 128 * 1024, // 128 KiB
    },
  })
  ```
</CodeGroup>

### Query bootstrap

<CodeGroup>
  ```ts TypeScript theme={null}
  import { connect } from '@tursodatabase/sync';

  const db = await connect({
    path: './app.db',
    url: 'libsql://...',
    authToken: process.env.TURSO_AUTH_TOKEN,
    partialSync: {
      bootstrapStrategy: {
        kind: 'query',
        query: `SELECT * FROM messages WHERE user_id = 'u_123' LIMIT 100`,
      },
    },
  });
  ```

  ```py Python theme={null}
  import turso.sync

  conn = turso.sync.connect(
      path=":memory:",
      remote_url="libsql://...",
      partial_sync_opts=turso.sync.PartialSyncOpts(
          bootstrap_strategy=turso.sync.PartialSyncQueryBootstrap(
              query="SELECT * FROM messages WHERE user_id = 'u_123' LIMIT 100"
          ),
      ),
  )
  ```

  ```go Go theme={null}
  import (
  	"turso"
  )

  db, err := turso.NewTursoSyncDb(context.Background(), turso.TursoSyncDbConfig{
    Path:            "./app.db",
    RemoteUrl:       "libsql://...",
    RemoteAuthToken: os.Getenv("TURSO_AUTH_TOKEN"),
    PartialSyncConfig: turso.TursoPartialSyncConfig{
      BoostrapStrategyQuery: "SELECT * FROM messages WHERE user_id = 'u_123' LIMIT 100",
    },
  })
  ```
</CodeGroup>

## Optimizations

### Segment size (batched lazy reads)

<Frame>
    <img src="https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/segment_size.png?fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=1de2b109e1c94210991f3958e59f93e0" alt="segment size" data-og-width="789" width="789" data-og-height="261" height="261" data-path="images/sync/segment_size.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/segment_size.png?w=280&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=cc6416fa7d9916df54b4e789374a3a3b 280w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/segment_size.png?w=560&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=8adee1fc28e31db44531da1d485cff3d 560w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/segment_size.png?w=840&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=3b5fdb3e77e8c318cfac5fa59cf45161 840w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/segment_size.png?w=1100&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=7ed2c89c2b5ef8f24fd327525b99ed50 1100w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/segment_size.png?w=1650&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=b8c46d28798fd2c3623aeaec652f1350 1650w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/segment_size.png?w=2500&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=dac2d272cfc161d8ef802672cf7449a4 2500w" />
</Frame>

When the client needs a page that isn’t present locally, partial sync performs an on-demand fetch from the remote database.
To reduce round-trips and speed up these fetches, you can configure the **segment size**: instead of requesting a single page, the client downloads a whole *segment* of pages in one request.

This lets the client amortize network overhead and hydrate nearby pages that are likely to be accessed soon.

**How it works**

Suppose your database has:

* `page_size = 4 KiB`
* `segment_size = 16 KiB`

If a local query touches page **6**, the client computes the segment that page belongs to:

* 16 KiB segment = 4 pages
* Segment covering page 6 = pages **5-8**

The client then fetches all four pages in a single request and stores them locally.
Future reads to those pages incur no additional network cost.

**Benefits**

* Fewer HTTP requests (one segment fetch vs. many single-page fetches)
* Faster hydration of hot ranges
* Better performance for workloads with spatial locality (e.g., range scans, index lookups)

**Default**

The default `segment_size` is **128 KiB** (typically 32 pages on a 4 KiB page size), which provides a good balance between request overhead and total bytes transferred.

<Tip>
  If your workload touches data in tight clusters (e.g., reading several adjacent rows), larger segment sizes can significantly improve performance.

  Conversely, very sparse/random-access workloads may benefit from smaller segment sizes.
</Tip>

<CodeGroup>
  ```ts TypeScript theme={null}
  await connect({
    ...
    partialSync: {
      bootstrapStrategy: { kind: 'prefix', length: 128 * 1024 }, // 128 KiB
      segmentSize: 16 * 1024,
    },
  });
  ```

  ```py Python theme={null}
  turso.sync.connect(
      ...
      partial_sync_opts=turso.sync.PartialSyncOpts(
          bootstrap_strategy=turso.sync.PartialSyncPrefixBootstrap(length=128 * 1024),
          segment_size=16 * 1024,
      ),
  )
  ```

  ```go Go theme={null}
  turso.NewTursoSyncDb(context.Background(), turso.TursoSyncDbConfig{
    ...
    PartialSyncConfig: turso.TursoPartialSyncConfig{
      BoostrapStrategyPrefix: 128 * 1024, // 128 KiB
      SegmentSize: 16 * 1024,
    },
  })
  ```
</CodeGroup>

### Prefetch

<Frame>
    <img src="https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/prefetch.png?fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=43b54c3397bd649dba217163b4d1eaf5" alt="prefetch" data-og-width="1127" width="1127" data-og-height="261" height="261" data-path="images/sync/prefetch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/prefetch.png?w=280&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=7928cec43f022d8c6660c0443bcb9bb7 280w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/prefetch.png?w=560&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=6033f28c8bc60ce5b62f07e6199552ad 560w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/prefetch.png?w=840&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=cd7a96917b89e3c6f9fd9d2789887a64 840w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/prefetch.png?w=1100&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=53f549da3b43c9cfb8d2ece6cc4a8f09 1100w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/prefetch.png?w=1650&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=75c2a48585b3991af298b782a81e888f 1650w, https://mintcdn.com/turso/A4cYzwt3gj7_8XXR/images/sync/prefetch.png?w=2500&fit=max&auto=format&n=A4cYzwt3gj7_8XXR&q=85&s=1576f8a31249a193396f63358899c1b4 2500w" />
</Frame>

Prefetch is an optional optimization that builds on top of lazy page fetches.
When enabled, the client not only retrieves the pages required by the current query, but also **inspects the structure of the newly downloaded pages and recent access patterns** to predict which pages are likely to be needed next.

If the client detects a natural continuation of the access pattern — such as child pages referenced by an internal B-tree node — it proactively downloads those pages in advance.
This reduces the number of future on-demand fetches and helps avoid stalls during operations like range scans, index walks, or sequential lookups.

<CodeGroup>
  ```ts TypeScript theme={null}
  await connect({
    ...
    partialSync: {
      bootstrapStrategy: { kind: 'prefix', length: 128 * 1024 }, // 128 KiB
      prefetch: true,
    },
  });
  ```

  ```py Python theme={null}
  turso.sync.connect(
      ...
      partial_sync_opts=turso.sync.PartialSyncOpts(
          bootstrap_strategy=turso.sync.PartialSyncPrefixBootstrap(length=128 * 1024),
          prefetch=True,
      ),
  )
  ```

  ```go Go theme={null}
  turso.NewTursoSyncDb(context.Background(), turso.TursoSyncDbConfig{
    ...
    PartialSyncConfig: turso.TursoPartialSyncConfig{
      BoostrapStrategyPrefix: 128 * 1024, // 128 KiB
      Prefetch: true,
    },
  })
  ```
</CodeGroup>

<Note>
  `segment_size` and `prefetch` are complementary.

  Segment size batches nearby pages into a single on-demand fetch, while prefetch looks at the query's access pattern and proactively fetches additional pages likely to be needed next.

  Using both together can provide the best performance for real-world workloads.
</Note>
