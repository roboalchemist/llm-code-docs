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

Zenoh Shared Memory (SHM) enables **zero-copy publish/subscribe communication between processes running on the same host**. Instead of serializing data and copying it through the network stack, SHM allows processes to share a common memory region, so a published buffer is accessed by the subscriber directly—without any data copy.

### What SHM Gives You

- **Zero-copy delivery** for large payloads between co-located processes
- **Reduced CPU usage** by eliminating serialization and memory-copy operations
- **Lower latency** for large messages compared to loopback network transport
- **Automatic fallback** to normal transport when SHM is not available or not negotiated
- **Typed buffer access** for safe interaction with structured data in shared memory
- **Pluggable backends** allowing custom memory allocation strategies

SHM is most impactful when messages are large (kilobytes to megabytes). For small messages, the overhead of SHM negotiation can exceed the benefit of zero-copy.

---

## How SHM Works

### Architecture

Zenoh SHM is built on top of POSIX named shared memory segments. The system has two sides:

**Provider side (publisher)**
- Owns and manages one or more SHM segments
- Allocates chunks within those segments using a configurable allocator backend
- Publishes a *descriptor* (not the data itself) over the Zenoh transport layer
- The descriptor contains: segment ID, chunk offset, length, protocol ID, and a watchdog reference

**Client side (subscriber)**
- Maintains a `ShmClientStorage` containing `ShmClient` instances, one per protocol
- Upon receiving a descriptor, calls the appropriate `ShmClient` to attach to the named segment
- Maps the chunk into its own address space and accesses data directly

```
┌─────────────────────────────────────────────────────────────┐
│                       Same Host                             │
│                                                             │
│  ┌──────────────────┐        ┌──────────────────────────┐  │
│  │    Publisher     │        │       Subscriber         │  │
│  │                  │        │                          │  │
│  │  ShmProvider     │        │  ShmClientStorage        │  │
│  │  ┌────────────┐  │        │  ┌────────────────────┐  │  │
│  │  │ Segment N  │  │        │  │ PosixShmClient     │  │  │
│  │  │ [data...]  │◄─┼────────┼──┤ attach(segment_id) │  │  │
│  │  └────────────┘  │        │  └────────────────────┘  │  │
│  │                  │        │                          │  │
│  │  publish(desc)──►│──wire──►  recv(desc) → map()     │  │
│  └──────────────────┘        └──────────────────────────┘  │
│                                                             │
│              POSIX Named Shared Memory                      │
└─────────────────────────────────────────────────────────────┘
```

### Provider/Subscriber Negotiation

When a publisher and subscriber are on the same host, Zenoh performs capability negotiation during session establishment. If both sides support the same SHM protocol (identified by a `ProtocolID`), the transport layer will attempt to use SHM delivery. The built-in POSIX protocol uses `POSIX_PROTOCOL_ID = 0`.

The protocol ID system allows for custom or third-party SHM implementations. A `ProtocolID` is a `u32`. It is the implementer's responsibility to ensure that incompatible `ShmClient` and `ShmProviderBackend` implementations never share the same `ProtocolID`.

### Automatic Fallback

If the subscriber does not have a matching `ShmClient` for the protocol used by the publisher, or if the segment cannot be attached (e.g., the publisher process has terminated), Zenoh automatically falls back to copying the data through the normal transport. This fallback is transparent to application code.

### Watchdog and Reference Counting

Each SHM buffer carries metadata including:
- A **reference count** tracking how many processes hold a reference
- A **watchdog** that allows the publisher to detect when all subscribers have released the buffer
- A **generation counter** to detect stale buffer reuse

The watchdog mechanism runs in background threads:
- A **confirmator** (publisher side) periodically confirms liveness of buffers it owns
- A **validator** (subscriber side) verifies that watchdog confirmations are still arriving

When the reference count drops to zero or watchdog validation fails, the buffer is eligible for garbage collection and the underlying chunk is returned to the provider's free list.

### Allocator Backends

Zenoh ships three allocator backends, all based on POSIX SHM segments:

| Backend | Type | Characteristics |
|---|---|---|
| `PosixShmProviderBackendTalc` | Default | General-purpose; excellent fragmentation resistance and memory efficiency |
| `PosixShmProviderBackendBuddy` | Buddy allocator | Fastest allocation speed; higher fragmentation |
| `PosixShmProviderBackendBinaryHeap` | Largest-fit | Legacy; no metadata in SHM segment; most resilient to corruption |

The default backend (`PosixShmProviderBackend`) is aliased to the Talc backend.

---

## Platform Support

### Operating Systems

| Platform | Status | Notes |
|---|---|---|
| Linux | ✅ Full support | POSIX SHM via `/dev/shm`; orphan cleanup fully implemented |
| macOS | ✅ Supported | BSD-family; uses external lockfile for segment locking (tmpfs advisory lock limitation) |
| Windows | ✅ Supported | Uses Windows named shared memory via `win-sys` / `winapi` |
| FreeBSD / DragonFly / NetBSD / OpenBSD | ✅ Supported | BSD-family; uses external lockfile |
| iOS / watchOS / tvOS / visionOS | ✅ Supported | Apple targets; uses external lockfile |

> **Note on orphan cleanup:** The cleanup routine that scans for and removes dangling SHM segments is fully implemented on Linux. On other platforms, `cleanup_orphaned_shm_segments()` currently does nothing. Manual cleanup may be required on non-Linux hosts after abnormal process termination.

### Language Bindings

| Language | SHM Support | Notes |
|---|---|---|
| Rust | ✅ Full | Native implementation; all features available |
| C | ✅ Full | Via `zenoh-c`; exposes SHM provider and buffer APIs |
| C++ | ✅ Full | Via `zenoh-cpp`; wraps the C bindings |
| Python | ⚠️ Partial | Via `zenoh-python`; SHM receive supported; publisher-side SHM may be limited |
| Java / Kotlin | ❌ Not supported | JVM boundary prevents direct SHM mapping |
| Go | ⚠️ Partial | Check `zenoh-go` release notes for current status |

---

## Requirements

For SHM to be active between two endpoints, all of the following must be true:

1. **Same host**: Both publisher and subscriber must be running on the same physical or virtual machine. SHM buffers are never transmitted over the network.

2. **Compatible SHM build**: Both processes must have been compiled with SHM support. In Rust, this is the `shared-memory` feature (enabled by default in `zenoh`). Check your build configuration.

3. **Matching protocol**: Both sides must support at least one common `ProtocolID`. The default POSIX protocol (`0`) is included automatically when SHM is enabled.

4. **Transport configuration**: SHM must be enabled in the transport configuration (see [Configuration](#configuration)).

5. **Sufficient OS resources**: The operating system must allow creation of named SHM segments of the requested size. On Linux, check `/proc/sys/kernel/shmmax` and available space in `/dev/shm`.

---

## Configuration

### Enabling SHM in Transport Configuration

SHM is controlled through the zenoh configuration file (JSON5 or YAML). The key section is under `transport.unicast`:

```json5
{
  "transport": {
    "unicast": {
      "lowlatency": false,
      "qos": {
        "enabled": true
      },
      "shm": {
        "enabled": true
      }
    }
  }
}
```

When `shm.enabled` is `true`, Zenoh will advertise SHM capability during session establishment and attempt SHM delivery for same-host peers.

### Programmatic Configuration (Rust)

```rust
use zenoh::Config;

let mut config = Config::default();
// Enable SHM transport
config
    .insert_json5("transport/unicast/shm/enabled", "true")
    .unwrap();
```

### SHM Provider Configuration

The SHM provider is configured entirely in application code, not in the transport configuration file. You choose the backend, segment size, and alignment when constructing the `ShmProvider`.

**Key configuration parameters:**

| Parameter | Type | Description |
|---|---|---|
| Segment size | `NonZeroUsize` / `usize` | Total bytes in the SHM segment |
| Alignment | `AllocAlignment` | Minimum allocation alignment (power of 2) |
| Backend | `ShmProviderBackend` impl | Allocator strategy |

### SHM Size and Layout

Memory layout in Zenoh SHM is represented by `MemoryLayout`, which pairs a size with an alignment:

```rust
use zenoh_shm::api::provider::{
    memory_layout::MemoryLayout,
    types::AllocAlignment,
};

// 64 MB segment with 4-byte alignment
let layout = MemoryLayout::new(
    64 * 1024 * 1024,         // size in bytes
    AllocAlignment::new(2)?,  // 2^2 = 4-byte alignment
)?;
```

Alignment is expressed as a power of 2:

| `AllocAlignment::new(n)` | Alignment |
|---|---|
| `0` | 1 byte |
| `1` | 2 bytes |
| `2` | 4 bytes |
| `3` | 8 bytes |
| `n` | 2ⁿ bytes |

Convenience constants are also available: `AllocAlignment::ALIGN_1_BYTE`, `ALIGN_2_BYTES`, `ALIGN_4_BYTES`, `ALIGN_8_BYTES`.

For typed allocations, you can derive the layout from a Rust type at compile time:

```rust
use zenoh_shm::api::provider::memory_layout::MemoryLayout;

#[repr(C)]
struct SensorData {
    timestamp: u64,
    value: f64,
    flags: u32,
}

// Layout is derived from the type's size and alignment
let layout = MemoryLayout::for_type::<SensorData>();
```

---

## API Reference

### ShmProvider: Allocating Buffers

`ShmProvider<Backend>` is the central object for creating SHM buffers on the publisher side. It owns the SHM segment and provides allocation methods.

#### Creating a Provider

```rust
use zenoh::Wait;
use zenoh_shm::api::provider::shm_provider::ShmProviderBuilder;

// Using the default backend (Talc)
let provider = ShmProviderBuilder::default_backend(64 * 1024 * 1024_usize)
    .wait()?;

// Using an explicit backend
use zenoh_shm::api::protocol_implementations::posix::{
    posix_shm_provider_backend::PosixShmProviderBackend,
};
let backend = PosixShmProviderBackend::builder(64 * 1024 * 1024_usize).wait()?;
let provider = ShmProviderBuilder::backend(backend).wait();
```

#### Allocating a Buffer

```rust
use zenoh::Wait;
use zenoh_shm::api::provider::shm_provider::JustAlloc;

// Simple allocation: 1024 bytes
let mut buf: ZShmMut = provider.alloc(1024_usize).wait()?;

// Write data into the SHM buffer
buf.as_mut().copy_from_slice(&my_data[..1024]);
```

#### Allocation Policies

Policies control what happens when the first allocation attempt fails:

| Policy | Behavior |
|---|---|
| `JustAlloc` | Single attempt; return error if allocation fails |
| `GarbageCollect` | Run GC on failure; retry if enough memory was reclaimed |
| `Defragment` | Defragment on failure; retry if large enough chunk was freed |
| `Deallocate` | Forcibly free up to N in-flight buffers (unsafe) |
| `BlockOn` | Block (sync or async) until memory becomes available |

```rust
use zenoh_shm::api::provider::shm_provider::{GarbageCollect, BlockOn};

// GC then retry
let buf = provider
    .alloc(1024_usize)
    .with_policy::<GarbageCollect>()
    .wait()?;

// Block until memory is available (async)
let buf = provider
    .alloc(1024_usize)
    .with_policy::<BlockOn>()
    .await?;
```

#### Typed Allocations

For structured data, use `TypedLayout` to get a type-safe buffer:

```rust
use zenoh_shm::api::provider::memory_layout::TypedLayout;
use zenoh_shm::api::buffer::typed::Typed;
use std::mem::MaybeUninit;

#[repr(C)]
struct SensorReading {
    timestamp: u64,
    value: f64,
}

// Allocate a typed buffer
let typed_buf: Typed<MaybeUninit<SensorReading>, ZShmMut> =
    provider.alloc(TypedLayout::<SensorReading>::new()).wait()?;

// Initialize the data
let mut typed_buf: Typed<SensorReading, ZShmMut> = typed_buf.initialize(SensorReading {
    timestamp: 1234567890,
    value: 3.14,
});
```

### Publishing with SHM Buffers

Once allocated and filled, an SHM buffer is published through the normal `Publisher` API. Zenoh automatically detects that it is an SHM buffer and delivers it via shared memory to eligible subscribers.

```rust
// Convert ZShmMut to immutable before publishing
let immutable_buf: ZShm = buf.into();
publisher.put(immutable_buf).await?;

// Or publish directly (ZShmMut is also accepted)
publisher.put(buf).await?;
```

### Receiving SHM Samples

On the subscriber side, samples arrive as normal `Sample` objects. When SHM delivery was used, the payload is backed by the shared memory buffer—no copy was made.

```rust
subscriber.recv_async().await?;
// Access the payload directly
let payload = sample.payload();
let data: &[u8] = &payload.to_bytes();
// data points into the SHM segment; no copy occurred
```

To explicitly check for and access the SHM buffer:

```rust
use zenoh_shm::api::buffer::zshm::ZShm;

if let Some(shm_buf) = sample.payload().as_shm() {
    let data: &[u8] = shm_buf.as_ref();
    println!("Received {} bytes via SHM", data.len());
}
```

### ShmClientStorage

The `ShmClientStorage` holds the set of `ShmClient` implementations a subscriber can use to attach to incoming SHM segments. This is registered with the session or runtime.

```rust
use std::sync::Arc;
use zenoh_shm::api::client_storage::{ShmClientStorage, GLOBAL_CLIENT_STORAGE};

// Default storage includes the POSIX client
let storage = Arc::new(
    ShmClientStorage::builder()
        .with_default_client_set()
        .build()
);

// Add custom clients alongside the default set
let storage = Arc::new(
    ShmClientStorage::builder()
        .with_default_client_set()
        .with_client(Arc::new(my_custom_client))?
        .build()
);
```

---

## Automatic vs Explicit SHM

### Automatic SHM

Zenoh selects SHM delivery automatically when all conditions are met:

- Both peers are on the same host
- Both have SHM enabled in transport config
- Both support a matching `ProtocolID`
- The publisher used an SHM-backed buffer (`ZShmMut` / `ZShm`)

If any condition fails, Zenoh falls back to standard transport transparently. No application code change is needed to trigger fallback.

### When Zenoh Chooses SHM Automatically

```
Publisher calls put(shm_buffer)
         │
         ▼
Transport layer checks each subscriber link
         │
    ┌────┴─────────────────────────────────────┐
    │ Same host AND SHM enabled AND            │
    │ matching ProtocolID?                     │
    └────┬─────────────────────────────────────┘
         │
    YES ─┼──► Send SHM descriptor over wire
         │    Subscriber maps segment directly (zero-copy)
         │
    NO  ─┼──► Serialize and copy buffer contents
              Send over normal transport
```

### Explicit SHM Control

You do not need to configure anything special in your application to receive via SHM—it happens automatically once the `ShmClientStorage` is registered with the session. On the publisher side, simply allocating and publishing an SHM buffer is sufficient.

If you want to **force** standard (non-SHM) delivery for a specific publication even when SHM is otherwise enabled, you can publish a regular byte buffer instead of an `ShmBuf`.

---

## SHM Cleanup

### Normal Lifecycle

When an SHM buffer is dropped, its reference count is decremented. When the count reaches zero:

1. The buffer's watchdog is invalidated
2. The next garbage collection pass reclaims the underlying chunk
3. The chunk is returned to the provider's free list for reuse

Garbage collection is triggered automatically by allocation policies (`GarbageCollect`) or can be called explicitly:

```rust
let reclaimed_bytes = provider.garbage_collect();
```

### What Happens on Crash

POSIX named shared memory segments are **persistent** in the OS until explicitly unlinked, even if all processes that created them have exited. This means a crashed publisher can leave orphaned segments consuming memory.

Zenoh addresses this through:

1. **RAII cleanup objects**: On normal exit (return from `main()` or `exit()` call), Zenoh's internal `CLEANUP` object is dropped, which unlinks all segments it owns.

2. **Orphan segment cleanup**: On first SHM segment creation and on normal process exit, Zenoh runs `cleanup_orphaned_segments()`, which:
   - Enumerates all known Zenoh SHM segments in the system
   - Checks whether any live process is still using each segment
   - Removes segments with no active users

3. **Manual trigger**: You can trigger cleanup at any time from application code:

```rust
use zenoh_shm::api::cleanup::cleanup_orphaned_shm_segments;

// Trigger orphan cleanup manually (may be expensive)
cleanup_orphaned_shm_segments();
```

### Platform Notes on Cleanup

- **Linux**: Full orphan detection is implemented. Segments are listed from `/dev/shm`; process liveness is checked via `/proc`.
- **macOS and other BSD variants**: `cleanup_orphaned_shm_segments()` currently does nothing. Orphaned segments must be removed manually (e.g., `ipcs -m` and `ipcrm`).
- **Windows**: Named shared memory objects are automatically reclaimed by the OS when the last handle is closed, reducing the orphan problem.

### Advisory Locking

On BSD-derived platforms (macOS, FreeBSD, etc.), Zenoh uses an **external lockfile** for SHM segment locking because tmpfs (used for POSIX SHM on these systems) does not support advisory file locking. This is handled transparently by the `shm_external_lockfile` configuration alias in the build system.

---

## Performance

### When SHM Is Faster

SHM provides the most benefit when:

| Condition | Reason |
|---|---|
| **Large messages** (≥ ~4 KB) | Copy cost dominates; zero-copy saves significant time |
| **High message rate** | Per-message copy overhead accumulates |
| **CPU-bound publisher** | Eliminating serialization frees CPU cycles |
| **Memory-bandwidth-limited workloads** | Zero-copy halves memory bus traffic for the payload |

For small messages (< ~1 KB), the fixed overhead of SHM negotiation, watchdog management, and descriptor transmission may exceed the cost of a simple `memcpy`. In those cases, standard transport may be as fast or faster.

### Overhead Components

| Component | Cost | Notes |
|---|---|---|
| Session negotiation | One-time, at connection | Advertise and match `ProtocolID` lists |
| Segment attachment (`attach`) | Per new segment, amortized | Map segment into subscriber address space |
| Chunk allocation | Per publication | Depends on allocator backend (Talc ≈ fast) |
| Descriptor transmission | Per publication | Small fixed-size message over wire transport |
| Watchdog confirmator | Background thread | Periodic heartbeat; negligible per-message cost |
| Reference counting | Per send/receive | Atomic increment/decrement |
| Garbage collection | Amortized | Triggered by policy or explicit call |

### Allocator Performance Characteristics

| Backend | Allocation Speed | Fragmentation Resistance | Metadata in SHM |
|---|---|---|---|
| Talc (default) | Fast | Excellent | Yes |
| Buddy | Fastest | Poor (power-of-2 rounding) | Yes |
| BinaryHeap | Slowest (O(n) defrag) | Good | No |

The BinaryHeap backend's lack of in-SHM metadata makes it useful in scenarios where the subscriber's memory cannot be fully trusted (e.g., sandboxed environments), since memory corruption at the receiver cannot corrupt the allocator's free list.

### Precomputed Layouts

For workloads that allocate many buffers of the same size, use `PrecomputedLayout` to avoid repeated layout calculation:

```rust
// Compute layout once
let layout = provider.alloc_layout(1024_usize)?;

// Allocate many buffers cheaply
for _ in 0..1000 {
    let buf = layout.alloc().wait()?;
    // ...
}
```

---

## Limitations

1. **Same host only**: SHM buffers cannot be transmitted over the network. If a zenoh router forwards a message to a remote peer, the payload is automatically serialized and sent as a normal network message. The SHM optimization applies only to the local delivery leg.

2. **No SHM across containers with separate IPC namespaces**: Containers running with `--ipc=private` (the Docker default) do not share a POSIX SHM namespace, so SHM will not work between them. Use `--ipc=host` or a shared IPC namespace.

3. **Fixed segment size**: Once an SHM segment is created, its size is fixed. If your workload requires more memory than the segment provides, you must create a larger segment or use multiple segments.

4. **Alignment constraints**: Individual allocations must respect the alignment configured for the backend. Allocations that require finer alignment than the backend supports will fail with `ZLayoutError`.

5. **No cross-architecture support**: SHM shares raw memory between processes. Both publisher and subscriber must use the same data representation (endianness, struct layout). Mixed-architecture SHM is not supported.

6. **Fragmentation**: Long-running providers that allocate and free many variably-sized buffers may fragment. Use the `Defragment` policy or the Talc backend (which has better fragmentation resistance) for such workloads.

7. **Segment persistence on crash (non-Linux)**: On platforms other than Linux, orphaned segments are not automatically reclaimed. See [SHM Cleanup](#shm-cleanup).

8. **Unstable API**: The `zenoh-shm` crate is marked as an internal crate. Its API is not guaranteed stable across patch versions. Applications should consume SHM through the public `zenoh` and `zenoh-ext` crate APIs.

---

## Language Binding Support

### Detailed Support Matrix

| Feature | Rust | C | C++ | Python | Go |
|---|---|---|---|---|---|
| SHM transport (receive) | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| SHM transport (publish) | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Custom ShmProvider backend | ✅ | ✅ | ✅ | ❌ | ❌ |
| Custom ShmClient | ✅ | ✅ | ✅ | ❌ | ❌ |
| Typed SHM buffers | ✅ | ❌ | ❌ | ❌ | ❌ |
| Async allocation policies | ✅ | ❌ | ❌ | ❌ | ❌ |
| Manual orphan cleanup | ✅ | ✅ | ✅ | ✅ | ⚠️ |

> ⚠️ = check language binding release notes for current status; feature may be partially implemented or in progress.

---

## Code Examples

### Complete Rust SHM Publisher

```rust
//! SHM Publisher example
//!
//! Allocates an SHM buffer, writes data, and publishes it.
//! Subscribers on the same host receive the data with zero-copy.

use std::time::Duration;
use zenoh::{Config, Wait};
use zenoh_shm::api::{
    client_storage::GLOBAL_CLIENT_STORAGE,
    provider::shm_provider::{GarbageCollect, ShmProviderBuilder},
};

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    // --- 1. Configure zenoh with SHM transport enabled ---
    let mut config = Config::default();
    config
        .insert_json5("transport/unicast/shm/enabled", "true")
        .unwrap();

    // --- 2. Open a zenoh session ---
    let session = zenoh::open(config).await?;

    // --- 3. Create an SHM provider with a 64 MB segment ---
    //        Default backend (Talc) is used automatically.
    let shm_provider = ShmProviderBuilder::default_backend(64 * 1024 * 1024_usize)
        .wait()
        .expect("Failed to create SHM provider");

    // --- 4. Declare a publisher ---
    let publisher = session
        .declare_publisher("shm/example/data")
        .await?;

    let mut sequence: u64 = 0;
    loop {
        // --- 5. Allocate an SHM buffer ---
        //        Use GarbageCollect policy to reclaim buffers if memory is tight.
        let mut shm_buf = shm_provider
            .alloc(1024_usize)
            .with_policy::<GarbageCollect>()
            .wait()
            .expect("SHM allocation failed");

        // --- 6. Write data into the SHM buffer ---
        let payload_bytes = shm_buf.as_mut();
        // Write a simple sequence number at the start
        payload_bytes[..8].copy_from_slice(&sequence.to_le_bytes());
        // Fill the rest with a pattern
        for (i, b) in payload_bytes[8..].iter_mut().enumerate() {
            *b = (i & 0xFF) as u8;
        }

        // --- 7. Publish the SHM buffer ---
        //        Zenoh detects that this is an SHM buffer and sends only the
        //        descriptor to co-located subscribers. Remote subscribers (if any)
        //        receive the data as a normal serialized copy.
        publisher.put(shm_buf).await?;

        println!("Published sequence {sequence} via SHM (1024 bytes)");
        sequence += 1;

        tokio::time::sleep(Duration::from_millis(100)).await;
    }
}
```

### Complete Rust SHM Subscriber

```rust
//! SHM Subscriber example
//!
//! Receives samples that may be backed by shared memory.
//! When SHM delivery is used, no data copy occurs.

use zenoh::Config;

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    // --- 1. Configure zenoh with SHM transport enabled ---
    let mut config = Config::default();
    config
        .insert_json5("transport/unicast/shm/enabled", "true")
        .unwrap();

    // --- 2. Open a zenoh session ---
    //        The session automatically registers the global ShmClientStorage,
    //        which includes the default POSIX SHM client.
    let session = zenoh::open(config).await?;

    // --- 3. Declare a subscriber ---
    let subscriber = session
        .declare_subscriber("shm/example/data")
        .await?;

    println!("Waiting for SHM samples on 'shm/example/data'...");

    loop {
        // --- 4. Receive a sample ---
        let sample = subscriber.recv_async().await?;

        // --- 5. Access the payload ---
        //        If SHM delivery was used, this is a zero-copy view into the
        //        shared memory segment. If fallback transport was used, it is
        //        a regular heap buffer. The application code is identical either way.
        let payload = sample.payload();
        let data = payload.to_bytes();

        // Read the sequence number written by the publisher
        if data.len() >= 8 {
            let seq = u64::from_le_bytes(data[..8].try_into().unwrap());
            println!(
                "Received sample on '{}': seq={}, {} bytes",
                sample.key_expr(),
                seq,
                data.len()
            );
        }

        // --- 6. Optionally detect SHM delivery ---
        //        This check is informational only; application logic should not
        //        depend on whether SHM or fallback transport was used.
        #[cfg(feature = "shared-memory")]
        if let Some(shm) = payload.as_shm() {
            println!(
                "  -> Delivered via SHM (zero-copy), buffer valid={}",
                shm.is_valid()
            );
        }
    }
}
```

### Typed SHM Buffer Example (Rust)

```rust
//! Typed SHM example: zero-copy sharing of a structured type.

use zenoh::Wait;
use zenoh_shm::api::provider::{
    memory_layout::TypedLayout,
    shm_provider::ShmProviderBuilder,
};

#[repr(C)]
#[derive(Debug, Clone, Copy)]
struct SensorReading {
    timestamp_ns: u64,
    temperature:  f32,
    pressure:     f32,
    flags:        u32,
}

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(zenoh::Config::default()).await?;
    let publisher = session.declare_publisher("sensors/env").await?;

    let shm_provider = ShmProviderBuilder::default_backend(1024 * 1024_usize)
        .wait()
        .expect("SHM provider creation failed");

    // Allocate a typed buffer sized and aligned for SensorReading
    // The buffer starts as MaybeUninit<SensorReading>
    let uninit_buf = shm_provider
        .all