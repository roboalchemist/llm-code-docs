# Zenoh Wire Protocol Internals

This guide documents Zenoh's wire protocol at the byte level, covering framing, message types, routing,
reliability, batching, compression, and overhead analysis. All byte layouts are taken directly from the
source code in `commons/zenoh-protocol/src/` and `commons/zenoh-codec/src/`.

---

## Table of Contents

- [Protocol Layers](#protocol-layers)
- [Variable-Length Encoding (VLE)](#variable-length-encoding-vle)
- [Framing](#framing)
  - [The Batch Concept](#the-batch-concept)
  - [Batch Size](#batch-size)
  - [Maximum Message Size](#maximum-message-size)
  - [The Frame Message](#the-frame-message)
  - [Fragmentation](#fragmentation)
  - [Sequence Numbers](#sequence-numbers)
- [Transport Layer Messages](#transport-layer-messages)
  - [Message ID Table](#message-id-table)
  - [INIT (InitSyn / InitAck) — ID: 0x01](#init-initsyn-initack-id-0x01)
  - [OPEN (OpenSyn / OpenAck) — ID: 0x02](#open-opensyn-openack-id-0x02)
  - [CLOSE — ID: 0x03](#close-id-0x03)
  - [KEEP_ALIVE — ID: 0x04](#keep_alive-id-0x04)
  - [JOIN — ID: 0x07](#join-id-0x07)
- [Network Layer Messages](#network-layer-messages)
  - [Message ID Table](#message-id-table)
  - [Common Fields in Network Messages](#common-fields-in-network-messages)
  - [Push — ID: 0x1d](#push-id-0x1d)
  - [Request — ID: 0x1c](#request-id-0x1c)
  - [Response — ID: 0x1b](#response-id-0x1b)
  - [ResponseFinal — ID: 0x1a](#responsefinal-id-0x1a)
  - [Interest — ID: 0x19](#interest-id-0x19)
  - [Declare — ID: 0x1e](#declare-id-0x1e)
- [Zenoh Payload Messages](#zenoh-payload-messages)
  - [Put](#put)
  - [Delete (Del)](#delete-del)
- [Session Handshake](#session-handshake)
- [Scouting and Discovery](#scouting-and-discovery)
  - [Scout](#scout)
  - [Hello](#hello)
- [Routing](#routing)
  - [Interest-Based Routing](#interest-based-routing)
  - [Key Expression Mapping](#key-expression-mapping)
  - [Linkstate Routing](#linkstate-routing)
  - [Wildcard Fanout](#wildcard-fanout)
  - [Router-to-Router Link State Exchange](#router-to-router-link-state-exchange)
- [Reliability](#reliability)
  - [Channels: Reliable vs. Best-Effort](#channels-reliable-vs-best-effort)
  - [What "Reliable" Guarantees](#what-reliable-guarantees)
  - [Congestion Control](#congestion-control)
  - [Non-Blocking Fault-Tolerant Reliability (NBFTReliability)](#non-blocking-fault-tolerant-reliability-nbftreliability)
  - [Queue Configuration](#queue-configuration)
- [Batching](#batching)
  - [How Batching Works](#how-batching-works)
  - [Adaptive Batching](#adaptive-batching)
  - [Express Flag](#express-flag)
- [Compression](#compression)
  - [Configuration](#configuration)
  - [Algorithm: LZ4](#algorithm-lz4)
  - [Interaction with Low-Latency Mode](#interaction-with-low-latency-mode)
  - [When Compression Helps vs. Hurts](#when-compression-helps-vs-hurts)
- [Protocol Overhead Analysis](#protocol-overhead-analysis)
  - [Minimum Push Message Overhead](#minimum-push-message-overhead)
  - [Overhead with Optional Fields](#overhead-with-optional-fields)
  - [Comparison: Zenoh vs. Other Protocols](#comparison-zenoh-vs-other-protocols)
  - [Declaring Key Expressions to Minimize Overhead](#declaring-key-expressions-to-minimize-overhead)
- [Configuration Reference](#configuration-reference)
  - [transport.link.tx section](#transportlinktx-section)
  - [transport.unicast section](#transportunicast-section)
  - [Example: Low-Overhead High-Throughput Configuration](#example-low-overhead-high-throughput-configuration)
  - [Example: Low-Latency Real-Time Configuration](#example-low-latency-real-time-configuration)
  - [Rust API: Observing QoS and Reliability](#rust-api-observing-qos-and-reliability)
- [Summary: Key Numbers](#summary-key-numbers)


---


## Protocol Layers

Zenoh uses a two-layer protocol stack:

```
┌─────────────────────────────────────────────────┐
│  Application API  (put/get/subscribe/query)      │
├─────────────────────────────────────────────────┤
│  Network Layer    (Push/Request/Response/Declare) │
├─────────────────────────────────────────────────┤
│  Transport Layer  (Frame/Fragment/Init/Open/...) │
├─────────────────────────────────────────────────┤
│  Link Layer       (TCP/UDP/TLS/QUIC/SHM/...)    │
└─────────────────────────────────────────────────┘
```

- **Transport layer** handles session establishment, keepalives, and framing. Messages have IDs in the
  range `0x00–0x07`.
- **Network layer** carries the actual Zenoh operations. Messages have IDs in the range `0x19–0x1f`.
  They are *always* carried inside a Transport Frame or Fragment.

IDs are designed to never collide between layers (see `transport/mod.rs` `id` module and
`network/mod.rs` `id` module).

---

## Variable-Length Encoding (VLE)

All integers (sequence numbers, lengths, IDs) are encoded as **variable-length little-endian** integers.
The codec is in `commons/zenoh-codec/src/core/zint.rs`.

Each byte contributes 7 bits of value. If bit 7 (MSB) is set, more bytes follow:

```
Value range          Wire bytes
0–127                1 byte:  [0xxxxxxx]
128–16383            2 bytes: [1xxxxxxx] [0xxxxxxx]
16384–2097151        3 bytes: [1xxxxxxx] [1xxxxxxx] [0xxxxxxx]
...
Up to 2^63           9 bytes maximum
```

**VLE byte counts by value:**

| Max value      | Wire bytes |
|----------------|-----------|
| 127 (0x7F)     | 1         |
| 16383 (0x3FFF) | 2         |
| 2097151        | 3         |
| 268435455      | 4         |

**Practical impact:**

- Sequence numbers 0–127 cost 1 byte, 128–16383 cost 2 bytes.
- A declared key expression ID (ExprId = u16) 0–127 costs 1 byte on the wire.
- Payload length fields use VLE bounded to u32, so lengths 0–127 cost 1 byte.

---

## Framing

### The Batch Concept

Zenoh's fundamental transmission unit is a **batch**. A batch is a buffer up to `batch_size` bytes
that accumulates one or more complete network messages. Batches are sent atomically.

```
┌────────────────────────────────────────────────────────┐
│ Batch (≤ batch_size bytes)                             │
│  ┌──────────────────────────────────────────────────┐  │
│  │ [2-byte length prefix on stream transports only] │  │
│  ├──────────────────────────────────────────────────┤  │
│  │ FRAME header (1 byte header + VLE sn)            │  │
│  ├──────────────────────────────────────────────────┤  │
│  │ NetworkMessage 1 (variable length)               │  │
│  ├──────────────────────────────────────────────────┤  │
│  │ NetworkMessage 2 (variable length)               │  │
│  ├──────────────────────────────────────────────────┤  │
│  │ NetworkMessage N ...                             │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

On **stream-oriented transports** (TCP, TLS, QUIC, UNIX socket), each batch is prefixed with a
2-byte little-endian length field. This is necessary because stream transports do not preserve message
boundaries. On **datagram transports** (UDP), no length prefix is added since each datagram is
self-delimiting.

### Batch Size

**Config key:** `transport.link.tx.batch_size`
**Type:** `u16`
**Default:** 65535 (unicast), platform-dependent for multicast (8192 on Linux/Windows, 9216 on macOS)
**Range:** 1–65535

The batch size is negotiated during session establishment (INIT message). The minimum of the two
peers' batch sizes is used. This means you can reduce overhead by lowering batch size at the cost
of constraining maximum message sizes.

```rust
// From transport/mod.rs
pub type BatchSize = u16;

pub mod batch_size {
    pub const UNICAST: BatchSize = BatchSize::MAX;  // 65535
    pub const MULTICAST: BatchSize = 8_192;
}
```

A message that does not fit in a batch is **fragmented** (see Fragmentation below).

### Maximum Message Size

The absolute maximum batch size is 65535 bytes (`u16::MAX`). Messages larger than the batch size
are split into fragments. The receiver can reassemble up to `transport.link.rx.max_message_size`
bytes (default: 1 GiB).

### The Frame Message

A `Frame` message wraps one or more complete `NetworkMessage` objects. Its wire layout is:

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|X|R|  FRAME  |   (ID = 0x05)
+-+-+-+---------+
%    seq num    %   (VLE, 1–5 bytes depending on SN resolution)
+---------------+
~  [FrameExts]  ~ if Z==1
+---------------+
~  [NetworkMsg] ~   (one or more, fills remainder of batch)
+---------------+
```

Flag bits:
- **R** (bit 5 = 0x20): Reliable. If 1, this frame is on the **reliable channel**. If 0, it is
  on the **best-effort channel**.
- **Z** (bit 7 = 0x80): Extensions follow. Currently only one extension type exists: QoS (ID=0x1),
  which carries a 1-byte priority value.
- **X** (bit 6): Reserved.

The `seq num` is a VLE-encoded `TransportSn` (type alias for `u32`). With the default 32-bit
sequence number resolution, small sequence numbers cost 1 byte; larger values cost 2–5 bytes.

### Fragmentation

When a `NetworkMessage` is too large to fit in a single batch, it is split into multiple `Fragment`
messages. The Fragment wire layout is:

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|M|R| FRAGMENT|   (ID = 0x06)
+-+-+-+---------+
%    seq num    %   (VLE)
+---------------+
~   [FragExts]  ~ if Z==1
+---------------+
~      [u8]     ~   (raw bytes, fills remainder of batch)
+---------------+
```

Flag bits:
- **R** (bit 5): Reliable channel.
- **M** (bit 6): More. If 1, more fragments follow. The final fragment has M=0.
- **Z** (bit 7): Extensions follow.

Extensions (since patch version ≥ 1):
- **First** (ID=0x2, ZExtUnit): Marks the *first* fragment of a fragmented message.
- **Drop** (ID=0x3, ZExtUnit): Signals that remaining fragments have been dropped (e.g., due to
  congestion control).

Fragment reassembly: The receiver accumulates fragments in order by sequence number. When a fragment
with M=0 arrives, the reassembled buffer is deserialized as a `NetworkMessage`.

Each fragment occupies exactly one batch. The fragment payload fills the batch from the end of the
Fragment header to the batch boundary. The `FrameHeader` codec writes the header, then calls
`siphon` to copy as much of the fragmented message's bytes as fit into the remaining buffer space.

### Sequence Numbers

Sequence numbers are negotiated during the INIT handshake. The `resolution` field is a packed byte:

```rust
// From core/resolution.rs
pub enum Bits {
    U8  = 0b00,   // 8-bit SN:  256 values
    U16 = 0b01,   // 16-bit SN: 65536 values
    U32 = 0b10,   // 32-bit SN: 4 billion values
    U64 = 0b11,   // 64-bit SN: 18 quintillion values
}
// Bits 0-1: Frame/fragment SN resolution
// Bits 2-3: Request ID resolution
```

The default resolution for both Frame SN and Request ID is **32 bits** (U32). The two communicating
peers negotiate down to the minimum value both support.

**Wire cost of sequence numbers at default 32-bit resolution:**

| SN value range    | VLE bytes |
|-------------------|-----------|
| 0–127             | 1         |
| 128–16383         | 2         |
| 16384–2097151     | 3         |
| 2097152–268435455 | 4         |
| 268435456–4294967295 | 5     |

With 32-bit SNs, the SN wraps around after ~4 billion frames. At 1 million frames/second, rollover
occurs in ~71 minutes. The receiver must handle rollover by treating a received SN much lower than
the expected SN as a post-rollover sequence number.

---

## Transport Layer Messages

Transport messages handle session lifecycle, keepalive, and batching. All transport message IDs are
in the low range (0x00–0x07) to avoid collision with network message IDs (0x19–0x1f).

### Message ID Table

| ID    | Name       | Direction        | Purpose                                    |
|-------|------------|------------------|--------------------------------------------|
| 0x00  | OAM        | Both             | Operations and management (internal)       |
| 0x01  | INIT       | Both             | Unicast session initiation handshake       |
| 0x02  | OPEN       | Both             | Unicast session open handshake             |
| 0x03  | CLOSE      | Both             | Session termination                        |
| 0x04  | KEEP_ALIVE | Both             | Link liveness                              |
| 0x05  | FRAME      | Both             | Transport frame (wraps network messages)   |
| 0x06  | FRAGMENT   | Both             | Fragment of a large message                |
| 0x07  | JOIN       | Both             | Multicast session advertisement            |

### INIT (InitSyn / InitAck) — ID: 0x01

Used only for **unicast** transports. Establishes the basic session parameters.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|S|A|   INIT  |
+-+-+-+---------+
|    version    |   (1 byte, must be 9 / 0x09)
+---------------+
|zid_len|x|x|wai|   (* WhatAmI, # ZID length)
+-------+-+-+---+
~      [u8]     ~   ZenohID of sender (1-16 bytes)
+---------------+
|x|x|x|x|rid|fsn| \ SN/ID resolution (if S==1)
+---------------+  |
|      u16      |  | Batch Size (if S==1)
|               | /
+---------------+
~    <u8;z16>   ~ if A==1 — Cookie (for InitAck)
+---------------+
~   [InitExts]  ~ if Z==1
+---------------+
```

Flags:
- **A** (bit 5): If 0, this is InitSyn; if 1, this is InitAck.
- **S** (bit 6): If 1, size parameters (SN resolution + batch size) are present.
- **Z** (bit 7): Extensions follow.

WhatAmI values (2-bit field):
- `0b00` = Router
- `0b01` = Peer
- `0b10` = Client

ZID length: encoded as `(zid_len field) + 1`. So a 16-byte ZID encodes `zid_len = 15`.

Extensions in INIT:
- **QoS** (0x1): Negotiates QoS priority channels.
- **Shm** (0x2): Challenges shared memory capability (optional build feature).
- **Auth** (0x3): Authentication challenge.
- **MultiLink** (0x4): Multi-link negotiation.
- **LowLatency** (0x5): Negotiates low-latency transport mode.
- **Compression** (0x6): Negotiates LZ4 compression.
- **Patch** (0x7): Protocol patch version (≥1 enables fragment First/Drop markers).

### OPEN (OpenSyn / OpenAck) — ID: 0x02

Finalizes a unicast session after INIT.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|T|A|   OPEN  |
+-+-+-+---------+
%     lease     %   (VLE, milliseconds or seconds depending on T flag)
+---------------+
%  initial_sn   %   (VLE, initial sequence number)
+---------------+
~    <u8;z16>   ~ if A==0 — Cookie (echo from InitAck, OpenSyn only)
+---------------+
~   [OpenExts]  ~ if Z==1
+---------------+
```

Flags:
- **A** (bit 5): OpenSyn if 0, OpenAck if 1.
- **T** (bit 6): Lease unit — if 1, lease is in seconds; if 0, milliseconds.

The `lease` is the link keepalive period. If no data is received within the lease period, the link
is considered dead. The default lease is 10000 ms (10 seconds). KeepAlive messages are sent at
`lease / keep_alive` intervals (default: 10000 / 4 = 2500 ms).

The `initial_sn` is the first sequence number to be used on this session. It is random, preventing
replay attacks. It must be compatible with the SN resolution negotiated in INIT.

### CLOSE — ID: 0x03

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|X|S|  CLOSE  |
+-+-+-+---------+
|     reason    |   (1 byte)
+---------------+
~  [CloseExts]  ~ if Z==1
+---------------+
```

Flag **S** (bit 5): If 1, close the whole session; if 0, close only this link.

Reason codes:
- `0x00` = GENERIC
- `0x01` = UNSUPPORTED
- `0x02` = INVALID
- `0x03` = MAX_SESSIONS
- `0x04` = MAX_LINKS
- `0x05` = EXPIRED (lease timeout)
- `0x06` = UNRESPONSIVE
- `0x07` = CONNECTION_TO_SELF

Total wire size: 2 bytes minimum (header + reason).

### KEEP_ALIVE — ID: 0x04

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|X|X| KALIVE  |
+-+-+-+---------+
~  [KAliveExts] ~ if Z==1
+---------------+
```

Minimum wire size: 1 byte (header only, no body). KeepAlive is sent when no other data has been
transmitted during the last keepalive interval. The interval is `lease / keep_alive` (default: 2500 ms).

Per the ITU-T G.8013/Y.1731 specification, the keepalive interval is set to `lease / 4` so that
a link is declared dead after receiving nothing for 3.5 × interval = ~8750 ms, which is less than
the 10-second lease.

### JOIN — ID: 0x07

Used only on **multicast** transports to advertise transport parameters without a handshake.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|S|T|   JOIN  |
+-+-+-+---------+
|    version    |
+---------------+
|zid_len|x|x|wai|
+---------------+
~     [u8]      ~   ZenohID
+---------------+
|x|x|x|x|rid|fsn| \ SN/ID resolution (if S==1)
+---------------+  |
|      u16      |  | Batch Size (if S==1)
|               | /
+---------------+
%     lease     %   (VLE)
+---------------+
%    next_sn    %   (VLE, for single-priority) or ext_qos with per-priority SNs
+---------------+
~   [JoinExts]  ~ if Z==1
+---------------+
```

JOIN is sent periodically (default: every 2500 ms) so new multicast group members can learn about
existing participants without a handshake. Default multicast batch size is 8192 bytes.

---

## Network Layer Messages

Network messages are always wrapped inside Transport `Frame` or `Fragment` messages. They carry
the actual Zenoh operations.

### Message ID Table

| ID    | Name           | Direction            | Purpose                                     |
|-------|----------------|----------------------|---------------------------------------------|
| 0x1d  | PUSH           | Publisher → Network  | Published data (Put or Delete)              |
| 0x1c  | REQUEST        | Querier → Queryable  | Query/get request                           |
| 0x1b  | RESPONSE       | Queryable → Querier  | Reply to a query                            |
| 0x1a  | RESPONSE_FINAL | Queryable → Querier  | Signals end of replies for a request        |
| 0x19  | INTEREST       | Any → Any            | Request declarations from a peer            |
| 0x1e  | DECLARE        | Any → Any            | Subscriber/publisher/queryable declarations |
| 0x1f  | OAM            | Internal             | Operations and management                   |

### Common Fields in Network Messages

All network messages share a common structure:

1. **Header byte** (1 byte): message ID in bits 0–4, flag bits in bits 5–7.
2. **WireExpr** (key expression): a `scope` (VLE-encoded u16 ExprId) plus optional suffix string.
3. **Extensions** (variable, conditional on Z flag in header): QoS, Timestamp, NodeId.
4. **Payload** (variable).

**WireExpr encoding:**

```
~ key_scope:z16 ~   VLE-encoded ExprId (0 = global scope, uses full string suffix)
+---------------+
~  key_suffix   ~   if N flag set in header — length-prefixed UTF-8 string
+---------------+
```

When `scope == 0`, the full key expression string is in the suffix. When `scope > 0`, it refers to
a previously declared key expression (via DeclareKeyExpr), and the suffix is either empty (exact
match) or an additional path component.

### Push — ID: 0x1d

Carries a published value (Put) or a deletion (Delete).

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|M|N|  PUSH   |
+-+-+-+---------+
~ key_scope:z16 ~   VLE ExprId
+---------------+
~  key_suffix   ~   if N==1 — length-prefixed string
+---------------+
~  [push_exts]  ~   if Z==1 (QoS, Timestamp, NodeId)
+---------------+
~   PushBody    ~   Put or Delete
+---------------+
```

Flags:
- **N** (bit 5): Named — key suffix is present.
- **M** (bit 6): Mapping — if 1, key expr mapping is sender-declared; if 0, receiver-declared.
- **Z** (bit 7): Extensions follow.

Extensions:
- **QoS** (ID=0x1, ZExtZ64): 1-byte value encoding priority (3 bits), congestion control (D/F flags),
  and express flag (E flag). Only present if non-default.
- **Timestamp** (ID=0x2, ZExtZBuf): uHLC timestamp — 8-byte NTP64 time + VLE-encoded ID size +
  1–16 byte ZenohID. Only present if timestamping is enabled.
- **NodeId** (ID=0x3, ZExtZ64): 2-byte u16 node ID for routing loops. Only present when non-zero
  (i.e., the message was forwarded by a router).

The `QoSType` extension byte layout (1 byte, bits):
```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|0|r|F|E|D|prio |
+---------------+
- prio: Priority class (3 bits, 0–7)
- D:    Don't drop — CongestionControl::Block
- E:    Express — bypass batching, send immediately
- F:    BlockFirst — drop all but the first (unstable feature)
- r:    Reserved
```

### Request — ID: 0x1c

Carries a query (get) to a queryable.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|M|N| Request |
+-+-+-+---------+
~ request_id:z32~   VLE request ID (u32)
+---------------+
~ key_scope:z16 ~
+---------------+
~  key_suffix   ~   if N==1
+---------------+
~   [req_exts]  ~   if Z==1
+---------------+
~  RequestBody  ~   Query payload
+---------------+
```

Extensions:
- **QoS** (0x1): Same as Push.
- **Timestamp** (0x2): uHLC timestamp.
- **NodeId** (0x3): Router forwarding node.
- **Target** (0x4): QueryTarget enum — BestMatching (0), All (1), AllComplete (2).
- **Budget** (0x5): Maximum number of replies (NonZeroU32).
- **Timeout** (0x6): Duration in milliseconds.

Direction: Querier → routers → Queryable. Routers forward based on key expression matching
against declared queryables.

### Response — ID: 0x1b

Carries a reply from a queryable back to the querier.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|M|N| Response|
+-+-+-+---------+
~ request_id:z32~   Echoes the request ID
+---------------+
~ key_scope:z16 ~
+---------------+
~  key_suffix   ~   if N==1
+---------------+
~  [reply_exts] ~   if Z==1
+---------------+
~  ResponseBody ~   Reply or Error
+---------------+
```

Extensions:
- **QoS** (0x1): Priority/express.
- **Timestamp** (0x2): uHLC timestamp.
- **ResponderId** (0x3, ZExtZBuf): Global entity ID (ZenohID + EntityId) identifying which queryable
  generated this response.

Direction: Queryable → routers → Querier (routed back using the request_id).

### ResponseFinal — ID: 0x1a

Signals that all replies for a given request have been sent.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|X|X| ResFinal|
+-+-+-+---------+
~ request_id:z32~   Matches the original request ID
+---------------+
~  [reply_exts] ~   if Z==1
+---------------+
```

Minimum wire size: 1 header + 1 byte (request_id ≤ 127) = 2 bytes.

### Interest — ID: 0x19

Requests current and/or future declarations from a peer.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|Mod|INTEREST |
+-+-+-+---------+
~    id:z32     ~   Interest ID (u32)
+---------------+
|A|M|N|R|T|Q|S|K|   Options byte (if Mod != Final)
+---------------+
~ key_scope:z16 ~   if R==1 (restricted to key expr)
+---------------+
~  key_suffix   ~   if R==1 && N==1
+---------------+
~  [int_exts]   ~   if Z==1
+---------------+
```

Mode (2-bit field in header bits 5–6):
- `0b00` = Final — terminates a previous CurrentFuture or Future interest.
- `0b01` = Current — request current declarations only.
- `0b10` = Future — request future declarations only.
- `0b11` = CurrentFuture — request current + subscribe to future.

Options byte bits:
- **K** (bit 0): Key expressions
- **S** (bit 1): Subscribers
- **Q** (bit 2): Queryables
- **T** (bit 3): Tokens (liveliness)
- **R** (bit 4): Restricted to a specific key expression
- **N** (bit 5): Key expression has name/suffix
- **M** (bit 6): Key expression mapping is sender's
- **A** (bit 7): Aggregate replies

### Declare — ID: 0x1e

Carries a single declaration (subscription, publication, queryable, key expression, etc.).

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|X|I| DECLARE |
+-+-+-+---------+
~interest_id:z32~   if I==1 (response to a specific Interest)
+---------------+
~  [decl_exts]  ~   if Z==1 (QoS, Timestamp, NodeId)
+---------------+
~  declaration  ~   One of the DeclareBody variants
+---------------+
```

Flag **I** (bit 5): If 1, this declare is in response to an Interest (interest_id present).

**DeclareBody variants and their IDs:**

| ID   | Body Type            | Wire Layout                              |
|------|----------------------|------------------------------------------|
| 0x00 | DeclareKeyExpr       | expr_id:z16 + key_scope:z16 + [suffix]   |
| 0x01 | UndeclareKeyExpr     | expr_id:z16                              |
| 0x02 | DeclareSubscriber    | subs_id:z32 + key_scope:z16 + [suffix]   |
| 0x03 | UndeclareSubscriber  | subs_id:z32                              |
| 0x04 | DeclareQueryable     | qbls_id:z32 + key_scope:z16 + [suffix]   |
| 0x05 | UndeclareQueryable   | qbls_id:z32                              |
| 0x06 | DeclareToken         | token_id:z32 + key_scope:z16 + [suffix]  |
| 0x07 | UndeclareToken       | token_id:z32                             |
| 0x1A | DeclareFinal         | (no body, signals end of Interest reply) |

Each sub-declaration has its own 1-byte header with flags for N (named, suffix present) and M
(mapping). The body type ID occupies bits 0–4 of this header byte.

**DeclareKeyExpr** maps a full key expression string to a short 16-bit ID. Once declared, all
subsequent Push/Request/Response messages on the same session can use the 16-bit ID instead of the
full string, dramatically reducing overhead for frequently used key expressions.

---

## Zenoh Payload Messages

Inside a Push or Response body, the actual application data is carried as a `Put` or `Del` message.

### Put

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|E|T|   PUT   |
+-+-+-+---------+
~   timestamp   ~   if T==1 — uHLC: 8-byte NTP64 + VLE length + 1-16 byte ZenohID
+---------------+
~   encoding    ~   if E==1 — VLE prefix + optional string suffix
+---------------+
~  [put_exts]   ~   if Z==1 (SourceInfo, SHM, Attachment)
+---------------+
~    payload    ~   VLE-bounded length + raw bytes
+---------------+
```

Flags:
- **T** (bit 5): Timestamp present.
- **E** (bit 6): Encoding present (non-default).
- **Z** (bit 7): Extensions follow.

The payload is encoded as a VLE length followed by raw bytes.

**Encoding wire format:** A VLE-encoded prefix ID (maps to IANA media type) plus an optional
length-prefixed string suffix for the schema. The default encoding (no schema, no prefix) requires
0 bytes.

### Delete (Del)

Same structure as Put but with no payload bytes. The `Del` header signals deletion of all matching
resources.

---

## Session Handshake

Unicast session establishment requires a 4-message exchange:

```
Initiator (A)               Responder (B)
     |        InitSyn          |
     |------------------------->|
     |        InitAck           |
     |<-------------------------|
     |        OpenSyn           |
     |   (echo cookie from      |
     |    InitAck + initial SN) |
     |------------------------->|
     |        OpenAck           |
     |   (lease + initial SN)   |
     |<-------------------------|
     |   Session Active         |
```

**What is negotiated:**
1. **Protocol version** (must match).
2. **WhatAmI** (Router/Peer/Client).
3. **ZenohID** of each peer.
4. **SN resolution** (min of both peers' configured value).
5. **Batch size** (min of both peers' configured value).
6. **Optional capabilities**: QoS, SHM, Auth, MultiLink, LowLatency, Compression.

The cookie in InitAck is an opaque blob chosen by the responder. The initiator echoes it in OpenSyn
to prove continuity (anti-amplification). The cookie is never reused.

**Multicast sessions** use JOIN instead of INIT/OPEN. JOIN is broadcast periodically with the current
SN state, allowing any new joiner to synchronize without a handshake. There is no cookie or
challenge in multicast.

---

## Scouting and Discovery

### Scout

Sent via UDP multicast (default group: `224.0.0.224:7446`) to discover peers and routers.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|X|X|  SCOUT  |
+-+-+-+---------+
|    version    |
+---------------+
|zid_len|I| what|   (* what = WhatAmI bitmap)
+-+-+-+-+-+-+-+-+
~      [u8]     ~   if I==1 — ZenohID of scouter
+---------------+
```

The `what` field is a 3-bit bitmap:
- bit 0 = Router
- bit 1 = Peer
- bit 2 = Client

A Scout with `what = 0b011` is asking "tell me about any routers or peers."

### Hello

Sent unicast in reply to a Scout, or multicast proactively.

```
 7 6 5 4 3 2 1 0
+-+-+-+-+-+-+-+-+
|Z|X|L|  HELLO  |
+-+-+-+---------+
|    version    |
+---------------+
|zid_len|X|X|wai|
+-+-+-+-+-+-+-+-+
~     [u8]      ~   ZenohID
+---------------+
~   <utf8;z8>   ~   if L==1 — list of locator strings
+---------------+
```

Flag **L** (bit 5): If 1, explicit locator list follows. If 0, the source address of the UDP
packet is used as the locator.

Locators are URI strings like `tcp/192.168.1.1:7447` or `udp/192.168.1.1:7447`.

**Gossip discovery:** Peers share Hello information (locators of known peers) over established
sessions, allowing peer discovery without multicast. This is the `scouting.gossip` mechanism.

---

## Routing

### Interest-Based Routing

Zenoh does not maintain per-flow state. Instead, routing is driven by declarations:

1. A node declares a **subscriber** for key expression `sensors/**`.
2. The declaration is propagated as a `DeclareSubscriber` network message.
3. The publisher's side network receives the declaration and records that there is interest in
   `sensors/**` downstream.
4. When a `Push` message for `sensors/temperature` is published, the network routes it to all
   nodes that declared a matching subscriber.

The **Interest** message implements the declaration exchange protocol:
- On session establishment, each node sends `Interest(mode=CurrentFuture)` to request both current
  declarations and future ones from the peer.
- The peer responds with its current `Declare*` messages, then sends a `DeclareFinal`.
- After DeclareFinal, future declarations/undeclarations flow as they occur, without a
  DeclareFinal.
- When the interest is no longer needed, the node sends `Interest(mode=Final)` to stop the stream.

### Key Expression Mapping

To avoid repeating long key expression strings in every message, a node declares a mapping via
`DeclareKeyExpr`:

```rust
// DeclareKeyExpr assigns a 16-bit ID to a key expression string
DeclareKeyExpr { id: 42, wire_expr: WireExpr { scope: 0, suffix: "sensors/temperature" } }

// Subsequent Push messages use ID 42 instead of the full string
Push { wire_expr: WireExpr { scope: 42, suffix: "" }, ... }
// vs. full-string version:
Push { wire_expr: WireExpr { scope: 0, suffix: "sensors/temperature" }, ... }
```

With a declared key expression ID ≤ 127, the scope field costs only 1 byte (VLE). This is the
primary mechanism for reducing per-message overhead.

### Linkstate Routing

In **linkstate** mode (configured via `routing.peer.mode = "linkstate"` or router routing), routers
exchange topology information using OAM messages. Each router broadcasts its link state (which
other routers/peers it is connected to and the link weights). This allows computing shortest paths.

The `routing.router.linkstate.transport_weights` configuration assigns weights to individual
transport links, influencing path selection.

### Wildcard Fanout

When a publisher sends to `sensors/**` and multiple subscribers match (e.g., `sensors/temperature`,
`sensors/humidity`), the router fans out the message. Each matching subscriber receives a copy.
The publisher sends one message; the router is responsible for duplication.

In practice, for unicast topologies (no actual multicast at the network layer), each copy is sent
as a separate Frame to each matching peer. Wildcards increase router CPU load proportionally to
the number of matching subscribers.

### Router-to-Router Link State Exchange

Between routers, link state is exchanged via OAM (Operations and Management) messages. These
messages carry the full network topology information needed for Dijkstra path computation. The
format is implementation-internal and not part of the public API.

---

## Reliability

### Channels: Reliable vs. Best-Effort

Each transport session maintains **two independent channels**, each with its own sequence number:

- **Reliable channel** (Frame with R=1): Carries messages where delivery must be guaranteed
  hop-to-hop.
- **Best-effort channel** (Frame with R=0): Carries messages where dropping is acceptable.

The `Zenoh080Batch` codec tracks the current frame type (`CurrentFrame::Reliable` or
`CurrentFrame::BestEffort`) to ensure that all messages within a single batch share the same channel.
If a message on the other channel needs to be sent, a new frame header is emitted.

From `network/mod.rs`, the `is_reliable()` method determines channel:

```rust
fn is_reliable(&self) -> bool {
    self.reliability() == Reliability::Reliable
}
```

The `reliability` field on a `NetworkMessage` is set based on the subscriber's declaration (reliable
or best-effort) and propagated along the route.

### What "Reliable" Guarantees

Zenoh's reliability is **hop-to-hop**, not end-to-end:

- On each individual transport link (A→B), all messages on the reliable channel arrive in order and
  without loss.
- If a link drops (router crash, network partition), messages in flight are **lost**. There is no
  end-to-end retransmission.
- Reliability does NOT mean exactly-once. It means ordered, lossless delivery on each hop in a stable
  topology.

### Congestion Control

The `CongestionControl` setting on a publisher determines behavior when the send queue is full:

- **Drop** (default): If no batch is available within `wait_before_drop` microseconds (default: 1000µs),
  the message is dropped silently.
- **Block**: Block the publisher until a batch is available, up to `wait_before_close` microseconds
  (default: 5,000,000µs = 5 seconds). After that, the transport session is closed.

This prevents a slow subscriber from blocking the entire network. If a subscriber is declared with
`Reliability::Reliable` but the publisher uses `CongestionControl::Drop`, messages can still be
dropped under congestion.

The RFC `Network/Reliability.md` explains the design rationale: "Publishers publish their data with
an associated Congestion Control strategy. If Drop has been selected, and push comes to shove, the
subscriber's expectation that a message is never dropped becomes false, as under extreme pressure,
some messages may be dropped."

### Non-Blocking Fault-Tolerant Reliability (NBFTReliability)

For end-to-end reliability across topology changes (router crashes, redeployments), Zenoh provides
the `NBFTReliability` mechanism in `zenoh-ext`:

1. `NBFTReliablePublisher` attaches `SourceInfo` metadata to each sample:
   - `source_id`: ZenohID of the publisher session.
   - `source_sn`: monotonically increasing sequence number.

2. `NBFTReliabilityCache` stores published samples (acts like a queryable storage) and exposes
   them via queries with selector `<source_id>/key/expression?_sn=<start>..<end>`.

3. `NBFTReliableSubscriber` tracks expected sequence numbers. On gap detection, it queries the
   nearest `NBFTReliabilityCache` for the missing samples.

This provides **at-least-once** delivery semantics even across router crashes, without requiring
a direct publisher→subscriber ACK/NACK channel.

### Queue Configuration

Per-priority queues at the sender side are configured via `transport.link.tx.queue.size`:

```json5
queue: {
  size: {
    control:          2,   // highest priority
    real_time:        2,
    interactive_high: 2,
    interactive_low:  2,
    data_high:        2,
    data:             2,   // default priority
    data_low:         2,
    background:       2,   // lowest priority
  }
}
```

Each queue entry holds one batch. With the default `batch_size` of 65535 bytes and 2 entries per
priority, each priority queue buffers up to 2 × 65535 = 131070 bytes. If QoS is disabled, only
the DATA priority queue is allocated.

---

## Batching

### How Batching Works

Batching is the mechanism of coalescing multiple small network messages into a single batch before
sending. It is implemented in `zenoh-codec/src/transport/batch.rs`.

The `Zenoh080Batch` codec maintains a write buffer. When writing a `NetworkMessage`:

1. Check if the message can be appended to the current frame (same channel as existing messages).
2. If a new frame is needed (different channel, or first message), emit a `FrameHeader` first.
3. Serialize the `NetworkMessage` into the buffer.
4. If the message does not fit, return `BatchError::DidntWrite` — the caller is responsible for
   flushing the current batch and starting a new one.

The batch is flushed either when it is full, when the time limit expires, or when an express
message forces an immediate send.

### Adaptive Batching

**Config key:** `transport.link.tx.queue.batching.enabled`
**Default:** `true`

**Config key:** `transport.link.tx.queue.batching.time_limit`
**Type:** integer (milliseconds)
**Default:** `1`

When enabled, batching is *adaptive*: it only activates under network back-pressure. If the
network is fast enough to send each message individually, batching does not introduce additional
latency. When back-pressure is detected (the send queue is non-empty), messages are held up to
`time_limit` milliseconds before being sent together.

**Latency vs. throughput trade-off:**
- `time_limit = 0`: Maximum latency reduction, minimum throughput optimization.
- `time_limit = 1` (default): Up to 1 ms additional latency under back-pressure for better
  throughput when the network is saturated.
- `time_limit = 10`: Aggressive batching, suitable for sustained high-throughput scenarios.

### Express Flag

The **Express** (E) flag in the QoS extension of a network message bypasses batching entirely.
When a message has E=1, it is serialized into its own batch and sent immediately, regardless of
the `time_limit` and `batching.enabled` settings.

```rust
// From network/mod.rs
fn is_express(&self) -> bool {
    match self.body() {
        NetworkBodyRef::Push(msg) => msg.ext_qos.is_express(),
        // ... all message types check their QoS extension
    }
}
```

Setting `express = true` on a publisher or using `CongestionControl::Block` will typically result
in the message being sent immediately. Use this when latency is more important than throughput.

---

## Compression

### Configuration

**Config keys:**
- `transport.unicast.compression.enabled` (type: bool, default: `false`)
- `transport.multicast.compression.enabled` (type: bool, default: `false`)

Compression is negotiated during the INIT handshake via the `Compression` extension (ID=0x6).
Both nodes must support compression for it to be activated. If only one side advertises the
extension, compression is not used.

### Algorithm: LZ4

Zenoh uses LZ4 compression on the entire batch payload. LZ4 is chosen for:
- Very low compression latency (~400 MB/s on modern hardware).
- Reasonable compression ratios for typical sensor/IoT data.
- Minimal CPU overhead compared to gzip/zstd.

### Interaction with Low-Latency Mode

The LowLatency transport mode (`transport.unicast.lowlatency = true`) is incompatible with
compression. The LowLatency transport bypasses QoS prioritization and batching, so applying
compression would negate its latency benefits.

Note: LowLatency mode also does not support fragmentation. All messages must fit within the
configured `batch_size`.

### When Compression Helps vs. Hurts

**Compression helps when:**
- Payloads are large (> 100 bytes) and repetitive (e.g., JSON sensor readings, structured data).
- Network bandwidth is the bottleneck (narrow-band wireless, WAN links).
- CPU is not the bottleneck.

**Compression hurts when:**
- Payloads are small (< 50 bytes): LZ4 framing overhead exceeds compression savings.
- Payloads are already compressed (JPEG images, compressed audio).
- CPU is constrained (microcontrollers, embedded devices).
- Latency is critical: even LZ4 adds ~1–5 µs per batch on modern hardware.

---

## Protocol Overhead Analysis

### Minimum Push Message Overhead

For a data publication to a pre-declared key expression with default QoS and no timestamp:

**Transport layer (Frame):**
```
Header byte:   1 byte  (0x05 | R_flag if reliable)
Sequence num:  1 byte  (VLE, SN 0–127 = 1 byte)
               ────────
               2 bytes total for Frame header
```

On TCP (stream), add 2 bytes length prefix per batch = 2 bytes amortized over all messages in batch.

**Network layer (Push):**
```
Header byte:   1 byte  (0x1d = PUSH, no flags if using declared KE with no suffix)
key_scope:     1 byte  (VLE, ExprId 1–127 = 1 byte, if pre-declared)
               ────────
               2 bytes (minimum, with declared key expression)
```

If the key expression is NOT pre-declared (using full string inline):
```
Header byte:   1 byte  (0x1d | N flag)
key_scope:     1 byte  (0x00 = global scope)
key_suffix:    2+ bytes (VLE length + string bytes, e.g., "a" = 2 bytes minimum)
```

**Zenoh payload layer (Put):**
```
Header byte:   1 byte  (PUT id)
payload_len:   1 byte  (VLE, payload ≤ 127 bytes = 1 byte)
               ────────
               2 bytes (minimum, default encoding, no timestamp)
```

**Total minimum overhead per data message (declared KE, no timestamp, no QoS ext):**
```
Frame header:   2 bytes
Push header:    2 bytes (with declared KE)
Put header:     2 bytes
               ────────
Total:          6 bytes overhead for the application payload
```

For the first message in a batch on TCP, add 2 bytes length prefix = **8 bytes total** for the
first message (or amortized with subsequent messages).

### Overhead with Optional Fields

| Field                       | Size                                   | Condition             |
|-----------------------------|----------------------------------------|-----------------------|
| QoS extension               | 3 bytes (1 ext header + 1 value + 1 chain) | Non-default QoS  |
| Timestamp extension wrapper | 2 bytes (1 ext header + 1 more flag)   | If timestamp enabled  |
| Timestamp NTP64             | 9 bytes (VLE u64)                      | If timestamp enabled  |
| Timestamp ZenohID           | 2–17 bytes (1 len + 1–16 bytes)        | If timestamp enabled  |
| NodeId extension            | 3 bytes (1 ext header + 2 node_id)     | When forwarded        |
| Full key expression suffix  | 2+ bytes per char                      | No declared KE        |

**With timestamp (16-byte ZenohID, typical NTP64):**
```
Timestamp extension header: 2 bytes
NTP64 time:                 8 bytes (u64 as VLE, large values = 9 bytes)
ZenohID size:               1 byte  (value = 16)
ZenohID bytes:              16 bytes
                            ─────────
Timestamp total:            27 bytes
```

Minimum Push overhead with timestamp: 6 + 27 = **33 bytes**.

### Comparison: Zenoh vs. Other Protocols

| Protocol     | Min data overhead | Notes                                      |
|--------------|-------------------|--------------------------------------------|
| Raw UDP      | 8 bytes           | UDP header only, no topic, no routing      |
| Zenoh        | 6–8 bytes         | Per message; per-batch 2B length on TCP    |
| MQTT 3.1.1   | 4–6 bytes         | PUBLISH header (2B fixed + topic length)   |
| MQTT 5.0     | 4–6+ bytes        | Plus optional user properties              |
| DDS RTPS     | ~24+ bytes        | Submessage header + InfoTimestamp + Data   |
| ROS2 (DDS)   | ~40–80 bytes      | DDS + RTPS headers + message metadata     |

Zenoh's overhead is competitive with MQTT and significantly lower than DDS/RTPS for small messages
with pre-declared key expressions.

### Declaring Key Expressions to Minimize Overhead

The most impactful optimization is declaring key expressions:

```rust
// Without declaration: "sensors/temperature/building_A/floor_3" = 40 bytes per message
session.put("sensors/temperature/building_A/floor_3", payload).await?;

// With declaration: 1 byte per message (ExprId 1–127)
let expr = session.declare_keyexpr("sensors/temperature/building_A/floor_3").await?;
session.put(&expr, payload).await?;
```

This reduces the per-message key expression cost from 40+ bytes to 1 byte — a 40× reduction in
key expression overhead alone.

---

## Configuration Reference

### transport.link.tx section

**`transport.link.tx.sequence_number_resolution`**
- Type: string
- Values: `"8bit"`, `"16bit"`, `"32bit"`, `"64bit"`
- Default: `"32bit"`
- Effect: Determines the wire size of sequence numbers. Lower values save bytes per frame; higher
  values extend time between rollover. At 32bit, rollover is ~71 minutes at 1M frames/sec.

**`transport.link.tx.lease`**
- Type: integer (milliseconds)
- Default: `10000`
- Effect: Link keepalive lease period. Peer closes session if no data is received within this period.

**`transport.link.tx.keep_alive`**
- Type: integer (count)
- Default: `4`
- Effect: Number of keepalive messages to send per lease period. Interval = `lease / keep_alive`.
  Default: 10000 / 4 = 2500ms.

**`transport.link.tx.batch_size`**
- Type: u16 (0–65535)
- Default: `65535` (unicast), `8192` (multicast)
- Effect: Maximum bytes per batch. Negotiated down to the minimum of both peers. Controls maximum
  unfragmented message size. Larger values reduce per-batch overhead; smaller values reduce latency
  for time-sensitive traffic on congested links.

**`transport.link.tx.queue.size.*`**
- Type: integer (1–16)
- Default: `2` for each of 8 priorities
- Effect: Number of batches buffered per priority queue. Total buffer = size × batch_size per
  priority. Increase for high-throughput, decrease for memory-constrained devices.

**`transport.link.tx.queue.batching.enabled`**
- Type: boolean
- Default: `true`
- Effect: Enable adaptive batching. When false, each message is sent in its own batch (increases
  packet count, reduces latency).

**`transport.link.tx.queue.batching.time_limit`**
- Type: integer (milliseconds)
- Default: `1`
- Effect: Maximum time a message waits for batching under back-pressure. `0` disables time-based
  flushing (batch only when full).

**`transport.link.tx.queue.congestion_control.drop.wait_before_drop`**
- Type: integer (microseconds)
- Default: `1000`
- Effect: How long to wait for a free batch before dropping a `CongestionControl::Drop` message.

**`transport.link.tx.queue.congestion_control.block.wait_before_close`**
- Type: integer (microseconds)
- Default: `5000000` (5 seconds)
- Effect: How long to wait for a free batch before closing the session for `CongestionControl::Block`
  messages.

**`transport.link.rx.buffer_size`**
- Type: integer (bytes)
- Default: `65535`
- Effect: Receive buffer size per link. Increase for very high-throughput scenarios.

**`transport.link.rx.max_message_size`**
- Type: integer (bytes)
- Default: `1073741824` (1 GiB)
- Effect: Maximum size of a reassembled fragmented message. Fragmented messages larger than this
  are dropped.

### transport.unicast section

**`transport.unicast.lowlatency`**
- Type: boolean
- Default: `false`
- Effect: Enable low-latency transport. Skips QoS prioritization, frame batching, and
  fragmentation. Messages are sent directly without frame wrappers. Incompatible with QoS.
  All messages must fit within `batch_size`.

**`transport.unicast.qos.enabled`**
- Type: boolean
- Default: `true`
- Effect: Enable QoS priority channels. When enabled, 8 priority queues are maintained. When
  disabled, only the DATA priority queue exists and the QoS extension is not sent.

**`transport.unicast.compression.enabled`**
- Type: boolean
- Default: `false`
- Effect: Negotiate LZ4 compression with peers. Both sides must enable for compression to activate.

### Example: Low-Overhead High-Throughput Configuration

```json5
transport: {
  unicast: {
    qos: { enabled: true },
    compression: { enabled: true },
  },
  link: {
    tx: {
      sequence_number_resolution: "32bit",
      batch_size: 65535,
      queue: {
        size: {
          data: 16,        // Increase queue depth for sustained throughput
          data_low: 8,
          background: 4,
        },
        batching: {
          enabled: true,
          time_limit: 5,   // Batch up to 5ms under back-pressure
        },
      },
    },
    rx: {
      buffer_size: 16777216,  // 16MiB for large in-flight messages
    },
  },
},
```

### Example: Low-Latency Real-Time Configuration

```json5
transport: {
  unicast: {
    lowlatency: false,        // Keep fragmentation support
    qos: { enabled: true },
    compression: { enabled: false },
  },
  link: {
    tx: {
      sequence_number_resolution: "8bit",  // 1-byte SNs (wraps at 256 frames)
      batch_size: 65535,
      queue: {
        size: {
          real_time: 2,      // Small queue to minimize latency
          data: 2,
        },
        batching: {
          enabled: true,
          time_limit: 0,     // No time-based batching, only back-pressure driven
        },
      },
    },
  },
},
```

### Rust API: Observing QoS and Reliability

```rust
use zenoh::prelude::r#async::*;

// Publisher with explicit QoS
let publisher = session
    .declare_publisher("sensors/temperature")
    .congestion_control(CongestionControl::Block)  // Never drop
    .priority(Priority::RealTime)                  // Highest priority queue
    .express(true)                                 // Bypass batching
    .res()
    .await?;

// Subscriber requesting reliable delivery (hop-to-hop)
let subscriber = session
    .declare_subscriber("sensors/**")
    .reliability(Reliability::Reliable)
    .res()
    .await?;

// Pre-declare a key expression to minimize per-message overhead
let ke = session
    .declare_keyexpr("sensors/temperature/building_A/floor_3")
    .res()
    .await?;
session.put(&ke, payload).res().await?;
// Wire cost: 1 byte ExprId instead of 40+ byte string
```

---

## Summary: Key Numbers

| Parameter               | Default Value   | Notes                                     |
|-------------------------|-----------------|-------------------------------------------|
| Batch size (unicast)    | 65535 bytes     | Max unfragmented message size             |
| Batch size (multicast)  | 8192 bytes      | Platform varies; 9216 on macOS            |
| SN resolution           | 32 bits         | Negotiated down to min of both peers      |
| Frame overhead          | 2 bytes min     | 1 header + 1 VLE SN (for SN ≤ 127)       |
| Push overhead (decl KE) | 4 bytes         | 1 header + 1 scope + 1 put header + 1 len|
| Total min data overhead | 6 bytes         | Frame + Push + Put (declared KE, no ts)  |
| Keepalive interval      | 2500 ms         | lease (10s) / keep_alive (4)              |
| Session lease           | 10000 ms        | After which no-response = dead link       |
| Fragment max size       | 1 GiB           | `rx.max_message_size`                     |
| Max batch queue depth   | 2 batches/prio  | 131070 bytes per priority default         |
| Batching time limit     | 1 ms            | Under back-pressure only                 |

## See Also

- [Architecture Guide](architecture-guide.md) — high-level protocol layers that this wire protocol guide implements in detail
- [QoS Guide](qos-guide.md) — how the 8-priority channel system maps to transport frame priority bits
- [Config Transport Link TX](config-transport-link-tx.md) — batch size, queue depth, and congestion control settings for the TX path
- [Performance Tuning Guide](performance-tuning-guide.md) — how wire overhead and batching translate to real-world throughput
