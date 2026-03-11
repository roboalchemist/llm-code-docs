# Zenoh ROS 2 Integration: Complete Documentation

---

## Table of Contents

1. [Overview](#1-overview)
2. [Architecture](#2-architecture)
3. [Installation](#3-installation)
4. [What Gets Bridged](#4-what-gets-bridged)
5. [Key Concepts](#5-key-concepts)
6. [Configuration Reference](#6-configuration-reference)
7. [Deployment Patterns](#7-deployment-patterns)
8. [Multi-Robot Patterns](#8-multi-robot-patterns)
9. [Example Configurations](#9-example-configurations)
10. [TurtleBot3 / ROS 2 Demo Walkthrough](#10-turtlebot3--ros-2-demo-walkthrough)
11. [Admin Space & Observability](#11-admin-space--observability)
12. [Troubleshooting](#12-troubleshooting)

---

## 1. Overview

`zenoh-bridge-ros2dds` bridges all ROS 2 communications — topics, services, actions, and graph discovery — over the Zenoh protocol. It intercepts DDS traffic on the local machine and relays it across Zenoh networks, enabling ROS 2 systems to communicate across machines, networks, and even cloud infrastructure without exposing raw DDS multicast traffic beyond the local host.

### Why Zenoh Instead of Raw DDS?

ROS 2 relies on DDS (Data Distribution Service), which uses UDP multicast for discovery and communication. Multicast works well on a single LAN but does not cross routers, traverse firewalls well, or scale to large fleets. Zenoh solves these problems by:

- Replacing multicast discovery with configurable point-to-point or gossip-based discovery
- Supporting TCP, UDP unicast, TLS, QUIC, and WebSocket transports
- Providing bandwidth control via downsampling (`pub_max_frequencies`)
- Supporting cloud and edge deployments via a router/plugin architecture
- Giving each robot a namespace so fleet topics do not collide

---

## 2. Architecture

### Two Deployment Forms

The bridge ships as two artifacts that share identical configuration and behavior:

| Form | Name | Use Case |
|---|---|---|
| Standalone executable | `zenoh-bridge-ros2dds` | Simplest deployment; run alongside ROS 2 nodes |
| Zenoh router plugin | `zenoh-plugin-ros2dds` | Load dynamically into `zenohd`; share a single router process |

### How the Bridge Works

```
┌──────────────────────────────────────┐
│           Robot (ROS 2 host)         │
│                                      │
│  ROS Node A ──┐                      │
│  ROS Node B ──┼──► DDS Domain 0 ──► zenoh-bridge-ros2dds ──► Zenoh network
│  ROS Node C ──┘                      │
└──────────────────────────────────────┘
```

1. The bridge joins the DDS domain (default: domain 0) and participates in standard DDS discovery.
2. It discovers all ROS 2 publishers, subscribers, service servers/clients, and action servers/clients.
3. For each discovered interface, it creates a bidirectional route between the DDS topic and a Zenoh key expression.
4. Remote bridges or native Zenoh applications can then communicate over that key expression.

### Zenoh Session Modes

Starting from v0.11.0, the bridge defaults to **router** mode:

- Listens on TCP port 7447 on all interfaces
- Does **not** auto-connect to other discovered bridges
- Remote bridges must be told explicitly to connect via `-e` or the `connect` section in config

Prior to v0.11.0, the bridge defaulted to **peer** mode (auto-connects to any discovered peer).

---

## 3. Installation

### Linux Debian / Ubuntu (Recommended)

```bash
# Add the Eclipse Zenoh repository
curl -L https://download.eclipse.org/zenoh/debian-repo/zenoh-public-key \
  | sudo gpg --dearmor --yes --output /etc/apt/keyrings/zenoh-public-key.gpg

echo "deb [signed-by=/etc/apt/keyrings/zenoh-public-key.gpg] \
  https://download.eclipse.org/zenoh/debian-repo/ /" \
  | sudo tee -a /etc/apt/sources.list > /dev/null

sudo apt update

# Install the standalone bridge
sudo apt install zenoh-bridge-ros2dds

# OR install the router plugin
sudo apt install zenoh-plugin-ros2dds
```

### Manual Binary Installation

Download from: https://download.eclipse.org/zenoh/zenoh-plugin-ros2dds/latest/

```bash
# For the standalone bridge
unzip zenoh-bridge-ros2dds-<version>-<platform>.zip
./zenoh-bridge-ros2dds

# For the plugin (place alongside zenohd or in /usr/lib)
unzip zenoh-plugin-ros2dds-<version>-<platform>.zip
```

### Docker

```bash
# Latest release
docker pull eclipse/zenoh-bridge-ros2dds:latest

# Nightly build
docker pull eclipse/zenoh-bridge-ros2dds:nightly

# Run (example)
docker run --network host eclipse/zenoh-bridge-ros2dds:latest
```

> **Note:** `--network host` is typically required so the bridge can reach DDS traffic on the local machine.

### Build from Source

**Prerequisites:**

```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup update

# Install LLVM/Clang (Debian/Ubuntu)
sudo apt install llvm-dev libclang-dev cmake

# Install CMake (required to build CycloneDDS)
sudo apt install cmake
```

```bash
git clone https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds.git
cd zenoh-plugin-ros2dds
cargo build --release
# Outputs: target/release/zenoh-bridge-ros2dds
#          target/release/libzenoh_plugin_ros2dds.so
```

### ROS 2 Package Build

```bash
# From workspace root
rosdep install --from-paths . --ignore-src -r -y
colcon build --packages-select zenoh_bridge_ros2dds \
             --cmake-args -DCMAKE_BUILD_TYPE=Release
```

---

## 4. What Gets Bridged

The bridge automatically discovers and routes the following ROS 2 interface types:

### Topics (Publishers and Subscribers)

All DDS topics corresponding to ROS 2 topics are bridged bidirectionally. A publisher on one side of the bridge is visible as a publisher to subscribers on the other side, and vice versa.

**Zenoh key expression mapping:**

ROS 2 topic names are mapped to Zenoh key expressions following a convention derived from the DDS topic name. ROS 2 DDS topic names use the prefix `rt/` (for "ros topic"):

| ROS 2 topic | Zenoh key expression (no namespace) |
|---|---|
| `/cmd_vel` | `rt/cmd_vel` |
| `/scan` | `rt/scan` |
| `/rosout` | `rt/rosout` |
| `/tf` | `rt/tf` |
| `/robot/odom` | `rt/robot/odom` |

When a namespace is configured (e.g., `/bot1`), the namespace is prepended:

| ROS 2 topic | Zenoh key expression (namespace `/bot1`) |
|---|---|
| `/cmd_vel` | `bot1/rt/cmd_vel` |
| `/scan` | `bot1/rt/scan` |
| `/rosout` | `bot1/rt/rosout` |
| `/tf` | `bot1/rt/tf` |

> **Important:** The namespace is applied to **all** topics, including absolute paths like `/rosout`, `/tf`, and `/tf_static`.

### Services (Clients and Servers)

ROS 2 services are mapped to Zenoh Queryables. A service call from a ROS 2 client is translated into a Zenoh `get()` query; the service server's response is returned as a reply.

**Zenoh key expression mapping** (prefix `rq/` for request, `rr/` for reply, or via Queryable):

| ROS 2 service | Zenoh key expression |
|---|---|
| `/set_parameters` | `rq/set_parameters` / `rr/set_parameters` |
| `/robot/get_state` | `rq/robot/get_state` |

### Actions (Clients and Servers)

ROS 2 actions are composed of three sub-services (send_goal, cancel_goal, get_result) plus feedback and status topics. The bridge handles all of these automatically, mapping them to Zenoh Queryables (for the service parts) and key expressions (for feedback and status).

### ROS 2 Graph Discovery

The bridge propagates ROS 2 graph information (which nodes exist, which topics/services/actions they expose) across the Zenoh network. This means that tools like `ros2 topic list`, `ros2 service list`, and `ros2 action list` work correctly on a host connected through the bridge, as though all remote ROS 2 nodes were local.

---

## 5. Key Concepts

### DDS Domain ID

ROS 2 uses DDS domain IDs to partition communications. Nodes with different domain IDs cannot communicate over DDS. The bridge joins a specific DDS domain (configured via `domain` or the `ROS_DOMAIN_ID` environment variable, defaulting to `0`).

**Critical rule:** There must be **no direct DDS path** between two hosts that are bridged. If DDS traffic leaks between bridged hosts, you will see duplicate or looping messages.

To prevent DDS leakage, use **one** of these approaches:

```bash
# Option 1: Restrict DDS to localhost (ROS Iron and later)
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
sudo ip l set lo multicast on   # enable multicast on loopback

# Option 2: Restrict DDS to localhost (before ROS Iron)
export ROS_LOCALHOST_ONLY=1
sudo ip l set lo multicast on

# Option 3: Use different ROS_DOMAIN_ID on each host
export ROS_DOMAIN_ID=1   # on host A
export ROS_DOMAIN_ID=2   # on host B

# Option 4: CycloneDDS XML config to restrict to specific interfaces
export CYCLONEDDS_URI=file:///path/to/cyclonedds.xml
```

Example `cyclonedds.xml` for a robot with a USB inter-board link:

```xml
<CycloneDDS>
  <Domain>
    <General>
      <Interfaces>
        <NetworkInterface name="usb0"/>
        <NetworkInterface address="127.0.0.1" multicast="true"/>
      </Interfaces>
      <DontRoute>true</DontRoute>
    </General>
  </Domain>
</CycloneDDS>
```

### Namespace Remapping

The `namespace` configuration option prefixes all bridged interface names when they are published to Zenoh. This is the primary mechanism for multi-robot isolation.

```
Robot config:  namespace: "/bot1"

DDS topic:     /cmd_vel
Zenoh key:     bot1/rt/cmd_vel

DDS topic:     /scan
Zenoh key:     bot1/rt/scan
```

On a monitoring host, you have two options:

**Option A:** Run a bridge with the same namespace. ROS 2 tools work without any remapping.

```bash
zenoh-bridge-ros2dds -e tcp/<robot-ip>:7447 --namespace /bot1
# Now: ros2 topic list shows /cmd_vel, /scan, etc.
```

**Option B:** Run a bridge without a namespace. Use topic remapping in ROS tools.

```bash
zenoh-bridge-ros2dds -e tcp/<robot-ip>:7447
# Now: ros2 topic list shows /bot1/cmd_vel, /bot1/scan, etc.
rviz2 --ros-args -r /tf:=/bot1/tf -r /tf_static:=/bot1/tf_static
```

### QoS Preservation

The bridge preserves ROS 2 Quality of Service settings:

**Reliability:**
- `RELIABLE` DDS writers → Zenoh `CongestionControl::Block` (when `reliable_routes_blocking: true`)
- `BEST_EFFORT` DDS writers → Zenoh `CongestionControl::Drop`

**Durability (TRANSIENT_LOCAL):**

When a `TRANSIENT_LOCAL` publisher is discovered, the bridge creates a `PublicationCache` in Zenoh to store recent publications. Late-joining subscribers (on other bridges) query this cache to receive the historical data they would have received from the DDS publisher directly.

The cache size is `history_length × transient_local_cache_multiplier` (default multiplier: 10).

### Topic Name to Zenoh Key Expression Convention

The mapping follows the DDS topic name as assigned by the ROS 2 middleware:

| Interface type | DDS prefix | Example DDS name | Zenoh key |
|---|---|---|---|
| Topic | `rt/` | `rt/cmd_vel` | `rt/cmd_vel` |
| Service request | `rq/` | `rq/set_parameters` | `rq/set_parameters` |
| Service reply | `rr/` | `rr/set_parameters` | `rr/set_parameters` |
| Action goal | `rq/` | `rq/navigate_to_pose/_action/send_goal` | (mapped internally) |

With namespace `/bot1`:
- `rt/cmd_vel` → `bot1/rt/cmd_vel`
- `rq/set_parameters` → `bot1/rq/set_parameters`

---

## 6. Configuration Reference

The bridge is configured via a JSON5 file passed with `-c <file>`. The full reference file is `DEFAULT_CONFIG.json5`. All settings are optional; values shown are defaults.

### Configuration File Structure

```json5
{
  plugins: {
    ros2dds: {
      // ROS 2 bridge settings go here
    }
  },
  // Zenoh session settings (mode, connect, listen, scouting)
}
```

---

### `nodename`

**What it does:** Sets the ROS 2 node name used by the bridge itself on the DDS domain. This is the name the bridge appears as in `ros2 node list`.

**Default:** `"zenoh_bridge_ros2dds"`

**Example:**

```json5
nodename: "my_bridge_node"
```

---

### `namespace`

**What it does:** Sets a ROS 2 namespace that is:
1. Applied to the bridge's own node.
2. Prepended to **all** bridged interface names when routing to Zenoh (topics, services, actions — including `/rosout`, `/tf`, `/tf_static`).

**Default:** `"/"` (no prefix applied)

**Example:**

```json5
namespace: "/robot1"
```

With this setting, a robot's `/scan` topic appears as `robot1/rt/scan` in Zenoh.

---

### `domain`

**What it does:** Specifies the DDS domain ID the bridge joins. All ROS 2 nodes in the same domain on the same host will be discovered and bridged.

**Default:** `0`, or the value of `$ROS_DOMAIN_ID` if set.

**Example:**

```json5
domain: 42
```

---

### `ros_localhost_only`

**What it does:** When `true`, restricts all DDS discovery and traffic to the loopback interface (`127.0.0.1`). Equivalent to setting `ROS_LOCALHOST_ONLY=1`. Use this to prevent DDS traffic from leaking to the physical network when bridging with zenoh.

**Default:** `false`, unless `ROS_LOCALHOST_ONLY=1` is set in the environment.

**Example:**

```json5
ros_localhost_only: true
```

> **Note:** Also run `sudo ip l set lo multicast on` to ensure DDS multicast works on loopback.

---

### `ros_automatic_discovery_range`

**What it does:** Controls how far the bridge's DDS participant attempts to discover other ROS 2 nodes. Available in ROS 2 Iron and later.

**Valid values:**

| Value | Meaning |
|---|---|
| `"SUBNET"` | Discover any node reachable via multicast (default DDS behavior) |
| `"LOCALHOST"` | Only discover nodes on the same machine |
| `"OFF"` | No discovery at all |
| `"SYSTEM_DEFAULT"` | Do not modify any discovery settings |

**Default:** `"SUBNET"`

**Example:**

```json5
ros_automatic_discovery_range: "LOCALHOST"
```

---

### `ros_static_peers`

**What it does:** A semicolon-separated list of IP addresses that ROS 2 should explicitly attempt to discover nodes on. Useful when multicast is unavailable. Available in ROS 2 Iron and later.

**Default:** unset

**Example:**

```json5
ros_static_peers: "192.168.1.10;192.168.1.11"
```

---

### `shm_enabled`

**What it does:** Enables Iceoryx shared memory for DDS communications. Requires the bridge to be built with the `dds_shm` feature flag. Cannot be used together with `prefix_symbols`.

**Default:** `false`

**Example:**

```json5
shm_enabled: true
```

---

### `allow` / `deny`

**What it does:** Filters which ROS 2 interfaces are routed over Zenoh. Each entry is a regular expression matched against the full interface name. You cannot set both `allow` and `deny` simultaneously.

**Behavior:**

- **`allow`**: Only listed interfaces are bridged. An interface type with an empty list or not mentioned means **no** interfaces of that type are bridged.
- **`deny`**: All interfaces are bridged **except** those listed. An interface type with an empty list or not mentioned means **all** interfaces of that type are bridged.
- **Neither set**: All interfaces are bridged.

**Interface types:** `publishers`, `subscribers`, `service_servers`, `service_clients`, `action_servers`, `action_clients`

**Default:** unset (all interfaces bridged)

**Example — allow only specific interfaces:**

```json5
allow: {
  publishers: [".*/laser_scan", "/tf", ".*/pose"],
  subscribers: [".*/cmd_vel"],
  service_servers: [".*/.*_parameters"],
  service_clients: [],
  action_servers: [".*/rotate_absolute"],
  action_clients: [],
}
```

**Example — deny noisy system topics:**

```json5
deny: {
  publishers: ["/rosout", "/parameter_events"],
  subscribers: ["/rosout"],
  service_servers: [".*/set_parameters"],
  service_clients: [".*/set_parameters"],
  action_servers: [],
  action_clients: [],
}
```

---

### `pub_max_frequencies`

**What it does:** Rate-limits publication routing to Zenoh for matching publishers. If a publisher produces messages faster than the configured limit, the bridge will drop excess messages (downsampling). Useful for reducing bandwidth on high-rate sensors like LiDAR or cameras.

**Format:** `["<regex>=<float_hz>", ...]`

- `regex`: Regular expression matching the publisher's topic name
- `float_hz`: Maximum frequency in Hz

**Default:** unset (no rate limiting)

**Example:**

```json5
pub_max_frequencies: [
  ".*/laser_scan=5",   // max 5 Hz for all laser_scan topics
  "/tf=10",            // max 10 Hz for /tf
  ".*/camera/image=2"  // max 2 Hz for camera images
]
```

---

### `pub_priorities`

**What it does:** Assigns Zenoh publication priorities to matching publisher topics. Higher-priority messages are preferentially transmitted when the network is congested. Optionally enables the "express" policy for reduced batching latency on a topic.

**Format:** `["<regex>=<integer>[:<express>]", ...]`

**Priority range:** 1 (highest) to 7 (lowest), default is 5.

**`:express` option:** When present, the message is sent immediately without waiting to be batched with other messages. Reduces latency but increases per-message overhead.

**Default:** unset (all topics at default priority 5)

**Example:**

```json5
pub_priorities: [
  "/scan=1:express",  // highest priority, immediate send
  "/pose=2",          // high priority, batched
  "/map=6",           // low priority
  "/rosout=7"         // lowest priority
]
```

---

### `reliable_routes_blocking`

**What it does:** Controls the Zenoh congestion control policy for `RELIABLE` DDS writers.

- `true`: Uses `CongestionControl::Block` — if the network is congested, the bridge blocks the DDS reader/writer until the message can be sent. Preserves all messages at the cost of potential backpressure.
- `false`: Uses `CongestionControl::Drop` — drops messages under congestion. Never blocks DDS.

`BEST_EFFORT` publishers always use `CongestionControl::Drop` regardless of this setting.

**Default:** `true`

**Example:**

```json5
reliable_routes_blocking: false
```

---

### `queries_timeout`

**What it does:** Configures timeout durations for Zenoh queries used by services, action calls, and TRANSIENT_LOCAL subscriber history retrieval.

**Fields:**

| Field | Description | Default |
|---|---|---|
| `default` | Fallback timeout for all queries not matched below | `5.0` seconds |
| `transient_local_subscribers` | Timeout when querying publishers for historical TRANSIENT_LOCAL data | `1.0` seconds |
| `services` | Timeout for service calls; can be a float or a `["<regex>=<float>", ...]` list | `5.0` seconds |
| `actions.send_goal` | Timeout for sending a goal to an action server | `5.0` seconds |
| `actions.cancel_goal` | Timeout for cancelling an action goal | `5.0` seconds |
| `actions.get_result` | Timeout for waiting on an action result; can be a float or list | `300.0` seconds |

**Default:** As shown in the table above.

**Example:**

```json5
queries_timeout: {
  default: 5.0,
  transient_local_subscribers: 1.0,
  services: ["add_two_ints=0.5", ".*=1.0"],
  actions: {
    send_goal: 1.0,
    cancel_goal: 1.0,
    get_result: [".*long_mission=3600", ".*short_action=10.0", ".*=300"]
  }
}
```

---

### `transient_local_cache_multiplier`

**What it does:** Determines the size of the Zenoh `PublicationCache` created for each `TRANSIENT_LOCAL` topic route. Since one route may serve multiple publishers on the same topic, the cache size is:

```
cache_size = publisher_history_length × transient_local_cache_multiplier
```

Increase this value if you have more than 10 `TRANSIENT_LOCAL` publishers on the same topic.

**Default:** `10`

**Example:**

```json5
transient_local_cache_multiplier: 20
```

---

### `work_thread_num`

**What it does:** Sets the number of worker threads in the Tokio async runtime used by the plugin. Worker threads handle non-blocking tasks. **Only applies when running as a plugin inside `zenohd`; has no effect on the standalone bridge.**

**Default:** `2`

**Example:**

```json5
work_thread_num: 4
```

---

### `max_block_thread_num`

**What it does:** Sets the maximum number of blocking threads in the Tokio async runtime used by the plugin. Blocking threads handle I/O and other blocking operations, spawned on demand. **Only applies when running as a plugin inside `zenohd`; has no effect on the standalone bridge.**

**Default:** `50`

**Example:**

```json5
max_block_thread_num: 100
```

---

### Zenoh Session Configuration

These fields appear at the top level of the config file (not under `plugins.ros2dds`) and control the Zenoh session itself.

#### `mode`

```json5
mode: "router"   // "router" | "peer" | "client"
```

Default is `"router"`. Routers listen for incoming connections; peers connect to peers and routers; clients connect only to routers.

#### `connect`

```json5
connect: {
  endpoints: [
    "tcp/192.168.1.100:7447",
    "tls/cloud.example.com:7447"
  ]
}
```

Specifies remote bridges or routers to connect to at startup.

#### `listen`

```json5
listen: {
  endpoints: [
    "tcp/0.0.0.0:7447"
  ]
}
```

Specifies what interfaces and ports to accept incoming connections on. Default in router mode: `tcp/0.0.0.0:7447`.

#### `scouting`

```json5
scouting: {
  multicast: {
    enabled: true,
    address: "224.0.0.224:7446",
    autoconnect: { router: [], peer: ["router", "peer"] }
  },
  gossip: {
    enabled: true,
    multihop: false,
    autoconnect: { router: [], peer: ["router", "peer"] }
  }
}
```

To enable automatic connection between routers (e.g., for local network auto-discovery of bridges):

```json5
scouting: {
  multicast: {
    autoconnect: { router: "router" }
  },
  gossip: {
    autoconnect: { router: "router" }
  }
}
```

---

## 7. Deployment Patterns

### Pattern 1: Single Machine

Run the bridge on the same host as all ROS 2 nodes. Useful for exposing a local ROS 2 system to remote Zenoh applications without a second bridge.

```
┌─────────────────────────────┐
│         Robot Host          │
│                             │
│  ROS 2 Nodes ──► DDS ──────►│──► zenoh-bridge-ros2dds (port 7447)
│                             │         │
└─────────────────────────────┘         │ TCP
                                        │
                              Remote Zenoh App / Monitoring Tool
```

**Setup:**

```bash
# On the robot
export ROS_LOCALHOST_ONLY=1
sudo ip l set lo multicast on
zenoh-bridge-ros2dds

# On the remote monitoring host
zenoh-bridge-ros2dds -e tcp/<robot-ip>:7447
ros2 topic list
```

---

### Pattern 2: Multi-Machine Local Network

Each machine runs its own bridge. Bridges connect to each other. DDS is restricted to localhost on each machine to prevent DDS traffic from crossing the network.

```
┌──────────────┐    TCP     ┌──────────────┐
│   Machine A  │◄──────────►│   Machine B  │
│              │            │              │
│ ROS Nodes    │            │ ROS Nodes    │
│ Bridge A     │            │ Bridge B     │
└──────────────┘            └──────────────┘
```

**Setup:**

```bash
# On Machine A (acts as the "server")
export ROS_LOCALHOST_ONLY=1
sudo ip l set lo multicast on
zenoh-bridge-ros2dds
# Listens on tcp/0.0.0.0:7447 by default

# On Machine B (connects to A)
export ROS_LOCALHOST_ONLY=1
sudo ip l set lo multicast on
zenoh-bridge-ros2dds -e tcp/<machine-a-ip>:7447
```

For automatic discovery between machines on the same LAN (no explicit `-e` needed), enable router autoconnect:

```json5
// bridge.config.json5
{
  scouting: {
    multicast: {
      autoconnect: { router: "router" }
    }
  }
}
```

---

### Pattern 3: Cloud + Robot (Edge/Cloud Architecture)

A Zenoh router runs in the cloud. The robot's bridge connects to it as a client. A monitoring application on any internet-connected host also connects to the cloud router.

```
┌─────────────┐   TCP/TLS    ┌──────────────────┐   TCP/TLS   ┌─────────────────┐
│    Robot    │◄────────────►│  Cloud (zenohd)  │◄───────────►│ Monitoring Host │
│             │              │                  │             │                 │
│ ROS Nodes   │              │  Zenoh Router    │             │  ros2 topic     │
│ Bridge      │              │  (port 7447)     │             │  rviz2          │
│ (client)    │              └──────────────────┘             └─────────────────┘
└─────────────┘
```

**Cloud router** (`zenohd` with no special config, just listening on 7447):

```bash
zenohd
```

**Robot bridge config** (`robot.config.json5`):

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/<cloud-ip>:7447"]
  },
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_localhost_only: true,
      domain: 0
    }
  }
}
```

```bash
# On robot
zenoh-bridge-ros2dds -c robot.config.json5
```

**Monitoring host:**

```bash
zenoh-bridge-ros2dds -e tcp/<cloud-ip>:7447 --namespace /robot1
ros2 topic list  # sees /scan, /cmd_vel, etc.
```

---

### Pattern 4: Multi-Robot Fleet

Each robot has its own bridge with a unique namespace. A cloud router aggregates traffic. The monitoring host connects to the cloud.

```
Robot 1 (namespace /bot1) ──────────────────────────┐
Robot 2 (namespace /bot2) ────────────────────────► Cloud zenohd ◄──── Fleet Monitor
Robot 3 (namespace /bot3) ──────────────────────────┘
```

**Robot bridges:**

```bash
# Robot 1
zenoh-bridge-ros2dds --namespace /bot1 -e tcp/<cloud>:7447 -m client

# Robot 2
zenoh-bridge-ros2dds --namespace /bot2 -e tcp/<cloud>:7447 -m client

# Robot 3
zenoh-bridge-ros2dds --namespace /bot3 -e tcp/<cloud>:7447 -m client
```

**Fleet monitor** (no namespace — sees all robots' namespaced topics):

```bash
zenoh-bridge-ros2dds -e tcp/<cloud>:7447 -m client
ros2 topic list
# /bot1/scan
# /bot1/cmd_vel
# /bot2/scan
# /bot2/cmd_vel
# /bot3/scan
# /bot3/cmd_vel
```

---

## 8. Multi-Robot Patterns

### Namespace Isolation Per Robot

Each robot's `zenoh-bridge-ros2dds` is configured with a unique namespace. No changes are required on the individual ROS 2 nodes — they continue using their standard topic names within the DDS domain. The bridge handles the namespacing transparently.

**Robot-side:** Nodes publish on `/scan`, `/cmd_vel`, `/odom` as normal.
**Cloud/monitor-side:** These appear as `/botX/scan`, `/botX/cmd_vel`, `/botX/odom`.

### Fleet-Wide Topic Aggregation

To subscribe to the same topic from all robots simultaneously, use Zenoh wildcard key expressions from native Zenoh applications:

```python
import zenoh

session = zenoh.open(zenoh.Config())
# Subscribe to /scan from all robots at once
sub = session.declare_subscriber("*/rt/scan", lambda sample: handle_scan(sample))
```

Or query all robots' status:

```python
replies = session.get("*/rt/diagnostics")
```

### Mixed Fleet

Different robot types can share the same Zenoh network as long as each has a unique namespace. A monitoring bridge can subscribe to any combination of namespaces:

```bash
# Monitor robot1 specifically
zenoh-bridge-ros
---

## See Also
- [deployment.md](deployment.md) — Network topology and multi-host deployment patterns
- [concepts.md](concepts.md) — Core zenoh abstractions mapped to ROS 2 concepts
- [faq.md](faq.md) — Common questions including ROS 2 integration scenarios
