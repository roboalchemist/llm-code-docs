# Source: https://docs.snowflake.com/en/user-guide-manage.md

# Managing Snowflake

These topics describes the tasks associated with using Snowflake.

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
* [Date & time data types](sql-reference/data-types-datetime.md) — Reference information and examples for working with dates, times and timestamps, and time zones in Snowflake:

  > * [Date and time input and output formats](sql-reference/date-time-input-output.md)
  > * [Working with date and time values](sql-reference/date-time-examples.md)
* [Introduction to loading semi-structured data](user-guide/semistructured-intro.md) — Key concepts and tasks for working with JSON and other types of semi-structured data:

  > * [Introduction to loading semi-structured data](user-guide/semistructured-intro.md)
  > * [Supported formats for semi-structured data](user-guide/semistructured-data-formats.md)
  > * [Considerations for semi-structured data stored in VARIANT](user-guide/semistructured-considerations.md)
  > * [Tutorial: JSON basics for Snowflake](user-guide/tutorials/json-basics-tutorial.md)
* [Introduction to unstructured data](user-guide/unstructured-intro.md) — Key concepts and tasks for working with unstructured data:

  > * [Directory tables](user-guide/data-load-dirtables.md)
  > * [REST API for unstructured data support](user-guide/data-load-unstructured-rest-api.md)
  > * [Share unstructured data with a secure view](user-guide/unstructured-data-sharing.md)
  > * [Troubleshooting processing of unstructured data](user-guide/unstructured-ts.md)
* [String & binary data types](sql-reference/data-types-text.md) — Reference information and examples for working with binary data in Snowflake:

  > * [Binary input and output](sql-reference/binary-input-output.md)
  > * [Using binary data](sql-reference/binary-examples.md)
* [Snowflake Time Travel & Fail-safe](user-guide/data-availability.md) — Key concepts and tasks for understanding how Snowflake maintains access to deleted and modified data, and also how Snowflake enables data recovery in the
  event of loss:

  > * [Understanding & using Time Travel](user-guide/data-time-travel.md)
  > * [Understanding and viewing Fail-safe](user-guide/data-failsafe.md)
  > * [Storage costs for Time Travel and Fail-safe](user-guide/data-cdp-storage-costs.md)
* [Introduction to streams and tasks](user-guide/data-pipelines-intro.md) — Key concepts and tasks for transforming and optimizing loaded data for analysis:

  > * [Introduction to streams](user-guide/streams-intro.md)
  > * [Introduction to tasks](user-guide/tasks-intro.md)
  > * [Introduction to dynamic tables](user-guide/dynamic-tables-about.md)
* [Introduction to business continuity & disaster recovery](user-guide/replication-intro.md) — Key concepts and tasks for replicating and failing over objects across multiple Snowflake
  accounts, as well as redirecting client connections, for business continuity and disaster recovery:

  > * [Introduction to replication and failover across multiple accounts](user-guide/account-replication-intro.md)
  > * [Redirecting client connections](user-guide/client-redirect.md)
* [Sample data sets](user-guide/sample-data.md) — Key concepts and tasks for using the sample data sets provided with Snowflake:

  > * [Use the sample database](user-guide/sample-data-using.md)
  > * [Sample data: TPC-H](user-guide/sample-data-tpch.md)
  > * [Sample Data: OpenWeatherMap — Deprecated](user-guide/sample-data-openweathermap.md)
