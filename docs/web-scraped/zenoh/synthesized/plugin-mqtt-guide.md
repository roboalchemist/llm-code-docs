# Zenoh MQTT Plugin: Comprehensive Guide

The `zenoh-plugin-mqtt` integrates MQTT ecosystems with Zenoh's distributed pub/sub infrastructure. The plugin implements an **MQTT broker** that translates between MQTT pub/sub and Zenoh pub/sub — MQTT clients connect to it and their publications flow bidirectionally through the Zenoh routing layer.

**Two deployment forms:**
- **`zenoh-plugin-mqtt`** — a dynamic library loaded by `zenohd`
- **`zenoh-bridge-mqtt`** — a standalone binary that acts as both MQTT broker and Zenoh peer/client

---

## Table of Contents

- [How It Works](#how-it-works)
  - [Topic-to-Key-Expression Mapping](#topic-to-key-expression-mapping)
- [Configuration Reference](#configuration-reference)
  - [`port`](#port)
  - [`scope`](#scope)
  - [`allow`](#allow)
  - [`deny`](#deny)
  - [`generalise_subs`](#generalise_subs)
  - [`generalise_pubs`](#generalise_pubs)
  - [`tx_channel_size`](#tx_channel_size)
  - [`tls`](#tls)
  - [`auth`](#auth)
  - [`work_thread_num`](#work_thread_num)
  - [`max_block_thread_num`](#max_block_thread_num)
- [Topic Scoping and Multi-Site Isolation](#topic-scoping-and-multi-site-isolation)
  - [The Collision Problem](#the-collision-problem)
  - [The Solution: Per-Site Scopes](#the-solution-per-site-scopes)
  - [Complete Multi-Site Example](#complete-multi-site-example)
- [Allow/Deny Filtering](#allowdeny-filtering)
  - [Logic](#logic)
  - [Pattern Examples](#pattern-examples)
- [QoS Mapping](#qos-mapping)
  - [MQTT → Zenoh (inbound)](#mqtt-zenoh-inbound)
  - [Zenoh → MQTT (outbound)](#zenoh-mqtt-outbound)
  - [Retained Messages](#retained-messages)
- [Operating Modes](#operating-modes)
  - [Mode 1: Plugin Within zenohd](#mode-1-plugin-within-zenohd)
  - [Mode 2: Standalone Bridge](#mode-2-standalone-bridge)
- [Complete Configuration Examples](#complete-configuration-examples)
  - [Example 1: Basic MQTT Broker for Factory Sensors](#example-1-basic-mqtt-broker-for-factory-sensors)
  - [Example 2: Secure MQTT Broker with mTLS and Authentication](#example-2-secure-mqtt-broker-with-mtls-and-authentication)
  - [Example 3: Multi-Site MQTT Bridge with Scoping](#example-3-multi-site-mqtt-bridge-with-scoping)
  - [Example 4: MQTT with Allow/Deny Filtering](#example-4-mqtt-with-allowdeny-filtering)
- [Admin Space](#admin-space)
- [Installation](#installation)
  - [Debian/Ubuntu](#debianubuntu)
  - [Docker](#docker)
  - [Manual / Build from Source](#manual-build-from-source)
- [Use Cases](#use-cases)

## How It Works

The plugin acts as an MQTT broker. MQTT clients (any v3 or v5 client) connect to it. When an MQTT client publishes, the plugin translates the topic to a Zenoh key expression and issues a Zenoh `put`. When a Zenoh subscriber publishes to a matching key expression, the plugin forwards it to subscribed MQTT clients.

```
MQTT Client → publish("sensors/temp", 23.4)
                    ↓
              [zenoh-plugin-mqtt]
              topic → KE: scope + "/" + topic
                    ↓
Zenoh network → key_expr: "factory1/sensors/temp"
                    ↓
Other zenoh apps, storages, routers
```

The reverse path works identically: zenoh publications matching an MQTT client's subscription are forwarded to that client.

### Topic-to-Key-Expression Mapping

MQTT wildcards map to Zenoh wildcards:

| MQTT | Zenoh | Meaning |
|------|-------|---------|
| `+` | `*` | Single level |
| `#` | `**` | Multi-level |
| `/` | `/` | Separator |

Examples:
- MQTT topic `device/123/temperature` → zenoh KE `device/123/temperature`
- MQTT subscription `device/#` → zenoh subscription `device/**`
- MQTT subscription `factory/+/status` → zenoh subscription `factory/*/status`

When `scope` is configured, it is prepended: `scope + "/" + mqtt_topic`. The reverse mapping strips the scope prefix when delivering to MQTT clients.

**Limitations:**
- MQTT topics with empty levels (starting with `/`, ending with `/`, or containing `//`) are not supported
- Zenoh KEs with wildcards cannot be delivered to MQTT clients (wildcards are resolved at subscription time, not publication time)

---

## Configuration Reference

Configuration can be provided via a JSON5 file (`-c config.json5`) or via command-line arguments. Command-line flags override file settings.

### `port`

**Type:** string or integer
**Default:** `"0.0.0.0:1883"`
**CLI:** `-p, --port`

TCP address for the MQTT broker to listen on. Accepts:
- Port number only: `1883` → binds to `0.0.0.0:1883`
- Full address: `"192.168.1.10:1883"` → binds to a specific interface

```json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
    }
  }
}
```

For MQTTS (TLS), clients connect to the same port — the TLS upgrade is handled by the `tls` section.

---

### `scope`

**Type:** string (valid zenoh key expression segment)
**Default:** unset (no prefix added)
**CLI:** `-s, --scope`

A prefix prepended to all MQTT topics when mapping to Zenoh key expressions. This is the primary mechanism for **multi-site isolation** — two MQTT systems using identical topic names can coexist on the same Zenoh network without collision.

The scope must be a valid zenoh key expression (no leading/trailing `/`, no `**`).

```json5
{
  plugins: {
    mqtt: {
      scope: "factory1",
    }
  }
}
```

With `scope: "factory1"`:
- MQTT publish `sensors/temp` → zenoh put on `factory1/sensors/temp`
- MQTT subscribe `sensors/#` → zenoh subscribe `factory1/sensors/**`
- Zenoh put on `factory1/sensors/temp` → MQTT publish `sensors/temp` (scope stripped)

**Important:** Zenoh publications must include the scope prefix to reach MQTT clients. A put on `sensors/temp` will NOT reach an MQTT client subscribed to `sensors/temp` when a scope is configured.

---

### `allow`

**Type:** string (regular expression)
**Default:** unset (all topics allowed)
**CLI:** `-a, --allow`

A regex matched against the raw MQTT topic name (before scope is applied). Only topics that match are routed over Zenoh; non-matching topics are handled locally (MQTT-to-MQTT routing only, using `Locality::SessionLocal`).

```json5
{
  plugins: {
    mqtt: {
      allow: "^sensors/|^actuators/",
    }
  }
}
```

**Effect of `allow` without `deny`:** topics matching the regex are routed to zenoh; all others are silently restricted to local MQTT routing.

---

### `deny`

**Type:** string (regular expression)
**Default:** unset (no topics denied)
**CLI:** `--deny`

A regex matched against the raw MQTT topic name. Topics that match are **not** routed over Zenoh; they are restricted to local MQTT routing.

```json5
{
  plugins: {
    mqtt: {
      deny: "^internal/|^debug/",
    }
  }
}
```

**When both `allow` and `deny` are set**, a topic is routed over zenoh only if it matches `allow` AND does not match `deny`:

```
// From mqtt_helpers.rs:
(Some(allow), Some(deny)) => allow.is_match(mqtt_topic) && !deny.is_match(mqtt_topic)
```

This means `deny` takes precedence over `allow` when both match the same topic.

---

### `generalise_subs`

**Type:** array of zenoh key expressions
**Default:** `[]` (empty)
**CLI:** `-r, --generalise-sub` (repeatable)

A list of zenoh key expressions used to **aggregate** subscriptions declared by the plugin. Instead of declaring many individual subscriptions (one per MQTT client subscription), the plugin aggregates them under these broader key expressions. This reduces discovery traffic in large zenoh networks.

```json5
{
  plugins: {
    mqtt: {
      generalise_subs: ["factory1/**", "factory2/**"],
    }
  }
}
```

See the [zenoh discovery blog post](https://zenoh.io/blog/2021-03-23-discovery/#leveraging-resource-generalisation) for details on when this is valuable.

---

### `generalise_pubs`

**Type:** array of zenoh key expressions
**Default:** `[]` (empty)
**CLI:** `-w, --generalise-pub` (repeatable)

Same concept as `generalise_subs` but for publications. Aggregates publication declarations to minimize discovery traffic.

```json5
{
  plugins: {
    mqtt: {
      generalise_pubs: ["factory1/**"],
    }
  }
}
```

> **Note:** The `DEFAULT_CONFIG.json5` file has a copy-paste error where both entries are labeled `generalise_subs`. The correct field names are `generalise_subs` and `generalise_pubs` as shown above.

---

### `tx_channel_size`

**Type:** unsigned integer
**Default:** `65536`
**CLI:** `--tx-channel-size`

Size of the internal channel that buffers Zenoh messages waiting to be sent to MQTT clients. If the channel fills up (e.g., a slow MQTT client), new messages from Zenoh are dropped until space becomes available.

```json5
{
  plugins: {
    mqtt: {
      tx_channel_size: 65536,
    }
  }
}
```

Increase this if you observe dropped messages with fast zenoh publishers and slower MQTT consumers. Decrease it to reduce memory usage and latency (at the cost of dropping messages sooner when clients are slow).

---

### `tls`

**Type:** object
**Default:** unset (plain MQTT, no TLS)

Enables MQTTS (MQTT over TLS). When this section is present, TLS is active. Two modes:

#### Server-side authentication (clients validate server)

```json5
{
  plugins: {
    mqtt: {
      tls: {
        server_private_key: "/path/to/private-key.pem",
        server_certificate: "/path/to/certificate.pem",
      }
    }
  }
}
```

#### Mutual TLS (mTLS — both sides validate)

```json5
{
  plugins: {
    mqtt: {
      tls: {
        server_private_key: "/path/to/private-key.pem",
        server_certificate: "/path/to/certificate.pem",
        root_ca_certificate: "/path/to/root-ca.pem",
      }
    }
  }
}
```

#### TLS fields

| Field | Type | Description |
|-------|------|-------------|
| `server_private_key` | string (path) | PEM file path for the server's private key |
| `server_private_key_base64` | string (base64) | Base64-encoded private key (alternative to file path) |
| `server_certificate` | string (path) | PEM file path for the server's certificate |
| `server_certificate_base64` | string (base64) | Base64-encoded certificate |
| `root_ca_certificate` | string (path) | CA cert for validating MQTT clients (enables mTLS) |
| `root_ca_certificate_base64` | string (base64) | Base64-encoded CA cert |

You must provide exactly one of the file or base64 form for each field — providing both is an error.

The TLS implementation uses rustls and accepts PKCS1, PKCS8, and SEC1 key formats.

CLI equivalents for the standalone bridge:
- `--server-private-key <FILE>`
- `--server-certificate <FILE>`
- `--root-ca-certificate <FILE>`

---

### `auth`

**Type:** object
**Default:** unset (no authentication, all clients accepted)

Enables username/password authentication for MQTT clients.

```json5
{
  plugins: {
    mqtt: {
      auth: {
        dictionary_file: "/etc/zenoh/mqtt-users.txt",
      }
    }
  }
}
```

The dictionary file format is one entry per line:
```
username1:password1
username2:password2
```

**Security note:** Credentials are transmitted in plaintext in the MQTT `CONNECT` packet. Always use `auth` in combination with `tls` to prevent credential interception.

CLI: `--dictionary-file <FILE>`

---

### `work_thread_num`

**Type:** unsigned integer
**Default:** `2`
**Applies to:** plugin mode only (no effect on standalone bridge)

Number of worker threads in the Tokio async runtime used by the plugin. Worker threads handle non-blocking tasks.

```json5
{ plugins: { mqtt: { work_thread_num: 2 } } }
```

---

### `max_block_thread_num`

**Type:** unsigned integer
**Default:** `50`
**Applies to:** plugin mode only

Maximum number of blocking threads for I/O-bound tasks. These threads are spawned on demand.

```json5
{ plugins: { mqtt: { max_block_thread_num: 50 } } }
```

When running as a standalone bridge, thread management is controlled via the `ZENOH_RUNTIME` environment variable.

---

## Topic Scoping and Multi-Site Isolation

### The Collision Problem

Consider two factories, each with MQTT sensors publishing on `sensors/temperature`. If both are bridged to the same Zenoh network without scoping, their data merges — subscribers see a mix of data from both sites with no way to distinguish them.

### The Solution: Per-Site Scopes

Each bridge instance is configured with a distinct `scope`. The scope becomes a Zenoh key expression prefix, namespacing all traffic from that site:

**Factory 1 config:**
```json5
{ plugins: { mqtt: { scope: "factory1", port: "0.0.0.0:1883" } } }
```

**Factory 2 config:**
```json5
{ plugins: { mqtt: { scope: "factory2", port: "0.0.0.0:1883" } } }
```

Result on the Zenoh network:
- Factory 1's `sensors/temperature` → `factory1/sensors/temperature`
- Factory 2's `sensors/temperature` → `factory2/sensors/temperature`

A central monitoring app can subscribe to `factory1/sensors/**` for site-specific data, or `*/sensors/temperature` to get all sites' temperature readings.

### Complete Multi-Site Example

```
Site A: MQTT sensors → [zenoh-bridge-mqtt, scope=site-a] → Zenoh network
Site B: MQTT sensors → [zenoh-bridge-mqtt, scope=site-b] → Zenoh network
                                                                ↓
                                              [Central zenohd with InfluxDB storage]
                                              Subscribes to **/sensors/**
```

A Zenoh subscriber can:
- Subscribe to `site-a/sensors/**` — site A only
- Subscribe to `site-b/sensors/**` — site B only
- Subscribe to `*/sensors/temperature` — all sites, temperature only

---

## Allow/Deny Filtering

### Logic

The `allow` and `deny` regexes are applied to the raw MQTT topic (before scope is prepended). The decision matrix:

| `allow` set | `deny` set | Result |
|-------------|------------|--------|
| No | No | All topics routed over zenoh |
| Yes | No | Only `allow`-matching topics routed over zenoh |
| No | Yes | All topics except `deny`-matching routed over zenoh |
| Yes | Yes | Topics matching `allow` AND NOT matching `deny` are routed |

**What happens to blocked topics?** They are not dropped — they still work between MQTT clients connected to the same bridge instance (local pub/sub). They are simply not propagated across the Zenoh network. This enables patterns like "local MQTT control plane + remote sensor data."

### Pattern Examples

Route only sensor data, block everything else:
```json5
{ allow: "^sensors/" }
```

Block internal/debug topics:
```json5
{ deny: "^internal/|^debug/|^$SYS/" }
```

Allow sensors, but not debug sensors:
```json5
{
  allow: "^sensors/",
  deny: "^sensors/debug/"
}
```

Filter by device namespace:
```json5
{ allow: "^device/[a-f0-9]{8}/" }
```

---

## QoS Mapping

### MQTT → Zenoh (inbound)

All MQTT publications, regardless of QoS level, are translated to Zenoh `put` operations. Zenoh's pub/sub layer uses its own reliability model:

| MQTT QoS | Zenoh equivalent |
|----------|-----------------|
| QoS 0 (At Most Once) | Zenoh `put` (best-effort on the zenoh layer) |
| QoS 1 (At Least Once) | Zenoh `put` (Zenoh's transport handles reliability) |
| QoS 2 (Exactly Once) | Zenoh `put` (at the application level, treated same as QoS 1) |

Zenoh transports (unicast TCP, TLS, etc.) provide their own reliability guarantees independent of MQTT QoS.

### Zenoh → MQTT (outbound)

All messages delivered to MQTT clients use `send_at_most_once` (QoS 0). This is a current implementation constraint — the plugin does not attempt to map Zenoh reliability semantics back to MQTT QoS 1 or 2.

```rust
// From mqtt_helpers.rs:
sink.publish(topic, payload).send_at_most_once()
```

**Practical implications:**
- If an MQTT client subscribes at QoS 1 or 2, the broker (this plugin) may confirm the subscription at QoS 0 (downgraded)
- Applications requiring guaranteed delivery from zenoh to MQTT should handle retries at the application layer or use Zenoh storage/replay

### Retained Messages

Zenoh does not have a native retained message concept. MQTT retained messages are not specially handled — they are published as regular Zenoh puts. To achieve retained-message semantics, configure a Zenoh storage (e.g., RocksDB or InfluxDB) that subscribes to the relevant key expressions. New MQTT subscribers can then query the storage to get the last value.

---

## Operating Modes

### Mode 1: Plugin Within zenohd

The plugin runs inside the Zenoh router as a dynamic library. It shares the router's session and benefits from the router's routing infrastructure.

Install the plugin library where `zenohd` can find it, then configure:

```json5
// zenohd-config.json5
{
  plugins_search_dirs: ["/usr/lib"],
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
      scope: "mysite",
    }
  }
}
```

Run: `zenohd -c zenohd-config.json5`

The plugin is automatically loaded at startup. Use `--rest-http-port 8000` to enable the REST API for admin space queries.

### Mode 2: Standalone Bridge

`zenoh-bridge-mqtt` runs as an independent process that acts as both an MQTT broker and a Zenoh peer or client.

```bash
# As a zenoh peer (discovers other peers automatically)
zenoh-bridge-mqtt --scope factory1 --port 1883

# As a zenoh client connecting to a specific router
zenoh-bridge-mqtt \
  --mode client \
  --peer tcp/zenoh-router.local:7447 \
  --scope factory1 \
  --port 1883
```

The standalone bridge mode is typically preferred for edge deployments where a full zenoh router is not needed or when connecting a remote site's MQTT system to a central Zenoh network.

---

## Complete Configuration Examples

### Example 1: Basic MQTT Broker for Factory Sensors

Simple setup where Zenoh acts as the MQTT broker for a factory's IoT sensors.

```json5
// factory-bridge.json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
      scope: "factory1",
      // Only route sensor and actuator topics
      allow: "^sensors/|^actuators/|^alarms/",
      // Block raw device debug output
      deny: "^sensors/debug/|^actuators/debug/",
      tx_channel_size: 65536,
    }
  },
  mode: "peer",
  connect: {
    endpoints: ["tcp/zenoh-router.local:7447"]
  }
}
```

Start:
```bash
zenoh-bridge-mqtt -c factory-bridge.json5
```

MQTT clients connect to `mqtt://this-host:1883`. Python zenoh subscriber:

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    # Subscribe to all factory1 sensor data
    sub = session.declare_subscriber("factory1/sensors/**")
    for sample in sub.receiver():
        topic = sample.key_expr
        value = bytes(sample.payload).decode()
        print(f"{topic}: {value}")
```

### Example 2: Secure MQTT Broker with mTLS and Authentication

Production deployment with mutual TLS and username/password authentication.

```json5
// secure-bridge.json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:8883",
      scope: "prod",
      tls: {
        server_private_key: "/etc/certs/broker-key.pem",
        server_certificate: "/etc/certs/broker-cert.pem",
        // Adding root_ca_certificate enables mTLS
        root_ca_certificate: "/etc/certs/client-ca.pem",
      },
      auth: {
        // Each line: username:password
        dictionary_file: "/etc/zenoh/mqtt-users.txt",
      },
      allow: "^devices/|^telemetry/",
    }
  },
  mode: "client",
  connect: {
    endpoints: ["tls/zenoh-cloud.example.com:7447"]
  }
}
```

### Example 3: Multi-Site MQTT Bridge with Scoping

Two factory sites bridged to a central Zenoh network, both using the same topic structure.

**Site A bridge** (`site-a.json5`):
```json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
      scope: "site-a",
      generalise_subs: ["site-a/**"],
      generalise_pubs: ["site-a/**"],
    }
  },
  mode: "client",
  connect: {
    endpoints: ["tcp/central-zenoh.example.com:7447"]
  }
}
```

**Site B bridge** (`site-b.json5`):
```json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
      scope: "site-b",
      generalise_subs: ["site-b/**"],
      generalise_pubs: ["site-b/**"],
    }
  },
  mode: "client",
  connect: {
    endpoints: ["tcp/central-zenoh.example.com:7447"]
  }
}
```

Central monitoring app (Python):
```python
import zenoh

config = zenoh.Config()
config.insert_json5("connect/endpoints", '["tcp/central-zenoh.example.com:7447"]')

with zenoh.open(config) as session:
    # Monitor temperature from all sites
    sub_all = session.declare_subscriber("*/sensors/temperature")

    # Monitor only site-a
    sub_a = session.declare_subscriber("site-a/**")

    # Publish setpoint back to site-b actuators
    # This will appear as MQTT topic "actuators/setpoint" on site-b
    pub = session.declare_publisher("site-b/actuators/setpoint")
    pub.put(b"22.5")
```

### Example 4: MQTT with Allow/Deny Filtering

Route only production sensor data, block all system and test topics.

```json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
      scope: "production",
      // Allow sensor, actuator, and alert namespaces
      allow: "^(sensors|actuators|alerts)/",
      // But never route test channels or $SYS broker stats
      deny: "^(sensors|actuators)/test/|^\\$SYS/",
      tx_channel_size: 32768,
    }
  },
  mode: "peer"
}
```

With this config:
- `sensors/line1/temp` → routed (matches allow, not deny)
- `sensors/test/bench` → NOT routed (matches deny)
- `alerts/critical` → routed
- `$SYS/broker/clients` → NOT routed (matches deny)
- `maintenance/status` → NOT routed (doesn't match allow)

---

## Admin Space

The bridge exposes a queryable admin space at `@/<uuid>/mqtt/`. Available endpoints:

| Key Expression | Content |
|---------------|---------|
| `@/<uuid>/mqtt/version` | Plugin version string |
| `@/<uuid>/mqtt/config` | Current running configuration (JSON) |

Query via the REST API:
```bash
# Start bridge with REST API enabled
zenoh-bridge-mqtt --rest-http-port 8080 --scope factory1

# Query all admin info
curl http://localhost:8080/@/** | jq .

# Query config specifically
curl "http://localhost:8080/@/**/mqtt/config" | jq .
```

Or via the zenoh Python API:
```python
import zenoh

with zenoh.open() as session:
    replies = session.get("@/**/mqtt/config")
    for reply in replies.receiver():
        import json
        config = json.loads(bytes(reply.ok.payload))
        print(json.dumps(config, indent=2))
```

---

## Installation

### Debian/Ubuntu

```bash
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" \
  | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt update

# Plugin for zenohd
sudo apt install zenoh-plugin-mqtt

# Or standalone bridge
sudo apt install zenoh-bridge-mqtt
```

### Docker

```bash
# Pull and run the bridge
docker pull eclipse/zenoh-bridge-mqtt:latest

# Basic run (binds MQTT on 1883, zenoh in peer mode)
docker run --init -p 1883:1883 eclipse/zenoh-bridge-mqtt

# With custom config
docker run --init \
  -p 1883:1883 \
  -v /path/to/config.json5:/config.json5 \
  eclipse/zenoh-bridge-mqtt -c /config.json5
```

### Manual / Build from Source

```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Clone and build
git clone https://github.com/eclipse-zenoh/zenoh-plugin-mqtt.git
cd zenoh-plugin-mqtt
cargo build --release

# Binaries in target/release/
# - zenoh-bridge-mqtt (standalone executable)
# - libzenoh_plugin_mqtt.so (Linux) / .dylib (macOS) / .dll (Windows)
```

> **ABI compatibility warning:** The plugin library must be built with the same Rust version and zenoh dependency version as `zenohd`. Mismatches cause `SIGSEGV` crashes at load time.

---

## Use Cases

| Scenario | Config pattern |
|----------|---------------|
| Connect legacy MQTT devices to Zenoh network | Default broker mode, `mode: "client"`, `connect` to zenoh router |
| Multiple MQTT sites with overlapping topics | Per-site `scope` prefix |
| Store MQTT data in InfluxDB/RocksDB | Use zenoh storage plugin on the router side, subscribing to `scope/**` |
| MQTT record/replay | Zenoh InfluxDB storage + queryable (replay via `get()`) |
| REST API access to MQTT data | `--rest-http-port` on zenohd, query by zenoh KE |
| MQTT-ROS2 bridge | Combine with zenoh ROS2 plugin on the same router |
| Cloud IoT connectivity | Standalone bridge in `client` mode connecting to cloud zenoh endpoint |
| Reduce zenoh discovery traffic | `generalise_subs` and `generalise_pubs` with broad KE patterns |

## See Also

- [Plugin Storage Manager Guide](plugin-storage-manager-guide.md) — use storage backends alongside MQTT to implement retained message semantics
- [Config Connect Listen](config-connect-listen.md) — how to connect the MQTT bridge to a Zenoh router
- [Key Expressions Guide](key-expressions-guide.md) — how MQTT topic wildcards map to Zenoh key expressions
