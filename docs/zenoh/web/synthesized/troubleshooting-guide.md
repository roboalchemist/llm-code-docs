# Zenoh Troubleshooting Guide

Synthesized from GitHub issues, FAQ, community forums, and tribal knowledge.

---

## Table of Contents

- [Connection Issues](#connection-issues)
- [ROS 2 Bridge Issues](#ros-2-bridge-issues)
- [Version and Compatibility Issues](#version-and-compatibility-issues)
- [TLS / Security Issues](#tls-security-issues)
- [Linker / Build Issues](#linker-build-issues)
- [Embedded / zenoh-pico Issues](#embedded-zenoh-pico-issues)
- [Key Expression Issues](#key-expression-issues)
- [Performance Issues](#performance-issues)
- [Python-Specific Issues](#python-specific-issues)
- [Admin Space / REST Debugging](#admin-space-rest-debugging)
- [Debugging Tools](#debugging-tools)
  - [Enable verbose logging](#enable-verbose-logging)
  - [Log level meanings](#log-level-meanings)
  - [REST admin space queries](#rest-admin-space-queries)
  - [Scout for active Zenoh nodes](#scout-for-active-zenoh-nodes)
  - [Check what's stored in memory storage](#check-whats-stored-in-memory-storage)
- [Quick Diagnostic Checklist](#quick-diagnostic-checklist)

## Connection Issues

**Problem**: `Unable to connect to any of [tcp/...]`
**Cause**: Router is not running, firewall blocks port 7447, or `connect.endpoints` is misconfigured.
**Fix**: Verify `zenohd` is running and reachable. Open TCP port 7447 in your firewall. In `client` mode, confirm `connect.endpoints` points to the correct IP/port. If `connect.timeout_ms: 0` is set, the session will not retry — use `-1` for infinite retry.

---

**Problem**: Two peers cannot find each other even though both are running.
**Cause**: Both nodes are in `client` mode. Clients only connect to routers; they never discover each other directly.
**Fix**: Set at least one node to `peer` mode, or deploy a `zenohd` router and point both clients at it. Only `peer` and `router` nodes participate in discovery.

---

**Problem**: Peers don't discover each other on a cloud VM or inside Docker (bridge network).
**Cause**: UDP multicast [scouting](scouting-guide.md) (group `224.0.0.224:7446`) is blocked on cloud hypervisors and Docker bridge networks.
**Fix**: Use explicit `connect.endpoints` in the config:
```json5
{ mode: "client", connect: { endpoints: ["tcp/<router-ip>:7447"] } }
```
Or use `--net host` on Linux Docker for host networking. Note: `--net host` is not supported on Docker Desktop for macOS/Windows.

---

**Problem**: Multicast scouting works on the same machine but not across subnets.
**Cause**: Multicast TTL defaults to 1; packets do not cross routers. Peers must be on the same LAN segment.
**Fix**: Deploy a `zenohd` router that both sides connect to, or increase the multicast TTL via `scouting.multicast.ttl` in the config.

---

**Problem**: `Received a close message (reason INVALID) in response to an InitSyn`
**Cause**: Version mismatch between two Zenoh endpoints. The 0.x and 1.x protocol wire formats are incompatible.
**Fix**: Ensure all Zenoh instances (router, libraries, bridges) are on the same major version. The error message will contain the transport version on both sides.

---

**Problem**: Application connects but messages are never received.
**Cause**: Key expression mismatch, or publisher and subscriber in different Zenoh subnetworks with no router bridging them.
**Fix**: Verify the key expressions are compatible (try an exact key first). Check that a `zenohd` router bridges the two networks if they are on different segments. Use the REST admin space to inspect declared publishers and subscribers: `curl http://localhost:8080/@/**`.

---

## ROS 2 Bridge Issues

**Problem**: ROS 2 topics are not bridged when running `zenoh-bridge-ros2dds` in a Docker container.
**Cause**: DDS uses UDP multicast for discovery, which does not traverse Docker bridge networks.
**Fix**: Run the bridge with host networking:
```bash
docker run --init --net host eclipse/zenoh-bridge-ros2dds:latest
```
Note: `--net host` is Linux-only and not supported on Docker Desktop.

---

**Problem**: `malformed packet` errors in CycloneDDS when using `zenoh-bridge-ros2dds`.
**Cause**: A bug in versions around 1.0.0-alpha truncated the 4-byte CDR header when converting `DDSRawSample` to `ZBytes`.
**Fix**: Upgrade to a stable 1.0+ release of `zenoh-bridge-ros2dds`.

---

**Problem**: `zenoh-bridge-ros2dds` config fails with `"unknown field 'id'"`.
**Cause**: The `id` field inside `plugins.ros2dds` config was removed in version 1.0.0-alpha.5.
**Fix**: Remove the `id` field from the `plugins.ros2dds` section of your config file. Set bridge identity via top-level Zenoh config flags instead.

---

**Problem**: DDS bridge only forwards topics at ~50 Hz instead of the expected rate.
**Cause**: Performance disparity between `zenoh-bridge-dds` (generic) and `zenoh-bridge-ros2dds` (ROS-aware). Also can be caused by QoS mismatches or type hash parse warnings causing message filtering.
**Fix**: Use `zenoh-bridge-ros2dds` for ROS 2 workloads. Check bridge logs for type hash warnings. Ensure QoS settings match on both sides.

---

**Problem**: Bridging two identical robots produces topic collisions.
**Cause**: Both ROS 2 systems publish/subscribe on the same topic names with no namespace separation.
**Fix**: Configure the bridge with per-robot namespaces using the `namespace` option in the bridge config or the `-n` flag. Each robot's bridge should use a unique namespace prefix.

---

## Version and Compatibility Issues

**Problem**: Build error `"cannot transmute between types of different sizes"` in zenoh-c.
**Cause**: Version mismatch. The zenoh-c bindings pin to a specific zenoh Rust crate version. An old tag's `Cargo.toml` may reference `master` instead of the matching release.
**Fix**: Always build zenoh-c from the same release tag as your zenoh library version. Do not mix release tags across zenoh and zenoh-c.

---

**Problem**: `zenoh-c` fails to build with `shared_memory` feature: `"Failed to generate opaque types"`.
**Cause**: Rust toolchain or dependency incompatibility. The SHM feature has stricter build requirements.
**Fix**: Use the exact Rust toolchain version specified in the zenoh-c repo's `rust-toolchain.toml`. Do not override this with a different toolchain version.

---

**Problem**: `zenoh-c` build fails with `panic="abort"`: `"Size mismatch: type z_loaned_mutex_t has size 16 while type z_owned_mutex_t has size 24"`.
**Cause**: When `panic="abort"`, Rust's std omits the `poison` flag in `Mutex`, changing struct sizes. This breaks the zenoh-c type size assumptions.
**Fix**: Switch to `decl_c_type_inequal!` (done in zenoh-c PR #1038) or upgrade to a release that includes this fix.

---

**Problem**: CMake `FetchContent` for zenoh-c fails with `"ninja: error: 'zenohc_shared-NOTFOUND'"` or CMP0111 warnings.
**Cause**: `IMPORTED_LOCATION` is not set for the imported CMake target. Fixed in zenoh-c PR #1041.
**Fix**: Upgrade to a version that includes this CMake fix. As a workaround, manually set `IMPORTED_LOCATION` in your CMakeLists after `FetchContent_MakeAvailable`.

---

## TLS / Security Issues

**Problem**: [TLS](encryption-guide.md) handshake fails or times out.
**Cause**: Certificate CN/SAN does not match `verify_name_on_connect`, or the certificate has expired.
**Fix**: Check certificate validity with `openssl x509 -in cert.pem -noout -dates`. `verify_name_on_connect` is a **boolean flag** (not a hostname string) — Zenoh matches the certificate SAN/CN against the hostname in the endpoint URI (e.g., `tls/my-hostname.com:7447`). Default handshake timeout is 10,000 ms (`tls_handshake_timeout_ms`). For development only: set `verify_name_on_connect: false`.

---

**Problem**: TLS configuration does not work with OpenSSL-style `.pem` chains.
**Cause**: Zenoh uses **rustls** (pure-Rust TLS), not OpenSSL. OpenSSL-specific options and PKCS#11 hardware tokens are not supported.
**Fix**: Provide certificates as PEM files compatible with rustls. Intermediate certificates must be concatenated into the chain file.

---

## Linker / Build Issues

**Problem**: Linker errors about SONAME when linking zenoh-c on Linux.
**Cause**: A known Cargo limitation — `.so` files built by Cargo do not embed a SONAME field.
**Fix**: Use pre-built packaged releases (SONAME is patched in). Or after building, set SONAME manually:
```bash
patchelf --set-soname libzenohc.so.1 target/release/libzenohc.so
```
Tracked upstream at https://github.com/rust-lang/cargo/issues/5045.

---

**Problem**: zenoh-c CMake include errors: headers not found after FetchContent.
**Cause**: Header includes were broken in some versions (fixed in zenoh-c PR #1044).
**Fix**: Upgrade to a release that includes this fix. Ensure `include_directories()` points to the fetched source tree.

---

## Embedded / zenoh-pico Issues

**Problem**: zenoh-pico on ESP32 fails to connect to `demo.zenoh.io`.
**Cause**: `demo.zenoh.io` is not a permanently-running public server — it is only online during ZettaScale demos.
**Fix**: Run your own Zenoh router. On a machine accessible from the ESP32:
```bash
zenohd
```
Then point the ESP32 at that IP. Confirm connectivity with a ping/TCP test first.

---

**Problem**: zenoh-pico ESP32 session fails repeatedly with `"Zenoh session failed. Retry in 27 sec..."`.
**Cause**: Could be NVS flash corruption, Wi-Fi not yet connected when zenoh init runs, or router unreachable.
**Fix**:
1. Erase NVS flash: `ESP_ERROR_CHECK(nvs_flash_erase())` before `nvs_flash_init()`.
2. Ensure Wi-Fi is fully connected (got IP) before starting zenoh.
3. Confirm router is reachable from ESP32 subnet.

---

**Problem**: zenoh-pico peers cannot find each other on a constrained network.
**Cause**: zenoh-pico peer mode does not support mesh routing (unlike the full Rust stack). Without a router, peer discovery requires multicast to work.
**Fix**: For embedded deployments without multicast, use client mode and run a `zenohd` router accessible from all devices.

---

## Key Expression Issues

**Problem**: Key expression rejected as invalid at runtime.
**Cause**: Key contains truly forbidden characters (`?`, `#`, or `//`), or uses `$` outside of `$*`, or is in non-canonical form. Note: `*` and `$*` are valid wildcards with placement rules, not forbidden characters.
**Fix**: Remove forbidden characters (`?`, `#`, `//`). Use `/` as the only separator. Canonical form rules:
- `**/**` → use `**`
- `**/*` → use `*/**`
- `$*$*` → use `$*`

---

**Problem**: Wildcard subscriber receives fewer messages than expected.
**Cause**: `*` only matches a single path segment. `a/*/c` does NOT match `a/b/b/c`.
**Fix**: Use `**` for multi-segment matching: `a/**/c` matches any depth.

---

**Problem**: Switching from `.` to `/` as key separator causes existing subscriptions to miss messages.
**Cause**: Key expressions are matched as strings — `sensor.imu` and `sensor/imu` are completely different keys.
**Fix**: Update all publishers and subscribers simultaneously to use `/`. The migration is a breaking change to your key space. Note: after migrating, CPU usage typically drops ~50% due to Zenoh's `/`-separator optimizations.

---

## Performance Issues

**Problem**: High latency at low message rates.
**Cause**: OS scheduler descheduling — at low rates, processes sleep between messages and wake-up adds latency. This is expected behavior, not a bug.
**Fix**: For latency-sensitive low-rate topics, use the `express` publication option (bypasses batching), or apply OS-level tuning: CPU affinity, real-time scheduling (`SCHED_FIFO`), and `isolcpus` kernel parameters. See `performance-tuning-guide.md` for details.

---

**Problem**: Throughput is lower than expected when using a router (`zenohd`).
**Cause**: Each extra router hop adds serialization/deserialization overhead. Large payloads are most affected when passing through multiple hops.
**Fix**: For local networks, use peer mode to eliminate the router hop entirely. For cross-network traffic where a router is required, tune `transport/unicast/lowlatency` and batch sizes in the config.

---

**Problem**: CPU usage is high even with moderate message rates.
**Cause**: Likely non-canonical key expressions or using `.` as separator instead of `/`.
**Fix**: Switch to `/` as separator. Validate key expressions are in canonical form. Profile with `RUST_LOG=zenoh=debug` to identify hot paths.

---

## Python-Specific Issues

**Problem**: Python script hangs on exit.
**Cause**: Session was not closed before script exit. Object finalizers may be called after the library thread exits.
**Fix**: Always use a context manager:
```python
with zenoh.open(conf) as session:
    ...
```
Or call `session.close()` explicitly before exit.

---

**Problem**: `'int' object is not iterable` when processing received payloads.
**Cause**: Payload deserialization returns raw bytes/string, not a Python iterable of the original type without explicit deserialization.
**Fix**: Call `sample.payload.to_string()` or deserialize explicitly. Do not iterate over the raw payload object.

---

## Admin Space / REST Debugging

**Problem**: Cannot query the admin space to inspect router state.
**Cause**: Admin space is read-only by default and may not be enabled.
**Fix**: Start `zenohd` with REST enabled:
```bash
zenohd --rest-http-port 8080
```
Query router state:
```bash
# List all declared publishers
curl http://localhost:8080/@/*/router/publisher/**

# List all subscribers
curl http://localhost:8080/@/*/router/subscriber/**

# List all storages
curl http://localhost:8080/@/*/router/**

# Get specific stored value
curl http://localhost:8080/my/key/expression
```

---

## Debugging Tools

### Enable verbose logging

**Rust**: Set the `RUST_LOG` environment variable:
```bash
RUST_LOG=zenoh=debug ./my_zenoh_app
# Or trace-level (very verbose):
RUST_LOG=zenoh=trace ./my_zenoh_app
# Only transport layer:
RUST_LOG=zenoh_transport=debug ./my_zenoh_app
```

**Python**:
```python
zenoh.init_log_from_env_or("debug")
# Or set: RUST_LOG=zenoh=debug python3 my_app.py
```

**C/C++**:
```c
zc_init_log_from_env_or("debug");
```

### Log level meanings
- `error` — only fatal errors (default in examples)
- `warn` — warnings and errors
- `info` — connection events, session lifecycle
- `debug` — routing decisions, scouting, keyexpr matching
- `trace` — every packet, frame, and byte (very high volume)

### REST admin space queries
The REST API (default port 8080 per the plugin's config.json5) exposes the full router state. Useful queries:
```bash
# All router info
curl http://localhost:8080/@/**

# Specific router's routes
curl http://localhost:8080/@/**

# Ping: write a value and read it back
curl -X PUT -d "hello" http://localhost:8080/test/ping
curl http://localhost:8080/test/ping
```

Enable write access to the admin space with `--adminspace-permissions rw`.

### Scout for active Zenoh nodes
```bash
# Using the z_scout example (Rust):
./target/release/examples/z_scout

# Using Python:
python3 z_scout.py
```

### Check what's stored in memory storage
```bash
# With REST plugin enabled and a memory storage on "myhome/**":
curl http://localhost:8080/myhome/**
```

---

## Quick Diagnostic Checklist

1. Is `zenohd` running? → `ps aux | grep zenohd`
2. Is port 7447 open? → `nc -zv <router-ip> 7447`
3. Are both sides on the same major version? → `zenohd --version`
4. Is multicast available? → Check if cloud/Docker blocks UDP 7446
5. Are modes correct? → At least one peer or a router required; two clients cannot discover each other
6. Are [key expressions](key-expressions-guide.md) compatible? → Test with exact (non-wildcard) keys first
7. Enable `RUST_LOG=zenoh=debug` and check for connection/routing errors
8. Query [admin space](admin-space-guide.md): `curl http://localhost:8080/@/**`

## See Also

- [FAQ](faq.md) — common questions and quick answers organized by category
- [Config Connect Listen](config-connect-listen.md) — connection timeout and retry configuration for the connection issues documented here
- [Scouting Guide](scouting-guide.md) — discovery configuration when multicast doesn't work
- [Encryption Guide](encryption-guide.md) — TLS troubleshooting for the security issues section
- [Admin Space Guide](admin-space-guide.md) — how to use the admin space to diagnose routing and subscription issues
