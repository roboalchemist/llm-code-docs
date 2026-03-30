# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-application-set-configuration-definition.md

# ALTER APPLICATION SET CONFIGURATION DEFINITION

Creates or updates an [app configuration](../../developer-guide/native-apps/inter-app-communication.md) for a Snowflake Native App.

> **Note:**
>
> This command can only be used by a Snowflake Native App.

See also:
:   [ALTER APPLICATION DROP CONFIGURATION DEFINITION](alter-application-drop-configuration-definition.md)

## Syntax

```sqlsyntax
ALTER APPLICATION SET CONFIGURATION DEFINITION <config>
  TYPE = {APPLICATION_NAME | STRING}
  LABEL = '<label>'
  DESCRIPTION = '<description>'
  APPLICATION_ROLES = ( <app_role1> [ , <app_role2> ... ] );
```

## Parameters

`config`
:   Identifier for the app configuration.

`TYPE`
:   Specifies the type of app configuration. Supported values are:

    * `APPLICATION_NAME`
    * `STRING`

`LABEL = 'label'`
:   Specifies a label for the app specification to be displayed in the Snowsight.

`DESCRIPTION = 'description'`
:   Specifies a description of the app specification. Snowflake recommends
    including information about the app specification type and why it is
    required by the app.

`APPLICATION_ROLES = ( <app_role1> [ , <app_role2> ... ] )`
:   Specifies the application roles that will have access to the app configuration object.

## Usage notes

* This command can only be used by a Snowflake Native App.
* When creating a configuration definition for the server app name for inter-app communication, you must set the `LABEL` and `DESCRIPTION` parameters to the same values as the `LABEL` and `DESCRIPTION` parameters of the associated `APPLICATION SPECIFICATION` object.
