# Source: https://docs.snowflake.com/en/sql-reference/account-usage/application_configuration_value_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/application_configuration_value_history.md

Categories:

[Table functions](../functions-table.md) (Tables)

# APPLICATION_CONFIGURATION_VALUE_HISTORY

Provides a history of the value changes for [application configurations](../../developer-guide/native-apps/app-configuration.md) in the specified Snowflake Native App.

You can call this function to check the history of the value changes for an application configuration. For information, see
[Application configuration](../../developer-guide/native-apps/app-configuration.md).

## Syntax

```sqlsyntax
APPLICATION_CONFIGURATION_VALUE_HISTORY(
  [ APPLICATION_NAME => '<application_name>' ]
  [ , CONFIGURATION_NAME => '<config_name>' ]
)
```

## Arguments

**Required:**

`application_name`
:   Name of the application that the configuration is in.

**Optional:**

`config_name`
:   Name of the configuration. If not provided, the function returns the history for all configurations in the application.

## Returns

The function returns the following columns:

| Column | Data type | Description |
| --- | --- | --- |
| NAME | STRING | The name of the configuration, defined by the provider. |
| APPLICATION_NAME | STRING | The name of the application that the configuration is in. |
| CREATED_ON | TIMESTAMP | The timestamp when the configuration object was created. |
| UPDATED_ON | TIMESTAMP | The timestamp when the configuration object was last updated. |
| TYPE | STRING | The type of the configuration. Possible values are APPLICATION_NAME and STRING. |
| STATUS | STRING | The status of the configuration. Possible values are PENDING and DONE. |
| SENSITIVE | BOOLEAN | Whether the value is sensitive or not. |
| VALUE | STRING | The value that is set by the consumer.  For application configurations of the APPLICATION_NAME type, this is the most up-to-date name of the application specified by the consumer. This may not be the same as initially provided if the application has been renamed. If the application has been dropped, no value will be shown here, as if the value is not set.  When `SENSITIVE=TRUE`, the value is hidden, unless the executing role is the application owning the configuration. |
| VALUE_UPDATED_ON | TIMESTAMP | The last updated timestamp when the value was set or unset. |
| LABEL | STRING | A user-friendly name to be displayed in the UI, provided by the provider. |
| DESCRIPTION | STRING | The description of the configuration. |
| APPLICATION_ROLES | STRING | The comma-separated app role names that have access to the configuration.  This displays the most up-to-date names, even if roles have been renamed. If an application role has been dropped, it will not be included in the output list. |

## Usage notes

* The view only displays configurations for which the current role for the session has been granted access privileges.
* The view does not include configurations that have been dropped.
* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the function name must be fully-qualified. For more details, see
  [Snowflake Information Schema](../info-schema.md).

## Examples

Retrieve the history of the value changes for the `config_name` application configuration
in the `application_name` application:

```sqlexample
SELECT * FROM TABLE(information_schema.application_configuration_value_history(application_name => 'my_app', configuration_name => 'my_configuration'));
```
