# Source: https://docs.datadoghq.com/ddsql_reference.md

---
title: DDSQL Reference
description: >-
  Complete reference for DDSQL syntax, data types, functions, operators, and
  statements for querying Datadog data with SQL.
breadcrumbs: Docs > DDSQL Reference
source_url: https://docs.datadoghq.com/index.html
---

# DDSQL Reference
Available for:
{% icon name="icon-ddsql" /%}
 DDSQL Editor | 
{% icon name="icon-notebook" /%}
 Notebooks 
## Overview{% #overview %}

DDSQL is SQL for Datadog data. It implements several standard SQL operations, such as `SELECT`, and allows queries against unstructured data. You can perform actions like getting exactly the data you want by writing your own `SELECT` statement, or querying tags as if they are standard table columns.

This documentation covers the SQL support available and includes:

- Syntax compatible with PostgreSQL
- Data types
- Type literals
- SQL functions
- Regular expressions
- Window functions
- JSON functions
- Table functions
- Tags

{% image
   source="https://datadog-docs.imgix.net/images/logs/workspace/sql_reference/sql_syntax_analysis_cell.0508237133cb7ed03597d35cb532ddd3.png?auto=format"
   alt="Example workspace cell with SQL syntax" /%}

## Syntax{% #syntax %}

The following SQL syntax is supported:

{% dl %}

{% dt %}
`SELECT (DISTINCT)` (DISTINCT: Optional)
{% /dt %}

{% dd %}
Retrieves rows from a database, with `DISTINCT` filtering out duplicate records.
```sql
SELECT DISTINCT customer_id
FROM orders 
```

{% /dd %}

{% dt %}
`JOIN`
{% /dt %}

{% dd %}
Combines rows from two or more tables based on a related column between them. Supports FULL JOIN, INNER JOIN, LEFT JOIN, RIGHT JOIN.
```sql
SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id 
```

{% /dd %}

{% dt %}
`GROUP BY`
{% /dt %}

{% dd %}
Groups rows that have the same values in specified columns into summary rows.
```sql
SELECT product_id, SUM(quantity)
FROM sales
GROUP BY product_id 
```

{% /dd %}

{% dt %}
`||` (concat)
{% /dt %}

{% dd %}
Concatenates two or more strings together.
```sql
SELECT first_name || ' ' || last_name AS full_name
FROM employees 
```

{% /dd %}

{% dt %}
`WHERE` (Includes support for `LIKE`, `IN`, `ON`, `OR` filters)
{% /dt %}

{% dd %}
Filters records that meet a specified condition.
```sql
SELECT *
FROM employees
WHERE department = 'Sales' AND name LIKE 'J%' 
```

{% /dd %}

{% dt %}
`CASE`
{% /dt %}

{% dd %}
Provides conditional logic to return different values based on specified conditions.
```sql
SELECT order_id,
  CASE
    WHEN quantity > 10 THEN 'Bulk Order'
    ELSE 'Standard Order'
  END AS order_type
FROM orders 
```

{% /dd %}

{% dt %}
`WINDOW`
{% /dt %}

{% dd %}
Performs a calculation across a set of table rows that are related to the current row.
```sql
SELECT
  timestamp,
  service_name,
  cpu_usage_percent,
  AVG(cpu_usage_percent) OVER (PARTITION BY service_name ORDER BY timestamp ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_cpu
FROM
  cpu_usage_data 
```

{% /dd %}

{% dt %}
`IS NULL` / `IS NOT NULL`
{% /dt %}

{% dd %}
Checks if a value is null or not null.
```sql
SELECT *
FROM orders
WHERE delivery_date IS NULL 
```

{% /dd %}

{% dt %}
`LIMIT`
{% /dt %}

{% dd %}
Specifies the maximum number of records to return.
```sql
SELECT *
FROM customers
LIMIT 10 
```

{% /dd %}

{% dt %}
`OFFSET`
{% /dt %}

{% dd %}
Skips a specified number of records before starting to return records from the query.
```sql
SELECT *
FROM employees
OFFSET 20 
```

{% /dd %}

{% dt %}
`ORDER BY`
{% /dt %}

{% dd %}
Sorts the result set of a query by one or more columns. Includes ASC, DESC for sorting order.
```sql
SELECT *
FROM sales
ORDER BY sale_date DESC 
```

{% /dd %}

{% dt %}
`HAVING`
{% /dt %}

{% dd %}
Filters records that meet a specified condition after grouping.
```sql
SELECT product_id, SUM(quantity)
FROM sales
GROUP BY product_id
HAVING SUM(quantity) > 10 
```

{% /dd %}

{% dt %}
`IN`, `ON`, `OR`
{% /dt %}

{% dd %}
Used for specified conditions in queries. Available in `WHERE`, `JOIN` clauses.
```sql
SELECT *
FROM orders
WHERE order_status IN ('Shipped', 'Pending') 
```

{% /dd %}

{% dt %}
`USING`
{% /dt %}

{% dd %}
This clause is a shorthand for joins where the join columns have the same name in both tables. It takes a comma-separated list of those columns and creates a separate equality condition for each matching pair. For example, joining `T1` and `T2` with `USING (a, b)` is equivalent to `ON T1.a = T2.a AND T1.b = T2.b`.
```sql
SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers
USING (customer_id) 
```

{% /dd %}

{% dt %}
`AS`
{% /dt %}

{% dd %}
Renames a column or table with an alias.
```sql
SELECT first_name AS name
FROM employees 
```

{% /dd %}

{% dt %}
Arithmetic Operations
{% /dt %}

{% dd %}
Performs basic calculations using operators like `+`, `-`, `*`, `/`.
```sql
SELECT price, tax, (price * tax) AS total_cost
FROM products 
```

{% /dd %}

{% dt %}
`INTERVAL value unit`
{% /dt %}

{% dd %}
Interval representing a time duration specified in a given unit. Supported units:- `milliseconds` / `millisecond`- `seconds` / `second`- `minutes` / `minute`- `hours` / `hour`- `days` / `day`
{% /dd %}

{% /dl %}

## Data types{% #data-types %}

DDSQL supports the following data types:

| Data Type   | Description                        |
| ----------- | ---------------------------------- |
| `BIGINT`    | 64-bit signed integers.            |
| `BOOLEAN`   | `true` or `false` values.          |
| `DECIMAL`   | Floating-point numbers.            |
| `INTERVAL`  | Time duration values.              |
| `JSON`      | JSON data.                         |
| `TIMESTAMP` | Date and time values.              |
| `VARCHAR`   | Variable-length character strings. |

### Array types{% #array-types %}

All data types support array types. Arrays can contain multiple values of the same data type.

## Type literals{% #type-literals %}

DDSQL supports explicit type literals using the syntax `[TYPE] [value]`.

| Type        | Syntax                  | Example                                |
| ----------- | ----------------------- | -------------------------------------- |
| `BIGINT`    | `BIGINT 'value'`        | `BIGINT '1234567'`                     |
| `BOOLEAN`   | `BOOLEAN 'value'`       | `BOOLEAN 'true'`                       |
| `DECIMAL`   | `DECIMAL 'value'`       | `DECIMAL '3.14159'`                    |
| `INTERVAL`  | `INTERVAL 'value unit'` | `INTERVAL '30 minutes'`                |
| `JSON`      | `JSON 'value'`          | `JSON '{"key": "value", "count": 42}'` |
| `TIMESTAMP` | `TIMESTAMP 'value'`     | `TIMESTAMP '2023-12-25 10:30:00'`      |
| `VARCHAR`   | `VARCHAR 'value'`       | `VARCHAR 'hello world'`                |

The type prefix can be omitted and the type is automatically inferred from the value. For example, `'hello world'` is inferred as `VARCHAR`, `123` as `BIGINT`, and `true` as `BOOLEAN`. Use explicit type prefixes when values could be ambiguous; for example,`TIMESTAMP '2025-01-01'` would be inferred as `VARCHAR` without the prefix.

### Array literals{% #array-literals %}

Array literals use the syntax `ARRAY[value1, value2, ...]`. The array type is automatically inferred from the values.

```sql
SELECT ARRAY['apple', 'banana', 'cherry'] AS fruits; -- Inferred as VARCHAR array
SELECT ARRAY[1, 2, 3] AS numbers;                    -- Inferred as BIGINT array
SELECT ARRAY[true, false, true] AS flags;            -- Inferred as BOOLEAN array
SELECT ARRAY[1.1, 2.2, 3.3] AS decimals;             -- Inferred as DECIMAL array
```

### Example{% #example %}

```sql
-- Using type literals in queries
SELECT
    VARCHAR 'Product Name: ' || name AS labeled_name,
    price * DECIMAL '1.08' AS price_with_tax,
    created_at + INTERVAL '7 days' AS expiry_date
FROM products
WHERE created_at > TIMESTAMP '2025-01-01';
```

## Functions{% #functions %}

The following SQL functions are supported. For Window function, see the separate Window function section in this documentation.

| Function                                                                    | Return Type                     | Description                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `MIN(variable v)`                                                           | typeof v                        | Returns the smallest value in a set of data.                                                                                                                                                                                                     |
| `MAX(variable v)`                                                           | typeof v                        | Returns the maximum value across all input values.                                                                                                                                                                                               |
| `COUNT(any a)`                                                              | numeric                         | Returns the number of input values that are not null.                                                                                                                                                                                            |
| `SUM(numeric n)`                                                            | numeric                         | Returns the summation across all input values.                                                                                                                                                                                                   |
| `AVG(numeric n)`                                                            | numeric                         | Returns the average value (arithmetic mean) across all input values.                                                                                                                                                                             |
| `BOOL_AND(boolean b)`                                                       | boolean                         | Returns whether all non-null input values are true.                                                                                                                                                                                              |
| `BOOL_OR(boolean b)`                                                        | boolean                         | Returns whether any non-null input value is true.                                                                                                                                                                                                |
| `CEIL(numeric n)` / `CEILING(numeric n)`                                    | numeric                         | Returns the value rounded up to the nearest integer. Both `CEIL` and `CEILING` are supported as aliases.                                                                                                                                         |
| `FLOOR(numeric n)`                                                          | numeric                         | Returns the value rounded down to the nearest integer.                                                                                                                                                                                           |
| `ROUND(numeric n)`                                                          | numeric                         | Returns the value rounded to the nearest integer.                                                                                                                                                                                                |
| `POWER(numeric base, numeric exponent)`                                     | numeric                         | Returns the value of base raised to the power of exponent.                                                                                                                                                                                       |
| `LOWER(string s)`                                                           | string                          | Returns the string as lowercase.                                                                                                                                                                                                                 |
| `UPPER(string s)`                                                           | string                          | Returns the string as uppercase.                                                                                                                                                                                                                 |
| `ABS(numeric n)`                                                            | numeric                         | Returns the absolute value.                                                                                                                                                                                                                      |
| `COALESCE(args a)`                                                          | typeof first non-null a OR null | Returns the first non-null value or null if all are null.                                                                                                                                                                                        |
| `CAST(value AS type)`                                                       | type                            | Converts the given value to the specified data type.                                                                                                                                                                                             |
| `LENGTH(string s)`                                                          | integer                         | Returns the number of characters in the string.                                                                                                                                                                                                  |
| `TRIM(string s)`                                                            | string                          | Removes leading and trailing whitespace from the string.                                                                                                                                                                                         |
| `REPLACE(string s, string from, string to)`                                 | string                          | Replaces occurrences of a substring within a string with another substring.                                                                                                                                                                      |
| `SUBSTRING(string s, int start, int length)`                                | string                          | Extracts a substring from a string, starting at a given position and for a specified length.                                                                                                                                                     |
| `REVERSE(string s)`                                                         | string                          | Returns the string with characters in reverse order.                                                                                                                                                                                             |
| `STRPOS(string s, string substring)`                                        | integer                         | Returns the first index position of the substring in a given string, or 0 if there is no match.                                                                                                                                                  |
| `SPLIT_PART(string s, string delimiter, integer index)`                     | string                          | Splits the string on the given delimiter and returns the string at the given position counting from one.                                                                                                                                         |
| `EXTRACT(unit from timestamp/interval)`                                     | numeric                         | Extracts a part of a date or time field (such as year or month) from a timestamp or interval.                                                                                                                                                    |
| `TO_TIMESTAMP(string timestamp, string format)`                             | timestamp                       | Converts a string to a timestamp according to the given format.                                                                                                                                                                                  |
| `TO_TIMESTAMP(numeric epoch)`                                               | timestamp                       | Converts a UNIX epoch timestamp (in seconds) to a timestamp.                                                                                                                                                                                     |
| `TO_CHAR(timestamp t, string format)`                                       | string                          | Converts a timestamp to a string according to the given format.                                                                                                                                                                                  |
| `DATE_BIN(interval stride, timestamp source, timestamp origin)`             | timestamp                       | Aligns a timestamp (source) to buckets of even length (stride). Returns the start of the bucket containing the source, calculated as the largest timestamp that is less than or equal to source and is a multiple of stride lengths from origin. |
| `DATE_TRUNC(string unit, timestamp t)`                                      | timestamp                       | Truncates a timestamp to a specified precision based on the provided unit.                                                                                                                                                                       |
| `CURRENT_SETTING(string setting_name)`                                      | string                          | Returns the current value of the specified setting. Supports the parameters `dd.time_frame_start` and `dd.time_frame_end`, which return the start and end of the global time frame, respectively.                                                |
| `NOW()`                                                                     | timestamp                       | Returns the current timestamp at the start of the current query.                                                                                                                                                                                 |
| `CARDINALITY(array a)`                                                      | integer                         | Returns the number of elements in the array.                                                                                                                                                                                                     |
| `ARRAY_POSITION(array a, typeof_array value)`                               | integer                         | Returns the index of the first occurrence of the value found in the array, or null if value is not found.                                                                                                                                        |
| `STRING_TO_ARRAY(string s, string delimiter)`                               | array of strings                | Splits the given string into an array of strings using the given delimiter.                                                                                                                                                                      |
| `ARRAY_TO_STRING(array a, string delimiter)`                                | string                          | Converts an array to a string by concatenating elements with the given delimiter.                                                                                                                                                                |
| `ARRAY_AGG(expression e)`                                                   | array of input type             | Creates an array by collecting all the input values.                                                                                                                                                                                             |
| `APPROX_PERCENTILE(double percentile) WITHIN GROUP (ORDER BY expression e)` | typeof expression               | Computes an approximate percentile value. The percentile must be between 0.0 and 1.0 (inclusive). Requires the `WITHIN GROUP (ORDER BY ...)` syntax.                                                                                             |
| `UNNEST(array a [, array b...])`                                            | rows of a [, bâ¦]                | Expands arrays into a set of rows. This form is only allowed in a FROM clause.                                                                                                                                                                   |

{% collapsible-section %}
### Examples

### `MIN`{% #min %}

```sql
SELECT MIN(response_time) AS min_response_time
FROM logs
WHERE status_code = 200
```

### `MAX`{% #max %}

```sql
SELECT MAX(response_time) AS max_response_time
FROM logs
WHERE status_code = 200
```

### `COUNT`{% #count %}

```sql
SELECT COUNT(request_id) AS total_requests
FROM logs
WHERE status_code = 200 
```

### `SUM`{% #sum %}

```sql
SELECT SUM(bytes_transferred) AS total_bytes
FROM logs
GROUP BY service_name
```

### `AVG`{% #avg %}

```sql
SELECT AVG(response_time)
AS avg_response_time
FROM logs
WHERE status_code = 200
GROUP BY service_name
```

### `BOOL_AND`{% #bool_and %}

```sql
SELECT BOOL_AND(status_code = 200) AS all_success
FROM logs
```

### `BOOL_OR`{% #bool_or %}

```sql
SELECT BOOL_OR(status_code = 200) AS some_success
FROM logs
```

### `CEIL`{% #ceil %}

```sql
SELECT CEIL(price) AS rounded_price
FROM products
```

### `FLOOR`{% #floor %}

```sql
SELECT FLOOR(price) AS floored_price
FROM products
```

### `ROUND`{% #round %}

```sql
SELECT ROUND(price) AS rounded_price
FROM products
```

### `POWER`{% #power %}

```sql
SELECT POWER(response_time, 2) AS squared_response_time
FROM logs
```

### `LOWER`{% #lower %}

```sql
SELECT LOWER(customer_name) AS lowercase_name
FROM customers
```

### `UPPER`{% #upper %}

```sql
SELECT UPPER(customer_name) AS uppercase_name
FROM customers
```

### `ABS`{% #abs %}

```sql
SELECT ABS(balance) AS absolute_balance
FROM accounts
```

### `COALESCE`{% #coalesce %}

```sql
SELECT COALESCE(phone_number, email) AS contact_info
FROM users
```

### `CAST`{% #cast %}

Supported cast target types:

- `BIGINT`
- `DECIMAL`
- `TIMESTAMP`
- `VARCHAR`

```sql
SELECT
  CAST(order_id AS VARCHAR) AS order_id_string,
  'Order-' || CAST(order_id AS VARCHAR) AS order_label
FROM
  orders
```

### `LENGTH`{% #length %}

```sql
SELECT
  customer_name,
  LENGTH(customer_name) AS name_length
FROM
  customers
```

### `INTERVAL`{% #interval %}

```sql
SELECT
  TIMESTAMP '2023-10-01 10:00:00' + INTERVAL '30 days' AS future_date,
  INTERVAL '1 MILLISECOND 2 SECONDS 3 MINUTES 4 HOURS 5 DAYS'
```

### `TRIM`{% #trim %}

```sql
SELECT
  TRIM(name) AS trimmed_name
FROM
  users
```

### `REPLACE`{% #replace %}

```sql
SELECT
  REPLACE(description, 'old', 'new') AS updated_description
FROM
  products
```

### `SUBSTRING`{% #substring %}

```sql
SELECT
  SUBSTRING(title, 1, 10) AS short_title
FROM
  books
```

### `REVERSE`{% #reverse %}

```sql
SELECT
  REVERSE(username) AS reversed_username
FROM
  users
LIMIT 5
```

### `STRPOS`{% #strpos %}

```sql
SELECT
  STRPOS('foobar', 'bar')
```

### `SPLIT_PART`{% #split_part %}

```sql
SELECT
  SPLIT_PART('aaa-bbb-ccc', '-', 2)
```

### `EXTRACT`{% #extract %}

Supported extraction units:

| Literal           | Input Type               | Description                                  |
| ----------------- | ------------------------ | -------------------------------------------- |
| `day`             | `timestamp` / `interval` | day of the month                             |
| `dow`             | `timestamp`              | day of the week `1` (Monday) to `7` (Sunday) |
| `doy`             | `timestamp`              | day of the year (`1` - `366`)                |
| `hour`            | `timestamp` / `interval` | hour of the day (`0` - `23`)                 |
| `minute`          | `timestamp` / `interval` | minute of the hour (`0` - `59`)              |
| `second`          | `timestamp` / `interval` | second of the minute (`0` - `59`)            |
| `week`            | `timestamp`              | week of the year (`1` - `53`)                |
| `month`           | `timestamp`              | month of the year (`1` - `12`)               |
| `quarter`         | `timestamp`              | quarter of the year (`1` - `4`)              |
| `year`            | `timestamp`              | year                                         |
| `timezone_hour`   | `timestamp`              | hour of the time zone offset                 |
| `timezone_minute` | `timestamp`              | minute of the time zone offset               |

```sql
SELECT
  EXTRACT(year FROM purchase_date) AS purchase_year
FROM
  sales
```

### `TO_TIMESTAMP`{% #to_timestamp %}

`TO_TIMESTAMP` has two forms:

**Form 1: Convert string to timestamp with format**

Supported patterns for date/time formatting:

| Pattern     | Description                          |
| ----------- | ------------------------------------ |
| `YYYY`      | year (4 digits)                      |
| `YY`        | year (2 digits)                      |
| `MM`        | month number (01 - 12)               |
| `DD`        | day of month (01 - 31)               |
| `HH24`      | hour of day (00 - 23)                |
| `HH12`      | hour of day (01 - 12)                |
| `HH`        | hour of day (01 - 12)                |
| `MI`        | minute (00 - 59)                     |
| `SS`        | second (00 - 59)                     |
| `MS`        | millisecond (000 - 999)              |
| `TZ`        | time-zone abbreviation               |
| `OF`        | time-zone offset from UTC            |
| `AM` / `am` | meridiem indicator (without periods) |
| `PM` / `pm` | meridiem indicator (without periods) |

```sql
SELECT
  TO_TIMESTAMP('25/12/2025 04:23 pm', 'DD/MM/YYYY HH:MI am') AS ts
```

**Form 2: Convert UNIX epoch timestamp to timestamp**

```sql
SELECT
  TO_TIMESTAMP(1735142580) AS ts_from_epoch
```

### `TO_CHAR`{% #to_char %}

Supported patterns for date/time formatting:

| Pattern     | Description                          |
| ----------- | ------------------------------------ |
| `YYYY`      | year (4 digits)                      |
| `YY`        | year (2 digits)                      |
| `MM`        | month number (01 - 12)               |
| `DD`        | day of month (01 - 31)               |
| `HH24`      | hour of day (00 - 23)                |
| `HH12`      | hour of day (01 - 12)                |
| `HH`        | hour of day (01 - 12)                |
| `MI`        | minute (00 - 59)                     |
| `SS`        | second (00 - 59)                     |
| `MS`        | millisecond (000 - 999)              |
| `TZ`        | time-zone abbreviation               |
| `OF`        | time-zone offset from UTC            |
| `AM` / `am` | meridiem indicator (without periods) |
| `PM` / `pm` | meridiem indicator (without periods) |

```sql
SELECT
  TO_CHAR(order_date, 'MM-DD-YYYY') AS formatted_date
FROM
  orders
```

### `DATE_BIN`{% #date_bin %}

```sql
SELECT DATE_BIN('15 minutes', TIMESTAMP '2025-09-15 12:34:56', TIMESTAMP '2025-01-01')
-- Returns 2025-09-15 12:30:00

SELECT DATE_BIN('1 day', TIMESTAMP '2025-09-15 12:34:56', TIMESTAMP '2025-01-01')
-- Returns 2025-09-15 00:00:00
```

### `DATE_TRUNC`{% #date_trunc %}

Supported truncations:

- `milliseconds`
- `seconds` / `second`
- `minutes` / `minute`
- `hours` / `hour`
- `days` / `day`
- `weeks` / `week`
- `months` / `month`
- `quarters` / `quarter`
- `years` / `year`

```sql
SELECT
  DATE_TRUNC('month', event_time) AS month_start
FROM
  events
```

### `CURRENT_SETTING`{% #current_setting %}

Supported setting parameters:

- `dd.time_frame_start`: Returns the start of the selected time frame in RFC 3339 format (`YYYY-MM-DD HH:mm:ss.sssÂ±HH:mm`).
- `dd.time_frame_end`: Returns the end of the selected time frame in RFC 3339 format (`YYYY-MM-DD HH:mm:ss.sssÂ±HH:mm`).

```sql
-- Define the current analysis window
WITH bounds AS (
  SELECT CAST(CURRENT_SETTING('dd.time_frame_start') AS TIMESTAMP) AS time_frame_start,
         CAST(CURRENT_SETTING('dd.time_frame_end')   AS TIMESTAMP) AS time_frame_end
),
-- Define the immediately preceding window of equal length
     previous_bounds AS (
  SELECT time_frame_start - (time_frame_end - time_frame_start) AS prev_time_frame_start,
         time_frame_start                                       AS prev_time_frame_end
  FROM bounds
)
SELECT * FROM bounds, previous_bounds
```

### `NOW`{% #now %}

```sql
SELECT
  *
FROM
  sales
WHERE
  purchase_date > NOW() - INTERVAL '1 hour'
```

### `CARDINALITY`{% #cardinality %}

```sql
SELECT
  CARDINALITY(recipients)
FROM
  emails
```

### `ARRAY_POSITION`{% #array_position %}

```sql
SELECT
  ARRAY_POSITION(recipients, 'hello@example.com')
FROM
  emails
```

### `STRING_TO_ARRAY`{% #string_to_array %}

```sql
SELECT
  STRING_TO_ARRAY('a,b,c,d,e,f', ',')
```

### `ARRAY_TO_STRING`{% #array_to_string %}

```sql
SELECT
  ARRAY_TO_STRING(ARRAY['a', 'b', 'c'], ',') AS joined_string
```

### `ARRAY_AGG`{% #array_agg %}

```sql
SELECT
  sender,
  ARRAY_AGG(subject) subjects,
  ARRAY_AGG(ALL subject) all_subjects,
  ARRAY_AGG(DISTINCT subject) distinct_subjects
FROM
  emails
GROUP BY
  sender
```

### `APPROX_PERCENTILE`{% #approx_percentile %}

```sql
-- Calculate the median (50th percentile) response time
SELECT
  APPROX_PERCENTILE(0.5) WITHIN GROUP (ORDER BY response_time) AS median_response_time
FROM
  logs

-- Calculate 95th and 99th response time percentiles by service
SELECT
  service_name,
  APPROX_PERCENTILE(0.95) WITHIN GROUP (ORDER BY response_time) AS p95_response_time,
  APPROX_PERCENTILE(0.99) WITHIN GROUP (ORDER BY response_time) AS p99_response_time
FROM
  logs
GROUP BY
  service_name
```

### `UNNEST`{% #unnest %}

```sql
SELECT
  sender,
  recipient
FROM
  emails,
  UNNEST(recipients) AS recipient
```

{% /collapsible-section %}

## Regular expressions{% #regular-expressions %}

### Flavor{% #flavor %}

All regular expression (regex) functions use the International Components for Unicode (ICU) flavor:

- [Metacharacters](https://unicode-org.github.io/icu/userguide/strings/regexp.html#regular-expression-metacharacters)
- [Operators](https://unicode-org.github.io/icu/userguide/strings/regexp.html#regular-expression-operators)
- [Set Expressions (Character Classes)](https://unicode-org.github.io/icu/userguide/strings/regexp.html#set-expressions-character-classes)
- [Flag Options for in-pattern flags](https://unicode-org.github.io/icu/userguide/strings/regexp.html#flag-options). Refer to the flags section below for function-level flags.
- [Find and Replace (using capture groups)](https://unicode-org.github.io/icu/userguide/strings/regexp.html#find-and-replace)

### Functions{% #functions-1 %}

| Function                                                                                                         | Return Type      | Description                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REGEXP_LIKE(string input, string pattern)`                                                                      | Boolean          | Evaluates whether a string matches a regular expression pattern.                                                                                                                                                                                             |
| `REGEXP_MATCH(string input, string pattern [, string flags ])`                                                   | array of strings | Returns substrings of the first pattern match in the string.This function searches the input string using the given pattern and returns captured substrings (capture groups) from the first match. If no capture groups are present, returns the full match. |
| `REGEXP_REPLACE(string input, string pattern, string replacement [, string flags ])`                             | string           | Replaces the substring that is the first match to the pattern, or all such matches if you use the optional `g` flag.                                                                                                                                         |
| `REGEXP_REPLACE (string input, string pattern, string replacement, integer start, integer N [, string flags ] )` | string           | Replaces the substring that is the Nth match to the pattern, or all such matches if `N` is zero, starting from `start`.                                                                                                                                      |

{% collapsible-section %}
### Examples

### `REGEXP_LIKE`{% #regexp_like %}

```sql
SELECT
  *
FROM
  emails
WHERE
  REGEXP_LIKE(email_address, '@example\.com$')
```

### `REGEXP_MATCH`{% #regexp_match %}

```sql
SELECT regexp_match('foobarbequebaz', '(bar)(beque)');
-- {bar,beque}

SELECT regexp_match('foobarbequebaz', 'barbeque');
-- {barbeque}

SELECT regexp_match('abc123xyz', '([a-z]+)(\d+)(x(.)z)');
-- {abc,123,xyz,y}
```

### `REGEXP_REPLACE`{% #regexp_replace %}

```sql
SELECT regexp_replace('Auth success token=abc123XYZ789', 'token=\w+', 'token=***');
-- Auth success token=***

SELECT regexp_replace('status=200 method=GET', 'status=(\d+) method=(\w+)', '$2: $1');
-- GET: 200

SELECT regexp_replace('INFO INFO INFO', 'INFO', 'DEBUG', 1, 2);
-- INFO DEBUG INFO
```

{% /collapsible-section %}

### Function-level flags{% #function-level-flags %}

You can use the following flags with regular expression functions:

{% dl %}

{% dt %}
`i`
{% /dt %}

{% dd %}
Case-insensitive matching
{% /dd %}

{% dt %}
`n` or `m`
{% /dt %}

{% dd %}
Newline-sensitive matching
{% /dd %}

{% dt %}
`g`
{% /dt %}

{% dd %}
Global; replace *all* matching substrings rather than only the first one
{% /dd %}

{% /dl %}

{% collapsible-section %}
### Examples

### `i` flag{% #i-flag %}

```sql
SELECT regexp_match('INFO', 'info')
-- NULL

SELECT regexp_match('INFO', 'info', 'i')
-- ['INFO']
```

### `n` flag{% #n-flag %}

```sql
SELECT regexp_match('a
b', '^b');
-- NULL

SELECT regexp_match('a
b', '^b', 'n');
-- ['b']
```

### `g` flag{% #g-flag %}

```sql
SELECT icu_regexp_replace('Request id=12345 completed, id=67890 pending', 'id=\d+', 'id=XXX');
-- Request id=XXX completed, id=67890 pending

SELECT regexp_replace('Request id=12345 completed, id=67890 pending', 'id=\d+', 'id=XXX', 'g');
-- Request id=XXX completed, id=XXX pending
```

{% /collapsible-section %}

## Window functions{% #window-functions %}

This table provides an overview of the supported window functions. For comprehensive details and examples, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-window.html).

| Function                      | Return Type   | Description                                                                         |
| ----------------------------- | ------------- | ----------------------------------------------------------------------------------- |
| `OVER`                        | N/A           | Defines a window for a set of rows for other window functions to operate on.        |
| `PARTITION BY`                | N/A           | Divides the result set into partitions, specifically for applying window functions. |
| `RANK()`                      | integer       | Assigns a rank to each row within a partition, with gaps for ties.                  |
| `ROW_NUMBER()`                | integer       | Assigns a unique sequential number to each row within a partition.                  |
| `LEAD(column n)`              | typeof column | Returns the value from the next row in the partition.                               |
| `LAG(column n)`               | typeof column | Returns the value from the previous row in the partition.                           |
| `FIRST_VALUE(column n)`       | typeof column | Returns the first value in an ordered set of values.                                |
| `LAST_VALUE(column n)`        | typeof column | Returns the last value in an ordered set of values.                                 |
| `NTH_VALUE(column n, offset)` | typeof column | Returns the value at the specified offset in an ordered set of values.              |

## JSON functions and operators{% #json-functions-and-operators %}

| Name                                          | Return type  | Description                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| json_extract_path_text(text json, text pathâ¦) | text         | Extracts a JSON sub-object as text, defined by the path. Its behavior is equivalent to the [Postgres function with the same name](https://www.postgresql.org/docs/current/functions-json.html). For example, `json_extract_path_text(col, âforest')` returns the value of the key `forest` for each JSON object in `col`. See the example below for a JSON array syntax. |
| json_extract_path(text json, text pathâ¦)      | JSON         | Same functionality as `json_extract_path_text`, but returns a column of JSON type instead of text type.                                                                                                                                                                                                                                                                  |
| json_array_elements(text json)                | rows of JSON | Expands a JSON array into a set of rows. This form is only allowed in a FROM clause.                                                                                                                                                                                                                                                                                     |
| json_array_elements_text(text json)           | rows of text | Expands a JSON array into a set of rows. This form is only allowed in a FROM clause.                                                                                                                                                                                                                                                                                     |

## Table functions{% #table-functions %}

{% callout %}
##### Join the Preview!

Querying Logs and Metrics through DDSQL is in Preview. Use this form to request access.

[Request Access](https://www.datadoghq.com/product-preview/logs-metrics-support-in-ddsql-editor/)
{% /callout %}

Table functions are used to query Logs and Metrics

| Function                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dd.logs(
    filter => varchar,
    columns => array < varchar >,
    indexes ? => array < varchar >,
    from_timestamp ? => timestamp,
    to_timestamp ? => timestamp
) AS (column_name type [, ...]) | Returns log data as a table. The columns parameter specifies which log fields to extract, and the AS clause defines the schema of the returned table. Optional: filtering by index or time range. When time is not specified, we default to the past 1 hour of data. | ```sql
  SELECT timestamp, host, service, message
  FROM dd.logs(
      filter  => 'source:java',
      columns => ARRAY['timestamp','host', 'service','message']
  ) AS (
      timestamp TIMESTAMP,
      host      VARCHAR,
      service   VARCHAR,
      message   VARCHAR
  )
``` |
| dd.metrics_scalar(
    query varchar,
    reducer varchar [, from_timestamp timestamp, to_timestamp timestamp]
)                                                                                         | Returns metric data as a scalar value. The function accepts a metrics query (with optional grouping), a reducer to determine how values are aggregated (avg, max, etc.), and optional timestamp parameters (default 1 hour) to define the time range.                | ```sql
  SELECT *
  FROM dd.metrics_scalar(
      'avg:system.cpu.user{*} by {service}',
      'avg',
      TIMESTAMP '2025-07-10 00:00:00.000-04:00',
      TIMESTAMP '2025-07-17 00:00:00.000-04:00'
  )
  ORDER BY value DESC;
```                                                   |
| dd.metrics_timeseries(
    query varchar [, from_timestamp timestamp, to_timestamp timestamp]
)                                                                                                          | Returns metric data as a timeseries. The function accepts a metrics query (with optional grouping) and optional timestamp parameters (default 1 hour) to define the time range. Returns data points over time rather than a single aggregated value.                 | ```sql
  SELECT *
  FROM dd.metrics_timeseries(
      'avg:system.cpu.user{*} by {service}',
      TIMESTAMP '2025-07-10 00:00:00.000-04:00',
      TIMESTAMP '2025-07-17 00:00:00.000-04:00'
  )
  ORDER BY timestamp, service;
```                                                    |

## Tags{% #tags %}

DDSQL exposes tags as an `hstore` type, which is inspired by PostgreSQL. You can access the values for specific tag keys using the PostgreSQL arrow operator. For example:

```sql
SELECT instance_type, count(instance_type)
FROM aws.ec2_instance
WHERE tags->'region' = 'us-east-1' -- region is a tag, not a column
GROUP BY instance_type
```

Tags are key-value pairs where each key can have zero, one, or multiple tag values corresponding to it. When accessed, the tag value returns a single string, containing *all* corresponding values. When the data has multiple tag values for the same tag key, they are represented as a sorted, comma-separated string. For example:

```sql
SELECT tags->'team', instance_type, architecture, COUNT(*) as instance_count
FROM aws.ec2_instance
WHERE tags->'team' = 'compute_provisioning,database_ops'
GROUP BY tags->'team', instance_type, architecture
ORDER BY instance_count DESC
```

You can also compare tag values as strings or entire tag sets:

```sql
SELECT *
FROM k8s.daemonsets da INNER JOIN k8s.deployments de
ON da.tags = de.tags -- for a specific tag: da.tags->'app' = de.tags->'app'
```

Additionally, you can extract tag keys and values into individual arrays of text:

```sql
SELECT akeys(tags), avals(tags)
FROM aws.ec2_instance
```

### HSTORE functions and operators{% #hstore-functions-and-operators %}

| Name               | Return type   | Description                                                           |
| ------------------ | ------------- | --------------------------------------------------------------------- |
| tags -> 'text'     | Text          | Gets the value for a given key. Returns `null` if key is not present. |
| akeys(hstore tags) | Array of text | Gets the keys of an HSTORE as an array                                |
| avals(hstore tags) | Array of text | Gets the values of an HSTORE as an array                              |

## Further reading{% #further-reading %}

- [Learn more about DDSQL Editor](https://docs.datadoghq.com/ddsql_editor/)
