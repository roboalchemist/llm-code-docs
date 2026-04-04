# Zenoh Public API Reference

> **Version:** zenoh 1.x (unstable features marked with `[unstable]`)
>
> Features gated behind `#[cfg(feature = "unstable")]` are marked **[unstable]** throughout this document. They require `features = ["unstable"]` in your `Cargo.toml`.

---

## Table of Contents

1. [Session Management](#1-session-management)
2. [Publisher API](#2-publisher-api)
3. [Subscriber API](#3-subscriber-api)
4. [Queryable API](#4-queryable-api)
5. [Querier API](#5-querier-api)
6. [Session Get](#6-session-get)
7. [Liveliness](#7-liveliness)
8. [Matching Status & Listeners](#8-matching-status--listeners)
9. [Scouting](#9-scouting)
10. [Key Expressions](#10-key-expressions)
11. [Selector](#11-selector)
12. [Sample Types](#12-sample-types)
13. [ZBytes & Serialization](#13-zbytes--serialization)
14. [Configuration](#14-configuration)
15. [Handlers](#15-handlers)
16. [Session Info](#16-session-info)
17. [QoS Types](#17-qos-types)

---

## 1. Session Management

### `zenoh::open()`

```rust
pub fn open<TryIntoConfig>(config: TryIntoConfig) -> OpenBuilder<TryIntoConfig>
where
    TryIntoConfig: TryInto<Config> + Send + 'static,
    TryIntoConfig::Error: Debug,
```

Opens a zenoh [`Session`]. Returns an `OpenBuilder` that resolves to `ZResult<Session>`.

**Parameters:**
- `config` — Anything convertible to `Config`: `Config::default()`, a file path string, etc.

**Returns:** `OpenBuilder<TryIntoConfig>` — resolves to `ZResult<Session>`

```rust
// Async usage
let session = zenoh::open(zenoh::Config::default()).await.unwrap();

// Sync usage
use zenoh::Wait;
let session = zenoh::open(zenoh::Config::default()).wait().unwrap();

// From file
let session = zenoh::open(zenoh::Config::from_file("config.json5").unwrap()).await.unwrap();
```

---

### `Session`

```rust
pub struct Session { /* ... */ }
```

A zenoh session. The main entry point for all pub/sub/query operations.

`Session` implements `Clone` (cheaply, via `Arc`) and `Drop` (closes the session).

#### Key Methods

```rust
impl Session {
    /// Declare a publisher on a key expression.
    pub fn declare_publisher<'b, TryIntoKeyExpr>(
        &self,
        key_expr: TryIntoKeyExpr,
    ) -> PublisherBuilder<'_, 'b>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>;

    /// Declare a subscriber on a key expression.
    pub fn declare_subscriber<'b, TryIntoKeyExpr>(
        &self,
        key_expr: TryIntoKeyExpr,
    ) -> SubscriberBuilder<'_, 'b, DefaultHandler>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>;

    /// Declare a queryable on a key expression.
    pub fn declare_queryable<'b, TryIntoKeyExpr>(
        &self,
        key_expr: TryIntoKeyExpr,
    ) -> QueryableBuilder<'_, 'b, DefaultHandler>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>;

    /// Declare a querier on a key expression.
    pub fn declare_querier<'b, TryIntoKeyExpr>(
        &self,
        key_expr: TryIntoKeyExpr,
    ) -> QuerierBuilder<'_, 'b>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>;

    /// Publish data (one-shot, without declaring a Publisher).
    pub fn put<'b, TryIntoKeyExpr, IntoZBytes>(
        &self,
        key_expr: TryIntoKeyExpr,
        payload: IntoZBytes,
    ) -> SessionPutBuilder<'_, 'b>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>,
        IntoZBytes: Into<ZBytes>;

    /// Delete data (one-shot).
    pub fn delete<'b, TryIntoKeyExpr>(
        &self,
        key_expr: TryIntoKeyExpr,
    ) -> SessionDeleteBuilder<'_, 'b>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>;

    /// Query the network.
    pub fn get<'b, IntoSelector>(
        &self,
        selector: IntoSelector,
    ) -> SessionGetBuilder<'_, 'b, DefaultHandler>
    where
        IntoSelector: TryInto<Selector<'b>>;

    /// Declare a key expression (obtains a numerical alias for efficient reuse).
    pub fn declare_keyexpr<'a, 'b: 'a, TryIntoKeyExpr>(
        &'a self,
        key_expr: TryIntoKeyExpr,
    ) -> impl Resolve<ZResult<KeyExpr<'b>>>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>;

    /// Access session info (ZID, router ZIDs, peer ZIDs).
    pub fn info(&self) -> SessionInfo<'_>;

    /// Access the liveliness API.
    pub fn liveliness(&self) -> Liveliness<'_>;

    /// Close the session explicitly.
    pub fn close(self) -> CloseBuilder<Session>;

    /// Undeclare a previously declared key expression.
    pub fn undeclare<'a, TryIntoKeyExpr>(
        &'a self,
        key_expr: TryIntoKeyExpr,
    ) -> impl Resolve<ZResult<()>> + 'a
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'a>> + 'a;
}
```

#### `Session::close()`

```rust
pub fn close(self) -> CloseBuilder<Session>
```

Closes the session. By default waits up to 10 seconds for pending operations.

```rust
session.close().await.unwrap();

// [unstable] Wait for all callbacks to complete before closing
session.close().wait_callbacks().await.unwrap();
```

---

### `CloseBuilder`

```rust
pub struct CloseBuilder<TCloseable: Closeable> { /* ... */ }
```

Builder returned by `Session::close()`. Resolves to `ZResult<()>`.

| Method | Description |
|--------|-------------|
| `wait_callbacks()` **[unstable]** | Block until all running callbacks return before completing close |

---

## 2. Publisher API

### `PublisherBuilder`

Returned by `Session::declare_publisher()`. Resolves to `ZResult<Publisher<'_>>`.

```rust
pub struct PublisherBuilder<'a, 'b> { /* ... */ }
```

#### Builder Methods

```rust
impl PublisherBuilder<'_, '_> {
    /// Set default encoding for all publications from this publisher.
    pub fn encoding<T: Into<Encoding>>(self, encoding: T) -> Self;

    /// Set congestion control policy.
    pub fn congestion_control(self, congestion_control: CongestionControl) -> Self;

    /// Set priority.
    pub fn priority(self, priority: Priority) -> Self;

    /// Enable/disable express mode (skip batching for lower latency).
    pub fn express(self, is_express: bool) -> Self;

    /// Restrict to subscribers with the given locality.
    pub fn allowed_destination(self, destination: Locality) -> Self;

    /// [unstable] Set reliability hint.
    pub fn reliability(self, reliability: Reliability) -> Self;
}
```

```rust
use zenoh::qos::{CongestionControl, Priority};

let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let publisher = session
    .declare_publisher("my/topic")
    .encoding(zenoh::bytes::Encoding::TEXT_PLAIN)
    .congestion_control(CongestionControl::Block)
    .priority(Priority::RealTime)
    .express(true)
    .await
    .unwrap();
```

---

### `Publisher`

```rust
pub struct Publisher<'a> { /* ... */ }
```

A declared publisher. Reuse this across multiple publications for efficiency (key expression is pre-registered).

#### Methods

```rust
impl<'a> Publisher<'a> {
    /// Publish a payload (Put).
    pub fn put<IntoZBytes>(&self, payload: IntoZBytes) -> PublisherPutBuilder<'_>
    where
        IntoZBytes: Into<ZBytes>;

    /// Publish a delete.
    pub fn delete(&self) -> PublisherDeleteBuilder<'_>;

    /// The key expression this publisher publishes to.
    pub fn key_expr(&self) -> &KeyExpr<'a>;

    /// The default encoding.
    pub fn encoding(&self) -> &Encoding;

    /// The congestion control setting.
    pub fn congestion_control(&self) -> CongestionControl;

    /// The priority setting.
    pub fn priority(&self) -> Priority;

    /// Whether express mode is enabled.
    pub fn is_express(&self) -> bool;

    /// Undeclare the publisher.
    pub fn undeclare(self) -> PublisherUndeclaration<'a>;

    /// [unstable] Get a MatchingStatus (are there matching subscribers?).
    pub fn matching_status(&self) -> ZResult<MatchingStatus>;

    /// [unstable] Declare a listener for matching status changes.
    pub fn matching_listener(&self) -> MatchingListenerBuilder<'_, DefaultHandler>;
}
```

```rust
let publisher = session.declare_publisher("demo/data").await.unwrap();

// Put
publisher.put("Hello, World!").await.unwrap();

// Put with options
publisher
    .put("Hello")
    .encoding(zenoh::bytes::Encoding::TEXT_PLAIN)
    .timestamp(uhlc::HLC::default().new_timestamp())
    .attachment(b"meta".as_slice())
    .await
    .unwrap();

// Delete
publisher.delete().await.unwrap();

// Explicit undeclare
publisher.undeclare().await.unwrap();
```

---

### `PublicationBuilder`

Returned by `Session::put()`, `Session::delete()`, `Publisher::put()`, and `Publisher::delete()`. Resolves to `ZResult<()>`.

```rust
pub struct PublicationBuilder<P, T> { /* ... */ }
```

#### Builder Methods (for `Put` variant)

```rust
// Encoding (only for Put)
pub fn encoding<T: Into<Encoding>>(self, encoding: T) -> Self;

// QoS (only on Session::put / Session::delete builders)
pub fn congestion_control(self, congestion_control: CongestionControl) -> Self;
pub fn priority(self, priority: Priority) -> Self;
pub fn express(self, is_express: bool) -> Self;
pub fn allowed_destination(self, destination: Locality) -> Self;

// [unstable] Reliability (only on Session::put / Session::delete builders)
pub fn reliability(self, reliability: Reliability) -> Self;

// Metadata
pub fn timestamp<T: Into<Option<uhlc::Timestamp>>>(self, timestamp: T) -> Self;
pub fn attachment<T: Into<OptionZBytes>>(self, attachment: T) -> Self;

// [unstable]
pub fn source_info<T: Into<Option<SourceInfo>>>(self, source_info: T) -> Self;
```

```rust
use zenoh::bytes::Encoding;
use zenoh::qos::CongestionControl;

// Session-level put (no pre-declared publisher)
session
    .put("demo/data", "payload string")
    .encoding(Encoding::TEXT_PLAIN)
    .congestion_control(CongestionControl::Block)
    .await
    .unwrap();

// Session-level delete
session.delete("demo/data").await.unwrap();
```

---

### Type Aliases

| Alias | Description |
|-------|-------------|
| `SessionPutBuilder<'a, 'b>` | `PublicationBuilder<PublisherBuilder<'a, 'b>, PublicationBuilderPut>` |
| `SessionDeleteBuilder<'a, 'b>` | `PublicationBuilder<PublisherBuilder<'a, 'b>, PublicationBuilderDelete>` |
| `PublisherPutBuilder<'a>` | `PublicationBuilder<&'a Publisher<'a>, PublicationBuilderPut>` |
| `PublisherDeleteBuilder<'a>` | `PublicationBuilder<&'a Publisher<'a>, PublicationBuilderDelete>` |

---

## 3. Subscriber API

### `SubscriberBuilder`

Returned by `Session::declare_subscriber()`. Resolves to `ZResult<Subscriber<H>>`.

```rust
pub struct SubscriberBuilder<'a, 'b, Handler, const BACKGROUND: bool = false> { /* ... */ }
```

#### Handler Selection Methods

```rust
impl<'a, 'b> SubscriberBuilder<'a, 'b, DefaultHandler> {
    /// Use a callback.
    pub fn callback<F>(self, callback: F) -> SubscriberBuilder<'a, 'b, Callback<Sample>>
    where
        F: Fn(Sample) + Send + Sync + 'static;

    /// Use a mutable callback (never called concurrently).
    pub fn callback_mut<F>(self, callback: F) -> SubscriberBuilder<'a, 'b, Callback<Sample>>
    where
        F: FnMut(Sample) + Send + Sync + 'static;

    /// Use any handler implementing IntoHandler<Sample>.
    pub fn with<Handler>(self, handler: Handler) -> SubscriberBuilder<'a, 'b, Handler>
    where
        Handler: IntoHandler<Sample>;
}

impl<'a, 'b> SubscriberBuilder<'a, 'b, Callback<Sample>> {
    /// Run subscriber in background until session closes (no Subscriber returned).
    pub fn background(self) -> SubscriberBuilder<'a, 'b, Callback<Sample>, true>;
}

impl<Handler, const BACKGROUND: bool> SubscriberBuilder<'_, '_, Handler, BACKGROUND> {
    /// Restrict to samples published with the given locality.
    pub fn allowed_origin(self, origin: Locality) -> Self;
}
```

```rust
// Callback-based subscriber
let subscriber = session
    .declare_subscriber("demo/**")
    .callback(|sample| {
        println!(
            "Received '{}': {:?}",
            sample.key_expr(),
            sample.payload()
        );
    })
    .await
    .unwrap();

// Channel-based subscriber (FIFO via flume)
let subscriber = session
    .declare_subscriber("demo/**")
    .with(flume::bounded(256))
    .await
    .unwrap();

while let Ok(sample) = subscriber.recv_async().await {
    println!("Received: {}", sample.key_expr());
}

// Background subscriber (fire and forget)
session
    .declare_subscriber("demo/**")
    .callback(|s| println!("{}", s.key_expr()))
    .background()
    .await
    .unwrap();
```

---

### `Subscriber<Handler>`

```rust
pub struct Subscriber<Handler> { /* ... */ }
```

A declared subscriber. Automatically undeclared on `Drop`.

`Subscriber<Handler>` implements `Deref<Target = Handler>` and `DerefMut`, so you can call handler methods directly.

```rust
impl<Handler> Subscriber<Handler> {
    /// The key expression this subscriber subscribes to.
    pub fn key_expr(&self) -> &KeyExpr<'static>;

    /// Reference to the handler.
    pub fn handler(&self) -> &Handler;

    /// Mutable reference to the handler.
    pub fn handler_mut(&mut self) -> &mut Handler;

    /// Undeclare the subscriber explicitly.
    pub fn undeclare(self) -> SubscriberUndeclaration<Handler>
    where
        Handler: Send;
}
```

```rust
// Using flume channel via Deref
let sub = session
    .declare_subscriber("demo/**")
    .with(flume::bounded(128))
    .await
    .unwrap();

// recv_async() is called via Deref to flume::Receiver
while let Ok(sample) = sub.recv_async().await {
    println!("{}", sample.key_expr());
}

// Explicit undeclare
sub.undeclare().await.unwrap();
```

---

### Handlers Overview

Three primary patterns:

| Pattern | Type | Description |
|---------|------|-------------|
| Callback | `Callback<T>` | Calls `F: Fn(T)` on each item |
| Mutable callback | `Callback<T>` (via `locked`) | Wraps `FnMut` in a mutex |
| Channel | `(flume::Sender<T>, flume::Receiver<T>)` | FIFO channel |
| Ring buffer | `RingChannel` **[unstable]** | Keeps only latest N items |

See [Section 15. Handlers](#15-handlers) for full details.

---

## 4. Queryable API

### `QueryableBuilder`

Returned by `Session::declare_queryable()`. Resolves to `ZResult<Queryable<H>>`.

```rust
pub struct QueryableBuilder<'a, 'b, Handler, const BACKGROUND: bool = false> { /* ... */ }
```

#### Handler Selection Methods

```rust
impl<'a, 'b> QueryableBuilder<'a, 'b, DefaultHandler> {
    pub fn callback<F>(self, callback: F) -> QueryableBuilder<'a, 'b, Callback<Query>>
    where
        F: Fn(Query) + Send + Sync + 'static;

    pub fn callback_mut<F>(self, callback: F) -> QueryableBuilder<'a, 'b, Callback<Query>>
    where
        F: FnMut(Query) + Send + Sync + 'static;

    pub fn with<Handler>(self, handler: Handler) -> QueryableBuilder<'a, 'b, Handler>
    where
        Handler: IntoHandler<Query>;
}

impl<'a, 'b> QueryableBuilder<'a, 'b, Callback<Query>> {
    /// Run in background until session closes.
    pub fn background(self) -> QueryableBuilder<'a, 'b, Callback<Query>, true>;
}

impl<Handler, const BACKGROUND: bool> QueryableBuilder<'_, '_, Handler, BACKGROUND> {
    /// Declare as "complete" — promises to have all data for its key expression.
    pub fn complete(self, complete: bool) -> Self;

    /// Restrict to queries with the given locality.
    pub fn allowed_origin(self, origin: Locality) -> Self;
}
```

```rust
// Callback-based queryable
let queryable = session
    .declare_queryable("demo/data")
    .callback(|query| {
        println!("Query on: {}", query.selector());
        // Reply with data
        query
            .reply("demo/data", "response payload")
            .wait()
            .unwrap();
    })
    .await
    .unwrap();

// Channel-based queryable
let queryable = session
    .declare_queryable("demo/data")
    .with(flume::bounded(64))
    .await
    .unwrap();

while let Ok(query) = queryable.recv_async().await {
    println!("Received query: '{}'", query.selector());
    query.reply(query.key_expr().clone(), "answer").await.unwrap();
}
```

---

### `Queryable<Handler>`

```rust
pub struct Queryable<Handler> { /* ... */ }
```

A declared queryable. Automatically undeclared on `Drop`.

`Queryable<Handler>` implements `Deref<Target = Handler>`.

```rust
impl<Handler> Queryable<Handler> {
    /// Key expression this queryable is registered on.
    pub fn key_expr(&self) -> &KeyExpr<'static>;

    /// Reference to the handler.
    pub fn handler(&self) -> &Handler;

    /// Mutable reference to the handler.
    pub fn handler_mut(&mut self) -> &mut Handler;

    /// Explicitly undeclare.
    pub fn undeclare(self) -> QueryableUndeclaration<Handler>
    where
        Handler: Send;
}
```

---

### `Query`

```rust
pub struct Query { /* ... */ }
```

Received by a queryable's handler when a query arrives.

```rust
impl Query {
    /// The full selector (key expression + parameters).
    pub fn selector(&self) -> Selector<'_>;

    /// The key expression part of the selector.
    pub fn key_expr(&self) -> &KeyExpr<'static>;

    /// The parameters part of the selector.
    pub fn parameters(&self) -> &Parameters<'_>;

    /// The optional payload sent with the query.
    pub fn payload(&self) -> Option<&ZBytes>;

    /// The optional encoding of the query payload.
    pub fn encoding(&self) -> Option<&Encoding>;

    /// The optional attachment.
    pub fn attachment(&self) -> Option<&ZBytes>;

    /// Reply with a Put sample.
    pub fn reply<'b, TryIntoKeyExpr, IntoZBytes>(
        &self,
        key_expr: TryIntoKeyExpr,
        payload: IntoZBytes,
    ) -> ReplyBuilder<'_, 'b, ReplyBuilderPut>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>,
        IntoZBytes: Into<ZBytes>;

    /// Reply with a Delete sample.
    pub fn reply_del<'b, TryIntoKeyExpr>(
        &self,
        key_expr: TryIntoKeyExpr,
    ) -> ReplyBuilder<'_, 'b, ReplyBuilderDelete>
    where
        TryIntoKeyExpr: TryInto<KeyExpr<'b>>;

    /// Reply with an error payload.
    pub fn reply_err<IntoZBytes>(
        &self,
        payload: IntoZBytes,
    ) -> ReplyErrBuilder<'_>
    where
        IntoZBytes: Into<ZBytes>;
}
```

#### `ReplyBuilder`

```rust
impl<T> ReplyBuilder<'_, '_, T> {
    pub fn timestamp<U: Into<Option<uhlc::Timestamp>>>(self, timestamp: U) -> Self;
    pub fn attachment<U: Into<OptionZBytes>>(self, attachment: U) -> Self;
    pub fn express(self, is_express: bool) -> Self;
    // [unstable]
    pub fn source_info<U: Into<Option<SourceInfo>>>(self, source_info: U) -> Self;
}

// Only for ReplyBuilderPut:
impl ReplyBuilder<'_, '_, ReplyBuilderPut> {
    pub fn encoding<T: Into<Encoding>>(self, encoding: T) -> Self;
}
```

#### `ReplyErrBuilder`

```rust
impl ReplyErrBuilder<'_> {
    pub fn encoding<T: Into<Encoding>>(self, encoding: T) -> Self;
}
```

```rust
// Full example: queryable that replies
let queryable = session
    .declare_queryable("demo/query")
    .with(flume::bounded(16))
    .await
    .unwrap();

tokio::spawn(async move {
    while let Ok(query) = queryable.recv_async().await {
        println!(
            "Query selector: {}, params: {}",
            query.key_expr(),
            query.parameters()
        );

        // Successful reply
        query
            .reply(query.key_expr().clone(), b"result data")
            .encoding(zenoh::bytes::Encoding::APPLICATION_OCTET_STREAM)
            .await
            .unwrap();

        // Or error reply
        // query.reply_err("not found").encoding(Encoding::TEXT_PLAIN).await.unwrap();
    }
});
```

---

## 5. Querier API

### `QuerierBuilder`

Returned by `Session::declare_querier()`. Resolves to `ZResult<Querier<'_>>`.

```rust
pub struct QuerierBuilder<'a, 'b> { /* ... */ }
```

```rust
impl QuerierBuilder<'_, '_> {
    /// Target queryable selection strategy.
    pub fn target(self, target: QueryTarget) -> Self;

    /// Consolidation mode for replies.
    pub fn consolidation<QC: Into<QueryConsolidation>>(self, consolidation: QC) -> Self;

    /// Restrict to queryables with the given locality.
    pub fn allowed_destination(self, destination: Locality) -> Self;

    /// Timeout for each get() issued by this querier.
    pub fn timeout(self, timeout: Duration) -> Self;

    /// Whether to accept replies on disjoint key expressions.
    pub fn accept_replies(self, accept: ReplyKeyExpr) -> Self;

    // QoS
    pub fn congestion_control(self, congestion_control: CongestionControl) -> Self;
    pub fn priority(self, priority: Priority) -> Self;
    pub fn express(self, is_express: bool) -> Self;
}
```

---

### `Querier`

```rust
pub struct Querier<'a> { /* ... */ }
```

A declared querier — a pre-configured query issuer for repeated queries on the same key expression.

```rust
impl<'a> Querier<'a> {
    /// Issue a get using this querier's configuration.
    pub fn get(&self) -> QuerierGetBuilder<'_, '_, DefaultHandler>;

    /// The key expression this querier targets.
    pub fn key_expr(&self) -> &KeyExpr<'a>;

    /// Undeclare the querier.
    pub fn undeclare(self) -> QuerierUndeclaration<'a>;

    /// [unstable] Matching status.
    pub fn matching_status(&self) -> ZResult<MatchingStatus>;

    /// [unstable] Matching listener.
    pub fn matching_listener(&self) -> MatchingListenerBuilder<'_, DefaultHandler>;
}
```

---

### `QuerierGetBuilder`

Returned by `Querier::get()`. Resolves to `ZResult<Handler::Handler>`.

```rust
impl<'a, 'b> QuerierGetBuilder<'a, 'b, DefaultHandler> {
    pub fn callback<F>(self, callback: F) -> QuerierGetBuilder<'a, 'b, Callback<Reply>>
    where F: Fn(Reply) + Send + Sync + 'static;

    pub fn callback_mut<F>(self, callback: F) -> QuerierGetBuilder<'a, 'b, Callback<Reply>>
    where F: FnMut(Reply) + Send + Sync + 'static;

    pub fn with<Handler>(self, handler: Handler) -> QuerierGetBuilder<'a, 'b, Handler>
    where Handler: IntoHandler<Reply>;
}

impl<'b, Handler> QuerierGetBuilder<'_, 'b, Handler> {
    /// Set the selector parameters (e.g. "value>1&key=foo").
    pub fn parameters<P: Into<Parameters<'b>>>(self, parameters: P) -> Self;

    /// Set a payload to send with the query.
    pub fn payload<IntoZBytes: Into<ZBytes>>(self, payload: IntoZBytes) -> Self;

    /// Set encoding for the query payload.
    pub fn encoding<T: Into<Encoding>>(self, encoding: T) -> Self;

    /// Set an attachment.
    pub fn attachment<T: Into<OptionZBytes>>(self, attachment: T) -> Self;

    // [unstable]
    pub fn source_info<T: Into<Option<SourceInfo>>>(self, source_info: T) -> Self;
    pub fn cancellation_token(self, token: CancellationToken) -> Self;
}
```

```rust
use zenoh::query::{ConsolidationMode, QueryTarget};

let querier = session
    .declare_querier("demo/data")
    .target(QueryTarget::All)
    .consolidation(ConsolidationMode::None)
    .timeout(std::time::Duration::from_secs(5))
    .await
    .unwrap();

// Issue repeated queries efficiently
let replies = querier
    .get()
    .parameters("value>1")
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Got: {}", sample.key_expr()),
        Err(err) => println!("Error: {:?}", err.payload()),
    }
}
```

---

## 6. Session Get

### `Session::get()`

```rust
pub fn get<'b, IntoSelector>(
    &self,
    selector: IntoSelector,
) -> SessionGetBuilder<'_, 'b, DefaultHandler>
where
    IntoSelector: TryInto<Selector<'b>>;
```

Issue a one-shot query to the network.

### `SessionGetBuilder`

Resolves to `ZResult<Handler::Handler>`.

```rust
impl<'a, 'b> SessionGetBuilder<'a, 'b, DefaultHandler> {
    pub fn callback<F>(self, callback: F) -> SessionGetBuilder<'a, 'b, Callback<Reply>>
    where F: Fn(Reply) + Send + Sync + 'static;

    pub fn callback_mut<F>(self, callback: F) -> SessionGetBuilder<'a, 'b, Callback<Reply>>
    where F: FnMut(Reply) + Send + Sync + 'static;

    pub fn with<Handler>(self, handler: Handler) -> SessionGetBuilder<'a, 'b, Handler>
    where Handler: IntoHandler<Reply>;
}

impl<Handler> SessionGetBuilder<'_, '_, Handler> {
    pub fn target(self, target: QueryTarget) -> Self;
    pub fn consolidation<QC: Into<QueryConsolidation>>(self, consolidation: QC) -> Self;
    pub fn allowed_destination(self, destination: Locality) -> Self;
    pub fn timeout(self, timeout: Duration) -> Self;
    pub fn accept_replies(self, accept: ReplyKeyExpr) -> Self;

    /// Payload to send with the query.
    pub fn payload<IntoZBytes: Into<ZBytes>>(self, payload: IntoZBytes) -> Self;

    /// Encoding for the query payload.
    pub fn encoding<T: Into<Encoding>>(self, encoding: T) -> Self;

    /// Attachment for the query.
    pub fn attachment<T: Into<OptionZBytes>>(self, attachment: T) -> Self;

    // QoS
    pub fn congestion_control(self, congestion_control: CongestionControl) -> Self;
    pub fn priority(self, priority: Priority) -> Self;
    pub fn express(self, is_express: bool) -> Self;

    // [unstable]
    pub fn source_info<T: Into<Option<SourceInfo>>>(self, source_info: T) -> Self;
    pub fn cancellation_token(self, token: CancellationToken) -> Self;
}
```

```rust
use zenoh::query::{ConsolidationMode, QueryTarget};

// Simple get with channel
let replies = session
    .get("demo/data")
    .with(flume::bounded(64))
    .await
    .unwrap();

while let Ok