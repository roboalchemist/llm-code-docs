# Zenoh Comprehensive FAQ

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Key Expressions and Selectors](#key-expressions-and-selectors)
3. [Pub/Sub](#pubsub)
4. [Query/Reply (Queryable)](#queryreply-queryable)
5. [Liveliness](#liveliness)
6. [Performance](#performance)
7. [Deployment](#deployment)
8. [ROS 2](#ros-2)
9. [Embedded / IoT](#embedded--iot)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Q: What is zenoh and how does it compare to MQTT/DDS/Kafka/ROS 2?

**A:** Zenoh (pronounced *"zeno"*) is a protocol and middleware stack that unifies **data in motion, data at rest, and computations**. It blends traditional pub/sub with geo-distributed storage, queries, and computation — with time and space efficiency designed to surpass mainstream stacks.

| Feature | Zenoh | MQTT | DDS | Kafka | ROS 2 (DDS) |
|---|---|---|---|---|---|
| Broker required | No (optional) | Yes (broker) | No | Yes (broker) | No |
| Peer-to-peer | Yes | No | Yes | No | Yes |
| Query/storage | Native | No | Limited | Consumer-pull | No |
| WAN/internet | Yes | Yes | Difficult | Yes | Difficult |
| Embedded/IoT | Yes (zenoh-pico) | Yes | Limited | No | No |
| Wildcard routing | Yes (key exprs) | Yes (topics) | Yes (content filter) | No | Partial |
| Throughput | >1 Gbps @ 128B | Lower | High | High | Medium |
| Latency | Sub-microsecond | Milliseconds | Microseconds | Milliseconds | Milliseconds |

Key differentiators:
- **vs MQTT**: No mandatory broker; native peer-to-peer; built-in query/reply; dramatically higher performance; works fine without internet connectivity.
- **vs DDS**: Simpler API; works transparently over WAN; supports clients with minimal resource footprint (zenoh-pico); avoids multicast flooding issues.
- **vs Kafka**: Not a message queue/log; designed for real-time low-latency, not durable stream processing; no broker required; embedded-friendly.
- **vs ROS 2 / DDS**: Drop-in replacement as ROS 2 RMW layer; handles WAN natively; works on microcontrollers; significantly lower overhead.

---

### Q: How do I install zenoh?

**A:** Zenoh has several installation paths depending on your use case.

**Rust library (recommended for Rust apps):**
```toml
# Cargo.toml
[dependencies]
zenoh = "1.5.1"
# For shared memory support:
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

**Run the zenohd router:**
```bash
cargo run --bin zenohd -- --config DEFAULT_CONFIG.json5
# Or from release binary:
./target/release/zenohd
```

**Other languages:**
- **C/C++**: [zenoh-c](https://github.com/eclipse-zenoh/zenoh-c) or [zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico)
- **Python**: [zenoh-python](https://github.com/eclipse-zenoh/zenoh-python) → `pip install eclipse-zenoh`
- **Kotlin/Java**: [zenoh-kotlin](https://github.com/eclipse-zenoh/zenoh-kotlin) / [zenoh-java](https://github.com/eclipse-zenoh/zenoh-java)
- **TypeScript**: [zenoh-ts](https://github.com/eclipse-zenoh/zenoh-ts)

Requires Rust ≥ 1.75.0 to compile from source.

---

### Q: What programming languages does zenoh support?

**A:** Zenoh supports a wide range of languages:

| Language | Repository | Notes |
|---|---|---|
| **Rust** | `eclipse-zenoh/zenoh` | Reference implementation |
| **C** | `eclipse-zenoh/zenoh-c` | Bindings to Rust lib |
| **C** (pure) | `eclipse-zenoh/zenoh-pico` | Pure C, for microcontrollers |
| **C++** | `eclipse-zenoh/zenoh-cpp` | Wrapper over zenoh-c |
| **Python** | `eclipse-zenoh/zenoh-python` | Bindings to Rust lib |
| **Kotlin** | `eclipse-zenoh/zenoh-kotlin` | JVM-based |
| **Java** | `eclipse-zenoh/zenoh-java` | JVM-based |
| **TypeScript** | `eclipse-zenoh/zenoh-ts` | WebSocket client via zenohd plugin |

The Rust crate is the primary, reference implementation. All other language bindings (except zenoh-pico) are wrappers around it.

---

### Q: Do I need a broker/server to use zenoh?

**A:** No — zenoh is designed to work **without any infrastructure** in many scenarios. Three modes govern how zenoh nodes connect:

- **Peer mode**: Nodes discover each other directly (via multicast scouting or configured endpoints) and route messages among themselves. No central broker needed.
- **Client mode**: Nodes connect to a router (zenohd) and rely on it for routing. Simpler but requires a router to be running.
- **Router mode**: The `zenohd` daemon acts as a routing infrastructure node, enabling larger networks, WAN connectivity, and plugin services (storage, REST API, etc.).

For simple local networks or embedded scenarios, **peer mode with no infrastructure** works out of the box. A router becomes valuable when you need WAN bridging, storage, or a stable rendezvous point.

---

### Q: What's the difference between zenoh router, peer, and client mode?

**A:**

| Mode | Binary | Routing | Discovery | Use case |
|---|---|---|---|---|
| **Router** | `zenohd` | Full routing tables | Responds to scout messages | Infrastructure node, WAN bridges, plugins |
| **Peer** | Your app | Routes among peers | Multicast scouting or configured endpoints | Local/LAN P2P, no infrastructure needed |
| **Client** | Your app | Delegates to router | Connects to router endpoint | Lightweight nodes, IoT devices, mobile apps |

**Router**: Runs as `zenohd`. Builds and maintains full routing tables. Supports plugins (storage, REST, etc.). Necessary for connecting different network segments.

**Peer**: Your application acts as a full participant. It can route data between itself and other peers. Supports arbitrary connectivity graphs. No single point of failure.

**Client**: Your application connects to one or more routers and delegates all routing to them. Lower resource overhead. Best for constrained devices or nodes that don't need to route.

**Configure the mode in your config or code:**
```rust
// Rust: set peer mode (default)
let mut config = zenoh::Config::default();
config.set_mode(Some(zenoh_config::WhatAmI::Peer)).unwrap();

// Client mode connecting to a router
config.set_mode(Some(zenoh_config::WhatAmI::Client)).unwrap();
config.connect.endpoints.set(
    vec!["tcp/192.168.1.100:7447".parse().unwrap()]
).unwrap();
```

---

## Key Expressions and Selectors

### Q: What is a key expression?

**A:** A key expression (KE) is zenoh's addressing mechanism — analogous to MQTT topics or DDS resource names, but more powerful. It is a UTF-8 string structured as a **path** using `/` as a separator.

```
robot/arm/joint1/position
sensors/temperature/room42
vehicle/telemetry/**
```

Key expressions can be:
- **Concrete** (no wildcards): `robot/arm/joint1` — identifies a single resource.
- **Wildcard** (with `*`, `**`, `$*`): match multiple resources.

In the API, you declare key expressions to enable wire-level optimization (the session assigns a numeric ID to avoid sending the full string repeatedly):

```rust
// Declare a key expression for reuse (wire optimization)
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let ke = session.declare_keyexpr("robot/arm/**").await.unwrap();
let publisher = session.declare_publisher(&ke).await.unwrap();
```

---

### Q: How do wildcards work? (`*`, `**`, `$*`)

**A:** Zenoh key expressions support three wildcard forms:

| Wildcard | Matches | Example |
|---|---|---|
| `*` | Any single chunk (between `/` separators), no `/` | `robot/*/position` matches `robot/arm/position` but NOT `robot/arm/joint1/position` |
| `**` | Any number of chunks, including zero, spanning `/` | `robot/**` matches `robot/arm`, `robot/arm/joint1`, `robot/arm/joint1/position` |
| `$*` | Used inside a chunk for partial matching | `robot/arm$*` matches `robot/arm`, `robot/arm1`, `robot/armL` |

**Examples:**
```
# * — single level wildcard
sensors/*/temp     → matches sensors/room1/temp, sensors/room2/temp
                   → does NOT match sensors/building1/room1/temp

# ** — multi-level wildcard
sensors/**         → matches sensors/room1/temp, sensors/building1/room1/temp, sensors/

# $* — partial chunk wildcard
robot/joint$*      → matches robot/joint1, robot/joint2, robot/jointA
```

**Intersection vs. Inclusion:**
- Two key expressions *intersect* if there is at least one concrete key matching both.
- Key expression A *includes* B if every key matching B also matches A.

Subscribers receive a sample if their key expression **intersects** with the publisher's key expression.

---

### Q: What's the difference between `*` and `**`?

**A:** The critical difference is **slash crossing**:

- `*` matches **exactly one path chunk** — it will not cross a `/`.
- `**` matches **zero or more chunks** — it crosses `/` boundaries freely.

```
Key expr: a/*/c
Matches:  a/b/c        ✓
Misses:   a/b/d/c      ✗ (two chunks between a and c)
Misses:   a/c          ✗ (zero chunks between a and c)

Key expr: a/**/c
Matches:  a/b/c        ✓
Matches:  a/b/d/c      ✓
Matches:  a/c          ✓ (** can match zero chunks)
Matches:  a/b/d/e/f/c  ✓
```

**Practical tip:** Use `**` when you want to subscribe to an entire subtree. Use `*` when you want exactly one dynamic segment.

---

### Q: What is a Selector?

**A:** A Selector extends a key expression with **query parameters**, similar to a URL query string. It is used in `session.get()` to query data from Queryables and storages.

```
Selector syntax:  <key_expression>?<parameters>

Examples:
  sensors/temperature?room=42
  robot/**?since=2024-01-01&limit=100
  data/metrics?_time=[now(-1h)..]
```

The part after `?` is the **Parameters** string. Queryables receive the full selector and can parse the parameters to filter/customize their response.

```rust
// Send a query with selector parameters
let replies = session
    .get("sensors/temperature?room=42&format=json")
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Got: {}", sample.key_expr()),
        Err(err) => println!("Error: {:?}", err),
    }
}
```

Time-range queries (using the `_time` parameter) are a special built-in parameter understood by zenoh storages for historical data retrieval.

---

### Q: How do key expression operators work (`&`, `|`, `)`)?

**A:** Zenoh supports **set operations** on key expressions for advanced routing and subscription scenarios (these are part of the unstable/advanced API):

- **`|` (Union)**: A key expression that matches resources matched by either operand.
  ```
  sensors/temp | sensors/humidity
  ```
  Matches anything matching `sensors/temp` OR `sensors/humidity`.

- **`&` (Intersection)**: Restricts to resources matched by both (rarely used directly, more relevant for routing logic).

- **Canonicalization**: Zenoh automatically simplifies and canonicalizes key expressions to avoid redundancy (e.g., `a/** | a/b` simplifies to `a/**`).

These operators are primarily relevant when working with zenoh's internal routing logic and advanced key expression algebra. Most application developers use simple key expressions with wildcards (`*`, `**`) rather than explicit set operators.

---

## Pub/Sub

### Q: How does pub/sub differ from traditional MQTT?

**A:** Several important differences:

| Aspect | Zenoh | MQTT |
|---|---|---|
| Infrastructure | Optional (peer-to-peer possible) | Requires broker |
| Wildcards | Rich (`*`, `**`, `$*`, set ops) | Basic (`+`, `#`) |
| QoS | Priority levels, congestion control, reliability | QoS 0/1/2 |
| Locality filtering | Yes (local-only, remote-only, any) | No |
| Query/storage | Native (queryable, storages) | No |
| Payload | Any bytes (`ZBytes`), encoding metadata | Any bytes |
| WAN | Native | Native |
| Embedded | zenoh-pico (pure C) | Many implementations |
| Performance | Orders of magnitude faster | Moderate |

**Basic pub/sub in Rust:**
```rust
// Subscriber
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let subscriber = session
    .declare_subscriber("sensors/temperature/**")
    .await
    .unwrap();

tokio::spawn(async move {
    while let Ok(sample) = subscriber.recv_async().await {
        println!("Received on {}: {:?}", sample.key_expr(), sample.payload());
    }
});

// Publisher
let publisher = session
    .declare_publisher("sensors/temperature/room42")
    .await
    .unwrap();
publisher.put("23.5").await.unwrap();
```

---

### Q: What is Locality filtering?

**A:** Locality filtering controls whether a publisher or subscriber interacts only with entities on the **same session** (process), only **remote** entities, or **both**.

Three values:
- `Locality::SessionLocal` — only communicate with entities in the same zenoh session (same process). Messages never go on the wire.
- `Locality::Remote` — only communicate with remote entities. Local messages are ignored.
- `Locality::Any` — communicate with both local and remote entities (default).

**Use cases:**
- `SessionLocal`: In-process communication without network overhead. Useful for decoupling components within a single application.
- `Remote`: Useful when you have a local handler that should not react to its own publications.
- `Any`: Standard behavior — widest reach.

```rust
// Subscriber that only sees remote publications (not from same session)
let subscriber = session
    .declare_subscriber("data/topic")
    .allowed_origin(Locality::Remote)
    .await
    .unwrap();

// Publisher that only publishes locally (no wire traffic)
let publisher = session
    .declare_publisher("data/topic")
    .allowed_destination(Locality::SessionLocal)
    .await
    .unwrap();
```

---

### Q: What are the priority levels and when do I use them?

**A:** Zenoh defines **8 priority levels** (from highest to lowest priority):

| Level | Name | Typical Use |
|---|---|---|
| 1 | `RealTime` | Safety-critical, hard real-time control |
| 2 | `InteractiveHigh` | High-priority interactive/UI data |
| 3 | `InteractiveLow` | Lower-priority interactive data |
| 4 | `DataHigh` | Important sensor data |
| 5 | `Data` | Standard data (default) |
| 6 | `DataLow` | Background sensor data |
| 7 | `Background` | Best-effort background transfers |

Priority affects the **scheduling order** when multiple messages are queued. Higher priority messages are dequeued and sent first. In congested conditions, lower priority messages are more likely to be dropped (with `CongestionControl::Drop`).

```rust
use zenoh::pubsub::Priority;

let publisher = session
    .declare_publisher("robot/control/velocity")
    .priority(Priority::RealTime)
    .await
    .unwrap();
```

**Guidelines:**
- Use `RealTime` / `InteractiveHigh` sparingly for truly latency-sensitive control commands.
- Use `Data` (default) for normal sensor telemetry.
- Use `Background` for bulk transfers, logs, or diagnostics that shouldn't compete with operational data.

---

### Q: What's the difference between `BestEffort` and `Reliable`?

**A:** These control **delivery guarantees** at the transport layer:

| Mode | Guarantee | Overhead | Use case |
|---|---|---|---|
| `BestEffort` | No retransmission; packet may be lost | Lowest | High-rate sensor streams, video, position updates where latest matters |
| `Reliable` | Ordered, lossless delivery (retransmission if needed) | Higher | Commands, configuration, events where every message matters |

```rust
// Currently in unstable API:
use zenoh::pubsub::Reliability;

let publisher = session
    .declare_publisher("robot/arm/position")
    .reliability(Reliability::BestEffort)  // high-rate stream, OK to drop
    .await
    .unwrap();

let publisher = session
    .declare_publisher("robot/commands")
    .reliability(Reliability::Reliable)    // commands must arrive
    .await
    .unwrap();
```

**Important**: `Reliable` does not mean *exactly-once* delivery end-to-end — it means the transport layer will attempt retransmission on lossy links. For application-level guarantees, use `zenoh-ext`'s `AdvancedPublisher`/`AdvancedSubscriber`.

---

### Q: What is `CongestionControl` and when does `Drop` vs `Block` matter?

**A:** `CongestionControl` determines what happens when a publisher produces data faster than it can be sent (i.e., the outgoing buffer is full):

| Mode | Behavior | Use case |
|---|---|---|
| `Drop` | **Discard** the message (default for most cases) | High-rate streams; latest-value more important than completeness |
| `Block` | **Block the publisher** until there is space | Slow but complete delivery; commands or critical events |

```rust
use zenoh_protocol::core::CongestionControl;

// Sensor stream: drop if congested (don't stall the publisher)
let publisher = session
    .declare_publisher("sensors/lidar/points")
    .congestion_control(CongestionControl::Drop)
    .await
    .unwrap();

// Critical event: block until delivered
let publisher = session
    .declare_publisher("robot/estop")
    .congestion_control(CongestionControl::Block)
    .await
    .unwrap();
```

**Warning**: `Block` can cause your publishing thread/task to stall indefinitely if the downstream consumer is slow or disconnected. Use it only when message completeness is more important than publisher responsiveness.

---

### Q: How do I handle backpressure?

**A:** Zenoh provides several mechanisms:

1. **`CongestionControl::Drop`** (default): The publisher drops messages when the send buffer is full. No backpressure propagated to the application — the publisher never blocks.

2. **`CongestionControl::Block`**: The publisher call blocks until buffer space is available. This propagates backpressure to the application but risks blocking indefinitely.

3. **Priority levels**: Lower-priority messages are dropped first under congestion, protecting higher-priority traffic.

4. **Subscriber channel sizing**: The default internal channel size is 256 messages (`API_DATA_RECEPTION_CHANNEL_SIZE`). If your callback is slow, consider processing in a separate task:

```rust
// Fast callback: offload heavy processing to avoid blocking the receive loop
let (tx, mut rx) = tokio::sync::mpsc::channel(1024);

let subscriber = session
    .declare_subscriber("data/**")
    .callback(move |sample| {
        let _ = tx.try_send(sample); // non-blocking; drop if full
    })
    .await
    .unwrap();

tokio::spawn(async move {
    while let Some(sample) = rx.recv().await {
        // heavy processing here
        process(sample).await;
    }
});
```

5. **`zenoh-ext` AdvancedSubscriber**: Provides more sophisticated delivery guarantees including sequence-number-based retransmission for applications requiring reliable ordered delivery.

---

## Query/Reply (Queryable)

### Q: What is a Queryable and when do I use it instead of a subscriber?

**A:** A **Queryable** is an entity that responds to queries — it's zenoh's mechanism for **request/reply** patterns and **on-demand data retrieval**.

| Use Subscriber when... | Use Queryable when... |
|---|---|
| You want a continuous stream of data as it's published | You want to serve data on demand, only when asked |
| Push model (publisher drives data flow) | Pull/query model (requester drives data flow) |
| You need the latest state delivered automatically | You need point-in-time or historical data retrieval |
| Simple event-driven processing | RPC-like interactions, storage backends |

```rust
// Queryable: listens for queries and replies
let queryable = session
    .declare_queryable("robot/config/**")
    .await
    .unwrap();

tokio::spawn(async move {
    while let Ok(query) = queryable.recv_async().await {
        println!("Query on: {} params: {}", query.key_expr(), query.parameters());
        
        // Reply with data
        query
            .reply("robot/config/max_speed", "1.5")
            .await
            .unwrap();
    }
});

// Requester: sends a query and collects replies
let replies = session.get("robot/config/**").await.unwrap();
while let Ok(reply) = replies.recv_async().await {
    if let Ok(sample) = reply.result() {
        println!("{}: {:?}", sample.key_expr(), sample.payload());
    }
}
```

**Key difference from pub/sub**: Queries are **targeted and transient** — they collect replies from all matching Queryables (and storages) that are currently alive and respond within the timeout.

---

### Q: What is `ConsolidationMode`?

**A:** When multiple Queryables (or storages) reply to the same query, you may receive multiple replies for the same key expression. `ConsolidationMode` controls how these are deduplicated:

| Mode | Behavior | Use case |
|---|---|---|
| `None` | All replies forwarded immediately as received | When you need all replies (e.g., votes, fan-out) |
| `Monotonic` | Forward a reply only if newer than any previously seen for same key | Streaming results, always-improving |
| `Latest` (default) | Buffer all replies; return only the newest per key at end | When you only care about the most recent value |
| `Auto` | `Latest` normally; `None` if time-range query | General use |

```rust
use zenoh::query::{ConsolidationMode, QueryConsolidation};

// Get only the latest value per key (default behavior)
let replies = session
    .get("sensors/**")
    .consolidation(ConsolidationMode::Latest)
    .await
    .unwrap();

// Get ALL replies (e.g., from multiple storage replicas)
let replies = session
    .get("sensors/**")
    .consolidation(ConsolidationMode::None)
    .await
    .unwrap();
```

**Note**: With `Latest`/`Monotonic`, replies are buffered until the query times out, then delivered. With `None`, replies are delivered as they arrive.

---

### Q: How does storage work with queries?

**A:** Zenoh storages are **Queryable + Subscriber** combinations. They:
1. **Subscribe** to a key expression and persist received data (in memory, InfluxDB, RocksDB, etc.)
2. **Respond to queries** on that key expression by returning stored data

Storages are implemented as **plugins** to `zenohd`. The router handles the storage lifecycle.

```json5
// DEFAULT_CONFIG.json5 — enable in-memory storage
{
  plugins: {
    storage_manager: {
      storages: {
        my_store: {
          key_expr: "sensors/**",
          volume: "memory"
        }
      }
    }
  }
}
```

Once configured:
```rust
// Any publication to sensors/** is stored automatically

// Query retrieves stored values (including historical if configured)
let replies = session.get("sensors/**").await.unwrap();
```

Supported storage backends include: Memory, InfluxDB, RocksDB, filesystem, and custom backends via the plugin API.

---

### Q: What's the difference between a `Querier` and `session.get()`?

**A:** Both issue queries, but with different trade-offs:

| | `session.get()` | `session.declare_querier()` |
|---|---|---|
| Declaration overhead | None (ad-hoc) | Declared upfront |
| Wire optimization | No key expression pre-registration | Key expression registered on declaration |
| Reuse | One-shot | Multiple `.get()` calls on same querier |
| Routing hint | None (remote routing discovers queryables on each call) | Router informed upfront; can optimize routing |

```rust
// Ad-hoc: simple, no declaration needed
let replies = session.get("robot/config/**").await.unwrap();

// Declared querier: better for repeated queries on same key
let querier = session
    .declare_querier("robot/config/**")
    .await
    .unwrap();

loop {
    let replies = querier.get().await.unwrap();
    // process replies...
    tokio::time::sleep(Duration::from_secs(1)).await;
}
```

**Rule of thumb**: Use `declare_querier` when you issue the same query repeatedly (e.g., polling). Use `session.get()` for one-off or infrequent queries.

---

## Liveliness

### Q: What is liveliness and when should I use it?

**A:** Liveliness is zenoh's built-in mechanism for **presence detection** — detecting when nodes join or leave the network. It works via **tokens**: a session declares a liveliness token on a key expression, and other sessions can subscribe to token appearances/disappearances.

```rust
// Node A: declare that it is "alive"
let session_a = zenoh::open(zenoh::Config::default()).await.unwrap();
let token = session_a
    .liveliness()
    .declare_token("robot/fleet/robot42")
    .await
    .unwrap();
// Token is alive as long as `token` is not dropped and session is open

// Node B: watch for liveliness changes
let session_b = zenoh::open(zenoh::Config::default()).await.unwrap();
let subscriber = session_b
    .liveliness()
    .declare_subscriber("robot/fleet/**")
    .history(true)  // get currently-alive tokens on subscribe
    .await
    .unwrap();

while let Ok(sample) = subscriber.recv_async().await {
    match sample.kind() {
        SampleKind::Put    => println!("Robot joined: {}", sample.key_expr()),
        SampleKind::Delete => println!("Robot left:   {}", sample.key_expr()),
    }
}
```

**When to use liveliness:**
- Fleet management (track which robots are online)
- Service discovery (detect when a service provider comes online)
- Health monitoring (detect crashes vs. clean shutdowns)
- Distributed coordination (wait for peers before starting)

---

### Q: How is liveliness different from a regular pub/sub heartbeat?

**A:**

| Aspect | Liveliness Token | Heartbeat via Pub/Sub |
|---|---|---|
| Protocol-level | Yes — built into zenoh routing | No — application-level |
| Automatic cleanup | Yes — token undeclared on session close/crash | No — must implement timeout logic |
| Bandwidth | Very low (one message on join/leave) | Continuous (e.g., every second) |
| Crash detection | Yes — detected by router when transport drops | Only after heartbeat timeout |
| False positives | None | Possible (slow network ≠ dead) |
| History | Yes (`history=true` gets current tokens) | No |

Liveliness tokens are **automatically undeclared** when the session closes (even on crash), because the router detects the transport-layer disconnection and propagates the "gone" event. A heartbeat-based system requires tuning timeout values and is prone to false alarms on slow networks.

---

### Q: How do I detect when a node leaves the network?

**A:** Subscribe to liveliness with the matching key expression and watch for `SampleKind::Delete` samples:

```rust
let liveliness_sub = session
    .liveliness()
    .declare_subscriber("myapp/nodes/**")
    .history(true)  // Receive current state on startup
    .await
    .unwrap();

while let Ok(sample) = liveliness_sub.recv_async().await {
    let node_id = sample.key_expr().to_string();
    match sample.kind() {
        SampleKind::Put => {
            println!("Node ONLINE:  {node_id}");
            // Add to active set
        }
        SampleKind::Delete => {
            println!("Node OFFLINE: {node_id}");
            // Remove from active set; trigger recovery logic
        }
    }
}
```

You can also **query** current liveliness state at any time (e.g., on startup) without waiting for events:

```rust
let replies = session
    .liveliness()
    .get("myapp/nodes/**")
    .timeout(Duration::from_secs(1))
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    if let Ok(sample) = reply.result() {
        println!("Currently alive: {}", sample.key_expr());
    }
}
```

---

## Performance

### Q: How fast is zenoh? (throughput, latency numbers)

**A:** Based on published benchmarks (2020 blog post measurements on an Intel Core i7 Linux laptop):

**Throughput:**
- **1 Gbps reached** at just **128-byte** message payloads
- Scales linearly with payload size up to network saturation

**From the 2020 benchmark:**
```
Payload size | Throughput
-------------|------------
     8 bytes | ~100 Mbps
    64 bytes | ~700 Mbps
   128 bytes | ~1 Gbps
  1024 bytes | ~1 Gbps (wire-saturated)
```

**Latency:**
- Sub-microsecond in shared-memory mode (intra-host)
- Low single-digit microseconds on loopback
- Competitive with or better than DDS implementations on LAN

**Comparison context**: These numbers significantly exceed MQTT brokers (which add broker round-trip latency of milliseconds) and are competitive with or better than DDS on equivalent hardware.

**Note**: Performance depends heavily on hardware, OS tuning, network, and configuration. Run zenoh's built-in throughput benchmarks in your environment:

```bash
# Build benchmarks
cargo build --release --examples

# Terminal 1: subscriber
./target/release/examples/z_sub_thr

# Terminal 2: publisher with 1024-byte payload
./target/release/examples/z_pub_thr 1024
```

---

### Q: When should I use shared memory?

**A:** Shared memory (SHM) transport is beneficial when:
- Publisher and subscriber are on the **same host** (same machine, different processes