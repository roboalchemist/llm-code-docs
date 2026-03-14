# Source: https://docs.acceldata.io/release/release-notes-440.md

# Version 4.6.0

**Date: 28 July, 2025**

> This section consists of the new features and enhancements introduced in this release.

- **Enhanced Power BI Lineage and Discovery**: ADOC now provides end-to-end, column-level lineage from Power BI to Snowflake, automatically mapped via  DBT models.  Lineage is enriched with detailed dataset metadata, including DAX logic and relationships. Fore more information see, [Lineage](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/lineage).
- **Enhancements to** **Selective Crawling:** ADOC now supports selective crawling for following data sources:

    - Snowflake
    - BigQuery
    - Databricks
    - Azure - Data Lake
    - Azure - Blob
    - GCS
    - AWS - S3

For more information see, [Crawl Data Sources](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/crawl-data-sources).

- **Dataplane V3 – Job Queue Management:** Job Queue Management is now available in Dataplane V3, providing improved control over resource utilization.
- **Centralized Configuration Export/Import:** ADOC now supports exporting and importing asset configurations, making it easier to replicate setups across environments. For more information see, [Export and Import Manager](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/export-and-import-manager).

---

> This section lists the issues that have been resolved in this release.

#### Data Reliability

- Kafka crawlers now handle scenarios where one or more assets contain no data, ensuring that remaining assets continue to be scanned successfully.
- Fixed schema drift score inconsistencies in the UI. 
- Resolved broken Configuration Download button on View Policy page.
- Fixed incremental mode failure in Recon policies. 
- Autosys data sources are now correctly shown only in the relevant ADOC section, resolving an issue where they were incorrectly displayed in the DR asset navigator.
- Fixed duplicate analyzer errors in SQL-based incremental policies.
- Policy API now handles missing ITEMS payload correctly. 
- Auto anomaly policies now trigger as expected.
- API-based Freshness policy creation stabilized.
- Resolved incorrect display of ENUM values in DQ policies.
- Fixed API casing for consistent asset-level policy retrieval.
- Resolved left and right row count mismatch in Reconciliation policy
- Fixed an issue where incremental fields were not greyed out in persisted columns for Recon policies.
- Fixed column selection issue in segment level configuration.
- Fixed an issue where the ruleset application failed if tagged columns were archived. Data Reliability policies now process archived columns without execution issues.
- Resolved SLA breach row count values displaying inaccurate freshness deltas.
- Fixed an issue where selected columns in anomaly policies were not retained during import.
- Fixed lineage gap between Power BI datasets and Synapse DW assets.

#### Others

- Dataplane upgrade option now available in client environment UI. 
- Snowflake user account locking issue resolved.
- Fixed issues when importing over empty MongoDB collections.
- Fixed Teradata Table names. The table names are now fully visible.
- Resolved issue, the tag and classification name now appear in the data profile view.
- ServiceNow integration now successfully creates tickets.
- Fixed a UI issue where editing DBT Cloud data source configurations showed a blank screen and the Crawl option behaved inconsistently.

---

> This section highlights features or functionalities that are being phased out and will no longer be supported in future releases.

- **Deprecate Composite Policy Option:** The Composite Policy option has been removed from Data Reliability and all other ADOC platforms.

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