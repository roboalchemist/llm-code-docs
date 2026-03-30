# Source: https://docs.snowflake.com/en/sql-reference/functions/extract_semantic_categories.md

Categories:
:   [System functions](../functions-system.md)

# EXTRACT_SEMANTIC_CATEGORIES

> **Note:**
>
> EXTRACT_SEMANTIC_CATEGORIES is a legacy function. Snowflake recommends using other methods of
> implementing [sensitive data classification](../../user-guide/classify-intro.md).

Returns a set of categories (semantic and privacy) for each supported column in the specified table or view. To return the categories for
a column, the column must use a [data type](../../user-guide/classify-intro.md) that supports classification and
does not contain all NULL values.

The categories are derived from the metadata and data contained in the columns, as well as the metadata about the columns and data. The
privacy categories rely on the generated semantic categories, if any.

## Syntax

```sqlsyntax
EXTRACT_SEMANTIC_CATEGORIES( '<object_name>' [ , <max_rows_to_scan> ] )
```

## Arguments

**Required:**

`object_name`
:   The name of the table, external table, view, or materialized view containing the columns to be classified. If a database and
    schema is not in use in the current session, the name must be fully-qualified.

    The name must be specified exactly as it is stored in the database. If the name contains special characters, capitalization, or blank
    spaces, the name must be enclosed first in double-quotes and then in single quotes.

**Optional:**

`max_rows_to_scan`
:   The sample size of rows to use for determining the classification categories in the specified table/view.

    Valid values: `1` to `10000`

    Default: `10000`

## Returns

As a representative example, the JSON object has the following structure:

```sqljson
{
  "valid_value_ratio": 1.0,
  "recommendation": {
    "semantic_category": "PASSPORT",
    "privacy_category": "IDENTIFIER",
    "confidence": "HIGH",
    "coverage": 0.7,
    "details": [
      {
        "semantic_category": "US_PASSPORT",
        "coverage": 0.7
      },
      {
        "semantic_category": "CA_PASSPORT",
        "coverage": 0.1
      }
    ]
  },
  "alternates": [
    {
      "semantic_category": "NATIONAL_IDENTIFIER",
      "privacy_category": "IDENTIFIER",
      "confidence": "LOW",
      "coverage": 0.3,
      "details": [
        {
          "semantic_category": "US_SSN",
          "privacy_category": "IDENTIFIER",
          "coverage": 0.3
        }
      ]
    }
  ]
}
```

Where:

`valid_value_ratio`
:   Specifies the ratio of valid values in the sample size. Invalid values include NULL, an empty string, and a string with more than 256
    characters.

`recommendation`
:   Specifies information about each tag and value. This information includes:

    `semantic_category`
    :   Specifies the semantic category tag value.

        For possible tag values, see [Native semantic categories of sensitive data classification](../../user-guide/classify-native.md).

    `privacy_category`
    :   Specifies the privacy category tag value.

        The possible values are `IDENTIFIER`, `QUASI-IDENTIFIER` and `SENSITIVE`.

    `confidence`
    :   Specifies one of the following values: `HIGH`, `MEDIUM`, or `LOW`. This value indicates the relative confidence that Snowflake has based upon the column sampling process and how the column data aligns with how Snowflake classifies data.

    `coverage`
    :   Specifies the percent of sampled cell values that match the rules for a particular category.

    `details`
    :   Specifies fields and values that can specify a geographical tag value for the SEMANTIC_CATEGORY tag.

`alternates`
:   Specifies information about each tag and value to consider other than the recommended tag.

## Usage notes

* The function requires a running warehouse. The warehouse can affect performance and cost.
* This function is no longer being updated to coincide with additional enhancements to
  [Data Classification](../../user-guide/classify-intro.md).

## Examples

Extract the semantic and privacy categories for the `my_db.my_schema.hr_data` table using the default (`10000`) for the number of
rows to scan:

> ```sqlexample
> USE ROLE data_engineer;
>
> USE WAREHOUSE classification_wh;
>
> SELECT EXTRACT_SEMANTIC_CATEGORIES('my_db.my_schema.hr_data');
> ```

Same as the previous example, but limited to scanning only 5000 rows in the table:

> ```sqlexample
> USE ROLE data_engineer;
>
> SELECT EXTRACT_SEMANTIC_CATEGORIES('my_db.my_schema.hr_data', 5000);
> ```

Same as the first example, but stores results in a table:

> ```sqlexample
> USE ROLE data_engineer;
>
> CREATE OR REPLACE TABLE classification_results(v VARIANT) AS
>   SELECT EXTRACT_SEMANTIC_CATEGORIES('my_db.my_schema.hr_data');
> ```
>
> Once the results are stored in a table, you can revise them before using
> [ASSOCIATE_SEMANTIC_CATEGORY_TAGS](../stored-procedures/associate_semantic_category_tags.md) to apply them.
