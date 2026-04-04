# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/pipes.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/pipes.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/pipes.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# PIPES view

This Account Usage view displays a row for each pipe defined in the account.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| PIPE_ID | NUMBER | Internal or system-generated identifier for the pipe. |
| PIPE_NAME | VARCHAR | The name of the pipe object.  For manually created pipes, this is the name defined in the CREATE PIPE statement.  For the Snowpipe Streaming high-performance default pipe, this is derived from the target table name; for example, `MY_TABLE-STREAMING`. |
| PIPE_SCHEMA_ID | NUMBER | Internal or system-generated identifier for the schema that the pipe belongs to.  For the default pipe, this corresponds to the target table’s schema ID. |
| PIPE_SCHEMA | VARCHAR | Schema that the pipe belongs to.  For the default pipe, this corresponds to the target table’s schema. |
| PIPE_CATALOG_ID | NUMBER | Internal or system-generated identifier for the database that the pipe belongs to.  For the default pipe, this corresponds to the target table’s database ID. |
| PIPE_CATALOG | VARCHAR | Name of the database that the pipe belongs to.  For the default pipe, this corresponds to the target table’s database. |
| IS_AUTOINGEST_ENABLED | VARCHAR | Whether AUTO-INGEST is enabled for the pipe. Represents future functionality. |
| NOTIFICATION_CHANNEL_NAME | VARCHAR | Amazon Resource Name of the Amazon SQS queue for the stage named in the DEFINITION column. Represents future functionality. |
| PIPE_OWNER | VARCHAR | Name of the role that owns the pipe.  Returns NULL for the default pipe. |
| DEFINITION | VARCHAR | COPY statement used to load data from queued files into a Snowflake table. |
| CREATED | TIMESTAMP_LTZ | Creation time of the pipe. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| COMMENT | VARCHAR | Comment for this pipe.  Returns the following message for the default pipe: “Default pipe for Snowpipe Streaming High Performance ingestion to a table. Created and managed by Snowflake.” |
| PATTERN | VARCHAR | PATTERN copy option value in the [COPY INTO <table>](../sql/copy-into-table.md) statement in the pipe definition, if the copy option was specified. |
| DELETED | TIMESTAMP_LTZ | Date and time when the pipe was deleted. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object; for example, ROLE.  If a Snowflake Native App owns the object, the value is APPLICATION.  Snowflake returns NULL if you delete the object because a deleted object doesn’t have an owner role.  Returns NULL for the default pipe. |

## Usage notes

* Latency for the view may be up to 180 minutes (3 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view does not recognize the MANAGE GRANTS privilege and consequently may show less information compared to a SHOW command
  executed by a user who holds the MANAGE GRANTS privilege.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.

## Examples

The following example joins this view with [PIPE_USAGE_HISTORY view](pipe_usage_history.md) on the PIPE_ID column to track the credit usage associated with each unique PIPE object:

```sqlexample
select a.PIPE_CATALOG as PIPE_CATALOG,
       a.PIPE_SCHEMA as PIPE_SCHEMA,
       a.PIPE_NAME as PIPE_NAME,
       b.CREDITS_USED as CREDITS_USED
from SNOWFLAKE.ACCOUNT_USAGE.PIPES a join SNOWFLAKE.ACCOUNT_USAGE.PIPE_USAGE_HISTORY b
on a.pipe_id = b.pipe_id
where b.START_TIME > date_trunc(month, current_date);
```
