# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips/optimize-pentaho-analyzer.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/performance-tuning/mondrian-performance-tips/optimize-pentaho-analyzer.md

# Optimize Pentaho Analyzer

Once you've properly tuned your data warehouse, you can move on to tuning your ROLAP schema, the Mondrian engine, and the Analyzer client tool.

## Partitioning high-cardinality dimensions

If you cannot avoid creating high-cardinality dimensions, then you must devise a strategy to make them more performant without reducing their size. Typically a database will partition large tables, which makes querying one partition a quick operation. However, the Analyzer engine does not have any way of detecting which tables are partitioned and which are not. Therefore, MDX queries will be translated into SQL statements that are too broad, resulting in a query that traverses all of a table's partitions.

To instruct the Analyzer engine to properly address a (partitioned) high-cardinality dimension, you must modify the ROLAP schema and explicitly set the **highCardinality** property of the **ElementCubeDimension** element to `true` on each applicable dimension. This will streamline SQL generation for partitioned tables; ultimately, only the relevant partitions will be queried, which could greatly increase query performance.

## Mondrian log analysis

To determine Analyzer performance problems, you can view a log of the Analyzer engine and your data warehouse database. This will reveal information about the infrastructure and the SQL and MDX queries involved in your Analyzer calculations. Your DBA should perform the initial database performance-tuning work by looking at the database logs, ensuring that statistics are up to date (access plans are computed and rational) and that your usage is profiled. Make sure the aggregation levels are based on the top 50-80 common uses.

Base all of your performance tuning on this data; it will tell you everything that you need to know about bottlenecks in your data structure.

You can also determine the causes behind hanging queries in an Analyzer report by viewing Mondrian log information directly through the Analyzer interface:

1. Log into the BA Server as an administrator.
2. Create or load an Analyzer report.
3. Click the **More actions and options** icon in the report toolbar, and select **Administration** > **Clear Cache**. Click **Ok**.
4. Click the icon again and select **Administration** > **XML**. Click **Ok**.
5. Click the icon again and select **Administration** > **Log**.

A new browser tab will open with log information about the open report. You can refresh this page to see the query progress in real time. The following log entries are the most important to watch out for:

* If each SQL query is reported twice. The first time is for Mondrian to get the first record and the second time is to retrieve all records
* SQL queries with high execution times
* SQL queries that return large volumes of data (more than 1000 rows)
* SQL queries that don't join tables
* SQL queries that don't include filters
* This log entry: `WARN mondrian.rolap.RolapUtil Unable to use native SQL evaluation for 'NonEmptyCrossJoin'; reason: arguments not supported`. If you see this, try switching the **contains** filter into an **includes** filter, or make the contains filter more selective

## Configuring Pentaho Analyzer for large data warehouses

Analyzer has some low-level configuration options that will improve performance when working with large data warehouses and high-cardinality dimensions:

* `filter.members.max.count=500`
* `filter.dialog.apply.report.context=false`
* `filter.dialog.useTopCount=true`
* `report.request.service.result.expire.time.seconds=30`
* `report.request.service.result.cleanup.time.seconds=300`

These **analyzer.properties** settings are explained in the following table:

| Property                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **filter.members.max.count**                           | Controls the maximum number of values to show in the filter dialogue, such as include/exclude filters and date range dropdowns.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **filter.dialog.apply.report.context**                 | If set to `true`, when showing available members in the filter dialog, Analyzer will limit those members to the existing filters or measures on the report. This means that when retrieving the list of members, Analyzer will perform the join in the fact table and then apply dimension filters. For a high-cardinality dimension, this may significantly reduce the list of members loaded into memory.                                                                                                                                                                                                                     |
| **filter.dialog.useTopCount**                          | If both this and **mondrian.native.topcount.enable** in mondrian.properties are set to `true`, when showing the first set of members in the filter dialogue, Analyzer will only show that set of members sorted within hierarchy. For high-cardinality dimensions, this is required to avoid loading all members into memory. However, if a user uses the Find box in the filter dialogue or if you have **filter.dialog.apply.report.context** set to true, then the TopCount will not be used.                                                                                                                                |
| **report.request.service.result.expire.time.seconds**  | Report results are released after this amount of time has passed.Analyzer report requests are processed asynchronously and immediately cleaned up after the first download. While this is efficient because clients usually don't need to download a report more than once, it causes issues with popup blockers that will block the first download and re-submit the download after prompting the user. If you expire the request after 30 seconds, you will work around the popup blocker issues while also enabling people to refresh the browser to re-download a report. This only applies to PDF, Excel or CSV downloads. |
| **report.request.service.result.cleanup.time.seconds** | Report result cleanup occurs after this amount of time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Configuring the Mondrian engine for large data warehouses

There are several **mondrian.properties** options that control how the Analyzer engine interacts with large data warehouse volumes in conjunction with Pentaho Analyzer:

* `mondrian.result.limit=5000000`
* `mondrian.rolap.iterationLimit=5000000`
* `mondrian.rolap.queryTimeout=300`
* `mondrian.native.crossjoin.enable=true`
* `mondrian.native.topcount.enable=true`
* `mondrian.native.filter.enable=true`
* `mondrian.native.nonempty.enable=true`
* `mondrian.rolap.maxConstraints=1000`
* `mondrian.native.ExpandNonNative=true`
* `mondrian.expCache.enable=true`

These **mondrian.properties** settings are explained in the following table:

| Property                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **mondrian.result.limit**            | Controls the largest cross join size that Mondrian will handle in-memory. Ideally, no queries should involve large cross joins in-memory; instead, they should be handled by the database.                                                                                                                                                                                                                                                            |
| **mondrian.rolap.iterationLimit**    | This is similar to **mondrian.result.limit**, except this applies to calculating aggregates in-memory such as SUM, MAX, AGGREGATE, etc. This should be set to the same value as **mondrian.result.limit**.                                                                                                                                                                                                                                            |
| **mondrian.rolap.queryTimeout**      | If any query runs past this number of seconds, then the query is immediately cancelled. The total sum of all SQL statements to process a single MDX statement must be less than this timeout. Setting this to zero disables query timeout, which is not recommended because runaway queries can deprive system resources from other necessary processes.                                                                                              |
| **mondrian.native.crossjoin.enable** | If this is set to `true`, when Mondrian needs to cross join multiple dimensions in a report, if the cross join is non-empty, meaning a fact table relationship has been defined, then the join operation is done using SQL. The resultant SQL query returns only combined dimension members that actually have fact data. This reduces the amount of tuples that need to be processed and is critical for performance on high-cardinality dimensions. |
| **mondrian.native.topcount.enable**  | If set to `true`, when fetching the first set of records for the filter dialog, Mondrian will only read that set of records into memory. If set to `false`, all records from the dimension level will be read into memory.                                                                                                                                                                                                                            |
| **mondrian.native.nonempty.enable**  | If set to `true`, when fetching the first set of records for the filter dialog, Mondrian will only read that set of records into memory. If set to `false`, all records from the dimension level will be read into memory.                                                                                                                                                                                                                            |
| **mondrian.rolap.maxConstraints**    | This should be set to the largest number of values that the data warehouse database supports in an IN list.                                                                                                                                                                                                                                                                                                                                           |
| **mondrian.native.ExpandNonNative**  | Works in conjunction with native evaluation of cross joins. If set to `true`, Mondrian will expand cross join inputs to simple member lists that are candidates for pushdown.                                                                                                                                                                                                                                                                         |

## Redesigning Analyzer reports for maximum performance

Once you have an idea of what you want to show with your Analyzer report, you will almost certainly have to redesign it to be more performant. Because an Analyzer report is basically a hierarchical list of actions, the order in which fields and filters are added to the report can make a big difference in query response time. Even though this does not change the report's graphical output, what happens behind the scenes can make that output display more quickly.

When you re-create your reports, follow this process for best performance:

1. Add and filter by low-cardinality dimensions first
2. Add measures to the report
3. Add high-cardinality dimensions last

   **Note:** When filtering, always choose include/exclude over contains/doesn't contain.

## Mondrian cache control

You can control the cache infrastructure that the Pentaho Analyzer engine uses for OLAP data. See **Install Pentaho Data Integration and Analytics** for details about Mondrian cache control.
