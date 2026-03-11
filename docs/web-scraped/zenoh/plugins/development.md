# Zenoh Plugin Development Guide

## Table of Contents

1. [Plugin Architecture Overview](#plugin-architecture-overview)
2. [Writing a Generic Plugin](#writing-a-generic-plugin)
3. [Writing a Storage Backend](#writing-a-storage-backend)
4. [Plugin Configuration Schema](#plugin-configuration-schema)

---

## Plugin Architecture Overview

Zenoh's plugin system allows extending `zenohd` with dynamic behavior through shared libraries loaded at startup. The system is built around a trait-based vtable architecture with ABI compatibility checking.

### Two Plugin Types

**Generic plugins** (`ZenohPlugin`) receive the full zenoh `DynamicRuntime` as their start argument and return a `RunningPlugin` instance. They interact directly with the zenoh session and can subscribe, publish, declare queryables, or do anything the zenoh API supports.

**Storage backends** (`Volume` + `Storage` traits) are loaded by the `zenoh-plugin-storage-manager` plugin. They implement a key-value storage interface and are driven by the storage manager rather than directly by `zenohd`.

### Plugin Lifecycle

Plugins move through three states managed by `PluginsManager`:

```
Declared ──load()──> Loaded ──start()──> Started
                                           │
                                        stop() (drop instance)
```

- **Declared**: The plugin source (path or name) is registered but the library has not been opened.
- **Loaded**: The shared library is open and its vtable has been verified for ABI compatibility.
- **Started**: The plugin's `start()` function has been called and its instance is running.

### ABI Compatibility

When a dynamic plugin is loaded, `zenohd` calls three exported C functions before doing anything else:

1. `get_plugin_loader_version()` — Returns a `u64` constant. Currently `2`. If this differs from the host's `PLUGIN_LOADER_VERSION`, loading fails immediately.
2. `get_compatibility()` — Returns a `Compatibility` struct containing the Rust compiler version, zenoh crate version, and enabled feature flags. The host checks all three before proceeding.
3. `load_plugin()` — Returns a `PluginVTable` containing the `start` function pointer.

This means **your plugin must be compiled with the exact same version of Rust, the same version of zenoh, and the same zenoh feature flags as the `zenohd` you are loading it into.** Build mismatches produce clear error messages rather than undefined behavior.

The `declare_plugin!` macro generates all three exported functions automatically.

---

## Writing a Generic Plugin

### The Plugin Trait

A generic plugin for `zenohd` implements two traits:

```rust
pub trait Plugin: Sized + 'static {
    type StartArgs: PluginStartArgs;  // DynamicRuntime for zenohd plugins
    type Instance: PluginInstance;    // RunningPlugin for zenohd plugins

    const DEFAULT_NAME: &'static str;
    const PLUGIN_VERSION: &'static str;
    const PLUGIN_LONG_VERSION: &'static str;

    fn start(name: &str, args: &Self::StartArgs) -> ZResult<Self::Instance>;
}
```

`ZenohPlugin` is a marker trait combining `Plugin<StartArgs = DynamicRuntime, Instance = RunningPlugin>` with no additional methods. Implementing it confirms your type satisfies `zenohd`'s expected interface.

`RunningPlugin` is a `Box<dyn RunningPluginTrait>`, so your plugin instance is a heap-allocated trait object. The `RunningPluginTrait` provides hooks for:

- `config_checker()` — Called when the plugin's configuration section changes at runtime.
- `adminspace_getter()` — Called when a GET query hits the admin space at your plugin's path.

### Cargo.toml Setup

```toml
[package]
name = "zenoh-plugin-example"
version = "1.0.0"
edition = "2021"

[lib]
# zenohd looks for libzenoh_plugin_example.so / .dylib / .dll
name = "zenoh_plugin_example"
crate-type = ["cdylib"]         # required for dynamic loading
# Use ["cdylib", "rlib"] if you also want to link statically

[features]
default = ["dynamic_plugin"]
dynamic_plugin = []             # gates the declare_plugin! call

[dependencies]
zenoh = { version = "1.0", features = ["default", "internal", "plugins", "unstable"] }
zenoh-plugin-trait = { version = "1.0" }
zenoh-util = { version = "1.0" }
tokio = { version = "1", features = ["full"] }
futures = "0.3"
tracing = "0.1"
lazy_static = "1"
git-version = "0.3"
serde_json = "1"
```

> **Note**: The `internal` and `plugins` features of `zenoh` expose `DynamicRuntime`, `RunningPlugin`, `RunningPluginTrait`, and `ZenohPlugin`. These are required for `zenohd`-targeting plugins.

### Loading a Plugin

In your `zenohd` configuration file (`config.json5` or `config.json`):

```json5
{
  "plugins_loading": {
    // Directories zenohd will search for plugins by name
    "search_dirs": ["/usr/lib/zenoh", "~/.local/lib/zenoh", "./target/debug"]
  },
  "plugins": {
    // Plugin loaded by searching search_dirs for libzenoh_plugin_example.so
    "example": {
      "storage-selector": "demo/example/**"
    },

    // Plugin loaded from explicit paths (first found wins)
    "my_plugin": {
      "__path__": [
        "/absolute/path/to/libmy_plugin.so",
        "/fallback/path/to/libmy_plugin.so"
      ],
      "my_option": "value"
    }
  }
}
```

The plugin name key under `"plugins"` is passed as the `name` argument to `Plugin::start()`. Your plugin reads its configuration using:

```rust
let config = runtime.get_config().get_plugin_config(name).unwrap();
```

### Plugin State Management

Your plugin instance (`RunningPlugin = Box<dyn RunningPluginTrait>`) must be `Send + Sync`. Since plugins typically own async tasks, you need an `Arc<Mutex<...>>` wrapper around mutable state and a mechanism to signal the background task to stop.

A common pattern using an `AtomicBool` flag:

```rust
use std::sync::{Arc, Mutex};
use std::sync::atomic::{AtomicBool, Ordering};

struct MyPluginInner {
    flag: Arc<AtomicBool>,
    name: String,
    runtime: DynamicRuntime,
}

#[derive(Clone)]
struct MyPluginInstance(Arc<Mutex<MyPluginInner>>);
```

### Tokio Runtime Handling

Dynamic plugins run inside `zenohd`'s process but may not share its Tokio runtime context. The example pattern creates a plugin-local runtime and tries the current one first:

```rust
use tokio::runtime::Handle;
use std::future::Future;

lazy_static::lazy_static! {
    static ref TOKIO_RUNTIME: tokio::runtime::Runtime =
        tokio::runtime::Builder::new_multi_thread()
            .worker_threads(2)
            .max_blocking_threads(50)
            .enable_all()
            .build()
            .expect("Unable to create runtime");
}

fn spawn_runtime(task: impl Future<Output = ()> + Send + 'static) {
    match Handle::try_current() {
        Ok(rt) => { rt.spawn(task); }
        Err(_) => { TOKIO_RUNTIME.spawn(task); }
    }
}
```

### Example: Minimal Plugin

This plugin subscribes to a configurable key expression and stores received samples in a `HashMap`, then replies to queries with the stored data.

**Project structure:**
```
zenoh-plugin-example/
├── Cargo.toml
└── src/
    └── lib.rs
```

**`Cargo.toml`:**

```toml
[package]
name = "zenoh-plugin-example"
version = "1.0.0"
edition = "2021"

[lib]
name = "zenoh_plugin_example"
crate-type = ["cdylib"]

[features]
default = ["dynamic_plugin"]
dynamic_plugin = []

[dependencies]
zenoh = { version = "1.0", features = ["default", "internal", "plugins", "unstable"] }
zenoh-plugin-trait = { version = "1.0" }
zenoh-util = { version = "1.0" }
tokio = { version = "1", features = ["full"] }
futures = "0.3"
tracing = "0.1"
lazy_static = "1"
git-version = "0.3"
serde_json = "1"

[package.metadata.cargo-machete]
ignored = ["git-version"]  # used by plugin_long_version! macro
```

**`src/lib.rs`:**

```rust
#![recursion_limit = "256"]

use std::{
    collections::HashMap,
    convert::TryFrom,
    future::Future,
    sync::{
        atomic::{AtomicBool, Ordering::Relaxed},
        Arc, Mutex,
    },
};

use futures::select;
use tracing::{debug, info};
use zenoh::{
    internal::{
        bail,
        plugins::{RunningPluginTrait, ZenohPlugin},
        runtime::DynamicRuntime,
        zlock,
    },
    key_expr::{keyexpr, KeyExpr},
    sample::Sample,
    Result as ZResult,
};
use zenoh_plugin_trait::{plugin_long_version, plugin_version, Plugin, PluginControl};
use zenoh_util::ffi::JsonKeyValueMap;

// ── Tokio runtime for dynamic plugin context ────────────────────────────────

const WORKER_THREAD_NUM: usize = 2;
const MAX_BLOCK_THREAD_NUM: usize = 50;

lazy_static::lazy_static! {
    static ref TOKIO_RUNTIME: tokio::runtime::Runtime =
        tokio::runtime::Builder::new_multi_thread()
            .worker_threads(WORKER_THREAD_NUM)
            .max_blocking_threads(MAX_BLOCK_THREAD_NUM)
            .enable_all()
            .build()
            .expect("Unable to create runtime");
}

fn spawn_runtime(task: impl Future<Output = ()> + Send + 'static) {
    match tokio::runtime::Handle::try_current() {
        Ok(rt) => { rt.spawn(task); }
        Err(_)  => { TOKIO_RUNTIME.spawn(task); }
    }
}

// ── Configuration default ────────────────────────────────────────────────────

const DEFAULT_SELECTOR: &str = "demo/example/**";

// ── Plugin struct and declaration ────────────────────────────────────────────

pub struct ExamplePlugin;

// Generates get_plugin_loader_version, get_compatibility, load_plugin exports.
// Conditional on the feature so the same crate can be linked statically too.
#[cfg(feature = "dynamic_plugin")]
zenoh_plugin_trait::declare_plugin!(ExamplePlugin);

impl ZenohPlugin for ExamplePlugin {}

impl Plugin for ExamplePlugin {
    type StartArgs = DynamicRuntime;
    type Instance = zenoh::internal::plugins::RunningPlugin;

    const DEFAULT_NAME: &'static str = "example";
    const PLUGIN_VERSION: &'static str = plugin_version!();
    const PLUGIN_LONG_VERSION: &'static str = plugin_long_version!();

    fn start(name: &str, runtime: &Self::StartArgs) -> ZResult<Self::Instance> {
        // Read the plugin's own config section from the zenoh config
        let config = runtime
            .get_config()
            .get_plugin_config(name)
            .unwrap();
        let map_cfg = config.as_object().unwrap();

        // Parse the "storage-selector" key from plugin config
        let selector: KeyExpr = match map_cfg.get("storage-selector") {
            Some(serde_json::Value::String(s)) => KeyExpr::try_from(s.as_str())?,
            None => KeyExpr::try_from(DEFAULT_SELECTOR).unwrap(),
            _ => bail!("storage-selector must be a string for plugin '{}'", name),
        }
        .into_owned();

        // Spawn the background task and retain a stop flag
        let flag = Arc::new(AtomicBool::new(true));
        spawn_runtime(run(runtime.clone(), selector, flag.clone()));

        // Return a RunningPlugin (Box<dyn RunningPluginTrait>)
        Ok(Box::new(RunningPlugin(Arc::new(Mutex::new(
            RunningPluginInner {
                flag,
                name: name.into(),
                runtime: runtime.clone(),
            },
        )))))
    }
}

// ── Running plugin state ──────────────────────────────────────────────────────

struct RunningPluginInner {
    flag: Arc<AtomicBool>,
    name: String,
    runtime: DynamicRuntime,
}

#[derive(Clone)]
struct RunningPlugin(Arc<Mutex<RunningPluginInner>>);

// PluginControl provides the report() and plugins_status() hooks.
// Default impls return empty/ok, which is fine for a simple plugin.
impl PluginControl for RunningPlugin {}

impl RunningPluginTrait for RunningPlugin {
    /// Called by zenohd when the plugin's config section changes at runtime.
    fn config_checker(
        &self,
        path: &str,
        old: &JsonKeyValueMap,
        new: &JsonKeyValueMap,
    ) -> ZResult<Option<JsonKeyValueMap>> {
        let old: serde_json::Map<String, serde_json::Value> = old.into();
        let new: serde_json::Map<String, serde_json::Value> = new.into();
        let mut guard = zlock!(&self.0);

        const SELECTOR_KEY: &str = "storage-selector";

        if path == SELECTOR_KEY || path.is_empty() {
            match (old.get(SELECTOR_KEY), new.get(SELECTOR_KEY)) {
                // Selector unchanged — nothing to do
                (Some(serde_json::Value::String(o)), Some(serde_json::Value::String(n)))
                    if o == n => {}

                // Selector changed — stop old task, start new one
                (_, Some(serde_json::Value::String(selector))) => {
                    guard.flag.store(false, Relaxed);
                    guard.flag = Arc::new(AtomicBool::new(true));
                    match KeyExpr::try_from(selector.as_str()) {
                        Err(e) => tracing::error!("{}", e),
                        Ok(sel) => {
                            spawn_runtime(run(
                                guard.runtime.clone(),
                                sel,
                                guard.flag.clone(),
                            ));
                        }
                    }
                    return Ok(None);
                }

                // Selector removed — just stop
                (_, None) => {
                    guard.flag.store(false, Relaxed);
                }

                _ => bail!("storage-selector for '{}' must be a string", guard.name),
            }
        }

        bail!("unknown config option '{}' for plugin '{}'", path, guard.name)
    }
}

impl Drop for RunningPlugin {
    fn drop(&mut self) {
        // Signal the background task to exit when the plugin is stopped
        zlock!(self.0).flag.store(false, Relaxed);
    }
}

// ── Background async task ─────────────────────────────────────────────────────

async fn run(runtime: DynamicRuntime, selector: KeyExpr<'_>, flag: Arc<AtomicBool>) {
    zenoh_util::init_log_from_env_or("error");

    // Reuse zenohd's runtime — no new network connection is created
    let session = zenoh::session::init(runtime).await.unwrap();
    let mut stored: HashMap<String, Sample> = HashMap::new();

    debug!("ExamplePlugin running with selector={}", selector);

    let sub = session.declare_subscriber(&selector).await.unwrap();
    let queryable = session.declare_queryable(&selector).await.unwrap();

    while flag.load(Relaxed) {
        select! {
            sample = sub.recv_async() => {
                let sample = sample.unwrap();
                let payload = sample
                    .payload()
                    .try_to_string()
                    .unwrap_or_else(|e| e.to_string().into());
                info!("Stored ('{}': '{}')", sample.key_expr(), payload);
                stored.insert(sample.key_expr().to_string(), sample);
            },
            query = queryable.recv_async() => {
                let query = query.unwrap();
                info!("Query on '{}'", query.selector());
                for (ke, sample) in &stored {
                    if query.key_expr().intersects(unsafe {
                        keyexpr::from_str_unchecked(ke)
                    }) {
                        query.reply_sample(sample.clone()).await.unwrap();
                    }
                }
            }
        }
    }
}
```

**Zenoh configuration to load this plugin:**

```json5
// config.json5
{
  "mode": "router",
  "timestamping": { "enabled": { "router": true } },
  "plugins_loading": {
    "search_dirs": ["./target/debug"]
  },
  "plugins": {
    "example": {
      "storage-selector": "demo/example/**"
    }
  }
}
```

**Build and run:**

```bash
cargo build
zenohd --config config.json5
```

---

## Writing a Storage Backend

### Architecture

Storage backends are plugins loaded by the `zenoh-plugin-storage-manager` plugin, not directly by `zenohd`. The storage manager introduces two concepts:

- **Volume**: A backend instance corresponding to a specific storage technology (memory, RocksDB, S3, etc.). Created once via `Plugin::start()`.
- **Storage**: A mapping from a key expression glob to a volume. Multiple storages can share one volume. Created by calling `Volume::create_storage()`.

```
zenohd
  └── zenoh-plugin-storage-manager  (Plugin<StartArgs=DynamicRuntime>)
        ├── Volume "memory"          (Plugin<StartArgs=VolumeConfig>)
        │     ├── Storage "demo/mem1/**"
        │     └── Storage "demo/mem2/**"
        └── Volume "rocksdb"         (Plugin<StartArgs=VolumeConfig>)
              └── Storage "demo/db/**"
```

### The Volume Trait

```rust
#[async_trait]
pub trait Volume: Send + Sync {
    /// Status JSON returned by admin space GET on this volume
    fn get_admin_status(&self) -> JsonValue;

    /// Declares what this backend guarantees
    fn get_capability(&self) -> Capability;

    /// Called by storage manager to create a storage instance
    async fn create_storage(&self, props: StorageConfig) -> ZResult<Box<dyn Storage>>;
}
```

`Capability` tells the storage manager what guarantees the backend provides:

```rust
pub struct Capability {
    pub persistence: Persistence,  // Volatile | Durable
    pub history: History,           // Latest | All
}
```

### The Storage Trait

```rust
#[async_trait]
pub trait Storage: Send + Sync {
    fn get_admin_status(&self) -> JsonValue;

    // Called for each incoming publication matching the storage's key expression.
    // key is None when the publication's key exactly equals the strip_prefix.
    async fn put(
        &mut self,
        key: Option<OwnedKeyExpr>,
        payload: ZBytes,
        encoding: Encoding,
        timestamp: Timestamp,
    ) -> ZResult<StorageInsertionResult>;

    // Called for each incoming deletion
    async fn delete(
        &mut self,
        key: Option<OwnedKeyExpr>,
        timestamp: Timestamp,
    ) -> ZResult<StorageInsertionResult>;

    // Called for each GET query matching the storage's key expression.
    // key is None means the caller wants the entry stored under the strip_prefix.
    async fn get(
        &mut self,
        key: Option<OwnedKeyExpr>,
        parameters: &str,   // query parameters, e.g. from selector "?arg=val"
    ) -> ZResult<Vec<StoredData>>;

    // Called by the replication subsystem to enumerate all stored keys+timestamps
    async fn get_all_entries(&self) -> ZResult<Vec<(Option<OwnedKeyExpr>, Timestamp)>>;
}
```

`StorageInsertionResult` communicates back to the storage manager:

```rust
pub enum StorageInsertionResult {
    Outdated,   // A newer timestamp was already stored; the write was ignored
    Inserted,   // New key-value pair created
    Replaced,   // Existing key-value pair updated
    Deleted,    // Entry removed
}
```

### The `strip_prefix` Behavior

The `StorageConfig` can set a `strip_prefix` that is stripped from incoming key expressions before passing them to the storage. If a publication's key exactly matches the `strip_prefix`, the key passed to `put()`/`delete()`/`get()` is `None`. Your storage must handle `None` keys — map them to a distinguished entry (e.g., use `Option<OwnedKeyExpr>` as the HashMap key directly).

### Example: In-Memory Backend

This is the actual implementation used by `zenoh-plugin-storage-manager` as its built-in "memory" volume.

**`Cargo.toml`:**

```toml
[package]
name = "zenoh-backend-memory"
version = "1.0.0"
edition = "2021"

[lib]
name = "zenoh_backend_memory"
crate-type = ["cdylib", "rlib"]

[features]
default = ["dynamic_plugin"]
dynamic_plugin = []

[dependencies]
zenoh = { version = "1.0", features = ["default", "internal", "unstable"] }
zenoh-plugin-trait = { version = "1.0" }
zenoh-backend-traits = { version = "1.0" }
zenoh-result = { version = "1.0" }
zenoh-util = { version = "1.0" }
async-trait = "0.1"
tokio = { version = "1", features = ["sync"] }
tracing = "0.1"
git-version = "0.3"
```

**`src/lib.rs`:**

```rust
use std::collections::HashMap;
use std::sync::Arc;

use async_trait::async_trait;
use tokio::sync::RwLock;
use zenoh::{
    bytes::{Encoding, ZBytes},
    key_expr::OwnedKeyExpr,
    time::Timestamp,
    Result as ZResult,
};
use zenoh_backend_traits::{
    config::{StorageConfig, VolumeConfig},
    Capability, History, Persistence, Storage, StorageInsertionResult, StoredData,
    Volume, VolumeInstance,
};
use zenoh_plugin_trait::{plugin_long_version, plugin_version, Plugin, PluginControl};
use zenoh_util::ffi::JsonValue;

// ── Backend (Volume) ──────────────────────────────────────────────────────────

pub struct MemoryBackend {
    config: VolumeConfig,
}

// Export C symbols so the storage manager can load this as a dynamic plugin
#[cfg(feature = "dynamic_plugin")]
zenoh_plugin_trait::declare_plugin!(MemoryBackend);

impl Plugin for MemoryBackend {
    // StartArgs for a Volume plugin is VolumeConfig, not DynamicRuntime
    type StartArgs = VolumeConfig;
    type Instance = VolumeInstance; // Box<dyn Volume>

    const DEFAULT_NAME: &'static str = "memory";
    const PLUGIN_VERSION: &'static str = plugin_version!();
    const PLUGIN_LONG_VERSION: &'static str = plugin_long_version!();

    fn start(_name: &str, args: &VolumeConfig) -> ZResult<VolumeInstance> {
        Ok(Box::new(MemoryBackend {
            config: args.clone(),
        }))
    }
}

#[async_trait]
impl Volume for MemoryBackend {
    fn get_admin_status(&self) -> JsonValue {
        self.config.to_json_value().into()
    }

    fn get_capability(&self) -> Capability {
        Capability {
            persistence: Persistence::Volatile, // data lost on restart
            history: History::Latest,            // only most recent value per key
        }
    }

    async fn create_storage(&self, config: StorageConfig) -> ZResult<Box<dyn Storage>> {
        tracing::debug!("Creating MemoryStorage with config: {:?}", config);
        Ok(Box::new(MemoryStorage::new(config).await?))
    }
}

// ── Storage ───────────────────────────────────────────────────────────────────

struct MemoryStorage {
    config: StorageConfig,
    // Option<OwnedKeyExpr> as key handles the strip_prefix==key case (None key)
    map: Arc<RwLock<HashMap<Option<OwnedKeyExpr>, StoredData>>>,
}

impl MemoryStorage {
    async fn new(config: StorageConfig) -> ZResult<Self> {
        Ok(Self {
            config,
            map: Arc::new(RwLock::new(HashMap::new())),
        })
    }
}

#[async_trait]
impl Storage for MemoryStorage {
    fn get_admin_status(&self) -> JsonValue {
        self.config.to_json_value().into()
    }

    async fn put(
        &mut self,
        key: Option<OwnedKeyExpr>,
        payload: ZBytes,
        encoding: Encoding,
        timestamp: Timestamp,
    ) -> ZResult<StorageInsertionResult> {
        tracing::trace!("put key={:?}", key);
        let mut map = self.map.write().await;
        let result = match map.entry(key) {
            std::collections::hash_map::Entry::Occupied(mut e) => {
                // Only update if the new timestamp is newer
                if timestamp > e.get().timestamp {
                    e.insert(StoredData { payload, encoding, timestamp });
                    StorageInsertionResult::Replaced
                } else {
                    StorageInsertionResult::Outdated
                }
            }
            std::collections::hash_map::Entry::Vacant(e) => {
                e.insert(StoredData { payload, encoding, timestamp });
                StorageInsertionResult::Inserted
            }
        };
        Ok(result)
    }

    async fn delete(
        &mut self,
        key: Option<OwnedKeyExpr>,
        _timestamp: Timestamp,
    ) -> ZResult<StorageInsertionResult> {
        tracing::trace!("delete key={:?}", key);
        self.map.write().await.remove(&key);
        Ok(StorageInsertionResult::Deleted)
    }

    async fn get(
        &mut self,
        key: Option<OwnedKeyExpr>,
        _parameters: &str,
    ) -> ZResult<Vec<StoredData>> {
        tracing::trace!("get key={:?}", key);
        // _parameters could be used for filtering; ignored in this simple implementation
        match self.map.read().await.get(&key) {
            Some(data) => Ok(vec![data.clone()]),
            None => Ok(vec![]),   // empty result, not an error
        }
    }

    async fn get_all_entries(&self) -> ZResult<Vec<(Option<OwnedKeyExpr>, Timestamp)>> {
        let map = self.map.read().await;
        Ok(map.iter().map(|(k, v)| (k.clone(), v.timestamp)).collect())
    }
}
```

### How the Storage Manager Loads Backends

The storage manager maintains its own `PluginsManager<VolumeConfig, VolumeInstance>`. When it encounters a volume config entry:

1. It looks for an existing loaded plugin with that volume ID.
2. If `__path__` is specified, it calls `declare_dynamic_plugin_by_paths()`.
3. Otherwise it calls `declare_dynamic_plugin_by_name()`, which prepends `"zenoh_backend_"` to form the library name (so `"rocksdb"` becomes `libzenoh_backend_rocksdb.so`).
4. It calls `load()` → `start(volume_config)` → `instance().create_storage(storage_config)` for each storage assigned to that volume.

The built-in `"memory"` volume is registered as a static plugin (no `.so` file needed):

```rust
plugins_manager.declare_static_plugin::<MemoryBackend, &str>(MEMORY_BACKEND_NAME, true);
```

### Storage Manager Configuration

```json5
// Inside the zenohd config.json5:
{
  "plugins": {
    "storage_manager": {
      // Optional: extra directories to search for backend .so files
      "backend_search_dirs": ["/usr/lib/zenoh/backends", "./target/debug"],

      "volumes": {
        // "memory" is built-in — no path needed
        // Additional backends reference their .so files:
        "rocksdb": {
          // backend name maps to libzenoh_backend_rocksdb.so
          // OR specify explicit paths:
          "__path__": [
            "./target/debug/libzenoh_backend_rocksdb.so",
            "./target/debug/libzenoh_backend_rocksdb.dylib"
          ],
          // Any extra keys here are passed to Volume::start() via VolumeConfig.rest
          "db_path": "/var/db/zenoh"
        },
        "s3": {
          "endpoint": "http://minio:9000",
          "bucket": "zenoh-data"
        }
      },

      "storages": {
        // Storage name → config
        "sensors": {
          "key_expr": "home/sensors/**",
          "volume": "memory"        // reference a volume by name
        },
        "history": {
          "key_expr": "home/history/**",
          "strip_prefix": "home",   // stripped before passing key to Storage::put/get/delete
          "complete": true,          // this storage claims to have complete data for the key_expr
          "volume": "rocksdb",

          // Optional garbage collection config
          "garbage_collection": {
            "period": 60,           // seconds between GC runs
            "lifespan": 86400       // seconds before metadata is GC'd
          },

          // Optional replication config (for distributed storage alignment)
          "replication": {
            "interval": 10.0,       // seconds between digest publications
            "sub_intervals": 5,
            "hot": 6,               // intervals in the "hot" era
            "warm": 30,             // intervals in the "warm" era
            "propagation_delay": 250 // ms
          }
        },
        "archive": {
          "key_expr": "home/archive/**",
          // volume can also be an object with extra per-storage config:
          "volume": {
            "id": "s3",
            "prefix": "archive/"   // passed to Storage via StorageConfig.volume_cfg
          }
        }
      }
    }
  }
}
```

### Dynamic Storage Management via Admin Space

With `--adminspace-permissions rw`, you can manage storages at runtime:

```bash
# Add a new storage
curl -X PUT \
  -H 'content-type:application/json' \
  -d '{"key_expr":"demo/live/**","volume":"memory"}' \
  'http://localhost:8080/@/local/router/config/plugins/storage_manager/storages/live'

# Remove a storage
curl -X DELETE \
  'http://localhost:8080/@/local/router/config/plugins/storage_manager/storages/live'

#