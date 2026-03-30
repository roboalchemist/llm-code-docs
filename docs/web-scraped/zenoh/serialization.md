# Zenoh Serialization Documentation

## Table of Contents

1. [ZBytes: The Payload Container](#zbytes)
2. [Encoding](#encoding)
3. [zenoh-ext Serialization Helpers](#zenoh-ext)
4. [Examples](#examples)
5. [Language Binding Differences](#language-bindings)
6. [CDR and ROS 2 Interop](#cdr)

---

## ZBytes: The Payload Container {#zbytes}

`ZBytes` is the fundamental payload container in zenoh. It is an opaque, reference-counted byte buffer designed for zero-copy data transport across the network. Every published value, query payload, and reply body is carried in a `ZBytes`.

### Key Properties

- **Opaque**: Internal representation is not part of the public API. Always access contents via the provided methods.
- **Zero-copy**: Backed by a reference-counted buffer; cloning is cheap and avoids memory copies where possible.
- **Non-exhaustive**: The type is `#[non_exhaustive]`. Never match on its internals; always use conversion methods.
- **Composable**: Multiple logical values can be packed into a single `ZBytes` using `ZSerializer`.

### Creating ZBytes

```rust
use zenoh::bytes::ZBytes;

// From a byte slice
let bytes: ZBytes = ZBytes::from(b"hello".as_slice());

// From a Vec<u8>
let bytes: ZBytes = ZBytes::from(vec![1u8, 2, 3, 4]);

// From a String or &str
let bytes: ZBytes = ZBytes::from("hello zenoh");
let bytes: ZBytes = ZBytes::from(String::from("hello zenoh"));

// From a number (uses native byte representation)
let bytes: ZBytes = ZBytes::from(42u32);
let bytes: ZBytes = ZBytes::from(3.14f64);

// Empty payload
let bytes: ZBytes = ZBytes::default();
```

### Extracting Data from ZBytes

```rust
use zenoh::bytes::ZBytes;

let bytes = ZBytes::from("hello zenoh");

// Extract as Vec<u8>
let raw: Vec<u8> = bytes.to_bytes().to_vec();

// Extract as a reader for streaming
let mut reader = bytes.reader();

// Deserialize back to a known type
let text: String = bytes.deserialize::<String>().unwrap();
let number: u32 = bytes.deserialize::<u32>().unwrap();
```

> **Important**: `ZBytes` is non-exhaustive. Never attempt to inspect its internal structure directly. Always use the `.reader()`, `.deserialize()`, or extension crate helpers to access the content.

### Shared Memory (SHM)

When the `shared-memory` feature is enabled, `ZBytes` can wrap an SHM buffer for true zero-copy between processes on the same machine:

```rust
#[cfg(feature = "shared-memory")]
{
    use zenoh::shm::{ZShm, ZShmMut};

    // Wrap SHM buffer — zero-copy put
    let shm_buf: ZShmMut = /* acquire from SHM provider */;
    let bytes = ZBytes::from(shm_buf);
}
```

---

## Encoding {#encoding}

`Encoding` describes the content type of a `ZBytes` payload. It is conceptually similar to an HTTP `Content-Type` header. Setting the encoding correctly allows subscribers and queryables to interpret received data without out-of-band agreement.

Encoding is metadata — zenoh does not inspect or validate it. The sender sets it; the receiver reads it.

### Predefined Encodings

zenoh ships with a set of well-known encoding constants that cover the most common cases:

```rust
use zenoh::bytes::Encoding;

// Raw binary — no structure assumed
Encoding::ZENOH_BYTES            // application/octet-stream equivalent

// Text
Encoding::ZENOH_STRING           // UTF-8 string
Encoding::TEXT_PLAIN
Encoding::TEXT_HTML
Encoding::TEXT_XML
Encoding::TEXT_CSV

// Structured
Encoding::APPLICATION_JSON
Encoding::APPLICATION_JSON5
Encoding::APPLICATION_CBOR
Encoding::APPLICATION_PROTOBUF
Encoding::APPLICATION_XML
Encoding::APPLICATION_OCTET_STREAM

// Images / media
Encoding::IMAGE_PNG
Encoding::IMAGE_JPEG
Encoding::IMAGE_GIF

// zenoh-specific
Encoding::ZENOH_SERIALIZED       // data serialized with ZSerializer
```

### Custom Encodings

If none of the predefined constants suit your application, create a custom encoding from any string:

```rust
use zenoh::bytes::Encoding;

let enc = Encoding::from("application/x-my-format");
let enc = Encoding::from("application/vnd.mycompany.v1+json");
```

Custom encoding strings are arbitrary UTF-8. By convention, follow MIME type syntax (`type/subtype` or `type/subtype+suffix`), but zenoh does not enforce this.

### Setting Encoding When Publishing

```rust
use zenoh::bytes::Encoding;

let session = zenoh::open(zenoh::Config::default()).await.unwrap();

session
    .put("my/key", payload)
    .encoding(Encoding::APPLICATION_JSON)
    .await
    .unwrap();

// Or on a declared publisher
let publisher = session
    .declare_publisher("my/key")
    .encoding(Encoding::APPLICATION_JSON)
    .await
    .unwrap();
publisher.put(payload).await.unwrap();
```

### Checking Encoding on Receipt

```rust
use zenoh::bytes::Encoding;

let subscriber = session
    .declare_subscriber("my/**")
    .await
    .unwrap();

while let Ok(sample) = subscriber.recv_async().await {
    let enc = sample.encoding();
    if enc == &Encoding::APPLICATION_JSON {
        // parse as JSON
    } else if enc == &Encoding::ZENOH_SERIALIZED {
        // use ZDeserializer
    } else {
        eprintln!("unexpected encoding: {enc}");
    }
}
```

---

## zenoh-ext Serialization Helpers {#zenoh-ext}

The `zenoh-ext` crate provides `ZSerializer` and `ZDeserializer` — ergonomic helpers for packing multiple typed values into a single `ZBytes` and unpacking them again. This eliminates the need to manually frame fields when building structured messages.

Add `zenoh-ext` to your `Cargo.toml`:

```toml
[dependencies]
zenoh = "1"
zenoh-ext = "1"
```

### ZSerializer

`ZSerializer` lets you append multiple values into one `ZBytes` sequentially. The wire format is length-prefixed, so each field's boundary is recoverable by `ZDeserializer`.

```rust
use zenoh_ext::ZSerializer;

let mut ser = ZSerializer::new();
ser.serialize(42u32);
ser.serialize("hello");
ser.serialize(3.14f64);
ser.serialize(true);

let zbytes: zenoh::bytes::ZBytes = ser.finish();
```

#### Supported Types

| Type | Notes |
|------|-------|
| `u8`, `u16`, `u32`, `u64`, `u128` | Little-endian |
| `i8`, `i16`, `i32`, `i64`, `i128` | Little-endian |
| `f32`, `f64` | IEEE 754 little-endian |
| `bool` | Single byte |
| `String`, `&str` | Length-prefixed UTF-8 |
| `Vec<u8>`, `&[u8]` | Length-prefixed bytes |
| `Vec<T>` | Length-prefixed sequence of `T` |
| Tuples `(A, B)`, `(A, B, C)` | Fields written in order |

### ZDeserializer

`ZDeserializer` reads values back out of a `ZBytes` in the same order they were written:

```rust
use zenoh_ext::ZDeserializer;

let mut de = ZDeserializer::new(&zbytes);
let n: u32 = de.deserialize().unwrap();
let s: String = de.deserialize().unwrap();
let f: f64 = de.deserialize().unwrap();
let b: bool = de.deserialize().unwrap();
```

> Fields must be deserialized in exactly the same order they were serialized. There is no field tagging or schema — the serialization format is positional.

### Serializing Sequences

```rust
use zenoh_ext::ZSerializer;

let mut ser = ZSerializer::new();
let values: Vec<u32> = vec![1, 2, 3, 4, 5];
ser.serialize(values);

let zbytes = ser.finish();

// Deserialize
use zenoh_ext::ZDeserializer;
let mut de = ZDeserializer::new(&zbytes);
let recovered: Vec<u32> = de.deserialize().unwrap();
assert_eq!(recovered, vec![1, 2, 3, 4, 5]);
```

### Serializing Tuples

```rust
use zenoh_ext::ZSerializer;

let mut ser = ZSerializer::new();
ser.serialize(("sensor_1", 98.6f32, true));
let zbytes = ser.finish();

use zenoh_ext::ZDeserializer;
let mut de = ZDeserializer::new(&zbytes);
let (id, temp, active): (String, f32, bool) = de.deserialize().unwrap();
```

### Convenience Functions

`zenoh-ext` also provides top-level functions for single-value serialization:

```rust
use zenoh_ext::{z_serialize, z_deserialize};

// Serialize a single value
let zbytes = z_serialize(&42u32);

// Deserialize a single value
let n: u32 = z_deserialize(&zbytes).unwrap();
```

### Custom Types with Serde

When the `serde` feature is enabled in `zenoh-ext`, you can serialize arbitrary types that implement `serde::Serialize` + `serde::Deserialize` using JSON, CBOR, or other serde-compatible formats:

```toml
[dependencies]
zenoh-ext = { version = "1", features = ["serde"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

```rust
use serde::{Serialize, Deserialize};
use zenoh::bytes::ZBytes;

#[derive(Serialize, Deserialize)]
struct SensorReading {
    sensor_id: String,
    temperature: f64,
    humidity: f64,
    timestamp_ms: u64,
}

// Serialize to JSON bytes manually
let reading = SensorReading {
    sensor_id: "sensor-42".to_string(),
    temperature: 23.5,
    humidity: 60.1,
    timestamp_ms: 1_700_000_000_000,
};

let json_bytes = serde_json::to_vec(&reading).unwrap();
let zbytes = ZBytes::from(json_bytes);

// Deserialize
let raw: Vec<u8> = zbytes.to_bytes().to_vec();
let recovered: SensorReading = serde_json::from_slice(&raw).unwrap();
```

---

## Examples {#examples}

### Example 1: Publishing a String

```rust
use zenoh::bytes::Encoding;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    // Simple string publish — encoding defaults to ZENOH_BYTES
    session
        .put("demo/hello", "Hello, zenoh!")
        .await
        .unwrap();

    // Explicit text encoding
    session
        .put("demo/hello", "Hello, zenoh!")
        .encoding(Encoding::TEXT_PLAIN)
        .await
        .unwrap();
}
```

### Example 2: Publishing JSON

Serialize a Rust struct to JSON, then publish it with the `APPLICATION_JSON` encoding so subscribers know how to parse it:

```rust
use zenoh::bytes::{Encoding, ZBytes};
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct Event {
    event_type: String,
    value: f64,
}

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    let event = Event {
        event_type: "temperature".to_string(),
        value: 22.3,
    };

    // Serialize with serde_json
    let json_bytes = serde_json::to_vec(&event).unwrap();
    let payload = ZBytes::from(json_bytes);

    session
        .put("sensors/temperature", payload)
        .encoding(Encoding::APPLICATION_JSON)
        .await
        .unwrap();
}
```

**Subscriber side:**

```rust
while let Ok(sample) = subscriber.recv_async().await {
    if sample.encoding() == &Encoding::APPLICATION_JSON {
        let raw = sample.payload().to_bytes();
        let event: Event = serde_json::from_slice(&raw).unwrap();
        println!("Received: {:?}", event);
    }
}
```

### Example 3: Multi-Field Message with ZSerializer

Pack a structured message without defining a schema format manually:

```rust
use zenoh_ext::ZSerializer;
use zenoh::bytes::Encoding;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    let mut ser = ZSerializer::new();
    ser.serialize("sensor-7");           // sensor ID
    ser.serialize(23.5f32);              // temperature
    ser.serialize(60u32);               // humidity percent
    ser.serialize(1_700_000_000u64);     // unix timestamp
    ser.serialize(true);                 // is_active

    let payload = ser.finish();

    session
        .put("sensors/readings", payload)
        .encoding(Encoding::ZENOH_SERIALIZED)
        .await
        .unwrap();
}
```

### Example 4: Reading a Structured Message with ZDeserializer

```rust
use zenoh_ext::ZDeserializer;
use zenoh::bytes::Encoding;

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();
    let subscriber = session
        .declare_subscriber("sensors/readings")
        .await
        .unwrap();

    while let Ok(sample) = subscriber.recv_async().await {
        if sample.encoding() != &Encoding::ZENOH_SERIALIZED {
            eprintln!("unexpected encoding: {}", sample.encoding());
            continue;
        }

        let mut de = ZDeserializer::new(sample.payload());

        let sensor_id: String  = de.deserialize().unwrap();
        let temperature: f32   = de.deserialize().unwrap();
        let humidity: u32      = de.deserialize().unwrap();
        let timestamp: u64     = de.deserialize().unwrap();
        let is_active: bool    = de.deserialize().unwrap();

        println!(
            "[{}] sensor={} temp={}°C humidity={}% active={}",
            timestamp, sensor_id, temperature, humidity, is_active
        );
    }
}
```

### Example 5: Custom Type Serialization

For complex nested types, implement the serialization yourself using `ZSerializer` and `ZDeserializer`, or use serde with a binary format like CBOR for compact encoding:

```rust
use zenoh::bytes::{Encoding, ZBytes};
use zenoh_ext::ZSerializer;
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug, Clone)]
struct Point3D {
    x: f64,
    y: f64,
    z: f64,
}

#[derive(Serialize, Deserialize, Debug)]
struct PointCloud {
    frame_id: String,
    points: Vec<Point3D>,
}

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    let cloud = PointCloud {
        frame_id: "world".to_string(),
        points: vec![
            Point3D { x: 1.0, y: 2.0, z: 3.0 },
            Point3D { x: 4.0, y: 5.0, z: 6.0 },
        ],
    };

    // Option A: serde_json
    let json_bytes = serde_json::to_vec(&cloud).unwrap();
    let payload_json = ZBytes::from(json_bytes);
    session
        .put("lidar/cloud", payload_json)
        .encoding(Encoding::APPLICATION_JSON)
        .await
        .unwrap();

    // Option B: Manual ZSerializer for flat structures
    let mut ser = ZSerializer::new();
    ser.serialize(cloud.frame_id.as_str());
    ser.serialize(cloud.points.len() as u32);
    for p in &cloud.points {
        ser.serialize(p.x);
        ser.serialize(p.y);
        ser.serialize(p.z);
    }
    let payload_ser = ser.finish();

    session
        .put("lidar/cloud/binary", payload_ser)
        .encoding(Encoding::ZENOH_SERIALIZED)
        .await
        .unwrap();
}
```

### Example 6: Using z_serialize / z_deserialize for Single Values

```rust
use zenoh_ext::{z_serialize, z_deserialize};

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    // Publish a single integer
    let payload = z_serialize(&1234u32);
    session.put("counter/value", payload).await.unwrap();

    // Subscribe and deserialize
    let subscriber = session.declare_subscriber("counter/value").await.unwrap();
    while let Ok(sample) = subscriber.recv_async().await {
        let value: u32 = z_deserialize(sample.payload()).unwrap();
        println!("Counter: {}", value);
    }
}
```

---

## Language Binding Differences {#language-bindings}

Zenoh supports multiple languages. The serialization story differs per binding:

### Rust

The native binding. Use `ZBytes` directly for raw bytes and `zenoh-ext` (`ZSerializer` / `ZDeserializer`) for structured multi-field messages.

```rust
// Rust: zenoh + zenoh-ext
use zenoh_ext::{ZSerializer, ZDeserializer};
let mut ser = ZSerializer::new();
ser.serialize(42u32);
let zbytes = ser.finish();
```

### Python

The Python binding (`zenoh-python`) accepts Python objects. Serialization is handled by the user before passing data to zenoh. Common patterns:

```python
import zenoh, json

session = zenoh.open(zenoh.Config())

# Publish JSON
data = {"temperature": 22.5, "unit": "C"}
payload = json.dumps(data).encode("utf-8")
session.put("sensors/temp", payload)

# Publish raw bytes
session.put("sensors/raw", bytes([0x01, 0x02, 0x03]))
```

For ROS 2 interop from Python, CDR encoding is managed by the `zenoh-plugin-ros2dds` bridge rather than user code.

### C / C++

The C binding exposes `z_bytes_t`. Serialization is entirely manual:

```c
// C: raw bytes
const char *msg = "hello";
z_owned_bytes_t payload;
z_bytes_from_static_str(&payload, msg);
z_publisher_put(z_loan(pub), z_move(payload), NULL);

// Read
z_owned_bytes_t received = /* from sample */;
z_owned_string_t text;
z_bytes_to_string(&text, z_loan(received));
printf("%s\n", z_string_data(z_loan(text)));
z_drop(z_move(text));
```

For structured data in C, you must implement your own framing (e.g., protobuf, flatbuffers, or a custom binary format).

### TypeScript / JavaScript

The TypeScript/JavaScript binding works with `Uint8Array`. JSON is the most common format:

```typescript
import { open, Config } from "@eclipse-zenoh/zenoh-ts";

const session = await open(new Config());

// Publish JSON
const data = { temperature: 22.5 };
const payload = new TextEncoder().encode(JSON.stringify(data));
await session.put("sensors/temp", payload);

// Subscribe
const subscriber = await session.declareSubscriber("sensors/temp");
for await (const sample of subscriber.receiver()) {
    const text = new TextDecoder().decode(sample.payload());
    const parsed = JSON.parse(text);
    console.log(parsed.temperature);
}
```

### Interoperability Between Bindings

When interoperating across language bindings, agree on:

1. **Encoding**: always set it explicitly (e.g., `APPLICATION_JSON`, `APPLICATION_PROTOBUF`)
2. **Byte order**: `ZSerializer` uses little-endian; match this in C/Python
3. **Schema**: use a schema-based format (protobuf, flatbuffers, JSON Schema) for cross-language structured messages

---

## CDR and ROS 2 Interop {#cdr}

CDR (Common Data Representation) is the wire format used by DDS and ROS 2. If you are bridging zenoh with ROS 2, understanding CDR is important.

### What CDR Is

CDR is a binary serialization format standardized by the Object Management Group (OMG). It is used by all DDS implementations (Cyclone DDS, Fast DDS, etc.) and therefore by ROS 2. CDR encodes primitive types with explicit alignment padding, handles endianness via a leading byte, and encodes strings as null-terminated with a 4-byte length prefix.

### Automatic CDR via zenoh-plugin-ros2dds

The recommended path for ROS 2 integration is `zenoh-plugin-ros2dds` (or `zenoh-bridge-ros2dds`). The plugin automatically handles CDR encoding and decoding when bridging ROS 2 topics to zenoh key expressions:

```
ROS 2 Topic (CDR) <---> zenoh-plugin-ros2dds <---> zenoh (ZBytes carrying raw CDR bytes)
```

When you receive a sample on the zenoh side that originated from a ROS 2 publisher, its payload is raw CDR bytes. The encoding will typically be `APPLICATION_CDR` or `APPLICATION_OCTET_STREAM`. You can deserialize it with a CDR library or pass it to another ROS 2 node via the bridge.

### Manual CDR

When you need to produce CDR bytes manually (e.g., to send data that a ROS 2 subscriber will consume without a bridge), use a CDR library:

```toml
[dependencies]
cdr = "0.2"           # or another CDR crate
zenoh = "1"
```

```rust
use zenoh::bytes::{Encoding, ZBytes};

#[derive(serde::Serialize, serde::Deserialize)]
struct RosString {
    data: String,
}

#[tokio::main]
async fn main() {
    let session = zenoh::open(zenoh::Config::default()).await.unwrap();

    let msg = RosString {
        data: "Hello from zenoh".to_string(),
    };

    // Serialize to CDR (little-endian, with 4-byte encapsulation header)
    let cdr_bytes = cdr::serialize::<_, _, cdr::CdrLe>(&msg, cdr::Infinite).unwrap();
    let payload = ZBytes::from(cdr_bytes);

    session
        .put("rt/chatter", payload)
        .encoding(Encoding::from("application/cdr"))
        .await
        .unwrap();
}
```

### CDR Key Points for Zenoh Users

| Concern | Detail |
|---------|--------|
| **Endianness** | CDR carries endianness in the encapsulation header. Most DDS implementations use little-endian in practice. |
| **Alignment** | CDR pads fields to their natural alignment. A `u32` is padded to a 4-byte boundary. Hand-rolled parsers must account for this. |
| **String encoding** | Strings are 4-byte length prefix (including null terminator) + UTF-8 bytes + null byte. |
| **Plugin bridge** | `zenoh-plugin-ros2dds` handles all of this automatically for bridged topics. Prefer the plugin over manual CDR. |
| **Type mapping** | ROS 2 `.msg` type definitions map to CDR. Use the generated code from `rosidl` or a compatible CDR library. |

### Checking for CDR Payload on Receipt

```rust
while let Ok(sample) = subscriber.recv_async().await {
    let enc = sample.encoding().to_string();
    if enc.contains("cdr") || enc == "application/octet-stream" {
        // May be CDR — check context or use a CDR parser
        let raw: Vec<u8> = sample.payload().to_bytes().to_vec();
        // Pass to CDR deserializer...
    }
}
```

---

## Quick Reference

| Goal | API |
|------|-----|
| Wrap raw bytes | `ZBytes::from(vec![...])` |
| Wrap a string | `ZBytes::from("hello")` |
| Pack multiple fields | `ZSerializer::new()` → `ser.serialize(v)` → `ser.finish()` |
| Unpack multiple fields | `ZDeserializer::new(&zbytes)` → `de.deserialize::<T>()` |
| Single value round-trip | `z_serialize(&v)` / `z_deserialize::<T>(&bytes)` |
| Set encoding on publish | `.encoding(Encoding::APPLICATION_JSON)` |
| Read encoding on receipt | `sample.encoding()` |
| Access raw bytes | `sample.payload().to_bytes()` |
| ROS 2 interop | Use `zenoh-plugin-ros2dds` for automatic CDR handling |