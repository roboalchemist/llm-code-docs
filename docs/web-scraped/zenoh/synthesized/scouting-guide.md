# Zenoh Scouting Guide

Scouting is the discovery mechanism that lets Zenoh nodes find each other without requiring hardcoded addresses. When a node starts, it announces itself and listens for announcements from others; when it hears a match it optionally establishes a session automatically. Two mechanisms exist: **multicast scouting** (UDP broadcast on the local network) and **gossip scouting** (propagation over existing sessions). You can also skip scouting entirely by providing static endpoints.

---

## Table of Contents

- [1. How Scouting Works — Overview](#1-how-scouting-works-overview)
  - [Protocol Primitives](#protocol-primitives)
  - [WhatAmI Roles and Default Behavior](#whatami-roles-and-default-behavior)
- [2. Multicast Scouting](#2-multicast-scouting)
  - [How It Works](#how-it-works)
  - [Config Options](#config-options)
  - [When Multicast Works](#when-multicast-works)
  - [When Multicast Fails](#when-multicast-fails)
  - [Complete Multicast Config Example](#complete-multicast-config-example)
- [3. Gossip Scouting](#3-gossip-scouting)
  - [How It Works](#how-it-works)
  - [Config Options](#config-options)
  - [Gossip vs Multicast Trade-offs](#gossip-vs-multicast-trade-offs)
  - [Complete Gossip Config Example](#complete-gossip-config-example)
- [4. Static Endpoints — Bypassing Scouting](#4-static-endpoints-bypassing-scouting)
  - [Config](#config)
  - [Endpoint Format](#endpoint-format)
  - [Per-Mode Endpoints](#per-mode-endpoints)
  - [Connection Timeout and Retry](#connection-timeout-and-retry)
  - [When to Use Static Endpoints](#when-to-use-static-endpoints)
- [5. open.return_conditions](#5-openreturn_conditions)
  - [`connect_scouted`](#connect_scouted)
  - [`declares`](#declares)
  - [Tuning for Fast Startup](#tuning-for-fast-startup)
  - [Tuning for Full Connectivity on Open](#tuning-for-full-connectivity-on-open)
- [6. Timing Parameters](#6-timing-parameters)
  - [`scouting.timeout`](#scoutingtimeout)
  - [`scouting.delay`](#scoutingdelay)
  - [`connect.retry.period_init_ms`](#connectretryperiod_init_ms)
  - [`connect.retry.period_max_ms`](#connectretryperiod_max_ms)
  - [`connect.retry.period_increase_factor`](#connectretryperiod_increase_factor)
  - [Timing Summary Table](#timing-summary-table)
- [7. The `zenoh::scout` API](#7-the-zenohscout-api)
  - [Rust](#rust)
  - [WhatAmI Filter Values](#whatami-filter-values)
  - [Python](#python)
- [8. Decision Guide — Which Mechanism to Use](#8-decision-guide-which-mechanism-to-use)
  - [Same LAN / Local Network](#same-lan-local-network)
  - [Docker (Default Bridge Networking)](#docker-default-bridge-networking)
  - [Kubernetes](#kubernetes)
  - [WAN / Multi-Datacenter](#wan-multi-datacenter)
  - [Mixed Environment (LAN + WAN + containers)](#mixed-environment-lan-wan-containers)
  - [Production: Known Topology, No Discovery](#production-known-topology-no-discovery)
- [9. Complete Config Reference](#9-complete-config-reference)


---


## 1. How Scouting Works — Overview

Every Zenoh node has a **WhatAmI** role: `router`, `peer`, or `client`. Scouting is the process of nodes announcing their role and locators so that other nodes can connect to them.

### Protocol Primitives

| Message   | Direction | Purpose |
|-----------|-----------|---------|
| `Scout`   | Sent by searcher | "Who's out there? I'm looking for `<WhatAmI>`." |
| `Hello`   | Sent by responder | "I'm here. My ZID is `<id>`, my locators are `<addrs>`, my role is `<role>`." |

When a node receives a `Hello` that matches its `autoconnect` filter, it opens a session to the announced locators. The scouting exchange itself is stateless; sessions that result from scouting are full Zenoh sessions.

### WhatAmI Roles and Default Behavior

| Role | Multicast scouting sends Scout? | Multicast scouting replies to Hello? | Gossip participates? |
|------|-------------------------------|--------------------------------------|---------------------|
| Router | Yes | Yes (listen: true) | Yes |
| Peer | Yes | Yes (listen: true) | Yes |
| Client | Yes | No by default | No (clients don't gossip) |

---

## 2. Multicast Scouting

### How It Works

When multicast scouting is enabled, a node binds a UDP socket and joins the multicast group specified by `address`. Periodically it sends a `Scout` UDP datagram to the multicast group. Every node that hears the Scout and has `listen: true` replies with a `Hello` unicast datagram back to the sender. If the sender's `autoconnect` filter matches the `Hello`'s role, it initiates a TCP (or other transport) session to the locators in the `Hello`.

The TTL of `1` (default) means multicast packets do not cross router boundaries — they stay within the local subnet. This is by design for LAN discovery.

```
Node A                       Node B
  |                             |
  |--Scout (multicast UDP)----->|
  |                             |
  |<--Hello (unicast UDP)-------|
  |                             |
  |--TCP connect (to B's addr)->|
  |<--TCP session established---|
```

### Config Options

All options live under `scouting.multicast` in the JSON5 config.

#### `enabled`
- **Type**: `bool`
- **Default**: `true`
- **Description**: Master switch. Set to `false` to disable multicast scouting entirely. When disabled, no Scout datagrams are sent and no Hello replies are sent.
- **Example**:
  ```json5
  scouting: { multicast: { enabled: false } }
  ```

#### `address`
- **Type**: `string` (IPv4 or IPv6 socket address: `"<ip>:<port>"`)
- **Default**: `"224.0.0.224:7446"`
- **Valid values**: Any routable multicast address and port. IPv6 is also supported (e.g. `"ff02::1:7446"`). The address must be the same on all nodes that should discover each other.
- **Description**: The multicast group and port. Scout messages are sent to this address; nodes join this group to receive them.
- **Example**:
  ```json5
  scouting: { multicast: { address: "224.0.0.224:7446" } }
  ```

#### `port`
The port is embedded in the `address` field — there is no separate `port` config key. To change only the port, update the port part of `address`:
```json5
scouting: { multicast: { address: "224.0.0.224:7447" } }
```

#### `ttl`
- **Type**: `uint32`
- **Default**: `1`
- **Valid values**: `1`–`255`
- **Description**: IP Time-To-Live for multicast UDP packets. `1` (default) restricts packets to the local subnet — they will not cross a router boundary. Increase this value only if you want multicast packets to traverse multiple hops (requires network infrastructure support for multicast routing, e.g. IGMP/PIM). In practice, values above `1` rarely work on cloud or managed datacenter networks.
- **Example** (site-local multicast):
  ```json5
  scouting: { multicast: { ttl: 32 } }
  ```

#### `interface`
- **Type**: `string` (interface name or IP address, or `"auto"`)
- **Default**: `"auto"`
- **Valid values**: `"auto"`, a network interface name (e.g. `"eth0"`, `"en0"`), or an IP address (e.g. `"192.168.1.10"`). When `"auto"`, Zenoh selects an appropriate interface automatically. You can also omit the field entirely — the behavior is the same as `"auto"`.
- **Description**: Binds the multicast socket to a specific network interface. Use this in multi-homed hosts to ensure scouting traffic uses the correct interface.
- **Example** (pin to a specific NIC):
  ```json5
  scouting: { multicast: { interface: "eth0" } }
  ```

#### `autoconnect`
- **Type**: `ModeDependentValue<WhatAmIMatcher>` — either a uniform list or a per-mode map
- **Default**: `{ router: [], peer: ["router", "peer"], client: ["router"] }`
- **Valid values**: Lists of `"router"`, `"peer"`, `"client"` or empty list `[]`. Can be specified as a flat list (applies to all modes) or as an object with keys `router`, `peer`, `client`.
- **Description**: Which discovered node types to automatically connect to. Routers default to not auto-connecting (they expect peers to connect to them). Peers auto-connect to both routers and peers. Clients auto-connect only to routers.
- **Examples**:
  ```json5
  // Flat: all modes connect to routers and peers
  scouting: { multicast: { autoconnect: ["router", "peer"] } }

  // Per-mode: peers connect to everything, clients only to routers
  scouting: {
    multicast: {
      autoconnect: { router: [], peer: ["router", "peer"], client: ["router"] }
    }
  }

  // Disable autoconnect entirely (use manual connect instead)
  scouting: { multicast: { autoconnect: [] } }
  ```

#### `autoconnect_strategy`
- **Type**: `ModeDependentValue<TargetDependentValue<AutoConnectStrategy>>`
- **Default**: `"always"` (all modes — router, peer, and client all default to `always` for all connection targets)
- **Valid values**:
  - `"always"` — always attempt connection, may result in bidirectional duplicate connections (duplicates are closed automatically)
  - `"greater-zid"` — only attempt connection if this node's ZID is lexicographically greater than the discovered node's ZID. If both nodes use this strategy, exactly one will initiate.
- **Description**: Controls whether duplicate connections are attempted. `"greater-zid"` reduces redundant connection attempts in a fully-connected peer mesh. It is not suitable when one node is behind NAT and cannot be reached by the other.
- **Examples**:
  ```json5
  // All modes, all targets: always connect
  scouting: { multicast: { autoconnect_strategy: "always" } }

  // Peers use greater-zid for peer-to-peer, always for router
  scouting: {
    multicast: {
      autoconnect_strategy: { peer: { to_router: "always", to_peer: "greater-zid" } }
    }
  }
  ```

#### `listen`
- **Type**: `ModeDependentValue<bool>` — uniform bool or per-mode map
- **Default**: `{ router: true, peer: true, client: false }`
- **Description**: Whether this node replies to Scout messages it receives on the multicast socket. When `false`, the node can still send Scouts and receive Hellos, but will not announce itself. Set to `false` for nodes that should discover but not be discovered (e.g. monitoring agents).
- **Example**:
  ```json5
  // Don't reply to scouts (passive observer)
  scouting: { multicast: { listen: false } }

  // Per-mode: routers reply, clients don't
  scouting: { multicast: { listen: { router: true, peer: true, client: false } } }
  ```

### When Multicast Works

- **Same broadcast domain / LAN segment** — all nodes on the same Layer 2 network.
- **VLANs with IGMP snooping configured** — if the switch is configured to forward multicast to the relevant ports, scouting works across VLANs on the same switch fabric.
- **Single machine** — loopback multicast works for local testing.

### When Multicast Fails

- **Cloud VMs** (AWS, GCP, Azure) — cloud networks typically block multicast entirely. Use gossip or static endpoints.
- **Cross-subnet / cross-router** — TTL=1 packets don't cross IP routers. Increasing TTL alone is insufficient without multicast routing infrastructure.
- **Docker with default bridge networking** — the Docker bridge network does not forward multicast between containers and the host. Use `--network host` or configure a user-defined bridge with multicast support.
- **Kubernetes** — pod networks almost universally block multicast. Use static endpoints pointing to router services.
- **Containers in separate network namespaces** — even on the same host, containers in separate namespaces won't see each other's multicast unless bridges are configured.

### Complete Multicast Config Example

```json5
{
  mode: "peer",
  scouting: {
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
      interface: "auto",
      ttl: 1,
      autoconnect: { router: [], peer: ["router", "peer"], client: ["router"] },
      autoconnect_strategy: "always",  // all modes default to always
      listen: true,
    }
  }
}
```

---

## 3. Gossip Scouting

### How It Works

Gossip scouting propagates discovery information over **existing sessions**, not over UDP multicast. When a node learns about another node (through multicast, static connect, or gossip itself), it can share that knowledge with its neighbors by piggy-backing scouting information on existing Zenoh protocol messages.

This allows discovery to traverse network boundaries that block UDP multicast, as long as at least one TCP/TLS/QUIC path exists between network segments.

```
Datacenter A              WAN link         Datacenter B
  Peer A ─── Router A ──────────────── Router B ─── Peer B
                |                          |
          [knows Peer A]             [knows Peer B]
                |   gossip Hello          |
                └──────────────────────── ┘
           Peer A learns about Peer B via gossip
           (even though UDP multicast can't cross the WAN)
```

**Key difference from multicast**: gossip only works between already-connected nodes. The initial connection must exist first. Gossip then extends discovery *through* that connection.

### Config Options

All options live under `scouting.gossip` in the JSON5 config.

> **Note**: Nodes in `client` mode do not participate in gossip. Gossip is a `router`/`peer` mechanism.

#### `enabled`
- **Type**: `bool`
- **Default**: `true`
- **Description**: Master switch for gossip scouting. When disabled, no gossip messages are sent or processed.
- **Example**:
  ```json5
  scouting: { gossip: { enabled: false } }
  ```

#### `multihop`
- **Type**: `bool`
- **Default**: `false`
- **Valid values**: `true` or `false`
- **Description**: Controls how far gossip information propagates.
  - `false` (default): gossip information is shared only with **directly connected** neighbors (one hop). Node A tells its directly connected neighbors about itself and about nodes it discovered.
  - `true`: gossip information is re-propagated by each recipient, spreading through the entire connected graph (multi-hop). This enables discovery in sparse topologies where not all nodes are directly connected, but comes at the cost of more scouting traffic and reduced scalability.

  Multi-hop gossip is primarily useful when using **linkstate routing mode**, where nodes intentionally form a sparse topology where not every node has a direct connection to every other node.
- **Example**:
  ```json5
  // Enable multi-hop for linkstate routing
  scouting: {
    gossip: {
      enabled: true,
      multihop: true,
    }
  }
  ```

#### `target`
- **Type**: `ModeDependentValue<WhatAmIMatcher>` — uniform list or per-mode map
- **Default**: `{ router: ["router", "peer"], peer: ["router", "peer"], client: [] }`
- **Valid values**: Lists of `"router"` and/or `"peer"`. Can be flat (all modes) or per-mode.
- **Description**: Which *connected* node types to **send** gossip messages to. This controls which neighbors receive the gossip information, not which nodes are discovered. Setting `target: { peer: ["router"] }` means peers will gossip only with routers, not with other peers.
- **Example**:
  ```json5
  // Peers gossip only with routers (hub-and-spoke)
  scouting: {
    gossip: {
      target: { router: ["router", "peer"], peer: ["router"] }
    }
  }
  ```

#### `autoconnect`
- **Type**: `ModeDependentValue<WhatAmIMatcher>`
- **Default**: `{ router: [], peer: ["router", "peer"], client: [] }`
- **Valid values**: Lists of `"router"`, `"peer"`. Flat or per-mode.
- **Description**: Which node types to automatically connect to upon discovery via gossip. Same semantics as `multicast.autoconnect` but for gossip-discovered nodes. Routers default to not auto-connecting (they wait for peers to connect).
- **Example**:
  ```json5
  scouting: {
    gossip: {
      autoconnect: { router: [], peer: ["router", "peer"] }
    }
  }
  ```

#### `autoconnect_strategy`
- **Type**: `ModeDependentValue<TargetDependentValue<AutoConnectStrategy>>`
- **Default**: `"always"` (all modes — router, peer, and client all default to `always` for all connection targets)
- **Valid values**: Same as `multicast.autoconnect_strategy` — `"always"` or `"greater-zid"`, flat or nested by mode and target type.
- **Description**: Same semantics as the multicast version — controls bidirectional connection deduplication. `"greater-zid"` ensures only one of two mutually-discoverable nodes initiates the connection.
- **Example**:
  ```json5
  scouting: {
    gossip: {
      autoconnect_strategy: { peer: { to_router: "always", to_peer: "greater-zid" } }
    }
  }
  ```

### Gossip vs Multicast Trade-offs

| Dimension | Multicast | Gossip |
|-----------|-----------|--------|
| Discovery latency | Fast (immediate Scout/Hello) | Slower (depends on existing sessions) |
| Network overhead | Constant UDP broadcast regardless of topology | Proportional to number of sessions × topology |
| Works across WAN | No (blocked by routers) | Yes (rides TCP/TLS sessions) |
| Works in cloud/K8s | No | Yes (once initial connection exists) |
| Requires initial seed | No | Yes — first node must connect to at least one other |
| Scales to large nets | Limited by multicast domain | Limited by multihop gossip traffic |
| Topology independence | Yes | Yes (with multihop) |

**Common pattern**: Use multicast for LAN discovery, and gossip to propagate that discovery across WAN links to other datacenters.

### Complete Gossip Config Example

```json5
{
  mode: "peer",
  scouting: {
    gossip: {
      enabled: true,
      multihop: false,
      target: { router: ["router", "peer"], peer: ["router", "peer"] },
      autoconnect: { router: [], peer: ["router", "peer"] },
      autoconnect_strategy: "always",  // all modes default to always
    }
  }
}
```

---

## 4. Static Endpoints — Bypassing Scouting

For production deployments with known topologies, you can skip scouting entirely and connect directly to fixed addresses. This eliminates discovery uncertainty and makes startup behavior fully deterministic.

### Config

Static endpoints are configured under `connect.endpoints`. This is independent of scouting configuration — you can have both enabled (static endpoints are tried in addition to scouted ones) or disable scouting entirely.

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/router.example.com:7447"],
  },
  scouting: {
    multicast: { enabled: false },
    gossip: { enabled: false },
  },
  open: {
    return_conditions: {
      connect_scouted: false,  // nothing to scout
      declares: true,
    }
  }
}
```

### Endpoint Format

Endpoints follow the format `<protocol>/<address>:<port>` with optional parameters after `#`:

```
tcp/192.168.1.100:7447
tcp/router.example.com:7447
tls/router.example.com:7447
quic/router.example.com:7447
tcp/192.168.1.100:7447#iface=eth0          # bind to interface (Linux only)
tcp/192.168.1.100:7447#prio=6-7;rel=0      # QoS parameters
tcp/192.168.1.100:7447#so_sndbuf=65000     # TCP buffer size
```

### Per-Mode Endpoints

Endpoints can be specified per node mode:

```json5
connect: {
  endpoints: {
    router: ["tcp/router1.example.com:7447", "tcp/router2.example.com:7447"],
    peer: ["tcp/router1.example.com:7447"],
    client: ["tcp/router1.example.com:7447"],
  }
}
```

### Connection Timeout and Retry

```json5
connect: {
  endpoints: ["tcp/router.example.com:7447"],
  // -1 = infinite retry, 0 = fail immediately if unreachable, >0 = timeout in ms
  timeout_ms: { router: -1, peer: -1, client: 0 },
  exit_on_failure: { router: false, peer: false, client: true },
  retry: {
    period_init_ms: 1000,      // initial retry interval
    period_max_ms: 4000,       // max retry interval (backoff ceiling)
    period_increase_factor: 2, // exponential backoff multiplier
  }
}
```

### When to Use Static Endpoints

- **Production deployments** with stable router addresses
- **Cloud environments** (AWS, GCP, Azure) where multicast is blocked
- **Kubernetes** — connect clients/peers to a stable ClusterIP or LoadBalancer service
- **Docker** — connect containers to a router container by service name
- **Security-sensitive environments** — no broadcast traffic, no discovery
- **Deterministic startup** — session open time is bounded by `connect.timeout_ms`

---

## 5. open.return_conditions

When you call `zenoh::open()`, by default it waits for discovery and connection to complete before returning. The `open.return_conditions` options control exactly what must happen before `open()` unblocks.

### `connect_scouted`
- **Type**: `bool`
- **Default**: `true`
- **Config path**: `open.return_conditions.connect_scouted`
- **Description**: When `true`, `session.open()` blocks until the session has connected to all scouted peers and routers (within the scouting timeout). When `false`, `open()` returns as soon as session initialization completes, and connections to scouted nodes happen asynchronously in the background.

  **Risk when `false`**: The first publications or queries sent immediately after `open()` returns may be lost if the connections haven't been established yet. This is acceptable for long-running publishers that will resend data, but problematic for one-shot senders.

  **When to set `false`**: Fast startup paths where you need `open()` to return quickly and can tolerate missing early messages, e.g. telemetry nodes that continuously publish sensor data.

### `declares`
- **Type**: `bool`
- **Default**: `true`
- **Config path**: `open.return_conditions.declares`
- **Description**: When `true`, `session.open()` waits to receive the initial interest declarations from connected peers before returning. Interest declarations tell the local session which key expressions remote peers are subscribed to, enabling efficient routing from the first message. When `false`, the session returns without waiting for these declarations.

  **Risk when `false`**: Initial publications may trigger extra traffic (routed to all nodes rather than just interested ones) because routing tables aren't populated yet.

  **When to set `false`**: Same as `connect_scouted: false` — when fast startup outweighs the cost of suboptimal initial routing.

### Tuning for Fast Startup

```json5
{
  mode: "peer",
  scouting: {
    timeout: 500,   // reduce client timeout (not used for peer, but harmless)
    delay: 100,     // reduce peer scouting delay from 500ms to 100ms
    multicast: { enabled: true }
  },
  open: {
    return_conditions: {
      connect_scouted: false,  // return immediately, connect in background
      declares: false,         // don't wait for routing table population
    }
  }
}
```

### Tuning for Full Connectivity on Open

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/router.example.com:7447"],
    timeout_ms: -1,   // wait indefinitely for connection
  },
  open: {
    return_conditions: {
      connect_scouted: true,   // wait until connected to router
      declares: true,          // wait until routing is established
    }
  }
}
```

---

## 6. Timing Parameters

### `scouting.timeout`
- **Type**: `uint64` (milliseconds)
- **Default**: `3000` (3 seconds)
- **Applies to**: **Client mode only**
- **Config path**: `scouting.timeout`
- **Description**: In client mode, how long to wait for a router reply before failing. If no router Hello is received within this window, the client fails to open the session (unless a static endpoint is configured). Increase this value on unreliable networks or when routers may take time to start. Decrease it for fast-fail behavior.
- **Example**:
  ```json5
  scouting: { timeout: 5000 }  // wait up to 5 seconds for a router
  ```

### `scouting.delay`
- **Type**: `uint64` (milliseconds)
- **Default**: `500` (0.5 seconds)
- **Applies to**: **Peer mode only**
- **Config path**: `scouting.delay`
- **Description**: In peer mode, the maximum time to wait for scouting replies before proceeding with other operations (opening subscriptions, publishers, etc.). Peers don't fail if no others are found — they just proceed after `delay` ms. Reduce this for faster peer startup when you know the topology is empty. Increase it if peers frequently miss each other during startup.
- **Example**:
  ```json5
  scouting: { delay: 200 }  // only wait 200ms for peers
  ```

### `connect.retry.period_init_ms`
- **Type**: `uint64` (milliseconds)
- **Default**: `1000` (1 second)
- **Config path**: `connect.retry.period_init_ms`
- **Description**: How long to wait before the first reconnect attempt when a static endpoint connection fails. This is the base interval for the exponential backoff.
- **Example**:
  ```json5
  connect: { retry: { period_init_ms: 500 } }
  ```

### `connect.retry.period_max_ms`
- **Type**: `uint64` (milliseconds)
- **Default**: `4000` (4 seconds)
- **Config path**: `connect.retry.period_max_ms`
- **Description**: The maximum interval between reconnect attempts. The backoff grows exponentially from `period_init_ms` up to this ceiling. Once this ceiling is reached, all subsequent retries use this interval.
- **Example**:
  ```json5
  connect: { retry: { period_max_ms: 30000 } }  // back off up to 30 seconds
  ```

### `connect.retry.period_increase_factor`
- **Type**: `float` (multiplier)
- **Default**: `2`
- **Config path**: `connect.retry.period_increase_factor`
- **Description**: Exponential backoff multiplier. Each failed reconnect attempt multiplies the wait interval by this factor. With the defaults (`init=1000`, `max=4000`, `factor=2`), the sequence is: 1000ms → 2000ms → 4000ms → 4000ms → ... Set to `1.0` to disable backoff (fixed interval).
- **Example**:
  ```json5
  connect: {
    retry: {
      period_init_ms: 1000,
      period_max_ms: 60000,
      period_increase_factor: 1.5,  // 1s → 1.5s → 2.25s → 3.4s → ... → 60s
    }
  }
  ```

### Timing Summary Table

| Parameter | Default | Mode | Description |
|-----------|---------|------|-------------|
| `scouting.timeout` | `3000` ms | Client only | Wait for router Hello before failing |
| `scouting.delay` | `500` ms | Peer only | Max wait for peer Hellos before proceeding |
| `connect.retry.period_init_ms` | `1000` ms | All | Initial reconnect wait |
| `connect.retry.period_max_ms` | `4000` ms | All | Backoff ceiling |
| `connect.retry.period_increase_factor` | `2` | All | Exponential backoff multiplier |

---

## 7. The `zenoh::scout` API

Beyond session-level scouting, Zenoh exposes a standalone `scout()` function that continuously listens for nodes on the multicast group and delivers `Hello` messages to your code. This is useful for network diagnostics, topology visualization, or building custom discovery logic.

The standalone scout does **not** open sessions — it only reports what it finds.

### Rust

```rust
use std::time::Duration;
use zenoh::{config::WhatAmI, scout, Config};

#[tokio::main]
async fn main() {
    // Scout for both peers and routers for 1 second
    let receiver = scout(WhatAmI::Peer | WhatAmI::Router, Config::default())
        .await
        .unwrap();

    let _ = tokio::time::timeout(Duration::from_secs(1), async {
        while let Ok(hello) = receiver.recv_async().await {
            println!("{hello}");
            // hello.zid()      -> ZenohId
            // hello.whatami()  -> WhatAmI (Router, Peer, or Client)
            // hello.locators() -> &[Locator]
        }
    })
    .await;

    receiver.stop();
}
```

**With a callback** (fire-and-forget, no receiver):

```rust
use zenoh::{config::WhatAmI, scout, Config};

#[tokio::main]
async fn main() {
    let scout = scout(WhatAmI::Peer | WhatAmI::Router, Config::default())
        .callback(|hello| {
            println!("Discovered: {} at {:?}", hello.zid(), hello.locators());
        })
        .await
        .unwrap();

    tokio::time::sleep(std::time::Duration::from_secs(5)).await;
    scout.stop();
}
```

**With a custom channel** (bounded):

```rust
use zenoh::{config::WhatAmI, scout, Config};

#[tokio::main]
async fn main() {
    let receiver = scout(WhatAmI::Peer | WhatAmI::Router, Config::default())
        .with(flume::bounded(32))
        .await
        .unwrap();

    while let Ok(hello) = receiver.recv_async().await {
        println!("{hello}");
    }
}
```

### WhatAmI Filter Values

| Value | Matches |
|-------|---------|
| `WhatAmI::Router` | Router nodes only |
| `WhatAmI::Peer` | Peer nodes only |
| `WhatAmI::Client` | Client nodes only |
| `WhatAmI::Peer \| WhatAmI::Router` | Peers and routers |
| `WhatAmI::Peer \| WhatAmI::Router \| WhatAmI::Client` | All node types |

### Python

```python
import threading
import zenoh

zenoh.init_log_from_env_or("error")

print("Scouting for 1 second...")
scout = zenoh.scout(what="peer|router")

# Stop after 1 second
threading.Timer(1.0, lambda: scout.stop()).start()

for hello in scout:
    print(f"ZID: {hello.zid}, WhatAmI: {hello.whatami}, Locators: {hello.locators}")
```

**With custom config** (restrict to a specific interface):

```python
import zenoh

conf = zenoh.Config()
conf.insert_json5("scouting/multicast/interface", '"eth0"')

scout = zenoh.scout(what="router", config=conf)

import threading
threading.Timer(2.0, lambda: scout.stop()).start()

for hello in scout:
    print(hello)
```

---

## 8. Decision Guide — Which Mechanism to Use

### Same LAN / Local Network

All nodes on the same Layer 2 subnet. Multicast scouting is the right choice — zero configuration required.

```json5
{
  mode: "peer",
  scouting: {
    multicast: { enabled: true },
    gossip: { enabled: true },  // gossip helps after connections are formed
  }
}
```

### Docker (Default Bridge Networking)

Docker's default bridge network does not support multicast between containers. Use either `--network host` (if containers can share the host network) or configure static endpoints.

**Option A — Host network mode** (simplest, Linux only):
```bash
docker run --network host my-zenoh-node
```
No config changes needed; multicast works on the host interface.

**Option B — Static endpoints** (works everywhere):
```json5
// Router config
{
  mode: "router",
  listen: { endpoints: ["tcp/0.0.0.0:7447"] },
  scouting: { multicast: { enabled: false }, gossip: { enabled: false } }
}

// Peer/client config (replace "zenoh-router" with container name or IP)
{
  mode: "peer",
  connect: { endpoints: ["tcp/zenoh-router:7447"] },
  scouting: { multicast: { enabled: false }, gossip: { enabled: false } }
}
```

### Kubernetes

Pod networks universally block multicast. Deploy a router as a Service and have all peers/clients connect to it statically.

```yaml
# zenoh-router Deployment + Service
apiVersion: v1
kind: Service
metadata:
  name: zenoh-router
spec:
  selector:
    app: zenoh-router
  ports:
    - port: 7447
      targetPort: 7447
```

```json5
// Router config (runs as Deployment)
{
  mode: "router",
  listen: { endpoints: ["tcp/0.0.0.0:7447"] },
  scouting: { multicast: { enabled: false }, gossip: { enabled: true } }
}

// Client/peer config
{
  mode: "client",
  connect: { endpoints: ["tcp/zenoh-router.default.svc.cluster.local:7447"] },
  scouting: { multicast: { enabled: false } }
}
```

### WAN / Multi-Datacenter

Nodes are separated by a WAN link. One or more routers have public/VPN-reachable addresses. Gossip propagates discovery across the WAN once routers are connected.

```json5
// Router A (datacenter A) — connects to Router B at startup
{
  mode: "router",
  connect: {
    endpoints: ["tcp/router-b.datacenter-b.example.com:7447"]
  },
  listen: { endpoints: ["tcp/0.0.0.0:7447"] },
  scouting: {
    multicast: { enabled: true },   // discover local peers via multicast
    gossip: {
      enabled: true,
      multihop: false,
      target: { router: ["router", "peer"], peer: ["router", "peer"] },
    }
  }
}

// Peer in datacenter A — discovers router A via multicast, gets datacenter B via gossip
{
  mode: "peer",
  scouting: {
    multicast: { enabled: true },
    gossip: { enabled: true, multihop: false }
  }
}
```

### Mixed Environment (LAN + WAN + containers)

```json5
// Hub router with static WAN peers and local multicast
{
  mode: "router",
  listen: { endpoints: ["tcp/0.0.0.0:7447"] },
  connect: {
    endpoints: ["tcp/wan-router-1.example.com:7447"]
  },
  scouting: {
    multicast: {
      enabled: true,
      interface: "eth0",   // LAN interface only
    },
    gossip: {
      enabled: true,
      multihop: false,     // one hop is enough via routers
    }
  }
}
```

### Production: Known Topology, No Discovery

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/router-1.prod.example.com:7447", "tcp/router-2.prod.example.com:7447"],
    timeout_ms: 10000,
    exit_on_failure: { client: true },
    retry: {
      period_init_ms: 1000,
      period_max_ms: 30000,
      period_increase_factor: 2,
    }
  },
  scouting: {
    multicast: { enabled: false },
    gossip: { enabled: false },
  },
  open: {
    return_conditions: {
      connect_scouted: false,
      declares: true,
    }
  }
}
```

---

## 9. Complete Config Reference

The full scouting section with all defaults shown explicitly:


```json5
{
  mode: "peer",

  // Static connect endpoints (empty = rely on scouting)
  connect: {
    timeout_ms: { router: -1, peer: -1, client: 0 },
    endpoints: [],
    exit_on_failure: { router: false, peer: false, client: true },
    retry: {
      period_init_ms: 1000,
      period_max_ms: 4000,
      period_increase_factor: 2,
    },
  },

  // What must be true before session.open() returns
  open: {
    return_conditions: {
      connect_scouted: true,   // wait for scouted-node connections
      declares: true,          // wait for routing declarations
    },
  },

  scouting: {
    // Client mode: how long to wait for a router Hello (ms)
    timeout: 3000,

    // Peer mode: max delay before proceeding without finding peers (ms)
    delay: 500,

    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
      interface: "auto",
      ttl: 1,
      autoconnect: { router: [], peer: ["router", "peer"], client: ["router"] },
      autoconnect_strategy: "always",  // all modes default to always
      listen: true,
    },

    gossip: {
      enabled: true,
      multihop: false,
      target: { router: ["router", "peer"], peer: ["router", "peer"] },
      autoconnect: { router: [], peer: ["router", "peer"] },
      autoconnect_strategy: "always",  // all modes default to always
    },
  },
}
```

## See Also

- [Node Types Guide](node-types-guide.md) — how router, peer, and client modes affect which scouting mechanisms are used
- [Config Connect Listen](config-connect-listen.md) — static endpoint configuration that replaces scouting in production deployments
- [Config Routing Aggregation](config-routing-aggregation.md) — routing configuration that works with the topology discovered by scouting
