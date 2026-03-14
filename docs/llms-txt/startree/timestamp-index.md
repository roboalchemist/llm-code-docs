# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/timestamp-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Timestamp Index

> The Timestamp index accelerates time-based queries by pre-computing and indexing multiple time granularities to optimize filtering and grouping operations.

## Overview and Purpose

A timestamp index is a specialized indexing solution that accelerates time-based queries with different time granularities. It's designed to optimize analytics workflows that involve filtering and grouping by common time dimensions like day, month, or year.

The TIMESTAMP data type in StarTree Cloud stores values as millisecond-precision epoch timestamps (long values). While this high precision is valuable for exact timestamps, it's often excessive for analytical queries where users typically want to analyze data at coarser time granularities.

Timestamp indexes are particularly valuable for:

* Range queries on time columns (e.g., queries for specific date ranges)
* Group-by operations with different time granularities (day, week, month, year, etc.)
* Time-series analytics across large datasets
* Any query pattern that involves time transformations like `dateTrunc()` or `dateTimeConvert()`

<Info>
  Without a timestamp index, time-based queries require extracting values at query time, applying transformation functions, and then performing filters or group-by operations, which can be computationally expensive for large datasets.
</Info>

## How the Index Works

### Core Concepts

Traditional querying of timestamp data requires time value conversions and transformations to be computed at query time. For example, to group data by month, the system would need to convert each timestamp to its corresponding month for every record in the dataset.

The timestamp index in StarTree Cloud optimizes these operations by:

1. **Pre-computing Time Granularities**: During segment generation, the system pre-computes additional derived columns for each configured time granularity.
2. **Derived Column Generation**: For each time granularity (e.g., DAY, MONTH, YEAR), a separate derived column is created following the naming pattern `$${ts_column_name}$${ts_granularity}`.
3. **Automatic Range Indexing**: Range indexes are automatically built for all granularity columns, enabling efficient filtering on time ranges.
4. **Query Rewriting**: At query time, functions like `dateTrunc('DAY', timestamp_col)` are automatically rewritten to use the pre-computed columns, dramatically reducing computation overhead.

### Example Illustration

For a timestamp column named `event_time` with configured granularities DAY, MONTH, and YEAR:

1. Three additional derived columns are generated:
   * `$event_time$DAY` - containing day-level timestamps
   * `$event_time$MONTH` - containing month-level timestamps
   * `$event_time$YEAR` - containing year-level timestamps
2. When a query includes `dateTrunc('MONTH', event_time)`, it's automatically rewritten to use the `$event_time$MONTH` column instead of computing this transformation during query execution.
3. Similarly, a filter condition like `dateTrunc('YEAR', event_time) = '2022'` would use the `$event_time$YEAR` column's range index for efficient filtering.

## Configuration

### Enabling Timestamp Index

To enable a timestamp index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "event_time",
      "timestampConfig": {
        "granularities": [
          "DAY",
          "WEEK",
          "MONTH"
        ]
      }
    }
  ]
}
```

### Supported Granularities

The timestamp index supports the following granularities:

* `MILLISECOND`
* `SECOND`
* `MINUTE`
* `HOUR`
* `DAY`
* `WEEK`
* `MONTH`
* `QUARTER`
* `YEAR`

### Important Configuration Considerations

1. **Data Type Requirement**: Timestamp indexes can only be created on columns with the `TIMESTAMP` data type.
2. **Storage Implications**: Each configured granularity creates an additional derived column, which increases storage requirements. Choose granularities based on your common query patterns.
3. **Index Generation Timing**: Timestamp indexes are created during segment generation, not at query time.
4. **Performance Impact**: While timestamp indexes accelerate query performance, configuring too many granularities may impact segment generation time and storage requirements.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DetGpHZuzDU" title="YouTube video player" allow="fullscreen; accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" />

*Mark Needham demos the Timestamp Index*

Built with [Mintlify](https://mintlify.com).
