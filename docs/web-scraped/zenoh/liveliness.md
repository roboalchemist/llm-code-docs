# Zenoh Liveliness

## Table of Contents

1. [What Is Liveliness?](#what-is-liveliness)
2. [Use Cases](#use-cases)
3. [How It Works](#how-it-works)
4. [Key Expressions for Liveliness](#key-expressions-for-liveliness)
5. [API Reference](#api-reference)
   - [Accessing the Liveliness API](#accessing-the-liveliness-api)
   - [Declaring a Liveliness Token](#declaring-a-liveliness-token)
   - [Subscribing to Liveliness Changes](#subscribing-to-liveliness-changes)
   - [Querying Currently Alive Tokens](#querying-currently-alive-tokens)
6. [Liveliness vs. Regular Pub/Sub](#liveliness-vs-regular-pubsub)
7. [Worked Example: Service Registry](#worked-example-service-registry)
8. [Comparison with ROS 2 Graph Events](#comparison-with-ros-2-graph-events)
9. [Known Limitations and Edge Cases](#known-limitations-and-edge-cases)

---

## What Is Liveliness?

Liveliness is a **token-based presence detection** mechanism built into Zenoh's routing layer. It is not a messaging pattern — it does not send data payloads between applications. Instead, it answers one question:

> *Is this logical entity currently alive and reachable on the network?*

A **liveliness token** is a handle declared by a Zenoh session on a key expression. While that token exists and its declaring session is reachable, any other session in the system can observe the token as *alive*. When the token is dropped, undeclared, or its declaring session disconnects or crashes, the token is automatically seen as *gone*.

This is distinct from heartbeat-based presence systems (like Zenoh's group management in `zenoh-ext`). Those require each participant to periodically broadcast a message to prove it is alive. Liveliness tokens instead rely on the liveness of the underlying Zenoh transport session itself — no polling, no heartbeats, no periodic traffic.

```
Node A declares token "services/camera/front"
        │
        ├── Node B subscribes → receives Put("services/camera/front")
        │
        │   ... time passes ...
        │
        └── Node A crashes or loses connectivity
                │
                └── Node B receives Delete("services/camera/front")
```

---

## Use Cases

### Service Discovery

Nodes can advertise their availability by declaring a liveliness token on a structured key expression such as `services/<type>/<instance-id>`. Other nodes query the liveliness space at startup to find currently running services, and subscribe to receive notifications as services come and go.

### Health Monitoring

An operator dashboard can subscribe to `nodes/**` and receive real-time `Put`/`Delete` events as compute nodes join and leave the system. No polling or dedicated health-check protocols are needed.

### Detecting Node Failures

Because liveliness cleanup is performed by the routing infrastructure — not the application — a crashed node (one that did not call `close()` or `undeclare()`) is handled identically to a graceful shutdown. Subscribers see a `Delete` event either way, as soon as connectivity to the dead node is lost.

### Presence Notifications

In multi-robot or distributed sensor systems, each agent declares a token under its own identity key. Other agents subscribe to the entire fleet namespace and maintain a live roster without any application-level coordination protocol.

---

## How It Works

### Liveliness Tokens

A liveliness token is declared by calling `session.liveliness().declare_token(key_expr)`. Internally, this registers the token with the Zenoh routing layer, which propagates knowledge of the token's existence to interested subscribers across the network.

A token is considered *alive* for as long as **all three** of these conditions hold:

1. The token has not been explicitly undeclared or dropped.
2. The Zenoh session that declared the token has not stopped or crashed.
3. There is Zenoh connectivity between the declaring session and the observing session.

If any condition becomes false, the token is seen as *dropped* by all remote observers.

### Automatic Cleanup on Session Close

The automatic cleanup is the key property that distinguishes liveliness from regular pub/sub. When a session closes — whether gracefully or due to a crash — the Zenoh routers that were relaying that session's liveliness tokens automatically propagate `Delete` events to all matching subscribers. The application does not need to send any final message; the infrastructure handles it.

This cleanup is tied to the **transport session liveliness**: routers detect when a transport connection drops and immediately notify downstream subscribers.

### Multiple Tokens on the Same Key

If multiple sessions declare tokens on the same key expression, that key is considered *alive* until the **last** token is dropped. The first declaration triggers a `Put` event; subsequent declarations on the same key from different sessions do not trigger additional events. Only when the final token disappears does a `Delete` event propagate.

### Network Partitions

In a network partition scenario, behavior is partition-local:

- Sessions that retain connectivity to the declaring node continue to see the token as *alive*.
- Sessions that lose connectivity to the declaring node see the token as *dropped* and receive a `Delete` event.

This is the correct behavior: from the perspective of a partitioned observer, the entity is genuinely unreachable and should be treated as gone.

### Connectivity Loss for Subscribers

When a subscriber session itself loses all connectivity (e.g., a client that cannot reach its router), it cannot know the current state of any token. To signal this condition, the infrastructure delivers a synthetic `Delete` on key `**` to matching liveliness subscribers. Applications should interpret this as "all previously known tokens are now unknown" and treat the liveliness state as invalidated until connectivity is restored.

---

## Key Expressions for Liveliness

Liveliness tokens use the same key expression syntax as regular Zenoh resources. There are no special reserved prefixes enforced by the API — the `@/liveliness/` namespace is used internally by the routing layer, but applications declare tokens using their own logical key expressions.

**Recommended conventions:**

```
# Group membership
<group-name>/<member-id>
robots/rover_01
robots/rover_02

# Typed service registry
services/<service-type>/<instance-id>
services/camera/front_left
services/lidar/top

# Hierarchical node registry
nodes/<datacenter>/<rack>/<node-id>
nodes/us-east/rack-3/worker-07

# Application-specific namespaces
myapp/workers/**
myapp/workers/alpha
```

**Wildcard queries** use standard Zenoh wildcards:

- `*` matches a single path segment: `robots/*` matches `robots/rover_01` but not `robots/fleet/rover_01`.
- `**` matches any number of segments: `services/**` matches all services at any depth.

Choose key expressions that reflect the logical structure of your system. Hierarchical naming makes it easy to subscribe to subsets of the presence space — for example, subscribing to `services/camera/**` to watch only camera services.

---

## API Reference

### Accessing the Liveliness API

All liveliness operations are accessed through the `Liveliness` struct, obtained from an open session:

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let liveliness = session.liveliness();
    // liveliness.declare_token(...)
    // liveliness.declare_subscriber(...)
    // liveliness.get(...)
}
```

The `Liveliness` struct is a lightweight wrapper; it holds a reference to the session and incurs no additional overhead.

---

### Declaring a Liveliness Token

```rust
pub fn declare_token<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessTokenBuilder<'a, 'b>
```

**Returns:** A `LivelinessTokenBuilder` that resolves (via `.await`) to a `LivelinessToken`.

**Behavior:**

- Declaring the token causes all matching liveliness subscribers in the system to receive a `SampleKind::Put` event.
- The token remains alive until it is dropped or explicitly undeclared.
- `LivelinessToken` is annotated with `#[must_use]` — if the returned value is not bound to a variable, it is immediately dropped and the token never actually becomes active.

#### Declaring a token

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // Declare a liveliness token. The token is alive for as long as
    // `token` is in scope and this session is connected.
    let token = session
        .liveliness()
        .declare_token("robots/rover_01")
        .await
        .unwrap();

    println!("Token is alive. Press CTRL-C to exit.");
    tokio::signal::ctrl_c().await.unwrap();

    // Token is automatically undeclared when dropped.
    // Equivalent to: token.undeclare().await.unwrap();
    drop(token);
}
```

#### Explicitly undeclaring a token

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let token = session
        .liveliness()
        .declare_token("robots/rover_01")
        .await
        .unwrap();

    // ... do work ...

    // Explicit undeclaration. Subscribers will receive a Delete event.
    token.undeclare().await.unwrap();

    // The session remains open; only the token is gone.
}
```

#### The `#[must_use]` rule

This is a common mistake:

```rust
// WRONG: token is immediately dropped; it is never actually alive
session.liveliness().declare_token("robots/rover_01").await.unwrap();

// CORRECT: bind to a variable
let _token = session.liveliness().declare_token("robots/rover_01").await.unwrap();
```

---

### Subscribing to Liveliness Changes

```rust
pub fn declare_subscriber<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessSubscriberBuilder<'a, 'b, DefaultHandler>
```

**Returns:** A `LivelinessSubscriberBuilder` that resolves to a `Subscriber`.

**Behavior:**

- The subscriber receives `SampleKind::Put` when a matching token becomes alive.
- The subscriber receives `SampleKind::Delete` when a matching token is dropped or lost.
- The subscriber only receives events that occur **after** it is declared. Tokens that were already alive before the subscriber was created are **not** delivered as `Put` events. Use `liveliness().get()` or a `QueryingSubscriber` (from `zenoh-ext`) to retrieve pre-existing tokens.

#### Basic subscriber

```rust
use zenoh::{sample::SampleKind, Config};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let subscriber = session
        .liveliness()
        .declare_subscriber("robots/**")
        .await
        .unwrap();

    println!("Watching for robot presence changes...");
    while let Ok(sample) = subscriber.recv_async().await {
        match sample.kind() {
            SampleKind::Put => {
                println!("[+] Robot appeared: {}", sample.key_expr());
            }
            SampleKind::Delete => {
                println!("[-] Robot lost:     {}", sample.key_expr());
            }
        }
    }
}
```

#### Callback-based subscriber

```rust
use zenoh::{sample::SampleKind, Config};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let _subscriber = session
        .liveliness()
        .declare_subscriber("services/**")
        .callback(|sample| {
            match sample.kind() {
                SampleKind::Put => {
                    println!("Service online:  {}", sample.key_expr());
                }
                SampleKind::Delete => {
                    println!("Service offline: {}", sample.key_expr());
                }
            }
        })
        .background()
        .await
        .unwrap();

    // Keep the session alive
    tokio::signal::ctrl_c().await.unwrap();
}
```

#### Getting history (pre-existing tokens) with the subscriber

By default `declare_subscriber` only receives future events. To also receive currently alive tokens at subscription time, use the `.history(true)` option on the builder:

```rust
use zenoh::{sample::SampleKind, Config};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // history(true) causes already-alive tokens to be delivered as Put events
    // before any future events arrive.
    let subscriber = session
        .liveliness()
        .declare_subscriber("robots/**")
        .history(true)
        .await
        .unwrap();

    while let Ok(sample) = subscriber.recv_async().await {
        match sample.kind() {
            SampleKind::Put => println!("Alive: {}", sample.key_expr()),
            SampleKind::Delete => println!("Gone:  {}", sample.key_expr()),
        }
    }
}
```

---

### Querying Currently Alive Tokens

```rust
pub fn get<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessGetBuilder<'a, 'b, DefaultHandler>
```

**Returns:** A `LivelinessGetBuilder` that resolves to a `Handler` (default: a FIFO channel of `Reply` values).

**Behavior:**

- Returns a snapshot of all tokens currently alive that match the key expression.
- Each matching token produces one `Reply` containing a `Sample` with `SampleKind::Put`.
- The query blocks until all matching routers have replied or the timeout elapses.
- Default timeout is taken from the session's `queries_default_timeout` configuration.

#### Querying alive tokens

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let replies = session
        .liveliness()
        .get("services/**")
        .await
        .unwrap();

    println!("Currently alive services:");
    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                println!("  {}", sample.key_expr());
            }
            Err(err) => {
                eprintln!("  Error: {:?}", err);
            }
        }
    }
}
```

#### Query with explicit timeout

```rust
use std::time::Duration;
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let replies = session
        .liveliness()
        .get("robots/**")
        .timeout(Duration::from_secs(5))
        .await
        .unwrap();

    let mut alive_robots: Vec<String> = Vec::new();
    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            alive_robots.push(sample.key_expr().to_string());
        }
    }

    println!("Found {} alive robots: {:?}", alive_robots.len(), alive_robots);
}
```

---

## Liveliness vs. Regular Pub/Sub

Liveliness and pub/sub are both built on key expressions and both deliver `Put`/`Delete` samples to subscribers. The critical differences are in **who manages the lifecycle** and **what the data represents**.

| Property | Regular Pub/Sub | Liveliness |
|---|---|---|
| **Lifecycle management** | Application must explicitly publish and delete | Automatically managed by the routing infrastructure |
| **Crash handling** | Publisher crash leaves last value; no delete sent | Token automatically deleted when session dies |
| **Data payload** | Arbitrary bytes | No payload; presence is the information |
| **Backfill** | Depends on storage/queryable setup | `liveliness().get()` returns current snapshot |
| **Network partition** | Data stops flowing | Partitioned observers receive Delete events |
| **Purpose** | Transmitting data between nodes | Detecting whether a node is present and reachable |

In pub/sub, if a publisher crashes after publishing `"status": "healthy"`, subscribers retain that last value indefinitely — there is no automatic correction. With liveliness, the token disappears the moment the routing layer detects the session is gone, and all matching subscribers receive a `Delete` event immediately.

Regular pub/sub requires the application to publish a tombstone (a `delete()` call or a final "I am shutting down" message) to inform other nodes. Liveliness tokens require no such coordination; the infrastructure handles it transparently.

---

## Worked Example: Service Registry

This example demonstrates a complete service registry using liveliness: a service advertises itself, and a registry node maintains a live roster.

### Service node (advertiser)

Each service instance declares a token encoding its type and unique ID.

```rust
// service_node.rs
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let service_type = "image_processor";
    let instance_id = std::process::id(); // Use PID as a simple unique ID
    let key = format!("services/{}/{}", service_type, instance_id);

    println!("Advertising service at '{}'", key);

    // Declare the token. This triggers Put events in all matching subscribers.
    let _token = session
        .liveliness()
        .declare_token(&key)
        .await
        .unwrap();

    println!("Service running. Press CTRL-C to stop.");
    tokio::signal::ctrl_c().await.unwrap();

    // _token is dropped here; all subscribers receive a Delete event.
    println!("Service shutting down.");
}
```

### Registry node (watcher)

The registry queries current state at startup and then subscribes to all future changes.

```rust
// registry.rs
use std::collections::HashSet;
use std::sync::{Arc, Mutex};
use zenoh::{sample::SampleKind, Config};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let registry: Arc<Mutex<HashSet<String>>> = Arc::new(Mutex::new(HashSet::new()));

    // --- Step 1: Query currently alive services ---
    let replies = session
        .liveliness()
        .get("services/**")
        .await
        .unwrap();

    {
        let mut reg = registry.lock().unwrap();
        while let Ok(reply) = replies.recv_async().await {
            if let Ok(sample) = reply.result() {
                let key = sample.key_expr().to_string();
                println!("[startup] Found alive service: {}", key);
                reg.insert(key);
            }
        }
        println!("[startup] Registry initialized with {} services.", reg.len());
    }

    // --- Step 2: Subscribe to future changes ---
    let registry_clone = Arc::clone(&registry);
    let subscriber = session
        .liveliness()
        .declare_subscriber("services/**")
        .await
        .unwrap();

    println!("Watching for service changes...");

    while let Ok(sample) = subscriber.recv_async().await {
        let key = sample.key_expr().to_string();
        let mut reg = registry_clone.lock().unwrap();

        match sample.kind() {
            SampleKind::Put => {
                println!("[+] Service online:  {}", key);
                reg.insert(key);
            }
            SampleKind::Delete => {
                println!("[-] Service offline: {}", key);
                reg.remove(&key);
            }
        }

        println!("    Active services ({}):", reg.len());
        for svc in reg.iter() {
            println!("      {}", svc);
        }
    }
}
```

### Running the example

```bash
# Terminal 1: start the registry
cargo run --bin registry

# Terminal 2: start a service (token declared)
cargo run --bin service_node
# Output: "Advertising service at 'services/image_processor/12345'"

# Terminal 1 output:
# [+] Service online: services/image_processor/12345
#     Active services (1):
#       services/image_processor/12345

# Terminal 2: press CTRL-C or kill the process
# Terminal 1 output:
# [-] Service offline: services/image_processor/12345
#     Active services (0):
```

The registry receives the `Delete` event whether the service shuts down cleanly or crashes.

### Handling the startup race condition

There is a potential race between the `get()` call completing and new `Put` events arriving before the subscriber is declared. To avoid missing events, declare the subscriber **before** calling `get()`, or use the `history(true)` option on the subscriber, which internally performs this coordination:

```rust
// Preferred: declare subscriber first, use history to get current state
let subscriber = session
    .liveliness()
    .declare_subscriber("services/**")
    .history(true)   // delivers pre-existing tokens as Put events
    .await
    .unwrap();

// Now drain: both historical and live events arrive through the same channel
while let Ok(sample) = subscriber.recv_async().await {
    // handle Put/Delete
}
```

---

## Comparison with ROS 2 Graph Events

ROS 2 provides graph event notifications through `rclcpp::Node::get_node_graph_interface()` and the `rcl_wait_set` mechanism. Zenoh Liveliness and ROS 2 graph events solve similar problems but with different scopes, models, and guarantees.

### Scope

**ROS 2 graph events** are scoped to a single DDS domain and reflect the ROS graph structure: nodes, topics, services, and actions. The information is inherently structured around ROS concepts.

**Zenoh Liveliness** is generic. It knows nothing about "nodes" or "services" in a ROS sense — it tracks the presence of arbitrary key expressions. Applications impose their own structure through key expression conventions. This makes it applicable outside ROS contexts and easier to extend with custom entity types.

### What triggers an event

In ROS 2, graph events fire when the DDS discovery layer detects a new participant, publisher, subscriber, service server, or service client. The application has limited control over what is tracked.

In Zenoh, only entities that explicitly call `declare_token()` are tracked. An application that does not declare a token is invisible to liveliness monitoring. This is intentional: it prevents unbounded scalability costs from monitoring every entity in a large system.

### Crash detection

ROS 2 graph events rely on DDS participant liveness QoS or lease duration mechanisms. Detection latency is configurable but often on the order of seconds and depends on correct QoS configuration.

Zenoh liveliness is tied to the Zenoh transport session. When a transport connection drops, the routing layer immediately detects it and propagates `Delete` events. Detection latency is bounded by the transport keepalive configuration, not an application-level QoS setting.

### Network transparency

ROS 2 graph events are traditionally local to a single machine or DDS domain. Cross-host graph awareness requires bridging (e.g., using `zenoh-bridge-ros2dds`).

Zenoh liveliness works natively across the entire Zenoh network, including across routers, WAN links, and heterogeneous transports. A subscriber in one datacenter can monitor liveliness tokens declared in another datacenter without any additional configuration.

### Query capability

ROS 2 provides synchronous graph introspection calls (`get_node_names()`, `get_topic_names_and_types()`, etc.) that return a snapshot of the current graph state.

Zenoh provides the equivalent through `liveliness().get()`, which queries the distributed liveliness state and returns currently alive tokens. The semantics are similar, but the Zenoh version is asynchronous and network-wide.

### Summary table

| Dimension | ROS 2 Graph Events | Zenoh Liveliness |
|---|---|---|
| **Scope** | ROS graph entities (nodes, topics, services) | Any user-defined key expression |
| **Opt-in tracking** | No — all entities tracked automatically | Yes — only declared tokens are tracked |
| **Crash detection latency** | Seconds (DDS QoS-dependent) | Transport keepalive (configurable, typically fast) |
| **Network reach** | DDS domain (single host by default) | Entire Zenoh network, WAN-capable |
| **Snapshot query** | Synchronous graph API | Async `liveliness().get()` |
| **Scalability** | Scales with DDS discovery overhead | Scales well; only declared tokens propagate |
| **Payload** | None (event only) | None (presence only) |

---

## Known Limitations and Edge Cases

### No associated payload (current release)

Liveliness tokens carry no user-defined payload. The token's key expression is the only information conveyed. If you need to associate metadata with a presence event (e.g., version, endpoint address, capabilities), encode that information in the key expression itself or publish it separately on a regular key expression after declaring the token.

The RFC notes that associated values are a planned future addition.

### Subscriber does not see historical tokens by default

A freshly declared subscriber only receives events that occur after its declaration. If tokens were already alive before the subscriber was created, those tokens are invisible to it unless `history(true)` is used or `liveliness().get()` is called separately.

### `#[must_use]` on `LivelinessToken`

Always bind the returned `LivelinessToken` to a named variable. A token bound to `_` (single underscore, not `_name`) is dropped immediately at the end of the statement:

```rust
// WRONG: dropped immediately, token never becomes active
let _ = session.liveliness().declare_token("my/service").await.unwrap();

// CORRECT: lives for the duration of the enclosing scope
let _token = session.liveliness().declare_token("my/service").await.unwrap();
```

### Connectivity loss to the subscriber itself

If the monitoring application loses all connectivity, the infrastructure delivers a synthetic `Delete` on `**`. Applications should treat this as a signal to invalidate their entire cached liveliness state and rebuild it via `liveliness().get()` once connectivity is restored.

### Feature stability

The liveliness API is marked **unstable** in the Zenoh roadmap. The routing-layer key space, API signatures, and value formats may change in future releases. Pin your dependency version if API stability is required.