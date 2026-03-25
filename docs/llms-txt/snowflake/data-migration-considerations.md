# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/teradata/data-migration-considerations.md

# SnowConvert AI - Teradata - Data Migration Considerations

This section describe important consideration when migration data from Teradata to Snowflake.

> **Note:**
>
> Consider that this is a work in progress.

When migrating data from Teradata to Snowflake, it is crucial to consider the functional differences between the databases. This page showcases the best suggestions for migrating data.

Review the following information:

## UNION ALL Data Migration

Data migration considerations for UNION ALL.

UNION ALL is a SQL operator that allows the combination of multiple resultsets. The syntax is the following:

```sql
 query_expression_1 UNION [ ALL ] query_expression_2
```

For more information, please review the following [Teradata](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Data-Manipulation-Language/Set-Operators/UNION-Operator/UNION-Operator-Syntax) documentation.

### Column Size differences

Even though the operator is translated into the same operator in Snowflake, there could be detailed differences in functional equivalence. For example, the union of different columns which have different column sizes. Teradata does truncate the values when the first SELECT statement contains less space in the columns.

#### Teradata behavior

> **Note:**
>
> **Same behavior in ANSI and TERA session modes.**

For this example, the following input will show the Teradata behavior.

##### Teradata setup data

```sql
 CREATE TABLE table1
(
col1 VARCHAR(20)
);

INSERT INTO table1 VALUES('value 1 abcdefghijk');
INSERT INTO table1 VALUES('value 2 abcdefghijk');

CREATE TABLE table2
(
col1 VARCHAR(10)
);

INSERT INTO table2 VALUES('t2 row 1 a');
INSERT INTO table2 VALUES('t2 row 2 a');
INSERT INTO table2 VALUES('t2 row 3 a');
```

##### Snowflake setup data

```sql
 CREATE OR REPLACE TABLE table1
(
col1 VARCHAR(20)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/14/2024" }}'
;

INSERT INTO table1
VALUES ('value 1 abcdefghijk');

INSERT INTO table1
VALUES ('value 2 abcdefghijk');

CREATE OR REPLACE TABLE table2
(
col1 VARCHAR(10)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/14/2024" }}'
;

INSERT INTO table2
VALUES ('t2 row 1 a');

INSERT INTO table2
VALUES ('t2 row 2 a');

INSERT INTO table2
VALUES ('t2 row 3 a');
```

#### **Case 1 - one single column: UNION ALL for a column VARCHAR(20) over a column VARCHAR(10)**

> **SuccessPlaceholder:**
>
> For this case, the functional equivalence is the same

##### Teradata input

```sql
 SELECT col1 FROM table1
UNION ALL
SELECT col1 FROM table2;
```

##### Teradata output

```none
value 1 abcdefghijk
t2 row 3 a
value 2 abcdefghijk
t2 row 1 a
t2 row 2 a
```

##### Snowflake input

```sql
 SELECT
col1 FROM
table1
UNION ALL
SELECT
col1 FROM
table2;
```

##### Snowflake output

```none
value 1 abcdefghijk
t2 row 3 a
value 2 abcdefghijk
t2 row 1 a
t2 row 2 a
```

#### **Case 2 - one single column: UNION ALL for a column VARCHAR(10) over a column VARCHAR(20)**

> **Danger:**
>
> In this case, the functional equivalence is not the same.

The following case does not show functional equivalence in Snowflake. The column values should be truncated as in the Teradata sample.

##### Teradata input

```sql
 SELECT col1 FROM table2
UNION ALL
SELECT col1 FROM table1;
```

##### Teradata output

```none
t2 row 3 a
value 1 ab --> truncated
t2 row 1 a
t2 row 2 a
value 2 ab --> truncated
```

##### Snowflake input

```sql
 SELECT
col1 FROM
table2
UNION ALL
SELECT
col1 FROM
table1;
```

##### Snowflake output

```none
t2 row 3 a
value 1 abcdefghijk --> NOT truncated
t2 row 1 a
t2 row 2 a
value 2 abcdefghijk --> NOT truncated
```

**Workaround to get the same functionality**

In this case, the size of the column of the `table2` is 10 and the `table1` is 20. So, the size of the first column in the query should be the element to complete the `LEFT()` function used here. For more information, see the [Snowflake LEFT function documentation](https://docs.snowflake.com/en/sql-reference/functions/left).

##### Snowflake input

```sql
 SELECT col1 FROM table2 -- size (10)
UNION ALL
SELECT LEFT(col1, 10) AS col1 FROM table1;
```

##### Snowflake output

```none
t2 row 1 a
t2 row 2 a
t2 row 3 a
value 1 ab
value 2 ab
```

#### **Case 3 - multiple columns - same size by table: UNION ALL for columns VARCHAR(20) over columns VARCHAR(10)**

For this case, it is required to set up new data as follows:

##### Teradata setup data

```sql
 CREATE TABLE table3
(
col1 VARCHAR(20),
col2 VARCHAR(20)
);

INSERT INTO table3 VALUES('value 1 abcdefghijk', 'value 1 abcdefghijk');
INSERT INTO table3 VALUES('value 2 abcdefghijk', 'value 2 abcdefghijk');

CREATE TABLE table4
(
col1 VARCHAR(10),
col2 VARCHAR(10)
);

INSERT INTO table4 VALUES('t2 row 1 a', 't2 row 1 b');
INSERT INTO table4 VALUES('t2 row 2 a', 't2 row 2 b');
INSERT INTO table4 VALUES('t2 row 3 a', 't2 row 3 b');
```

##### Snowflake setup data

```sql
 CREATE OR REPLACE TABLE table3
(
col1 VARCHAR(20),
col2 VARCHAR(20)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/14/2024" }}'
;

INSERT INTO table3
VALUES ('value 1 abcdefghijk', 'value 1 abcdefghijk');

INSERT INTO table3
VALUES ('value 2 abcdefghijk', 'value 2 abcdefghijk');

CREATE OR REPLACE TABLE table4
(
col1 VARCHAR(10),
col2 VARCHAR(10)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/14/2024" }}'
;

INSERT INTO table4
VALUES ('t2 row 1 a', 't2 row 1 b');

INSERT INTO table4
VALUES ('t2 row 2 a', 't2 row 2 b');

INSERT INTO table4
VALUES ('t2 row 3 a', 't2 row 3 b');
```

Once the new tables and data are created, the following query can be evaluated.

> **Note:**
>
> For this case, the functional equivalence is the same

##### Teradata input

```sql
 select col1, col2 from table3
union all
select col1, col2 from table4;
```

##### Teradata output

| col1 | col2 |
| --- | --- |
| value 1 abcdefghijk | value 1 abcdefghijk |
| t2 row 3 a | t2 row 3 b |
| value 2 abcdefghijk | value 2 abcdefghijk |
| t2 row 1 a | t2 row 1 b |
| t2 row 2 a | t2 row 2 b |

##### Snowflake input

```sql
 SELECT
col1, col2 FROM
table3
UNION ALL
SELECT
col1, col2 FROM
table4;
```

##### Snowflake output

| col1 | col2 |
| --- | --- |
| value 1 abcdefghijk | value 1 abcdefghijk |
| value 2 abcdefghijk | value 2 abcdefghijk |
| t2 row 1 a | t2 row 1 b |
| t2 row 2 a | t2 row 2 b |
| t2 row 3 a | t2 row 3 b |

#### Case 4 - multiple columns - same size by table: UNION ALL for columns VARCHAR(10) over columns VARCHAR(20)

> **Warning:**
>
> In this case, the functional equivalence is not the same.

##### Teradata input

```sql
 select col1, col2 from table4
union all
select col1, col2 from table3;
```

##### Teradata output

| col1 | col2 |
| --- | --- |
| t2 row 3 a | t2 row 3 b |
| value 1 ab | value 1 ab |
| t2 row 1 a | t2 row 1 b |
| t2 row 2 a | t2 row 2 b |
| value 2 ab | value 2 ab |

##### Snowflake input

```sql
 SELECT
col1, col2 FROM
table4
UNION ALL
SELECT
col1, col2 FROM
table3;
```

##### Snowflake output

| col1 | col2 |
| --- | --- |
| t2 row 1 a | t2 row 1 b |
| t2 row 2 a | t2 row 2 b |
| t2 row 3 a | t2 row 3 b |
| value 1 abcdefghijk | value 1 abcdefghijk |
| value 2 abcdefghijk | value 2 abcdefghijk |

**Workaround to get the same functionality**

Apply the column size to the second `SELECT` on the columns to get the same functionality.

##### Snowflake input

```sql
 SELECT col1, col2 FROM table4 -- size (10)
UNION ALL
SELECT LEFT(col1, 10) AS col1, LEFT(col2, 10) AS col2 FROM table3;
```

##### Snowflake output

| col1 | col2 |
| --- | --- |
| t2 row 1 a | t2 row 1 b |
| t2 row 2 a | t2 row 2 b |
| t2 row 3 a | t2 row 3 b |
| value 1 ab | value 1 ab |
| value 2 ab | value 2 ab |

#### Case 5 - multiple columns - different sizes by table: UNION ALL for columns VARCHAR(10) over columns VARCHAR(20)

For this case, it is required to set up new data as follows:

##### Teradata setup data

```sql
 CREATE TABLE table5
(
col1 VARCHAR(20),
col2 VARCHAR(12)
);

INSERT INTO table5 VALUES('value 1 abcdefghijk', 'value 1 abcdefghijk');
INSERT INTO table5 VALUES('value 2 abcdefghijk', 'value 2 abcdefghijk');

CREATE TABLE table6
(
col1 VARCHAR(10),
col2 VARCHAR(5)
);

INSERT INTO table6 VALUES('t2 row 1 a', 't2 row 1 b');
INSERT INTO table6 VALUES('t2 row 2 a', 't2 row 2 b');
INSERT INTO table6 VALUES('t2 row 3 a', 't2 row 3 b');
```

##### Snowflake setup data

```sql
 CREATE OR REPLACE TABLE table5
(
col1 VARCHAR(20),
col2 VARCHAR(12)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/14/2024" }}'
;

INSERT INTO table5
VALUES ('value 1 abcdefghijk', 'value 1 abcd');

INSERT INTO table5
VALUES ('value 2 abcdefghijk', 'value 2 abcd');

CREATE OR REPLACE TABLE table6
(
col1 VARCHAR(10),
col2 VARCHAR(5)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/14/2024" }}'
;

INSERT INTO table6
VALUES ('t2 row 1 a', 't2 1b');

INSERT INTO table6
VALUES ('t2 row 2 a', 't2 2b');

INSERT INTO table6
VALUES ('t2 row 3 a', 't2 3b');
```

Once the new tables and data are created, the following query can be evaluated.

> **Note:**
>
> For this case, the functional equivalence is the same

##### Teradata input

```sql
 select col1, col2 from table5
union all
select col1, col2 from table6;
```

##### Teradata output

| col1 | col2 |
| --- | --- |
| value 1 abcdefghijk | value 1 abcd |
| t2 row 3 a | t2 3b |
| value 2 abcdefghijk | value 2 abcd |
| t2 row 1 a | t2 1b |
| t2 row 2 a | t2 2b |

##### Snowflake input

```sql
 SELECT
col1, col2 FROM
table5
UNION ALL
SELECT
col1, col2 FROM
table6;
```

##### Snowflake output

| col1 | col2 |
| --- | --- |
| value 1 abcdefghijk | value 1 abcd |
| value 2 abcdefghijk | value 2 abcd |
| t2 row 1 a | t2 1b |
| t2 row 2 a | t2 2b |
| t2 row 3 a | t2 3b |

#### Case 6 - multiple columns - different sizes by table: UNION ALL for columns VARCHAR(20), VARCHAR(10) over columns VARCHAR(10), VARCHAR(5)

> **Warning:**
>
> In this case, the functional equivalence is not the same.

##### Teradata input

```sql
 select col1, col2 from table6
union all
select col1, col2 from table5;
```

##### Teradata output

| col1 | col2 |
| --- | --- |
| t2 row 3 a | t2 3b |
| **value 1 ab** | **value** |
| t2 row 1 a | t2 1b |
| t2 row 2 a | t2 2b |
| **value 2 ab** | **value** |

##### Snowflake input

```sql
 SELECT
col1, col2 FROM
table6
UNION ALL
SELECT
col1, col2 FROM
table5;
```

##### Snowflake output

| col1 | col2 |
| --- | --- |
| t2 row 1 a | t2 1b |
| t2 row 2 a | t2 2b |
| t2 row 3 a | t2 3b |
| **value 1 abcdefghijk** | **value 1 abcd** |
| **value 2 abcdefghijk** | **value 2 abcd** |

**Workaround to get the same functionality**

The column with the smallest size from the first `SELECT` is used to determine the size of the columns from the second `SELECT`.

##### Snowflake input

```sql
 SELECT
col1, col2 FROM
table6
UNION ALL
SELECT
LEFT(col1, 5) as col1, LEFT(col2, 5) AS col2 FROM
table5;
```

##### Snowflake output

| col1 | col2 |
| --- | --- |
| t2 row 3 a | t2 3b |
| **value 1 ab** | **value** |
| t2 row 1 a | t2 1b |
| t2 row 2 a | t2 2b |
| **value 2 ab** | **value** |

#### Case 7 - multiple columns *expression* - different sizes by table: UNION ALL for columns VARCHAR(20), VARCHAR(20) over columns VARCHAR(10), VARCHAR(10)

Use the data set up in Case 3 — Multiple columns — Same size by table. Once the new tables and data are created, the following query can be evaluated.

> **Note:**
>
> For this case, the functional equivalence is the same

##### Teradata input

```sql
 select col1 || col2 from table3
union all
select col1 || col2 from table4;
```

##### Teradata output

| col1 || col2 |
| --- |
| value 1 abcdefghijkvalue 1 abcdefghijk |
| t2 row 3 at2 row 3 b |
| value 2 abcdefghijkvalue 2 abcdefghijk |
| t2 row 1 at2 row 1 b |
| t2 row 2 at2 row 2 b |

##### Snowflake input

```sql
 SELECT
col1 || col2 FROM
table3
UNION ALL
SELECT
col1 || col2 FROM
table4;
```

##### Snowflake output

| col1 || col2 |
| --- |
| value 1 abcdefghijkvalue 1 abcdefghijk |
| value 2 abcdefghijkvalue 2 abcdefghijk |
| t2 row 1 at2 row 1 b |
| t2 row 2 at2 row 2 b |
| t2 row 3 at2 row 3 b |

#### Case 8 - multiple columns *expression* - different sizes by table: UNION ALL for columns VARCHAR(20), VARCHAR(20) over columns VARCHAR(10), VARCHAR(10)

> **Warning:**
>
> This case has functional differences.

##### Teradata input

```sql
 select col1 || col2 from table4
union all
select col1 || col2 from table3;
```

##### Teradata output

| col1 || col2 |
| --- |
| t2 row 1 at2 row 1 b |
| t2 row 2 at2 row 2 b |
| t2 row 3 at2 row 3 b |
| value 1 abcdefghijkv |
| value 2 abcdefghijkv |

##### Snowflake input

```sql
 SELECT
col1 || col2 FROM
table4
UNION ALL
SELECT
col1 || col2 FROM
table3;
```

##### Snowflake output

| col1 || col2 |
| --- |
| t2 row 1 at2 row 1 b |
| t2 row 2 at2 row 2 b |
| t2 row 3 at2 row 3 b |
| value 1 abcdefghijkvalue 1 abcdefghijk |
| value 2 abcdefghijkvalue 2 abcdefghijk |

**Workaround to get the same functionality**

The sum of the column sizes of the smaller column should be used in the `LEFT` function. For example, if the smaller column is VARCHAR(10), then the limit of the `LEFT` function should be 20 (10 + 10).

> **Warning:**
>
> If the first `SELECT` result is smaller, its sum would be used for the truncation of the values.

##### Snowflake input

```sql
 SELECT
col1 || col2 FROM
table4
UNION ALL
SELECT
LEFT(col1 || col2, 20) FROM
table3;
```

##### Snowflake output

| col1 || col2 |
| --- |
| t2 row 1 at2 row 1 b |
| t2 row 2 at2 row 2 b |
| t2 row 3 at2 row 3 b |
| value 1 abcdefghijkv |
| value 2 abcdefghijkv |

#### Other considerations about column size differences

* `CHAR` and `VARCHAR` behave the same.
* Number columns may behave differently. The numbers cannot be truncated, so there is an overflow in the Teradata environment. So, this is not applied to these data types. Review the following example:

```sql
-- Teradata number sample
CREATE TABLE table11
(
col1 NUMBER(2)
);

INSERT INTO table11 VALUES(10);
INSERT INTO table11 VALUES(10);

CREATE TABLE table12
(
col1 NUMBER(1)
);

INSERT INTO table12 VALUES(1);
INSERT INTO table12 VALUES(1);
INSERT INTO table12 VALUES(1);

-- ERROR!  Overflow occurred when computing an expression involving table11.col1
SELECT col1 FROM table12
UNION ALL
SELECT col1 FROM table11;
```
