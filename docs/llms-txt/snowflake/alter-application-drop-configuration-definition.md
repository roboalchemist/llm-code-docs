# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-drop-configuration-definition.md

# ALTER APPLICATION DROP CONFIGURATION DEFINITION

Deletes the [app configuration definition](../../developer-guide/native-apps/inter-app-communication.md) for a Snowflake Native App.

> **Note:**
>
> This command can only be used by a Snowflake Native App.

See also:
:   [ALTER APPLICATION SET CONFIGURATION DEFINITION](alter-application-set-configuration-definition.md)

## Syntax

```sqlsyntax
ALTER APPLICATION DROP CONFIGURATION DEFINITION {config};
```

## Parameters

`config`
:   Identifier for the app configuration definition.
