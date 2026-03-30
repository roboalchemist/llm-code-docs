# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-connect-supported-apis.md

# PySpark APIs supported for Snowpark Connect for Spark

Snowpark Connect for Spark supports PySpark APIs as described in this topic.

Snowpark Connect for Spark provides compatibility with PySpark’s 3.5.3 Spark Connect API, allowing you to run Spark workloads on Snowflake.
Snowpark Connect for Spark compatibility is defined by its execution behavior when running a Spark application that uses the Pyspark 3.5.3
Spark Connect API. This guide details which APIs are supported and their compatibility levels.

## Compatibility level definitions

Full compatibility APIs
:   APIs with full compatibility behave identically to native PySpark. You can use these APIs with confidence that results will match exactly.

High compatibility APIs
:   APIs with high compatibility work correctly but might have minor differences:

    * Error message formatting might differ.
    * Output display format might vary (such as decimal precision, column name casing).
    * Edge cases might produce slightly different results.

Partial compatibility APIs
:   APIs with partial compatibility are functional but have notable limitations:

    * Only a subset of functionality might be available.
    * Behavior might differ from PySpark in specific scenarios.
    * Additional configuration might be required.
    * Performance characteristics might differ.

Unsupported APIs
:   APIs that are not currently implemented or cannot be supported on Snowflake.

## DataFrame APIs

The core DataFrame API coverage.

### Full compatibility APIs

* `cache`
* `coalesce`
* `collect`
* `count`
* `crossJoin`
* `dropDuplicates`
* `drop_duplicates`
* `dropna`
* `fillna`
* `first`
* `head`
* `isEmpty`
* `join`
* `limit`
* `melt`
* `offset`
* `persist`
* `repartitionByRange`
* `replace`
* `select`
* `show`
* `tail`
* `take`
* `toDF`
* `toLocalIterator`
* `toPandas`
* `unionAll`
* `unpersist`
* `unpivot`
* `where`
* `withColumnsRenamed`
* `toLocalIterator`
* `toPandas`
* `unionAll`
* `unpersist`
* `unpivot`
* `where`
* `withColumnsRenamed`

### High compatibility APIs

* `agg`
* `colRegex`
* `corr`
* `cov`
* `crosstab`
* `cube`
* `describe`
* `distinct`
* `drop`
* `exceptAll`
* `groupBy`
* `groupby`
* `intersect`
* `intersectAll`
* `isLocal`
* `mapInPandas`
* `orderBy`
* `rollup`
* `sort`
* `union`
* `unionByName`
* `withColumn`

#### Notes

* `orderBy` / `sort`: Column ordering inferred from the last DataFrame in the chain.
* `union` / `unionByName`: Type widening behavior might differ slightly.
* `describe`: Statistical output format might vary.

### Partial compatibility APIs

* `alias`
* `approxQuantile`
* `createGlobalTempView`
* `createOrReplaceGlobalTempView`
* `createOrReplaceTempView`
* `createTempView`
* `explain`
* `filter`
* `freqItems`
* `hint`
* `inputFiles`
* `printSchema`
* `randomSplit`
* `repartition`
* `sameSemantics`
* `sample`
* `sampleBy`
* `selectExpr`
* `semanticHash`
* `sortWithinPartitions`
* `subtract`
* `summary`
* `transform`
* `withColumns`
* `withMetadata`

### Notes

* `explain`: Query plan format differs from Spark.
* `repartition`: Partition count might not be exact.
* `sample`: Random sampling implementation differs.
* `createTempView`: View lifecycle might differ.

### Unsupported APIs

* `checkSameSparkSession`
* `dropDuplicatesWithinWatermark`
* `observe`
* `pandas_api`
* `registerTempTable`
* `to_pandas_on_spark`
* `withWatermark`

## Column APIs

Coverage for column operations.

### Full compatibility APIs

* `asc`
* `between`
* `contains`
* `desc`
* `eqNullSafe`
* `getItem`
* `isNull`
* `isin`
* `like`
* `otherwise`
* `startswith`
* `substr`
* `when`

### High compatibility APIs

* `alias`
* `asc_nulls_first`
* `asc_nulls_last`
* `astype`
* `bitwiseAND`
* `bitwiseOR`
* `bitwiseXOR`
* `cast`
* `desc_nulls_first`
* `desc_nulls_last`
* `endswith`
* `isNotNull`

#### Notes

* `cast`: Some invalid casts return NULL in Spark but error in Snowpark.
* `alias`: Struct field display format might differ.

### Partial compatibility APIs

* `dropFields`
* `ilike`
* `over`
* `rlike`
* `withField`

#### Notes

* `over`: Window frame specifications might have subtle differences.
* `rlike`: Regex syntax follows Snowflake conventions.

## SparkSession APIs

### Full compatibility APIs

* `range`
* `sql`
* `table`

### High compatibility APIs

* `createDataFrame`

#### Notes

Schema inference might produce different types (such as `NUMBER(38,0)` vs `LONG`).

### Partial compatibility APIs

* `addArtifact`
* `addArtifacts`
* `addTag`
* `clearTags`
* `getTags`
* `interruptAll`
* `interruptOperation`
* `interruptTag`
* `removeTag`

#### Notes

* Tags are mapped to Snowflake query tags.
* Interrupt operations use Snowflake query IDs instead of operation IDs.

### Unsupported APIs

* `copyFromLocalToFs`
* `stop`

## GroupedData APIs

### Full compatibility APIs

* `agg`
* `mean`
* `pivot`

### High compatibility APIs

* `agg`
* `mean`
* `pivot`

### Partial compatibility APIs

* `apply`
* `avg`
* `sum`

### Unsupported APIs

* `applyInPandasWithState`
* `cogroup`

## DataFrameReader APIs

### Full compatibility APIs

* `table`

### High compatibility APIs

* `csv`

### Partial compatibility APIs

* `json`
* `load`
* `parquet`
* `jdbc`

#### Notes

* File paths use Snowflake stages or cloud storage (S3, GCS, Azure).
* Schema inference might differ from native Spark.
* Some format-specific options might not be supported.

### Unsupported APIs

* `orc`

## DataFrameWriter APIs

### Full compatibility APIs

* `mode`
* `saveAsTable`
* `text`

### Partial compatibility APIs

* `csv`
* `json`
* `options`
* `parquet`

#### Notes

* Writes go to Snowflake stages or cloud storage.
* Partitioning behavior might differ.

### Unsupported APIs

* `bucketBy`
* `insertInto`
* `jdbc`
* `orc`
* `sortBy`

## DataFrameWriterV2 APIs

Coverage for the newer DataFrameWriterV2 API.

### Full compatibility APIs

* `replace`

### Partial compatibility APIs

* `append`
* `create`
* `createOrReplace`
* `option`
* `options`
* `partitionedBy`
* `tableProperty`
* `using`

## Catalog APIs

### Full compatibility APIs

* `cacheTable`
* `clearCache`
* `dropGlobalTempView`
* `dropTempView`
* `isCached`
* `refreshByPath`
* `refreshTable`
* `uncacheTable`

### High compatibility APIs

* `currentCatalog`
* `listCatalogs`
* `listColumns`
* `recoverPartitions`
* `setCurrentCatalog`

#### Notes

* `listColumns`: Column names are uppercase, types are Snowflake-specific.
* Error messages might differ in format.

### Unsupported APIs

* `createExternalTable`
* `createTable`
* `functionExists`
* `getFunction`
* `listFunctions`
* `registerFunction`

## Window & WindowSpec APIs

Coverage for window functions.

### Window (all D0) APIs

* `partitionBy`
* `orderBy`
* `rangeBetween`
* `rowsBetween`
* `unboundedPreceding`
* `unboundedFollowing`
* `currentRow`

### WindowSpec(all D0) APIs

* `partitionBy`
* `orderBy`
* `rangeBetween`
* `rowsBetween`
