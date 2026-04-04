# Zenoh Liveliness

## Table of Contents

1. [What Is Liveliness?](#what-is-liveliness)
2. [Use Cases](#use-cases)
3. [How It Works](#how-it-works)
4. [Key Expressions for Liveliness](#key-expressions-for-liveliness)
5. [API Reference](#api-reference)
6. [Difference from Regular Pub/Sub](#difference-from-regular-pubsub)
7. [Worked Example: Service Registry Pattern](#worked-example-service-registry-pattern)
8. [Difference from ROS 2 Graph Events](#difference-from-ros-2-graph-events)

---

## What Is Liveliness?

Liveliness is a **token-based presence detection** mechanism built into Zenoh. It lets any application in the system declare that it is "alive" by publishing a named token, and lets other applications observe when those tokens appear or disappear — without requiring any application-level heartbeat logic.

A **liveliness token** is a named object tied to a Zenoh session. It is:

- Declared on a **key expression** that names the entity.
- **Alive** for exactly as long as the declaring session is alive and has network connectivity to the observer.
- **Automatically removed** — without any application code — when the session closes, crashes, or loses connectivity.

This is fundamentally different from regular pub/sub, where the application must explicitly publish a "goodbye" message before shutting down. With liveliness, the infrastructure itself detects and propagates the disappearance.

```rust
// Declare a token. While `token` is in scope and the session is alive,
// remote observers see this entity as present.
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let token = session
    .liveliness()
    .declare_token("robots/robot-42/navigation")
    .await
    .unwrap();

// When `token` is dropped — or the process crashes — the infrastructure
// automatically notifies all observers that "robots/robot-42/navigation"
// is gone. No explicit cleanup code required.
```

### Multiple Tokens on the Same Key

If multiple sessions declare tokens on the same key expression, the key is considered alive as long as **at least one** of those tokens exists. It only becomes "dead" when the **last** token on that key is dropped or the last declaring session disconnects.

---

## Use Cases

### Service Discovery

Microservices or robot nodes declare a liveliness token when they start. Other nodes subscribe to the token namespace to learn which services are currently available, without polling or maintaining a central registry.

```
services/image-processor/node-a
services/path-planner/node-b
services/localization/node-c
```

When `node-b`'s process is killed, a `Delete` event is automatically delivered to all subscribers of `services/**`.

### Health Monitoring

A watchdog process subscribes to `fleet/**`. Each vehicle declares a token under `fleet/<vehicle-id>`. The watchdog receives a `Delete` sample the moment any vehicle loses connectivity, without the vehicle needing to send a shutdown message.

### Detecting Node Failures

Unlike application-level health checks (which require the application to be responsive enough to send a heartbeat), liveliness detection works at the **transport session** level. If a node is alive but stuck in an infinite loop and cannot send heartbeats, it may falsely appear healthy to application-level monitors. Liveliness tokens are managed by Zenoh's routing layer, so they disappear as soon as the underlying transport session is lost — even if the application code is frozen.

### Presence Notifications

Chat systems, collaborative editors, and multi-robot coordination all benefit from knowing which participants are currently online. Liveliness tokens provide this with zero application-level bookkeeping.

### Dynamic Subscription Routing

A data broker can subscribe to `sources/**` liveliness events and use them to dynamically set up or tear down forwarding pipelines whenever a new data source appears or disappears.

---

## How It Works

### Liveliness Tokens

A liveliness token is declared on a **key expression**. The key expression is the public name of the entity — it is what other nodes use to identify it.

Internally, Zenoh's routing layer tracks which sessions have declared which tokens. This state is propagated through the router network so that any application anywhere in the system can observe it.

### Lifecycle and Automatic Cleanup

A token's liveliness ends under any of the following conditions:

| Condition | Effect |
|---|---|
| `token.undeclare().await` called | Token is explicitly removed; observers receive `Delete` |
| `token` is dropped | Token is automatically undeclared; observers receive `Delete` |
| The declaring session is closed | All tokens from that session are removed |
| The declaring process crashes | Transport session is lost; routers propagate `Delete` |
| Network partition separates declarer from observer | Observers on the isolated side receive `Delete` for all tokens they can no longer reach |

```rust
// Explicit undeclaration
token.undeclare().await.unwrap();

// Or just let it drop — same effect
drop(token);
```

The `#[must_use]` attribute on `LivelinessToken` ensures you bind it to a variable. Failing to do so causes an immediate drop and immediate undeclaration:

```rust
// WARNING: this token is immediately dropped and undeclared!
session.liveliness().declare_token("my/service").await.unwrap();

// CORRECT: bind to a variable to keep it alive
let _token = session.liveliness().declare_token("my/service").await.unwrap();
```

### Network Partitions

If a client application subscribing to liveliness events loses all connectivity (e.g., its router goes down), the Zenoh infrastructure signals the loss of **all** previously known tokens by delivering a synthetic `Delete` with key `**`. This tells the application that its entire view of the system is now stale, without requiring the infrastructure to enumerate every individual token the client was tracking.

### Routing Layer Integration

Liveliness is implemented at the **routing layer**, not the application layer. This means:

- No periodic heartbeat messages are required.
- The overhead scales with the number of **declared tokens**, not the number of nodes observing them.
- Detection latency is bounded by the underlying transport session detection timeout, not by a heartbeat interval.

---

## Key Expressions for Liveliness

Liveliness tokens use **standard Zenoh key expressions**. There is no special namespace prefix required in your application code — you choose the key expression schema that makes sense for your system.

### Recommended Conventions

**Group/Member pattern** (most common):

```
<group>/<member-id>
```

Example: `robots/arm-controller-1`, `fleet/truck-007`, `services/localization`

**Hierarchical role pattern** (for systems with multiple entity types):

```
<system>/<subsystem>/<role>/<instance-id>
```

Example: `factory/line-a/sensor/temp-42`, `factory/line-a/actuator/motor-7`

**Session-scoped pattern** (when you need to associate tokens with session identities):

```
<group>/<zenoh-session-id>
```

This is useful when one session may declare multiple tokens and you want to correlate all tokens from the same session.

### Wildcard Queries and Subscriptions

Key expression wildcards work exactly as they do in regular Zenoh:

| Key Expression | Matches |
|---|---|
| `robots/*` | All direct children: `robots/arm-1`, `robots/base-2`, etc. |
| `robots/**` | All descendants at any depth |
| `**/localization` | Any entity named `localization` anywhere in the hierarchy |
| `fleet/truck-*/navigation` | Navigation component of any truck |

```rust
// Subscribe to all members of group1
let sub = session.liveliness().declare_subscriber("group1/**").await.unwrap();

// Query all alive robots
let replies = session.liveliness().get("robots/**").await.unwrap();
```

### Avoiding Conflicts with Regular Key Expressions

Liveliness tokens occupy a **separate internal namespace** managed by Zenoh. You do not need to prefix your liveliness keys to avoid collisions with regular publisher/subscriber key expressions. A token declared on `robots/arm-1` does not conflict with a publisher writing data to `robots/arm-1`.

---

## API Reference

All liveliness functions are accessed through `session.liveliness()`, which returns a `Liveliness` struct bound to the session's lifetime.

```rust
let liveliness = session.liveliness();
```

---

### `declare_token` — Announce Presence

```rust
pub fn declare_token<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessTokenBuilder<'a, 'b>
```

Declares a liveliness token on the given key expression. Returns a builder that resolves to a `LivelinessToken` upon `.await`.

**The returned `LivelinessToken` must be bound to a variable.** It is annotated `#[must_use]`; dropping it immediately undeclares the token.

#### Example

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // Declare the token. This node is now "alive" as "group1/member1".
    let token = session
        .liveliness()
        .declare_token("group1/member1")
        .await
        .unwrap();

    println!("Token declared. Press Ctrl-C to exit.");
    tokio::signal::ctrl_c().await.unwrap();

    // Explicit undeclaration — optional, dropping `token` has the same effect.
    token.undeclare().await.unwrap();
}
```

#### `LivelinessToken` Methods

| Method | Description |
|---|---|
| `token.undeclare()` | Explicitly undeclares the token. Returns a `Resolve<ZResult<()>>`. |

Dropping a `LivelinessToken` without calling `undeclare()` is safe and correct — Zenoh will automatically undeclare it.

---

### `declare_subscriber` — Watch for Presence Changes

```rust
pub fn declare_subscriber<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessSubscriberBuilder<'a, 'b, DefaultHandler>
```

Declares a subscriber that receives notifications whenever a liveliness token matching the given key expression appears or disappears.

**Received samples:**

| `sample.kind()` | Meaning |
|---|---|
| `SampleKind::Put` | A new token has appeared (entity joined) |
| `SampleKind::Delete` | A token has disappeared (entity left, crashed, or lost connectivity) |

The `sample.key_expr()` identifies which token changed.

> **Note:** A liveliness subscriber only receives events that occur **after** it is declared. Tokens that were already alive before the subscriber was declared are **not** delivered as `Put` events. To get both pre-existing tokens and future changes, use a `QueryingSubscriber` from `zenoh-ext` (see [Getting Current State + Future Changes](#getting-current-state--future-changes)), or issue a `get()` call followed by `declare_subscriber()`.

#### Example

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

    println!("Watching for liveliness changes on 'group1/**'...");

    while let Ok(sample) = subscriber.recv_async().await {
        match sample.kind() {
            SampleKind::Put => {
                println!("[JOIN]  {}", sample.key_expr());
            }
            SampleKind::Delete => {
                println!("[LEAVE] {}", sample.key_expr());
            }
        }
    }
}
```

#### Builder Options

The `LivelinessSubscriberBuilder` supports a `history` option (when available) to also receive samples for tokens that were alive before the subscriber was declared:

```rust
// Receive history of already-alive tokens as Put events, then watch for changes
let subscriber = session
    .liveliness()
    .declare_subscriber("group1/**")
    .history(true)  // also get pre-existing tokens
    .await
    .unwrap();
```

---

### `get` — Snapshot of Currently Alive Tokens

```rust
pub fn get<'b, TryIntoKeyExpr>(
    &self,
    key_expr: TryIntoKeyExpr,
) -> LivelinessGetBuilder<'a, 'b, DefaultHandler>
```

Queries the current set of alive liveliness tokens matching the given key expression. Returns a builder that resolves to a receiver of `Reply` values.

Each reply contains a `Sample` with `kind == SampleKind::Put` and a `key_expr` identifying an alive token.

This is a **point-in-time snapshot**. It does not deliver future changes — use `declare_subscriber` for ongoing monitoring.

#### Builder Options

| Option | Type | Default | Description |
|---|---|---|---|
| `.timeout(duration)` | `Duration` | Session default | Maximum time to wait for replies |

#### Example

```rust
use std::time::Duration;
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let replies = session
        .liveliness()
        .get("group1/**")
        .timeout(Duration::from_secs(1))
        .await
        .unwrap();

    println!("Currently alive tokens in 'group1':");
    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => println!("  alive: {}", sample.key_expr()),
            Err(err) => eprintln!("  error: {:?}", err.payload()),
        }
    }
}
```

---

### Getting Current State + Future Changes

A common requirement is to get a consistent view that includes **both** tokens that were alive before your observer started **and** future changes. There are two approaches:

#### Approach 1: `get` then `subscribe` (manual)

```rust
use zenoh::{Config, sample::SampleKind};
use std::collections::HashSet;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // Step 1: subscribe first to avoid missing events during the query
    let subscriber = session
        .liveliness()
        .declare_subscriber("group1/**")
        .await
        .unwrap();

    // Step 2: snapshot current state
    let mut alive: HashSet<String> = HashSet::new();
    let replies = session
        .liveliness()
        .get("group1/**")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            alive.insert(sample.key_expr().to_string());
        }
    }
    println!("Initial alive tokens: {:?}", alive);

    // Step 3: process ongoing changes
    while let Ok(sample) = subscriber.recv_async().await {
        match sample.kind() {
            SampleKind::Put => {
                alive.insert(sample.key_expr().to_string());
                println!("[JOIN]  {} | total alive: {}", sample.key_expr(), alive.len());
            }
            SampleKind::Delete => {
                alive.remove(&sample.key_expr().to_string());
                println!("[LEAVE] {} | total alive: {}", sample.key_expr(), alive.len());
            }
        }
    }
}
```

#### Approach 2: `declare_subscriber` with `history(true)`

If the builder option is available in your Zenoh version:

```rust
let subscriber = session
    .liveliness()
    .declare_subscriber("group1/**")
    .history(true)
    .await
    .unwrap();

// All pre-existing tokens are delivered as Put, then future changes stream in
while let Ok(sample) = subscriber.recv_async().await {
    // handle Put and Delete as normal
}
```

---

## Difference from Regular Pub/Sub

Liveliness and regular pub/sub both deliver `Sample` values with key expressions, but they serve fundamentally different purposes and have different lifecycle semantics.

| Property | Regular Pub/Sub | Liveliness |
|---|---|---|
| **Purpose** | Data distribution | Presence detection |
| **Lifetime of state** | Explicit: you publish and delete | Automatic: tied to session/transport |
| **Crash detection** | Application must publish a "goodbye" | Routing layer detects transport loss |
| **Historical data** | Via storage/queryable | Via `liveliness().get()` |
| **Payload** | Arbitrary bytes | No payload (key expression only) |
| **Namespace** | Any key expression | Any key expression (separate internal namespace) |
| **Subscriber sees** | All published/deleted values | Join (`Put`) and leave (`Delete`) events |
| **Who sends Delete?** | Application explicitly | Zenoh infrastructure automatically |

### The Core Difference: Automatic Lifecycle

With regular pub/sub, the application controls the entire lifecycle of published data:

```rust
// Regular pub/sub — the application must explicitly signal departure
let session = zenoh::open(Config::default()).await.unwrap();
session.put("services/my-service", "online").await.unwrap();

// ... if the process crashes here, no "offline" is ever sent ...

session.put("services/my-service", "offline").await.unwrap(); // never reached on crash
```

With liveliness, the routing infrastructure handles departure automatically:

```rust
// Liveliness — crash = automatic Delete delivered to all subscribers
let session = zenoh::open(Config::default()).await.unwrap();
let token = session
    .liveliness()
    .declare_token("services/my-service")
    .await
    .unwrap();

// ... if the process crashes here, Zenoh delivers Delete to all observers automatically ...

// No explicit "offline" announcement needed
drop(token); // or just let the session close
```

---

## Worked Example: Service Registry Pattern

This example shows a complete service registry where:

- Each service process declares a liveliness token when it starts.
- A central registry process tracks which services are alive.
- The registry stays accurate even when services crash.

### The Service Process

Each service declares a token under `services/<service-type>/<instance-id>`. Because the token is tied to the session, no shutdown hook is needed — a crash, OOM kill, or graceful exit all result in the same `Delete` notification to the registry.

```rust
// service.rs — run one instance per service node
use zenoh::Config;

#[tokio::main]
async fn main() {
    let service_type = std::env::var("SERVICE_TYPE")
        .unwrap_or_else(|_| "localization".to_string());
    let instance_id = std::env::var("INSTANCE_ID")
        .unwrap_or_else(|_| "node-1".to_string());

    let session = zenoh::open(Config::default()).await.unwrap();

    // Declare presence. Format: services/<type>/<instance>
    let key = format!("services/{}/{}", service_type, instance_id);
    let token = session
        .liveliness()
        .declare_token(&key)
        .await
        .unwrap();

    println!("[{}] Declared liveliness token on '{}'", instance_id, key);

    // Do actual service work here...
    println!("[{}] Running. Press Ctrl-C to stop.", instance_id);
    tokio::signal::ctrl_c().await.unwrap();

    println!("[{}] Shutting down gracefully.", instance_id);
    // token.undeclare() is called implicitly when `token` is dropped,
    // but explicit undeclaration gives a cleaner shutdown signal.
    token.undeclare().await.unwrap();
}
```

### The Registry Process

The registry combines a `get()` for the initial snapshot with a `declare_subscriber()` for ongoing changes. It maintains an in-memory map of which services are alive.

```rust
// registry.rs — run once as the service monitor
use std::collections::{HashMap, HashSet};
use zenoh::{Config, sample::SampleKind};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    // --- Step 1: Subscribe BEFORE querying to avoid a race condition.
    // If we queried first, a service could join between query completion
    // and subscriber declaration, and we'd miss the Put event.
    let subscriber = session
        .liveliness()
        .declare_subscriber("services/**")
        .await
        .unwrap();

    // --- Step 2: Snapshot currently alive services.
    // Map of service_type -> set of alive instance_ids
    let mut registry: HashMap<String, HashSet<String>> = HashMap::new();

    let replies = session
        .liveliness()
        .get("services/**")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            let key = sample.key_expr().to_string();
            if let Some((service_type, instance_id)) = parse_service_key(&key) {
                registry
                    .entry(service_type.to_string())
                    .or_default()
                    .insert(instance_id.to_string());
            }
        }
    }

    println!("=== Initial Registry State ===");
    print_registry(&registry);

    // --- Step 3: Process live changes.
    println!("\n=== Watching for Changes (Ctrl-C to quit) ===");
    while let Ok(sample) = subscriber.recv_async().await {
        let key = sample.key_expr().to_string();

        match sample.kind() {
            SampleKind::Put => {
                if let Some((service_type, instance_id)) = parse_service_key(&key) {
                    registry
                        .entry(service_type.to_string())
                        .or_default()
                        .insert(instance_id.to_string());
                    println!(
                        "[JOIN]  {}::{} | alive instances: {:?}",
                        service_type,
                        instance_id,
                        registry.get(service_type).map(|s| s.len()).unwrap_or(0)
                    );
                }
            }
            SampleKind::Delete => {
                // Handle the wildcard Delete that indicates total connectivity loss
                if key == "**" {
                    println!("[WARN]  Lost all connectivity — clearing registry");
                    registry.clear();
                    continue;
                }

                if let Some((service_type, instance_id)) = parse_service_key(&key) {
                    if let Some(instances) = registry.get_mut(service_type) {
                        instances.remove(instance_id);
                        if instances.is_empty() {
                            registry.remove(service_type);
                        }
                    }
                    println!(
                        "[LEAVE] {}::{} (crash or graceful shutdown)",
                        service_type, instance_id
                    );
                }

                print_registry(&registry);
            }
        }
    }
}

/// Parse "services/<service_type>/<instance_id>" into its components.
fn parse_service_key(key: &str) -> Option<(&str, &str)> {
    let mut parts = key.splitn(3, '/');
    let prefix = parts.next()?;
    if prefix != "services" {
        return None;
    }
    let service_type = parts.next()?;
    let instance_id = parts.next()?;
    Some((service_type, instance_id))
}

fn print_registry(registry: &HashMap<String, HashSet<String>>) {
    if registry.is_empty() {
        println!("  (no services alive)");
        return;
    }
    for (service_type, instances) in registry {
        println!("  {} ({} alive):", service_type, instances.len());
        for instance in instances {
            println!("    - {}", instance);
        }
    }
}
```

### Running the Example

Start the registry:
```bash
cargo run --bin registry
```

Start several service instances in separate terminals:
```bash
SERVICE_TYPE=localization INSTANCE_ID=node-1 cargo run --bin service
SERVICE_TYPE=localization INSTANCE_ID=node-2 cargo run --bin service
SERVICE_TYPE=path-planner INSTANCE_ID=node-1 cargo run --bin service
```

Kill one of them with `kill -9` (no graceful shutdown) and observe the registry immediately receiving a `Delete` event — without any application-level timeout or polling.

---

## Difference from ROS 2 Graph Events

Zenoh's liveliness feature solves a similar problem to ROS 2's graph change events, but with significant design differences.

### ROS 2 Graph Events

ROS 2 provides graph event notifications through `rclcpp::Node::get_graph_event()` and `rclcpp::Node::wait_for_graph_change()`. These notifications fire when any of the following change:

- A node appears or disappears.
- A publisher or subscription is created or destroyed on any topic.
- A service server or client appears or disappears.

This is a **coarse-grained, whole-graph notification**. The application knows *something* changed, but must then call graph introspection APIs (`get_node_names()`, `get_topic_names_and_types()`, etc.) to discover *what* changed.

### Zenoh Liveliness

Zenoh liveliness is **fine-grained and selective**:

| Property | ROS 2 Graph Events | Zenoh Liveliness |
|---|---|---|
| **Granularity** | Any graph change fires a single event | Each token has its own named key expression |
| **What changed** | Not specified — must query graph | Exact key expression of the changed token |
| **Filtering** | None — all graph changes or none | Arbitrary key expression wildcards |
| **Payload** | None | None (key expression only; payload support planned) |
| **Crash detection** | Relies on DDS liveliness QoS | Built into routing layer transport detection |
| **Custom entities** | Only ROS 2 entities (nodes, topics, services) | Any named entity the application defines |
| **Network partitions** | Behavior depends on DDS configuration | Explicit: synthetic `Delete` with key `**` |
| **Performance** | All watchers are notified on any change | Only subscribers matching the key are notified |

### Key Conceptual Difference

ROS 2 graph events describe the **communication graph** — nodes, topics, services, and their type information. They are tightly coupled to the ROS 2 middleware layer.

Zenoh liveliness describes **application-defined named entities**. The token key expressions are entirely under the application's control. A token can represent a ROS node, but equally well a database connection, a robot arm, a configuration version, or any other concept the application cares about. There is no centrally maintained "graph" — liveliness is a distributed, decentralized mechanism.

### Achieving ROS 2 Graph-Like Behavior in Zenoh

Applications that need ROS 2-style whole-graph awareness can subscribe to a wildcard:

```rust
// Subscribe to ALL liveliness changes anywhere in the system
let subscriber = session
    .liveliness()
    .declare_subscriber("**")
    .await
    .unwrap();
```

Applications that need fine-grained, role-specific awareness subscribe to a narrow expression:

```rust
// Only care about path-planner instances
let subscriber = session
    .liveliness()
    .declare_subscriber("robots/*/path-planner")
    .await
    .unwrap();
```

This selective subscription means that in a large system with thousands of entities, a node watching only one service type receives no traffic when unrelated entities join or leave — a significant scalability advantage over the ROS 2 model where any graph change wakes up all graph-event watchers.