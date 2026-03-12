# Source: https://clickhouse.ferndocs.com/reference/sql-reference/table-functions/timeSeriesMetrics.md

---

description: >-
  timeSeriesMetrics returns the metrics table used by table
  `db_name.time_series_table` whose table engine is the TimeSeries engine.
sidebar_label: timeSeriesMetrics
sidebar_position: 145
slug: /sql-reference/table-functions/timeSeriesMetrics
title: timeSeriesMetrics
doc_type: reference
---

`timeSeriesMetrics(db_name.time_series_table)` - Returns the [metrics](/reference/engines/table-engines/special/time_series#metrics-table) table
used by table `db_name.time_series_table` whose table engine is the [TimeSeries](/reference/engines/table-engines/special/time_series) engine:

```sql
CREATE TABLE db_name.time_series_table ENGINE=TimeSeries METRICS metrics_table
```

The function also works if the _metrics_ table is inner:

```sql
CREATE TABLE db_name.time_series_table ENGINE=TimeSeries METRICS INNER UUID '01234567-89ab-cdef-0123-456789abcdef'
```

The following queries are equivalent:

```sql
SELECT * FROM timeSeriesMetrics(db_name.time_series_table);
SELECT * FROM timeSeriesMetrics('db_name.time_series_table');
SELECT * FROM timeSeriesMetrics('db_name', 'time_series_table');
```
