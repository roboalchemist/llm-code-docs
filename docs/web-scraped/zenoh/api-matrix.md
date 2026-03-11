# Zenoh Language Bindings Feature Parity Matrix

---

## Language Bindings Overview

| Binding | Language | Implementation | Status | Primary Use Case |
|---------|----------|----------------|--------|-----------------|
| **zenoh** (Rust) | Rust | Native (reference) | ✅ Stable | All platforms, primary reference |
| **zenoh-python** | Python | Rust FFI via PyO3/maturin | ✅ Stable | Data science, scripting, rapid prototyping |
| **zenoh-c** | C | Rust FFI (C wrapper) | ✅ Stable | Native C applications, embedded systems |
| **zenoh-cpp** | C++ | Header-only C++ wrapper over zenoh-c or zenoh-pico | ✅ Stable | C++ applications, robotics (ROS2) |
| **zenoh-kotlin** | Kotlin/JVM/Android | Rust JNI (Zenoh-JNI) | ✅ Stable | Android, JVM applications |
| **zenoh-java** | Java/JVM/Android | Rust JNI (Zenoh-JNI, Kotlin-based) | ✅ Stable | Android, JVM applications |
| **zenoh-ts** | TypeScript/JavaScript | WebSocket → zenoh-plugin-remote-api | ⚠️ Active Development | Browser, Deno, web applications |
| **zenoh-csharp** | C# | Planned | 🔄 Planned | .NET applications |
| **zenoh-go** | Go | Planned | 🔄 Planned | Go applications |
| **zenoh-pico** | C (pure) | Native C (not Rust-based) | ✅ Stable | Constrained/embedded devices, microcontrollers |

> **Note:** zenoh-cpp can use either zenoh-c or zenoh-pico as its backend. Feature availability in zenoh-cpp depends on which backend is used.

---

## Feature Matrix

### Legend
| Symbol | Meaning |
|--------|---------|
| ✅ | Full support |
| ⚠️ | Partial / limited support |
| ❌ | Not supported |
| 🔄 | In progress / planned |
| N/A | Not applicable |

---

### Core Pub/Sub & Query

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Publisher** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Subscriber** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Queryable** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Session.get()** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Querier (declared)** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |

> **Querier (declared):** A pre-declared `Querier` entity for repeated gets, similar to how `Publisher` is a pre-declared entity for repeated puts. Not yet available in zenoh-pico or the zenoh-pico backend for zenoh-cpp.

---

### Liveliness

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Liveliness token** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| **Liveliness subscriber** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| **Liveliness get** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |

> Liveliness APIs are marked unstable in zenoh core and require enabling unstable feature flags in C/C++.

---

### Matching & Observability

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Matching status** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| **Matching listener** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |

> Matching status/listener allows a publisher to know whether there are active subscribers on its key expression.

---

### Shared Memory (SHM)

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Shared Memory (SHM)** | ✅ | ⚠️ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 🔄 | 🔄 | ❌ |
| **SHM automatic negotiation** | ✅ | ⚠️ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | 🔄 | 🔄 | ❌ |

> **Rust:** Full SHM support, enabled via `features = ["shared-memory"]` in Cargo.toml.  
> **C:** Requires `-DZENOHC_BUILD_WITH_SHARED_MEMORY=true` at CMake configuration time.  
> **Python:** Can be enabled at build time: `pip install eclipse-zenoh --no-binary :all: --config-settings build-args="--features=zenoh/shared-memory"`. Not available in standard binary wheels.  
> **C++ (zenoh-c backend):** Available when zenoh-c is built with SHM support.  
> **zenoh-pico:** Pure C implementation; no SHM support by design (constrained device focus).

---

### Transport Protocols

| Transport | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|-----------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **TCP** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ✅ |
| **UDP (unicast)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ✅ |
| **UDP (multicast)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ✅ |
| **QUIC transport** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| **TLS transport** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| **WebSocket transport** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ⚠️ |
| **Serial** | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

> **TypeScript:** Does not implement transports directly — it connects exclusively via WebSocket to the `zenoh-plugin-remote-api`. All other transports are handled server-side by `zenohd`.  
> **zenoh-pico WebSocket:** Available for Emscripten (WASM) target only.  
> **QUIC/TLS:** Rust-based bindings inherit from zenoh core. Enabled via cargo features (`transport_quic`, `transport_tls`). Not available in pure-C zenoh-pico.

---

### Network & Protocol Features

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Compression** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | N/A | 🔄 | 🔄 | ❌ |
| **Access Control (ACL)** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ⚠️ |
| **Admin space** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |

> **ACL:** Configured via the zenoh router config file (`zenohd`). Client-side bindings respect ACL enforcement by the router. Direct ACL configuration API varies per binding.  
> **Admin space:** Accessible via `@/...` key expressions through any binding's `get()`. Direct admin API (e.g., Rust's `Session::admin()`) may not be exposed in all bindings.

---

### Discovery & Scouting

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Scouting API** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ✅ |
| **Scout function** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ✅ |

> **Scout function:** Standalone `zenoh::scout()` call to discover peers/routers without opening a full session. Available in most mature bindings.

---

### Key Expression Operations

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Key expression operators** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Key expression concat** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Key expression intersects/includes** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Declared key expressions** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |

---

### zenoh-ext / Extended Features

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **zenoh-ext serialization helpers** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| **AdvancedPublisher** | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ | ⚠️ | ❌ | 🔄 | 🔄 | ❌ |
| **AdvancedSubscriber** | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ | ⚠️ | ❌ | 🔄 | 🔄 | ❌ |
| **Publication cache** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| **Querying subscriber** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |

> **zenoh-ext serialization:** Universal serialization helpers for primitives and common types. Designed to be interoperable across all bindings.  
> **C++ (zenoh-pico backend):** Limited zenoh-ext support as zenoh-pico does not expose the full ext API.

---

### API Style & Concurrency

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Async API** | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| **Callbacks (sync)** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **FIFO channel handler** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| **Ring channel handler** | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |

> **Async API:**  
> - Rust: native `async/await` with tokio  
> - Python: `async/await` via asyncio  
> - Kotlin/Java: coroutines / CompletableFuture  
> - TypeScript: Promise/async-await  
> - C/C++: synchronous only (callbacks, no async runtime)  
> - zenoh-pico: synchronous only (designed for constrained environments)

---

### Advanced / Developer Features

| Feature | Rust | Python | C | C++ (zenoh-c) | C++ (zenoh-pico) | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|------|--------|---|---------------|------------------|--------|------|------------|----|----|------------|
| **Unstable features flag** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ✅ |
| **Plugin development** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Timestamps** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Encoding metadata** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| **Attachment metadata** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ⚠️ |
| **Session info / zid** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |

> **Plugin development:** Only possible in Rust via the `zenoh` plugin API. Plugins run inside `zenohd` and have access to internal APIs. The `zenoh-plugin-remote-api` used by TypeScript is an example of such a Rust plugin.

---

## Consolidated Feature Summary

| Feature | Rust | Python | C | C++ | Kotlin | Java | TypeScript | C# | Go | zenoh-pico |
|---------|:----:|:------:|:-:|:---:|:------:|:----:|:----------:|:--:|:--:|:----------:|
| Publisher / Subscriber | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| Queryable / Session.get() | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| Querier (declared) | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| Liveliness tokens + sub + get | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| Matching status + listener | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| Shared Memory (SHM) | ✅ | ⚠️ | ✅ | ⚠️ | ❌ | ❌ | ❌ | 🔄 | 🔄 | ❌ |
| SHM automatic negotiation | ✅ | ⚠️ | ✅ | ⚠️ | ❌ | ❌ | ❌ | 🔄 | 🔄 | ❌ |
| QUIC transport | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| TLS transport | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| WebSocket transport | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ⚠️ |
| Compression | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 🔄 | 🔄 | ❌ |
| Access Control (ACL) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ⚠️ |
| Admin space | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| Scouting API | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ✅ |
| Scout function | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ✅ |
| Key expression operators | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| zenoh-ext serialization | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| Async API | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ❌ |
| Callbacks (sync) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔄 | 🔄 | ✅ |
| FIFO channel handler | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ❌ |
| Ring channel handler | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | 🔄 | 🔄 | ❌ |
| Unstable features | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | 🔄 | 🔄 | ✅ |
| Plugin development | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## Per-Language Notes

### 🦀 Rust (zenoh)

- **Current version:** 1.5.1
- **Repository:** https://github.com/eclipse-zenoh/zenoh
- **Docs:** https://docs.rs/zenoh/latest/zenoh/ | https://docs.rs/zenoh-ext/latest/zenoh_ext/
- **Status:** Primary reference implementation. All features available here first.
- **Notes:**
  - All unstable APIs gated behind `#[cfg(feature = "unstable")]`
  - SHM requires `features = ["shared-memory"]` in Cargo.toml
  - zenoh-ext provides `AdvancedPublisher`, `AdvancedSubscriber`, serialization helpers, publication cache, querying subscriber
  - Tokio-based async runtime; supports both callback and channel-based handler patterns
  - Plugin API available for extending `zenohd`
  - MSRV: Rust 1.75.0 (with pinned deps crate)

---

### 🐍 Python (zenoh-python)

- **Current version:** 1.x (tracks zenoh core)
- **Repository:** https://github.com/eclipse-zenoh/zenoh-python
- **Docs:** https://zenoh-python.readthedocs.io/
- **Status:** Stable, actively maintained
- **Notes:**
  - Built with PyO3/maturin — requires Rust toolchain to build from source
  - Binary wheels provided for Linux x86_64, i686, ARM, macOS universal2, Windows amd64
  - Python 3.8–3.12 supported
  - SHM requires building from source: `pip install eclipse-zenoh --no-binary :all: --config-settings build-args="--features=zenoh/shared-memory"`
  - Supports both synchronous callbacks and `async/await` via asyncio
  - Unstable features require building with appropriate feature flags

---

### 🇨 C (zenoh-c)

- **Current version:** 1.x (tracks zenoh core, CMake versioning)
- **Repository:** https://github.com/eclipse-zenoh/zenoh-c
- **Docs:** https://zenoh-c.readthedocs.io/
- **Status:** Stable, actively maintained
- **Notes:**
  - Rust FFI wrapper; requires Rust toolchain to build
  - MSRV: Rust 1.75.0
  - SHM enabled with `-DZENOHC_BUILD_WITH_SHARED_MEMORY=true`
  - Unstable API enabled with `-DZENOHC_BUILD_WITH_UNSTABLE_API=true`
  - Supports cross-compilation via CMake toolchain files + `ZENOHC_CUSTOM_TARGET`
  - No async API; all operations are synchronous with callbacks or channel handlers
  - Memory management follows explicit owned/loaned/moved pattern

---

### ➕➕ C++ (zenoh-cpp)

- **Current version:** 1.x (tracks zenoh-c / zenoh-pico)
- **Repository:** https://github.com/eclipse-zenoh/zenoh-cpp
- **Docs:** https://zenoh-cpp.readthedocs.io/
- **Status:** Stable, actively maintained (note: "still under active development" per README)
- **Notes:**
  - Header-only C++17 library; wraps either zenoh-c or zenoh-pico backend
  - Feature set depends heavily on which backend is selected
  - zenoh-c backend: near-full feature parity with C binding
  - zenoh-pico backend: limited to features supported by zenoh-pico
  - Examples split into `universal/` (both backends) and `zenohc/` (zenoh-c specific)
  - No async API; synchronous callbacks only
  - All zenoh functionality under `zenoh::` namespace via `#include "zenoh.hxx"`

---

### 🎯 Kotlin (zenoh-kotlin)

- **Current version:** 1.1.1
- **Repository:** https://github.com/eclipse-zenoh/zenoh-kotlin
- **Docs:** https://eclipse-zenoh.github.io/zenoh-kotlin/index.html
- **Status:** Stable, actively maintained
- **Notes:**
  - JNI-based binding using Zenoh-JNI (Rust) native library
  - Targets JVM and Android (min SDK 30)
  - Android targets: x86, x86_64, arm, arm64
  - JVM targets: x86_64/aarch64 on Linux, macOS, Windows
  - Supports Kotlin coroutines for async patterns
  - Distributed via Maven Central: `org.eclipse.zenoh:zenoh-kotlin-jvm` / `zenoh-kotlin-android`
  - Android requires `INTERNET` and `ACCESS_NETWORK_STATE` permissions
  - Rust logs configurable via `RUST_LOG` env var or `Zenoh.initLogFromEnvOr()`

---

### ☕ Java (zenoh-java)

- **Current version:** 1.1.1
- **Repository:** https://github.com/eclipse-zenoh/zenoh-java
- **Docs:** https://eclipse-zenoh.github.io/zenoh-java/index.html
- **Status:** Stable, actively maintained
- **Notes:**
  - Java-compatible API built on the same Kotlin/JNI infrastructure as zenoh-kotlin
  - Feature parity with zenoh-kotlin; same native library (Zenoh-JNI)
  - Same platform support as zenoh-kotlin (JVM + Android)
  - Distributed via Maven Central: `org.eclipse.zenoh:zenoh-java-jvm` / `zenoh-java-android`
  - Uses `CompletableFuture` patterns for async operations
  - Android min SDK 30; same platform targets as zenoh-kotlin

---

### 🌐 TypeScript (zenoh-ts)

- **Current version:** Latest on npm `@eclipse-zenoh/zenoh-ts`
- **Repository:** https://github.com/eclipse-zenoh/zenoh-ts
- **Docs:** https://eclipse-zenoh.github.io/zenoh-ts/
- **Status:** Active development
- **Notes:**
  - **Architecture is fundamentally different:** All operations are proxied over WebSocket through `zenoh-plugin-remote-api` running inside `zenohd`
  - Does **not** directly connect to Zenoh network — requires a running `zenohd` with the remote-api plugin or `zenoh-bridge-remote-api`
  - Transport, SHM, compression