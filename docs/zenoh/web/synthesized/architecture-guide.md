# Zenoh Protocol Architecture

A deep-dive reference for the zenoh protocol stack, message model, routing, storage, shared memory, security, and plugin systems. Drawn from the eclipse-zenoh RFCs, official documentation, and ZettaScale technical material.

---

## Table of Contents

- [Protocol Layers](#protocol-layers)
- [Message Types](#message-types)
  - [ZBytes and Encoding](#zbytes-and-encoding)
  - [Attachment](#attachment)
- [Key Expression System](#key-expression-system)
  - [Design](#design)
  - [Wildcards](#wildcards)
  - [Set Relations](#set-relations)
  - [WireExpr Compression](#wireexpr-compression)
- [Session Modes](#session-modes)
- [Routing](#routing)
  - [Scouting](#scouting)
  - [Interest-Based Routing](#interest-based-routing)
  - [Gossip and Mesh Routing](#gossip-and-mesh-routing)
  - [Routing Table](#routing-table)
- [Storage System](#storage-system)
  - [Architecture](#architecture)
  - [Storage Backends](#storage-backends)
  - [Timestamps and Alignment](#timestamps-and-alignment)
  - [Consolidation](#consolidation)
- [Shared Memory (SHM)](#shared-memory-shm)
  - [Overview](#overview)
  - [Buffer Types](#buffer-types)
  - [Auto-Negotiation](#auto-negotiation)
  - [Two-Layer Provider Architecture](#two-layer-provider-architecture)
  - [Allocation Policies](#allocation-policies)
  - [Robustness](#robustness)
  - [Best Practices](#best-practices)
- [Reliability and Congestion Control](#reliability-and-congestion-control)
  - [Reliability Modes](#reliability-modes)
  - [Congestion Control (Publisher-side)](#congestion-control-publisher-side)
  - [Non-Blocking Fault-Tolerant Reliability (NBFTReliability)](#non-blocking-fault-tolerant-reliability-nbftreliability)
- [Security Architecture](#security-architecture)
  - [Transport Security](#transport-security)
  - [Authentication](#authentication)
  - [Access Control (ACL)](#access-control-acl)
- [Liveliness](#liveliness)
  - [Design](#design)
  - [API](#api)
- [Plugin System](#plugin-system)
  - [Architecture](#architecture)
  - [Plugin Lifecycle](#plugin-lifecycle)
  - [Hot-loading and Hot-configuration](#hot-loading-and-hot-configuration)
  - [Bundled Plugins](#bundled-plugins)
  - [ABI Constraint](#abi-constraint)
- [Wire Efficiency](#wire-efficiency)
  - [5-Byte Minimum Overhead](#5-byte-minimum-overhead)
  - [WireExpr Compression](#wireexpr-compression)
  - [Batching](#batching)
  - [Transport Frame Structure](#transport-frame-structure)
- [Admin Space](#admin-space)
- [Sources](#sources)

## Protocol Layers

Zenoh is organized into four conceptual layers:

```
┌─────────────────────────────────────────────────────┐
│  Application Layer (API)                            │
│  Publisher / Subscriber / Queryable / Get           │
├─────────────────────────────────────────────────────┤
│  Session Layer                                      │
│  Session management, declaration, routing state     │
├─────────────────────────────────────────────────────┤
│  Transport Layer                                    │
│  Unicast / Multicast, batching, reliability         │
├─────────────────────────────────────────────────────┤
│  Link Layer                                         │
│  TCP / UDP / QUIC / TLS / SHM / Serial              │
└─────────────────────────────────────────────────────┘
```

**Link Layer**: Zenoh runs over TCP, UDP (unicast and multicast), [QUIC](quic-guide.md), TLS/mTLS, Unix sockets, Bluetooth, and serial links. Transport links carry batched zenoh frames. Multiple links between the same pair of nodes can be configured with different priorities and reliability settings (e.g., `tcp/localhost?prio=6-7;rel=0`).

**Transport Layer**: Responsible for hop-to-hop reliability, congestion control, and batching. Messages are batched into transport frames to improve throughput — this is a key reason Zenoh outperforms protocols that send one message per packet at small payload sizes.

**Session Layer**: Manages zenoh sessions (one per application instance), declaration of publishers/subscribers/queryables, interest propagation, and the mapping of Key Expressions to internal WireExpr identifiers.

**API Layer**: The programmer-facing surface: `put`, `delete`, `get`, `declare_subscriber`, `declare_publisher`, `declare_queryable`, and liveliness tokens.

---

## Message Types

Zenoh's wire protocol defines the following message categories:

| Message | Direction | Purpose |
|---|---|---|
| `Data` (Put) | Publisher → Subscribers | Publish a value on a key expression |
| `Delete` | Publisher → Subscribers | Remove a value (signals deletion to storages and subscribers) |
| `Query` | Querier → Queryables | Request data matching a key expression + selector |
| `Reply` | Queryable → Querier | Response to a Query (data, delete, or error) |
| `Declaration` | Session → Network | Declare a publisher, subscriber, queryable, or token |
| `Interest` | Router → Router | Propagate subscription interest through the routing mesh |
| `Liveliness Token` | Session → Network | Signal entity presence; detected via routing layer |
| `Scouting` | Multicast | Discover peers and routers on the local network |

### ZBytes and Encoding

As of Zenoh 1.0, the payload type is `ZBytes` — an opaque byte buffer. The associated `Encoding` field is optional metadata (IANA MIME type or user-defined string). Zenoh does not interpret payload content; encoding is passed through for application use. Known encodings may receive wire-level optimization.

### Attachment

Any operation (`put`, `delete`, query, reply) can carry an optional `Attachment` as additional metadata, also typed as `ZBytes`.

---

## Key Expression System

### Design

Zenoh's address space is a Named-Data namespace. Data is addressed by *keys* — `/`-separated sequences of UTF-8 chunks (no leading/trailing slash, no empty chunks, no `*$?#` characters). Key Expressions (KEs) are a superset of keys that address *sets* of keys.

### Wildcards

- `*` — exactly one chunk of any value (equivalent to `[^/]+`)
- `**` — zero or more chunks of any value (equivalent to `.*` across `/`-boundaries)
- `$*` — sub-chunk wildcard (equivalent to `[^/]*`); discouraged for performance reasons

**Example**:
- `sensors/*/temperature` matches `sensors/room1/temperature` but not `sensors/room1/floor2/temperature`
- `sensors/**/temperature` matches both

**Note**: Publishing a `DELETE` on `**` deletes everything — equivalent to `rm -rf /`.

### Set Relations

Two KEs can be: disjoint, intersecting, or one includes the other. Intersection determines whether a publication triggers a subscription or storage. The KE language enforces a unique canonical form — string equality implies set equality for valid KEs.

### WireExpr Compression

On the wire, KEs are declared once and subsequently referenced by a compact integer identifier (WireExpr). This reduces repeated topic-string overhead to near zero after the initial declaration, contributing to the 5-byte minimum per-message overhead.

---

## Session Modes

Zenoh nodes operate in one of three modes:

| Mode | Description |
|---|---|
| `peer` | Connects directly to other peers; participates in gossip routing |
| `client` | Connects to a router; does not route for others |
| `router` | Full routing node (`zenohd`); can load plugins |

Peers form a mesh and gossip routing/declaration state. Clients delegate routing to their attached router. Routers form the backbone infrastructure.

---

## Routing

### Scouting

On startup, Zenoh nodes emit [scouting](scouting-guide.md) messages via UDP multicast on the local network. Peers and routers respond, enabling automatic neighbor discovery without configuration. Scouting is configurable — multicast can be disabled and explicit endpoints provided.

### Interest-Based Routing

Zenoh does not forward publications unless there is a known subscriber interest. Routers propagate `Interest` messages through the mesh when a subscriber is declared. This prevents unnecessary traffic and is the primary mechanism by which Zenoh reduces discovery overhead compared to DDS (which floods all entity metadata to all participants).

**Discovery traffic comparison** (ROS 2 TurtleBot SLAM scenario):
- DDS: 251,576 bytes (686 packets, avg 367 bytes each)
- Zenoh: 3,710 bytes (99.7% reduction with key expression generalization)

### Gossip and Mesh Routing

In peer mode, Zenoh uses a gossip protocol to propagate topology and subscription information. Unlike DDS (which forms a clique — every node talks to every other directly), Zenoh routes over arbitrary mesh topologies. This enables internet-scale deployments where nodes are not all mutually reachable.

### Routing Table

Each router/peer maintains a routing table mapping KE → set of outbound faces (links to other nodes). When a publication arrives, it is forwarded to all faces with matching interest. The routing table is updated incrementally as subscribers and publishers are declared and undeclared.

---

## Storage System

### Architecture

Zenoh's [storage system](plugin-storage-manager-guide.md) is implemented as the `storage_manager` plugin (bundled with `zenohd`). Storages subscribe to a configured key expression and persist received data. [Queryables](queryable-complete-guide.md) can then answer `get` requests from that stored data.

```
Publisher --put--> zenoh network ---> Storage (subscribes to KE)
                                         |
Querier   --get--> zenoh network <-------+ (queryable answers)
```

### Storage Backends

Storage backends are pluggable. Available backends:
- `zenoh-backend-filesystem` — files on disk
- `zenoh-backend-rocksdb` — RocksDB key-value store
- `zenoh-backend-influxdb` — InfluxDB time-series
- `zenoh-backend-s3` — AWS S3 / compatible object storage
- Custom backends via the backend trait

### Timestamps and Alignment

Storages require timestamped samples for alignment (replication across multiple storage nodes). The `timestamping` configuration option must be enabled on the node loading the storage. Timestamps are generated from a `Session` and inherit the `ZenohID` of that session.

Note: In Zenoh 1.0, client and peer nodes can load storage plugins, but their default configuration disables timestamping — this must be explicitly enabled.

### Consolidation

When a `get` query matches multiple storage nodes, Zenoh supports three consolidation modes to deduplicate responses:

- **None**: Every reply from every queryable is forwarded to the querier.
- **Monotonic**: Forward a sample immediately if its timestamp is newer than any previously seen for that key. Low latency, may receive multiple samples per key.
- **Latest**: Hold all replies until all queryables have answered; deliver only the sample with the highest timestamp per key. Strongest guarantee, highest latency and memory use.
- **Auto** (default): Resolves to `Latest` unless the selector contains a `_time` argument (time-series query), in which case `None` is used.

---

## Shared Memory (SHM)

### Overview

Zenoh's SHM provides zero-copy data transfer between processes on the same host. The mechanism is transparent: a publisher allocates an `SHM buffer`, wraps it in `ZBytes`, and calls `put` normally. SHM-aware subscribers on the same host receive a handle to the same memory region with no copy. For remote subscribers or non-SHM-aware subscribers, Zenoh automatically copies the buffer at the SHM domain boundary.

### Buffer Types

- `ZShmMut` — mutable SHM buffer (allocated by publisher)
- `ZShm` — immutable handle (distributed to subscribers)
- Both wrap transparently into `ZBytes` for API compatibility

### Auto-Negotiation

SHM support is negotiated during the Zenoh session handshake. Each node declares its SHM capabilities and protocol version. Mutual SHM availability is verified. If a link partner does not support SHM, Zenoh falls back to standard serialization transparently.

### Two-Layer Provider Architecture

```
Application
    │
    ▼
ShmProvider  (high-level API: allocation policies, GC, reference counting)
    │
    ▼
ShmProviderBackend  (pluggable: POSIX shm_open/mmap, custom OS API, hugepages)
```

The default backend is `PosixShmProviderBackend` using POSIX shared memory. Custom backends can be implemented for vendor-specific memory (e.g., GPU memory, FPGA memory, DMA buffers).

### Allocation Policies

Providers support multiple allocation strategies when the SHM segment is full:
- Block (wait for space)
- Defragment (coalesce free chunks)
- Garbage collect (reclaim lost buffer references)
- Return error immediately

### Robustness

- Each provider independently manages its own SHM segments — no global contention.
- Lost buffer references (process crash, transport loss, reconnect) are garbage-collected automatically. Worst-case reclamation delay: 100 ms.
- SHM buffers are reference-counted. A buffer survives until all references across the zenoh network are dropped.

### Best Practices

- Optimal provider capacity: ~2x the sum of in-flight payload sizes.
- Use `Reliable` reliability for SHM publications.
- Avoid `Block` congestion control under heavy congestion — publishers can stall and buffers may be GC'd in-flight.

---

## Reliability and Congestion Control

Zenoh implements hop-to-hop reliability rather than end-to-end per reader-writer pair (unlike DDS RELIABLE which is per reader-writer). This design choice keeps scalability bounded — publisher state is independent of subscriber count.

### Reliability Modes

- `BestEffort` — no delivery guarantee; messages may be dropped under congestion
- `Reliable` — hop-to-hop reliability; no samples dropped in stable conditions

### Congestion Control (Publisher-side)

- `Drop` — discard messages when network buffers are full (default; avoids deadlock)
- `Block` — apply backpressure to publisher until space is available

The publisher's congestion control setting takes precedence. A subscriber requesting `Reliable` delivery may still lose messages if the publisher uses `Drop` under extreme congestion. This prevents a single slow subscriber from degrading throughput for all subscribers on a topic.

### Non-Blocking Fault-Tolerant Reliability (NBFTReliability)

An advanced reliability mode available via `zenoh-ext`. Provides end-to-end reliability across topology changes (router crashes, redeployments) without requiring O(n*m) state for n publishers and m subscribers:

- Publishers attach `SourceInfo` (source_id + sequence number) to samples
- An `AdvancedPublisher` (from `zenoh-ext`) maintains a local cache of recent samples (`AdvancedCache` via `CacheConfig`)
- Subscribers detect sequence gaps and query the cache for missed samples
- No extra control messages (heartbeats, acks) are needed in stable operation

---

## Security Architecture

### Transport Security

Zenoh supports [TLS and mTLS](encryption-guide.md) (mutual TLS) on TCP and QUIC links. Configuration is per-listener or per-connect endpoint.

### Authentication

- **Username/password**: Configured in the session `credentials` block.
- **TLS client certificates**: Used for mTLS-based identity.

### Access Control (ACL)

Zenoh 1.0 includes a built-in [ACL](acl-guide.md) engine configured in `config.json5`. The ACL evaluates rules on every message at ingress and egress.

**Config structure**:
```json5
access_control: {
  enabled: true,
  default_permission: "deny",
  rules: [
    {
      id: "allow sensors",
      messages: ["put", "delete", "declare_subscriber"],
      flows: ["ingress", "egress"],
      permission: "allow",
      key_exprs: ["sensors/**"],
    }
  ],
  subjects: [
    { id: "internal", interfaces: ["lo0", "lo"] },
    { id: "app1", usernames: ["app1_user"] },
  ],
  policies: [
    { rules: ["allow sensors"], subjects: ["internal", "app1"] }
  ]
}
```

**Supported message types for ACL**: `put`, `delete`, `declare_subscriber`, `query`, `reply`, `declare_queryable`, `liveliness_token`, `declare_liveliness_subscriber`, `liveliness_query`.

**Evaluation order**: Explicit rules take precedence over `default_permission`. Rules are matched by subject (interface or username), message type, flow direction, and key expression.

---

## Liveliness

Zenoh provides a built-in mechanism for entity presence detection without polling or heartbeat floods.

### Design

Any session can declare one or more `LivelinessToken` on a key expression. The token is visible as "alive" to any other session that subscribes to that key expression, for as long as:
- The token has not been explicitly undeclared or dropped
- The declaring session is alive and connected
- Network connectivity exists between the declaring and monitoring sessions

In a network partition, sessions that lose connectivity see the token as "dropped."

### API

```rust
// Declare a liveliness token
let token = session.liveliness()
    .declare_token("group1/member1")
    .await.unwrap();

// Subscribe to liveliness changes
let _subscriber = session.liveliness()
    .declare_subscriber("group1/**")
    .callback(|sample| { /* appeared or disappeared */ })
    .await.unwrap();
```

Liveliness is implemented in the routing layer, piggybacking on existing transport session state — no periodic heartbeats are needed in stable conditions.

---

## Plugin System

### Architecture

`zenohd` (the reference router daemon) supports dynamically loaded plugins via Rust shared libraries (`.so`/`.dylib`/`.dll`). Plugins share the host's Zenoh session internals — communications between co-located plugins happen entirely in RAM.

### Plugin Lifecycle

1. `zenohd` reads the configuration and lists named plugins
2. For each plugin, loads the shared library and calls `load_plugin` (via `declare_plugin!` macro)
3. Plugin's `start` method receives the `runtime` and spins up background tasks
4. Plugin returns a `RunningPlugin` handle — used for config change notifications and adminspace queries
5. When plugin config is deleted, `RunningPlugin` is dropped → plugin cleans up

### Hot-loading and Hot-configuration

- **Hot-loading**: Plugins are loaded when their configuration appears and dropped when it disappears — no `zenohd` restart required.
- **Hot-configuration**: Plugins receive validation callbacks before configuration changes are applied; they can accept, reject, or transform the new config.

### Bundled Plugins

`zenohd` statically links two plugins by default:

| Plugin | Purpose |
|---|---|
| `storage_manager` | Subscribe to KEs and persist data; enable queryable storage |
| `rest` | Expose zenoh pub/sub/query over HTTP REST API |

Additional plugins (`zenoh-plugin-ros2dds`, `zenoh-plugin-mqtt`, `zenoh-plugin-dds`, etc.) are maintained in separate repositories and loaded dynamically.

### ABI Constraint

Plugins must be compiled with the same Rust compiler version and the same `zenoh` dependency version and feature set as the `zenohd` they are loaded into. Rust's ABI is unstable; mismatches cause undefined behavior.

---

## Wire Efficiency

### 5-Byte Minimum Overhead

Zenoh's minimum per-message wire overhead is 5 bytes. This is the smallest of any protocol in its class:

| Protocol | Min wire overhead (data publish) |
|---|---|
| Zenoh | 5 bytes |
| XRCE-DDS | +75% vs. Zenoh |
| MQTT | +64% vs. Zenoh |
| OPC-UA | +98% vs. Zenoh |

### WireExpr Compression

KE strings are declared once per session. Subsequent messages reference the KE by a compact integer (WireExpr). For a key like `sensors/room1/floor2/temperature/celsius`, the declaration cost is paid once; every subsequent `put` costs only the WireExpr integer bytes.

### Batching

The transport layer aggregates multiple messages into a single network packet (batch transport). This dramatically reduces per-message overhead at high publication rates and is why Zenoh can sustain 4M+ msg/s at 8-byte payloads — individual messages are not sent as individual UDP/TCP writes.

### Transport Frame Structure

Each transport frame contains:
- Frame header (compact encoding of session ID, sequence number, reliability)
- One or more zenoh messages (data, declarations, queries)
- Encoding is variable-length integer (VarInt) for all length fields

---

## Admin Space

Zenoh routers expose an internal key space under `@/<zid>/` for introspection:

- `@/<zid>/router` — router metadata (name, version, configuration)
- `@/<zid>/session/transport/unicast/<peer_zid>` — unicast transport info
- `@/<zid>/session/transport/unicast/<peer_zid>/link/<hash>` — per-link statistics
- `@/<zid>/router/subscriber/<ke>` — declared subscribers
- `@/<zid>/router/publisher/<ke>` — declared publishers

The admin space is queryable via `get` using standard zenoh APIs or the REST plugin.

---

## Sources

- [eclipse-zenoh/roadmap: Key Expressions RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Key%20Expressions.md)
- [eclipse-zenoh/roadmap: Shared Memory RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/SHM.md)
- [eclipse-zenoh/roadmap: Access Control Rules RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Access%20Control%20Rules.md)
- [eclipse-zenoh/roadmap: Liveliness RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Liveliness.md)
- [eclipse-zenoh/roadmap: Plugins RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Plugins-zenoh-plugins.md)
- [eclipse-zenoh/roadmap: Network Reliability RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Network%20Reliability.md)
- [eclipse-zenoh/roadmap: Network Consolidation RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Network%20Consolidation.md)
- [eclipse-zenoh/roadmap: Non-Blocking Fault-Tolerant Reliability RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Non-Blocking-Fault-Tolerant-Reliability.md)
- [Zenoh 1.0 Concepts Migration Guide](https://zenoh.io/docs/migration_1.0/concepts/)
- [Zenoh DEFAULT_CONFIG.json5](https://github.com/eclipse-zenoh/zenoh/blob/main/DEFAULT_CONFIG.json5)
- ZettaScale Blog: "Boosting Zenoh Performance" (2022)
- ZettaScale Blog: "ROS2 Discovery Traffic Reduction" (2021)

## See Also

- [Wire Protocol Guide](wire-protocol-guide.md) — byte-level detail on the framing and encoding described in this architecture overview
- [Node Types Guide](node-types-guide.md) — how routers, peers, and clients map onto the session and routing layers
- [Programming Model Guide](programming-model-guide.md) — the application-layer API surface that sits on top of this protocol stack
- [Scouting Guide](scouting-guide.md) — the discovery mechanism described in the Routing section
