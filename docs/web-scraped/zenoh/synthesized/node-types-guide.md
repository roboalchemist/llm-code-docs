# Zenoh Node Types: Router, Peer, and Client

Zenoh defines three node modes that determine how a session participates in the network: **router**, **peer**, and **client**. The mode controls routing behavior, discovery mechanisms, session establishment, and failover characteristics. Choosing the right mode is one of the most important architectural decisions in any Zenoh deployment.

---

## Table of Contents

- [Overview](#overview)
- [Router](#router)
  - [What a Router Does](#what-a-router-does)
  - [When to Use Multiple Routers](#when-to-use-multiple-routers)
  - [Router-to-Router Links](#router-to-router-links)
  - [Router-Specific Config Options](#router-specific-config-options)
- [Peer](#peer)
  - [What a Peer Does](#what-a-peer-does)
  - [Multicast Scouting vs Gossip Scouting](#multicast-scouting-vs-gossip-scouting)
  - [`AutoConnectStrategy`: Always vs GreaterZid](#autoconnectstrategy-always-vs-greaterzid)
  - [P2P Mesh Behavior and Limitations](#p2p-mesh-behavior-and-limitations)
  - [Peer-Specific Config Options](#peer-specific-config-options)
- [Client](#client)
  - [What a Client Does](#what-a-client-does)
  - [What Happens When the Router Dies](#what-happens-when-the-router-dies)
  - [Reconnect Behavior](#reconnect-behavior)
  - [Client-Specific Config Options](#client-specific-config-options)
- [Config Examples](#config-examples)
  - [1. Basic Router](#1-basic-router)
  - [2. Peer with Multicast Scouting (LAN)](#2-peer-with-multicast-scouting-lan)
  - [3. Peer with Gossip Only (No Multicast — Cloud/Container)](#3-peer-with-gossip-only-no-multicast-cloudcontainer)
  - [4. Client Connecting to a Specific Router](#4-client-connecting-to-a-specific-router)
  - [5. Redundant Multi-Router Topology](#5-redundant-multi-router-topology)
- [Code Examples](#code-examples)
  - [Rust](#rust)
  - [Python](#python)
- [Topology Decision Tree](#topology-decision-tree)
  - [Summary Table by Scenario](#summary-table-by-scenario)
  - [Quick Mode Selection](#quick-mode-selection)


---


## Overview

| Property | Router | Peer | Client |
|---|---|---|---|
| Listens for connections | Yes (default: `tcp/[::]:7447`) | Yes (default: `tcp/[::]:0`, ephemeral) | No |
| Forwards messages | Yes | Yes (in P2P mesh) | No |
| Participates in gossip | Yes | Yes | No |
| Participates in multicast | No autoconnect | Yes | Yes |
| Requires router to start | No | No | Yes |
| Routing protocol | Linkstate (inter-router) | P2P or Linkstate | Delegated to router |
| Timestamps messages | Yes (default) | No (default) | No (default) |

The `mode` field in the config file (or set programmatically via `config.set_mode()`) determines which role a session plays. The string values are `"router"`, `"peer"`, and `"client"`.

**Default mode**: `"peer"` when using the library API. `zenohd` runs as `"router"` by default.

---

## Router

### What a Router Does

A router is the infrastructure node of Zenoh. It:

- **Accepts connections** from peers and clients, listening on configured endpoints (default: all interfaces, TCP port 7447).
- **Routes messages** between all connected parties. When a publisher connected to router A publishes on key `/data`, the router forwards it to all connected subscribers, including those connected to peer nodes that have sessions with the router.
- **Propagates topology via linkstate**: Routers exchange linkstate tables with each other, building a full map of the router mesh. Each router knows which other routers exist, which peers and clients are attached to them, and what interests (subscribers, queryables) exist where.
- **Brokers failover for peers** (when `routing.router.peers_failover_brokering = true`): If two peers are both connected to the same router but not directly to each other, the router detects this and forwards data between them. This requires gossip discovery to be enabled and peers configured to gossip to routers.

### When to Use Multiple Routers

Use multiple routers when you need:

- **Redundancy**: If a single router dies, clients and peers attached to it lose connectivity. Two routers with overlapping connections provide a fallback.
- **Geographic separation / WAN bridging**: Connect a router in your cloud to a router in each office. Routers form a backbone mesh; peers and clients at each site connect to the local router.
- **Load distribution**: Many thousands of clients benefit from multiple routers sharing the connection load.
- **Network segmentation**: Separate router meshes with selective bridge routers between zones.

### Router-to-Router Links

Routers connect to each other by listing peer router endpoints in `connect.endpoints`. When configured with mode-dependent values, the `router:` key specifies the endpoints that routers use exclusively.

```json5
connect: {
  endpoints: { router: ["tcp/router2.example.com:7447"] },
}
```

Routers do **not** autoconnect to other routers via multicast scouting by default:
```json5
scouting.multicast.autoconnect: { router: [] }  // empty — routers don't autoconnect
```

Router-to-router links use the linkstate routing protocol to propagate interest declarations across the mesh.

### Router-Specific Config Options

**`routing.router.peers_failover_brokering`**
- Type: `bool`
- Default: `true`
- What it does: When `true`, the router forwards data between two peers that are both connected to it but not directly to each other. Requires `scouting.gossip.enabled = true` and peers with `gossip.target` including `"router"`.
- Example: Two factory floor sensors as peers connect to a gateway router. They cannot reach each other directly (different VLANs). With failover brokering enabled, the router bridges their communication automatically.

**`routing.router.linkstate.transport_weights`**
- Type: `Array<{ dst_zid: string, weight: u16 }>`
- Default: `[]` (empty — all links have weight 100)
- What it does: Assigns a cost/weight to links in linkstate routing. The router uses the higher weight when both endpoints specify one. Used for traffic engineering in multi-router topologies.
- Example:
  ```json5
  routing.router.linkstate.transport_weights: [
    { dst_zid: "aabbccddeeff0011", weight: 10 },   // prefer this link
    { dst_zid: "1122334455667788", weight: 200 },  // avoid this link
  ]
  ```

**`timestamping.enabled`**
- Type: `bool` or `{ router: bool, peer: bool, client: bool }`
- Default: `{ router: true, peer: false, client: false }`
- What it does: Routers timestamp all data messages that do not already carry a timestamp. This enables ordering and deduplication across the mesh.

**`listen.endpoints`**
- Type: `string[]` or `{ router: string[], peer: string[] }`
- Default for router: `["tcp/[::]:7447"]`
- What it does: Which addresses the router accepts incoming connections on. The `[::]` binds to all interfaces on both IPv4 and IPv6.
- Example for a router that also accepts TLS:
  ```json5
  listen.endpoints: ["tcp/0.0.0.0:7447", "tls/0.0.0.0:7448"]
  ```

**`listen.exit_on_failure`**
- Type: `bool`
- Default: `true`
- What it does: If the router cannot bind any listen endpoint, it exits immediately rather than continuing without listening. Typically left `true` for routers since a router that cannot accept connections is useless.

**`transport.unicast.max_sessions`**
- Type: `usize`
- Default: `1000`
- What it does: Maximum number of concurrent unicast transport sessions. Tune upward for routers handling many clients.

**`transport.unicast.max_links`**
- Type: `usize`
- Default: `1`
- What it does: Maximum number of incoming links per transport session. Values greater than 1 enable multipath.

---

## Peer

### What a Peer Does

A peer is the primary application node in Zenoh. It:

- **Communicates directly with other peers** without routing through a router. A peer that discovers another peer via scouting opens a direct session to it.
- **Routes messages through the P2P mesh**: In the default `peer_to_peer` routing mode, each peer forwards messages it receives to all its directly connected neighbors, minus the origin.
- **Optionally connects to routers**: When a router is available, peers connect to it to reach beyond their local discovery zone.
- **Participates in scouting**: Peers listen for and reply to multicast and gossip scout messages, enabling zero-configuration discovery.

### Multicast Scouting vs Gossip Scouting

Zenoh peers discover each other through two complementary mechanisms:

**Multicast scouting** (`scouting.multicast`):
- Uses UDP multicast to `224.0.0.224:7446` (default) to announce presence and discover others on the same Layer 2 network segment.
- Works only within a single L2 broadcast domain (same VLAN, no WAN).
- Controlled by `scouting.multicast.enabled` (default: `true`).
- Fast: discovery happens in milliseconds.
- Not suitable for routed networks (TTL 1 by default, does not cross routers).

**Gossip scouting** (`scouting.gossip`):
- Uses existing unicast transport connections to propagate discovery information.
- Works across routers: when a peer connects to a router, the router gossips back information about all other known peers, which the new peer then connects to.
- Controlled by `scouting.gossip.enabled` (default: `true`).
- `scouting.gossip.multihop` (default: `false`): when `true`, gossip is relayed multiple hops through the mesh, enabling discovery in linkstate mode where not all nodes have direct connectivity. Increases traffic; only useful with `routing.peer.mode = "linkstate"`.

**When to use each:**
- LAN deployment: rely on multicast scouting; gossip is supplemental.
- Cloud/WAN deployment: disable multicast scouting, use gossip only (peers connect to known router addresses, gossip spreads the rest).
- Embedded/constrained devices: disable both and use explicit `connect.endpoints` to connect to a specific router.

### `AutoConnectStrategy`: Always vs GreaterZid

When scouting discovers a peer, both sides may attempt to connect to each other simultaneously, creating redundant connections that are then closed. `AutoConnectStrategy` controls this:

**`"always"` (default)**:
- Both sides attempt to connect when they discover each other.
- Results in a brief window of two simultaneous connection attempts; the duplicate is detected and closed.
- Works correctly in all network topologies, including NAT and asymmetric reachability.
- Use when either peer might not be reachable by the other (e.g., one is behind NAT).

**`"greater-zid"`**:
- A peer only initiates a connection to another peer if its own ZID (128-bit UUID) is numerically greater than the other's.
- Since ZIDs are random UUIDs, exactly one of the two peers will have the greater ZID and initiate the connection.
- Eliminates redundant connection attempts entirely.
- **Risk**: If the peer with the greater ZID is behind NAT or otherwise unreachable, no connection is made. Only use in symmetric networks where either peer can reach the other.

Setting per-target strategy:
```json5
scouting.multicast.autoconnect_strategy: {
  peer: { to_router: "always", to_peer: "greater-zid" }
}
```

This tells peers: always connect to routers when discovered via multicast (routers are expected to be reachable), but use `greater-zid` for peer-to-peer to avoid duplicate connections.

### P2P Mesh Behavior and Limitations

In `routing.peer.mode = "peer_to_peer"` (the default):
- Every peer connects directly to every other peer it discovers.
- Each peer forwards messages to all its neighbors except the sender.
- This creates a full mesh: O(N²) connections, O(1) hop count for any source-to-destination pair.
- **Limitation**: Does not scale beyond tens of peers. With 50 peers in a mesh, each peer holds 49 sessions. With 200 peers, 199 sessions each — this saturates file descriptors and memory.
- **Limitation**: Does not work well across WAN where direct peer-to-peer sessions are impractical (firewall traversal, NAT).

In `routing.peer.mode = "linkstate"`:
- Peers exchange linkstate tables and compute shortest paths, similar to routers.
- Peers do not need full-mesh connectivity; a chain or tree topology works.
- Requires all peers (and routers) in the subsystem to use `mode = "linkstate"`.
- Enables `scouting.gossip.multihop = true` for discovery.
- Use for large peer meshes or sparse/partial-connectivity topologies.

### Peer-Specific Config Options

**`routing.peer.mode`**
- Type: `string` — `"peer_to_peer"` or `"linkstate"`
- Default: `"peer_to_peer"`
- What it does: Selects the intra-peer routing algorithm. Must be the same on all peers and routers in the subsystem.

**`routing.peer.linkstate.transport_weights`**
- Type: `Array<{ dst_zid: string, weight: u16 }>`
- Default: `[]`
- What it does: Same semantics as router linkstate weights, but applies to the peer's outgoing links in linkstate mode.

**`scouting.delay`**
- Type: `u64` (milliseconds)
- Default: `500`
- What it does: In peer mode, the maximum time to wait for remote peers to be discovered before proceeding with other operations. Increasing this allows more peers to be found before the first message is sent, reducing early message loss.

**`scouting.multicast.enabled`**
- Type: `bool`
- Default: `true`
- What it does: Enables UDP multicast scouting. Disable when multicast is not available (cloud, WAN, container networks without multicast routing).

**`scouting.multicast.address`**
- Type: `socket_addr` (IP:port string)
- Default: `"224.0.0.224:7446"`
- What it does: The multicast group address to join. Change only if you have conflicting multicast usage on the same network.

**`scouting.multicast.interface`**
- Type: `string`
- Default: `"auto"`
- What it does: Network interface to use for multicast. `"auto"` picks the first non-loopback interface. Specify explicitly (e.g., `"eth0"`) when a host has multiple interfaces and you need to control which network carries multicast traffic.

**`scouting.multicast.ttl`**
- Type: `u32`
- Default: `1`
- What it does: IP TTL on multicast packets. TTL 1 limits discovery to the local L2 segment. Increase with caution — multicast escaping subnets can cause widespread unexpected connections.

**`scouting.multicast.autoconnect`**
- Type: `WhatAmIMatcher[]` or `{ router: [...], peer: [...], client: [...] }`
- Default: `{ router: [], peer: ["router", "peer"], client: ["router"] }`
- What it does: Which node types to automatically connect to upon multicast discovery. Default peers autoconnect to routers and other peers.

**`scouting.multicast.autoconnect_strategy`**
- Type: `"always"` | `"greater-zid"` or per-mode/per-target object
- Default: `{ peer: { to_router: "always", to_peer: "always" } }`
- What it does: Strategy for avoiding duplicate connections. See AutoConnectStrategy section above.

**`scouting.multicast.listen`**
- Type: `bool` or mode-dependent
- Default: `true`
- What it does: Whether to listen for scout messages on multicast and reply to them. Disabling prevents others from discovering this node via multicast.

**`scouting.gossip.enabled`**
- Type: `bool`
- Default: `true`
- What it does: Enables gossip-based peer discovery through existing connections.

**`scouting.gossip.multihop`**
- Type: `bool`
- Default: `false`
- What it does: When `true`, gossip discovery information is relayed beyond the immediate neighbors. Required for full discovery in linkstate deployments where nodes lack full-mesh connectivity.

**`scouting.gossip.target`**
- Type: `WhatAmIMatcher[]` or per-mode object
- Default: `{ router: ["router", "peer"], peer: ["router", "peer"] }`
- What it does: Which node types to send gossip messages to.

**`scouting.gossip.autoconnect`**
- Type: `WhatAmIMatcher[]` or per-mode object
- Default: `{ router: [], peer: ["router", "peer"] }`
- What it does: Which node types to automatically connect to upon gossip discovery.

**`open.return_conditions.connect_scouted`**
- Type: `bool`
- Default: `true`
- What it does: When `true`, `zenoh::open()` does not return until all scouted peers have been connected. This prevents message loss on the first publish immediately after open. Set `false` for faster startup when you accept that early messages may be lost.

**`open.return_conditions.declares`**
- Type: `bool`
- Default: `true`
- What it does: When `true`, `zenoh::open()` waits to receive initial interest declarations from connected peers. This ensures subscribers and queryables are known before open returns.

**`listen.endpoints`**
- Type: `string[]` or `{ router: string[], peer: string[] }`
- Default for peer: `["tcp/[::]:0"]` (ephemeral port)
- What it does: Peers listen on a random port by default so other peers can connect to them. Specify a fixed port if you need predictable addresses.

---

## Client

### What a Client Does

A client is the simplest Zenoh node. It:

- **Delegates all routing to its router**: A client cannot route messages itself. Every publication, query, and subscription flows through the connected router.
- **Does not listen**: Clients do not accept incoming connections from other nodes. All communication is client-initiated.
- **Does not participate in gossip**: Clients are not in the gossip topology and are invisible to peers that use gossip.
- **Uses multicast scouting to find a router** at startup (unless `connect.endpoints` is configured).

Clients are appropriate for resource-constrained environments, IoT devices, and applications that should not be infrastructure nodes.

### What Happens When the Router Dies

When a client's router becomes unreachable:

1. The transport keepalive mechanism detects the link failure (after `transport.link.tx.lease` milliseconds, divided by `transport.link.tx.keep_alive` checks — default: 10s / 4 checks = detection within ~2.5-10s).
2. The client enters reconnect mode.
3. The client retries connecting to the router using exponential backoff controlled by `connect.retry`.
4. **All in-flight and buffered messages are lost** — the client has no store-and-forward capability.
5. **Subscriptions are re-declared** automatically when the client reconnects.

During the disconnected period, publications from the client are dropped and incoming publications to the client's subscriptions are missed.

### Reconnect Behavior

The reconnect delay uses exponential backoff:

- Starts at `connect.retry.period_init_ms` (default: 1000ms = 1s)
- Multiplies by `connect.retry.period_increase_factor` (default: 2) after each failed attempt
- Caps at `connect.retry.period_max_ms` (default: 4000ms = 4s)

So the retry sequence (with defaults) is: 1s, 2s, 4s, 4s, 4s, ...

The client will keep retrying indefinitely unless:
- `connect.exit_on_failure = true` (default for client mode) and `connect.timeout_ms` is exceeded. Default `timeout_ms` for clients is `0`, meaning **the client fails immediately** if the initial connection attempt fails.

**Important nuance on `connect.timeout_ms` for clients:**
The default is `{ router: -1, peer: -1, client: 0 }`. For clients, `0` means "no retry on initial connect". Once connected and then disconnected, the retry behavior above applies. To make a client retry at startup (useful for containers that start before the router), set:

```json5
connect: {
  timeout_ms: -1,  // wait indefinitely for initial connection
  exit_on_failure: { client: false },
}
```

### Client-Specific Config Options

**`connect.endpoints`**
- Type: `string[]` or `{ router: string[], peer: string[], client: string[] }`
- Default: `[]`
- What it does: Explicit router addresses to connect to. In client mode without endpoints configured, the client uses multicast scouting to find a router. For production deployments, always specify endpoints explicitly.
- Example: `["tcp/router.example.com:7447"]`

**`connect.timeout_ms`**
- Type: `i64` or `{ router: i64, peer: i64, client: i64 }`
- Default: `{ router: -1, peer: -1, client: 0 }`
- Values: `0` = no retry (fail if not immediately connected), `-1` = infinite retry, positive value = timeout in milliseconds
- What it does: Total time to wait for the initial connection to succeed. After this timeout, if not connected: if `exit_on_failure = true`, the process exits; otherwise, `open()` returns an error.

**`connect.exit_on_failure`**
- Type: `bool` or `{ router: bool, peer: bool, client: bool }`
- Default: `{ router: false, peer: false, client: true }`
- What it does: Whether to exit the process if the initial connection cannot be established within `timeout_ms`. The default `true` for clients means a client that cannot find a router will abort rather than silently running disconnected.

**`connect.retry.period_init_ms`**
- Type: `u64` (milliseconds)
- Default: `1000`
- What it does: The initial wait before the first reconnect attempt after a connection loss.

**`connect.retry.period_max_ms`**
- Type: `u64` (milliseconds)
- Default: `4000`
- What it does: The maximum wait between reconnect attempts. After the backoff reaches this value, all subsequent retries use this interval.

**`connect.retry.period_increase_factor`**
- Type: `f64`
- Default: `2`
- What it does: Multiplier applied after each failed reconnect attempt. `2` doubles the wait each time.

**`scouting.timeout`**
- Type: `u64` (milliseconds)
- Default: `3000`
- What it does: In client mode, the maximum time to spend scouting for a router via multicast before giving up (and falling back to explicit connect endpoints or failing). Increase this if routers take longer to respond to scout messages.

**`scouting.multicast.autoconnect`**
- Type: `WhatAmIMatcher[]` or per-mode object
- Default: `{ client: ["router"] }`
- What it does: Clients only autoconnect to routers via multicast, not to other peers.

**`routing.interests.timeout`**
- Type: `u64` (milliseconds)
- Default: `10000`
- What it does: After connecting, how long to wait for incoming interest declarations from the router before proceeding. If this times out, some subscriptions or queryables known to the router may not yet be known to this client, potentially causing message loss for the first publication.

---

## Config Examples

### 1. Basic Router

```json5
{
  mode: "router",

  // Listen on all interfaces, TCP port 7447
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
    exit_on_failure: true,
  },

  // No connect endpoints — wait for others to connect to us
  connect: {
    endpoints: [],
  },

  routing: {
    router: {
      // Forward data between peers that aren't directly connected to each other
      peers_failover_brokering: true,
    },
  },

  timestamping: {
    enabled: true,
    drop_future_timestamp: false,
  },

  scouting: {
    // Routers don't autoconnect via multicast — they are infrastructure
    multicast: {
      enabled: true,
      autoconnect: { router: [] },
      listen: true,  // reply to scout messages so peers can find us
    },
    gossip: {
      enabled: true,
      target: { router: ["router", "peer"] },
      autoconnect: { router: [] },
    },
  },
}
```

### 2. Peer with Multicast Scouting (LAN)

```json5
{
  mode: "peer",

  // Listen on ephemeral port so others can connect back to us
  listen: {
    endpoints: ["tcp/0.0.0.0:0"],
  },

  scouting: {
    delay: 500,  // wait up to 500ms for peers to be discovered before proceeding
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
      interface: "auto",
      ttl: 1,
      autoconnect: { peer: ["router", "peer"] },
      autoconnect_strategy: { peer: { to_router: "always", to_peer: "always" } },
      listen: true,
    },
    gossip: {
      enabled: true,
      multihop: false,
      autoconnect: { peer: ["router", "peer"] },
    },
  },

  routing: {
    peer: {
      mode: "peer_to_peer",
    },
  },

  open: {
    return_conditions: {
      connect_scouted: true,
      declares: true,
    },
  },
}
```

### 3. Peer with Gossip Only (No Multicast — Cloud/Container)

```json5
{
  mode: "peer",

  // Explicit router address — required when multicast is disabled
  connect: {
    endpoints: ["tcp/router.internal:7447"],
    timeout_ms: -1,        // wait indefinitely for router
    exit_on_failure: false,
    retry: {
      period_init_ms: 1000,
      period_max_ms: 30000,
      period_increase_factor: 2,
    },
  },

  listen: {
    endpoints: ["tcp/0.0.0.0:0"],
  },

  scouting: {
    delay: 1000,
    multicast: {
      enabled: false,  // no multicast in cloud/container networks
    },
    gossip: {
      enabled: true,
      multihop: false,
      target: { peer: ["router", "peer"] },
      autoconnect: { peer: ["router", "peer"] },
      autoconnect_strategy: { peer: { to_router: "always", to_peer: "always" } },
    },
  },

  routing: {
    peer: {
      mode: "peer_to_peer",
    },
  },
}
```

### 4. Client Connecting to a Specific Router

```json5
{
  mode: "client",

  connect: {
    // Explicit router address — clients should always configure this in production
    endpoints: ["tcp/router.example.com:7447"],

    // Wait up to 30 seconds for initial connection (useful for startup ordering)
    timeout_ms: 30000,
    exit_on_failure: { client: true },

    retry: {
      period_init_ms: 1000,
      period_max_ms: 8000,
      period_increase_factor: 2,
    },
  },

  scouting: {
    // Multicast scouting timeout if no explicit endpoints found a router
    timeout: 3000,
    multicast: {
      enabled: false,  // disable multicast when using explicit endpoints
    },
    gossip: {
      enabled: false,  // clients don't participate in gossip
    },
  },

  // Clients don't listen — no listen section needed
}
```

### 5. Redundant Multi-Router Topology

Two routers interconnected; peers and clients connect to either router and reach all subscribers.

**Router A** (primary data center):
```json5
{
  mode: "router",

  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
    exit_on_failure: true,
  },

  connect: {
    // Connect to Router B for inter-DC routing
    endpoints: { router: ["tcp/router-b.dc2.example.com:7447"] },
    timeout_ms: { router: -1 },
    exit_on_failure: { router: false },  // start even if B is temporarily down
    retry: {
      period_init_ms: 5000,
      period_max_ms: 60000,
      period_increase_factor: 2,
    },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
      // Prefer the direct link to Router B; high weight = more preferred
      linkstate: {
        transport_weights: [
          { dst_zid: "router-b-zid-here", weight: 10 },
        ],
      },
    },
  },

  scouting: {
    multicast: {
      enabled: true,
      autoconnect: { router: [] },
      listen: true,
    },
    gossip: {
      enabled: true,
      autoconnect: { router: [] },
    },
  },
}
```

**Router B** (secondary data center — mirror image):
```json5
{
  mode: "router",

  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  connect: {
    endpoints: { router: ["tcp/router-a.dc1.example.com:7447"] },
    timeout_ms: { router: -1 },
    exit_on_failure: { router: false },
    retry: {
      period_init_ms: 5000,
      period_max_ms: 60000,
      period_increase_factor: 2,
    },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
    },
  },

  scouting: {
    multicast: {
      enabled: true,
      autoconnect: { router: [] },
      listen: true,
    },
    gossip: {
      enabled: true,
      autoconnect: { router: [] },
    },
  },
}
```

**Client at DC1** (connects to Router A, falls back to Router B):
```json5
{
  mode: "client",

  connect: {
    endpoints: [
      "tcp/router-a.dc1.example.com:7447",
      "tcp/router-b.dc2.example.com:7447",
    ],
    timeout_ms: -1,
    exit_on_failure: { client: false },
    retry: {
      period_init_ms: 1000,
      period_max_ms: 10000,
      period_increase_factor: 2,
    },
  },

  scouting: {
    multicast: {
      enabled: false,
    },
  },
}
```

---

## Code Examples

### Rust

#### Opening a Session as Each Node Type

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    // --- Router ---
    let mut router_config = Config::default();
    router_config
        .insert_json5("mode", r#""router""#)
        .expect("invalid config key");
    router_config
        .insert_json5("listen/endpoints", r#"["tcp/0.0.0.0:7447"]"#)
        .expect("invalid config key");
    let _router_session = zenoh::open(router_config).await.expect("failed to open router session");

    // --- Peer (default mode) ---
    let peer_config = Config::default(); // default mode is "peer"
    let _peer_session = zenoh::open(peer_config).await.expect("failed to open peer session");

    // --- Client connecting to a specific router ---
    let client_config = zenoh::config::client(["tcp/localhost:7447"]);
    let _client_session = zenoh::open(client_config).await.expect("failed to open client session");
}
```

#### Programmatic Config Building

```rust
use zenoh::{Config, config::WhatAmI};

fn build_router_config(listen_addr: &str) -> Config {
    let mut config = Config::default();
    config.set_mode(Some(WhatAmI::Router)).expect("set mode");
    config
        .insert_json5("listen/endpoints", &format!(r#"["{}"]"#, listen_addr))
        .expect("insert listen endpoints");
    config
        .insert_json5("routing/router/peers_failover_brokering", "true")
        .expect("insert failover brokering");
    config
        .insert_json5("scouting/multicast/autoconnect", r#"{"router": []}"#)
        .expect("insert multicast autoconnect");
    config
}

fn build_peer_config_no_multicast(router_addr: &str) -> Config {
    let mut config = Config::default();
    config.set_mode(Some(WhatAmI::Peer)).expect("set mode");
    config
        .insert_json5("connect/endpoints", &format!(r#"["{}"]"#, router_addr))
        .expect("insert connect endpoints");
    config
        .insert_json5("scouting/multicast/enabled", "false")
        .expect("disable multicast");
    config
        .insert_json5("connect/timeout_ms", "-1")
        .expect("insert timeout");
    config
}

fn build_client_config(router_addrs: &[&str]) -> Config {
    let endpoints: Vec<_> = router_addrs.iter().map(|a| format!("\"{}\"", a)).collect();
    let endpoints_json = format!("[{}]", endpoints.join(", "));

    let mut config = Config::default();
    config.set_mode(Some(WhatAmI::Client)).expect("set mode");
    config
        .insert_json5("connect/endpoints", &endpoints_json)
        .expect("insert connect endpoints");
    config
        .insert_json5("connect/timeout_ms", "30000")
        .expect("insert timeout");
    config
        .insert_json5("scouting/multicast/enabled", "false")
        .expect("disable multicast");
    config
}

#[tokio::main]
async fn main() {
    // Open a router
    let router_session = zenoh::open(build_router_config("tcp/0.0.0.0:7447"))
        .await
        .expect("router open");

    // Open a peer that finds the router through gossip
    let peer_session = zenoh::open(build_peer_config_no_multicast("tcp/localhost:7447"))
        .await
        .expect("peer open");

    // Open a client
    let client_session = zenoh::open(build_client_config(&["tcp/localhost:7447"]))
        .await
        .expect("client open");

    // Use the sessions...
    let pub1 = peer_session.declare_publisher("demo/data").await.unwrap();
    pub1.put("hello from peer").await.unwrap();

    let _sub = client_session
        .declare_subscriber("demo/**")
        .callback(|sample| {
            println!("client received: {:?}", sample.payload());
        })
        .background()
        .await
        .unwrap();

    // Clean up
    peer_session.close().await.unwrap();
    client_session.close().await.unwrap();
    router_session.close().await.unwrap();
}
```

#### Loading Config from File

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    // Load mode and all settings from a JSON5 file
    let config = Config::from_file("/etc/zenoh/router.json5")
        .expect("failed to load config file");

    let session = zenoh::open(config).await.expect("failed to open session");

    // Inspect the actual mode after open
    let info = session.info();
    let zid = info.zid().await;
    println!("Session ZID: {}", zid);

    session.close().await.unwrap();
}
```

### Python

#### Opening a Session as Each Node Type

```python
import json
import zenoh


def open_router(listen_addr: str = "tcp/0.0.0.0:7447") -> zenoh.Session:
    conf = zenoh.Config()
    conf.insert_json5("mode", json.dumps("router"))
    conf.insert_json5("listen/endpoints", json.dumps([listen_addr]))
    conf.insert_json5("routing/router/peers_failover_brokering", json.dumps(True))
    conf.insert_json5("scouting/multicast/autoconnect", json.dumps({"router": []}))
    return zenoh.open(conf)


def open_peer(router_addr: str | None = None) -> zenoh.Session:
    conf = zenoh.Config()
    conf.insert_json5("mode", json.dumps("peer"))
    if router_addr is not None:
        # Connect to a specific router; disable multicast
        conf.insert_json5("connect/endpoints", json.dumps([router_addr]))
        conf.insert_json5("scouting/multicast/enabled", json.dumps(False))
        conf.insert_json5("connect/timeout_ms", json.dumps(-1))
    # If router_addr is None, rely on multicast scouting (LAN default)
    return zenoh.open(conf)


def open_client(router_addrs: list[str], timeout_ms: int = 30000) -> zenoh.Session:
    conf = zenoh.Config()
    conf.insert_json5("mode", json.dumps("client"))
    conf.insert_json5("connect/endpoints", json.dumps(router_addrs))
    conf.insert_json5("connect/timeout_ms", json.dumps(timeout_ms))
    conf.insert_json5("scouting/multicast/enabled", json.dumps(False))
    return zenoh.open(conf)


if __name__ == "__main__":
    # Start a router (typically run as a separate process / zenohd)
    with open_router("tcp/0.0.0.0:7447") as router:
        print(f"Router ZID: {router.info().zid()}")

        # Peer that discovers router via explicit connect
        with open_peer("tcp/localhost:7447") as peer:
            print(f"Peer ZID: {peer.info().zid()}")

            # Client that connects to the router
            with open_client(["tcp/localhost:7447"]) as client:
                print(f"Client ZID: {client.info().zid()}")

                # Peer publishes, client receives
                sub = client.declare_subscriber(
                    "demo/**",
                    lambda sample: print(f"Client received: {sample.payload.to_string()}")
                )

                pub = peer.declare_publisher("demo/data")
                pub.put("hello from peer")

                import time
                time.sleep(0.1)  # allow message delivery
```

#### Loading Config from File

```python
import zenoh


def open_from_file(config_path: str) -> zenoh.Session:
    conf = zenoh.Config.from_file(config_path)
    return zenoh.open(conf)


# Override a single setting after loading from file
def open_client_from_file(config_path: str, router_addr: str) -> zenoh.Session:
    import json
    conf = zenoh.Config.from_file(config_path)
    conf.insert_json5("connect/endpoints", json.dumps([router_addr]))
    return zenoh.open(conf)
```

#### Setting Mode Dynamically

```python
import json
import zenoh


def open_with_mode(mode: str, **kwargs) -> zenoh.Session:
    """
    Open a session with a specific mode.
    mode: "router", "peer", or "client"
    kwargs: optional overrides, e.g. connect_endpoints=["tcp/..."]
    """
    assert mode in ("router", "peer", "client"), f"invalid mode: {mode}"
    conf = zenoh.Config()
    conf.insert_json5("mode", json.dumps(mode))

    if "connect_endpoints" in kwargs:
        conf.insert_json5("connect/endpoints", json.dumps(kwargs["connect_endpoints"]))
    if "listen_endpoints" in kwargs:
        conf.insert_json5("listen/endpoints", json.dumps(kwargs["listen_endpoints"]))
    if kwargs.get("no_multicast"):
        conf.insert_json5("scouting/multicast/enabled", json.dumps(False))

    return zenoh.open(conf)


# Examples
router = open_with_mode("router", listen_endpoints=["tcp/0.0.0.0:7447"])
peer   = open_with_mode("peer",   connect_endpoints=["tcp/localhost:7447"], no_multicast=True)
client = open_with_mode("client", connect_endpoints=["tcp/localhost:7447"], no_multicast=True)
```

---

## Topology Decision Tree

Work through these questions from top to bottom to select the right mode(s) for each node in your system.

```
Is this node a dedicated infrastructure/routing node?
├── YES → Use ROUTER
│         └── Does it need to reach other routers in different locations?
│               ├── YES → Add their addresses to connect.endpoints (router key)
│               └── NO  → Leave connect.endpoints empty; peers find you via multicast/gossip
│
└── NO → Is the device resource-constrained (embedded MCU, IoT sensor, mobile)?
          ├── YES → Use CLIENT
          │         └── Does it have a known router address?
          │               ├── YES → Set connect.endpoints explicitly; disable multicast
          │               └── NO  → Enable multicast scouting (only works on LAN)
          │
          └── NO → Use PEER
                    └── What is your network topology?
                          │
                          ├── LAN (same subnet, multicast available)
                          │     └── Use PEER with multicast scouting (defaults work)
                          │
                          ├── Cloud / containers / WAN (no multicast)
                          │     └── Use PEER, disable multicast,
                          │         set connect.endpoints to router address,
                          │         rely on gossip for peer discovery
                          │
                          ├── Large mesh (>50 peers)
                          │     └── Use PEER with routing.peer.mode = "linkstate"
                          │         + scouting.gossip.multihop = true
                          │         (requires all peers to use linkstate)
                          │
                          ├── Need direct P2P without any router
                          │     └── Use PEER, multicast scouting enabled,
                          │         no connect.endpoints (pure P2P mesh)
                          │
                          └── Hybrid (some peers on LAN, some across WAN)
                                └── Use ROUTER at the WAN boundary
                                    LAN peers autoconnect to each other via multicast
                                    WAN peers connect to the router explicitly
```

### Summary Table by Scenario

| Scenario | Node Types | Key Config |
|---|---|---|
| Single LAN, all nodes on same subnet | All peers | Multicast scouting, defaults |
| LAN with many (>50) subscribers | Peers + 1 router | P2P peers, 1 router for fan-out |
| Cloud deployment | Peers + router(s) | No multicast, gossip only, explicit connect |
| IoT sensors → cloud pipeline | Clients + router | Clients connect to router, no listen |
| Embedded MCU | Client or zenoh-pico | Minimal config, explicit connect |
| Two data centers bridged | 2 routers + peers | Router-to-router connect, peers find local router |
| High availability (no single point of failure) | 2+ routers + peers/clients | Clients list both routers in connect.endpoints |
| Offline / airgapped LAN | Peers only | Multicast scouting, no router needed |
| ROS2 robot + cloud processing | Peer (robot) + peer/router (cloud) | zenoh-plugin-ros2dds on robot; cloud peer or router |

### Quick Mode Selection

- **Routing infrastructure / broker**: Router
- **Application that should be reachable by others**: Peer
- **Application that only sends/receives, no routing needed**: Client
- **Embedded / MCU / severely constrained**: Client (or zenoh-pico in client mode)
- **Not sure**: Peer — it works everywhere and degrades gracefully

## See Also

- [Scouting Guide](scouting-guide.md) — multicast and gossip discovery mechanisms that let peers and clients find routers automatically
- [Config Routing Aggregation](config-routing-aggregation.md) — the `routing.router` and `routing.peer` settings that tune inter-node routing behavior
- [Programming Model Guide](programming-model-guide.md) — the session API that reflects the node mode choice
