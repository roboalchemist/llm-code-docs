# zenoh-pico vs zenoh-c vs zenoh (Rust): Comprehensive Comparison Guide

## Table of Contents

- [Overview](#overview)
- [zenoh-pico: Embedded C for MCU-class Devices](#zenoh-pico-embedded-c-for-mcu-class-devices)
  - [Target Platforms](#target-platforms)
  - [Pure C, No C++ Required](#pure-c-no-c-required)
  - [Build System](#build-system)
- [zenoh-c: Full C Bindings for Systems with a Full OS](#zenoh-c-full-c-bindings-for-systems-with-a-full-os)
  - [What zenoh-c Is](#what-zenoh-c-is)
  - [Build Requirements](#build-requirements)
  - [zenoh-c Target Use Cases](#zenoh-c-target-use-cases)
  - [Feature Flags (cargo features)](#feature-flags-cargo-features)
- [Feature Matrix](#feature-matrix)
- [Memory Model](#memory-model)
  - [zenoh-pico: Compile-Time Buffer Sizing](#zenoh-pico-compile-time-buffer-sizing)
  - [zenoh-pico: Application-Level Memory](#zenoh-pico-application-level-memory)
  - [zenoh-c: Standard Rust Heap](#zenoh-c-standard-rust-heap)
  - [Multicast Batch Size Compatibility](#multicast-batch-size-compatibility)
- [Z_FEATURE_* Flags in zenoh-pico](#z_feature_-flags-in-zenoh-pico)
  - [Core Messaging Features](#core-messaging-features)
  - [Transport Features](#transport-features)
  - [Threading and I/O](#threading-and-io)
  - [Protocol and Optimization](#protocol-and-optimization)
  - [Feature Dependencies Summary](#feature-dependencies-summary)
  - [Minimal Footprint Configuration](#minimal-footprint-configuration)
- [Runtime Config Parameters in zenoh-pico](#runtime-config-parameters-in-zenoh-pico)
  - [Session Configuration](#session-configuration)
  - [Scouting Configuration](#scouting-configuration)
  - [TLS Configuration](#tls-configuration)
  - [Compile-Time Constants (not runtime-configurable)](#compile-time-constants-not-runtime-configurable)
- [API Differences: zenoh-pico vs zenoh-c](#api-differences-zenoh-pico-vs-zenoh-c)
  - [Ownership Model (both libraries)](#ownership-model-both-libraries)
  - [Task Model: zenoh-pico](#task-model-zenoh-pico)
  - [Task Model: zenoh-c](#task-model-zenoh-c)
  - [Error Handling](#error-handling)
  - [Config Insertion](#config-insertion)
  - [Publish/Subscribe Pattern Comparison](#publishsubscribe-pattern-comparison)
- [When to Use Each](#when-to-use-each)
  - [Use zenoh-pico when:](#use-zenoh-pico-when)
  - [Use zenoh-c when:](#use-zenoh-c-when)
  - [Use zenoh (Rust) when:](#use-zenoh-rust-when)
  - [Quick decision tree:](#quick-decision-tree)
- [Performance](#performance)
  - [zenoh-pico](#zenoh-pico)
  - [zenoh-c](#zenoh-c)
  - [zenoh (Rust)](#zenoh-rust)
- [Serial Transport: MCU to zenoh Router Setup](#serial-transport-mcu-to-zenoh-router-setup)
  - [Architecture](#architecture)
  - [Step 1: zenoh-pico on the MCU](#step-1-zenoh-pico-on-the-mcu)
  - [Step 2: RPi Pico Serial Connection](#step-2-rpi-pico-serial-connection)
  - [Step 3: STM32 ThreadX Serial](#step-3-stm32-threadx-serial)
  - [Step 4: zenoh Router on Linux Host](#step-4-zenoh-router-on-linux-host)
  - [Step 5: Verify End-to-End](#step-5-verify-end-to-end)
  - [Serial Transport Config Reference](#serial-transport-config-reference)
- [Debugging](#debugging)
  - [zenoh-pico Debug Logs](#zenoh-pico-debug-logs)
  - [Common Issues](#common-issues)

## Overview

Zenoh has three primary implementation targets, each designed for a different class of hardware:

| Implementation | Language | Target | Binary Footprint |
|---|---|---|---|
| **zenoh-pico** | Pure C (C99/C11) | Microcontrollers, RTOS, bare-metal | ~40KB min, ~15KB stripped |
| **zenoh-c** | C (wrapping Rust) | Linux/macOS/Windows with full OS | ~5–20MB (Rust runtime + zenoh) |
| **zenoh (Rust)** | Rust | Any platform with Rust support | ~5–20MB |

The key decision is whether your target has a full operating system (file system, heap, pthreads). If not, use zenoh-pico. If yes, use zenoh-c or zenoh directly.

---

## zenoh-pico: Embedded C for MCU-class Devices

### Target Platforms

zenoh-pico is the right choice when your hardware is constrained — no Linux kernel, limited RAM (typically <256KB), and often running a real-time operating system or bare-metal firmware.

**Supported (RT)OS and transport combinations:**

| Platform | UDP (unicast/multicast) | TCP | Serial | BLE | WebSocket |
|---|---|---|---|---|---|
| Unix/Linux | Yes | Yes | No | No | No |
| Windows | Yes | Yes | No | No | No |
| Zephyr RTOS | Yes | Yes | Yes | No | No |
| Arduino | Yes | Yes | Yes | Yes (Serial profile) | No |
| ESP-IDF (ESP32) | Yes | Yes | Yes | No | No |
| MbedOS (STM32, etc.) | Yes | Yes | Yes | No | No |
| OpenCR (ROS robotics) | Yes | Yes | No | No | No |
| Emscripten (WASM) | No | No | No | No | Yes |
| FreeRTOS+TCP | Yes (unicast only) | Yes | No | No | No |
| Raspberry Pi Pico (RP2040) | Yes | Yes | Yes | No | No |

**Network layer support:**

- **IPv4** — all platforms
- **IPv6** — Unix, Windows, Zephyr, Arduino, ESP-IDF, MbedOS, Emscripten
- **6LoWPAN** — Unix, Zephyr (Thread networks)

**Data link / physical layer:**

- **WiFi** — most platforms
- **Ethernet** — most platforms
- **Serial (UART)** — Zephyr, Arduino, ESP-IDF, MbedOS, RPi Pico
- **USB CDC** — RPi Pico (experimental, requires `Z_FEATURE_LINK_SERIAL_USB` + `Z_FEATURE_UNSTABLE_API`)
- **Bluetooth** (Serial profile) — Arduino only

### Pure C, No C++ Required

zenoh-pico is written in C99/C11 with no C++ dependencies. It compiles with standard GCC or Clang cross-compilers for ARM Cortex-M, RISC-V, Xtensa (ESP32), and others. This makes it compatible with toolchains that do not ship a C++ standard library (bare-metal newlib-nano configurations, for example).

### Build System

zenoh-pico uses CMake as its primary build system. It also integrates with PlatformIO for Arduino/ESP-IDF/Zephyr/MbedOS projects.

**Basic Unix build:**

```bash
cd zenoh-pico
make                   # Release build
BUILD_TYPE=Debug make  # Debug build with symbols
make install           # Install to /usr/local
```

**PlatformIO integration (platformio.ini):**

```ini
[env:esp32]
platform = espressif32
board = az-delivery-devkit-v4
framework = arduino
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico

# Override buffer sizes for constrained devices
board_build.cmake_extra_args =
  -DBATCH_UNICAST_SIZE=1024
  -DFRAG_MAX_SIZE=2048
  -DZ_FEATURE_LINK_SERIAL=1
```

**Zephyr** targets are built via PlatformIO (not native CMake):
```bash
# Zephyr / FreeRTOS via PlatformIO
platformio init -b <board>
platformio run
```

**Raspberry Pi Pico** builds use the examples directory:
```bash
cd examples/rpi_pico
cmake -Bbuild -DPICO_BOARD="pico" \
      -DWIFI_SSID=myssid -DWIFI_PASSWORD=mypassword \
      -DZENOH_CONFIG_MODE=client \
      -DZENOH_CONFIG_CONNECT="tcp/192.168.1.100:7447"
cmake --build build
```

See the zenoh-pico README for full platform-specific build instructions.

---

## zenoh-c: Full C Bindings for Systems with a Full OS

### What zenoh-c Is

zenoh-c is a C API that wraps the full Rust zenoh implementation. It is **not** a reimplementation — it compiles zenoh (Rust) into a native library and exposes all functionality through a C header interface. This means:

- **All features of Rust zenoh are available** — QUIC, SHM, TLS, ACL, admin space, all transports
- **Performance is identical** to Rust zenoh — the C wrapper is thin FFI with zero overhead on the hot path
- **Rust toolchain required at build time** — the Rust compiler and Cargo are needed to compile zenoh-c, but the resulting `libzenohc.so` is a standard shared library with no Rust runtime dependency at link time

### Build Requirements

```bash
# Install Rust (required)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup update

# Build zenoh-c
mkdir build && cd build
cmake ../zenoh-c
cmake --build . --config Release

# Enable Shared Memory support (Linux only)
cmake -DZENOHC_BUILD_WITH_SHARED_MEMORY=true ../zenoh-c
cmake --build . --config Release

# Enable unstable API
cmake -DZENOHC_BUILD_WITH_UNSTABLE_API=true ../zenoh-c
```

### zenoh-c Target Use Cases

- **Raspberry Pi (any model)** running Linux — use zenoh-c, not zenoh-pico
- **Embedded Linux** (Yocto, Buildroot, OpenWRT) — use zenoh-c
- **Language FFI** — Python (cffi/ctypes), Go (cgo), Java (JNI), .NET (P/Invoke), Ruby
- **Legacy C codebases** on Linux/macOS/Windows that need zenoh integration
- **Any scenario requiring SHM, QUIC, or TLS** — these are only in zenoh-c/Rust

### Feature Flags (cargo features)

zenoh-c inherits all feature flags from the underlying Rust zenoh crate. To customize which transports are compiled in:

```bash
cmake ../zenoh-c -DZENOHC_CARGO_FLAGS="--no-default-features;--features=transport_tcp,transport_udp"
```

Available features (from `Cargo.toml`) include: `transport_tcp`, `transport_udp`, `transport_tls`, `transport_quic`, `transport_ws`, `transport_unixsock-stream`, `transport_unixpipe`, `transport_serial`, `transport_vsock`, `transport_multilink`, `transport_compression`, `auth_pubkey`, `auth_usrpwd`, `shared-memory`, `stats`, `unstable`, `default`. Note: there is no separate `transport_shm` feature; shared memory support is enabled via the `shared-memory` feature.

---

## Feature Matrix

| Feature | zenoh-pico | zenoh-c | zenoh (Rust) |
|---|---|---|---|
| **Core messaging** | | | |
| Publisher | Yes | Yes | Yes |
| Subscriber | Yes | Yes | Yes |
| Queryable | Yes | Yes | Yes |
| Get (query) | Yes | Yes | Yes |
| Advanced Publisher (cache, history) | Yes (unstable) | Yes (unstable) | Yes (unstable) |
| Advanced Subscriber (recovery, replay) | Yes (unstable) | Yes (unstable) | Yes (unstable) |
| Liveliness tokens | Yes | Yes | Yes |
| Liveliness subscriber | Yes | Yes | Yes |
| Matching listeners | Yes | Yes | Yes |
| **Session modes** | | | |
| Client mode | Yes | Yes | Yes |
| Peer mode | Yes | Yes | Yes |
| Router mode | No | No | Yes (zenohd) |
| **Transports** | | | |
| TCP | Yes | Yes | Yes |
| UDP unicast | Yes | Yes | Yes |
| UDP multicast | Yes | Yes | Yes |
| Serial (UART) | Yes (opt-in) | Yes (opt-in, `transport_serial` feature) | Yes |
| Bluetooth (BLE/Serial) | Yes (opt-in, Arduino only) | No | No |
| Raw Ethernet | Yes (opt-in) | No | No |
| TLS | Yes (opt-in, MbedTLS) | Yes | Yes |
| QUIC | No | Yes | Yes |
| WebSocket | Yes (opt-in) | Yes | Yes |
| Unix domain socket | No | Yes | Yes |
| **Shared memory** | | | |
| SHM transport | No | Yes (opt-in) | Yes (opt-in) |
| **Scouting** | | | |
| Multicast scouting (UDP) | Yes | Yes | Yes |
| Gossip scouting | No | Yes | Yes |
| **Protocols / integrations** | | | |
| Storage plugin | No | Via zenoh router | Via zenoh router |
| ACL / security | No | Yes | Yes |
| Admin space (`@/...`) | Yes (unstable) | Yes | Yes |
| ROS2/DDS bridge | No | Via plugin | Via plugin |
| **Build system** | | | |
| Pure C (no Rust) | Yes | No (Rust required to build) | No |
| Static library | Yes | Yes | Yes |
| Shared library | Yes | Yes | Yes |
| PlatformIO | Yes | No | No |

**Notes:**
- zenoh-pico's Serial and Bluetooth links are disabled by default; enable with `Z_FEATURE_LINK_SERIAL=1` and `Z_FEATURE_LINK_BLUETOOTH=1`
- zenoh-pico's TLS uses MbedTLS 2.x/3.x (not OpenSSL)
- zenoh-pico supports only a subset of gossip scouting (unicast-based, not full gossip)
- zenoh-pico does not implement a router — it can run as a client connecting to a zenoh router, or as a peer in a P2P group

---

## Memory Model

### zenoh-pico: Compile-Time Buffer Sizing

zenoh-pico uses fixed-size buffers configured at compile time. There is no hidden heap allocation for protocol framing — all wire-level buffers are allocated from the sizes you specify at build time.

**Key buffer parameters (set via CMake):**

| Parameter | CMake Flag | Default | Description |
|---|---|---|---|
| `Z_FRAG_MAX_SIZE` | `FRAG_MAX_SIZE` | 4096 bytes | Maximum size of a message that can be fragmented across multiple packets. Messages larger than this cannot be sent. |
| `Z_BATCH_UNICAST_SIZE` | `BATCH_UNICAST_SIZE` | 2048 bytes | Maximum packet size for client-mode (unicast) communication. |
| `Z_BATCH_MULTICAST_SIZE` | `BATCH_MULTICAST_SIZE` | 2048 bytes | Maximum packet size for peer-mode (multicast) communication. |

**Reducing memory for tight constraints:**

```bash
# Minimal MCU configuration
cmake .. \
  -DFRAG_MAX_SIZE=1024 \
  -DBATCH_UNICAST_SIZE=512 \
  -DBATCH_MULTICAST_SIZE=512
```

Or in `platformio.ini`:

```ini
board_build.cmake_extra_args =
  -DBATCH_UNICAST_SIZE=1024
  -DFRAG_MAX_SIZE=2048
```

**When opening a session fails on a microcontroller**, the most common cause is that the default buffer sizes exceed the available RAM. Reduce `BATCH_UNICAST_SIZE` and `FRAG_MAX_SIZE` until the session opens successfully.

### zenoh-pico: Application-Level Memory

The `z_owned_*` types in the zenoh-pico API use the system allocator (malloc/free) for variable-length data like key expressions, payloads, and strings. On platforms with a working heap (most RTOS with heap configured), this is fine. On bare-metal without heap, you would need to provide a custom malloc or avoid dynamic strings entirely.

For maximum static allocation, keep key expressions and payloads small enough to fit in the batch buffers and use `z_view_*` types (non-owning views into existing memory) wherever possible.

### zenoh-c: Standard Rust Heap

zenoh-c uses the Rust allocator (the system allocator — `glibc malloc` on Linux, `malloc` on macOS/Windows; modern Rust does not use jemalloc by default). Memory is managed through `z_owned_*` / `z_loaned_*` semantics identical to zenoh-pico's API style.

### Multicast Batch Size Compatibility

When zenoh-pico peers communicate via UDP multicast, all nodes must use the same batch size. The defaults differ by platform:

- Linux/Windows: 65535 bytes
- macOS: 9216 bytes
- Other: 8192 bytes

If mixing zenoh-pico with other zenoh implementations on multicast, configure `transport/link/tx/batch_size` in the router/peer configuration to match `BATCH_MULTICAST_SIZE` on the pico side.

---

## Z_FEATURE_* Flags in zenoh-pico

Every feature in zenoh-pico can be individually enabled or disabled at compile time via CMake. Disabling features reduces binary size and eliminates dead code. The flags are defined in `include/zenoh-pico/config.h` (generated from `config.h.in`).

### Core Messaging Features

| Flag | Default | Description |
|---|---|---|
| `Z_FEATURE_PUBLICATION` | 1 (on) | Enable publisher declarations and `z_publisher_put()` / `z_put()`. Required for publishing. |
| `Z_FEATURE_SUBSCRIPTION` | 1 (on) | Enable subscriber declarations and sample callbacks. Required for subscribing. |
| `Z_FEATURE_QUERY` | 1 (on) | Enable `z_get()` (initiating queries). Required to retrieve data from queryables. |
| `Z_FEATURE_QUERYABLE` | 1 (on) | Enable queryable declarations and query handlers. Required to serve queries. |
| `Z_FEATURE_LIVELINESS` | 1 (on) | Enable liveliness token declarations and liveliness subscribers. Adds ~2KB code. |
| `Z_FEATURE_INTEREST` | 1 (on) | Enable interest/matching infrastructure. Required for `Z_FEATURE_MATCHING`. |
| `Z_FEATURE_MATCHING` | 1 (on) | Enable matching status notifications. Depends on `Z_FEATURE_INTEREST`. |
| `Z_FEATURE_ADVANCED_PUBLICATION` | 0 (off) | Cache-based publication with history/replay. Requires `Z_FEATURE_UNSTABLE_API`, `Z_FEATURE_PUBLICATION`, `Z_FEATURE_LIVELINESS`. |
| `Z_FEATURE_ADVANCED_SUBSCRIPTION` | 0 (off) | Advanced subscriber with message recovery and replay. Requires `Z_FEATURE_UNSTABLE_API`, `Z_FEATURE_SUBSCRIPTION`, `Z_FEATURE_LIVELINESS`, `Z_FEATURE_MULTI_THREAD`. |
| `Z_FEATURE_LOCAL_SUBSCRIBER` | 0 (off) | Allow subscribers to receive samples published on the same session (loopback). Off by default to save session processing. |
| `Z_FEATURE_LOCAL_QUERYABLE` | 0 (off) | Allow queries to be served by queryables on the same session. |
| `Z_FEATURE_ADMIN_SPACE` | 0 (off) | Enable `@/...` admin key expression namespace for introspection. Requires `Z_FEATURE_UNSTABLE_API`. |

### Transport Features

| Flag | Default | Description |
|---|---|---|
| `Z_FEATURE_LINK_TCP` | 1 (on) | Enable TCP transport links. |
| `Z_FEATURE_LINK_UDP_UNICAST` | 1 (on) | Enable UDP unicast transport links. Disabling also disables scouting (`Z_FEATURE_SCOUTING`). |
| `Z_FEATURE_LINK_UDP_MULTICAST` | 1 (on) | Enable UDP multicast transport links. Required for peer-mode multicast. |
| `Z_FEATURE_LINK_SERIAL` | 0 (off) | Enable UART serial transport. Required for MCU-to-router serial connections. |
| `Z_FEATURE_LINK_SERIAL_USB` | 0 (off) | Enable USB CDC serial (RPi Pico). Requires `Z_FEATURE_UNSTABLE_API`. |
| `Z_FEATURE_LINK_BLUETOOTH` | 0 (off) | Enable Bluetooth Serial Profile transport (Arduino only). |
| `Z_FEATURE_LINK_WS` | 0 (off) | Enable WebSocket transport (Emscripten target). |
| `Z_FEATURE_LINK_TLS` | 0 (off) | Enable TLS transport via MbedTLS 2.x or 3.x. |
| `Z_FEATURE_RAWETH_TRANSPORT` | 0 (off) | Enable raw Ethernet frame transport (Layer 2, no IP). |
| `Z_FEATURE_UNICAST_TRANSPORT` | 1 (on) | Enable unicast transport mode (client mode sessions). |
| `Z_FEATURE_MULTICAST_TRANSPORT` | 1 (on) | Enable multicast transport mode (peer mode sessions). |
| `Z_FEATURE_SCOUTING` | 1 (on) | Enable UDP multicast scouting for peer/router discovery. Automatically disabled when `Z_FEATURE_LINK_UDP_UNICAST=0`. |

### Threading and I/O

| Flag | Default | Description |
|---|---|---|
| `Z_FEATURE_MULTI_THREAD` | 1 (on) | Enable POSIX-thread support. When enabled, `zp_start_read_task()` / `zp_start_lease_task()` spawn background threads. When disabled, the application must call `zp_read()` and `zp_send_keep_alive()` manually in its main loop. |
| `Z_FEATURE_BATCH_TX_MUTEX` | 0 (off) | Lock a mutex at the per-batch transmit level (finer-grained than session mutex). |
| `Z_FEATURE_BATCH_PEER_MUTEX` | 0 (off) | Lock a mutex at the per-peer level for batch transmission. |
| `Z_FEATURE_UNICAST_PEER` | 1 (on) | Enable unicast peer mode (peer-to-peer without multicast). Requires `Z_FEATURE_MULTI_THREAD`. |

### Protocol and Optimization

| Flag | Default | Description |
|---|---|---|
| `Z_FEATURE_FRAGMENTATION` | 1 (on) | Enable message fragmentation. Required to send messages larger than the batch size. Disable on extremely constrained targets if all messages fit in one batch. |
| `Z_FEATURE_ENCODING_VALUES` | 1 (on) | Include the full set of standard MIME encoding constants. Disable to save a few hundred bytes if you only use raw bytes. |
| `Z_FEATURE_TCP_NODELAY` | 1 (on) | Set `TCP_NODELAY` on all TCP sockets (disable Nagle algorithm). Reduces latency at cost of slightly higher packet count. |
| `Z_FEATURE_BATCHING` | 1 (on) | Enable message batching to improve throughput. |
| `Z_FEATURE_SESSION_CHECK` | 1 (on) | Validate that publishers/queriers are used with the same session they were declared on. Disable on single-session embedded applications to save a pointer check. |
| `Z_FEATURE_AUTO_RECONNECT` | 1 (on) | Automatically attempt to reconnect after transport failure. |
| `Z_FEATURE_RX_CACHE` | 0 (off) | Cache recently received message sequence numbers to detect duplicates (size configured by `Z_RX_CACHE_SIZE`). |
| `Z_FEATURE_MULTICAST_DECLARATIONS` | 0 (off) | Propagate resource declarations over multicast (experimental). |
| `Z_FEATURE_PERIODIC_TASKS` | 0 (off) | Enable periodic scheduler. Automatically enabled when advanced pub/sub is enabled. Requires `Z_FEATURE_UNSTABLE_API`. |
| `Z_FEATURE_UNSTABLE_API` | 0 (off) | Enable unstable/experimental API surface. Required for admin space, periodic tasks, advanced pub/sub, USB serial. |

### Feature Dependencies Summary

```
Z_FEATURE_MATCHING         → requires Z_FEATURE_INTEREST
Z_FEATURE_UNICAST_PEER     → requires Z_FEATURE_MULTI_THREAD
Z_FEATURE_SCOUTING         → requires Z_FEATURE_LINK_UDP_UNICAST
Z_FEATURE_LINK_SERIAL_USB  → requires Z_FEATURE_UNSTABLE_API
Z_FEATURE_ADMIN_SPACE      → requires Z_FEATURE_UNSTABLE_API
Z_FEATURE_PERIODIC_TASKS   → requires Z_FEATURE_UNSTABLE_API
Z_FEATURE_ADVANCED_PUBLICATION → requires UNSTABLE_API + PUBLICATION + LIVELINESS
Z_FEATURE_ADVANCED_SUBSCRIPTION → requires UNSTABLE_API + SUBSCRIPTION + LIVELINESS + MULTI_THREAD
```

### Minimal Footprint Configuration

To achieve the smallest binary (suitable for very constrained MCUs, ~15–20KB):

```cmake
cmake .. \
  -DZ_FEATURE_MULTI_THREAD=0 \
  -DZ_FEATURE_LIVELINESS=0 \
  -DZ_FEATURE_INTEREST=0 \
  -DZ_FEATURE_MATCHING=0 \
  -DZ_FEATURE_QUERY=0 \
  -DZ_FEATURE_QUERYABLE=0 \
  -DZ_FEATURE_ENCODING_VALUES=0 \
  -DZ_FEATURE_FRAGMENTATION=0 \
  -DZ_FEATURE_LINK_UDP_MULTICAST=0 \
  -DZ_FEATURE_MULTICAST_TRANSPORT=0 \
  -DZ_FEATURE_SCOUTING=0 \
  -DZ_FEATURE_LINK_TCP=1 \
  -DZ_FEATURE_LINK_SERIAL=1 \
  -DZ_FEATURE_PUBLICATION=1 \
  -DZ_FEATURE_SUBSCRIPTION=1 \
  -DFRAG_MAX_SIZE=512 \
  -DBATCH_UNICAST_SIZE=512 \
  -DBATCH_MULTICAST_SIZE=512
```

---

## Runtime Config Parameters in zenoh-pico

These parameters are set at runtime via `zp_config_insert()` before opening a session, using the key constants defined in `config.h`.

### Session Configuration

| Key Constant | Key Byte | Type | Default | Description |
|---|---|---|---|---|
| `Z_CONFIG_MODE_KEY` | 0x40 | string | `"client"` | Session mode. Valid: `"client"` (connects to router), `"peer"` (direct P2P). |
| `Z_CONFIG_CONNECT_KEY` | 0x41 | string | none | Endpoint to connect to. E.g. `"tcp/192.168.1.100:7447"`. Used in both client mode (connect to router) and peer mode (connect to peer). |
| `Z_CONFIG_LISTEN_KEY` | 0x42 | string | none | Endpoint to listen on. E.g. `"tcp/0.0.0.0:7447"`. Only one listen endpoint is supported in zenoh-pico. |
| `Z_CONFIG_USER_KEY` | 0x43 | string | none | Username for authentication. |
| `Z_CONFIG_PASSWORD_KEY` | 0x44 | string | none | Password for authentication. |
| `Z_CONFIG_SESSION_ZID_KEY` | 0x49 | UUID (128-bit hex) | auto-generated | Fixed Zenoh session ID. Use when you need a stable, deterministic session identity. |
| `Z_CONFIG_ADD_TIMESTAMP_KEY` | 0x4A | bool string | `"false"` | Automatically attach a timestamp to all published samples. Valid: `"true"`, `"false"`. (Currently unused in zenoh-pico.) |

### Scouting Configuration

| Key Constant | Key Byte | Type | Default | Description |
|---|---|---|---|---|
| `Z_CONFIG_MULTICAST_SCOUTING_KEY` | 0x45 | bool string | `"true"` | Enable/disable UDP multicast scouting for router/peer discovery. |
| `Z_CONFIG_MULTICAST_LOCATOR_KEY` | 0x46 | endpoint string | `"udp/224.0.0.224:7446"` | Multicast group and port for scouting. |
| `Z_CONFIG_SCOUTING_TIMEOUT_KEY` | 0x47 | int (ms) string | `"1000"` | Time in milliseconds to wait for a router during scouting before failing `z_open()`. Increase on slow networks. |
| `Z_CONFIG_SCOUTING_WHAT_KEY` | 0x48 | bitmask string | `"3"` | What entities to find: 1=router, 2=peer, 3=both (bitmask of `z_whatami_t`). |

### TLS Configuration

| Key Constant | Key Byte | Description |
|---|---|---|
| `Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_KEY` | 0x4B | Path to root CA certificate file. |
| `Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_BASE64_KEY` | 0x4C | Base64-encoded root CA certificate. |
| `Z_CONFIG_TLS_LISTEN_PRIVATE_KEY_KEY` | 0x4D | Path to server private key file. |
| `Z_CONFIG_TLS_LISTEN_PRIVATE_KEY_BASE64_KEY` | 0x4E | Base64-encoded server private key. |
| `Z_CONFIG_TLS_LISTEN_CERTIFICATE_KEY` | 0x4F | Path to server certificate file. |
| `Z_CONFIG_TLS_LISTEN_CERTIFICATE_BASE64_KEY` | 0x50 | Base64-encoded server certificate. |
| `Z_CONFIG_TLS_ENABLE_MTLS_KEY` | 0x51 | Enable mutual TLS (mTLS). |
| `Z_CONFIG_TLS_CONNECT_PRIVATE_KEY_KEY` | 0x52 | Path to client private key for mTLS. |
| `Z_CONFIG_TLS_CONNECT_PRIVATE_KEY_BASE64_KEY` | 0x53 | Base64-encoded client private key. |
| `Z_CONFIG_TLS_CONNECT_CERTIFICATE_KEY` | 0x54 | Path to client certificate for mTLS. |
| `Z_CONFIG_TLS_CONNECT_CERTIFICATE_BASE64_KEY` | 0x55 | Base64-encoded client certificate. |
| `Z_CONFIG_TLS_VERIFY_NAME_ON_CONNECT_KEY` | 0x56 | Verify hostname in server certificate on connect. |

### Compile-Time Constants (not runtime-configurable)

| Constant | Value | Description |
|---|---|---|
| `Z_ZID_LENGTH` | 16 | Session ID byte length (fixed at 16 bytes = 128-bit UUID). |
| `Z_PROTO_VERSION` | 9 | Zenoh wire protocol version. Must match between all nodes. |
| `Z_JOIN_INTERVAL` | 2500 ms | Interval at which a peer sends join messages on multicast. |
| `Z_RX_CACHE_SIZE` | 10 | Number of sequence numbers cached for dedup when `Z_FEATURE_RX_CACHE=1`. |
| `Z_GET_TIMEOUT_DEFAULT` | 10000 ms | Default timeout for `z_get()` if no timeout is specified. |
| `Z_TRANSPORT_LEASE` | 10000 ms | Transport lease duration announced to remote peers. |
| `Z_TRANSPORT_LEASE_EXPIRE_FACTOR` | 3 | Multiplier applied to lease duration before declaring a session dead. |
| `Z_CONFIG_SOCKET_TIMEOUT` | 100 ms | Socket receive timeout (blocks for at most this long per `zp_read()` call). |
| `ZP_PERIODIC_SCHEDULER_MAX_TASKS` | 64 | Maximum number of periodic tasks in the scheduler. |
| `Z_LISTEN_MAX_CONNECTION_NB` | 10 | Maximum concurrent inbound connections on a listen socket. |

---

## API Differences: zenoh-pico vs zenoh-c

Both zenoh-pico and zenoh-c share the same `z_*` naming convention and `z_owned_*` / `z_loaned_*` ownership model. However, there are meaningful API-level differences.

### Ownership Model (both libraries)

Both use a three-tier ownership model:

- **`z_owned_*`** — owns the resource, must be dropped with `z_drop(z_move(x))` or moved with `z_move()`
- **`z_loaned_*`** — borrowed reference, does not own, must not be dropped
- **`z_view_*`** — non-owning view into existing memory (zero-copy, stack-allocated alias)

```c
// zenoh-pico: create an owned key expression
z_owned_keyexpr_t ke;
z_keyexpr_from_str(&ke, "demo/example/**");

// Loan it for use
z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(cb), NULL);

// Drop when done
z_drop(z_move(ke));

// Or use a zero-copy view (no allocation, borrows from string literal)
z_view_keyexpr_t ke_view;
z_view_keyexpr_from_str(&ke_view, "demo/example/**");
// z_view_* does not need z_drop
```

### Task Model: zenoh-pico

The critical difference in zenoh-pico is how network I/O is driven. zenoh-pico has two operational modes:

#### Multi-thread mode (`Z_FEATURE_MULTI_THREAD=1`, default)

Background threads handle all I/O automatically:

```c
z_owned_session_t s;
z_open(&s, z_move(config), NULL);

// Start background read and lease threads (these block and do all I/O)
zp_start_read_task(z_loan_mut(s), NULL);
zp_start_lease_task(z_loan_mut(s), NULL);

// Now declare entities and sleep — callbacks fire in the read thread
z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(cb), NULL);
while (1) { sleep(1); }  // Application logic here

// Before closing, stop the background tasks
zp_stop_read_task(z_loan_mut(s));
zp_stop_lease_task(z_loan_mut(s));
z_drop(z_move(s));
```

#### Single-thread mode (`Z_FEATURE_MULTI_THREAD=0`) — required for bare-metal/RTOS

The application must poll explicitly in its main loop:

```c
z_owned_session_t s;
z_open(&s, z_move(config), NULL);

// No background tasks — you drive the I/O
z_clock_t pulse_time = z_clock_now();

while (1) {
    // Do your application work here
    my_application_tick();

    // Drive zenoh I/O: receive any incoming data and fire callbacks
    zp_read(z_loan(s), NULL);

    // Periodically send keep-alive and peer join announcements
    unsigned long elapsed_ms = z_clock_elapsed_ms(&pulse_time);
    if (elapsed_ms >= (Z_TRANSPORT_LEASE / Z_TRANSPORT_LEASE_EXPIRE_FACTOR)) {
        pulse_time = z_clock_now();
        zp_send_keep_alive(z_loan(s), NULL);
        zp_send_join(z_loan(s), NULL);
    }
}
```

The `Z_CONFIG_SOCKET_TIMEOUT` compile-time constant (default: 100ms) controls how long `zp_read()` blocks waiting for incoming data. In a cooperative RTOS task, set this to a low value (e.g., 10ms) and call `zp_read()` frequently.

#### Why keep-alive matters

The transport lease (`Z_TRANSPORT_LEASE`, default 10 seconds) is the duration a remote node will consider the link alive without hearing from you. `zp_send_keep_alive()` resets this timer. If you forget to call it in your main loop, the router or peer will eventually drop the connection. The safe interval is `Z_TRANSPORT_LEASE / Z_TRANSPORT_LEASE_EXPIRE_FACTOR` = 10000 / 3 ≈ 3.3 seconds.

### Task Model: zenoh-c

zenoh-c inherits the Rust async runtime (tokio). All I/O happens on background threads automatically. There is no polling API — just open the session and declare entities:

```c
// zenoh-c: no background task management needed
z_owned_session_t s;
z_open(&s, z_move(config), NULL);

// Declare subscriber — callbacks fire on background thread
z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(cb), NULL);

// Sleep — everything is handled automatically
while (1) { sleep(1); }

z_drop(z_move(sub));
z_drop(z_move(s));
```

### Error Handling

Both libraries use the same `z_result_t` (int) convention: `0` = success, negative value = error.

```c
z_result_t rc = z_open(&s, z_move(config), NULL);
if (rc < 0) {
    printf("Failed to open session: %d\n", rc);
    return -1;
}
```

### Config Insertion

```c
// Both libraries: same API
z_owned_config_t config;
z_config_default(&config);

zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.100:7447");

// After open(), the config is moved (consumed)
z_open(&s, z_move(config), NULL);
```

### Publish/Subscribe Pattern Comparison

**zenoh-pico (single-thread, polling):**

```c
#include <zenoh-pico.h>

void data_handler(z_loaned_sample_t *sample, void *ctx) {
    z_view_string_t keystr;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &keystr);
    z_owned_string_t value;
    z_bytes_to_string(z_sample_payload(sample), &value);
    printf("Received on '%.*s': '%.*s'\n",
           (int)z_string_len(z_loan(keystr)), z_string_data(z_loan(keystr)),
           (int)z_string_len(z_loan(value)), z_string_data(z_loan(value)));
    z_drop(z_move(value));
}

int main(void) {
    z_owned_config_t config;
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.100:7447");

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) return -1;

    z_owned_closure_sample_t cb;
    z_closure(&cb, data_handler, NULL, NULL);

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, "demo/**");

    z_owned_subscriber_t sub;
    z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(cb), NULL);

    z_clock_t pulse = z_clock_now();
    while (1) {
        zp_read(z_loan(s), NULL);
        if (z_clock_elapsed_ms(&pulse) >= 3333) {
            pulse = z_clock_now();
            zp_send_keep_alive(z_loan(s), NULL);
            zp_send_join(z_loan(s), NULL);
        }
    }

    z_drop(z_move(sub));
    z_drop(z_move(s));
    return 0;
}
```

**zenoh (Rust) equivalent:**

```rust
use zenoh::prelude::*;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::config::default()).await.unwrap();
    let subscriber = session
        .declare_subscriber("demo/**")
        .await
        .unwrap();

    while let Ok(sample) = subscriber.recv_async().await {
        let key = sample.key_expr();
        let payload = sample.payload().to_string();
        println!("Received on '{}': '{}'", key, payload);
    }
}
```

**zenoh-c equivalent:**

```c
#include <zenoh.h>
#include <stdio.h>
#include <unistd.h>

void data_handler(z_loaned_sample_t *sample, void *ctx) {
    z_view_string_t keystr;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &keystr);
    z_owned_string_t value;
    z_bytes_to_string(z_sample_payload(sample), &value);
    printf("Received on '%.*s': '%.*s'\n",
           (int)z_string_len(z_loan(keystr)), z_string_data(z_loan(keystr)),
           (int)z_string_len(z_loan(value)), z_string_data(z_loan(value)));
    z_drop(z_move(value));
}

int main(void) {
    z_owned_config_t config;
    z_config_default(&config);

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) return -1;

    z_owned_closure_sample_t cb;
    z_closure(&cb, data_handler, NULL, NULL);

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, "demo/**");

    z_owned_subscriber_t sub;
    z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(cb), NULL);

    while (1) { sleep(1); }  // Callbacks fire automatically on background thread

    z_drop(z_move(sub));
    z_drop(z_move(s));
    return 0;
}
```

---

## When to Use Each

### Use zenoh-pico when:

- Target is a **microcontroller**: ESP32, STM32, nRF52, RP2040, Arduino AVR/ARM
- RAM is **less than 256KB** (zenoh-pico can operate in ~40KB total)
- Running **RTOS**: Zephyr, FreeRTOS, ThreadX, MbedOS, or bare-metal
- Transport is **serial (UART)** — only zenoh-pico supports serial at the library level
- Transport is **Bluetooth Serial** (Arduino only)
- Transport is **raw Ethernet** frames (Layer 2)
- No Rust toolchain is available or desired in the build system
- Using **PlatformIO** as the build system

### Use zenoh-c when:

- Target is **Raspberry Pi** (any model with Linux)
- Target is **embedded Linux** (Yocto, Buildroot, OpenWRT)
- Building **FFI bindings** for another language (Python cffi, Go cgo, Java JNI)
- Need **Shared Memory (SHM)** for zero-copy IPC on the same machine
- Need **QUIC** transport
- Need **full TLS** (with OpenSSL/rustls, not MbedTLS)
- Need **gossip scouting** for large distributed networks
- Need **ACL** (access control lists) on the broker
- Building a legacy C application on a full OS that needs zenoh

### Use zenoh (Rust) when:

- Writing a new application in Rust
- Need the **async/await** programming model (tokio)
- Need the **full feature set** without any FFI overhead
- Building a **zenoh router** (`zenohd`)
- Using zenoh **plugins** (storage, REST API, DDS bridge)
- Performance-critical applications where even thin FFI overhead matters

### Quick decision tree:

```
Has a full Linux/macOS/Windows OS?
├── Yes → Are you writing Rust code?
│         ├── Yes → Use zenoh (Rust)
│         └── No  → Use zenoh-c
└── No  → Use zenoh-pico
           ├── Serial/UART transport needed? → Enable Z_FEATURE_LINK_SERIAL=1
           ├── Bluetooth needed?             → Enable Z_FEATURE_LINK_BLUETOOTH=1
           └── Very tight RAM (<64KB)?       → Disable features, reduce buffer sizes
```

---

## Performance

### zenoh-pico

Performance numbers are hardware-dependent, but on a capable MCU or embedded Linux system:

- **Throughput**: 3M+ messages/second on Linux (when used as a benchmark, not typical MCU use)
- **Latency**: ~12µs round-trip on Linux loopback
- **Memory footprint**:
  - Default feature set: ~40KB binary
  - With all optional features disabled: ~15KB binary
  - RAM usage at runtime: dominated by your configured buffer sizes (`Z_BATCH_UNICAST_SIZE` × 2 + `Z_FRAG_MAX_SIZE` + session overhead)

On actual MCUs (ESP32, STM32):
- Throughput is limited by the transport (UART at 115200 baud: ~10KB/s raw)
- Latency is in the millisecond range over serial, microseconds over WiFi/Ethernet
- Stack depth for `zp_read()` call: ~1–2KB depending on platform

### zenoh-c

zenoh-c performance is essentially identical to Rust zenoh. The FFI boundary adds a single function call overhead that is unmeasurable compared to network latency.

- **Throughput**: tens of millions of messages/second on loopback SHM
- **Latency**: sub-microsecond over SHM, ~30–100µs over loopback TCP, network-limited otherwise
- **Binary size**: ~5–20MB (Rust runtime + zenoh + all features)

### zenoh (Rust)

- Same as zenoh-c in all practical measurements
- Async zero-copy pipelines are available via the `Sample::payload()` → `&Bytes` path
- SHM transport: zero-copy between processes on the same machine

---

## Serial Transport: MCU to zenoh Router Setup

This is the most common zenoh-pico integration pattern: a microcontroller connected via UART to a Linux host running a zenoh router.

### Architecture

```
[MCU]──UART──[Linux Host: zenohd]──TCP/UDP──[rest of zenoh network]
```

The Linux host acts as a zenoh router that bridges the serial link to the rest of the network.

### Step 1: zenoh-pico on the MCU

Build zenoh-pico with serial transport enabled:

```bash
cmake .. \
  -DZ_FEATURE_LINK_SERIAL=1 \
  -DZ_FEATURE_LINK_TCP=0 \
  -DZ_FEATURE_LINK_UDP_UNICAST=0 \
  -DZ_FEATURE_LINK_UDP_MULTICAST=0 \
  -DZ_FEATURE_MULTICAST_TRANSPORT=0 \
  -DZ_FEATURE_SCOUTING=0 \
  -DFRAG_MAX_SIZE=1024 \
  -DBATCH_UNICAST_SIZE=512
```

MCU application code (single-thread mode for RTOS):

```c
#include <zenoh-pico.h>

int main(void) {
    z_owned_config_t config;
    z_config_default(&config);

    // Connect to zenoh router via UART serial
    // Format: serial/<device>#baudrate=<baud>
    // On Arduino/ESP-IDF: serial/0 means the first UART
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
    zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "serial/0#baudrate=115200");

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        // Handle error
        return -1;
    }

    // Declare publisher
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, "mcu/sensor/temperature");
    z_owned_publisher_t pub;
    z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL);

    z_clock_t pulse = z_clock_now();

    while (1) {
        // Read sensor
        float temp = read_temperature_sensor();

        // Publish
        char buf[32];
        snprintf(buf, sizeof(buf), "%.2f", temp);
        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, buf);
        z_publisher_put(z_loan(pub), z_move(payload), NULL);

        // Drive zenoh I/O
        zp_read(z_loan(s), NULL);

        // Keep-alive
        if (z_clock_elapsed_ms(&pulse) >= 3333) {
            pulse = z_clock_now();
            zp_send_keep_alive(z_loan(s), NULL);
        }

        // Sleep 1 second
        z_sleep_ms(1000);
    }
}
```

### Step 2: RPi Pico Serial Connection

For Raspberry Pi Pico W, set serial pin configuration at build time:

```bash
cmake -Bbuild \
  -DPICO_BOARD=pico_w \
  -DZENOH_CONFIG_MODE=client \
  -DZENOH_CONFIG_CONNECT="serial/uart0_0#baudrate=115200"
cmake --build ./build
```

Valid RPi Pico UART pin pairs:

| TX Pin | RX Pin | Device Name |
|---|---|---|
| 0 | 1 | `uart0_0` |
| 4 | 5 | `uart1_0` |
| 8 | 9 | `uart1_1` |
| 12 | 13 | `uart0_1` |
| 16 | 17 | `uart0_2` |

### Step 3: STM32 ThreadX Serial

For STM32 with ThreadX, add to STM32CubeIDE project defines:

```
ZENOH_THREADX_STM32
ZENOH_HUART=huart1
```

### Step 4: zenoh Router on Linux Host

Install zenohd (the zenoh router):

```bash
# Install via cargo
cargo install zenohd

# Or use Docker
docker pull eclipse/zenoh:main
```

Start zenohd listening on the serial device:

```bash
# Direct install
zenohd --listen "serial//dev/ttyUSB0#baudrate=115200"

# Also expose TCP for other zenoh nodes to connect
zenohd \
  --listen "serial//dev/ttyUSB0#baudrate=115200" \
  --listen "tcp/0.0.0.0:7447"

# Docker (Linux only — needs --privileged or device mapping)
docker run --init --device=/dev/ttyUSB0 eclipse/zenoh:main \
  --listen "serial//dev/ttyUSB0#baudrate=115200" \
  --listen "tcp/0.0.0.0:7447"
```

The serial endpoint format for zenohd: `serial/<device_path>#baudrate=<baud>`

### Step 5: Verify End-to-End

On any machine connected to the zenoh router via TCP, subscribe to verify MCU data arrives:

```bash
# Using zenoh-c example or rust zenoh CLI
z_sub -e tcp/192.168.1.100:7447 -k "mcu/**"
```

Or with the Rust zenoh CLI tool:

```bash
cargo install zenoh-tools
z-sub --connect tcp/192.168.1.100:7447 --key mcu/**
```

### Serial Transport Config Reference

The serial link config is embedded in the endpoint URL using the `#key=value` fragment syntax:

```
serial/<device>#baudrate=<baud>
```

Only `baudrate` is currently configurable (other parameters like data bits, stop bits, parity, flow control are hardcoded to 8N1 no-flow-control defaults).

Common baud rates: `9600`, `19200`, `38400`, `57600`, `115200`, `230400`, `460800`, `921600`.

For USB CDC on RPi Pico (experimental):

```bash
# MCU side
-DZENOH_CONFIG_CONNECT="serial/usb#baudrate=112500"

# Host side
zenohd --listen "serial//dev/ttyACM0#baudrate=112500"
```

---

## Debugging

### zenoh-pico Debug Logs

Enable verbose logging at build time:

```bash
cmake .. -DZENOH_LOG=DEBUG
# or for maximum verbosity:
cmake .. -DZENOH_LOG=TRACE
```

Log levels: `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`

### Common Issues

**Session fails to open on MCU:** Reduce buffer sizes. Start with `BATCH_UNICAST_SIZE=512`, `FRAG_MAX_SIZE=1024`.

**Session drops unexpectedly:** In single-thread mode, `zp_send_keep_alive()` is not being called frequently enough. Ensure your main loop runs faster than `Z_TRANSPORT_LEASE / Z_TRANSPORT_LEASE_EXPIRE_FACTOR` ms.

**Multicast communication fails:** Ensure all participants use the same `BATCH_MULTICAST_SIZE`. The default varies by OS (65535 on Linux, 9216 on macOS, 8192 elsewhere).

**Serial connection fails:** Verify the baud rate matches on both ends, UART pins are correct, and `Z_FEATURE_LINK_SERIAL=1` was set at build time.

**zenoh-c session fails to open:** Ensure the Rust async runtime initializes correctly. In multi-threaded programs, ensure `z_open()` is called before spawning other threads that might conflict with Tokio's thread pool.

## See Also

- [Zenoh Pico Guide](zenoh-pico-guide.md) — complete guide to zenoh-pico feature flags, configuration, and platform-specific setup
- [Programming Model Guide](programming-model-guide.md) — the full Zenoh API that zenoh-c mirrors with C bindings
- [Performance Tuning Guide](performance-tuning-guide.md) — how to get the best performance from each implementation variant
