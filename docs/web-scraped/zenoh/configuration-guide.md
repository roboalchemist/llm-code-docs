# Zenoh Configuration Decision Tree

A practical guide to exact, copy-pasteable config snippets for every common scenario.

---

## How to Use This Guide

```
What are you building?
│
├── Local testing only? ──────────────────────► Section 1: No config needed
├── LAN pub/sub, no broker? ──────────────────► Section 2: Peer + Multicast
├── LAN with central router? ─────────────────► Section 3: Router + Clients
├── Two LANs connected? ──────────────────────► Section 4: Router-to-Router
├── Cloud + IoT edge? ────────────────────────► Section 5: Cloud Router + TLS Clients
├── Need low latency? ────────────────────────► Section 6: Low Latency + SHM
├── Need guaranteed delivery? ────────────────► Section 7: Reliable QoS
├── Need encryption? ─────────────────────────► Section 8: TLS Transport
├── Need access control? ─────────────────────► Section 9: ACL Rules
├── Bridging ROS 2? ──────────────────────────► Section 10: ROS 2 Bridge
├── Bridging MQTT? ───────────────────────────► Section 11: MQTT Bridge
├── Need storage/replay? ─────────────────────► Section 12: Storage Manager
├── Need rate limiting? ──────────────────────► Section 13: Downsampling
└── Need zero-copy SHM? ──────────────────────► Section 14: Shared Memory
```

---

## Section 1: Local Testing — Two Processes on the Same Machine

**Decision:** Same host, just exploring? Use defaults. Peer mode with multicast scouting
auto-discovers the other process. No config file needed at all.

```bash
# Terminal 1
z_pub --key demo/hello --value "Hello"

# Terminal 2  
z_sub --key demo/**
```

If you want an explicit config that documents what's happening:

```json5
// local-test.json5
// Both processes use this identical config
{
  mode: "peer",
  scouting: {
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
    },
  },
}
```

```bash
z_pub --config local-test.json5 --key demo/hello --value "Hello"
z_sub --config local-test.json5 --key demo/**
```

> **Why it works:** Both peers hear each other's multicast scout packets on loopback
> and auto-connect. No router, no static addresses required.

---

## Section 2: LAN Pub/Sub — No Broker (Peer Mesh)

**Decision:** All devices on the same network segment, no central coordinator wanted.
Each node discovers others via UDP multicast.

```json5
// peer-lan.json5  (same config on every node)
{
  mode: "peer",
  scouting: {
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",
      // "auto" picks the right interface automatically
      // Pin to a specific NIC if you have multiple: interface: "eth0"
      interface: "auto",
      ttl: 1,                  // stay within one network hop
      autoconnect: {
        peer: ["router", "peer"],
      },
    },
    gossip: {
      enabled: true,           // propagates discovery beyond direct neighbors
    },
  },
}
```

```bash
# Same config file on every machine on the LAN
z_pub --config peer-lan.json5 --key sensors/temperature --value "22.5"
z_sub --config peer-lan.json5 --key sensors/**
```

> **Limitation:** Multicast does not cross router boundaries (subnets). If you have
> multiple VLANs or subnets, use Section 4 instead.

---

## Section 3: LAN Pub/Sub — Central Router (Broker Mode)

**Decision:** You want a single known contact point. Clients don't discover each other
directly — all traffic routes through the router. Best for larger deployments or
when multicast is blocked.

### 3a. Router Config (run on the broker host, e.g. `192.168.1.10`)

```json5
// router.json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },
  scouting: {
    multicast: {
      enabled: false,           // router doesn't need multicast; clients connect directly
    },
  },
}
```

```bash
zenohd --config router.json5
```

### 3b. Client Config (all publishers and subscribers)

```json5
// client.json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.10:7447"],
    // Retry forever until router is available
    timeout_ms: { client: -1 },
    exit_on_failure: { client: false },
  },
  scouting: {
    multicast: {
      enabled: false,           // clients don't scout; they connect directly
    },
  },
}
```

```bash
z_pub --config client.json5 --key sensors/temperature --value "22.5"
z_sub --config client.json5 --key sensors/**
```

> **Rule of thumb:** Use `mode: "client"` for anything that should not participate
> in the routing plane — IoT sensors, application services, dashboards.

---

## Section 4: Connect Two Separate LANs (Router-to-Router)

**Decision:** You have two office networks, two factory floors, or two data centers.
Each LAN has its own router. The routers connect to each other to bridge traffic.

```
LAN A (192.168.1.x)          LAN B (10.0.0.x)
  [clients] ──► [Router A] ◄────────────────► [Router B] ◄── [clients]
               192.168.1.10                   10.0.0.10
```

### Router A Config (LAN A side)

```json5
// router-a.json5
{
  mode: "router",
  listen: {
    // Accept connections from LAN A clients AND from Router B
    endpoints: ["tcp/0.0.0.0:7447"],
  },
  connect: {
    // Actively connect to Router B on the other LAN
    endpoints: ["tcp/10.0.0.10:7447"],
    timeout_ms: { router: -1 },   // retry forever
    exit_on_failure: { router: false },
  },
}
```

### Router B Config (LAN B side)

```json5
// router-b.json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },
  // Router B passively waits; Router A initiates the connection.
  // Alternatively, both can connect to each other for redundancy.
}
```

### Clients on either LAN (same pattern as Section 3b)

```json5
// client-lan-a.json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.10:7447"],
  },
}
```

> **Traffic flow:** Client on LAN A publishes → Router A receives → Router A
> forwards to Router B → Router B delivers to subscribers on LAN B.
>
> **Redundancy:** Both routers can have `connect.endpoints` pointing at each other.
> Zenoh deduplicates and manages the redundant path automatically.

---

## Section 5: Cloud + IoT Edge Devices

**Decision:** A cloud VM acts as the always-reachable hub. Edge devices (IoT sensors,
gateways) are clients that connect out through NAT. TLS secures all traffic.

### 5a. Cloud Router Config

```json5
// cloud-router.json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      tls: {
        listen_private_key: "/etc/zenoh/certs/server.key",
        listen_certificate:  "/etc/zenoh/certs/server.crt",
        root_ca_certificate: "/etc/zenoh/certs/ca.crt",
        enable_mtls: true,      // require clients to present certificates
      },
    },
  },
  scouting: {
    multicast: {
      enabled: false,
    },
  },
}
```

### 5b. Edge Client Config

```json5
// edge-client.json5
{
  mode: "client",
  connect: {
    endpoints: ["tls/cloud.example.com:7447"],
    timeout_ms: { client: -1 },
    exit_on_failure: { client: false },
    retry: {
      period_init_ms: 1000,
      period_max_ms:  30000,    // back off to 30s max between retries
      period_increase_factor: 2,
    },
  },
  scouting: {
    multicast: {
      enabled: false,
    },
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate:  "/etc/zenoh/certs/ca.crt",
        connect_private_key:  "/etc/zenoh/certs/edge-device.key",
        connect_certificate:  "/etc/zenoh/certs/edge-device.crt",
        verify_name_on_connect: true,  // verify cloud.example.com matches cert CN
      },
    },
  },
}
```

> **Firewall note:** Only outbound port 7447 TCP needs to be open from the edge device.
> The cloud router needs inbound 7447 open. No inbound ports needed on edge devices.

---

## Section 6: Lowest Possible Latency

**Decision:** You need sub-millisecond delivery. Trade throughput guarantees for
raw speed. Works best on shared-memory (same host) or fast LAN.

> **Constraints before enabling:**
> - `lowlatency: true` requires `qos.enabled: false`
> - LowLatency transport does not support message fragmentation — keep messages
>   smaller than `batch_size` (default 65535 bytes)
> - QoS priority lanes are not preserved in lowlatency mode

```json5
// low-latency.json5
{
  mode: "peer",           // or "client" pointing at a low-latency router

  transport: {
    unicast: {
      lowlatency: true,
      qos: {
        enabled: false,   // REQUIRED when lowlatency is true
      },
    },
    link: {
      tx: {
        batch_size: 65535,
        queue: {
          batching: {
            enabled: false,  // disable batching to avoid artificial delay
          },
        },
      },
    },
    shared_memory: {
      enabled: true,          // zero-copy for same-host communication
      mode: "init",           // initialize SHM at startup, not on first use
      transport_optimization: {
        enabled: true,
        pool_size: 67108864,  // 64 MiB pool; tune to your message volume
        message_size_threshold: 1024,  // SHM for messages >= 1 KiB
      },
    },
  },
}
```

In your application code, combine with API-level settings:

```rust
// Rust API — set on the publisher
let publisher = session
    .declare_publisher("rt/sensor/data")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Drop)  // never block on full queue
    .express(true)                                 // skip batching at API level
    .await?;
```

Or use the config-level QoS overwrite (when NOT in lowlatency mode):

```json5
// qos-override.json5  (use when lowlatency is false)
{
  qos: {
    publication: [
      {
        key_exprs: ["rt/**"],
        config: {
          priority: "real_time",
          congestion_control: "drop",
          express: true,
        },
      },
    ],
  },
}
```

---

## Section 7: Guaranteed Message Delivery

**Decision:** You cannot afford to drop messages. You accept higher latency and
potential backpressure in exchange for delivery guarantees.

```json5
// reliable.json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.10:7447"],
  },
  transport: {
    unicast: {
      qos: {
        enabled: true,         // required for reliability settings
      },
    },
    link: {
      tx: {
        queue: {
          congestion_control: {
            block: {
              // How long to wait for queue space before dropping the transport.
              // 5 seconds (in microseconds). Increase for very bursty workloads.
              wait_before_close: 5000000,
            },
          },
          batching: {
            enabled: true,
            time_limit: 1,     // max 1ms batching delay
          },
        },
      },
    },
  },
}
```

In your application code:

```rust
// Rust — declare subscriber requesting reliable delivery
let subscriber = session
    .declare_subscriber("data/**")
    .reliability(Reliability::Reliable)
    .await?;

// Rust — publish with blocking congestion control (never drop)
let publisher = session
    .declare_publisher("data/critical")
    .reliability(Reliability::Reliable)
    .congestion_control(CongestionControl::Block)
    .await?;
```

Or force it via config QoS overwrite for all messages matching a pattern:

```json5
// reliable-qos-override.json5
{
  qos: {
    publication: [
      {
        key_exprs: ["data/critical/**"],
        config: {
          reliability: "reliable",
          congestion_control: "block",
          express: false,      // allow batching for throughput
        },
      },
    ],
  },
}
```

> **Trade-off:** `CongestionControl::Block` with a full queue will block the
> publishing thread until space is available or `wait_before_close` is exceeded.
> Size your queues (`transport.link.tx.queue.size`) appropriately for peak burst.

---

## Section 8: TLS Encryption

**Decision:** You need encrypted transport. Covers both server-only TLS (clients
verify server) and mutual TLS (mTLS, where server also verifies clients).

### 8a. Server-Only TLS (one-way — clients verify server)

```json5
// tls-router.json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      tls: {
        listen_private_key:  "/path/to/server.key",
        listen_certificate:  "/path/to/server.crt",
        root_ca_certificate: "/path/to/ca.crt",
        enable_mtls: false,
      },
    },
  },
}
```

```json5
// tls-client.json5
{
  mode: "client",
  connect: {
    endpoints: ["tls/myrouter.example.com:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate:    "/path/to/ca.crt",
        verify_name_on_connect: true,   // verify hostname matches cert
      },
    },
  },
}
```

### 8b. Mutual TLS (mTLS — both sides present certificates)

```json5
// mtls-router.json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      tls: {
        listen_private_key:  "/path/to/server.key",
        listen_certificate:  "/path/to/server.crt",
        root_ca_certificate: "/path/to/ca.crt",
        enable_mtls: true,              // require client certs
        close_link_on_expiration: true, // disconnect expired certs automatically
      },
    },
  },
}
```

```json5
// mtls-client.json5
{
  mode: "client",
  connect: {
    endpoints: ["tls/myrouter.example.com:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate:    "/path/to/ca.crt",
        connect_private_key:    "/path/to/client.key",
        connect_certificate:    "/path/to/client.crt",
        verify_name_on_connect: true,
      },
    },
  },
}
```

### Certificate Generation (self-signed, for testing)

```bash
# CA
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt -subj "/CN=ZenohCA"

# Server cert
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "/CN=myrouter.example.com"
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out server.crt

# Client cert (repeat with different CN per device for mTLS)
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/CN=edge-device-01"
openssl x509 -req -days 365 -in client.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out client.crt
```

---

## Section 9: Access Control (ACL)

**Decision:** You want to restrict which nodes can publish, subscribe, or query
which key expressions.

### 9a. Minimal ACL — Allow Everything (open default)

```json5
// acl-open.json5
{
  access_control: {
    enabled: true,
    default_permission: "allow",  // allow unless explicitly denied
    rules: [],
    subjects: [],
    policies: [],
  },
}
```

### 9b. Deny-by-Default with Explicit Allow Rules

```json5
// acl-strict.json5
{
  mode: "router",
  access_control: {
    enabled: true,
    default_permission: "deny",   // deny everything not explicitly allowed

    rules: [
      {
        id: "allow-sensors",
        messages: ["put", "delete", "declare_subscriber"],
        flows: ["egress", "ingress"],
        permission: "allow",
        key_exprs: ["sensors/**"],
      },
      {
        id: "allow-commands",
        messages: ["query", "reply", "declare_queryable"],
        flows: ["egress", "ingress"],
        permission: "allow",
        key_exprs: ["commands/**"],
      },
    ],

    subjects: [
      {
        id: "sensor-nodes",
        cert_common_names: ["edge-sensor-01", "edge-sensor-02"],
      },
      {
        id: "backend-services",
        cert_common_names: ["backend.internal"],
      },
      {
        id: "all-nodes",
        // empty subject = wildcard, matches everyone
      },
    ],

    policies: [
      {
        id: "sensors-can-publish",
        rules:    ["allow-sensors"],
        subjects: ["sensor-nodes"],
      },
      {
        id: "backend-can-query",
        rules:    ["allow-commands"],
        subjects: ["backend-services"],
      },
    ],
  },
}
```

### 9c. Interface-Based ACL (restrict by network interface)

```json5
// acl-interface.json5
{
  access_control: {
    enabled: true,
    default_permission: "deny",

    rules: [
      {
        id: "internal-only",
        messages: ["put", "declare_subscriber", "query", "reply",
                   "declare_queryable"],
        flows: ["ingress", "egress"],
        permission: "allow",
        key_exprs: ["internal/**"],
      },
    ],

    subjects: [
      {
        id: "local-interfaces",
        interfaces: ["lo", "eth0"],  // only traffic on these interfaces
      },
    ],

    policies: [
      {
        rules:    ["internal-only"],
        subjects: ["local-interfaces"],
      },
    ],
  },
}
```

> **Note:** `cert_common_names` requires TLS or QUIC. For username/password
> auth, use `usernames` in subjects and configure
> `transport.auth.usrpwd.dictionary_file`.

---

## Section 10: ROS 2 Bridging (zenoh-bridge-ros2dds)

**Decision:** You have ROS 2 nodes and want to bridge them over Zenoh, either
to connect across networks or to use Zenoh tooling with ROS 2 data.

```json5
// ros2-bridge.json5
// Used with: zenoh-bridge-ros2dds --config ros2-bridge.json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.10:7447"],
  },

  plugins: {
    ros2dds: {
      // ROS 2 domain ID to bridge (matches ROS_DOMAIN_ID env var)
      ros_domain_id: 0,

      // Namespace prefix added to all bridged topics/services
      // E.g. /robot_arm/cmd_vel instead of /cmd_vel
      namespace: "/robot_arm",

      // Which ROS 2 topics to bridge (allow-list). Omit to bridge everything.
      // allow: {
      //   publishers:  ["rt/chatter", "rt/sensor_msgs/**"],
      //   subscribers: ["rt/cmd_vel"],
      //   service_servers:   [],
      //   service_clients:   [],
      //   action_servers:    [],
      //   action_clients:    [],
      // },

      // Optionally deny specific topics
      // deny: {
      //   publishers: ["rt/rosout/**"],
      // },

      // Forward liveliness (ROS graph changes) across the bridge
      forward_discovery: true,

      // Route data between local ROS nodes and remote via Zenoh
      transient_local_cache_multiplier: 10,
    },
  },

  plugins_loading: {
    enabled: true,
  },
}
```

```bash
ROS_DOMAIN_ID=0 zenoh-bridge-ros2dds --config ros2-bridge.json5
```

> **Two-robot example:** Run the bridge on each robot with the same router
> endpoint. Robot A's `/cmd_vel` becomes available to Robot B automatically,
> prefixed by namespace if configured.

---

## Section 11: MQTT Bridging (zenoh-plugin-mqtt)

**Decision:** You have existing MQTT devices and want to integrate them into
a Zenoh network without changing device firmware.

```json5
// mqtt-bridge.json5
// Used with: zenohd --config mqtt-bridge.json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  plugins_loading: {
    enabled: true,
  },

  plugins: {
    mqtt: {
      // Port for MQTT clients to connect to (standard MQTT port)
      port: 1883,

      // Scope prefix: MQTT topic "sensors/temp" becomes Zenoh key "factory/sensors/temp"
      scope: "factory",

      // Whether to allow MQTT clients to publish to any Zenoh key
      // Set to false and configure allow_topics for tighter control
      allow_keyexpr_topics: true,

      // Optional: only bridge these MQTT topic patterns
      // allow_topics: ["sensors/**", "actuators/**"],

      // QoS mapping: MQTT QoS 0/1/2 → Zenoh
      // QoS 0 = best effort, QoS 1/2 = reliable
    },
  },
}
```

```bash
zenohd --config mqtt-bridge.json5
```

MQTT clients connect to port 1883 as normal. Their messages are automatically
bridged into the Zenoh key space:

```
MQTT topic: sensors/temperature    →  Zenoh key: factory/sensors/temperature
MQTT topic: actuators/fan/speed    →  Zenoh key: factory/actuators/fan/speed
```

---

## Section 12: Storage and Data Retrieval (Storage Manager)

**Decision:** You want late-joining subscribers to receive the last known value,
or you want to query historical data.

### 12a. In-Memory Storage (last-value cache)

```json5
// storage-memory.json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  plugins_loading: {
    enabled: true,
  },

  plugins: {
    storage_manager: {
      storages: {
        // "demo-cache" is just a name for this storage instance
        demo_cache: {
          key_expr: "sensors/**",    // store everything under sensors/
          volume: "memory",          // built-in, always available
          // complete: true tells queryors this storage has ALL keys in the range
          complete: true,
        },
      },
    },
  },

  // Enable admin space so you can inspect storages via HTTP
  adminspace: {
    enabled: true,
    permissions: { read: true, write: false },
  },
}
```

### 12b. Filesystem Storage (persistent across restarts)

```json5
// storage-filesystem.json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  plugins_loading: {
    enabled: true,
    search_dirs: ["/usr/lib", "/usr/local/lib"],
  },

  plugins: {
    storage_manager: {
      volumes: {
        filesystem: {
          // Directory where data files will be written
          dir: "/var/lib/zenoh/storage",
        },
      },
      storages: {
        persistent_sensors: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",  // strip this from the stored key path
          volume: {
            id: "filesystem",
          },
          complete: true,
          garbage_collection: {
            period:   30,           // GC runs every 30 seconds
            lifespan: 86400,        // discard metadata older than 24 hours
          },
        },
      },
    },
  },
}
```

Querying stored data from application code:

```rust
// Get the latest value for a specific key
let replies = session.get("sensors/temperature").await?;

// Get all stored values matching a wildcard
let replies = session.get("sensors/**").await?;
```

> **Timestamps required for replicated storage:** If you use `replication:` in
> your storage config, enable `timestamping.enabled: true` on the router
> so all stored messages carry a timestamp.

---

## Section 13: Rate Limiting (Downsampling)

**Decision:** A high-frequency source is flooding a slow link or consuming too
much bandwidth. You want to cap delivery frequency per key expression.

```json5
// downsampling.json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },

  downsampling: [
    {
      id: "limit-wlan-egress",
      // Only apply to traffic going OUT over the wireless interface
      interfaces: ["wlan0"],
      flows: ["egress"],
      messages: ["put", "delete"],

      rules: [
        // High-frequency IMU data: cap at 10 Hz over WiFi
        { key_expr: "robot/imu/**",         freq: 10.0  },
        // Camera frames: cap at 2 Hz over WiFi
        { key_expr: "robot/camera/**",      freq: 2.0   },
        // Slow telemetry: pass through unchanged (no rule = no limit)
        // { key_expr: "robot/telemetry/**" }  ← omit = unlimited
      ],
    },
    {
      id: "limit-all-debug",
      // Cap debug streams everywhere regardless of interface
      flows: ["egress", "ingress"],
      messages: ["put"],
      rules: [
        { key_expr: "debug/**",  freq: 1.0 },
      ],
    },
  ],
}
```

> **Frequency unit:** `freq` is in Hz. `freq: 0.1` = one message per 10 seconds.
> `freq: 100.0` = max 100 messages/second. Messages exceeding the rate are
> silently dropped at the router before forwarding.

---

## Section 14: Shared Memory Zero-Copy

**Decision:** Publisher and subscriber are on the same host. You want to skip
network serialization entirely and pass data via shared memory.

> **Requirements:**
> - Both publisher and subscriber must have `shared_memory.enabled: true`
> - Zenoh must be compiled with the `shared-memory` feature flag
> - Both processes must be on the same physical host

```json5
// shm-config.json5  (same config for both publisher and subscriber)
{
  mode: "peer",

  transport: {
    shared_memory: {
      enabled: true,
      // "init" avoids first-message latency spike; "lazy" saves startup time
      mode: "init",

      transport_optimization: {
        enabled: true,
        // 64 MiB pool — tune to (peak_msg_size × concurrent_messages × 2)
        pool_size: 67108864,
        // Only use SHM for messages at or above this size (bytes)
        // Small messages are cheaper to copy than to SHM-map
        message_size_threshold: 4096,
      },
    },

    unicast: {
      // SHM works best with low-latency transport
      // Comment out if you need QoS priorities
      lowlatency: true,
      qos: {
        enabled: false,   // required when lowlatency: true
      },
    },
  },

  scouting: {
    multicast: {
      enabled: true,
    },
  },
}
```

In application code, allocate from the SHM pool explicitly (Rust):

```rust
use zenoh::shm::*;

// Publisher side: allocate from SHM pool
let shm_provider = session
    .shm()
    .provider()
    .with_layout_and_provider(
        MemoryLayout::new(payload_size, AllocAlignment::default())?,
        POSIX_PROTOCOL_ID,
    )
    .res()?;

let mut shm_buf = shm_provider.alloc().res()?;
shm_buf[..data.len()].copy_from_slice(&data);
publisher.put(shm_buf).res().await?;

// Subscriber side: receives SHMBuf automatically if SHM is enabled
// No special code needed — zenoh handles the mapping transparently
```

> **Verification:** Use the admin space or `z_info` to confirm SHM is negotiated.
> If either side has SHM disabled, zenoh transparently falls back to serialized
> network transport without error.

---

## Quick Reference Table

| Goal | Config Key | Value |
|------|-----------|-------|
| Set node role | `mode` | `"router"` \| `"peer"` \| `"client"` |
| Accept connections | `listen.endpoints` | `["tcp/0.0.0.0:7447"]` |
| Connect to router | `connect.endpoints` | `["tcp/host:7447"]` |
| Retry connect forever | `connect.timeout_ms` | `{ client: -1 }` |
| Enable multicast discovery