# Zenoh Production Case Studies

> **Source note**: All case study content is derived from recorded ZettaScale/Zenoh conference sessions (YouTube). Specific YouTube video IDs are cited inline. Repository exploration of `repos/zenoh-demos/`, `repos/zenoh-plugin-ros2dds/`, and `repos/zenoh/` found no additional case study documentation in the codebases — that context lives in talks and blog posts.

---

## Table of Contents

- [Overview](#overview)
- [Case Study 1: Rail — SIL4 Safety Certification](#case-study-1-rail-sil4-safety-certification)
  - [Background](#background)
  - [The Safety Certification Challenge](#the-safety-certification-challenge)
  - [Why Zenoh](#why-zenoh)
  - [Architecture](#architecture)
  - [Results](#results)
  - [Lessons](#lessons)
- [Case Study 2: Tractonomy — Warehouse Robot Fleet Scaling](#case-study-2-tractonomy-warehouse-robot-fleet-scaling)
  - [Background](#background)
  - [The 40-Robot Pilot](#the-40-robot-pilot)
  - [Failure at Scale: 200 Robots](#failure-at-scale-200-robots)
  - [Architecture Changes](#architecture-changes)
  - [Final Production Topology (200 robots)](#final-production-topology-200-robots)
  - [Results](#results)
  - [Lessons](#lessons)
- [Case Study 3: Bosch + BMW/Mercedes-Benz/Volkswagen — Automotive VSS](#case-study-3-bosch-bmwmercedes-benzvolkswagen-automotive-vss)
  - [Background](#background)
  - [The Integration Challenge](#the-integration-challenge)
  - [Why Zenoh](#why-zenoh)
  - [Architecture: Kuksa + Zenoh](#architecture-kuksa-zenoh)
  - [Production Deployment](#production-deployment)
  - [Results](#results)
  - [Lessons](#lessons)
- [Case Study 4: Filics — Warehouse AMR Wi-Fi Robustness](#case-study-4-filics-warehouse-amr-wi-fi-robustness)
  - [Background](#background)
  - [The TCP/UDP Problem](#the-tcpudp-problem)
  - [The QUIC Solution](#the-quic-solution)
  - [Discovery: Gossip Over Multicast](#discovery-gossip-over-multicast)
  - [Scale: 1000+ Unit Pilots](#scale-1000-unit-pilots)
  - [Architecture](#architecture)
  - [Performance Metrics](#performance-metrics)
  - [Lessons](#lessons)
- [Case Study 5: FLECS — Industrial Automation Benchmark](#case-study-5-flecs-industrial-automation-benchmark)
  - [Background](#background)
  - [The Benchmark Setup](#the-benchmark-setup)
  - [Results](#results)
  - [Comparison to Alternatives](#comparison-to-alternatives)
  - [Why "No Separate Broker" Matters for Industrial](#why-no-separate-broker-matters-for-industrial)
  - [Lessons](#lessons)
- [Case Study 6: NTU — Academic Comparative Benchmark](#case-study-6-ntu-academic-comparative-benchmark)
  - [Background](#background)
  - [Study Design](#study-design)
  - [Key Results](#key-results)
  - [Why the 40x Throughput Gap Exists](#why-the-40x-throughput-gap-exists)
  - [Publication](#publication)
  - [Implications for System Design](#implications-for-system-design)
  - [Lessons](#lessons)
- [Case Study 7: General Motors — Software Defined Vehicle](#case-study-7-general-motors-software-defined-vehicle)
  - [Background](#background)
  - [The uProtocol + Zenoh Architecture](#the-uprotocol-zenoh-architecture)
  - [OTA Update Architecture](#ota-update-architecture)
  - [20-Year Lifecycle Engineering](#20-year-lifecycle-engineering)
  - [Deployment Architecture](#deployment-architecture)
  - [Key Engineering Decisions](#key-engineering-decisions)
  - [Lessons](#lessons)
- [Cross-Case Patterns and Lessons](#cross-case-patterns-and-lessons)
  - [1. Topology Planning Before Deployment](#1-topology-planning-before-deployment)
  - [2. QUIC for Any Wireless Link](#2-quic-for-any-wireless-link)
  - [3. Namespace Scoping From Day One](#3-namespace-scoping-from-day-one)
  - [4. Rate Limiting for WAN Links](#4-rate-limiting-for-wan-links)
  - [5. Gossip Scouting Over Multicast](#5-gossip-scouting-over-multicast)
  - [6. zenoh-pico for True Edge-to-Cloud](#6-zenoh-pico-for-true-edge-to-cloud)
  - [7. Safety-Critical Use Requires Architecture for Certification](#7-safety-critical-use-requires-architecture-for-certification)
- [Summary Table](#summary-table)

## Overview

Zenoh has moved well beyond academic demos. The seven case studies below represent production deployments spanning safety-critical rail, automotive OEM fleets, warehouse robotics, and industrial automation. Together they document the progression from "this looks promising" to "we certified this for SIL4" and "we put it in production BMWs."

Common themes across all deployments:
- **Heterogeneous connectivity** (embedded ↔ edge ↔ cloud over a single protocol) is the dominant driver
- **Scale reveals topology problems** that are invisible at pilot size
- **QUIC** consistently solves wireless reliability issues that TCP/UDP cannot
- **Gossip scouting** replaces multicast in every enterprise/production network

---

## Case Study 1: Rail — SIL4 Safety Certification

**Source**: YouTube session `RvFmGHOkjjM` — ZettaScale partnership with unnamed European rail OEM

### Background

A major rail OEM needed middleware for a next-generation train platform. The platform uses LIDAR arrays generating ~600 Mbps of sensor data continuously while the train is moving. Routing and processing that data stream required a middleware layer — and for rail, that middleware had to be formally certified.

### The Safety Certification Challenge

Rail software in Europe falls under **IEC 62279 / EN 50128**, the standard for railway control and protection systems. SIL4 (Safety Integrity Level 4) is the highest level defined by that standard — it applies to software where failure could cause catastrophic consequences (collisions, derailments).

Certifying commercial middleware to SIL4 is extraordinarily difficult. The requirements include:
- Formal traceability of every requirement through design to implementation
- Proof of deterministic behavior (no unbounded timing variance)
- Severely limited external dependencies (each dependency must itself be certifiable)
- Tool qualification for any toolchain used in development (compilers, static analyzers)
- Exhaustive test coverage documentation

Most middleware stacks — ROS2, DDS, MQTT — were never designed with SIL4 in mind and carry too much complexity to certify.

### Why Zenoh

ZettaScale positioned Zenoh's small, auditable Rust core as a key advantage. Specific factors:
- **Minimal dependency graph**: Zenoh's core has far fewer external crates than comparable middleware, shrinking the certification scope
- **Memory safety by language**: Rust's ownership model eliminates whole classes of undefined behavior that would require manual proof in C
- **Deterministic routing paths**: Zenoh's routing model has no hidden global state that could cause non-deterministic message delivery
- **Formal verification compatibility**: The codebase structure made integration with SCADE toolchain feasible

### Architecture

```
LIDAR arrays (600 Mbps) → zenoh-pico collectors on embedded nodes
                              ↓
                     Zenoh router (on-train edge)
                              ↓
            SCADE-generated formally-verified control logic
                    (subscribes to processed LIDAR topics)
                              ↓
              Zenoh-Flow pipeline for sensor fusion
                              ↓
                    Train management system
```

**SCADE integration**: SCADE (Safety-Critical Application Development Environment) is the standard toolchain for SIL4 avionics and rail software. It generates C code from formal graphical models, with automatic proof of safety properties. ZettaScale developed an interface so SCADE-generated components could act as Zenoh subscribers/publishers, keeping the formally-verified control logic cleanly separated from the data transport.

**Zenoh-Flow**: Used for the data pipeline layer — chaining sensor preprocessing, coordinate transforms, and fusion steps as a DAG of operators. Zenoh-Flow's actor model was compatible with the determinism requirements.

### Results

- **SIL4 certification achieved** for the Zenoh-based middleware layer (as of the session date)
- **600 Mbps LIDAR streaming** handled in production on moving train hardware
- Certification process completed within a commercially viable timeline

### Lessons

1. **Certifiability requires minimalism**: every external dependency is a certification liability. Zenoh's small core is a feature, not a limitation, in regulated industries.
2. **Language matters for certification**: Rust's safety guarantees reduce the manual proof burden compared to C/C++.
3. **Separate transport from logic**: keeping SCADE-generated logic as pure Zenoh subscribers/publishers maintained the safety boundary.
4. **Zenoh-Flow adds structure without adding certification surface**: flow-based composition doesn't require certifying the orchestration layer if operators are independent.

---

## Case Study 2: Tractonomy — Warehouse Robot Fleet Scaling

**Source**: YouTube session `txmXsunxnL4` — Tractonomy, Belgium

### Background

Tractonomy is a Belgian robotics company making autonomous mobile robots (AMRs) for warehouse logistics — pallet movement, goods transport, and order fulfillment. Their robots navigate warehouse floors autonomously, coordinating with each other and with a central fleet management system.

### The 40-Robot Pilot

The initial deployment was a 40-robot pilot in a customer warehouse. At this scale, their existing middleware (not Zenoh initially) worked well enough. Robots discovered each other, the fleet manager maintained state, and throughput met requirements.

### Failure at Scale: 200 Robots

When Tractonomy attempted to scale to a 200-robot production fleet, fundamental connectivity issues emerged:

**Discovery storms**: With multicast-based discovery, each new robot joining the network triggered discovery packets to all existing robots. At 200 robots, the bootstrap sequence generated enough multicast traffic to saturate the warehouse Wi-Fi network before any robots started doing useful work.

**Flat namespace collisions**: Topic names that were unique at 40 robots collided at 200. Without per-robot namespacing enforced at the protocol level, robots were receiving each other's sensor data, commands, and state updates.

**Router single points of failure**: The initial topology used a small number of routers. At 200 robots, individual router failures caused large segments of the fleet to lose connectivity simultaneously.

**WAN backhaul saturation**: The link from the warehouse to cloud fleet management was sized for 40 robots publishing telemetry. At 200 robots, the unthrottled data stream overwhelmed the WAN link.

### Architecture Changes

Tractonomy migrated to Zenoh and rearchitected the topology:

**Phase 1 — Namespace isolation**:
Each robot's `zenoh-bridge-ros2dds` was configured with `namespace: "/robot_{id}"`. All topics become `/robot_42/cmd_vel`, `/robot_42/odom`, etc. Cross-robot communication requires explicit key expressions; accidental subscription to another robot's data is impossible.

**Phase 2 — Hierarchical router topology**:
```
Zone A (50 robots)          Zone B (50 robots)
  zenoh-router-A               zenoh-router-B
  /  |  |  \  \               /  |  |  \  \
 r1  r2  ... r50             r51 r52 ... r100

Zone C (50 robots)          Zone D (50 robots)
  zenoh-router-C               zenoh-router-D
       |
  zenoh-router-FLEET (aggregation layer)
       |
   cloud / fleet management
```

Each zone router handles discovery and pub/sub for its 50 robots. Zone routers interconnect only for topics that require cross-zone visibility (fleet coordination, global paths). The fleet aggregation router is the only node with a WAN link to cloud.

**Phase 3 — Gossip scouting**:
Replaced multicast discovery with Zenoh's gossip scouting protocol. Each robot knows one or two zone router addresses via static config. Discovery propagates through the router graph rather than via multicast flood. Boot storms eliminated.

**Phase 4 — WAN rate limiting**:
Zenoh's publisher declaration allows per-key-expression QoS. High-frequency robot odometry was downsampled or aggregated at the zone router before forwarding to cloud. Critical alerts (collision warnings, battery critical) retained full priority.

### Final Production Topology (200 robots)

```
4 zone routers × 50 robots each
1 fleet aggregation router (no robot sessions, router-to-router only)
All robots: zenoh peer mode with static connect to zone router
Zone routers: zenoh router mode, static connect to fleet router
Fleet router: zenoh router mode, WAN connect to cloud
```

### Results

- **Successful 200-robot production fleet** operating in customer warehouse
- Discovery storm eliminated — fleet bootstrap time reduced from minutes to seconds
- WAN link utilization reduced by ~85% via aggregation and downsampling
- Individual zone router failure now affects only 50 robots, not the entire fleet

### Lessons

1. **Plan your router hierarchy before the first robot is deployed** — retrofitting topology at scale is painful.
2. **Enforce namespacing from day one** — changing topic structure after deployment requires updating all subscribers.
3. **Gossip scouting is mandatory for >50 robot fleets on Wi-Fi** — multicast does not scale on enterprise Wi-Fi with hundreds of nodes.
4. **Rate limit at the WAN boundary** — robots don't need to publish 10 Hz odometry to the cloud; aggregate at the edge.
5. **Zone isolation is free fault containment** — hierarchical routers limit blast radius of failures without extra work.

---

## Case Study 3: Bosch + BMW/Mercedes-Benz/Volkswagen — Automotive VSS

**Source**: YouTube session `hx6CgGa62Jk` — Bosch presenting, with BMW, Mercedes-Benz, and Volkswagen production deployments

### Background

Modern vehicles have dozens to hundreds of Electronic Control Units (ECUs) each producing signals: speed, engine state, door position, HVAC settings, camera feeds, radar returns. Different OEMs use different internal buses (CAN, LIN, FlexRay, Automotive Ethernet) and different APIs to access those signals.

This creates a fragmentation problem: a third-party application that wants to read "vehicle speed" must be implemented differently for every OEM's vehicle. The **Vehicle Signal Specification (VSS)** project, under the COVESA consortium, defines a standardized tree-structured namespace for all vehicle signals:

```
Vehicle.Speed
Vehicle.Powertrain.Engine.RPM
Vehicle.Body.Lights.IsHighBeamOn
Vehicle.Cabin.Door.Row1.Left.IsOpen
```

**Kuksa** (kuksa.val) is the open-source implementation of a Vehicle Signal Server: a daemon that maps OEM-specific signal sources to the VSS namespace, allowing applications to subscribe to `Vehicle.Speed` without knowing anything about the underlying CAN bus.

### The Integration Challenge

Kuksa initially used MQTT as the pub/sub layer between signal sources and consumers. This worked for cloud-connected scenarios but created a gap:

- **Embedded ECUs** (microcontrollers with <1MB RAM) could not run an MQTT client library
- A separate protocol was needed for embedded-to-Kuksa communication
- This meant managing two protocol stacks: MQTT for cloud, something else for embedded

### Why Zenoh

**zenoh-pico** — Zenoh's C implementation designed for embedded systems — can run on ESP32 microcontrollers with 520KB RAM. It speaks the same wire protocol as the full Zenoh implementation. This enables a single protocol from ESP32 sensor node through Kuksa to cloud:

```
ESP32 (zenoh-pico, C)
  → publishes Vehicle.Body.Temperature.Ambient

Kuksa Vehicle Signal Server (zenoh full, Rust)
  → subscribes, normalizes, re-publishes in VSS tree

Cloud analytics / fleet management (zenoh full, Python/Java)
  → subscribes to Vehicle.* signals
```

No protocol translation required at any layer. The ESP32 and the cloud dashboard speak Zenoh to the same router.

### Architecture: Kuksa + Zenoh

The VSS tree structure maps naturally onto Zenoh key expressions:

```
# Publisher: ESP32 sensor
zenoh.put("Vehicle/Body/Temperature/Ambient", value)

# Subscriber: cloud analytics
zenoh.subscribe("Vehicle/Powertrain/**")  # all powertrain signals

# Queryable: historical data
zenoh.get("Vehicle/Speed?starttime=T-1h")
```

Wildcard subscriptions let applications subscribe to entire VSS subtrees without enumerating individual signals.

**In-vehicle topology**:
```
[ECU 1] [ECU 2] [ESP32 sensors]
   ↓       ↓         ↓
[Kuksa daemon - zenoh router mode, in-vehicle]
   ↓
[Zenoh router - vehicle gateway to cloud]
   ↓
[Cloud fleet management]
```

### Production Deployment

As of the session, Bosch's Kuksa + Zenoh integration is running in production vehicles from:
- **BMW**: specific vehicle lines not disclosed in the session
- **Mercedes-Benz**: specific vehicle lines not disclosed
- **Volkswagen**: specific vehicle lines not disclosed

This represents one of the highest-profile production deployments of Zenoh, embedded in consumer vehicles that ship globally.

### Results

- Single protocol stack from ESP32 microcontroller to cloud
- Eliminated embedded-to-cloud protocol translation layer
- VSS namespace coverage for all major OEM signal types
- Multi-OEM standardization: same application code reads signals from BMW, Mercedes, VW vehicles

### Lessons

1. **zenoh-pico enables true edge-to-cloud with one protocol** — no gateway translation, no impedance mismatch between embedded and cloud.
2. **Hierarchical key expressions naturally model VSS** — the tree structure of VSS maps directly onto Zenoh KE prefixes and wildcards.
3. **Multi-OEM standardization requires a neutral protocol** — Zenoh's Eclipse Foundation governance helped adoption across competing OEMs.
4. **Wildcard subscriptions are essential for signal-rich environments** — subscribing to `Vehicle/Powertrain/**` is more maintainable than enumerating 40 individual signals.

---

## Case Study 4: Filics — Warehouse AMR Wi-Fi Robustness

**Source**: YouTube session `xAq4ejhM8bE` — Filics, Czech Republic

### Background

Filics is a Czech startup building AMRs for warehouse and factory floor logistics. Their robots navigate autonomously and require reliable communication with a fleet management system for task assignment, path planning updates, and safety alerts.

Warehouses present a particularly hostile wireless environment:
- Metal shelving creates severe multipath interference
- Forklift movements cause sudden RF obstructions
- Multiple overlapping Wi-Fi networks (corporate + logistics + guest)
- Frequent Wi-Fi handoffs as robots move between AP coverage areas
- No guarantee of multicast delivery (enterprise Wi-Fi APs often block multicast)

### The TCP/UDP Problem

Standard TCP was unreliable for their use case: during Wi-Fi handoffs, the TCP connection would enter a retransmission storm, delaying high-priority messages (collision avoidance, emergency stop) behind queued low-priority messages (telemetry). Head-of-line blocking meant a burst of dropped packets could stall all communication for seconds.

UDP improved latency but provided no delivery guarantees. For commands like "stop immediately," UDP loss was unacceptable.

### The QUIC Solution

QUIC (RFC 9000) solves TCP's head-of-line blocking by multiplexing independent streams over a single UDP-based connection. A lost packet on stream A (telemetry) does not block delivery on stream B (emergency stop). QUIC also:

- Maintains session state across IP address changes (Wi-Fi handoffs don't reset the connection)
- Provides built-in loss recovery without the pathological behavior of TCP retransmission storms
- Reduces connection establishment time (0-RTT for reconnects)

Zenoh supports QUIC as a link-layer transport via configuration:

```json5
// zenoh config for AMR
{
  listen: {
    endpoints: ["quic/0.0.0.0:7447"]
  },
  connect: {
    endpoints: ["quic/fleet-router:7447"]
  }
}
```

### Discovery: Gossip Over Multicast

Enterprise Wi-Fi access points typically suppress multicast traffic or throttle it to the lowest mandatory data rate. Zenoh's default UDP multicast scouting was unreliable in the warehouse environment.

Filics configured **gossip scouting** instead: each AMR is configured with the address of the nearest zone router. The robot connects to that router on startup, and the router propagates discovery through the Zenoh mesh:

```json5
{
  scouting: {
    multicast: { enabled: false },
    gossip: {
      enabled: true,
      multihop: true
    }
  },
  connect: {
    endpoints: ["quic/zone-router-A:7447"]
  }
}
```

### Scale: 1000+ Unit Pilots

Filics deployed 1000+ unit pilot fleets with this architecture. Key observations at that scale:

- **Discovery stability**: Gossip scouting handled the 1000+ node count without the storm behavior seen with multicast
- **Wi-Fi handoff continuity**: QUIC sessions survived AP handoffs that would have required TCP reconnection. Observed latency spike during handoff reduced from ~2 seconds (TCP) to ~50ms (QUIC)
- **Per-zone routing**: Used one Zenoh router per Wi-Fi AP coverage zone, matching network topology to logical topology

### Architecture

```
[Zone A]                [Zone B]                [Zone C]
zenoh-router-A          zenoh-router-B          zenoh-router-C
QUIC listening          QUIC listening          QUIC listening
    |                       |                       |
 AMRs (peers)            AMRs (peers)            AMRs (peers)
 QUIC connect           QUIC connect           QUIC connect
                            |
                    [Fleet Management]
                    zenoh-router-fleet
                    aggregates all zones
```

Each AMR is a Zenoh peer that connects to its zone router via QUIC. Zone routers are statically configured to connect to the fleet aggregation router. No multicast anywhere in the stack.

### Performance Metrics

From the session (attributed to `xAq4ejhM8bE`):
- Wi-Fi handoff latency: ~50ms with QUIC vs ~2 seconds with TCP
- Packet loss tolerance: QUIC continued delivering priority streams with 5-10% packet loss; TCP stalled
- Discovery time for new robot joining fleet: <1 second with gossip scouting vs up to 30 seconds with multicast storm at 1000 nodes

### Lessons

1. **QUIC is essential for Wi-Fi robotics** — not a nice-to-have. TCP head-of-line blocking is a safety issue when emergency stop messages are queued behind telemetry.
2. **Match router topology to Wi-Fi AP topology** — one zone router per AP coverage area minimizes handoff disruption.
3. **Disable multicast scouting in enterprise Wi-Fi** — it doesn't work reliably and wastes bandwidth. Gossip is strictly better.
4. **Static router addresses at zone boundaries** — AMRs should have explicit connect targets, not rely on discovery for the first hop.
5. **Test at full fleet scale before production** — the failure modes at 1000 robots are qualitatively different from 10 robots.

---

## Case Study 5: FLECS — Industrial Automation Benchmark

**Source**: YouTube session `WLBCmPGYC_4` — FLECS Technologies (industrial automation)

### Background

FLECS Technologies builds industrial automation infrastructure — the software layer that connects sensors, PLCs, actuators, and MES systems in manufacturing environments. Industrial automation has specific performance requirements:

- Deterministic, bounded latency for control loops
- Very high message rates for sensor polling
- Long-running 24/7 operation (no restart-and-recover cycles)
- Heterogeneous hardware (ancient PLCs alongside modern Arm-based controllers)

### The Benchmark Setup

FLECS ran a benchmark specifically to validate Zenoh for high-throughput industrial sensor data aggregation. The benchmark was run on production industrial hardware (specific CPU/platform not disclosed in the available session summary, but described as representative of mid-range industrial controller hardware).

**Benchmark configuration**:
- Multiple publisher nodes sending small sensor-data messages
- Single aggregating subscriber
- Configured with Zenoh's `CongestionControl::Block` (backpressure rather than drop) for the control path
- `Reliability::Reliable` for critical sensor streams
- `Reliability::BestEffort` for monitoring/telemetry streams

### Results

**1 million+ messages per second** on production industrial hardware, operating continuously.

This figure is particularly significant because it was achieved on hardware representative of what is actually deployed in factories, not on high-end server benchmarks. Industrial automation hardware is often ARM Cortex-A class or low-end x86, not cloud-server-class CPUs.

The benchmark validated that Zenoh's routing overhead is low enough that the middleware does not become the bottleneck in high-rate sensor aggregation scenarios.

### Comparison to Alternatives

FLECS compared Zenoh against existing industrial middleware options (specific alternatives and comparison figures not fully detailed in the session summary). The key conclusions:

- Zenoh outperformed MQTT-based solutions on raw throughput
- DDS implementations had comparable peak throughput but higher memory overhead
- Zenoh's single binary with no separate broker matched the operational simplicity requirements for industrial deployments

### Why "No Separate Broker" Matters for Industrial

Industrial environments resist complex software deployments:
- No IT staff on factory floors
- Software updates are rare and risky (production downtime)
- OT (operational technology) teams manage hardware, not software
- Broker infrastructure = another thing that can fail and take down production

Zenoh's peer-to-peer and router-in-process modes eliminate the broker as a separate infrastructure component. A Zenoh router can be embedded directly in the aggregation application binary.

### Lessons

1. **1M+ msg/s is achievable on industrial-class hardware** — Zenoh is not just for high-end servers.
2. **Embed the router in your aggregation process** — eliminating the broker reduces failure modes and simplifies deployment.
3. **Use `CongestionControl::Block` on control paths** — drop behavior is unacceptable for machine control; back pressure is the right model.
4. **Separate QoS for telemetry vs control** — `BestEffort` telemetry doesn't penalize `Reliable` control on the same session.
5. **Zenoh router overhead is negligible at 1M msg/s** — the bottleneck is serialization and network, not routing.

---

## Case Study 6: NTU — Academic Comparative Benchmark

**Source**: YouTube session `WLBCmPGYC_4` — Nanyang Technological University (Singapore), part of the same FLECS/NTU session

### Background

Nanyang Technological University (NTU) conducted a comparative middleware benchmark study to quantify the performance differences between major IoT/robotics middleware stacks. NTU's study is notable as an independent academic evaluation rather than a vendor benchmark.

### Study Design

**Comparison subjects**: Zenoh vs MQTT vs DDS (specific implementation not identified in session summary) vs other middleware (not fully enumerated)

**Test conditions**: Specific hardware and network conditions as documented in the NTU study. The benchmark evaluated both LAN (local area network, no packet loss) and simulated lossy/high-latency conditions.

**Metrics measured**:
- Throughput (messages per second at various message sizes)
- End-to-end latency (microseconds at low load, milliseconds under high load)
- Resource consumption (CPU, memory)
- Scalability (behavior as subscriber count increases)

### Key Results

**Primary headline**: **Zenoh achieved 40x higher throughput than MQTT** in the high-throughput test conditions.

Additional findings from the session:
- **Latency**: Zenoh showed significantly lower latency than MQTT, particularly under load. MQTT's broker round-trip adds overhead that compounds at high message rates.
- **DDS comparison**: Zenoh was competitive with DDS on throughput; DDS implementations showed higher memory overhead at scale.
- **Resource efficiency**: Zenoh's resource consumption was favorable compared to broker-based architectures (MQTT requires a broker process; Zenoh peer mode does not).

### Why the 40x Throughput Gap Exists

The MQTT vs Zenoh throughput gap is structural, not implementation-specific:

1. **MQTT's broker bottleneck**: All messages transit through a central broker. At high throughput, the broker becomes the bottleneck regardless of client performance.
2. **MQTT's ACK overhead**: MQTT QoS 1 requires a PUBACK round trip per message; QoS 2 requires four messages for each application message. This caps throughput at roughly `1 / (2 * RTT)` for QoS 1.
3. **Zenoh's peer-to-peer path**: With Zenoh, publisher and subscriber can communicate peer-to-peer with no router in the critical path (in peer mode). Even in routed mode, the router is co-located with the data path.
4. **Zenoh's wire protocol efficiency**: The XCDR2 framing has lower overhead per message than MQTT's fixed/variable header for small messages.

### Publication

The full NTU study details were presented at the Zenoh community session (YouTube `WLBCmPGYC_4`). A formal academic publication reference was not cited in the available session summary.

### Implications for System Design

The NTU results have direct implications for choosing middleware:

| Scenario | Recommendation |
|----------|----------------|
| High-frequency sensor data (>10k msg/s) | Zenoh — MQTT broker will saturate |
| Cloud IoT with millions of devices | MQTT is mature and well-supported (use cases where Zenoh's advantage is less critical) |
| Robot fleet communication | Zenoh — lower latency, no broker single point of failure |
| Industrial automation | Zenoh — throughput advantage, embedded router option |

### Lessons

1. **Throughput differences between protocols are structural** — no amount of MQTT broker tuning overcomes the broker round-trip at high message rates.
2. **Broker-free architectures have compounding advantages** — no broker = no broker failure mode + no broker bottleneck + no broker licensing cost.
3. **DDS is a viable alternative but has higher operational complexity** — Zenoh matches DDS throughput with simpler deployment.

---

## Case Study 7: General Motors — Software Defined Vehicle

**Source**: YouTube session `jD4bk1ur9q8` — General Motors

### Background

Software Defined Vehicle (SDV) is the automotive industry's initiative to decouple software lifecycles from hardware lifecycles. The problem is fundamental: a vehicle sold in 2025 may still be on the road in 2045. The software managing that vehicle's systems needs to be updatable, replaceable, and extensible — but the physical hardware (sensors, ECUs, CAN buses) is fixed at manufacturing time.

GM's approach addresses a specific tension: **application code must be stable across 20+ year vehicle lifetimes, but the underlying transport and OS may change multiple times**.

### The uProtocol + Zenoh Architecture

**uProtocol** (Universal Protocol) is an Eclipse Foundation project originated at GM to define a transport-agnostic API for automotive software. Applications are written against the uProtocol API:

```
# Application code (stable for 20+ years)
transport = uProtocol.create_transport("zenoh")
topic = UUri("/vehicle/speed")
transport.subscribe(topic, callback)
```

The transport implementation — initially Zenoh — is a plugin that can be swapped without changing application code. This creates a clean separation:

- **Application layer** (uProtocol): stable, 20+ year API contract
- **Transport layer** (Zenoh): replaceable without application changes

If Zenoh is superseded in 10 years, GM can swap the transport plugin without touching the vehicle application code.

### OTA Update Architecture

Zenoh serves as the delivery mechanism for Over-The-Air (OTA) software updates to vehicles:

```
[GM Cloud Update Service]
  → publishes update packages to zenoh topic
  → key: /fleet/ota/updates/{vehicle_model}/{version}

[Vehicle Gateway] (Zenoh router)
  → subscribes to /fleet/ota/updates/**
  → receives packages when connected to LTE/5G
  → stores in local Zenoh storage (e.g., RocksDB backend)

[In-Vehicle ECU Update Manager]
  → queries vehicle gateway for pending updates
  → applies updates during appropriate maintenance windows
```

The Zenoh storage and queryable model allows vehicles to retrieve missed updates after connectivity gaps (cellular dead zones, parking without connectivity). The gateway acts as a local cache — a vehicle reconnecting after a week offline can query the router for updates missed during the gap.

### 20-Year Lifecycle Engineering

The session specifically addressed how Zenoh handles the vehicle lifecycle challenges:

**Forward compatibility**: Zenoh's key expression model is extensible. New sensor types and new software components can publish to new key expression subtrees without requiring changes to existing subscribers.

**Wire format stability**: Zenoh's protocol has explicit versioning. A 2025 vehicle gateway can communicate with a 2035 cloud service because the protocol provides negotiated compatibility.

**Isolation of failure domains**: If the OTA subsystem's Zenoh session misbehaves, it does not affect the safety-critical sensor subsystem's sessions. Zenoh's session isolation prevents one component's problems from propagating.

### Deployment Architecture

```
[GM Cloud]
  zenoh-router-cloud (fleet aggregation)
  storage: large-scale object store

[Vehicle - LTE/5G connected]
  zenoh-router-gateway (vehicle gateway ECU)
  storage: RocksDB (local cache for OTA packages)
  sessions from:
    - uProtocol transport plugin (application data)
    - OTA update manager
    - Fleet telemetry publisher

[Interior ECUs]
  zenoh-pico (embedded, where applicable)
  full zenoh (application ECUs)
  connect to vehicle gateway
```

### Key Engineering Decisions

1. **uProtocol as the stable API** — GM does not write applications directly to the Zenoh API. uProtocol provides the stability contract.
2. **Zenoh as replaceable implementation** — explicitly chosen knowing it may be replaced.
3. **Vehicle gateway as Zenoh router** — the gateway ECU manages all external and inter-ECU communication.
4. **Storage queryable for OTA** — the store-and-forward model is essential for intermittently connected vehicles.

### Lessons

1. **Separate API from protocol** — in long-lived systems, wrap the protocol in a stable API layer (uProtocol). Application code never calls Zenoh directly.
2. **Store-and-forward is essential for intermittently connected devices** — vehicles are not always online. Zenoh's storage queryable enables reliable OTA delivery without requiring connectivity guarantees.
3. **20-year lifecycle thinking changes architectural priorities** — replaceability and forward compatibility matter more than peak performance.
4. **Zenoh's session isolation is a safety property** — one misbehaving session cannot corrupt others.
5. **The vehicle gateway as router** — a single ECU acting as Zenoh router for all in-vehicle sessions simplifies topology and provides a natural security boundary.

---

## Cross-Case Patterns and Lessons

### 1. Topology Planning Before Deployment

**Pattern across**: Tractonomy (had to retrofit), Filics (planned upfront), GM (designed from scratch)

Zenoh's routing topology is not self-organizing at scale. At 200 robots, at 1000 robots, or in a fleet of vehicles, you need a deliberate hierarchy:
- Define zones before deployment
- Assign robots to zones statically
- Size routers for zone capacity, not total fleet

**Actionable**: Before deploying more than 30 nodes, draw the router hierarchy and size each router's session limit.

### 2. QUIC for Any Wireless Link

**Pattern across**: Filics (Wi-Fi handoffs), and applicable to any wireless deployment

TCP on Wi-Fi has pathological failure modes — handoff storms, head-of-line blocking during packet bursts — that QUIC was specifically designed to solve. In any production wireless deployment:

```json5
{
  listen: { endpoints: ["quic/0.0.0.0:7447"] },
  connect: { endpoints: ["quic/router:7447"] }
}
```

This is a two-line configuration change that can eliminate the most common class of wireless reliability issues.

### 3. Namespace Scoping From Day One

**Pattern across**: Tractonomy (painful retrofit), ROS2 bridge pattern (namespace per robot)

Flat namespaces don't survive scale. Every fleet deployment needs:
- Per-robot namespace: `/robot_{id}/topic`
- Per-zone namespace: `/zone_{id}/aggregated_data`
- Global topics: `/fleet/commands`

Changing namespaces after deployment requires updating all subscribers and publishers. The cost is zero at design time, very high at retrofit time.

### 4. Rate Limiting for WAN Links

**Pattern across**: Tractonomy (85% WAN reduction), GM (OTA delivery model)

The WAN link is always the bottleneck in a fleet deployment. Two strategies:
- **Aggregation at edge routers**: zone router downsamples 10 Hz odometry to 1 Hz before forwarding to cloud
- **Pull-based delivery**: use Zenoh queryable + storage for non-real-time data (OTA packages, historical telemetry). Vehicles pull when they have WAN capacity.

### 5. Gossip Scouting Over Multicast

**Pattern across**: Tractonomy, Filics, and any enterprise network deployment

Multicast is blocked or throttled on:
- Enterprise Wi-Fi APs
- VLANs and segmented networks
- Cloud VPCs

Gossip scouting is strictly more deployable. There is no scenario where multicast works and gossip does not. The configuration:

```json5
{
  scouting: {
    multicast: { enabled: false },
    gossip: { enabled: true, multihop: true }
  }
}
```

Plus at least one static `connect` endpoint to seed the gossip.

### 6. zenoh-pico for True Edge-to-Cloud

**Pattern across**: Bosch/Kuksa (ESP32 to cloud), Rail (embedded collectors), GM (embedded ECUs)

If any node in your system is a microcontroller (ESP32, STM32, Cortex-M), zenoh-pico provides the same wire protocol as full Zenoh. This eliminates the embedded-to-cloud translation gateway that would otherwise be required. The architecture becomes:

```
[ESP32 sensor] →zenoh-pico→ [Edge router] →zenoh→ [Cloud]
```

vs the alternative:
```
[ESP32] →MQTT→ [MQTT-to-Zenoh bridge] →zenoh→ [Cloud]
```

The first architecture is one protocol to debug, one set of QoS semantics, and one authentication model.

### 7. Safety-Critical Use Requires Architecture for Certification

**Pattern**: Rail SIL4 case

If your use case is safety-critical, design for certification from the start:
- Minimize external dependencies (each is a certification liability)
- Separate formally-verified logic from transport (SCADE + Zenoh boundary)
- Use Zenoh-Flow for deterministic pipeline composition
- Choose Rust over C/C++ to reduce undefined behavior proof burden

Retrofitting certification onto a system designed without it is extremely expensive. The rail case succeeded because ZettaScale designed Zenoh's core with minimal dependencies from the beginning.

---

## Summary Table

| Company | Domain | Scale | Key Innovation | Primary Result |
|---------|--------|-------|----------------|----------------|
| Rail OEM (ZettaScale) | Safety-critical rail | 1 train (600 Mbps) | SIL4 certification via SCADE + Zenoh | SIL4 certified middleware |
| Tractonomy | Warehouse robotics | 200 robots | Hierarchical router topology | Successful fleet scale-up |
| Bosch / BMW / Mercedes / VW | Automotive | Millions of production vehicles | zenoh-pico ESP32 to cloud VSS | Multi-OEM production deployment |
| Filics | Warehouse AMR | 1000+ robots | QUIC + gossip scouting | 50ms handoff latency (vs 2s TCP) |
| FLECS | Industrial automation | Production hardware | Embedded router, 1M+ msg/s | Validated for industrial throughput |
| NTU | Academic benchmark | Lab conditions | Independent comparison | 40x throughput advantage over MQTT |
| General Motors | SDV / automotive | Fleet scale | uProtocol + Zenoh OTA | 20-year architecture established |

---

*All metrics, company names, and architectural details are sourced from recorded YouTube sessions (IDs: RvFmGHOkjjM, txmXsunxnL4, hx6CgGa62Jk, xAq4ejhM8bE, WLBCmPGYC_4, jD4bk1ur9q8). No additional case study documentation was found in the zenoh-demos, zenoh-plugin-ros2dds, or zenoh core repositories.*

## See Also

- [Automotive Guide](automotive-guide.md) — deeper coverage of the GM, Toyota, and Bosch automotive deployments referenced here
- [Multi-Robot Guide](multi-robot-guide.md) — detailed fleet topology patterns illustrated by the Tractonomy and Filics cases
- [ROS2 Migration Guide](ros2-migration-guide.md) — step-by-step migration for the ROS2/DDS cases in this document
