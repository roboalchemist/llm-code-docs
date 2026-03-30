# Source: https://docs.snowflake.com/en/sql-reference/stored-procedures/system_cancel_classify_schema.md

# SYSTEM$CANCEL_CLASSIFY_SCHEMA

Schedules the cancellation of the classification process for the tables in the specified schema. You can cancel the classification process
for tables that the role used to call this stored procedure can access.

A table that is staged to have the classification process canceled is not classified until you classify the table again.

## Syntax

```sqlsyntax
SYSTEM$CANCEL_CLASSIFY_SCHEMA( '<object_name>' )
```

## Arguments

`object_name`
:   The name of the schema containing the tables to have the classification process cancelled. If a database and schema are not in use in the
    current session, the name must be fully-qualified.

    The name must be specified exactly as it is stored in the database. If the name contains special characters, capitalization, or blank
    spaces, the name must be enclosed first in double-quotes and then in single quotes.

## Returns

The stored procedure returns a JSON object in the following formats depending on the specified schema name:

* If you call [SYSTEM$CLASSIFY_SCHEMA](system_classify_schema.md) to stage classification and then call SYSTEM$CANCEL_CLASSIFY_SCHEMA with the same
  schema name to cancel the classification process, the output is as follows:

  ```sqljson
  {
    "failed": [],
    "succeeded": [
      {
        "message": "Classification Cancelled for table [T1].",
        "table_name": "T1"
      },
      {
        "message": "Classification Cancelled for table [T2].",
        "table_name": "T2"
      },
      ...
      }
    ]
  }
  ```

* If you call SYSTEM$CANCEL_CLASSIFY_SCHEMA and the specified schema is not staged for classification, the output is as follows:

  ```sqljson
  {
    "failed": [
      {
        "message": "Unable to cancel classification for table [T1] since its already complete.",
        "table_name": "T1"
      },
      {
        "message": "Unable to cancel classification for table [T2] since its already complete.",
        "table_name": "T2"
      },
      ...
    ],
    "succeeded": []
  }
  ```

Where:

`failed`
:   Specifies a reason why the cancellation process cannot be performed for the specified table.

`succeeded`
:   Confirms the cancellation process is scheduled for the specified table.

## Usage notes

* The cancellation process can take a short time (seconds) to complete. This is analogous to
  [canceling a query](../../user-guide/querying-cancel-statements.md).
* The specified schema name can contain up to 1000 table objects. If the schema contains more than 1000 table objects, Snowflake returns an
  error message.
* Snowflake-provided stored procedures utilize caller’s rights. For more details, see
  [Understanding caller’s rights and owner’s rights stored procedures](../../developer-guide/stored-procedure/stored-procedures-rights.md).

## Examples

Cancels the classification of tables in the schema:

> ```sqlexample
> CALL SYSTEM$CANCEL_CLASSIFY_SCHEMA('hr.tables');
> ```
