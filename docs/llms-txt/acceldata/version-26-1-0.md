# Source: https://docs.acceldata.io/release/version-26-1-0.md

# Version 26.1.0

**Date: 11th January 2026**

> This section consists of the new features and enhancements introduced in this release.

- **SnapLogic Integration for Pipeline Observability**: ADOC now supports native observability for SnapLogic pipelines, including automatic pipeline discovery, execution status, error visibility, and log access. Data quality and reliability policies can be triggered based on SnapLogic pipeline outcomes, with secure data-plane–based connectivity. For more information, see [SnapLogic](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/snaplogic).
- **Enhanced Rule-Level Thresholds in Data Quality and Freshness Policy Creation**: Rule-level checks can now optionally show Success, Warning, or Failure, instead of only pass or fail. This allows users to see early signs of data quality degradation before a rule fully fails, while keeping existing policies unchanged unless warning thresholds are explicitly added. For more information, see [Configure Rules for Data Quality Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-quality-policy#configure-rules).
- **Custom SQL Support for Reconciliation Policies**: ADOC now supports Custom SQL–based reconciliation, allowing users to apply transformations, aggregations, and business logic on source and target datasets before comparison. This enables reconciliation on derived data and complex enterprise use cases while preserving existing incremental and selective execution capabilities. Hash Equality reconciliation is deprecated. For more information, see Reconciliation Policy documentation. For more information, see [Configure Rules for Reconciliation Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/reconciliation-policy#configure-rules).
- **Reliability Reporting Service Updates**: Reliability Reports now follow updated scheduling behavior after being saved, support Email notifications through the Reporting Service, and enforce clearer permission requirements for report access. Policy-based score aggregation is supported in reports, while rule-level and column-level views remain unavailable in the current reporting experience. For more information, see [Reliability Reports](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/reliability-reports).

> This section lists the issues that have been resolved in this release.

- Resolved an issue where asset filters in the Discover Assets page stopped working after changing filter conditions—such as removing a data source filter causing the remaining domain filter to be ignored—ensuring filters are now applied dynamically and consistently as they are added or removed.
- Resolved an issue where migrating Freshness policies created duplicate policies instead of overwriting existing ones, ensuring correct policy updates and accessibility on target assets.
- Resolved an issue where modifying an SQL rule in a Data Quality policy reset the selected columns to all columns, ensuring previously selected column subsets are preserved after edits.
- Resolved an issue where profiling failed for tables with long column names due to column length limitations, ensuring successful profiling for assets with extended column name lengths across supported data sources.
- Resolved issues with the List Data Quality Policies API where the rule_status filter was ignored and pagination failed for tenants with a large number of policies, ensuring accurate filtering and reliable retrieval of all DQ policies across pages.
- Resolved an issue where reference validation jobs could not be canceled from the Jobs page and returned an internal server error, ensuring running jobs can now be canceled successfully.
- Resolved an issue where the Azure Synapse crawler failed with connection timeout errors while fetching metadata, ensuring successful crawler completion and asset registration in the ADOC catalog.
- Resolved an issue where DQ policy execution times appeared inconsistent between the Reliability Reporting Performance Trend chart and the Policy Execution History page, ensuring consistent timezone handling across both views.
- Resolved an issue where Data Quality jobs failed with a “Shutdown in progress” exception during control plane deployments, ensuring running jobs are handled gracefully during pod restarts and are not interrupted by service updates.
- Resolved an issue where updating Data Reliability automations on pipelines failed with a “similar automation policy already exists” error, ensuring existing automations can now be edited successfully without requiring deletion and recreation.
- Resolved an issue where datasource connections failed due to Vault token expiry requiring manual pod restarts, ensuring Vault tokens are refreshed proactively to maintain uninterrupted datasource connectivity.
- Resolved an issue where the Pipeline dashboard displayed incorrect execution durations when hovering over recent runs, ensuring accurate execution time values are shown.
- Resolved an issue where changing the timezone in the schedule configuration of a Freshness policy did not take effect, ensuring the updated timezone is now applied correctly.