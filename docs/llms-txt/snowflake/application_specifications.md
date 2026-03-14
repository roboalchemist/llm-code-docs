# Source: https://docs.snowflake.com/en/sql-reference/account-usage/application_specifications.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/application_specifications.md

# APPLICATION_SPECIFICATION view

This Information Schema view displays a row for each app specification request currently defined
in the specified or current database where the information schema is located.

For more information about app specification, see
[Overview of app specifications](../../developer-guide/native-apps/requesting-app-specs.md).

## Columns

The following table provides definitions for the `APPLICATION_SPECIFICATIONS` view columns.

| Column | Data type | Description |
| --- | --- | --- |
| NAME | TEXT | The name of the app specification. |
| APPLICATION_NAME | TEXT | The name of the app that contains the app specification. |
| TYPE | TEXT | The type of app specification. Possible values are EXTERNAL_ACCESS, SECURITY_INTEGRATION, and LISTING. |
| SEQUENCE_NUMBER | NUMBER | The sequence number of the app specification. |
| REQUESTED_ON | TIMESTAMP_LTZ | The timestamp when the app created the app specification. |
| STATUS | TEXT | The status of the app specification. Possible values are: APPROVED, PENDING, or DECLINED. |
| STATUS_UPDATED_ON | TIMESTAMP_LTZ | The timestamp when the app specification was last updated, including when it was created, approved, or declined. |
| LABEL | TEXT | A label containing the name of the app specification that is displayed to consumer in Snowsight. |
| DESCRIPTION | TEXT | A description of the app specification. This description is displayed to the consumer. |
| DEFINITION | TEXT | The fields that comprise the app specification definition. |
