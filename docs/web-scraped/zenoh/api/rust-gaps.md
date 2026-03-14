# Zenoh API Documentation for Missing Symbols

## Module: `close`

### `fn in_background`

Converts a close operation into a background close operation that runs concurrently.

**Returns:** `BackgroundCloseBuilder` wrapping the close future.

**Note:** Requires both `unstable` and `internal` features.

```rust
#[cfg(all(feature = "unstable", feature = "internal"))]
let handle = session.close().in_background().await;
handle.wait(); // optionally wait for completion
```

---

### `struct BackgroundCloseBuilder`

A builder for close operations that run in the background (concurrently). Wraps an async close future and spawns it on the zenoh runtime, returning a `NolocalJoinHandle` to optionally await the result.

**Note:** Requires both `unstable` and `internal` features.

```rust
#[cfg(all(feature = "unstable", feature = "internal"))]
let handle = session.close().in_background().await;
// The close operation runs concurrently; join via handle if needed
let result = handle.await;
```

---

### `struct NolocalJoinHandle`

A join handle for a background close operation that does not rely on thread-local storage. Useful for waiting on background operations that were spawned on the zenoh runtime.

**Type parameter:** `TOutput: Send + 'static` — the output type of the background operation.

**Note:** Requires both `unstable` and `internal` features.

```rust
#[cfg(all(feature = "unstable", feature = "internal"))]
let handle: NolocalJoinHandle<ZResult<()>> = session.close().in_background().await;
let result = handle.await; // waits for the background close to complete
```

---

## Module: `info_links`

### `struct LinkEventsListenerUndeclaration`

A [`Resolvable`] returned by [`LinkEventsListener::undeclare`]. When resolved (awaited or `.wait()`-ed), it undeclares the link events listener and stops event delivery.

Optionally, you can call `.wait_callbacks()` to block until all in-flight callback invocations have completed before undeclaring.

**Note:** Requires the `unstable` feature.

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let listener = session.info()
    .link_events_listener()
    .with(flume::bounded(32))
    .await
    .unwrap();
// Later, undeclare and wait for callbacks
listener.undeclare().wait_callbacks().await.unwrap();
# }
```

---

## Module: `info_transport`

### `struct TransportEventsListenerUndeclaration`

A [`Resolvable`] returned by [`TransportEventsListener::undeclare`]. When resolved, it undeclares the transport events listener and stops transport event delivery.

Optionally, call `.wait_callbacks()` to wait for all in-flight callbacks to finish before undeclaring.

**Note:** Requires the `unstable` feature.

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let listener = session.info()
    .transport_events_listener()
    .with(flume::bounded(32))
    .await
    .unwrap();
listener.undeclare().wait_callbacks().await.unwrap();
# }
```

---

## Module: `publisher`

### `struct PublicationBuilderPut`

A marker type used as a type parameter of [`PublicationBuilder`] to indicate a **Put** publication. Carries the encoding for the payload.

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let publisher = session.declare_publisher("demo/topic").await.unwrap();
// put() returns a PublicationBuilder<PublicationBuilderPut>
publisher.put("hello").await.unwrap();
# }
```

---

### `struct PublicationBuilderDelete`

A marker type used as a type parameter of [`PublicationBuilder`] to indicate a **Delete** publication.

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let publisher = session.declare_publisher("demo/topic").await.unwrap();
// delete() returns a PublicationBuilder<PublicationBuilderDelete>
publisher.delete().await.unwrap();
# }
```

---

## Module: `sample`

### `struct SampleBuilderPut`

A marker type indicating a **Put** sample builder. Used as a type parameter in [`SampleBuilder`] to produce samples of kind `SampleKind::Put`.

```rust
use zenoh::sample::SampleBuilder;
// Created implicitly when using session.put(...)
```

---

### `struct SampleBuilderDelete`

A marker type indicating a **Delete** sample builder. Used as a type parameter in [`SampleBuilder`] to produce samples of kind `SampleKind::Delete`.

```rust
// Created implicitly when using session.delete(...)
```

---

### `struct SampleBuilderAny`

A marker type indicating a sample builder that can produce samples of any kind. Used when the sample kind is not fixed at compile time.

```rust
// Used internally when sample kind is determined at runtime
```

---

### `struct SampleBuilder`

A builder for constructing [`Sample`]s with configurable quality-of-service, timestamps, encoding, and payload. The type parameter `T` is one of `SampleBuilderPut`, `SampleBuilderDelete`, or `SampleBuilderAny`.

Implements [`QoSBuilderTrait`], [`TimestampBuilderTrait`], [`SampleBuilderTrait`], and [`EncodingBuilderTrait`] (for Put variants).

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
session.put("demo/topic", "payload")
    .priority(zenoh::qos::Priority::RealTime)
    .await
    .unwrap();
# }
```

---

### `trait QoSBuilderTrait`

A trait for builders that allow configuring Quality-of-Service parameters on publications or samples.

Provides methods such as:
- `priority(Priority)` — set the message priority.
- `congestion_control(CongestionControl)` — set congestion control behavior.
- `express(bool)` — enable/disable express mode (bypass batching).

```rust
# #[tokio::main]
# async fn main() {
use zenoh::qos::{CongestionControl, Priority};
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
session.put("demo/topic", "data")
    .priority(Priority::DataHigh)
    .congestion_control(CongestionControl::Drop)
    .express(true)
    .await
    .unwrap();
# }
```

---

### `trait TimestampBuilderTrait`

A trait for builders that allow attaching a [`Timestamp`] to a sample.

Provides:
- `timestamp(impl Into<Option<Timestamp>>)` — attach or clear the timestamp.

```rust
# #[tokio::main]
# async fn main() {
use zenoh::time::Timestamp;
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let ts = zenoh::time::new_reception_timestamp();
session.put("demo/topic", "data")
    .timestamp(ts)
    .await
    .unwrap();
# }
```

---

### `trait SampleBuilderTrait`

A trait for builders that produce [`Sample`]s. Provides common sample configuration methods, including source information.

Provides:
- `source_info(SourceInfo)` — attach source information (unstable).

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
session.put("demo/topic", "data").await.unwrap();
# }
```

---

### `trait EncodingBuilderTrait`

A trait for builders that allow specifying the [`Encoding`] of a payload.

Provides:
- `encoding(impl Into<Encoding>)` — set the encoding for the payload.

```rust
# #[tokio::main]
# async fn main() {
use zenoh::bytes::Encoding;
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
session.put("demo/topic", "hello")
    .encoding(Encoding::TEXT_PLAIN)
    .await
    .unwrap();
# }
```

---

## Module: `scouting`

### `struct ScoutBuilder`

A builder returned by [`zenoh::scout`] for discovering zenoh nodes on the network. Allows configuring what kinds of nodes to scout for and how to handle results.

**Methods include:**
- `what(WhatAmIMatcher)` — filter by node type (Router, Peer, Client).
- `config(Config)` — provide a custom configuration.
- `with(handler)` — set the result handler.
- `callback(F)` — provide a callback function.

```rust
# #[tokio::main]
# async fn main() {
use zenoh::scouting::WhatAmI;
let scout = zenoh::scout(WhatAmI::Peer | WhatAmI::Router, zenoh::Config::default())
    .await
    .unwrap();
while let Ok(hello) = scout.recv_async().await {
    println!("Found: {:?}", hello);
}
# }
```

---

## Module: `session`

### `fn init`

Initializes a zenoh session from a [`Config`]. This is a lower-level entry point equivalent to [`zenoh::open`], primarily used internally or for advanced scenarios.

**Parameters:**
- `config: Config` — the session configuration.

**Returns:** An `InitBuilder` that resolves to `ZResult<Session>`.

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::session::init(zenoh::Config::default()).await.unwrap();
# }
```

---

### `fn aggregated_subscribers`

Returns the list of key expressions for which subscriber interest is aggregated (reported as a single interest rather than individually). Configured via the session config.

**Returns:** `&[OwnedKeyExpr]`

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
// Typically used internally; accessible via session internals
# }
```

---

### `fn aggregated_publishers`

Returns the list of key expressions for which publisher interest is aggregated. Configured via the session config.

**Returns:** `&[OwnedKeyExpr]`

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
// Typically used internally; accessible via session internals
# }
```

---

### `struct InitBuilder`

A builder returned by [`session::init`] that resolves to a [`Session`]. Allows configuring session initialization options.

```rust
# #[tokio::main]
# async fn main() {
let session = zenoh::session::init(zenoh::Config::default())
    .await
    .unwrap();
# }
```

---

## Module: `bytes`

### `fn is_empty`

Returns `true` if the `ZBytes` buffer contains no data.

**Returns:** `bool`

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::default();
assert!(b.is_empty());
```

---

### `fn len`

Returns the total number of bytes in the `ZBytes` buffer.

**Returns:** `usize`

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from("hello");
assert_eq!(b.len(), 5);
```

---

### `fn to_bytes`

Converts the `ZBytes` into a contiguous `Cow<[u8]>`. This may involve copying if the buffer is fragmented.

**Returns:** `Cow<[u8]>`

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from("hello");
let raw: std::borrow::Cow<[u8]> = b.to_bytes();
assert_eq!(&*raw, b"hello");
```

---

### `fn try_to_string`

Attempts to interpret the `ZBytes` contents as a UTF-8 string.

**Returns:** `Result<Cow<str>, _>`

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from("hello");
assert_eq!(b.try_to_string().unwrap(), "hello");
```

---

### `fn reader`

Creates a [`ZBytesReader`] for reading from the `ZBytes` buffer sequentially.

**Returns:** `ZBytesReader`

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from("hello");
let mut reader = b.reader();
// use reader to deserialize
```

---

### `fn from_reader`

Constructs a `ZBytes` by consuming a [`ZBytesReader`], capturing whatever data remains.

**Parameters:**
- `reader: ZBytesReader` — the reader to reconstruct from.

**Returns:** `ZBytes`

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from("hello");
let reader = b.reader();
let b2 = ZBytes::from_reader(reader);
```

---

### `fn writer`

Creates a [`ZBytesWriter`] for writing data into a new `ZBytes` buffer.

**Returns:** `ZBytesWriter`

```rust
use zenoh::bytes::ZBytes;
let mut writer = ZBytes::writer();
// serialize data into writer
let b: ZBytes = writer.finish();
```

---

### `fn slices`

Returns a [`ZBytesSliceIterator`] that iterates over the internal contiguous byte slices composing the buffer. Useful for zero-copy access.

**Returns:** `ZBytesSliceIterator`

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from("hello");
for slice in b.slices() {
    println!("{:?}", slice);
}
```

---

### `fn as_shm`

Returns a reference to the shared-memory buffer if this `ZBytes` wraps one.

**Returns:** `Option<&ZShm>`

**Note:** Requires the `shared-memory` feature.

```rust
#[cfg(feature = "shared-memory")]
{
    use zenoh::bytes::ZBytes;
    let b = ZBytes::from("hello");
    let shm = b.as_shm(); // None if not SHM
}
```

---

### `fn as_shm_mut`

Returns a mutable reference to the shared-memory buffer if this `ZBytes` wraps one.

**Returns:** `Option<&mut ZShm>`

**Note:** Requires the `shared-memory` feature.

```rust
#[cfg(feature = "shared-memory")]
{
    use zenoh::bytes::ZBytes;
    let mut b = ZBytes::from("hello");
    let shm = b.as_shm_mut();
}
```

---

### `fn remaining`

Returns the number of bytes remaining to be read in a [`ZBytesReader`].

**Returns:** `usize`

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from("hello");
let reader = b.reader();
assert_eq!(reader.remaining(), 5);
```

---

### `fn append`

Appends another `ZBytes` to a [`ZBytesWriter`], or appends raw bytes to the buffer without copying (zero-copy append where possible).

**Parameters:**
- `bytes: ZBytes` — the bytes to append.

```rust
use zenoh::bytes::ZBytes;
let mut writer = ZBytes::writer();
writer.append(ZBytes::from("hello"));
writer.append(ZBytes::from(" world"));
let b = writer.finish();
```

---

### `fn finish`

Finalizes a [`ZBytesWriter`] and returns the completed `ZBytes` buffer.

**Returns:** `ZBytes`

```rust
use zenoh::bytes::ZBytes;
let mut writer = ZBytes::writer();
writer.append(ZBytes::from("data"));
let b: ZBytes = writer.finish();
```

---

### `struct ZBytesReader`

A sequential reader over the contents of a [`ZBytes`] buffer. Supports deserializing typed values via the `Deserialize` integration.

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from("hello");
let reader = b.reader();
let s: String = reader.deserialize().unwrap();
```

---

### `struct ZBytesWriter`

A writer for building up a [`ZBytes`] buffer. Supports appending raw bytes, serializing typed values, and zero-copy appending.

```rust
use zenoh::bytes::ZBytes;
let mut writer = ZBytes::writer();
writer.serialize("hello");
let b = writer.finish();
```

---

### `struct ZBytesSliceIterator`

An iterator over the contiguous byte slices that compose a [`ZBytes`] buffer. Allows zero-copy access to underlying data segments.

```rust
use zenoh::bytes::ZBytes;
let b = ZBytes::from(vec![1u8, 2, 3]);
for slice in b.slices() {
    println!("{:?}", slice);
}
```

---

## Module: `cancellation`

### `fn is_cancelled`

Returns `true` if the associated cancellation token has been cancelled.

**Returns:** `bool`

```rust
// Used on a CancellationToken to check cancellation status
if token.is_cancelled() {
    println!("Operation was cancelled");
}
```

---

### `struct CancelResult`

Represents the result of a cancellable operation. Indicates whether the operation completed successfully or was cancelled.

```rust
match cancel_result {
    CancelResult::Completed(val) => println!("Got: {:?}", val),
    CancelResult::Cancelled => println!("Cancelled"),
}
```

---

### `trait CancellationTokenBuilderTrait`

A trait for builders that support attaching a cancellation token. Provides the method:
- `cancellation_token(token: CancellationToken)` — attach a token to cancel the operation.

```rust
// Used internally by builders that support cooperative cancellation
```

---

## Module: `config`

### `fn from_env`

Creates a zenoh [`Config`] by reading configuration from environment variables.

**Returns:** `ZResult<Config>`

```rust
let config = zenoh::Config::from_env().unwrap();
```

---

### `fn from_json5`

Parses a zenoh [`Config`] from a JSON5-formatted string.

**Parameters:**
- `s: &str` — the JSON5 configuration string.

**Returns:** `ZResult<Config>`

```rust
let config = zenoh::Config::from_json5(r#"{ mode: "peer" }"#).unwrap();
```

---

### `fn insert_json5`

Inserts a JSON5 value at a given path within the configuration tree.

**Parameters:**
- `key: &str` — the dot-separated path in the config.
- `value: &str` — the JSON5-encoded value to insert.

**Returns:** `ZResult<()>`

```rust
let mut config = zenoh::Config::default();
config.insert_json5("mode", r#""router""#).unwrap();
```

---

### `fn get_json`

Retrieves the JSON-encoded value at a given path in the configuration tree.

**Parameters:**
- `key: &str` — the dot-separated path in the config.

**Returns:** `ZResult<String>`

```rust
let config = zenoh::Config::default();
let mode = config.get_json("mode").unwrap();
println!("Mode: {}", mode);
```

---

### `struct Notifier`

A handle for notifying listeners when configuration values change. Used to subscribe to live configuration updates.

```rust
// Obtained from config; used to receive dynamic config change notifications
let notifier = config.notifier().unwrap();
```

---

### `struct LookupGuard`

A guard returned when looking up a value in the configuration. Holds a read lock on the config tree while active.

```rust
// Used internally when reading config values under a lock
```

---

### `type Notification`

A type alias representing a configuration change notification, typically containing the changed key path and its new JSON value.

```rust
// Received via Notifier when config values change
```

---

## Module: `encoding`

### `fn with_schema`

Attaches a schema string to an [`Encoding`], producing a new encoding with that schema annotation.

**Parameters:**
- `schema: impl Into<Cow<'static, str>>` — the schema identifier string.

**Returns:** `Encoding`

```rust
use zenoh::bytes::Encoding;
let enc = Encoding::APPLICATION_JSON.with_schema("my-schema");
```

---

### `fn schema`

Returns the schema annotation of this [`Encoding`], if any.

**Returns:** `Option<&str>`

```rust
use zenoh::bytes::Encoding;
let enc = Encoding::TEXT_PLAIN;
println!("{:?}", enc.schema()); // None for built-in encodings
```

---

## Module: `callback`

### `fn locked`

Wraps an [`FnMut`]`(T)` into an [`Fn`]`(T)` by protecting calls with a [`Mutex`]. This is useful when you need to pass a mutable closure where an immutable one is required.

**Parameters:**
- `fnmut: impl FnMut(T)` — the mutable closure to wrap.

**Returns:** `impl Fn(T)`

```rust
use zenoh::handlers::locked;
let mut count = 0usize;
let cb = locked(move |_: ()| { count += 1; });
cb(()); // safe to call concurrently
```

---

### `struct Callback`

The core callback type used throughout zenoh. Stores a type-erased, `Send + Sync` callable behind an `Arc`, so it can be cloned and shared across threads.

**Type parameter:** `T: CallbackParameter`

**Key method:**
- `call(&self, arg: T)` — invoke the callback.

```rust
use zenoh::handlers::Callback;
let cb = Callback::from(|msg: String| println!("{}", msg));
cb.call("hello".to_string());
```

---

### `struct CallbackDrop`

A handler that pairs a callback function with a drop function. Guarantees that:
- The drop function is called exactly once, after all callback invocations have finished.
- The callback is never called concurrently with the drop function.

**Fields:**
- `callback: Callback` — the event handler.
- `drop: DropFn` — called when the handler is dropped.

```rust
use zenoh::handlers::CallbackDrop;
let handler = CallbackDrop {
    callback: |sample: zenoh::sample::Sample| println!("Got sample"),
    drop: || println!("Handler dropped"),
};
```

---

### `trait CallbackParameter`

A trait that types must implement to be usable as callback parameters in zenoh handlers. It defines how an owned `T` is produced from a message reference.

**Associated type:** `Message<'a>` — the borrowed message type.

**Required method:** `from_message(msg: Self::Message<'_>) -> Self`

```rust
// Implemented automatically for zenoh built-in types like Sample, Hello, etc.
```

---

## Module: `fifo`

### `fn recv_deadline`

Receives a value from the FIFO channel, blocking until one is available or the deadline passes.

**Parameters:**
- `deadline: Instant` — the point in time after which the call returns `None`.

**Returns:** `ZResult<Option<T>>`

```rust
use std::time::{Duration, Instant};
let (_, handler) = flume::bounded::<String>(8);
// For FifoChannelHandler:
// let val = handler.recv_deadline(Instant::now() + Duration::from_secs(1));
```

---

### `fn recv_timeout`

Receives a value from the FIFO channel, blocking until one is available or the timeout expires.

**Parameters:**
- `timeout: Duration` — maximum time to wait.

**Returns:** `ZResult<Option<T>>`

```rust
use std::time::Duration;
// let val = handler.recv_timeout(Duration::from_millis(100));
```

---

### `fn iter`

Returns a blocking iterator over the FIFO channel. Iteration stops when the channel is disconnected and drained.

**Returns:** `impl Iterator<Item = T>`

```rust
// for item in handler.iter() { ... }
```

---

### `fn try_iter`

Returns a non-blocking iterator that yields all currently available items without blocking.

**Returns:** `TryIter<T>`

```rust
// for item in handler.try_iter() { ... }
```

---

### `fn drain`

Drains all currently available items from the FIFO channel into a `Drain` iterator.

**Returns:** `Drain<T>`

```rust
// let drained: Vec<_> = handler.drain().collect();
```

---

### `fn is_disconnected`

Returns `true` if all senders for this FIFO channel have been dropped.

**Returns:** `bool`

```rust
// if handler.is_disconnected() { println!("no more senders"); }
```

---

### `fn is_full`

Returns `true` if the FIFO channel's buffer is currently full.

**Returns:** `bool`

```rust
// if handler.is_full() { println!("channel full"); }
```

---

### `fn capacity`

Returns the capacity of the FIFO channel, or `None` if unbounded.

**Returns:** `Option<usize>`

```rust
// println!("capacity: {:?}", handler.capacity());
```

---

### `fn sender_count`

Returns the number of active senders connected to this FIFO channel.

**Returns:** `usize`

```rust
// println!("senders: {}", handler.sender_count());
```

---

### `fn receiver_count`

Returns the number of active receivers connected to this FIFO channel.

**Returns:** `usize`

```rust
// println!("receivers: {}", handler.receiver_count());
```

---

### `fn same_channel`

Returns `true` if two handlers refer to the same underlying FIFO channel.

**Parameters:**
- `other: &FifoChannelHandler<T>` — the handler to compare with.

**Returns:** `bool`

```rust
// assert!(handler.same_channel(&handler_clone));
```

---

### `fn into_recv_async`

Converts this handler into an async receive future.

**Returns:** `RecvFut<T>`

```rust
// let val = handler.into_recv_async().await;
```

---

### `fn stream`

Returns an async `Stream` that yields items from the FIFO channel.

**Returns:** `RecvStream<T>`

```rust
use futures::StreamExt;
// while let Some(item) = handler.stream().next().await { ... }
```

---

### `fn into_stream`

Converts this handler into an owned async `Stream`.

**Returns:** `RecvStream<T>`

```rust
use futures::StreamExt;
// let mut stream = handler.into_stream();
// while let Some(item) = stream.next().await { ... }
```

---

### `struct FifoChannel`

A bounded FIFO channel handler factory. When used with zenoh entities (subscribers, queryables, etc.), it buffers received data in a FIFO queue of fixed capacity, blocking the sender if full.

```rust
use zenoh::handlers::FifoChannel;
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let subscriber = session
    .declare_subscriber("demo/topic")
    .with(FifoChannel::new(256))
    .await
    .unwrap();
while let Ok(sample) = subscriber.recv_async().await {
    println!("Received: {:?}", sample);
}
# }
```

---

### `struct FifoChannelHandler`

The receiver end of a [`FifoChannel`]. Provides blocking and async methods to receive items queued by zenoh callbacks.

```rust
use zenoh::handlers::FifoChannel;
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let handler = session
    .declare_subscriber("demo/topic")
    .with(FifoChannel::new(64))
    .await
    .unwrap();
// handler is a FifoChannelHandler<Sample>
let sample = handler.recv_async().await.unwrap();
# }
```

---

### `struct TryIter`

A non-blocking iterator returned by `FifoChannelHandler::try_iter`. Yields all items currently available in the channel without blocking.

```rust
// for item in handler.try_iter() { process(item); }
```

---

### `struct Drain`

An iterator returned by `FifoChannelHandler::drain`. Drains all currently buffered items from the channel.

```rust
// let items: Vec<_> = handler.drain().collect();
```

---

### `struct IntoIter`

An owning iterator over a `FifoChannelHandler`. Consumes the handler and yields all items until the channel is disconnected and empty.

```rust
// for item in handler { process(item); }
```

---

### `struct RecvFut`

A future returned by async receive operations on a [`FifoChannelHandler`]. Resolves to the next available item.

```rust
// let item = handler.recv_async().await.unwrap();
```

---

### `struct RecvStream`

An async `Stream` over a [`FifoChannelHandler`]. Yields items as they become available.

```rust
use futures::StreamExt;
// let mut stream = handler.into_stream();
// while let Some(item) = stream.next().await { process(item); }
```

---

## Module: `ring`

### `struct RingChannel`

A bounded ring-buffer channel. Unlike [`FifoChannel`], when the buffer is full, the **oldest** item is dropped to make room for the newest. This ensures the receiver always sees the most recent data.

**Constructor:** `RingChannel::new(capacity: usize)`

```rust
use zenoh::handlers::RingChannel;
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let subscriber = session
    .declare_subscriber("demo/sensor")
    .with(RingChannel::new(8))
    .await
    .unwrap();
// Only the latest 8 unread samples are retained
while let Ok(sample) = subscriber.recv_async().await {
    println!("Latest: {:?}", sample);
}
# }
```

---

### `struct RingChannelHandler`

The receiver end of a [`RingChannel`]. Provides blocking, timeout, deadline, and async methods for receiving items. When the ring buffer overflows, old items are silently dropped.

**Methods:**
- `recv() -> ZResult<T>` — block until an item is available.
- `recv_deadline(Instant) -> ZResult<Option<T>>` — block with a deadline.
- `recv_timeout(Duration) -> ZResult<Option<T>>` — block with a timeout.
- `recv_async() -> ZResult<T>` — async receive.
- `try_recv() -> ZResult<Option<T>>` — non-blocking receive.

```rust
use zenoh::handlers::RingChannel;
# #[tokio::main]
# async fn main() {
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let handler = session
    .declare_subscriber("demo/sensor")
    .with(RingChannel::new(4))
    .await
    .unwrap();
if let Ok(Some(sample)) = handler.try_recv() {
    println!("Got: {:?}", sample);
}
# }
```

---

## Module: `info`

### `fn locators`

Returns the locators (network addresses) on which this zenoh session is currently listening.

**Returns:** `impl Iterator<Item = Locator>`

```rust
# #[tokio::main]
# async