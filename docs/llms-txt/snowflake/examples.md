# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/examples.md

# Common feature and query patterns

> **Note:**
>
> The Snowflake Feature Store API is available in the Snowpark ML Python package (`snowflake-ml-python`) v1.5.0 and later.

The `FeatureView` class accepts a Snowpark DataFrame object containing the feature transformation logic. You can
therefore describe your features in any way supported by the Snowpark DataFrame API or by Snowflake SQL. You can pass
the DataFrame to the `FeatureView` constructor directly.

The Snowpark Python API provides
[analytics functions](https://docs.snowflake.com/developer-guide/snowpark/reference/python/latest/snowpark/api/snowflake.snowpark.DataFrameAnalyticsFunctions)
for easily defining many common feature types, such as windowed aggregations. This topic contains some examples of these.

The open source [snowflake-ml-python](https://github.com/snowflakedb/snowflake-ml-python/tree/main/snowflake/ml/feature_store/examples)
on Github also contains some sample feature view and entity definitions using public datasets.

## Per-row features

In per-row features, functions are applied to each row of tabular data. For example, the following code fills null in
`foo` with zero, then computes a ZIP code from `lat` and `long`. There is one output row per input
row.

Python:

```python
def get_zipcode(df: snowpark.DataFrame) -> snowpark.DataFrame:
    df = df.fillna({"foo": 0})
    df = df.with_column(
        "zipcode",
        F.compute_zipcode(df["lat"], df["long"])
    )
    return df
```

Snowflake SQL:

```sqlexample
SELECT
    COALESCE(foo, 0) AS foo,
    compute_zipcode(lat, long) AS zipcode
FROM <source_table_name>;
```

## Per-group features

Per-group features aggregate values in a column within a group. For example, the sum of daily rainfall might be grouped
by city for weather forecasting. The output DataFrame has one row per group.

Python:

```python
def sum_rainfall(df: snowpark.DataFrame) -> snowpark.DataFrame:
    df = df.group_by(
        ["location", to_date(timestamp)]
    ).agg(
        sum("rain").alias("sum_rain"),
        avg("humidity").alias("avg_humidity")
    )
    return df
```

Snowflake SQL:

```sqlexample
SELECT
    location,
    TO_DATE(timestamp) AS date,
    SUM(rain) AS sum_rain,
    AVG(humidity) AS avg_humidity
FROM <source_table_name>
GROUP BY location, date;
```

## Row-based window features

Row-based window features aggregate values over a fixed window of rows; for example, summing the last three
transaction amounts. The output DataFrame has one row per window frame.

Python:

```python
def sum_past_3_transactions(df: snowpark.DataFrame) -> snowpark.DataFrame:
    window = Window.partition_by("id").order_by("ts").rows_between(2, Window.CURRENT_ROW)

    return df.select(
        sum("amount").over(window).alias("sum_past_3_transactions")
    )
```

Snowflake SQL:

```sqlexample
SELECT
    id,
    SUM(amount) OVER (PARTITION BY id ORDER BY ts ROWS BETWEEN 2 PRECEDING and 0 FOLLOWING)
        AS sum_past_3_transactions
FROM <source_table_name>;
```

## Moving aggregation features

Moving aggregation features calculate moving statistics, such as sum and average, within a specified window size.
This function dynamically computes these aggregates across different subsets of the DataFrame based on the defined
window sizes, order, and groupings. The output DataFrame has one row per window frame.

```python
new_df =  df.analytics.moving_agg(
    aggs={"SALESAMOUNT": ["SUM", "AVG"]},
    window_sizes=[2, 3],
    order_by=["ORDERDATE"],
    group_by=["PRODUCTKEY"]
)
```

## Cumulative aggregation features

Cumulative aggregation computes ongoing totals, minimums, maximums, and other cumulative statistics across a data
partition, which is sorted and grouped as specified. Unlike moving aggregates, these totals extend from the start of the
partition or to the end, depending on the direction specified, providing running totals that do not reset. The output
DataFrame has one row per input row.

```python
 new_df = df.analytics.cumulative_agg(
    aggs={"SALESAMOUNT": ["SUM", "MIN", "MAX"]},
    order_by=["ORDERDATE"],
    group_by=["PRODUCTKEY"],
    is_forward=True
)
```

## Lag features

Lag features introduce new columns containing values from prior rows within each partition, offset by a specified number
of rows. This function is critical for comparing current values against previous values in a dataset, thus assisting in
detecting trends or changes over time. The output DataFrame has one row per input row.

```python
new_df = df.analytics.compute_lag(
    cols=["SALESAMOUNT"],
    lags=[1, 2],
    order_by=["ORDERDATE"],
    group_by=["PRODUCTKEY"]
)
```

## Lead features

The inverse of lag features, lead features create new columns containing values from subsequent rows, shifting data
upward. This feature is essential for making predictions or assumptions based on future data points already present in a
dataset. The output DataFrame has one row per input row.

```python
new_df = df.analytics.compute_lead(
    cols=["SALESAMOUNT"],
    leads=[1, 2],
    order_by=["ORDERDATE"],
    group_by=["PRODUCTKEY"]
)
```

## Time-series features

Time-series features compute feature values based on a time window and a fixed position along the time axis. Examples
include the count of trips over the past week for rideshares or the sum of sales over the past three days. The output
DataFrame has one row per time window.

Recent versions of the Snowflake Feature Store include an experimental time series aggregation API. Using this API,
a time series feature can be created using code like the following:

Python:

```python
def custom_column_naming(input_col, agg, window):
    return f"{agg}_{input_col}_{window.replace('-', 'past_')}"

result_df = weather_df.analytics.time_series_agg(
    aggs={"rain": ["SUM"]},
    windows=["-3D", "-5D"],
    sliding_interval="1D",
    group_by=["location"],
    time_col="ts",
    col_formatter=custom_column_naming
)
```

You can also construct time-series features with RANGE BETWEEN syntax in SQL. for more details, see
[Snowflake Window functions](../../../sql-reference/functions-window.md).

Snowflake SQL:

```sqlexample
select
    TS,
    LOCATION,
    sum(RAIN) over (
        partition by LOCATION
        order by TS
        range between interval '3 days' preceding and current row
    ) SUM_RAIN_3D,
    sum(RAIN) over (
        partition by LOCATION
        order by TS
        range between interval '5 days' preceding and current row
    ) SUM_RAIN_5D
from <source_table_name>
```

## Using user-defined functions in feature pipelines

The Snowflake Feature Store supports user defined functions (UDFs) in feature pipeline definitions. However, only
deterministic functions (functions that always return the same result for the same input) can be incrementally
maintained. To enable incremental maintenance, mark your UDF as immutable when registering it.

```python
# In Python
@F.udf(
    name="MY_UDF",
    immutable=True,
    # ...
)
def my_udf(...):
    # ...
```

If your function is written in SQL, specify the IMMUTABLE keyword. See [this guide](../../../sql-reference/sql/create-function.md).
