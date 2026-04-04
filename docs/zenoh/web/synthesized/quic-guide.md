# Zenoh QUIC Transport Guide

## Table of Contents

- [Overview](#overview)
- [Enabling QUIC](#enabling-quic)
- [Configuration](#configuration)
- [TLS with QUIC](#tls-with-quic)
- [Locator Format](#locator-format)
- [When to Use QUIC](#when-to-use-quic)
- [ACL / QoS Policy Integration](#acl-qos-policy-integration)
- [Current Limitations (zenoh 1.x)](#current-limitations-zenoh-1x)
- [Programmatic Configuration (Rust API)](#programmatic-configuration-rust-api)
- [References](#references)

## Overview

Zenoh supports QUIC as a transport layer option alongside TCP, UDP, TLS, WebSocket, and others.
QUIC is a multiplexed, encrypted transport protocol built on UDP that was standardized as
RFC 9000. It eliminates head-of-line blocking (a key TCP limitation), provides built-in TLS 1.3
encryption, and supports faster connection establishment through 0-RTT and 1-RTT handshakes.

**Key advantages of QUIC over TCP for zenoh:**
- No head-of-line blocking: independent streams for pub/sub and query/reply traffic
- Built-in TLS 1.3 encryption (mandatory, not optional)
- Faster reconnection: 0-RTT session resumption avoids full TLS handshake penalty
- Better performance on lossy networks (mobile, satellite, WAN links)
- Connection migration: sessions survive IP address changes (relevant for mobile clients)

## Enabling QUIC

QUIC is a compile-time feature flag (`transport_quic`) in zenoh. Pre-built binaries from the
eclipse-zenoh GitHub releases include it. When building from source:

```toml
# Cargo.toml
zenoh = { version = "1.x", features = ["transport_quic"] }
```

## Configuration

QUIC endpoints use the `quic/` scheme in zenoh locators:

```json5
{
  listen: {
    endpoints: ["quic/0.0.0.0:7447"],
  },
  connect: {
    endpoints: ["quic/router.example.com:7447"],
  }
}
```

You can also restrict a session to QUIC-only (disable TCP/UDP):

```json5
{
  transport: {
    link: {
      // Whitelist only quic (and tls if desired)
      protocols: ["quic"],
    }
  }
}
```

QUIC shares the same TLS configuration block as TLS links in `DEFAULT_CONFIG.json5`:

```json5
{
  transport: {
    link: {
      tls: {
        // CA certificate for validating peers (null = use WebPKI roots for client mode)
        root_ca_certificate: "/path/to/ca.pem",

        // Server-side (listener) identity
        listen_private_key: "/path/to/server.key",
        listen_certificate: "/path/to/server.pem",

        // Client-side (connector) identity — required for mTLS
        connect_private_key: "/path/to/client.key",
        connect_certificate: "/path/to/client.pem",

        // Enable mutual TLS (client certificate authentication)
        enable_mtls: false,

        // Disconnect when remote certificate expires (requires mTLS for listener side)
        close_link_on_expiration: false,

        // Verify SNI/hostname on connect (true recommended)
        verify_name_on_connect: true,
      }
    }
  }
}
```

For local-network or development use, you can disable hostname verification:

```json5
{
  transport: {
    link: {
      tls: {
        verify_name_on_connect: false,
      }
    }
  }
}
```

## TLS with QUIC

QUIC mandates TLS 1.3 — there is no unencrypted QUIC. You must provide certificates.

**Self-signed certificate setup (development):**

```bash
# Generate CA
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 1826 -key ca.key -out ca.pem \
  -subj "/CN=ZenohCA"

# Generate server cert
openssl genrsa -out server.key 4096
openssl req -new -key server.key -out server.csr \
  -subj "/CN=localhost"
openssl x509 -req -days 825 -in server.csr -CA ca.pem -CAkey ca.key \
  -CAcreateserial -out server.pem \
  -extfile <(printf "subjectAltName=DNS:localhost,IP:127.0.0.1")
```

**Access control with QUIC:** The ACL system can use TLS/QUIC certificate common names as
subjects for fine-grained access policies:

```json5
{
  access_control: {
    rules: [{
      // cert_common_names available when using TLS or QUIC
      subjects: [{ cert_common_names: ["router-node"] }],
      // ...
    }]
  }
}
```

## Locator Format

QUIC locators follow the same pattern as TCP/TLS:

```
quic/<host>:<port>[?<metadata>][#<config>]
```

The `?` delimiter is for metadata (priority, reliability). The `#` delimiter is for configuration parameters (like `bind`).

Examples:
- `quic/localhost:7447` — local QUIC listener/connector
- `quic/0.0.0.0:7447` — listen on all interfaces
- `quic/[::]:7447` — listen on all IPv6 interfaces
- `quic/192.168.1.10:7448` — specific IP

You can also specify a `bind` address for the local socket (useful for multi-homed hosts):

```json5
{
  connect: {
    endpoints: ["quic/router.example.com:7447#bind=192.168.1.5:0"],
  }
}
```

## When to Use QUIC

| Scenario | Recommendation |
|----------|---------------|
| High packet loss (mobile, satellite) | QUIC preferred over TCP |
| Multiplexed pub/sub + queries, avoid head-of-line blocking | QUIC |
| Already need TLS encryption | QUIC (one protocol instead of TCP+TLS) |
| Embedded / constrained devices (zenoh-pico) | TCP or UDP (QUIC not available in zenoh-pico) |
| Maximum raw throughput on reliable LAN | TCP may outperform (less overhead) |
| UDP multicast (peer discovery) | UDP (QUIC is unicast only) |
| Firewall traversal issues with UDP | TCP or TLS (QUIC uses UDP ports) |

## ACL / QoS Policy Integration

QUIC links can be referenced in access control and QoS overwrite rules by protocol name:

```json5
{
  access_control: {
    rules: [{
      // Apply rule only to QUIC links
      link_protocols: ["quic"],
      // ...
    }]
  },
  // QoS overwrite for QUIC links only
  // link_protocols: ["quic"]
}
```

## Current Limitations (zenoh 1.x)

- **zenoh-pico**: The C implementation for embedded devices does not include QUIC support.
  QUIC requires a TLS stack (rustls in zenoh's case) that is not feasible on MCUs.
- **UDP-based**: QUIC uses UDP internally. Firewalls that block UDP or require stateful
  inspection of TCP may interfere. Ensure UDP port 7447 (or your configured port) is open.
- **Single socket per QUIC endpoint**: When multiple QUIC links exist, they share a UDP socket.
  Binding behavior differs from TCP (only the first bind takes effect; subsequent attempts to
  bind the same port for a second QUIC link will fail — handled internally by zenoh).
- **mTLS for server-side expiration**: The `close_link_on_expiration` option requires mTLS
  to be enabled for the listener to detect client certificate expiry.

## Programmatic Configuration (Rust API)

```rust
use zenoh::config::Config;

let mut config = Config::default();

// Set QUIC listen endpoint
config.listen.endpoints
    .set(vec!["quic/0.0.0.0:7447".parse().unwrap()])
    .unwrap();

// Set TLS config for QUIC
config.transport.link.tls
    .set_root_ca_certificate(Some("/path/to/ca.pem".into()))
    .unwrap();
config.transport.link.tls
    .set_listen_private_key(Some("/path/to/server.key".into()))
    .unwrap();
config.transport.link.tls
    .set_listen_certificate(Some("/path/to/server.pem".into()))
    .unwrap();

let session = zenoh::open(config).await.unwrap();
```

Or load from a JSON5 config file:

```rust
let config = Config::from_file("/path/to/config.json5").unwrap();
let session = zenoh::open(config).await.unwrap();
```

## References

- Configuration reference: `configuration.md` (transport.link.tls section)
- TLS/auth details: `security.md`
- ACL configuration: `acl-guide.md`
- zenoh RFC on transport abstraction: `rfcs/` directory
- Rust `EndPoint` struct: https://docs.rs/zenoh/latest/zenoh/config/struct.EndPoint.html

## See Also

- [Config Transport Link RX TCP](config-transport-link-rx-tcp.md) — the `transport.link.tls` configuration block shared by QUIC and TLS transports
- [Encryption Guide](encryption-guide.md) — certificate generation and TLS configuration that QUIC requires
- [Config Connect Listen](config-connect-listen.md) — how to specify `quic://` endpoints in connect and listen configuration
