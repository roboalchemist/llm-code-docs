# Zenoh Concepts Reference

## Complete Reference for Eclipse Zenoh — Pub/Sub/Query Protocol

---

## Table of Contents

1. [Session](#session)
2. [Key Expressions](#key-expressions)
3. [Selector](#selector)
4. [Publisher](#publisher)
5. [Subscriber](#subscriber)
6. [Queryable](#queryable)
7. [Query / Get](#query--get)
8. [Querier](#querier)
9. [Liveliness](#liveliness)
10. [Matching](#matching)
11. [Scouting](#scouting)
12. [WhatAmI](#whatami)
13. [Sample](#sample)
14. [SampleKind](#samplekind)
15. [ZBytes](#zbytes)
16. [Encoding](#encoding)
17. [Priority](#priority)
18. [Reliability](#reliability)
19. [CongestionControl](#congestioncontrol)
20. [Locality](#locality)
21. [Timestamp](#timestamp)
22. [Shared Memory](#shared-memory)
23. [Admin Space](#admin-space)
24. [Handlers](#handlers)
25. [Builders](#builders)

---

## Session

### What It Is

A `Session` is the primary entry point and root object in Zenoh. It represents a connection to the Zenoh network and owns all resources declared through it — publishers, subscribers, queryables, etc. All network activity flows through a session. Sessions are cheaply clonable via reference counting; the underlying connection is shared.

A session can be opened in one of three modes (see [WhatAmI](#whatami)): `client`, `peer`, or `router`. The mode determines how the session participates in the network topology.

### Lifecycle

Sessions are created via `zenoh::open()`, which returns a builder. The session remains alive as long as the returned `Session` handle is alive. When the `Session` is dropped, all declared entities are undeclared and the network connection is closed (with a default 10-second timeout for in-flight operations to complete).

Sessions can also be explicitly closed via `session.close()`, which returns a `CloseBuilder` that can be awaited. Explicit close allows waiting for all callbacks to finish (`wait_callbacks()`).

### Key Properties

- Uniquely identified by a `ZenohId` (128-bit UUID assigned at creation or from config)
- Thread-safe and cheaply cloneable (`Arc`-backed)
- Holds a `WeakSession` internally for use inside callbacks (avoids reference cycles)
- Supports both async (`.await`) and sync (`.wait()`) resolution of all operations

### Builder Pattern

```rust
// Async open with default config
let session = zenoh::open(zenoh::Config::default()).await.unwrap();

// Sync open
use zenoh::Wait;
let session = zenoh::open(zenoh::Config::default()).wait().unwrap();

// Open with custom config (router mode, TCP listener)
let mut config = zenoh::Config::default();
config.set_mode(Some(WhatAmI::Router)).unwrap();
config.listen.endpoints.push("tcp/0.0.0.0:7447".parse().unwrap());
let session = zenoh::open(config).await.unwrap();

// Explicit close
session.close().await.unwrap();

// Explicit close, waiting for all callbacks to finish
session.close().wait_callbacks().await.unwrap();

// Session info
let zid = session.info().zid().await;
let router_zids: Vec<_> = session.info().routers_zid().await.collect();
let peer_zids: Vec<_> = session.info().peers_zid().await.collect();
```

### Session Info

The `session.info()` accessor returns a `SessionInfo` handle with builders for inspecting the session's current state:

- `session.info().zid()` — own ZenohId
- `session.info().routers_zid()` — ZenohIds of connected routers
- `session.info().peers_zid()` — ZenohIds of connected peers
- `session.info().transports()` — (unstable) active transport sessions
- `session.info().links()` — (unstable) active network links

---

## Key Expressions

### What It Is

A **Key Expression** (KE) is the addressing primitive of Zenoh — analogous to a topic in pub/sub systems but far more expressive. Key expressions are slash-delimited strings of *chunks*, where each chunk is a sequence of UTF-8 characters excluding `*`, `$`, `?`, `#`, `[`, `]`. Key expressions can be concrete (identifying a single resource) or *wildcarded* (matching a set of resources).

Key expressions are the primary routing unit: publishers publish to them, subscribers declare interest in them, queryables serve them, and the Zenoh network uses them for routing decisions.

### Syntax and Wildcards

| Pattern | Meaning |
|---------|---------|
| `a/b/c` | Concrete key — matches exactly `a/b/c` |
| `a/*/c` | Single-chunk wildcard — `*` matches any single non-empty chunk. Matches `a/b/c`, `a/x/c`, but not `a/b/c/d` |
| `a/**/c` | Multi-chunk wildcard — `**` matches zero or more chunks. Matches `a/c`, `a/b/c`, `a/b/x/c` |
| `a/**` | Suffix wildcard — matches `a`, `a/b`, `a/b/c`, etc. |
| `**` | Matches everything |

Wildcards can only appear as complete chunks. `a/b*c` is **not** valid. `a/*/c` is valid.

### Canonicalization

Key expressions must be in *canonical form* before use. Zenoh automatically canonicalizes KEs created via the Rust API's `TryFrom<&str>` conversions. Canonical rules include:

- `**/**` collapses to `**`
- `**/a/**` simplifies where consecutive `**` exist
- Trailing or leading slashes are rejected

The `keyexpr::autocanonize()` function performs in-place canonicalization. The `ke!()` macro validates at compile time.

### Operations / Operators

Key expressions support set-theoretic operations:

- **Intersection** (`intersects()`): Do the two KEs have at least one common key? A subscriber interested in `a/**` intersects with a publisher on `a/b/c`.
- **Includes** (`includes()`): Does KE A fully include KE B? (Every key matched by B is also matched by A.) `a/**` includes `a/b/c`.
- **Concatenation** (`/` operator in Rust): Joins two KEs with a `/` separator.
- **Join**: Concatenation that handles `**` at boundaries correctly.

### Types

| Type | Owned? | Validated? |
|------|--------|------------|
| `KeyExpr<'a>` | Borrowed or owned | Yes |
| `OwnedKeyExpr` | Always owned | Yes |
| `&keyexpr` | Reference | Yes (compile-time with `ke!` macro) |

### Declaration (Optimization)

Declaring a key expression with the session registers it with the network, enabling numerical ID compression for wire-level efficiency:

```rust
// Ad-hoc key expression (string validated at call site)
session.put("sensors/temperature/room1", 22.5_f32).await.unwrap();

// Declared key expression (registered with session, wire-efficient)
let ke = session.declare_keyexpr("sensors/temperature/**").await.unwrap();
session.put(&ke, 22.5_f32).await.unwrap();

// Compile-time validated literal
use zenoh::key_expr::ke;
let ke = ke!("sensors/temperature/room1");

// Wildcarded
let ke = KeyExpr::try_from("sensors/*/room?").unwrap(); // error: ? not valid
let ke = KeyExpr::try_from("sensors/*/room*").unwrap(); // error: * mid-chunk
let ke = KeyExpr::try_from("sensors/**/data").unwrap(); // OK

// Set operations
let a = KeyExpr::try_from("a/**").unwrap();
let b = KeyExpr::try_from("a/b/c").unwrap();
assert!(a.intersects(&b));
assert!(a.includes(&b));
assert!(!b.includes(&a));
```

---

## Selector

### What It Is

A `Selector` extends a Key Expression with an optional query parameter string, separated by `?`. Selectors are used exclusively in the query/get subsystem. The key expression part identifies which queryables to route the query to; the parameters part is passed to the queryable for application-level filtering.

```
sensors/temperature/**?room=kitchen&value>20
^^^^^^^^^^^^^^^^^^^     ^^^^^^^^^^^^^^^^^^^^^^
    Key Expression          Parameters
```

### Parameters

Parameters form a URL-query-string-like structure: `key=value&key2=value2`. They are opaque to Zenoh routing but are passed verbatim to the matching queryable(s). The queryable interprets them at the application level.

### Special Parameters

- `_anyke`: Reserved parameter (value `""`) that, when present, instructs the network to accept replies even from queryables whose key expression does not intersect with the query's key expression. Used by the `accept_replies(ReplyKeyExpr::Any)` setting.

### Usage

```rust
// From a string — parameters follow '?'
let replies = session.get("sensors/**?room=kitchen").await.unwrap();

// From a Selector struct
use zenoh::selector::Selector;
let selector = Selector::new("sensors/**", "room=kitchen&value>20");
let replies = session.get(selector).await.unwrap();

// Parameters-only access from within a queryable handler
fn handle_query(query: Query) {
    let ke = query.key_expr();
    let params = query.parameters(); // "room=kitchen&value>20"
    let room = params.get("room");   // Some("kitchen")
}
```

---

## Publisher

### What It Is

A `Publisher` is a declared entity that publishes data (puts or deletes) on a fixed key expression. Declaring a publisher informs the network of the intent to publish, enabling route pre-computation. Publishers carry default QoS settings that apply to all publications unless overridden per-put.

The alternative to declaring a publisher is `session.put()` / `session.delete()`, which are ad-hoc and do not pre-announce routes.

### Declaration

```rust
use zenoh::qos::{CongestionControl, Priority};

let publisher = session
    .declare_publisher("sensors/temperature/room1")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Block)
    .express(true)
    .encoding(Encoding::APPLICATION_JSON)
    .allowed_destination(Locality::Any)
    .await
    .unwrap();
```

### Publishing Data

```rust
// Put (default kind = SampleKind::Put)
publisher.put("hello world").await.unwrap();

// Put with options
publisher.put(b"binary data".as_ref())
    .encoding(Encoding::APPLICATION_OCTET_STREAM)
    .timestamp(session.new_timestamp())
    .attachment(b"metadata")
    .await
    .unwrap();

// Delete (sends SampleKind::Delete)
publisher.delete().await.unwrap();

// Ad-hoc put (no pre-declared publisher)
session.put("some/key", "value")
    .priority(Priority::Interactive)
    .await
    .unwrap();
```

### Key Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `priority` | `Priority` | `Priority::Data` (4) | Message scheduling priority |
| `congestion_control` | `CongestionControl` | `Drop` | What to do when network is congested |
| `express` | `bool` | `false` | Bypass batching for low latency |
| `reliability` | `Reliability` | `Reliable` | Wire reliability hint (unstable) |
| `encoding` | `Encoding` | `ZENOH_BYTES` | Payload content type |
| `allowed_destination` | `Locality` | `Any` | Restrict to local/remote/any subscribers |

### Undeclaring

```rust
publisher.undeclare().await.unwrap();
// Or: let publisher drop out of scope
```

---

## Subscriber

### What It Is

A `Subscriber` declares interest in samples published on matching key expressions. The Zenoh network routes matching publications to all declared subscribers. Subscribers can filter by locality (session-local, remote, or any).

Subscribers receive `Sample` objects containing the key expression, payload, encoding, kind (put/delete), timestamp, QoS, and optional attachment.

### Declaration

```rust
// Default handler (FIFO channel, 256-capacity)
let subscriber = session
    .declare_subscriber("sensors/**")
    .await
    .unwrap();

// With callback
let subscriber = session
    .declare_subscriber("sensors/**")
    .callback(|sample| {
        println!("Received: {} = {:?}", sample.key_expr(), sample.payload());
    })
    .await
    .unwrap();

// With a channel handler
let subscriber = session
    .declare_subscriber("sensors/**")
    .with(flume::bounded(128))
    .await
    .unwrap();

// Receiving samples
while let Ok(sample) = subscriber.recv_async().await {
    println!("{}: {:?}", sample.key_expr(), sample.kind());
}

// With locality filter (only session-local publications)
let subscriber = session
    .declare_subscriber("sensors/**")
    .allowed_origin(Locality::SessionLocal)
    .callback(|s| println!("{}", s.key_expr()))
    .await
    .unwrap();
```

### Background Subscribers

A background subscriber runs until the session closes, without keeping a `Subscriber` handle:

```rust
session
    .declare_subscriber("sensors/**")
    .callback(|s| println!("{}", s.key_expr()))
    .background()
    .await
    .unwrap();
```

### Undeclaring

```rust
subscriber.undeclare().await.unwrap();
```

---

## Queryable

### What It Is

A `Queryable` is a declared entity that handles incoming queries (from `session.get()` or `Querier::get()`). A queryable can optionally declare itself as *complete*, meaning it claims to have all data for its key expression — routing will then favor it for matching queries.

Unlike subscribers (push model), queryables implement a **pull/request model**: data is only computed and returned in response to explicit queries.

### Declaration

```rust
let queryable = session
    .declare_queryable("sensors/**")
    .complete(true)   // claim to have complete data for this KE
    .allowed_origin(Locality::Any)
    .callback(|query| {
        println!("Query on: {} params: {}", query.key_expr(), query.parameters());
        // Reply with data
        query.reply("sensors/temperature/room1", 22.5_f32)
            .encoding(Encoding::APPLICATION_JSON)
            .await
            .unwrap();
    })
    .await
    .unwrap();

// With channel
let queryable = session
    .declare_queryable("db/**")
    .with(flume::bounded(32))
    .await
    .unwrap();

loop {
    let query = queryable.recv_async().await.unwrap();
    // Fetch data from DB...
    query.reply(query.key_expr().clone(), fetched_data).await.unwrap();
    // Multiple replies allowed
    query.reply("db/extra", extra_data).await.unwrap();
    // Error reply
    query.reply_err("not found").await.unwrap();
    // query drop = no more replies
}
```

### Replying to Queries

The `Query` object received by a queryable provides:

- `query.key_expr()` — the key expression of the query
- `query.parameters()` — the parameters string (from `?...`)
- `query.payload()` — optional payload sent with the query
- `query.encoding()` — encoding of the query payload
- `query.reply(key, payload)` — send a successful reply (builder)
- `query.reply_err(payload)` — send an error reply
- `query.reply_del(key)` — send a delete reply

Replies can be sent multiple times before the query is dropped. When the `Query` object drops, the reply channel is closed and the querier receives no more replies.

```rust
// Full reply with options
query.reply("sensors/temperature/room1", 22.5_f64)
    .encoding(Encoding::APPLICATION_JSON)
    .timestamp(uhlc_timestamp)
    .attachment(b"source=sensor42")
    .await
    .unwrap();
```

---

## Query / Get

### What It Is

`session.get()` initiates an ad-hoc query to the network. It sends a request to all queryables whose key expressions intersect with the selector's key expression, collects replies, and delivers them to a handler. This is the **pull** side of Zenoh's request-reply model.

### Basic Usage

```rust
use zenoh::query::{ConsolidationMode, QueryTarget};

let replies = session
    .get("sensors/**?room=kitchen")
    .target(QueryTarget::BestMatching)   // default
    .consolidation(ConsolidationMode::None)
    .timeout(Duration::from_secs(5))
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Got: {} = {:?}", sample.key_expr(), sample.payload()),
        Err(err)   => println!("Error: {:?}", err.payload()),
    }
}
```

### QueryTarget

Controls which queryables receive the query:

| Variant | Behavior |
|---------|---------|
| `BestMatching` | (default) Route to the *best* matching queryable — prefers complete ones |
| `All` | Route to ALL matching queryables |
| `AllComplete` | Route to all queryables that declared `complete(true)` |

### ConsolidationMode

Controls reply deduplication/merging at the network level before delivery to the application:

| Variant | Behavior |
|---------|---------|
| `None` | No consolidation — all replies delivered as received |
| `Monotonic` | Drop replies with timestamps older than already-seen for same key |
| `Latest` | Keep only the most recent reply per key expression |
| `Auto` | Let the implementation decide (usually `None` for ad-hoc, `Monotonic` for declared querier) |

### Reply and ReplyError

```rust
// Reply struct
match reply.result() {
    Ok(sample) => {
        // sample: Sample with key_expr, payload, encoding, kind, timestamp, qos
        let ke = sample.key_expr();
        let payload = sample.payload();
    }
    Err(reply_err) => {
        // reply_err: ReplyError with payload and encoding
        let err_bytes = reply_err.payload();
    }
}
```

### Sending a Query Payload

Queries can carry a payload (e.g., query parameters in structured form):

```rust
session.get("rpc/add")
    .payload(b"[1, 2]")
    .encoding(Encoding::APPLICATION_JSON)
    .await
    .unwrap();
```

### ReplyKeyExpr

By default, a get only accepts replies whose key expression intersects with the query's key expression. This can be relaxed:

```rust
session.get("sensors/**")
    .accept_replies(ReplyKeyExpr::Any)  // accept replies from any key
    .await
    .unwrap();
```

---

## Querier

### What It Is

A `Querier` is a *declared* query entity — the query-side analog of `Publisher` for pub/sub. Declaring a querier pre-announces query intent to the network, enabling route pre-computation for repeated queries to the same key expression. This is more efficient than repeated `session.get()` calls.

A querier is declared once and can issue many `get()` calls, each optionally with different parameters.

### Declaration

```rust
use zenoh::query::{ConsolidationMode, QueryTarget};

let querier = session
    .declare_querier("sensors/**")
    .target(QueryTarget::All)
    .consolidation(ConsolidationMode::None)
    .timeout(Duration::from_secs(3))
    .allowed_destination(Locality::Any)
    .accept_replies(ReplyKeyExpr::Any)
    .await
    .unwrap();
```

### Issuing Gets

```rust
// Simple get
let replies = querier.get()
    .await
    .unwrap();

// Get with parameters (appended to selector)
let replies = querier.get()
    .parameters("room=kitchen&value>20")
    .await
    .unwrap();

// Get with payload
let replies = querier.get()
    .payload(b"query body")
    .encoding(Encoding::APPLICATION_JSON)
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    println!("{:?}", reply.result());
}
```

### Ad-hoc Get vs Declared Querier

| | `session.get()` | `Querier::get()` |
|---|---|---|
| Route pre-computation | No | Yes (at declare time) |
| Target/consolidation | Per call | Set at declare, used for all gets |
| Efficiency for repeated queries | Lower | Higher |
| Use case | One-shot queries | Repeated queries to same KE |

---

## Liveliness

### What It Is

Liveliness is a first-class feature for **presence detection** — determining whether a given entity (identified by a key expression) is currently alive/connected to the Zenoh network. It is conceptually similar to "last-will" in MQTT or DDS Liveliness QoS, but works as a first-class key expression-based system.

There are three pieces:
1. **LivelinessToken** — declares "I am alive at this key expression"
2. **Liveliness Subscriber** — receives events when tokens appear/disappear
3. **Liveliness Get** — queries for currently live tokens

### LivelinessToken

```rust
// Declare a liveliness token (I am alive)
let token = session
    .liveliness()
    .declare_token("robots/robot42/status")
    .await
    .unwrap();

// Token is alive as long as `token` is not dropped/undeclared
// When dropped: SampleKind::Delete is sent to liveliness subscribers
token.undeclare().await.unwrap();
```

### Liveliness Subscriber

Receives `SampleKind::Put` when a token appears, `SampleKind::Delete` when it disappears:

```rust
let sub = session
    .liveliness()
    .declare_subscriber("robots/**")
    .history(true)   // also receive currently-live tokens on subscribe
    .await
    .unwrap();

while let Ok(sample) = sub.recv_async().await {
    match sample.kind() {
        SampleKind::Put    => println!("Online: {}", sample.key_expr()),
        SampleKind::Delete => println!("Offline: {}", sample.key_expr()),
    }
}
```

### Liveliness Get

Query for currently live tokens (one-shot presence check):

```rust
let replies = session
    .liveliness()
    .get("robots/**")
    .timeout(Duration::from_secs(2))
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    if let Ok(sample) = reply.result() {
        println!("Currently alive: {}", sample.key_expr());
    }
}
```

### Use Cases

- Robot fleet presence detection
- Service discovery (is service X available?)
- Connection health monitoring
- Distributed system membership

---

## Matching

### What It Is

Matching is a **publisher/querier awareness** feature that lets a publisher (or querier) know whether there are currently any matching subscribers (or queryables) for its key expression. This enables adaptive behavior — e.g., skipping expensive data computation when no one is listening.

Two primitives:
- **MatchingStatus** — one-shot check: are there matching subscribers right now?
- **MatchingListener** — ongoing notifications when matching status changes

### MatchingStatus

```rust
let publisher = session.declare_publisher("sensors/temperature").await.unwrap();

// One-shot check
let status = publisher.matching_status().await.unwrap();
if status.matching() {
    println!("There are subscribers — publishing data");
    publisher.put(compute_expensive_sensor_data()).await.unwrap();
} else {
    println!("No subscribers — skipping");
}
```

### MatchingListener

```rust
let listener = publisher
    .matching_listener()
    .callback(|status| {
        if status.matching() {
            println!("Subscribers appeared — start publishing");
        } else {
            println!("No more subscribers — can pause");
        }
    })
    .await
    .unwrap();

// Or with channel
let listener = publisher
    .matching_listener()
    .with(flume::bounded(16))
    .await
    .unwrap();

while let Ok(status) = listener.recv_async().await {
    println!("Matching changed: {}", status.matching());
}

listener.undeclare().await.unwrap();
```

### Querier Matching

The same API is available on `Querier` for detecting whether queryables exist:

```rust
let querier = session.declare_querier("services/**").await.unwrap();
let status = querier.matching_status().await.unwrap();
if status.matching() {
    let replies = querier.get().await.unwrap();
    // process replies
}
```

---

## Scouting

### What It Is

Scouting is the discovery mechanism used by Zenoh nodes to find each other on the network before establishing connections. `scout()` sends multicast/gossip discovery probes and collects `Hello` responses from other Zenoh nodes, each describing their `WhatAmI` role, ZenohId, and reachable locators.

Scouting is typically automatic (driven by config), but the API allows explicit scouting for custom discovery logic.

### Usage

```rust
use zenoh::scouting::WhatAmI;

// Scout for all node types
let scout = zenoh::scout(WhatAmI::Peer | WhatAmI::Router, zenoh::Config::default())
    .await
    .unwrap();

while let Ok(hello) = scout.recv_async().await {
    println!(
        "Found {:?} at {:?} (zid={})",
        hello.whatami(),
        hello.locators(),
        hello.zid()
    );
}
```

### Hello

Each `Hello` contains:
- `hello.zid()` — ZenohId of the discovered node
- `hello.whatami()` — role: Router, Peer, or Client
- `hello.locators()` — list of endpoints to connect to

### Discovery Mechanisms

Zenoh supports multiple discovery mechanisms controlled by config:

| Mechanism | Description |
|-----------|-------------|
| **Multicast** | UDP multicast on LAN (default: `udp/224.0.0.224:7446`). Fast local discovery |
| **Gossip** | Peer-to-peer gossip protocol — nodes share neighbor info. Works across subnets |
| **Static** | Explicit `connect` endpoints in config — no discovery needed |

Discovery can be combined: multicast for LAN, connect for WAN.

---

## WhatAmI

### What It Is

`WhatAmI` is an enumeration describing the **role** of a Zenoh node in the network topology. It fundamentally determines routing behavior, connection behavior, and resource usage.

### Variants

#### `Router`
A **dedicated infrastructure node**. Routers:
- Store and forward data between peers and clients
- Maintain full routing tables
- Connect to other routers to form a routing backbone
- Enable communication across network boundaries (e.g., between subnets)
- Run as standalone processes (e.g., `zenohd`)
- High resource usage; not suitable for constrained devices

```
[Client A] ─── [Router 1] ─── [Router 2] ─── [Client B]
                                    │
                               [Router 3]
                                    │
                               [Client C]
```

#### `Peer`
A **full-capability node** without centralized routing role. Peers:
- Connect directly to each other (mesh topology)
- Perform local routing between their direct neighbors
- Can operate without routers on small/trusted networks
- Suitable for LAN deployments, embedded systems with enough resources
- Discovery via multicast or gossip

```
[Peer A] ─── [Peer B]
    │              │
[Peer C] ─── [Peer D]
```

#### `Client`
A **lightweight consumer/producer** node. Clients:
- Must connect through at least one router or peer (cannot route independently)
- Minimal resource footprint — suitable for constrained devices, mobile apps
- Do not participate in discovery or routing
- Single connection point (to a router or peer)
- Ideal for IoT sensors, mobile clients, browser applications

```
[Client A] ─── [Router] ─── [Client B]
[Client C] ───/
```

### Choosing a Mode

| Scenario | Recommended Mode |
|----------|-----------------|
| Cloud/edge infrastructure node | `Router` |
| Server-class machine, LAN peer | `Peer` |
| IoT device, mobile app | `Client` |
| ROS 2 node on robot | `Peer` (or `Client` if connecting to infrastructure) |
| Bridge between networks | `Router` |

```rust
let mut config = zenoh::Config::default();
// Set mode
config.set_mode(Some(WhatAmI::Client)).unwrap();
// Connect to router
config.connect.endpoints.push("tcp/192.168.1.10:7447".parse().unwrap());
let session = zenoh::open(config).await.unwrap();
```

---

## Sample

### What It Is

A `Sample` is the core data unit received by subscribers and queryables. Every piece of data flowing through Zenoh — whether from a put, delete, or query reply — is wrapped in a `Sample`. It aggregates all metadata associated with a publication.

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `key_expr()` | `&KeyExpr` | The key expression this sample was published on |
| `payload()` | `&ZBytes` | The raw payload (zero-copy) |
| `kind()` | `SampleKind` | `Put` or `Delete` |
| `encoding()` | `&Encoding` | Content type of the payload |
| `timestamp()` | `Option<&Timestamp>` | HLC timestamp (if set) |
| `priority()` | `Priority` | QoS priority |
| `congestion_control()` | `CongestionControl` | QoS congestion control |
| `express()` | `bool` | Whether express mode was used |
| `reliability()` | `Reliability` | QoS reliability |
| `attachment()` | `Option<&ZBytes>` | Optional opaque attachment metadata |
| `source_info()` | `Option<&SourceInfo>` | Source session/sequence (unstable) |

### Usage

```rust
session.declare_subscriber("sensors/**")
    .callback(|sample| {
        println!("Key:      {}", sample.key_expr());
        println!("Kind:     {:?}", sample.kind());
        println!("Encoding: {}", sample.encoding());
        
        if let Some(ts) = sample.timestamp() {
            println!("Time: {}", ts);
        }
        
        // Deserialize payload
        let value: f64 = sample.payload().deserialize().unwrap();
        println!("Value: {}", value);
        
        if let Some(att) = sample.attachment() {
            let meta: String = att.deserialize().unwrap();
            println!("Attachment: {}", meta);
        }
    })
    .await
    .unwrap();
```

---

## SampleKind

### What It Is

`SampleKind` is a two-variant enum that classifies whether a sample represents a data publication or a deletion. It is critical for implementing distributed state — subscribers can maintain a local cache and use deletes to evict entries.

### Variants

| Variant | Wire Value | Created By | Meaning |
|---------|-----------|------------|---------|
| `Put` | `0` | `publisher.put()`, `session.put()` | Data was published/updated |
| `Delete` | `1` | `publisher.delete()`, `session.delete()` | Data was removed