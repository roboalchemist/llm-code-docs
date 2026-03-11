# Zenoh Comprehensive FAQ

---

## Getting Started

---

**Q: What is zenoh and how does it compare to MQTT/DDS/Kafka/ROS2?**

Zenoh (pronounced *"zeno"*) is an open-source, unified data-in-motion and data-at-rest protocol that blends pub/sub, geo-distributed storage, queries, and computations into a single stack. The tagline is "Zero Overhead Pub/Sub, Store/Query and Compute."

Unlike single-paradigm protocols, zenoh natively handles:
- **Pub/Sub** (like MQTT or DDS)
- **Queryable/Get** (like a distributed key-value store or REST)
- **Storages** (geo-distributed, queryable data at rest)
- **Liveliness** (presence detection without heartbeat polling)

| Feature | MQTT | DDS | Kafka | Zenoh |
|---|---|---|---|---|
| Broker required | Yes (mandatory) | No (multicast) | Yes (mandatory) | No (optional) |
| Peer-to-peer | No | Yes (LAN) | No | Yes (LAN + WAN) |
| Query/Reply | No | Limited | Consumer API | Native first-class |
| WAN / internet | With bridges | Hard | Yes | Yes (native) |
| Embedded support | Yes (lite) | Partial | No | Yes (zenoh-pico, ~100KB) |
| Data at rest | No | No | Yes | Yes (pluggable backends) |
| Language support | Many | Many | Many | Rust, C, C++, Python, Java, Kotlin, TypeScript |

**vs MQTT:** MQTT requires a broker and uses a simple topic string model with limited QoS. Zenoh supports brokerless peer-to-peer, richer wildcard key expressions, native query/reply, and is significantly faster for high-throughput scenarios.

**vs DDS:** DDS is powerful but complex (IDL, XML configuration, multicast-heavy). Zenoh achieves similar or better performance with a dramatically simpler API and natural WAN traversal.

**vs Kafka:** Kafka is designed for persistent log streaming with consumer groups. Zenoh targets low-latency real-time messaging with optional storage, not high-volume log archival.

**vs ROS2:** ROS2 uses DDS under the hood. Zenoh can replace DDS as the ROS2 transport layer (via `rmw_zenoh`) and extends naturally beyond a single robot to multi-robot fleets, cloud connectivity, and IoT.

---

**Q: How do I install zenoh?**

**Rust (primary implementation):**
```bash
# Install Rust toolchain (>= 1.75.0)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Add zenoh to your Cargo.toml
[dependencies]
zenoh = "1.5.1"
```

**Zenoh router (zenohd):**
```bash
# Build from source
git clone https://github.com/eclipse-zenoh/zenoh.git
cd zenoh
cargo build --release
./target/release/zenohd

# Or download a pre-built release from:
# https://github.com/eclipse-zenoh/zenoh/releases
```

**Other languages:**
- **C/C++**: [zenoh-c](https://github.com/eclipse-zenoh/zenoh-c) or [zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico)
- **Python**: `pip install eclipse-zenoh`
- **Java/Kotlin**: Maven/Gradle packages at [zenoh-java](https://github.com/eclipse-zenoh/zenoh-java) / [zenoh-kotlin](https://github.com/eclipse-zenoh/zenoh-kotlin)

See [zenoh.io/docs/getting-started/installation/](https://zenoh.io/docs/getting-started/installation/) for platform-specific instructions.

---

**Q: What programming languages does zenoh support?**

| Language | Repository | Notes |
|---|---|---|
| **Rust** | `eclipse-zenoh/zenoh` | Primary/reference implementation |
| **C** | `eclipse-zenoh/zenoh-c` | Rust binding; same API as zenoh-pico |
| **C** (pure) | `eclipse-zenoh/zenoh-pico` | Pure C for embedded/microcontrollers |
| **C++** | `eclipse-zenoh/zenoh-cpp` | C++ wrapper over zenoh-c or zenoh-pico |
| **Python** | `eclipse-zenoh/zenoh-python` | Python bindings |
| **Java** | `eclipse-zenoh/zenoh-java` | JVM |
| **Kotlin** | `eclipse-zenoh/zenoh-kotlin` | JVM / Android |
| **TypeScript** | `eclipse-zenoh/zenoh-ts` | WebSocket client via zenohd plugin |

All non-Rust bindings wrap the Rust core library (except zenoh-pico), so behavior is consistent across languages.

---

**Q: Do I need a broker/server to use zenoh?**

**No.** Zenoh can operate completely broker-free in **peer mode**, where nodes discover each other via multicast scouting and communicate directly. This is one of zenoh's key differentiators from MQTT (which mandates a broker).

However, you can optionally run a **zenoh router** (`zenohd`) when you need:
- WAN/internet connectivity (NAT traversal)
- Bridging isolated network segments
- Persistent storage plugins
- Centralized access control
- Routing between peers that cannot directly reach each other

**Quick rule of thumb:**
- Single machine or local LAN with multicast → no router needed
- Multiple sites, cloud, internet, or complex topologies → use a router

---

**Q: What's the difference between zenoh router, peer, and client mode?**

Zenoh has three node **whatami** modes, set in configuration:

| Mode | Routing | Discovery | Use Case |
|---|---|---|---|
| **Router** | Full routing tables | Multicast + unicast | Infrastructure node (`zenohd`) |
| **Peer** | Participates in routing | Multicast scouting | Application nodes that also route for others |
| **Client** | None (offloads to router) | Unicast to known router | Resource-constrained devices, IoT, mobile |

**Router:** Runs as `zenohd`. Maintains full routing state, connects multiple network segments, hosts plugins (storage, REST API, etc.).

**Peer:** An application node that both communicates *and* routes data for other peers. Peers can form mesh networks and discover each other via multicast. Two peers on the same LAN can communicate without any router.

**Client:** A lightweight node that connects to a router (or peer acting as a router) and delegates all routing. Ideal for embedded devices, mobile apps, or nodes behind NAT.

```json5
// Example config snippet
{
  mode: "peer",           // or "router" or "client"
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"]  // for client mode
  }
}
```

---

## Key Expressions and Selectors

---

**Q: What is a key expression?**

A key expression is zenoh's addressing mechanism — similar to a topic in MQTT or a subject in NATS, but more powerful. It is a hierarchical path composed of `/`-separated chunks (called **chunks**).

```
robot/arm/joint1/position
sensors/temperature/room42
```

Key expressions can be:
1. **Concrete** — an exact resource name: `robot/arm/joint1`
2. **Wildcarded** — using `*`, `**`, or `$*` to match multiple resources

Key expressions are validated at compile/declaration time. Declaring a key expression with `session.declare_keyexpr()` registers it with the network for wire-level compression (numeric IDs instead of strings).

```rust
// Declare a key expression for repeated use (optimized on wire)
let ke = session.declare_keyexpr("robot/arm/**").await?;

// Or use inline strings (slightly less efficient but simpler)
let publisher = session.declare_publisher("robot/arm/joint1").await?;
```

---

**Q: How do wildcards work? (`*`, `**`, `$*`)**

| Wildcard | Matches | Example |
|---|---|---|
| `*` | Any single non-empty chunk (no `/`) | `robot/*/position` matches `robot/arm/position` but NOT `robot/arm/elbow/position` |
| `**` | Any sequence of chunks, including zero chunks | `robot/**/position` matches `robot/position`, `robot/arm/position`, `robot/arm/elbow/position` |
| `$*` | A **DSL suffix** within a single chunk — matches any suffix of a chunk | `robot/arm$*` matches `robot/arm`, `robot/arm1`, `robot/arm_left` |

**Important rules:**
- `*` never crosses a `/` boundary
- `**` can appear as a standalone chunk: `a/**/b` or as part of an expression
- `**` at the end matches everything under a prefix: `sensors/**`

```
# Examples
"a/*/c"   matches "a/b/c" ✓  but NOT "a/b/d/c" ✗
"a/**/c"  matches "a/c" ✓, "a/b/c" ✓, "a/b/d/c" ✓
"a/**"    matches "a/" ✓, "a/b" ✓, "a/b/c/d" ✓
```

---

**Q: What's the difference between `*` and `**`?**

`*` matches exactly **one chunk** (the part between two `/` separators).
`**` matches **zero or more chunks** including their separators.

```
Expression: sensor/*/value
Matches:    sensor/temp/value    ✓
            sensor/humidity/value ✓
Does NOT:   sensor/room1/temp/value ✗  (two chunks between sensor and value)

Expression: sensor/**/value
Matches:    sensor/value         ✓  (zero chunks)
            sensor/temp/value    ✓  (one chunk)
            sensor/room1/temp/value ✓  (two chunks)
```

Use `*` when you know there is exactly one level of hierarchy between your anchors. Use `**` when the depth is variable or unknown.

---

**Q: What is a Selector?**

A `Selector` extends a key expression with an optional **parameter string** separated by `?`. It is used exclusively with `session.get()` and queryables.

```
key/expression?param1=value1&param2=value2
```

The key expression part routes the query to matching queryables. The parameter string is passed to the queryable as-is — its meaning is defined by the application. Common built-in uses include:

- **Time range queries** on storages: `sensor/temp?_time=[2024-01-01T00:00:00Z/now]`
- **Filtering**: `robot/state?status=active`

```rust
// Using a selector with parameters
let replies = session
    .get("sensor/temperature?_time=[now(-1h)/now]")
    .await?;
```

---

**Q: How do key expression operators work?**

Zenoh key expressions support set operations for advanced matching:

- **Union** (`|`): `a/b|c/d` — matches resources matching either `a/b` or `c/d`
- **Intersection** (`&`): matches resources in the intersection of two key expression sets (less commonly used directly in APIs)
- **Negation / complement**: used internally in routing optimizations

In practice, most users work with wildcards (`*`, `**`) rather than explicit set operators. The operators are most relevant when building routing logic or advanced storage plugins.

```
"robot/arm|robot/leg"  // matches robot/arm OR robot/leg
```

---

## Pub/Sub

---

**Q: How does pub/sub differ from traditional MQTT?**

| Aspect | MQTT | Zenoh |
|---|---|---|
| Broker | Required | Optional |
| Wildcards | `+` (one level), `#` (multi) | `*`, `**`, `$*` (richer) |
| QoS levels | 0, 1, 2 (at-most-once, at-least-once, exactly-once) | Priority levels + BestEffort/Reliable |
| Query/Reply | None | Native (Queryable) |
| Retained messages | Yes (last value) | Via storage plugins |
| Peer-to-peer | No | Yes |
| WAN | With broker | Native |
| Performance | Moderate | Significantly higher |

```rust
// Publisher
let session = zenoh::open(zenoh::Config::default()).await?;
let publisher = session
    .declare_publisher("robot/arm/joint1")
    .await?;
publisher.put("42.5").await?;

// Subscriber
let subscriber = session
    .declare_subscriber("robot/arm/**")
    .await?;
while let Ok(sample) = subscriber.recv_async().await {
    println!("Key: {}, Value: {:?}", sample.key_expr(), sample.payload());
}
```

---

**Q: What is Locality filtering?**

Locality (called `origin` for subscribers, `destination` for publishers) filters whether messages are routed locally, remotely, or both.

| `Locality` | Behavior |
|---|---|
| `Locality::Any` | Default — send/receive both local (same session) and remote |
| `Locality::SessionLocal` | Only route within the same session (no network traffic) |
| `Locality::Remote` | Only route to/from remote nodes (skip local callbacks) |

**Use cases:**
- `SessionLocal`: inter-task communication within one process with zero network overhead
- `Remote`: a publisher that should not trigger its own co-located subscribers
- `Any`: standard behavior

```rust
// Only receive from remote publishers (not same session)
let subscriber = session
    .declare_subscriber("sensor/data")
    .allowed_origin(Locality::Remote)
    .await?;

// Only publish to remote subscribers
let publisher = session
    .declare_publisher("sensor/data")
    .allowed_destination(Locality::Remote)
    .await?;
```

---

**Q: What are the priority levels and when do I use them?**

Zenoh defines 8 priority levels (lower number = higher priority). From the source, `Priority::DEFAULT` is used unless overridden.

| Priority | Numeric | Use Case |
|---|---|---|
| `RealTime` | 1 | Safety-critical, control loops, emergency stop |
| `InteractiveHigh` | 2 | User-facing interactive commands |
| `InteractiveLow` | 3 | Interactive but delay-tolerant |
| `DataHigh` | 4 | High-value sensor data |
| `Data` | 5 | **Default** — general data |
| `DataLow` | 6 | Background telemetry |
| `Background` | 7 | Bulk transfers, logs |

Priority affects message scheduling in the router's transmit queue. Higher priority messages are sent first when the queue is contested.

```rust
use zenoh::pubsub::Priority;

let publisher = session
    .declare_publisher("robot/emergency_stop")
    .priority(Priority::RealTime)
    .await?;
```

---

**Q: What's the difference between `BestEffort` and `Reliable`?**

`Reliability` controls the delivery guarantee on a per-publisher basis.

| Mode | Guarantee | Overhead |
|---|---|---|
| `BestEffort` | No retransmission, may be dropped | Lower latency, lower CPU |
| `Reliable` | Ordered, loss-detected delivery | Slight overhead for sequencing |

**When to use each:**
- `BestEffort`: Video streams, high-frequency sensor data (100 Hz+), telemetry where a dropped sample is acceptable
- `Reliable`: Commands, configuration updates, state changes where every message matters

> **Note:** As of zenoh 1.x, the `reliability` field on publishers is under the `unstable` feature flag. The default behavior provides reliable delivery over TCP transports.

```rust
#[cfg(feature = "unstable")]
use zenoh::qos::Reliability;

let publisher = session
    .declare_publisher("sensor/imu")
    .reliability(Reliability::BestEffort)
    .await?;
```

---

**Q: What is `CongestionControl` and when does `Drop` vs `Block` matter?**

`CongestionControl` determines what happens when the transmit buffer is full:

| Mode | Behavior | Use Case |
|---|---|---|
| `Drop` | **Default** — discard the message if the queue is full | High-frequency streams, telemetry |
| `Block` | Block the caller until space is available | Commands that must not be lost |

**Practical guidance:**
- Use `Drop` for sensor streams (100+ Hz). If one sample is lost, the next will arrive shortly. Blocking a 100 Hz publisher for even 10 ms causes severe jitter.
- Use `Block` for important infrequent messages (robot commands, configuration) where losing the message is unacceptable and you can tolerate the sender blocking briefly.

```rust
use zenoh::qos::CongestionControl;

// High-frequency sensor — drop if congested
let sensor_pub = session
    .declare_publisher("sensor/lidar")
    .congestion_control(CongestionControl::Drop)
    .await?;

// Command — never drop, block if needed
let cmd_pub = session
    .declare_publisher("robot/command")
    .congestion_control(CongestionControl::Block)
    .await?;
```

---

**Q: How do I handle backpressure?**

Zenoh provides several mechanisms:

1. **`CongestionControl::Block`** — naturally applies backpressure to the publisher by blocking `put()` until the network can accept the message.

2. **`CongestionControl::Drop`** — the publisher never blocks; messages are silently dropped. Monitor drop rates via the admin space (`@/router/local/subscriber/**`).

3. **Priority queuing** — assign lower priority to less critical publishers so high-priority messages are never starved.

4. **Shared Memory (SHM)** — for intra-host pub/sub, SHM eliminates copy overhead and effectively removes the serialization bottleneck that often causes backpressure.

5. **Application-level flow control** — use `session.get()` (request/reply) instead of pub/sub when you need explicit acknowledgement before sending the next message.

```rust
// Pattern: send-and-wait for acknowledgement (no backpressure buildup)
let querier = session.declare_querier("robot/arm/move").await?;
let replies = querier.get().payload("goto_home").await?;
while let Ok(reply) = replies.recv_async().await {
    // process ack
}
```

---

## Query/Reply (Queryable)

---

**Q: What is a Queryable and when do I use it instead of a subscriber?**

A `Queryable` is an entity that listens for queries and replies with data. Think of it as a server-side handler for pull-based communication.

**Use a Subscriber when:**
- Data is pushed continuously and you want all samples as they arrive
- You don't need to ask "what is the current state?" — you maintain state from the stream

**Use a Queryable when:**
- You provide on-demand data (current state, computed results, database queries)
- You want request/reply semantics (one request → one or more responses)
- You need to return data to late-joining nodes that missed pub/sub messages
- You're implementing a service (like ROS2 services but more flexible)

```rust
// Queryable — acts like a server
let queryable = session
    .declare_queryable("robot/status")
    .await?;

tokio::spawn(async move {
    while let Ok(query) = queryable.recv_async().await {
        println!("Query from: {}, params: {}", query.key_expr(), query.parameters());
        query
            .reply("robot/status", "online")
            .await
            .unwrap();
    }
});

// Client — queries the server
let replies = session.get("robot/status").await?;
while let Ok(reply) = replies.recv_async().await {
    println!("Status: {:?}", reply.result());
}
```

---

**Q: What is `ConsolidationMode`?**

`ConsolidationMode` controls how multiple replies for the same key expression are merged before being delivered to the application.

| Mode | Behavior |
|---|---|
| `None` | All replies delivered immediately as received |
| `Monotonic` | For each key, only deliver replies with increasing timestamps (filter outdated) |
| `Latest` *(default)* | For each key, only deliver the single most recent reply after all replies arrive |
| `Auto` | Use `Latest` normally; use `None` if a time-range parameter is present |

**When to use each:**
- `None`: You want every reply from every storage, even duplicates or older versions. Use for debugging or when you need the full picture.
- `Monotonic`: Streaming results where you want progressively newer data without waiting.
- `Latest`: You want exactly one "current" answer per key — ideal for getting current state.
- `Auto`: Good default for general use.

```rust
use zenoh::query::ConsolidationMode;

let replies = session
    .get("sensor/temperature/**")
    .consolidation(ConsolidationMode::Latest)
    .await?;
```

---

**Q: How does storage work with queries?**

Zenoh supports pluggable storage backends (memory, InfluxDB, RocksDB, etc.) that:
1. **Subscribe** to a key expression and store incoming publications
2. **Register a Queryable** on the same key expression to serve stored data

When you `session.get("sensor/**")`, the query is routed to all matching queryables — including storage queryables — which reply with their stored data.

Storage plugins run inside `zenohd` and are configured in the router config:

```json5
// zenohd config with in-memory storage
{
  plugins: {
    storage_manager: {
      storages: {
        sensor_storage: {
          key_expr: "sensor/**",
          volume: { id: "memory" }
        }
      }
    }
  }
}
```

Available backends: Memory, InfluxDB, RocksDB, S3, MySQL, PostgreSQL, SQLite.

---

**Q: What's the difference between a `Querier` and `session.get()`?**

Both send queries, but they differ in lifecycle and optimization:

| | `session.get()` | `session.declare_querier()` |
|---|---|---|
| Lifecycle | One-shot, creates/destroys per call | Declared once, reused many times |
| Network efficiency | Announces interest each time | Pre-announces interest, allows routers to optimize routing tables |
| Use case | Occasional queries | Frequent queries to the same key expression |

`session.get()` is a convenience shortcut. `Querier` is more efficient when you query the same key expression repeatedly because the router can pre-compute routes.

```rust
// One-shot (simpler)
let replies = session.get("sensor/temperature").await?;

// Reusable querier (more efficient for repeated queries)
let querier = session
    .declare_querier("sensor/temperature")
    .await?;
// Query many times efficiently
for _ in 0..100 {
    let replies = querier.get().await?;
    // ...
}
```

---

## Liveliness

---

**Q: What is liveliness and when should I use it?**

Liveliness is a built-in mechanism to declare that an entity is "alive" and to detect when it goes away. It uses **tokens** — lightweight presence markers attached to key expressions.

**Use cases:**
- Service discovery: "Is robot_arm_1 online?"
- Fleet management: detect when a robot disconnects
- Health monitoring without implementing custom heartbeats
- Gate functionality: only subscribe to data if the publisher is alive

```rust
// Node declares it is alive
let token = session
    .liveliness()
    .declare_token("robot/fleet/robot_001")
    .await?;
// Token is alive as long as this variable lives.
// When dropped (or session closes), a "death" event is emitted.

// Observer watches for presence/absence
let subscriber = session
    .liveliness()
    .declare_subscriber("robot/fleet/**")
    .history(true)  // get current state of all tokens on subscribe
    .await?;

while let Ok(sample) = subscriber.recv_async().await {
    match sample.kind() {
        SampleKind::Put => println!("{} came online", sample.key_expr()),
        SampleKind::Delete => println!("{} went offline", sample.key_expr()),
    }
}
```

---

**Q: How is liveliness different from a regular pub/sub heartbeat?**

| Aspect | Heartbeat (pub/sub) | Zenoh Liveliness |
|---|---|---|
| Implementation | You write it | Built-in, zero application code |
| False positives | Possible (missed heartbeat ≠ dead) | Session-level: token disappears exactly when session closes or is dropped |
| Latency to detect failure | ≥ heartbeat interval | Near-immediate (transport-level detection) |
| Bandwidth | Periodic messages | Zero bandwidth while alive; single event on death |
| History | Requires retained/last-value storage | `history(true)` gives current snapshot on subscribe |

Liveliness is more reliable because it is tied directly to the transport session lifecycle — if the process crashes, the network connection drops, or the session is explicitly closed, the token disappears and subscribers are notified without waiting for a missed heartbeat.

---

**Q: How do I detect when a node leaves the network?**

Use a liveliness subscriber with `history(true)` to get both current state and future changes:

```rust
let liveliness_sub = session
    .liveliness()
    .declare_subscriber("robot/fleet/**")
    .history(true)  // receive current tokens immediately on subscribe
    .await?;

while let Ok(sample) = liveliness_sub.recv_async().await {
    match sample.kind() {
        SampleKind::Put => {
            println!("Node JOINED: {}", sample.key_expr());
        }
        SampleKind::Delete => {
            println!("Node LEFT: {}", sample.key_expr());
            // Trigger failover, alert, cleanup, etc.
        }
    }
}
```

You can also query current liveness state once without subscribing:

```rust
let replies = session
    .liveliness()
    .get("robot/fleet/**")
    .await?;
// Each reply represents a currently-alive token
```

---

## Performance

---

**Q: How fast is zenoh? (throughput and latency numbers)**

Published benchmark results (from blog posts, circa 2020 on a Linux laptop with Intel Core i7):

- **Throughput**: Reaches **1 Gbps** with message payloads of just **128 bytes**
- At larger payloads, throughput scales to saturate 10 GbE links
- **Latency**: Sub-100 microsecond end-to-end latency on localhost; low single-digit milliseconds on LAN

In comparisons with other middleware:
- Zenoh significantly outperforms MQTT in both throughput and latency
- Zenoh matches or exceeds DDS performance while using less CPU
- Over shared memory (same host), zenoh achieves near-zero-copy performance approaching memory bandwidth limits

> **Note:** Performance depends heavily on transport (TCP, UDP, shared memory), hardware, payload size, and configuration. Always benchmark for your specific use case.

The repository includes dedicated throughput and latency benchmark examples:
```bash
# Run throughput benchmark
cargo run --example z_sub_thr --release
cargo run --example z_pub_thr --release 1024  # 1024-byte payload
```

---

**Q: When should I use shared memory (SHM)?**

Use shared memory when:
- Publisher and subscriber are on the **same physical machine** (different processes)
- Payload is **large** (images, point clouds, video frames — typically > 64 KB)
- You need **zero-copy** semantics (the subscriber gets a pointer into the SHM buffer, no copy occurs)

SHM is **not useful** for:
- Cross-machine communication (data must be serialized for the network anyway)
- Small messages (SHM setup overhead outweighs the copy savings)

**Enabling SHM:**
```toml
# Cargo.toml
zenoh = { version = "1.5.1", features = ["shared-memory"] }
```

```json5
// Config: enable SHM transport
{
  transport: {
    shared_memory: { enabled: true }
  }
}
```

The session exposes `session.get_shm_provider()` (unstable API) for accessing the SHM provider for custom zero-copy publishing.

---

**Q: How does zenoh compare to DDS performance?**

Zenoh consistently matches or beats DDS (FastDDS, CycloneDDS) in benchmarks:

- **Lower latency** for peer-to-peer on LAN (no multicast-based discovery overhead)
- **Higher throughput** especially for many-to-many scenarios
- **Lower CPU** usage due to simpler protocol encoding
- **Better WAN performance** since DDS is not designed for WAN and requires bridges

For ROS2 specifically, `rmw_zenoh` (Zenoh RMW) has demonstrated lower latency than `rmw_fastrtps` and `rmw_cyclonedds` in controlled tests, particularly at higher message rates and larger payload sizes.

---

**Q: What configuration settings improve performance?**

Key settings to tune (in the zenoh JSON5 config):

```json5
{
  transport: {
    unicast: {
      // Increase buffer sizes for high-throughput
      lowlatency: false,      // set true to reduce batching latency (trades throughput)
    },
    // Enable SHM for same-host communication
    shared_memory: { enabled: true }
  },
  // Disable timestamping if not needed (saves ~100ns per message)
  timestamping: { enabled: false },
  
  // Tune QoS
  qos: {
    publication: [
      {
        key_exprs: ["sensor/lidar/**"],
        congestion_control: "Drop",
        priority: "DataHigh"
      }
    ]
  }
}
```

**General tips:**
1. Use `Priority::RealTime` for latency-sensitive topics
2. Use `CongestionControl::Drop` for high-frequency streams
3. Enable SHM for intra-host large-payload pub/sub
4. Use `declare_keyexpr()` for key expressions used repeatedly — reduces wire overhead
5. Use `Publisher` objects (declared once) rather than `session.put()` for repeated publications
6. Set `is_express: true` on publishers to skip batching for lowest latency (trades throughput)

---

## Deployment

---

**Q: When do I need a zenoh router vs just peers?**

**Peers only (no router) is sufficient when:**
- All nodes are on the same LAN with multicast available
- The network is a simple clique (everyone can reach everyone)
- You don't need persistent storage or access control plugins

**You need a zenoh router (`zenohd`) when:**
- Connecting across different networks or the internet (WAN)
- Nodes are behind NAT or firewall
- You need storage plugins (InfluxDB, memory, etc.)
- You want centralized REST API access (`zenoh-plugin-rest`)
- You need access control / security policies
- Network topology is complex (hub-and-spoke, hierarchical)
- Multicast is unavailable or disabled

---

**Q: How does peer discovery work?**

Zenoh uses a **scouting** protocol for automatic peer discovery:

1. **Multicast scouting** (default on LAN): Nodes send multicast "Hello" messages on `239.255.0.1:7446`. Other nodes on the same multicast domain respond and establish connections automatically.

2. **Unicast scouting**: For environments without multicast, specify known endpoints in config. Starting from one known peer, zenoh discovers the "closure" — all peers reachable directly or indirectly.

```json5
// Explicit connect for client mode or when multicast is unavailable
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.10:7447"]
  }
}

// Disable multicast scouting (for controlled environments)
{
  scouting: {
    multicast: { enabled: false },
    gossip: { enabled: true }  // use gossip-based discovery instead
  }
}
```

---

**Q: Can zenoh work over the internet (WAN)?**

Yes. WAN connectivity is a first-class zenoh feature, unlike DDS which is primarily L