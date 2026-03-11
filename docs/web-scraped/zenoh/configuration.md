# Zenoh Configuration Reference Guide

## Table of Contents

1. [Overview & File Format](#overview)
2. [Node Identity & Metadata](#identity)
3. [Mode](#mode)
4. [Connect](#connect)
5. [Listen](#listen)
6. [Open (Session Open Behavior)](#open)
7. [Scouting](#scouting)
   - [Multicast Scouting](#multicast-scouting)
   - [Gossip Scouting](#gossip-scouting)
8. [Timestamping](#timestamping)
9. [Queries](#queries)
10. [Routing](#routing)
11. [QoS Overwrite](#qos-overwrite)
12. [Aggregation](#aggregation)
13. [Namespace](#namespace)
14. [Transport](#transport)
    - [Unicast Transport](#unicast-transport)
    - [Multicast Transport](#multicast-transport)
    - [Link Layer](#link-layer)
    - [Shared Memory](#shared-memory)
    - [Authentication](#authentication)
15. [Access Control (ACL)](#access-control)
16. [Downsampling](#downsampling)
17. [Low Pass Filter](#low-pass-filter)
18. [Admin Space](#admin-space)
19. [Plugins](#plugins)
20. [Configuration Decision Guide](#decision-guide)

---

## Overview & File Format {#overview}

Zenoh configuration files use JSON5 format (`.json5`), which supports comments (`//`), trailing commas, and unquoted keys. YAML (`.yaml`/`.yml`) is also supported. TOML is supported as an unstable feature.

Pass the config file to `zenohd` with `-c my_config.json5`, or load programmatically via `Config::from_file()`.

**Key concepts:**
- Many options accept a **mode-dependent value**: either a single value applying to all modes, or an object with `router`, `peer`, and `client` keys supplying per-mode values.
- Options commented out with `//` show valid structure but are disabled by default.
- `null` means "not set / use default."

---

## Node Identity & Metadata {#identity}

### `id`

| Property | Value |
|---|---|
| **Path** | `id` |
| **Type** | String (hex unsigned 128-bit integer, no leading zeros) |
| **Default** | Random u128 generated at startup |
| **Example** | `"1234567890abcdef"` |

**What it controls:** The unique identifier of this zenoh node across the entire zenoh network. Used for routing decisions and visible in the admin space at `@/<zid>/router` (or `peer`/`client`).

**When to change:** Set explicitly when you need deterministic node identity—for example, when another node's ACL or routing policy references this node by ZID, or when you need reproducible testing environments.

**Tradeoffs:**
- ✅ Deterministic identity, useful for ACL rules referencing `zids`
- ✅ Consistent admin space paths across restarts
- ⚠️ **ZIDs must be globally unique.** Duplicate ZIDs in a network cause undefined routing behavior and may silently corrupt message delivery. Never copy a config file with a fixed `id` to multiple nodes without changing it.

---

### `metadata`

| Property | Value |
|---|---|
| **Path** | `metadata` |
| **Type** | Arbitrary JSON object |
| **Default** | `{}` (empty) |
| **Example** | `{ name: "edge-sensor-01", location: "building-A", role: "publisher" }` |

**What it controls:** Human-readable metadata attached to this node. Not interpreted by zenoh itself. Exposed in the admin space at `@/<zid>/router` (or `peer`/`client`). Useful for fleet management, diagnostics, and monitoring tools.

**When to change:** Always populate in production deployments for observability. Add any fields relevant to your operational context.

**Tradeoffs:**
- ✅ Visible in admin space for diagnostics with no runtime cost
- ✅ Completely free-form; any JSON is valid
- ℹ️ Not transmitted on the data plane; only in admin/scouting info

---

## Mode {#mode}

### `mode`

| Property | Value |
|---|---|
| **Path** | `mode` |
| **Type** | String enum |
| **Valid Values** | `"router"`, `"peer"`, `"client"` |
| **Default** | `"peer"` |

**What it controls:** The fundamental operational role of this zenoh node.

| Mode | Description |
|---|---|
| `"router"` | Forwards data between peers and clients. Listens on well-known ports. Acts as a broker/relay. Participates in all routing protocols. |
| `"peer"` | Full participant: publishes, subscribes, and can relay data to other directly-connected peers. Participates in gossip. Does not run linkstate by default. |
| `"client"` | Lightweight consumer/producer. Connects to routers only. Does not relay data. Does not participate in gossip or multicast scouting (only initiates scout). |

**When to change:**
- Use `"router"` for infrastructure nodes (cloud VMs, gateways, brokers).
- Use `"peer"` for devices that need direct P2P communication or can assist in local relay.
- Use `"client"` for resource-constrained devices or applications that only need to talk to a router.

**Tradeoffs:**

| Mode | CPU/Memory | Connectivity | Routing participation |
|---|---|---|---|
| `router` | High | Listens + connects | Full (linkstate, gossip) |
| `peer` | Medium | Listens (ephemeral port) + connects | Gossip, P2P |
| `client` | Low | Connects only | None |

---

## Connect {#connect}

Controls outbound connections to other zenoh nodes.

### `connect.endpoints`

| Property | Value |
|---|---|
| **Path** | `connect.endpoints` |
| **Type** | Array of endpoint strings, or mode-dependent object |
| **Default** | `[]` (empty) |
| **Examples** | `["tcp/10.0.0.1:7447"]`, `{ router: ["tcp/router:7447"], peer: [] }` |

**What it controls:** The list of remote endpoints this node attempts to connect to at startup. Supports TCP, UDP, TLS, QUIC, WebSocket, Unix sockets, and vSock. Endpoint URIs follow the pattern `<protocol>/<address>:<port>`.

**Endpoint modifiers** (appended with `#`):
- `iface=eth0` — bind outgoing connection to a specific interface (Linux only)
- `so_sndbuf=65000;so_rcvbuf=65000` — TCP socket buffer sizes
- `bind=192.168.0.1:0` — local bind address (incompatible with `iface`)
- `dscp=0x08` — IP DSCP field for QoS marking
- `retry_period_init_ms=5000;retry_period_max_ms=30000` — per-endpoint retry override

**Link-level QoS modifiers** (appended with `?`):
- `prio=6-7` — restrict this link to carrying only priority levels 6–7 (data_low, background)
- `rel=0` — mark link as best-effort

**When to change:** Set explicit endpoints when:
- Multicast scouting is not available (e.g., cross-subnet, cloud)
- You want to connect to a known router/peer deterministically
- You need to disable discovery entirely and use static topology

**Tradeoffs:**
- ✅ Deterministic, works across subnets and firewalls
- ✅ Can partition traffic across links by priority
- ⚠️ Static topology—doesn't adapt to network changes without config update
- ⚠️ Must be kept in sync with the remote's `listen.endpoints`

---

### `connect.timeout_ms`

| Property | Value |
|---|---|
| **Path** | `connect.timeout_ms` |
| **Type** | Integer (ms) or mode-dependent object |
| **Default** | `{ router: -1, peer: -1, client: 0 }` |

**What it controls:** How long the node waits for **all** configured `connect.endpoints` to be successfully connected before proceeding.

| Value | Behavior |
|---|---|
| `0` | No retry; proceed immediately even if connections failed |
| `-1` | Wait indefinitely until all connections are established |
| `N > 0` | Wait up to N milliseconds |

**When to change:**
- Set to `-1` for routers and critical peers that must not start without their upstream connections.
- Set to `0` for clients that should start immediately and reconnect in the background.
- Set to a positive value (e.g., `30000`) for startup orchestration with a timeout.

**Tradeoffs:**
- `-1` guarantees connectivity before proceeding but can block startup indefinitely if peers are unavailable
- `0` allows fast startup but may lose early publications/queries
- Positive value provides a bounded startup delay

---

### `connect.exit_on_failure`

| Property | Value |
|---|---|
| **Path** | `connect.exit_on_failure` |
| **Type** | Boolean or mode-dependent object |
| **Default** | `{ router: false, peer: false, client: true }` |

**What it controls:** Whether the process exits if the `connect.timeout_ms` deadline is exceeded without all connections being established.

**When to change:**
- Set to `true` for clients in managed environments where a failed connection should trigger a restart (e.g., via systemd or Kubernetes).
- Set to `false` for peers/routers that should continue operating in degraded mode.

---

### `connect.retry`

Controls the exponential backoff behavior for reconnection attempts.

#### `connect.retry.period_init_ms`

| Property | Value |
|---|---|
| **Path** | `connect.retry.period_init_ms` |
| **Type** | Integer (ms) or mode-dependent |
| **Default** | `1000` |

Initial wait before the first retry attempt.

#### `connect.retry.period_max_ms`

| Property | Value |
|---|---|
| **Path** | `connect.retry.period_max_ms` |
| **Type** | Integer (ms) or mode-dependent |
| **Default** | `4000` |

Maximum interval between retries (cap for exponential backoff).

#### `connect.retry.period_increase_factor`

| Property | Value |
|---|---|
| **Path** | `connect.retry.period_increase_factor` |
| **Type** | Float |
| **Default** | `2.0` |

Multiplier applied to the retry interval after each failed attempt. With defaults: 1s → 2s → 4s (capped).

**When to change retry parameters:**
- Reduce `period_max_ms` (e.g., `2000`) for fast-reconnecting sensors.
- Increase `period_max_ms` (e.g., `60000`) for cloud/WAN connections to reduce connection storm during outages.
- Set `period_increase_factor: 1.0` for a fixed-interval retry (no backoff).

---

## Listen {#listen}

Controls which local endpoints this node binds and accepts connections on.

### `listen.endpoints`

| Property | Value |
|---|---|
| **Path** | `listen.endpoints` |
| **Type** | Array of endpoint strings, or mode-dependent object |
| **Default** | `{ router: ["tcp/[::]:7447"], peer: ["tcp/[::]:0"] }` |

**What it controls:** The local addresses this node listens on for incoming connections.

- `[::]:7447` — all interfaces, IPv4+IPv6, port 7447 (router well-known port)
- `[::]:0` — all interfaces, OS-assigned ephemeral port (peer default)
- `0.0.0.0:7447` — IPv4 only
- `tcp/0.0.0.0:7447#iface=eth0` — bind only to eth0

Same modifier syntax as `connect.endpoints` applies (`#iface`, `#so_sndbuf`, `?prio`, etc.).

**When to change:**
- Clients typically do not listen; set `endpoints: []` for pure clients.
- Bind to a specific interface/IP for security (avoid listening on untrusted interfaces).
- Use a fixed port for firewall rules.
- Use Unix sockets (`unixsock-stream`) for local IPC.

**Tradeoffs:**
- Listening on `[::]:0` (peer default) makes peer discoverable but uses an unpredictable port
- Listening on a fixed port is firewall-friendly but requires port uniqueness per host
- Not listening at all (client mode) reduces attack surface but requires a router

---

### `listen.timeout_ms`

| Property | Value |
|---|---|
| **Path** | `listen.timeout_ms` |
| **Type** | Integer (ms) or mode-dependent |
| **Default** | `0` |

**What it controls:** How long to wait for all listen endpoints to be successfully bound. `0` means try once with no retry. `-1` means wait indefinitely.

**When to change:** Set to `-1` for routers that must bind before accepting connections, or when the desired port may be temporarily unavailable (e.g., TIME_WAIT state).

---

### `listen.exit_on_failure`

| Property | Value |
|---|---|
| **Path** | `listen.exit_on_failure` |
| **Type** | Boolean or mode-dependent |
| **Default** | `true` |

**What it controls:** Whether the process exits if any listen endpoint fails to bind within `listen.timeout_ms`.

**When to change:** Set to `false` for resilient deployments where partial listen failure is acceptable.

---

### `listen.retry`

Same structure and semantics as `connect.retry`. Controls backoff when retrying a failed listen bind.

| Sub-option | Default |
|---|---|
| `period_init_ms` | `1000` |
| `period_max_ms` | `4000` |
| `period_increase_factor` | `2.0` |

---

## Open (Session Open Behavior) {#open}

### `open.return_conditions.connect_scouted`

| Property | Value |
|---|---|
| **Path** | `open.return_conditions.connect_scouted` |
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** When `true`, `zenoh::open()` blocks until the session has connected to all scouted peers and routers before returning to the application.

**When to change:** Set to `false` for applications that must start immediately (e.g., embedded systems with tight boot deadlines) and can tolerate losing early messages.

**Tradeoffs:**
- `true`: Safer startup, first publications are more likely delivered; slight startup delay
- `false`: Faster startup; early publications/queries to scouted nodes may be lost

---

### `open.return_conditions.declares`

| Property | Value |
|---|---|
| **Path** | `open.return_conditions.declares` |
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** When `true`, `zenoh::open()` waits to receive initial declarations (subscriber/publisher/queryable info) from connected peers before returning.

**When to change:** Set to `false` if startup time is critical; but note this may cause extra redundant traffic as peers re-declare interests.

---

## Scouting {#scouting}

Scouting is zenoh's peer discovery mechanism. Two mechanisms exist: UDP multicast and gossip (over established sessions).

### `scouting.timeout`

| Property | Value |
|---|---|
| **Path** | `scouting.timeout` |
| **Type** | Integer (ms) |
| **Default** | `3000` |
| **Applies to** | Client mode |

**What it controls:** How long a **client** waits for a router to be found via scouting before failing. If no router is found within this window, the client connect attempt fails (subject to `connect.exit_on_failure`).

**When to change:**
- Increase (e.g., `10000`) in environments where router startup is slow or unreliable
- Decrease (e.g., `1000`) for fast-fail applications that have a fallback

---

### `scouting.delay`

| Property | Value |
|---|---|
| **Path** | `scouting.delay` |
| **Type** | Integer (ms) |
| **Default** | `500` |
| **Applies to** | Peer mode |

**What it controls:** How long a **peer** dedicates to scouting for other remote peers before proceeding with other operations.

**When to change:**
- Increase for larger or slower networks where peer discovery takes longer
- Decrease for fast-startup peers in a known topology

---

## Multicast Scouting {#multicast-scouting}

### `scouting.multicast.enabled`

| Property | Value |
|---|---|
| **Path** | `scouting.multicast.enabled` |
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** Enables UDP multicast-based peer discovery. When enabled, this node sends and receives multicast scout packets to automatically discover other zenoh nodes on the local network segment.

**When to change:** Disable when:
- Operating in a multicast-hostile environment (many cloud VMs, some VLANs, VPNs)
- All endpoints are statically configured and discovery is unnecessary
- You want to prevent unintended peer discovery

**Tradeoffs:**
- `true`: Zero-configuration local discovery; may cause unwanted connections in shared networks
- `false`: No automatic discovery; all peers must be explicitly configured in `connect.endpoints`

---

### `scouting.multicast.address`

| Property | Value |
|---|---|
| **Path** | `scouting.multicast.address` |
| **Type** | String (`IP:port`) |
| **Default** | `"224.0.0.224:7446"` |

**What it controls:** The UDP multicast group address and port used for scouting traffic.

**When to change:** Change when:
- `224.0.0.224` conflicts with another application on the network
- Your network policy restricts which multicast groups are allowed
- You want to isolate separate zenoh networks on the same L2 segment (use different addresses per network)

---

### `scouting.multicast.interface`

| Property | Value |
|---|---|
| **Path** | `scouting.multicast.interface` |
| **Type** | String |
| **Default** | `"auto"` |

**What it controls:** The network interface to use for multicast scouting. `"auto"` lets zenoh select the best available interface automatically.

**When to change:** Specify explicitly (e.g., `"eth0"`, `"wlan0"`) when:
- The host has multiple interfaces and you want scouting on a specific one
- `auto` selects the wrong interface (e.g., selects loopback or VPN adapter)

---

### `scouting.multicast.ttl`

| Property | Value |
|---|---|
| **Path** | `scouting.multicast.ttl` |
| **Type** | Integer (1–255) |
| **Default** | `1` |

**What it controls:** IP Time-to-Live on multicast scout packets. TTL 1 limits packets to the local subnet only (packets don't cross routers).

**When to change:**
- Increase (e.g., `4`) only if you want multicast scouting to span multiple hops (requires network infrastructure support for multicast routing, which is rare)
- Keep at `1` for security (prevents scouting traffic from leaking beyond the local segment)

**Tradeoffs:**
- `1`: Secure, local-only scouting
- `>1`: Cross-subnet scouting (complex, rarely needed; use gossip instead for multi-hop)

---

### `scouting.multicast.autoconnect`

| Property | Value |
|---|---|
| **Path** | `scouting.multicast.autoconnect` |
| **Type** | Array of strings, or mode-dependent object |
| **Default** | `{ router: [], peer: ["router", "peer"], client: ["router"] }` |
| **Valid values** | Subset of `["router", "peer", "client"]` |

**What it controls:** Which types of discovered zenoh nodes this node automatically establishes a session with upon multicast discovery.

| Default behavior | |
|---|---|
| Router | Does not autoconnect to anything via multicast (routers are usually explicitly connected) |
| Peer | Autoconnects to discovered routers and peers |
| Client | Autoconnects only to discovered routers |

**When to change:**
- Set `peer: []` to disable automatic peer-to-peer connections and force all traffic through routers
- Set `router: ["router"]` to allow router-to-router connections via multicast (unusual)
- Add `"client"` to allow connections to discovered clients (generally not recommended)

---

### `scouting.multicast.autoconnect_strategy`

| Property | Value |
|---|---|
| **Path** | `scouting.multicast.autoconnect_strategy` |
| **Type** | String enum or mode/target-dependent object |
| **Default** | `{ peer: { to_router: "always", to_peer: "always" } }` |
| **Valid values** | `"always"`, `"greater-zid"` |

**What it controls:** Strategy to avoid redundant bidirectional connections when two nodes discover each other simultaneously.

| Strategy | Behavior |
|---|---|
| `"always"` | Both nodes attempt to connect; zenoh deduplicates the resulting sessions |
| `"greater-zid"` | Only the node with the numerically greater ZID initiates; prevents redundant connections |

**When to change:** Use `"greater-zid"` in dense peer networks to halve the number of simultaneous connection attempts. Do **not** use `"greater-zid"` if one side is behind NAT (it may not be reachable).

---

### `scouting.multicast.listen`

| Property | Value |
|---|---|
| **Path** | `scouting.multicast.listen` |
| **Type** | Boolean or mode-dependent |
| **Default** | `true` for router and peer; `false` for client |

**What it controls:** Whether this node listens for incoming scout messages on the multicast group and replies with its own locator information.

**When to change:** Set to `false` to make a node "invisible" to multicast scouting while still being able to initiate scouting itself.

---

## Gossip Scouting {#gossip-scouting}

Gossip propagates discovery information over already-established sessions. Clients do not participate in gossip.

### `scouting.gossip.enabled`

| Property | Value |
|---|---|
| **Path** | `scouting.gossip.enabled` |
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** Enables gossip-based discovery. When enabled, nodes share topology information (who else they know about) with their direct connections, propagating discovery beyond the local L2 segment.

**When to change:** Disable when:
- All topology is statically configured
- You want to minimize control-plane overhead in very constrained environments

---

### `scouting.gossip.multihop`

| Property | Value |
|---|---|
| **Path** | `scouting.gossip.multihop` |
| **Type** | Boolean |
| **Default** | `false` |

**What it controls:** When `true`, gossip information is propagated through multiple hops, eventually reaching all nodes in the subsystem even without direct connectivity between all pairs. When `false`, gossip only goes one hop (direct neighbors).

**When to change:** Enable when using `linkstate` routing mode, where not all nodes have direct connections. Required for full topology discovery in a multi-hop linkstate network.

**Tradeoffs:**
- `false`: Lower gossip traffic, scales better; but discovery limited to direct neighbors
- `true`: Complete topology discovery; more traffic; lower scalability in large networks

---

### `scouting.gossip.target`

| Property | Value |
|---|---|
| **Path** | `scouting.gossip.target` |
| **Type** | Array or mode-dependent object |
| **Default** | `{ router: ["router", "peer"], peer: ["router", "peer"] }` |

**What it controls:** Which types of nodes this node sends gossip messages to. Controls the direction of gossip propagation.

**When to change:** Restrict to reduce gossip traffic in large deployments. For example, peers in a client-only leaf network could target only `["router"]`.

---

### `scouting.gossip.autoconnect`

| Property | Value |
|---|---|
| **Path** | `scouting.gossip.autoconnect` |
| **Type** | Array or mode-dependent object |
| **Default** | `{ router: [], peer: ["router", "peer"] }` |

**What it controls:** Which discovered node types to automatically connect to based on gossip information (nodes learned about indirectly, not seen directly via multicast).

**When to change:** Same considerations as `scouting.multicast.autoconnect`. Note that clients are not included because clients don't participate in gossip.

---

### `scouting.gossip.autoconnect_strategy`

| Property | Value |
|---|---|
| **Path** | `scouting.gossip.autoconnect_strategy` |
| **Type** | String enum or mode/target-dependent object |
| **Default** | `{ peer: { to_router: "always", to_peer: "always" } }` |
| **Valid values** | `"always"`, `"greater-zid"` |

Same semantics as `scouting.multicast.autoconnect_strategy` but applied to gossip-discovered nodes.

---

## Timestamping {#timestamping}

### `timestamping.enabled`

| Property | Value |
|---|---|
| **Path** | `timestamping.enabled` |
| **Type** | Boolean or mode-dependent object |
| **Default** | `{ router: true, peer: false, client: false }` |

**What it controls:** When enabled, zenoh automatically attaches a HLC (Hybrid Logical Clock) timestamp to any data message that doesn't already have one before forwarding it.

**When to change:** Enable on peers and clients when:
- Using the storage manager plugin with replication (timestamps are required for conflict resolution)
- Your application logic needs timestamps on all messages
- You need consistent causal ordering across distributed publishers

**Tradeoffs:**
- `true`: All messages have timestamps; small overhead (timestamp attachment + HLC maintenance); required for distributed storage replication
- `false`: No overhead; messages without timestamps pass through unchanged

---

### `timestamping.drop_future_timestamp`

| Property | Value |
|---|---|
| **Path** | `timestamping.drop_future_timestamp` |
| **Type** | Boolean |
| **Default** | `false` |

**What it controls:** What happens when a message arrives with a timestamp in the future (indicates clock skew between nodes). When `false`, the timestamp is replaced with the current time (retimestamped). When `true`, the message is dropped entirely.

**When to change:** Set to `true` in security-sensitive environments where future timestamps could indicate message replay attacks or clock manipulation.

**Tradeoffs:**
- `false`: Tolerant of clock skew; all messages delivered
- `true`: Strict; messages with future timestamps lost; requires accurate NTP across all nodes

---

## Queries {#queries}

### `queries_default_timeout`

| Property | Value |
|---|---|
| **Path** | `queries_default_timeout` |
| **Type** | Integer (ms) |
| **Default** | `10000` (10 seconds) |

**What it controls:** The default timeout applied to `session.get()` queries if the application does not specify one explicitly. After this timeout, no more replies are accepted for the query.

**When to change:**
- Reduce (e.g., `2000`) for latency-sensitive query/reply applications
- Increase for queries that may trigger slow storage lookups
- Applications should generally set per-query timeouts explicitly rather than relying on this default

---

## Routing {#routing}

### `routing.router.peers_failover_brokering`

| Property | Value |
|---|---|
| **Path** | `routing.router.peers_failover_brokering` |
| **Type** | Boolean |
| **Default** | `true` |
| **Applies to** | Router mode |

**What it controls:** When `true`, a router detects if two peers connected to it are not directly connected to each other, and if so, the router will forward data between them (acting as a broker/proxy for that peer-to-peer traffic). Requires gossip discovery to be enabled with peers configured to gossip to routers.

**When to change:** Set to `false` when:
- You explicitly want to prevent the router from brokering peer-to-peer traffic
- All peers are directly connected to each other and brokering adds unnecessary overhead

**Tradeoffs:**
- `true`: Resilience—peers can communicate through the router even without direct connectivity; adds latency through the router hop
- `false`: Peers must be directly reachable; potentially lower latency for direct connections

---

### `routing.peer.mode`

| Property | Value |
|---|---|
| **Path** | `routing.peer.mode` |
| **Type** | String enum |
| **Valid Values** | `"peer_to_peer"`, `"linkstate"` |
| **Default** | `"peer_to_peer"` |
| **Applies to** | Peer mode |

**What it controls:** The routing algorithm used by peers.

| Mode | Description |
|---|---|
| `"peer_to_peer"` | Each peer only routes to nodes it is directly connected to. Simple, low overhead. |
| `"linkstate"` | Peers exchange full topology information (link-state advertisements). Enables multi-hop routing through peers without a central router. Requires gossip multihop enabled. |

**⚠️ Important:** All peers and routers in a subsystem must use the same routing mode.

**When to change:** Use `"linkstate"` when:
- You want a fully decentralized network with no routers
- Peers are not all directly connected but need to route through each other
- You require dynamic path selection based on link weights

**Tradeoffs:**
- `peer_to_peer`: Simple, scalable, low overhead; but requires direct connectivity or a router for relay
- `linkstate`: Full mesh routing without routers; more control-plane overhead; requires consistent configuration; more complex

---

### `routing.router.linkstate.transport_weights`

| Property | Value |
|---|---|
| **Path** | `routing.router.linkstate.transport_weights` |
| **Type** | Array of `{ dst_zid: string, weight: integer }` |
| **Default** | `[]` (empty; all links default to weight 100) |

**What it controls:** Assigns routing weights to outgoing links in linkstate mode. Lower weight = preferred path. If both endpoints specify weights, the greater value is used. If neither specifies, weight 100 is used.

**When to change:** Use to prefer high-bandwidth or low-latency links over expensive WAN links in linkstate topology.

**Example:**
```json5
transport_weights: [
  { dst_zid: "abcdef1234567890", weight: 10 },  // prefer this fast link
  { dst_zid: "fedcba0987654321", weight: 200 }, // avoid this expensive WAN link
]
```

The same configuration exists under `routing.peer.linkstate.transport_weights`.

---

### `routing.interests.timeout`

| Property | Value |
|---|---|
| **Path** | `routing.interests.timeout` |
| **Type** | Integer (ms) |
| **Default** | `10000` |

**What it controls:** How long a node waits for incoming interest declarations (subscriber/publisher/queryable declarations from peers) when a new session is established. Expiration before all interests are received may cause incomplete routing tables and lost messages at startup.

**When to change:**
- Increase in slow networks where session establishment takes longer
- Decrease in fast local networks where 10 seconds is excessive
- Usually does not need adjustment

---

## QoS Overwrite {#qos-overwrite}

The `qos` section provides two mechanisms to override message QoS attributes independent of what the application API sets.

### `qos.publication` — Publisher QoS Override

| Property | Value |
|---|---|
| **Path** | `qos.publication` |
| **Type** | Array of `{ key_exprs, config }` objects |
| **Default** | `[]` (disabled) |

**What it controls:** Overrides QoS for PUT and DELETE messages matching specified key expressions, applied **before** the message enters the network. This is the highest-performance override path.