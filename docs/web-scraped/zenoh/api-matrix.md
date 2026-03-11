# Zenoh Language Bindings Feature Parity Matrix

---

## Language Bindings Overview

| Binding | Language | Implementation | Status | Description |
|---------|----------|---------------|--------|-------------|
| **zenoh** | Rust | Native | ✅ Stable | Primary reference implementation. All features land here first. |
| **zenoh-python** | Python | Rust (PyO3/maturin) | ✅ Stable | Full-featured binding; ships binary wheels on PyPI. |
| **zenoh-c** | C | Rust (FFI) | ✅ Stable | C binding over the Rust implementation; basis for zenoh-cpp. |
| **zenoh-cpp** | C++ | C (header-only) | ✅ Stable | C++17 header-only wrapper over zenoh-c or zenoh-pico. |
| **zenoh-kotlin** | Kotlin / JVM / Android | Rust (JNI) | ✅ Stable | JVM + Android targets via Zenoh-JNI native library. |
| **zenoh-java** | Java / JVM / Android | Rust (JNI) | ✅ Stable | Java-compatible Kotlin binding; same JNI backend as zenoh-kotlin. |
| **zenoh-ts** | TypeScript / JavaScript | WebSocket | ⚠️ Active dev | Browser + Deno client via `zenoh-plugin-remote-api`; no direct transport. |
| **zenoh-csharp** | C# | TBD | 🔄 Planned | Officially on roadmap; no code yet. |
| **zenoh-go** | Go | TBD | 🔄 Planned | Officially on roadmap; no code yet. |
| **zenoh-pico** | C (embedded) | Pure C | ✅ Stable | Lightweight native C implementation for constrained/embedded devices. |

---

## Feature Matrix

### Legend
| Symbol | Meaning |
|--------|---------|
| ✅ | Full support |
| ⚠️ | Partial / limited support |
| ❌ | Not supported |
| 🔄 | In progress / planned |
| N/A | Not applicable to this binding |

---

### Core Pub/Sub & Query

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| **Publisher** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Subscriber** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Queryable** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Session.get()** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Querier (declared)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |

> **Notes:**
> - `Querier` (a declared, reusable `get` endpoint) was introduced in zenoh 1.x. zenoh-pico targets constrained devices and omits this higher-level abstraction. TypeScript support depends on the remote-API plugin version.

---

### Advanced / Unstable Features

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| **Liveliness tokens** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ⚠️ |
| **Liveliness subscriber** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ⚠️ |
| **Liveliness get** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| **Matching status** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| **Matching listener** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| **Unstable API features** | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | 🔄 | 🔄 | ⚠️ |

> **Notes:**
> - Liveliness is marked as **unstable** in the Rust API (`#[cfg(feature = "unstable")]`). All bindings expose it conditionally.
> - zenoh-pico has partial liveliness support (token declaration + subscriber) but the `liveliness.get()` call is not yet implemented.
> - Matching status/listener require the publisher to query the router for subscriber matches — a feature not yet bridged in the TypeScript remote-API plugin or available in zenoh-pico.
> - Unstable APIs in C/C++ are gated behind the `ZENOHC_BUILD_WITH_UNSTABLE_API` CMake flag.

---

### Shared Memory (SHM)

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| **Shared Memory (SHM)** | ✅ | ⚠️ | ✅ | ✅ | ❌ | ❌ | ❌ | 🔄 | 🔄 | ❌ |
| **SHM automatic negotiation** | ✅ | ⚠️ | ✅ | ✅ | ❌ | ❌ | ❌ | 🔄 | 🔄 | ❌ |

> **Notes:**
> - Rust: SHM requires the `shared-memory` Cargo feature (`zenoh = { features = ["shared-memory"] }`).
> - C: Requires `-DZENOHC_BUILD_WITH_SHARED_MEMORY=true` at CMake configure time.
> - C++: Inherits SHM from the zenoh-c backend; not available with zenoh-pico backend.
> - Python: SHM can be enabled by building from source with `--features=zenoh/shared-memory`; not available in default PyPI wheels.
> - Kotlin/Java: JNI boundary makes zero-copy SHM semantics impractical; not planned.
> - TypeScript: Architecturally incompatible — data is serialized over WebSocket.
> - zenoh-pico: Pure C embedded implementation; no shared memory subsystem.

---

### Transport Protocols

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| **TCP transport** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ✅ |
| **UDP transport** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ✅ |
| **QUIC transport** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ❌ |
| **TLS transport** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ❌ |
| **WebSocket transport** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Serial transport** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | N/A | ❌ | ❌ | ✅ |
| **Bluetooth Serial** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | N/A | ❌ | ❌ | ✅ |

> **Notes:**
> - TypeScript connects exclusively via WebSocket to `zenoh-plugin-remote-api`; the underlying transport layer is managed by the `zenohd` router, not the TypeScript client.
> - zenoh-pico does not support QUIC or TLS because these require `std` / heavyweight TLS libraries incompatible with embedded targets.
> - zenoh-pico uniquely supports Serial (UART), USB-CDC Serial (experimental), and Bluetooth Serial profile on Arduino/Zephyr.
> - Emscripten builds of zenoh-pico use WebSocket as the only transport.
> - Transport features in Rust bindings (Python/C/C++/Kotlin/Java) can be tuned via Cargo features (e.g., `transport_tcp`, `transport_udp`).

---

### Middleware & Infrastructure Features

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| **Compression** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ❌ |
| **Access Control (ACL)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| **Admin space** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| **Scouting API** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ✅ |
| **Scout function** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ✅ |
| **Plugin development** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

> **Notes:**
> - Compression is configured on the router/transport layer via config files; all Rust-backed bindings inherit it transparently. zenoh-pico omits compression to save flash/RAM.
> - ACL is enforced by the zenoh router (`zenohd`). Client libraries pass config but enforcement is always router-side. TypeScript clients inherit ACL enforcement from the router but cannot configure it programmatically via the TS library.
> - Admin space (`@/...` key space) is queryable by any binding that supports `session.get()`; direct admin-space management APIs are primarily a Rust/router concept.
> - Plugin development (`zenohd` plugins) is exclusively a Rust capability, as plugins must link against the Rust zenoh runtime.

---

### Key Expression Operators

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| **Key expression operators** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ⚠️ |

> **Notes:**
> - "Key expression operators" refers to programmatic KE manipulation: intersection test, canonicalization, concatenation, autocanonization, etc.
> - TypeScript exposes basic key expression strings but does not implement the full operator algebra locally (relies on router for matching).
> - zenoh-pico supports the core wildcard matching and intersection test but may not expose the full set of KE operators available in the Rust API.

---

### API Style & Handler Types

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| **Async API** | ✅ | ✅ | ❌ | ❌ | ✅ | ⚠️ | ✅ | 🔄 | 🔄 | ❌ |
| **Callbacks (sync)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **FIFO channel handler** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| **Ring channel handler** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |

> **Notes:**
> - **Rust**: First-class `async/await` via Tokio; handlers return `Receiver<T>` for FIFO/ring channel patterns.
> - **Python**: Async via `asyncio`; subscribers/queryables support both callback and `async for` iteration patterns.
> - **C/C++**: Purely synchronous/callback-based; no async runtime. FIFO handlers are exposed as blocking queues (`z_fifo_handler_*`).
> - **Kotlin**: Coroutine-based async; `Channel`-backed FIFO handlers available.
> - **Java**: `CompletableFuture`-based async (partial); primarily callback-driven.
> - **TypeScript**: Fully async (`Promise`/`async-await`); FIFO-like via async iteration.
> - **zenoh-pico**: Callback-only; no RTOS-agnostic channel abstraction.

---

### zenoh-ext (Extended APIs)

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| **zenoh-ext serialization helpers** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| **AdvancedPublisher** | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | 🔄 | 🔄 | ❌ |
| **AdvancedSubscriber** | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ❌ | 🔄 | 🔄 | ❌ |

> **Notes:**
> - **zenoh-ext serialization**: Lightweight, universal serialization format for primitive types and common containers. Supported across all mature Rust-backed bindings and TypeScript (via the remote-API plugin's protocol support).
> - **AdvancedPublisher/AdvancedSubscriber**: Provides publication cache, sample miss detection, and retransmission. These are explicitly marked as part of `zenoh-ext` and bindings vary in how completely they expose this API surface. Marked ⚠️ where only partial subset (e.g., publication cache only) is exposed.
> - zenoh-pico does not include `zenoh-ext` functionality due to its resource-constrained target environment.

---

## Summary Heatmap

| Feature Group | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|--------------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| Core Pub/Sub/Query | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| Liveliness | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ⚠️ |
| Matching | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| Shared Memory | ✅ | ⚠️ | ✅ | ✅ | ❌ | ❌ | ❌ | 🔄 | 🔄 | ❌ |
| Transports | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ⚠️ |
| Infra (ACL/Admin) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| Scouting | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ✅ |
| Async API | ✅ | ✅ | ❌ | ❌ | ✅ | ⚠️ | ✅ | 🔄 | 🔄 | ❌ |
| Channel Handlers | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| zenoh-ext | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | 🔄 | 🔄 | ❌ |
| Plugin dev | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## Per-Language Notes

### Rust (zenoh)
- **Version**: 1.5.1 (current stable)
- **Repository**: https://github.com/eclipse-zenoh/zenoh
- **Docs**: https://docs.rs/zenoh/latest/zenoh/
- **Notes**:
  - Primary reference implementation; all features land here first.
  - Unstable features guarded by `#[cfg(feature = "unstable")]`.
  - SHM requires `features = ["shared-memory"]`.
  - Plugin API in `zenoh/plugins` crate; plugins must be written in Rust.
  - MSRV: 1.75.0 (with `zenoh-pinned-deps-1-75` for compatibility crate).
  - `zenoh-ext` crate provides `AdvancedPublisher`, `AdvancedSubscriber`, serialization.

---

### Python (zenoh-python)
- **Version**: tracks zenoh 1.x (1.1.x / 1.5.x)
- **Repository**: https://github.com/eclipse-zenoh/zenoh-python
- **Docs**: https://zenoh-python.readthedocs.io/
- **PyPI**: `pip install eclipse-zenoh`
- **Tested Python versions**: 3.8 – 3.12
- **Notes**:
  - Built with PyO3 + maturin; binary wheels for Linux x86_64/i686/ARM, macOS universal2, Windows amd64.
  - SHM requires building from source: `pip install eclipse-zenoh --no-binary :all: --config-settings build-args="--features=zenoh/shared-memory"`.
  - Supports both callback and `async/await` (`asyncio`) APIs.
  - `zenoh-ext` serialization available; `AdvancedPublisher/Subscriber` partially exposed.
  - Requires Rust toolchain only when building from source distribution.

---

### C (zenoh-c)
- **Version**: tracks zenoh 1.x (CMake `MAJOR.MINOR.PATCH.TWEAK` versioning)
- **Repository**: https://github.com/eclipse-zenoh/zenoh-c
- **Docs**: https://zenoh-c.readthedocs.io/
- **Notes**:
  - CMake-based build; links Rust library via FFI.
  - Unstable API: `-DZENOHC_BUILD_WITH_UNSTABLE_API=true`.
  - SHM: `-DZENOHC_BUILD_WITH_SHARED_MEMORY=true`.
  - Cross-compilation supported via CMake toolchain files + `ZENOHC_CUSTOM_TARGET`.
  - MSRV: 1.75.0.
  - No async runtime; purely callback/blocking.
  - `zenoh-ext` subset exposed (serialization, some advanced pub/sub).
  - Transport features selectable via `ZENOHC_CARGO_FLAGS` (e.g., `--no-default-features;--features=transport_tcp`).

---

### C++ (zenoh-cpp)
- **Version**: tracks zenoh-c version
- **Repository**: https://github.com/eclipse-zenoh/zenoh-cpp
- **Docs**: https://zenoh-cpp.readthedocs.io/
- **Notes**:
  - Header-only C++17 library; requires either zenoh-c or zenoh-pico as backend.
  - `zenohcxx::zenohc` target for zenoh-c backend; `zenohcxx::zenohpico` for zenoh-pico backend.
  - Features available depend heavily on which backend is used:
    - zenoh-c backend: full feature set including SHM.
    - zenoh-pico backend: limited to zenoh-pico's constrained feature set.
  - Examples split into `universal/` (both backends) and `zenohc/` (zenoh-c specific).
  - Still marked "under active development" for broader platform testing.
  - No async runtime; synchronous/callback API only.

---

### Kotlin (zenoh-kotlin)
- **Version**: 1.1.1 (current)
- **Repository**: https://github.com/eclipse-zenoh/zenoh-kotlin
- **Docs**: https://eclipse-zenoh.github.io/zenoh-kotlin/
- **Maven**: `org.eclipse.zenoh:zenoh-kotlin-jvm:1.1.1` / `org.eclipse.zenoh:zenoh-kotlin-android:1.1.1`
- **Notes**:
  - Rust JNI native library (`zenoh-jni`) bridges Kotlin ↔ Rust.
  - JVM targets: x86_64/aarch64 on Linux, macOS, Windows.
  - Android targets: x86, x86_64, arm, arm64 (min SDK 30); requires NDK 26.0.10792818.
  - Kotlin Coroutines-based async API.
  - Rust logs via `RUST_LOG` env var; programmatic via `Zenoh.initLogFromEnvOr(level)`.
  - SHM not supported (JNI boundary prevents zero-copy semantics).
  - `zenoh-ext` serialization supported; AdvancedPublisher/Subscriber partial.

---

### Java (zenoh-java)
- **Version**: 1.1.1 (current)
- **Repository**: https://github.com/eclipse-zenoh/zenoh-java
- **Docs**: https://eclipse-zenoh.github.io/zenoh-java/
- **Maven**: `org.eclipse.zenoh:zenoh-java-jvm:1.1.1` / `org.eclipse.zenoh:zenoh-java-android:1.1.1`
- **Notes**:
  - Shares the same Rust JNI backend as zenoh-kotlin (`zenoh-jni`).
  - Java-compatible API layer on top of the Kotlin implementation.
  - Same platform matrix as zenoh-kotlin (JVM + Android).
  - `CompletableFuture`-based async where applicable; primarily callback-driven.
  - All limitations of zenoh-kotlin apply (no SHM, etc.).
  - Logging via `RUST_LOG` or `Zenoh.initLogFromEnvOr(level)`.

---

### TypeScript (zenoh-ts)
- **Version**: tracks latest plugin API (npm `@eclipse-zenoh/zenoh-ts`)
- **Repository**: https://github.com/eclipse-zenoh/zenoh-ts
- **Docs**: https://eclipse-zenoh.github.io/zenoh-ts/
- **npm**: `npm install @eclipse-zenoh/zenoh-ts`
- **Notes**:
  - **Architecture**: NOT a direct zenoh transport binding. All communication goes through `zenoh-plugin-remote-api` (WebSocket plugin in `zenohd`).
  - Long-term plan is WASM target; currently requires router plugin.
  - Compatible with browsers and Deno; **not** Node.js (WebSocket library limitation).
  - Default WebSocket connection: `ws://localhost:10000`.
  - Full `async/await` API; `Promise`-based.
  - No SHM, no QUIC/TLS (transport is abstracted by the router).
  - No scouting API (requires direct UDP multicast, impossible in browser).
  - No matching status/listener (not bridged in remote-API protocol).
  - Serialization helpers available via the protocol.

---

### C# (zenoh-csharp)
- **Version**: Not yet released
- **Repository**: https://github.com/eclipse-zenoh/zenoh-csharp
- **Status**: 🔄 Work planned — on official roadmap
- **Contact**: contact@zettascale.tech
- **Notes**:
  - No code has been committed yet.
  - Expected to follow the C/Rust FFI pattern similar to zenoh-c.
  - All feature matrix entries are 🔄 (planned).

---

### Go (zenoh-go)
- **Version**: Not yet released
- **Repository**: https://github.com/eclipse-zenoh/zenoh-go
- **Status**: 🔄 Work planned — on official roadmap
- **Contact**: contact@zettascale.tech
- **Notes**:
  - No code has been committed yet.
  - Expected to use CGo bindings over zenoh-c or a native Go implementation.
  - All feature matrix entries are 🔄 (planned).

---

### C/pico (zenoh-pico)
- **Version**: tracks zenoh 1.x protocol compatibility
- **Repository**: https://github.com/eclipse-zenoh/zenoh-pico
- **Docs**: https://zenoh-pico.readthedocs.io/
- **Notes**:
  - **Pure C implementation** — does NOT link against the Rust zenoh library.
  - Targets constrained devices: Zephyr, Arduino, ESP-IDF, MbedOS, FreeRTOS, OpenCR, Raspberry Pi Pico, STM32 ThreadX.
  - Supports TCP, UDP (unicast + multicast), WebSocket, Serial (UART), USB-CDC (experimental), Bluetooth Serial.
  - Does **not** support: QUIC, TLS, SHM, compression, ACL config, admin space, ring/FIFO channel handlers, async runtimes, zenoh-ext.
  - Key tuning: `BATCH_UNICAST_SIZE`, `BATCH_MULTICAST_SIZE`, `FRAG_MAX_SIZE` CMake options for memory-constrained targets.
  - Unstable features gated by `Z_FEATURE_UNSTABLE_API` compile flag.
  - Liveliness: token + subscriber supported; `liveliness.get()` not implemented.
  - USB-CDC Serial requires `Z_FEATURE_LINK_SERIAL_USB` + `Z_FEATURE_UNSTABLE_API`.
  - Debug logs via `-DZENOH_LOG=DEBUG`.
  - Available as Debian/RPM/tgz packages for Linux; PlatformIO for embedded.

---

## Version Matrix

This table maps each binding's release version to the zenoh core protocol/API version it targets.

| Binding | Binding Version | Targets zenoh Core | Notes |
|---------|----------------|-------------------|-------|
| **zenoh (Rust)** | 1.5.1 | 1.5.1 | Reference implementation |
| **zenoh-python** | 1.x (tracks core) | 1.x | Version mirrors core; `pip install eclipse-zenoh` |
| **zenoh-c** | 1.x.y.z (CMake) | 1.x.y | CMake `MAJOR.MINOR.PATCH.TWEAK` → SemVer `MAJOR.MINOR.PATCH[-pre.TWEAK]` |
| **zenoh-cpp** | 1.x (tracks zenoh-c) | 1.x | Header-only; version tracks zenoh-c backend |
| **zenoh-kotlin** | 1.1.1 | 1.1.x | JNI backend version matches |
| **zenoh-java** | 1.1.1 | 1.1.x | Shares JNI backend with zenoh-kotlin |
| **zenoh-ts** | latest (npm) | 1.x (plugin) | Requires matching `zenoh-plugin-remote-api` version |
| **zenoh-csharp** | — (not released) | TBD | Planned |
| **zenoh-go** | — (not released) | TBD | Planned |
| **zenoh-pico** | 1.x (tracks protocol) | Protocol 1.x | Independent C impl; protocol-