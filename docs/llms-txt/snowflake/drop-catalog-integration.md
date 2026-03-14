# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-catalog-integration.md

# DROP CATALOG INTEGRATION

Removes a [catalog integration](../../user-guide/tables-iceberg.md) from the account.

See also:
:   [CREATE CATALOG INTEGRATION](create-catalog-integration.md) , [ALTER CATALOG INTEGRATION](alter-catalog-integration.md) , [SHOW CATALOG INTEGRATIONS](show-catalog-integrations.md) , [DESCRIBE CATALOG INTEGRATION](desc-catalog-integration.md)

## Syntax

```sqlsyntax
DROP CATALOG INTEGRATION [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the catalog integration to drop. If the identifier contains spaces, special characters,
    or mixed-case characters, the entire string must be enclosed in double quotes. Identifiers enclosed
    in double quotes are also case-sensitive (for example, `"My Catalog"`).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Integration (catalog) | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Dropped catalog integrations cannot be recovered; they must be recreated.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

* You can’t drop or replace a catalog integration if one or more Apache Iceberg™ tables
  are associated with the catalog integration.

  To view the tables that depend on a catalog integration,
  you can use the [SHOW ICEBERG TABLES](show-iceberg-tables.md) command and
  a query using the [pipe operator](../operators-flow.md) (`->>`) that filters on
  the `catalog_name` column.

  > **Note:**
  >
  > The column identifier (`catalog_name`) is case-sensitive.
  > Specify the column identifier exactly as it appears in the SHOW ICEBERG TABLES output.

  For example:

  ```sqlexample
  SHOW ICEBERG TABLES
    ->> SELECT *
          FROM $1
          WHERE "catalog_name" = 'my_catalog_integration_1';
  ```

## Examples

Drop a catalog integration:

> ```sqlexample
> DROP CATALOG INTEGRATION myInt;
> ```

Drop the catalog integration again, but don’t raise an error if the integration doesn’t exist:

> ```sqlexample
> DROP CATALOG INTEGRATION IF EXISTS myInt;
> ```
