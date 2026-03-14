# zenoh-pico: Comprehensive Embedded Documentation

## Table of Contents

1. [What is zenoh-pico?](#1-what-is-zenoh-pico)
2. [Supported Platforms & Transport Matrix](#2-supported-platforms--transport-matrix)
3. [Installation & Build](#3-installation--build)
4. [Compile-Time Feature Flags](#4-compile-time-feature-flags)
5. [Runtime Configuration](#5-runtime-configuration)
6. [Core Concepts & API](#6-core-concepts--api)
7. [API Reference Overview](#7-api-reference-overview)
8. [Differences from Full Zenoh](#8-differences-from-full-zenoh)
9. [Getting Started Examples](#9-getting-started-examples)
10. [Memory Optimization](#10-memory-optimization)
11. [Debugging & Troubleshooting](#11-debugging--troubleshooting)
12. [Adding a Custom Platform](#12-adding-a-custom-platform)

---

## 1. What is zenoh-pico?

**zenoh-pico** is the native C implementation of the [Eclipse Zenoh](https://zenoh.io/) protocol, purpose-built for microcontrollers and deeply constrained embedded systems. It provides a lightweight, feature-selective subset of the full Zenoh functionality in a C API that can run without an operating system, on an RTOS, or bare-metal.

### Key Properties

| Property | Detail |
|---|---|
| **Language** | Pure C (C99/C11) |
| **Compatibility** | Wire-protocol compatible with Rust zenoh and zenoh-c |
| **Footprint** | Configurable; can be stripped to a minimal pub/sub-only build |
| **Threading model** | Optional; can run fully single-threaded with manual task spinning |
| **Dynamic memory** | Minimized; buffer sizes are compile-time constants |
| **License** | EPL-2.0 OR Apache-2.0 |

### What zenoh-pico Provides

- **Pub/Sub** — Declare publishers and subscribers with key-expression routing
- **Queryable/Get** — Request/reply pattern (optional)
- **Liveliness** — Detect peer presence (optional)
- **Scouting** — Automatic peer/router discovery via UDP multicast (optional)
- **Serialization helpers** — Typed encode/decode for common primitives
- **Multiple transports** — TCP, UDP unicast, UDP multicast, Serial, Bluetooth, WebSocket, TLS (platform-dependent)
- **Client and Peer modes** — Connect to a router or operate P2P

### What zenoh-pico Does NOT Provide (vs. Full Zenoh)

- Built-in storage backends
- Full async Rust runtime
- Admin REST API (admin space is optional and limited)
- Plugin system
- Some advanced routing optimizations present only in the router

---

## 2. Supported Platforms & Transport Matrix

### Full Platform × Transport Matrix

| **(RT)OS** | **TCP** | **UDP Unicast** | **UDP Multicast** | **Serial** | **Bluetooth (Serial)** | **WebSocket** | **TLS** | **Network Layers** | **Data Links** |
|---|---|---|---|---|---|---|---|---|---|
| **Linux / macOS / BSD** | ✅ | ✅ | ✅ | ✅ | — | — | ✅ | IPv4, IPv6, 6LoWPAN | WiFi, Ethernet, Thread |
| **Windows** | ✅ | ✅ | ✅ | — | — | — | ✅ | IPv4, IPv6 | WiFi, Ethernet |
| **Zephyr RTOS** | ✅ | ✅ | ✅ | ✅ | — | — | ✅ | IPv4, IPv6, 6LoWPAN | WiFi, Ethernet, Thread, Serial |
| **Arduino** | ✅ | ✅ | ✅ | ✅ | ✅ (Serial profile) | — | — | IPv4, IPv6 | WiFi, Ethernet, BT Serial |
| **ESP-IDF** | ✅ | ✅ | ✅ | ✅ | — | — | — | IPv4, IPv6 | WiFi, Ethernet |
| **MbedOS** | ✅ | ✅ | ✅ | ✅ | — | — | — | IPv4, IPv6 | WiFi, Ethernet |
| **OpenCR** | ✅ | ✅ | ✅ | — | — | — | — | IPv4 | WiFi |
| **FreeRTOS-Plus-TCP** | ✅ | ✅ | — | — | — | — | — | IPv4 | Ethernet |
| **FreeRTOS + LWIP** | ✅ | ✅ | ✅ | — | — | — | — | IPv4 | Ethernet |
| **Raspberry Pi Pico** | ✅ (Pico W) | ✅ (Pico W) | ✅ (Pico W) | ✅ | — | — | — | IPv4 | WiFi (W models), Serial, USB CDC |
| **Emscripten** | — | — | — | — | — | ✅ | — | IPv4, IPv6 | WiFi, Ethernet |
| **STM32 ThreadX** | — | — | — | ✅ | — | — | — | — | UART |
| **Generic/Bare-metal** | platform-defined | platform-defined | — | platform-defined | — | — | — | platform-defined | platform-defined |

### Zephyr RTOS — Tested Boards

| Board | Notes |
|---|---|
| `reel_board` | Nordic nRF52840-based |
| `nucleo-f767zi` | STM32F767ZI |
| `nucleo-f420zi` | STM32F420ZI |
| `nRF52840` DK | Nordic Bluetooth/Thread SoC |

Zephyr supports the widest transport selection of any RTOS target, including 6LoWPAN over Thread networks.

### Arduino — Tested Boards

| Board | Platform | Notes |
|---|---|---|
| `az-delivery-devkit-v4` | ESP32 | WiFi via Arduino WiFi library |
| `OpenCR 1.0` | ROBOTIS OpenCR | ROS-capable board |
| Various Arduino-compatible | Various | Any board with WiFi/Ethernet/Serial support |

### Raspberry Pi Pico — Board Variants

| Board | WiFi | UART Serial | USB CDC Serial |
|---|---|---|---|
| Pico | — | ✅ | Experimental |
| Pico W | ✅ | ✅ | Experimental |
| Pico 2 | — | ✅ | Experimental |
| Pico 2 W | ✅ | ✅ | Experimental |

**RPi Pico UART pin assignments:**

| TX/RX Pins | Device Name | UART Instance |
|---|---|---|
| 0 / 1 | `uart0_0` | UART0 |
| 4 / 5 | `uart1_0` | UART1 |
| 8 / 9 | `uart1_1` | UART1 |
| 12 / 13 | `uart0_1` | UART0 |
| 16 / 17 | `uart0_2` | UART0 |

---

## 3. Installation & Build

### 3.1 Linux / macOS / BSD (CMake)

```bash
cd /path/to/zenoh-pico
make               # Release build
make install       # sudo required on Linux

# Debug build
BUILD_TYPE=Debug make
make install
```

Alternatively with explicit CMake:

```bash
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
make install
```

**Key CMake options at configure time:**

```bash
cmake .. \
  -DCMAKE_BUILD_TYPE=Release \
  -DBATCH_UNICAST_SIZE=1024 \
  -DBATCH_MULTICAST_SIZE=1024 \
  -DFRAG_MAX_SIZE=2048 \
  -DZ_FEATURE_PUBLICATION=1 \
  -DZ_FEATURE_SUBSCRIPTION=1 \
  -DZ_FEATURE_QUERY=0 \
  -DZ_FEATURE_QUERYABLE=0 \
  -DZ_FEATURE_LIVELINESS=0 \
  -DZENOH_LOG=INFO
```

### 3.2 Zephyr RTOS (PlatformIO)

Project structure:
```
project_dir/
├── src/main.c
├── zephyr/
│   ├── prj.conf
│   └── CMakeLists.txt
└── platformio.ini
```

`platformio.ini`:
```ini
[env:reel_board]
platform = nordicnrf52
board = reel_board
framework = zephyr
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
board_build.cmake_extra_args =
    -DBATCH_UNICAST_SIZE=1024
    -DFRAG_MAX_SIZE=2048
    -DZ_FEATURE_QUERY=0
    -DZ_FEATURE_QUERYABLE=0
```

Build and flash:
```bash
platformio run
platformio run -t upload
```

### 3.3 Arduino / ESP32 (PlatformIO)

Project structure:
```
project_dir/
├── src/main.ino
└── platformio.ini
```

`platformio.ini`:
```ini
[env:az-delivery-devkit-v4]
platform = espressif32
board = az-delivery-devkit-v4
framework = arduino
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
board_build.cmake_extra_args =
    -DBATCH_UNICAST_SIZE=1024
    -DFRAG_MAX_SIZE=2048
```

### 3.4 ESP-IDF (PlatformIO)

```ini
[env:az-delivery-devkit-v4]
platform = espressif32
board = az-delivery-devkit-v4
framework = espidf
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
```

### 3.5 Raspberry Pi Pico SDK

Install prerequisites:
```bash
sudo apt update
sudo apt install -y cmake gcc-arm-none-eabi libnewlib-arm-none-eabi \
    build-essential g++ libstdc++-arm-none-eabi-newlib
```

Set up the Pico SDK:
```bash
export PICO_SDK_PATH=$HOME/src/pico-sdk
git clone https://github.com/raspberrypi/pico-sdk.git $PICO_SDK_PATH
cd $PICO_SDK_PATH && git submodule update --init
```

Set up FreeRTOS (required for Pico examples):
```bash
export FREERTOS_KERNEL_PATH=$HOME/src/FreeRTOS-Kernel
git clone https://github.com/FreeRTOS/FreeRTOS-Kernel.git $FREERTOS_KERNEL_PATH
cd $FREERTOS_KERNEL_PATH && git submodule update --init
```

Build for Pico W with WiFi:
```bash
cd examples/rpi_pico
cmake -Bbuild \
    -DPICO_BOARD=pico_w \
    -DWIFI_SSID="MyNetwork" \
    -DWIFI_PASSWORD="MyPassword" \
    -DZENOH_CONFIG_MODE=client \
    -DZENOH_CONFIG_CONNECT="tcp/192.168.1.100:7447"
cmake --build ./build
```

Flash: copy the generated `.uf2` file to the Pico when it appears as a USB drive (hold BOOTSEL while connecting).

**Serial transport connect string examples:**
```bash
# By pin numbers (TX.RX)
-DZENOH_CONFIG_CONNECT="serial/0.1#baudrate=115200"
# By device name
-DZENOH_CONFIG_CONNECT="serial/uart1_0#baudrate=38400"
# USB CDC (requires Z_FEATURE_LINK_SERIAL_USB and Z_FEATURE_UNSTABLE_API)
-DZENOH_CONFIG_CONNECT="serial/usb#baudrate=115200"
```

### 3.6 STM32 ThreadX

1. Create a new STM32CubeIDE project for your target MCU.
2. In CubeMX:
   - Add Azure RTOS (ThreadX) middleware.
   - Enable UART with RX DMA in circular mode and global interrupt.
   - Move HAL_Tick to a TIM peripheral.
3. Generate code, then clone zenoh-pico into the project folder.
4. Add `zenoh-pico/src` to source folders; exclude all `platforms/*` except `common` and `threadx/stm32`.
5. Add `zenoh-pico/include` to include paths.
6. Add a `hal.h` file: `#include "stm32f4xx_hal.h"` (adjust for your MCU).
7. Add project defines:
   - `ZENOH_THREADX_STM32`
   - `ZENOH_HUART=huart1` (or whichever UART)
8. Set static bytepool size > 25 KB.
9. On host, run: `zenohd -l serial//dev/ttyACM0#baudrate=115200`

---

## 4. Compile-Time Feature Flags

All feature flags are defined in `include/zenoh-pico/config.h` (generated from `config.h.in` by CMake) and can be overridden via CMake arguments or `platformio.ini`'s `board_build.cmake_extra_args`.

### 4.1 Core Communication Features

---

#### `Z_FEATURE_PUBLICATION`
**Default:** `1` (ON)

Enables the publication API: `z_put()`, `z_declare_publisher()`, `z_publisher_put()`, `z_publisher_delete()`.

Without this flag, the device cannot send any data into the zenoh network.

**When to disable:** Receive-only nodes (e.g., sensor aggregators that only subscribe), display nodes, actuators controlled purely by subscription.

**Memory impact:** Removing saves code space for all publisher data path logic (~1–4 KB depending on platform).

---

#### `Z_FEATURE_SUBSCRIPTION`
**Default:** `1` (ON)

Enables the subscription API: `z_declare_subscriber()`, `z_declare_background_subscriber()`.

Without this flag, the device cannot receive published data.

**When to disable:** Transmit-only sensor nodes that never need to receive data.

**Memory impact:** Removes subscriber dispatch table and callback infrastructure.

---

#### `Z_FEATURE_QUERY`
**Default:** `1` (ON)

Enables the query (get) API: `z_get()`, `z_declare_querier()`. Allows the device to issue queries and receive replies from queryables.

**When to disable:** Devices that only publish/subscribe and never need to query stored data or services.

---

#### `Z_FEATURE_QUERYABLE`
**Default:** `1` (ON)

Enables the queryable API: `z_declare_queryable()`. Allows the device to respond to incoming queries.

**When to disable:** Devices that are pure data producers/consumers, not service providers.

---

#### `Z_FEATURE_LIVELINESS`
**Default:** `1` (ON)

Enables liveliness tokens and liveliness subscriptions. Allows detection of peer presence/absence.

**When to disable:** Systems that do not need peer health monitoring. Saves both code and a small amount of session state.

**Dependencies:** Required by `Z_FEATURE_ADVANCED_PUBLICATION` and `Z_FEATURE_ADVANCED_SUBSCRIPTION`.

---

#### `Z_FEATURE_SCOUTING`
**Default:** `1` (ON)

Enables UDP multicast scouting for automatic router/peer discovery. When enabled, a node without an explicit connect/listen endpoint will attempt to find peers automatically.

**When to disable:** Always-connected systems with static router addresses. Saves UDP socket management code.

**Dependency:** Requires `Z_FEATURE_LINK_UDP_UNICAST`. If UDP unicast is disabled, scouting is automatically disabled.

---

#### `Z_FEATURE_FRAGMENTATION`
**Default:** `1` (ON)

Enables message fragmentation/defragmentation. Without this, the device cannot send or receive messages larger than the batch buffer size (`Z_BATCH_UNICAST_SIZE` or `Z_BATCH_MULTICAST_SIZE`).

**When to disable:** Devices with very limited RAM that only exchange small messages. The defragmentation buffer (`Z_FRAG_MAX_SIZE`, default 4096 bytes) is the largest single buffer in zenoh-pico; disabling fragmentation eliminates it entirely.

**Memory impact:** Eliminating the 4096-byte defrag buffer is one of the most impactful memory savings available.

---

#### `Z_FEATURE_BATCHING`
**Default:** `1` (ON)

Enables message batching (packing multiple messages into one transport packet). Improves throughput at the cost of slightly increased latency.

**When to disable:** Ultra-low-latency systems where every message must be sent immediately. Very low-memory systems can save the batch buffer logic.

---

### 4.2 Transport & Link Features

---

#### `Z_FEATURE_LINK_TCP`
**Default:** `1` (ON)

Enables TCP transport. TCP provides reliable, ordered delivery and is the most common transport for connecting to a zenoh router.

**When to disable:** Systems using only UDP, Serial, or other transports. Saves TCP socket management code.

---

#### `Z_FEATURE_LINK_UDP_UNICAST`
**Default:** `1` (ON)

Enables UDP unicast transport. Used for unicast point-to-point communication without TCP overhead. Also required for scouting.

**When to disable:** TCP-only or serial-only systems.

---

#### `Z_FEATURE_LINK_UDP_MULTICAST`
**Default:** `1` (ON)

Enables UDP multicast transport. Used for peer-to-peer multicast communication (peer mode without a router).

**When to disable:** Client-mode-only devices that always connect to a router via TCP/unicast. Saves multicast group management code.

---

#### `Z_FEATURE_LINK_SERIAL`
**Default:** `0` (OFF)

Enables serial (UART) transport. Used to connect to a zenoh router over a physical serial link — ideal for microcontrollers without network hardware.

**When to enable:** Any device using UART to communicate with a router or another embedded node.

**Typical use:** RPi Pico without WiFi, STM32 boards, Arduino without network shields.

---

#### `Z_FEATURE_LINK_SERIAL_USB`
**Default:** `0` (OFF)

Enables USB CDC (virtual serial) transport. **Experimental.**

**Dependency:** Requires both `Z_FEATURE_LINK_SERIAL` and `Z_FEATURE_UNSTABLE_API`.

---

#### `Z_FEATURE_LINK_BLUETOOTH`
**Default:** `0` (OFF)

Enables Bluetooth Serial Profile transport. Available on Arduino-compatible boards with Bluetooth.

**When to enable:** Systems communicating over Bluetooth to a router or another node.

---

#### `Z_FEATURE_LINK_WS`
**Default:** `0` (OFF)

Enables WebSocket transport. Used by Emscripten (browser) targets.

---

#### `Z_FEATURE_LINK_TLS`
**Default:** `0` (OFF)

Enables TLS transport for encrypted TCP connections. Uses **Mbed TLS** (versions 2.x or 3.x supported; 4.x not supported).

**When to enable:** Production deployments requiring encryption and/or mutual authentication.

**Memory impact:** Significant. Mbed TLS adds substantial code and RAM overhead; evaluate carefully for constrained targets.

---

### 4.3 Threading & Task Management

---

#### `Z_FEATURE_MULTI_THREAD`
**Default:** `1` (ON)

Enables multi-threading support. When ON, background read and lease tasks can be started with `zp_start_read_task()` and `zp_start_lease_task()`, which run in separate threads.

When OFF, the library is single-threaded only. You must manually call `zp_read()` and `zp_send_keep_alive()` in your main loop.

**When to disable:** Bare-metal or RTOS systems without POSIX thread support, or systems where you want full manual control of timing.

**Dependencies:** `Z_FEATURE_UNICAST_PEER` and `Z_FEATURE_ADVANCED_SUBSCRIPTION` require this to be ON.

---

#### `Z_FEATURE_AUTO_RECONNECT`
**Default:** `1` (ON)

Enables automatic reconnection when a transport link is lost. The library will attempt to re-establish the connection transparently.

**When to disable:** Systems where reconnection must be application-controlled, or where the overhead of reconnection logic is unacceptable.

---

### 4.4 Local Loopback Features

---

#### `Z_FEATURE_LOCAL_SUBSCRIBER`
**Default:** `0` (OFF)

When ON, subscribers are triggered by publications made by the same session (local loopback). By default, local publications do not trigger local subscribers — they go only to the network.

**When to enable:** Systems where a single node both publishes and subscribes to the same key expression and needs local delivery.

**Memory impact:** Minimal code addition; slightly increases dispatch overhead.

---

#### `Z_FEATURE_LOCAL_QUERYABLE`
**Default:** `0` (OFF)

When ON, queryables are triggered by queries made by the same session (local loopback).

---

### 4.5 Advanced & Unstable Features

---

#### `Z_FEATURE_UNSTABLE_API`
**Default:** `0` (OFF)

Gates compilation of unstable APIs that may change in future releases. Required to enable:
- `Z_FEATURE_LINK_SERIAL_USB`
- `Z_FEATURE_PERIODIC_TASKS`
- `Z_FEATURE_ADVANCED_PUBLICATION`
- `Z_FEATURE_ADVANCED_SUBSCRIPTION`
- `Z_FEATURE_ADMIN_SPACE`

---

#### `Z_FEATURE_ADVANCED_PUBLICATION` *(Unstable)*
**Default:** `0` (OFF)

Enables advanced publisher with sample cache, allowing late-joining subscribers to retrieve missed samples.

**Dependencies:** `Z_FEATURE_UNSTABLE_API`, `Z_FEATURE_PUBLICATION`, `Z_FEATURE_LIVELINESS`

---

#### `Z_FEATURE_ADVANCED_SUBSCRIPTION` *(Unstable)*
**Default:** `0` (OFF)

Enables advanced subscriber with missed-sample detection and recovery.

**Dependencies:** `Z_FEATURE_UNSTABLE_API`, `Z_FEATURE_SUBSCRIPTION`, `Z_FEATURE_LIVELINESS`, `Z_FEATURE_MULTI_THREAD`

---

#### `Z_FEATURE_MATCHING`
**Default:** `1` (ON)

Enables matching status listeners — notifications when a publisher gains or loses matching subscribers (or vice versa).

**Dependency:** Requires `Z_FEATURE_INTEREST`.

---

#### `Z_FEATURE_ADMIN_SPACE` *(Unstable)*
**Default:** `0` (OFF)

Exposes internal runtime state (transports, peers, links) via a queryable namespace, useful for diagnostics.

**Dependency:** Requires `Z_FEATURE_UNSTABLE_API`.

---

### 4.6 Feature Flag Quick Reference Table

| Flag | Default | Description | Can Safely Disable When... |
|---|---|---|---|
| `Z_FEATURE_PUBLICATION` | ON | Publish data | Receive-only node |
| `Z_FEATURE_SUBSCRIPTION` | ON | Subscribe to data | Transmit-only node |
| `Z_FEATURE_QUERY` | ON | Issue queries | No query/reply pattern needed |
| `Z_FEATURE_QUERYABLE` | ON | Respond to queries | Not a service provider |
| `Z_FEATURE_LIVELINESS` | ON | Peer presence detection | No health monitoring needed |
| `Z_FEATURE_SCOUTING` | ON | Auto router discovery | Static router address configured |
| `Z_FEATURE_FRAGMENTATION` | ON | Large message support | Only small messages (<2 KB) |
| `Z_FEATURE_BATCHING` | ON | Message batching | Ultra-low-latency required |
| `Z_FEATURE_MULTI_THREAD` | ON | Background thread tasks | Single-thread / bare-metal |
| `Z_FEATURE_AUTO_RECONNECT` | ON | Automatic reconnection | App-controlled reconnect |
| `Z_FEATURE_LINK_TCP` | ON | TCP transport | Serial/UDP-only systems |
| `Z_FEATURE_LINK_UDP_UNICAST` | ON | UDP unicast | TCP/Serial-only systems |
| `Z_FEATURE_LINK_UDP_MULTICAST` | ON | UDP multicast | Client-only, no P2P needed |
| `Z_FEATURE_LINK_SERIAL` | OFF | UART transport | Network-connected systems |
| `Z_FEATURE_LINK_BLUETOOTH` | OFF | Bluetooth transport | No Bluetooth hardware |
| `Z_FEATURE_LINK_WS` | OFF | WebSocket transport | Non-browser targets |
| `Z_FEATURE_LINK_TLS` | OFF | TLS encryption | Trusted/internal networks |
| `Z_FEATURE_LOCAL_SUBSCRIBER` | OFF | Local pub→sub loopback | No local delivery needed |
| `Z_FEATURE_LOCAL_QUERYABLE` | OFF | Local query→queryable loopback | No local queries |
| `Z_FEATURE_MATCHING` | ON | Matching status listener | No subscriber tracking needed |
| `Z_FEATURE_UNSTABLE_API` | OFF | Unstable API gate | Stable production builds |
| `Z_FEATURE_ADVANCED_PUBLICATION` | OFF | Publisher sample cache | No late-joiner support |
| `Z_FEATURE_ADVANCED_SUBSCRIPTION` | OFF | Subscriber miss detection | No reliability guarantees |
| `Z_FEATURE_ADMIN_SPACE` | OFF | Runtime diagnostic queries | No external diagnostics |
| `Z_FEATURE_ENCODING_VALUES` | ON | Encoding constants | Custom encoding only |
| `Z_FEATURE_SESSION_CHECK` | ON | Publisher/querier session check | Maximum performance mode |

---

## 5. Runtime Configuration

Runtime configuration is applied before opening a session using `zp_config_insert()`.

### 5.1 Buffer Size Parameters (CMake / compile-time)

These are the most critical parameters for memory-constrained devices:

| Parameter | CMake Variable | Default | Description |
|---|---|---|---|
| Defragmentation buffer | `FRAG_MAX_SIZE` | `4096` | Maximum size (bytes) of a reassembled fragmented message. Any incoming message larger than this is dropped. |
| Unicast batch buffer | `BATCH_UNICAST_SIZE` | `2048` | Maximum packet size (bytes) in client/unicast mode. Larger messages are fragmented. |
| Multicast batch buffer | `BATCH_MULTICAST_SIZE` | `2048` | Maximum packet size (bytes) in peer/multicast mode. |

> **Warning:** Multicast batch sizes must match across all nodes in a multicast group. Linux/Windows defaults are 65535; macOS defaults to 9216; zenoh-pico defaults to 2048 (or 8192 for other Zenoh implementations). Mismatch causes session open failures.

**Setting via CMake:**
```bash
cmake .. \
  -DBATCH_UNICAST_SIZE=1024 \
  -DBATCH_MULTICAST_SIZE=1024 \
  -DFRAG_MAX_SIZE=2048
```

**Setting via platformio.ini:**
```ini
board_build.cmake_extra_args =
    -DBATCH_UNICAST_SIZE=1024
    -DFRAG_MAX_SIZE=2048
```

### 5.2 Session & Timing Parameters

| Parameter | CMake Variable | Default | Description |
|---|---|---|---|
| Socket timeout | `Z_CONFIG_SOCKET_TIMEOUT` | `100` ms | Timeout for blocking socket operations |
| Transport lease | `Z_TRANSPORT_LEASE` | `10000` ms | Maximum time without receiving a message before closing a connection |
| Lease expire factor | `Z_TRANSPORT_LEASE_EXPIRE_FACTOR` | `3` | Divisor for calculating keep-alive interval (`lease / factor`) |
| Join interval | `Z_JOIN_INTERVAL` | configured | Delay between multicast join messages (ms) |
| Scouting timeout | `Z_CONFIG_SCOUTING_TIMEOUT_DEFAULT` | configured | How long to wait for scouting replies (ms) |

### 5.3 Periodic Scheduler

| Parameter | CMake Variable | Default | Description |
|---|---|---|---|
| Max scheduler tasks | `ZP_PERIODIC_SCHEDULER_MAX_TASKS` | `64` | Maximum number of concurrent periodic task slots |

Reduce this on very constrained systems if you use fewer periodic tasks.

### 5.4 Runtime Configuration Keys

Use `zp_config_insert(z_loan(cfg), key, value)` with the following keys:

```c
z_owned_config_t cfg;
z_config_default(&cfg);

// Set client mode
zp_config_insert(z_loan(cfg), Z_CONFIG_MODE_KEY, Z_CONFIG_MODE_CLIENT);

// Connect to a specific router
zp_config_insert(z_loan(cfg), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.100:7447");

// Or listen (peer mode)
zp_config_insert(z_loan(cfg), Z_CONFIG_LISTEN_KEY, "udp/224.0.0.123:7447#iface=eth0");

// Disable multicast scouting (when router address is known)
zp_config_insert(z_loan(cfg), Z_CONFIG_MULTICAST_SCOUTING_KEY, "false");

// Custom session ID
zp_config_insert(z_loan(cfg), Z_CONFIG_SESSION_ZID_KEY, "aabbccddeeff00112233445566778899");
```

#### Mode Keys
- `Z_CONFIG_MODE_KEY` — `Z_CONFIG_MODE_CLIENT` or `Z_CONFIG_MODE_PEER`

#### Connectivity Keys
- `Z_CONFIG_CONNECT_KEY` — Endpoint to connect to (e.g., `tcp/192.168.1.1:7447`, `serial/0.1#baudrate=115200`)
- `Z_CONFIG_LISTEN_KEY` — Endpoint to listen on (peer mode)

#### Scouting Keys
- `Z_CONFIG_MULTICAST_SCOUTING_KEY` — `"true"` / `"false"`
- `Z_CONFIG_MULTICAST_LOCATOR_KEY` — Multicast address for scouting (default: `udp/224.0.0.224:7447`)
- `Z_CONFIG_SCOUTING_TIMEOUT_KEY` — Timeout in milliseconds
- `Z_CONFIG_SCOUTING_WHAT_KEY` — Bitmask of `z_whatami_t` to scout for

#### TLS Keys (when `Z_FEATURE_LINK_TLS` enabled)
- `Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_KEY` — Path to CA certificate bundle
- `Z_CONFIG_TLS_ROOT_CA_CERTIFICATE_BASE64_KEY` — Base64-encoded CA certificate
- `Z_CONFIG_TLS_LISTEN_PRIVATE_KEY_KEY` — Listener private key path
- `Z_CONFIG_TLS_LISTEN_CERTIFICATE_KEY` — Listener certificate path
- `Z_CONFIG_TLS_ENABLE_MTLS_KEY` — Enable mutual TLS (`"true"`/`"false"`)
- `Z_CONFIG_TLS_CONNECT_PRIVATE_KEY_KEY` — Client private key (mTLS)
- `Z_CONFIG_TLS_CONNECT_CERTIFICATE_KEY` — Client certificate (mTLS)
- `Z_CONFIG_TLS_VERIFY_NAME_ON_CONNECT_KEY` — Verify server hostname (`"true"`/`"false"`)

---

## 6. Core Concepts & API

### 6.1 Type System

zenoh-pico uses a structured ownership model enforced through naming conventions: