# Source: https://electric-sql.com/products/durable-streams.md

---
url: /products/durable-streams.md
description: >-
  Persistent, addressable, real-time streams that power resilient, collaborative
  AI applications.
---

# Durable Streams

Persistent, addressable, real-time streams that power resilient,

collaborative

AI applications.

## What are Durable Streams?

Durable Streams are persistent, addressable, real-time streams. They're a flexible,

swiss-army-knife
data primitive that's ideal for:

* token streaming
* collaborative AI sessions
* real-time presence

They're resumeable and resilient to patchy connectivity. They're high-throughput, low-latency and highly scalable. They unlock building [multi-user, multi-agent systems](/blog/2026/01/12/durable-sessions-for-collaborative-ai).

They're extensible, with [wrapper protocols](#wrapper-protocols) for everything from type-safe JSON streams running off a Standard Schema, to multi-modal data and structured database sync.

## Why do we need them?

Modern applications frequently need ordered, durable sequences of data that can be replayed from arbitrary points and tailed in real time.

Durable Streams addresses this gap for apps and agents across all platforms: web browsers, mobile apps, native clients, IoT devices, and edge workers.

### Use cases

* **token streaming** - stream LLM token responses
* **agentic apps** - stream tool outputs and events
* **database sync** - stream database changes
* **collaborative editing** - sync CRDTs and OTs across devices
* **real-time updates** - push state to clients and workers
* **workflow execution** - build durable workflows on durable state

### Benefits

* **multi-tab** - works seamlessly and efficiently across browser tabs
* **multi-device** - start on your laptop, continue on your phone
* **never re-run** - don't repeat expensive work because of a disconnect
* **share links** - consume and interact with the same stream
* **refresh-safe** - refresh the page, switch tabs or background the app
* **massive fan-out** - scale to millions of concurrent viewers

## How do they work?

The core primitive is a byte stream that can be written to and consumed via an [open protocol](https://github.com/durable-streams/durable-streams/blob/main/PROTOCOL.md) using a wide range of [client libraries](https://github.com/durable-streams/durable-streams/tree/main/packages).

### Resilient, scalable data delivery

The protocol is a generalization of the Electric [HTTP API](/docs/api/http).

It ensures resilience and reliable, exactly-once message delivery. Which can be scaled out through existing CDN infrastructure.

### High throughput, low-latency

The core streams are extremely simple: append-only binary logs.

As a result, they support very high throughput (millions of writes per second) and can be cached and served with single-digit ms latency at the cloud edge.

### Real-time and asynchronous collaboration

Streams are persistent and addressible, with their own storage and URL.

Clients can consume the stream from any position in the log, providing message history and resumability. They can connect and subscribe to them at any time, for both asynchronous and real-time collaboration.

## Wrapper protocols

Durable Streams support multiple wrapper protocols for different use cases:

* **Binary streams** — efficient binary encoding for high-throughput data
* **JSON mode** — human-readable JSON for debugging and interoperability
* **Proxy** — transparent proxy mode for existing SSE endpoints
* **Durable state** — persisted session state with automatic recovery
* **TanStack AI** — integration with TanStack Query for AI responses
* **Vercel AI SDK** — drop-in transport adapter for Vercel AI SDK
* **Yjs** — CRDT-based collaborative editing with Yjs

## Related posts

## More information

See the [project on GitHub](https://github.com/durable-streams/durable-streams) for more info.
