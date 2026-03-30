# Source: https://go.soda.io/core-docs

Title: Contract Language reference | Documentation

URL Source: https://go.soda.io/core-docs

Markdown Content:
⌘Ctrl k

1.   [Reference](https://docs.soda.io/reference)

Contract Language reference
---------------------------

A Soda data contract is a YAML document that contains data quality checks. The checks in a Soda data contract are similar to unit tests for testing software. Verifying a contract means evaluating the checks against the actual data. If contract verification fails, notifications can be sent out or the new data can be stopped from being released to users.

This page documents the necessary contract structure and the supported check types, filters, and configuration options available in soda's data contract language.

A Soda data contract YAML must include the following blocks:

*   A top-level `dataset:` key 
*   
One of the following:

    *   A `checks:` block, if you’re defining dataset-wide checks 
    *   A `columns:` list 

```
dataset: datasource/db/schema/dataset #mandatory dataset fully qualified name

checks: #dataset level checks
  - schema:
  - row_count: 

columns: #columns list
  - name: id
    checks: # column level checks (optional)
      - missing:
  - name: name
    checks:
      - missing:
          threshold:
            metric: percent
            must_be_less_than: 10
  - name: size
    checks:
      - invalid:
          valid_values: ['S', 'M', 'L']
```

Every contract must have a dataset fully qualified name that follows the structure below:

`dataset: datasource/db/schema/dataset`

Casing has to match the casing in the data source.

A dataset fully qualified name is composed of 3 parts, all slash-separated:

*   
The **data source name**: This is the name of the data source in which the dataset exists. The data source name is configured in a data source YAML configuration file or in Soda Cloud.

    *   A**list of prefixes**: Prefixes represent the full list of hierarchical elements of the data source, like the **database name** and the **schema name**. Postgres, for example, has a database name and a schema name as prefixes. Databricks has catalog and schema as prefixes. Prefix names are also slash-separated. 

*   The **dataset name**: The name of the table or view. 

Every contract must include a list of columns. If a schema check is configured, this list can be used to validate the **presence, data type, and order** of columns.

Each column entry includes:

*   `name`: the column name (required) 
*   `data_type` (optional): used by the schema check 
*   `character_maximum_length` (optional): used by the schema check 
*   
`checks` (optional): a list of checks that apply only to that column

    *   `type` 
    *   Threshold keys (for any check that _needs_ a threshold, such as `must_be`, `must_be_between`, etc.) 

Example:

```
# Example of fully operational contract with only column-level checks

dataset: datasource/db/schema/dataset
columns:
  - name: id
    data_type: varchar
    checks:    # Column-level checks definition
      - missing:
      - duplicate:
  - name: name
  - name: code
```

A contract that exclusively defines **dataset-level checks** that do not run against any specific column **still requires the**`columns`**list**. In this case, providing an empty list is enough.

```
# Example of fully operational contract with only dataset-level checks

dataset: datasource/db/schema/dataset

checks:
  - schema:
  - row_count:
  
columns: []
```

The `checks` section defines the quality rules and expectations for your dataset. Checks can be written at two levels:

*   **Dataset-level**: Rules that apply to the dataset as a whole (e.g., row count, schema, freshness, duplicates across multiple columns). 
*   **Column-level**: Rules that apply to a specific column (e.g., missing, invalid, duplicate on a single column). 

Each check entry includes:

*   `type` 
*   `column:` (not required to compile) 
*   Threshold keys (for any check that _needs_ a threshold, such as `must_be`, `must_be_between`, etc.) 

**Example of a dataset-level**`checks`**block:**

```
checks: 
  - schema: 
  - row_count:
```

* * *

**Example of column-level**`checks`**block:**

```
columns:
  - name: email
    checks:
      - missing:
      - invalid:
          invalid_format:
            name: Email format
            regex: ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```

Each check defines what “good data” looks like, ensuring that your dataset meets the expected standards.

You can customize each check by adding filters, thresholds, or variable references depending on your specific use case. Learn more about the different check types on this page.

* * *

A Schema check verifies that the structure of a dataset matches the expectations defined in the contract—such as required columns, data types, and optional constraints. It ensures that changes to the dataset schema (like missing columns, unexpected data types, or reordered fields) are detected early, helping maintain stability and trust in your data.

**Example:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: id
  - name: last_name
  - name: address_line1

checks:
  - schema:
      allow_extra_columns: false
      allow_other_column_order: false
```

**Column keys used by the schema check:**

The schema check uses the columns as specified in the contract and compares them with the measured dataset columns as as the expected columns.

`name`

The name of the column. The name is **case sensitive**.

No

`data_type`

The data type of the column as is returned by the metadata from the data source. Data types are compared case insensitive.

Yes

`character_maximum_length`

The character maximum length. This represents the maximum length for data types like `VARCHAR(255)`

Yes

**Check configuration keys:**

`allow_extra_columns`

Specifies if columns other than the ones listed in the contract are allowed in the dataset. Values are `true` or `false`. Default is false, which means that all columns in the dataset must be specified in the contract.

Yes

`allow_other_column_order`

Specifies if column ordering must be exact the same as in the contract YAML document. Values are `true` or `false`. Default is false, which means that columns must appear in the order as in the contract.

Yes

`name`

Yes

`qualifier`

Yes

`attributes`

Yes

* * *

A Row Count check verifies that the dataset contains the expected number of rows. It ensures that the data source has at least a minimum number of records and no unexpected gaps. This is a fundamental check to confirm the presence and completeness of data in a dataset.

**Example**:

```
dataset: datasource/db/schema/dataset

checks:
  - row_count:

columns: []
```

**Check configuration keys**

`name`

Yes

`threshold`

The default row count threshold verifies there is at least 1 row present. [Thresholds](https://docs.soda.io/reference/contract-language-reference#thresholds)

Yes

`filter`

Yes

`qualifier`

Yes

`attributes`

Yes

* * *

A freshness check verifies if data is not too old by measuring the period between the current time and the most recent timestamp present in a given column.

* * *

**Example:**

```
dataset: datasource/db/schema/dataset

checks:
  - freshness:
      column: created_at
      threshold:
        unit: hour
        must_be_less_than: 24

columns: []
```

**Check configuration keys**

`column`

Specifies a timestamp column that represents the time of the row or

No

`name`

Yes

`threshold`

It defines the **acceptable data age limit.** It sets the maximum time allowed between the current time and the newest timestamp found in the target column.

*   `unit` : The time unit used for the threshold, e.g., `minute`, `hour`, `day`. 

No

`filter`

Yes

`qualifier`

Yes

`attributes`

Yes

* * *

A Missing check verifies that a specific column does not contain null or empty values beyond an acceptable threshold. It ensures that critical fields are populated and helps catch incomplete or corrupted data that could impact downstream processes.

**Example:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: id
    checks:
      - missing:
```

* * *

**Check configuration keys**

`missing_values`

The list of values is considered missing. NULL is always considered a missing value and doesn't need to be included

No*

`missing_format`

A SQL regex that matches with missing values. (Advanced)

No*

`name`

Yes

`threshold`

The default missing check threshold verifies there are no missing values in the column. [Thresholds](https://docs.soda.io/reference/contract-language-reference#thresholds)

Yes

`filter`

Yes

`qualifier`

Yes

`attributes`

Yes

* there are several configuration keys to configure the missing values. At least one missing configuration is required.

* * *

**Configure extra missing values in a list**

Configure a list of values that, apart from NULL, must also be considered as missing values. Typical examples are `'-'`, `'No value'`, `'N/A'`, `'None'`, `'null'`, `-1`, `999`

```
dataset: datasource/db/schema/dataset

columns:
  - name: id
    checks:
      - missing:
          missing_values: ['N/A', '-']
```

The `missing_values` configuration is only supported on **string**and **numeric**data types.

* * *

**Configure extra missing values with a regular expression**

Configure a SQL regular expression that, apart from NULL, also matches values that are considered as missing values. Only supported for columns having a text data type

```
dataset: datasource/db/schema/dataset

columns:
  - name: id
    checks:
      - missing:
          missing_format:
            name: All dashes
            regex: ^[-]+$
```

The `regex` syntax must match the SQL engine of the data source.

The `name` is a human-readable description of what the regex does. It helps explain the purpose of the pattern, making it easier for others to understand the intent of the check.

* * *

An Invalid check verifies that the values in a column conform to a set of allowed formats, values, or constraints. It helps catch data that does not meet the expected standards, such as incorrect formats, out-of-range values, or entries that violate business rules.

**Example with valid values**:

```
dataset: datasource/db/schema/dataset

columns:
  - name: size
    checks:
      - invalid:
          valid_values: ['S', 'M', 'L']
```

**Check configuration keys**

`valid_values`

A list of valid values

No*

`valid_format`

A SQL regular expression that matches with valid values

No*

`valid_reference_data`

References a dataset and column that contains valid values

No*

`valid_min`

Valid values must be greater or equal than the configured value

No*

`valid_max`

Valid values must be less or equal than the configured value

No*

`valid_length`

The fixed length of valid values

No*

`valid_min_length`

The minimum length of valid values

No*

`valid_max_length`

The maximum length of valid values

No*

`invalid_values`

A list of invalid values

No*

`invalid_format`

A SQL regular expression that matches with invalid values

No*

`name`

Yes

`threshold`

The default invalid check threshold ensures there must not be any invalid values. [Thresholds](https://docs.soda.io/reference/contract-language-reference#thresholds)

Yes

`filter`

Yes

`qualifier`

Yes

`attributes`

Yes

* there are several configuration keys to configure the invalid values. At least one validity configuration is required. Multiple validity configurations can be combined.

**Example with a regular expression**

Format is only supported for string data type.

```
dataset: datasource/db/schema/dataset

columns:
  - name: code
    checks:
      - invalid:
          valid_format:
            name: Alpha Code
            regex: \^[A-Z]{3}$\
```

The `regex` syntax must match the SQL engine of the data source.

The `name` is a human-readable description of what the regex does. It helps explain the purpose of the pattern, making it easier for others to understand the intent of the check.

* * *

**Example minimum and maximum values:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: code
    checks:
      - invalid:
          valid_min: 1
          valid_max: 100
```

`valid_min` and `valid_max` can be used independently.

It's supported on columns with numerical data types.

* * *

**Example minimum and maximum length:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: code
    checks:
      - invalid:
          valid_length: 2
          valid_min_length: 1
          valid_max_length: 5
```

`valid_length` , `valid_min_length` and `valid_max_length` can be used independently.

* * *

```
dataset: datasource/db/schema/dataset

columns:
  - name: code
    checks:
      - invalid:
          valid_reference_data:
            dataset: data_source/db/schema/reference_dataset
            column: valid_code
```

`valid_reference_data` has 2 nested configurations:

*   `dataset`: fully qualified dataset name. Limitation: The reference dataset must be in the same data source. 
*   `column`: the name of the column containing the valid values 

Commonly referred to as a reference check or referential integrity check.

* * *

A Duplicate check ensures that values in a column or combination of columns are unique, helping prevent data integrity issues. It can be used at the **column level** or **dataset level**.

```
dataset: datasource/db/schema/dataset

columns:
  - name: id
    checks:
      - duplicate:
```

**Configuration keys:**

`name`

Yes

`threshold`

The default duplicate check threshold requires that all values are unique. [Thresholds](https://docs.soda.io/reference/contract-language-reference#thresholds)

Yes

`filter`

Check filter

Yes

`qualifier`

Yes

`attributes`

Yes

```
dataset: datasource/db/schema/dataset

checks:
  - duplicate:
      columns: ['col1', 'col2']
      
columns: []
```

**Configuration keys:**

`columns`

List of column names

No

`name`

Yes

`threshold`

The default duplicate check threshold requires that all values are unique. Data Contract Language Reference ✅

Yes

`filter`

Yes

`qualifier`

Yes

`attributes`

Yes

* * *

An Aggregate check verifies that the result of an aggregate function, such as `avg`, `sum`, `min`, `max`, or `count`—meets the expected thresholds. It helps ensure that summary statistics over a column remain within acceptable ranges and that key metrics derived from your data stay accurate and consistent.

**Example:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: age
    checks:
      - aggregate:
          function: avg
          threshold:
            must_be_between:
              greater_than: 20
              less_than: 50
```

**Check configuration keys**

`function`

Supported by all data sources: `avg`, `avg_length`, `max`, `min`, `max_length`, `min_length`, `sum`

No

`name`

Yes

`threshold`

No

`filter`

Yes

`qualifier`

Yes

`attributes`

Yes

* * *

A Metric check validates the result of a custom SQL expression or query against a threshold. It supports complex business logic, calculated metrics, or cross-column relationships. Metric checks can be defined at the dataset level (across multiple columns) or column level (single column).

For better performance, we recommend SQL expressions over full SQL queries—they’re simpler to write and can be combined with other checks in a single query.

**Example at the dataset level:**

```
dataset: datasource/db/schema/dataset

checks:
  - metric:
      expression: AVG("end" - "start")
      threshold:
        must_be_between:
          greater_than: 3
          less_than: 8

columns: []
```

**Example at the column level:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: end
    checks:
      - metric:
          expression: AVG("end" - "start")
          threshold:
            must_be_between:
              greater_than: 3
              less_than: 8
```

* * *

**Check configuration keys**

`expression`

A SQL expression that produces the numeric metric value that will be compared with the threshold.

No

`name`

Yes

`threshold`

No

`qualifier`

Yes

`attributes`

Yes

**Example at the dataset level:**

```
dataset: datasource/db/schema/dataset

checks:
  - metric:
      query: |
        SELECT AVG("end" - "start")
        FROM datasource.db.schema.table
      threshold:
        must_be_greater_than: 3

columns: []
```

**Example at the column level:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: end
    checks:
      - metric:
          query: |
            SELECT AVG("end" - "start")
            FROM datasource.db.schema.table
          threshold:
            must_be_greater_than: 3
```

`query`

A SQL query that produces a single numeric metric value that will be compared with the threshold.

No

`name`

Yes

`threshold`

No

`qualifier`

Yes

`attributes`

Yes

* * *

A Failed Rows check identifies rows that violate a specific condition, such as a filter or SQL expression. It helps pinpoint problematic data like outliers or rule violations and can save references for further review.

Failed Rows checks can apply at the dataset level (testing conditions across multiple columns) or at the column level (validating individual column values).

We recommend using SQL expressions over full SQL queries for simplicity and efficiency—they allow combining multiple checks into a single query for better performance.

**Example at the dataset level:**

```
dataset: datasource/db/schema/dataset

checks:
  - failed_rows:
      expression: ("end" - "start") > 5
      
columns: []
```

**Example at the column level:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: end
    data_type: DATE
    checks:
      - failed_rows:
          expression: ("end" - "start") > 0
```

**Check configuration keys**

`Expression`

A SQL expression, used as the WHERE clause, that produces any tabular data indicating failures with the data. An expression returning zero rows indicates there is no problem with the data.

No

`name`

Yes

`threshold`

The default is that there should be no failed rows.[Thresholds](https://docs.soda.io/reference/contract-language-reference#thresholds)

Yes

`qualifier`

Yes

`attributes`

Yes

**Example at the dataset level:**

```
dataset: datasource/db/schema/dataset

checks:
  - failed_rows:
      query: |
        SELECT * FROM datasource.db.schema.table WHERE ("end" - "start") > 5
        
columns: []
```

**Example at the column level:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: end
    data_type: DATE
    checks:
      - failed_rows:
        query: |
          SELECT * FROM datasource.db.schema.table WHERE ("end" - "start") > 0
```

**Check configuration keys**

`query`

A SQL query that produces any tabular data indicating failures with the data. An expression returning zero rows indicates there is no problem with the data. I

No

`name`

Yes

`threshold`

The default is that there should be no failed rows. The threshold can only be count-based. Percent thresholds are not supported. [Thresholds](https://docs.soda.io/reference/contract-language-reference#thresholds)

Yes

`qualifier`

Yes

`attributes`

Yes

* * *

> Documentation for reconciliation checks is available in [Reconciliation checks](https://docs.soda.io/reference/contract-language-reference/reconciliation-checks)

A `group by` check allows you to run validations on **aggregated metrics per group of records**based on one or more fields. You can then apply thresholds to metrics like counts, sums, or averages for each group.

Group By checks require having installed **the**`soda-groupby`**package using the**[**private PyPI**](https://docs.soda.io/reference/contract-language-reference#private-pypi-installation-flow) (Team or Entreprise license), unless you are using an agent.

Need access to the private PyPI? Please [contact us](https://www.soda.io/contact).

> **Follow the**[**private PyPi installation flow**](https://docs.soda.io/deployment-options/soda-python-libraries#private-pypi-installation-flow)to set up your environment and install the necessary Soda extensions.

**Example at the dataset level:**

```
dataset: datasource/db/schema/dataset

checks:
  - group_by:
      name: ""
      query: |-
        SELECT
            warehouse_id,
            product_id,
            COUNT(*) AS record_count,
            SUM(qty_on_hand) AS total_qty_on_hand,
        FROM soda_demo.retail_stock_levels
        GROUP BY warehouse_id, product_id
      fields:
        - warehouse_id
        - product_id
      metric_name: total_qty_on_hand
      threshold:
        must_be_greater_than: 1
    
columns: []
```

**Check configuration keys**

`query`

SQL query returning grouping fields and metrics

No

`fields`

List of column(s) used to group results

No

`metric_name`

Metric (from query alias) used for threshold evaluation

`name`

Yes

`threshold`

The threshold to compare each of the group metrics with.[Thresholds](https://docs.soda.io/reference/contract-language-reference#thresholds)

No

`qualifier`

Yes

`attributes`

Yes

* * *

Most checks support a `filter` to limit the rows on which the check applies:

```
dataset: datasource/db/schema/dataset

columns:
  - name: id
    checks:
      - missing:
          filter: "country = 'USA'"
```

Note: If a dataset filter is configured, both the dataset and the check filter will be applied.

**All column-level checks**(except `failed_rows` check type) as well as the dataset-level **Freshness check,****support a**`column_expression`**configuration** that allows you to modify the column value before the check is evaluated. You can optionally define:

`column_expression: <SQL expression>`

This SQL expression:

*   Uses the SQL dialect of your connected data source. 
*   Is applied during query generation. 
*   Modifies the column value before the check is evaluated 

Soda then runs the check against the result of that expression instead of the raw column.

Performance will depend on the complexity of the SQL expression. All expressions must be valid in the underlying warehouse dialect; **Soda does not validate SQL syntax before execution**.

You can use `column_expression` to:

*   Access and validate **nested properties**in structured columns (for example, JSON, STRUCT, or OBJECT fields). 
*   **Cast data types** before applying checks (e.g., convert a string to a date for freshness validation). 
*   Reuse standard Soda checks (freshness, missing, validity, etc.) without writing custom SQL. 

You can define `column_expression` at the column level so that it applies to all checks on that column.

```
columns:
  - name: column_name
    column_expression: <SQL expression>
    checks:
      - missing:
      - duplicate:
      - invalid:
          valid_min: 0
```

You can also define a `column_expression` inside an individual check:

```
columns:
  - name: employee
    checks:
      - invalid:
          valid_min: 100
          column_expression: <SQL expression>
```

If both column-level and check-level `column_expression` are defined, the check-level expression overrides the column-level expression.

**Validate nested fields in structured columns**[](https://go.soda.io/core-docs#validate-nested-fields-in-structured-columns)

If a column "employee" contains structured data such as JSON or STRUCT:

```
{
  "data": {
    "id": 1234,
    "value": 250
  }
}
```

You can validate nested properties directly using standard checks.

**Example (Postgres syntax)**

```
columns:
  - name: employee
    data_type: struct
    column_expression: employee.data->>'id'
    checks:
      - invalid:
          valid_min: 1000
          column_expression: employee.data->>'id'
      - invalid:
          valid_min: 200
          column_expression: employee.data->>'value'
```

Soda applies built-in validation logic to the extracted nested value. In this example, `employee.data->>'id'` is evaluated before applying the `invalid` check.

**Cast data types for compatibility with checks**[](https://go.soda.io/core-docs#cast-data-types-for-compatibility-with-checks)

Some checks require specific data types.

For example:

*   `freshness` requires a date/timestamp 
*   `valid format` (regex) works on strings 
*   Numeric validations require numeric types 

If your column type does not match the check’s requirement, you can cast it.

**Example: Cast string to date for freshness (Postgres syntax)**

```
checks:
  - freshness:
      column: hire_date
      column_expression: hire_date::date
      threshold:
        must_be_less_than: "7 days"
```

If `hire_date` is stored as a string, casting it to `date` using `::date` allows freshness evaluation, since the check requires a valid date-formatted value.

**Example: Cast numeric to string for regex validation (Postgres syntax)**

```
columns:
  - name: employee_id
    type: 
    checks:
      - invalid:
          valid_format: "^[A-Z]{2}[0-9]{6}$"
          column_expression: employee_id::text
```

This enables regex validation on numeric IDs, since in some data sources, regular expressions can only be executed on text-type columns.

*   Expressions must use the **data source dialect** (Snowflake, BigQuery, Databricks, etc.). 
*   Soda does not normalize SQL syntax across data sources. 
*   
`column_expression` is not supported for:

    *   `failed_rows` 
    *   `row_count` 
    *   `duplicate` (dataset level) 
    *   `group_by` 
    *   `schema` 
    *   Custom metric checks 

Every check (except the schema check) has a metric value that is evaluated and produces a check outcome. The threshold is the check part that specifies which numeric values make the check pass or fail.

An example threshold is: "The missing count metric value must be less than 5."

```
dataset: datasource/db/schema/dataset

columns:
  - name: status
    checks:
      - missing:
          threshold:
            must_be_less_than: 0
```

Use one of the following threshold configuration keys to specify an open range.

`must_be`

The metric value must be equal to the configured value

`must_not_be`

The metric value must be different from the configured value

`must_be_greater_than`

The metric value must be greater than the configured value

`must_be_greater_than_or_equal`

The metric value must be greater than or equal to the configured value

`must_be_less_than`

The metric value must be less than the configured value

`must_be_less_than_or_equal`

The metric value must be less than or equal to the configured value

`must_be_between`

The metric value must be between the acceptable bounds for a metric. The bounds must be expressed as either a **strict** range (`greater_than` / `less_than`) or an **inclusive** range (`greater_than_or_equal` / `less_than_or_equal`). The bounds are specified as **nested properties** under `must_be_between`.

`must_be_not_between`

The metric value must not be between the acceptable bounds for a metric. The bounds must be expressed as either a **strict** range (`greater_than` / `less_than`) or an **inclusive** range (`greater_than_or_equal` / `less_than_or_equal`). The bounds are specified as **nested properties** under `must_not_be_between`.

Use a closed range to ensure metric values are between 2 boundaries.

**Example:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: success_ratio
    checks:
      - missing:
          threshold:
            must_be_between:
              greater_than: 0
              less_than: 100
```

*   Use `greater_than` or `greater_than_or_equal` to specify the lower bound 
*   Use `less_than` or `less_than_or_equal` to specify the upper bound 

Use an open range to ensure metric values are outside 2 boundaries.

**Example:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: success_ratio
    checks:
      - missing:
          threshold:
            must_be_not_between:
              less_than: 0
              greater_than: 100
```

*   Use `less_than` or `less_than_or_equal` to specify the lower bound 
*   Use `greater_than` or `greater_than_or_equal` to specify the upper bound 

**Set a threshold as a percentage**

To specify a threshold as a percentage of the total, add `metric: percent` to the threshold.

The `metric` The property has 2 possible values: `count` is the default and `percentage` can be configured.

Percentage-based thresholds are only available on checks where the metric value can be expressed as a percentage of a total value. These are missing, invalid, and duplicate checks.

Note that the total value refers to the total number of rows checked. In case of a dataset filter or a check filter, the total refers to the number of rows passing the filters.

**Example:**

```
dataset: datasource/db/schema/table

columns:
  - name: status
    checks:
      - missing:
          threshold:
            metric: percent
            must_be_less_than: 5
```

To change the default "fail" threshold level, add `level: warn` to the threshold.

This will cause a given check to emit warning instead of check failure.

**Example:**

```
dataset: datasource/db/schema/dataset

columns:
  - name: status
    checks:
      - missing:
          threshold:
            level: warn
```

The `name` property provides a human-readable description for a check. It helps explain the purpose of the check in plain language, making it easier for users to understand the intent behind each rule, especially when reviewing results in Soda Cloud.

For example, instead of relying on technical details like a regex pattern or threshold, a well-written `name` offers a simple summary, such as:

```
dataset: datasource/db/schema/dataset

columns:
  - name: status
    checks:
      - missing:
          name:  The missing count metric value must be less than 5%
          threshold:
            metric: percent
            must_be_less_than: 5
```

In this example, the `name` ("Email format") clarifies the purpose of the regex. This is particularly helpful for non-technical users reviewing the contract or verification results.

**Best Practices for Check Names:**

*   Write check names in plain language. 
*   Focus on the intent or business rule the check enforces. 
*   Avoid repeating technical details already visible in the check configuration. 

The `name` Property is optional but highly recommended for improving clarity and collaboration.

By default, the check name is the check type.

Use attributes to **label**, **sort**, and **route** your checks in Soda Cloud. Attributes help you organize checks by properties such as domain, priority, location, and sensitivity (e.g., PII).

> Learn how to leverage attributes with [Notifications](https://docs.soda.io/manage-issues/notifications) and [Browse datasets](https://docs.soda.io/manage-issues/browse-datasets).

**Apply Attributes to Checks**

You can add attributes directly to individual checks. For example:

```
dataset: datasource/db/schema/dataset

columns:
  - name: customer_email
    data_type: VARCHAR
    checks:
      - missing:
          attributes:
            domain: Sales
            pii: True
            dimension: completeness
```

**Set Default Attributes at the Top Level**

You can also define default attributes at the dataset level. These attributes apply to **all checks**, unless overridden at the individual check level.

```
dataset: datasource/db/schema/dataset

check_attributes:
  domain: Sales
  
columns:
  - name: customer_email
    data_type: VARCHAR
    checks:
      - missing:
          attributes:
            pii: True
            dimension: completeness
```

When publishing contract results to Soda Cloud, **all check attributes must be pre-defined in Soda Cloud**. If any attribute used in a contract is not registered in your Soda Cloud environment, the results will **not be published**, and the data contract scan will be **marked as failed**.

> Learn how to configure attributes in Soda Cloud: [Check and dataset attributes](https://docs.soda.io/manage-issues/check-and-dataset-attributes).

When sending results to Soda Cloud, check qualifiers ensure that the checks in the source YAML document can be correlated with the checks in Soda Cloud.

Most checks don't need a qualifier because there is only one check in a `checks` section of the same type. If you have multiple checks of the same type in a `checks` section, you need to ensure that each check has a distinct string `qualifier` value.

Keep in mind that if you change the qualifier, the historical information of this check on Soda Cloud is lost.

We want to ensure that all contracts are Soda Cloud ready so we have made it mandatory to specify qualifiers where needed.

In case two checks have the same identity, contract verification will complain with an error `Duplicate identity`

Configure distinct qualifiers to create unique check identities:

```
dataset: datasource/db/schema/table

columns:
  - name: status
    checks:
      - invalid:
          valid_values: ["C", "A", "D"]
      - invalid:
          qualifier: c2
          valid_format:
            regex: ^[CAD]$
            name: Characters format
```

Any text or numeric value is allowed as the qualifier. No qualifier is considered different from other checks with a qualifier like in the example above.

* * *

A dataset filter ensures that all checks in the contract are only applied to a subset of the rows in the dataset.

This is most commonly used to apply all checks to the latest time partition of the data. Each time new data is appended to an incremental dataset, the contract verification should evaluate the checks only on the rows in the latest time partition.

```
dataset: datasource / db / schema / dataset;

filter: "created_at >= CURRENT_DATE - INTERVAL '1 day'";
    
columns: []
```

Variables allow dynamic substitution of values in contracts. They help you:

*   **Parameterize** values that differ across environments, datasets, or schedules. 
*   **Reuse values** in multiple places within the same contract to reduce duplication and improve maintainability. 

Variables can be used in filters, checks, thresholds, and more.

Declare variables at the top of the contract:

```
dataset: datasource/db/schema/dataset

variables:
  COUNTRY:
    default: France
    
columns: []
```

The default value is optional. Variables without a `default` are required when verifying a contract (see below). _If you don't specify a_`default`_value, don't forget the colon (_`:`_) after the variable name._

Use variables in other places in the contract with syntax: `${var.VARIABLE_NAME}`

```
dataset: datasource/db/schema/dataset

filter: "created_at >= '${var.START_DATE}'"

columns:
  - name: status
    checks:
      - missing:
```

**Variables are case sensitive**. We recommend always using upper case and underscores for variable names.

You can specify variables values when verifying a contract:

`soda contract verify --set START_DATE=2024-05-19T14:30:00Z`

Setting a variable at verification time overrides the default value configured in the contract.

Soda currently supports only **string** and **numeric** variables, meaning that variables must be represented as either **text values** or **numbers**. Other variable types (such as boolean, date/time, arrays, or complex objects) are not supported at this time, so **any inputs should be formatted or converted into one of these two supported formats** before being used in Soda.

`${soda.NOW}` is a built-in variable that provides the **current timestamp at the moment of scan execution**, allowing you to create dynamic filters relative to the time of scan execution. For example, to check for records in the last 24 hours.

* * *

Soda Cloud can execute the contract verification on a time schedule.

First, configure the time schedule in the contract.

```
dataset: datasource/db/schema/dataset

soda_agent:
  checks_schedule:
    cron: 0 0 * * *
    timezone: UTC
    
columns: []
```

*   This defines a cron-based schedule to trigger contract **verification** 
*   Requires the data source to be configured in Soda Cloud with Soda Agent 

Second, publish the contract to Soda Cloud.

* * *

Last updated 9 days ago

Was this helpful?
