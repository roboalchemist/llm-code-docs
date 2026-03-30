# Zenoh Matching Status Guide

> **Stability note**: The Matching Status API is marked **unstable** in the RFC. The core `matching_status()` and `matching_listener()` methods are available in stable builds; some advanced features (e.g. `wait_callbacks()`) require the `unstable` feature flag.

## Table of Contents

- [Overview](#overview)
- [MatchingStatus](#matchingstatus)
  - [What It Reports](#what-it-reports)
  - [Rust API](#rust-api)
  - [Python API](#python-api)
  - [Return Type Reference](#return-type-reference)
- [MatchingListener](#matchinglistener)
  - [What It Does](#what-it-does)
  - [Lifecycle](#lifecycle)
  - [Rust API — Channel-Based (Default)](#rust-api-channel-based-default)
  - [Rust API — Callback-Based](#rust-api-callback-based)
  - [Rust API — Mutable Callback](#rust-api-mutable-callback)
  - [Rust API — Custom Handler (e.g. flume channel)](#rust-api-custom-handler-eg-flume-channel)
  - [Python API — Iterator-Based (Default)](#python-api-iterator-based-default)
  - [Python API — Callback-Based](#python-api-callback-based)
  - [Python API — Context Manager](#python-api-context-manager)
  - [Undeclaring Explicitly](#undeclaring-explicitly)
- [Use Cases](#use-cases)
  - [Conditional Publishing — Only Publish When Someone Listens](#conditional-publishing-only-publish-when-someone-listens)
  - [Adaptive Behavior — Vary Rate or Verbosity Based on Subscribers](#adaptive-behavior-vary-rate-or-verbosity-based-on-subscribers)
  - [Backpressure Detection](#backpressure-detection)
  - [Service Discovery Pattern](#service-discovery-pattern)
- [Limitations](#limitations)
  - [What MatchingStatus Does NOT Tell You](#what-matchingstatus-does-not-tell-you)
  - [Race Conditions](#race-conditions)
- [Full API Reference](#full-api-reference)
  - [Rust](#rust)
  - [Python](#python)
- [Relationship to Other Zenoh Features](#relationship-to-other-zenoh-features)

## Overview

Matching Status lets a Publisher (or Querier) ask a simple question: *"Is anyone listening?"* Specifically:

- **MatchingStatus** — a point-in-time snapshot: does at least one Subscriber currently match this Publisher's key expression?
- **MatchingListener** — an asynchronous watcher: get notified each time the answer changes (0→1 subscriber, or 1→0 subscribers).

This is cheaper than using [Liveliness](https://zenoh.io/docs/manual/liveliness/) for the same purpose, because it requires no extra token declarations on the subscriber side. The information already exists inside the Zenoh local infrastructure (which must track it for writer-side filtering), so exposing it to the application adds essentially no overhead.

---

## MatchingStatus

### What It Reports

`MatchingStatus` contains a single boolean field that answers: *does at least one Subscriber exist whose key expression intersects the Publisher's key expression?*

It does **not** tell you:
- How many subscribers exist (just ≥1 or 0)
- Whether subscribers are keeping up with the publication rate
- Whether remote subscribers over multi-hop routers are reachable

The struct is intentionally opaque (a struct with a method, not a bare `bool`) to allow backward-compatible additions in future releases.

### Rust API

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session.declare_publisher("demo/sensor/temperature").await.unwrap();

    // Point-in-time check
    let status: bool = publisher
        .matching_status()
        .await
        .unwrap()
        .matching();

    if status {
        println!("At least one subscriber is present — safe to publish");
    } else {
        println!("No subscribers — skip expensive data acquisition");
    }
}
```

`publisher.matching_status()` returns a `Resolve<ZResult<MatchingStatus>>`. Await it (or call `.wait()` in synchronous contexts) to get `ZResult<MatchingStatus>`, then call `.matching()` to extract the `bool`.

### Python API

```python
import zenoh

session = zenoh.open(zenoh.Config())
publisher = session.declare_publisher("demo/sensor/temperature")

# Point-in-time check via property accessor
status = publisher.matching_status

if status.matching:
    print("At least one subscriber is present")
else:
    print("No subscribers")

session.close()
```

In Python, `publisher.matching_status` is a **property** (not a method call), and returns a `MatchingStatus` object. Call `.matching` on it to get the `bool`. Note: `if publisher.matching_status:` will always be truthy because it returns an object, not a bool — always use `publisher.matching_status.matching`.

### Return Type Reference

| Language | Call | Return Type | Access |
|----------|------|-------------|--------|
| Rust | `publisher.matching_status().await.unwrap()` | `MatchingStatus` | `.matching() -> bool` |
| Python | `publisher.matching_status` | `MatchingStatus` | `.matching -> bool` |

---

## MatchingListener

### What It Does

A `MatchingListener` watches for changes in the Publisher's matching status and delivers a `MatchingStatus` notification each time the count of matching subscribers crosses a threshold:

- **0 → 1**: First subscriber appears. Callback fires with `matching() == true`.
- **1 → 0**: Last subscriber disappears. Callback fires with `matching() == false`.

Intermediate changes (e.g. 1 → 2 → 3 → 2 subscribers) do **not** produce notifications; the listener only fires when the binary state flips.

**Initial state**: When you declare a `MatchingListener`, it does **not** immediately fire a callback with the current state. You receive the first notification only when the state *changes*. To know the current state at startup, call `publisher.matching_status()` once after declaring the listener.

### Lifecycle

The `MatchingListener` is tied to its Publisher:
- When the Publisher is dropped (or explicitly undeclared), all its `MatchingListener` instances are automatically undeclared.
- A `MatchingListener` itself also undeclares when dropped (RAII), unless configured to run in the background.
- You can undeclare it early by calling `.undeclare()`.

### Rust API — Channel-Based (Default)

The default handler provides a channel. Use `recv_async()` in an async loop or `recv()` in a sync context.

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session.declare_publisher("demo/sensor/temperature").await.unwrap();

    // Declare listener — returns MatchingListener<DefaultHandler>
    let matching_listener = publisher.matching_listener().await.unwrap();

    // Async receive loop
    while let Ok(status) = matching_listener.recv_async().await {
        if status.matching() {
            println!("Subscriber appeared — start publishing");
        } else {
            println!("Last subscriber gone — stop publishing");
        }
    }
}
```

### Rust API — Callback-Based

For fire-and-forget use, register a callback and optionally run it in the background (no handle returned):

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session.declare_publisher("demo/sensor/temperature").await.unwrap();

    // Callback-based listener — listener lives as long as publisher does
    publisher
        .matching_listener()
        .callback(|status| {
            if status.matching() {
                println!("Subscriber appeared");
            } else {
                println!("No more subscribers");
            }
        })
        .background()  // runs until publisher is dropped, no handle returned
        .await
        .unwrap();

    // Publisher continues; listener fires automatically in background
    publisher.put("25.3°C").await.unwrap();
}
```

Without `.background()`, the returned `MatchingListener` handle is dropped at end of scope, which automatically undeclares the listener. Use `.background()` when you don't need the handle.

### Rust API — Mutable Callback

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session.declare_publisher("demo/events").await.unwrap();

    let mut event_count = 0usize;
    let _listener = publisher
        .matching_listener()
        .callback_mut(move |_status| {
            event_count += 1;
            println!("Matching status change #{}", event_count);
        })
        .await
        .unwrap();
}
```

### Rust API — Custom Handler (e.g. flume channel)

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session.declare_publisher("demo/sensor/temperature").await.unwrap();

    let (tx, rx) = flume::bounded(32);
    let _listener = publisher
        .matching_listener()
        .with((tx, rx.clone()))  // IntoHandler requires (Sender, Receiver) tuple
        .await
        .unwrap();

    // Receive from the flume receiver
    while let Ok(status) = rx.recv_async().await {
        println!("Matching: {}", status.matching());
    }
}
```

### Python API — Iterator-Based (Default)

```python
import zenoh

session = zenoh.open(zenoh.Config())
publisher = session.declare_publisher("demo/sensor/temperature")

# Declare matching listener
listener = publisher.declare_matching_listener()

# Iterate — blocks until each status arrives
for status in listener:
    if status.matching:
        print("Subscriber appeared — start publishing")
    else:
        print("Last subscriber gone — stop publishing")

session.close()
```

### Python API — Callback-Based

```python
import zenoh

def on_matching_change(status: zenoh.MatchingStatus):
    if status.matching:
        print("Subscriber appeared")
    else:
        print("No more subscribers")

session = zenoh.open(zenoh.Config())
publisher = session.declare_publisher("demo/sensor/temperature")

# Pass callback directly
listener = publisher.declare_matching_listener(on_matching_change)

# listener runs until undeclared or session closed
session.close()
```

### Python API — Context Manager

```python
import zenoh

session = zenoh.open(zenoh.Config())
publisher = session.declare_publisher("demo/sensor/temperature")

with publisher.declare_matching_listener() as listener:
    for status in listener:
        print(f"Matching: {status.matching}")
        break  # exit after first notification

session.close()
```

### Undeclaring Explicitly

**Rust:**
```rust
let listener = publisher.matching_listener().await.unwrap();
// ... later ...
listener.undeclare().await.unwrap();
```

**Python:**
```python
listener = publisher.declare_matching_listener()
# ... later ...
listener.undeclare()
```

---

## Use Cases

### Conditional Publishing — Only Publish When Someone Listens

The most common use case: avoid computing or acquiring expensive sensor data when no subscribers exist.

**Rust — complete example:**
```rust
use std::sync::{Arc, atomic::{AtomicBool, Ordering}};
use std::time::Duration;
use zenoh::Config;
use tokio::time::sleep;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session.declare_publisher("factory/sensor/vibration").await.unwrap();

    let publishing_enabled = Arc::new(AtomicBool::new(false));
    let flag = publishing_enabled.clone();

    // Check initial state before starting the listener
    let initial = publisher.matching_status().await.unwrap().matching();
    publishing_enabled.store(initial, Ordering::SeqCst);
    println!("Initial state: subscribers={}", initial);

    // Background listener flips the flag when state changes
    publisher
        .matching_listener()
        .callback(move |status| {
            let has_sub = status.matching();
            flag.store(has_sub, Ordering::SeqCst);
            if has_sub {
                println!("Subscriber appeared — starting data acquisition");
            } else {
                println!("No subscribers — suspending data acquisition");
            }
        })
        .background()
        .await
        .unwrap();

    // Publishing loop: only sample sensor when needed
    loop {
        if publishing_enabled.load(Ordering::SeqCst) {
            let reading = read_vibration_sensor(); // expensive FFT
            publisher.put(reading).await.unwrap();
        }
        sleep(Duration::from_millis(100)).await;
    }
}

fn read_vibration_sensor() -> f64 {
    // Simulate expensive sensor acquisition
    42.7
}
```

**Python — complete example:**
```python
import zenoh
import threading
import time

session = zenoh.open(zenoh.Config())
publisher = session.declare_publisher("factory/sensor/vibration")

publishing_enabled = threading.Event()

# Check initial state
if publisher.matching_status.matching:
    publishing_enabled.set()
    print("Initial state: subscribers present")

def on_matching_change(status: zenoh.MatchingStatus):
    if status.matching:
        publishing_enabled.set()
        print("Subscriber appeared — starting data acquisition")
    else:
        publishing_enabled.clear()
        print("No subscribers — suspending data acquisition")

listener = publisher.declare_matching_listener(on_matching_change)

def publishing_loop():
    while True:
        if publishing_enabled.is_set():
            reading = read_vibration_sensor()  # expensive FFT
            publisher.put(reading)
        time.sleep(0.1)

def read_vibration_sensor() -> float:
    return 42.7  # simulate expensive sensor acquisition

t = threading.Thread(target=publishing_loop, daemon=True)
t.start()

# Run for a while then clean up
time.sleep(60)
listener.undeclare()
session.close()
```

---

### Adaptive Behavior — Vary Rate or Verbosity Based on Subscribers

**Pattern: reduce publish frequency when no subscribers exist (battery saving):**

**Rust:**
```rust
use std::sync::{Arc, Mutex};
use std::time::Duration;
use zenoh::Config;
use tokio::time::sleep;

#[derive(Clone)]
struct PublishConfig {
    interval_ms: u64,
    verbose: bool,
}

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session.declare_publisher("sensor/telemetry").await.unwrap();

    let config = Arc::new(Mutex::new(PublishConfig {
        interval_ms: 5000,  // 5s default: no subscribers
        verbose: false,
    }));
    let cfg = config.clone();

    publisher
        .matching_listener()
        .callback(move |status| {
            let mut c = cfg.lock().unwrap();
            if status.matching() {
                c.interval_ms = 100;   // 10 Hz when subscribers present
                c.verbose = true;
                println!("High-rate mode: subscriber connected");
            } else {
                c.interval_ms = 5000;  // 0.2 Hz in standby
                c.verbose = false;
                println!("Low-rate mode: no subscribers");
            }
        })
        .background()
        .await
        .unwrap();

    loop {
        let (interval, verbose) = {
            let c = config.lock().unwrap();
            (c.interval_ms, c.verbose)
        };
        let payload = if verbose {
            "temp=25.3 hum=62.1 pres=1013.2 lat=51.5 lon=-0.1"
        } else {
            "alive"
        };
        publisher.put(payload).await.unwrap();
        sleep(Duration::from_millis(interval)).await;
    }
}
```

**Python:**
```python
import zenoh
import threading
import time

session = zenoh.open(zenoh.Config())
publisher = session.declare_publisher("sensor/telemetry")

config_lock = threading.Lock()
publish_interval = 5.0   # seconds
verbose_mode = False

def on_matching_change(status: zenoh.MatchingStatus):
    global publish_interval, verbose_mode
    with config_lock:
        if status.matching:
            publish_interval = 0.1   # 10 Hz
            verbose_mode = True
            print("High-rate mode: subscriber connected")
        else:
            publish_interval = 5.0   # 0.2 Hz
            verbose_mode = False
            print("Low-rate mode: no subscribers")

listener = publisher.declare_matching_listener(on_matching_change)

while True:
    with config_lock:
        interval = publish_interval
        payload = (
            "temp=25.3 hum=62.1 pres=1013.2"
            if verbose_mode
            else "alive"
        )
    publisher.put(payload)
    time.sleep(interval)
```

---

### Backpressure Detection

Matching Status and `CongestionControl` address different problems:

| | Matching Status | CongestionControl |
|---|---|---|
| **Level** | Application-level | Transport-level |
| **Question** | "Is anyone subscribed?" | "Is the network dropping messages?" |
| **When to use** | Skip computation when no consumers exist | Handle network saturation |
| **Granularity** | Binary (≥1 or 0 subscribers) | Per-message drop policy |
| **Overhead** | Zero at publish time | Applied per-put |

Use `MatchingStatus` to implement **application-level backpressure** — avoid generating data that will have no consumers. Use `CongestionControl::Drop` or `CongestionControl::Block` for **transport-level** behavior when the network queue is full.

**Rust — combined approach:**
```rust
use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Arc;
use zenoh::{Config, qos::CongestionControl};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let publisher = session
        .declare_publisher("pipeline/frames")
        .congestion_control(CongestionControl::Drop)  // transport: drop if queue full
        .await
        .unwrap();

    let has_subscribers = Arc::new(AtomicBool::new(false));
    let flag = has_subscribers.clone();

    // Application-level: skip encoding if no one is listening
    publisher
        .matching_listener()
        .callback(move |s| flag.store(s.matching(), Ordering::SeqCst))
        .background()
        .await
        .unwrap();

    // Application loop
    loop {
        if has_subscribers.load(Ordering::SeqCst) {
            // Only encode the frame when someone needs it
            let encoded_frame = encode_video_frame();
            // CongestionControl::Drop handles network saturation at transport level
            publisher.put(encoded_frame).await.unwrap();
        }
    }
}

fn encode_video_frame() -> Vec<u8> {
    vec![0u8; 640 * 480 * 3]  // simulate frame encoding
}
```

---

### Service Discovery Pattern

Treat a Publisher as a **service endpoint** and use `MatchingListener` to detect when clients connect or disconnect. Initialize expensive resources (database connections, hardware locks, compute threads) only when clients are present, and release them when the last client disconnects.

**Rust — complete example:**
```rust
use std::sync::{Arc, Mutex};
use zenoh::Config;

struct ExpensiveResource {
    // e.g. database connection, hardware lock, GPU context
    name: String,
}

impl ExpensiveResource {
    fn initialize(name: &str) -> Self {
        println!("Initializing expensive resource: {}", name);
        ExpensiveResource { name: name.to_string() }
    }
}

impl Drop for ExpensiveResource {
    fn drop(&mut self) {
        println!("Releasing expensive resource: {}", self.name);
    }
}

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session.declare_publisher("service/lidar/pointcloud").await.unwrap();

    let resource: Arc<Mutex<Option<ExpensiveResource>>> = Arc::new(Mutex::new(None));
    let res = resource.clone();

    publisher
        .matching_listener()
        .callback(move |status| {
            let mut guard = res.lock().unwrap();
            if status.matching() {
                // First client connected — initialize
                if guard.is_none() {
                    *guard = Some(ExpensiveResource::initialize("lidar-driver"));
                }
            } else {
                // Last client disconnected — release
                *guard = None;  // Drop calls ExpensiveResource::drop
            }
        })
        .background()
        .await
        .unwrap();

    // Publishing loop — only runs when resource is initialized
    loop {
        let guard = resource.lock().unwrap();
        if guard.is_some() {
            drop(guard);  // release lock before await
            let data = scan_lidar();
            publisher.put(data).await.unwrap();
        } else {
            drop(guard);
            tokio::time::sleep(std::time::Duration::from_millis(10)).await;
        }
    }
}

fn scan_lidar() -> Vec<u8> {
    vec![0u8; 1024]  // simulate lidar scan data
}
```

**Python — complete example:**
```python
import zenoh
import threading
import time

class ExpensiveResource:
    def __init__(self, name: str):
        print(f"Initializing expensive resource: {name}")
        self.name = name
        # e.g. open serial port, allocate GPU memory, connect to database

    def close(self):
        print(f"Releasing expensive resource: {self.name}")
        # cleanup

session = zenoh.open(zenoh.Config())
publisher = session.declare_publisher("service/lidar/pointcloud")

resource_lock = threading.Lock()
resource: ExpensiveResource | None = None

def on_client_connection_change(status: zenoh.MatchingStatus):
    global resource
    with resource_lock:
        if status.matching and resource is None:
            resource = ExpensiveResource("lidar-driver")
        elif not status.matching and resource is not None:
            resource.close()
            resource = None

# Check if clients already present at startup
if publisher.matching_status.matching:
    resource = ExpensiveResource("lidar-driver")

listener = publisher.declare_matching_listener(on_client_connection_change)

def publishing_loop():
    while True:
        with resource_lock:
            active = resource is not None
        if active:
            data = scan_lidar()
            publisher.put(data)
        time.sleep(0.033)  # ~30 Hz

def scan_lidar() -> bytes:
    return bytes(1024)  # simulate lidar scan

t = threading.Thread(target=publishing_loop, daemon=True)
t.start()

time.sleep(300)  # run for 5 minutes
listener.undeclare()
with resource_lock:
    if resource is not None:
        resource.close()
session.close()
```

---

## Limitations

### What MatchingStatus Does NOT Tell You

**It's binary — no subscriber count.** `matching()` returns `true` if ≥1 subscriber exists, and `false` if 0 exist. There is no way to ask "how many subscribers are there?" If you need subscriber counts, you must maintain them yourself via some external coordination mechanism (e.g. Liveliness tokens).

**It doesn't indicate subscriber health.** A subscriber that exists but is slow, blocked, or deadlocked still shows as `matching() == true`. MatchingStatus has no concept of throughput, queue depth, or consumer lag.

**Multi-hop routing.** Matching Status reflects the Zenoh local infrastructure's view of the network. Subscribers reachable through Zenoh routers are included — the system is topology-aware. However, in split-brain scenarios or during router reconnection, there can be a brief window where the local view is stale.

### Race Conditions

There is an inherent race between checking `matching_status()` and acting on the result. A subscriber can appear or disappear between the status check and the first `put()`. This is expected behavior and usually not a problem — the worst case is one missed publication or one unnecessary publication.

To handle this correctly:
1. Declare the `MatchingListener` first.
2. Then call `matching_status()` once to get the current state.
3. Use the listener for all subsequent state changes.

This ensures no state changes are missed between setup and steady-state operation.

```rust
// Correct startup sequence
let publisher = session.declare_publisher("key/expr").await.unwrap();

// 1. Declare listener first (captures all future changes)
let listener = publisher.matching_listener().await.unwrap();

// 2. Then sample current state (no gap)
let current = publisher.matching_status().await.unwrap().matching();
println!("Current state: {}", current);

// 3. Listen for changes going forward
while let Ok(status) = listener.recv_async().await {
    println!("State changed: {}", status.matching());
}
```

---

## Full API Reference

### Rust

#### `MatchingStatus`

```rust
pub struct MatchingStatus { /* private */ }

impl MatchingStatus {
    /// Returns true if at least one Subscriber matches the Publisher's key expression.
    pub fn matching(&self) -> bool;
}
```

#### `Publisher` matching methods

```rust
impl<'a> Publisher<'a> {
    /// Point-in-time check. Async — must be awaited.
    pub fn matching_status(&self) -> impl Resolve<ZResult<MatchingStatus>> + '_;

    /// Returns a builder for declaring a MatchingListener.
    pub fn matching_listener(&self) -> MatchingListenerBuilder<'_, DefaultHandler>;
}
```

#### `MatchingListenerBuilder` methods

```rust
impl<'a> MatchingListenerBuilder<'a, DefaultHandler> {
    /// Register a thread-safe callback. Fn(MatchingStatus) + Send + Sync + 'static.
    pub fn callback<F>(self, callback: F) -> MatchingListenerBuilder<'a, Callback<MatchingStatus>>;

    /// Register a mutable callback (wrapped in a Mutex internally).
    pub fn callback_mut<F>(self, callback: F) -> MatchingListenerBuilder<'a, Callback<MatchingStatus>>;

    /// Use a custom handler type (e.g. flume channel, crossbeam channel).
    pub fn with<Handler>(self, handler: Handler) -> MatchingListenerBuilder<'a, Handler>;
}

impl<'a> MatchingListenerBuilder<'a, Callback<MatchingStatus>> {
    /// Run in background — no handle returned, lives until publisher is dropped.
    pub fn background(self) -> MatchingListenerBuilder<'a, Callback<MatchingStatus>, true>;
}
```

Resolve the builder with `.await` or `.wait()` to get `ZResult<MatchingListener<Handler>>`.

#### `MatchingListener<Handler>`

```rust
pub struct MatchingListener<Handler> { /* private */ }

impl<Handler> MatchingListener<Handler> {
    /// Explicitly undeclare the listener.
    pub fn undeclare(self) -> MatchingListenerUndeclaration<Handler>;

    /// Access the underlying handler.
    pub fn handler(&self) -> &Handler;
    pub fn handler_mut(&mut self) -> &mut Handler;
}

impl<Handler> Drop for MatchingListener<Handler> {
    // Automatically undeclares on drop (unless .background() was used)
}
```

The `MatchingListener<DefaultHandler>` also implements `Deref` to `DefaultHandler`, giving access to `.recv()`, `.recv_async()`, and `.try_recv()` directly on the listener.

#### Unstable: `wait_callbacks()`

With the `unstable` feature flag, you can block until all in-flight callbacks complete:

```rust
listener.undeclare().wait_callbacks().await.unwrap();
// or on publisher undeclare:
publisher.undeclare().wait_callbacks().await.unwrap();
```

---

### Python

#### `MatchingStatus`

```python
class MatchingStatus:
    @property
    def matching(self) -> bool:
        """True if at least one matching Subscriber (or Queryable) exists."""
```

#### `Publisher` matching methods

```python
class Publisher:
    @property
    def matching_status(self) -> MatchingStatus:
        """Returns MatchingStatus object; use .matching property to get bool."""

    def declare_matching_listener(
        self,
        handler: Callable[[MatchingStatus], None]   # callback
              | RustHandler[MatchingStatus]          # built-in channel
              | None                                 # default channel
    ) -> MatchingListener[Handler[MatchingStatus]]
              | MatchingListener[None]:
        """Create a MatchingListener. Fires each time matching status changes."""
```

#### `MatchingListener[H]`

```python
class MatchingListener(Generic[H]):
    @property
    def handler(self) -> H:
        """The underlying handler (a channel or None for callback-based)."""

    def try_recv(self: MatchingListener[Handler[MatchingStatus]]) -> MatchingStatus | None:
        """Non-blocking receive. Returns None if no notification is ready."""

    def recv(self: MatchingListener[Handler[MatchingStatus]]) -> MatchingStatus:
        """Blocking receive. Blocks until a notification arrives."""

    def __iter__(self) -> Iterator[MatchingStatus]:
        """Iterate over notifications. Blocks between each."""

    def undeclare(self) -> None:
        """Explicitly undeclare this listener."""

    def __enter__(self) -> MatchingListener: ...
    def __exit__(self, *args) -> None: ...  # calls undeclare()
```

---

## Relationship to Other Zenoh Features

| Feature | Mechanism | Use When |
|---------|-----------|----------|
| **MatchingStatus** | Built-in infrastructure query | Publisher wants to know if any subscriber exists, zero overhead |
| **Liveliness** | Separate token declarations | You need subscriber identity, cross-session visibility, or fine-grained presence tracking |
| **CongestionControl** | Per-message transport policy | Network queue is full and you want to drop or block messages |
| **QoS Priority** | Per-message routing priority | Some messages matter more than others under load |

## See Also

- [Key Expressions Guide](key-expressions-guide.md) — key expression intersection is the mechanism that determines whether a publisher "matches" a subscriber
- [QoS Guide](qos-guide.md) — CongestionControl and Priority that work alongside MatchingStatus for full publisher control
- [Programming Model Guide](programming-model-guide.md) — how MatchingStatus fits into the broader publisher lifecycle
