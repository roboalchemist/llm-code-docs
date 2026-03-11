# Zenoh Deployment and Topology Guide

## Table of Contents

1. [WhatAmI: Router, Peer, Client](#1-whatami-router-peer-client)
2. [Scouting Mechanisms](#2-scouting-mechanisms)
3. [Topology Patterns](#3-topology-patterns)
4. [Routing Modes](#4-routing-modes)
5. [zenohd Router Daemon](#5-zenohd-router-daemon)
6. [Multi-Process Patterns](#6-multi-process-patterns)

---

## 1. WhatAmI: Router, Peer, Client

Every Zenoh session declares one of three roles. This role governs how the node participates in topology discovery, how it routes messages, and what responsibilities it takes on.

### 1.1 Router

A **router** is a dedicated infrastructure node, typically run as `zenohd`. Its defining characteristics are:

- **Fixed topology**: Routers do not perform autonomous self-discovery of other routers. They must be explicitly told where to connect via static `connect` endpoints, or they must `listen` and wait for incoming connections.
- **Routes for others**: A router forwards messages between any combination of clients, peers, and other routers connected to it.
- **Stable, always-on**: Routers are long-lived processes. They form the backbone of a Zenoh deployment.
- **Linkstate propagation**: In multi-router deployments, routers exchange topology information (link-state) so that each router has a global view of the network graph and can compute optimal forwarding paths.

Routers are the right choice when you need a reliable rendezvous point, when you need to bridge network segments, or when you are building cloud infrastructure.

### 1.2 Peer

A **peer** is a full participant in the Zenoh mesh that discovers other participants and routes its own traffic. Its defining characteristics are:

- **Dynamic self-discovery**: Peers use multicast scouting and/or gossip scouting to find each other without any prior configuration.
- **Direct connections**: Once two peers discover each other, they open a direct transport session. There is no mandatory intermediary.
- **Mesh networking**: A peer network converges to a mesh where every peer has direct links to every other discovered peer (in `peer_to_peer` mode) or exchanges link-state to route over multi-hop paths (in `linkstate` mode).
- **No dedicated infrastructure required**: A local LAN can function fully with only peers — no router process is needed.

Peers are the right choice for local-area deployments (robots, lab equipment, embedded devices on a LAN) where low latency and mesh resilience are important.

### 1.3 Client

A **client** delegates all routing responsibility to a connected router or peer gateway. Its defining characteristics:

- **Single upstream**: A client connects to exactly one router (or peer acting as a gateway). All pub/sub/query traffic flows through that single connection.
- **No routing**: A client does not forward traffic on behalf of anyone else. It only sends and receives its own data.
- **Lightweight**: Clients maintain minimal state. They do not need to track the rest of the topology.
- **Reconnection**: If the upstream router fails, a client can be configured with multiple endpoints to try in sequence or with retry logic.

Clients are the right choice for resource-constrained devices, browser applications (via WebSocket), or any node that simply wants to publish or subscribe without participating in infrastructure.

### Summary Table

| Characteristic | Router | Peer | Client |
|---|---|---|---|
| Self-discovers | No (static config) | Yes (multicast/gossip) | No |
| Routes for others | Yes | Yes (in mesh) | No |
| Requires `zenohd` | Typically yes | No | No |
| Topology role | Infrastructure backbone | Mesh participant | Leaf node |
| Typical use case | Cloud, gateway, WAN bridge | LAN devices, robots | IoT sensors, browsers |

---

## 2. Scouting Mechanisms

Scouting is the process by which Zenoh nodes discover each other and decide whether to establish transport sessions. There are three approaches: multicast, gossip, and static configuration.

### 2.1 Multicast Scouting

Multicast scouting uses UDP multicast to announce presence and discover neighbors on the same Layer 2 network segment.

**How it works:**

1. On startup, a node sends a `Scout` UDP multicast packet to the configured multicast group address and port.
2. Any node already listening on that address responds with a `Hello` message containing its ZID, its WhatAmI role, and its listening locators.
3. The scouting node evaluates the `autoconnect` configuration to decide whether to open a transport session to the discovered node.
4. Scouting continues periodically so that nodes joining later are discovered.

**Key configuration fields under `scouting.multicast`:**

| Field | Default | Description |
|---|---|---|
| `enabled` | `true` | Enable or disable multicast scouting entirely |
| `address` | `224.0.0.224:7446` | Multicast group address and UDP port |
| `interface` | auto | Network interface to use |
| `ttl` | `1` | IP TTL on multicast packets (1 = LAN only) |
| `autoconnect` | role-dependent | Which WhatAmI roles to automatically connect to on discovery |
| `autoconnect_strategy` | `always` | `always` or `greater_zid` (see below) |
| `listen` | role-dependent | Whether to reply to incoming scout messages |

**TTL:** The default TTL of `1` prevents multicast packets from leaving the local subnet. Increasing TTL allows discovery across routers that forward multicast, but this is rarely desired — multicast scouting is fundamentally a LAN mechanism.

**AutoConnectStrategy:**

The `autoconnect_strategy` field controls duplicate-connection prevention in a peer mesh:

- **`always`** (default): Every node that discovers another will attempt to connect. Two peers discovering each other simultaneously will both attempt to connect, resulting in two parallel transport sessions briefly. Zenoh detects and closes the duplicate, but there is a window of redundancy.
- **`greater_zid`**: A node will only initiate a connection if its own ZID (a 128-bit value) is lexicographically greater than the discovered node's ZID. Since both nodes use the same rule, exactly one will initiate. This eliminates duplicate connections entirely in a well-connected mesh.

`greater_zid` is recommended for stable peer meshes. `always` is safer when NAT or asymmetric connectivity means one peer cannot reach the other.

### 2.2 Gossip Scouting

Gossip scouting propagates discovery information through the network by piggybacking on existing transport sessions. It is the mechanism used when multicast is not available (WAN, cloud, VPN, cross-subnet).

**How it works:**

1. When two nodes are connected, they exchange information about other nodes they know about.
2. This "gossip" propagates through the network, allowing nodes that cannot see each other via multicast to learn about each other's existence and locators.
3. Based on the `autoconnect` configuration, a node may then open a direct transport session to a newly gossip-discovered node.

**Key configuration fields under `scouting.gossip`:**

| Field | Default | Description |
|---|---|---|
| `enabled` | `true` | Enable or disable gossip scouting |
| `multihop` | `false` | Whether gossip information is re-propagated beyond one hop |
| `target` | role-dependent | Which WhatAmI roles to send gossip messages to |
| `autoconnect` | role-dependent | Which WhatAmI roles to automatically connect to via gossip |
| `autoconnect_strategy` | `always` | `always` or `greater_zid` |

**`multihop`:** When `false`, gossip only propagates one hop (to directly connected nodes). When `true`, each node re-propagates the gossip it receives, allowing discovery across the entire connected network. Multihop is primarily useful with `linkstate` peer routing mode, where not all nodes are directly connected. It increases scouting traffic and reduces scalability, so it should be enabled only when needed.

### 2.3 Static Configuration

For maximum control and predictability, scouting can be disabled entirely and connections configured statically.

**Disabling scouting:**

```json5
scouting: {
  multicast: { enabled: false },
  gossip:    { enabled: false },
}
```

**Static connect endpoints:**

```json5
connect: {
  endpoints: ["tcp/192.168.1.10:7447", "tcp/192.168.1.11:7447"],
}
```

**Static listen endpoints:**

```json5
listen: {
  endpoints: ["tcp/0.0.0.0:7447"],
}
```

Static configuration is appropriate for production infrastructure where topology must be explicit and deterministic, for security-sensitive environments where autodiscovery is a risk, and for WAN/cloud deployments where multicast is unavailable and gossip would require a pre-existing connection anyway.

---

## 3. Topology Patterns

### Pattern 1: Peer-to-Peer Local Network

**Use case:** A group of devices on the same LAN (robots, lab instruments, developer workstations) that need to communicate directly without any infrastructure process.

**Topology:**

```
[Peer A] ←——→ [Peer B]
    ↑               ↑
    └———→ [Peer C] ←┘
```

All nodes run as peers. Multicast scouting discovers all participants, and each pair establishes a direct transport session. This forms a full mesh.

**How it works:**
- Each peer sends multicast scout packets on startup.
- Each peer replies to incoming scout messages.
- `autoconnect: ["peer"]` causes each peer to connect to every other peer it discovers.
- With `greater_zid` strategy, each pair of peers ends up with exactly one connection between them.

**Config (all nodes use this):**

```json5
// peer_local.json5
{
  mode: "peer",

  scouting: {
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
      ttl: 1,
      // Connect to any peer discovered via multicast
      autoconnect: { peer: ["peer"] },
      autoconnect_strategy: {
        peer: { peer: "greater_zid" }
      },
      listen: { peer: true },
    },
    gossip: {
      enabled: true,
      multihop: false,
      autoconnect: { peer: ["peer"] },
    },
  },

  routing: {
    peer: {
      mode: "peer_to_peer",
    },
  },
}
```

**Tradeoffs:**
- Zero infrastructure required.
- Each node must be on the same multicast domain (same LAN/VLAN).
- Full mesh means O(n²) connections as the network grows — use `linkstate` mode for larger peer networks.

---

### Pattern 2: Client + Single Router (IoT Gateway)

**Use case:** Resource-constrained IoT devices connect to a central gateway router. Sensors publish data; actuators subscribe. The router is the single point of rendezvous.

**Topology:**

```
[Sensor A] ──┐
[Sensor B] ──┼──→ [Router / Gateway] ←── [Dashboard Client]
[Sensor C] ──┘
```

**Router config:**

```json5
// router_gateway.json5
{
  mode: "router",

  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  scouting: {
    multicast: {
      enabled: true,
      // Router listens for scouts but doesn't autoconnect to clients
      autoconnect: { router: [] },
      listen: { router: true },
    },
    gossip: {
      enabled: true,
    },
  },

  routing: {
    router: {
      peers_failover_brokering: false,
    },
  },

  adminspace: {
    enabled: true,
    permissions: { read: true, write: false },
  },
}
```

**Client (sensor/device) config:**

```json5
// client_sensor.json5
{
  mode: "client",

  connect: {
    endpoints: ["tcp/192.168.1.1:7447"],
    // Retry connection if router is temporarily unavailable
    exit_on_failure: { client: false },
    retry: {
      period_init_ms: 1000,
      period_max_ms:  30000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    // Clients can use multicast to find the router automatically
    // if they don't know the router's IP in advance
    multicast: {
      enabled: true,
      autoconnect: { client: ["router"] },
    },
    timeout: 3000,
  },
}
```

**Notes:**
- If the router's address is known, set `scouting.multicast.enabled: false` and rely entirely on `connect.endpoints`.
- The `exit_on_failure: false` combined with retry config lets clients survive router restarts.
- If scouting is used for discovery, the client will connect to the first router it finds.

---

### Pattern 3: Client + Router Cluster (High Availability)

**Use case:** Production deployment where a single router is a single point of failure. Multiple routers are deployed, and clients connect to whichever is available.

**Topology:**

```
[Client] ──→ [Router 1] ←——→ [Router 2]
                                  ↑
[Client] ──────────────────────→─┘
```

The two routers are connected to each other so that messages published on one are forwarded to subscribers on the other. Clients list both routers in their `connect.endpoints` and will connect to the first available.

**Router 1 config:**

```json5
// router1.json5
{
  mode: "router",

  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  connect: {
    // Connect to router 2 to form a router mesh
    endpoints: ["tcp/192.168.1.12:7447"],
    exit_on_failure: { router: false },
    retry: {
      period_init_ms: 1000,
      period_max_ms: 10000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    multicast: { enabled: false },
    gossip: {
      enabled: true,
      // Gossip to routers and peers; clients discover via connect endpoints
      target: { router: ["router", "peer"] },
    },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
      linkstate: {},
    },
  },

  adminspace: {
    enabled: true,
    permissions: { read: true, write: false },
  },
}
```

**Router 2 config** — identical except it does not `connect` to Router 1 (Router 1 initiates), or both can initiate with idempotent connection handling:

```json5
// router2.json5
{
  mode: "router",

  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  // Router 2 also tries to connect to Router 1 for resilience
  connect: {
    endpoints: ["tcp/192.168.1.11:7447"],
    exit_on_failure: { router: false },
    retry: {
      period_init_ms: 1000,
      period_max_ms: 10000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    multicast: { enabled: false },
    gossip: { enabled: true },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
    },
  },

  adminspace: {
    enabled: true,
    permissions: { read: true, write: false },
  },
}
```

**Client config (HA-aware):**

```json5
// client_ha.json5
{
  mode: "client",

  connect: {
    // List both routers; client will connect to the first reachable one
    endpoints: [
      "tcp/192.168.1.11:7447",
      "tcp/192.168.1.12:7447",
    ],
    exit_on_failure: { client: false },
    retry: {
      period_init_ms: 500,
      period_max_ms: 5000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    multicast: { enabled: false },
  },
}
```

**Notes:**
- The client connects to exactly one router at a time. If that router fails, the client retries the endpoint list.
- The two routers maintain a session between themselves, so a subscriber on Router 2 receives publications from a client on Router 1.
- `peers_failover_brokering: true` allows the router to broker messages between two peers that are both connected to it but not connected to each other.

---

### Pattern 4: Multi-Hop Mesh (Routers Linking Network Segments)

**Use case:** Multiple network segments (factory floors, building wings, data center racks) each have their own local devices and a local router. The routers are connected over a WAN or management network to form a multi-hop topology.

**Topology:**

```
Segment A                  WAN                  Segment B
[Peer A1]─┐                                    ┌─[Peer B1]
[Peer A2]─┼─→ [Router A] ←——— TCP ———→ [Router B] ←─┤
[Peer A3]─┘        ↑                        ↑   └─[Peer B2]
                   └──────── [Router C] ────┘
                              ↑
                         Segment C
```

**Router A config:**

```json5
// router_segment_a.json5
{
  mode: "router",

  listen: {
    // Listen for local peers on the LAN
    endpoints: [
      "tcp/10.0.1.1:7447",    // local segment interface
    ],
  },

  connect: {
    // Connect to other routers over WAN
    endpoints: [
      "tcp/10.100.0.2:7447",  // Router B WAN address
      "tcp/10.100.0.3:7447",  // Router C WAN address
    ],
    exit_on_failure: { router: false },
    retry: {
      period_init_ms: 2000,
      period_max_ms:  60000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    // Use multicast locally to discover peers on the LAN
    multicast: {
      enabled: true,
      interface: "eth0",       // LAN interface
      ttl: 1,
      autoconnect: { router: ["peer"] },
      listen: { router: true },
    },
    gossip: {
      enabled: true,
      // Propagate peer discovery info to other routers via gossip
      target: { router: ["router", "peer"] },
      autoconnect: { router: ["peer"] },
    },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
      linkstate: {
        // Optionally weight this router's links
        transport_weights: [
          // Lower weight = preferred path to Router B
          // { dst_zid: "<router_b_zid>", weight: 50 }
        ],
      },
    },
  },

  adminspace: { enabled: true },
}
```

**Peers on Segment A** use the standard peer config but with `autoconnect: { peer: ["router"] }` in multicast to ensure they connect to Router A:

```json5
// peer_segment_a.json5
{
  mode: "peer",

  scouting: {
    multicast: {
      enabled: true,
      interface: "eth0",
      ttl: 1,
      autoconnect: {
        peer: ["router", "peer"],  // connect to router and other local peers
      },
      autoconnect_strategy: {
        peer: {
          peer: "greater_zid",
          router: "always",
        }
      },
      listen: { peer: true },
    },
    gossip: {
      enabled: true,
      multihop: true,   // needed for cross-segment peer discovery
    },
  },

  routing: {
    peer: {
      mode: "linkstate",  // needed for multi-hop peer routing
    },
  },
}
```

**Notes:**
- Router-to-router links carry traffic between segments. Each router is responsible for routing local traffic to and from remote segments.
- `gossip.multihop: true` on peers allows them to discover peers in other segments via the router chain.
- Link-state weights allow traffic engineering: you can prefer certain inter-router links over others.

---

### Pattern 5: Cloud + Edge

**Use case:** Edge devices (cameras, sensors, PLCs) at remote sites connect to a centralized cloud router cluster. The cloud exposes data to analytics applications and dashboards.

**Topology:**

```
Cloud Region
┌────────────────────────────────┐
│  [Cloud Router 1]              │
│         ↕  (router mesh)       │
│  [Cloud Router 2]              │
└───────────┬────────────────────┘
            │ Internet / VPN
     ┌──────┴──────┐
     ↓             ↓
[Edge Router A]  [Edge Router B]
  ↓    ↓           ↓     ↓
[Dev] [Dev]      [Dev]  [Dev]
```

**Cloud router config:**

```json5
// cloud_router.json5
{
  mode: "router",

  listen: {
    endpoints: [
      "tcp/0.0.0.0:7447",
      // TLS for external connections from edge
      "tls/0.0.0.0:7448",
    ],
  },

  connect: {
    // Connect to peer cloud router(s)
    endpoints: ["tcp/10.0.0.2:7447"],  // internal cloud network
    exit_on_failure: { router: false },
    retry: {
      period_init_ms: 1000,
      period_max_ms: 10000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    // No multicast in cloud
    multicast: { enabled: false },
    gossip: {
      enabled: true,
      target: { router: ["router"] },
    },
  },

  transport: {
    link: {
      tls: {
        listen_certificate: "/etc/zenoh/certs/server.pem",
        listen_private_key: "/etc/zenoh/certs/server.key",
        root_ca_certificate: "/etc/zenoh/certs/ca.pem",
        enable_mtls: true,
      },
    },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
    },
  },

  adminspace: { enabled: true },
}
```

**Edge router config:**

```json5
// edge_router.json5
{
  mode: "router",

  listen: {
    // Listen for local edge devices on LAN
    endpoints: ["tcp/192.168.10.1:7447"],
  },

  connect: {
    // Connect to cloud router(s) over TLS
    endpoints: [
      "tls/cloud-router-1.example.com:7448",
      "tls/cloud-router-2.example.com:7448",
    ],
    exit_on_failure: { router: false },
    retry: {
      period_init_ms: 5000,
      period_max_ms:  120000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    // Multicast to find local edge devices
    multicast: {
      enabled: true,
      interface: "eth1",  // LAN-facing interface
      ttl: 1,
      autoconnect: { router: ["peer", "client"] },
      listen: { router: true },
    },
    gossip: { enabled: true },
  },

  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/certs/ca.pem",
        connect_certificate: "/etc/zenoh/certs/edge-client.pem",
        connect_private_key: "/etc/zenoh/certs/edge-client.key",
        verify_name_on_connect: true,
      },
    },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
    },
  },
}
```

**Edge device (client) config:**

```json5
// edge_device_client.json5
{
  mode: "client",

  connect: {
    // Connect to local edge router
    endpoints: ["tcp/192.168.10.1:7447"],
    exit_on_failure: { client: false },
    retry: {
      period_init_ms: 1000,
      period_max_ms: 30000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    multicast: {
      enabled: true,
      // Will auto-find the edge router via multicast if IP unknown
      autoconnect: { client: ["router"] },
    },
    timeout: 5000,
  },
}
```

**Notes:**
- Mutual TLS (mTLS) is strongly recommended for cloud-facing links. The `enable_mtls: true` setting on the cloud router, combined with client certificates on edge routers, ensures bidirectional authentication.
- The edge router bridges the local LAN (multicast-based discovery) to the cloud (static TLS connections).
- If the cloud connection drops, edge devices can still communicate locally through the edge router.

---

### Pattern 6: Isolated Peer Groups

**Use case:** Multiple independent peer groups on the same physical network (e.g., multiple robot teams in the same building) that must not interfere with each other. Each group forms its own mesh, invisible to the others.

**The isolation problem:** If all groups use the default multicast address `224.0.0.224:7446`, they will discover each other and potentially cross-connect.

**Two isolation approaches:**

#### Approach A: Different Multicast Addresses

Give each group a distinct multicast group address and/or port:

```json5
// group_alpha.json5
{
  mode: "peer",
  scouting: {
    multicast: {
      enabled: true,
      address: "224.0.0.225:7446",  // Group Alpha's exclusive address
      ttl: 1,
      autoconnect: { peer: ["peer"] },
      autoconnect_strategy: { peer: { peer: "greater_zid" } },
    },
    gossip: { enabled: true },
  },
  routing: { peer: { mode: "peer_to_peer" } },
}
```

```json5
// group_beta.json5
{
  mode: "peer",
  scouting: {
    multicast: {
      enabled: true,
      address: "224.0.0.226:7446",  // Group Beta's exclusive address
      ttl: 1,
      autoconnect: { peer: ["peer"] },
      autoconnect_strategy: { peer: { peer: "greater_zid" } },
    },
    gossip: { enabled: true },
  },
  routing: { peer: { mode: "peer_to_peer" } },
}
```

#### Approach B: Disable Multicast, Use Static Endpoints

Each group disables multicast scouting and uses explicit connect addresses:

```json5
// group_alpha_node.json5
{
  mode: "peer",
  scouting: {
    multicast: { enabled: false },  // No cross-group discovery
    gossip: { enabled: true },
  },
  connect: {
    // Only connect to known members of this group
    endpoints: [
      "tcp/10.0.1.11:7447",
      "tcp/10.0.1.12:7447",
    ],
  },
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },
  routing: { peer: { mode: "peer_to_peer" } },
}
```

**Notes:**
- Different multicast addresses is simpler to manage as group membership grows.
- Static endpoints are more secure but require updating configs when nodes are added.
- VLANs at the network layer provide the strongest isolation, but Zenoh-level isolation (different multicast groups) is practical when VLAN configuration is not available.

---

## 4. Routing Modes

### 4.1 Peer Routing: `peer_to_peer` vs `linkstate`

The `routing.peer.mode` field controls how peers route messages in a peer mesh. This setting **must be consistent across all peers and routers in a deployment**.

#### `peer_to_peer` (default)

In `peer_to_peer` mode, a peer only routes messages along its directly established transport sessions. It does not maintain or exchange a global topology map.

- **Subscription propagation**: When peer A subscribes to key expression `foo/**`, it declares that interest to all peers directly connected to it. Those peers will forward matching publications to A.
- **Scope**: Only works across direct connections. If peer A is connected to peer B, and B is connected to peer C, but A is not directly connected to C, then A will not receive publications from C (unless the router provides failover brokering).
- **Best for**: Small-to-medium fully connected meshes (all peers connected to all others). Most LAN deployments.
- **Scalability**: O(n²) connections; practical up to tens of peers.

```json5
routing: {
  peer: {
    mode: "peer_to_peer",
  },
}
```

#### `linkstate`

In `linkstate` mode, every peer exchanges its full link-state (what it is connected to) with every other peer in the network. Each node builds a global graph and computes shortest paths.

- **Multi-hop routing**: Peer A can route messages to peer C via peer B even without a direct A↔C connection. This allows sparse mesh topologies.
- **Gossip required**: `scouting.gossip.multihop: true` should be enabled so that nodes learn about each other beyond one hop.
- **State overhead**: Each peer maintains the full topology graph. This increases memory and CPU usage as the network grows.
- **Best for**: Large peer networks, cases where direct full-mesh connectivity is not possible (e.g., mixed wired/wireless with range limitations), or geographic deployments.

```json5
routing: {
  peer: {
    mode: "linkstate",
  },
  // Also enable multihop gossip for multi-hop peer discovery
}
```

Combined with multihop gossip:

```json5
{
  mode: "peer",
  scouting: {
    gossip: {
      enabled: true,
      multihop: true,
      autoconnect: { peer: ["peer", "router"] },
    },
    multicast: {
      enabled: true,
      autoconnect: { peer: ["peer", "router"] },
    },
  },
  routing: {
    peer: {
      mode: "linkstate",
    },
  },
}
```

### 4.2 Router Link-State

Router-to-router routing always uses link-state. The `routing.router.linkstate` section configures per-link weights for traffic engineering:

```json5
routing: {
  router: {
    linkstate: {
      transport_weights: [
        {
          // Prefer traffic to this specific router over a faster link
          dst_zid: "aabbccddeeff00112233445566778899",
          weight: 50,  // Lower weight = preferred (like OSPF cost)
        },
        {
          dst_zid: "112233445566778899aabbccddeeff00",
          weight: 200,  // Higher weight = backup path
        },
      ],
    },
  },
}
```

**Weight semantics:**
- If neither endpoint specifies a weight, the default weight of `100` is used.
- If only one endpoint specifies a weight, that weight is used.
- If both specify weights, the **greater** value is applied (conservative approach: the link is as slow as its slowest estimator).

### 4.3 Failover Brokering (`peers_failover_brokering`)

When two peers are both connected to the same router but not directly connected to each other, normally they cannot communicate in `peer_to