# Zenoh Shared Memory (SHM) Documentation

## Table of Contents

1. [Overview](#overview)
2. [How SHM Works](#how-shm-works)
3. [Platform Support](#platform-support)
4. [Requirements](#requirements)
5. [Configuration](#configuration)
6. [API Reference](#api-reference)
7. [Automatic vs Explicit SHM](#automatic-vs-explicit-shm)
8. [SHM Cleanup](#shm-cleanup)
9. [Performance](#performance)
10. [Limitations](#limitations)
11. [Language Binding Support](#language-binding-support)
12. [Code Examples](#code-examples)

---

## Overview

Zenoh Shared Memory (SHM) enables **zero-copy publish/subscribe communication** between processes running on the same host. Instead of serializing data into a network buffer and copying it from publisher to subscriber, SHM lets the publisher write data once into a shared memory region that all local subscribers can read directly by pointer—no serialization, no copying.

**When to use SHM:**

- High-throughput, low-latency data pipelines on a single host (sensor data, video frames, point clouds)
- Large messages where copy overhead is measurable (images, LiDAR scans, ML tensors)
- Real-time systems where predictable latency matters more than network flexibility

**When SHM is not needed:**

- Messages crossing machine boundaries (SHM buffers are never transmitted over the network)
- Small messages where copy cost is negligible
- Scenarios where process isolation from shared memory is required

---

## How SHM Works

### Architecture

Zenoh SHM is built on a **provider/client** model on top of OS-level shared memory primitives (POSIX named shared memory on Linux/macOS, Windows shared memory objects on Windows).

```
  Publisher Process                    Subscriber Process
  ┌─────────────────────────────┐      ┌──────────────────────────────┐
  │  Application                │      │  Application                 │
  │  ┌──────────────────────┐   │      │  ┌───────────────────────┐   │
  │  │ ShmProvider          │   │      │  │ ShmClientStorage      │   │
  │  │ (allocates memory)   │   │      │  │ (attaches to segments)│   │
  │  └──────────┬───────────┘   │      │  └────────────┬──────────┘   │
  │             │               │      │               │              │
  │  ┌──────────▼───────────┐   │      │  ┌────────────▼──────────┐   │
  │  │ SHM Segment (mmap'd) │◄──┼──────┼──│ SHM Segment (mmap'd) │   │
  │  │  [data written here] │   │      │  │  [data read here]    │   │
  │  └──────────────────────┘   │      │  └───────────────────────┘   │
  │             │               │      │               ▲              │
  │  ┌──────────▼───────────┐   │      │               │              │
  │  │ Zenoh Session        │   │      │  ┌────────────┴──────────┐   │
  │  │ (sends descriptor)   ├───┼─────►│  │ Zenoh Session        │   │
  │  └──────────────────────┘   │      │  │ (receives descriptor) │   │
  └─────────────────────────────┘      └──────────────────────────────┘

  ═══════════════════════════════════════════════════════════════════
                    OS Shared Memory (POSIX / Windows)
  ═══════════════════════════════════════════════════════════════════
```

### Step-by-Step Flow

1. **Segment creation**: The publisher creates an `ShmProvider` backed by a POSIX shared memory segment of a configured size.
2. **Buffer allocation**: The publisher allocates a `ZShmMut` buffer from the provider. This is a slice of the shared memory segment.
3. **Data write**: The publisher writes data directly into the `ZShmMut` buffer.
4. **Descriptor transmission**: Instead of sending the data, Zenoh sends a small **chunk descriptor** over the normal transport (e.g., UDP, TCP). The descriptor contains:
   - Protocol ID (identifies the SHM protocol, e.g., POSIX = 0)
   - Segment ID (which shared memory segment)
   - Chunk offset and length (where in the segment the data lives)
5. **Segment attachment**: On the subscriber side, Zenoh's `ShmClientStorage` receives the descriptor. If it has not already done so, it calls `ShmClient::attach()` to memory-map the named segment into the subscriber's address space.
6. **Zero-copy delivery**: The subscriber's callback receives a `ZShm` (or `zshm`) reference pointing directly into the shared memory. No copy occurs.
7. **Reference counting and watchdog**: Zenoh maintains reference counts and a watchdog mechanism to track when buffers are safe to reclaim. The provider's busy list tracks all outstanding allocations.

### Provider/Subscriber Negotiation

SHM capability is negotiated during session establishment. Both publisher and subscriber must:

- Have SHM enabled in their transport configuration
- Share a compatible `ProtocolID` (the publisher's provider and the subscriber's client must speak the same protocol)

If SHM negotiation fails (e.g., the subscriber is on a different host, or SHM is not configured), Zenoh **automatically falls back** to copying the buffer contents into a regular network buffer and sending it over the wire. The publisher and subscriber application code does not need to change.

### Memory Layout and Allocators

The `ShmProvider` supports multiple allocator backends:

| Backend | Type | Characteristics |
|---|---|---|
| `PosixShmProviderBackendTalc` | **Default** | Best general-purpose performance; excellent fragmentation resistance |
| `PosixShmProviderBackendBuddy` | Alternative | Fastest raw allocation speed; higher fragmentation |
| `PosixShmProviderBackendBinaryHeap` | Legacy | Largest-fit; stores no metadata in SHM (crash-resistant) |

All backends manage memory within a single POSIX named shared memory segment created at provider construction time.

---

## Platform Support

| Platform | SHM Support | Notes |
|---|---|---|
| **Linux** | ✅ Full | POSIX `shm_open`; orphan cleanup supported |
| **macOS** | ✅ Full | POSIX `shm_open`; BSD locking variant used |
| **Windows** | ✅ Full | Windows named shared memory objects |
| **FreeBSD / DragonFly / NetBSD / OpenBSD** | ✅ Full | POSIX; external lockfile variant for advisory locking |
| **iOS / watchOS / tvOS / visionOS** | ⚠️ Limited | Apple targets; advisory locking variant |
| **Embedded / no-std** | ❌ Not supported | SHM requires OS primitives |

> **Note on Linux orphan cleanup:** Linux is currently the only platform where Zenoh can enumerate `/dev/shm` entries and detect orphaned segments from crashed processes. On other platforms, the cleanup routine is defined but currently a no-op for orphan detection.

---

## Requirements

For SHM communication to work between two processes:

1. **Same host**: Both publisher and subscriber must be on the same physical or virtual machine. SHM buffers are never transmitted over the network.

2. **SHM feature enabled at compile time**: Both processes must be built with the `shared-memory` feature flag enabled in their Zenoh dependency.

3. **SHM enabled in transport configuration**: The Zenoh session must have `transport.unicast.lowlatency` or SHM explicitly enabled in its config (see [Configuration](#configuration)).

4. **Compatible SHM protocol**: Both sides must share a `ShmClient`/`ShmProviderBackend` pair with the same `ProtocolID`. The built-in POSIX implementation uses `POSIX_PROTOCOL_ID = 0`.

5. **Sufficient OS-level shared memory quota**: On Linux, check `/proc/sys/kernel/shmmax` and `/proc/sys/kernel/shmall`. On macOS, see `sysctl kern.sysv.shmmax`.

---

## Configuration

### Enabling SHM in Transport Configuration

SHM is configured within the Zenoh session configuration JSON/JSON5. The key section is `transport.unicast`:

```json5
{
  transport: {
    unicast: {
      // Enable SHM transport
      lowlatency: false,
      
      // SHM is negotiated per-link
      shm: {
        enabled: true
      }
    }
  }
}
```

In code, you can build a config with SHM enabled:

```rust
use zenoh::config::Config;

let mut config = Config::default();
// Enable SHM transport negotiation
config
    .insert_json5("transport/unicast/shm/enabled", "true")
    .unwrap();
```

### SHM Provider Configuration

The `ShmProvider` is configured entirely in application code—there is no config-file format for provider parameters. You specify the memory segment size and alignment at construction:

```rust
use zenoh_shm::api::provider::{
    shm_provider::ShmProviderBuilder,
    types::AllocAlignment,
    memory_layout::MemoryLayout,
};
use zenoh_core::Wait;

// 64 MB segment with default (1-byte) alignment
let layout = MemoryLayout::new(64 * 1024 * 1024, AllocAlignment::default()).unwrap();
let provider = ShmProviderBuilder::default_backend(layout).wait().unwrap();
```

### SHM Size and Layout

The memory layout controls both the total segment size and the minimum allocation alignment:

```rust
use zenoh_shm::api::provider::{
    types::AllocAlignment,
    memory_layout::MemoryLayout,
};

// 1-byte alignment (default) — any size allocation
let layout_1b = MemoryLayout::new(16 * 1024 * 1024, AllocAlignment::ALIGN_1_BYTE).unwrap();

// 8-byte alignment — allocations are multiples of 8 bytes
let layout_8b = MemoryLayout::new(16 * 1024 * 1024, AllocAlignment::ALIGN_8_BYTES).unwrap();

// Alignment for a specific type (e.g., f64)
let layout_typed = MemoryLayout::for_type::<f64>();

// Custom power-of-2 alignment: AllocAlignment::new(pow)
// pow=0 → 1 byte, pow=1 → 2 bytes, pow=2 → 4 bytes, pow=3 → 8 bytes
let layout_4b = MemoryLayout::new(
    16 * 1024 * 1024,
    AllocAlignment::new(2).unwrap(),  // 4-byte alignment
).unwrap();
```

> **Constraint**: The segment size must be a multiple of the alignment. Zenoh will return `ZLayoutError::IncorrectLayoutArgs` if this is violated.

### Choosing Backend Allocator

```rust
use zenoh_shm::api::protocol_implementations::posix::{
    posix_shm_provider_backend_talc::PosixShmProviderBackendTalc,       // default
    posix_shm_provider_backend_buddy::PosixShmProviderBackendBuddy,     // fastest
    posix_shm_provider_backend_binary_heap::PosixShmProviderBackendBinaryHeap, // legacy
};
use zenoh_shm::api::provider::shm_provider::ShmProviderBuilder;
use zenoh_core::Wait;

// Use the buddy allocator backend explicitly
let layout = /* ... */;
let backend = PosixShmProviderBackendBuddy::builder(layout).wait().unwrap();
let provider = ShmProviderBuilder::backend(backend).wait();
```

---

## API Reference

### Publisher Side: Allocating and Sending SHM Buffers

#### Creating a Provider

```rust
use zenoh_shm::api::provider::{
    shm_provider::{ShmProviderBuilder, JustAlloc, GarbageCollect, BlockOn},
    types::AllocAlignment,
    memory_layout::MemoryLayout,
};
use zenoh_core::Wait;

let layout = MemoryLayout::new(
    64 * 1024 * 1024,   // 64 MB segment
    AllocAlignment::default(),
).unwrap();

let provider = ShmProviderBuilder::default_backend(layout)
    .wait()
    .expect("Failed to create SHM provider");
```

#### Allocating a Buffer

```rust
use zenoh_shm::api::provider::shm_provider::{JustAlloc, GarbageCollect, BlockOn};
use zenoh_core::Wait;

// Simple allocation — fails immediately if no memory available
let buf: ZShmMut = provider
    .alloc(1024usize)
    .wait()
    .expect("Allocation failed");

// With garbage collection fallback
let buf: ZShmMut = provider
    .alloc(1024usize)
    .with_policy::<GarbageCollect>()
    .wait()
    .expect("Allocation failed");

// Block until memory is available (sync)
let buf: ZShmMut = provider
    .alloc(1024usize)
    .with_policy::<BlockOn>()
    .wait()
    .expect("Allocation failed");

// Block until memory is available (async)
let buf: ZShmMut = provider
    .alloc(1024usize)
    .with_policy::<BlockOn>()
    .await
    .expect("Allocation failed");
```

#### Using Precomputed Layouts for Repeated Allocations

For high-frequency allocation of same-sized buffers, precompute the layout once:

```rust
let precomputed = provider
    .alloc_layout(1024usize)
    .expect("Layout computation failed");

// Allocate many buffers without re-computing layout
for _ in 0..1000 {
    let buf = precomputed.alloc().wait().expect("Allocation failed");
    // ... fill and publish buf
}
```

#### Typed Allocations

For structured data, use typed allocations:

```rust
use zenoh_shm::api::provider::memory_layout::TypedLayout;

#[repr(C)]
struct SensorData {
    timestamp: u64,
    x: f64,
    y: f64,
    z: f64,
}

// Allocate with type layout (MaybeUninit wrapping for safety)
let typed_buf = provider
    .alloc(TypedLayout::<SensorData>::new())
    .wait()
    .expect("Allocation failed");

// Initialize the value
let initialized = typed_buf.initialize(SensorData {
    timestamp: 12345,
    x: 1.0, y: 2.0, z: 3.0,
});
```

#### Writing Data and Publishing

```rust
// Write into the mutable buffer
let mut buf: ZShmMut = provider.alloc(1024usize).wait().unwrap();
buf.copy_from_slice(&data[..1024]);

// Publish — zenoh takes ownership and handles the descriptor
publisher.put(buf).await.unwrap();
```

### Subscriber Side: Receiving SHM Samples

The subscriber API is identical whether SHM or regular transport is used. Zenoh transparently provides a view into shared memory when SHM was used, or a copied buffer when it was not.

```rust
use zenoh::bytes::ZBytes;
use zenoh_shm::api::buffer::zshm::zshm;

let subscriber = session
    .declare_subscriber("sensor/data")
    .await
    .unwrap();

while let Ok(sample) = subscriber.recv_async().await {
    let payload = sample.payload();
    
    // Option 1: treat payload as bytes regardless of transport
    let bytes: Vec<u8> = payload.to_bytes().into_owned();
    
    // Option 2: attempt zero-copy SHM access (Rust API)
    // The sample's payload internally holds a ZShm reference when SHM was used
    println!("Received {} bytes", payload.len());
}
```

#### Checking if a Sample Arrived via SHM

In Rust, you can inspect the underlying buffer type by attempting to extract the SHM reference:

```rust
// zenoh's ZBytes internally wraps ZSlice which may hold a ZShm
// Access is transparent; the Rust borrow checker enforces lifetime safety
let payload = sample.payload();
// payload.as_shm() returns Option<&zshm> when the feature is enabled
if let Some(shm_buf) = payload.as_shm() {
    println!("Zero-copy SHM buffer, len={}", shm_buf.len());
} else {
    println!("Regular (copied) buffer");
}
```

### Buffer Types Reference

| Type | Description | Mutability |
|---|---|---|
| `ZShmMut` | Owned, mutable SHM buffer | Read + Write |
| `ZShm` | Owned, immutable SHM buffer | Read only |
| `zshmmut` | Borrowed, mutable SHM buffer (DST) | Read + Write |
| `zshm` | Borrowed, immutable SHM buffer (DST) | Read only |
| `Typed<T, Buf>` | Typed wrapper over any of the above | Depends on `Buf` |

**Conversion rules:**

```rust
// Mutable → immutable (always succeeds)
let immut: ZShm = mutable_buf.into();

// Immutable → mutable (succeeds only if unique reference and valid)
let mutable: Result<ZShmMut, ZShm> = immut.try_into();

// Resize an owned buffer (within the allocated chunk size)
buf.try_resize(NonZeroUsize::new(512).unwrap());
```

### Allocation Policies

| Policy | Description | Safe? |
|---|---|---|
| `JustAlloc` | Single attempt; returns error immediately | ✅ |
| `GarbageCollect` | Collect freed buffers and retry | ✅ |
| `Defragment` | Defragment memory and retry | ✅ |
| `BlockOn` | Block/await until memory available | ✅ |
| `Deallocate<N>` | Force-free up to N buffers | ⚠️ Unsafe |

Policies compose:

```rust
use zenoh_shm::api::provider::shm_provider::{
    Defragment, GarbageCollect, BlockOn, JustAlloc,
};

// Try → GC → Defragment → Block
type MyPolicy = BlockOn<GarbageCollect<Defragment>>;

let buf = provider
    .alloc(4096usize)
    .with_policy::<MyPolicy>()
    .wait()
    .unwrap();
```

### ShmClientStorage Configuration

The subscriber side uses `ShmClientStorage` to know which SHM protocols it can handle. The global default includes the POSIX protocol:

```rust
use zenoh_shm::api::client_storage::{ShmClientStorage, GLOBAL_CLIENT_STORAGE};
use std::sync::Arc;

// Use the global default (POSIX protocol pre-registered)
let storage = GLOBAL_CLIENT_STORAGE.read().clone();

// Or build a custom storage
let custom_storage = ShmClientStorage::builder()
    .with_default_client_set()    // adds POSIX client
    // .with_client(my_custom_client)  // add custom protocol
    .build();

// Pass to session builder
let session = zenoh::open(config)
    .with_shm_client_storage(Arc::new(custom_storage))
    .await
    .unwrap();
```

---

## Automatic vs Explicit SHM

### Automatic SHM

When SHM is enabled in the transport configuration and both endpoints are on the same host with matching protocol support, Zenoh uses SHM **automatically and transparently**:

- The publisher simply publishes any `ZShmMut` buffer; Zenoh decides whether to transmit via SHM descriptor or fall back to network copy
- The subscriber receives data identically regardless of transport
- No application code changes are needed to benefit from SHM

**Fallback behavior**: If SHM negotiation succeeds but the subscriber later cannot attach to a segment (e.g., permissions issue), Zenoh falls back to sending a serialized copy.

### Explicit SHM

For maximum control, applications explicitly:

1. Create and manage `ShmProvider` instances with specific segment sizes
2. Allocate `ZShmMut` buffers from the provider with specific policies
3. Write data into those buffers and publish them directly
4. Optionally inspect received samples to confirm SHM delivery

Explicit SHM is recommended when:

- You need to pre-allocate memory pools to avoid runtime allocation failures
- You need to control memory layout or alignment for SIMD/DMA operations
- You want to implement custom SHM protocols (`ShmProviderBackend` + `ShmClient` pair)

---

## SHM Cleanup

### The Problem: POSIX Persistence

POSIX named shared memory segments are **persistent** — they survive beyond the lifetime of the process that created them, stored under `/dev/shm/` on Linux. If a Zenoh publisher crashes (SIGKILL, OOM kill, power loss), its shared memory segments remain in the OS until:

- Another process explicitly calls `shm_unlink()` on them, or
- The system is rebooted

Without cleanup, crashed processes leave "orphaned" segments that waste memory and may eventually exhaust the system's SHM quota.

### Zenoh's Cleanup Strategy

Zenoh implements a multi-layered cleanup approach:

#### 1. Normal Exit Cleanup (RAII)

The global `CLEANUP` object (initialized via `static_init::dynamic`) is an RAII guard. On normal process exit (return from `main`, `exit()` call), its `Drop` implementation:

1. Calls `cleanup_orphaned_segments()` to remove segments from crashed processes
2. Calls `Segment::ensure_not_persistent()` on all segments registered to the current process

This means **normal exits always clean up cleanly**.

#### 2. Orphan Detection on Startup

Every time a Zenoh process creates its first SHM segment, the cleanup subsystem runs `cleanup_orphaned_segments()`. This:

- Enumerates all Zenoh-related segments currently in `/dev/shm/` (Linux)
- For each segment, checks whether any live process holds it open
- Removes segments that have no live owners

This means **orphaned segments from previous crashes are cleaned up by the next Zenoh process to start**.

#### 3. Manual Cleanup

You can trigger orphan cleanup at any time:

```rust
use zenoh_shm::api::cleanup::cleanup_orphaned_shm_segments;

// Trigger orphan cleanup manually
// Safe to call anytime; may be expensive on systems with many SHM segments
cleanup_orphaned_shm_segments();
```

#### 4. Platform Notes

| Platform | Orphan Detection | Automatic Cleanup |
|---|---|---|
| **Linux** | ✅ Full (enumerates `/dev/shm`) | ✅ Yes |
| **macOS / BSD** | ⚠️ Advisory lock variant | ⚠️ Partial |
| **Windows** | N/A (OS auto-cleans) | ✅ Yes (by OS) |

On Linux, Zenoh uses advisory file locks to associate segment ownership with process liveness. The `shm_external_lockfile` cfg alias selects an external lockfile approach for BSD targets where advisory locking on `tmpfs` is not supported.

#### 5. Watchdog and Reference Counting

Beyond segment cleanup, Zenoh maintains a **watchdog** system per SHM buffer:

- Each `ZShmMut` buffer has a reference count in a metadata section
- A `GLOBAL_CONFIRMATOR` thread periodically confirms that live providers still hold their buffers
- A `GLOBAL_VALIDATOR` thread on the subscriber side validates that descriptors it has received still point to live data
- If the provider crashes without releasing a buffer, the watchdog detects this via `watchdog_invalidated` flag and the buffer is marked invalid on the subscriber side

This prevents subscribers from reading stale data from segments whose provider has crashed.

---

## Performance

### When SHM is Faster

SHM provides the most benefit when:

| Scenario | Speedup Potential |
|---|---|
| Large messages (> 64 KB) | Very high — copy dominates without SHM |
| High-frequency small messages | Moderate — descriptor overhead matters |
| NUMA-aware workloads | High — data stays in local NUMA node |
| Real-time systems needing bounded latency | High — eliminates variable copy latency |

### Overhead of SHM

SHM is not free. The overhead includes:

- **Provider construction**: One-time `shm_open` + `ftruncate` + `mmap` — O(1), done at startup
- **Allocation**: Allocator-dependent; Talc and Buddy are O(log n); Binary Heap is O(log n)
- **Descriptor transmission**: A small fixed-size descriptor (~24 bytes: protocol ID 4B + segment ID 4B + chunk offset 4B + length 8B + metadata descriptor) travels over the normal Zenoh transport
- **Segment attachment**: First delivery to a subscriber from a new segment triggers `shm_open` + `mmap` — this is a one-time cost per segment per subscriber process
- **Reference count updates**: Atomic operations on shared metadata per send/receive
- **Watchdog confirmations**: Periodic atomic writes in a background thread

For very small messages (< 1 KB), the descriptor overhead and allocation overhead may exceed the copy cost. Benchmark for your specific message size.

### Latency Profile

```
Without SHM (same host, loopback):
  serialize → copy to network buffer → loopback → copy from network buffer → deserialize
  Latency contribution: 2× memcpy of full message

With SHM (same host):
  write to SHM buffer → send 24-byte descriptor → attach segment (first time) → pointer to reader
  Latency contribution: 1× write (unavoidable) + descriptor send (tiny)
```

### Benchmarking Tips

- Use `provider.available()` to monitor free memory pressure
- Use `GarbageCollect` policy to reclaim buffers from slow subscribers before blocking
- Use precomputed layouts (`provider.alloc_layout()`) to eliminate per-allocation layout computation
- For maximum throughput, use the `BlockOn<GarbageCollect>` combined policy to avoid allocation failures

---

## Limitations

### Same-Host Only

This is the most important limitation. **SHM buffers are never transmitted over the network.** When a Zenoh session sends an SHM buffer to a remote subscriber (different machine), one of two things happens:

1. **Automatic fallback**: If the transport layer detects the subscriber cannot use SHM (different host, no SHM negotiated), it serializes the buffer contents and sends them as regular bytes. The subscriber receives a normal (copied) payload.
2. **Silent degradation**: If you rely on SHM for performance and do not check, you may be silently falling back to copies for remote subscribers without realizing it.

### No Cross-Host SHM

There is no "network SHM" or RDMA integration built into the standard Zenoh SHM stack. For cross-host zero-copy, you would need a custom `ShmProviderBackend` + `ShmClient` pair using a technology like:
- RDMA (InfiniBand, RoCE) with custom protocol ID
- Cross-host mmap over NFS/FUSE (not zero-copy in practice)

### Single Segment per Provider

Each `ShmProvider` instance manages exactly one POSIX shared memory segment. If the segment fills up:
- Allocation fails with `ZAllocError::OutOfMemory`
- `GarbageCollect` policy reclaims buffers held by no subscriber
- `Defragment` policy coalesces adjacent free chunks (for BinaryHeap backend)
- `BlockOn` policy waits for space to become available

Multiple providers can coexist, each with its own segment.

### Segment Size is Fixed at Creation

The segment size is specified at `ShmProvider` construction and cannot be changed at runtime. Plan segment sizes based on:
- Maximum message size × maximum concurrent in-flight buffers
- Add headroom for allocator metadata (typically < 1% overhead)

### No Windows `/dev/shm` Orphan Enumeration

On Windows, OS-level named objects are automatically cleaned up when all handles are closed. Orphan cleanup routines are defined but the Windows variant relies on OS-level cleanup rather than enumeration.

### Unstable API Warning

The `zenoh-shm` crate is marked as internal. All public items are annotated `#[zenoh_macros::unstable_doc]`. The API may change between versions, including patch versions. Applications should depend on the `zenoh` and `zenoh-ext` crates and use their stable SHM interfaces rather than using `zenoh-shm` directly.

---

## Language Binding Support

| Language | SHM Support | Notes |
|---|---|---|
| **Rust** | ✅ Full | Native; `zenoh-shm` crate; all provider/client APIs available |
| **C** | ✅ Full | `zenoh-c` bindings expose SHM provider and buffer APIs |
| **C++** | ✅ Full | `zenoh-cpp` wraps `zenoh-c`; SHM APIs available |
| **Python** | ⚠️ Partial | `zenoh-python`; SHM transparent receive; explicit provider API limited |
| **Kotlin/Java** | ⚠️ Partial | `zenoh-kotlin`/`zenoh-java`; transparent receive; explicit SHM API not exposed |
| **Swift** | ⚠️ Partial | `zenoh-swift`; SHM transparent; limited explicit API |
| **Go** | ⚠️ Partial | Community bindings; SHM transparency dependent on implementation |

> **Note**: "Transparent receive" means the subscriber can receive SHM buffers and Zenoh handles the attachment automatically. "Full" means the application can also create providers and explicitly allocate SHM buffers. Check the specific binding's release notes for the exact feature set, as SHM API coverage evolves independently in each binding.

---

## Code Examples

### Complete Rust SHM Publisher

```rust
//! SHM Publisher Example
//!
//! Publishes sensor data using shared memory for zero-copy delivery
//! to co-located subscribers.

use std::time::Duration;
use zenoh::Config;
use zenoh_core::Wait;
use zenoh_shm::api::provider::{
    shm_provider::{BlockOn, GarbageCollect, ShmProviderBuilder},
    types::AllocAlignment,
    memory_layout::MemoryLayout,
};

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    // ── 1. Configure Zenoh session with SHM enabled ──────────────────────────
    let mut config = Config::default();
    config
        .insert_json5("transport/unicast/shm/enabled", "true")
        .unwrap();

    let session = zenoh::open(config).await.unwrap();

    // ── 2. Create an SHM provider ─────────────────────────────────────────────
    //
    // 64 MB segment with 8-byte alignment (suitable for f64 arrays)
    let layout = MemoryLayout::new(
        64 * 1024 * 1024,
        AllocAlignment::ALIGN_8_BYTES,
    )
    .expect("Invalid layout");

    let provider = ShmProviderBuilder::default_backend(layout)
        .wait()
        .expect("Failed to create SHM provider");

    // ── 3. Pre-compute the allocation layout for 4096-byte messages ───────────
    //
    // This avoids re-computing layout on every allocation.
    let precomputed = provider
        .alloc_layout(4096usize)
        .expect("Failed to precompute layout");

    // ── 4. Declare a publisher ────────────────────────────────────────────────
    let publisher = session
        .declare_publisher("sensor/lidar/points")
        .await
        .unwrap();

    println!("SHM Publisher ready. Publishing to 'sensor/lidar/points'...");

    let mut sequence: u64 = 0;
    loop {