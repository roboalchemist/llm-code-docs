# Source: https://docs.snowflake.com/en/index.md

# Welcome to Snowflake Documentation

In these topics, you will find the information you need to access your Snowflake account and perform all the administrative and user tasks associated
with using Snowflake. The documentation also provides conceptual overviews, tutorials, and a detailed reference for all supported SQL commands,
functions, and operators.

You can start by browsing the contents on the left or using the search box at the top to search across the documentation and other Snowflake resources.
If you do not find the information you are looking for, please feel free to reach out to Snowflake Documentation or Snowflake Support using the buttons
at the bottom of each page.

## [Get started with Snowflake for users](getting-started-for-users.md)

[Before you begin](user-guide/setup.md)
:   Overview of getting an account and methods for accessing Snowflake.

[Sign in to Snowflake](user-guide/connecting.md)
:   Overview of the different ways to connect to Snowflake.

[Snowflake key concepts and architecture](user-guide/intro-key-concepts.md)
:   Description of Snowflake architecture, key concepts, and features.

[Snowsight quick tour](user-guide/ui-snowsight-quick-tour.md)
:   Overview of Snowsight, Snowflake’s web-based interface.

[Overview of the data lifecycle](user-guide/data-lifecycle.md)
:   Introduces the main operations and corresponding SQL commands for getting your data into Snowflake and
    then using it to perform queries and other SQL operations.

## [Tutorials and Other Resources](other-resources.md)

This topic provides links to assorted “how to” tutorials/labs and “best practices” for using Snowflake.

## [Using Snowflake](user-guide.md)

* [Snowsight: The Snowflake web interface](user-guide/ui-snowsight.md) — Learn how to use Snowsight for your Snowflake operations:

  > * [Snowsight quick tour](user-guide/ui-snowsight-quick-tour.md)
  > * [Getting started with Snowsight](user-guide/ui-snowsight-gs.md)
  > * [Work with worksheets in Snowsight](user-guide/ui-snowsight-worksheets.md)
  > * [Workspaces](user-guide/ui-snowsight/workspaces.md)
  > * [About Snowflake Notebooks](user-guide/ui-snowsight/notebooks.md)
  > * [Using Snowflake Copilot](user-guide/snowflake-copilot.md)
  > * [Visualizing data with dashboards](user-guide/ui-snowsight-dashboards.md)
  > * [Explore and manage database objects in Snowsight](user-guide/ui-snowsight-data.md)
  > * [Monitor query activity with Query History](user-guide/ui-snowsight-activity.md)
  > * [Evaluating and monitoring account security in the Trust Center](user-guide/trust-center/overview.md)
  > * [Manage Snowflake Support cases](user-guide/ui-support.md)
  > * [Set up and manage notification contacts for Snowflake](user-guide/ui-snowsight-contacts.md)
* [Virtual warehouses](user-guide/warehouses.md) — Key concepts and tasks for creating and using virtual warehouses to execute queries and perform DML operations, such as loading and unloading data:

  > * [Overview of warehouses](user-guide/warehouses-overview.md)
  > * [Multi-cluster warehouses](user-guide/warehouses-multicluster.md)
  > * [Warehouse considerations](user-guide/warehouses-considerations.md)
  > * [Working with warehouses](user-guide/warehouses-tasks.md)
  > * [Using the Query Acceleration Service (QAS)](user-guide/query-acceleration-service.md)
  > * [Monitoring warehouse load](user-guide/warehouses-load-monitoring.md)
* [Databases, Tables & Views](user-guide/databases.md) — Key concepts and tasks related to understanding and working with Snowflake databases and tables:

  > * [Understanding Snowflake Table Structures](user-guide/tables-micro-partitions.md)
  > * [Working with Temporary and Transient Tables](user-guide/tables-temp-transient.md)
  > * [Introduction to external tables](user-guide/tables-external-intro.md)
  > * [Overview of Views](user-guide/views-introduction.md)
  > * [Working with Secure Views](user-guide/views-secure.md)
  > * [Working with Materialized Views](user-guide/views-materialized.md)
  > * [Table Design Considerations](user-guide/table-considerations.md)
  > * [Cloning considerations](user-guide/object-clone.md)
  > * [Data storage considerations](user-guide/tables-storage-considerations.md)
* [Query Data in Snowflake](guides-overview-queries.md) — Key concepts and tasks for executing queries in Snowflake:

  > * [Working with joins](user-guide/querying-joins.md)
  > * [Understanding How Snowflake Can Eliminate Redundant Joins](user-guide/join-elimination.md)
  > * [Working with Subqueries](user-guide/querying-subqueries.md)
  > * [Querying Hierarchical Data](user-guide/queries-hierarchical.md)
  > * [Working with CTEs (Common Table Expressions)](user-guide/queries-cte.md)
  > * [Querying Semi-structured Data](user-guide/querying-semistructured.md)
  > * [Analyzing data with window functions](user-guide/functions-window-using.md)
  > * [Identifying Sequences of Rows That Match a Pattern](user-guide/match-recognize-introduction.md)
  > * [Using Sequences](user-guide/querying-sequences.md)
  > * [Using Persisted Query Results](user-guide/querying-persisted-results.md)
  > * [Computing the Number of Distinct Values](user-guide/querying-distinct-counts.md)
  > * [Estimating Similarity of Two or More Sets](user-guide/querying-approximate-similarity.md)
  > * [Estimating Frequent Values](user-guide/querying-approximate-frequent-values.md)
  > * [Estimating Percentile Values](user-guide/querying-approximate-percentile-values.md)
  > * [Querying data using worksheets](user-guide/ui-snowsight-query.md)
  > * [Canceling Statements](user-guide/querying-cancel-statements.md)
* [Introduction to loading semi-structured data](user-guide/semistructured-intro.md) — Key concepts and tasks for working with JSON and other types of semi-structured data:

  > * [Supported formats for semi-structured data](user-guide/semistructured-data-formats.md)
  > * [Considerations for semi-structured data stored in VARIANT](user-guide/semistructured-considerations.md)
  > * [Tutorial: JSON basics for Snowflake](user-guide/tutorials/json-basics-tutorial.md)
* [Introduction to unstructured data](user-guide/unstructured-intro.md) — Key concepts and tasks for working with unstructured data:

  > * [Directory tables](user-guide/data-load-dirtables.md)
  > * [REST API for unstructured data support](user-guide/data-load-unstructured-rest-api.md)
  > * [Share unstructured data with a secure view](user-guide/unstructured-data-sharing.md)
  > * [Troubleshooting processing of unstructured data](user-guide/unstructured-ts.md)
* [Snowflake Time Travel & Fail-safe](user-guide/data-availability.md) — Key concepts and tasks for understanding how Snowflake maintains access to deleted and modified data, and also how Snowflake enables data recovery in the
  event of loss:

  > * [Understanding & using Time Travel](user-guide/data-time-travel.md)
  > * [Understanding and viewing Fail-safe](user-guide/data-failsafe.md)
  > * [Storage costs for Time Travel and Fail-safe](user-guide/data-cdp-storage-costs.md)
* [Introduction to streams and tasks](user-guide/data-pipelines-intro.md) — Key concepts and tasks for transforming and optimizing loaded data for analysis:

  > * [Introduction to streams](user-guide/streams-intro.md)
  > * [Introduction to tasks](user-guide/tasks-intro.md)
* [Introduction to business continuity & disaster recovery](user-guide/replication-intro.md) — Key concepts and tasks for replicating and failing over databases across multiple Snowflake accounts, as well as redirecting client connections, for business continuity and disaster recovery:

  > * [Introduction to replication and failover across multiple accounts](user-guide/account-replication-intro.md)
  > * [Redirecting client connections](user-guide/client-redirect.md)
* [Sample data sets](user-guide/sample-data.md) — Key concepts and tasks for using the sample data sets provided with Snowflake:

  > * [Use the sample database](user-guide/sample-data-using.md)
  > * [Sample data: TPC-H](user-guide/sample-data-tpch.md)
  > * [Sample Data: OpenWeatherMap — Deprecated](user-guide/sample-data-openweathermap.md)
* [Alerts and Notifications](guides-overview-alerts.md) — Key concepts and tasks for sending email notifications in SQL (e.g. from a
  stored procedure, task, etc.) and setting up alerts to perform actions or send notifications when data in Snowflake meets
  certain conditions.

  > * [Setting up alerts based on data in Snowflake](user-guide/alerts.md)
  > * [Notifications in Snowflake](user-guide/notifications/about-notifications.md)
* [Snowflake Postgres](user-guide/snowflake-postgres/about.md) — Create, manage, and use Postgres instances directly from Snowflake:

  > * [Creating a Snowflake Postgres Instance](user-guide/snowflake-postgres/postgres-create-instance.md)
  > * [Connecting to Snowflake Postgres](user-guide/snowflake-postgres/connecting-to-snowflakepg.md)
  > * [Snowflake Postgres Roles](user-guide/snowflake-postgres/postgres-roles.md)
  > * [Snowflake Postgres Connection Pooling](user-guide/snowflake-postgres/postgres-connection-pooling.md)
  > * [Snowflake Postgres Maintenance](user-guide/snowflake-postgres/postgres-maintenance.md)
  > * [Snowflake Postgres Read Replicas](user-guide/snowflake-postgres/postgres-create-replica.md)
  > * [Snowflake Postgres High Availability](user-guide/snowflake-postgres/high-availability.md)
  > * [Snowflake Postgres Cost Evaluation](user-guide/snowflake-postgres/postgres-cost.md)
  > * [Snowflake Postgres Insights](user-guide/snowflake-postgres/insights.md)
  > * [Snowflake Postgres logging](user-guide/snowflake-postgres/postgres-logging.md)
  > * [Snowflake Postgres networking](user-guide/snowflake-postgres/postgres-network.md)
  > * [Snowflake Postgres Instance Sizes](user-guide/snowflake-postgres/postgres-instance-sizes.md)
  > * [Snowflake Postgres Extensions](user-guide/snowflake-postgres/postgres-extensions.md)
  > * [Snowflake Postgres Server Settings](user-guide/snowflake-postgres/postgres-server-settings.md)

## [Managing Your Snowflake Account](user-guide-admin.md)

* [Account identifiers](user-guide/admin-account-identifier.md)

  > Detailed descriptions of the two unique account identifiers supported for connecting to Snowflake and using features that span multiple accounts.
* [Trial accounts](user-guide/admin-trial-account.md)

  > Instructions for signing up for a trial account, adding a credit card to the account, and canceling the account.
* [Parameter management](user-guide/admin-account-management.md)

  > Instructions for setting account, session, and object parameters for your account.
* [User management](user-guide/admin-user-management.md)

  > Instructions for creating and managing users in your account.
* [Behavior change management](release-notes/bcr-bundles/managing-behavior-change-releases.md)

  > Instructions for enabling and disabling behavior change releases in your account.

## [General reference](sql-reference.md)

* [Parameters](sql-reference/parameters.md) — parameters that can be used to control system behavior at the account, user, session, and object
  level.
* [References](sql-reference/references.md) — use references to authorize access on objects for owner’s rights stored procedures,
  applications, and classes.
* [Ternary logic](sql-reference/ternary-logic.md) — information about the behavior of NULL in Boolean expressions and with comparison operators.
* [Collation support](sql-reference/collation.md) — information about sorting and other character-set-dependent operations on text strings.
* [SQL format models](sql-reference/sql-format-models.md) — formats for specifying conversion of numeric and date/time values to and from text strings.
* [Object identifiers](sql-reference/identifiers.md) — rules for defining and using object identifiers, including resolving object names used in SQL
  statements:

  * [Identifier requirements](sql-reference/identifiers-syntax.md)
  * [Literals and variables as identifiers with IDENTIFIER() syntax](sql-reference/identifier-literal.md)
  * [Object name resolution](sql-reference/name-resolution.md)
* [Constraints](sql-reference/constraints.md) — concepts and reference information for defining and maintaining unique, primary key, and foreign
  key constraints in tables:

  * [Overview of Constraints](sql-reference/constraints-overview.md)
  * [Creating Constraints](sql-reference/constraints-create.md)
  * [Modifying Constraints](sql-reference/constraints-alter.md)
  * [Dropping Constraints](sql-reference/constraints-drop.md)
* [SQL variables](sql-reference/session-variables.md) — concepts and reference for defining and using variables in sessions.
* [Transactions](sql-reference/transactions.md) — concepts and reference for using transactions with SQL statements.
* [Table literals](sql-reference/literals-table.md) — concepts and reference for using table literals instead of a single scalar value in queries.
* [SNOWFLAKE database](sql-reference/snowflake-db.md) — reference for the SNOWFLAKE shared database, which is provided by Snowflake for
  querying/reporting on your organization, account, data sharing, and other object usage.
* [Snowflake Information Schema](sql-reference/info-schema.md) — concepts and reference for the Snowflake Information Schema, which consists of a set of metadata
  views and historical table functions for querying/reporting on objects in Snowflake.
* [Metadata fields in Snowflake](sql-reference/metadata.md) — concepts and reference for metadata fields in Snowflake.

## [SQL command reference](sql-reference-commands.md)

* [Query syntax](sql-reference/constructs.md) — structure of SQL queries in Snowflake.
* [Query operators](sql-reference/operators.md) — arithmetic, logical, and other types of operators.
* [Data Definition Language (DDL) commands](sql-reference/sql-ddl-summary.md) — overview of DDL commands.
* [Data Manipulation Language (DML) commands](sql-reference/sql-dml.md) — commands for performing DML operations, including:

  * Inserting, deleting, updating, and merging data in Snowflake tables.
  * Bulk copying data into and out of Snowflake tables.
  * Staging files for bulk copying.
* [All commands (alphabetical)](sql-reference/sql-all.md) — alphabetical list of all the commands.
* Commands categorized by the type of objects and operations they control, including:

  * General account-level objects (accounts, users, roles, security policies, integrations, etc.) and operations (failover & recovery, etc.).
  * Session-based operations (session context, queries, variables, transactions, etc.).
  * Virtual warehouses (for loading data and performing queries) and resource monitors (for controlling credit usage).
  * Databases, schemas, tables, and other schema-level objects (views, sequences, etc.).
  * Snowflake extensions and application development (user-defined functions, stored procedures, scripting, etc.).
  * Objects for sharing data (shares, listings, etc.).
  * Objects for classifying, protecting, and governing data (masking policies, row-access policies, tags, etc.).

## [Function and stored procedure reference](sql-reference-functions.md)

* [Summary of functions](sql-reference/intro-summary-operators-functions.md) — combined summary of all system-defined functions. Can be used as a
  quick-reference.
* [All functions (alphabetical)](sql-reference/functions-all.md) — alphabetical list of all system-defined functions (scalar, aggregate, table, etc.).
* [Aggregate functions](sql-reference/functions-aggregation.md) — functions that take multiple rows/values as input and return a single value.
* [Scalar functions](sql-reference/functions.md) — functions that take a single row/value as input and return a single value:

  * [Bitwise expression functions](sql-reference/expressions-byte-bit.md)
  * [Conditional expression functions](sql-reference/expressions-conditional.md)
  * [Context functions](sql-reference/functions-context.md)
  * [Conversion functions](sql-reference/functions-conversion.md)
  * [Data generation functions](sql-reference/functions-data-generation.md)
  * [Date & time functions](sql-reference/functions-date-time.md)
  * [Differential privacy functions](sql-reference/functions-differential-privacy.md)
  * [Encryption functions](sql-reference/functions-encryption.md)
  * [Geospatial functions](sql-reference/functions-geospatial.md)
  * [Hash functions](sql-reference/functions-hash-scalar.md)
  * [Metadata functions](sql-reference/functions-metadata.md)
  * [Notification functions](sql-reference/functions-notification.md)
  * [Numeric functions](sql-reference/functions-numeric.md)
  * [Semi-structured and structured data functions](sql-reference/functions-semistructured.md)
  * [String functions (regular expressions)](sql-reference/functions-regexp.md) — regular expression (search) functions
  * [String & binary functions](sql-reference/functions-string.md)
  * [Vector functions](sql-reference/functions-vector.md)
* [Model monitor functions](sql-reference/functions-model-monitors.md) — functions that retrieve metrics from machine learning model monitors.
* [System functions](sql-reference/functions-system.md) — functions that perform control operations or return system-level information.
* [Table functions](sql-reference/functions-table.md) — functions that return results in tabular format.
* [Window functions](sql-reference/functions-window.md) — functions that run analytic calculations, such as moving aggregations and rankings.
* [Data metric functions](sql-reference/functions-data-metric.md) — functions that enable data quality measurements for tables and views.
* [Stored procedures](sql-reference-stored-procedures.md) — stored procedures to facilitate using certain Snowflake features.

## [Snowflake Scripting reference](sql-reference-snowflake-scripting.md)

* [AWAIT](sql-reference/snowflake-scripting/await.md)
* [BEGIN … END](sql-reference/snowflake-scripting/begin.md)
* [BREAK](sql-reference/snowflake-scripting/break.md)
* [CANCEL](sql-reference/snowflake-scripting/cancel.md)
* [CASE](sql-reference/snowflake-scripting/case.md)
* [CLOSE](sql-reference/snowflake-scripting/close.md)
* [CONTINUE](sql-reference/snowflake-scripting/continue.md)
* [DECLARE](sql-reference/snowflake-scripting/declare.md)
* [EXCEPTION](sql-reference/snowflake-scripting/exception.md)
* [FETCH](sql-reference/snowflake-scripting/fetch.md)
* [FOR](sql-reference/snowflake-scripting/for.md)
* [IF](sql-reference/snowflake-scripting/if.md)
* [LET](sql-reference/snowflake-scripting/let.md)
* [LOOP](sql-reference/snowflake-scripting/loop.md)
* [NULL](sql-reference/snowflake-scripting/null.md)
* [OPEN](sql-reference/snowflake-scripting/open.md)
* [RAISE](sql-reference/snowflake-scripting/raise.md)
* [REPEAT](sql-reference/snowflake-scripting/repeat.md)
* [RETURN](sql-reference/snowflake-scripting/return.md)
* [WHILE](sql-reference/snowflake-scripting/while.md)

## [Appendices](appendices.md)

* [Notational conventions](sql-reference/conventions.md)

  > Notational conventions used in the Snowflake documentation.
* [Reserved & limited keywords](sql-reference/reserved-keywords.md)

  > List of words reserved for Snowflake SQL.
