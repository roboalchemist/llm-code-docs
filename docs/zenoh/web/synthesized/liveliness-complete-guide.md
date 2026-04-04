# Zenoh Liveliness: Complete Guide

## Table of Contents

- [What Is Liveliness?](#what-is-liveliness)
- [Token Lifecycle](#token-lifecycle)
  - [Declaring a Token](#declaring-a-token)
  - [Undeclaring: Explicit vs Drop](#undeclaring-explicit-vs-drop)
  - [Session Close Behavior](#session-close-behavior)
  - [Session Reconnect Behavior](#session-reconnect-behavior)
  - [Multiple Tokens on the Same Key Expression](#multiple-tokens-on-the-same-key-expression)
- [The `/liveliness/` Key Space](#the-liveliness-key-space)
- [Liveliness Subscriber](#liveliness-subscriber)
  - [Declaring a Subscriber](#declaring-a-subscriber)
  - [Put Event](#put-event)
  - [Delete Event](#delete-event)
  - [Ordering Guarantees](#ordering-guarantees)
  - [History: Seeing Existing Tokens](#history-seeing-existing-tokens)
- [get(): Point-in-Time Snapshot](#get-point-in-time-snapshot)
  - [Timeout Behavior](#timeout-behavior)
  - [get() vs subscriber for Complete Picture](#get-vs-subscriber-for-complete-picture)
- [History Retention](#history-retention)
- [Practical Patterns](#practical-patterns)
  - [Pattern 1: Service Registry](#pattern-1-service-registry)
  - [Pattern 2: Health Monitoring / Watchdog](#pattern-2-health-monitoring-watchdog)
  - [Pattern 3: Distributed Leader Election](#pattern-3-distributed-leader-election)
- [Liveliness vs Regular Pub/Sub Heartbeat](#liveliness-vs-regular-pubsub-heartbeat)
  - [The Heartbeat Approach (and Why It Falls Short)](#the-heartbeat-approach-and-why-it-falls-short)
  - [Why Liveliness Is Better](#why-liveliness-is-better)
  - [When Heartbeats Are Still Appropriate](#when-heartbeats-are-still-appropriate)
- [Full API Reference](#full-api-reference)
  - [Rust API](#rust-api)
  - [Python API](#python-api)
- [Quick Reference](#quick-reference)

## What Is Liveliness?

Zenoh Liveliness is a mechanism for tracking whether remote entities (processes, services, nodes) are reachable and alive. Instead of requiring applications to send periodic heartbeat messages, Zenoh ties token existence directly to transport-layer session health. When a process crashes, loses network connectivity, or cleanly exits, Zenoh propagates the liveness change automatically — with no application-level heartbeat thread required.

A **liveliness token** is a named entity declared on a key expression. Any other application in the system can subscribe to liveliness changes or query the current snapshot of alive tokens. The token is considered alive as long as:

1. The declaring application has not explicitly undeclared or dropped the token.
2. The declaring application is running (has not crashed or stopped).
3. The declaring application has Zenoh connectivity with the observer.

If any of these conditions breaks, the token is seen as dropped by observers.

---

## Token Lifecycle

### Declaring a Token

Tokens are declared through the `liveliness()` accessor on a `Session`:

**Rust:**
```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // Declare a liveliness token on the key expression "group1/service-a"
    let token = session
        .liveliness()
        .declare_token("group1/service-a")
        .await
        .unwrap();

    // Token is now visible to all observers matching "group1/**"
    // Keep the token alive by keeping the variable in scope
    println!("Token declared. Press CTRL-C to exit.");
    std::thread::park();

    // Explicit undeclare (optional — drop also works)
    token.undeclare().await.unwrap();
}
```

**Python:**
```python
import time
import zenoh

conf = zenoh.Config()
with zenoh.open(conf) as session:
    # Context manager keeps token alive until the `with` block exits
    with session.liveliness().declare_token("group1/service-a") as token:
        print("Token declared. Press CTRL-C to exit.")
        while True:
            time.sleep(1)
    # Token undeclared here when the inner `with` block exits
```

### Undeclaring: Explicit vs Drop

There are two ways to end a token's life:

**Explicit undeclare (Rust):**
```rust
token.undeclare().await.unwrap();
```

**Implicit undeclare via drop (Rust):**
```rust
{
    let token = session.liveliness().declare_token("svc/node-1").await.unwrap();
    // ... do work ...
} // token is dropped here; undeclared automatically
```

The `LivelinessToken` struct has `undeclare_on_drop: bool = true` by default. When the token is dropped without an explicit `undeclare()` call, the `Drop` implementation calls `undeclare_impl()`. Calling `undeclare()` sets this flag to `false` first to prevent a double-undeclare on the subsequent drop.

**Python** uses context managers for the same pattern — exiting the `with` block undeclares the token.

### Session Close Behavior

When the Zenoh session closes (either explicitly or because the process exits), all tokens declared on that session are automatically undeclared. Observers receive `Delete` events for each token. There is no need to manually undeclare tokens before closing the session — cleanup is automatic.

### Session Reconnect Behavior

Liveliness tokens are **not automatically re-declared after a reconnect**. The token lifetime is tied to the transport session at the time of declaration. If a client disconnects and reconnects, it must redeclare any tokens it wants to be visible again. This is an important consideration for resilient services: at startup (or reconnect), always declare the liveliness token before announcing readiness.

### Multiple Tokens on the Same Key Expression

Multiple applications (or multiple sessions) can declare tokens on the same key expression. The token is considered alive as long as **at least one** declaration is active anywhere in the system. The token is considered dropped only when the **last** declaration is undeclared or dropped. This allows redundant services to share a single well-known key without false-positive death notifications.

---

## The `/liveliness/` Key Space

Liveliness tokens do not live in the normal pub/sub key space. Internally, Zenoh uses a reserved `@/liveliness/` prefix (or similar internal routing prefix) to segregate liveliness state from regular data. This prevents liveliness tokens from colliding with application data and allows routers to apply specialized propagation rules.

Key points about the liveliness key space:
- **User-facing**: You declare tokens on your own key expressions (e.g., `group1/service-a`), not on `@/liveliness/...` directly. Zenoh routes them internally.
- **Router propagation**: Routers propagate liveliness state across the network so that any connected observer sees tokens from any connected peer.
- **Network partitions**: If connectivity is lost between two parts of the network, observers on one side see tokens from the other side as **dropped** (even though those tokens may still be alive on the other side). When connectivity is restored, tokens reappear as `Put` events.
- **Durability**: Liveliness state is **not durable** — it does not survive router restarts. If a router restarts, tokens must be redeclared by their declaring sessions. Router restarts appear to observers as all tokens being dropped (Delete events for all live tokens), followed by Put events when the declaring sessions reconnect and redeclare.

---

## Liveliness Subscriber

### Declaring a Subscriber

A liveliness subscriber watches for changes in token state. It receives `Put` samples when tokens appear and `Delete` samples when they disappear.

**Rust:**
```rust
use zenoh::{Config, sample::SampleKind};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let subscriber = session
        .liveliness()
        .declare_subscriber("group1/**")
        .await
        .unwrap();

    println!("Watching liveliness on 'group1/**'...");
    while let Ok(sample) = subscriber.recv_async().await {
        match sample.kind() {
            SampleKind::Put => {
                println!("[+] Token alive: {}", sample.key_expr());
            }
            SampleKind::Delete => {
                println!("[-] Token dropped: {}", sample.key_expr());
            }
        }
    }
}
```

**Python:**
```python
import zenoh

conf = zenoh.Config()
with zenoh.open(conf) as session:
    with session.liveliness().declare_subscriber("group1/**") as sub:
        print("Watching liveliness on 'group1/**'...")
        for sample in sub:
            if sample.kind == zenoh.SampleKind.PUT:
                print(f"[+] Token alive: {sample.key_expr}")
            elif sample.kind == zenoh.SampleKind.DELETE:
                print(f"[-] Token dropped: {sample.key_expr}")
```

### Put Event

A `Put` sample is delivered when:
- A new token is declared on a matching key expression.
- An existing token becomes visible due to network reconnection.
- The subscriber is declared with `history=true` and existing tokens are found (these arrive as `Put` samples).

The `sample.key_expr()` carries the full key expression of the token that appeared.

### Delete Event

A `Delete` sample is delivered when:
- A token is explicitly undeclared.
- A token is dropped (process exited, session closed, variable went out of scope).
- Network connectivity is lost to the declaring application.

**Special case — subscriber loses all connectivity**: If the subscribing application itself loses all connectivity (loses its router and cannot reconnect), Zenoh sends a synthetic `Delete` with key `**` to matching subscribers. This wildcard Delete indicates "consider all tokens dropped" without requiring the client to maintain an explicit registry of all known tokens. Applications should handle a `Delete` on `**` by clearing their entire liveness map.

### Ordering Guarantees

Events are delivered in the order they arrive from the network. Within a single session, events are ordered. Across sessions/routers, Zenoh does not guarantee strict global ordering of concurrent Put/Delete events — applications that need causal ordering should implement their own sequencing (e.g., attach timestamps or sequence numbers when the liveliness-with-value feature lands).

### History: Seeing Existing Tokens

By default (`history=false`), a new subscriber only receives events that occur **after** it is declared. Tokens declared before the subscriber was created are invisible to it.

Setting `history=true` causes Zenoh to perform an implicit `get()` query at subscription time and deliver currently-alive tokens as `Put` events before the subscriber starts receiving live changes. This gives late-joining subscribers a complete initial view.

**Rust:**
```rust
let subscriber = session
    .liveliness()
    .declare_subscriber("group1/**")
    .history(true)   // see tokens that were declared before this subscription
    .await
    .unwrap();
```

**Python:**
```python
sub = session.liveliness().declare_subscriber("group1/**", history=True)
```

The `history` flag is equivalent to combining a `get()` snapshot with a live subscriber, but done atomically by Zenoh so no events are missed between the snapshot and the subscription.

**Default value**: `false` (no history).

---

## get(): Point-in-Time Snapshot

`liveliness().get()` returns all currently alive tokens matching a key expression at the moment of the query. This is a one-shot operation: it does not deliver future changes.

**Rust:**
```rust
use std::time::Duration;
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let replies = session
        .liveliness()
        .get("group1/**")
        .timeout(Duration::from_secs(5))
        .await
        .unwrap();

    println!("Currently alive tokens matching 'group1/**':");
    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => println!("  alive: {}", sample.key_expr()),
            Err(err) => {
                let msg = err.payload().try_to_string()
                    .unwrap_or_else(|e| e.to_string().into());
                println!("  error: {msg}");
            }
        }
    }
}
```

**Python:**
```python
import zenoh

conf = zenoh.Config()
with zenoh.open(conf) as session:
    replies = session.liveliness().get("group1/**", timeout=5.0)
    print("Currently alive tokens:")
    for reply in replies:
        try:
            print(f"  alive: {reply.ok.key_expr}")
        except Exception:
            print(f"  error: {reply.err.payload.to_string()}")
```

### Timeout Behavior

The default timeout is the session's `queries_default_timeout` (typically 10 seconds, as shown in the examples with `default_value = "10000"` ms). The query is sent to all matching nodes; replies arrive as they come in. The receiver channel closes when the timeout expires or all replies have been received.

### get() vs subscriber for Complete Picture

To get a complete and continuously-updated view:
- Use `get()` alone for a one-shot snapshot (current state only).
- Use a subscriber alone for future changes (misses tokens already alive at subscription time unless `history=true`).
- Use `declare_subscriber(...).history(true)` for the recommended combined approach: initial snapshot + live changes, delivered in order with no gap.

The `history=true` subscriber is preferred over manually combining `get()` + subscriber because it handles the race condition between the query results and live events atomically.

---

## History Retention

The `history` option on `declare_subscriber` controls whether a newly created subscriber sees tokens that were **already alive** when the subscription was made.

| `history` | Behavior |
|-----------|----------|
| `false` (default) | Subscriber receives only events that occur after subscription. Pre-existing tokens are invisible. |
| `true` | Subscriber receives currently-alive tokens as `Put` events, then continues receiving live events. |

Internally, `history=true` causes Zenoh to issue a liveliness GET query at declaration time. The results are merged with the live event stream before delivery, so the subscriber sees a consistent initial state followed by incremental updates.

**When to use `history=true`**: Any application that needs to build a complete registry of alive services must use `history=true` (or separately call `get()`). If `history=false`, the subscriber starts blind — it will learn about services only as they come and go after the subscription.

---

## Practical Patterns

### Pattern 1: Service Registry

Use liveliness tokens to implement a distributed service registry. Each service instance declares a token with a structured key encoding its type, name, and instance ID. Consumers watch for these tokens to discover available services.

**Design:**
- Token key: `registry/service/<service-type>/<instance-id>`
- Subscriber key: `registry/service/<service-type>/**` (for a specific type) or `registry/service/**` (all services)

**Rust — Service Producer:**
```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let instance_id = "node-42";
    let service_type = "image-processor";

    let token_key = format!("registry/service/{service_type}/{instance_id}");
    let token = session
        .liveliness()
        .declare_token(&token_key)
        .await
        .unwrap();

    println!("Service registered at '{token_key}'");
    println!("Running... Press CTRL-C to exit.");

    // Simulate work
    tokio::signal::ctrl_c().await.unwrap();

    // Explicit undeclare signals graceful shutdown to observers
    token.undeclare().await.unwrap();
    println!("Service gracefully deregistered.");
}
```

**Rust — Service Consumer:**
```rust
use std::collections::HashSet;
use zenoh::{Config, sample::SampleKind};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let mut alive_services: HashSet<String> = HashSet::new();

    // history=true: see services that registered before we started
    let subscriber = session
        .liveliness()
        .declare_subscriber("registry/service/image-processor/**")
        .history(true)
        .await
        .unwrap();

    while let Ok(sample) = subscriber.recv_async().await {
        let key = sample.key_expr().to_string();
        match sample.kind() {
            SampleKind::Put => {
                alive_services.insert(key.clone());
                println!("[+] Service available: {key}");
                println!("    Total alive: {}", alive_services.len());
            }
            SampleKind::Delete => {
                // Handle wildcard delete (subscriber lost all connectivity)
                if key == "**" {
                    println!("[!] Lost all connectivity — clearing service registry");
                    alive_services.clear();
                } else {
                    alive_services.remove(&key);
                    println!("[-] Service gone: {key}");
                    println!("    Total alive: {}", alive_services.len());
                }
            }
        }
    }
}
```

**Python — Service Registry Consumer:**
```python
import zenoh

conf = zenoh.Config()
alive_services = set()

with zenoh.open(conf) as session:
    # history=True ensures we see services registered before us
    with session.liveliness().declare_subscriber(
        "registry/service/**", history=True
    ) as sub:
        print("Service registry watching 'registry/service/**'")
        for sample in sub:
            key = str(sample.key_expr)
            if sample.kind == zenoh.SampleKind.PUT:
                alive_services.add(key)
                print(f"[+] Service available: {key} (total: {len(alive_services)})")
            elif sample.kind == zenoh.SampleKind.DELETE:
                if key == "**":
                    print("[!] Lost all connectivity — clearing registry")
                    alive_services.clear()
                else:
                    alive_services.discard(key)
                    print(f"[-] Service gone: {key} (total: {len(alive_services)})")
```

---

### Pattern 2: Health Monitoring / Watchdog

Use liveliness to monitor whether a critical remote process is still running. Declare one token per process at startup; a monitor subscribes and alerts on `Delete` events.

**Rust — Monitored Process:**
```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let process_id = std::process::id();
    let token_key = format!("health/process/{process_id}");

    // Declare token immediately at startup — this is the "I am alive" signal
    let token = session
        .liveliness()
        .declare_token(&token_key)
        .await
        .unwrap();

    println!("Process {process_id} declared liveness at '{token_key}'");

    // Do real work here
    tokio::time::sleep(std::time::Duration::from_secs(30)).await;

    drop(token); // Or explicit: token.undeclare().await.unwrap();
}
```

**Rust — Watchdog:**
```rust
use zenoh::{Config, sample::SampleKind};
use std::collections::HashMap;
use std::time::Instant;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let mut process_start_times: HashMap<String, Instant> = HashMap::new();

    let subscriber = session
        .liveliness()
        .declare_subscriber("health/process/**")
        .history(true)
        .await
        .unwrap();

    println!("Watchdog monitoring 'health/process/**'");

    while let Ok(sample) = subscriber.recv_async().await {
        let key = sample.key_expr().to_string();
        match sample.kind() {
            SampleKind::Put => {
                process_start_times.insert(key.clone(), Instant::now());
                println!("[OK] Process alive: {key}");
            }
            SampleKind::Delete => {
                if key == "**" {
                    eprintln!("[WARN] Watchdog lost all connectivity");
                    process_start_times.clear();
                } else {
                    let uptime = process_start_times
                        .remove(&key)
                        .map(|t| t.elapsed())
                        .map(|d| format!("{:.1}s", d.as_secs_f64()))
                        .unwrap_or_else(|| "unknown".to_string());
                    eprintln!("[ALERT] Process DIED: {key} (was up {uptime})");
                    // Trigger alert: pager, email, restart logic, etc.
                }
            }
        }
    }
}
```

**Python — Watchdog:**
```python
import zenoh
from datetime import datetime

conf = zenoh.Config()
process_registry = {}  # key -> start_time

with zenoh.open(conf) as session:
    with session.liveliness().declare_subscriber(
        "health/process/**", history=True
    ) as sub:
        print("Watchdog monitoring 'health/process/**'")
        for sample in sub:
            key = str(sample.key_expr)
            if sample.kind == zenoh.SampleKind.PUT:
                process_registry[key] = datetime.now()
                print(f"[OK] Process alive: {key}")
            elif sample.kind == zenoh.SampleKind.DELETE:
                if key == "**":
                    print("[WARN] Lost all connectivity — clearing watchdog state")
                    process_registry.clear()
                else:
                    start = process_registry.pop(key, None)
                    if start:
                        uptime = (datetime.now() - start).total_seconds()
                        print(f"[ALERT] Process DIED: {key} (was up {uptime:.1f}s)")
                    else:
                        print(f"[ALERT] Process DIED: {key} (uptime unknown)")
```

---

### Pattern 3: Distributed Leader Election

Use liveliness tokens to implement leader election in a group of peers. The candidate with the lexicographically greatest session ZID (Zenoh ID) wins when it holds the only surviving token in the leadership key space.

The core insight: declare a token at `leader/<zid>`. After subscribing with history, collect all peer tokens. The leader is the peer with the largest ZID among those still alive.

**Rust:**
```rust
use std::collections::BTreeSet;
use zenoh::{Config, sample::SampleKind};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let my_zid = session.zid().to_string();

    println!("My ZID: {my_zid}");

    // Declare our presence in the election group
    let token_key = format!("election/group1/{my_zid}");
    let _token = session
        .liveliness()
        .declare_token(&token_key)
        .await
        .unwrap();

    // Watch all candidates (history=true to see existing members)
    let subscriber = session
        .liveliness()
        .declare_subscriber("election/group1/**")
        .history(true)
        .await
        .unwrap();

    let mut candidates: BTreeSet<String> = BTreeSet::new();

    while let Ok(sample) = subscriber.recv_async().await {
        let key = sample.key_expr().to_string();
        // Extract ZID from "election/group1/<zid>"
        let candidate_zid = key.split('/').last().unwrap_or("").to_string();

        match sample.kind() {
            SampleKind::Put => {
                candidates.insert(candidate_zid.clone());
                println!("[+] Candidate joined: {candidate_zid}");
            }
            SampleKind::Delete => {
                if key == "**" {
                    candidates.clear();
                    candidates.insert(my_zid.clone());
                    println!("[!] Lost connectivity — assuming leadership");
                } else {
                    candidates.remove(&candidate_zid);
                    println!("[-] Candidate left: {candidate_zid}");
                }
            }
        }

        // Leader = candidate with max ZID (lexicographic order)
        if let Some(leader) = candidates.iter().next_back() {
            if leader == &my_zid {
                println!("[LEADER] I am the current leader");
            } else {
                println!("[FOLLOWER] Current leader: {leader}");
            }
        }
    }
}
```

**Python:**
```python
import zenoh

conf = zenoh.Config()

with zenoh.open(conf) as session:
    my_zid = str(session.zid())
    print(f"My ZID: {my_zid}")

    token_key = f"election/group1/{my_zid}"
    with session.liveliness().declare_token(token_key) as _token:
        candidates = set()

        with session.liveliness().declare_subscriber(
            "election/group1/**", history=True
        ) as sub:
            for sample in sub:
                key = str(sample.key_expr)
                candidate_zid = key.split("/")[-1]

                if sample.kind == zenoh.SampleKind.PUT:
                    candidates.add(candidate_zid)
                    print(f"[+] Candidate joined: {candidate_zid}")
                elif sample.kind == zenoh.SampleKind.DELETE:
                    if key == "**":
                        candidates.clear()
                        candidates.add(my_zid)
                        print("[!] Lost connectivity — assuming leadership")
                    else:
                        candidates.discard(candidate_zid)
                        print(f"[-] Candidate left: {candidate_zid}")

                if candidates:
                    leader = max(candidates)
                    if leader == my_zid:
                        print("[LEADER] I am the current leader")
                    else:
                        print(f"[FOLLOWER] Current leader: {leader}")
```

---

## Liveliness vs Regular Pub/Sub Heartbeat

### The Heartbeat Approach (and Why It Falls Short)

A common pattern for liveness detection is to have each process publish a heartbeat message (e.g., every 5 seconds) and have monitors track the last-seen timestamp. If no heartbeat is received within a timeout window, the process is considered dead.

Problems with this approach:

| Problem | Description |
|---------|-------------|
| **Arbitrary delay** | The monitor cannot detect death faster than the heartbeat interval plus timeout margin. A 5-second heartbeat with a 2x timeout means up to 10 seconds of undetected failure. |
| **False positives** | A transient network hiccup causes a "missed heartbeat" even though the process is alive. The monitor must tune thresholds carefully to avoid false alarms. |
| **Extra infrastructure** | Every monitored process needs a heartbeat publisher thread, an application-level topic, and a consumer tracking last-seen times. |
| **Reconnect blindness** | When the monitoring subscriber reconnects, it has no idea whether the monitored processes are alive. It must wait for the next heartbeat cycle to rebuild state. |
| **No clean-shutdown signal** | Heartbeats just stop; there is no semantic difference between "clean shutdown" and "crash". |

### Why Liveliness Is Better

| Advantage | Description |
|-----------|-------------|
| **Transport-layer detection** | Death is detected when the Zenoh transport session closes — as fast as TCP keepalive / link failure detection, not constrained by a heartbeat interval. |
| **No heartbeat thread** | Zero application code for the producer. Declare the token at startup and forget it. |
| **Immediate Delete on network failure** | When connectivity is lost, observers receive `Delete` events immediately (bounded by TCP keepalive timeout), not "after N missed heartbeats". |
| **Clean shutdown distinction** | Explicit `undeclare()` vs crash/drop produces the same `Delete` event to observers — the distinction is that explicit undeclare is immediate, while crash is bounded by TCP timeout. |
| **Late-joiner support** | `history=true` subscribers see all currently alive tokens at subscription time. A heartbeat-based system requires waiting for all processes to send their next heartbeat. |
| **Multi-producer merging** | Multiple tokens on the same key are tracked automatically — the token is alive until the last one is gone, with no application logic needed. |

### When Heartbeats Are Still Appropriate

Liveliness is not a substitute for heartbeats in all cases:

- **Application-level health**: Liveliness tells you the process is running and connected. It does not tell you whether the application is healthy (e.g., deadlocked but not crashed). A heartbeat that requires the application to actively produce it can detect application-level hangs that liveliness cannot.
- **Attached data**: Liveliness tokens currently carry no payload (a future enhancement is planned). If you need to communicate health metadata (load, version, capabilities), pub/sub is still needed alongside liveliness.
- **Extremely tight SLAs**: If your SLA requires detecting failure faster than TCP keepalive allows (typically 30–90 seconds on default settings), you need application-level detection even with liveliness.

---

## Full API Reference

### Rust API

#### `session.liveliness() -> Liveliness<'_>`

Returns the `Liveliness` accessor. Does not allocate resources; it is a zero-cost view over the session.

---

#### `Liveliness::declare_token(key_expr) -> LivelinessTokenBuilder`

Declare a liveliness token on the given key expression.

```rust
pub fn declare_token<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessTokenBuilder<'a, 'b>
```

- **`key_expr`**: Any type implementing `TryInto<KeyExpr<'b>>`. Accepts `&str`, `String`, `KeyExpr`, etc.
- **Returns**: `LivelinessTokenBuilder` — must be `.await`ed or `.wait()`ed to actually declare.
- **Resolves to**: `ZResult<LivelinessToken>`

`LivelinessTokenBuilder` has no additional configuration options — tokens are declared as-is.

---

#### `LivelinessToken`

```rust
pub struct LivelinessToken {
    session: WeakSession,
    id: Id,
    undeclare_on_drop: bool,  // true by default
}
```

Methods:

```rust
// Explicitly undeclare the token. Immediate notification to observers.
pub fn undeclare(self) -> impl Resolve<ZResult<()>>
// Usage: token.undeclare().await.unwrap();
```

Dropping the token without calling `undeclare()` also undeclares it (via the `Drop` implementation), but any error from undeclare is logged and swallowed rather than returned.

---

#### `Liveliness::declare_subscriber(key_expr) -> LivelinessSubscriberBuilder`

Subscribe to liveliness changes.

```rust
pub fn declare_subscriber<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessSubscriberBuilder<'a, 'b, DefaultHandler>
```

Builder options:

```rust
// Set whether to query existing tokens at subscription time (default: false)
.history(bool) -> Self

// Use a callback handler (fires synchronously in the Zenoh thread)
.callback(|sample: Sample| { ... }) -> LivelinessSubscriberBuilder<'a, 'b, Callback<Sample>>

// Use a mutable callback (never called concurrently)
.callback_mut(|sample: Sample| { ... }) -> LivelinessSubscriberBuilder<'a, 'b, Callback<Sample>>

// Use a custom handler (e.g., flume channel)
.with(handler) -> LivelinessSubscriberBuilder<'a, 'b, Handler>

// Run subscriber in background until session closes (no Subscriber object returned)
.background() -> LivelinessSubscriberBuilder<'a, 'b, Callback<Sample>, true>
```

Resolves to: `ZResult<Subscriber<H>>` (or `ZResult<()>` for background variant).

The `Subscriber<H>` provides:
```rust
subscriber.recv_async().await  // async receive
subscriber.recv()              // blocking receive
subscriber.undeclare().await   // stop the subscriber
```

---

#### `Liveliness::get(key_expr) -> LivelinessGetBuilder`

Query currently alive tokens.

```rust
pub fn get<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessGetBuilder<'a, 'b, DefaultHandler>
```

Builder options:

```rust
// Set query timeout (default: session.queries_default_timeout(), typically 10s)
.timeout(Duration) -> Self

// Use callback handler
.callback(|reply: Reply| { ... }) -> LivelinessGetBuilder<'a, 'b, Callback<Reply>>

// Use mutable callback
.callback_mut(|reply: Reply| { ... }) -> LivelinessGetBuilder<'a, 'b, Callback<Reply>>

// Use custom handler
.with(handler) -> LivelinessGetBuilder<'a, 'b, Handler>

// Provide a cancellation token (unstable feature)
.cancellation_token(ct) -> Self
```

Resolves to: `ZResult<H::Handler>` — the handler receives `Reply` values.

Each `Reply` contains:
```rust
reply.result()  // -> Result<&Sample, &ReplyError>
// Sample fields:
sample.key_expr()   // -> &KeyExpr — the token's key expression
sample.payload()    // -> &ZBytes — empty for liveliness tokens
sample.kind()       // -> SampleKind::Put (always Put for get() results)
```

---

### Python API

#### `session.liveliness()`

Returns the `Liveliness` accessor.

---

#### `liveliness.declare_token(key_expr: str) -> LivelinessToken`

Returns a context-manager-compatible token object.

```python
# Context manager (preferred — auto-undeclares)
with session.liveliness().declare_token("group1/svc-a") as token:
    pass  # token undeclared when block exits

# Manual (must call undeclare() or use as context manager)
token = session.liveliness().declare_token("group1/svc-a")
token.undeclare()
```

---

#### `liveliness.declare_subscriber(key_expr: str, *, history: bool = False) -> Subscriber`

Subscribe to liveliness changes.

```python
# Default (no history)
sub = session.liveliness().declare_subscriber("group1/**")

# With history (see pre-existing tokens)
sub = session.liveliness().declare_subscriber("group1/**", history=True)

# Use as iterable (blocking)
for sample in sub:
    if sample.kind == zenoh.SampleKind.PUT:
        print(f"alive: {sample.key_expr}")
    elif sample.kind == zenoh.SampleKind.DELETE:
        print(f"dropped: {sample.key_expr}")

# Use as context manager
with session.liveliness().declare_subscriber("group1/**", history=True) as sub:
    for sample in sub:
        ...
```

---

#### `liveliness.get(key_expr: str, *, timeout: float = 10.0) -> Iterable[Reply]`

Query currently alive tokens. Returns an iterable of `Reply` objects.

```python
replies = session.liveliness().get("group1/**", timeout=5.0)
for reply in replies:
    try:
        print(f"alive: {reply.ok.key_expr}")
    except Exception:
        print(f"error: {reply.err.payload.to_string()}")
```

- `timeout`: seconds (float), default 10.0
- `reply.ok`: the `Sample` on success (`reply.ok.key_expr` is the token key)
- `reply.err`: the error on failure

---

## Quick Reference

| Operation | Rust | Python |
|-----------|------|--------|
| Declare token | `session.liveliness().declare_token("k").await?` | `session.liveliness().declare_token("k")` |
| Undeclare token | `token.undeclare().await?` | context manager exit or `token.undeclare()` |
| Subscribe (no history) | `.declare_subscriber("k/**").await?` | `.declare_subscriber("k/**")` |
| Subscribe (with history) | `.declare_subscriber("k/**").history(true).await?` | `.declare_subscriber("k/**", history=True)` |
| Query snapshot | `.get("k/**").await?` | `.get("k/**")` |
| Query with timeout | `.get("k/**").timeout(Duration::from_secs(5)).await?` | `.get("k/**", timeout=5.0)` |
| Check Put event | `SampleKind::Put` | `zenoh.SampleKind.PUT` |
| Check Delete event | `SampleKind::Delete` | `zenoh.SampleKind.DELETE` |
| Handle all-connectivity-lost | `if key == "**" { registry.clear() }` | `if key == "**": registry.clear()` |

## See Also

- [Key Expressions Guide](key-expressions-guide.md) — key expression syntax used when declaring liveliness tokens and subscribers
- [Queryable Complete Guide](queryable-complete-guide.md) — the query/reply pattern used internally by liveliness's `get()` method
- [Programming Model Guide](programming-model-guide.md) — the session API that exposes `session.liveliness()` alongside pub/sub and query
