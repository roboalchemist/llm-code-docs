# Zenoh Serialization Documentation

## Table of Contents
1. [ZBytes: The Payload Container](#zbytes)
2. [Encoding](#encoding)
3. [zenoh-ext Serialization Helpers](#zenoh-ext)
4. [Examples](#examples)
5. [Language Binding Differences](#language-bindings)
6. [CDR and ROS 2 Interop](#cdr)

---

## ZBytes: The Payload Container

`ZBytes` is zenoh's opaque, zero-copy byte buffer. It is the fundamental type for all payload data flowing through zenoh — every published message, query payload, and reply body is carried as a `ZBytes`.

### What ZBytes Is

`ZBytes` makes no assumptions about the content of the bytes it holds. It is deliberately opaque: the type system does not tell you whether the bytes are UTF-8 text, a serialized struct, a raw sensor reading, or anything else. That information is conveyed separately via `Encoding` (see below).

`ZBytes` is designed for zero-copy operation. When you create a `ZBytes` from a `Vec<u8>`, the buffer is moved rather than copied. When zenoh receives data from the network, it can hand you a `ZBytes` that references the underlying network buffer directly, avoiding an extra allocation.

`ZBytes` is a **non-exhaustive** type. Do not pattern-match on its internal structure; always interact with it through its provided methods.

### Creating ZBytes

```rust
use zenoh::bytes::ZBytes;

// From a byte slice (copies the data)
let bytes: ZBytes = ZBytes::from(b"hello".as_slice());

// From a Vec<u8> (moves the data, no copy)
let vec: Vec<u8> = vec![1, 2, 3, 4];
let bytes: ZBytes = ZBytes::from(vec);

// From a String (moves the data)
let s = String::from("hello zenoh");
let bytes: ZBytes = ZBytes::from(s);

// From a &str (copies the data)
let bytes: ZBytes = ZBytes::from("hello zenoh");

// From a number — converts to little-endian bytes
let bytes: ZBytes = ZBytes::from(42u32);

// Empty payload
let bytes: ZBytes = ZBytes::default();
```

When using `zenoh-ext`, the `z_serialize` helper provides a uniform interface:

```rust
use zenoh_ext::z_serialize;

let bytes = z_serialize(&42u32);
let bytes = z_serialize(&"hello");
let bytes = z_serialize(&vec![1u8, 2, 3]);
```

### Extracting Data from ZBytes

Reading back from `ZBytes` is done through typed deserialization:

```rust
use zenoh::bytes::ZBytes;

let bytes = ZBytes::from("hello zenoh");

// Extract as a Cow<str> — zero-copy if the bytes are contiguous UTF-8
let text: std::borrow::Cow<str> = bytes.try_into().unwrap();
println!("{}", text);

// Extract as Vec<u8>
let bytes = ZBytes::from(vec![1u8, 2, 3]);
let raw: Vec<u8> = bytes.into();

// Extract a number
let bytes = ZBytes::from(42u32);
let n: u32 = bytes.try_into().unwrap();
```

Using `zenoh-ext`:

```rust
use zenoh_ext::z_deserialize;

let bytes = ZBytes::from(42u32);
let n: u32 = z_deserialize(&bytes).unwrap();

let bytes = ZBytes::from("hello");
let s: String = z_deserialize(&bytes).unwrap();
```

### Iterating Over Raw Bytes

`ZBytes` may be internally fragmented (e.g., composed of multiple network buffers). Always use the iterator interface rather than assuming contiguity:

```rust
use zenoh::bytes::ZBytes;

let bytes = ZBytes::from(vec![1u8, 2, 3, 4, 5]);

// Iterate over byte slices (each slice is a contiguous fragment)
for slice in bytes.slices() {
    println!("{:?}", slice);
}

// Collect all bytes into a contiguous Vec<u8>
let raw: Vec<u8> = bytes.into();
```

---

## Encoding

`Encoding` is a MIME-type-like label attached to a `ZBytes` payload. It is metadata: zenoh does not interpret or enforce it. Its purpose is to let subscribers and queryables understand how to deserialize the payload they receive.

### What Encoding Is

An `Encoding` value is a string identifier, optionally with a schema suffix separated by a semicolon. Examples:

- `application/octet-stream`
- `text/plain;charset=utf-8`
- `application/json`
- `application/cbor`

`Encoding` travels alongside the payload in every `Sample`. The sender sets it; the receiver reads it.

### Predefined Encodings

`zenoh` provides constants for common encodings in `Encoding`:

```rust
use zenoh::bytes::Encoding;

// Raw bytes — no interpretation
let enc = Encoding::APPLICATION_OCTET_STREAM;

// UTF-8 text
let enc = Encoding::TEXT_PLAIN;

// JSON
let enc = Encoding::APPLICATION_JSON;

// CBOR
let enc = Encoding::APPLICATION_CBOR;

// Protobuf
let enc = Encoding::APPLICATION_PROTOBUF;

// CDR (used for ROS 2 / DDS interop)
let enc = Encoding::APPLICATION_CDR;

// Zenoh's own serialization format (used by zenoh-ext)
let enc = Encoding::ZENOH_SERIALIZATION;
```

A complete list is available in the `zenoh::bytes::Encoding` documentation.

### Custom Encodings

Any string can be used as an encoding:

```rust
use zenoh::bytes::Encoding;

let enc = Encoding::from("application/vnd.mycompany.widget+json");
let enc = Encoding::from("application/flatbuffers");
let enc = Encoding::from("image/png");
```

### Setting Encoding When Publishing

```rust
use zenoh::bytes::Encoding;

let session = zenoh::open(zenoh::Config::default()).await.unwrap();

// Set encoding on a one-shot put
session
    .put("my/topic", serde_json::to_vec(&my_value).unwrap())
    .encoding(Encoding::APPLICATION_JSON)
    .await
    .unwrap();

// Set default encoding on a declared publisher
let publisher = session
    .declare_publisher("my/topic")
    .encoding(Encoding::APPLICATION_JSON)
    .await
    .unwrap();

publisher.put(serde_json::to_vec(&my_value).unwrap()).await.unwrap();

// Override encoding per message
publisher
    .put(payload)
    .encoding(Encoding::APPLICATION_CBOR)
    .await
    .unwrap();
```

### Checking Encoding When Receiving

```rust
use zenoh::bytes::Encoding;

let subscriber = session
    .declare_subscriber("my/topic")
    .await
    .unwrap();

while let Ok(sample) = subscriber.recv_async().await {
    let encoding = sample.encoding();
    
    if *encoding == Encoding::APPLICATION_JSON {
        let text: String = sample.payload().try_into().unwrap();
        let value: serde_json::Value = serde_json::from_str(&text).unwrap();
        println!("JSON: {:?}", value);
    } else if *encoding == Encoding::APPLICATION_OCTET_STREAM {
        let raw: Vec<u8> = sample.payload().clone().into();
        println!("raw bytes: {} bytes", raw.len());
    } else {
        println!("unknown encoding: {}", encoding);
    }
}
```

---

## zenoh-ext Serialization Helpers

The `zenoh-ext` crate provides `ZSerializer` and `ZDeserializer` for packing multiple typed values into a single `ZBytes`, and the convenience functions `z_serialize` / `z_deserialize` for single-value round-trips.

Add to `Cargo.toml`:

```toml
[dependencies]
zenoh = "1.x"
zenoh-ext = "1.x"
```

### z_serialize / z_deserialize

For single values, use the top-level functions:

```rust
use zenoh_ext::{z_serialize, z_deserialize};

// Serialize
let payload = z_serialize(&42u32);
let payload = z_serialize(&"hello world");
let payload = z_serialize(&vec![1u8, 2, 3]);
let payload = z_serialize(&true);
let payload = z_serialize(&3.14f64);

// Deserialize
let n: u32      = z_deserialize(&payload).unwrap();
let s: String   = z_deserialize(&payload).unwrap();
let v: Vec<u8>  = z_deserialize(&payload).unwrap();
let b: bool     = z_deserialize(&payload).unwrap();
let f: f64      = z_deserialize(&payload).unwrap();
```

### ZSerializer: Packing Multiple Values

`ZSerializer` writes values sequentially into a single `ZBytes`. Each call to `serialize` appends to the buffer. The resulting `ZBytes` must be deserialized in the same order with `ZDeserializer`.

```rust
use zenoh_ext::ZSerializer;

let mut serializer = ZSerializer::new();

serializer.serialize(42u32);
serializer.serialize("status");
serializer.serialize(true);
serializer.serialize(3.14f64);

let payload: zenoh::bytes::ZBytes = serializer.finish();
```

### ZDeserializer: Unpacking Multiple Values

```rust
use zenoh_ext::ZDeserializer;

let mut deserializer = ZDeserializer::new(&payload);

let id: u32         = deserializer.deserialize().unwrap();
let label: String   = deserializer.deserialize().unwrap();
let active: bool    = deserializer.deserialize().unwrap();
let value: f64      = deserializer.deserialize().unwrap();

assert!(deserializer.done()); // verify all bytes were consumed
```

### Supported Types

The following types implement zenoh-ext's `Serialize` / `Deserialize` traits:

| Type | Notes |
|------|-------|
| `u8`, `u16`, `u32`, `u64`, `u128` | Little-endian |
| `i8`, `i16`, `i32`, `i64`, `i128` | Little-endian |
| `f32`, `f64` | IEEE 754, little-endian |
| `bool` | 1 byte, 0 or 1 |
| `String` | Length-prefixed UTF-8 |
| `&str` | Length-prefixed UTF-8 (serialize only) |
| `Vec<u8>` | Length-prefixed raw bytes |
| `&[u8]` | Length-prefixed raw bytes (serialize only) |
| `Vec<T>` | Length-prefixed sequence of serialized `T` |
| `(A, B)` | Two values in order |
| `(A, B, C)` | Three values in order |

### Sequences

```rust
use zenoh_ext::ZSerializer;

let mut serializer = ZSerializer::new();

// Vec<u32> — serialized as: [length: u32][elem0: u32][elem1: u32]...
let values = vec![10u32, 20, 30, 40];
serializer.serialize(values);

let payload = serializer.finish();
```

```rust
use zenoh_ext::ZDeserializer;

let mut deserializer = ZDeserializer::new(&payload);
let values: Vec<u32> = deserializer.deserialize().unwrap();
assert_eq!(values, vec![10u32, 20, 30, 40]);
```

### Tuples

```rust
use zenoh_ext::ZSerializer;

let mut serializer = ZSerializer::new();

// Tuple (u32, String) — values written in order
serializer.serialize((42u32, String::from("hello")));

let payload = serializer.finish();
```

```rust
use zenoh_ext::ZDeserializer;

let mut deserializer = ZDeserializer::new(&payload);
let (id, label): (u32, String) = deserializer.deserialize().unwrap();
```

### Custom Types via Serde

When the `serde` feature is enabled in `zenoh-ext`, types that implement `serde::Serialize` + `serde::Deserialize` can be serialized using a configured codec (e.g., JSON, CBOR).

```toml
[dependencies]
zenoh-ext = { version = "1.x", features = ["serde", "serde_json"] }
serde = { version = "1", features = ["derive"] }
```

```rust
use serde::{Serialize, Deserialize};
use zenoh_ext::{z_serialize, z_deserialize};

#[derive(Serialize, Deserialize, Debug, PartialEq)]
struct SensorReading {
    sensor_id: u32,
    temperature: f64,
    humidity: f64,
    label: String,
}

let reading = SensorReading {
    sensor_id: 7,
    temperature: 22.5,
    humidity: 60.0,
    label: "office".to_string(),
};

// Serialize using the serde codec
let payload = z_serialize(&reading);

// Deserialize
let decoded: SensorReading = z_deserialize(&payload).unwrap();
assert_eq!(reading, decoded);
```

---

## Examples

### 1. Publishing a Plain String

```rust
use zenoh::bytes::Encoding;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    session
        .put("sensors/temperature", "23.4 C")
        .encoding(Encoding::TEXT_PLAIN)
        .await
        .unwrap();

    println!("Published temperature string.");
}
```

### 2. Publishing JSON

```rust
use zenoh::bytes::Encoding;
use serde_json::json;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    let data = json!({
        "sensor_id": 42,
        "temperature": 22.5,
        "unit": "celsius"
    });

    let payload = serde_json::to_vec(&data).unwrap();

    session
        .put("sensors/data", payload)
        .encoding(Encoding::APPLICATION_JSON)
        .await
        .unwrap();

    println!("Published JSON payload.");
}
```

On the subscriber side:

```rust
let subscriber = session.declare_subscriber("sensors/data").await.unwrap();

while let Ok(sample) = subscriber.recv_async().await {
    if *sample.encoding() == Encoding::APPLICATION_JSON {
        let raw: Vec<u8> = sample.payload().clone().into();
        let value: serde_json::Value = serde_json::from_slice(&raw).unwrap();
        println!("Received JSON: {:?}", value);
    }
}
```

### 3. Multi-Field Message with ZSerializer

Pack a structured message without defining a schema:

```rust
use zenoh::bytes::Encoding;
use zenoh_ext::ZSerializer;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    let mut s = ZSerializer::new();
    s.serialize(7u32);           // device ID
    s.serialize("pressure");     // metric name
    s.serialize(101325.0f64);    // value
    s.serialize(true);           // valid flag
    let payload = s.finish();

    session
        .put("devices/reading", payload)
        .encoding(Encoding::ZENOH_SERIALIZATION)
        .await
        .unwrap();
}
```

### 4. Reading a Structured Message with ZDeserializer

```rust
use zenoh::bytes::Encoding;
use zenoh_ext::ZDeserializer;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();
    let subscriber = session.declare_subscriber("devices/reading").await.unwrap();

    while let Ok(sample) = subscriber.recv_async().await {
        if *sample.encoding() != Encoding::ZENOH_SERIALIZATION {
            eprintln!("Unexpected encoding: {}", sample.encoding());
            continue;
        }

        let mut d = ZDeserializer::new(sample.payload());

        let device_id: u32  = d.deserialize().unwrap();
        let metric: String  = d.deserialize().unwrap();
        let value: f64      = d.deserialize().unwrap();
        let valid: bool     = d.deserialize().unwrap();

        assert!(d.done(), "unexpected trailing bytes");

        println!(
            "Device {}: {} = {} (valid={})",
            device_id, metric, value, valid
        );
    }
}
```

### 5. Custom Type Serialization (Full Round-Trip)

```rust
use serde::{Serialize, Deserialize};
use zenoh::bytes::Encoding;
use zenoh_ext::{z_serialize, z_deserialize};

#[derive(Serialize, Deserialize, Debug, PartialEq)]
struct Pose {
    x: f64,
    y: f64,
    heading_deg: f32,
}

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    // Publisher
    let publisher = session
        .declare_publisher("robot/pose")
        .encoding(Encoding::ZENOH_SERIALIZATION)
        .await
        .unwrap();

    let pose = Pose { x: 1.0, y: 2.5, heading_deg: 90.0 };
    publisher.put(z_serialize(&pose)).await.unwrap();

    // Subscriber
    let subscriber = session.declare_subscriber("robot/pose").await.unwrap();

    if let Ok(sample) = subscriber.recv_async().await {
        let received: Pose = z_deserialize(sample.payload()).unwrap();
        println!("Received pose: {:?}", received);
        assert_eq!(pose, received);
    }
}
```

---

## Language Binding Differences

### Rust

Rust uses `ZBytes` directly, with `zenoh-ext` providing `ZSerializer`/`ZDeserializer` and the `z_serialize`/`z_deserialize` convenience functions. Serde integration is available as a cargo feature.

```rust
// Cargo.toml
// zenoh = "1.x"
// zenoh-ext = { version = "1.x", features = ["serde", "serde_json"] }

use zenoh_ext::{z_serialize, z_deserialize};

let payload = z_serialize(&42u32);
let value: u32 = z_deserialize(&payload).unwrap();
```

### Python

The Python bindings expose `ZBytes` and provide helpers that wrap common Python types:

```python
import zenoh

session = zenoh.open(zenoh.Config())

# String payload
session.put("my/key", "hello from python")

# Bytes payload
session.put("my/key", bytes([1, 2, 3, 4]))

# On receive
def callback(sample):
    # payload is a ZBytes — convert to bytes
    raw: bytes = bytes(sample.payload)
    text: str = sample.payload.decode("utf-8")  # if text
    print(f"Received: {text}")

sub = session.declare_subscriber("my/key", callback)
```

For structured data, Python users typically serialize with `json`, `msgpack`, or `struct` before passing bytes to zenoh:

```python
import json, zenoh
from zenoh import Encoding

data = {"sensor": 1, "value": 42.0}
payload = json.dumps(data).encode("utf-8")
session.put("sensors/data", payload, encoding=Encoding.APPLICATION_JSON())
```

### C

The C API uses `z_bytes_t` and requires manual serialization. There is no built-in serialization framework; users bring their own (e.g., nanopb for protobuf, a hand-rolled packer, etc.).

```c
#include "zenoh.h"

// Publish raw bytes
z_owned_session_t session;
z_open(&session, z_move(config), NULL);

const char *msg = "hello from C";
z_view_bytes_t payload;
z_view_bytes_from_buf(&payload, (const uint8_t *)msg, strlen(msg));

z_publisher_put_options_t opts;
z_publisher_put_options_default(&opts);

z_publisher_put(z_loan(pub), z_loan(payload), &opts);

// Receive
void data_handler(z_loaned_sample_t *sample, void *arg) {
    z_view_string_t key_str;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key_str);

    z_bytes_slice_iterator_t iter = z_bytes_get_slice_iterator(z_sample_payload(sample));
    z_view_slice_t slice;
    while (z_bytes_slice_iterator_next(&iter, &slice)) {
        // process slice.data, slice.len
    }
}
```

For structured data in C, use an external serialization library and pass the resulting byte buffer to zenoh.

### TypeScript / JavaScript

The TypeScript bindings use `Uint8Array` as the payload type. JSON is the most common approach for structured data:

```typescript
import zenoh from "@eclipse-zenoh/zenoh-ts";

const session = await zenoh.open(new zenoh.Config());

// Publish a string
const encoder = new TextEncoder();
await session.put("my/topic", encoder.encode("hello from typescript"));

// Publish JSON
const data = { sensor: 1, value: 42.0 };
const payload = encoder.encode(JSON.stringify(data));
await session.put("sensors/data", payload, {
    encoding: zenoh.Encoding.APPLICATION_JSON,
});

// Subscribe
const subscriber = await session.declareSubscriber("my/topic");
for await (const sample of subscriber.receiver()) {
    const decoder = new TextDecoder();
    const text = decoder.decode(sample.payload());
    console.log("Received:", text);
}
```

---

## CDR and ROS 2 Interop

### What CDR Is

CDR (Common Data Representation) is the binary serialization format used by OMG DDS and ROS 2. It encodes structs, arrays, strings, and primitives in a platform-aware format with alignment padding. All ROS 2 messages on the wire use CDR.

### Using zenoh-plugin-ros2dds

When bridging between ROS 2 and zenoh via `zenoh-plugin-ros2dds`, CDR encoding and decoding are handled automatically. ROS 2 messages arrive at the plugin as CDR-encoded `ZBytes`, and are forwarded to zenoh subscribers with `Encoding::APPLICATION_CDR`. In the reverse direction, the plugin decodes CDR from zenoh payloads and publishes them to the DDS bus.

No manual CDR handling is required when using the plugin.

### Manual CDR

If you need to manually produce or consume CDR payloads — for example, when communicating with a ROS 2 node directly without the plugin — use a CDR library:

```toml
[dependencies]
cdr = "0.2"
```

```rust
use zenoh::bytes::{Encoding, ZBytes};
use cdr::{CdrLe, Infinite};
use serde::{Serialize, Deserialize};

// A ROS 2-compatible message type
#[derive(Serialize, Deserialize, Debug)]
struct Twist {
    linear_x: f64,
    linear_y: f64,
    angular_z: f64,
}

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    let cmd = Twist {
        linear_x: 0.5,
        linear_y: 0.0,
        angular_z: 0.1,
    };

    // Serialize to CDR (little-endian, with 4-byte header)
    let cdr_bytes = cdr::serialize::<_, _, CdrLe>(&cmd, Infinite).unwrap();
    let payload = ZBytes::from(cdr_bytes);

    session
        .put("rt/cmd_vel", payload)
        .encoding(Encoding::APPLICATION_CDR)
        .await
        .unwrap();

    // Receive and decode CDR
    let subscriber = session
        .declare_subscriber("rt/cmd_vel")
        .await
        .unwrap();

    if let Ok(sample) = subscriber.recv_async().await {
        if *sample.encoding() == Encoding::APPLICATION_CDR {
            let raw: Vec<u8> = sample.payload().clone().into();
            let twist: Twist = cdr::deserialize::<Twist>(&raw).unwrap();
            println!("Received Twist: {:?}", twist);
        }
    }
}
```

### CDR Encoding Notes

- CDR uses native or explicit endianness. ROS 2 defaults to little-endian (XCDR version 1).
- The first 4 bytes of a CDR buffer are a representation identifier header: `[0x00, 0x01, 0x00, 0x00]` for little-endian.
- String fields are null-terminated and length-prefixed in CDR.
- When setting encoding on CDR payloads destined for ROS 2, use `Encoding::APPLICATION_CDR`.

---

## Summary

| Task | API |
|------|-----|
| Publish raw bytes | `session.put(key, bytes)` |
| Publish with encoding | `.put(key, bytes).encoding(Encoding::APPLICATION_JSON)` |
| Serialize one value | `z_serialize(&value)` |
| Deserialize one value | `z_deserialize::<T>(&zbytes)` |
| Pack multiple values | `ZSerializer::new()` → `s.serialize(v)` → `s.finish()` |
| Unpack multiple values | `ZDeserializer::new(&zbytes)` → `d.deserialize::<T>()` |
| Custom struct (serde) | `z_serialize(&my_struct)` with serde feature |
| Check payload encoding | `sample.encoding()` |
| ROS 2 / CDR interop | `zenoh-plugin-ros2dds` or manual `cdr` crate |