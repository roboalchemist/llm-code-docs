# Zenoh Config: Shared Memory Transport

Configuration reference for `transport.shared_memory` — controls the Shared Memory (SHM) subsystem and its transport-level optimization for large messages.

> For a comprehensive guide to using SHM in Zenoh applications, see [shared-memory-complete-guide.md](./shared-memory-complete-guide.md).

---

## Table of Contents

- [Overview](#overview)
- [Fields](#fields)
  - [`transport.shared_memory.enabled`](#transportshared_memoryenabled)
  - [`transport.shared_memory.mode`](#transportshared_memorymode)
  - [`transport.shared_memory.transport_optimization.enabled`](#transportshared_memorytransport_optimizationenabled)
  - [`transport.shared_memory.transport_optimization.pool_size`](#transportshared_memorytransport_optimizationpool_size)
  - [`transport.shared_memory.transport_optimization.message_size_threshold`](#transportshared_memorytransport_optimizationmessage_size_threshold)
- [Full SHM Configuration Example](#full-shm-configuration-example)
- [Disabling SHM Completely](#disabling-shm-completely)
- [Requirements](#requirements)
- [Source](#source)

## Overview

The SHM transport in Zenoh has two distinct modes:
1. **Application-level SHM**: Applications explicitly allocate SHM buffers via the Zenoh API and publish them — data is transferred via SHM for zero-copy.
2. **Transport-level optimization** (`transport_optimization`): Zenoh automatically places large messages into SHM internally, even when the application does not explicitly use SHM. This happens transparently for any session that supports SHM.

Both modes require SHM to be enabled (`enabled: true`) and both endpoints to negotiate SHM support during session establishment.

---

## Fields

### `transport.shared_memory.enabled`

**Type**: `bool`
**Default**: `true`

Announces SHM buffer optimization support to connecting peers during session establishment. When `true`, a probing procedure occurs at session open time — if both sides have SHM enabled, SHM transport is used; otherwise, the session falls back to network mode.

Setting to `false` completely disables SHM support for this session, including both application-level and transport-level optimization.

```json5
transport: { shared_memory: { enabled: true } }
```

> **Note**: For SHM to operate (rather than falling back to network), both the publisher and subscriber must have `enabled: true`. Setting it on only one side causes fallback to network mode.

### `transport.shared_memory.mode`

**Type**: `"init"` | `"lazy"`
**Default**: `"lazy"`

Controls when SHM subsystem internals are initialized.

- `"lazy"` (default): SHM resources are initialized on first use (first SHM buffer allocation or reception). Provides faster startup time and lower resource usage at idle, at the cost of extra latency on the very first SHM interaction.
- `"init"`: SHM resources are initialized when the session opens. Eliminates first-interaction latency but increases startup time and resource consumption.

```json5
transport: { shared_memory: { mode: "lazy" } }
```

Use `"init"` in latency-sensitive applications where the first message must not pay an initialization cost.

### `transport.shared_memory.transport_optimization.enabled`

**Type**: `bool`
**Default**: `true`

Enables transparent transport-level optimization for large messages. When enabled, Zenoh automatically copies messages that exceed `message_size_threshold` into a shared-memory pool for any session that has SHM support. The sending application does not need to use the SHM API explicitly.

Disable this if you want SHM only for explicitly allocated SHM buffers and not for automatic large-message optimization.

```json5
transport: {
  shared_memory: {
    transport_optimization: { enabled: true }
  }
}
```

### `transport.shared_memory.transport_optimization.pool_size`

**Type**: `NonZeroUsize` (bytes)
**Default**: `16777216` (16 MiB = 16 × 1024 × 1024)

Size in bytes of the shared-memory pool used for transport optimization. This pool is pre-allocated (or lazily filled, depending on `mode`) and shared among all SHM-capable sessions on the same machine.

Increase if your application sends many large messages concurrently:

```json5
transport: {
  shared_memory: {
    transport_optimization: { pool_size: 67108864 }  // 64 MiB
  }
}
```

### `transport.shared_memory.transport_optimization.message_size_threshold`

**Type**: `usize` (bytes)
**Default**: `3072` (3 KiB)

Minimum message size (in bytes) for the transport optimization to apply. Messages equal to or larger than this threshold are candidates for automatic SHM placement. Messages smaller than this threshold are sent over the network regardless.

Tuning this value:
- **Lower threshold**: More messages use SHM, reducing serialization overhead for medium-sized messages.
- **Higher threshold**: Only large messages use SHM, reducing pool fragmentation for small-message workloads.

```json5
transport: {
  shared_memory: {
    transport_optimization: { message_size_threshold: 8192 }  // 8 KiB
  }
}
```

---

## Full SHM Configuration Example

```json5
transport: {
  shared_memory: {
    enabled: true,
    mode: "lazy",
    transport_optimization: {
      enabled: true,
      pool_size: 16777216,
      message_size_threshold: 3072,
    },
  }
}
```

---

## Disabling SHM Completely

```json5
transport: {
  shared_memory: {
    enabled: false,
  }
}
```

---

## Requirements

- SHM transport requires both communicating endpoints to be on the **same host** (shared memory is not available across machines).
- If one endpoint sets `enabled: false`, the session falls back to network mode transparently.
- The SHM feature must be compiled into Zenoh (`default-features` or explicit `shared-memory` cargo feature).

---

## Source

- `repos/zenoh/commons/zenoh-config/src/lib.rs` — `ShmConf`, `LargeMessageTransportOpt`
- `repos/zenoh/commons/zenoh-config/src/defaults.rs` — `Default for ShmConf`, `Default for LargeMessageTransportOpt`
- `repos/zenoh/DEFAULT_CONFIG.json5` — annotated SHM section

## See Also

- [Shared Memory Complete Guide](shared-memory-complete-guide.md) — comprehensive API and usage guide for the SHM feature these settings control
- [Performance Tuning Guide](performance-tuning-guide.md) — when and how to use SHM for maximum throughput
- [Config Transport Unicast Multicast](config-transport-unicast-multicast.md) — the surrounding transport configuration that SHM works alongside
