# DDS Scalability Problems That Zenoh Solves

## Table of Contents

- [Overview](#overview)
- [Part 1: How DDS Discovery Works](#part-1-how-dds-discovery-works)
  - [SPDP: Simple Participant Discovery Protocol](#spdp-simple-participant-discovery-protocol)
  - [SEDP: Simple Endpoint Discovery Protocol](#sedp-simple-endpoint-discovery-protocol)
  - [The "Every Participant Learns Everything" Model](#the-every-participant-learns-everything-model)
- [Part 2: The N² Discovery Problem](#part-2-the-n²-discovery-problem)
  - [What N² Means in Practice](#what-n²-means-in-practice)
  - [The 150-Node Experiment: 200 Seconds to Discover](#the-150-node-experiment-200-seconds-to-discover)
  - [Network Partition Recovery: The Rediscovery Storm](#network-partition-recovery-the-rediscovery-storm)
  - [Memory: The Per-Node Discovery Database](#memory-the-per-node-discovery-database)
- [Part 3: Multicast Floods Generate O(N) Response Storms](#part-3-multicast-floods-generate-on-response-storms)
  - [The Mechanics of SPDP Multicast](#the-mechanics-of-spdp-multicast)
  - [Measured Network Impact: 2GB/s Spikes](#measured-network-impact-2gbs-spikes)
  - [Why This Is Structural, Not a Tuning Problem](#why-this-is-structural-not-a-tuning-problem)
- [Part 4: The Hub-and-Spoke Workaround and Its Limits](#part-4-the-hub-and-spoke-workaround-and-its-limits)
  - [DDS Discovery Server: The Official Workaround](#dds-discovery-server-the-official-workaround)
  - [Why 40 Seconds Is Still Unacceptable](#why-40-seconds-is-still-unacceptable)
  - [Remaining Problems with Discovery Server](#remaining-problems-with-discovery-server)
  - [Docker: The Multicast Deal-Breaker](#docker-the-multicast-deal-breaker)
- [Part 5: QoS Complexity and Silent Failures](#part-5-qos-complexity-and-silent-failures)
  - [22 QoS Policies](#22-qos-policies)
  - [Silent QoS Mismatches](#silent-qos-mismatches)
  - [Traffic Shaping Complexity](#traffic-shaping-complexity)
  - [The Implicit Requirement to Understand All 22 Policies](#the-implicit-requirement-to-understand-all-22-policies)
- [Part 6: Shared Memory — Fast but Fundamentally Limited](#part-6-shared-memory-fast-but-fundamentally-limited)
  - [Cyclone DDS + iceoryx: 3,000 → 50 GB/s](#cyclone-dds-iceoryx-3000-50-gbs)
  - [The Critical Limitation: Same-Host Only](#the-critical-limitation-same-host-only)
- [Part 7: WAN and Cloud — The Multicast Wall](#part-7-wan-and-cloud-the-multicast-wall)
  - [DDS Is Fundamentally LAN-Centric](#dds-is-fundamentally-lan-centric)
  - [The Bridge Tax](#the-bridge-tax)
- [Part 8: How Zenoh Solves Each Problem](#part-8-how-zenoh-solves-each-problem)
  - [Discovery Scaling: Linkstate Routing](#discovery-scaling-linkstate-routing)
  - [No Multicast Storms: Scout/Hello Exchange](#no-multicast-storms-scouthello-exchange)
  - [Same-Host: Zenoh SHM Transport](#same-host-zenoh-shm-transport)
  - [Simplified QoS: Three Meaningful Knobs](#simplified-qos-three-meaningful-knobs)
  - [WAN Connectivity: Native QUIC](#wan-connectivity-native-quic)
  - [Protocol Overhead](#protocol-overhead)
- [Part 9: Performance Comparison](#part-9-performance-comparison)
- [Part 10: Where DDS Still Works Well](#part-10-where-dds-still-works-well)
- [Part 11: Migration Path — zenoh-bridge-ros2dds](#part-11-migration-path-zenoh-bridge-ros2dds)
- [Summary](#summary)

## Overview

The Data Distribution Service (DDS) is a mature, standardized pub/sub middleware with decades of deployments in defense, aerospace, and industrial systems. It gained enormous new attention when ROS 2 adopted it as its default communication layer. But DDS was designed for reliable LANs with a modest number of nodes — not for fleets of 100+ robots, cloud-connected deployments, or multi-site robotics infrastructure.

This guide documents the specific, measured scalability problems in DDS and explains how Zenoh addresses each one architecturally. The performance numbers come from recorded sessions by Cyclone DDS maintainers and The Construct robotics platform.

---

## Part 1: How DDS Discovery Works

Before diagnosing the problems, it helps to understand the DDS discovery model at a protocol level.

### SPDP: Simple Participant Discovery Protocol

When a DDS application starts, it broadcasts **SPDP** (Simple Participant Discovery Protocol) announcements over UDP multicast to a well-known multicast address (default `239.255.0.1:7400`). Every other DDS participant on the network receives this multicast and responds with a direct unicast reply containing their own participant information.

The result: when participant A joins, every other participant B, C, D, ... N simultaneously learns about A, and A learns about all of them via N unicast responses. This is an O(N) response storm for every single join event.

SPDP announcements repeat on a configurable period (default 30 seconds) to handle participant loss.

### SEDP: Simple Endpoint Discovery Protocol

Once two participants know about each other (via SPDP), they exchange **SEDP** (Simple Endpoint Discovery Protocol) messages to advertise their individual publishers and subscribers. Each endpoint descriptor includes:

- Topic name and type name
- QoS policies (22 policy dimensions in the DDS spec)
- Partition memberships
- GUID (globally unique identifier)

SEDP runs over unicast between each pair of participants. The critical property: **every participant receives information about every endpoint in the system**, regardless of whether they share any topics.

In a system with N participants each publishing M topics, the SEDP exchange produces N × (N-1) × M endpoint advertisements — every pair, every endpoint.

### The "Every Participant Learns Everything" Model

This is the foundational design choice that generates DDS's scaling problems. DDS discovery is intentionally omniscient: each participant builds and maintains a complete picture of every other participant and endpoint in the domain. This was a reasonable trade-off for a 20-node control system. It becomes catastrophic for a 150-node robot fleet.

The design assumption: DDS was built for local area networks where broadcast/multicast is cheap, latency is low, and node count is bounded. The internet, WAN, and large-scale robotics deployments violate all three assumptions.

---

## Part 2: The N² Discovery Problem

### What N² Means in Practice

With N participants, DDS discovery requires:

- **N² SPDP message pairs** on the network (each participant must know about every other)
- **N² × M² SEDP message pairs** for endpoint discovery (each participant×endpoint pair must be matched)

Concrete example with a modest robot fleet:
- 100 robots, each running 50 ROS 2 topics (a typical mobile robot)
- N = 100 participants
- M = 50 endpoints per participant
- SEDP endpoint pairs: 100 × 99 × 50 × 50 = **24,750,000 endpoint pair announcements**

All of this must be exchanged before any robot can communicate with any other robot.

### The 150-Node Experiment: 200 Seconds to Discover

Cyclone DDS maintainers measured discovery time for a 150-node cluster running standard SPDP/SEDP. The result: **approximately 200 seconds** for all nodes to fully discover each other and begin communicating.

For reference, a 200-second startup delay means:
- A robot fleet takes over 3 minutes before any node can reach any other node after a restart
- Network partition recovery (nodes temporarily losing visibility) causes a full re-discovery storm
- Any rolling restart of the fleet resets the discovery clock

This is not a Cyclone DDS-specific problem — it is the DDS standard's design. Other DDS implementations (RTI Connext, eProsima Fast DDS) exhibit the same behavior.

### Network Partition Recovery: The Rediscovery Storm

The discovery problem doesn't only occur at startup. When a network partition heals — whether from a WiFi dropout, a network switch reboot, or a temporary link failure — all nodes that lost visibility simultaneously attempt to rediscover each other. This produces a **synchronized discovery storm**: hundreds of nodes each sending multicast SPDP announcements at roughly the same moment, flooding the network.

The result is often worse than the initial startup: the network is already under load from application traffic, and the burst of discovery traffic degrades application performance exactly when recovery is most needed.

### Memory: The Per-Node Discovery Database

Each DDS participant must maintain an in-memory database of every other participant and endpoint. For 150 nodes with 50 topics each, this means:
- 149 remote participant records
- 7,450 remote endpoint records
- Per-endpoint QoS state (22 QoS dimensions × 7,450 endpoints)

This is not merely memory overhead — it is CPU overhead too. Every network change triggers database updates across all N participants simultaneously.

---

## Part 3: Multicast Floods Generate O(N) Response Storms

### The Mechanics of SPDP Multicast

When a new robot joins a fleet, it sends a single UDP multicast SPDP announcement. Every other participant on the network receives this multicast. Per the DDS specification, each recipient responds with a direct unicast reply.

The result: joining a 100-robot fleet immediately triggers **100 simultaneous unicast responses** flooding back to the joiner.

### Measured Network Impact: 2GB/s Spikes

The Construct, a robotics education and infrastructure platform, documented this behavior in production. When a new node joined their ROS 2 cluster, they observed **network traffic spikes of ~2 GB/s** on the joining node's interface. This is sustained for seconds while all participants complete their unicast exchanges.

For a robot with a standard WiFi or even a gigabit Ethernet connection, a 2 GB/s multicast response storm is devastating. For embedded systems with 100 Mbps links (common in robotics), it saturates the link entirely.

### Why This Is Structural, Not a Tuning Problem

A natural reaction is to tune SPDP parameters: reduce announcement frequency, increase response jitter, adjust multicast TTL. These help at the margins but do not change the fundamental O(N) response-to-join relationship. The problem is structural: the DDS standard requires every participant to respond to SPDP announcements. No amount of tuning eliminates the O(N) unicast flood on join.

The only configuration change that reduces this is restricting DDS to localhost-only traffic (`ROS_LOCALHOST_ONLY=1`), which eliminates network discovery entirely — but also eliminates all multi-host communication, defeating the purpose of a networked robot fleet.

---

## Part 4: The Hub-and-Spoke Workaround and Its Limits

### DDS Discovery Server: The Official Workaround

Both RTI Connext and eProsima Fast DDS offer a "Discovery Server" mode that replaces multicast SPDP with a centralized server. Instead of broadcasting to all peers, each participant registers with a discovery server. The server maintains the participant database and answers queries.

This reduces SPDP from O(N²) multicast traffic to O(N) unicast registrations. The Cyclone DDS experiment showed this improved discovery from **200 seconds to ~40 seconds** for 150 nodes.

### Why 40 Seconds Is Still Unacceptable

A 40-second discovery time after a network event is still catastrophic for real-time systems:
- Emergency stop propagation relies on fast network recovery
- Human-robot interaction requires responsiveness within milliseconds, not tens of seconds
- Autonomous navigation systems cannot afford 40-second blind spots after WiFi dropouts

The improvement is 5x but the baseline was so bad that 5x improvement still leaves the system non-functional for production robotics.

### Remaining Problems with Discovery Server

Even with a discovery server, DDS still sends **every endpoint to every participant**. The server reduces the announcement mechanism overhead, but does not filter what information each participant receives. A participant working only with robot arm topics still receives full endpoint information for all 50 topics on every other robot.

Additional concerns:
- **Single point of failure**: A discovery server crash means all participants lose visibility of new joiners. Multi-server setups add complexity without eliminating the SPOF concern for the transition period.
- **Operational complexity**: Every participant must be configured with the discovery server's address. In dynamic fleets where robots enter and exit, this requires either static configuration (inflexible) or its own service discovery mechanism (recursive problem).
- **WAN blindness**: Discovery servers only address LAN discovery. They do nothing for multi-site deployments, cloud connectivity, or cross-NAT communication.

### Docker: The Multicast Deal-Breaker

DDS's reliance on UDP multicast creates immediate problems in containerized deployments. Docker does not support UDP multicast between a container and its host by default. As the zenoh-bridge-dds README documents, the only known workaround is `--net host`, which is **only supported on Linux hosts**. This immediately blocks DDS deployments on macOS Docker (common in development) and Windows Docker entirely.

This is not a Docker limitation that will be fixed — it reflects a fundamental mismatch between DDS's multicast model and container network isolation.

---

## Part 5: QoS Complexity and Silent Failures

### 22 QoS Policies

DDS defines 22 Quality of Service policies, including RELIABILITY, DURABILITY, DEADLINE, HISTORY, LATENCY_BUDGET, OWNERSHIP, LIFESPAN, TRANSPORT_PRIORITY, and more. Publishers and subscribers each configure their own QoS independently.

### Silent QoS Mismatches

DDS QoS compatibility is checked at discovery time. If a subscriber requests QoS that is "incompatible" with what a publisher offers, the match simply does not occur. No error is raised. No warning is logged. The subscriber receives no data and is given no indication why.

A common failure pattern in ROS 2 deployments:
1. Publisher is configured with `RELIABILITY=BEST_EFFORT` (publish and forget)
2. Subscriber is configured with `RELIABILITY=RELIABLE` (requires delivery guarantee)
3. Per DDS spec, the subscriber's request is "stronger" than what the publisher offers — mismatch
4. No connection is established, no data flows
5. Developer spends hours debugging before discovering the QoS mismatch

This happens regularly in ROS 2 because different packages use different default QoS profiles, and the defaults are not consistent across the ecosystem.

### Traffic Shaping Complexity

The Cyclone DDS session on QoS for production deployments (YouTube: `l-qrKTPcEt0`) covers the additional complexity of traffic shaping in a DDS network:

- **DEADLINE QoS**: publisher and subscriber specify deadlines independently. Mismatch produces a silent failure.
- **LIFESPAN QoS**: data has an expiration time. If processing is slow, data silently expires before delivery.
- **Multicast burst reduction**: a common production tuning exercise is reducing SPDP announcement rates and adding jitter to avoid synchronized bursts — but this trades recovery speed for stability.
- **Publisher stall under RELIABLE**: when a RELIABLE publisher's internal queue fills because a subscriber is slow, the publisher blocks. This can cascade across unrelated topics sharing the same participant.

### The Implicit Requirement to Understand All 22 Policies

Production-grade DDS deployment requires deep understanding of QoS interactions. Teams that get it wrong silently lose data or connectivity. The complexity is not just operator burden — it's a source of hard-to-reproduce bugs where "everything looks connected but no data flows."

---

## Part 6: Shared Memory — Fast but Fundamentally Limited

### Cyclone DDS + iceoryx: 3,000 → 50 GB/s

The Cyclone DDS shared memory session (YouTube: `5GpROveP6Hg`) demonstrated a remarkable result: enabling the iceoryx PSMX plugin (Physical Shared Memory eXchange) improves throughput from ~3,000 messages/second to an effective **~50 GB/s** for same-host publishers and subscribers.

This works by placing message data in shared memory pages directly accessible by both publisher and subscriber. No serialization, no network stack, no kernel crossing for the data path. The result is genuine zero-copy delivery between processes on the same machine.

### The Critical Limitation: Same-Host Only

Shared memory operates at the process level. For subscribers on a different host, DDS falls back to its standard UDP transport path. The shared memory optimization is invisible from the network — remote participants still discover the endpoint via SPDP/SEDP, still establish the SEDP-driven unicast connections, and still receive data via the standard DDS wire protocol.

The implication: even if every robot in a fleet uses SHM internally, the **fleet-level scaling problems remain entirely unaddressed**. The N² discovery problem, the multicast join storm, and the QoS complexity all operate at the network layer, which SHM does not touch.

The iceoryx integration also introduces operational complexity:
- The `iox-roudi` daemon must be running before any SHM-enabled participant starts
- SHM is not supported on Windows
- Only "memcpy-safe" data types (no pointer indirections) can use SHM in the DDS bridge forward discovery mode

DDS SHM demonstrates that DDS can be made very fast in controlled same-host scenarios. It does not demonstrate that DDS scales to multi-host fleets — those remain separate, unsolved problems.

---

## Part 7: WAN and Cloud — The Multicast Wall

### DDS Is Fundamentally LAN-Centric

UDP multicast does not cross NAT boundaries, does not traverse firewalls by default, and does not route between subnets without explicit multicast routing configuration (PIM, IGMP snooping, etc.). These are not configuration oversights — they reflect that IP multicast was designed for enterprise LANs, not the internet.

This means DDS-based ROS 2 systems cannot natively:
- Connect robots in different buildings
- Bridge to cloud monitoring infrastructure
- Communicate across VPN boundaries without additional configuration
- Support remote robot operation without a VPN or dedicated bridge

### The Bridge Tax

The standard workaround is deploying a DDS bridge at each boundary — a dedicated host that has both LAN and WAN connectivity, runs a DDS participant on the LAN side, and forwards traffic to the remote site via TCP or custom protocol.

This is what the `zenoh-bridge-dds` and `zenoh-bridge-ros2dds` plugins are: they translate DDS multicast discovery into Zenoh's network-capable protocol. But deploying these bridges adds:
- Additional infrastructure to manage
- Additional failure points
- Complexity in routing rules (which topics cross the bridge)
- Latency from the bridge hop

The need for bridges is itself an indicator that DDS's network model is not well-suited to the deployment patterns that modern robotics requires.

## See Also

- [Plugin DDS Bridge Guide](plugin-dds-bridge-guide.md) — the `zenoh-bridge-dds` and `zenoh-bridge-ros2dds` plugins that solve the problems documented here
- [ROS2 Migration Guide](ros2-migration-guide.md) — step-by-step migration from DDS/ROS2 to Zenoh
- [Comparison Guide](comparison-guide.md) — quantitative comparison of Zenoh vs DDS, MQTT, and Kafka
- [Wire Protocol Guide](wire-protocol-guide.md) — how Zenoh's wire protocol achieves the lower overhead compared to RTPS

---

## Part 8: How Zenoh Solves Each Problem

### Discovery Scaling: Linkstate Routing

Zenoh routers use a **linkstate routing** protocol to propagate topology information. For full scouting configuration, see the [scouting guide](scouting-guide.md). When a new peer or router joins, the change propagates through the router network incrementally — each router informs its neighbors, which inform their neighbors, until all routers have converged.

Critically, this propagation is O(N log N) in practice, not O(N²). Each router only needs to know the full topology, not a flat list of all endpoint pairs. Subscriptions are propagated similarly: a subscriber announcement reaches only the routers that need to know, not every participant in the system.

The practical result: a Zenoh network of 150 nodes does not produce a 200-second discovery phase. Router convergence for a well-connected graph of 150 routers completes in under a second. Clients connecting to routers receive only the routing table entry for their subscription, not the full N² endpoint matrix.

### No Multicast Storms: Scout/Hello Exchange

Zenoh's equivalent of SPDP is the **scouting protocol**: a peer sends a `Scout` message (optionally multicast), and Zenoh entities that choose to reply send `Hello` responses. Crucially:

1. Scouting is optional. In most production deployments, Zenoh routers are configured with explicit peer addresses (`-e tcp/host:7447`), making scouting unnecessary.
2. Router mode (the default for `zenoh-bridge-ros2dds` v0.11+) does not auto-connect on discovery — it listens for incoming connections, preventing spontaneous mesh formation.
3. Once connected, topology changes propagate via linkstate gossip, not via re-announcement to all participants simultaneously.

The join-a-fleet scenario: a new `zenoh-bridge-ros2dds` connects to one existing router. That router propagates the new node's subscription interest via linkstate. The new node does not receive N unicast floods. The rest of the network receives one incremental topology update.

### Same-Host: Zenoh SHM Transport

Zenoh has its own shared memory transport that operates when publisher and subscriber are on the same host. Unlike DDS SHM, Zenoh SHM integrates with the Zenoh API transparently — no iceoryx daemon required, no separate PSMX configuration.

Zenoh same-host latency with SHM: approximately 12µs for small messages. Comparable to Cyclone DDS with iceoryx (~8µs) for same-host scenarios, while retaining full network transport capability.

### Simplified QoS: Three Meaningful Knobs

Zenoh [QoS](qos-guide.md) reduces to three operationally significant dimensions:

- **Priority**: 7 levels (RealTime, Interactive High/Low, Data High/Low/Background, Background)
- **Reliability**: 2 options (Reliable, BestEffort)
- **Congestion Control**: 3 options (Block, Drop, BlockOnFull)

There are no silent compatibility failures. A Zenoh subscriber with Reliable mode receives reliable delivery; a subscriber with BestEffort accepts whatever the publisher sends. There is no "compatibility matrix" to consult, no silent non-match.

For ROS 2 users migrating from DDS, `zenoh-bridge-ros2dds` translates DDS QoS to Zenoh QoS on the bridge boundary, preserving ROS 2 QoS semantics while the inter-bridge network uses Zenoh's simpler model.

### WAN Connectivity: Native QUIC

Zenoh supports QUIC as a first-class transport. QUIC:
- Traverses NAT with connection initiation from the NATed side
- Multiplexes streams over a single UDP flow (no connection-per-topic overhead)
- Provides built-in TLS 1.3 encryption
- Handles packet reordering without head-of-line blocking

A `zenoh-bridge-ros2dds` at a remote site can connect directly to a Zenoh router via QUIC over the internet, without VPN or dedicated bridge infrastructure. The DDS network on each side remains LAN-local; the inter-site link is QUIC.

This is not a workaround — it is how Zenoh was designed. The protocol was built from the beginning for multi-hop, heterogeneous network topologies.

### Protocol Overhead

DDS uses the RTPS (Real-Time Publish Subscribe) wire format. A minimal RTPS data submessage with header is approximately **80–120 bytes** of overhead regardless of payload size. For small control messages (common in robotics), this overhead is significant relative to payload.

Zenoh wire protocol overhead: **4–6 bytes** for small messages (topic key + flags). The encoding uses variable-length integers and minimizes fixed overhead. For a 12-byte sensor reading, the difference between 120-byte DDS overhead and 6-byte Zenoh overhead is a 10× efficiency gain on the wire.

---

## Part 9: Performance Comparison

| Metric | DDS (CycloneDDS) | Zenoh |
|--------|-----------------|-------|
| Discovery: 150 nodes, no workaround | ~200 seconds | <1 second |
| Discovery: 150 nodes, discovery server | ~40 seconds | <1 second |
| Join storm: N responses on join | N unicast floods | Incremental gossip, no storm |
| Same-host latency (SHM) | ~8 µs (iceoryx) | ~12 µs |
| Network latency (LAN) | ~50 µs | ~12 µs |
| WAN connectivity | Via bridge only | Native QUIC |
| NAT traversal | Not supported | Supported |
| Docker (non-Linux) | Not supported (multicast) | Supported |
| Protocol overhead (small msg) | ~100 bytes | 4–6 bytes |
| QoS policies | 22 | 3 operational |
| Silent QoS mismatch possible | Yes | No |
| Discovery database per participant | Full N×M endpoint matrix | Routing table only |

*Source: Cyclone DDS maintainer sessions (YouTube IDs: f4OLU2UFVEk, Twpq1l2aE7c, l-qrKTPcEt0, 5GpROveP6Hg); The Construct robotics platform.*

---

## Part 10: Where DDS Still Works Well

Fairness requires acknowledging the scenarios where DDS is well-suited:

**Small, stable, LAN-confined deployments**: A 10-node embedded control system running DDS on a dedicated VLAN with no WiFi and no cloud connectivity works fine. The N² problem is negligible at 10 nodes.

**Same-host latency with SHM**: Cyclone DDS + iceoryx achieves ~8µs same-host latency. Zenoh achieves ~12µs. DDS wins for same-host ultra-low-latency applications where network scaling is not a concern.

**Standards compliance**: DDS is an OMG standard with multiple certified implementations. For systems that require interoperability between different vendors' DDS stacks (RTI, eProsima, ADLINK), the standard is the interoperability layer. Zenoh has no equivalent cross-vendor standard (though its spec is open).

**Mature QoS semantics**: Despite the complexity cost, DDS QoS policies cover scenarios that Zenoh does not directly address (OWNERSHIP for exclusive writer, LIFESPAN for message expiry, DURABILITY for late-joining subscribers getting history). Applications that need these semantics precisely may find DDS QoS beneficial once mastered.

---

## Part 11: Migration Path — zenoh-bridge-ros2dds

The `zenoh-bridge-ros2dds` plugin enables incremental migration from DDS to Zenoh for ROS 2 systems. The architecture:

1. Run one bridge per robot (or per ROS domain)
2. Configure `ROS_LOCALHOST_ONLY=1` to confine DDS to loopback (eliminating network DDS traffic entirely)
3. The bridge discovers all local ROS nodes via DDS on loopback, then exposes them via Zenoh to the broader network

This approach:
- Eliminates inter-host DDS multicast entirely (and thus eliminates join storms)
- Maintains full compatibility with existing ROS 2 nodes (they still talk DDS internally)
- Provides the zenoh.io blog's documented improvement: "helped lot of robotic use cases to overcome some wireless connectivity, bandwidth and integration issues"
- Enables services and actions as Zenoh Queryables (more efficient than DDS RPC)
- Propagates compact discovery information between bridges rather than raw DDS SPDP/SEDP traffic

The per-robot namespace configuration (`namespace: "/bot1"`) solves fleet-level topic isolation without modifying any ROS node, because the DDS traffic between nodes on the same robot remains namespace-free.

---

## Summary

DDS was designed for a world of small, trusted, LAN-connected systems. Its discovery model — every participant learns about every endpoint via multicast — generates O(N²) scaling behavior that makes it unsuitable for large robot fleets, cloud-connected deployments, or containerized infrastructure.

The specific, measured failure modes:
1. **200-second discovery** for 150-node clusters (Cyclone DDS maintainer data)
2. **2 GB/s network spikes** on node join (The Construct measurement)
3. **Silent QoS mismatches** that prevent data flow with no error indication
4. **Docker multicast incompatibility** on all non-Linux hosts
5. **WAN opacity**: no native internet connectivity without bridge infrastructure

Zenoh addresses each of these structurally: linkstate routing replaces omniscient endpoint flooding, QUIC enables native WAN traversal, simplified QoS eliminates silent failures, and gossip-based scouting eliminates join storms. The `zenoh-bridge-ros2dds` plugin provides a migration path that keeps existing ROS 2 nodes working unchanged while eliminating DDS's network-level scaling problems.
