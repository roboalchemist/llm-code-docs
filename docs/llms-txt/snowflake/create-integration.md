# Source: https://docs.snowflake.com/en/sql-reference/sql/create-integration.md

# CREATE INTEGRATION

Creates a new integration in the system or replaces an existing integration. An integration is a Snowflake object that provides an
interface between Snowflake and third-party services.

See also:
:   [ALTER INTEGRATION](alter-integration.md), [DROP INTEGRATION](drop-integration.md), [SHOW INTEGRATIONS](show-integrations.md) , [DESCRIBE INTEGRATION](desc-integration.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] <integration_type> INTEGRATION [ IF NOT EXISTS ] <object_name>
  [ <integration_type_params> ]
  [ COMMENT = '<string_literal>' ]
```

Where `integration_type_params` are specific to the integration type.

For specific syntax, usage notes, and examples, see:

* [CREATE API INTEGRATION](create-api-integration.md)
* [CREATE CATALOG INTEGRATION](create-catalog-integration.md)
* [CREATE EXTERNAL ACCESS INTEGRATION](create-external-access-integration.md)
* [CREATE NOTIFICATION INTEGRATION](create-notification-integration.md)
* [CREATE SECURITY INTEGRATION](create-security-integration.md)
* [CREATE STORAGE INTEGRATION](create-storage-integration.md)

## General usage notes

* `OR REPLACE` and `IF NOT EXISTS` clauses are mutually exclusive; they cannot both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.
