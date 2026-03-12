# Source: https://docs.snowflake.com/en/sql-reference/classes/top-insights/commands/create-top-insights.md

# CREATE SNOWFLAKE.ML.TOP_INSIGHTS

Creates a new Top Insights instance or replaces an existing one. You must instantiate this class to gain access to the
method that provides insights into your data, called GET_DRIVERS. The instance does not store any data or settings. In
most cases, you do not need to create more than one instance of this class.

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SNOWFLAKE.ML.TOP_INSIGHTS [ IF NOT EXISTS ] <instance_name>()
[ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
[ COMMENT = '<string_literal>' ]
```

## Usage notes

Use the IF NOT EXISTS form of this command to make sure that the instance exists before you call the GET_DRIVERS method.

[Replication](../../../../user-guide/account-replication-intro.md) is supported only for instances
of the [CUSTOM_CLASSIFIER](../../custom_classifier.md) class.

## Examples

See [Examples](../../../../user-guide/ml-functions/top-insights.md).
