# Zenoh Python API Reference

**Version:** 1.7.x  
**Package:** `eclipse-zenoh` (`import zenoh`)

---

## Table of Contents

1. [Module-level Functions](#module-level-functions)
2. [Config](#config)
3. [Session](#session)
4. [KeyExpr](#keyexpr)
5. [Selector & Parameters](#selector--parameters)
6. [Publisher](#publisher)
7. [Subscriber](#subscriber)
8. [Queryable & Query](#queryable--query)
9. [Querier](#querier)
10. [Sample](#sample)
11. [ZBytes](#zbytes)
12. [Encoding](#encoding)
13. [Reply & ReplyError](#reply--replyerror)
14. [Liveliness](#liveliness)
15. [Handlers](#handlers)
16. [Matching](#matching)
17. [Scouting](#scouting)
18. [Timestamps & Identifiers](#timestamps--identifiers)
19. [zenoh.ext — Serialization](#zenohext--serialization)
20. [Error Types](#error-types)
21. [Complete Working Examples](#complete-working-examples)

---

## Module-level Functions

### `zenoh.open()`

```python
def open(config: Config) -> Session
```

Opens a Zenoh session with the given configuration. The recommended pattern is to use the session as a context manager with a `with` statement to ensure proper cleanup.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `config` | `Config` | Session configuration object |

**Returns:** `Session` — An active Zenoh session.

**Raises:** `ZError` if the session cannot be opened (e.g., invalid config, network error).

> ⚠️ **Warning:** If you do not use a context manager (`with` statement) or explicitly call `session.close()`, the script may hang on exit because finalizers may run after the library thread has been terminated.

```python
import zenoh

# Recommended: context manager
with zenoh.open(zenoh.Config()) as session:
    # use session here
    pass

# Alternative: explicit close
session = zenoh.open(zenoh.Config())
try:
    pass  # use session
finally:
    session.close()
```

---

### `zenoh.scout()`

```python
def scout(
    what: WhatAmI | int = WhatAmI.Peer | WhatAmI.Router,
    config: Config | None = None,
    timeout: float = 1.0,
) -> Scout
```

Scouts for Zenoh nodes on the network. Returns a `Scout` object that yields `Hello` messages.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `what` | `WhatAmI` | Which types of nodes to scout for |
| `config` | `Config \| None` | Optional configuration; default config used if `None` |
| `timeout` | `float` | Timeout in seconds |

**Returns:** `Scout` — An iterable of `Hello` messages.

```python
import zenoh

scout = zenoh.scout(what=zenoh.WhatAmI.Peer | zenoh.WhatAmI.Router, timeout=2.0)
for hello in scout:
    print(f"Found: zid={hello.zid}, whatami={hello.whatami}")
    print(f"  Locators: {hello.locators}")
```

---

## Config

The `Config` class holds the configuration for a Zenoh session. Configuration is stored internally as JSON5 and can be loaded from files, strings, or environment variables.

### `zenoh.Config`

```python
class Config
```

Default configuration suitable for a peer that uses multicast scouting for discovery.

#### `Config()`

```python
def __init__(self) -> None
```

Creates a default configuration.

```python
config = zenoh.Config()
```

---

#### `Config.from_file()`

```python
@staticmethod
def from_file(path: str) -> Config
```

Loads configuration from a JSON5 file.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `path` | `str` | Path to the JSON5 configuration file |

**Returns:** `Config`

**Raises:** `ZError` if the file cannot be read or parsed.

```python
config = zenoh.Config.from_file("/etc/zenoh/config.json5")
```

---

#### `Config.from_json5()`

```python
@staticmethod
def from_json5(json5: str) -> Config
```

Loads configuration from a JSON5 string.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `json5` | `str` | JSON5 string containing the configuration |

**Returns:** `Config`

**Raises:** `ZError` if the string cannot be parsed.

```python
config = zenoh.Config.from_json5("""
{
  mode: "peer",
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"]
  },
  scouting: {
    multicast: {
      enabled: true
    }
  }
}
""")
```

---

#### `Config.get()`

```python
def get(self, key: str) -> str | None
```

Retrieves a configuration value by its JSON path key.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` | `str` | Dot-separated path into the JSON5 config (e.g., `"mode"`) |

**Returns:** `str | None` — The JSON5-encoded value as a string, or `None` if not found.

```python
config = zenoh.Config()
mode = config.get("mode")
print(mode)  # e.g., '"peer"'
```

---

#### `Config.insert_json5()`

```python
def insert_json5(self, key: str, value: str) -> None
```

Inserts or updates a configuration value using a JSON5-encoded string.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key` | `str` | Dot-separated path into the config |
| `value` | `str` | JSON5-encoded value string |

**Raises:** `ZError` if the key or value is invalid.

```python
config = zenoh.Config()
config.insert_json5("mode", '"client"')
config.insert_json5('connect/endpoints', '["tcp/localhost:7447"]')
```

---

## Session

A `Session` represents an active connection to the Zenoh network. It is the primary object for declaring publishers, subscribers, queryables, queriers, and for performing direct put/get/delete operations.

```python
class Session
```

Sessions are created with `zenoh.open()` and should be closed explicitly or used as context managers.

---

### Session Context Manager

```python
def __enter__(self) -> Session
def __exit__(self, ...) -> None
```

Sessions support the context manager protocol. On `__exit__`, the session is automatically closed.

```python
with zenoh.open(zenoh.Config()) as session:
    # session is active here
    pass
# session is closed here
```

---

### `Session.close()`

```python
def close(self) -> None
```

Explicitly closes the session and releases all associated resources. All declared entities (publishers, subscribers, etc.) are undeclared.

```python
session = zenoh.open(zenoh.Config())
session.close()
```

---

### `Session.zid()`

```python
def zid(self) -> ZenohId
```

Returns the unique identifier of this session.

**Returns:** `ZenohId`

```python
with zenoh.open(zenoh.Config()) as session:
    print(f"Session ID: {session.zid()}")
```

---

### `Session.declare_keyexpr()`

```python
def declare_keyexpr(self, key_expr: KeyExpr | str) -> KeyExpr
```

Declares a key expression with the session for optimized routing and reduced network overhead. The returned `KeyExpr` carries a numeric identifier that routers can use to avoid transmitting the full string.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr \| str` | The key expression to declare |

**Returns:** `KeyExpr` — A declared key expression backed by a session-assigned ID.

```python
with zenoh.open(zenoh.Config()) as session:
    ke = session.declare_keyexpr("robot/sensor/temperature")
    pub = session.declare_publisher(ke)
```

---

### `Session.undeclare_keyexpr()`

```python
def undeclare_keyexpr(self, key_expr: KeyExpr) -> None
```

Undeclares a previously declared key expression.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `key_expr` | `KeyExpr` | A key expression previously returned by `declare_keyexpr` |

---

### `Session.declare_publisher()`

```python
def declare_publisher(
    self,
    key_expr: KeyExpr | str,
    *,
    encoding: Encoding | str | None = None,
    congestion_control: CongestionControl = CongestionControl.DROP,
    priority: Priority = Priority.DATA,
    express: bool = False,
    reliability: Reliability = Reliability.RELIABLE,
) -> Publisher
```

Declares a publisher for the given key expression.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `key_expr` | `KeyExpr \| str` | required | Key expression to publish on |
| `encoding` | `Encoding \| str \| None` | `None` | Default encoding for published data |
| `congestion_control` | `CongestionControl` | `DROP` | What to do when the network is congested |
| `priority` | `Priority` | `DATA` | Message priority |
| `express` | `bool` | `False` | If `True`, disables batching for lower latency |
| `reliability` | `Reliability` | `RELIABLE` | Reliability mode |

**Returns:** `Publisher`

```python
with zenoh.open(zenoh.Config()) as session:
    pub = session.declare_publisher(
        "robot/sensor/temp",
        encoding=zenoh.Encoding.APPLICATION_JSON,
        priority=zenoh.Priority.DATA_HIGH,
    )
    pub.put(zenoh.ZBytes('{"temp": 22.5}'))
```

---

### `Session.declare_subscriber()`

```python
def declare_subscriber(
    self,
    key_expr: KeyExpr | str,
    handler: Callable[[Sample], None]
            | FifoChannel
            | RingChannel
            | tuple[Callable, Any]
            | None = None,
) -> Subscriber
```

Declares a subscriber for the given key expression.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `key_expr` | `KeyExpr \| str` | required | Key expression to subscribe to (may include wildcards) |
| `handler` | callable, channel, tuple, or `None` | `None` (DefaultHandler) | How to handle incoming samples. `None` uses a default FIFO channel. A callable runs in background mode. |

**Returns:** `Subscriber`

> **Callback mode:** When `handler` is a callable, the subscriber runs in *background mode* — it remains active even if the returned object goes out of scope.

> **Channel mode:** When `handler` is a channel (or `None`), the returned `Subscriber` is iterable.

```python
# Channel mode (iterable)
with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("robot/**")
    for sample in sub:
        print(f"Received on {sample.key_expr}: {sample.payload.to_string()}")

# Callback mode (background)
def on_sample(sample: zenoh.Sample):
    print(f"Got: {sample.payload.to_string()}")

with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("robot/**", on_sample)
    import time; time.sleep(5)
```

---

### `Session.declare_queryable()`

```python
def declare_queryable(
    self,
    key_expr: KeyExpr | str,
    handler: Callable[[Query], None]
            | FifoChannel
            | RingChannel
            | None = None,
    *,
    complete: bool = False,
) -> Queryable
```

Declares a queryable that answers queries matching the given key expression.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `key_expr` | `KeyExpr \| str` | required | Key expression this queryable serves |
| `handler` | callable, channel, or `None` | `None` | How to handle incoming queries |
| `complete` | `bool` | `False` | If `True`, this queryable is considered a complete answer for the key expression (no merging with other replies) |

**Returns:** `Queryable`

```python
with zenoh.open(zenoh.Config()) as session:
    queryable = session.declare_queryable("service/temperature")
    for query in queryable:
        print(f"Query on: {query.key_expr}")
        query.reply(query.key_expr, zenoh.ZBytes("22.5"))
```

---

### `Session.declare_querier()`

```python
def declare_querier(
    self,
    key_expr: KeyExpr | str,
    *,
    target: QueryTarget = QueryTarget.BEST_MATCHING,
    consolidation: ConsolidationMode = ConsolidationMode.NONE,
    timeout: float = 10.0,
    accept_replies: ReplyKeyExpr = ReplyKeyExpr.ANY,
) -> Querier
```

Declares a querier for repeated queries on the same key expression.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `key_expr` | `KeyExpr \| str` | required | Key expression to query |
| `target` | `QueryTarget` | `BEST_MATCHING` | Which queryables to target |
| `consolidation` | `ConsolidationMode` | `NONE` | How to consolidate replies |
| `timeout` | `float` | `10.0` | Timeout in seconds |
| `accept_replies` | `ReplyKeyExpr` | `ANY` | Which reply key expressions to accept |

**Returns:** `Querier`

```python
with zenoh.open(zenoh.Config()) as session:
    querier = session.declare_querier("service/temperature")
    replies = querier.get()
    for reply in replies:
        if reply.ok:
            print(f"Value: {reply.ok.payload.to_string()}")
```

---

### `Session.get()`

```python
def get(
    self,
    selector: Selector | KeyExpr | str,
    handler: Callable[[Reply], None]
            | FifoChannel
            | RingChannel
            | None = None,
    *,
    target: QueryTarget = QueryTarget.BEST_MATCHING,
    consolidation: ConsolidationMode = ConsolidationMode.NONE,
    timeout: float = 10.0,
    encoding: Encoding | str | None = None,
    payload: ZBytes | bytes | str | None = None,
    attachment: ZBytes | bytes | str | None = None,
) -> Receiver[Reply] | None
```

Performs an ad-hoc query without declaring a persistent querier.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `selector` | `Selector \| KeyExpr \| str` | required | Target key expression or full selector with parameters |
| `handler` | callable, channel, or `None` | `None` | Reply handler; `None` uses default FIFO channel |
| `target` | `QueryTarget` | `BEST_MATCHING` | Which queryables to target |
| `consolidation` | `ConsolidationMode` | `NONE` | How to consolidate replies |
| `timeout` | `float` | `10.0` | Timeout in seconds |
| `encoding` | `Encoding \| str \| None` | `None` | Encoding of the query payload |
| `payload` | `ZBytes \| bytes \| str \| None` | `None` | Optional query payload |
| `attachment` | `ZBytes \| bytes \| str \| None` | `None` | Optional attachment |

**Returns:** `Receiver[Reply]` when using a channel handler; `None` when using a callback.

```python
with zenoh.open(zenoh.Config()) as session:
    replies = session.get("service/temperature?unit=celsius", timeout=5.0)
    for reply in replies:
        if reply.ok:
            print(f"Reply: {reply.ok.payload.to_string()}")
        else:
            print(f"Error: {reply.err.payload.to_string()}")
```

---

### `Session.put()`

```python
def put(
    self,
    key_expr: KeyExpr | str,
    payload: ZBytes | bytes | str,
    *,
    encoding: Encoding | str | None = None,
    congestion_control: CongestionControl = CongestionControl.DROP,
    priority: Priority = Priority.DATA,
    express: bool = False,
    attachment: ZBytes | bytes | str | None = None,
    timestamp: Timestamp | None = None,
) -> None
```

Publishes data on a key expression directly from the session (without declaring a publisher).

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `key_expr` | `KeyExpr \| str` | required | Destination key expression |
| `payload` | `ZBytes \| bytes \| str` | required | Data payload |
| `encoding` | `Encoding \| str \| None` | `None` | MIME-like encoding hint |
| `congestion_control` | `CongestionControl` | `DROP` | Congestion control mode |
| `priority` | `Priority` | `DATA` | Message priority |
| `express` | `bool` | `False` | Disable batching for lower latency |
| `attachment` | `ZBytes \| bytes \| str \| None` | `None` | Optional metadata attachment |
| `timestamp` | `Timestamp \| None` | `None` | Explicit timestamp |

```python
with zenoh.open(zenoh.Config()) as session:
    session.put("robot/status", b"online", encoding=zenoh.Encoding.TEXT_PLAIN)
```

---

### `Session.delete()`

```python
def delete(
    self,
    key_expr: KeyExpr | str,
    *,
    congestion_control: CongestionControl = CongestionControl.DROP,
    priority: Priority = Priority.DATA,
    express: bool = False,
    attachment: ZBytes | bytes | str | None = None,
    timestamp: Timestamp | None = None,
) -> None
```

Publishes a deletion on a key expression. Subscribers will receive a `Sample` with `kind == SampleKind.DELETE`.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `key_expr` | `KeyExpr \| str` | required | Key expression to delete |
| `congestion_control` | `CongestionControl` | `DROP` | Congestion control mode |
| `priority` | `Priority` | `DATA` | Message priority |
| `express` | `bool` | `False` | Disable batching |
| `attachment` | `ZBytes \| bytes \| str \| None` | `None` | Optional metadata attachment |
| `timestamp` | `Timestamp \| None` | `None` | Explicit timestamp |

```python
with zenoh.open(zenoh.Config()) as session:
    session.delete("robot/sensor/old_value")
```

---

### `Session.liveliness()`

```python
def liveliness(self) -> Liveliness
```

Returns the `Liveliness` API object associated with this session.

**Returns:** `Liveliness`

```python
with zenoh.open(zenoh.Config()) as session:
    lv = session.liveliness()
    token = lv.declare_token("node/myapp")
```

---

### `Session.info()`

```python
def info(self) -> SessionInfo
```

Returns information about the session.

**Returns:** `SessionInfo` — contains `zid()`, `routers_zid()`, `peers_zid()`.

```python
with zenoh.open(zenoh.Config()) as session:
    info = session.info()
    print(f"My ZID: {info.zid()}")
    print(f"Routers: {list(info.routers_zid())}")
```

---

## KeyExpr

Key expressions are Zenoh's address space. They are slash-separated paths that can contain wildcards:

- `*` — matches any single chunk (segment between `/`)
- `**` — matches any number of chunks (including zero)

```python
class KeyExpr
```

---

### `KeyExpr()`

```python
def __init__(self, expr: str) -> None
```

Creates a validated key expression from a string. Raises `ZError` if the syntax is invalid or not in canonical form.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `str` | The key expression string |

**Raises:** `ZError` for invalid syntax or non-canonical form (use `autocanonize` instead).

```python
ke = zenoh.KeyExpr("robot/sensor/temperature")
wildcard_ke = zenoh.KeyExpr("robot/*/temperature")
deep_wildcard = zenoh.KeyExpr("robot/**")
```

---

### `KeyExpr.autocanonize()`

```python
@staticmethod
def autocanonize(expr: str) -> KeyExpr
```

Creates a key expression and automatically converts it to canonical form. Use this when the expression may not be in canonical form (e.g., `a/**/*` → `a/*/**`).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `expr` | `str` | Key expression string, possibly non-canonical |

**Returns:** `KeyExpr` in canonical form.

```python
ke = zenoh.KeyExpr.autocanonize("robot/sensor/**/*/**")
print(ke)  # "robot/sensor/*/**"
```

---

### `KeyExpr.intersects()`

```python
def intersects(self, other: KeyExpr | str) -> bool
```

Returns `True` if this key expression and `other` have at least one key in common (i.e., there exists a concrete key that both expressions match).

```python
a = zenoh.KeyExpr("robot/**")
b = zenoh.KeyExpr("robot/sensor/temperature")
print(a.intersects(b))   # True
print(b.intersects("other/key"))  # False
```

---

### `KeyExpr.includes()`

```python
def includes(self, other: KeyExpr | str) -> bool
```

Returns `True` if every key matched by `other` is also matched by `self` (i.e., `self` is a superset of `other`).

```python
a = zenoh.KeyExpr("robot/**")
b = zenoh.KeyExpr("robot/sensor/temperature")
print(a.includes(b))  # True
print(b.includes(a))  # False
```

---

### `KeyExpr.join()`

```python
def join(self, suffix: str) -> KeyExpr
```

Appends a suffix to this key expression with an intervening `/` separator.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `suffix` | `str` | Suffix to append |

**Returns:** New `KeyExpr`

```python
base = zenoh.KeyExpr("robot/sensor")
temp = base.join("temperature")  # "robot/sensor/temperature"
all_ = base.join("**")           # "robot/sensor/**"
```

---

### `KeyExpr.concat()`

```python
def concat(self, suffix: str) -> KeyExpr
```

Concatenates a suffix **without** adding a `/` separator. Useful for building expressions like `sensor_*`.

```python
ke = zenoh.KeyExpr("robot/sensor_").concat("temp")  # "robot/sensor_temp"
```

---

### `KeyExpr.__str__()`

```python
def __str__(self) -> str
```

Returns the string representation.

```python
ke = zenoh.KeyExpr("a/b/c")
print(str(ke))  # "a/b/c"
```

---

### `KeyExpr.__eq__()` / `__hash__()`

`KeyExpr` supports equality comparison and can be used in sets and as dictionary keys.

```python
ke1 = zenoh.KeyExpr("a/b")
ke2 = zenoh.KeyExpr("a/b")
assert ke1 == ke2
```

---

## Selector & Parameters

### `Selector`

A `Selector` combines a `KeyExpr` with optional parameters (similar to a URL path + query string). Used with `Session.get()`.

```python
class Selector
```

#### `Selector()`

```python
def __init__(self, selector: str) -> None
```

Parses a selector string of the form `key/expression?param1=value1;param2=value2`.

```python
sel = zenoh.Selector("service/temperature?unit=celsius;format=json")
```

---

#### `Selector.key_expr`

```python
@property
def key_expr(self) -> KeyExpr
```

The key expression part of the selector.

---

#### `Selector.parameters`

```python
@property
def parameters(self) -> Parameters
```

The parameters part of the selector.

---

### `Parameters`

```python
class Parameters
```

Holds the parameters part of a selector (the portion after `?`).

#### `Parameters()`

```python
def __init__(self, params: str | dict[str, str]) -> None
```

Creates parameters from a semicolon-separated string or a dictionary.

```python
# From string
params = zenoh.Parameters("unit=celsius;format=json")

# From dict
params = zenoh.Parameters({"unit": "celsius", "format": "json"})
```

---

#### `Parameters.get()`

```python
def get(self, key: str) -> str | None
```

Retrieves the value of a named parameter.

---

#### `Parameters.__str__()`

Returns the parameters as a `key=value;...` string.

---

#### Combining `KeyExpr` + `Parameters` into a `Selector`

```python
ke = zenoh.KeyExpr("service/temperature")
params = zenoh.Parameters({"unit": "celsius"})
# Pass as a string selector:
replies = session.get(f"{ke}?{params}")
```

---

## Publisher

A `Publisher` is a long-lived entity for repeatedly publishing data on a fixed key expression. Declared via `Session.declare_publisher()`.

```python
class Publisher
```

---

### `Publisher.put()`

```python
def put(
    self,
    payload: ZBytes | bytes | str,
    *,
    encoding: Encoding | str | None = None,
    timestamp: Timestamp | None = None,
    attachment: ZBytes | bytes | str | None = None,
) -> None
```

Publishes a value. The key expression, priority, and congestion control are those set at declaration time, but can be overridden per-call for encoding, timestamp, and attachment.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `payload` | `ZBytes \| bytes \| str` | required | Data to publish |
| `encoding` | `Encoding \| str \| None` | Publisher's default | MIME-like encoding hint |
| `timestamp` | `Timestamp \| None` | `None` | Override timestamp |
| `attachment` | `ZBytes \| bytes \| str \| None` | `None` | Optional metadata |

```python
pub.put(b"hello world")
pub.put("hello", encoding=zenoh.Encoding.TEXT_PLAIN)
pub.put(
    zenoh.ZBytes(b"\x01\x02"),
    encoding=zenoh.Encoding.APPLICATION_OCTET_STREAM,
    attachment=zenoh.ZBytes("meta"),
)
```

---

### `Publisher.delete()`

```python
def delete(
    self,
    *,
    timestamp: Timestamp | None = None,
    attachment: ZBytes | bytes | str | None = None,
) -> None
```

Publishes a deletion event on this publisher's key expression.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `timestamp` | `Timestamp \| None` | `None` | Override timestamp |
| `attachment` | `ZBytes \| bytes \| str \| None` | `None` | Optional metadata |

```python
pub.delete()
```

---

### `Publisher.key_expr`

```python
@property
def key_expr(self) -> KeyExpr
```

The key expression this publisher publishes on.

---

### `Publisher.encoding`

```python
@property
def encoding(self) -> Encoding
```

The default encoding for this publisher.

---

### `Publisher.declare_matching_listener()`

```python
def declare_matching_listener(
    self,
    handler: Callable[[MatchingStatus], None]
            | FifoChannel
            | RingChannel
            | None = None,
) -> MatchingListener
```

Declares a listener that notifies when the publisher's matching status changes (i.e., when a matching subscriber appears or disappears).

**Returns:** `MatchingListener`

```python
pub = session.declare_publisher("key/expr")
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
def matching_status(self) -> MatchingStatus
```

Returns the current matching status (whether there are matching subscribers).

---

### `Publisher.undeclare()`

```python
def undeclare(self) -> None
```

Explicitly undeclares the publisher, releasing its resources.

---

## Subscriber

A `Subscriber` receives data published on matching key expressions. Declared via `Session.declare_subscriber()`.

```python
class Subscriber
```

---

### `Subscriber.recv()`

```python
def recv(self) -> Sample
```

Blocks until a sample is received and returns it. Only available when using a channel handler.

**Returns:** `Sample`

**Raises:** `ZError` if the subscriber has been undeclared.

```python
sub = session.declare_subscriber("robot/**")
sample = sub.recv()
print(sample.payload.to_string())
```

---

### `Subscriber.try_recv()`

```python
def try_recv(self) -> Sample | None
```

Attempts a non-blocking receive. Returns `None` if no sample is immediately available.

```python
sample = sub.try_recv()
if sample is not None:
    print(sample.payload.to_string())
```

---

### `Subscriber.__iter__()`

```python
def __iter__(self) -> Iterator[Sample]
```

Iterates over received samples, blocking between each. The iteration ends when the subscriber is undeclared or the session is closed.

```python
sub = session.declare_subscriber("robot/**")
for sample in sub:
    print(f"{sample.key_expr}: {sample.payload.to_string()}")
```

---

### `Subscriber.handler`

```python
@property
def handler(self) -> Any
```

Returns the underlying handler object (channel or custom handler). Useful when using a custom channel.

```python
sub = session.declare_subscriber("key/expr", (channel.send, channel))
received = sub.handler.recv()
```

---

### `Subscriber.key_expr`

```python
@property
def key_expr(self) -> KeyExpr
```

The key expression this subscriber is subscribed to.

---

### `Subscriber.undeclare()`

```python
def undeclare(self) -> None
```

Explicitly undeclares the subscriber. This also stops the iteration in `__iter__`.

---

## Queryable & Query

### `Queryable`