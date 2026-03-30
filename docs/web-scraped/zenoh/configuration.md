# Zenoh Configuration Reference Guide

## Table of Contents

1. [Configuration File Format](#configuration-file-format)
2. [Node Identity: `id`, `mode`, `metadata`](#node-identity)
3. [Connect Configuration](#connect-configuration)
4. [Listen Configuration](#listen-configuration)
5. [Session Open Behavior](#session-open-behavior)
6. [Scouting Configuration](#scouting-configuration)
7. [Timestamping](#timestamping)
8. [Queries Default Timeout](#queries-default-timeout)
9. [Routing Configuration](#routing-configuration)
10. [QoS Configuration](#qos-configuration)
11. [Transport Configuration](#transport-configuration)
    - [Unicast Transport](#unicast-transport)
    - [Multicast Transport](#multicast-transport)
    - [Link Configuration](#link-configuration)
    - [Shared Memory](#shared-memory)
    - [Authentication](#authentication)
12. [Access Control (ACL)](#access-control)
13. [Downsampling](#downsampling)
14. [Low-Pass Filter](#low-pass-filter)
15. [Admin Space](#admin-space)
16. [Namespace](#namespace)
17. [Aggregation](#aggregation)
18. [Stats](#stats)
19. [Plugins](#plugins)
20. [Configuration Decision Guide](#configuration-decision-guide)

---

## Configuration File Format

Zenoh configuration files use **JSON5** format (`.json5`), which is a superset of JSON that allows:
- Comments (`//` and `/* */`)
- Trailing commas
- Unquoted keys
- Single-quoted strings

Files can also be written in **YAML** (`.yaml`/`.yml`) or **TOML** (`.toml`, unstable).

**Loading a config file:**
```
zenohd --config /path/to/config.json5
```

**Programmatic loading (Rust):**
```rust
let config = Config::from_file("config.json5")?;
let session = zenoh::open(config).await?;
```

**Partial key insertion at runtime:**
```rust
config.insert_json5("transport/unicast/lowlatency", "true")?;
```

> **Note:** Values shown in `DEFAULT_CONFIG.json5` are correctly typed but may not represent sensible defaults for all deployments. Many values are illustrative examples.

---

## Node Identity

### `id`

| Property | Value |
|----------|-------|
| **Type** | String (hex, lowercase, no leading zeros) |
| **Valid values** | 1–32 hex characters representing a u128 |
| **Default** | Not set (random u128 generated at startup) |

**What it controls:** The unique identifier of this zenoh node in the network. Visible to other nodes and used for routing, admin space queries (`@/<zid>/router` etc.), and session identification.

**When to change:** When you need deterministic, reproducible node identities (e.g., for persistent storage keys, fixed ACL rules referencing ZIDs, or reproducible test setups).

**Tradeoffs:**
- ✅ Enables stable admin space paths and ACL rules keyed by ZID
- ✅ Required if you want to reference a specific node in `routing.router.linkstate.transport_weights` or ACL `subjects.zids`
- ⚠️ **MUST be globally unique.** Duplicate ZIDs in the same network cause undefined routing behavior
- ⚠️ Do not reuse IDs across deployments without careful coordination

```json5
id: "1234567890abcdef"
```

---

### `mode`

| Property | Value |
|----------|-------|
| **Type** | String enum |
| **Valid values** | `"router"`, `"peer"`, `"client"` |
| **Default** | `"peer"` (in library); `"router"` in `zenohd` |

**What it controls:** The fundamental role this node plays in the zenoh network.

| Mode | Description |
|------|-------------|
| `"router"` | Dedicated infrastructure node. Forwards data between other nodes. Listens for incoming connections. Does not join peer-to-peer mesh by default. |
| `"peer"` | Full participant. Can both publish and subscribe, and routes data between directly connected peers. Forms meshes with other peers. |
| `"client"` | Lightweight endpoint. Connects to a router for all communication. Does not forward data. Cannot be connected *to* by other nodes. |

**When to change:**
- Use `"router"` for dedicated brokers/infrastructure nodes (cloud, edge hubs)
- Use `"peer"` for embedded devices or services that should form direct P2P connections
- Use `"client"` for resource-constrained devices, mobile apps, or nodes behind NAT/firewall that cannot accept incoming connections

**Tradeoffs:**

| Mode | CPU/Memory | Connectivity | Complexity |
|------|-----------|--------------|------------|
| `router` | Highest | Can reach all nodes | Requires fixed endpoints |
| `peer` | Medium | Direct P2P + router | Auto-discovery via scouting |
| `client` | Lowest | Router-dependent | Simple, no listening |

```json5
mode: "router"
```

---

### `metadata`

| Property | Value |
|----------|-------|
| **Type** | Arbitrary JSON object |
| **Valid values** | Any JSON object |
| **Default** | `{}` |

**What it controls:** Arbitrary, user-defined metadata attached to this node. Not interpreted by zenoh. Available in the admin space at `@/<zid>/router`, `@/<zid>/peer`, or `@/<zid>/client`.

**When to change:** Add identifying information for operational visibility — node names, physical location, rack/region, DNS names, hardware type, software version.

**Tradeoffs:**
- ✅ Purely informational, zero performance impact
- ✅ Useful for monitoring dashboards and topology visualization
- ⚠️ Not validated or processed by zenoh; purely a pass-through for operators

```json5
metadata: {
  name: "edge-gateway-01",
  location: "rack-3-datacenter-eu-west",
  version: "1.2.3",
}
```

---

## Connect Configuration

The `connect` section defines which remote endpoints this node should connect to at startup, and how connection failures are handled.

### `connect.endpoints`

| Property | Value |
|----------|-------|
| **Type** | Array of endpoint strings, or mode-dependent object |
| **Valid values** | List of `"<proto>/<address>"` strings |
| **Default** | `[]` (empty — rely on scouting) |

**What it controls:** The explicit list of remote zenoh nodes to connect to. Bypasses scouting discovery for these nodes.

**Supported protocols and endpoint formats:**

| Protocol | Example | Notes |
|----------|---------|-------|
| TCP | `tcp/192.168.1.10:7447` | Standard reliable transport |
| UDP | `udp/192.168.1.10:7447` | Unreliable, low overhead |
| TLS | `tls/192.168.1.10:7447` | Encrypted TCP |
| QUIC | `quic/192.168.1.10:7447` | Encrypted UDP-based |
| WebSocket | `ws/192.168.1.10:7447` | Browser/firewall traversal |
| Unix Socket | `unixsock-stream//tmp/zenoh.sock` | Local IPC |
| Unix Pipe | `unixpipe//tmp/zenoh.pipe` | Local IPC |
| vSock | `vsock/2:7447` | VM-to-hypervisor |
| Serial | `serial//dev/ttyS0#baudrate=115200` | Serial link |

**Per-endpoint options** (appended as `#key=value;key=value`):

| Option | Example | Description |
|--------|---------|-------------|
| `iface` | `#iface=eth0` | Bind to specific interface (Linux TCP/UDP) |
| `prio` | `#prio=1-3` | Assign priority range to this link |
| `rel` | `#rel=0` | Set reliability (`0`=best-effort, `1`=reliable) |
| `so_sndbuf` | `#so_sndbuf=65000` | TCP send buffer size |
| `so_rcvbuf` | `#so_rcvbuf=65000` | TCP receive buffer size |
| `bind` | `#bind=192.168.0.1:0` | Local socket address |
| `dscp` | `#dscp=0x08` | IP DSCP field value |
| `retry_period_init_ms` | `#retry_period_init_ms=5000` | Per-endpoint retry override |
| `retry_period_max_ms` | `#retry_period_max_ms=30000` | Per-endpoint retry max |

**Mode-dependent format:**
```json5
endpoints: {
  router: ["tcp/router1.example.com:7447"],
  peer:   ["tcp/10.0.0.1:7447"],
  client: ["tcp/10.0.0.1:7447"],
}
```

**When to change:** Whenever scouting is unavailable or unreliable — WAN connections, fixed infrastructure, cloud deployments, CI/CD environments, or whenever you want deterministic topology.

**Tradeoffs:**
- ✅ Predictable topology, no reliance on multicast
- ✅ Works across subnets and WAN
- ⚠️ Requires knowing endpoint addresses ahead of time
- ⚠️ No automatic failover to alternate endpoints unless multiple are listed

```json5
connect: {
  endpoints: [
    "tcp/router.example.com:7447",
    "tcp/router-backup.example.com:7447",
  ],
}
```

---

### `connect.timeout_ms`

| Property | Value |
|----------|-------|
| **Type** | Integer (ms) or mode-dependent object |
| **Valid values** | `-1` (infinite), `0` (no retry), positive integer |
| **Default** | `{ router: -1, peer: -1, client: 0 }` |

**What it controls:** How long to wait for *all* configured endpoints to be connected before proceeding. This is the total timeout for the full connect cycle, not per-endpoint.

**Semantics:**
- `-1` — Wait indefinitely (block until all endpoints connect)
- `0` — Do not retry; fail immediately if connection fails
- `N` — Wait up to N milliseconds total

**When to change:**
- Set `client: -1` if your client **must** have a router connection before it can function
- Set `client: 0` in test/dev environments where failure should be immediately visible
- Keep default `-1` for routers and peers that should keep retrying in production

**Tradeoffs:**
- `0` (no retry): Fast failure detection, good for tests; bad for resilient production systems
- `-1` (infinite): Resilient; application startup blocks until network is available
- Fixed value: Bounded startup time; may fail if infrastructure is slow

```json5
connect: {
  timeout_ms: { router: -1, peer: -1, client: 30000 },
}
```

---

### `connect.exit_on_failure`

| Property | Value |
|----------|-------|
| **Type** | Boolean or mode-dependent object |
| **Valid values** | `true`, `false` |
| **Default** | `{ router: false, peer: false, client: true }` |

**What it controls:** Whether the application exits if the connect timeout is exceeded.

**When to change:**
- Set `client: false` if your client application can function without a router connection (degraded mode)
- Set `router: true` / `peer: true` in production to force restart on connectivity loss (let systemd/k8s restart the service)

**Tradeoffs:**
- `true`: Clean failure model, integrates with process supervisors
- `false`: Application continues in a degraded state; useful for edge nodes with intermittent connectivity

---

### `connect.retry`

Controls the retry backoff behavior when connection attempts fail.

#### `connect.retry.period_init_ms`

| Property | Value |
|----------|-------|
| **Type** | Integer (ms) or mode-dependent |
| **Default** | `1000` |

Initial wait before the first retry attempt.

#### `connect.retry.period_max_ms`

| Property | Value |
|----------|-------|
| **Type** | Integer (ms) or mode-dependent |
| **Default** | `4000` |

Maximum wait between retry attempts. The backoff will not exceed this value.

#### `connect.retry.period_increase_factor`

| Property | Value |
|----------|-------|
| **Type** | Float |
| **Default** | `2.0` |

Exponential backoff multiplier. Each retry waits `previous_wait * factor`, capped at `period_max_ms`.

**Backoff sequence example (defaults):** 1s → 2s → 4s → 4s → 4s → ...

**When to change:**
- Increase `period_init_ms` and `period_max_ms` in WAN environments with slow recovery (e.g., 5s → 60s)
- Decrease both for local/LAN environments where recovery is fast
- Set `period_increase_factor: 1.0` for linear retry (constant interval)

**Tradeoffs:**
- Aggressive retry (low values): Faster reconnect, higher CPU and network load during outage
- Conservative retry (high values): Lower load, slower reconnect

```json5
connect: {
  retry: {
    period_init_ms: 2000,
    period_max_ms: 30000,
    period_increase_factor: 2.0,
  },
}
```

---

## Listen Configuration

The `listen` section configures which local endpoints this node exposes for incoming connections.

### `listen.endpoints`

| Property | Value |
|----------|-------|
| **Type** | Array of endpoint strings or mode-dependent object |
| **Valid values** | List of `"<proto>/<address>"` strings |
| **Default** | `{ router: ["tcp/[::]:7447"], peer: ["tcp/[::]:0"] }` |

**What it controls:** The local sockets/interfaces this node listens on. Other nodes can connect to these addresses.

**Key defaults:**
- Routers listen on `tcp/[::]:7447` (dual-stack IPv4+IPv6, port 7447)
- Peers listen on `tcp/[::]:0` (OS-assigned random port)
- Clients do not listen by default

**Per-endpoint options:** Same as `connect.endpoints` (`iface`, `prio`, `rel`, `so_sndbuf`, `so_rcvbuf`, `dscp`).

**When to change:**
- Restrict to specific interface: `tcp/192.168.1.0:7447#iface=eth0`
- Listen on specific port for firewall rules
- Add TLS endpoint alongside TCP: `["tcp/[::]:7447", "tls/[::]:7448"]`
- Disable listening entirely: `[]`
- Add Unix socket for local IPC: `["tcp/[::]:7447", "unixsock-stream//tmp/zenoh.sock"]`

**Tradeoffs:**
- Listening on `0.0.0.0`/`[::]` accepts connections from any interface (convenient but broad)
- Binding to specific IP limits exposure but requires static IP configuration
- Multiple listen endpoints increase connectivity options at the cost of resource usage

```json5
listen: {
  endpoints: ["tcp/[::]:7447", "tls/[::]:7448"],
}
```

---

### `listen.timeout_ms`

| Property | Value |
|----------|-------|
| **Type** | Integer (ms) or mode-dependent |
| **Valid values** | `0` (no retry), `-1` (infinite), positive integer |
| **Default** | `0` |

**What it controls:** How long to wait for all listen endpoints to successfully bind.

**Note:** Default is `0` (fail immediately if bind fails), unlike connect which defaults to `-1`.

**When to change:** Set to `-1` or a positive value in orchestrated environments where the port may be temporarily unavailable during container startup races.

---

### `listen.exit_on_failure`

| Property | Value |
|----------|-------|
| **Type** | Boolean or mode-dependent |
| **Default** | `true` |

**What it controls:** Whether to exit if listen binding fails.

**When to change:** Set `false` if you want the node to start even if some listen endpoints fail (e.g., optional TLS endpoint fails but TCP is acceptable).

---

### `listen.retry`

Same structure as `connect.retry` — controls backoff for listen bind retries.

| Parameter | Default |
|-----------|---------|
| `period_init_ms` | `1000` |
| `period_max_ms` | `4000` |
| `period_increase_factor` | `2.0` |

---

## Session Open Behavior

### `open.return_conditions.connect_scouted`

| Property | Value |
|----------|-------|
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** When `true`, `zenoh::open()` blocks until it has connected to all scouted peers/routers before returning. When `false`, `open()` returns immediately and connections are established asynchronously.

**When to change:** Set `false` for faster startup in scenarios where you accept that initial publications may be lost before connections are established.

**Tradeoffs:**
- `true`: Slower startup, but first publications after `open()` are reliably delivered to already-discovered peers
- `false`: Faster startup; early publications may be lost if subscribers haven't connected yet

---

### `open.return_conditions.declares`

| Property | Value |
|----------|-------|
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** When `true`, `zenoh::open()` waits to receive the full set of initial interest declarations from connected peers before returning. When `false`, `open()` returns without waiting.

**When to change:** Set `false` to reduce startup latency when declaration exchange overhead is acceptable or when you expect peers to re-declare interests dynamically.

**Tradeoffs:**
- `true`: All subscribers/publishers are visible immediately after `open()`; avoids extra startup traffic from peers sending declarations for already-known interests
- `false`: Faster `open()` return; may cause redundant network traffic as peers catch up

---

## Scouting Configuration

Scouting is the mechanism by which zenoh nodes discover each other. There are two mechanisms: **multicast UDP** (local network) and **gossip** (via existing connections).

### `scouting.timeout`

| Property | Value |
|----------|-------|
| **Type** | Integer (ms) |
| **Default** | `3000` |

**What it controls:** In **client mode**, the maximum time to wait for a router to be discovered via scouting before failing.

**When to change:**
- Decrease (e.g., `1000`) for faster failure detection in dev/test
- Increase (e.g., `10000`) in slow or congested networks where routers may take time to respond

---

### `scouting.delay`

| Property | Value |
|----------|-------|
| **Type** | Integer (ms) |
| **Default** | `500` |

**What it controls:** In **peer mode**, the maximum time spent scouting for remote peers before proceeding with other operations.

**When to change:**
- Decrease for faster startup when peers are already known via `connect.endpoints`
- Increase in large networks or when peer discovery is slow

---

### Multicast Scouting

#### `scouting.multicast.enabled`

| Property | Value |
|----------|-------|
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** Enables/disables UDP multicast-based node discovery on the local network.

**When to change:** Disable when:
- Running in containers/VMs where multicast is not supported
- On cloud networks (AWS, GCP, Azure) which typically don't support multicast
- When all endpoints are explicitly configured via `connect.endpoints`
- In security-sensitive environments where broadcast discovery is undesirable

**Tradeoffs:**
- `true`: Zero-config discovery on local network
- `false`: Requires explicit endpoint configuration; more predictable but less flexible

---

#### `scouting.multicast.address`

| Property | Value |
|----------|-------|
| **Type** | String (IP:port) |
| **Default** | `"224.0.0.224:7446"` |

**What it controls:** The multicast group and port used for scouting UDP messages.

**When to change:** Change if `224.0.0.224:7446` conflicts with other software on your network, or if you want to segregate zenoh deployments on the same network.

**Tradeoffs:** Must be identical on all nodes in the same scouting domain.

---

#### `scouting.multicast.interface`

| Property | Value |
|----------|-------|
| **Type** | String or `"auto"` |
| **Default** | `"auto"` |

**What it controls:** Which network interface to use for multicast scouting.

**When to change:** On hosts with multiple network interfaces (e.g., `eth0` for data, `eth1` for management), specify the correct interface explicitly to prevent scouting on the wrong network.

```json5
interface: "eth0"
```

---

#### `scouting.multicast.ttl`

| Property | Value |
|----------|-------|
| **Type** | Integer |
| **Valid values** | `1`–`255` |
| **Default** | `1` |

**What it controls:** IP Time-To-Live on multicast scouting packets. TTL=1 means packets are restricted to the local subnet (will not cross routers).

**When to change:**
- Increase only if your topology requires scouting across multiple IP subnets connected by multicast-capable routers (unusual)
- Keep at `1` for standard local network discovery

**Tradeoffs:**
- `1` (default): Safest, discovery limited to local segment
- Higher values: Risk of scouting traffic leaking across network boundaries

---

#### `scouting.multicast.autoconnect`

| Property | Value |
|----------|-------|
| **Type** | Array of WhatAmI strings, or mode-dependent object |
| **Valid values** | Lists containing `"router"`, `"peer"`, `"client"` |
| **Default** | `{ router: [], peer: ["router", "peer"], client: ["router"] }` |

**What it controls:** Which types of discovered nodes this node will automatically attempt to connect to upon multicast discovery.

**Defaults explained:**
- Routers do not auto-connect to anything via multicast (connections are manually configured or via gossip)
- Peers auto-connect to both routers and other peers
- Clients auto-connect only to routers

**When to change:**
- `peer: []` — Disable automatic peer-to-peer mesh formation; peers connect only to manually configured endpoints
- `client: ["router", "peer"]` — Allow clients to connect directly to peers (unusual but possible)
- `peer: ["router"]` — Peer only connects to routers, not other peers (router-centric topology)

**Tradeoffs:**
- More permissive autoconnect: Richer mesh, but potentially redundant connections
- More restrictive: Cleaner topology but requires manual configuration

---

#### `scouting.multicast.autoconnect_strategy`

| Property | Value |
|----------|-------|
| **Type** | String or mode/target-dependent object |
| **Valid values** | `"always"`, `"greater-zid"` |
| **Default** | `{ peer: { to_router: "always", to_peer: "always" } }` |

**What it controls:** Strategy to avoid redundant connections when multiple nodes discover each other simultaneously.

| Strategy | Behavior |
|----------|----------|
| `"always"` | Every node that discovers another will attempt to connect. May result in bidirectional connections (both are then deduplicated at transport level). |
| `"greater-zid"` | Only the node with the larger ZID initiates the connection. Prevents double-connections in symmetric peer discovery. |

**When to change:** Use `"greater-zid"` for `to_peer` when you have many peers on the same subnet and want to minimize redundant connection attempts.

**Tradeoffs:**
- `"always"`: Simpler, always connects; safe when one node may be unreachable from the other (asymmetric NAT/firewall)
- `"greater-zid"`: Halves connection attempts in symmetric topologies; may fail if the "greater" node cannot reach the "lesser" node

```json5
autoconnect_strategy: {
  peer: { to_router: "always", to_peer: "greater-zid" }
}
```

---

#### `scouting.multicast.listen`

| Property | Value |
|----------|-------|
| **Type** | Boolean or mode-dependent |
| **Default** | `{ router: true, peer: true, client: false }` |

**What it controls:** Whether this node listens for incoming scout messages on the multicast socket and replies to them (making itself discoverable).

**When to change:** Set `false` to make a node invisible to multicast scouting (it can still scout others). Useful for "shadow" monitoring nodes.

---

### Gossip Scouting

Gossip scouting propagates discovery information through existing transport connections, enabling discovery of nodes not reachable by multicast.

#### `scouting.gossip.enabled`

| Property | Value |
|----------|-------|
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** Enables gossip-based node discovery. Nodes share information about known peers/routers with their direct neighbors.

**When to change:** Disable in large, stable deployments with fully explicit configuration where gossip overhead is undesirable.

> **Note:** Clients do not participate in gossip.

---

#### `scouting.gossip.multihop`

| Property | Value |
|----------|-------|
| **Type** | Boolean |
| **Default** | `false` |

**What it controls:** When `true`, gossip information is propagated beyond the immediate next hop — spreading discovery information through the entire network. When `false`, gossip is only sent to directly connected neighbors.

**When to change:** Enable **only** when using `routing.peer.mode: "linkstate"` and the network topology has nodes that are not directly connected to each other but need to discover each other.

**Tradeoffs:**
- `false`: Lower traffic, better scalability, sufficient for most topologies
- `true`: More thorough discovery in complex multi-hop topologies; significantly more scouting traffic; reduced scalability

---

#### `scouting.gossip.target`

| Property | Value |
|----------|-------|
| **Type** | Array or mode-dependent |
| **Default** | `{ router: ["router", "peer"], peer: ["router", "peer"] }` |

**What it controls:** Which types of nodes this node sends gossip messages to.

**When to change:** Restrict to reduce gossip traffic in large networks (e.g., `peer: ["router"]` to only gossip with routers).

---

#### `scouting.gossip.autoconnect`

| Property | Value |
|----------|-------|
| **Type** | Array or mode-dependent |
| **Default** | `{ router: [], peer: ["router", "peer"] }` |

**What it controls:** Which types of nodes discovered via gossip this node will automatically connect to.

**When to change:** Same considerations as `scouting.multicast.autoconnect` but for gossip-discovered nodes.

---

#### `scouting.gossip.autoconnect_strategy`

Same options as `scouting.multicast.autoconnect_strategy` — `"always"` or `"greater-zid"`.

| Property | Value |
|----------|-------|
| **Default** | `{ peer: { to_router: "always", to_peer: "always" } }` |

---

## Timestamping

### `timestamping.enabled`

| Property | Value |
|----------|-------|
| **Type** | Boolean or mode-dependent |
| **Default** | `{ router: true, peer: false, client: false }` |

**What it controls:** When enabled, any data message received or generated that does not already have a timestamp will be assigned a timestamp (HLC — Hybrid Logical Clock) before being forwarded/stored.

**When to change:**
- Enable on peers/clients if you need timestamps for causality tracking, storage replication, or ordering guarantees without a router in the path
- Keep enabled on routers (default) for distributed storage consistency
- Required for `storage_manager` replication to work correctly

**Tradeoffs:**
- `true`: Adds a few bytes per message (timestamp metadata); ensures global ordering
- `false`: Slightly lower per-message overhead; timestamps not added (but existing timestamps are preserved and passed through)

```json5
timestamping: {
  enabled: { router: true, peer: true, client: false },
}
```

---

### `timestamping.drop_future_timestamp`

| Property | Value |
|----------|-------|
| **Type** | Boolean |
| **Default** | `false` |

**What it controls:** How to handle messages with timestamps in the future (which indicate clock skew between nodes).

- `false` (default): Messages with future timestamps are **re-timestamped** to the current time
- `true`: Messages with future timestamps are **dropped**

**When to change:** Enable `true` in strict environments where clock skew should be treated as an error and you want to protect against replayed or malformed messages.

**Tradeoffs:**
- `false`: More forgiving; handles clock skew gracefully at the cost of timestamp accuracy
- `true`: Strict; requires well-synchronized clocks (e.g., NTP/PTP); protects against replay attacks

---

## Queries Default Timeout

### `queries_default_timeout`

| Property | Value |
|----------|-------|
| **Type** | Integer (ms) |
| **Default** | `10000` (10 seconds) |

**What it controls:** The default timeout applied to `get()` queries when no explicit timeout is specified by the application.

**When to change:**
- Decrease (e.g., `1000`) for responsive UIs or health checks
- Increase (e.g., `60000`) for queries to slow queryables (database backends, remote APIs)

**Tradeoffs:**
- Short timeout: Query fails fast; may miss slow responders
- Long timeout: More complete results; application blocks longer on `get()`

```json5
queries_default_timeout: 5000
```

---

## Routing Configuration

### `routing.router.peers_failover_brokering`

| Property | Value |
|----------|-------|
| **Type** | Boolean |
| **Default** | `true` |

**What it controls:** When `true`, a router that detects two directly-connected peers that are **not** connected to each other will broker data between them (act as a relay). This provides automatic failover routing when the direct peer-to-peer link is unavailable.

**Prerequisites:** Gossip scouting must be enabled, and peers must have `gossip.target` including `"router"`.

**When to change:** Set `false` if you explicitly want to prevent the router from acting as a relay between peers (e.g., in strict security topologies where peer-to-peer isolation is required).

**Tradeoffs:**
- `true`: Resilience — data flows through router when direct P2P link is unavailable; slight router overhead
- `false`: Strict topology — peers only communicate if directly connected

---

### `routing.router.linkstate.transport_weights`

| Property | Value |
|----------|-------|
| **Type** | Array of `{ dst_zid, weight }` objects |
| **Default** | `[]` (all links weight 100) |

**What it controls:** In linkstate routing mode, assigns weights to outgoing transport links for routing cost calculations. Higher weight = less preferred path.

**Weight resolution:**
- Both endpoints specify weight → the **greater** weight wins
- Only one endpoint specifies weight → that weight is used
- Neither specifies → default weight `100`

**When to change:** In multi-hop linkstate topologies where you want to prefer certain paths (e.g., high-bandwidth fiber over slow WAN).

```json5
routing: {
  router: {
    linkstate: {
      transport_weights: [
        { dst_zid: "aabbccdd11223344", weight: 10 },   // prefer this link
        { dst_zid: "99887766554433aa", weight: 500 },  // avoid this link
      ],
    },
  },
}
```

---

### `routing.peer.mode`

| Property | Value |
|----------|-------|
| **Type** | String enum |
| **Valid values** | `"peer_to_peer"`, `"linkstate"` |
| **Default** | `"peer_to_peer"` |

**What it controls:**