# Zenoh Configuration Decision Tree

A practical guide to the minimal config you actually need, organized by what you're trying to do.

---

## How to Use This Guide

```
What are you building?
│
├─ Local testing only? ──────────────────────────► No config needed (Section 1)
│
├─ LAN pub/sub?
│   ├─ No central broker? ───────────────────────► Peer + multicast (Section 2)
│   └─ Central router? ──────────────────────────► Client + router (Section 3)
│
├─ Multiple LANs / sites? ───────────────────────► Router-to-router (Section 4)
│
├─ Cloud + IoT? ─────────────────────────────────► Cloud router + TLS (Section 5)
│
├─ Performance critical?
│   ├─ Lowest latency? ──────────────────────────► Low-latency + SHM (Section 6)
│   └─ Guaranteed delivery? ─────────────────────► Reliable + Block (Section 7)
│
├─ Security?
│   ├─ Encryption? ──────────────────────────────► TLS transport (Section 8)
│   └─ Access control? ──────────────────────────► ACL rules (Section 9)
│
├─ Bridging?
│   ├─ ROS 2? ───────────────────────────────────► zenoh-bridge-ros2dds (Section 10)
│   └─ MQTT? ────────────────────────────────────► zenoh-plugin-mqtt (Section 11)
│
├─ Data persistence? ────────────────────────────► Storage manager (Section 12)
├─ Rate limiting? ───────────────────────────────► Downsampling (Section 13)
└─ Zero-copy? ───────────────────────────────────► Shared memory (Section 14)
```

---

## Section 1 — Local Testing (Two Processes, Same Machine)

**Decision:** Same machine, just want it to work → use defaults, no config file needed.

Both processes run as `peer` mode (the default). Multicast scouting finds them automatically on loopback.

```json5
// No config file needed.
// Run your publisher and subscriber with zero configuration.
// They will auto-discover each other via multicast on 224.0.0.224:7446.
//
// If you want to be explicit, this is the equivalent minimal config:
{
  mode: "peer",
  scouting: {
    multicast: {
      enabled: true,
    },
  },
}
```

> **Tip:** For quick CLI testing: `z_pub` and `z_sub` from zenoh examples work with zero flags.

---

## Section 2 — LAN Pub/Sub Without a Broker (Peer Mode)

**Decision:** Multiple machines on the same subnet, no router process, fully decentralized.

All nodes run as `peer`. Multicast scouting handles discovery automatically within the subnet.

```json5
// peer.json5 — same file used on every node
{
  mode: "peer",
  scouting: {
    multicast: {
      enabled: true,
      address: "224.0.0.224:7446",  // default multicast group
      interface: "auto",             // auto-selects the right NIC
      autoconnect: {
        peer: ["router", "peer"],    // connect to any peer or router found
      },
    },
  },
}
```

> **When this breaks:** Multicast is blocked between VLANs and most cloud VPCs. If nodes can't see each other, move to Section 3 or 4.

---

## Section 3 — LAN Pub/Sub With a Central Router

**Decision:** You want a stable broker, easier topology management, or clients on constrained devices.

Run one `zenohd` instance as the router. All publishers and subscribers run as `client`.

### Router config (`router.json5`)

```json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],  // listen on all interfaces
  },
  scouting: {
    multicast: {
      enabled: true,  // lets clients find this router via multicast
    },
  },
}
```

### Client config (`client.json5`)

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"],  // replace with your router's IP
  },
  scouting: {
    multicast: {
      enabled: false,  // clients don't need multicast when router IP is known
    },
  },
}
```

> **Start order:** Start the router first. Clients retry connection automatically (default: up to 4 s between retries).

---

## Section 4 — Connecting Two Separate LANs

**Decision:** Devices on different physical networks (two offices, data center + factory floor, etc.) that need to share data.

Deploy one router per LAN. The routers connect to each other explicitly. Clients on each LAN only need to reach their local router.

```
  LAN A                          LAN B
  ┌──────────────┐               ┌──────────────┐
  │ client-a     │               │ client-b     │
  │    │         │               │    │         │
  │ router-a ───────────────── router-b         │
  │ :7447        │  TCP/TLS      │ :7447        │
  └──────────────┘               └──────────────┘
```

### Router A config (`router-a.json5`)

```json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },
  connect: {
    endpoints: ["tcp/203.0.113.20:7447"],  // router-b's public IP
    timeout_ms: { router: -1 },            // retry forever until router-b is up
  },
}
```

### Router B config (`router-b.json5`)

```json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },
  // Router-B just listens; Router-A initiates the connection.
  // Avoids duplicate connections. Only one side needs to connect.
}
```

### Client on either LAN (`client.json5`)

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.1:7447"],  // local router only
  },
}
```

> **Important:** Only one router should initiate the inter-router connection to avoid duplicates. Use TLS here (Section 8) for traffic over public internet.

---

## Section 5 — Cloud Router + IoT Edge Devices

**Decision:** Edge devices (Raspberry Pi, MCUs, embedded Linux) publish data to a cloud-hosted router. Security is essential.

```
  Edge (IoT)                    Cloud
  ┌─────────────────┐           ┌──────────────────────┐
  │ sensor-device   │  TLS/TCP  │ cloud-router         │
  │ (client mode)   ├──────────►│ (router mode)        │
  │ low resources   │           │ public IP, port 7447 │
  └─────────────────┘           └──────────────────────┘
```

### Cloud router config (`cloud-router.json5`)

```json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      tls: {
        listen_private_key: "/etc/zenoh/certs/server.key",
        listen_certificate: "/etc/zenoh/certs/server.crt",
        root_ca_certificate: "/etc/zenoh/certs/ca.crt",
        enable_mtls: true,  // require client certificates
      },
    },
  },
  scouting: {
    multicast: {
      enabled: false,  // no multicast in cloud
    },
  },
}
```

### Edge device config (`edge-client.json5`)

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tls/cloud.example.com:7447"],
    timeout_ms: { client: -1 },    // keep retrying if cloud is unreachable
    exit_on_failure: { client: false },
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/certs/ca.crt",
        connect_private_key: "/etc/zenoh/certs/device.key",
        connect_certificate: "/etc/zenoh/certs/device.crt",
        verify_name_on_connect: true,
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

> **Certificate setup:** Each device gets its own cert signed by your CA. `enable_mtls: true` on the router rejects uncertified devices.

---

## Section 6 — Lowest Possible Latency

**Decision:** Same machine or directly connected nodes where you need microsecond-level latency (robotics, HFT, real-time control).

**Constraints:** `lowlatency` is **incompatible** with `qos: enabled: true`. You must disable QoS. Also: messages must fit in one batch (no fragmentation); max size = `batch_size` (default 65535 bytes).

```json5
// lowlatency.json5
{
  mode: "peer",
  transport: {
    unicast: {
      lowlatency: true,
      qos: {
        enabled: false,  // REQUIRED when lowlatency is true
      },
    },
    link: {
      tx: {
        queue: {
          batching: {
            enabled: false,  // disable batching to avoid artificial delay
          },
        },
      },
    },
    shared_memory: {
      enabled: true,       // enable SHM negotiation (zero-copy on same host)
      mode: "init",        // pre-initialize to avoid first-message latency spike
      transport_optimization: {
        enabled: true,
        message_size_threshold: 1024,  // apply SHM for messages >= 1KB
      },
    },
  },
  scouting: {
    multicast: {
      enabled: false,  // skip scouting delay if peers are known
    },
  },
  connect: {
    endpoints: ["tcp/127.0.0.1:7447"],
  },
}
```

**In your application code, also set:**

```rust
// Rust
let publisher = session
    .declare_publisher("rt/sensor")
    .priority(Priority::RealTime)
    .congestion_control(CongestionControl::Drop)
    .express(true)  // skip batching at API level
    .await?;
```

```python
# Python
pub = session.declare_publisher(
    "rt/sensor",
    priority=Priority.REAL_TIME(),
    congestion_control=CongestionControl.DROP(),
    express=True,
)
```

> **SHM only works between processes on the same host.** For network peers, the SHM path falls back to serialized transport automatically.

---

## Section 7 — Guaranteed Message Delivery

**Decision:** You cannot afford to lose messages (alarms, commands, audit logs). Willing to trade latency for reliability.

Reliability in zenoh is set **per publisher/subscriber** in the API, not in the config file. However, you can enforce it globally via the `qos` config override.

### Config-level enforcement (`reliable.json5`)

```json5
{
  mode: "peer",  // or "client"
  transport: {
    unicast: {
      qos: {
        enabled: true,  // QoS must be enabled for reliability settings to work
      },
    },
    link: {
      tx: {
        queue: {
          congestion_control: {
            block: {
              // Wait up to 5 seconds before closing transport on a blocked send.
              // Increase if your consumers can be slow but must not lose data.
              wait_before_close: 5000000,  // microseconds = 5 seconds
            },
          },
        },
      },
    },
  },
  // Force reliable + block on specific key expressions regardless of publisher settings
  qos: {
    publication: [
      {
        key_exprs: ["commands/**", "alarms/**"],
        config: {
          congestion_control: "block",      // never drop, block the sender instead
          reliability: "reliable",
          priority: "data_high",
          express: false,                   // allow batching for efficiency
        },
      },
    ],
  },
}
```

**In your application code:**

```rust
// Rust — subscriber side must also declare Reliable
let subscriber = session
    .declare_subscriber("commands/**")
    .reliability(Reliability::Reliable)
    .await?;
```

> **Trade-off:** `CongestionControl::Block` will pause your publisher thread if the network can't keep up. Size your queue (`transport.link.tx.queue.size`) appropriately for your burst rate.

---

## Section 8 — TLS Encryption

**Decision:** Traffic crosses untrusted networks (internet, shared infrastructure). Needs encryption. Optionally mutual authentication.

### One-way TLS (server authenticated only)

The router presents a certificate; clients verify it but don't need their own cert.

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
        listen_private_key: "/path/to/server.key",
        listen_certificate: "/path/to/server.crt",
        root_ca_certificate: "/path/to/ca.crt",
        enable_mtls: false,
        verify_name_on_connect: true,
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
    endpoints: ["tls/router.example.com:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate: "/path/to/ca.crt",
        verify_name_on_connect: true,
      },
    },
  },
}
```

### Mutual TLS (mTLS — both sides authenticated)

Add client key/cert, enable `enable_mtls: true` on the router.

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
        listen_private_key: "/path/to/server.key",
        listen_certificate: "/path/to/server.crt",
        root_ca_certificate: "/path/to/ca.crt",
        enable_mtls: true,                          // require client certs
        close_link_on_expiration: true,             // disconnect expired clients
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
    endpoints: ["tls/router.example.com:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate: "/path/to/ca.crt",
        connect_private_key: "/path/to/client.key",
        connect_certificate: "/path/to/client.crt",
        verify_name_on_connect: true,
      },
    },
  },
}
```

> **QUIC alternative:** Replace `tls/` with `quic/` in endpoints. QUIC uses the same TLS config block and adds multiplexing + better congestion handling over lossy links.

---

## Section 9 — Access Control

**Decision:** Multiple clients connect to a shared router. You need to restrict which key expressions each client can publish to or subscribe from.

Access control has three parts: **subjects** (who), **rules** (what), and **policies** (who gets what).

```json5
// acl-router.json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      tls: {
        listen_private_key: "/path/to/server.key",
        listen_certificate: "/path/to/server.crt",
        root_ca_certificate: "/path/to/ca.crt",
        enable_mtls: true,  // cert common names used as subject identifiers
      },
    },
  },
  access_control: {
    enabled: true,
    default_permission: "deny",  // deny everything not explicitly allowed

    // --- WHO ---
    subjects: [
      {
        id: "sensors",
        cert_common_names: ["sensor.example.com"],  // matches TLS cert CN
      },
      {
        id: "dashboard",
        cert_common_names: ["dashboard.example.com"],
      },
      {
        id: "admin",
        cert_common_names: ["admin.example.com"],
      },
    ],

    // --- WHAT ---
    rules: [
      {
        id: "sensor-publish",
        messages: ["put", "delete"],
        flows: ["ingress"],         // ingress = arriving at router from this client
        permission: "allow",
        key_exprs: ["sensors/**"],
      },
      {
        id: "dashboard-subscribe",
        messages: ["declare_subscriber", "query", "reply"],
        flows: ["egress"],          // egress = leaving the router toward this client
        permission: "allow",
        key_exprs: ["sensors/**"],
      },
      {
        id: "admin-all",
        messages: [
          "put", "delete", "declare_subscriber",
          "query", "reply", "declare_queryable",
        ],
        flows: ["ingress", "egress"],
        permission: "allow",
        key_exprs: ["**"],
      },
    ],

    // --- WHO GETS WHAT ---
    policies: [
      {
        id: "sensor-policy",
        subjects: ["sensors"],
        rules: ["sensor-publish"],
      },
      {
        id: "dashboard-policy",
        subjects: ["dashboard"],
        rules: ["dashboard-subscribe"],
      },
      {
        id: "admin-policy",
        subjects: ["admin"],
        rules: ["admin-all"],
      },
    ],
  },
}
```

> **Flow direction reference:**
> - `ingress` = message arriving at this node from the network (a client is sending to you)
> - `egress` = message leaving this node to the network (you are forwarding to a client)

---

## Section 10 — ROS 2 Bridging

**Decision:** You have ROS 2 nodes using DDS and want to bridge them over zenoh (for multi-robot, cloud, or cross-domain communication).

Uses the separate `zenoh-bridge-ros2dds` binary. Config goes in its own file.

```json5
// ros2-bridge.json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"],  // your zenoh router
  },

  plugins_loading: {
    enabled: true,
  },

  plugins: {
    ros2dds: {
      // ROS 2 domain ID to bridge (default: 0, or reads ROS_DOMAIN_ID env var)
      domain: 0,

      // Namespace prefix added to all bridged topics/services
      // e.g. /robot1/cmd_vel becomes zenoh key: robot1/cmd_vel
      namespace: "/robot1",

      // Which ROS topics to allow (default: all)
      // Use key expression wildcards
      allow: {
        publishers: ["**"],
        subscribers: ["**"],
        service_servers: ["**"],
        service_clients: ["**"],
        action_servers: ["**"],
        action_clients: ["**"],
      },

      // Whether to bridge liveliness (node discovery)
      liveliness: true,
    },
  },
}
```

**Run it:**
```bash
zenoh-bridge-ros2dds --config ros2-bridge.json5
```

> **Multi-robot tip:** Give each robot a unique `namespace`. All robots' topics are then visible as `robot1/cmd_vel`, `robot2/cmd_vel`, etc. under a single zenoh router.

---

## Section 11 — MQTT Bridging

**Decision:** You have existing MQTT devices/brokers and want to integrate them into a zenoh network without rewriting firmware.

Uses `zenoh-plugin-mqtt`. MQTT topics are mapped to zenoh key expressions.

```json5
// mqtt-bridge.json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"],  // zenoh router
  },

  plugins_loading: {
    enabled: true,
  },

  plugins: {
    mqtt: {
      // Port for the embedded MQTT broker that your MQTT devices connect to
      port: 1883,

      // Scope prefix: MQTT topic "temperature/room1"
      // becomes zenoh key "home/temperature/room1"
      scope: "home",

      // Whether to allow MQTT clients to publish into zenoh (default: true)
      allow_raw_publish: true,

      // QoS mapping: zenoh reliability for MQTT QoS levels
      // (QoS 0 = best effort, QoS 1/2 = reliable)
      generalise_pub: [],
      generalise_sub: [],
    },
  },
}
```

**Run it:**
```bash
zenohd --config mqtt-bridge.json5
# or as a plugin alongside zenohd
```

> **Topic mapping:** MQTT `sensors/temp` ↔ zenoh key `home/sensors/temp` (with `scope: "home"`). MQTT wildcards `#` and `+` map to zenoh `**` and `*`.

---

## Section 12 — Storage and Retrieval (Data Persistence)

**Decision:** Late-joining subscribers should receive the last known value, or you need queryable historical data.

### In-memory storage (last value cache)

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
      volumes: {
        // "memory" volume is always available, no extra backend needed
      },
      storages: {
        sensor_cache: {
          // Store all keys under "sensors/"
          key_expr: "sensors/**",
          volume: "memory",
          // Reply to late subscribers with stored values
          complete: true,
        },
      },
    },
  },
}
```

### Filesystem storage (survives restarts)

```json5
// storage-filesystem.json5
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
      volumes: {
        filesystem: {
          // Uses zenoh-backend-filesystem
          dir: "/var/lib/zenoh/storage",
        },
      },
      storages: {
        sensor_log: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",  // store keys without the "sensors/" prefix
          volume: {
            id: "filesystem",
          },
          garbage_collection: {
            period: 60,       // run GC every 60 seconds
            lifespan: 86400,  // keep data for 24 hours
          },
        },
      },
    },
  },
}
```

> **Query stored data:** Use `session.get("sensors/**")` — the storage replies to zenoh queries automatically.

---

## Section 13 — Rate Limiting (Downsampling)

**Decision:** A fast sensor floods the network. You want to cap how often its data is forwarded over a specific interface or to specific subscribers.

```json5
// downsampling.json5
{
  mode: "router",

  downsampling: [
    {
      id: "wifi-rate-limit",
      // Only apply downsampling on the WiFi interface
      interfaces: ["wlan0"],
      // Only for egress (outgoing from this router toward clients)
      flows: ["egress"],
      messages: ["put"],
      rules: [
        // Camera stream: max 5 frames/sec over WiFi
        { key_expr: "robot/camera/**", freq: 5.0 },
        // IMU at 10 Hz over WiFi (original may be 1000 Hz)
        { key_expr: "robot/imu/**",    freq: 10.0 },
        // Everything else on wlan0: max 1 msg/sec
        { key_expr: "**",              freq: 1.0 },
      ],
    },
    {
      id: "wan-rate-limit",
      // More aggressive limiting on the WAN uplink
      interfaces: ["eth1"],
      flows: ["egress"],
      messages: ["put"],
      rules: [
        { key_expr: "telemetry/**", freq: 0.1 },  // once every 10 seconds
      ],
    },
  ],
}
```

> **Frequency is in Hz.** `freq: 0.1` = once per 10 seconds. The first message always passes through; subsequent messages within the period are dropped.

---

## Section 14 — Shared Memory Zero-Copy

**Decision:** Multiple processes on the same machine exchange large messages (video frames, point clouds, tensors) and you want to avoid copies.

SHM is **only** effective between processes on the same machine. Across the network, zenoh automatically falls back to normal serialization.

```json5
// shm.json5
{
  mode: "peer",

  transport: {
    shared_memory: {
      enabled: true,
      // "init" pre-allocates SHM at startup — eliminates first-message latency.
      // Use "lazy" to save memory if SHM might not always be used.
      mode: "init",
      transport_optimization: {
        enabled: true,
        // SHM pool size in bytes (default 16 MiB, increase for large messages)
        pool_size: 67108864,   // 64 MiB
        // Only use SHM for messages >= this size (bytes)
        // Small messages are cheaper to copy than to SHM-allocate
        message_size_threshold: 4096,  // 4 KB
      },
    },
    unicast: {
      qos: {
        enabled: true,
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

**Publisher side (Rust) — allocate directly into SHM:**

```rust
// Publisher must use SHM-allocated buffers for zero-copy to activate
let mut shm_client = ShmClientBuilder::default().build()?;
let mut buf = shm_client.alloc(4096).await?;
// write into buf...
publisher.put(buf).await?;  // zero-copy: no memcpy on the subscriber side
```

> **Verification:** If both publisher and subscriber have `shared_memory.enabled: true`, zenoh performs a SHM probe at session open. Check logs for `SHM probing succeeded`.

---

## Quick Reference Table

| Goal | Config Key | Value |
|---|---|---|
| Set node type | `mode` | `"router"` / `"peer"` / `"client"` |
| Listen for connections | `listen.endpoints` | `["tcp/0.0.0.0:7447"]` |
| Connect to router | `connect.endpoints` | `["tcp/192.168.1.x:7447"]` |
| Enable multicast discovery | `scouting.multicast.enabled` | `true` |
| Disable multicast (cloud/WAN) | `scouting.multicast.enabled` | `false` |
| Retry connect forever | `connect.timeout_ms` | `{ client: -1 }` |
| Low latency mode | `transport.unicast.lowlatency` | `true` |
| Disable QoS (required for lowlatency) | `transport.unicast.qos.enabled` | `false` |
| Disable batching | `transport.link.tx.queue.batching.enabled` | `false` |
| Enable SHM | `transport.shared_memory.enabled` | `true` |
| SHM pool size | `transport.shared_memory.transport_optimization.pool_size` | bytes, e.g. `67108864` |
| SHM init at startup | `transport.shared_memory.mode` | `"init"` |
| TLS server cert | `transport.link.tls.listen_certificate` | `"/path/to/server.crt"` |
| TLS server key | `transport.link.tls.listen_private_key` | `"/path/to/server.key"` |
| TLS CA cert | `transport.link.tls.root_ca_certificate` | `"/path/to/ca.crt"` |
| Require client certs (mTLS) | `transport.link.tls.enable_mtls` | `true` |
| Enable ACL | `access_control.enabled` | `true` |
| Default deny policy | `access_control.default_permission` | `"deny"` |
| Block publisher on congestion | `qos.publication[].config.congestion_control` | `"block"` |
| Force reliable delivery | `qos.publication[].config.reliability` | `"reliable"` |
| Rate limit on interface | `downsampling[].rules[].freq` | Hz as float, e.g. `5.0` |
| In-memory storage | `plugins.storage_manager.storages.x.volume` | `"memory"` |
| Storage key scope | `plugins.storage_manager.storages.x.key_expr` | `"sensors/**"` |
| Enable admin space | `adminspace.enabled` | `true` |
| Enable compression | `transport.unicast.compression.enabled` | `true` |
| Timestamping (router) | `timestamping.enabled` | `{ router: true }` |

---

## Common Mistakes

| Mistake | Symptom | Fix |
|---|---|---|
| `lowlatency: true` with `qos.enabled: true` | Session fails to open | Set `qos.enabled: false` |
| Large messages with `lowlatency` | Messages silently dropped | Messages must be < `batch_size` (65535 B) |
| Both routers connecting to each other | Duplicate transport sessions | Only one router initiates inter-router connect |
| `mode: "client"` with multicast expected to work | Clients never find each other | Clients don't peer directly; they need a router |
| SHM enabled on publisher only | Falls back to copy | Enable SHM on both publisher and subscriber |
| `access_control` with `default_permission: "deny"` and no rules | Everything blocked | Add explicit allow rules for your key expressions |
| Connecting with `tcp/` to a `tls/` listener | Connection refused or handshake error | Match protocol in connect/listen endpoints |
| `downsampling` on a `peer` node for network traffic | No effect on intra-process | Apply downsampling on the router that forwards the traffic |