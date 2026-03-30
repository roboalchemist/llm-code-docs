# Zenoh vs. Alternatives: Protocol Comparison Guide

## Table of Contents

- [Overview](#overview)
- [Comparison Matrix](#comparison-matrix)
- [Performance Benchmarks](#performance-benchmarks)
  - [Throughput (16 KB payload, multi-machine, 100 GbE)](#throughput-16-kb-payload-multi-machine-100-gbe)
  - [Message Rate (small payloads, single machine, same hardware)](#message-rate-small-payloads-single-machine-same-hardware)
  - [Latency (multi-machine, 100 GbE, 64-byte payload, NTU 2023 study)](#latency-multi-machine-100-gbe-64-byte-payload-ntu-2023-study)
  - [Embedded: Zenoh-Pico vs. Constrained Protocols](#embedded-zenoh-pico-vs-constrained-protocols)
  - [Caveat on Benchmark Methodology](#caveat-on-benchmark-methodology)
- [Feature Comparison](#feature-comparison)
  - [vs. MQTT](#vs-mqtt)
  - [vs. DDS / CycloneDDS](#vs-dds-cyclonedds)
  - [vs. Kafka](#vs-kafka)
  - [vs. ZeroMQ](#vs-zeromq)
  - [vs. NATS](#vs-nats)
- [Use Case Recommendations](#use-case-recommendations)
- [Migration Guides](#migration-guides)
- [Sources](#sources)

## Overview

Zenoh is a Named-Data oriented protocol designed for the full Cloud-to-Things continuum — from constrained microcontrollers to distributed cloud infrastructure. Its core differentiator is that it natively supports peer-to-peer, brokered, and routed topologies within a single protocol, while delivering lower wire overhead and higher throughput than any comparable protocol in its class.

Zenoh is maintained as an Eclipse Foundation project. The reference implementation (Rust) is developed by ZettaScale Technology. A C/C++ micro-implementation, Zenoh-Pico, targets embedded and constrained devices.

---

## Comparison Matrix

| Feature | Zenoh | MQTT | DDS (CycloneDDS) | Kafka | ZeroMQ | NATS |
|---|---|---|---|---|---|---|
| Primary transport | UDP/TCP/QUIC/SHM/Multicast | TCP | UDP multicast / TCP | TCP | TCP/IPC | TCP/WS |
| P2P mode | Native | Broker required | Native | Broker required | Native | Broker required |
| Brokered mode | Optional (router) | Mandatory | Not supported | Mandatory | N/A | Mandatory |
| Routed mesh | Native (arbitrary topology) | No | No | No | Manual | No |
| Pub/sub | Yes | Yes | Yes | Yes (topics) | Yes | Yes |
| Query/reply (get) | Native (Queryable) | No (request-reply via topics) | Yes (via DDS-RPC) | No | Yes (REQ/REP) | Yes (request) |
| Geo-distributed storage | Native | No | Limited | No | No | JetStream |
| Shared memory (zero-copy) | Native, auto-negotiated | No | IceOryx (external) | No | Yes (IPC) | No |
| Embedded/MCU support | Zenoh-Pico (< 50 KB flash) | MQTT-SN (partial) | Micro-XRCE-DDS | No | No | No |
| Wire overhead (min) | **5 bytes** | 2 bytes (header) + topic | ~24 bytes (RTPS) | Variable (framing) | 1 byte | Variable |
| Language bindings | Rust, C, C++, Python, Java, Kotlin, TypeScript (Go: planned) | Wide | Wide | Wide | Wide | Wide |
| Security | TLS/mTLS + ACL | TLS + username/password | TLS/DDS-Security | TLS + SASL | CurveZMQ | TLS + user creds |
| Internet-scale routing | Native | Via bridge | No (LAN/WAN bridge) | Cluster | No | Cluster |
| ROS 2 integration | Native (rmw_zenoh, zenoh-plugin-dds) | No | Native (rmw_fastdds) | No | No | No |
| Open standard | Eclipse/OMG (in progress) | OASIS standard | OMG standard | Apache | LGPL | Apache |

---

## Performance Benchmarks

All figures from the NTU (National Taiwan University) 2023 study unless noted. Hardware: AMD Ryzen 7 5800X, 32 GB DDR4, 100 Gb Ethernet.

### Throughput (16 KB payload, multi-machine, 100 GbE)

| Protocol | Bitrate |
|---|---|
| Zenoh (peer-to-peer) | ~50 Gbps |
| Zenoh (routed via router) | ~34 Gbps |
| CycloneDDS | ~14 Gbps |
| MQTT (Mosquitto 2.0.15, QoS 0) | ~5 Gbps |
| Kafka (3.2.1) | ~5 Gbps |

**Summary**: Zenoh peer-to-peer delivers 3x the throughput of DDS and over 10x that of Kafka and MQTT at 16 KB payload. Peak measured: 67 Gbps on large payloads.

### Message Rate (small payloads, single machine, same hardware)

| Protocol | Peak msg/s (8 bytes) |
|---|---|
| Zenoh (peer-to-peer) | > 4M msg/s |
| CycloneDDS | ~2M msg/s |
| Kafka | ~53–62K msg/s |
| MQTT | ~32–38K msg/s |

At 8-byte payload: Zenoh is ~2x DDS, ~60x Kafka, ~100x MQTT in message rate.

### Latency (multi-machine, 100 GbE, 64-byte payload, NTU 2023 study)

| Protocol | Latency |
|---|---|
| Zenoh-Pico | ~13 µs |
| Zenoh (peer-to-peer) | ~16 µs |
| CycloneDDS | ~37 µs |
| Zenoh (routed) | ~41 µs |

### Embedded: Zenoh-Pico vs. Constrained Protocols

Source: ZettaScale "Zenoh-Pico Deep Dive" blog.

| Protocol | Relative throughput vs. Zenoh-Pico | Wire overhead vs. Zenoh |
|---|---|---|
| Zenoh-Pico | 1x (baseline) | 5 bytes min |
| XRCE-DDS | ~10x worse | +75% larger |
| MQTT | ~40x worse | +64% larger |
| OPC-UA | ~55x worse | +98% larger |

### Caveat on Benchmark Methodology

The NTU study used RELIABLE QoS for DDS. The Zenoh team noted this is appropriate for camera/point-cloud workloads where BEST_EFFORT is common. DDS shared memory (IceOryx) was not tested; Zenoh's own SHM was also excluded to keep the comparison at the protocol level.

---

## Feature Comparison

### vs. MQTT

**Architecture**: MQTT is a broker-centric protocol. Every message must pass through a broker (e.g., Mosquitto, EMQX). Zenoh supports both brokered (via the zenoh router) and fully peer-to-peer modes with no broker required.

**Throughput**: MQTT reaches up to ~9 Gbps on 100 GbE at 32 KB payloads but degrades significantly for larger payloads. In NTU multi-machine tests, MQTT failed for payloads larger than 64 MiB. Zenoh delivers 50+ Gbps peer-to-peer.

**Wire overhead**: MQTT has a 2-byte fixed header plus variable-length topic strings (e.g., `sensors/room1/temperature` adds 24+ bytes). Zenoh compresses key expressions using WireExpr identifiers after declaration, bringing overhead to as low as 5 bytes.

**Query/reply**: MQTT has no native request-reply. Applications typically implement it using paired topics and correlation IDs. Zenoh has a native `get`/`Queryable` mechanism.

**Embedded**: MQTT-SN is the constrained variant, but it requires a gateway. Zenoh-Pico runs natively on MCUs (ESP32, STM32) with no gateway.

**Verdict**: Zenoh is a strict superset of MQTT's feature set, with far higher performance and native P2P. MQTT remains simpler for integrators already operating MQTT brokers with existing tooling ecosystems.

---

### vs. DDS / CycloneDDS

**Architecture**: DDS (Data Distribution Service) is the OMG standard underlying ROS 2. It is a peer-to-peer protocol using RTPS (Real-Time Publish-Subscribe) over UDP multicast. DDS has no concept of a broker or router — all discovery is done via SPDP/SEDP multicast.

**Discovery overhead**: DDS discovery traffic grows quadratically — O(n*(n-1)*(r+w)) where n = participants, r = readers, w = writers. In a measured ROS 2 / TurtleBot scenario, DDS generated 251,576 bytes of discovery traffic. Zenoh generated 3,710 bytes — a 98.5% reduction. With key expression generalization, Zenoh can reduce this further to 728 bytes (99.7% reduction).

**Throughput**: CycloneDDS delivers ~14 Gbps at 16 KB on 100 GbE. Zenoh peer-to-peer delivers ~50 Gbps — 3.5x higher. On loopback, the two protocols are close in latency; Zenoh-Pico beats both.

**Latency**: Zenoh P2P: ~10 µs. CycloneDDS: ~12 µs. Both are in the same order of magnitude. Zenoh-Pico achieves 5 µs, the lowest of any tested protocol.

**Wireless / WAN**: DDS was designed for wired, high-bandwidth networks. Discovery floods wireless links. In NTU edge tests (Wi-Fi, 4G), Zenoh outperformed DDS — Zenoh's trajectory drift error was smallest in actual robot experiments on a TurtleBot 4.

**Routing**: DDS operates as a clique (every node talks to every other directly). Zenoh can route over arbitrary mesh topologies, enabling internet-scale deployments.

**ROS 2**: Zenoh provides `rmw_zenoh` as a drop-in RMW (Robot Middleware) for ROS 2, and `zenoh-plugin-dds` which transparently bridges existing DDS/ROS 2 applications over Zenoh with no application changes required.

**Verdict**: For LAN-only, high-throughput, low-node-count deployments, CycloneDDS is competitive. For wireless, WAN, large-scale, or internet-routed robot deployments, Zenoh substantially outperforms DDS in discovery overhead and connectivity robustness.

---

### vs. Kafka

**Architecture**: Kafka is a distributed log / event streaming platform. It is strongly broker-centric: all messages pass through Kafka brokers and are durably stored in partitioned logs. It is designed for high-throughput event ingestion and replay, not low-latency sensor data.

**Throughput**: Kafka achieves ~5 Gbps at 16 KB payloads — 10x lower than Zenoh peer-to-peer. In NTU testing, the Kafka bindings used failed on payloads larger than 512 KiB in multi-machine tests (larger than 1 MB in single-machine tests). Zenoh handles up to 512 MB in testing.

**Latency**: Kafka latency is in the milliseconds range when configured for durability. Zenoh latency is in the tens-of-microseconds range.

**Use model**: Kafka is optimized for durable event streaming, replay, consumer groups, and stream processing. Zenoh is optimized for real-time pub/sub, queryable storage, and low-latency data paths. Zenoh's storage plugin can implement replay-like semantics but Kafka's durability guarantees are stronger.

**Embedded/edge**: Kafka has no embedded footprint. Zenoh-Pico runs on MCUs.

**Verdict**: These protocols serve different primary use cases. Kafka wins for durable event log, replay, and stream processing at scale. Zenoh wins for real-time, low-latency pub/sub across the cloud-to-edge-to-device continuum.

---

### vs. ZeroMQ

**Architecture**: ZeroMQ is a messaging library rather than a protocol. It provides socket patterns (PUB/SUB, REQ/REP, PUSH/PULL) over TCP, IPC, and inproc transports. There is no router, broker, or naming system — addresses are raw endpoints (e.g., `tcp://localhost:5555`).

**Naming**: ZeroMQ has no key/topic space. Applications connect directly to socket addresses. Zenoh uses key expressions as a Named-Data namespace, enabling wildcard subscriptions, queryable storage, and routing by content address.

**P2P and SHM**: Both support P2P and shared memory. Zenoh's SHM is protocol-aware — it auto-negotiates during session handshake and transparently falls back to copy for remote subscribers.

**Topology**: ZeroMQ requires applications to manage their own topology (which sockets connect to which). Zenoh provides scouting, gossip routing, and router-based forwarding automatically.

**Embedded**: ZeroMQ has no MCU footprint. Zenoh-Pico targets sub-50 KB flash devices.

**Verdict**: ZeroMQ is lower-level and gives more control but requires more application-level infrastructure. Zenoh provides a richer programming model (pub/sub + query/reply + storage) with automatic topology management.

---

### vs. NATS

**Architecture**: NATS is a cloud-native messaging system with a lightweight broker. It supports pub/sub and request-reply. NATS JetStream adds persistence and consumer groups.

**Topology**: NATS requires a server. Zenoh supports serverless peer-to-peer operation.

**Embedded**: NATS has no embedded footprint. Zenoh-Pico runs on constrained devices.

**Storage**: NATS JetStream provides durable streams. Zenoh's storage manager plugin provides queryable distributed storage backed by pluggable backends (RocksDB, InfluxDB, etc.).

**Performance**: No direct head-to-head benchmark found in collected data, but Zenoh's 50+ Gbps throughput and 10 µs P2P latency exceed NATS's published figures.

**Verdict**: NATS is well-suited for cloud-native microservices. Zenoh extends further into the edge and device layer and operates without a server.

---

## Use Case Recommendations

**Choose Zenoh when**:
- You need to span cloud, edge, and embedded devices in a single protocol stack
- You require peer-to-peer communication without a broker
- You need low latency (< 100 µs) and high throughput (10+ Gbps)
- You are building ROS 2 robotics applications and need wireless/WAN support
- You want native shared memory zero-copy between local processes
- You need queryable geo-distributed storage alongside pub/sub
- You are running on constrained hardware (MCU/RTOS) and need Zenoh-Pico

**Choose MQTT when**:
- You have existing MQTT infrastructure and tooling
- Your devices are already MQTT-capable with established broker connectivity
- Throughput requirements are modest (< 1 Gbps) and broker-centric is acceptable

**Choose DDS when**:
- You need strict OMG DDS compliance or ROS 2 with the default RMW
- Your deployment is wired LAN with a stable, small number of nodes
- You require formal DDS QoS profiles (DEADLINE, LIFESPAN, OWNERSHIP, etc.)

**Choose Kafka when**:
- Durable event log with replay is the primary requirement
- You need stream processing with consumer groups and partition semantics
- Latency in the millisecond range is acceptable

**Choose ZeroMQ when**:
- You need a lightweight messaging library with manual topology control
- You want direct socket patterns without protocol overhead

**Choose NATS when**:
- You are building cloud-native microservices and want a simple, fast broker
- JetStream persistence fits your durability needs

---

## Migration Guides

- **DDS/ROS 2 to Zenoh**: Use `zenoh-plugin-dds` for transparent bridging (no application changes). For new projects use `rmw_zenoh`. See [zenoh-plugin-dds](https://github.com/eclipse-zenoh/zenoh-plugin-dds).
- **MQTT to Zenoh**: Use `zenoh-plugin-mqtt` to bridge existing MQTT clients. Key expression maps to MQTT topics. See [zenoh-plugin-mqtt](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt).
- **ROS 2 bridge**: `ros2 run rmw_zenoh_cpp rmw_zenohd` replaces the DDS RMW layer end-to-end.

---

## Sources

- "A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS" — Liang, Yuan, Lin (NTU, 2023). [Blog](https://zenoh.io/blog/2023-03-21-zenoh-vs-mqtt-kafka-dds/)
- "Comparison of DDS, MQTT, and Zenoh in Edge-to-Edge/Cloud Communication with ROS 2" — Zhang, Yu et al. (TIERS Lab, University of Turku). Semantic Scholar / DeepAI.
- ZettaScale Blog: "Zenoh-Pico Deep Dive" (2022) — embedded throughput vs. XRCE-DDS, MQTT, OPC-UA
- ZettaScale Blog: "Boosting Zenoh Performance" (2022) — peer-to-peer and routed benchmarks
- ZettaScale Blog: "ROS2 Discovery Overhead Reduction" (2021) — DDS vs. Zenoh discovery traffic
- "Automotive Middleware Performance: Comparison of FastDDS, Zenoh and vSomeIP" (IEEE VTC, 2022)
- ROS Discourse thread: "Zenoh Performance" (2023) — community methodology discussion

## See Also

- [Performance Tuning Guide](performance-tuning-guide.md) — how to configure Zenoh to achieve its best performance
- [Benchmarks](benchmarks.md) — raw benchmark data underlying the comparisons in this guide
- [ROS2 Migration Guide](ros2-migration-guide.md) — practical migration path for DDS/ROS2 users
- [DDS Context Guide](dds-context-guide.md) — detailed analysis of the DDS scalability problems Zenoh addresses
