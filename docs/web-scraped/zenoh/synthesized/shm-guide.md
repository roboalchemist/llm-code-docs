# Zenoh Shared Memory (SHM) Guide

## Table of Contents

- [Overview](#overview)
- [When to Use SHM](#when-to-use-shm)
- [Build Requirements](#build-requirements)
  - [Rust](#rust)
  - [Python](#python)
  - [C / C++](#c-c)
- [Configuration](#configuration)
- [Rust API](#rust-api)
  - [Basic Rust Usage](#basic-rust-usage)
- [Python API](#python-api)
- [Limitations](#limitations)
  - [Same-Host Only](#same-host-only)
  - [Router Topology (Pre-1.0 limitation, partially resolved in 1.0)](#router-topology-pre-10-limitation-partially-resolved-in-10)
  - [NTU Benchmark Exclusion](#ntu-benchmark-exclusion)
  - [zenoh-pico](#zenoh-pico)
- [Performance](#performance)
- [Troubleshooting](#troubleshooting)

## Overview

Zenoh's Shared Memory (SHM) transport enables zero-copy pub/sub between processes on the same host. Instead of copying payload bytes through the network stack, the publisher writes data directly into a shared memory segment and sends only a lightweight descriptor to subscribers. Subscribers map the same segment and read the payload without any copy.

SHM support was present in pre-1.0 Zenoh releases and received significant improvements in the 1.x series. Zenoh 1.x includes a redesigned SHM subsystem with improved API and transport optimization features.

---

## When to Use SHM

SHM is beneficial when:

- Publisher and subscriber(s) are on the **same host** (different processes)
- **Payload is large** (kilobytes to megabytes) — the zero-copy benefit dominates serialization cost
- **Latency is critical** — avoiding kernel copies reduces end-to-end latency by tens of microseconds

SHM is **not applicable** when:

- Communicating across hosts (SHM is local-only)
- Using zenoh-pico (the embedded C implementation does not support SHM)
- The subscriber is connected through a router (see Limitations section)

---

## Build Requirements

SHM support is a compile-time feature. It is not included in default builds.

### Rust

Add the `shared-memory` feature to your `Cargo.toml`:

```toml
[dependencies]
zenoh = { version = "1.7", features = ["shared-memory"] }
```

### Python

Install from source with the `shared-memory` feature:

```bash
pip install eclipse-zenoh --no-binary :all: \
  --config-settings build-args="--features=zenoh/shared-memory"
```

The `zenoh.shm` module becomes available after this build:

```python
import zenoh.shm
```

### C / C++

Build zenoh-c with the `ZENOHC_BUILD_WITH_SHARED_MEMORY` CMake option:

```cmake
cmake -DZENOHC_BUILD_WITH_SHARED_MEMORY=true ..
```

---

## Configuration

SHM transport is configured under `transport.shared_memory` in the JSON5 config. Both publisher and subscriber must enable it.

```json5
transport: {
  shared_memory: {
    /// Enable SHM transport support. Announces SHM capability to peers.
    /// Both sides must have this true for SHM to activate.
    enabled: true,

    /// Initialization mode (default: "lazy")
    /// - "lazy": SHM subsystem starts on first SHM buffer use.
    ///   Zero startup overhead, but slight latency spike on first use.
    /// - "init": SHM subsystem starts at Session open.
    ///   Predictable latency at the cost of slightly longer startup.
    mode: "lazy",

    /// Implicit SHM optimization for large messages (only for SHM-compatible connections)
    transport_optimization: {
      /// Automatically put large messages into shared memory
      enabled: true,

      /// SHM arena/pool size in bytes (default: 16 MiB)
      pool_size: 16777216,

      /// Message size threshold in bytes above which implicit SHM is used (default: 3072 bytes = 3 KiB)
      message_size_threshold: 3072,
    }
  }
}
```

A probing procedure runs at session opening. If both peers have `enabled: true` and are co-located, SHM activates automatically. If the remote peer does not support SHM, the session falls back to normal serialized transport transparently.

---

## Rust API

The `zenoh-shm` crate provides the SHM API. Key types:

| Type | Crate | Description |
|------|-------|-------------|
| `ShmBufInner` | `zenoh-shm` | A zenoh buffer in shared memory |
| `ShmBufInfo` | `zenoh-shm` | Metadata/descriptor for an `ShmBufInner` |
| `ShmInitMode` | `zenoh-config` | Controls SHM initialization timing (`Lazy`/`Init`) |

The `zenoh-shm` crate exposes internal modules:

- `zenoh_shm::api` — high-level SHM provider API
- `zenoh_shm::posix_shm` — POSIX shared memory backend
- `zenoh_shm::header` — SHM segment header management
- `zenoh_shm::watchdog` — Liveness monitoring for SHM buffers
- `zenoh_shm::reader` — Subscriber-side SHM reader

Docs: https://docs.rs/zenoh-shm/latest/zenoh_shm/

### Basic Rust Usage

```rust
use zenoh::prelude::*;

#[tokio::main]
async fn main() {
    // Open session with SHM enabled (requires shared-memory feature)
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    // Publisher: allocate SHM buffer and publish
    let publisher = session.declare_publisher("demo/shm").await.unwrap();

    // With implicit SHM (low_latency config), large payloads are
    // automatically routed through shared memory for SHM-capable subscribers
    publisher.put(vec![0u8; 1_000_000]).await.unwrap();

    // Subscriber receives without copying when SHM-capable
    let subscriber = session.declare_subscriber("demo/shm").await.unwrap();
    while let Ok(sample) = subscriber.recv_async().await {
        // sample.payload() can be read directly from the SHM segment
        println!("Received {} bytes", sample.payload().len());
    }
}
```

---

## Python API

After installing with `shared-memory` feature, the `zenoh.shm` module is available.

```python
import zenoh
import zenoh.shm

# Open session (SHM activates automatically with co-located peers)
config = zenoh.Config()
session = zenoh.open(config)

# Publishing large payloads — SHM is used implicitly when both sides support it
pub = session.declare_publisher("demo/shm")
pub.put(bytes(1_000_000))  # 1 MB payload goes via SHM if subscriber is local

# Subscribing — payload is zero-copy when SHM is active
sub = session.declare_subscriber("demo/shm", lambda sample:
    print(f"Received {len(sample.payload.to_bytes())} bytes"))
```

The `zenoh.shm` module exposes automodule documentation via Sphinx:

```python
# See the module structure:
import zenoh.shm
help(zenoh.shm)
```

---

## Limitations

### Same-Host Only

SHM buffers cannot be forwarded across hosts. When a router forwards a publication, it serializes the payload and transmits it over the network transport — the zero-copy benefit is lost. SHM is strictly a same-host optimization.

### Router Topology (Pre-1.0 limitation, partially resolved in 1.0)

As of the 1.0.0 release, zenoh supports SHM only in clique topologies (direct peer-to-peer without router forwarding of the SHM buffer). The ZettaScale roadmap notes plans to extend SHM support to arbitrary router topologies and to allow third-party SHM provider integration:

> "Zenoh already supports Shared Memory and Zero copy, but as of today, that only works on clique topologies. Our goal for the next release is to support any topology and allow third parties to safely integrate shared memory providers."

Check the latest changelogs for the current status of topology-aware SHM.

### NTU Benchmark Exclusion

The widely-cited National Taiwan University (NTU) performance benchmark of Zenoh vs. MQTT, Kafka, and DDS deliberately excluded SHM to provide a fair protocol-level comparison:

> "NTU was interested in measuring the protocol efficiency and going through ICEOryx for Cyclone DDS or using Zenoh zero-copy support would kind of defeat the purpose."

SHM/zero-copy real-world throughput and latency gains will be significantly better than those benchmarks show for same-host scenarios with large payloads.

### zenoh-pico

The C implementation for embedded/constrained devices (`zenoh-pico`) does not support SHM. SHM is available in `zenoh-c` (built with `ZENOH_FEATURES=shared_memory`) but not in `zenoh-pico`.

---

## Performance

SHM is most impactful for:

- **Large payloads (>16KB)**: The copy saved becomes significant relative to serialization overhead
- **High-frequency publication**: Eliminates per-message kernel copies that accumulate at high rates
- **Ultra-low-latency applications**: ZettaScale notes SHM enables "ultra-low latency communication" and is required for the high-performance SHM API

For small payloads (<1KB), the overhead of SHM probing and descriptor exchange may negate the benefit. Benchmark your specific workload.

The `transport_optimization.pool_size` config option (default 16 MiB) controls the SHM arena size. The `transport_optimization.message_size_threshold` option (default 3072 bytes) controls the size above which messages are automatically placed in SHM. For applications publishing many concurrent large buffers, increase `pool_size`.

---

## Troubleshooting

**SHM not activating between two local processes:**
- Verify both processes have `transport.shared_memory.enabled: true`
- Verify the zenoh library was compiled with `--features=shared-memory` (Python: installed with `--no-binary`)
- Check logs for the SHM probing exchange at session open — look for `shm probe` log entries at `DEBUG` level

**Falling back to network transport silently:**
- This is by design — if one peer doesn't support SHM, zenoh falls back transparently
- To force SHM-only and detect mismatches, add an integration test that verifies the connection type

**Memory pool exhausted:**
- Increase `transport_optimization.pool_size` in config
- Ensure subscribers are consuming messages promptly (SHM buffers are held until the subscriber drops its reference)

## See Also

- [Shared Memory Complete Guide](shared-memory-complete-guide.md) — comprehensive internals, platform differences, allocation policies, and full API reference
- [Config Transport SHM](config-transport-shm.md) — the JSON5 configuration fields that control SHM behavior
- [Performance Tuning Guide](performance-tuning-guide.md) — when to use SHM and how to size the pool for your workload
