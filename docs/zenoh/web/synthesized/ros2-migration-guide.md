# ROS2/DDS to Zenoh Migration Guide

A practical, step-by-step guide for migrating ROS2 systems from DDS to Zenoh — from zero-change bridging to full native Zenoh nodes.

---

## Table of Contents

- [Why Migrate: DDS Pain Points](#why-migrate-dds-pain-points)
  - [Discovery Overhead: The N² Problem](#discovery-overhead-the-n²-problem)
  - [The 2 GB/s Multicast Spike (The Construct)](#the-2-gbs-multicast-spike-the-construct)
  - [Publisher Stall: RELIABLE QoS Blocks the Publisher Thread (Akara Robotics)](#publisher-stall-reliable-qos-blocks-the-publisher-thread-akara-robotics)
  - [Cloud Connectivity: DDS Doesn't Cross Subnets](#cloud-connectivity-dds-doesnt-cross-subnets)
- [Step-by-Step Migration](#step-by-step-migration)
  - [Phase 1: Non-Breaking Bridge (Zero Code Changes)](#phase-1-non-breaking-bridge-zero-code-changes)
  - [Phase 2: Multi-Site Connectivity](#phase-2-multi-site-connectivity)
  - [Phase 3: Native Zenoh Nodes (Gradual Replacement)](#phase-3-native-zenoh-nodes-gradual-replacement)
  - [Phase 4: Full Zenoh (No ROS2 Required)](#phase-4-full-zenoh-no-ros2-required)
- [Namespace Scoping for Multi-Robot Fleets](#namespace-scoping-for-multi-robot-fleets)
  - [The Problem Without Scoping](#the-problem-without-scoping)
  - [The Solution: Bridge-Level Namespacing](#the-solution-bridge-level-namespacing)
  - [Multi-Robot Fleet Config (Full Example)](#multi-robot-fleet-config-full-example)
  - [How ROS2 Namespaces Map to Zenoh Key Expressions](#how-ros2-namespaces-map-to-zenoh-key-expressions)
- [Queryables for Services and Actions](#queryables-for-services-and-actions)
  - [ROS2 Service → Zenoh Queryable](#ros2-service-zenoh-queryable)
  - [ROS2 Action → Zenoh Queryables](#ros2-action-zenoh-queryables)
- [The Publisher Stall Problem (Akara Robotics)](#the-publisher-stall-problem-akara-robotics)
  - [Root Cause in DDS](#root-cause-in-dds)
  - [Zenoh's Non-Blocking Architecture](#zenohs-non-blocking-architecture)
  - [Before/After: Akara Robotics](#beforeafter-akara-robotics)
- [Multicast Spike Elimination (The Construct)](#multicast-spike-elimination-the-construct)
  - [Root Cause in DDS](#root-cause-in-dds)
  - [Zenoh's Gossip Discovery](#zenohs-gossip-discovery)
  - [Before/After: The Construct](#beforeafter-the-construct)
- [QUIC for Wi-Fi Robustness (Filics Warehouse AMRs)](#quic-for-wi-fi-robustness-filics-warehouse-amrs)
  - [Why TCP Fails on Lossy Wi-Fi](#why-tcp-fails-on-lossy-wi-fi)
  - [QUIC's Per-Stream Loss Recovery](#quics-per-stream-loss-recovery)
  - [Migration: TCP to QUIC](#migration-tcp-to-quic)
  - [Before/After: Filics Warehouse AMRs](#beforeafter-filics-warehouse-amrs)
- [Topic Filtering for Bandwidth Reduction](#topic-filtering-for-bandwidth-reduction)
- [Common Migration Mistakes](#common-migration-mistakes)
  - [1. Forgetting to Scope Multi-Robot Deployments](#1-forgetting-to-scope-multi-robot-deployments)
  - [2. Using TCP Instead of QUIC on Wi-Fi](#2-using-tcp-instead-of-quic-on-wi-fi)
  - [3. DDS Traffic Escaping to Other Hosts](#3-dds-traffic-escaping-to-other-hosts)
  - [4. CDR Encoding Mismatch Between Zenoh and ROS2 Nodes](#4-cdr-encoding-mismatch-between-zenoh-and-ros2-nodes)
  - [5. Not Setting `complete(true)` on Storage Queryables](#5-not-setting-completetrue-on-storage-queryables)
  - [6. `reliable_routes_blocking: true` Recreating the Publisher Stall](#6-reliable_routes_blocking-true-recreating-the-publisher-stall)
- [Admin Space: Observing Bridge State](#admin-space-observing-bridge-state)
- [Migration Checklist](#migration-checklist)
  - [Pre-Migration](#pre-migration)
  - [Phase 1 (Bridge)](#phase-1-bridge)
  - [Phase 2 (Multi-site)](#phase-2-multi-site)
  - [Phase 3 (Native nodes, optional)](#phase-3-native-nodes-optional)
  - [Phase 4 (Full zenoh, optional)](#phase-4-full-zenoh-optional)

## Why Migrate: DDS Pain Points

### Discovery Overhead: The N² Problem

DDS discovery uses SPDP (Simple Participant Discovery Protocol) and SEDP (Simple Endpoint Discovery Protocol) multicast messages. Every new participant must exchange discovery information with every existing participant. With N nodes, this is O(N²) message exchanges.

In a modest ROS2 fleet with 20 nodes, each running 30-40 topics, you get 700+ DDS readers/writers (as observed in the DDS → Zenoh migration case study). Every new robot that joins triggers SPDP multicast, and all 700+ existing endpoints respond simultaneously. This produces a discovery storm that can saturate the network.

Zenoh uses gossip scouting or linkstate routing: each new peer contacts a known router, which propagates the information incrementally. There is no multicast broadcast that triggers simultaneous responses from all existing peers.

### The 2 GB/s Multicast Spike (The Construct)

The Construct, an online cloud robotics lab running ROS2 environments for students, observed a 2 GB/s network spike at startup and whenever a new user joined a shared environment. The root cause was DDS multicast: each new participant triggered SPDP from all existing peers. With dozens of concurrent lab sessions, this became catastrophic.

After migrating to Zenoh, the spike was eliminated entirely. Zenoh's gossip discovery is incremental — new peers contact a router, the router propagates the information point-to-point. No multicast storm. Network traffic dropped from spikes measured in gigabits per second to sustained traffic proportional to actual data.

### Publisher Stall: RELIABLE QoS Blocks the Publisher Thread (Akara Robotics)

This is one of the most dangerous DDS failure modes in safety-critical robotics.

**Root cause in DDS:** When a publisher uses RELIABLE QoS and a subscriber's receive queue fills up, DDS backpressure causes the publisher's `write()` call to block. The publisher thread is frozen until the slow subscriber drains its queue. This means a single slow sensor node — perhaps a visualization tool or a logger running over Wi-Fi — can stall the publisher that controls a robot arm.

**What Akara Robotics observed:** Robot arm commands were being delayed not because the arm controller was slow, but because a monitoring subscriber was backing up. Safety-critical messages sat queued behind normal-priority messages. The robot arm would periodically freeze for hundreds of milliseconds.

**How Zenoh solves it:** Zenoh maintains per-subscriber queues at the router layer. A slow subscriber gets its own queue; its backpressure does not reach the publisher. The publisher's `put()` call returns immediately. If the queue fills, the Zenoh router applies the configured `CongestionControl` policy — `Drop` (discard messages) or `Block` (apply backpressure only to that subscriber) — without stalling the source.

The result at Akara: robot arm command latency became consistent and bounded, independent of slow monitoring subscribers.

### Cloud Connectivity: DDS Doesn't Cross Subnets

DDS multicast discovery is bound to the local subnet. To connect a robot in one network to an operator console in another, you need either custom DDS configuration (static peer lists, unicast discovery) or a VPN. Neither scales well for a fleet of 1000+ robots.

Zenoh is transport-agnostic. A zenoh router in the cloud accepts TCP connections from robots behind NAT. QUIC transport adds reliability on lossy links. No VPN required; no multicast required.

---

## Step-by-Step Migration

### Phase 1: Non-Breaking Bridge (Zero Code Changes)

The `zenoh-bridge-ros2dds` bridges all ROS2 DDS traffic over Zenoh with no changes to existing ROS2 nodes. This is the recommended entry point — your existing code keeps running exactly as before.

**Step 1: Install the bridge**

On Debian/Ubuntu:
```bash
curl -L https://download.eclipse.org/zenoh/debian-repo/zenoh-public-key \
  | sudo gpg --dearmor --yes --output /etc/apt/keyrings/zenoh-public-key.gpg
echo "deb [signed-by=/etc/apt/keyrings/zenoh-public-key.gpg] \
  https://download.eclipse.org/zenoh/debian-repo/ /" \
  | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt update
sudo apt install zenoh-bridge-ros2dds
```

Or via Docker:
```bash
docker pull eclipse/zenoh-bridge-ros2dds:latest
```

**Step 2: Prevent DDS from leaking outside the robot**

The bridge works correctly only if DDS traffic stays local to the robot — no DDS multicast escaping to other hosts. Pick one:

Option A — restrict discovery to localhost (ROS Iron and later):
```bash
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
sudo ip l set lo multicast on   # enable multicast on loopback
```

Option B — restrict via domain ID (always works):
```bash
export ROS_DOMAIN_ID=42   # use a unique ID per robot
```

Option C — restrict via CycloneDDS config (most explicit):
```xml
<!-- Save as /etc/cyclonedds/robot.xml, export CYCLONEDDS_URI=file:///etc/cyclonedds/robot.xml -->
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

**Step 3: Start the bridge on the robot**

```bash
zenoh-bridge-ros2dds
```

The bridge starts in router mode by default, listening on TCP port 7447.

**Step 4: Connect an operator host to the robot**

On the operator host:
```bash
zenoh-bridge-ros2dds -e tcp/<robot-ip>:7447
```

**Step 5: Verify everything still works**

```bash
ros2 topic list       # should show all robot topics
ros2 service list     # should show all robot services
ros2 action list      # should show all robot actions
rviz2                 # should connect and display normally
```

All existing ROS2 tooling works transparently. The bridge maps ROS2 topic names to zenoh key expressions: a topic `/cmd_vel` becomes the Zenoh key `cmd_vel` (the leading `/` is stripped). Note: the DDS layer uses `rt/cmd_vel` as the DDS topic name internally, but the Zenoh key expression does not include the `rt/` prefix.

---

### Phase 2: Multi-Site Connectivity

**Step 1: Start a bridge on each robot with a unique namespace**

```bash
# On robot 1
zenoh-bridge-ros2dds --namespace /robot1

# On robot 2
zenoh-bridge-ros2dds --namespace /robot2
```

Or via config file `robot1-config.json5`:
```json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_automatic_discovery_range: "LOCALHOST",
    }
  }
}
```

```bash
zenoh-bridge-ros2dds -c robot1-config.json5
```

**Step 2: Deploy a zenoh router in the cloud or operations center**

```bash
zenohd
```

**Step 3: Connect each robot bridge to the central router**

```json5
// robot1-config.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
    }
  },
  connect: {
    endpoints: ["tcp/<router-ip>:7447"]
  }
}
```

**Step 4: Verify cross-site topic access from the operator**

From an operator host connected to the same router:
```bash
# See all robot topics (namespaced)
ros2 topic list
# /robot1/cmd_vel
# /robot1/scan
# /robot2/cmd_vel
# /robot2/scan

# Subscribe to robot1's lidar
ros2 topic echo /robot1/scan
```

**Step 5: Scoped operator access**

To operate a specific robot with existing ROS2 tools (without typing the namespace everywhere):
```bash
# Connect operator bridge scoped to robot1
zenoh-bridge-ros2dds -e tcp/<router-ip>:7447 --namespace /robot1
# Now: ros2 topic list shows /cmd_vel, /scan (not /robot1/...)
```

To operate all robots from one bridge (no namespace, use remapping):
```bash
zenoh-bridge-ros2dds -e tcp/<router-ip>:7447
# Use remap to target specific robot:
rviz2 --ros-args -r /tf:=/robot1/tf -r /tf_static:=/robot1/tf_static
```

---

### Phase 3: Native Zenoh Nodes (Gradual Replacement)

At this point you can start replacing individual ROS2 nodes with native zenoh nodes, one at a time. The remaining ROS2 nodes continue using the bridge; native zenoh nodes communicate directly.

**CDR encoding** is required for interoperability: ROS2 uses CDR (Common Data Representation) for message serialization over DDS. If your native zenoh node publishes to a topic that a ROS2 subscriber listens to (or vice versa via the bridge), the payload must be CDR-encoded.

Install `pycdr2`:
```bash
pip install pycdr2
```

**Example: Native zenoh publisher replacing a ROS2 publisher node**

This Python node publishes `geometry_msgs/Twist` to `/cmd_vel` in a format compatible with any ROS2 subscriber:

```python
import zenoh
from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import float64

@dataclass
class Vector3(IdlStruct, typename="Vector3"):
    x: float64
    y: float64
    z: float64

@dataclass
class Twist(IdlStruct, typename="Twist"):
    linear: Vector3
    angular: Vector3

# Open a zenoh session (peer mode to connect directly to a bridge/router)
conf = zenoh.Config()
conf.insert_json5('mode', '"peer"')
conf.insert_json5('connect/endpoints', '["tcp/robot-ip:7447"]')

session = zenoh.open(conf)

# Publish to cmd_vel — the bridge maps this to ROS2 topic /cmd_vel
# Zenoh key expression is the ROS2 topic name with the leading "/" stripped
twist = Twist(
    linear=Vector3(x=0.5, y=0.0, z=0.0),
    angular=Vector3(x=0.0, y=0.0, z=0.1)
)
session.put("cmd_vel", twist.serialize())

session.close()
```

Key naming convention used by `zenoh-bridge-ros2dds`:
- Regular topics: `<topic_name>` with leading `/` stripped (e.g., `/cmd_vel` → `cmd_vel`, `/scan` → `scan`). With a configured `namespace: "/robot1"` (note: namespace config values MUST start with `/`), topics become `robot1/cmd_vel` etc. (the leading `/` of the namespace is stripped when building the Zenoh key).
- Services: declared on the base service name (e.g., `/add_two_ints` → `add_two_ints`). The `rq/rr` prefixes are DDS topic names, not Zenoh key expressions.
- Actions: declared on the base action name with suffixes like `_action/send_goal`, `_action/cancel_goal`, `_action/get_result`, `_action/feedback`, `_action/status`

**Example: Native zenoh subscriber replacing a ROS2 subscriber node**

```python
import zenoh
from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import uint32, float32
from typing import List

@dataclass
class LaserScan(IdlStruct, typename="LaserScan"):
    # ... field definitions matching sensor_msgs/LaserScan
    range_min: float32
    range_max: float32
    ranges: List[float32]
    intensities: List[float32]

def on_scan(sample):
    scan = LaserScan.deserialize(sample.payload)
    print(f"Received scan: {len(scan.ranges)} points, range [{scan.range_min:.2f}, {scan.range_max:.2f}]")

session = zenoh.open(zenoh.Config())
sub = session.declare_subscriber("robot1/scan", on_scan)

input("Press Enter to stop...\n")
sub.undeclare()
session.close()
```

**Gradually replace nodes:**
1. Start with leaf nodes (sensors, actuators) — they have the fewest dependencies
2. Keep the bridge running while any ROS2 nodes remain
3. Validate each replacement node before removing the ROS2 version
4. When all nodes on a robot are native zenoh, decommission the bridge

---

### Phase 4: Full Zenoh (No ROS2 Required)

When all nodes are native zenoh and no ROS2 tools are needed on the path, you can drop CDR encoding entirely and use any serialization you prefer. This delivers maximum performance.

**When to stay with CDR:** If you still use `ros2 topic echo`, `rviz2`, or `rosbag2` anywhere on that data path, keep CDR.

**When to switch to custom serialization:**
- Full zenoh fleet with no ROS2 tooling
- Performance-critical paths (CDR has overhead for complex types)
- Embedded or microcontroller nodes (zenoh-pico + CDR is cumbersome)

Example with raw bytes (no framework dependency):
```python
import zenoh
import struct

session = zenoh.open(zenoh.Config())

# Publish a simple IMU reading as raw packed binary
# Format: timestamp_ns (uint64) + accel_x/y/z (float32 × 3) + gyro_x/y/z (float32 × 3)
def publish_imu(timestamp_ns, accel, gyro):
    payload = struct.pack(">Qffffff", timestamp_ns, *accel, *gyro)
    session.put("robot/imu/raw", payload)
```

---

## Namespace Scoping for Multi-Robot Fleets

### The Problem Without Scoping

Two robots running identical ROS2 node graphs both publish `/cmd_vel`, `/scan`, `/tf`. Without namespace isolation, these topics merge on the zenoh network. A control command intended for robot A reaches robot B. TF trees from different robots collide.

### The Solution: Bridge-Level Namespacing

Configure each bridge with a unique namespace. The bridge prepends the namespace to **all** topics, services, and actions — including `/rosout`, `/tf`, and `/tf_static`. Individual ROS2 nodes need no modification; their DDS traffic stays on localhost, already namespaced correctly for each robot's internal graph.

```json5
// robot1-config.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_automatic_discovery_range: "LOCALHOST",
    }
  },
  connect: {
    endpoints: ["tcp/fleet-router:7447"]
  }
}
```

```json5
// robot2-config.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot2",
      ros_automatic_discovery_range: "LOCALHOST",
    }
  },
  connect: {
    endpoints: ["tcp/fleet-router:7447"]
  }
}
```

On the operator side, `/cmd_vel` becomes `/robot1/cmd_vel` and `/robot2/cmd_vel` — distinct zenoh key expressions that don't interfere.

### Multi-Robot Fleet Config (Full Example)

```json5
// fleet-router.json5 — central router, no ROS2 plugin
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  },
  scouting: {
    gossip: {
      enabled: true,
      multihop: false,
    }
  }
}
```

Start the router:
```bash
zenohd -c fleet-router.json5
```

Start each robot bridge:
```bash
# On robot 1
zenoh-bridge-ros2dds -c robot1-config.json5

# On robot 2
zenoh-bridge-ros2dds -c robot2-config.json5
```

### How ROS2 Namespaces Map to Zenoh Key Expressions

| ROS2 topic | Configured bridge namespace (`namespace:`) | Zenoh key expression |
|---|---|---|
| `/cmd_vel` | `/robot1` | `robot1/cmd_vel` |
| `/scan` | `/robot1` | `robot1/scan` |
| `/tf` | `/robot1` | `robot1/tf` |
| `/rosout` | `/robot1` | `robot1/rosout` |

This is the zenoh key expression that native zenoh nodes should subscribe to. The bridge: (1) strips the leading `/` from the ROS2 topic name, (2) prepends the configured namespace (also with its leading `/` stripped), resulting in no `rt/` prefix in the Zenoh key. **Important:** The `namespace:` config value must start with `/` — the bridge code assumes this and strips the first character when building key expressions.

---

## Queryables for Services and Actions

### ROS2 Service → Zenoh Queryable

A ROS2 service (`AddTwoInts`) maps to a zenoh queryable. The bridge handles the mapping automatically. For native zenoh nodes replacing a service server:

```python
import zenoh
from pycdr2 import IdlStruct
from dataclasses import dataclass
from pycdr2.types import int64

@dataclass
class AddTwoIntsRequest(IdlStruct, typename="AddTwoInts_Request_"):
    a: int64
    b: int64

@dataclass
class AddTwoIntsResponse(IdlStruct, typename="AddTwoInts_Response_"):
    sum: int64

def add_two_ints_handler(query):
    req = AddTwoIntsRequest.deserialize(query.payload)
    result = AddTwoIntsResponse(sum=req.a + req.b)
    query.reply(query.key_expr, result.serialize())

session = zenoh.open(zenoh.Config())
queryable = session.declare_queryable("add_two_ints", add_two_ints_handler)

input("Service running. Press Enter to stop.\n")
queryable.undeclare()
session.close()
```

### ROS2 Action → Zenoh Queryables

A ROS2 action has three components: `send_goal`, `cancel_goal`, and `get_result`. Each becomes a separate zenoh queryable. The bridge maps these automatically for ROS2 ↔ native zenoh interop.

Default timeouts (configurable in `queries_timeout`):
- `send_goal`: 5.0 seconds
- `cancel_goal`: 5.0 seconds
- `get_result`: 300.0 seconds (actions can run for minutes)

For long-running actions, override the default:
```json5
{
  plugins: {
    ros2dds: {
      queries_timeout: {
        default: 5.0,
        actions: {
          send_goal: 1.0,
          cancel_goal: 1.0,
          get_result: [".*long_mission=3600", ".*short_action=10.0", ".*=300"],
        }
      }
    }
  }
}
```

---

## The Publisher Stall Problem (Akara Robotics)

### Root Cause in DDS

DDS RELIABLE QoS guarantees delivery by maintaining a send queue. When a subscriber's receive queue is full, the DDS writer's `write()` call blocks until the subscriber drains. There is one shared send queue per writer that serves all subscribers.

This means:
- 1 slow subscriber (monitoring laptop on Wi-Fi) can stall the publisher
- The publisher thread blocks — no messages go out to any subscriber, including fast, reliable subscribers on the same robot
- Safety-critical arm commands queue behind diagnostic messages

In a system with mixed QoS (some RELIABLE, some BEST_EFFORT), the interaction between a RELIABLE publisher and a RELIABLE subscriber creates these stall scenarios.

### Zenoh's Non-Blocking Architecture

Zenoh decouples publisher from subscriber at the router layer:
- Each subscriber has its own queue
- A slow subscriber's queue backing up does not affect the publisher's `put()` call
- `CongestionControl::Drop` (default) discards messages to a full queue without blocking
- `CongestionControl::Block` applies backpressure only to that specific subscriber

For the bridge, this is controlled by `reliable_routes_blocking`:

```json5
{
  plugins: {
    ros2dds: {
      // true = RELIABLE DDS Writers use CongestionControl::Block (preserves DDS semantics)
      // false = use CongestionControl::Drop (prevents publisher stall)
      reliable_routes_blocking: false,
    }
  }
}
```

Setting `reliable_routes_blocking: false` prevents the publisher stall. The trade-off is that some messages may be dropped to a congested subscriber — which is exactly what you want for safety-critical systems where the alternative is a frozen publisher.

### Before/After: Akara Robotics

Before (DDS): Robot arm commands intermittently delayed 200-800ms when the monitoring subscriber's Wi-Fi bandwidth was saturated. The publisher thread blocked. Safety watchdog false triggers.

After (Zenoh): Arm command latency bounded to <5ms regardless of monitoring subscriber state. The monitoring subscriber received messages when bandwidth allowed; the arm controller was unaffected.

---

## Multicast Spike Elimination (The Construct)

### Root Cause in DDS

DDS SPDP uses UDP multicast address `239.255.0.1:7400` (by default) to announce participants. When a new participant joins:
1. It sends a multicast SPDP announcement
2. **Every existing participant responds** with its own SPDP data
3. SEDP unicast then fires between the new participant and all existing ones

With 700 readers/writers (typical for a 20-node robot), joining triggers 700 SPDP/SEDP responses simultaneously. With 50 concurrent lab sessions, startup means 35,000 near-simultaneous responses.

### Zenoh's Gossip Discovery

Zenoh scouting is incremental:
1. New node sends a scout message to its configured router
2. Router adds the new node to its routing table
3. Router notifies interested peers via gossip (point-to-point, not multicast broadcast)
4. No existing node sends a burst response

The result: O(1) per new participant, not O(N).

### Before/After: The Construct

Before (DDS): 2 GB/s network spike at lab session startup. Spikes also occurred when any student's ROS node crashed and restarted, triggering re-discovery. Cloud ingress bills were impacted.

After (Zenoh): Network traffic at startup was proportional to actual data — no discovery spikes. Session startup time dropped from several seconds (waiting for DDS discovery) to under 100ms.

---

## QUIC for Wi-Fi Robustness (Filics Warehouse AMRs)

### Why TCP Fails on Lossy Wi-Fi

TCP is a stream protocol with head-of-line blocking: if one packet is lost, all data behind it in the stream waits until the lost packet is retransmitted. On a warehouse floor with 802.11 interference, forklifts blocking signals, and AMRs moving between access points, packet loss is frequent. TCP's response:
1. Detect loss (timeout or NACK)
2. Retransmit
3. Reduce congestion window
4. All pending data stalls during retransmit

For a robot publishing at 50Hz, a 20ms retransmit stall corrupts the entire stream. Multiple stalls compound into multi-second communication gaps.

### QUIC's Per-Stream Loss Recovery

QUIC (implemented in zenoh via `quic` transport) runs multiple logical streams over one UDP connection. Loss in one stream does not block others. For robotics:
- Stream 1: `/cmd_vel` (safety-critical, low latency)
- Stream 2: `/scan` (lidar, high bandwidth)
- Stream 3: `/camera/image_raw` (very high bandwidth, can tolerate drops)

A lost lidar packet does not delay the next cmd_vel command.

Additionally, QUIC handles handoff between access points more gracefully than TCP — connection migration keeps the session alive through IP address changes.

### Migration: TCP to QUIC

In the bridge config, change the listen/connect endpoints:

```json5
// Before: TCP
{
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  }
}

// After: QUIC (TLS certificate required)
{
  listen: {
    endpoints: ["quic/0.0.0.0:7447"]
  }
}
```

For robots connecting to the fleet router:
```json5
{
  connect: {
    endpoints: ["quic/fleet-router:7447"]
  }
}
```

QUIC requires a TLS certificate. For internal fleet use, a self-signed cert is sufficient. Zenoh's TLS configuration:

```json5
{
  transport: {
    unicast: {
      tls: {
        root_ca_certificate: "/etc/zenoh/ca.pem",
        server_certificate: "/etc/zenoh/server.pem",
        server_private_key: "/etc/zenoh/server.key",
      }
    }
  }
}
```

### Before/After: Filics Warehouse AMRs

Before (TCP): AMRs experienced communication gaps of 1-3 seconds during handoffs between access points in the warehouse. Navigation commands were delayed, causing AMRs to stop and wait for connection recovery.

After (QUIC): Handoffs became transparent. Communication gaps under 50ms. A 1000+ unit pilot deployment showed reliable navigation in environments with known Wi-Fi interference.

---

## Topic Filtering for Bandwidth Reduction

Not all topics need to cross every site boundary. Use `allow` or `deny` to control what gets routed over zenoh:

```json5
{
  plugins: {
    ros2dds: {
      // Only route these topics outbound (everything else stays local to the robot)
      allow: {
        publishers: [".*/scan", ".*/pose", "/tf", "/tf_static", "/rosout"],
        subscribers: [".*/cmd_vel", ".*/goal_pose"],
        service_servers: [".*/navigate_to_pose"],
        service_clients: [],
        action_servers: [".*/navigate_to_pose"],
        action_clients: [],
      }
    }
  }
}
```

For high-frequency sensors like lidar, rate-limit rather than block entirely:

```json5
{
  plugins: {
    ros2dds: {
      // Lidar at 30Hz, TF at 10Hz — rate-limited over zenoh to reduce bandwidth
      pub_max_frequencies: [".*/scan=5", "/tf=10"],
    }
  }
}
```

For mixed-priority traffic, set priorities so safety-critical topics aren't delayed by bulk data:

```json5
{
  plugins: {
    ros2dds: {
      // Priority 1 (highest) for cmd_vel, 7 (lowest) for logs
      pub_priorities: [".*/cmd_vel=1:express", ".*/scan=3", "/rosout=7"],
    }
  }
}
```

The `:express` flag on `cmd_vel` tells zenoh to send immediately without batching — reducing latency at the cost of slightly lower throughput.

---

## Common Migration Mistakes

### 1. Forgetting to Scope Multi-Robot Deployments

**Symptom:** Two robots receive each other's `cmd_vel` commands. TF trees are corrupted with transforms from both robots merged into one tree.

**Fix:** Always configure `namespace` in the bridge config when running more than one robot on the same zenoh network. The namespace must be unique per robot.

```json5
// robot1-config.json5
{ plugins: { ros2dds: { namespace: "/robot1" } } }

// robot2-config.json5
{ plugins: { ros2dds: { namespace: "/robot2" } } }
```

### 2. Using TCP Instead of QUIC on Wi-Fi

**Symptom:** Robot navigation stalls during access point handoffs. Intermittent multi-second communication gaps on warehouse floors or outdoor deployments.

**Fix:** Switch from `tcp/<ip>:7447` to `quic/<ip>:7447` in both the bridge's `connect.endpoints` and the router's `listen.endpoints`. Generate TLS certificates if you haven't already.

### 3. DDS Traffic Escaping to Other Hosts

**Symptom:** Duplicate messages, discovery loops, topics appearing from unexpected sources. `ros2 topic echo /cmd_vel` on the operator machine shows messages but with suspicious extra copies.

**Fix:** The bridge must be the only path for DDS traffic between hosts. Ensure all ROS2 nodes on the robot have `ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST` (Iron+) or use a `CYCLONEDDS_URI` that restricts interfaces to loopback. If using `ROS_DOMAIN_ID`, make sure the IDs differ between hosts.

### 4. CDR Encoding Mismatch Between Zenoh and ROS2 Nodes

**Symptom:** Native zenoh subscriber receives garbage data from a ROS2 publisher via the bridge. Or a native zenoh publisher's data causes a ROS2 subscriber to crash with a deserialization error.

**Fix:** Native zenoh nodes interoperating with ROS2 nodes through the bridge must use CDR encoding. Use `pycdr2` in Python. The `typename` field in `IdlStruct` must exactly match the DDS type name used by ROS2.

```python
# Wrong: typename doesn't match what DDS expects
@dataclass
class Twist(IdlStruct, typename="Twist"):  # OK for simple case

# For geometry_msgs/Twist, the DDS typename is "geometry_msgs::msg::dds_::Twist_"
# The bridge handles the mapping, but if you write your own bridge logic,
# use the correct DDS type name.
```

When unsure, inspect what the bridge publishes:
```bash
# List DDS readers/writers discovered by the bridge
curl http://localhost:8000/@/local/ros2/dds/**
```

Start the bridge with the REST plugin enabled: `zenoh-bridge-ros2dds --rest-http-port 8000`.

### 5. Not Setting `complete(true)` on Storage Queryables

**Symptom:** Late-joining ROS2 nodes with `TRANSIENT_LOCAL` QoS don't receive historical data that was published before they started.

**Fix:** When using a zenoh storage to serve historical data to late joiners (replacing DDS `TRANSIENT_LOCAL`), declare the queryable with `complete: true` to signal that it can answer all queries for its key space.

The bridge handles `TRANSIENT_LOCAL` automatically via `PublicationCache`. The default history multiplier is 10× the publisher's history depth. For topics with many publishers, increase it:

```json5
{
  plugins: {
    ros2dds: {
      transient_local_cache_multiplier: 20,
    }
  }
}
```

### 6. `reliable_routes_blocking: true` Recreating the Publisher Stall

**Symptom:** After migrating to the bridge, robot arm commands are still intermittently delayed when a monitoring subscriber is slow.

**Fix:** Set `reliable_routes_blocking: false`. The default `true` value preserves DDS RELIABLE semantics end-to-end, which means the publisher stall can propagate through the bridge. Setting it to `false` allows the bridge to drop messages to congested subscribers rather than blocking the publisher.

---

## Admin Space: Observing Bridge State

The bridge exposes its internal routing state via zenoh admin space. Start the bridge with the REST plugin to query it over HTTP:

```bash
zenoh-bridge-ros2dds --rest-http-port 8000
```

Useful queries:
```bash
# All ROS nodes discovered by this bridge
curl http://localhost:8000/@/local/ros2/node/**

# All DDS readers/writers (useful for debugging endpoint counts)
curl http://localhost:8000/@/local/ros2/dds/**

# All active zenoh routes (topic → zenoh key mappings)
curl http://localhost:8000/@/local/ros2/route/**

# Routes for cmd_vel across all bridges (multi-host view)
curl http://localhost:8000/@/*/ros2/route/**/cmd_vel
```

The `@/*/ros2/route/**` pattern queries all bridges connected to the same zenoh network, giving a network-wide view of what is being routed where. This is invaluable when debugging multi-robot scoping issues or unexpected topic routing.

---

## Migration Checklist

### Pre-Migration
- [ ] Baseline current DDS network traffic (bandwidth, discovery storms)
- [ ] Identify all ROS2 domain IDs in use
- [ ] Document all topics, services, and actions that cross host boundaries
- [ ] Decide on namespace scheme for multi-robot deployments

### Phase 1 (Bridge)
- [ ] Install `zenoh-bridge-ros2dds` on each robot
- [ ] Configure `ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST` (or equivalent) on all robot nodes
- [ ] Verify `ros2 topic list`, `ros2 service list`, `ros2 action list` work from operator
- [ ] Verify `rviz2` connects correctly
- [ ] Measure network traffic reduction

### Phase 2 (Multi-site)
- [ ] Deploy central zenoh router
- [ ] Configure unique `namespace` per robot
- [ ] Test cross-robot topic isolation (robot1/cmd_vel does not reach robot2)
- [ ] Test service and action bridging

### Phase 3 (Native nodes, optional)
- [ ] Identify nodes to replace (start with leaves: sensors and actuators)
- [ ] Install `pycdr2` for CDR serialization
- [ ] Validate each native node against ROS2 counterpart before switching
- [ ] Decommission bridge on robots where all nodes are native zenoh

### Phase 4 (Full zenoh, optional)
- [ ] Remove CDR dependency where no ROS2 tooling touches the data path
- [ ] Switch to [QUIC](quic-guide.md) transport if on Wi-Fi
- [ ] Apply topic filtering and [QoS](qos-guide.md) priority config for bandwidth optimization
- [ ] Configure `reliable_routes_blocking: false` to eliminate publisher stall risk

## See Also

- [Plugin DDS Bridge Guide](plugin-dds-bridge-guide.md) — full reference for `zenoh-bridge-ros2dds` and `zenoh-bridge-dds` configuration
- [DDS Context Guide](dds-context-guide.md) — detailed analysis of the DDS scalability problems this migration solves
- [Node Types Guide](node-types-guide.md) — how to choose the right Zenoh topology for your robot fleet
- [Scouting Guide](scouting-guide.md) — configuring discovery to replace DDS multicast across Wi-Fi and WAN links
- [Key Expressions Guide](key-expressions-guide.md) — how ROS2 topic names map to Zenoh key expressions
