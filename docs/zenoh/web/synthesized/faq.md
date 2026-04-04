# Zenoh FAQ

Synthesized from GitHub issues, blog posts, ROS Discourse discussions, and official documentation.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Deployment Modes](#deployment-modes)
- [Configuration](#configuration)
- [Key Expressions](#key-expressions)
- [Performance](#performance)
- [ROS 2 / Robotics](#ros-2-robotics)
- [Embedded / zenoh-pico](#embedded-zenoh-pico)
- [Security](#security)
- [Troubleshooting](#troubleshooting)

## Getting Started

**Q: What is Zenoh?**
A: Zenoh is a pub/sub/query protocol by Eclipse/ZettaScale designed for edge computing, IoT, and robotics. It unifies data in motion, data at rest, and computations in a single protocol. It operates on key/value spaces and supports three primitives: publish/subscribe, storage (put/get), and queryables (on-demand computation).

**Q: What languages does Zenoh support?**
A: Rust (primary/canonical implementation), Python, C, C++, Java, and Kotlin. TypeScript/JavaScript (`zenoh-ts`) is a WebSocket client that connects via the `zenoh-plugin-remote-api` plugin (not a direct Rust binding and not via the REST plugin). Zenoh-pico is a separate pure-C implementation targeting embedded/constrained devices and does not wrap the Rust core.

**Q: How do I install Zenoh?**
A: The Zenoh router (`zenohd`) is available as pre-built binaries:
- **macOS**: `brew install zenoh`
- **Linux (Debian/Ubuntu)**: `sudo apt install zenoh`
- **Windows/Other**: Download from GitHub releases, unzip, run `zenohd` (or `zenohd.exe`)
- **Rust library**: `cargo add zenoh`
- **Python**: `pip install eclipse-zenoh`

**Q: How do I start the Zenoh router?**
A: Simply run `zenohd`. It starts with default configuration listening on `tcp/[::]:7447`. You can supply a config file: `zenohd -c my-config.json5`.

**Q: What is the default port Zenoh listens on?**
A: The router listens on TCP port **7447** (`tcp/[::]:7447`) by default. Peers listen on port `0` (ephemeral, OS-assigned). Multicast scouting uses UDP port **7446** on group `224.0.0.224`.

**Q: Where can I find code examples?**
A: Examples are included in each language repo under an `examples/` directory, and are also available in the main `zenoh` Rust repository as runnable binaries in `target/release/examples/`.

---

## Deployment Modes

**Q: What are the three deployment modes in Zenoh?**
A:
- **peer**: Applications communicate directly with each other. Uses multicast and gossip scouting to discover peers automatically. Default mode for most applications.
- **client**: Applications connect to a Zenoh router and rely on it for routing. Uses multicast scouting to find routers, or can be given explicit endpoints.
- **router** (`zenohd`): Routes data between clients and local peer subnetworks. Routers can be interconnected in arbitrary topologies.

**Q: When should I use peer mode vs. client mode?**
A: Use **peer mode** when applications are on the same local network and can communicate directly (LAN, same subnet). Use **client mode** when applications need to communicate across networks, through firewalls, or over the internet — in these cases configure a `zenohd` router as the intermediary and point clients at it with `connect.endpoints`.

**Q: How do Zenoh peers discover each other automatically?**
A: Peers in `peer` mode use two scouting mechanisms:
1. **Multicast scouting**: Joins multicast group `224.0.0.224:7446` and sends scout messages. All reachable peers and routers on the same LAN segment are discovered and connected automatically.
2. **Gossip scouting**: Peers forward their known-peer list to newly connected peers. Useful when multicast is unavailable. Requires configuring an initial entry point (a router or another peer) via `connect.endpoints`.

**Q: How do I connect applications across the internet or through a firewall?**
A: Deploy a `zenohd` router on a reachable host (e.g., a cloud VM with a public IP). Configure your applications as clients pointing to that router:
```json5
{ mode: "client", connect: { endpoints: ["tcp/123.4.5.6:7447"] } }
```
Multiple routers can be interconnected for redundancy or geographic distribution.

**Q: What is a mesh network deployment in Zenoh?**
A: Peers can run a linkstate protocol to communicate in mesh topologies where direct connections are impossible. Enable it with:
```json5
{ mode: "peer", routing: { peer: { mode: "linkstate" } } }
```
Note: If a Zenoh router is used to bridge the mesh to a wider network, that router also needs the same `routing` section.

---

## Configuration

**Q: What format does Zenoh's configuration file use?**
A: JSON5 (`.json5`) or YAML. JSON5 allows comments and trailing commas, making it more readable than plain JSON. The default configuration (`DEFAULT_CONFIG.json5`) is included in the zenoh repository.

**Q: How do I configure a storage?**
A: Add a `storage_manager` plugin section to your config:
```json5
{
  plugins: {
    storage_manager: {
      storages: {
        mystorage: {
          key_expr: "myhome/**",
          volume: "memory"
        }
      }
    }
  }
}
```
Other volumes: `rocksdb`, `influxdb`, `s3`, `filesystem` (require respective backend plugins).

**Q: How do I enable the REST/HTTP API?**
A: Add the `rest` plugin to config, or start `zenohd` with `--rest-http-port 8080`. The REST plugin's config.json5 defaults to port **8080**. Access it at `http://localhost:8080/<key-expression>`.

**Q: How do I pass configuration changes on the command line without a file?**
A: Use `--cfg` flags with `KEY:VALUE` pairs:
```bash
zenohd --cfg='plugins/storage_manager/storages/demo:{key_expr:"demo/**",volume:"memory"}'
```

**Q: How do I configure priority and reliability per link?**
A: Append to the endpoint string:
```
tcp/localhost?prio=6-7;rel=0
```
This assigns "data_low" and "background" priorities with unreliable transport to that link.

---

## Key Expressions

**Q: What is a key expression?**
A: A key expression is a pattern language for matching sets of keys in Zenoh's key/value space. Keys use `/` as the hierarchy separator (like a filesystem path). Key expressions add wildcards: `*` matches one path segment, `**` matches any number of segments including zero.

**Q: What is the difference between `*` and `**`?**
A:
- `a/*/c` matches `a/b/c` but NOT `a/b/b/c` (single segment only)
- `a/**/c` matches `a/c`, `a/b/c`, `a/b/b/c` (any depth)
- `$*` within a segment matches a partial segment: `a/foo$*/c` matches `a/foobar/c`

**Q: Are there restrictions on key names?**
A: Yes. Keys cannot contain `*`, `$`, `?`, `#`, or `//` (double slash). The `/` character is reserved as the hierarchy separator. Using `/` as separator (instead of `.` or other chars) unlocks Zenoh optimizations — one user reported switching from `.` to `/` halved their CPU usage.

**Q: What is a canonical (canon) key expression?**
A: Zenoh requires key expressions to be in a canonical form to ensure that equivalent patterns have one unique string representation. Forbidden non-canon patterns include `**/**` (use `**`), `**/*` (use `*/**`), and adjacent `$*$*` (use `$*`).

---

## Performance

**Q: How does Zenoh compare to DDS in throughput?**
A: In the NTU 2023 benchmark on 100 Gb Ethernet:
- Zenoh (peer-to-peer): ~50 Gbps at 16 KB payload
- CycloneDDS (RELIABLE): ~14 Gbps at 16 KB payload
- Zenoh delivers over 3x higher throughput than DDS in this configuration.

**Q: How does Zenoh compare to MQTT and Kafka in throughput?**
A: At 16 KB payload over 100 GbE, both MQTT (Mosquitto) and Kafka achieve ~5 Gbps vs. Zenoh's ~50 Gbps — approximately 10x lower than Zenoh.

**Q: What is Zenoh's latency?**
A:
- Zenoh peer-to-peer (backlogged, 64-byte payload): **35 µs**
- Zenoh via router (one extra hop): **70 µs**
- Zenoh-Pico (unicast): **45 µs**; (multicast peer mode): **15 µs**
- NTU comparison: Zenoh P2P over network: ~10 µs; Zenoh-Pico: ~5 µs (lowest of all protocols tested)

**Q: How can I improve latency for a specific topic in the ROS2 bridge?**
A: Use the `express` option in `pub_priorities`. Setting `:express` on a key expression causes Zenoh to send messages immediately without batching, which reduces latency for that topic at the cost of slightly lower overall throughput.

**Q: Does using a `/` separator vs. `.` matter for performance?**
A: Yes. Users have reported that switching from `.` to `/` as the key hierarchy separator almost halved their CPU usage, because Zenoh can apply optimizations when using the canonical `/` separator.

---

## ROS 2 / Robotics

**Q: What is the difference between `zenoh-bridge-dds` and `zenoh-bridge-ros2dds`?**
A: `zenoh-bridge-ros2dds` is the recommended bridge for ROS 2 users. It has better integration with the ROS graph (topics, services, actions), supports ROS namespace configuration on the bridge, and exposes services/actions as Zenoh Queryables. `zenoh-bridge-dds` is a generic DDS bridge and will eventually be deprecated for ROS 2 use.

**Q: How do I bridge two ROS 2 systems over the internet?**
A: Run `zenoh-bridge-ros2dds` as a client on each robot, pointing both at a `zenohd` router in the cloud:
```bash
zenoh-bridge-ros2dds -m client -e tcp/<router-ip>:7447
```
The two bridges will route ROS topics/services/actions through the zenoh router.

**Q: Can Zenoh replace the RMW (ROS 2 middleware) layer entirely?**
A: Not yet via an official RMW. The community and ZettaScale are working toward a Zenoh RMW (`rmw_zenoh`), but as of recent versions, the bridge approach (`zenoh-bridge-ros2dds`) is the primary integration path. A native RMW would eliminate the DDS layer entirely.

**Q: What ROS 2 distributions are supported by `zenoh-bridge-ros2dds`?**
A: Humble, Iron, and Rolling are commonly tested. ROS 2 Foxy has been tested but is older. Always match the bridge version to your ROS 2 distribution and Zenoh version.

**Q: I'm seeing `malformed packet` errors in CycloneDDS when using `zenoh-bridge-ros2dds`. What causes this?**
A: A known issue in versions around 1.0.0-alpha affected CDR header handling — the 4-byte CDR header was truncated when converting `DDSRawSample` to `ZBytes`. This was fixed in subsequent releases. Upgrade to a stable 1.0+ release.

**Q: The `zenoh-bridge-ros2dds` config fails with "unknown field `id`". Why?**
A: The `id` field inside the `ros2dds` plugin config section was removed in version 1.0.0-alpha.5. Remove the `id` field from the `plugins.ros2dds` section of your config; assign the bridge identity via the top-level Zenoh config or command-line flags instead.

**Q: The DDS bridge only forwards topics at ~50 Hz instead of the expected 1000 Hz. Why?**
A: This is a known performance disparity between `zenoh-bridge-dds` and `zenoh-bridge-ros2dds`. `zenoh-bridge-ros2dds` handles ROS2 type system metadata more efficiently. Also check that QoS settings on both sides are compatible and that the bridge is not filtering messages due to type hash parse warnings.

---

## Embedded / zenoh-pico

**Q: What is zenoh-pico?**
A: zenoh-pico is a pure-C implementation of the Zenoh protocol targeting microcontrollers and constrained embedded devices. It is fully compatible with the Rust zenoh stack. It supports client mode (connecting to a zenoh router) and peer mode (direct peer-to-peer).

**Q: What is the minimum flash footprint of zenoh-pico?**
A: Under 50 KB for a full build, reducible to approximately 15 KB in tailored compilation setups (stripping unused features).

**Q: What boards/platforms does zenoh-pico support?**
A: Tested platforms include Zephyr (nucleo-f767zi, reel_board), Arduino (ESP32), and standard POSIX systems. Community contributions have expanded support further.

**Q: What is zenoh-pico's throughput on a microcontroller?**
A: On ESP32 (WiFi): over 5.2k msg/s with 8-byte payload. On nucleo-f767zi (10 Mb Ethernet): ~9.2 Mbps, which saturates a 10 Mb/s link. Full Linux workstations running zenoh-pico achieve ~2.5M msg/s (8 bytes) and >25 Gbps (large payloads).

**Q: Does zenoh-pico support peer mode on MCUs?**
A: Peer mode support is available. Note that zenoh-pico's peer mode does not support mesh routing (unlike the full Rust stack), which is also why its latency is lower (~5 µs) — there is no linkstate overhead.

**Q: What protocols can zenoh-pico use as transports?**
A: TCP, UDP (unicast and multicast), serial, and Bluetooth (community contributions). TLS is available on platforms that support it.

---

## Security

**Q: How do I enable TLS in Zenoh?**
A: Configure the `tls` transport section with certificate paths. Zenoh uses rustls (not OpenSSL). Required fields depend on whether you are configuring the listen or connect side:
- `root_ca_certificate_file` / `root_ca_certificate_raw` / `root_ca_certificate_base64`
- `listen_private_key_file` / `listen_certificate_file` (for the server side)
- `connect_private_key_file` / `connect_certificate_file` (for the client side)

**Q: Does Zenoh support mutual TLS (mTLS)?**
A: Yes. Set `enable_mtls: true` in the TLS configuration section. Both sides must provide certificates.

**Q: Does Zenoh use OpenSSL?**
A: No. Zenoh uses **rustls** for TLS, which is a pure-Rust TLS implementation. This avoids introducing C/C++ security dependencies into the core.

**Q: Is there access control in Zenoh?**
A: Yes. Zenoh supports access control rules (see `rfcs/rfcs-all-access-control-rules.md` in this doc set). You can configure read/write permissions on the admin space via `--adminspace-permissions [r|w|rw|none]`.

---

## Troubleshooting

**Q: My application fails to connect with "Unable to connect to any of [tcp/...]".**
A: Check that `zenohd` is running and reachable. Verify firewall rules allow TCP port 7447. If using `client` mode, confirm the `connect.endpoints` list in your config points to the correct IP/port. If `timeout: 0` is set, it will not retry — set to `-1` for infinite retry.

**Q: I get a build error: "cannot transmute between types of different sizes" in zenoh-c.**
A: This is a version mismatch. The zenoh-c bindings pin to a specific zenoh Rust crate. If you check out an older tag of zenoh-c, the Cargo.toml may reference `master` branch of zenoh rather than the corresponding version. Always build zenoh-c from the same release tag as the zenoh library version you are targeting.

**Q: zenoh-c fails to build with `shared_memory` feature: "Failed to generate opaque types".**
A: This is typically a toolchain or dependency incompatibility. Ensure you are using the exact Rust toolchain version specified in the zenoh-c repository's `rust-toolchain.toml`. The SHM feature has stricter build requirements.

**Q: TLS handshake fails or times out.**
A: Default handshake timeout is 10,000 ms (`tls_handshake_timeout_ms`). Check certificate validity and that server name verification (`verify_name_on_connect`) matches your certificate's CN/SAN. For development, you can set `verify_name_on_connect: false` but do not do this in production.

**Q: My zenoh application is running but not discovering peers.**
A: Common causes:
1. Multicast is blocked on the network (common in cloud/VMs) — use explicit `connect.endpoints` instead.
2. Both applications are in `client` mode — clients do not discover each other, they only connect to routers. At least one side must be `peer` or a `router` must be involved.
3. TTL on multicast packets is 1 by default — peers must be on the same LAN segment.

**Q: I have high latency at low message rates. Is this a bug?**
A: No, this is expected behavior. At low message rates, processes are frequently descheduled by the OS scheduler, adding wake-up latency. Latency is lowest in the backlogged/high-rate scenario where processes stay scheduled. To minimize latency at low rates, consider OS-level tuning (CPU affinity, real-time scheduling) or use the `express` publication option.

**Q: The `z_undeclare_keyexpr` function in zenoh-c is not actually deleting the keyexpr. Why?**
A: An older bug caused `z_undeclare_keyexpr` to clone the keyexpr and drop the clone instead of the original. This was fixed in later releases. Ensure you are using a recent stable release of zenoh-c.

**Q: I get linker errors about SONAME when linking zenoh-c on Linux.**
A: This is a known issue in Cargo where `.so` files do not include a SONAME field. A workaround is to set the SONAME explicitly with `patchelf` or `chrpath` after building, or to use the packaged releases which have this applied. The upstream Cargo issue is tracked at https://github.com/rust-lang/cargo/issues/5045.

## See Also

- [Troubleshooting Guide](troubleshooting-guide.md) — deeper diagnostics for connection, build, and performance issues
- [Node Types Guide](node-types-guide.md) — clarifies the peer/client/router modes frequently asked about here
- [Scouting Guide](scouting-guide.md) — explains the discovery mechanisms mentioned in deployment mode questions
- [Config Connect Listen](config-connect-listen.md) — endpoint and timeout configuration for the connection questions
