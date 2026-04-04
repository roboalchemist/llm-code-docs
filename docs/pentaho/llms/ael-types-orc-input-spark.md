# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/orc-input/select-an-engine-orc-input-step/using-orc-input-step-on-the-spark-engine/options-orc-input-spark-engine/fields-orc-input-spark-engine/ael-types-orc-input-spark.md

# AEL types

In AEL, the ORC step automatically converts ORC rows to Spark SQL rows. The following table lists the conversion types.

| ORC Type  | Spark SQL Type |
| --------- | -------------- |
| Boolean   | Boolean        |
| TinyInt   | Short          |
| SmallInt  | Short          |
| Integer   | Integer        |
| BigInt    | Long           |
| Binary    | Binary         |
| Float     | Float          |
| Double    | Double         |
| Decimal   | BigNumber      |
| Char      | String         |
| VarChar   | String         |
| Timestamp | Timestamp      |
| Date      | Date           |
