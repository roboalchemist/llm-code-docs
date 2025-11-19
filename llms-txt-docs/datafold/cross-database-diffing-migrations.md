# Source: https://docs.datafold.com/data-migration-automation/cross-database-diffing-migrations.md

# Cross-Database Diffing for Migrations

> Validate migration parity with Datafold's cross-database diffing solution.

When migrating data from one system to another, ensuring that the data is accurately transferred and remains consistent is critical. Datafold’s cross-database diffing provides a robust method to validate parity between the source and target databases. It compares data across databases, identifying discrepancies at the dataset, column, and row levels, ensuring full confidence in your migration process.

## How cross-database diffing works

Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.

### What kind of information does Datafold output?

Datafold’s cross-database diffing will produce the following results:

* **High-Level Summary:**
  * Total number of different rows
  * Total number of rows (primary keys) that are present in one database but not the other
  * Aggregate schema differences
* **Schema Differences:** Per-column mapping of data types, column order, etc.
* **Primary Key Differences:** Sample of specific rows that are present in one database but not the other.
* **Value-Level Differences:** Sample of differing column values for each column with identified discrepancies. The full dataset of differences can be downloaded or materialized to the warehouse.

### How does a user run a data diff?

Users can run data diffs through the following methods:

* Via Datafold’s interactive UI
* Via the Datafold API
* On a schedule (as a monitor) with optional alerting via Slack, email, PagerDuty, etc.

### Can I run multiple data diffs at the same time?

Yes, users can run as many diffs as they would like, with concurrency limited by the underlying database.

### What if my data is changing and replicated live, how can I ensure proper comparison?

In such cases, we recommend using watermarking—diffing data within a specified time window of row creation or update (e.g., `updated_at timestamp`).

### What if the data types do not match between source and target?

Datafold performs best-effort type matching for cases where deterministic type casting is possible, e.g., comparing `VARCHAR` type with `STRING` type. When automatic type casting without information loss is not possible, the user can define type casting manually using diffing in Query mode.

### Can data diff help if the dataset in the source and target databases has a different shape/schema/column naming?

Yes, users can reshape input datasets by writing a SQL query and diffing in Query mode to bring the dataset to a comparable shape. Datafold also supports column remapping for datasets with different column names between tables.

## Learn more

To learn more, check out our guide on [how cross-database diffing works](../data-diff/cross-database-diffing/creating-a-new-data-diff) in Datafold, or explore our extensive [FAQ section](../faq/data-migration-automation) covering cross-database diffing and data migration.
