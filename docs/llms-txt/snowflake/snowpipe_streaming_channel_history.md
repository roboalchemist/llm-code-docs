# Source: https://docs.snowflake.com/en/sql-reference/account-usage/snowpipe_streaming_channel_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SNOWPIPE_STREAMING_CHANNEL_HISTORY view

This Account Usage view provides a historical record of pipeline errors, enabling users to monitor performance trends. This view displays key metrics such as processed data volume, error rates, and latency.

You can use this Account Usage view to query the error history for a specific pipe or channel.

> **Note:**
>
> The SNOWPIPE_STREAMING_CHANNEL_HISTORY view only applies to [Snowpipe Streaming with high-performance architecture](../../user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-overview.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ACCOUNT_ID | NUMBER | The ID of the Snowflake account. |
| CREATED_ON | TIMESTAMP_LTZ | Date and time when the rowset channel history was created. |
| CHANNEL_ID | NUMBER | The internal, system-generated ID of the Snowpipe Streaming channel. |
| CHANNEL_NAME | VARCHAR | The user-defined name of the Snowpipe Streaming channel. |
| PIPE_ID | NUMBER | The internal ID of the Snowpipe object associated with this Snowpipe Streaming channel. |
| END_OFFSET | VARCHAR | The last offset token processed and included in this specific channel history record. |
| TABLE_ID | NUMBER | The internal ID of the target table for this Snowpipe Streaming channel. |
| TABLE_NAME | VARCHAR | The name of the target table for this Snowpipe Streaming channel. |
| TABLE_SCHEMA_ID | NUMBER | The internal ID of the schema containing the target table. |
| TABLE_SCHEMA_NAME | VARCHAR | The name of the schema containing the target table. |
| TABLE_DATABASE_ID | NUMBER | The internal ID of the database containing the target table. |
| TABLE_DATABASE_NAME | VARCHAR | The name of the database containing the target table. |
| PIPE_NAME | VARCHAR | The name of the Snowpipe object associated with the current Snowpipe Streaming channel history entry.  Named pipes: The value is the user-defined name of the Snowpipe object associated with the channel.  Default pipe: The value is automatically derived from the target table name; for example, MY_TABLE-STREAMING. |
| PIPE_SCHEMA_ID | NUMBER | The internal identifier for the schema associated with the Snowpipe Streaming channel.  Named pipes: The value is the internal ID of the schema that contains the user-defined Snowpipe object.  Default pipe: The value is the internal ID of the schema that contains the target table. |
| PIPE_SCHEMA_NAME | VARCHAR | The name of the schema associated with the Snowpipe Streaming channel.  Named pipes: The value is the user-defined name of the schema that contains the Snowpipe object.  Default pipe: The value is the name of the schema that contains the target table. |
| PIPE_DATABASE_ID | NUMBER | The internal identifier for the database associated with the Snowpipe Streaming channel.  Named pipes: The value is the internal ID of the database that contains the user-defined Snowpipe object.  Default pipe: The value is the internal ID of the database that contains the target table. |
| PIPE_DATABASE_NAME | VARCHAR | The name of the database associated with the Snowpipe Streaming channel.  Named pipes: The value is the user-defined name of the database that contains the Snowpipe object.  Default pipe: The value is the name of the database that contains the target table. |
| LAST_ERROR_OFFSET_UPPER_BOUND | VARCHAR | The upper bound of the offset token range of the last rowset that encountered errors during this historical period. |
| LAST_ERROR_MESSAGE | VARCHAR | The last error message encountered while writing data to the channel. This column displays a redacted error message when an error is encountered. |
| SNOWFLAKE_PROCESSING_LATENCY_MS | NUMBER | The average latency, in milliseconds, observed by the Snowflake service in processing rowsets for this channel during this historical period. |
| ROWS_INSERTED | NUMBER | The total number of rows successfully inserted through this channel during this historical period. |
| ROWS_PARSED | NUMBER | The total number of rows parsed (processed) by the channel during this historical period. |
| ROW_ERROR_COUNT | NUMBER | The total number of rows that encountered errors and were not inserted through this channel during this historical period. |

## Usage notes

* The Snowpipe Streaming high-performance architecture only supports ON_ERROR=CONTINUE. Other ON_ERROR options are not supported.
