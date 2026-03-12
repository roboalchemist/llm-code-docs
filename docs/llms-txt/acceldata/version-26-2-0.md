# Source: https://docs.acceldata.io/release/version-26-2-0.md

# Version 26.2.0

**Date: 31st January 2026**

> This section consists of the new features and enhancements introduced in this release.

- **Advanced Custom Spark SQL Support for Kafka and Google Pub/Sub**: ADOC now extends advanced custom Spark SQL support for reconciliation policies to Google Pub/Sub sources. This enhancement enables customers to define custom SQL for column selection and ordering when reconciling Pub/Sub data with other sources, supporting more flexible and accurate reconciliation use cases. For more information, see [Reconciliation Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/reconciliation-policy#configure-data-selection).
- **Improved Visibility for SQL-Based Policies**: ADOC now displays SQL statements and parameters in view mode for Data Quality and Reconciliation policies. This information is available in policy details, execution history (including sub-query types), and exported results, enabling easier review and auditing without editing the policy. For more information, see [Configuring Data Selection for Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-quality-policy#2-configure-data-selection).
- **Enhanced Policy Deletion Confirmation**: ADOC now adds an optional input field to the policy deletion confirmation dialog, allowing users to enter a message explaining the deletion. This message is also displayed on the Audit Logs page. For more information, see [Audit](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings#7-audit).
- **DAG Stitching for Improved Control Flow Visibility (Airflow OpenLineage)**: ADOC enhances Airflow OpenLineage integration by stitching multiple DAGs through shared data assets, providing clearer end-to-end control flow visibility where pipelines interact with the same underlying asset. This helps users better understand how changes made by different DAGs converge on common datasets. _Note:_ This stitching is currently asset-centric. Direct pipeline-to-pipeline stitching (for example, one DAG triggering another) is not supported at this time. For more information, see [Lineage Graph](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/understanding-the-pipeline-run-details#lineage-graph).
- **Improved Error Visibility for Pipeline Job Failures**: Error messages for failed pipeline jobs are now surfaced directly at the job level. When a pipeline task fails, users can quickly view the relevant failure details without navigating through multiple spans, making it easier to identify root causes and troubleshoot pipeline issues faster.
- **Next-Generation UX/UI Enhancements**: ADOC introduces visual and usability improvements with updated fonts, standardized buttons, and consistent colors and typography across the platform. These updates begin with Discover Assets, Manage Policies, and Asset Details pages and will be expanded to additional areas over time.

> The following data sources have transitioned from **Preview** to **General Availability**:> > - **[Atlan](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/atlan)**> - **[Trino](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/trino)**> - **[Google Cloud Pub/Sub](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/google-cloud-pub-sub)**

> This section highlights features or functionalities that are being phased out and will no longer be supported in future releases.

- **Deprecation of Data Policy Templates**: ADOC is deprecating Policy Templates as part of a broader shift toward direct rule-based configurations. Users can continue to create anomaly detection logic using rulesets, which provide equivalent and more flexible functionality.

> This section lists the issues that have been resolved in this release.

- Improved error handling for export failures by showing clearer messages and disabling retries when summary generation fails.
- Fixed profiling failures for tables with long column names across supported data sources.
- Resolved authorization issues that caused incorrect access denials for non-tenant Admin users.
- Fixed blank screen issues during initial login for users with specific permission configurations.
- Aligned role and permission checks across key UI flows to match RBAM expectations.
- Stabilized import configuration workflows, resolving failures in multi-step onboarding.
- Fixed asset registration issues during system configuration onboarding.
- Improved configuration navigation and validation consistency across environments.
- Resolved missing or empty values in the **Total Row Counts** column on the Discover Assets page.
- Fixed filtering issues on the Discover Assets page to ensure predictable behavior.
- Corrected inconsistent status labels across catalog and filter views.
- Fixed UI label mismatches and inconsistent status indicators across pages.
- Resolved navigation and rendering issues to improve overall UI stability and responsiveness.
- Fixed intermittent UI failures when viewing profiling and execution results.
- Resolved SnapLogic connector issues affecting pipeline discovery and monitoring.
- Fixed Azure Synapse crawler timeouts impacting datasource onboarding.
- Improved handling of datasource connection failures caused by Vault token expiry.
- Fixed issues with analyze-query execution in Compute.
- Resolved Data Quality job failures caused by executor shutdown race conditions.
- Fixed issues preventing reference validation jobs from being cancelled.
- Resolved reconciliation policy failures caused by schema and column mapping changes.
- Fixed reconciliation failures when writing results to S3 for large datasets.
- Resolved failures in generating and delivering Reliability reports.
- Fixed misalignment between Performance Trend charts and Policy Execution History timelines.
- Added support for namespace-based filtering of Airflow pipelines in the UI.
- Ensured Airflow task error messages are correctly surfaced in the Acceldata UI.
- Fixed issues caused by adding tags to Airflow pipelines.
- Fixed dbt Cloud pipeline runs incorrectly marked as incomplete.
- Ensured policy exports correctly include tags required for tag-match rules.
- Fixed SQL rule edits resetting previously selected columns.
- Resolved intermittent execution failures for SQL View–based policies.
- Fixed false “already exists” errors when updating similar automation policies.
- Aligned rule alert behavior with policy-level threshold flexibility for consistent alert semantics.