# Zenoh Upstream Contribution Candidates

Highest-priority items for contributing back to zenoh.io or the eclipse-zenoh repos.

Identified by comparing our scraped/synthesized corpus against the 11-page zenoh.io/docs scrape (stream 01-website-docs) and community sources (GitHub issues, ROS Discourse, Stack Overflow).

---

## Priority 1: Missing Documentation

These topics are completely absent from zenoh.io/docs but are well-covered in our corpus from issues, blog posts, or source code.

### 1.1 Breaking Changes Migration Guide — 1.0.0 to 1.7.x

The official docs have a migration guide for 0.x → 1.0.0 but stop there. Our extracted/breaking-changes.json documents 31 breaking changes across versions 1.0.0 and 1.7.0 covering Rust, Python, C, and C++. Approximately 17 of these changes are not documented anywhere on zenoh.io.

High-value items missing from official docs:
- Callback opaque type: use `Callback::new()` not direct construction
- `flume::Receiver` replaced by `zenoh::handlers::FifoChannelHandler`
- `ZDeserializeError` replaces `DidntRead` / `ZReadOrDeserializeError`
- `Selector` field access replaced by method calls (`.key_expr()`, `.parameters()`)
- zenoh-c: `z_bytes_to_slice()` API for sample payload access
- zenoh-c/cpp: `replier_id` type changed to `z_entity_global_id_t` / `EntityGlobalId`
- zenoh-cpp: header renamed from `zenoh.h` to `zenoh.hxx`
- zenoh-cpp: `zc_locality` → `z_locality` (1.7.0)

**Contribution target**: `https://zenoh.io/docs/migration_1.0/` or a new `migration_1.7/` page.

### 1.2 Access Control / ACL Policy Configuration

Zenoh has a policy-based ACL system controlling which subjects can publish/subscribe to which key expressions. This system is configured via the `access_control` section of the config file but is completely absent from zenoh.io documentation. Our security.md covers TLS/mTLS in depth but the ACL system is only visible in DEFAULT_CONFIG.json5 comments.

**Contribution target**: New page at `zenoh.io/docs/manual/access-control/`.

### 1.3 Shared Memory (SHM) Configuration Guide

Zenoh supports zero-copy shared memory transport for co-located processes. Benchmarks reference SHM as excluded from NTU comparisons to keep things at the protocol level, implying it performs even better. There is no how-to guide on enabling or configuring SHM. The SHM feature requires specific Cargo features and config parameters that are not documented on the website.

**Contribution target**: New page at `zenoh.io/docs/manual/shared-memory/`.

### 1.4 Storage Backend Comparison and Selection Guide

Four storage backends exist (filesystem, influxdb, rocksdb, S3), all at 1.7.2. There is no documentation comparing them by:
- Use case (time-series vs. file-based vs. embedded vs. cloud)
- Performance characteristics
- Configuration complexity
- Persistence guarantees

Users must read four separate READMEs to understand the tradeoffs.

**Contribution target**: New page at `zenoh.io/docs/manual/backends/` or a table in the storage section.

### 1.5 Plugin Development Guide

The zenoh plugin system allows custom plugins to be loaded into `zenohd` via dynamic linking. The `__plugin__` configuration field and multi-instance plugin pattern are documented only in a code comment (DEFAULT_CONFIG.json5). No walkthrough exists for how to write a plugin, what traits to implement, or how to structure the Cargo.toml.

**Contribution target**: New page at `zenoh.io/docs/manual/plugins/development/`.

---

## Priority 2: Incomplete Guides

These topics are partially documented on zenoh.io but could be meaningfully expanded with material from our corpus.

### 2.1 TLS Guide — Post-1.0 Parameter Names

The zenoh.io TLS documentation (if it exists) likely still references the pre-1.0 parameter names (`server_certificate`, `client_auth`, `server_name_verification`). The 1.0 release renamed these to `listen_certificate`, `enable_mtls`, and `verify_name_on_connect`. Our security.md and configuration.md already use the correct names (sourced from actual source code). The official guide needs to be updated or a callout added.

Additionally, our corpus documents three certificate input methods per parameter (file path, raw PEM, base64-encoded) and the `tls_handshake_timeout_ms` parameter — none of which appear prominently in the website docs.

**Contribution target**: Update `zenoh.io/docs/manual/tls/`.

### 2.2 Scouting and Peer Discovery Deep Dive

The FAQ and getting-started output contain detailed content on multicast scouting, gossip scouting, scout messages, and the `autoconnect_strategy` field. The zenoh.io docs cover only the surface of scouting. Notable gaps:
- The `autoconnect_strategy` config field (with `to_router` / `to_peer` sub-fields)
- Gossip scouting configuration (`multihop` field, `autoconnect` per mode)
- How to diagnose when scouting fails (admin space queries, `zenohd -v`)
- Why peers on the same machine may not discover each other (loopback interface, Docker networking)

**Contribution target**: Expand `zenoh.io/docs/getting-started/deployment/`.

### 2.3 QoS (Quality of Service) Guide

Zenoh supports Reliability, CongestionControl, and Priority QoS settings on publishers, but the official docs do not have a standalone QoS guide. The API docs reference these types but do not explain:
- When to use `Reliability::Reliable` vs. `BestEffort`
- What `CongestionControl::Drop` vs. `Block` means in practice
- Priority levels and their effect on scheduling

Our tribal-knowledge.json and api-surface.json capture this detail from issues and blog posts.

**Contribution target**: New or expanded section in `zenoh.io/docs/manual/`.

### 2.4 Getting Started — Remove Stale "1.0 rc" Language

The official getting-started page at zenoh.io still contains the note:

> "The examples are updated to use the 1.0 version currently in rc..."

This was accurate in mid-2024. As of early 2026, Zenoh is at 1.7.2 and 1.0 has been stable for 16+ months. This note should be removed and installation instructions updated to reflect that no version specifier is needed for stable installs.

**Contribution target**: Update `https://zenoh.io/docs/getting-started/`.

---

## Priority 3: FAQ Items

These questions come up repeatedly in GitHub issues, ROS Discourse, and Stack Overflow but are not addressed in the official zenoh.io docs. Our faq.md documents 50 Q&A pairs; the following are the highest-value items for upstreaming.

### Troubleshooting Questions (high community recurrence)

| Question | Source | Notes |
|----------|--------|-------|
| "Unable to connect to any of [tcp/...]" — what does this mean? | Multiple GH issues | Firewall, port 7447, wrong endpoint format |
| High latency at low message rates — is this a bug? | ROS Discourse, GH issues | OS scheduler descheduling explanation |
| Application not discovering peers on same machine | GH issues, SO | Loopback / Docker networking explanation |
| TLS handshake fails or times out | GH issues | Cert format, hostname mismatch, `verify_name_on_connect` |
| `z_undeclare_keyexpr` not actually deleting the keyexpr | GH issue zenoh-c | Bug/limitation, known workaround |
| Linker errors about SONAME on Linux with zenoh-c | SO #79644595 | `patchelf` workaround, upstream Cargo issue |
| zenoh-c build failure with `shared_memory` feature | GH issues | bindgen / opaque types workaround |

### Configuration Questions

| Question | Source | Notes |
|----------|--------|-------|
| How do I configure a storage without editing JSON5 directly? | Community | `--cfg` CLI flag pattern |
| How do I run multiple plugin instances of the same plugin? | GH issues | `__plugin__` field explanation |
| How do I bridge zenoh-bridge-ros2dds with a non-default config? | ROS Discourse | `id` field removal, correct config structure |
| DDS bridge only forwards at ~50 Hz instead of 1000 Hz | ROS Discourse | `max_frequency` config, throttling explanation |

**Contribution target**: `https://zenoh.io/docs/` FAQ section or a Troubleshooting guide page.

---

## Priority 4: Benchmark Updates

The current zenoh.io benchmark blog posts are from 2021–2022 (pre-1.0). Our benchmarks.md compiles results from multiple sources including the NTU 2023 research paper. Items not reflected on the official site:

| Benchmark | Result | Source | Missing from zenoh.io |
|-----------|--------|--------|----------------------|
| NTU 2023: Zenoh vs. DDS/MQTT/Kafka at 16 KB, 100 GbE | ~50 Gbps vs. ~14 Gbps DDS, ~5 Gbps MQTT/Kafka | NTU paper + zenoh.io blog (2023-03-21) | Blog post exists; not in main docs |
| Zenoh-Pico vs. XRCE-DDS: 10x throughput advantage | Pico 10x better than XRCE-DDS | ZettaScale blog | Not on main benchmark page |
| Zenoh-Pico vs. MQTT: 40x throughput advantage | — | ZettaScale blog | Not on main benchmark page |
| Zenoh-Pico vs. OPC-UA: 55x throughput advantage | — | ZettaScale blog | Not on main benchmark page |
| Zenoh wire overhead: 5 bytes minimum | vs. XRCE-DDS 75% larger, MQTT 64% larger, OPC-UA 98% larger | ZettaScale blog | Not in main docs |
| NTU 2023 latency: Zenoh-Pico at 5 µs — lowest of all tested | — | NTU paper | Not in main docs |
| Microcontroller: ESP32 WiFi at >5.2k msg/s | — | ZettaScale blog | Not in main docs |

The NTU paper results were summarized in a zenoh.io blog post (2023-03-21) but are not referenced in the main documentation. A dedicated benchmarks page in the docs (not just the blog) would be valuable.

**Contribution target**: New page at `zenoh.io/docs/manual/performance/` with a benchmarks table and link to zenoh-perf repo.

---

## How to Contribute

- **zenoh.io source**: https://github.com/eclipse-zenoh/zenoh.io
- **Docs source directory**: https://github.com/eclipse-zenoh/zenoh.io/tree/main/content/docs
- **Default config reference**: https://github.com/eclipse-zenoh/zenoh/blob/main/DEFAULT_CONFIG.json5
- **Migration guide location**: https://zenoh.io/docs/migration_1.0/
- **Zenoh perf repo**: https://github.com/ZettaScaleLabs/zenoh-perf

The zenoh.io repo accepts PRs. Each doc page is a Markdown file in `content/docs/`. Breaking change documentation and FAQ items are the highest return-on-investment contributions given the volume of community questions they address.
