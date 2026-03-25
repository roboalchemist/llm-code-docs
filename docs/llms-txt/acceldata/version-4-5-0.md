# Source: https://docs.acceldata.io/release/version-4-5-0.md

# Version 4.5.0

**Date: 23 June, 2025**

> This section consists of the new features and enhancements introduced in this release.

### Data Reliability

- **SQL Metric Rule Check in Data Quality Policy**: ADOC introduces the SQL Metric Rule Check, allowing users to define numeric validation rules using SQL projections with support for absolute, relative, and anomaly-based checks across Spark and Pushdown data sources. For more information, see [Data Quality Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-quality-policy).
- **Data Freshness Rule in Data Quality Policy**: ADOC introduces the Data Freshness Rule, allowing users to validate date or timestamp columns using either anomaly detection or explicit threshold checks across Spark and Pushdown data sources. For more information, see [Data Quality Policy Rules](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-quality-policy#configure-rules).
- **Pushdown Support for Good/Bad Records in Snowflake**: ADOC now supports exporting good and bad records from policy executions to Snowflake for Pushdown config, enabling secure and flexible handling using external tables, inline queries, and OAuth or Username/Password authentication. For more information, see [Snowflake](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/snowflake-reliability).
- **Introduced Crawler Jobs Execution History Page**: Users can now view a complete history of crawler job executions, including detailed metadata such as the number of databases, tables, views, and columns processed in each run. For more information, see [Crawler Jobs](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/reliability-jobs#types-of-jobs).
- **Improved SLA Breach Labeling in Data Freshness:** Updated labels from **Anomaly Detected/No Anomaly Detected** to **SLA Breached/No SLA Breached** to avoid confusion between SLA breaches and anomaly detection alerts. For more information, see [Data Freshness Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-freshness).
- **Added Support for External S3 Endpoints for Bad Records:** Extended bad record write support beyond AWS S3 to include external S3-compatible endpoints such as NetApp S3. This enables seamless integration for organizations that use NetApp S3 as their primary storage.
- **Improved Atlan Integration for Unified User Experience:** Enhanced the ADOC–Atlan integration by aligning the trust badge label from **Data Reliability Score** to **Overall Reliability** to ensure consistency across both platforms. Also improved UI formatting by matching decimal precision with ADOC, adding a percentage symbol to the score, and displaying the **Last Updated** timestamp in a human-readable format. These updates aim to improve user trust, adoption, and overall platform usability.
- **Custom Notification Templates for Email and Webhook:** ADOC introduces custom notification template groups for email and webhook channels, allowing tailored messages by source type (e.g., Data Reliability Policies, Pipelines). Templates use the new Freemarker engine and include standardized payloads with additional metadata support. For more information, see [Notification Templates](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/notification-templates).

### Pipelines

- **Manual Column-Level Lineage Support**: ADOC now supports manual lineage addition at the column level, allowing users to define upstream and downstream relationships between column-level assets. A new API endpoint enables this functionality, and the UI provides a Lineage tab for column-type assets with asset hierarchy selection down to the column level. For more information, see [Pipelines](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/pipelines).

### UI/UX

- **Accessibility Compliance (WCAG Level A & AA):** ADOC has enhanced accessibility support for the Data Sources Register, Discover Assets, and Asset Details pages by implementing WCAG Level A and AA standards. Improvements include keyboard navigation, alt text for images, consistent navigation, and screen reader compatibility. These updates were validated using Accessibility Insights for Web and Chrome Lighthouse, ensuring a more inclusive experience for all users.

> This section lists the issues that have been resolved in this release.

**Data Reliability**

- Fixed an issue where applying a ruleset failed when a User-Defined Type (UDT) column was added. Also fixed a problem where removing the UDT rule allowed the ruleset to pass, but the UDT was then removed from the Data Quality policy. UDTs are now handled correctly during ruleset edits and application.
- Fixed an issue where Composite Policy results were not being displayed in Alation.
- Fixed an issue where Kafka incremental reconciliation runs always used the initial offset, instead of continuing from the last run’s end value. The system now correctly resumes from the latest snapshot after the first run.
- Resolved an issue where jobs that failed on the data plane remained stuck in a running state on the control plane. This was caused by a 500 error from the catalog service when canceling the job. Job statuses now update correctly to prevent zombie jobs.
- Fixed an issue where Anomaly policies referencing notification channels with the same name across environments were imported successfully but did not appear in the notification channel dropdown.
- Fixed an issue where Kafka data sources did not support scheduled crawling and required manual triggers. Crawling schedules can now be configured and automated for Kafka, like other supported sources.
- Fixed an issue where updates to `additionalPersistedColumns` via API had no effect unless at least one column was added through the UI first. API changes now apply correctly without requiring prior manual edits.
- Resolved an issue where deleting a tag from the middle of a list removed the last tag instead. This only happened with manually entered tags. Tag deletions now work as expected, regardless of position.
- Resolved an issue where a Recon policy was shown as successful but later marked as aborted, without any explanation in the UI or audit logs. The system now provides clearer status messages and logs to help identify the cause of job abortions.
- Resolved an issue where duplicate rules could be added to a Data Quality policy, creating conflicts that blocked updates. The system now prevents duplicate rules and includes better validation and logging to support troubleshooting.
- Resolved an issue where the ThumbsDown feedback message in Anomaly Detection was identical to ThumbsUp. The message now correctly says: _**“Thank you for your feedback that you didn’t find this alert relevant. Please add additional comments to help us improve further.”**_
- Fixed an issue where only 10 profiled assets were shown in the dropdown when assigning assets to Automated Data Reliability pipelines. All profiled assets are now visible and searchable in the selection list.
- Fixed an issue where health data was not showing in Alation despite successful integration and configuration. Health metrics now populate correctly, providing full visibility in Alation.

**UI/UX**

Fixed an issue where non–tenant admin users couldn’t delete reports, even with create and modify permissions. Also fixed a problem where reports couldn’t be added to a resource group after creation if one wasn’t selected initially.

**Common Services**

Resolved an issue where importing rulesets with SQL rules incorrectly changed the Asset Tag Match Type from `Table_Tag`  to  `Column_Tag`. The correct match type is now retained after import.

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