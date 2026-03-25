# zenoh-pico: Complete Guide for Embedded Systems

zenoh-pico is the native C implementation of the Zenoh protocol for constrained devices and microcontrollers. It is fully wire-compatible with the Rust zenoh implementation while targeting environments with as little as 15KB of flash. This guide covers every compile-time flag, every runtime configuration parameter, all supported platforms, and the complete API surface for embedded deployment.

---

## Table of Contents

- [Overview](#overview)
- [Compile-Time Feature Flags](#compile-time-feature-flags)
  - [Core Protocol Features](#core-protocol-features)
  - [Transport Features](#transport-features)
  - [Link (Transport Driver) Features](#link-transport-driver-features)
  - [Thread and Concurrency Features](#thread-and-concurrency-features)
  - [Advanced Features (Unstable API)](#advanced-features-unstable-api)
- [Buffer and Timing Parameters](#buffer-and-timing-parameters)
  - [`FRAG_MAX_SIZE` → `Z_FRAG_MAX_SIZE`](#frag_max_size-z_frag_max_size)
  - [`BATCH_UNICAST_SIZE` → `Z_BATCH_UNICAST_SIZE`](#batch_unicast_size-z_batch_unicast_size)
  - [`BATCH_MULTICAST_SIZE` → `Z_BATCH_MULTICAST_SIZE`](#batch_multicast_size-z_batch_multicast_size)
  - [`Z_CONFIG_SOCKET_TIMEOUT`](#z_config_socket_timeout)
  - [`Z_TRANSPORT_LEASE`](#z_transport_lease)
  - [`Z_TRANSPORT_LEASE_EXPIRE_FACTOR`](#z_transport_lease_expire_factor)
  - [`ZP_PERIODIC_SCHEDULER_MAX_TASKS`](#zp_periodic_scheduler_max_tasks)
- [Runtime Configuration Parameters](#runtime-configuration-parameters)
  - [`Z_CONFIG_MODE_KEY` (0x40)](#z_config_mode_key-0x40)
  - [`Z_CONFIG_CONNECT_KEY` (0x41)](#z_config_connect_key-0x41)
  - [`Z_CONFIG_LISTEN_KEY` (0x42)](#z_config_listen_key-0x42)
  - [`Z_CONFIG_USER_KEY` (0x43)](#z_config_user_key-0x43)
  - [`Z_CONFIG_PASSWORD_KEY` (0x44)](#z_config_password_key-0x44)
  - [`Z_CONFIG_MULTICAST_SCOUTING_KEY` (0x45)](#z_config_multicast_scouting_key-0x45)
  - [`Z_CONFIG_MULTICAST_LOCATOR_KEY` (0x46)](#z_config_multicast_locator_key-0x46)
  - [`Z_CONFIG_SCOUTING_TIMEOUT_KEY` (0x47)](#z_config_scouting_timeout_key-0x47)
  - [`Z_CONFIG_SCOUTING_WHAT_KEY` (0x48)](#z_config_scouting_what_key-0x48)
  - [`Z_CONFIG_SESSION_ZID_KEY` (0x49)](#z_config_session_zid_key-0x49)
  - [`Z_CONFIG_ADD_TIMESTAMP_KEY` (0x4A)](#z_config_add_timestamp_key-0x4a)
  - [TLS Configuration Keys](#tls-configuration-keys)
- [Supported Platforms](#supported-platforms)
  - [ESP32 (ESP-IDF)](#esp32-esp-idf)
  - [Arduino (AVR/ARM/ESP32)](#arduino-avrarmesp32)
  - [Zephyr RTOS](#zephyr-rtos)
  - [FreeRTOS](#freertos)
  - [Raspberry Pi Pico (RP2040)](#raspberry-pi-pico-rp2040)
  - [STM32 (ThreadX / Azure RTOS)](#stm32-threadx-azure-rtos)
  - [PX4 (NuttX RTOS)](#px4-nuttx-rtos)
- [API Model](#api-model)
  - [The Fundamental Difference: Explicit Network Polling](#the-fundamental-difference-explicit-network-polling)
  - [Subscriber Callbacks](#subscriber-callbacks)
- [Memory Ownership Model](#memory-ownership-model)
  - [Owned Types (`z_owned_*`)](#owned-types-z_owned_)
  - [Loaned Types (`z_loaned_*`)](#loaned-types-z_loaned_)
  - [View Types (`z_view_*`)](#view-types-z_view_)
  - [Moving (`z_move`)](#moving-z_move)
  - [Dropping (`z_drop`)](#dropping-z_drop)
  - [Complete session lifecycle pattern:](#complete-session-lifecycle-pattern)
- [Serial Transport: Complete Setup Guide](#serial-transport-complete-setup-guide)
  - [Step 1: Wiring](#step-1-wiring)
  - [Step 2: MCU Configuration](#step-2-mcu-configuration)
  - [Step 3: Host Router Configuration](#step-3-host-router-configuration)
  - [Step 4: Testing the Connection](#step-4-testing-the-connection)
  - [Step 5: Tuning for Reliability](#step-5-tuning-for-reliability)
- [Performance Numbers](#performance-numbers)
  - [Throughput](#throughput)
  - [Latency](#latency)
  - [Flash Footprint](#flash-footprint)
- [zenoh-pico vs micro-ROS](#zenoh-pico-vs-micro-ros)
- [Footprint Optimization Recipes](#footprint-optimization-recipes)
  - [Recipe: Sensor Node (publish only, no WiFi, serial transport)](#recipe-sensor-node-publish-only-no-wifi-serial-transport)
  - [Recipe: Subscriber-only node (receive sensor data, no sending)](#recipe-subscriber-only-node-receive-sensor-data-no-sending)
  - [Recipe: Full-featured IoT node (pub/sub + queries, WiFi TCP)](#recipe-full-featured-iot-node-pubsub-queries-wifi-tcp)
- [PX4 / NuttX Deployment](#px4-nuttx-deployment)
  - [Topology](#topology)
  - [UDP Multicast Discovery (Ethernet)](#udp-multicast-discovery-ethernet)
  - [Failover Redundancy](#failover-redundancy)
  - [Flight Data Patterns](#flight-data-patterns)
  - [Production Considerations](#production-considerations)
- [Quick Reference: Complete Minimal Build](#quick-reference-complete-minimal-build)


---


## Overview

zenoh-pico targets the same protocol as zenoh (Rust), making them fully interoperable over the network. A zenoh-pico node on an ESP32 speaks to zenoh routers and full zenoh nodes with no translation layer.

Key design constraints addressed:
- **No heap required for core operation** — static buffers configurable at compile time
- **No internal threads** — application controls when to read from network
- **Modular features** — unused protocol features compile out entirely
- **C99/C11 compatible** — works with embedded compilers including GCC for ARM, Xtensa, RISC-V

The library is available from:
- PlatformIO: `lib_deps = https://github.com/eclipse-zenoh/zenoh-pico`
- CMake subproject: clone and `add_subdirectory`
- Debian/RPM packages for Linux (libzenohpico-dev)

---

## Compile-Time Feature Flags

All flags are set in CMakeLists.txt using `set(Z_FEATURE_XXX <0|1>)` or as `-DZ_FEATURE_XXX=<0|1>` on the cmake command line. In a PlatformIO project, use `board_build.cmake_extra_args`.

The generated values appear in `include/zenoh-pico/config.h` and are checked throughout the codebase with `#if Z_FEATURE_XXX == 1` guards. Disabling a feature removes the associated code from the binary entirely.

### Core Protocol Features

#### `Z_FEATURE_PUBLICATION`
- **Default:** `1` (ON)
- **What it enables:** `z_declare_publisher()`, `z_publisher_put()`, `z_put()` — the ability to send data to key expressions.
- **Size impact when OFF:** ~3–5KB flash (removes all publisher declaration and put path code)
- **Use case:** Subscriber-only nodes (e.g., a sensor aggregator that only consumes data), or queryable-only services.
- **Note:** The source examples guard their entire body with `#if Z_FEATURE_PUBLICATION == 1`.

#### `Z_FEATURE_SUBSCRIPTION`
- **Default:** `1` (ON)
- **What it enables:** `z_declare_subscriber()`, subscriber callbacks — receiving data matching a key expression.
- **Size impact when OFF:** ~3–5KB flash
- **Use case:** Publisher-only nodes like sensor transmitters that never need to receive.

#### `Z_FEATURE_QUERY`
- **Default:** `1` (ON)
- **What it enables:** `z_get()` — sending queries to queryable nodes to retrieve stored or computed data.
- **Size impact when OFF:** ~2–3KB flash
- **Use case:** Nodes that only publish or subscribe and never issue get requests.

#### `Z_FEATURE_QUERYABLE`
- **Default:** `1` (ON)
- **What it enables:** `z_declare_queryable()` — registering a handler that responds to incoming queries.
- **Size impact when OFF:** ~2–3KB flash
- **Use case:** Pure pub/sub nodes with no query-response capability needed.

#### `Z_FEATURE_LIVELINESS`
- **Default:** `1` (ON)
- **What it enables:** `z_liveliness_declare_token()`, `z_liveliness_declare_subscriber()`, `z_liveliness_get()` — tokens that advertise node presence and disappear when the session closes.
- **Size impact when OFF:** ~2–4KB flash
- **Use case:** Nodes that don't need presence detection or liveliness-based service discovery.
- **Dependency:** Required by `Z_FEATURE_ADVANCED_PUBLICATION` and `Z_FEATURE_ADVANCED_SUBSCRIPTION`.

#### `Z_FEATURE_INTEREST`
- **Default:** `1` (ON)
- **What it enables:** Interest-based routing optimization — allows nodes to advertise interest in specific key expressions so the router can filter routing decisions.
- **Size impact when OFF:** ~1–2KB flash
- **Use case:** Ultra-minimal builds; note that `Z_FEATURE_MATCHING` is automatically disabled when this is off.
- **Dependency:** `Z_FEATURE_MATCHING` requires this to be ON.

#### `Z_FEATURE_FRAGMENTATION`
- **Default:** `1` (ON)
- **What it enables:** Splitting messages larger than the batch size into multiple transport frames.
- **Size impact when OFF:** ~1–2KB flash. Payloads exceeding `Z_FRAG_MAX_SIZE` will fail to send.
- **Use case:** Sensor nodes that only publish small fixed-size payloads and never need large messages.

#### `Z_FEATURE_ENCODING_VALUES`
- **Default:** `1` (ON)
- **What it enables:** Predefined encoding constants (`z_encoding_*`) for MIME types, Zenoh protocol encodings, etc.
- **Size impact when OFF:** ~1KB flash (removes the encoding constant table)
- **Use case:** Builds where all data is opaque bytes and encoding metadata is irrelevant.

#### `Z_FEATURE_MATCHING`
- **Default:** `1` (ON)
- **What it enables:** `z_declare_matching_listener()` — notification when subscribers or publishers appear/disappear matching your key expression.
- **Size impact when OFF:** ~1–2KB flash
- **Dependency:** Requires `Z_FEATURE_INTEREST`. Auto-disabled if interest is OFF.
- **Use case:** Nodes that don't need to react to subscriber/publisher appearance.

#### `Z_FEATURE_AUTO_RECONNECT`
- **Default:** `1` (ON)
- **What it enables:** Automatic reconnection to the router when the connection drops.
- **Size impact when OFF:** ~1KB flash
- **Use case:** Controlled environments where manual reconnection is preferred; disabling saves a small amount of state tracking code.

#### `Z_FEATURE_SESSION_CHECK`
- **Default:** `1` (ON)
- **What it enables:** Validates that publishers and queriers belong to a live session before operations.
- **Size impact when OFF:** Negligible
- **Use case:** Only disable if you are certain the session lifecycle is managed correctly and need to shave every byte.

#### `Z_FEATURE_BATCHING`
- **Default:** `1` (ON)
- **What it enables:** Coalescing multiple small messages into a single transport frame (up to batch size) for efficiency.
- **Size impact when OFF:** ~1–2KB flash; throughput will decrease for burst workloads.
- **Use case:** Very low-memory nodes where the batching buffers are too costly.

#### `Z_FEATURE_LOCAL_SUBSCRIBER`
- **Default:** `0` (OFF)
- **What it enables:** Subscribers receive publications from the same session (loopback).
- **Size impact when ON:** ~1–2KB flash
- **Use case:** Testing, or nodes that need to observe their own publications.

#### `Z_FEATURE_LOCAL_QUERYABLE`
- **Default:** `0` (OFF)
- **What it enables:** Queryables receive queries from the same session.
- **Size impact when ON:** ~1KB flash
- **Use case:** Self-querying patterns, testing.

#### `Z_FEATURE_RX_CACHE`
- **Default:** `0` (OFF)
- **What it enables:** A receive cache (`Z_RX_CACHE_SIZE` entries, default 10) for deduplicating received messages.
- **Size impact when ON:** RAM cost of 10 × message ID entries
- **Use case:** Multicast environments where duplicate delivery is common.

#### `Z_FEATURE_ADMIN_SPACE`
- **Default:** `0` (OFF)
- **Dependency:** Requires `Z_FEATURE_UNSTABLE_API`.
- **What it enables:** Admin space queryable at `@/...` — introspection of the local zenoh node's state.
- **Use case:** Debugging, diagnostics.

#### `Z_FEATURE_PERIODIC_TASKS`
- **Default:** `0` (OFF)
- **Dependency:** Requires `Z_FEATURE_UNSTABLE_API`. Auto-enabled when advanced pub/sub is enabled.
- **What it enables:** A scheduler for periodic background tasks within the zenoh runtime.
- **Use case:** Advanced publisher heartbeats, history maintenance.

#### `Z_FEATURE_MULTICAST_DECLARATIONS`
- **Default:** `0` (OFF)
- **What it enables:** Resource declarations propagated over multicast transport (peer-to-peer without a router).
- **Use case:** Pure peer mode over UDP multicast where there is no router to forward declarations.

### Transport Features

#### `Z_FEATURE_MULTICAST_TRANSPORT`
- **Default:** `1` (ON)
- **What it enables:** UDP multicast transport for peer-to-peer operation without a router.
- **Size impact when OFF:** ~3–5KB flash
- **Use case:** Client-only nodes that always connect to a router via TCP/UDP unicast.

#### `Z_FEATURE_UNICAST_TRANSPORT`
- **Default:** `1` (ON)
- **What it enables:** TCP and UDP unicast transport (client-router connections).
- **Size impact when OFF:** Only useful if you're operating pure multicast peer mode.

#### `Z_FEATURE_UNICAST_PEER`
- **Default:** `1` (ON)
- **Dependency:** Requires `Z_FEATURE_MULTI_THREAD`.
- **What it enables:** Peer-mode unicast connections (node-to-node without a router).
- **Use case:** Disable if you only use client mode and want to save code.

#### `Z_FEATURE_RAWETH_TRANSPORT`
- **Default:** `0` (OFF)
- **What it enables:** Raw Ethernet (Layer 2) transport — bypasses IP/UDP entirely, sending zenoh frames directly as Ethernet frames. Useful for real-time industrial networks.
- **Size impact when ON:** ~4–6KB flash
- **Use case:** TSN (Time-Sensitive Networking), industrial fieldbus replacements, robotics backplanes. Requires network interface that supports raw socket access.

### Link (Transport Driver) Features

#### `Z_FEATURE_LINK_TCP`
- **Default:** `1` (ON)
- **What it enables:** TCP socket transport. Used for client→router connections and unicast peer connections.
- **Endpoint format:** `tcp/192.168.1.1:7447`

#### `Z_FEATURE_LINK_UDP_UNICAST`
- **Default:** `1` (ON)
- **What it enables:** UDP unicast socket transport. Lighter than TCP, no connection overhead.
- **Endpoint format:** `udp/192.168.1.1:7447`
- **Note:** Disabling this also auto-disables `Z_FEATURE_SCOUTING`.

#### `Z_FEATURE_LINK_UDP_MULTICAST`
- **Default:** `1` (ON)
- **What it enables:** UDP multicast socket. Used for multicast scouting and peer-mode communication.
- **Endpoint format:** `udp/224.0.0.123:7447#iface=eth0`

#### `Z_FEATURE_LINK_SERIAL`
- **Default:** `0` (OFF)
- **What it enables:** UART/serial transport for microcontrollers with no IP stack. Enables connection to a zenoh router on a host machine via a physical serial cable.
- **Endpoint format:** `serial//dev/ttyUSB0#baudrate=115200` (Linux host), `serial/0.1#baudrate=38400` (RPi Pico pin pair)
- **Use case:** ESP32 UART to router, STM32 USART to router, RPi Pico UART to host.

#### `Z_FEATURE_LINK_SERIAL_USB`
- **Default:** `0` (OFF)
- **Dependency:** Requires `Z_FEATURE_UNSTABLE_API`. Build will warn and force-disable if UNSTABLE_API is not set.
- **What it enables:** USB CDC (Virtual COM Port) transport on platforms like Raspberry Pi Pico. The MCU appears as a serial device over USB.
- **Endpoint format:** `serial/usb#baudrate=112500` (MCU side), `serial//dev/ttyACM0#baudrate=112500` (host side)

#### `Z_FEATURE_LINK_BLUETOOTH`
- **Default:** `0` (OFF)
- **What it enables:** Bluetooth Serial Profile (SPP) transport. Supported on Arduino with BT hardware.
- **Endpoint format:** `bt/<bt_address>` (platform-specific)
- **Use case:** Wearable sensors, Arduino BT shield, wireless MCU connections.

#### `Z_FEATURE_LINK_WS`
- **Default:** `0` (OFF)
- **What it enables:** WebSocket transport. Used on Emscripten (browser WASM) targets.
- **Endpoint format:** `ws/localhost:7447`
- **Use case:** Browser applications compiled with Emscripten.

#### `Z_FEATURE_LINK_TLS`
- **Default:** `0` (OFF)
- **What it enables:** TLS-encrypted TCP transport via Mbed TLS 2.x or 3.x (auto-detected via pkg-config).
- **Endpoint format:** `tls/192.168.1.1:7447`
- **Config keys:** `Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_KEY`, `Z_CONFIG_TLS_LISTEN_PRIVATE_KEY_KEY`, etc.
- **Use case:** Production deployments requiring encrypted transport.

#### `Z_FEATURE_SCOUTING`
- **Default:** `1` (ON)
- **What it enables:** UDP multicast scouting — automatic router/peer discovery without knowing the address. A client in scout mode sends multicast discovery packets and waits for a router to respond.
- **Dependency:** Requires `Z_FEATURE_LINK_UDP_UNICAST`. Auto-disabled if UDP unicast is OFF.
- **Use case:** Disable if you always use explicit connect addresses (`Z_CONFIG_CONNECT_KEY`) and want to save code.

### Thread and Concurrency Features

#### `Z_FEATURE_MULTI_THREAD`
- **Default:** `1` (ON)
- **What it enables:** Thread-safety in the session and internal data structures; allows `zp_start_read_task()` and `zp_start_lease_task()` to spawn background OS threads.
- **Size impact when OFF:** Small (~1KB); disables `zp_start_read_task`/`zp_start_lease_task`. You must use manual polling.
- **Use case:** Single-threaded bare-metal systems with no RTOS, where you manually call `zp_read()` and `zp_send_keep_alive()` in your main loop.

#### `Z_FEATURE_BATCH_TX_MUTEX`
- **Default:** `0` (OFF)
- **What it enables:** Mutex lock at the batch (frame) level instead of per-message. Reduces contention for high-frequency multi-threaded publishers.
- **Use case:** High-throughput multi-producer scenarios.

#### `Z_FEATURE_BATCH_PEER_MUTEX`
- **Default:** `0` (OFF)
- **What it enables:** Per-peer mutex for transmit batching — finer-grained locking when communicating with multiple peers simultaneously.

### Advanced Features (Unstable API)

#### `Z_FEATURE_UNSTABLE_API`
- **Default:** `0` (OFF)
- **What it enables:** Guards unstable/experimental API surface that may change between releases. Required by: `Z_FEATURE_LINK_SERIAL_USB`, `Z_FEATURE_PERIODIC_TASKS`, `Z_FEATURE_ADMIN_SPACE`, `Z_FEATURE_ADVANCED_PUBLICATION`, `Z_FEATURE_ADVANCED_SUBSCRIPTION`.
- **Use case:** Enable when you need any of the above features and accept potential API churn.

#### `Z_FEATURE_ADVANCED_PUBLICATION`
- **Default:** `0` (OFF)
- **Dependency:** Requires `Z_FEATURE_UNSTABLE_API` + `Z_FEATURE_PUBLICATION` + `Z_FEATURE_LIVELINESS`. Auto-enables `Z_FEATURE_PERIODIC_TASKS`.
- **What it enables:** Publisher with cache, history, and recovery. Messages are cached locally so late-joining subscribers can retrieve missed data.
- **Use case:** Reliable pub/sub over lossy links where subscribers may miss messages.

#### `Z_FEATURE_ADVANCED_SUBSCRIPTION`
- **Default:** `0` (OFF)
- **Dependency:** Requires `Z_FEATURE_UNSTABLE_API` + `Z_FEATURE_SUBSCRIPTION` + `Z_FEATURE_LIVELINESS` + `Z_FEATURE_MULTI_THREAD`. Auto-enables `Z_FEATURE_PERIODIC_TASKS`.
- **What it enables:** Subscriber with recovery — automatically requests missed messages from an advanced publisher's cache.
- **Use case:** Reliable delivery over unreliable links.

---

## Buffer and Timing Parameters

These are set in `CMakeLists.txt` as `set(PARAM value)` or passed as `-DPARAM=value`. They control RAM allocation and timing behavior and are critical for constrained systems.

### `FRAG_MAX_SIZE` → `Z_FRAG_MAX_SIZE`
- **Default:** `4096` (bytes)
- **What it controls:** Maximum size of a message that can be fragmented into multiple frames. A single message larger than this cannot be sent. This buffer is allocated statically.
- **RAM impact:** 4096 bytes of buffer space always reserved.
- **Tuning:** Set to the maximum expected payload size. For small sensor data, 512 or 1024 bytes is sufficient.
- **PlatformIO example:**
  ```ini
  board_build.cmake_extra_args =
    -DFRAG_MAX_SIZE=1024
  ```

### `BATCH_UNICAST_SIZE` → `Z_BATCH_UNICAST_SIZE`
- **Default:** `2048` (bytes)
- **What it controls:** Maximum size of a transport frame in client/unicast mode. Messages are batched into frames up to this size before transmission.
- **RAM impact:** 2048 bytes transmit buffer + 2048 receive buffer = ~4KB.
- **Tuning:** Match to your MTU. For TCP over WiFi, 1500 bytes (Ethernet MTU) is a common choice. Reduce to 512 for very constrained MCUs.
- **Must match router:** All nodes must use compatible batch sizes. Mismatches cause session open failures.

### `BATCH_MULTICAST_SIZE` → `Z_BATCH_MULTICAST_SIZE`
- **Default:** `2048` (bytes)
- **What it controls:** Maximum frame size in peer/multicast mode.
- **Platform defaults:** Linux/Windows: 65535; macOS: 9216; embedded: 8192 (or whatever you set).
- **Warning:** All nodes in a multicast group must use the same value. Mismatches cause sessions to fail to open — this is the most common source of "unable to open session" errors on microcontrollers.

### `Z_CONFIG_SOCKET_TIMEOUT`
- **Default:** `100` (milliseconds)
- **What it controls:** Socket receive timeout. `zp_read()` blocks for at most this duration waiting for incoming data.
- **Tuning:** Reduce for more responsive single-threaded polling loops. 10ms is common for real-time applications.

### `Z_TRANSPORT_LEASE`
- **Default:** `10000` (milliseconds)
- **What it controls:** Session lease duration announced to peers. If keepalives are not sent within this window, the remote side considers the session dead.
- **Tuning:** Reduce for faster failure detection (e.g., 3000ms). Increase for lossy links where keepalive delivery is uncertain.

### `Z_TRANSPORT_LEASE_EXPIRE_FACTOR`
- **Default:** `3`
- **What it controls:** Multiplier on the lease duration before declaring a session expired. Effective timeout = `Z_TRANSPORT_LEASE × Z_TRANSPORT_LEASE_EXPIRE_FACTOR` = 30 seconds by default.

### `ZP_PERIODIC_SCHEDULER_MAX_TASKS`
- **Default:** `64`
- **What it controls:** Maximum concurrent tasks in the periodic scheduler (used by advanced pub/sub).
- **RAM impact:** Each task entry is a small struct; 64 entries ≈ 1–2KB.
- **Tuning:** Reduce to 8–16 if using advanced pub/sub with few entities.

---

## Runtime Configuration Parameters

Runtime configuration is set programmatically using `zp_config_insert()` before opening the session. Keys are integer constants; values are strings.

```c
z_owned_config_t config;
z_config_default(&config);
zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.100:7447");
z_open(&session, z_move(config), NULL);
```

### `Z_CONFIG_MODE_KEY` (0x40)
- **Type:** String enum
- **Values:** `"client"` | `"peer"`
- **Default:** `"client"` (`Z_CONFIG_MODE_CLIENT`)
- **What it controls:** Session operating mode.
  - **client**: Connects to a zenoh router. Does not route between sessions. Most constrained devices should use client mode.
  - **peer**: Participates in peer-to-peer routing. Can communicate directly with other peers via multicast, or via unicast with `Z_FEATURE_UNICAST_PEER`.

### `Z_CONFIG_CONNECT_KEY` (0x41)
- **Type:** String (locator)
- **Default:** None (scouts via multicast if not set)
- **Format:** `<transport>/<address>:<port>[#<options>]`
- **Examples:**
  - `"tcp/192.168.1.100:7447"` — TCP to router
  - `"udp/192.168.1.100:7447"` — UDP unicast to router
  - `"serial//dev/ttyUSB0#baudrate=115200"` — Serial to router
  - `"serial/0.1#baudrate=38400"` — RPi Pico UART0 pins 0/1
- **Note in zenoh-pico:** Only one connect locator is accepted per session in most builds. Multiple values require peer unicast mode.
- **Client mode:** Use this to specify the router address. If empty and scouting is enabled, the library will send multicast scouting packets and use the first router that responds.

### `Z_CONFIG_LISTEN_KEY` (0x42)
- **Type:** String (locator)
- **Default:** None
- **Note:** Multiple values are **not** accepted in zenoh-pico (unlike full zenoh). Only one listen endpoint.
- **Use:** Peer mode — specify the address/interface to listen on for incoming connections.
- **Example:** `"udp/224.0.0.123:7447#iface=eth0"` for multicast peer mode.

### `Z_CONFIG_USER_KEY` (0x43)
- **Type:** String
- **Default:** None
- **What it controls:** Username for authentication against the router.

### `Z_CONFIG_PASSWORD_KEY` (0x44)
- **Type:** String
- **Default:** None
- **What it controls:** Password for authentication.

### `Z_CONFIG_MULTICAST_SCOUTING_KEY` (0x45)
- **Type:** String boolean
- **Values:** `"true"` | `"false"`
- **Default:** `"true"` (`Z_CONFIG_MULTICAST_SCOUTING_DEFAULT`)
- **What it controls:** Whether to send multicast scouting packets when no explicit connect address is provided.

### `Z_CONFIG_MULTICAST_LOCATOR_KEY` (0x46)
- **Type:** String (multicast locator)
- **Default:** `"udp/224.0.0.224:7446"` (`Z_CONFIG_MULTICAST_LOCATOR_DEFAULT`)
- **What it controls:** Multicast group address and port used for scouting and multicast transport.
- **Note:** All nodes on a network segment must use the same multicast address to discover each other.

### `Z_CONFIG_SCOUTING_TIMEOUT_KEY` (0x47)
- **Type:** String integer (milliseconds)
- **Default:** `"1000"` (`Z_CONFIG_SCOUTING_TIMEOUT_DEFAULT`)
- **What it controls:** How long a client waits during multicast scouting before giving up and returning an error from `z_open()`.
- **Tuning:** Increase on slow networks; decrease if you know the router is always available and want fast startup.

### `Z_CONFIG_SCOUTING_WHAT_KEY` (0x48)
- **Type:** String integer (bitfield)
- **Default:** `"3"` (`Z_CONFIG_SCOUTING_WHAT_DEFAULT`)
- **Values:** Bitwise combination of `z_whatami_t` values: Router=1, Peer=2, Client=4.
- **Default 3** means scout for Routers (1) and Peers (2).

### `Z_CONFIG_SESSION_ZID_KEY` (0x49)
- **Type:** String (128-bit UUID hex)
- **Default:** Auto-generated
- **What it controls:** Force a static, deterministic session ID. Useful when the session needs a known identity (e.g., for routing rules or debugging).

### `Z_CONFIG_ADD_TIMESTAMP_KEY` (0x4A)
- **Type:** String boolean
- **Values:** `"true"` | `"false"`
- **Default:** `"false"` (`Z_CONFIG_ADD_TIMESTAMP_DEFAULT`)
- **What it controls:** Whether to attach a timestamp to every published message. Timestamps use the Zenoh HLC (Hybrid Logical Clock).

### TLS Configuration Keys

Used when `Z_FEATURE_LINK_TLS` is enabled:

| Key | Constant | Purpose |
|-----|----------|---------|
| Root CA cert (path) | `Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_KEY` (0x4B) | CA certificate file path |
| Root CA cert (base64) | `Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_BASE64_KEY` (0x4C) | Inline CA cert |
| Server private key (path) | `Z_CONFIG_TLS_LISTEN_PRIVATE_KEY_KEY` (0x4D) | Listener key file |
| Server private key (base64) | `Z_CONFIG_TLS_LISTEN_PRIVATE_KEY_BASE64_KEY` (0x4E) | Inline listener key |
| Server cert (path) | `Z_CONFIG_TLS_LISTEN_CERTIFICATE_KEY` (0x4F) | Listener cert file |
| Server cert (base64) | `Z_CONFIG_TLS_LISTEN_CERTIFICATE_BASE64_KEY` (0x50) | Inline listener cert |
| Enable mTLS | `Z_CONFIG_TLS_ENABLE_MTLS_KEY` (0x51) | Mutual TLS |
| Client private key (path) | `Z_CONFIG_TLS_CONNECT_PRIVATE_KEY_KEY` (0x52) | Connector key |
| Client cert (path) | `Z_CONFIG_TLS_CONNECT_CERTIFICATE_KEY` (0x54) | Connector cert |
| Verify server name | `Z_CONFIG_TLS_VERIFY_NAME_ON_CONNECT_KEY` (0x56) | SNI verification |

---

## Supported Platforms

### ESP32 (ESP-IDF)

**Tested boards:** az-delivery-devkit-v4, ESP32-S3

**Transports:** TCP, UDP unicast, UDP multicast, Serial (UART)

**Setup (PlatformIO):**
```ini
[env:esp32]
platform = espressif32
board = az-delivery-devkit-v4
framework = espidf
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
board_build.cmake_extra_args =
  -DZ_FEATURE_LINK_SERIAL=0
  -DBATCH_UNICAST_SIZE=1024
  -DFRAG_MAX_SIZE=2048
```

**Key pattern:** ESP-IDF uses FreeRTOS internally. After `z_open()`, call `zp_start_read_task()` and `zp_start_lease_task()` to launch background FreeRTOS tasks that handle network I/O. The WiFi must be initialized before calling `z_open()`.

```c
// Minimal ESP-IDF publisher pattern
#include <zenoh-pico.h>

void app_main() {
    // 1. Initialize WiFi (platform-specific)
    wifi_init_sta();

    // 2. Configure session
    z_owned_config_t config;
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
    // Leave connect empty to use multicast scouting, or set explicitly:
    zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.100:7447");

    // 3. Open session
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Failed to open session\n");
        return;
    }

    // 4. Start background network tasks (ESP-IDF/FreeRTOS)
    zp_start_read_task(z_loan_mut(s), NULL);
    zp_start_lease_task(z_loan_mut(s), NULL);

    // 5. Declare publisher
    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str_unchecked(&ke, "sensors/temperature");
    z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL);

    // 6. Publish loop
    for (;;) {
        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, "23.5");
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
```

**Limitations:**
- Serial USB not available (no USB CDC stack in standard ESP-IDF without additional config)
- Bluetooth requires `Z_FEATURE_LINK_BLUETOOTH=1` and appropriate IDF BT component

### Arduino (AVR/ARM/ESP32)

**Tested boards:** ESP32 with Arduino framework, AVR boards with Ethernet shield

**Transports:** TCP, UDP unicast/multicast, Serial (UART), Bluetooth Serial Profile

**Setup (PlatformIO):**
```ini
[env:arduino_esp32]
platform = espressif32
board = az-delivery-devkit-v4
framework = arduino
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
```

**Key difference from ESP-IDF:** In Arduino, `setup()` is called once and `loop()` runs repeatedly. Background tasks started via `zp_start_read_task()` use the FreeRTOS underlying Arduino. For AVR (no RTOS), use single-threaded mode with manual polling.

### Zephyr RTOS

**Tested boards:** reel_board, nucleo-f767zi, nucleo-f420zi, nRF52840

**Transports:** TCP, UDP unicast/multicast, Serial, Bluetooth LE (via Bluetooth Serial), raw Ethernet

**Build flag:** `-DWITH_ZEPHYR=ON` or set in PlatformIO config.

**Zephyr prj.conf** (for nucleo-f767zi with TCP):
```conf
CONFIG_NETWORKING=y
CONFIG_NET_TCP=y
CONFIG_NET_UDP=y
CONFIG_NET_IPV4=y
CONFIG_HEAP_MEM_POOL_SIZE=16384
CONFIG_MAIN_STACK_SIZE=4096
CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE=2048
```

**PlatformIO setup:**
```ini
[env:nucleo_f767zi]
platform = ststm32
board = nucleo_f767zi
framework = zephyr
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
platform_packages = framework-zephyr
```

**Limitations:**
- 6LoWPAN available for Thread network transport
- nRF52840 has Bluetooth LE available via Zephyr BT stack

### FreeRTOS

Two variants are supported:

**FreeRTOS-Plus-TCP** (`-DWITH_FREERTOS_PLUS_TCP=ON`):
- Supports: UDP unicast, TCP, IPv4, Ethernet
- Background task variant: `zp_start_read_task()` / `zp_start_lease_task()`
- Single-threaded variant: manual `zp_read()` / `zp_send_keep_alive()` / `zp_send_join()`

**FreeRTOS + LwIP** (`-DWITH_FREERTOS_LWIP=ON`):
- Supports: UDP unicast/multicast, TCP, IPv4/IPv6, Ethernet, WiFi
- More widely used in embedded WiFi MCUs (ESP32, STM32 with WiFi module)

**Single-threaded FreeRTOS pattern** (no background tasks):
```c
// Use when Z_FEATURE_MULTI_THREAD=0 or when you want explicit control
void app_main(void) {
    z_owned_config_t config;
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");

    z_owned_session_t s;
    z_open(&s, z_move(config), NULL);

    // Declare publisher (NO background tasks started)
    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str_unchecked(&ke, "demo/data");
    z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL);

    // Read initial declarations
    zp_read(z_loan(s), NULL);

    z_clock_t now = z_clock_now();
    for (;;) {
        if (z_clock_elapsed_ms(&now) > 1000) {
            z_owned_bytes_t payload;
            z_bytes_copy_from_str(&payload, "hello");
            z_publisher_put(z_loan(pub), z_move(payload), NULL);
            now = z_clock_now();
        }
        // Must call periodically:
        zp_read(z_loan(s), NULL);           // process incoming messages
        zp_send_keep_alive(z_loan(s), NULL); // send session keepalive
        zp_send_join(z_loan(s), NULL);       // send peer join (peer mode)
    }
}
```

### Raspberry Pi Pico (RP2040)

**Tested boards:** Pico W, Pico 2 W

**Transports:** TCP, UDP unicast/multicast (WiFi, Pico W only), Serial (UART), USB CDC (experimental)

**Build requirements:**
```bash
sudo apt install -y cmake gcc-arm-none-eabi libnewlib-arm-none-eabi \
    build-essential g++ libstdc++-arm-none-eabi-newlib

export PICO_SDK_PATH=$HOME/src/pico-sdk
git clone https://github.com/raspberrypi/pico-sdk.git $PICO_SDK_PATH
cd $PICO_SDK_PATH && git submodule update --init

export FREERTOS_KERNEL_PATH=$HOME/src/FreeRTOS-Kernel
git clone https://github.com/FreeRTOS/FreeRTOS-Kernel.git $FREERTOS_KERNEL_PATH
cd $FREERTOS_KERNEL_PATH && git submodule update --init
```

**Build (WiFi TCP client):**
```bash
cd examples/rpi_pico
cmake -Bbuild \
  -DPICO_BOARD=pico_w \
  -DWIFI_SSID=MyNetwork \
  -DWIFI_PASSWORD=MyPassword \
  -DZENOH_CONFIG_MODE=client \
  -DZENOH_CONFIG_CONNECT="tcp/192.168.1.100:7447"
cmake --build ./build
```

**Build (Serial UART):**
```bash
cmake -Bbuild \
  -DPICO_BOARD=pico \
  -DZENOH_CONFIG_MODE=client \
  -DZENOH_CONFIG_CONNECT="serial/0.1#baudrate=115200"
```

**UART pin combinations:**
| Pins (TX.RX) | Device Name |
|-------------|-------------|
| 0.1 | uart0_0 |
| 4.5 | uart1_0 |
| 8.9 | uart1_1 |
| 12.13 | uart0_1 |
| 16.17 | uart0_2 |

**Flash:** Copy the generated `.uf2` file to the Pico in bootloader mode (hold BOOTSEL while connecting USB).

### STM32 (ThreadX / Azure RTOS)

**Tested boards:** nucleo-f747zi, nucleo-f429zi, stm32f4xx variants

**Transports:** Serial UART (primary), Ethernet (with LwIP)

**Setup in STM32CubeIDE:**
1. Create project for target MCU in STMCubeIDE
2. In CubeMX: enable Azure RTOS (ThreadX), enable UART with RX DMA in circular mode and UART global interrupt
3. Move HAL_Tick to TIM peripheral (required for ThreadX)
4. Generate init code
5. Clone zenoh-pico into project, add `zenoh-pico/src` to source folders (exclude all `platforms/*` except `common` and `threadx/stm32`)
6. Add to project defines: `ZENOH_THREADX_STM32`, `ZENOH_HUART=huart1` (your UART instance)
7. Set static bytepool size > 25KB
8. Replace `app_threadx.c` with one of the examples from `zenoh-pico/examples/threadx_stm32/`

**STM32 serial publisher example:**
```c
// LOCATOR = "serial/Serial" uses the ZENOH_HUART defined UART
#define MODE "client"
#define LOCATOR "serial/Serial"

VOID start_example_thread(ULONG initial_input) {
    z_owned_config_t config;
    z_owned_session_t s;
    z_result_t r = _Z_ERR_GENERIC;

    // Retry until router is available
    while (r != Z_OK) {
        z_config_default(&config);
        zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, MODE);
        zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, LOCATOR);
        r = z_open(&s, z_move(config), NULL);
    }

    // Start background tasks (ThreadX tasks)
    zp_start_read_task(z_loan_mut(s), NULL);
    zp_start_lease_task(z_loan_mut(s), NULL);

    // Declare and publish
    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str_unchecked(&ke, "stm32/data");
    z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL);

    for (;;) {
        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, "sensor_value");
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
        z_sleep_s(1);
    }
}
```

**Host router command:**
```bash
zenohd -l serial//dev/ttyACM0#baudrate=115200
```

### PX4 (NuttX RTOS)

See [PX4 / NuttX Deployment](#px4-nuttx-deployment) section for complete coverage.

---

## API Model

### The Fundamental Difference: Explicit Network Polling

Full zenoh (Rust) spawns internal threads that continuously poll the network. zenoh-pico does not. The application is responsible for driving network I/O through two mechanisms:

**Option A: Background tasks (RTOS required)**

After `z_open()`, start two background tasks:
```c
zp_start_read_task(z_loan_mut(session), NULL);   // reads from network, triggers callbacks
zp_start_lease_task(z_loan_mut(session), NULL);  // manages keepalives and session lease
```
These create RTOS tasks (FreeRTOS, Zephyr threads, ThreadX threads) that run concurrently. Callbacks are called from the read task context.

**Option B: Manual polling (bare-metal or single-threaded)**

Disable `Z_FEATURE_MULTI_THREAD` and call explicitly:
```c
zp_read(z_loan(session), NULL);            // process one batch of incoming data
zp_send_keep_alive(z_loan(session), NULL); // send session keepalive to router
zp_send_join(z_loan(session), NULL);       // send peer join announcement (peer mode)
```

These must be called often enough that:
- The session lease does not expire (call `zp_send_keep_alive` within `Z_TRANSPORT_LEASE` ms)
- Incoming messages are processed promptly (call `zp_read` in your main loop)

`zp_read()` blocks for up to `Z_CONFIG_SOCKET_TIMEOUT` milliseconds (default 100ms) waiting for data, then returns. Tune this for your response latency requirements.

**Typical single-threaded loop:**
```c
while (1) {
    // Your application logic
    do_sensor_reading();

    // Drive zenoh
    zp_read(z_loan(session), NULL);
    zp_send_keep_alive(z_loan(session), NULL);

    sleep_ms(10);
}
```

### Subscriber Callbacks

Subscriber callbacks in zenoh-pico are synchronous and run in the context of the read task (or `zp_read()` call site). This has important implications:

1. **Must return quickly** — long processing in the callback blocks incoming message processing.
2. **Cannot call zenoh APIs that block** — specifically, do not call `z_get()` from a callback.
3. **Pattern for heavy processing:** Copy data into a queue or shared buffer in the callback, process in main task.

```c
// Volatile flag for signaling from callback to main loop
static volatile bool new_data = false;
static char data_buf[256];

void my_callback(z_loaned_sample_t *sample, void *arg) {
    // FAST: copy data and signal
    z_owned_string_t value;
    z_bytes_to_string(z_sample_payload(sample), &value);
    snprintf(data_buf, sizeof(data_buf), "%.*s",
             (int)z_string_len(z_loan(value)),
             z_string_data(z_loan(value)));
    z_drop(z_move(value));
    new_data = true;
    // Return immediately
}

// Main loop processes data_buf when new_data == true
```

---

## Memory Ownership Model

zenoh-pico uses an explicit ownership model identical to the Rust zenoh API, expressed in C through naming conventions.

### Owned Types (`z_owned_*`)

An owned type holds a resource that must eventually be freed:
```c
z_owned_session_t session;    // owns the session
z_owned_publisher_t pub;      // owns the publisher
z_owned_subscriber_t sub;     // owns the subscriber
z_owned_bytes_t payload;      // owns a byte buffer
z_owned_config_t config;      // owns config (consumed by z_open)
```

Declare owned types uninitialized on the stack (they are initialized by the API calls that populate them).

### Loaned Types (`z_loaned_*`)

A loaned type is a non-owning reference to an owned resource. Most API functions take loaned types:
```c
z_loan(thing)        // borrow immutably: z_owned_T -> const z_loaned_T*
z_loan_mut(thing)    // borrow mutably:   z_owned_T -> z_loaned_T*
```

### View Types (`z_view_*`)

A view type aliases external memory without copying. Use for key expressions from string literals:
```c
z_view_keyexpr_t ke;
z_view_keyexpr_from_str_unchecked(&ke, "sensors/temp");  // no copy, aliases the literal
// ke is valid as long as the string literal lives (forever for string literals)
```

### Moving (`z_move`)

`z_move()` transfers ownership, leaving the source in an invalid state:
```c
z_owned_bytes_t payload;
z_bytes_copy_from_str(&payload, "data");
z_publisher_put(z_loan(pub), z_move(payload), NULL);
// payload is now invalid; do not use it
```

Config is always moved into `z_open()`:
```c
z_owned_config_t config;
z_config_default(&config);
z_open(&session, z_move(config), NULL);  // config consumed here
// Do not use config after this
```

### Dropping (`z_drop`)

Free any owned resource:
```c
z_drop(z_move(sub));      // undeclare subscriber, free resources
z_drop(z_move(pub));      // undeclare publisher
z_drop(z_move(session));  // close session, free all resources
```

### Complete session lifecycle pattern:

```c
#include <zenoh-pico.h>

void my_zenoh_app(void) {
    // 1. Config
    z_owned_config_t config;
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
    zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.1:7447");

    // 2. Open session (config is consumed/moved)
    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        // config is already invalid here whether open succeeded or not
        return;
    }

    // 3. Start I/O tasks
    zp_start_read_task(z_loan_mut(s), NULL);
    zp_start_lease_task(z_loan_mut(s), NULL);

    // 4. Declare subscriber
    z_owned_closure_sample_t cb;
    z_closure(&cb, my_callback, /*dropper=*/NULL, /*context=*/NULL);

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str_unchecked(&ke, "demo/**");

    z_owned_subscriber_t sub;
    z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(cb), NULL);

    // 5. Run application
    while (keep_running) {
        z_sleep_s(1);
    }

    // 6. Cleanup in reverse order
    z_drop(z_move(sub));   // undeclare first
    z_drop(z_move(s));     // then close session
}
```

---

## Serial Transport: Complete Setup Guide

Serial transport connects a zenoh-pico MCU to a full zenoh router on a Linux host via a physical UART link. This is the primary transport for MCUs without an IP stack (STM32, some AVR boards, bare RPi Pico).

### Step 1: Wiring

Standard UART crossing: MCU TX → Host RX, MCU RX → Host TX, common GND.

```
MCU              USB-Serial adapter    Linux Host
TX  ─────────────  RX
RX  ─────────────  TX                  /dev/ttyUSB0
GND ─────────────  GND
```

Common baud rates: 115200, 460800, 921600. Higher speeds may be unreliable on long cables or 3.3V logic.

For STM32: The USB connection through ST-LINK on Nucleo boards creates `/dev/ttyACM0` — this is the UART, not a JTAG interface.

### Step 2: MCU Configuration

**CMake / PlatformIO — enable serial transport:**
```cmake
-DZ_FEATURE_LINK_SERIAL=1
-DZ_FEATURE_LINK_TCP=0        # optional: disable TCP to save code
-DZ_FEATURE_LINK_UDP_UNICAST=0  # optional: disable UDP if not needed
-DZ_FEATURE_SCOUTING=0          # auto-disabled when UDP unicast is OFF
```

**Runtime config:**
```c
z_owned_config_t config;
z_config_default(&config);
zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
// Format: serial/<device_or_pins>#baudrate=<baud>
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY,
                 "serial//dev/ttyS1#baudrate=115200");  // Linux-style device
// OR for RPi Pico:
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY,
                 "serial/0.1#baudrate=115200");  // pin pair TX=0, RX=1
// OR for STM32 ThreadX:
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY,
                 "serial/Serial");  // uses ZENOH_HUART define
```

**Complete ESP32 serial publisher (no WiFi):**
```c
#include <zenoh-pico.h>
// ESP-IDF: Z_FEATURE_LINK_SERIAL=1, Z_FEATURE_LINK_TCP=0

void app_main(void) {
    z_owned_config_t config;
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
    // UART1: GPIO 17 (TX), GPIO 16 (RX) on ESP32
    zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY,
                     "serial/1#baudrate=115200");

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Failed to connect via serial\n");
        return;
    }

    // Start background tasks
    zp_start_read_task(z_loan_mut(s), NULL);
    zp_start_lease_task(z_loan_mut(s), NULL);

    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str_unchecked(&ke, "esp32/serial/data");
    z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL);

    for (int i = 0; ; i++) {
        char buf[64];
        snprintf(buf, sizeof(buf), "serial_msg_%d", i);
        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, buf);
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
```

### Step 3: Host Router Configuration

**Install zenohd:**
```bash
# Option 1: Docker
docker run --init --net host eclipse/zenoh:latest \
  -l serial//dev/ttyUSB0#baudrate=115200

# Option 2: Binary release
# Download from https://github.com/eclipse-zenoh/zenoh/releases
zenohd -l serial//dev/ttyUSB0#baudrate=115200
```

**With explicit JSON5 config** (recommended for production):
```json5
// zenoh-router-serial.json5
{
  mode: "router",
  listen: {
    endpoints: [
      "tcp/0.0.0.0:7447",
      "serial//dev/ttyUSB0#baudrate=115200"
    ]
  }
}
```

```bash
zenohd --config zenoh-router-serial.json5
```

The router now bridges the serial-connected MCU to the TCP/UDP network. Any zenoh subscriber on the network receives data from the MCU, and vice versa.

### Step 4: Testing the Connection

**On host — subscribe to MCU data:**
```bash
z_sub -e tcp/localhost:7447 -k "esp32/**"
```

**On host — publish to MCU:**
```bash
z_pub -e tcp/localhost:7447 -k "mcu/command" -v "start"
```

**Debugging — enable zenoh-pico debug logs:**
```cmake
-DZENOH_LOG=DEBUG
```

This prints framing, session open/close, keepalive events to the MCU's debug output.

### Step 5: Tuning for Reliability

- **Reduce batch sizes** for serial: `BATCH_UNICAST_SIZE=512` prevents fragmentation over slow links
- **Increase socket timeout** if the serial link has delays: `Z_CONFIG_SOCKET_TIMEOUT=500`
- **Use explicit connect** — do not rely on scouting over serial (scouting uses UDP multicast, not serial)
- **Flow control:** Hardware RTS/CTS improves reliability at high baud rates; zenoh-pico serial does not require it but benefits from it

---

## Performance Numbers

These numbers are from live hardware demonstrations (YouTube session OfvVS0oaT6s):

### Throughput

| Platform | Condition | Result |
|----------|-----------|--------|
| ESP32 (240 MHz) | WiFi TCP, small payloads (<64 bytes), local network | **3M+ messages/second** |
| ESP32 | WiFi TCP, 1KB payloads | ~100K messages/second |

### Latency

| Platform | Condition | Result |
|----------|-----------|--------|
| ESP32 | WiFi TCP, local network, end-to-end round trip | **~12µs** |

### Flash Footprint

| Build configuration | Flash usage |
|---------------------|-------------|
| Default build (all features ON) | **~40KB** |
| Minimal pub/sub only (queries, queryables, liveliness, serial, BT, WS all OFF) | **~15KB** |
| Absolute minimum (pub only, no sub, no query, TCP only, no scouting) | **~12KB** |

Footprint reduction flags for 15KB target:
```cmake
-DZ_FEATURE_QUERY=0
-DZ_FEATURE_QUERYABLE=0
-DZ_FEATURE_LIVELINESS=0
-DZ_FEATURE_INTEREST=0
-DZ_FEATURE_LINK_SERIAL=0
-DZ_FEATURE_LINK_BLUETOOTH=0
-DZ_FEATURE_LINK_WS=0
-DZ_FEATURE_MULTICAST_TRANSPORT=0
-DZ_FEATURE_RAWETH_TRANSPORT=0
-DZ_FEATURE_ENCODING_VALUES=0
-DFRAG_MAX_SIZE=512
-DBATCH_UNICAST_SIZE=512
```

---

## zenoh-pico vs micro-ROS

| Feature | zenoh-pico | micro-ROS |
|---------|------------|-----------|
| **Flash footprint (minimal)** | ~15KB | ~100KB+ |
| **Protocol** | Zenoh native (binary, compact) | DDS RTPS over XRCE-DDS |
| **Middleware dependency** | None — standalone C library | ROS 2 required on host for DDS bridge |
| **Transports** | Serial, TCP, UDP unicast/multicast, BLE, raw Ethernet, TLS | Serial, UDP |
| **Discovery** | Zenoh scouting (UDP multicast or explicit) | DDS SPDP via micro-XRCE agent |
| **ROS 2 integration** | Via zenoh-ros2-bridge (not built-in) | Native — topics/services/actions |
| **Non-ROS systems** | First-class — any zenoh node on any language | Via bridge only |
| **Querying stored data** | Built-in (z_get / queryable) | Not available |
| **Geo-distributed systems** | Supported via zenoh routers | Not designed for this |
| **Programming model** | Polling (explicit read tasks) | Polling (spin tasks) |
| **C++ support** | C API only (use C++ wrapper project) | Native C++ |
| **License** | EPL 2.0 / Apache 2.0 | Apache 2.0 |
| **When to choose** | Non-ROS systems, minimal footprint, heterogeneous networks, robots needing zenoh infrastructure | ROS 2 robot systems, need native topic/service/action compatibility |

**Where each excels (from live deployment experience):**

*zenoh-pico wins when:*
- The embedded device needs to talk to non-ROS systems (cloud, databases, web)
- Footprint is critical (<32KB flash targets)
- Serial is the only transport (no IP stack)
- The wider system uses zenoh for data fabric (not ROS)
- Real-time fieldbus replacement (raw Ethernet transport)

*micro-ROS wins when:*
- The embedded device participates in a ROS 2 system with full topic/service/action semantics
- You need `rclcpp` or `rclc` node model
- The rest of the system uses ROS 2 tooling (rviz, rosbag, ros2 topic echo)

---

## Footprint Optimization Recipes

### Recipe: Sensor Node (publish only, no WiFi, serial transport)

Target: MCU with 64KB flash, no IP stack, UART to zenoh router.

```cmake
# CMake flags
-DZ_FEATURE_SUBSCRIPTION=0      # no subscribing
-DZ_FEATURE_QUERY=0              # no queries
-DZ_FEATURE_QUERYABLE=0          # no queryable
-DZ_FEATURE_LIVELINESS=0         # no liveliness
-DZ_FEATURE_INTEREST=0           # disables matching too
-DZ_FEATURE_ENCODING_VALUES=0    # no encoding table
-DZ_FEATURE_MULTICAST_TRANSPORT=0  # no multicast
-DZ_FEATURE_LINK_TCP=0           # no TCP
-DZ_FEATURE_LINK_UDP_UNICAST=0   # no UDP unicast
-DZ_FEATURE_LINK_UDP_MULTICAST=0 # no UDP multicast
-DZ_FEATURE_SCOUTING=0           # no scouting (auto-disabled anyway)
-DZ_FEATURE_LINK_SERIAL=1        # serial only
-DZ_FEATURE_LINK_BLUETOOTH=0
-DZ_FEATURE_LINK_WS=0
-DZ_FEATURE_FRAGMENTATION=0      # only if all payloads < batch size
-DFRAG_MAX_SIZE=256
-DBATCH_UNICAST_SIZE=256
-DBATCH_MULTICAST_SIZE=256
```

Expected result: ~12–15KB flash, ~1KB RAM for buffers.

### Recipe: Subscriber-only node (receive sensor data, no sending)

```cmake
-DZ_FEATURE_PUBLICATION=0
-DZ_FEATURE_QUERY=0
-DZ_FEATURE_QUERYABLE=0
-DZ_FEATURE_LIVELINESS=0
-DBATCH_UNICAST_SIZE=512
-DFRAG_MAX_SIZE=1024
```

### Recipe: Full-featured IoT node (pub/sub + queries, WiFi TCP)

Default configuration with reduced buffer sizes for constrained memory:

```cmake
# Keep all features ON but tune buffers
-DBATCH_UNICAST_SIZE=1024
-DBATCH_MULTICAST_SIZE=1024
-DFRAG_MAX_SIZE=2048
```

This targets ~40KB flash with ~6KB RAM for transport buffers.

---

## PX4 / NuttX Deployment

PX4 runs NuttX RTOS on ARM Cortex-M flight controllers. The primary use case (from YouTube session rOqDWM7vYVM) is connecting the flight controller to a companion computer (e.g., Raspberry Pi 5 or Jetson) running full zenoh, using the companion as a zenoh router.

### Topology

```
PX4 (NuttX)           Companion Computer (Linux)
zenoh-pico  <─────>  zenoh router  <────> Cloud / GCS
  UDP multicast         eth0
  or serial
```

### UDP Multicast Discovery (Ethernet)

When the flight controller and companion computer share an Ethernet segment (common in drones with an Ethernet switch on the carrier board):

**PX4 side (zenoh-pico):**
```c
z_owned_config_t config;
z_config_default(&config);
zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
// Use multicast scouting to find the router on Ethernet
zp_config_insert(z_loan_mut(config), Z_CONFIG_MULTICAST_SCOUTING_KEY, "true");
// OR explicit connect:
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "udp/192.168.1.10:7447");
```

**Companion computer (router):**
```bash
zenohd -l udp/0.0.0.0:7447 -l tcp/0.0.0.0:7447
```

### Failover Redundancy

The NXP PX4 deployment demonstrated primary + backup zenoh connections for redundancy. Pattern:

```c
// Try primary connection, fall back to secondary
z_owned_config_t config;
z_config_default(&config);
zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
// zenoh-pico: try primary endpoint
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.10:7447");

z_owned_session_t s;
z_result_t r = z_open(&s, z_move(config), NULL);
if (r < 0) {
    // Fall back to secondary
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
    zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.11:7447");
    r = z_open(&s, z_move(config), NULL);
}
```

With `Z_FEATURE_AUTO_RECONNECT=1` (default), the session automatically attempts reconnection if the router drops — this is the primary failover mechanism in production deployments.

### Flight Data Patterns

Typical PX4 + zenoh-pico data flow:
- Flight controller publishes: `px4/sensors/imu`, `px4/sensors/gps`, `px4/actuators/output`
- Companion subscribes: aggregates, logs, or forwards to cloud
- GCS subscribes via router: receives telemetry without being directly connected to PX4

**NuttX-specific notes:**
- NuttX POSIX-compatible; zenoh-pico compiles with `-DPOSIX_COMPATIBLE=ON` or as a standard Unix build
- UDP multicast on NuttX requires the network interface name (e.g., `eth0`) in the multicast locator
- Serial transport on NuttX uses standard POSIX device paths: `serial//dev/ttyS1#baudrate=921600`
- Stack size: zenoh-pico's read and lease tasks require ~4KB stack each; configure NuttX task stacks accordingly

### Production Considerations

1. **Reduce batch sizes** for limited flight controller RAM: `BATCH_UNICAST_SIZE=1024`, `FRAG_MAX_SIZE=2048`
2. **Disable unused features**: If the flight controller only publishes sensor data, disable SUBSCRIPTION, QUERY, QUERYABLE
3. **Use explicit connect** rather than scouting to avoid startup delays during critical flight phases
4. **Monitor session lease**: Set `Z_TRANSPORT_LEASE=3000` for faster detection of dropped router connections
5. **Enable AUTO_RECONNECT**: Default ON; ensures session recovery after link interruptions without application restart

---

## Quick Reference: Complete Minimal Build

The smallest possible zenoh-pico build that publishes over serial:

**platformio.ini:**
```ini
[env:minimal_serial_pub]
platform = ststm32
board = nucleo_f767zi
framework = zephyr
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
board_build.cmake_extra_args =
  -DZ_FEATURE_SUBSCRIPTION=0
  -DZ_FEATURE_QUERY=0
  -DZ_FEATURE_QUERYABLE=0
  -DZ_FEATURE_LIVELINESS=0
  -DZ_FEATURE_INTEREST=0
  -DZ_FEATURE_ENCODING_VALUES=0
  -DZ_FEATURE_MULTICAST_TRANSPORT=0
  -DZ_FEATURE_LINK_TCP=0
  -DZ_FEATURE_LINK_UDP_UNICAST=0
  -DZ_FEATURE_LINK_UDP_MULTICAST=0
  -DZ_FEATURE_LINK_SERIAL=1
  -DZ_FEATURE_FRAGMENTATION=0
  -DBATCH_UNICAST_SIZE=256
  -DFRAG_MAX_SIZE=256
```

**main.c:**
```c
#include <zenoh-pico.h>

int main(void) {
    z_owned_config_t config;
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
    zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY,
                     "serial//dev/ttyACM0#baudrate=115200");

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) return -1;

    zp_start_read_task(z_loan_mut(s), NULL);
    zp_start_lease_task(z_loan_mut(s), NULL);

    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str_unchecked(&ke, "mcu/data");
    z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL);

    for (;;) {
        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, "hello");
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
        z_sleep_s(1);
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));
    return 0;
}
```

**Host router:**
```bash
zenohd -l serial//dev/ttyACM0#baudrate=115200 -l tcp/0.0.0.0:7447
```

Expected flash: ~12–15KB for Zephyr + zenoh-pico with the above flags.

## See Also

- [Pico vs Full Guide](pico-vs-full-guide.md) — when to use zenoh-pico vs zenoh-c vs full Rust zenoh
- [Zephyr Guide](zephyr-guide.md) — Zephyr RTOS-specific setup, Kconfig options, and board examples
- [Programming Model Guide](programming-model-guide.md) — the full Zenoh API that zenoh-pico implements in C
- [Key Expressions Guide](key-expressions-guide.md) — key expression syntax used in zenoh-pico's `z_keyexpr_from_str` functions
