# Zenoh Plugin Development Guide

## Table of Contents
1. [Plugin Architecture Overview](#architecture)
2. [Writing a Generic Plugin](#generic-plugin)
3. [Writing a Storage Backend](#storage-backend)
4. [Plugin Configuration Schema](#config-schema)
5. [Loading and Deploying Plugins](#loading)

---

## Plugin Architecture Overview {#architecture}

Zenoh's plugin system allows extending `zenohd` at runtime by loading dynamic shared libraries. Plugins are loaded at startup based on the configuration file and follow a defined lifecycle: **Declared → Loaded → Started**.

### Two Plugin Types

**Generic Plugins** receive the full zenoh `DynamicRuntime` as their start argument. They can access the zenoh session, subscribe to key expressions, declare queryables, and interact with the network freely.

**Storage Backends** (Volumes) receive a `VolumeConfig` as their start argument. They are loaded and managed by the `zenoh-plugin-storage-manager` plugin, which acts as a meta-plugin that coordinates multiple backends and storage instances.

### Plugin Lifecycle States

```
Declared  -->  Loaded  -->  Started
   |              |             |
   |           (library      (Plugin::start()
   |           loaded)        called)
   |
(path or name
 registered)
```

- **Declared**: The plugin path/name is registered in the `PluginsManager`, but the library has not been loaded yet.
- **Loaded**: The shared library has been opened via `dlopen` (or equivalent), version/ABI compatibility has been verified, and the vtable has been extracted.
- **Started**: `Plugin::start()` has been called and a `PluginInstance` is running.

Stopping a plugin simply drops its `Instance`. The plugin should clean up subscriptions, tasks, and other resources in the instance's `Drop` implementation.

### Compatibility Checking

Before a plugin is started, zenohd performs strict compatibility checks between the host and the plugin library:

1. **Loader version** (`PLUGIN_LOADER_VERSION`): The ABI version of the plugin loading protocol.
2. **Rust compiler version**: Major, minor, and patch must match.
3. **Zenoh version**: The semantic version and git commit hash of the `zenoh` crate used to build the plugin must match the host.
4. **Feature flags**: The enabled Cargo features of the `zenoh` crate must match.

This means plugins **must be compiled with the exact same version of `zenoh` as `zenohd`**.

---

## Writing a Generic Plugin {#generic-plugin}

### The Plugin Trait

Every zenoh plugin implements the `Plugin` trait from `zenoh-plugin-trait`:

```rust
pub trait Plugin: Sized + 'static {
    type StartArgs: PluginStartArgs;
    type Instance: PluginInstance;

    const DEFAULT_NAME: &'static str;
    const PLUGIN_VERSION: &'static str;
    const PLUGIN_LONG_VERSION: &'static str;

    fn start(name: &str, args: &Self::StartArgs) -> ZResult<Self::Instance>;
}
```

For plugins targeting `zenohd`:
- `StartArgs` = `DynamicRuntime` (the running zenoh router runtime)
- `Instance` = `RunningPlugin` (a `Box<dyn RunningPluginTrait>`)

Your plugin struct must also implement the marker trait `ZenohPlugin`:

```rust
impl ZenohPlugin for MyPlugin {}
```

### The Instance: RunningPluginTrait

The value returned by `Plugin::start()` must implement `RunningPluginTrait`, which has two important methods:

```rust
pub trait RunningPluginTrait: PluginControl + Send + Sync {
    /// Called when the plugin's config section changes at runtime.
    fn config_checker(
        &self,
        path: &str,
        old: &JsonKeyValueMap,
        new: &JsonKeyValueMap,
    ) -> ZResult<Option<JsonKeyValueMap>>;

    /// Called when the admin space is queried for plugin status.
    fn adminspace_getter<'a>(
        &'a self,
        key_expr: &'a KeyExpr<'a>,
        plugin_status_key: &str,
    ) -> ZResult<Vec<Response>>;
}
```

`config_checker` enables hot-reloading of plugin configuration without restarting `zenohd`. Return `Ok(None)` to accept the change, or `Err(...)` to reject it.

### Cargo.toml Setup

```toml
[package]
name = "zenoh-plugin-myplugin"
version = "1.0.0"
edition = "2021"

[features]
default = ["dynamic_plugin"]
# Guard the declare_plugin! macro behind this feature so the crate
# can also be used as a statically linked plugin.
dynamic_plugin = []

[lib]
# The library name determines the file name zenohd looks for:
#   Linux:   libzenoh_plugin_myplugin.so
#   macOS:   libzenoh_plugin_myplugin.dylib
#   Windows: zenoh_plugin_myplugin.dll
name = "zenoh_plugin_myplugin"
crate-type = ["cdylib"]  # dynamic library output

[dependencies]
zenoh = { version = "1.0", features = ["default", "internal", "plugins", "unstable"] }
zenoh-plugin-trait = { version = "1.0" }
zenoh-util = { version = "1.0" }
tokio = { version = "1", features = ["full"] }
tracing = "0.1"
git-version = "0.3"  # needed by plugin_long_version! macro
lazy_static = "1"    # for global Tokio runtime in dynamic plugin context

[package.metadata.cargo-machete]
ignored = ["git-version"]  # used by macro but not detected by machete
```

> **Important**: The `zenoh` dependency must use the **exact same version** (including git commit) as the `zenohd` binary you are targeting. ABI mismatches will cause `zenohd` to refuse loading the plugin.

### Registering the Plugin Entry Points

The `declare_plugin!` macro generates the three C-ABI functions that `zenohd` looks for when loading the shared library:

- `get_plugin_loader_version()` → protocol version check
- `get_compatibility()` → Rust/zenoh version check  
- `load_plugin()` → returns the vtable with the `start` function pointer

```rust
// Only compile the dynamic entry points when built as a dynamic library
#[cfg(feature = "dynamic_plugin")]
zenoh_plugin_trait::declare_plugin!(MyPlugin);
```

### Managing the Tokio Runtime in Dynamic Plugins

Dynamic plugins loaded into `zenohd` cannot access the router's internal Tokio runtime. They must create their own:

```rust
use lazy_static::lazy_static;

lazy_static! {
    static ref TOKIO_RUNTIME: tokio::runtime::Runtime =
        tokio::runtime::Builder::new_multi_thread()
            .worker_threads(2)
            .max_blocking_threads(50)
            .enable_all()
            .build()
            .expect("Unable to create runtime");
}

fn spawn_runtime(task: impl std::future::Future<Output = ()> + Send + 'static) {
    match tokio::runtime::Handle::try_current() {
        Ok(handle) => { handle.spawn(task); }
        Err(_) => { TOKIO_RUNTIME.spawn(task); }
    }
}
```

### Example: Minimal Subscriber Plugin

This complete example implements a plugin that subscribes to a configurable key expression and stores received samples in a HashMap, then answers queries from that map.

#### `src/lib.rs`

```rust
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

// ─── Runtime management ───────────────────────────────────────────────────────

lazy_static::lazy_static! {
    static ref TOKIO_RUNTIME: tokio::runtime::Runtime =
        tokio::runtime::Builder::new_multi_thread()
            .worker_threads(2)
            .max_blocking_threads(50)
            .enable_all()
            .build()
            .expect("Unable to create tokio runtime");
}

fn spawn_runtime(task: impl Future<Output = ()> + Send + 'static) {
    match tokio::runtime::Handle::try_current() {
        Ok(handle) => { handle.spawn(task); }
        Err(_) => { TOKIO_RUNTIME.spawn(task); }
    }
}

// ─── Plugin struct ────────────────────────────────────────────────────────────

pub struct MyPlugin;

// Register C-ABI entry points for dynamic loading
#[cfg(feature = "dynamic_plugin")]
zenoh_plugin_trait::declare_plugin!(MyPlugin);

// Marker trait required for zenohd plugins
impl ZenohPlugin for MyPlugin {}

impl Plugin for MyPlugin {
    // For zenohd plugins, StartArgs is always DynamicRuntime
    type StartArgs = DynamicRuntime;
    // For zenohd plugins, Instance is always RunningPlugin
    type Instance = zenoh::internal::plugins::RunningPlugin;

    const DEFAULT_NAME: &'static str = "myplugin";
    const PLUGIN_VERSION: &'static str = plugin_version!();
    const PLUGIN_LONG_VERSION: &'static str = plugin_long_version!();

    fn start(name: &str, runtime: &Self::StartArgs) -> ZResult<Self::Instance> {
        // Read this plugin's configuration section
        let config = runtime
            .get_config()
            .get_plugin_config(name)
            .unwrap_or_default();

        // Extract the key expression from config, falling back to a default
        let selector: KeyExpr = match config
            .as_object()
            .and_then(|m| m.get("key_expr"))
            .and_then(|v| v.as_str())
        {
            Some(s) => KeyExpr::try_from(s)?,
            None => KeyExpr::try_from("demo/myplugin/**")?,
        }
        .into_owned();

        // Shared stop flag, dropped when plugin stops
        let flag = Arc::new(AtomicBool::new(true));

        // Spawn the async main loop
        spawn_runtime(run(runtime.clone(), selector, flag.clone()));

        // Return a handle that zenohd holds while the plugin is running
        Ok(Box::new(RunningPlugin(Arc::new(Mutex::new(
            RunningPluginInner { flag, name: name.into(), runtime: runtime.clone() },
        )))))
    }
}

// ─── Running plugin state ─────────────────────────────────────────────────────

struct RunningPluginInner {
    flag: Arc<AtomicBool>,
    name: String,
    runtime: DynamicRuntime,
}

#[derive(Clone)]
struct RunningPlugin(Arc<Mutex<RunningPluginInner>>);

// Required: PluginControl allows reporting sub-plugin status (none here)
impl PluginControl for RunningPlugin {}

impl RunningPluginTrait for RunningPlugin {
    fn config_checker(
        &self,
        path: &str,
        old: &JsonKeyValueMap,
        new: &JsonKeyValueMap,
    ) -> ZResult<Option<JsonKeyValueMap>> {
        let old: serde_json::Map<String, serde_json::Value> = old.into();
        let new: serde_json::Map<String, serde_json::Value> = new.into();
        let mut guard = zlock!(&self.0);

        if path == "key_expr" || path.is_empty() {
            let old_ke = old.get("key_expr").and_then(|v| v.as_str());
            let new_ke = new.get("key_expr").and_then(|v| v.as_str());

            match (old_ke, new_ke) {
                (Some(o), Some(n)) if o == n => {
                    // No change, nothing to do
                }
                (_, Some(new_selector)) => {
                    // Stop the old loop, start a new one
                    guard.flag.store(false, Relaxed);
                    guard.flag = Arc::new(AtomicBool::new(true));
                    let selector = KeyExpr::try_from(new_selector.to_string())?;
                    spawn_runtime(run(
                        guard.runtime.clone(),
                        selector,
                        guard.flag.clone(),
                    ));
                }
                (_, None) => {
                    guard.flag.store(false, Relaxed);
                }
            }
            return Ok(None);
        }
        bail!("Unknown config option '{}' for plugin '{}'", path, guard.name)
    }
}

// Signal the async loop to stop when the plugin is dropped
impl Drop for RunningPlugin {
    fn drop(&mut self) {
        zlock!(self.0).flag.store(false, Relaxed);
    }
}

// ─── Async main loop ──────────────────────────────────────────────────────────

async fn run(runtime: DynamicRuntime, selector: KeyExpr<'_>, flag: Arc<AtomicBool>) {
    // Share the router's session instead of creating a new zenoh connection
    let session = zenoh::session::init(runtime).await.unwrap();
    let mut stored: HashMap<String, Sample> = HashMap::new();

    debug!("myplugin running with selector={}", selector);

    let sub = session.declare_subscriber(&selector).await.unwrap();
    let queryable = session.declare_queryable(&selector).await.unwrap();

    while flag.load(Relaxed) {
        select! {
            sample = sub.recv_async() => {
                let sample = sample.unwrap();
                info!("Storing ('{}': '{}')",
                    sample.key_expr(),
                    sample.payload().try_to_string().unwrap_or_default());
                stored.insert(sample.key_expr().to_string(), sample);
            },
            query = queryable.recv_async() => {
                let query = query.unwrap();
                info!("Handling query '{}'", query.selector());
                for (key, sample) in &stored {
                    if query.key_expr().intersects(
                        unsafe { keyexpr::from_str_unchecked(key) }
                    ) {
                        query.reply_sample(sample.clone()).await.unwrap();
                    }
                }
            }
        }
    }
}
```

### Reading Plugin Configuration

Plugin-specific configuration lives under `plugins.<plugin_name>` in the zenoh config. Inside `Plugin::start`, read it via:

```rust
let config = runtime.get_config().get_plugin_config(name).unwrap_or_default();

// config is a serde_json::Value (an object)
if let Some(obj) = config.as_object() {
    let timeout = obj.get("timeout_ms")
        .and_then(|v| v.as_u64())
        .unwrap_or(1000);
    
    let topics: Vec<String> = obj.get("topics")
        .and_then(|v| v.as_array())
        .map(|arr| arr.iter()
            .filter_map(|v| v.as_str().map(String::from))
            .collect())
        .unwrap_or_default();
}
```

---

## Writing a Storage Backend {#storage-backend}

Storage backends are a specialized plugin type managed by `zenoh-plugin-storage-manager`. Instead of receiving `DynamicRuntime`, they receive a `VolumeConfig`.

### Concept: Volumes and Storages

- **Volume**: A backend instance (e.g., one RocksDB instance, one S3 bucket). Implements the `Volume` trait.
- **Storage**: A mapping from a key expression to a Volume. Multiple storages can share one volume. Implements the `Storage` trait.

The storage manager creates volumes by calling `Plugin::start()` on backend libraries, then creates storage instances by calling `Volume::create_storage()`.

### The Volume Trait

```rust
#[async_trait]
pub trait Volume: Send + Sync {
    /// Status reported to the admin space
    fn get_admin_status(&self) -> JsonValue;
    
    /// Declare what guarantees this volume provides
    fn get_capability(&self) -> Capability;
    
    /// Create a new storage instance for the given config
    async fn create_storage(&self, props: StorageConfig) -> ZResult<Box<dyn Storage>>;
}
```

`Capability` tells the storage manager about persistence and history guarantees:

```rust
pub struct Capability {
    pub persistence: Persistence,  // Volatile | Durable
    pub history: History,          // Latest | All
}
```

### The Storage Trait

```rust
#[async_trait]
pub trait Storage: Send + Sync {
    fn get_admin_status(&self) -> JsonValue;

    /// Store a value. key is None when it exactly matches strip_prefix.
    async fn put(
        &mut self,
        key: Option<OwnedKeyExpr>,
        payload: ZBytes,
        encoding: Encoding,
        timestamp: Timestamp,
    ) -> ZResult<StorageInsertionResult>;

    /// Delete a value.
    async fn delete(
        &mut self,
        key: Option<OwnedKeyExpr>,
        timestamp: Timestamp,
    ) -> ZResult<StorageInsertionResult>;

    /// Retrieve values matching key_expr.
    async fn get(
        &mut self,
        key_expr: Option<OwnedKeyExpr>,
        parameters: &str,
    ) -> ZResult<Vec<StoredData>>;

    /// List all (key, timestamp) pairs - used by replication.
    async fn get_all_entries(&self) -> ZResult<Vec<(Option<OwnedKeyExpr>, Timestamp)>>;
}
```

`StorageInsertionResult` communicates what happened:
- `Inserted`: new entry created
- `Replaced`: existing entry updated
- `Outdated`: incoming timestamp is older than stored, not applied
- `Deleted`: entry removed

### The `None` Key Case

When a key expression exactly matches the `strip_prefix` configuration, the key passed to `put`, `delete`, and `get` will be `None`. Your storage must handle this case correctly—do not ignore it, as it represents a valid data entry.

### Cargo.toml for a Backend

```toml
[package]
name = "zenoh-backend-mydb"
version = "1.0.0"
edition = "2021"

[lib]
# zenoh-plugin-storage-manager looks for libraries named "zenoh_backend_<name>"
# so this name determines what you put in the volumes config.
name = "zenoh_backend_mydb"
crate-type = ["cdylib"]

[dependencies]
zenoh = { version = "1.0", features = ["default", "internal", "unstable"] }
zenoh-plugin-trait = { version = "1.0" }
zenoh_backend_traits = { version = "1.0" }
async-trait = "0.1"
tracing = "0.1"
git-version = "0.3"
```

### Example: In-Memory HashMap Backend

This is the complete implementation of an in-memory storage backend, equivalent to zenoh's built-in `memory` backend:

```rust
use std::collections::HashMap;

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
    Capability, History, Persistence, Storage, StorageInsertionResult, StoredData, Volume,
    VolumeInstance,
};
use zenoh_plugin_trait::{plugin_long_version, plugin_version, Plugin, PluginControl};
use zenoh_util::ffi::JsonValue;

// ─── Volume (the "backend factory") ──────────────────────────────────────────

pub struct MemoryVolume {
    config: VolumeConfig,
}

// Register dynamic entry points
zenoh_plugin_trait::declare_plugin!(MemoryVolume);

impl Plugin for MemoryVolume {
    // Storage backends use VolumeConfig as StartArgs, not DynamicRuntime
    type StartArgs = VolumeConfig;
    type Instance = VolumeInstance;   // Box<dyn Volume>

    const DEFAULT_NAME: &'static str = "memory";
    const PLUGIN_VERSION: &'static str = plugin_version!();
    const PLUGIN_LONG_VERSION: &'static str = plugin_long_version!();

    fn start(_name: &str, args: &VolumeConfig) -> ZResult<VolumeInstance> {
        Ok(Box::new(MemoryVolume { config: args.clone() }))
    }
}

#[async_trait]
impl Volume for MemoryVolume {
    fn get_admin_status(&self) -> JsonValue {
        // Return the volume's config as its admin status
        self.config.to_json_value().into()
    }

    fn get_capability(&self) -> Capability {
        Capability {
            persistence: Persistence::Volatile,  // data lost on restart
            history: History::Latest,            // only keeps newest value per key
        }
    }

    async fn create_storage(&self, config: StorageConfig) -> ZResult<Box<dyn Storage>> {
        tracing::debug!("Creating MemoryStorage for key_expr={}", config.key_expr);
        Ok(Box::new(MemoryStorage::new(config)))
    }
}

// ─── Storage (one storage instance) ──────────────────────────────────────────

struct MemoryStorage {
    config: StorageConfig,
    // RwLock allows concurrent reads, exclusive writes
    // The map key is Option<OwnedKeyExpr> to handle the strip_prefix==key case
    data: RwLock<HashMap<Option<OwnedKeyExpr>, StoredData>>,
}

impl MemoryStorage {
    fn new(config: StorageConfig) -> Self {
        MemoryStorage {
            config,
            data: RwLock::new(HashMap::new()),
        }
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
        tracing::trace!("put {:?}", key);
        let mut map = self.data.write().await;

        // Reject outdated updates (important for replication correctness)
        if let Some(existing) = map.get(&key) {
            if existing.timestamp > timestamp {
                tracing::debug!("Dropping outdated put for {:?}", key);
                return Ok(StorageInsertionResult::Outdated);
            }
        }

        let result = if map.contains_key(&key) {
            StorageInsertionResult::Replaced
        } else {
            StorageInsertionResult::Inserted
        };

        map.insert(key, StoredData { payload, encoding, timestamp });
        Ok(result)
    }

    async fn delete(
        &mut self,
        key: Option<OwnedKeyExpr>,
        _timestamp: Timestamp,
    ) -> ZResult<StorageInsertionResult> {
        tracing::trace!("delete {:?}", key);
        self.data.write().await.remove(&key);
        Ok(StorageInsertionResult::Deleted)
    }

    async fn get(
        &mut self,
        key: Option<OwnedKeyExpr>,
        _parameters: &str,
    ) -> ZResult<Vec<StoredData>> {
        tracing::trace!("get {:?}", key);
        let map = self.data.read().await;

        match &key {
            // Exact key lookup (or None key lookup)
            Some(_) | None => {
                match map.get(&key) {
                    Some(data) => Ok(vec![data.clone()]),
                    None => Ok(vec![]),
                }
            }
        }
    }

    async fn get_all_entries(&self) -> ZResult<Vec<(Option<OwnedKeyExpr>, Timestamp)>> {
        let map = self.data.read().await;
        Ok(map.iter().map(|(k, v)| (k.clone(), v.timestamp)).collect())
    }
}

impl Drop for MemoryStorage {
    fn drop(&mut self) {
        tracing::debug!("MemoryStorage dropped");
    }
}
```

### Wildcard Get Handling

The `get` method receives the key expression **after** the `strip_prefix` has been removed. If the storage manager is configured with `strip_prefix`, you may receive wildcard key expressions like `sensors/*` in your `get` call.

For a HashMap-based storage, you need to iterate and match:

```rust
async fn get(
    &mut self,
    key: Option<OwnedKeyExpr>,
    _parameters: &str,
) -> ZResult<Vec<StoredData>> {
    let map = self.data.read().await;

    match &key {
        None => {
            // The query key exactly matched the strip_prefix
            Ok(map.get(&None).cloned().into_iter().collect())
        }
        Some(query_ke) => {
            if query_ke.is_wild() {
                // Wildcard: return all matching entries
                let mut results = Vec::new();
                for (stored_key, data) in map.iter() {
                    if let Some(sk) = stored_key {
                        if query_ke.intersects(sk) {
                            results.push(data.clone());
                        }
                    }
                }
                Ok(results)
            } else {
                // Exact lookup
                Ok(map.get(&Some(query_ke.clone())).cloned().into_iter().collect())
            }
        }
    }
}
```

---

## Plugin Configuration Schema {#config-schema}

### Generic Plugin Configuration

Plugin configuration lives in the zenoh config file under the `plugins` key. The entire object under `plugins.<name>` is passed to your plugin via `runtime.get_config().get_plugin_config(name)`.

```json5
// zenoh config (JSON5)
{
  "plugins": {
    "myplugin": {
      // Tell zenohd where to find the library (optional if in search path)
      "__path__": [
        "/usr/lib/zenoh/libzenoh_plugin_myplugin.so",
        "/usr/lib/zenoh/libzenoh_plugin_myplugin.dylib"
      ],
      // Plugin-specific config fields
      "key_expr": "demo/myplugin/**",
      "timeout_ms": 5000,
      "features": ["subscribe", "query"]
    }
  }
}
```

### Typed Config with Serde

For robust configuration parsing, define a typed struct with `serde`:

```rust
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct MyPluginConfig {
    /// Key expression to subscribe to
    #[serde(default = "default_key_expr")]
    pub key_expr: String,

    /// Timeout for operations in milliseconds
    #[serde(default = "default_timeout")]
    pub timeout_ms: u64,

    /// Optional list of feature flags
    #[serde(default)]
    pub features: Vec<String>,
}

fn default_key_expr() -> String { "demo/myplugin/**".to_string() }
fn default_timeout() -> u64 { 5000 }

impl MyPluginConfig {
    pub fn from_runtime(runtime: &DynamicRuntime, name: &str) -> ZResult<Self> {
        let raw = runtime
            .get_config()
            .get_plugin_config(name)
            .ok_or_else(|| format!("No config found for plugin '{}'", name))?;

        serde_json::from_value(raw)
            .map_err(|e| format!("Invalid config for plugin '{}': {}", name, e).into())
    }
}

// Use in Plugin::start:
fn start(name: &str, runtime: &Self::StartArgs) -> ZResult<Self::Instance> {
    let config = MyPluginConfig::from_runtime(runtime, name)?;
    // ...
}
```

### Storage Backend Plugin Configuration

The `zenoh-plugin-storage-manager` uses a structured configuration with `volumes` and `storages` sections:

```json5
{
  "plugins": {
    "storage_manager": {
      // Optional: additional directories to search for backend libraries
      "backend_search_dirs": ["/usr/lib/zenoh/backends"],

      // Volume definitions: name -> backend config
      "volumes": {
        // Built-in memory backend (no path needed, statically linked)
        "memory": {},

        // External backend loaded by library name
        // Looks for libzenoh_backend_rocksdb.so in search dirs
        "myrocksdb": {
          "backend": "rocksdb",
          "db_path": "/var/lib/zenoh/rocksdb"
        },

        // External backend loaded by explicit path
        "myvolume": {
          "__path__": [
            "/opt/zenoh/libzenoh_backend_mydb.so",
            "/opt/zenoh/libzenoh_backend_mydb.dylib"
          ],
          // Additional config passed to the Volume as VolumeConfig.rest
          "connection_string": "host=localhost port=5432"
        }
      },

      // Storage definitions: name -> storage config
      "storages": {
        "sensors": {
          "volume": "memory",           // Which volume to use
          "key_expr": "sensors/**",     // What key expressions to store
          "complete": false,            // true = this is the complete, authoritative storage
          "strip_prefix": "sensors"    // Optional: strip this prefix before passing to backend
        },

        "archived": {
          // Volume reference with backend-specific config
          "volume": {
            "id": "myrocksdb",
            "column_family": "archived_data"  // Backend-specific
          },
          "key_expr": "archive/**",

          // Garbage collection for metadata
          "garbage_collection": {
            "period": 3600,    // Run GC every hour (seconds)
            "lifespan": 86400  // Remove metadata older than 1 day (seconds)
          },

          // Optional: enable replication with other storages
          "replication": {
            "interval": 10.0,          // Digest interval in seconds
            "sub_intervals": 5,        // Sub-intervals per interval
            "hot": 6,                  // Hot era: last 6 intervals
            "warm": 30,                // Warm era: last 30 intervals
            "propagation_delay": 250   // Expected network delay in ms
          }
        }
      }
    }
  }
}
```

### Config Validation with JSON Schema

The storage manager validates its config at build time using `schemars`. You can do the same for your plugin by deriving `JsonSchema`:

```rust
// Cargo.toml: schemars = { version = "0.8", features = ["derive"] }
use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize, JsonSchema)]
pub struct MyPluginConfig {
    ///