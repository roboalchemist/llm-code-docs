# Source: https://docs.snowflake.com/en/user-guide/tables-iceberg-catalog-linked-database.md

# Use a catalog-linked database for Apache Iceberg™ tables

With a catalog-linked database, you can access multiple remote Iceberg tables
from Snowflake without creating individual [externally managed tables](tables-iceberg.md).

A catalog-linked database is a Snowflake database connected to an external Iceberg REST catalog.
Snowflake automatically syncs with the external catalog to detect namespaces and Iceberg tables,
and registers the remote tables to the catalog-linked database. Catalog-linked databases also support creating and dropping schemas or Iceberg tables.

## Billing for catalog-linked databases

Snowflake bills your account for the following usage:

* Automatic table discovery, create schema, drop schema, and drop table. Snowflake will bill your account for this usage under the
  CREDITS_USED_CLOUD_SERVICES usage type. Usage for
  cloud services is charged only if the daily consumption of cloud services exceeds 10% of the daily usage of virtual warehouses. For more
  information, see [Understanding billing for cloud services usage](cost-understanding-compute.md).
* Create table. Snowflake will bill your account for this usage under the CREDITS_USED_COMPUTE usage type through auto refresh.
  The cost for this usage is described in Table 5 of the [Snowflake service consumption table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf) on the Snowflake website.
  Refer to the Snowflake-managed compute column for the Automated Refresh and Data Registration row.

Snowflake won’t bill you for any cloud services that you use during table creation.

> **Note:**
>
> To view the credit usage for your catalog-linked databases, use the [CATALOG_LINKED_DATABASE_USAGE_HISTORY view](../sql-reference/account-usage/catalog_linked_database_usage_history.md).

## Workflow to configure access to your external catalog and table storage

The following steps cover how to create a catalog-linked database, check the sync status between
Snowflake and your catalog, and create or query a table in the database.

1. Configure access to your external catalog and table storage
2. Create a catalog-linked database
3. Check the catalog sync status
4. Query a table in your catalog-linked database or Write to your remote catalog

## Configure access to your external catalog and table storage

Before you create a catalog-linked database, you need to configure access to
your external catalog and table storage. To configure this access, you configure a catalog integration with vended credentials. With this
option, your remote Iceberg catalog must support credential vending.

For instructions, see [Use catalog-vended credentials for Apache Iceberg™ tables](tables-iceberg-configure-catalog-integration-vended-credentials.md).

> **Note:**
>
> If your remote Iceberg catalog doesn’t support credential vending, you must configure an [external volume](tables-iceberg.md) and a
> [catalog integration](tables-iceberg.md) to configure access to your external catalog and table storage.
> First,
> [configure an external volume for your cloud storage provider](tables-iceberg-configure-external-volume.md). Then,
> [configure a Apache Iceberg™ REST catalog integration for your remote Iceberg catalog](tables-iceberg-configure-catalog-integration-rest.md).

## Create a catalog-linked database

Create a catalog-linked database with the [CREATE DATABASE (catalog-linked)](../sql-reference/sql/create-database-catalog-linked.md) command:

The following example creates a catalog-linked database that uses vended credentials. The sync interval is 30 seconds, which is the default.
The sync interval tells Snowflake how often to poll your remote catalog.

```sqlexample
CREATE DATABASE my_linked_db
  LINKED_CATALOG = (
    CATALOG = 'my_catalog_int'
  );
```

> **Note:**
>
> To create a catalog-linked database that uses an external volume, see [CREATE DATABASE (catalog-linked)](../sql-reference/sql/create-database-catalog-linked.md), including
> the [example](../sql-reference/sql/create-database-catalog-linked.md).

Your catalog-linked database includes a link icon.

## Check the configuration of a catalog-linked database

After you create a catalog-linked database, use the [SYSTEM$GET_CATALOG_LINKED_DATABASE_CONFIG](../sql-reference/functions/system_get_catalog_linked_database_config.md) function to
check the configuration for the database.

```sqlexample
SELECT SYSTEM$GET_CATALOG_LINKED_DATABASE_CONFIG('my_linked_db');
```

## Check the catalog sync status

To check whether Snowflake has successfully linked your remote catalog to your database, use the [SYSTEM$CATALOG_LINK_STATUS](../sql-reference/functions/system_catalog_link_status.md)
function.

The function also provides information to help you identify tables in the remote catalog that fail to sync.

```sqlexample
SELECT SYSTEM$CATALOG_LINK_STATUS('my_linked_db');
```

### Identify tables that were created but couldn’t be initialized

To identify tables in the remote catalog that synced successfully but fail to refresh automatically, run the [SHOW ICEBERG TABLES](../sql-reference/sql/show-iceberg-tables.md)
command, and then refer to the `auto_refresh_status` column in the output. These tables
have an `executionState` of `ICEBERG_TABLE_NOT_INITIALIZED` in the output.

For example, Snowflake might successfully discover and create a table in your remote catalog to your catalog-linked database, but this
table has a corrupted data file in your remote catalog. As a result, Snowflake can’t automatically refresh the table until you resolve
the error.

Automated refresh is turned off for these kinds of tables, so querying the table in Snowflake returns an error that says the
table was never initialized. To query the table, you must fix the error, and then [turn on automated refresh for the table](tables-iceberg-auto-refresh.md).

## Query a table in your catalog-linked database

After you create a catalog-linked database, Snowflake starts the table discovery process and
automatically polls your linked catalog using the value of the SYNC_INTERVAL_SECONDS parameter (with a default interval of 30 seconds) to check for changes.

In the database, allowed namespaces from the remote catalog appear as schemas, and Iceberg tables appear under their respective schemas.

You can query the remote tables by using a SELECT statement.

> **Note:**
>
> For the requirements for identifying objects in a catalog-linked database, see Requirements for identifier resolution in a catalog-linked database.
>
> For more information about object identifiers, see [Identifier requirements](../sql-reference/identifiers-syntax.md).

For example:

```sqlexample
USE DATABASE my_linked_db;

SELECT * FROM my_namespace.my_iceberg_table
  LIMIT 20;
```

## Write to your remote catalog

You can use Snowflake to create namespaces and Iceberg tables in your linked catalog. For more information, see the
following topics:

* [Write support for externally managed Apache Iceberg™ tables](tables-iceberg-externally-managed-writes.md)
* [Use CREATE SCHEMA to create namespaces in your external catalog](tables-iceberg-externally-managed-writes.md)
* [Create an Iceberg table in a catalog-linked database](tables-iceberg-externally-managed-writes.md)

## Requirements for identifier resolution in a catalog-linked database

The requirement for resolving an identifier depends on the following:

* The value that you specified for the CATALOG_CASE_SENSITIVITY parameter when you
  [created your catalog-linked database](../sql-reference/sql/create-database-catalog-linked.md)
* Whether your external Iceberg catalog uses case-sensitive or case-insensitive identifiers.

> **Note:**
>
> * These requirements apply to identifying existing schemas, tables, and table columns. They also include some special cases for
>   creating or altering an object.
> * When you create a new
>   schema, table, or column in a case-sensitive catalog such as AWS Glue or Unity Catalog, you must use lowercase letters and surround
>   the schema, table, and column names in double quotes. This is also required for other Iceberg REST catalogs that only support
>   lowercase identifiers.

The following table shows the requirement for each scenario:

| CATALOG_CASE_SENSITIVITY value | External Iceberg catalog uses | Requirement |
| --- | --- | --- |
| CASE_SENSITIVE | Case sensitive identifiers | Snowflake matches identifiers exactly as they appear, including case. Snowflake automatically converts unquoted identifiers to uppercase, but quoted identifiers must match exactly the case in your external catalog.  The following example shows a valid query for creating a table:  ```sqlexample CREATE TABLE "Table1" (id INT, name STRING);```  Snowflake creates the table in the external catalog as `Table1`, which preserves the capitalization you used. Note that you can also create a lowercase `table1` table, if needed.  The following example shows a valid query for selecting the `Table1` table:  ```sqlexample SELECT * FROM "Table1";```  In the previous example, the double quotes are required for matching the capitalization exactly.  The following example shows an invalid query, unless a `TABLE1` table exists:  ```sqlexample SELECT * FROM table1;```  In the previous example, the query is invalid if `TABLE1` doesn’t exist because the identifier isn’t surrounded with double quotes. As a result, Snowflake converts the identifier to uppercase.  The following example shows an invalid query for the case when an all uppercase `TABLE1` doesn’t exist:  ```sqlexample SELECT * FROM TABLE1;``` |
| CASE_SENSITIVE | Case insensitive identifiers | If the external Iceberg catalog is actually case insensitive, and normalizes to lowercase, you must surround identifiers in double quotes.  The following example shows valid queries:  ```sqlexample SELECT * from "s1"; SELECT * from "lowercasetablename";``` |
| CASE_INSENSITIVE | Case insensitive identifiers | *If your case insensitive catalog has a lowercase `table1` table, all of the following queries are valid:  ```sqlexample   SELECT * from table1;   SELECT * from TABLE1;   SELECT * from Table1;   SELECT * from "table1";```* For any of the following commands, you must surround the schema, table, and column names in double quotes:    + CREATE ICEBERG TABLE   + CREATE SCHEMA   + ALTER ICEBERG TABLE ADD COLUMN   + ALTER ICEBERG TABLE RENAME COLUMN |
| CASE_INSENSITIVE | Case sensitive identifiers | If the external Iceberg catalog is actually case sensitive, Snowflake treats unquoted identifiers as case-insensitive and automatically converts unquoted identifiers to uppercase. When you create or query objects, Snowflake matches identifiers regardless of case, as long as they are unquoted.  Using this pattern is discouraged because Snowflake can’t resolve two different identifiers that differ in casing. This pattern only works when no two identifiers are different in casing only.  Consider the case where the remote catalog has a `Table1` table. All of the following queries are valid for querying that table.  ```sqlexample SELECT * from table1; SELECT * from TABLE1; SELECT * from Table1; SELECT * from "Table1";```  Quoted identifiers preserve case and match exactly. However, in CASE_INSENSITIVE mode, unquoted and quoted forms are both supported. |

## Considerations for using a catalog-linked database for Iceberg tables

Consider the following items when you use a catalog-linked database:

* Supported only when you use a catalog integration for Iceberg REST (for example, Snowflake Open Catalog).
* To limit automatic table discovery to a specific set of namespaces, use the ALLOWED_NAMESPACES parameter. You can also use the
  BLOCKED_NAMESPACES parameter to block a set of namespaces.
* Snowflake doesn’t sync remote catalog access control for users or roles.
* You can create schemas, externally managed Iceberg tables, or database roles in a catalog-linked database. Creating other Snowflake objects
  isn’t currently supported.
* When you create a catalog-linked database, you can’t specify the default Iceberg version or merge-on-read behavior to use for
  Iceberg tables.

  However, you can modify these properties for an existing database by using the [ALTER DATABASE (catalog-linked)](../sql-reference/sql/alter-database-catalog-linked.md)
  command to set the following parameters:

  * ICEBERG_VERSION_DEFAULT
  * ENABLE_ICEBERG_MERGE_ON_READ
* For Iceberg tables in a catalog-linked database:

  * Snowflake doesn’t copy remote catalog table properties, such as retention policies or buffers, and doesn’t currently support altering table properties.
  * [Automated refresh](tables-iceberg-auto-refresh.md) is enabled by default. If the `table-uuid` of an external table
    and the catalog-linked database table don’t match, refresh fails and Snowflake drops the table from the catalog-linked database; Snowflake doesn’t change the remote table.
  * If you drop a table from the remote catalog, Snowflake drops the table from the catalog-linked database.
    This action is asynchronous, so you might not see the change in the remote catalog right away.
  * If you rename a table in the remote catalog, Snowflake drops the existing table from the catalog-linked database and creates a table with the new name.
  * Masking policies and tags are supported. Other Snowflake-specific features, including replication and cloning, aren’t supported.
  * The character that you choose for the NAMESPACE_FLATTEN_DELIMITER parameter can’t appear in your remote namespaces. During the auto discovery process,
    Snowflake skips any namespace that contains the delimiter, and doesn’t create a corresponding schema in your catalog-linked database.
  * If you specify anything other than `_`, `$`, or numbers for the NAMESPACE_FLATTEN_DELIMITER parameter,
    you must put the schema name in quotes when you query the table.
  * For databases linked to AWS Glue, you must use lowercase letters and surround the schema, table, and column names in double quotes.
    This is also required for other Iceberg REST catalogs that only support lowercase identifiers.

    The following example shows a valid query:

    ```sqlexample
    CREATE SCHEMA "s1";
    ```

    The following statements aren’t valid, because they use uppercase letters or omit the double quotes:

    ```sqlexample
    CREATE SCHEMA s1;
    CREATE SCHEMA "Schema1";
    ```

  * Using UNDROP ICEBERG TABLE isn’t supported.
  * Sharing:

    * Sharing with a listing isn’t currently supported
    * Direct sharing is supported
* For writing to tables in a catalog-linked database:

  * Creating tables in nested namespaces isn’t currently supported.
  * Writing to tables in nested namespaces isn’t currently supported.
  * Position [row-level deletes](https://iceberg.apache.org/spec/#row-level-deletes) are supported for tables stored
    on Amazon S3, Azure, or Google Cloud. Row-level deletes with equality delete files aren’t supported. For more information about row-level deletes,
    see [Use row-level deletes](tables-iceberg-manage.md). To turn off position deletes, which enable
    running the Data Manipulation Language (DML) operations in copy-on-write mode, set the `ENABLE_ICEBERG_MERGE_ON_READ` parameter to FALSE at the table, schema, or
    database level.
