# Zenoh Transport Layer: Complete Guide

## Overview

Zenoh's transport layer is modular — each transport is implemented as a separate link plugin. All transports share the same Zenoh protocol framing; only the underlying carrier changes. The endpoint format follows a consistent pattern:

```
protocol/address:port[?config_key=value&...]
```

Transport selection happens at configuration time. Multiple transports can be active simultaneously, each handling a different class of peer or network segment.

---

## Table of Contents

1. [TCP](#1-tcp)
2. [UDP Unicast](#2-udp-unicast)
3. [UDP Multicast](#3-udp-multicast)
4. [TLS](#4-tls)
5. [QUIC (Stream)](#5-quic-stream)
6. [QUIC Datagram](#6-quic-datagram)
7. [WebSocket](#7-websocket)
8. [Serial](#8-serial)
9. [Shared Memory](#9-shared-memory)
10. [Link-Level Configuration](#10-link-level-configuration)
11. [TX Queue and Congestion Control](#11-tx-queue-and-congestion-control)
12. [Multiple Transports Simultaneously](#12-multiple-transports-simultaneously)
13. [Transport Selection Priority](#13-transport-selection-priority)

---

## 1. TCP

### Endpoint Format

```
tcp/<host>:<port>
tcp/0.0.0.0:7447          # listen on all interfaces
tcp/192.168.1.10:7447     # listen on specific interface
tcp/router.example.com:7447  # connect by hostname
tcp/[::1]:7447            # IPv6 loopback
```

### Use Cases

- **Default transport for all Zenoh deployments.** If you do not specify a transport, Zenoh uses TCP.
- Reliable, ordered delivery required (e.g., telemetry pipelines, command-and-control).
- Long-lived persistent connections between routers, clients, and peers.
- WAN links where packet loss must be handled by the transport.
- Firewall-friendly: single TCP connection, predictable port usage.

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | ✅ Yes |
| Ordered | ✅ Yes |
| Streamed | ✅ Yes (byte-stream) |
| Multicast | ❌ No |
| MTU | Up to 65535 bytes (BatchSize::MAX) |
| Effective batch size | Negotiated from TCP MSS |

TCP is a byte-stream transport. Zenoh uses 2-byte length framing on top of it, so the practical batch limit is 65535 bytes. On Linux/Unix, the MTU is further refined against the TCP MSS: Zenoh reads the socket's MSS via `socket2`, then computes the largest multiple of MSS/2 that fits below the default MTU. This minimises per-message overhead.

TCP enables `TCP_NODELAY` (disabling Nagle's algorithm) and sets `SO_LINGER` to 10 seconds by default.

### Configuration Options

TCP has both global config (applied via the `zenoh.json5` config file) and per-endpoint config (appended as query parameters to the endpoint URI).

#### Global config (`transport.link.tcp`)

```json5
{
  "transport": {
    "link": {
      "tcp": {
        "so_rcvbuf": 1048576,   // OS RX socket buffer (bytes)
        "so_sndbuf": 1048576    // OS TX socket buffer (bytes)
      }
    }
  }
}
```

#### Per-endpoint config (query parameters)

| Parameter | Description | Example |
|---|---|---|
| `so_rcvbuf` | OS RX buffer size (bytes) | `so_rcvbuf=1048576` |
| `so_sndbuf` | OS TX buffer size (bytes) | `so_sndbuf=1048576` |
| `iface` | Bind to specific network interface | `iface=eth0` |
| `bind` | Bind to specific local socket address | `bind=192.168.1.5:0` |
| `dscp` | DSCP/QoS byte for the socket | `dscp=46` |

> **Note:** `iface` and `bind` are mutually exclusive. Using both will produce an error.

### Example Configurations

#### Listener (router or peer accepting connections)

```json5
// zenoh-router.json5
{
  "listen": {
    "endpoints": [
      "tcp/0.0.0.0:7447"
    ]
  },
  "transport": {
    "link": {
      "tcp": {
        "so_rcvbuf": 2097152,
        "so_sndbuf": 2097152
      }
    }
  }
}
```

#### Connector (client or peer initiating connections)

```json5
{
  "connect": {
    "endpoints": [
      "tcp/192.168.1.10:7447?so_rcvbuf=524288&so_sndbuf=524288"
    ]
  }
}
```

#### Bind to specific interface

```json5
{
  "connect": {
    "endpoints": [
      "tcp/192.168.1.10:7447?iface=eth1"
    ]
  }
}
```

---

## 2. UDP Unicast

### Endpoint Format

```
udp/<host>:<port>
udp/0.0.0.0:7447
udp/192.168.1.10:7447
udp/[::]:7447
```

### Use Cases

- Lower latency than TCP for small, infrequent messages where head-of-line blocking matters.
- Best-effort telemetry where occasional loss is acceptable (sensor readings, LIDAR point clouds).
- Environments where TCP connection setup overhead is a concern.
- Pairing with Zenoh's own reliability/fragmentation layer when needed.

> **When to prefer TCP instead:** Use TCP when you need guaranteed delivery, when messages are large and need fragmentation, or when the network is lossy.

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | ❌ No (unreliable by default) |
| Ordered | ❌ No |
| Streamed | ❌ No (datagram) |
| Multicast | ❌ No (unicast variant) |
| MTU (Linux/Windows) | 65527 bytes (u16::MAX − 8 − 40) |
| MTU (macOS) | 9216 bytes |
| MTU (other) | 8192 bytes |

Because UDP is datagram-based, each Zenoh batch must fit in a single UDP datagram. This makes the effective MTU platform-dependent and significantly smaller than TCP's 65535 cap.

### Configuration Options

| Parameter | Description |
|---|---|
| `iface` | Bind to specific network interface |
| `bind` | Bind to specific local socket address |
| `dscp` | DSCP/QoS byte |
| `so_rcvbuf` | OS RX socket buffer |
| `so_sndbuf` | OS TX socket buffer |

Global config:

```json5
{
  "transport": {
    "link": {
      "udp": {
        "so_rcvbuf": 2097152,
        "so_sndbuf": 2097152
      }
    }
  }
}
```

### Example Configurations

#### UDP Listener

```json5
{
  "listen": {
    "endpoints": [
      "udp/0.0.0.0:7447"
    ]
  }
}
```

#### UDP Connector

```json5
{
  "connect": {
    "endpoints": [
      "udp/192.168.1.10:7447"
    ]
  }
}
```

#### Mixed TCP + UDP (accept either)

```json5
{
  "listen": {
    "endpoints": [
      "tcp/0.0.0.0:7447",
      "udp/0.0.0.0:7447"
    ]
  }
}
```

---

## 3. UDP Multicast

### Endpoint Format

```
udp/<multicast-group>:<port>
udp/224.0.0.224:7447           # IPv4 multicast group
udp/[ff02::1]:7447             # IPv6 link-local multicast
```

Multicast addresses:
- IPv4 range: `224.0.0.0` – `239.255.255.255`
- IPv6 range: `ff00::/8`

### Use Cases

- **Scouting**: discovering peers on the local network without pre-configured addresses. This is Zenoh's primary use of multicast.
- One-to-many data distribution (e.g., broadcast sensor data to all subscribers on a LAN).
- Robot swarms or peer discovery in embedded/IoT deployments.
- Local network segments (multicast does not cross routers by default without PIM/IGMP).

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | ❌ No |
| Ordered | ❌ No |
| Streamed | ❌ No (datagram) |
| Multicast | ✅ Yes |
| MTU | Same as UDP unicast (platform-dependent) |

Multicast delivery is inherently best-effort. If reliability is required, use multicast only for discovery and fall back to unicast TCP/UDP for data.

### Scouting Configuration

Zenoh uses multicast scouting automatically. The scouting address and period are configured separately from data links:

```json5
{
  "scouting": {
    "multicast": {
      "enabled": true,
      "listen": true,
      "address": "224.0.0.224:7446",   // default scouting group
      "interface": "auto",             // or "eth0", "lo", etc.
      "autoconnect": {
        "router": "peer|router",
        "peer": "router|peer"
      },
      "delay": 200                     // ms before declaring scouting done
    },
    "gossip": {
      "enabled": true,
      "multihop": false,
      "autoconnect": {
        "router": "peer|router",
        "peer": "router|peer"
      }
    }
  }
}
```

### Example Configurations

#### Multicast Listener (for data, not just scouting)

```json5
{
  "listen": {
    "endpoints": [
      "udp/224.0.0.224:7447"
    ]
  }
}
```

#### Disable Multicast Scouting (fixed topology)

```json5
{
  "scouting": {
    "multicast": {
      "enabled": false
    }
  },
  "connect": {
    "endpoints": [
      "tcp/192.168.1.10:7447"
    ]
  }
}
```

#### Multicast on Specific Interface

```json5
{
  "scouting": {
    "multicast": {
      "enabled": true,
      "interface": "eth0",
      "address": "224.0.0.224:7446"
    }
  }
}
```

---

## 4. TLS

### Endpoint Format

```
tls/<host>:<port>
tls/0.0.0.0:7447
tls/router.example.com:7447
tls/192.168.1.10:7447
```

### Use Cases

- Secure communication over untrusted networks (WAN, cloud, internet).
- Authentication of peers via X.509 certificates.
- Mutual TLS (mTLS) for zero-trust environments where both sides must present certificates.
- Regulatory compliance requiring encryption in transit.
- Any scenario where TCP is appropriate but confidentiality is also required.

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | ✅ Yes |
| Ordered | ✅ Yes |
| Streamed | ✅ Yes |
| Multicast | ❌ No |
| MTU | Up to 65535 bytes |
| Overhead | TLS record overhead (~13–53 bytes/record) + handshake latency |

TLS uses TLS 1.3 exclusively (via `rustls`). The first connection incurs a 1-RTT handshake. Session resumption can reduce this in future connections. The MTU computation mirrors TCP (MSS-based on Unix).

### Certificate Setup

Zenoh's TLS uses PEM-format certificates. You can supply them as:
1. **File paths** (`*_file` keys) — read from disk at startup
2. **Inline Base64** (`*_base64` keys) — embedded in config, decoded at runtime
3. **Raw PEM string** (`*_raw` keys) — inline PEM text

All three forms are equivalent; choose based on your deployment model.

#### Generate a Self-Signed CA and Certificates (example with openssl)

```bash
# Generate CA
openssl req -x509 -newkey rsa:4096 -keyout ca.key -out ca.pem \
  -days 365 -nodes -subj "/CN=ZenohCA"

# Generate server key and CSR
openssl req -newkey rsa:4096 -keyout server.key -out server.csr \
  -nodes -subj "/CN=zenoh-router"

# Sign server certificate with CA
openssl x509 -req -in server.csr -CA ca.pem -CAkey ca.key \
  -CAcreateserial -out server.pem -days 365

# Generate client key and cert (for mTLS)
openssl req -newkey rsa:4096 -keyout client.key -out client.csr \
  -nodes -subj "/CN=zenoh-client"
openssl x509 -req -in client.csr -CA ca.pem -CAkey ca.key \
  -CAcreateserial -out client.pem -days 365
```

### Configuration Options

#### Server-side (listener) TLS config keys

| Key | Description |
|---|---|
| `tls_listen_certificate_file` | Path to server PEM certificate |
| `tls_listen_private_key_file` | Path to server PEM private key |
| `tls_listen_certificate_base64` | Base64-encoded server certificate |
| `tls_listen_private_key_base64` | Base64-encoded server private key |
| `tls_root_ca_certificate_file` | CA cert for verifying clients (mTLS) |
| `tls_root_ca_certificate_base64` | Base64-encoded CA cert |
| `tls_enable_mtls` | `true` to require client certificates |
| `tls_close_link_on_expiration` | Close link when certificate expires |

#### Client-side (connector) TLS config keys

| Key | Description |
|---|---|
| `tls_root_ca_certificate_file` | CA cert to trust the server |
| `tls_root_ca_certificate_base64` | Base64-encoded CA cert |
| `tls_connect_certificate_file` | Client cert (for mTLS) |
| `tls_connect_private_key_file` | Client private key (for mTLS) |
| `tls_connect_certificate_base64` | Base64-encoded client cert |
| `tls_connect_private_key_base64` | Base64-encoded client private key |
| `tls_enable_mtls` | `true` to send client certificate |
| `tls_verify_name_on_connect` | `true` (default) to verify server hostname |
| `tls_close_link_on_expiration` | Close link when certificate expires |

### Example Configurations

#### Server (TLS, one-way authentication)

```json5
// router.json5
{
  "listen": {
    "endpoints": [
      "tls/0.0.0.0:7447"
    ]
  },
  "transport": {
    "link": {
      "tls": {
        "listen_private_key": "/etc/zenoh/certs/server.key",
        "listen_certificate": "/etc/zenoh/certs/server.pem",
        "root_ca_certificate": "/etc/zenoh/certs/ca.pem"
      }
    }
  }
}
```

#### Client (TLS, one-way)

```json5
{
  "connect": {
    "endpoints": [
      "tls/router.example.com:7447"
    ]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/etc/zenoh/certs/ca.pem"
      }
    }
  }
}
```

#### Mutual TLS (mTLS)

```json5
// router.json5
{
  "listen": {
    "endpoints": ["tls/0.0.0.0:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "listen_certificate": "/certs/server.pem",
        "listen_private_key": "/certs/server.key",
        "root_ca_certificate": "/certs/ca.pem",
        "enable_mtls": true
      }
    }
  }
}

// client.json5
{
  "connect": {
    "endpoints": ["tls/router.example.com:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/certs/ca.pem",
        "connect_certificate": "/certs/client.pem",
        "connect_private_key": "/certs/client.key",
        "enable_mtls": true,
        "verify_name_on_connect": true
      }
    }
  }
}
```

#### Per-endpoint TLS (inline in endpoint URI)

```json5
{
  "connect": {
    "endpoints": [
      "tls/router.example.com:7447?tls_root_ca_certificate_file=/certs/ca.pem&tls_enable_mtls=false"
    ]
  }
}
```

#### Certificate expiration monitoring

```json5
{
  "transport": {
    "link": {
      "tls": {
        "close_link_on_expiration": true
      }
    }
  }
}
```

When enabled, Zenoh monitors the earliest `not_after` date in the peer's certificate chain and proactively closes the link as it approaches expiry, triggering reconnection with fresh certificates.

---

## 5. QUIC (Stream)

### Endpoint Format

```
quic/<host>:<port>
quic/0.0.0.0:7447
quic/router.example.com:7447
```

### Use Cases

- **Low-latency encrypted connections** where TLS over TCP adds too much handshake latency. QUIC performs a 1-RTT (or 0-RTT) handshake.
- Environments with packet loss or reordering (QUIC avoids TCP's head-of-line blocking at the transport level).
- Mobile or roaming clients where the underlying IP address changes (QUIC connection migration).
- When you need both encryption and UDP-based multiplexing.
- Replacing TLS in environments where TCP itself is a bottleneck.

> **QUIC vs TLS over TCP:** QUIC is preferred when connection establishment speed matters, the network is lossy, or clients are mobile. TLS/TCP is simpler to operate and debug.

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | ✅ Yes |
| Ordered | ✅ Yes (within a stream) |
| Streamed | ✅ Yes |
| Multicast | ❌ No |
| MTU | Up to 65535 bytes (BatchSize::MAX) |
| Encryption | ✅ Always (TLS 1.3 mandatory) |
| Linger timeout | 10 seconds |
| Accept throttle | 100 ms on error |

QUIC uses a single bidirectional QUIC stream per Zenoh session. Unidirectional streams and additional bidirectional streams are disabled. QUIC requires certificates — it cannot run without TLS.

### Certificate Configuration

QUIC uses the same certificate keys as TLS:

| Key | Description |
|---|---|
| `tls_listen_certificate_file` | Server certificate |
| `tls_listen_private_key_file` | Server private key |
| `tls_root_ca_certificate_file` | CA certificate |
| `tls_enable_mtls` | Enable mutual authentication |
| `tls_verify_name_on_connect` | Verify server hostname |
| `tls_close_link_on_expiration` | Auto-close on cert expiry |
| `iface` | Bind to interface |
| `bind` | Bind to specific local address |
| `dscp` | DSCP marking |

### Example Configurations

#### QUIC Listener (router)

```json5
{
  "listen": {
    "endpoints": [
      "quic/0.0.0.0:7447"
    ]
  },
  "transport": {
    "link": {
      "tls": {
        "listen_certificate": "/certs/server.pem",
        "listen_private_key": "/certs/server.key",
        "root_ca_certificate": "/certs/ca.pem"
      }
    }
  }
}
```

#### QUIC Connector (client)

```json5
{
  "connect": {
    "endpoints": [
      "quic/router.example.com:7447"
    ]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/certs/ca.pem"
      }
    }
  }
}
```

#### QUIC with mTLS

```json5
// listener
{
  "listen": {
    "endpoints": ["quic/0.0.0.0:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "listen_certificate": "/certs/server.pem",
        "listen_private_key": "/certs/server.key",
        "root_ca_certificate": "/certs/ca.pem",
        "enable_mtls": true
      }
    }
  }
}

// connector
{
  "connect": {
    "endpoints": ["quic/router.example.com:7447"]
  },
  "transport": {
    "link": {
      "tls": {
        "root_ca_certificate": "/certs/ca.pem",
        "connect_certificate": "/certs/client.pem",
        "connect_private_key": "/certs/client.key",
        "enable_mtls": true
      }
    }
  }
}
```

#### Per-endpoint QUIC config

```json5
{
  "connect": {
    "endpoints": [
      "quic/router.example.com:7447?tls_root_ca_certificate_file=/certs/ca.pem&iface=eth0"
    ]
  }
}
```

---

## 6. QUIC Datagram

### Endpoint Format

```
quic/<host>:<port>?rel=0
```

The `rel=0` metadata tag in the locator marks this as the unreliable QUIC datagram variant (as opposed to the reliable QUIC stream variant above).

### Use Cases

- **Low-latency unreliable delivery with encryption.** Combines UDP-like datagram semantics with QUIC's mandatory TLS 1.3.
- Sensor data where staleness matters more than completeness.
- Real-time control loops tolerating occasional dropped messages.
- Environments requiring encryption but not ordering or reliability guarantees.

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | ❌ No |
| Ordered | ❌ No |
| Streamed | ❌ No (datagram) |
| Multicast | ❌ No |
| MTU | Dynamic (from `connection.max_datagram_size()`) |
| Encryption | ✅ Always (TLS 1.3) |

The MTU is negotiated dynamically by QUIC's MTU discovery mechanism. The server can configure an initial MTU and discovery interval:

| Config key | Description |
|---|---|
| `initial_mtu` | Starting MTU value (u16) |
| `mtu_discovery_interval_secs` | Seconds between MTU probes |

### Example Configuration

```json5
// listener
{
  "listen": {
    "endpoints": ["quic/0.0.0.0:7448"]
  },
  "transport": {
    "link": {
      "tls": {
        "listen_certificate": "/certs/server.pem",
        "listen_private_key": "/certs/server.key",
        "root_ca_certificate": "/certs/ca.pem"
      }
    }
  }
}
```

Per-endpoint MTU config (on the listener endpoint URI):

```
quic/0.0.0.0:7448?initial_mtu=1400&mtu_discovery_interval_secs=60
```

---

## 7. WebSocket

### Endpoint Format

```
ws://<host>:<port>
ws://0.0.0.0:7447
ws://router.example.com:7447
wss://router.example.com:7447    # WebSocket over TLS
```

### Use Cases

- **Browser-based Zenoh clients** using the zenoh-js or zenoh-ts libraries.
- Environments where only HTTP/WebSocket traffic is permitted through firewalls or proxies.
- Web applications subscribing to or publishing Zenoh topics directly.
- Cloud environments where WebSocket is the standard upgrade from HTTP.

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | ✅ Yes |
| Ordered | ✅ Yes |
| Streamed | ✅ Yes |
| Multicast | ❌ No |
| MTU | Up to 65535 bytes |
| Overhead | WebSocket framing (2–14 bytes/frame) + HTTP upgrade handshake |

WebSocket adds a one-time HTTP upgrade handshake and per-frame overhead compared to raw TCP, but this is negligible for most workloads.

### Example Configurations

#### WebSocket Listener

```json5
{
  "listen": {
    "endpoints": [
      "tcp/0.0.0.0:7447",
      "ws/0.0.0.0:7448"
    ]
  }
}
```

#### WebSocket Connector (from a server-side process)

```json5
{
  "connect": {
    "endpoints": [
      "ws/router.example.com:7448"
    ]
  }
}
```

#### Browser client (zenoh-js)

```javascript
import init, { Session, Config } from "@eclipse-zenoh/zenoh-ts";

await init();
const conf = new Config('ws/router.example.com:7448');
const session = await Session.open(conf);
```

#### WebSocket with TLS (wss)

```json5
{
  "listen": {
    "endpoints": [
      "tls/0.0.0.0:7447",
      "wss/0.0.0.0:7448"
    ]
  },
  "transport": {
    "link": {
      "tls": {
        "listen_certificate": "/certs/server.pem",
        "listen_private_key": "/certs/server.key"
      }
    }
  }
}
```

---

## 8. Serial

### Endpoint Format

```
serial/<device-path>[?baudrate=<rate>&exclusive=<bool>&tout=<us>]

# Linux/macOS
serial//dev/ttyUSB0
serial//dev/ttyUSB0?baudrate=115200&exclusive=true

# Windows
serial/COM3
serial/COM3?baudrate=9600&exclusive=true
```

### Use Cases

- **Embedded systems and microcontrollers** running zenoh-pico.
- UART links between MCUs and host systems.
- USB-serial adapters connecting constrained devices.
- Industrial sensors using RS-232/RS-485 serial interfaces.
- Scenarios where no IP networking is available.

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | ❌ No (best-effort) |
| Ordered | Depends on medium |
| Streamed | ❌ No (message-framed) |
| Multicast | ❌ No |
| MTU | `z_serial::MAX_MTU` (platform-defined) |
| Default baud rate | 9600 bps |
| Default timeout | 50,000 μs (50 ms) |

Serial is not streamed in the TCP sense — it uses message-level framing from the `z-serial` library. The link is unreliable (no retransmission at the serial transport level; Zenoh's session layer handles reliability if configured).

### Configuration Options

| Parameter | Default | Description |
|---|---|---|
| `baudrate` | `9600` | Serial baud rate (e.g., 9600, 115200, 921600) |
| `exclusive` | `true` | Exclusive port access |
| `tout` | `50000` | Read timeout in microseconds |
| `release_on_close` | `true` | Release port when link closes |

### Example Configurations

#### Serial Listener (embedded device acting as server)

```json5
{
  "listen": {
    "endpoints": [
      "serial//dev/ttyUSB0?baudrate=115200&exclusive=true"
    ]
  }
}
```

#### Serial Connector (host connecting to device)

```json5
{
  "connect": {
    "endpoints": [
      "serial//dev/ttyUSB0?baudrate=115200&exclusive=true&tout=100000"
    ]
  }
}
```

#### Serial with Low Timeout (for responsive embedded loops)

```json5
{
  "connect": {
    "endpoints": [
      "serial//dev/ttyACM0?baudrate=921600&tout=10000"
    ]
  }
}
```

#### Release on Close Disabled (keep port open across reconnects)

```json5
{
  "listen": {
    "endpoints": [
      "serial//dev/ttyUSB0?baudrate=115200&release_on_close=false"
    ]
  }
}
```

### zenoh-pico Serial Example (C)

```c
// zenoh-pico on embedded (e.g., Arduino/Zephyr)
z_owned_config_t config;
z_config_default(&config);
zp_config_insert(z_config_loan(&config),
    Z_CONFIG_CONNECT_KEY,
    "serial//dev/ttyUSB0?baudrate=115200");
```

---

## 9. Shared Memory

### Overview

Shared Memory (SHM) is not a separate transport protocol in the same sense as TCP or UDP. It is a **zero-copy optimization layer** applied on top of an existing unicast transport (typically TCP or Unix domain sockets between processes on the same host). When SHM is available and the publisher and subscriber are co-located on the same machine, Zenoh replaces the serialized payload with a handle pointing into a shared memory region. The receiver maps that region and reads the payload without copying.

### Use Cases

- **High-throughput inter-process communication on a single host** (zero-copy).
- Large payloads (images, point clouds, video frames) where serialization cost is significant.
- Real-time systems requiring deterministic latency without memory allocation on the data path.
- Any scenario where publisher and subscriber are on the same physical machine.

### Performance Characteristics

| Property | Value |
|---|---|
| Reliable | Depends on underlying transport |
| Zero-copy | ✅ Yes (on same host) |
| Cross-host | ❌ No (falls back to normal transport) |
| Requires feature flag | ✅ Yes (`shared-memory` Cargo feature) |
| Memory backend | Platform-specific POSIX/Windows SHM |

When the receiver is on a different host, Zenoh automatically falls back to serialized transmission — no code change required.

### Enabling SHM

#### Cargo feature flag (Rust)

```toml
[dependencies]
zenoh = { version = "1.x", features = ["shared-memory"] }
```

#### Configuration

```json5
{