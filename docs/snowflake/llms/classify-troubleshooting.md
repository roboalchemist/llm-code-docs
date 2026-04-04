# Source: https://docs.snowflake.com/en/user-guide/classify-troubleshooting.md

# Troubleshooting sensitive data classification

The simplest way to start troubleshooting a table that wasn’t classified by
[sensitive data classification](classify-intro.md) is to query the table directly (for example, `SELECT * FROM my_table`). If
a table can’t be queried, it can’t be classified.

If an object can’t be classified, Snowflake logs an event to an
[event table](../developer-guide/logging-tracing/event-table-setting-up.md). By default, the event is logged to the account-level event
table. If you have an event table defined for the failed object’s database, then the event is logged there instead.

In general, there is a delay before Snowflake tries to classify the object again. Every additional failed attempt is logged to the event
table. This delay and retry process continues until the object is fixed or removed from automatic classification.

> **Note:**
>
> To help avoid unnecessary costs, Snowflake waits additional time to retry classification for some errors, such as timeouts. For these
> timeout errors, Snowflake doesn’t retry classification until all objects are reclassified; the schedule on which objects are reclassified
> is controlled by the `maximum_classification_validity_days` key of the classification profile.

If you want prevent classification events from being logged, set the [ENABLE_AUTOMATIC_SENSITIVE_DATA_CLASSIFICATION_LOG](../sql-reference/parameters.md) account
parameter to FALSE.

## Listing general errors

The following query returns general errors related to sensitive data classification from the event table:

```sqlexample
SELECT
  record_type,
  record:severity_text::string log_level,
  parse_json(value) error_message
  FROM <event_db>.<event_schema>.<event_table>
  WHERE record_type='LOG' and scope:name ='snow.automatic_sensitive_data_classification'
  ORDER BY log_level;
```

For a subset of the possible error messages returned by this query, see Tag-related error messages.

## Listing object-level classification errors

The following query against the event table returns errors related to the classification of a specific object. For example, it returns
errors that occurred when Snowflake tried to classify a specific table.

```sqlexample
SELECT
  RECORD_ATTRIBUTES:"object_name"::string AS object_name,
  parse_json(value):"error_message" error_message,
  PARSE_JSON(VALUE):"profile_name" classification_profile_name,
  timestamp,
  FROM <event_db>.<event_schema>.<event_table>
  WHERE record_type='LOG'
    AND scope:name ='snow.automatic_sensitive_data_classification'
    AND RECORD_ATTRIBUTES:"event_type" = 'CLASSIFICATION_ERROR'
  ORDER BY TIMESTAMP DESC;
```

## Tag-related error messages

|  |  |
| --- | --- |
| Error | ```output "failure_reason":"NO_TAGGING_PRIVILEGE"``` |
| Cause | The role that was used for sensitive data classification does not have the correct privileges to set tags. |
| Solution | Grant the necessary privileges to the role used for sensitive data classification. For more information, see [Tag privileges](object-tagging/work.md). |

|  |  |
| --- | --- |
| Error | ```output "failure_reason":"MANUALLY_APPLIED_VALUE_PRESENT"``` |
| Cause | Another tag is manually set on the column. |
| Solution | Determine whether you want to keep the tag that was manually set on the column. If not, unset the tag before classifying the table using automatic classification or the SYSTEM$CLASSIFY stored procedure. |

|  |  |
| --- | --- |
| Error | ```output "failure_reason":"TAG_NOT_ACCESSIBLE_OR_AUTHORIZED"``` |
| Cause | The role that was used for classification cannot access the tag. |
| Solution | *If the tag does not exist, create the tag.* If the tag exists, grant privileges on the tag, or the database and schema that contains the tag, to the role that was used to   classify the database or schema. |

For more information about event table messages, see [Viewing log messages](../developer-guide/logging-tracing/logging-accessing-messages.md).
