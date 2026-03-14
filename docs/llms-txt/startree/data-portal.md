# Source: https://docs.startree.ai/reference/startree-release-notes/data-portal.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Portal Release Notes

This page tracks Data Portal release notes. Each entry covers new features and enhancements shipped in that release.

## March 11, 2026

### New Features

* **Raw S3 Parquet data lake support (Beta, enabled on demand)**\
  Data Portal can now help connect Pinot Query Engine to S3 Parquet datasets as a S3 data lake source. Point to an S3 location and query it using Pinot Query Engine.

* **Iceberg REST catalog support — AWS Glue and S3Tables (Beta, enabled on demand)**\
  Query Iceberg tables using Pinot Query Engine. Data Portal now supports connecting to Iceberg REST catalogs backed by AWS Glue and AWS S3Tables, using REST endpoints with AWS SigV4 authentication.

* **Table storage usage UI (Beta, enabled on demand)**\
  A new UI surfaces table storage usage and growth trends over time, showing segment count and total size. This helps with understanding table growth patterns and planning capacity.

### Enhancements

* **Dark mode**\
  Data Portal now supports dark mode, improving usability in low-light environments and for those who prefer a darker UI.

* **Swagger UI for Data Portal APIs**\
  The Data Portal Swagger UI is now exposed alongside Pinot's Swagger, giving you a single place to browse and test Data Manager APIs. You can now use this to manage connections to your data sources.

* **Deleted segments no longer appear in Data Portal**\
  Fixed a discrepancy where segments deleted from an offline table could still appear in Data Portal. Data Portal now correctly reflects the empty state after deletions.

## February 18, 2026

### New Features

* **Configure tiered storage directly in Data Portal**\
  Introduced support for configuring Pinot tiered storage from Data Portal. Users can enable or disable tiered storage, configure tiers following [documented best practices](/corecapabilities/manage-data/set-up-tiered-storage/setup), and rely on sensible defaults where appropriate.

* **Broker and server tenant configuration in the UI**\
  Added the ability to configure broker and server tenants for tables directly from Data Portal, removing the need for manual edits to accomplish cluster-level configuration.

* **Retention time configuration**\
  Introduced controls to set and adjust table retention time (defaulting to 10 years), giving users direct control over data lifecycle policies without leaving the UI.

* **MAP data type — end-to-end support**\
  Added full support for the Pinot `MAP` data type across the stack. The Data Modeling UI lets users define MAP fields with key/value specs, validation rules, and index constraints (JSON index supported; some index types restricted). Query Console renders MAP column values as JSON for easier inspection.

### Enhancements

* **Saved queries no longer auto-run on click**\
  Saved queries are no longer executed automatically when clicked. Users can now open a saved query to review or edit it before choosing to run it, reducing accidental execution of heavy queries.

* **Support for newer Kafka consumer implementation**\
  Updated the default Kafka consumer implementation in Data Portal to use the newer `KafkaFactory` class from Apache Pinot. This aligns with current best practices and improves compatibility with newer Kafka and Pinot deployments.

### Bug Fixes

* **Long double values no longer show as "Invalid Number"**\
  Fixed an issue where certain long double values (for example, `97.60000000000001`) were incorrectly displayed as "Invalid Number" in query results. These values now render correctly.

* **Stale ingestion status in the Data Portal UI**\
  The table ingestion status could appear outdated even while ingestion was running. The table details view now refreshes more frequently, giving users an accurate, up-to-date status.

* **Pinot Preview API hanging on S3 files**\
  Resolved an issue where the Pinot Preview API could hang when previewing data from S3. The preview experience for S3-based sources is now more reliable.

* **Clearer permission error for running queries**\
  Improved error handling in Query Console when a user is missing the `getRunningQueries` permission. Queries continue to run successfully with clearer, less disruptive messaging instead of a confusing 403 popup.

***

## January 15, 2026

### New Features

* **Protobuf descriptor file support for real-time tables**\
  When creating real-time tables with Protobuf data, users can now point to a descriptor file (for example, a file on S3) instead of requiring a schema registry URL. This aligns Data Portal with common Protobuf deployment patterns and removes the need for manual overrides.

* **Cancel queries from the editor**\
  The query editor now attaches a unique client query ID to each execution, enabling cancellation of that specific query mid-flight without going through a separate API call.

### Enhancements

* **Text index support in index configuration**\
  Extended index configuration to include text index options via Pinot APIs, improving query performance and search flexibility on free-text fields.

***

## January 9, 2026

### New Features

* **Query observability**\
  Operators can now see all running queries alongside their metadata and total runtime via Pinot's query APIs, filling a key gap for managing long-running or expensive queries.

### Enhancements

* **Richer Table List view**\
  The Table List now surfaces operational details at a glance: ingestion status with a clear definition of "healthy", disabled table indicators, data source details (bucket, topic, or saved connection name), table size, and segment count. Real-time tables that have no scheduled next run show "N/A" rather than a misleading value.

* **Inline IAM setup guidance for S3 and Kinesis**\
  The S3/Kinesis connection flow now includes sample IAM and trust policies with placeholders for StarTree and bucket details, plus a link to the [full IAM role setup guide](/corecapabilities/ingestdata/recipes/iam-role-s3). Users get step-by-step guidance without leaving Data Portal.

* **Group claims visible in the user menu**\
  When RBAC is enabled, the user menu now shows the group claims from the authentication token alongside the user's email. A summary of groups is shown by default with an option to expand all. When RBAC is off or the token carries no group claims, the UI handles this gracefully.

* **Stale error messages cleared on retry**\
  When a user retries an action after a failure, the previous error toast is now dismissed before the new attempt resolves. This prevents stale errors from lingering and makes the outcome of each retry clear.

***

## December 17, 2025

### New Features

* **Visual query execution stats and EXPLAIN PLAN**\
  Building on the stage-level stats introduced in the previous release, Query Console now surfaces EXPLAIN plan visualizations alongside execution stats for all query types, making performance debugging significantly easier.

* **Cleaner execution details with a dedicated JSON tab**\
  Execution details are now organized into tabs, with raw JSON in its own tab and the table widget standardized across the app.

* **Type-ahead search in all dropdowns**\
  Every dropdown in Data Portal now supports inline filtering — type a few characters to narrow a long list of options. Loading indicators appear inside the dropdown while data is being fetched.

### Bug Fixes

* **Transformation rules consistently enforced across views**\
  Fixed an inconsistency where transformation functions could be applied to existing fields in JSON View even though Table View blocked it. Validation is now enforced at the API level regardless of which view is used.

* **Query execution metadata no longer returns empty values**\
  Resolved an issue where the Query Console SQL API sometimes returned zero or empty values for query timings and stats.

***

## December 10, 2025

### New Features

* **Stage-level stats for multi-stage engine queries**\
  Query Console now includes `stageStats` in the JSON response and a visual representation of the stage stats when running queries with the multi-stage engine. This gives users detailed per-stage execution stats for performance tuning and troubleshooting without needing a separate tool.

### Enhancements

* **Smarter segment builder defaults based on schema width**\
  Data Portal now automatically sets `columnMajorSegmentBuilderEnabled` based on table schema width — disabled for tables with fewer than 40 columns, enabled for wider schemas. Commit-time compaction defaults to off, with the option to enable it when turning on Upsert during table creation. This avoids a one-size-fits-all configuration and improves out-of-the-box performance.

* **Consistent default indexes across all ingestion flows**\
  The Upload File ingestion flow now applies the same default index configuration logic used in other ingestion paths. Tables created from uploaded files get sensible indexes automatically, reducing the need for manual tuning after setup.

* **JSON and text columns default to no-dictionary**\
  JSON and text columns are now marked as "no dictionary" by default, with JSON index enabled where appropriate. This prevents the segment bloat that occurred when these column types were incorrectly assigned a dictionary, and aligns default behavior with best practices for JSON and text workloads.

***

## December 4, 2025

### New Features

* **Folder selection for batch sources**\
  When adding a batch source in Data Portal, you can now browse and select folders directly using a folder picker instead of typing paths manually. This makes source configuration faster and reduces the chance of path errors.

* **Partial results in Query Console**\
  When some segments are unavailable, Query Console now displays the partial results alongside a clear error message, rather than showing only an error.

### Enhancements

* **Ingestion type renamed from "Standard" to "Append"**\
  In the Additional Config section for real-time tables, the ingestion type previously labeled "Standard" is now called "Append". The new label better describes how the mode works and reduces confusion when choosing between Append, Upsert, and Dedupe.

* **Ingestion failures surface explicitly**
  Ingestion flows now default to `"continueOnError": false`, so failures are surfaced immediately instead of being silently skipped. This makes it easier to catch and act on ingestion issues early.

* **More reliable file pattern handling**\
  The ingestion backend now correctly prioritizes `includeFilePatterns` when present, ensuring ingestion follows the configured patterns and avoids picking up unintended files.

***

## November 11, 2025

### New Features

* **Tableau available as a dedicated client**\
  Tableau is now listed as a first-class client in the Clients page, with a tailored connection URL generation flow. This removes the need for manual URL construction when connecting Tableau to StarTree.

* **Clients section moved into Data Portal**\
  Client connection management has moved from MyApps into Data Portal, so all client setup and configuration is accessible from one place within the main UI.

***

Built with [Mintlify](https://mintlify.com).
