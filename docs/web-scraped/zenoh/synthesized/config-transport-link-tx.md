# Zenoh Config: Transport Link TX

Configuration reference for `transport.link.tx` — the transmit-side link configuration including sequence numbers, batching, priority queues, and congestion control.

---

## Table of Contents

- [Sequence Number and Session Parameters](#sequence-number-and-session-parameters)
  - [`transport.link.tx.sequence_number_resolution`](#transportlinktxsequence_number_resolution)
  - [`transport.link.tx.lease`](#transportlinktxlease)
  - [`transport.link.tx.keep_alive`](#transportlinktxkeep_alive)
  - [`transport.link.tx.batch_size`](#transportlinktxbatch_size)
  - [`transport.link.tx.threads`](#transportlinktxthreads)
- [Priority Queue Sizes (`transport.link.tx.queue.size`)](#priority-queue-sizes-transportlinktxqueuesize)
- [Congestion Control](#congestion-control)
  - [Drop Behavior (`transport.link.tx.queue.congestion_control.drop`)](#drop-behavior-transportlinktxqueuecongestion_controldrop)
  - [Block Behavior (`transport.link.tx.queue.congestion_control.block`)](#block-behavior-transportlinktxqueuecongestion_controlblock)
- [Batching (`transport.link.tx.queue.batching`)](#batching-transportlinktxqueuebatching)
  - [`transport.link.tx.queue.batching.enabled`](#transportlinktxqueuebatchingenabled)
  - [`transport.link.tx.queue.batching.time_limit`](#transportlinktxqueuebatchingtime_limit)
- [Queue Allocation Mode (`transport.link.tx.queue.allocation.mode`)](#queue-allocation-mode-transportlinktxqueueallocationmode)
- [Full TX Example](#full-tx-example)
- [Source](#source)

## Sequence Number and Session Parameters

### `transport.link.tx.sequence_number_resolution`

**Type**: `Bits` (string: `"8bit"`, `"16bit"`, `"32bit"`, `"64bit"`)
**Default**: `"32bit"` (derived from `TransportSn::MAX` which is `u32::MAX`)

Resolution used for message sequence numbers. When establishing a session with a remote node, the lower of the two configured values is used.

Higher resolution supports more in-flight messages before wrap-around, at the cost of slightly more header overhead.

```json5
transport: { link: { tx: { sequence_number_resolution: "32bit" } } }
```

### `transport.link.tx.lease`

**Type**: `u64`
**Default**: `10000` (10 seconds)

Link lease duration in milliseconds. If a remote node does not send any message (including keep-alives) within this window, the link is considered dead and closed.

### `transport.link.tx.keep_alive`

**Type**: `usize`
**Default**: `4`

Number of keep-alive messages sent per lease period. Keep-alives are evenly spaced across the lease window to confirm liveness when no data is being sent. With default settings: one keep-alive every 2500ms (10000ms / 4).

### `transport.link.tx.batch_size`

**Type**: `BatchSize` (u16)
**Default**: `65535` (`BatchSize::MAX` = 2^16 - 1)

The MTU equivalent for Zenoh: maximum number of bytes in a single transmission batch. Multiple messages may be coalesced into one batch up to this size. Cannot exceed 65535.

### `transport.link.tx.threads`

**Type**: `usize`
**Default**: `1 + ((num_cpus - 1) / 4)` (e.g., 1 on single-core, 2 on 4-core, 3 on 8-core)

Number of threads dedicated to the TX path. The default scales with CPU count to balance throughput with resource consumption.

---

## Priority Queue Sizes (`transport.link.tx.queue.size`)

Each of the 8 priority levels has an independent queue. Queue size is the number of batches a queue can hold. Memory per queue = `size × batch_size` bytes.

When `transport.unicast.qos.enabled = false`, only the `data` queue is allocated.

| Field | Default | Notes |
|-------|---------|-------|
| `control` | `2` | Session management messages |
| `real_time` | `2` | Highest user priority |
| `interactive_high` | `2` | |
| `interactive_low` | `2` | |
| `data_high` | `2` | |
| `data` | `2` | Default priority for user data |
| `data_low` | `2` | |
| `background` | `2` | Lowest priority |

**Valid range**: 1–16 (inclusive) per queue.

```json5
transport: {
  link: {
    tx: {
      queue: {
        size: {
          control: 2,
          real_time: 2,
          interactive_high: 2,
          interactive_low: 2,
          data_high: 2,
          data: 2,
          data_low: 2,
          background: 2,
        }
      }
    }
  }
}
```

---

## Congestion Control

Congestion occurs when all batches in a queue are in-flight (queue is empty). Behavior depends on the message's `CongestionControl` setting.

### Drop Behavior (`transport.link.tx.queue.congestion_control.drop`)

Applied to messages with `CongestionControl::Drop`.

#### `wait_before_drop`

**Type**: `i64` (microseconds)
**Default**: `1000` (1ms)

Maximum time in microseconds to wait for a free batch before dropping the message. If no batch becomes available within this window, the message is discarded.

#### `max_wait_before_drop_fragments`

**Type**: `i64` (microseconds)
**Default**: `50000` (50ms)

Maximum wait for multi-fragment (large) messages before dropping all their fragments. Fragments awaiting reassembly are also dropped if this deadline is exceeded.

### Block Behavior (`transport.link.tx.queue.congestion_control.block`)

Applied to messages with `CongestionControl::Block`.

#### `wait_before_close`

**Type**: `i64` (microseconds)
**Default**: `5000000` (5 seconds)

Maximum time in microseconds to block the sender waiting for a free batch. If no batch becomes available within this window, the transport session is closed. Use with care — a blocking message that cannot be delivered will tear down the session.

---

## Batching (`transport.link.tx.queue.batching`)

Adaptive batching coalesces small messages into fewer network frames under back-pressure.

### `transport.link.tx.queue.batching.enabled`

**Type**: `bool`
**Default**: `true`

When enabled, multiple small messages may be combined into a single batch when the network is not fast enough to transmit each one individually. Reduces per-message overhead in high-throughput scenarios with small messages. Activated by network back-pressure, not on every message.

### `transport.link.tx.queue.batching.time_limit`

**Type**: `u64` (milliseconds)
**Default**: `1` (1ms)

Maximum time a message may be held waiting for co-batching. If no co-batching opportunity arises within this window, the message is sent alone. Limits the latency cost of batching.

---

## Queue Allocation Mode (`transport.link.tx.queue.allocation.mode`)

**Type**: `"init"` | `"lazy"`
**Default**: `"lazy"`

Controls when batch memory is allocated for the priority queues.

- `"lazy"` (default): Batch memory is allocated on first use, up to the configured `size`. Reduces startup memory footprint; useful for constrained environments.
- `"init"`: All batch memory is pre-allocated at session initialization. Eliminates allocation overhead at runtime; useful for latency-sensitive, memory-rich deployments.

```json5
transport: {
  link: {
    tx: {
      queue: {
        allocation: { mode: "lazy" }
      }
    }
  }
}
```

---

## Full TX Example

```json5
transport: {
  link: {
    tx: {
      sequence_number_resolution: "32bit",
      lease: 10000,
      keep_alive: 4,
      batch_size: 65535,
      threads: 2,
      queue: {
        size: {
          control: 2, real_time: 2,
          interactive_high: 2, interactive_low: 2,
          data_high: 2, data: 2,
          data_low: 2, background: 2,
        },
        congestion_control: {
          drop: {
            wait_before_drop: 1000,
            max_wait_before_drop_fragments: 50000,
          },
          block: {
            wait_before_close: 5000000,
          },
        },
        batching: {
          enabled: true,
          time_limit: 1,
        },
        allocation: { mode: "lazy" },
      },
    }
  }
}
```

---

## Source

- `repos/zenoh/commons/zenoh-config/src/lib.rs` — `LinkTxConf`, `QueueConf`, `QueueSizeConf`, `CongestionControlDropConf`, `CongestionControlBlockConf`, `BatchingConf`, `QueueAllocConf`, `QueueAllocMode`
- `repos/zenoh/commons/zenoh-config/src/defaults.rs` — `Default for LinkTxConf`, `Default for QueueSizeConf`, `Default for CongestionControlDropConf`, `Default for CongestionControlBlockConf`, `Default for BatchingConf`

## See Also

- [QoS Guide](qos-guide.md) — how priority levels map to the 8 queues configured here and when to use Drop vs Block
- [Performance Tuning Guide](performance-tuning-guide.md) — practical guidance on tuning batch size, queue depths, and congestion control
- [Config Transport Unicast Multicast](config-transport-unicast-multicast.md) — session-level settings that control whether QoS is enabled for these queues
- [Wire Protocol Guide](wire-protocol-guide.md) — how the transport frame structure uses the batch_size configured here
