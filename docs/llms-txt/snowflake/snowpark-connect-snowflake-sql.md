# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-connect-snowflake-sql.md

# Executing Snowflake SQL with Snowpark Connect for Spark

To execute SQL commands specific to Snowflake, you can use the `SnowflakeSession` interface. As with the `spark.sql` method,
query results are returned as Spark DataFrames with which you can continue applying or chaining Spark DataFrame transformations and
actions on the resulting data.

With most SQL operations, you can use the `spark.sql` method to execute SQL statements directly and retrieve the results as Spark
DataFrames. However, some parts of Snowflake SQL syntax—including QUALIFY, CONNECT BY, LATERAL FLATTEN, and time travel queries—are
not compatible with Spark SQL.

The following example shows how to use `SnowflakeSession` to execute a Snowflake SQL command that includes the CONNECT BY clause.

```python
import snowflake.snowpark_connect
from snowflake.snowpark_connect.snowflake_session import SnowflakeSession

spark = snowflake.snowpark_connect.init_spark_session()
snowflake_session = SnowflakeSession(spark)
result_df = snowflake_session.sql("""
  SELECT
  employee_name,
  manager_name,
  LEVEL
FROM employees
START WITH employee_name = 'Alice'
CONNECT BY PRIOR manager_name = employee_name
""").show()
result_df.limit(1).show()
```

You can also use the `SnowflakeSession` interface to execute configuration directives specific to Snowflake. These directives
include setting session-level parameters such as the active database, schema, or warehouse.

The following example shows how to use `SnowflakeSession` to set session-level parameters.

```python
import snowflake.snowpark_connect
from snowflake.snowpark_connect.client import SnowflakeSession

spark = snowflake.snowpark_connect.init_spark_session()
snowflake_session = SnowflakeSession(spark)

snowflake_session.use_database("MY_DATABASE")
snowflake_session.use_schema("MY_SCHEMA")
snowflake_session.use_warehouse("MY_WH")
snowflake_session.use_role("PUBLIC")
```
