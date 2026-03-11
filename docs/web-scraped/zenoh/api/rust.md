# Zenoh Crate — Public API Reference

> **Version**: zenoh 1.x (unstable features marked with `[unstable]`)
>
> All builder methods implement the builder pattern and resolve via `.await` (async) or `.wait()` (sync). Most builders are annotated `#[must_use]`.

---

## Table of Contents

1. [Session Management](#1-session-management)
2. [Publisher API](#2-publisher-api)
3. [Subscriber API](#3-subscriber-api)
4. [Queryable API](#4-queryable-api)
5. [Querier API](#5-querier-api)
6. [Session `get()`](#6-session-get)
7. [Liveliness](#7-liveliness)
8. [Matching Status](#8-matching-status)
9. [Scouting](#9-scouting)
10. [Key Expressions](#10-key-expressions)
11. [Selector](#11-selector)
12. [Sample Types](#12-sample-types)
13. [ZBytes & Serialization](#13-zbytes--serialization)
14. [Config](#14-config)
15. [Handlers](#15-handlers)
16. [Session Info & Transport \[unstable\]](#16-session-info--transport-unstable)

---

## 1. Session Management

### `zenoh::open()`

```rust
pub fn open<TryIntoConfig>(config: TryIntoConfig) -> OpenBuilder<TryIntoConfig>
where
    TryIntoConfig: TryInto<Config> + Send + 'static,
    TryIntoConfig::Error: Debug,
```

Opens a zenoh `Session`. Returns an `OpenBuilder` which resolves to `ZResult<Session>`.

**Parameters**
- `config` — Any value that can be converted into a `Config` (e.g., `Config::default()`, a file path, JSON5 string).

**Returns** `ZResult<Session>`

```rust
// Async
let session = zenoh::open(zenoh::Config::default()).await.unwrap();

// Sync
use zenoh::Wait;
let session = zenoh::open(zenoh::Config::default()).wait().unwrap();
```

---

### `OpenBuilder`

```rust
pub struct OpenBuilder<TryIntoConfig> { /* private */ }
```

Builder returned by `zenoh::open()`.

| Method | Signature | Description |
|--------|-----------|-------------|
| `with_shm_clients` | `fn with_shm_clients(self, shm_clients: Arc<ShmClientStorage>) -> Self` | **[unstable/feature=shared-memory]** Attach shared-memory clients. |

Implements `IntoFuture<Output = ZResult<Session>>` and `Wait`.

---

### `Session`

```rust
pub struct Session { /* private */ }
```

The central zenoh handle. `Session` implements `Clone` (reference-counted) and `Drop` (auto-closes).

#### Session methods

| Method | Signature | Description |
|--------|-----------|-------------|
| `info` | `fn info(&self) -> SessionInfo<'_>` | Returns session metadata (ZID, router ZIDs, peer ZIDs). |
| `declare_publisher` | `fn declare_publisher<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> PublisherBuilder<'_, 'b>` | Declare a `Publisher`. |
| `declare_subscriber` | `fn declare_subscriber<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> SubscriberBuilder<'_, 'b, DefaultHandler>` | Declare a `Subscriber`. |
| `declare_queryable` | `fn declare_queryable<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> QueryableBuilder<'_, 'b, DefaultHandler>` | Declare a `Queryable`. |
| `declare_querier` | `fn declare_querier<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> QuerierBuilder<'_, 'b>` | Declare a `Querier`. |
| `declare_keyexpr` | `fn declare_keyexpr<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> impl Resolvable<To = ZResult<KeyExpr<'static>>>` | Optimize a key expression on the wire. |
| `put` | `fn put<'b, TryIntoKeyExpr, IntoZBytes>(&self, key_expr: TryIntoKeyExpr, payload: IntoZBytes) -> SessionPutBuilder<'_, 'b>` | Publish data (put). |
| `delete` | `fn delete<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> SessionDeleteBuilder<'_, 'b>` | Publish a delete. |
| `get` | `fn get<'b, IntoSelector>(&self, selector: IntoSelector) -> SessionGetBuilder<'_, 'b, DefaultHandler>` | Issue a query. |
| `liveliness` | `fn liveliness(&self) -> Liveliness<'_>` | Access the liveliness API. |
| `close` | `fn close(&self) -> CloseBuilder<Self>` | Close the session. |
| `downgrade` | `fn downgrade(&self) -> WeakSession` | Get a weak reference. |

```rust
let session = zenoh::open(zenoh::Config::default()).await.unwrap();

// Put
session.put("demo/key", "hello").await.unwrap();

// Delete
session.delete("demo/key").await.unwrap();

// Close
session.close().await.unwrap();
```

---

### `SessionInfo`

```rust
pub struct SessionInfo<'a> { /* private */ }
```

Provides access to runtime information.

| Method | Returns | Description |
|--------|---------|-------------|
| `zid()` | `ZenohIdBuilder<'_>` → `ZenohId` | The ZID of this session. |
| `routers_zid()` | `RoutersZenohIdBuilder<'_>` → `impl Iterator<Item=ZenohId>` | ZIDs of connected routers. |
| `peers_zid()` | `PeersZenohIdBuilder<'_>` → `impl Iterator<Item=ZenohId>` | ZIDs of connected peers. |
| `transports()` | **[unstable]** `TransportsBuilder<'_>` → `impl Iterator<Item=Transport>` | Active transports. |
| `links()` | **[unstable]** `LinksBuilder<'_>` → `impl Iterator<Item=Link>` | Established links. |
| `transport_events_listener()` | **[unstable]** `TransportEventsListenerBuilder<'_>` | Subscribe to transport lifecycle events. |
| `link_events_listener()` | **[unstable]** `LinkEventsListenerBuilder<'_>` | Subscribe to link lifecycle events. |

```rust
let session = zenoh::open(zenoh::Config::default()).await.unwrap();
let zid = session.info().zid().await;
println!("My ZID: {zid}");

let mut router_zids = session.info().routers_zid().await;
while let Some(rzid) = router_zids.next() {
    println!("Connected to router: {rzid}");
}
```

---

### `CloseBuilder`

```rust
pub struct CloseBuilder<TCloseable> { /* private */ }
```

Returned by `Session::close()`. Resolves to `ZResult<()>`.

| Method | Description |
|--------|-------------|
| `timeout(Duration)` | **[unstable+internal]** Set close timeout (default: 10s). |
| `wait_callbacks()` | **[unstable]** Block until all running callbacks have returned. |

```rust
session.close().wait_callbacks().await.unwrap();
```

---

## 2. Publisher API

### `PublisherBuilder`

```rust
pub struct PublisherBuilder<'a, 'b> { /* private */ }
```

Returned by `Session::declare_publisher()`. Resolves to `ZResult<Publisher<'b>>`.

| Method | Description |
|--------|-------------|
| `encoding(impl Into<Encoding>)` | Default encoding for publications. |
| `congestion_control(CongestionControl)` | `Drop` (default) or `Block`. |
| `priority(Priority)` | Message priority (1=highest … 7=lowest). |
| `express(bool)` | Disable batching for low-latency. |
| `allowed_destination(Locality)` | Restrict to `SessionLocal`, `Remote`, or `Any`. |
| `reliability(Reliability)` | **[unstable]** `BestEffort` or `Reliable`. |

```rust
use zenoh::qos::{CongestionControl, Priority};

let publisher = session
    .declare_publisher("demo/key")
    .congestion_control(CongestionControl::Block)
    .priority(Priority::RealTime)
    .await
    .unwrap();
```

---

### `Publisher<'a>`

```rust
pub struct Publisher<'a> { /* private */ }
```

A declared publisher. Drop to undeclare, or call `.undeclare()`.

| Method | Signature | Description |
|--------|-----------|-------------|
| `put` | `fn put<IntoZBytes>(&self, payload: IntoZBytes) -> PublisherPutBuilder<'_>` | Publish data. |
| `delete` | `fn delete(&self) -> PublisherDeleteBuilder<'_>` | Publish a delete. |
| `key_expr` | `fn key_expr(&self) -> &KeyExpr<'a>` | The publisher's key expression. |
| `encoding` | `fn encoding(&self) -> &Encoding` | Default encoding. |
| `congestion_control` | `fn congestion_control(&self) -> CongestionControl` | Current congestion control. |
| `priority` | `fn priority(&self) -> Priority` | Current priority. |
| `is_express` | `fn is_express(&self) -> bool` | Express mode flag. |
| `matching_status` | `fn matching_status(&self) -> impl Resolvable<To=ZResult<MatchingStatus>>` | **[unstable]** Check if matching subscribers exist. |
| `matching_listener` | `fn matching_listener(&self) -> MatchingListenerBuilder<'_, DefaultHandler>` | **[unstable]** Subscribe to matching status changes. |
| `undeclare` | `fn undeclare(self) -> PublisherUndeclaration<'a>` | Explicitly undeclare. |

```rust
let publisher = session.declare_publisher("demo/key").await.unwrap();

// Simple put
publisher.put("hello world").await.unwrap();

// Put with options
publisher
    .put("hello")
    .encoding(zenoh::bytes::Encoding::TEXT_PLAIN)
    .timestamp(session.new_timestamp())
    .await
    .unwrap();

// Delete
publisher.delete().await.unwrap();

// Undeclare
publisher.undeclare().await.unwrap();
```

---

### `PublicationBuilder<P, T>`

```rust
pub struct PublicationBuilder<P, T> { /* private */ }
```

Returned by `session.put()`, `session.delete()`, `publisher.put()`, `publisher.delete()`. Type aliases:

- `SessionPutBuilder<'a, 'b>` — from `session.put()`
- `SessionDeleteBuilder<'a, 'b>` — from `session.delete()`
- `PublisherPutBuilder<'a>` — from `publisher.put()`
- `PublisherDeleteBuilder<'a>` — from `publisher.delete()`

All resolve to `ZResult<()>`.

| Method | Applicable to | Description |
|--------|---------------|-------------|
| `encoding(impl Into<Encoding>)` | Put only | Payload encoding. |
| `timestamp(impl Into<Option<Timestamp>>)` | Both | HLC timestamp. |
| `attachment(impl Into<OptionZBytes>)` | Both | Arbitrary attachment. |
| `congestion_control(CongestionControl)` | Session builders | Override congestion control. |
| `priority(Priority)` | Session builders | Override priority. |
| `express(bool)` | Session builders | Override express. |
| `allowed_destination(Locality)` | Session builders | Restrict destination. |
| `reliability(Reliability)` | **[unstable]** Session builders | Override reliability. |
| `source_info(SourceInfo)` | **[unstable]** Both | Attach source info. |

```rust
use zenoh::bytes::Encoding;
use zenoh::qos::CongestionControl;

// Via session (one-shot, no persistent publisher)
session
    .put("demo/key", b"binary data")
    .encoding(Encoding::APPLICATION_OCTET_STREAM)
    .congestion_control(CongestionControl::Block)
    .await
    .unwrap();

// Via declared publisher
publisher
    .put("hello")
    .timestamp(uhlc::HLC::default().new_timestamp())
    .attachment("metadata")
    .await
    .unwrap();
```

---

## 3. Subscriber API

### `SubscriberBuilder`

```rust
pub struct SubscriberBuilder<'a, 'b, Handler, const BACKGROUND: bool = false> { /* private */ }
```

Returned by `Session::declare_subscriber()`.

| Method | Description |
|--------|-------------|
| `callback(F)` | Handle samples with `F: Fn(Sample) + Send + Sync + 'static`. |
| `callback_mut(F)` | Handle samples with `F: FnMut(Sample)` (non-concurrent). |
| `with(Handler)` | Use any `IntoHandler<Sample>` (e.g., channel). |
| `allowed_origin(Locality)` | Restrict to `SessionLocal`, `Remote`, or `Any`. |
| `background()` | (After `.callback()`) Run until session closes; returns `ZResult<()>`. |

Resolves to `ZResult<Subscriber<Handler::Handler>>` (or `ZResult<()>` in background mode).

```rust
// With channel
let subscriber = session
    .declare_subscriber("demo/**")
    .with(flume::bounded(256))
    .await
    .unwrap();

while let Ok(sample) = subscriber.recv_async().await {
    println!("Received on '{}': {:?}", sample.key_expr(), sample.payload());
}

// With callback (background)
session
    .declare_subscriber("demo/**")
    .callback(|sample| println!("Got: {:?}", sample.payload()))
    .background()
    .await
    .unwrap();
```

---

### `Subscriber<Handler>`

```rust
pub struct Subscriber<Handler> { /* private */ }
```

Implements `Deref<Target = Handler>` so you can call channel methods directly.

| Method | Description |
|--------|-------------|
| `key_expr()` | Returns `&KeyExpr<'static>`. |
| `handler()` | `&Handler` reference. |
| `handler_mut()` | `&mut Handler` reference. |
| `undeclare(self)` | Explicitly undeclare, returns `SubscriberUndeclaration`. |
| `set_background(bool)` | **[internal]** Control drop behavior. |

`SubscriberUndeclaration` resolves to `ZResult<()>` and supports `.wait_callbacks()` **[unstable]**.

```rust
let subscriber = session
    .declare_subscriber("demo/**")
    .with(flume::bounded(32))
    .await
    .unwrap();

// Use deref to call flume methods directly
if let Ok(sample) = subscriber.try_recv() {
    println!("{:?}", sample.payload());
}

subscriber.undeclare().await.unwrap();
```

---

## 4. Queryable API

### `QueryableBuilder`

```rust
pub struct QueryableBuilder<'a, 'b, Handler, const BACKGROUND: bool = false> { /* private */ }
```

Returned by `Session::declare_queryable()`.

| Method | Description |
|--------|-------------|
| `callback(F)` | Handle queries with `F: Fn(Query)`. |
| `callback_mut(F)` | Handle queries with `F: FnMut(Query)` (non-concurrent). |
| `with(Handler)` | Use any `IntoHandler<Query>`. |
| `complete(bool)` | Mark queryable as complete (has all data for its key expression). |
| `allowed_origin(Locality)` | Restrict accepted query origins. |
| `background()` | Run until session closes; returns `ZResult<()>`. |

Resolves to `ZResult<Queryable<Handler::Handler>>`.

```rust
let queryable = session
    .declare_queryable("demo/key")
    .complete(true)
    .with(flume::bounded(32))
    .await
    .unwrap();

while let Ok(query) = queryable.recv_async().await {
    println!("Query: {}", query.selector());
    query
        .reply("demo/key", "answer")
        .await
        .unwrap();
}
```

---

### `Queryable<Handler>`

```rust
pub struct Queryable<Handler> { /* private */ }
```

Implements `Deref<Target = Handler>`.

| Method | Description |
|--------|-------------|
| `key_expr()` | `&KeyExpr<'static>`. |
| `handler()` | `&Handler`. |
| `handler_mut()` | `&mut Handler`. |
| `undeclare(self)` | Returns `QueryableUndeclaration`. |

---

### `Query`

```rust
pub struct Query { /* private */ }
```

Received by a queryable's handler. Represents an incoming query.

| Method | Signature | Description |
|--------|-----------|-------------|
| `selector()` | `fn selector(&self) -> &Selector<'_>` | The full selector (key expression + parameters). |
| `key_expr()` | `fn key_expr(&self) -> &KeyExpr<'static>` | The key expression part. |
| `parameters()` | `fn parameters(&self) -> &Parameters<'_>` | The parameters part. |
| `payload()` | `fn payload(&self) -> Option<&ZBytes>` | Optional query payload. |
| `encoding()` | `fn encoding(&self) -> Option<&Encoding>` | Payload encoding. |
| `attachment()` | `fn attachment(&self) -> Option<&ZBytes>` | Optional attachment. |
| `reply` | `fn reply<'b, TryIntoKeyExpr, IntoZBytes>(&self, key_expr: TryIntoKeyExpr, payload: IntoZBytes) -> ReplyBuilder<'_, 'b, ReplyBuilderPut>` | Reply with data. |
| `reply_del` | `fn reply_del<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> ReplyBuilder<'_, 'b, ReplyBuilderDelete>` | Reply with a delete. |
| `reply_err` | `fn reply_err<IntoZBytes>(&self, payload: IntoZBytes) -> ReplyErrBuilder<'_>` | Reply with an error. |

```rust
while let Ok(query) = queryable.recv_async().await {
    // Inspect
    println!("Query key: {}, params: {}", query.key_expr(), query.parameters());

    // Reply with data
    query.reply("demo/key", "answer").encoding(Encoding::TEXT_PLAIN).await.unwrap();

    // Reply with error
    // query.reply_err("not found").await.unwrap();
}
```

---

### `ReplyBuilder<'a, 'b, T>`

Returned by `Query::reply()` / `Query::reply_del()`. Resolves to `ZResult<()>`.

| Method | Applicable to | Description |
|--------|---------------|-------------|
| `encoding(impl Into<Encoding>)` | Put only | Payload encoding. |
| `timestamp(impl Into<Option<Timestamp>>)` | Both | HLC timestamp. |
| `attachment(impl Into<OptionZBytes>)` | Both | Arbitrary attachment. |
| `express(bool)` | Both | Disable batching. |
| `source_info(SourceInfo)` | **[unstable]** | Attach source info. |

### `ReplyErrBuilder<'a>`

Returned by `Query::reply_err()`. Resolves to `ZResult<()>`.

| Method | Description |
|--------|-------------|
| `encoding(impl Into<Encoding>)` | Error payload encoding. |

---

## 5. Querier API

### `QuerierBuilder`

```rust
pub struct QuerierBuilder<'a, 'b> { /* private */ }
```

Returned by `Session::declare_querier()`. Resolves to `ZResult<Querier<'b>>`.

| Method | Description |
|--------|-------------|
| `target(QueryTarget)` | `BestMatching` (default), `All`, `AllComplete`. |
| `consolidation(impl Into<QueryConsolidation>)` | Reply consolidation mode. |
| `allowed_destination(Locality)` | Restrict matching queryables. |
| `timeout(Duration)` | Query timeout. |
| `accept_replies(ReplyKeyExpr)` | Whether to accept replies on disjoint key expressions. |
| `congestion_control(CongestionControl)` | QoS setting. |
| `priority(Priority)` | QoS setting. |
| `express(bool)` | QoS setting. |

```rust
use zenoh::query::{ConsolidationMode, QueryTarget};

let querier = session
    .declare_querier("demo/**")
    .target(QueryTarget::All)
    .consolidation(ConsolidationMode::None)
    .timeout(std::time::Duration::from_secs(5))
    .await
    .unwrap();
```

---

### `Querier<'a>`

```rust
pub struct Querier<'a> { /* private */ }
```

A declared querier for reuse across multiple queries.

| Method | Description |
|--------|-------------|
| `get()` | Returns `QuerierGetBuilder<'_, '_, DefaultHandler>`. |
| `key_expr()` | `&KeyExpr<'a>`. |
| `target()` | Current `QueryTarget`. |
| `consolidation()` | Current `QueryConsolidation`. |
| `timeout()` | Current timeout. |
| `matching_status()` | **[unstable]** `ZResult<MatchingStatus>`. |
| `matching_listener()` | **[unstable]** `MatchingListenerBuilder`. |
| `undeclare(self)` | Explicitly undeclare. |

---

### `QuerierGetBuilder`

```rust
pub struct QuerierGetBuilder<'a, 'b, Handler> { /* private */ }
```

Returned by `Querier::get()`. Resolves to `ZResult<Handler::Handler>`.

| Method | Description |
|--------|-------------|
| `parameters(impl Into<Parameters<'b>>)` | Selector parameters string. |
| `payload(impl Into<ZBytes>)` | Query payload. |
| `encoding(impl Into<Encoding>)` | Payload encoding. |
| `attachment(impl Into<OptionZBytes>)` | Attachment. |
| `callback(F)` | Handle replies with callback. |
| `callback_mut(F)` | Non-concurrent callback. |
| `with(Handler)` | Use channel or custom handler. |
| `source_info(SourceInfo)` | **[unstable]** Source info. |
| `cancellation_token(CancellationToken)` | **[unstable]** Cancel in-flight query. |

```rust
let replies = querier
    .get()
    .parameters("value>1")
    .with(flume::bounded(32))
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("Reply: {:?}", sample.payload()),
        Err(err) => println!("Error: {:?}", err.payload()),
    }
}
```

---

## 6. Session `get()`

### `Session::get()`

```rust
pub fn get<'b, IntoSelector>(&self, selector: IntoSelector) -> SessionGetBuilder<'_, 'b, DefaultHandler>
where
    IntoSelector: TryInto<Selector<'b>>,
    IntoSelector::Error: Into<Error>,
```

Issues a one-shot query. The selector can be a string like `"demo/key"` or `"demo/key?param=value"`.

---

### `SessionGetBuilder`

```rust
pub struct SessionGetBuilder<'a, 'b, Handler> { /* private */ }
```

Resolves to `ZResult<Handler::Handler>`.

| Method | Description |
|--------|-------------|
| `target(QueryTarget)` | `BestMatching`, `All`, `AllComplete`. |
| `consolidation(impl Into<QueryConsolidation>)` | Reply consolidation. |
| `allowed_destination(Locality)` | Restrict query destination. |
| `timeout(Duration)` | Query timeout. |
| `accept_replies(ReplyKeyExpr)` | Accept replies on disjoint key exprs. |
| `payload(impl Into<ZBytes>)` | Query payload. |
| `encoding(impl Into<Encoding>)` | Payload encoding. |
| `attachment(impl Into<OptionZBytes>)` | Attachment. |
| `congestion_control(CongestionControl)` | QoS. |
| `priority(Priority)` | QoS. |
| `express(bool)` | QoS. |
| `callback(F)` | Handle replies with callback. |
| `callback_mut(F)` | Non-concurrent callback. |
| `with(Handler)` | Channel or custom handler. |
| `source_info(SourceInfo)` | **[unstable]** Source info. |
| `cancellation_token(CancellationToken)` | **[unstable]** Cancel query. |

```rust
use zenoh::query::{ConsolidationMode, QueryTarget};

let replies = session
    .get("demo/**?_time=[2024-01-01T00:00:00Z..]")
    .target(QueryTarget::All)
    .consolidation(ConsolidationMode::None)
    .timeout(std::time::Duration::from_secs(5))
    .with(flume::bounded(32))
    .await
    .unwrap();

while let Ok(reply) = replies.recv_async().await {
    match reply.result() {
        Ok(sample) => println!("'{}': {:?}", sample.key_expr(), sample.payload()),
        Err(err)   => println!("Error: {:?}", err.payload()),
    }
}
```

---

### `Reply`

```rust
pub struct Reply { /* private */ }
```

A reply received from a `get()` or `Querier::get()`.

| Method | Signature | Description |
|--------|-----------|-------------|
| `result()` | `fn result(&self) -> Result<&Sample, &ReplyError>` | Ok(sample) or Err(error). |
| `into_result()` | `fn into_result(self) -> Result<Sample, ReplyError>` | Consuming version. |
| `replier_id()` | `fn replier_id(&self) -> Option<ZenohId>` | ZID of the replier. |

---

### `ReplyError`

```rust
pub struct ReplyError { /* private */ }
```

| Method | Signature | Description |
|--------|-----------|-------------|
| `payload()` | `fn payload(&self) -> &ZBytes` | Error payload. |
| `encoding()` | `fn encoding(&self) -> &Encoding` | Error encoding. |

---

## 7. Liveliness

### `session.liveliness()`

```rust
pub fn liveliness(&self) -> Liveliness<'_>
```

Returns the liveliness API handle.

---

### `Liveliness<'a>`

```rust
pub struct Liveliness<'a> { /* private */ }
```

| Method | Signature | Description |
|--------|-----------|-------------|
| `declare_token` | `fn declare_token<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> LivelinessTokenBuilder<'a, 'b>` | Announce this process as alive on a key expression. |
| `declare_subscriber` | `fn declare_subscriber<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> LivelinessSubscriberBuilder<'a, 'b, DefaultHandler>` | Subscribe to liveliness events. |
| `get` | `fn get<'b, TryIntoKeyExpr>(&self, key_expr: TryIntoKeyExpr) -> LivelinessGetBuilder<'a, 'b, DefaultHandler>` | Query currently live tokens. |

---

### `LivelinessToken`

```rust
pub struct LivelinessToken { /* private */ }
```

Alive as long as this token is held. Drop or call `.undeclare()` to retract.

| Method | Description |
|--------|-------------|
| `key_expr()` | `&KeyExpr<'static>` |
| `undeclare(self)` | Returns `LivelinessTokenUndeclaration → ZResult<()>`. |

```rust
let token = session
    .liveliness()
    .declare_token("my/service/instance1")
    .await
    .unwrap();

// Token is alive here...

token.undeclare().await.unwrap();
// or just: drop(token);
```

---

### `LivelinessTokenBuilder`

Returned by `Liveliness::declare_token()`. Resolves to `ZResult<LivelinessToken>`.

---

### `LivelinessSubscriberBuilder`

```rust
pub struct LivelinessSubscriberBuilder<'a, 'b, Handler, const BACKGROUND: bool = false> { /* private */ }
```

| Method | Description |
|--------|-------------|
| `history(bool)` | When `true`, query for currently live tokens on declaration. |
| `callback(F)` | Handle `Sample` with callback. |
| `callback_mut(F)` | Non-concurrent callback. |
| `with(Handler)` | Channel or custom handler. |
| `background()` | Run until session closes. |

Resolves to `ZResult<Subscriber<Handler::Handler>>`.

```rust
let sub = session
    .liveliness()
    .declare_subscriber("my/service/**")
    .history(true)           // get existing live tokens
    .with(flume::bounded(32))
    .await
    .unwrap();

while let Ok(sample) = sub.recv_async().await {
    match sample.kind() {
        SampleKind::Put    => println!("Alive: {}", sample.key_expr()),
        SampleKind::Delete => println!("Gone:  {}", sample.key_expr()),
    }
}
```

---

### `LivelinessGetBuilder`

```rust
pub struct LivelinessGetBuilder<'a, 'b, Handler> { /* private */ }
```

| Method | Description |
|--------|-------------|
| `timeout(Duration)` | Query timeout. |
| `callback(F)` | Handle `Reply` with callback. |
| `callback_mut(F)` | Non-concurrent callback. |
| `with(Handler)` | Channel or custom handler. |
| `cancellation_token(CancellationToken)` | **[unstable]** Cancel the query. |

Resolves to `ZResult<Handler::Handler>`.

```rust
let replies = session
    .liveliness()
    .get("my/service/**")
    .timeout(std::time::Duration::from_secs(2))
    .with(flume::bounded(32))
    .await