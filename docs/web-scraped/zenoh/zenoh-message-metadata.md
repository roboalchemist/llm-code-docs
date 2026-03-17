# Message Metadata & Attachments

Zenoh messages carry structured metadata alongside the payload. Some metadata fields are set by the protocol (timestamps, QoS), while the **attachment** field provides a user-controlled side channel for application-level metadata — correlation IDs, tracing spans, routing hints, or any key-value headers — without polluting the payload.

## Metadata Fields on a Sample

Every received `Sample` exposes the following metadata:

| Field | Type (Rust) | Set by | Description |
|---|---|---|---|
| `key_expr()` | `KeyExpr<'static>` | Publisher | The concrete key expression the data was published on |
| `encoding()` | `Encoding` | Publisher | MIME-like descriptor of the payload bytes |
| `kind()` | `SampleKind` | Publisher | `Put` or `Delete` |
| `timestamp()` | `Option<Timestamp>` | Router/Publisher | HLC timestamp; present if timestamping is enabled |
| `priority()` | `Priority` | Publisher | QoS priority level (RealTime through Background) |
| `congestion_control()` | `CongestionControl` | Publisher | `Drop` or `Block` on congestion |
| `express()` | `bool` | Publisher | Whether batching was bypassed |
| `attachment()` | `Option<ZBytes>` | Publisher | **User-defined opaque metadata** |
| `reliability()` | `Reliability` | Publisher | `Reliable` or `BestEffort` (unstable API) |

The `source_info()` field (unstable) carries a `SourceInfo` with publisher `ZenohId` and sequence number — useful for deduplication and origin tracking.

## Attachments: User-Defined Metadata

The attachment is an `Option<ZBytes>` — the same opaque byte container used for payloads. Zenoh does not inspect or interpret it. It travels alongside the payload through every hop and is available on the receiving `Sample`, `Query`, and `Reply`.

### When to Use Attachments

- **Correlation IDs**: link a request to its response across pub/sub
- **Tracing context**: propagate OpenTelemetry span IDs or trace headers
- **Source identification**: tag messages with a producer name or device ID
- **Routing hints**: application-level metadata that subscribers use for filtering
- **Schema version**: indicate which schema version the payload was serialised with

### When NOT to Use Attachments

- **Large data**: attachments count toward the `size_limit` in ACL/QoS rules — `serialized payload + serialized attachment` is evaluated together
- **Data that needs indexing**: storages and queryables do not index attachments — use key expression hierarchy instead
- **Security-sensitive fields**: attachments are not encrypted separately from the payload

## Publishing with Attachments

### Rust

```rust
use zenoh::bytes::ZBytes;

// Simple string attachment
session
    .put("sensors/temperature", "23.5")
    .encoding(Encoding::TEXT_PLAIN)
    .attachment("source=sensor-42")  // &str converts to ZBytes
    .await?;

// Structured attachment using ZBytes serialization
let mut attachment = ZBytes::new();
attachment.append(ZBytes::from("trace-id"));
attachment.append(ZBytes::from("abc-123-def"));
session
    .put("sensors/temperature", "23.5")
    .attachment(attachment)
    .await?;
```

On a declared publisher, the attachment is set per-put:

```rust
let publisher = session
    .declare_publisher("sensors/temperature")
    .priority(Priority::DataHigh)
    .await?;

publisher
    .put("23.5")
    .encoding(Encoding::TEXT_PLAIN)
    .attachment("source=sensor-42")
    .await?;
```

### Python

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    session.put(
        "sensors/temperature",
        b"23.5",
        encoding=zenoh.Encoding.TEXT_PLAIN(),
        attachment="source=sensor-42",  # str, bytes, or ZBytes
    )
```

### C

```c
z_publisher_put_options_t options;
z_publisher_put_options_default(&options);

// Serialize metadata into the attachment
int64_t metadata = 42;
z_owned_bytes_t attachment;
ze_serialize_int64(&attachment, metadata);
options.attachment = z_move(attachment);

z_owned_bytes_t payload;
z_bytes_copy_from_str(&payload, "23.5");
z_publisher_put(z_loan(pub), z_move(payload), &options);
// Both payload and attachment are consumed by z_publisher_put
```

## Reading Attachments

### Rust

```rust
let subscriber = session.declare_subscriber("sensors/**").await?;

while let Ok(sample) = subscriber.recv_async().await {
    println!("key: {}", sample.key_expr());
    println!("payload: {}", sample.payload().try_to_string().unwrap_or_default());

    if let Some(att) = sample.attachment() {
        let att_str = att.try_to_string().unwrap_or_else(|e| e.to_string().into());
        println!("attachment: {att_str}");
    }
}
```

### Python

```python
subscriber = session.declare_subscriber("sensors/**")

for sample in subscriber:
    print(f"key: {sample.key_expr}")
    print(f"payload: {bytes(sample.payload)}")
    if sample.attachment is not None:
        print(f"attachment: {bytes(sample.attachment)}")
```

## Attachments on Queries and Replies

Attachments are not limited to pub/sub. The `get()` and `reply()` builders also accept `.attachment()`:

```rust
// Query with attachment
let replies = session
    .get("sensors/**")
    .attachment("request-id=req-001")
    .await?;

// Queryable reading the attachment
let queryable = session
    .declare_queryable("sensors/**")
    .callback(|query| {
        if let Some(att) = query.attachment() {
            println!("query attachment: {}", att.try_to_string().unwrap_or_default());
        }
        query.reply("sensors/temp", "23.5")
            .attachment("response-id=resp-001")
            .await
            .unwrap();
    })
    .await?;
```

## Source Info (Unstable)

The `source_info` field provides publisher origin tracking:

```rust
// Set on publish (unstable feature)
publisher
    .put("23.5")
    .source_info(SourceInfo { ... })
    .await?;

// Read on receive
if let Some(info) = sample.source_info() {
    println!("from: {:?}, seq: {:?}", info.source_id, info.source_sn);
}
```

This is useful for deduplication in networks with redundant paths — if two copies of the same message arrive via different routes, the `(source_id, source_sn)` pair identifies them as duplicates.

## Wire Format and Overhead

Attachments are serialized as `ZBytes` and carried in the zenoh wire protocol alongside the payload. Key overhead considerations:

- **Size limit enforcement**: ACL `size_limit` rules evaluate `serialized payload + serialized attachment` together. Messages exceeding the limit are **dropped silently** — no error is returned to the publisher.
- **No compression**: attachments are not compressed by the protocol. Keep them small.
- **Zero-copy path**: like payloads, attachments benefit from zenoh's zero-copy buffer design for local (same-session) delivery.
- **Routing transparency**: routers forward attachments without inspecting them. They do not appear in admin space queries or storage backends.

## Comparison: Attachment vs Encoding vs Key Expression

| Mechanism | Purpose | Inspected by routers? | Available for queries? |
|---|---|---|---|
| **Key expression** | Routing and subscription matching | Yes | Yes (storages index by key) |
| **Encoding** | Payload format hint for deserialization | No | No (pass-through) |
| **Attachment** | Application-level metadata side channel | No (but counted for size_limit) | No (pass-through) |
| **Timestamp** | Ordering and conflict resolution | Yes (re-stamping, consolidation) | Yes (latest-value queries) |
| **QoS fields** | Priority, reliability, congestion control | Yes (scheduling, queuing) | No |

## Best Practices

1. **Keep attachments small** — use them for IDs and tags, not data. A typical correlation ID or trace header is tens of bytes.
2. **Use a consistent serialization format** — agree on a convention (e.g., `key=value` pairs, or a compact binary format) across all producers and consumers.
3. **Don't duplicate key expression information** — if the metadata can be encoded in the key hierarchy (`sensors/{device_id}/temperature`), prefer that over an attachment.
4. **Check for `None`** — attachments are optional. Always handle the case where `sample.attachment()` returns `None`.
5. **Don't rely on attachments for persistence** — storage backends (InfluxDB, RocksDB, S3) store payloads, not attachments. If metadata must survive storage round-trips, embed it in the payload.

## See Also

- [Sample & Data Model](concept-sample.md) — the container that carries payload, encoding, and metadata together
- [Encoding & ZBytes](concept-encoding.md) — the payload format descriptor
- [QoS](concept-qos.md) — priority, reliability, congestion control, express mode
- [Timestamps & HLC](concept-timestamps.md) — timestamp metadata and ordering
- [Serialization](serialization-complete-guide.md) — ZBytes serialization patterns
