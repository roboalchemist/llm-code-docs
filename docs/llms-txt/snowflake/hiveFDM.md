# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/functional-difference/hiveFDM.md

# SnowConvert AI - Hive Functional Differences

## SSC-FDM-HV0001

Inserting values into an external table is not supported in Snowflake

### Description

Hive Format tables allow you to insert values, but Snowflake External Tables do not support value insertions. This means that while the table structure will be converted, any operations that attempt to insert data directly into the external table in Snowflake will fail.

### Code Example

#### Input

##### Spark

```sql
 CREATE EXTERNAL TABLE IF NOT EXISTS External_table_hive_format
(
  order_id int,
  date string,
  client_name string,
  total float
)
stored as AVRO
LOCATION 'gs://sc_external_table_bucket/folder_with_avro/orders.avro';
```

#### Output

##### Snowflake

```sql
 --** SSC-FDM-HV0001 - INSERTING VALUES INTO AN EXTERNAL TABLE IS NOT SUPPORTED IN SNOWFLAKE **
CREATE EXTERNAL TABLE IF NOT EXISTS hive_format_orders_Andres
(
  order_id int AS CAST(GET_IGNORE_CASE($1, 'order_id') AS int),
  date string AS CAST(GET_IGNORE_CASE($1, 'date') AS string),
  client_name string AS CAST(GET_IGNORE_CASE($1, 'client_name') AS string),
  total float AS CAST(GET_IGNORE_CASE($1, 'total') AS float)
)
!!!RESOLVE EWI!!! /*** SSC-EWI-0032 - EXTERNAL TABLE REQUIRES AN EXTERNAL STAGE TO ACCESS gs:, DEFINE AND REPLACE THE EXTERNAL_STAGE PLACEHOLDER ***/!!!
LOCATION = @EXTERNAL_STAGE
AUTO_REFRESH = false
FILE_FORMAT = (TYPE = AVRO)
PATTERN = '/sc_external_table_bucket/folder_with_avro/orders.avro'
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "spark",  "convertedOn": "06/18/2025",  "domain": "no-domain-provided" }}';
```

#### Best Practices

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
