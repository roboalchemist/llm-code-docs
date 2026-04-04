# Zenoh Config: Transport Link RX, TCP, and Protocol Whitelist

Configuration reference for `transport.link.rx`, `transport.link.tcp`, `transport.link.tls`, `transport.link.unixpipe`, and `transport.link.protocols`.

---

## Table of Contents

- [Receive Buffer (`transport.link.rx`)](#receive-buffer-transportlinkrx)
  - [`transport.link.rx.buffer_size`](#transportlinkrxbuffer_size)
  - [`transport.link.rx.max_message_size`](#transportlinkrxmax_message_size)
- [TCP Link Configuration (`transport.link.tcp`)](#tcp-link-configuration-transportlinktcp)
  - [`transport.link.tcp.so_sndbuf`](#transportlinktcpso_sndbuf)
  - [`transport.link.tcp.so_rcvbuf`](#transportlinktcpso_rcvbuf)
- [Unix Pipe Configuration (`transport.link.unixpipe`)](#unix-pipe-configuration-transportlinkunixpipe)
  - [`transport.link.unixpipe.file_access_mask`](#transportlinkunixpipefile_access_mask)
- [Protocol Whitelist (`transport.link.protocols`)](#protocol-whitelist-transportlinkprotocols)
- [TLS Link Configuration (`transport.link.tls`)](#tls-link-configuration-transportlinktls)
- [Full RX + TCP Example](#full-rx-tcp-example)
- [Source](#source)

## Receive Buffer (`transport.link.rx`)

### `transport.link.rx.buffer_size`

**Type**: `usize` (bytes)
**Default**: `65535` (= `u16::MAX` = `BatchSize::MAX`; one byte less than 64 KiB)

Receive buffer size in bytes per link. Frames received from the network are first placed in this buffer before being deserialized into messages.

For high-throughput scenarios with large messages, increase this to reduce the number of read syscalls:

```json5
transport: { link: { rx: { buffer_size: 16777216 } } }  // 16 MiB
```

### `transport.link.rx.max_message_size`

**Type**: `usize` (bytes)
**Default**: `1073741824` (1 GiB = 2^30 bytes)

Maximum size of the defragmentation buffer. Multi-fragment messages that would require more than this many bytes to reassemble are dropped. This is the effective maximum size of a single Zenoh message (after all fragments are assembled).

For embedded or constrained environments, reduce this to limit memory usage:

```json5
transport: { link: { rx: { max_message_size: 10485760 } } }  // 10 MiB
```

---

## TCP Link Configuration (`transport.link.tcp`)

### `transport.link.tcp.so_sndbuf`

**Type**: `Option<u32>` (bytes)
**Default**: `null` (OS default)

Sets the `SO_SNDBUF` socket option for TCP links — the kernel-level send buffer size. When `null`, the OS default applies (typically 256 KiB–4 MiB depending on OS).

Increase for high-throughput, high-latency links (e.g., WAN):

```json5
transport: { link: { tcp: { so_sndbuf: 4194304 } } }  // 4 MiB
```

### `transport.link.tcp.so_rcvbuf`

**Type**: `Option<u32>` (bytes)
**Default**: `null` (OS default)

Sets the `SO_RCVBUF` socket option for TCP links — the kernel-level receive buffer size.

```json5
transport: { link: { tcp: { so_rcvbuf: 4194304 } } }  // 4 MiB
```

> **Note**: These settings also apply to TLS links (`transport.link.tls.so_sndbuf` / `transport.link.tls.so_rcvbuf`), which expose the same fields.

---

## Unix Pipe Configuration (`transport.link.unixpipe`)

### `transport.link.unixpipe.file_access_mask`

**Type**: `Option<u32>`
**Default**: `null` (OS default)

File permission mask (Unix octal) applied to the Unix pipe socket file. When `null`, the system umask is used.

```json5
transport: { link: { unixpipe: { file_access_mask: 432 } } }  // 432 decimal = 0o660 octal
```

---

## Protocol Whitelist (`transport.link.protocols`)

**Type**: `Option<Vec<String>>`
**Default**: `null` (all supported protocols enabled)

An optional whitelist of link protocols allowed for accepting and opening sessions. When `null`, all protocols compiled into the binary are available.

Valid protocol names depend on compiled-in features. Common values:
- `"tcp"` — TCP unicast
- `"udp"` — UDP unicast/multicast
- `"tls"` — TLS over TCP
- `"quic"` — QUIC
- `"ws"` — WebSocket
- `"unixpipe"` — Unix domain socket pipe
- `"unixsock-stream"` — Unix domain socket stream
- `"serial"` — Serial link
- `"vsock"` — VM socket

```json5
// Allow only TCP and TLS:
transport: { link: { protocols: ["tcp", "tls"] } }

// Allow all (default):
transport: { link: { protocols: null } }
```

---

## TLS Link Configuration (`transport.link.tls`)

TLS-specific fields for secure transport links. See the [encryption guide](./encryption-guide.md) for full TLS configuration.

Key fields (all `Option<...>`, default `null` unless noted):

| Field | Type | Notes |
|-------|------|-------|
| `root_ca_certificate` | `Option<String>` | Path to root CA certificate file |
| `root_ca_certificate_base64` | `Option<SecretValue>` | Base64-encoded root CA cert (not serialized) |
| `listen_private_key` | `Option<String>` | Path to server private key file |
| `listen_private_key_base64` | `Option<SecretValue>` | Base64-encoded server private key (not serialized) |
| `listen_certificate` | `Option<String>` | Path to server certificate file |
| `listen_certificate_base64` | `Option<SecretValue>` | Base64-encoded server certificate (not serialized) |
| `enable_mtls` | `Option<bool>` | Enable mutual TLS (client cert required) |
| `connect_private_key` | `Option<String>` | Path to client private key |
| `connect_private_key_base64` | `Option<SecretValue>` | Base64-encoded client private key (not serialized) |
| `connect_certificate` | `Option<String>` | Path to client certificate |
| `connect_certificate_base64` | `Option<SecretValue>` | Base64-encoded client certificate (not serialized) |
| `verify_name_on_connect` | `Option<bool>` | Verify server hostname during TLS handshake (default behavior when `null`: `true`) |
| `close_link_on_expiration` | `Option<bool>` | Close link when certificate expires (default behavior when `null`: `false`) |
| `so_sndbuf` | `Option<u32>` | TCP send buffer for TLS links |
| `so_rcvbuf` | `Option<u32>` | TCP receive buffer for TLS links |

---

## Full RX + TCP Example

```json5
transport: {
  link: {
    protocols: null,  // all protocols
    rx: {
      buffer_size: 65535,
      max_message_size: 1073741824,
    },
    tcp: {
      so_sndbuf: null,  // OS default
      so_rcvbuf: null,  // OS default
    },
    unixpipe: {
      file_access_mask: null,  // OS default
    },
  }
}
```

---

## Source

- `repos/zenoh/commons/zenoh-config/src/lib.rs` — `LinkRxConf`, `TcpConf`, `TLSConf`, `UnixPipeConf`, `TransportLinkConf`
- `repos/zenoh/commons/zenoh-config/src/defaults.rs` — `Default for LinkRxConf`

## See Also

- [Encryption Guide](encryption-guide.md) — full TLS configuration details for the `transport.link.tls` section referenced here
- [Config Transport Link TX](config-transport-link-tx.md) — the corresponding transmit-side link configuration
- [Performance Tuning Guide](performance-tuning-guide.md) — how `so_sndbuf`/`so_rcvbuf` and `max_message_size` affect throughput
