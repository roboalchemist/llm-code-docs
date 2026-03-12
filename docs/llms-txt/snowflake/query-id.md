# Source: https://docs.snowflake.com/en/developer-guide/snowflake-scripting/query-id.md

# Getting the query ID of the last query

If you need to access the query ID of the last query that was executed, use the global variable SQLID.

> **Note:**
>
> If no query was executed, the default value of SQLID is NULL.

The following example executes two queries and returns an ARRAY containing the query IDs:

```sqlexample
DECLARE
  query_id_1 VARCHAR;
  query_id_2 VARCHAR;
BEGIN
  SELECT 1;
  query_id_1 := SQLID;
  SELECT 2;
  query_id_2 := SQLID;
  RETURN [query_id_1, query_id_2];
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  query_id_1 VARCHAR;
  query_id_2 VARCHAR;
BEGIN
  SELECT 1;
  query_id_1 := SQLID;
  SELECT 2;
  query_id_2 := SQLID;
  RETURN [query_id_1, query_id_2];
END;
$$
;
```
