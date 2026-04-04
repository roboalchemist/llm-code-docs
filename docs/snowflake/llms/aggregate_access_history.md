# Source: https://docs.snowflake.com/en/sql-reference/account-usage/aggregate_access_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# AGGREGATE_ACCESS_HISTORY view

This Account Usage view provides aggregated [Access History](../../user-guide/access-history.md) for all workloads in Snowflake.
When a workload involves highly recurrent transactional queries, the access pattern of those queries is also frequently repeated. It is more efficient to view such access history information in an aggregation.

The AGGREGATE_ACCESS_HISTORY view contains similar data to the
[ACCESS_HISTORY view](access_history.md), aggregated over time for
repeated queries in one-minute intervals.

This view also provides access history information associated with both
analytical and transactional queries. In contrast, note that the
[ACCESS_HISTORY view](access_history.md) contains access history
information associated only with queries that appear in the
[QUERY_HISTORY view](query_history.md), and does not include
certain short-running transactional queries.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| INTERVAL_START_TIME | TIMESTAMP_LTZ | Start time of the window of measurement. |
| INTERVAL_END_TIME | TIMESTAMP_LTZ | End time of the window of measurement. |
| QUERY_PARAMETERIZED_HASH | TEXT | Unique ID to identify identical parameterized queries. See [QUERY_PARAMETERIZED_HASH column](aggregate_query_history.md). |
| USER_NAME | TEXT | User who issued the query. |
| CALLS | NUMBER | The number of times the access behavior occurred during the window of time specified by INTERVAL_START_TIME and INTERVAL_END_TIME and triggered by a specific parameterized query and user. |
| DIRECT_OBJECTS_ACCESSED | ARRAY | A JSON array of data objects such as user-defined functions (i.e. UDFs and UDTFs), stored procedures, tables, views, and columns directly named in the query explicitly or through shortcuts such as using an asterisk (i.e. `*`).  Virtual columns can be returned in this field.  For additional notes about UDFs, see [Usage notes](access_history.md). |
| BASE_OBJECTS_ACCESSED | ARRAY | A JSON array of all base data objects to execute a query, including columns, external functions, UDFs, and stored procedures.  In the example in [ACCESS_HISTORY view](access_history.md), the fields in the first array specify a UDF. These same fields in the first array also specify a stored procedure, when applicable.  Note the following:   * This field specifies view names or view columns, including virtual columns, if a shared view is accessed in a data sharing consumer   account.   For additional notes about UDFs, see [Usage notes](access_history.md). |
| OBJECTS_MODIFIED | ARRAY | A JSON array that specifies the objects that were associated with a write operation in the query.  The UDF and stored procedure array is the same as what appears in the arrays for `baseSources` and `directSources` in the examples in [ACCESS_HISTORY view](access_history.md), depending on how the access took place. For brevity, the example omits the UDF and stored procedure array  For additional notes about UDFs, see [Usage notes](access_history.md). |
| OBJECT_MODIFIED_BY_DDL | OBJECT | Specifies the DDL operation on a database, schema, table, view, and column. These operations also include statements that specify a row access policy on a table or view, a masking policy on a column, and tag updates (e.g. set a tag, change a tag value) on the object or column. |
| POLICIES_REFERENCED | ARRAY | Specifies information about the enforced masking policy set on the column and the enforced row access policy set on the table, including policies set on intermediate objects or columns. |

The fields in the JSON array for the DIRECT_OBJECTS_ACCESSED, BASE_OBJECTS_ACCESSED, OBJECTS_MODIFIED, and POLICIES_REFERENCED columns are
described below.

| Field | Data Type | Description |
| --- | --- | --- |
| columnId | NUMBER | A column ID that is unique within the account. This value is identical to the value in the `column_id` column in the [COLUMNS](columns.md) view. |
| columnName | TEXT | The name of the accessed column. For policies, specifies the column on which the masking policy is set. |
| objectId | NUMBER | An identifier for the object, which is unique within a given account and domain. This number will match:   *The value in the `TABLE_ID` column in the [TABLE](tables.md), [VIEWS](views.md),   and [MATERIALIZED_VIEW_REFRESH_HISTORY](materialized_view_refresh_history.md) views.* If a stage was accessed, this number will match the:    + `NAME` identifier for a [user](users.md) (User stage).   + `TABLE_ID` number for a [table](tables.md) (Table stage).   + `STAGE_ID` number for a [stage](stages.md) (Named stage). |
| objectName | TEXT | The fully qualified name of the object that was accessed.  If a masking policy is set on a column or a row access policy is set on a table or view, the value refers to the fully qualified name of the table or view on which the row access policy is set or the table or view that has a masking policy set on one of its columns.  If a stage was accessed, this value will be the:   *`username` (User stage).* `table_name` (Table stage). * `stage_name` (Named stage). |
| objectDomain | TEXT | One of the following: `EXTERNAL TABLE`, `FUNCTION`, `MATERIALIZED VIEW`, `PROCEDURE`, `STAGE`, `STREAM`, or `VIEW`.  Note that `FUNCTION` specifies UDFs, UDTFs, and external functions.  For policies, specifies the domain of the object on which the row access policy is set. |
| location | TEXT | The URL of the external location when data is accessed from an external location (for example, `s3://mybucket/a.csv`).  If the query does not access a stage, this field is omitted. |
| stageKind | TEXT | When writing to a stage, one of the following: `Table`, `User`, `Internal Named`, or `External Named`.  If the query does not access a stage, this field is omitted. |
| baseSources | TEXT | The columns that serve as the source columns for the columns specified by `directSources`. These columns facilitate column lineage. |
| directSources | TEXT | The columns specifically mentioned in the data write portion of the SQL statement that serves as the source columns in the target table to which data is written. These columns facilitate column lineage. |
| policyName | TEXT | The fully-qualified name of the policy. |
| policyId | NUMBER | An identifier for the policy, which is unique within a given account and domain. This value matches the identifier for a masking policy in the [MASKING_POLICIES view](masking_policies.md) or the identifier for a row access policy in the [ROW_ACCESS_POLICIES view](row_access_policies.md) |
| policyKind | TEXT | Either: MASKING_POLICY or ROW_ACCESS_POLICY |
| argumentSignature | TEXT | The name and data type for each argument in the UDF or stored procedure. |
| dataType |  | The data type of the return value for a UDF or stored procedure.  This value helps to differentiate two or more UDFs that have the same name but different return types. |

The fields for the OBJECT_MODIFIED_BY_DDL column are described below.

| Field | Data type | Description |
| --- | --- | --- |
| objectDomain | TEXT | The domain of the object defined or modified by the DDL operation, which includes [all objects that can be tagged](../../user-guide/object-tagging/introduction.md) and `MASKING POLICY`, `ROW ACCESS POLICY`, and `TAG`. |
| objectId | NUMBER | The identifier for the object, which is unique within a given account and domain, defined or modified by the DDL operation. |
| objectName | TEXT | The fully qualified name of the object defined or modified by the DDL operation. |
| operationType | TEXT | The SQL keyword that specifies the operation on the table, view, or column: `ALTER`, `CREATE`, `DROP`, `REPLACE`, or `UNDROP`. |
| properties | ARRAY | A JSON array that specifies the object or column properties when you create, modify, drop, or undrop the object or column. There are two types of properties: atomic and compound. |

For the `properties` field:

* Atomic: one value per property (e.g. a `comment` has a single string value, the `enabled` property is a boolean and has one value).
* Compound: the property is multi-valued (e.g. `allowed_values` for a tag, masking policy).

Compound properties are recorded in a JSON array. For example, if a table contains a single column named EMAIL, the column is recorded as
follows:

```sqljson
columns: {
  "email": {
    objectId: {
      "value": 1
    },
    "subOperationType": "ADD"
  }
}
```

The `subOperationType` value can be one of the following:

* `ADD` specifies adding a compound property (e.g. add a column, set allowed values).
* `DROP` specifies removing a compound property.
* `ALTER` specifies modifying a compound property.

The `objectId` specifies the identifier for the column or object, except for allowed tag values which do not have an
identifier.

## Usage notes

* Latency for the view may be up to 180 minutes (3 hours).
* This Account Usage view can be used to query the aggregated access history of Snowflake objects (e.g. table, view, column) within the last 365 days (1 year).
