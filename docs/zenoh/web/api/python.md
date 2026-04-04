# Zenoh Python API Reference

Complete reference for the zenoh Python binding (v1.7.x).

---

## Table of Contents

1. [Module Overview](#module-overview)
2. [zenoh.open()](#zenohopen)
3. [Config](#config)
4. [Session](#session)
5. [KeyExpr](#keyexpr)
6. [Selector & Parameters](#selector--parameters)
7. [Publisher](#publisher)
8. [Subscriber](#subscriber)
9. [Queryable & Query](#queryable--query)
10. [Querier](#querier)
11. [Reply & ReplyError](#reply--replyerror)
12. [Sample](#sample)
13. [ZBytes](#zbytes)
14. [Encoding](#encoding)
15. [Liveliness](#liveliness)
16. [Handlers](#handlers)
17. [Scouting](#scouting)
18. [Matching](#matching)
19. [zenoh.ext — Serialization](#zenohext--serialization)
20. [Error Types](#error-types)
21. [Complete Working Examples](#complete-working-examples)

---

## Module Overview

```python
import zenoh
```

Zenoh is a Zero Overhead Pub/Sub, Store/Query, and Compute protocol. The Python binding exposes the full Zenoh API through a native Rust extension compiled with PyO3.

**Key design points:**

- All sessions, publishers, subscribers, and other declared entities should be managed with a `with` statement (context manager) or explicitly closed/undeclared to avoid resource leaks.
- Handlers control how data is received: either as a **callback** (function) or a **channel** (iterable object).
- `ZBytes` is the universal data container; use `zenoh.ext` for higher-level serialization.

---

## `zenoh.open()`

### `zenoh.open(config: Config) -> Session`

Opens a Zenoh session using the provided configuration.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `config` | `Config` | Session configuration. |

**Returns:** `Session` — An active Zenoh session.

**Raises:** `ZError` — If the session cannot be opened (e.g., invalid config, network error).

**Notes:**
- Use as a context manager (`with` statement) to ensure the session is properly closed.
- If not closed explicitly, the session may hang on exit due to finalizer ordering.

```python
import zenoh

# Recommended: context manager
with zenoh.open(zenoh.Config()) as session:
    session.put("demo/example", b"hello")

# Alternative: explicit close
session = zenoh.open(zenoh.Config())
try:
    session.put("demo/example", b"hello")
finally:
    session.close()
```

---

## Config

### `class zenoh.Config`

Holds the configuration for a Zenoh session. Configuration is stored in JSON5 format.

---

### `Config()`

```python
Config() -> Config
```

Creates a default configuration suitable for local testing and development.

```python
config = zenoh.Config()
```

---

### `Config.from_file()`

```python
@staticmethod
Config.from_file(path: str) -> Config
```

Loads configuration from a JSON5 file on disk.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `path` | `str` | Absolute or relative path to the JSON5 configuration file. |

**Returns:** `Config`

**Raises:** `ZError` — If the file cannot be read or parsed.

```python
config = zenoh.Config.from_file("/etc/zenoh/config.json5")
with zenoh.open(config) as session:
    pass
```

---

### `Config.from_json5()`

```python
@staticmethod
Config.from_json5(json5: str) -> Config
```

Parses configuration from a JSON5 string.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `json5` | `str` | A valid JSON5 string containing the Zenoh configuration. |

**Returns:** `Config`

**Raises:** `ZError` — If the string cannot be parsed.

```python
config = zenoh.Config.from_json5("""
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.10:7447"]
  }
}
""")
with zenoh.open(config) as session:
    pass
```

**Common configuration fields:**

| Field | Values | Description |
|-------|--------|-------------|
| `mode` | `"peer"`, `"client"`, `"router"` | Session mode. |
| `connect.endpoints` | `["tcp/host:port"]` | List of router endpoints to connect to. |
| `listen.endpoints` | `["tcp/0.0.0.0:7447"]` | Endpoints to listen on. |
| `scouting.multicast.enabled` | `true`/`false` | Enable multicast scouting. |

---

## Session

### `class zenoh.Session`

The central object for all Zenoh communication. Obtained by calling `zenoh.open()`. Implements the context manager protocol.

---

### `Session.close()`

```python
Session.close() -> None
```

Closes the session and releases all associated resources. All declared entities (publishers, subscribers, etc.) are automatically undeclared.

```python
session = zenoh.open(zenoh.Config())
session.close()
```

---

### `Session.put()`

```python
Session.put(
    key_expr: Union[KeyExpr, str],
    payload: Union[ZBytes, bytes, str],
    *,
    encoding: Optional[Encoding] = None,
    congestion_control: Optional[CongestionControl] = None,
    priority: Optional[Priority] = None,
    express: bool = False,
    attachment: Optional[Union[ZBytes, bytes, str]] = None,
    timestamp: Optional[Timestamp] = None,
) -> None
```

Publishes data directly from the session without declaring a publisher.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | The key expression to publish to. |
| `payload` | `ZBytes`, `bytes`, or `str` | The data payload. |
| `encoding` | `Encoding` (optional) | Encoding of the payload. |
| `congestion_control` | `CongestionControl` (optional) | How to handle network congestion. |
| `priority` | `Priority` (optional) | Message priority. |
| `express` | `bool` | If `True`, disables batching for lower latency. |
| `attachment` | `ZBytes`, `bytes`, or `str` (optional) | Optional metadata attachment. |
| `timestamp` | `Timestamp` (optional) | Optional timestamp. |

```python
with zenoh.open(zenoh.Config()) as session:
    session.put("demo/temperature", b"23.5")
    session.put("demo/status", "OK", encoding=zenoh.Encoding.TEXT_PLAIN)
```

---

### `Session.delete()`

```python
Session.delete(
    key_expr: Union[KeyExpr, str],
    *,
    congestion_control: Optional[CongestionControl] = None,
    priority: Optional[Priority] = None,
    express: bool = False,
    attachment: Optional[Union[ZBytes, bytes, str]] = None,
    timestamp: Optional[Timestamp] = None,
) -> None
```

Sends a DELETE message for a key expression, signalling that the value no longer exists.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | The key expression to delete. |
| `congestion_control` | `CongestionControl` (optional) | Congestion control setting. |
| `priority` | `Priority` (optional) | Message priority. |
| `express` | `bool` | If `True`, disables batching. |
| `attachment` | `ZBytes`, `bytes`, or `str` (optional) | Optional metadata. |
| `timestamp` | `Timestamp` (optional) | Optional timestamp. |

```python
with zenoh.open(zenoh.Config()) as session:
    session.delete("demo/temperature")
```

---

### `Session.declare_publisher()`

```python
Session.declare_publisher(
    key_expr: Union[KeyExpr, str],
    *,
    encoding: Optional[Encoding] = None,
    congestion_control: CongestionControl = CongestionControl.DROP,
    priority: Priority = Priority.DEFAULT,
    express: bool = False,
    reliability: Reliability = Reliability.RELIABLE,
) -> Publisher
```

Declares a `Publisher` for the given key expression.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | The key expression to publish on. |
| `encoding` | `Encoding` (optional) | Default encoding for all publications. |
| `congestion_control` | `CongestionControl` | How to handle congestion. Default: `DROP`. |
| `priority` | `Priority` | Message priority. Default: `DEFAULT`. |
| `express` | `bool` | Disable batching for low latency. |
| `reliability` | `Reliability` | Reliability of message delivery. |

**Returns:** `Publisher`

```python
with zenoh.open(zenoh.Config()) as session:
    publisher = session.declare_publisher("demo/sensor/temp")
    publisher.put(b"25.3")
```

---

### `Session.declare_subscriber()`

```python
Session.declare_subscriber(
    key_expr: Union[KeyExpr, str],
    handler: Union[Callable[[Sample], None], FifoChannel, RingChannel, None] = None,
) -> Subscriber
```

Declares a `Subscriber` that receives samples published to matching key expressions.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | Key expression to subscribe to. Wildcards (`*`, `**`) are supported. |
| `handler` | callable, channel, or `None` | How samples are delivered. `None` uses the default FIFO channel. A callable runs in background mode. |

**Returns:** `Subscriber`

```python
# Channel mode (iterable)
with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("demo/**")
    for sample in sub:
        print(f"[{sample.key_expr}] {sample.payload.to_string()}")

# Callback mode (background)
with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("demo/**", lambda s: print(s.payload.to_string()))
```

---

### `Session.declare_queryable()`

```python
Session.declare_queryable(
    key_expr: Union[KeyExpr, str],
    handler: Union[Callable[[Query], None], FifoChannel, RingChannel, None] = None,
    *,
    complete: bool = False,
) -> Queryable
```

Declares a `Queryable` that handles incoming queries for matching key expressions.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | Key expression this queryable handles. |
| `handler` | callable, channel, or `None` | How queries are delivered. |
| `complete` | `bool` | If `True`, declares this queryable as a complete data source. Default: `False`. |

**Returns:** `Queryable`

```python
with zenoh.open(zenoh.Config()) as session:
    queryable = session.declare_queryable("demo/service")
    for query in queryable:
        print(f"Query on: {query.key_expr}")
        query.reply(query.key_expr, b"response data")
```

---

### `Session.declare_querier()`

```python
Session.declare_querier(
    key_expr: Union[KeyExpr, str],
    *,
    target: QueryTarget = QueryTarget.BEST_MATCHING,
    consolidation: ConsolidationMode = ConsolidationMode.NONE,
    timeout: Optional[timedelta] = None,
) -> Querier
```

Declares a `Querier` for repeated querying of a fixed key expression.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | The target key expression for queries. |
| `target` | `QueryTarget` | Which queryables to target. |
| `consolidation` | `ConsolidationMode` | How to consolidate replies. |
| `timeout` | `timedelta` (optional) | Maximum wait time for replies. |

**Returns:** `Querier`

```python
with zenoh.open(zenoh.Config()) as session:
    querier = session.declare_querier("demo/service")
    replies = querier.get()
    for reply in replies:
        if reply.ok:
            print(reply.ok.payload.to_string())
```

---

### `Session.get()`

```python
Session.get(
    selector: Union[Selector, KeyExpr, str],
    handler: Union[Callable[[Reply], None], FifoChannel, RingChannel, None] = None,
    *,
    target: QueryTarget = QueryTarget.BEST_MATCHING,
    consolidation: ConsolidationMode = ConsolidationMode.NONE,
    payload: Optional[Union[ZBytes, bytes, str]] = None,
    encoding: Optional[Encoding] = None,
    timeout: Optional[timedelta] = None,
    attachment: Optional[Union[ZBytes, bytes, str]] = None,
) -> Union[ReplyReceiver, None]
```

Sends a get request (query) and retrieves replies.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `selector` | `Selector`, `KeyExpr`, or `str` | Key expression (with optional parameters) to query. |
| `handler` | callable, channel, or `None` | How replies are delivered. `None` uses the default channel. |
| `target` | `QueryTarget` | Which queryables to target. |
| `consolidation` | `ConsolidationMode` | How to consolidate replies. |
| `payload` | `ZBytes`, `bytes`, or `str` (optional) | Optional payload to send with the query. |
| `encoding` | `Encoding` (optional) | Encoding of the query payload. |
| `timeout` | `timedelta` (optional) | Time to wait for replies. |
| `attachment` | `ZBytes`, `bytes`, or `str` (optional) | Optional metadata. |

**Returns:** `ReplyReceiver` (iterable) when using channel mode; `None` when using callback mode.

```python
from datetime import timedelta
import zenoh

with zenoh.open(zenoh.Config()) as session:
    replies = session.get("demo/service", timeout=timedelta(seconds=2))
    for reply in replies:
        if reply.ok:
            print(f"Reply: {reply.ok.payload.to_string()}")
        else:
            print(f"Error: {reply.err.payload.to_string()}")
```

---

### `Session.declare_keyexpr()`

```python
Session.declare_keyexpr(key_expr: Union[KeyExpr, str]) -> KeyExpr
```

Declares a key expression with the session for optimized routing and network usage. The router maps the string to a numeric ID, reducing wire overhead.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | The key expression to declare. |

**Returns:** `KeyExpr` — A session-scoped key expression.

```python
with zenoh.open(zenoh.Config()) as session:
    ke = session.declare_keyexpr("robot/sensor/temperature")
    publisher = session.declare_publisher(ke)
```

---

### `Session.liveliness()`

```python
Session.liveliness() -> Liveliness
```

Returns the `Liveliness` object for this session, used to declare tokens, subscribers, and get queries.

**Returns:** `Liveliness`

```python
with zenoh.open(zenoh.Config()) as session:
    liveliness = session.liveliness()
    token = liveliness.declare_token("node/A")
```

---

### `Session.info()`

```python
Session.info() -> SessionInfo
```

Returns information about the current session.

**Returns:** `SessionInfo`

**`SessionInfo` attributes:**

| Attribute | Type | Description |
|-----------|------|-------------|
| `zid()` | `ZenohId` | The unique ID of this session. |
| `routers_zid()` | `List[ZenohId]` | ZIDs of connected routers. |
| `peers_zid()` | `List[ZenohId]` | ZIDs of connected peers. |

```python
with zenoh.open(zenoh.Config()) as session:
    info = session.info()
    print(f"My ZID: {info.zid()}")
```

---

## KeyExpr

### `class zenoh.KeyExpr`

Represents a validated Zenoh key expression. Key expressions form the address space of Zenoh, using `/`-separated path segments with optional wildcards.

**Wildcard syntax:**

| Wildcard | Matches |
|----------|---------|
| `*` | Any single chunk (characters between `/`) |
| `**` | Any number of chunks (including zero) |

---

### `KeyExpr(expr: str)`

```python
KeyExpr(expr: str) -> KeyExpr
```

Creates and validates a key expression. Raises `ZError` if the expression is syntactically invalid or not in canonical form.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `str` | The key expression string. |

**Raises:** `ZError` — Invalid syntax or non-canonical form.

```python
ke = zenoh.KeyExpr("robot/sensor/temperature")
ke_wildcard = zenoh.KeyExpr("robot/*/temperature")
ke_multi = zenoh.KeyExpr("robot/**")
```

---

### `KeyExpr.autocanonize()`

```python
@staticmethod
KeyExpr.autocanonize(expr: str) -> KeyExpr
```

Creates a key expression from a string, automatically converting it to canonical form if needed.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `str` | The key expression string (may be non-canonical). |

**Returns:** `KeyExpr`

```python
# Non-canonical: robot/sensor/**/*/**/**
# Canonical form: robot/sensor/*/**
ke = zenoh.KeyExpr.autocanonize("robot/sensor/**/*/**/**")
assert str(ke) == "robot/sensor/*/**"
```

---

### `KeyExpr.join()`

```python
KeyExpr.join(other: Union[KeyExpr, str]) -> KeyExpr
```

Concatenates this key expression with another, joining with a `/`.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `other` | `KeyExpr` or `str` | The segment to append. |

**Returns:** `KeyExpr`

```python
base = zenoh.KeyExpr("robot/sensor")
full = base.join("temperature")
assert str(full) == "robot/sensor/temperature"
```

---

### `KeyExpr.concat()`

```python
KeyExpr.concat(other: str) -> KeyExpr
```

Concatenates a string directly to this key expression without adding a `/`.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `other` | `str` | String to append directly. |

**Returns:** `KeyExpr`

```python
ke = zenoh.KeyExpr("robot").concat("/sensor")
assert str(ke) == "robot/sensor"
```

---

### `KeyExpr.intersects()`

```python
KeyExpr.intersects(other: Union[KeyExpr, str]) -> bool
```

Returns `True` if there exists at least one key that matches both this expression and `other`.

```python
a = zenoh.KeyExpr("robot/**")
b = zenoh.KeyExpr("robot/sensor/temp")
assert a.intersects(b)  # True
```

---

### `KeyExpr.includes()`

```python
KeyExpr.includes(other: Union[KeyExpr, str]) -> bool
```

Returns `True` if every key matched by `other` is also matched by `self`.

```python
broad = zenoh.KeyExpr("robot/**")
narrow = zenoh.KeyExpr("robot/sensor/temp")
assert broad.includes(narrow)   # True
assert not narrow.includes(broad)  # False
```

---

### `KeyExpr.__str__()`

```python
str(key_expr) -> str
```

Returns the string representation of the key expression.

```python
ke = zenoh.KeyExpr("robot/sensor")
print(str(ke))  # "robot/sensor"
```

---

## Selector & Parameters

### `class zenoh.Selector`

A `Selector` combines a `KeyExpr` with optional query parameters. It is used in `Session.get()` to address a queryable and pass additional context.

**Selector string format:** `key/expression?param1=value1;param2=value2`

---

### `Selector(key_expr, parameters=None)`

```python
Selector(
    key_expr: Union[KeyExpr, str],
    parameters: Optional[Union[Parameters, str]] = None,
) -> Selector
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | The key expression part. |
| `parameters` | `Parameters`, `str`, or `None` | Optional query parameters. |

```python
# From a selector string
sel = zenoh.Selector("demo/service?mode=fast;limit=10")

# Programmatic construction
params = zenoh.Parameters({"mode": "fast", "limit": "10"})
sel = zenoh.Selector("demo/service", params)
```

---

### `Selector.key_expr`

```python
Selector.key_expr -> KeyExpr
```

The key expression component of this selector.

---

### `Selector.parameters`

```python
Selector.parameters -> Parameters
```

The parameters component of this selector.

---

### `class zenoh.Parameters`

Represents query parameters as a key-value mapping.

```python
Parameters(mapping: Union[dict, str]) -> Parameters
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `mapping` | `dict` or `str` | Either a dictionary of string key-value pairs or a `key=value;...` string. |

```python
params = zenoh.Parameters({"format": "json", "limit": "100"})
params = zenoh.Parameters("format=json;limit=100")

# Access values
value = params.get("format")  # "json"
print(str(params))             # "format=json;limit=100"
```

**Methods:**

| Method | Returns | Description |
|--------|---------|-------------|
| `get(key: str) -> Optional[str]` | `str` or `None` | Gets a parameter value. |
| `is_empty() -> bool` | `bool` | Returns `True` if no parameters are set. |
| `__contains__(key: str) -> bool` | `bool` | Tests if a key is present. |
| `__str__() -> str` | `str` | Returns the `key=value;...` string form. |

---

## Publisher

### `class zenoh.Publisher`

Publishes data on a fixed key expression. Obtained via `Session.declare_publisher()`. Implements the context manager protocol.

---

### `Publisher.put()`

```python
Publisher.put(
    payload: Union[ZBytes, bytes, str],
    *,
    encoding: Optional[Encoding] = None,
    timestamp: Optional[Timestamp] = None,
    attachment: Optional[Union[ZBytes, bytes, str]] = None,
) -> None
```

Publishes a value on this publisher's key expression.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `payload` | `ZBytes`, `bytes`, or `str` | Data to publish. |
| `encoding` | `Encoding` (optional) | Overrides the publisher's default encoding. |
| `timestamp` | `Timestamp` (optional) | Optional timestamp. |
| `attachment` | `ZBytes`, `bytes`, or `str` (optional) | Optional metadata attachment. |

```python
with zenoh.open(zenoh.Config()) as session:
    pub = session.declare_publisher("demo/sensor")
    pub.put(b"42.0")
    pub.put("hello", encoding=zenoh.Encoding.TEXT_PLAIN)
    pub.put(b"data", attachment=b"meta")
```

---

### `Publisher.delete()`

```python
Publisher.delete(
    *,
    timestamp: Optional[Timestamp] = None,
    attachment: Optional[Union[ZBytes, bytes, str]] = None,
) -> None
```

Sends a DELETE message on this publisher's key expression, indicating the value no longer exists.

```python
with zenoh.open(zenoh.Config()) as session:
    pub = session.declare_publisher("demo/sensor")
    pub.delete()
```

---

### `Publisher.key_expr`

```python
Publisher.key_expr -> KeyExpr
```

The key expression this publisher is declared on.

---

### `Publisher.encoding`

```python
Publisher.encoding -> Encoding
```

The default encoding for this publisher.

---

### `Publisher.undeclare()`

```python
Publisher.undeclare() -> None
```

Undeclares the publisher and releases its resources.

---

### `Publisher.declare_matching_listener()`

```python
Publisher.declare_matching_listener(
    handler: Union[Callable[[MatchingStatus], None], FifoChannel, RingChannel, None] = None,
) -> MatchingListener
```

Declares a listener that is notified when the publisher's matching status changes (i.e., when subscribers appear or disappear).

```python
with zenoh.open(zenoh.Config()) as session:
    pub = session.declare_publisher("demo/topic")
    listener = pub.declare_matching_listener()
    for status in listener:
        if status.matching:
            print("Has subscribers")
        else:
            print("No subscribers")
```

---

### `Publisher.matching_status()`

```python
Publisher.matching_status() -> MatchingStatus
```

Returns the current matching status of the publisher synchronously.

```python
with zenoh.open(zenoh.Config()) as session:
    pub = session.declare_publisher("demo/topic")
    status = pub.matching_status()
    print(f"Has matching subscribers: {status.matching}")
```

---

## Subscriber

### `class zenoh.Subscriber`

Receives samples published to matching key expressions. Obtained via `Session.declare_subscriber()`. Implements both the context manager and iterator protocols when used with a channel handler.

---

### `Subscriber.recv()`

```python
Subscriber.recv() -> Sample
```

Blocks until a sample is available and returns it. Only available when using a channel handler (not callback mode).

**Returns:** `Sample`

**Raises:** `ZError` — If the subscriber has been undeclared.

```python
with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("demo/**")
    sample = sub.recv()
    print(sample.payload.to_string())
```

---

### `Subscriber.try_recv()`

```python
Subscriber.try_recv() -> Optional[Sample]
```

Attempts to receive a sample without blocking. Returns `None` if no sample is immediately available.

**Returns:** `Sample` or `None`

```python
with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("demo/**")
    sample = sub.try_recv()
    if sample is not None:
        print(sample.payload.to_string())
```

---

### `Subscriber.__iter__()`

```python
for sample in subscriber:
    ...
```

Iterates over incoming samples. Blocks waiting for each sample. The loop ends when the subscriber is undeclared or the session is closed.

```python
with zenoh.open(zenoh.Config()) as session:
    with session.declare_subscriber("demo/**") as sub:
        for sample in sub:
            print(f"{sample.key_expr}: {sample.payload.to_string()}")
```

---

### `Subscriber.handler`

```python
Subscriber.handler -> Any
```

Returns the underlying handler object (the channel or custom handler passed during declaration).

---

### `Subscriber.undeclare()`

```python
Subscriber.undeclare() -> None
```

Undeclares the subscriber and releases its resources. After this call, no more samples will be delivered.

---

### `Subscriber.key_expr`

```python
Subscriber.key_expr -> KeyExpr
```

The key expression this subscriber is declared on.

---

## Queryable & Query

### `class zenoh.Queryable`

Handles incoming queries for a declared key expression. Obtained via `Session.declare_queryable()`. Implements the context manager and iterator protocols.

---

### `Queryable.__iter__()`

```python
for query in queryable:
    ...
```

Iterates over incoming queries when using a channel handler.

---

### `Queryable.recv()`

```python
Queryable.recv() -> Query
```

Blocks until a query is received.

---

### `Queryable.try_recv()`

```python
Queryable.try_recv() -> Optional[Query]
```

Non-blocking receive; returns `None` if no query is pending.

---

### `Queryable.undeclare()`

```python
Queryable.undeclare() -> None
```

Undeclares the queryable.

---

### `class zenoh.Query`

Represents an incoming query received by a `Queryable`. Provides methods to send replies.

---

### `Query.key_expr`

```python
Query.key_expr -> KeyExpr
```

The key expression of the incoming query.

---

### `Query.selector`

```python
Query.selector -> Selector
```

The full selector including both key expression and parameters.

---

### `Query.parameters`

```python
Query.parameters -> Parameters
```

The query parameters (the part after `?` in the selector).

---

### `Query.payload`

```python
Query.payload -> Optional[ZBytes]
```

Optional payload sent with the query (used for query-with-value patterns).

---

### `Query.encoding`

```python
Query.encoding -> Optional[Encoding]
```

Encoding of the query payload, if present.

---

### `Query.attachment`

```python
Query.attachment -> Optional[ZBytes]
```

Optional metadata attachment on the query.

---

### `Query.reply()`

```python
Query.reply(
    key_expr: Union[KeyExpr, str],
    payload: Union[ZBytes, bytes, str],
    *,
    encoding: Optional[Encoding] = None,
    timestamp: Optional[Timestamp] = None,
    attachment: Optional[Union[ZBytes, bytes, str]] = None,
) -> None
```

Sends a `PUT` reply to the querier.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` or `str` | The key expression for the reply. |
| `payload` | `ZBytes`, `bytes`, or `str` | Reply data. |
| `encoding` | `Encoding` (optional) | Encoding of the reply payload. |
| `timestamp` | `Timestamp` (optional) | Optional timestamp. |
| `attachment` | `ZBytes`, `bytes`, or `str` (optional) | Optional metadata. |

```python
with zenoh.open(zenoh.Config()) as session:
    queryable = session.declare_queryable("demo/temperature")
    for query in queryable:
        query.reply(query.key_expr, b"23.5")
```

---

### `Query.reply_del()`

```python
Query.reply_del(
    key_expr: Union[KeyExpr, str],
    *,
    timestamp: Optional[Timestamp]