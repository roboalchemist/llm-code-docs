# Eclipse Zenoh ROS 2 Integration — Complete Documentation

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [What Gets Bridged](#what-gets-bridged)
5. [Key Concepts](#key-concepts)
6. [Configuration Reference](#configuration-reference)
7. [Deployment Patterns](#deployment-patterns)
8. [Multi-Robot Patterns](#multi-robot-patterns)
9. [Example Configurations](#example-configurations)
10. [TurtleBot3 Demo Walkthrough](#turtlebot3-demo-walkthrough)
11. [Admin Space and Monitoring](#admin-space-and-monitoring)
12. [Troubleshooting](#troubleshooting)

---

## Overview

`zenoh-bridge-ros2dds` bridges all ROS 2 communications—topics, services, actions, and graph discovery—over the Eclipse Zenoh protocol. This enables ROS 2 robots to communicate across networks where direct DDS multicast would be impractical or impossible: across subnets, over the internet, through NAT, and to cloud infrastructure.

The bridge is built on top of [CycloneDDS](https://github.com/eclipse-cyclonedds/cyclonedds) and participates in the local DDS domain exactly like any other ROS 2 node. On the other side it speaks native Zenoh, inheriting Zenoh's efficient routing, multiplexing, and transport-layer flexibility.

```
  Robot Host                           Remote Host / Cloud
  ┌────────────────────────────┐       ┌────────────────────────────┐
  │  ROS 2 Node A  ──DDS──┐   │       │   ┌──DDS── ROS 2 Node C   │
  │  ROS 2 Node B  ──DDS──┤   │       │   ├──DDS── ROS 2 Node D   │
  │                        ▼   │       │   ▼                        │
  │              zenoh-bridge  │◄─────►│  zenoh-bridge             │
  │              ros2dds       │ zenoh │  ros2dds                  │
  └────────────────────────────┘       └────────────────────────────┘
```

### Plugin or Bridge?

The software ships in two forms with identical features and configuration:

| Form | Package | Use Case |
|---|---|---|
| **Standalone executable** | `zenoh-bridge-ros2dds` | Run directly on a host alongside ROS 2 nodes |
| **Zenoh router plugin** | `zenoh-plugin-ros2dds` | Load dynamically inside `zenohd`; share one router process |

Throughout this document the words *bridge* and *plugin* are interchangeable.

---

## Architecture

### How It Works

1. The bridge joins the DDS domain (same `ROS_DOMAIN_ID` as local ROS nodes).
2. It discovers every publisher, subscriber, service server/client, and action server/client on that domain via standard DDS discovery.
3. For each discovered interface it creates a corresponding Zenoh route:
   - DDS publisher → Zenoh publisher
   - DDS subscriber → Zenoh subscriber (queryable for TRANSIENT_LOCAL)
   - DDS service server → Zenoh queryable
   - DDS service client → Zenoh get() caller
4. All ROS interface names are mapped to Zenoh key expressions using a well-defined convention (see [Topic Name Mapping](#topic-name-mapping)).
5. A second bridge on a remote host mirrors the same mapping, so data flows transparently end-to-end.

### Zenoh Mode

From **v0.11.0** onwards the bridge defaults to `router` mode:

- Listens on `tcp/0.0.0.0:7447` for incoming connections from other bridges or any Zenoh application.
- Does **not** auto-connect to anything on startup.
- Connectivity must be configured explicitly via the `-e` CLI option or `connect.endpoints` in the config file.

Automatic connection between two routers can be re-enabled by adding scouting configuration (see [Connectivity Configuration](#connectivity-configuration)).

---

## Installation

### Linux Debian / Ubuntu (recommended)

```bash
# Add the Eclipse Zenoh repository
curl -L https://download.eclipse.org/zenoh/debian-repo/zenoh-public-key \
  | sudo gpg --dearmor --yes --output /etc/apt/keyrings/zenoh-public-key.gpg

echo "deb [signed-by=/etc/apt/keyrings/zenoh-public-key.gpg] \
  https://download.eclipse.org/zenoh/debian-repo/ /" \
  | sudo tee -a /etc/apt/sources.list > /dev/null

sudo apt update

# Install standalone bridge
sudo apt install zenoh-bridge-ros2dds

# Or install the router plugin
sudo apt install zenoh-plugin-ros2dds
```

### Manual / All Platforms

Download from:

```
https://download.eclipse.org/zenoh/zenoh-plugin-ros2dds/latest/
```

- `zenoh-bridge-ros2dds-<version>-<platform>.zip` — standalone executable
- `zenoh-plugin-ros2dds-<version>-<platform>.zip` — router plugin (`.so`/`.dylib`/`.dll`)

### Docker

```bash
# Latest release
docker pull eclipse/zenoh-bridge-ros2dds:latest

# Nightly build (main branch)
docker pull eclipse/zenoh-bridge-ros2dds:nightly
```

### Build from Source

Prerequisites: Rust toolchain, `llvm-dev`, `libclang-dev`, CMake.

```bash
# Install dependencies (Debian/Ubuntu)
sudo apt install llvm-dev libclang-dev cmake

# Install / update Rust
rustup update

# Build
git clone https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds.git
cd zenoh-plugin-ros2dds
cargo build --release
```

Binaries are placed in `target/release/`.

#### Optional Feature: DDS Symbol Prefixing

If you need to load both `zenoh-plugin-ros2dds` and `zenoh-plugin-dds` in the same router process, build with prefixed symbols to avoid DDS library clashes:

```bash
cargo build --release --features prefix_symbols
```

> **Note:** `prefix_symbols` and `dds_shm` cannot be enabled at the same time.

### ROS 2 Package Build

```bash
# From the repo root
rosdep install --from-paths . --ignore-src -r -y
colcon build --packages-select zenoh_bridge_ros2dds \
             --cmake-args -DCMAKE_BUILD_TYPE=Release
```

---

## What Gets Bridged

### Topics

Every ROS 2 publisher and subscriber on the DDS domain is discovered and routed bidirectionally over Zenoh. QoS reliability (RELIABLE vs BEST_EFFORT) and durability (TRANSIENT_LOCAL) are preserved across the bridge (see [QoS Preservation](#qos-preservation)).

### Services

ROS 2 services are mapped to Zenoh Queryables. A service server on the DDS side becomes a queryable that answers `get()` calls arriving from the Zenoh network. A service client initiates `get()` calls that are routed to the appropriate server.

### Actions

ROS 2 actions are composed of multiple DDS topics and services internally. The bridge handles all of them as a unit, mapping each action to a set of Zenoh key expressions. Action clients and servers are both fully bridged.

### ROS 2 Graph Discovery

The bridge propagates the ROS 2 graph (node names, topic types, QoS) to remote bridges so that `ros2 topic list`, `ros2 service list`, `ros2 action list`, and tools like `rviz2` work correctly on a remote host as if it were on the same LAN.

---

## Key Concepts

### DDS Domain ID

The bridge participates in the DDS domain identified by `ROS_DOMAIN_ID` (default `0`). All ROS nodes that should be bridged must share the same domain ID on a given host.

```bash
# Set explicitly
export ROS_DOMAIN_ID=42
zenoh-bridge-ros2dds
```

Or use the `domain` config key (see [Configuration Reference](#configuration-reference)).

### DDS Isolation — Preventing Loops

> **Critical:** If two hosts are connected by both DDS *and* the Zenoh bridge, traffic will loop. You must ensure DDS traffic cannot flow directly between the bridged hosts.

Choose one of:

1. **Localhost-only DDS** (recommended for single-machine bridge scenarios):

   ```bash
   # ROS 2 Iron and later
   export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
   # Before Iron
   export ROS_LOCALHOST_ONLY=1
   # Also enable multicast on loopback
   sudo ip l set lo multicast on
   ```

2. **Different `ROS_DOMAIN_ID`** on each host.

3. **CycloneDDS interface restriction** via `CYCLONEDDS_URI`:

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

A `namespace` configured on the bridge is prepended to every ROS interface name before it is published to the Zenoh network. This applies to **all** interfaces including `/rosout`, `/tf`, and `/tf_static`.

```
DDS side:   /cmd_vel
Zenoh side: /robot1/cmd_vel   (with namespace: "/robot1")
```

This is the foundation of multi-robot isolation (see [Multi-Robot Patterns](#multi-robot-patterns)).

### Topic Name to Zenoh Key Expression Mapping

ROS 2 DDS topic names follow a convention established by the RMW layer:

| Interface Type | DDS Name Prefix | Example DDS Name | Zenoh Key |
|---|---|---|---|
| Topic | `rt/` | `rt/cmd_vel` | `cmd_vel` |
| Service request | `rq/` | `rq/add_two_ints/_service_event_info` | mapped internally |
| Service response | `rr/` | `rr/add_two_ints/_service_event_info` | mapped internally |
| Action | `ra/` | `ra/navigate_to_pose/_action/...` | mapped internally |

The `rt/` prefix stands for "ROS topic". When writing Zenoh native clients that interoperate with the bridge, use the full DDS name (including `rt/`, `rq/`, etc.) as the Zenoh key expression.

For example, from the Python teleop demo:

```python
# This key expression is the DDS topic name for /turtle1/cmd_vel
session.put('rt/turtle1/cmd_vel', twist_bytes)
```

### QoS Preservation

| DDS QoS | Zenoh Behavior |
|---|---|
| `RELIABLE` | Uses `CongestionControl::Block` (when `reliable_routes_blocking: true`). The route blocks on congestion, back-pressuring the DDS writer. |
| `BEST_EFFORT` | Uses `CongestionControl::Drop`. Data may be dropped under congestion. |
| `TRANSIENT_LOCAL` | The bridge creates a `PublicationCache` on the Zenoh route. Late-joining subscribers receive the cached history from the publisher's `history_length` QoS setting, multiplied by `transient_local_cache_multiplier`. |

---

## Configuration Reference

The bridge is configured via a JSON5 file passed with `-c <file>`. All settings live under the `plugins.ros2dds` key. When using the router plugin, this section goes into the router's config under `plugins`.

Run `zenoh-bridge-ros2dds -h` to see which options are also available as CLI flags (CLI flags override config file values).

---

### `nodename`

The name of the ROS node that the bridge itself creates on the DDS domain.

| | |
|---|---|
| **Default** | `"zenoh_bridge_ros2dds"` |
| **Type** | string |

```json5
nodename: "my_bridge_node"
```

---

### `namespace`

A ROS namespace prepended to every bridged interface name when publishing to Zenoh. Also applied to the bridge's own node.

| | |
|---|---|
| **Default** | `"/"` (no prefix) |
| **Type** | string |

```json5
// Robot 1 bridge config
namespace: "/robot1"

// A topic /cmd_vel on the robot becomes robot1/cmd_vel on Zenoh
```

> **Note:** Setting the namespace on the bridge eliminates the need to configure namespaces on individual ROS nodes. DDS traffic between nodes on the same robot stays un-namespaced internally.

---

### `domain`

The DDS Domain ID the bridge will join.

| | |
|---|---|
| **Default** | `0`, or the value of `$ROS_DOMAIN_ID` if set |
| **Type** | integer |

```json5
domain: 42
```

---

### `ros_localhost_only`

When `true`, restricts all DDS discovery and traffic to `127.0.0.1`. Equivalent to `ROS_LOCALHOST_ONLY=1`.

| | |
|---|---|
| **Default** | `false`, unless `ROS_LOCALHOST_ONLY=1` is set |
| **Type** | boolean |

```json5
ros_localhost_only: true
```

---

### `ros_automatic_discovery_range`

Controls how far DDS discovery propagates. Introduced in ROS 2 Iron.

| | |
|---|---|
| **Default** | `"SUBNET"` |
| **Valid values** | `"SUBNET"`, `"LOCALHOST"`, `"OFF"`, `"SYSTEM_DEFAULT"` |
| **ROS version** | Iron and later |

```json5
ros_automatic_discovery_range: "LOCALHOST"
```

| Value | Behavior |
|---|---|
| `"SUBNET"` | Standard DDS multicast discovery across the subnet |
| `"LOCALHOST"` | Discover only nodes on the same machine |
| `"OFF"` | No discovery at all |
| `"SYSTEM_DEFAULT"` | Do not override any discovery settings |

---

### `ros_static_peers`

A semicolon-separated list of IP addresses for explicit peer discovery. ROS 2 Iron and later.

| | |
|---|---|
| **Default** | unset |
| **Type** | string |

```json5
ros_static_peers: "192.168.1.10;192.168.1.11"
```

---

### `shm_enabled`

Enable Iceoryx shared memory for DDS communications. Requires the bridge to be compiled with the `dds_shm` feature.

| | |
|---|---|
| **Default** | `false` |
| **Type** | boolean |

```json5
shm_enabled: true
```

---

### `allow` / `deny`

Filter which ROS 2 interfaces are bridged. You can specify **either** `allow` or `deny`, but not both.

Each value is a list of regular expressions matched against the full interface name.

**`allow`**: Only the listed interfaces are bridged. An interface type with an empty list or not specified means **no** interfaces of that type are bridged.

**`deny`**: All interfaces are bridged **except** the listed ones. An interface type with an empty list or not specified means **all** interfaces of that type are bridged.

Interface types:

- `publishers`
- `subscribers`
- `service_servers`
- `service_clients`
- `action_servers`
- `action_clients`

```json5
// Allow only specific interfaces
allow: {
  publishers: [".*/laser_scan", "/tf", ".*/pose"],
  subscribers: [".*/cmd_vel"],
  service_servers: [".*/.*_parameters"],
  service_clients: [],
  action_servers: [".*/rotate_absolute"],
  action_clients: [],
},
```

```json5
// Deny specific noisy topics
deny: {
  publishers: ["/rosout", "/parameter_events"],
  subscribers: ["/rosout"],
  service_servers: [".*/set_parameters"],
  service_clients: [".*/set_parameters"],
  action_servers: [],
  action_clients: [],
},
```

---

### `pub_max_frequencies`

Downsampling: cap the publication rate of specific topics over Zenoh. Useful for high-frequency sensors (LiDAR, cameras) where the remote consumer does not need every sample.

Format: `"<regex>=<hz>"`

| | |
|---|---|
| **Default** | unset (no rate limiting) |
| **Type** | list of strings |

```json5
pub_max_frequencies: [
  ".*/laser_scan=5",   // max 5 Hz for any laser_scan topic
  "/tf=10",            // max 10 Hz for /tf
  ".*/image_raw=2",    // max 2 Hz for camera images
]
```

---

### `pub_priorities`

Set Zenoh publication priority for specific topics. Higher-priority publications preempt lower-priority ones when the Zenoh network is congested.

Format: `"<regex>=<priority>[:<policy>]"`

- Priority range: `1` (highest) to `7` (lowest). Default is `5`.
- Optional `:express` policy sends the message immediately without batching, reducing latency at the cost of throughput.

| | |
|---|---|
| **Default** | unset (priority 5 for all) |
| **Type** | list of strings |

```json5
pub_priorities: [
  "/scan=1:express",   // highest priority, no batching
  "/pose=2",           // high priority
  "/map=6",            // low priority (large, infrequent)
  "/rosout=7",         // lowest priority
]
```

---

### `reliable_routes_blocking`

When `true`, publications from a RELIABLE DDS writer use `CongestionControl::Block` in Zenoh. The route will block (and back-pressure the DDS writer) if the Zenoh network is congested, preventing data loss for RELIABLE topics.

When `false` (or for BEST_EFFORT writers), `CongestionControl::Drop` is used.

| | |
|---|---|
| **Default** | `true` |
| **Type** | boolean |

```json5
reliable_routes_blocking: true
```

---

### `queries_timeout`

Timeout configuration for Zenoh queries used by services, actions, and TRANSIENT_LOCAL subscribers.

Each field accepts either a single float (seconds, applies to all matching queries) or a list of `"<regex>=<float>"` strings for per-interface timeouts.

| | |
|---|---|
| **Default** | `default: 5.0`, `actions.get_result: 300.0` |

```json5
queries_timeout: {
  // Fallback timeout for any query not matched below
  default: 5.0,

  // Timeout when querying publishers for TRANSIENT_LOCAL history
  transient_local_subscribers: 1.0,

  // Per-service timeouts: first match wins
  services: ["add_two_ints=0.5", ".*=1.0"],

  // Action sub-timeouts
  actions: {
    send_goal: 1.0,
    cancel_goal: 1.0,
    // Long-running missions get a long timeout
    get_result: [".*long_mission=3600", ".*short_action=10.0", ".*=300"],
  }
},
```

---

### `transient_local_cache_multiplier`

Determines the size of the `PublicationCache` created for TRANSIENT_LOCAL publisher routes. The cache stores publications for late-joining subscribers.

Cache size = `publisher history_length QoS` × `transient_local_cache_multiplier`

Because one route may serve multiple publishers on the same topic, this multiplier accounts for that.

| | |
|---|---|
| **Default** | `10` |
| **Type** | integer |

```json5
// Increase if more than 10 TRANSIENT_LOCAL publishers share a topic
transient_local_cache_multiplier: 20
```

---

### `work_thread_num`

Number of Tokio worker threads for the asynchronous runtime. **Plugin only** — has no effect on the standalone bridge.

| | |
|---|---|
| **Default** | `2` |
| **Type** | integer |

```json5
work_thread_num: 4
```

---

### `max_block_thread_num`

Maximum number of Tokio blocking threads for I/O operations. **Plugin only**.

| | |
|---|---|
| **Default** | `50` |
| **Type** | integer |

```json5
max_block_thread_num: 100
```

---

### Zenoh-Level Configuration

These are standard Zenoh settings that sit alongside the `plugins` block, not inside `ros2dds`.

#### `mode`

```json5
mode: "router"  // or "peer" or "client"
```

#### `connect.endpoints`

```json5
connect: {
  endpoints: ["tcp/192.168.1.100:7447"]
}
```

#### `listen.endpoints`

```json5
listen: {
  endpoints: ["tcp/0.0.0.0:7447"]
}
```

#### `scouting`

```json5
scouting: {
  multicast: {
    enabled: true,
    address: "224.0.0.224:7446",
    // Re-enable auto-connect between routers
    autoconnect: { router: "router" }
  },
  gossip: {
    enabled: true,
    autoconnect: { router: "router" }
  }
}
```

---

## Connectivity Configuration

### DDS Side

The bridge discovers local ROS nodes via DDS UDP multicast on the configured domain. CycloneDDS configuration (via `CYCLONEDDS_URI`) controls which network interfaces DDS uses.

Tested with `RMW_IMPLEMENTATION=rmw_cyclonedds_cpp`. Other RMW implementations are interoperable over standard DDS but non-standard features (e.g., vendor-specific shared memory) may cause issues.

### Zenoh Side

By default (v0.11.0+), the bridge:

- Listens on `tcp/0.0.0.0:7447`
- Does not auto-connect to any remote endpoint

To connect a robot bridge to a remote bridge or router:

```bash
# CLI
zenoh-bridge-ros2dds -e tcp/192.168.1.100:7447

# Or in config
connect: {
  endpoints: ["tcp/192.168.1.100:7447"]
}
```

---

## Deployment Patterns

### Pattern 1: Single Machine

Bridge and ROS nodes on the same host. Use LOCALHOST-only DDS to prevent any external DDS traffic.

```
Host
├── ROS Node A
├── ROS Node B
└── zenoh-bridge-ros2dds
    └── listens on tcp/0.0.0.0:7447
```

```bash
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
sudo ip l set lo multicast on
zenoh-bridge-ros2dds
```

A remote Zenoh application or bridge can then connect to `tcp/<host-ip>:7447`.

---

### Pattern 2: Multi-Machine Local Network

A bridge on each machine. Machines are on the same LAN but DDS multicast across machines must be prevented.

```
Machine A (Robot)              Machine B (Operator)
├── ROS nodes                  ├── ROS nodes
└── zenoh-bridge ──────────── └── zenoh-bridge
    (router mode)       TCP        (router mode, connects to A)
    :7447
```

```bash
# On Machine A
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
zenoh-bridge-ros2dds

# On Machine B
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
zenoh-bridge-ros2dds -e tcp/<machine-a-ip>:7447

# Verify
ros2 topic list   # should show Machine A's topics
```

To enable automatic discovery between peers on the same LAN instead of static connection:

```json5
// Add to both bridge configs
scouting: {
  multicast: {
    autoconnect: { router: "router" }
  }
}
```

---

### Pattern 3: Cloud + Robot (Edge Gateway)

The bridge on the robot connects out to a Zenoh router in the cloud. The cloud router can serve multiple services and monitoring dashboards.

```
Robot (edge)                   Cloud
├── ROS nodes                  ├── zenohd (router)
└── zenoh-bridge               │   ├── REST plugin → HTTP dashboard
    -m client                  │   ├── Storage plugin → data history
    -e tcp/<cloud>:7447 ───────┘   └── Other bridges / services
```

```bash
# On the robot
zenoh-bridge-ros2dds \
  -m client \
  -e tcp/<cloud-ip>:7447 \
  --namespace /robot1
```

```json5
// Cloud zenohd config
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  },
  plugins: {
    rest: { http_port: 8000 },
    storage_manager: {
      volumes: { influxdb: { url: "http://localhost:8086" } },
      storages: {
        robot_data: {
          key_expr: "robot1/**",
          volume: { id: "influxdb", db: "robots", create_db: true }
        }
      }
    }
  }
}
```

---

### Pattern 4: Multi-Robot Fleet

Each robot runs a bridge with a unique namespace. A central aggregation host connects to all robots, allowing fleet-wide monitoring.

```
Robot 1                  Robot 2                  Fleet Monitor
├── ROS nodes            ├── ROS nodes            ├── zenoh-bridge (no ns)
└── zenoh-bridge ───┐    └── zenoh-bridge ───┐    │   or zenoh-bridge (/robot1)
    ns=/robot1      │        ns=/robot2      │    │
                    └────────────────────────┴────┘
                              (zenohd or direct peer connections)
```

Fleet monitor options:

1. **Bridge with matching namespace**: Run one bridge per robot on the monitor, each with the corresponding robot namespace.

   ```bash
   zenoh-bridge-ros2dds --namespace /robot1 -e tcp/<robot1-ip>:7447
   # Then use standard ROS tools without remapping
   rviz2
   ```

2. **Bridge without namespace**: Run one bridge connecting to all robots. Use ROS remapping to target a specific robot.

   ```bash
   zenoh-bridge-ros2dds -e tcp/<robot1-ip>:7447 -e tcp/<robot2-ip>:7447
   # Use remapping to work with robot1
   rviz2 --ros-args -r /tf:=/robot1/tf -r /tf_static:=/robot1/tf_static
   ```

---

## Multi-Robot Patterns

### Namespace Isolation Per Robot

Each robot's bridge gets a unique namespace. All topics, services, and actions are automatically prefixed.

```
Without namespace:   /cmd_vel, /odom, /scan, /tf
With /robot1:        /robot1/cmd_vel, /robot1/odom, /robot1/scan, /robot1/tf
With /robot2:        /robot2/cmd_vel, /robot2/odom, /robot2/scan, /robot2/tf
```

This means:
- No ROS node on the robot needs to be reconfigured with a namespace.
- DDS traffic between nodes on the same robot stays internal and namespace-free.
- The bridge applies the prefix only when routing to Zenoh.

### Fleet-Wide Topic Aggregation

A Zenoh key expression wildcard on the aggregation side can subscribe to matching topics across all robots:

```python
# Python — subscribe to /scan from all robots at once
session.declare_subscriber("*/scan", handle_scan)
# Receives: /robot1/scan, /robot2/scan, /robot3/scan ...
```

### Mixed Fleet

Robots of different types can share a single Zenoh network. Each has its own bridge with its own namespace. A monitoring bridge without a namespace sees all of them under their respective prefixes.

```
/robot_arm1/joint_states
/mobile_base2/cmd_vel
/drone3/pose
```

---

## Example Configurations

### Minimal Bridge Config

```json5
// minimal-bridge.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      domain: 0,
      ros_automatic_discovery_range: "LOCALHOST",
    }
  },
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  }
}
```

```bash
zenoh-bridge-ros2dds -c minimal-bridge.json5
```

---

### Selective Topic Bridging

Bridge only essential topics to conserve bandwidth. Deny noisy internal ROS topics.

```json5
// selective-bridge.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_automatic_discovery_range: "LOCALHOST",

      // Deny high-volume / internal topics
      deny: {
        publishers: [
          "/rosout",
          "/parameter_events",
          ".*/transition_event",
        ],
        subscribers: [
          "/rosout",
          "/parameter_events",
        ],
        service_servers: [
          ".*/describe_parameters",
          ".*/get_parameter_types",
          ".*/list_parameters",
          ".*/set_parameters",
          ".*/set_parameters_atomically",
        ],
        service_clients: [
          ".*/set_parameters",
        ],
        action_servers: [],
        action_clients: [],
      },
    }
  },
  mode: "router",
  connect: {
    endpoints: ["tcp/cloud-host:7447"]
  }
}
```

Alternatively, use `allow` to whitelist only what is needed:

```json5
{
  plugins: {
    ros2dds: {
      allow: {
        publishers: [".*/scan", ".*/odom", "/tf", "/tf_static", ".*/battery_state"],
        subscribers: [".*/cmd_vel", ".*/goal_pose"],
        service_servers: [],
        service_clients: [],
        action_servers: [".*/navigate_to_pose"],
        action_clients: [],
      }
    }
  }
}
```

---

### Rate-Limited Bridging

Cap publication rates for high-frequency sensor data and assign priorities.

```json5
// rate-limited-bridge.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_automatic_discovery_range: "LOCALHOST",

      pub_max_frequencies: [
        ".*/scan=5",          // LiDAR: max 5 Hz over Zenoh
        ".*/image_raw=2",     // Camera: max 2 Hz
        ".*/point_cloud=1",   // 3D cloud: max 1 Hz
        "/tf=20",             // TF: max 20 Hz
        ".*/imu=50",          // IMU: max 50 Hz
      ],

      pub_priorities: [
        ".*/cmd_vel=1:express",     // Control commands: highest priority, low latency
        ".*/e_stop=1:express",      // Emergency stop: highest priority
        ".*/pose=2",                // Pose: high priority
        ".*/odom=3",                // Odometry: elevated priority
        ".*/scan=5",                // LiDAR: normal priority
        ".*/image_raw=6",           // Images: low priority
        "/rosout=7",                // Logs: lowest priority
      ],

      reliable_routes_blocking: true,
    }
  },
  mode: "router",
  connect: {
    endpoints: ["tcp/cloud-host:7447"]
  }
}
```

---

### Multi-Robot Fleet Config

**Robot bridge config (deploy one per robot, varying `namespace` and `connect` endpoint):**

```json5
// robot-bridge.json5  (robot1)
{
  plugins: {
    ros2dds: {
      nodename: "zenoh_bridge_robot1",