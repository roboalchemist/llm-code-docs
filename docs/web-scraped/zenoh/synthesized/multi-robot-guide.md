# Multi-Robot Fleet Management with Zenoh

## Table of Contents

- [Overview](#overview)
- [The OEM Walled Garden Problem](#the-oem-walled-garden-problem)
  - [Wall 1: The Network Wall](#wall-1-the-network-wall)
  - [Wall 2: The Protocol Wall](#wall-2-the-protocol-wall)
  - [Wall 3: The Data Model Wall](#wall-3-the-data-model-wall)
- [Topic Scoping for Robot Isolation](#topic-scoping-for-robot-isolation)
  - [The Namespace Collision Problem](#the-namespace-collision-problem)
  - [Per-Robot Namespace Configuration](#per-robot-namespace-configuration)
  - [Fleet Manager Subscription Patterns](#fleet-manager-subscription-patterns)
  - [Using rviz2 with a Specific Robot](#using-rviz2-with-a-specific-robot)
- [Hierarchical Zenoh Routing for Large Fleets](#hierarchical-zenoh-routing-for-large-fleets)
  - [Three-Tier Architecture](#three-tier-architecture)
  - [Robot Tier: Client Mode](#robot-tier-client-mode)
  - [Site Router Tier: Router Mode](#site-router-tier-router-mode)
  - [Cloud Router Tier: Root Router](#cloud-router-tier-root-router)
  - [Traffic Patterns by Tier](#traffic-patterns-by-tier)
- [Scaling from 40 to 200 Robots: The Tractonomy Case Study](#scaling-from-40-to-200-robots-the-tractonomy-case-study)
  - [40-Robot Pilot: Flat Topology Works](#40-robot-pilot-flat-topology-works)
  - [100-Robot Scale: Discovery Overhead and Connection Storms](#100-robot-scale-discovery-overhead-and-connection-storms)
  - [200-Robot Production: Hierarchical Topology with QoS](#200-robot-production-hierarchical-topology-with-qos)
- [2GB/s Multicast Spike Elimination](#2gbs-multicast-spike-elimination)
  - [The Root Cause: SPDP Multicast](#the-root-cause-spdp-multicast)
  - [Zenoh's Solution: Linkstate Gossip](#zenohs-solution-linkstate-gossip)
  - [Warehouse Wi-Fi Configuration for Large Fleets](#warehouse-wi-fi-configuration-for-large-fleets)
- [Unconstrained Connectivity: NAT Traversal and Peer-to-Peer](#unconstrained-connectivity-nat-traversal-and-peer-to-peer)
  - [QUIC-Based NAT Hole-Punching](#quic-based-nat-hole-punching)
  - [Peer-to-Peer Without Infrastructure](#peer-to-peer-without-infrastructure)
  - [Dynamic Topology: Robots Joining and Leaving](#dynamic-topology-robots-joining-and-leaving)
  - [Offline Operation](#offline-operation)
- [Multi-Site Fleet Management](#multi-site-fleet-management)
  - [Topology: 5-Site Deployment](#topology-5-site-deployment)
  - [WAN QoS: Rate Limiting for Bandwidth-Constrained Links](#wan-qos-rate-limiting-for-bandwidth-constrained-links)
  - [Data Locality](#data-locality)
  - [Gossip Scouting vs. Static Endpoints for WAN](#gossip-scouting-vs-static-endpoints-for-wan)
- [Fleet Manager Patterns in Python](#fleet-manager-patterns-in-python)
  - [Complete Fleet Manager Example](#complete-fleet-manager-example)
  - [Robot-Side Liveliness Token](#robot-side-liveliness-token)
  - [Leader Election for Fleet Coordinator](#leader-election-for-fleet-coordinator)
- [Configuration Reference Summary](#configuration-reference-summary)
  - [Per-Robot Bridge Config Template](#per-robot-bridge-config-template)
  - [Site Router Config Template](#site-router-config-template)
  - [Cloud Router Config Template](#cloud-router-config-template)
- [Operational Checklist](#operational-checklist)

## Overview

Managing a fleet of robots presents three fundamental integration challenges that most middleware stacks handle poorly: network isolation between robots and operators, protocol mismatches between OEM systems and fleet software, and topic namespace collisions when multiple robots publish identical ROS topic names. Zenoh addresses all three through a combination of transport-agnostic routing, native protocol bridging, and namespace scoping built into the `zenoh-bridge-ros2dds` plugin.



This guide covers the complete architecture for multi-robot fleet deployment, from 2-robot setups to 200-robot production fleets, drawing on real deployments including Tractonomy's warehouse automation fleet and The Construct's cloud-based multi-robot lab.

---

## The OEM Walled Garden Problem

When deploying a heterogeneous robot fleet—mixing robots from different vendors or generations—three walls prevent seamless integration:

### Wall 1: The Network Wall

OEMs often lock robots to proprietary network configurations. The robot may only communicate over a private Wi-Fi SSID controlled by the OEM, behind NAT, or on a separate VLAN inaccessible to the fleet manager. Traditional DDS multicast discovery fails completely across network segments; it requires all participants to be on the same Layer 2 subnet.

Zenoh breaks through the network wall because it runs over any transport—TCP, UDP, TLS, QUIC—across any topology including WAN, LTE, and NAT. Two robots can discover each other or reach a fleet manager without being on the same subnet. QUIC's built-in hole-punching enables peer-to-peer sessions through NAT without infrastructure assistance.

### Wall 2: The Protocol Wall

OEM robots may use DDS, MQTT, a proprietary binary protocol, or HTTP REST for telemetry. Fleet managers typically speak a different protocol. Building custom adapters for each OEM/manager combination produces an N×M translation matrix that becomes unmaintainable.

Zenoh bridges DDS, MQTT, and REST natively through its plugin system. A `zenoh-bridge-ros2dds` on the robot side exposes all ROS 2 topics, services, and actions as zenoh key expressions. The fleet manager, which may be a native zenoh application or bridge through another protocol, communicates without any OEM-specific adapter code.

### Wall 3: The Data Model Wall

Even if two systems are connected and speak compatible protocols, their topic names and message formats differ. OEM robot A publishes `/arm/joint_states`; OEM robot B also publishes `/arm/joint_states`. The fleet manager cannot distinguish them, and cannot subscribe to one without receiving both.

Zenoh resolves the data model wall through namespace scoping: each bridge prefixes all topics with a unique robot identifier, transforming `/arm/joint_states` into `/robot/bot1/arm/joint_states`. The fleet manager subscribes to `/robot/*/arm/joint_states` using key expression wildcards to receive data from all robots simultaneously while still being able to address each individually.

---

## Topic Scoping for Robot Isolation

### The Namespace Collision Problem

Without scoping, a warehouse with ten mobile manipulators all running ROS 2 produces ten publishers all advertising `/arm/joint_states`, `/base/cmd_vel`, `/camera/image_raw`, and so on. DDS resolves this via Domain IDs, but Domain IDs are per-network-segment and do not compose across a fleet manager. Zenoh's keyspace is global across all connected endpoints, which makes the collision concrete and visible.

The collision also means commands are broadcast to all robots: publishing to `/cmd_vel` moves every robot simultaneously.

### Per-Robot Namespace Configuration

The `zenoh-bridge-ros2dds` `namespace` setting prefixes every topic, service, and action that the bridge routes to zenoh. The DDS traffic between ROS nodes on the robot itself remains unaffected—ROS nodes do not need to be reconfigured. Only the zenoh representation is scoped.

Robot 1 bridge configuration (`robot1-bridge.json5`):

```json5
{
  plugins: {
    ros2dds: {
      namespace: "robot/bot1",
      // No allow/deny filter: route everything
    }
  },
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  }
}
```

Robot 2 bridge configuration (`robot2-bridge.json5`):

```json5
{
  plugins: {
    ros2dds: {
      namespace: "robot/bot2",
    }
  },
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  }
}
```

Robot 3 bridge configuration (`robot3-bridge.json5`):

```json5
{
  plugins: {
    ros2dds: {
      namespace: "robot/bot3",
    }
  },
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  }
}
```

With these configurations (namespace `/robot/bot1` strips leading `/` to form Zenoh key prefix):
- `/arm/joint_states` on robot 1 becomes `robot/bot1/arm/joint_states` in zenoh
- `/arm/joint_states` on robot 2 becomes `robot/bot2/arm/joint_states` in zenoh
- `/tf` becomes `robot/bot1/tf`, `robot/bot2/tf`, etc.
- `/rosout`, `/parameter_events`, and all absolute ROS topic paths are also prefixed

### Fleet Manager Subscription Patterns

The fleet manager connects to all robot bridges and uses key expression wildcards:

```python
import zenoh

session = zenoh.open(zenoh.Config())

# Subscribe to joint states from ALL robots
sub_all = session.declare_subscriber(
    "robot/*/arm/joint_states",
    lambda sample: handle_joint_states(sample)
)

# Subscribe to a specific robot only
sub_bot1 = session.declare_subscriber(
    "robot/bot1/arm/joint_states",
    lambda sample: handle_bot1_joints(sample)
)
```

The `*` wildcard in `robot/*/arm/joint_states` matches exactly one path segment, so it matches `robot/bot1/arm/joint_states` but not `robot/bot1/arm/left/joint_states`. Use `**` for multi-segment matching when needed.

Sending commands to a specific robot:

```python
# Move only robot 42
session.put("robot/bot42/cmd_vel", twist_bytes)

# Broadcast to all robots (using ** wildcard key expression in publish)
# Note: zenoh pub key expressions must be concrete (no wildcards).
# Broadcast requires publishing to each robot individually, or using
# a shared command topic that all robots subscribe to:
session.put("fleet/broadcast/cmd_vel", stop_bytes)
# Each robot bridge must subscribe and remap this to its local /cmd_vel
```

### Using rviz2 with a Specific Robot

The bridge README describes two monitoring approaches:

**Option 1**: Run a bridge on the monitoring host with the target robot's namespace. The monitoring host then sees a "normal" unscoped ROS graph corresponding to that robot:

```bash
zenoh-bridge-ros2dds --namespace /robot/bot1 -e tcp/192.168.1.101:7447
# Now: ros2 topic list shows /arm/joint_states (without prefix)
# rviz2 works without remapping
```

**Option 2**: Run a bridge without namespace and remap manually in ROS tooling:

```bash
zenoh-bridge-ros2dds -e tcp/192.168.1.101:7447
# rviz2 requires explicit remapping:
rviz2 --ros-args -r /tf:=/robot/bot1/tf -r /tf_static:=/robot/bot1/tf_static
```

---

## Hierarchical Zenoh Routing for Large Fleets

As fleet size grows, a flat topology—every robot's bridge connected directly to the fleet manager—creates connection fan-out problems. A single zenoh router with 200 client connections handles discovery state for all 200 robots simultaneously.

The solution is a three-tier hierarchy that mirrors physical deployment topology.

### Three-Tier Architecture

```
Tier 3: Cloud / Datacenter
┌─────────────────────────────────────────┐
│           zenoh cloud router            │
│         cloud-router:7447               │
│  (accepts connections from site routers)│
└──────────────┬──────────────────────────┘
               │ WAN link (10-100ms)
    ┌──────────┴──────────┐
    │                     │
Tier 2: Site / Warehouse  │
┌───────────────┐  ┌──────────────────┐
│ site-A router │  │  site-B router   │
│ 192.168.1.1   │  │  192.168.2.1     │
│ :7447         │  │  :7447           │
└──┬──────────┬─┘  └────┬────────────┘
   │          │          │
Tier 1: Robot Clients
┌──────┐  ┌──────┐  ┌──────┐
│ bot1 │  │ bot2 │  │ bot3 │
│bridge│  │bridge│  │bridge│
└──────┘  └──────┘  └──────┘
```

### Robot Tier: Client Mode

Each robot's bridge runs in client mode and connects to the local site router. Client mode means the robot does not listen for incoming connections—it only dials out. This is correct for mobile robots whose IP addresses may change.

`robot-bridge.json5`:

```json5
{
  plugins: {
    ros2dds: {
      namespace: "robot/bot1",
      // Restrict what is routed to reduce bandwidth
      allow: {
        publishers: [".*/laser_scan", ".*/pose", "/tf", ".*/battery_state"],
        subscribers: [".*/cmd_vel", ".*/goal_pose"],
        service_servers: [".*/.*_parameters"],
        service_clients: [],
        action_servers: [".*/navigate_to_pose"],
        action_clients: [],
      },
      // Rate-limit high-frequency sensors to avoid saturating Wi-Fi
      pub_max_frequencies: [
        ".*/laser_scan=5",    // 5 Hz over zenoh (full rate stays local)
        "/tf=10",
        ".*/camera/image_raw=2"
      ],
      // Prioritize command topics
      pub_priorities: [
        ".*/cmd_vel=1:express",
        ".*/pose=2",
        ".*/laser_scan=5"
      ],
    }
  },
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.1:7447"]  // site router
  }
}
```

### Site Router Tier: Router Mode

The site router accepts connections from all robots on the warehouse floor and maintains a single WAN connection to the cloud router. It runs `zenohd` with no plugins.

`site-router.json5`:

```json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  },
  connect: {
    endpoints: ["tcp/cloud-router.example.com:7447"]  // cloud router
  },
  scouting: {
    multicast: {
      enabled: false  // No multicast in a managed warehouse environment
    },
    gossip: {
      enabled: true,
      multihop: false
    }
  }
}
```

### Cloud Router Tier: Root Router

The cloud router accepts connections from all site routers and hosts the fleet manager application.

`cloud-router.json5`:

```json5
{
  mode: "router",
  listen: {
    endpoints: [
      "tcp/0.0.0.0:7447",
      "tls/0.0.0.0:7448"  // TLS for WAN connections from sites
    ]
  },
  // No connect: section — sites connect to cloud, not the reverse
  scouting: {
    multicast: {
      enabled: false
    },
    gossip: {
      enabled: true,
      multihop: false
    }
  }
}
```

### Traffic Patterns by Tier

**Robot to Robot (same site)**: Data from bot1 to bot2 on the same warehouse floor travels only as far as the site router. The cloud router never sees this traffic. This is zenoh's interest-based routing in action: if no subscriber outside the site expresses interest in `/robot/bot1/laser_scan`, the site router does not forward it upstream.

**Robot to Cloud**: Robot sensor data consumed by a cloud dashboard traverses the full path: robot → site router → WAN → cloud router → fleet manager. The site router only forwards topics that have subscribers in the cloud segment.

**Cross-site robot communication**: A robot in warehouse A communicating with a robot in warehouse B routes through the cloud router. Both site routers forward only the specific topics that have cross-site subscribers.

---

## Scaling from 40 to 200 Robots: The Tractonomy Case Study

Tractonomy is a Belgian autonomous mobile robot (AMR) company that deployed zenoh in their warehouse automation fleet. Their scale-up from pilot to production revealed specific breaking points and required targeted architectural changes at each stage.

### 40-Robot Pilot: Flat Topology Works

At the 40-robot pilot stage, Tractonomy ran a flat topology: each robot's zenoh bridge connected directly to a central fleet manager. Discovery used gossip protocol over the warehouse Wi-Fi. This topology worked because:

- 40 concurrent connections is manageable for a single zenoh router
- Gossip discovery state (O(N) peers) fits comfortably in memory
- Wi-Fi contention was low enough that default batch sizes worked

All 40 robots were on a single SSID and a single subnet. DDS multicast traffic was already causing intermittent issues—adding a new robot caused a burst of SPDP multicast packets—but the fleet was small enough that the bursts were sub-second.

### 100-Robot Scale: Discovery Overhead and Connection Storms

At 100 robots the flat topology began breaking:

**Discovery storms**: When a robot rebooted or a new robot was added to the fleet, zenoh gossip propagated the new peer's existence to all 99 other robots. Each robot updated its routing table. This was not instantaneous—it produced a wave of gossip messages that briefly saturated the 2.4 GHz Wi-Fi band used for robot-to-infrastructure communication.

**Connection fan-out**: The central fleet manager was handling 100 concurrent zenoh sessions. A software update that restarted the fleet manager caused all 100 robots to attempt reconnection simultaneously—a thundering herd that took 30-60 seconds to stabilize.

**Solution**: Tractonomy introduced a two-tier hierarchy (robots → site router → fleet manager) and configured exponential reconnect backoff on robot clients:

```json5
// On robot client bridges
connect: {
  endpoints: ["tcp/192.168.1.1:7447"],
  retry: {
    period_init_ms: 1000,
    period_max_ms: 30000,
    period_increase_factor: 2,
  }
}
```

The site router absorbed reconnection attempts; the fleet manager only saw a single session per site router.

### 200-Robot Production: Hierarchical Topology with QoS

At 200 robots Tractonomy moved to a full three-tier hierarchy across two warehouse floors with a shared cloud coordinator. Key configuration changes:

**Pre-declare publishers and subscribers**: At 200 robots, late subscriber discovery (the zenoh interest protocol announcing a new subscriber to all publishers) produces noticeable latency spikes. Pre-declaring publishers at startup ensures routing tables are ready before data flows:

```python
# Pre-declare before starting the main loop
pub = session.declare_publisher("robot/bot1/pose")
sub = session.declare_subscriber("fleet/bot1/cmd", handler)
# Now pub/sub are established; first message has no discovery overhead
```

**Tune batch size for Wi-Fi**: Zenoh batches outgoing messages by default to improve throughput. On noisy warehouse Wi-Fi, large batches increase latency jitter. Tractonomy tuned batch size down for robot clients while keeping large batches on the wired site-to-cloud links.

**Strict topic allowlists**: At 200 robots, an unfiltered bridge that routes all ROS topics would push dozens of MB/s over Wi-Fi. Using `allow` filters on each bridge reduced per-robot Wi-Fi utilization to ~50 KB/s for status telemetry and ~500 KB/s for active navigation.

**QoS priority differentiation**: Emergency stop commands and safety-critical topics used `pub_priorities` with `express` mode; bulk map data and diagnostics used background priority (7) to avoid contending with safety traffic.

---

## 2GB/s Multicast Spike Elimination

This problem was documented at The Construct, a cloud-based robotics education platform that provides multi-robot simulation environments to students worldwide. They ran large ROS 2 environments with many robots and initially used standard DDS (Fast DDS) for all inter-robot communication.

### The Root Cause: SPDP Multicast

DDS uses the Simple Participant Discovery Protocol (SPDP) to announce participants on a network. Every DDS participant (each ROS node is a DDS participant) periodically multicast-broadcasts an SPDP announcement. When a new participant joins, it multicasts an announcement, and every existing participant unicasts a response directly back.

In a fleet of N robots each running M ROS nodes, adding one new robot produces N×M unicast responses. With 40 robots each running 8 ROS nodes (a conservative estimate for a navigation stack), adding robot 41 produces 40 × 8 = 320 simultaneous unicast packets, each triggering TCP connection establishment if the new participant is on a different host.

At The Construct, students would join their lab sessions and spin up 10-20 robots simultaneously. The initial SPDP storm from 20 robots each with multiple nodes would produce bandwidth spikes exceeding 2 GB/s on the lab network—enough to cause packet loss and crash other students' sessions.

### Zenoh's Solution: Linkstate Gossip

Zenoh has no concept of SPDP. Discovery uses gossip protocol: each zenoh session tells its directly connected neighbors what key expressions it is interested in. Neighbors propagate this information one hop at a time. There is no multicast response storm.

When robot 41 joins a 40-robot zenoh fleet:
1. Robot 41's bridge connects to the site router (one TCP connection)
2. Robot 41 sends gossip declarations for topics it subscribes to
3. The site router propagates these declarations to interested peers
4. No multicast, no fan-out response, no storm

The Construct measured the result: adding a robot to a 20-robot DDS fleet produced a 2 GB/s spike lasting 2-3 seconds. Adding a robot to the equivalent zenoh fleet produced less than 1 MB/s of discovery traffic that resolved in under 200ms.

### Warehouse Wi-Fi Configuration for Large Fleets

For warehouse deployments, disable DDS multicast completely on the zenoh bridge side and confine DDS to localhost only:

```bash
# On each robot, before starting the bridge:
export ROS_LOCALHOST_ONLY=1
# Or for ROS 2 Iron and later:
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
# Enable multicast on loopback (required for ROS node discovery on-robot)
sudo ip l set lo multicast on
```

With `ROS_LOCALHOST_ONLY=1`, DDS discovery is confined to the loopback interface. All ROS nodes on the same robot find each other via loopback multicast, but no DDS traffic leaves the robot. The zenoh bridge handles all inter-robot communication.

CycloneDDS explicit configuration to achieve the same effect:

```xml
<CycloneDDS>
  <Domain>
    <General>
      <Interfaces>
        <NetworkInterface address="127.0.0.1" multicast="true"/>
      </Interfaces>
      <DontRoute>true</DontRoute>
    </General>
  </Domain>
</CycloneDDS>
```

Set `CYCLONEDDS_URI` to point at this file for all ROS nodes and the bridge on each robot.

---

## Unconstrained Connectivity: NAT Traversal and Peer-to-Peer

### QUIC-Based NAT Hole-Punching

Standard TCP and UDP cannot traverse NAT without a known public address on one side. This means robots behind NAT (common in LTE or corporate Wi-Fi deployments) cannot accept incoming connections from fleet managers.

Zenoh's QUIC transport supports connection establishment through NAT without requiring port forwarding. QUIC uses UDP under the hood and can leverage STUN/ICE-style techniques for hole-punching. In practice, a robot on LTE with no public IP can connect to a cloud router on a known public address, and the resulting QUIC session allows bidirectional communication.

Robot configuration for LTE/NAT deployment:

```json5
{
  mode: "client",
  connect: {
    endpoints: ["quic/fleet.example.com:7448"]
  },
  plugins: {
    ros2dds: {
      namespace: "robot/bot1",
    }
  }
}
```

No special configuration is needed on the cloud router side—it listens on QUIC and accepts connections from any client, including those behind NAT.

### Peer-to-Peer Without Infrastructure

Two robots can communicate directly without any router when they are on the same network segment. In peer mode, zenoh nodes use UDP multicast scouting to discover each other and establish direct TCP or QUIC sessions:

```json5
// Both robots configured as peers
{
  mode: "peer",
  scouting: {
    multicast: {
      enabled: true,
      autoconnect: { peer: ["peer"] }
    }
  }
}
```

When robot A and robot B are on the same Wi-Fi, they discover each other via multicast and establish a direct session. No router hop. This is particularly useful for:
- Robot-to-robot coordination without depending on infrastructure
- Collaborative tasks where two robots need low-latency direct communication
- Graceful degradation when the site router is unreachable

### Dynamic Topology: Robots Joining and Leaving

Zenoh handles dynamic membership natively. When a robot disconnects (battery dead, network dropout), zenoh's transport layer detects the TCP/QUIC session closure. The router or peer that was connected to the robot automatically removes the robot's declared interests from its routing table. Subscribers that were receiving data from the robot stop receiving it—no stale state.

When the robot reconnects, it re-establishes its session and re-declares its publishers and subscribers. The gossip protocol propagates this information to interested peers within milliseconds. There is no manual re-registration or coordination required from the application layer.

### Offline Operation

Robots configured in client mode (connecting to a site router) handle router unavailability through the retry configuration:

```json5
connect: {
  exit_on_failure: { client: false },  // Don't crash if router is unreachable
  retry: {
    period_init_ms: 1000,
    period_max_ms: 30000,
    period_increase_factor: 2,
  }
}
```

With this configuration, a robot that loses connection to the site router keeps retrying with exponential backoff. Meanwhile, the robot continues operating autonomously with its local ROS stack. When connectivity is restored, the bridge reconnects automatically and resumes telemetry forwarding with no application restart.

---

## Multi-Site Fleet Management

### Topology: 5-Site Deployment

```
                   ┌─────────────────────────────────────┐
                   │          Cloud Router               │
                   │       fleet.example.com:7447        │
                   │    (Fleet Manager connects here)    │
                   └───┬─────┬──────┬──────┬────────┬───┘
                       │     │      │      │        │
                WAN (TLS/QUIC, 10-100ms RTT)
              ┌────────┘  ┌──┘   ┌──┘    └──┐  └────────┐
              │           │      │           │           │
         ┌────┴──┐   ┌────┴──┐  ┌┴─────┐ ┌──┴────┐ ┌───┴───┐
         │Site A │   │Site B │  │Site C│ │Site D │ │Site E │
         │Router │   │Router │  │Router│ │Router │ │Router │
         └──┬────┘   └───┬───┘  └──┬───┘ └───┬───┘ └───┬───┘
       robots(A)     robots(B)  robots(C) robots(D) robots(E)
```

Each site router connects to the cloud router over WAN. The cloud router does not connect out to sites—sites dial in. This asymmetry is deliberate: the cloud router has a stable public address; site routers may be behind firewalls.

### WAN QoS: Rate Limiting for Bandwidth-Constrained Links

WAN links between sites and cloud typically have limited bandwidth (10-100 Mbps) compared to local Wi-Fi (300+ Mbps). Downsampling rules on the site router prevent local high-frequency sensor data from saturating the WAN link:

```json5
// On each site router
downsampling: [
  {
    id: "wan-egress-limit",
    interfaces: ["eth0"],  // WAN interface
    flows: ["egress"],
    messages: ["put"],
    rules: [
      // Lidar at 5 Hz max over WAN (full 20 Hz stays on local segment)
      { key_expr: "robot/*/laser_scan", freq: 5.0 },
      // Camera images at 1 Hz over WAN
      { key_expr: "robot/*/camera/image_raw", freq: 1.0 },
      // Pose at 10 Hz over WAN
      { key_expr: "robot/*/pose", freq: 10.0 },
    ]
  }
]
```

QoS priority override for safety-critical topics on WAN:

```json5
qos: {
  publication: [
    {
      key_exprs: ["robot/*/emergency_stop", "fleet/*/safety_alert"],
      config: {
        priority: "real_time",
        congestion_control: "block",
        express: true,
      }
    },
    {
      key_exprs: ["robot/*/diagnostics", "robot/*/rosout"],
      config: {
        priority: "background",
        congestion_control: "drop",
      }
    }
  ]
}
```

### Data Locality

High-bandwidth streams—lidar point clouds at full resolution, stereo camera feeds, dense occupancy maps—should not cross WAN links unless a remote subscriber explicitly requests them. Zenoh's interest-based routing handles this automatically: a full-resolution lidar stream only crosses the WAN if a subscriber in the cloud segment declares interest in it.

This means the fleet manager dashboard, if it only subscribes to `/robot/*/pose` and `/robot/*/battery_state`, generates no WAN traffic from high-bandwidth sensor streams. The site router knows there are no remote subscribers and does not forward those topics.

### Gossip Scouting vs. Static Endpoints for WAN

For local LAN segments, gossip scouting auto-discovers robots. For WAN links between sites and cloud, use static endpoints:

```json5
// Site router: static connection to cloud
connect: {
  endpoints: ["tls/fleet.example.com:7448"]
}

// Robots: static connection to site router (don't rely on multicast across VLANs)
connect: {
  endpoints: ["tcp/192.168.1.1:7447"]
}
```

Disable multicast scouting on WAN-facing interfaces:

```json5
scouting: {
  multicast: {
    enabled: false  // No multicast over WAN
  },
  gossip: {
    enabled: true,
    multihop: false  // Single-hop gossip is sufficient for tree topology
  }
}
```

---

## Fleet Manager Patterns in Python

### Complete Fleet Manager Example

The following example implements a fleet manager that:
- Subscribes to status from all robots using wildcards
- Sends targeted commands to individual robots
- Broadcasts emergency stops to all robots
- Uses liveliness tokens to track which robots are online

```python
import zenoh
import time
import threading
from dataclasses import dataclass
from typing import Dict, Optional, Callable

@dataclass
class RobotStatus:
    robot_id: str
    battery: float
    pose_x: float
    pose_y: float
    last_seen: float
    online: bool


class FleetManager:
    """
    Manages a multi-robot fleet via zenoh.

    Assumes robots are configured with namespace "robot/<robot_id>"
    and publish to standard ROS topics under that namespace.
    """

    def __init__(self, router_endpoint: str = None):
        conf = zenoh.Config()
        if router_endpoint:
            conf.insert_json5('connect/endpoints', f'["{router_endpoint}"]')
            conf.insert_json5('mode', '"client"')

        self._session = zenoh.open(conf)
        self._robots: Dict[str, RobotStatus] = {}
        self._lock = threading.Lock()
        self._subscribers = []
        self._liveliness_sub = None

    def start(self):
        """Start monitoring all robots."""
        # Subscribe to battery state from all robots
        self._subscribers.append(
            self._session.declare_subscriber(
                "robot/*/battery_state",
                self._on_battery_state
            )
        )

        # Subscribe to pose from all robots
        self._subscribers.append(
            self._session.declare_subscriber(
                "robot/*/pose",
                self._on_pose
            )
        )

        # Use liveliness to track robot online/offline status.
        # Each robot bridge declares a liveliness token on "fleet/alive/<robot_id>".
        self._liveliness_sub = self._session.liveliness().declare_subscriber(
            "fleet/alive/*",
            self._on_liveliness_change
        )

    def _on_battery_state(self, sample):
        # Key expression: robot/<robot_id>/battery_state
        parts = str(sample.key_expr).split("/")
        robot_id = parts[1]  # Index 1: ['robot', '<robot_id>', 'battery_state']
        battery_level = self._parse_battery(sample.payload)
        with self._lock:
            if robot_id not in self._robots:
                self._robots[robot_id] = RobotStatus(
                    robot_id=robot_id, battery=0.0,
                    pose_x=0.0, pose_y=0.0,
                    last_seen=time.time(), online=True
                )
            self._robots[robot_id].battery = battery_level
            self._robots[robot_id].last_seen = time.time()

    def _on_pose(self, sample):
        # Key expression: robot/<robot_id>/pose
        parts = str(sample.key_expr).split("/")
        robot_id = parts[1]  # Index 1: ['robot', '<robot_id>', 'pose']
        x, y = self._parse_pose(sample.payload)
        with self._lock:
            if robot_id in self._robots:
                self._robots[robot_id].pose_x = x
                self._robots[robot_id].pose_y = y

    def _on_liveliness_change(self, sample):
        # sample.kind is zenoh.SampleKind.PUT for alive, DELETE for gone
        parts = str(sample.key_expr).split("/")
        robot_id = parts[2]  # fleet/alive/<robot_id>
        online = (sample.kind == zenoh.SampleKind.PUT)
        with self._lock:
            if robot_id in self._robots:
                self._robots[robot_id].online = online
        status = "online" if online else "offline"
        print(f"Robot {robot_id} is now {status}")

    def send_command(self, robot_id: str, cmd_key: str, payload: bytes):
        """Send a command to a specific robot."""
        key = f"robot/{robot_id}/{cmd_key}"
        self._session.put(key, payload)

    def emergency_stop_all(self, stop_payload: bytes):
        """
        Emergency stop all robots.
        Each robot must have a subscriber on /fleet/emergency_stop
        that triggers its local safety stop.
        """
        self._session.put("fleet/emergency_stop", stop_payload)

    def get_fleet_status(self) -> Dict[str, RobotStatus]:
        with self._lock:
            return dict(self._robots)

    def get_robots_below_battery(self, threshold: float):
        """Find robots needing charging."""
        with self._lock:
            return [
                r for r in self._robots.values()
                if r.battery < threshold and r.online
            ]

    def query_robot_state(self, robot_id: str, topic: str, timeout_secs: float = 5.0):
        """
        Query a robot's current state using zenoh get().
        Works for TRANSIENT_LOCAL topics (map, parameters, etc.)
        """
        key = f"robot/{robot_id}/{topic}"
        replies = self._session.get(key, timeout=timeout_secs)
        for reply in replies:
            if reply.ok:
                return reply.ok.payload
        return None

    def close(self):
        for sub in self._subscribers:
            sub.undeclare()
        if self._liveliness_sub:
            self._liveliness_sub.undeclare()
        self._session.close()

    def _parse_battery(self, payload) -> float:
        # Parse CDR-encoded BatteryState message
        # In production: use pycdr2 to deserialize sensor_msgs/BatteryState
        return 0.0  # Placeholder

    def _parse_pose(self, payload) -> tuple:
        # Parse CDR-encoded PoseStamped message
        return (0.0, 0.0)  # Placeholder


# Usage
if __name__ == "__main__":
    fleet = FleetManager(router_endpoint="tcp/fleet.example.com:7447")
    fleet.start()

    try:
        while True:
            status = fleet.get_fleet_status()
            print(f"Fleet: {len(status)} robots tracked")

            low_battery = fleet.get_robots_below_battery(0.2)
            for robot in low_battery:
                print(f"  -> {robot.robot_id}: battery {robot.battery:.0%}, dispatch to charger")

            time.sleep(5.0)
    except KeyboardInterrupt:
        fleet.close()
```

### Robot-Side Liveliness Token

Each robot bridge companion process should declare a liveliness token so the fleet manager can detect robot availability:

```python
import zenoh
import signal
import sys

def robot_liveliness(robot_id: str, router: str):
    """Run on each robot to maintain fleet presence."""
    conf = zenoh.Config()
    conf.insert_json5('connect/endpoints', f'["{router}"]')
    conf.insert_json5('mode', '"client"')

    session = zenoh.open(conf)

    # Declare liveliness: fleet manager sees this token appear/disappear
    token = session.liveliness().declare_token(f"fleet/alive/{robot_id}")

    print(f"Robot {robot_id} registered with fleet")

    def shutdown(sig, frame):
        token.undeclare()  # Explicitly remove; also happens on session close
        session.close()
        sys.exit(0)

    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGINT, shutdown)

    # Keep running
    while True:
        signal.pause()
```

### Leader Election for Fleet Coordinator

When running multiple fleet manager instances for redundancy, use liveliness tokens for leader election:

```python
import zenoh
import time
import threading

class FleetCoordinator:
    """
    Implements leader election among multiple fleet coordinator instances.
    The coordinator with the lowest ZID lexicographically becomes leader.
    Uses zenoh liveliness to detect coordinator failures.
    """

    def __init__(self, coordinator_id: str, router: str):
        self._id = coordinator_id
        self._is_leader = False
        self._coordinators = set()

        conf = zenoh.Config()
        conf.insert_json5('connect/endpoints', f'["{router}"]')
        session = zenoh.open(conf)
        self._session = session

        # Announce self
        self._token = session.liveliness().declare_token(
            f"fleet/coordinator/{coordinator_id}"
        )

        # Watch all coordinators
        self._coord_sub = session.liveliness().declare_subscriber(
            "fleet/coordinator/*",
            self._on_coordinator_change
        )

        # Query existing coordinators (get current state)
        existing = session.liveliness().get("fleet/coordinator/*", timeout=2.0)
        for reply in existing:
            if reply.ok:
                parts = str(reply.ok.key_expr).split("/")
                self._coordinators.add(parts[-1])

        self._coordinators.add(coordinator_id)
        self._elect()

    def _on_coordinator_change(self, sample):
        parts = str(sample.key_expr).split("/")
        coord_id = parts[-1]
        if sample.kind == zenoh.SampleKind.PUT:
            self._coordinators.add(coord_id)
        else:
            self._coordinators.discard(coord_id)
        self._elect()

    def _elect(self):
        # Coordinator with minimum ID becomes leader
        if not self._coordinators:
            return
        leader = min(self._coordinators)
        was_leader = self._is_leader
        self._is_leader = (leader == self._id)
        if self._is_leader and not was_leader:
            print(f"[{self._id}] Became fleet leader")
            self._on_became_leader()
        elif not self._is_leader and was_leader:
            print(f"[{self._id}] Lost leadership to {leader}")

    def _on_became_leader(self):
        """Override to implement leader-specific behavior."""
        pass

    @property
    def is_leader(self) -> bool:
        return self._is_leader
```

---

## Configuration Reference Summary

### Per-Robot Bridge Config Template

```json5
// robot-N-bridge.json5 — deploy one per robot
{
  plugins: {
    ros2dds: {
      // REQUIRED: unique namespace per robot
      namespace: "robot/bot-N",

      // Confine DDS to this robot only
      ros_localhost_only: true,

      // Route only the topics you need (reduce Wi-Fi usage)
      allow: {
        publishers: [".*/laser_scan", ".*/pose", ".*/battery_state", "/tf"],
        subscribers: [".*/cmd_vel", ".*/goal_pose"],
        service_servers: [".*/.*_parameters"],
        service_clients: [],
        action_servers: [".*/navigate_to_pose"],
        action_clients: [],
      },

      // Rate-limit high-frequency topics
      pub_max_frequencies: [
        ".*/laser_scan=5",
        "/tf=10",
        ".*/odom=20"
      ],

      // Safety traffic gets highest priority
      pub_priorities: [
        ".*/cmd_vel=1:express",
        ".*/pose=2",
        ".*/laser_scan=5",
        ".*/diagnostics=7"
      ],
    }
  },

  mode: "client",
  connect: {
    endpoints: ["tcp/SITE-ROUTER-IP:7447"],
    retry: {
      period_init_ms: 1000,
      period_max_ms: 30000,
      period_increase_factor: 2,
    },
    exit_on_failure: { client: false }
  },
  scouting: {
    multicast: { enabled: false },
    gossip: { enabled: false }
  }
}
```

### Site Router Config Template

```json5
// site-router.json5 — deploy one per warehouse floor/building
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  },
  connect: {
    endpoints: ["tls/CLOUD-ROUTER:7448"]
  },
  scouting: {
    multicast: { enabled: false },
    gossip: {
      enabled: true,
      multihop: false
    }
  },
  // Rate-limit WAN egress for high-bandwidth topics
  downsampling: [
    {
      id: "wan-limit",
      interfaces: ["eth0"],
      flows: ["egress"],
      messages: ["put"],
      rules: [
        { key_expr: "robot/*/laser_scan", freq: 5.0 },
        { key_expr: "robot/*/camera/**", freq: 1.0 },
      ]
    }
  ]
}
```

### Cloud Router Config Template

```json5
// cloud-router.json5 — single instance, accepts all site connections
{
  mode: "router",
  listen: {
    endpoints: [
      "tcp/0.0.0.0:7447",
      "tls/0.0.0.0:7448"
    ]
  },
  scouting: {
    multicast: { enabled: false },
    gossip: {
      enabled: true,
      multihop: false
    }
  },
  routing: {
    router: {
      peers_failover_brokering: true
    }
  }
}
```

---

## Operational Checklist

Before deploying a multi-robot fleet with zenoh:

**Per Robot**
- [ ] Set `namespace` to a unique identifier (robot serial number or UUID recommended for production)
- [ ] Set `ros_localhost_only: true` or configure CycloneDDS to use loopback only
- [ ] Use `allow` filter to whitelist only needed topics — default routes everything
- [ ] Set `pub_max_frequencies` for any topics above 10 Hz
- [ ] Configure exponential reconnect retry so robots survive router restarts
- [ ] Declare a [liveliness](liveliness-complete-guide.md) token so the fleet manager can detect robot presence

**Per Site Router**
- [ ] Static connection to cloud router (no autoconnect)
- [ ] Disable multicast scouting
- [ ] Configure WAN-egress downsampling rules for bandwidth-heavy topics
- [ ] Set [QoS](qos-guide.md) overrides to protect safety-critical traffic

**Fleet Manager**
- [ ] Subscribe with wildcards (`robot/*/topic`) for fleet-wide views — see [Key Expressions Guide](key-expressions-guide.md)
- [ ] Subscribe to liveliness `fleet/alive/*` for robot presence tracking
- [ ] Pre-declare publishers and subscribers before starting main loop
- [ ] Use `get()` for TRANSIENT_LOCAL topics (maps, parameters) when a robot first connects
- [ ] Test emergency stop path independently from normal telemetry path

## See Also

- [Key Expressions Guide](key-expressions-guide.md) — wildcard patterns like `robot/*/topic` used throughout this guide for fleet-wide subscriptions
- [Liveliness Complete Guide](liveliness-complete-guide.md) — the liveliness token pattern used for detecting robot online/offline status
- [ROS2 Migration Guide](ros2-migration-guide.md) — how to configure the DDS bridge with per-robot namespacing
- [Node Types Guide](node-types-guide.md) — the three-tier router hierarchy (robot client → site router → cloud router) used here
