# Zenoh Programming Model: A Comprehensive Guide

Zenoh is a protocol and API that unifies data-in-motion (pub/sub) and data-at-rest (storage/query) under a single, location-transparent abstraction. This guide covers the complete programming model from design philosophy through practical patterns, drawing from the Rust and Python implementations.

---

## Table of Contents

- [Design Philosophy](#design-philosophy)
  - [The Genesis: Why Zenoh Was Built](#the-genesis-why-zenoh-was-built)
  - [Location Transparency: The Core Design Goal](#location-transparency-the-core-design-goal)
  - [Unified Data-in-Motion + Data-at-Rest](#unified-data-in-motion-data-at-rest)
  - [Protocol Unification](#protocol-unification)
  - [Design Tensions](#design-tensions)
- [The Session: Root of Everything](#the-session-root-of-everything)
  - [Opening a Session](#opening-a-session)
  - [Session Internals](#session-internals)
  - [Clone Semantics](#clone-semantics)
  - [Closing a Session](#closing-a-session)
- [Key Expressions](#key-expressions)
  - [Wildcards](#wildcards)
  - [The Intersection Model](#the-intersection-model)
  - [Verbatim Chunks](#verbatim-chunks)
  - [Declared vs Inline Key Expressions](#declared-vs-inline-key-expressions)
- [The Builder Pattern](#the-builder-pattern)
  - [Why Builders?](#why-builders)
  - [The Resolvable / Wait Pattern](#the-resolvable-wait-pattern)
  - [Builder Lifecycle](#builder-lifecycle)
- [Publishing Data](#publishing-data)
  - [Session Put: The Simplest Form](#session-put-the-simplest-form)
  - [Declared Publisher: Optimization + Wire ID](#declared-publisher-optimization-wire-id)
  - [Publisher QoS](#publisher-qos)
  - [Publisher Delete](#publisher-delete)
- [Subscribing to Data](#subscribing-to-data)
  - [Basic Subscriber](#basic-subscriber)
  - [Sample Structure](#sample-structure)
  - [Locality: Filtering by Source](#locality-filtering-by-source)
- [Handler Types: FIFO, Ring, and Callback](#handler-types-fifo-ring-and-callback)
  - [The Default: FIFO Channel](#the-default-fifo-channel)
  - [Ring Channel: Drop-Oldest Strategy](#ring-channel-drop-oldest-strategy)
  - [Callback Handler: Lowest Latency](#callback-handler-lowest-latency)
  - [Choosing a Handler](#choosing-a-handler)
- [Querying Data: The Get/Queryable Pattern](#querying-data-the-getqueryable-pattern)
  - [Issuing a Query: `session.get()`](#issuing-a-query-sessionget)
  - [Query Targets](#query-targets)
  - [Declaring a Queryable](#declaring-a-queryable)
  - [The `complete` Flag](#the-complete-flag)
  - [Query Selector: Key Expression + Parameters](#query-selector-key-expression-parameters)
  - [Reply Errors](#reply-errors)
- [Consolidation Modes](#consolidation-modes)
- [The Storage Pattern: Combining Subscriber + Queryable](#the-storage-pattern-combining-subscriber-queryable)
- [Async vs Sync API](#async-vs-sync-api)
  - [When to Use Async](#when-to-use-async)
  - [When to Use Sync](#when-to-use-sync)
  - [Thread Count Implications](#thread-count-implications)
- [Thread Minimization](#thread-minimization)
  - [Starting Point: Thread-per-Subscriber](#starting-point-thread-per-subscriber)
  - [Step 1: Consolidate to One Async Event Loop](#step-1-consolidate-to-one-async-event-loop)
  - [Step 2: Use Callbacks for Fire-and-Forget Operations](#step-2-use-callbacks-for-fire-and-forget-operations)
  - [Step 3: Use FIFO Channel on Main Thread for Ordered Processing](#step-3-use-fifo-channel-on-main-thread-for-ordered-processing)
  - [Summary: Thread Reduction Playbook](#summary-thread-reduction-playbook)
- [Message Attachments](#message-attachments)
  - [Attaching Metadata at Publish Time](#attaching-metadata-at-publish-time)
  - [Reading Attachments at Subscribe Time](#reading-attachments-at-subscribe-time)
  - [Use Cases](#use-cases)
- [Timestamps](#timestamps)
  - [Timestamp Format](#timestamp-format)
  - [Automatic vs Manual Timestamps](#automatic-vs-manual-timestamps)
  - [Reading Timestamps](#reading-timestamps)
  - [Why Timestamps Matter](#why-timestamps-matter)
- [QoS: Priority, Reliability, Congestion Control](#qos-priority-reliability-congestion-control)
  - [Priority](#priority)
  - [Congestion Control](#congestion-control)
  - [Reliability](#reliability)
  - [Express Mode](#express-mode)
- [Locality Control](#locality-control)
- [Matching Status](#matching-status)
  - [Checking Matching Status](#checking-matching-status)
  - [Matching Listener](#matching-listener)
- [The zenoh-ext Extension Library](#the-zenoh-ext-extension-library)
  - [Publication Cache](#publication-cache)
  - [Querying Subscriber](#querying-subscriber)
  - [Advanced Publisher and Subscriber](#advanced-publisher-and-subscriber)
  - [Serialization Utilities](#serialization-utilities)
- [Complete Examples](#complete-examples)
  - [Rust: Minimal Pub/Sub](#rust-minimal-pubsub)
  - [Python: Minimal Pub/Sub](#python-minimal-pubsub)
  - [Rust: Query/Reply](#rust-queryreply)
- [Quick Reference](#quick-reference)
  - [API Surface](#api-surface)
  - [Handler Selection](#handler-selection)
  - [Optimization Checklist](#optimization-checklist)


---


## Design Philosophy

### The Genesis: Why Zenoh Was Built

Before zenoh, distributed systems had to pick from a menu of incomplete solutions:

- **DDS** (Data Distribution Service): excellent QoS, but heavyweight, XML-based, requires domain management, not internet-friendly, and the "topic" model forces you to know at design time what data you'll need.
- **MQTT**: lightweight and broker-based, but the broker is a single point of failure and the topic model is flat—no wildcards over hierarchical paths, no request-reply.
- **REST**: familiar and internet-native, but strictly request-response only, no push notifications, high overhead for high-frequency data.
- **Custom protocols**: you end up implementing your own, and interoperability dies.

Zenoh was designed from the observation that all these protocols share a common core: they are all about **named data**. A DDS topic is a name. An MQTT topic is a name. A REST URL is a name. The key insight is: **if you get the naming model right and the routing model right, you can unify all of them**.

### Location Transparency: The Core Design Goal

The deepest design goal is **location transparency**: your application code should not need to know where data comes from or where it goes. You subscribe to `sensors/**` and you receive data from any publisher on that pattern, regardless of:

- Whether publishers are on the same process
- Whether they're across a LAN
- Whether they're across the internet via bridges
- Whether they were running before you started or started after you

This isn't just a convenience—it's an architectural guarantee. Code that is correct on a local machine is correct in a distributed deployment. No code changes, no configuration changes in application logic. Only the zenoh configuration changes (which routers to connect to), and that's intentionally separated from application code.

### Unified Data-in-Motion + Data-at-Rest

The same key expression system that addresses pub/sub also addresses stored data. When you call `session.get("sensors/**")`, zenoh routes that query to:

1. **Live queryables**: processes that registered `declare_queryable("sensors/**")` and respond programmatically
2. **Storage backends**: zenoh plugins (RocksDB, InfluxDB, S3, filesystem) that store published data and answer queries for it

Your application uses the same `session.get()` call for both. The separation between "data that is flowing now" and "data that was stored previously" is handled transparently by the routing layer.

### Protocol Unification

Zenoh ships bridge plugins that connect to DDS, MQTT, and ROS2 networks. From a zenoh application's perspective, a temperature sensor publishing via DDS and a sensor publishing via native zenoh look identical—they both appear as samples on key expressions. This is what "protocol unification" means: one API surface, multiple wire protocols behind it.

### Design Tensions

Not every "obvious" feature is present, and the absences are intentional:

**Why no persistent subscriptions?** Persistent subscriptions would require the routing infrastructure to remember who wants what, creating stateful infrastructure that breaks location transparency. Instead, zenoh uses the storage + queryable pattern: store data in a backend, query it when you reconnect.

**Why no message IDs by default?** IDs are application-level concerns. Zenoh provides timestamps (which are globally ordered thanks to HLC), and zenoh-ext provides sequence numbers if you need them.

**Why does `session.put()` not require declaring a publisher first?** For convenience. The declaration is an optimization (see [Publisher: Optional but Valuable](#publishing-data)), not a requirement.

---

## The Session: Root of Everything

The `Session` is the single point of contact between your application and the zenoh network. Every operation—publishing, subscribing, querying—flows through it.

### Opening a Session

**Rust:**
```rust
use zenoh::Config;

// Default config: peer mode, multicast scouting enabled
let session = zenoh::open(Config::default()).await?;

// From config file
let config = Config::from_file("/path/to/zenoh.json5")?;
let session = zenoh::open(config).await?;

// Synchronous version
let session = zenoh::open(Config::default()).wait()?;
```

**Python:**
```python
import zenoh

# Default config
session = zenoh.open(zenoh.Config())

# As context manager (preferred for automatic cleanup)
with zenoh.open(zenoh.Config()) as session:
    # session is automatically closed on exit
    ...

# From config file
config = zenoh.Config.from_file("/path/to/zenoh.json5")
session = zenoh.open(config)
```

### Session Internals

Internally, the Session maintains:

- A **wire expression ID counter**: when you declare a publisher or subscriber, the key expression string is mapped to a compact integer that travels over the wire instead of the full string. This is the "wire ID mapping" optimization.
- **Publisher, subscriber, and queryable registries**: tracked for cleanup on close
- **In-flight query tracking**: outstanding `get()` operations with their reply channels
- A **QoS configuration tree**: indexed by key expression, allowing per-topic QoS overrides from config
- **Aggregated subscriber lists**: optimization to avoid redundant declarations to routers

### Clone Semantics

In Rust, `Session` is cheaply cloneable—it wraps an `Arc` internally. Cloning a session gives you another handle to the same underlying connection. This is important for moving a session into multiple tasks or closures:

```rust
let session = zenoh::open(Config::default()).await?;
let session_clone = session.clone();

// Pass to a task
tokio::spawn(async move {
    session_clone.put("a/b/c", "hello").await.unwrap();
});

// Original still usable
session.put("x/y/z", "world").await?;
```

### Closing a Session

Sessions are closed when dropped. In Rust, the `Drop` implementation initiates cleanup. For explicit control:

```rust
// Explicit close (waits for cleanup to complete)
session.close().await?;
```

When a session closes, all outstanding subscribers, publishers, and queryables are undeclared. In-flight queries receive no further replies. The close is graceful—cleanup messages are sent to routers before the connection terminates.

---

## Key Expressions

Key expressions (KEs) are the addressing layer of zenoh. They look like path-like strings but with powerful matching semantics.

### Wildcards

| Syntax | Matches |
|--------|---------|
| `a/b/c` | Exactly `a/b/c` |
| `a/*/c` | Any single chunk: `a/x/c`, `a/foo/c` |
| `a/**/c` | Any number of chunks: `a/c`, `a/b/c`, `a/b/x/c` |
| `a/**` | Everything under `a/`: `a/`, `a/b`, `a/b/c` |
| `**` | Everything |
| `a/$*` | DSL variables (advanced; for programmatic KE construction) |

### The Intersection Model

Matching is symmetric: a subscriber on `sensors/**` receives from publishers on `sensors/temperature/room1` and `sensors/humidity/floor2`. A subscriber on `sensors/temperature/*` does NOT receive from `sensors/humidity/floor2`.

The router evaluates intersections: if a publisher's KE and subscriber's KE have any overlap (they can produce/consume the same resource), messages are routed.

### Verbatim Chunks

Chunks starting with `@` are verbatim—they match only themselves, never wildcards. This is used for system-level metadata in key expressions where you don't want `**` to accidentally match protocol-internal keys.

### Declared vs Inline Key Expressions

In Rust, key expressions can be declared on the session:

```rust
// Declare once, reuse many times (gets a wire ID)
let ke = session.declare_keyexpr("sensors/temperature/room1").await?;
// Publisher.put() only takes payload — use session.put() with the declared KE:
session.put(&ke, data).await?;

// Inline (string parsed each time, no wire ID optimization)
session.put("sensors/temperature/room1", data).await?;
```

For publishers, key expression declaration happens automatically when you call `declare_publisher()`.

---

## The Builder Pattern

Every significant operation in zenoh uses a builder. This is not incidental—it is a deliberate API design choice.

### Why Builders?

A publish operation has many optional parameters: encoding, QoS priority, congestion control, express mode, attachment, timestamp, locality. Without builders, you'd need either:

1. Functions with 8 parameters (most optional, causing combinatorial overloading)
2. A configuration struct passed to every call (verbose at callsites)
3. Multiple function variants (unmaintainable)

Builders give you a fluent API where you only specify what you care about:

```rust
// Minimal form
session.put("a/b", "hello").await?;

// With options
session.put("a/b", "hello")
    .encoding(Encoding::TEXT_PLAIN)
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Drop)
    .attachment("trace-id-xyz")
    .await?;
```

### The Resolvable / Wait Pattern

All builders implement the `Resolvable` trait. This means they can be resolved either asynchronously (`.await`) or synchronously (`.wait()`):

```rust
// Async resolution (in async context)
let subscriber = session.declare_subscriber("a/**").await?;

// Sync resolution (in sync context, no async runtime needed)
let subscriber = session.declare_subscriber("a/**").wait()?;
```

In Python, the API is synchronous by default. Async support exists but the synchronous form is more common in Python examples.

### Builder Lifecycle

Builders capture parameters by value. Nothing is sent to the network until `.await` or `.wait()` is called. This means:

```rust
let builder = session.declare_publisher("a/b")
    .priority(Priority::RealTime);
// Nothing has happened yet—no network traffic, no allocation beyond the builder struct

let publisher = builder.await?;
// NOW the key expression is declared on the network
```

---

## Publishing Data

### Session Put: The Simplest Form

```rust
// Rust: one-shot put, no declaration
session.put("demo/hello", "Hello, zenoh!").await?;

// With QoS
session.put("demo/hello", "urgent")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Drop)
    .await?;
```

```python
# Python: one-shot put
session.put("demo/hello", "Hello, zenoh!")
```

### Declared Publisher: Optimization + Wire ID

Declaring a publisher is optional but valuable when you publish to the same key expression repeatedly:

```rust
// Declare once
let publisher = session.declare_publisher("sensors/temperature/room1").await?;

// Publish many times
loop {
    publisher.put(read_temperature()).await?;
    tokio::time::sleep(Duration::from_secs(1)).await;
}
```

```python
pub = session.declare_publisher("sensors/temperature/room1")
while True:
    pub.put(read_temperature())
    time.sleep(1)
```

**Why declaration matters:** When you declare a publisher, two things happen:

1. **Wire ID mapping**: The key expression string (e.g., `"sensors/temperature/room1"`) is registered with the session and mapped to a compact integer. Subsequent `put()` calls send this integer over the wire instead of the full string. For a 30-character key expression, this saves 30 bytes per message—significant at high frequencies.

2. **Router pre-routing**: Routers learn that this key expression will be published. They can pre-compute routing tables, establishing the path from publisher to all matching subscribers before the first message arrives. Without declaration, the first message may cause a routing table miss and be delayed.

**The optimization kicks in** when you publish repeatedly to the same key expression. For one-shot puts, the overhead of declaration isn't worth it.

### Publisher QoS

QoS can be set at declaration time (applies to all publications from this publisher) or overridden per-publication:

```rust
// Declare with default QoS
let publisher = session
    .declare_publisher("alerts/critical")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Block)
    .reliability(Reliability::Reliable)
    .await?;

// Per-publication override of encoding and attachment
publisher
    .put(alert_data)
    .encoding(Encoding::APPLICATION_JSON)
    .attachment(correlation_id)
    .await?;
```

### Publisher Delete

Publishers can also send delete messages (tombstones) to inform storage backends and subscribers that data at this key has been removed:

```rust
publisher.delete().await?;

// Or via session directly
session.delete("sensors/temperature/room1").await?;
```

---

## Subscribing to Data

### Basic Subscriber

**Rust (async, FIFO channel—default):**
```rust
let subscriber = session.declare_subscriber("sensors/**").await?;

while let Ok(sample) = subscriber.recv_async().await {
    println!("Received on {}: {:?}",
        sample.key_expr(),
        sample.payload().try_to_string());
}
```

**Rust (callback):**
```rust
let _subscriber = session
    .declare_subscriber("sensors/**")
    .callback(|sample| {
        println!("Received on {}: {:?}",
            sample.key_expr(),
            sample.payload().try_to_string());
    })
    .await?;
// _subscriber must be kept alive; dropping it undeclares the subscription
```

**Python (callback—most common):**
```python
def on_sample(sample: zenoh.Sample):
    print(f"Received on {sample.key_expr}: {sample.payload.to_string()}")

sub = session.declare_subscriber("sensors/**", on_sample)

# Keep running
while True:
    time.sleep(1)
```

### Sample Structure

Every received message is a `Sample` containing:

| Field | Type | Description |
|-------|------|-------------|
| `key_expr()` | `KeyExpr` | The concrete key expression this sample was published on |
| `payload()` | `ZBytes` | The message payload (opaque bytes) |
| `kind()` | `SampleKind` | `Put` or `Delete` |
| `encoding()` | `Encoding` | MIME-like encoding metadata |
| `timestamp()` | `Option<Timestamp>` | HLC timestamp (may be absent if not set by publisher) |
| `attachment()` | `Option<ZBytes>` | Optional opaque metadata attached to the message |

### Locality: Filtering by Source

Subscribers can filter messages by where they originate:

```rust
use zenoh::sample::Locality;

// Only receive from publishers in the same session (same process)
let sub = session
    .declare_subscriber("sensors/**")
    .allowed_origin(Locality::SessionLocal)
    .await?;

// Only receive from remote publishers
let sub = session
    .declare_subscriber("sensors/**")
    .allowed_origin(Locality::Remote)
    .await?;

// Default: receive from everyone
let sub = session
    .declare_subscriber("sensors/**")
    .allowed_origin(Locality::Any)
    .await?;
```

---

## Handler Types: FIFO, Ring, and Callback

The handler is how zenoh delivers incoming messages to your application. Three strategies are provided, each making different tradeoffs between latency, throughput, and memory.

### The Default: FIFO Channel

When you call `declare_subscriber()` without specifying a handler, you get a `FifoChannel` with the default capacity (256 messages). The subscriber object returned is the receiver side of this channel.

```rust
// Default: FIFO with 256 capacity
let subscriber = session.declare_subscriber("a/**").await?;
// subscriber is a FifoChannelHandler<Sample>

// Receive methods:
subscriber.recv_async().await?;        // async wait for next message
subscriber.recv()?;                    // blocking wait
subscriber.recv_timeout(Duration::from_secs(1))?; // blocking with timeout
subscriber.try_recv()?;               // non-blocking, returns Ok(None) if empty
```

**What FIFO guarantees:**
- Messages are delivered in the order they arrive
- No messages are dropped (unless the sender—Zenoh's receive thread—drops them due to the channel being full)
- **Backpressure**: if your consumer is slower than the publisher, the FIFO fills up and blocks the zenoh receive thread. This is intentional—it applies backpressure to the entire delivery pipeline.

**The backpressure risk:** A slow consumer can hold up other subscribers on the same session by blocking the shared zenoh receive thread. This is why the default capacity exists: it gives your consumer a 256-message buffer to absorb bursts, but if you consistently can't keep up, you should either increase capacity or switch to a callback or ring channel.

**Custom capacity:**
```rust
use zenoh::handlers::FifoChannel;

let subscriber = session
    .declare_subscriber("high-volume/**")
    .with(FifoChannel::new(1024))  // 1024-message buffer
    .await?;
```

### Ring Channel: Drop-Oldest Strategy

The ring channel never blocks. When full, it drops the oldest message to make room for the newest. This is the right choice when you only care about the **current state** of something, not a complete history.

```rust
use zenoh::handlers::RingChannel;

let subscriber = session
    .declare_subscriber("sensors/temperature/**")
    .with(RingChannel::new(10))  // keep only last 10 measurements
    .await?;

loop {
    // Drain all available samples, then sleep
    while let Ok(Some(sample)) = subscriber.try_recv() {
        println!("Latest temp: {:?}", sample.payload().try_to_string());
    }
    tokio::time::sleep(Duration::from_secs(5)).await;
}
```

```python
import zenoh

sub = session.declare_subscriber("sensors/temperature/**", zenoh.handlers.RingChannel(10))

while True:
    time.sleep(5)
    # Drain everything accumulated in the ring
    while True:
        sample = sub.try_recv()
        if sample is None:
            break
        print(f"Latest: {sample.payload.to_string()}")
```

**When to use ring channel:**
- Sensor telemetry where only the latest value matters (temperature, position, status)
- Display applications that refresh periodically
- Any application that can tolerate missed intermediate values

**When NOT to use ring channel:**
- Command streams where every command must execute (motor control, actuator commands)
- Financial data where every price update matters
- Anything that requires ordered processing

### Callback Handler: Lowest Latency

Callbacks are invoked directly in zenoh's receive thread, synchronously, before the message is placed anywhere. This gives the lowest possible latency—no channel, no copy, no context switch.

```rust
let _subscriber = session
    .declare_subscriber("control/**")
    .callback(|sample| {
        // Called synchronously in receive thread
        // MUST return quickly
        // MUST NOT block (no I/O, no mutex with long hold times)
        update_control_state(sample.payload());
    })
    .await?;
```

**The critical constraint:** Your callback executes on zenoh's internal receive thread. If it blocks or takes too long, it delays ALL subsequent message delivery from that session—not just for this subscriber. This means:

- No blocking I/O (no file writes, no database queries, no network calls)
- No heavy computation (no FFT, no image processing)
- No waiting on mutexes held by other threads
- Typically: update a shared atomic, push to a lockfree queue, or wake an event loop

**For mutable closures, use `callback_mut`:**
```rust
let mut count = 0;
let _subscriber = session
    .declare_subscriber("a/**")
    .callback_mut(move |sample| {
        count += 1;
        println!("Message #{}: {:?}", count, sample.key_expr());
    })
    .await?;
// callback_mut wraps the FnMut in a Mutex, guaranteeing no concurrent calls
```

**Python callbacks** use the same model—the callback is invoked in a background thread, and the same constraints apply:

```python
import threading

state = {"count": 0}
lock = threading.Lock()

def handler(sample: zenoh.Sample):
    with lock:  # Keep lock duration minimal
        state["count"] += 1
        # Don't do I/O here

sub = session.declare_subscriber("a/**", handler)
```

### Choosing a Handler

| Scenario | Handler | Reason |
|----------|---------|--------|
| Processing every message in order | FIFO channel | Backpressure prevents loss |
| Only latest value matters | Ring channel | No blocking, drops stale data |
| Lowest latency, simple action | Callback | No channel overhead |
| Slow consumer, high-volume stream | Ring channel | Avoids blocking receive thread |
| Reliable command processing | FIFO channel | Nothing dropped |
| Multiple subscribers, event loop | FIFO channel on main thread | Consolidate into one recv loop |

---

## Querying Data: The Get/Queryable Pattern

The get/queryable pattern is zenoh's request-reply mechanism. Unlike HTTP request-reply, it is **many-to-many**: a single `get()` can receive replies from multiple queryables, storage backends, and live peers simultaneously.

### Issuing a Query: `session.get()`

```rust
use zenoh::query::QueryTarget;
use std::time::Duration;

let replies = session
    .get("sensors/**")
    .target(QueryTarget::BestMatching)
    .timeout(Duration::from_secs(5))
    .await?;

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Reply: {} = {:?}",
            sample.key_expr(),
            sample.payload().try_to_string()),
        Err(err) => println!("Error reply: {:?}", err.payload().try_to_string()),
    }
}
```

```python
replies = session.get("sensors/**", timeout=5.0)
for reply in replies:
    try:
        print(f"Reply: {reply.ok.key_expr} = {reply.ok.payload.to_string()}")
    except:
        print(f"Error: {reply.err.payload.to_string()}")
```

The `replies` value is itself a channel (FIFO by default, or ring if you specify `.with(RingChannel::new(N))`). You iterate it until it closes—which happens when the timeout expires or all queryables have replied.

### Query Targets

The `target` parameter controls which queryables receive and respond to the query:

| Target | Meaning |
|--------|---------|
| `BestMatching` | Default. Routes to one "best" queryable per matched key expression. What "best" means is router-dependent (usually closest complete queryable). |
| `All` | Routes to ALL queryables matching the key expression. Use when you want responses from every peer—e.g., collecting status from all nodes. |
| `AllComplete` | Routes to ALL queryables declared with `.complete(true)`. Use when you want authoritative responses only. |

### Declaring a Queryable

A queryable registers your application as a responder for queries matching a key expression:

```rust
let queryable = session
    .declare_queryable("sensors/**")
    .complete(true)  // This queryable has ALL data for sensors/**
    .await?;

while let Ok(query) = queryable.recv_async().await {
    println!("Query received: {}", query.selector());

    // Reply with data
    query.reply("sensors/temperature/room1", 22.5_f32).await?;
    query.reply("sensors/temperature/room2", 23.1_f32).await?;
    // Channel closes when query is dropped = no more replies
}
```

```python
queryable = session.declare_queryable("sensors/**", complete=True)

while True:
    with queryable.recv() as query:
        print(f"Query received: {query.selector}")
        query.reply("sensors/temperature/room1", "22.5")
        # Context manager handles reply finalization on exit
```

### The `complete` Flag

Declaring a queryable with `.complete(true)` advertises to the routing layer that this queryable can answer **all** queries for its key expression—it has complete data. This affects routing:

- `QueryTarget::AllComplete` only routes to complete queryables
- `QueryTarget::BestMatching` prefers complete queryables

If you're implementing a storage backend, set `complete(true)`. If you're implementing a live responder that only knows about currently-active entities, leave it `false`.

### Query Selector: Key Expression + Parameters

A query can include a selector that extends the key expression with parameters:

```
sensors/temperature/**?starttime=1h&stoptime=now
```

The part after `?` is the **selector parameters**. Queryables receive the full selector:

```rust
while let Ok(query) = queryable.recv_async().await {
    let ke = query.key_expr();          // "sensors/temperature/**"
    let params = query.parameters();   // "starttime=1h&stoptime=now"
    let selector = query.selector();   // Full selector
    ...
}
```

This is how time-range queries work in storage backends—the `_time` parameter is a zenoh convention that storage plugins interpret.

### Reply Errors

Queryables can reply with an error instead of data:

```rust
if !can_answer_query(&query) {
    query.reply_err("Not available").await?;
}
```

The caller receives this as a `Reply` where `reply.result()` is `Err(ReplyError)`.

---

## Consolidation Modes

When a `get()` routes through multiple hops and there are multiple copies of a queryable (or storage) in the network, you might receive duplicate replies. Consolidation modes control how duplicates are handled:

| Mode | Meaning | When to Use |
|------|---------|-------------|
| `None` | No consolidation; forward all replies | Topology discovery, want all responses |
| `Monotonic` | Forward only if newer than previous from same keyexpr | Reduce duplicates, still want progress |
| `Latest` | Keep only the most recent reply per keyexpr | Storage queries where only newest matters |

```rust
use zenoh::query::ConsolidationMode;

let replies = session
    .get("sensors/**")
    .consolidation(ConsolidationMode::Latest)
    .await?;
```

**Example:** You have three storage replicas each holding temperature data. With `ConsolidationMode::None`, you get three replies for `sensors/temperature/room1`. With `ConsolidationMode::Latest`, you get one—the most recent across all three replicas.

For topology inspection (asking "what queryables are out there?"), use `ConsolidationMode::None`—you want every response.

---

## The Storage Pattern: Combining Subscriber + Queryable

The most powerful zenoh pattern is implementing an in-memory storage that serves both live and historical data. This is exactly what the `z_storage.rs` example demonstrates:

**Rust:**
```rust
use std::collections::HashMap;
use futures::select;
use zenoh::{key_expr::keyexpr, sample::{Sample, SampleKind}};

let key_expr = "demo/example/**";
let mut stored: HashMap<String, Sample> = HashMap::new();

let session = zenoh::open(Config::default()).await?;

// Subscribe to live data
let subscriber = session.declare_subscriber(key_expr).await?;

// Answer queries from stored data
let queryable = session
    .declare_queryable(key_expr)
    .complete(true)
    .await?;

loop {
    select!(
        // Handle incoming publications
        sample = subscriber.recv_async() => {
            let sample = sample?;
            match sample.kind() {
                SampleKind::Delete => { stored.remove(&sample.key_expr().to_string()); }
                SampleKind::Put    => { stored.insert(sample.key_expr().to_string(), sample); }
            }
        },
        // Handle incoming queries
        query = queryable.recv_async() => {
            let query = query?;
            for (key, sample) in &stored {
                if query.key_expr().intersects(unsafe { keyexpr::from_str_unchecked(key) }) {
                    query.reply(sample.key_expr().clone(), sample.payload().clone()).await?;
                }
            }
        }
    );
}
```

This pattern is the foundation of all zenoh storage backends. The subscriber keeps the store synchronized with live data; the queryable serves historical data to late joiners and recovery scenarios.

---

## Async vs Sync API

Zenoh provides both async and sync APIs, and choosing between them matters for both correctness and performance.

### When to Use Async

Use async when:
- Your application is already Tokio-based
- You have many concurrent operations (many subscribers, many publishers)
- You want the runtime to handle concurrency via task scheduling rather than threads
- You're building a high-throughput data pipeline

```rust
#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    let sub1 = session.declare_subscriber("a/**").await?;
    let sub2 = session.declare_subscriber("b/**").await?;

    // Both subscribers handled in one async task, no extra threads
    loop {
        tokio::select! {
            Ok(s) = sub1.recv_async() => handle_a(s),
            Ok(s) = sub2.recv_async() => handle_b(s),
        }
    }
}
```

### When to Use Sync

Use sync when:
- You have a simpler threads-based application
- You're integrating zenoh into an existing synchronous codebase
- You're in a context where running a full async runtime is undesirable

```rust
fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).wait()?;
    let subscriber = session.declare_subscriber("sensors/**").wait()?;

    // Blocking receive loop
    while let Ok(sample) = subscriber.recv() {
        println!("Got: {}", sample.key_expr());
    }
    Ok(())
}
```

### Thread Count Implications

Async reduces thread count because the Tokio runtime uses a threadpool shared across all async tasks. Without async:
- Each blocking `recv()` loop needs its own thread
- N subscribers = N threads
- Plus zenoh's internal threads

With async:
- All `recv_async()` loops share the runtime's threads
- N subscribers can all run on 2-4 threads
- The select! macro multiplexes them efficiently

---

## Thread Minimization

A practical case study: reducing a moderate-complexity zenoh application from 22 threads to 5.

### Starting Point: Thread-per-Subscriber

The naive approach allocates one thread per subscriber:

```rust
// BEFORE: 22 threads for 10 subscribers + overhead
let session = zenoh::open(Config::default()).wait()?;

for topic in &topics {
    let session_clone = session.clone();
    let topic = topic.clone();
    std::thread::spawn(move || {
        let sub = session_clone.declare_subscriber(&topic).wait().unwrap();
        while let Ok(sample) = sub.recv() {
            process(sample);
        }
    });
}
// 10 subscriber threads + zenoh internal threads + main = ~22 threads
```

### Step 1: Consolidate to One Async Event Loop

Replace per-thread blocking receives with a single async task:

```rust
// AFTER STEP 1: one thread handles all subscribers
#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let mut subscribers = Vec::new();
    for topic in &topics {
        let sub = session.declare_subscriber(topic).await.unwrap();
        subscribers.push(sub);
    }

    // Single select loop handles all subscribers
    loop {
        // With futures::select or tokio::select over multiple recv_async() calls
        futures::select! {
            Ok(s) = subscribers[0].recv_async().fuse() => process_0(s),
            Ok(s) = subscribers[1].recv_async().fuse() => process_1(s),
            // ...
        }
    }
}
// Tokio runtime uses 2-4 threads + zenoh internal = ~5 threads
```

### Step 2: Use Callbacks for Fire-and-Forget Operations

If some subscribers only need to update shared state and don't need a loop, callbacks eliminate even the select overhead:

```rust
let shared_state = Arc::new(Mutex::new(State::default()));

// Callback: no channel, no thread, inline execution
let _sub = session
    .declare_subscriber("state/**")
    .callback({
        let state = shared_state.clone();
        move |sample| {
            if let Ok(mut s) = state.try_lock() {
                s.update(sample.payload());
            }
            // Non-blocking: try_lock, not lock
        }
    })
    .await?;
```

### Step 3: Use FIFO Channel on Main Thread for Ordered Processing

For subscribers that need ordered processing, use FIFO but drain them on main:

```rust
let sub_a = session.declare_subscriber("commands/**").await?;
let sub_b = session.declare_subscriber("feedback/**").await?;

// One event loop, zero extra threads
loop {
    tokio::select! {
        Ok(cmd) = sub_a.recv_async() => execute_command(cmd),
        Ok(fb)  = sub_b.recv_async() => update_feedback(fb),
    }
}
```

### Summary: Thread Reduction Playbook

| Technique | Thread Saving |
|-----------|--------------|
| Replace thread-per-subscriber with async select | Eliminate N-1 subscriber threads |
| Use callbacks for stateless updates | Remove channels for simple operations |
| Consolidate to tokio::main | Share runtime thread pool |
| Use `try_recv` polling on ring channels | Replace blocking wait threads |

Target: with 10 subscribers in a Tokio application, you should need ~3-5 threads total (tokio runtime workers + zenoh internals), not 10-20.

---

## Message Attachments

Attachments are opaque byte payloads that travel alongside the main message payload. They're intended for metadata that the routing layer doesn't need to inspect—trace IDs, hop counts, correlation IDs, custom headers.

### Attaching Metadata at Publish Time

**Rust:**
```rust
// Attach a string
publisher
    .put(sensor_reading)
    .attachment("trace-id: abc-123")
    .await?;

// Attach structured bytes (serialize yourself)
let metadata = serde_json::to_vec(&TraceContext {
    trace_id: "abc-123",
    span_id: "def-456",
})?;
publisher
    .put(sensor_reading)
    .attachment(ZBytes::from(metadata))
    .await?;

// Also works on session.put()
session
    .put("sensors/temp", 22.5_f32)
    .attachment("source: sensor-node-42")
    .await?;
```

**Python:**
```python
pub.put(sensor_reading, attachment="trace-id: abc-123")
```

### Reading Attachments at Subscribe Time

**Rust:**
```rust
let sub = session.declare_subscriber("sensors/**").await?;

while let Ok(sample) = sub.recv_async().await {
    let payload = sample.payload().try_to_string()?;

    if let Some(att) = sample.attachment() {
        let att_str = att.try_to_string().unwrap_or("(binary)".into());
        println!("Payload: {}, Attachment: {}", payload, att_str);
    }
}
```

**Python:**
```python
def on_sample(sample: zenoh.Sample):
    print(f"Payload: {sample.payload.to_string()}")
    if sample.attachment is not None:
        print(f"Attachment: {sample.attachment.to_string()}")
```

### Use Cases

**Request correlation:** When a controller sends a command and wants to correlate it with a feedback message, embed a UUID as an attachment:

```rust
// Publisher (controller)
let req_id = Uuid::new_v4().to_string();
session.put("commands/motor/1", command).attachment(req_id).await?;

// Subscriber (feedback handler) reads the req_id back
// and matches it against outstanding requests
```

**Distributed tracing:** Propagate OpenTelemetry trace context through zenoh messages without polluting the payload format.

**Hop counting:** A router or forwarder node increments an attachment counter to detect routing loops.

**Schema versioning:** Embed a schema version tag so consumers can parse the payload correctly even as schemas evolve.

---

## Timestamps

Zenoh assigns a globally-ordered timestamp to every message using a **Hybrid Logical Clock (HLC)**. HLC timestamps combine wall-clock time with a logical counter, giving you timestamps that are:

1. **Monotonically increasing** within a session (never go backward)
2. **Causally consistent** across sessions (if A caused B, timestamp(A) < timestamp(B))
3. **Approximately synchronized** with wall clock (within NTP precision)

### Timestamp Format

A zenoh timestamp consists of:
- **NTP64 time**: a 64-bit NTP timestamp (seconds since Jan 1, 1900, with sub-second fraction in the lower 32 bits)
- **ID**: the `ZenohId` of the session that generated the timestamp

```rust
if let Some(ts) = sample.timestamp() {
    let time = ts.get_time();        // &NTP64
    let id = ts.get_id();           // &ZenohId

    // Convert NTP64 to SystemTime
    let secs_since_unix = time.as_secs() - 2_208_988_800; // NTP epoch offset
    println!("Timestamp: {} from session {:?}", secs_since_unix, id);
}
```

### Automatic vs Manual Timestamps

By default, when you publish without specifying a timestamp, zenoh may or may not assign one automatically (behavior depends on configuration). To guarantee a timestamp is attached:

```rust
// Manually set a timestamp
let ts = session.new_timestamp();  // generates a fresh HLC timestamp
session.put("a/b/c", data)
    .timestamp(ts)
    .await?;
```

Storage backends typically require timestamps to implement `ConsolidationMode::Latest` correctly—they compare timestamps to decide which of several versions of the same key is newest.

### Reading Timestamps

**Rust:**
```rust
while let Ok(sample) = sub.recv_async().await {
    match sample.timestamp() {
        Some(ts) => println!("Timestamped: {:?}", ts),
        None     => println!("No timestamp"),
    }
}
```

**Python:**
```python
def on_sample(sample: zenoh.Sample):
    if sample.timestamp is not None:
        print(f"Timestamp: {sample.timestamp}")
```

### Why Timestamps Matter

**Storage ordering:** A storage backend may receive the same key from two publishers simultaneously. Without timestamps, the ordering is arbitrary. With HLC timestamps, the storage can always keep the "latest" value in a causally consistent way.

**Time-range queries:** Storage backends interpret the `_time` selector parameter using timestamps:
```python
# Query data from the last hour
replies = session.get("sensors/temperature/**?_time=[now(-1h);now()]")
```

**Event ordering:** When debugging a distributed system, timestamps let you reconstruct the causal order of events even if log entries arrive out of order.

---

## QoS: Priority, Reliability, Congestion Control

QoS (Quality of Service) parameters control how zenoh treats messages at the transport level.

### Priority

Priority affects message scheduling when the network or router is under load. Higher-priority messages are processed first.

```rust
use zenoh::qos::Priority;

let publisher = session
    .declare_publisher("alerts/critical")
    .priority(Priority::RealTime)          // Highest
    .await?;

let publisher2 = session
    .declare_publisher("telemetry/verbose")
    .priority(Priority::Background)        // Lowest
    .await?;
```

| Priority | Value | Use Case |
|----------|-------|----------|
| `RealTime` | 1 | Control commands, safety signals |
| `InteractiveHigh` | 2 | UI updates, operator feedback |
| `InteractiveLow` | 3 | Non-urgent UI |
| `DataHigh` | 4 | Sensor data, default for most apps |
| `Data` | 5 | Default priority |
| `DataLow` | 6 | Bulk transfer |
| `Background` | 7 | Logging, diagnostics |

### Congestion Control

Controls behavior when the network is congested:

```rust
use zenoh::qos::CongestionControl;

// Drop: discard message if network buffer is full (best-effort)
publisher.put(data)
    .congestion_control(CongestionControl::Drop)
    .await?;

// Block: wait until network can accept the message (reliable delivery)
publisher.put(data)
    .congestion_control(CongestionControl::Block)
    .await?;
```

- **Drop**: Never blocks the publisher. Messages may be lost under congestion. Appropriate for high-frequency sensor data where a dropped sample is acceptable.
- **Block**: Publisher blocks until the network can absorb the message. Ensures delivery but can stall your publish loop under heavy load. Appropriate for commands or infrequent critical data.

### Reliability

The `reliability` parameter (currently unstable API) hints to the transport whether messages should be delivered reliably:

```rust
#[cfg(feature = "unstable")]
use zenoh::qos::Reliability;

let publisher = session
    .declare_publisher("commands/**")
    .reliability(Reliability::Reliable)     // Request reliable delivery
    .await?;
```

Note: Zenoh's reliability semantics depend on the underlying transport. Over multicast UDP, reliability is best-effort. Over unicast connections, retransmission is available.

### Express Mode

Express mode disables batching—the message is sent immediately without waiting to fill a batch buffer:

```rust
session.put("control/emergency", "STOP")
    .express(true)
    .await?;
```

Without express mode, zenoh may hold a message briefly to batch it with other outgoing messages for efficiency. Express mode trades throughput for latency: appropriate for infrequent, latency-critical messages.

---

## Locality Control

Locality controls whether a publication is visible only within the session, only to remote peers, or both.

```rust
use zenoh::sample::Locality;

// Publish to all (default)
publisher.put(data)
    .allowed_destination(Locality::Any)
    .await?;

// Publish only to subscribers in the same session (loopback only)
publisher.put(data)
    .allowed_destination(Locality::SessionLocal)
    .await?;

// Publish only to remote subscribers (not same-session subscribers)
publisher.put(data)
    .allowed_destination(Locality::Remote)
    .await?;
```

Similarly, subscribers can filter by source:

```rust
// Only receive from same session
let sub = session.declare_subscriber("a/**")
    .allowed_origin(Locality::SessionLocal)
    .await?;

// Only receive from remote peers
let sub = session.declare_subscriber("a/**")
    .allowed_origin(Locality::Remote)
    .await?;
```

**Use cases:**
- `SessionLocal` publish + `SessionLocal` subscribe: in-process event bus, zero network traffic
- `Remote` subscribe: ignore your own publications (prevent echo loops in forwarding scenarios)
- `Any`: default, full location transparency

---

## Matching Status

Publishers can query whether any matching subscribers currently exist. This is useful to avoid expensive serialization and publication when nobody is listening.

### Checking Matching Status

```rust
let publisher = session.declare_publisher("sensors/camera/frame").await?;

// Check before expensive encode
if publisher.matching_status().await?.matching() {
    let frame = capture_and_encode_frame()?;  // expensive
    publisher.put(frame).await?;
}
```

### Matching Listener

Instead of polling, register a callback to be notified when subscriber presence changes:

**Rust:**
```rust
publisher
    .matching_listener()
    .callback(|status| {
        if status.matching() {
            println!("Someone is listening — start producing data");
        } else {
            println!("No listeners — stop producing data");
        }
    })
    .background()
    .await?;
```

**Python:**
```python
def on_matching_status(status: zenoh.MatchingStatus):
    if status.matching:
        print("Subscribers present — producing")
    else:
        print("No subscribers — pausing")

pub.declare_matching_listener(on_matching_status)
```

The `.background()` call makes the listener persist as long as the publisher exists, without needing to hold a handle to the listener.

**Important:** Matching status reflects locally-known subscribers. If the router has subscribers the local session hasn't been notified about yet (timing windows), matching status may temporarily return false. Use this as an optimization hint, not a guarantee.

---

## The zenoh-ext Extension Library

The `zenoh-ext` crate provides higher-level patterns built on top of the core API. These are not part of the core protocol but reflect common application needs.

### Publication Cache

Caches recent publications on a key expression and serves them to late-joining subscribers:

```rust
use zenoh_ext::SessionExt;

let pub_cache = session
    .declare_publication_cache("sensors/**")
    .history(100)  // Cache last 100 publications per key
    .await?;

// Now late-joining subscribers that do session.get("sensors/**")
// will receive the last 100 publications
```

### Querying Subscriber

A subscriber that, when first created, issues a `get()` to catch up on missed data, then seamlessly transitions to receiving live publications:

```rust
use zenoh_ext::{SessionExt, FetchingSubscriber};

let sub = session
    .declare_querying_subscriber("sensors/**")
    .query_timeout(Duration::from_secs(5))
    .await?;

// sub behaves like a normal subscriber but first delivers
// historical data from storage, then live data
while let Ok(sample) = sub.recv_async().await {
    process(sample);
}
```

This solves the "missed data during startup" problem without requiring application-level logic.

### Advanced Publisher and Subscriber

The `AdvancedPublisher` and `AdvancedSubscriber` add:
- **Sequence numbers**: detect and report missed messages
- **Recovery**: request retransmission of missed messages
- **Timestamp-based ordering**: reorder out-of-order deliveries

```rust
use zenoh_ext::{AdvancedPublisherBuilderExt, AdvancedSubscriberBuilderExt};

let pub = session
    .declare_publisher("reliable/stream")
    .advanced()
    .cache(1000)  // Keep 1000 samples for recovery
    .await?;

let sub = session
    .declare_subscriber("reliable/stream")
    .advanced()
    .history(zenoh_ext::HistoryConfig::default())
    .recovery(zenoh_ext::RecoveryConfig::default())
    .await?;
```

### Serialization Utilities

`zenoh-ext` provides serialization helpers for common types:

```rust
use zenoh_ext::{z_serialize, z_deserialize};

// Serialize a struct
let bytes = z_serialize(&my_struct)?;
session.put("data/key", bytes).await?;

// Deserialize from a sample
let received: MyStruct = z_deserialize(sample.payload())?;
```

---

## Complete Examples

### Rust: Minimal Pub/Sub

```rust
use std::time::Duration;
use zenoh::Config;

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    // Publisher
    let publisher = session.declare_publisher("demo/hello").await?;

    // Subscriber
    let subscriber = session.declare_subscriber("demo/**").await?;

    // Publish in background task
    tokio::spawn({
        let publisher = publisher.clone();
        async move {
            let mut i = 0u32;
            loop {
                publisher.put(format!("Message {i}")).await.unwrap();
                i += 1;
                tokio::time::sleep(Duration::from_secs(1)).await;
            }
        }
    });

    // Receive loop
    while let Ok(sample) = subscriber.recv_async().await {
        println!("Received on {}: {:?}",
            sample.key_expr(),
            sample.payload().try_to_string());
    }

    Ok(())
}
```

### Python: Minimal Pub/Sub

```python
import time
import threading
import zenoh

def main():
    with zenoh.open(zenoh.Config()) as session:
        pub = session.declare_publisher("demo/hello")

        def on_sample(sample: zenoh.Sample):
            print(f"Received on {sample.key_expr}: {sample.payload.to_string()}")

        _sub = session.declare_subscriber("demo/**", on_sample)

        # Publish in main loop
        i = 0
        while True:
            pub.put(f"Message {i}")
            i += 1
            time.sleep(1)

main()
```

### Rust: Query/Reply

```rust
use zenoh::{Config, query::QueryTarget};
use std::time::Duration;

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    // Queryable: acts as a data source
    let queryable = session
        .declare_queryable("data/**")
        .complete(true)
        .await?;

    // Handle queries in background
    tokio::spawn(async move {
        while let Ok(query) = queryable.recv_async().await {
            println!("Query for: {}", query.selector());
            query.reply("data/temperature", "22.5°C").await.unwrap();
        }
    });

    // Give queryable time to register
    tokio::time::sleep(Duration::from_millis(100)).await;

    // Querier: ask for data
    let replies = session
        .get("data/**")
        .target(QueryTarget::AllComplete)
        .timeout(Duration::from_secs(5))
        .await?;

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            println!("Reply: {} = {:?}",
                sample.key_expr(),
                sample.payload().try_to_string());
        }
    }

    Ok(())
}
```

---

## Quick Reference

### API Surface

| Operation | Rust | Python |
|-----------|------|--------|
| Open session | `zenoh::open(config).await?` | `zenoh.open(config)` |
| One-shot put | `session.put(ke, data).await?` | `session.put(ke, data)` |
| Declare publisher | `session.declare_publisher(ke).await?` | `session.declare_publisher(ke)` |
| Publish | `pub.put(data).await?` | `pub.put(data)` |
| Delete | `session.delete(ke).await?` | `session.delete(ke)` |
| Declare subscriber | `session.declare_subscriber(ke).await?` | `session.declare_subscriber(ke, handler)` |
| Receive async | `sub.recv_async().await` | N/A (Python uses callbacks) |
| Receive sync | `sub.recv()` | `sub.recv()` |
| Try receive | `sub.try_recv()` | `sub.try_recv()` |
| Query | `session.get(selector).await?` | `session.get(selector)` |
| Declare queryable | `session.declare_queryable(ke).await?` | `session.declare_queryable(ke)` |
| Reply to query | `query.reply(ke, data).await?` | `query.reply(ke, data)` |
| Reply error | `query.reply_err(msg).await?` | `query.reply_err(msg)` |

### Handler Selection

```
High frequency, only latest matters?  → RingChannel
Must process every message in order?  → FifoChannel (default)
Lowest latency, simple callback?      → .callback(|s| ...)
Multiple subscribers, one thread?     → FifoChannel + async select!
```

### Optimization Checklist

- [ ] Declare publishers when publishing repeatedly to the same key expression
- [ ] Use `RingChannel` for sensors/telemetry where only latest matters
- [ ] Use `callback` for stateless updates to shared state
- [ ] Use `async`/`await` + `select!` to consolidate multiple subscribers onto one thread
- [ ] Set `priority(Priority::RealTime)` for control messages
- [ ] Set `congestion_control(CongestionControl::Drop)` for high-frequency, loss-tolerant data
- [ ] Check `matching_status()` before expensive serialization
- [ ] Use `complete(true)` on queryables that own all data for their key expression

## See Also

- [Key Expressions Guide](key-expressions-guide.md) — the addressing language used throughout the pub/sub and query APIs
- [Node Types Guide](node-types-guide.md) — how session mode (router/peer/client) affects the programming model
- [Quickstart Recipes](quickstart-recipes.md) — minimal working code examples for the most common patterns
- [Serialization Complete Guide](serialization-complete-guide.md) — how to encode and decode payloads in the ZBytes type
