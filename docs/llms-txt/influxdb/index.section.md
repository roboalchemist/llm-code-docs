## Source: https://docs.influxdata.com/flux/v0/index.section.md

## Source: https://docs.influxdata.com/kapacitor/v1/index.section.md

## Source: https://docs.influxdata.com/chronograf/v1/index.section.md

## Source: https://docs.influxdata.com/telegraf/v1/index.section.md

## Source: https://docs.influxdata.com/enterprise_influxdb/v1/index.section.md

## Source: https://docs.influxdata.com/influxdb/v1/index.section.md

## Source: https://docs.influxdata.com/influxdb/cloud/index.section.md

## Source: https://docs.influxdata.com/influxdb/v2/index.section.md

## Source: https://docs.influxdata.com/influxdb3/clustered/index.section.md

## Source: https://docs.influxdata.com/influxdb3/cloud-serverless/index.section.md

## Source: https://docs.influxdata.com/influxdb3/cloud-dedicated/index.section.md

## Source: https://docs.influxdata.com/influxdb3/enterprise/index.section.md

## Source: https://docs.influxdata.com/influxdb3/core/index.section.md

---
title: InfluxDB 3 Core documentation
description: InfluxDB 3 Core is an open source time series database designed and optimized for real-time and recent data. Learn how to use and leverage InfluxDB 3 in use cases such as edge data collection, IoT data, and events.
url: https://docs.influxdata.com/influxdb3/core/
product: InfluxDB 3 Core
type: section
pages: 12
estimated_tokens: 50479
child_pages:
- url: https://docs.influxdata.com/influxdb3/core/write-data/
    title: Write data to InfluxDB 3 Core
- url: https://docs.influxdata.com/influxdb3/core/visualize-data/
    title: Visualize data
- url: https://docs.influxdata.com/influxdb3/core/tags/
    title: Related to "Tags"
- url: https://docs.influxdata.com/influxdb3/core/release-notes/
    title: InfluxDB 3 Core release notes
- url: https://docs.influxdata.com/influxdb3/core/reference/
    title: InfluxDB 3 Core reference documentation
- url: https://docs.influxdata.com/influxdb3/core/query-data/
    title: Query data in InfluxDB 3 Core
- url: https://docs.influxdata.com/influxdb3/core/plugins/
    title: Processing engine and Python plugins
- url: https://docs.influxdata.com/influxdb3/core/object-storage/
    title: Configure object storage
- url: https://docs.influxdata.com/influxdb3/core/install/
    title: Install InfluxDB 3 Core
- url: https://docs.influxdata.com/influxdb3/core/get-started/
    title: Get started with InfluxDB 3 Core
- url: https://docs.influxdata.com/influxdb3/core/admin/
    title: Administer InfluxDB 3 Core
---

# InfluxDB 3 Core documentation

InfluxDB 3 Core is a database built to collect, process, transform, and store event and time series data, and is ideal for use cases that require real-time ingest and fast query response times to build user interfaces, monitoring, and automation solutions.

Common use cases include:

- Monitoring sensor data
- Server monitoring
- Application performance monitoring
- Network monitoring
- Financial market and trading analytics
- Behavioral analytics

InfluxDB is optimized for scenarios where near real-time data monitoring is essential and queries need to return quickly to support user experiences such as dashboards and interactive user interfaces.

InfluxDB 3 Core is the InfluxDB 3 open source release.

Core’s feature highlights include:

- Diskless architecture with object storage support (or local disk with no dependencies)
- Fast query response times (under 10ms for last-value queries, or 30ms for distinct metadata)
- Embedded Python VM for plugins and triggers
- Parquet file persistence
- Compatibility with InfluxDB 1.x and 2.x write APIs

[Get started with InfluxDB 3 Core](/influxdb3/core/get-started/)

The Enterprise version adds the following features to Core:

- Historical query capability and single series indexing
- High availability
- Read replicas
- Enhanced security (coming soon)
- Row-level delete support (coming soon)
- Integrated admin UI (coming soon)

For more information, see how to [get started with InfluxDB 3 Enterprise](/influxdb3/enterprise/get-started/).

---

## Write data to InfluxDB 3 Core

Use tools like the

`influxdb3` CLI, Telegraf, and InfluxDB client libraries to write time series data to InfluxDB 3 Core. [line protocol](#line-protocol) is the text-based format used to write data to InfluxDB.

Tools are available to convert other formats (for example—[CSV](/influxdb3/core/write-data/use-telegraf/csv/)) to line protocol.

- [Choose the write endpoint for your workload](#choose-the-write-endpoint-for-your-workload)
    
  - [Timestamp precision across write APIs](#timestamp-precision-across-write-apis)
- [Line protocol](#line-protocol)
    
  - [Line protocol elements](#line-protocol-elements)
- [Write data to InfluxDB](#write-data-to-influxdb)
    
  - [Use InfluxDB client libraries to write data](#use-influxdb-client-libraries-to-write-data)
  - [Use the InfluxDB HTTP API to write data](#use-the-influxdb-http-api-to-write-data)
  - [Use Telegraf to write data](#use-telegraf-to-write-data)
  - [Use the influxdb3 CLI to write data](#use-the-influxdb3-cli-to-write-data)
  - [Best practices for writing data](#best-practices-for-writing-data)
  - [Troubleshoot issues writing data](#troubleshoot-issues-writing-data)
    
### Choose the write endpoint for your workload

When creating new write workloads, use the [InfluxDB HTTP API `/api/v3/write_lp` endpoint](/influxdb3/core/write-data/http-api/v3-write-lp/) and [client libraries](/influxdb3/core/write-data/client-libraries/).

When bringing existing *v1* write workloads, use the InfluxDB 3 Core HTTP API [`/write` endpoint](/influxdb3/core/api/v3/#operation/PostV1Write).

When bringing existing *v2* write workloads, use the InfluxDB 3 Core HTTP API [`/api/v2/write` endpoint](/influxdb3/core/api/v3/#operation/PostV2Write).

**For Telegraf**, use the InfluxDB v1.x [`outputs.influxdb`](/telegraf/v1/output-plugins/influxdb/) or v2.x [`outputs.influxdb_v2`](/telegraf/v1/output-plugins/influxdb_v2/) output plugins. See how to [use Telegraf to write data](/influxdb3/core/write-data/use-telegraf/).

## Timestamp precision across write APIs

InfluxDB 3 Core provides multiple write endpoints for compatibility with different InfluxDB versions. The following table compares timestamp precision support across v1, v2, and v3 write APIs:

| Precision | v1 (/write) | v2 (/api/v2/write) | v3 (/api/v3/write_lp) |
| --- | --- | --- | --- |
| Auto detection | ❌ No | ❌ No | ✅ auto (default) |
| Seconds | ✅ s | ✅ s | ✅ second |
| Milliseconds | ✅ ms | ✅ ms | ✅ millisecond |
| Microseconds | ✅ u or µ | ✅ us | ✅ microsecond |
| Nanoseconds | ✅ ns | ✅ ns | ✅ nanosecond |
| Minutes | ✅ m | ❌ No | ❌ No |
| Hours | ✅ h | ❌ No | ❌ No |
| Default | Nanosecond | Nanosecond | Auto (guessed) |

- All write endpoints accept timestamps in line protocol format.
- InfluxDB 3 Core multiplies timestamps by the appropriate precision value to convert them to nanoseconds for internal storage.
- All timestamps are stored internally as nanoseconds regardless of the precision specified when writing.

## Line protocol

All data written to InfluxDB is written using [line protocol](/influxdb3/core/reference/line-protocol/), a text-based format that lets you provide the necessary information to write a data point to InfluxDB.

### Line protocol elements

In InfluxDB, a point contains a table name, one or more fields, a timestamp, and optional tags that provide metadata about the observation.

Each line of line protocol contains the following elements:

\* Required

- \* **table**: A string that identifies the table to store the data in.
- **tag set**: Comma-delimited list of key value pairs, each representing a tag. Tag keys and values are unquoted strings. *Spaces, commas, and equal characters must be escaped.*
- \* **field set**: Comma-delimited list of key value pairs, each representing a field. Field keys are unquoted strings. *Spaces and commas must be escaped.* Field values can be [strings](/influxdb3/core/reference/line-protocol/#string) (quoted), [floats](/influxdb3/core/reference/line-protocol/#float), [integers](/influxdb3/core/reference/line-protocol/#integer), [unsigned integers](/influxdb3/core/reference/line-protocol/#uinteger), or [booleans](/influxdb3/core/reference/line-protocol/#boolean).
- **timestamp**: [Unix timestamp](/influxdb3/core/reference/line-protocol/#unix-timestamp) associated with the data. InfluxDB supports up to nanosecond precision. *If the precision of the timestamp is not in nanoseconds, you must specify the precision when writing the data to InfluxDB.*

#### Line protocol element parsing

- **table**: Everything before the *first unescaped comma before the first whitespace*.
- **tag set**: Key-value pairs between the *first unescaped comma* and the *first unescaped whitespace*.
- **field set**: Key-value pairs between the *first and second unescaped whitespaces*.
- **timestamp**: Integer value after the *second unescaped whitespace*.
- Lines are separated by the newline character (`\n`). Line protocol is whitespace sensitive.

myTable,tag1=val1,tag2=val2 field1="v1",field2=1i 0000000000000000000

*For schema design recommendations, see [InfluxDB schema design](/influxdb3/core/write-data/best-practices/schema-design/).*

## Write data to InfluxDB

### [Use InfluxDB client libraries to write data](/influxdb3/core/write-data/client-libraries/)

Use InfluxDB API clients to write points as line protocol data to InfluxDB 3 Core.

### [Use the InfluxDB HTTP API to write data](/influxdb3/core/write-data/http-api/)

Use the `/api/v3/write_lp`, `/api/v2/write`, or `/write` HTTP API endpoints to write data to InfluxDB 3 Core.

### [Use Telegraf to write data](/influxdb3/core/write-data/use-telegraf/)

Use Telegraf to collect and write data to InfluxDB 3 Core.

### [Use the influxdb3 CLI to write data](/influxdb3/core/write-data/influxdb3-cli/)

Use the [`influxdb3` CLI](/influxdb3/core/reference/cli/influxdb3/) to write line protocol data to InfluxDB 3 Core.

### [Best practices for writing data](/influxdb3/core/write-data/best-practices/)

Learn about the recommendations and best practices for writing data to InfluxDB 3 Core.

### [Troubleshoot issues writing data](/influxdb3/core/write-data/troubleshoot/)

Troubleshoot issues writing data. Find response codes for failed writes. Discover how writes fail, from exceeding rate or payload limits, to syntax errors and schema conflicts.

[write](/influxdb3/core/tags/write/) [line protocol](/influxdb3/core/tags/line-protocol/)

---

## Visualize data

Use visualization tools like Grafana, Superset, and others to visualize time series data queried from InfluxDB 3 Core.

### [Chronograf](/influxdb3/core/visualize-data/chronograf/)

Chronograf is a data visualization and dashboarding tool designed to visualize data in InfluxDB 1.x. Learn how to use Chronograf with InfluxDB 3 Core.

### [Grafana](/influxdb3/core/visualize-data/grafana/)

Install and run [Grafana](https://grafana.com/) to query and visualize data from InfluxDB 3 Core.

### [Power BI](/influxdb3/core/visualize-data/powerbi/)

Use Microsoft Power BI Desktop with the InfluxDB 3 custom connector to query and visualize data from InfluxDB 3 Core.

#### Related

- [Query data in InfluxDB 3 Core](/influxdb3/core/query-data/)

---

## Related to "Tags"

### [Administration](/influxdb3/core/tags/administration/)

### [Adtk](/influxdb3/core/tags/adtk/)

### [Aggregation](/influxdb3/core/tags/aggregation/)

### [AI](/influxdb3/core/tags/ai/)

### [Alerting](/influxdb3/core/tags/alerting/)

### [Analytics](/influxdb3/core/tags/analytics/)

### [Anomaly-Detection](/influxdb3/core/tags/anomaly-detection/)

### [API](/influxdb3/core/tags/api/)

### [Backup](/influxdb3/core/tags/backup/)

### [C#](/influxdb3/core/tags/c%23/)

### [Cache](/influxdb3/core/tags/cache/)

### [Catalog](/influxdb3/core/tags/catalog/)

### [CLI](/influxdb3/core/tags/cli/)

### [Client Libraries](/influxdb3/core/tags/client-libraries/)

### [Data-Lake](/influxdb3/core/tags/data-lake/)

### [Data-Processing](/influxdb3/core/tags/data-processing/)

### [Data-Write](/influxdb3/core/tags/data-write/)

### [Database](/influxdb3/core/tags/database/)

### [Databases](/influxdb3/core/tags/databases/)

### [Deadman](/influxdb3/core/tags/deadman/)

### [Developer Tools](/influxdb3/core/tags/developer-tools/)

### [Downsampling](/influxdb3/core/tags/downsampling/)

### [Enterprise](/influxdb3/core/tags/enterprise/)

### [Errors](/influxdb3/core/tags/errors/)

### [Evaluation](/influxdb3/core/tags/evaluation/)

### [Event-Detection](/influxdb3/core/tags/event-detection/)

### [Examples](/influxdb3/core/tags/examples/)

### [Export](/influxdb3/core/tags/export/)

### [Flight](/influxdb3/core/tags/flight/)

### [Flight API](/influxdb3/core/tags/flight-api/)

### [Flight Client](/influxdb3/core/tags/flight-client/)

### [Flight RPC](/influxdb3/core/tags/flight-rpc/)

### [Flight SQL](/influxdb3/core/tags/flight-sql/)

### [Forecasting](/influxdb3/core/tags/forecasting/)

### [Glossary](/influxdb3/core/tags/glossary/)

### [Go](/influxdb3/core/tags/go/)

### [GRPC](/influxdb3/core/tags/grpc/)

### [Iceberg](/influxdb3/core/tags/iceberg/)

### [Influxdb3](/influxdb3/core/tags/influxdb3/)

### [Influxql](/influxdb3/core/tags/influxql/)

### [Install](/influxdb3/core/tags/install/)

### [Integration](/influxdb3/core/tags/integration/)

### [Internals](/influxdb3/core/tags/internals/)

### [Java](/influxdb3/core/tags/java/)

### [JavaScript](/influxdb3/core/tags/javascript/)

### [Line Protocol](/influxdb3/core/tags/line-protocol/)

### [LLM](/influxdb3/core/tags/llm/)

### [Machine-Learning](/influxdb3/core/tags/machine-learning/)

### [MCP](/influxdb3/core/tags/mcp/)

### [Metrics](/influxdb3/core/tags/metrics/)

### [Migration](/influxdb3/core/tags/migration/)

### [Monitoring](/influxdb3/core/tags/monitoring/)

### [NodeJS](/influxdb3/core/tags/nodejs/)

### [Notifications](/influxdb3/core/tags/notifications/)

### [Object Storage](/influxdb3/core/tags/object-storage/)

### [Observability](/influxdb3/core/tags/observability/)

### [Official](/influxdb3/core/tags/official/)

### [Performance](/influxdb3/core/tags/performance/)

### [Plugin](/influxdb3/core/tags/plugin/)

### [Plugins](/influxdb3/core/tags/plugins/)

### [Powerbi](/influxdb3/core/tags/powerbi/)

### [Processing Engine](/influxdb3/core/tags/processing-engine/)

### [Prophet](/influxdb3/core/tags/prophet/)

### [Python](/influxdb3/core/tags/python/)

### [Query](/influxdb3/core/tags/query/)

### [Regular Expressions](/influxdb3/core/tags/regular-expressions/)

### [Restore](/influxdb3/core/tags/restore/)

### [Retention](/influxdb3/core/tags/retention/)

### [S3](/influxdb3/core/tags/s3/)

### [Schemas](/influxdb3/core/tags/schemas/)

### [Security](/influxdb3/core/tags/security/)

### [SQL](/influxdb3/core/tags/sql/)

### [State-Tracking](/influxdb3/core/tags/state-tracking/)

### [Stateless](/influxdb3/core/tags/stateless/)

### [Statistics](/influxdb3/core/tags/statistics/)

### [Syntax](/influxdb3/core/tags/syntax/)

### [System Information](/influxdb3/core/tags/system-information/)

### [System-Metrics](/influxdb3/core/tags/system-metrics/)

### [Tables](/influxdb3/core/tags/tables/)

### [Telegraf](/influxdb3/core/tags/telegraf/)

### [Telemetry](/influxdb3/core/tags/telemetry/)

### [Thresholds](/influxdb3/core/tags/thresholds/)

### [Tokens](/influxdb3/core/tags/tokens/)

### [Transformation](/influxdb3/core/tags/transformation/)

### [Upgrade](/influxdb3/core/tags/upgrade/)

### [Visualization](/influxdb3/core/tags/visualization/)

### [Wal](/influxdb3/core/tags/wal/)

### [Window Functions](/influxdb3/core/tags/window-functions/)

### [Write](/influxdb3/core/tags/write/)

---

## InfluxDB 3 Core release notes

### InfluxDB 3 Core and Enterprise relationship

InfluxDB 3 Enterprise is a superset of InfluxDB 3 Core. All updates to Core are automatically included in Enterprise. The Enterprise sections below only list updates exclusive to Enterprise.

## v3.8.3

### Core

#### Bug fixes

- **WAL Buffer**: Fix an edge case that could potentially cause the WAL buffer to overflow

## v3.8.2

### Core (2)

#### Features

- **TLS: Skip certificate verification in CLI subcommands**: Use the new `--tls-no-verify` flag with any CLI subcommand to skip TLS certificate verification when connecting to a server. Useful for testing environments with self-signed certificates.
    
- **Environment variable prefix standardization**: InfluxDB 3 specific environment variables use the `INFLUXDB3_` prefix for consistency. Legacy variable names continue to work (deprecated) for backward compatibility.
    
    `INFLUXDB3_LOG_FILTER` is currently ignored. To set the log filter, use `LOG_FILTER` or the `--log-filter` flag.
    
- **Parquet output format for `show` subcommands**: You can now save query results from the `show` subcommand directly to a Parquet file.
    
- **SQL: `tag_values()` table function**: Query distinct tag values using the new `tag_values()` SQL table function.
    
- **InfluxQL: `SHOW TAG VALUES` improvements**: In Enterprise deployments with auto-DVC enabled, `SHOW TAG VALUES` queries now use the Distinct Value Cache (DVC) automatically for improved performance. The `WHERE` clause is also now supported in `SHOW TAG VALUES` queries backed by the DVC, including compound predicates using `AND` and `OR`.
    
- **InfluxQL: `SHOW RETENTION POLICIES` returns duration**: The `duration` column in `SHOW RETENTION POLICIES` results now returns the configured retention period in InfluxDB v1-compatible format (for example, `168h0m0s`) instead of returning an empty value.
    
- **Ceph S3 backend support**: Use `--aws-s3-custom-backend ceph` with `influxdb3 serve` to connect to Ceph S3-compatible object storage. This enables ETag quote stripping required for conditional PUT operations with Ceph.
    
- **`_internal` database default retention**: The `_internal` system database now defaults to a 7-day retention period (previously infinite). Only admin tokens can modify retention on the `_internal` database.
    
#### Bug fixes (2)

- **Sparse write handling for LVC, DVC, and Processing Engine**: Fixed incorrect behavior when processing sparse writes (writes that include only some fields from a table with multiple field families).
    
- **`influxdb3-launcher`: SSL certificate path on RHEL systems**: Fixed an issue where the `SSL_CERT_FILE` environment variable was not correctly set on affected RHEL-based systems when using the `influxdb3-launcher` script.
    
- Additional bug fixes and performance improvements.
    
### Enterprise

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Features (2)

- **Data-only deletion for databases and tables**: Delete only the stored data from a database or table while preserving catalog entries, schema, and associated resources (tokens, triggers, caches, and processing engine configurations).

#### Bug fixes (3)

- **Compaction stability**: Several fixes to compaction scheduling and processing to improve stability and correctness in multi-node clusters.
    
- **TableIndexCache initialization**: Fixed a concurrency bug that could cause incorrect behavior during `TableIndexCache` initialization.
    
- **Snapshot checkpointing**: Fixed an issue where snapshot checkpoint cleanup was not running as a background task.
    
## v3.8.0

### Core (3)

#### Features (3)

- **Linux Service Management**: Run InfluxDB 3 as a managed system service on Linux ([#27026](https://github.com/influxdata/influxdb/pull/27026)):
  - Use `influxdb3-launcher` script to initialize the service
  - Deploy with systemd on modern Linux distributions
  - Deploy with SysV init on legacy systems
  - Customize service behavior with configuration files

#### Bug fixes (4)

- **CLI**: View only active databases and tables when running `SHOW RETENTION`
- **Database operations**: Receive an error when attempting to delete tables from an already-deleted database
- **Retention Policy**: Receive an error when attempting to modify retention settings on deleted databases

#### Security

- **Processing Engine**: Run processing engine plugins with Python 3.13.11, which includes security and bug fixes ([#27014](https://github.com/influxdata/influxdb/pull/27014))

### Enterprise (2)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Bug fixes (5)

- **Table Limits**: Delete tables without affecting your table limit quota
- **Retention Policy**: Receive an error when attempting to modify retention settings on deleted tables

## v3.7.0

### Core (4)

#### Features (4)

- **HTTP API Enhancements**:
  - All HTTP responses now include a `cluster-uuid` header containing the catalog UUID, enabling clients to identify specific cluster instances programmatically
  - HTTP API now supports multi-member gzip payloads enabling batch operations
- **CLI Commands**:
  - The new `influxdb3 show retention` command displays effective retention periods for each table, showing whether retention is set at the database-level or table-level with human-readable formatting (for example, “7d”, “24h”)

#### Bug fixes (6)

- **Authorization**: Fixed multi-database permission handling to properly authorize queries across multiple databases.
    
- **General Improvements**: Several key bug fixes and performance improvements.
    
### Enterprise (3)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

- **General Improvements**: Several key bug fixes and performance improvements.

## v3.6.0

### Core (5)

#### Features (5)

- **Quick-Start Developer Experience**:
  - `influxdb3` now supports running without arguments for instant database startup, automatically generating IDs and storage flags values based on your system’s setup.
- **Processing Engine**:
  - Plugins now support multiple files instead of single-file limitations.
  - When creating a trigger, you can upload a plugin directly from your local machine using the `--upload` flag.
  - Existing plugin files can now be updated at runtime without recreating triggers.
  - New `system.plugin_files` table and `show plugins` CLI command now provide visibility into all loaded plugin files.
  - Custom plugin repositories are now supported via `--plugin-repo` CLI flag.
  - Python package installation can now be disabled with `--package-manager disabled` for locked-down environments.
  - Plugin file path validation now prevents directory traversal attacks by blocking relative and absolute path patterns.

#### Bug fixes (7)

- **Write API**: Fixed abbreviated precision values (`ns`, `ms`, `us`, `s`) to work correctly with the `/api/v3/write_lp` endpoint. Previously, only full precision names (`nanosecond`, `microsecond`, `millisecond`, `second`) worked.
- **Token management**: Token display now works correctly for hard-deleted databases

### Enterprise (4)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Operational improvements

- **Storage engine**: improvements to the Docker-based license service development environment
- **Catalog consistency**: Node management fixes for catalog edge cases
- Other enhancements and performance improvements

## v3.5.0

### Core (6)

#### Features (6)

- **Custom Plugin Repository**:
  - Use the `--plugin-repo` option with `influxdb3 serve` to specify custom plugin repositories. This enables loading plugins from personal repos or disabling remote repo access.

#### Bug fixes (8)

- **Database reliability**:
  - Table index updates now complete atomically before creating new indices, preventing race conditions that could corrupt database state ([#26838](https://github.com/influxdata/influxdb/pull/26838))
  - Delete operations are now idempotent, preventing errors during object store cleanup ([#26839](https://github.com/influxdata/influxdb/pull/26839))
- **Write path**:
  - Write operations to soft-deleted databases are now rejected, preventing data loss ([#26722](https://github.com/influxdata/influxdb/pull/26722))
- **Runtime stability**:
  - Fixed a compatibility issue that could cause deadlocks for concurrent operations ([#26804](https://github.com/influxdata/influxdb/pull/26804))
- Other bug fixes and performance improvements

#### Security & Misc

- Sensitive environment variable values are now hidden in CLI output and log messages ([#26837](https://github.com/influxdata/influxdb/pull/26837))

### Enterprise (5)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Features (7)

- **Cache optimization**:
  - Last Value Cache (LVC) and Distinct Value Cache (DVC) now populate on creation and only on query nodes, reducing resource usage on ingest nodes.

#### Bug fixes (9)

- **Object store reliability**:
  - Object store operations now use retryable mechanisms with better error handling

#### Operational improvements (2)

- **Compaction optimizations**:
  - Compaction producer now waits 10 seconds before starting cycles, reducing resource contention during startup
  - Enhanced scheduling algorithms distribute compaction work more efficiently across available resources
- **System tables**:
  - System tables now provide consistent data across different node modes (ingest, query, compact), enabling better monitoring in multi-node deployments

## v3.4.2

### Core (7)

#### Bug fixes (10)

- **Database reliability**:
  - TableIndexCache initialization and ObjectStore improvements
  - Persister doesn’t need a TableIndexCache

#### HTTP API changes

- **v2 write API**: Standardized `/api/v2/write` error response format to match other InfluxDB editions. Error responses now use the consistent format: `{"code": "<code>", "message": "<detailed message>"}` ([#26787](https://github.com/influxdata/influxdb/pull/26787))

### Enterprise (6)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Features (8)

- **Storage engine**: Pass in root CA and disable TLS verify for object store
- **Support**: Add support for manually stopping a node

#### Bug fixes (11)

- **Bug fix**: Generation detail path calculation panic
- **Database reliability**: Pass TableIndexCache through to PersistedFiles

#### Operational improvements (3)

- **Compaction optimizations**:
  - Compaction cleaner now waits for 1 hour by default (previously 10 minutes)
  - Compaction producer now waits for 10 seconds before starting compaction cycle
- **Catalog synchronization**: Background catalog update is synchronized every 1 second (previously 10 seconds)
- **Logging improvements**: Added clear logging to indicate what sequence is persisted on producer side and what is consumed by the consumer side

## v3.4.1

### Core (8)

#### Bug Fixes

- Upgrading from 3.3.0 to 3.4.x no longer causes possible catalog migration issues ([#26756](https://github.com/influxdata/influxdb/pull/26756))

## v3.4.0

### Core (9)

#### Features (9)

- **Token Provisioning**:
  - Generate admin tokens offline and use them when starting the database if tokens do not already exist. This is meant for automated deployments and containerized environments. ([#26734](https://github.com/influxdata/influxdb/pull/26734))
- **Azure Endpoint**:
  - Use the `--azure-endpoint` option with `influxdb3 serve` to specify the Azure Blob Storage endpoint for object store connections. ([#26687](https://github.com/influxdata/influxdb/pull/26687))
- **No\_Sync via CLI**:
  - Use the `--no-sync` option with `influxdb3 write` to skip waiting for WAL persistence on write and immediately return a response to the write request. ([#26703](https://github.com/influxdata/influxdb/pull/26703))

#### Bug Fixes (2)

- Validate tag and field names when creating tables ([#26641](https://github.com/influxdata/influxdb/pull/26641))
- Using GROUP BY twice on the same column no longer causes incorrect data ([#26732](https://github.com/influxdata/influxdb/pull/26732))

#### Operational and security improvements

- Introduce a new `v2` catalog path structure:
    
  - `catalog/v2/logs/` directory for log files (instead of `catalogs/`)
  - `catalog/v2/snapshot` file for checkpoint/snapshot files (instead of `_catalog_checkpoint`)
- Reduce verbosity of the TableIndexCache log. ([#26709](https://github.com/influxdata/influxdb/pull/26709))
    
- WAL replay concurrency limit defaults to number of CPU cores, preventing possible OOMs. ([#26715](https://github.com/influxdata/influxdb/pull/26715))
    
- Remove unsafe signal\_handler code. ([#26685](https://github.com/influxdata/influxdb/pull/26685))
    
- Upgrade Python version to 3.13.7-20250818. ([#26686](https://github.com/influxdata/influxdb/pull/26686), [#26700](https://github.com/influxdata/influxdb/pull/26700))
    
- Tags with `/` in the name no longer break the primary key.
    
### Enterprise (7)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Features (10)

- **Token Provisioning**:
    
  - Generate *resource* and *admin* tokens offline and use them when starting the database.
- Select a home or trial license without using an interactive terminal. Use `--license-type` \[home | trial | commercial\] option to the `influxdb3 serve` command to automate the selection of the license type.
    
#### Bug Fixes (3)

- Don’t initialize the Processing Engine when the specified `--mode` does not require it.
- Don’t panic when `INFLUXDB3_PLUGIN_DIR` is set in containers without the Processing Engine enabled.

## v3.3.0

### Core (10)

#### Features (11)

- **Database management**:
  - Add `influxdb_schema` system table for database schema management ([#26640](https://github.com/influxdata/influxdb/pull/26640))
  - Add `system.processing_engine_trigger_arguments` table for trigger configuration management ([#26604](https://github.com/influxdata/influxdb/pull/26604))
  - Add write path logging to capture database name and client IP address for failed writes. The IP address is fetched from `x-forwarded-for` header if available, `x-real-ip` if available, or remote address as reported by TlsStream/AddrStream ([#26616](https://github.com/influxdata/influxdb/pull/26616))
- **Storage engine**: Introduce `TableIndexCache` for efficient automatic cleanup of expired gen1 Parquet files based on retention policies and hard deletes. Includes new background loop for applying data retention policies with configurable intervals and comprehensive purge operations for tables and retention period expired data ([#26636](https://github.com/influxdata/influxdb/pull/26636))
- **Authentication and security**: Add admin token recovery server that allows regenerating lost admin tokens without existing authentication. Includes new `--admin-token-recovery-http-bind` option for running recovery server on separate port, with automatic shutdown after successful token regeneration ([#26594](https://github.com/influxdata/influxdb/pull/26594))
- **Build process**: Allow passing git hash via environment variable in build process ([#26618](https://github.com/influxdata/influxdb/pull/26618))

#### Bug Fixes (4)

- **Database reliability**:
  - Fix URL-encoded table name handling failures ([#26586](https://github.com/influxdata/influxdb/pull/26586))
  - Allow hard deletion of existing soft-deleted schema ([#26574](https://github.com/influxdata/influxdb/pull/26574))
- **Authentication**: Fix AWS S3 API error handling when tokens are expired ([#1013](https://github.com/influxdata/influxdb/pull/1013))
- **Query processing**: Set nanosecond precision as default for V1 query API CSV output ([#26577](https://github.com/influxdata/influxdb/pull/26577))
- **CLI reliability**:
  - Mark `--object-store` CLI argument as explicitly required ([#26575](https://github.com/influxdata/influxdb/pull/26575))
  - Add help text for the new update subcommand ([#26569](https://github.com/influxdata/influxdb/pull/26569))

### Enterprise (8)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Features (12)

- **License management**:
  - Improve licensing suggestions for Core users
  - Update license information handling
- **Database management**:
  - Enhance `TableIndexCache` with advanced features beyond Core’s basic cleanup: persistent snapshots, object store integration, merge operations for distributed environments, and recovery capabilities for multi-node clusters
  - Add `TableIndexSnapshot`, `TableIndex`, and `TableIndices` types for distributed table index management
- **Support**: Include contact information in trial error messages
- **Telemetry**: Send onboarding telemetry before licensing setup

#### Bug Fixes (5)

- **Compaction stability**:
  - Fix compactor re-compaction issues on max generation data overwrite
  - Fix compactor to treat “all” mode as “ingest” mode
- **Database reliability**:
  - Add missing system tables to compact mode
- **Storage integrity**: Update Parquet file paths to use 20 digits of 0-padding
- **General fixes**:
  - Only load processing engine in correct server modes
  - Remove load generator alias clash

## v3.2.1

### Core (11)

#### Features (13)

- **Enhanced database lifecycle management**:
  - Allow updating the hard deletion date for already-deleted databases and tables, providing flexibility in managing data retention and compliance requirements
  - Include `hard_deletion_date` column in `_internal` system tables (`databases` and `tables`) for better visibility into data lifecycle and audit trails

#### Bug Fixes (6)

- **CLI improvements**:
  - Added help text for the new `update` subcommand for database and table update features ([#26569](https://github.com/influxdata/influxdb/pull/26569))
  - `--object-store` and storage configuration parameters are required for the `serve` command ([#26575](https://github.com/influxdata/influxdb/pull/26575))
- **Query processing**: Fixed V1-compatible `/query` HTTP API endpoint to correctly default to nanosecond precision (`ns`) for CSV output, ensuring backward compatibility with InfluxDB 1.x clients and preventing data precision loss ([#26577](https://github.com/influxdata/influxdb/pull/26577))
- **Database reliability**: Fixed issue preventing hard deletion of soft-deleted databases and tables, enabling complete data removal for compliance and storage management needs ([#26574](https://github.com/influxdata/influxdb/pull/26574))

### Enterprise (9)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Features (14)

- **License management improvements**: New `influxdb3 show license` command displays detailed license information including type, expiration date, and resource limits, making it easier to monitor license status and compliance

#### Bug Fixes (7)

- **API stability**: Fixed HTTP API trigger specification to use the correct `"request:REQUEST_PATH"` syntax, ensuring proper request-based trigger configuration for processing engine workflows

## v3.2.0

**Core**: revision 1ca3168bee  
**Enterprise**: revision 1ca3168bee

### Core (12)

#### Features (15)

- **Hard delete for databases and tables**: Permanently delete databases and tables, enabling complete removal of data structures for compliance and storage management ([#26553](https://github.com/influxdata/influxdb/pull/26553))
- **AWS credentials auto-reload**: Support dynamic reloading of ephemeral AWS credentials from files, improving security and reliability when using AWS services ([#26537](https://github.com/influxdata/influxdb/pull/26537))
- **Database retention period support**: Add retention period support for databases via CLI commands (`create database` and `update database` commands) and HTTP APIs ([#26520](https://github.com/influxdata/influxdb/pull/26520)):
  - New CLI command: `update database --retention-period`
- **Configurable lookback duration**: Users can specify lookback duration for PersistedFiles buffer, providing better control over query performance ([#26528](https://github.com/influxdata/influxdb/pull/26528))
- **WAL replay concurrency control**: Add concurrency limits for WAL (Write-Ahead Log) replay to improve startup performance and resource management ([#26483](https://github.com/influxdata/influxdb/pull/26483))
- **Enhanced write path**: Separate write path executor with unbounded memory for improved write performance ([#26455](https://github.com/influxdata/influxdb/pull/26455))

#### Bug Fixes (8)

- **WAL corruption handling**: Handle corrupt WAL files during replay without panic, improving data recovery and system resilience ([#26556](https://github.com/influxdata/influxdb/pull/26556))
- **Database naming validation**: Disallow underscores in database names when created via API to ensure consistency ([#26507](https://github.com/influxdata/influxdb/pull/26507))
- **Object store cleanup**: Automatic intermediate directory cleanup for file object store, preventing storage bloat ([#26480](https://github.com/influxdata/influxdb/pull/26480))

#### Additional Updates

- Track generation 1 duration in catalog for better performance monitoring ([#26508](https://github.com/influxdata/influxdb/pull/26508))
- Add retention period support to the catalog ([#26479](https://github.com/influxdata/influxdb/pull/26479))
- Update help text for improved user experience ([#26509](https://github.com/influxdata/influxdb/pull/26509))

### Enterprise (10)

All Core updates are included in Enterprise. Additional Enterprise-specific features and fixes:

#### Features (16)

- **License management improvements**:
  - New `influxdb3 show license` command to display current license information
- **Table-level retention period support**: Add retention period support for individual tables in addition to database-level retention, providing granular data lifecycle management
  - New CLI commands: `create table --retention-period` and `update table --retention-period`
  - Set or clear table-specific retention periods independent of database settings
- **Compaction improvements**:
  - Address compactor restart issues for better reliability
  - Track compacted generation durations in catalog for monitoring
  - Disable Parquet cache for ingest mode to optimize memory usage

#### Bug Fixes (9)

- **Query optimization**: Correctly partition query chunks into generations for improved performance
- **Data integrity**: Don’t delete generation 1 files as part of compaction process
- **License handling**: Trim whitespace from license file contents after reading to prevent validation issues

## v3.1.0

**Core**: revision 482dd8aac580c04f37e8713a8fffae89ae8bc264

**Enterprise**: revision 2cb23cf32b67f9f0d0803e31b356813a1a151b00

### Core (13)

#### Token and Security Updates

- Named admin tokens can now be created, with configurable expirations
- `health`, `ping`, and `metrics` endpoints can now be opted out of authorization
- `Basic $TOKEN` is now supported for all APIs
- Additional info available when creating a new token
- Additional info available when starting InfuxDB using `--without-auth`

#### Additional Updates (2)

- New catalog metrics available for count operations
- New object store metrics available for transfer latencies and transfer sizes
- New query duration metrics available for Last Value caches
- `/ping` API now contains versioning headers
- Other performance improvements

#### Fixes

- New tags are now backfilled with NULL instead of empty strings
- Bitcode deserialization error fixed
- Series key metadata not persisting to Parquet is now fixed
- Other general fixes and corrections

### Enterprise (11)

#### Token and Security Updates (2)

- Resource tokens now use resource names in `show tokens`
- Tokens can now be granted `CREATE` permission for creating databases

#### Additional Updates (3)

- Last value caches reload on restart
- Distinct value caches reload on restart
- Other performance improvements
- Replaces remaining “INFLUXDB\_IOX” Dockerfile environment variables with the following:
  - `ENV INFLUXDB3_OBJECT_STORE=file`
  - `ENV INFLUXDB3_DB_DIR=/var/lib/influxdb3`

#### Fixes (2)

- Improvements and fixes for license validations
- False positive fixed for catalog error on shutdown
- UX improvements for error and onboarding messages
- Other general fixes and corrections

## v3.0.3

**Core**: revision 384c457ef5f0d5ca4981b22855e411d8cac2688e

**Enterprise**: revision 34f4d28295132b9efafebf654e9f6decd1a13caf

### Core (14)

#### Fixes (3)

- Prevent operator token, `_admin`, from being deleted.

### Enterprise (12)

#### Fixes (4)

- Fix object store info digest that is output during onboarding.
- Fix issues with false positive catalog error on shutdown.
- Fix licensing validation issues.
- Other fixes and performance improvements.

## v3.0.2

**Core**: revision d80d6cd60049c7b266794a48c97b1b6438ac5da9

**Enterprise**: revision e9d7e03c2290d0c3e44d26e3eeb60aaf12099f29

### Core (15)

#### Security updates

- Generate testing TLS certificates on the fly.
- Set the TLS CA via the INFLUXDB3\_TLS\_CA environment variable.
- Enforce a minimum TLS version for enhanced security.
- Allow CORS requests from browsers.

#### General updates

- Support the `--format json` option in the token creation output.
- Remove the Last Values Cache size limitation to improve performance and flexibility.
- Incorporate additional performance improvements.

#### Fixes (5)

- Fix a counting bug in the distinct cache.
- Fix how the distinct cache handles rows with null values.
- Fix handling of `group by` tag columns that use escape quotes.
- Sort the IOx table schema consistently in the `SHOW TABLES` command.

### Enterprise (13)

#### Updates

- Introduce a command and system table to list cluster nodes.
- Support multiple custom permission argument matches.
- Improve overall performance.

#### Fixes (6)

- Initialize the object store only once.
- Prevent the Home license server from crashing on restart.
- Enforce the `--num-cores` thread allocation limit.

## v3.0.1

**Core**: revision d7c071e0c4959beebc7a1a433daf8916abd51214

**Enterprise**: revision 96e4aad870b44709e149160d523b4319ea91b54c

### Core (16)

#### Updates (2)

- TLS CA can now be set with an environment variable: `INFLUXDB3_TLS_CA`
- Other general performance improvements

#### Fixes (7)

- The `--tags` argument is now optional for creating a table, and additionally now requires at least one tag *if* specified

### Enterprise (14)

#### Updates (3)

- Catalog limits for databases, tables, and columns are now configurable using `influxdb3 serve` options:
  - `--num-database-limit`
  - `--num-table-limit`
  - `--num-total-columns-per-table-limit`
- Improvements to licensing prompts for clarity
- Other general performance improvements

#### Fixes (8)

- **Home** license thread count log errors

## v3.0.0

### Core (17)

#### Breaking Changes

- **Parquet cache configuration**: Replaced `--parquet-mem-cache-size-mb` option with `--parquet-mem-cache-size`. The new option accepts values in megabytes (as an integer) or as a percentage of total available memory (for example, `20%`). The default value changed from `1000` MB to `20%` of total available memory. The environment variable `INFLUXDB3_PARQUET_MEM_CACHE_SIZE_MB` was replaced with `INFLUXDB3_PARQUET_MEM_CACHE_SIZE`. ([#26023](https://github.com/influxdata/influxdb/pull/26023))
- **Memory settings updates**:
  - Force snapshot memory threshold now defaults to `50%` of available memory
  - DataFusion execution memory pool now defaults to `20%` of available memory

#### General Updates

- Performance and reliability improvements.

### Enterprise (15)

#### Token Support

- Authorization is now turned on by default.
- Token support for database level permissions are now available.
- Token support for system level queries are now available.

#### General Updates (2)

- You can now use Commercial, Trial, and At-Home licenses.

## v3.0.0-0.beta.3

**Core**: revision f881c5844bec93a85242f26357a1ef3ebf419dd3

**Enterprise**: revision 6bef9e700a59c0973b0cefdc6baf11583933e262

### Core (18)

#### General Improvements

- InfluxDB 3 now supports graceful shutdowns when sending the interrupt signal to the service.

#### Bug fixes (12)

- Empty batches in JSON format results are now handled properly
- The Processing Engine now properly extracts data from DictionaryArrays

### Enterprise (16)

#### Multi-node improvements

- Query nodes now automatically detect new ingest nodes

#### Bug fixes (13)

- Several fixes for compaction planning and processing
- The Processing Engine now properly extracts data from DictionaryArrays

## v3.0.0-0.beta.2

**Core**: revision 033e1176d8c322b763b4aefb24686121b1b24f7c

**Enterprise**: revision e530fcd498c593cffec2b56d4f5194afc717d898

This update brings several backend performance improvements to both Core and Enterprise in preparation for additional new features over the next several weeks.

## v3.0.0-0.beta.1

### Core (19)

#### Features (17)

##### Query and storage enhancements

- New ability to stream response data for CSV and JSON queries, similar to how JSONL streaming works
- Parquet files are now cached on the query path, improving performance
- Query buffer is incrementally cleared when snapshotting, lowering memory spikes

##### Processing engine improvements

- New Trigger Types:
  - *Scheduled*: Run Python plugins on custom, time-defined basis
  - *Request*: Call Python plugins via HTTP requests
- New in-memory cache for storing data temporarily; cached data can be stored for a single trigger or across all triggers
- Integration with virtual environments and install packages:
  - Specify Python virtual environment via CLI or `VIRTUAL_ENV` variable
  - Install packages or a `requirements.txt`
- Python plugins are now implemented through triggers only. Simply create a trigger that references your Python plugin code file directly
- Snapshots are now persisted in parallel, improving performance by running jobs simultaneously, rather than sequentially
- Write to logs from within the Processing Engine

##### Database and CLI improvements

- You can now specify the precision on your timestamps for writes using the `--precision` flag. Includes nano/micro/milli/seconds (ns/us/ms/s)
- Added a new `show` system subcommand to display system tables with different options via SQL (default limit: 100)
- Clearer table creation error messages

#### Bug fixes (14)

- If a database was created and the service was killed before any data was written, the database would not be retained
- A last cache with specific “value” columns could not be queried
- Running CTRL-C no longer stopped an InfluxDB process, due to a Python trigger
- A previous build had broken JSON queries for RecordBatches
- There was an issue with the distinct cache that caused panics

#### Parameter changes

For Core and Enterprise, there are parameter changes for simplicity:

| Old Parameter | New Parameter |
| --- | --- |
| --writer-id--host-id | --node-id |

### Enterprise features

#### Cluster management

- Nodes are now associated with *clusters*, simplifying compaction, read replication, and processing
- Node specs are now available for simpler management of cache creations

#### Mode types

- Set `ingest`, `query`, `compact`, and `process` individually per node

### Enterprise parameter changes

For Enterprise, additional parameters for the `serve` command have been consolidated for simplicity:

| Old Parameter | New Parameter |
| --- | --- |
| --read-from-node-ids--compact-from-node-ids | --cluster-id |
| --run-compactions--mode=compactor | --mode=compact--mode=compact |

In addition to the above changes, `--cluster-id` is now a required parameter for all new instances.

#### Related (2)

- [Get started with InfluxDB 3 Core](/influxdb3/core/get-started/)

---

## InfluxDB 3 Core reference documentation

### [InfluxDB 3 Core configuration options](/influxdb3/core/reference/config-options/)

InfluxDB 3 Core lets you customize your server configuration by using `influxdb3 serve` command options or by setting environment variables.

### [Command line tools](/influxdb3/core/reference/cli/)

View command line tools used to manage and interact with InfluxDB 3 Core.

### [Line protocol reference](/influxdb3/core/reference/line-protocol/)

InfluxDB 3 Core uses line protocol to write data points. It is a text-based format that provides the table, tag set, field set, and timestamp of a data point.

### [Processing engine reference](/influxdb3/core/reference/processing-engine/)

The InfluxDB 3 Processing engine is an embedded Python virtual machine that runs inside InfluxDB 3 Core to execute Python code in response to triggers you define without requiring external application servers or middleware.

### [SQL reference documentation](/influxdb3/core/reference/sql/)

Learn the SQL syntax and structure used to query InfluxDB.

### [InfluxQL reference documentation](/influxdb3/core/reference/influxql/)

InfluxQL is an SQL-like query language for interacting with data in InfluxDB.

### [InfluxDB HTTP API](/influxdb3/core/reference/api/)

The InfluxDB HTTP API for InfluxDB 3 Core provides a programmatic interface for interactions with InfluxDB, including writing, querying, and processing data, and managing an InfluxDB 3 instance.

### [API client libraries](/influxdb3/core/reference/client-libraries/)

InfluxDB client libraries are language-specific tools that integrate with InfluxDB APIs. View the list of available client libraries.

### [InfluxDB 3 Core internals](/influxdb3/core/reference/internals/)

Learn about InfluxDb 3 Core internal systems and mechanisms.

### [Naming restrictions and conventions](/influxdb3/core/reference/naming-restrictions/)

Learn about naming restrictions and conventions for databases, tables, tags, fields, and other identifiers in InfluxDB 3 Core.

### [Usage telemetry](/influxdb3/core/reference/telemetry/)

InfluxData collects telemetry data to help improve the InfluxDB 3 Core. Learn what data InfluxDB 3 Core collects and sends to InfluxData, how it’s used, and how you can opt out.

### [Glossary](/influxdb3/core/reference/glossary/)

Terms related to InfluxData products and platforms.

### [Sample data](/influxdb3/core/reference/sample-data/)

Sample datasets are used throughout the the InfluxDB 3 Core documentation to demonstrate functionality. Use the following sample datasets to replicate provided examples.

---

## Query data in InfluxDB 3 Core

Learn to query data in InfluxDB 3 Core.

### [Execute queries](/influxdb3/core/query-data/execute-queries/)

Use tools and libraries to query data from InfluxDB 3 Core.

### [Query data with SQL](/influxdb3/core/query-data/sql/)

Learn to query data in InfluxDB 3 Core using SQL.

### [Query data with InfluxQL](/influxdb3/core/query-data/influxql/)

Learn to use InfluxQL to query data in InfluxDB 3 Core.

[query](/influxdb3/core/tags/query/)

---

## Processing engine and Python plugins

Use the Processing Engine in InfluxDB 3 Core to extend your database with custom Python code. Trigger your code on write, on a schedule, or on demand to automate workflows, transform data, and create API endpoints.

## What is the Processing Engine?

The Processing Engine is an embedded Python virtual machine that runs inside your InfluxDB 3 Core database. You configure *triggers* to run your Python *plugin* code in response to:

- **Data writes** - Process and transform data as it enters the database
- **Scheduled events** - Run code at defined intervals or specific times
- **HTTP requests** - Expose custom API endpoints that execute your code

You can use the Processing Engine’s in-memory cache to manage state between executions and build stateful applications directly in your database.

This guide walks you through setting up the Processing Engine, creating your first plugin, and configuring triggers that execute your code on specific events.

## Before you begin

Ensure you have:

- A working InfluxDB 3 Core instance
- Access to command line
- Python installed if you’re writing your own plugin
- Basic knowledge of the InfluxDB CLI

Once you have all the prerequisites in place, follow these steps to implement the Processing Engine for your data automation needs.

- [Set up the Processing Engine](#set-up-the-processing-engine)
- [Add a Processing Engine plugin](#add-a-processing-engine-plugin)
  - [Upload plugins from local machine](#upload-plugins-from-local-machine)
  - [Update existing plugins](#update-existing-plugins)
  - [View loaded plugins](#view-loaded-plugins)
- [Create a trigger](#create-a-trigger)
- [Manage plugin dependencies](#manage-plugin-dependencies)
- [Plugin security](#plugin-security)

## Set up the Processing Engine

The Processing Engine activates when `--plugin-dir` or `INFLUXDB3_PLUGIN_DIR` is configured.

### Default behavior by deployment type

| Deployment | Default state | Configuration |
| --- | --- | --- |
| Docker images | Enabled | INFLUXDB3_PLUGIN_DIR=/plugins |
| DEB/RPM packages | Enabled | plugin-dir="/var/lib/influxdb3/plugins" |
| Binary/source | Disabled | No plugin-dir configured |

If you installed InfluxDB 3 Core using Docker or a DEB/RPM package, the Processing Engine is already enabled—skip to [Add a Processing Engine plugin](#add-a-processing-engine-plugin). To disable the Processing Engine, see [Enable and disable the Processing Engine](/influxdb3/core/reference/processing-engine/#enable-and-disable-the-processing-engine).

### Enable the Processing Engine manually

To activate the Processing Engine when running from a binary or source build, start your InfluxDB 3 Core server with the `--plugin-dir` flag. This flag tells InfluxDB where to load your plugin files.

#### Keep the influxdb3 binary with its python directory

The influxdb3 binary requires the adjacent `python/` directory to function. If you manually extract from tar.gz, keep them in the same parent directory:

```
your-install-location/
├── influxdb3
└── python/
```

Add the parent directory to your PATH; do not move the binary out of this directory.

```bash
influxdb3 serve \
  --NODE_ID \
  --object-store OBJECT_STORE_TYPE \
  --plugin-dir PLUGIN_DIR
```

In the example above, replace the following:

- `NODE_ID`: Unique identifier for your instance
- `OBJECT_STORE_TYPE`: Type of object store (for example, file or s3)
- `PLUGIN_DIR`: Absolute path to the directory where plugin files are stored. Store all plugin files in this directory or its subdirectories.

#### Use custom plugin repositories

By default, plugins referenced with the `gh:` prefix are fetched from the official [influxdata/influxdb3\_plugins](https://github.com/influxdata/influxdb3_plugins) repository. To use a custom repository, add the `--plugin-repo` flag when starting the server. See [Use a custom plugin repository](#option-3-use-a-custom-plugin-repository) for details.

### Configure distributed environments

When running InfluxDB 3 Core in a distributed setup, follow these steps to configure the Processing Engine:

1. Decide where each plugin should run
- Data processing plugins, such as WAL plugins, run on ingester nodes
- HTTP-triggered plugins run on nodes handling API requests
- Scheduled plugins can run on any configured node
2. Enable plugins on the correct instance
3. Maintain identical plugin files across all instances where plugins run
- Use shared storage or file synchronization tools to keep plugins consistent

#### Provide plugins to nodes that run them

Configure your plugin directory on the same system as the nodes that run the triggers and plugins.

## Add a Processing Engine plugin

A plugin is a Python script that defines a function with a trigger-compatible (*trigger spec*) signature. When the specified event occurs, InfluxDB runs the plugin.

### Choose a plugin strategy

You have two main options for adding plugins to your InfluxDB instance:

- [Use example plugins](#use-example-plugins) - Get started with prebuilt plugins
- [Create a custom plugin](#create-a-custom-plugin) - Build your own for specialized use cases

### Use example plugins

InfluxData maintains a repository of official and community plugins that you can use immediately in your Processing Engine setup.

Browse the [plugin library](/influxdb3/core/plugins/library/) to find examples and InfluxData official plugins for:

- **Data transformation**: Process and transform incoming data
- **Alerting**: Send notifications based on data thresholds
- **Aggregation**: Calculate statistics on time series data
- **Integration**: Connect to external services and APIs
- **System monitoring**: Track resource usage and health metrics

For community contributions, see the [influxdb3\_plugins repository](https://github.com/influxdata/influxdb3_plugins) on GitHub.

#### Add example plugins

You have two options for using plugins from the repository:

##### Option 1: Copy plugins locally

Clone the `influxdata/influxdb3_plugins` repository and copy plugins to your configured plugin directory:

```bash
# Clone the repository
git clone https://github.com/influxdata/influxdb3_plugins.git
   
# Copy a plugin to your configured plugin directory
cp influxdb3_plugins/influxdata/system_metrics/system_metrics.py /path/to/plugins/
```

##### Option 2: Reference plugins directly from GitHub

Skip downloading plugins by referencing them directly from GitHub using the `gh:` prefix:

```bash
# Create a trigger using a plugin from GitHub
influxdb3 create trigger \
  --trigger-spec "every:1m" \
  --path "gh:influxdata/system_metrics/system_metrics.py" \
  --database my_database \
  system_metrics
```

This approach:

- Ensures you’re using the latest version
- Simplifies updates and maintenance
- Reduces local storage requirements

##### Option 3: Use a custom plugin repository

For organizations that maintain their own plugin repositories or need to use private/internal plugins, configure a custom plugin repository URL:

```bash
# Start the server with a custom plugin repository
influxdb3 serve \
  --node-id node0 \
  --object-store file \
  --data-dir ~/.influxdb3 \
  --plugin-dir ~/.plugins \
  --plugin-repo "https://internal.company.com/influxdb-plugins/"
```

Then reference plugins from your custom repository using the `gh:` prefix:

```bash
# Fetches from: https://internal.company.com/influxdb-plugins/myorg/custom_plugin.py
influxdb3 create trigger \
  --trigger-spec "every:5m" \
  --path "gh:myorg/custom_plugin.py" \
  --database my_database \
  custom_trigger
```

**Use cases for custom repositories:**

- **Private plugins**: Host proprietary plugins not suitable for public repositories
- **Air-gapped environments**: Use internal mirrors when external internet access is restricted
- **Development and staging**: Test plugins from development branches before production deployment
- **Compliance requirements**: Meet data governance policies requiring internal hosting

The `--plugin-repo` option accepts any HTTP/HTTPS URL that serves raw plugin files. See the [plugin-repo configuration option](/influxdb3/core/reference/config-options/#plugin-repo) for more details.

Plugins have various functions such as:

- Receive plugin-specific arguments (such as written data, call time, or an HTTP request)
- Access keyword arguments (as `args`) passed from *trigger arguments* configurations
- Access the `influxdb3_local` shared API to write data, query data, and managing state between executions

For more information about available functions, arguments, and how plugins interact with InfluxDB, see how to [Extend plugins](/influxdb3/core/extend-plugin/).

### Create a custom plugin

To build custom functionality, you can create your own Processing Engine plugin.

#### Prerequisites

Before you begin, make sure:

- The Processing Engine is enabled on your InfluxDB 3 Core instance.
- You’ve configured the `--plugin-dir` where plugin files are stored.
- You have access to that plugin directory.

#### Steps to create a plugin:

- [Choose your plugin type](#choose-your-plugin-type)
- [Create your plugin file](#create-your-plugin-file)
- [Next Steps](#next-steps)

#### Choose your plugin type

Choose a plugin type based on your automation goals:

| Plugin Type | Best For |
| --- | --- |
| Data write | Processing data as it arrives |
| Scheduled | Running code at specific intervals or times |
| HTTP request | Running code on demand via API endpoints |

#### Create your plugin file

Plugins now support both single-file and multifile architectures:

**Single-file plugins:**

- Create a `.py` file in your plugins directory
- Add the appropriate function signature based on your chosen plugin type
- Write your processing logic inside the function

**Multifile plugins:**

- Create a directory in your plugins directory
- Add an `__init__.py` file as the entry point (required)
- Organize supporting modules in additional `.py` files
- Import and use modules within your plugin code

##### Example multifile plugin structure

```
my_plugin/
├── __init__.py       # Required - entry point with trigger function
├── utils.py          # Supporting module
├── processors.py     # Data processing functions
└── config.py         # Configuration helpers
```

The `__init__.py` file must contain your trigger function:

```python
# my_plugin/__init__.py
from .processors import process_data
from .config import get_settings

def process_writes(influxdb3_local, table_batches, args=None):
    settings = get_settings()
    for table_batch in table_batches:
        process_data(influxdb3_local, table_batch, settings)
```

Supporting modules can contain helper functions:

```python
# my_plugin/processors.py
def process_data(influxdb3_local, table_batch, settings):
    # Processing logic here
    pass
```

After writing your plugin, [create a trigger](#create-a-trigger) to connect it to a database event and define when it runs.

#### Create a data write plugin

Use a data write plugin to process data as it’s written to the database. These plugins use [`table:` or `all_tables:`](#trigger-on-data-writes) trigger specifications. Ideal use cases include:

- Data transformation and enrichment
- Alerting on incoming values
- Creating derived metrics

```python
def process_writes(influxdb3_local, table_batches, args=None):
    # Process data as it's written to the database
    for table_batch in table_batches:
        table_name = table_batch["table_name"]
        rows = table_batch["rows"]
        
        # Log information about the write
        influxdb3_local.info(f"Processing {len(rows)} rows from {table_name}")
        
        # Write derived data back to the database
        line = LineBuilder("processed_data")
        line.tag("source_table", table_name)
        line.int64_field("row_count", len(rows))
        influxdb3_local.write(line)
```

#### Create a scheduled plugin

Scheduled plugins run at defined intervals using [`every:` or `cron:`](#trigger-on-a-schedule) trigger specifications. Use them for:

- Periodic data aggregation
- Report generation
- System health checks

```python
def process_scheduled_call(influxdb3_local, call_time, args=None):
    # Run code on a schedule
    
    # Query recent data
    results = influxdb3_local.query("SELECT * FROM metrics WHERE time > now() - INTERVAL '1 hour'")
    
    # Process the results
    if results:
        influxdb3_local.info(f"Found {len(results)} recent metrics")
    else:
        influxdb3_local.warn("No recent metrics found")
```

#### Create an HTTP request plugin

HTTP request plugins respond to API calls using [`request:`](#trigger-on-http-requests) trigger specifications. Use them for:

- Creating custom API endpoints
- Webhooks for external integrations
- User interfaces for data interaction

```python
def process_request(influxdb3_local, query_parameters, request_headers, request_body, args=None):
    # Handle HTTP requests to a custom endpoint
    
    # Log the request parameters
    influxdb3_local.info(f"Received request with parameters: {query_parameters}")
    
    # Process the request body
    if request_body:
        import json
        data = json.loads(request_body)
        influxdb3_local.info(f"Request data: {data}")
    
    # Return a response (automatically converted to JSON)
    return {"status": "success", "message": "Request processed"}
```

#### Next steps

After writing your plugin:

- [Create a trigger](#create-a-trigger) to connect your plugin to database events
- [Install any Python dependencies](#manage-plugin-dependencies) your plugin requires
- Learn how to [extend plugins with the API](/influxdb3/core/extend-plugin/)

### Upload plugins from local machine

For local development and testing, you can upload plugin files directly from your machine when creating triggers. This eliminates the need to manually copy files to the server’s plugin directory.

- [Upload a plugin using the influxdb3 CLI](#upload-a-plugin-using-the-influxdb3-cli)
- [Upload a plugin using the HTTP API](#upload-a-plugin-using-the-http-api)

#### Upload a plugin using the influxdb3 CLI

Use the `--upload` flag with `--path` to transfer local files or directories:

```bash
# Upload single-file plugin
influxdb3 create trigger \
  --trigger-spec "every:10s" \
  --path "/local/path/to/plugin.py" \
  --upload \
  --database metrics \
  my_trigger

# Upload multifile plugin directory
influxdb3 create trigger \
  --trigger-spec "every:30s" \
  --path "/local/path/to/plugin-dir" \
  --upload \
  --database metrics \
  complex_trigger
```

For more information, see the [`influxdb3 create trigger` CLI reference](/influxdb3/core/reference/cli/influxdb3/create/trigger/).

#### Upload a plugin using the HTTP API

To upload a plugin file using the HTTP API, send a `PUT` request to the `/api/v3/plugins/files` endpoint:

[PUT localhost:8181/api/v3/plugins/files](/influxdb3/core/api/v3/#operation/PutPluginFile)

Include the following in your request:

- **Headers**:
  - `Authorization: Bearer` with your admin token
  - `Content-Type: application/octet-stream`
- **Query parameters**:
  - `path` *(string, required)*: Path to the plugin file relative to the plugin directory

```bash
# Upload a single-file plugin
curl -X PUT "localhost:8181
/api/v3/plugins/files?path=plugin.py" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/octet-stream" \
  --data-binary "@/local/path/to/plugin.py"
```

Replace `AUTH_TOKEN`: your [admin token](/influxdb3/core/admin/tokens/admin)

#### Admin privileges required

Plugin uploads require an admin token. This security measure prevents unauthorized code execution on the server.

**When to use plugin upload:**

- Local plugin development and testing
- Deploying plugins without SSH access to the server
- Rapid iteration on plugin code
- Automating plugin deployment in CI/CD pipelines

### Update existing plugins

Modify plugin code for running triggers without recreating them. This allows you to iterate on plugin development while preserving trigger configuration and history.

- [Update a plugin using the influxdb3 CLI](#update-a-plugin-using-the-influxdb3-cli)
- [Update a plugin using the HTTP API](#update-a-plugin-using-the-http-api)

#### Update a plugin using the influxdb3 CLI

Use the `influxdb3 update trigger` command:

```bash
# Update single-file plugin
influxdb3 update trigger \
  --database metrics \
  --trigger-name my_trigger \
  --path "/path/to/updated/plugin.py"

# Update multifile plugin
influxdb3 update trigger \
  --database metrics \
  --trigger-name complex_trigger \
  --path "/path/to/updated/plugin-dir"
```

For complete reference, see [`influxdb3 update trigger`](/influxdb3/core/reference/cli/influxdb3/update/trigger/).

#### Update a plugin using the HTTP API

To update a plugin file using the HTTP API, send a `PUT` request to the `/api/v3/plugins/files` endpoint:

[PUT localhost:8181/api/v3/plugins/files](/influxdb3/core/api/v3/#operation/PutPluginFile)

Include the following in your request:

- **Headers**:
  - `Authorization: Bearer` with your admin token
  - `Content-Type: application/octet-stream`
- **Query parameters**:
  - `path` *(string, required)*: Path to the plugin file relative to the plugin directory

```bash
# Update a plugin file
curl -X PUT "localhost:8181
/api/v3/plugins/files?path=plugin.py" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/octet-stream" \
  --data-binary "@/path/to/updated/plugin.py"
```

Replace `AUTH_TOKEN`: your [admin token](/influxdb3/core/admin/tokens/admin)

**The update operation:**

- Replaces plugin files immediately
- Preserves trigger configuration (spec, schedule, arguments)
- Requires admin token for security
- Works with both local paths and uploaded files

### View loaded plugins

Monitor which plugins are loaded in your system for operational visibility and troubleshooting.

**Option 1: Use the CLI command**

```bash
# List all plugins
influxdb3 show plugins --token $ADMIN_TOKEN

# JSON format for programmatic access
influxdb3 show plugins --format json --token $ADMIN_TOKEN
```

**Option 2: Query the system table**

The `system.plugin_files` table in the `_internal` database provides detailed plugin file information:

```bash
influxdb3 query \
  -d _internal \
  "SELECT * FROM system.plugin_files ORDER BY plugin_name" \
  --token $ADMIN_TOKEN
```

**Available columns:**

- `plugin_name` (String): Trigger name
- `file_name` (String): Plugin file name
- `file_path` (String): Full server path
- `size_bytes` (Int64): File size
- `last_modified` (Int64): Modification timestamp (milliseconds)

**Example queries:**

```sql
-- Find plugins by name
SELECT * FROM system.plugin_files WHERE plugin_name = 'my_trigger';

-- Find large plugins
SELECT plugin_name, size_bytes
FROM system.plugin_files
WHERE size_bytes > 10000;

-- Check modification times
SELECT plugin_name, file_name, last_modified
FROM system.plugin_files
ORDER BY last_modified DESC;
```

For more information, see the [`influxdb3 show plugins` reference](/influxdb3/core/reference/cli/influxdb3/show/plugins/) and [Query system data](/influxdb3/core/admin/query-system-data/#query-plugin-files).

## Create a trigger

A trigger connects your plugin code to database events. When the specified event occurs, the processing engine executes your plugin.

- [Understand trigger types](#understand-trigger-types)
- [Create a trigger using the influxdb3 CLI](#create-a-trigger-using-the-influxdb3-cli)
- [Create a trigger using the HTTP API](#create-a-trigger-using-the-http-api)
- [Trigger specification examples](#trigger-specification-examples)

### Understand trigger types

| Plugin Type | Trigger Specification | When Plugin Runs |
| --- | --- | --- |
| Data write | table:<TABLE_NAME> or all_tables | When data is written to tables |
| Scheduled | every:<DURATION> or cron:<EXPRESSION> | At specified time intervals |
| HTTP request | request:<REQUEST_PATH> | When HTTP requests are received |

### Create a trigger using the influxdb3 CLI

Use the `influxdb3 create trigger` command with the appropriate trigger specification:

```bash
influxdb3 create trigger \
  --trigger-spec SPECIFICATION \
  --path PLUGIN_FILE \
  --database DATABASE_NAME \
  TRIGGER_NAME
```

In the example above, replace the following:

- `SPECIFICATION`: Trigger specification
- `PLUGIN_FILE`: Plugin filename relative to your configured plugin directory
- `DATABASE_NAME`: Name of the database
- `TRIGGER_NAME`: Name of the new trigger

#### Plugin paths

- For **single-file plugins**, provide just the `.py` filename to `--path` (for example, `test_plugin.py`).
- For **multi-file plugins**, provide the directory name containing `__init__.py`.

When not using `--upload`, the server resolves paths relative to the configured `--plugin-dir`. For details about multi-file plugin structure, see [Create your plugin file](#create-your-plugin-file).

For complete reference, see [`influxdb3 create trigger`](/influxdb3/core/reference/cli/influxdb3/create/trigger/).

### Create a trigger using the HTTP API

To create a trigger using the HTTP API, send a `POST` request to the `/api/v3/configure/processing_engine_trigger` endpoint:

[POST localhost:8181/api/v3/configure/processing\_engine\_trigger](/influxdb3/core/api/v3/#operation/PostConfigureProcessingEngineTrigger)

Include the following in your request:

- **Headers**:
  - `Authorization: Bearer` with your authentication token
  - `Content-Type: application/json`
- **Request body**: JSON object with trigger configuration
  - `db` *(string, required)*: Database name
  - `trigger_name` *(string, required)*: Trigger name
  - `plugin_filename` *(string, required)*: Plugin filename relative to the plugin directory
  - `trigger_specification` *(string, required)*: When the plugin runs (see [trigger types](#understand-trigger-types))
  - `trigger_settings` *(object, required)*: Configuration for error handling and execution
        - `run_async` *(boolean)*: Whether to run asynchronously (default: `false`)
        - `error_behavior` *(string)*: How to handle errors: `Log`, `Retry`, or `Disable` (default: `Log`)
  - `disabled` *(boolean, required)*: Whether the trigger is disabled
  - `trigger_arguments` *(object, optional)*: Arguments passed to the plugin

```bash
# Create a basic trigger
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "TRIGGER_NAME",
    "plugin_filename": "PLUGIN_FILE",
    "trigger_specification": "TRIGGER_SPEC",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Log"
    },
    "disabled": false
  }'
```

In the example above, replace the following:

- `DATABASE_NAME`: Name of the database
- `TRIGGER_NAME`: Name of the new trigger
- `PLUGIN_FILE`: Plugin filename relative to your configured plugin directory
- `TRIGGER_SPEC`: Trigger specification (see [examples](#trigger-specification-examples))
- `AUTH_TOKEN`: your [token](/influxdb3/core/admin/tokens/)

### Trigger specification examples

The following examples demonstrate how to create triggers for different event types.

#### Trigger on data writes

<!-- Tabbed content: Select one of the following options -->

**influxdb3 CLI:**

```bash
# Trigger on writes to a specific table
# The plugin file must be in your configured plugin directory
influxdb3 create trigger \
  --trigger-spec "table:sensor_data" \
  --path "process_sensors.py" \
  --database my_database \
  sensor_processor

# Trigger on writes to all tables
influxdb3 create trigger \
  --trigger-spec "all_tables" \
  --path "process_all_data.py" \
  --database my_database \
  all_data_processor
```

**HTTP API:**

```bash
# Trigger on writes to a specific table (2)
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "sensor_processor",
    "plugin_filename": "process_sensors.py",
    "trigger_specification": "table:sensor_data",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Log"
    },
    "disabled": false
  }'

# Trigger on writes to all tables (2)
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "all_data_processor",
    "plugin_filename": "process_all_data.py",
    "trigger_specification": "all_tables",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Log"
    },
    "disabled": false
  }'
```

Replace the following:

- `DATABASE_NAME`: the name of the database
- `AUTH_TOKEN`: your [token](/influxdb3/core/admin/tokens/)

<!-- End tabbed content -->

The trigger runs when the database flushes ingested data for the specified tables to the Write-Ahead Log (WAL) in the Object store (default is every second).

The plugin receives the written data and table information.

#### Trigger on data writes with table exclusion

If you want to use a single trigger for all tables but exclude specific tables, you can use trigger arguments and your plugin code to filter out unwanted tables–for example:

```bash
influxdb3 create trigger \
  --database DATABASE_NAME \
  --token AUTH_TOKEN \
  --path processor.py \
  --trigger-spec "all_tables" \
  --trigger-arguments "exclude_tables=temp_data,debug_info,system_logs" \
  data_processor
```

Replace the following:

- DATABASE\_NAME: the name of the database
- AUTH\_TOKEN: your [token](/influxdb3/core/admin/tokens/)

Then, in your plugin:

```python
# processor.py
def on_write(self, database, table_name, batch):
    # Get excluded tables from trigger arguments
    excluded_tables = set(self.args.get('exclude_tables', '').split(','))

    if table_name in excluded_tables:
        return

    # Process allowed tables
    self.process_data(database, table_name, batch)
```

##### Recommendations

- **Early return**: Check exclusions as early as possible in your plugin.
- **Efficient lookups**: Use sets for O(1) lookup performance with large exclusion lists.
- **Performance**: Log skipped tables for debugging but avoid excessive logging in production.
- **Multiple triggers**: For few tables, consider creating separate table-specific triggers instead of filtering within plugin code. See HTTP API [Processing engine endpoints](/influxdb3/core/api/v3/#tag/Processing-engine) for managing triggers.

#### Trigger on a schedule

<!-- Tabbed content: Select one of the following options -->

**influxdb3 CLI:**

```bash
# Run every 5 minutes
influxdb3 create trigger \
  --trigger-spec "every:5m" \
  --path "periodic_check.py" \
  --database my_database \
  regular_check

# Run on a cron schedule (8am daily)
# Supports extended cron format with seconds
influxdb3 create trigger \
  --trigger-spec "cron:0 0 8 * * *" \
  --path "daily_report.py" \
  --database my_database \
  daily_report
```

**HTTP API:**

```bash
# Run every 5 minutes (2)
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "regular_check",
    "plugin_filename": "periodic_check.py",
    "trigger_specification": "every:5m",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Log"
    },
    "disabled": false
  }'

# Run on a cron schedule (8am daily) (2)
# Supports extended cron format with seconds (2)
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "daily_report",
    "plugin_filename": "daily_report.py",
    "trigger_specification": "cron:0 0 8 * * *",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Log"
    },
    "disabled": false
  }'
```

Replace the following:

- `DATABASE_NAME`: the name of the database
- `AUTH_TOKEN`: your [token](/influxdb3/core/admin/tokens/)

<!-- End tabbed content -->

The plugin receives the scheduled call time.

#### Trigger on HTTP requests

<!-- Tabbed content: Select one of the following options -->

**influxdb3 CLI:**

```bash
# Create an endpoint at /api/v3/engine/webhook
influxdb3 create trigger \
  --trigger-spec "request:webhook" \
  --path "webhook_handler.py" \
  --database my_database \
  webhook_processor
```

**HTTP API:**

```bash
# Create an endpoint at /api/v3/engine/webhook (2)
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "webhook_processor",
    "plugin_filename": "webhook_handler.py",
    "trigger_specification": "request:webhook",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Log"
    },
    "disabled": false
  }'
```

Replace the following:

- `DATABASE_NAME`: the name of the database
- `AUTH_TOKEN`: your [token](/influxdb3/core/admin/tokens/)

<!-- End tabbed content -->

Access your endpoint at `/api/v3/engine/{REQUEST_PATH}` (in this example, `/api/v3/engine/webhook`). The trigger is enabled by default and runs when an HTTP request is received at the specified path.

To run the plugin, send a `GET` or `POST` request to the endpoint–for example:

```bash
curl http://localhost:8181
/api/v3/engine/webhook
```

The plugin receives the HTTP request object with methods, headers, and body.

To view triggers associated with a database, use the `influxdb3 show summary` command:

```bash
influxdb3 show summary --database my_database --token AUTH_TOKEN
```

### Pass arguments to plugins

Use trigger arguments to pass configuration from a trigger to the plugin it runs. You can use this for:

- Threshold values for monitoring
- Connection properties for external services
- Configuration settings for plugin behavior

<!-- Tabbed content: Select one of the following options -->

**influxdb3 CLI:**

```bash
influxdb3 create trigger \
  --trigger-spec "every:1h" \
  --path "threshold_check.py" \
  --trigger-arguments threshold=90,notify_email=admin@example.com \
  --database my_database \
  threshold_monitor
```

**HTTP API:**

```bash
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "threshold_monitor",
    "plugin_filename": "threshold_check.py",
    "trigger_specification": "every:1h",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Log"
    },
    "trigger_arguments": {
      "threshold": "90",
      "notify_email": "admin@example.com"
    },
    "disabled": false
  }'
```

Replace the following:

- `DATABASE_NAME`: the name of the database
- `AUTH_TOKEN`: your [token](/influxdb3/core/admin/tokens/)

<!-- End tabbed content -->

The arguments are passed to the plugin as a `Dict[str, str]` where the key is the argument name and the value is the argument value:

```python
def process_scheduled_call(influxdb3_local, call_time, args=None):
    if args and "threshold" in args:
        threshold = float(args["threshold"])
        email = args.get("notify_email", "default@example.com")
        
        # Use the arguments in your logic
        influxdb3_local.info(f"Checking threshold {threshold}, will notify {email}")
```

### Control trigger execution

By default, triggers run synchronously—each instance waits for previous instances to complete before executing.

To allow multiple instances of the same trigger to run simultaneously, configure triggers to run asynchronously:

<!-- Tabbed content: Select one of the following options -->

**influxdb3 CLI:**

```bash
# Allow multiple trigger instances to run simultaneously
influxdb3 create trigger \
  --trigger-spec "table:metrics" \
  --path "heavy_process.py" \
  --run-asynchronous \
  --database my_database \
  async_processor
```

**HTTP API:**

```bash
# Allow multiple trigger instances to run simultaneously (2)
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "async_processor",
    "plugin_filename": "heavy_process.py",
    "trigger_specification": "table:metrics",
    "trigger_settings": {
      "run_async": true,
      "error_behavior": "Log"
    },
    "disabled": false
  }'
```

Replace the following:

- `DATABASE_NAME`: the name of the database
- `AUTH_TOKEN`: your [token](/influxdb3/core/admin/tokens/)

<!-- End tabbed content -->

### Configure error handling for a trigger

To configure error handling behavior for a trigger, specify one of the following values:

- `log` (default): Log all plugin errors to stdout and the `system.processing_engine_logs` table in the trigger’s database.
- `retry`: Attempt to run the plugin again immediately after an error.
- `disable`: Automatically disable the plugin when an error occurs (can be re-enabled later).

<!-- Tabbed content: Select one of the following options -->

**influxdb3 CLI:**

For more information, see how to [Query trigger logs](/influxdb3/core/admin/query-system-data/#query-trigger-logs).

```bash
# Automatically retry on error
influxdb3 create trigger \
  --trigger-spec "table:important_data" \
  --path "critical_process.py" \
  --error-behavior retry \
  --database my_database \
  critical_processor

# Disable the trigger on error
influxdb3 create trigger \
  --trigger-spec "request:webhook" \
  --path "webhook_handler.py" \
  --error-behavior disable \
  --database my_database \
  auto_disable_processor
```

**HTTP API:**

```bash
# Automatically retry on error (2)
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "critical_processor",
    "plugin_filename": "critical_process.py",
    "trigger_specification": "table:important_data",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Retry"
    },
    "disabled": false
  }'

# Disable the trigger on error (2)
curl -X POST "localhost:8181
/api/v3/configure/processing_engine_trigger" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "db": "DATABASE_NAME",
    "trigger_name": "auto_disable_processor",
    "plugin_filename": "webhook_handler.py",
    "trigger_specification": "request:webhook",
    "trigger_settings": {
      "run_async": false,
      "error_behavior": "Disable"
    },
    "disabled": false
  }'
```

Replace the following:

- `DATABASE_NAME`: the name of the database
- `AUTH_TOKEN`: your [token](/influxdb3/core/admin/tokens/)

<!-- End tabbed content -->

## Manage plugin dependencies

Use the `influxdb3 install package` command to add third-party libraries (like `pandas`, `requests`, or `influxdb3-python`) to your plugin environment.  
This installs packages into the Processing Engine’s embedded Python environment to ensure compatibility with your InfluxDB instance.

<!-- Tabbed content: Select one of the following options -->

**influxdb3 CLI:**

```bash
# Use the CLI to install a Python package
influxdb3 install package pandas
```

**Docker:**

```bash
# Use the CLI to install a Python package in a Docker container
docker exec -it CONTAINER_NAME influxdb3 install package pandas
```

**HTTP API:**

```bash
# Use the HTTP API to install Python packages
curl -X POST "localhost:8181
/api/v3/configure/plugin_environment/install_packages" \
  --header "Authorization: Bearer AUTH_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "packages": ["pandas", "requests", "numpy"]
  }'
```

Replace `AUTH_TOKEN`: your [admin token](/influxdb3/core/admin/tokens/admin)

For complete reference, see [Install plugin packages](/influxdb3/core/api/v3/#operation/PostInstallPluginPackages).

<!-- End tabbed content -->

These examples install the specified Python packages (for example, pandas) into the Processing Engine’s embedded virtual environment.

- Use the CLI command when running InfluxDB directly on your system.
- Use the Docker variant if you’re running InfluxDB in a containerized environment.
- Use the HTTP API for programmatic package installation or CI/CD workflows.

### Use bundled Python for plugins

When you start the server with the `--plugin-dir` option, InfluxDB 3 creates a Python virtual environment (`<PLUGIN_DIR>/venv`) for your plugins. If you need to create a custom virtual environment, use the Python interpreter bundled with InfluxDB 3. Don’t use the system Python. Creating a virtual environment with the system Python (for example, using `python -m venv`) can lead to runtime errors and plugin failures.

For more information, see the [processing engine README](https://github.com/influxdata/influxdb/blob/main/README_processing_engine.md).

InfluxDB creates a Python virtual environment in your plugins directory with the specified packages installed.

### Disable package installation for secure environments

For air-gapped deployments or environments with strict security requirements, you can disable Python package installation while maintaining Processing Engine functionality.

Start the server with `--package-manager disabled`:

```bash
influxdb3 serve \
  --node-id node0 \
  --object-store file \
  --data-dir ~/.influxdb3 \
  --plugin-dir ~/.plugins \
  --package-manager disabled
```

When package installation is disabled:

- The Processing Engine continues to function normally for triggers
- Plugin code executes without restrictions
- Package installation commands are blocked
- Pre-installed dependencies in the virtual environment remain available

**Pre-install required dependencies:**

Before disabling the package manager, install all required Python packages:

```bash
# Install packages first
influxdb3 install package pandas requests numpy

# Then start with disabled package manager
influxdb3 serve \
  --plugin-dir ~/.plugins \
  --package-manager disabled
```

**Use cases for disabled package management:**

- Air-gapped environments without internet access
- Compliance requirements prohibiting runtime package installation
- Centrally managed dependency environments
- Security policies requiring pre-approved packages only

For more configuration options, see [–package-manager](/influxdb3/core/reference/config-options/#package-manager).

## Plugin security

The Processing Engine includes security features to protect your InfluxDB 3 Core instance from unauthorized code execution and file system attacks.

### Plugin path validation

All plugin file paths are validated to prevent directory traversal attacks. The system blocks:

- **Relative paths with parent directory references** (`../`, `../../`)
- **Absolute paths** (`/etc/passwd`, `/usr/bin/script.py`)
- **Symlinks that escape the plugin directory**

When creating or updating triggers, plugin paths must resolve within the configured `--plugin-dir`.

**Example of blocked paths:**

```bash
# These will be rejected
influxdb3 create trigger \
  --path "../../../etc/passwd" \  # Blocked: parent directory traversal
  ...

influxdb3 create trigger \
  --path "/tmp/malicious.py" \    # Blocked: absolute path
  ...
```

**Valid plugin paths:**

```bash
# These are allowed
influxdb3 create trigger \
  --path "myapp/plugin.py" \      # Relative to plugin-dir
  ...

influxdb3 create trigger \
  --path "transforms/data.py" \    # Subdirectory in plugin-dir
  ...
```

### Upload and update permissions

Plugin upload and update operations require admin tokens to prevent unauthorized code deployment:

- `--upload` flag requires admin privileges
- `update trigger` command requires admin token
- Standard resource tokens cannot upload or modify plugin code

This security model ensures only administrators can introduce or modify executable code in your database.

### Best practices

**For development:**

- Use the `--upload` flag to deploy plugins during development
- Test plugins in non-production environments first
- Review plugin code before deployment

**For production:**

- Pre-deploy plugins to the server’s plugin directory via secure file transfer
- Use custom plugin repositories for vetted, approved plugins
- Disable package installation (`--package-manager disabled`) in locked-down environments
- Audit plugin files using the [`system.plugin_files` table](#view-loaded-plugins)
- Implement change control processes for plugin updates

For more security configuration options, see [Configuration options](/influxdb3/core/reference/config-options/).

#### Related (3)

- [influxdb3 test wal\_plugin](/influxdb3/core/reference/cli/influxdb3/test/wal_plugin/)
- [influxdb3 create trigger](/influxdb3/core/reference/cli/influxdb3/create/trigger/)

[processing engine](/influxdb3/core/tags/processing-engine/) [python](/influxdb3/core/tags/python/)

---

## Configure object storage

InfluxDB 3 Core can be configured to use different object storage providers to store time series data in Parquet format. The process of configuring and connecting to different object storage providers varies. The following guides walk through configuring, connecting to, and using different object storage providers as your InfluxDB 3 Core object store.

### [MinIO](/influxdb3/core/object-storage/minio/)

Use [MinIO](min.io) as the object store for your InfluxDB 3 Core instance. InfluxDB uses the MinIO S3-compatible API to interact with your MinIO server or cluster.

#### Related (4)

- [InfluxDB 3 Core configuration options](/influxdb3/core/reference/config-options/)

[object storage](/influxdb3/core/tags/object-storage/) [S3](/influxdb3/core/tags/s3/)

---

## Install InfluxDB 3 Core

### Upgrade to InfluxDB 3 Enterprise

If you want to upgrade from InfluxDB 3 Core to InfluxDB 3 Enterprise for features like high availability, read replicas, and historical query capability, see [Upgrade to Enterprise](/influxdb3/core/admin/upgrade-to-enterprise/).

- [System Requirements](#system-requirements)
- [Install](#install)
  - [Quick install for Linux and macOS](#quick-install-for-linux-and-macos)
  - [Download and install the latest build artifacts](#download-and-install-the-latest-build-artifacts)
  - [Pull the Docker image](#pull-the-docker-image)
  - [Linux DEB or RPM](#linux-deb-or-rpm)
        - [TOML configuration (Linux)](#toml-configuration-linux)
        - [Run as a system service (Linux)](#run-as-a-system-service-linux)
  - [Verify the installation](#verify-the-installation)

## System Requirements

### Operating system

InfluxDB 3 Core runs on **Linux**, **macOS**, and **Windows**.

#### Object storage

A key feature of InfluxDB 3 is its use of object storage to store time series data in Apache Parquet format. You can choose to store these files on your local file system. Performance on your local filesystem will likely be better, but object storage has the advantage of not running out of space and being accessible by other systems over the network. InfluxDB 3 Core natively supports Amazon S3, Azure Blob Storage, and Google Cloud Storage. You can also use many local object storage implementations that provide an S3-compatible API, such as [Minio](https://min.io/).

## Install

InfluxDB 3 Core runs on **Linux**, **macOS**, and **Windows**.

Choose one of the following methods to install InfluxDB 3 Core:

- [Quick install for Linux and macOS](#quick-install-for-linux-and-macos)
- [Download and install the latest build artifacts](#download-and-install-the-latest-build-artifacts)
- [Pull the Docker image](#pull-the-docker-image)
- [Linux DEB or RPM](#linux-deb-or-rpm)

### Quick install for Linux and macOS

To install InfluxDB 3 Core on **Linux** or **macOS**, download and run the quick installer script for InfluxDB 3 Core–for example, using [`curl`](https://curl.se/) to download the script:

```bash
curl -O https://www.influxdata.com/d/install_influxdb3.sh \
&& sh install_influxdb3.sh 
```

The quick installer script is updated with each InfluxDB 3 Core release, so it always installs the latest version.

#### Production deployment

For production deployments, use [Linux DEB or RPM](#linux-deb-or-rpm) for built-in systemd sandboxing, or [Docker](#pull-the-docker-image) with your own container security configuration.

For detailed security options, see [Manage security](/influxdb3/core/admin/security/).

### Download and install the latest build artifacts

You can also download and install [InfluxDB 3 Core build artifacts](/influxdb3/core/install/#download-influxdb-3-core-binaries) directly:

[](#linux-binaries)

Linux binaries

- [Linux | AMD64 (x86\_64) | GNU](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.8.3_linux_amd64.tar.gz) • [sha256](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.8.3_linux_amd64.tar.gz.sha256)
- [Linux | ARM64 (AArch64) | GNU](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.8.3_linux_arm64.tar.gz) • [sha256](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.8.3_linux_arm64.tar.gz.sha256)

[](#macos-binaries)

macOS binaries

- [macOS | Silicon (ARM64)](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.8.3_darwin_arm64.tar.gz) • [sha256](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.8.3_darwin_arm64.tar.gz.sha256)

macOS Intel builds are coming soon.

[](#windows-binaries)

Windows binaries

- [Windows (AMD64, x86\_64) binary](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.8.3-windows_amd64.zip) • [sha256](https://dl.influxdata.com/influxdb/releases/influxdb3-core-3.8.3-windows_amd64.zip.sha256)

### Pull the Docker image

Run the following command to pull the [`influxdb:3-core` image](https://hub.docker.com/_/influxdb/tags?tag=3-core&name=3-core), available for x86\_64 (AMD64) and ARM64 architectures:

```bash
docker pull influxdb:3-core
```

Docker automatically pulls the appropriate image for your system architecture.

[](#pull-for-a-specific-system-architecture)

Pull for a specific system architecture

To specify the system architecture, use platform-specific tags–for example:

```bash
# For x86_64/AMD64
docker pull \
--platform linux/amd64 \
influxdb:3-core
```

```bash
# For ARM64
docker pull \
--platform linux/arm64 \
influxdb:3-core
```

### Linux DEB or RPM

When installed via DEB or RPM on a `systemd`\-enabled system, InfluxDB 3 Core runs in a sandboxed environment. The included `systemd` unit file configures the environment to provide security isolation for typical deployments. For more information, see [Manage security](/influxdb3/core/admin/security/).

DEB and RPM installation is **recommended for non-Docker production deployments** due to built-in `systemd` sandboxing.

[](#deb-based-systems)

DEB-based systems

Use `apt-get` to install InfluxDB 3 Core from the InfluxData repository:

```bash
curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key
gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive.key 2>&1 \
| grep -q '^fpr:\+24C975CBA61A024EE1B631787C3D57159FC2F927:$' \
&& cat influxdata-archive.key \
| gpg --dearmor \
| sudo tee /usr/share/keyrings/influxdata-archive.gpg > /dev/null \
&& echo 'deb [signed-by=/usr/share/keyrings/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main' \
| sudo tee /etc/apt/sources.list.d/influxdata.list
sudo apt-get update && sudo apt-get install influxdb3-core
```

[](#rpm-based-systems)

RPM-based systems

Use `yum` to install InfluxDB 3 Core from the InfluxData repository:

```bash
curl --silent --location -O https://repos.influxdata.com/influxdata-archive.key
test -d /usr/share/influxdata-archive-keyring/keyrings || sudo mkdir -p /usr/share/influxdata-archive-keyring/keyrings
gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive.key 2>&1 \
| grep -q '^fpr:\+24C975CBA61A024EE1B631787C3D57159FC2F927:$' \
&& sudo cp ./influxdata-archive.key /usr/share/influxdata-archive-keyring/keyrings/influxdata-archive.asc \
&& cat <<EOF | sudo tee /etc/yum.repos.d/influxdata.repo
[influxdata]
name = InfluxData Repository - Stable
baseurl = https://repos.influxdata.com/stable/\$basearch/main
enabled = 1
gpgcheck = 1
gpgkey = file:///usr/share/influxdata-archive-keyring/keyrings/influxdata-archive.asc
EOF
sudo yum install influxdb3-core
```

#### TOML configuration (Linux)

After you install the DEB or RPM package, the InfluxDB 3 Core TOML configuration file is located at `/etc/influxdb3/influxdb3-core.conf` and contains the following settings:

- [object-store](/influxdb3/core/reference/config-options/#object-store): `file`
- [data-dir](/influxdb3/core/reference/config-options/#data-dir): `/var/lib/influxdb3/data`
- [plugin-dir](/influxdb3/core/reference/config-options/#plugin-dir): `/var/lib/influxdb3/plugins`
- [node-id](/influxdb3/core/reference/config-options/#node-id): `primary-node`

#### Run as a system service (Linux)

InfluxDB 3 Core DEB and RPM installs include service files for running as a managed system service on Linux:

- **systemd**: For modern Linux distributions
- **SysV init**: For legacy system compatibility

##### Run using systemd

On `systemd` systems, the `influxdb3-core` unit file is `enabled` on install, but the unit is not started in order to allow configuration.

To start the database, enter the following commands:

```bash
# Start the service
systemctl start influxdb3-core

# View status
systemctl status influxdb3-core

# View logs
journalctl --unit influxdb3-core
```

##### Run using SysV

On SysV init systems, `influxdb3-core` is disabled on install and can be enabled by adjusting `/etc/default/influxdb3-core` to contain `ENABLED=yes`.

To start the database, enter the following commands:

```bash
# Start the database
/etc/init.d/influxdb3-core start

# View status (2)
/etc/init.d/influxdb3-core status

# View logs (2)
tail -f /var/lib/influxdb3/influxdb3-core.log
```

### Verify the installation

After installing InfluxDB 3 Core, enter the following command to verify that it installed successfully:

```bash
influxdb3 --version
```

If your system can’t locate `influxdb3` following a [quick install](#quick-install-for-linux-and-macos), `source` the configuration file (for example, `.bashrc`, `.zshrc`) for your shell–for example:

```zsh
source ~/.zshrc
```

[Get started with InfluxDB 3 Core](/influxdb3/core/get-started/)

#### Related (5)

- [Upgrade InfluxDB 3 Core](/influxdb3/core/admin/upgrade/)

[install](/influxdb3/core/tags/install/)

---

## Get started with InfluxDB 3 Core

InfluxDB 3 Core is purpose-built for real-time data monitoring and recent data. InfluxDB 3 Enterprise builds on top of Core with support for historical data analysis and extended features. querying, high availability, read replicas, and more. Enterprise will soon unlock enhanced security, row-level deletions, an administration UI, and more. Learn more about [InfluxDB 3 Enterprise](/influxdb3/enterprise/).

This guide walks through the basic steps of getting started with InfluxDB 3 Core, including the following:

1. [Set up InfluxDB 3 Core](/influxdb3/core/get-started/setup/)
2. [Write data to InfluxDB 3 Core](/influxdb3/core/get-started/write/)
3. [Query data in InfluxDB 3 Core](/influxdb3/core/get-started/query/)
4. [Process data in InfluxDB 3 Core](/influxdb3/core/get-started/process/)

### Find support for InfluxDB 3 Core

The [InfluxDB Discord server](https://discord.gg/9zaNCW2PRT) is the best place to find support for InfluxDB 3 Core and InfluxDB 3 Enterprise. For other InfluxDB versions, see the [Support and feedback](#bug-reports-and-feedback) options.

## Data model

The InfluxDB 3 Core server contains logical databases; databases contain tables; and tables are comprised of columns.

Compared to previous versions of InfluxDB, you can think of a database as an InfluxDB v2 `bucket` in v2 or an InfluxDB v1 `db/retention_policy`. A `table` is equivalent to an InfluxDB v1 and v2 `measurement`.

Columns in a table represent time, tags, and fields. Columns can be one of the following types:

- String dictionary (tag)
- `int64` (field)
- `float64` (field)
- `uint64` (field)
- `bool` (field)
- `string` (field)
- `time` (time with nanosecond precision)

In InfluxDB 3 Core, every table has a primary key–the ordered set of tags and the time–for its data. The primary key uniquely identifies each and determines the sort order for all Parquet files related to the table. When you create a table, either through an explicit call or by writing data into a table for the first time, it sets the primary key to the tags in the order they arrived. Although InfluxDB is still a *schema-on-write* database, the tag column definitions for a table are immutable.

Tags should hold unique identifying information like `sensor_id`, `building_id`, or `trace_id`. All other data should be stored as fields.

## Tools to use

The following table compares tools that you can use to interact with InfluxDB 3 Core. This tutorial covers many of the recommended tools.

| Tool | Administration | Write | Query |
| --- | --- | --- | --- |
| influxdb3 CLI |  |  |  |
| InfluxDB HTTP API |  |  |  |
| InfluxDB 3 Explorer |  |  |  |
| InfluxDB 3 client libraries | - |  |  |
| InfluxDB v2 client libraries | - |  | - |
| InfluxDB v1 client libraries | - |  |  |
| InfluxDB 3 processing engine |  |  |  |
| Telegraf | - |  | - |
| Chronograf | - | - | - |
| influx CLI | - | - | - |
| influxctl CLI | - | - | - |
| InfluxDB v2.x user interface | - | - | - |
| Third-party tools |  |  |  |
| Flight SQL clients | - | - |  |
| Grafana | - | - |  |

[Set up InfluxDB 3 Core](/influxdb3/core/get-started/setup/)

### Related topics

- [Query system data](/influxdb3/core/admin/query-system-data/)
- [Write data to InfluxDB 3 Core](/influxdb3/core/write-data/)
- [Query data in InfluxDB 3 Core](/influxdb3/core/query-data/)

---

## Administer InfluxDB 3 Core

The following articles provide information about managing your InfluxDB 3 Core resources:

### [Identify InfluxDB 3 Core version](/influxdb3/core/admin/identify-version/)

Learn how to identify your InfluxDB 3 Core version using command-line tools, HTTP endpoints, and other methods.

### [Manage databases](/influxdb3/core/admin/databases/)

An InfluxDB 3 Core database is a named location where time series data is stored. Each database can contain multiple tables.

### [Manage tables](/influxdb3/core/admin/tables/)

Tables in InfluxDB 3 Core are synonymous with measurements and contain time series data. Each table has a defined schema with tag and field columns.

### [Manage tokens](/influxdb3/core/admin/tokens/)

Manage tokens to authenticate and authorize access to server actions, resources, and data in an InfluxDB 3 Core instance.

### [Manage the Last Value Cache](/influxdb3/core/admin/last-value-cache/)

The InfluxDB 3 Core Last Value Cache (LVC) lets you cache the most recent values for specific fields in a table, improving the performance of queries that return the most recent value of a field for specific time series or the last N values of a field.

### [Manage the Distinct Value Cache](/influxdb3/core/admin/distinct-value-cache/)

The InfluxDB 3 Core Distinct Value Cache (DVC) lets you cache distinct values of one or more columns in a table, improving the performance of queries that return distinct tag and field values.

### [Query system data](/influxdb3/core/admin/query-system-data/)

Query system tables to see data related to the server, queries, and tables in an InfluxDB 3 Core instance. Use the HTTP SQL query API to retrieve information about your database server and table schemas.

### [Back up and restore data](/influxdb3/core/admin/backup-restore/)

Back up and restore your InfluxDB 3 Core instance by copying object storage files in the recommended order.

### [Performance tuning](/influxdb3/core/admin/performance-tuning/)

Optimize InfluxDB 3 Core performance by tuning thread allocation, memory settings, and other configuration options for your specific workload.

### [Security](/influxdb3/core/admin/security/)

Tune InfluxDB 3 Core security for local requirements.

### [Upgrade InfluxDB 3 Core](/influxdb3/core/admin/upgrade/)

Learn how to upgrade your InfluxDB 3 Core instance to the latest version.

### [Upgrade to InfluxDB 3 Enterprise](/influxdb3/core/admin/upgrade-to-enterprise/)

Upgrade from InfluxDB 3 Core to InfluxDB 3 Enterprise. Your existing data and plugins are compatible–no data migration is required.

### [Use the InfluxDB 3 MCP server](/influxdb3/core/admin/mcp-server/)

Use the **InfluxDB MCP server** to interact with and manage InfluxDB 3 Core using natural language with LLM agents to query and analyze data, manage databases and more. Query InfluxDB 3 Core documentation from your IDE using the InfluxDB documentation MCP server.