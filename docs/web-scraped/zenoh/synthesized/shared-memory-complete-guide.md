# Zenoh Shared Memory (SHM) — Complete Guide

Zenoh Shared Memory (SHM) provides zero-copy data transfer between processes on the same host while preserving the standard `ZBytes` interface. A publisher allocates a buffer in a named POSIX shared memory segment; a subscriber on the same host maps that segment and reads the data directly — no copy across a socket. Subscribers on different hosts receive a transparently serialized copy over the network, with no changes required in application code.

---

## Table of Contents

- [Contents](#contents)
- [POSIX Named SHM Internals](#posix-named-shm-internals)
  - [Segment Creation](#segment-creation)
  - [How the Receiver Attaches](#how-the-receiver-attaches)
  - [Advisory Locking](#advisory-locking)
  - [Virtual Memory Notes](#virtual-memory-notes)
- [Buffer Layout and Metadata](#buffer-layout-and-metadata)
  - [Metadata Segment Layout (`Metadata<S>`)](#metadata-segment-layout-metadatas)
  - [ChunkHeaderType Fields](#chunkheadertype-fields)
  - [Data Segment Layout](#data-segment-layout)
- [What Travels on the Wire](#what-travels-on-the-wire)
- [Session Negotiation](#session-negotiation)
  - [How Zenoh Decides SHM vs. Network](#how-zenoh-decides-shm-vs-network)
- [Automatic Fallback](#automatic-fallback)
  - [Verifying SHM Is Active](#verifying-shm-is-active)
- [Cleanup and Garbage Collection](#cleanup-and-garbage-collection)
  - [POSIX Semantics](#posix-semantics)
  - [Two Cleanup Mechanisms](#two-cleanup-mechanisms)
  - [Manual Cleanup](#manual-cleanup)
  - [Removing Dangling Segments Manually](#removing-dangling-segments-manually)
- [Watchdog and Lost-Buffer Recovery](#watchdog-and-lost-buffer-recovery)
  - [How It Works](#how-it-works)
- [Configuration Reference](#configuration-reference)
  - [`transport.shared_memory.enabled`](#transportshared_memoryenabled)
  - [`transport.shared_memory.mode`](#transportshared_memorymode)
  - [`transport.shared_memory.transport_optimization.enabled`](#transportshared_memorytransport_optimizationenabled)
  - [`transport.shared_memory.transport_optimization.pool_size`](#transportshared_memorytransport_optimizationpool_size)
  - [`transport.shared_memory.transport_optimization.message_size_threshold`](#transportshared_memorytransport_optimizationmessage_size_threshold)
  - [Complete Config Block](#complete-config-block)
- [Allocation Policies](#allocation-policies)
  - [Available Policies](#available-policies)
  - [Rust Examples](#rust-examples)
  - [Python Examples](#python-examples)
  - [Best Practices](#best-practices)
- [API Usage by Language](#api-usage-by-language)
  - [Rust — Full SHM API](#rust-full-shm-api)
  - [Python — Full SHM API](#python-full-shm-api)
  - [C (zenoh-c) — Full SHM API](#c-zenoh-c-full-shm-api)
- [Transport Optimization (Implicit SHM)](#transport-optimization-implicit-shm)
- [Language Binding Support](#language-binding-support)
  - [zenoh-pico Has No SHM](#zenoh-pico-has-no-shm)
- [Platform Differences](#platform-differences)
  - [Linux](#linux)
  - [macOS](#macos)
  - [Windows](#windows)
  - [BSD (FreeBSD, OpenBSD)](#bsd-freebsd-openbsd)
- [Performance Characteristics](#performance-characteristics)
  - [Latency](#latency)
  - [Throughput (Zero-Copy)](#throughput-zero-copy)
  - [Break-Even Point](#break-even-point)
  - [GC Jitter](#gc-jitter)
- [Docker](#docker)
- [Compilation Flags](#compilation-flags)
  - [Rust](#rust)
  - [Python](#python)
  - [C / C++](#c-c)
- [Troubleshooting](#troubleshooting)
  - [SHM Is Not Being Used (Falling Back to Network)](#shm-is-not-being-used-falling-back-to-network)
  - [Dangling Segments After Crash](#dangling-segments-after-crash)
  - [`mlock` Permission Denied](#mlock-permission-denied)
  - [SHM Pool Exhausted (OOM errors)](#shm-pool-exhausted-oom-errors)
  - [Watchdog Invalidations (Unexpected Buffer Loss)](#watchdog-invalidations-unexpected-buffer-loss)
  - [Inspecting SHM Usage at Runtime](#inspecting-shm-usage-at-runtime)

## Contents

1. [POSIX Named SHM Internals](#posix-named-shm-internals)
2. [Buffer Layout and Metadata](#buffer-layout-and-metadata)
3. [What Travels on the Wire](#what-travels-on-the-wire)
4. [Session Negotiation](#session-negotiation)
5. [Automatic Fallback](#automatic-fallback)
6. [Cleanup and Garbage Collection](#cleanup-and-garbage-collection)
7. [Watchdog and Lost-Buffer Recovery](#watchdog-and-lost-buffer-recovery)
8. [Configuration Reference](#configuration-reference)
9. [Allocation Policies](#allocation-policies)
10. [API Usage by Language](#api-usage-by-language)
11. [Transport Optimization (Implicit SHM)](#transport-optimization-implicit-shm)
12. [Language Binding Support](#language-binding-support)
13. [Platform Differences](#platform-differences)
14. [Performance Characteristics](#performance-characteristics)
15. [Docker](#docker)
16. [Compilation Flags](#compilation-flags)
17. [Troubleshooting](#troubleshooting)

---

## POSIX Named SHM Internals

### Segment Creation

When a `PosixShmProviderBackend` (or any POSIX-backed `ShmProvider`) is created, Zenoh allocates one named POSIX shared memory segment using `shm_open` + `ftruncate` + `mmap`:

```
shm_open("/{random_u64}.zenoh", O_CREAT | O_EXCL | O_RDWR, S_IRUSR | S_IWUSR)
ftruncate(fd, requested_size)
mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_NORESERVE, fd, 0)
mlock(ptr, size)   # pin pages — no swap
```

The segment name is `/{random_u64}.zenoh`. The random 64-bit ID is generated with `rand::thread_rng().gen::<u64>()` and retried up to 100 times if a collision occurs. On Linux these segments appear under `/dev/shm/` as files named `{id}.zenoh`.

### How the Receiver Attaches

When a subscriber receives a buffer reference pointing to a segment it has not opened before, the `PosixShmClient` calls:

```rust
shm_open("{id}.zenoh", O_RDWR, ...)   // open the existing segment by name
mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_NORESERVE, fd, 0)
mlock(ptr, size)
```

From that point the subscriber can read/write the buffer via the same physical pages, without any copy.

### Advisory Locking

Every process that has a segment open holds a **shared** advisory file lock on the SHM file descriptor (Linux/macOS) or a separate lockfile in `temp_dir()` (BSD without tmpfs). When a segment is dropped, the lock is released. The cleanup code tries to acquire an **exclusive** advisory lock; if it succeeds, no other process holds the segment — it is safe to unlink.

### Virtual Memory Notes

- Pages are locked into RAM via `mlock`. Your system must have enough free RAM for all SHM pools.
- On Linux you may need to raise the memlock limit: `ulimit -l unlimited` (or a `/etc/security/limits.conf` entry).
- Segments use `MAP_NORESERVE`, which disables swap space reservation. Memory is pre-committed and page-faults are avoided after `mlock`.

---

## Buffer Layout and Metadata

Zenoh maintains a **separate** POSIX shared memory segment called the *metadata segment*. This segment holds chunk headers and watchdog atomics, separated from payload data.

### Metadata Segment Layout (`Metadata<S>`)

```
MetadataSegment (separate SHM segment):
┌────────────────────────────────────────────────────┐
│  headers: [ChunkHeaderType; S]                     │
│  watchdogs: [AtomicU64; S/64]  (1 bit per header)  │
└────────────────────────────────────────────────────┘
  default S = 32768 slots
```

### ChunkHeaderType Fields

```rust
pub struct ChunkHeaderType {
    pub refcount:            AtomicU32,   // reference count across all processes
    pub watchdog_invalidated: AtomicBool,  // set true if watchdog fires
    pub generation:          AtomicU32,   // incremented on reuse
    pub protocol:            AtomicU32,   // 0 = POSIX, user-defined for custom backends
    segment:                 AtomicU32,   // segment ID
    chunk:                   AtomicU32,   // byte offset index within segment
    len:                     AtomicUsize, // logical length of the buffer
}
```

### Data Segment Layout

The data segment is a flat byte array managed by the Talc allocator (a general-purpose heap allocator). There is no fixed per-buffer header inside the data region — the header lives in the separate metadata segment indexed by segment ID and chunk index.

```
Data Segment (PosixShmSegment):
┌──────────────────────────────────────────────────────┐
│  [raw bytes managed by Talc heap allocator]          │
│  ...alloc'd chunks at various offsets...             │
└──────────────────────────────────────────────────────┘
```

---

## What Travels on the Wire

An SHM buffer is transmitted as a **16-byte descriptor** message — not the data itself:

```
┌─────────────────────────────────────────────────┐
│  ShmBufInfo (16 bytes on the wire)              │
│  ├── MetadataDescriptor (segment_id, index)     │
│  └── Data ChunkDescriptor (segment_id, chunk,   │
│       len)                                      │
└─────────────────────────────────────────────────┘
```

The receiver maps the referenced segments into its address space and reads through that pointer. No data bytes cross the OS network stack between co-located processes.

---

## Session Negotiation

SHM support is negotiated at **session open time** as part of the Zenoh handshake:

1. Each side announces:
   - Whether it has the `shared-memory` feature compiled in and `enabled: true` in config
   - SHM protocol version
   - A list of SHM protocol IDs it can read (e.g., `[0]` for POSIX)

2. During the handshake, each side performs a **mutual SHM availability probe**: it attempts to open the peer's metadata SHM segment by name to confirm that both ends are on the same host and have filesystem access to the same SHM namespace.

3. If the probe succeeds, SHM is activated for that link. If it fails (different host, different Docker network, permissions issue), the link falls back to serialized network transport automatically.

### How Zenoh Decides SHM vs. Network

- **Same host, same SHM namespace** → probe succeeds → SHM active
- **Different host** → segment name not accessible → serialized copy over TCP/UDP
- **Same host, different Docker containers without shared `/dev/shm`** → probe fails → network fallback

There is no explicit "same host" detection; the capability check *is* the test. If the peer can map the segment, SHM works; otherwise it doesn't.

---

## Automatic Fallback

When the receiver cannot use SHM (negotiation failed, or the remote side does not have the `shared-memory` feature), Zenoh performs a **transparent copy at the SHM domain boundary**:

- The SHM `ZBytes` is deserialized into a regular heap `ZBytes` containing a copy of the payload.
- The copy is sent over the network link exactly as if the publisher had sent a regular `ZBytes` from the start.
- **Application code is unchanged.** The subscriber's `ZBytes` looks like any other bytes; it just happens to be a copy rather than a zero-copy reference.

### Verifying SHM Is Active

Enable debug logging to confirm SHM is being used:

```bash
RUST_LOG=zenoh=debug ./my_app
```

Look for lines like:
```
DEBUG zenoh::net::transport::unicast::establishment: SHM probing succeeded
DEBUG zenoh_shm::posix_shm::segment: Created SHM segment, len: 1048576, id: 12345678901234
DEBUG zenoh_shm::posix_shm::segment: Opened SHM segment, id: 12345678901234
```

On Linux you can also confirm segments exist while the process runs:
```bash
ls -la /dev/shm/*.zenoh
```

---

## Cleanup and Garbage Collection

### POSIX Semantics

Named POSIX SHM objects persist until explicitly unlinked with `shm_unlink`. The kernel will not remove them when processes exit. On Linux they appear as files in `/dev/shm/`.

### Two Cleanup Mechanisms

#### 1. Destructor-Based GC

When a `Segment` struct is dropped in Rust:
- `munmap(ptr, len)` is called to unmap the segment.
- The code attempts to acquire an **exclusive** advisory file lock.
- If the exclusive lock succeeds (no other process holds the segment), `shm_unlink("{id}.zenoh")` is called.
- The segment is removed from the cleanup registry.

This works reliably on orderly shutdown. It fails if a process is killed with SIGKILL, crashes, or calls `_exit()` without running destructors.

#### 2. Dangling-Segment GC

`cleanup_orphaned_segments()` is called at two points:

1. **On first SHM subsystem initialization** — when any Zenoh process first touches SHM.
2. **On orderly exit** — when the global `CLEANUP` static is dropped.

**Linux implementation** (in `posix_shm/cleanup.rs`):

```rust
fn cleanup_orphaned_segments_inner() -> ZResult<()> {
    for segment_file in fs::read_dir("/dev/shm")? {
        if file.extension() == Some("zenoh") {
            if let Ok(id) = file_stem.parse::<u64>() {
                Segment::ensure_not_persistent(id);
            }
        }
    }
}
```

`ensure_not_persistent` attempts an exclusive advisory lock. If it succeeds (no live holders), `shm_unlink` is called.

**macOS/BSD**: `cleanup_orphaned_segments` is a no-op (`fn cleanup_orphaned_segments() {}`). Lockfiles are in `temp_dir()` instead of the SHM namespace, so the scan is not performed automatically. Dangling segments on macOS are cleaned up on next startup of a Zenoh process only via destructor-based GC from that same process.

### Manual Cleanup

You can trigger cleanup explicitly:

```rust
// Rust: force GC on provider
shm_provider.garbage_collect();

// Or drop the provider to run destructor-based cleanup
drop(shm_provider);
```

### Removing Dangling Segments Manually

**Linux:**
```bash
# List all Zenoh SHM segments
ls /dev/shm/*.zenoh

# Check which are orphaned (no process has them open)
for f in /dev/shm/*.zenoh; do
    id=$(basename "$f" .zenoh)
    # fuser is non-zero exit if no process uses the file
    fuser "$f" 2>/dev/null || echo "ORPHAN: $f"
done

# Remove them
rm /dev/shm/*.zenoh
```

**`ipcs` command (System V SHM — not used by Zenoh):**
Zenoh uses POSIX named SHM, not System V `shmget`. The `ipcs -m` command shows System V segments only and will not show Zenoh's segments. Use `/dev/shm/*.zenoh` on Linux instead.

---

## Watchdog and Lost-Buffer Recovery

Zenoh uses a watchdog system to reclaim buffers whose references have been lost (e.g., a subscriber process crashed while holding a reference).

### How It Works

- The *Confirmator* runs in the buffer holder's process. Every 100 ms it sets a bit in the watchdog AtomicU64 for each buffer it holds.
- The *Validator* runs in the SHM provider's process. Every 100 ms it checks all watched buffers. If a buffer's watchdog bit is zero (not confirmed this cycle), it sets `watchdog_invalidated = true` in the chunk header and removes the buffer from the tracked set.
- Once `watchdog_invalidated` is true, the provider treats that chunk as reclaimable.

**Worst-case lost-buffer reclamation delay: 100 ms.**

```
Confirmator (subscriber process)     Validator (provider process)
│                                    │
│  every 100ms: set bit in watchdog  │  every 100ms: check bits
│  AtomicU64 for each held buffer    │  if bit == 0: invalidate header
│                                    │  if bit == 1: clear bit, retain
```

This design allows the provider to recover buffers even after catastrophic subscriber failure.

---

## Configuration Reference

All settings live under `transport.shared_memory` in `DEFAULT_CONFIG.json5`.

> SHM settings only take effect when zenoh is compiled with the `shared-memory` feature. Without it, these settings are silently ignored.

### `transport.shared_memory.enabled`

- **Type:** boolean
- **Default:** `true`
- **Description:** When `true`, SHM buffer support is announced to other parties during session handshake. This does not mandate SHM — both ends must announce SHM support for a link to use it. Set to `false` to completely disable SHM on this session.
- **Example:**
  ```json5
  shared_memory: { enabled: false }
  ```

### `transport.shared_memory.mode`

- **Type:** string, one of `"lazy"` or `"init"`
- **Default:** `"lazy"`
- **Description:**
  - `"lazy"` — The SHM subsystem (metadata segment, watchdog threads, cleanup routines) is initialized on first demand: either the first `alloc()` call or the first received SHM buffer. Provides faster startup and lower resource usage when SHM is rarely used. Incurs extra latency on the very first SHM interaction.
  - `"init"` — SHM subsystem is fully initialized at session open. Startup is slower but there is no latency spike on the first SHM buffer.
- **Example:**
  ```json5
  shared_memory: { mode: "init" }
  ```

### `transport.shared_memory.transport_optimization.enabled`

- **Type:** boolean
- **Default:** `true`
- **Description:** Enables the implicit transport optimization. When `true`, Zenoh automatically copies large non-SHM `ZBytes` payloads into a temporary SHM buffer before sending them over SHM-capable links. The receiver gets zero-copy access without the publisher explicitly using the SHM API.
- **Example:**
  ```json5
  transport_optimization: { enabled: false }
  ```

### `transport.shared_memory.transport_optimization.pool_size`

- **Type:** integer (bytes)
- **Default:** `16777216` (16 MiB)
- **Description:** Size of the internal SHM pool used exclusively for the implicit transport optimization. This pool is separate from any user-created `ShmProvider`. The pool is initialized lazily (lazy-opportunistic: created in a background task on first demand; not guaranteed to be available for every message).
- **Valid values:** Any positive integer. Practical range: 1 MiB–512 MiB.
- **Example:**
  ```json5
  transport_optimization: { pool_size: 67108864 }  // 64 MiB
  ```

### `transport.shared_memory.transport_optimization.message_size_threshold`

- **Type:** integer (bytes)
- **Default:** `3072` (3 KiB)
- **Description:** Messages strictly below this size are not candidates for implicit SHM optimization. Messages at or above this threshold are copied into the transport optimization SHM pool (if available) before forwarding to SHM-capable peers.
- **Valid values:** Any non-negative integer.
- **Example:**
  ```json5
  transport_optimization: { message_size_threshold: 65536 }  // 64 KiB
  ```

### Complete Config Block

```json5
transport: {
  shared_memory: {
    /// Enable/disable SHM transport announcement (default: true)
    enabled: true,

    /// Initialization mode: "lazy" (default) or "init"
    mode: "lazy",

    transport_optimization: {
      /// Enable implicit SHM optimization for large messages (default: true)
      enabled: true,

      /// Internal pool size in bytes (default: 16 MiB)
      pool_size: 16777216,

      /// Minimum message size to optimize, in bytes (default: 3 KiB)
      message_size_threshold: 3072,
    },
  },
},
```

---

## Allocation Policies

Allocation policies control how the `ShmProvider` behaves when memory is insufficient. Policies compose generically in Rust.

### Available Policies

| Policy | Sync/Async | Behavior |
|--------|-----------|---------|
| `JustAlloc` | sync | Allocate once, return error immediately if OOM. Default. |
| `GarbageCollect` | sync | If OOM, trigger GC (reclaim invalidated buffers) and retry. |
| `Defragment` | sync | If OOM due to fragmentation, defragment and retry. |
| `BlockOn` | sync + async | Block the caller until memory becomes available. |
| `Deallocate<N, Inner>` | sync | Force-deallocate up to N buffers, then retry with `Inner` policy. Unsafe. |

Policies chain from outer to inner: `BlockOn<Defragment<GarbageCollect>>` means "try to GC, then defragment, then block if still OOM."

### Rust Examples

```rust
use zenoh::shm::{JustAlloc, GarbageCollect, Defragment, BlockOn};

// Default: try once, error on OOM
let buf = provider.alloc(1024).wait()?;

// GC + retry
let buf = provider.alloc(1024)
    .with_policy::<GarbageCollect>()
    .wait()?;

// Defragment + GC + retry
let buf = provider.alloc(1024)
    .with_policy::<Defragment<GarbageCollect>>()
    .wait()?;

// Block until memory is available (async)
let buf = provider.alloc(1024)
    .with_policy::<BlockOn<GarbageCollect>>()
    .await?;

// Block until memory is available (sync)
let buf = provider.alloc(1024)
    .with_policy::<BlockOn>()
    .wait()?;
```

### Python Examples

```python
import zenoh.shm as shm

provider = shm.ShmProvider.default_backend(1024 * 1024)

# Just allocate (error if OOM)
buf = provider.alloc(1024)

# GC on OOM
buf = provider.alloc(1024, policy=shm.GarbageCollect())

# Block on OOM
buf = provider.alloc(1024, policy=shm.BlockOn())

# Block after GC
buf = provider.alloc(1024, policy=shm.BlockOn(shm.GarbageCollect()))
```

### Best Practices

- **Provider capacity**: set it to roughly **2× the sum of all in-flight payloads**. Too small → frequent OOM/GC jitter. Too large → poor cache utilization.
- **GC latency**: `GarbageCollect` triggers a scan of all tracked buffers. If many buffers are in flight, GC can take non-trivial time. For latency-sensitive paths, pre-allocate buffers or call `provider.garbage_collect()` explicitly in a low-priority background task.
- **Alignment**: use `AllocAlignment::ALIGN_8_BYTES` (the default) unless your payloads require specific SIMD alignment.
- **Reliability**: prefer `CongestionControl::Reliable` with reliable transport protocols to minimize lost-buffer events that trigger the 100 ms watchdog recovery delay.

---

## API Usage by Language

### Rust — Full SHM API

**Cargo.toml:**
```toml
zenoh = { version = "1.x", features = ["shared-memory", "unstable"] }
```

**Creating a Provider and Publishing:**

```rust
use zenoh::{
    shm::{BlockOn, GarbageCollect, ShmProviderBuilder},
    Config, Wait,
};

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    // Create SHM provider backed by 1 MiB POSIX segment
    let provider = ShmProviderBuilder::default_backend(1024 * 1024)
        .wait()?;

    let publisher = session.declare_publisher("demo/shm/example").await?;

    loop {
        // Allocate a mutable SHM buffer
        let mut buf = provider
            .alloc(256)
            .with_policy::<BlockOn<GarbageCollect>>()
            .await?;

        // Write data directly into shared memory
        buf[..13].copy_from_slice(b"hello via shm");

        // Put it — no copy for same-host subscribers
        publisher.put(buf).await?;
        tokio::time::sleep(std::time::Duration::from_secs(1)).await;
    }
}
```

**Subscribing (SHM-transparent):**

```rust
// The subscriber does NOT need to create a provider.
// It just receives ZBytes, which may be backed by SHM or regular memory.
let subscriber = session.declare_subscriber("demo/shm/example").await?;

while let Ok(sample) = subscriber.recv_async().await {
    // Works with both SHM and non-SHM payloads
    let text = sample.payload().try_to_string()?;
    println!("Received: {text}");
}
```

**Inspecting the buffer type (requires `unstable` feature):**

```rust
use zenoh::shm::zshmmut;

let mut sample = subscriber.recv_async().await?;
match sample.payload_mut().as_shm_mut() {
    Some(shm) => {
        let is_mutable = <&mut zshmmut>::try_from(shm).is_ok();
        println!("SHM buffer (mutable: {is_mutable})");
    }
    None => println!("Regular (non-SHM) buffer"),
}
```

**ZShm / ZShmMut buffer API:**

```rust
use zenoh::shm::{ZShm, ZShmMut, ShmProviderBuilder};

let provider = ShmProviderBuilder::default_backend(4096).wait().unwrap();

// Allocate mutable
let mut owned_mut: ZShmMut = provider.alloc(1024).wait().unwrap();
owned_mut[0..5].copy_from_slice(b"hello");

// Convert to immutable (reference counted, multi-clone)
let owned: ZShm = owned_mut.into();

// Convert back to mutable (fails if refcount > 1)
let owned_mut: ZShmMut = owned.try_into().unwrap();

// Wrap in ZBytes for sending
let payload: zenoh::bytes::ZBytes = owned_mut.into();
```

**Custom provider with explicit alignment:**

```rust
use zenoh::shm::{AllocAlignment, MemoryLayout, PosixShmProviderBackend, ShmProviderBuilder};

let layout = MemoryLayout::new(65536, AllocAlignment::ALIGN_8_BYTES).unwrap();
let backend = PosixShmProviderBackend::builder(&layout).wait()?;
let provider = ShmProviderBuilder::backend(backend).wait()?;
```

**Typed SHM allocation (Rust only):**

```rust
use std::sync::atomic::AtomicUsize;
use zenoh::shm::{ResideInShm, ShmProviderBuilder, TypedLayout, Typed, ZShmMut};
use std::mem::MaybeUninit;

#[repr(C)]
pub struct SharedData {
    pub counter: AtomicUsize,
    pub payload: [u8; 1024],
}

// Safety: SharedData is safe to share across processes via SHM
unsafe impl ResideInShm for SharedData {}

let provider = ShmProviderBuilder::default_backend(65536).wait()?;
let typed_buf: Typed<MaybeUninit<SharedData>, ZShmMut> =
    provider.alloc(TypedLayout::<SharedData>::new()).wait()?;
let raw_buf: ZShmMut = Typed::into_inner(typed_buf);
```

---

### Python — Full SHM API

Python exposes the SHM API through the `zenoh.shm` module. All SHM types are marked `@_unstable`.

**Installation note:** The Python package must be built with the `shared-memory` feature (the official PyPI wheels include it).

**Publishing via SHM:**

```python
import zenoh
import zenoh.shm as shm

with zenoh.open(zenoh.Config()) as session:
    # Create a 1 MiB SHM provider
    provider = shm.ShmProvider.default_backend(1024 * 1024)
    pub = session.declare_publisher("demo/shm/example")

    for i in range(100):
        # Allocate a mutable SHM buffer (bytes-like object)
        buf: shm.ZShmMut = provider.alloc(
            256,
            policy=shm.BlockOn(shm.GarbageCollect()),
        )
        msg = f"[{i:4d}] hello from python SHM".encode()
        buf[:len(msg)] = msg

        # Publish — zero-copy for same-host subscribers
        pub.put(buf)
```

**Subscribing (SHM-transparent):**

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("demo/shm/example")

    for sample in sub:
        # Works regardless of whether payload is SHM or regular
        print(f"Received: {bytes(sample.payload())}")
```

**Python SHM classes:**

| Class | Purpose |
|-------|---------|
| `shm.ShmProvider` | Allocator backed by a POSIX SHM segment |
| `shm.ZShmMut` | Mutable SHM buffer (bytes-like, supports `__setitem__`) |
| `shm.ZShm` | Immutable SHM buffer |
| `shm.MemoryLayout` | Describes size + alignment for allocation |
| `shm.AllocAlignment` | Alignment constant (`ALIGN_1_BYTE`..`ALIGN_8_BYTE`) |
| `shm.JustAlloc` | Default allocation policy |
| `shm.GarbageCollect` | GC policy |
| `shm.Defragment` | Defragment policy |
| `shm.BlockOn` | Block-on-OOM policy |

---

### C (zenoh-c) — Full SHM API

zenoh-c exposes the SHM API via a C interface. Compile with `-DZENOH_C_SHARED_MEMORY=ON`.

**Publishing via SHM:**

```c
#include "zenoh.h"

int main(void) {
    z_owned_config_t config;
    z_config_default(&config);

    z_owned_session_t s;
    z_open(&s, z_move(config), NULL);

    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, "demo/shm/example");
    z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL);

    // Create 4 KiB SHM provider
    z_owned_shm_provider_t provider;
    z_shm_provider_default_new(&provider, 4096);

    for (int i = 0; ; i++) {
        z_sleep_s(1);

        // Allocate SHM buffer with GC+defrag+block policy
        z_buf_layout_alloc_result_t alloc;
        z_shm_provider_alloc_gc_defrag_blocking(&alloc, z_loan(provider), 256);

        if (alloc.status == ZC_BUF_LAYOUT_ALLOC_STATUS_OK) {
            uint8_t* data = z_shm_mut_data_mut(z_loan_mut(alloc.buf));
            snprintf((char*)data, 256, "[%4d] hello from C SHM", i);

            // Wrap SHM buffer into ZBytes payload
            z_owned_bytes_t payload;
            z_bytes_from_shm_mut(&payload, z_move(alloc.buf));

            z_publisher_put_options_t opts;
            z_publisher_put_options_default(&opts);
            z_publisher_put(z_loan(pub), z_move(payload), &opts);
        }
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));
    z_drop(z_move(provider));
}
```

**Key C SHM functions:**

| Function | Description |
|----------|-------------|
| `z_shm_provider_default_new(provider, size)` | Create POSIX SHM provider |
| `z_shm_provider_alloc_gc_defrag_blocking(result, provider, size)` | Alloc with GC+defrag+block |
| `z_shm_mut_data_mut(buf)` | Get mutable pointer to SHM data |
| `z_bytes_from_shm_mut(bytes, buf)` | Wrap SHM buffer into ZBytes |
| `z_shm_mut_data(buf)` | Get const pointer to SHM data |

---

## Transport Optimization (Implicit SHM)

When the transport optimization is enabled (default), Zenoh automatically moves large non-SHM payloads into a temporary SHM buffer when sending to SHM-capable peers:

```
Publisher sends ZBytes (regular heap, size >= 3072 bytes)
    │
    ▼
Zenoh detects SHM-capable peer link
    │
    ▼
Copy payload into internal 16 MiB SHM pool (once per peer)
    │
    ▼
Send 16-byte SHM descriptor to peer
    │
    ▼
Peer reads via shared memory (zero-copy on receive)
```

**Key properties:**
- The conversion is **per peer** — if you have 3 SHM-capable subscribers, the payload is copied into SHM once per subscriber.
- The pool is initialized **lazily** in a background task. If the task hasn't completed yet, the message is sent as a regular network payload instead.
- The optimization is **not guaranteed** — if the 16 MiB pool is full, the message falls back to network copy.
- This is especially valuable for **routers and gateways** that receive large packets from the network and need to forward them to local co-located processes.

**To disable it** (when you want explicit control or need to save memory):
```json5
transport_optimization: { enabled: false }
```

---

## Language Binding Support

| Language | SHM Publish | SHM Receive (transparent) | Custom Backend | Notes |
|----------|-------------|---------------------------|----------------|-------|
| **Rust** | Full | Full | Full | `features = ["shared-memory", "unstable"]` for API |
| **Python** | Full | Full | No | `zenoh.shm` module; unstable API |
| **C** | Full | Full | Yes (C API) | Compile with `ZENOH_C_SHARED_MEMORY=ON` |
| **C++** | Full | Full | Yes | Via zenoh-c wrapper |
| **zenoh-pico** | **Not supported** | **Not supported** | No | MCU target: no POSIX, no virtual memory |

### zenoh-pico Has No SHM

zenoh-pico targets bare-metal microcontrollers and embedded systems. These platforms typically:
- Have no OS / no POSIX API
- Have no virtual memory or `mmap`
- Have no shared address spaces between processes (often single-process)
- Cannot accommodate the watchdog threads or metadata segments

zenoh-pico will receive SHM messages from full zenoh nodes as regular deserialized network buffers (the automatic fallback path). It cannot create or hold SHM references.

---

## Platform Differences

### Linux

- Full SHM support.
- Segments visible at `/dev/shm/{id}.zenoh`.
- `ipcs -m` shows **System V** shared memory only — not Zenoh's POSIX segments. Use `/dev/shm` directly.
- Orphaned segment scan is fully automatic (scans `/dev/shm` on startup/shutdown).
- `mlock` requires sufficient `ulimit -l` (memlock limit). Check: `ulimit -l`. Set unlimited: `ulimit -l unlimited`.
- Inspect open SHM segments: `lsof /dev/shm/*.zenoh`

### macOS

- Full POSIX SHM support, but `/dev/shm` does **not exist**.
- POSIX SHM is stored in kernel memory, not a filesystem path.
- Segments can be listed with: `ls /tmp/*.zenoh` (lockfiles only — the SHM objects themselves are not filesystem-visible on macOS).
- The orphaned-segment scan (`cleanup_orphaned_segments`) is a **no-op on macOS**. Only destructor-based cleanup runs.
- Docker on macOS: share `/tmp` between containers (lockfiles live there).
- `mlock` is supported on macOS but may require `sudo` or SIP adjustments.

### Windows

- Named shared memory uses the Windows API: `CreateFileMapping` / `MapViewOfFile` / `OpenFileMapping`.
- Segment name format is still `{id}.zenoh`.
- `VirtualLock` (equivalent of `mlock`) is currently **disabled** in the Windows implementation due to CI limitations; memory is not pinned on Windows.
- No automatic orphaned-segment scan (only destructor-based cleanup).
- Segments auto-close when all handles are closed — unlike POSIX, there is no persistent name to unlink.

### BSD (FreeBSD, OpenBSD)

- Uses `shm_external_lockfile` compile-time flag: separate lockfiles are created in `temp_dir()` (typically `/tmp`) because BSD POSIX SHM may not be on tmpfs.
- SHM object creation and `mmap` work identically to Linux.
- Orphaned-segment scan is a no-op (same as macOS).

---

## Performance Characteristics

### Latency

SHM eliminates serialization and socket round-trips for same-host communication. Typical comparisons (indicative, varies by hardware):

| Transport | Latency (single message, ~1KB) |
|-----------|-------------------------------|
| TCP loopback | ~30–100 µs |
| UNIX socket | ~10–30 µs |
| SHM (Zenoh) | ~1–5 µs |

The SHM wire message is 16 bytes, traveling via the normal Zenoh transport (TCP or UNIX socket) to trigger the receiver. The actual payload is read from the mapped segment without a syscall.

### Throughput (Zero-Copy)

For large payloads, "zero-copy" means:
- Publisher writes bytes into SHM once.
- Each same-host subscriber reads from the same physical pages — no per-subscriber copy.
- For N co-located subscribers: 1 write, 0 additional copies (versus N copies with TCP).

### Break-Even Point

The SHM path has fixed overhead: acquiring a buffer from the Talc allocator, setting up the metadata header, sending the 16-byte descriptor, and the subscriber mapping the segment on first access. For very small messages (< ~1 KB), this overhead can exceed the cost of a TCP socket write.

Practical rule:
- **< 1 KB**: TCP loopback is often comparable or faster than SHM.
- **1 KB – 64 KB**: SHM provides latency improvement.
- **> 64 KB**: SHM provides significant latency and throughput improvements; zero-copy effect is most pronounced.
- **The transport optimization threshold (3072 bytes default)** reflects this — below 3 KB, implicit SHM is not applied.

### GC Jitter

If the SHM pool runs low and `GarbageCollect` triggers, expect a latency spike of 0–5 ms depending on the number of in-flight buffers. Size the pool to 2× the maximum in-flight data to minimize GC frequency.

---

## Docker

Zenoh SHM is fully compatible with Docker.

**Linux containers (same host):**
```yaml
# docker-compose.yml
services:
  publisher:
    volumes:
      - /dev/shm:/dev/shm   # share POSIX SHM namespace
  subscriber:
    volumes:
      - /dev/shm:/dev/shm
```

**macOS Docker (uses Linux VM — share `/tmp` for lockfiles):**
```yaml
services:
  publisher:
    volumes:
      - /tmp:/tmp
  subscriber:
    volumes:
      - /tmp:/tmp
```

Both `/dev/shm` and `/tmp` must be shared between containers that need SHM connectivity.

---

## Compilation Flags

### Rust

```toml
# Cargo.toml — receiving SHM buffers only (no alloc API)
zenoh = { version = "1.x", features = ["shared-memory"] }

# Full SHM API including alloc, ZShmMut, custom backends
zenoh = { version = "1.x", features = ["shared-memory", "unstable"] }
```

- `shared-memory`: compile the SHM transport layer; required to receive SHM buffers without copy.
- `unstable`: unlocks the allocation API (`ShmProvider`, `ZShmMut`, `PosixShmProviderBackend`, etc.).

**Without `shared-memory`:** The session will always use network serialization. Peers that send SHM buffers will have them transparently copied before delivery to this session.

**With `shared-memory` but without `unstable`:** The session can receive SHM buffers without copy, but cannot allocate new ones. Buffer type introspection (`as_shm`, `as_shm_mut`) is unavailable.

### Python

The Python package must be built with the `shared-memory` feature. Official PyPI wheels for supported platforms include it. To check:

```python
import zenoh.shm
print(dir(zenoh.shm))   # should list ShmProvider, ZShmMut, etc.
```

### C / C++

Pass `-DZENOH_C_SHARED_MEMORY=ON` to CMake when building zenoh-c:

```bash
cmake -DZENOH_C_SHARED_MEMORY=ON ..
make
```

---

## Troubleshooting

### SHM Is Not Being Used (Falling Back to Network)

**Symptom:** Subscriber receives data but performance is no better than TCP; `RUST_LOG=zenoh=debug` shows no SHM segment opens.

**Diagnosis:**
1. Check that both publisher and subscriber have `shared_memory.enabled: true` (it is the default, but may be overridden by a config file).
2. Check that both are compiled with the `shared-memory` feature.
3. Check that the SHM probe succeeded in the logs:
   ```
   DEBUG zenoh::net::transport::unicast::establishment: SHM probing succeeded
   ```
   If absent or replaced by a failure line, the probe failed.
4. If in Docker: verify `/dev/shm` is shared between containers.
5. Verify both processes can access each other's SHM:
   ```bash
   # From subscriber container, can it see publisher's SHM files?
   ls /dev/shm/*.zenoh
   ```

### Dangling Segments After Crash

**Symptom:** `/dev/shm/*.zenoh` files accumulate; new processes complain about existing segments.

**Fix:**
```bash
# Linux: remove all Zenoh SHM segments
rm -f /dev/shm/*.zenoh

# Verify none remain
ls /dev/shm/*.zenoh 2>/dev/null && echo "Still present" || echo "Cleared"
```

The next Zenoh process to start will also run the automatic dangling-segment cleanup routine (Linux only), which will unlink any `.zenoh` files that have no live advisory lock holders.

### `mlock` Permission Denied

**Symptom:** Zenoh startup fails with an OS error during SHM initialization, or SHM silently falls back.

**Fix (Linux):**
```bash
# Check current limit
ulimit -l

# Set unlimited for current session
ulimit -l unlimited

# Permanent: add to /etc/security/limits.conf
# * soft memlock unlimited
# * hard memlock unlimited
```

### SHM Pool Exhausted (OOM errors)

**Symptom:** `alloc()` returns errors; `JustAlloc` policy fails frequently.

**Fix options:**
1. **Increase pool size**: `ShmProviderBuilder::default_backend(4 * 1024 * 1024)` (4 MiB instead of the default you passed).
2. **Use GC policy**: `.with_policy::<GarbageCollect>()` to reclaim invalidated buffers before failing.
3. **Use BlockOn policy**: `.with_policy::<BlockOn<GarbageCollect>>()` to wait for memory.
4. **Reduce in-flight buffer count**: publish more slowly or increase subscriber processing speed.
5. **Call `provider.garbage_collect()`** periodically in your application to proactively reclaim memory.

### Watchdog Invalidations (Unexpected Buffer Loss)

**Symptom:** Occasional `watchdog_invalidated` errors or buffers disappearing before subscribers process them.

**Cause:** A subscriber process is not confirming watchdog bits fast enough (100 ms interval), or has crashed while holding buffer references.

**Fix:**
- Ensure subscribers process or drop SHM buffers within 100 ms.
- Use `CongestionControl::Reliable` to prevent in-flight message loss.
- Avoid `CongestionControl::Block` under heavy congestion (can stall publishers and cause GC to reclaim buffers still in transit).

### Inspecting SHM Usage at Runtime

```bash
# List all Zenoh SHM segments on Linux
ls -lah /dev/shm/*.zenoh

# Count active segments
ls /dev/shm/*.zenoh 2>/dev/null | wc -l

# See which processes have them open
lsof /dev/shm/*.zenoh 2>/dev/null

# Memory usage of SHM
du -sh /dev/shm/*.zenoh 2>/dev/null
```

## See Also

- [Config Transport SHM](config-transport-shm.md) — the transport-level SHM configuration fields that activate and tune the subsystem
- [Performance Tuning Guide](performance-tuning-guide.md) — when SHM provides the best throughput vs network transport
- [Programming Model Guide](programming-model-guide.md) — the session and publisher API that SHM integrates with transparently
