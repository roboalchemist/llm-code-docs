# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-set-configuration-value.md

# ALTER APPLICATION SET CONFIGURATION VALUE

Sets a value in an [app configuration definition](../../developer-guide/native-apps/inter-app-communication.md) for a Snowflake Native App.

See also:
:   [ALTER APPLICATION SET CONFIGURATION DEFINITION](alter-application-set-configuration-definition.md), [ALTER APPLICATION DROP CONFIGURATION DEFINITION](alter-application-drop-configuration-definition.md)

## Syntax

```sqlsyntax
ALTER APPLICATION <app> SET CONFIGURATION <config> VALUE = '<value>';
```

## Parameters

`app`
:   Identifier for the Snowflake Native App that contains the configuration.

`config`
:   Identifier for the app configuration definition.

`VALUE = 'value'`
:   Specifies the value to set for the app configuration definition.

## Usage notes

* This command can only be used by a consumer. This command cannot be used by the Snowflake Native App itself.
* For a configuration definition of type `APPLICATION_NAME`, the value must be the name of a Snowflake Native App that is installed in the current account.
* In order to set a configuration, the current role must be granted an application role that has access to the configuration (that is, one of the application roles specified in the `APPLICATION_ROLES` field in the `ALTER APPLICATION SET CONFIGURATION DEFINITION` command).
