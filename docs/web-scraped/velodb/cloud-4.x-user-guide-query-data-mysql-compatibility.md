# Source: https://docs.velodb.io/cloud/4.x/user-guide/query-data/mysql-compatibility

Version: 4.x

On this page

# MySQL Compatibility

Doris is highly compatible with MySQL syntax and supports standard SQL.
However, there are several differences between Doris and MySQL, as outlined
below.

## Data Types​

### Numeric Types​

Type| MySQL| Doris| Boolean| \- Supported \- Range: 0 represents false, 1 represents true| \- Supported \- Keyword: Boolean \- Range: 0 represents false, 1 represents true| Bit| \- Supported \- Range: 1 to 64| Not supported| Tinyint| \- Supported \- Supports signed and unsigned \- Range: signed range from -128 to 127, unsigned range from 0 to 255 | \- Supported \- Only supports signed \- Range: -128 to 127| Smallint| \- Supported \- Supports signed and unsigned \- Range: signed range from -2^15 to 2^15-1, unsigned range from 0 to 2^16-1| \- Supported \- Only supports signed \- Range: -32768 to 32767| Mediumint| \- Supported \- Supports signed and unsigned \- Range: signed range from -2^23 to 2^23-1, unsigned range from 0 to 2^24-1| \- Not supported| Int| \- Supported \- Supports signed and unsigned \- Range: signed range from -2^31 to 2^31-1, unsigned range from 0 to 2^32-1| \- Supported \- Only supports signed \- Range: -2147483648 to 2147483647| Bigint| \- Supported \- Supports signed and unsigned \- Range: signed range from -2^63 to 2^63-1, unsigned range from 0 to 2^64-1| \- Supported \- Only supports signed \- Range: -2^63 to 2^63-1| Largeint| \- Not supported| \- Supported \- Only supports signed \- Range: -2^127 to 2^127-1| Decimal| \- Supported \- Supports signed and unsigned (deprecated after 8.0.17) \- Default: Decimal(10, 0)| \- Supported \- Only supports signed \- Default: Decimal(9, 0)| Float/Double| -Supported \- Supports signed and unsigned (deprecated after 8.0.17)| \- Supported \- Only supports signed  
---|---|---  
  
### Date Types​

Type| MySQL| Doris| Date| \- Supported \- Range: ['1000-01-01', '9999-12-31']
\- Format: YYYY-MM-DD| \- Supported \- Range: ['0000-01-01', '9999-12-31'] \-
Format: YYYY-MM-DD| DateTime| \- Supported \- DATETIME([P]), where P is an
optional parameter defined precision \- Range: '1000-01-01 00:00:00.000000' to
'9999-12-31 23:59:59.999999' \- Format: YYYY-MM-DD hh:mm.fraction| \-
Supported \- DATETIME([P]), where P is an optional parameter defined precision
\- Range: ['0000-01-01 00:00:00[.000000]', '9999-12-31 23:59:59[.999999]'] \-
Format: YYYY-MM-DD hh:mm.fraction| Timestamp| \- Supported \- Timestamp[(p)],
where P is an optional parameter defined precision \- Range: ['1970-01-01
00:00:01.000000' UTC, '2038-01-19 03:14:07.999999' UTC] \- Format: YYYY-MM-DD
hh:mm.fraction| \- Not supported| Time| \- Supported \- Time[(p)] \- Range:
['-838:59:59.000000' to '838:59:59.000000'] \- Format: hh:mm.fraction| \- Not
supported| Year| \- Supported \- Range: 1901 to 2155, or 0000 \- Format: yyyy|
\- Not supported  
---|---|---  
  
### String Types​

Type| MySQL| Doris| Char| -Supported - CHAR[(M)], where M is the character
length. If omitted, default length is 1 \- Fixed-length \- Range: [0, 255]
bytes| \- Supported \- CHAR[(M)], where M is the byte length \- Variable-
length \- Range: [1, 255]| Varchar| \- Supported \- VARCHAR(M), where M is the
character length \- Range: [0, 65535] bytes| \- Supported \- VARCHAR(M), where
M is the byte length \- Range: [1, 65533]| String| \- Not supported| \-
Supported \- 1,048,576 bytes (1MB), can be increased to 2,147,483,643 bytes
(2GB)| Binary| \- Supported \- Similar to Char| \- Not supported| Varbinary|
\- Supported \- Similar to Varchar| \- Not supported| Blob| \- Supported \-
TinyBlob, Blob, MediumBlob, LongBlob| \- Not supported| Text| \- Supported \-
TinyText, Text, MediumText, LongText| \- Not supported| Enum| \- Supported \-
Supports up to 65,535 elements| \- Not supported| Set| \- Supported \-
Supports up to 64 elements| \- Not supported  
---|---|---  
  
### JSON Type​

Type| MySQL| Doris| JSON| Supported| Supported  
---|---|---  
  
### Doris unique data type​

Doris has several unique data types. Here are the details:

  * **HyperLogLog**

HLL (HyperLogLog) is a data type that cannot be used as a key column. In an
aggregate model table, the corresponding aggregation type for HLL is
HLL_UNION. The length and default value do not need to be specified. The
length is controlled internally based on the data aggregation level. HLL
columns can only be queried or used with `HLL_UNION_AGG`, `HLL_RAW_AGG`,
`HLL_CARDINALITY`, `HLL_HASH`, and other related functions.

HLL is used for approximate fuzzy deduplication and performs better than count
distinct when dealing with large amounts of data. The typical error rate of
HLL is around 1%, sometimes reaching up to 2%.

  * **Bitmap**

Bitmap is a data type that cannot be used as a key column. In aggregate model
table, the corresponding aggregation type for BITMAP is BITMAP_UNION. Similar
to HLL, the length and default values do not need to be specified, and the
length is controlled internally based on the data aggregation level. Bitmap
columns can only be queried or used with functions like `BITMAP_UNION_COUNT`,
`BITMAP_UNION`, `BITMAP_HASH`, `BITMAP_HASH64` and others.

Using BITMAP in traditional scenarios may impact loading speed, but it
generally performs better than Count Distinct when dealing with large amounts
of data. Please note that in real-time scenarios, using BITMAP without a
global dictionary and with bitmap_hash() function may introduce an error of
around 0.1%. If this error is not acceptable, you can use bitmap_hash64
instead.

  * **QUANTILE_PERCENT**

QUANTILE_STATE is a data type that cannot be used as a key column. In an
aggregate model table, the corresponding aggregation type for QUANTILE_STATE
is QUANTILE_UNION. The length and default value do not need to be specified,
and the length is controlled internally based on the data aggregation level.
QUANTILE_STATE columns can only be queried or used with functions like
`QUANTILE_PERCENT`, `QUANTILE_UNION`, `TO_QUANTILE_STATE` and others.

QUANTILE_STATE is used for calculating approximate quantile values. During
import, it performs pre-aggregation on the same key with different values.
When the number of values does not exceed 2048, it stores all the data in
detail. When the number of values exceeds 2048, it uses the TDigest algorithm
to aggregate (cluster) the data and save the centroids of the clusters.

  * **Array <T>**

Array is a data type in Doris that represents an array composed of elements of
type T. It cannot be used as a key column.

  * **MAP <K, V>**

MAP is a data type in Doris that represents a map composed of elements of
types K and V.

  * **STRUCT <field_name:field_type,...>**

A structure (STRUCT) is composed of multiple fields. It can also be identified
as a collection of multiple columns.

    * field_name: The identifier of the field, which must be unique.
    * field_type: The type of field.
  * **Agg_State**

AGG_STATE is a data type in Doris that cannot be used as a key column. During
table creation, the signature of the aggregation function needs to be
declared.

The length and default value do not need to be specified, and the actual
storage size depends on the implementation of the function.

AGG_STATE can only be used in combination with [STATE](/cloud/4.x/sql-
manual/sql-functions/combinators/state) / [MERGE](/cloud/4.x/sql-manual/sql-
functions/combinators/merge)/ [UNION](/cloud/4.x/sql-manual/sql-
functions/combinators/union) functions from the SQL manual for aggregators.

## Syntax​

### DDL​

#### 01 Create Table Syntax in Doris​

    
    
    CREATE TABLE [IF NOT EXISTS] [database.]table  
    (  
        column_definition_list  
        [, index_definition_list]  
    )  
    [engine_type]  
    [keys_type]  
    [table_comment]  
    [partition_info]  
    distribution_desc  
    [rollup_list]  
    [properties]  
    [extra_properties]  
    

#### 02 Differences with MySQL​

Parameter| Differences from MySQL| Column_definition_list| \- Field list
definition: The basic syntax is similar to MySQL but includes an additional
operation for aggregate types.  
\- The aggregate type operation primarily supports Aggregate.  
\- When creating a table, MySQL allows adding constraints like Index (e.g.,
Primary Key, Unique Key) after the field list definition, while Doris supports
these constraints and computations by defining data models.|
Index_definition_list| \- Index list definition: The basic syntax is similar
to MySQL, supporting bitmap indexes, inverted indexes, and N-Gram indexes, but
Bloom filter indexes are set through properties.  
\- MySQL supports B+Tree and Hash indexes.| Engine_type| \- Table engine type:
Optional.  
\- The currently supported table engine is mainly the OLAP native engine.  
\- MySQL supports storage engines such as Innodb, MyISAM, etc.| Keys_type| \-
Data model: Optional.  
\- Supported types include: 1) DUPLICATE KEY (default): The specified columns
are sort columns. 2) AGGREGATE KEY: The specified columns are dimension
columns. 3) UNIQUE KEY: The specified columns are primary key columns.  
\- MySQL does not have the concept of a data model.| Table_comment| Table
comment| Partition_info| \- Partitioning algorithm: Optional. Doris supported
partitioning algorithms include:  
\- LESS THAN: Only defines the upper bound of partitions. The lower bound is
determined by the upper bound of the previous partition.  
\- FIXED RANGE: Defines left-closed and right-open intervals for partitions.  
\- MULTI RANGE: Creates multiple RANGE partitions in bulk, defining left-
closed and right-open intervals, setting time units and steps. Time units
support years, months, days, weeks, and hours.  
MySQL supports algorithms such as Hash, Range, List, Key. MySQL also supports
subpartitions, with only Hash and Key supported for subpartitions.|
Distribution_desc| \- Bucketing algorithm: Required. Includes: 1) Hash
bucketing syntax: DISTRIBUTED BY HASH (k1[,k2 ...]) [BUCKETS num|auto].
Description: Uses specified key columns for hash bucketing. 2) Random
bucketing syntax: DISTRIBUTED BY RANDOM [BUCKETS num|auto]. Description: Uses
random numbers for bucketing.  
\- MySQL does not have a bucketing algorithm.| Rollup_list| \- Multiple sync
materialized views can be created while creating the table.  
\- Syntax: `rollup_name (col1[, col2, ...]) [DUPLICATE KEY(col1[, col2,
...])][PROPERTIES("key" = "value")]`  
\- MySQL does not support this.| Properties| Table properties: They differ
from MySQL's table properties, and the syntax for defining table properties
also differs from MySQL.  
---|---  
  
#### 03 CREATE INDEX​

    
    
    CREATE INDEX [IF NOT EXISTS] index_name ON table_name (column [, ...],) [USING BITMAP];  
    

  * Doris currently supports Bitmap index, Inverted index, and N-Gram index. BloomFilter index are supported as well, but they have a separate syntax for setting them.

  * MySQL supports index algorithms such as B+Tree and Hash.

#### 04 CREATE VIEW​

    
    
    CREATE VIEW [IF NOT EXISTS]  
     [db_name.]view_name  
     (column1[ COMMENT "col comment"][, column2, ...])  
    AS query_stmt  
      
    CREATE MATERIALIZED VIEW (IF NOT EXISTS)? mvName=multipartIdentifier  
            (LEFT_PAREN cols=simpleColumnDefs RIGHT_PAREN)? buildMode?  
            (REFRESH refreshMethod? refreshTrigger?)?  
            (KEY keys=identifierList)?  
            (COMMENT STRING_LITERAL)?  
            (PARTITION BY LEFT_PAREN partitionKey = identifier RIGHT_PAREN)?  
            (DISTRIBUTED BY (HASH hashKeys=identifierList | RANDOM) (BUCKETS (INTEGER_VALUE | AUTO))?)?  
            propertyClause?  
            AS query  
    

  * The basic syntax is consistent with MySQL.
  * Doris supports logical view and supports two types of materialized views: synchronous materialized views and asynchronous materialized views
  * MySQL do not supports asynchronous materialized views.

#### 05 ALTER TABLE / ALTER INDEX​

The syntax of Doris ALTER is basically the same as that of MySQL.

### DROP TABLE / DROP INDEX​

The syntax of Doris DROP is basically the same as MySQL.

### DML​

#### INSERT​

    
    
    INSERT INTO table_name  
        [ PARTITION (p1, ...) ]  
        [ WITH LABEL label]  
        [ (column [, ...]) ]  
        [ [ hint [, ...] ] ]  
        { VALUES ( { expression | DEFAULT } [, ...] ) [, ...] | query }  
    

The Doris INSERT syntax is basically the same as MySQL.

#### UPDATE​

    
    
    UPDATE target_table [table_alias]  
        SET assignment_list  
        WHERE condition  
      
    assignment_list:  
        assignment [, assignment] ...  
      
    assignment:  
        col_name = value  
      
    value:  
        {expr | DEFAULT}  
    

The Doris UPDATE syntax is basically the same as MySQL, but it should be noted
that the **`WHERE` condition must be added.**

#### Delete​

    
    
    DELETE FROM table_name [table_alias]   
        [PARTITION partition_name | PARTITIONS (partition_name [, partition_name])]  
        WHERE column_name op { value | value_list } [ AND column_name op { value | value_list } ...];  
    

The syntax can only specify filter predicates

    
    
    DELETE FROM table_name [table_alias]  
        [PARTITION partition_name | PARTITIONS (partition_name [, partition_name])]  
        [USING additional_tables]  
        WHERE condition  
    

This syntax can only be used on the UNIQUE KEY model table.

The DELETE syntax in Doris is basically the same as in MySQL. However, since
Doris is an analytical database, deletions cannot be too frequent.

#### SELECT​

    
    
    SELECT  
        [hint_statement, ...]  
        [ALL | DISTINCT]  
        select_expr [, select_expr ...]  
        [EXCEPT ( col_name1 [, col_name2, col_name3, ...] )]  
        [FROM table_references  
          [PARTITION partition_list]  
          [TABLET tabletid_list]  
          [TABLESAMPLE sample_value [ROWS | PERCENT]  
            [REPEATABLE pos_seek]]  
        [WHERE where_condition]  
        [GROUP BY [GROUPING SETS | ROLLUP | CUBE] {col_name | expr | position}]  
        [HAVING where_condition]  
        [ORDER BY {col_name | expr | position} [ASC | DESC], ...]  
        [LIMIT {[offset_count,] row_count | row_count OFFSET offset_count}]  
        [INTO OUTFILE 'file_name']  
    

The Doris SELECT syntax is basically the same as MySQL.

## SQL Function​

Doris Function covers most MySQL functions.

On This Page

  * Data Types
    * Numeric Types
    * Date Types
    * String Types
    * JSON Type
    * Doris unique data type
  * Syntax
    * DDL
    * DROP TABLE / DROP INDEX
    * DML
  * SQL Function

