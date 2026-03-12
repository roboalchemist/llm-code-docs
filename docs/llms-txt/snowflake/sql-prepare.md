# Source: https://docs.snowflake.com/en/user-guide/sql-prepare.md

# SQL Statements Supported for Preparation

Some drivers and connectors support the ability to send a SQL statement for preparation before execution. Snowflake supports
preparation for the following types of SQL statements:

* [SELECT](../sql-reference/sql/select.md)
* [Data Manipulation Language (DML) commands](../sql-reference/sql-dml.md)
* [SHOW <objects>](../sql-reference/sql/show.md)

Note that if a driver or connector sends other types of SQL statements for preparation, those statements will not be prepared. For
example, if you send a DDL statement for preparation and execution, Snowflake just executes the statement without preparing it.
