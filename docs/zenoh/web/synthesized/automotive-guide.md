# Zenoh in Automotive and Software Defined Vehicle (SDV) Contexts

Zenoh has emerged as a foundational middleware in the automotive industry, selected by General Motors, Woven by Toyota, TTTech Auto, and the Eclipse SDV working group as the communication backbone for next-generation Software Defined Vehicles. This guide covers the architectural decisions, deployment patterns, and specific configurations needed to use Zenoh in automotive systems — from in-vehicle ECU communication through V2X to cloud fleet management.

---

## Table of Contents

- [1. Why Automotive Needs New Middleware](#1-why-automotive-needs-new-middleware)
- [2. V2X Challenges and Scale](#2-v2x-challenges-and-scale)
  - [DDS Fails at V2X](#dds-fails-at-v2x)
  - [MQTT Fails at Scale](#mqtt-fails-at-scale)
  - [How Zenoh Addresses V2X](#how-zenoh-addresses-v2x)
- [3. The MQTT TLS Thundering Herd Problem](#3-the-mqtt-tls-thundering-herd-problem)
  - [How the Storm Forms](#how-the-storm-forms)
  - [Why QUIC Avoids This](#why-quic-avoids-this)
  - [Zenoh Router Scaling for Fleets](#zenoh-router-scaling-for-fleets)
- [4. AUTOSAR Adaptive Platform Integration](#4-autosar-adaptive-platform-integration)
  - [The AUTOSAR Adaptive Problem](#the-autosar-adaptive-problem)
  - [AUTOSAR Concept Mapping to Zenoh](#autosar-concept-mapping-to-zenoh)
  - [AUTOSAR Classic Integration via Xenopico](#autosar-classic-integration-via-xenopico)
  - [In-Vehicle Zenoh Topology for AUTOSAR](#in-vehicle-zenoh-topology-for-autosar)
- [5. uProtocol Architecture — GM and Toyota](#5-uprotocol-architecture-gm-and-toyota)
  - [What is Eclipse uProtocol](#what-is-eclipse-uprotocol)
  - [uProtocol's Three-Layer Architecture](#uprotocols-three-layer-architecture)
  - [Mapping uProtocol Addresses to Zenoh Key Expressions](#mapping-uprotocol-addresses-to-zenoh-key-expressions)
  - [GM's Deployment Rationale](#gms-deployment-rationale)
  - [Woven by Toyota: The Bridge Pattern](#woven-by-toyota-the-bridge-pattern)
  - [Rust and Memory Safety in uProtocol](#rust-and-memory-safety-in-uprotocol)
- [6. Eclipse SDV Fleet Management Blueprint](#6-eclipse-sdv-fleet-management-blueprint)
  - [Eclipse SDV Working Group](#eclipse-sdv-working-group)
  - [Fleet Management System Blueprint Architecture](#fleet-management-system-blueprint-architecture)
  - [VSS Key Expression Mapping](#vss-key-expression-mapping)
  - [Key KE Patterns Used in the FMS Blueprint](#key-ke-patterns-used-in-the-fms-blueprint)
  - [Zetta Platform Integration](#zetta-platform-integration)
- [7. Zetta Auto: Safety-Critical DDS Replacement](#7-zetta-auto-safety-critical-dds-replacement)
  - [What Zetta Auto Is](#what-zetta-auto-is)
  - [ISO 26262 ASIL-D Requirements](#iso-26262-asil-d-requirements)
  - [Time-Sensitive Networking Integration](#time-sensitive-networking-integration)
  - [DDS and Zenoh Interoperability](#dds-and-zenoh-interoperability)
- [8. Zenoh-Flow for Autonomous Driving Pipelines](#8-zenoh-flow-for-autonomous-driving-pipelines)
  - [What Zenoh-Flow Is](#what-zenoh-flow-is)
  - [Zero-Copy Optimization](#zero-copy-optimization)
  - [Data Flow Determinism vs. ROS 2](#data-flow-determinism-vs-ros-2)
- [9. TTTech Auto: Deterministic Execution and ISO 26262](#9-tttech-auto-deterministic-execution-and-iso-26262)
  - [Timing Contracts](#timing-contracts)
  - [Scheduling Optimization](#scheduling-optimization)
  - [Offline Analyzability for Safety Certification](#offline-analyzability-for-safety-certification)
- [10. Fleet Management at Scale — GM's 20-Year Lifecycle](#10-fleet-management-at-scale-gms-20-year-lifecycle)
  - [The 20-Year Software Problem](#the-20-year-software-problem)
  - [uProtocol as the Stable API Layer](#uprotocol-as-the-stable-api-layer)
  - [Multiple Ownership Transfer](#multiple-ownership-transfer)
  - [OTA Update Architecture](#ota-update-architecture)
- [11. Production Deployment Patterns](#11-production-deployment-patterns)
  - [In-Vehicle Topology](#in-vehicle-topology)
  - [Edge (Roadside Unit / MEC Node)](#edge-roadside-unit-mec-node)
  - [Cloud Router Cluster](#cloud-router-cluster)
- [12. Security and mTLS per Vehicle](#12-security-and-mtls-per-vehicle)
  - [Certificate-per-Vehicle Architecture](#certificate-per-vehicle-architecture)
  - [ACL Enforcement by VIN](#acl-enforcement-by-vin)
  - [Certificate Rotation](#certificate-rotation)
- [13. Key Expression Patterns for Vehicle Fleets](#13-key-expression-patterns-for-vehicle-fleets)
  - [Telemetry (Vehicle → Cloud)](#telemetry-vehicle-cloud)
  - [Commands (Cloud → Vehicle)](#commands-cloud-vehicle)
  - [Status and Health](#status-and-health)
  - [OTA Updates](#ota-updates)
  - [Digital Twin Queries](#digital-twin-queries)
  - [Fleet-Wide Subscriptions](#fleet-wide-subscriptions)
  - [uProtocol-style Service Addressing](#uprotocol-style-service-addressing)
- [Summary](#summary)


---


## 1. Why Automotive Needs New Middleware

Modern vehicles contain over 100 million lines of code. They are assembled from dozens of Electronic Control Units (ECUs) communicating over heterogeneous bus systems: CAN, LIN, FlexRay, SOME/IP over Ethernet, and increasingly Ethernet-native compute platforms. At the same time, the industry is transitioning to Software Defined Vehicles where hardware function is determined by software rather than by dedicated hardware modules — meaning software must be updatable over the entire vehicle lifecycle.

This shift exposes the limits of current middleware:

| Protocol | Problem in SDV Context |
|----------|----------------------|
| CAN/LIN | Bandwidth-limited, no IP routing, not addressable from cloud |
| DDS over UDP multicast | Works inside the vehicle; fails for V2X (multicast requires shared L2, blocked by NAT and firewalls) |
| MQTT | Hub-spoke topology requires central cloud broker; TLS at scale causes reconnection storms; no healing mechanisms |
| SOME/IP | AUTOSAR-specific, requires static service discovery configuration, not cloud-native |

The automotive industry identified three requirements that no single existing protocol satisfied:

1. **Unified span**: One protocol that works on a 256KB microcontroller, a gateway ECU, and a cloud data center
2. **Location transparency**: Applications should not need to know whether data comes from local storage, another ECU, or a remote cloud service
3. **Healing and state management**: When a vehicle loses connectivity and reconnects, the protocol should restore state without application-layer intervention

Zenoh addresses all three. It operates across serial, Bluetooth, IPv4/IPv6, TCP, UDP, and QUIC transports. It supports pub/sub, distributed queries (queryables), and distributed storage with alignment protocols. Its protocol overhead is approximately 5 bytes, enabling deployment on Arduino and ESP32 class hardware while running the same code on cloud infrastructure.

*(Source: "Zenoh for Software Defined Vehicle Architectures" — video `_WB7bOHUErU`; "Transforming Automotive Communication with Zetta Auto" — video `BGJRHCOBtSE`)*

---

## 2. V2X Challenges and Scale

**V2X** (Vehicle-to-Everything) refers to all communication paths involving a vehicle:

- **V2C**: Vehicle-to-Cloud (telemetry, OTA updates, fleet management)
- **V2V**: Vehicle-to-Vehicle (cooperative awareness, collision avoidance)
- **V2I**: Vehicle-to-Infrastructure (toll systems, traffic signals, roadside units)
- **V2N**: Vehicle-to-Network (mobile network handoff during movement)

### DDS Fails at V2X

DDS's discovery and data distribution rely on UDP multicast. Within a single L2 network segment inside a vehicle, this works efficiently. However, V2X communication requires routing across the internet, through NATs, and across carrier networks. UDP multicast does not traverse these boundaries. Even configuring DDS for unicast over WAN requires careful manual endpoint configuration and scales poorly to fleets of millions of vehicles.

### MQTT Fails at Scale

MQTT requires a central broker. For a fleet of one million vehicles, all vehicles connect to a broker cluster. This centralization creates three failure modes:

1. **Single point of failure**: A broker outage disconnects the entire fleet
2. **No state healing**: MQTT does not provide mechanisms to retrieve state published during disconnection; vehicles that reconnect start from scratch
3. **TLS reconnection storms** — described in detail in the next section

### How Zenoh Addresses V2X

Zenoh routes across all transport types simultaneously. A Zenoh router deployed at an edge node (a roadside unit, a 5G MEC node, or a regional gateway) participates in the same keyspace as the vehicle's internal Zenoh session and the cloud backend. No protocol conversion is required.

Zenoh's **query mechanism** solves the state healing problem directly. When a vehicle reconnects after an outage, it can issue a `get()` against a key expression to retrieve data that was published during its disconnection. The query resolves against whichever storage node currently holds the data — whether that is a local edge router or a cloud backend — without application code changes.

Dynamic routing allows a Zenoh router to adapt routing paths as vehicle location changes. As a vehicle moves from one roadside unit's coverage area to another, the Zenoh gossip protocol re-establishes optimal paths without requiring application-layer connection management.

*(Source: "How is Zenoh addressing the current V2X challenges" — video `4udbGc4N6-E`)*

---

## 3. The MQTT TLS Thundering Herd Problem

The thundering herd problem is a specific failure mode that occurs when a large fleet of vehicles reconnects to cloud infrastructure simultaneously after an outage. It is not a theoretical concern: any cloud maintenance window, regional network outage, or cloud provider incident triggers this pattern.

### How the Storm Forms

When a cloud MQTT broker cluster comes back online after an outage, every vehicle that was disconnected attempts reconnection at approximately the same time:

```
Cloud outage ends at T=0
├── Vehicle 1 detects TCP connection lost → initiates TLS handshake at T=0.1s
├── Vehicle 2 detects TCP connection lost → initiates TLS handshake at T=0.1s
├── ...
└── Vehicle 1,000,000 → initiates TLS handshake at T~0.5s
```

Each TLS 1.2 handshake requires:
- TCP three-way handshake (3 round trips)
- TLS ClientHello / ServerHello exchange
- Certificate chain transmission from server
- Certificate chain validation by client (CPU-intensive)
- Client certificate validation by server (for mTLS)
- Session key derivation

At 1 million vehicles reconnecting within seconds, the broker cluster must:
1. Accept 1M+ incoming TCP connections simultaneously (kernel `accept()` queue exhaustion)
2. Transmit the server certificate chain 1M times (network saturation)
3. Validate 1M client certificates (CPU saturation on HSMs or certificate validation servers)
4. Establish 1M TLS sessions in state tables (memory exhaustion)

The result: the broker cluster cannot accept connections fast enough. Vehicles time out and retry — increasing the load further. The system enters a positive feedback loop where the reconnection storm itself prevents recovery.

### Why QUIC Avoids This

QUIC (RFC 9000), the transport Zenoh supports natively, was designed specifically to improve on TCP+TLS reconnection behavior:

**0-RTT resumption**: QUIC stores session tickets on the client side. When a vehicle reconnects to a QUIC endpoint it has connected to before, it can send the first data packet in the same roundtrip as the handshake ("0-RTT"). The server validates the session ticket rather than performing a full certificate exchange.

**Connection migration**: QUIC connections are identified by connection IDs, not by IP:port tuples. When a vehicle moves between network interfaces (cellular to Wi-Fi, or between 4G cells), the connection migrates without a full teardown and re-establishment. This eliminates an entire class of reconnection events.

**Built-in multiplexing**: Multiple data streams share a single QUIC connection without head-of-line blocking. Telemetry and command channels can run on separate streams over one connection rather than requiring separate TCP connections.

**Congestion-aware retransmission**: QUIC's built-in congestion control handles burst retransmissions gracefully, preventing the retry amplification that worsens TCP-based storm recovery.

### Zenoh Router Scaling for Fleets

Zenoh's routers handle fleet reconnection through gossip-based discovery rather than centralized broker registration. When a vehicle connects to a regional Zenoh router:

- The router announces the vehicle's key expression space to the rest of the router mesh via gossip
- Publishers and subscribers interested in that vehicle's data re-establish their interest declarations
- No central registry must be updated for every connection event

This distributes the reconnection load across the router mesh proportionally to fleet size — rather than concentrating it at a central broker.

**Recommended backoff configuration for vehicle clients:**

```json5
// zenoh config for vehicle ECU — connection with jittered backoff
{
  connect: {
    endpoints: ["quic/fleet-gw.example.com:7447"],
    timeout_ms: 5000,
    retry: {
      period_init_ms: 1000,
      period_max_ms: 30000,
      period_increase_factor: 2.0
    }
  },
  transport: {
    unicast: {
      lowlatency: false,
      qos: { enabled: true }
    }
  }
}
```

Adding random jitter (`period_init_ms` should be randomized per-vehicle using the VIN as seed) prevents synchronized reconnection even from geographically co-located vehicles.

*(Source: "How is Zenoh addressing the current V2X challenges" — video `4udbGc4N6-E`; "Transforming Automotive Communication with Zetta Auto" — video `BGJRHCOBtSE`)*

---

## 4. AUTOSAR Adaptive Platform Integration

AUTOSAR (AUTomotive Open System ARchitecture) defines two standards:

- **AUTOSAR Classic**: Static, compile-time configured middleware for deeply embedded ECUs (engine control, ABS, airbags). Uses SOME/IP for on-vehicle Ethernet communication. Suitable for safety-critical ASIL-D functions.
- **AUTOSAR Adaptive**: Dynamic, runtime-configurable middleware for high-compute ECUs (ADAS processing, infotainment, gateway functions). Based on ara::com API, typically implemented over DDS.

### The AUTOSAR Adaptive Problem

AUTOSAR Adaptive with DDS brings substantial resource consumption. DDS discovery alone generates significant multicast traffic. On embedded hardware with constrained RAM and no multicast-capable interfaces, standard DDS implementations are impractical. ZettaScale addressed this directly by building Zenoh as a lighter alternative.

### AUTOSAR Concept Mapping to Zenoh

AUTOSAR Adaptive's communication model is service-oriented. Applications declare services via ara::com and communicate through service instances. Zenoh maps to these concepts cleanly:

| AUTOSAR Adaptive Concept | Zenoh Mapping |
|--------------------------|--------------|
| `ara::com::proxy::ServiceProxy` | `session.declare_subscriber(ke)` |
| `ara::com::skeleton::ServiceSkeleton` | `session.declare_publisher(ke)` |
| SOME/IP EventGroup (publish-subscribe) | Zenoh pub/sub on KE namespace |
| SOME/IP Method (request-response) | Zenoh queryable with `get()` |
| Service discovery (SD) | Zenoh scouting / gossip discovery |
| ara::com field (value + notification) | Zenoh publisher + storage alignment |

A SOME/IP event group publishing radar distance data on service instance `0x1234` maps naturally to a Zenoh topic `vehicle/sensors/radar/front/distance`. Consumers declare subscribers on the same key expression without needing to know the originating service instance ID.

### AUTOSAR Classic Integration via Xenopico

For deeply embedded AUTOSAR Classic ECUs, ZettaScale provides **Xenopico** — a Zenoh Pico variant with AUTOSAR Classic bindings. Xenopico allows ECU developers to work with AUTOSAR Classic's ara::com-style abstractions while maintaining full DDS interoperability with microprocessor-based ECUs running AUTOSAR Adaptive.

Xenopico runs on:
- Arduino class hardware
- Zephyr RTOS
- FreeRTOS
- Bare metal environments
- AUTOSAR Classic OS

This enables a unified communication stack from the deepest embedded controller through gateway ECUs to cloud services, without requiring protocol bridges at each layer.

### In-Vehicle Zenoh Topology for AUTOSAR

```
┌─────────────────────────────────────────────────────────────────┐
│                          Vehicle                                 │
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│  │  AUTOSAR     │    │  AUTOSAR     │    │   Gateway ECU    │  │
│  │  Classic ECU │    │  Adaptive ECU│    │   (zenoh router) │  │
│  │  Xenopico    │◄──►│  zenoh peer  │◄──►│                  │◄─┼──► Cloud
│  │  (ASIL-D)    │    │  (ADAS)      │    │   Zenoh + TSN    │  │
│  └──────────────┘    └──────────────┘    └──────────────────┘  │
│                                                                  │
│  ◄────────────── Zenoh keyspace ─────────────────────────────►  │
└─────────────────────────────────────────────────────────────────┘
```

*(Source: "Zenoh for Software Defined Vehicle Architectures" — video `_WB7bOHUErU`; "Transforming Automotive Communication with Zetta Auto" — video `BGJRHCOBtSE`)*

---

## 5. uProtocol Architecture — GM and Toyota

### What is Eclipse uProtocol

Eclipse uProtocol is an application-layer protocol specification developed by General Motors and contributed to the Eclipse Foundation. It defines a vendor-neutral communication API for Software Defined Vehicles that abstracts applications away from the underlying transport. An application written against the uProtocol API works unchanged whether the transport is MQTT, DDS, SOME/IP, or Zenoh.

The motivation is specific to automotive: a vehicle sold today will be on the road for 20+ years. The underlying transport middleware will change multiple times over that lifetime, but the application logic (and the customer-facing APIs exposed by the vehicle) must remain stable.

Without uProtocol, changing middleware requires rewriting every application that uses it. With uProtocol, only the transport binding changes — application code is untouched.

### uProtocol's Three-Layer Architecture

```
┌──────────────────────────────────────────┐
│           Application Layer               │
│  uEntity, uResource, uTopic (stable API)  │
├──────────────────────────────────────────┤
│           Protocol Layer                  │
│  Message format, addressing, routing      │
├──────────────────────────────────────────┤
│           Transport Layer                 │
│  Zenoh / MQTT / SOME/IP / DDS bindings   │
└──────────────────────────────────────────┘
```

- **uEntity**: A named, versioned software service (e.g., `body.lamps/1`)
- **uResource**: A specific capability of a service (e.g., `door.front_left/open`)
- **uTopic**: The combination of uEntity + uResource forming a complete address

### Mapping uProtocol Addresses to Zenoh Key Expressions

uProtocol addresses map directly to Zenoh key expressions:

| uProtocol Address | Zenoh Key Expression |
|-------------------|---------------------|
| `//vehicle.vin/body.lamps/1/door.front_left` | `vehicle/<vin>/body/lamps/v1/door/front_left` |
| `//cloud.backend/ota/1/updates` | `ota/<vin>/updates` |
| `//vehicle.vin/chassis/1/speed` | `vehicle/<vin>/chassis/v1/speed` |

The Zenoh uProtocol transport plugin translates between uProtocol message format and Zenoh publications/subscriptions automatically. Applications use the uProtocol API; Zenoh carries the data.

### GM's Deployment Rationale

*(Source: "Zenoh User Meeting 2023 x Steven Hartley (General Motors)" — video `jD4bk1ur9q8`)*

GM identified that their current approach required 150 engineers across 10 time zones over 3 years to add simple mobile features to a vehicle. The root cause was protocol heterogeneity: SOME/IP for mechatronics, proprietary protocols for cloud, separate MQTT infrastructure for IoT telemetry, and custom solutions for each mobile integration.

Each new feature required engineers who understood all protocol layers at all integration points. With uProtocol + Zenoh:

1. A developer writes application logic against the uProtocol API
2. The Zenoh transport plugin carries messages to wherever the subscriber is — in-vehicle, edge, or cloud
3. No protocol bridging code is written by the application developer
4. The same application binary works across trim levels (different hardware configurations) because the transport is resolved at runtime

GM is co-developing the uProtocol Zenoh transport with ZettaScale engineers. Other OEMs participating in the Eclipse SDV working group include Mercedes, Volkswagen, BMW, and Continental.

### Woven by Toyota: The Bridge Pattern

*(Source: "Zenoh User Meeting 2024 x Pete LeVasseur (Woven by Toyota)" — video `PxA6amv5CX4`)*

Woven by Toyota (Toyota's software subsidiary) uses a different integration pattern. The in-vehicle communication bus runs native uProtocol over an IP transport suited to the vehicle's safety architecture. The cloud backbone runs Zenoh. A **uProtocol bridge** connects the two:

```
┌─────────────────────────────┐         ┌────────────────────────┐
│         Vehicle              │         │          Cloud          │
│                              │         │                        │
│  ECU  ──┐                   │         │  Fleet services        │
│  ECU  ──┤  uProtocol bus    │         │  Digital twin          │
│  ECU  ──┤  (IP transport)   │◄──────►│  OTA orchestration     │
│  ECU  ──┘         │         │  Zenoh  │  Analytics pipeline    │
│               uProtocol     │  QUIC   │                        │
│               bridge        │         │  Zenoh router cluster  │
│               (Zenoh plugin)│         └────────────────────────┘
└─────────────────────────────┘
```

The bridge is implemented as a Zenoh plugin loaded by the vehicle's gateway Zenoh router. It translates uProtocol messages from the internal bus into Zenoh publications for the cloud backbone, and vice versa. Vehicle-internal software uses uProtocol APIs; cloud services use Zenoh APIs; the bridge handles the translation transparently.

This pattern allows vehicle-internal software (which may have safety certifications tied to specific transport implementations) to remain unchanged as the cloud transport evolves.

### Rust and Memory Safety in uProtocol

Both GM and Woven by Toyota implementations use Rust as the primary language for uProtocol and Zenoh integration code. The safety rationale is concrete: Microsoft reported that approximately 70% of all CVEs across their codebase were caused by memory safety issues. Rust's borrow checker prevents use-after-free, buffer overflow, and null pointer dereference at compile time — the same class of vulnerability exploited in the Tesla hack (French security researchers exploited an out-of-bounds memory access).

Ferris Systems provides an ISO 26262-qualified Rust toolchain with signed documentation, enabling production use in safety-certified automotive systems. The Rust Safety Critical Consortium is developing coding guidelines and SAE task force materials to establish Rust in formal functional safety standards.

---

## 6. Eclipse SDV Fleet Management Blueprint

### Eclipse SDV Working Group

The Eclipse Software Defined Vehicle working group is a cross-industry initiative including Volkswagen, General Motors, Continental, ZF, and Microsoft. Its goal is to define an open, modular vehicle software platform — the non-differentiating infrastructure layer on which OEMs compete through features rather than fighting to build basic middleware.

*(Source: "Zenoh User Meeting 2023 x Sara Gallian (Eclipse Software Defined Vehicle)" — video `zgUmUnZ7rj4`)*

The working group produces **blueprints**: reference architectures with working code that demonstrate how Eclipse SDV components integrate. The Fleet Management System (FMS) blueprint is the most developed.

### Fleet Management System Blueprint Architecture

*(Source: "Integrating Zenoh into Eclipse SDV's Fleet Management System (FMS) Blueprint" — video `LjK-_mhIoeA`)*

The FMS blueprint solves a specific problem: truck fleet operators need continuous visibility into vehicle signals (speed, fuel, diagnostics, location) across a geographically distributed fleet, and need to send commands back to vehicles (route changes, configuration updates, OTA triggers).

The blueprint's architecture:

```
Vehicle
├── Sensor ECUs (CAN/SOME/IP)
│       │
│   CUXA data broker
│   (normalizes signals → VSS format)
│       │
│   Zenoh Pico client (on gateway ECU)
│       │
└── [cellular/Wi-Fi uplink]
        │
   Regional edge router
   (Zenoh router at MEC node)
        │
   Cloud Zenoh router cluster
   ├── InfluxDB backend (via zenoh-backend-influxdb)
   ├── Grafana dashboards (queries InfluxDB)
   ├── FMS API services (Zenoh subscribers)
   └── OTA orchestration service (Zenoh publisher)
```

**CUXA** (a data broker component in the blueprint) normalizes heterogeneous vehicle signals into VSS (COVESA Vehicle Signal Specification) format. VSS provides engineers across all services with a common vocabulary for vehicle data: `Vehicle.Speed`, `Vehicle.Powertrain.FuelSystem.Level`, `Vehicle.OBD.EngineLoad`, etc. This standardization means a fleet monitoring service written for one vehicle model works across all models that emit standard VSS signals.

Zenoh carries the VSS-formatted data from the vehicle's gateway ECU through the edge and to cloud services. The same pub/sub model works at each hop — there is no protocol conversion between the vehicle gateway and the cloud analytics pipeline.

### VSS Key Expression Mapping

VSS signal names map naturally to Zenoh key expressions:

```
Vehicle.Speed                    → fleet/<vin>/v/speed
Vehicle.Powertrain.FuelLevel     → fleet/<vin>/v/powertrain/fuel_level
Vehicle.OBD.EngineLoad           → fleet/<vin>/v/obd/engine_load
Vehicle.CurrentLocation.Latitude → fleet/<vin>/v/location/lat
Vehicle.Chassis.Odometer         → fleet/<vin>/v/chassis/odometer
```

Fleet-wide subscriptions use wildcards:

```python
# Subscribe to speed telemetry from all vehicles
session.declare_subscriber("fleet/*/v/speed", callback)

# Subscribe to all telemetry from a specific vehicle
session.declare_subscriber("fleet/VIN1234567890ABCDEF/v/**", callback)

# Subscribe to location from an entire regional fleet segment
session.declare_subscriber("fleet/*/v/location/**", callback)
```

### Key KE Patterns Used in the FMS Blueprint

```
# Telemetry (vehicle → cloud)
fleet/<vin>/v/<vss_signal_path>

# Commands (cloud → vehicle)
fleet/<vin>/cmd/<command_name>

# Status and health (vehicle → cloud)
fleet/<vin>/status/<component>

# OTA update orchestration (cloud → vehicle)
ota/<vin>/trigger
ota/<vin>/package/<update_id>
ota/<vin>/status

# Digital twin queries (cloud → storage)
fleet/<vin>/twin/**
```

### Zetta Platform Integration

The Zetta platform (ZettaScale's managed offering) provides a control plane over the Zenoh infrastructure. For fleet management, it offers:

- Centralized provisioning of Zenoh router configurations across the vehicle fleet
- Monitoring of router health, message rates, and routing topology
- Access control policy management (which VINs can publish to which key expressions)
- Geographic distribution management for edge router placement

From an operator's perspective, the Zetta platform abstracts away the complexity of managing thousands of Zenoh routers while preserving the full flexibility of Zenoh's data model.

---

## 7. Zetta Auto: Safety-Critical DDS Replacement

*(Source: "Transforming Automotive Communication with Zetta Auto in Software Defined Vehicles" — video `BGJRHCOBtSE`)*

### What Zetta Auto Is

Zetta Auto is a joint platform developed by ZettaScale and TTTech Auto targeting next-generation SDV deployments. It consists of two editions:

- **Zetta Auto Professional**: Full-featured, flexible edition for development and testing. Supports dynamic configuration, rapid iteration, and integration with development tools.
- **Zetta Auto Certified**: Safety-certified edition (ISO 26262) for production deployment. Configurations are frozen at build time to enable offline static analysis and deterministic behavior arguments.

The distinction between editions reflects a fundamental automotive requirement: development environments need flexibility; production safety-critical systems need analyzability and determinism. Zetta Auto Professional gives developers the DX they need; Zetta Auto Certified gives safety engineers the properties they need to certify the system.

### ISO 26262 ASIL-D Requirements

ISO 26262 is the automotive functional safety standard. ASIL (Automotive Safety Integrity Level) ratings range from A (lowest) to D (highest). ASIL-D covers safety functions where failure could cause life-threatening consequences: braking, steering, airbag deployment.

Requirements that affect middleware for ASIL-D functions:

1. **Deterministic behavior**: The system must behave identically given identical inputs. Non-deterministic scheduling, dynamic memory allocation, and runtime configuration changes are disallowed.
2. **Freedom from interference**: A safety-critical function must not be affected by failures in non-safety-critical components (mixed criticality isolation).
3. **Analyzability**: The system must be amenable to static analysis. Declarative, frozen configurations satisfy this requirement; dynamic code does not.
4. **Fault tolerance**: The system must tolerate single-point failures and transition to a safe state.

Zetta Auto Certified satisfies these requirements by:
- Freezing Zenoh router and transport configurations at build time
- Using IPC separation between safety and non-safety communication paths
- Providing offline analyzability through declarative YAML configuration files
- Supporting timing contracts for guaranteed worst-case latency bounds

### Time-Sensitive Networking Integration

TTTech Auto contributed Time-Sensitive Networking (TSN) integration to Zetta Auto. TSN is a set of IEEE 802.1 standards that provides deterministic, real-time behavior over standard Ethernet:

- **IEEE 802.1Qbv (Time-Aware Shaper)**: Time-scheduled transmission gates ensure safety-critical frames are sent in reserved time slots
- **IEEE 802.1CB (Frame Replication)**: Frame duplication across redundant paths eliminates single-point network failure
- **IEEE 802.1AS (gPTP)**: Precise time synchronization across all network nodes

Zetta Auto integrates Zenoh's QoS priority system with TSN scheduling:

| Zenoh Priority | TSN Traffic Class | Use Case |
|---------------|-------------------|----------|
| RealTime | Class A (< 4ms latency) | Brake commands, steering inputs |
| InteractiveHigh | Class B (< 10ms) | ADAS sensor fusion |
| InteractiveLow | Class C (< 50ms) | HMI events |
| DataHigh | Best Effort | Infotainment, logging |
| Background | Best Effort | OTA updates |

The Zenoh QoS configuration for a safety-critical brake control publisher:

```json5
{
  transport: {
    unicast: {
      qos: { enabled: true }
    }
  }
}
```

```rust
// Rust: publishing brake command with RealTime priority
let publisher = session
    .declare_publisher("vehicle/chassis/brakes/cmd")
    .priority(Priority::RealTime)
    .reliability(Reliability::Reliable)
    .await?;

publisher.put(brake_command_bytes).await?;
```

### DDS and Zenoh Interoperability

Zetta Auto does not replace DDS — it integrates it. Eclipse CycloneDDS provides the AUTOSAR Adaptive-compatible DDS API that developers and tools already use. Zenoh handles the V2X and cloud transport layers that DDS cannot address.

The integration is transparent: CycloneDDS applications use the standard DDS API; Zenoh carries the data where DDS cannot reach; the protocol bridge operates as a Zenoh plugin that requires no changes to application code.

---

## 8. Zenoh-Flow for Autonomous Driving Pipelines

*(Source: "Zenoh for Software Defined Vehicle Architectures" — video `_WB7bOHUErU`)*

### What Zenoh-Flow Is

Zenoh-Flow is a declarative dataflow framework for building distributed data processing pipelines on top of Zenoh. It is particularly suited to autonomous driving perception and sensor fusion pipelines, which require:

- Deterministic execution order when multiple sensors contribute to one decision
- Zero-copy data transfer between co-located processing nodes
- Dynamic pipeline reconfiguration without restarting the entire system
- Geographic distribution of computation (some processing on ECU, some on roadside GPU, some in cloud)

A Zenoh-Flow pipeline is described in YAML:

```yaml
# Autonomous driving perception pipeline
flow: perception_pipeline

sources:
  - id: camera_front
    uri: zenoh://vehicle/sensors/camera/front
    outputs: [raw_frame]

  - id: lidar_roof
    uri: zenoh://vehicle/sensors/lidar/roof
    outputs: [point_cloud]

operators:
  - id: object_detection
    uri: file:///opt/adas/object_detection.so
    inputs: [raw_frame]
    outputs: [detections]

  - id: sensor_fusion
    uri: file:///opt/adas/sensor_fusion.so
    inputs: [detections, point_cloud]
    outputs: [fused_scene]

  - id: path_planner
    uri: file:///opt/adas/path_planner.so
    inputs: [fused_scene]
    outputs: [trajectory]

sinks:
  - id: drive_controller
    uri: zenoh://vehicle/chassis/trajectory_cmd
    inputs: [trajectory]
```

### Zero-Copy Optimization

When two Zenoh-Flow nodes run on the same ECU, Zenoh-Flow uses shared memory (SHM) to pass data between them. The `raw_frame` output from `camera_front` is placed in SHM; `object_detection` reads it directly without any copy. When nodes are distributed across ECUs or to the cloud, standard Zenoh serialization takes over automatically.

The application code does not change between co-located and distributed deployments. The Zenoh-Flow runtime resolves the transport based on the deployment topology at launch time.

### Data Flow Determinism vs. ROS 2

In ROS 2's pure event-driven model, a sensor fusion node is called whenever any of its inputs publishes. This causes:

- Race conditions when two sensors publish at slightly different times
- Non-deterministic execution order when inputs arrive out of expected sequence
- Spurious wakeups when a node processes incomplete data

Zenoh-Flow only dispatches a node when **all** of its declared inputs have data available for the current processing cycle. The `sensor_fusion` node above waits until both `detections` (from camera) and `point_cloud` (from lidar) are available before executing. This eliminates the race condition entirely and makes the execution order deterministic — a requirement for safety certification.

---

## 9. TTTech Auto: Deterministic Execution and ISO 26262

*(Source: "Zenoh User Meeting 2023: TTTech Auto - Zenoh Flow in Automotive Safety" — video `GsEuPucS4F4`)*

TTTech Auto's MotionWise is an AUTOSAR Adaptive platform that integrates Zenoh-Flow as the data processing runtime for ADAS functions. Christopher Helpa's presentation at Zenoh User Meeting 2023 detailed the scheduling approach:

### Timing Contracts

Each Zenoh-Flow node in a safety-critical pipeline declares a **timing contract**: a maximum execution time within which the node must complete its computation.

```yaml
operators:
  - id: emergency_brake_decision
    uri: file:///opt/adas/emergency_brake.so
    inputs: [fused_scene, road_conditions]
    outputs: [brake_trigger]
    timing_contract_ms: 5   # Must complete within 5ms
    criticality: ASIL_D
```

If the node exceeds its timing contract, Zenoh-Flow's runtime takes a safe action:
- Logs the timing violation
- Allows the downstream pipeline to continue with the most recent available output
- Does not block the safety-critical output

The system trades **completeness** for **guaranteed timing** — it is better to produce an imperfect braking decision in 5ms than to produce a perfect one in 8ms. This tradeoff is explicitly designed into the safety architecture and documented in the safety case.

### Scheduling Optimization

With timing contracts declared for each node, Zenoh-Flow can perform offline heuristic scheduling analysis:

1. Build the dependency graph of the pipeline
2. Identify the critical path (longest chain of sequential dependencies)
3. Assign nodes to CPU cores to minimize idle time on the critical path

TTTech Auto measured that this offline scheduling optimization reduced end-to-end pipeline latency from 50ms to 40ms — a 20% reduction — by eliminating CPU idle time that occurred when nodes were dispatched suboptimally.

At runtime, the scheduler uses timing contract information to make adaptive dispatch decisions, preempting lower-priority nodes when higher-priority nodes are ready to execute.

### Offline Analyzability for Safety Certification

AUTOSAR Adaptive with dynamic code is difficult to certify because safety engineers cannot statically analyze what the system will do. Zenoh-Flow's YAML pipeline specification is fully declarative: it describes every node, every data dependency, every timing contract, and every data flow path.

Safety engineers can read the YAML specification and reason about system behavior without reading C++ code. This is a direct enabler for ISO 26262 certification: the safety case can reference the pipeline specification as evidence of system design, rather than requiring code-level analysis.

---

## 10. Fleet Management at Scale — GM's 20-Year Lifecycle

*(Source: "Zenoh User Meeting 2023 x Steven Hartley (General Motors)" — video `jD4bk1ur9q8`)*

### The 20-Year Software Problem

A vehicle sold in 2024 will still be on the road in 2044. Over that 20-year period:

- The cellular network will transition from 5G to at least two successor generations
- Cloud infrastructure providers will change APIs multiple times
- OTA update protocols will be revised
- Security requirements will evolve (certificate lifetimes, cipher suites, key lengths)
- Multiple owners will take possession of the vehicle, each with different connected service subscriptions

Traditional middleware is built into vehicle firmware at the factory and cannot be updated without a full ECU reflash — an operation requiring dealer service. Software-defined vehicles must support over-the-air middleware updates as routine maintenance.

### uProtocol as the Stable API Layer

GM's solution: define the application-facing API in uProtocol, which provides a stable, versioned addressing scheme independent of transport. Applications in the vehicle interact with uEntity/uResource addresses that are guaranteed stable for the vehicle's lifetime.

The transport layer beneath uProtocol can be updated without application changes. A 2024 vehicle might ship with uProtocol over SOME/IP for in-vehicle communication and uProtocol over MQTT for cloud connectivity. A 2031 OTA update might replace the cloud transport with uProtocol over Zenoh — without touching any application code.

This decoupling enables GM to:
1. Update transport middleware via OTA without affecting applications
2. Evolve security protocols (TLS cipher suites, certificate authorities) independently
3. Adapt to new network generation protocols without application code changes
4. Maintain a single application codebase across trim levels with different hardware configurations

### Multiple Ownership Transfer

When a vehicle changes ownership, subscriptions to fleet management services, dealer services, and user-specific services must transfer or terminate. uProtocol addresses include the vehicle's identity (VIN-based), enabling:

- Cloud-side ACL updates when ownership transfers (revoke old owner's access tokens, provision new owner)
- Vehicle-side credential rotation via OTA (new owner's certificate pushed to vehicle's keystore)
- Subscription migration (fleet telemetry subscriptions associated with the vehicle, not the owner)

Zenoh's ACL system (configured at the router level) can enforce these ownership boundaries without requiring application code changes.

### OTA Update Architecture

Over-the-air updates in a Zenoh-based fleet use a combination of pub/sub (for push notifications) and queries (for delta download):

```
OTA Flow:
1. Cloud publishes update manifest to:
   ota/<vin>/manifest
   (Vehicle subscribes, receives notification)

2. Vehicle queries for update packages:
   get("ota/<vin>/package/v2.1.4/**")
   (Resolves against nearest storage — edge cache or cloud)

3. Vehicle applies update and publishes status:
   ota/<vin>/status = {"version": "2.1.4", "result": "success"}

4. Cloud fleet management subscribes to:
   ota/*/status
   (Receives completion from all vehicles)
```

The query-based download step is critical: it allows edge caches (deployed at 5G MEC nodes near vehicle clusters) to serve the update package without all vehicles hitting the central cloud. A software update rolling out to 100,000 vehicles in a city can be served entirely from the regional edge cache once the cloud has populated it.

---

## 11. Production Deployment Patterns

### In-Vehicle Topology

Each ECU in the vehicle runs a Zenoh client or peer:

```
ECU Roles:
├── Deeply embedded ECUs (AUTOSAR Classic): Zenoh Pico / Xenopico
│   ├── Engine control: zenoh-pico client
│   ├── ABS/ESC: zenoh-pico client
│   └── Airbag: zenoh-pico client (read-only, ASIL-D isolation)
│
├── Domain controllers (AUTOSAR Adaptive): Zenoh peer
│   ├── ADAS domain controller: zenoh peer + Zenoh-Flow runtime
│   ├── Body domain controller: zenoh peer
│   └── Infotainment: zenoh peer
│
└── Vehicle gateway / telematics unit: Zenoh router
    ├── Routes in-vehicle traffic between domains
    ├── Manages cellular/Wi-Fi uplink to edge
    └── Enforces ACLs between safety and non-safety domains
```

The gateway ECU is the only node in the vehicle that has both in-vehicle and external connectivity. It runs a full Zenoh router with explicit ACL rules that prevent safety-critical key expressions from being accessed externally:

```json5
// Gateway router config: ACL rules
{
  access_control: {
    enabled: true,
    default_permission: "deny",
    rules: [
      // Safety-critical KEs: local ECUs only
      {
        id: "safety-local-only",
        messages: ["put", "declare_subscriber"],
        key_exprs: ["vehicle/chassis/brakes/**", "vehicle/chassis/steering/**"],
        flows: ["ingress", "egress"],
        permission: "allow",
        subject: { interfaces: ["lo", "eth_internal"] }
      },
      // Telemetry: allow egress to cloud only
      {
        id: "telemetry-cloud-egress",
        messages: ["put"],
        key_exprs: ["fleet/<vin>/v/**"],
        flows: ["egress"],
        permission: "allow",
        subject: { interfaces: ["wwan0", "wlan0"] }
      },
      // Commands: allow ingress from cloud only
      {
        id: "commands-cloud-ingress",
        messages: ["put"],
        key_exprs: ["fleet/<vin>/cmd/**", "ota/<vin>/**"],
        flows: ["ingress"],
        permission: "allow",
        subject: { cert_common_names: ["fleet-ota.example.com"] }
      }
    ]
  }
}
```

### Edge (Roadside Unit / MEC Node)

Regional edge nodes serve as Zenoh routers that aggregate traffic from vehicles in their coverage area:

```json5
// Edge router config
{
  listen: {
    endpoints: [
      "quic/0.0.0.0:7447",   // Vehicle uplink (QUIC for reconnection resilience)
      "tcp/0.0.0.0:7448"     // Cloud downlink (TCP for reliability)
    ]
  },
  plugins: {
    storage_manager: {
      storages: {
        // Cache VSS telemetry for 1 hour (serves OTA package queries locally)
        vehicle_telemetry: {
          key_expr: "fleet/**/v/**",
          volume: { id: "influxdb", db: "telemetry_cache" },
          garbage_collection_period: 3600
        },
        ota_packages: {
          key_expr: "ota/**/package/**",
          volume: { id: "filesystem", dir: "/var/zenoh/ota-cache" }
        }
      }
    }
  }
}
```

### Cloud Router Cluster

The cloud tier runs a Zenoh router cluster with geographic distribution:

```
Cloud Topology:
├── us-west router cluster (handles West coast vehicles)
│   ├── router-us-west-1 (primary)
│   ├── router-us-west-2 (failover)
│   └── router-us-west-3 (failover)
│
├── us-east router cluster
├── eu-central router cluster
└── ap-southeast router cluster

Inter-cluster gossip: router mesh connects all regions
Fleet management services connect to nearest cluster as Zenoh clients
```

Each cloud router cluster uses the `connect` section to establish the router mesh:

```json5
{
  connect: {
    endpoints: [
      "tcp/router-us-east-1.internal:7447",
      "tcp/router-eu-central-1.internal:7447"
    ],
    retry: { period_init_ms: 500, period_max_ms: 10000 }
  },
  scouting: {
    gossip: {
      enabled: true,
      autoconnect: { router: "router" }
    }
  }
}
```

---

## 12. Security and mTLS per Vehicle

### Certificate-per-Vehicle Architecture

Each vehicle has a unique TLS client certificate issued from the fleet's PKI. The Common Name or Subject Alternative Name encodes the VIN:

```
Subject: CN=VIN1234567890ABCDEF, O=FleetOperator, C=US
SAN: DNS:vin1234567890abcdef.vehicles.fleet.example.com
```

Zenoh router TLS configuration enforcing mTLS:

```json5
{
  transport: {
    unicast: {
      tls: {
        root_ca_certificate: "/etc/zenoh/fleet-root-ca.pem",
        listen_private_key: "/etc/zenoh/router-key.pem",
        listen_certificate: "/etc/zenoh/router-cert.pem",
        verify_client_certificate: true,  // Require vehicle cert
        client_auth: true
      }
    }
  }
}
```

### ACL Enforcement by VIN

Because the vehicle's VIN is in its certificate Common Name, the Zenoh router can enforce key expression ACLs per vehicle:

```json5
{
  access_control: {
    rules: [
      {
        // Vehicles can only publish to their own VIN namespace
        messages: ["put"],
        key_exprs: ["fleet/**"],
        flows: ["ingress"],
        permission: "deny"
        // Overridden by vehicle-specific rule matching CN
      }
    ]
  }
}
```

In practice, per-vehicle ACL rules are provisioned by the fleet management system when a vehicle registers. The Zetta platform automates this provisioning.

### Certificate Rotation

Vehicle certificates have defined lifetimes. Rotation requires:

1. Cloud pushes new certificate to vehicle via `ota/<vin>/cert_rotation`
2. Vehicle stores new certificate in secure enclave
3. Vehicle reconnects using new certificate
4. Cloud revokes old certificate

Zenoh's QUIC transport supports connection migration, enabling the certificate rotation reconnection to complete without data loss on active subscriptions.

---

## 13. Key Expression Patterns for Vehicle Fleets

A consistent KE naming convention across all services reduces integration friction. The following patterns are derived from the Eclipse SDV FMS Blueprint and GM uProtocol mapping:

### Telemetry (Vehicle → Cloud)

```
fleet/<vin>/v/<vss_path>

Examples:
fleet/VIN1234567890ABCDEF/v/speed
fleet/VIN1234567890ABCDEF/v/powertrain/fuel_level
fleet/VIN1234567890ABCDEF/v/location/lat
fleet/VIN1234567890ABCDEF/v/location/lon
fleet/VIN1234567890ABCDEF/v/obd/engine_load
fleet/VIN1234567890ABCDEF/v/chassis/odometer
fleet/VIN1234567890ABCDEF/v/battery/state_of_charge  # EV
```

### Commands (Cloud → Vehicle)

```
fleet/<vin>/cmd/<command>

Examples:
fleet/VIN1234567890ABCDEF/cmd/door_unlock
fleet/VIN1234567890ABCDEF/cmd/horn_activate
fleet/VIN1234567890ABCDEF/cmd/climate/target_temp
fleet/VIN1234567890ABCDEF/cmd/charge_schedule
```

### Status and Health

```
fleet/<vin>/status/<component>

Examples:
fleet/VIN1234567890ABCDEF/status/engine
fleet/VIN1234567890ABCDEF/status/connectivity
fleet/VIN1234567890ABCDEF/status/adas_system
fleet/VIN1234567890ABCDEF/status/battery
```

### OTA Updates

```
ota/<vin>/manifest          # Cloud pushes update notification
ota/<vin>/package/<id>/**   # Vehicle queries for package data
ota/<vin>/status            # Vehicle publishes update result
ota/<vin>/rollback          # Cloud triggers rollback
```

### Digital Twin Queries

```
fleet/<vin>/twin/**         # Query resolves against stored last-known state
fleet/<vin>/twin/v/speed    # Last known speed (queryable)
fleet/<vin>/twin/status/**  # Last known component status
```

### Fleet-Wide Subscriptions

```python
# All vehicles' speed
session.declare_subscriber("fleet/*/v/speed", on_speed)

# All low-fuel vehicles (requires server-side filtering or application-level filtering)
session.declare_subscriber("fleet/*/v/powertrain/fuel_level", on_fuel)

# All vehicles in a geographic region (handled by routing topology, not KE)
# Configure edge routers for the region to forward fleet/*/v/** to regional services

# All OTA completion events
session.declare_subscriber("ota/*/status", on_ota_complete)
```

### uProtocol-style Service Addressing

For GM uProtocol deployments where the application layer uses uEntity/uResource addressing:

```
vehicle/<vin>/<uentity>/<version>/<uresource>/<message>

Examples:
vehicle/VIN1234567890ABCDEF/body.lamps/v1/front_left/state
vehicle/VIN1234567890ABCDEF/chassis.brakes/v1/front_left/pressure
vehicle/VIN1234567890ABCDEF/adas.parking/v2/proximity/front
```

The Zenoh uProtocol transport plugin translates between this KE structure and uProtocol's native addressing at the bridge layer, with no application code changes required.

---

## Summary

| Use Case | Company | Pattern |
|----------|---------|---------|
| In-vehicle pub/sub replacing DDS | TTTech Auto / Zetta Auto | Zenoh peer on each ECU, Zenoh router on gateway |
| V2X at fleet scale | Multiple OEMs | Zenoh + QUIC, edge routers at MEC nodes |
| TLS storm avoidance | Any fleet operator | Replace MQTT+TCP with Zenoh+QUIC |
| AUTOSAR Classic ECUs | ZettaScale / Xenopico | Zenoh Pico with AUTOSAR bindings |
| Stable API across vehicle lifetime | General Motors | uProtocol over Zenoh transport |
| In-vehicle → cloud bridge | Woven by Toyota | uProtocol bridge plugin in gateway router |
| Fleet management | Eclipse SDV FMS Blueprint | VSS + Zenoh + InfluxDB storage backend |
| Autonomous driving pipeline | TTTech Auto / Zenoh-Flow | Declarative dataflow with timing contracts |
| ISO 26262 ASIL-D | Zetta Auto Certified | Frozen config + TSN integration + Rust |

Zenoh's single-protocol approach — spanning microcontrollers to cloud without protocol bridges — is what enables it to serve as the communication backbone for the full SDV architecture. DDS handles in-vehicle safety-critical communication where standards compliance is required. MQTT handles legacy IoT integrations. Zenoh handles everything else, and bridges the gaps between them.

## See Also

- [Node Types Guide](node-types-guide.md) — the router/peer/client topology patterns central to the hub-and-spoke ECU architectures here
- [QoS Guide](qos-guide.md) — priority and congestion control for safety-critical vs telemetry traffic separation
- [Shared Memory Complete Guide](shared-memory-complete-guide.md) — zero-copy IPC between ECUs on the same compute node
- [Performance Tuning Guide](performance-tuning-guide.md) — how to configure Zenoh for the latency bounds required by automotive safety
- [Zenoh Pico Guide](zenoh-pico-guide.md) — the embedded C implementation used on microcontroller ECUs
