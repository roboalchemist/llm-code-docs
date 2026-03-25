# Zenoh Storage Manager Plugin: Complete Guide

The storage manager is Zenoh's built-in persistence layer. It bridges data-in-motion (pub/sub) to
data-at-rest (databases, filesystems, memory) by acting simultaneously as a **subscriber** (receiving
puts and deletes) and a **queryable** (answering `get` queries from the rest of the network).

---

## Table of Contents

1. [What the Storage Manager Does](#what-the-storage-manager-does)
2. [Volume vs Storage: The Core Distinction](#volume-vs-storage-the-core-distinction)
3. [Plugin Loading](#plugin-loading)
4. [All Configuration Options](#all-configuration-options)
   - [Top-level plugin options](#top-level-plugin-options)
   - [Volume options](#volume-options)
   - [Storage options](#storage-options)
   - [Garbage collection options](#garbage-collection-options)
   - [Replication options](#replication-options)
5. [Replication Deep Dive](#replication-deep-dive)
6. [Admin Space Queries](#admin-space-queries)
7. [Example Configurations](#example-configurations)
8. [Code Examples](#code-examples)

---

## What the Storage Manager Does

When the storage manager plugin is loaded, every configured **storage** does two things
simultaneously:

1. **Declares a subscriber** on its `key_expr`. Every `put` and `delete` published on the network
   that matches the key expression is received and forwarded to the backend for persistence.

2. **Declares a queryable** on the same `key_expr`. Any `get` request matching the key expression
   causes the storage to be queried, and stored values are returned as replies. Setting
   `complete: true` advertises that this storage claims to hold *all* keys in the namespace, which
   affects how Zenoh routes consolidating queries.

The result: a storage makes the key-space it covers **persistent and queriable** — any peer that
was offline when a value was published can still retrieve it later.

### The Timestamp Requirement

The storage manager refuses to start if the `timestamping` setting is disabled in the Zenoh
configuration. Every sample stored must carry an HLC timestamp; without the HLC there is no way to
resolve ordering for replication and last-write-wins conflict resolution. Ensure your config
includes:

```json5
timestamping: {
  enabled: { router: true, peer: true, client: false },
}
```

---

## Volume vs Storage: The Core Distinction

**Volume** — a running instance of a backend library. Think of it as an open database connection:
one RocksDB directory, one InfluxDB endpoint, one in-process memory map. The volume's job is to
`create_storage()` on demand.

**Storage** — a logical namespace layered over a volume. It maps a Zenoh key expression to a
section of the volume. One volume can back arbitrarily many storages. One storage cannot span
multiple volumes.

```
Zenoh network
      │  (put / delete / get)
      ▼
Storage Manager Plugin
  ├── Volume: "memory"          ← built-in, always present
  │     ├── Storage: "demo"     key_expr = "demo/**"
  │     └── Storage: "sensors"  key_expr = "sensors/**"
  │
  └── Volume: "rocks"           ← loaded from libzenoh_backend_rocksdb.so
        └── Storage: "archive"  key_expr = "archive/**"
```

Backend library naming: the plugin system searches for a shared library named
`libzenoh_backend_{name}.so` / `libzenoh_backend_{name}.dylib` / `zenoh_backend_{name}.dll`.
For example, a volume with `backend: "rocksdb"` loads `libzenoh_backend_rocksdb`.

---

## Plugin Loading

### As a zenohd built-in

```json5
plugins_loading: {
  enabled: true,
  search_dirs: ["/usr/local/lib/zenoh-plugins"],
},
plugins: {
  storage_manager: {
    // ... config ...
  },
}
```

### Via explicit library path

```json5
plugins: {
  storage_manager: {
    __path__: [
      "./target/release/libzenoh_plugin_storage_manager.so",
      "./target/release/libzenoh_plugin_storage_manager.dylib",
    ],
    // ... config ...
  },
}
```

---

## All Configuration Options

### Top-level plugin options

These sit directly inside `plugins.storage_manager { ... }`.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `__path__` | `string \| string[]` | _(auto-search)_ | Explicit path(s) to the plugin shared library. When set, auto-search is disabled. |
| `__required__` | `bool` | `true` | If `true`, zenohd exits when the plugin fails to load. |
| `backend_search_dirs` | `string \| string[]` | `[]` | Directories searched when loading volume backend libraries by name. Backends declared via `__path__` are not subject to this search. |
| `volumes` | `object` | `{}` | Map of named volume configurations. The built-in `"memory"` volume is always available without declaring it here. |
| `storages` | `object` | `{}` | Map of named storage configurations. |

---

### Volume options

Volumes are declared as keys under `volumes: { <volume_name>: { ... } }`.

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| _(key)_ | string | — | The **volume name**. This is the identifier referenced by storages via their `volume` field. |
| `backend` | `string \| null` | _(same as volume name)_ | Which backend library to load. Resolved to `libzenoh_backend_{backend}`. If omitted, the volume name is used as the backend name. Use this when you need two volumes from the same backend (e.g., two separate InfluxDB connections). |
| `__path__` | `string \| string[]` | _(auto-search)_ | Explicit path(s) to the backend shared library. |
| `__required__` | `bool` | `true` | If `true`, zenohd exits when this volume fails to load. Set to `false` to make a volume optional. |
| `private` | `object` | — | A sub-object whose contents are hidden from the admin space. Use for passwords and tokens. Any key nested under `private` is passed to the backend but never returned in introspection queries. |
| _(any other key)_ | — | — | Backend-specific configuration. Passed verbatim to the backend's `start()` function. Common examples: `url`, `db`, `dir`. |

**Example — two InfluxDB volumes from the same backend library:**

```json5
volumes: {
  influxdb_prod: {
    backend: "influxdb",
    url: "https://influx.prod.example.com",
    private: {
      token: "prod-token-here",
    },
  },
  influxdb_dev: {
    backend: "influxdb",
    url: "http://localhost:8086",
    private: {
      token: "dev-token-here",
    },
  },
},
```

---

### Storage options

Storages are declared as keys under `storages: { <storage_name>: { ... } }`.

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| _(key)_ | string | yes | — | The **storage name**. Used in admin space paths. |
| `key_expr` | string (key expression) | yes | — | The Zenoh key expression this storage subscribes to and answers queries for. Wildcards (`*`, `**`) are allowed. Must be a valid key expression (no double slashes, etc.). |
| `volume` | `string \| { id: string, ...extras }` | yes | — | Which volume backs this storage. Either a bare string (the volume name), or an object with `id` (the volume name) plus any volume-specific per-storage options the backend needs (e.g., `db: "mydb"` for InfluxDB). |
| `complete` | `bool \| "true" \| "false"` | no | `false` | Whether this storage advertises itself as complete for its key expression. A complete storage tells Zenoh routers it holds *all* matching keys, affecting how consolidating `get` queries are routed. |
| `strip_prefix` | `string` | no | _(none)_ | A key expression prefix to strip from keys before passing them to the backend. Must be a non-wildcard prefix of `key_expr`. If a published key equals the prefix exactly, the storage receives `None` as the key (the backend must handle this). **⚠️ Must be identical across all replicas of this storage.** |
| `garbage_collection` | `object` | no | _(defaults below)_ | Configuration for periodic GC of internal metadata (wildcard tombstones, latest-update cache). |
| `replication` | `object \| null` | no | `null` | When present, enables replication with other storage instances on the same key expression. See replication options below. |

**`volume` as a string (simple case):**

```json5
storages: {
  my_storage: {
    key_expr: "sensors/**",
    volume: "memory",
  },
}
```

**`volume` as an object (backend-specific options per-storage):**

```json5
storages: {
  influx_demo: {
    key_expr: "demo/influxdb/**",
    strip_prefix: "demo/influxdb",
    volume: {
      id: "influxdb_prod",
      db: "example_db",     // InfluxDB-specific: which database bucket to use
    },
  },
}
```

---

### Garbage collection options

Located at `storages.<name>.garbage_collection { ... }`.

The storage manager maintains in-memory metadata for wildcard updates and deletes (tombstones) plus
a latest-update cache. These are periodically purged to prevent unbounded memory growth.

| Option | Type | Default | Unit | Description |
|--------|------|---------|------|-------------|
| `period` | `integer` | `30` | seconds | How often the GC event fires. Metadata is inspected and pruned every `period` seconds. |
| `lifespan` | `integer` | `86400` | seconds | Metadata older than this many seconds is eligible for collection. Default is 24 hours. |

**Example:**

```json5
garbage_collection: {
  period: 60,       // run GC every minute
  lifespan: 3600,   // discard metadata older than 1 hour
},
```

---

### Replication options

Located at `storages.<name>.replication { ... }`.

Replication is optional. When a `replication` block is present, the storage joins an
anti-entropy synchronization group with any other storage instances that share the same
`key_expr` (and the same replication fingerprint, which is a hash of the key expression,
strip_prefix, and all replication parameters).

**⚠️ All replicas that should stay aligned MUST have identical values for every replication
parameter.** Mismatched parameters produce a different fingerprint, causing replicas to silently
ignore each other's digests.

| Option | Type | Default | Unit | Description |
|--------|------|---------|------|-------------|
| `interval` | `float` | `10.0` | seconds | Time between digest publication cycles. Controls the maximum time two replicas may diverge before convergence is attempted. Larger values reduce network overhead; smaller values reduce convergence latency. |
| `sub_intervals` | `integer` | `5` | count | Number of equal-length sub-intervals within each interval. Each sub-interval gets its own fingerprint. Higher values increase digest size but reduce the data transferred during alignment; lower values reduce digest size but increase alignment data. |
| `hot` | `integer` | `6` | intervals | Number of intervals in the "hot" era. With defaults: `6 × 10s = 60s`. Events within the hot era are tracked with the finest granularity (per sub-interval). |
| `warm` | `integer` | `30` | intervals | Number of intervals in the "warm" era. With defaults: `30 × 10s = 300s = 5min`. Events in the warm era are tracked at interval granularity. Events older than hot+warm intervals are in the "cold" era and tracked as a single aggregate fingerprint. |
| `propagation_delay` | `integer` | `250` | milliseconds | Estimated time for a publication to propagate to all storage replicas. The digest is published at `(n × interval) + propagation_delay` seconds to ensure all publications that belong to interval `n` have arrived before the digest for that interval is computed. **Constraint:** `propagation_delay` must be less than `interval / 2`. |

**Example with custom values:**

```json5
replication: {
  interval: 5.0,           // sync every 5 seconds
  sub_intervals: 10,       // 10 sub-intervals per interval
  hot: 12,                 // hot era = last 60 seconds
  warm: 60,                // warm era = last 300 seconds
  propagation_delay: 100,  // assume 100ms network latency
},
```

---

## Replication Deep Dive

### How convergence works

The replication system uses a three-tier anti-entropy protocol inspired by Merkle trees:

1. **Digest publication**: Every `interval + propagation_delay` seconds, each replica computes a
   *digest* — a compact fingerprint summary of everything it has stored, bucketed by time. It
   publishes the digest on a well-known internal key expression derived from the storage's
   `key_expr` and fingerprint.

2. **Digest subscription**: Each replica subscribes to the same digest key expression. When a
   foreign digest arrives, the replica compares it against its own digest.

3. **Aligner queryable/query**: When a mismatch is detected, the replica that is missing data
   queries the other replica's *aligner queryable*. The aligner responds with only the samples
   that are missing, avoiding full-dataset transfer.

### Time eras

The digest divides history into three eras to balance precision and overhead:

- **Hot era** (most recent `hot × interval` seconds): Tracked per sub-interval. Fine-grained
  detection of recent divergence. Fingerprints are recomputed each cycle.
- **Warm era** (the preceding `warm × interval` seconds): Tracked per interval. Coarser but still
  distinguishes which time bucket diverged.
- **Cold era** (everything older): Tracked as a single aggregate fingerprint. Only a full cold-era
  mismatch triggers a cold scan.

### Initial alignment

When a newly started storage is empty and detects an existing replica on the network, it skips the
digest exchange and performs an **initial alignment** — a single bulk query to the replica's aligner
to fetch its entire content. This is more efficient than iterative digest comparison for a cold start.

### Conflict resolution

Zenoh uses last-writer-wins based on HLC timestamps. Every sample must carry a timestamp (enforced
by requiring `timestamping` to be enabled). If two replicas receive conflicting writes to the same
key, the one with the newer timestamp wins. The storage backend receives `StorageInsertionResult::Outdated`
when it tries to store a sample that is older than what it already has.

### Wildcard updates

A `put` or `delete` with a wildcard key expression (`*` or `**`) is stored in a separate in-memory
wildcard cache alongside the normal per-key store. When a concrete key arrives, the storage checks
whether a wildcard update with a newer timestamp overrides it. This ensures wildcard deletes act as
tombstones that are correctly propagated even when concrete keys arrive out of order.

---

## Admin Space Queries

The storage manager exposes its runtime state through the Zenoh [admin space](admin-space-guide.md) — a special key namespace rooted at `@/`. The admin space is queried with regular `session.get()` calls; no special API is needed.

### Admin space key format

```
@/{router_zid}/{whatami}/status/plugins/{plugin_name}
```

Where `{whatami}` is `router`, `peer`, or `client`. For the storage manager plugin (default name
`storage_manager`):

```
@/{router_zid}/router/status/plugins/storage_manager
```

Sub-paths exposed by the storage manager:

| Path | Content |
|------|---------|
| `.../status/plugins/storage_manager/version` | Plugin version string |
| `.../status/plugins/storage_manager/volumes/{volume_name}` | Volume admin status (JSON) |
| `.../status/plugins/storage_manager/volumes/{volume_name}/__path__` | Path of the loaded backend library |
| `.../status/plugins/storage_manager/storages/{storage_name}` | Storage admin status (JSON, from backend) |

Use wildcards to query across all routers or all volumes/storages.

### Rust examples

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // List all storages on any router
    let replies = session
        .get("@/*/router/status/plugins/storage_manager/storages/*")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            println!("Storage: {}  status: {}", sample.key_expr(), sample.payload().try_to_string().unwrap_or_default());
        }
    }

    // List all volumes on any router
    let replies = session
        .get("@/*/router/status/plugins/storage_manager/volumes/*")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            println!("Volume: {}  status: {}", sample.key_expr(), sample.payload().try_to_string().unwrap_or_default());
        }
    }
}
```

### Python examples

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    # List all storages
    replies = session.get("@/*/router/status/plugins/storage_manager/storages/*")
    for reply in replies:
        if reply.ok:
            s = reply.ok
            print(f"Storage: {s.key_expr}  status: {bytes(s.payload).decode()}")

    # List all volumes
    replies = session.get("@/*/router/status/plugins/storage_manager/volumes/*")
    for reply in replies:
        if reply.ok:
            s = reply.ok
            print(f"Volume: {s.key_expr}  status: {bytes(s.payload).decode()}")
```

### Notes on admin space

- The admin space is served by the router's own session; a remote session can query it if it has
  connectivity to the router.
- The value returned for a storage is whatever the backend's `get_admin_status()` returns — for
  the built-in memory backend this is the `StorageConfig` serialized as JSON.
- The `__path__` sub-key for a volume returns the filesystem path of the loaded `.so`/`.dylib`.
- If the router uses a non-default plugin name (e.g., `plugins.my_storages`), replace
  `storage_manager` with that name in the query path.

---

## Example Configurations

### 1. In-memory storage (no backend library required)

The `memory` volume is built in and always available. No `volumes` declaration needed.

```json5
{
  timestamping: {
    enabled: { router: true, peer: true, client: false },
  },
  plugins: {
    storage_manager: {
      storages: {
        // Store everything under demo/ in memory
        demo: {
          key_expr: "demo/**",
          volume: "memory",
        },
        // Sensor readings, complete=true to serve all-keys queries
        sensors: {
          key_expr: "sensors/**",
          volume: "memory",
          complete: true,
        },
      },
    },
  },
}
```

### 2. Single storage with filesystem backend

Assumes `libzenoh_backend_filesystem.so` is on the library search path or in `backend_search_dirs`.

```json5
{
  timestamping: {
    enabled: { router: true, peer: true, client: false },
  },
  plugins: {
    storage_manager: {
      backend_search_dirs: ["/usr/local/lib/zenoh-backends"],
      volumes: {
        fs: {
          // Loads libzenoh_backend_filesystem (name matches volume name)
          dir: "/var/zenoh-data",   // backend-specific: root directory
        },
      },
      storages: {
        telemetry: {
          key_expr: "telemetry/**",
          strip_prefix: "telemetry",
          volume: "fs",
          complete: true,
          garbage_collection: {
            period: 60,
            lifespan: 604800,    // keep metadata 7 days
          },
        },
      },
    },
  },
}
```

### 3. Multiple storages on one volume (different key expression prefixes)

Both storages share the same `fs` volume (same backend instance) but cover different namespaces.

```json5
{
  timestamping: {
    enabled: { router: true, peer: true, client: false },
  },
  plugins: {
    storage_manager: {
      backend_search_dirs: ["/usr/local/lib/zenoh-backends"],
      volumes: {
        fs: {
          dir: "/var/zenoh-data",
        },
      },
      storages: {
        // Storage A: covers camera frames
        cameras: {
          key_expr: "cameras/**",
          strip_prefix: "cameras",
          volume: "fs",
          complete: true,
        },
        // Storage B: covers door sensor readings
        doors: {
          key_expr: "doors/**",
          strip_prefix: "doors",
          volume: "fs",
          complete: true,
        },
        // Storage C: covers all alerts, no strip_prefix
        alerts: {
          key_expr: "alerts/**",
          volume: "fs",
        },
      },
    },
  },
}
```

> Both `cameras` and `doors` use the same `fs` volume, so the same backend instance handles both.
> Each storage strips its own prefix, so keys are stored without the namespace prefix in the
> backend. `alerts` does not strip a prefix, so the full key is passed to the backend.

### 4. Replicated storage pair

Two routers each run this config. The storage manager on each router will discover the other and
keep them synchronized.

**Both routers must use this identical config** (especially the `replication` block):

```json5
{
  timestamping: {
    enabled: { router: true, peer: true, client: false },
  },
  plugins: {
    storage_manager: {
      storages: {
        replicated_sensors: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",
          volume: "memory",
          complete: true,
          garbage_collection: {
            period: 30,
            lifespan: 86400,
          },
          replication: {
            interval: 10.0,
            sub_intervals: 5,
            hot: 6,
            warm: 30,
            propagation_delay: 250,
          },
        },
      },
    },
  },
}
```

**What happens at startup:**
1. Router A starts with an empty storage and publishes its (empty) digest.
2. Router B starts with an empty storage and also publishes its digest.
3. Both are empty, so no alignment occurs initially.
4. As data arrives via `put`, each router stores it and the digests diverge if a router missed a
   publication.
5. Every 10.25 seconds (10.0s interval + 0.25s propagation delay) each router compares digests with
   the other and queries for any missing samples.

**For a cold-start where one router already has data:**
- The new router, on startup with an empty storage, performs an **initial alignment**: a single bulk
  query to the existing router to fetch its entire storage contents before starting the periodic
  digest cycle.

---

## Code Examples

### Rust: implementing a basic in-process storage

This uses the same pattern as the built-in `z_storage` example — no plugin loading, just the dual
subscriber+queryable pattern in application code:

```rust
use std::collections::HashMap;
use futures::select;
use zenoh::{key_expr::KeyExpr, sample::SampleKind, Config};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let key_expr = "demo/example/**";
    let mut stored: HashMap<String, zenoh::sample::Sample> = HashMap::new();

    let subscriber = session.declare_subscriber(key_expr).await.unwrap();
    let queryable = session
        .declare_queryable(key_expr)
        .complete(true)   // advertise as complete for this key expression
        .await
        .unwrap();

    loop {
        select!(
            sample = subscriber.recv_async() => {
                let sample = sample.unwrap();
                match sample.kind() {
                    SampleKind::Put => {
                        stored.insert(sample.key_expr().to_string(), sample);
                    }
                    SampleKind::Delete => {
                        stored.remove(&sample.key_expr().to_string());
                    }
                }
            },
            query = queryable.recv_async() => {
                let query = query.unwrap();
                for (key, sample) in &stored {
                    if query.key_expr().intersects(
                        zenoh::key_expr::keyexpr::new(key).unwrap()
                    ) {
                        query.reply(sample.key_expr().clone(), sample.payload().clone())
                            .await
                            .unwrap();
                    }
                }
            },
        );
    }
}
```

### Rust: querying data from a storage

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // Get all values under sensors/
    let replies = session.get("sensors/**").await.unwrap();

    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                let value = sample.payload().try_to_string().unwrap_or_default();
                println!("{} = {}", sample.key_expr(), value);
            }
            Err(err) => eprintln!("Error: {:?}", err),
        }
    }
}
```

### Python: putting and getting via a configured storage

```python
import zenoh
import time

config = zenoh.Config.from_file("zenoh-config.json5")  # config with storage_manager enabled

with zenoh.open(config) as session:
    # Put some values — the storage manager will store them
    for i in range(5):
        session.put(f"sensors/temperature/{i}", f"{20 + i}".encode())

    time.sleep(0.1)  # let the storage process the puts

    # Query them back — the storage queryable answers
    replies = session.get("sensors/temperature/**")
    for reply in replies:
        if reply.ok:
            s = reply.ok
            print(f"{s.key_expr} = {bytes(s.payload).decode()}")
```

### Python: introspecting storage manager via admin space

```python
import zenoh
import json

with zenoh.open(zenoh.Config()) as session:
    # Discover all storage manager instances and their storages
    replies = session.get("@/*/router/status/plugins/storage_manager/storages/*")
    for reply in replies:
        if reply.ok:
            sample = reply.ok
            try:
                status = json.loads(bytes(sample.payload))
                print(f"Storage at {sample.key_expr}:")
                print(f"  key_expr: {status.get('key_expr')}")
                print(f"  volume:   {status.get('volume')}")
                print(f"  complete: {status.get('complete', False)}")
            except Exception:
                print(f"Storage at {sample.key_expr}: {bytes(sample.payload)}")
```

---

## Summary: Config Quick Reference

```json5
plugins: {
  storage_manager: {
    // Optional: where to find backend .so/.dylib files
    backend_search_dirs: ["/path/to/backends"],


    // Volumes: named backend instances
    volumes: {
      <volume_name>: {
        backend: "<backend_lib_name>",  // optional, defaults to volume_name
        __required__: true,             // optional, default true
        private: { password: "..." },   // hidden from admin space
        // ... backend-specific options ...
      },
    },

    // Storages: named logical namespaces backed by a volume
    storages: {
      <storage_name>: {
        key_expr: "path/to/**",           // required
        volume: "<volume_name>",           // required (string or {id, ...extras})
        complete: false,                   // optional, default false
        strip_prefix: "path/to",          // optional, no wildcards allowed

        garbage_collection: {             // optional
          period: 30,                     // seconds, default 30
          lifespan: 86400,                // seconds, default 86400 (24h)
        },

        replication: {                    // optional; enables anti-entropy sync
          interval: 10.0,                 // seconds (float), default 10.0
          sub_intervals: 5,               // integer, default 5
          hot: 6,                         // intervals, default 6
          warm: 30,                       // intervals, default 30
          propagation_delay: 250,         // milliseconds, default 250
        },
      },
    },
  },
},
```

## See Also

- [Storage Backends Guide](storage-backends-guide.md) — comparison of all backend types (in-memory, filesystem, RocksDB, InfluxDB, S3) with selection guidance
- [Plugin InfluxDB Guide](plugin-influxdb-guide.md) — InfluxDB-specific configuration, time-series queries, and v1 vs v2 differences
- [Plugin RocksDB Guide](plugin-rocksdb-guide.md) — RocksDB backend configuration, crash recovery, and performance characteristics
- [Plugin S3 Guide](plugin-s3-guide.md) — S3 backend configuration for AWS, MinIO, and compatible object stores
- [Plugin Filesystem Guide](plugin-filesystem-guide.md) — filesystem backend configuration for human-readable key/value storage
- [Admin Space Guide](admin-space-guide.md) — how to query storage status and manage storages at runtime via the admin space
