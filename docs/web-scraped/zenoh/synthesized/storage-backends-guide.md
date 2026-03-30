# Zenoh Storage Backends: Complete Comparison Guide

Zenoh's storage subsystem transforms a message bus into a distributed database. A single `session.get()` call can transparently query across multiple heterogeneous backends—RocksDB on an edge device and S3 in the cloud—and receive a unified, deduplicated response. This guide covers all five backend types, their architecture, configuration, and the patterns that make geo-distributed storage practical.

---

## Table of Contents

1. [Storage Manager Architecture](#1-storage-manager-architecture)
2. [Backend Comparison Table](#2-backend-comparison-table)
3. [Transparent Multi-Backend Queries](#3-transparent-multi-backend-queries)
4. [Heterogeneous Replication](#4-heterogeneous-replication)
5. [Geographically Distributed Storage](#5-geographically-distributed-storage)
6. [Fault Tolerance](#6-fault-tolerance)
7. [Backend Deep Dives](#7-backend-deep-dives)
   - [In-Memory](#71-in-memory-backend)
   - [Filesystem](#72-filesystem-backend)
   - [RocksDB](#73-rocksdb-backend)
   - [InfluxDB](#74-influxdb-backend)
   - [S3](#75-s3-backend)
8. [Complete Config Examples](#8-complete-config-examples)
9. [When to Choose Each Backend](#9-when-to-choose-each-backend)

---

## 1. Storage Manager Architecture

The storage manager is a plugin (`zenoh-plugin-storage-manager`) that sits between the Zenoh pub/sub fabric and pluggable storage backends. It introduces two core abstractions: **Volumes** and **Storages**.

### Volumes and Storages

**Volume** = a backend connection. A volume is an instance of a backend driver (memory, filesystem, RocksDB, InfluxDB, or S3) with its own connection parameters. You can have multiple volumes of the same backend type—for example, two InfluxDB volumes pointing to different servers.

**Storage** = a logical namespace. A storage is bound to a volume and subscribes to a key expression. When a publisher puts data to `sensors/factory1/temp`, every storage whose key expression matches receives and stores it.

```
Volume: influxdb-prod  ───────┐
  (url: http://influx:8086)   │
                              ├── Storage: factory-temps
Volume: rocksdb-edge  ────────┘   (key_expr: sensors/**/temp)
  (dir: /var/zenoh/db)
```

### Trait Definitions

All backends implement the `Volume` and `Storage` traits from `zenoh-backend-traits`:

```rust
// A backend implementation (loaded once per volume config)
pub trait Volume: Send + Sync {
    fn get_admin_status(&self) -> JsonValue;
    fn get_capability(&self) -> Capability;
    async fn create_storage(&self, props: StorageConfig) -> ZResult<Box<dyn Storage>>;
}

// A storage instance (one per storage config entry)
pub trait Storage: Send + Sync {
    async fn put(&mut self, key: Option<OwnedKeyExpr>, payload: ZBytes,
                 encoding: Encoding, timestamp: Timestamp) -> ZResult<StorageInsertionResult>;
    async fn delete(&mut self, key: Option<OwnedKeyExpr>, timestamp: Timestamp)
                   -> ZResult<StorageInsertionResult>;
    async fn get(&mut self, key_expr: Option<OwnedKeyExpr>, parameters: &str)
                -> ZResult<Vec<StoredData>>;
    async fn get_all_entries(&self) -> ZResult<Vec<(Option<OwnedKeyExpr>, Timestamp)>>;
}
```

### Capability Model

Each volume declares its capabilities, which affect how the storage manager handles it:

```rust
pub struct Capability {
    pub persistence: Persistence,  // Volatile or Durable
    pub history: History,          // Latest or All
}
```

| Capability | Meaning |
|---|---|
| `Persistence::Volatile` | Data lost on restart (memory backend) |
| `Persistence::Durable` | Data survives restarts (all disk backends) |
| `History::Latest` | Only the most recent value per key is stored |
| `History::All` | All historical values retained (InfluxDB with `_time`) |

> **Replication requires `History::Latest`.** The anti-entropy protocol only works with backends that return a single canonical value per key.

### Storage Service Internals

For each configured storage, the storage manager spawns a `StorageService` that:

1. Declares a **Zenoh subscriber** on the storage's `key_expr` to receive puts/deletes
2. Declares a **Zenoh queryable** on the same `key_expr` to serve get requests
3. Maintains **wildcard put/delete trees** for conflict-free replication
4. Runs a **periodic garbage collector** to purge old deletion tombstones
5. Optionally runs a **replication service** for eventual consistency with peer storages

### Query Routing: The `complete` Flag

Every storage config has a `complete` boolean (default: `false`). This flag tells the router whether this storage holds **all** data matching its key expression:

- `complete: true` — "I have every key that matches my expression." The router can use `ConsolidationMode::Latest` when querying this storage, knowing it won't miss data elsewhere.
- `complete: false` — "I only have some of the data." The router will fan out to all matching storages and merge results.

When a client calls `session.get("sensors/**")`, the router:
1. Finds all storages with matching key expressions
2. Sends get requests to each
3. Applies the client's `ConsolidationMode` to deduplicate responses

---

## 2. Backend Comparison Table

| Feature | In-Memory | Filesystem | RocksDB | InfluxDB | S3 |
|---|---|---|---|---|---|
| **Persistence** | No (volatile) | Yes | Yes | Yes | Yes |
| **Crash safety** | N/A | OS page cache (risk) | WAL + SST | WAL + compaction | Server-side durability |
| **Time-series native** | No | No | No | Yes (measurements) | No |
| **`_time` selector** | No | No | No | Yes (full range queries) | No (metadata only) |
| **Write throughput** | Highest (RAM) | Moderate (I/O bound) | High (LSM tree) | High (WAL + async) | Moderate (HTTP latency) |
| **Read throughput** | Highest | Moderate | High (bloom filters) | Moderate (query parse) | Low (object per key) |
| **Latency** | Sub-microsecond | 10s of µs | 100s of µs | ~1ms | 10–100ms |
| **Data volume** | RAM-limited | Disk | Disk | Disk | Effectively unlimited |
| **Key limit** | None | Filesystem path limits | None | None | None |
| **Wildcard GET** | Yes | Yes | Yes (prefix seek) | v1 only | Yes |
| **read_only mode** | No | Yes | Yes | No | Yes |
| **Replication support** | Yes (volatile) | Yes | Yes | Yes | Yes |
| **Operational complexity** | None | Minimal | Minimal (embedded) | Medium (external server) | Low (managed cloud) |
| **Best for** | Cache, testing | Config, small files, human-readable | High-freq sensors, embedded | Time-series analytics, dashboards | Long-term archival, large payloads |
| **Library name** | built-in | `zenoh_backend_fs` | `zenoh_backend_rocksdb` | `zenoh_backend_influxdb` | `libzenoh_backend_s3` |

---

## 3. Transparent Multi-Backend Queries

One of Zenoh's most powerful storage features is transparent fan-out: a single `session.get()` call can query multiple storages simultaneously, and the responses are automatically merged.

### How It Works

When a client issues `session.get("sensors/**")`:

```
Client                          Router
  │                               │
  │──── get("sensors/**") ────>   │
  │                               │── to StorageService A (RocksDB, "sensors/**")
  │                               │── to StorageService B (S3, "sensors/**")
  │                               │── to StorageService C (InfluxDB, "sensors/**")
  │<─── merged replies ──────────-│
```

Each storage receives the query, calls its backend's `get()`, and sends replies back. The client sees all replies in a single stream. With `ConsolidationMode::Latest`, duplicate keys are deduplicated by keeping the highest-timestamped reply.

### Code Example: Querying Across Two Backends

```rust
use zenoh::prelude::r#async::*;
use zenoh::query::ConsolidationMode;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::config::default()).res().await.unwrap();

    // This single get() will fan out to ALL storages matching "sensors/**"
    // -- edge RocksDB (last hour of data)
    // -- cloud S3 (historical archive)
    let replies = session
        .get("sensors/**")
        .consolidation(ConsolidationMode::Latest)  // deduplicate by timestamp
        .res()
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        match reply.sample {
            Ok(sample) => println!(
                "Key: {}, Value: {:?}, Timestamp: {:?}",
                sample.key_expr,
                sample.value,
                sample.timestamp
            ),
            Err(err) => println!("Error: {:?}", err),
        }
    }
}
```

```python
import zenoh

conf = zenoh.Config()
session = zenoh.open(conf)

# Fan-out query across all matching storages
replies = session.get("sensors/**", zenoh.Queue())
for reply in replies:
    if reply.ok:
        print(f"Key: {reply.ok.key_expr}, Value: {reply.ok.payload.decode()}")
```

### Consolidation Modes

| Mode | Behavior |
|---|---|
| `ConsolidationMode::None` | Return all replies, including duplicates |
| `ConsolidationMode::Monotonic` | Deduplicate in transit; keep highest-timestamped per key |
| `ConsolidationMode::Latest` | Full deduplication; only one value per key returned |

For multi-backend queries, `ConsolidationMode::Latest` is almost always what you want.

### The `complete` Flag and `AllComplete` Target

```json5
storages: {
  edge_store: {
    key_expr: "sensors/**",
    complete: true,   // "I have ALL sensor data"
    volume: { id: "rocksdb", dir: "sensors" }
  }
}
```

When a storage has `complete: true`, clients using `QueryTarget::AllComplete` will only receive responses from complete storages, skipping partial ones. This is useful when you have a "primary" storage that holds the full dataset and secondary caches.

---

## 4. Heterogeneous Replication

Zenoh's replication system synchronizes storages with the same key expression across multiple routers, even when they use different backends. An edge device running RocksDB can replicate to a central InfluxDB server.

### How Anti-Entropy Replication Works

Replication uses an **interval-based digest** algorithm:

1. **Time partitioning**: The timeline is divided into intervals (default: 10s), each subdivided into sub-intervals (default: 5). This creates a hierarchical fingerprint of recent data.

2. **Hot/Warm/Cold eras**: Recent data ("hot", default: last 60s) is reconciled frequently. Older data ("warm", default: next 5 min) less frequently. Cold data is checked rarely.

3. **Digest exchange**: Each replica periodically publishes its digest fingerprint on a well-known key expression. Peers receive these and compare against their own digest.

4. **Alignment on divergence**: When digests differ, the nodes exchange their `get_all_entries()` results for the diverging time interval and pull missing updates.

### Replication Config

```json5
replication: {
  interval: 10.0,         // seconds between sync cycles (float, default: 10)
  sub_intervals: 5,       // time slots per interval (default: 5)
  hot: 6,                 // intervals considered "hot" = 6 × 10s = 60s (default: 6)
  warm: 30,               // intervals considered "warm" = 30 × 10s = 5min (default: 30)
  propagation_delay: 250, // milliseconds to wait for publications to arrive (default: 250)
}
```

**Critical constraints:**
- All replicas must use **identical** replication config values
- `propagation_delay` must be less than half of `interval × 1000` (in ms)
- Replication only works with `History::Latest` backends
- All data must be **timestamped** (HLC timestamps); untimstamped puts are rejected

### Example: Replicating RocksDB Across 3 Edge Nodes

On each edge node, configure the storage with the same key expression and identical replication config:

```json5
// edge-node-1.json5 (same config on node-2 and node-3, only peers list differs)
{
  plugins: {
    storage_manager: {
      volumes: {
        rocksdb: {}
      },
      storages: {
        sensor_store: {
          key_expr: "plant/sensors/**",
          strip_prefix: "plant/sensors",
          complete: true,
          volume: {
            id: "rocksdb",
            dir: "plant-sensors",
            create_db: true
          },
          replication: {
            interval: 10.0,
            sub_intervals: 5,
            hot: 6,
            warm: 30,
            propagation_delay: 250
          }
        }
      }
    }
  }
}
```

The three routers discover each other via the Zenoh scouting mechanism. Once connected, they will continuously synchronize `plant/sensors/**` data using the anti-entropy digest protocol.

---

## 5. Geographically Distributed Storage

A common production pattern: edge nodes hold recent high-frequency data in embedded RocksDB, while a central node archives everything to S3 or InfluxDB. Queries transparently span both.

### Architecture

```
  Edge Site A                   Edge Site B
  ┌─────────────────┐           ┌─────────────────┐
  │ zenohd (router) │           │ zenohd (router) │
  │ RocksDB storage │           │ RocksDB storage │
  │ "sensors/**"    │           │ "sensors/**"    │
  └────────┬────────┘           └────────┬────────┘
           │  Zenoh P2P / routed             │
           └──────────────┬─────────────────┘
                          │
                 ┌────────┴────────┐
                 │ zenohd (cloud)  │
                 │ S3 storage      │
                 │ "sensors/**"    │
                 │ InfluxDB storage│
                 │ "sensors/**"    │
                 └─────────────────┘
```

**Data flow:**
- Sensor devices publish to `sensors/<site>/<device>/reading`
- The nearest edge router's RocksDB storage subscribes and stores locally (low latency writes)
- The cloud router's S3 storage subscribes and archives everything durably
- Optionally, InfluxDB on the cloud router stores the same data for time-series analytics

**Query flow:**
- `session.get("sensors/**")` fans out to edge RocksDB (fast, recent) and cloud S3 (complete archive)
- With `ConsolidationMode::Latest`, the most recent value per key is returned, wherever it lives

### Config: Edge Node (RocksDB)

```json5
// edge-node.json5
{
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  },
  connect: {
    endpoints: ["tcp/cloud.example.com:7447"]
  },
  plugins: {
    storage_manager: {
      volumes: {
        rocksdb: {}
      },
      storages: {
        local_sensors: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",
          complete: false,  // we only have local data
          volume: {
            id: "rocksdb",
            dir: "sensor-cache",
            create_db: true
          },
          // Optional: garbage collect old data after 1 hour
          garbage_collection: {
            period: 60,       // GC run every 60 seconds
            lifespan: 3600    // keep data for 1 hour
          }
        }
      }
    }
  }
}
```

### Config: Cloud Node (S3 Archive + InfluxDB Analytics)

```json5
// cloud-node.json5
{
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  },
  plugins: {
    storage_manager: {
      volumes: {
        s3: {
          region: "us-east-1"
        },
        influxdb: {
          url: "http://influxdb:8086",
          private: {
            username: "admin",
            password: "password"
          }
        }
      },
      storages: {
        // Long-term S3 archive
        s3_archive: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",
          complete: true,  // cloud has everything
          volume: {
            id: "s3",
            bucket: "zenoh-sensor-archive",
            reuse_bucket: true,
            on_closure: "do_nothing",
            private: {
              access_key: "AKIAIOSFODNN7EXAMPLE",
              secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
            }
          }
        },
        // InfluxDB for time-series analytics
        influx_analytics: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",
          volume: {
            id: "influxdb",
            db: "sensor_metrics",
            create_db: true,
            on_closure: "do_nothing"
          }
        }
      }
    }
  }
}
```

---

## 6. Fault Tolerance

### When a Storage Node Goes Down

Zenoh handles storage node failures gracefully at multiple levels:

**During the outage:**
- Queries to the unavailable storage timeout or return partial results
- Other storages with the same key expression still respond
- With `ConsolidationMode::Latest` and multiple backends covering the same KE, the client receives responses from available nodes
- Publishers continue writing; the offline node misses those publications

**Recovery via anti-entropy:**
When the node comes back up with replication enabled:
1. The node generates its digest fingerprint (representing only what it has)
2. Peers detect divergence in the hot/warm time intervals
3. The alignment protocol fetches missing entries from peers
4. The node catches up to the current state within `interval × (hot + warm)` seconds

For a default config (10s interval, hot=6, warm=30), a node that was down for up to 6 minutes will fully converge within one replication cycle.

**Data written during outage** that was stored on other replicas will be synchronized back once the node reconnects. Data that was **only** written to the offline node (no replication, single-node storage) is unavailable until the node recovers.

### Partial Results Pattern

Applications should be written to handle partial results gracefully:

```rust
use zenoh::prelude::r#async::*;
use zenoh::query::ConsolidationMode;
use std::time::Duration;

let replies = session
    .get("sensors/**")
    .timeout(Duration::from_millis(500))   // don't wait forever for slow nodes
    .consolidation(ConsolidationMode::Latest)
    .res()
    .await
    .unwrap();

let mut results = vec![];
while let Ok(reply) = replies.recv_async().await {
    if let Ok(sample) = reply.sample {
        results.push(sample);
    }
    // Errors from unavailable storages are silently skipped
}
// Work with whatever arrived within the timeout
```

### Replication for High Availability

For HA, configure at least 3 replicas (quorum tolerance for 1 failure):

```json5
// Run this config on each of 3 nodes; they discover each other via Zenoh scouting
storages: {
  ha_store: {
    key_expr: "critical/**",
    complete: true,
    volume: {
      id: "rocksdb",
      dir: "ha-data",
      create_db: true
    },
    replication: {
      interval: 5.0,          // faster sync for critical data
      sub_intervals: 5,
      hot: 12,                // last 60s considered hot
      warm: 60,               // next 5 minutes warm
      propagation_delay: 100  // 100ms propagation assumption
    }
  }
}
```

---

## 7. Backend Deep Dives

### 7.1 In-Memory Backend

**Built-in**, no external library required. Backed by a `HashMap<OwnedKeyExpr, StoredData>` protected by a `RwLock`.

**Capabilities:** `Persistence::Volatile`, `History::Latest`

**Volume config:** No parameters required.

```json5
volumes: {
  memory: {}   // or just use the implicit "memory" volume
}
```

**Storage config:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `key_expr` | string (KE) | required | Key expression to subscribe to |
| `strip_prefix` | string (KE) | none | Prefix stripped before storing keys |
| `complete` | bool | `false` | Whether this storage holds all matching keys |

**Behavior:**
- `put`: Inserts or replaces the value for the key
- `delete`: Removes the key from the map; does **not** leave a tombstone (purely volatile)
- `get`: HashMap lookup for exact keys; linear scan with KE matching for wildcards
- **Data is lost on router restart** — no durability whatsoever

**Use cases:** Development, unit testing, L1 caching in front of a persistent backend, ephemeral session state.

---

### 7.2 Filesystem Backend

**Library:** `zenoh_backend_fs`
**Environment variable:** `ZENOH_BACKEND_FS_ROOT` (default: `~/.zenoh/zenoh_backend_fs`)

**Capabilities:** `Persistence::Durable`, `History::Latest`

**Volume config:** No volume-level parameters required.

```json5
volumes: {
  fs: {}
}
```

**Storage config:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `dir` | string | required | Subdirectory under `$ZENOH_BACKEND_FS_ROOT` for this storage |
| `read_only` | bool | `false` | If true, only responds to GET; rejects PUT/DELETE |
| `on_closure` | string | `"do_nothing"` | `"do_nothing"` or `"delete_all"` (removes directory) |
| `follow_links` | bool | `false` | Follow symbolic links when traversing the storage directory |
| `keep_mime_types` | bool | `true` | Return MIME-typed Custom values for unknown encodings; `false` returns raw bytes |

**Key-to-path mapping:**
- Key `sensors/factory1/temp` with `strip_prefix: "sensors"` → file `${ROOT}/dir/factory1/temp`
- Subdirectories are created as needed
- File names that conflict with Zenoh keys get `.##z` suffix to avoid collisions

**Metadata storage:** Each filesystem storage maintains a RocksDB sidecar database (inside the storage directory) storing encoding and timestamp metadata for each file. If no metadata exists for a file (e.g., the file was created externally), the encoding is guessed from the file extension using mime_guess, and the timestamp is taken from the file's mtime.

**Behavior on deletion:** The file is removed, and a deletion tombstone with timestamp is written to the RocksDB sidecar. A periodic GC task removes tombstones older than `lifespan` that have no corresponding file.

**Behavior on GET:** Scans the directory for files matching the key expression. For each file, retrieves encoding and timestamp from the RocksDB sidecar, or guesses from file metadata if not found.

**Use cases:** Configuration files that humans edit directly, small static datasets, data that needs to be inspectable as plain files, situations where other tools need to read/write the same data.

---

### 7.3 RocksDB Backend

**Library:** `zenoh_backend_rocksdb`
**Environment variable:** `ZENOH_BACKEND_ROCKSDB_ROOT` (default: `~/.zenoh/zenoh_backend_rocksdb`)
**Build requirement:** `clang` (RocksDB FFI bindings)

**Capabilities:** `Persistence::Durable`, `History::Latest`

**Volume config:** No volume-level parameters required.

```json5
volumes: {
  rocksdb: {}
}
```

**Storage config:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `dir` | string | required | Subdirectory under `$ZENOH_BACKEND_ROCKSDB_ROOT` for the database |
| `create_db` | bool | `false` | Create the database if it doesn't exist |
| `read_only` | bool | `false` | Read-only mode; rejects all PUT/DELETE |
| `on_closure` | string | unset | If `"destroy_db"`, deletes the database on storage removal; otherwise leaves it |

**Internal storage format:** Two RocksDB column families per storage:

- `"default"` CF: key → raw encoded value bytes
- `"data_info"` CF: key → binary packed struct:
  - 8 bytes: HLC timestamp seconds
  - 16 bytes: HLC node ID
  - 1 byte: `is_deleted` flag
  - variable: encoding prefix (ZInt)
  - variable: encoding suffix (length-prefixed string)

**Behavior on PUT:** Writes value bytes to `"default"` CF and timestamp/encoding metadata to `"data_info"` CF. If the incoming timestamp is older than what's already stored, the write is rejected (`StorageInsertionResult::Outdated`) — this is what prevents stale data from overwriting fresh data in out-of-order delivery scenarios.

**Behavior on DELETE:** Removes the entry from `"default"` CF. Writes a tombstone (with `is_deleted=true` and deletion timestamp) to `"data_info"` CF. A periodic GC task removes tombstones older than `lifespan` seconds.

**Behavior on GET:**
- Exact key: direct `get` on both column families — O(1) with bloom filters
- Key expression with wildcards: prefix seek optimization when the KE has a non-wildcard prefix, then linear scan with KE matching for the remaining keys

**Use cases:** High-frequency sensor data on embedded Linux, edge devices with crash requirements (WAL ensures no data loss), situations where you need thousands to millions of keys with sub-millisecond reads, IoT gateways.

---

### 7.4 InfluxDB Backend

**Library:** `zenoh_backend_influxdb`
**Supports:** InfluxDB v1.x and v2.x (different configs, same library name `zenoh_backend_influxdb`)

**Capabilities:** `Persistence::Durable`, `History::All`

> InfluxDB is the **only** backend with `History::All`, meaning it retains all historical values per key, not just the latest. This enables time-series queries.

**Volume config (v1.x):**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `url` | string | yes | InfluxDB server URL, e.g. `http://localhost:8086` |
| `private.username` | string | no | Admin username for DB creation/drop |
| `private.password` | string | no | Admin password |

**Volume config (v2.x):** Use volume named `influxdb2`; append `/api/v2` to url

| Parameter | Type | Required | Description |
|---|---|---|---|
| `url` | string | yes | InfluxDB v2 URL, e.g. `http://localhost:8086/api/v2` |
| `private.org_id` | string | no | Organization ID (ALL-ACCESS token recommended) |
| `private.token` | string | no | Admin token for bucket creation/drop |

**Storage config:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `volume.id` | string | required | Must match volume name (`influxdb` for v1, `influxdb2` for v2) |
| `volume.db` | string | auto-generated | InfluxDB database/bucket name |
| `volume.create_db` | bool | `false` | Create database if absent |
| `volume.on_closure` | string | `"do_nothing"` | `"do_nothing"`, `"drop_db"`, or `"drop_series"` (v1 only) |
| `volume.private.username` | string | no | Read-write user credentials (v1) |
| `volume.private.password` | string | no | Read-write user password (v1) |
| `volume.private.org_id` | string | no | Organization ID (v2) |
| `volume.private.token` | string | no | Read-write token (v2) |

**Mapping to InfluxDB concepts:**
- Each Zenoh **storage** → one InfluxDB **database** (v1) or **bucket** (v2)
- Each Zenoh **key** → one InfluxDB **measurement** (the key stripped of `strip_prefix`)
- Each Zenoh **put** → one InfluxDB **point** with nanosecond timestamp and these fields:
  - `kind` tag: `"PUT"` or `"DEL"`
  - `timestamp` field: original Zenoh HLC timestamp
  - `encoding` field: encoding flag integer
  - `base64` field: boolean
  - `value` field: value as string (base64-encoded for binary)

**Time-series queries with `_time` selector:**

Without `_time`, GET returns only the **latest** point per measurement (to stay consistent with other backends). To get historical data, add `_time` to the selector:

```bash
# All historical values for a key (infinite range)
curl 'http://localhost:8000/demo/example/temp?_time=[..]'

# Values in a fixed date range
curl 'http://localhost:8000/demo/example/temp?_time=[2024-01-01T00:00:00Z..2024-02-01T00:00:00Z]'

# Relative range: last 2 hours
curl 'http://localhost:8000/demo/example/temp?_time=[now(-2h)..now()]'

# Relative range: between 2 and 1 day ago
curl 'http://localhost:8000/demo/example/temp?_time=[now(-2d)..now(-1d)]'
```

In Rust:
```rust
let replies = session
    .get("demo/example/temp?_time=[now(-1h)..]")
    .consolidation(ConsolidationMode::None)  // keep all historical points
    .res()
    .await
    .unwrap();
```

**Wildcard limitation:** Wildcard GET (`sensors/**`) works in InfluxDB v1 but is **not fully supported** in InfluxDB v2 due to API limitations.

**Use cases:** Time-series analytics, Grafana dashboards (InfluxDB datasource), data retention policies, audit logs, anomaly detection where history matters.

---

### 7.5 S3 Backend

**Library:** `libzenoh_backend_s3`
**Compatible with:** Amazon S3, MinIO, and any S3-compatible API

**Capabilities:** `Persistence::Durable`, `History::Latest`

**Volume config:**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `region` | string | AWS: yes | AWS region name (e.g., `"us-east-1"`); ignored by MinIO |
| `url` | string | MinIO: yes | Endpoint URL (e.g., `"http://localhost:9000"`); auto-resolved for AWS |
| `tls.private.root_ca_certificate_file` | string | no | Path to CA cert for MinIO TLS |
| `tls.private.root_ca_certificate_base64` | string | no | Base64-encoded CA cert for MinIO TLS |

**Storage config:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `volume.id` | string | required | Must match volume name (e.g., `"s3"`) |
| `volume.bucket` | string | required | S3 bucket name |
| `volume.reuse_bucket` | bool | `false` | If `true`, use existing bucket owned by you; `false` fails if bucket exists |
| `volume.read_only` | bool | `false` | Read-only mode; only responds to GET |
| `volume.on_closure` | string | `"do_nothing"` | `"do_nothing"` or `"destroy_bucket"` |
| `volume.private.access_key` | string | required | AWS access key / MinIO root user |
| `volume.private.secret_key` | string | required | AWS secret key / MinIO root password |

**Key-to-object mapping:**
- Zenoh key `sensors/factory1/temp` with `strip_prefix: "sensors"` → S3 object key `factory1/temp`
- Object value: raw bytes payload
- Timestamp stored as object **metadata** (`x-amz-meta-*` headers), with fallback for legacy deployments that don't have metadata

**Behavior on GET:** Lists objects matching the key expression prefix, then filters by KE matching. Each matched object is fetched individually. This means wildcard GETs (`sensors/**`) can be expensive for large buckets.

**Behavior on DELETE:** Deletes the S3 object.

**TLS with MinIO:** MinIO requires providing the CA certificate since it uses a self-signed cert by default. Generate with `minica --domains localhost`, then specify `root_ca_certificate_file`.

**Use cases:** Long-term archival of large payloads (images, firmware, logs), cloud-native deployments where S3 is already the storage of record, multi-region data availability, payloads too large for RocksDB or InfluxDB.

---

## 8. Complete Config Examples

### 8.1 In-Memory Storage for Testing

```json5
// zenoh-test.json5 — fast, no disk I/O, perfect for development
{
  plugins: {
    storage_manager: {
      storages: {
        demo: {
          key_expr: "test/**",
          volume: "memory"  // use the built-in memory volume
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
```

```bash
zenohd -c zenoh-test.json5
curl -X PUT -d "hello" http://localhost:8000/test/foo
curl http://localhost:8000/test/**
```

### 8.2 Multi-Backend: RocksDB + Filesystem on Same Router

```json5
// zenoh-multi.json5 — different backends for different data types
{
  plugins: {
    storage_manager: {
      volumes: {
        rocksdb: {},
        fs: {}
      },
      storages: {
        // High-frequency sensor readings → RocksDB (fast writes)
        sensors: {
          key_expr: "data/sensors/**",
          strip_prefix: "data/sensors",
          volume: {
            id: "rocksdb",
            dir: "sensor-data",
            create_db: true
          }
        },
        // Configuration files → filesystem (human-editable)
        config: {
          key_expr: "config/**",
          strip_prefix: "config",
          volume: {
            id: "fs",
            dir: "config-files"
          }
        }
      }
    }
  }
}
```

### 8.3 Geographically Distributed: Edge RocksDB + Central S3

**Edge node** (`edge-site-a.json5`):
```json5
{
  listen: { endpoints: ["tcp/0.0.0.0:7447"] },
  connect: { endpoints: ["tcp/cloud.example.com:7447"] },
  plugins: {
    storage_manager: {
      volumes: {
        rocksdb: {}
      },
      storages: {
        edge_cache: {
          key_expr: "plant/**",
          strip_prefix: "plant",
          complete: false,
          volume: {
            id: "rocksdb",
            dir: "plant-edge",
            create_db: true
          },
          garbage_collection: {
            period: 300,     // GC every 5 minutes
            lifespan: 3600   // keep data for 1 hour
          }
        }
      }
    }
  }
}
```

**Central cloud node** (`cloud.json5`):
```json5
{
  listen: { endpoints: ["tcp/0.0.0.0:7447"] },
  plugins: {
    storage_manager: {
      volumes: {
        s3: {
          region: "us-east-1"
        }
      },
      storages: {
        s3_archive: {
          key_expr: "plant/**",
          strip_prefix: "plant",
          complete: true,   // cloud has the complete dataset
          volume: {
            id: "s3",
            bucket: "plant-data-archive",
            reuse_bucket: true,
            on_closure: "do_nothing",
            private: {
              access_key: "AKIAIOSFODNN7EXAMPLE",
              secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
            }
          }
        }
      }
    }
  }
}
```

### 8.4 Replicated RocksDB Across 3 Nodes

Deploy this identical config on all three nodes (they find each other via scouting):

```json5
// node-1.json5, node-2.json5, node-3.json5 — identical storage config
{
  listen: { endpoints: ["tcp/0.0.0.0:7447"] },
  // Each node lists the other two as peers
  connect: {
    endpoints: [
      "tcp/node-2.local:7447",
      "tcp/node-3.local:7447"
    ]
  },
  plugins: {
    storage_manager: {
      volumes: {
        rocksdb: {}
      },
      storages: {
        replicated_store: {
          key_expr: "critical/**",
          strip_prefix: "critical",
          complete: true,
          volume: {
            id: "rocksdb",
            dir: "critical-data",
            create_db: true
          },
          replication: {
            interval: 10.0,
            sub_intervals: 5,
            hot: 6,
            warm: 30,
            propagation_delay: 250
          }
        }
      }
    }
  }
}
```

### 8.5 InfluxDB Time-Series with `_time` Query

```json5
// zenoh-influx.json5
{
  plugins: {
    storage_manager: {
      volumes: {
        influxdb: {
          url: "http://localhost:8086",
          private: {
            username: "admin",
            password: "secretpassword"
          }
        }
      },
      storages: {
        metrics: {
          key_expr: "metrics/**",
          strip_prefix: "metrics",
          volume: {
            id: "influxdb",
            db: "zenoh_metrics",
            create_db: true,
            on_closure: "do_nothing",
            private: {
              username: "zenoh_user",
              password: "zenoh_pass"
            }
          }
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
```

**Publishing and querying time-series data:**

```bash
# Publish several data points
curl -X PUT -d "22.5" http://localhost:8000/metrics/temperature/sensor1
sleep 1
curl -X PUT -d "23.1" http://localhost:8000/metrics/temperature/sensor1
sleep 1
curl -X PUT -d "21.8" http://localhost:8000/metrics/temperature/sensor1

# Get only the latest value (default behavior)
curl 'http://localhost:8000/metrics/temperature/sensor1'

# Get the full time series (all historical values)
curl -g 'http://localhost:8000/metrics/temperature/sensor1?_time=[..]'

# Get the last 5 minutes
curl -g 'http://localhost:8000/metrics/temperature/**?_time=[now(-5m)..]'

# Get a specific date range
curl -g 'http://localhost:8000/metrics/temperature/**?_time=[2024-01-15T00:00:00Z..2024-01-16T00:00:00Z]'
```

In Rust:
```rust
use zenoh::prelude::r#async::*;
use zenoh::query::ConsolidationMode;

let session = zenoh::open(zenoh::config::default()).res().await.unwrap();

// Query last hour of temperature history for all sensors
let replies = session
    .get("metrics/temperature/**?_time=[now(-1h)..]")
    .consolidation(ConsolidationMode::None)  // none: keep all historical points
    .res()
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    if let Ok(sample) = reply.sample {
        println!("{}: {} @ {:?}",
            sample.key_expr,
            sample.value,
            sample.timestamp
        );
    }
}
```

---

## 9. When to Choose Each Backend

### In-Memory

**Choose when:**
- Writing tests or running demos — no setup required, instant teardown
- Implementing a short-lived cache in front of a persistent backend
- Data lifetime is sub-second or tied to router uptime
- You want zero operational overhead

**Avoid when:** Any data must survive a router restart.

---

### Filesystem

**Choose when:**
- Data needs to be human-readable (configs in YAML/JSON, text files)
- Other tools (scripts, editors, rsync) need to access the same data without Zenoh
- Key count is small (< ~10,000 files — directories degrade past that)
- You want to expose an existing directory tree via Zenoh GET
- `follow_links: true` lets you serve symlinked content

**Avoid when:**
- High write frequency (many small file creates/deletes stress the filesystem)
- You need guaranteed crash safety (page cache can lose data on power loss)
- Key count exceeds tens of thousands

---

### RocksDB

**Choose when:**
- High-frequency sensor or telemetry data (thousands of writes/second)
- Embedded Linux or resource-constrained devices (RocksDB is in-process, no daemon)
- You need crash safety without running an external database server
- Key count in the millions is expected
- Replication between edge nodes is required

**Avoid when:**
- You need time-series range queries (RocksDB has no native time dimension)
- Data needs to be accessed by external analytics tools
- You're on a platform where compiling RocksDB (requires clang) is impractical

---

### InfluxDB

**Choose when:**
- Data is inherently time-series (metrics, telemetry, logs with retention policies)
- You need `_time` range queries: "give me all values between T1 and T2"
- Grafana dashboards will visualize the data (InfluxDB is a native datasource)
- Data retention policies are required (InfluxDB can auto-expire old data)
- Analytics workflows will run InfluxQL or Flux queries directly

**Avoid when:**
- You only need the latest value per key (in-memory or RocksDB are faster and simpler)
- Wildcard GET across many keys is critical (v2 has limitations here)
- You're running on embedded hardware (external InfluxDB server required)
- Key names change frequently (each unique key → a new measurement)

---

### S3

**Choose when:**
- Long-term archival with essentially unlimited storage capacity
- Payloads are large (images, firmware binaries, logs — S3 object storage is designed for this)
- Cloud-native deployment where S3 is already your object store
- Multi-region availability is required (configure bucket replication at the S3 level)
- You want to use existing S3 lifecycle policies for tiering and expiry

**Avoid when:**
- Low-latency reads are required (HTTP round-trip per object is 10–100ms)
- High write frequency (S3 PUT costs and latency add up fast)
- Wildcard GET across millions of objects (list + fetch is expensive)
- Offline or air-gapped environments (requires S3 connectivity; MinIO mitigates this)

---

### Quick Decision Guide

```
Need to survive restart?
  No  → In-Memory
  Yes → Continue...

Time-series range queries with _time selector?
  Yes → InfluxDB

Data large/archival/cloud?
  Yes → S3

Embedded, edge, high-frequency?
  Yes → RocksDB

Human-readable, low key count, inspectable files?
  Yes → Filesystem

High frequency + must survive crash + no external server?
  Default → RocksDB
```

## See Also

- [Plugin Storage Manager Guide](plugin-storage-manager-guide.md) — the storage manager plugin that loads all these backends and manages replication
- [Plugin InfluxDB Guide](plugin-influxdb-guide.md) — InfluxDB backend with time-series queries and v1 vs v2 differences
- [Plugin RocksDB Guide](plugin-rocksdb-guide.md) — RocksDB backend with crash recovery, column families, and performance details
- [Plugin S3 Guide](plugin-s3-guide.md) — S3 backend for AWS, MinIO, and GCS
- [Plugin Filesystem Guide](plugin-filesystem-guide.md) — filesystem backend with RocksDB sidecar for metadata
