# Zenoh Comprehensive FAQ

---

## Getting Started

### Q: What is zenoh and how does it compare to MQTT/DDS/Kafka/ROS2?

**A:** Zenoh (pronounced */zeno/*) is a protocol that unifies **data in motion, data at rest, and computations**. It combines pub/sub messaging with geo-distributed storage and distributed queries in a single, highly efficient stack.

| Feature | Zenoh | MQTT | DDS | Kafka |
|---------|-------|------|-----|-------|
| Pub/Sub | ✅ | ✅ | ✅ | ✅ |
| Query/Reply | ✅ | ❌ | Limited | ❌ |
| Storage/History | ✅ (built-in) | ❌ | Limited | ✅ |
| Peer-to-peer | ✅ | ❌ | ✅ | ❌ |
| Brokerless | ✅ | ❌ | ✅ | ❌ |
| Constrained devices | ✅ (zenoh-pico) | ✅ | ❌ | ❌ |
| WAN/Internet | ✅ | Partial | Hard | ✅ |
| Discovery overhead | Very low | N/A | High | N/A |

**Key differentiators vs MQTT:** No central broker required; supports queries and storage; wildcard subscriptions use a richer model; runs peer-to-peer natively.

**Key differentiators vs DDS:** Dramatically lower discovery overhead (97–99.97% less traffic measured in ROS2 scenarios); scales to WAN/Internet; works on constrained devices.

**Key differentiators vs Kafka:** No JVM/heavy broker; sub-millisecond latency; native peer-to-peer; works on edge/embedded devices.

**Key differentiators vs ROS2:** Zenoh can transparently bridge ROS2 traffic while reducing discovery overhead by up to 99.97%; supports Internet-scale routing natively.

---

### Q: How do I install zenoh?

**A:** There are several options depending on your use case:

**Rust library** (add to `Cargo.toml`):
```toml
[dependencies]
zenoh = "1.5.1"
```

For shared memory support:
```toml
zenoh = { version = "1.5.1", features = ["shared-memory"] }
```

**Build from source:**
```bash
# Install Rust first: https://doc.rust-lang.org/cargo/getting-started/installation.html
rustup update

git clone https://github.com/eclipse-zenoh/zenoh.git
cd zenoh
cargo build --release --all-targets
```

**Run the zenoh router (`zenohd`):**
```bash
cargo run --bin zenohd -- --config DEFAULT_CONFIG.json5
# or after build:
./target/release/zenohd
```

**Other language bindings** are available as separate repositories:
- C/C++: `zenoh-c`, `zenoh-pico`, `zenoh-cpp`
- Python: `zenoh-python`
- Kotlin/Java: `zenoh-kotlin`, `zenoh-java`
- TypeScript: `zenoh-ts`

---

### Q: What programming languages does zenoh support?

**A:** Zenoh supports a wide range of languages:

| Language | Package | Notes |
|----------|---------|-------|
| **Rust** | `zenoh` crate | Primary/reference implementation |
| **C** | `zenoh-c` | Rust library binding |
| **C** (pure) | `zenoh-pico` | Pure C, for microcontrollers |
| **C++** | `zenoh-cpp` | C++ wrapper over C libraries |
| **Python** | `zenoh-python` | |
| **Kotlin** | `zenoh-kotlin` | |
| **Java** | `zenoh-java` | |
| **TypeScript** | `zenoh-ts` | WebSocket client via zenohd plugin |

All non-Rust bindings wrap or bind to the Rust implementation (except `zenoh-pico` which is a pure C implementation of the zenoh protocol).

---

### Q: Do I need a broker/server to use zenoh?

**A:** No. Zenoh supports fully **brokerless peer-to-peer** operation. Nodes in `peer` mode discover each other (via UDP multicast by default) and route data directly between themselves.

However, a **zenoh router (`zenohd`)** is useful when:
- Connecting nodes across different network segments or the WAN/Internet
- Bridging multiple local networks
- Hosting persistent storage plugins
- Enabling TypeScript/WebSocket clients (which require a router with the TypeScript plugin)

**Minimal example with no router:**
```rust
// Both nodes run peer mode; discovery via multicast
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
```

---

### Q: What's the difference between zenoh router, peer, and client mode?

**A:** Zenoh has three session modes:

| Mode | Description | Use Case |
|------|-------------|----------|
| **Router** (`zenohd`) | Dedicated infrastructure node; routes between peers and clients; can host plugins | Connecting multiple subnets, WAN bridging, storage hosting |
| **Peer** | Full participant; routes data to/from other peers; participates in link-state routing; can serve clients | Edge nodes, robot computers, server applications |
| **Client** | Lightweight; connects to a router or peer; does NOT route; does NOT run link-state | Constrained devices, zenoh-pico nodes, simple apps |

**Configure mode in Rust:**
```rust
let mut config = zenoh::Config::default();
// Default is already "peer" for the Rust library
// To explicitly set client mode:
config.set_mode(Some(WhatAmI::Client)).unwrap();
config.connect.endpoints.set(
    ["tcp/192.168.1.10:7447"].iter().map(|s| s.parse().unwrap()).collect()
).unwrap();
let session = zenoh::open(config).await.unwrap();
```

**Key insight:** Peers route on behalf of clients. When using `zenoh-pico` on a microcontroller, it always operates as a client and connects to a peer or router.

---

## Key Expressions and Selectors

### Q: What is a key expression?

**A:** A key expression (KE) is a path-like string that names a resource in zenoh. It is used to identify data when publishing, subscribing, and querying. Key expressions follow a hierarchical structure using `/` as a separator.

Examples:
```
my/robot/sensor/temperature
home/bedroom/light
fleet/robot_01/status
```

You can declare a key expression to let zenoh optimize its wire representation (an integer alias is used instead of the full string):

```rust
let session = zenoh::open(zenoh::Config::default()).await.unwrap();

// Simple use - just pass the string
session.put("my/robot/sensor/temperature", 42.0_f32).await.unwrap();

// Declare for optimization when using repeatedly
let key = session.declare_keyexpr("my/robot/sensor/temperature").await.unwrap();
session.put(&key, 42.0_f32).await.unwrap();
```

**Rules for valid key expressions:**
- Non-empty string
- Cannot contain `?` or `#` (those are selector/parameter syntax)
- Segments are separated by `/`
- Can contain wildcards (`*`, `**`, `$*`) for subscriptions and queries

---

### Q: How do wildcards work? (`*`, `**`, `$*`)

**A:** Zenoh supports three wildcard types:

| Wildcard | Matches | Example |
|----------|---------|---------|
| `*` | Any single path segment (no `/`) | `home/*/light` matches `home/bedroom/light` but NOT `home/floor1/room2/light` |
| `**` | Any number of path segments (including zero) | `home/**/light` matches `home/light`, `home/bedroom/light`, `home/floor1/room2/light` |
| `$*` | Any suffix within a segment (DSL-like) | `home/$*room/light` matches `home/bedroom/light`, `home/livingroom/light` |

```rust
// Subscribe to all temperature sensors across all robots
let sub = session.declare_subscriber("fleet/*/sensors/temperature").await.unwrap();

// Subscribe to everything under fleet/
let sub = session.declare_subscriber("fleet/**").await.unwrap();

// Subscribe to all sensors of any type
let sub = session.declare_subscriber("fleet/robot_01/sensors/*").await.unwrap();
```

---

### Q: What's the difference between `*` and `**`?

**A:**

- `*` matches exactly **one** path segment (no `/` allowed in match)
- `**` matches **zero or more** path segments (crosses `/` boundaries)

```
Key: home/floor1/room2/temp

"home/*/temp"        → NO MATCH  (two segments between home and temp)
"home/**/temp"       → MATCH
"home/*/*/temp"      → MATCH
"home/**"            → MATCH
"**"                 → MATCH (matches everything)
"home/floor1/room2/temp" → MATCH (exact)
```

**Practical rule:** Use `*` when you know the exact depth of the hierarchy. Use `**` when the depth may vary.

---

### Q: What is a Selector?

**A:** A Selector extends a key expression with optional **parameters** (query string), used with `session.get()` queries. The format is:

```
key_expression?param1=value1&param2=value2
```

```rust
// Query with parameters
let replies = session.get("fleet/**/temperature?_time=[now(-1h)..]").await.unwrap();

// Query without parameters (just a key expression)
let replies = session.get("fleet/robot_01/status").await.unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Got: {} = {:?}", sample.key_expr(), sample.payload()),
        Err(err) => println!("Error: {:?}", err),
    }
}
```

Parameters are passed to the queryable and can be interpreted by the storage or application logic. Standard parameters include:
- `_time` — time-range query for storages (e.g., `_time=[now(-1h)..]`)
- Custom parameters defined by your queryable

---

### Q: How do key expression operators work (`&`, `|`, `)`)?

**A:** Zenoh key expressions support set-theoretic operations that allow computing intersections, unions, and canonical forms:

- **Intersection (`intersects()`)**: Do the two KEs match any common resources?
- **Inclusion (`includes()`)**: Does KE A include all resources matched by KE B?
- **Canonicalization**: Simplify a KE to its canonical form

These are used internally for routing decisions and storage matching, but also available in the API:

```rust
use zenoh::key_expr::KeyExpr;

let ke1: KeyExpr = "home/**".try_into().unwrap();
let ke2: KeyExpr = "home/bedroom/light".try_into().unwrap();

assert!(ke1.intersects(&ke2));  // true
assert!(ke1.includes(&ke2));    // true - ke1 is superset
```

**Practical use:** When zenoh routes a publication, it checks `intersects()` against all subscriber key expressions to determine which subscribers should receive the data. This is also how storage queries determine which stored keys to return.

---

## Pub/Sub

### Q: How does pub/sub differ from traditional MQTT?

**A:** Several important differences:

| Feature | Zenoh | MQTT |
|---------|-------|------|
| Broker required | No (peer mode) | Yes |
| Wildcard matching | `*`, `**`, `$*` | `+`, `#` |
| QoS levels | Priority + Reliability + CongestionControl | 0, 1, 2 |
| Query/reply | Native | No |
| Retained messages | Via storage plugin | Via broker flag |
| Session modes | Router/Peer/Client | Client only |
| Payload encoding | Typed `ZBytes` + `Encoding` | Raw bytes |
| Timestamps | Built-in HLC timestamps | No |

```rust
// Publisher
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let publisher = session
    .declare_publisher("my/topic")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Drop)
    .await
    .unwrap();
publisher.put("hello world").await.unwrap();

// Subscriber
let subscriber = session.declare_subscriber("my/topic").await.unwrap();
while let Ok(sample) = subscriber.recv_async().await {
    println!("Received: {:?}", sample.payload());
}
```

---

### Q: What is Locality filtering?

**A:** Locality filtering controls whether a publisher or subscriber communicates with **local** (same process/session), **remote** (different sessions/processes), or **any** (both) endpoints.

```rust
use zenoh::sample::Locality;

// Only receive from remote publishers (not local ones in same session)
let sub = session
    .declare_subscriber("my/topic")
    .allowed_origin(Locality::Remote)
    .await
    .unwrap();

// Only publish locally within this session (useful for testing or local IPC)
let pub_ = session
    .declare_publisher("my/topic")
    .allowed_destination(Locality::SessionLocal)
    .await
    .unwrap();

// Default: Locality::Any (both local and remote)
```

**Use cases:**
- `SessionLocal`: Intra-process communication, avoiding network overhead
- `Remote`: A subscriber that only wants external data, ignoring its own session's publishers
- `Any`: Default behavior — receive from everywhere

---

### Q: What are the priority levels and when do I use them?

**A:** Zenoh has 7 priority levels (lower number = higher priority):

| Priority | Value | Use Case |
|----------|-------|----------|
| `RealTime` | 1 | Highest — safety-critical, actuator commands |
| `InteractiveHigh` | 2 | Time-sensitive UI updates |
| `InteractiveLow` | 3 | Interactive but tolerant of slight delays |
| `DataHigh` | 4 | Important sensor data |
| `Data` | 5 | **Default** — normal data |
| `DataLow` | 6 | Background data streams |
| `Background` | 7 | Lowest — bulk transfers, logging |

```rust
use zenoh::publisher::Priority;

// High-priority publisher for robot commands
let cmd_publisher = session
    .declare_publisher("robot/commands")
    .priority(Priority::RealTime)
    .await
    .unwrap();

// Low-priority publisher for diagnostics
let log_publisher = session
    .declare_publisher("robot/diagnostics")
    .priority(Priority::Background)
    .await
    .unwrap();
```

When a zenoh transport link becomes congested, higher-priority messages are sent first. This ensures critical data (e.g., emergency stop commands) gets through even when the network is busy.

---

### Q: What's the difference between `BestEffort` and `Reliable`?

**A:** These are the two **reliability** modes for data transmission:

| Mode | Guarantee | Overhead | Use Case |
|------|-----------|----------|----------|
| `BestEffort` | No delivery guarantee — messages may be lost | Lower | High-frequency sensor data, video streams, position updates |
| `Reliable` | Ordered, loss-less delivery (within transport) | Higher | Commands, state changes, critical events |

```rust
use zenoh_protocol::core::Reliability;

// BestEffort (default for most transports) - fast sensor stream
let publisher = session
    .declare_publisher("robot/lidar")
    // BestEffort is the default
    .await
    .unwrap();

// Reliable - important state updates (unstable API)
#[cfg(feature = "unstable")]
let publisher = session
    .declare_publisher("robot/commands")
    .reliability(Reliability::Reliable)
    .await
    .unwrap();
```

**Important note:** `Reliable` in zenoh means reliable delivery over each individual transport hop. It does NOT provide end-to-end reliability across a multi-hop routed path in all scenarios. For end-to-end guaranteed delivery with history/retransmission, see `zenoh-ext`'s `AdvancedPublisher`/`AdvancedSubscriber`.

---

### Q: What is `CongestionControl` and when does `Drop` vs `Block` matter?

**A:** `CongestionControl` determines what zenoh does when a downstream buffer is full:

| Mode | Behavior | Use Case |
|------|----------|----------|
| `Drop` | **Drop the message** — never blocks the publisher | High-frequency data where latest value matters more than completeness (sensor streams, video) |
| `Block` | **Block the publisher** until buffer drains | Critical data that must not be lost (commands, events) |

```rust
use zenoh_protocol::core::CongestionControl;

// Sensor publisher - it's OK to drop old readings when congested
let sensor_pub = session
    .declare_publisher("robot/sensors/lidar")
    .congestion_control(CongestionControl::Drop)  // Default
    .await
    .unwrap();

// Command publisher - never drop a command
let cmd_pub = session
    .declare_publisher("robot/commands")
    .congestion_control(CongestionControl::Block)
    .await
    .unwrap();
```

**Recommendation:**
- Use `Drop` for high-frequency streaming data (sensors, video, telemetry)
- Use `Block` for infrequent but critical messages (commands, configuration changes)

---

### Q: How do I handle backpressure?

**A:** Zenoh handles backpressure through `CongestionControl`:

1. **`CongestionControl::Drop`** — publisher never blocks; messages are silently dropped when the receiver can't keep up. This is the zero-backpressure approach.

2. **`CongestionControl::Block`** — publisher blocks (async `await`) until the downstream can accept the message. This propagates backpressure to the publisher.

For the subscriber side, using an async handler processes messages as fast as possible:

```rust
// Option 1: Channel-based subscriber (natural backpressure via channel capacity)
let subscriber = session
    .declare_subscriber("my/topic")
    .await
    .unwrap();

tokio::spawn(async move {
    while let Ok(sample) = subscriber.recv_async().await {
        // Process sample - if this is slow, channel fills up
        process(sample).await;
    }
});

// Option 2: Callback-based (called inline - keep it fast)
let subscriber = session
    .declare_subscriber("my/topic")
    .callback(|sample| {
        // Must be fast - blocking here blocks routing
        println!("Got: {:?}", sample.key_expr());
    })
    .await
    .unwrap();
```

**Best practice:** For slow consumers, use the channel-based API with `recv_async()` and set `CongestionControl::Drop` on publishers to avoid memory buildup.

---

## Query/Reply (Queryable)

### Q: What is a Queryable and when do I use it instead of a subscriber?

**A:** A `Queryable` responds to on-demand queries (`session.get()`). Think of it as a **request/response** or **RPC** pattern, vs pub/sub's continuous streaming.

**Use a Queryable when:**
- You want to serve current state on demand
- You need request/response semantics
- You're implementing a storage or cache
- You want to support time-range or filtered queries

**Use a Subscriber when:**
- You want to receive all future publications continuously
- You need push-based data delivery

```rust
// Queryable - serves data on request
let queryable = session
    .declare_queryable("robot/status")
    .await
    .unwrap();

tokio::spawn(async move {
    while let Ok(query) = queryable.recv_async().await {
        println!("Got query on: {} with params: {}", 
                 query.key_expr(), query.parameters());
        
        // Reply with current value
        query.reply("robot/status", "running").await.unwrap();
        
        // Or reply with an error
        // query.reply_err("not available").await.unwrap();
    }
});

// Query the queryable
let replies = session.get("robot/status").await.unwrap();
while let Ok(reply) = replies.recv_async().await {
    println!("Status: {:?}", reply.result());
}
```

A queryable can reply with **multiple samples** (e.g., a storage returning historical data) and must explicitly send all replies before the query handler is dropped.

---

### Q: What is `ConsolidationMode`?

**A:** `ConsolidationMode` controls how the zenoh runtime handles **duplicate replies** when multiple queryables respond to the same query (e.g., multiple storages):

| Mode | Behavior |
|------|----------|
| `None` | Pass all replies through as-is — caller sees every reply |
| `Monotonic` | Per key expression: forward a new reply only if its timestamp is ≥ the last seen for that KE (delivers monotonically increasing data during query) |
| `Latest` | Per key expression: buffer all replies, then deliver only the one with the **latest timestamp** per KE at the end |
| `Auto` | Default — uses `Latest` normally; switches to `None` if a time-range parameter is present |

```rust
use zenoh::query::{ConsolidationMode, QueryConsolidation};

// Get only the latest value for each key (default for simple gets)
let replies = session
    .get("fleet/**/temperature")
    .consolidation(ConsolidationMode::Latest)
    .await
    .unwrap();

// Get all replies including duplicates (e.g., for debugging)
let replies = session
    .get("fleet/**/temperature")
    .consolidation(ConsolidationMode::None)
    .await
    .unwrap();
```

**Practical guidance:**
- Use `Latest` (default) when querying storage and you want the most recent value per key
- Use `None` when you want all historical records (combined with time-range parameters)
- Use `Monotonic` for streaming query results where you want progressive updates

---

### Q: How does storage work with queries?

**A:** Zenoh's storage system is provided by the **zenohd router** via storage plugins. A storage:

1. **Subscribes** to a key expression and persists incoming publications
2. **Declares a Queryable** on the same key expression to serve stored data on request
3. Supports time-range queries via the `_time` parameter

Available storage backends include: Memory, InfluxDB, RocksDB, and others via the plugin system.

```bash
# Enable the memory storage backend in zenohd config (JSON5)
{
  plugins: {
    storage_manager: {
      storages: {
        my_storage: {
          key_expr: "robot/**",
          volume: "memory"
        }
      }
    }
  }
}
```

```rust
// Query the storage with a time range
let replies = session
    .get("robot/sensors/temperature?_time=[now(-1h)..]")
    .consolidation(ConsolidationMode::None)  // Want all historical records
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    if let Ok(sample) = reply.result() {
        println!("{}: {:?} at {:?}", 
                 sample.key_expr(), sample.payload(), sample.timestamp());
    }
}
```

---

### Q: What's the difference between a `Querier` and `session.get()`?

**A:** Both issue queries, but they serve different use cases:

| | `session.get()` | `session.declare_querier()` |
|--|----------------|----------------------------|
| **Use case** | One-off queries | Repeated queries to the same KE |
| **Declaration** | No declaration overhead | Declares interest, enabling routing optimizations |
| **Performance** | Fine for infrequent queries | Better for frequent/repeated queries |
| **Configuration** | Set per-call | Set once on declaration |

```rust
// One-off query with session.get()
let replies = session
    .get("robot/status")
    .timeout(Duration::from_secs(1))
    .await
    .unwrap();

// Declared querier - better for repeated queries
let querier = session
    .declare_querier("fleet/**/status")
    .timeout(Duration::from_secs(1))
    .target(QueryTarget::All)
    .await
    .unwrap();

// Can call .get() multiple times efficiently
loop {
    let replies = querier.get().await.unwrap();
    while let Ok(reply) = replies.recv_async().await {
        // process reply
    }
    tokio::time::sleep(Duration::from_secs(5)).await;
}
```

Declaring a querier also signals to the network that you will be querying a certain key expression, which can help routers pre-establish paths to relevant queryables.

---

## Liveliness

### Q: What is liveliness and when should I use it?

**A:** Liveliness is a mechanism to track **whether a zenoh entity (session/node) is alive**. It works through "tokens" — a node declares a liveliness token on a key expression, and when that node disconnects or undeclares the token, all liveliness subscribers are notified.

**Use cases:**
- Service discovery (is my data source still alive?)
- Fleet monitoring (which robots are currently online?)
- Dynamic topology awareness
- Dead peer detection

```rust
// Node A: declare a liveliness token to announce presence
let session_a = zenoh::open(zenoh::Config::default()).await.unwrap();
let token = session_a
    .liveliness()
    .declare_token("fleet/robot_01")
    .await
    .unwrap();
// Token is alive as long as `token` is not dropped and session is open

// Node B: subscribe to liveliness changes
let session_b = zenoh::open(zenoh::Config::default()).await.unwrap();
let liveliness_sub = session_b
    .liveliness()
    .declare_subscriber("fleet/**")
    .history(true)  // Get current state of all alive tokens on subscribe
    .await
    .unwrap();

tokio::spawn(async move {
    while let Ok(sample) = liveliness_sub.recv_async().await {
        match sample.kind() {
            SampleKind::Put => println!("Node came online: {}", sample.key_expr()),
            SampleKind::Delete => println!("Node went offline: {}", sample.key_expr()),
        }
    }
});

// Query currently alive tokens
let replies = session_b
    .liveliness()
    .get("fleet/**")
    .await
    .unwrap();
while let Ok(reply) = replies.recv_async().await {
    if let Ok(sample) = reply.result() {
        println!("Currently alive: {}", sample.key_expr());
    }
}
```

---

### Q: How is liveliness different from a regular pub/sub heartbeat?

**A:** Key differences:

| | Liveliness Token | Heartbeat pub/sub |
|--|-----------------|-------------------|
| **Detection speed** | Near-instant (session-level event) | Delayed by heartbeat interval |
| **False positives** | None — tied to actual session state | Possible (message loss) |
| **Network overhead** | Very low (single declaration) | Continuous (each heartbeat) |
| **Implementation** | Built into zenoh protocol | User-implemented |
| **History** | Built-in (`history=true`) | Must implement manually |

A liveliness token is automatically undeclared when the session closes, even on **abnormal disconnect** (crash, network failure). This makes it far more reliable than a heartbeat, which would keep sending "alive" signals until the application explicitly stops, or stop silently leaving subscribers uncertain.

```rust
// With liveliness: instant detection when node crashes
// The token is automatically undeclared on session close

// With heartbeat: subscriber must wait for missed_beats * interval
// before concluding the publisher is dead
```

---

### Q: How do I detect when a node leaves the network?

**A:** Use a liveliness subscriber with `history=true`:

```rust
let liveness_sub = session
    .liveliness()
    .declare_subscriber("fleet/**")
    .history(true)  // See currently-alive nodes immediately
    .await
    .unwrap();

tokio::spawn(async move {
    while let Ok(sample) = liveness_sub.recv_async().await {
        match sample.kind() {
            SampleKind::Put => {
                // Node joined or was already alive (when history=true)
                println!("Node ONLINE: {}", sample.key_expr());
            }
            SampleKind::Delete => {
                // Node left - session closed or crashed
                println!("Node OFFLINE: {}", sample.key_expr());
                // Trigger reconnection logic, alert, cleanup, etc.
            }
        }
    }
});
```

A `SampleKind::Delete` on a liveliness subscriber is triggered when:
1. The remote session explicitly calls `.close()`
2. The remote session is dropped
3. The transport connection to the remote node is lost (detected by the routing layer)

---

## Performance

### Q: How fast is zenoh? (throughput, latency numbers)

**A:** Benchmarks from the zenoh team (on Linux workstations, AMD Ryzen 7 3800X, 10GbE):

**Throughput:**
- **1 Gbps** reached at **128-byte** message payloads
- **10 Gbps** reached at **1024-byte** message payloads
- The 1 Gbps mark was already achieved on an Intel Core i7 laptop with 128-byte messages in earlier benchmarks

**Messages per second:** Millions of messages/second for small payloads

**Latency:** Sub-microsecond latency achievable in shared-memory mode on the same machine; single-digit microseconds over loopback; network-bound otherwise.

These numbers come from the built-in throughput benchmarks:
```bash
# Build examples
cargo build --release --examples

# Run subscriber (collects 30 measurements of 100K messages each)
./target/release/examples/z_sub_thr -s 30

# Run publisher with 1024-byte payload
./target/release/examples/z_pub_thr 1024
```

**Optimization tip** used in early benchmarks:
```bash
export RUSTFLAGS="-C target-cpu=native"
cargo build --release
```

---

### Q: When should I use shared memory?

**A:** Shared memory (SHM) is beneficial when:
- Publisher and subscriber are on the **same machine** (same OS, not VMs)
- Payload is **large** (images, point clouds, large sensor arrays)
- You want to minimize CPU copies

```toml
# Enable in Cargo.toml
zenoh = { version = "1.5.1", features = ["shared-memory"] }
```

```rust
// Both shared-memory and transport optimization must be enabled in config
// The runtime will handle SHM negotiation automatically when both sides support it
let session = zenoh::open(config).await.unwrap();

// SHM provider is available via (unstable API)
#[cfg(all(feature = "shared-memory", feature = "unstable"))]
let shm_provider = session.get_shm_provider();
```

With SHM enabled, zenoh can pass a pointer to shared memory instead of copying data, resulting in **near-zero copy** for large payloads between processes on the same machine.

**When NOT to use SHM:**
- Cross-machine communication (SHM falls back to normal transport automatically)
- Small payloads (overhead of SHM management exceeds copy cost)
- Environments without shared memory support (some containers, VMs)

---

### Q: How does zenoh compare to DDS performance?

**A:** Based on measurements from the zenoh blog:

- **Discovery overhead:** Zenoh reduces discovery traffic by **97–99.97%** compared to DDS in ROS2 scenarios
  - DDS: 686 packets, ~251 KB for a single ROS2 app startup
  - Zenoh: 31 packets, ~6.6 KB (**97.37% reduction**)
  - Zenoh with resource generalization: 13 packets, ~1.8 KB (**99.29% reduction**)
  - Zenoh warm start + resource generalization: 1 packet, 82 bytes 
---

## See Also
- [concepts.md](concepts.md) — Core zenoh abstractions and terminology
- [configuration-guide.md](configuration-guide.md) — Annotated configuration walkthroughs for common scenarios
- [deployment.md](deployment.md) — Deployment patterns for routers, peers, and clients
