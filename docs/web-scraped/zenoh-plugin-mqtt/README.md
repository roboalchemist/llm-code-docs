# Zenoh MQTT Plugin

## Overview

The Zenoh MQTT Plugin is a bridge that enables seamless integration between MQTT and the Zenoh pub/sub system. It acts as an MQTT broker, accepting connections from MQTT clients (V3 and V5) and translating MQTT pub/sub operations into Zenoh pub/sub operations. This allows MQTT systems to leverage Zenoh's distributed routing infrastructure and capabilities.

**Key Repository**: [eclipse-zenoh/zenoh-plugin-mqtt](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt)

## What is Zenoh?

Zenoh (pronounced "zeno") is an open-source pub/sub, store/query, and compute framework that unifies data in motion, data at rest, and computations. It provides:

- Zero-overhead pub/sub messaging
- Geo-distributed storage and queries
- Efficient computation routing
- Time and space efficiency beyond mainstream stacks

For more information, visit [zenoh.io](http://zenoh.io) and the [roadmap](https://github.com/eclipse-zenoh/roadmap).

## How the Bridge Works

The Zenoh MQTT Plugin acts as a bridge between MQTT and Zenoh:

### Topic Mapping

- MQTT publications on topic `device/123/temperature` are routed as Zenoh publications on key expression `device/123/temperature`
- MQTT subscriptions on topic `device/#` are mapped to Zenoh subscriptions on key expression `device/**`
- MQTT wildcards (`+` and `#`) are mapped to Zenoh wildcards (`*` and `**`)

### Deployment Options

The plugin is available in two forms:

1. **Dynamic Plugin**: Loaded by the Zenoh router (`zenohd`) as a dynamic library
2. **Standalone Bridge** (`zenoh-bridge-mqtt`): Can act as a Zenoh client or peer

## Use Cases

- **IoT to Cloud**: Route MQTT data from devices to edge nodes and cloud infrastructure
- **Multi-System Bridging**: Connect two distinct MQTT systems across the internet with NAT traversal
- **REST Integration**: Pub/sub to MQTT via Zenoh's REST API
- **Robotics**: Enable MQTT-ROS2 communication
- **Data Storage**: Store MQTT publications in Zenoh storage backends (RocksDB, InfluxDB, filesystem)
- **Record/Replay**: Implement MQTT record/replay using InfluxDB as a storage backend

## Installation

### Manual Installation (All Platforms)

Download from the [Eclipse Zenoh download page](https://download.eclipse.org/zenoh/zenoh-plugin-mqtt/latest/):

1. Choose your platform (see [Rust platform support](https://doc.rust-lang.org/stable/rustc/platform-support.html))
2. For the plugin: Download `zenoh-plugin-mqtt-<version>-<platform>.zip` and extract in the same directory as `zenohd` or in `/usr/lib`
3. For the standalone bridge: Download `zenoh-bridge-mqtt-<version>-<platform>.zip` and extract anywhere

### Linux Debian

```bash
# Add Eclipse Zenoh repository
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt update

# Install plugin
sudo apt install zenoh-plugin-mqtt

# Or install the standalone bridge
sudo apt install zenoh-bridge-mqtt
```

### Docker

```bash
# Latest release
docker pull eclipse/zenoh-bridge-mqtt:latest

# Main branch (nightly)
docker pull eclipse/zenoh-bridge-mqtt:main

# Run with default settings
docker run --init -p 1883:1883 eclipse/zenoh-bridge-mqtt

# Run with custom arguments
docker run --init -p 1883:1883 eclipse/zenoh-bridge-mqtt \
  -c /path/to/config.json5 \
  --scope mqtt-edge
```

## Configuration

### Configuration File Format

Configure via JSON5 file (passed with `-c` argument) or command-line arguments. The `"mqtt"` section in the configuration can be used:
- In the Zenoh router config (within `"plugins"`)
- In the standalone bridge config

### Configuration Options

#### Basic MQTT Settings

- **`port`** (default: `"0.0.0.0:1883"`)
  - Bind address for the MQTT server
  - Format: `<ip>:<port>` or just `<port>` (uses `0.0.0.0`)

- **`scope`** (optional)
  - Prefix added to all MQTT topics when mapped to Zenoh key expressions
  - Use to avoid conflicts when bridging multiple distinct MQTT systems
  - Example: `mqtt-edge`, `home-1`

- **`allow`** (optional)
  - Regular expression matching MQTT topics to route via Zenoh
  - Default: All topics allowed
  - When both `allow` and `deny` are set, topics matching only `allow` are permitted

- **`deny`** (optional)
  - Regular expression matching MQTT topics to exclude from Zenoh routing
  - Default: No topics denied
  - When both `allow` and `deny` are set, topics matching only `allow` are permitted

#### Performance & Resource Settings

- **`tx_channel_size`** (default: `65536`)
  - Size of the transmit channel buffering messages from Zenoh to MQTT clients
  - If capacity is reached, new messages are dropped until space becomes available

- **`work_thread_num`** (default: `2`, plugin only)
  - Number of worker threads in the async runtime
  - No effect on standalone bridge

- **`max_block_thread_num`** (default: `50`, plugin only)
  - Maximum number of blocking threads in the async runtime
  - No effect on standalone bridge

#### Generalization (Discovery Optimization)

- **`generalise_subs`** (optional)
  - List of key expressions for generalizing Zenoh subscriptions
  - Minimizes discovery traffic
  - Example: `["device/**", "sensor/**"]`

- **`generalise_pubs`** (optional)
  - List of key expressions for generalizing Zenoh publications
  - Minimizes discovery traffic
  - Example: `["device/**", "sensor/**"]`

#### TLS/MQTTS Configuration

Only required for MQTTS support. Supports both server-side and mutual TLS (mTLS):

- **`server_private_key`** or **`server_private_key_base64`**
  - TLS private key (file path or base64-encoded string)
  - Required for MQTTS

- **`server_certificate`** or **`server_certificate_base64`**
  - TLS public certificate (file path or base64-encoded string)
  - Required for MQTTS

- **`root_ca_certificate`** or **`root_ca_certificate_base64`**
  - CA certificate for client validation (enables mTLS)
  - Optional; only required for mutual TLS

#### Authentication

- **`dictionary_file`** (optional)
  - Path to file with MQTT client credentials
  - Format: one credential per line as `username:password`
  - Credentials sent in cleartext; use MQTTS to encrypt on wire

### Configuration Examples

#### Basic Configuration (JSON5)

```json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
      scope: "mqtt-edge",
      allow: "home/.*",
    }
  }
}
```

#### Advanced Configuration with MQTTS

```json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
      scope: "iot-gateway",
      allow: "sensors/.*|devices/.*",
      generalise_subs: ["sensors/**", "devices/**"],
      generalise_pubs: ["sensors/**", "devices/**"],
      tx_channel_size: 131072,
      tls: {
        server_private_key: "/etc/mqtt/server-key.pem",
        server_certificate: "/etc/mqtt/server-cert.pem",
      }
    }
  }
}
```

#### Mutual TLS (mTLS) Configuration

```json5
{
  plugins: {
    mqtt: {
      port: "0.0.0.0:1883",
      tls: {
        server_private_key: "/etc/mqtt/server-key.pem",
        server_certificate: "/etc/mqtt/server-cert.pem",
        root_ca_certificate: "/etc/mqtt/ca-cert.pem"
      },
      auth: {
        dictionary_file: "/etc/mqtt/credentials.txt"
      }
    }
  }
}
```

## Command-Line Arguments

### Zenoh-related Arguments

- **`-c, --config <FILE>`** - Configuration file path
- **`-m, --mode <MODE>`** - Zenoh session mode: `peer` (default) or `client`
- **`-l, --listen <LOCATOR>`** - Locator for incoming sessions (repeatable)
  - Example: `tcp/localhost:7447`
- **`-e, --peer <LOCATOR>`** - Peer locator to connect to (repeatable)
  - Example: `tcp/192.168.1.100:7447`
- **`--no-multicast-scouting`** - Disable automatic Zenoh peer discovery
- **`-i, --id <hex_string>`** - Unique identifier as hex string
  - **WARNING**: Must be unique in the system; defaults to random UUIDv4
- **`--rest-http-port [PORT | IP:PORT]`** - HTTP interface for REST API
  - Disabled by default; setting this option enables it

### MQTT-related Arguments

- **`-p, --port [PORT | IP:PORT]`** - MQTT server bind address (default: `0.0.0.0:1883`)
- **`-s, --scope <String>`** - Prefix for MQTT topics mapped to Zenoh
- **`-a, --allow <String>`** - Regex matching allowed MQTT topics
- **`--deny <String>`** - Regex matching denied MQTT topics
- **`-w, --generalise-pub <String>`** - Generalize Zenoh publications (repeatable)
- **`-r, --generalise-sub <String>`** - Generalize Zenoh subscriptions (repeatable)
- **`--tx-channel-size <Unsigned Integer>`** - MQTT transmit channel size (default: 65536)
- **`--dictionary-file <FILE>`** - Path to MQTT credentials file
- **`--server-private-key <FILE>`** - TLS private key file
- **`--server-certificate <FILE>`** - TLS certificate file
- **`--root-ca-certificate <FILE>`** - Root CA certificate for mTLS

## Usage Examples

### Basic Standalone Bridge

Run with default settings (MQTT on port 1883):

```bash
zenoh-bridge-mqtt
```

### With Configuration File

```bash
zenoh-bridge-mqtt -c config.json5
```

### Client Mode Connecting to Zenoh Router

```bash
zenoh-bridge-mqtt -m client -e tcp/router-ip:7447
```

### Peer Mode with Custom Port and Scope

```bash
zenoh-bridge-mqtt -p 1883 -s mqtt-building-1 --listen tcp/0.0.0.0:7447
```

### Enable REST API

```bash
zenoh-bridge-mqtt --rest-http-port 8000
```

Then query via curl:

```bash
curl http://localhost:8000/@/service/**
curl http://localhost:8000/@/service/**/mqtt/version
curl http://localhost:8000/@/service/**/mqtt/config
```

Pipe into `jq` for pretty-printing:

```bash
curl http://localhost:8000/@/service/** | jq .
```

### With MQTTS and Authentication

```bash
zenoh-bridge-mqtt \
  -p 8883 \
  --server-private-key /etc/mqtt/server-key.pem \
  --server-certificate /etc/mqtt/server-cert.pem \
  --dictionary-file /etc/mqtt/users.txt
```

### With Topic Filtering

Allow only specific topics:

```bash
zenoh-bridge-mqtt --allow "home/sensor|home/actuator"
```

Deny specific topics:

```bash
zenoh-bridge-mqtt --deny "internal/.*|debug/.*"
```

### Docker Example with Configuration

```bash
docker run --init -p 1883:1883 \
  -v /path/to/config.json5:/config.json5 \
  eclipse/zenoh-bridge-mqtt -c /config.json5
```

## Administration Interface

The bridge exposes an administration space accessible via any Zenoh API, including REST.

### Admin Space Paths

Paths are prefixed with `@/service/<uuid>/mqtt` (where `<uuid>` is the bridge instance ID):

- **`@/service/<uuid>/mqtt/version`** - Bridge version
- **`@/service/<uuid>/mqtt/config`** - Bridge configuration

### Querying Admin Space

Via REST API (requires `--rest-http-port`):

```bash
# Query all admin spaces
curl http://localhost:8000/@/service/**

# Get bridge version
curl http://localhost:8000/@/service/**/mqtt/version

# Get bridge configuration
curl http://localhost:8000/@/service/**/mqtt/config | jq .
```

## Security Considerations

### Username/Password Authentication

- Credentials sent in MQTT `CONNECT` message in **cleartext**
- Can be viewed with network analysis tools (e.g., Wireshark)
- **Strongly recommended**: Use MQTTS to encrypt credentials on the wire

### TLS/MQTTS Best Practices

1. **Server-side authentication**: Clients validate server certificates
2. **Mutual TLS (mTLS)**: Both parties validate each other
3. Always use MQTTS when credentials are transmitted
4. Regularly rotate certificates and keys
5. Use strong cipher suites

## MQTT Version Support

- **MQTT V3** (3.1.1) - Fully supported
- **MQTT V5** - Fully supported

## Building from Source

### Prerequisites

Install [Rust](https://www.rust-lang.org/tools/install):

```bash
rustup update
```

### Build

```bash
git clone https://github.com/eclipse-zenoh/zenoh-plugin-mqtt.git
cd zenoh-plugin-mqtt
cargo build --release
```

### Output Artifacts

Located in `target/release/`:

- **`zenoh-bridge-mqtt`** - Standalone bridge executable
- **Plugin library** - `*.so` (Linux), `*.dylib` (macOS), `*.dll` (Windows)

### Build Compatibility Warning

The plugin must be built with the **same Rust version and Zenoh version** as `zenohd`. Mismatches can cause `SIGSEGV` crashes due to ABI incompatibilities.

## Environment Variables

### ZENOH_RUNTIME (Standalone Bridge)

Configure the async runtime. Options: `tokio`, `async-std`, etc. (see [zenoh-runtime docs](https://docs.rs/zenoh-runtime/latest/zenoh_runtime/enum.ZRuntime.html))

```bash
ZENOH_RUNTIME=tokio zenoh-bridge-mqtt
```

## Troubleshooting

### Plugin Won't Load

1. Verify Rust version matches `zenohd`: `rustc --version`
2. Check Zenoh version in plugin `Cargo.toml` matches `zenohd`
3. Ensure plugin file is in correct location (`LD_LIBRARY_PATH` on Linux)

### MQTT Clients Can't Connect

1. Check firewall allows port 1883 (or custom port)
2. Verify bridge is running: `netstat -tlnp | grep 1883`
3. Check logs for binding errors
4. Ensure no other service is using the port

### Topic Not Routing to Zenoh

1. Check `allow`/`deny` regex patterns match topic
2. Verify bridge scope prefix (if configured)
3. Use REST API to inspect admin space
4. Enable debug logging

### High Memory Usage

1. Reduce `tx_channel_size` if not buffering many messages
2. Reduce `work_thread_num` and `max_block_thread_num`
3. Monitor with `--rest-http-port` and query metrics

## Related Resources

- **Official Website**: [zenoh.io](http://zenoh.io)
- **Roadmap & Discussion**: [github.com/eclipse-zenoh/roadmap](https://github.com/eclipse-zenoh/roadmap)
- **Discord Community**: [Discord Server](https://discord.gg/2GJ958VuHs)
- **Documentation**: [docs.zenoh.io](https://docs.zenoh.io/)
- **Main Repository**: [github.com/eclipse-zenoh/zenoh](https://github.com/eclipse-zenoh/zenoh)
- **License**: EPL 2.0 and Apache 2.0

---

**Documentation Source**: [eclipse-zenoh/zenoh-plugin-mqtt](https://github.com/eclipse-zenoh/zenoh-plugin-mqtt)
**Last Updated**: 2026-02-06
