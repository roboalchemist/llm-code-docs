# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-integration.md

# ALTER INTEGRATION

Modifies the properties for an existing integration.

See also:
:   [CREATE INTEGRATION](create-integration.md), [DROP INTEGRATION](drop-integration.md), [SHOW INTEGRATIONS](show-integrations.md) , [DESCRIBE INTEGRATION](desc-integration.md)

## Syntax

```sqlsyntax
ALTER <integration_type> INTEGRATION <object_name> <actions>
```

Where `actions` are specific to the object type.

For specific syntax, usage notes, and examples, see:

* [ALTER API INTEGRATION](alter-api-integration.md)
* [ALTER CATALOG INTEGRATION](alter-catalog-integration.md)
* [ALTER EXTERNAL ACCESS INTEGRATION](alter-external-access-integration.md)
* [ALTER NOTIFICATION INTEGRATION](alter-notification-integration.md)
* [ALTER SECURITY INTEGRATION](alter-security-integration.md)
* [ALTER STORAGE INTEGRATION](alter-storage-integration.md)
