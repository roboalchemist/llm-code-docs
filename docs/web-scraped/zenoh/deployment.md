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

Every zenoh session declares one of three roles. The role governs how the session discovers neighbors, how it routes messages, and what infrastructure responsibilities it accepts.

### 1.1 Router

A router is a dedicated infrastructure node. It:

- **Routes messages on behalf of others.** Clients and peers that connect to a router rely on it to forward publications, queries, and declarations to the rest of the network.
- **Does not self-discover via multicast.** Routers listen on explicit endpoints and wait for others to connect to them; they do not join multicast groups to find peers spontaneously.
- **Participates in router-level linkstate.** When multiple routers are present they exchange linkstate advertisements so that every router has a full map of the router mesh and can compute shortest paths.
- **Supports failover brokering.** A router can detect that two of its directly-connected peers are not connected to each other and broker messages between them (`peers_failover_brokering`).

Routers are typically long-lived, publicly reachable daemons (`zenohd`). They are the backbone of any multi-segment or cloud deployment.

### 1.2 Peer

A peer is an application-level participant that also performs some routing on its own behalf. It:

- **Self-discovers** using UDP multicast scouting (LAN) or gossip scouting (WAN/mesh).
- **Forms a direct mesh** with other peers it discovers, without needing a router intermediary.
- **Routes within the peer subsystem** using either peer-to-peer mode (flat, direct forwarding) or linkstate mode (topology-aware shortest-path forwarding).
- **Can connect to routers** to bridge with other network segments or cloud infrastructure.

Peers suit scenarios where low administrative overhead is acceptable and all nodes are on the same reachable network segment.

### 1.3 Client

A client is the lightest role. It:

- **Delegates all routing** to a single connected router or peer (its "gateway").
- **Does not route for others.** Messages from other sessions never transit through a client.
- **Connects to one gateway** at a time (though it may be configured with multiple candidate endpoints for failover).
- **Does not participate in scouting** by default — it connects to a statically configured endpoint.

Clients are ideal for constrained devices, browser-based applications, or any endpoint where a full routing stack is undesirable.

```
┌───────────┐         ┌───────────┐         ┌───────────┐
│  Client   │────────▶│  Router   │◀────────│  Client   │
└───────────┘         │           │         └───────────┘
                      │  (routes) │
┌───────────┐         │           │         ┌───────────┐
│   Peer    │◀───────▶│           │◀───────▶│   Peer    │
└───────────┘         └─────┬─────┘         └───────────┘
                            │
                      ┌─────▼─────┐
                      │  Router   │  (another segment)
                      └───────────┘
```

---

## 2. Scouting Mechanisms

Scouting is how zenoh nodes discover each other without requiring pre-configured addresses for every pair.

### 2.1 Multicast Scouting

Multicast scouting is the default discovery mechanism for local networks.

**How it works:**

1. When a session opens, it sends a `Scout` datagram to a well-known UDP multicast group.
2. Any session listening on that group responds with a `Hello` containing its ZID, mode, and listen locators.
3. The scouting session inspects the `Hello` and, if the responder's `WhatAmI` matches its `autoconnect` filter, initiates a unicast transport session to the advertised locator.

**Key configuration parameters:**

| Parameter | Description | Default |
|---|---|---|
| `scouting.multicast.enabled` | Enable/disable multicast scouting | `true` (peer), `false` (router) |
| `scouting.multicast.address` | Multicast group + port | `224.0.0.224:7446` |
| `scouting.multicast.interface` | Network interface for multicast socket | auto-selected |
| `scouting.multicast.ttl` | IP TTL on scout datagrams | `1` |
| `scouting.multicast.autoconnect` | Which `WhatAmI` types to connect to upon discovery | mode-dependent |
| `scouting.multicast.autoconnect_strategy` | `always` or `greater-zid` | `always` |
| `scouting.multicast.listen` | Whether to reply to incoming scout messages | mode-dependent |
| `scouting.delay` | How long (ms) a peer waits for scouts before proceeding | `200` |
| `scouting.timeout` | How long (ms) a client waits to find a router | `3000` |

**TTL = 1** means multicast packets do not cross router boundaries — scouting is confined to the local subnet. This is intentional for local peer discovery. To extend multicast across subnets you would raise TTL and ensure your network infrastructure supports multicast routing (PIM, etc.), though for WAN scenarios gossip scouting is usually more practical.

**AutoConnect strategies:**

- `always` — Upon receiving a `Hello`, unconditionally attempt to connect. Both sides may attempt simultaneously; one connection will be closed as redundant after establishment. This is safe but wastes a brief setup cycle.
- `greater-zid` — Only attempt a connection if your ZID (a 128-bit UUID) is lexicographically greater than the remote's ZID. Since only one side will satisfy this condition, exactly one connection attempt is made. **Caveat:** this assumes both nodes can reach each other. If one is behind NAT and unreachable from the other side, use `always`.

```json5
// Multicast scouting config excerpt
scouting: {
  delay: 200,
  multicast: {
    enabled: true,
    address: "224.0.0.224:7446",
    ttl: 1,
    // autoconnect is mode-dependent: peer connects to peers+routers, client connects to routers
    autoconnect: { peer: "peer|router", client: "router" },
    autoconnect_strategy: { peer: { peer: "greater-zid" }, client: { router: "always" } },
    listen: { peer: true, client: false },
  },
},
```

### 2.2 Gossip Scouting

Gossip scouting propagates discovery information through the already-established zenoh transport graph. It is the mechanism used when multicast is unavailable — for example, across the internet, between cloud VMs, or in complex multi-hop mesh deployments.

**How it works:**

1. When two nodes establish a transport session, they exchange gossip messages describing what other nodes they know about (ZID, mode, locators).
2. Each recipient can connect to the newly-announced nodes.
3. With `multihop: true`, gossip is re-propagated: a node forwards discovery information it received from one neighbor to all other neighbors, allowing discovery to propagate across multiple hops even when there is no direct connectivity.

**Key parameters:**

| Parameter | Description | Default |
|---|---|---|
| `scouting.gossip.enabled` | Enable gossip scouting | `true` |
| `scouting.gossip.multihop` | Propagate gossip beyond direct neighbors | `false` |
| `scouting.gossip.target` | Which node types receive gossip messages | mode-dependent |
| `scouting.gossip.autoconnect` | Which discovered node types to connect to | mode-dependent |
| `scouting.gossip.autoconnect_strategy` | `always` or `greater-zid` | `always` |

**When to enable `multihop`:** Primarily in `linkstate` peer routing mode, where not every peer has a direct connection to every other peer. Without multihop, a peer only learns about nodes its direct neighbors know about. With multihop, discovery flows through the entire connected component. Be aware that multihop gossip increases scouting traffic proportionally to the network size.

```json5
// Gossip scouting for a WAN/cloud scenario
scouting: {
  gossip: {
    enabled: true,
    multihop: true,   // needed for non-fully-connected meshes
    target: { router: "router", peer: "peer|router" },
    autoconnect: { peer: "peer|router" },
    autoconnect_strategy: { peer: { peer: "greater-zid", router: "always" } },
  },
},
```

### 2.3 Static Configuration (No Scouting)

When the network topology is fully known in advance, scouting can be disabled entirely. Nodes are told exactly which endpoints to connect to.

```json5
// Static connect, no scouting
scouting: {
  multicast: { enabled: false },
  gossip:    { enabled: false },
},
connect: {
  endpoints: ["tcp/router1.example.com:7447", "tcp/router2.example.com:7447"],
},
```

This is the safest approach for production deployments where you want deterministic behavior and no surprise connections.

### 2.4 AutoConnect Strategy Summary

```
Scenario                              Recommended strategy
─────────────────────────────────────────────────────────────
All peers mutually reachable (LAN)    greater-zid   (avoids duplicate connections)
One side behind NAT                   always         (NAT'd side can't receive inbound)
Client → Router                       always         (client always initiates)
Router mesh (static connect)          N/A            (scouting disabled)
```

---

## 3. Topology Patterns

### Pattern 1: Peer-to-Peer Local Network

**Use case:** A group of applications on the same LAN that want to publish and subscribe to each other without any dedicated infrastructure.

**Characteristics:**
- All nodes run in `peer` mode
- Multicast scouting discovers all peers automatically
- Each peer connects directly to every other peer it discovers
- No router required
- Scales well up to ~50–100 peers; beyond that, consider adding routers

```
┌────────┐    ┌────────┐    ┌────────┐
│ Peer A │◀──▶│ Peer B │◀──▶│ Peer C │
└────────┘    └────────┘    └────────┘
     ▲                           ▲
     └───────────────────────────┘
       (all connected via multicast discovery)
```

**Config for each peer:**

```json5
// peer_local.json5
{
  mode: "peer",

  scouting: {
    delay: 200,
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
      ttl: 1,
      autoconnect: { peer: "peer|router" },
      autoconnect_strategy: { peer: { peer: "greater-zid" } },
      listen: { peer: true },
    },
    gossip: {
      enabled: true,
      multihop: false,
      autoconnect: { peer: "peer" },
    },
  },

  routing: {
    peer: {
      mode: "peer_to_peer",
    },
  },
}
```

**Notes:**
- `greater-zid` prevents both sides attempting to connect simultaneously.
- `peer_to_peer` routing mode is appropriate here — every peer has a direct link to every other.
- If peers are added dynamically, gossip scouting propagates their existence.

---

### Pattern 2: Client + Single Router (IoT Gateway)

**Use case:** Many constrained devices (sensors, actuators) send data to a central aggregation point. The router acts as the gateway; clients connect to it and rely on it for all routing.

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│ Client 1 │───▶│          │◀───│ Client 3 │
└──────────┘    │  Router  │    └──────────┘
┌──────────┐    │ (zenohd) │
│ Client 2 │───▶│          │
└──────────┘    └──────────┘
```

**Router config (`router_gateway.json5`):**

```json5
{
  mode: "router",

  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  scouting: {
    multicast: { enabled: false },
    gossip:    { enabled: false },
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

**Client config (`client_iot.json5`):**

```json5
{
  mode: "client",

  connect: {
    endpoints: ["tcp/192.168.1.100:7447"],
    timeout_ms: { client: 10000 },
    exit_on_failure: { client: true },
  },

  scouting: {
    timeout: 3000,
    multicast: { enabled: false },
    gossip:    { enabled: false },
  },
}
```

**Notes:**
- Clients use `exit_on_failure: true` so that a failed connection to the router causes the process to exit cleanly rather than silently dropping data.
- Setting `timeout_ms` ensures the client doesn't wait indefinitely.
- Scouting is disabled on both sides — the router's address is statically known.

---

### Pattern 3: Client + Router Cluster (High Availability)

**Use case:** Multiple routers in a cluster provide redundancy. Clients connect to whichever router is available. If a router fails, the client reconnects to another.

```
                ┌──────────────┐
           ┌───▶│   Router A   │◀──────────────────────┐
           │    └──────┬───────┘                       │
           │           │ (router-to-router link)        │
┌──────────┴┐   ┌──────▼───────┐                ┌──────┴────┐
│  Client 1  │   │   Router B   │                │  Client 2  │
└──────────┬┘   └──────────────┘                └──────┬────┘
           │                                           │
           └──────────────────┬────────────────────────┘
                              │ (clients try both routers)
```

**Router A config (`router_a.json5`):**

```json5
{
  mode: "router",
  id: "router-a",

  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  connect: {
    // Connect to Router B to form the cluster
    endpoints: ["tcp/router-b.internal:7447"],
  },

  scouting: {
    multicast: { enabled: false },
    gossip: {
      enabled: true,
      multihop: false,
    },
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

**Router B config (`router_b.json5`):** Mirror of Router A with `connect` pointing to Router A.

**Client config with HA failover (`client_ha.json5`):**

```json5
{
  mode: "client",

  connect: {
    // List multiple routers; zenoh will use the first available and reconnect on failure
    endpoints: [
      "tcp/router-a.internal:7447",
      "tcp/router-b.internal:7447",
    ],
    timeout_ms: { client: 5000 },
    exit_on_failure: { client: false },  // keep retrying, don't exit
    retry: {
      period_init_ms: 1000,
      period_max_ms:  10000,
      period_increase_factor: 2.0,
    },
  },

  scouting: {
    timeout: 5000,
    multicast: { enabled: false },
    gossip:    { enabled: false },
  },
}
```

**Notes:**
- Routers connect to each other, forming a small router mesh. Publications from a client on Router A reach subscribers on Router B automatically.
- `peers_failover_brokering: true` allows a router to broker between two clients that are both connected to it but not to each other — useful when clients on the same router can't communicate directly.
- The client's endpoint list is tried in order. On disconnect the client retries with exponential backoff.

---

### Pattern 4: Multi-Hop Router Mesh

**Use case:** Multiple physically separated network segments (e.g., factory floors, buildings, data centers) each have a local router. These routers interconnect to form a WAN mesh. Peers and clients in each segment connect to their local router.

```
  Segment A                Segment B                Segment C
┌────────────┐           ┌────────────┐           ┌────────────┐
│  Peer A1   │           │  Peer B1   │           │  Peer C1   │
│  Peer A2   │           │  Peer B2   │           │  Client C1 │
│     │      │           │     │      │           │     │      │
│  Router A  │───WAN────▶│  Router B  │───WAN────▶│  Router C  │
└────────────┘           └────────────┘           └────────────┘
                                ▲
                                │ WAN
                                ▼
                         ┌────────────┐
                         │  Router D  │  (hub/core router)
                         └────────────┘
```

**Core router config (`router_core.json5`):**

```json5
{
  mode: "router",
  id: "router-core",

  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  scouting: {
    multicast: { enabled: false },
    gossip: {
      enabled: true,
      multihop: false,   // router mesh uses linkstate, not gossip multihop
    },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
      linkstate: {
        // Optional: tune weights for asymmetric WAN links
        transport_weights: [],
      },
    },
  },

  adminspace: {
    enabled: true,
    permissions: { read: true, write: true },
  },
}
```

**Edge router config (`router_edge_a.json5`):**

```json5
{
  mode: "router",
  id: "router-edge-a",

  listen: {
    // Listen locally for peers/clients in Segment A
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  connect: {
    // Connect to the core router (and optionally peer edge routers for redundancy)
    endpoints: ["tcp/core-router.example.com:7447"],
  },

  scouting: {
    // Allow local peers to discover this router via multicast
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
      ttl: 1,
      autoconnect: { router: "peer" },
      listen: { router: true },
    },
    gossip: {
      enabled: true,
      multihop: false,
    },
  },

  routing: {
    router: {
      peers_failover_brokering: true,
    },
  },
}
```

**Local peer config (connects to edge router):**

```json5
{
  mode: "peer",

  scouting: {
    delay: 200,
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
      ttl: 1,
      // Connect to routers found via multicast, and to other local peers
      autoconnect: { peer: "peer|router" },
      autoconnect_strategy: { peer: { peer: "greater-zid", router: "always" } },
      listen: { peer: true },
    },
    gossip: {
      enabled: true,
      multihop: false,
      autoconnect: { peer: "router" },
    },
  },

  routing: {
    peer: {
      mode: "peer_to_peer",
    },
  },
}
```

**Notes:**
- Router-to-router links form the WAN backbone. Routers exchange linkstate so each knows the full router topology.
- Local peers use multicast to find their segment's router; the router's `listen` on multicast enables it to respond to scout messages.
- The core router can be a single point of failure — for production, deploy Router D with redundant connections and use a VIP or load-balancer.

---

### Pattern 5: Cloud + Edge

**Use case:** Edge devices (industrial controllers, cameras, sensors) run as clients or peers. A cloud-hosted router cluster aggregates all data and exposes it to cloud-based analytics, dashboards, or storage.

```
         CLOUD
┌─────────────────────────┐
│   ┌──────────┐          │
│   │ Router 1 │          │
│   └────┬─────┘          │
│        │                │
│   ┌────▼─────┐          │
│   │ Router 2 │          │
│   └──────────┘          │
│        ▲                │
└────────┼────────────────┘
         │  TLS/QUIC over internet
    ┌────┴─────────────────────────┐
    │  EDGE SITE                   │
    │  ┌──────────┐  ┌──────────┐  │
    │  │ Client 1 │  │ Client 2 │  │
    │  └──────────┘  └──────────┘  │
    └──────────────────────────────┘
```

**Cloud router config (`cloud_router.json5`):**

```json5
{
  mode: "router",
  id: "cloud-router-1",

  listen: {
    // Accept TLS connections from edge clients
    endpoints: ["tls/0.0.0.0:7447"],
  },

  transport: {
    link: {
      tls: {
        listen_private_key: "/etc/zenoh/server.key",
        listen_certificate: "/etc/zenoh/server.crt",
        root_ca_certificate: "/etc/zenoh/ca.crt",
        enable_mtls: true,   // require client certificates for mutual auth
      },
    },
  },

  scouting: {
    multicast: { enabled: false },
    gossip:    { enabled: true, multihop: false },
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

**Edge client config (`edge_client.json5`):**

```json5
{
  mode: "client",

  connect: {
    endpoints: [
      "tls/cloud-router-1.example.com:7447",
      "tls/cloud-router-2.example.com:7447",
    ],
    timeout_ms: { client: 15000 },
    exit_on_failure: { client: false },
    retry: {
      period_init_ms: 2000,
      period_max_ms:  60000,
      period_increase_factor: 2.0,
    },
  },

  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/ca.crt",
        connect_private_key: "/etc/zenoh/edge-device.key",
        connect_certificate:  "/etc/zenoh/edge-device.crt",
        verify_name_on_connect: true,
      },
    },
  },

  scouting: {
    timeout: 10000,
    multicast: { enabled: false },
    gossip:    { enabled: false },
  },
}
```

**Notes:**
- Use `tls` or `quic` locators for encrypted WAN transport. Mutual TLS ensures both the server and the device are authenticated.
- Exponential backoff retry (`period_increase_factor: 2.0`) prevents thundering-herd reconnects if the cloud router restarts.
- `exit_on_failure: false` allows edge devices to keep running and buffer data locally while the cloud is unreachable (combine with `zenoh-ext` AdvancedPublisher for reliable delivery).

---

### Pattern 6: Isolated Peer Groups

**Use case:** Multiple independent peer meshes coexist on the same network segment but must not discover or connect to each other. For example, a factory with separate production lines, or a test environment alongside production.

**Isolation mechanisms:**

1. **Different multicast addresses** — the most reliable isolation method
2. **Different network interfaces** — if groups are on separate VLANs
3. **Disabled scouting + static connect** — total isolation, fully manual topology

**Group A config (`peer_group_a.json5`):**

```json5
{
  mode: "peer",
  id: "peer-group-a-1",

  scouting: {
    delay: 200,
    multicast: {
      enabled: true,
      // Use a non-default multicast address for Group A
      address: "224.0.0.1:7446",
      interface: "eth0",
      ttl: 1,
      autoconnect: { peer: "peer" },
      autoconnect_strategy: { peer: { peer: "greater-zid" } },
      listen: { peer: true },
    },
    gossip: {
      enabled: true,
      multihop: false,
      autoconnect: { peer: "peer" },
    },
  },

  routing: {
    peer: {
      mode: "peer_to_peer",
    },
  },
}
```

**Group B config (`peer_group_b.json5`):**

```json5
{
  mode: "peer",
  id: "peer-group-b-1",

  scouting: {
    delay: 200,
    multicast: {
      enabled: true,
      // Different multicast address — Group B peers never see Group A scouts
      address: "224.0.0.2:7446",
      interface: "eth0",
      ttl: 1,
      autoconnect: { peer: "peer" },
      autoconnect_strategy: { peer: { peer: "greater-zid" } },
      listen: { peer: true },
    },
    gossip: {
      enabled: true,
      multihop: false,
      autoconnect: { peer: "peer" },
    },
  },

  routing: {
    peer: {
      mode: "peer_to_peer",
    },
  },
}
```

**Notes:**
- Since `224.0.0.1` and `224.0.0.2` are different multicast groups, the two sets of peers are completely invisible to each other at the scouting level.
- Combine with key-expression namespacing (`namespace: "group_a"`) to prevent accidental subscription overlap even if the transport isolation is ever bridged.
- For strict security isolation, also bind listeners to specific interfaces and use ACL rules.

---

## 4. Routing Modes

### 4.1 Peer Routing: `peer_to_peer` vs `linkstate`

The `routing.peer.mode` setting controls how peers route publications when they have multiple paths available.

#### `peer_to_peer` (default)

```json5
routing: { peer: { mode: "peer_to_peer" } }
```

- Each peer forwards a message on **all** outgoing links to neighbors that have expressed interest.
- Simple and low-overhead; no global topology state is maintained.
- Best when all peers are fully or nearly fully connected (i.e., every peer can directly reach every other peer on the LAN).
- Does **not** handle multi-hop routing within the peer subsystem — if Peer A cannot reach Peer C directly, messages will not route through Peer B.

#### `linkstate`

```json5
routing: { peer: { mode: "linkstate" } }
```

- Peers exchange linkstate advertisements to build a complete map of the peer-to-peer topology.
- Shortest-path routing is computed; messages hop through intermediate peers when no direct link exists.
- Required for **multi-hop peer meshes** where not all peers are directly connected.
- Increases scouting and routing overhead. Enable `gossip.multihop: true` so discovery propagates across the entire mesh.
- **All peers and routers in the subsystem must use the same mode.** Mixing `peer_to_peer` and `linkstate` leads to undefined routing behavior.

```
When to use linkstate:
  ✓ Peer mesh spans multiple hops (e.g., wireless mesh, serial chains)
  ✓ Not all peers are directly reachable from each other
  ✓ You need optimal routing across a large peer network

When to use peer_to_peer:
  ✓ All peers on the same LAN segment with direct connectivity
  ✓ Small number of peers (<20)
  ✓ Lowest possible routing overhead required
```

### 4.2 Router Linkstate

Routers always use linkstate routing among themselves — this is not configurable. Every router advertises its connections to all other routers, enabling the full router mesh to compute optimal paths.

The `routing.router.linkstate.transport_weights` option assigns weights to specific router-to-router links, influencing path selection in asymmetric topologies:

```json5
routing: {
  router: {
    linkstate: {
      transport_weights: [
        {
          dst_zid: "aabbccddeeff00112233445566778899",
          weight: 200,   // higher weight = less preferred
        },
      ],
    },
  },
},
```

**Weight semantics:** If neither endpoint specifies a weight, the link defaults to weight 100. If one endpoint specifies a weight, that value is used. If both specify weights, the **greater** value is used (conservative — the higher cost wins to avoid loops and asymmetric routing).

### 4.3 Failover Brokering (`peers_failover_brokering`)

```json5
routing: {
  router: {
    peers_failover_brokering: true,
  },
},
```

When enabled, a router monitors which of its directly-connected peers are also connected to each other (via gossip). If two peers are both connected to the router but **not** to each other, the router proactively routes messages between them, acting as a broker.

This is essentially a "soft mesh" feature: peers that would normally only communicate through a direct link can fall back to using the router as an intermediary when the direct link is absent or unavailable. Requires gossip scouting to be enabled (the router uses gossip information to detect peer-to-peer connectivity).

---

## 5. zenohd Router Daemon

### 5.1 Starting zenohd

```bash
# From a binary installation
zenohd

# With a configuration file
zenohd --config /etc/zenoh/router.json5

# With individual config overrides (JSON5 key=value pairs)
zenohd --config /etc/zenoh/router.json5 \
       --cfg "listen/endpoints:[\"tcp/0.0.0.0:7448\"]" \
       --cfg "adminspace/enabled:true"

# From source with cargo
cargo run --release --bin zenohd -- --config DEFAULT_CONFIG.json5
```

**Command-line flags:**

| Flag | Description |
|---|---|
| `--config <path>` | Path to a JSON5, YAML, or JSON config file |
| `--cfg <key=value>` | Override a single config key