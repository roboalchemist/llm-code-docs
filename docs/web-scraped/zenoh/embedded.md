# zenoh-pico: Comprehensive Embedded Documentation

## Table of Contents

1. [What is zenoh-pico?](#1-what-is-zenoh-pico)
2. [Supported Platforms & Transport Matrix](#2-supported-platforms--transport-matrix)
3. [Installation & Build](#3-installation--build)
4. [Compile-Time Feature Flags](#4-compile-time-feature-flags)
5. [Runtime Configuration](#5-runtime-configuration)
6. [Core Concepts & API Patterns](#6-core-concepts--api-patterns)
7. [API Reference Overview](#7-api-reference-overview)
8. [API Differences from Full Zenoh](#8-api-differences-from-full-zenoh)
9. [Getting Started Examples](#9-getting-started-examples)
10. [Memory Optimization](#10-memory-optimization)
11. [Troubleshooting](#11-troubleshooting)

---

## 1. What is zenoh-pico?

zenoh-pico is the native C implementation of the [Eclipse Zenoh](https://zenoh.io) protocol, designed specifically for resource-constrained embedded systems and microcontrollers. It is fully wire-compatible with the main [Rust Zenoh implementation](https://github.com/eclipse-zenoh/zenoh), allowing microcontrollers to participate as first-class citizens in Zenoh networks alongside servers, gateways, and cloud nodes.

### Key Characteristics

| Property | Detail |
|---|---|
| **Language** | C (C99/C11) |
| **License** | EPL-2.0 OR Apache-2.0 |
| **Wire Compatibility** | 100% compatible with zenoh (Rust) |
| **OS Requirement** | None — runs on bare-metal, RTOS, or full OS |
| **Memory Model** | Configurable static/dynamic allocation |
| **Threading** | Optional — can run single-threaded with manual task spinning |

### What zenoh-pico Provides

- **Pub/Sub**: Publish data on key expressions; subscribe to data matching key expression patterns
- **Query/Queryable**: Issue queries to key expressions; respond to queries (request/reply)
- **Liveliness**: Track presence of nodes in the network
- **Scouting**: Discover peers and routers on the network automatically
- **Fragmentation**: Send/receive messages larger than a single packet
- **Multiple Transports**: TCP, UDP unicast, UDP multicast, Serial, Bluetooth, WebSocket, TLS
- **Client and Peer modes**: Connect to a router (client) or form a direct P2P mesh (peer)

### What zenoh-pico Does NOT Provide (vs. full Zenoh)

- No built-in storage/queryable backend
- No plugin system
- No admin REST API (optional Admin Space is available but limited)
- No Zenoh Flow (computation graphs)
- Reduced advanced pub/sub features (configurable at compile time)

---

## 2. Supported Platforms & Transport Matrix

### Full Platform/Transport Matrix

| **(RT)OS** | **UDP Unicast** | **UDP Multicast** | **TCP** | **Serial** | **Bluetooth** | **WebSocket** | **TLS** | **6LoWPAN** |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Linux/Unix** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| **Windows** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **macOS/BSD** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Zephyr RTOS** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ |
| **Arduino** | ✅ | ✅ | ✅ | ✅ | ✅ (Serial profile) | ❌ | ❌ | ❌ |
| **ESP-IDF** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **MbedOS** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **OpenCR** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Emscripten** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| **FreeRTOS-Plus-TCP** | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **FreeRTOS + LWIP** | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Raspberry Pi Pico** | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **STM32 ThreadX** | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Generic (bare-metal)** | custom | custom | custom | custom | custom | custom | ❌ | ❌ |

> **Note:** USB CDC Serial is experimentally supported on Raspberry Pi Pico when `Z_FEATURE_LINK_SERIAL_USB` and `Z_FEATURE_UNSTABLE_API` are enabled.

---

### Platform-Specific Notes

#### Zephyr RTOS
- **Tested boards**: `reel_board`, `nucleo-f767zi`, `nucleo-f420zi`, `nRF52840`
- **Network layers**: IPv4, IPv6, 6LoWPAN (Thread network)
- **Data link**: WiFi, Ethernet, Thread (OpenThread), Serial
- **Build system**: PlatformIO or native Zephyr west/CMake
- Requires `prj.conf` with networking and socket support enabled

#### Arduino
- **Tested boards**: `az-delivery-devkit-v4` (ESP32), `OpenCR 1.0`
- **Network layers**: IPv4, IPv6
- **Data link**: WiFi, Ethernet, Bluetooth (Serial profile), Serial (UART)
- **Build system**: PlatformIO (recommended) or Arduino IDE

#### ESP-IDF
- **Tested chips**: ESP32 (az-delivery-devkit-v4)
- **Network layers**: IPv4, IPv6
- **Data link**: WiFi, Ethernet, Serial
- **Build system**: PlatformIO or native ESP-IDF `idf.py`

#### FreeRTOS
Two variants are supported:
- **FreeRTOS-Plus-TCP**: UDP unicast + TCP, IPv4, Ethernet only
- **FreeRTOS + LWIP**: UDP unicast + multicast + TCP, IPv4, Ethernet

#### Raspberry Pi Pico
- **Tested boards**: `Raspberry Pi Pico W` (RP2040), `Raspberry Pi Pico 2 W` (RP2350)
- **Network**: WiFi (W variants only), Serial UART, USB CDC (experimental)
- **Board types**: `pico`, `pico_w`, `pico2`, `pico2_w`
- **Serial UART pin mappings**:

| TX/RX Pins | Device Name |
|---|---|
| 0 / 1 | `uart0_0` |
| 4 / 5 | `uart1_0` |
| 8 / 9 | `uart1_1` |
| 12 / 13 | `uart0_1` |
| 16 / 17 | `uart0_2` |

#### MbedOS
- **Tested boards**: `nucleo-f747zi`, `nucleo-f429zi`
- **Network layers**: IPv4, IPv6
- **Data link**: WiFi, Ethernet, Serial

#### Emscripten (WebAssembly)
- Only WebSocket transport is available
- Useful for running Zenoh in a browser or Node.js environment

#### STM32 ThreadX
- Serial transport only (UART with DMA)
- Requires STM32CubeIDE project setup
- See [Section 3.7](#stm32-threadx) for detailed setup

#### Generic / Bare-Metal
- Set `ZENOH_GENERIC=1` compile flag
- Provide custom `network.c` and `system.c` implementations
- See [`docs/generic_platform.md`](https://github.com/eclipse-zenoh/zenoh-pico/blob/main/docs/generic_platform.md)

---

## 3. Installation & Build

### 3.1 Linux/macOS (Unix)

Requirements: `cmake >= 3.14`, a C compiler (GCC or Clang)

```bash
git clone https://github.com/eclipse-zenoh/zenoh-pico.git
cd zenoh-pico

# Release build
make
sudo make install

# Debug build
BUILD_TYPE=Debug make
sudo make install

# With specific feature flags
cmake -Bbuild \
  -DCMAKE_BUILD_TYPE=Release \
  -DZ_FEATURE_PUBLICATION=1 \
  -DZ_FEATURE_SUBSCRIPTION=1 \
  -DZ_FEATURE_QUERY=0 \
  -DZ_FEATURE_QUERYABLE=0 \
  -DBATCH_UNICAST_SIZE=1024 \
  -DFRAG_MAX_SIZE=2048
cmake --build build
```

### 3.2 PlatformIO (Embedded Targets)

PlatformIO is the recommended build system for all embedded targets. Install it from [platformio.org](https://platformio.org).

#### Common `platformio.ini` Patterns

**Arduino/ESP32:**
```ini
[env:esp32]
platform = espressif32
board = az-delivery-devkit-v4
framework = arduino
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
monitor_speed = 115200
board_build.cmake_extra_args =
    -DZ_FEATURE_SUBSCRIPTION=1
    -DZ_FEATURE_PUBLICATION=1
    -DZ_FEATURE_QUERY=0
    -DZ_FEATURE_QUERYABLE=0
    -DBATCH_UNICAST_SIZE=1024
    -DFRAG_MAX_SIZE=2048
```

**Zephyr (reel_board):**
```ini
[env:reel_board]
platform = nordicnrf52
board = reel_board
framework = zephyr
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
```

**MbedOS (Nucleo F747ZI):**
```ini
[env:nucleo_f747zi]
platform = ststm32
board = nucleo_f747zi
framework = mbed
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
```

**OpenCR:**
```ini
[env:opencr]
platform = opencr
board = opencr
framework = arduino
lib_deps = https://github.com/eclipse-zenoh/zenoh-pico
```

#### Build and Flash Commands
```bash
platformio run               # Build
platformio run -t upload     # Build and flash
platformio device monitor    # Open serial monitor
```

### 3.3 Zephyr (Detailed Setup)

Project structure:
```
project_dir/
├── include/
├── lib/
│   └── zenoh-pico -> /path/to/zenoh-pico   # symlink or copy
├── src/
│   └── main.c
├── zephyr/
│   ├── prj.conf
│   └── CMakeLists.txt
└── platformio.ini
```

Minimal `prj.conf` for TCP/UDP networking:
```ini
# Networking
CONFIG_NETWORKING=y
CONFIG_NET_TCP=y
CONFIG_NET_UDP=y
CONFIG_NET_IPV4=y
CONFIG_NET_SOCKETS=y
CONFIG_NET_SOCKETS_POSIX_NAMES=y

# For WiFi
CONFIG_WIFI=y
CONFIG_NET_DHCPV4=y

# Stack sizes
CONFIG_MAIN_STACK_SIZE=8192
CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE=4096
```

### 3.4 Raspberry Pi Pico

Prerequisites:
```bash
sudo apt update
sudo apt install -y cmake gcc-arm-none-eabi libnewlib-arm-none-eabi \
    build-essential g++ libstdc++-arm-none-eabi-newlib

# Pico SDK
export PICO_SDK_PATH=$HOME/src/pico-sdk
git clone https://github.com/raspberrypi/pico-sdk.git $PICO_SDK_PATH
cd $PICO_SDK_PATH && git submodule update --init

# FreeRTOS (required for Pico examples)
export FREERTOS_KERNEL_PATH=$HOME/src/FreeRTOS-Kernel
git clone https://github.com/FreeRTOS/FreeRTOS-Kernel.git $FREERTOS_KERNEL_PATH
cd $FREERTOS_KERNEL_PATH && git submodule update --init
```

Build examples:
```bash
cd zenoh-pico/examples/rpi_pico
cmake -Bbuild \
    -DPICO_BOARD=pico_w \
    -DWIFI_SSID="MyNetwork" \
    -DWIFI_PASSWORD="MyPassword" \
    -DZENOH_CONFIG_MODE=client \
    -DZENOH_CONFIG_CONNECT="tcp/192.168.1.100:7447"
cmake --build ./build
```

Flash: Connect Pico in bootloader mode (hold BOOTSEL while plugging in USB), then copy the `.uf2` file to the mounted drive.

**Serial connection example:**
```bash
-DZENOH_CONFIG_CONNECT="serial/uart0_0#baudrate=115200"
# or using pin numbers:
-DZENOH_CONFIG_CONNECT="serial/0.1#baudrate=115200"
```

**USB CDC (experimental):**
```bash
# Build with USB serial support
-DZ_FEATURE_LINK_SERIAL_USB=1 -DZ_FEATURE_UNSTABLE_API=1

# Connect string on Pico side:
-DZENOH_CONFIG_CONNECT="serial/usb#baudrate=115200"

# On host side (zenoh router):
zenohd -l serial//dev/ttyACM0#baudrate=115200
```

### 3.5 ESP-IDF

```bash
cd zenoh-pico/examples/espidf
idf.py set-target esp32
idf.py menuconfig   # configure WiFi SSID/password under Zenoh Configuration
idf.py build
idf.py -p /dev/ttyUSB0 flash monitor
```

### 3.6 STM32 ThreadX

1. Create a new STM32CubeIDE project for your MCU
2. In CubeMX:
   - Enable **Azure RTOS (ThreadX)** middleware
   - Enable UART peripheral with **RX DMA in circular mode** and **UART global interrupt**
   - Set HAL tick source to a TIM peripheral (not SysTick, which ThreadX uses)
3. Clone zenoh-pico into your project folder
4. Add `zenoh-pico/src` to source folders (exclude all `platforms/*` except `common` and `threadx/stm32`)
5. Add `zenoh-pico/include` to include paths
6. Create `hal.h` in your project: `#include "stm32f4xx_hal.h"` (adjust for your MCU)
7. Add compiler defines:
   ```
   ZENOH_THREADX_STM32
   ZENOH_HUART=huart2
   ```
8. Exclude `Core/Src/app_threadx.c` and replace with a zenoh-pico example from `examples/threadx_stm32/`
9. Set static byte pool size to at least 25 KB
10. Run zenoh router on host:
    ```bash
    zenohd -l serial//dev/ttyACM0#baudrate=115200
    ```

### 3.7 Generic / Bare-Metal Platform

To port zenoh-pico to a new platform:

1. Set `ZENOH_GENERIC=1` in your compile flags
2. Create two implementation files:
   - `network.c` — socket/link layer (TCP, UDP, Serial, etc.)
   - `system.c` — time, sleep, mutex, threads (or stubs for single-thread)
3. Create `zenoh_generic_config.h` and `zenoh_generic_platform.h`

Example `platformio.ini` for a custom TI Tiva platform:
```ini
[env:tiva]
platform = titiva
board = lplm4f120h5qr
framework = libopencm3
lib_deps =
    https://github.com/eclipse/zenoh-pico
build_flags =
    -DZENOH_GENERIC=1
    -DZENOH_DEBUG=0
    -std=gnu++17
```

---

## 4. Compile-Time Feature Flags

All feature flags are set via CMake (or passed as `-D` flags to the build system). They generate constants in `include/zenoh-pico/config.h`.

### 4.1 Threading

#### `Z_FEATURE_MULTI_THREAD`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | Multi-threaded operation: background read task, lease task, mutex primitives |
| **When to disable** | Ultra-constrained MCUs with no RTOS, single-core bare-metal where you manually call `zp_read()` and `zp_send_keep_alive()` in your main loop |
| **Memory impact** | Disabling saves significant RAM (no thread stacks) and code size |
| **Dependencies** | Required by `Z_FEATURE_UNICAST_PEER`, `Z_FEATURE_ADVANCED_SUBSCRIPTION` |

> ⚠️ When disabled, you **must** manually call `zp_read()` and `zp_send_keep_alive()` periodically in your application loop.

---

### 4.2 Publication

#### `Z_FEATURE_PUBLICATION`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | `z_put()`, `z_delete()`, `z_declare_publisher()`, `z_publisher_put()`, `z_publisher_delete()` |
| **When to disable** | Subscriber-only nodes (e.g., actuator endpoints that only receive commands) |
| **Memory impact** | ~2–5 KB flash savings |

#### `Z_FEATURE_ADVANCED_PUBLICATION`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | `ze_declare_advanced_publisher()` — maintains a local cache of published samples for late-joining subscribers |
| **Dependencies** | Requires `Z_FEATURE_UNSTABLE_API=1`, `Z_FEATURE_PUBLICATION=1`, `Z_FEATURE_LIVELINESS=1` |
| **Memory impact** | Additional RAM for sample cache |

---

### 4.3 Subscription

#### `Z_FEATURE_SUBSCRIPTION`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | `z_declare_subscriber()`, `z_undeclare_subscriber()`, subscriber callbacks |
| **When to disable** | Publisher-only nodes (e.g., sensors that only send data) |
| **Memory impact** | ~2–5 KB flash savings |

#### `Z_FEATURE_LOCAL_SUBSCRIBER`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | Subscribers are triggered by publications from the **same session** (local loopback) |
| **When to enable** | Applications that need to react to their own publications |
| **Memory impact** | Minimal — adds a loopback routing path |

#### `Z_FEATURE_ADVANCED_SUBSCRIPTION`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | `ze_declare_advanced_subscriber()` — can receive historical samples and detect/recover missed samples |
| **Dependencies** | Requires `Z_FEATURE_UNSTABLE_API=1`, `Z_FEATURE_SUBSCRIPTION=1`, `Z_FEATURE_LIVELINESS=1`, `Z_FEATURE_MULTI_THREAD=1` |

---

### 4.4 Query / Queryable

#### `Z_FEATURE_QUERY`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | `z_get()` — send queries and receive replies |
| **When to disable** | Devices that never query (pure pub/sub only) |
| **Memory impact** | ~3–6 KB flash savings |

#### `Z_FEATURE_QUERYABLE`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | `z_declare_queryable()` — respond to incoming queries |
| **When to disable** | Devices that never answer queries |
| **Memory impact** | ~3–6 KB flash savings |

#### `Z_FEATURE_LOCAL_QUERYABLE`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | Queryables are triggered by local queries from the same session |
| **When to enable** | Same as `Z_FEATURE_LOCAL_SUBSCRIBER` but for queryables |

---

### 4.5 Liveliness

#### `Z_FEATURE_LIVELINESS`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | `z_liveliness_declare_token()`, `z_liveliness_declare_subscriber()`, `z_liveliness_get()` |
| **When to disable** | When presence tracking is not needed |
| **Memory impact** | ~2–4 KB flash savings |

---

### 4.6 Transport Link Types

#### `Z_FEATURE_LINK_TCP`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | TCP transport link (reliable, ordered, unicast) |
| **When to disable** | WiFi-less or serial-only devices |

#### `Z_FEATURE_LINK_UDP_UNICAST`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | UDP unicast transport (unreliable, low-latency) |
| **When to disable** | Devices where only TCP or serial is used |
| **Note** | Disabling this also disables `Z_FEATURE_SCOUTING` automatically |

#### `Z_FEATURE_LINK_UDP_MULTICAST`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | UDP multicast transport — required for peer mode without a router |
| **When to disable** | Devices in client mode only, or where multicast is not supported |

#### `Z_FEATURE_LINK_SERIAL`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | Serial (UART) transport — common for MCUs without WiFi/Ethernet |
| **When to enable** | Any MCU connected via UART to a host running a zenoh router |
| **Memory impact** | Small overhead for serial buffers |

#### `Z_FEATURE_LINK_SERIAL_USB`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | USB CDC serial transport (experimental) |
| **Dependencies** | Requires `Z_FEATURE_UNSTABLE_API=1` and `Z_FEATURE_LINK_SERIAL=1` |
| **Platform** | Currently Raspberry Pi Pico only |

#### `Z_FEATURE_LINK_BLUETOOTH`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | Bluetooth Serial Profile transport |
| **Platform** | Arduino only (tested on ESP32) |
| **When to enable** | Wireless embedded devices without WiFi that have Bluetooth |

#### `Z_FEATURE_LINK_WS`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | WebSocket transport |
| **Platform** | Linux/Unix, Emscripten (WebAssembly) |
| **When to enable** | Browser-based applications or environments where only HTTP/WS is available |

#### `Z_FEATURE_LINK_TLS`
| Property | Value |
|---|---|
| **Default** | `0` (OFF) |
| **What it enables** | TLS-encrypted TCP transport (via Mbed TLS 2.x or 3.x) |
| **Dependencies** | Requires Mbed TLS installed on the system |
| **Memory impact** | Significant — TLS handshake requires several KB of stack and heap |
| **When to enable** | Production deployments where data security is required |

---

### 4.7 Scouting

#### `Z_FEATURE_SCOUTING`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | `z_scout()` — automatically discover zenoh routers/peers on the network via UDP multicast |
| **When to disable** | When the router address is always known (hardcoded connect string), saving code size |
| **Dependencies** | Automatically disabled if `Z_FEATURE_LINK_UDP_UNICAST=0` |

---

### 4.8 Fragmentation

#### `Z_FEATURE_FRAGMENTATION`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | Send and receive messages larger than a single transport batch (`Z_FRAG_MAX_SIZE`) |
| **When to disable** | When you can guarantee all messages fit in one packet — saves a defragmentation buffer |
| **Memory impact** | Disabling saves `Z_FRAG_MAX_SIZE` bytes of RAM (default 4096 bytes) |

---

### 4.9 Batching

#### `Z_FEATURE_BATCHING`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | Batch multiple small messages into a single transport packet for improved throughput |
| **When to disable** | When latency matters more than throughput, or on very constrained devices |

---

### 4.10 Automatic Reconnection

#### `Z_FEATURE_AUTO_RECONNECT`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | Automatically attempt to reconnect to a router/peer if the connection is lost |
| **When to disable** | Applications that prefer to manage connection state explicitly |

---

### 4.11 Matching

#### `Z_FEATURE_MATCHING`
| Property | Value |
|---|---|
| **Default** | `1` (ON) |
| **What it enables** | `z_publisher_get_matching_status()`, `z_publisher_declare_matching_listener()` — notify publishers when subscribers appear/disappear |
| **Dependencies** | Requires `Z_FEATURE_INTEREST=1` |

---

### 4.12 Miscellaneous Feature Flags

| Flag | Default | Description |
|---|---|---|
| `Z_FEATURE_UNSTABLE_API` | `0` | Enables experimental/unstable APIs (required by some advanced features) |
| `Z_FEATURE_INTEREST` | `1` | Interest protocol for write filtering and matching |
| `Z_FEATURE_ENCODING_VALUES` | `1` | Predefined encoding constants (e.g., `z_encoding_application_json()`) |
| `Z_FEATURE_MULTICAST_TRANSPORT` | `1` | Multicast transport layer |
| `Z_FEATURE_UNICAST_TRANSPORT` | `1` | Unicast transport layer |
| `Z_FEATURE_RAWETH_TRANSPORT` | `0` | Raw Ethernet frame transport |
| `Z_FEATURE_UNICAST_PEER` | `1` | Peer-to-peer unicast mode (requires `Z_FEATURE_MULTI_THREAD`) |
| `Z_FEATURE_TCP_NODELAY` | `1` | Disable Nagle's algorithm on TCP sockets (reduces latency) |
| `Z_FEATURE_SESSION_CHECK` | `1` | Validate session is still open before operations |
| `Z_FEATURE_RX_CACHE` | `0` | LRU cache on RX side (improves throughput, costs heap) |
| `Z_FEATURE_MULTICAST_DECLARATIONS` | `0` | Declare key expressions over multicast |
| `Z_FEATURE_PERIODIC_TASKS` | `0` | Periodic task scheduler (required by advanced pub/sub) |
| `Z_FEATURE_LOCAL_SUBSCRIBER` | `0` | Trigger subscribers on local publications |
| `Z_FEATURE_LOCAL_QUERYABLE` | `0` | Trigger queryables on local queries |
| `Z_FEATURE_ADMIN_SPACE` | `0` | Runtime diagnostics queryable (requires `Z_FEATURE_UNSTABLE_API`) |
| `Z_FEATURE_BATCH_TX_MUTEX` | `0` | Coarse-grained TX mutex (higher throughput, risk of keep-alive loss) |
| `Z_FEATURE_BATCH_PEER_MUTEX` | `0` | Coarse-grained peer mutex |

### 4.13 Feature Flag Quick Reference Table

| Use Case | Recommended Flags |
|---|---|
| **Minimal publisher (sensor)** | `PUBLICATION=1`, `SUBSCRIPTION=0`, `QUERY=0`, `QUERYABLE=0`, `LIVELINESS=0`, `SCOUTING=0`, `FRAGMENTATION=0` |
| **Minimal subscriber (actuator)** | `PUBLICATION=0`, `SUBSCRIPTION=1`, `QUERY=0`, `QUERYABLE=0`, `LIVELINESS=0`, `SCOUTING=0` |
| **Serial-only device** | `LINK_TCP=0`, `LINK_UDP_UNICAST=0`, `LINK_UDP_MULTICAST=0`, `LINK_SERIAL=1`, `SCOUTING=0`, `MULTI_THREAD=0` |
| **Single-thread bare-metal** | `MULTI_THREAD=0`, `UNICAST_PEER=0`, `BATCHING=0` |
| **Full-featured embedded** | All defaults |
| **Secure production** | `LINK_TLS=1`, `AUTO_RECONNECT=1` |

---

## 5. Runtime Configuration

Runtime configuration is managed through a `z_owned_config_t` object passed to `z_open()`. Use `zp_config_insert()` to set values by key.

```c
z_owned_config_t config;
z_config_default(&config);
zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.100:7447");
```

### 5.1 Mode

| Key | Values | Default |
|---|---|---|
| `Z_CONFIG_MODE_KEY` | `"client"`, `"peer"` | `"client"