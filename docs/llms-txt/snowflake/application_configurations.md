# Source: https://docs.snowflake.com/en/sql-reference/info-schema/application_configurations.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/application_configurations.md

# APPLICATION_CONFIGURATIONS view

This Account Usage view displays a row for each application configuration currently defined in the specified or current database where the account usage schema is located.

For more information about application configuration, see [Application configuration](../../developer-guide/native-apps/app-configuration.md).

## Columns

The following table provides definitions for the `APPLICATION_CONFIGURATIONS` view columns.

| Column | Data type | Description |
| --- | --- | --- |
| ID | NUMBER | The system-generated ID for the application configuration. |
| NAME | STRING | The name of the configuration. |
| APPLICATION_ID | NUMBER | The system-generated ID for the application that the configuration is in. |
| APPLICATION_NAME | STRING | The name of the application that the configuration is in. |
| CREATED_ON | TIMESTAMP | The timestamp when the configuration object was created. |
| MODIFIED_ON | TIMESTAMP | The timestamp when the configuration object was last updated. |
| DELETED_ON | TIMESTAMP | The timestamp when the configuration object was deleted. |
| TYPE | STRING | The type of the configuration. Possible values are APPLICATION_NAME and STRING. |
| STATUS | STRING | The status of the configuration. Possible values are PENDING and DONE. |
| SENSITIVE | BOOLEAN | Whether the value is sensitive or not. |
| VALUE | STRING | The value that is set by the consumer.  For application configurations of the APPLICATION_NAME type, this is the most up-to-date name of the application specified by the consumer. This may not be the same as initially provided if the application has been renamed. If the application has been dropped, no value will be shown here, as if the value is not set.  When `SENSITIVE=TRUE`, the value is hidden, unless the executing role is the application owning the configuration. |
| VALUE_UPDATED_ON | TIMESTAMP | The last updated timestamp when the value was set or unset. |
| LABEL | STRING | A user-friendly name to be displayed in the UI, provided by the provider. |
| DESCRIPTION | STRING | The description of the configuration. |
| APPLICATION_ROLES | STRING | The comma-separated app role names that have access to the configuration.  This displays the most up-to-date names, even if roles have been renamed. If an application role has been dropped, it will not be included in the output list. |

## Usage notes

* The retention time for deleted app configurations is 365 days. Data older than 365 days will not be available in the view.

## Examples

Retrieve all listings in the current account:

```sqlexample
SELECT * FROM SNOWFLAKE.ACCOUNT_USAGE.APPLICATION_CONFIGURATIONS;
```
