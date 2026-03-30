# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-drop-app-spec.md

# ALTER APPLICATION DROP SPECIFICATION

Drops an app specification from an app.

> **Note:**
>
> This command can only be used by a Snowflake Native App.

See also:
:   [ALTER APPLICATION SET SPECIFICATION](alter-application-set-app-spec.md), [ALTER APPLICATION … { APPROVE | DECLINE} SPECIFICATION](alter-application-sequence-number.md)

## Syntax

```sqlsyntax
ALTER APPLICATION DROP SPECIFICATION <app_spec_name>;
```

## Parameters

`app_spec_name`
:   The name of the app specification.
