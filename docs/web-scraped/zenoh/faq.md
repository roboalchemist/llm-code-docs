# Zenoh Comprehensive FAQ

---

## Getting Started

### Q: What is zenoh and how does it compare to MQTT/DDS/Kafka/ROS2?

**A:** Zenoh (pronounced *"zeno"*) is an open-source, zero-overhead pub/sub, store/query, and compute middleware. It unifies **data in motion**, **data at rest**, and **computations** in a single protocol designed for extreme performance and flexibility across the full compute continuum — from microcontrollers to cloud.

| Feature | zenoh | MQTT | DDS | Kafka |
|---|---|---|---|---|
| Broker required | Optional | Yes (broker) | No (but discovery heavy) | Yes (broker cluster) |
| Peer-to-peer | Yes | No | Yes | No |
| WAN-native | Yes | Limited | Poor | Limited |
| Embedded support | Yes (zenoh-pico) | Yes | Limited | No |
| Query/storage | Built-in | No | Limited | Consumer groups |
| Wildcard routing | Rich (`*`, `**`) | Limited (`+`, `#`) | Topic-based | No |
| Latency | Sub-microsecond (SHM) | ms range | Low | ms–s range |

**vs MQTT:** MQTT requires a central broker and has weak wildcard semantics. Zenoh can act as a drop-in MQTT replacement (via the MQTT plugin) while adding peer-to-peer, queries, and geo-distributed storage. Zenoh also has no concept of QoS levels 0/1/2 mapped to protocol overhead — it uses fine-grained priority and reliability settings.

**vs DDS:** DDS has notoriously heavy discovery traffic (multicast floods), poor WAN support, and complex configuration. Zenoh achieves similar or better performance with dramatically simpler deployment and a fraction of the discovery traffic. The ROS 2 zenoh plugin is a transparent replacement.

**vs Kafka:** Kafka is a log-based streaming platform built around brokers and consumer groups. Zenoh is a general-purpose protocol stack that includes queryable geo-distributed storage — you can get Kafka-like retention behavior via the storage plugin, but with peer-to-peer capability and microcontroller support.

**vs ROS 2 (DDS):** ROS 2's default DDS-based communication struggles at scale, across WANs, and with resource-constrained devices. The zenoh-plugin-ros2dds bridges ROS 2 transparently, dramatically reducing discovery overhead and enabling cross-internet robot communication.

---

### Q: How do I install zenoh?

**A:**

**Rust library** (add to `Cargo.toml`):
```toml
[dependencies]
zenoh = "1.5.1"

# Optional: shared memory support
zenoh = { version = "1.5.1", features = ["shared-memory"] }
```

**Zenoh router (zenohd)**:
```bash
# Build from source
git clone https://github.com/eclipse-zenoh/zenoh.git
cd zenoh
cargo build --release
./target/release/zenohd

# Or download pre-built binaries from GitHub Releases
```

**Other languages** — install the respective package:
- Python: `pip install eclipse-zenoh`
- C/C++: Download from [zenoh-c](https://github.com/eclipse-zenoh/zenoh-c) releases
- Embedded: See [zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico)

**Quick test** (requires Rust):
```bash
# Terminal 1 — subscriber
cargo run --example z_sub

# Terminal 2 — publisher
cargo run --example z_pub
```

---

### Q: What programming languages does zenoh support?

**A:** Zenoh supports the following languages:

| Language | Repository | Notes |
|---|---|---|
| **Rust** | `eclipse-zenoh/zenoh` | Primary/reference implementation |
| **C** | `eclipse-zenoh/zenoh-c` | Rust binding |
| **C** (pure) | `eclipse-zenoh/zenoh-pico` | Pure C for embedded |
| **C++** | `eclipse-zenoh/zenoh-cpp` | Wrapper over zenoh-c |
| **Python** | `eclipse-zenoh/zenoh-python` | Rust binding |
| **Kotlin** | `eclipse-zenoh/zenoh-kotlin` | |
| **Java** | `eclipse-zenoh/zenoh-java` | |
| **TypeScript** | `eclipse-zenoh/zenoh-ts` | WebSocket client |

All language bindings (except zenoh-pico) wrap the Rust core and share the same wire protocol, so they interoperate transparently.

---

### Q: Do I need a broker/server to use zenoh?

**A:** No. Zenoh is designed to work **without any infrastructure** in peer mode. Peers discover each other via multicast scouting and communicate directly.

You *optionally* add a **zenoh router** (`zenohd`) when you need:
- WAN connectivity (peers that can't reach each other directly)
- Centralized storage/queryables
- Bridging between network segments
- Client mode support for resource-constrained devices

```rust
// Zero infrastructure — works out of the box
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
session.put("my/key", "hello").await.unwrap();
```

---

### Q: What's the difference between zenoh router, peer, and client mode?

**A:** Zenoh has three node kinds, configurable via `mode` in the config:

| Mode | Routing | Discovery | Use case |
|---|---|---|---|
| **Router** | Full routing for others | Announces itself | Infrastructure node (`zenohd`) |
| **Peer** | Routes for itself + neighbors | Multicast scouting | Typical application node |
| **Client** | No routing, depends on router | Connects to router | Resource-constrained, behind NAT |

```json5
// Config to set mode
{
  mode: "peer",       // or "router" or "client"
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"]  // connect to router (for client mode)
  }
}
```

**Key rule of thumb:**
- Local LAN with capable devices → use **peer** mode, no router needed
- Across internet / firewalls → use **client** mode connecting to a **router**
- Hosting a relay/bridge → deploy a **router**

---

## Key Expressions and Selectors

### Q: What is a key expression?

**A:** A key expression (KE) is zenoh's addressing mechanism — analogous to a topic in MQTT/DDS, but more powerful. It's a UTF-8 string composed of path-like segments separated by `/`.

```
sensors/robot1/temperature
home/living-room/lights
a/b/c
```

Key expressions can be **canonical** (no wildcards) or **wild** (containing wildcards). They are validated at compile/parse time — invalid KEs are rejected before reaching the network.

```rust
// Declare a key expression once for efficiency
let key = session.declare_keyexpr("sensors/robot1/temp").await?;
session.put(&key, 42.0f64).await?;
```

Declaring a KE with `declare_keyexpr` tells zenoh to cache the string→ID mapping, saving bandwidth on repeated use.

---

### Q: How do wildcards work? (`*`, `**`, `$*`)

**A:** Zenoh supports three wildcard types:

| Wildcard | Matches | Example |
|---|---|---|
| `*` | Any single chunk (no `/`) | `sensors/*/temp` matches `sensors/robot1/temp` |
| `**` | Any sequence of chunks (including `/`) | `sensors/**/temp` matches `sensors/floor1/room2/temp` |
| `$*` | DSL: zero or more characters within a chunk | `sensor$*` matches `sensor`, `sensor1`, `sensor_imu` |

```rust
// Subscribe to all robot temperatures
let sub = session.declare_subscriber("sensors/*/temperature").await?;

// Subscribe to everything under sensors/
let sub = session.declare_subscriber("sensors/**").await?;

// Mix both
let sub = session.declare_subscriber("robots/**/cmd_vel").await?;
```

**Matching semantics:** A subscriber on `a/*/c` receives publications to `a/b/c` but NOT `a/b/d/c`. Use `a/**/c` to match any depth.

---

### Q: What's the difference between `*` and `**`?

**A:**

- `*` matches **exactly one path segment** (no slashes)
- `**` matches **zero or more path segments** (can span slashes)

```
Key expression: sensors/*/temp
Matches:        sensors/robot1/temp    ✓
Does NOT match: sensors/floor1/robot1/temp  ✗

Key expression: sensors/**/temp
Matches:        sensors/temp           ✓  (zero segments)
                sensors/robot1/temp    ✓  (one segment)
                sensors/floor1/robot1/temp ✓ (two segments)
```

Use `*` when the hierarchy depth is fixed; use `**` when you want to match at any depth.

---

### Q: What is a Selector?

**A:** A Selector is a key expression with an optional **parameter string** appended after `?`. It extends a key expression for use with queries (`get()`).

```
sensors/robot1/temp?start=1h&end=now
my/storage/**?encoding=json
```

The part before `?` is the key expression; the part after is the **parameters string** (URL-query-style). Queryables receive both parts and can use parameters for filtering, time ranges, etc.

```rust
// Query with parameters
let replies = session.get("sensors/**?start=2024-01-01").await?;

// In a queryable handler:
while let Ok(query) = queryable.recv_async().await {
    println!("Key: {}", query.key_expr());
    println!("Params: {}", query.parameters());
    query.reply("sensors/robot1/temp", 42.0f64).await?;
}
```

---

### Q: How do key expression operators work?

**A:** Zenoh provides set-theoretic operators on key expressions (available via the API):

- **Intersection** (`ke1.intersects(ke2)`): true if the two KEs match at least one common key
- **Includes** (`ke1.includes(ke2)`): true if every key matched by `ke2` is also matched by `ke1`

```rust
use zenoh::key_expr::KeyExpr;

let a: KeyExpr = "sensors/**".try_into()?;
let b: KeyExpr = "sensors/robot1/temp".try_into()?;

assert!(a.intersects(&b));  // true
assert!(a.includes(&b));    // true — a is a superset
assert!(!b.includes(&a));   // false — b doesn't include a
```

These are used internally for routing decisions and are also useful for application-level filtering logic.

---

## Pub/Sub

### Q: How does pub/sub differ from traditional MQTT?

**A:** Key differences:

| Aspect | MQTT | Zenoh |
|---|---|---|
| Broker | Required, central | Optional |
| Wildcards | `+` (single), `#` (multi) | `*`, `**`, `$*` |
| QoS | 3 levels (0/1/2) | Priority (8 levels) + Reliability + CongestionControl |
| Locality | Always via broker | Can filter local vs remote |
| Query/Reply | Not built-in | First-class (`get()` / Queryable) |
| Retained messages | Yes (last value) | Via storage queryable |
| Payload | Bytes | Typed `ZBytes` with serialization helpers |

```rust
// Publisher
let publisher = session.declare_publisher("sensors/temp")
    .priority(Priority::RealTime)
    .reliability(Reliability::BestEffort)
    .await?;
publisher.put(42.0f64).await?;

// Subscriber
let subscriber = session.declare_subscriber("sensors/**").await?;
while let Ok(sample) = subscriber.recv_async().await {
    println!("{}: {:?}", sample.key_expr(), sample.payload());
}
```

---

### Q: What is Locality filtering?

**A:** Locality lets you control whether messages are routed to session-local entities only, remote entities only, or both.

```rust
use zenoh::sample::Locality;

// Only deliver to subscribers in the same session process
let publisher = session.declare_publisher("my/key")
    .allowed_destination(Locality::SessionLocal)
    .await?;

// Only receive from remote publishers (ignore same-session)
let subscriber = session.declare_subscriber("my/key")
    .allowed_origin(Locality::Remote)
    .await?;

// Default: Any (both local and remote)
```

**Use cases:**
- `SessionLocal`: In-process message passing (zero-copy, no network overhead)
- `Remote`: Avoid processing your own publications (echo suppression)
- `Any`: Standard behavior (default)

---

### Q: What are the priority levels and when do I use them?

**A:** Zenoh has **8 priority levels** (lower number = higher priority):

```rust
pub enum Priority {
    RealTime        = 1,  // Highest — control-critical data
    InteractiveHigh = 2,
    InteractiveLow  = 3,
    DataHigh        = 4,
    Data            = 5,  // Default
    DataLow         = 6,
    Background      = 7,
    Background2     = 8,  // Lowest — bulk transfers
}
```

Priority affects the order messages are scheduled in the zenoh transmit queues. Higher-priority messages jump ahead of lower-priority ones.

```rust
// Safety-critical control
let publisher = session.declare_publisher("robot/emergency_stop")
    .priority(Priority::RealTime)
    .await?;

// Telemetry logs — low priority
let publisher = session.declare_publisher("robot/logs")
    .priority(Priority::Background)
    .await?;
```

---

### Q: What's the difference between BestEffort and Reliable?

**A:**

| Mode | Delivery guarantee | Ordering | Overhead |
|---|---|---|---|
| `BestEffort` | No — packets may be dropped | Not guaranteed | Minimal |
| `Reliable` | Yes — retransmission on loss | Ordered | Higher |

```rust
use zenoh::qos::Reliability;

// High-frequency sensor data — occasional drop is OK
let pub = session.declare_publisher("sensors/lidar")
    .reliability(Reliability::BestEffort)
    .await?;

// Commands that must arrive
let pub = session.declare_publisher("robot/cmd")
    .reliability(Reliability::Reliable)
    .await?;
```

**Rule of thumb:**
- Use `BestEffort` for high-frequency telemetry where the next sample makes stale ones irrelevant (IMU, lidar scans, video)
- Use `Reliable` for commands, configuration updates, or any data where loss is unacceptable

> **Note:** As of zenoh 1.x, `Reliability` on the publisher is marked `unstable` in the API; it's being stabilized.

---

### Q: What is CongestionControl and when does Drop vs Block matter?

**A:** `CongestionControl` determines what happens when a publication cannot be sent immediately (e.g., the network or internal queue is saturated):

| Mode | Behavior | Use when |
|---|---|---|
| `Drop` | Message is silently discarded | Real-time sensors — freshness matters more than delivery |
| `Block` | Publisher blocks until queue drains | Commands — delivery matters more than latency |

```rust
use zenoh::qos::CongestionControl;

// Sensor stream — drop old data under congestion
let pub = session.declare_publisher("sensors/camera")
    .congestion_control(CongestionControl::Drop)
    .await?;

// Critical command — block until sent
let pub = session.declare_publisher("robot/cmd")
    .congestion_control(CongestionControl::Block)
    .await?;
```

---

### Q: How do I handle backpressure?

**A:** Backpressure in zenoh is handled via `CongestionControl`:

1. **Drop** (default for most cases): Fast publishers are never blocked; old messages are dropped if the receiver or network can't keep up. This is appropriate for streaming sensor data.

2. **Block**: The `put()` call will block (async await) until the message is queued. This provides natural backpressure to the publisher.

3. **Subscriber-side**: The default subscriber uses a bounded channel (`API_DATA_RECEPTION_CHANNEL_SIZE = 256`). If your callback is slow, consider using a separate processing thread or async task, or increasing the channel size in config.

```rust
// For slow consumers: process in separate task
let sub = session.declare_subscriber("heavy/data").await?;
tokio::spawn(async move {
    while let Ok(sample) = sub.recv_async().await {
        // process asynchronously
        process(sample).await;
    }
});
```

---

## Query/Reply (Queryable)

### Q: What is a Queryable and when do I use it instead of a subscriber?

**A:** A `Queryable` responds to **on-demand requests** rather than continuous streams. Think of it as a function-as-a-resource: callers ask for data, the queryable computes and replies.

| Use subscriber when... | Use queryable when... |
|---|---|
| Data is pushed continuously | Data is requested on demand |
| Fire-and-forget semantics | Request-reply semantics |
| Streaming telemetry | "What is the current state?" |
| No response needed | Caller waits for answer |

```rust
// Queryable — acts like a server
let queryable = session.declare_queryable("robot/status").await?;
tokio::spawn(async move {
    while let Ok(query) = queryable.recv_async().await {
        let status = get_robot_status();  // compute response
        query.reply("robot/status", status).await.unwrap();
    }
});

// Caller — get() sends a query and collects replies
let replies = session.get("robot/status").await?;
while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Status: {:?}", sample.payload()),
        Err(e) => println!("Error: {:?}", e),
    }
}
```

Queryables are also used to front **storage backends** — queries to a key expression are answered with historical data.

---

### Q: What is ConsolidationMode?

**A:** When a `get()` query is sent, multiple queryables (on different nodes) may reply. `ConsolidationMode` controls how the session handles **duplicate or conflicting replies** for the same key:

| Mode | Behavior |
|---|---|
| `Auto` | Default: `Latest` normally; `None` if time range in parameters |
| `None` | Forward every reply immediately as received |
| `Monotonic` | Forward a reply only if it has a newer timestamp than any previously seen reply for the same key |
| `Latest` | Collect all replies; deliver only the latest (by timestamp) per key at the end |

```rust
use zenoh::query::ConsolidationMode;

// Get latest value only (deduplicated)
let replies = session.get("sensors/**")
    .consolidation(ConsolidationMode::Latest)
    .await?;

// Get all replies (e.g., for audit/history)
let replies = session.get("sensors/**")
    .consolidation(ConsolidationMode::None)
    .await?;
```

---

### Q: How does storage work with queries?

**A:** Zenoh has a **storage subsystem** built into the router via plugins. When a storage is configured for a key expression:

1. It subscribes to matching publications and persists them
2. It declares a queryable for that key expression
3. When `get()` is called, it replies with stored data

```json5
// zenohd config — in-memory storage
{
  plugins: {
    storage_manager: {
      storages: {
        my_store: {
          key_expr: "sensors/**",
          volume: { id: "memory" }
        }
      }
    }
  }
}
```

External backends (InfluxDB, RocksDB, MySQL, etc.) plug in as volume providers. This enables time-series queries, last-value caching, and geo-distributed eventually-consistent storage.

---

### Q: What's the difference between a Querier and `session.get()`?

**A:** `session.get()` is a **one-shot query** — convenient for occasional requests. A `Querier` is a **pre-declared, reusable query handle** optimized for repeated queries to the same key expression.

```rust
// One-shot (simple, but re-negotiates routing each time)
let replies = session.get("sensors/robot1/**").await?;

// Querier (declares intent once, optimized for repeated queries)
let querier = session.declare_querier("sensors/robot1/**").await?;
loop {
    let replies = querier.get().await?;
    // process replies...
    tokio::time::sleep(Duration::from_secs(1)).await;
}
```

The `Querier` also receives routing information about matching queryables as they appear/disappear (similar to how a `Publisher` tracks subscribers), enabling smarter routing decisions.

---

## Liveliness

### Q: What is liveliness and when should I use it?

**A:** Liveliness is a first-class zenoh mechanism for tracking **whether a session/entity is alive**. A node declares a **liveliness token** on a key expression; other nodes subscribe to liveliness events to detect presence/absence.

```rust
// Node A — declare that it's alive
let token = session.liveliness()
    .declare_token("robot/robot1/alive")
    .await?;
// token is alive while in scope; dropping it signals departure

// Node B — watch for nodes coming and going
let sub = session.liveliness()
    .declare_subscriber("robot/*/alive")
    .await?;
while let Ok(sample) = sub.recv_async().await {
    match sample.kind() {
        SampleKind::Put => println!("{} came online", sample.key_expr()),
        SampleKind::Delete => println!("{} went offline", sample.key_expr()),
    }
}

// Node C — query current live nodes
let replies = session.liveliness()
    .get("robot/**")
    .await?;
```

**Use cases:** service discovery, fleet presence tracking, health monitoring, graceful vs. crash detection.

---

### Q: How is liveliness different from a regular pub/sub heartbeat?

**A:**

| Aspect | Heartbeat (pub/sub) | Liveliness token |
|---|---|---|
| Implementation | App-level periodic publish | Protocol-level mechanism |
| Crash detection | Only after missed heartbeats | Immediate on session close/crash |
| Bandwidth | Continuous traffic | Event-driven only |
| History | No | Query current state anytime |
| Timeout config | App-managed | Protocol-managed |

A heartbeat requires your application to continuously publish, set up timers, and handle timeouts. Liveliness tokens are **automatically undeclared** when a session closes (cleanly or by crash), and subscribers receive a `Delete` sample immediately — no timer needed.

---

### Q: How do I detect when a node leaves the network?

**A:** Subscribe to liveliness events on the node's token key expression. When the node disconnects (gracefully or crashes), zenoh automatically sends a `Delete` sample to all liveliness subscribers:

```rust
let sub = session.liveliness()
    .declare_subscriber("fleet/**")
    .history(true)  // also get currently-alive nodes on subscribe
    .await?;

while let Ok(sample) = sub.recv_async().await {
    match sample.kind() {
        SampleKind::Put => {
            println!("Node joined: {}", sample.key_expr());
        }
        SampleKind::Delete => {
            println!("Node left (or crashed): {}", sample.key_expr());
            // trigger failover, alerting, etc.
        }
    }
}
```

The `history(true)` flag means you'll receive `Put` events for all **currently alive** tokens when you first subscribe.

---

## Performance

### Q: How fast is zenoh? (throughput, latency numbers)

**A:** Based on ZettaScale benchmarks (Linux, Intel Core i7, intra-machine):

| Scenario | Performance |
|---|---|
| Throughput (128-byte messages) | >1 Gbps network saturation |
| Throughput (large messages) | Near line rate |
| Latency (shared memory) | Sub-microsecond |
| Latency (loopback UDP) | Low single-digit microseconds |

From the 2020 benchmark blog post: "The 1 Gbps mark is reached already for messages with a payload of just 128 bytes" on commodity laptop hardware.

A comparative study from National Taiwan University showed zenoh outperforming MQTT, Kafka, and DDS across throughput and latency metrics.

**Latency hierarchy** (best to worst):
1. `SessionLocal` + shared memory → sub-µs
2. Loopback (same machine, UDP/TCP) → µs
3. LAN (GigE) → ~10-50 µs typical
4. WAN → network RTT dominated

---

### Q: When should I use shared memory?

**A:** Use shared memory (SHM) when:
- Publisher and subscriber are on the **same machine**
- Payloads are **large** (images, point clouds, sensor arrays)
- You need **zero-copy** delivery

Enable it in `Cargo.toml`:
```toml
zenoh = { version = "1.5.1", features = ["shared-memory"] }
```

And in config:
```json5
{
  transport: {
    shared_memory: { enabled: true },
    unicast: {
      qos: { enabled: true }
    }
  }
}
```

With SHM, the payload is written once into a shared memory region; the subscriber gets a pointer — no copy, minimal latency. Zenoh automatically negotiates SHM capability with connected peers; if SHM is not available, it falls back to normal transport transparently.

---

### Q: How does zenoh compare to DDS performance?

**A:** In ROS 2 benchmarks and production usage, zenoh shows improvements over DDS in several areas:

- **Discovery traffic**: DDS floods the network with multicast SPDP/SEDP advertisements. Zenoh's scouting is far lighter, especially with many participants.
- **WAN latency**: DDS is fundamentally designed for LAN; zenoh routes over TCP/TLS natively.
- **Scalability**: DDS discovery overhead grows with participant count; zenoh's router-based routing scales better.
- **Large-payload throughput**: Comparable on LAN; zenoh wins on heterogeneous networks.

Specifically for ROS 2 scenarios: field reports show significantly reduced bandwidth utilization (especially discovery bandwidth), better behavior on WiFi, and the ability to span robots across different network segments trivially.

---

### Q: What configuration settings improve performance?

**A:**

```json5
{
  transport: {
    unicast: {
      // Enable QoS for priority scheduling
      qos: { enabled: true },
      // Larger buffers for high-throughput
      lowlatency: false
    },
    shared_memory: {
      enabled: true  // For same-machine communication
    }
  },
  // Tune internal channel sizes (larger = more buffering, less drops)
  // Set via environment variables:
  // ZENOH_API_DATA_RECEPTION_CHANNEL_SIZE=1024
}
```

**Performance tips:**
1. Enable **QoS** to use priority scheduling
2. Use **shared memory** for intra-machine large payloads
3. Use `BestEffort` reliability for high-frequency sensor streams
4. Pre-declare key expressions with `declare_keyexpr()` for repeated use
5. Declare a `Publisher` object rather than using `session.put()` in hot loops
6. Use `is_express(true)` on a publisher to bypass the priority queue (ultra-low latency at the cost of QoS guarantees)

---

## Deployment

### Q: When do I need a zenoh router vs just peers?

**A:**

**Peers only (no router needed):**
- All nodes on the same LAN with multicast available
- Small number of nodes (< ~20)
- No WAN connectivity required
- No persistent storage needed

**Add a router when:**
- Nodes span different subnets/VLANs where multicast is blocked
- Any node is behind NAT or a firewall
- You need WAN connectivity (internet)
- You want persistent storage (storage plugin)
- You have clients (embedded/mobile) that can't run in peer mode
- You need bridging to other protocols (MQTT, DDS, REST)

```bash
# Start a router
zenohd --config my_router_config.json5

# Client connects to router
# In client config:
# { mode: "client", connect: { endpoints: ["tcp/router_ip:7447"] } }
```

---

### Q: How does peer discovery work?

**A:** Zenoh uses **scouting** for automatic discovery:

1. **Multicast scouting** (default on LAN): Peers send "Scout" messages to the multicast group `224.0.0.224:7446`. Peers that hear the scout reply with their connection info.

2. **Unicast scouting**: For environments without multicast, configure explicit endpoints to scout:
```json5
{
  scouting: {
    multicast: { enabled: false },
    gossip: { enabled: true }
  },
  connect: {
    endpoints: ["tcp/known_peer:7447"]
  }
}
```

3. **Closure-based discovery**: From a single known peer, zenoh can discover the full reachable set (the "closure") by following neighbor advertisements.

---

### Q: Can zenoh work over the internet (WAN)?

**A:** Yes — WAN connectivity is a first-class zenoh use case. Unlike DDS (which is LAN-only), zenoh was designed to span the full network topology.

**Setup:**
1. Deploy a zenoh router on a public IP (cloud VM, VPS)
2. Configure peers/clients to connect to it

```json5
// Cloud router config
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447", "tls/0.0.0.0:7448"]
  }
}

// Field robot config
{
  mode: "client",
  connect: {
    endpoints: ["tcp/my-cloud-router.example.com:7447"]
  }
}
```

**Transport options:** TCP, TLS (encrypted), QUIC, WebSocket, UDP. TLS and QUIC are recommended for WAN deployments.

---

### Q: How do I connect multiple sites?

**A:** Deploy a router at each site and connect the routers:

```
Site A                  Site B
[peers] → [routerA] ←→ [routerB] ← [peers]
               ↕
          [cloud router]
               ↕
          [Site C peers]
```

```json5
// Router A config — connects to Router B
{
  mode: "router",
  listen: { endpoints: ["tcp/0.0.0.0:7447"] },
  connect: { endpoints: ["tcp/router-b.example.com:7447"] }
}
```

Zenoh's region-based routing ensures that routing table size scales with the **region** size, not the global network size — making multi-site deployments practical even with many participants.

---

## ROS 2

### Q: How do I bridge ROS 2 topics over zenoh?

**A:** Use the `zenoh-plugin-ros2dds` (also available as `zenoh-bridge-ros2dds` standalone binary):

```bash
# Install
cargo install zenoh-bridge-ros2dds

# Run alongside your ROS 2 nodes (no code changes needed)
zenoh-bridge-ros2dds

# With custom config (e.g., connect to remote router)
zenoh-bridge-ros2dds --config bridge_config.json5
```

The bridge automatically discovers all ROS 2 topics, services, and actions via DDS and exposes them on zenoh under the namespace `<ros_namespace>/<topic_name>`. Remote bridges subscribe/publish transparently, so ROS 2 nodes see no difference.

```
Robot A (ROS 2 + bridge) ←→ [zenoh network] ←→ (ROS 2 + bridge) Robot B
```

---

### Q: Does the bridge support services