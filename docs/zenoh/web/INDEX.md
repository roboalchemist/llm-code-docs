# Zenoh Documentation Index

Zenoh (pronounced /zeno/) is a pub/sub/query protocol by Eclipse/ZettaScale for edge computing, IoT, and robotics. It unifies data in motion, data at rest, and computations.

This index covers all 68+ output files produced by the zenoh-docs pipeline.

---

## Synthesized Guides (Phase 3–4)

LLM-synthesized reference documents drawing on all scraped sources.

### Core Concepts & Getting Started
- [concepts.md](concepts.md) — Key abstractions: sessions, key expressions, publishers, subscribers, queryables, encoding, QoS, and more
- [getting-started.md](getting-started.md) — Installation and first application across all language bindings
- [faq.md](faq.md) — Frequently asked questions: performance, protocol comparison, troubleshooting

### Configuration
- [configuration.md](configuration.md) — Complete configuration reference (DEFAULT_CONFIG.json5 annotated)
- [configuration-guide.md](configuration-guide.md) — Practical configuration walkthroughs for common deployment scenarios

### Networking & Deployment
- [transports.md](transports.md) — Transport protocols: TCP, UDP, TLS, QUIC, VSOCK, shared memory, serial
- [deployment.md](deployment.md) — Routers, peers, clients, multi-host topologies, Docker, Kubernetes
- [shared-memory.md](shared-memory.md) — Zero-copy shared-memory transport for intra-host high-throughput messaging
- [liveliness.md](liveliness.md) — Liveliness tokens: presence detection and subscriber monitoring

### Security
- [security.md](security.md) — TLS/mTLS configuration, ACLs, authentication, certificate management

### Serialization & Data
- [serialization.md](serialization.md) — Payload encoding, SHM buffers, zenoh-ext serialization helpers

### Integrations
- [ros2.md](ros2.md) — ROS 2 bridge: zenoh-plugin-ros2dds, topic mapping, QoS translation
- [embedded.md](embedded.md) — zenoh-pico on embedded/MCU targets: Zephyr, Arduino, FreeRTOS

### Knowledge Extracts (Phase 4)
- [breaking-changes.json](breaking-changes.json) — Structured timeline of breaking API/behavior changes by version (9 entries)
- [benchmarks.json](benchmarks.json) — Extracted performance benchmarks with metrics, scenarios, and comparisons (10 entries)
- [api-surface.json](api-surface.json) — Public API symbols extracted from zenoh Rust source (272 entries: fn, struct, enum, trait, type)

---

## API References

### Language Bindings
- [api/rust.md](api/rust.md) — Rust API (primary implementation, docs.rs reference)
- [api/python.md](api/python.md) — Python bindings (zenoh-python)
- [api/c.md](api/c.md) — C bindings (zenoh-c + zenoh-pico)
- [api/cpp.md](api/cpp.md) — C++ bindings (zenoh-cpp)
- [api/typescript.md](api/typescript.md) — TypeScript/JavaScript bindings
- [api/java.md](api/java.md) — Java bindings
- [api/kotlin.md](api/kotlin.md) — Kotlin bindings

### Cross-Language Matrix
- [api-matrix.md](api-matrix.md) — Feature availability matrix across all language bindings

---

## Plugins

### Protocol Bridges
- [plugins/ros2dds.md](plugins/ros2dds.md) — ROS 2 / DDS bridge (zenoh-plugin-ros2dds)
- [plugins/dds.md](plugins/dds.md) — Generic DDS bridge
- [plugins/mqtt.md](plugins/mqtt.md) — MQTT bridge
- [plugins/webserver.md](plugins/webserver.md) — REST/HTTP plugin (zenoh-plugin-webserver)

### Plugin Development
- [plugins/development.md](plugins/development.md) — Building custom zenoh plugins: API, lifecycle, configuration injection

---

## Storage Backends

- [backends/influxdb.md](backends/influxdb.md) — InfluxDB storage backend
- [backends/s3.md](backends/s3.md) — S3-compatible storage backend
- [backends/rocksdb.md](backends/rocksdb.md) — RocksDB embedded storage backend
- [backends/filesystem.md](backends/filesystem.md) — Filesystem storage backend

---

## Changelogs & Release Notes

- [changelog.md](changelog.md) — Consolidated changelog across all zenoh repositories

---

## Blog & Research

- [blog.md](blog.md) — ZettaScale and Eclipse zenoh blog posts
- [research.md](research.md) — Academic papers, arXiv preprints, and third-party evaluations

---

## Code Examples

Language-specific example collections extracted from official repositories:

- [examples/zenoh.md](examples/zenoh.md) — Rust examples (zenoh core)
- [examples/zenoh-python.md](examples/zenoh-python.md) — Python examples
- [examples/zenoh-c.md](examples/zenoh-c.md) — C examples
- [examples/zenoh-cpp.md](examples/zenoh-cpp.md) — C++ examples
- [examples/zenoh-java.md](examples/zenoh-java.md) — Java examples
- [examples/zenoh-kotlin.md](examples/zenoh-kotlin.md) — Kotlin examples

---

## RFCs & Design Documents

Formal design proposals from the eclipse-zenoh/roadmap repository:

- [rfcs/readme.md](rfcs/readme.md) — RFC index and process overview
- [rfcs/rfcs-1-discussing.md](rfcs/rfcs-1-discussing.md) — RFCs under active discussion
- [rfcs/rfcs-3-implemented.md](rfcs/rfcs-3-implemented.md) — Implemented RFCs
- [rfcs/rfcs-4-master.md](rfcs/rfcs-4-master.md) — Merged / master-tracked RFCs
- [rfcs/rfcs-all-access-control-rules.md](rfcs/rfcs-all-access-control-rules.md) — ACL rules RFC
- [rfcs/rfcs-all-connectivity-status-and-events.md](rfcs/rfcs-all-connectivity-status-and-events.md) — Connectivity status events RFC
- [rfcs/rfcs-all-key-expressions.md](rfcs/rfcs-all-key-expressions.md) — Key expression format RFC
- [rfcs/rfcs-all-key-formatters.md](rfcs/rfcs-all-key-formatters.md) — Key formatter RFC
- [rfcs/rfcs-all-liveliness.md](rfcs/rfcs-all-liveliness.md) — Liveliness RFC
- [rfcs/rfcs-all-matching-status.md](rfcs/rfcs-all-matching-status.md) — Matching status RFC
- [rfcs/rfcs-all-network-consolidation.md](rfcs/rfcs-all-network-consolidation.md) — Network consolidation RFC
- [rfcs/rfcs-all-network-reliability.md](rfcs/rfcs-all-network-reliability.md) — Network reliability RFC
- [rfcs/rfcs-all-non-blocking-fault-tolerant-reliability.md](rfcs/rfcs-all-non-blocking-fault-tolerant-reliability.md) — Non-blocking fault-tolerant reliability RFC
- [rfcs/rfcs-all-ownership-in-c.md](rfcs/rfcs-all-ownership-in-c.md) — Ownership model in C bindings RFC
- [rfcs/rfcs-all-plugins-zenoh-plugins.md](rfcs/rfcs-all-plugins-zenoh-plugins.md) — Plugin architecture RFC
- [rfcs/rfcs-all-query-payload.md](rfcs/rfcs-all-query-payload.md) — Query payload RFC
- [rfcs/rfcs-all-readme.md](rfcs/rfcs-all-readme.md) — RFC repository README
- [rfcs/rfcs-all-selectors-_filter.md](rfcs/rfcs-all-selectors-_filter.md) — Selector `_filter` parameter RFC
- [rfcs/rfcs-all-selectors-_project.md](rfcs/rfcs-all-selectors-_project.md) — Selector `_project` parameter RFC
- [rfcs/rfcs-all-selectors-_time.md](rfcs/rfcs-all-selectors-_time.md) — Selector `_time` parameter RFC
- [rfcs/rfcs-all-selectors-readme.md](rfcs/rfcs-all-selectors-readme.md) — Selector RFC overview
- [rfcs/rfcs-all-serialization.md](rfcs/rfcs-all-serialization.md) — Serialization RFC
- [rfcs/rfcs-all-shm.md](rfcs/rfcs-all-shm.md) — Shared memory RFC

---

## Migration Guides

- [migration/index.md](migration/index.md) — Migration notes for breaking version upgrades

---

## Sources

This documentation was assembled from:

1. zenoh.io official website (docs + blog)
2. GitHub repos (eclipse-zenoh org — 28 repos)
3. docs.rs Rust API documentation
4. Release notes and changelogs (558 releases)
5. RFCs and design documents (24 docs)
6. Academic papers and research
7. Phase 4 knowledge extraction: breaking changes, benchmarks, API surface
