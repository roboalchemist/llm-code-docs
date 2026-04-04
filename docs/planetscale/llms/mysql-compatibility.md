# Source: https://planetscale.com/docs/vitess/troubleshooting/mysql-compatibility.md

# Source: https://planetscale.com/docs/vitess/mysql-compatibility.md

# MySQL compatibility

> PlanetScale's Vitess product is built on top of open-source Vitess, a database clustering system for horizontal scaling of MySQL. Consequently, PlanetScale is only compatible with MySQL databases.

## Overview

PlanetScale databases run on MySQL 8. If you're [importing an existing database](/docs/vitess/imports/database-imports), PlanetScale supports MySQL database versions `5.7` through `8.0`.

New PlanetScale databases are created on MySQL 8 with character set `utf8mb4_0900_ai_ci`. PlanetScale supports `utf8`, `utf8mb4`, and `utf8mb3`, character sets. We also support `latin1` and `ascii` character sets, but do not recommend them.

## MySQL compatibility limitations

The following reference guide will cover some MySQL syntax, features, and more that PlanetScale either does not support or has limitations around. We are actively working on driving up compatibility, but it's an ongoing effort and will take some time to complete. See this [project board on GitHub](https://github.com/vitessio/docs/vitess/projects/4) to learn what the Vitess team is currently focusing on.

If you're attempting to import a database using our Import tool, there are some additional requirements that you can find in our [Database imports documentation](/docs/vitess/imports/database-imports#import-limitations).

### Queries, functions, syntax, data types, and SQL modes

<Note>
  <Icon icon="exclamation" color="orange" /> = *Limitations in support*

  <Icon icon="xmark" color="red" /> = *Not supported*
</Note>

| Statement                     | Support                           | Description                                                                                                                                                                                                                                                |
| ----------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ALTER TABLE...RENAME COLUMN` | <Icon icon="xmark" color="red" /> | Renaming columns and tables may be destructive. See our [guide for column rename recommendations](/docs/vitess/schema-changes/handling-table-and-column-renames).                                                                                          |
| `CREATE DATABASE`             | <Icon icon="xmark" color="red" /> | You cannot `CREATE` a PlanetScale database from the MySQL command line, however, this is supported in the [PlanetScale CLI](/docs/cli/database).                                                                                                           |
| `DROP DATABASE`               | <Icon icon="xmark" color="red" /> | You cannot `DROP` a PlanetScale database from the MYSQL command line, however, this is supported in the [PlanetScale CLI](/docs/cli/database).                                                                                                             |
| `JSON_TABLE`                  | <Icon icon="xmark" color="red" /> | The [`JSON_TABLE` function](https://dev.mysql.com/doc/refman/8.0/en/json-table-functions.html#function_json-table) is not yet supported. All other [JSON SQL functions](https://dev.mysql.com/doc/refman/8.0/en/json-function-reference.html) should work. |
| `PROCEDURE`                   | <Icon icon="xmark" color="red" /> | We do not support any form of [stored routines](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html).                                                                                                                                             |
| `FUNCTION`                    | <Icon icon="xmark" color="red" /> | We do not support any form of [stored routines](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html).                                                                                                                                             |
| `TRIGGER`                     | <Icon icon="xmark" color="red" /> | We do not support any form of [stored routines](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html).                                                                                                                                             |
| `EVENT`                       | <Icon icon="xmark" color="red" /> | We do not support any form of [stored routines](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html).                                                                                                                                             |
| `LOAD DATA INFILE`            | <Icon icon="xmark" color="red" /> | Loading data via [`LOAD DATA INFILE` is not supported](https://github.com/vitessio/docs/vitess/issues/2976).                                                                                                                                               |
| `KILL`                        | <Icon icon="xmark" color="red" /> | We do not support killing queries or shards from the command line.                                                                                                                                                                                         |
| `:=`                          | <Icon icon="xmark" color="red" /> | The `:=` assignment operator is not yet supported.                                                                                                                                                                                                         |
| `SET GLOBAL time_zone`        | <Icon icon="xmark" color="red" /> | The global time zone is set to UTC and can not be modified.                                                                                                                                                                                                |
| `SET GLOBAL sql_mode`         | <Icon icon="xmark" color="red" /> | The global SQL mode can not be changed permanently. Set each new session's mode instead with `SET sql_mode`.                                                                                                                                               |
| `PIPES_AS_CONCAT`             | <Icon icon="xmark" color="red" /> | Enabling this SQL mode can interfere with Vitess' evalengine parsing the SQL queries so enabling it may result in incorrect or unexpected results. Please use MySQL's standard dialect instead, e.g. `CONCAT()`.                                           |
| `ANSI_QUOTES`                 | <Icon icon="xmark" color="red" /> | Enabling this SQL mode can interfere with Vitess' evalengine parsing the SQL queries so enabling it may result in incorrect or unexpected results. Please use MySQL's standard quotation instead.                                                          |
| `WITH RECURSIVE`              | <Icon icon="xmark" color="red" /> | Experimental support for recursive common table expressions (CTEs) was introduced in Vitess 21 for `SELECT` queries.                                                                                                                                       |

## Miscellaneous

| Action                        | Support                                    | Description                                                                                                                                                                                                                               |
| ----------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Empty schemas**             | <Icon icon="xmark" color="red" />          | Databases with empty schemas are invalid. You cannot deploy a schema change to production if no tables exist.                                                                                                                             |
| **Non-InnoDB Storage engine** | <Icon icon="xmark" color="red" />          | We only support [InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html) storage engine.                                                                                                                              |
| **No applicable unique key**  | <Icon icon="xmark" color="red" />          | We require all tables have a [unique, non-null key](/docs/vitess/schema-changes/onlineddl-change-unique-keys) and that respective covered columns are shared between old and new schema.                                                  |
| **Direct DDL**                | <Icon icon="xmark" color="red" />          | We do [not allow Direct DDL](/docs/vitess/schema-changes/how-online-schema-change-tools-work) on production branches when [safe migrations](/docs/vitess/schema-changes/safe-migrations) is enabled. This includes `TRUNCATE` statements. |
| **Binary log access**         | <Icon icon="xmark" color="red" />          | PlanetScale does not currently support binlog replication to external databases.                                                                                                                                                          |
| **Large JSON documents**      | <Icon icon="exclamation" color="orange" /> | MySQL supports JSON documents up to 1 GB in size. However, we do not recommend to store more than a few MB in a JSON document for performance reasons.                                                                                    |

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt