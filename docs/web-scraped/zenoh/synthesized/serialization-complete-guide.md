# Zenoh Serialization: Complete Guide

Zenoh is an **untyped protocol** that transports raw bytes. The protocol itself imposes no serialization format. What Zenoh provides—through its core `ZBytes` type and the optional `zenoh-ext` crate—is a practical layer on top of those raw bytes. This guide explains everything from buffer mechanics to cross-language interoperability.

---

## Table of Contents

- [ZBytes: The Core Buffer Type](#zbytes-the-core-buffer-type)
  - [What ZBytes Is](#what-zbytes-is)
  - ["Zero-Copy" Explained Precisely](#zero-copy-explained-precisely)
  - [Creating ZBytes](#creating-zbytes)
  - [Reading ZBytes](#reading-zbytes)
- [zenoh-ext: ZSerializer and ZDeserializer](#zenoh-ext-zserializer-and-zdeserializer)
  - [What zenoh-ext Provides](#what-zenoh-ext-provides)
  - [The Wire Format](#the-wire-format)
  - [ZSerializer: Supported Types](#zserializer-supported-types)
  - [Using ZSerializer and ZDeserializer](#using-zserializer-and-zdeserializer)
  - [Error Handling](#error-handling)
  - [Python zenoh-ext Equivalents](#python-zenoh-ext-equivalents)
- [Encoding System](#encoding-system)
  - [What Encoding Is](#what-encoding-is)
  - [The Default Encoding](#the-default-encoding)
  - [Predefined Encodings (Complete List)](#predefined-encodings-complete-list)
  - [The Three Zenoh-Specific Encodings](#the-three-zenoh-specific-encodings)
  - [Setting Encoding: Rust](#setting-encoding-rust)
  - [Setting Encoding: Python](#setting-encoding-python)
  - [Custom Encodings](#custom-encodings)
  - [Schema Field](#schema-field)
- [CDR: ROS2/DDS Interoperability](#cdr-ros2dds-interoperability)
  - [What CDR Is](#what-cdr-is)
  - [When Zenoh Uses CDR](#when-zenoh-uses-cdr)
  - [Using CDR in Rust](#using-cdr-in-rust)
  - [Using CDR in Python](#using-cdr-in-python)
  - [ROS2 Bridge Key Expression Mapping](#ros2-bridge-key-expression-mapping)
- [External Serialization Formats](#external-serialization-formats)
  - [JSON (serde_json)](#json-serde_json)
  - [Protobuf (prost)](#protobuf-prost)
  - [CBOR (ciborium / serde_cbor)](#cbor-ciborium-serde_cbor)
- [Cross-Language Interoperability](#cross-language-interoperability)
  - [The Core Problem](#the-core-problem)
  - [Safe Cross-Language Formats (Recommended)](#safe-cross-language-formats-recommended)
  - [Unsafe Cross-Language (Avoid)](#unsafe-cross-language-avoid)
  - [zenoh-ext Cross-Language: What Works and What Doesn't](#zenoh-ext-cross-language-what-works-and-what-doesnt)
  - [Complete Cross-Language Example: JSON](#complete-cross-language-example-json)
  - [Rust ZBytes ↔ Python bytes](#rust-zbytes-python-bytes)
  - [C `z_bytes_t` Interoperability](#c-z_bytes_t-interoperability)
- [Performance: When Copies Actually Happen](#performance-when-copies-actually-happen)
  - [Publisher Side](#publisher-side)
  - [Subscriber Side](#subscriber-side)
  - [Minimizing Copies: Practical Rules](#minimizing-copies-practical-rules)
- [Format Decision Guide](#format-decision-guide)
  - [Encoding Constants Summary](#encoding-constants-summary)


---


## ZBytes: The Core Buffer Type

### What ZBytes Is

`ZBytes` is a reference-counted, possibly non-contiguous byte buffer. It wraps an internal `ZBuf` (zenoh buffer), which can hold data in multiple disjoint memory regions called slices.

```
ZBytes
  └── ZBuf (internal)
        ├── ZSlice [0..N]  ← points into owned memory or SHM
        ├── ZSlice [N..M]
        └── ZSlice [M..P]
```

This multi-slice design is what enables zero-copy in specific scenarios.

### "Zero-Copy" Explained Precisely

The word "zero-copy" appears in Zenoh documentation, but its meaning depends on which operation you're looking at.

**When it IS zero-copy:**

1. **SHM (Shared Memory) path**: When a sender and receiver are on the same host, Zenoh can use a `ZShm` or `ZShmMut` buffer. The data lives in shared memory. Converting a `ZShm` to `ZBytes` and later accessing it skips any copy of the actual payload bytes. This is the one scenario where "zero-copy" means the data bytes never move.

2. **`append()` in ZBytesWriter**: Calling `writer.append(existing_zbytes)` takes ownership and links the existing slice into the writer's internal buffer without copying the data. The result is a multi-slice `ZBytes` that views both original memory regions.

   ```rust
   let one = ZBytes::from(vec![0, 1]);     // owns vec [0,1]
   let two = ZBytes::from(vec![2, 3, 4]);  // owns vec [2,3,4]

   let mut writer = ZBytes::writer();
   writer.append(one);   // no copy — transfers ZSlice ownership
   writer.append(two);   // no copy — transfers ZSlice ownership
   let combined = writer.finish();
   // combined has two slices, [0,1] and [2,3,4], no data was copied
   ```

3. **`to_bytes()` on a single-slice ZBytes**: Returns `Cow::Borrowed`, meaning it hands back a reference into the existing buffer with no allocation.

**When a copy DOES happen:**

1. **Creating ZBytes from `&[u8]` or `&str`**: The slice is copied into a new `Vec<u8>`. From `Vec<u8>` or `String`, the data is moved (no copy), but from a reference, it is copied.

   ```rust
   let data: &[u8] = b"hello";
   let z1 = ZBytes::from(data);       // COPY: allocates a new Vec
   let z2 = ZBytes::from(data.to_vec()); // MOVE: no copy of data bytes
   ```

2. **`z_serialize()`**: Serializing a struct or numeric value writes bytes through `ZBytesWriter`, which accumulates data in a `Vec<u8>` internally. The data is encoded into this buffer — a copy from the source type's memory representation.

3. **`to_bytes()` on a multi-slice ZBytes**: Returns `Cow::Owned` — allocates a new `Vec<u8>` and copies all slices into it.

   ```rust
   let z: ZBytes = /* received fragmented from network */;
   let bytes: Cow<[u8]> = z.to_bytes(); // may allocate if multi-slice
   ```

4. **Receiving data from the network**: The network stack reassembles packets into `ZBuf` slices. The data is always copied from kernel socket buffers to user-space.

**The marketing vs engineering reality:**

Zenoh's "zero-copy" claim is specifically accurate for the SHM intraprocess/intrahost path and for the `append()` composition pattern. For typical pub/sub over UDP or TCP where data is serialized and transmitted, at least one copy happens on the send side (serialization) and at least one on the receive side (network receive). This is normal and unavoidable — the claim is that Zenoh avoids *additional* copies on top of those.

### Creating ZBytes

**From raw bytes:**

```rust
use zenoh::bytes::ZBytes;

// From &[u8] — copies
let b: &[u8] = b"hello";
let z = ZBytes::from(b);

// From Vec<u8> — moves, no copy
let v: Vec<u8> = vec![1, 2, 3];
let z = ZBytes::from(v);

// From &str — copies UTF-8 bytes
let z = ZBytes::from("hello");

// From String — moves, no copy
let z = ZBytes::from(String::from("hello"));

// From [u8; N] array — copies
let z = ZBytes::from([0u8, 1, 2, 3]);

// From &[u8; N] array reference — copies
let arr = [0u8, 1, 2, 3];
let z = ZBytes::from(&arr);

// From bytes::Bytes — zero-copy (reference-counted)
let b = bytes::Bytes::from_static(b"data");
let z = ZBytes::from(b);
```

**From serializable types (zenoh-ext):**

```rust
use zenoh_ext::{z_serialize, z_deserialize};

let z = z_serialize(&42u32);
let z = z_serialize(&vec![1.0f32, 2.0, 3.0]);
let z = z_serialize(&("key".to_string(), 100i64));
```

**From SHM (unstable feature):**

```rust
// Requires feature flags: unstable + shared-memory
use zenoh_shm::api::buffer::zshmmut::ZShmMut;

let shm_buf: ZShmMut = /* allocate from SHM provider */;
let z = ZBytes::from(shm_buf); // zero-copy: data stays in shared memory
```

**Using the writer for composition:**

```rust
use std::io::Write;
use zenoh::bytes::ZBytes;

let mut writer = ZBytes::writer();
writer.write_all(b"header").unwrap();          // copies into writer's vec
writer.append(ZBytes::from(vec![1, 2, 3]));   // zero-copy append
let z = writer.finish();
```

### Reading ZBytes

**As a contiguous byte slice:**

```rust
// Returns Cow<[u8]>: borrowed if single-slice, owned if multi-slice
let bytes: std::borrow::Cow<[u8]> = z.to_bytes();
let slice: &[u8] = &*bytes; // deref to &[u8]
```

**As a string:**

```rust
// Returns Result<Cow<str>, Utf8Error>
let s: std::borrow::Cow<str> = z.try_to_string().unwrap();
```

**Using the reader (implements std::io::Read + Seek):**

```rust
use std::io::Read;

let mut reader = z.reader();
let mut buf = [0u8; 4];
reader.read_exact(&mut buf).unwrap();
println!("remaining: {}", reader.remaining());
```

**Iterating over slices (avoids contiguous-copy for multi-slice):**

```rust
// Each item is a &[u8] pointing into original memory
for slice in z.slices() {
    println!("slice: {:02x?}", slice);
}
```

**Using z_deserialize (zenoh-ext):**

```rust
use zenoh_ext::z_deserialize;

let value: u32 = z_deserialize(&z).unwrap();
let values: Vec<f64> = z_deserialize(&z).unwrap();
let pair: (i32, String) = z_deserialize(&z).unwrap();
```

**Python equivalents:**

```python
from zenoh import ZBytes

z = ZBytes(b"hello")
raw: bytes = z.to_bytes()    # equivalent to bytes(z)
text: str = z.to_string()    # equivalent to str(z)
```

---

## zenoh-ext: ZSerializer and ZDeserializer

The `zenoh-ext` crate provides a structured serialization layer on top of `ZBytes`. It defines its own binary wire format specified in the [Serialization RFC](https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Serialization.md).

### What zenoh-ext Provides

- A concrete, documented binary format for primitive types and collections
- `ZSerializer`: builder for encoding structured messages
- `ZDeserializer`: corresponding reader
- `z_serialize()` / `z_deserialize()`: convenience functions for single-value round trips
- `Serialize` / `Deserialize` traits you can implement for custom types

### The Wire Format

The Zenoh serialization format is:

- **Little-endian** for all numeric types
- **Two's complement** for signed integers
- **IEEE 754** for floating-point
- **LEB128 varint** for sequence lengths (compact encoding)
- **Not self-describing**: the receiver must know the expected type

**Number encoding (concrete bytes):**

```
7u8    → 0x07
-1i8   → 0xff
0i32   → 0x00 0x00 0x00 0x00
42i32  → 0x2a 0x00 0x00 0x00    (little-endian)
1.5f32 → 0x00 0x00 0xc0 0x3f    (IEEE 754 LE)
true   → 0x01
```

**Sequence encoding (length prefix + elements):**

```
[1u8, 2, 3] → 0x03 0x01 0x02 0x03
              └──┘ └─────────────┘
              LEB128 len=3   elements
```

**String encoding (length-prefixed UTF-8, no null terminator):**

```
"Hello!" → 0x06 0x48 0x65 0x6c 0x6c 0x6f 0x21
           └──┘ └───────────────────────────────┘
           LEB128 len=6    UTF-8 bytes
```

**Tuple encoding (concatenated fields, no separator):**

```
(42u8, 0.5f32) → 0x2a 0x00 0x00 0x00 0x3f
                  └──┘ └─────────────────┘
                  42u8    0.5f32 (LE)
```

### ZSerializer: Supported Types

**Primitives** (exact Rust types):
- Integers: `u8`, `u16`, `u32`, `u64`, `u128`, `i8`, `i16`, `i32`, `i64`, `i128`
- Floats: `f32`, `f64`
- Boolean: `bool` (serialized as `u8`, restricted to 0 or 1)

**Strings:**
- `&str`, `String`, `Cow<'_, str>` — length-prefixed UTF-8 bytes

**Collections:**
- `&[T]`, `[T; N]` (serialized as variable-length sequence), `Vec<T>`, `Box<[T]>`, `Cow<'_, [T]>`
- `HashMap<K, V>`, `BTreeMap<K, V>` — as sequence of `(K, V)` pairs
- `HashSet<T>`, `BTreeSet<T>` — as sequences

**Tuples** (up to 16 elements):
- `(T0,)`, `(T0, T1)`, ..., `(T0, ..., T15)` — concatenated serializations

**ZBytes itself:**
- Can be serialized as a length-prefixed byte sequence

**Variable-length integer:**
- `VarInt<usize>` — LEB128-encoded `usize`, used internally for lengths

### Using ZSerializer and ZDeserializer

**Single-value convenience functions (most common):**

```rust
use zenoh_ext::{z_serialize, z_deserialize};

// Serialize
let zbytes = z_serialize(&42u32);
let zbytes = z_serialize(&vec![1.0f32, 2.0, 3.0]);
let zbytes = z_serialize(&("name".to_string(), 42i32, true));

// Deserialize
let n: u32 = z_deserialize(&zbytes).unwrap();
let v: Vec<f32> = z_deserialize(&zbytes).unwrap();
let t: (String, i32, bool) = z_deserialize(&zbytes).unwrap();
```

**ZSerializer for multi-field messages:**

```rust
use zenoh_ext::{ZSerializer, z_deserialize};

let mut ser = ZSerializer::new();
ser.serialize(42i32);
ser.serialize(vec![1u8, 2, 3]);
ser.serialize("status".to_string());
let zbytes = ser.finish();

// Equivalent: deserialize as a tuple
let (n, v, s): (i32, Vec<u8>, String) = z_deserialize(&zbytes).unwrap();
// Or use ZDeserializer to read field-by-field
```

**ZDeserializer for field-by-field reading:**

```rust
use zenoh_ext::{ZDeserializer, ZDeserializeError};

let zbytes = /* received ZBytes */;
let mut deser = ZDeserializer::new(&zbytes);

let id: u32 = deser.deserialize().map_err(|_| "failed to read id")?;
let name: String = deser.deserialize().map_err(|_| "failed to read name")?;
let score: f64 = deser.deserialize().map_err(|_| "failed to read score")?;

if !deser.done() {
    // trailing bytes — likely wrong type or version mismatch
    return Err("unexpected trailing bytes".into());
}
```

**Iterating sequences via serialize_iter / deserialize_iter:**

```rust
use zenoh_ext::{ZSerializer, ZDeserializer};

let items = vec!["alpha", "beta", "gamma"];

let mut ser = ZSerializer::new();
ser.serialize_iter(items.iter());   // requires ExactSizeIterator
let zbytes = ser.finish();

let mut deser = ZDeserializer::new(&zbytes);
let iter = deser.deserialize_iter::<String>().unwrap();
for item in iter {
    let s: String = item.unwrap();
    println!("{}", s);
}
```

**Custom struct serialization:**

```rust
use zenoh_ext::{Serialize, Deserialize, ZSerializer, ZDeserializer, ZDeserializeError, z_serialize, z_deserialize};

#[derive(Debug, PartialEq)]
struct SensorReading {
    timestamp_ms: u64,
    temperature: f32,
    humidity: f32,
    label: String,
}

impl Serialize for SensorReading {
    fn serialize(&self, serializer: &mut ZSerializer) {
        serializer.serialize(self.timestamp_ms);
        serializer.serialize(self.temperature);
        serializer.serialize(self.humidity);
        serializer.serialize(self.label.as_str());
    }
}

impl Deserialize for SensorReading {
    fn deserialize(deserializer: &mut ZDeserializer) -> Result<Self, ZDeserializeError> {
        Ok(SensorReading {
            timestamp_ms: deserializer.deserialize()?,
            temperature: deserializer.deserialize()?,
            humidity: deserializer.deserialize()?,
            label: deserializer.deserialize()?,
        })
    }
}

// Usage
let reading = SensorReading {
    timestamp_ms: 1700000000000,
    temperature: 23.5,
    humidity: 61.2,
    label: "sensor-a".to_string(),
};

let zbytes = z_serialize(&reading);
let recovered: SensorReading = z_deserialize(&zbytes).unwrap();
assert_eq!(reading, recovered);
```

### Error Handling

`z_deserialize` and `ZDeserializer::deserialize` return `Result<T, ZDeserializeError>`. `ZDeserializeError` is a unit struct with no inner detail — it signals only that deserialization failed (short read, invalid bool byte, wrong sequence length for fixed-size array, or trailing bytes when using `z_deserialize`).

The `done()` check is important: `z_deserialize` will return an error if any bytes remain after reading the expected type, which protects against accidentally reading a `u32` from a buffer that actually contains a `(u32, String)`.

### Python zenoh-ext Equivalents

Python's `zenoh.ext` module mirrors the Rust API with type annotations:

```python
from zenoh.ext import (
    UInt8, UInt16, UInt32, UInt64, UInt128,
    Int8, Int16, Int32, Int64, Int128,
    Float32, Float64,
    z_serialize, z_deserialize
)

# Numeric types need explicit wrapper (Python has no fixed-size int types)
payload = z_serialize(UInt32(1234))
value = z_deserialize(UInt32, payload)

# float defaults to Float64
payload = z_serialize(3.14)  # Float64
value = z_deserialize(float, payload)

# list (homogeneous)
payload = z_serialize([0.0, 1.5, 42.0])  # all floats (Float64)
values = z_deserialize(list[float], payload)

# dict
payload = z_serialize({0: "hello", 1: "world"})
d = z_deserialize(dict[int, str], payload)

# tuple
payload = z_serialize((0.42, "hello"))
t = z_deserialize(tuple[float, str], payload)
```

---

## Encoding System

### What Encoding Is

`Encoding` is an optional content-type hint attached to a message. It tells the receiver how to interpret the payload — but Zenoh does **not** enforce it. The receiver can ignore the encoding entirely or use it to dispatch to different deserializers.

Encoding is represented as a MIME-like string: `type/subtype[;schema]`. Zenoh internally maps 53 predefined encoding strings to compact integer IDs for efficient transmission. Custom encodings are also supported.

### The Default Encoding

If no encoding is specified, Zenoh uses `Encoding::ZENOH_BYTES` (ID 0, string `"zenoh/bytes"`). This means: raw bytes with no interpretation.

### Predefined Encodings (Complete List)

| Constant | ID | String |
|---|---|---|
| `ZENOH_BYTES` | 0 | `zenoh/bytes` |
| `ZENOH_STRING` | 1 | `zenoh/string` |
| `ZENOH_SERIALIZED` | 2 | `zenoh/serialized` |
| `APPLICATION_OCTET_STREAM` | 3 | `application/octet-stream` |
| `TEXT_PLAIN` | 4 | `text/plain` |
| `APPLICATION_JSON` | 5 | `application/json` |
| `TEXT_JSON` | 6 | `text/json` |
| `APPLICATION_CDR` | 7 | `application/cdr` |
| `APPLICATION_CBOR` | 8 | `application/cbor` |
| `APPLICATION_YAML` | 9 | `application/yaml` |
| `TEXT_YAML` | 10 | `text/yaml` |
| `TEXT_JSON5` | 11 | `text/json5` |
| `APPLICATION_PYTHON_SERIALIZED_OBJECT` | 12 | `application/python-serialized-object` |
| `APPLICATION_PROTOBUF` | 13 | `application/protobuf` |
| `APPLICATION_JAVA_SERIALIZED_OBJECT` | 14 | `application/java-serialized-object` |
| `APPLICATION_OPENMETRICS_TEXT` | 15 | `application/openmetrics-text` |
| `IMAGE_PNG` | 16 | `image/png` |
| `IMAGE_JPEG` | 17 | `image/jpeg` |
| `IMAGE_GIF` | 18 | `image/gif` |
| `IMAGE_BMP` | 19 | `image/bmp` |
| `IMAGE_WEBP` | 20 | `image/webp` |
| `APPLICATION_XML` | 21 | `application/xml` |
| `APPLICATION_X_WWW_FORM_URLENCODED` | 22 | `application/x-www-form-urlencoded` |
| `TEXT_HTML` | 23 | `text/html` |
| `TEXT_XML` | 24 | `text/xml` |
| `TEXT_CSS` | 25 | `text/css` |
| `TEXT_JAVASCRIPT` | 26 | `text/javascript` |
| `TEXT_MARKDOWN` | 27 | `text/markdown` |
| `TEXT_CSV` | 28 | `text/csv` |
| `APPLICATION_SQL` | 29 | `application/sql` |
| `APPLICATION_COAP_PAYLOAD` | 30 | `application/coap-payload` |
| `APPLICATION_JSON_PATCH_JSON` | 31 | `application/json-patch+json` |
| `APPLICATION_JSON_SEQ` | 32 | `application/json-seq` |
| `APPLICATION_JSONPATH` | 33 | `application/jsonpath` |
| `APPLICATION_JWT` | 34 | `application/jwt` |
| `APPLICATION_MP4` | 35 | `application/mp4` |
| `APPLICATION_SOAP_XML` | 36 | `application/soap+xml` |
| `APPLICATION_YANG` | 37 | `application/yang` |
| `AUDIO_AAC` | 38 | `audio/aac` |
| `AUDIO_FLAC` | 39 | `audio/flac` |
| `AUDIO_MP4` | 40 | `audio/mp4` |
| `AUDIO_OGG` | 41 | `audio/ogg` |
| `AUDIO_VORBIS` | 42 | `audio/vorbis` |
| `VIDEO_H261` | 43 | `video/h261` |
| `VIDEO_H263` | 44 | `video/h263` |
| `VIDEO_H264` | 45 | `video/h264` |
| `VIDEO_H265` | 46 | `video/h265` |
| `VIDEO_H266` | 47 | `video/h266` |
| `VIDEO_MP4` | 48 | `video/mp4` |
| `VIDEO_OGG` | 49 | `video/ogg` |
| `VIDEO_RAW` | 50 | `video/raw` |
| `VIDEO_VP8` | 51 | `video/vp8` |
| `VIDEO_VP9` | 52 | `video/vp9` |

**Custom encodings** use internal ID `0xFFFF` and are stored fully in the schema field.

### The Three Zenoh-Specific Encodings

`ZENOH_BYTES`, `ZENOH_STRING`, and `ZENOH_SERIALIZED` are Zenoh's own encoding constants:

- **`ZENOH_BYTES`** (ID 0): Raw bytes. Use with `ZBytes::from(vec)` / `ZBytes::from(&[u8])`. Read back with `to_bytes()`.
- **`ZENOH_STRING`** (ID 1): UTF-8 string. Use with `ZBytes::from(string)`. Read back with `try_to_string()`.
- **`ZENOH_SERIALIZED`** (ID 2): zenoh-ext format. Use with `z_serialize()`. Read back with `z_deserialize()`. The `schema` field can optionally describe the schema, e.g. `"zenoh/serialized;com.example.SensorReading"`.

### Setting Encoding: Rust

**On put():**

```rust
use zenoh::bytes::Encoding;

// Put with explicit encoding
session
    .put("demo/key", payload)
    .encoding(Encoding::APPLICATION_JSON)
    .await
    .unwrap();

// Put with zenoh-ext serialized encoding
session
    .put("demo/key", z_serialize(&my_struct))
    .encoding(Encoding::ZENOH_SERIALIZED)
    .await
    .unwrap();
```

**On a declared publisher:**

```rust
use zenoh::bytes::Encoding;

let publisher = session
    .declare_publisher("demo/sensor")
    .encoding(Encoding::APPLICATION_JSON)   // default encoding for this publisher
    .await
    .unwrap();

publisher.put(payload).await.unwrap();

// Override encoding per-message
publisher
    .put(payload)
    .encoding(Encoding::APPLICATION_CBOR)
    .await
    .unwrap();
```

**Reading encoding from a received sample:**

```rust
let subscriber = session.declare_subscriber("demo/**").await.unwrap();
while let Ok(sample) = subscriber.recv_async().await {
    let enc = sample.encoding();
    println!("encoding: {}", enc);  // e.g. "application/json"

    match enc {
        e if e == &Encoding::APPLICATION_JSON => {
            let s = sample.payload().try_to_string().unwrap();
            let v: serde_json::Value = serde_json::from_str(&s).unwrap();
        }
        e if e == &Encoding::ZENOH_SERIALIZED => {
            let reading: SensorReading = z_deserialize(sample.payload()).unwrap();
        }
        _ => {
            println!("unknown encoding, raw bytes: {:?}", sample.payload().to_bytes());
        }
    }
}
```

### Setting Encoding: Python

```python
import zenoh
from zenoh import Encoding

with zenoh.open(zenoh.Config()) as session:
    # Put with encoding
    session.put(
        "demo/key",
        b'{"value": 42}',
        encoding=Encoding.APPLICATION_JSON
    )

    # Publisher with default encoding
    pub = session.declare_publisher(
        "demo/sensor",
        encoding=Encoding.APPLICATION_JSON
    )
    pub.put(b'{"temp": 23.5}')

    # Read encoding from subscriber
    def on_sample(sample):
        enc = sample.encoding
        print(f"encoding: {enc}")
        if enc == Encoding.APPLICATION_JSON:
            import json
            data = json.loads(sample.payload.to_string())

    sub = session.declare_subscriber("demo/**", on_sample)
```

### Custom Encodings

```rust
// Define a custom encoding from a string
let my_encoding = Encoding::from("application/x-my-format");

// Add a schema
let with_schema = Encoding::from("application/x-my-format;v2.1");
// Or equivalently:
let with_schema = Encoding::from("application/x-my-format").with_schema("v2.1");

// Use it
session.put("key", payload).encoding(my_encoding).await.unwrap();
```

Custom encodings (strings not in the predefined table) are transmitted as their full string representation. This is less efficient than predefined encodings — the string is sent with every message rather than a 2-byte integer ID.

### Schema Field

Encodings can carry an optional schema string after `;`. Zenoh does not define schema semantics. Common uses:

- `text/plain;utf-8` — charset hint
- `application/json;com.example.MyType` — type hint for consumers
- `zenoh/serialized;SensorReading_v2` — zenoh-ext format with type annotation

```rust
let enc = Encoding::APPLICATION_JSON.with_schema("com.example.SensorReading");
assert_eq!(enc.to_string(), "application/json;com.example.SensorReading");
```

---

## CDR: ROS2/DDS Interoperability

### What CDR Is

Common Data Representation (CDR) is the binary encoding used by DDS (Data Distribution Service) and its IDL-based type system. It originated in the CORBA specification. ROS2 uses CDR as its serialization format for message types.

CDR characteristics:
- **Big-endian or little-endian** (header byte indicates which)
- **Padded alignment**: fields are aligned to their natural size (4-byte ints at 4-byte boundaries, etc.)
- **Self-contained per message**: each CDR message starts with a 4-byte header (`\x00\x01\x00\x00` for little-endian)
- **Schema is external**: IDL files define the type; CDR does not embed type information

### When Zenoh Uses CDR

Zenoh itself never automatically converts to/from CDR. CDR appears in the Zenoh ecosystem in two ways:

1. **Via the zenoh-plugin-ros2dds bridge**: The bridge subscribes to ROS2 topics and republishes them onto Zenoh key expressions. ROS2 messages arrive as CDR-encoded bytes and are forwarded as-is into `ZBytes` with `APPLICATION_CDR` encoding. Subscribers on the Zenoh side receive raw CDR bytes.

2. **Directly by the application**: You can serialize any CDR-compatible data and publish it with `APPLICATION_CDR` encoding for consumption by ROS2 nodes or other DDS participants (via the bridge).

### Using CDR in Rust

There is no CDR serialization library in the standard Rust ecosystem that is commonly used. When working with the ROS2 bridge, you typically handle CDR at the Python or C++ level. However, you can publish raw CDR bytes:

```rust
// Assume cdr_bytes is a Vec<u8> of properly serialized CDR data
// (e.g., generated by ros2 or a CDR library)
session
    .put("rt/my_topic", cdr_bytes)
    .encoding(Encoding::APPLICATION_CDR)
    .await
    .unwrap();
```

### Using CDR in Python

Python has `rclpy.serialization` (from ROS2) and the standalone `pycdr2` library:

**With rclpy (requires ROS2 installation):**

```python
import zenoh
from zenoh import Encoding
from rclpy.serialization import serialize_message, deserialize_message
from std_msgs.msg import String as RosString

with zenoh.open(zenoh.Config()) as session:
    # Serialize a ROS2 message to CDR
    msg = RosString()
    msg.data = "hello from zenoh"
    cdr_bytes = serialize_message(msg)

    # Publish with CDR encoding
    session.put(
        "rt/chatter",
        cdr_bytes,
        encoding=Encoding.APPLICATION_CDR
    )

    # Receive and deserialize CDR
    def on_sample(sample):
        if sample.encoding == Encoding.APPLICATION_CDR:
            msg = deserialize_message(sample.payload.to_bytes(), RosString)
            print(f"received: {msg.data}")

    sub = session.declare_subscriber("rt/chatter", on_sample)
```

**With pycdr2 (no ROS2 required):**

```python
import zenoh
from zenoh import Encoding
from pycdr2 import IdlStruct
from dataclasses import dataclass

@dataclass
class Temperature(IdlStruct, typename="Temperature"):
    sensor_id: str
    value: float

with zenoh.open(zenoh.Config()) as session:
    # Serialize
    reading = Temperature(sensor_id="sensor-a", value=23.5)
    cdr_bytes = reading.serialize()

    session.put("sensors/temp", cdr_bytes, encoding=Encoding.APPLICATION_CDR)

    # Deserialize
    def on_sample(sample):
        t = Temperature.deserialize(sample.payload.to_bytes())
        print(f"{t.sensor_id}: {t.value}°C")

    sub = session.declare_subscriber("sensors/temp", on_sample)
```

### ROS2 Bridge Key Expression Mapping

When using the zenoh-plugin-ros2dds bridge, ROS2 topic names are mapped to Zenoh key expressions with the `rt/` prefix:

```
ROS2 topic: /chatter       → Zenoh key: rt/chatter
ROS2 topic: /sensors/temp  → Zenoh key: rt/sensors/temp
```

Messages always use `APPLICATION_CDR` encoding through the bridge.

---

## External Serialization Formats

Zenoh places no constraints on what you put in `ZBytes`. Any serialization format works. These are the common patterns:

### JSON (serde_json)

```rust
use zenoh::bytes::{ZBytes, Encoding};
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct SensorData {
    sensor_id: String,
    temperature: f64,
    timestamp: u64,
}

// Publish
let data = SensorData {
    sensor_id: "sensor-a".into(),
    temperature: 23.5,
    timestamp: 1700000000,
};
let json_bytes = serde_json::to_vec(&data).unwrap();
session
    .put("sensors/data", json_bytes)
    .encoding(Encoding::APPLICATION_JSON)
    .await
    .unwrap();

// Subscribe
let subscriber = session.declare_subscriber("sensors/**").await.unwrap();
while let Ok(sample) = subscriber.recv_async().await {
    let data: SensorData = serde_json::from_slice(&sample.payload().to_bytes()).unwrap();
    println!("{}: {}°C", data.sensor_id, data.temperature);
}
```

**Python side (producer) with JSON:**

```python
import json
import zenoh
from zenoh import Encoding

with zenoh.open(zenoh.Config()) as session:
    data = {"sensor_id": "sensor-a", "temperature": 23.5, "timestamp": 1700000000}
    payload = json.dumps(data).encode("utf-8")
    session.put("sensors/data", payload, encoding=Encoding.APPLICATION_JSON)
```

### Protobuf (prost)

```rust
use prost::Message;

// Encode
let msg = MyProtoMessage { id: 1, name: "test".into() };
let bytes = msg.encode_to_vec();
session
    .put("key", bytes)
    .encoding(Encoding::APPLICATION_PROTOBUF)
    .await
    .unwrap();

// Decode
let msg = MyProtoMessage::decode(&*sample.payload().to_bytes()).unwrap();
```

### CBOR (ciborium / serde_cbor)

CBOR is compact binary JSON. Use `Encoding::APPLICATION_CBOR`.

```rust
use zenoh::bytes::Encoding;

let mut buf = Vec::new();
ciborium::into_writer(&my_value, &mut buf).unwrap();
session.put("key", buf).encoding(Encoding::APPLICATION_CBOR).await.unwrap();

// Decode
let value: MyType = ciborium::from_reader(sample.payload().to_bytes().as_ref()).unwrap();
```

---

## Cross-Language Interoperability

### The Core Problem

Zenoh is language-agnostic, but each language has its own type system. The serialization format must be agreed upon by both sides. The wrong choices here are common sources of bugs.

### Safe Cross-Language Formats (Recommended)

| Format | Encoding Constant | Works Across | Notes |
|---|---|---|---|
| JSON | `APPLICATION_JSON` | All languages | Verbose but universal; use for config, events |
| Protobuf | `APPLICATION_PROTOBUF` | All languages with a protoc plugin | Schema required; most compact+typed option |
| CBOR | `APPLICATION_CBOR` | All languages with a CBOR library | Binary JSON; good balance |
| CDR | `APPLICATION_CDR` | ROS2/DDS ecosystems | Required for ROS2 interop |
| Raw bytes | `ZENOH_BYTES` | All languages | You define the format |

### Unsafe Cross-Language (Avoid)

| Format | Why It Fails Across Languages |
|---|---|
| `zenoh-ext` / `z_serialize` | The format is cross-language, but Python's types differ (see below) |
| `ZENOH_SERIALIZED` | Language bindings must agree on exact type mapping |
| Python pickle | `APPLICATION_PYTHON_SERIALIZED_OBJECT` — Python-only |
| Java serialization | `APPLICATION_JAVA_SERIALIZED_OBJECT` — Java-only |

### zenoh-ext Cross-Language: What Works and What Doesn't

The Zenoh serialization format RFC is implemented in both Rust and Python. The wire format is the same. However, types map differently:

| Rust type | Python type | Wire-compatible? |
|---|---|---|
| `u32` | `UInt32` | Yes, if both sides use the right type |
| `i32` | `Int32` or `int` | `int` maps to `Int32` in Python |
| `f64` | `float` | Yes |
| `f32` | `Float32` | Yes, if Python uses `Float32` explicitly |
| `Vec<u8>` | `list[int]`... or `bytes`? | Risky: Python list serializes element-by-element |
| `String` | `str` | Yes |
| `[T; N]` | — | Rust fixed arrays serialize as variable-length sequence; Python decodes as `list` |

**Rust producer → Python consumer (works):**

```rust
// Rust: publish a (u32, f64, String) tuple
use zenoh_ext::{z_serialize};
use zenoh::bytes::Encoding;

let payload = z_serialize(&(42u32, 23.5f64, "sensor-a".to_string()));
session
    .put("sensors/reading", payload)
    .encoding(Encoding::ZENOH_SERIALIZED)
    .await
    .unwrap();
```

```python
# Python: receive and decode
from zenoh.ext import UInt32, Float64, z_deserialize

def on_sample(sample):
    result = z_deserialize(tuple[UInt32, Float64, str], sample.payload)
    id_, temp, name = result
    print(f"{name}: {temp}°C (id={id_})")
```

**Python producer → Rust consumer (works):**

```python
# Python: publish
from zenoh.ext import UInt32, Float64, z_serialize
import zenoh
from zenoh import Encoding

with zenoh.open(zenoh.Config()) as session:
    payload = z_serialize((UInt32(42), Float64(23.5), "sensor-a"))
    session.put("sensors/reading", payload, encoding=Encoding.ZENOH_SERIALIZED)
```

```rust
// Rust: receive
let (id, temp, name): (u32, f64, String) = z_deserialize(sample.payload()).unwrap();
```

### Complete Cross-Language Example: JSON

This example shows a Rust publisher and Python subscriber exchanging structured data through Zenoh using JSON.

**Rust publisher:**

```rust
use serde::Serialize;
use zenoh::{bytes::Encoding, Config};

#[derive(Serialize)]
struct Event {
    event_type: String,
    value: f64,
    timestamp_ms: u64,
}

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();

    let event = Event {
        event_type: "temperature".to_string(),
        value: 23.5,
        timestamp_ms: 1700000000000,
    };

    let json_bytes = serde_json::to_vec(&event).unwrap();

    session
        .put("events/temperature", json_bytes)
        .encoding(Encoding::APPLICATION_JSON)
        .await
        .unwrap();

    println!("published event");
}
```

**Python subscriber:**

```python
import json
import zenoh
from zenoh import Encoding

def on_event(sample):
    if sample.encoding == Encoding.APPLICATION_JSON:
        event = json.loads(sample.payload.to_string())
        print(f"type={event['event_type']} value={event['value']}")
    else:
        print(f"unexpected encoding: {sample.encoding}")

with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("events/**", on_event)
    print("listening for events... press Ctrl-C to stop")
    import time
    while True:
        time.sleep(1)
```

### Rust ZBytes ↔ Python bytes

At the raw bytes level, conversion is direct:

```rust
// Rust side: send raw bytes
let data: Vec<u8> = vec![0x01, 0x02, 0x03, 0x04];
session.put("raw/data", data).await.unwrap();
```

```python
# Python side: receive raw bytes
def on_sample(sample):
    raw: bytes = sample.payload.to_bytes()
    # raw is a Python bytes object
    print(f"received {len(raw)} bytes: {raw.hex()}")
```

```python
# Python side: send raw bytes
payload = bytes([0x01, 0x02, 0x03, 0x04])
session.put("raw/data", payload)
```

```rust
// Rust side: receive raw bytes
let bytes: std::borrow::Cow<[u8]> = sample.payload().to_bytes();
```

### C `z_bytes_t` Interoperability

In the C bindings, `z_bytes_t` wraps the same underlying `ZBuf`. The conversion semantics are:

```c
// C: create ZBytes from raw bytes (copies)
const uint8_t data[] = {1, 2, 3, 4};
z_owned_bytes_t payload;
z_bytes_from_buf(&payload, data, sizeof(data), NULL, NULL);

// C: access raw bytes
z_bytes_t view = z_bytes_loan(&payload);
const uint8_t *ptr;
size_t len;
z_bytes_get_contiguous_view(&view, &ptr, &len);

// Equivalent to Rust's to_bytes()
// Same format on wire — bytes are bytes
```

The zenoh-ext serialization format works from C as well, using the `zenoh_ext::z_bytes_serialize_from_*` family of functions, which produce the same wire format.

---

## Performance: When Copies Actually Happen

Understanding the copy profile of common operations:

### Publisher Side

| Operation | Copies | Notes |
|---|---|---|
| `ZBytes::from(vec)` | 0 | Vec is moved |
| `ZBytes::from(&[u8])` | 1 | Slice is copied to new Vec |
| `ZBytes::from("str")` | 1 | String bytes are copied |
| `ZBytes::from(String)` | 0 | String bytes are moved |
| `z_serialize(&value)` | 1+ | Data is encoded into writer's buffer |
| `writer.append(z)` | 0 | ZSlices transferred by reference |
| `writer.write_all(buf)` | 1 | Buf written into writer's vec |
| Send over network | 1 | Kernel socket buffer copy |
| Send over SHM | 0 | Data stays in shared memory |

### Subscriber Side

| Operation | Copies | Notes |
|---|---|---|
| Receive from network | 1 | Kernel → user space |
| Receive via SHM | 0 | Read from shared memory |
| `to_bytes()` (single-slice) | 0 | Returns `Cow::Borrowed` |
| `to_bytes()` (multi-slice) | 1 | Allocates contiguous buffer |
| `z_deserialize::<T>()` | 1 | Decoded into T's representation |
| `slices()` iteration | 0 | Reference iteration |

### Minimizing Copies: Practical Rules

1. **Use `Vec<u8>` → `ZBytes::from(vec)` over `&[u8]` → `ZBytes::from(slice)`**: Avoid the up-front copy if you own the data.

2. **Use `writer.append()` to compose large messages**: If you're building a payload from multiple existing `ZBytes` instances, use `append()` to avoid intermediate copies.

3. **Use `slices()` iteration instead of `to_bytes()` for large multi-slice payloads**: Avoids allocating a contiguous copy.

4. **Use SHM for high-throughput intrahost communication**: This is the only path where the payload bytes themselves never move.

5. **Prefer `ZBytes::from(String)` over `ZBytes::from(string.as_str())`**: Moving avoids a copy.

6. **For cross-language JSON**: `serde_json::to_vec()` produces a `Vec<u8>` that can be moved into `ZBytes` with no additional copy.

---

## Format Decision Guide

```
Are you communicating across languages (Rust ↔ Python, Rust ↔ C, etc.)?
  ├── Yes, and you need a schema/types? → Use Protobuf (APPLICATION_PROTOBUF)
  ├── Yes, and you need human readability? → Use JSON (APPLICATION_JSON)
  ├── Yes, and you need compact binary? → Use CBOR (APPLICATION_CBOR)
  ├── Yes, and you're talking to ROS2? → Use CDR (APPLICATION_CDR)
  └── Yes, for simple structures only? → Use zenoh-ext with careful type mapping

Are you communicating Rust ↔ Rust (or Python ↔ Python) only?
  ├── Simple types (numbers, strings, tuples, vecs)? → Use z_serialize / ZENOH_SERIALIZED
  ├── Complex/versioned structs? → Use serde + JSON/CBOR/Protobuf
  └── Raw bytes are sufficient? → ZBytes directly, no encoding needed

Do you need maximum throughput on the same host?
  └── Use [shared memory](shared-memory-complete-guide.md) + ZENOH_BYTES
```

## See Also

- [Programming Model Guide](programming-model-guide.md) — the API context in which ZBytes and Encoding are used
- [Zenoh Ext Guide](zenoh-ext-guide.md) — the `z_serialize`/`z_deserialize` API for structured data
- [Performance Tuning Guide](performance-tuning-guide.md) — how serialization format choice affects throughput

### Encoding Constants Summary

| Scenario | Encoding to use |
|---|---|
| Raw bytes, no interpretation | `ZENOH_BYTES` (default) |
| UTF-8 text | `ZENOH_STRING` |
| zenoh-ext structured data | `ZENOH_SERIALIZED` |
| JSON | `APPLICATION_JSON` |
| Protobuf | `APPLICATION_PROTOBUF` |
| CBOR | `APPLICATION_CBOR` |
| YAML | `APPLICATION_YAML` |
| ROS2/DDS | `APPLICATION_CDR` |
| Images (PNG) | `IMAGE_PNG` |
| Video (H.264) | `VIDEO_H264` |
| Custom format | `Encoding::from("my/format")` |
