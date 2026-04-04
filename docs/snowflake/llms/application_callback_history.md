# Source: https://docs.snowflake.com/en/sql-reference/account-usage/application_callback_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/application_callback_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# APPLICATION_CALLBACK_HISTORY

Returns information about the history of
[callback](../../developer-guide/native-apps/callbacks.md) invocations for Snowflake Native Apps in your Snowflake account.
Each row represents a callback invocation, including the callback type, execution mode, state, and any error information.

## Syntax

```sqlsyntax
APPLICATION_CALLBACK_HISTORY(
  [ APPLICATION_NAME => '<application_name>' ]
  [ , CALLBACK_TYPE => '<callback_manifest_name>' ]
  [ , LIMIT => <number> ]
)
```

## Optional arguments

`APPLICATION_NAME => 'application_name'`
:   The name of the app for which to retrieve callback history. If not specified, returns
    history for all apps in the account.

`CALLBACK_TYPE => 'callback_manifest_name'`
:   The callback type as defined in the manifest file. If not specified, returns
    history for all callback types in the specified app.

`LIMIT => number`
:   The maximum number of rows to return. Default is 100. Maximum is 10000.

## Usage notes

* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the function name must be fully-qualified. For more details, see
  [Snowflake Information Schema](../info-schema.md).
* The `QUERY_TEXT` and `ERROR_MESSAGE` columns are redacted unless the caller is the app itself.
* Using this function requires one of the following:

  * OWNERSHIP on the app.
  * MONITOR privilege on the app.
  * Running as the app itself.

## Output

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| TYPE | VARCHAR | The callback type as defined in the manifest file. |
| EXECUTION_MODE | VARCHAR | The execution mode of the callback. Possible values are: `SYNC`, `ASYNC`. |
| APPLICATION_NAME | VARCHAR | The name of the app that defines the callback. |
| STATE | VARCHAR | The state of the callback execution. See Callback states. |
| STARTED_ON | TIMESTAMP_LTZ | The timestamp when the callback was invoked. |
| COMPLETED_ON | TIMESTAMP_LTZ | The completion timestamp. NULL if the callback has not yet completed. |
| TRIGGERING_QUERY_ID | VARCHAR | The query ID of the SQL statement that triggered the callback. NULL if the callback was not triggered by a SQL query (for example, when triggered after an upgrade completes). |
| QUERY_ID | VARCHAR | The query ID of the callback procedure execution. NULL if the callback has not yet completed. |
| QUERY_TEXT | VARCHAR | The procedure call SQL text. NULL if the callback has not yet completed. This column is redacted unless the caller is the app itself. |
| ERROR_CODE | VARCHAR | The error code. NULL unless STATE is `FAILED` or `ABORTED`. |
| ERROR_MESSAGE | VARCHAR | The error message. NULL unless STATE is `FAILED` or `ABORTED`. This column is redacted unless the caller is the app itself. |

## Callback states

The following table describes the possible values for the STATE column:

| State | Applies to | Description |
| --- | --- | --- |
| `QUEUED` | Async only | The callback is waiting to be scheduled. |
| `SCHEDULED` | Async only | The callback has been scheduled and is waiting to be executed. |
| `EXECUTING` | Async / Sync | The callback procedure is currently running. |
| `COMPLETED` | Async / Sync | The callback procedure finished successfully. |
| `FAILED` | Async / Sync | The callback procedure failed validation (for example, wrong signature) or execution. |
| `ABORTED` | Async only | An internal scheduling error occurred. This state requires support intervention. |

## Examples

Retrieve the callback history for a specific application:

```sqlexample
SELECT *
FROM TABLE(
    INFORMATION_SCHEMA.APPLICATION_CALLBACK_HISTORY(
        APPLICATION_NAME => 'my_app'));
```

Retrieve the callback history for a specific callback type with a custom limit:

```sqlexample
SELECT *
FROM TABLE(
    INFORMATION_SCHEMA.APPLICATION_CALLBACK_HISTORY(
        APPLICATION_NAME => 'my_app',
        CALLBACK_TYPE => 'after_configuration_change',
        LIMIT => 100));
```
