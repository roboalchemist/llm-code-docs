# Source: https://docs.snowflake.com/en/sql-reference/functions/available_listing_refresh_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# AVAILABLE_LISTING_REFRESH_HISTORY

Returns the past 14 days of refresh history for an available listing or a database mounted from a listing using cross-cloud
auto-fulfillment. The information returned contains replication details for data added to the listing database in each refresh event. This
function is available to consumers of listings who have any privilege on the available listing or mounted database.

## Syntax

```sqlsyntax
AVAILABLE_LISTING_REFRESH_HISTORY(
  OBJECT_TYPE => '<object_type>',
  OBJECT_NAME => '<object_name>' )
```

## Arguments

`OBJECT_TYPE => 'object_type'`
:   Type of the object, either `listing` or `database`.

`OBJECT_NAME => 'object_name'`
:   Name of the object, which can be either the listing’s global name or the mounted database name, depending on the object type.

## Output

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| OBJECT_TYPE | TEXT | Lists the type of Snowflake object. For example, listing. |
| OBJECT_NAME | TEXT | Name of the listing or the mounted database. |
| PHASE | TEXT | Current phase in the replication operation, represented as one phase out of a total of X phases. For example, 2/6. |
| PHASE_NAME | TEXT | Name of the replication phases completed (or in progress) so far.  For the list of phases, see usage notes. |
| PROGRESS | TEXT | PRIMARY_UPLOADING_DATA: Percentage of total bytes replicated.  SECONDARY_DOWNLOADING_METADATA: Percentage of the total number of objects replicated.  SECONDARY_DOWNLOADING_DATA: Percentage of total bytes replicated.  Empty for remaining phases. |
| START_TIME | TIMESTAMP_LTZ | Time when the replication phase began. |
| END_TIME | TIMESTAMP_LTZ | Time when the phase finished, if applicable.  NULL if the phase is in progress or is the terminating phase (`COMPLETED/FAILED/CANCELED`). |
| JOB_UUID | TEXT | Query ID for the refresh job. |
| PRIMARY_SNAPSHOT_TIMESTAMP | TIMESTAMP_LTZ | Timestamp when the primary snapshot was created. |
| ERROR | VARIANT | NULL if the refresh operation is successful. If the refresh operation fails, returns a JSON object that provides detailed information about the error:   *`errorCode`: Error code of the failure.* `errorMessage`: Error message of the failure. |

## Usage notes

* Only returns rows for a role with any privilege on the listing, if the listing is visible to the account.
* When `object_type` is set to `database` (as opposed to `listing`), only rows for roles with any privilege on that database are returned.
* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the function name must be fully-qualified. For more information, see [Information Schema](../info-schema.md).

* Phase list in the order processed:

  1. SECONDARY_SYNCHRONIZING_MEMBERSHIP
  2. SECONDARY_UPLOADING_INVENTORY
  3. PRIMARY_UPLOADING_METADATA
  4. PRIMARY_UPLOADING_DATA
  5. SECONDARY_DOWNLOADING_METADATA
  6. SECONDARY_DOWNLOADING_DATA
  7. COMPLETED / FAILED / CANCELED

## Examples

Retrieve the history for the database `my_mounted_database`.

```sqlexample
SELECT * FROM TABLE(
  INFORMATION_SCHEMA.AVAILABLE_LISTING_REFRESH_HISTORY(
    OBJECT_TYPE=>'database',
    OBJECT_NAME=>'my_mounted_database'
  )
);
```
