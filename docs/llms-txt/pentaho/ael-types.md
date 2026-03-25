# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/parquet-input/select-an-engine-parquet-input/using-parquet-input-on-spark-engine/general-parquet-input-spark/fields-parquet-input-spark-engine/ael-types.md

# Spark types

When used with the Spark engine, the Parquet Input step automatically converts Parquet rows to Spark SQL rows. The following table lists the conversion types:

| Parquet Type         | Spark Type Output |
| -------------------- | ----------------- |
| Boolean              | Boolean           |
| Int8                 | Short             |
| Int16                | Short             |
| Int32                | Integer           |
| Int64                | Long              |
| Int96                | Timestamp         |
| UInt8                | Short             |
| UInt16               | Short             |
| UInt32               | Integer           |
| UInt64               | Long              |
| Binary               | Binary            |
| FixedLengthByteArray | Binary            |
| Float                | Float             |
| Double               | Double            |
| Decimal              | BigNumber         |
| UTF8                 | String            |
| VarChar              | String            |
| TimeMillis           | Timestamp         |
| TimestampMillis      | Timestamp         |
| Date                 | Date              |
