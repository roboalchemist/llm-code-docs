# Source: https://fivetran.com/docs/destinations

Title: Supported Destinations | Fivetran destination documentation and setup

URL Source: https://fivetran.com/docs/destinations

Markdown Content:
You must connect a destination to Fivetran so that our connectors can sync data into it from your sources. Fivetran supports cloud data warehouses, databases, online data platforms, and data lakes as destinations.

Destinations were previously called "warehouses" in our documentation because we originally only supported data warehouses as destinations.

* * *

Supported destinations[](https://fivetran.com/docs/destinations#supporteddestinations)
--------------------------------------------------------------------------------------

Fivetran supports the following destinations:

*   [Apache Kafka](https://fivetran.com/docs/destinations/apache-kafka)
*   [Azure Synapse](https://fivetran.com/docs/destinations/azure-warehouse)
*   [BigQuery](https://fivetran.com/docs/destinations/bigquery)
*   [ClickHouse Cloud](https://fivetran.com/docs/destinations/clickhouse)[Partner-Built](https://fivetran.com/docs/partner-built-program)[Beta](https://fivetran.com/docs/core-concepts#releasephases)
*   [Convex](https://fivetran.com/docs/destinations/convex)[Partner-Built](https://fivetran.com/docs/partner-built-program)In Dev
*   [Databricks](https://fivetran.com/docs/destinations/databricks)
*   [Managed Data Lake Service](https://fivetran.com/docs/destinations/managed-data-lake-service)
*   [Materialize](https://fivetran.com/docs/destinations/materialize)[Partner-Built](https://fivetran.com/docs/partner-built-program)[Private Preview](https://fivetran.com/docs/core-concepts#releasephases)
*   [Milvus](https://fivetran.com/docs/destinations/milvus)[Partner-Built](https://fivetran.com/docs/partner-built-program)[Private Preview](https://fivetran.com/docs/core-concepts#releasephases)
*   [MotherDuck](https://fivetran.com/docs/destinations/motherduck)[Partner-Built](https://fivetran.com/docs/partner-built-program)[Private Preview](https://fivetran.com/docs/core-concepts#releasephases)
*   [MySQL](https://fivetran.com/docs/destinations/mysql)[Beta](https://fivetran.com/docs/core-concepts#releasephases)
*   [OneLake](https://fivetran.com/docs/destinations/onelake)
*   [Oracle](https://fivetran.com/docs/destinations/oracle)[Beta](https://fivetran.com/docs/core-concepts#releasephases)
*   [PostgreSQL](https://fivetran.com/docs/destinations/postgresql)
*   [Redshift](https://fivetran.com/docs/destinations/redshift)
*   [SingleStore](https://fivetran.com/docs/destinations/singlestore)[Partner-Built](https://fivetran.com/docs/partner-built-program)[Beta](https://fivetran.com/docs/core-concepts#releasephases)
*   [Snowflake](https://fivetran.com/docs/destinations/snowflake)
*   [SurrealDB](https://fivetran.com/docs/destinations/surrealdb)[Partner-Built](https://fivetran.com/docs/partner-built-program)[Beta](https://fivetran.com/docs/core-concepts#releasephases)
*   [SQL Server](https://fivetran.com/docs/destinations/sql-server)
*   [Teradata Vantage](https://fivetran.com/docs/destinations/teradata)[Partner-Built](https://fivetran.com/docs/partner-built-program)[Private Preview](https://fivetran.com/docs/core-concepts#releasephases)

[Let us know](mailto:sales@fivetran.com) if there is a destination that you would like, but that is not yet supported.

* * *

Unsupported scenarios[](https://fivetran.com/docs/destinations#unsupportedscenarios)
------------------------------------------------------------------------------------

Our load queries are designed to ingest data into your destination as efficiently as possible. However, it is not always possible to load large datasets into [row stores](https://en.wikipedia.org/wiki/Column-oriented_DBMS) like PostgreSQL and MySQL that were designed as operational data stores. If your database is unable to execute our load queries due to data size, you will need to switch to a horizontally scalable column store like Snowflake, Redshift, BigQuery, or Azure Synapse.

Also, we do not support configuring multiple connectors to the same destination table as it can lead to sync failures.

* * *

Data types[](https://fivetran.com/docs/destinations#datatypes)
--------------------------------------------------------------

All destinations contain data in the following types. We may need to convert a few data types to a type accepted by your destination. You can find information about the conversions on the individual destination pages.

| Data Type |
| --- |
| BOOLEAN |
| SHORT |
| INT |
| LONG |
| BIGDECIMAL |
| FLOAT |
| DOUBLE |
| LOCALDATE |
| LOCALDATETIME |
| INSTANT |
| STRING |
| XML |
| JSON |
| BINARY |

For more information about data types, see our [Data types documentation](https://fivetran.com/docs/core-concepts#datatypes).

* * *

Type inference[](https://fivetran.com/docs/destinations#typeinference)
----------------------------------------------------------------------

Sources do not always specify data types with great enough specificity for Fivetran to map directly to the destination type. For instance, a source may specify the type as `number`, when that could mean SHORT, INT,DOUBLE, etc. Or it may provide no types at all, like a bare .csv file. In these situations, Fivetran is capable of inferring the necessary data types, providing an on-the-fly mapping from untyped source values to typed destination values.

Occasionally, there is no good way to even infer a type, like when a type is unknown and no data exists for that column. In this case, Fivetran will not create a destination column, because there is no clear choice as to what type the destination column should have.

For more information about type inference, see our [Type inference documentation](https://fivetran.com/docs/core-concepts#typeinference).

* * *

Sync overview[](https://fivetran.com/docs/destinations#syncoverview)
--------------------------------------------------------------------

1.   Create one or more source connections.
2.   Connect target destination.
3.   Fivetran does the rest! Extracting, transforming, and loading the data into your destination.

If your destination gets disconnected, we will still keep a record of the progress that we've made for every source connection. Fivetran maintains an internal set of progress cursors which is recorded when an update is successfully synced. This provides an air-tight handoff between syncs so that no data is ever missed. Because of this, Fivetran's system is extremely tolerant to service interruptions. If there is an interruption in your service, such as your destination going down, Fivetran will automatically resume syncing exactly where it left off after your destination is live again (even if it's days or weeks later).

* * *

Destination costs[](https://fivetran.com/docs/destinations#destinationcosts)
----------------------------------------------------------------------------

Fivetran uses queries to load data into your destination. If your service provider charges for compute usage, they will charge you when Fivetran loads data into your destination. Two main factors influence your costs:

*   **Data volume**: Loading large amounts of data costs more.
*   **Sync frequency**: Syncing data frequently may cost more, depending on how often updates happen in your source. In your Fivetran dashboard, you can choose how frequently your syncs run, from every 5 minutes to every 24 hours.

The costs vary depending on your service provider. For more information, see the individual destination pages.

* * *

Schema and table management[](https://fivetran.com/docs/destinations#schemaandtablemanagement)
----------------------------------------------------------------------------------------------

Fivetran uses the **Destination schema** name you provide in the connection setup form to create the schema in your destination. By default, we use the connection name as the destination schema name. The destination schema name is permanent and cannot be changed.

Fivetran creates, delivers, and manages the base tables to your destination. Base tables are the direct replicated tables from the source, that you use as the building blocks to build your analysis. Fivetran maintains an internal representation of the tables and schemas that we deliver. On every update, we check against this internal representation to identify any schema changes in the source. We _do not_ build our internal representation from your destination.

Any schema changes that you make to the destination tables will not be captured in our internal representation.

### Let Fivetran do the mapping[](https://fivetran.com/docs/destinations#letfivetrandothemapping)

Fivetran creates the mapping between source objects/columns and your destination tables/columns. When you add a column or otherwise make a change to the source schema, that change will be detected and pushed into your destination automatically.

### Updating Fivetran-delivered tables[](https://fivetran.com/docs/destinations#updatingfivetrandeliveredtables)

If you make manual changes to the destination tables, during any subsequent updates, the schema/tables will be updated as though your changes had not been made. If you manipulate the tables in your destination, our internal representation will not be updated, and the schema migrations and updates will not occur as expected. Fivetran essentially manages the base tables in your destination, so it's best _not to_ manipulate these tables. Instead, you can create views referencing these tables with the desired changes.

There are certain optimizations that you can apply to your destination tables (sort keys, dist. keys, etc.) that Fivetran will not interfere with. These changes are destination-specific, so check the individual destination page for more information on each.

### Schema migrations[](https://fivetran.com/docs/destinations#schemamigrations)

On each update, we compare the incoming data to the internal record of what we have already delivered to your destination, looking for:

1.   New objects/tables
2.   New columns
3.   Column type changes

![Image 1: Overview Fivetran Automatic Schema Migration](https://fivetran.com/static-assets-docs/_next/static/media/schema-migrations.51c8cb4c.webp)

Fivetran doesn't scan your destination during every update, but rather has an internal understanding of the tables/schemas that we have already delivered. If you manipulate the tables in your destination, our internal representation will not be updated, and the schema migrations will not occur as explained. Fivetran essentially manages the base tables in your destination so, as a rule, it's best not to manipulate these tables, but rather to create views referencing these tables with the desired changes.

#### Table changes[](https://fivetran.com/docs/destinations#tablechanges)

When we see new objects or tables in your source, we will automatically create them as tables in your destination.Any objects that are deleted from the source are left untouched as tables in your destination, remaining in the state they were in at the last update. Renamed objects will be treated as a new table and a deleted table.

#### Column changes[](https://fivetran.com/docs/destinations#columnchanges)

Our sync is in one direction: from the data source (a SaaS application, database, etc.) to your destination, but not the other way around.

New columns in a source table are added in your destination, and we trigger a full re-import or incremental sync of the table.

We treat renamed columns as two: a new column and a deleted column.

Deleted columns are handled in one of two ways:

*   Some connectors leave the deleted column in your destination with its previous data intact and add `NULL` values from its delete date forward. If the table is re-synced, the previous data in the deleted column is removed.

*   Certain connectors replace all values in the deleted column with `NULL` values. The connectors are:

    *   [MySQL](https://fivetran.com/docs/connectors/databases/mysql) (includes Generic MySQL, Amazon Aurora MySQL, Amazon RDS MySQL, Azure Database for MySQL, Google Cloud MySQL)
    *   [Oracle](https://fivetran.com/docs/connectors/databases/oracle) (includes Generic Oracle, Oracle RAC, Amazon RDS Oracle, High-Volume Agent Oracle)
    *   SQL Server (includes only [High-Volume Agent SQL Server](https://fivetran.com/docs/connectors/databases/sql-server/hva-sql-server))
    *   [Snowflake](https://fivetran.com/docs/connectors/databases/snowflake)

If you manually added a column to your destination's schema table that causes inconsistencies, we do not manage those inconsistencies. If this occurs, the next sync cycle won't be successful. The solution for this is to delete the columns that you manually added to your destination's schema table and wait for the next sync to begin, at which point new attributes from your data source will be created/synced into your destination.

#### Column type changes[](https://fivetran.com/docs/destinations#columntypechanges)

When you change the data type of a column in your source, we look at whether it is a widening or a narrowing change.

*   If it is a widening change (for example, when you change a column type from INT to LONG), we update the column type in your destination.

*   If it is a narrowing change (for example, when you change a column type from LONG to INT), we do not update the column type in your destination.

#### Primary key changes[](https://fivetran.com/docs/destinations#primarykeychanges)

When you change the primary key in your source, you may observe duplicate records or other data integrity issues in your destination.

We have detected data integrity issues in the destination when:

*   the primary key is initially a combination of two or more columns and is later changed to a single column. For example, `id` and `row_id` to `product_id`.
*   the primary key column changes. For example, `id` to `row_id`.

If you change the primary key for a database or application connection, we recommend dropping the existing table from the destination and re-syncing the table.

[Monthly Active Rows (MAR)](https://fivetran.com/docs/usage-based-pricing#monthlyactiverows) (MAR) is the number of distinct primary keys synced from the source system to your destination in a given calendar month. We separately count primary keys by account, destination, connector, and table. Changing the primary key in your source will impact your MAR.

### Long value truncation[](https://fivetran.com/docs/destinations#longvaluetruncation)

Destinations have different maximum allowed lengths for JSON, STRING, and BINARY type columns.

If a value in a JSON column exceeds the maximum allowed length for your destination, it is replaced with a JSON error message reading `{"FIVETRAN ERROR": "Original value could not be synced because it exceeded your warehouse's maximum length of N"}`, where _N_ is the maximum column length your destination allows.

If a value in a STRING column exceeds the maximum allowed length, it is truncated to the maximum length allowed.

If a value in a BINARY column exceeds the maximum allowed length, it is replaced with `null`. A warning message reading `"encoded_binary_string_too_long", "A record containing a Base64 encoded binary value that was over <max binary allowed in your warehouse> characters in length of your warehouse limit, in the '<column name>' column of the '<schema name>'.'<table name>' table, was overwritten with null value."` is displayed on the Fivetran dashboard.

If a value in an XML column exceeds the maximum allowed length for your destination, it is replaced with an XML error message reading `<errmsg> <error>FIVETRAN_ERROR</error> <message>Original value could not be synced because it exceeded your warehouse's maximum length of N </message> </errmsg>`, where _N_ is the maximum column length your destination allows.

### Date and time value range[](https://fivetran.com/docs/destinations#dateandtimevaluerange)

Every destination defines its own supported ranges for date and time data types. Fivetran aligns with those limits during data loading to ensure compatibility. However, most destinations support year values in the range **0001** to **9999**. For the exact supported limits, see your destination's documentation.

The 0001–9999 year range applies to the following Fivetran data types:

| Data Type | Minimum value | Maximum value |
| --- | --- | --- |
| LOCALDATE | 0001-01-01 | 9999-12-31 |
| LOCALDATETIME | 0001-01-01 00:00:00 | 9999-12-31 23:59:59 |
| INSTANT | 0001-01-01T00:00:00Z | 9999-12-31T23:59:59Z |

If the source sends a date or time value outside this range, Fivetran replaces the value with `NULL` during sync.

If your source data contains values outside the supported range, contact our [support team](https://support.fivetran.com/).

* * *

Connecting your destination[](https://fivetran.com/docs/destinations#connectingyourdestination)
-----------------------------------------------------------------------------------------------

Fivetran must be able to connect to your destination to deliver data because our connectors follow a push strategy. We support the following connection methods:

*   Direct connection by safelisting Fivetran’s IP
*   SSH tunnel
*   Reverse SSH tunnel
*   AWS PrivateLink, Azure Private Link, or Google Cloud Private Service Connect ([Business Critical](https://fivetran.com/docs/usage-based-pricing#usagebasedpricing) only)
*   Private Google Access
*   VPN tunnel

For more information about the connection methods, see our [Destination Connection Options documentation](https://fivetran.com/docs/destinations/connection-options).

* * *

Connecting multiple destinations[](https://fivetran.com/docs/destinations#connectingmultipledestinations)
---------------------------------------------------------------------------------------------------------

Fivetran supports multiple destinations per Fivetran account. Each destination has separate connections, users and access permissions.

Common use cases for multiple destinations are:

*   maintaining a second "testing" destination for BI experimentation
*   isolating users from having access to other connections
*   trialing another type of destination temporarily

### Instructions[](https://fivetran.com/docs/destinations#instructions)

To add another destination, go to the [Destinations page](https://fivetran.com/dashboard/destinations) and click **Add destination**. You must have an [Account Administrator, Destination Creator role or a custom role with the Create Destinations permissions](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control) in your Fivetran account to add a destination.

* * *

Choosing your data processing location and cloud service provider[](https://fivetran.com/docs/destinations#choosingyourdataprocessinglocationandcloudserviceprovider)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Fivetran runs data connectors on servers in the US, EU, Australia, UK, Canada, Singapore, and India regions. Configure the geography you want to use in your destination settings.

Depending on the plan you are on, you can also select the cloud service provider and cloud region. See our [Data Residency documentation](https://fivetran.com/docs/privacy#fivetrandataresidency) for details.

### Instructions[](https://fivetran.com/docs/destinations#instructions_1)

1.   On your Fivetran dashboard, [select **Destination**](https://fivetran.com/dashboard/warehouse).
2.   Find and select the destination you want to update.
3.   On the destination overview page, click **Actions** and then click **Edit connection details**.
4.   Use the **Data processing location** drop-down menu to select the region from which you'd like Fivetran to run your syncs.
5.   If you are on an [Enterprise or Business Critical plan](https://www.fivetran.com/pricing/features), select the **Cloud service provider**.
6.   If you are on a Business Critical plan, select the **AWS region**, **Azure region**, or **GCP region** respectively.

* * *

Choosing your time zone[](https://fivetran.com/docs/destinations#choosingyourtimezone)
--------------------------------------------------------------------------------------

Fivetran uses your destination time zone to determine when to start your syncs. Our time zones are all Coordinated Universal Time (UTC) offsets - for example, Pacific Standard Time is UTC-08. Configure the time zone you want to use in your destination settings.

We call the UTC offsets by their standard names. For example, UTC-05 is called Eastern Standard Time, not Central Daylight Time.

By default, we do _not_ shift your UTC offset with daylight saving time. For example, you have syncs set to run every 24 hours at 2 a.m. Once daylight saving time begins, your syncs start at 3 a.m. local time. To preserve your sync start time, you can choose to automatically update your time zone when the US observes daylight saving time (from the second Sunday in March to the first Sunday in November). You can also manually change your time zone to match daylight saving time in your region.

### Instructions[](https://fivetran.com/docs/destinations#instructions_2)

1.   On your Fivetran dashboard, [select **Destination**](https://fivetran.com/dashboard/warehouse).
2.   Find and select the destination you want to update.
3.   Click **Actions** and then click **Edit connection details**.
4.   Use the **Time zone** drop-down menu to select your chosen time zone.
5.   (US only) To automatically update your time zone when daylight saving time begins or ends, set the **Shift my UTC offset with daylight saving time (US Only)** toggle to ON before daylight saving time begins.The daylight saving time toggle only works if it is set to ON _during the time shift_. For example, if you had the toggle on but turned it off before daylight saving time ends, we do not automatically update your time zone to standard time. 

* * *

Switching destinations[](https://fivetran.com/docs/destinations#switchingdestinations)
--------------------------------------------------------------------------------------

If you want to migrate to a different type of destination, you should first create a second destination by going to the [Destinations page](https://fivetran.com/dashboard/destinations) and clicking **Add destination**. By request, [Fivetran Support](https://support.fivetran.com/) can copy your connection configurations to a new destination. The new connections will still need to perform an initial sync.Once you have completed the migration, remember to pause the connections for your old destination.

* * *

Supported character sets[](https://fivetran.com/docs/destinations#supportedcharactersets)
-----------------------------------------------------------------------------------------

We only support UTF-8 character set for our destinations.

Thanks for your feedback!

Was this page helpful?
