# Zenoh Queryable: Complete Guide

Zenoh's query/reply pattern is implemented through three components: **Queryables** (answerers), **Queries** (requests), and **Replies** (responses). This guide covers all aspects of the pattern, from basic usage to advanced routing strategies.

---

## Table of Contents

- [Conceptual Overview](#conceptual-overview)
- [Declaring a Queryable](#declaring-a-queryable)
  - [Rust](#rust)
  - [Rust (callback-based)](#rust-callback-based)
  - [Python](#python)
  - [Explicit Undeclaration](#explicit-undeclaration)
- [Complete vs. Incomplete Queryables](#complete-vs-incomplete-queryables)
  - [complete(true) — Authoritative](#completetrue-authoritative)
  - [complete(false) — Non-Authoritative (Default)](#completefalse-non-authoritative-default)
  - [How completeness affects routing](#how-completeness-affects-routing)
- [Query Targets](#query-targets)
  - [BestMatching (Default)](#bestmatching-default)
  - [All](#all)
  - [AllComplete](#allcomplete)
- [ConsolidationMode (Deduplication)](#consolidationmode-deduplication)
  - [Auto (Default)](#auto-default)
  - [None](#none)
  - [Monotonic](#monotonic)
  - [Latest](#latest)
  - [Where consolidation happens](#where-consolidation-happens)
- [The Query Object](#the-query-object)
  - [Key Expression](#key-expression)
  - [Selector (Key Expression + Parameters)](#selector-key-expression-parameters)
  - [Payload](#payload)
  - [Attachment](#attachment)
  - [QoS (unstable feature)](#qos-unstable-feature)
  - [accepts_replies](#accepts_replies)
- [Selectors and Parameters](#selectors-and-parameters)
  - [Accessing Parameters in a Queryable](#accessing-parameters-in-a-queryable)
  - [Standard Parameters](#standard-parameters)
  - [Sending a Query with Parameters](#sending-a-query-with-parameters)
- [Reply Types](#reply-types)
  - [reply() — Successful Data Reply](#reply-successful-data-reply)
  - [reply_del() — Delete Reply](#reply_del-delete-reply)
  - [reply_err() — Error Reply](#reply_err-error-reply)
  - [Receiving Replies](#receiving-replies)
  - [Reply struct](#reply-struct)
  - [ReplyError struct](#replyerror-struct)
  - [ResponseFinal](#responsefinal)
- [Timeout Behavior](#timeout-behavior)
  - [Default timeout](#default-timeout)
  - [Setting timeout](#setting-timeout)
- [Querier vs. session.get()](#querier-vs-sessionget)
  - [session.get() — Ad-hoc Query](#sessionget-ad-hoc-query)
  - [declare_querier() — Declared Querier](#declare_querier-declared-querier)
- [Complete Working Examples](#complete-working-examples)
  - [1. Basic Queryable Replying with Static Data](#1-basic-queryable-replying-with-static-data)
  - [2. Queryable That Implements _time Range Filtering](#2-queryable-that-implements-_time-range-filtering)
  - [3. Queryable That Returns ReplyError for Unknown Keys](#3-queryable-that-returns-replyerror-for-unknown-keys)
  - [4. Fan-Out Query: All Target + None Consolidation](#4-fan-out-query-all-target-none-consolidation)
  - [5. Storage-Style Query: AllComplete + Latest Consolidation](#5-storage-style-query-allcomplete-latest-consolidation)
  - [6. Using Querier for Repeated Queries to the Same KE](#6-using-querier-for-repeated-queries-to-the-same-ke)
- [Summary: Quick Reference](#summary-quick-reference)


---


## Conceptual Overview

The query/reply pattern works as follows:

```
Getter (session.get / Querier.get)
   |
   | Query (key expression + parameters + optional payload)
   v
Router selects target queryable(s) based on:
   - Key expression intersection
   - QueryTarget (BestMatching / All / AllComplete)
   - complete flag on registered queryables
   |
   v
Queryable(s) receive Query
   |
   | Reply (Put/Delete sample, or ReplyError)
   v
Getter receives replies until timeout
```

The query/reply pattern is the Zenoh equivalent of an RPC or HTTP request. Unlike pub/sub, queries are routable through the network and allow requesting current state from remote nodes, querying distributed storage, or implementing request/response services.

---

## Declaring a Queryable

### Rust

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // Default handler (channel-based): queryable.recv_async() / queryable.recv()
    let queryable = session
        .declare_queryable("demo/example/**")
        .await
        .unwrap();

    while let Ok(query) = queryable.recv_async().await {
        println!("Received query on: {}", query.key_expr());
        // Use the queryable's own declared key expression for the reply,
        // not query.key_expr() (which may be a wildcard from the getter)
        query
            .reply("demo/example/result", "hello")
            .await
            .unwrap();
    }
    // Queryable is automatically undeclared when dropped
}
```

### Rust (callback-based)

```rust
use zenoh::{Config, Wait};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let _queryable = session
        .declare_queryable("demo/example/**")
        .callback(move |query| {
            println!("Received query: {}", query.selector());
            // Use the queryable's declared key expression, not query.key_expr()
            query.reply("demo/example/result", "hello").wait().unwrap();
        })
        .await
        .unwrap();

    // Keep running until Ctrl-C
    tokio::signal::ctrl_c().await.unwrap();
}
```

### Python

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    queryable = session.declare_queryable("demo/example/**")

    while True:
        with queryable.recv() as query:
            print(f"Received query: {query.selector}")
            # Use the queryable's declared key expression, not query.key_expr (may be wildcard)
            query.reply("demo/example/result", "hello")
```

### Explicit Undeclaration

```rust
// Rust: explicit undeclare
let queryable = session.declare_queryable("key/expr").await.unwrap();
queryable.undeclare().await.unwrap();
```

```python
# Python: explicit undeclare
queryable = session.declare_queryable("key/expr")
queryable.undeclare()
```

---

## Complete vs. Incomplete Queryables

The `complete` flag is a routing hint that tells the network whether this queryable is **authoritative** for its key expression — i.e., whether it can fully answer queries for that key expression by itself.

### complete(true) — Authoritative

```rust
let queryable = session
    .declare_queryable("my/storage/**")
    .complete(true)
    .await
    .unwrap();
```

```python
queryable = session.declare_queryable("my/storage/**", complete=True)
```

**When to use `complete(true)`:**
- Storage plugins that hold data for the entire key expression space
- Service implementations that are the authoritative source for a resource
- Any queryable that can fully answer the query without needing other queryables

**Effect:** When a getter uses `QueryTarget::BestMatching` (the default), the router will prefer routing to complete queryables. When `QueryTarget::AllComplete` is used, only complete queryables receive the query.

### complete(false) — Non-Authoritative (Default)

```rust
let queryable = session
    .declare_queryable("sensor/readings/**")
    .complete(false)   // this is the default
    .await
    .unwrap();
```

**When to use `complete(false)` (or omit it):**
- Supplementary data sources that provide partial coverage
- Queryables that only respond for a subset of the key expression
- Application-level queryables where you don't need routing optimization

**Effect:** These queryables receive queries only when `QueryTarget::All` is used, or when no complete queryable is available and `BestMatching` falls back to any available queryable.

### How completeness affects routing

| QueryTarget | Receives complete=true | Receives complete=false |
|-------------|------------------------|-------------------------|
| `BestMatching` | Yes (preferred) | Only if no complete available |
| `All` | Yes | Yes |
| `AllComplete` | Yes | **No** |

---

## Query Targets

The query target controls which queryables receive a given query. It is set by the getter (not the queryable) at query time.

### BestMatching (Default)

```rust
use zenoh::query::QueryTarget;

let replies = session
    .get("my/data/**")
    .target(QueryTarget::BestMatching)  // this is the default
    .await
    .unwrap();
```

```python
replies = session.get("my/data/**", target=zenoh.QueryTarget.BEST_MATCHING)
```

**Behavior:** The router picks the best subset of queryables to answer the query, preferring complete queryables. "Best" means the set likely to provide the fastest and most complete reply — typically a single complete queryable or the nearest available match. If multiple complete queryables match, the router may select one or a few based on routing topology.

**Use case:** The default for most applications. Gets a useful response without querying every possible source.

### All

```rust
let replies = session
    .get("my/data/**")
    .target(QueryTarget::All)
    .await
    .unwrap();
```

```python
replies = session.get("my/data/**", target=zenoh.QueryTarget.ALL)
```

**Behavior:** All queryables with intersecting key expressions receive the query, both complete and incomplete.

**Use cases:**
- Fan-out queries where you want every node to respond
- Multi-source data aggregation
- Discovery queries to find all active participants
- Debugging (see everything that's out there)

### AllComplete

```rust
let replies = session
    .get("my/storage/**")
    .target(QueryTarget::AllComplete)
    .await
    .unwrap();
```

```python
replies = session.get("my/storage/**", target=zenoh.QueryTarget.ALL_COMPLETE)
```

**Behavior:** Only queryables declared with `complete(true)` receive the query. All such complete queryables matching the key expression receive it (not just one).

**Use cases:**
- Distributed storage queries where you need data from every storage node
- Ensuring all authoritative sources reply (e.g., querying all shards of a distributed store)
- When you need a complete view across all storage nodes

---

## ConsolidationMode (Deduplication)

When a query travels through the network, the same data may arrive via multiple paths (multi-hop routing can deliver duplicates). ConsolidationMode controls whether and how duplicate replies are filtered.

### Auto (Default)

```rust
use zenoh::query::ConsolidationMode;

let replies = session
    .get("my/data/**")
    .consolidation(ConsolidationMode::Auto)  // default
    .await
    .unwrap();
```

**Behavior:** `Auto` maps to `Latest` in the current implementation (replies are buffered and deduplicated, keeping only the newest per key). The only exception is when the unstable feature is enabled and a time range is specified in the query parameters, in which case it maps to `None`.

### None

```rust
let replies = session
    .get("my/data/**")
    .consolidation(ConsolidationMode::None)
    .await
    .unwrap();
```

```python
replies = session.get("my/data/**", consolidation=zenoh.ConsolidationMode.NONE)
```

**Behavior:** No deduplication. Every reply is forwarded to the getter as-is. Multiple replies for the same key-timestamp pair may be received.

**Use cases:**
- Topology queries where you want to see every reply individually
- Fan-out queries with `All` target where every response matters
- When you need to count how many nodes replied
- Debugging

### Monotonic

```rust
let replies = session
    .get("my/data/**")
    .consolidation(ConsolidationMode::Monotonic)
    .await
    .unwrap();
```

**Behavior:** Replies are forwarded immediately. If a reply arrives that is stale (i.e., a reply with an equal or more recent timestamp for the same key has already been forwarded), it is dropped. Effectively: newer arrivals are forwarded; stale duplicates are dropped.

**Use cases:**
- Multi-path routing environments where the same data may arrive via different network paths
- Reducing bandwidth while keeping low latency
- When you want streaming replies but don't need duplicates

### Latest

```rust
let replies = session
    .get("my/storage/**")
    .consolidation(ConsolidationMode::Latest)
    .await
    .unwrap();
```

```python
replies = session.get("my/storage/**", consolidation=zenoh.ConsolidationMode.LATEST)
```

**Behavior:** Holds back all replies until the query is complete (timeout), then delivers only the reply with the highest timestamp for each unique key. Earlier or duplicate replies for the same key are discarded.

**Use cases:**
- Storage queries where only the most recent value per key is needed
- Combined with `AllComplete` to get the definitive latest value from all storage nodes
- When freshness matters more than seeing intermediate values

### Where consolidation happens

Consolidation is a **client-side** operation in the current Zenoh implementation. The `QueryState` in the session tracks `reception_mode: ConsolidationMode` and the collected `replies: Option<HashMap<OwnedKeyExpr, Reply>>`. For `Latest` mode, replies are buffered in this hashmap and delivered only after the query completes. For `Monotonic`, the forwarding decision happens per-reply as they arrive.

---

## The Query Object

When a queryable receives a query, the callback or channel delivers a `Query` struct. The query contains everything the getter sent.

### Key Expression

```rust
// The key expression the GETTER used (may contain wildcards)
let ke: &KeyExpr = query.key_expr();

// IMPORTANT: do NOT use query.key_expr() as the reply key.
// Use your queryable's key expression instead.
// Example: query is "sensor/**", queryable is "sensor/temp"
// Reply should use "sensor/temp", not "sensor/**"
```

### Selector (Key Expression + Parameters)

```rust
// Full selector: key_expr + "?" + parameters
let selector = query.selector();  // e.g., "sensor/**?_time=[2024-01-01,2024-12-31]"
println!("Key: {}", query.key_expr());
println!("Params: {}", query.parameters());
```

### Payload

Queries can optionally carry a payload (useful for parameterized queries, search requests, etc.):

```rust
if let Some(payload) = query.payload() {
    // ZBytes does not have a deserialize() method; use to_bytes() or reader()
    let bytes = payload.to_bytes();
    // Deserialize manually using serde_json or similar:
    // let request: MyRequest = serde_json::from_slice(&bytes).unwrap();
}
```

```python
if query.payload is not None:
    data = query.payload.to_string()
```

### Attachment

```rust
if let Some(attachment) = query.attachment() {
    // Process attachment bytes
}
```

### QoS (unstable feature)

When the `unstable` feature is enabled:

```rust
#[cfg(feature = "unstable")]
{
    let priority = query.priority();
    let congestion_control = query.congestion_control();
    let express = query.express();
}
```

### accepts_replies

By default, replies must use a key expression that intersects with the query's key expression. A getter can relax this restriction:

```rust
// Getter side: allow disjoint replies
let replies = session
    .get("sensor/**")
    .accept_replies(zenoh::query::ReplyKeyExpr::Any)
    .await
    .unwrap();

// Queryable side: check what's accepted
let reply_ke = query.accepts_replies();
// ReplyKeyExpr::MatchingQuery (default) or ReplyKeyExpr::Any
```

---

## Selectors and Parameters

A **selector** is a key expression optionally followed by `?` and URL-encoded parameters:

```
demo/example/**?_time=[2024-01-01T00:00:00Z,2024-12-31T23:59:59Z]&limit=100
^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  key expression                     parameters
```

### Accessing Parameters in a Queryable

```rust
let params = query.parameters();

// Access a specific parameter by key
if let Some(time_range) = params.get("_time") {
    println!("Time range: {time_range}");
}

// Iterate all parameters
for (key, value) in params.iter() {
    println!("{key} = {value}");
}

// Check for presence
if params.contains_key("_filter") {
    let filter_expr = params.get("_filter").unwrap();
    // Apply filter
}
```

```python
params = query.parameters  # returns a Parameters object
time_range = params.get("_time")
```

### Standard Parameters

**`_time`** — Time range filter for historical queries. Format: `[start,end]` using ISO 8601 timestamps. Storage queryables that support time-based queries should check for this parameter and return only data within the range.

```
?_time=[2024-01-01T00:00:00Z,2024-06-01T00:00:00Z]
?_time=[..,2024-06-01T00:00:00Z]   # up to a time
?_time=[2024-01-01T00:00:00Z,..]   # from a time onward
```

**`_filter`** — Expression filter. Queryables that support server-side filtering should evaluate this expression against their data before replying.

**Custom parameters** — Any `key=value` pairs are valid. Use URL encoding for values containing special characters (`%20` for space, `%26` for `&`, etc.).

### Sending a Query with Parameters

```rust
// Rust: embed parameters in the selector string
let replies = session
    .get("storage/**?_time=[2024-01-01T00:00:00Z,2024-12-31T23:59:59Z]&limit=50")
    .await
    .unwrap();
```

```python
# Python: embed in the selector string
replies = session.get("storage/**?_time=[2024-01-01T00:00:00Z,..]")
```

---

## Reply Types

### reply() — Successful Data Reply

Sends a `Sample` of kind `Put` to the getter:

```rust
// Basic reply
query.reply("my/key/expr", "payload data").await.unwrap();

// Reply with encoding
query
    .reply("my/key/expr", payload_bytes)
    .encoding(zenoh::bytes::Encoding::APPLICATION_JSON)
    .await
    .unwrap();

// Reply with timestamp
query
    .reply("my/key/expr", "value")
    .timestamp(session.new_timestamp())
    .await
    .unwrap();
```

```python
# Basic reply — use a concrete key expression, not query.key_expr (may be wildcard)
query.reply("my/queryable/key", "payload data")

# Reply with encoding
query.reply("my/queryable/key", b'{"key": "value"}',
            encoding=zenoh.Encoding.APPLICATION_JSON)
```

**Key expression rule:** The reply key expression must intersect with the query's key expression, unless the getter opted in to `ReplyKeyExpr::Any`. For example, if the query is `sensor/**` and your queryable handles `sensor/temperature`, reply with `sensor/temperature`, not `sensor/**`.

### reply_del() — Delete Reply

Sends a `Sample` of kind `Delete`. Used by storage backends to indicate a key has been deleted:

```rust
query.reply_del("my/key/expr").await.unwrap();
```

### reply_err() — Error Reply

Sends a `ReplyError` with an error payload:

```rust
// Send error with string message
query.reply_err("Key not found").await.unwrap();

// Send error with encoding
query
    .reply_err(r#"{"code": 404, "message": "Not found"}"#)
    .encoding(zenoh::bytes::Encoding::APPLICATION_JSON)
    .await
    .unwrap();
```

```python
query.reply_err("Key not found")
```

**Multiple replies:** A queryable can send multiple replies to a single query (e.g., one reply per matching key):

```rust
for key in matching_keys {
    query.reply(&key, get_value(&key)).await.unwrap();
}
// The query is finalized (ResponseFinal sent) when the Query object is dropped
```

### Receiving Replies

```rust
let replies = session.get("key/**").await.unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => {
            println!("Got: {} = {:?}", sample.key_expr(), sample.payload());
        }
        Err(err) => {
            let msg = err.payload().try_to_string().unwrap_or_default();
            println!("Error: {msg}");
        }
    }
}
```

```python
replies = session.get("key/**", timeout=5.0)
for reply in replies:
    try:
        print(f"Got: {reply.ok.key_expr} = {reply.ok.payload.to_string()}")
    except:
        print(f"Error: {reply.err.payload.to_string()}")
```

### Reply struct

The `Reply` struct contains:
- `result()` → `Result<&Sample, &ReplyError>`
- `into_result()` → `Result<Sample, ReplyError>` (consumes reply)
- `replier_id()` → `Option<EntityGlobalId>` (unstable feature: the ID of the zenoh instance that replied)

### ReplyError struct

`ReplyError` contains:
- `payload()` → `&ZBytes` — application-defined error data
- `encoding()` → `&Encoding` — encoding of the error payload

There are no predefined error codes in the `ReplyError` itself; the payload is fully application-defined.

### ResponseFinal

When a `Query` object is dropped (at the end of its scope or when the queryable finishes handling it), Zenoh automatically sends a `ResponseFinal` message back to the getter. This is an internal protocol message that tells the session the queryable is done replying — it is not exposed directly to application code.

---

## Timeout Behavior

Every query has a timeout. When the timeout expires:

- The reply channel is closed (no more replies will arrive)
- Any in-flight replies that haven't been received by the getter are discarded
- The getter's `recv_async()` or iterator returns `Err`/stops iterating
- A `ReplyError` with payload `"Timeout"` is sent before the channel closes, so the getter will observe one final error reply indicating the timeout

**What happens to the queryable:** The queryable is not notified of the timeout. If it sends a reply after the getter has timed out, the reply is silently dropped (the underlying connection may still accept it briefly, but the getter will not process it).

### Default timeout

The default timeout is controlled by `queries_default_timeout_ms` in the Zenoh config. The factory default is **10,000 ms (10 seconds)**.

### Setting timeout

```rust
use std::time::Duration;

// On session.get()
let replies = session
    .get("key/**")
    .timeout(Duration::from_secs(5))
    .await
    .unwrap();

// On a declared Querier
let querier = session
    .declare_querier("key/**")
    .timeout(Duration::from_secs(5))
    .await
    .unwrap();
```

```python
# Python
replies = session.get("key/**", timeout=5.0)  # seconds as float
```

---

## Querier vs. session.get()

### session.get() — Ad-hoc Query

```rust
let replies = session.get("key/expression").await.unwrap();
```

`session.get()` sends a query directly without pre-registration. Each call carries the full key expression on the wire.

### declare_querier() — Declared Querier

```rust
let querier = session
    .declare_querier("key/expression")
    .target(QueryTarget::BestMatching)
    .consolidation(ConsolidationMode::None)
    .timeout(Duration::from_secs(5))
    .await
    .unwrap();

// Send a query using the pre-declared key expression
let replies = querier.get().await.unwrap();

// Can add parameters per-call
let replies = querier
    .get()
    .parameters("_time=[2024-01-01T00:00:00Z,..]")
    .await
    .unwrap();
```

```python
querier = session.declare_querier("key/expression")
replies = querier.get()
```

**The optimization:** Declaring a querier registers a wire-level ID for the key expression, similar to how a declared publisher avoids sending the full key expression string on every message. When you call `querier.get()` repeatedly, the key expression is compressed on the wire using this ID rather than re-sent as a full string each time.

**When the optimization applies:**
- When you send many queries to the same key expression (e.g., polling, repeated requests)
- The optimization is in routing: the network can pre-compute routing tables for the declared key expression

**Additional features of Querier:**
- `matching_status()` — check if there are queryables matching the key expression and target
- `matching_listener()` — get notified when matching queryables appear or disappear
- Per-call parameters via `.parameters()`

**When to use which:**
- Use `session.get()` for occasional or one-off queries
- Use `declare_querier()` when sending many queries to the same key expression or needing matching status/listeners

---

## Complete Working Examples

### 1. Basic Queryable Replying with Static Data

**Rust:**

```rust
use zenoh::Config;

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    let queryable = session
        .declare_queryable("demo/greeting")
        .await?;

    println!("Queryable ready on 'demo/greeting'");

    while let Ok(query) = queryable.recv_async().await {
        println!("Received query: {}", query.selector());
        query.reply("demo/greeting", "Hello from Zenoh!").await?;
    }

    Ok(())
}
```

**Python:**

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    queryable = session.declare_queryable("demo/greeting")
    print("Queryable ready on 'demo/greeting'")

    while True:
        with queryable.recv() as query:
            print(f"Received query: {query.selector}")
            query.reply("demo/greeting", "Hello from Zenoh!")
```

---

### 2. Queryable That Implements _time Range Filtering

**Rust:**

```rust
use std::collections::HashMap;
use zenoh::Config;

// Simulated time-series data
fn get_data_in_range(start: &str, end: &str) -> Vec<(String, String)> {
    // In a real implementation, query your storage with the time range
    vec![
        ("demo/sensor/temp".to_string(), "22.5".to_string()),
        ("demo/sensor/humidity".to_string(), "60.0".to_string()),
    ]
}

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    let queryable = session
        .declare_queryable("demo/sensor/**")
        .complete(true)  // This is a storage — declare as complete
        .await?;

    println!("Storage queryable ready");

    while let Ok(query) = queryable.recv_async().await {
        let params = query.parameters();

        let results = if let Some(time_range) = params.get("_time") {
            // Parse time range: format is [start,end]
            let range = time_range.trim_matches(|c| c == '[' || c == ']');
            let parts: Vec<&str> = range.splitn(2, ',').collect();
            if parts.len() == 2 {
                get_data_in_range(parts[0].trim(), parts[1].trim())
            } else {
                get_data_in_range("", "")
            }
        } else {
            get_data_in_range("", "")
        };

        for (key, value) in results {
            // Only reply for keys that intersect with the query
            if let Ok(ke) = zenoh::key_expr::KeyExpr::new(&key) {
                if query.key_expr().intersects(&ke) {
                    query.reply(key, value).await?;
                }
            }
        }
    }

    Ok(())
}
```

**Python:**

```python
import zenoh

def get_data_in_range(start, end):
    # Query your time-series store here
    return [
        ("demo/sensor/temp", "22.5"),
        ("demo/sensor/humidity", "60.0"),
    ]

with zenoh.open(zenoh.Config()) as session:
    queryable = session.declare_queryable("demo/sensor/**", complete=True)
    print("Storage queryable ready")

    while True:
        with queryable.recv() as query:
            params = query.parameters
            time_range = params.get("_time") if params else None

            if time_range:
                range_str = time_range.strip("[]")
                parts = range_str.split(",", 1)
                start = parts[0].strip() if len(parts) > 0 else ""
                end = parts[1].strip() if len(parts) > 1 else ""
                results = get_data_in_range(start, end)
            else:
                results = get_data_in_range("", "")

            for key, value in results:
                query.reply(key, value)
```

---

### 3. Queryable That Returns ReplyError for Unknown Keys

**Rust:**

```rust
use std::collections::HashMap;
use zenoh::Config;

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    // A registry of known keys and their values
    let registry: HashMap<&str, &str> = [
        ("services/auth", "running"),
        ("services/db", "running"),
    ]
    .into_iter()
    .collect();

    let queryable = session
        .declare_queryable("services/**")
        .await?;

    while let Ok(query) = queryable.recv_async().await {
        let key = query.key_expr().as_str();

        // Check if the exact key is known (wildcard matching would require more logic)
        if let Some(value) = registry.get(key) {
            query.reply(key, *value).await?;
        } else {
            // Send an error reply
            query
                .reply_err(format!("Unknown service: {key}"))
                .await?;
        }
    }

    Ok(())
}
```

**Python:**

```python
import zenoh

registry = {
    "services/auth": "running",
    "services/db": "running",
}

with zenoh.open(zenoh.Config()) as session:
    queryable = session.declare_queryable("services/**")

    while True:
        with queryable.recv() as query:
            key = str(query.key_expr)
            if key in registry:
                query.reply(key, registry[key])
            else:
                query.reply_err(f"Unknown service: {key}")
```

---

### 4. Fan-Out Query: All Target + None Consolidation

This pattern queries every node and collects all responses without deduplication.

**Rust (getter side):**

```rust
use zenoh::{query::{QueryTarget, ConsolidationMode}, Config};

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    let replies = session
        .get("cluster/nodes/**")
        .target(QueryTarget::All)            // Ask every matching queryable
        .consolidation(ConsolidationMode::None) // Keep every reply, even duplicates
        .await?;

    let mut count = 0;
    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                count += 1;
                println!(
                    "[{}] node={} status={}",
                    count,
                    sample.key_expr(),
                    sample.payload().try_to_string().unwrap_or_default()
                );
            }
            Err(err) => {
                println!("Error from node: {}", err.payload().try_to_string().unwrap_or_default());
            }
        }
    }
    println!("Received {} total responses", count);

    Ok(())
}
```

**Python (getter side):**

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    replies = session.get(
        "cluster/nodes/**",
        target=zenoh.QueryTarget.ALL,
        consolidation=zenoh.ConsolidationMode.NONE,
    )

    count = 0
    for reply in replies:
        try:
            count += 1
            print(f"[{count}] {reply.ok.key_expr} = {reply.ok.payload.to_string()}")
        except:
            print(f"Error: {reply.err.payload.to_string()}")

    print(f"Received {count} total responses")
```

---

### 5. Storage-Style Query: AllComplete + Latest Consolidation

This pattern queries all authoritative storage nodes and keeps only the most recent value per key.

**Rust (storage queryable):**

```rust
use zenoh::Config;

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    // Declare as complete — this is an authoritative storage node
    let queryable = session
        .declare_queryable("data/**")
        .complete(true)
        .await?;

    println!("Storage node ready");

    while let Ok(query) = queryable.recv_async().await {
        // Simulate stored data with timestamps
        let data = vec![
            ("data/sensor/temp", "23.1"),
            ("data/sensor/pressure", "1013.25"),
        ];

        for (key, value) in data {
            if let Ok(ke) = zenoh::key_expr::KeyExpr::new(key) {
                if query.key_expr().intersects(&ke) {
                    query
                        .reply(key, value)
                        .timestamp(session.new_timestamp())
                        .await?;
                }
            }
        }
    }

    Ok(())
}
```

**Rust (getter side):**

```rust
use zenoh::{query::{QueryTarget, ConsolidationMode}, Config};

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    let replies = session
        .get("data/**")
        .target(QueryTarget::AllComplete)       // Only ask complete (storage) queryables
        .consolidation(ConsolidationMode::Latest) // Keep only the latest per key
        .await?;

    // With Latest consolidation, replies are delivered after the query completes
    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => println!(
                "{} = {} (ts: {:?})",
                sample.key_expr(),
                sample.payload().try_to_string().unwrap_or_default(),
                sample.timestamp()
            ),
            Err(err) => println!("Error: {}", err.payload().try_to_string().unwrap_or_default()),
        }
    }

    Ok(())
}
```

**Python (getter side):**

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    replies = session.get(
        "data/**",
        target=zenoh.QueryTarget.ALL_COMPLETE,
        consolidation=zenoh.ConsolidationMode.LATEST,
    )

    for reply in replies:
        try:
            print(f"{reply.ok.key_expr} = {reply.ok.payload.to_string()}")
        except:
            print(f"Error: {reply.err.payload.to_string()}")
```

---

### 6. Using Querier for Repeated Queries to the Same KE

Use `declare_querier()` when you send many queries to the same key expression. The wire-level key expression ID avoids resending the full key string on every query.

**Rust:**

```rust
use std::time::Duration;
use zenoh::{query::{QueryTarget, ConsolidationMode}, Config};

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    // Declare once, reuse for many queries
    let querier = session
        .declare_querier("telemetry/device/**")
        .target(QueryTarget::AllComplete)
        .consolidation(ConsolidationMode::Latest)
        .timeout(Duration::from_secs(2))
        .await?;

    // Poll every 5 seconds
    loop {
        println!("Querying telemetry...");

        let replies = querier
            .get()
            // Optional: add parameters per-call
            .parameters("_time=[..,now]")
            .await?;

        while let Ok(reply) = replies.recv_async().await {
            match reply.result() {
                Ok(sample) => println!(
                    "  {} = {}",
                    sample.key_expr(),
                    sample.payload().try_to_string().unwrap_or_default()
                ),
                Err(err) => println!(
                    "  ERROR: {}",
                    err.payload().try_to_string().unwrap_or_default()
                ),
            }
        }

        tokio::time::sleep(Duration::from_secs(5)).await;
    }
}
```

**Python:**

```python
import time
import zenoh

with zenoh.open(zenoh.Config()) as session:
    querier = session.declare_querier(
        "telemetry/device/**",
        target=zenoh.QueryTarget.ALL_COMPLETE,
        consolidation=zenoh.ConsolidationMode.LATEST,
        timeout=2.0,
    )

    while True:
        print("Querying telemetry...")
        replies = querier.get()

        for reply in replies:
            try:
                print(f"  {reply.ok.key_expr} = {reply.ok.payload.to_string()}")
            except:
                print(f"  ERROR: {reply.err.payload.to_string()}")

        time.sleep(5)
```

---

## Summary: Quick Reference

| Concept | Value | When to Use |
|---------|-------|-------------|
| `complete(true)` | Authoritative queryable | Storage plugins, full service implementations |
| `complete(false)` | Non-authoritative (default) | Supplementary sources, app queryables |
| `QueryTarget::BestMatching` | Router picks best | Default — most applications |
| `QueryTarget::All` | Every matching queryable | Fan-out, discovery, aggregation |
| `QueryTarget::AllComplete` | All complete queryables | Distributed storage, ensure full coverage |
| `ConsolidationMode::Auto` | Implementation decides | Default |
| `ConsolidationMode::None` | No dedup, stream all | Count responses, see every reply |
| `ConsolidationMode::Monotonic` | Forward, skip stale | Multi-path routing, low-latency dedup |
| `ConsolidationMode::Latest` | Buffer, emit newest per key | Storage queries, freshest value only |
| `session.get()` | Ad-hoc query | One-off or infrequent queries |
| `declare_querier()` | Reusable querier | Repeated queries, matching status/listener |
| `query.reply()` | Success + data | Normal response |
| `query.reply_del()` | Delete tombstone | Key deleted in storage |
| `query.reply_err()` | Application error | Key not found, access denied, etc. |

## See Also

- [Key Expressions Guide](key-expressions-guide.md) — selector syntax (`?parameters`) and wildcard matching used in get() calls
- [Serialization Complete Guide](serialization-complete-guide.md) — how to encode/decode query payloads and reply values
- [Zenoh Ext Guide](zenoh-ext-guide.md) — AdvancedPublisher/AdvancedSubscriber patterns that extend the queryable model
- [Programming Model Guide](programming-model-guide.md) — the session API context for declaring queryables and making get() calls
