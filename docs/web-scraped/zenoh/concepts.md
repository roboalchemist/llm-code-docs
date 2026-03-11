# Zenoh Concepts Reference

> **Comprehensive reference documentation for Eclipse Zenoh — the unified pub/sub/query/storage protocol for edge, fog, and cloud. Based on the Zenoh 1.x Rust API.**

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

A `Session` is the root object in Zenoh — the gateway to the network. Every operation (publish, subscribe, query, etc.) flows through a session. Sessions manage:

- Network connections to routers or peers
- Resource declarations (publishers, subscribers, queryables, etc.)
- A unique **ZenohId** (128-bit UUID) identifying this participant
- The local routing table and all internal state

A session is relatively heavyweight: you should create one per process (or one per logical subsystem in advanced deployments), not one per message.

### Lifecycle

Sessions are opened asynchronously with `zenoh::open()` and closed explicitly or on drop. Closing is graceful: the session sends un-declaration messages, allowing peers to clean up subscriptions. The close builder supports a configurable timeout (default 10 seconds).

```rust
// Open a session with default config
let session = zenoh::open(zenoh::Config::default()).await?;

// Access session metadata
let zid = session.info().zid().await;                    // Own ZenohId
let routers = session.info().routers_zid().await;        // Connected routers
let peers   = session.info().peers_zid().await;          // Connected peers

// Explicit close (graceful, waits up to 10s)
session.close().await?;

// Close and wait for all callbacks to finish
session.close().wait_callbacks().await?;
```

### Configuration

The `Config` object controls:

- **Mode**: `router`, `peer`, or `client` (see [WhatAmI](#whatami))
- **Endpoints**: list of `locator` strings (`tcp/192.168.1.1:7447`, `udp/...`, `tls/...`, etc.)
- **Scouting**: multicast group, gossip settings
- **QoS overrides**: per-key-expression defaults for priority, congestion control, etc.
- **Access control**: ACL rules
- **Shared memory**: SHM configuration

```rust
// From a JSON5 config file
let config = zenoh::Config::from_file("zenoh.json5")?;

// Programmatic config
let mut config = zenoh::Config::default();
config.set_mode(Some(WhatAmI::Client))?;
config.connect.endpoints.set(vec!["tcp/192.168.1.100:7447".parse()?])?;

let session = zenoh::open(config).await?;
```

### Builder Pattern

`zenoh::open()` returns an `OpenBuilder` that resolves to `ZResult<Session>`. All Zenoh builders implement both `.await` (async) and `.wait()` (sync):

```rust
// Async
let session = zenoh::open(config).await?;

// Sync (blocks current thread)
let session = zenoh::open(config).wait()?;
```

### WeakSession

Internal subsystems (admin space, publishers stored in state) hold a `WeakSession` — a non-owning reference that does not prevent the session from being dropped. User code always holds the strong `Session`.

### Key Properties

| Property | Description |
|---|---|
| `session.info().zid()` | Own 128-bit ZenohId |
| `session.info().routers_zid()` | ZenohIds of connected routers |
| `session.info().peers_zid()` | ZenohIds of connected peers |
| `session.declare_publisher(ke)` | Declare a publisher |
| `session.declare_subscriber(ke)` | Declare a subscriber |
| `session.declare_queryable(ke)` | Declare a queryable |
| `session.declare_querier(ke)` | Declare a querier |
| `session.get(selector)` | Ad-hoc query |
| `session.put(ke, payload)` | Ad-hoc publish |
| `session.delete(ke)` | Ad-hoc delete |
| `session.liveliness()` | Liveliness subsystem |

---

## Key Expressions

### What They Are

Key Expressions (KEs) are the addressing primitive in Zenoh — the equivalent of topics in pub/sub or resource paths in REST. Every piece of data is associated with a key expression, and routing decisions are made by matching key expressions.

A key expression is a UTF-8 string composed of **chunks** separated by `/`. Each chunk is a sequence of characters that may include wildcards.

### Syntax Rules

```
key_expr  ::= chunk ('/' chunk)*
chunk     ::= non-empty string of printable characters (no '/')
            | '*'       -- single-chunk wildcard
            | '**'      -- multi-chunk wildcard (only at chunk boundaries)
```

**Valid examples:**
```
robot/arm/joint1
sensors/temperature
fleet/*/status          -- matches fleet/A/status, fleet/B/status, etc.
fleet/**/telemetry      -- matches any depth under fleet/
a/**/b                  -- matches a/b, a/x/b, a/x/y/b, etc.
**                      -- matches everything
```

**Invalid examples:**
```
/leading/slash          -- chunks cannot be empty
trailing/slash/         -- chunks cannot be empty
a**b                    -- ** must occupy an entire chunk
a/b*c/d                 -- * must occupy an entire chunk
```

### Wildcards

| Wildcard | Meaning | Example |
|---|---|---|
| `*` | Matches exactly one chunk (any content) | `a/*/c` matches `a/b/c` but not `a/b/x/c` |
| `**` | Matches zero or more chunks | `a/**/c` matches `a/c`, `a/b/c`, `a/b/d/c` |

### Canonicalization

KEs must be in canonical form before use. Non-canonical KEs (e.g., double slashes, redundant wildcards) are automatically canonicalized. The API will reject or normalize KEs at declaration time.

```rust
use zenoh::key_expr::KeyExpr;

// Static checked at compile time (macro)
let ke = zenoh::kedefine!(pub KE_SENSORS: "sensors/**");

// Runtime construction — canonicalized automatically
let ke: KeyExpr = "sensors/*/temp".try_into()?;

// Concatenation via / operator
let base: KeyExpr = "robot".try_into()?;
let full = &base / "arm" / "joint1";  // "robot/arm/joint1"
```

### Operators

```rust
// Intersection: do these two KEs share any common resources?
ke1.intersects(&ke2)   // true if any string matches both

// Inclusion: does ke1 include all resources of ke2?
ke1.includes(&ke2)     // true if every string matching ke2 also matches ke1

// Equality
ke1 == ke2
```

### Owned vs Borrowed

| Type | Description |
|---|---|
| `KeyExpr<'a>` | Borrowed — may reference a string slice |
| `OwnedKeyExpr` | Owned — heap-allocated, `'static` |
| `&keyexpr` | Borrowed reference to a validated KE slice (low-level) |

Use `KeyExpr::autocanonize()` when constructing from user input, and `ke.into_owned()` when you need to store or move a KE.

### Key Expression Declaration

Declaring a KE with the session allows the runtime to assign a compact numeric alias, reducing wire overhead:

```rust
let declared_ke = session.declare_keyexpr("robot/arm/**").await?;
// Now 'declared_ke' carries the alias; use it for publishers/subscribers
```

---

## Selector

### What It Is

A `Selector` extends a Key Expression with an optional **parameters** string, using the syntax:

```
selector ::= key_expression ['?' parameters]
parameters ::= key=value('&'key=value)*
```

Selectors are used exclusively for **queries** (`session.get()`). The parameters are passed to queryables as metadata — Zenoh itself does not interpret them (except for the special `_anyke` parameter). The queryable's application logic interprets parameters to filter or transform the reply.

```rust
// Simple selector
let replies = session.get("sensors/temperature").await?;

// With parameters
let replies = session.get("sensors/temperature?location=room1&unit=celsius").await?;

// Explicit construction
let selector = Selector::new("sensors/**", "ts>1000&ts<2000");
```

### Special Parameters

| Parameter | Meaning |
|---|---|
| `_anyke` (internal) | Accept replies on any key expression (not just intersecting ones) |

### Accessing Parameters in a Queryable

```rust
session.declare_queryable("sensors/**")
    .callback(|query| {
        let params = query.parameters();
        let location = params.get("location");
        // ... use params to filter reply
        query.reply(query.key_expr(), "25.3").await.unwrap();
    })
    .await?;
```

---

## Publisher

### What It Is

A `Publisher` is a declared, reusable object for sending data on a fixed key expression. Declaring a publisher:
- Registers the publisher with the session, enabling matching detection
- Negotiates a key expression alias (saves wire bytes)
- Captures default QoS settings (priority, congestion control, encoding, etc.)

### Declaration

```rust
let publisher = session
    .declare_publisher("robot/arm/joint_angles")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Drop)
    .encoding(Encoding::APPLICATION_JSON)
    .reliability(Reliability::Reliable)      // unstable
    .allowed_destination(Locality::Any)
    .await?;
```

### Publishing

```rust
// Put (data publication)
publisher.put("payload data").await?;

// Delete (tombstone — marks key as deleted)
publisher.delete().await?;

// Per-message overrides
publisher.put("payload")
    .encoding(Encoding::TEXT_PLAIN)
    .timestamp(session.new_timestamp())
    .attachment(b"extra metadata")
    .await?;
```

### Ad-hoc Publishing (without declaring a publisher)

```rust
// One-shot put — less efficient but simpler
session.put("robot/arm/joint_angles", "data")
    .priority(Priority::Interactive)
    .await?;

session.delete("robot/arm/joint_angles").await?;
```

### QoS Options

| Option | Type | Default | Description |
|---|---|---|---|
| `priority` | `Priority` | `DataHigh` | Message scheduling priority |
| `congestion_control` | `CongestionControl` | `Drop` | Behavior when queues are full |
| `express` | `bool` | `false` | Skip batching for low-latency |
| `reliability` | `Reliability` (unstable) | `BestEffort` | Wire-level reliability hint |
| `encoding` | `Encoding` | `ZENOH_BYTES` | Content type |
| `allowed_destination` | `Locality` | `Any` | Filter which subscribers receive data |

### Undeclaring

```rust
publisher.undeclare().await?;
// or just drop — publishers auto-undeclare on drop
```

---

## Subscriber

### What It Is

A `Subscriber` receives data published to matching key expressions. Declaring a subscriber registers interest with the network so routers can route matching publications here.

### Declaration

```rust
// With FIFO channel (default)
let subscriber = session
    .declare_subscriber("robot/arm/**")
    .await?;

// Receive samples
while let Ok(sample) = subscriber.recv_async().await {
    println!("key: {}, payload: {:?}", sample.key_expr(), sample.payload());
}
```

### Handlers

```rust
// Callback handler
let subscriber = session
    .declare_subscriber("sensors/**")
    .callback(|sample| {
        println!("Received: {}", sample.key_expr());
    })
    .await?;

// Callback (mutable, never called concurrently)
let mut count = 0;
let subscriber = session
    .declare_subscriber("sensors/**")
    .callback_mut(move |_sample| { count += 1; })
    .await?;

// Ring channel (drops oldest on overflow)
let subscriber = session
    .declare_subscriber("sensors/**")
    .with(zenoh::handlers::RingChannel::new(16))
    .await?;

// FIFO channel (blocks or drops on overflow depending on config)
let subscriber = session
    .declare_subscriber("sensors/**")
    .with(flume::bounded(64))
    .await?;

// Background subscriber (no handle needed)
session
    .declare_subscriber("sensors/**")
    .callback(|s| println!("{}", s.key_expr()))
    .background()
    .await?;
```

### Locality Filtering

```rust
// Only receive publications from within this session (loopback)
let subscriber = session
    .declare_subscriber("data/**")
    .allowed_origin(Locality::SessionLocal)
    .await?;

// Only from remote (other sessions/nodes)
let subscriber = session
    .declare_subscriber("data/**")
    .allowed_origin(Locality::Remote)
    .await?;

// Both (default)
let subscriber = session
    .declare_subscriber("data/**")
    .allowed_origin(Locality::Any)
    .await?;
```

### Key Properties

| Method | Description |
|---|---|
| `subscriber.recv_async()` | Async receive (if using channel handler) |
| `subscriber.recv()` | Sync receive |
| `subscriber.key_expr()` | The subscribed key expression |
| `subscriber.undeclare()` | Stop receiving and unregister |

---

## Queryable

### What It Is

A `Queryable` is the server side of Zenoh's request/reply pattern. When a query arrives matching its key expression, the queryable's handler is invoked with a `Query` object. The handler must respond with zero or more replies by calling `query.reply()`, `query.reply_err()`, or `query.reply_del()`.

Queryables are used to implement on-demand data access — think of them as "data servers" or "service endpoints."

### Declaration

```rust
let queryable = session
    .declare_queryable("robot/config/**")
    .complete(true)    // signals this KE is fully served by this queryable
    .allowed_origin(Locality::Any)
    .callback(|query| {
        println!("Query on: {}", query.key_expr());
        println!("Params: {}", query.parameters());

        // Reply with data
        query.reply(query.key_expr(), "config_value")
            .encoding(Encoding::TEXT_PLAIN)
            .await
            .unwrap();
    })
    .await?;
```

### The `complete` Flag

When `complete(true)`, the queryable promises to have authoritative data for its entire key expression. This enables `QueryTarget::BestMatching` optimization — when a complete queryable is found, the query need not be forwarded further.

```
complete = true  → "I own all data for this KE"
complete = false → "I have some data for this KE" (default)
```

### Replying

```rust
// Successful reply
query.reply(query.key_expr(), payload)
    .encoding(Encoding::APPLICATION_JSON)
    .timestamp(ts)
    .await?;

// Delete reply (tombstone)
query.reply_del(query.key_expr()).await?;

// Error reply
query.reply_err("not found").await?;
```

### Multiple Replies

A queryable can send multiple replies for a single query:

```rust
.callback(|query| {
    for item in &data_store {
        if query.key_expr().intersects(&item.key) {
            query.reply(item.key.clone(), item.value.clone())
                .wait()
                .unwrap();
        }
    }
    // query is dropped here — signals end of replies
})
```

### Background Queryable

```rust
session
    .declare_queryable("data/**")
    .callback(|q| { q.reply(q.key_expr(), "value").wait().unwrap(); })
    .background()
    .await?;
// Lives until session closes
```

---

## Query / Get

### What It Is

A **Get** (`session.get()`) initiates a query: it sends a request to all matching queryables in the network and collects their replies. This is the client side of the request/reply pattern.

### Basic Usage

```rust
let replies = session
    .get("robot/config/**")
    .await?;  // returns a handler (FIFO channel by default)

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Got: {} = {:?}", sample.key_expr(), sample.payload()),
        Err(err)   => println!("Error: {:?}", err.payload()),
    }
}
```

### QueryTarget

Controls which queryables should respond:

```rust
use zenoh::query::QueryTarget;

session.get("key/**")
    .target(QueryTarget::BestMatching)  // default: first complete match
    .target(QueryTarget::All)           // all matching queryables
    .target(QueryTarget::AllComplete)   // only complete queryables
    .await?;
```

| Target | Description |
|---|---|
| `BestMatching` | Prefer complete queryables; stop when found |
| `All` | Send to all matching queryables |
| `AllComplete` | Send only to complete queryables |

### ConsolidationMode

Controls how duplicate replies (same key expression) are filtered:

```rust
use zenoh::query::ConsolidationMode;

session.get("key/**")
    .consolidation(ConsolidationMode::None)      // all replies, no filtering
    .consolidation(ConsolidationMode::Monotonic) // keep latest per key
    .consolidation(ConsolidationMode::Latest)    // deduplicate by timestamp
    .await?;
```

| Mode | Description |
|---|---|
| `None` | Deliver all replies as received |
| `Monotonic` | Only deliver a reply if its timestamp is newer than any previously seen for the same key |
| `Latest` | Deduplicate: only deliver the single latest reply per key (after timeout) |
| `Auto` | Let the implementation choose (default) |

### Reply and ReplyError

```rust
match reply.result() {
    Ok(sample) => {
        // sample: &Sample — key_expr, payload, encoding, timestamp, etc.
        println!("key={}, payload={:?}", sample.key_expr(), sample.payload());
    }
    Err(reply_err) => {
        // ReplyError: payload + encoding describing the error
        println!("error payload: {:?}", reply_err.payload());
    }
}
```

### With Parameters / Payload

```rust
// Send a query with parameters (passed to queryable)
session.get("sensors/temperature?unit=celsius")
    .payload("optional request body")
    .encoding(Encoding::TEXT_PLAIN)
    .timeout(Duration::from_secs(5))
    .await?;
```

### ReplyKeyExpr

By default, replies must have a key expression that intersects the query's key expression. Use `accept_replies(ReplyKeyExpr::Any)` to accept replies on any key expression (useful for wildcard queries where replies may use concrete sub-keys):

```rust
session.get("sensors/**")
    .accept_replies(ReplyKeyExpr::Any)
    .await?;
```

---

## Querier

### What It Is

A `Querier` is a **declared, reusable** query object — the query-side analog of `Publisher`. Declaring a querier:
- Pre-negotiates the key expression alias
- Captures default query parameters (target, consolidation, timeout, QoS)
- Enables matching detection (like publishers)

Use a Querier when you repeatedly query the same key expression with the same settings — it is more efficient than repeated `session.get()` calls.

### Declaration and Use

```rust
let querier = session
    .declare_querier("robot/config/**")
    .target(QueryTarget::All)
    .consolidation(ConsolidationMode::None)
    .timeout(Duration::from_secs(5))
    .priority(Priority::DataHigh)
    .allowed_destination(Locality::Any)
    .await?;

// Issue a get — inherits all defaults from the querier
let replies = querier.get()
    .parameters("subsystem=arm")
    .await?;

while let Ok(reply) = replies.recv_async().await {
    println!("{:?}", reply.result());
}
```

### Querier vs Ad-hoc Get

| | `session.get()` | `Querier` |
|---|---|---|
| Key expression alias | Not pre-negotiated | Pre-negotiated |
| Matching listener | Not available | Available |
| Reuse overhead | High (re-resolves KE each time) | Low |
| Flexibility | Any KE/params per call | Fixed KE, variable params |

---

## Liveliness

### What It Is

Liveliness is a **presence detection** system built on top of Zenoh's pub/sub infrastructure. A **liveliness token** is a virtual assertion: "I (this session) am alive and associated with this key expression." When the token is undeclared or the session closes, a `Delete` event is automatically generated, notifying all liveliness subscribers.

This is used for service discovery, presence awareness, health monitoring, and distributed system membership.

### Key Space

Liveliness tokens use a special key prefix managed by Zenoh. From the user's perspective, tokens are associated with user-defined key expressions (e.g., `robot/fleet/robot1`).

### Tokens

```rust
// Declare a token — publishes "I am alive at this key"
let token = session
    .liveliness()
    .declare_token("robot/fleet/robot1")
    .await?;

// Token is live while this object is held
// When dropped or undeclared, a Delete is auto-published
token.undeclare().await?;
```

### Liveliness Subscribers

```rust
let subscriber = session
    .liveliness()
    .declare_subscriber("robot/fleet/**")
    .history(true)   // receive currently-alive tokens on startup
    .await?;

while let Ok(sample) = subscriber.recv_async().await {
    match sample.kind() {
        SampleKind::Put    => println!("Joined: {}", sample.key_expr()),
        SampleKind::Delete => println!("Left:   {}", sample.key_expr()),
    }
}
```

### Getting Current Live Tokens

```rust
let live = session
    .liveliness()
    .get("robot/fleet/**")
    .timeout(Duration::from_secs(1))
    .await?;

while let Ok(reply) = live.recv_async().await {
    if let Ok(sample) = reply.result() {
        println!("Currently alive: {}", sample.key_expr());
    }
}
```

### When to Use

- **Service registry**: Declare a token when a service starts; subscribers detect join/leave.
- **Robot fleet management**: Each robot declares a token; a monitor subscribes to the fleet namespace.
- **Health monitoring**: Watchdog processes detect token disappearance as a crash signal.
- **Leader election**: First to declare wins; subscriber detects leadership changes.

---

## Matching

### What It Is

The matching subsystem lets publishers and queriers discover whether matching subscribers or queryables currently exist. This enables **adaptive behavior** — e.g., stop computing expensive data if nobody is listening.

### MatchingStatus

A point-in-time snapshot of whether matching entities exist:

```rust
let publisher = session.declare_publisher("data/stream").await?;

let status = publisher.matching_status().await?;
if status.matching() {
    println!("Someone is subscribed — start publishing");
} else {
    println!("No subscribers — can skip computation");
}
```

### MatchingListener

A continuous listener that fires whenever the matching status changes:

```rust
let listener = publisher
    .matching_listener()
    .callback(|status| {
        if status.matching() {
            println!("Subscriber(s) appeared!");
        } else {
            println!("No more subscribers");
        }
    })
    .await?;

// Background variant (auto-cleaned when publisher drops)
publisher
    .matching_listener()
    .callback(|s| println!("matching: {}", s.matching()))
    .background()
    .await?;
```

### For Queriers

Queriers also support matching detection — detecting whether matching queryables exist:

```rust
let querier = session.declare_querier("robot/config/**").await?;
let status = querier.matching_status().await?;
```

### When to Use

- **Lazy publishers**: Only compute and send data when subscribers are present.
- **Adaptive rate control**: Increase/decrease publication frequency based on subscriber count changes.
- **Service health**: Alert when a required queryable disappears.

---

## Scouting

### What It Is

Scouting is Zenoh's peer/router **discovery mechanism**. Before a session is opened (or independently), you can scout the network to find other Zenoh participants. Scouting uses UDP multicast (on a configured group/port) and/or the gossip protocol.

### Scout API

```rust
use zenoh::scouting::{Scout, WhatAmI};

let scout = zenoh::scout(WhatAmI::Peer | WhatAmI::Router, Config::default())
    .await?;

while let Some(hello) = scout.recv_async().await {
    println!(
        "Found {:?} at {:?} with ZenohId {}",
        hello.whatami(),
        hello.locators(),
        hello.zid()
    );
}
```

### Hello Message

Each scouted peer returns a `Hello` containing:
- `zid()` — ZenohId of the discovered peer
- `whatami()` — role (Router / Peer / Client)
- `locators()` — list of locators where you can connect

### Discovery Mechanisms

| Mechanism | Config Key | Description |
|---|---|---|
| UDP Multicast | `scouting.multicast` | Sends Hello on `224.0.0.224:7447` (default). Works on LAN. |
| Gossip | `scouting.gossip` | Routers/peers relay Hello messages. Works across subnets. |

### When to Use Scouting

- **Dynamic discovery**: Automatically find routers without hardcoded addresses.
- **Introspection tools**: Build network topology visualizers.
- **Automated configuration**: Pick the closest router at startup.
- **Testing**: Verify which nodes are active on the network.

---

## WhatAmI

### What It Is

`WhatAmI` is an enum describing the **role** of a Zenoh participant. It determines routing behavior, scouting visibility, and connection topology.

### Variants

#### `Router`

```rust
config.set_mode(Some(WhatAmI::Router))?;
```

- **Purpose**: Infrastructure node. Routes data between clients and peers across network boundaries.
- **Connects to**: Other routers and peers.
- **Routing**: Full routing table — routes for all known key expressions.
- **Use when**: Running a dedicated Zenoh infrastructure process, a bridge, or a backbone node.

#### `Peer`

```rust
config.set_mode(Some(WhatAmI::Peer))?;  // default
```

- **Purpose**: Application node that also participates in peer-to-peer routing.
- **Connects to**: Routers, other peers.
- **Routing**: Partial routing (routes for its own subscriptions/publishers and those it learns from peers).
- **Use when**: Running application logic on a capable machine (PC, server, powerful embedded). This is the **default mode**.

#### `Client`

```rust
config.set_mode(Some(WhatAmI::Client))?;
```

- **Purpose**: Leaf node. Relies entirely on a connected router for routing.
- **Connects to**: Exactly one router (or a pool of routers for failover).
- **Routing**: None — all routing delegated to the router.
- **Use when**: Constrained devices, mobile nodes, or any process that should not participate in routing.

### Decision Guide

```
Do you need this node to route data for others?
├─ Yes → Router
└─ No
   ├─ Can it maintain connections to multiple peers?
   │  ├─ Yes → Peer (default)
   │  └─ No (constrained/mobile) → Client
```

### In Scouting Filters

```rust
// Scout for only routers
zenoh::scout(WhatAmI::Router, config).await?;

// Scout for peers or routers
zenoh::scout(WhatAmI::Peer | WhatAmI::Router, config).await?;
```

---

## Sample

### What It Is

A `Sample` is the fundamental data unit received by subscribers and queryables. Every published value, delete, and query reply arrives as a `Sample`. It is an immutable snapshot containing all metadata associated with a data event.

### Fields

```rust
// Received in a subscriber callback
fn handle(sample: Sample) {
    let key   = sample.key_expr();           // KeyExpr — which resource
    let body  = sample.payload();            // &ZBytes — raw payload
    let kind  = sample.kind();               // SampleKind::Put or Delete
    let enc   = sample.encoding();           // &Encoding — content type
    let ts    = sample.timestamp();          // Option<&Timestamp> — HLC timestamp
    let qos   = sample.qos();               // QoS parameters
    let att   = sample.attachment();         // Option<&ZBytes> — sidecar data
    let src   = sample.source_info();        // unstable: source ZenohId + SN
}
```

### QoS from Sample

```rust
let priority = sample.qos().priority();
let congestion = sample.qos().congestion_control();
let express = sample.qos().express();
let reliability = sample.qos().reliability();  // unstable
```

### Attachment

The attachment is an optional sidecar `ZBytes` that travels alongside the payload without Zenoh interpreting it. Use it for message metadata, correlation IDs, or custom headers:

```rust
publisher.put("payload")
    .attachment(b"correlation-id:42")
    .await?;

// In subscriber:
if let Some(att) = sample.attachment() {
    println!("attachment: {:?}", att);
}
```

---

## SampleKind

### What It Is

`SampleKind` is a two-variant enum indicating whether a sample represents data being written or data being deleted (a tombstone).

### Variants

```rust
pub enum SampleKind {
    Put,     // Data is being published/written
    Delete,  // Data is being removed (tombstone)
}
```

### When Each Is Produced

| Event | SampleKind |
|---|---|
| `publisher.put(...)` | `Put` |
| `publisher.delete()` | `Delete` |
| `session.put(...)` | `Put` |
| `session.delete(...)` | `Delete` |
| Liveliness token declared | `Put` |
| Liveliness token undeclared/session closed | `Delete` |

### Usage

```rust
match sample.kind() {
    SampleKind::Put    => println!("New value: {:?}", sample.payload()),
    SampleKind::Delete => println!("Key deleted: {}", sample.key_expr()),
}
```

---

##