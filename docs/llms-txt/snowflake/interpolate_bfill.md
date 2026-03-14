# Source: https://docs.snowflake.com/en/sql-reference/functions/interpolate_bfill.md

Categories:
:   [Window functions](../functions-window.md) (General)

# INTERPOLATE_BFILL, INTERPOLATE_FFILL, INTERPOLATE_LINEAR

Updates rows in a time-series data set to gap-fill missing values based on surrounding values.

You can call the following interpolation window functions:

* INTERPOLATE_BFILL: Gap-fills rows based on the next observed row.
* INTERPOLATE_FFILL: Gap-fills rows based on the previously observed row.
* INTERPOLATE_LINEAR: Gap-fills rows based on the linear interpolation of previous and next values. This function
  only supports numeric values.

These functions have the same [window function syntax](../functions-window-syntax.md). They don’t
support explicit window frames.

## Syntax

```sqlsyntax
INTERPOLATE_BFILL( <expr> )
  OVER ( [ PARTITION BY <expr1> ] ORDER BY <expr2> [ { ASC | DESC } ] [ NULLS { FIRST | LAST } ] )
```

```sqlsyntax
INTERPOLATE_FFILL( <expr> )
  OVER ( [ PARTITION BY <expr1> ] ORDER BY <expr2> [ { ASC | DESC } ] [ NULLS { FIRST | LAST } ] )
```

```sqlsyntax
INTERPOLATE_LINEAR( <expr> )
  OVER ( [ PARTITION BY <expr1> ] ORDER BY <expr2> [ { ASC | DESC } ] [ NULLS { FIRST | LAST } ] )
```

## Arguments

`expr`
:   An expression that defines the column that you want to gap-fill.

    The INTERPOLATE_LINEAR input expression must be a numeric data type.

    The INTERPOLATE_BFILL and INTERPOLATE_FFILL input expressions do not support [geospatial data types](../data-types-geospatial.md).

## Parameters

`OVER`
:   Standard window function OVER clause. See [Window function syntax and usage](../functions-window-syntax.md). For the interpolation functions, the
    PARTITION BY clause is optional, but the ORDER BY clause is required. You can’t specify an explicit window frame.

    The INTERPOLATE_LINEAR function can have only one ORDER BY expression, and it must be a numeric, DATE, or TIMESTAMP expression (including all TIMESTAMP variants).

## Returns

These functions return the same data type as the data type of the input expression.

## Usage notes

* When you use INTERPOLATE window functions with the [RESAMPLE](../constructs/resample.md) clause, include the columns to partition by in both PARTITION BY clauses: RESAMPLE (PARTITION BY) and INTERPOLATE (PARTITION BY). This approach ensures that:

  * RESAMPLE generates rows with non-NULL values for the partition columns.
  * INTERPOLATE functions operate within the correct partitions.
  * Any WHERE clause filters preserve the generated rows for the partitions you want to keep.

  For examples of using INTERPOLATE with RESAMPLE, see [Filling gaps in time-series data](../../user-guide/querying-time-series-data.md).

## Examples

The following examples show how to use the interpolation functions in simple queries.

### Example with two interpolation functions

The following example returns resampled `temperature` values and two different interpolated `temperature` values in the same query. (The table `march_temps_every_five_mins` was created earlier in this topic.)

```sqlexample
SELECT observed,
    temperature,
    INTERPOLATE_BFILL(temperature) OVER (PARTITION BY city, county ORDER BY observed) bfill_temp,
    INTERPOLATE_FFILL(temperature) OVER (PARTITION BY city, county ORDER BY observed) ffill_temp,
    city,
    county
  FROM march_temps_every_five_mins
  ORDER BY observed;
```

```output
+-------------------------+-------------+------------+------------+------------------+----------------+
| OBSERVED                | TEMPERATURE | BFILL_TEMP | FFILL_TEMP | CITY             | COUNTY         |
|-------------------------+-------------+------------+------------+------------------+----------------|
| 2025-03-15 09:45:00.000 |        NULL |         48 |       NULL | Big Bear City    | San Bernardino |
| 2025-03-15 09:49:00.000 |          48 |         48 |         48 | Big Bear City    | San Bernardino |
| 2025-03-15 09:50:00.000 |        NULL |         49 |         48 | Big Bear City    | San Bernardino |
| 2025-03-15 09:50:00.000 |          44 |         44 |         44 | South Lake Tahoe | El Dorado      |
| 2025-03-15 09:55:00.000 |          49 |         49 |         49 | Big Bear City    | San Bernardino |
| 2025-03-15 09:55:00.000 |          46 |         46 |         46 | South Lake Tahoe | El Dorado      |
| 2025-03-15 10:00:00.000 |        NULL |         51 |         49 | Big Bear City    | San Bernardino |
| 2025-03-15 10:00:00.000 |        NULL |         52 |         46 | South Lake Tahoe | El Dorado      |
| 2025-03-15 10:05:00.000 |        NULL |         51 |         49 | Big Bear City    | San Bernardino |
| 2025-03-15 10:05:00.000 |        NULL |         52 |         46 | South Lake Tahoe | El Dorado      |
| 2025-03-15 10:10:00.000 |          51 |         51 |         51 | Big Bear City    | San Bernardino |
| 2025-03-15 10:10:00.000 |          52 |         52 |         52 | South Lake Tahoe | El Dorado      |
| 2025-03-15 10:15:00.000 |        NULL |         54 |         51 | Big Bear City    | San Bernardino |
| 2025-03-15 10:15:00.000 |          54 |         54 |         54 | South Lake Tahoe | El Dorado      |
| 2025-03-15 10:18:00.000 |          54 |         54 |         54 | Big Bear City    | San Bernardino |
+-------------------------+-------------+------------+------------+------------------+----------------+
```

The `bfill_temp` column returns a meaningful value for every row, but `ffill_temp` returns NULL
for the first row. The INTERPOLATE_FFILL function requires a previous value in order to return a non-NULL result.
The INTERPOLATE_BFILL function only requires a next value.

### Example of an expected error for an explicit window frame

The following query returns an error because the interpolation functions do not support explicit window frames:

```sqlexample
SELECT observed, temperature,
    INTERPOLATE_BFILL(temperature)
      OVER (PARTITION BY city, county ORDER BY observed ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) bfill_temp,
    city, county
  FROM march_temps_every_five_mins
  ORDER BY observed;
```

```output
002303 (0A000): SQL compilation error: error line 1 at position 111
Sliding window frame unsupported for function INTERPOLATE_BFILL
```
