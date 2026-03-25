# zenoh-ext: Zenoh Extension Crate

## Table of Contents

- [Overview](#overview)
- [Adding to Cargo.toml](#adding-to-cargotoml)
- [Serialization / Deserialization](#serialization-deserialization)
  - [Key types and functions](#key-types-and-functions)
  - [Supported types](#supported-types)
  - [Example](#example)
  - [Custom types](#custom-types)
- [Publication Cache (deprecated — prefer AdvancedPublisher)](#publication-cache-deprecated-prefer-advancedpublisher)
- [Querying Subscriber (deprecated — prefer AdvancedSubscriber)](#querying-subscriber-deprecated-prefer-advancedsubscriber)
- [Advanced Publisher](#advanced-publisher)
  - [CacheConfig options](#cacheconfig-options)
- [Advanced Subscriber](#advanced-subscriber)
  - [HistoryConfig options](#historyconfig-options)
  - [RecoveryConfig options](#recoveryconfig-options)
- [Liveliness](#liveliness)
- [Session Extension Trait](#session-extension-trait)
- [Feature Flags](#feature-flags)
- [Migration: Old → New APIs](#migration-old-new-apis)
- [Source and Documentation](#source-and-documentation)

## Overview

`zenoh-ext` is a Rust crate that builds on top of the core `zenoh` crate to provide
higher-level utilities for common patterns: type-safe serialization, publication caching
for late-joining subscribers, querying subscribers that recover missed samples, and
advanced publisher/subscriber pairs with delivery guarantees.

Most advanced features require the `unstable` Cargo feature. Serialization is stable and
enabled by default.

## Adding to Cargo.toml

```toml
# Stable — serialization only
zenoh-ext = "1.0"

# Unstable features (AdvancedPublisher, AdvancedSubscriber, PublicationCache, etc.)
zenoh-ext = { version = "1.0", features = ["unstable"] }
```

The `unstable` feature also pulls in `zenoh/unstable` and `zenoh/internal`.

## Serialization / Deserialization

zenoh-ext provides a compact, cross-language binary serialization format. The same format
is supported in C, C++, Python, Java, Kotlin, TypeScript, and zenoh-pico, which makes it
the recommended way to exchange typed data across language boundaries.

### Key types and functions

- `z_serialize(value)` — serialize any `T: Serialize` into a `ZBytes`
- `z_deserialize::<T>(zbytes)` — deserialize a `ZBytes` into `T: Deserialize`
- `ZSerializer` — low-level streaming writer (appends fields in order)
- `ZDeserializer` — low-level streaming reader
- `ZReadIter` — iterator over repeated items in a payload

### Supported types

All primitive Rust types (`bool`, `u8`–`u128`, `i8`–`i128`, `f32`, `f64`, `char`,
`String`, `&str`, `Vec<u8>`, `&[u8]`), tuples up to reasonable arity, `Vec<T>`,
`HashMap<K,V>`, `BTreeMap<K,V>`, `HashSet<T>`, `BTreeSet<T>`, and `Option<T>`.

### Example

```rust
use zenoh_ext::*;

// Serialize a tuple
let zbytes = z_serialize(&(42i32, vec![1u8, 2, 3]));

// Deserialize
let (n, v) = z_deserialize::<(i32, Vec<u8>)>(&zbytes).unwrap();
assert_eq!(n, 42);
assert_eq!(v, vec![1, 2, 3]);
```

### Custom types

Implement `Serialize` and `Deserialize` manually or use the `ZSerializer`/`ZDeserializer`
directly for complex structs. Fields must be written and read in the same order.

```rust
use zenoh_ext::{Serialize, Deserialize, ZSerializer, ZDeserializer, ZDeserializeError};

struct Point { x: f64, y: f64 }

impl Serialize for Point {
    fn serialize(&self, s: &mut ZSerializer) {
        self.x.serialize(s);
        self.y.serialize(s);
    }
}

impl Deserialize for Point {
    fn deserialize(d: &mut ZDeserializer) -> Result<Self, ZDeserializeError> {
        Ok(Point { x: f64::deserialize(d)?, y: f64::deserialize(d)? })
    }
}
```

## Publication Cache (deprecated — prefer AdvancedPublisher)

`PublicationCache` maintains a local cache of recent publications on a key expression.
Late-joining subscribers can query the cache via a companion Queryable to receive missed
samples. This pattern is now superseded by `AdvancedPublisher` + `AdvancedSubscriber`.

Requires `unstable` feature.

```rust
use zenoh_ext::SessionExt;

let pub_cache = session
    .declare_publication_cache("my/key/**")
    .history(10)          // keep last 10 samples per resource
    .await
    .unwrap();
```

## Querying Subscriber (deprecated — prefer AdvancedSubscriber)

`FetchingSubscriber` / `QueryingSubscriberBuilder` subscribes to live publications and
also queries for historical samples on startup, merging them in timestamp order.

Requires `unstable` feature.

```rust
use zenoh_ext::{SessionExt, SubscriberBuilderExt};

let subscriber = session
    .declare_subscriber("my/key/**")
    .querying()
    .await
    .unwrap();
```

## Advanced Publisher

`AdvancedPublisher` extends the standard publisher with:

- **Publication cache** — stores recent samples for late-joining subscribers
- **Sample miss detection** — sends periodic heartbeats so subscribers can detect gaps
- **Publisher detection** — notifies subscribers when a new publisher appears

Requires `unstable` feature. Enable timestamping in the session config for correct
sequencing.

```rust
use std::time::Duration;
use zenoh_ext::{AdvancedPublisherBuilderExt, CacheConfig, MissDetectionConfig};

let publisher = session
    .declare_publisher("demo/example/**")
    .cache(CacheConfig::default().max_samples(10))
    .sample_miss_detection(
        MissDetectionConfig::default().heartbeat(Duration::from_millis(500))
    )
    .publisher_detection()
    .await
    .unwrap();

publisher.put("hello").await.unwrap();
```

### CacheConfig options

- `.max_samples(n)` — maximum number of samples to cache per key expression
- `.replies_config(RepliesConfig::...)` — tune query consolidation for cache replies

## Advanced Subscriber

`AdvancedSubscriber` complements `AdvancedPublisher` with:

- **History** — on startup, queries for cached samples from matching publishers
- **Recovery** — re-requests samples missed due to network loss (using heartbeat gaps)
- **Miss detection** — exposes a `SampleMissListener` that fires when samples are skipped
- **Publisher detection** — discovers publishers that come online after subscription

Requires `unstable` feature.

```rust
use zenoh_ext::{AdvancedSubscriberBuilderExt, HistoryConfig, RecoveryConfig};

let subscriber = session
    .declare_subscriber("demo/example/**")
    .history(HistoryConfig::default().detect_late_publishers())
    .recovery(RecoveryConfig::default().heartbeat())
    .subscriber_detection()
    .await
    .unwrap();

// Listen for detected sample gaps
let miss_listener = subscriber.sample_miss_listener().await.unwrap();

loop {
    tokio::select! {
        sample = subscriber.recv_async() => {
            if let Ok(s) = sample {
                println!("Received: {}", s.payload().try_to_string().unwrap());
            }
        },
        miss = miss_listener.recv_async() => {
            if let Ok(m) = miss {
                println!("Missed {} samples from {:?}", m.nb(), m.source());
            }
        },
    }
}
```

### HistoryConfig options

- `.detect_late_publishers()` — also fetch history from publishers that come online after the subscriber
- `.max_samples(n)` — limit number of historical samples to request

### RecoveryConfig options

- `.heartbeat()` — use publisher heartbeats to detect and recover missed samples
- `.periodic_queries(Duration)` — periodically re-query for missed samples as fallback

## Liveliness

zenoh-ext does not add new liveliness APIs beyond what the core `zenoh` crate provides.
Liveliness tokens (`session.liveliness().declare_token(key)`) and liveliness subscribers
(`session.liveliness().declare_subscriber(key)`) are available directly in `zenoh`.

The `FetchingSubscriber` in zenoh-ext does support a `LivelinessSpace` key space for
querying liveliness tokens historically, but this is also deprecated in favor of the
advanced subscriber pattern.

## Session Extension Trait

`SessionExt` (from `zenoh_ext::SessionExt`) adds convenience methods to `Session`:

- `session.declare_publication_cache(key)` — shorthand for PublicationCache builder

Note: The querying subscriber is accessed via `SubscriberBuilderExt` (a separate trait): `session.declare_subscriber(key).querying()`. There is no `session.declare_querying_subscriber(key)` method on `SessionExt`.

Import with:

```rust
use zenoh_ext::SessionExt;
```

## Feature Flags

| Feature | Default | Description |
|---------|---------|-------------|
| `default` | yes | Enables `zenoh/default` (serialization always available) |
| `unstable` | no | Enables advanced pub/sub, publication cache, querying subscriber |
| `internal` | no | Exposes internal types like `VarInt` for codec work |

## Migration: Old → New APIs

| Old (deprecated) | New (recommended) |
|------------------|-------------------|
| `PublicationCache` | `AdvancedPublisher` with `CacheConfig` |
| `QueryingSubscriber` / `FetchingSubscriber` | `AdvancedSubscriber` with `HistoryConfig` + `RecoveryConfig` |

Both old and new APIs are present in the codebase. Prefer the `AdvancedPublisher` /
`AdvancedSubscriber` pair for all new code.

## Source and Documentation

- Crate source: `zenoh-ext/` in the [eclipse-zenoh/zenoh](https://github.com/eclipse-zenoh/zenoh) repo
- API docs: <https://docs.rs/zenoh-ext>
- Examples: `zenoh-ext/examples/examples/` — `z_advanced_pub.rs`, `z_advanced_sub.rs`, `z_member.rs`
- Serialization RFC: <https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Serialization.md>

## See Also

- [Queryable Complete Guide](queryable-complete-guide.md) — the query/reply pattern used internally by AdvancedPublisher's cache
- [Serialization Complete Guide](serialization-complete-guide.md) — the `z_serialize`/`z_deserialize` format also available in zenoh-ext
- [Storage Backends Guide](storage-backends-guide.md) — the storage manager provides similar persistence for publisher caches at a infrastructure level
