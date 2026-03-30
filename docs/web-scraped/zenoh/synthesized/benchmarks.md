# Zenoh Performance Benchmarks

## Table of Contents

- [Summary](#summary)
- [Throughput Benchmarks](#throughput-benchmarks)
  - [Zenoh (Rust) — Peer-to-Peer, 100 GbE](#zenoh-rust-peer-to-peer-100-gbe)
  - [Zenoh (Rust) — Routed (via zenoh router), 100 GbE](#zenoh-rust-routed-via-zenoh-router-100-gbe)
  - [Zenoh — Early Results (Intel Core i7 Laptop)](#zenoh-early-results-intel-core-i7-laptop)
  - [Zenoh — AMD Ryzen 7 3800X + 10 GbE Workstation](#zenoh-amd-ryzen-7-3800x-10-gbe-workstation)
  - [Zenoh-Pico — Embedded / Constrained Devices, 100 GbE](#zenoh-pico-embedded-constrained-devices-100-gbe)
  - [Zenoh-Pico — Microcontroller Boards](#zenoh-pico-microcontroller-boards)
- [Latency Benchmarks](#latency-benchmarks)
  - [Zenoh (Rust) — Peer-to-Peer Latency, 100 GbE](#zenoh-rust-peer-to-peer-latency-100-gbe)
  - [Zenoh-Pico — Latency](#zenoh-pico-latency)
  - [NTU Multi-Protocol Comparison — Latency (Network, 100 GbE)](#ntu-multi-protocol-comparison-latency-network-100-gbe)
- [Comparisons](#comparisons)
  - [Zenoh vs. DDS, MQTT, Kafka — Throughput (NTU 2023, 100 GbE, multi-machine)](#zenoh-vs-dds-mqtt-kafka-throughput-ntu-2023-100-gbe-multi-machine)
  - [Zenoh-Pico vs. Embedded Protocols](#zenoh-pico-vs-embedded-protocols)
  - [Wire Overhead](#wire-overhead)
  - [Notes on Comparison Fairness](#notes-on-comparison-fairness)
- [Methodology Notes](#methodology-notes)
  - [NTU 2023 Benchmark](#ntu-2023-benchmark)
  - [ZettaScale Internal Benchmarks](#zettascale-internal-benchmarks)
  - [Running Your Own Benchmarks](#running-your-own-benchmarks)
- [Sources](#sources)

## Summary

Zenoh is designed from the ground up for high performance across the full Cloud-to-Things continuum. Key characteristics:

- **Throughput**: Over 3.5M msg/s for small payloads (8 bytes); over 45 Gb/s for large payloads
- **Latency**: As low as 35 µs peer-to-peer; 70 µs via router; 5 µs for Zenoh-Pico
- **Wire overhead**: Minimum 5 bytes per data transmission (smallest of any comparable protocol)
- **Embedded footprint**: Zenoh-Pico fits in under 50 KB flash; as low as ~15 KB in tailored builds
- **Comparison headline**: In NTU benchmark — 3x higher throughput than DDS; 10x higher than Kafka and MQTT

---

## Throughput Benchmarks

### Zenoh (Rust) — Peer-to-Peer, 100 GbE

Hardware: AMD Ryzen 5800x, 32 GB RAM, 100 Gb Ethernet (3 workstations), Ubuntu, configured per [easyperf.net guide](https://easyperf.net/blog/2019/08/02/Perf-measurement-environment-on-Linux).

Source: ZettaScale blog post "Boosting Zenoh Performance" (~2022)

| Payload | zenoh-net API (msg/s) | zenoh API (msg/s) | Network saturation |
|---|---|---|---|
| 8 bytes | >3.5M msg/s | 2M msg/s | 100 Mb/s |
| 32 bytes | — | — | 1 Gb/s (zenoh-net) |
| 64 bytes | — | — | 1 Gb/s (zenoh) |
| 512 bytes | — | — | 10 Gb/s (zenoh-net) |
| 1024 bytes | — | — | 10 Gb/s (zenoh) |
| 128 KB+ | — | — | 40 Gb/s |
| 1 MB | >45 Gb/s | — | — |

### Zenoh (Rust) — Routed (via zenoh router), 100 GbE

Same hardware; publisher → router → subscriber across 3 machines.

| Payload | zenoh-net API (msg/s) | zenoh API (msg/s) | Network saturation |
|---|---|---|---|
| 8 bytes | 3M msg/s | 1.8M msg/s | 100 Mb/s |
| 64 bytes | — | — | 1 Gb/s |
| 1024 bytes | — | — | 10 Gb/s |
| Large | 20–30 Gb/s forwarded | — | — |

### Zenoh — Early Results (Intel Core i7 Laptop)

Source: Early zenoh blog post (Rust master branch, pre-1.0)

- **128-byte payload** reached **1 Gbps** throughput on a Linux laptop.

### Zenoh — AMD Ryzen 7 3800X + 10 GbE Workstation

Source: Zenoh Aithusa blog post

- **128-byte payload**: Reached 1 Gbps
- **1024-byte payload**: Reached 10 Gbps

### Zenoh-Pico — Embedded / Constrained Devices, 100 GbE

Hardware: Two workstations, AMD Ryzen 5800X @ 4.0 GHz, 32 GB RAM, 100 Gb Ethernet (Mellanox ConnectX-6 Dx), Ubuntu 20.04.3.

Source: ZettaScale blog "Zenoh-Pico: Performance Deep Dive"

| Payload | Throughput (unicast) | Notes |
|---|---|---|
| 8 bytes | ~2.5M msg/s | Saturates 100 Mb/s |
| 64 bytes | — | Saturates 1 Gb/s |
| 1024 bytes | — | Saturates 10 Gb/s |
| >8 KB | >25 Gbps | — |

Multicast transport is lower than unicast due to lack of message batching.

### Zenoh-Pico — Microcontroller Boards

Source: ZettaScale blog "Zenoh on Arduino / Zephyr"

| Board | Payload | Throughput |
|---|---|---|
| ESP32 (WiFi) | 8 bytes | >5.2k msg/s |
| nucleo-f767zi (10 Mb Ethernet) | 4096 bytes | ~9.2 Mbps (saturates 10 Mb link) |

Memory footprint:
- nucleo-f767zi: ~2.8% of flash
- reel_board: ~9.2% of flash
- ESP32: ~0.9% of flash

---

## Latency Benchmarks

### Zenoh (Rust) — Peer-to-Peer Latency, 100 GbE

Hardware: AMD Ryzen 5800x, 32 GB RAM, 100 GbE, 3 workstations.
Measurement: Backlogged scenario (messages sent back-to-back). Payload: 64 bytes.

- **P2P latency (backlogged)**: **35 µs** (both zenoh-net and zenoh APIs)
- **Routed latency (via zenoh router)**: **70 µs** — doubling due to the extra network hop

Note: Latency decreases as message rate increases (processes are descheduled at low rates by the OS, adding scheduling overhead).

### Zenoh-Pico — Latency

Hardware: Two workstations, AMD Ryzen 5800X, 100 GbE.

| Transport | Latency (one-way delay, backlogged, 16-byte payload) |
|---|---|
| Unicast | **45 µs** |
| Multicast (peer mode) | **15 µs** |

### NTU Multi-Protocol Comparison — Latency (Network, 100 GbE)

Source: NTU (National Taiwan University) research blog, 2023. Hardware: AMD Ryzen 7 5800X @ 4.0 GHz, 32 GB DDR4, 100 Gb Ethernet.

- **Zenoh peer-to-peer (network)**: ~10 µs
- **Zenoh-Pico**: ~5 µs (lowest overall)
- **CycloneDDS (network)**: ~12 µs (2 µs more than Zenoh P2P)
- On loopback: Zenoh and DDS are very close; Zenoh-Pico is slightly better.

Note from kydos: "For Zenoh-Pico, which does not support mesh-routing, its latency is 5 µs, which is the lowest overall."

---

## Comparisons

### Zenoh vs. DDS, MQTT, Kafka — Throughput (NTU 2023, 100 GbE, multi-machine)

Source: "A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS" — Liang, Yuan, Lin (NTU); also summarized at zenoh.io blog 2023-03-21.

Hardware: AMD Ryzen 7 5800X, 32 GB RAM, 100 Gb Ethernet.

| Protocol | 16 KB payload bitrate |
|---|---|
| Zenoh (peer-to-peer) | **~50 Gbps** |
| CycloneDDS | ~14 Gbps |
| MQTT (Mosquitto 2.0.15, QoS 0) | ~5 Gbps |
| Kafka (3.2.1) | ~5 Gbps |

Summary from kydos: "Zenoh outperforms DDS by 3x, and Kafka/MQTT by over 10x at 16 KB payload on 100 Gb Ethernet."

Peak throughput noted elsewhere: **67 Gbps** (Zenoh, large payload, 100 GbE).

### Zenoh-Pico vs. Embedded Protocols

Source: ZettaScale blog "Zenoh-Pico Deep Dive"

| Protocol | Relative throughput |
|---|---|
| Zenoh-Pico (unicast) | **1x (baseline)** |
| XRCE-DDS | ~10x worse (Zenoh is 10x better) |
| MQTT | ~40x worse (Zenoh is 40x better) |
| OPC-UA | ~55x worse (Zenoh is 55x better) |

Wire overhead comparison (data publish operation):
- Zenoh: **5 bytes** minimum overhead
- XRCE-DDS: 75% larger overhead than Zenoh
- MQTT: 64% larger overhead than Zenoh
- OPC-UA: 98% larger overhead than Zenoh

### Wire Overhead

Zenoh's minimum wire overhead per data transmission is **5 bytes**, which is the smallest of any protocol in the comparison set.

### Notes on Comparison Fairness

Community discussion (from ROS Discourse, 2023) raised the following methodological points:

- NTU used RELIABLE QoS for DDS, which penalizes DDS throughput relative to BEST_EFFORT. The Zenoh team responded that for camera/point-cloud topics, BEST_EFFORT is common practice, and the settings were reasonable for the test.
- DDS shared memory (IceOryx) was not tested; Zenoh's own zero-copy SHM was similarly excluded to keep the comparison at the protocol level.
- On the Y axis of NTU charts: the scale is large (one tick = ~10 Gbps), so lines that look close may differ by tens of Gbps.

---

## Methodology Notes

### NTU 2023 Benchmark

- **Hardware**: AMD Ryzen 7 5800X @ 4.0 GHz, 8-Core/16-thread, 32 GiB DDR4 3200 MHz, 100 Gb Ethernet
- **Versions**: Zenoh (peer mode + router mode), CycloneDDS, Mosquitto 2.0.15 (MQTT), Kafka 3.2.1
- **Setup**: Two-machine scenario (publisher and subscriber on separate machines; broker/router on a third for brokered protocols)
- **Measurement guide**: [easyperf.net Linux perf environment guide](https://easyperf.net/blog/2019/08/02/Perf-measurement-environment-on-Linux)
- **Code**: Available at [zenoh-perf/comparison](https://github.com/ZettaScaleLabs/zenoh-perf/tree/master/comparison)

### ZettaScale Internal Benchmarks

- **Hardware**: AMD Ryzen 5800X / 5800x, 32 GB RAM, 100 GbE (Mellanox ConnectX-6 Dx), Ubuntu 20.04, Kernel 5.4.0
- **Latency metric**: One-way delay (not RTT), backlogged scenario (messages sent as fast as possible)
- **Payload for latency**: 64 bytes (same as ICMP)
- **Reproducibility**: Tests are provided as examples in the main zenoh distribution (`zn_pub_thr`, `zn_sub_thr`, latency examples)

### Running Your Own Benchmarks

```bash
git clone https://github.com/eclipse-zenoh/zenoh.git
cd zenoh
cargo build --release --examples
# Throughput subscriber:
./target/release/examples/zn_sub_thr
# Throughput publisher (payload size 1024):
./target/release/examples/zn_pub_thr 1024
```

Full performance test suite: [ZettaScaleLabs/zenoh-perf](https://github.com/ZettaScaleLabs/zenoh-perf)

---

## Sources

- [ZettaScale Blog: Boosting Zenoh Performance (2022)](https://zenoh.io/blog/) — peer-to-peer and routed throughput/latency
- [ZettaScale Blog: Zenoh-Pico Deep Dive (2022)](https://zenoh.io/blog/) — embedded throughput/latency vs. XRCE-DDS, MQTT, OPC-UA
- [ZettaScale Blog: Zenoh on Arduino/Zephyr (2021)](https://zenoh.io/blog/) — microcontroller benchmarks
- [NTU Blog / Research Paper: "A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS" — Liang, Yuan, Lin (2023)](https://zenoh.io/blog/2023-03-21-zenoh-vs-mqtt-kafka-dds/)
- [ROS Discourse discussion thread (2023)](https://discourse.ros.org) — methodology discussion, community commentary
- [ZettaScale Blog: Performance Evaluation on Rust Async Frameworks (2022)](https://zenoh.io/blog/) — Rust async RTT latency (async-std vs. Tokio vs. smol)
- Research paper: "Automotive Middleware Performance: Comparison of FastDDS, Zenoh and vSomeIP" (2022, IEEE VTC)
- Research paper: "Latency Analysis of ROS2 Multi-Node Systems" — Kronauer et al. (2021)

## See Also

- [Performance Tuning Guide](performance-tuning-guide.md) — how to configure Zenoh to approach these benchmark numbers in production
- [Comparison Guide](comparison-guide.md) — protocol-level feature comparison alongside the throughput and latency numbers
