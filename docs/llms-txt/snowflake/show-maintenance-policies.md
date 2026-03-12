# Source: https://docs.snowflake.com/en/sql-reference/sql/show-maintenance-policies.md

# SHOW MAINTENANCE POLICIES

Lists the [maintenance policies](../../developer-guide/native-apps/consumer-maintenance-policies.md) applied to the specified account or app.

See also:
:   [CREATE MAINTENANCE POLICY](create-maintenance-policy.md), [ALTER MAINTENANCE POLICY](alter-maintenance-policy.md), [DROP MAINTENANCE POLICY](drop-maintenance-policy.md)

## Syntax

```sqlsyntax
SHOW MAINTENANCE POLICIES { ON | IN } { ACCOUNT | APPLICATION <app_name> | <entity_type> <entity_name> }
```

`ACCOUNT`
:   Shows the maintenance policies applied to the account.

`APPLICATION <app_name>`
:   Shows the maintenance policies applied to the specified app.

## Parameters

`{ ON | IN }`
:   Specifies the scope of the command. Specify one of the following:

    `ACCOUNT`
    :   Returns records for the entire account.

    `APPLICATION app_name`
    :   Returns records for the specified app.

    `IN entity_type entity_name`
    :   Returns records for the specified entity. Specify one of the following for the `entity_type`:

        * `DATABASE`
        * `APPLICATION PACKAGE`
        * `SCHEMA`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| APPLY MAINTENANCE POLICY | Account |  |
| OWNERSHIP | Maintenance policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

## Examples

The following example shows all maintenance policies applied to the account:

```sqlexample
SHOW MAINTENANCE POLICIES ON ACCOUNT;
```

Show maintenance policies for a specific app:

```sqlexample
SHOW MAINTENANCE POLICIES ON APPLICATION my_app;
```

Show maintenance policies for a specific database:

```sqlexample
SHOW MAINTENANCE POLICIES IN DATABASE my_database;
```

Show maintenance policies for a specific app package:

```sqlexample
SHOW MAINTENANCE POLICIES IN APPLICATION PACKAGE my_app_package;
```

Show maintenance policies for a specific schema:

```sqlexample
SHOW MAINTENANCE POLICIES IN SCHEMA my_schema;
```
