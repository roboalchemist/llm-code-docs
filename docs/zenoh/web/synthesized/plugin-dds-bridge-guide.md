# Zenoh DDS Bridge & ROS2DDS Bridge: Comprehensive Guide

## Table of Contents

- [Overview](#overview)
- [1. DDS Bridge vs ROS2DDS Bridge: Decision Guide](#1-dds-bridge-vs-ros2dds-bridge-decision-guide)
  - [`zenoh-plugin-dds` — Generic DDS Bridge](#zenoh-plugin-dds-generic-dds-bridge)
  - [`zenoh-plugin-ros2dds` — ROS2-Specific Bridge](#zenoh-plugin-ros2dds-ros2-specific-bridge)
- [2. Installation](#2-installation)
  - [Debian / Ubuntu](#debian-ubuntu)
  - [Docker](#docker)
  - [Build from Source](#build-from-source)
  - [As a ROS2 Package](#as-a-ros2-package)
- [3. Basic Usage](#3-basic-usage)
  - [Typical Robot + Operator Setup](#typical-robot-operator-setup)
- [4. ROS2DDS Bridge: All Configuration Options](#4-ros2dds-bridge-all-configuration-options)
  - [`nodename`](#nodename)
  - [`namespace`](#namespace)
  - [`domain`](#domain)
  - [`ros_localhost_only`](#ros_localhost_only)
  - [`ros_automatic_discovery_range`](#ros_automatic_discovery_range)
  - [`ros_static_peers`](#ros_static_peers)
  - [`shm_enabled`](#shm_enabled)
  - [`allow` / `deny`](#allow-deny)
  - [`pub_max_frequencies`](#pub_max_frequencies)
  - [`pub_priorities`](#pub_priorities)
  - [`reliable_routes_blocking`](#reliable_routes_blocking)
  - [`queries_timeout`](#queries_timeout)
  - [`transient_local_cache_multiplier`](#transient_local_cache_multiplier)
  - [`work_thread_num` / `max_block_thread_num`](#work_thread_num-max_block_thread_num)
- [5. Generic DDS Bridge Configuration](#5-generic-dds-bridge-configuration)
  - [Key Differences from ROS2DDS](#key-differences-from-ros2dds)
  - [DDS Bridge Config Options](#dds-bridge-config-options)
  - [DDS Topic to Zenoh Key Mapping](#dds-topic-to-zenoh-key-mapping)
- [6. Forward vs Mirror Discovery Modes (Generic DDS Bridge)](#6-forward-vs-mirror-discovery-modes-generic-dds-bridge)
  - [Default Mode (`forward_discovery: false`) — Mirror Mode](#default-mode-forward_discovery-false-mirror-mode)
  - [Forward Discovery Mode (`forward_discovery: true`)](#forward-discovery-mode-forward_discovery-true)
- [7. Scoping for Multi-Robot Isolation](#7-scoping-for-multi-robot-isolation)
  - [The Problem](#the-problem)
  - [Solution: `namespace` (ROS2DDS) or `scope` (Generic DDS)](#solution-namespace-ros2dds-or-scope-generic-dds)
  - [Multi-Robot Topology](#multi-robot-topology)
  - [Hierarchical Scoping for Large Fleets](#hierarchical-scoping-for-large-fleets)
- [8. Rate Limiting and Downsampling](#8-rate-limiting-and-downsampling)
  - [`pub_max_frequencies` Syntax](#pub_max_frequencies-syntax)
  - [Common Rate Limiting Scenarios](#common-rate-limiting-scenarios)
  - [Interaction with Zenoh QoS](#interaction-with-zenoh-qos)
- [9. QoS Translation](#9-qos-translation)
  - [Reliability](#reliability)
  - [Durability](#durability)
  - [History (KEEP_LAST vs KEEP_ALL)](#history-keep_last-vs-keep_all)
  - [Ownership (EXCLUSIVE vs SHARED)](#ownership-exclusive-vs-shared)
  - [Deadline, Lifespan, Liveliness](#deadline-lifespan-liveliness)
  - [QoS Adaptation Details](#qos-adaptation-details)
- [10. Services and Actions Bridging (ROS2DDS)](#10-services-and-actions-bridging-ros2dds)
  - [ROS2 Service → Zenoh Mapping](#ros2-service-zenoh-mapping)
  - [ROS2 Action → Zenoh Mapping](#ros2-action-zenoh-mapping)
  - [Allowing/Denying Services and Actions](#allowingdenying-services-and-actions)
- [11. Admin Space](#11-admin-space)
  - [ROS2DDS Admin Space](#ros2dds-admin-space)
  - [Generic DDS Admin Space (v0.11.0+)](#generic-dds-admin-space-v0110)
- [12. Example Configurations](#12-example-configurations)
  - [Example 1: Basic Single-Robot ROS2DDS Bridge](#example-1-basic-single-robot-ros2dds-bridge)
  - [Example 2: Multi-Robot Fleet with Namespace Scoping](#example-2-multi-robot-fleet-with-namespace-scoping)
  - [Example 3: WAN Bridge with Rate Limiting](#example-3-wan-bridge-with-rate-limiting)
  - [Example 4: ROS2DDS Bridge with Service/Action Bridging and Timeouts](#example-4-ros2dds-bridge-with-serviceaction-bridging-and-timeouts)
  - [Example 5: Generic DDS Bridge for Non-ROS2 System](#example-5-generic-dds-bridge-for-non-ros2-system)
- [13. Zenoh Router Integration](#13-zenoh-router-integration)
- [14. Connectivity Configuration](#14-connectivity-configuration)
  - [Bridge as Router (Default since v0.11.0)](#bridge-as-router-default-since-v0110)
  - [Enable Auto-Discovery Between Bridges](#enable-auto-discovery-between-bridges)
  - [Connect Through a Central Zenoh Router](#connect-through-a-central-zenoh-router)
  - [Multi-Protocol Support](#multi-protocol-support)
- [15. Troubleshooting](#15-troubleshooting)
  - [DDS Traffic Duplication](#dds-traffic-duplication)
  - [Bridge Doesn't Start / SIGSEGV](#bridge-doesnt-start-sigsegv)
  - [Services / Actions Not Visible Across Bridge](#services-actions-not-visible-across-bridge)
  - [Late Joining Subscribers Miss Historical Data](#late-joining-subscribers-miss-historical-data)
  - [Action get_result Timeout Too Short](#action-get_result-timeout-too-short)
  - [High Memory Use with Many TRANSIENT_LOCAL Topics](#high-memory-use-with-many-transient_local-topics)
  - [Docker DDS Discovery Failure](#docker-dds-discovery-failure)

## Overview

Zenoh provides two bridge plugins for DDS (Data Distribution Service) connectivity:

| Plugin | Package | Standalone Binary | Use Case |
|--------|---------|-------------------|----------|
| `zenoh-plugin-dds` | Generic DDS bridge | `zenoh-bridge-dds` | Any DDS system, raw topics, non-ROS2 applications |
| `zenoh-plugin-ros2dds` | ROS2-specific bridge | `zenoh-bridge-ros2dds` | ROS2 systems — understands topics, services, actions, QoS profiles |

Both are available as a dynamic plugin library (loaded by `zenohd`) or a standalone executable. Configuration described for one applies to the other in the same way.

---

## 1. DDS Bridge vs ROS2DDS Bridge: Decision Guide

### `zenoh-plugin-dds` — Generic DDS Bridge

Use this when:
- You have a non-ROS2 DDS application (e.g., industrial, automotive, simulation)
- You need raw DDS topic passthrough — the bridge treats all traffic as opaque CDR bytes
- You want to bridge between different DDS domains across transports
- You're integrating a DDS system with zenoh-pico (embedded) or other Zenoh plugins (MQTT, storages)
- You want DDS Security support (`dds_security` feature)
- You want Iceoryx shared memory support (`dds_shm` feature)

**Limitations for ROS2:** Works partially with ROS2, but:
- Does not understand ROS2 services or actions (only pub/sub)
- Does not integrate with the ROS graph (`ros2 topic list` / `ros2 service list`)
- Does not support namespace configuration on the bridge
- Will eventually be deprecated for ROS2 usage

### `zenoh-plugin-ros2dds` — ROS2-Specific Bridge

Use this when:
- You have a ROS2 system using DDS (any DDS implementation, tested with `rmw_cyclonedds_cpp`)
- You need `ros2 topic list`, `ros2 service list`, `ros2 action list` to work across bridges
- You want ROS2 namespace configuration centralized at the bridge (not on each node)
- You need services and actions bridged — not just pub/sub
- You want more compact discovery (doesn't flood `ros_discovery_info` raw messages)

**Decision summary:**
- Building a robot fleet in ROS2? → **zenoh-plugin-ros2dds**
- Building a non-ROS DDS integration? → **zenoh-plugin-dds**
- Unsure? → **zenoh-plugin-ros2dds** if you have ROS2 nodes involved

---

## 2. Installation

### Debian / Ubuntu

```bash
# Add Eclipse Zenoh repository
curl -L https://download.eclipse.org/zenoh/debian-repo/zenoh-public-key \
  | sudo gpg --dearmor --yes --output /etc/apt/keyrings/zenoh-public-key.gpg
echo "deb [signed-by=/etc/apt/keyrings/zenoh-public-key.gpg] https://download.eclipse.org/zenoh/debian-repo/ /" \
  | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt update

# Install bridge (choose one)
sudo apt install zenoh-bridge-ros2dds   # for ROS2
sudo apt install zenoh-bridge-dds       # for generic DDS
```

### Docker

```bash
# ROS2DDS bridge
docker pull eclipse/zenoh-bridge-ros2dds:latest

# Generic DDS bridge (Linux only, requires --net host for UDP multicast)
docker pull eclipse/zenoh-bridge-dds:latest
docker run --init --net host eclipse/zenoh-bridge-dds
```

### Build from Source

```bash
# Prerequisites: Rust, llvm-dev, libclang-dev, cmake
sudo apt install llvm-dev libclang-dev cmake

git clone https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds.git
cd zenoh-plugin-ros2dds
cargo build --release

# Outputs:
#   target/release/zenoh-bridge-ros2dds  (standalone)
#   target/release/libzenoh_plugin_ros2dds.so  (plugin for zenohd)
```

### As a ROS2 Package

```bash
rosdep install --from-paths . --ignore-src -r -y
colcon build --packages-select zenoh_bridge_ros2dds \
  --cmake-args -DCMAKE_BUILD_TYPE=Release
```

---

## 3. Basic Usage

### Typical Robot + Operator Setup

Prevent DDS from leaking between hosts (pick one approach):

```bash
# Option A: Restrict DDS to localhost (ROS2 Iron+)
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
sudo ip l set lo multicast on   # Enable multicast on loopback (Linux)

# Option B: Legacy (before ROS2 Iron)
export ROS_LOCALHOST_ONLY=1

# Option C: Different domain IDs per host
export ROS_DOMAIN_ID=42   # robot
export ROS_DOMAIN_ID=0    # operator (different)
```

On the robot:
```bash
zenoh-bridge-ros2dds
```

On the operator host:
```bash
zenoh-bridge-ros2dds -e tcp/<robot-ip>:7447

# Verify ROS graph is visible
ros2 topic list
ros2 service list
ros2 action list
```

The bridge runs in `router` mode by default (since v0.11.0), listening on TCP port 7447.

---

## 4. ROS2DDS Bridge: All Configuration Options

Configuration is passed via a JSON5 file with `-c config.json5`. All settings live in the `plugins.ros2dds` object. All settings are optional.

**Full config skeleton:**
```json5
{
  plugins: {
    ros2dds: {
      // All options documented below
    }
  }
}
```

### `nodename`
- **Type:** string (valid Zenoh key expression)
- **Default:** `"zenoh_bridge_ros2dds"`
- **Description:** The ROS2 node name used by the bridge on the local DDS domain. Visible to other ROS2 nodes via `ros2 node list`.

```json5
ros2dds: {
  nodename: "my_bridge_node",
}
```

### `namespace`
- **Type:** string
- **Default:** `"/"`
- **Description:** A ROS2 namespace applied to the bridge itself and prepended to **all** routed topic/service/action names when mapped to Zenoh key expressions. This includes topics with absolute paths like `/rosout`, `/tf`, `/tf_static`.

This is the primary mechanism for multi-robot isolation. With `namespace: "/robot1"`, the topic `/cmd_vel` becomes `/robot1/cmd_vel` in Zenoh.

```json5
ros2dds: {
  namespace: "/robot1",
}
```

### `domain`
- **Type:** integer (0–232)
- **Default:** `0`, or the value of `$ROS_DOMAIN_ID` environment variable if set
- **Description:** The DDS domain ID to join for discovery and communication.

```json5
ros2dds: {
  domain: 42,
}
```

### `ros_localhost_only`
- **Type:** boolean
- **Default:** `false`, or `true` if `ROS_LOCALHOST_ONLY=1` env var is set
- **Description:** When `true`, all DDS discovery and data traffic is restricted to the localhost interface (`127.0.0.1`). Use this to prevent DDS from propagating across the network when the bridge is responsible for all cross-host communication.
- **When to use:** On every host where the bridge runs, to ensure DDS traffic stays local and only Zenoh crosses the network.

```json5
ros2dds: {
  ros_localhost_only: true,
}
```

### `ros_automatic_discovery_range`
- **Type:** string enum
- **Default:** not set (uses DDS defaults), or taken from `ROS_AUTOMATIC_DISCOVERY_RANGE` env var
- **Available since:** ROS2 Iron
- **Valid values:**
  - `"SUBNET"` — Discover nodes via multicast, reachable across the subnet (DDS default)
  - `"LOCALHOST"` — Only discover nodes on the same machine
  - `"OFF"` — No discovery at all, not even on the same machine
  - `"SYSTEM_DEFAULT"` — Don't override any discovery settings

```json5
ros2dds: {
  ros_automatic_discovery_range: "LOCALHOST",
}
```

### `ros_static_peers`
- **Type:** string (semicolon-separated IP addresses)
- **Default:** not set
- **Description:** A list of IP addresses that the bridge will statically attempt to discover ROS2 nodes on. Useful when multicast is unavailable or disabled. Requires ROS2 Iron or later.

```json5
ros2dds: {
  ros_static_peers: "192.168.1.10;192.168.1.11",
}
```

### `shm_enabled`
- **Type:** boolean
- **Default:** `false`
- **Description:** Enable Iceoryx shared memory (PSMX plugin) for DDS communication. Requires the bridge to be built with the `dds_shm` feature flag. When enabled, the Iceoryx `iox-roudi` daemon must be running.
- **Note:** Cannot be combined with `prefix_symbols` build feature.

```json5
ros2dds: {
  shm_enabled: false,
}
```

### `allow` / `deny`
- **Type:** object with per-interface-type regex lists
- **Default:** if neither is set, all interfaces are allowed
- **Constraint:** You cannot set both `allow` and `deny` in the same config

**`allow`** — only bridge the listed interfaces. Interface types not listed (or set to empty list) mean **no** interfaces of that type are bridged.

**`deny`** — bridge everything **except** the listed interfaces. Interface types not listed (or set to empty list) mean **all** interfaces of that type are bridged.

Each value is a list of regular expressions matched against the full ROS2 interface name (e.g., `/robot1/cmd_vel`). Regexes are anchored: `^<pattern>$`.

**Interface type keys:**
- `publishers` — DDS Writers (data sources)
- `subscribers` — DDS Readers (data sinks)
- `service_servers` — ROS2 service servers
- `service_clients` — ROS2 service clients
- `action_servers` — ROS2 action servers
- `action_clients` — ROS2 action clients

```json5
// Allow only specific interfaces
ros2dds: {
  allow: {
    publishers: [".*/laser_scan", "/tf", ".*/pose"],
    subscribers: [".*/cmd_vel"],
    service_servers: [".*/.*_parameters"],
    service_clients: [],        // no service clients allowed
    action_servers: [".*/navigate_to_pose"],
    action_clients: [],         // no action clients allowed
  },
}

// Deny noisy internal topics
ros2dds: {
  deny: {
    publishers: ["/rosout", "/parameter_events"],
    subscribers: ["/rosout"],
    service_servers: [".*/set_parameters"],
    service_clients: [".*/set_parameters"],
    action_servers: [],
    action_clients: [],
  },
}
```

### `pub_max_frequencies`
- **Type:** list of `"<regex>=<float>"` strings
- **Default:** empty (no rate limiting)
- **Description:** Per-topic rate limiting for publications routed over Zenoh. When a publisher produces data faster than the specified frequency, the bridge downsamples by dropping intermediate messages.
- **Format:** `"<regex>=<frequency_hz>"` where regex matches the ROS2 publisher name

```json5
ros2dds: {
  pub_max_frequencies: [
    ".*/scan=5",         // LIDAR scans: max 5 Hz over Zenoh
    ".*/camera/image=10", // camera: max 10 Hz
    "/tf=50",            // TF: max 50 Hz
  ],
}
```

**Notes:**
- Regex is matched against the full ROS2 interface name
- Downsampling is per-DDS instance (per publisher entity, not per topic globally)
- Only affects publications routing FROM DDS TO Zenoh; does not throttle inbound Zenoh → DDS

### `pub_priorities`
- **Type:** list of `"<regex>=<integer>[:<express>]"` strings
- **Default:** empty (all topics use Zenoh default priority 5)
- **Description:** Per-topic Zenoh publication priority. In high-traffic scenarios, higher-priority publications are processed before lower-priority ones in Zenoh queues.
- **Priority range:** 1 (highest) to 7 (lowest), default is 5
- **`:express` suffix:** When present, Zenoh sends the message immediately without batching. Improves latency for the topic at the cost of throughput.

```json5
ros2dds: {
  pub_priorities: [
    "/scan=1:express",    // LIDAR: highest priority, immediate send
    "/pose=2",            // Pose: high priority, batched
    "/map=6",             // Map: low priority
    "/rosout=7",          // Logs: lowest priority
  ],
}
```

### `reliable_routes_blocking`
- **Type:** boolean
- **Default:** `true`
- **Description:** Controls congestion behavior for RELIABLE DDS Writer routes.
  - `true` — Uses `CongestionControl::Block`. If Zenoh is congested, the route blocks, which back-pressures the DDS Reader and eventually the RELIABLE DDS Writer. Guarantees no data loss for reliable topics, but may cause latency spikes.
  - `false` — Uses `CongestionControl::Drop`. If Zenoh is congested, data is dropped rather than blocking. BEST_EFFORT DDS Writers always use `Drop` regardless of this setting.

```json5
ros2dds: {
  reliable_routes_blocking: true,
}
```

**When to set `false`:** WAN bridges where blocking would cascade failures or when you prefer dropped messages over head-of-line blocking.

### `queries_timeout`
- **Type:** object (all fields optional)
- **Description:** Fine-grained timeouts for different categories of Zenoh queries. When a timeout expires on a TRANSIENT_LOCAL query, historical data may be missed but the route is not blocked.

**Sub-fields:**

| Field | Default | Description |
|-------|---------|-------------|
| `default` | `5.0` (seconds) | Fallback for any query not matched by more specific rules |
| `transient_local_subscribers` | uses `default` | Timeout for querying historical publications when a TRANSIENT_LOCAL subscriber joins late |
| `services` | uses `default` | Timeout for ROS2 service call requests |
| `actions.send_goal` | uses `default` | Timeout for action send_goal phase |
| `actions.cancel_goal` | uses `default` | Timeout for action cancel_goal phase |
| `actions.get_result` | `300.0` (seconds) | Timeout for action get_result phase (large default because actions may run long) |

Each field accepts either a single float (applies to all matching queries) or a list of `"<regex>=<float>"` strings matched against the interface name, evaluated in order.

```json5
ros2dds: {
  queries_timeout: {
    default: 5.0,
    transient_local_subscribers: 1.0,
    services: ["add_two_ints=0.5", ".*=2.0"],
    actions: {
      send_goal: 1.0,
      cancel_goal: 1.0,
      get_result: [".*long_mission=3600", ".*=300"],
    },
  },
}
```

### `transient_local_cache_multiplier`
- **Type:** integer
- **Default:** `10`
- **Description:** Controls the size of the `PublicationCache` created for TRANSIENT_LOCAL publisher routes. The cache allows late-joining bridges to receive historical data.

The actual cache size is: `publisher.history_length × transient_local_cache_multiplier`

Since one route may serve multiple publishers (per-topic), the multiplier ensures the cache is large enough to hold samples from multiple concurrent TRANSIENT_LOCAL publishers on the same topic.

```json5
ros2dds: {
  transient_local_cache_multiplier: 10,
}
```

**When to increase:** If you have more than 10 TRANSIENT_LOCAL publishers on the same topic, increase proportionally.

### `work_thread_num` / `max_block_thread_num`
- **Type:** integer
- **Defaults:** `work_thread_num: 2`, `max_block_thread_num: 50`
- **Description:** Tokio async runtime thread pool sizes. Only affects the plugin (loaded into `zenohd`); standalone bridge uses the Zenoh session's runtime (configurable via `ZENOH_RUNTIME` env var).

```json5
ros2dds: {
  work_thread_num: 4,         // more non-blocking worker threads
  max_block_thread_num: 100,  // more blocking I/O threads
}
```

---

## 5. Generic DDS Bridge Configuration

The `zenoh-plugin-dds` config lives under `plugins.dds`. It has a simpler interface since it doesn't understand ROS2 semantics.

### Key Differences from ROS2DDS

| Option | zenoh-plugin-dds | zenoh-plugin-ros2dds |
|--------|-----------------|---------------------|
| Namespace | `scope` (string prefix) | `namespace` (ROS2 namespace) |
| Allow/deny | `allow`/`deny` (single regex on `partition/topic`) | Per-interface-type regex objects |
| Rate limiting | `max_frequencies` | `pub_max_frequencies` |
| Discovery modes | `forward_discovery: false/true` | Built-in (always uses forward-style) |
| Services/actions | Not supported | Full support |
| ROS graph | Not visible | Visible via liveliness |

### DDS Bridge Config Options

```json5
{
  plugins: {
    dds: {
      // scope: A prefix added to all routed DDS topics when mapped to Zenoh keys.
      // Type: string
      // Default: not set (no prefix)
      // scope: "robot-1",

      // domain: DDS Domain ID
      // Type: integer
      // Default: 0, or $ROS_DOMAIN_ID if set
      // domain: 0,

      // localhost_only: Restrict DDS to loopback interface
      // Type: boolean
      // Default: false, or true if ROS_LOCALHOST_ONLY=1
      // localhost_only: true,

      // shm_enabled: Use Iceoryx shared memory (requires dds_shm build feature)
      // Type: boolean
      // Default: false
      // shm_enabled: false,

      // allow: Regex matching "partition/topic-name" to allow
      // Type: string or list of strings (concatenated with |)
      // Default: all allowed
      // allow: [".*/cmd_vel", ".*rosout"],

      // deny: Regex matching "partition/topic-name" to deny
      // Type: string or list of strings (concatenated with |)
      // Default: none denied
      // deny: ["diagnostic.*"],

      // max_frequencies: Rate limiting per topic
      // Type: list of "<regex>=<float>" strings
      // Default: empty
      // max_frequencies: ["diagnostic.*=10", "rosout=5"],

      // forward_discovery: Enable forward discovery mode
      // Type: boolean
      // Default: false
      // forward_discovery: false,

      // reliable_routes_blocking: Block on congestion for RELIABLE writers
      // Type: boolean
      // Default: true
      // reliable_routes_blocking: true,

      // queries_timeout: Timeout (seconds) for remote bridge queries
      // Type: float
      // Default: 5.0
      // queries_timeout: 5.0,

      // generalise_subs: Key expressions for generalising subscriptions (reduces discovery traffic)
      // generalise_subs: ["SUB1", "SUB2"],

      // generalise_pubs: Key expressions for generalising publications
      // generalise_pubs: ["PUB1", "PUB2"],

      // work_thread_num: Tokio worker threads (plugin only)
      // work_thread_num: 2,

      // max_block_thread_num: Tokio blocking threads (plugin only)
      // max_block_thread_num: 50,
    },
  },
}
```

### DDS Topic to Zenoh Key Mapping

The generic bridge maps DDS topics to Zenoh key expressions directly:

| DDS Topic | DDS Partition | Zenoh Key (no scope) | Zenoh Key (scope=`"S"`) |
|-----------|--------------|----------------------|-------------------------|
| `TopicA` | none | `TopicA` | `S/TopicA` |
| `TopicA` | `PartitionX` | `PartitionX/TopicA` | `S/PartitionX/TopicA` |

For ROS2 nodes using the generic DDS bridge, the DDS topic names follow the ROS2 → DDS mapping:

| ROS2 Name | DDS Topic | Zenoh Key (scope=`"myscope"`) |
|-----------|-----------|------------------------------|
| topic `/rosout` | `rt/rosout` | `myscope/rt/rosout` |
| topic `/cmd_vel` | `rt/cmd_vel` | `myscope/rt/cmd_vel` |
| service `/set_pen` (request) | `rq/set_penRequest` | `myscope/rq/set_penRequest` |
| service `/set_pen` (reply) | `rr/set_penReply` | `myscope/rr/set_penReply` |

---

## 6. Forward vs Mirror Discovery Modes (Generic DDS Bridge)

The generic `zenoh-plugin-dds` has two discovery modes, controlled by `forward_discovery`.

### Default Mode (`forward_discovery: false`) — Mirror Mode

In this mode, each bridge independently discovers DDS entities on its local DDS domain and creates local routes:

1. Bridge A discovers a local DDS Writer for topic `T`
2. Bridge A creates a local DDS Reader (mirror) and a Zenoh publisher for `T`
3. Data from the Writer flows: DDS Writer → Bridge A's mirror Reader → Zenoh → Bridge B → Bridge B's mirror Writer → remote DDS Reader

**Characteristics:**
- No discovery information crosses the Zenoh network — only data does
- Each bridge creates routes for ALL discovered local entities, regardless of whether the remote side has interest
- More resource usage (extra DDS entities, routes created eagerly)
- Simpler — works without any Zenoh-level coordination
- ROS2 graph is partially visible but not complete (no `ros_discovery_info` forwarding)

### Forward Discovery Mode (`forward_discovery: true`)

In this mode, discovery information is forwarded across Zenoh, and remote bridges create matching replica entities:

1. Bridge A discovers a local DDS Writer for topic `T`
2. Bridge A forwards this discovery info (compactly) over Zenoh
3. Bridge B receives the discovery info and creates a replica DDS Writer on its local domain
4. Remote ROS2 nodes discover the replica Writer, matching happens locally
5. For ROS2 systems: `ros_discovery_info` is forwarded with GID remapping so remote nodes see a consistent ROS graph

**Characteristics:**
- Routes are created only where there is actual matching between writers and readers
- Full ROS graph visibility across bridges (`ros2 topic list` works correctly)
- More efficient — routes created on demand rather than eagerly
- `zenoh-plugin-ros2dds` always uses forward-style discovery (it's built-in and not configurable)

```json5
// Generic DDS bridge in forward discovery mode
{
  plugins: {
    dds: {
      forward_discovery: true,
    },
  },
}
```

**Performance implications:**

| Aspect | Mirror Mode | Forward Discovery |
|--------|-------------|-------------------|
| Route creation | Eager (all local entities) | Demand-driven |
| Network overhead | More DDS entities created | Compact discovery traffic |
| ROS graph visibility | Partial | Full |
| Resource usage | Higher | Lower |
| Shared memory DDS | Supported | Limited (non-memcpy-safe types not forwarded) |

---

## 7. Scoping for Multi-Robot Isolation

### The Problem

Without scoping, two robots publishing to `/cmd_vel` would have their messages interleave in Zenoh — there is no per-robot isolation.

### Solution: `namespace` (ROS2DDS) or `scope` (Generic DDS)

Both options add a unique prefix to all Zenoh key expressions for the bridge:

**ROS2DDS bridge (recommended):**
```json5
ros2dds: {
  namespace: "/robot1",
}
```

**Generic DDS bridge:**
```json5
dds: {
  scope: "robot1",
}
```

### Multi-Robot Topology

**Robot side (each robot runs its own bridge):**

```json5
// robot1/config.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_localhost_only: true,  // keep DDS local to robot
    },
  },
}
```

```json5
// robot2/config.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot2",
      ros_localhost_only: true,
    },
  },
}
```

**Operator side — option 1: target a single robot**

```json5
// operator_watching_robot1.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",       // mirror robot1's namespace
    },
  },
  connect: {
    endpoints: ["tcp/192.168.1.10:7447"],  // robot1's bridge
  },
}
```

With this setup, `rviz2` (no namespace args needed) sees `/robot1/cmd_vel` as `/cmd_vel`.

**Operator side — option 2: monitor all robots without a bridge namespace**

```json5
// operator_all_robots.json5
{
  plugins: {
    ros2dds: {
      // no namespace — all robot topics visible with their prefix
    },
  },
  connect: {
    endpoints: [
      "tcp/192.168.1.10:7447",   // robot1
      "tcp/192.168.1.11:7447",   // robot2
    ],
  },
}
```

With this setup, use remapping to target a specific robot:
```bash
rviz2 --ros-args -r /tf:=/robot1/tf -r /tf_static:=/robot1/tf_static
ros2 topic echo /robot2/scan
```

### Hierarchical Scoping for Large Fleets

For a fleet with sub-groups (e.g., floors in a building):

```json5
// robot on floor2, unit 3
ros2dds: {
  namespace: "/floor2/robot3",
}
```

Zenoh key expressions become `/floor2/robot3/cmd_vel`, `/floor2/robot3/scan`, etc.

A monitoring station can subscribe to all floor2 robots:
```
zenoh get "/floor2/*/scan"     // all floor2 robot scans
zenoh get "/*/*/cmd_vel"       // all fleet command velocities
```

---

## 8. Rate Limiting and Downsampling

### `pub_max_frequencies` Syntax

```json5
ros2dds: {
  pub_max_frequencies: [
    "<regex>=<frequency_hz>",
    "<regex>=<frequency_hz>",
  ],
}
```

- `<regex>`: matched against the full ROS2 publisher name (e.g., `/robot1/scan`)
- `<frequency_hz>`: float, maximum Hz to route over Zenoh; higher publication rates are downsampled
- Rules are evaluated in order; the first matching rule wins
- Downsampling is per-DDS instance (individual publisher entity), not across all publishers on a topic

### Common Rate Limiting Scenarios

**WAN bridge (reduce bandwidth):**
```json5
ros2dds: {
  pub_max_frequencies: [
    ".*/scan=5",               // LIDAR: 10Hz sensor → 5Hz over WAN
    ".*/camera/image_raw=2",   // camera: 30Hz → 2Hz over WAN
    ".*/point_cloud=1",        // pointcloud: 20Hz → 1Hz
    "/tf=20",                  // TF: 100Hz → 20Hz
  ],
}
```

**Local bridge (prevent saturation):**
```json5
ros2dds: {
  pub_max_frequencies: [
    ".*/diagnostics=10",       // cap diagnostic floods
    "/rosout=20",              // cap log output
  ],
}
```

### Interaction with Zenoh QoS

Rate limiting and congestion control are orthogonal:

- `pub_max_frequencies` — proactive downsampling: drops intermediate messages at the source before sending
- `reliable_routes_blocking: false` — reactive dropping: drops when the Zenoh queue is full
- Together: rate limiting reduces how often messages enter the queue; `Drop` policy handles bursts

For a WAN LIDAR bridge running at 10Hz but with `pub_max_frequencies: [".*/scan=5"]`, you'll see at most 5Hz of LIDAR data regardless of network conditions.

---

## 9. QoS Translation

The bridge translates DDS QoS policies to Zenoh equivalents when routing data.

### Reliability

| DDS QoS | Zenoh Equivalent | Behavior |
|---------|-----------------|----------|
| `RELIABLE` | `Reliability::Reliable` | Bridge routes with `CongestionControl::Block` (if `reliable_routes_blocking: true`) |
| `BEST_EFFORT` | `Reliability::BestEffort` | Bridge routes with `CongestionControl::Drop` |

The bridge creates a mirror DDS entity with the same reliability QoS as the original, preserving the reliability contract end-to-end.

### Durability

| DDS QoS | Zenoh Equivalent | Behavior |
|---------|-----------------|----------|
| `VOLATILE` | No cache | Data is only delivered to currently-subscribed sessions |
| `TRANSIENT_LOCAL` | `PublicationCache` | Historical samples cached for late joiners; cache size = `history_length × transient_local_cache_multiplier` |
| `TRANSIENT` / `PERSISTENT` | Not directly supported | Treated as `TRANSIENT_LOCAL` |

For **TRANSIENT_LOCAL** publishers:
1. The bridge creates a `PublicationCache` to store historical publications
2. When a late-joining bridge receives a TRANSIENT_LOCAL subscriber, it queries the cache
3. Historical data is replayed up to `queries_timeout.transient_local_subscribers` seconds
4. The bridge mirror Writer has `durability_service` QoS configured with matching history so CycloneDDS serves historical samples correctly

```json5
ros2dds: {
  // Allow 2 seconds to receive historical data for TRANSIENT_LOCAL subscribers
  queries_timeout: {
    transient_local_subscribers: 2.0,
  },
  // If you have many TRANSIENT_LOCAL publishers on same topic, increase multiplier
  transient_local_cache_multiplier: 20,
}
```

### History (KEEP_LAST vs KEEP_ALL)

The bridge preserves History QoS in the mirror entities. The `transient_local_cache_multiplier` scales the `PublicationCache` relative to the KEEP_LAST depth.

### Ownership (EXCLUSIVE vs SHARED)

Ownership QoS is preserved in the mirror entities. The bridge does not interfere with DDS ownership arbitration.

### Deadline, Lifespan, Liveliness

These QoS policies are preserved in the mirror entities. The DDS middleware enforces them locally. The bridge does not perform cross-network deadline checking; violations are detected per-domain, not across the Zenoh link.

### QoS Adaptation Details

When a DDS Writer is discovered, the bridge creates a mirror DDS Reader with adapted QoS:
- Writer-only QoS fields removed: `durability_service`, `ownership_strength`, `transport_priority`, `lifespan`, `writer_data_lifecycle`, `writer_batching`
- `ignore_local` set to `PARTICIPANT` to prevent the bridge from echoing data back to itself

When a DDS Reader is discovered, the bridge creates a mirror DDS Writer with adapted QoS:
- Reader-only QoS fields removed: `time_based_filter`, `reader_data_lifecycle`
- `ignore_local` set to `PARTICIPANT`
- For TRANSIENT_LOCAL readers: `durability_service` configured with matching history settings

---

## 10. Services and Actions Bridging (ROS2DDS)

The ROS2DDS bridge has first-class support for ROS2 services and actions, mapping them to Zenoh queryable/query patterns.

### ROS2 Service → Zenoh Mapping

A ROS2 service has a server (handles requests) and clients (send requests):

| ROS2 Component | DDS Topics | Zenoh Mapping |
|----------------|-----------|---------------|
| Service Server | `rq/<name>Request`, `rr/<name>Reply` | Zenoh Queryable |
| Service Client | `rq/<name>Request`, `rr/<name>Reply` | Zenoh Querier (issues `get()`) |

When the bridge routes a service:
1. A remote service client issues a Zenoh `get()` on the service key expression
2. The bridge on the server side receives the query, forwards it as a DDS request
3. The service server processes it and returns a DDS reply
4. The bridge sends the Zenoh reply back
5. The remote client receives the response

**Timeout handling:** The `queries_timeout.services` setting controls how long the client-side bridge waits for a reply. Default is 5 seconds. If the service server doesn't respond in time, the client receives a timeout error (the route itself is not affected).

```json5
ros2dds: {
  queries_timeout: {
    services: [
      "add_two_ints=0.5",   // fast service, short timeout
      "compute_path=30.0",  // slow path planning, longer timeout
      ".*=5.0",             // default for everything else
    ],
  },
}
```

### ROS2 Action → Zenoh Mapping

A ROS2 action involves 5 DDS topics:

| Phase | DDS Topics | Zenoh Key Pattern |
|-------|-----------|-------------------|
| Send Goal | `rq/<name>/_action/send_goalRequest`, `rr/<name>/_action/send_goalReply` | `<ke>/_action/send_goal` |
| Cancel Goal | `rq/<name>/_action/cancel_goalRequest`, `rr/<name>/_action/cancel_goalReply` | `<ke>/_action/cancel_goal` |
| Get Result | `rq/<name>/_action/get_resultRequest`, `rr/<name>/_action/get_resultReply` | `<ke>/_action/get_result` |
| Status | `rt/<name>/_action/status` | `<ke>/_action/status` |
| Feedback | `rt/<name>/_action/feedback` | `<ke>/_action/feedback` |

All 5 topics are bridged automatically when an action server or client is discovered.

**Timeout handling for actions:**

The `get_result` phase has a default timeout of **300 seconds** (5 minutes) because actions can be long-running. Other phases default to 5 seconds.

```json5
ros2dds: {
  queries_timeout: {
    actions: {
      send_goal: 2.0,
      cancel_goal: 5.0,
      get_result: [
        ".*navigate_to_pose=600",  // navigation may take 10 minutes
        ".*dock=30",               // docking is fast
        ".*=300",                  // 5 minutes for everything else
      ],
    },
  },
}
```

**Error propagation:** If a timeout occurs during `send_goal` or `get_result`, the action client receives a service timeout error. The bridge removes the in-flight query but does not kill the action server — it continues running. The client is responsible for cancelling if needed.

### Allowing/Denying Services and Actions

```json5
ros2dds: {
  allow: {
    publishers: [".*/scan", "/tf"],
    subscribers: [".*/cmd_vel"],
    service_servers: [".*/navigate.*"],     // only navigation services
    service_clients: [".*/get_map"],        // only map retrieval clients
    action_servers: [".*/navigate_to_pose"],
    action_clients: [],                     // no action clients bridged
  },
}
```

---

## 11. Admin Space

Both bridges expose internal state via Zenoh admin space, queryable via any Zenoh client or the REST API.

### ROS2DDS Admin Space

Path prefix: `@/<bridge-id>/ros2/`

```
@/<id>/ros2/node/**          - all discovered ROS2 nodes and their interfaces
@/<id>/ros2/dds/**           - all discovered DDS readers/writers
@/<id>/ros2/route/**         - all established routes (pub, sub, service, action)
@/*/ros2/node/**             - all nodes across all bridges
@/*/ros2/route/**/cmd_vel    - all routes for cmd_vel across all bridges
```

Enable REST API:
```json5
{
  plugins: {
    ros2dds: { ... },
    rest: { http_port: 8000 },
  },
}
```

Then query:
```bash
curl http://localhost:8000/@/local/ros2/node/**
curl http://localhost:8000/@/local/ros2/route/**
curl http://localhost:8000/@/*/ros2/route/**/scan
```

### Generic DDS Admin Space (v0.11.0+)

Path prefix: `@/<uuid>/dds/`

```bash
curl http://localhost:8000/@/*/dds/participant/**    # all DDS entities
curl http://localhost:8000/@/*/dds/route/**          # all routes
curl http://localhost:8000/@/*/dds/**/cmd_vel        # entities + routes for cmd_vel
```

---

## 12. Example Configurations

### Example 1: Basic Single-Robot ROS2DDS Bridge

```json5
// robot_bridge.json5
{
  plugins: {
    ros2dds: {
      nodename: "zenoh_bridge_ros2dds",
      domain: 0,
      ros_localhost_only: true,
    },
  },
  // Listen for incoming connections from operators
  // Default: tcp/0.0.0.0:7447 in router mode
}
```

```bash
# On robot
ROS_LOCALHOST_ONLY=1 zenoh-bridge-ros2dds -c robot_bridge.json5

# On operator
zenoh-bridge-ros2dds -e tcp/192.168.1.100:7447
```

### Example 2: Multi-Robot Fleet with Namespace Scoping

```json5
// fleet_robot1.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_localhost_only: true,
      reliable_routes_blocking: true,
    },
  },
}
```

```json5
// fleet_robot2.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot2",
      ros_localhost_only: true,
      reliable_routes_blocking: true,
    },
  },
}
```

```json5
// fleet_operator.json5 — monitors all robots
{
  plugins: {
    ros2dds: {
      // no namespace — sees /robot1/... and /robot2/... topics
      domain: 0,
    },
    rest: { http_port: 8000 },
  },
  connect: {
    endpoints: [
      "tcp/192.168.1.10:7447",   // robot1
      "tcp/192.168.1.11:7447",   // robot2
    ],
  },
}
```

### Example 3: WAN Bridge with Rate Limiting

Connecting a robot on a local network to a cloud monitoring station over WAN:

```json5
// wan_robot_side.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_localhost_only: true,
      // Rate limit high-bandwidth topics before sending over WAN
      pub_max_frequencies: [
        ".*/scan=5",               // LIDAR: 10Hz → 5Hz
        ".*/camera/image_raw=3",   // Camera: 30Hz → 3Hz
        ".*/point_cloud=1",        // Pointcloud: 20Hz → 1Hz
        "/tf=20",                  // TF: 100Hz → 20Hz
      ],
      // On WAN, don't block on congestion — prefer dropping
      reliable_routes_blocking: false,
      // Prioritize control traffic
      pub_priorities: [
        ".*/cmd_vel=1",            // control: highest priority
        ".*/scan=3",               // sensor: high
        ".*/camera.*=5",           // camera: normal
        ".*/point_cloud=6",        // pointcloud: low
      ],
    },
  },
  // Connect to cloud Zenoh router
  connect: {
    endpoints: ["tcp/cloud.example.com:7447"],
  },
}
```

```json5
// wan_cloud_side.json5
{
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      // Cloud-side subscribes to throttled data
    },
  },
  // Cloud router listens on fixed port
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },
}
```

### Example 4: ROS2DDS Bridge with Service/Action Bridging and Timeouts

```json5
// navigation_bridge.json5
{
  plugins: {
    ros2dds: {
      namespace: "/nav_robot",
      ros_localhost_only: true,

      // Only bridge navigation-relevant interfaces
      allow: {
        publishers: ["/tf", "/tf_static", ".*/scan", ".*/odom", ".*/map"],
        subscribers: [".*/cmd_vel", ".*/initialpose"],
        service_servers: [".*/get_map", ".*/clear_costmaps"],
        service_clients: [],
        action_servers: [".*/navigate_to_pose", ".*/follow_path"],
        action_clients: [],
      },

      // Fine-grained timeouts for navigation
      queries_timeout: {
        default: 5.0,
        transient_local_subscribers: 2.0,
        services: [
          "get_map=10.0",        // map service may be slow
          "clear_costmaps=3.0",
          ".*=5.0",
        ],
        actions: {
          send_goal: 3.0,
          cancel_goal: 5.0,
          get_result: [
            ".*navigate_to_pose=1800",   // 30 min max for navigation
            ".*follow_path=3600",         // 1 hour for follow path
            ".*=300",
          ],
        },
      },

      // TRANSIENT_LOCAL for map topic (late joiners need map)
      transient_local_cache_multiplier: 10,

      reliable_routes_blocking: true,
    },
  },
}
```

### Example 5: Generic DDS Bridge for Non-ROS2 System

```json5
// industrial_dds_bridge.json5
{
  plugins: {
    dds: {
      // Scope prevents collision with other DDS systems in Zenoh
      scope: "plant-floor-A",

      // DDS domain for the industrial system
      domain: 5,

      // Only bridge specific production topics
      allow: ["ProductionLine-1/.*", "ProductionLine-2/.*", ".*/Alarms"],

      // Deny high-frequency diagnostic noise
      deny: [".*Diagnostics", ".*Heartbeat"],

      // Rate limit high-frequency sensor data
      max_frequencies: [
        ".*Sensor.*=50",       // cap sensors at 50Hz
        ".*Camera.*=10",       // cameras at 10Hz
      ],

      // Use forward discovery for efficiency
      forward_discovery: true,

      // Timeout for TRANSIENT_LOCAL historical queries
      queries_timeout: 10.0,
    },
  },

  // Connect to a central Zenoh router
  connect: {
    endpoints: ["tcp/10.0.1.1:7447"],
  },
}
```

---

## 13. Zenoh Router Integration

Both bridges can run as plugins inside a `zenohd` router instead of standalone executables.

**Plugin mode config for zenohd:**
```json5
// zenohd_with_ros2dds_plugin.json5
{
  plugins_loading: {
    enabled: true,
    search_dirs: ["/usr/lib"],
  },
  plugins: {
    ros2dds: {
      namespace: "/robot1",
      ros_localhost_only: true,
    },
    rest: {
      http_port: 8000,
    },
  },
}
```

```bash
zenohd -c zenohd_with_ros2dds_plugin.json5
```

**Plugin ABI constraint:** The plugin must be built with the exact same Rust version as `zenohd` and the same `zenoh` crate version. Mismatch causes `SIGSEGV` crashes. Use the prebuilt packages from the same release to guarantee compatibility.

**Symbol prefix for co-loading both plugins:**

If you load both `zenoh-plugin-dds` and `zenoh-plugin-ros2dds` simultaneously in the same `zenohd`, they both use `cyclors` (CycloneDDS bindings) and may have symbol clashes. Build both with `--features prefix_symbols`:

```bash
cargo build --release --features prefix_symbols
```

Note: `prefix_symbols` is incompatible with `dds_shm`.

---

## 14. Connectivity Configuration

### Bridge as Router (Default since v0.11.0)

The bridge starts in `router` mode and listens on `tcp/0.0.0.0:7447`. It does **not** auto-connect to anything. You must explicitly configure one side to connect to the other:

```bash
# Robot bridge listens passively
zenoh-bridge-ros2dds

# Operator bridge connects to robot
zenoh-bridge-ros2dds -e tcp/192.168.1.100:7447
```

### Enable Auto-Discovery Between Bridges

```json5
{
  scouting: {
    multicast: {
      autoconnect: { router: "router" },
    },
    gossip: {
      autoconnect: { router: "router" },
    },
  },
  plugins: {
    ros2dds: { ... },
  },
}
```

### Connect Through a Central Zenoh Router

```json5
// bridge_via_router.json5
{
  mode: "client",   // connect to router instead of peer mode
  connect: {
    endpoints: ["tcp/zenoh-router.internal:7447"],
  },
  plugins: {
    ros2dds: {
      namespace: "/robot3",
      ros_localhost_only: true,
    },
  },
}
```

### Multi-Protocol Support

Zenoh supports multiple transports. The bridge supports any transport Zenoh supports:

```json5
connect: {
  endpoints: [
    "tcp/192.168.1.100:7447",     // TCP
    "udp/224.0.0.224:7446",       // UDP multicast
    "tls/192.168.1.100:7448",     // TLS
    "quic/192.168.1.100:7447",    // QUIC
  ],
}
```

---

## 15. Troubleshooting

### DDS Traffic Duplication

**Symptom:** Messages arrive twice, or ROS nodes see their own messages echo'd back.

**Cause:** DDS multicast is not restricted, so the bridge and regular ROS nodes can both see the same traffic.

**Fix:** Restrict DDS to localhost using one of:
- `ros_localhost_only: true` in config
- `export ROS_LOCALHOST_ONLY=1` before starting all nodes
- `export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST` (ROS2 Iron+)
- Different `ROS_DOMAIN_ID` on each host

### Bridge Doesn't Start / SIGSEGV

**Cause:** Plugin ABI mismatch — different Rust version or `zenoh` crate version between plugin and `zenohd`.

**Fix:** Use prebuilt packages from the same release, or build both from source with the same `cargo` toolchain.

### Services / Actions Not Visible Across Bridge

**Cause:** Using `zenoh-plugin-dds` instead of `zenoh-plugin-ros2dds`.

**Fix:** Switch to `zenoh-plugin-ros2dds`. The generic DDS bridge does not understand ROS2 service/action DDS topic patterns.

### Late Joining Subscribers Miss Historical Data

**Cause:** TRANSIENT_LOCAL `queries_timeout` too short, or `transient_local_cache_multiplier` too small.

**Fix:**
```json5
ros2dds: {
  queries_timeout: {
    transient_local_subscribers: 5.0,   // increase from default 5s if needed
  },
  transient_local_cache_multiplier: 20, // increase if many publishers on same topic
}
```

### Action get_result Timeout Too Short

**Symptom:** Long-running actions fail with timeout errors before completing.

**Fix:**
```json5
ros2dds: {
  queries_timeout: {
    actions: {
      get_result: [
        ".*navigate.*=3600",  // 1 hour for navigation actions
        ".*=300",
      ],
    },
  },
}
```

### High Memory Use with Many TRANSIENT_LOCAL Topics

**Cause:** Each TRANSIENT_LOCAL publisher route allocates a `PublicationCache`. With many topics and a high `transient_local_cache_multiplier`, this can consume significant memory.

**Fix:** Reduce `transient_local_cache_multiplier` to minimum needed for your publisher counts, or use `deny` to exclude topics that don't need historical delivery.

### Docker DDS Discovery Failure

**Cause:** Docker bridge networking doesn't support UDP multicast.

**Fix:** Always use `--net host` for DDS bridge containers on Linux:
```bash
docker run --init --net host eclipse/zenoh-bridge-ros2dds
```

Note: `--net host` is Linux-only. On macOS/Windows Docker, use explicit `connect` endpoints instead of relying on discovery.


## See Also

- [ROS2 Migration Guide](ros2-migration-guide.md) — step-by-step migration from DDS/ROS2 using the bridges documented here
- [DDS Context Guide](dds-context-guide.md) — the scalability problems in DDS that these bridges solve
- [Node Types Guide](node-types-guide.md) — how the bridge operates as a router or peer in the Zenoh topology
- [Config Connect Listen](config-connect-listen.md) — endpoint configuration for connecting bridges to Zenoh routers
