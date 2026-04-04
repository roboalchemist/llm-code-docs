# Zenoh Performance Tuning Guide

## Table of Contents

- [Baseline Numbers](#baseline-numbers)
- [Key Expression Design](#key-expression-design)
- [QoS: Priority and Congestion Control](#qos-priority-and-congestion-control)
  - [Priority Levels](#priority-levels)
  - [Congestion Control](#congestion-control)
  - [Reliability](#reliability)
- [Transport Selection](#transport-selection)
  - [Unicast vs. Multicast](#unicast-vs-multicast)
  - [TCP Buffer Sizes](#tcp-buffer-sizes)
  - [Shared Memory (SHM) — Same Host](#shared-memory-shm-same-host)
- [Batching](#batching)
- [Low-Latency Mode](#low-latency-mode)
- [Scouting and Discovery Overhead](#scouting-and-discovery-overhead)
  - [Reducing startup latency](#reducing-startup-latency)
  - [Gossip scouting](#gossip-scouting)
  - [ROS2 benefit](#ros2-benefit)
- [Worker Threads](#worker-threads)
- [Queue Size Tuning](#queue-size-tuning)
- [OS-Level Tuning](#os-level-tuning)
- [Common Anti-Patterns](#common-anti-patterns)
- [Sources](#sources)

## Baseline Numbers

Before tuning, know what the ceiling looks like on reference hardware (AMD Ryzen 5800X, 100 GbE):

| Scenario | Throughput / Latency |
|---|---|
| Peer-to-peer, 8-byte payload | >3.5M msg/s |
| Peer-to-peer, 1 MB payload | >45 Gb/s |
| Routed (via zenohd), 8-byte | ~3M msg/s |
| Zenoh-Pico, 8-byte | ~2.5M msg/s |
| P2P latency (backlogged, 64-byte) | 35 µs |
| Routed latency (one extra hop) | 70 µs |
| Zenoh-Pico unicast latency | 45 µs |
| Zenoh-Pico multicast latency | 15 µs |
| NTU P2P over network (multi-machine, 100 GbE) | ~16 µs |
| Zenoh-Pico (NTU, multi-machine, 100 GbE) | ~13 µs |

Versus competing protocols at 16 KB payload on 100 GbE: Zenoh ~50 Gbps, CycloneDDS ~14 Gbps, MQTT/Kafka ~5 Gbps.

Run your own benchmarks:
```bash
git clone https://github.com/eclipse-zenoh/zenoh.git && cd zenoh
cargo build --release --examples
./target/release/examples/z_sub_thr &
./target/release/examples/z_pub_thr 1024
```

Full suite: [ZettaScaleLabs/zenoh-perf](https://github.com/ZettaScaleLabs/zenoh-perf)

---

## Key Expression Design

This is the highest-leverage, zero-cost tuning step.

**Use `/` as the hierarchy separator, not `.`**

Zenoh's key expression language uses `/` as the hierarchy separator (`.` is not a Zenoh KE separator). Using well-formed KEs with `/` separators enables proper canonical-form optimization in the routing engine.

```
# Before (suboptimal)
sensor.imu.accel
robot.arm.joint.1

# After (optimal)
sensor/imu/accel
robot/arm/joint/1
```

**Avoid deep hierarchies for hot paths.** Matching cost grows with depth. A flat two-level key like `sensors/imu` is faster to match than `robot/platform/sensors/imu/accel/raw`.

**Avoid non-canonical patterns.** Zenoh rejects or penalizes patterns that require normalization at match time:
- Use `**` not `**/**`
- Use `*/**` not `**/*`
- Use `$*` not `$*$*`

---

## QoS: Priority and Congestion Control

### Priority Levels

Zenoh has 8 priority levels (0-7). Level 0 (`Control`) is reserved for internal protocol use and not available to user publishers. The 7 user-accessible levels, ordered highest to lowest:

| Priority | Enum | Typical use |
|---|---|---|
| 1 | `RealTime` | Hard real-time control |
| 2 | `InteractiveHigh` | Interactive, latency-critical |
| 3 | `InteractiveLow` | Interactive, moderate latency |
| 4 | `DataHigh` | High-importance sensor data |
| 5 | `Data` (default) | Normal data traffic |
| 6 | `DataLow` | Low-importance data |
| 7 | `Background` | Bulk transfers, uploads |

Set per publisher in Rust:
```rust
let publisher = session
    .declare_publisher("robot/control/cmd_vel")
    .priority(Priority::RealTime)
    .await?;
```

Per link (endpoint config), append to the endpoint string:
```
tcp/192.168.1.1:7447?prio=1-3;rel=1   # RealTime through InteractiveLow, reliable
tcp/192.168.1.1:7447?prio=6-7;rel=0   # DataLow + Background, best-effort
```

This lets you pin control traffic to a fast lane and bulk data to a slow lane over the same physical link.

### Congestion Control

Two modes, set per publisher or overridden globally via config:

| Mode | Behavior | Use when |
|---|---|---|
| `Drop` (default) | Drops message if queue is full | High-frequency sensor streams, point clouds, video |
| `Block` | Applies backpressure, blocks publisher | Command/control where loss is unacceptable |

Config override (overrides API settings for matched key expressions):
```json5
qos: {
  publication: [
    {
      key_exprs: ["robot/control/**"],
      config: {
        congestion_control: "block",
        priority: "real_time",
        express: true,
      }
    },
    {
      key_exprs: ["robot/camera/**"],
      config: {
        congestion_control: "drop",
        priority: "data_low",
      }
    }
  ]
}
```

`wait_before_drop` (default: 1000 µs) controls how long Drop mode waits before discarding. `wait_before_close` (default: 5000000 µs) controls how long Block mode waits before closing the session.

### Reliability

`Reliability` is currently a **marker**, not a retransmission mechanism. It signals intent and can guide link selection (e.g., route reliable traffic over TCP, best-effort over UDP):

```rust
publisher.reliability(Reliability::Reliable)   // TCP preferred
publisher.reliability(Reliability::BestEffort) // UDP acceptable
```

---

## Transport Selection

### Unicast vs. Multicast

| Transport | Latency | Throughput | Batching |
|---|---|---|---|
| Unicast (TCP/UDP) | 45 µs (Zenoh-Pico) | Saturates link | Yes |
| Multicast (UDP peer mode) | **15 µs** (Zenoh-Pico) | Lower | No |

Multicast achieves lower latency because it skips the unicast acknowledgement path. Multicast does support batching, but the effective batch size is limited by OS-dependent platform maximums (Linux/Windows: 65535 bytes, macOS: 9216 bytes). Use multicast for latency-sensitive, same-LAN deployments. Use unicast for throughput-critical paths.

Peer mode uses multicast scouting by default on `224.0.0.224:7446`. Disable it when not needed to reduce overhead in large deployments:
```json5
scouting: {
  multicast: { enabled: false }
}
```

### TCP Buffer Sizes

For high-throughput paths, the OS default TCP socket buffers (typically 128–256 KB) become a bottleneck. Increase them per endpoint:
```
tcp/192.168.1.1:7447#so_sndbuf=4194304;so_rcvbuf=4194304
```

Or set system-wide on Linux:
```bash
sysctl -w net.core.rmem_max=67108864
sysctl -w net.core.wmem_max=67108864
sysctl -w net.ipv4.tcp_rmem="4096 87380 67108864"
sysctl -w net.ipv4.tcp_wmem="4096 65536 67108864"
```

### Shared Memory (SHM) — Same Host

For publishers and subscribers on the same host, [SHM](shared-memory-complete-guide.md) provides zero-copy delivery and eliminates serialization cost. SHM has shown approximately 35% throughput improvements and approximately 600K additional msg/s in specific benchmarks.

SHM is enabled by default (`transport.shared_memory.enabled: true` in DEFAULT_CONFIG.json5). Both sender and receiver must have SHM support compiled in (the `shared-memory` feature) for the SHM transport to activate.

Both sender and receiver must have SHM enabled. If either side lacks it, Zenoh falls back to socket transport silently — verify with admin space or logs that SHM is actually in use.

---

## Batching

Zenoh batches small messages into a single network write to improve throughput. Default batch size is 65535 bytes. For multicast links, the effective batch size is OS-dependent (Linux/Windows: 65535 bytes, macOS: 9216 bytes, others: 8192 bytes) — this affects multicast only, not unicast. Batching is adaptive: it activates under back-pressure, not proactively.

```json5
transport: {
  link: {
    tx: {
      batch_size: 65535,
      queue: {
        batching: {
          enabled: true,
          time_limit: 1,  // max ms a message waits in batch under backpressure
        }
      }
    }
  }
}
```

**Latency vs. throughput tradeoff:** batching increases throughput but adds up to `time_limit` ms of latency. Set `time_limit: 0` to disable the wait (messages batch only if already queued, not by waiting).

**Express mode disables batching for a specific key expression.** Use it for control topics where latency matters more than throughput:
```json5
qos: {
  publication: [
    {
      key_exprs: ["robot/control/**"],
      config: {
        express: true,
      }
    }
  ]
}
```

In ROS2 bridge config:
```json5
pub_priorities: [".*/cmd_vel=1:express"]
```

---

## Low-Latency Mode

`lowlatency: true` bypasses the QoS priority queue entirely and sends messages directly from the calling thread without enqueueing. This removes scheduling jitter at the cost of no priority separation.

**Incompatible with `qos.enabled: true`.** You must explicitly disable QoS to use it:
```json5
transport: {
  unicast: {
    lowlatency: true,
    qos: { enabled: false },
  }
}
```

Use this only when all traffic on a session is equally latency-critical and you do not need priority differentiation.

---

## Scouting and Discovery Overhead

Scouting dominates startup latency in dynamic environments. In large deployments it also contributes to steady-state CPU load.

### Reducing startup latency

In client mode, the default scouting timeout is 3000 ms. In deployments with a known router, skip scouting entirely by providing explicit endpoints:
```json5
mode: "client",
connect: { endpoints: ["tcp/10.0.0.1:7447"] },
scouting: { timeout: 0 }
```

### Gossip scouting

Gossip propagates peer lists across hops. `multihop` defaults to `false` in DEFAULT_CONFIG.json5, so no action is required for typical stable deployments. If your deployment enables `multihop: true`, note that it floods the network with higher overhead — disable it in production with stable topologies.

### ROS2 benefit

In ROS2 deployments, replacing DDS discovery with Zenoh scouting reduces discovery traffic by 97–99.9% in large multi-robot systems. The bridge handles this automatically.

---

## Worker Threads

The Zenoh TX path uses a thread pool. The number of async worker threads is determined internally (formula: `1 + (num_cpus - 1) / 4`). This is not a configurable parameter in `DEFAULT_CONFIG.json5` — there is no `threads` key under `transport.link.tx`. The Zenoh runtime uses tokio's default thread pool configuration.

For high-fan-out router scenarios, OS-level CPU affinity and process priority may help more than configuration tuning.

---

## Queue Size Tuning

The TX queue has separate depth per priority level. All priority levels default to 2:

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

Increase `data` depth for bursty high-throughput publishers to absorb spikes without triggering congestion control. Increase `background` for bulk file transfer scenarios.

---

## OS-Level Tuning

For the best latency numbers (matching NTU benchmark conditions), apply the easyperf.net Linux tuning guide:

```bash
# Disable CPU frequency scaling
for cpu in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do
  echo performance > $cpu
done

# Disable hyperthreading (optional, for deterministic latency)
echo off > /sys/devices/system/cpu/smt/control

# Set CPU affinity for zenoh process
taskset -c 0,1 zenohd

# Real-time scheduling (requires CAP_SYS_NICE or root)
chrt -f 99 zenohd
```

Latency at low message rates is dominated by OS scheduler wakeup overhead (processes descheduled between messages). The backlogged scenario (messages sent as fast as possible) is the fair comparison point for protocol latency numbers.

---

## Common Anti-Patterns

| Anti-pattern | Problem | Fix |
|---|---|---|
| Key separator is `.` not `/` | Up to 2x CPU overhead in matching | Switch to `/` |
| SHM enabled on one side only | Falls back silently to socket | Enable on both sender and receiver |
| `lowlatency` + `qos.enabled` | Config error, session fails | Disable QoS when using lowlatency mode |
| Default scouting timeout with known router | 3-second startup delay | Set `scouting.timeout: 0`, use explicit endpoint |
| `Block` congestion control on sensor streams | Publisher stalls | Use `Drop` for high-rate data; `Block` only for control |
| Very deep key hierarchies on hot topics | Higher match cost | Flatten key structure |
| `multihop` gossip enabled | Excess discovery traffic | `multihop` defaults to `false`; only set if you intentionally enabled it |
| DDS bridge (`zenoh-bridge-dds`) for ROS2 | Capped at ~50 Hz in some configs | Use `zenoh-bridge-ros2dds` instead |

---

## Sources

- ZettaScale Blog: "Boosting Zenoh Performance" (2022)
- ZettaScale Blog: "Zenoh-Pico: Performance Deep Dive" (2022)
- NTU: "A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS" — Liang, Yuan, Lin (2023)
- Zenoh DEFAULT_CONFIG.json5 (configuration reference)
- GitHub issues: zenoh-bridge-ros2dds #192, #549, zenoh #1017
- Community FAQ and ROS Discourse discussions

## See Also

- [QoS Guide](qos-guide.md) — complete guide to priority levels, congestion control, and express mode for performance tuning
- [Shared Memory Complete Guide](shared-memory-complete-guide.md) — the zero-copy SHM path that gives the best same-host performance
- [Config Transport Link TX](config-transport-link-tx.md) — queue sizes, batch settings, and congestion control config
- [Config Transport SHM](config-transport-shm.md) — transport-level SHM optimization configuration
- [Wire Protocol Guide](wire-protocol-guide.md) — the protocol-level overhead analysis that explains Zenoh's performance advantage
- [Benchmarks](benchmarks.md) — reference throughput and latency numbers to compare against
