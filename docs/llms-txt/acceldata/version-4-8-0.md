# Source: https://docs.acceldata.io/release/version-4-8-0.md

# Version 4.8.0

**Date: 29 September 2025**

> This section consists of the new features and enhancements introduced in this release.

- **Service User Management V1**: Service accounts replace personal API keys for integrations and system operations. This ensures stable, auditable, and secure credentials that are not tied to individual user lifecycles. For more information, see [Service Users](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/service-users).
- **Profile Metrics for Pushdown Assets**: Profiling in the pushdown engine (Snowflake, BigQuery, Databricks) now achieves parity with Spark. Users gain richer insights such as patterns, arrays, keys, and exact distinct counts, with tenant-level controls for governance.
- **Backward Lineage from Power BI to Redshift**: Backward lineage is now supported for Power BI, providing end-to-end traceability from dashboards to underlying sources. This extends parity with Snowflake, BigQuery, Databricks, and Redshift. For more information see, [Lineage](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/lineage).
- **Custom Notifications V2**: Custom Notifications now integrate with Slack, Teams, Google Chat, Jira, and ServiceNow. Teams can receive alerts directly in their collaboration and ITSM tools alongside existing email and webhook channels. For more information see, [Notification Templates](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/notification-templates).
- **Detailed Column-Level Data Quality Reporting**: Column-level data quality scores are now surfaced in Discover Assets page, enabling deeper visibility into field-level health, faster root cause analysis, and greater trust in data assets. For more information, see [Column-Level Data Quality Reporting](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/asset-details#column-level-data-quality-reporting).
- **Hive Cadence Support**: Hive external tables now support cadence-based updates using native SQL commands, ensuring freshness and freshness policies run against the latest Hive Metastore metrics. For more information see, [Enable Freshness Monitoring](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-freshness#step-1-enable-freshness-monitoring).
- **Kafka Reconciliation Jobs – Start/End Value Support**: Kafka reconciliation and profiling jobs now include start and end offsets/timestamps, aligning with Oracle and other sources for full auditability and traceability.
- **Tenant-Level Configuration for Profile Metrics**: Tenant admins can now set profiling defaults across all assets or new assets only. This ensures consistent governance, optimized performance, and parity across Spark and pushdown engines. For more information see, [Profile Metrics Capabilities](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings#5-profile-metrics-capabilities).

> This section lists the issues that have been resolved in this release.

**Connectors**

- **Oracle → Databricks**: Fixed reconciliation failures on select Oracle tables with `ORA-01858`.
- **Databricks**: Fixed profiling and data quality failures after enabling partition configuration.
- **Databricks pushdown**: Resolved Pattern Match (Regex) rule failures on `TIMESTAMP` columns.
- **SAP → Snowflake**: Fixed row-count reconciliation job failures caused by “Spark Applications Already Exists.”

**Data Quality & Policies**

- Fixed intermittent DQ policy execution errors (`No Request Received in Dataplane`).
- Corrected alerts that were triggered incorrectly for failed reconciliation jobs.
- Fixed import errors for reconciliation policies created from different sources.
- Resolved issue where policies were archived after crawling despite no metadata changes.
- Fixed Schema Drift policy import failures.
- Reconciliation policy exports now capture timezone correctly, preventing schedule mismatches after import.
- Fixed policy errors when column names contained spaces or dots.
- Improved reliability in retrieving asset column metadata for programmatic DQ policy creation using custom SQL.
- **Pushdown parity**: Data Violations tab now displays rows correctly when columns contain NULL values (aligned with Spark behavior).
- Resolved failures migrating data quality policies from Torch to ADOC.

**Scheduling & Execution**

- Fixed DQ scans/jobs that were stuck in **Waiting** state indefinitely.
- Fixed reconciliation jobs stuck in **Running** state after upgrade to 4.6.1.
- **Autosys**: Corrected case-mismatch handling for job names that blocked status pickup.

**Reporting & UI**

- **Navigator**: Fixed over-provisioning of permissions when viewing datasources.
- **Profile Settings Migration**: Notification group selections are now preserved.
- Fixed incremental profiling and sample data views for date-partitioned Parquet files.
- **UI Config**: `KUBERNETES_SPARK_NODE_SELECTOR` settings now apply correctly at pod level.

**Other Fixes**

- Corrected permissions to allow deletion of profiling resources (previously missing cluster role).
- Fixed engine type migration so left/right engine settings carry forward between tenants.
- Resolved policy failures with error: _“Dataplane not running, please contact your administrator.”_