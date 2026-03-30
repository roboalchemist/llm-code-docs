# Zenoh Config: Routing, Aggregation & Query Timeout

Configuration reference for `routing`, `aggregation`, and `queries_default_timeout`.

---

## Table of Contents

- [Router Routing (`routing.router`)](#router-routing-routingrouter)
  - [`routing.router.peers_failover_brokering`](#routingrouterpeers_failover_brokering)
  - [`routing.router.linkstate.transport_weights`](#routingrouterlinkstatetransport_weights)
- [Peer Routing (`routing.peer`)](#peer-routing-routingpeer)
  - [`routing.peer.mode`](#routingpeermode)
  - [`routing.peer.linkstate.transport_weights`](#routingpeerlinkstatetransport_weights)
- [Interest-Based Routing (`routing.interests`)](#interest-based-routing-routinginterests)
  - [`routing.interests.timeout`](#routingintereststimeout)
- [Declaration Aggregation (`aggregation`)](#declaration-aggregation-aggregation)
  - [`aggregation.subscribers`](#aggregationsubscribers)
  - [`aggregation.publishers`](#aggregationpublishers)
- [Query Default Timeout (`queries_default_timeout`)](#query-default-timeout-queries_default_timeout)
- [Full Routing Example](#full-routing-example)
- [Source](#source)

## Router Routing (`routing.router`)

Configuration for nodes running in `router` mode.

### `routing.router.peers_failover_brokering`

**Type**: `bool`
**Default**: `true`

When enabled, a router acts as a broker for two directly connected peers that are not connected to each other. If the router detects that two of its peer clients are not directly connected, it forwards messages between them through itself.

This is the "failover brokering" behavior: if peer-to-peer direct links are unavailable, the router bridges the gap. Requires gossip discovery to be enabled (so the router can detect peer-peer connectivity).

```json5
routing: { router: { peers_failover_brokering: true } }
```

### `routing.router.linkstate.transport_weights`

**Type**: `Vec<TransportWeight>`
**Default**: `[]` (empty — all links weighted equally at 100)

Per-destination link weights for linkstate routing mode. Each entry specifies a destination node by ZID and the weight of the outgoing link to that node.

**Weight resolution rules**:
- If neither endpoint specifies a weight: effective weight = `100`
- If only one endpoint specifies a weight: the specified weight is used
- If both endpoints specify a weight: the greater weight is used

```json5
routing: {
  router: {
    linkstate: {
      transport_weights: [
        { dst_zid: "abcdef1234567890abcdef1234567890", weight: 50 },
        { dst_zid: "11223344556677889900aabbccddeeff", weight: 200 },
      ]
    }
  }
}
```

`weight` must be a non-zero `u16` value (1–65535).

---

## Peer Routing (`routing.peer`)

Configuration for nodes running in `peer` mode.

### `routing.peer.mode`

**Type**: `String`
**Default**: `"peer_to_peer"`
**Valid values**: `"peer_to_peer"` | `"linkstate"`

The routing strategy for peer nodes.

- `"peer_to_peer"` (default): Peers route messages directly to connected neighbors. No global topology awareness; works for flat meshes.
- `"linkstate"`: Peers maintain a full topology map of the network and compute optimal routes. Enables routing across non-directly-connected nodes, but requires more memory and network overhead. All nodes in the subsystem must use the same mode.

```json5
routing: { peer: { mode: "peer_to_peer" } }
```

> **Important**: `routing.peer.mode` must be set consistently across all peers and routers in a Zenoh subsystem. Mismatched modes can cause routing failures.

### `routing.peer.linkstate.transport_weights`

Same structure as `routing.router.linkstate.transport_weights`. Applies when peer mode is `"linkstate"`.

---

## Interest-Based Routing (`routing.interests`)

### `routing.interests.timeout`

**Type**: `u64` (milliseconds)
**Default**: `10000` (10 seconds)

Timeout for waiting for incoming interest declarations during session setup. Interests are declarations of subscriber/queryable intent that enable targeted routing. This applies to all modes (router, peer, client).

```json5
routing: { interests: { timeout: 10000 } }
```

---

## Declaration Aggregation (`aggregation`)

Aggregation reduces declaration traffic in large deployments by collapsing many specific key expressions into a single broader one for routing purposes.

### `aggregation.subscribers`

**Type**: `Vec<OwnedKeyExpr>`
**Default**: `[]` (no aggregation)

A list of key expressions. All subscriber declarations matching any of these expressions are aggregated into a single declaration for the aggregated expression. Reduces the number of subscriber declarations propagated through the network.

Useful when many nodes subscribe to fine-grained keys (e.g., `sensor/room1/temperature`, `sensor/room2/temperature`, …) and you want to aggregate them as `sensor/**`.

```json5
aggregation: {
  subscribers: ["sensor/**", "robot/*/status"]
}
```

### `aggregation.publishers`

**Type**: `Vec<OwnedKeyExpr>`
**Default**: `[]` (no aggregation)

Same as `aggregation.subscribers` but for publisher declarations.

```json5
aggregation: {
  publishers: ["sensor/**"]
}
```

> **Note**: Aggregation is a routing optimization. It does not affect which messages are delivered — only how routing declarations are propagated. With aggregation, some redundant routing may occur (broader declarations match more endpoints than needed).

---

## Query Default Timeout (`queries_default_timeout`)

**Type**: `u64` (milliseconds)
**Default**: `10000` (10 seconds)
**Config path**: top-level field

The default timeout for `get()` queries when no explicit timeout is specified in the query options. Queries that do not receive a reply within this window are considered complete.

```json5
queries_default_timeout: 10000
```

Override per-query at the API level:
```rust
session.get("my/key").timeout(Duration::from_secs(5)).await
```

---

## Full Routing Example

```json5
routing: {
  router: {
    peers_failover_brokering: true,
    linkstate: {
      transport_weights: [],
    },
  },
  peer: {
    mode: "peer_to_peer",
    linkstate: {
      transport_weights: [],
    },
  },
  interests: {
    timeout: 10000,
  },
},
aggregation: {
  subscribers: [],
  publishers: [],
},
queries_default_timeout: 10000,
```

---

## Source

- `repos/zenoh/commons/zenoh-config/src/lib.rs` — `RoutingConf`, `RouterRoutingConf`, `PeerRoutingConf`, `LinkstateConf`, `InterestsConf`, `AggregationConf`, `TransportWeight`
- `repos/zenoh/commons/zenoh-config/src/defaults.rs` — `routing.router.peers_failover_brokering`, `routing.peer.mode`, `routing.interests.timeout`, `queries_default_timeout`

## See Also

- [Node Types Guide](node-types-guide.md) — router and peer modes that determine which routing config fields apply
- [Scouting Guide](scouting-guide.md) — discovery mechanism that works alongside the routing configuration
- [Config Connect Listen](config-connect-listen.md) — endpoint configuration that feeds into the routing topology
