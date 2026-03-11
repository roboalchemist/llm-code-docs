# Zenoh Concepts Reference

A comprehensive reference for all major concepts, types, and abstractions in the Eclipse/ZettaScale zenoh pub/sub/query protocol.

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

The `Session` is the central object in zenoh. Every interaction with the zenoh network — publishing data, subscribing to data, issuing queries, declaring entities — flows through a `Session`. It owns the network runtime, manages entity lifecycles, and routes messages.

A `Session` is created by calling `zenoh::open()`, which accepts any configuration that can be converted to `zenoh::Config`. It is backed by an async tokio runtime internally but can be used both synchronously (via `.wait()`) and asynchronously (via `.await`).

### When to Use It

You need exactly one `Session` per zenoh application. Multiple sessions per process are allowed but uncommon. Hold the `Session` for the lifetime of your application's zenoh activity; dropping it closes the session and undeclares all entities.

### Lifecycle

```
zenoh::open(config)  →  Session  →  use  →  session.close()  or  drop
```

Opening is async and may block on network initialization. Closing is also async — it tears down transports, flushes buffers, and waits for all in-flight callbacks to complete (optionally).

### Key Properties

| Property | Description |
|----------|-------------|
| `Session::zid()` | The unique `ZenohId` (128-bit UUID) of this session |
| `Session::info()` | Access `SessionInfo` for routers/peers/zid introspection |
| `Session::close()` | Returns a `CloseBuilder`; resolves to `ZResult<()>` |
| `Session::downgrade()` | Returns a `WeakSession` — does not prevent session close |
| Session is `Clone` | Cloning a `Session` clones an `Arc` handle, not the runtime |

### Builder Pattern for Open

```rust
// Async open
let session = zenoh::open(zenoh::Config::default()).await.unwrap();

// Synchronous open (blocks current thread)
use zenoh::Wait;
let session = zenoh::open(zenoh::Config::default()).wait().unwrap();

// Open with a file-based config
let session = zenoh::open(zenoh::Config::from_file("zenoh.json5")).await.unwrap();

// Open with SHM clients (requires "shared-memory" feature)
let session = zenoh::open(config)
    .with_shm_clients(shm_clients)
    .await
    .unwrap();
```

### Closing

```rust
// Graceful async close
session.close().await.unwrap();

// With callback drain (wait for all running callbacks to return)
session.close().wait_callbacks().await.unwrap();

// Implicit: dropping a Session triggers close (sync, with timeout)
drop(session);
```

### Session Info

```rust
let info = session.info();

// Own ZID
let zid: ZenohId = info.zid().await;

// Connected router ZIDs
let mut routers = info.routers_zid().await;
while let Some(rzid) = routers.next() {
    println!("Router: {}", rzid);
}

// Connected peer ZIDs
let mut peers = info.peers_zid().await;
while let Some(pzid) = peers.next() {
    println!("Peer: {}", pzid);
}
```

---

## Key Expressions

### What It Is

A **Key Expression** (KE) is zenoh's addressing scheme — a path-like string that names data resources. Key expressions can be concrete (like a filesystem path) or contain wildcards that match multiple concrete keys. Key expressions are the fundamental routing primitive: publishers declare them, subscribers filter on them, queryables register them.

### Syntax Rules

Key expressions are `/`-separated sequences of **chunks**. Each chunk is a non-empty string of unreserved characters. The special characters `*` and `$` have wildcard meaning.

| Syntax | Name | Matches |
|--------|------|---------|
| `a/b/c` | Concrete key | Exactly `a/b/c` |
| `a/*/c` | Single-chunk wildcard | Any single chunk between `a/` and `/c` — e.g., `a/x/c`, `a/foo/c` |
| `a/**/c` | Multi-chunk wildcard | Zero or more chunks between `a/` and `/c` — e.g., `a/c`, `a/x/c`, `a/x/y/c` |
| `a/**` | Suffix double-star | `a/` followed by anything |
| `**` | Universe | Every key |
| `a/$*foo` | DSL wildcard | Custom pattern (advanced) |

### Canonicalization

Key expressions must be in canonical form for routing. Zenoh performs automatic canonicalization:

- Removes trailing `/**` where not needed
- Reduces `**/**` to `**`
- Normalizes consecutive slashes

```rust
use zenoh::key_expr::KeyExpr;

// Parse and canonicalize from string
let ke: KeyExpr = "a/b/c".try_into().unwrap();

// From literal (compile-time validated via macro)
use zenoh::key_expr::keyexpr;
let ke = keyexpr!("a/b/**");

// Autocanon on session declaration
let ke = session.declare_keyexpr("a//b/../c").await.unwrap();
// Canonical: "a/c" (simplified)
```

### Operators

```rust
let ke_a: KeyExpr = "a/b/c".try_into().unwrap();
let ke_b: KeyExpr = "a/*/c".try_into().unwrap();

// Intersection: do they match any common key?
assert!(ke_a.intersects(&ke_b));

// Inclusion: does ke_b match everything ke_a matches?
assert!(ke_b.includes(&ke_a));

// Concatenation
let combined = &ke_a / &ke_b; // "a/b/c/a/*/c"

// Prefix check
assert!(ke_a.starts_with("a/b"));
```

### Declaring Key Expressions

For performance-sensitive paths, pre-declare a key expression on the session. This exchanges the string for a compact numeric wire ID:

```rust
// Declare a KE — reduces routing overhead
let declared_ke = session.declare_keyexpr("a/b/c").await.unwrap();

// Use the declared KE for publications (cheaper wire encoding)
session.put(&declared_ke, "hello").await.unwrap();
```

### Key Expression Types

| Type | Description |
|------|-------------|
| `KeyExpr<'static>` | Owned, heap-allocated |
| `KeyExpr<'a>` | Borrowed, references existing string |
| `OwnedKeyExpr` | Alias for `KeyExpr<'static>` |
| `&keyexpr` | Borrowed primitive (similar to `&str`) |

---

## Selector

### What It Is

A **Selector** extends a key expression with a query parameters string, separated by a `?`. It is used exclusively with `Session::get()` and `Querier::get()` operations to provide additional filtering or metadata to queryables.

The parameters section is a `&`-separated list of `key=value` pairs, or bare flags. The interpretation of parameters is application-defined — zenoh routes the selector but does not interpret user parameters itself.

### Syntax

```
<key_expression>[?<parameters>]

Examples:
  "temperature/sensor1"
  "temperature/**?unit=celsius"
  "telemetry/**?since=2024-01-01&limit=100"
  "key/expr?_anyke"   ← special internal parameter
```

### Special Parameters

| Parameter | Meaning |
|-----------|---------|
| `_anyke` / `_anyke=` | Accept replies on any key expression (see `ReplyKeyExpr::Any`) |

### Usage

```rust
use zenoh::selector::Selector;

// Inline string (key?params)
let replies = session.get("temp/**?unit=celsius").await.unwrap();

// Programmatic construction
let selector = Selector::try_from(("temp/**", "unit=celsius")).unwrap();
let replies = session.get(selector).await.unwrap();

// Access parameters from a Query inside a Queryable
let queryable = session.declare_queryable("temp/**").await.unwrap();
while let Ok(query) = queryable.recv_async().await {
    let params = query.parameters();        // &Parameters
    let unit = params.get("unit");          // Option<&str>
    println!("Query for unit: {:?}", unit);
}
```

### Parameters API

```rust
let params: &Parameters = query.parameters();

// Iterate key-value pairs
for (k, v) in params.iter() {
    println!("{} = {}", k, v);
}

// Get specific value
let v = params.get("key");
```

---

## Publisher

### What It Is

A **Publisher** is a declared entity that sends data (put/delete samples) on a fixed key expression. Declaring a publisher before sending data allows zenoh to optimize routing: it advertises the publication upstream so routers and subscribers can set up forwarding paths ahead of time.

You can also publish without declaring a publisher, via `session.put()` and `session.delete()` — these are ad-hoc publications.

### When to Use

Use a declared `Publisher` when:
- You publish repeatedly to the same key expression
- You want the network to set up routes in advance
- You want to monitor matching subscribers via `MatchingListener`

Use `session.put()` for infrequent or one-shot publications.

### Declaration

```rust
use zenoh::qos::{CongestionControl, Priority};

let publisher = session
    .declare_publisher("sensors/temperature")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Drop)
    .express(false)
    .allowed_destination(Locality::Any)
    .await
    .unwrap();
```

### Publishing Data

```rust
// Put (publish a value)
publisher.put("42.5°C")
    .encoding(Encoding::TEXT_PLAIN)
    .timestamp(session.new_timestamp())
    .attachment(b"metadata")
    .await
    .unwrap();

// Delete (tombstone — erase stored data)
publisher.delete().await.unwrap();

// Ad-hoc put without declared publisher
session.put("sensors/temperature", "42.5°C")
    .priority(Priority::RealTime)
    .await
    .unwrap();
```

### QoS Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `priority` | `Priority` | `Priority::Data` | 7-level message priority |
| `congestion_control` | `CongestionControl` | `Drop` | What to do when buffers are full |
| `express` | `bool` | `false` | Skip batching for lower latency |
| `reliability` | `Reliability` | `Reliable` | Best-effort vs reliable hint (unstable) |
| `allowed_destination` | `Locality` | `Any` | Restrict to local/remote/any subscribers |

### Undeclaring

```rust
// Explicit undeclare
publisher.undeclare().await.unwrap();

// Implicit: publisher undeclares on drop (default)
drop(publisher);
```

---

## Subscriber

### What It Is

A **Subscriber** receives data samples published on key expressions that intersect with the subscriber's key expression. When declared, zenoh notifies the network of interest in that key expression, enabling routers to forward matching publications.

Subscribers are push-based: data arrives asynchronously via callbacks or channels.

### Declaration

```rust
// With FIFO channel handler (default)
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

// With mutable callback (never called concurrently)
let mut count = 0;
let subscriber = session
    .declare_subscriber("sensors/**")
    .callback_mut(move |_sample| { count += 1; })
    .await
    .unwrap();

// With flume channel
let subscriber = session
    .declare_subscriber("sensors/**")
    .with(flume::bounded(256))
    .await
    .unwrap();

// Locality filtering: only receive from remote publishers
let subscriber = session
    .declare_subscriber("sensors/**")
    .allowed_origin(Locality::Remote)
    .await
    .unwrap();
```

### Receiving Samples

```rust
// From FIFO channel (default handler)
while let Ok(sample) = subscriber.recv_async().await {
    println!("{}: {:?}", sample.key_expr(), sample.payload());
}

// Synchronous receive (blocks)
while let Ok(sample) = subscriber.recv() {
    // ...
}
```

### Background Subscriber

```rust
// Background subscribers live until the session closes
// No variable needed
session
    .declare_subscriber("sensors/**")
    .callback(|sample| println!("Got: {:?}", sample))
    .background()
    .await
    .unwrap();
```

### Undeclaring

```rust
subscriber.undeclare().await.unwrap();
// or just drop — undeclares on drop by default
```

### Key Properties

| Property | Description |
|----------|-------------|
| `allowed_origin` | Filter by `Locality` (SessionLocal / Remote / Any) |
| Handler type | Controls how samples are delivered |
| `undeclare_on_drop` | Default `true`; set `false` for background mode |

---

## Queryable

### What It Is

A **Queryable** is zenoh's request-handler entity. It registers interest in a key expression and receives `Query` objects. The queryable is responsible for replying to each query with zero or more data samples (or an error). This enables the request/reply interaction pattern.

### When to Use

Use a `Queryable` when:
- You serve stored/computed data to on-demand requests
- You need the query/reply interaction pattern (RPC-style)
- You want to act as a data cache or resource server

### Declaration

```rust
let queryable = session
    .declare_queryable("data/**")
    .complete(true)   // Promises to have all data for this key expression
    .allowed_origin(Locality::Any)
    .await
    .unwrap();
```

### Completeness

The `complete` flag is an important optimization hint:

- **`complete(true)`**: This queryable promises to have the full dataset for its declared key expression. A querier with `QueryTarget::BestMatching` (the default) may stop querying other queryables when it finds a complete match.
- **`complete(false)`** (default): Partial data — queryable only has some of the matching data.

### Handling Queries

```rust
while let Ok(query) = queryable.recv_async().await {
    println!(
        "Query on: {} params: {}",
        query.key_expr(),
        query.parameters()
    );

    // Reply with a put (data)
    query
        .reply("data/foo", b"the_value")
        .encoding(Encoding::APPLICATION_JSON)
        .timestamp(session.new_timestamp())
        .await
        .unwrap();

    // Reply with a delete
    query.reply_del("data/foo").await.unwrap();

    // Reply with an error
    query
        .reply_err(b"not found")
        .encoding(Encoding::TEXT_PLAIN)
        .await
        .unwrap();

    // Query is automatically "closed" when dropped —
    // no more replies can be sent after that.
}
```

### Query Properties

```rust
let query: Query = ...;

query.key_expr()       // &KeyExpr — the requested key expression
query.selector()       // &Selector — key + parameters
query.parameters()     // &Parameters — just the query string
query.payload()        // Option<&ZBytes> — optional query payload
query.encoding()       // Option<&Encoding> — payload encoding
query.attachment()     // Option<&ZBytes> — attached metadata
```

### ReplyKeyExpr Requirement

By default, a queryable **must** reply on a key expression that intersects with the query's key expression. To reply on any key expression (including disjoint), the querier must set `accept_replies(ReplyKeyExpr::Any)`.

---

## Query / Get

### What It Is

`Session::get()` sends a query into the network matching a `Selector`. All matching `Queryable` instances receive the query and can reply. The caller collects the `Reply` stream via a handler.

This is the read/pull pattern: unlike subscribers (push), `get()` proactively fetches data.

### Basic Usage

```rust
use zenoh::query::{ConsolidationMode, QueryTarget};

let replies = session
    .get("sensors/temperature/**")
    .target(QueryTarget::BestMatching)  // default
    .consolidation(ConsolidationMode::Monotonic)
    .timeout(Duration::from_secs(5))
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!(
            "Reply: {} = {:?}",
            sample.key_expr(),
            sample.payload()
        ),
        Err(err) => println!("Error reply: {:?}", err.payload()),
    }
}
```

### Query with Payload

```rust
let replies = session
    .get("rpc/add")
    .payload(b"1+1")
    .encoding(Encoding::TEXT_PLAIN)
    .await
    .unwrap();
```

### QueryTarget

| Variant | Description |
|---------|-------------|
| `BestMatching` | Default — route to the "best" queryable(s) matching the KE. If a complete queryable fully covers the KE, stop there. |
| `All` | Route to every matching queryable, complete or not |
| `AllComplete` | Route to every complete queryable matching the KE |

### ConsolidationMode

Consolidation controls how multiple replies arriving for the same key expression are handled. Especially relevant when multiple storage queryables hold the same key.

| Mode | Description |
|------|-------------|
| `None` | All replies are delivered, no deduplication |
| `Monotonic` | Only deliver a reply if its timestamp is newer than any previously seen for that key |
| `Latest` | Buffer all replies; deliver only the newest per key when the query times out |
| `Auto` | Let zenoh pick the best strategy based on context |

```rust
use zenoh::query::{ConsolidationMode, QueryConsolidation};

// Explicit mode
.consolidation(ConsolidationMode::Latest)

// Auto (recommended when unsure)
.consolidation(QueryConsolidation::AUTO)
```

### Reply and ReplyError

```rust
let reply: Reply = ...;

match reply.result() {
    Ok(sample) => {
        // sample: &Sample
        println!("Key: {}", sample.key_expr());
        println!("Payload: {:?}", sample.payload());
    }
    Err(err) => {
        // err: &ReplyError
        println!("Error payload: {:?}", err.payload());
        println!("Error encoding: {:?}", err.encoding());
    }
}

// ReplyError fields
err.payload()    // &ZBytes
err.encoding()   // &Encoding
```

### Accept Disjoint Replies

By default, replies must intersect with the query key expression. To accept replies on any key:

```rust
use zenoh::query::ReplyKeyExpr;

let replies = session
    .get("my/query")
    .accept_replies(ReplyKeyExpr::Any)
    .await
    .unwrap();
```

---

## Querier

### What It Is

A **Querier** is the query equivalent of a `Publisher` — a pre-declared query entity that registers interest with the network for a fixed key expression. Like `Publisher` enables route setup for publications, a `Querier` enables route setup for repeated queries to the same target.

### When to Use

Use a `Querier` when:
- You repeatedly query the same key expression
- You want network routes pre-established for lower first-query latency
- You want matching listeners to detect when queryables become available

### Declaration

```rust
use zenoh::query::{ConsolidationMode, QueryTarget};

let querier = session
    .declare_querier("sensors/temperature/**")
    .target(QueryTarget::All)
    .consolidation(ConsolidationMode::None)
    .timeout(Duration::from_secs(5))
    .allowed_destination(Locality::Any)
    .await
    .unwrap();
```

### Issuing Queries

```rust
let replies = querier
    .get()
    .parameters("unit=celsius&since=2024-01-01")
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Got: {:?}", sample.payload()),
        Err(err) => println!("Error: {:?}", err.payload()),
    }
}
```

### Querier vs Ad-hoc Get

| Aspect | `session.get()` | `Querier::get()` |
|--------|-----------------|------------------|
| Route setup | Per-call | Pre-declared, amortized |
| Key expression | Specified per call | Fixed at declaration |
| Matching listener | No | Yes |
| Overhead | Higher per call | Lower per call after setup |

---

## Liveliness

### What It Is

The **Liveliness** subsystem enables **presence detection** — detecting whether a remote entity is alive (connected and active). A node declares a **LivelinessToken** on a key expression; as long as that node holds the token, it is "alive" at that key. Other nodes can subscribe to liveliness events or query for currently live tokens.

Liveliness is commonly used for service discovery, peer presence, and session health monitoring.

### Declaring a Liveliness Token

```rust
let token = session
    .liveliness()
    .declare_token("nodes/sensor_01")
    .await
    .unwrap();

// While `token` is alive, "nodes/sensor_01" is "live"
// Dropping or undeclaring the token signals absence
token.undeclare().await.unwrap();
```

### Subscribing to Liveliness Events

```rust
let sub = session
    .liveliness()
    .declare_subscriber("nodes/**")
    .history(true)  // Also receive currently alive tokens at subscribe time
    .await
    .unwrap();

while let Ok(sample) = sub.recv_async().await {
    match sample.kind() {
        SampleKind::Put    => println!("Alive:   {}", sample.key_expr()),
        SampleKind::Delete => println!("Gone:    {}", sample.key_expr()),
    }
}
```

The `history(true)` option performs a background `get` to retrieve currently live tokens, delivering them as `Put` samples before live updates.

### Querying Currently Live Tokens

```rust
let live_tokens = session
    .liveliness()
    .get("nodes/**")
    .timeout(Duration::from_secs(1))
    .await
    .unwrap();

while let Ok(reply) = live_tokens.recv_async().await {
    if let Ok(sample) = reply.result() {
        println!("Live: {}", sample.key_expr());
    }
}
```

### Liveliness Sample Semantics

| Kind | Meaning |
|------|---------|
| `SampleKind::Put` | Token appeared (entity came online) |
| `SampleKind::Delete` | Token disappeared (entity went offline or crashed) |

Liveliness `Delete` events are generated automatically by the network when the declaring session disconnects, even if the application crashes — this is the key feature distinguishing liveliness from regular subscriptions.

---

## Matching

### What It Is

The **Matching** subsystem lets a `Publisher` or `Querier` know whether there are currently any matching subscribers or queryables for its key expression. This enables adaptive behavior: a publisher can pause expensive data generation when nobody is listening.

### MatchingStatus

```rust
// Check if publisher currently has matching subscribers
let status: MatchingStatus = publisher.matching_status().await.unwrap();
if status.matching() {
    println!("Has subscribers — publishing");
} else {
    println!("No subscribers — skipping");
}
```

### MatchingListener

A `MatchingListener` delivers `MatchingStatus` events whenever the matching state changes (subscribers appear or disappear):

```rust
let listener = publisher
    .matching_listener()
    .callback(|status| {
        if status.matching() {
            println!("Subscriber appeared");
        } else {
            println!("No more subscribers");
        }
    })
    .await
    .unwrap();

// Background variant (no variable needed)
publisher
    .matching_listener()
    .callback(|status| { /* ... */ })
    .background()
    .await
    .unwrap();
```

### Querier Matching

```rust
// Querier can also detect matching queryables
let listener = querier
    .matching_listener()
    .callback(|status| {
        if status.matching() {
            println!("Queryable available");
        }
    })
    .await
    .unwrap();
```

### MatchingStatusType

Internally, matching tracks:
- **Subscribers** for publishers
- **Queryables** for queriers

The type is selected automatically based on the entity the listener is attached to.

---

## Scouting

### What It Is

**Scouting** is zenoh's peer-discovery mechanism. Before or without opening a `Session`, you can scout the network for other zenoh nodes matching a `WhatAmIMatcher` (a bitmask filter on node types). Scouting sends `Hello` messages over multicast (and/or gossip) and collects responses.

### When to Use

- Dynamic discovery of zenoh infrastructure (routers, peers)
- Network topology inspection
- Pre-connection verification that a router exists

### Basic Scouting

```rust
use zenoh::config::WhatAmI;

let scout = zenoh::scout(
    WhatAmI::Peer | WhatAmI::Router,
    zenoh::Config::default()
)
.await
.unwrap();

// Collect hellos until timeout or done
while let Ok(hello) = scout.recv_async().await {
    println!(
        "Found: zid={} whatami={:?} locators={:?}",
        hello.zid(),
        hello.whatami(),
        hello.locators()
    );
}

// Scouting stops when Scout is dropped
drop(scout);
```

### Hello Message

```rust
let hello: Hello = ...;

hello.zid()       // ZenohId — unique node identifier
hello.whatami()   // WhatAmI — Router / Peer / Client
hello.locators()  // &[Locator] — network addresses (TCP, UDP, etc.)
```

### Scout Builder

```rust
// With callback
zenoh::scout(WhatAmI::Router, zenoh::Config::default())
    .callback(|hello| println!("Found router: {}", hello.zid()))
    .await
    .unwrap();

// With channel
let receiver = zenoh::scout(WhatAmI::Peer | WhatAmI::Router, config)
    .with(flume::bounded(32))
    .await
    .unwrap();
```

### Discovery Mechanisms

Zenoh supports two discovery transports, configured in the config:

| Mechanism | Description |
|-----------|-------------|
| **Multicast** | UDP multicast `224.0.0.224:7447` — works on local network segments |
| **Gossip** | Peer-to-peer gossip propagation — works across subnets via connected peers |

---

## WhatAmI

### What It Is

`WhatAmI` describes the **operational mode** of a zenoh node. It determines routing behavior, connection topology, and resource usage. Every session declares one `WhatAmI` in its configuration.

### Variants

#### Router

```
WhatAmI::Router
```

- A full-featured routing node
- Maintains complete routing tables for all connected peers and clients
- Stores and forwards subscriptions and queryable registrations
- Suitable for infrastructure nodes (always-on, high-resource)
- Accepts connections from peers and clients
- Participates in multicast discovery

#### Peer

```
WhatAmI::Peer
```

- A peer-to-peer node
- Maintains routing tables for its direct neighbors
- Can connect to routers and other peers
- Routing coverage limited to its directly connected graph
- Suitable for resource-constrained edge devices that still want P2P capability
- Participates in multicast/gossip discovery

#### Client

```
WhatAmI::Client
```

- Minimal resource usage
- Depends entirely on a connected router for routing and discovery
- No routing table maintenance
- Cannot directly connect to other clients
- Must connect to at least one router (or peer acting as proxy)
- Suitable for constrained devices, mobile applications, short-lived processes

### Choosing a Mode

| Scenario | Mode |
|----------|------|
| Infrastructure daemon (always-on server) | Router |
| Edge device with P2P requirements | Peer |
| Mobile app, IoT sensor, CLI tool | Client |
| Plugin inside a zenoh router | Peer or Router (shares runtime) |

### Configuration

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/router.example.com:7447"]
  }
}
```

```rust
let mut config = zenoh::Config::default();
config.set_mode(Some(WhatAmI::Client)).unwrap();
config.connect.endpoints.set(
    vec!["tcp/192.168.1.100:7447".parse().unwrap()]
).unwrap();
let session = zenoh::open(config).await.unwrap();
```

---

## Sample

### What It Is

A `Sample` is the fundamental data unit in zenoh — it represents a single piece of data received by a subscriber or returned by a query. Every `Sample` carries the key it was published on, the payload, and rich metadata.

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `key_expr` | `KeyExpr<'static>` | The concrete key this sample was published on |
| `payload` | `ZBytes` | The raw data payload |
| `kind` | `SampleKind` | `Put` or `Delete` |
| `encoding` | `Encoding` | Content type of the payload |
| `timestamp` | `Option<Timestamp>` | HLC-based timestamp (if set) |
| `qos` | `QoS` | Quality of service metadata |
| `attachment` | `Option<ZBytes>` | Optional user-defined attachment |
| `source_info` | `Option<SourceInfo>` | Original publisher info (unstable) |
| `reliability` | `Reliability` | Best-effort or reliable hint (unstable) |

### Accessing Sample Data

```rust
fn handle_sample(sample: Sample) {
    println!("Key:       {}", sample.key_expr());
    println!("Payload:   {:?}", sample.payload());
    println!("Kind:      {:?}", sample.kind());
    println!("Encoding:  {}", sample.encoding());

    if let Some(ts) = sample.timestamp() {
        println!("Timestamp: {:?}", ts);
    }

    if let Some(att) = sample.attachment() {
        