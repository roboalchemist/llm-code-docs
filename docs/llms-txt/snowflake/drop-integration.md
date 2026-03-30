# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-integration.md

# DROP INTEGRATION

Removes an integration from the account.

See also:
:   [CREATE INTEGRATION](create-integration.md) , [ALTER INTEGRATION](alter-integration.md) , [SHOW INTEGRATIONS](show-integrations.md) , [DESCRIBE INTEGRATION](desc-integration.md)

API integrations:
:   [CREATE API INTEGRATION](create-api-integration.md)

catalog integrations:
:   [CREATE CATALOG INTEGRATION](create-catalog-integration.md)

External access integrations:
:   [CREATE EXTERNAL ACCESS INTEGRATION](create-external-access-integration.md)

Notification integrations:
:   [CREATE NOTIFICATION INTEGRATION](create-notification-integration.md)

Security integrations:
:   [CREATE SECURITY INTEGRATION](create-security-integration.md)

Storage integrations:
:   [CREATE STORAGE INTEGRATION](create-storage-integration.md)

## Syntax

```sqlsyntax
DROP [ { API | CATALOG | EXTERNAL ACCESS | NOTIFICATION | SECURITY | STORAGE } ] INTEGRATION [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the integration to drop. If the identifier contains spaces, special characters, or mixed-case characters,
    the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive
    (e.g. `"My Object"`).

`API | CATALOG | EXTERNAL ACCESS | NOTIFICATION | SECURITY | STORAGE`
:   Specifies the integration type.

## Usage notes

* Dropped integrations cannot be recovered; they must be recreated.
* Disabling or dropping the integrations may not take effect immediately, since integrations may be cached.
  It is recommended to remove the integration privilege from the cloud provider to take effect sooner.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop an integration:

> ```sqlexample
> SHOW INTEGRATIONS LIKE 't2%';
>
> DROP INTEGRATION t2;
>
> SHOW INTEGRATIONS LIKE 't2%';
> ```

Drop the integration again, but don’t raise an error if the integration does not exist:

> ```sqlexample
> DROP INTEGRATION IF EXISTS t2;
> ```
