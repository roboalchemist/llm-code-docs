# Zenoh Documentation

Zenoh (pronounced /zeno/) is a pub/sub/query protocol by Eclipse/ZettaScale for
edge computing, IoT, and robotics. It unifies data in motion, data at rest,
and computations.

## Contents

### Core Documentation
- [concepts.md](concepts.md) — Key concepts and abstractions
- [getting-started.md](getting-started.md) — Installation and first app
- [configuration.md](configuration.md) — Configuration reference (DEFAULT_CONFIG.json5)
- [changelog.md](changelog.md) — Consolidated changelog and release notes

### API References
- [api/rust.md](api/rust.md) — Rust API (primary implementation)
- [api/python.md](api/python.md) — Python bindings
- [api/c.md](api/c.md) — C bindings (zenoh-c + zenoh-pico)
- [api/cpp.md](api/cpp.md) — C++ bindings
- [api/typescript.md](api/typescript.md) — TypeScript bindings
- [api/java.md](api/java.md) — Java bindings
- [api/kotlin.md](api/kotlin.md) — Kotlin bindings

### Plugins
- [plugins/ros2dds.md](plugins/ros2dds.md) — ROS 2 / DDS bridge
- [plugins/mqtt.md](plugins/mqtt.md) — MQTT bridge
- [plugins/dds.md](plugins/dds.md) — DDS bridge
- [plugins/webserver.md](plugins/webserver.md) — REST/HTTP plugin

### Storage Backends
- [backends/influxdb.md](backends/influxdb.md) — InfluxDB backend
- [backends/s3.md](backends/s3.md) — S3 backend
- [backends/rocksdb.md](backends/rocksdb.md) — RocksDB backend
- [backends/filesystem.md](backends/filesystem.md) — Filesystem backend

### Design & Research
- [rfcs/](rfcs/) — RFCs and design documents
- [research.md](research.md) — Academic papers and research
- [examples/](examples/) — Code examples by language
- [migration/](migration/) — Migration guides

## Sources

This documentation was assembled from:
1. zenoh.io official website (docs + blog)
2. GitHub repos (eclipse-zenoh org — 28 repos)
3. docs.rs Rust API documentation
4. Release notes and changelogs (558 releases)
5. RFCs and design documents (24 docs)
6. Academic papers and research
