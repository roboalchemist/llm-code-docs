# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-from/copy-from-with-format.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# COPY FROM with FORMAT

## Overview

This version of a [`COPY FROM`](/sql-reference/sql-statements/copy-from/copy-from) statement, allows you to specify the imported file format and currently three types are supported.

<Note> With each file type there will be differences in performance and behavior</Note>

Here's a list of supported formats:

* **CSV** (comma-separated values): simple columnar text format
* **ORC** (optimized row columnar): columnar storage format developed by Apache
* **Parquet** (Apache Parquet): columnar data storage used in Apache Hadoop ecosystem

<Note>Each query **without** a specified file format assumes to be importing a CSV file (**There is no** format detection in place)</Note>

## Syntax

In order to sepcify the file format using the `COPY FROM` statement you can use the following syntax:

```sql  theme={null}
COPY tablename FROM 'file_path' (FORMAT format_name);
```

<Note>Format name is case insensitive</Note>

## Examples

When copying from the CSV, ORC or Parquet formats, as the first step you need to create a destination table:

```sql  theme={null}
CREATE TABLE cab_types (id bigint, cab_type text);
```

Once that is done, you can copy the file content into the table by following one of the examples below.

### ORC

Copying a dataset from an ORC format file is **only** supported if the ORC file resides in an object storage solution, such as an S3 bucket.

```sql  theme={null}
copy cab_types from 's3://oxla-testdata/cab_types.orc' (format orc, HEADER);
```

* Use `HEADER` if your ORC file includes column headers

### Parquet

Copying a dataset from a parquet format file is **only** supported if the parquet file resides in an object storage solution, such as an S3 bucket.

```sql  theme={null}
copy cab_types from 's3://oxla-testdata/cab_types.parquet' (format parquet);
```

<Warning>Copying from Parquet files is memory consuming. Files bigger than a few gigabytes might result in **out of memory** error</Warning>

### CSV

When it comes to CSV files, we have a few cases here:

* **CSV**

```sql  theme={null}
copy cab_types from 's3://oxla-testdata/cab_types.csv' (format csv);
```

* **CSV with Specified Delimiter**

```sql  theme={null}
copy cab_types from 's3://oxla-testdata/cab_types.csv' (format csv, delimiter ':');
```

* **CSV skipping invalid rows**

```sql  theme={null}
copy cab_types from 's3://oxla-testdata/cab_types.csv' (format csv, on_error stop|ignore);
```

By default invalid rows stops data ingestion and Oxla returns an error. Setting `on_error` action to `ignore` enforce further processing after skipping invalid rows.

## Differences in Behavior

* **Ignored Options**
  * `HEADER`, `DELIMITER`, `NULL`, `ON_ERROR` options are ignored not affecting the execution of the queries for formats different than CSV

* **Null Values Handling**
  * All ORC files have nullable columns. In order to import a nullable column to an Oxla column, which are described as `NOT NULL`, the column in the ORC file cannot contain a null value, otherwise the request will be terminated.
  * For Parquet files, inserting a nullable column to a non nullable column is allowed as long as there are no null values in the source column.
  * When using `ON_ERROR` option for CSV files, null constraint violation causes row skipping

* **Column Matching**
  * ORC and Parquet files are only being matched based on **column index**, while CSVs can be matched both with names or indexes. For more information regarding that, please refer to our [COPY FROM with HEADER doc](/sql-reference/sql-statements/copy-from/copy-from-with-header)
