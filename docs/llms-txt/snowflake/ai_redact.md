# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_redact.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AI_REDACT

Detects and redacts personally identifiable information (PII) from unstructured text data.

## Syntax

Use AI_REDACT to detect and redact PII:

```sqlsyntax
AI_REDACT( <input> [, <categories> ] [, <return_error_details> ] [, <mode> ] )
```

## Arguments

**Required:**

`input`
:   A VARCHAR value that contains text data that may contain personally identifiable information (PII).

**Optional:**

`categories`
:   An ARRAY of string values that specify the types of PII to be redacted. If not specified, all supported PII
    categories are redacted. See [Detected PII categories](../../user-guide/snowflake-cortex/redact-pii.md) for a list of supported categories.

    Passing an unsupported category results in an error.

`return_error_details`
:   A BOOLEAN flag that indicates whether to return error details in case of error. When set to TRUE, the function returns
    an OBJECT that contains the value and the error message, one of which is NULL depending on whether the function
    succeeded or failed.

    Requires the session parameter AI_SQL_ERROR_HANDLING_USE_FAIL_ON_ERROR to be set to FALSE.

`mode`
:   A VARCHAR value that specifies the operating mode. Accepted values:

    * `redact` (default): Replaces detected PII with category placeholders, such as [NAME] and [ADDRESS].
    * `detect`: Returns an OBJECT that contains a `spans` array that identifies the location and category of each detected PII instance
      without redacting the text.

> **Note:**
>
> The `mode` argument is case insensitive.

## Returns

The return value of AI_REDACT depends on the `mode` argument.

### Redact mode (default)

Returns a VARCHAR that contains the input text with PII replaced by category placeholders, such as `[NAME]` where the input
text was “John Smith”.

### Detect mode

Returns an OBJECT that contains a `spans` array. Each element in the array is an OBJECT with the following fields:

> * `category`: A VARCHAR value that identifies the PII category (for example, `NAME` or `ADDRESS`).
> * `start`: A NUMBER value that identifies the start index of the PII in the input text.
> * `end`: A NUMBER value that identifies the end index of the PII in the input text.
> * `text`: A VARCHAR value that contains the matched PII text.

## Error behavior

By default, if AI_REDACT cannot process the input, the function returns an error. If the query processes multiple rows, the entire query fails.

When AI_SQL_ERROR_HANDLING_USE_FAIL_ON_ERROR is set to FALSE, the return value on error depends on the `return_error_details`
argument. The following table shows the return value based on the `return_error_details` argument:

> | `return_error_details` | Return value | Description |
> | --- | --- | --- |
> | FALSE    Not passed | NULL |  |
> | TRUE | OBJECT with `value` and `error` fields | `value`: A VARCHAR value that contains the redacted text, or NULL if an error occurred.    `error`: A VARCHAR value that contains the error message if an error occurred, or NULL if the function succeeded. |

For more information about handling errors, see [Handle row-level errors in multi-row queries](../../user-guide/snowflake-cortex/redact-pii.md).

## Usage notes

* For categories of PII that AI_REDACT can redact, see [Detected PII categories](../../user-guide/snowflake-cortex/redact-pii.md).
* For limitations in the current version of AI_REDACT, see [Limitations](../../user-guide/snowflake-cortex/redact-pii.md).

## Examples

See [Redaction examples](../../user-guide/snowflake-cortex/redact-pii.md).
