# Source: https://docs.snowflake.com/en/sql-reference/account-usage/application_specification_status_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/application_specification_status_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# APPLICATION_SPECIFICATION_STATUS_HISTORY

Returns information about the history of the
[status changes for app specifications](../../developer-guide/native-apps/ui-consumer-app-spec.md) in your Snowflake account.

## Syntax

```sqlsyntax
APPLICATION_SPECIFICATION_STATUS_HISTORY(
  [ APPLICATION_NAME => '<application_name>' ]
  [ , SPECIFICATION_NAME => '<specification_name>'])
  [ LIMIT => <number_of_rows> ]
```

## Arguments

`APPLICATION_NAME => 'application_name'`
:   The name of the application for which to retrieve specification status history. If not specified,
    returns status history for all app specifications.

`SPECIFICATION_NAME => 'specification_name'`
:   The name of the app specification for which to retrieve status history. If not specified, returns
    status history for all app specifications.

`LIMIT <number_of_rows>`
:   The maximum number of rows to return.

## Usage notes

* This function only returns rows for app specifications that current role has privileges to view.
* This function only returns rows for app specifications in the current account.

## Output

The APPLICATION_SPECIFICATION table function produces one row for each app specification.
Each row contains the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| NAME | TEXT | The name of the app specification. |
| APPLICATION_NAME | TEXT | The name of the app that contains the app specification |
| SEQUENCE_NUMBER | NUMBER | The sequence number of the app specification. |
| REQUESTED_ON | TIMESTAMP_TZ | The date and time when the app created the app specification. |
| USER_NAME | TEXT | The user that updated the app specification. This value is empty if it is a new pending request created by the application. |
| STATUS | TEXT | The status of the app specification. One of the following values: : `PENDING`, `APPROVED`, `DECLINED`. |
| STATUS_UPDATED_ON | TIMESTAMP_TZ | The date and time when the app specification was last modified. |
| LABEL | TEXT | The label associated with the app specification status change, if any. |
| DESCRIPTION | TEXT | The description associated with the app specification status change, if any. |
| DEFINITION | TEXT | The fields that comprise the app specification definition. For more information, see [Overview of app specifications](../../developer-guide/native-apps/requesting-app-specs.md). |

## Example

```sqlexample
SELECT *
FROM TABLE(
    INFORMATION_SCHEMA.APPLICATION_SPECIFICATION_STATUS_HISTORY(
        application_name=>'my_app',
        specification_name=>'eai_spec'))
    LIMIT 5;
```

The preceding example returns the last five status changes for the app specification named `my_spec` in the app named `my_app`.
