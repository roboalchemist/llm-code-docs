# Zenoh InfluxDB Backend Plugin Guide

## Table of Contents

- [Overview](#overview)
  - [Concept Mapping](#concept-mapping)
- [v1 vs v2: Key Differences](#v1-vs-v2-key-differences)
  - [When to Use Which](#when-to-use-which)
  - [Build Targets](#build-targets)
- [Installation](#installation)
  - [Debian / Ubuntu](#debian-ubuntu)
  - [Manual (all platforms)](#manual-all-platforms)
- [Configuration Reference](#configuration-reference)
  - [Volume Configuration (v1)](#volume-configuration-v1)
  - [Volume Configuration (v2)](#volume-configuration-v2)
  - [Storage Configuration (v1 and v2)](#storage-configuration-v1-and-v2)
  - [Storage-level `key_expr` and `strip_prefix`](#storage-level-key_expr-and-strip_prefix)
- [Complete Working Configs](#complete-working-configs)
  - [InfluxDB v1 Storage](#influxdb-v1-storage)
  - [InfluxDB v2 Storage](#influxdb-v2-storage)
  - [Multiple Storages: Time-Series Sensor Pattern](#multiple-storages-time-series-sensor-pattern)
- [Zenoh Timestamp → InfluxDB Timestamp Mapping](#zenoh-timestamp-influxdb-timestamp-mapping)
- [GET Behavior: Default vs Time-Series](#get-behavior-default-vs-time-series)
- [`_time` Selector Syntax](#_time-selector-syntax)
  - [Format](#format)
  - [Time Expression Types](#time-expression-types)
  - [Using `_time` from Rust](#using-_time-from-rust)
  - [Using `_time` from Python](#using-_time-from-python)
  - [Using `_time` via curl (REST plugin)](#using-_time-via-curl-rest-plugin)
- [Wildcard Query Fan-Out (v1 Only)](#wildcard-query-fan-out-v1-only)
  - [Regex Conversion Rules](#regex-conversion-rules)
  - [v2 Limitation](#v2-limitation)
  - [Performance Implications](#performance-implications)
- [Deletion Behavior](#deletion-behavior)
  - [v1 Behavior](#v1-behavior)
  - [v2 Behavior](#v2-behavior)
  - [Late-Arriving PUT Protection](#late-arriving-put-protection)
- [Runtime Configuration via Admin Space](#runtime-configuration-via-admin-space)
- [Retention Policy Interaction](#retention-policy-interaction)
  - [`on_closure` vs Retention Policies](#on_closure-vs-retention-policies)
- [Quick-Start Example](#quick-start-example)
- [Troubleshooting](#troubleshooting)
  - ["Database doesn't exist in InfluxDb"](#database-doesnt-exist-in-influxdb)
  - ["The InfluxDB credentials are not for an admin user"](#the-influxdb-credentials-are-not-for-an-admin-user)
  - ["Admin creds not provided. Can't proceed without them." (v2)](#admin-creds-not-provided-cant-proceed-without-them-v2)
  - [Wildcard queries return no results (v2)](#wildcard-queries-return-no-results-v2)
  - [ABI crash (SIGSEGV) on startup](#abi-crash-sigsegv-on-startup)
  - [Wrong volume name](#wrong-volume-name)

## Overview

The Zenoh InfluxDB backend plugin stores key/value publications made via zenoh into an InfluxDB time-series database and returns stored values on queries. It ships as two separate libraries — one for InfluxDB v1.x (`zenoh_backend_influxdb`) and one for InfluxDB v2.x (`zenoh_backend_influxdb2`) — because the two InfluxDB versions have incompatible wire protocols and query languages.

### Concept Mapping

| Zenoh concept | InfluxDB concept |
|---------------|-----------------|
| Storage | Database (v1) / Bucket (v2) |
| Key expression | Measurement name (after `strip_prefix`) |
| Published value | Point with nanosecond timestamp |
| PUT | Point tagged `kind="PUT"` |
| DELETE | Delete older points + tombstone point tagged `kind="DEL"` |

Each point written to InfluxDB carries the following fields and tags:

| Column | Type | Description |
|--------|------|-------------|
| `kind` | tag (string) | `"PUT"` or `"DEL"` |
| `timestamp` | field (string) | Full zenoh NTP-based timestamp |
| `encoding_prefix` | field (u8/i64) | Zenoh encoding ID |
| `encoding_suffix` | field (string) | Zenoh encoding string representation |
| `base64` | field (bool) | Whether the value is base64-encoded |
| `value` | field (string) | Payload, possibly base64-encoded for binary data |

---

## v1 vs v2: Key Differences

### When to Use Which

| Criteria | InfluxDB v1 | InfluxDB v2 |
|----------|-------------|-------------|
| InfluxDB version | 1.x only | 2.x (including InfluxDB Cloud) |
| Query language | InfluxQL (SQL-like) | Flux (functional pipeline) |
| Wildcard queries (`*`, `**`) | **Fully supported** | **Not supported** |
| `drop_series` on_closure | Supported | Supported (deletes all data via time range) |
| Measurement drop after delete | Yes (after 5 second delay) | No (API limitation) |
| Authentication | username + password | API token + org_id |
| Library name | `zenoh_backend_influxdb` | `zenoh_backend_influxdb2` |
| Cargo package | `zenoh-backend-influxdb-v1` | `zenoh-backend-influxdb-v2` |
| Debian package | `zenoh-backend-influxdb-v1` | `zenoh-backend-influxdb-v2` |
| Volume name in config | `influxdb` | `influxdb2` |
| URL format | `http://localhost:8086` | `http://localhost:8086/api/v2/` |

The critical limitation to understand: **wildcard key expression queries (using `*` or `**`) only work with InfluxDB v1**. The v2 API does not expose the measurement-level regex filtering needed to fan out across multiple measurements in a single query. If your application issues queries like `sensors/**` that span multiple keys, you must use v1.

### Build Targets

The workspace contains two sub-crates. Build only what you need:

```bash
# Build v1 backend only
cargo build --release --all-targets -p zenoh-backend-influxdb-v1

# Build v2 backend only
cargo build --release --all-targets -p zenoh-backend-influxdb-v2

# Build both
cargo build --release --all-targets
```

The compiled `.so` / `.dylib` / `.dll` must be placed in the same directory as `zenohd`, or in `~/.zenoh/lib`, or `/usr/lib`.

**ABI Warning**: The backend library must be built with the exact same Rust toolchain version as `zenohd`. ABI mismatch causes `SIGSEGV` at runtime. Always check: `zenohd --version` → use the same rustc version.

---

## Installation

### Debian / Ubuntu

```bash
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt update

# For InfluxDB v1
sudo apt install zenoh-backend-influxdb-v1

# For InfluxDB v2
sudo apt install zenoh-backend-influxdb-v2
```

### Manual (all platforms)

Download from `https://download.eclipse.org/zenoh/zenoh-backend-influxdb/latest/`, choose your target platform, unzip into `~/.zenoh/lib/`.

---

## Configuration Reference

Configuration lives inside `plugins.storage_manager` in a JSON5 file passed to `zenohd -c zenoh.json5`.

There are two levels:
- **Volume config** — connection to the InfluxDB server (shared across storages)
- **Storage config** — per-storage database/bucket settings

Credentials should always be placed inside a `private:` block to prevent them from being exposed when the router configuration is queried via the admin space.

---

### Volume Configuration (v1)

The volume section key must be `influxdb` (exactly).

#### `url`
- **Type**: string
- **Required**: yes
- **Description**: HTTP URL to the InfluxDB v1 service. Do not append a path.
- **Example**: `"http://localhost:8086"`

#### `username` *(private)*
- **Type**: string
- **Required**: no (but needed for database creation/drop)
- **Description**: InfluxDB admin username. Used to create databases, grant privileges, and drop databases. Must be an admin user if you need `create_db: true`. If the credentials are not for an admin, zenoh logs a warning and skips database creation/drop operations.
- **Example**: `"admin"`

#### `password` *(private)*
- **Type**: string
- **Required**: no (must coexist with `username` if provided)
- **Description**: InfluxDB admin password.
- **Example**: `"my-admin-password"`

Both `username` and `password` must be provided together or not at all.

```json5
influxdb: {
  url: "http://localhost:8086",
  private: {
    username: "admin",
    password: "my-admin-password"
  }
}
```

---

### Volume Configuration (v2)

The volume section key must be `influxdb2` (exactly).

#### `url`
- **Type**: string
- **Required**: yes
- **Description**: HTTP URL to the InfluxDB v2 API. **Must include `/api/v2/`** as a path suffix.
- **Example**: `"http://localhost:8086/api/v2/"`

#### `org_id` *(private)*
- **Type**: string
- **Required**: yes (v2 requires credentials; unlike v1, credentials cannot be omitted)
- **Description**: InfluxDB organization ID (not the organization name). Used to create and delete buckets. Obtain from the InfluxDB UI under Organization Settings.
- **Example**: `"a1b2c3d4e5f60001"`

#### `token` *(private)*
- **Type**: string
- **Required**: yes
- **Description**: InfluxDB API token for admin operations (bucket creation/deletion). Recommended: ALL-ACCESS token. Minimum: permission to create and delete buckets. If you only need to access an existing bucket, an operator token or read/write token works.
- **Example**: `"my-all-access-token=="`

```json5
influxdb2: {
  url: "http://localhost:8086/api/v2/",
  private: {
    org_id: "a1b2c3d4e5f60001",
    token: "my-all-access-token=="
  }
}
```

---

### Storage Configuration (v1 and v2)

Storage config goes inside `volume: { ... }` within each named storage.

#### `id`
- **Type**: string
- **Required**: yes
- **Description**: Must match the volume name exactly (`"influxdb"` for v1, `"influxdb2"` for v2).

#### `db`
- **Type**: string
- **Required**: no
- **Default**: If omitted, a random UUID-based name is generated in the format `zenoh_db_<uuid>` and the database is auto-created.
- **Description**: The InfluxDB database name (v1) or bucket name (v2) this storage maps to.
- **Example**: `"my_sensor_data"`

#### `create_db`
- **Type**: boolean (only the key's presence matters; value is checked but the key presence triggers creation)
- **Required**: no
- **Default**: `false` (database is not created unless `db` is omitted)
- **Description**: When `true`, create the InfluxDB database/bucket if it does not already exist. Requires admin credentials in the volume config. If the database already exists and `create_db: true`, v2 logs a warning but continues normally. On v1, the admin client must be able to see `_internal` in `SHOW DATABASES` — if not, a warning is logged that creation/drop won't work.
- **Example**: `create_db: true`

#### `on_closure`
- **Type**: string
- **Required**: no
- **Default**: `"do_nothing"`
- **Valid values**:
  - `"do_nothing"` — The database/bucket remains untouched when the storage is removed. Use this for persistent production data.
  - `"drop_db"` — Drop (delete) the entire database/bucket when the storage is closed. Use for ephemeral/test storages.
  - `"drop_series"` — Drop all measurements/series data but keep the empty database/bucket. On v2, this is implemented by deleting all data in the full supported time range (`1677-09-21T00:12:44Z` to `2262-04-11T23:47:16Z`).
- **Example**: `on_closure: "drop_db"`

#### `username` *(private, v1 only)*
- **Type**: string
- **Required**: no
- **Description**: Non-admin InfluxDB user for read/write operations on this storage's database. If the admin credentials created the database, the user is granted `ALL` privileges via `GRANT ALL ON "db" TO "user"`. Must coexist with `password`.
- **Example**: `"reader_writer"`

#### `password` *(private, v1 only)*
- **Type**: string
- **Required**: no (must coexist with `username`)
- **Description**: Password for the storage-level user.
- **Example**: `"rw-password"`

#### `org_id` *(private, v2 only)*
- **Type**: string
- **Required**: no (falls back to volume-level `org_id` if not provided)
- **Description**: Organization ID for read/write operations. Should be the same as the admin org_id.
- **Example**: `"a1b2c3d4e5f60001"`

#### `token` *(private, v2 only)*
- **Type**: string
- **Required**: no (falls back to volume-level token if not provided)
- **Description**: Read/write API token for this storage's bucket. Two token types work:
  - A token with Read+Write access to the specific named bucket (when bucket already exists)
  - A token with Read+Write access to all buckets (when zenoh needs to create a new bucket)
- **Example**: `"my-readwrite-token=="`

---

### Storage-level `key_expr` and `strip_prefix`

These are standard zenoh storage fields (not InfluxDB-specific):

- **`key_expr`** — Key expression this storage subscribes to and answers queries for. Example: `"sensors/**"`
- **`strip_prefix`** — Optional prefix stripped from the key before using it as the InfluxDB measurement name. Example: strip `"sensors"` so `"sensors/temperature/room1"` stores as `"temperature/room1"`.

---

## Complete Working Configs

### InfluxDB v1 Storage

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        influxdb: {
          url: "http://localhost:8086",
          private: {
            username: "admin",
            password: "admin-secret"
          }
        }
      },
      storages: {
        sensor_v1: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",
          volume: {
            id: "influxdb",
            db: "zenoh_sensors",
            create_db: true,
            on_closure: "do_nothing",
            private: {
              username: "zenoh_rw",
              password: "rw-secret"
            }
          }
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
```

### InfluxDB v2 Storage

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        influxdb2: {
          url: "http://localhost:8086/api/v2/",
          private: {
            org_id: "a1b2c3d4e5f60001",
            token: "my-all-access-token=="
          }
        }
      },
      storages: {
        sensor_v2: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",
          volume: {
            id: "influxdb2",
            db: "zenoh_sensors",
            create_db: true,
            on_closure: "do_nothing",
            private: {
              org_id: "a1b2c3d4e5f60001",
              token: "my-readwrite-token=="
            }
          }
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
```

### Multiple Storages: Time-Series Sensor Pattern

This config defines separate buckets for different sensor categories, a short-lived ephemeral cache, and a long-term archive.

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        influxdb: {
          url: "http://influxdb:8086",
          private: {
            username: "admin",
            password: "admin-secret"
          }
        }
      },
      storages: {
        // Temperature sensors — persistent
        temperature: {
          key_expr: "factory/sensors/temperature/**",
          strip_prefix: "factory/sensors/temperature",
          volume: {
            id: "influxdb",
            db: "temperature_data",
            create_db: true,
            on_closure: "do_nothing",
            private: {
              username: "zenoh_rw",
              password: "rw-secret"
            }
          }
        },

        // Pressure sensors — persistent
        pressure: {
          key_expr: "factory/sensors/pressure/**",
          strip_prefix: "factory/sensors/pressure",
          volume: {
            id: "influxdb",
            db: "pressure_data",
            create_db: true,
            on_closure: "do_nothing",
            private: {
              username: "zenoh_rw",
              password: "rw-secret"
            }
          }
        },

        // Ephemeral test cache — auto-dropped on shutdown
        test_cache: {
          key_expr: "test/**",
          volume: {
            id: "influxdb",
            // db omitted: auto-generated UUID name, auto-created
            on_closure: "drop_db",
            private: {
              username: "admin",
              password: "admin-secret"
            }
          }
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
```

---

## Zenoh Timestamp → InfluxDB Timestamp Mapping

Zenoh uses a **Hybrid Logical Clock (HLC/UHLC)** based on NTP. Each timestamp has two components:
- A 64-bit NTP time (seconds + fractional seconds since Unix epoch)
- A 128-bit UUID for the clock ID (to distinguish clocks across nodes)

When a value is stored:

1. The zenoh timestamp's NTP time component is converted to a `Duration` since Unix epoch via `timestamp.get_time().to_duration()`.
2. The duration is expressed in **nanoseconds** (`as_nanos()`).
3. This nanosecond value is used as the InfluxDB point timestamp.

```
zenoh Timestamp (NTP) → Duration since epoch → nanoseconds → InfluxDB timestamp
```

**Precision**: Always nanoseconds. InfluxDB v1 uses nanoseconds natively. InfluxDB v2 accepts nanoseconds as `i64`.

**The full zenoh timestamp string** (including UUID) is also stored separately as the `timestamp` field within each point. This full string is used when returning results — the HLC timestamp is reconstructed from it, not from the InfluxDB point time. This preserves the UUID component needed for distributed causality tracking.

**Ordering**: Because the InfluxDB point time is derived from the NTP component of the zenoh timestamp, ordering in InfluxDB matches zenoh's logical time ordering. Out-of-order messages are handled explicitly: on DELETE, all older points are purged, and a tombstone is inserted so late-arriving PUTs with timestamps older than the deletion are silently dropped (the `get_deletion_timestamp` check in `put()`).

---

## GET Behavior: Default vs Time-Series

By default, a GET returns only the **latest point** per measurement. This mimics the behavior of key-value backends (one value per key).

```
GET sensors/temperature/room1
→ returns: most recent PUT for that key
```

To retrieve time-series history, add a `_time` selector argument:

```
GET sensors/temperature/room1?_time=[..]
→ returns: all points ever stored for that key
```

The backend's query logic:
- No `_time` parameter → appends `ORDER BY time DESC LIMIT 1` (v1) or `|> last()` (v2)
- `_time` parameter present → translates time bounds into InfluxDB WHERE clauses (v1) or `range()` filters (v2)

---

## `_time` Selector Syntax

The `_time` parameter follows the [zenoh `_time` RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Selectors/_time.md).

### Format

```
_time=[<start>..<end>]
```

Bounds use `..` as separator. Either bound can be omitted for open-ended ranges.

### Time Expression Types

**Unbounded** (all history):
```
_time=[..]
```

**Absolute timestamps** — ISO 8601 with nanosecond precision:
```
_time=[2024-01-01T00:00:00Z..2024-01-02T12:00:00.000000000Z]
```

**Relative timestamps** — `now(offset)` where offset is a signed duration:
```
_time=[now(-1h)..]           # last 1 hour to now
_time=[now(-30m)..now(-5m)]  # 30 min ago to 5 min ago
_time=[now(-1d)..now(-12h)]  # 24h ago to 12h ago
_time=[now(-2d)..now(-1d)]   # day before yesterday
```

Supported offset units: `s` (seconds), `m` (minutes), `h` (hours), `d` (days).

### Using `_time` from Rust

```rust
use zenoh::prelude::*;
use zenoh::config::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // Get all history
    let replies = session
        .get("sensors/temperature/room1?_time=[..]")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                let ts = sample.timestamp().unwrap();
                let value: String = sample.payload().try_to_string().unwrap().into();
                println!("ts={ts} val={value}");
            }
            Err(e) => eprintln!("Error: {e:?}"),
        }
    }

    // Get last hour of data
    let replies = session
        .get("sensors/temperature/room1?_time=[now(-1h)..]")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            println!("{:?}", sample.payload().try_to_string());
        }
    }
}
```

### Using `_time` from Python

```python
import zenoh
import time

config = zenoh.Config()
with zenoh.open(config) as session:
    # Get all history for a single key
    replies = session.get("sensors/temperature/room1?_time=[..]")
    for reply in replies:
        if reply.ok:
            print(f"ts={reply.ok.timestamp} val={bytes(reply.ok.payload).decode()}")

    # Get last 30 minutes across all rooms (v1 only — wildcard)
    replies = session.get("sensors/temperature/**?_time=[now(-30m)..]")
    for reply in replies:
        if reply.ok:
            print(f"key={reply.ok.key_expr} val={bytes(reply.ok.payload).decode()}")
```

### Using `_time` via curl (REST plugin)

```bash
# All history
curl -g 'http://localhost:8000/sensors/temperature/room1?_time=[..]'

# Fixed date range
curl -g 'http://localhost:8000/sensors/temperature/room1?_time=[2024-01-01T00:00:00Z..2024-01-02T00:00:00Z]'

# Last 2 hours
curl -g 'http://localhost:8000/sensors/temperature/room1?_time=[now(-2h)..]'

# The -g flag prevents curl from interpreting [] as glob patterns
```

---

## Wildcard Query Fan-Out (v1 Only)

When a zenoh GET key expression contains `*` or `**`, the InfluxDB v1 backend converts it to an InfluxDB regex and issues a single `SELECT * FROM /regex/ WHERE ...` query that matches multiple measurements in one round trip.

### Regex Conversion Rules

The `key_exprs_to_influx_regex` function applies these transformations:

| Zenoh pattern | InfluxDB regex fragment |
|---------------|------------------------|
| `**` | `.*` |
| `*` | `.*` |
| `/` | `\/` |

Result is wrapped in `/^...$/.`. For example:

```
sensors/temperature/**  →  /^sensors\/temperature\/.*$/
factory/*/pressure      →  /^factory\/.*\/pressure$/
**                      →  /^.*$/
```

The generated InfluxDB query looks like:

```sql
SELECT * FROM /^sensors\/temperature\/.*$/ WHERE kind!='DEL' AND time >= '2024-01-01T00:00:00Z'
```

### v2 Limitation

InfluxDB v2's Flux query language does not support querying across multiple measurements with a single regex filter in the same way. The v2 backend can filter `_measurement` by regex in Flux using `=~`, but the InfluxDB v2 client library used (`influxdb2` crate) does not expose this cleanly for cross-measurement fan-out. As a result, wildcard queries in v2 return empty results or are silently constrained to a single measurement.

**If you need wildcard queries across many keys, use InfluxDB v1.**

### Performance Implications

- Each `**` query issues exactly one InfluxDB query regardless of how many measurements match.
- Adding a `_time` filter (e.g., `_time=[now(-1h)..]`) is strongly recommended for wildcard queries on large databases, as `SELECT * FROM /.*$/` without a time bound will scan all data.
- Without a time bound, the default behavior (`LIMIT 1 ORDER BY time DESC`) applies per measurement, which is efficient — it reads only the latest point from each matching measurement.

---

## Deletion Behavior

When zenoh deletes a key:

### v1 Behavior
1. Delete all points older than the deletion timestamp:
   ```sql
   DELETE FROM "measurement" WHERE time < <influx_nanosecond_timestamp>
   ```
2. Insert a tombstone point with `kind="DEL"` at the deletion timestamp.
3. Schedule a background task (5 second delay) to check if the measurement is now empty. If it contains no non-DEL points, drop the measurement entirely with `DROP MEASUREMENT "measurement"`. This cleanup keeps the database tidy.

### v2 Behavior
1. Delete all points from Unix epoch to the deletion timestamp using the InfluxDB v2 delete API.
2. Insert a tombstone point with `kind="DEL"` at the deletion timestamp.
3. **No measurement drop** — InfluxDB v2 does not support dropping individual measurements via the API. The empty measurement (containing only the DEL tombstone) remains.

### Late-Arriving PUT Protection

The tombstone mechanism protects against late-arriving network messages. If a PUT arrives with a timestamp older than an existing DEL tombstone, the `put()` handler queries for the latest DEL timestamp and silently drops the outdated PUT (returning `StorageInsertionResult::Outdated`).

---

## Runtime Configuration via Admin Space

Instead of a config file, storages can be added/removed at runtime using the admin space API (requires `--adminspace-permissions=rw`).

```bash
# Start zenohd with admin write access
zenohd --adminspace-permissions=rw --rest-http-port=8000

# Add a v1 volume
curl -X PUT -H 'content-type:application/json' \
  -d '{url:"http://localhost:8086"}' \
  'http://localhost:8000/@/local/router/config/plugins/storage_manager/volumes/influxdb'

# Add a storage on that volume
curl -X PUT -H 'content-type:application/json' \
  -d '{key_expr:"sensors/**",strip_prefix:"sensors",volume:{id:"influxdb",db:"sensor_db",create_db:true}}' \
  'http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/sensors'

# Remove the storage (triggers on_closure behavior)
curl -X DELETE \
  'http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/sensors'
```

For v2, use `influxdb2` as the volume name and include `on_closure` in the storage config if needed.

---

## Retention Policy Interaction

The InfluxDB backend itself does not configure or manage retention policies. Retention is handled entirely at the InfluxDB level.

**InfluxDB v1**: Configure retention policies directly in InfluxDB (`CREATE RETENTION POLICY`). Zenoh writes to the `DEFAULT` retention policy unless you configure InfluxDB to route to a specific one. Data expired by InfluxDB's retention policy is silently gone — zenoh storage does not re-recreate or notice the loss.

**InfluxDB v2**: Configure bucket retention in the InfluxDB UI or API when creating the bucket. If zenoh's `create_db: true` creates the bucket, it uses the default infinite retention. To set a specific retention, create the bucket manually in InfluxDB first, then point zenoh at it (with `create_db: false`).

### `on_closure` vs Retention Policies

These are complementary, not competing:

- **Retention policy** — time-based automatic expiry of old data, managed by InfluxDB independently of zenoh.
- **`on_closure`** — action taken when a zenoh storage is explicitly removed (router shutdown, admin space DELETE). Does not interact with retention policies.

A common production pattern: use `on_closure: "do_nothing"` (so data persists across router restarts) combined with an InfluxDB retention policy of 30 or 90 days to bound storage growth.

---

## Quick-Start Example

Prerequisites: `zenohd` installed, InfluxDB v1 running on `localhost:8086`.

```bash
# 1. Create config file
cat > /tmp/zenoh.json5 << 'EOF'
{
  plugins: {
    storage_manager: {
      volumes: {
        influxdb: {
          url: "http://localhost:8086"
        }
      },
      storages: {
        demo: {
          key_expr: "demo/**",
          strip_prefix: "demo",
          volume: {
            id: "influxdb",
            db: "zenoh_demo",
            create_db: true,
            on_closure: "drop_db"
          }
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
EOF

# 2. Start router (library must be in ~/.zenoh/lib/ or same dir as zenohd)
zenohd -c /tmp/zenoh.json5

# 3. Publish some values
curl -X PUT -d "23.5" http://localhost:8000/demo/temperature/room1
curl -X PUT -d "24.1" http://localhost:8000/demo/temperature/room1
curl -X PUT -d "19.2" http://localhost:8000/demo/temperature/room2

# 4. Query latest value (default — no time range)
curl http://localhost:8000/demo/temperature/room1

# 5. Query full time series
curl -g 'http://localhost:8000/demo/temperature/room1?_time=[..]'

# 6. Query last hour across all rooms (wildcard — v1 only)
curl -g 'http://localhost:8000/demo/temperature/**?_time=[now(-1h)..]'
```

---

## Troubleshooting

### "Database doesn't exist in InfluxDb"
`create_db` is not set (or set to `false`) and the named database doesn't exist. Either create it manually in InfluxDB or add `create_db: true` to the storage config.

### "The InfluxDB credentials are not for an admin user"
The volume-level username/password can see databases but not `_internal`. Provide admin credentials in the volume `private` block if you need automatic database creation/drop.

### "Admin creds not provided. Can't proceed without them." (v2)
InfluxDB v2 backend requires `org_id` and `token` in the volume `private` block. Unlike v1, credentials are mandatory.

### Wildcard queries return no results (v2)
This is a known limitation. Wildcard queries (`*`, `**`) across multiple measurements are not supported by the v2 backend. Use InfluxDB v1 or query each key individually.

### ABI crash (SIGSEGV) on startup
The backend `.so` was compiled with a different Rust toolchain than `zenohd`. Rebuild the backend with the exact rustc version reported by `zenohd --version`.

### Wrong volume name
The volume key in `volumes:` must exactly match the `id:` in each storage's `volume:` block, and must be either `influxdb` (v1) or `influxdb2` (v2). Using the wrong name causes the wrong library to be loaded.

## See Also

- [Plugin Storage Manager Guide](plugin-storage-manager-guide.md) — the storage manager plugin that loads and manages InfluxDB storages
- [Storage Backends Guide](storage-backends-guide.md) — when to choose InfluxDB vs RocksDB or filesystem for your use case
- [Config Connect Listen](config-connect-listen.md) — connect endpoint configuration for reaching the Zenoh router that hosts the InfluxDB storage
