# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/snowpark-connect-2026.md

# Snowpark Connect for Spark release notes for 2026

Snowflake uses semantic versioning for Snowpark Connect for Spark updates.

For documentation, see [Run Apache Spark™ workloads on Snowflake with Snowpark Connect for Spark](../../developer-guide/snowpark-connect/snowpark-connect-overview.md) and
[Submitting Spark applications](../../developer-guide/snowpark-connect/snowpark-submit.md).

## 1.14.0 (February 19, 2026)

### Snowpark Connect for Spark

#### Bug fixes

* Cache table type when running `saveAsTable`
* Optimize literal input for substring and type casting for `coalesce`
* Handle decimal overflow in `avg`/`mean` and fix decimal type coercion
* Iceberg - Preserve grants on overwrite
* Standardize SQL passthrough mode
* Optimize `from_utc_timestamp`/`to_utc_timestamp` for literal timezone
* Handle JSON null values in structured types to match Spark semantics
* Emulate integral types on creating tables from SQL
* Fix edge case with mapping nested rows in Scala UDFs
* Fix how Parquet handles read and write of complex structured datatypes
* Support save ignore argument for parquet files
* Add support for artifact repository
* Fix array nullability in Scala UDxF
* Fix `log1p` for args from (-1, 0) range
* Fix `first_value` and `last_value` in aggregate context
* Fix reading `DayTimeIntervalType` for Scala client

#### New features

* Handle timezones correctly in Scala UDFs
* Support Java 11 and 17 without any configuration

### Snowpark Submit updates

#### New features

* Support `snowpark-submit` for python 3.9
* Enhance `init_spark_session` to be usable in `snowpark-submit` workflow

## 1.13.0 (February 13, 2026)

### Snowpark Connect for Spark

#### Bug fixes

* Fixed `split` function issue
* Downgraded snowflake-snowpark-python dependency to version 1.44
* Fixed `Neo4j` dialect matching to improve SQL translation
* Fixed operation ID returned in execute responses to be consistent
* Fixed `gRPC` metadata handling for TCP channel connections

#### New features

* Added support for `partition_hint` in `mapPartitions` operations
* Added XML reader support for scenarios with user-defined schemas

## 1.11.0 (January 28, 2026)

### Snowpark Connect for Spark

#### Bug fixes

* Preserve hidden columns after various DataFrame operators
* Fix issues for scala udf input types (`byte`, `binary`, `scala.math.BigDecimal`)

#### Other updates

* Add `snowpark-submit` User Defined Args to comment

## 1.10.0 (January 22, 2026)

### Snowpark Connect for Spark

#### Bug fixes

* Fix config unset error for session configuration.
* Use copy into to load CSV files in parallel.
* Fix writes for DataFrames using outer joins.
* Handle nulls in Scala UDFs.
* Optimize CTE query generation with parameter protection.
* Avoid casting arguments of `DATEDIFF`.
* Fix appending partitioned files and reading of null partitions.
* Make a 10X performance improvement for conversion between base 10 and 16 using SQL.

#### New features

* Overwrite only modified partitions for parquet files.

#### Other updates

* Updated logic to detect if Snowpark Connect for Spark is running on XP.
* Support writing to a table with variant data type in Snowflake.
* Remove unnecessary info logs.
* Move Java tests out of Scala tests job to a separate job.
* Update the dependency version for gcsfs.

### Snowpark Submit

None.

## 1.9.0 (January 14, 2026)

### Snowpark Connect for Spark

#### Bug fixes

* Fix serializing Scala tuples.
* Fix loading huge JSON files.
* Implement small fixes for customer issues.
* Implement fixes for struct comparisons.
* Add handling for 0-column DataFrames.
* Correct upload file path.
* Fix `Upload_files_if_needed` not running in parallel.
* Improve input type inference when UDF input types are not defined in the proto.
* Fix NA edge cases.

#### New features

* Support reading single JSON BZ2 file.
* Support Scala UDFs in server-side Snowpark Connect for Spark.
* Implement cast between string and `daytime`.
* Add support for Scala UDFs in `group_map`.

### Snowpark Submit

#### Bug fixes

* Reduce generated workload names.

## 1.8.0 (January 07, 2026)

### Snowpark Connect for Spark

#### Bug fixes

* Fixed JAVA_HOME handling for Windows.

#### New features

* Support `neo4j` data source via JDBC.

### Snowpark Submit

None.
