# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/functions.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/functions.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/functions.md

# Source: https://docs.snowflake.com/en/sql-reference/functions.md

# Scalar functions

This document provides links to the system-defined scalar functions, grouped by category.

A scalar function is a function that returns one value per invocation; in most cases, you can think of this as returning
one value per row. This contrasts with [Aggregate functions](functions-aggregation.md), which return one value per group of rows.

| Category | Description |
| --- | --- |
| [Bitwise expression functions](expressions-byte-bit.md) | Perform bitwise operations on expressions. |
| [Conditional expression functions](expressions-conditional.md) | Manipulate conditional expressions. |
| [Context functions](functions-context.md) | Provide contextual information about the current environment, session, and object. |
| [Conversion functions](functions-conversion.md) | Convert expressions from one data type to another data type. |
| [Data generation functions](functions-data-generation.md) | Generate random or sequential values. |
| [Date & time functions](functions-date-time.md) | Manipulate dates, times, and timestamps. |
| [Differential privacy functions](functions-differential-privacy.md) | Work with data protected by [differential privacy](../user-guide/diff-privacy/differential-privacy-overview.md). |
| [Encryption functions](functions-encryption.md) | Perform encryption and decryption on VARCHAR or BINARY values. |
| [File functions](functions-file.md) | Access files staged in cloud storage. |
| [Geospatial functions](functions-geospatial.md) | Work with geospatial data. |
| [Hash functions](functions-hash-scalar.md) | Hash values to signed 64-bit integers using a deterministic algorithm. |
| [Metadata functions](functions-metadata.md) | Retrieve data or metadata about database objects (e.g. tables) or files (e.g. staged files). |
| [Model monitor functions](functions-model-monitors.md) | Retrieve metrics from machine learning [model monitors](../developer-guide/snowflake-ml/model-registry/model-observability.md). |
| [Notification functions](functions-notification.md) | Produce JSON-formatted strings that you pass to [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](stored-procedures/system_send_snowflake_notification.md) when sending a notification to a queue or email address. |
| [Numeric functions](functions-numeric.md) | Perform rounding, truncation, exponent, root, logarithmic, and trigonometric operations on numeric values. |
| [Semi-structured and structured data functions](functions-semistructured.md) | Work with semi-structured data (JSON, Avro, etc.). |
| [String & binary functions](functions-string.md) | Manipulate and transform string input. |
| [String functions (regular expressions)](functions-regexp.md) | Subset of strings functions for performing operations on items that match a regular expression. |
