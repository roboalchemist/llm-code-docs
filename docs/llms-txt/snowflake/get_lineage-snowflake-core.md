# Source: https://docs.snowflake.com/en/sql-reference/functions/get_lineage-snowflake-core.md

Categories:
:   [Table functions](../functions-table.md)

# GET_LINEAGE (SNOWFLAKE.CORE)

Given a Snowflake object, returns data lineage information upstream or downstream from that object. Upstream means the
path of objects that led to the creation of the object; downstream means the path of objects that were created
from the object.

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.GET_LINEAGE(
    '<object_name>',
    '<object_domain>',
    '<direction>',
    [ <distance>, ]
    [ '<object_version>' ]
)
```

## Arguments

**Required:**

`'object_name'`
:   Name of the object for which data lineage information is retrieved. Use the fully qualified name if the object is in a
    schema different from the current schema in the session.

`'object_domain'`
:   The domain of the object. Supported domains are ‘COLUMN’, ‘TABLE’ (which includes all table-like objects including
    views and dynamic tables), ‘SEMANTIC_VIEW’ (for [semantic views](../../user-guide/views-semantic/overview.md)), and ‘STAGE’.

    For ML lineage, use `TABLE` for feature views (which are dynamic tables and views internally), ‘DATASET’, or ‘MODULE’ for
    models.

`'direction'`
:   The direction for which the lineage should be retained. Supported directions are ‘UPSTREAM’ and ‘DOWNSTREAM’.

**Optional:**

`distance`
:   The number of levels of lineage to retrieve. The maximum is 5; this is also the default.

`'object_version'`
:   For versioned objects, such as datasets and models, the version of the object for which lineage is retrieved. If not
    specified, the default version is used.

## Output

The output is a table with one row per object relationship in the lineage path (that is, an edge in the lineage graph).
Relationships are between objects designated as source and target in each row. The table includes the following columns:

| Column | Type | Description |
| --- | --- | --- |
| `SOURCE_OBJECT_DATABASE` | VARCHAR | The database that contains the source object. |
| `SOURCE_OBJECT_SCHEMA` | VARCHAR | The schema that contains the source object. |
| `SOURCE_OBJECT_NAME` | VARCHAR | The unqualified name of the source object. |
| `SOURCE_OBJECT_DOMAIN` | VARCHAR | The domain of the target object. Possible values are ‘COLUMN’, ‘TABLE’, ‘SEMANTIC_VIEW’, ‘DATASET’, ‘MODULE’ (for ML models), and ‘STAGE’. |
| `SOURCE_OBJECT_VERSION` | VARCHAR | The version of the source object, for versioned objects such as datasets and models. NULL if the source object is not versioned. |
| `SOURCE_COLUMN_NAME` | VARCHAR | The name of the source column, if the source object is a column. NULL if the source object is not a column. |
| `SOURCE_STATUS` | VARCHAR | The status of the source object. Possible values are ‘ACTIVE’ and ‘MASKED’. |
| `TARGET_OBJECT_DATABASE` | VARCHAR | The database that contains the target object. |
| `TARGET_OBJECT_SCHEMA` | VARCHAR | The schema that contains the target object. |
| `TARGET_OBJECT_NAME` | VARCHAR | The unqualified name of the target object. |
| `TARGET_OBJECT_DOMAIN` | VARCHAR | The domain of the target object. Possible values are ‘COLUMN’, ‘TABLE’, ‘SEMANTIC_VIEW’, ‘DATASET’, ‘MODULE’ (for ML models), and ‘STAGE’. |
| `TARGET_OBJECT_VERSION` | VARCHAR | The version of the target object, for versioned objects such as datasets and models. NULL if the target object is not versioned. |
| `TARGET_COLUMN_NAME` | VARCHAR | The name of the target column, if the target object is a column. NULL if the target object is not a column. |
| `TARGET_STATUS` | VARCHAR | The status of the target object. Possible values are ‘ACTIVE’ and ‘MASKED’. |
| `DISTANCE` | INTEGER | The distance of the target object from the source object in the lineage path. A direct relationship has a distance of 1. |
| `PROCESS` | VARIANT | Provides details about how lineage between the source object and target object was established. For example, it might include the query ID of a SQL query or the name of a stored procedure that moved data from the source object to the target object. |

## Usage notes

* You will receive an error message if the object does not exist, if the object is not accessible to the current user,
  if the object does not support data lineage, or if the object is not in the specified domain.
* The output table contains no rows if no lineage information is available for the specified object; this is not an error.
* `GET_LINEAGE` returns at most 10 million rows, each row representing an edge (relationship) in the lineage graph.
  If there are more than 10 million rows in the output, the function silently truncates output to 10 million rows.
* For limitations and considerations that apply to using this function, see
  [Lineage limitations and considerations](../../user-guide/ui-snowsight-lineage.md).

## Example

Assume you have created a table named TABLE_B from TABLE_A using CREATE TABLE AS SELECT, then created a table named
TABLE_C from TABLE_B in a similar manner. The following SQL query retrieves two steps of downstream lineage from
TABLE_A:

```sqlexample
SELECT
    DISTANCE,
    SOURCE_OBJECT_DOMAIN,
    SOURCE_OBJECT_DATABASE,
    SOURCE_OBJECT_SCHEMA,
    SOURCE_OBJECT_NAME,
    SOURCE_STATUS,
    TARGET_OBJECT_DOMAIN,
    TARGET_OBJECT_DATABASE,
    TARGET_OBJECT_SCHEMA,
    TARGET_OBJECT_NAME,
    TARGET_STATUS,
FROM TABLE (SNOWFLAKE.CORE.GET_LINEAGE('my_database.sch.table_a', 'TABLE', 'DOWNSTREAM', 2));
```

The output is similar to the following:

```output
+----------+----------------------+------------------------+----------------------+--------------------+---------------+----------------------+------------------------+----------------------+--------------------+---------------+
| DISTANCE | SOURCE_OBJECT_DOMAIN | SOURCE_OBJECT_DATABASE | SOURCE_OBJECT_SCHEMA | SOURCE_OBJECT_NAME | SOURCE_STATUS | TARGET_OBJECT_DOMAIN | TARGET_OBJECT_DATABASE | TARGET_OBJECT_SCHEMA | TARGET_OBJECT_NAME | TARGET_STATUS |
|----------+----------------------+------------------------+----------------------+--------------------+---------------+----------------------+------------------------+----------------------+--------------------+---------------|
|        1 | TABLE                | MY_DATABASE            | SCH                  | TABLE_A            | ACTIVE        | TABLE                | MY_DATABASE            | SCH                  | TABLE_B            | ACTIVE        |
|        2 | TABLE                | MY_DATABASE            | SCH                  | TABLE_B            | ACTIVE        | TABLE                | MY_DATABASE            | SCH                  | TABLE_C            | ACTIVE        |
+----------+----------------------+------------------------+----------------------+--------------------+---------------+----------------------+------------------------+----------------------+--------------------+---------------+
```
