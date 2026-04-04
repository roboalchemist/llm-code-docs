# zenoh-pico on Zephyr RTOS

## Table of Contents

- [Overview](#overview)
- [Adding zenoh-pico as a Zephyr Module](#adding-zenoh-pico-as-a-zephyr-module)
- [Kconfig Options](#kconfig-options)
  - [Zephyr Networking Prerequisites](#zephyr-networking-prerequisites)
- [Minimum Heap and Stack Requirements](#minimum-heap-and-stack-requirements)
- [CMake Integration](#cmake-integration)
- [Publisher Example (Zephyr)](#publisher-example-zephyr)
- [Subscriber Example (Zephyr)](#subscriber-example-zephyr)
- [Important: Read and Lease Tasks](#important-read-and-lease-tasks)
- [Performance on MCUs](#performance-on-mcus)
- [Memory Footprint](#memory-footprint)
- [Supported Transports on Zephyr](#supported-transports-on-zephyr)
- [Connecting to a zenohd Router](#connecting-to-a-zenohd-router)
- [Peer Mode (Direct MCU-to-MCU)](#peer-mode-direct-mcu-to-mcu)
- [Tested Hardware Summary](#tested-hardware-summary)
- [Sources](#sources)

## Overview

zenoh-pico is a pure-C implementation of the Zenoh protocol targeting microcontrollers and constrained embedded devices. It is API-compatible with the full Rust zenoh stack and supports both client mode (connecting through a zenohd router) and peer mode (direct peer-to-peer).

Zephyr RTOS is a first-class supported target. The zenoh-pico repository ships a Zephyr module (`zephyr/module.yml` + `zephyr/CMakeLists.txt` + `zephyr/Kconfig.zenoh`) that integrates cleanly into the Zephyr build system via `west`.

**Tested boards include:**
- `nucleo-f767zi` (STM32F7, 10 Mb Ethernet)
- `reel_board` (nRF52840)
- ESP32 (via ESP-IDF, not Zephyr — see "ESP32" section)

---

## Adding zenoh-pico as a Zephyr Module

zenoh-pico is registered as a Zephyr module. Add it to your `west.yml`:

```yaml
manifest:
  projects:
    - name: zenoh-pico
      url: https://github.com/eclipse-zenoh/zenoh-pico
      revision: main          # or pin to a release tag
      path: modules/zenoh-pico
```

Then fetch:
```bash
west update
```

The module declares itself in `zephyr/module.yml`:
```yaml
name: zenoh-pico
build:
  cmake: zephyr/
  kconfig: zephyr/Kconfig.zenoh
```

This is all that is needed for `west build` to discover zenoh-pico automatically.

---

## Kconfig Options

Enable zenoh-pico and select features in your `prj.conf`:

```kconfig
# Core enable
CONFIG_ZENOH_PICO=y

# Features (enable only what you need to minimize flash)
CONFIG_ZENOH_PICO_PUBLICATION=y
CONFIG_ZENOH_PICO_SUBSCRIPTION=y
CONFIG_ZENOH_PICO_QUERY=y
CONFIG_ZENOH_PICO_QUERYABLE=y
CONFIG_ZENOH_PICO_SCOUTING=y

# Transport links
CONFIG_ZENOH_PICO_LINK_TCP=y
CONFIG_ZENOH_PICO_LINK_UDP_UNICAST=y
CONFIG_ZENOH_PICO_LINK_UDP_MULTICAST=y

# Threading (required for zp_start_read_task / zp_start_lease_task)
CONFIG_ZENOH_PICO_MULTI_THREAD=y

# Optional: serial transport
# CONFIG_ZENOH_PICO_LINK_SERIAL=y

# Optional: raw Ethernet transport
# CONFIG_ZENOH_PICO_RAWETH_TRANSPORT=y
```

Each `CONFIG_ZENOH_PICO_*` option maps directly to a `Z_FEATURE_*` compile definition in the C code. Disabling unused features is the primary lever for reducing flash footprint.

### Zephyr Networking Prerequisites

zenoh-pico over TCP/UDP requires Zephyr's BSD socket API. Add to `prj.conf`:

```kconfig
CONFIG_NETWORKING=y
CONFIG_NET_SOCKETS=y
CONFIG_NET_SOCKETS_POSIX_NAMES=y
CONFIG_NET_TCP=y
CONFIG_NET_UDP=y
CONFIG_NET_IPV4=y

# For multicast scouting / peer mode
CONFIG_NET_IPV4_IGMP=y

# DNS (needed if connecting by hostname)
CONFIG_DNS_RESOLVER=y
CONFIG_DNS_RESOLVER_MAX_SERVERS=1
```

For Ethernet (e.g., nucleo-f767zi):
```kconfig
CONFIG_NET_L2_ETHERNET=y
CONFIG_ETH_STM32_HAL=y        # board-specific driver
CONFIG_NET_DHCPV4=y           # or configure static IP
```

---

## Minimum Heap and Stack Requirements

zenoh-pico requires heap for session state, internal buffers, and message queues. A minimal Zephyr configuration:

```kconfig
CONFIG_HEAP_MEM_POOL_SIZE=16384    # 16 KB minimum; 32 KB recommended
CONFIG_MAIN_STACK_SIZE=4096        # 4 KB for the main thread
CONFIG_SYSTEM_WORKQUEUE_STACK_SIZE=2048
```

For multi-threaded operation with both read and lease tasks:
```kconfig
CONFIG_HEAP_MEM_POOL_SIZE=32768    # 32 KB
CONFIG_MAIN_STACK_SIZE=8192
```

The read task and lease task each consume stack. Adjust `CONFIG_ZENOH_PICO_STACK_SIZE` if the Kconfig exposes it, or use `z_task_attr_t` to configure per-task stack sizes in application code.

---

## CMake Integration

When building outside the Zephyr module system (e.g., as a standalone CMake project targeting Zephyr), pass `-DWITH_ZEPHYR=ON`:

```cmake
cmake_minimum_required(VERSION 3.20)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(my_app)

# zenoh-pico is pulled in via west modules; no explicit add_subdirectory needed.
# If building manually:
# add_subdirectory(path/to/zenoh-pico)
# target_link_libraries(app PRIVATE zenohpico::static)

target_sources(app PRIVATE src/main.c)
```

Build:
```bash
west build -b nucleo_f767zi -- -DBOARD=nucleo_f767zi
west flash
```

---

## Publisher Example (Zephyr)

The following is adapted from the official zenoh-pico Zephyr example (`examples/zephyr/z_pub.c`):

```c
#include <stdio.h>
#include <zenoh-pico.h>

/* Choose mode: 0 = client (connect to router), 1 = peer (direct) */
#define CLIENT_OR_PEER 0

#if CLIENT_OR_PEER == 0
#define MODE    "client"
#define LOCATOR ""        /* empty = use scouting to find router */
#elif CLIENT_OR_PEER == 1
#define MODE    "peer"
#define LOCATOR "udp/224.0.0.225:7447#iface=eth0"
#endif

#define KEYEXPR "demo/example/zenoh-pico-pub"
#define VALUE   "[Zephyr]{nucleo-F767ZI} Pub from zenoh-pico!"

#if Z_FEATURE_PUBLICATION == 1
int main(void) {
    /* Brief delay to allow network stack to initialize */
    k_sleep(K_SECONDS(5));

    z_owned_config_t config;
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, MODE);
    if (strlen(LOCATOR) > 0) {
        if (strcmp(MODE, "client") == 0)
            zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, LOCATOR);
        else
            zp_config_insert(z_loan_mut(config), Z_CONFIG_LISTEN_KEY, LOCATOR);
    }

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        return -1;
    }

    /* Start background read and lease-renewal tasks */
    zp_start_read_task(z_loan_mut(s), NULL);
    zp_start_lease_task(z_loan_mut(s), NULL);

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str_unchecked(&ke, KEYEXPR);
    z_owned_publisher_t pub;
    if (z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL) < 0) {
        printf("Unable to declare publisher!\n");
        return -1;
    }

    char buf[256];
    for (int idx = 0; ; ++idx) {
        k_sleep(K_SECONDS(1));
        snprintf(buf, sizeof(buf), "[%4d] %s", idx, VALUE);
        printf("Putting: %s\n", buf);

        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, buf);
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));
    return 0;
}
#else
int main(void) {
    printf("ERROR: compiled without Z_FEATURE_PUBLICATION\n");
    return -2;
}
#endif
```

---

## Subscriber Example (Zephyr)

```c
#include <stdio.h>
#include <zenoh-pico.h>

#define CLIENT_OR_PEER 0
#if CLIENT_OR_PEER == 0
#define MODE    "client"
#define LOCATOR ""
#elif CLIENT_OR_PEER == 1
#define MODE    "peer"
#define LOCATOR "udp/224.0.0.225:7447#iface=eth0"
#endif

#define KEYEXPR "demo/example/**"

#if Z_FEATURE_SUBSCRIPTION == 1
void data_handler(z_loaned_sample_t *sample, void *arg) {
    z_view_string_t key;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key);
    z_owned_string_t value;
    z_bytes_to_string(z_sample_payload(sample), &value);
    printf("[Subscriber] '%.*s': '%.*s'\n",
           (int)z_string_len(z_loan(key)),   z_string_data(z_loan(key)),
           (int)z_string_len(z_loan(value)), z_string_data(z_loan(value)));
    z_drop(z_move(value));
}

int main(void) {
    k_sleep(K_SECONDS(5));

    z_owned_config_t config;
    z_config_default(&config);
    zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, MODE);
    if (strlen(LOCATOR) > 0) {
        if (strcmp(MODE, "client") == 0)
            zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, LOCATOR);
        else
            zp_config_insert(z_loan_mut(config), Z_CONFIG_LISTEN_KEY, LOCATOR);
    }

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        return -1;
    }

    zp_start_read_task(z_loan_mut(s), NULL);
    zp_start_lease_task(z_loan_mut(s), NULL);

    z_owned_closure_sample_t cb;
    z_closure(&cb, data_handler, NULL, NULL);
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str_unchecked(&ke, KEYEXPR);
    z_owned_subscriber_t sub;
    if (z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(cb), NULL) < 0) {
        printf("Unable to declare subscriber!\n");
        return -1;
    }

    while (1) {
        k_sleep(K_SECONDS(1));
    }

    z_drop(z_move(sub));
    z_drop(z_move(s));
    return 0;
}
#else
int main(void) {
    printf("ERROR: compiled without Z_FEATURE_SUBSCRIPTION\n");
    return -2;
}
#endif
```

---

## Important: Read and Lease Tasks

On Zephyr (and all embedded targets), zenoh-pico does not automatically process incoming data. You must explicitly start two background tasks after `z_open()`:

```c
zp_start_read_task(z_loan_mut(s), NULL);    /* processes incoming messages */
zp_start_lease_task(z_loan_mut(s), NULL);   /* renews session lease / keepalive */
```

Forgetting either call results in sessions that appear to open successfully but either drop after the lease timeout (missing lease task) or never deliver received messages (missing read task).

---

## Performance on MCUs

Source: ZettaScale blog "Zenoh on Arduino / Zephyr" and Zenoh-Pico deep dive (2022).

| Board | Transport | Payload | Throughput |
|---|---|---|---|
| nucleo-f767zi (STM32F7) | 10 Mb Ethernet | 4096 bytes | ~9.2 Mbps (saturates 10 Mb link) |
| reel_board (nRF52840) | — | — | — |
| ESP32 (ESP-IDF, WiFi) | WiFi | 8 bytes | >5,200 msg/s |
| Workstation (Linux, zenoh-pico) | 100 GbE | 8 bytes | ~2.5M msg/s |
| Workstation (Linux, zenoh-pico) | 100 GbE | >8 KB | >25 Gbps |

For the NTU multi-protocol comparison: zenoh-pico achieved **5 µs latency** (one-way delay, backlogged), the lowest of all protocols tested — lower than CycloneDDS (12 µs) and full zenoh Rust P2P (10 µs). This is because zenoh-pico's peer mode does not implement mesh routing, eliminating the linkstate protocol overhead.

---

## Memory Footprint

Flash usage as a percentage of total flash on each board (full feature build):

| Board | Flash used | % of total flash |
|---|---|---|
| nucleo-f767zi | — | ~2.8% |
| reel_board | — | ~9.2% |
| ESP32 | — | ~0.9% |

A full zenoh-pico build fits in under **50 KB of flash**. By disabling unused features via Kconfig (e.g., disabling queryable, scouting, multicast), this can be reduced to approximately **15 KB** in tailored builds.

---

## Supported Transports on Zephyr

| Transport | Kconfig | Notes |
|---|---|---|
| TCP (unicast) | `CONFIG_ZENOH_PICO_LINK_TCP=y` | Standard client/peer connection |
| UDP unicast | `CONFIG_ZENOH_PICO_LINK_UDP_UNICAST=y` | Low-overhead point-to-point |
| UDP multicast | `CONFIG_ZENOH_PICO_LINK_UDP_MULTICAST=y` | Peer discovery, lowest latency |
| Serial | `CONFIG_ZENOH_PICO_LINK_SERIAL=y` | UART-based transport |
| Raw Ethernet | `CONFIG_ZENOH_PICO_RAWETH_TRANSPORT=y` | Layer-2 framing, no IP stack |
| WebSocket | `CONFIG_ZENOH_PICO_LINK_WS=y` | Browser/cloud bridging |

The Zephyr platform header (`include/zenoh-pico/system/platform/zephyr.h`) abstracts sockets using the union of file descriptors (TCP/UDP) and `struct device*` (serial), transparently selected at compile time via feature flags.

---

## Connecting to a zenohd Router

The most common Zephyr deployment: MCU in client mode, connecting to a zenohd router on a development machine or cloud VM.

1. Start the router on your host:
```bash
zenohd
```

2. In the MCU firmware, set mode to `client` and provide the router IP:
```c
zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "client");
zp_config_insert(z_loan_mut(config), Z_CONFIG_CONNECT_KEY, "tcp/192.168.1.100:7447");
```

3. Disable multicast scouting if not needed (saves overhead):
```c
zp_config_insert(z_loan_mut(config), Z_CONFIG_MULTICAST_SCOUTING_KEY, "false");
```

Alternatively, leave `LOCATOR` empty and let zenoh-pico scout for a router via UDP multicast on the same LAN segment — convenient for development, not recommended for production.

---

## Peer Mode (Direct MCU-to-MCU)

For two MCUs communicating directly without a router, both use peer mode with UDP multicast:

```c
zp_config_insert(z_loan_mut(config), Z_CONFIG_MODE_KEY, "peer");
zp_config_insert(z_loan_mut(config), Z_CONFIG_LISTEN_KEY, "udp/224.0.0.225:7447#iface=eth0");
```

Note: zenoh-pico's peer mode does not support mesh routing. It is point-to-point (or broadcast via multicast), not a multi-hop mesh. For multi-hop topologies, use a zenohd router.

---

## Tested Hardware Summary

| Board | MCU | Network | Zenoh-Pico support |
|---|---|---|---|
| `nucleo-f767zi` | STM32F767ZI (Cortex-M7, 216 MHz) | 10/100 Mb Ethernet | Verified (Zephyr) |
| `reel_board` | nRF52840 (Cortex-M4, 64 MHz) | BLE / USB | Verified (Zephyr) |
| ESP32 | Xtensa LX6, 240 MHz | WiFi 802.11n | Verified (ESP-IDF) |
| Raspberry Pi Pico | RP2040 (Cortex-M0+, 133 MHz) | via SPI/UART | Verified (FreeRTOS) |
| Generic STM32 (Tiva, STM32Cube) | Various Cortex-M | — | Community (single-thread) |
| Generic FreeRTOS + LwIP | Any | Ethernet | Verified |
| Generic FreeRTOS + FreeRTOS-Plus-TCP | Any | Ethernet | Verified |

---

## Sources

- zenoh-pico `zephyr/CMakeLists.txt` and `zephyr/module.yml` (source)
- zenoh-pico `examples/zephyr/z_pub.c`, `z_sub.c` (source)
- zenoh-pico `include/zenoh-pico/system/platform/zephyr.h` (source)
- ZettaScale Blog: "Zenoh on Arduino / Zephyr" (2021) — MCU benchmarks
- ZettaScale Blog: "Zenoh-Pico: Performance Deep Dive" (2022) — workstation benchmarks
- NTU: "A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS" (2023) — latency comparison
- zenoh-pico FAQ entries for flash footprint and peer mode

## See Also

- [Zenoh Pico Guide](zenoh-pico-guide.md) — complete zenoh-pico guide covering all platforms, feature flags, and the full C API
- [Pico vs Full Guide](pico-vs-full-guide.md) — when to use zenoh-pico vs zenoh-c and when a full OS build is warranted
