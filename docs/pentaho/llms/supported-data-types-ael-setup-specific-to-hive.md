# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/vendor-supplied-clients/hive-ael-setup-specific-to-hive/supported-data-types-ael-setup-specific-to-hive.md

# Supported data types

Pre-existing Hive tables that use the Varchar data type are converted to strings when you select the **Truncate Table** option in the Table Output step. Pentaho limits support for binary types and does not recommend using Hive binary types with AEL. See the.**Pentaho Data Integration** document for details on using the Table Output step.

The following table lists the supported Hive data types:

| Spark data type | Hive data type        | Pentaho support                        | Pentaho data type |
| --------------- | --------------------- | -------------------------------------- | ----------------- |
| ByteType        | TinyInt               | Supported                              | Integer           |
| ShortType       | SmallInt              | Supported                              | Integer           |
| IntegerType     | Integer               | Supported                              | Integer           |
| LongType        | BigInt                | Supported                              | BigNumber         |
| FloatType       | Float                 | Supported                              | Number            |
| DoubleType      | Double                | Supported                              | Number            |
| DecimalType     | Decimal               | Supported                              | BigNumber         |
| StringType      | String, Char, Varchar | Supported, except Varchar with length  | String            |
| BinaryType      | Binary                | Not supported                          | N/A               |
| BooleanType     | Boolean               | Supported                              | Boolean           |
| TimestampType   | Timestamp             | Not supported, yet converted to String | String            |
| DataType        | Date                  | Supported                              | Date              |
| ArrayType       | Array                 | Not Supported                          | N/A               |
| StructType      | Struct                | Not Supported                          | N/A               |
