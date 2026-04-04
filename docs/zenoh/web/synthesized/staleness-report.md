# Zenoh Documentation Staleness Report

Generated: 2026-03-09
Source streams: 22 (scraped 2026-03-09 to 2026-03-10)

---

## Coverage Summary

- Total output files: 62
- Total extracted JSON: 7 files, 238 structured entries
  - api-surface.json: 74 entries (API symbols across 5 languages)
  - benchmarks.json: 28 entries
  - breaking-changes.json: 31 entries
  - concepts.json: 22 entries
  - security-model.json: 1 (nested document)
  - tribal-knowledge.json: 52 entries
  - usage-patterns.json: 30 entries
- Raw source files: 1,384 processed files across 22 streams

---

## Version Currency

| Component | Latest Release | Docs Reference | Status |
|-----------|---------------|----------------|--------|
| zenoh (Rust core) | 1.7.2 (2026-01-08) | "1.0 rc" language in getting-started.md | Stale |
| zenoh-c | 1.7.2 (2026-01-08) | 1.7.0 breaking changes captured | Current |
| zenoh-cpp | 1.7.2 (2026-01-08) | 1.7.0 breaking changes captured | Current |
| zenoh-python | 1.7.2 (2026-01-08) | 1.7.0 breaking changes captured | Current |
| zenoh-java | 1.7.2 | No API docs in output | Gap |
| zenoh-kotlin | 1.7.2 | No API docs in output | Gap |
| zenoh-ts | 1.7.2 | Minimal coverage (3 pages) | Thin |
| zenoh-plugin-ros2dds | 1.7.2 | Covered in ros2.md | Current |
| zenoh-plugin-mqtt | 1.7.2 | Covered in integrations.md | Current |
| All backends (filesystem, influxdb, rocksdb, s3) | 1.7.2 | Covered in integrations.md | Current |

Latest scraped release for all repositories: **1.7.2**.

---

## Version Staleness Detail

### getting-started.md

The getting-started output contains a note reading:

> "The examples are updated to use the 1.0 version currently in rc, which is why version must be specified in the installation command."

This language was copied verbatim from the zenoh.io docs page during the Tavily scrape and is now stale. Zenoh 1.0 shipped in September 2024; as of the scrape date the current release is 1.7.2. The "1.0 rc" framing will mislead users into thinking the stable API is a release candidate.

Additionally, a log snippet in the output reads `zenohd v0.11.0-dev-965-g764be602d` — this is from a pre-release development build and appears in two places in the output. It should be treated as an illustrative example, not the current version.

### configuration.md

- **TLS parameters**: The 1.0.0 breaking change renamed `server_certificate`, `client_certificate`, `server_private_key`, `client_private_key`, `server_name_verification`, and `client_auth` to `listen_certificate`, `connect_certificate`, `listen_private_key`, `connect_private_key`, `verify_name_on_connect`, and `enable_mtls`. The configuration.md output uses the **new** names (confirmed: `listen_certificate`, `connect_certificate` appear; old names have zero occurrences). Status: current.
- **`autoconnect` format**: The 1.0.0 breaking change converted `autoconnect` from a bitfield string to a JSON array. The configuration.md output uses array syntax (`["router", "peer"]`). Status: current.
- **Plugin config**: The `__plugin__` field pattern for multi-instance plugins is referenced. Status: current.
- **Version callout in config page**: References "version 0.6" as a major configuration change milestone. This is accurate historical context but may confuse readers on an ancient migration step.

---

## Breaking Changes Documentation Coverage

31 breaking changes are captured in extracted/breaking-changes.json. Coverage assessment by status:

### Well-documented (covered in migration/ output or configuration.md)
- res() → wait() / await rename (Rust, 1.0.0)
- TLS parameter rename: server/client → listen/connect (1.0.0)
- Session Arc-like clone semantics (1.0.0)
- Serialization moved to zenoh-ext (Rust and Python, 1.0.0)
- zenoh-ext close() → undeclare() rename (1.0.0)
- autoconnect config array format (1.0.0)
- Plugin config __plugin__ field (1.0.0)

### Partially documented (mentioned in output but no step-by-step migration guide)
- Subscriber reliability option removed (1.0.0) — FAQ touches on this
- Admin space key expressions remapped (1.0.0) — noted in concepts
- Encoding constants removed / ZENOH_SERIALIZED added (1.0.0) — mentioned in changelog
- zenoh-ext unstable feature gate (1.0.0) — mentioned in migration notes
- SourceInfo changed to Option<SourceInfo> (1.7.0) — in breaking-changes.json only
- zenoh-python try_recv exception behavior (1.0.0) — in breaking-changes.json only

### Not documented in output (in breaking-changes.json only)
- Callback made opaque / Callback::new() pattern (1.0.0)
- Builder traits made internal (1.0.0)
- Deserialization errors unified — ZDeserializeError (1.0.0)
- flume::Receiver encapsulated → FifoChannelHandler (1.0.0)
- replier_id type changed to z_entity_global_id_t (zenoh-c/cpp, 1.0.0)
- zenoh-c sample payload opaque API (z_bytes_to_slice) (1.0.0)
- zenoh::Config import path changed (1.0.0)
- KeyExpr::from_boxed_string_unchecked rename (1.0.0)
- Selector accessor methods (field → method call) (1.0.0)
- Storage History::Latest enforcement change (1.0.0)
- zenoh-cpp header renamed to zenoh.hxx (1.0.0)
- zenoh-cpp zc_locality → z_locality (1.7.0)
- zenoh-c source_info non-owned type (1.7.0)
- zenoh-python source_info Query.source_info() added (1.7.0)
- zenoh-bridge-ros2dds id field removed from plugin config (1.0.0-rc)

**Summary**: 7 of 31 breaking changes are well-documented, 7 are partially documented, and 17 are captured only in the extracted JSON with no corresponding narrative in the output docs.

---

## Coverage Gaps

### Missing topic areas

- **zenoh-java / zenoh-kotlin API docs**: No API documentation for JVM bindings in the output beyond README-level content. Stream 12 only fetched 3 pages total for TypeScript/Java/Kotlin combined.
- **zenoh-ts (TypeScript) API docs**: Very thin — 3 pages total scraped. The JS/TS binding is production-ready but largely undocumented in this corpus.
- **Storage backend comparison guide**: No document comparing filesystem vs. influxdb vs. rocksdb vs. S3 backends by use case, performance, or configuration complexity.
- **Plugin development guide**: No walkthrough for writing a custom zenoh plugin; the plugin system architecture is described at a high level only.
- **Shared memory (SHM) configuration guide**: SHM is mentioned in benchmarks and concepts but there is no hands-on configuration example.
- **Access control / ACL policy**: The ACL/policy-based access control system is not documented — security.md covers TLS and mTLS but not key-expression-level ACL configuration.
- **zenohd REST API reference**: The REST plugin endpoints are mentioned but not enumerated.
- **Downgrade / version pinning guidance**: No documentation on how to pin or downgrade zenoh versions, important during the rapid 1.x minor release cadence.
- **Windows-specific setup**: Windows build notes exist in getting-started but Windows-specific troubleshooting (WSL, MSVC toolchain, firewall) is absent.

### Thin topic areas

- **Wildcard / intersection key expression semantics**: Concepts.md defines key expressions but does not deeply cover the intersection and inclusion operator rules used for routing.
- **QoS configuration**: Reliability, congestion control, and priority are referenced in API docs but there is no standalone QoS guide.
- **Timestamps and data freshness**: The Timestamp concept is covered in concepts.json but the getting-started and FAQ outputs do not explain how to use timestamps for ordering or deduplication.

---

## Freshness

All 22 streams were scraped within a 12-hour window on 2026-03-09 to 2026-03-10. The data reflects the state of:
- zenoh.io docs and blog as of 2026-03-10
- GitHub release notes and changelogs through 2026-01-08 (latest release: 1.7.2)
- GitHub issues and PRs through 2026-03-10 (420 pages)
- docs.rs/zenoh Rust API docs through 2026-03-10

Potential staleness sources after this scrape date:
- Any zenoh 1.7.3 or 1.8.x releases
- New RFCs merged to the roadmap repo (25 pages scraped)
- Breaking changes in main-branch development that have not yet been released

Recommended re-scrape cadence: monthly for release notes and API streams; quarterly for website and blog.
