# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-model-monitor.md

# DROP MODEL MONITOR

Removes the specified [model monitor](../../developer-guide/snowflake-ml/model-registry/model-observability.md) from the
current or specified schema. Dropped monitors cannot be recovered; they must be recreated.

See also:
:   [CREATE MODEL MONITOR](create-model-monitor.md),
    [ALTER MODEL MONITOR](alter-model-monitor.md),
    [SHOW MODEL MONITORS](show-model-monitors.md),
    [DESCRIBE MODEL MONITOR](desc-model-monitor.md)

## Syntax

```sqlsyntax
DROP MODEL MONITOR [ IF EXISTS ] <monitor_name>;
```

## Parameters

`monitor_name`
:   Specifies the identifier for the model monitor to drop. If the identifier contains spaces, special characters, or
    mixed-case characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are
    also case-sensitive.

    If the model identifier is not fully qualified (in the form of `db_name.schema_name.monitor_name` or
    `schema_name.monitor_name`)), the command looks for the model in the current schema for the session.

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Model monitor | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

## Usage notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.
