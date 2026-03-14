# Source: https://docs.acceldata.io/release/version-4-7-0.md

# Version 4.7.0

**Date: 03 September, 2025**

> This section consists of the new features and enhancements introduced in this release.

### Data Reliability

- **Row-Based Data Quality Scoring**: ADOC now supports row-weighted scoring, enabling data quality scores to reflect the actual number of rows evaluated or affected—rather than relying on a simple average of policy scores. For more information, see [Score Aggregation Methodology](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/score-aggregation-methodology).
- **Incremental Strategies in Reconciliation Policy:** ADOC now supports incremental and selective reconciliation of large or streaming datasets, comparing only the data that changed since the last run. For more information, see [Reconciliation Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/reconciliation-policy#incremental-and-selective-execution).

### Connectors

- **Pub/Sub Connector Integration**: ADOC now supports **Google Cloud Pub/Sub** as a data source (batch reader) for data crawling, profiling, quality checks, and reconciliation. This release also enables **cross-system reconciliation between Pub/Sub and Kafka**, ensuring consistent data reliability across streaming pipelines. For more information, see [Google Cloud Pub/Sub](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/google-cloud-pub-sub).

### UI/UX

**Revamp of Asset Relationship View:** The asset relationship graph has been rebuilt with a modern, responsive design for easier navigation and analysis.

### Storage

**Folder Configuration for AWS S3 Global Storage:** ADOC adds support for dedicated folder paths in S3 global storage for separating good and bad records. For more information, see [Specifying Custom Folder Paths for Good/Bad Records](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/global-storage#specifying-custom-folder-paths-for-goodbad-records).

---

> This section lists the issues that have been resolved in this release.

#### Connectors

- **Snowflake Pushdown (Dataplane Lite):** Fixed profiling failures on very wide tables.
- **Databricks:** Fixed policy creation for pattern match; resolved pushdown profiling failures.
- **ServiceNow:** Fixed token re-authentication on expiry.
- **Teradata:** Fixed lineage for integral columns in SQL views.
- **DBT Cloud:** Fixed missing fetch of failed pipelines.
- **Secret Manager:** Extended support to Oracle, Tableau, and other connectors.
- **NetApp-S3 (Global Storage):** Fixed policies stuck in _Execution Pending_.

#### Data Reliability and Policies

- Fixed scoring and alert behavior in SQL-based rules.
- Fixed inconsistent output in Schema Match rules.
- Fixed disabled rules being scheduled.
- Fixed skipped executions in freshness policies.
- Resolved reconciliation errors by adding microsecond precision in timestamps.
- Fixed email notifications not triggering for incremental reconciliation jobs.

#### Scheduling & Execution

- **Quartz Scheduler:** Resolved lock contention that slowed job performance (high-priority fix).
- Resolved jobs stuck in _Running_ state for long periods.
- Fixed column order mismatches between manual and scheduled job runs.

#### Reporting & UI

- **DR-Reporting:** Fixed missing _Policies_ tab in some repositories.
- **Reliability Reporting:** Fixed missing PowerBI lineage and SQL view creation issues.
- **Asset Settings:** Resolved Asset Settings not displaying features for some tenants.
- **Profile Jobs:** Fixed incorrect sorting (now ascends by asset name).

---

> This section consists of known limitations we are aware of persisting in this release.

- Crawler notifications are not supported for Jira and ServiceNow integrations, as alerts are not generated for crawler events.
- Oracle's TIMESTAMP WITH LOCAL TIMEZONE data type is not supported in Spark and may result in errors such as: org.apache.spark.SparkSQLException: Unrecognized SQL type -102
- Native Incremental Processing Support for Custom SQL Queries Limitations:
    - This feature only supports SQL-based policies. It does **not** apply to alias-based filtering (commonly used in Spark type configurations).
    - The placeholders for bounds must **strictly** be {{{lower_bound}}} and {{{upper_bound}}}. Custom placeholder names are not supported.
    - When using a custom SQL view with **incremental execution**, one additional row may be included due to the inclusive nature of the BETWEEN clause.
    - **Full policy execution** is currently **not supported** for custom SQL queries that use bound placeholders ({{{lower_bound}}}, {{{upper_bound}}}).
    - Values entered for SQL validation during policy creation are **not stored** and are used only for testing the query.
    - In **Selective execution** mode, the bounds defined in the incremental configuration window are passed to the SQL query.
    - Queries using NOT BETWEEN conditions will **not work** with incremental execution. For example:
SELECT * FROM table WHERE date_column NOT BETWEEN {{{lower_bound}}} AND {{{upper_bound}}}
    - This feature is **not compatible** with older Dataplane versions. Customers must upgrade to **Dataplane 4.3.0 or later** to use native incremental SQL queries.

- Within the Freshness Trend chart found in the Data Cadence tab, the upper bound, lower bound, and change in row count metrics are exclusively accessible for time filters such as today, yesterday, and those based on an hourly time frame.
- Anomaly detection is not supported for nested columns of an asset.
- When the refresh token time expires for ServiceNow OAuth Integration, the status remains as configured instead of changing to expired.
- Dataproc is only supported on GCP as the cloud provider for data plane installation.
- Glossary window fails to load data due to Dataproc APIs failure.
- The Smart tag feature is currently available only for Kubernetes-driven Spark deployments.
- When a 2FA credential is activated, the credentials do not work.
- User-specific usage data for a specific day may not be accurately displayed or retrieved.
- Issue with GCP test connections.
- Profiling in BigQuery fails for tables when the partition filter is enabled.
- DQ Policy fails sometimes due to an inability to verify a space column with special characters.
- Unable to pick a reference asset on a Data Policy template when defining a Lookup Rule.
- The data lineage view for job runs is not visible on Databricks' Job Run Details page.
- If all values are null for primitive string and complex data types, profiling will occur, but the data type will be unknown.
- All failed events are not captured in the Audit Logs page.
- When performing Incremental Data Quality (DQ) checks with `Datetime2` and`DateOffset` formats in Synapse, if no new records are added, the system processes the last record instead of skipping processing.