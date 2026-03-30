# Zenoh Quality of Service (QoS) Complete Guide

Zenoh provides fine-grained control over message delivery behavior through a set of QoS
parameters. These parameters govern how messages are prioritized, how delivery is
guaranteed, what happens under congestion, and when messages get dropped or filtered.

---

## Table of Contents

- [Quick Reference Table](#quick-reference-table)
- [Priority](#priority)
  - [Priority Levels](#priority-levels)
  - [How Priority Works at the Transport Layer](#how-priority-works-at-the-transport-layer)
  - [When to Use Each Priority Level](#when-to-use-each-priority-level)
  - [Default Priority](#default-priority)
  - [API: Setting Priority](#api-setting-priority)
- [Reliability](#reliability)
  - [Modes](#modes)
  - [What Reliability Actually Does](#what-reliability-actually-does)
  - [When Reliability Fails](#when-reliability-fails)
  - [Performance Overhead](#performance-overhead)
  - [Default Reliability](#default-reliability)
  - [API: Setting Reliability (Unstable)](#api-setting-reliability-unstable)
- [Congestion Control](#congestion-control)
  - [Modes](#modes)
  - [`wait_before_drop` (Drop Behavior Tuning)](#wait_before_drop-drop-behavior-tuning)
  - [`wait_before_close` (Block Behavior Tuning)](#wait_before_close-block-behavior-tuning)
  - [When to Use Drop vs Block](#when-to-use-drop-vs-block)
  - [API: Setting Congestion Control](#api-setting-congestion-control)
- [Express](#express)
  - [What Express Does](#what-express-does)
  - [When to Use Express](#when-to-use-express)
  - [Default](#default)
  - [API: Setting Express](#api-setting-express)
- [Locality (allowed_destination)](#locality-allowed_destination)
  - [Modes](#modes)
  - [Use Cases](#use-cases)
  - [API: Setting Locality](#api-setting-locality)
- [QoS Overrides in Configuration](#qos-overrides-in-configuration)
  - [1. Publication-Level Overrides (`qos.publication`)](#1-publication-level-overrides-qospublication)
  - [2. Network-Level Overrides (`qos.network`)](#2-network-level-overrides-qosnetwork)
  - [Example: Force All `/safety/**` to RealTime + Block](#example-force-all-safety-to-realtime-block)
- [Downsampling (Frequency Limiting)](#downsampling-frequency-limiting)
  - [Configuration Location](#configuration-location)
  - [Full Syntax](#full-syntax)
  - [Fields](#fields)
  - [How Downsampling Interacts with QoS](#how-downsampling-interacts-with-qos)
  - [Use Case: Rate-Limiting LIDAR over WAN](#use-case-rate-limiting-lidar-over-wan)
- [Low-Pass Filter (Size Limiting)](#low-pass-filter-size-limiting)
  - [Configuration Location](#configuration-location)
  - [Full Syntax](#full-syntax)
  - [Fields](#fields)
  - [Behavior When Message Exceeds Limit](#behavior-when-message-exceeds-limit)
  - [Use Case: Preventing Large Messages on Low-Bandwidth Links](#use-case-preventing-large-messages-on-low-bandwidth-links)
- [Channel: Priority × Reliability](#channel-priority-reliability)
  - [How Channels Map to Queues](#how-channels-map-to-queues)
  - [Why This Matters: Head-of-Line Blocking](#why-this-matters-head-of-line-blocking)
  - [Practical Implication](#practical-implication)
- [Queue Configuration](#queue-configuration)
- [Complete Example: Mixed-QoS Robotics Application](#complete-example-mixed-qos-robotics-application)

## Quick Reference Table

| Parameter | Type | Default | Stable? | Where Set |
|-----------|------|---------|---------|-----------|
| `priority` | `Priority` enum | `Data` (5) | Yes | Publisher, put/delete |
| `reliability` | `Reliability` enum | `Reliable` | **Unstable** | Publisher |
| `congestion_control` | `CongestionControl` enum | `Drop` | Yes | Publisher, put/delete |
| `express` | `bool` | `false` | Yes | Publisher, put/delete |
| `allowed_destination` (Locality) | `Locality` enum | `Any` | **Unstable** | Publisher |
| `wait_before_drop` | `u64` µs | `1000` | Yes | Config only |
| `wait_before_close` | `u64` µs | `5_000_000` | Yes | Config only |
| Downsampling `freq` | `f64` Hz | — | Yes | Config only |
| Low-pass filter `size_limit` | `u64` bytes | — | Yes | Config only |

---

## Priority

### Priority Levels

Priority controls the scheduling order in the transport layer's per-priority queues.
Messages in higher-priority queues are sent before lower-priority queues drain.
Lower numeric value = higher priority.

| Level | Value | Config String | Rust | Python |
|-------|-------|---------------|------|--------|
| RealTime | 1 | `"real_time"` | `Priority::RealTime` | `Priority.REAL_TIME` |
| InteractiveHigh | 2 | `"interactive_high"` | `Priority::InteractiveHigh` | `Priority.INTERACTIVE_HIGH` |
| InteractiveLow | 3 | `"interactive_low"` | `Priority::InteractiveLow` | `Priority.INTERACTIVE_LOW` |
| DataHigh | 4 | `"data_high"` | `Priority::DataHigh` | `Priority.DATA_HIGH` |
| **Data** | **5** | `"data"` | `Priority::Data` *(default)* | `Priority.DATA` *(default)* |
| DataLow | 6 | `"data_low"` | `Priority::DataLow` | `Priority.DATA_LOW` |
| Background | 7 | `"background"` | `Priority::Background` | `Priority.BACKGROUND` |

There is also an internal `Control` level (0) reserved for Zenoh protocol internals
(session management, declarations, routing). It is not exposed in the public API.

### How Priority Works at the Transport Layer

Each link has a separate transmission queue for each priority level. The scheduler
services higher-priority queues before lower-priority ones, so a RealTime message
enqueued while DataLow messages are waiting will bypass the DataLow queue entirely.

Queue sizes are configurable per priority (see **Queue Configuration** below). Each
queue holds a number of *batches*, where each batch is up to `batch_size` bytes (default
65535). The default queue depth is 2 batches per priority.

### When to Use Each Priority Level

| Priority | Use Case |
|----------|----------|
| RealTime | Safety-critical commands (emergency stop, actuator override), hard real-time loops |
| InteractiveHigh | Human-in-the-loop control (joystick input, teleoperation), UI feedback |
| InteractiveLow | Soft real-time feedback (status displays, dashboards) |
| DataHigh | High-frequency sensors that must not be delayed (IMU at 1 kHz) |
| Data | Normal sensor streams (camera frames, LIDAR scans) — default |
| DataLow | Low-priority telemetry, optional diagnostics |
| Background | Logging, bulk file transfer, configuration sync, firmware updates |

### Default Priority

The default priority is `Data` (5) for both `session.put()` and `session.declare_publisher()`.

### API: Setting Priority

**Rust — on a one-off put:**
```rust
use zenoh::qos::Priority;

let session = zenoh::open(zenoh::Config::default()).await.unwrap();
session
    .put("robot/cmd/estop", "true")
    .priority(Priority::RealTime)
    .await
    .unwrap();
```

**Rust — on a declared publisher:**
```rust
use zenoh::qos::Priority;

let publisher = session
    .declare_publisher("sensor/imu")
    .priority(Priority::DataHigh)
    .await
    .unwrap();

publisher.put(imu_bytes).await.unwrap();
```

**Python — on a one-off put:**
```python
import zenoh

session = zenoh.open(zenoh.Config())
session.put("robot/cmd/estop", b"true", priority=zenoh.Priority.REAL_TIME)
```

**Python — on a declared publisher:**
```python
publisher = session.declare_publisher(
    "sensor/imu",
    priority=zenoh.Priority.DATA_HIGH,
)
publisher.put(imu_bytes)
```

---

## Reliability

### Modes

| Mode | Value | Rust | Python |
|------|-------|------|--------|
| **Reliable** | 1 | `Reliability::Reliable` *(default)* | `Reliability.RELIABLE` |
| BestEffort | 0 | `Reliability::BestEffort` | `Reliability.BEST_EFFORT` |

> **Important:** `Reliability` is an **unstable API** as of Zenoh 1.x. Enable the
> `unstable` feature flag in Rust or use the unstable Python bindings to access it.

### What Reliability Actually Does

Despite its name, `Reliability` in Zenoh is **not a retransmission protocol**. The
source code comment from `publisher.rs` is explicit:

> "Currently `reliability` does not trigger any data retransmission on the wire. It is
> rather used as a marker on the wire and it may be used to select the best link
> available (e.g. TCP for reliable data and UDP for best effort data)."

In practice:
- **Reliable** marks the message as requiring a reliable transport. Zenoh will prefer
  TCP, TLS, QUIC, or other connection-oriented links for routing. These links handle
  retransmission at the transport layer.
- **BestEffort** marks the message as tolerating loss. Zenoh may route over UDP or
  other datagram-based links, which have lower overhead but no retransmission.

Within a reliable transport like TCP, **all messages are delivered in order** by the
transport protocol itself. Zenoh does not add sequence numbers on top of TCP's guarantees.

### When Reliability Fails

- **Network partition**: Both modes lose messages when the network is split. TCP will
  buffer until the timeout (`wait_before_close`, default 5 seconds) and then close the
  session.
- **Buffer overflow**: When queues fill faster than they drain, `CongestionControl` takes
  over (see below). `Reliability::Reliable` combined with `CongestionControl::Block` will
  back-pressure the publisher rather than drop.
- **Session close**: Queued-but-unsent messages are lost on session close.

### Performance Overhead

`BestEffort` over UDP has lower per-message overhead than `Reliable` over TCP because:
- UDP has no ACK round-trips
- No head-of-line blocking when a packet is lost
- No TCP slow-start on new connections

Use `BestEffort` for high-frequency sensor streams where occasional loss is acceptable
and latency is more important than delivery guarantees.

### Default Reliability

The default is `Reliability::Reliable`. This reflects that Zenoh defaults to TCP
transports which naturally provide in-order delivery.

### API: Setting Reliability (Unstable)

**Rust:**
```rust
#[cfg(feature = "unstable")]
use zenoh::qos::Reliability;

let publisher = session
    .declare_publisher("sensor/camera/frames")
    .reliability(Reliability::BestEffort)
    .await
    .unwrap();
```

**Python (unstable feature required):**
```python
publisher = session.declare_publisher(
    "sensor/camera/frames",
    reliability=zenoh.Reliability.BEST_EFFORT,
)
```

---

## Congestion Control

Congestion control governs what happens when the transmission queue for a given priority
is full (no available batch to enqueue into).

### Modes

| Mode | Rust | Python | Config String | Default? |
|------|------|--------|---------------|---------|
| Drop | `CongestionControl::Drop` | `CongestionControl.DROP` | `"drop"` | **Yes** |
| Block | `CongestionControl::Block` | `CongestionControl.BLOCK` | `"block"` | No |
| BlockFirst | `CongestionControl::BlockFirst` | `CongestionControl.BLOCK_FIRST` | — | No (unstable) |

**Drop**: When the queue is full, the publisher waits up to `wait_before_drop`
microseconds for a batch to free up. If none frees in time, the message is silently
dropped. Zero overhead to the publisher after the wait period.

**Block**: When the queue is full, the publisher waits indefinitely for a batch to
free up. If the queue does not drain within `wait_before_close` microseconds, Zenoh
closes the transport session to prevent deadlock. This creates backpressure up to the
application.

**BlockFirst** *(unstable)*: On the first message sent with this strategy, behave like
Block. For subsequent messages while the queue remains full, behave like Drop. Useful
when you need to guarantee the first message of a burst is delivered but can tolerate
losing the rest under sustained congestion.

### `wait_before_drop` (Drop Behavior Tuning)

- **Type**: `u64` (unsigned integer, microseconds)
- **Default**: `1000` µs (1 millisecond)
- **Location**: `transport.link.tx.queue.congestion_control.drop.wait_before_drop`
- **Valid range**: 0 to any reasonable value (no explicit upper bound in config)

When a Drop-mode message arrives at a full queue, Zenoh waits this many microseconds
before actually dropping it. This provides a small congestion tolerance window — brief
bursts that clear within the wait period will not drop any messages, while sustained
congestion will result in drops without blocking the publisher.

Setting `wait_before_drop: 0` gives true zero-wait drop behavior (good for ultra
low-latency sensor streams where stale data is worse than no data).

Setting `wait_before_drop` to a higher value (e.g., 50000 = 50 ms) tolerates longer
bursts at the cost of increased latency variance.

There is also `max_wait_before_drop_fragments` (default 50000 µs) which applies to
multi-fragment messages (messages larger than one batch). This prevents a fragmented
message from being abandoned mid-send.

### `wait_before_close` (Block Behavior Tuning)

- **Type**: `u64` (microseconds)
- **Default**: `5_000_000` µs (5 seconds)
- **Location**: `transport.link.tx.queue.congestion_control.block.wait_before_close`

If a Block-mode message cannot be enqueued within this time, Zenoh considers the
transport session deadlocked and closes it. This is a safety valve to prevent
applications from hanging indefinitely on a broken link.

### When to Use Drop vs Block

| Scenario | Recommendation |
|----------|---------------|
| Sensor streams (camera, LIDAR, IMU) | `Drop` — stale data is useless |
| Actuator commands, emergency stop | `Block` — every command must arrive |
| Log aggregation | `Drop` — losing a log line is acceptable |
| Configuration updates | `Block` — must arrive reliably |
| High-frequency control at DataHigh priority | `Drop` with short `wait_before_drop` |

### API: Setting Congestion Control

**Rust:**
```rust
use zenoh::qos::CongestionControl;

// One-off put with blocking
session
    .put("robot/cmd/actuator", command_bytes)
    .congestion_control(CongestionControl::Block)
    .await
    .unwrap();

// Declared publisher
let publisher = session
    .declare_publisher("sensor/lidar")
    .congestion_control(CongestionControl::Drop)
    .await
    .unwrap();
```

**Python:**
```python
# One-off put with blocking
session.put(
    "robot/cmd/actuator",
    command_bytes,
    congestion_control=zenoh.CongestionControl.BLOCK,
)

# Declared publisher
publisher = session.declare_publisher(
    "sensor/lidar",
    congestion_control=zenoh.CongestionControl.DROP,
)
```

---

## Express

### What Express Does

Setting `express=true` disables batching for a message. Normally, Zenoh's adaptive
batching collects multiple small messages and sends them together when the network is
under back-pressure, reducing per-message overhead. Express bypasses this: the message
is sent immediately, one message per network packet.

- **Latency impact**: Lower and more consistent latency for the express message.
- **Throughput impact**: Higher per-message overhead; reduces aggregate throughput if
  every message is express.

### When to Use Express

Use `express=true` when:
- You are publishing a time-critical update (e.g., an E-stop command, a pose correction)
  where the extra 1–2 ms of batching delay is unacceptable.
- You have a single infrequent but latency-critical event.

Do not use `express=true` by default on high-frequency publishers — the batching overhead
savings (fewer syscalls, better cache usage) are significant for throughput.

### Default

Express defaults to `false` (batching is enabled).

### API: Setting Express

**Rust:**
```rust
session
    .put("robot/cmd/estop", b"true")
    .express(true)
    .await
    .unwrap();

// On a publisher
let publisher = session
    .declare_publisher("control/pose_correction")
    .express(true)
    .await
    .unwrap();
```

**Python:**
```python
session.put("robot/cmd/estop", b"true", express=True)

publisher = session.declare_publisher(
    "control/pose_correction",
    express=True,
)
```

---

## Locality (allowed_destination)

Locality controls which subscribers receive a publication based on their location
relative to the publishing session.

> **Note:** `allowed_destination` on publishers is an **unstable API** in Zenoh 1.x.

### Modes

| Mode | Rust | Python | Description |
|------|------|--------|-------------|
| **Any** | `Locality::Any` | `Locality.ANY` | Deliver to all matching subscribers (default) |
| SessionLocal | `Locality::SessionLocal` | `Locality.SESSION_LOCAL` | Only subscribers in the same session |
| Remote | `Locality::Remote` | `Locality.REMOTE` | Only remote subscribers (not same session) |

### Use Cases

**SessionLocal**: In-process pipelines where data should not leave the local session.
Useful for testing pipelines, in-process data transformation chains, or when you
explicitly want to avoid network round-trips.

**Remote**: Publish to network peers only, avoiding delivery to any local subscriber
within the same session. Prevents echo effects when a node subscribes to its own key
expression (common in bidirectional control loops).

**Any**: Normal operation — deliver to everyone with a matching subscription.

### API: Setting Locality

**Rust:**
```rust
use zenoh::sample::Locality;

// Session-local only — won't go to the network
let publisher = session
    .declare_publisher("test/pipeline/stage1")
    .allowed_destination(Locality::SessionLocal)
    .await
    .unwrap();

// Remote only — skip any in-session subscribers
let publisher = session
    .declare_publisher("sensor/data")
    .allowed_destination(Locality::Remote)
    .await
    .unwrap();
```

**Python (unstable):**
```python
publisher = session.declare_publisher(
    "test/pipeline/stage1",
    allowed_destination=zenoh.Locality.SESSION_LOCAL,
)
```

---

## QoS Overrides in Configuration

Zenoh supports config-level QoS overrides that apply on top of (or instead of) the QoS
set in application code. This is useful for enforcing QoS policies without modifying
application source, or for network administrators who need to reclassify traffic.

There are two override mechanisms in `DEFAULT_CONFIG.json5`:

### 1. Publication-Level Overrides (`qos.publication`)

These overrides apply to PUT and DELETE messages based on key expression matching,
at the publisher side before the message enters the transport queue.

```json5
qos: {
  publication: [
    {
      // Key expressions whose publications will have QoS overridden
      key_exprs: ["safety/**", "robot/cmd/estop"],
      // Override values (all fields optional; omit to keep API-set value)
      config: {
        congestion_control: "block",   // "drop" | "block" | "block_first"
        priority: "real_time",         // see priority string names below
        express: true,                 // bool
        // unstable fields:
        reliability: "reliable",       // "reliable" | "best_effort"
        allowed_destination: "any",    // "any" | "session_local" | "remote"
      },
    },
    {
      key_exprs: ["log/**", "telemetry/**"],
      config: {
        priority: "background",
        congestion_control: "drop",
      },
    },
  ],
},
```

**Priority string names for config:**

| Priority | Config String |
|----------|--------------|
| RealTime | `"real_time"` |
| InteractiveHigh | `"interactive_high"` |
| InteractiveLow | `"interactive_low"` |
| DataHigh | `"data_high"` |
| Data | `"data"` |
| DataLow | `"data_low"` |
| Background | `"background"` |

Publication-level overrides support **relative priority adjustments** using integer
increments (e.g., `-1` to raise priority by one level, `+2` to lower by two levels),
in addition to absolute named values.

### 2. Network-Level Overrides (`qos.network`)

These overrides apply to messages passing through a transport, with more granular
matching (per-interface, per-protocol, per-ZID). They are slightly less performant
than publication overrides but offer finer control.

```json5
qos: {
  network: [
    {
      id: "wan_safety_rules",          // optional, must be unique
      // zids: ["38a4829bce9166ee"],   // optional: only apply to specific peers
      interfaces: ["eth0"],            // optional: specific network interfaces
      link_protocols: ["tcp", "tls"],  // optional: filter by transport protocol
      messages: ["put", "delete"],     // "put" | "delete" | "query"
      flows: ["egress", "ingress"],    // optional: filter by direction
      // QoS filter: only apply overwrite if message matches these QoS values
      qos: {
        priority: "data",
        congestion_control: "drop",
      },
      // Optional: filter by payload size range
      // payload_size: "1000000..",   // >= 1MB
      key_exprs: ["safety/**"],
      // What to change
      overwrite: {
        priority: "real_time",
        congestion_control: "block",
        express: true,
      },
    },
  ],
},
```

### Example: Force All `/safety/**` to RealTime + Block

```json5
qos: {
  publication: [
    {
      key_exprs: ["safety/**"],
      config: {
        priority: "real_time",
        congestion_control: "block",
        express: true,
      },
    },
  ],
},
```

This override ensures that no matter what priority/congestion setting the application
uses, safety messages always get real-time priority and block on congestion.

---

## Downsampling (Frequency Limiting)

Downsampling limits the rate at which messages matching a key expression are forwarded
across a link. Messages exceeding the configured frequency are silently dropped before
transmission.

This operates at the network layer — it applies when messages flow through or out of a
Zenoh node on a given interface, not at the publisher application.

### Configuration Location

```
downsampling: [ ... ]   (top-level in zenoh config)
```

### Full Syntax

```json5
downsampling: [
  {
    id: "wan_lidar_limit",             // optional, must be unique
    interfaces: ["wlan0"],             // optional: only on these interfaces
    link_protocols: [                  // optional: only on these transport protocols
      "tcp", "udp", "tls", "quic",
      "ws", "serial", "unixsock-stream", "unixpipe", "vsock"
    ],
    flows: ["egress"],                 // optional: "egress" | "ingress" | both
    messages: ["put", "delete"],       // required: non-empty list
                                       //   "put" | "delete" | "query" | "reply"
    rules: [
      { key_expr: "sensor/lidar/**", freq: 10.0 },  // max 10 Hz
      { key_expr: "sensor/camera/**", freq: 5.0 },  // max 5 Hz
    ],
  },
],
```

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | No | Unique identifier for this downsampling rule |
| `interfaces` | `[string]` | No | Apply only on these network interfaces; if absent, applies to all |
| `link_protocols` | `[string]` | No | Apply only on transports using these protocols; if absent, applies to all |
| `flows` | `[string]` | No | `"egress"`, `"ingress"`, or both; if absent, applies to both |
| `messages` | `[string]` | **Yes** | Message types to downsample: `"put"`, `"delete"`, `"query"`, `"reply"` |
| `rules` | array | **Yes** | List of `{ key_expr, freq }` pairs |
| `rules[].key_expr` | string | Yes | Key expression to match |
| `rules[].freq` | float (Hz) | Yes | Maximum forwarding frequency in Hz |

### How Downsampling Interacts with QoS

Downsampling is applied transparently regardless of message priority or reliability.
A `RealTime` message matched by a downsampling rule will still be dropped if it exceeds
the configured frequency. Downsampling happens before the message is scheduled for
transmission, so priority ordering within the surviving messages is preserved.

To protect high-priority traffic from downsampling, use more specific key expressions
in the downsampling rules that exclude critical key expressions.

### Use Case: Rate-Limiting LIDAR over WAN

A robot publishes LIDAR scans at 20 Hz locally but a WAN link to the cloud cannot
sustain that rate. Cap outgoing LIDAR to 2 Hz on the WAN interface:

```json5
downsampling: [
  {
    id: "wan_lidar_cap",
    interfaces: ["eth1"],   // the WAN NIC
    flows: ["egress"],
    messages: ["put"],
    rules: [
      { key_expr: "robot/sensor/lidar/**", freq: 2.0 },
    ],
  },
],
```

---

## Low-Pass Filter (Size Limiting)

The low-pass filter drops messages whose payload exceeds a configured byte limit. It
is a complement to downsampling: downsampling limits *frequency*, low-pass filtering
limits *size*.

### Configuration Location

```
low_pass_filter: [ ... ]   (top-level in zenoh config)
```

### Full Syntax

```json5
low_pass_filter: [
  {
    id: "filter1",                     // optional, must be unique
    interfaces: ["wlan0"],             // optional: only on these interfaces
    link_protocols: [                  // optional: only on these protocols
      "tcp", "udp", "tls", "quic",
      "ws", "serial", "unixsock-stream", "unixpipe", "vsock"
    ],
    flows: ["ingress", "egress"],      // optional: direction filter
    messages: ["put", "delete", "query", "reply"],  // required
    key_exprs: ["sensor/**"],          // messages on these key expressions are filtered
    size_limit: 8192,                  // max payload size in bytes (inclusive)
  },
],
```

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | No | Unique identifier |
| `interfaces` | `[string]` | No | Limit to these network interfaces |
| `link_protocols` | `[string]` | No | Limit to these transport protocols |
| `flows` | `[string]` | No | `"egress"`, `"ingress"`, or both |
| `messages` | `[string]` | **Yes** | Message types to filter |
| `key_exprs` | `[string]` | Yes | Key expressions whose messages are filtered |
| `size_limit` | `u64` bytes | Yes | Inclusive maximum size of serialized payload + attachment |

### Behavior When Message Exceeds Limit

Messages whose `serialized payload + serialized attachment` size exceeds `size_limit`
are **dropped silently**. No error is returned to the publisher and no notification is
sent to the subscriber. This is a best-effort protective mechanism, not a reliable
flow-control signal.

### Use Case: Preventing Large Messages on Low-Bandwidth Links

A node on a serial or narrow wireless link cannot handle point clouds exceeding 64 KB.
Cap incoming messages to protect the link buffer:

```json5
low_pass_filter: [
  {
    id: "serial_size_cap",
    interfaces: ["ttyS0"],
    flows: ["ingress"],
    messages: ["put"],
    key_exprs: ["sensor/**"],
    size_limit: 65536,
  },
],
```

---

## Channel: Priority × Reliability

At the wire level, Zenoh combines `priority` and `reliability` into a **channel**,
defined as:

```rust
pub struct Channel {
    pub priority: Priority,
    pub reliability: Reliability,
}
```

### How Channels Map to Queues

Each link maintains separate transmission queues per `(priority, reliability)` pair.
With 7 user-visible priority levels and 2 reliability modes, there are up to
**14 distinct channels** per link (plus the internal `Control` priority queue).

| Priority | BestEffort Queue | Reliable Queue |
|----------|-----------------|----------------|
| RealTime | ✓ | ✓ |
| InteractiveHigh | ✓ | ✓ |
| InteractiveLow | ✓ | ✓ |
| DataHigh | ✓ | ✓ |
| Data | ✓ | ✓ |
| DataLow | ✓ | ✓ |
| Background | ✓ | ✓ |

### Why This Matters: Head-of-Line Blocking

Without channel separation, a large Reliable message blocking in a full queue could
hold back small BestEffort messages at the same priority. With separate queues per
channel, BestEffort messages can drain independently of Reliable ones.

This also means that a Reliable publisher using `CongestionControl::Block` will only
block that channel's queue. A co-located BestEffort publisher at the same priority
continues to make progress.

### Practical Implication

When combining priority and reliability:
- Use `RealTime + Reliable + Block` for safety commands: highest priority, guaranteed
  delivery, backpressure to the application if the link is saturated.
- Use `Data + BestEffort + Drop` for sensor streams: normal priority, low overhead,
  tolerates loss under congestion.
- Use `Background + BestEffort + Drop` for logging: cannot compete with real-time
  traffic; dropped freely under load.

---

## Queue Configuration

Queue depths and congestion timing are set in the transport section of the config:

```json5
transport: {
  unicast: {
    qos: { enabled: true },    // must be true to use per-priority queues
    // ...
  },
  link: {
    tx: {
      batch_size: 65535,       // max bytes per batch (1–65535)
      queue: {
        // Depth of each priority queue in batches (1–16 per queue)
        // Memory per queue = size * batch_size
        size: {
          control: 2,
          real_time: 2,
          interactive_high: 2,
          interactive_low: 2,
          data_high: 2,
          data: 2,
          data_low: 2,
          background: 2,
        },
        congestion_control: {
          drop: {
            // Time to wait before dropping (µs)
            wait_before_drop: 1000,
            // Wait limit for fragmented message parts (µs)
            max_wait_before_drop_fragments: 50000,
          },
          block: {
            // Time before closing session when blocked (µs)
            wait_before_close: 5000000,
          },
        },
        batching: {
          enabled: true,
          time_limit: 1,       // max ms a message waits for batching
        },
      },
    },
  },
},
```

> **Note:** If `transport.unicast.qos.enabled` is `false`, only the `Data` priority
> queue is allocated and all messages use it regardless of their `priority` setting.
> QoS is enabled by default for unicast and disabled by default for multicast (for
> Zenoh-Pico compatibility).

> **Note:** `LowLatency` transport mode (`transport.unicast.lowlatency: true`) is
> **incompatible with QoS**. To enable LowLatency you must set `qos.enabled: false`.
> LowLatency does not support fragmentation either.

---

## Complete Example: Mixed-QoS Robotics Application

This example demonstrates a mobile robot node with multiple publishers at different
priority levels, plus config-level safety overrides:

**Config (`robot_qos.json5`):**
```json5
{
  mode: "peer",
  transport: {
    unicast: {
      qos: { enabled: true },
      link: {
        tx: {
          queue: {
            size: {
              control: 2,
              real_time: 4,        // deeper queue for safety commands
              interactive_high: 2,
              interactive_low: 2,
              data_high: 4,        // deeper queue for IMU
              data: 2,
              data_low: 2,
              background: 2,
            },
            congestion_control: {
              drop: { wait_before_drop: 500 },
              block: { wait_before_close: 10000000 },
            },
          },
        },
      },
    },
  },
  qos: {
    publication: [
      {
        key_exprs: ["robot/safety/**"],
        config: {
          priority: "real_time",
          congestion_control: "block",
          express: true,
        },
      },
      {
        key_exprs: ["robot/log/**"],
        config: {
          priority: "background",
          congestion_control: "drop",
        },
      },
    ],
  },
  downsampling: [
    {
      id: "wan_sensor_limit",
      interfaces: ["eth1"],
      flows: ["egress"],
      messages: ["put"],
      rules: [
        { key_expr: "robot/sensor/lidar/**", freq: 2.0 },
        { key_expr: "robot/sensor/camera/**", freq: 1.0 },
      ],
    },
  ],
}
```

**Application (Rust):**
```rust
use zenoh::qos::{CongestionControl, Priority};

let config = zenoh::Config::from_file("robot_qos.json5").unwrap();
let session = zenoh::open(config).await.unwrap();

// Safety: RealTime + Block (config overrides guarantee this even if you forget)
let estop_pub = session
    .declare_publisher("robot/safety/estop")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Block)
    .express(true)
    .await
    .unwrap();

// Control: InteractiveHigh + Block (joystick input)
let joystick_pub = session
    .declare_publisher("robot/control/joystick")
    .priority(Priority::InteractiveHigh)
    .congestion_control(CongestionControl::Block)
    .await
    .unwrap();

// IMU: DataHigh + Drop (high-frequency, tolerate loss)
let imu_pub = session
    .declare_publisher("robot/sensor/imu")
    .priority(Priority::DataHigh)
    .congestion_control(CongestionControl::Drop)
    .await
    .unwrap();

// Camera: Data + Drop + express=false (batching is fine for video)
let camera_pub = session
    .declare_publisher("robot/sensor/camera/rgb")
    .priority(Priority::Data)
    .congestion_control(CongestionControl::Drop)
    .await
    .unwrap();

// Logs: Background + Drop (never compete with real-time traffic)
let log_pub = session
    .declare_publisher("robot/log/events")
    .priority(Priority::Background)
    .congestion_control(CongestionControl::Drop)
    .await
    .unwrap();
```

**Application (Python):**
```python
import zenoh

config = zenoh.Config.from_file("robot_qos.json5")
session = zenoh.open(config)

# Safety: RealTime + Block
estop_pub = session.declare_publisher(
    "robot/safety/estop",
    priority=zenoh.Priority.REAL_TIME,
    congestion_control=zenoh.CongestionControl.BLOCK,
    express=True,
)

# Control: InteractiveHigh + Block
joystick_pub = session.declare_publisher(
    "robot/control/joystick",
    priority=zenoh.Priority.INTERACTIVE_HIGH,
    congestion_control=zenoh.CongestionControl.BLOCK,
)

# IMU: DataHigh + Drop
imu_pub = session.declare_publisher(
    "robot/sensor/imu",
    priority=zenoh.Priority.DATA_HIGH,
    congestion_control=zenoh.CongestionControl.DROP,
)

# Camera: Data + Drop
camera_pub = session.declare_publisher(
    "robot/sensor/camera/rgb",
    priority=zenoh.Priority.DATA,
    congestion_control=zenoh.CongestionControl.DROP,
)

# Logs: Background + Drop
log_pub = session.declare_publisher(
    "robot/log/events",
    priority=zenoh.Priority.BACKGROUND,
    congestion_control=zenoh.CongestionControl.DROP,
)
```

## See Also

- [Performance Tuning Guide](performance-tuning-guide.md) — how to combine QoS settings with transport tuning for maximum performance
- [Config Transport Link TX](config-transport-link-tx.md) — the queue size and congestion control timeout configuration that QoS settings interact with
- [Config Misc](config-misc.md) — the `qos.publication` and `qos.network` config overrides that apply QoS policies without code changes
