# Zenoh Filesystem Backend Plugin Guide

The `zenoh-backend-filesystem` plugin (library name: `zenoh_backend_fs`) backs zenoh storages with the host's file system. Each published key/value maps to a file, making stored data directly inspectable with standard OS tools. Encoding and timestamp metadata are preserved in a co-located RocksDB sidecar database.

**Version covered**: 1.7.2 (zenoh 1.7.2 / main branch)

---

## Table of Contents

- [Installation](#installation)
  - [Linux (Debian/Ubuntu)](#linux-debianubuntu)
  - [Manual (all platforms)](#manual-all-platforms)
  - [Build from Source](#build-from-source)
- [Architecture Overview](#architecture-overview)
- [Directory Layout and KE-to-Path Mapping](#directory-layout-and-ke-to-path-mapping)
  - [Root Path Resolution](#root-path-resolution)
  - [KE-to-File-Path Mapping](#ke-to-file-path-mapping)
  - [Mapping Examples](#mapping-examples)
  - [The `@root` Special File](#the-root-special-file)
  - [Directory Auto-Creation](#directory-auto-creation)
- [Config Reference](#config-reference)
  - [Volume-Level Config](#volume-level-config)
  - [Storage-Level Config](#storage-level-config)
  - [Config Option Summary Table](#config-option-summary-table)
- [File Naming Details](#file-naming-details)
  - [Direct Mapping (No Escaping)](#direct-mapping-no-escaping)
  - [Conflict Resolution: The `.##z` Suffix](#conflict-resolution-the-z-suffix)
  - [The `.zenoh_datainfo` Directory](#the-zenoh_datainfo-directory)
- [Binary and Text Storage](#binary-and-text-storage)
  - [How Payloads Are Written](#how-payloads-are-written)
  - [Reading Files Written Without Zenoh](#reading-files-written-without-zenoh)
  - [Note: No `base64` Option](#note-no-base64-option)
- [Encoding Preservation](#encoding-preservation)
  - [The `.zenoh_datainfo` RocksDB Sidecar](#the-zenoh_datainfo-rocksdb-sidecar)
  - [Encoding Fields Stored](#encoding-fields-stored)
  - [Timestamp Fields Stored](#timestamp-fields-stored)
  - [Garbage Collection](#garbage-collection)
- [Wildcard Query Behavior](#wildcard-query-behavior)
  - [Scan Algorithm](#scan-algorithm)
  - [Performance Implications](#performance-implications)
  - [The `.zenoh_datainfo` Directory Is Excluded](#the-zenoh_datainfo-directory-is-excluded)
  - [Symlinks During Scans](#symlinks-during-scans)
- [Deletion Behavior](#deletion-behavior)
- [Symlink Handling](#symlink-handling)
- [Complete Config Examples](#complete-config-examples)
  - [1. Basic Filesystem Storage](#1-basic-filesystem-storage)
  - [2. Read-Only Storage (Serving Static Files)](#2-read-only-storage-serving-static-files)
  - [3. Ephemeral Storage — Delete on Shutdown](#3-ephemeral-storage-delete-on-shutdown)
  - [4. Storage with Symlink Support](#4-storage-with-symlink-support)
- [Runtime Admin via REST API](#runtime-admin-via-rest-api)
  - [Start the Router with Admin Access](#start-the-router-with-admin-access)
  - [Add the `fs` Volume](#add-the-fs-volume)
  - [Add a Storage](#add-a-storage)
  - [Remove a Storage](#remove-a-storage)
- [Code Examples](#code-examples)
  - [Rust — Put and Get via Filesystem Storage](#rust-put-and-get-via-filesystem-storage)
  - [Rust — Wildcard GET (Directory Walk)](#rust-wildcard-get-directory-walk)
  - [Python — Put, Get, and Subscribe](#python-put-get-and-subscribe)
  - [Python — Check What's on Disk After PUT](#python-check-whats-on-disk-after-put)
  - [curl — Test via REST API](#curl-test-via-rest-api)
- [Troubleshooting](#troubleshooting)
  - [Storage Fails to Start: "the path must be relative"](#storage-fails-to-start-the-path-must-be-relative)
  - [Files Are Written but GET Returns Nothing](#files-are-written-but-get-returns-nothing)
  - [Encoding Reported as `application/octet-stream` for Known File Types](#encoding-reported-as-applicationoctet-stream-for-known-file-types)
  - [Conflict Files with `.##z` Extension Appearing on Disk](#conflict-files-with-z-extension-appearing-on-disk)
  - [RocksDB Errors on Startup](#rocksdb-errors-on-startup)


---


## Installation

### Linux (Debian/Ubuntu)

```bash
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | \
  sudo tee -a /etc/apt/sources.list.d/zenoh.list > /dev/null
sudo apt update
sudo apt install zenoh-backend-filesystem
```

### Manual (all platforms)

Download the `.zip` for your target from:
`https://download.eclipse.org/zenoh/zenoh-backend-filesystem/latest/`

Unzip into the same directory as `zenohd`, or into any directory on the library search path (e.g. `~/.zenoh/lib`).

### Build from Source

The library **must** be built with the same Rust toolchain version as `zenohd`:

```bash
# Check what version zenohd was built with
zenohd --version
# Example output: The zenoh router v1.7.2 built with rustc 1.82.0

rustup default 1.82.0
cargo build --release --all-targets
```

> **Warning**: Rust has no stable ABI. A version mismatch between `zenohd` and the backend library will cause a SIGSEGV at load time.

---

## Architecture Overview

```
zenoh publisher                         zenoh subscriber / querier
     │                                           ▲
     │  PUT demo/example/sensors/temp            │  GET demo/example/**
     ▼                                           │
┌─────────────────────────────────────────────────────────────┐
│                    zenohd (router)                          │
│  storage-manager plugin                                     │
│  └── "fs" volume  ──►  zenoh_backend_fs (this library)     │
└─────────────────────────────────────────────────────────────┘
     │                                           ▲
     │  write raw bytes                          │  read file + lookup RocksDB
     ▼                                           │
${ZENOH_BACKEND_FS_ROOT}/
└── example/                          ← storage dir
    └── sensors/
        └── temp                      ← data file (raw bytes)
    └── .zenoh_datainfo/              ← RocksDB: encoding + timestamp index
```

The `ZENOH_BACKEND_FS_ROOT` environment variable sets the root for **all** storages managed by this backend instance. If unset, it falls back to `${ZENOH_HOME}/zenoh_backend_fs` where `ZENOH_HOME` defaults to `~/.zenoh`. So if `ZENOH_HOME` is set to `/opt/zenoh`, the default root will be `/opt/zenoh/zenoh_backend_fs`, not `~/.zenoh/zenoh_backend_fs`.

---

## Directory Layout and KE-to-Path Mapping

### Root Path Resolution

Each storage gets a directory at:

```
${ZENOH_BACKEND_FS_ROOT}/<dir>
```

where `<dir>` is the `dir` config value (must be a relative path; `..` components are rejected).

If `ZENOH_BACKEND_FS_ROOT` is not set:

```
~/.zenoh/zenoh_backend_fs/<dir>
```

### KE-to-File-Path Mapping

When a key/value is put into a storage, the zenoh key is first stripped of the `strip_prefix` (configured on the storage, not the volume), then mapped directly to a filesystem path:

```
file path = ${ZENOH_BACKEND_FS_ROOT}/<dir>/<key-after-strip_prefix>
```

On **Unix/macOS**: `/` in the key expression maps directly to the path separator `/`.
On **Windows**: `/` in the key expression maps to `\`.

There is no character escaping performed on key chunks — the raw chunk string becomes the file or directory name.

### Mapping Examples

Given `ZENOH_BACKEND_FS_ROOT=/data`, storage `dir=sensors`, `strip_prefix=demo/example`:

| Zenoh Key Expression          | Relative Key (after strip) | File Path                             |
|-------------------------------|---------------------------|---------------------------------------|
| `demo/example/temp`           | `temp`                    | `/data/sensors/temp`                  |
| `demo/example/room/a/temp`    | `room/a/temp`             | `/data/sensors/room/a/temp`           |
| `demo/example/room/a/b`       | `room/a/b`                | `/data/sensors/room/a/b`              |
| `demo/example` (= strip_prefix exactly) | *(root key)*  | `/data/sensors/@root`                 |

### The `@root` Special File

When `strip_prefix` exactly matches the received key, the remaining relative key is empty. The plugin stores this as a file named `@root` directly inside the storage directory. This name is specifically chosen to be invalid as a zenoh key expression chunk, preventing collision with normal keys.

### Directory Auto-Creation

When a PUT is received for a nested key, all required parent directories are created automatically (equivalent to `mkdir -p`). Empty parent directories are pruned on DELETE.

---

## Config Reference

### Volume-Level Config

The `fs` volume requires **no additional configuration** at the volume level. Declaring the volume is sufficient:

```json5
volumes: {
  fs: {}
}
```

Any volume can use the `fs` backend by adding `backend: "fs"` to its config. A volume named `fs` uses the `fs` backend automatically.

### Storage-Level Config

All storage-specific options are placed inside the `volume: { id: "fs", ... }` block of the storage definition.

---

#### `dir`

| Field   | Value                   |
|---------|-------------------------|
| Type    | `string`                |
| Default | *(none — required)*     |
| Valid   | Any relative path with no `..` components |

The subdirectory (relative to `ZENOH_BACKEND_FS_ROOT`) where this storage's files will be written.

- **Must be a relative path** — absolute paths are rejected at startup.
- **Must not contain `..`** — parent traversal is rejected at startup.
- The directory is created automatically if it does not exist.
- If the path exists but is not a directory, startup fails.
- If the path is not writable (and `read_only` is false), startup fails.

```json5
volume: {
  id: "fs",
  dir: "sensors/temperature"   // files go in $ROOT/sensors/temperature/
}
```

---

#### `read_only`

| Field   | Value             |
|---------|-------------------|
| Type    | `boolean`         |
| Default | `false`           |
| Valid   | `true`, `false`   |

When `true`, the storage only answers GET queries. Any incoming PUT or DELETE message is rejected with a warning log and an error response — no files are written or removed. This is useful for serving a pre-populated directory of static files.

```json5
volume: {
  id: "fs",
  dir: "static-content",
  read_only: true
}
```

---

#### `on_closure`

| Field   | Value                          |
|---------|--------------------------------|
| Type    | `string`                       |
| Default | `"do_nothing"`                 |
| Valid   | `"do_nothing"`, `"delete_all"` |

Controls what happens to the storage directory when the storage is removed (e.g. via admin space or router shutdown).

- `"do_nothing"` (default): The storage directory and all its contents remain on disk. Useful for persistent data that outlives the router session.
- `"delete_all"`: The entire storage directory is deleted recursively (equivalent to `rm -rf`). The `.zenoh_datainfo` RocksDB is flushed and destroyed first, then the directory is removed.

```json5
volume: {
  id: "fs",
  dir: "ephemeral-cache",
  on_closure: "delete_all"
}
```

---

#### `follow_links`

| Field   | Value             |
|---------|-------------------|
| Type    | `boolean`         |
| Default | `false`           |
| Valid   | `true`, `false`   |

When `false` (default), the storage **silently skips** any file or directory that is, or is reachable through, a symbolic link during reads (GET / wildcard scans). Note: symlink checks apply only to the read path — PUT operations always write the file regardless of symlinks in the path.

When `true`, symbolic links are traversed normally during reads and scans. The plugin uses `WalkDir::follow_links(true)` for directory traversal, meaning symlinked directories are recursed into.

**Security note**: Enabling `follow_links: true` on storage directories that users or external processes can influence may allow reads from outside the intended root. Use with care in shared environments.

```json5
volume: {
  id: "fs",
  dir: "with-symlinks",
  follow_links: true
}
```

---

#### `keep_mime_types`

| Field   | Value             |
|---------|-------------------|
| Type    | `boolean`         |
| Default | `true`            |
| Valid   | `true`, `false`   |

Controls how encoding is reported for files that were **not** written through zenoh (i.e. files placed in the directory manually, whose encoding is not in the `.zenoh_datainfo` RocksDB).

- `true` (default): The mime type is guessed from the file extension using the [`mime_guess`](https://crates.io/crates/mime_guess) crate. The guessed mime string is used as the zenoh `Encoding` (e.g. `text/plain`, `image/png`). If `mime_guess` returns no match, `application/octet-stream` is used.
- `false`: All externally-placed files are returned with `Encoding::APPLICATION_OCTET_STREAM` regardless of extension.

This option has **no effect** on files written by zenoh — those always have their encoding stored in the RocksDB sidecar and retrieved exactly.

```json5
volume: {
  id: "fs",
  dir: "mixed-content",
  keep_mime_types: false   // always return octet-stream for unknown files
}
```

---

### Config Option Summary Table

| Option           | Type    | Default       | Required | Description                                      |
|------------------|---------|---------------|----------|--------------------------------------------------|
| `dir`            | string  | —             | yes      | Storage root directory (relative to `$FS_ROOT`)  |
| `read_only`      | boolean | `false`       | no       | Serve GET only; reject PUT and DELETE            |
| `on_closure`     | string  | `"do_nothing"`| no       | What to do with data when storage is removed     |
| `follow_links`   | boolean | `false`       | no       | Follow symbolic links during reads and scans     |
| `keep_mime_types`| boolean | `true`        | no       | Guess encoding from file extension for non-zenoh files |

---

## File Naming Details

### Direct Mapping (No Escaping)

Key expression chunks map verbatim to filesystem path components. There is no percent-encoding or character substitution. This means:

- Key `sensors/room-1/temp` → path component `room-1` → directory named `room-1`
- Key `data/file.json` → file named `file.json`

Characters that are invalid in file names on the target OS (e.g. `:`, `*`, `?`, `"` on Windows) should be avoided in key expressions used with this backend.

### Conflict Resolution: The `.##z` Suffix

A conflict arises when a PUT operation targets a key whose path component is already used as both a **file** and a **directory**. For example:

- First PUT: `sensors/temp` → creates file `/data/sensors/temp`
- Second PUT: `sensors/temp/high` → needs `/data/sensors/temp/` to be a *directory*

The plugin resolves this by renaming the conflicting file to `<name>.##z` (the `CONFLICT_SUFFIX`). The RocksDB metadata entry is updated to track the new name. The conflict suffix is invisible to zenoh callers — the plugin trims it when constructing key expressions from file paths.

On GET, the plugin first checks the canonical path, then falls back to the `.##z` variant.

### The `.zenoh_datainfo` Directory

Each storage directory contains a hidden subdirectory named `.zenoh_datainfo` which is the RocksDB database. This directory is:

- Created automatically when the storage is first opened.
- Excluded from wildcard file scans (the `FilesIterator` calls `skip_current_dir()` when encountering it).
- Flushed and destroyed (with `DB::destroy`) when the storage is closed with `on_closure: "delete_all"`.
- **Not** user-editable — modifying RocksDB internals manually will corrupt metadata.

---

## Binary and Text Storage

### How Payloads Are Written

The raw `ZBytes` buffer transported by zenoh is written directly to the file — no encoding or transformation is applied. This means:

- **Text payloads** (encoding `text/plain`, `application/json`, etc.) produce human-readable files.
- **Binary payloads** (encoding `application/octet-stream`, protobuf, etc.) produce binary files.
- The file content is byte-for-byte identical to the zenoh payload.

### Reading Files Written Without Zenoh

Files placed in the storage directory manually (not via zenoh PUT) can be read back with GET. The plugin:

1. Reads the file contents as raw bytes.
2. Looks up encoding/timestamp in `.zenoh_datainfo` — finds nothing.
3. Falls back: guesses encoding from the file extension (if `keep_mime_types: true`), or uses `application/octet-stream` (if `keep_mime_types: false`).
4. Falls back for timestamp: uses the file's `modified` time, then `accessed` time, then `created` time (birth time, not the Unix ctime), then `SystemTime::now()`.

### Note: No `base64` Option

The filesystem backend does **not** have a `base64` configuration option. All data is stored as raw bytes. If you need base64 encoding, apply it at the application layer before publishing.

---

## Encoding Preservation

### The `.zenoh_datainfo` RocksDB Sidecar

When a PUT is received, the plugin saves both the file (raw bytes) and the metadata (encoding + timestamp) sequentially (not in a single atomic transaction — the file is written first, then the RocksDB metadata entry):

1. Raw bytes → written to the file path.
2. `DataInfo { encoding, timestamp }` → serialized and written to RocksDB.

**RocksDB key**: the full absolute file path as a UTF-8 string (e.g. `/data/sensors/temp`).
**RocksDB value**: a zenoh-serialized tuple `(timestamp_time: u64, timestamp_id: [u8; 16], encoding_id: u16, encoding_schema: Vec<u8>)`.

### Encoding Fields Stored

The zenoh `Encoding` type has two parts:

| Field            | Type    | Description                                        |
|------------------|---------|----------------------------------------------------|
| `encoding_id`    | `u16`   | Numeric ID for a known encoding (e.g. `text/plain` = 4) |
| `encoding_schema`| `Vec<u8>` | Optional schema string for custom encodings (e.g. `"protobuf/MyMsg"`) |

Both are stored in the RocksDB entry and restored exactly on GET.

### Timestamp Fields Stored

The zenoh `Timestamp` contains:

| Field            | Type     | Description                                     |
|------------------|----------|-------------------------------------------------|
| `timestamp_time` | `NTP64`  | NTP64-encoded wall clock time (as `u64`)        |
| `timestamp_id`   | `[u8;16]`| Identifier of the node that generated the timestamp |

### Garbage Collection

When a key is deleted, the plugin removes the file and immediately deletes the corresponding RocksDB metadata entry via `del_data_info()`. **Note:** The source code defines GC constants (`GC_PERIOD: 30s`, `MIN_DELAY_BEFORE_REMOVAL: 5s`) but these are currently unused — no background GC task is actually running. Tombstones are not retained; deletion removes both the file and metadata immediately.

---

## Wildcard Query Behavior

### Scan Algorithm

When a GET with a wildcard key expression arrives (e.g. `sensors/**`), the plugin:

1. Finds the **longest non-wildcard prefix** of the key expression. For `sensors/room-*/temp`, this is `sensors`.
2. Locates the corresponding directory: `${ZENOH_BACKEND_FS_ROOT}/<dir>/sensors`.
3. Walks the directory tree recursively using [`walkdir`](https://crates.io/crates/walkdir).
4. For each file found, converts its path back to a zenoh key expression and tests `intersects()` against the query's key expression.
5. Reads matching files and looks up their encoding/timestamp from RocksDB.

### Performance Implications

| Scenario                        | Performance                                    |
|---------------------------------|------------------------------------------------|
| Shallow wildcard (`sensors/*`)  | Fast — scans only immediate children of one dir |
| Deep wildcard (`**`)            | Walks the entire storage tree; O(n files)      |
| Many files in one directory     | Linear scan; no indexing beyond the prefix opt |
| Deep nesting (many levels)      | More directories to traverse; use specific prefixes when possible |

For large datasets, prefer narrowing key expressions to avoid full-tree scans. The backend has no secondary index beyond the filesystem directory structure.

### The `.zenoh_datainfo` Directory Is Excluded

During wildcard scans, the iterator checks if the current directory entry is named `.zenoh_datainfo`. If so, it calls `skip_current_dir()` — the entire RocksDB directory is skipped and never included in query results.

### Symlinks During Scans

If `follow_links: false` (default) and the scan encounters a path that is or traverses a symlink, the plugin:

- Logs a debug message: `"Don't search for files in ... as it's within a symbolic link"`
- Returns an empty iterator for that subtree (falls back to a `WalkDir::new("")` iterator that yields nothing).

If `follow_links: true`, symlinked directories are traversed normally and their contents are included in results.

---

## Deletion Behavior

When a DELETE is received for a key:

1. The corresponding file is removed from disk.
2. Empty parent directories are pruned upward (up to but not including the storage `base_dir`).
3. The RocksDB metadata entry for this key is deleted via `del_data_info()` — no tombstone is retained. The GC constants in the source (`GC_PERIOD`, `MIN_DELAY_BEFORE_REMOVAL`) are defined but currently unused; no background task exists to remove tombstones.

In `read_only` mode, DELETE is rejected with a warning and an error is returned to the caller.

---

## Symlink Handling

The plugin checks for symlinks using `symlink_metadata()` — not `metadata()` — so the symlink itself is detected, not its target.

The check traverses all path ancestors from the file up to (but not including) the `base_dir`. If **any** ancestor segment is a symlink, the file is considered "inside a symbolic link."

```
base_dir = /data/sensors
file     = /data/sensors/lab/link-to-outside/temp
                           ^^^^^^^^^^^^^^^^^ symlink here
```

In this case, with `follow_links: false`, **reads** (GET and wildcard scans) of paths containing `link-to-outside` are silently skipped. Writes (PUT) are not checked for symlinks — they always proceed regardless of `follow_links`.

With `follow_links: true`, `WalkDir` is configured with `.follow_links(true)`, and the symlink check in `contains_symlink()` is bypassed for read operations.

---

## Complete Config Examples

### 1. Basic Filesystem Storage

```json5
// zenoh.json5
{
  plugins: {
    storage_manager: {
      volumes: {
        fs: {}   // loads zenoh_backend_fs; no extra volume config needed
      },
      storages: {
        sensor_data: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",  // store relative keys under dir
          volume: {
            id: "fs",
            dir: "sensor_data"     // $ZENOH_BACKEND_FS_ROOT/sensor_data/
          }
        }
      }
    },
    rest: { http_port: 8000 }
  }
}
```

Run with:
```bash
export ZENOH_BACKEND_FS_ROOT=/var/zenoh-data
zenohd -c zenoh.json5
```

Files land in `/var/zenoh-data/sensor_data/<relative-key>`.

### 2. Read-Only Storage (Serving Static Files)

Pre-populate the directory with files, then serve them via zenoh GET queries. Incoming PUTs and DELETEs are rejected.

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        fs: {}
      },
      storages: {
        static_config: {
          key_expr: "config/**",
          strip_prefix: "config",
          volume: {
            id: "fs",
            dir: "static-config",     // pre-populated directory
            read_only: true,
            keep_mime_types: true     // serve .json as application/json, etc.
          }
        }
      }
    }
  }
}
```

Usage: Place files manually in `$ZENOH_BACKEND_FS_ROOT/static-config/`. A GET for `config/device.json` returns the file contents with encoding `application/json` (guessed from `.json` extension).

### 3. Ephemeral Storage — Delete on Shutdown

Useful for caching or temporary coordination data that should not persist across router restarts.

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        fs: {}
      },
      storages: {
        temp_cache: {
          key_expr: "cache/**",
          strip_prefix: "cache",
          volume: {
            id: "fs",
            dir: "temp-cache",
            on_closure: "delete_all"   // wipe on storage removal / router shutdown
          }
        }
      }
    }
  }
}
```

### 4. Storage with Symlink Support

For serving content from a directory structure that uses symbolic links (e.g. a content library organized with symlinks).

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        fs: {}
      },
      storages: {
        media_library: {
          key_expr: "media/**",
          strip_prefix: "media",
          volume: {
            id: "fs",
            dir: "media-root",
            read_only: true,
            follow_links: true,       // traverse symlinked directories
            keep_mime_types: true
          }
        }
      }
    }
  }
}
```

---

## Runtime Admin via REST API

The storage manager admin space allows creating and removing storages at runtime without a config file restart.

### Start the Router with Admin Access

```bash
zenohd --adminspace-permissions=rw --rest-http-port=8000
```

### Add the `fs` Volume

```bash
curl -X PUT \
  -H 'content-type:application/json' \
  -d '{}' \
  'http://localhost:8000/@/local/router/config/plugins/storage_manager/volumes/fs'
```

### Add a Storage

```bash
curl -X PUT \
  -H 'content-type:application/json' \
  -d '{
    "key_expr": "sensors/**",
    "strip_prefix": "sensors",
    "volume": {
      "id": "fs",
      "dir": "sensor_data"
    }
  }' \
  'http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/sensor_data'
```

### Remove a Storage

```bash
curl -X DELETE \
  'http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/sensor_data'
```

If `on_closure: "delete_all"` was configured, the storage directory is deleted when this DELETE is processed.

---

## Code Examples

### Rust — Put and Get via Filesystem Storage

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    // Load config from file (which declares the fs volume + storage)
    let config = Config::from_file("zenoh.json5").unwrap();
    let session = zenoh::open(config).await.unwrap();

    // PUT a value — stored as a file on disk
    session
        .put("sensors/room-1/temperature", 23.5_f64)
        .encoding(zenoh::bytes::Encoding::APPLICATION_JSON)
        .await
        .unwrap();

    // GET it back
    let replies = session
        .get("sensors/room-1/temperature")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            let value: f64 = sample.payload().deserialize().unwrap();
            println!("Got: {} (encoding: {})", value, sample.encoding());
        }
    }

    session.close().await.unwrap();
}
```

### Rust — Wildcard GET (Directory Walk)

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let config = Config::from_file("zenoh.json5").unwrap();
    let session = zenoh::open(config).await.unwrap();

    // GET all keys under sensors/ — triggers a filesystem directory walk
    let replies = session.get("sensors/**").await.unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            println!(
                "key={} encoding={}",
                sample.key_expr(),
                sample.encoding()
            );
        }
    }

    session.close().await.unwrap();
}
```

### Python — Put, Get, and Subscribe

```python
import zenoh
import time

conf = zenoh.Config.from_file("zenoh.json5")
with zenoh.open(conf) as session:
    # PUT — value written to disk as raw bytes
    session.put("sensors/room-1/humidity", b"65.2")

    # GET — reads file; encoding retrieved from .zenoh_datainfo RocksDB
    replies = session.get("sensors/room-1/humidity")
    for reply in replies:
        if reply.ok:
            print(f"Got: {bytes(reply.ok.payload)} encoding={reply.ok.encoding}")

    # Wildcard GET — walks the storage directory
    all_replies = session.get("sensors/**")
    for reply in all_replies:
        if reply.ok:
            print(f"  {reply.ok.key_expr}: {bytes(reply.ok.payload)[:64]}")

    # Subscribe to live updates
    def on_sample(sample):
        print(f"Update: {sample.key_expr} = {bytes(sample.payload)}")

    sub = session.declare_subscriber("sensors/**", on_sample)
    time.sleep(5)
    sub.undeclare()
```

### Python — Check What's on Disk After PUT

```python
import zenoh, os

conf = zenoh.Config.from_file("zenoh.json5")
root = os.environ.get("ZENOH_BACKEND_FS_ROOT", os.path.expanduser("~/.zenoh/zenoh_backend_fs"))

with zenoh.open(conf) as session:
    session.put("sensors/lab/co2", b"412")
    session.put("sensors/lab/temp", b"21.3")

# Inspect files directly — no zenoh needed
storage_dir = os.path.join(root, "sensor_data")  # matches dir: "sensor_data"
for dirpath, dirs, files in os.walk(storage_dir):
    # Skip the RocksDB metadata dir
    dirs[:] = [d for d in dirs if d != ".zenoh_datainfo"]
    for fname in files:
        fpath = os.path.join(dirpath, fname)
        rel = os.path.relpath(fpath, storage_dir)
        with open(fpath, "rb") as f:
            content = f.read()
        print(f"{rel}: {content}")
# Output:
#   lab/co2: b'412'
#   lab/temp: b'21.3'
```

### curl — Test via REST API

```bash
# PUT values
curl -X PUT -d "23.5"          http://localhost:8000/sensors/room-1/temperature
curl -X PUT -d '{"val": 65.2}' -H 'content-type: application/json' \
                               http://localhost:8000/sensors/room-1/humidity

# GET a single key
curl http://localhost:8000/sensors/room-1/temperature

# Wildcard GET — returns all files under sensors/
curl http://localhost:8000/sensors/**

# DELETE a key (removes the file)
curl -X DELETE http://localhost:8000/sensors/room-1/temperature
```

---

## Troubleshooting

### Storage Fails to Start: "the path must be relative"

The `dir` value is an absolute path. It must be relative to `ZENOH_BACKEND_FS_ROOT`.

```json5
// Wrong
dir: "/var/data/sensors"

// Right
dir: "sensors"   // resolves to $ZENOH_BACKEND_FS_ROOT/sensors
```

### Files Are Written but GET Returns Nothing

Check if `follow_links` is needed. If the target directory is (or is reached through) a symlink and `follow_links: false`, reads return empty silently.

```bash
ls -la $ZENOH_BACKEND_FS_ROOT/my-dir/
# If any component is a symlink, enable follow_links: true
```

### Encoding Reported as `application/octet-stream` for Known File Types

Set `keep_mime_types: true` (it's the default) and ensure the file has a recognizable extension. The `mime_guess` crate maps extensions like `.json`, `.txt`, `.png`, `.mp4` to their mime types. Files with no extension or unrecognized extensions get `application/octet-stream`.

### Conflict Files with `.##z` Extension Appearing on Disk

This is normal. A key was published at both a path and a sub-path of that path (e.g. both `a/b` and `a/b/c`), creating a file/directory name conflict. The `.##z` file holds the value of the shallower key. The plugin handles this transparently; zenoh callers never see the suffix.

### RocksDB Errors on Startup

The `.zenoh_datainfo` directory may be locked by another process or corrupted. Stop all processes using the storage directory and restart. If the directory is corrupted, deleting `.zenoh_datainfo/` will lose encoding/timestamp metadata for existing files but allow the storage to start; files will be served with guessed encoding.

## See Also

- [Plugin Storage Manager Guide](plugin-storage-manager-guide.md) — the storage manager plugin that loads and manages filesystem backend storages
- [Storage Backends Guide](storage-backends-guide.md) — comparison of all backend types and when to choose filesystem vs RocksDB vs S3
