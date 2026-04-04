# Zenoh Config: Transport Unicast & Multicast

Configuration reference for `transport.unicast` and `transport.multicast` sections.

---

## Table of Contents

- [Unicast Transport (`transport.unicast`)](#unicast-transport-transportunicast)
  - [`transport.unicast.open_timeout`](#transportunicastopen_timeout)
  - [`transport.unicast.accept_timeout`](#transportunicastaccept_timeout)
  - [`transport.unicast.accept_pending`](#transportunicastaccept_pending)
  - [`transport.unicast.max_sessions`](#transportunicastmax_sessions)
  - [`transport.unicast.max_links`](#transportunicastmax_links)
  - [`transport.unicast.lowlatency`](#transportunicastlowlatency)
  - [`transport.unicast.qos.enabled`](#transportunicastqosenabled)
  - [`transport.unicast.compression.enabled`](#transportunicastcompressionenabled)
- [Multicast Transport (`transport.multicast`)](#multicast-transport-transportmulticast)
  - [`transport.multicast.join_interval`](#transportmulticastjoin_interval)
  - [`transport.multicast.max_sessions`](#transportmulticastmax_sessions)
  - [`transport.multicast.qos.enabled`](#transportmulticastqosenabled)
  - [`transport.multicast.compression.enabled`](#transportmulticastcompressionenabled)
- [Relationship to QoS and Scouting](#relationship-to-qos-and-scouting)
- [Source](#source)

## Unicast Transport (`transport.unicast`)

Controls session establishment behavior for point-to-point (unicast) transports.

### `transport.unicast.open_timeout`

**Type**: `u64`
**Default**: `10000` (10 seconds)

Timeout in milliseconds when opening a unicast link. If the link is not established within this time, the attempt is abandoned.

### `transport.unicast.accept_timeout`

**Type**: `u64`
**Default**: `10000` (10 seconds)

Timeout in milliseconds when accepting an incoming unicast link. If the remote side does not complete the handshake within this time, the pending link is dropped.

### `transport.unicast.accept_pending`

**Type**: `usize`
**Default**: `100`

Maximum number of incoming unicast link requests that may be pending (in the accept phase) simultaneously. Additional connection requests beyond this limit are dropped until pending slots free up.

### `transport.unicast.max_sessions`

**Type**: `usize`
**Default**: `1000`

Maximum number of simultaneous unicast sessions. New session requests are rejected when this limit is reached.

### `transport.unicast.max_links`

**Type**: `usize`
**Default**: `1`

Maximum number of incoming links per unicast transport session.

- When set to `1` (default), only a single link per session is allowed, and only one outgoing link per session is allowed.
- When set to `> 1`, multiple incoming links per session are accepted; multiple outgoing links per session are also allowed.

> **Note**: Multi-link support is tracked in [zenoh issue #1533](https://github.com/eclipse-zenoh/zenoh/issues/1533).

### `transport.unicast.lowlatency`

**Type**: `bool`
**Default**: `false`

Enables the low-latency transport mode. This does not mandate low-latency transport — the actual implementation depends on the establish procedure and the remote peer's configuration. Both sides should agree on this setting for it to take effect.

### `transport.unicast.qos.enabled`

**Type**: `bool`
**Default**: `true`

Enables Quality of Service for unicast transport. When `false`, QoS prioritization is disabled and only the `DATA` priority queue is used. Disabling QoS reduces per-message overhead at the cost of no traffic differentiation.

### `transport.unicast.compression.enabled`

**Type**: `bool`
**Default**: `false`

Enables batch-level compression for unicast transport. Requires Zenoh to be compiled with the `transport_compression` feature flag. When enabled, transmitted batches are compressed before sending.

**Full unicast example:**

```json5
transport: {
  unicast: {
    open_timeout: 10000,
    accept_timeout: 10000,
    accept_pending: 100,
    max_sessions: 1000,
    max_links: 1,
    lowlatency: false,
    qos: { enabled: true },
    compression: { enabled: false },
  }
}
```

---

## Multicast Transport (`transport.multicast`)

Controls behavior for multicast transports (used with multicast scouting when peers communicate over a shared multicast channel).

### `transport.multicast.join_interval`

**Type**: `Option<u64>`
**Default**: `2500` (2.5 seconds)

Interval in milliseconds at which a node re-sends its join message on the multicast group. Periodic join messages allow late-joining peers to discover existing members. Set to `null` to disable periodic join messages.

### `transport.multicast.max_sessions`

**Type**: `Option<usize>`
**Default**: `1000`

Maximum number of simultaneous multicast sessions. New sessions beyond this limit are rejected. Set to `null` for no limit.

### `transport.multicast.qos.enabled`

**Type**: `bool`
**Default**: `false`

Enables Quality of Service for multicast transport. Disabled by default because multicast groups typically share a common channel without per-peer flow control, making QoS prioritization impractical.

### `transport.multicast.compression.enabled`

**Type**: `bool`
**Default**: `false`

Enables batch-level compression for multicast transport. Requires the `transport_compression` feature flag.

**Full multicast example:**

```json5
transport: {
  multicast: {
    join_interval: 2500,
    max_sessions: 1000,
    qos: { enabled: false },
    compression: { enabled: false },
  }
}
```

---

## Relationship to QoS and Scouting

- **Unicast QoS** (`qos.enabled: true`) is required for the full 8-priority queue structure to be active. When disabled, only the DATA queue exists.
- **Multicast sessions** are discovered via `scouting.multicast`; the `transport.multicast` section controls the ongoing session maintenance after discovery.
- **Low-latency mode** bypasses the priority queue entirely, trading throughput for minimal latency. It requires `lowlatency: true` on both endpoints.

---

## Source

- `repos/zenoh/commons/zenoh-config/src/lib.rs` — `TransportUnicastConf`, `TransportMulticastConf`, `QoSUnicastConf`, `QoSMulticastConf`, `CompressionUnicastConf`, `CompressionMulticastConf`
- `repos/zenoh/commons/zenoh-config/src/defaults.rs` — `Default for TransportUnicastConf`, `Default for TransportMulticastConf`

## See Also

- [Config Transport Link TX](config-transport-link-tx.md) — per-priority queue sizes and congestion control that depend on `qos.enabled` configured here
- [Config Transport Link RX TCP](config-transport-link-rx-tcp.md) — receive buffer and TCP socket configuration for unicast sessions
- [Config Transport SHM](config-transport-shm.md) — shared memory transport configuration that works alongside unicast sessions
- [QoS Guide](qos-guide.md) — full explanation of the 8-priority queue system enabled by `transport.unicast.qos.enabled`
