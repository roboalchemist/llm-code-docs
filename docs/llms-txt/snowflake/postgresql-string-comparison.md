# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/postgres/postgresql-string-comparison.md

# SnowConvert AI - PostgreSQL - String Comparison

In PostgreSQL and PostgreSQL-based languages (Greenplum, RedShift, Netezza), when comparing fixed-length data types (CHAR, CHARACTER, etc) or comparing fixed-length data types against varchar data types, trailing spaces are ignored. This means that a string like `'water '` (value with a trailing space) would be considered equal to `'water'` (value without a trailing space).

If you compare

```sql
CHAR(6) 'hello', which is stored as 'hello ', with one padded character
```

against

```sql
CHAR(6) 'hello ', with no need to add any padding character
```

They are effectively the same after trailing spaces.

Meanwhile, Snowflake does not have fixed-length character types and takes a more literal approach for its `VARCHAR` data type, treating strings exactly as they are stored, including any trailing blanks. Therefore, in Snowflake, `'water '` is *not* considered equal to `'water'`.

To prevent trailing spaces from affecting string comparison outcomes in PostgreSQL to Snowflake conversions, SnowConvert AI automatically adds `BTRIM` to relevant comparisons as our team has identified. This ensures consistent behavior.

## Sample Source Patterns

Let’s use the following script data to explain string comparison.

```sql
create table table1(c1 char(2), c2 char(2), c3 VARCHAR(2), c4 VARCHAR(2));

insert into table1 values ('a','a ','a','a ');

insert into table1 values ('b','b','b','b');
```

### NULLIF

#### Varchar Data Type

Input Code:

##### PostgreSQL

```sql
SELECT NULLIF(c3,c4) FROM table1;
```

Output Code:

##### Snowflake

```sql
SELECT
NULLIF(c3,c4) FROM
table1;
```

#### Char Data Types

Input Code:

##### PostgreSQL

```sql
select nullif(c1,c2) AS case2 from table1;
```

Output Code:

##### Snowflake

```sql
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "table1" **
select
nullif(c1,c2) AS case2 from
table1;
```

### GREATEST or LEAST

Input Code:

#### PostgreSQL

```sql
select '"' || greatest(c1, c2) || '"' AS greatest, '"' || least(c1, c2) || '"' AS least from table1;
```

Output Code:

##### Snowflake

```sql
--** SSC-FDM-0007 - MISSING DEPENDENT OBJECT "table1" **
select '"' || GREATEST_IGNORE_NULLS(c1, c2) || '"' AS greatest, '"' || LEAST_IGNORE_NULLS(c1, c2) || '"' AS least from
table1;
```
