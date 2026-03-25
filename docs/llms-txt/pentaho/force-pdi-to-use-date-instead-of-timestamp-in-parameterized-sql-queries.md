# Source: https://docs.pentaho.com/pdia-data-integration/data-integration-issues/troubleshooting-database-connections/force-pdi-to-use-date-instead-of-timestamp-in-parameterized-sql-queries.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-issues/troubleshooting-database-connections/force-pdi-to-use-date-instead-of-timestamp-in-parameterized-sql-queries.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-issues/troubleshooting-database-connections/force-pdi-to-use-date-instead-of-timestamp-in-parameterized-sql-queries.md

# Force PDI to use DATE instead of TIMESTAMP in Parameterized SQL queries

If your query optimizer is incorrectly using the predicate **TIMESTAMP**, it is because the JDBC driver/database converts the data type from a **TIMESTAMP** to a **DATE**. In certain circumstances, this casting prevents the query optimizer of the database from using the correct index. For example, Oracle might state that it cannot use the index, and generates the following error message:

```
The predicate DATE used at line ID 1 of the execution plan contains an implicit
   data type conversion on indexed column DATE. This implicit data type conversion prevents
   the optimizer from selecting indices on table A.
```

To resolve this issue, use a Select Values step and set **Precision** to`1` and **Value** to `DATE`. These changes force the parameter to be set as a **DATE** instead of a **TIMESTAMP**.
