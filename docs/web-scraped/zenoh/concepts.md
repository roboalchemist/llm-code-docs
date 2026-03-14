# Zenoh Concepts Reference

> **Definitive reference for Eclipse Zenoh** — the unified pub/sub/query protocol designed for the continuum from microcontrollers to cloud. Based on zenoh source code (0.11.x/1.x), RFCs, and official documentation.

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
22. [Shared Memory (SHM)](#shared-memory-shm)
23. [Admin Space](#admin-space)
24. [Handlers](#handlers)
25. [Builders](#builders)

---

## Session

### What it is

The `Session` is the central entry point for all zenoh operations. It represents a connection to the zenoh network and is the factory for every other zenoh entity: publishers, subscribers, queryables, queriers, and liveliness tokens. All resources are tied to the session's lifetime.

A session is created via `zenoh::open()`, which takes a `Config`. When the session is dropped (or explicitly closed), all declared entities are undeclared and all in-flight operations are terminated. The close operation has a configurable timeout (default: 10 seconds).

### When to use

Create one session per process (occasionally per major logical component in a large application). Sessions are `Arc`-wrapped internally and cloneable (the clone refers to the same underlying session). Prefer a single session to avoid redundant network connections.

### Lifecycle

```
zenoh::open(config) → Session
     │
     ├── declare_publisher(...)
     ├── declare_subscriber(...)
     ├── declare_queryable(...)
     ├── declare_querier(...)
     ├── get(...)
     ├── liveliness()
     └── close() → CloseBuilder
```

The session can be closed explicitly with `session.close().await` (or `.wait()`). Dropping the `Session` without closing it triggers an implicit close. The `CloseBuilder` exposes:
- `.timeout(Duration)` — override the 10-second close timeout.
- `.wait_callbacks()` *(unstable)* — block until all running callbacks have returned before closing.

### Builder pattern

`zenoh::open()` returns an `OpenBuilder` that resolves to `ZResult<Session>`. Configuration is provided via `zenoh::Config`.

```rust
// Async open
let session = zenoh::open(zenoh::Config::default()).await?;

// Sync open
let session = zenoh::open(zenoh::Config::default()).wait()?;

// Open with custom config
let mut config = zenoh::Config::default();
config.set_mode(Some(WhatAmI::Peer));
let session = zenoh::open(config).await?;

// Explicit close
session.close().await?;

// Close with callback drain
session.close().wait_callbacks().await?;
```

### Key session methods

| Method | Returns | Description |
|---|---|---|
| `session.info()` | `SessionInfo` | Access ZID, connected routers/peers |
| `session.declare_publisher(ke)` | `PublisherBuilder` | Declare a publisher |
| `session.declare_subscriber(ke)` | `SubscriberBuilder` | Declare a subscriber |
| `session.declare_queryable(ke)` | `QueryableBuilder` | Declare a queryable |
| `session.declare_querier(ke)` | `QuerierBuilder` | Declare a reusable querier |
| `session.get(selector)` | `SessionGetBuilder` | Ad-hoc query |
| `session.put(ke, payload)` | `SessionPutBuilder` | Direct put (no predeclared publisher) |
| `session.delete(ke)` | `SessionDeleteBuilder` | Direct delete |
| `session.liveliness()` | `Liveliness` | Access liveliness API |
| `session.declare_keyexpr(ke)` | key expr optimization | Pre-declare a key expression |
| `session.zid()` | `ZenohId` | This session's unique ID |

### Session Info

```rust
let info = session.info();
let my_zid = info.zid().await;
let routers: Vec<ZenohId> = info.routers_zid().await.collect();
let peers: Vec<ZenohId> = info.peers_zid().await.collect();
```

---

## Key Expressions

### What it is

A **Key Expression** (KE) is the fundamental addressing mechanism in zenoh. It is a `/`-separated path that identifies a resource. Every put, subscribe, query, and reply operates on key expressions. KEs can be concrete (identifying a single resource) or contain wildcards (identifying a set of resources).

### Syntax rules

- Segments are separated by `/`
- A segment must not be empty (no `//`)
- The string must not start or end with `/`
- Allowed characters in segments: any except `*`, `?`, `#`, `[`, `]`

### Wildcards

| Wildcard | Meaning | Example |
|---|---|---|
| `*` | Matches any single segment (one chunk, no `/`) | `home/*/temp` matches `home/kitchen/temp` |
| `**` | Matches any number of segments including zero | `home/**/temp` matches `home/temp`, `home/floor1/room2/temp` |
| `$*` | DSL — alternative (within segments) | Not commonly used in basic API |

Examples:
```
home/kitchen/temperature     # concrete
home/*/temperature           # single wildcard — any room
home/**/temperature          # double wildcard — any depth
**/temperature               # all temperatures anywhere
**                           # everything
```

### Canonicalization

Key expressions are canonicalized on construction. Canonicalization:
- Removes redundant `**` patterns (e.g., `a/**/**/b` → `a/**/b`)
- Normalizes the expression to its minimal form

Always prefer the `keyexpr!` macro for compile-time-validated literals, or `KeyExpr::try_from("...")` for runtime construction.

### Operators

Two key expressions can be tested for relationships:

| Method | Meaning |
|---|---|
| `ke1.intersects(ke2)` | Is there any string matched by both? |
| `ke1.includes(ke2)` | Does ke1 match everything ke2 matches? (ke1 ⊇ ke2) |
| `ke1 / ke2` | Concatenate with `/` separator |

```rust
use zenoh::key_expr::KeyExpr;

// Construction
let ke: KeyExpr = "home/kitchen/temp".try_into()?;

// Compile-time validated via macro
use zenoh_macros::ke;
let ke: &keyexpr = ke!("home/kitchen/temp");

// Wildcards
let wildcard: KeyExpr = "home/*/temp".try_into()?;

// Relationships
assert!(wildcard.intersects(&ke));
assert!(wildcard.includes(&ke));
assert!(!ke.includes(&wildcard));

// Concatenation
let base: KeyExpr = "home".try_into()?;
let full = base / KeyExpr::try_from("kitchen/temp")?;
// => "home/kitchen/temp"

// Pre-declare to optimize routing (reduces wire overhead)
let optimized = session.declare_keyexpr("home/kitchen/temp").await?;
```

### Pre-declared key expressions

Calling `session.declare_keyexpr(ke)` registers the key expression with the session and network, returning a mapped `KeyExpr` that carries a compact numeric ID on the wire. This is an optimization — not a requirement.

---

## Selector

### What it is

A `Selector` extends a key expression with an optional parameter string, separated by `?`. Selectors are used exclusively in `get()` and `Queryable` interactions to pass filtering or query parameters to queryables.

### Syntax

```
<key_expression>?<parameters>
```

Parameters are a `&`-separated list of `key=value` pairs (query-string style):

```
home/sensors?room=kitchen&value>20
temperature/**?unit=celsius&precision=2
```

The `?` and everything after it is the **parameters** portion. The key expression portion is the part before `?`.

### Key properties

- Parameters are queryable-application-defined — zenoh does not interpret them (except for built-in ones like `_anyke` for disjoint replies)
- A `Selector` with no `?` is equivalent to just a key expression
- The special parameter `_anyke` (constant `REPLY_KEY_EXPR_ANY_SEL_PARAM`) tells zenoh to accept replies on key expressions that don't intersect with the query KE

```rust
use zenoh::selector::Selector;

// From a string (parsed at runtime)
let sel: Selector = "home/*/temp?room=kitchen".try_into()?;

// Accessing parts
let ke = sel.key_expr();       // "home/*/temp"
let params = sel.parameters(); // "room=kitchen"

// In a get call
let replies = session
    .get("home/*/temp?room=kitchen")
    .await?;

// Explicit selector construction
let sel = Selector::new("home/*/temp", "room=kitchen&min=18");

// Accept disjoint replies
let replies = session
    .get("home/*/temp")
    .accept_replies(ReplyKeyExpr::Any)
    .await?;
```

---

## Publisher

### What it is

A `Publisher` is a declared entity that sends data (samples) to all matching subscribers on a specific key expression. Declaring a publisher pre-registers QoS settings and the key expression with the network, enabling routing optimization. Publishers send `Put` and `Delete` samples.

### When to use

Use a declared publisher (vs `session.put()`) when you publish to the same key expression repeatedly. Pre-declaration:
- Reduces wire overhead (key expression ID instead of full string)
- Allows the network to pre-establish routing paths
- Enables `MatchingListener` (subscriber presence detection)
- Applies QoS defaults consistently across all publications

Use `session.put()` for occasional one-off publications.

### Declaration and options

All options are set on the `PublisherBuilder` before resolution:

```rust
let publisher = session
    .declare_publisher("home/kitchen/temp")
    .encoding(Encoding::APPLICATION_JSON)          // default encoding for put()
    .priority(Priority::RealTime)                   // traffic priority
    .congestion_control(CongestionControl::Block)   // backpressure behavior
    .express(true)                                  // skip batching for low latency
    .reliability(Reliability::Reliable)             // wire-level hint (unstable)
    .allowed_destination(Locality::Any)             // local-only, remote-only, or any
    .await?;
```

### Publishing data

```rust
// Put (with optional per-put overrides)
publisher.put("25.3")
    .encoding(Encoding::TEXT_PLAIN)
    .timestamp(session.new_timestamp())
    .attachment(b"sensor-v2")
    .await?;

// Delete
publisher.delete().await?;

// Direct session put (no predeclared publisher)
session.put("home/kitchen/temp", "25.3")
    .encoding(Encoding::TEXT_PLAIN)
    .priority(Priority::DataHigh)
    .await?;

// Direct session delete
session.delete("home/kitchen/temp").await?;
```

### QoS options summary

| Option | Type | Default | Description |
|---|---|---|---|
| `priority` | `Priority` | `Data` (4) | Message scheduling priority |
| `congestion_control` | `CongestionControl` | `Drop` | Behavior when buffers are full |
| `express` | `bool` | `false` | Skip batching for lower latency |
| `reliability` | `Reliability` | `BestEffort` | Wire-level transport hint |
| `allowed_destination` | `Locality` | `Any` | Restrict to local/remote/both |

### Publisher lifecycle

```rust
// Explicit undeclare
publisher.undeclare().await?;

// Drop (implicit undeclare)
drop(publisher);

// Background publisher (lives until session closes)
session
    .declare_publisher("key/expression")
    .callback_mut(|_| {})   // Not applicable here, but background
    // Publishers don't have background mode; hold the variable or undeclare explicitly
```

---

## Subscriber

### What it is

A `Subscriber` receives samples published on key expressions that match its declared key expression. A subscriber's key expression typically includes wildcards to receive from multiple publishers. Each received sample includes the key expression, payload, encoding, timestamp, QoS metadata, and attachment.

### Declaration

```rust
// With FIFO channel handler (default)
let subscriber = session
    .declare_subscriber("home/**/temperature")
    .allowed_origin(Locality::Any)  // SessionLocal, Remote, or Any
    .await?;

// Receive samples from the channel
while let Ok(sample) = subscriber.recv_async().await {
    println!("{}: {:?}", sample.key_expr(), sample.payload());
}
```

### Handlers

Three handler patterns are available (see [Handlers](#handlers)):

```rust
// 1. Callback — fires on every sample, no buffering
let sub = session
    .declare_subscriber("home/**/temperature")
    .callback(|sample| {
        println!("Received: {}", sample.key_expr());
    })
    .await?;

// 2. Mutable callback (serialized — never concurrent)
let mut count = 0;
let sub = session
    .declare_subscriber("home/**/temperature")
    .callback_mut(move |_sample| { count += 1; })
    .await?;

// 3. Custom handler (FIFO or ring channel)
let sub = session
    .declare_subscriber("home/**/temperature")
    .with(flume::bounded(128))  // FIFO, drops oldest when full
    .await?;

// 4. Background subscriber (lives until session closes, no variable needed)
session
    .declare_subscriber("home/**/temperature")
    .callback(|sample| { println!("{}", sample.key_expr()); })
    .background()
    .await?;
```

### Locality filtering

`allowed_origin(Locality)` restricts which samples are delivered:

| Value | Behavior |
|---|---|
| `Locality::SessionLocal` | Only samples from publishers in the **same session** |
| `Locality::Remote` | Only samples from **other sessions** (different process or host) |
| `Locality::Any` | All samples (default) |

```rust
// Only receive data published in the same process
let local_sub = session
    .declare_subscriber("**")
    .allowed_origin(Locality::SessionLocal)
    .await?;
```

### Undeclaring a subscriber

```rust
subscriber.undeclare().await?;
// Or just drop it — undeclare happens automatically
```

---

## Queryable

### What it is

A `Queryable` is the server-side entity in zenoh's query/reply model. It declares interest in receiving queries matching a key expression, and for each received query it can send back zero or more replies. Queryables are the foundation of request-response, data-retrieval-from-storage, and RPC patterns.

### Declaration

```rust
let queryable = session
    .declare_queryable("home/**/temperature")
    .complete(true)     // signals this queryable has complete data for its KE
    .allowed_origin(Locality::Any)
    .await?;
```

**`complete` flag**: When `true`, the queryable declares that it has all data for its key expression. Queries with `QueryTarget::BestMatching` will route to this queryable and stop there rather than querying other nodes. Set to `false` (default) for queryables that may only have partial data.

### Handling queries and replying

Each `Query` object received has:
- `query.key_expr()` — the query's key expression
- `query.parameters()` — the selector parameters string
- `query.payload()` / `query.encoding()` / `query.attachment()` — optional request body
- `query.reply(ke, payload)` — send a successful reply
- `query.reply_err(payload)` — send an error reply
- `query.reply_del(ke)` — send a delete reply

```rust
// With channel handler
let queryable = session
    .declare_queryable("home/**/temperature")
    .complete(true)
    .with(flume::bounded(32))
    .await?;

while let Ok(query) = queryable.recv_async().await {
    println!(
        "Query on '{}' with params '{}'",
        query.key_expr(),
        query.parameters()
    );

    // Reply with data
    query
        .reply("home/kitchen/temperature", "23.5")
        .encoding(Encoding::TEXT_PLAIN)
        .await?;

    // Reply with an error
    // query.reply_err("sensor offline").await?;

    // Reply indicating deletion
    // query.reply_del("home/kitchen/temperature").await?;
}
```

### Callback-based queryable

```rust
let queryable = session
    .declare_queryable("home/**/temperature")
    .callback(|query| {
        let ke = query.key_expr().clone();
        tokio::spawn(async move {
            query.reply(ke, "22.0").await.unwrap();
        });
    })
    .await?;
```

### Background queryable

```rust
session
    .declare_queryable("home/**/temperature")
    .callback(|query| {
        let _ = query.reply(query.key_expr().clone(), "22.0");
    })
    .background()
    .await?;
// No variable needed — lives until session closes
```

### Consolidation

Queryables themselves don't set consolidation — that is done by the **querier**. However, queryables should be aware that they may receive the same query from multiple network paths. The `complete` flag helps the network avoid redundant delivery.

---

## Query / Get

### What it is

`session.get()` sends a query into the network matching a selector and collects replies from all matching queryables. This is the **request/response** or **data-retrieval** primitive in zenoh. Replies arrive asynchronously through a handler until the query times out or all queryables have replied.

### When to use

- Fetching current state from a storage or queryable
- RPC (remote procedure call) patterns
- Discovering live data: "what values exist for `home/**/temperature`?"
- Complementary to subscriptions: get current value, then subscribe for updates

### `ConsolidationMode`

Controls deduplication/merging of replies when multiple paths return data for the same key:

| Mode | Behavior |
|---|---|
| `ConsolidationMode::None` | Deliver all replies as received — duplicates included |
| `ConsolidationMode::Monotonic` | Only deliver replies with strictly increasing timestamps for each key |
| `ConsolidationMode::Latest` | Only deliver the single latest reply per key (highest timestamp) |
| `QueryConsolidation::AUTO` | Let the implementation choose the best mode |

### `QueryTarget`

Controls which queryables receive the query:

| Target | Behavior |
|---|---|
| `QueryTarget::BestMatching` | Route to the "best" matching queryable (considers `complete` flag) |
| `QueryTarget::All` | Send to all matching queryables |
| `QueryTarget::AllComplete` | Send only to queryables declared as `complete(true)` |

### Reply and ReplyError

Each reply is a `Reply` which has:
- `reply.result()` → `Result<&Sample, &ReplyError>`
- On success: a full `Sample` with key expression, payload, encoding, timestamp
- On error: a `ReplyError` with a payload describing the failure

```rust
// Basic get
let replies = session
    .get("home/**/temperature")
    .await?;

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => {
            println!("  Key: {}", sample.key_expr());
            println!("  Value: {:?}", sample.payload());
        }
        Err(err) => println!("  Error: {:?}", err.payload()),
    }
}

// With full options
let replies = session
    .get("home/**/temperature?room=kitchen")
    .target(QueryTarget::All)
    .consolidation(ConsolidationMode::Latest)
    .timeout(Duration::from_secs(5))
    .allowed_destination(Locality::Any)
    .priority(Priority::DataHigh)
    .congestion_control(CongestionControl::Block)
    .express(true)
    .payload(b"query-body")         // optional request body
    .encoding(Encoding::ZENOH_BYTES)
    .attachment(b"meta")
    .with(flume::bounded(64))       // use a bounded channel
    .await?;

// With callback
session
    .get("home/**/temperature")
    .callback(|reply| {
        println!("Reply: {:?}", reply.result());
    })
    .await?;
```

### `ReplyKeyExpr`

By default, replies must be on key expressions that intersect with the query KE. Setting `accept_replies(ReplyKeyExpr::Any)` removes this restriction, allowing queryables to reply with any key:

```rust
let replies = session
    .get("home/sensors")
    .accept_replies(ReplyKeyExpr::Any)
    .await?;
```

---

## Querier

### What it is

A `Querier` is a **declared reusable querier** — the query analog to `Publisher` for get operations. Like a publisher pre-declares QoS settings and key expression for repeated publications, a `Querier` pre-declares all query settings for repeated get operations to the same key expression.

### Querier vs ad-hoc `session.get()`

| Aspect | `session.get()` | `Querier` |
|---|---|---|
| Declaration overhead | Per call | Once at declaration |
| Key expression wire optimization | No | Yes (numeric ID) |
| Routing pre-computation | No | Yes |
| `MatchingListener` support | No | Yes |
| Best for | Occasional queries | Frequent queries to same KE |

### Declaration and use

```rust
// Declare a querier
let querier = session
    .declare_querier("home/**/temperature")
    .target(QueryTarget::All)
    .consolidation(ConsolidationMode::None)
    .timeout(Duration::from_secs(5))
    .allowed_destination(Locality::Any)
    .accept_replies(ReplyKeyExpr::Any)
    .priority(Priority::Data)
    .congestion_control(CongestionControl::Block)
    .await?;

// Issue a get via the querier (inherits declared settings)
let replies = querier
    .get()
    .parameters("room=kitchen&value>20")  // add selector parameters
    .payload(b"request-body")             // optional body
    .with(flume::bounded(32))
    .await?;

while let Ok(reply) = replies.recv_async().await {
    println!("{:?}", reply.result());
}

// Undeclare
querier.undeclare().await?;
```

The `querier.get()` builder only exposes options that vary per-call (parameters, payload, encoding, attachment). Options fixed at declaration time (target, consolidation, timeout, destination) come from the declared state.

---

## Liveliness

### What it is

The **Liveliness** API provides presence/reachability detection. A `LivelinessToken` is a declaration that says "I am alive and reachable on this key expression." When the token is undeclared or the session closes, a `Delete` sample is published to liveliness subscribers. This enables building liveness/heartbeat mechanisms without polling.

### When to use

- Service discovery: detect when microservices come online/go offline
- Robot/device presence: "is robot-3 currently connected?"
- Health monitoring: detect disconnections without polling
- Complementary to subscriptions: know if a publisher is still alive

### Liveliness Token

```rust
// Declare a liveliness token (I am alive)
let token = session
    .liveliness()
    .declare_token("robots/robot-3/status")
    .await?;

// Token is alive while this variable is held.
// When dropped or undeclared → Delete sample sent to subscribers.

token.undeclare().await?;
```

### Liveliness Subscriber

```rust
// Subscribe to liveliness events
let sub = session
    .liveliness()
    .declare_subscriber("robots/**")
    .history(true)   // get currently-live tokens on declaration
    .await?;

while let Ok(sample) = sub.recv_async().await {
    match sample.kind() {
        SampleKind::Put    => println!("ALIVE: {}", sample.key_expr()),
        SampleKind::Delete => println!("GONE:  {}", sample.key_expr()),
    }
}
```

**`history(true)`**: On subscriber declaration, zenoh queries the network for currently live tokens and delivers them as `Put` samples before live events. This ensures the subscriber sees the current state, not just future changes.

### Getting current live tokens

```rust
// One-shot query for all currently live tokens
let live = session
    .liveliness()
    .get("robots/**")
    .timeout(Duration::from_secs(2))
    .await?;

while let Ok(reply) = live.recv_async().await {
    if let Ok(sample) = reply.result() {
        println!("Currently alive: {}", sample.key_expr());
    }
}
```

### Summary of liveliness semantics

| Event | Wire effect |
|---|---|
| Token declared | `Put` sample delivered to matching subscribers |
| Token undeclared | `Delete` sample delivered |
| Session closes (token in scope) | `Delete` sample delivered |
| Network partition heals | Tokens may be re-announced |

---

## Matching

### What it is

The **Matching** API allows a `Publisher` or `Querier` to know whether there are currently any matching subscribers (for publishers) or queryables (for queriers) in the network. This is useful for avoiding wasteful work when no one is listening.

### MatchingStatus

A point-in-time snapshot: "does this publisher currently have matching subscribers?"

```rust
// Check once
let status: MatchingStatus = publisher.matching_status().await?;
if status.matching() {
    println!("Publisher has subscribers — worth publishing");
} else {
    println!("No subscribers — can skip expensive computation");
}
```

### MatchingListener

A reactive listener that fires when the matching status changes:

```rust
let listener = publisher
    .matching_listener()
    .callback(|status: MatchingStatus| {
        if status.matching() {
            println!("Subscribers connected — start publishing");
        } else {
            println!("No more subscribers — can pause");
        }
    })
    .await?;

// With channel
let listener = publisher
    .matching_listener()
    .with(flume::bounded(8))
    .await?;

while let Ok(status) = listener.recv_async().await {
    println!("Matching changed: {}", status.matching());
}

// Background (lives with publisher)
publisher
    .matching_listener()
    .callback(|s| println!("{}", s.matching()))
    .background()
    .await?;

// Undeclare
listener.undeclare().await?;
```

### Querier matching

The same API is available on `Querier` to detect when queryables become available:

```rust
let listener = querier
    .matching_listener()
    .callback(|status| {
        println!("Queryable available: {}", status.matching());
    })
    .await?;
```

---

## Scouting

### What it is

**Scouting** is zenoh's peer/router discovery mechanism. It allows a process to discover other zenoh nodes on the local network without prior configuration. Scouting sends `Scout` messages (via UDP multicast or broadcast) and collects `Hello` responses from any zenoh nodes that hear them.

### When to use

- Auto-configuration: discover routers to connect to
- Network inventory: list all zenoh nodes on the LAN
- Diagnostics: verify the network topology
- Bootstrap: find initial peers before opening a session

### `scout()`

```rust
use zenoh::scouting::{WhatAmI, Scout};

// Scout for all zenoh nodes
let scout = zenoh::scout(WhatAmI::Router | WhatAmI::Peer, zenoh::Config::default())
    .await?;

while let Some(hello) = scout.recv_async().await {
    println!(
        "Found {:?} at {:?} (ZID: {})",
        hello.whatami(),
        hello.locators(),
        hello.zid()
    );
}

// Scout only for routers
let scout = zenoh::scout(WhatAmI::Router, zenoh::Config::default())
    .callback(|hello| {
        println!("Router found: {}", hello.zid());
    })
    .await?;
```

### Discovery mechanisms

Zenoh supports two discovery modes, configured in `Config`:

| Mode | Mechanism | Use case |
|---|---|---|
| **Multicast** | UDP multicast packets | LAN environments, automatic discovery |
| **Gossip** | Peer-to-peer gossip protocol | WAN, cloud, environments without multicast |

Multicast discovery uses a configurable multicast address (default: `224.0.0.224:7447`). Gossip discovery propagates reachability information through known connections.

### Hello message

Each discovered node returns a `Hello` containing:
- `hello.zid()` — the node's unique ZenohID
- `hello.whatami()` — `Router`, `Peer`, or `Client`
- `hello.locators()` — list of endpoints the node is reachable at

---

## WhatAmI

### What it is

`WhatAmI` is a 3-valued enum describing the **role** of a zenoh node in the network. The role determines routing behavior, connection topology, and resource usage.

### Variants

#### `WhatAmI::Router`

A **router** is a dedicated infrastructure node that:
- Participates in network-level routing and topology management
- Maintains routing tables for all key expressions
- Connects to other routers to form the backbone of the zenoh network
- Can be connected to by both `Peer` and `Client` nodes
- Typically runs as a standalone process (`zenohd`)

**When to use**: For infrastructure deployments — cloud gateways, data center bridges, WAN routing nodes.

#### `WhatAmI::Peer`

A **peer** is a fully-featured node that:
- Participates in distributed routing decisions
- Performs peer-to-peer routing with neighboring peers (no dedicated router needed)
- Can connect to both routers and other peers
- Can form ad-hoc mesh networks without any router
- Has higher resource usage than Client but supports fully decentralized operation

**When to use**: For devices that need to communicate in ad-hoc networks (robots, edge devices, IoT gateways) without a dedicated router. The default mode for most applications.

#### `WhatAmI::Client`

A **client** is a lightweight node that:
- Relies entirely on a router (or peer acting as a broker) for routing
- Performs no routing itself
- Minimal resource usage
- Must connect to at least one `Router` or `Peer`
- Suitable for constrained devices

**When to use**: For resource-constrained devices (microcontrollers, embedded systems) that connect to a known router.

### Configuration

```rust
// Set role in config
let mut config = zenoh::Config::default();
config.set_mode(Some(WhatAmI::Peer));   // or Router, Client

// Router
config.set_mode(Some(WhatAmI::Router));
// Typically also set listeners:
// config.listen.endpoints = ["tcp/0.0.0.0:7447"]

// Client connecting to a known router
config.set_mode(Some(WhatAmI::Client));
// config.connect.endpoints = ["