# Source: https://clickhouse.ferndocs.com/reference/sql-reference/window-functions/lagInFrame.md

---
description: Documentation for the lagInFrame window function
sidebar_label: lagInFrame
sidebar_position: 9
slug: /sql-reference/window-functions/lagInFrame
title: lagInFrame
doc_type: reference
---

Returns a value evaluated at the row that is at a specified physical offset row before the current row within the ordered frame.

<Warning>
`lagInFrame` behavior differs from the standard SQL `lag` window function.
Clickhouse window function `lagInFrame` respects the window frame.
To get behavior identical to the `lag`, use `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.
</Warning>

**Syntax**

```sql
lagInFrame(x[, offset[, default]])
  OVER ([[PARTITION BY grouping_column] [ORDER BY sorting_column]
        [ROWS or RANGE expression_to_bound_rows_withing_the_group]] | [window_name])
FROM table_name
WINDOW window_name as ([[PARTITION BY grouping_column] [ORDER BY sorting_column])
```

For more detail on window function syntax see: [Window Functions - Syntax](./index.md/#syntax).

**Parameters**
- `x` — Column name.
- `offset` — Offset to apply. [(U)Int*](../data-types/int-uint.md). (Optional - `1` by default).
- `default` — Value to return if calculated row exceeds the boundaries of the window frame. (Optional - default value of column type when omitted).

**Returned value**

- Value evaluated at the row that is at a specified physical offset before the current row within the ordered frame.

**Example**

This example looks at historical data for a specific stock and uses the `lagInFrame` function to calculate a day-to-day delta and percentage change in the closing price of the stock.

Query:

```sql
CREATE TABLE stock_prices
(
    `date`   Date,
    `open`   Float32, -- opening price
    `high`   Float32, -- daily high
    `low`    Float32, -- daily low
    `close`  Float32, -- closing price
    `volume` UInt32   -- trade volume
)
Engine = Memory;

INSERT INTO stock_prices FORMAT Values
    ('2024-06-03', 113.62, 115.00, 112.00, 115.00, 438392000),
    ('2024-06-04', 115.72, 116.60, 114.04, 116.44, 403324000),
    ('2024-06-05', 118.37, 122.45, 117.47, 122.44, 528402000),
    ('2024-06-06', 124.05, 125.59, 118.32, 121.00, 664696000),
    ('2024-06-07', 119.77, 121.69, 118.02, 120.89, 412386000);
```

```sql
SELECT
    date,
    close,
    lagInFrame(close, 1, close) OVER (ORDER BY date ASC
       ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
     ) AS previous_day_close,
    COALESCE(ROUND(close - previous_day_close, 2)) AS delta,
    COALESCE(ROUND((delta / previous_day_close) * 100, 2)) AS percent_change
FROM stock_prices
ORDER BY date DESC
```

Result:

```response
   ┌───────date─┬──close─┬─previous_day_close─┬─delta─┬─percent_change─┐
1. │ 2024-06-07 │ 120.89 │                121 │ -0.11 │          -0.09 │
2. │ 2024-06-06 │    121 │             122.44 │ -1.44 │          -1.18 │
3. │ 2024-06-05 │ 122.44 │             116.44 │     6 │           5.15 │
4. │ 2024-06-04 │ 116.44 │                115 │  1.44 │           1.25 │
5. │ 2024-06-03 │    115 │                115 │     0 │              0 │
   └────────────┴────────┴────────────────────┴───────┴────────────────┘
```
