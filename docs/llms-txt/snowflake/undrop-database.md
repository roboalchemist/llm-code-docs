# Source: https://docs.snowflake.com/en/sql-reference/sql/undrop-database.md

# UNDROP DATABASE

Restores the most recent version of a dropped database.

See also:
:   [CREATE DATABASE](create-database.md) , [ALTER DATABASE](alter-database.md) , [DESCRIBE DATABASE](desc-database.md) , [DROP DATABASE](drop-database.md) , [SHOW DATABASES](show-databases.md)

## Syntax

```sqlsyntax
UNDROP DATABASE <name>
```

## Parameters

`name`
:   Specifies the identifier for the database to restore. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* If a database with the same name already exists, an error is returned.

* UNDROP relies on the Snowflake [Time Travel](../../user-guide/data-time-travel.md) feature. An object can be restored only if
  the object was deleted within the [Data retention period](../../user-guide/data-time-travel.md). The default value is 24 hours.

* Hybrid tables that belong to the specified database are not undropped.
* If you have multiple dropped databases with the same name, you can use the [IDENTIFIER keyword](../identifier-literal.md)
  with the system-generated identifier (from the [DATABASES view](../account-usage/databases.md)) to specify which database to
  restore. The name of the restored database remains the same. See Examples.

  > **Note:**
  >
  > You can only use the system-generated identifier with the IDENTIFIER() keyword when executing the UNDROP command for notebooks, tables, block storage snapshots, schemas, and databases.

## Examples

### Basic example

Restore the most recent version of a dropped database (this example builds on the [DROP DATABASE](drop-database.md) examples):

```sqlexample
UNDROP DATABASE mytestdb2;
```

```output
+-------------------------------------------+
| status                                    |
|-------------------------------------------|
| Database MYTESTDB2 successfully restored. |
+-------------------------------------------+
```

```sqlexample
SHOW DATABASES HISTORY;
```

```output
+---------------------------------+-----------+------------+------------+--------+--------+---------+---------+----------------+------------+
| created_on                      | name      | is_default | is_current | origin | owner  | comment | options | retention_time | dropped_on |
|---------------------------------+-----------+------------+------------+--------+--------+---------+---------+----------------+------------|
| Tue, 17 Mar 2015 16:57:04 -0700 | MYTESTDB  | N          | Y          |        | PUBLIC |         |         |              1 | [NULL]     |
| Tue, 17 Mar 2015 17:06:32 -0700 | MYTESTDB2 | N          | N          |        | PUBLIC |         |         |              1 | [NULL]     |
| Wed, 25 Feb 2015 17:30:04 -0800 | SALES1    | N          | N          |        | PUBLIC |         |         |              1 | [NULL]     |
| Fri, 13 Feb 2015 19:21:49 -0800 | DEMO1     | N          | N          |        | PUBLIC |         |         |              1 | [NULL]     |
+---------------------------------+-----------+------------+------------+--------+--------+---------+---------+----------------+------------+
```

### UNDROP database using the database ID

Restore a dropped database by ID using IDENTIFIER(). You can find the database ID of the specific database to restore using the
`database_id` column in the [DATABASES view](../account-usage/databases.md). For example, if you have multiple dropped
databases named `my_database`, and you want to restore the second-to-last dropped database `my_database`, follow
these steps:

1. Find the database ID of the dropped database in the Account Usage DATABASES view:

   ```sqlexample
   SELECT database_id,
     database_name,
     created,
     deleted,
     comment
   FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES
   WHERE database_name = 'MY_DATABASE'
   AND deleted IS NOT NULL
   ORDER BY deleted;
   ```

   ```output
   +-------------+---------------+-------------------------------+-------------------------------+---------+
   | DATABASE_ID | DATABASE_NAME | CREATED                       | DELETED                       | COMMENT |
   |-------------+---------------+-------------------------------+-------------------------------+---------|
   |         494 | MY_DATABASE   | 2024-07-01 17:51:33.380 -0700 | 2024-07-01 17:51:46.228 -0700 | NULL    |
   |         492 | MY_DATABASE   | 2024-07-01 17:51:52.560 -0700 | 2024-07-01 17:52:39.881 -0700 | NULL    |
   |         493 | MY_DATABASE   | 2024-07-01 17:52:39.849 -0700 | 2024-07-01 17:52:44.562 -0700 | NULL    |
   +-------------+---------------+-------------------------------+-------------------------------+---------+
   ```

2. Undrop `my_database` by database ID. To restore the second-to-last deleted database, use database ID `492` from the output of
   the previous statement. After you execute the following statement, the database is restored with its original name, `my_database`:

   ```sqlexample
   UNDROP DATABASE IDENTIFIER(492);
   ```
