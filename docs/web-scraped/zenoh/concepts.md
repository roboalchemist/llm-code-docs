## Zenoh Protocol Comprehensive Reference

This document serves as the definitive reference for understanding and working with the Zenoh protocol. It includes detailed descriptions of all major components, their purpose, use cases, and provides illustrative Rust pseudocode examples.

---

## Session

### Overview

A Session is a central concept in Zenoh, representing a logical connection between a Zenoh application and the underlying transport infrastructure. It manages the lifecycle of connected entities such as publishers, subscribers, queriers, and queryables.

### Lifecycle

- **Opening a Session**: Establishes connections to the Zenoh network.
- **Closing a Session**: Cleans up resources and disconnects from the network.

### Builder Pattern

Zenoh uses a builder pattern for creating and managing sessions, allowing configuration through method chaining.

### Pseudocode Example

```rust
let session = zenoh::Session::builder()
    .locator("tcp/localhost:7447")
    .open()
    .await.unwrap();

// Perform operations with session

session.close().await.unwrap();
```

---

## Key Expressions

### Overview

Key Expressions are used to specify paths in the Zenoh data space, supporting pattern matching with wildcards and operators.

### Syntax and Variants

- **Wildcards**: `*` matches a single level, `**` matches multiple levels.
- **Operators**: Support for concatenation, intersection, etc.
- **Canonicalization**: Transformation into a standard form.

### Pseudocode Example

```rust
let key_expr = zenoh::KeyExpr::new("temperature/sensors/**");
```

---

## Selector

### Overview

Selectors extend Key Expressions with parameters for querying and retrieving data under specific conditions.

### Pseudocode Example

```rust
let selector = zenoh::Selector::new("temperature/sensors/*?location=room1");
```

---

## Publisher

### Overview

Publishers are responsible for declaring intents to send data under specified keys.

### Options

- **Priority**: Different levels from `RealTime` to `Background`.
- **Reliability**: `BestEffort` or `Reliable`.
- **Congestion Control**: `Drop`, `Block`, `BlockFirst`.
- **Express**: Determines batching behavior.

### Pseudocode Example

```rust
let publisher = session.declare_publisher("example/key")
    .priority(Priority::RealTime)
    .reliability(Reliability::Reliable)
    .congestion_control(CongestionControl::Block)
    .encoding(Encoding::APPLICATION_JSON)
    .await.unwrap();
    
publisher.put("Hello Zenoh!").await.unwrap();
```

---

## Subscriber

### Overview

Subscribers listen for data published under specified key expressions.

### Handlers

- **FIFO/Ring**: Use channels for ordered data processing.
- **Callback**: Direct function invocation on data reception.

### Locality Filtering

Filtering subscriptions to session-local, remote, or any origin.

### Pseudocode Example

```rust
let subscriber = session.declare_subscriber("example/key")
    .callback(|sample| {
        println!("Received: {:?}", sample.payload());
    })
    .await.unwrap();
```

---

## Queryable

### Overview

Queryables respond to queries targeted at key expressions they match.

### Pseudocode Example

```rust
let queryable = session.declare_queryable("example/key")
    .callback(|query| {
        query.reply(Reply::Ok("Response")).await.unwrap();
    })
    .await.unwrap();
```

---

## Query / Get

### Overview

Queries request data from the Zenoh network, either through a session or a querier, using a selector and optional parameters.

### ConsolidationMode

Controls how multiple replies are handled.

### Pseudocode Example

```rust
let replies = session.get("example/key?param=value")
    .consolidation(ConsolidationMode::Auto)
    .await.unwrap();

while let Ok(reply) = replies.recv_async().await {
    println!("Reply: {:?}", reply.result());
}
```

---

## Querier

### Overview

A Querier is used for repeatedly querying the Zenoh network with a more persistent pattern compared to ad-hoc `get`.

### Pseudocode Example

```rust
let querier = session.declare_querier("example/key")
    .target(QueryTarget::All)
    .await.unwrap();

let replies = querier.get().await.unwrap();
```

---

## Liveliness

### Overview

Liveliness involves detecting the presence of tokens and subscribers, ensuring entities are active.

### Pseudocode Example

```rust
let token = session.liveliness()
    .declare_token("example/key")
    .await.unwrap();

let subscriber = session.liveliness()
    .declare_subscriber("example/key")
    .callback(|sample| {
        println!("Live: {:?}", sample);
    })
    .await.unwrap();
```

---

## Matching

### Overview

Matching components provide awareness of subscribers and queryables, indicating when data recipients are available.

### Pseudocode Example

```rust
let listener = publisher.matching_listener()
    .callback(|status| {
        if status.matching() {
            println!("Subscribers available");
        } else {
            println!("No subscribers");
        }
    })
    .await.unwrap();
```

---

## Scouting

### Overview

Scouting facilitates discovery of peers and topologies, using multicast or gossip mechanisms.

### Pseudocode Example

```rust
session.scout().await.unwrap();
```

---

## WhatAmI

### Overview

Defines modes for entities: Router, Peer, or Client, each serving different roles in Zenoh networks.

### When to Use

- **Router**: For centralize routing of messages.
- **Peer**: For direct communication without intermediaries.
- **Client**: For lightweight, endpoint communication.

### Pseudocode Example

```rust
let whatami = WhatAmI::Router;
```

---

## Sample

### Overview

Samples are the data units exchanged in Zenoh, encapsulating metadata such as encoding, timestamp, and QoS settings.

### Components

- **SampleKind**: `Put` for sending data, `Delete` for removing.
- **Encoding**: Indicates data format, similar to MIME types.
- **Priority, Reliability, Congestion Control, Locality**: Configurable QoS aspects.
- **Timestamp and Attachments**: Metadata for time and additional data.

### Pseudocode Example

```rust
let sample = Sample::builder("example/key", "payload data")
    .kind(SampleKind::Put)
    .encoding(Encoding::APPLICATION_JSON)
    .priority(Priority::Normal)
    .reliability(Reliability::Reliable)
    .timestamp(current_timestamp())
    .build();
```

---

## ZBytes

### Overview

ZBytes is a zero-copy payload container used in Zenoh for efficient data serialization and transmission, leveraging the zenoh-ext library.

### Pseudocode Example

```rust
let payload = ZBytes::from("example data");
```

---

## Encoding

### Overview

Encoding in Zenoh refers to the content-type system used to handle various data formats, akin to MIME types.

### Pseudocode Example

```rust
let encoding = Encoding::APPLICATION_JSON;
```

---

## Builders

### Overview

Zenoh employs builder patterns for entity declarations, facilitating method chaining for configuration and instantiation.

### Pseudocode Example

```rust
let publisher = session.declare_publisher("example/key")
    .congestion_control(CongestionControl::Drop)
    .priority(Priority::High)
    .await.unwrap();
```

---

This documentation provides the foundational knowledge required to leverage Zenoh's capabilities effectively. For further details, refer to individual component documentation and the provided source code snippets.