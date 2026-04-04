# Source: https://docs.snowflake.com/en/sql-reference/functions-metadata.md

# Metadata functions

Snowflake provides functions that return metadata information, such as descriptions of the statements used to create database
objects (e.g. tables).

| Function Name | Notes |
| --- | --- |
| [GENERATE_COLUMN_DESCRIPTION](functions/generate_column_description.md) | Generate a list of columns from a set of staged files that contain [semi-structured data](../user-guide/semistructured-intro.md). |
| [GET_DDL](functions/get_ddl.md) | Get DDL to [re-]create a database object. |
