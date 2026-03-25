# Zenoh RocksDB Backend Plugin Guide

**Version:** 1.7.2
**Library name:** `zenoh_backend_rocksdb`
**Source:** [eclipse-zenoh/zenoh-backend-rocksdb](https://github.com/eclipse-zenoh/zenoh-backend-rocksdb)

---

## Table of Contents

- [What Is RocksDB?](#what-is-rocksdb)
- [When to Use RocksDB vs Alternatives](#when-to-use-rocksdb-vs-alternatives)
- [Installation](#installation)
  - [Linux Debian](#linux-debian)
  - [Manual (all platforms)](#manual-all-platforms)
  - [Build from Source](#build-from-source)
- [Configuration Reference](#configuration-reference)
  - [Environment Variables](#environment-variables)
  - [Volume Configuration](#volume-configuration)
  - [Storage Configuration (volume block)](#storage-configuration-volume-block)
  - [RocksDB Engine Tuning](#rocksdb-engine-tuning)
- [Storage Internals](#storage-internals)
  - [Mapping: Zenoh Keys → RocksDB Keys](#mapping-zenoh-keys-rocksdb-keys)
  - [Column Families](#column-families)
  - [Atomic Writes](#atomic-writes)
  - [Deletion Behavior](#deletion-behavior)
  - [GET Behavior](#get-behavior)
- [Persistence Guarantees](#persistence-guarantees)
  - [Write-Ahead Log (WAL)](#write-ahead-log-wal)
  - [What Survives a Crash](#what-survives-a-crash)
  - [Crash Recovery](#crash-recovery)
  - [Compaction](#compaction)
- [Performance Characteristics](#performance-characteristics)
  - [Write Amplification](#write-amplification)
  - [Memory Usage](#memory-usage)
  - [Throughput (estimates)](#throughput-estimates)
  - [Concurrency](#concurrency)
- [Example Configurations](#example-configurations)
  - [1. Basic RocksDB Storage (Start Fresh)](#1-basic-rocksdb-storage-start-fresh)
  - [2. Read-Only Storage (Serve Pre-existing Data)](#2-read-only-storage-serve-pre-existing-data)
  - [3. Ephemeral RocksDB Storage (Auto-Cleanup on Removal)](#3-ephemeral-rocksdb-storage-auto-cleanup-on-removal)
- [Runtime Management via Admin Space](#runtime-management-via-admin-space)
- [Rust API Example](#rust-api-example)
- [Python API Example](#python-api-example)
- [Troubleshooting](#troubleshooting)
  - ["Failed to open data-info database"](#failed-to-open-data-info-database)
  - ["rocksdb backed storages need volume-specific configurations"](#rocksdb-backed-storages-need-volume-specific-configurations)
  - [SIGSEGV on startup](#sigsegv-on-startup)
  - ["Received update for read-only DB"](#received-update-for-read-only-db)
  - [High disk usage](#high-disk-usage)
  - [Lock file prevents reopening after crash](#lock-file-prevents-reopening-after-crash)

## What Is RocksDB?

RocksDB is an embedded key-value storage engine developed by Facebook, optimized for write-heavy workloads on fast storage (SSD/NVMe). It is based on a **Log-Structured Merge-tree (LSM-tree)** architecture: instead of modifying data in-place, writes are first appended to a write-ahead log (WAL) and buffered in memory (memtable), then flushed to sorted immutable files (SSTables) on disk. Background compaction periodically merges these files to reduce read amplification.

Key characteristics:
- **Write-optimized**: sequential disk writes during flush + compaction are fast; random writes are absorbed into the memtable
- **Production-grade**: used in Facebook, LinkedIn, MySQL (MyRocks), TiKV, and many distributed systems
- **Embedded**: no server process; the database is a directory of files accessed directly by the host process
- **Column Families**: logical namespaces within one database that share the WAL and compaction infrastructure

The Zenoh RocksDB backend uses two column families per storage:
- `default` — stores raw zenoh payloads (bytes)
- `data_info` — stores metadata (timestamp, encoding, deleted flag) for each key

---

## When to Use RocksDB vs Alternatives

| Criteria | RocksDB | Filesystem | InfluxDB | In-memory |
|---|---|---|---|---|
| **Write throughput** | Very high (batched, sequential) | Medium (one file per key) | High (time-series optimized) | Highest (RAM-only) |
| **Read throughput** | Good for point lookups; moderate for scans | Medium | Very high for time-range queries | Highest |
| **Time-series workloads** | Good (append-heavy fits LSM) | Poor (no ordering) | Excellent (native time-series) | Ephemeral only |
| **Random access workloads** | Good (bloom filters help) | Good (one file = one key) | Poor (requires time bounds) | Excellent |
| **Operational complexity** | Low (embedded, no server) | Very low (just files) | High (InfluxDB process, retention policies) | None |
| **Disk space efficiency** | Good (compaction reclaims space) | Fair (many small files) | Good (compression + downsampling) | N/A |
| **Crash recovery** | Automatic (WAL replay, typically <1 s) | Manual (incomplete writes leave corrupt files) | Automatic (WAL) | No recovery (data lost) |
| **Query capabilities** | Key lookups + prefix scan | Key lookups only | Rich time-series queries (Flux/InfluxQL) | Key lookups only |
| **Data survives restart** | Yes | Yes | Yes | No |

**Choose RocksDB when:**
- You need durable storage with automatic crash recovery
- Workloads are write-heavy or mixed read/write
- You want an embedded backend with no external server dependency
- You store device telemetry, sensor data, or state that must persist across restarts

**Choose Filesystem when:**
- Keys map naturally to files (e.g., config blobs, static assets)
- Simplicity matters more than performance
- You need to inspect stored data with standard tools

**Choose InfluxDB when:**
- Your workload is time-series with time-range queries
- You need data retention policies or downsampling

**Choose In-memory when:**
- Data is ephemeral (caches, live sensor streams)
- Latency is critical and durability is not required

---

## Installation

### Linux Debian

```bash
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | \
  sudo tee -a /etc/apt/sources.list.d/zenoh.list > /dev/null
sudo apt update
sudo apt install zenoh-backend-rocksdb
```

This installs the shared library to the same location as `zenohd`. The package depends on `zenoh-plugin-storage-manager`.

### Manual (all platforms)

Download the `.zip` for your Rust target from:

```
https://download.eclipse.org/zenoh/zenoh-backend-rocksdb/latest/
```

Unzip the `.so` / `.dylib` / `.dll` into:
- The same directory as `zenohd`, or
- `~/.zenoh/lib/`, or
- Any directory on the library search path

### Build from Source

```bash
# Match the exact Rust version used to build zenohd
zenohd --version
# Example output: The zenoh router v1.7.2 built with rustc 1.75.0

rustup default 1.75.0
cargo build --release --all-targets
```

> **Warning:** Rust has no stable ABI. The backend library **must** be built with the same Rust version and the same zenoh dependency version as `zenohd`. A version mismatch causes a `SIGSEGV` crash at load time.

---

## Configuration Reference

### Environment Variables

| Variable | Default | Description |
|---|---|---|
| `ZENOH_BACKEND_ROCKSDB_ROOT` | `~/.zenoh/zenoh_backend_rocksdb` | Root directory for all RocksDB databases managed by this backend. Each storage's `dir` is resolved relative to this root. |

`ZENOH_HOME` defaults to `~/.zenoh`. If `ZENOH_BACKEND_ROCKSDB_ROOT` is unset, databases land at `~/.zenoh/zenoh_backend_rocksdb/<dir>`.

### Volume Configuration

The `rocksdb` volume itself takes no configuration properties — an empty object `{}` is all that is needed:

```json5
volumes: {
  rocksdb: {}
}
```

The volume exposes two admin-space properties at runtime: `root` (resolved absolute path) and `version` (plugin version string).

### Storage Configuration (volume block)

Each storage that uses the `rocksdb` volume must include a `volume` block with `id: "rocksdb"` and the following properties:

---

#### `dir`

| Field | Value |
|---|---|
| **Type** | string |
| **Required** | Yes |
| **Default** | none |

The name of the subdirectory (relative to `${ZENOH_BACKEND_ROCKSDB_ROOT}`) where the RocksDB database files are stored. The resolved absolute path is `${ZENOH_BACKEND_ROCKSDB_ROOT}/<dir>`.

Must be a string. An error is returned if missing or not a string.

```json5
volume: {
  id: "rocksdb",
  dir: "my-storage"
  // Database will be at ${ZENOH_BACKEND_ROCKSDB_ROOT}/my-storage/
}
```

---

#### `create_db`

| Field | Value |
|---|---|
| **Type** | boolean |
| **Required** | No |
| **Default** | `false` (unset) |

When `true`, the RocksDB database is created if it does not already exist. When `false` or absent, opening a non-existent database returns an error.

```json5
volume: {
  id: "rocksdb",
  dir: "new-storage",
  create_db: true   // Create the database directory and files on first run
}
```

If the directory already exists with a valid RocksDB database, `create_db: true` is a no-op (the existing database is opened normally).

---

#### `read_only`

| Field | Value |
|---|---|
| **Type** | boolean |
| **Required** | No |
| **Default** | `false` (unset) |

When `true`, the storage opens the RocksDB database in read-only mode:
- `GET` queries are served normally from the database
- `PUT` operations are rejected with an error log: `"Received update for read-only DB"`
- `DELETE` operations are rejected with an error log: `"Received update for read-only DB"`
- The database is opened using `DB::open_cf_for_read_only` with `error_if_log_file_exists: true`

This is useful for serving pre-existing databases populated by an external process or another zenoh router.

```json5
volume: {
  id: "rocksdb",
  dir: "archived-data",
  read_only: true
}
```

---

#### `on_closure`

| Field | Value |
|---|---|
| **Type** | string |
| **Required** | No |
| **Default** | `"do_nothing"` (unset) |
| **Valid values** | `"do_nothing"`, `"destroy_db"` |

Controls what happens to the RocksDB database files when the storage is removed (e.g., via admin space DELETE or router shutdown).

- **`"do_nothing"` (default):** The database directory is left on disk. Data persists and can be opened again by a future storage with the same `dir`.
- **`"destroy_db"`:** The database is flushed, closed, and then destroyed (`DB::destroy`). The directory and all its files are deleted permanently.

On drop (regardless of `on_closure`), the database is flushed with `db.flush()` before being closed. If the flush fails, a warning is logged but the drop continues.

```json5
volume: {
  id: "rocksdb",
  dir: "temp-cache",
  on_closure: "destroy_db"  // Clean up automatically when the storage is removed
}
```

---

### RocksDB Engine Tuning

The backend does **not** expose RocksDB engine options (block cache size, write buffer size, bloom filters, compression, etc.) through the JSON5 configuration. Internally it uses `Options::default()` for both column families. If you need fine-grained tuning (e.g., for high-throughput or memory-constrained environments), you must build a custom backend from source and modify `Options` before opening the database.

---

## Storage Internals

### Mapping: Zenoh Keys → RocksDB Keys

The full zenoh key expression for a published value (e.g., `demo/example/sensor/temp`) has the `strip_prefix` removed before storage. With `strip_prefix: "demo/example"`, the key stored in RocksDB is `sensor/temp`.

When `strip_prefix` exactly matches the key (i.e., the stripped key would be empty), the special key `@@none_key@@` is used in the database.

### Column Families

Every RocksDB storage has exactly two column families:

**`default` (payloads)**
Raw zenoh value bytes. The key is the stripped zenoh key expression string.

**`data_info`**
Metadata for each key, encoded as:
- 8 bytes: HLC timestamp time component (NTP64, big-endian u64)
- 16 bytes: HLC timestamp ID (TimestampId, little-endian)
- 1 byte: `deleted` flag (boolean)
- 2 bytes: encoding ID (u16)
- variable: encoding schema bytes

### Atomic Writes

Every `PUT` writes to both column families atomically using a `WriteBatch`. This ensures that payload and metadata are always consistent: you will never see a payload without a corresponding `data_info` entry or vice versa.

### Deletion Behavior

On `DELETE`:
- The key is removed from the `default` column family (payload deleted)
- The key is removed from the `data_info` column family (metadata deleted)

This is also done atomically via `WriteBatch`.

> Note: The README describes a previous behavior where deletions left a tombstone in `data_info` with a `deleted=true` flag to prevent re-insertion of older out-of-order messages. The current source code (v1.7.2) performs a full atomic delete from both CFs on DELETE.

### GET Behavior

- **Exact key (no wildcards):** Direct `get_cf` on both column families. Returns the payload and decodes encoding + timestamp from `data_info`. Returns `None` if either the payload is missing or the `deleted` flag is set.
- **Wildcard key expression:** Iterates using `prefix_iterator_cf` on the `data_info` column family (to avoid loading payloads during the scan), then fetches matching payloads.

---

## Persistence Guarantees

**Durability class:** `Persistence::Durable` (as declared in the plugin's `Capability`).

### Write-Ahead Log (WAL)

RocksDB uses a WAL to make writes durable before acknowledging them. Every `WriteBatch` commit (both PUT and DELETE operations) is appended to the WAL sequentially on disk. A write is durable once it reaches the WAL, even before it is compacted into SSTables.

### What Survives a Crash

| Scenario | Data preserved? |
|---|---|
| Normal process exit | Yes — `db.flush()` is called on drop |
| SIGKILL / `kill -9` | Yes — WAL replay recovers all committed writes |
| OS crash / power loss (with fsync) | Yes — WAL entries that were fsync'd are recovered |
| OS crash / power loss (without fsync, battery-backed cache) | Usually yes — depends on hardware write cache |
| Storage media failure | No — use replication or backups |

RocksDB's default `Options` use the kernel's page cache and do not force an `fsync` per write (sync mode is `false` by default). In practice on SSDs, writes are durable within the OS write cache flush interval. For strict durability guarantees on power loss without battery-backed cache, you would need to set `sync = true` in RocksDB options — this is not currently configurable from zenoh's JSON5 config.

### Crash Recovery

1. On startup, RocksDB checks for a `LOCK` file in the database directory. If the file exists from a previous crashed process, it is cleared and the WAL is replayed.
2. WAL replay re-applies all committed `WriteBatch` entries that were not yet flushed to SSTables.
3. Any `WriteBatch` that was written to the WAL but not `fsync`'d before the crash may be lost (the OS buffer flush window, typically milliseconds to seconds).
4. Recovery is automatic and typically completes in under one second for databases with normal-sized WALs.
5. After recovery, normal operation resumes — no manual intervention is needed.

### Compaction

RocksDB's background compaction merges SSTables, reclaims deleted-key space, and reduces read amplification. Compaction runs automatically in background threads and does not block reads or writes. The default RocksDB configuration uses **Leveled Compaction**, which targets a read amplification of ~10 levels and a write amplification of ~10–30x (meaning each byte written externally causes 10–30 bytes of internal I/O over the lifetime of the data).

---

## Performance Characteristics

### Write Amplification

**Write amplification** is the ratio of bytes written to disk relative to bytes written by the application. For RocksDB with Leveled Compaction:

- Typical factor: **10–30x** for mixed workloads
- Sequential append-only workloads: closer to **5–10x**
- This means a 1 GB/day application write rate drives 10–30 GB/day of actual disk I/O

Write amplification is the main trade-off of LSM-tree designs: you get excellent write throughput at the cost of background I/O.

### Memory Usage

RocksDB uses memory in three main areas:

| Component | Purpose | Notes |
|---|---|---|
| **Memtable** | Write buffer before flush | Default: 64 MB per column family. Zenoh uses 2 CFs, so ~128 MB default |
| **Block cache** | LRU cache for SSTable data blocks | Default: 8 MB (shared across CFs). Increase for read-heavy workloads |
| **Bloom filters** | Probabilistic skip of SSTables | Included in block cache; reduces unnecessary SSTable reads for point lookups |

The default configuration is conservative. For high-throughput deployments, increase the block cache by building with custom `Options`.

### Throughput (estimates)

These are rough estimates for default configuration on NVMe SSD:

| Operation | Approximate throughput |
|---|---|
| Sequential writes (PUT) | 50,000–200,000 ops/sec |
| Point reads (exact GET) | 20,000–100,000 ops/sec |
| Prefix scans (wildcard GET) | Depends on result set size |

Actual throughput depends heavily on value size, key cardinality, available memory, and storage hardware.

### Concurrency

The backend wraps the `DB` handle in `Arc<Mutex<Option<DB>>>` (a single async mutex). All operations — PUT, DELETE, GET, and `get_all_entries` — serialize through this mutex. This means concurrent requests to the same storage are **single-threaded** at the database level. For workloads requiring high concurrency, consider multiple storages with disjoint key expressions backed by separate RocksDB databases.

---

## Example Configurations

### 1. Basic RocksDB Storage (Start Fresh)

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        rocksdb: {}
      },
      storages: {
        sensors: {
          key_expr: "factory/sensors/**",
          strip_prefix: "factory/sensors",
          volume: {
            id: "rocksdb",
            dir: "sensors-db",     // Stored at ${ZENOH_BACKEND_ROCKSDB_ROOT}/sensors-db/
            create_db: true        // Create if not present
          }
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
```

Start the router:
```bash
export ZENOH_BACKEND_ROCKSDB_ROOT=/var/lib/zenoh
zenohd -c zenoh.json5
```

Test:
```bash
# Publish a value
curl -X PUT -d '{"temperature": 23.5}' http://localhost:8000/factory/sensors/hall/temp

# Query all stored values
curl http://localhost:8000/factory/sensors/**

# Query a specific key
curl http://localhost:8000/factory/sensors/hall/temp
```

---

### 2. Read-Only Storage (Serve Pre-existing Data)

Use this when the database was populated externally (another node, a migration script, or a previous zenoh instance) and you want to expose it read-only to the zenoh network.

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        rocksdb: {}
      },
      storages: {
        archive: {
          key_expr: "archive/2024/**",
          strip_prefix: "archive/2024",
          volume: {
            id: "rocksdb",
            dir: "archive-2024",   // Pre-existing database directory
            read_only: true        // Refuse all PUT and DELETE
            // Note: create_db omitted — database must already exist
          }
        }
      }
    }
  }
}
```

Attempting to PUT to a read-only storage:
```bash
curl -X PUT -d "data" http://localhost:8000/archive/2024/event/001
# Returns an error; the storage logs:
#   WARN Received PUT for read-only DB on Some("event/001") - ignored
```

---

### 3. Ephemeral RocksDB Storage (Auto-Cleanup on Removal)

Use this for temporary caches or experiment storages that should be wiped when the storage is removed or the router shuts down.

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        rocksdb: {}
      },
      storages: {
        experiment: {
          key_expr: "experiment/run42/**",
          strip_prefix: "experiment/run42",
          volume: {
            id: "rocksdb",
            dir: "run42-db",
            create_db: true,
            on_closure: "destroy_db"  // Delete all files when storage is removed
          }
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
```

To manually remove the storage at runtime (triggers `destroy_db`):
```bash
curl -X DELETE http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/experiment
```

---

## Runtime Management via Admin Space

You can add and remove storages without restarting the router by writing to the zenoh admin space. Start the router with admin write permissions:

```bash
zenohd --adminspace-permissions=rw --rest-http-port=8000
```

**Add the rocksdb volume (load the plugin):**
```bash
curl -X PUT \
  -H 'content-type:application/json' \
  -d '{}' \
  http://localhost:8000/@/local/router/config/plugins/storage_manager/volumes/rocksdb
```

**Add a storage:**
```bash
curl -X PUT \
  -H 'content-type:application/json' \
  -d '{
    "key_expr": "demo/example/**",
    "strip_prefix": "demo/example",
    "volume": {
      "id": "rocksdb",
      "dir": "example",
      "create_db": true
    }
  }' \
  http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/demo
```

**Remove a storage** (triggers `on_closure` behavior):
```bash
curl -X DELETE \
  http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/demo
```

**Inspect volume status:**
```bash
curl http://localhost:8000/@/local/router/status/plugins/storage_manager/volumes/rocksdb
# Returns: {"root": "/home/user/.zenoh/zenoh_backend_rocksdb", "version": "1.7.2"}
```

---

## Rust API Example

```rust
use zenoh::prelude::*;

#[tokio::main]
async fn main() {
    // Open a zenoh session with RocksDB storage configured inline
    let config = zenoh::Config::from_file("zenoh.json5").unwrap();
    let session = zenoh::open(config).await.unwrap();

    // Publish a value — will be stored by the RocksDB backend
    session
        .put("factory/sensors/hall/temp", "23.5")
        .await
        .unwrap();

    // Query the stored value back
    let replies = session
        .get("factory/sensors/**")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                println!(
                    "Key: {} | Value: {:?}",
                    sample.key_expr(),
                    sample.payload()
                );
            }
            Err(e) => eprintln!("Error: {:?}", e),
        }
    }

    session.close().await.unwrap();
}
```

Cargo.toml:
```toml
[dependencies]
zenoh = { version = "1.7.2", features = ["unstable"] }
tokio = { version = "1", features = ["full"] }
```

---

## Python API Example

```python
import zenoh
import json

def main():
    # Configure with RocksDB storage
    conf = zenoh.Config.from_file("zenoh.json5")

    with zenoh.open(conf) as session:
        # Publish values — stored in RocksDB
        session.put("factory/sensors/hall/temp", json.dumps({"value": 23.5}))
        session.put("factory/sensors/hall/humidity", json.dumps({"value": 65.2}))

        # Query stored values
        replies = session.get("factory/sensors/**", zenoh.Queue())

        for reply in replies:
            try:
                print(f"Key: {reply.ok.key_expr} | Value: {reply.ok.payload.decode('utf-8')}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Install:
```bash
pip install eclipse-zenoh
```

---

## Troubleshooting

### "Failed to open data-info database"

The `dir` path does not exist and `create_db` was not set to `true`.

Fix: Add `create_db: true` to the volume config, or manually create the directory.

### "rocksdb backed storages need volume-specific configurations"

The `volume` block is missing or not an object. Every RocksDB storage requires at minimum `{ id: "rocksdb", dir: "..." }`.

### SIGSEGV on startup

The backend library was built with a different Rust version or different zenoh version than `zenohd`. Rebuild with the exact Rust version reported by `zenohd --version`.

### "Received update for read-only DB"

A PUT or DELETE was sent to a storage configured with `read_only: true`. Either remove `read_only` or use a different storage for writes.

### High disk usage

RocksDB SSTable files accumulate until compaction runs. This is normal; compaction reclaims space automatically. If disk usage grows unbounded, check that background compaction is not blocked (monitor RocksDB's `LOG` file in the database directory for compaction errors).

### Lock file prevents reopening after crash

RocksDB uses a `LOCK` file in the database directory to prevent concurrent opens. If a zenoh router crashed, the `LOCK` file may block reopening on the next start. RocksDB resolves this automatically on `DB::open` — you do not need to delete the `LOCK` file manually. If the open still fails, check that no other `zenohd` process has the database open.

## See Also

- [Plugin Storage Manager Guide](plugin-storage-manager-guide.md) — the storage manager plugin that loads and manages RocksDB storages
- [Storage Backends Guide](storage-backends-guide.md) — when to choose RocksDB vs filesystem, InfluxDB, or S3
