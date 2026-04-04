# Zenoh Documentation

Zenoh is a zero-overhead publish/subscribe, put/get, and query protocol designed for the IoT, robotics, and edge-to-cloud continuum. It unifies data in motion, data at rest, and computations under a single, location-transparent API.

---

## Quick Navigation

| I want to… | Go to |
|------------|-------|
| Get up and running fast | [Quickstart Recipes](quickstart-recipes.md) |
| Understand how sessions work | [Programming Model](programming-model-guide.md) |
| Configure connect/listen endpoints | [Connect & Listen](config-connect-listen.md) |
| Set up scouting / discovery | [Scouting & Discovery](scouting-guide.md) |
| Add TLS or user/password auth | [Encryption & Authentication](encryption-guide.md) |
| Bridge to ROS2 / DDS | [DDS Bridge Plugin](plugin-dds-bridge-guide.md) |
| Use zenoh on microcontrollers | [zenoh-pico Guide](zenoh-pico-guide.md) |
| Tune for low latency / high throughput | [Performance Tuning](performance-tuning-guide.md) |
| Compare zenoh to MQTT / DDS / Kafka | [Comparison Guide](comparison-guide.md) |
| Debug a connection problem | [Troubleshooting](troubleshooting-guide.md) |

---

## What's in This Site

### Getting Started
Quickstart recipes, the programming model, node types, and common questions.

### Configuration
Complete reference for every config field: connect/listen, scouting, routing, transport layers, QoS, encryption, ACL, and admin space.

### API & Features
Key expressions, queryables, liveliness, matching, serialization, shared memory, and zenoh-ext extensions.

### Plugins
Storage manager, REST bridge, DDS, MQTT, InfluxDB, RocksDB, S3, and filesystem backends.

### Platforms
zenoh-pico (MCU), Zephyr RTOS, QUIC transport, and Docker deployment.

### Use Cases
Automotive/SDV, multi-robot, ROS2 migration, DDS interop, and case studies.

### Reference
Architecture internals, wire protocol, zenoh-flow, performance benchmarks, and comparison with other protocols.

### Resources
Video summaries and talk recordings from the ZettaScale channel.

---

## Key Concepts

**Key Expression** — A URI-like path that identifies a resource. Supports wildcards (`*`, `**`) for fan-out subscriptions and queries.

**Session** — A connection to the Zenoh network. Opens with `zenoh::open(config)`.

**Mode** — Every session is a `router`, `peer`, or `client`. Determines routing behavior and default scouting role.

**Publisher / Subscriber** — Put data on a key expression; receive data matching a key expression.

**Queryable / Get** — Request data from a key expression; reply with a value.

**Storage** — A plugin-managed persistent store that answers queries for key expressions.
