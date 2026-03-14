# Zenoh Transport Layer: Complete Guide

## Table of Contents

1. [TCP](#1-tcp)
2. [UDP Unicast](#2-udp-unicast)
3. [UDP Multicast](#3-udp-multicast)
4. [TLS](#4-tls)
5. [QUIC](#5-quic)
6. [WebSocket](#6-websocket)
7. [Serial](#7-serial)
8. [Shared Memory](#8-shared-memory)
9. [Link-Level Configuration](#9-link-level-configuration)
10. [TX Queue and Congestion Control](#10-tx-queue-and-congestion-control)
11. [RX Buffer Sizes](#11-rx-buffer-sizes)
12. [Multiple Transports Simultaneously](#12-multiple-transports-simultaneously)
13. [Transport Selection Priority](#13-transport-selection-priority)

---

## 1. TCP

### Overview

TCP is Zenoh's **default transport**. It is the most widely supported, reliable, and stream-oriented. When you specify no transport in your config, Zenoh defaults to `tcp/`.

### Endpoint Format

```
tcp/<host>:<port>
tcp/0.0.0.0:7447          # listen on all interfaces
tcp/192.168.1.10:7447     # listen on specific IP
tcp/localhost:7447         # connect to local host
tcp/[::]:7447              # IPv6 any-address
tcp/[::1]:7447             # IPv6 loopback
```

### Use Cases

- General-purpose peer-to-peer and client-router communication
- LAN and WAN deployments where reliability is required
- Default for zenohd router processes
- Any scenario where you don't have specific constraints favoring other transports
- Environments where UDP is blocked by firewalls

### Performance Characteristics

- **Reliability:** Yes (TCP guarantees delivery and ordering)
- **Streamed:** Yes (byte-stream; Zenoh uses 16-bit length prefix framing)
- **Max MTU:** 65535 bytes (`BatchSize::MAX`, i.e., `2^16 - 1`)
- **Effective MTU:** Computed at link creation time from the TCP MSS; on Unix the actual MTU is the largest multiple of MSS that fits within the 65535 ceiling. For IPv4 a 40-byte header overhead is subtracted; for IPv6, 60 bytes.
- **Latency:** Low but higher than UDP due to TCP's built-in ACK/retransmit mechanism
- **Throughput:** High; TCP window scaling handles long-fat networks well
- **TCP_NODELAY:** Enabled automatically on every link
- **SO_LINGER:** Set to 10 seconds by default

### TCP-Specific Configuration Options

These can be placed in the global config under `transport.link.tcp` **or** inline in the endpoint config string.

| Key | Description | Default |
|-----|-------------|---------|
| `so_rcvbuf` | Socket receive buffer size (bytes) | OS default |
| `so_sndbuf` | Socket send buffer size (bytes) | OS default |
| `iface` | Bind to a specific network interface name | unset |
| `bind` | Bind to a specific local `ip:port` | unset |
| `dscp` | DSCP value for QoS marking (0–63) | unset |

> **Note:** `iface` and `bind` are mutually exclusive. Setting both causes an error.

### Config Snippets

**Minimal listener (JSON5):**
```json5
{
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  }
}
```

**Connect to a remote router:**
```json5
{
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"]
  }
}
```

**Full TCP config with buffer tuning:**
```json5
{
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  },
  transport: {
    link: {
      tcp: {
        so_rcvbuf: 2097152,   // 2 MiB receive buffer
        so_sndbuf: 2097152    // 2 MiB send buffer
      }
    }
  }
}
```

**Per-endpoint config via inline parameters (endpoint config string):**
```
tcp/192.168.1.100:7447#so_rcvbuf=2097152;so_sndbuf=2097152;iface=eth0
```

**Bind to specific local address:**
```json5
{
  connect: {
    endpoints: ["tcp/192.168.1.100:7447#bind=192.168.1.50:0"]
  }
}
```

---

## 2. UDP Unicast

### Overview

UDP unicast sends datagrams to a single specific endpoint. It trades TCP's reliability guarantees for lower per-packet overhead and latency. Zenoh handles framing and sequencing at the protocol level when needed.

### Endpoint Format

```
udp/<host>:<port>
udp/0.0.0.0:7447
udp/192.168.1.10:7447
udp/[::]:7447
```

### Use Cases

- Low-latency telemetry where occasional packet loss is acceptable
- Local network environments with negligible packet loss
- High-frequency sensor data where freshness matters more than completeness
- When multicast is not needed but UDP overhead savings are desired
- Systems where TCP connection overhead is significant (many short-lived sessions)

### Performance Characteristics

- **Reliability:** No (best-effort delivery)
- **Streamed:** No (datagram-based)
- **Max MTU:** Platform-dependent:
  - Linux / Windows: `65535 - 8 (UDP header) - 40 (IP header) = 65487`
  - macOS: `9216`
  - Other platforms: `8192`
- **Latency:** Lower than TCP; no connection setup, no ACK round-trips
- **Throughput:** Good for small messages; large messages fragment at IP layer
- **Head-of-line blocking:** None (each datagram is independent)

### UDP Unicast-Specific Configuration Options

| Key | Description | Default |
|-----|-------------|---------|
| `so_rcvbuf` | Socket receive buffer size (bytes) | OS default |
| `so_sndbuf` | Socket send buffer size (bytes) | OS default |
| `iface` | Bind to a specific network interface | unset |
| `bind` | Bind to a specific local `ip:port` | unset |
| `dscp` | DSCP/ToS value for QoS | unset |

### Config Snippets

**Listen on UDP:**
```json5
{
  listen: {
    endpoints: ["udp/0.0.0.0:7447"]
  }
}
```

**Connect via UDP:**
```json5
{
  connect: {
    endpoints: ["udp/192.168.1.100:7447"]
  }
}
```

**UDP with buffer tuning:**
```json5
{
  listen: {
    endpoints: ["udp/0.0.0.0:7447"]
  },
  transport: {
    link: {
      udp: {
        so_rcvbuf: 4194304,   // 4 MiB
        so_sndbuf: 4194304
      }
    }
  }
}
```

**Inline per-endpoint config:**
```
udp/192.168.1.100:7447#so_rcvbuf=4194304;iface=eth0
```

---

## 3. UDP Multicast

### Overview

UDP multicast enables one-to-many communication within a multicast group. Zenoh uses multicast primarily for **scouting** — the automatic discovery of other Zenoh peers and routers on the local network without requiring pre-configured endpoints. Each node joins a multicast group, and scouting messages are sent to that group so all members discover each other.

### Endpoint Format

```
udp/<multicast-group>:<port>
udp/224.0.0.224:7446      # default Zenoh scouting address (IPv4)
udp/[ff02::1]:7446         # IPv6 link-local all-nodes multicast
```

The default Zenoh multicast scouting address is `224.0.0.224:7446`.

### Use Cases

- **Automatic peer discovery** on a LAN (the primary use case)
- Broadcast-style data distribution where all group members should receive every message
- IoT deployments where nodes should self-organize without a central router
- Lab or development environments for zero-configuration setup
- Edge computing clusters on a common L2 segment

### Performance Characteristics

- **Reliability:** No (UDP best-effort)
- **Streamed:** No (datagram-based)
- **Scope:** Limited to the multicast TTL / scope (default link-local)
- **Latency:** Very low for discovery (single UDP packet sent, all receivers process simultaneously)
- **MTU:** Same platform limits as UDP unicast
- **Scalability:** Degrades with very large numbers of group members due to multicast amplification

### Multicast Group and Interface Configuration

| Config Path | Description | Default |
|-------------|-------------|---------|
| `scouting.multicast.address` | Multicast group address and port | `224.0.0.224:7446` |
| `scouting.multicast.enabled` | Enable multicast scouting | `true` |
| `scouting.multicast.interface` | Network interface to use for multicast | `auto` |
| `scouting.multicast.ttl` | Multicast TTL (hops) | `1` (link-local) |
| `scouting.multicast.autoconnect` | Auto-connect to discovered peers | peer-mode specific |
| `scouting.multicast.listen` | Whether to listen for multicast scouts | `true` |

### Config Snippets

**Default multicast scouting (no explicit config needed):**
```json5
{
  scouting: {
    multicast: {
      enabled: true
    }
  }
}
```

**Custom multicast group:**
```json5
{
  scouting: {
    multicast: {
      enabled: true,
      address: "224.0.0.123:7446",
      interface: "eth0",
      ttl: 1
    }
  }
}
```

**Disable multicast scouting (use only configured endpoints):**
```json5
{
  scouting: {
    multicast: {
      enabled: false
    }
  },
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"]
  }
}
```

**IPv6 multicast:**
```json5
{
  scouting: {
    multicast: {
      enabled: true,
      address: "[ff02::1]:7446",
      interface: "eth0"
    }
  }
}
```

**Explicitly add a multicast listen endpoint:**
```json5
{
  listen: {
    endpoints: ["udp/224.0.0.224:7446"]
  }
}
```

### Multicast Notes

- TTL of `1` means multicast is confined to the local network segment (does not cross routers). Increase to extend scope, but be mindful of network policies.
- On multi-homed hosts, always specify the `interface` to avoid sending scouting traffic on unintended interfaces.
- Multicast scouting does **not** replace unicast data transport; once peers discover each other, they typically establish TCP or UDP unicast sessions for data exchange.

---

## 4. TLS

### Overview

TLS provides **TCP + TLS 1.3** encrypted transport. It uses the same byte-stream model as TCP but adds authentication (via X.509 certificates) and encryption. Zenoh's TLS implementation is built on `rustls` + `tokio-rustls`.

### Endpoint Format

```
tls/<host>:<port>
tls/0.0.0.0:7447
tls/192.168.1.10:7447
tls/my.broker.example.com:7447
```

### Use Cases

- Any deployment over untrusted networks (WAN, public internet)
- IoT fleets requiring device authentication (use mTLS)
- Regulatory or compliance requirements mandating encryption in transit
- Multi-tenant environments where peer identity must be verified
- Cloud-to-edge communication across organizational boundaries

### Performance Characteristics

- **Reliability:** Yes (inherits TCP reliability)
- **Streamed:** Yes
- **Max MTU:** 65535 bytes (same as TCP)
- **Effective MTU:** Same MSS-based computation as TCP, minus TLS record overhead
- **Latency overhead:** ~1 RTT for TLS 1.3 handshake on first connect (0-RTT resumption not currently used)
- **CPU overhead:** AES-NI hardware acceleration used when available via `ring` crypto provider
- **Auth:** Server certificate verified by default; mTLS adds client certificate verification

### Certificate Loading Methods

Certificates and keys can be supplied in three ways for each parameter:

| Method | Config Key Suffix |
|--------|-------------------|
| File path | `_file` |
| Base64-encoded PEM string | `_base64` |
| Raw inline string | `_raw` |

### TLS Configuration Options

These live under `transport.link.tls` in the global config **or** inline in the endpoint config string.

| Key | Description | Default |
|-----|-------------|---------|
| `root_ca_certificate_file` | Path to PEM CA certificate to trust | unset |
| `root_ca_certificate_base64` | Base64 PEM CA cert | unset |
| `listen_private_key_file` | Server private key (PEM) | required for listener |
| `listen_private_key_base64` | Base64 server private key | required for listener |
| `listen_certificate_file` | Server certificate chain (PEM) | required for listener |
| `listen_certificate_base64` | Base64 server cert chain | required for listener |
| `connect_private_key_file` | Client private key (PEM) for mTLS | required if mTLS |
| `connect_private_key_base64` | Base64 client private key | required if mTLS |
| `connect_certificate_file` | Client certificate chain (PEM) for mTLS | required if mTLS |
| `connect_certificate_base64` | Base64 client cert | required if mTLS |
| `enable_mtls` | Enable mutual TLS (client cert required) | `false` |
| `verify_name_on_connect` | Verify server hostname in cert | `true` |
| `close_link_on_expiration` | Auto-close when cert expires | `false` |
| `so_rcvbuf` | TCP receive buffer size | OS default |
| `so_sndbuf` | TCP send buffer size | OS default |
| `iface` | Bind to interface | unset |
| `bind` | Bind to local `ip:port` | unset |
| `dscp` | DSCP value | unset |

> **Key formats supported:** RSA, PKCS8, EC private keys (auto-detected via `rustls-pemfile`).

### Config Snippets

**TLS listener (server-side):**
```json5
{
  listen: {
    endpoints: ["tls/0.0.0.0:7447"]
  },
  transport: {
    link: {
      tls: {
        listen_private_key_file: "/etc/zenoh/server.key",
        listen_certificate_file: "/etc/zenoh/server.crt"
      }
    }
  }
}
```

**TLS client connecting to a known CA:**
```json5
{
  connect: {
    endpoints: ["tls/router.example.com:7447"]
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate_file: "/etc/zenoh/ca.crt"
      }
    }
  }
}
```

**Mutual TLS (mTLS) — both sides authenticate:**
```json5
// Server config
{
  listen: {
    endpoints: ["tls/0.0.0.0:7447"]
  },
  transport: {
    link: {
      tls: {
        listen_private_key_file: "/etc/zenoh/server.key",
        listen_certificate_file: "/etc/zenoh/server.crt",
        root_ca_certificate_file: "/etc/zenoh/ca.crt",
        enable_mtls: true
      }
    }
  }
}

// Client config
{
  connect: {
    endpoints: ["tls/router.example.com:7447"]
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate_file: "/etc/zenoh/ca.crt",
        connect_private_key_file: "/etc/zenoh/client.key",
        connect_certificate_file: "/etc/zenoh/client.crt",
        enable_mtls: true
      }
    }
  }
}
```

**Disable hostname verification (testing only — not for production):**
```json5
{
  transport: {
    link: {
      tls: {
        verify_name_on_connect: false
      }
    }
  }
}
```

**Inline endpoint parameters:**
```
tls/router.example.com:7447#root_ca_certificate_file=/etc/zenoh/ca.crt;enable_mtls=false
```

**Base64-encoded certificates (for containerized deployments):**
```json5
{
  transport: {
    link: {
      tls: {
        root_ca_certificate_base64: "LS0tLS1CRUdJTi...",
        listen_private_key_base64: "LS0tLS1CRUdJTi...",
        listen_certificate_base64: "LS0tLS1CRUdJTi..."
      }
    }
  }
}
```

### Certificate Expiration Monitoring

When `close_link_on_expiration: true`, Zenoh spawns a background task that monitors the peer certificate chain's `not_after` field and closes the link when the earliest expiring certificate in the chain expires. This forces a reconnect, which will fail if the certificate has not been renewed.

---

## 5. QUIC

### Overview

QUIC runs over UDP but provides stream multiplexing, built-in TLS 1.3, and connection migration. Zenoh supports **two QUIC modes**:

- **`quic/` (stream mode):** Uses a single bidirectional QUIC stream per connection. Reliable and ordered, similar to TLS/TCP but with faster connection setup. This is the standard QUIC transport.
- **`quic_datagram/` (datagram mode):** Uses QUIC's unreliable datagram extension (RFC 9221). Provides encryption and authentication without reliability guarantees. Lower latency than stream mode.

Zenoh's QUIC implementation uses the `quinn` crate with `rustls` as the crypto backend.

### Endpoint Format

```
quic/<host>:<port>          # stream mode (reliable)
quic/0.0.0.0:7447
quic/router.example.com:7448
```

### Use Cases

**Prefer QUIC over TCP when:**
- You need **TLS-equivalent security** with **faster connection establishment** (0-RTT or 1-RTT vs TCP's 3-way handshake + TLS handshake)
- You're on a **lossy network** where TCP's head-of-line blocking would hurt throughput
- **Mobile or multi-homed** scenarios where IP addresses may change (QUIC connection migration)
- Traversing **NATs** where UDP is more likely to succeed than TCP
- You want encryption **mandatory by design** (QUIC cannot run without TLS)

**Prefer QUIC datagram when:**
- You want encryption + authentication but can tolerate packet loss
- Low-latency telemetry over secured channels
- Same use cases as UDP unicast but on networks where UDP requires TLS-level authentication

### Performance Characteristics

| Property | QUIC Stream | QUIC Datagram |
|----------|-------------|---------------|
| Reliability | Yes | No |
| Streamed | Yes | No |
| Max MTU | 65535 | Platform UDP MTU |
| Encryption | Mandatory TLS 1.3 | Mandatory TLS 1.3 |
| Head-of-line blocking | None (per-stream) | None |
| Connection setup | 1-RTT (0-RTT possible) | 1-RTT |
| MTU discovery | Static | Dynamic (configurable) |

QUIC stream MTU is `65535` (constrained by Zenoh's 16-bit batch size encoding). QUIC datagram MTU is discovered dynamically and is queried from `connection.max_datagram_size()` at runtime.

### QUIC Requires TLS Certificates

Unlike TCP/UDP, QUIC **always requires TLS configuration**. A listener with no TLS config will fail with `"No QUIC configuration provided"`. The certificate options are identical to the TLS transport.

### QUIC Configuration Options

| Key | Description | Default |
|-----|-------------|---------|
| `root_ca_certificate_file` | CA cert to trust for server verification | unset |
| `root_ca_certificate_base64` | Base64 CA cert | unset |
| `listen_private_key_file` | Server private key | required for listener |
| `listen_certificate_file` | Server certificate | required for listener |
| `connect_private_key_file` | Client key for mTLS | required if mTLS |
| `connect_certificate_file` | Client cert for mTLS | required if mTLS |
| `enable_mtls` | Mutual TLS | `false` |
| `verify_name_on_connect` | Verify server hostname | `true` |
| `close_link_on_expiration` | Close on cert expiry | `false` |
| `iface` | Bind to interface | unset |
| `bind` | Bind to local socket | unset |
| `dscp` | DSCP value | unset |
| `initial_mtu` *(datagram only)* | Initial MTU hint | unset |
| `mtu_discovery_interval_secs` *(datagram only)* | MTU discovery interval | QUIC default |

### QUIC Protocol Constraints

From the source code, each QUIC connection allows:
- **0 unidirectional streams** (`max_concurrent_uni_streams = 0`)
- **1 bidirectional stream** (`max_concurrent_bidi_streams = 1`)

ALPN protocol negotiated: `hq-29` (HTTP/3 draft compatible — used as a standard ALPN token).

### Config Snippets

**QUIC listener:**
```json5
{
  listen: {
    endpoints: ["quic/0.0.0.0:7448"]
  },
  transport: {
    link: {
      tls: {
        listen_private_key_file: "/etc/zenoh/server.key",
        listen_certificate_file: "/etc/zenoh/server.crt"
      }
    }
  }
}
```

**QUIC client:**
```json5
{
  connect: {
    endpoints: ["quic/router.example.com:7448"]
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate_file: "/etc/zenoh/ca.crt"
      }
    }
  }
}
```

**QUIC with inline cert config:**
```
quic/router.example.com:7448#root_ca_certificate_file=/etc/zenoh/ca.crt;enable_mtls=false
```

**QUIC datagram listener:**
```json5
{
  listen: {
    endpoints: ["quic/0.0.0.0:7448#rel=0;initial_mtu=1400;mtu_discovery_interval_secs=60"]
  },
  transport: {
    link: {
      tls: {
        listen_private_key_file: "/etc/zenoh/server.key",
        listen_certificate_file: "/etc/zenoh/server.crt"
      }
    }
  }
}
```

> **Note on reliability metadata:** The `rel=0` metadata tag in the locator signals unreliable transport to the Zenoh protocol layer when using QUIC datagrams.

---

## 6. WebSocket

### Overview

The WebSocket transport (`ws://` or `wss://` for secure) enables Zenoh to communicate through browser environments and WebSocket-capable proxies. It wraps Zenoh's binary protocol in WebSocket frames, which are HTTP-upgradeable TCP connections.

### Endpoint Format

```
ws/<host>:<port>
ws/0.0.0.0:7447
ws/127.0.0.1:7447
wss/0.0.0.0:7448          # WebSocket over TLS
```

### Use Cases

- **Browser-based Zenoh clients** (zenoh-ts, zenoh-js) connecting to a router
- Environments where only HTTP/WebSocket ports (80, 443) are open through firewalls
- REST/WebSocket API gateways bridging web clients to the Zenoh fabric
- CDN or load balancer environments that support WebSocket passthrough
- Web dashboards and monitoring applications

### Performance Characteristics

- **Reliability:** Yes (WebSocket runs over TCP)
- **Streamed:** Yes
- **MTU:** 65535 bytes (same 16-bit limit as TCP)
- **Overhead:** HTTP upgrade handshake on connection; per-frame header (2–10 bytes per message) on top of TCP
- **Latency:** Similar to TCP after handshake; slightly higher due to framing
- **Browser compatibility:** Full (any modern browser supports WebSocket)

### WebSocket Configuration

WebSocket shares most config with TCP. The primary config is the endpoint itself:

```json5
{
  listen: {
    endpoints: ["ws/0.0.0.0:7447"]
  }
}
```

For TLS-secured WebSocket (`wss://`), configure TLS certificates just as you would for the `tls/` transport:
```json5
{
  listen: {
    endpoints: ["ws/0.0.0.0:8443"]
  },
  transport: {
    link: {
      tls: {
        listen_private_key_file: "/etc/zenoh/server.key",
        listen_certificate_file: "/etc/zenoh/server.crt"
      }
    }
  }
}
```

### Multi-Transport Router (TCP + WebSocket)

A common pattern is to run TCP for native clients and WebSocket for web clients on the same router:

```json5
{
  listen: {
    endpoints: [
      "tcp/0.0.0.0:7447",
      "ws/0.0.0.0:7446"
    ]
  }
}
```

---

## 7. Serial

### Overview

The Serial transport enables Zenoh communication over **UART / RS-232 / USB serial** connections. This is the primary transport for embedded systems using **zenoh-pico** (Zenoh's C implementation for microcontrollers) connected to a host machine.

### Endpoint Format

```
serial/<device-path>
serial//dev/ttyUSB0
serial//dev/ttyACM0
serial/COM3               # Windows
serial//dev/ttyS0         # hardware UART
```

The device path is the OS device node for the serial port.

### Use Cases

- Connecting microcontrollers / embedded devices (Arduino, STM32, ESP32) to a Zenoh network via USB-serial adapter
- UART-based sensor networks bridged to IP networks
- Industrial equipment using RS-232 or RS-485 interfaces
- Robotics platforms communicating with motor controllers or sensor boards
- Any zenoh-pico device connected to a zenoh (full) router via serial cable

### Performance Characteristics

- **Reliability:** No (serial framing with `z_serial`'s COBS-like encoding; no guaranteed delivery at this layer)
- **Streamed:** No (message-framed)
- **Max MTU:** Determined by `z_serial::MAX_MTU` (the `z-serial` crate's maximum message size)
- **Baudrate:** 9600 baud default; configurable up to hardware maximum
- **Latency:** Proportional to baudrate; a 115200 baud link has ~87 µs per byte
- **Exclusive access:** Port is locked exclusively by default to prevent conflicts

### Serial-Specific Configuration Options

These are set via endpoint config parameters:

| Key | Description | Default |
|-----|-------------|---------|
| `baudrate` | Serial port baud rate | `9600` |
| `exclusive` | Lock port exclusively | `true` |
| `tout` | Read timeout in microseconds | `50000` (50 ms) |
| `release_on_close` | Release (close) the port file handle when link closes | `true` |

### Config Snippets

**Listen on a serial port (waiting for a device to connect):**
```json5
{
  listen: {
    endpoints: ["serial//dev/ttyUSB0#baudrate=115200"]
  }
}
```

**Connect to a device via serial:**
```json5
{
  connect: {
    endpoints: ["serial//dev/ttyACM0#baudrate=115200;exclusive=true;tout=100000"]
  }
}
```

**Windows serial port:**
```json5
{
  connect: {
    endpoints: ["serial/COM3#baudrate=9600"]
  }
}
```

**Keep port open across reconnects:**
```json5
{
  listen: {
    endpoints: ["serial//dev/ttyUSB0#baudrate=115200;release_on_close=false"]
  }
}
```

When `release_on_close=false`, the serial file descriptor is kept open even after the link closes, which reduces reconnect latency when the remote device reboots.

### Serial Listener Behavior

The serial listener (`new_listener`) spawns an accept loop that:
1. Waits for the port to become disconnected
2. Opens the serial device (if `release_on_close=true`)
3. Clears RX buffers
4. Calls `port.accept()` in a poll loop with 100 ms sleeps until a connection handshake is detected
5. Reports the new link to the transport manager

This means serial connections are **re-established automatically** after a disconnect, making it suitable for hot-pluggable USB devices.

---

## 8. Shared Memory

### Overview

Shared Memory (SHM) is not a network transport in the traditional sense — it is a **zero-copy IPC mechanism** for processes on the **same host**. Instead of copying message payloads through sockets, the publisher writes data into a shared memory segment and sends only a reference (pointer + metadata) over the normal transport. The subscriber maps the same segment and reads directly from it.

### Requirements

- Both publisher and subscriber must be on the **same machine**
- The `transport.shared_memory.enabled` config must be set to `true`
- Both processes must use a transport that supports SHM metadata (TCP and UDP unicast work; the metadata message is tiny)
- The `zenoh` crate must be compiled with the `shared-memory` feature (or use the official release builds which include it)

### How It Works

1. **Publisher side:** When publishing, if SHM is enabled and the message is large enough, Zenoh allocates the payload in a named SHM segment. The message sent over the transport contains only a **SHM descriptor** (segment ID, offset, length) rather than the actual bytes.
2. **Transport:** The SHM descriptor rides over the normal transport (TCP/UDP) as a small control message.
3. **Subscriber side:** Upon receiving an SHM descriptor, Zenoh maps the referenced segment and presents the data directly to the application — **zero copy**, no data movement.
4. **Garbage collection:** Reference counting ensures the SHM segment is released only after all readers have finished.

### Automatic vs Explicit SHM

**Automatic (transparent):** Enable SHM globally; Zenoh decides when to use it based on whether both endpoints are on the same host and the payload is above a threshold.

```json5
{
  transport: {
    shared_memory: {
      enabled: true
    }
  }
}
```

**Explicit (API-level):** Use `ShmProvider` and `ZSlice` APIs to explicitly allocate and publish from SHM buffers. Gives full control over allocation and reuse.

### SHM Configuration Options

| Config Path | Description | Default |
|-------------|-------------|---------|
| `transport.shared_memory.enabled` | Enable SHM transport globally | `false` |

Additional configuration is done programmatically via the `ShmProvider` API